# 10B — BLIND FINAL KNOWLEDGE AUDITOR

## Independence requirement

This stage MUST NOT read:
- 03_core_subject.json
- 03_knowledge_graph.json
- 05_blind_knowledge_inventory.json
- 06_knowledge_closure.json
- 07/08/09 knowledge delta files
- any previous concept/knowledge list

Inputs allowed:
- 00_project_brief.yaml
- 10_final_candidate.md
- prompts/KNOWLEDGE_GROUNDING_PROTOCOL.md

## Role

Extract knowledge requirements from the final candidate from scratch.

Do not assume topic terms are understood.

Specifically test:
- core subject grounding;
- scientific/common/related labels;
- acronyms;
- components;
- mechanisms;
- common words used in specialized roles;
- relationships the narration expects the viewer to know;
- first-use positions.

## Output

Write:
- 10b_blind_knowledge_inventory.json

Include:
- candidates
- core_entity_candidates
- alias_candidates
- relationship_candidates
- specialized_role_candidates
- first_use_index
