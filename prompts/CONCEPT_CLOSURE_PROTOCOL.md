# CONCEPT CLOSURE PROTOCOL

## Purpose

This is the shared source of truth for concept accessibility across the pipeline.

It prevents concept leakage: a concept is explained using another concept the audience does not understand, or a rewrite introduces a new unfamiliar concept after the initial graph was created.

A script cannot pass merely because its originally tracked concepts were explained. The actual current script must reach concept closure.

## Core model

Use a dynamic Concept Dependency Graph, not a static glossary.

A concept is resolved only when every dependency required to understand its use is already KNOWN or EXPLAINED earlier in the narration.

If an explanation introduces another unfamiliar concept, that new concept becomes a dependency and must be resolved recursively.

## Concept states

Every concept carrying factual, causal, technical or narrative meaning has one state:

- KNOWN: reasonably understood by the target audience in the role used here.
- EXPLAINED: introduced in plain language and all required dependencies are KNOWN or already EXPLAINED.
- UNRESOLVED: present but unexplained, dependent on an unexplained concept, contextually unfamiliar, or still confusable with another concept.
- REMOVED: unnecessary label/detail replaced by simpler wording or deleted.

Do not mark a concept KNOWN merely because its word is familiar. Label familiarity and role familiarity are different.

## No Unknowns in Definitions

Hard rule:

A concept is NOT explained if its explanation requires another unexplained concept.

Example failure:
Lactase is an enzyme that breaks down lactose.

This is not closed if enzyme or lactose is not understood.

Closed sequence:
Lactose is the natural sugar in milk.
The small intestine uses an enzyme called lactase to break that sugar down.

## Concept record

Recommended fields:

- concept_id
- name
- aliases
- status
- label_familiarity
- role_familiarity
- importance
- technical_term_required
- necessity: required | replaceable | removable
- definition.text
- definition.dependencies
- confusable_with
- first_use_strategy
- reuse_policy

Each dependency records:
- name
- relationship
- status

## Contextual familiarity

Always distinguish LABEL FAMILIARITY from ROLE FAMILIARITY.

A familiar label can still be unfamiliar in the mechanism currently being explained.

Example: calcium may be familiar from nutrition, but calcium dissolving and recrystallizing inside a concrete crack is a specialized role.

If role familiarity is low, explain the role, replace the label with concrete wording, or remove it.

## Necessity test

Before teaching a technical label ask:

Does the viewer need this label to understand later reasoning?

Choose one:
- EXPLAIN: concept/label is needed later.
- REPLACE: underlying idea matters but label does not.
- REMOVE: neither label nor detail is needed.

Prefer REPLACE or REMOVE over glossary-like definitions.

## Confusable concepts

If two concepts are easily confused and both appear, explicitly distinguish their roles at first introduction.

Example:
Lactose is the sugar in milk.
Lactase is different: it is the enzyme that helps break lactose down.

The confusable_with field creates an editorial obligation.

## Full Script Concept Discovery

Concept audits must scan the current script from scratch.

Never limit discovery to concepts already present in the Initial Concept Graph.

Extract unfamiliar or cognitively expensive:
- scientific terms and mechanisms
- acronyms
- historical institutions
- technical processes
- specialist classifications
- legal/economic concepts
- unfamiliar causal roles
- common words used in a specialized role

Do not turn ordinary vocabulary into a glossary.

## Concept Delta Scan

After every stage that rewrites narration, compare INPUT SCRIPT CONCEPTS vs OUTPUT SCRIPT CONCEPTS.

Record newly introduced concepts and contextual roles.

For every new concept choose:
- EXPLAIN
- REPLACE
- REMOVE
- ROUTE_TO_CLOSURE_EDITOR

No new concept may become invisible merely because it was introduced after stage 03.

## Recursive closure algorithm

For each concept in the current script:

1. Determine whether its role in this context is KNOWN.
2. If not KNOWN, inspect its first use.
3. If explanation is absent, mark UNRESOLVED.
4. If explanation exists, extract every concept required to understand that explanation.
5. For each dependency:
   - KNOWN: continue.
   - EXPLAINED earlier: continue.
   - otherwise: mark dependency UNRESOLVED.
6. Apply necessity test.
7. Repair by explaining dependencies first, replacing the label, or removing it.
8. Repeat discovery and dependency checks until a full pass creates no new unresolved concept.

That fixed point is concept closure.

## Weighted concept load

Suggested warning heuristic:
- KNOWN concept: 0
- simple new concept: 1
- technical/abstract new concept: 2
- confusable pair: +1
- dependency depth greater than 1: +1
- specialized contextual role: +1

Use judgment, not a mechanical target.

## Closure artifact

A closure artifact is both:
1. a gate summary, and
2. the current resolved graph snapshot.

Report:
- concepts_detected
- known
- explained
- removed
- unresolved
- concepts: full current concept nodes with state, first use, definition, dependencies and confusable relationships
- dependency_edges: full current dependency edges
- unresolved_dependencies
- confusable_pairs_unresolved
- new_concepts_discovered
- closure_iterations
- status

PASS requires:
- unresolved = 0
- unresolved_dependencies = 0
- confusable_pairs_unresolved = 0

## Final Concept Closure Gate

The final editor must rebuild the concept inventory from the final candidate narration itself.

Do not trust an earlier PASS.

Every meaningful concept in the final script must be KNOWN, EXPLAINED before or at first use, or REMOVED.

If a final edit creates a new concept, rescan.

The pipeline is not complete until the scan reaches a stable fixed point with UNRESOLVED = 0.
