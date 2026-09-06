# Compact survival and all-weight BB cover bounds

Read `REPORT.md` for the symbolic proofs, exact scope, and dependencies.

## Main results

For binary strict-trinomial BB double covers, the report proves compact survival in the genuinely higher-rank, non-finite-check incidence regime at every circuit weight. The argument identifies a universal cyclic homology generator and proves a finite nonboundary directly; it does not assume that homology commutes with specialization.

The resulting elementary all-weight bound is

    d2 <= max(2*d^4, 8*d^3, 4*d^(log2(9))).

This gives d2 <= 2*d^4 for d >= 4. The previously established d=2 case extends that simpler formula to all distances. No classifications at d=4 or d=6 are required. Independently of that small-case input, d2 <= 4*d^4 is immediate.

Using the published arbitrary-boundary geometric distance theorem further gives d2 = O(d^(log2(9))) and Gamma(N) = O(sqrt(N)). These are not constant-factor amplification bounds. The supplied 7/3 record is not recomputed or improved here.

## Reproduce the supplementary arithmetic checks

Only Python 3.10 or later is required. There are no third-party package dependencies, external solvers, decoder estimates, or heuristic lower-distance claims.

```sh
python run_all.py
```

The checks are supplementary to the symbolic proof, not an exhaustive classification of eight-column cases.

- `verify_mechanisms.py` checks the root-polytope minors, the nilpotent-pencil mechanism over an exact rational-function field and finite fields, and the explicit specialization negative control outside the BB class.
- `verify_finite_covers.py` builds finite term-matched covers and constructs primal/dual logical certificates.
- `audit_finite_certificates.py` independently verifies those certificates without importing the construction, rank, or field routines. A nonboundary is certified by a functional orthogonal to every boundary but not to the proposed cycle.
- `verify_weight8_testbed.py` checks a compact weight-eight mechanism and weight-sixteen cover logicals. Exact minimum distances are deliberately not asserted.

The JSON files are retained outputs. All bounds called symbolic in the report have explicit proofs independent of the finite-code tests. The code is not a proof-assistant formalization or an independent human referee report.

## Scope cautions

Compact survival is not asserted for arbitrary Koszul deformations. The report contains a concrete counterexample to that unrestricted statement, including a nonzero tensor-product homology term whose entire edge image is killed. Low-rank and finite-check incidence cases are bounded geometrically or by finite subgroup size instead.

No constant C_* is proved finite, and no unbounded-ratio family is constructed. The new result rules out bounded base distance with unbounded cover distance at every fixed distance, not just through distance six.
