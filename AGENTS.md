# AGENTS.md

## Repository purpose

This repository is a prompt-native pipeline for creating research-driven YouTube documentary narration with strong visual storytelling.

The pipeline runs through ChatGPT Web with GitHub access. It does **not** require a local runtime, package manager, Python application, Node application, CI workflow, or external orchestration service.

## Source of truth

When asked to create a new script:

1. Read this file.
2. Read `prompts/00_orchestrator.md`.
3. Follow the stage prompts in numerical order.
4. Use web research when the task requests research or when factual freshness/verification is needed.
5. Create a new directory under `projects/`.
6. Persist every required artifact before moving to dependent stages.
7. The final production artifact is `10_final_script.md`.

## Pipeline

```text
00 Orchestrator
01 Angle Engine
02 Researcher
03 Claim + Concept Mapper
04 Story Architect
05 Visual Narrative Writer
06 Audience + Concept Editor
07 Retention Editor
08 Anti-AI Editor
09 Fact Checker
10 Final Story Editor
```

## Non-goals

Do not create any of the following unless the user explicitly asks for a separate workflow:

- storyboard;
- shot list;
- image prompts;
- image-generation plan;
- B-roll list;
- camera directions;
- visual timeline;
- editing timeline;
- video-generation prompts.

“Visual storytelling” means the narration itself should create clear mental images through scenes, actions, objects, transformations, contrasts, scale and human decisions.

## Required principles

### Story before prose
Do not draft the full script before the story architecture exists.

### Understanding before terminology
Do not make a general audience learn a technical label unless the label is necessary.

### Concrete before abstract
Prefer concrete actions, objects, scenes, changes and contrasts before abstract explanation.

### Evidence before drama
Never strengthen certainty, precision or causation beyond what the source supports.

### Language-native editing
Naturalness must be judged according to the target language itself. Do not use English or Vietnamese as a universal stylistic reference.

## Project isolation

Every run must create a unique project directory.

Recommended slug:

```text
projects/YYYY-MM-DD_<topic-slug>/
```

If that path already exists, append `_02`, `_03`, etc.

Never overwrite artifacts from a previous project unless the user explicitly asks to update that project.

## Stage dependencies

- 01 depends on 00.
- 02 depends on 00 + 01.
- 03 depends on 02.
- 04 depends on 00 + 01 + 02 + 03.
- 05 depends on 04 + Claim Map + Concept Map.
- 06 depends on 05 + Concept Map.
- 07 depends on 06 + 04.
- 08 depends on 07.
- 09 depends on 08 + Claim Map + sources.
- 10 depends on all current upstream artifacts.

If a downstream editor changes factual substance, the changed claim must be rechecked by stage 09.

## Research discipline

Prefer primary sources, peer-reviewed research, official institutions, high-quality reference works and reputable reporting.

For each important factual claim record:

- source;
- source date;
- access date when useful;
- confidence;
- whether the wording is direct evidence, inference or disputed interpretation.

Do not manufacture probability values, citations, quotations, dates or study conclusions.

## Concept discipline

Track unfamiliar concepts before script drafting.

Each concept should include:

- audience familiarity;
- importance;
- technical-term requirement;
- first-use strategy;
- plain-language explanation;
- reuse policy.

Default concept protocol:

```text
mental model / familiar action
→ plain-language explanation
→ technical label only if needed
```

## Reporting language

Unless the user requests otherwise:

- final narration uses the requested script language;
- intermediate reports use the requested script language;
- source titles may remain in their original language.

## Completion rule

Do not claim the pipeline is complete unless:

- all required artifacts exist;
- 09_fact_check contains no unresolved material unsupported claim;
- 10_final_story_report passes the quality gates;
- 10_final_script.md exists and fits the requested duration within a reasonable narration-rate tolerance.

## User-facing completion response

Keep the completion response compact. Include:

- project path;
- selected angle;
- approximate final word count / duration;
- whether fact check passed;
- link or reference to `10_final_script.md`;
- notable limitations only if they materially affect the script.
