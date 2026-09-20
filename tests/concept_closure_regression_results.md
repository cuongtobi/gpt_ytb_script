# Concept Closure Regression — Manual Acceptance Run

Date: 2026-09-20
Pipeline: v2.0
Protocol: prompts/CONCEPT_CLOSURE_PROTOCOL.md

This is a prompt-native repository, so these are manual acceptance runs against the protocol rather than executable unit tests.

## Case 1 — lactase definition creates lactose dependency

### Input

Một em bé gần như được sinh ra để tiêu hóa sữa. Ruột non tạo lactase, một enzyme cắt đường lactose trong sữa để cơ thể hấp thu.

### v2 discovery

Detected:
- lactase
- enzyme
- lactose

Problems:
- lactose is required to understand the lactase explanation but is not explained before use
- enzyme is an extra technical label that is not required for this short story
- lactase / lactose are confusable

Pre-repair:
- lactose: UNRESOLVED
- lactase: UNRESOLVED
- enzyme: REPLACE candidate
- confusable pair lactase/lactose: unresolved

### v2 repair

Lactose là loại đường tự nhiên có trong sữa. Ruột non tạo lactase, một chất giúp cơ thể xử lý loại đường này.

Post-repair:
- lactose: EXPLAINED
- lactase: EXPLAINED
- enzyme: REMOVED / not introduced
- confusable pair: resolved
- unresolved: 0

Result: PASS

## Case 2 — Writer introduces calcium after initial graph

### Input

Vôi sống gặp nước sẽ tỏa nhiệt. Sau khi hỗn hợp đông lại, một số cục giàu calcium có thể vẫn nằm trong vật liệu.

### v2 discovery

Initial graph does not contain calcium.

05 Concept Delta must detect:
- calcium: NEW_CONCEPT
- contextual role: specialized materials chemistry

Necessity test:
- label is not needed for the short explanation

### v2 repair

Vôi sống gặp nước sẽ tỏa nhiệt. Sau khi hỗn hợp đông lại, một số cục vôi còn phản ứng vẫn có thể nằm bên trong vật liệu.

Later mechanism:

Khi nước lọt vào một vết nứt, một phần vật chất trong cục vôi có thể hòa vào nước rồi đóng lại trong khe, giúp lấp một phần vết nứt.

Post-repair:
- calcium: REMOVED
- no replacement concept left unresolved
- unresolved: 0

Result: PASS

## Case 3 — Anti-AI editor introduces new jargon

### Before style edit

Khi nước lọt vào khe, vật chất trong cục vôi có thể hòa vào nước rồi đóng lại trong khe.

### Invalid style rewrite

Khi nước lọt vào khe, calcium carbonate có thể tái kết tinh.

### v2 behavior

08 Concept Delta detects:
- calcium carbonate: NEW_CONCEPT
- recrystallization role: specialized

Because neither label is required for the narration, stage 08 must replace with plain language or route back to stage 06.

Stage 08 cannot PASS while this concept remains unresolved.

Result: PASS

## Acceptance summary

- full-script discovery: PASS
- new concept after stage 03 detected: PASS
- recursive definition dependency: PASS
- contextual-role familiarity: PASS
- confusable-pair obligation: PASS
- replace/remove before glossary expansion: PASS
- UNRESOLVED = 0 final gate: PASS
