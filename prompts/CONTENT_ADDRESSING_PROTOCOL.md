# CONTENT ADDRESSING PROTOCOL — v3.3

## Purpose

Prevent stale or misbound audits by proving exactly which bytes each audit read.

## Hash algorithm

Use SHA-256 over exact file bytes as stored in the project.
For text artifacts this means their exact UTF-8 bytes; do not normalize whitespace, Unicode, line endings or final newlines before hashing.

Hash format:
- lowercase hexadecimal
- exactly 64 characters

## Audit envelope

Every audit JSON artifact must include:

{
  "content_address": {
    "hash_algorithm": "sha256",
    "inputs": [
      {
        "path": "relative/project/path",
        "sha256": "..."
      }
    ]
  }
}

Include every input actually read by the audit.
Do not claim an input was unread if the current execution context exposed it to the auditor.

## Script-changing stages

For a stage that compares or rewrites a script, record both:
- input_script_sha256
- output_script_sha256

If they differ, downstream content-addressed audits must use the new output bytes.

## Final audit binding

10B1, 10B2 and 10B3 must each bind to:
- exact final-candidate script bytes;
- exact canonical final sentence index bytes when that audit uses the index.

Before release, 10D requires:
SHA256(10_final_script.md)
==
audited script SHA for B1
==
audited script SHA for B2
==
audited script SHA for B3.

If 10_final_candidate.md is copied byte-for-byte to 10_final_script.md, the hashes naturally match.
If 10C changes text, rerun 10A1 and all B audits.

## Artifact manifest

artifact_manifest.json is generated only after the final text and final audits are stable.

It records SHA-256 for required project artifacts.
10D recomputes all listed hashes and rejects:
- missing files;
- extra declared paths that cannot be resolved;
- duplicate manifest paths;
- any mismatch.

## Fail closed

Never repair a hash mismatch by editing the recorded hash alone.
Regenerate the stale artifact from the current inputs.
