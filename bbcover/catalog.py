"""Read the complete claim register without depending on a source checkout."""
from __future__ import annotations
import json
from importlib.resources import files
from typing import Any


def catalog() -> dict[str, Any]:
    """Return a fresh decoded register, including explicit evidence limitations."""
    return json.loads(files("bbcover").joinpath("catalog.json").read_text(encoding="utf-8"))


def find_results(identifier: str | None = None, *, branch: str | None = None,
                 status: str | None = None, view: str = "all") -> dict[str, Any]:
    data = catalog()
    rows = data["results"]
    allowed = {"all", *data["review_categories"]}
    if view not in allowed:
        raise ValueError(f"Unknown result view: {view!r}")
    if identifier is not None:
        matches = [row for row in rows if row["id"] == identifier]
        if not matches:
            raise ValueError(f"Unknown result identifier: {identifier!r}")
        rows = matches
    if branch is not None:
        rows = [row for row in rows if row["branch"] == branch]
    if status is not None:
        rows = [row for row in rows if row["status"] == status]
    if view != "all":
        rows = [row for row in rows if row["review"]["disposition"] == view]
    return {"view": view,
            "record_warning": "Research records are not all valid or independent theorems. See review.disposition, scope and evidence limitations.",
            "schema_version": data["schema_version"], "version": data["version"],
            "count": len(rows), "path_convention": "Proof/evidence paths are relative to the complete research repository, not the installed wheel.",
            "results": rows}
