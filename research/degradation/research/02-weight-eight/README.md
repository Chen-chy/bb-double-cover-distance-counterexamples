# Strict-trinomial weight-eight quotient certificate

Main result: a term-preserving finite abelian quotient of a strict-trinomial code of distance exactly eight has base distance at most 96, provided the base has positive dimension. In particular, `d_2=8 => d<=96` for every valid strict-trinomial binary BB double cover.

Read `proof.md` for the complete mathematical argument, the scope of the theorem, and the dependencies of the ratio corollaries. This is a computer-assisted proof, not a bounded-size code search.

## Reproduction

Requirements: Python 3.10 or later, SymPy 1.14.0, and a C++17 compiler. The exact Python dependency is pinned in `requirements.txt`. The tested versions are recorded in `verification_summary.json`.

Run:

```sh
bash run_all.sh
```

The script recompiles the generators and reruns the complete 40,917,312-assignment mixed enumeration and 5,598,720-assignment pure enumeration, then runs all independent checkers. It writes logs and recreates the TSV/JSON results. Integer overflow bounds are checked during the C++ row reductions.

For an arithmetic audit of the retained catalogues:

```sh
python3 verify_graphs.py
python3 verify_highrank.py
python3 verify_low_and_pure.py
python3 verify_nilpotent_lemmas.py
python3 verify_summary.py
```

Checking retained certificates alone does not replace the exhaustive generator for completeness.

## Files

`graphs_eight.cpp` and `colorings.py` generate graph and colouring representatives. `verify_graphs.py` independently counts labelled graphs using a degree-sequence recurrence and verifies representative and colouring completeness.

`classify_eight.cpp` enumerates and retains all admissible mixed presentations with at least two free directions. `scan_low_free.cpp` retains every distinct finite/strip relation lattice, before admissibility filtering. `pure_eight.cpp` handles the pure-block case.

`verify_highrank.py` reconstructs original graph/port relations and uses independent exact Smith decompositions, cycle calculations, and explicit fillings. `verify_low_and_pure.py` uses integer minors and index comparisons instead of the generator's row-reduction algorithm.

`verify_nilpotent_lemmas.py` checks finite witnesses by binary matrix rank and span membership. It does not compute or claim exact code distances; the uniform proofs are in the note.

`verify_summary.py` checks complete accounting, all verifier results, and catalogue hashes. `verification_summary.json` is the concise result record. All claimed distance inequalities for infinite families of quotients are proved in the mathematical note.

No new finite ratio record, universal positive ratio, or vanishing-ratio family is claimed. The retained 6/7 upper construction is an input from the preceding research state, not recertified by this package.
