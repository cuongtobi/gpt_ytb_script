# AGENTS.md

## Repository purpose

Research-driven YouTube documentary narration with strong storytelling and proof-carrying integrity checks.

Runs primarily on ChatGPT Web + GitHub.

## Source of truth for new projects

Read:
1. AGENTS.md
2. prompts/00_orchestrator.md
3. prompts/KNOWLEDGE_GROUNDING_PROTOCOL.md
4. prompts/FINAL_INTEGRITY_PROTOCOL.md
5. prompts/INTEGRITY_PROOF_PROTOCOL.md

## Current pipeline: v3.2

v3.2 fixes four v3.1 false-PASS classes:

1. lexical sweep completeness
2. temporal first-use proof
3. candidate-by-candidate conservation
4. real blind-audit isolation

## Core design

### Creative lane
Story, prose, retention and naturalness remain flexible.

### Integrity lane
Auditors must provide machine-checkable proof.

Do not make the writer produce glossary prose just to satisfy audit counters.

### Minimal intervention
Prefer:
REMOVE → REPLACE → REORDER → minimal grounding.

### Fail closed
Missing proof is failure.

### Isolation honesty
Same-chat sequential audit is not verified isolation.

If fresh execution contexts cannot be attested:
project_status must not be PASS_VERIFIED.

## Non-goals

No storyboard, shot list, image prompts, B-roll, camera directions or visual timeline unless explicitly requested.

## Final source of truth

For v3.2:
- 10_final_integrity.json
- 10d_proof_verification.json

PASS_VERIFIED requires both content and proof gates.
