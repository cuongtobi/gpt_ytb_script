# 10B1 — ISOLATED BLIND FINAL KNOWLEDGE AUDITOR

## Execution requirement

Run in a fresh execution context.

Allowed:
- 00_project_brief.yaml
- 10_final_candidate.md
- 10_final_sentence_index.json
- CONTENT_ADDRESSING_PROTOCOL.md
- KNOWLEDGE_GROUNDING_PROTOCOL.md
- INTEGRITY_PROOF_PROTOCOL.md

Forbidden:
- graph
- closure
- terminology prune
- knowledge deltas
- prior inventories
- 10B2/10B3 outputs

Hash every actual input.

## Forward + reverse review

For every canonical sentence fill all knowledge category arrays in both independent directions:
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

## Candidate union

Create unique candidate IDs from the union.
exact_phrase must occur in the final candidate.
first_use_sentence_id must be the actual earliest canonical occurrence.

## Sentence ledger

Exactly one row per sentence:
- sentence_id
- forward_review
- reverse_review
- lexical_candidate_ids

## Output

Write 10b1_blind_knowledge_inventory.json including:
- audit_run_id supplied by runtime
- content_address
- sentence_ledger
- lexical_candidates
- semantic_crosswalk
- coverage_proof
- status

Do not create or guess execution identity.
