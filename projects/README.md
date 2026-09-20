# projects/

Các thư mục dưới đây là artifact do pipeline tạo.

## Pipeline hiện tại: v3.1

Project mới dùng Final Integrity System v3.1.

Các artifact integrity quan trọng:

- 05_lexical_knowledge_sweep.json
- 05_blind_knowledge_inventory.json
- 06_knowledge_closure.json
- 06_terminology_prune.json
- 07_reveal_audit.json
- 08_naturalness_audit.json
- 09_claim_strength_audit.json
- 10b1_blind_knowledge_inventory.json
- 10b2_blind_claim_inventory.json
- 10b3_blind_naturalness_audit.json
- 10_final_integrity.json
- 10_final_script.md

Final project chỉ PASS khi mọi count trong 10_final_integrity.json bằng 0 và stage 09 fact check PASS.

## v3 legacy projects

Project dùng:
- 10_knowledge_closure.json

là v3 trước Final Integrity System.

Giữ lại để regression-test.

## v2 legacy projects

Project dùng:
- 03_concept_graph.json
- *_concept_delta.json
- *_concept_closure.json

là schema v2.

## v1 legacy fixtures

- 2026-09-20_test_onion_tears
- 2026-09-20_test_milk_adults
- 2026-09-20_test_roman_concrete

## Regression tests

- tests/concept_closure_regression.md
- tests/concept_closure_regression_results.md
- tests/knowledge_grounding_v3_regression.md
- tests/final_integrity_v3_1_regression.md

## Source of truth

- AGENTS.md
- prompts/00_orchestrator.md
- prompts/KNOWLEDGE_GROUNDING_PROTOCOL.md
- prompts/FINAL_INTEGRITY_PROTOCOL.md

Không copy schema artifact từ project legacy cho project mới.
