# 10B1 — ISOLATED BLIND FINAL KNOWLEDGE AUDITOR

## Execution requirement

Must run in a fresh execution context.

Allowed:
- 00_project_brief.yaml
- 10_final_candidate.md
- 10_final_sentence_index.json
- KNOWLEDGE_GROUNDING_PROTOCOL.md
- INTEGRITY_PROOF_PROTOCOL.md

Forbidden:
- graph
- closure
- prune
- knowledge deltas
- previous knowledge inventories
- 10B2/10B3 outputs

## Sentence ledger

For every sentence_id in 10_final_sentence_index.json create one row:
- sentence_id
- lexical_candidate_ids: []

Do not omit zero-candidate sentences.

## Candidate records

For each candidate:
- candidate_id
- exact_phrase
- first_use_sentence_id
- candidate_type
- reason_flagged

## Coverage proof

Compare sentence IDs from canonical index vs ledger.

Record:
- missing_sentence_ids
- extra_sentence_ids
- duplicate_sentence_ids
- coverage_ok

If false:
audit FAILS.

## Semantic crosswalk

Every candidate ID must appear exactly once in semantic crosswalk.

Do not assign final disposition.

## Output

Write:
- 10b1_blind_knowledge_inventory.json

Include:
- audit_run_id supplied by runtime
- sentence_ledger
- lexical_candidates
- semantic_crosswalk
- core_entity_candidates
- alias_candidates
- relationship_candidates
- specialized_role_candidates
- coverage_proof
- status
