# 07 — RETENTION + REVEAL INTEGRITY EDITOR

## Role

Improve retention without fake suspense, duplicate reveals or knowledge regression.

Read normal stage inputs plus:
- CONTENT_ADDRESSING_PROTOCOL.md
- FINAL_INTEGRITY_PROTOCOL.md

Hash every actual input.

Stage 06 and 06B must PASS.

## Retention audit

Review 30–60 second blocks for:
- curiosity
- change
- tension
- concrete anchor
- new information
- payoff
- knowledge load
- repetition
- scope relevance

## Reveal Duplication Audit

Build claim-occurrence records:
- claim_id or normalized_claim
- section/block
- evidence_used
- meaning
- story_function: TEASE|EXPLAIN|EVIDENCE|COMPLICATE|PAYOFF|CALLBACK

Same claim + same evidence + same meaning with no distinct story function = REDUNDANT_REVEAL.

## Knowledge Delta

Compare input/output for new knowledge.
If unresolved, route back to stage 06/06B.

## Outputs

Write:
- 07_retention_report.md
- 07_reveal_audit.json
- 07_knowledge_delta.json
- 07_script_retention_edit.md

Both JSON audits include:
- content_address
- input_script_sha256
- output_script_sha256

07_reveal_audit.json includes finding IDs and dispositions for every reveal issue.
No finding may disappear without RESOLVED or KEEP_WITH_REASON.
