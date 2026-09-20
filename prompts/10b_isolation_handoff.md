# 10B — ISOLATED AUDIT HANDOFF

## Purpose

Create truly isolated final audits where runtime capabilities allow it.

## Required isolated runs

Run separately:
- 10B1 knowledge
- 10B2 claims
- 10B3 naturalness

Each must start from a fresh execution context.

## Runtime manifest

Only the orchestration runtime may write:
- 10b_isolation_manifest.json

Top-level:
- manifest_origin: runtime
- attestation_source
- isolation_status

Per audit:
- audit_id
- execution_id
- context_mode
- allowed_input_files
- observed_input_files
- forbidden_input_files
- forbidden_input_accessed
- runtime_attested

## Valid verified isolation

For PASS_VERIFIED:
- manifest_origin must be `runtime`;
- attestation_source must identify the runtime/agent mechanism;
- execution IDs must be non-empty and distinct;
- context_mode = fresh;
- runtime_attested = true;
- observed inputs must be a subset of allowed inputs;
- observed inputs must not intersect forbidden inputs;
- forbidden_input_accessed = false.

## Fail closed

If the current environment cannot create or attest fresh contexts:

isolation_status = ISOLATION_NOT_VERIFIED

Do not invent:
- execution IDs
- runtime attestation
- a fresh-context claim

Advisory audits may still run, but project_status cannot be PASS_VERIFIED.
