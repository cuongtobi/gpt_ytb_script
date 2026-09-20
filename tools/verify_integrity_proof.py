#!/usr/bin/env python3
"""Deterministic verifier for v3.2 proof-carrying integrity artifacts."""

import argparse
import json
import re
import sys
from pathlib import Path


TERMINALS = ".!?…"
CLOSERS = '"”’\')]}»'


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def sid_num(sid):
    m = re.fullmatch(r"S(\d+)", sid or "")
    return int(m.group(1)) if m else None


def canonical_units(markdown_text):
    """Return exact narration units using the v3.2 canonical segmentation rule."""
    units = []
    current_heading = ""
    for raw_line in markdown_text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("#"):
            current_heading = line.lstrip("#").strip()
            continue

        start = 0
        i = 0
        n = len(line)
        while i < n:
            ch = line[i]
            boundary = False
            if ch in TERMINALS:
                if ch == "." and i > 0 and i + 1 < n and line[i - 1].isdigit() and line[i + 1].isdigit():
                    boundary = False
                else:
                    j = i + 1
                    while j < n and line[j] in CLOSERS:
                        j += 1
                    if j == n or line[j].isspace():
                        boundary = True
            if boundary:
                j = i + 1
                while j < n and line[j] in CLOSERS:
                    j += 1
                text = line[start:j].strip()
                if text:
                    units.append((current_heading, text))
                while j < n and line[j].isspace():
                    j += 1
                start = j
                i = j
                continue
            i += 1

        tail = line[start:].strip()
        if tail:
            units.append((current_heading, tail))
    return units


def blind_candidate_ids(blind):
    out = []
    for rec in blind.get("lexical_candidates", []):
        if isinstance(rec, str):
            out.append(rec)
        elif isinstance(rec, dict):
            cid = rec.get("candidate_id") or rec.get("id")
            if cid:
                out.append(cid)
    return out


