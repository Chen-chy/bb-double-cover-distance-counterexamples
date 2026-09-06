# Strict-trinomial quadratic bottleneck: research and exact checks

The universal quadratic bound is **not proved or refuted** by this package.

Read `proof.md` for the new theorems and their restrictions. The main result is compact/linear descent for support-generated rank-one presentations with odd-order torsion. It reduces the unresolved mixed finite/strip case to visible 2-primary torsion. The package also proves an exact specialization formula, gives a cyclic-torsion gcd criterion, and demonstrates why a short-row cofactor estimate cannot by itself become quadratic.

Run:

```sh
./run_all.sh
```

Python 3 is sufficient; no third-party libraries are needed. The checks use exact binary and integer arithmetic.

`verify.py` and `verify_independent.py` check the odd-torsion statement by different constructions. `verify_cyclic_strip.py` tests the explicit gcd formula against finite binary matrices. `summary.json` records the results, `manifest.json` hashes the source and output files, and the case JSON files contain reproducible inputs and exact computed dimensions.

These are finite consistency checks of symbolic proofs, not exhaustive incidence classifications and not new minimum-distance or degradation records. The previous cubic bound and 6/7 construction are inherited, with their supplied certification status.
