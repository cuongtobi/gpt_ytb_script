# 06 — AUDIENCE KNOWLEDGE CLOSURE EDITOR

## Role

Reconcile actual draft, two-pass blind discovery and initial knowledge graph.

Read:
- 00_project_brief.yaml
- 03_core_subject.json
- 03_claim_map.json
- 03_knowledge_graph.json
- 04_story_architecture.md
- 05_script_draft.md
- 05_lexical_knowledge_sweep.json
- 05_blind_knowledge_inventory.json
- prompts/KNOWLEDGE_GROUNDING_PROTOCOL.md
- prompts/FINAL_INTEGRITY_PROTOCOL.md

## Phase 1 — Discovery coverage

Every lexical candidate must receive one disposition:
- BASELINE_KNOWN
- GROUNDED
- REPLACED
- REMOVED
- UNRESOLVED

Create a crosswalk from candidate_id → disposition.

No Silent Ignore.

Record:
- lexical_candidates
- reconciled_candidates
- silently_ignored_candidates

If silently_ignored_candidates > 0:
FAIL.

## Phase 2 — Strict BASELINE_KNOWN validation

A candidate may be BASELINE_KNOWN only if:
- exact/canonical phrase is supported by audience baseline;
- or explicitly mapped to a declared primitive.

Do not infer KNOWN from familiarity.

## Phase 3 — Core subject

Check:
- kind of thing;
- story-relevant parts/properties;
- alias relations;
- component relations.

Topic mention alone is not grounding.

## Phase 4 — Alias/relation closure

Retained aliases must be mapped before free reuse.

Required relations must be understood before claims rely on them.

## Phase 5 — Recursive dependencies

Reject explanations that require unresolved knowledge.

Ground, replace or remove dependencies recursively.

## Phase 6 — Temporal closure

For each unfamiliar required item:
- actual first_use
- grounded_at

FAIL if grounded later.

## Phase 7 — Confusable labels

Resolve distinctions at first introduction.

## Outputs

Write:
- 06_audience_report.md
- 06_knowledge_closure.json
- 06_script_accessible.md

06_knowledge_closure.json includes:
- core_entities_ungrounded
- unmapped_aliases
- missing_discovered_nodes
- unresolved_concepts
- unresolved_dependencies
- unresolved_relations
- temporal_first_use_failures
- confusable_pairs_unresolved
- silently_ignored_candidates
- discovery_coverage
- candidate_disposition_crosswalk
- nodes
- relations
- first_use_timeline
- closure_iterations
- status

PASS only when all nine knowledge failure counts are zero.
