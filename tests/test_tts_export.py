#!/usr/bin/env python3
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from tools.export_tts_text import export_project, transform_for_tts  # noqa: E402

try:
    import jsonschema
except ImportError:
    jsonschema = None


EXPECTED = {
    "vi": ("25 phần trăm", "20 độ C", "70 độ Fahrenheit"),
    "en": ("25 percent", "20 degrees Celsius", "70 degrees Fahrenheit"),
    "de": ("25 Prozent", "20 Grad Celsius", "70 Grad Fahrenheit"),
    "fr": ("25 pour cent", "20 degrés Celsius", "70 degrés Fahrenheit"),
    "es": ("25 por ciento", "20 grados Celsius", "70 grados Fahrenheit"),
    "ko": ("25 퍼센트", "섭씨 20도", "화씨 70도"),
    "ja": ("25パーセント", "摂氏20度", "華氏70度"),
}


class TTSExportTests(unittest.TestCase):
    def test_profiles_preserve_unicode_and_expand_safe_units(self):
        for locale, expected in EXPECTED.items():
            with self.subTest(locale=locale):
                source = (
                    "# Title\n\n"
                    "## Section\n"
                    "**Narration** is 25% ready at 20 °C and 70 °F.\n"
                    "[Source label](https://example.com) should stay as words.\n"
                )
                out, stats, warnings = transform_for_tts(source, locale)
                self.assertNotIn("#", out)
                self.assertNotIn("https://", out)
                self.assertNotIn("**", out)
                self.assertIn("Narration", out)
                self.assertIn("Source label", out)
                self.assertIn(expected[0], out)
                self.assertIn(expected[1], out)
                self.assertIn(expected[2], out)
                self.assertEqual([], warnings)
                self.assertGreaterEqual(stats["headings_removed"], 2)

    def test_japanese_fullwidth_punctuation_is_preserved(self):
        out, _, _ = transform_for_tts("# 題\n最初です。次です！本当ですか？\n", "ja-JP")
        self.assertEqual("最初です。次です！本当ですか？\n", out)

    def test_vietnamese_diacritics_are_preserved(self):
        out, _, _ = transform_for_tts("# Tiêu đề\nĐây là tiếng Việt tự nhiên, rõ ràng.\n", "vi-VN")
        self.assertIn("Đây là tiếng Việt tự nhiên, rõ ràng.", out)

    def test_code_fence_fails_closed(self):
        with self.assertRaises(ValueError):
            transform_for_tts("# Title\n```python\nprint('x')\n```\n", "en")

    def test_export_requires_passing_10d_and_writes_content_addressed_report(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            script = "# Title\nHello world. 10% at 20 °C.\n"
            (root / "10_final_script.md").write_text(script, encoding="utf-8")
            digest = hashlib.sha256(script.encode("utf-8")).hexdigest()
            (root / "00_project_brief.yaml").write_text(
                "project:\n  locale: en\npipeline:\n  version: '3.3'\n",
                encoding="utf-8",
            )
            proof = {
                "proof_verifier_status": "PASS",
                "project_status": "CONTENT_PASS_ISOLATION_NOT_VERIFIED",
                "isolation_verified": False,
                "released_script_sha256": digest,
            }
            (root / "10d_proof_verification.json").write_text(
                json.dumps(proof, indent=2) + "\n", encoding="utf-8"
            )

            report = export_project(root)
            self.assertEqual("PASS", report["status"])
            self.assertTrue((root / "final.txt").exists())
            self.assertTrue((root / "11_tts_export.json").exists())
            final_text = (root / "final.txt").read_text(encoding="utf-8")
            self.assertEqual("Hello world. 10 percent at 20 degrees Celsius.\n", final_text)

            if jsonschema is not None:
                schema = json.loads(
                    (REPO_ROOT / "schemas" / "v3.3" / "tts-export.schema.json").read_text(encoding="utf-8")
                )
                base = (REPO_ROOT / "schemas" / "v3.3").resolve().as_uri() + "/"
                resolver = jsonschema.RefResolver(base_uri=base, referrer=schema)
                jsonschema.Draft202012Validator(schema, resolver=resolver).validate(report)

    def test_export_rejects_failed_proof(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            script = "# Title\nHello.\n"
            (root / "10_final_script.md").write_text(script, encoding="utf-8")
            (root / "00_project_brief.yaml").write_text("project:\n  locale: en\n", encoding="utf-8")
            (root / "10d_proof_verification.json").write_text(
                json.dumps({"proof_verifier_status": "FAIL", "project_status": "FAIL"}) + "\n",
                encoding="utf-8",
            )
            with self.assertRaises(ValueError):
                export_project(root)


if __name__ == "__main__":
    unittest.main()
