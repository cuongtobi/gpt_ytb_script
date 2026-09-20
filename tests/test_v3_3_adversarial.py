#!/usr/bin/env python3
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from tools.verify_integrity_proof import verify_v33, canonical_units  # noqa: E402


K_KEYS = [
    "technical_scientific","acronyms_symbols","abstract_processes","classifications",
    "evidence_methods","measurements_quantities","historical_institutional",
    "specialized_common_words","aliases_relations","mechanisms"
]
C_KEYS = [
    "empirical_fact","dates_quantities","causal_mechanism","scope_population_geography",
    "comparison_superlative","attribution_source","uncertainty_model",
    "negative_absence_claim","definition_classification","historical_event"
]
N_KEYS = [
    "translationese","academic_compression","unnecessary_label","alias_overload",
    "duplicate_explanation_or_reveal","repeated_opening_or_fragment",
    "parallelism_overload","rhetorical_question_overload","awkward_terminology",
    "audio_density","high_load_listening_block","unclear_pronoun","surface_error"
]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def dump(path, data):
    Path(path).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def ca(*pairs):
    return {
        "hash_algorithm": "sha256",
        "inputs": [{"path": name, "sha256": digest} for name, digest in pairs]
    }


def refresh_manifest(root):
    hashes = {}
    for p in sorted(root.iterdir()):
        if p.is_file() and p.name not in {"artifact_manifest.json", "10d_proof_verification.json"}:
            hashes[p.name] = sha(p)
    dump(root / "artifact_manifest.json", {
        "pipeline_version": "3.3",
        "artifact_schema_version": "3.3.0",
        "segmenter_version": "3.3.0",
        "inputs": {"project_root": ".", "hash_algorithm": "sha256"},
        "outputs": {
            "final_script": "10_final_script.md",
            "final_index": "10_final_sentence_index.json",
            "final_integrity": "10_final_integrity.json",
            "artifact_count": len(hashes)
        },
        "hashes": hashes
    })


