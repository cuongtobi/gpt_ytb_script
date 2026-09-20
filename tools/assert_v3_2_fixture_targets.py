#!/usr/bin/env python3
import json
from pathlib import Path
import sys

CASES = {
    "projects/2026-09-20_test_v3_2_birds_power_lines_10min": {
        "draft_must_detect": ["điện áp", "đường dây truyền tải", "đường phân phối"],
        "final_must_not_contain": ["điện áp", "đường dây truyền tải", "đường phân phối"],
    },
    "projects/2026-09-20_test_v3_2_maize_domestication_10min": {
        "draft_must_detect": ["dữ liệu di truyền", "quần thể", "phát tán", "khảo cổ"],
        "final_must_not_contain": ["dữ liệu di truyền", "quần thể", "phát tán", "khảo cổ"],
    },
    "projects/2026-09-20_test_v3_2_seawater_rain_10min": {
        "draft_must_detect": ["phong hóa", "khí quyển"],
        "final_must_not_contain": ["phong hóa", "khí quyển"],
    },
}

def main(project):
    cfg=CASES[project]
    sweep=json.loads(Path(project,"05_lexical_knowledge_sweep.json").read_text(encoding="utf-8"))
    detected={x["exact_phrase"].casefold() for x in sweep.get("candidates",[])}
    final=Path(project,"10_final_script.md").read_text(encoding="utf-8").casefold()
    errors=[]
    for term in cfg["draft_must_detect"]:
        if term.casefold() not in detected:
            errors.append(f"draft lexical sweep missed regression target: {term}")
    for term in cfg["final_must_not_contain"]:
        if term.casefold() in final:
            errors.append(f"regression target still remains in final script: {term}")
    result={"project":project,"targeted_regression_status":"PASS" if not errors else "FAIL","errors":errors}
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 0 if not errors else 1

if __name__=="__main__":
    if len(sys.argv)!=2 or sys.argv[1] not in CASES:
        raise SystemExit("usage: assert_v3_2_fixture_targets.py <fixture-project-path>")
    raise SystemExit(main(sys.argv[1]))
