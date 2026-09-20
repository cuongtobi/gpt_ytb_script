# AGENTS.md

## Repository purpose

This repository is a prompt-native pipeline for creating research-driven YouTube documentary narration with strong visual storytelling.

It runs through ChatGPT Web with GitHub access. It does not require a local runtime, Python app, Node app, CI workflow or external orchestration service.

## Source of truth

When asked to create a new script:

1. Read this file.
2. Read prompts/00_orchestrator.md.
3. Read prompts/CONCEPT_CLOSURE_PROTOCOL.md.
4. Follow stage prompts in numerical order.
5. Use web research when requested or required for freshness/verification.
6. Create a new directory under projects/.
7. Persist every required artifact before moving to dependent stages.
8. Final production artifact is 10_final_script.md.

## Pipeline

00 Orchestrator
→ 01 Angle Engine
→ 02 Researcher
→ 03 Claim Map + Initial Concept Graph
→ 04 Story Architect
→ 05 Visual Narrative Writer + Concept Delta
→ 06 Audience + Recursive Concept Closure
→ 07 Retention Editor + Concept Delta
→ 08 Anti-AI Editor + Concept Delta
→ 09 Fact Checker + Concept Delta
→ 10 Final Story Editor + Final Concept Closure

## Non-goals

Do not create unless explicitly requested:
- storyboard
- shot list
- image prompts
- image-generation plan
- B-roll list
- camera directions
- visual timeline
- editing timeline
- video-generation prompts

Visual storytelling means narration itself creates clear mental images through scenes, actions, objects, transformations, contrasts, scale and human decisions.

## Required principles

### Story before prose
Do not draft the full script before story architecture exists.

### Understanding before terminology
Do not make a general audience learn a technical label unless the label is needed.

### Concrete before abstract
Prefer actions, objects, scenes, changes and contrasts before abstraction.

### Evidence before drama
Never strengthen certainty, precision or causation beyond sources.

### Language-native editing
Judge naturalness according to the target language itself.

### Dynamic concepts, not a static glossary
03_concept_graph.json is only an initial graph.

The current narration must be rescanned after every rewrite.

### No Unknowns in Definitions
A concept is not explained if its explanation depends on another unresolved concept.

### Final closure from actual final script
Stage 10 must rebuild concept inventory from the final candidate. Earlier PASS results are not enough.

## Project isolation

Every run creates a unique directory:
projects/YYYY-MM-DD_topic-slug/

Append _02, _03 and so on if needed.

Never overwrite previous projects unless explicitly requested.

## Stage dependencies

- 01 depends on 00
- 02 depends on 00 + 01
- 03 depends on 02
- 04 depends on 00 + 01 + 02 + 03
- 05 depends on 04 + Claim Map + Concept Graph
- 06 depends on 05 + Concept Delta + Concept Graph
- 07 depends on stage 06 closure PASS
- 08 depends on stage 07 concept delta PASS
- 09 depends on stage 08 concept delta PASS + Claim Map + sources
- 10 depends on all current artifacts + stage 09 factual PASS

If stage 07 or 08 introduces an unresolved concept, route the current narration back to stage 06 before continuing.

If a downstream editor changes factual substance, stage 09 must recheck it.

## Research discipline

Prefer:
- primary sources
- peer-reviewed research
- official institutions
- high-quality reference works
- reputable reporting

For each important claim record:
- source
- source date
- confidence
- direct evidence vs inference
- caveats

Do not manufacture probabilities, citations, quotations, dates or conclusions.

## Concept discipline

Use the shared Concept Closure Protocol.

Each concept may include:
- label familiarity
- contextual role familiarity
- necessity
- dependencies
- status
- first-use strategy
- confusable concepts
- reuse policy

States:
- KNOWN
- EXPLAINED
- UNRESOLVED
- REMOVED

Required closure:
- unresolved = 0
- unresolved_dependencies = 0
- confusable_pairs_unresolved = 0

Prefer EXPLAIN only when the term is needed.
Otherwise REPLACE or REMOVE.

## Reporting language

Unless user requests otherwise:
- final narration uses requested script language
- intermediate reports use requested script language
- source titles may remain original

## Completion rule

Do not claim complete unless:
- all required artifacts exist
- factual audit PASS
- final concept closure PASS
- 10_final_story_report passes quality gates
- 10_final_script.md exists
- duration is reasonably aligned with target

## User-facing completion response

Include:
- project path
- selected angle
- approximate word count / duration
- fact-check PASS/FAIL
- concept-closure PASS/FAIL
- final script path
- material limitations only
