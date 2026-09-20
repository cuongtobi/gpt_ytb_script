# 10B2 — ISOLATED BLIND FINAL CLAIM/CERTAINTY AUDITOR

## Execution requirement

Must run in a fresh execution context distinct from 10B1 and 10B3.

Allowed:
- 00_project_brief.yaml
- 10_final_candidate.md
- FINAL_INTEGRITY_PROTOCOL.md
- INTEGRITY_PROOF_PROTOCOL.md

Forbidden:
- Claim Map
- research notes/sources
- stage 09 audits
- 10B1/10B3 outputs

## Extract

For every factual commitment:
- claim_candidate_id
- exact quote/paraphrase
- section
- claim type
- date/quantity
- causal strength
- certainty markers
- superlatives
- geographic scope
- population scope
- vague temporal language

Do not decide support yet.

## Output

Write:
- 10b2_blind_claim_inventory.json

Include audit_run_id supplied by runtime.

Do not self-create or guess execution identity.
