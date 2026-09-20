# 06B — TERMINOLOGY NECESSITY PRUNER

## Role

Remove labels that are understandable but unnecessary.

Read:
- 00_project_brief.yaml
- 03_core_subject.json
- 03_knowledge_graph.json
- 06_knowledge_closure.json
- 06_script_accessible.md
- prompts/FINAL_INTEGRITY_PROTOCOL.md

Do not add new factual substance.

## Audit every non-baseline label

Record:
- label
- needed_for_later_reasoning
- reuse_count
- precision_gain: high|medium|low|none
- story_value: high|medium|low|none
- replacement_available
- context_scope
- action: KEEP|KEEP_ONCE|REPLACE|REMOVE
- replacement_text_if_any

## Hard pruning preference

If:
needed_for_later_reasoning = false
AND replacement_available = true

prefer REPLACE or REMOVE.

A label is not justified merely because stage 06 successfully explained it.

## Alias Budget

For each core entity enforce:
- primary_spoken_label
- scientific_alias_policy
- allowed_reuse_aliases
- discouraged_reuse_aliases
- removed_aliases

Flag alias_overload when the narration alternates labels without story/precision value.

## Context scope

For retained category labels ensure definition is scoped correctly.

Do not universalize study-specific labels.

## Repair

Produce a full revised script.

After pruning, verify removal does not:
- create ambiguity;
- break a dependency;
- change factual meaning.

## Outputs

Write:
- 06_terminology_prune.json
- 06_script_pruned.md

06_terminology_prune.json includes:
- labels_audited
- kept
- kept_once
- replaced
- removed
- unnecessary_labels
- alias_overload
- entity_label_policy_after_prune
- status

PASS requires:
- unnecessary_labels = 0
- alias_overload = 0
