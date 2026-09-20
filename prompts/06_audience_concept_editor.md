# 06 — AUDIENCE & CONCEPT CLOSURE EDITOR

## Role

Edit the current draft for a general audience listening once in real time and force recursive concept closure.

Your key question is not:
Were tracked terms explained?

It is:
Does the current script contain ANY meaningful concept or contextual role that the target audience must understand but does not?

Read and obey:
- prompts/CONCEPT_CLOSURE_PROTOCOL.md

This stage is the primary concept-closure gate.

## Inputs

Read:
- 00_project_brief.yaml
- 03_claim_map.json
- 03_concept_graph.json
- 04_story_architecture.md
- 05_script_draft.md
- 05_concept_delta.json

# Phase 1 — Full Script Concept Discovery

Scan 05_script_draft.md from scratch.

Do NOT limit discovery to tracked concepts.

Extract concepts that are:
- unfamiliar
- technical
- abstract
- used in a specialized contextual role
- likely to be confused with another concept
- required to understand a causal mechanism

Merge these with the Initial Concept Graph.

# Phase 2 — Recursive Dependency Resolution

For every concept in the actual script:

1. classify state: KNOWN | EXPLAINED | UNRESOLVED | REMOVED
2. locate first use
3. if explained, extract the concepts required to understand that explanation
4. resolve every dependency recursively
5. apply the necessity test:
   - EXPLAIN
   - REPLACE
   - REMOVE
6. repeat the scan until no new unresolved dependency appears

Hard rule:
No Unknowns in Definitions.

A parent concept cannot be EXPLAINED while any required dependency remains UNRESOLVED.

# Phase 3 — Confusable-pair audit

Use both:
- confusable_with metadata
- pairs discovered in the actual script

If both concepts appear and could be confused:
- explicitly distinguish their roles at first introduction
- do not rely on spelling differences alone

# Phase 4 — Contextual familiarity audit

Ask not only:
Does the audience know this word?

Also ask:
Does the audience understand the role this concept plays in THIS explanation?

If label familiarity is high but role familiarity is low:
- explain the role
- replace with concrete wording
- or remove

# Phase 5 — Weighted concept-load audit

Review approximate 30 to 60 second listening blocks.

Use the shared weighted heuristic:
- simple new concept: +1
- technical or abstract: +2
- confusable: +1
- dependency depth greater than 1: +1
- specialized role: +1

Use judgment, not a mechanical score target.

Reduce load by:
- sequencing dependencies earlier
- replacing labels with plain language
- removing unnecessary names
- splitting mechanisms across story beats

# Phase 6 — Listening test

Check:
- sentences too dense for audio
- acronym or name stacks
- nested definitions
- definitions that require another definition
- unclear antecedents
- abstract nouns replacing actions

Preserve visual storytelling while simplifying.

## Closure requirement

Stage 06 may only PASS when the revised script reaches a fixed point:

- unresolved = 0
- unresolved_dependencies = 0
- confusable_pairs_unresolved = 0

If a technical label is unnecessary, REMOVE or REPLACE it rather than teaching it.

## Outputs

Write:
- 06_audience_report.md
- 06_concept_closure.json
- 06_script_accessible.md

06_concept_closure.json is the resolved graph snapshot for downstream editors. It must include:
- concepts_detected
- known
- explained
- removed
- unresolved
- concepts: every current concept node with state, first_use, label_familiarity, role_familiarity, definition, dependencies, necessity and confusable_with
- dependency_edges
- unresolved_dependencies
- confusable_pairs_unresolved
- new_concepts_discovered_after_stage_03
- closure_iterations
- status

The revised script must be complete, not a diff.

Do not add production directions.
