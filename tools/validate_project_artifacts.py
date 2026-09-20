#!/usr/bin/env python3
"""Validate v3.3 machine-readable artifacts against schemas/v3.3."""

import argparse
import json
from pathlib import Path

import jsonschema
import yaml


def load_data(path):
    if path.suffix.lower() in {".yaml", ".yml"}:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project")
    args = ap.parse_args()

    root = Path(args.project).resolve()
    repo_root = Path(__file__).resolve().parents[1]
    schema_dir = repo_root / "schemas" / "v3.3"
    mapping = json.loads((schema_dir / "schema_manifest.json").read_text(encoding="utf-8"))["artifacts"]
    errors = []

    for rel, schema_name in mapping.items():
        if rel == "10d_proof_verification.json" and not (root / rel).exists():
            continue
        path = root / rel
        if not path.exists():
            errors.append(f"missing required artifact: {rel}")
            continue
        try:
            data = load_data(path)
            schema_path = schema_dir / schema_name
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
            resolver = jsonschema.RefResolver(
                base_uri=schema_dir.resolve().as_uri() + "/",
                referrer=schema
            )
            validator = jsonschema.Draft202012Validator(schema, resolver=resolver)
            for issue in validator.iter_errors(data):
                loc = ".".join(str(x) for x in issue.path)
                errors.append(f"{rel}:{loc or '<root>'}: {issue.message}")
        except Exception as exc:
            errors.append(f"{rel}: {exc}")

    result = {"schema_status": "PASS" if not errors else "FAIL", "errors": errors}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
