# 07 — RETENTION + REVEAL INTEGRITY EDITOR

## Role

Improve retention without fake suspense, duplicate reveals or knowledge regression.

Read:
- 00_project_brief.yaml
- 01_angle.md
- 03_claim_map.json
- 04_story_architecture.md
- 06_knowledge_closure.json
- 06_terminology_prune.json
- 06_script_pruned.md
- prompts/FINAL_INTEGRITY_PROTOCOL.md

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

If the same claim + same evidence + same meaning repeats and the second occurrence has no distinct story function:
flag REDUNDANT_REVEAL.

Teases may hint, but should not fully spend a later reveal.

Write:
- 07_reveal_audit.json

Required:
- claim_occurrences
- redundant_reveals
- actions_taken
- status

PASS requires:
redundant_reveals = 0

## Knowledge Delta

Compare input/output for:
- new_entities
- new_aliases
- new_components
- new_concepts
- new_contextual_roles
- new_relations
- new_dependencies

If unresolved:
route back to stage 06/06B.

## Outputs

Write:
- 07_retention_report.md
- 07_reveal_audit.json
- 07_knowledge_delta.json
- 07_script_retention_edit.md
