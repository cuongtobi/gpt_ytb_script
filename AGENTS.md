# AGENTS.md

## Repository purpose

Research-driven YouTube documentary narration with strong storytelling and machine-checkable integrity proofs.

Runs primarily on ChatGPT Web + GitHub.

## Source of truth for new projects

Read:
1. AGENTS.md
2. prompts/00_orchestrator.md
3. prompts/CONTENT_ADDRESSING_PROTOCOL.md
4. prompts/KNOWLEDGE_GROUNDING_PROTOCOL.md
5. prompts/EVIDENCE_PROVENANCE_PROTOCOL.md
6. prompts/FINAL_INTEGRITY_PROTOCOL.md
7. prompts/INTEGRITY_PROOF_PROTOCOL.md

## Current pipeline: v3.3

v3.3 extends v3.2 proof-carrying integrity with:

1. content-addressed audits using SHA-256
2. sentence-complete blind claim discovery
3. claim conservation
4. deterministic verification of B1, B2 and B3
5. hard-counter recomputation from proof records
6. JSON Schema contracts for machine-readable artifacts
7. claim → evidence → source provenance
8. locale-aware sentence segmentation
9. adversarial/mutation regression tests
10. artifact manifest and stale-audit detection
11. deterministic post-10D TTS export for vi/en/de/fr/es/ko/ja

## Core design

### Creative lane
Story, prose, retention and naturalness remain flexible.

### Integrity lane
Auditors must provide machine-checkable proof and bind their outputs to exact input bytes.

Do not make the writer produce glossary prose just to satisfy audit counters.

### Minimal intervention
Prefer:
REMOVE → REPLACE → REORDER → minimal grounding.

### Fail closed
Missing proof, hash mismatch, stale audit, missing schema fields or unresolved candidate/claim/finding = failure.

### Isolation honesty
Same-chat sequential audit is not verified isolation.

If fresh execution contexts cannot be attested:
project_status must not be PASS_VERIFIED.

## Content-addressing rule

Every audit artifact must record SHA-256 for every input it actually used.
Final B1/B2/B3 audit script hashes must equal the released 10_final_script.md hash.
Any final-text change invalidates the final sentence index and all three final blind audits.

## TTS publication output

After 10D content proof passes, run Stage 11 to create:
- `final.txt` — plain UTF-8 narration ready for TTS;
- `11_tts_export.json` — content-addressed export report.

Stage 11 is presentation-only. It must not translate, paraphrase, add facts, change claim strength, or invent pronunciations.

## Non-goals

No storyboard, shot list, image prompts, B-roll, camera directions or visual timeline unless explicitly requested.

## Final source of truth

For v3.3:
- artifact_manifest.json
- 10_final_integrity.json
- 10d_proof_verification.json

PASS_VERIFIED requires all content, provenance, schema, hash, conservation, temporal and isolation gates to pass.

`final.txt` is a downstream publication artifact, not an integrity source of truth.
