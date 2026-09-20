# 10B — ISOLATED AUDIT HANDOFF

## Purpose

Create truly isolated, content-addressed final audits where runtime capabilities allow it.

## Required isolated runs

Run separately:
- 10B1 knowledge
- 10B2 claims
- 10B3 naturalness

Each starts from a fresh execution context and receives only its allowed inputs.

## Runtime manifest

Only the orchestration runtime may write 10b_isolation_manifest.json.

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
- observed_input_hashes
- forbidden_input_files
- forbidden_input_accessed
- runtime_attested

observed_input_hashes must match each audit artifact's content_address inputs.

## Valid verified isolation

For PASS_VERIFIED:
- manifest_origin = runtime;
- attestation_source identifies the runtime/agent mechanism;
- execution IDs are non-empty and distinct;
- context_mode = fresh;
- runtime_attested = true;
- observed inputs are a subset of allowed inputs;
- observed inputs do not intersect forbidden inputs;
- forbidden_input_accessed = false;
- observed hashes equal current project bytes and audit-declared hashes.

## Fail closed

If the environment cannot create or attest fresh contexts:
isolation_status = ISOLATION_NOT_VERIFIED.

Do not invent execution IDs, runtime attestation or fresh-context claims.
Advisory audits may still run, but project_status cannot be PASS_VERIFIED.
