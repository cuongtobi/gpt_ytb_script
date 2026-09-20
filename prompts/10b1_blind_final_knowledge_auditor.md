# 10B1 — BLIND FINAL KNOWLEDGE AUDITOR

## Independence

MUST NOT read:
- 03_core_subject.json
- 03_knowledge_graph.json
- 05 blind inventories
- 06 closure/prune artifacts
- 07/08/09 knowledge deltas
- prior knowledge lists

Allowed:
- 00_project_brief.yaml
- 10_final_candidate.md
- KNOWLEDGE_GROUNDING_PROTOCOL.md
- FINAL_INTEGRITY_PROTOCOL.md

## PASS A — sentence-by-sentence lexical sweep

Assign sentence IDs.

Extract every possible knowledge-bearing phrase:
- technical/scientific
- acronym
- abstract process
- classification
- evidence method
- measurement
- common word in specialized role
- alias
- mechanism
- relation

Record candidate IDs.

## PASS B — semantic audit

For every lexical candidate classify:
- likely knowledge-bearing
- likely ordinary
- duplicate
- alias
- specialized role

Do not assign closure status.

## Output

Write:
- 10b1_blind_knowledge_inventory.json

Include:
- sentences_scanned
- lexical_candidates
- semantic_candidates
- ordinary_candidates
- duplicate_map
- core_entity_candidates
- alias_candidates
- relationship_candidates
- specialized_role_candidates
- first_use_index

Every lexical candidate ID must appear in the semantic crosswalk.
