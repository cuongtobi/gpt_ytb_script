# 05B — BLIND KNOWLEDGE DISCOVERY WITH COVERAGE PROOF

## Independence

Must not read graph/closure/delta artifacts.

Allowed:
- 00_project_brief.yaml
- 05_script_draft.md
- 05_draft_sentence_index.json
- shared protocols
- prompts/CONTENT_ADDRESSING_PROTOCOL.md

## PASS A1 — Forward lexical review

Process canonical sentence IDs from first to last.

For EVERY sentence create a review with all category keys:
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

List phrases considered under each category.

## PASS A2 — Reverse lexical review

Process the same sentence IDs from last to first.

Do not merely copy A1.
Look specifically for phrases A1 may have normalized away or treated as ordinary.

Use the same complete category matrix.

## Candidate union

For each sentence:
lexical_candidate_ids = union(A1 candidates, A2 candidates)

Candidate record:
- candidate_id
- exact_phrase
- first_use_sentence_id
- candidate_type
- reason_flagged
- discovered_by: forward | reverse | both

## Coverage proof

There must be exactly one final ledger row for every canonical sentence ID.

Each row contains:
- sentence_id
- forward_review
- reverse_review
- lexical_candidate_ids

Missing sentence or missing category key = FAIL.

## PASS B — Semantic crosswalk

Every candidate ID must appear exactly once in semantic crosswalk:
- likely_knowledge_bearing
- likely_ordinary_vocabulary
- duplicate_of_candidate
- alias_candidate
- specialized_role_candidate

Do not assign final disposition here.

## Content address

Before writing outputs, record SHA-256 for every actual input. Both JSON outputs must include `content_address` using `CONTENT_ADDRESSING_PROTOCOL.md`.

## Outputs

Write:
- 05_lexical_knowledge_sweep.json
- 05_blind_knowledge_inventory.json
