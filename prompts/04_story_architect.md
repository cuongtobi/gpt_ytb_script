# 04 — STORY + KNOWLEDGE ARCHITECT

## Role

Design narrative order, knowledge order and reveal order before prose drafting.

Read:
- 00_project_brief.yaml
- 01_angle.md
- 02_research_notes.md
- 03_core_subject.json
- 03_claim_map.json
- 03_knowledge_graph.json
- prompts/KNOWLEDGE_GROUNDING_PROTOCOL.md
- prompts/FINAL_INTEGRITY_PROTOCOL.md

Do not write full narration.

## Story spine

Preserve one central question.

Every major section must:
- advance;
- complicate;
- evidence;
- transform;
- or pay off that question.

## Beat design

Each beat should include:
- beat_id
- purpose
- viewer_state_before
- core_information
- concrete_anchor
- human_action
- transformation_or_contrast
- claim_ids
- claim_story_function
- knowledge_nodes_required
- knowledge_nodes_grounded_here
- aliases_introduced_here
- relations_grounded_here
- question_opened
- question_answered
- viewer_state_after
- approx_duration

claim_story_function is one of:
- TEASE
- EXPLAIN
- EVIDENCE
- COMPLICATE
- PAYOFF
- CALLBACK

## Knowledge order

If A depends on B:
- B is baseline/grounded earlier;
- or A is grounded inline;
- or A is replaced/removed.

Core subject grounding precedes specialized aliases/components/mechanisms.

## Temporal first-use plan

For every unfamiliar required node record:
- planned_first_use
- planned_grounding_position

Require:
planned_grounding_position <= planned_first_use

## Terminology plan

Respect entity label policy.

Do not schedule a label merely because it is technically available.

For each non-baseline label state why later reasoning needs it.

## Reveal Duplication Prevention

Create a claim-occurrence map.

If a claim appears in multiple beats:
- each occurrence must have a distinct story function.

Do not fully explain the same evidence in the hook and again in its evidence section.

A TEASE should tease, not consume the later reveal.

## Visual storytelling

Prefer:
- scene
- action
- object
- transformation
- contrast
- movement
- scale
- human decision

## Output

Write:
- 04_story_architecture.md

Include:
- central question
- core transformation
- story beats
- knowledge-order lane
- first-use plan
- terminology/alias plan
- claim-occurrence/reveal map
- evidence escalation
- scope guardrails
- ending payoff
