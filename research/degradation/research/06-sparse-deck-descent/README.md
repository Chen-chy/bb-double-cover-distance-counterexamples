# Reproduction package: sparse deck-involution descent

Read `proof.md` for the exact theorem, its scope, and its proof.
Run with Python 3.9 or later, using only the standard library:

```sh
python3 verify.py
```

This regenerates `cases.json` and `verification_summary.json` deterministically.
`run_all.sh` also saves the printed record to `run_output.txt`.

The new result is conditional on a compact incidence lift over an odd-torsion
one-involution strip, with that involution equal to the deck kernel. It is
not a global proof of quadratic BB double-cover descent.

The checks are exact polynomial and binary linear algebra checks. No
minimum-distance computation or new exact distance record is claimed.
