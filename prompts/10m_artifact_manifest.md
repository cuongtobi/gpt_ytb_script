# 10M — ARTIFACT MANIFEST

## Role

Generate the project artifact manifest only after the final candidate, final index, B1/B2/B3, reconciliation and released final script are stable.

Read:
- CONTENT_ADDRESSING_PROTOCOL.md
- required artifact list from 00_orchestrator.md
- current project files

Do not edit any upstream artifact.

## Output

Write artifact_manifest.json:

{
  "pipeline_version": "3.3",
  "artifact_schema_version": "3.3.0",
  "segmenter_version": "3.3.0",
  "inputs": {...},
  "outputs": {...},
  "hashes": {
    "relative/path": "<sha256>"
  }
}

## Rules

- SHA-256 is over exact current file bytes.
- Each path appears once.
- Include every required machine-readable proof artifact and every final script/index/audit input.
- Do not include artifact_manifest.json's own hash inside itself.
- If any upstream file changes after manifest generation, regenerate the manifest before 10D.

Prefer tools/build_artifact_manifest.py when Python is available.
