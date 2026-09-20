#!/usr/bin/env python3
"""Create a plain-text, TTS-ready narration export from a verified final script.

Stage 11 is deliberately post-10D. It never rewrites factual wording with an
LLM. It applies deterministic presentation-only cleanup plus a very small set
of locale-safe spoken-unit expansions.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path

SUPPORTED_LANGS = {"vi", "en", "de", "fr", "es", "ko", "ja"}

UNIT_WORDS = {
    "vi": {"percent": "phần trăm", "celsius_after": "độ C", "fahrenheit_after": "độ Fahrenheit"},
    "en": {"percent": "percent", "celsius_after": "degrees Celsius", "fahrenheit_after": "degrees Fahrenheit"},
    "de": {"percent": "Prozent", "celsius_after": "Grad Celsius", "fahrenheit_after": "Grad Fahrenheit"},
    "fr": {"percent": "pour cent", "celsius_after": "degrés Celsius", "fahrenheit_after": "degrés Fahrenheit"},
    "es": {"percent": "por ciento", "celsius_after": "grados Celsius", "fahrenheit_after": "grados Fahrenheit"},
    "ko": {"percent": "퍼센트", "celsius_before": "섭씨", "celsius_after": "도", "fahrenheit_before": "화씨", "fahrenheit_after": "도"},
    "ja": {"percent": "パーセント", "celsius_before": "摂氏", "celsius_after": "度", "fahrenheit_before": "華氏", "fahrenheit_after": "度"},
}

RICH_TOKEN_RE = re.compile(r"[^]*")
MD_LINK_RE = re.compile(r"!\[([^\]]*)\]\([^)]+\)|\[([^\]]+)\]\([^)]+\)")
RAW_URL_RE = re.compile(r"https?://\S+|www\.\S+", re.IGNORECASE)
HTML_TAG_RE = re.compile(r"<[^>]+>")
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+")
HR_RE = re.compile(r"^\s{0,3}(?:[-*_]\s*){3,}$")
LIST_RE = re.compile(r"^\s*(?:[-+*]|\d+[.)])\s+")
BLOCKQUOTE_RE = re.compile(r"^\s*>\s?")
FENCE_RE = re.compile(r"^\s*(?:```|~~~)")
INLINE_CODE_RE = re.compile(r"`([^`]+)`")
EMPHASIS_RE = re.compile(r"(?<!\w)(?:\*\*|__)(.+?)(?:\*\*|__)|(?<!\w)(?:\*|_)(.+?)(?:\*|_)")
CONTROL_RE = re.compile(r"[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]")
PERCENT_RE = re.compile(r"(?P<num>\d+(?:[.,]\d+)?)\s*%")
CELSIUS_RE = re.compile(r"(?P<num>[+-]?\d+(?:[.,]\d+)?)\s*°\s*C\b", re.IGNORECASE)
FAHRENHEIT_RE = re.compile(r"(?P<num>[+-]?\d+(?:[.,]\d+)?)\s*°\s*F\b", re.IGNORECASE)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def detect_locale(brief_text: str) -> str | None:
    match = re.search(r"(?m)^\s*locale\s*:\s*['\"]?([A-Za-z]{2,3}(?:-[A-Za-z0-9]+)?)['\"]?\s*$", brief_text)
    return match.group(1) if match else None


def base_language(locale: str) -> str:
    return locale.strip().lower().replace("_", "-").split("-")[0]


def _replace_markdown_link(match: re.Match[str]) -> str:
    return (match.group(1) or match.group(2) or "").strip()


def _replace_emphasis(text: str) -> str:
    previous = None
    while previous != text:
        previous = text
        text = EMPHASIS_RE.sub(lambda m: (m.group(1) or m.group(2) or ""), text)
    return text


def _expand_units(text: str, lang: str, stats: dict) -> str:
    words = UNIT_WORDS[lang]

    def pct(m):
        stats["percent_expansions"] += 1
        num = m.group("num")
        if lang == "ja":
            return f"{num}{words['percent']}"
        return f"{num} {words['percent']}"

    def temp(m, scale):
        num = m.group("num")
        stats[f"{scale}_expansions"] += 1
        before = words.get(f"{scale}_before", "")
        after = words[f"{scale}_after"]
        if lang == "ko":
            return f"{before} {num}{after}"
        if lang == "ja":
            return f"{before}{num}{after}"
        return f"{num} {after}"

    text = CELSIUS_RE.sub(lambda m: temp(m, "celsius"), text)
    text = FAHRENHEIT_RE.sub(lambda m: temp(m, "fahrenheit"), text)
    text = PERCENT_RE.sub(pct, text)
    return text


def transform_for_tts(markdown_text: str, locale: str) -> tuple[str, dict, list[str]]:
    lang = base_language(locale)
    if lang not in SUPPORTED_LANGS:
        raise ValueError(f"unsupported locale for TTS export: {locale}")

    stats = {
        "headings_removed": 0,
        "horizontal_rules_removed": 0,
        "list_markers_removed": 0,
        "blockquote_markers_removed": 0,
        "rich_tokens_removed": 0,
        "raw_urls_removed": 0,
        "markdown_links_simplified": 0,
        "inline_code_markers_removed": 0,
        "emphasis_markers_removed": 0,
        "html_tags_removed": 0,
        "control_characters_removed": 0,
        "percent_expansions": 0,
        "celsius_expansions": 0,
        "fahrenheit_expansions": 0,
    }
    warnings: list[str] = []

    text = unicodedata.normalize("NFC", markdown_text).replace("\ufeff", "")
    lines = text.splitlines()
    out_lines: list[str] = []

    for raw in lines:
        if FENCE_RE.match(raw):
            raise ValueError("code fence found in final script; fix 10_final_script.md before TTS export")

        line = raw.strip()
        if not line:
            if out_lines and out_lines[-1] != "":
                out_lines.append("")
            continue

        if HEADING_RE.match(line):
            stats["headings_removed"] += 1
            if out_lines and out_lines[-1] != "":
                out_lines.append("")
            continue

        if HR_RE.match(line):
            stats["horizontal_rules_removed"] += 1
            if out_lines and out_lines[-1] != "":
                out_lines.append("")
            continue

        if BLOCKQUOTE_RE.match(line):
            stats["blockquote_markers_removed"] += 1
            line = BLOCKQUOTE_RE.sub("", line, count=1)

        if LIST_RE.match(line):
            stats["list_markers_removed"] += 1
            line = LIST_RE.sub("", line, count=1)

        rich = len(RICH_TOKEN_RE.findall(line))
        if rich:
            stats["rich_tokens_removed"] += rich
            line = RICH_TOKEN_RE.sub("", line)

        links = len(MD_LINK_RE.findall(line))
        if links:
            stats["markdown_links_simplified"] += links
            line = MD_LINK_RE.sub(_replace_markdown_link, line)

        urls = len(RAW_URL_RE.findall(line))
        if urls:
            stats["raw_urls_removed"] += urls
            line = RAW_URL_RE.sub("", line)

        code_marks = line.count("`") // 2
        if code_marks:
            stats["inline_code_markers_removed"] += code_marks
            line = INLINE_CODE_RE.sub(r"\1", line)

        before = line
        line = _replace_emphasis(line)
        if line != before:
            stats["emphasis_markers_removed"] += 1

        tags = len(HTML_TAG_RE.findall(line))
        if tags:
            stats["html_tags_removed"] += tags
            line = HTML_TAG_RE.sub("", line)

        controls = len(CONTROL_RE.findall(line))
        if controls:
            stats["control_characters_removed"] += controls
            line = CONTROL_RE.sub("", line)

        line = line.replace("\u00a0", " ").replace("\u202f", " ")
        line = re.sub(r"[ \t]+", " ", line).strip()
        line = re.sub(r"\s+([,.;:!?。！？、，；：])", r"\1", line)
        line = _expand_units(line, lang, stats)

        if line:
            out_lines.append(line)

    while out_lines and out_lines[-1] == "":
        out_lines.pop()

    compact: list[str] = []
    for line in out_lines:
        if line == "" and compact and compact[-1] == "":
            continue
        compact.append(line)

    output = "\n".join(compact).strip() + "\n"

    residual = {
        "markdown_heading": bool(re.search(r"(?m)^\s*#{1,6}\s+", output)),
        "code_fence": bool(re.search(r"(?m)^\s*(?:```|~~~)", output)),
        "markdown_link": bool(MD_LINK_RE.search(output)),
        "raw_url": bool(RAW_URL_RE.search(output)),
        "rich_token": bool(RICH_TOKEN_RE.search(output)),
        "control_character": bool(CONTROL_RE.search(output)),
    }
    bad = [name for name, present in residual.items() if present]
    if bad:
        raise ValueError("residual non-TTS markup after export: " + ", ".join(bad))

    stats["paragraph_count"] = len([p for p in output.strip().split("\n\n") if p.strip()])
    stats["line_count"] = len(output.rstrip("\n").splitlines()) if output.strip() else 0
    stats["character_count"] = len(output.rstrip("\n"))
    stats["residual_checks"] = {k: not v for k, v in residual.items()}
    return output, stats, warnings


def export_project(
    project_dir: Path,
    *,
    locale: str | None = None,
    source_name: str = "10_final_script.md",
    proof_name: str = "10d_proof_verification.json",
    output_name: str = "final.txt",
    report_name: str = "11_tts_export.json",
) -> dict:
    root = project_dir.resolve()
    source = root / source_name
    proof = root / proof_name
    brief = root / "00_project_brief.yaml"
    output = root / output_name
    report_path = root / report_name

    for required in (source, proof, brief):
        if not required.exists():
            raise FileNotFoundError(f"required Stage 11 input missing: {required.name}")

    proof_obj = json.loads(proof.read_text(encoding="utf-8"))
    if proof_obj.get("proof_verifier_status") != "PASS":
        raise ValueError("10D proof_verifier_status is not PASS")
    if proof_obj.get("project_status") not in {"PASS_VERIFIED", "CONTENT_PASS_ISOLATION_NOT_VERIFIED"}:
        raise ValueError("10D project_status is not exportable")

    source_hash = sha256_file(source)
    declared_source_hash = proof_obj.get("released_script_sha256")
    if declared_source_hash and declared_source_hash != source_hash:
        raise ValueError("10D released_script_sha256 does not match current 10_final_script.md")

    selected_locale = locale or detect_locale(brief.read_text(encoding="utf-8"))
    if not selected_locale:
        raise ValueError("project locale missing; pass --locale explicitly")

    tts_text, stats, warnings = transform_for_tts(source.read_text(encoding="utf-8"), selected_locale)
    output.write_text(tts_text, encoding="utf-8", newline="\n")
    output_hash = sha256_file(output)

    report = {
        "tts_export_version": "1.0",
        "locale": selected_locale,
        "base_language": base_language(selected_locale),
        "supported_language": base_language(selected_locale) in SUPPORTED_LANGS,
        "content_address": {
            "hash_algorithm": "sha256",
            "inputs": [
                {"path": source_name, "sha256": source_hash},
                {"path": proof_name, "sha256": sha256_file(proof)},
                {"path": "00_project_brief.yaml", "sha256": sha256_file(brief)},
            ],
        },
        "source": {"file": source_name, "sha256": source_hash},
        "integrity_proof": {
            "file": proof_name,
            "sha256": sha256_file(proof),
            "proof_verifier_status": proof_obj.get("proof_verifier_status"),
            "project_status": proof_obj.get("project_status"),
            "isolation_verified": proof_obj.get("isolation_verified"),
        },
        "output": {
            "file": output_name,
            "sha256": output_hash,
            "encoding": "utf-8",
            "bom": False,
            "character_count": stats["character_count"],
            "paragraph_count": stats["paragraph_count"],
            "line_count": stats["line_count"],
        },
        "transformations": {
            k: v for k, v in stats.items()
            if k not in {"character_count", "paragraph_count", "line_count", "residual_checks"}
        },
        "checks": {
            "source_matches_10d": declared_source_hash in {None, source_hash},
            "plain_text_only": all(stats["residual_checks"].values()),
            "no_semantic_rewrite_stage": True,
            "supported_locale": base_language(selected_locale) in SUPPORTED_LANGS,
        },
        "warnings": warnings,
        "status": "PASS",
    }
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    return report


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("project", help="Project directory")
    ap.add_argument("--locale", help="Override locale from 00_project_brief.yaml")
    ap.add_argument("--source", default="10_final_script.md")
    ap.add_argument("--proof", default="10d_proof_verification.json")
    ap.add_argument("--output", default="final.txt")
    ap.add_argument("--report", default="11_tts_export.json")
    args = ap.parse_args()

    try:
        report = export_project(
            Path(args.project),
            locale=args.locale,
            source_name=args.source,
            proof_name=args.proof,
            output_name=args.output,
            report_name=args.report,
        )
    except Exception as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False, indent=2))
        return 1

    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
