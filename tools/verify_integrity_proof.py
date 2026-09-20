#!/usr/bin/env python3
"""Deterministic verifier for v3.3 content-addressed full integrity.

When the v3.3-only arguments are omitted, the verifier keeps a compatibility
path for historical v3.2 regression fixtures.
"""

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    jsonschema = None

try:
    import yaml
except ImportError:
    yaml = None

KNOWLEDGE_KEYS = {
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

CLAIM_KEYS = {
    "empirical_fact",
    "dates_quantities",
    "causal_mechanism",
    "scope_population_geography",
    "comparison_superlative",
    "attribution_source",
    "uncertainty_model",
    "negative_absence_claim",
    "definition_classification",
    "historical_event",
}

NATURALNESS_KEYS = {
    "translationese",
    "academic_compression",
    "unnecessary_label",
    "alias_overload",
    "duplicate_explanation_or_reveal",
    "repeated_opening_or_fragment",
    "parallelism_overload",
    "rhetorical_question_overload",
    "awkward_terminology",
    "audio_density",
    "high_load_listening_block",
    "unclear_pronoun",
    "surface_error",
}

CLOSERS = '"”’\')]}»」』】》〉'
HASH_RE = re.compile(r"^[0-9a-f]{64}$")


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def sha256_file(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def sid_num(sid):
    m = re.fullmatch(r"S(\d+)", sid or "")
    return int(m.group(1)) if m else None


def terminals_for_locale(locale):
    base = set(".!?…")
    lang = (locale or "").lower().split("-")[0]
    if lang in {"ja", "zh", "ko"}:
        base.update("。！？｡")
    return base


def canonical_units(markdown_text, locale="en"):
    units = []
    current_heading = ""
    terminals = terminals_for_locale(locale)
    wide = set("。！？｡")

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
            if ch in terminals:
                if ch == "." and i > 0 and i + 1 < n and line[i - 1].isdigit() and line[i + 1].isdigit():
                    boundary = False
                else:
                    j = i + 1
                    while j < n and line[j] in CLOSERS:
                        j += 1
                    boundary = ch in wide or j == n or line[j].isspace()

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


def review_shape_ok(review, keys):
    return (
        isinstance(review, dict)
        and keys.issubset(set(review.keys()))
        and all(isinstance(review.get(k), list) for k in keys)
    )


def actual_first_sentence_id(phrase, computed):
    if not phrase:
        return None
    for i, (_, text) in enumerate(computed, start=1):
        if re.search(re.escape(phrase), text, flags=re.IGNORECASE):
            return f"S{i:04d}"
    return None


def safe_project_path(root, rel):
    p = Path(rel)
    if p.is_absolute() or ".." in p.parts:
        return None
    resolved = (root / p).resolve()
    try:
        resolved.relative_to(root.resolve())
    except ValueError:
        return None
    return resolved


def verify_content_address(obj, root, errors, label, counters=None):
    ca = obj.get("content_address") if isinstance(obj, dict) else None
    if not isinstance(ca, dict):
        errors.append(f"{label}: missing content_address")
        if counters is not None:
            counters["hash_failures"] += 1
        return {}

    if ca.get("hash_algorithm") != "sha256":
        errors.append(f"{label}: hash_algorithm must be sha256")
        if counters is not None:
            counters["hash_failures"] += 1

    inputs = ca.get("inputs")
    if not isinstance(inputs, list) or not inputs:
        errors.append(f"{label}: content_address.inputs missing/empty")
        if counters is not None:
            counters["hash_failures"] += 1
        return {}

    declared = {}
    for rec in inputs:
        if not isinstance(rec, dict):
            errors.append(f"{label}: malformed input hash record")
            if counters is not None:
                counters["hash_failures"] += 1
            continue
        rel = rec.get("path")
        digest = rec.get("sha256")
        if not isinstance(rel, str) or not HASH_RE.fullmatch(digest or ""):
            errors.append(f"{label}: invalid path/hash record")
            if counters is not None:
                counters["hash_failures"] += 1
            continue
        if rel in declared:
            errors.append(f"{label}: duplicate hashed input {rel}")
            if counters is not None:
                counters["hash_failures"] += 1
            continue
        p = safe_project_path(root, rel)
        if p is None or not p.exists():
            errors.append(f"{label}: hashed input missing/unsafe: {rel}")
            if counters is not None:
                counters["hash_failures"] += 1
            continue
        actual = sha256_file(p)
        if actual != digest:
            errors.append(f"{label}: input hash mismatch for {rel}")
            if counters is not None:
                counters["hash_failures"] += 1
        declared[rel] = digest
    return declared


def declared_script_hash(hash_map):
    for rel, digest in hash_map.items():
        if Path(rel).name in {"10_final_candidate.md", "10_final_script.md"}:
            return digest
    return None


def validate_schema(data, schema_path, errors, label, counters):
    if jsonschema is None:
        errors.append("jsonschema package unavailable")
        counters["schema_failures"] += 1
        return
    try:
        schema = load_json(schema_path)
        base_uri = schema_path.parent.resolve().as_uri() + "/"
        resolver = jsonschema.RefResolver(base_uri=base_uri, referrer=schema)
        validator = jsonschema.Draft202012Validator(schema, resolver=resolver)
        issues = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
        for issue in issues:
            loc = ".".join(str(x) for x in issue.path)
            errors.append(f"{label}: schema error at {loc or '<root>'}: {issue.message}")
            counters["schema_failures"] += 1
    except Exception as exc:
        errors.append(f"{label}: schema validation failed: {exc}")
        counters["schema_failures"] += 1


def validate_all_project_artifacts(root, schema_dir, errors, counters):
    mapping_path = schema_dir / "schema_manifest.json"
    if not mapping_path.exists():
        errors.append("schema manifest missing")
        counters["schema_failures"] += 1
        return
    mapping = load_json(mapping_path).get("artifacts", {})
    for rel, schema_name in mapping.items():
        if rel == "10d_proof_verification.json" and not (root / rel).exists():
            continue
        p = root / rel
        if not p.exists():
            errors.append(f"required v3.3 artifact missing: {rel}")
            counters["schema_failures"] += 1
            continue
        try:
            if p.suffix.lower() in {".yaml", ".yml"}:
                if yaml is None:
                    raise RuntimeError("PyYAML package unavailable")
                data = yaml.safe_load(p.read_text(encoding="utf-8"))
            else:
                data = load_json(p)
        except Exception as exc:
            errors.append(f"{rel}: parse failure: {exc}")
            counters["schema_failures"] += 1
            continue
        validate_schema(data, schema_dir / schema_name, errors, rel, counters)


def verify_manifest(manifest, root, errors, counters):
    if manifest.get("pipeline_version") != "3.3":
        errors.append("artifact manifest pipeline_version must be 3.3")
        counters["hash_failures"] += 1
    hashes = manifest.get("hashes")
    if not isinstance(hashes, dict) or not hashes:
        errors.append("artifact manifest hashes missing/empty")
        counters["hash_failures"] += 1
        return

    required = {
        "10_final_script.md",
        "10_final_sentence_index.json",
        "10b1_blind_knowledge_inventory.json",
        "10b2_blind_claim_inventory.json",
        "10b3_blind_naturalness_audit.json",
        "10_final_integrity.json",
        "10b_isolation_manifest.json",
        "02_sources.json",
        "02_evidence_ledger.json",
    }
    missing = required - set(hashes.keys())
    for rel in sorted(missing):
        errors.append(f"artifact manifest missing required hash: {rel}")
        counters["hash_failures"] += 1

    for rel, digest in hashes.items():
        if rel == "artifact_manifest.json":
            errors.append("artifact manifest must not self-hash")
            counters["hash_failures"] += 1
            continue
        if not HASH_RE.fullmatch(digest or ""):
            errors.append(f"artifact manifest invalid hash: {rel}")
            counters["hash_failures"] += 1
            continue
        p = safe_project_path(root, rel)
        if p is None or not p.exists():
            errors.append(f"artifact manifest path missing/unsafe: {rel}")
            counters["hash_failures"] += 1
            continue
        if sha256_file(p) != digest:
            errors.append(f"artifact manifest hash mismatch: {rel}")
            counters["hash_failures"] += 1


def verify_index(idx, computed, script_hash, errors, counters):
    expected_ids = [f"S{i:04d}" for i in range(1, len(computed) + 1)]
    indexed = idx.get("units", [])
    index_ids = [u.get("sentence_id") for u in indexed if isinstance(u, dict)]

    if idx.get("source_sha256") != script_hash:
        errors.append("final sentence index source_sha256 differs from released script")
        counters["stale_audit_failures"] += 1

    if index_ids != expected_ids:
        errors.append("canonical index IDs do not match recomputed script")
        counters["sentence_coverage_failures"] += 1

    if len(indexed) != len(computed):
        errors.append("canonical index count differs from recomputed script")
        counters["sentence_coverage_failures"] += 1
    else:
        for pos, ((heading, text), rec) in enumerate(zip(computed, indexed), start=1):
            if rec.get("exact_text") != text:
                errors.append(f"sentence text mismatch at S{pos:04d}")
                counters["sentence_coverage_failures"] += 1
            if rec.get("section_heading", "") != heading:
                errors.append(f"section heading mismatch at S{pos:04d}")
                counters["sentence_coverage_failures"] += 1

    if idx.get("source_sentence_count") != len(computed):
        errors.append("source_sentence_count differs from recomputed script")
        counters["sentence_coverage_failures"] += 1
    if idx.get("indexed_sentence_count") != len(indexed):
        errors.append("indexed_sentence_count differs from index units")
        counters["sentence_coverage_failures"] += 1
    return expected_ids


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


def verify_b1(blind, expected_ids, computed, integrity, errors, counters, hard):
    ledger = blind.get("sentence_ledger", [])
    ledger_ids = [r.get("sentence_id") for r in ledger if isinstance(r, dict)]
    if ledger_ids != expected_ids:
        errors.append("10B1 ledger does not cover every canonical sentence exactly once")
        counters["sentence_coverage_failures"] += 1

    union_ids = set()
    for row in ledger:
        sid = row.get("sentence_id")
        if not review_shape_ok(row.get("forward_review"), KNOWLEDGE_KEYS):
            errors.append(f"10B1 incomplete forward category matrix at {sid}")
            counters["sentence_coverage_failures"] += 1
        if not review_shape_ok(row.get("reverse_review"), KNOWLEDGE_KEYS):
            errors.append(f"10B1 incomplete reverse category matrix at {sid}")
            counters["sentence_coverage_failures"] += 1
        ids = row.get("lexical_candidate_ids")
        if not isinstance(ids, list):
            errors.append(f"10B1 lexical_candidate_ids missing/not list at {sid}")
            counters["sentence_coverage_failures"] += 1
        else:
            union_ids.update(ids)

    candidates = blind_candidates(blind)
    discovered = set(candidates)
    if len(discovered) != len(blind.get("lexical_candidates", [])):
        errors.append("duplicate or malformed lexical candidate IDs in 10B1")
        counters["candidate_conservation_failures"] += 1
    if union_ids != discovered:
        errors.append("10B1 ledger candidate union differs from lexical_candidates")
        counters["candidate_conservation_failures"] += 1

    for cid, item in candidates.items():
        phrase = item["phrase"]
        declared = item["record"].get("first_use_sentence_id")
        actual = actual_first_sentence_id(phrase, computed)
        if not phrase:
            errors.append(f"missing exact_phrase for {cid}")
            counters["candidate_conservation_failures"] += 1
        elif actual is None:
            errors.append(f"exact_phrase for {cid} does not occur in released script")
            counters["candidate_conservation_failures"] += 1
        elif declared != actual:
            errors.append(f"10B1 first_use mismatch for {cid}: declared {declared}, actual {actual}")
            counters["temporal_proof_failures"] += 1

    proof = integrity.get("candidate_conservation_proof", {})
    declared_discovered = set(proof.get("discovered_candidate_ids", []))
    dispositions = proof.get("dispositions", {})
    if declared_discovered != discovered:
        errors.append("knowledge conservation discovered IDs differ from 10B1")
        counters["candidate_conservation_failures"] += 1
    if set(dispositions.keys()) != discovered:
        errors.append("knowledge disposition IDs do not equal 10B1 candidate IDs")
        counters["candidate_conservation_failures"] += 1

    allowed = {"BASELINE_KNOWN", "GROUNDED", "REPLACED", "REMOVED", "UNRESOLVED"}
    state_counts = {k: 0 for k in allowed}
    unresolved_types = []

    for cid, rec in dispositions.items():
        state = rec.get("status")
        if state not in allowed:
            errors.append(f"invalid knowledge disposition for {cid}: {state}")
            counters["candidate_conservation_failures"] += 1
            continue
        state_counts[state] += 1
        if state == "BASELINE_KNOWN":
            prov = rec.get("baseline_provenance") or {}
            if prov.get("baseline_source_type") not in {"assumed_known", "normal_language_primitive"} or not prov.get("baseline_source_id_or_exact_entry"):
                errors.append(f"invalid BASELINE_KNOWN provenance for {cid}")
                hard["knowledge"]["invalid_baseline_provenance"] += 1
        if state == "UNRESOLVED":
            ctype = str(candidates.get(cid, {}).get("record", {}).get("candidate_type", "")).upper()
            unresolved_types.append(ctype)
        if state in {"REPLACED", "REMOVED"}:
            phrase = candidates.get(cid, {}).get("phrase")
            if phrase and actual_first_sentence_id(phrase, computed) is not None:
                errors.append(f"{state} knowledge candidate still appears in released script: {cid}")
                counters["candidate_conservation_failures"] += 1

    hard["knowledge"]["silently_ignored_candidates"] = len(discovered.symmetric_difference(set(dispositions.keys())))
    hard["knowledge"]["missing_discovered_nodes"] = hard["knowledge"]["silently_ignored_candidates"]
    hard["knowledge"]["unresolved_concepts"] = sum(1 for t in unresolved_types if "CONCEPT" in t or "PROCESS" in t or "MECHANISM" in t)
    hard["knowledge"]["unmapped_aliases"] = sum(1 for t in unresolved_types if "ALIAS" in t)
    hard["knowledge"]["core_entities_ungrounded"] = sum(1 for t in unresolved_types if "CORE" in t or "ENTITY" in t)
    hard["knowledge"]["unresolved_relations"] = sum(1 for t in unresolved_types if "RELATION" in t)
    hard["knowledge"]["unresolved_dependencies"] = sum(1 for t in unresolved_types if "DEPEND" in t)
    hard["knowledge"]["confusable_pairs_unresolved"] = sum(1 for t in unresolved_types if "CONFUS" in t)

    if state_counts["UNRESOLVED"]:
        errors.append("unresolved knowledge candidates remain")
        counters["candidate_conservation_failures"] += state_counts["UNRESOLVED"]

    temporal = integrity.get("temporal_proofs", [])
    by_cid = {r.get("candidate_id"): r for r in temporal if isinstance(r, dict)}
    temporal_failures = 0

    for cid, rec in dispositions.items():
        state = rec.get("status")
        if state in {"REPLACED", "REMOVED", "UNRESOLVED"}:
            continue
        phrase = candidates.get(cid, {}).get("phrase")
        actual_first = actual_first_sentence_id(phrase, computed)
        tr = by_cid.get(cid)
        if not tr:
            errors.append(f"missing temporal proof for {cid}")
            temporal_failures += 1
            continue
        if tr.get("first_use_sentence_id") != actual_first:
            errors.append(f"temporal proof first-use mismatch for {cid}")
            temporal_failures += 1
        mode = tr.get("grounding_mode")
        if mode == "BASELINE":
            if state != "BASELINE_KNOWN":
                errors.append(f"BASELINE temporal mode inconsistent for {cid}")
                temporal_failures += 1
            continue
        first = sid_num(actual_first)
        ground = sid_num(tr.get("grounding_sentence_id"))
        if first is None or ground is None:
            errors.append(f"invalid temporal coordinates for {cid}")
            temporal_failures += 1
        elif mode == "PRIOR" and not (ground < first):
            errors.append(f"PRIOR ordering invalid for {cid}")
            temporal_failures += 1
        elif mode == "INLINE" and not (ground == first):
            errors.append(f"INLINE ordering invalid for {cid}")
            temporal_failures += 1
        elif mode not in {"PRIOR", "INLINE"}:
            errors.append(f"invalid temporal mode for {cid}: {mode}")
            temporal_failures += 1

    counters["temporal_proof_failures"] += temporal_failures
    hard["knowledge"]["temporal_first_use_failures"] = temporal_failures
    return discovered, state_counts


def verify_b2(claims, expected_ids, indexed, integrity, evidence, sources, claim_map, errors, counters, hard):
    ledger = claims.get("sentence_ledger", [])
    ledger_ids = [r.get("sentence_id") for r in ledger if isinstance(r, dict)]
    if ledger_ids != expected_ids:
        errors.append("10B2 claim ledger does not cover every canonical sentence exactly once")
        counters["sentence_coverage_failures"] += 1
        hard["claims"]["missing_claim_sentence_rows"] = len(set(expected_ids).symmetric_difference(set(ledger_ids)))

    union_ids = set()
    for row in ledger:
        sid = row.get("sentence_id")
        if not review_shape_ok(row.get("forward_claim_review"), CLAIM_KEYS):
            errors.append(f"10B2 incomplete forward claim matrix at {sid}")
            counters["sentence_coverage_failures"] += 1
        if not review_shape_ok(row.get("reverse_claim_review"), CLAIM_KEYS):
            errors.append(f"10B2 incomplete reverse claim matrix at {sid}")
            counters["sentence_coverage_failures"] += 1
        ids = row.get("claim_candidate_ids")
        if not isinstance(ids, list):
            errors.append(f"10B2 claim_candidate_ids missing/not list at {sid}")
            counters["sentence_coverage_failures"] += 1
        else:
            union_ids.update(ids)

    indexed_by_sid = {u.get("sentence_id"): u.get("exact_text", "") for u in indexed}
    candidate_list = claims.get("claim_candidates", [])
    candidate_map = {}
    for rec in candidate_list:
        if not isinstance(rec, dict):
            continue
        cid = rec.get("claim_candidate_id")
        if cid:
            if cid in candidate_map:
                errors.append(f"duplicate claim candidate ID: {cid}")
                counters["claim_conservation_failures"] += 1
            candidate_map[cid] = rec
            sid = rec.get("sentence_id")
            quote = rec.get("exact_quote")
            if sid not in indexed_by_sid or not isinstance(quote, str) or quote not in indexed_by_sid.get(sid, ""):
                errors.append(f"10B2 exact_quote does not occur in declared sentence for {cid}")
                counters["claim_conservation_failures"] += 1

    discovered = set(candidate_map)
    if union_ids != discovered:
        errors.append("10B2 ledger claim union differs from claim_candidates")
        counters["claim_conservation_failures"] += 1

    proof = integrity.get("claim_conservation_proof", {})
    declared = set(proof.get("discovered_claim_ids", []))
    dispositions = proof.get("dispositions", {})
    if declared != discovered or set(dispositions.keys()) != discovered:
        errors.append("claim conservation IDs do not exactly match 10B2")
        counters["claim_conservation_failures"] += 1
    hard["claims"]["unconserved_claims"] = len(discovered.symmetric_difference(set(dispositions.keys())))

    evidence_map = {e.get("evidence_id"): e for e in evidence.get("evidence", []) if isinstance(e, dict) and e.get("evidence_id")}
    source_ids = {s.get("id") for s in sources.get("sources", []) if isinstance(s, dict)}
    claim_ids = {c.get("claim_id") for c in claim_map.get("claims", []) if isinstance(c, dict)} if claim_map else set()

    allowed = {"SUPPORTED", "QUALIFIED", "NON_FACTUAL", "UNRESOLVED"}
    unresolved = 0
    invalid_links = 0

    for cid, rec in dispositions.items():
        status = rec.get("status")
        if status not in allowed:
            errors.append(f"invalid claim disposition for {cid}: {status}")
            counters["claim_conservation_failures"] += 1
            continue
        issues = rec.get("remaining_issue_types", [])
        if not isinstance(issues, list):
            issues = ["invalid_issue_record"]
        for issue in issues:
            if issue == "unsupported_claim":
                hard["factual"]["unsupported_claims"] += 1
            elif issue == "certainty_overstatement":
                hard["factual"]["certainty_overstatements"] += 1
            elif issue == "unsupported_temporal_generalization":
                hard["factual"]["unsupported_temporal_generalizations"] += 1
            elif issue == "scope_overstatement":
                hard["factual"]["scope_overstatements"] += 1
        if status == "UNRESOLVED":
            unresolved += 1
            continue
        if status in {"SUPPORTED", "QUALIFIED"}:
            mapped = rec.get("mapped_claim_ids")
            ev_ids = rec.get("evidence_ids")
            if not isinstance(mapped, list) or not mapped or not isinstance(ev_ids, list) or not ev_ids:
                errors.append(f"factual claim disposition lacks claim/evidence mapping: {cid}")
                invalid_links += 1
                continue
            for mcid in mapped:
                if claim_map and mcid not in claim_ids:
                    errors.append(f"mapped claim ID missing from 03_claim_map.json: {cid}->{mcid}")
                    invalid_links += 1
            for eid in ev_ids:
                ev = evidence_map.get(eid)
                if not ev:
                    errors.append(f"evidence ID missing for {cid}: {eid}")
                    invalid_links += 1
                    continue
                if ev.get("source_id") not in source_ids:
                    errors.append(f"evidence source missing for {cid}: {eid}")
                    invalid_links += 1
                if not set(ev.get("claim_ids", [])).intersection(mapped):
                    errors.append(f"evidence does not support mapped claim IDs for {cid}: {eid}")
                    invalid_links += 1

    hard["claims"]["unresolved_claims"] = unresolved
    hard["claims"]["invalid_evidence_links"] = invalid_links
    if unresolved:
        errors.append("unresolved blind factual claims remain")
        counters["claim_conservation_failures"] += unresolved
    if invalid_links:
        counters["claim_conservation_failures"] += invalid_links
    return discovered


def verify_b3(naturalness, expected_ids, integrity, errors, counters, hard):
    ledger = naturalness.get("sentence_ledger", [])
    ledger_ids = [r.get("sentence_id") for r in ledger if isinstance(r, dict)]
    if ledger_ids != expected_ids:
        errors.append("10B3 naturalness ledger does not cover every canonical sentence exactly once")
        counters["sentence_coverage_failures"] += 1

    for row in ledger:
        sid = row.get("sentence_id")
        flags = row.get("flags")
        if not review_shape_ok(flags, NATURALNESS_KEYS):
            errors.append(f"10B3 incomplete naturalness flag matrix at {sid}")
            counters["sentence_coverage_failures"] += 1

    findings = {}
    for rec in naturalness.get("findings", []):
        if not isinstance(rec, dict):
            continue
        fid = rec.get("finding_id")
        if not fid or fid in findings:
            errors.append("duplicate or malformed 10B3 finding ID")
            counters["finding_conservation_failures"] += 1
            continue
        findings[fid] = rec

    proof = integrity.get("naturalness_finding_conservation_proof", {})
    declared = set(proof.get("discovered_finding_ids", []))
    dispositions = proof.get("dispositions", {})
    discovered = set(findings)

    if declared != discovered or set(dispositions.keys()) != discovered:
        errors.append("naturalness finding conservation IDs do not exactly match 10B3")
        counters["finding_conservation_failures"] += 1

    allowed = {"RESOLVED", "KEEP_WITH_REASON", "UNRESOLVED"}
    unresolved = 0
    for fid, rec in dispositions.items():
        status = rec.get("status")
        if status not in allowed:
            errors.append(f"invalid naturalness finding disposition for {fid}: {status}")
            counters["finding_conservation_failures"] += 1
            continue
        finding = findings.get(fid, {})
        ftype = finding.get("finding_type")
        if status == "KEEP_WITH_REASON":
            if finding.get("severity") != "soft" or not str(rec.get("reason", "")).strip():
                errors.append(f"invalid KEEP_WITH_REASON for {fid}")
                counters["finding_conservation_failures"] += 1
        if status == "UNRESOLVED":
            unresolved += 1
            if ftype == "translationese":
                hard["naturalness"]["translationese_flags"] += 1
            elif ftype in {"repeated_opening_or_fragment", "parallelism_overload", "rhetorical_question_overload"}:
                hard["naturalness"]["repeated_rhetorical_patterns"] += 1
            elif ftype in {"audio_density", "high_load_listening_block"}:
                hard["naturalness"]["unresolved_audio_density_flags"] += 1
                hard["narrative"]["high_load_listening_blocks"] += 1
            elif ftype == "unnecessary_label":
                hard["terminology"]["unnecessary_labels"] += 1
            elif ftype == "alias_overload":
                hard["terminology"]["alias_overload"] += 1
            elif ftype == "duplicate_explanation_or_reveal":
                hard["narrative"]["redundant_reveals"] += 1

    hard["naturalness"]["unresolved_naturalness_findings"] = unresolved
    if unresolved:
        errors.append("unresolved 10B3 findings remain")
        counters["finding_conservation_failures"] += unresolved
    return discovered


def isolation_verified(isolation, root, errors, counters):
    verified = isolation.get("isolation_status") == "VERIFIED"
    if isolation.get("manifest_origin") != "runtime":
        verified = False
    if not isolation.get("attestation_source"):
        verified = False

    audits = isolation.get("audits", {})
    exec_ids = []
    for name in ("10B1", "10B2", "10B3"):
        rec = audits.get(name, {})
        allowed_inputs = set(rec.get("allowed_input_files", []))
        observed = set(rec.get("observed_input_files", []))
        forbidden = set(rec.get("forbidden_input_files", []))
        if rec.get("context_mode") != "fresh":
            verified = False
        if rec.get("runtime_attested") is not True:
            verified = False
        if rec.get("forbidden_input_accessed") is not False:
            verified = False
        if not observed.issubset(allowed_inputs) or observed.intersection(forbidden):
            verified = False
        observed_hashes = rec.get("observed_input_hashes", {})
        if not isinstance(observed_hashes, dict):
            verified = False
        else:
            for rel in observed:
                p = safe_project_path(root, rel)
                if p is None or not p.exists() or observed_hashes.get(rel) != sha256_file(p):
                    verified = False
        eid = rec.get("execution_id")
        if not eid:
            verified = False
        else:
            exec_ids.append(eid)

    if len(exec_ids) != 3 or len(set(exec_ids)) != 3:
        verified = False
    return verified


def compare_summary(integrity, hard, counters, errors):
    for section in ("knowledge", "claims", "terminology", "narrative", "factual", "naturalness"):
        declared = integrity.get(section, {})
        for key, actual in hard[section].items():
            if key not in declared:
                errors.append(f"missing required summary counter {section}.{key}")
            elif declared.get(key) != actual:
                errors.append(f"summary counter mismatch {section}.{key}: declared {declared.get(key)}, recomputed {actual}")

    declared_proof = integrity.get("proof", {})
    for key, actual in counters.items():
        if key not in declared_proof:
            errors.append(f"missing required proof counter proof.{key}")
        elif declared_proof.get(key) != actual:
            errors.append(f"proof counter mismatch proof.{key}: declared {declared_proof.get(key)}, recomputed {actual}")


def verify_v33(args):
    script_path = Path(args.script).resolve()
    root = script_path.parent
    idx = load_json(args.index)
    blind = load_json(args.blind)
    claims = load_json(args.claims)
    naturalness = load_json(args.naturalness)
    integrity = load_json(args.integrity)
    isolation = load_json(args.isolation)
    manifest = load_json(args.manifest)
    evidence = load_json(args.evidence)
    sources = load_json(args.sources)
    claim_map_path = root / "03_claim_map.json"
    claim_map = load_json(claim_map_path) if claim_map_path.exists() else {}

    errors = []
    counters = {
        "schema_failures": 0,
        "hash_failures": 0,
        "stale_audit_failures": 0,
        "sentence_coverage_failures": 0,
        "candidate_conservation_failures": 0,
        "claim_conservation_failures": 0,
        "finding_conservation_failures": 0,
        "temporal_proof_failures": 0,
        "isolation_failures": 0,
    }
    hard = {
        "knowledge": {
            "core_entities_ungrounded": 0,
            "unmapped_aliases": 0,
            "missing_discovered_nodes": 0,
            "unresolved_concepts": 0,
            "unresolved_dependencies": 0,
            "unresolved_relations": 0,
            "temporal_first_use_failures": 0,
            "confusable_pairs_unresolved": 0,
            "silently_ignored_candidates": 0,
            "invalid_baseline_provenance": 0,
        },
        "claims": {
            "missing_claim_sentence_rows": 0,
            "unconserved_claims": 0,
            "unresolved_claims": 0,
            "invalid_evidence_links": 0,
        },
        "terminology": {"unnecessary_labels": 0, "alias_overload": 0},
        "narrative": {"redundant_reveals": 0, "high_load_listening_blocks": 0},
        "factual": {
            "unsupported_claims": 0,
            "certainty_overstatements": 0,
            "unsupported_temporal_generalizations": 0,
            "scope_overstatements": 0,
        },
        "naturalness": {
            "translationese_flags": 0,
            "repeated_rhetorical_patterns": 0,
            "unresolved_audio_density_flags": 0,
            "unresolved_naturalness_findings": 0,
        },
    }

    repo_root = Path(__file__).resolve().parents[1]
    schema_dir = repo_root / "schemas" / "v3.3"
    validate_all_project_artifacts(root, schema_dir, errors, counters)
    verify_manifest(manifest, root, errors, counters)

    script_hash = sha256_file(script_path)
    b1_hashes = verify_content_address(blind, root, errors, "10B1", counters)
    b2_hashes = verify_content_address(claims, root, errors, "10B2", counters)
    b3_hashes = verify_content_address(naturalness, root, errors, "10B3", counters)
    verify_content_address(integrity, root, errors, "10_final_integrity", counters)
    verify_content_address(idx, root, errors, "10_final_sentence_index", counters)

    for label, hm in (("10B1", b1_hashes), ("10B2", b2_hashes), ("10B3", b3_hashes)):
        audited_hash = declared_script_hash(hm)
        if audited_hash != script_hash:
            errors.append(f"{label}: audited script hash differs from released 10_final_script.md")
            counters["stale_audit_failures"] += 1

    locale = idx.get("locale", "en")
    computed = canonical_units(script_path.read_text(encoding="utf-8"), locale)
    expected_ids = verify_index(idx, computed, script_hash, errors, counters)

    indexed = idx.get("units", [])
    knowledge_ids, knowledge_counts = verify_b1(blind, expected_ids, computed, integrity, errors, counters, hard)
    claim_ids = verify_b2(claims, expected_ids, indexed, integrity, evidence, sources, claim_map, errors, counters, hard)
    finding_ids = verify_b3(naturalness, expected_ids, integrity, errors, counters, hard)

    iso_ok = isolation_verified(isolation, root, errors, counters)
    counters["isolation_failures"] = 0 if iso_ok else 1

    compare_summary(integrity, hard, counters, errors)

    content_errors = list(errors)
    status = "PASS" if not content_errors else "FAIL"
    project_status = (
        "PASS_VERIFIED"
        if not content_errors and iso_ok
        else "CONTENT_PASS_ISOLATION_NOT_VERIFIED"
        if not content_errors
        else "FAIL"
    )

    verifier_input_paths = [
        args.script, args.index, args.blind, args.claims, args.naturalness,
        args.integrity, args.isolation, args.manifest, args.evidence, args.sources
    ]
    if claim_map_path.exists():
        verifier_input_paths.append(str(claim_map_path))
    proof_content_address = {
        "hash_algorithm": "sha256",
        "inputs": [
            {"path": Path(p).name, "sha256": sha256_file(p)}
            for p in verifier_input_paths
        ]
    }

    return {
        "content_address": proof_content_address,
        "pipeline_version": "3.3",
        "proof_verifier_status": status,
        "isolation_verified": iso_ok,
        "project_status": project_status,
        "released_script_sha256": script_hash,
        "recomputed_sentence_count": len(computed),
        "discovered_candidate_count": len(knowledge_ids),
        "discovered_claim_count": len(claim_ids),
        "discovered_naturalness_finding_count": len(finding_ids),
        "recomputed_hard_counters": hard,
        "recomputed_proof_counters": counters,
        "errors": errors,
    }


def verify_v32(args):
    script_text = Path(args.script).read_text(encoding="utf-8")
    idx = load_json(args.index)
    blind = load_json(args.blind)
    integ = load_json(args.integrity)
    isolation = load_json(args.isolation)
    errors = []

    computed = canonical_units(script_text, "en")
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

    ledger = blind.get("sentence_ledger", [])
    if [r.get("sentence_id") for r in ledger] != expected_ids:
        errors.append("10B1 ledger does not cover every canonical sentence exactly once")

    for row in ledger:
        sid = row.get("sentence_id")
        if not review_shape_ok(row.get("forward_review"), KNOWLEDGE_KEYS):
            errors.append(f"incomplete forward category matrix at {sid}")
        if not review_shape_ok(row.get("reverse_review"), KNOWLEDGE_KEYS):
            errors.append(f"incomplete reverse category matrix at {sid}")

    candidates = blind_candidates(blind)
    discovered = set(candidates)
    for cid, item in candidates.items():
        phrase = item["phrase"]
        actual = actual_first_sentence_id(phrase, computed)
        if not phrase or actual is None:
            errors.append(f"invalid exact_phrase for {cid}")
        elif item["record"].get("first_use_sentence_id") != actual:
            errors.append(f"10B1 first_use_sentence_id mismatch for {cid}")

    proof = integ.get("candidate_conservation_proof", {})
    dispositions = proof.get("dispositions", {})
    if set(proof.get("discovered_candidate_ids", [])) != discovered:
        errors.append("10C discovered candidate IDs differ from 10B1")
    if set(dispositions.keys()) != discovered:
        errors.append("disposition IDs do not equal 10B1 discovered IDs")

    counts = {k: 0 for k in {"BASELINE_KNOWN", "GROUNDED", "REPLACED", "REMOVED", "UNRESOLVED"}}
    for cid, rec in dispositions.items():
        state = rec.get("status")
        if state not in counts:
            errors.append(f"invalid disposition for {cid}: {state}")
            continue
        counts[state] += 1
        if state == "BASELINE_KNOWN":
            prov = rec.get("baseline_provenance") or {}
            if prov.get("baseline_source_type") not in {"assumed_known", "normal_language_primitive"} or not prov.get("baseline_source_id_or_exact_entry"):
                errors.append(f"invalid BASELINE_KNOWN provenance for {cid}")

    if counts["UNRESOLVED"] != 0:
        errors.append("unresolved candidates remain")

    temporal = {r.get("candidate_id"): r for r in integ.get("temporal_proofs", [])}
    for cid, rec in dispositions.items():
        state = rec.get("status")
        phrase = candidates.get(cid, {}).get("phrase")
        actual_first = actual_first_sentence_id(phrase, computed)
        if state in {"REPLACED", "REMOVED"}:
            if phrase and actual_first is not None:
                errors.append(f"{state} candidate phrase still appears in final script: {cid}")
            continue
        tr = temporal.get(cid)
        if not tr:
            errors.append(f"missing temporal proof for {cid}")
            continue
        if tr.get("first_use_sentence_id") != actual_first:
            errors.append(f"temporal proof first-use mismatch for {cid}")
            continue
        mode = tr.get("grounding_mode")
        if mode == "BASELINE":
            continue
        first = sid_num(actual_first)
        ground = sid_num(tr.get("grounding_sentence_id"))
        if first is None or ground is None:
            errors.append(f"invalid temporal coordinates for {cid}")
        elif mode == "PRIOR" and not (ground < first):
            errors.append(f"PRIOR ordering invalid for {cid}")
        elif mode == "INLINE" and not (ground == first):
            errors.append(f"INLINE ordering invalid for {cid}")

    iso_ok = isolation.get("isolation_status") == "VERIFIED" and isolation.get("manifest_origin") == "runtime" and bool(isolation.get("attestation_source"))
    audits = isolation.get("audits", {})
    exec_ids = []
    for name in ("10B1", "10B2", "10B3"):
        rec = audits.get(name, {})
        allowed = set(rec.get("allowed_input_files", []))
        observed = set(rec.get("observed_input_files", []))
        forbidden = set(rec.get("forbidden_input_files", []))
        if rec.get("context_mode") != "fresh" or rec.get("runtime_attested") is not True or rec.get("forbidden_input_accessed") is not False:
            iso_ok = False
        if not observed.issubset(allowed) or observed.intersection(forbidden):
            iso_ok = False
        eid = rec.get("execution_id")
        if not eid:
            iso_ok = False
        else:
            exec_ids.append(eid)
    if len(exec_ids) != 3 or len(set(exec_ids)) != 3:
        iso_ok = False

    return {
        "pipeline_version": "3.2-compat",
        "proof_verifier_status": "PASS" if not errors else "FAIL",
        "isolation_verified": iso_ok,
        "project_status": (
            "PASS_VERIFIED" if not errors and iso_ok
            else "CONTENT_PASS_ISOLATION_NOT_VERIFIED" if not errors
            else "FAIL"
        ),
        "recomputed_sentence_count": len(computed),
        "discovered_candidate_count": len(discovered),
        "disposition_counts": counts,
        "errors": errors,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--script", required=True)
    ap.add_argument("--index", required=True)
    ap.add_argument("--blind", required=True)
    ap.add_argument("--integrity", required=True)
    ap.add_argument("--isolation", required=True)
    ap.add_argument("--claims")
    ap.add_argument("--naturalness")
    ap.add_argument("--manifest")
    ap.add_argument("--evidence")
    ap.add_argument("--sources")
    args = ap.parse_args()

    v33_args = [args.claims, args.naturalness, args.manifest, args.evidence, args.sources]
    if any(v33_args) and not all(v33_args):
        ap.error("v3.3 requires --claims --naturalness --manifest --evidence --sources together")

    result = verify_v33(args) if all(v33_args) else verify_v32(args)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["proof_verifier_status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
