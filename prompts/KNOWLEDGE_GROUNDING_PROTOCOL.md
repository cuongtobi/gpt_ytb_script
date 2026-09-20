# KNOWLEDGE GROUNDING PROTOCOL — v3.1

## Purpose

This is the source of truth for what the audience knows at each point in narration.

Use together with:
- prompts/FINAL_INTEGRITY_PROTOCOL.md

A script cannot pass simply because tracked technical terms are eventually defined.

The pipeline manages:
- core subjects;
- entities;
- aliases;
- components;
- properties;
- processes;
- mechanisms;
- concepts;
- evidence types;
- classifications;
- institutions;
- measurements;
- semantic relationships;
- first-use timing.

## Knowledge node types

- CORE_ENTITY
- ENTITY
- ALIAS
- COMPONENT
- PROPERTY
- PROCESS
- MECHANISM
- CONCEPT
- EVIDENCE_TYPE
- CLASSIFICATION
- INSTITUTION
- MEASUREMENT

## Relationship types

- IS_A
- ALIAS_OF
- SHORT_FORM_OF
- RELATED_TO
- PART_OF
- CONTAINS
- PRODUCES
- ACTS_ON
- CAUSES
- ASSOCIATED_WITH
- USED_FOR
- SELECTED_FOR
- SUBTYPE_OF
- EVIDENCE_FOR
- CONTRASTS_WITH
- DEPENDS_ON

## Core Subject Grounding

For every CORE_ENTITY distinguish:
- label_familiarity;
- subject_understanding.

A familiar topic name does not prove subject understanding.

Minimum story-relevant grounding should answer:
- what kind of thing is it?
- which parts/properties matter?
- which names refer to it?
- which related labels are not exact aliases?

The common topic label may appear in the title/hook before complete grounding.

Before a specialized alias, component or mechanism relies on the subject, minimum grounding must already exist in the same sentence or earlier.

## Alias Resolution

Do not assume two labels are understood as the same/related entity.

Retained labels require explicit relations such as:
- ALIAS_OF
- SHORT_FORM_OF
- RELATED_TO
- SUBTYPE_OF

If an alias adds no later reasoning value, terminology pruning should remove it.

## Minimum Grounding Requirement

Teach only what later reasoning needs.

Each required node records:
- minimum_grounding
- dependencies
- relations
- first_use_strategy

## Knowledge states

- BASELINE_KNOWN
- GROUNDED
- UNRESOLVED
- REMOVED

### Strict baseline rule

A node may be BASELINE_KNOWN only if:
1. the phrase appears in audience_baseline.assumed_known; or
2. it is explicitly mapped to a declared normal_language_primitive.

Do not infer KNOWN from familiarity.

High label familiarity is not a knowledge state.

## No Unknowns in Explanations

A node is not GROUNDED if its explanation depends on unresolved knowledge.

For every explanation:
1. extract dependencies;
2. validate dependencies;
3. ground, replace or remove them;
4. recurse until all required dependencies terminate at BASELINE_KNOWN or earlier GROUNDED nodes.

## Temporal Knowledge Closure

Narration is linear.

Eventually explained is not enough.

Record:
- first_use;
- grounded_at.

PASS requires:
grounded_at <= first_use

or grounding occurs inside the same first-use sentence before the label is relied upon.

## Blind Discovery — two passes

Blind discovery must not read the prior graph.

PASS A:
sentence-by-sentence lexical knowledge sweep.

PASS B:
semantic knowledge audit.

The lexical sweep must create candidate IDs so every candidate can later be reconciled.

Do not silently drop:
- common words in specialized roles;
- abstract process labels;
- scientific labels;
- acronyms;
- classifications;
- evidence methods;
- mechanisms.

## No Silent Ignore

Every lexical candidate must receive one final disposition:
- BASELINE_KNOWN
- GROUNDED
- REPLACED
- REMOVED
- UNRESOLVED

PASS requires:
silently_ignored_candidates = 0

## Independent Reconciliation

Closure reconciles:
- lexical sweep;
- semantic blind inventory;
- Audience Knowledge Graph;
- actual current script.

Check:
- core subject;
- aliases;
- relations;
- dependencies;
- contextual role;
- temporal first use;
- confusable labels;
- graph omissions;
- discovery coverage.

## Knowledge Delta

After every rewrite compare input/output for:
- new_entities
- new_aliases
- new_components
- new_concepts
- new_contextual_roles
- new_relations
- new_dependencies

Every new item must be:
- GROUND
- REPLACE
- REMOVE
- ROUTE_TO_STAGE_06

## Context Scope

Knowledge nodes may include:
- definition_scope
- safe_definition
- unsafe_definition

Do not turn research-specific categories into universal definitions.

## Final Knowledge Counts

Knowledge closure requires:
- core_entities_ungrounded = 0
- unmapped_aliases = 0
- missing_discovered_nodes = 0
- unresolved_concepts = 0
- unresolved_dependencies = 0
- unresolved_relations = 0
- temporal_first_use_failures = 0
- confusable_pairs_unresolved = 0
- silently_ignored_candidates = 0

Final completion additionally requires every gate in FINAL_INTEGRITY_PROTOCOL.md.
