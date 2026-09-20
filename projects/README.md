# projects/

Các thư mục project dưới đây là artifact do pipeline tạo.

## Pipeline v2.0

Project mới phải dùng các artifact concept sau:

- 03_concept_graph.json
- 05_concept_delta.json
- 06_concept_closure.json
- 07_concept_delta.json
- 08_concept_delta.json
- 09_concept_delta.json
- 10_concept_closure.json

Final project chỉ được PASS khi final concept closure có:

- unresolved = 0
- unresolved_dependencies = 0
- confusable_pairs_unresolved = 0

## Legacy test fixtures

Ba project sau được tạo trước khi Dynamic Concept Graph / Recursive Concept Closure được triển khai:

- 2026-09-20_test_onion_tears
- 2026-09-20_test_milk_adults
- 2026-09-20_test_roman_concrete

Chúng được giữ lại như regression/failure fixtures của pipeline v1.

Đặc biệt:
- milk_adults chứa ví dụ lactase → lactose, nơi definition sinh dependency chưa được xử lý đúng.
- roman_concrete chứa ví dụ calcium, một concept được Writer sinh ra sau Concept Map và bị audit cũ bỏ sót.

Không dùng cấu trúc artifact của các project legacy này làm mẫu cho project mới.

Acceptance tests cho lỗi này nằm tại:
- tests/concept_closure_regression.md
