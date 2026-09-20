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
- terminology prune
- knowledge deltas
- prior knowledge inventories
- 10B2/10B3 outputs

## PASS A1 — Forward review

Read canonical sentences S0001 → last.

For every sentence fill ALL category arrays:
- technical_scientific
- acronyms_symbols
- abstract_processes
- classifications
- evidence_methods
- measurements_quantities
- historical_institutional
- specialized_common_words
- aliases_relations
- mechanisms

## PASS A2 — Reverse review

Read last sentence → S0001.

Independently look for phrases the forward pass may have missed.

Fill the same category matrix for every sentence.

## Candidate union

Create candidate IDs from the union of both passes.

Candidate record:
- candidate_id
- exact_phrase
- first_use_sentence_id
- candidate_type
- reason_flagged
- discovered_by

The exact_phrase must be text that actually occurs in the final candidate.

## Sentence ledger

Exactly one row per canonical sentence:
- sentence_id
- forward_review
- reverse_review
- lexical_candidate_ids

Zero candidates is allowed.
Missing category key is not.

## Semantic crosswalk

Every candidate ID appears exactly once.

Do not assign final closure status.

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
