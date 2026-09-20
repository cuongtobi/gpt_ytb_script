# 10D — INTEGRITY PROOF VERIFIER

## Role

Verify proofs only. Do not improve prose.

Read:
- 10_final_script.md
- 10_final_sentence_index.json
- 10b_isolation_manifest.json
- 10b1_blind_knowledge_inventory.json
- 10_final_integrity.json
- prompts/INTEGRITY_PROOF_PROTOCOL.md

When Python runtime is available, run:

```
python tools/verify_integrity_proof.py \
  --script <project>/10_final_script.md \
  --index <project>/10_final_sentence_index.json \
  --blind <project>/10b1_blind_knowledge_inventory.json \
  --integrity <project>/10_final_integrity.json \
  --isolation <project>/10b_isolation_manifest.json
```

## Verify

1. recompute canonical sentence units directly from script
2. exact-match index sentence IDs/text/order
3. exact-match 10B1 ledger sentence-ID sequence
4. take discovered candidate IDs directly from 10B1
5. verify discovered IDs == 10C disposition IDs
6. verify conservation arithmetic
7. verify strict BASELINE_KNOWN provenance
8. verify temporal coordinates
9. verify REMOVED/REPLACED phrases are absent where required
10. validate runtime isolation manifest

## Status

- PASS_VERIFIED
- CONTENT_PASS_ISOLATION_NOT_VERIFIED
- FAIL

Write:
- 10d_proof_verification.json

Do not repair script silently.
