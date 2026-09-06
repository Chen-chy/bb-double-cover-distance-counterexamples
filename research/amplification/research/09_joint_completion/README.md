# BB slope-(2,1) joint-completion research

Read `REPORT.md` for the exact all-message graph reduction, proofs, and limits.
The half-weight completion lemma and the full factor-three inequality remain
unresolved. This bundle contains no new amplification record.

## Reproduce all checks

Python 3.10 or later; standard library only:

```sh
python verify_graph.py
python verify_components.py
python verify_majority_control.py
python verify_pareto.py
```

Each command writes a JSON verification record. `verify_pareto.py` re-audits
three lower-bound certificates from the supplied previous round, rather than
assuming that a failed finite search excludes a lower weight.

## Files and provenance

`laurent.py` and `graph_completion.py` implement the full compact signed-cut
normal form and exact elimination of odd boundary variables. The other scripts
reconstruct identities or finite matrices separately where described in the
report. None is a proof-assistant formalization.

`previous_report.md` is the supplied previous report, retained for provenance.
`previous_certificates/` retains its five original certificate files and
independent audit program. The current Pareto proof needs three of those
lower bounds. The old 6-to-14 distances are not a new record; the new result
is the complete projection/completion frontier {(12,1),(14,0)}.

The 182-to-550 majority control is a BASE BOUNDARY. It refutes only a
restricted local-lift assertion for arbitrary circuits, even with strict
single-stabilizer stability. It is not a logical-distance counterexample.

The fixed-message support bound in the report is proved uniformly. It does
not supply an a priori finite range of all homology messages.
