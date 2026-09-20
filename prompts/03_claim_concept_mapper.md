# 03 — CLAIM MAP + INITIAL CONCEPT GRAPH

## Role

Convert research into two control layers before script writing:

1. Claim Map — what the script may safely assert.
2. Initial Concept Dependency Graph — what the audience may need to understand before and during narration.

The Concept Graph is initial, not final. Downstream stages must discover concepts newly created by actual prose.

Read and obey:
- prompts/CONCEPT_CLOSURE_PROTOCOL.md

You are not writing documentary prose.

# Part A — Claim Map

## Inputs

Read:
- 00_project_brief.yaml
- 01_angle.md
- 02_research_notes.md
- 02_sources.json

## Claim record

Each important factual claim should include:
- claim_id
- claim
- category
- importance: core | supporting | optional
- confidence: high | medium | low
- support_type: direct | inference | contested
- source_ids
- safe_wording
- unsafe_wording
- caveats
- visual_potential
- story_function

Safe wording must preserve source certainty and precision.

Flag unsupported:
- probabilities
- percentages
- exact dates derived from ranges
- causal wording from correlational evidence
- first / only / all claims without strong support
- global generalizations from limited samples

Write:
- 03_claim_map.json

# Part B — Initial Concept Dependency Graph

## Goal

Build the first model of concepts likely to be needed by the selected story.

This is not a glossary. It is a dependency graph.

The actual script may later introduce new concepts; those must be discovered by delta and closure scans.

## Audience baseline

Create a small audience baseline appropriate to:
- requested language
- audience
- technical level
- topic context

Do not create a huge list of common words.

Use the baseline only to stop recursive explanation at reasonable common-language primitives.

## Discover likely concepts

Extract concepts that may be:
- unfamiliar
- abstract
- technical
- cognitively expensive
- familiar as a label but unfamiliar in the role used here

Examples:
- scientific mechanisms
- specialist terms
- acronyms
- historical institutions
- legal or economic processes
- unfamiliar causal roles

## Concept record

Each concept should include:
- concept_id
- name
- aliases
- status: KNOWN | EXPLAINED | UNRESOLVED | REMOVED
- label_familiarity: high | medium | low | very_low
- role_familiarity: high | medium | low | very_low
- importance: core | supporting | optional
- technical_term_required: true | false
- necessity: required | replaceable | removable
- definition.text
- definition.dependencies
- first_use_strategy
- best_explanation_type
- mental_model
- confusable_with
- explicit_contrast_required
- reuse_policy
- avoid_explanation

Each dependency should include:
- name
- relationship
- status

Allowed explanation types:
- direct_definition
- analogy
- human_action
- contrast
- mechanism
- example

## Dependency rules

For every proposed explanation:
1. extract concepts required to understand it
2. add them as dependencies
3. classify contextual familiarity
4. recursively resolve until dependencies reach KNOWN or EXPLAINED concepts

Hard rule:
No Unknowns in Definitions.

If a dependency is not necessary to the story, prefer rewriting the parent explanation rather than expanding a chain of jargon.

## Confusable-pair rules

If confusable_with is not empty and both concepts are likely to appear:
- require an explicit first-use distinction
- sequence the simpler or base concept first

## Necessity rules

For every technical label decide:
- EXPLAIN because later reasoning needs it
- REPLACE with plain language
- REMOVE

A concept can be important while its technical label is unnecessary.

## Concept-load planning

Estimate high-load clusters using the weighted heuristic from the shared protocol.

Do not merely count terms.

## Output

Write:
- 03_concept_graph.json

Top-level fields should include:
- audience_baseline
- concepts
- dependency_edges
- high_load_clusters
- concepts_intentionally_removed
- confusable_pairs
- initial_closure_status

The graph may contain UNRESOLVED concepts before narration is written, but they must have a clear planned resolution.

Do not output 03_concept_map.json for new projects. 03_concept_graph.json is the source of truth.
