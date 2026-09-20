# 03A — CORE SUBJECT GROUNDING

## Role

Build the minimum mental model the target audience needs for the central subject before specialized names, components or mechanisms are used.

Read:
- 00_project_brief.yaml
- 01_angle.md
- 02_research_notes.md
- prompts/KNOWLEDGE_GROUNDING_PROTOCOL.md
- prompts/FINAL_INTEGRITY_PROTOCOL.md

Do not write narration.

## Core entity record

For each central subject record:
- canonical_name
- audience_name
- entity_type
- label_familiarity
- subject_understanding
- minimum_grounding
- aliases
- related_but_not_equivalent_labels
- relevant_parts_or_components
- story_relevant_properties
- labels_recommended_for_removal

## Topic-familiarity trap

Do not assume the viewer understands the subject because the label is common.

Ask:
- What kind of thing is it?
- Which parts/properties matter to this story?
- Which alternate names will appear?
- Which related names are not exact synonyms?
- What must be known before the first specialized claim?

## Entity Label Policy

Create:
- primary_spoken_label
- scientific_alias_policy
- allowed_reuse_aliases
- discouraged_reuse_aliases
- removed_aliases

Prefer one primary spoken label.

A scientific name may appear once or be reused only when it adds precision/story value.

Do not multiply aliases unnecessarily.

## Output

Write:
- 03_core_subject.json

Include:
- core_entities
- alias_map
- entity_label_policy
- minimum_grounding_requirements
- first_specialized_use_dependencies
- labels_recommended_for_removal
- status
