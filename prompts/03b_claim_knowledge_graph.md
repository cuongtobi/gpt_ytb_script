# 03B — CLAIM MAP + AUDIENCE KNOWLEDGE GRAPH

## Role

Create:
1. factual Claim Map;
2. initial Audience Knowledge Graph.

Read:
- 00_project_brief.yaml
- 01_angle.md
- 02_research_notes.md
- 02_sources.json
- 03_core_subject.json
- prompts/KNOWLEDGE_GROUNDING_PROTOCOL.md
- prompts/FINAL_INTEGRITY_PROTOCOL.md

Do not write narration.

## Part A — Claim Map

For each material claim record:
- claim_id
- claim
- importance
- confidence
- support_type
- source_ids
- safe_wording
- unsafe_wording
- caveats
- story_function
- allowed_certainty
- forbidden_strengthening
- time_scope
- geographic_scope
- population_scope
- preferred_temporal_wording
- forbidden_temporal_shortcuts

Claim strength is a contract for stages 05, 09 and 10C.

Do not allow later prose to become more certain, broader or more temporally vague than the evidence.

## Part B — Audience baseline

Record:
- language
- audience
- technical_level
- assumed_known
- normal_language_primitives
- never_auto_known_categories

Never-auto-known normally includes:
- scientific species names
- acronyms
- biochemical terms
- specialist archaeological methods
- specialist genetics/evolution terms
- legal/technical labels
- specialized uses of ordinary words

BASELINE_KNOWN requires exact baseline support or explicit canonical mapping to a primitive.

## Part C — Knowledge graph

Node fields:
- knowledge_id
- label
- type
- canonical_entity
- state
- label_familiarity
- role_familiarity
- importance
- necessity
- minimum_grounding
- dependencies
- relations
- aliases
- confusable_with
- first_use_strategy
- removal_strategy
- definition_scope
- safe_definition
- unsafe_definition

Necessity should include when relevant:
- needed_for_later_reasoning
- expected_reuse
- precision_gain
- story_value
- replacement_available

## Alias Budget

Import entity_label_policy from 03_core_subject.json.

Graph aliases must respect:
- primary spoken label
- scientific alias policy
- reuse policy
- labels recommended for removal

## Dependency validation

A dependency may be BASELINE_KNOWN only if supported by audience baseline.

Otherwise create/ground/replace/remove it.

## Outputs

Write:
- 03_claim_map.json
- 03_knowledge_graph.json

03_knowledge_graph.json includes:
- audience_baseline
- entity_label_policy
- nodes
- relations
- dependency_edges
- alias_map
- confusable_pairs
- initial_unresolved
- status
