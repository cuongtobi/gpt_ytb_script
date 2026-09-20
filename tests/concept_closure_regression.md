# Concept Closure Regression Tests

These are acceptance tests for pipeline v2.0.

The tests target the root failure that a definition can introduce a new concept, or a rewrite can introduce a concept absent from the initial graph.

## Test 1 — Definition dependency: lactase → lactose

### Failing input

Một em bé gần như được sinh ra để tiêu hóa sữa. Ruột non tạo lactase, một enzyme cắt đường lactose trong sữa để cơ thể hấp thu.

### Expected discovery

The closure scan must identify:
- lactase
- enzyme
- lactose

If lactose has not been explained or marked KNOWN in its contextual role, lactase cannot be marked EXPLAINED.

Expected state before repair:
- lactose: UNRESOLVED
- lactase: UNRESOLVED because a required dependency is unresolved

### Expected repair

Prefer dependency-first sequencing and remove unnecessary labels:

Lactose là loại đường tự nhiên có trong sữa. Ruột non tạo lactase, một chất giúp cơ thể xử lý loại đường này.

The label “enzyme” is not required for this short explanation, so the preferred action is REPLACE rather than creating another dependency.

### Pass condition

- lactose: EXPLAINED
- lactase: EXPLAINED
- enzyme: REMOVED or not introduced
- unresolved: 0
- unresolved_dependencies: 0

## Test 2 — New concept introduced after initial graph: calcium

### Initial graph

Contains:
- vôi sống
- trộn nóng
- cục giàu vôi
- vật liệu núi lửa

Does NOT contain:
- calcium

### Failing rewrite

Vôi sống gặp nước sẽ tỏa nhiệt. Sau khi hỗn hợp đông lại, một số cục giàu calcium có thể vẫn nằm trong vật liệu.

### Expected discovery

Post-write delta scan must detect:
- calcium = NEW_CONCEPT

The pipeline must not ignore it because it was absent from stage 03.

### Necessity test

For a short general-audience script, the technical label calcium is not required to understand the later mechanism.

Expected action:
- REPLACE

### Expected repair

Vôi sống gặp nước sẽ tỏa nhiệt. Sau khi hỗn hợp đông lại, một số cục vôi còn phản ứng vẫn có thể nằm bên trong vật liệu.

Later mechanism can remain plain:

Khi nước lọt vào một vết nứt, một phần vật chất trong cục vôi có thể hòa vào nước rồi đóng lại trong khe, giúp lấp một phần vết nứt.

### Pass condition

- calcium: REMOVED
- no new unresolved replacement concept
- unresolved: 0

## Test 3 — Confusable concepts

### Failing input

Lactase giúp xử lý lactose.

### Expected behavior

Because lactase and lactose are confusable and both are non-obvious to a general audience, spelling difference is not enough.

Expected repair:

Lactose là loại đường tự nhiên có trong sữa. Lactase thì khác: đó là enzyme giúp cơ thể phân giải lactose.

### Pass condition

- confusable_pairs_unresolved: 0

## Test 4 — Editor-introduced jargon

### Input to Anti-AI Editor

Khi nước lọt vào khe, vật chất trong cục vôi có thể hòa vào nước rồi tạo khoáng mới.

### Invalid Anti-AI rewrite

Khi nước lọt vào khe, calcium carbonate có thể tái kết tinh.

### Expected behavior

08_concept_delta.json must detect:
- calcium carbonate = NEW_CONCEPT
- specialized role = NEW

Unless this label is necessary and recursively explained, stage 08 must:
- REPLACE it with the original plain-language mechanism
- or route back to stage 06

Stage 08 cannot PASS with an unresolved new concept.

## Global acceptance criteria

For every test:
- actual current script is scanned from scratch
- discovery is not limited to stage-03 concepts
- definitions are recursively dependency-checked
- contextual role familiarity is evaluated
- unnecessary labels are replaced or removed
- final closure reaches a stable fixed point
- unresolved = 0
- unresolved_dependencies = 0
- confusable_pairs_unresolved = 0
