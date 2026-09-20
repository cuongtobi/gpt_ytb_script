#!/usr/bin/env python3
"""Deterministic verifier for v3.2 proof-carrying integrity artifacts."""

import argparse
import json
import re
import sys
from pathlib import Path

TERMINALS = ".!?…"
CLOSERS = '"”’\')]}»'
CATEGORY_KEYS = {
    "technical_scientific",
    "acronyms_symbols",
    "abstract_processes",
    "classifications",
    "evidence_methods",
    "measurements_quantities",
    "historical_institutional",
    "specialized_common_words",
    "aliases_relations",
    "mechanisms",
}


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def sid_num(sid):
    m = re.fullmatch(r"S(\d+)", sid or "")
    return int(m.group(1)) if m else None


def canonical_units(markdown_text):
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


def blind_candidates(blind):
    out = {}
    for rec in blind.get("lexical_candidates", []):
        if not isinstance(rec, dict):
            continue
        cid = rec.get("candidate_id") or rec.get("id")
        phrase = rec.get("exact_phrase") or rec.get("phrase")
        if cid:
            out[cid] = {"phrase": phrase, "record": rec}
    return out


def review_shape_ok(review):
    return isinstance(review, dict) and CATEGORY_KEYS.issubset(set(review.keys())) and all(
        isinstance(review.get(k), list) for k in CATEGORY_KEYS
    )


def actual_first_sentence_id(phrase, computed):
    if not phrase:
        return None
    for i, (_, text) in enumerate(computed, start=1):
        if re.search(re.escape(phrase), text, flags=re.IGNORECASE):
            return f"S{i:04d}"
    return None


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

    computed = canonical_units(script_text)
    indexed = idx.get("units", [])
    expected_ids = [f"S{i:04d}" for i in range(1, len(computed) + 1)]
    index_ids = [u.get("sentence_id") for u in indexed]

    if index_ids != expected_ids:
        errors.append("canonical index IDs do not match recomputed script")
    if len(indexed) != len(computed):
        errors.append("canonical index count differs from recomputed script")
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

    ledger = blind.get("sentence_ledger", [])
    ledger_ids = [r.get("sentence_id") for r in ledger]
    if ledger_ids != expected_ids:
        errors.append("10B1 ledger does not cover every canonical sentence exactly once")

    for row in ledger:
        sid = row.get("sentence_id")
        if not review_shape_ok(row.get("forward_review")):
            errors.append(f"incomplete forward category matrix at {sid}")
        if not review_shape_ok(row.get("reverse_review")):
            errors.append(f"incomplete reverse category matrix at {sid}")
        if not isinstance(row.get("lexical_candidate_ids"), list):
            errors.append(f"lexical_candidate_ids missing/not list at {sid}")

    candidates = blind_candidates(blind)
    discovered = set(candidates.keys())
    if len(discovered) != len(blind.get("lexical_candidates", [])):
        errors.append("duplicate or malformed lexical candidate IDs in 10B1")

    # Candidate first-use claims must match actual first occurrence of exact phrase.
    for cid, item in candidates.items():
        phrase = item["phrase"]
        declared = item["record"].get("first_use_sentence_id")
        actual = actual_first_sentence_id(phrase, computed)
        if not phrase:
            errors.append(f"missing exact_phrase for {cid}")
        elif actual is None:
            errors.append(f"exact_phrase for {cid} does not occur in script")
        elif declared != actual:
            errors.append(f"10B1 first_use_sentence_id mismatch for {cid}: declared {declared}, actual {actual}")

    proof = integ.get("candidate_conservation_proof", {})
    declared_discovered = set(proof.get("discovered_candidate_ids", []))
    if declared_discovered != discovered:
        errors.append("10C discovered candidate IDs differ from 10B1")

    dispositions = proof.get("dispositions", {})
    if set(dispositions.keys()) != discovered:
        errors.append("disposition IDs do not equal 10B1 discovered IDs")

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
                errors.append(f"missing BASELINE_KNOWN provenance for {cid}")

    if sum(counts.values()) != len(discovered):
        errors.append("candidate conservation arithmetic mismatch")
    if counts["UNRESOLVED"] != 0:
        errors.append("unresolved candidates remain")

    temporal = integ.get("temporal_proofs", [])
    by_cid = {r.get("candidate_id"): r for r in temporal}

    for cid, rec in dispositions.items():
        state = rec.get("status")
        phrase = candidates.get(cid, {}).get("phrase")
        actual_first = actual_first_sentence_id(phrase, computed)

        if state in {"REPLACED", "REMOVED"}:
            if phrase and actual_first is not None:
                errors.append(f"{state} candidate phrase still appears in final script: {cid}")
            continue

        tr = by_cid.get(cid)
        if not tr:
            errors.append(f"missing temporal proof for {cid}")
            continue

        if tr.get("first_use_sentence_id") != actual_first:
            errors.append(f"temporal proof first-use does not match actual occurrence for {cid}")

        mode = tr.get("grounding_mode")
        if mode == "BASELINE":
            if state != "BASELINE_KNOWN":
                errors.append(f"BASELINE temporal mode inconsistent for {cid}")
            continue

        first = sid_num(actual_first)
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
