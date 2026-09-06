# BB double-cover counterexample: referee package

Exact claim:

```
A = A_tilde = 1 + x^8 + x^25
B = B_tilde = 1 + x^2 + x^13
(ell,m) = (39,1)
(ell_tilde,m_tilde) = (78,1)
[[78,4,6]] -> [[156,4,14]]
14 > 2*6
```

## Run either verifier as a single standalone file

Python 3.10 or later, standard library only. No package installation, network,
randomness, floating-point arithmetic, solver, or input data files are needed.

```sh
python3 verify_bitset.py
python3 verify_polynomial.py
```

Each must exit with code 0 and end its stdout with exactly:

```
BB_DOUBLE_COVER_COUNTEREXAMPLE_VERIFIED
```

The first uses integer-bitset matrices, binary boundary-span elimination, and
first-present-neighbor branching. The second uses sparse polynomial sets,
Bezout-congruence boundary membership, and all-odd-subsets branching. Neither
imports or reads the other. Both independently perform the full Z and X distance
exclusions. No expected circuit support list is used in either enumeration.

To regenerate the matrices, all 741 cover circuits, ten canonical orbit records,
and full per-root search statistics in separate directories:

```sh
python3 verify_bitset.py --output-dir regenerated_bitset
python3 verify_polynomial.py --output-dir regenerated_polynomial
```

Their four matrix files and `circuits.txt` must agree byte for byte. The JSON
reports' `circuits` objects (including all preimages), ranks, and results agree.
Search-tree node counts deliberately differ because the branch rules differ.

## Files

`CERTIFICATE.md` is the complete mathematical certificate, organized in the
requested sections A-H. It proves source-scope validity, including m=1, the
polynomial dimensions, all displayed witness identities, search completeness,
safety of each pruning/stopping rule, the orbit classification, and X/Z equality.

`verify_bitset.py` and `verify_polynomial.py` are the standalone verifiers.
`bitset_run.txt` and `polynomial_run.txt` are their actual successful stdout
transcripts from this certification run, not hand-written expected outputs.

`bitset_output/` and `polynomial_output/` contain the independently regenerated
matrices, complete short-circuit set, and JSON reports. Matrices include all
specified stabilizer rows, including the two dependent rows; their row/column
order and exact SHA-256 serialization are defined in the mathematical certificate.

`EXECUTION_METADATA.json` records the actual interpreter, process exit codes,
script/transcript hashes, and the subsequent bytewise cross-comparison.

`source/2511.13560v3.pdf` is the original attached primary-source PDF. It is not
needed by the computational verifiers. `source/SOURCE_NOTE.md` pins its hash and
identifies the precise definition/theorem pages used.

`SHA256SUMS.txt` hashes every other file in this package. It is an integrity
manifest, not a substitute for running and inspecting the verifiers.

## Result of the packaged run

Both finalized verifiers completed with exit code 0 and the required success
line. All four matrices, all 741 circuits, all ten canonical orbit records and
preimages, both ranks, and both distances agree between implementations. The
statements certified are computer-assisted mathematical statements, not claims
of third-party peer review or proof-assistant formalization.

STATUS: UPPER_BOUND_FALSE
STATUS: ORIGINAL_DISTANCE_CONJECTURE_FALSE
