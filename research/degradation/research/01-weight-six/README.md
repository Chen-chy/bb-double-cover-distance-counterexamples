# Reproduction package

Read `proof.md` for the mathematical arguments and their scope. The principal conclusion is the computer-assisted uniform implication d>56 => d_2>=8, using the prior weight-four exclusions supplied with the task. The package also gives a uniform counterexample to the two-check filling lemma and unbounded lifted filling weights for weight-six boundaries. It does not resolve the infimum of d_2/d.

Requirements: Python with SymPy, and a C++17 compiler (`g++` by default).

Run from this directory:

```sh
bash run_all.sh
```

The pipeline regenerates all six abstract pairing graphs, enumerates all pure and mixed port assignments, verifies the retained mixed presentations with independent Smith computations, and checks finite members of the filling family using exact GF(2) arithmetic.

Core files:

- `proof.md`: uniform proofs, completeness argument, and limitations.
- `graphs.py`, `pure_six.py`, `classify_six.cpp`: exhaustive incidence enumeration.
- `mixed_presentations.tsv`: all 5392 retained mixed presentation-cycle pairs.
- `verify_presentations.py`: independent exact check of every retained mixed pair.
- `pure_six_results.json`: pure-cycle counts and fourteen certificates.
- `verify_family.py`, `family_verification.json`: finite checks, without claiming exact distances.
- `presentation_verification.json`: aggregate checked bounds and zero unresolved cases.

The optional discovery scripts `finite_scan.py` and `classify_rank_two.py` are not needed for the proof pipeline. They are retained for auditability.

The catalogue is not a table of finite codes, and its formal cycles are not presumed nontrivial in finite quotients. The mathematical implications for actual finite homology are in Sections 4 and 5 of the proof note.
