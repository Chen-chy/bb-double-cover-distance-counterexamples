#!/usr/bin/env python3
"""Check editorial selection, evidence gates and prominent report navigation.

This validates reporting consistency only. It is not a formal proof checker,
independent mathematical review, or a substitute for distance certificates.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_FROM_POSITIVE_PROOF = {"negative", "historical", "gap", "exploratory", "open", "outside"}


def validate(root: Path = ROOT) -> dict:
    errors: list[str] = []
    policy = json.loads((root / "results/review_policy.json").read_text(encoding="utf-8"))
    catalog = json.loads((root / "results/catalog.json").read_text(encoding="utf-8"))
    rows = {row["id"]: row for row in catalog["results"]}
    reviews = {row["id"]: row for row in policy["records"]}
    if len(reviews) != 104 or set(reviews) != set(rows):
        errors.append("Every research record must have exactly one current-use classification")
    if len(reviews) != len(policy["records"]):
        errors.append("Duplicate editorial identifiers")
    categories = policy["categories"]
    headlines = policy["headline_ids"]
    if len(headlines) != 12 or len(set(headlines)) != 12:
        errors.append("The current headline report must index 12 distinct selected records")
    for ident, review in reviews.items():
        if review["disposition"] not in categories:
            errors.append("Unknown disposition: " + ident)
        if review["headline"] != (ident in headlines) or review["headline"] != (review["disposition"] == "main"):
            errors.append("Headline/disposition inconsistency: " + ident)
        if not review["reason_zh"].strip():
            errors.append("Missing explicit current-use explanation: " + ident)
        if ident in rows and rows[ident].get("review") != review:
            errors.append("Catalog editorial overlay is stale: " + ident)
        if ident in rows and "open" in rows[ident]["status"] and review["disposition"] != "open":
            errors.append("An open problem was promoted to a result: " + ident)
        for dep in review["known_dependencies"]:
            if dep not in reviews:
                errors.append("Unknown listed dependency: " + ident + " -> " + dep)
    # This guards listed curation dependencies, not an exhaustive proof graph.
    def walk(ident: str, path: tuple[str, ...] = ()) -> None:
        if ident in path:
            errors.append("Cycle in listed report dependencies: " + " -> ".join(path + (ident,)))
            return
        review = reviews.get(ident)
        if review is None:
            return
        if review["disposition"] in EXCLUDED_FROM_POSITIVE_PROOF:
            errors.append("Headline depends on excluded/conditional record: " + " -> ".join(path + (ident,)))
        for dep in review["known_dependencies"]:
            walk(dep, path + (ident,))
    for ident in headlines:
        walk(ident)
    for ident in ("DIST-UPPER", "DIST-INTERVAL", "DIST-TRUNCATED", "LATTICE-TRANSPORT"):
        if not reviews[ident]["consolidation_review"]:
            errors.append("Consolidation review dependency was hidden: " + ident)
    if reviews["DEG-D01"]["disposition"] != "gap" or "DEG-I03" not in reviews["DEG-D01"]["known_dependencies"]:
        errors.append("The weight-six inherited-input gate is missing")
    if reviews["DEG-D04"]["disposition"] != "scoped":
        errors.append("The independent weight-eight theorem must be separated from its combined corollaries")
    for ident in ("AMP-SEARCH-01", "AMP-SEARCH-02"):
        if reviews[ident]["disposition"] != "exploratory":
            errors.append("Search record promoted to a general theorem: " + ident)
    if reviews["DEG-P15"]["disposition"] != "outside":
        errors.append("Five-term lift admitted to the strict-trinomial target")
    counts = dict(Counter(r["disposition"] for r in reviews.values()))
    if counts != catalog["disposition_counts"]:
        errors.append("Status counts are stale")
    if policy["version"] != catalog["version"]:
        errors.append("Review policy and catalog versions disagree")
    for filename, target in (("README.md", "REPORT.md"), ("README.en.md", "REPORT.en.md")):
        text = (root / filename).read_text(encoding="utf-8")
        if f"]({target})" not in "\n".join(text.splitlines()[:16]):
            errors.append("Primary report is not prominent in the first screen: " + filename)
    report = (root / "REPORT.md").read_text(encoding="utf-8")
    for ident in headlines:
        if f"results/CLAIMS.md#{ident}" not in report:
            errors.append("Headline lacks a stable record link in the primary report: " + ident)
    if "104 条研究记录，而不是 104 个已证定理" not in report:
        errors.append("Research-record versus theorem-count warning is missing")
    if "DEG-D01" not in report or "weight-four" not in report:
        errors.append("Report omits the identified inherited-input caveat")
    note_count = 0
    for note in (root / "results/notes").glob("*.md"):
        code = note.name.split("-", 1)[0]
        warning = policy["note_warnings"].get(code)
        if not warning or warning not in "\n".join(note.read_text(encoding="utf-8").splitlines()[:6]):
            errors.append("Missing or stale per-note current-use warning: " + note.name)
        note_count += 1
    if note_count != 25:
        errors.append("Expected all 25 complete reading notes")
    register = (root / "results/CLAIMS.md").read_text(encoding="utf-8")
    for ident, review in reviews.items():
        if review["disposition"] == "open":
            marker = f"## {ident}\n"
            block = register.split(marker, 1)[-1].split("\n## ", 1)[0]
            if "问题出处（不是证明）" not in block or "**完整证明：**" in block:
                errors.append("Problem source mislabeled as a proof: " + ident)
    return {"status": "passed" if not errors else "failed", "version": policy["version"],
            "research_records": len(reviews), "headline_record_indices": len(headlines),
            "disposition_counts": counts, "reading_notes_with_current_use_warnings": note_count,
            "scope": "Editorial consistency and listed dependency gates only; not verification of mathematical proofs.",
            "errors": errors}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="read-only validation (also the default)")
    args = parser.parse_args()
    result = validate()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return result["status"] != "passed"


if __name__ == "__main__":
    raise SystemExit(main())
