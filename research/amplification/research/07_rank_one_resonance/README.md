# Rank-one BB resonance: reproducibility bundle

Read `REPORT.md` for the complete symbolic proof, scope, and unresolved inequality.

## Status

The all-cases rank-one factor-three bound is **not proved or refuted**. This round proves factor two for one-sided defects and several additional exhaustive parity branches, identifies the remaining two-sided cyclotomic resonance, constructs a slope-dependent replacement, and proves eventual equality of compact and actual finite distances along explicit period progressions.

The large-period theorem does not turn an expensive chosen representative into a counterexample. It applies to the minimum over all compact classes and all boundary adjustments.

## Reproduce

Python 3.10 or later; standard library only. No solver, numerical approximation, network access, or external package is required.

```sh
python verify_structure.py
python verify_lifts.py
python check_seed_coordinates.py
python verify_finite_parity.py
python verify_sharpness.py
python audit_certificates.py
```

`arithmetic.py` implements the construction arithmetic. The auditor imports none of it and rebuilds finite boundaries, group multiplication, ranks, and the separating-dual tests independently.

The retained JSON files are full completed execution records. They certify exact identities, dimensions, membership, and nonboundary witnesses. They are not a new table of exact quantum distances. The existing seed's exact distances are inherited from the supplied certificates and are not re-enumerated here.

The proof is symbolic with independent exact computational checks; it is not proof-assistant formalization or a human referee report.

## Files

- `REPORT.md`: proofs, exact reduction, limitations, and next lemma.
- `arithmetic.py`: binary polynomial, Laurent, and finite-cover construction arithmetic.
- `verify_structure.py`: cyclic-module, transfer, compact-image, and period-stability checks.
- `verify_lifts.py`: derivative, parity/resonance, and divided-Euler constructions.
- `check_seed_coordinates.py`: locates the supplied seed in the residual resonance family.
- `verify_finite_parity.py`: finite split-cover parity checks, including noncompact logicals.
- `verify_sharpness.py`: exact finite lower checks for the uniform factor-two sharpness family.
- `audit_certificates.py`: independent finite nonboundary and rank auditor.
- `*_summary.json`, `*_cases.json`, `*_certificates.json`: retained exact records.
- `run_all.py`: repeat all verifications in dependency order.
