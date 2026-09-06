#!/usr/bin/env python3
"""Exact implementation audit of the root determinants and index-two transport.

The universal proof is Lemma 3.4 in the manuscript (refer to its label if numbering
changes). This deterministic finite audit tests identities, not all BB codes.
"""
import argparse
import itertools
import json
from pathlib import Path
import random


def determinant(rows):
    n = len(rows)
    if n == 0:
        return 1
    if any(len(r) != n for r in rows):
        raise ValueError("Expected a square matrix")
    if n == 1:
        return rows[0][0]
    return sum((-1)**j * rows[0][j] * determinant([r[:j] + r[j+1:] for r in rows[1:]])
               for j in range(n))


def cofactor(rows):
    if len(rows) != 3 or any(len(r) != 4 for r in rows):
        raise ValueError("Expected three relation rows in Z^4")
    return tuple((-1)**j * determinant([r[:j] + r[j+1:] for r in rows]) for j in range(4))


def need(condition, message):
    if not condition:
        raise RuntimeError(message)


def audit():
    positive = [(1,0,0,0),(0,1,0,0),(1,-1,0,0),
                (0,0,1,0),(0,0,0,1),(0,0,1,-1)]
    roots = positive + [tuple(-v for v in r) for r in positive]
    histogram = {-1: 0, 0: 0, 1: 0}
    for rows in itertools.product(roots, repeat=4):
        d = determinant(list(rows))
        need(d in histogram, "Port-root determinant is not 0 or +/-1")
        histogram[d] += 1
    rng = random.Random(20260906)
    count = 0
    for _ in range(512):
        while True:
            rows = [tuple(rng.randrange(-9, 10) for _ in range(4)) for _ in range(3)]
            c = cofactor(rows)
            if any(c):
                break
        need(all(sum(a*b for a,b in zip(row,c)) == 0 for row in rows), "Cofactor orthogonality")
        for parity in itertools.product((0, 1), repeat=3):
            index = 2 if any(parity) else 1
            coeff = [[int(i == j) for j in range(3)] for i in range(3)]
            if any(parity):
                pivot = parity.index(1)
                coeff[pivot][pivot] = 2
                for i in range(3):
                    if i != pivot:
                        coeff[i][pivot] = -parity[i]
            need(determinant(coeff) == index, "Kernel basis must have index one or two")
            need(all(sum(a*b for a,b in zip(v,parity)) % 2 == 0 for v in coeff), "Odd kernel voltage")
            lifted = [tuple(sum(v[j]*rows[j][t] for j in range(3)) for t in range(4)) for v in coeff]
            need(cofactor(lifted) == tuple(index*t for t in c), "Cofactor transport failed")
            count += 1
    return {"status": "passed", "root_determinants": 12**4,
            "root_determinant_histogram": histogram, "rank_three_samples": 512,
            "all_voltage_cases_checked": count, "random_seed": 20260906,
            "scope": "exact algebraic identity tests, not a proof by finite examples"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    data = audit()
    text = json.dumps(data, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
