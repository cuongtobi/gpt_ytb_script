# 10C — FINAL TEMPORAL KNOWLEDGE CLOSURE

## Role

Reconcile the final blind inventory against the project knowledge system and repair the final candidate until knowledge closure is complete.

Read:
- 00_project_brief.yaml
- 03_core_subject.json
- 03_claim_map.json
- 03_knowledge_graph.json
- 06_knowledge_closure.json
- 07_knowledge_delta.json
- 08_knowledge_delta.json
- 09_knowledge_delta.json
- 09_fact_check.md
- 10_story_report_draft.md
- 10_final_candidate.md
- 10b_blind_knowledge_inventory.json
- prompts/KNOWLEDGE_GROUNDING_PROTOCOL.md

## Required reconciliation

Every blind-discovered candidate must be accounted for.

Check:
1. core subject grounding;
2. aliases;
3. semantic relations;
4. dependencies;
5. contextual role familiarity;
6. temporal first use;
7. confusable labels;
8. nodes missing from prior graph.

Do not allow a node to be BASELINE_KNOWN unless supported by the audience baseline.

## Temporal rule

For every required unfamiliar node:

grounded_at <= first_use

If not:
- move grounding earlier;
- ground inline;
- replace;
- remove.

## Repair loop

After repair, rescan the repaired final text for newly introduced knowledge.

Repeat until stable.

If repair changes factual substance:
- route affected statements through stage 09 before PASS.

## Final gate

All must equal zero:
- core_entities_ungrounded
- unmapped_aliases
- missing_discovered_nodes
- unresolved_concepts
- unresolved_dependencies
- unresolved_relations
- temporal_first_use_failures
- confusable_pairs_unresolved

Also require:
- stage 09 factual PASS
- Visual Storytelling Score >= 8.0
- reasonable duration alignment

## Outputs

Write:
- 10_final_story_report.md
- 10_knowledge_closure.json
- 10_final_script.md

10_knowledge_closure.json must include:
- all eight failure counts
- nodes
- relations
- alias_map
- first_use_timeline
- blind_inventory_reconciliation
- repair_iterations
- status
