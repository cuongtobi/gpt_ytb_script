# 06B — TERMINOLOGY NECESSITY PRUNER

## Role

Remove labels that are understandable but unnecessary.

Read the normal stage inputs plus CONTENT_ADDRESSING_PROTOCOL.md and FINAL_INTEGRITY_PROTOCOL.md.
Hash every actual input.

## Audit every non-baseline label

Record:
- label
- needed_for_later_reasoning
- reuse_count
- precision_gain
- story_value
- replacement_available
- context_scope
- action: KEEP|KEEP_ONCE|REPLACE|REMOVE
- replacement_text_if_any

Prefer REPLACE/REMOVE when the label is not needed.

## Alias Budget

Enforce primary spoken label and alias policy.
Flag alias_overload when labels alternate without story/precision value.

## Repair safety

Do not add new factual substance.
Replacement language must use baseline or grounded knowledge.
If necessary replacement creates unfamiliar knowledge, route back to stage 06.

## Outputs

Write:
- 06_terminology_prune.json
- 06_script_pruned.md

06_terminology_prune.json includes:
- content_address
- input_script_sha256
- output_script_sha256
- labels_audited
- kept
- kept_once
- replaced
- removed
- unnecessary_labels
- alias_overload
- status

PASS requires unnecessary_labels = 0 and alias_overload = 0.
