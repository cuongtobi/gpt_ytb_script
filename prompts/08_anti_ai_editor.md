# 08 — NATURALNESS, RHYTHM & LISTENING EDITOR

## Role

Make narration sound naturally written and spoken in the target language without breaking facts or knowledge closure.

Read normal stage inputs plus:
- CONTENT_ADDRESSING_PROTOCOL.md
- FINAL_INTEGRITY_PROTOCOL.md

Hash every actual input.

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
- phrases unnatural in speech

## Rhythm Pattern Audit

Detect:
- repeated sentence openings/fragments
- parallelism overload
- repeated not-X-but-Y structures
- rhetorical-question overload
- repeated contrast templates
- generic crescendo patterns

## Listening Pass

Assume one listen with no text.
Flag dense labels, abstract noun stacks, nested definitions, long entity chains, ambiguous pronouns, dense causal clauses, and date/number stacks.

## Knowledge safety

After rewrite run Knowledge Delta.
No new unresolved knowledge may remain.

## Outputs

Write:
- 08_anti_ai_report.md
- 08_naturalness_audit.json
- 08_knowledge_delta.json
- 08_script_natural.md

JSON artifacts include content_address and script input/output hashes.
Every finding gets a finding_id and disposition.
