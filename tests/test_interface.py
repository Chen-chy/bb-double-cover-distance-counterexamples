"""Regression tests for the standalone repository interface, not new distance proofs."""
from __future__ import annotations
import contextlib
import io
import json
from pathlib import Path
import unittest
from bbcover import __version__
from bbcover.__main__ import main, compare_cover, inspect_example
from bbcover.catalog import catalog, find_results

ROOT = Path(__file__).resolve().parents[1]


class InterfaceTests(unittest.TestCase):
    def call(self, *args):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            main(list(args))
        return json.loads(out.getvalue())

    def test_version(self):
        self.assertEqual(__version__, "0.2.1")

    def test_complete_register(self):
        data = catalog()
        self.assertEqual(data["counts"], {"main": 16, "homology": 10, "amplification": 38, "degradation": 40, "total": 104})
        self.assertEqual(len(data["results"]), 104)
        self.assertEqual(len({r["id"] for r in data["results"]}), 104)

    def test_register_matches_repository(self):
        self.assertEqual(catalog(), json.loads((ROOT / "results/catalog.json").read_text()))

    def test_unknown_result(self):
        with self.assertRaises(ValueError):
            find_results("not-a-result")

    def test_branch_filter(self):
        self.assertEqual(find_results(branch="amplification")["count"], 38)
        self.assertEqual(find_results(branch="degradation")["count"], 40)
        self.assertEqual(find_results(branch="main")["count"], 16)
        self.assertEqual(find_results(branch="homology")["count"], 10)

    def test_status_filter(self):
        row = find_results("CEX-UP")["results"][0]
        self.assertTrue(find_results(status=row["status"])["count"] >= 2)
        self.assertEqual(find_results(status="nonexistent")["count"], 0)

    def test_returns_fresh_data(self):
        first = catalog()
        first["results"].clear()
        self.assertEqual(len(catalog()["results"]), 104)

    def test_upper_comparison(self):
        data = compare_cover("upper")
        self.assertEqual(data["ratio_d2_over_d"], "7/3")
        self.assertEqual(data["base"]["k_recomputed"], 4)
        self.assertTrue(data["violation_verified_using_certified_distances"])
        self.assertFalse(data["distance_recomputed_by_this_command"])
        self.assertTrue(data["cover_validation"]["neighborhood_bijections"])

    def test_lower_comparison(self):
        data = compare_cover("lower")
        self.assertEqual(data["ratio_d2_over_d"], "6/7")
        self.assertEqual(data["cover"]["k_recomputed"], 8)
        self.assertTrue(data["violation_verified_using_certified_distances"])
        self.assertEqual(data["cover"]["witness_weight"], 12)

    def test_comparison_rejects_unknown(self):
        with self.assertRaises(ValueError):
            compare_cover("either")

    def test_inspection_scope(self):
        data = inspect_example("q78")
        self.assertEqual(data["distance_from_independent_certificate"], 14)
        self.assertFalse(data["distance_recomputed_by_this_command"])
        self.assertTrue(data["witness_is_nonboundary_cycle"])

    def test_results_cli(self):
        data = self.call("results", "DIST-UPPER")
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], "DIST-UPPER")

    def test_bounds_cli(self):
        data = self.call("bounds", "14", "--n", "156", "--k", "4", "--k2", "8")
        self.assertEqual((data["lower"], data["upper"]), (2, 28))

    def test_invalid_cli_argument(self):
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as ctx:
                main(["results", "not-a-result"])
        self.assertEqual(ctx.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
