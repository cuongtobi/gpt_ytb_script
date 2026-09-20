# KNOWLEDGE GROUNDING PROTOCOL — v3

## Purpose

This is the shared source of truth for audience understanding.

The pipeline does not merely manage technical terms. It manages what the audience knows at each point in the narration.

A script can fail even when every tracked technical term is eventually defined.

Examples of failure:
- the topic itself is familiar by name but never grounded as an object;
- an alias appears before the viewer knows what it refers to;
- THC appears before the viewer knows it is a compound made by cannabis;
- a definition introduces an unexplained dependency;
- a concept is explained later, after its first use;
- the final script contains a concept absent from the old graph.

The pipeline therefore uses an Audience Knowledge Graph plus Temporal Knowledge Closure.

---

## 1. Knowledge node types

Track all story-relevant knowledge that may require grounding.

Node types:
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

Do not turn ordinary vocabulary into a glossary.

---

## 2. Relationship types

Use explicit semantic relationships when useful:

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

A relationship itself can be unknown and require grounding.

---

## 3. Core Subject Grounding

Every project must identify one or more CORE_ENTITY nodes.

For each core entity, distinguish:

- label_familiarity: has the viewer heard the name?
- subject_understanding: does the viewer know what kind of thing it is and which properties matter to this story?

High label familiarity does NOT imply adequate subject understanding.

A core entity needs minimum story-relevant grounding:
- what kind of thing it is;
- which properties/parts matter to this story;
- which names refer to it;
- which related labels are not exact aliases.

Example:
"Cần sa" may be familiar as a word while the viewer may not know it is a plant used for seed, fiber, flowers/resin and chemically active compounds.

### Core label exception

The common topic label may appear in the title or first hook line before full grounding.

However, before the narration uses:
- a scientific name;
- a specialized alias;
- a component;
- a mechanism;
- a claim that depends on understanding the entity's nature;

the minimum grounding must already be present in the same sentence or earlier.

---

## 4. Alias Resolution

Never assume the audience knows that two labels refer to the same or overlapping thing.

Every nontrivial alternate label must have a relationship:
- ALIAS_OF
- SHORT_FORM_OF
- RELATED_TO
- SUBTYPE_OF
- or another explicit relationship

An alias or related label cannot be freely alternated until the relationship has been grounded.

If the label is unnecessary, REMOVE it.

---

## 5. Minimum Grounding Requirement

Do not teach more than the story requires.

Each required node should define minimum_grounding: the smallest set of facts the viewer needs to follow later reasoning.

Example:

THC:
- is_what: a compound made by cannabis;
- story_role: strongly associated with intoxicating effects.

Not required:
- molecular structure;
- receptor pharmacology;
- biosynthetic pathway.

---

## 6. Knowledge states

Each knowledge node has one current state:

- BASELINE_KNOWN
- GROUNDED
- UNRESOLVED
- REMOVED

BASELINE_KNOWN is strictly controlled.

A node may be BASELINE_KNOWN only if:
1. it appears explicitly in the project audience baseline; or
2. it is a normal-language primitive declared by that baseline policy.

A downstream stage may NOT self-declare a new technical, scientific, historical or specialized item as known merely because it feels familiar.

High label familiarity is not the same as BASELINE_KNOWN.

---

## 7. No Unknowns in Explanations

A node is not GROUNDED if its explanation requires another unresolved node or relation.

For every explanation:
1. extract dependencies;
2. validate every dependency;
3. simplify, replace or remove unnecessary labels;
4. recurse until dependencies terminate at BASELINE_KNOWN or earlier GROUNDED nodes.

---

## 8. Temporal Knowledge Closure

Documentary narration is linear.

Eventually explained is NOT good enough.

For every required node record:
- first_use position;
- grounded_at position.

PASS requires:

grounded_at <= first_use

or grounding occurs inside the same first-use sentence before the unfamiliar label becomes necessary.

If:
- genome appears in the opening;
- genome is defined several minutes later;

that is a temporal failure.

---

## 9. Blind Knowledge Discovery

A blind auditor must discover knowledge from the current script without seeing the previous knowledge graph.

Required inputs only:
- project audience profile;
- current script.

Do NOT provide:
- 03_knowledge_graph.json;
- earlier closure reports;
- earlier knowledge inventories.

The auditor extracts:
- entities;
- aliases;
- components;
- processes;
- mechanisms;
- technical concepts;
- specialized contextual roles;
- relationships required to understand claims.

This prevents graph-confirmation bias.

---

## 10. Independent reconciliation

After blind discovery, a separate closure stage reconciles:

BLIND INVENTORY
+
AUDIENCE KNOWLEDGE GRAPH
+
CURRENT SCRIPT

Questions:
- Did blind discovery find nodes absent from the graph?
- Are aliases mapped?
- Are required relations grounded?
- Is the core subject grounded?
- Are dependencies resolved?
- Is each node grounded before or at first use?
- Are confusable labels distinguished?

A graph missing a blind-discovered node is itself a failure until repaired.

---

## 11. Knowledge Delta after rewrites

Every stage that rewrites narration must compare input vs output for:

- new_entities
- new_aliases
- new_components
- new_concepts
- new_contextual_roles
- new_relations
- new_dependencies

Each delta item must be:
- GROUND
- REPLACE
- REMOVE
- ROUTE_TO_STAGE_06

No rewrite stage may introduce unresolved knowledge and still PASS.

---

## 12. Necessity test

For every unfamiliar label or relationship ask:

Does the viewer need this exact label or relationship to follow later reasoning?

If YES:
- GROUND it.

If the idea matters but the label does not:
- REPLACE with plain language.

If neither matters:
- REMOVE.

Prefer replacement/removal over glossary expansion.

---

## 13. Confusable labels

If two labels can be confused and both remain:
- explicitly distinguish their roles at first introduction.

Examples:
- lactose vs lactase;
- hemp vs drug-type cannabis;
- common name vs scientific name where needed.

---

## 14. Required final gate

Final Knowledge Closure PASS requires all values to be zero:

- core_entities_ungrounded
- unmapped_aliases
- missing_discovered_nodes
- unresolved_concepts
- unresolved_dependencies
- unresolved_relations
- temporal_first_use_failures
- confusable_pairs_unresolved

The pipeline cannot be marked complete otherwise.
