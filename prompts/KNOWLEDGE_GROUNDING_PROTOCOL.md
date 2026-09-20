# KNOWLEDGE GROUNDING PROTOCOL — v3.3

## Purpose

Manage what the audience knows at each point in narration without forcing glossary-style writing.

Use together with:
- CONTENT_ADDRESSING_PROTOCOL.md
- FINAL_INTEGRITY_PROTOCOL.md
- INTEGRITY_PROOF_PROTOCOL.md

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

Familiar label != subject understanding.

Before specialized aliases/components/mechanisms rely on the subject, ground the minimum story-relevant mental model.

## Knowledge states

- BASELINE_KNOWN
- GROUNDED
- UNRESOLVED
- REMOVED

## Strict baseline provenance

BASELINE_KNOWN is valid only if:
1. exact phrase is in audience_baseline.assumed_known; or
2. phrase is explicitly mapped to a declared normal_language_primitive.

Every BASELINE_KNOWN result carries machine-auditable provenance.

No inferred known.

## No Unknowns in Explanations

A grounding explanation cannot depend on unresolved knowledge.

Recursively ground, replace or remove dependencies.

## Temporal Knowledge Closure

Eventually explained is not enough.

Every retained unfamiliar candidate must have temporal proof using canonical sentence IDs.

## Blind discovery

Discovery uses the content-addressed canonical sentence index.

Every sentence ID must have a lexical-ledger row, including zero-candidate sentences.

Every candidate later receives exactly one disposition.

## Candidate conservation

Final reconciliation must satisfy:

DISCOVERED
=
BASELINE_KNOWN
+ GROUNDED
+ REPLACED
+ REMOVED
+ UNRESOLVED

No missing or duplicated candidate IDs.

## Terminology principle

Do not explain what the story can avoid naming.

Prefer:
REMOVE → REPLACE → REORDER → MINIMAL GROUNDING.

## Knowledge Delta

After each rewrite compare:
- new_entities
- new_aliases
- new_components
- new_concepts
- new_contextual_roles
- new_relations
- new_dependencies

Each delta artifact must be content-addressed to the exact input and output script bytes.

## Final knowledge proof

Knowledge PASS requires:
- all normal knowledge counters = 0
- sentence coverage valid
- candidate conservation valid
- temporal proof valid
- baseline provenance valid
- all audit hashes valid
