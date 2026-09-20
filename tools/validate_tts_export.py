#!/usr/bin/env python3
"""Validate Stage 11 TTS export schema, hashes, and final plain-text output."""

import argparse
import hashlib
import json
import sys
from pathlib import Path

import jsonschema


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("project", help="Project directory containing final.txt and 11_tts_export.json")
    args = ap.parse_args()

    root = Path(args.project).resolve()
    report_path = root / "11_tts_export.json"
    final_path = root / "final.txt"
    repo_root = Path(__file__).resolve().parents[1]
    schema_dir = repo_root / "schemas" / "v3.3"
    schema_path = schema_dir / "tts-export.schema.json"
    errors = []

    if not report_path.exists():
        errors.append("11_tts_export.json missing")
    if not final_path.exists():
        errors.append("final.txt missing")
    if errors:
        print(json.dumps({"tts_export_validation": "FAIL", "errors": errors}, ensure_ascii=False, indent=2))
        return 1

    try:
        report = json.loads(report_path.read_text(encoding="utf-8"))
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        resolver = jsonschema.RefResolver(base_uri=schema_dir.resolve().as_uri() + "/", referrer=schema)
        validator = jsonschema.Draft202012Validator(schema, resolver=resolver)
        for issue in validator.iter_errors(report):
            loc = ".".join(str(x) for x in issue.path)
            errors.append(f"schema:{loc or '<root>'}: {issue.message}")
    except Exception as exc:
        errors.append(f"schema validation error: {exc}")
        report = {}

    output = report.get("output", {})
    if output.get("sha256") != sha256(final_path):
        errors.append("final.txt hash does not match 11_tts_export.json")

    ca = report.get("content_address", {})
    for rec in ca.get("inputs", []) if isinstance(ca, dict) else []:
        rel = rec.get("path")
        digest = rec.get("sha256")
        if not isinstance(rel, str):
            errors.append("invalid content-address path")
            continue
        p = root / rel
        if not p.exists():
            errors.append(f"content-address input missing: {rel}")
        elif sha256(p) != digest:
            errors.append(f"content-address hash mismatch: {rel}")

    raw = final_path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        errors.append("final.txt must be UTF-8 without BOM")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        errors.append("final.txt is not valid UTF-8")
        text = ""

    if not text.strip():
        errors.append("final.txt is empty")
    if any(token in text for token in ("```", "~~~", "")):
        errors.append("final.txt contains residual non-TTS markup")

    result = {
        "tts_export_validation": "PASS" if not errors else "FAIL",
        "locale": report.get("locale"),
        "output_sha256": sha256(final_path),
        "errors": errors,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
