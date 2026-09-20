# 05B — BLIND KNOWLEDGE DISCOVERY WITH COVERAGE PROOF

## Independence

Must not read:
- 03_core_subject.json
- 03_knowledge_graph.json
- prior closure/delta artifacts

Allowed:
- 00_project_brief.yaml
- 05_script_draft.md
- 05_draft_sentence_index.json
- shared protocols

## PASS A — Lexical sentence ledger

For EVERY sentence_id in 05_draft_sentence_index.json create exactly one ledger row.

Row:
- sentence_id
- lexical_candidate_ids: []

A zero-candidate row is required when no candidate exists.

Candidate triggers include:
- scientific/technical label
- acronym
- abstract process
- classification
- evidence method
- measurement
- historical/institutional label
- ordinary word in specialized role
- mechanism
- alias
- relationship the audience may need

Candidate record:
- candidate_id
- first_use_sentence_id
- exact_phrase
- candidate_type
- reason_flagged

## Coverage proof

Record:
- index_sentence_ids
- ledger_sentence_ids
- missing_sentence_ids
- extra_sentence_ids
- duplicate_sentence_ids
- coverage_ok

If coverage_ok != true:
FAIL immediately.

## PASS B — Semantic audit

Every candidate ID must be crosswalked as one of:
- likely_knowledge_bearing
- likely_ordinary_vocabulary
- duplicate_of_candidate
- alias_candidate
- specialized_role_candidate

Do not assign final closure disposition here.

## Outputs

Write:
- 05_lexical_knowledge_sweep.json
- 05_blind_knowledge_inventory.json

Do not claim discovery PASS without the sentence-ID coverage proof.