def candidate_phrase_map(blind):
    out = {}
    for rec in blind.get("lexical_candidates", []):
        if isinstance(rec, dict):
            cid = rec.get("candidate_id") or rec.get("id")
            phrase = rec.get("exact_phrase") or rec.get("phrase")
            if cid and phrase:
                out[cid] = phrase
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--script", required=True)
    ap.add_argument("--index", required=True)
    ap.add_argument("--blind", required=True)
    ap.add_argument("--integrity", required=True)
    ap.add_argument("--isolation", required=True)
    args = ap.parse_args()

    script_text = Path(args.script).read_text(encoding="utf-8")
    idx = load_json(args.index)
    blind = load_json(args.blind)
    integ = load_json(args.integrity)
    isolation = load_json(args.isolation)
    errors = []

    # 1. Recompute canonical units from the real script.
    computed = canonical_units(script_text)
    indexed = idx.get("units", [])
    expected_ids = [f"S{i:04d}" for i in range(1, len(computed) + 1)]
    index_ids = [u.get("sentence_id") for u in indexed]

    if index_ids != expected_ids:
        errors.append("canonical index sentence IDs are not exact sequential IDs for recomputed script")
    if len(indexed) != len(computed):
        errors.append("canonical index unit count differs from recomputed script")
    else:
        for pos, ((heading, text), rec) in enumerate(zip(computed, indexed), start=1):
            if rec.get("exact_text") != text:
                errors.append(f"sentence text mismatch at S{pos:04d}")
            if rec.get("section_heading", "") != heading:
                errors.append(f"section heading mismatch at S{pos:04d}")

    if idx.get("source_sentence_count") != len(computed):
        errors.append("source_sentence_count differs from recomputed script")
    if idx.get("indexed_sentence_count") != len(indexed):
        errors.append("indexed_sentence_count differs from index units")

    # 2. Blind sentence-ledger coverage.
    ledger = blind.get("sentence_ledger", [])
    ledger_ids = [r.get("sentence_id") for r in ledger]
    if ledger_ids != expected_ids:
        errors.append("10B1 ledger does not cover every canonical sentence exactly once")

    # 3. Candidate conservation uses discovered IDs directly from 10B1.
    discovered_list = blind_candidate_ids(blind)
    if len(discovered_list) != len(set(discovered_list)):
        errors.append("duplicate lexical candidate IDs in 10B1")
    discovered = set(discovered_list)

    proof = integ.get("candidate_conservation_proof", {})
    declared_discovered = set(proof.get("discovered_candidate_ids", []))
    if declared_discovered != discovered:
        errors.append("10C discovered candidate IDs differ from 10B1 lexical candidate IDs")

    dispositions = proof.get("dispositions", {})
    disposition_ids = set(dispositions.keys())
    if disposition_ids != discovered:
        errors.append("disposition candidate IDs do not equal 10B1 discovered IDs")

    allowed = {"BASELINE_KNOWN", "GROUNDED", "REPLACED", "REMOVED", "UNRESOLVED"}
    counts = {k: 0 for k in allowed}
    for cid, rec in dispositions.items():
        state = rec.get("status")
        if state not in allowed:
            errors.append(f"invalid disposition for {cid}: {state}")
            continue
        counts[state] += 1
        if state == "BASELINE_KNOWN":
            prov = rec.get("baseline_provenance") or {}
            if prov.get("baseline_source_type") not in {"assumed_known", "normal_language_primitive"}:
                errors.append(f"invalid BASELINE_KNOWN source type for {cid}")
            if not prov.get("baseline_source_id_or_exact_entry"):
                errors.append(f"missing BASELINE_KNOWN provenance entry for {cid}")

    if sum(counts.values()) != len(discovered):
        errors.append("candidate conservation arithmetic mismatch")
    if counts["UNRESOLVED"] != 0:
        errors.append("unresolved candidates remain")

    # 4. Temporal proofs.
    temporal = integ.get("temporal_proofs", [])
    by_cid = {r.get("candidate_id"): r for r in temporal}
    phrases = candidate_phrase_map(blind)

    for cid, rec in dispositions.items():
        state = rec.get("status")
        if state in {"REPLACED", "REMOVED"}:
            phrase = phrases.get(cid)
            if phrase and re.search(re.escape(phrase), script_text, flags=re.IGNORECASE):
                errors.append(f"{state} candidate phrase still appears in final script: {cid}")
            continue

        tr = by_cid.get(cid)
        if not tr:
            errors.append(f"missing temporal proof for {cid}")
            continue

        mode = tr.get("grounding_mode")
        first = sid_num(tr.get("first_use_sentence_id"))

        if mode == "BASELINE":
            if state != "BASELINE_KNOWN":
                errors.append(f"BASELINE temporal mode inconsistent for {cid}")
            continue

        ground = sid_num(tr.get("grounding_sentence_id"))
        if first is None or ground is None:
            errors.append(f"invalid temporal coordinates for {cid}")
            continue
        if mode == "PRIOR" and not (ground < first):
            errors.append(f"PRIOR ordering invalid for {cid}")
        elif mode == "INLINE" and not (ground == first):
            errors.append(f"INLINE ordering invalid for {cid}")
        elif mode not in {"PRIOR", "INLINE"}:
            errors.append(f"invalid temporal mode for retained candidate {cid}: {mode}")

    # 5. Isolation manifest.
    isolation_verified = isolation.get("isolation_status") == "VERIFIED"
    if isolation.get("manifest_origin") != "runtime":
        isolation_verified = False
    if not isolation.get("attestation_source"):
        isolation_verified = False

    audits = isolation.get("audits", {})
    exec_ids = []
    for name in ("10B1", "10B2", "10B3"):
        rec = audits.get(name, {})
        allowed_inputs = set(rec.get("allowed_input_files", []))
        observed = set(rec.get("observed_input_files", []))
        forbidden = set(rec.get("forbidden_input_files", []))
        if rec.get("context_mode") != "fresh":
            isolation_verified = False
        if rec.get("runtime_attested") is not True:
            isolation_verified = False
        if rec.get("forbidden_input_accessed") is not False:
            isolation_verified = False
        if not observed.issubset(allowed_inputs):
            isolation_verified = False
        if observed.intersection(forbidden):
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
            "PASS_VERIFIED"
            if not errors and isolation_verified
            else "CONTENT_PASS_ISOLATION_NOT_VERIFIED"
            if not errors
            else "FAIL"
        ),
        "recomputed_sentence_count": len(computed),
        "discovered_candidate_count": len(discovered),
        "disposition_counts": counts,
        "errors": errors,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
