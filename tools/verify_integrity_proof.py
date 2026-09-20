#!/usr/bin/env python3
"""Deterministic verifier for v3.2 integrity proof artifacts.

Stdlib only. It verifies arithmetic/ID proofs and sentence-ledger coverage.
Isolation is accepted only when runtime manifest explicitly attests distinct
fresh contexts; this script cannot independently prove model-context isolation.
"""

import argparse
import json
import re
import sys
from pathlib import Path


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def sid_num(sid):
    m = re.fullmatch(r"S(\d+)", sid or "")
    return int(m.group(1)) if m else None


def fail(errors, msg):
    errors.append(msg)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--index", required=True)
    ap.add_argument("--blind", required=True)
    ap.add_argument("--integrity", required=True)
    ap.add_argument("--isolation", required=True)
    args = ap.parse_args()

    idx = load_json(args.index)
    blind = load_json(args.blind)
    integ = load_json(args.integrity)
    isolation = load_json(args.isolation)
    errors = []

    # Sentence index
    units = idx.get("units", [])
    index_ids = [u.get("sentence_id") for u in units]
    if len(index_ids) != len(set(index_ids)):
        fail(errors, "duplicate sentence IDs in canonical index")
    if idx.get("indexed_sentence_count") != len(units):
        fail(errors, "indexed_sentence_count mismatch")
    if idx.get("source_sentence_count") != len(units):
        fail(errors, "source_sentence_count mismatch")
    if idx.get("reconstruction_ok") is not True:
        fail(errors, "canonical index reconstruction_ok is not true")

    # Blind ledger coverage
    ledger = blind.get("sentence_ledger", [])
    ledger_ids = [r.get("sentence_id") for r in ledger]
    if index_ids != ledger_ids:
        fail(errors, "10B1 sentence ledger does not exactly match canonical sentence ID sequence")
    if len(ledger_ids) != len(set(ledger_ids)):
        fail(errors, "duplicate sentence IDs in 10B1 ledger")

    # Candidate conservation
    proof = integ.get("candidate_conservation_proof", {})
    discovered = set(proof.get("discovered_candidate_ids", []))
    dispositions = proof.get("dispositions", {})
    disposition_ids = list(dispositions.keys())
    if set(disposition_ids) != discovered:
        fail(errors, "candidate disposition IDs do not equal discovered candidate IDs")
    if len(disposition_ids) != len(set(disposition_ids)):
        fail(errors, "duplicate candidate disposition IDs")
    allowed = {"BASELINE_KNOWN", "GROUNDED", "REPLACED", "REMOVED", "UNRESOLVED"}
    counts = {k: 0 for k in allowed}
    for cid, rec in dispositions.items():
        state = rec.get("status")
        if state not in allowed:
            fail(errors, f"invalid disposition for {cid}: {state}")
            continue
        counts[state] += 1
        if state == "BASELINE_KNOWN":
            prov = rec.get("baseline_provenance") or {}
            if not prov.get("baseline_source_type") or not prov.get("baseline_source_id_or_exact_entry"):
                fail(errors, f"missing BASELINE_KNOWN provenance for {cid}")
    if counts["UNRESOLVED"] != 0:
        fail(errors, "unresolved candidates remain")
    if sum(counts.values()) != len(discovered):
        fail(errors, "candidate conservation arithmetic mismatch")

    # Temporal proofs
    temporal = integ.get("temporal_proofs", [])
    by_cid = {r.get("candidate_id"): r for r in temporal}
    for cid, rec in dispositions.items():
        state = rec.get("status")
        if state in {"REPLACED", "REMOVED"}:
            continue
        if cid not in by_cid:
            fail(errors, f"missing temporal proof for {cid}")
            continue
        tr = by_cid[cid]
        mode = tr.get("grounding_mode")
        first = sid_num(tr.get("first_use_sentence_id"))
        if mode == "BASELINE":
            if state != "BASELINE_KNOWN":
                fail(errors, f"BASELINE temporal mode inconsistent for {cid}")
            continue
        ground = sid_num(tr.get("grounding_sentence_id"))
        if first is None or ground is None:
            fail(errors, f"invalid temporal coordinates for {cid}")
            continue
        if mode == "PRIOR" and not (ground < first):
            fail(errors, f"PRIOR ordering invalid for {cid}")
        if mode == "INLINE" and not (ground == first):
            fail(errors, f"INLINE ordering invalid for {cid}")
        if mode not in {"PRIOR", "INLINE"}:
            fail(errors, f"invalid grounding mode for retained candidate {cid}: {mode}")

    # Isolation manifest
    audits = isolation.get("audits", {})
    exec_ids = []
    isolation_verified = isolation.get("isolation_status") == "VERIFIED"
    for name in ("10B1", "10B2", "10B3"):
        rec = audits.get(name, {})
        if rec.get("context_mode") != "fresh":
            isolation_verified = False
        if rec.get("runtime_attested") is not True:
            isolation_verified = False
        if rec.get("forbidden_input_accessed") is not False:
            isolation_verified = False
        eid = rec.get("execution_id")
        if not eid:
            isolation_verified = False
        else:
            exec_ids.append(eid)
    if len(exec_ids) != 3 or len(set(exec_ids)) != 3:
        isolation_verified = False

    result = {
        "proof_verifier_status": "PASS" if not errors else "FAIL",
        "isolation_verified": isolation_verified,
        "project_status": (
            "PASS_VERIFIED" if not errors and isolation_verified
            else "CONTENT_PASS_ISOLATION_NOT_VERIFIED" if not errors
            else "FAIL"
        ),
        "errors": errors,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
