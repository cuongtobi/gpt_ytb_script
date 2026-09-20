# 10B — ISOLATED AUDIT HANDOFF

## Purpose

Create blind-audit input packets without pretending same-context execution is isolated.

## Required isolated runs

Run separately:
- 10B1 knowledge audit
- 10B2 claim audit
- 10B3 naturalness audit

Each must start from a fresh model/agent/chat context.

## Runtime manifest

The orchestration runtime, not the auditor, writes:
- 10b_isolation_manifest.json

For each audit:
- audit_id
- execution_id
- context_mode
- allowed_input_files
- observed_input_files
- forbidden_input_files
- forbidden_input_accessed
- runtime_attested

## Fail closed

If the current environment cannot create or attest fresh contexts:

isolation_status = ISOLATION_NOT_VERIFIED

Do not invent execution IDs.
Do not self-attest from the auditor prompt.

The project may continue for advisory audit, but cannot become PASS_VERIFIED.
