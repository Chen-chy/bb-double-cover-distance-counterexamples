# Nonlocal source-free tree exchanges for BB slope (2,1)

Read `REPORT.md` first. The factor-three inequality is **not** proved or refuted.

The new uniform results are the exact source-free-tree/independent-set reduction,
a sharper anchor-interval theorem, and the complete two-equation common-message
characterization. All messages remain in the full compact optimization.

## Reproduce the retained audits

Python 3.10+; standard library only:

```sh
python run_all.py
```

This verifies formal algebraic identities, full-spin comparisons with the exact
forest reduction, all-or-nothing tree contractions, a genuine odd conflict cycle,
a Bellman certificate for one fixed-message minimum, the separated-message
identities, and the two inherited compact-distance certificates.

The conditional value 74 (or 74N) is **not a code distance** and is not the full
compact minimum. The same universal class has minimum fourteen. The report gives
an explicit universal boundary between the exhibited representatives. This
negative control tests proof quantifiers; it is not an amplification construction.

`fixed_message_potential.bin` is a lower Bellman-potential certificate. The
independent auditor checks every legal transition inequality and a matching
attaining word. The anchor-interval proof, not a numerical truncation, justifies
its finite domain. The lexicographic objective also certifies support fifteen
among minimum-energy fields.

The inherited minimum-six and minimum-fourteen certificates are clearly isolated
in `inherited_certificates/`; they are re-audited, not claimed as new searches.

## Regenerate the new Bellman certificate

This optional step requires NumPy:

```sh
python make_fixed_certificate.py
python audit_fixed_certificate.py
```

`laurent.py` and `graph_completion.py` are retained baseline modules from the
preceding round and are used by the construction. The independent Bellman,
triangle, finite-dual, and formal-identity auditors do not import their arithmetic.

No node-limited search, decoder output, or heuristic failure is used as a minimum
certificate. These proofs and programs are not proof-assistant formalizations.
