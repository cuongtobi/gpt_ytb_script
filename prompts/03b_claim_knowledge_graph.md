# 03B — CLAIM MAP + AUDIENCE KNOWLEDGE GRAPH

## Role

Create:
1. the factual Claim Map;
2. the initial Audience Knowledge Graph.

Read:
- 00_project_brief.yaml
- 01_angle.md
- 02_research_notes.md
- 02_sources.json
- 03_core_subject.json
- prompts/KNOWLEDGE_GROUNDING_PROTOCOL.md

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

Preserve uncertainty and precision.

Write:
- 03_claim_map.json

## Part B — Audience baseline

Create a deliberately small audience baseline.

Record:
- language
- audience
- technical_level
- assumed_known
- normal_language_primitives
- never_auto_known_categories

Never-auto-known should normally include:
- scientific species names;
- acronyms;
- biochemical terms;
- specialist archaeological methods;
- specialist genetics/evolution terms;
- legal/technical labels.

A node cannot later become BASELINE_KNOWN unless justified by this baseline.

## Part C — Knowledge graph

Node fields:
- knowledge_id
- label
- type
- canonical_entity
- state: BASELINE_KNOWN | GROUNDED | UNRESOLVED | REMOVED
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

Relationship fields:
- source
- relation_type
- target
- grounding_required
- status

Node types and relations must follow the shared protocol.

## Dependency validation

Do not place status=BASELINE_KNOWN on a dependency unless:
- it exists in audience_baseline.assumed_known or normal_language_primitives.

Otherwise:
- create a node;
- ground it;
- replace it;
- or remove the dependency.

## Core subject integration

Every core entity and every retained alias from 03_core_subject.json must appear in the graph.

## Output

Write:
- 03_claim_map.json
- 03_knowledge_graph.json

03_knowledge_graph.json must include:
- audience_baseline
- nodes
- relations
- dependency_edges
- alias_map
- confusable_pairs
- initial_unresolved
- status
