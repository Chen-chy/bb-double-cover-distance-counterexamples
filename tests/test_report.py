"""Editorial reporting regression tests, not proofs of mathematical results."""
from __future__ import annotations
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import unittest
from bbcover.catalog import catalog, find_results
from bbcover.__main__ import main

ROOT = Path(__file__).resolve().parents[1]


class ReportTests(unittest.TestCase):
    def cli(self, *args: str) -> dict:
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            main(list(args))
        return json.loads(stream.getvalue())

    def test_default_is_curated(self):
        result = self.cli("results")
        self.assertEqual(result["view"], "main")
        self.assertEqual(result["count"], 12)
        self.assertTrue(all(r["review"]["headline"] for r in result["results"]))

    def test_all_process_is_explicit(self):
        self.assertEqual(self.cli("results", "--view", "all")["count"], 104)
        self.assertEqual(find_results()["count"], 104)  # existing Python API retained

    def test_categories_partition_records(self):
        data = catalog()
        expected = {"main": 12, "scoped": 52, "negative": 15, "historical": 3,
                    "gap": 8, "exploratory": 2, "open": 8, "outside": 4}
        self.assertEqual(data["disposition_counts"], expected)
        collected = [r["id"] for kind in expected for r in find_results(view=kind)["results"]]
        self.assertEqual(len(collected), 104)
        self.assertEqual(len(set(collected)), 104)

    def test_invalid_view_is_rejected(self):
        with self.assertRaises(ValueError):
            find_results(view="all-proven")

    def test_open_questions_are_not_headline(self):
        for r in find_results(view="open")["results"]:
            self.assertFalse(r["review"]["headline"])
            self.assertIn("open", r["status"])

    def test_negative_not_positive(self):
        row = find_results("DEG-P06")["results"][0]
        self.assertEqual(row["review"]["disposition"], "negative")
        self.assertFalse(row["review"]["headline"])

    def test_weight_six_dependency_gate(self):
        row = find_results("DEG-D01")["results"][0]
        self.assertEqual(row["review"]["disposition"], "gap")
        self.assertIn("DEG-I03", row["review"]["known_dependencies"])
        other = find_results("DEG-D04")["results"][0]
        self.assertEqual(other["review"]["disposition"], "scoped")

    def test_finite_certificate_repair_is_not_missing(self):
        row = find_results("DEG-I01")["results"][0]
        self.assertIn("superseded", row["limitations"])
        self.assertIn("not present", row["historical_limitations"])
        self.assertEqual(row["review"]["disposition"], "scoped")

    def test_wrong_scope_stays_out(self):
        row = find_results("DEG-P15")["results"][0]
        self.assertEqual(row["review"]["disposition"], "outside")
        for ident in ("AMP-TREE-04", "AMP-TREE-05"):
            self.assertEqual(find_results(ident)["results"][0]["review"]["disposition"], "negative")

    def test_constant_eight_provenance_flag(self):
        for ident in ("DIST-UPPER", "DIST-INTERVAL", "DIST-TRUNCATED", "LATTICE-TRANSPORT"):
            self.assertTrue(find_results(ident)["results"][0]["review"]["consolidation_review"])

    def test_selectors_keep_explicit_historical_access(self):
        self.assertEqual(self.cli("results", "AMP-OPEN-01")["count"], 1)
        self.assertEqual(self.cli("results", "--branch", "degradation")["count"], 40)
        self.assertEqual(self.cli("results", "AMP-OPEN-01", "--view", "main")["count"], 0)

    def test_full_report_check(self):
        spec = importlib.util.spec_from_file_location("check_report", ROOT / "scripts/check_report.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        result = module.validate(ROOT)
        self.assertEqual(result["errors"], [])


if __name__ == "__main__":
    unittest.main()
