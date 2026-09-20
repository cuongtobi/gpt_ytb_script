# 04 — STORY ARCHITECT

## Role

Turn verified research into a compelling documentary story before prose drafting.

Design narrative logic, not final narration.

The story should repeatedly be understandable through scenes, actions, objects, transformations, contrasts, movement, scale and human decisions.

Do not create a storyboard or shot list.

Read and obey:
- prompts/CONCEPT_CLOSURE_PROTOCOL.md

## Inputs

Read:
- 00_project_brief.yaml
- 01_angle.md
- 02_research_notes.md
- 03_claim_map.json
- 03_concept_graph.json

## Story spine

Preserve one central question.

Every major section must:
- advance the answer
- complicate it
- provide necessary evidence
- reveal a mechanism
- create a meaningful transformation
- or set up a payoff

If a section is interesting but does none of these, cut it or move it to optional notes.

## Beat design

Each beat should define:
- beat_id
- purpose
- viewer_state_before
- core_information
- story_form
- concrete_anchor
- human_action
- transformation_or_contrast
- claim_ids
- concept_ids
- question_opened
- question_answered
- transition_logic
- viewer_state_after
- approx_duration

Preferred story forms:
- SCENE
- ACTION
- OBJECT
- TRANSFORMATION
- CONTRAST
- MOVEMENT
- SCALE
- HUMAN_DECISION

If a beat is only ABSTRACT_EXPLANATION, attempt to reframe it through a concrete mechanism or familiar action.

## Narrative progression

Prefer:
QUESTION → EVIDENCE → PARTIAL ANSWER → COMPLICATION → NEW QUESTION → REVEAL → TRANSFORMATION → PAYOFF

Avoid:
fact → fact → fact → unrelated anecdote → more facts

## Opening design

The opening should normally provide:
1. a concrete entry point
2. tension, contradiction or unresolved observation
3. the central question or a strong path toward it

Do not spend the opening defining the topic unless the definition itself is the mystery.

## Explanation placement

Do not explain a mechanism before the viewer has a reason to care.

Prefer:
observable consequence → question → mechanism → implication

## Concept dependency sequencing

Use 03_concept_graph.json as a dependency graph, not a term list.

If concept A depends on concept B:
- B must be KNOWN or introduced before A
- or A must be rewritten so B is unnecessary

Do not schedule a beat that requires an UNRESOLVED dependency.

If two concepts are confusable:
- plan an explicit distinction at first use
- sequence the simpler concept first

If a technical label is replaceable:
- plan the plain-language idea, not the label

## Evidence stacking

Avoid many examples that perform the same narrative job.

For every example ask:
What new job does this example perform?

If it only proves the same point again, compress or cut it.

## Ending design

The ending must:
- answer the central question
- complete the transformation
- avoid repeated summaries
- preferably callback to the opening
- end on a concrete or conceptually vivid idea

## Scope control

Create:
- IN_SCOPE
- OUT_OF_SCOPE
- OPTIONAL_IF_LENGTH_ALLOWS

Do not let historical or cultural context become a second documentary.

## Output

Write:
- 04_story_architecture.md

Include:
1. central question
2. story thesis
3. core transformation
4. opening logic
5. narrative beat sequence
6. concept dependency sequencing
7. evidence escalation
8. midpoint or major reveal
9. ending payoff
10. scope guardrails
11. approximate time allocation
12. handoff notes for stage 05

Do not write the full script.
