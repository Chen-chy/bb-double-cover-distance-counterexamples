# Reproducing the available packages

## Environment

Use Python 3.10 or newer. The export environment reports Python 3.13.5 and SymPy 1.14.0; exact environment strings are in `checks/export/retained-verifiers/report.json`. Only stages 01–03 need the pinned third-party dependency. Later packages use standard-library Python. C++17 and a `g++`-compatible compiler are needed for full regeneration in stages 01, 02, and 07. Set `CXX` to choose a compiler.

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/check_integrity.py
```

Integrity checking verifies original ZIP digests and CRCs, complete member coverage, byte-identical extracted files, standalone-upload mappings, original manifests, Python syntax, and the root checksum manifest. It does not check mathematical truth.

## Preferred workflow: disposable copies

The wrapper only runs the original programs. It copies one stage at a time into a temporary directory, captures stdout/stderr and return codes, retains changed JSON/TSV/log/certificate outputs separately, and checks that original research files remain unchanged.

```sh
python scripts/run_checks.py --list
python scripts/run_checks.py --mode verify --output checks/local/all-retained
```

Choose a fresh output directory for each run; the runner refuses to overwrite an existing report. `checks/local/` is ignored by Git. The mode and exact commands are listed in `metadata/checks.json`. A per-command timeout can be changed with `--timeout`; a timeout is reported as a failure, never as a successful check.

For one or several stages:

```sh
python scripts/run_checks.py --stage 07-rank-one-amplification --output checks/local/bellman
python scripts/run_checks.py --stage 08-mixed-laurent --stage 09-fixed-c-product-bound --output checks/local/latest
```

The last command needs no SymPy and preserves the originals.

## Verification versus regeneration

| Stage | `verify` mode | `rebuild` mode |
|---|---|---|
| 01 weight six | Checks retained mixed presentations and the existing two filling-family instances. | Original full graph/pure/mixed enumeration, independent checkers, and catalogue hash. |
| 02 weight eight | Checks retained graph, high-rank, low-rank and pure certificates, nilpotent witnesses, and accounting. | Original complete graph/coloring and port-assignment generation, then all checkers. |
| 03 structural | Existing twist, geometry, and odd-sector checks. | Same checks; no incidence search belongs to this proof. |
| 04 bottleneck | Original, independent, and cyclic-strip checks; summary builder. | Same fixed suite. |
| 05 visible two-primary | Original contact, local, structured, family checks; summary builder. | Same fixed suite. |
| 06 sparse deck | Existing chain maps, replacement witnesses, and retained-involution controls. | Same fixed suite. |
| 07 rank-one amplification | Independent Bellman edge verification and finite matrix witnesses; no shortest-path search. | Recompile trellis generator, regenerate the already specified family certificates, then independently verify. |
| 08 mixed Laurent | Original sparse verifier and separate bit-polynomial audit. | Same fixed suite. |
| 09 fixed-$c$ | Original quotient, orbit, incidence, and inadmissible-control checks. | Same fixed suite. |

To regenerate a specific original certificate package:

```sh
python scripts/run_checks.py --mode rebuild --stage 01-weight-six --output checks/local/rebuild-six
python scripts/run_checks.py --mode rebuild --stage 02-weight-eight --output checks/local/rebuild-eight
python scripts/run_checks.py --mode rebuild --stage 07-rank-one-amplification --output checks/local/rebuild-bellman
```

The original package scripts are also retained and runnable from their directories, but they overwrite their local generated outputs. Use a separate copy, or the wrapper above, when preserving the snapshot matters. Read each original `README.md` for its own claims and cautions.

## Exact lower-bound certificates in stage 07

`base_potential.bin` and `cover_potential.bin` are little-endian unsigned-16-bit Bellman potentials, not executables. They contain 256 and 16,384 state values. `family_certificate.json` retains the encoders, labels, and equality witnesses. `verify.py` checks every edge inequality and the correct nonzero-homology terminal conditions, and independently checks that the encoder spans the complete universal cycle module. Removing these binary files would lose the retained all-degree lower-bound certificates.

Regeneration compiles `trellis.cpp` and runs `generate_family.py`. Do not confuse the optional exploratory `try_trellis.py` main program with the exact fixed-family certificate pipeline.

## Optional discovery material

Stages 01 and 07 contain exploratory scripts in addition to their proof pipelines. They are retained for provenance and continuation. The export did not run those discovery entrypoints, broaden a search, or generate new candidate codes. Stage 01's exact archived catalogues and supporting classification outputs remain available independently of those optional scripts.

## Interpreting output changes

Original summaries sometimes include elapsed seconds or environment strings. A rerun can produce different byte hashes solely from such metadata. The runner records all changed working-copy files and retains their regenerated contents; it does not edit the originals to make them match. Consult the relevant mathematical counters and checker exit status, as well as raw differences.

A successful stage 03/04/05/06/08/09 suite checks examples, identities, or displayed witnesses supporting its symbolic arguments; it does not compute new exact minima. The weight-six/eight retained-catalogue checks do not replace generator completeness. The stage 07 potential verification, in contrast, is an exact all-degree minimum certificate for the particular retained family.

## GitHub use

The tree can be committed as supplied; no local `.git` database is required by any checker. Original archive bytes are protected from line-ending conversion by `.gitattributes`. All source ZIPs and `.bin` certificates are intended to be tracked. Generated verifier runs and compiled programs are ignored; no Git LFS is needed for the sizes in this snapshot.

The included workflow uses a selected verification subset, not the exhaustive generators. Its status should not be described as a full mathematical audit. Authorship and licensing remain to be supplied by the repository owner; see `NOTICE.md`.