def build_fixture(root):
    script = "# Test\nWater boils at 100 °C.\n"
    (root / "10_final_script.md").write_text(script, encoding="utf-8")
    (root / "10_final_candidate.md").write_text(script, encoding="utf-8")
    script_hash = sha(root / "10_final_script.md")
    candidate_hash = sha(root / "10_final_candidate.md")

    (root / "00_project_brief.yaml").write_text(
        "project:\n  topic: Test\n  language: English\n  locale: en\n  duration_minutes: 1\n"
        "pipeline:\n  version: '3.3'\n  artifact_schema_version: '3.3.0'\n  segmenter_version: '3.3.0'\n",
        encoding="utf-8"
    )

    dump(root / "02_sources.json", {
        "sources": [{"id": "S001", "title": "Reference", "source_type": "primary", "url_or_locator": "https://example.com"}]
    })
    dump(root / "02_evidence_ledger.json", {
        "evidence": [{
            "evidence_id": "E001",
            "claim_ids": ["C001"],
            "source_id": "S001",
            "locator": "result section",
            "support_mode": "DIRECT",
            "evidence_summary": "Supports the test claim.",
            "limitations": ""
        }]
    })
    dump(root / "03_core_subject.json", {
        "core_entities": [], "alias_map": {}, "entity_label_policy": {},
        "minimum_grounding_requirements": [], "status": "PASS"
    })
    dump(root / "03_claim_map.json", {
        "claims": [{
            "claim_id": "C001", "claim": "Water boils at 100 °C.",
            "source_ids": ["S001"], "evidence_ids": ["E001"], "confidence": "high",
            "allowed_certainty": "direct", "time_scope": None,
            "geographic_scope": None, "population_scope": None
        }],
        "status": "PASS"
    })
    dump(root / "03_knowledge_graph.json", {
        "audience_baseline": {
            "language": "English", "audience": "general",
            "assumed_known": [], "normal_language_primitives": []
        },
        "nodes": [], "relations": [], "dependency_edges": [], "alias_map": {}, "status": "PASS"
    })

    index = {
        "source_file": "10_final_candidate.md",
        "source_sha256": script_hash,
        "locale": "en",
        "segmenter_version": "3.3.0",
        "content_address": ca(("10_final_candidate.md", candidate_hash)),
        "units": [{"sentence_id": "S0001", "section_heading": "Test", "exact_text": "Water boils at 100 °C."}],
        "source_sentence_count": 1,
        "indexed_sentence_count": 1,
        "duplicate_sentence_ids": [],
        "missing_sentence_ids": [],
        "reconstruction_ok": True,
        "status": "PASS"
    }
    dump(root / "10_final_sentence_index.json", index)
    index_hash = sha(root / "10_final_sentence_index.json")
    dump(root / "05_draft_sentence_index.json", index)

    k_review = {k: [] for k in K_KEYS}
    b1 = {
        "audit_run_id": None,
        "content_address": ca(
            ("10_final_candidate.md", candidate_hash),
            ("10_final_sentence_index.json", index_hash)
        ),
        "sentence_ledger": [{
            "sentence_id": "S0001",
            "forward_review": k_review,
            "reverse_review": k_review,
            "lexical_candidate_ids": []
        }],
        "lexical_candidates": [],
        "semantic_crosswalk": [],
        "coverage_proof": {"coverage_ok": True},
        "status": "PASS"
    }
    dump(root / "10b1_blind_knowledge_inventory.json", b1)
    dump(root / "05_blind_knowledge_inventory.json", b1)

    c_review = {k: [] for k in C_KEYS}
    c_review["empirical_fact"] = ["Water boils at 100 °C."]
    b2 = {
        "audit_run_id": None,
        "content_address": ca(
            ("10_final_candidate.md", candidate_hash),
            ("10_final_sentence_index.json", index_hash)
        ),
        "sentence_ledger": [{
            "sentence_id": "S0001",
            "forward_claim_review": c_review,
            "reverse_claim_review": c_review,
            "claim_candidate_ids": ["BC001"]
        }],
        "claim_candidates": [{
            "claim_candidate_id": "BC001",
            "sentence_id": "S0001",
            "exact_quote": "Water boils at 100 °C.",
            "normalized_claim": "Water boils at 100 °C.",
            "claim_type": "empirical_fact",
            "discovered_by": "both",
            "risk_flags": []
        }],
        "coverage_proof": {"coverage_ok": True},
        "status": "PASS"
    }
    dump(root / "10b2_blind_claim_inventory.json", b2)

    n_flags = {k: [] for k in N_KEYS}
    b3 = {
        "audit_run_id": None,
        "content_address": ca(
            ("10_final_candidate.md", candidate_hash),
            ("10_final_sentence_index.json", index_hash)
        ),
        "sentence_ledger": [{"sentence_id": "S0001", "flags": n_flags}],
        "findings": [],
        "coverage_proof": {"coverage_ok": True},
        "status": "PASS"
    }
    dump(root / "10b3_blind_naturalness_audit.json", b3)

    generic = {"content_address": ca(("10_final_script.md", script_hash)), "status": "PASS"}
    for name in [
        "05_lexical_knowledge_sweep.json",
        "06_terminology_prune.json",
        "07_reveal_audit.json",
        "07_knowledge_delta.json",
        "08_naturalness_audit.json",
        "08_knowledge_delta.json",
        "09_claim_strength_audit.json",
        "09_knowledge_delta.json"
    ]:
        dump(root / name, generic)

    dump(root / "06_knowledge_closure.json", {
        "content_address": ca(("10_final_script.md", script_hash)),
        "candidate_conservation_proof": {
            "discovered_candidate_ids": [], "dispositions": {}
        },
        "temporal_proofs": [],
        "status": "PASS"
    })

    observed = {
        "10_final_candidate.md": candidate_hash,
        "10_final_sentence_index.json": index_hash
    }
    dump(root / "10b_isolation_manifest.json", {
        "manifest_origin": "orchestrator_unverified",
        "attestation_source": None,
        "isolation_status": "ISOLATION_NOT_VERIFIED",
        "audits": {
            name: {
                "audit_id": name,
                "execution_id": None,
                "context_mode": "same_context_unverified",
                "allowed_input_files": list(observed),
                "observed_input_files": list(observed),
                "observed_input_hashes": observed,
                "forbidden_input_files": [],
                "forbidden_input_accessed": None,
                "runtime_attested": False
            } for name in ("10B1", "10B2", "10B3")
        }
    })

    b1_hash = sha(root / "10b1_blind_knowledge_inventory.json")
    b2_hash = sha(root / "10b2_blind_claim_inventory.json")
    b3_hash = sha(root / "10b3_blind_naturalness_audit.json")

    integrity = {
        "content_address": ca(
            ("10_final_script.md", script_hash),
            ("10b1_blind_knowledge_inventory.json", b1_hash),
            ("10b2_blind_claim_inventory.json", b2_hash),
            ("10b3_blind_naturalness_audit.json", b3_hash)
        ),
        "knowledge": {
            "core_entities_ungrounded": 0, "unmapped_aliases": 0,
            "missing_discovered_nodes": 0, "unresolved_concepts": 0,
            "unresolved_dependencies": 0, "unresolved_relations": 0,
            "temporal_first_use_failures": 0, "confusable_pairs_unresolved": 0,
            "silently_ignored_candidates": 0, "invalid_baseline_provenance": 0
        },
        "claims": {
            "missing_claim_sentence_rows": 0, "unconserved_claims": 0,
            "unresolved_claims": 0, "invalid_evidence_links": 0
        },
        "terminology": {"unnecessary_labels": 0, "alias_overload": 0},
        "narrative": {"redundant_reveals": 0, "high_load_listening_blocks": 0},
        "factual": {
            "unsupported_claims": 0, "certainty_overstatements": 0,
            "unsupported_temporal_generalizations": 0, "scope_overstatements": 0
        },
        "naturalness": {
            "translationese_flags": 0, "repeated_rhetorical_patterns": 0,
            "unresolved_audio_density_flags": 0, "unresolved_naturalness_findings": 0
        },
        "proof": {
            "schema_failures": 0, "hash_failures": 0, "stale_audit_failures": 0,
            "sentence_coverage_failures": 0, "candidate_conservation_failures": 0,
            "claim_conservation_failures": 0, "finding_conservation_failures": 0,
            "temporal_proof_failures": 0, "isolation_failures": 1
        },
        "candidate_conservation_proof": {
            "discovered_candidate_ids": [], "dispositions": {}
        },
        "temporal_proofs": [],
        "claim_conservation_proof": {
            "discovered_claim_ids": ["BC001"],
            "dispositions": {
                "BC001": {
                    "status": "SUPPORTED",
                    "mapped_claim_ids": ["C001"],
                    "evidence_ids": ["E001"],
                    "remaining_issue_types": []
                }
            }
        },
        "naturalness_finding_conservation_proof": {
            "discovered_finding_ids": [], "dispositions": {}
        },
        "isolation_status": "ISOLATION_NOT_VERIFIED",
        "content_integrity_status": "PASS",
        "proof_verifier_status": "PENDING",
        "project_status": "PENDING_10D"
    }
    dump(root / "10_final_integrity.json", integrity)
    refresh_manifest(root)


