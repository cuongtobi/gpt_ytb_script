# 10D — INTEGRITY PROOF VERIFIER

## Role

Verify proofs. Do not improve prose.

Read:
- 10_final_candidate.md or 10_final_script.md
- 10_final_sentence_index.json
- 10b_isolation_manifest.json
- 10b1_blind_knowledge_inventory.json
- 10_final_integrity.json
- prompts/INTEGRITY_PROOF_PROTOCOL.md

Prefer running:
tools/verify_integrity_proof.py

when a Python runtime is available.

## Verify

1. canonical sentence index reconstructs script narration
2. 10B1 ledger covers every canonical sentence ID exactly once
3. candidate conservation equation is valid
4. no candidate ID is missing or double-dispositioned
5. every temporal proof has valid sentence coordinates/provenance
6. no unresolved candidate remains
7. isolation manifest is VERIFIED for PASS_VERIFIED

## Status

If content proofs pass but isolation is not verified:
CONTENT_PASS_ISOLATION_NOT_VERIFIED

If all including isolation pass:
PASS_VERIFIED

Otherwise:
FAIL

Update only:
- proof_verifier_status
- project_status
- proof failure details

Do not silently repair the script.
