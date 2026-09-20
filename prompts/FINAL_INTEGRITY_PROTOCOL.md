# FINAL INTEGRITY PROTOCOL — v3.1

## Purpose

Knowledge closure alone is not enough.

A documentary script can be understandable yet still fail because:
- the blind auditor missed a concept;
- the script teaches labels the viewer does not need;
- the same reveal is explained twice;
- certainty becomes stronger than the evidence;
- vague time language replaces a better-supported date;
- definitions are technically correct but too broad for context;
- prose is understandable but unnatural when spoken;
- repeated rhetorical patterns make the narration sound formulaic.

v3.1 adds a Final Integrity System around the v3 Audience Knowledge Graph.

The five integrity layers are:

1. DISCOVERY COMPLETENESS
2. TERMINOLOGY NECESSITY
3. NARRATIVE INTEGRITY
4. CLAIM CALIBRATION
5. NATURALNESS + LISTENING INTEGRITY

---

## 1. Discovery Completeness

### Two-pass discovery

Blind knowledge discovery must use two passes.

PASS A — LEXICAL KNOWLEDGE SWEEP

Read every sentence in order.

Create a candidate when a phrase may be:
- a scientific/technical label;
- an acronym;
- an abstract process;
- a classification;
- an evidence method;
- a measurement concept;
- a historical/institutional label;
- a common word used in a specialized role;
- a causal mechanism;
- a relationship the viewer must understand.

Do not skip a phrase because it appears familiar.

PASS B — SEMANTIC KNOWLEDGE AUDIT

For every lexical candidate decide whether it is:
- likely knowledge-bearing;
- likely ordinary vocabulary;
- duplicated by another candidate;
- an alias of another candidate;
- a contextual-role candidate.

The blind stage does NOT decide final closure status.

### No Silent Ignore

Every lexical candidate must receive a final disposition during reconciliation:

- BASELINE_KNOWN
- GROUNDED
- REPLACED
- REMOVED
- UNRESOLVED

No candidate may disappear between discovery and closure.

PASS requires:

silently_ignored_candidates = 0

### Discovery coverage report

Report:
- sentences_scanned
- lexical_candidates
- semantic_candidates
- reconciled_candidates
- silently_ignored_candidates

---

## 2. Strict KNOWN Validation

No inferred known.

A phrase may be BASELINE_KNOWN only when:
1. it exactly matches an audience-baseline entry; or
2. it is explicitly canonicalized/mapped to a declared normal-language primitive.

A model may not mark a scientific, technical, historical or specialized phrase known merely because it feels familiar.

Examples requiring explicit review unless baseline says otherwise:
- di truyền
- genome
- hàm lượng
- phytolith
- hemp
- cannabinoid

---

## 3. Terminology Necessity Gate

Being explainable does not justify keeping a label.

For every non-baseline label record:

- needed_for_later_reasoning
- reuse_count
- precision_gain
- story_value
- replacement_available
- context_scope
- action

Allowed actions:
- KEEP
- KEEP_ONCE
- REPLACE
- REMOVE

### Hard pruning rule

If:

needed_for_later_reasoning = false
AND replacement_available = true

prefer REPLACE or REMOVE.

Do not make the audience memorize labels that add no later reasoning value.

### Alias Budget

For each core entity define:

- primary_spoken_label
- scientific_alias_policy
- allowed_reuse_aliases
- discouraged_reuse_aliases
- removed_aliases

Prefer:
- one primary spoken label;
- at most one scientific label when useful;
- functional subtype labels only when essential.

Repeatedly alternating aliases increases cognitive load even when every alias is explained.

---

## 4. Context-scoped Definitions

A label can be valid in one research context but not as a universal definition.

Knowledge nodes that need scoped wording should include:

- definition_scope.type
- definition_scope.context
- safe_definition
- unsafe_definition

Example:

hemp

Safer:
"Trong các nghiên cứu về lịch sử thuần hóa này, những dòng thiên về thân, sợi hoặc hạt thường được xếp vào nhóm hemp."

Riskier:
"hemp nghĩa là..."

Do not universalize a study category into a global legal/botanical definition.

---

## 5. Knowledge–Story Duplication Gate

Grounding must not destroy narrative progression.

Track each important claim/reveal occurrence with a story function:

- TEASE
- EXPLAIN
- EVIDENCE
- COMPLICATE
- PAYOFF
- CALLBACK

If the same claim + same evidence + same meaning appears multiple times, each occurrence must have a distinct story function.

Otherwise flag:

REDUNDANT_REVEAL

PASS requires:

redundant_reveals = 0

A teaser may hint at a later reveal, but should not fully explain the same evidence twice.

---

## 6. Claim Strength Contract

