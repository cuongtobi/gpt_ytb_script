# 10C — FINAL INTEGRITY RECONCILIATION WITH CONSERVATION

## Role

Reconcile final candidate and blind outputs while preserving exact proof identity.

Read:
- normal upstream evidence
- 02_sources.json
- 02_evidence_ledger.json
- 03_claim_map.json
- 10_final_candidate.md
- 10_final_sentence_index.json
- 10b_isolation_manifest.json
- 10b1_blind_knowledge_inventory.json
- 10b2_blind_claim_inventory.json
- 10b3_blind_naturalness_audit.json
- shared protocols

Hash every actual input.

## 1. Isolation status

Read runtime manifest.
If isolation is not VERIFIED, continue advisory reconciliation but final project cannot be PASS_VERIFIED.

## 2. Validate freshness before reconciliation

Require B1/B2/B3 declared script/index hashes to match the current final candidate/index.
A mismatch is stale proof and requires rerunning the stale audit before reconciliation.

## 3. Knowledge conservation

Every B1 candidate receives exactly one:
- BASELINE_KNOWN
- GROUNDED
- REPLACED
- REMOVED
- UNRESOLVED

Require exact discovered/disposition ID equality, strict baseline provenance and valid temporal proof.

## 4. Claim conservation

Every B2 claim candidate receives exactly one FINAL disposition:
- SUPPORTED
- QUALIFIED
- NON_FACTUAL
- UNRESOLVED

For SUPPORTED/QUALIFIED record:
- mapped_claim_ids
- evidence_ids
- remaining_issue_types

Evidence IDs must already exist in 02_evidence_ledger.json.
Mapped claim IDs must already exist in 03_claim_map.json.

If a blind claim needs new research, reroute to stage 02/03B/09; do not manufacture evidence here.

UNRESOLVED must be zero.

## 5. Naturalness finding conservation

Every B3 finding receives exactly one:
- RESOLVED
- KEEP_WITH_REASON
- UNRESOLVED

KEEP_WITH_REASON requires a reason and is permitted only for soft/editorial findings.
UNRESOLVED must be zero.

## 6. Repair loop

If reconciliation changes final text:
- write the repaired text back as a new 10_final_candidate.md;
- invalidate 10_final_sentence_index.json;
- invalidate B1/B2/B3;
- rerun 10A1 and all three blind audits;
- rerun 10C.

Never release a script that differs from the script bytes audited by B1/B2/B3.

## 7. Recomputable integrity record

Write proof records, not only summary zeros.

10_final_integrity.json must contain:
- content_address
- knowledge candidate_conservation_proof
- temporal_proofs
- claim_conservation_proof
- naturalness_finding_conservation_proof
- summary counters
- isolation_status
- content_integrity_status
- proof_verifier_status: PENDING
- project_status: PENDING_10D

## Outputs

Write:
- 10_final_story_report.md
- 10_final_integrity.json
- 10_final_script.md

10_final_script.md must be byte-identical to the final candidate audited by B1/B2/B3. If not, rerun the final proof cycle.

Do not declare PASS_VERIFIED here.
