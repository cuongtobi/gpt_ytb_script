# 05B — BLIND KNOWLEDGE DISCOVERY WITH COVERAGE PROOF

## Independence

Must not read graph/closure/delta artifacts.

Allowed:
- 00_project_brief.yaml
- 05_script_draft.md
- 05_draft_sentence_index.json
- shared protocols

Hash every actual input using CONTENT_ADDRESSING_PROTOCOL.md.

## PASS A1 — Forward lexical review

Process every canonical sentence from first to last.

For EVERY sentence fill all category arrays:
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

## PASS A2 — Reverse lexical review

Process the same sentences last to first.
Do not copy A1.

## Candidate union

lexical_candidate_ids = union(A1 candidates, A2 candidates)

Candidate record:
- candidate_id
- exact_phrase
- first_use_sentence_id
- candidate_type
- reason_flagged
- discovered_by

## Coverage proof

Exactly one ledger row per canonical sentence.
Zero candidates is valid.
Missing row/category key is FAIL.

## Semantic crosswalk

Every candidate ID appears exactly once in semantic crosswalk.
Do not assign final disposition here.

## Outputs

Write:
- 05_lexical_knowledge_sweep.json
- 05_blind_knowledge_inventory.json

Both include content_address with hashes of every actual input.
