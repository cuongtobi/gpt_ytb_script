# 00 — ORCHESTRATOR

## Role

Control the v3.3 content-addressed proof-carrying documentary pipeline.

Read:
- AGENTS.md
- CONTENT_ADDRESSING_PROTOCOL.md
- KNOWLEDGE_GROUNDING_PROTOCOL.md
- EVIDENCE_PROVENANCE_PROTOCOL.md
- FINAL_INTEGRITY_PROTOCOL.md
- INTEGRITY_PROOF_PROTOCOL.md

## Pipeline v3.3

00 Project Brief
→ 01 Angle
→ 02 Research + Evidence Ledger
→ 03A Core Subject
→ 03B Claim Map + Knowledge Graph
→ 04 Story + Knowledge Architect
→ 05 Writer
→ 05A1 Canonical Draft Sentence Index
→ 05B Blind Knowledge Discovery + Coverage Proof
→ 06 Knowledge Closure + Conservation + Temporal Proof
→ 06B Terminology Pruner
→ 07 Retention + Reveal Audit
→ 08 Naturalness + Listening
→ 09 Fact Check + Claim Strength
→ 10A Final Story Editor
→ 10A1 Canonical Final Sentence Index
→ 10B Isolation Handoff
→ 10B1 Isolated Knowledge Audit
→ 10B2 Isolated Sentence-Level Claim Audit
→ 10B3 Isolated Naturalness Audit
→ 10C Final Reconciliation
→ Artifact Manifest
→ 10D Full Integrity Proof Verifier
→ FINAL

## Creative vs integrity lanes

Creative stages should optimize story quality.
Do not force the writer to explain every candidate.

Integrity stages prove:
- exact input identity;
- sentence coverage;
- candidate and claim conservation;
- temporal grounding;
- claim-to-evidence-to-source provenance;
- final naturalness/redundancy finding closure;
- blind execution isolation where available.

## Content-addressing

Every audit artifact records SHA-256 for every actual input.
Final B1/B2/B3 must bind to the same exact script hash as 10_final_script.md.

Any final-text change invalidates:
- 10_final_sentence_index.json;
- 10B1;
- 10B2;
- 10B3;
- 10_final_integrity.json;
- artifact_manifest.json;
- 10D.

Regenerate from 10A1 onward after a final-text change.

## Blind isolation rule

10B1, 10B2 and 10B3 require separate fresh execution contexts.

If runtime supports isolated agents/tasks/chats:
- create distinct executions;
- runtime writes 10b_isolation_manifest.json.

If runtime cannot verify fresh contexts:
- set isolation_status = ISOLATION_NOT_VERIFIED;
- continue advisory audits;
- final project cannot be PASS_VERIFIED.

Never fabricate execution IDs or isolation proof.

## Project brief

pipeline.version: 3.3
artifact_schema_version: 3.3.0
segmenter_version: 3.3.0

## Required v3.3 artifacts

00_project_brief.yaml
01_angle.md
02_research_notes.md
02_sources.json
02_evidence_ledger.json
03_core_subject.json
03_claim_map.json
03_knowledge_graph.json
04_story_architecture.md
05_script_draft.md
05_draft_sentence_index.json
05_lexical_knowledge_sweep.json
05_blind_knowledge_inventory.json
06_audience_report.md
06_knowledge_closure.json
06_script_accessible.md
06_terminology_prune.json
06_script_pruned.md
07_retention_report.md
07_reveal_audit.json
07_knowledge_delta.json
07_script_retention_edit.md
08_anti_ai_report.md
08_naturalness_audit.json
08_knowledge_delta.json
08_script_natural.md
09_fact_check.md
09_claim_strength_audit.json
09_knowledge_delta.json
09_script_fact_checked.md
10_story_report_draft.md
10_final_candidate.md
10_final_sentence_index.json
10b_isolation_manifest.json
10b1_blind_knowledge_inventory.json
10b2_blind_claim_inventory.json
10b3_blind_naturalness_audit.json
10_final_story_report.md
10_final_integrity.json
10_final_script.md
artifact_manifest.json
10d_proof_verification.json

## Completion

PASS_VERIFIED requires:
- all artifact/schema gates pass;
- all declared audit input hashes match current bytes;
- final B1/B2/B3 script hashes equal the released script hash;
- canonical sentence coverage passes for B1/B2/B3;
- knowledge candidate conservation passes;
- claim conservation passes;
- finding conservation passes;
- temporal proof passes;
- strict baseline provenance passes;
- factual dispositions have valid evidence/source provenance;
- recomputed hard counters are zero;
- isolation VERIFIED;
- tools/verify_integrity_proof.py passes.

If content passes but isolation cannot be verified:
project_status = CONTENT_PASS_ISOLATION_NOT_VERIFIED

Do not call that PASS_VERIFIED.
