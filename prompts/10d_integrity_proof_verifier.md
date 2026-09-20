# 10D — FULL INTEGRITY PROOF VERIFIER

## Role

Verify proofs only. Do not improve prose.

Read:
- 10_final_script.md
- 10_final_sentence_index.json
- 10b_isolation_manifest.json
- 10b1_blind_knowledge_inventory.json
- 10b2_blind_claim_inventory.json
- 10b3_blind_naturalness_audit.json
- 10_final_integrity.json
- artifact_manifest.json
- 02_evidence_ledger.json
- 02_sources.json
- 03_claim_map.json when available for claim referential checks
- INTEGRITY_PROOF_PROTOCOL.md

When Python is available run:

~~~bash
python tools/verify_integrity_proof.py \
  --script <project>/10_final_script.md \
  --index <project>/10_final_sentence_index.json \
  --blind <project>/10b1_blind_knowledge_inventory.json \
  --claims <project>/10b2_blind_claim_inventory.json \
  --naturalness <project>/10b3_blind_naturalness_audit.json \
  --integrity <project>/10_final_integrity.json \
  --isolation <project>/10b_isolation_manifest.json \
  --manifest <project>/artifact_manifest.json \
  --evidence <project>/02_evidence_ledger.json \
  --sources <project>/02_sources.json
~~~

## Verify

1. validate required v3.3 JSON schemas;
2. verify artifact manifest hashes;
3. verify every audit-declared input hash;
4. require B1/B2/B3 script hashes equal released script hash;
5. recompute locale-aware canonical sentence units;
6. exact-match final sentence index;
7. exact-match B1/B2/B3 sentence coverage;
8. verify knowledge candidate conservation;
9. verify temporal first-use coordinates;
10. verify strict BASELINE_KNOWN provenance;
11. verify claim conservation;
12. verify claim → evidence → source referential integrity;
13. verify B3 finding conservation;
14. recompute hard counters from proof records;
15. require summary counters to match recomputed counters;
16. validate runtime isolation manifest.

## Status

- PASS_VERIFIED
- CONTENT_PASS_ISOLATION_NOT_VERIFIED
- FAIL

Write 10d_proof_verification.json.

The output itself must include `content_address` with SHA-256 for every project artifact actually read by 10D, including the claim map when used. This terminal proof output is not included in `artifact_manifest.json` because it is produced after manifest verification.

Do not repair script or proof artifacts silently.
