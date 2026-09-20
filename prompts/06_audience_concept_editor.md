# 06 — AUDIENCE KNOWLEDGE CLOSURE EDITOR

## Role

Reconcile the actual draft with the initial graph and independent blind inventory.

Read:
- 00_project_brief.yaml
- 03_core_subject.json
- 03_claim_map.json
- 03_knowledge_graph.json
- 04_story_architecture.md
- 05_script_draft.md
- 05_blind_knowledge_inventory.json
- prompts/KNOWLEDGE_GROUNDING_PROTOCOL.md

## Phase 1 — Missing-node reconciliation

Every candidate from blind inventory must be:
- mapped to an existing graph node;
- added as a new node;
- or explicitly classified as ordinary vocabulary that requires no knowledge node.

Do not silently ignore blind-discovered candidates.

Record missing_discovered_nodes.

## Phase 2 — Core Subject Grounding

Check:
- what kind of thing the core subject is;
- story-relevant parts/properties;
- alias relationships;
- required component relationships.

The topic label itself does not count as grounding.

## Phase 3 — Alias and relation closure

For every retained alias:
- verify relationship is clear before free reuse.

For every required relation:
- verify the viewer can understand it at the first claim that relies on it.

## Phase 4 — Recursive dependency closure

For each node:
- validate dependencies;
- reject self-declared BASELINE_KNOWN nodes not supported by audience baseline;
- replace/remove unnecessary jargon;
- recurse until all required dependencies terminate at baseline-known or earlier-grounded nodes.

## Phase 5 — Temporal closure

For each unfamiliar required node:
- identify actual first use;
- identify grounding position.

FAIL if grounding happens after first use.

Repair by:
- moving grounding earlier;
- grounding inline;
- replacing the label;
- removing it.

## Phase 6 — Confusable labels

Resolve all required distinctions at first introduction.

## Outputs

Write:
- 06_audience_report.md
- 06_knowledge_closure.json
- 06_script_accessible.md

06_knowledge_closure.json must include:
- core_entities_ungrounded
- unmapped_aliases
- missing_discovered_nodes
- unresolved_concepts
- unresolved_dependencies
- unresolved_relations
- temporal_first_use_failures
- confusable_pairs_unresolved
- nodes
- relations
- first_use_timeline
- blind_inventory_reconciliation
- closure_iterations
- status

PASS only if all eight failure counts are zero.
