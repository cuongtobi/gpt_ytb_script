# 03A — CORE SUBJECT GROUNDING

## Role

Build the minimum mental model the target audience needs for the central subject before the story uses specialized names, components or mechanisms.

Read:
- 00_project_brief.yaml
- 01_angle.md
- 02_research_notes.md
- prompts/KNOWLEDGE_GROUNDING_PROTOCOL.md

Do not write narration.

## Identify core entity

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
- labels_to_remove_if_unnecessary

## Topic-familiarity trap

Do not assume the audience understands the subject simply because the topic name is common.

Ask:
- What kind of thing is it?
- Which parts/properties matter to THIS story?
- Which alternate names will appear?
- Which related names are not exact synonyms?
- What must the viewer know before the first specialized claim?

## Minimum grounding

Keep it short and story-relevant.

Do not turn this into a dictionary definition or encyclopedic overview.

## Alias mapping

Classify each alternate label with an explicit relationship:
- ALIAS_OF
- SHORT_FORM_OF
- RELATED_TO
- SUBTYPE_OF

Do not mark overlapping labels as synonyms unless sources and context support that.

## Output

Write:
- 03_core_subject.json

Required top-level fields:
- core_entities
- alias_map
- minimum_grounding_requirements
- first_specialized_use_dependencies
- labels_recommended_for_removal
- status
