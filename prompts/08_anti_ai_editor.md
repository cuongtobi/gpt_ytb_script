# 08 — NATURALNESS, RHYTHM & LISTENING EDITOR

## Role

Make narration sound naturally written and naturally spoken in the target language without breaking facts or knowledge closure.

Read:
- 00_project_brief.yaml
- 03_claim_map.json
- 06_knowledge_closure.json
- 06_terminology_prune.json
- 07_reveal_audit.json
- 07_knowledge_delta.json
- 07_script_retention_edit.md
- prompts/FINAL_INTEGRITY_PROTOCOL.md

## Language-native rule

Judge naturalness by the target language itself.

Preserve regional/formality choices from project brief.

## Naturalness audit

Find:
- translationese
- noun stacking
- academic compression
- abstract nominalization
- overly formal wording
- awkward terminology
- phrases understandable on paper but unnatural in speech

## Rhythm Pattern Audit

Detect:
- repeated sentence openings
- repeated fragments
- parallelism overload
- repeated "not X but Y" structures
- rhetorical-question overload
- repeated contrast templates
- generic crescendo patterns

Intentional repetition may remain only when it clearly serves rhetoric.

## Narration Listening Pass

Assume one listen with no text.

Flag:
- too many unfamiliar labels in one block
- multiple abstract nouns in one sentence
- nested definitions
- long entity chains
- ambiguous pronouns
- dense causal clauses
- date/number stacks without concrete anchor

Repair with:
- concrete verbs
- shorter clauses
- plain language
- sentence splitting
- label removal
- clearer referents

## Knowledge safety

After rewrite run Knowledge Delta.

No new unresolved label/alias/relation may remain.

## Outputs

Write:
- 08_anti_ai_report.md
- 08_naturalness_audit.json
- 08_knowledge_delta.json
- 08_script_natural.md

08_naturalness_audit.json includes:
- translationese_flags
- repeated_rhetorical_patterns
- unresolved_audio_density_flags
- high_load_listening_blocks
- actions_taken
- status

PASS requires all four counts = 0.
