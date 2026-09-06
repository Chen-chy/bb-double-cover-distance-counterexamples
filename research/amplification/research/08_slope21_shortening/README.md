# Slope-(2,1) BB compact-shortening research

**Status:** the full factor-three inequality remains unresolved. This bundle
proves sharp factor-two universal-sector purification, gives an exact
projection/syndrome-completion formula, and certifies a counterexample to
stronger sector-first shortening claims. It does not contain an amplification
ratio above 7/3 or a counterexample to factor three.

Read `REPORT.md` for definitions, complete structural proofs, the distinction
between universal and finite homology, and the precise remaining lemma.

## Audit the supplied minimum certificates

Run with Python 3.10 or later, without optimization mode (`-O`):

```sh
python audit_certificates.py
python verify_structure.py
```

Only the Python standard library is needed. The first command checks finite
sublevel closure under **every** possible transition, rather than trusting or
rerunning the shortest-path search. It also directly checks the attaining
cycles and their homology labels. The closure proof covers arbitrary finite
Laurent support lengths; it is not a support-window search.

The exact compact minima are:

- full base: 6;
- universally resonance-pure base: 12;
- universally complementary-pure base: 10;
- full cover: 14;
- universally resonance-pure cover: 16.

The restricted 12 and 16 must not be confused with actual base/cover code
distances. The physical cover distance in the long-period realization is 14,
not 16. The complete report explains why the killed universal component helps.

`verify_structure.py` checks the formal Laurent identities in four variables,
the explicit base-boundary adjustment, and finite matrices at L=201. It also
constructs dual functionals annihilating all boundaries and detecting the
attaining logicals. Its finite checks are witness/dimension checks; the exact
finite lower bounds combine the compact certificates with the symbolic
no-winding lemma.

## Regenerate the certificates

A C++17 compiler named `g++` is required only for regeneration:

```sh
python run_exact.py
python audit_certificates.py
```

`run_exact.py` compiles `trellis_exact.cpp`, obtains an attaining terminated
path, and writes the finite lower-bound certificates. The internal state cap
is a guard: a capped result is inconclusive and is rejected. None of the five
retained runs was capped. No upper witness alone is reported as a minimum.

## Files

`exact_results.json` records parameters and primal words. `certificates/*.bin`
contain sorted state/cost tables. `independent_audit.json` records the complete
closure audit. `structure_verification.json` contains the exact identity and
finite-homology checks. `MANIFEST.sha256` records content hashes.

The generator and closure auditor are independently implemented algorithms.
This bundle is not a proof-assistant formalization or independent human
referee validation. The symbolic proofs, certificate format, transition
semantics, and completeness argument are provided for adversarial inspection.
