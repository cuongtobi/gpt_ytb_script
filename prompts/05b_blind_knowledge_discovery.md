# 05B — TWO-PASS BLIND KNOWLEDGE DISCOVERY

## Independence requirement

MUST NOT read:
- 03_core_subject.json
- 03_knowledge_graph.json
- any earlier knowledge closure/delta artifact

Allowed inputs:
- 00_project_brief.yaml
- 05_script_draft.md
- prompts/KNOWLEDGE_GROUNDING_PROTOCOL.md
- prompts/FINAL_INTEGRITY_PROTOCOL.md

Purpose: independent discovery, not graph confirmation.

## PASS A — Lexical Knowledge Sweep

Read EVERY sentence in order.

Assign sentence IDs:
S001, S002, S003...

Create a lexical candidate for any phrase that may be:
- scientific/technical;
- acronym;
- abstract process;
- classification;
- evidence method;
- measurement concept;
- historical/institutional term;
- common word in a specialized role;
- causal mechanism;
- nontrivial alias;
- relation the viewer may need.

For every lexical candidate record:
- candidate_id
- sentence_id
- exact_phrase
- first_use_quote
- candidate_type
- reason_flagged

Do not skip a phrase because it sounds familiar.

Write:
- 05_lexical_knowledge_sweep.json

Include:
- sentences_scanned
- candidates

## PASS B — Semantic Knowledge Audit

Using only:
- project brief;
- draft;
- lexical sweep;
- shared protocols

For EVERY lexical candidate classify:
- likely_knowledge_bearing
- likely_ordinary_vocabulary
- duplicate_of_candidate
- alias_candidate
- specialized_role_candidate

Do not assign final BASELINE_KNOWN/GROUNDED status here.

Extract relationships and core-entity candidates.

Write:
- 05_blind_knowledge_inventory.json

Required:
- lexical_candidate_ids
- semantic_candidates
- ordinary_vocabulary_candidates
- duplicate_candidate_map
- core_entity_candidates
- alias_candidates
- relationship_candidates
- specialized_role_candidates
- first_use_index

## Coverage invariant

Every lexical candidate ID must appear somewhere in PASS B output.

If not:
- discovery stage FAILS.

Do not silently ignore a lexical candidate.
