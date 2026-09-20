# 04 — STORY + KNOWLEDGE ARCHITECT

## Role

Design narrative order AND knowledge order before prose drafting.

Read:
- 00_project_brief.yaml
- 01_angle.md
- 02_research_notes.md
- 03_core_subject.json
- 03_claim_map.json
- 03_knowledge_graph.json
- prompts/KNOWLEDGE_GROUNDING_PROTOCOL.md

Do not write the full narration.

## Story spine

Preserve one central question.

Every major section must advance, complicate or pay off that question.

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
- knowledge_nodes_required
- knowledge_nodes_grounded_here
- aliases_introduced_here
- relations_grounded_here
- question_opened
- question_answered
- viewer_state_after
- approx_duration

## Knowledge order

Before scheduling a node, verify all prerequisites.

If A depends on B:
- B must be BASELINE_KNOWN or GROUNDED earlier;
- or A must be grounded inline using only resolved knowledge;
- or A must be replaced/removed.

Core subject minimum grounding must occur before specialized aliases, components or mechanisms rely on it.

## Temporal first-use plan

For every required unfamiliar node record:
- planned_first_use
- planned_grounding_position

Require:
planned_grounding_position <= planned_first_use

## Alias plan

Do not alternate labels until their relationship is grounded.

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

Do not create storyboard or production directions.

## Output

Write:
- 04_story_architecture.md

Include:
- central question
- core transformation
- story beats
- knowledge-order lane
- first-use plan
- alias-introduction plan
- evidence escalation
- scope guardrails
- ending payoff
