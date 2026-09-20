# projects/

Các thư mục dưới đây là artifact do pipeline tạo.

## Pipeline hiện tại: v3.0

Project mới phải dùng schema Knowledge Grounding v3.

Artifact bắt buộc:

- 03_core_subject.json
- 03_claim_map.json
- 03_knowledge_graph.json
- 05_script_draft.md
- 05_blind_knowledge_inventory.json
- 06_knowledge_closure.json
- 07_knowledge_delta.json
- 08_knowledge_delta.json
- 09_knowledge_delta.json
- 10_final_candidate.md
- 10b_blind_knowledge_inventory.json
- 10_knowledge_closure.json
- 10_final_script.md

Final project chỉ được PASS khi tất cả bằng 0:

- core_entities_ungrounded
- unmapped_aliases
- missing_discovered_nodes
- unresolved_concepts
- unresolved_dependencies
- unresolved_relations
- temporal_first_use_failures
- confusable_pairs_unresolved

Ngoài ra:
- stage 09 fact check phải PASS;
- Visual Storytelling Score phải đạt gate;
- duration phải hợp lý.

## Legacy v2 projects

Các project dùng:
- 03_concept_graph.json
- *_concept_delta.json
- *_concept_closure.json

là project v2 và không còn là schema mẫu cho project mới.

Chúng vẫn hữu ích để regression-test các lỗi:
- definition sinh dependency mới;
- Writer/Editor sinh jargon sau graph ban đầu;
- recursive concept closure.

## Legacy v1 fixtures

Các project test v1:
- 2026-09-20_test_onion_tears
- 2026-09-20_test_milk_adults
- 2026-09-20_test_roman_concrete

được giữ lại như failure fixtures.

## Regression tests

- tests/concept_closure_regression.md
- tests/concept_closure_regression_results.md
- tests/knowledge_grounding_v3_regression.md

## Lưu ý

Không copy artifact schema từ project legacy để khởi tạo project mới.

Source of truth cho project mới:
- AGENTS.md
- prompts/00_orchestrator.md
- prompts/KNOWLEDGE_GROUNDING_PROTOCOL.md
