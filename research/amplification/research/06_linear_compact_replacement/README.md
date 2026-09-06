# Exact compact replacement for strict-trinomial BB covers

Read `REPORT.md` for the precise theorem and proof.

The result is **compact factor two in the torsion–Frobenius normal form**, not an all-code factor-two claim. The exact compact representative weight is

    |T_odd| * 2^(a-b) * 3^b * (3^s+1),

where the two-primary invariant factors are 2^a >= 2^b and q=2^s. Every compatible double cover has exact compact ratio 1, 3/2, or 2 when compact base homology survives the chosen finite quotient.

The report proves a lower bound for every universal nonboundary and constructs a shortest representative generating the full compact module. It separates universal representative weight from actual finite quantum distance.

## Reproduce

Python 3.10 or later, standard library only:

```sh
python run_all.py
```

There are no heuristic distance-search cutoffs or external solvers. The principal theorem is symbolic; the scripts are supplementary checks, not a proof-assistant formalization.

`verify_sparse_generators.py` verifies exact sparse identities, weights, and explicit universal boundaries between the old and optimized generators.

`verify_embeddings.py` independently checks the faithful generic B-evaluation into a twisted finite group with polynomial coefficients in an indeterminate. It does not specialize that indeterminate to a finite field.

`field_distance.py` independently enumerates 15 small **classical** F_4 kernels. These are not quantum BB distances.

`verify_finite_replacement.py` constructs finite bivariate logicals and separating dual certificates. `finite_arithmetic.py` retains the binary arithmetic from the supplied previous bundle. `audit_replacement_certificates.py` imports none of those routines and independently checks all cycles, all boundaries, dual pairings, ranks, term matches, and norm images.

`verify_sharpness.py` gives the one exact finite quantum distance pair asserted in this round: [[18,4,2]] -> [[36,4,4]]. Its lower certificates are nonzero columns, odd column weight, and pairwise distinct cover columns. This is a sharpness example for the compact theorem, not a new amplification record.

JSON files and `.log` files retain execution records. `SHA256SUMS.json` hashes the included files. No binary executables or font files are included.

## Limits

The global constant C_* remains unresolved. The old 7/3 record is not re-established by this bundle, and no larger ratio is asserted. The cubic all-code corollary combines this result with the explicitly identified presentation estimates and geometric theorem from the supplied prior proof state.
