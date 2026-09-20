# 05B — BLIND KNOWLEDGE DISCOVERY

## Independence requirement

This stage MUST NOT read:
- 03_core_subject.json
- 03_knowledge_graph.json
- any earlier knowledge closure/delta file

Inputs allowed:
- 00_project_brief.yaml
- 05_script_draft.md
- prompts/KNOWLEDGE_GROUNDING_PROTOCOL.md

The purpose is independent discovery, not confirmation of the existing graph.

## Role

Read the draft as a general viewer and extract every story-relevant piece of knowledge that may require grounding.

Extract:
- core entities
- other entities
- aliases/names
- components
- properties
- processes
- mechanisms
- concepts
- evidence types
- classifications
- specialized contextual roles
- relationships required to understand claims

For each candidate record:
- label
- type
- first_use_quote_or_position
- why_it_may_need_grounding
- likely_relationships
- confidence

Do not decide closure status from prior graph knowledge.

## Output

Write:
- 05_blind_knowledge_inventory.json

Required:
- candidates
- core_entity_candidates
- alias_candidates
- relationship_candidates
- specialized_role_candidates
- first_use_index
