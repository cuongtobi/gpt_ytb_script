# 00 — ORCHESTRATOR

## Role

Control the v3.2 proof-carrying documentary pipeline.

Read:
- AGENTS.md
- KNOWLEDGE_GROUNDING_PROTOCOL.md
- FINAL_INTEGRITY_PROTOCOL.md
- INTEGRITY_PROOF_PROTOCOL.md

## Pipeline v3.2

00 Project Brief
→ 01 Angle
→ 02 Research
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
→ 10B2 Isolated Claim Audit
→ 10B3 Isolated Naturalness Audit
→ 10C Final Reconciliation
→ 10D Integrity Proof Verifier
→ FINAL

## Creative vs integrity lanes

Creative stages should optimize story quality.

Do not force the writer to explain every candidate.

Integrity stages prove coverage after writing.

## Blind isolation rule

10B1, 10B2 and 10B3 require separate fresh execution contexts.

If runtime supports isolated agents/tasks/chats:
- create distinct executions;
- runtime writes 10b_isolation_manifest.json.

If runtime cannot verify fresh contexts:
- set isolation_status = ISOLATION_NOT_VERIFIED;
- continue advisory audits if useful;
- final project cannot be PASS_VERIFIED.

Never fabricate execution IDs or isolation proof.

## Project brief

pipeline.version: 3.2

## Required v3.2 artifacts

00_project_brief.yaml
01_angle.md
02_research_notes.md
02_sources.json
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
10d_proof_verification.json

## Completion

PASS_VERIFIED requires:
- all content integrity gates pass;
- canonical sentence coverage proof passes;
- candidate conservation proof passes;
- temporal proof passes;
- strict baseline provenance passes;
- stage 09 passes;
- isolation VERIFIED;
- tools/verify_integrity_proof.py or equivalent deterministic proof check passes.

If content passes but isolation cannot be verified:
project_status = CONTENT_PASS_ISOLATION_NOT_VERIFIED

Do not call that PASS_VERIFIED.
