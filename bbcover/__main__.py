"""Inspect certified examples, compare covers, calculate bounds, and search results."""
from __future__ import annotations
import argparse
from dataclasses import asdict
from fractions import Fraction
import hashlib
import json
from . import __version__
from .bounds import cubic_interval
from .catalog import find_results
from .code import validate_double_cover
from .examples import get_example, names
from .gf2 import rank


def inspect_example(name: str) -> dict:
    code, witness, data = get_example(name)
    return {"example": name, "n": code.n, "k_recomputed": code.k,
            "rank_HX": rank(code.hx_rows), "rank_HZ": rank(code.hz_rows),
            "connected": code.is_connected(), "witness_weight": witness.bit_count(),
            "witness_is_nonboundary_cycle": code.is_logical(witness),
            "distance_from_independent_certificate": data["parameters"][2],
            "distance_recomputed_by_this_command": False,
            "certificate": data["certificate"],
            "matrix_sha256": {s: hashlib.sha256(code.matrix_bytes(s)).hexdigest()
                              for s in ("X", "Z")}}


def compare_cover(which: str) -> dict:
    if which not in {"upper", "lower"}:
        raise ValueError("Cover must be 'upper' or 'lower'")
    base_name, cover_name = ("q39", "q78") if which == "upper" else ("q78", "q78x2")
    base, _, base_data = get_example(base_name)
    cover, _, cover_data = get_example(cover_name)
    d, d2 = base_data["parameters"][2], cover_data["parameters"][2]
    return {"counterexample": which, "base": inspect_example(base_name),
            "cover": inspect_example(cover_name), "cover_validation": validate_double_cover(base, cover),
            "ratio_d2_over_d": str(Fraction(d2, d)),
            "violated_claim": "d2 <= 2*d" if which == "upper" else "d2 >= d",
            "violation_verified_using_certified_distances": d2 > 2*d if which == "upper" else d2 < d,
            "distance_recomputed_by_this_command": False,
            "exact_distance_verification": "python scripts/reproduce.py --profile core --output checks/new-run",
            "scope": "This command reconstructs ranks, witnesses and cover maps; exhaustive distance exclusion is performed by the independent certificate verifiers."}


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", action="version", version=__version__)
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("inspect", help="reconstruct a fixed certified example")
    p.add_argument("example", choices=names())
    p = sub.add_parser("compare", help="check one of the two double-cover examples")
    p.add_argument("cover", choices=("upper", "lower"))
    p = sub.add_parser("bounds", help="evaluate the integer-safe cubic interval (not the analytic pi cap)")
    p.add_argument("d", type=int)
    p.add_argument("--n", type=int, help="base number of qubits")
    p.add_argument("--k", type=int)
    p.add_argument("--k2", type=int)
    p = sub.add_parser("results", help="read the complete, evidence-qualified claim register")
    p.add_argument("identifier", nargs="?")
    p.add_argument("--branch", choices=("main", "homology", "amplification", "degradation"))
    p.add_argument("--status", help="exact status string, as stored in the register")
    args = parser.parse_args(argv)
    try:
        if args.command == "bounds":
            result = asdict(cubic_interval(args.d, args.n, k=args.k, k2=args.k2))
        elif args.command == "inspect":
            result = inspect_example(args.example)
        elif args.command == "compare":
            result = compare_cover(args.cover)
        else:
            result = find_results(args.identifier, branch=args.branch, status=args.status)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