def args_for(root):
    return SimpleNamespace(
        script=str(root / "10_final_script.md"),
        index=str(root / "10_final_sentence_index.json"),
        blind=str(root / "10b1_blind_knowledge_inventory.json"),
        claims=str(root / "10b2_blind_claim_inventory.json"),
        naturalness=str(root / "10b3_blind_naturalness_audit.json"),
        integrity=str(root / "10_final_integrity.json"),
        isolation=str(root / "10b_isolation_manifest.json"),
        manifest=str(root / "artifact_manifest.json"),
        evidence=str(root / "02_evidence_ledger.json"),
        sources=str(root / "02_sources.json")
    )


class V33AdversarialTests(unittest.TestCase):
    def fresh(self):
        td = tempfile.TemporaryDirectory()
        root = Path(td.name)
        build_fixture(root)
        self.addCleanup(td.cleanup)
        return root

    def test_valid_bundle_passes_content_proof(self):
        root = self.fresh()
        result = verify_v33(args_for(root))
        self.assertEqual("PASS", result["proof_verifier_status"], result["errors"])
        self.assertEqual("CONTENT_PASS_ISOLATION_NOT_VERIFIED", result["project_status"])

    def test_stale_b2_hash_fails(self):
        root = self.fresh()
        data = json.loads((root / "10b2_blind_claim_inventory.json").read_text(encoding="utf-8"))
        data["content_address"]["inputs"][0]["sha256"] = "0" * 64
        dump(root / "10b2_blind_claim_inventory.json", data)
        refresh_manifest(root)
        result = verify_v33(args_for(root))
        self.assertEqual("FAIL", result["proof_verifier_status"])
        self.assertTrue(any("10B2" in e and "hash" in e for e in result["errors"]))

    def test_missing_claim_sentence_row_fails(self):
        root = self.fresh()
        data = json.loads((root / "10b2_blind_claim_inventory.json").read_text(encoding="utf-8"))
        data["sentence_ledger"] = []
        dump(root / "10b2_blind_claim_inventory.json", data)
        refresh_manifest(root)
        result = verify_v33(args_for(root))
        self.assertEqual("FAIL", result["proof_verifier_status"])
        self.assertTrue(any("10B2 claim ledger" in e for e in result["errors"]))

    def test_dropped_claim_disposition_fails(self):
        root = self.fresh()
        data = json.loads((root / "10_final_integrity.json").read_text(encoding="utf-8"))
        data["claim_conservation_proof"]["dispositions"] = {}
        dump(root / "10_final_integrity.json", data)
        refresh_manifest(root)
        result = verify_v33(args_for(root))
        self.assertEqual("FAIL", result["proof_verifier_status"])
        self.assertTrue(any("claim conservation" in e for e in result["errors"]))

    def test_invalid_evidence_link_fails(self):
        root = self.fresh()
        data = json.loads((root / "10_final_integrity.json").read_text(encoding="utf-8"))
        data["claim_conservation_proof"]["dispositions"]["BC001"]["evidence_ids"] = ["E999"]
        dump(root / "10_final_integrity.json", data)
        refresh_manifest(root)
        result = verify_v33(args_for(root))
        self.assertEqual("FAIL", result["proof_verifier_status"])
        self.assertTrue(any("evidence ID missing" in e for e in result["errors"]))

    def test_unresolved_b3_finding_fails(self):
        root = self.fresh()
        b3 = json.loads((root / "10b3_blind_naturalness_audit.json").read_text(encoding="utf-8"))
        b3["findings"] = [{
            "finding_id": "NF001",
            "finding_type": "translationese",
            "sentence_ids": ["S0001"],
            "description": "Synthetic mutation.",
            "severity": "hard",
            "suggested_action": "rewrite"
        }]
        dump(root / "10b3_blind_naturalness_audit.json", b3)

        integrity = json.loads((root / "10_final_integrity.json").read_text(encoding="utf-8"))
        integrity["naturalness_finding_conservation_proof"] = {
            "discovered_finding_ids": ["NF001"],
            "dispositions": {"NF001": {"status": "UNRESOLVED"}}
        }
        integrity["content_address"]["inputs"][3]["sha256"] = sha(root / "10b3_blind_naturalness_audit.json")
        dump(root / "10_final_integrity.json", integrity)
        refresh_manifest(root)

        result = verify_v33(args_for(root))
        self.assertEqual("FAIL", result["proof_verifier_status"])
        self.assertTrue(any("unresolved 10B3 findings" in e for e in result["errors"]))

    def test_false_hard_counter_fails(self):
        root = self.fresh()
        data = json.loads((root / "10_final_integrity.json").read_text(encoding="utf-8"))
        data["factual"]["unsupported_claims"] = 7
        dump(root / "10_final_integrity.json", data)
        refresh_manifest(root)
        result = verify_v33(args_for(root))
        self.assertEqual("FAIL", result["proof_verifier_status"])
        self.assertTrue(any("summary counter mismatch factual.unsupported_claims" in e for e in result["errors"]))

    def test_stale_manifest_fails(self):
        root = self.fresh()
        (root / "10_final_script.md").write_text("# Test\nWater boils at 100 °C!\n", encoding="utf-8")
        result = verify_v33(args_for(root))
        self.assertEqual("FAIL", result["proof_verifier_status"])
        self.assertTrue(any("artifact manifest hash mismatch" in e for e in result["errors"]))

    def test_japanese_fullwidth_segmentation(self):
        units = canonical_units("# 題\n最初です。次です。", "ja")
        self.assertEqual(["最初です。", "次です。"], [text for _, text in units])


if __name__ == "__main__":
    unittest.main()
