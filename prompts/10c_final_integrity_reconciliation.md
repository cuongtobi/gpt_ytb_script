# 10C — FINAL INTEGRITY RECONCILIATION

## Role

Reconcile three independent blind audits against project evidence and repair the final candidate until all integrity layers PASS.

Read:
- 00_project_brief.yaml
- 02_research_notes.md
- 02_sources.json
- 03_core_subject.json
- 03_claim_map.json
- 03_knowledge_graph.json
- 06_knowledge_closure.json
- 06_terminology_prune.json
- 07_reveal_audit.json
- 08_naturalness_audit.json
- 09_fact_check.md
- 09_claim_strength_audit.json
- 10_story_report_draft.md
- 10_final_candidate.md
- 10b1_blind_knowledge_inventory.json
- 10b2_blind_claim_inventory.json
- 10b3_blind_naturalness_audit.json
- KNOWLEDGE_GROUNDING_PROTOCOL.md
- FINAL_INTEGRITY_PROTOCOL.md

## Part A — Knowledge reconciliation

Every 10B1 lexical candidate receives final disposition:
- BASELINE_KNOWN
- GROUNDED
- REPLACED
- REMOVED
- UNRESOLVED

Validate:
- core subjects
- aliases
- relations
- dependencies
- temporal first use
- confusable labels
- strict baseline
- discovery coverage

No Silent Ignore.

## Part B — Terminology reconciliation

For every blind unnecessary-label candidate:
- verify necessity;
- apply alias budget;
- remove/replace labels not needed later.

Recheck context-scoped definitions.

## Part C — Claim reconciliation

Reconcile every 10B2 claim candidate against:
- Claim Map
- sources
- stage 09 audit

Repair:
- unsupported claims
- certainty drift
- temporal overgeneralization
- scope drift

If repair changes factual substance:
- rerun stage 09.

## Part D — Narrative reconciliation

Reconcile 10B3 duplicate-reveal candidates against architecture/reveal audit.

Remove/compress repeated claim+evidence+meaning unless occurrences have distinct story functions.

## Part E — Naturalness/listening reconciliation

Repair:
- translationese
- repeated rhetorical patterns
- alias overload
- audio-density failures
- awkward academic compression

Do not introduce new factual meaning.

## Repair loop

After ANY change to final candidate:
1. rerun affected stage checks;
2. rerun 10B1, 10B2 and 10B3 on the repaired final text;
3. reconcile again.

Stop only at stable fixed point.

## Final gate

Write 10_final_integrity.json with:

knowledge:
- core_entities_ungrounded
- unmapped_aliases
- missing_discovered_nodes
- unresolved_concepts
- unresolved_dependencies
- unresolved_relations
- temporal_first_use_failures
- confusable_pairs_unresolved
- silently_ignored_candidates

terminology:
- unnecessary_labels
- alias_overload

narrative:
- redundant_reveals
- high_load_listening_blocks

factual:
- unsupported_claims
- certainty_overstatements
- unsupported_temporal_generalizations
- scope_overstatements

naturalness:
- translationese_flags
- repeated_rhetorical_patterns
- unresolved_audio_density_flags

All counts must be 0.

Also require:
- stage 09 factual PASS
- Visual Storytelling Score >= 8.0
- duration reasonably aligned
- no production directions unless requested

## Outputs

Write:
- 10_final_story_report.md
- 10_final_integrity.json
- 10_final_script.md

Do not use 10_knowledge_closure.json as the final source of truth for v3.1 projects.
