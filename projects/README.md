# projects/

## Current schema: v3.3

New projects use content-addressed full-integrity proofs.

Important v3.3 artifacts:
- 02_evidence_ledger.json
- 05_draft_sentence_index.json
- 10_final_sentence_index.json
- 10b_isolation_manifest.json
- 10b1_blind_knowledge_inventory.json
- 10b2_blind_claim_inventory.json
- 10b3_blind_naturalness_audit.json
- 10_final_integrity.json
- artifact_manifest.json
- 10d_proof_verification.json
- final.txt — post-10D TTS-ready narration
- 11_tts_export.json — post-10D export proof

Allowed final statuses:
- PASS_VERIFIED
- CONTENT_PASS_ISOLATION_NOT_VERIFIED
- FAIL

v3.1/v3.2 projects remain regression fixtures.
Do not copy their artifact schemas into new projects.

For new v3.3 projects, Stage 11 should run after 10D and should leave `10_final_script.md` unchanged.

See:
- tests/v3_2_integrity_proof_regression.md
- tests/v3_3_adversarial_regression.md
- schemas/v3.3/schema_manifest.json
