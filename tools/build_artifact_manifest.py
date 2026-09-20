#!/usr/bin/env python3
"""Build artifact_manifest.json for a stable v3.3 project."""

import argparse
import hashlib
import json
from pathlib import Path


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project")
    ap.add_argument("--output", default="artifact_manifest.json")
    args = ap.parse_args()

    root = Path(args.project).resolve()
    if not root.is_dir():
        raise SystemExit(f"not a project directory: {root}")

    excluded = {args.output, "10d_proof_verification.json", "final.txt", "11_tts_export.json"}
    files = sorted(
        p for p in root.iterdir()
        if p.is_file() and p.name not in excluded
    )

    hashes = {p.name: sha256(p) for p in files}
    manifest = {
        "pipeline_version": "3.3",
        "artifact_schema_version": "3.3.0",
        "segmenter_version": "3.3.0",
        "inputs": {
            "project_root": ".",
            "hash_algorithm": "sha256"
        },
        "outputs": {
            "final_script": "10_final_script.md",
            "final_index": "10_final_sentence_index.json",
            "final_integrity": "10_final_integrity.json",
            "artifact_count": len(files)
        },
        "hashes": hashes
    }

    out = root / args.output
    out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(out), "artifact_count": len(files)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
