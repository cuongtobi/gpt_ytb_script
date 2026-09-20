# 10B3 — ISOLATED BLIND FINAL NATURALNESS/REDUNDANCY AUDITOR

## Execution requirement

Must run in a fresh execution context distinct from 10B1 and 10B2.

Allowed:
- 00_project_brief.yaml
- 10_final_candidate.md
- FINAL_INTEGRITY_PROTOCOL.md
- INTEGRITY_PROOF_PROTOCOL.md

Forbidden:
- retention report
- reveal audit
- anti-AI/naturalness report
- terminology prune
- 10B1/10B2 outputs

## Audit

Find:
- translationese
- academic compression
- unnecessary labels
- duplicate explanations/reveals
- repeated openings/fragments
- parallelism overload
- rhetorical-question overload
- awkward terminology
- audio-density problems
- unclear pronouns
- surface errors

## Output

Write:
- 10b3_blind_naturalness_audit.json

Include audit_run_id supplied by runtime.

Do not self-create or guess execution identity.
