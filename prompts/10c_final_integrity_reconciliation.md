# 10C — FINAL INTEGRITY RECONCILIATION WITH CONSERVATION

## Role

Reconcile final candidate and isolated blind outputs.

Read:
- normal upstream evidence
- 10_final_candidate.md
- 10_final_sentence_index.json
- 10b_isolation_manifest.json
- 10b1_blind_knowledge_inventory.json
- 10b2_blind_claim_inventory.json
- 10b3_blind_naturalness_audit.json
- shared protocols
- CONTENT_ADDRESSING_PROTOCOL.md
- EVIDENCE_PROVENANCE_PROTOCOL.md

## 1. Isolation status

Read runtime manifest.

If isolation not VERIFIED:
- continue only as advisory reconciliation;
- project cannot be PASS_VERIFIED.

Do not rewrite manifest.

## 2. Validate 10B1 sentence coverage

Require:
- canonical sentence IDs == 10B1 ledger sentence IDs
- no missing/extra/duplicate IDs

Otherwise FAIL.

## 3. Candidate-level disposition

Every 10B1 candidate receives exactly one:
- BASELINE_KNOWN
- GROUNDED
- REPLACED
- REMOVED
- UNRESOLVED

BASELINE_KNOWN requires exact provenance.

## 4. Conservation equation

Compute and store:

discovered_count
=
baseline_known_count
+ grounded_count
+ replaced_count
+ removed_count
+ unresolved_count

Also:
- missing_candidate_ids
- duplicate_disposition_ids
- equation_valid

If invalid:
FAIL.

## 5. Temporal proof

For every retained unfamiliar candidate record:
- first_use_sentence_id
- grounding_mode
- grounding_sentence_id or baseline provenance
- ordering_valid

If coordinate missing or ordering invalid:
FAIL.

## 6. Claims

Reconcile all 10B2 claims against Claim Map/sources/stage 09.

Repair unsupported strength/scope minimally.

If factual substance changes:
rerun 09.

## 7. Naturalness/redundancy

Reconcile 10B3 flags.

Prefer minimal repair.

## 8. Repair loop

Any final-text change invalidates:
- 10_final_sentence_index.json
- all 10B outputs
- temporal proofs

Regenerate index and rerun all three isolated audits.

## Outputs

Write:
- 10_final_story_report.md
- 10_final_integrity.json
- 10_final_script.md

10_final_integrity.json must include:
- all normal integrity counters
- sentence_coverage_proof
- candidate_conservation_proof
- temporal_proof_summary
- baseline_provenance_summary
- isolation_status
- content_integrity_status
- proof_verifier_status: PENDING
- project_status: PENDING_10D

Do not declare PASS_VERIFIED here.


## v3.3 — Content-addressed claim + finding conservation

Before reconciliation, require 10B1/10B2/10B3 script/index hashes to match the current final candidate/index. Hash mismatch means stale proof and requires rerunning that blind audit.

### Blind claim conservation

Every 10B2 claim_candidate_id receives exactly one final disposition:
- SUPPORTED
- QUALIFIED
- NON_FACTUAL
- UNRESOLVED

For SUPPORTED/QUALIFIED record:
- mapped_claim_ids
- evidence_ids
- remaining_issue_types

Evidence must already exist in 02_evidence_ledger.json and map onward to a valid source. New evidence may not be invented in 10C.

### B3 finding conservation

Every 10B3 finding_id receives exactly one:
- RESOLVED
- KEEP_WITH_REASON
- UNRESOLVED

KEEP_WITH_REASON is allowed only for soft/editorial findings and requires a reason.

### Repair invalidation

If any final-text change is made, regenerate 10_final_sentence_index.json and rerun 10B1, 10B2 and 10B3 before continuing. Final released script bytes must equal the bytes audited by all three blind auditors.

### Additional 10_final_integrity.json proof records

Include:
- content_address
- claim_conservation_proof
- naturalness_finding_conservation_proof
- v3.3 proof counters for schema/hash/stale-audit/claim/finding conservation

10D recomputes these counters and rejects summary mismatches.
