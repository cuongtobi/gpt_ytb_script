# projects/

## Current schema: v3.2

New projects use proof-carrying integrity.

Important new artifacts:
- 05_draft_sentence_index.json
- 10_final_sentence_index.json
- 10b_isolation_manifest.json
- 10_final_integrity.json
- 10d_proof_verification.json

Allowed final statuses:
- PASS_VERIFIED
- CONTENT_PASS_ISOLATION_NOT_VERIFIED
- FAIL

v3.1 projects remain regression fixtures.

See:
- tests/v3_1_three_10min_stress_test.md
- tests/v3_2_integrity_proof_regression.md

Do not copy v3/v3.1 artifact schemas into new projects.
