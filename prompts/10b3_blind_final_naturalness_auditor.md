# 10B3 — BLIND FINAL NATURALNESS/REDUNDANCY AUDITOR

## Independence

MUST NOT read:
- 07 retention report/reveal audit
- 08 anti-AI/naturalness report
- 06 terminology prune
- previous naturalness judgments

Allowed:
- 00_project_brief.yaml
- 10_final_candidate.md
- prompts/FINAL_INTEGRITY_PROTOCOL.md

## Role

Read the final candidate as a listener, not an editor who already knows the pipeline.

Find:
- translationese
- academic compression
- noun stacking
- unnecessary aliases/labels
- duplicate reveals
- repeated sentence openings
- fragment-pattern repetition
- parallelism overload
- rhetorical-question overload
- repeated contrast templates
- awkward terminology
- high audio density
- unclear pronouns

For duplicate reveal candidates record:
- normalized meaning
- evidence
- occurrences
- likely story function

For rhythm candidates record:
- pattern
- occurrences in block
- severity

## Output

Write:
- 10b3_blind_naturalness_audit.json

Include:
- translationese_candidates
- unnecessary_label_candidates
- duplicate_reveal_candidates
- repeated_rhetorical_pattern_candidates
- audio_density_candidates
- alias_overload_candidates