Each material claim should define:

- allowed_certainty
- forbidden_strengthening
- time_scope
- geographic_scope
- population_scope
- preferred_temporal_wording
- forbidden_temporal_shortcuts

Fact checking must scan certainty language such as:

- chắc chắn
- rõ ràng
- đầu tiên
- sớm nhất
- duy nhất
- luôn
- tất cả
- chưa từng
- từ rất lâu
- từ xa xưa

A phrase is not automatically wrong, but it must be supported at that strength.

### Temporal Precision Gate

When the source supports a useful concrete date/range, prefer it over vague stronger language.

Example:

Prefer:
"Ít nhất khoảng 2.500 năm trước..."

over:
"Từ rất lâu..."

when the specific evidence is approximately 2,500 years old.

PASS requires:

certainty_overstatements = 0
unsupported_temporal_generalizations = 0
scope_overstatements = 0

---

## 7. Plain-language Naturalness Gate

UNDERSTANDABLE does not automatically mean NATURAL.

Audit for:
- translationese;
- noun stacking;
- academic compression;
- abstract nominalization;
- unnecessarily formal labels;
- phrases unlikely in natural spoken target-language narration.

Possible repairs:
- replace abstract nouns with actions;
- shorten noun chains;
- use a familiar spoken phrase;
- split dense clauses;
- remove labels already unnecessary under the terminology gate.

PASS requires:

translationese_flags = 0

---

## 8. Rhythm Pattern Audit

Detect patterns such as:
- repeated sentence openings;
- repeated fragments;
- parallelism overload;
- repeated "không phải X, mà Y";
- rhetorical-question overload;
- repeated contrast templates;
- generic documentary crescendo.

Record:
- pattern_type
- phrase/pattern
- occurrences_in_block
- action

Meaningful intentional repetition may remain only when it serves a clear rhetorical function.

PASS requires:

repeated_rhetorical_patterns = 0

---

## 9. Narration Listening Pass

Assume the viewer hears the script once without reading text.

Flag a listening block when it contains:
- too many unfamiliar labels;
- multiple abstract nouns in one sentence;
- nested definitions;
- long entity chains;
- ambiguous pronouns;
- dense causal clauses;
- several dates/numbers without a concrete anchor.

Repair using:
- shorter sentences;
- concrete action;
- plain language;
- removing unnecessary labels;
- moving knowledge earlier;
- splitting one mechanism across beats.

PASS requires:

unresolved_audio_density_flags = 0
high_load_listening_blocks = 0

---

## 10. Independent Final Auditors

Final integrity requires three blind auditors.

### 10B1 — Blind Knowledge Auditor

May read only:
- project brief/audience profile;
- final candidate;
- shared protocols.

Must not read:
- Knowledge Graph;
- closure reports;
- earlier inventories.

Extract knowledge sentence by sentence.

### 10B2 — Blind Claim/Certainty Auditor

May read only:
- project brief;
- final candidate;
- Final Integrity Protocol.

Must not read Claim Map before extraction.

Extract:
- factual claims;
- dates;
- quantities;
- causal statements;
- certainty markers;
- superlatives;
- vague temporal claims;
- geographic/population scope.

Only later does 10C reconcile this inventory with Claim Map/sources.

### 10B3 — Blind Naturalness/Redundancy Auditor

May read only:
- project brief;
- final candidate;
- Final Integrity Protocol.

Must not read:
- Anti-AI report;
- Retention report;
- prior naturalness audits.

Find:
- translationese;
- unnecessary aliases;
- duplicate reveals;
- repeated rhetorical patterns;
- audio-density problems;
- awkward terminology.

---

## 11. Final Integrity Gate

The final artifact is 10_final_integrity.json.

PASS requires every relevant count below to equal zero.

knowledge:
- core_entities_ungrounded
- unmapped_aliases
- missing_discovered_nodes
- unresolved_concepts
- unresolved_dependencies
- unresolved_relations
- temporal_first_use_failures
- confusable_pairs_unresolved
- silently_ignored_candidates

terminology:
- unnecessary_labels
- alias_overload

narrative:
- redundant_reveals
- high_load_listening_blocks

factual:
- unsupported_claims
- certainty_overstatements
- unsupported_temporal_generalizations
- scope_overstatements

naturalness:
- translationese_flags
- repeated_rhetorical_patterns
- unresolved_audio_density_flags

Also require:
- stage 09 factual PASS;
- Visual Storytelling Score >= 8.0;
- reasonable duration alignment;
- no production directions unless requested.

If a repair changes final text:
- rerun all affected audits;
- if factual substance changes, rerun stage 09;
- rerun 10B1, 10B2 and 10B3 before final PASS.
