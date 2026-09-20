# Final Stress-Test Report — FAIL

The script is broadly correct and understandable, but v3.1 falsely reported PASS.

Independent post-run audit found:
- "điện áp" remains in final text without first-use grounding;
- "đường dây truyền tải" and "đường phân phối" were absent from 10B1 lexical inventory;
- therefore silently_ignored_candidates cannot be zero.

This project is a regression fixture for lexical discovery completeness.
