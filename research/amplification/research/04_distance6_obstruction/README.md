# BB distance-six obstruction

Read `REPORT.md` for the proof and scope.

## Main conclusion

For every valid binary strict-trinomial BB double cover with positive base dimension,

    base distance 6  =>  cover distance at most 112.

This is a uniform computer-assisted theorem. It does not assert optimality of 112,
a finite universal bound on the amplification ratio, or a new distance record.
The core higher-rank mixed mechanisms actually give cover distance at most 12;
the larger constant comes from low-rank strip/finite-size cases.

## Standalone exhaustive verifier

Only a C++17 compiler is needed:

```sh
g++ -O3 -std=c++17 verify6_all_pairings.cpp -o verify6_all_pairings
./verify6_all_pairings > independent_pairings.json
```

This program generates every perfect pairing of eighteen incidences with no
same-column pair, for each of the three mixed support types. It uses no supplied
graph list, external solver, random sampling, node cutoff, or distance decoder.
It fails explicitly if a presentation violates the bounds or is unclassified.

## Reproduce all checks

Requires Python 3.10+, g++, and SymPy for the third arithmetic check:

```sh
python run_all.py
```

This additionally generates all 640 connected labeled cubic multigraphs, checks
2,488,320 normalized presentations with a separate implementation, reconstructs
the full nine-generator matrices for all 684 retained higher-rank cases with
Smith/Hermite normal forms, and tests the new power-cycle lemma on 4,000 finite
covers. The finite cover checks certify logical witnesses, not exact distances.

The run regenerates `rank2_candidates.jsonl`, an intermediate file of about 19 MB.
It is not included in the archive, but all code needed to recreate it is supplied.
Executables are also omitted. Elapsed seconds in output files are diagnostic only.

## Files

- `REPORT.md`: complete proof, classification interpretation, limits, and next lemma.
- `verify6_all_pairings.cpp`: independent all-pairings verifier.
- `generate_graphs.py`, `enumerate6_bounded.cpp`: normalized graph enumeration.
- `presentations.py`, `filter6.py`, `certify_highrank6.py`: exact group reduction,
  circuit filters, and explicit algebraic/boundary certificates.
- `verify_presentations_sympy.py`: independent full-matrix arithmetic check.
- `verify_frobenius.py`, `finite_algebra.py`: finite power-cycle lifting checks.
- `highrank6_certificates.json`: relation matrices, coordinates, classification,
  and explicit boundary/gauge certificates for the retained cases.
- JSON summaries and logs: retained successful execution records.

`finite_algebra.py` is retained from the supplied prior-round bundle. It is used
only in supplementary finite checks; it is not used by either exhaustive
presentation verifier. The new symbolic proof does not depend on prior distance
searches.

Separate implementations are not an independent human referee report or a
proof-assistant formalization. The supplied scripts make the finite part of the
argument directly reproducible and inspectable.
