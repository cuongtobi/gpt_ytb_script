# Pipeline v2 — Three-example rerun

Date: 2026-09-20

## Projects

1. projects/2026-09-20_test_onion_tears_v2
2. projects/2026-09-20_test_milk_adults_v2
3. projects/2026-09-20_test_roman_concrete_v2

Each project contains 24 v2 artifacts, including:
- 03_concept_graph.json
- 05_concept_delta.json
- 06_concept_closure.json
- 07_concept_delta.json
- 08_concept_delta.json
- 09_concept_delta.json
- 10_concept_closure.json

## Results

### Onion tears
- Final words: 512
- Concept closure: PASS
- Fact check: PASS
- Visual Storytelling Score: 9.1/10
- Key behavior: unnecessary biochemical labels are removed; no explanation chain is left open.

### Adult milk digestion
- Final words: 560
- Concept closure: PASS
- Fact check: PASS
- Visual Storytelling Score: 9.2/10
- Regression fixed:
  - lactose is introduced first as the natural sugar in milk
  - lactase is introduced only after lactose is EXPLAINED
  - enzyme, lactase-persistence and selection-pressure labels are removed because the short script does not need them
  - confusable pair lactose/lactase is resolved

### Roman concrete
- Final words: 605
- Concept closure: PASS
- Fact check: PASS
- Visual Storytelling Score: 9.4/10
- Regression fixed:
  - calcium is treated as an unnecessary specialized concept
  - calcium, calcium carbonate, recrystallization and lime-clast labels are REMOVED
  - the mechanism is explained with plain physical actions
  - later editors introduce no unresolved jargon

## Closure summary

All three final closure artifacts report:
- unresolved = 0
- unresolved_dependencies = 0
- confusable_pairs_unresolved = 0
- status = PASS

## v1 → v2 conclusion

The old failure mode was:
static concept list → writer creates new dependency/jargon → concept is invisible → false PASS.

The v2 behavior is:
initial graph → actual-script discovery → concept delta → recursive dependency closure → downstream delta scans → final rescan from scratch → PASS only at closure.
