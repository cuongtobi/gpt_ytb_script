# AGENTS.md

## Repository purpose

Prompt-native pipeline for research-driven YouTube documentary narration with strong visual storytelling and audience knowledge grounding.

Runs on ChatGPT Web + GitHub.

## Source of truth

For new projects:
1. Read AGENTS.md.
2. Read prompts/00_orchestrator.md.
3. Read prompts/KNOWLEDGE_GROUNDING_PROTOCOL.md.
4. Follow stage prompts in order.
5. Persist all required artifacts.
6. Final production artifact is 10_final_script.md.

## Pipeline v3

00 Orchestrator
→ 01 Angle
→ 02 Research
→ 03A Core Subject Grounding
→ 03B Claim Map + Audience Knowledge Graph
→ 04 Story + Knowledge Architect
→ 05 Writer
→ 05B Blind Knowledge Discovery
→ 06 Audience Knowledge Closure
→ 07 Retention + Knowledge Delta
→ 08 Anti-AI + Knowledge Delta
→ 09 Fact Check + Knowledge Delta
→ 10A Final Story Editor
→ 10B Blind Final Knowledge Audit
→ 10C Final Temporal Knowledge Closure

## Non-goals

Unless explicitly requested, do not create:
- storyboard
- shot list
- image prompts
- B-roll plan
- camera directions
- visual timeline
- editing timeline
- video-generation prompts

Visual storytelling belongs inside narration.

## Core principles

### Story before prose
Architecture first.

### Understanding before terminology
Do not teach labels the story does not need.

### Core subject before specialized claims
A familiar topic name is not proof that the viewer understands the subject.

### Alias relationships must be explicit
Do not freely switch names before mapping them.

### Known is strict
A node is BASELINE_KNOWN only if supported by the audience baseline.

### No Unknowns in Explanations
An explanation cannot depend on unresolved knowledge.

### Temporal closure
Eventually explained is not enough. Ground before or at first use.

### Blind discovery
Blind stages must not read the prior knowledge graph.

### Evidence before drama
Do not overstate sources.

### Language-native editing
Judge naturalness in the target language.

## Blind-stage input isolation

05B allowed:
- 00_project_brief.yaml
- 05_script_draft.md
- KNOWLEDGE_GROUNDING_PROTOCOL.md

10B allowed:
- 00_project_brief.yaml
- 10_final_candidate.md
- KNOWLEDGE_GROUNDING_PROTOCOL.md

Do not preload graph/closure artifacts into these stages.

## Completion

Do not claim complete unless:
- factual audit PASS;
- final knowledge closure PASS;
- all eight knowledge failure counts are zero;
- final story QC PASS;
- final script exists;
- duration is reasonable.

## Legacy

v1/v2 project artifacts may contain:
- 03_concept_map.json
- 03_concept_graph.json
- concept_delta files
- concept_closure files

Do not use legacy schemas for new projects.
