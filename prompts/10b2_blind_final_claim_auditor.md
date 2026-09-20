# 10B2 — ISOLATED BLIND FINAL SENTENCE-LEVEL CLAIM AUDITOR

## Execution requirement

Run in a fresh execution context distinct from 10B1 and 10B3.

Allowed:
- 00_project_brief.yaml
- 10_final_candidate.md
- 10_final_sentence_index.json
- CONTENT_ADDRESSING_PROTOCOL.md
- FINAL_INTEGRITY_PROTOCOL.md
- INTEGRITY_PROOF_PROTOCOL.md

Forbidden:
- Claim Map
- research notes/sources/evidence ledger
- stage 09 audits
- 10B1/10B3 outputs

Hash every actual input.

## PASS C1 — Forward claim review

Process canonical sentence IDs from first to last.

For EVERY sentence create all category arrays:
- empirical_fact
- dates_quantities
- causal_mechanism
- scope_population_geography
- comparison_superlative
- attribution_source
- uncertainty_model
- negative_absence_claim
- definition_classification
- historical_event

List exact factual phrases considered in that sentence.
Empty arrays are allowed; missing keys are not.

## PASS C2 — Reverse claim review

Process the same sentences from last to first.
Do not copy C1.
Specifically look for factual commitments that sound like ordinary narration and may have been normalized away.

Use the same complete category matrix.

## Claim candidate union

For each sentence:
claim_candidate_ids = union(C1 candidates, C2 candidates)

Each claim candidate:
- claim_candidate_id
- sentence_id
- exact_quote
- normalized_claim
- claim_type
- discovered_by: forward|reverse|both
- risk_flags

risk_flags may include:
- unsupported_candidate
- certainty_overstatement_candidate
- temporal_generalization_candidate
- scope_overstatement_candidate

Do not decide source support here.

exact_quote must occur inside the indexed sentence.

## Coverage proof

Exactly one ledger row for every canonical sentence ID.
Each row:
- sentence_id
- forward_claim_review
- reverse_claim_review
- claim_candidate_ids

Zero claims is valid.
Missing sentence/category key is FAIL.

## Output

Write 10b2_blind_claim_inventory.json including:
- audit_run_id supplied by runtime
- content_address
- sentence_ledger
- claim_candidates
- coverage_proof
- status

Do not self-create execution identity.
Do not read research evidence during discovery.
