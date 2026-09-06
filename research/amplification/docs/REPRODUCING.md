# Reproduction guide

## 1. Preserve archival bytes; run in working copies

Historical scripts often write JSON or logs beside themselves. The original
snapshots must therefore be treated as immutable. `tools/run_checks.py` makes a
full writable copy before executing them. It restores every original path from
the provenance map, including byte-identical inherited files stored once in the
repository. No symlink behavior, old `/mnt/data` path, external workspace, or
network download is required.

```sh
python tools/check_repository.py
python tools/run_checks.py --profile audit --list
python tools/run_checks.py --profile audit --output .work/audit-1
```

Use a new output path for each run; existing log directories are not silently
overwritten. `--timeout 0` disables the wrapper's per-command timeout. Any wrapper
timeout is logged as **incomplete**, not a mathematical result.

To work directly with one round:

```sh
python tools/materialize.py --module 10_nonlocal_exchange --output .work
cd .work/10_nonlocal_exchange
python run_all.py
```

The original README's relative paths apply in that materialized copy. `--force`
only replaces a directory carrying the materializer's own marker; it does not
alter `research/`.

## 2. Requirements

The historical programs target Python 3.10 or later. Do not use `python -O` or
set `PYTHONOPTIMIZE`: assertions are part of the audit logic. Most certificate
audits use only the standard library.

C++17 with a compiler named `g++` is needed for the finite circuit engines,
meet-in-the-middle exclusion, compact-certificate regeneration, and exhaustive
incidence classification. SymPy is needed for the full Smith/Hermite checks.
NumPy is needed only to regenerate the latest Bellman certificate, not to audit
it. The exact installed versions used at export are recorded in
`checks/export_2026-09-06/audit_summary.json`. A convenience requirements file
pins those nonstandard packages; the recorded environment used Python 3.13.5.
Availability of the pinned packages on older Python versions was not tested.

```sh
python -m pip install -r requirements-reproduction.txt
```

This installation is not required for the latest standard-library audit:

```sh
python tools/run_checks.py --profile audit \
  --module 10_nonlocal_exchange --output .work/latest-audit
```

No external optimizer, SAT service, decoder, API credential, or connected account
is required.

## 3. What the default audit profile does

| Module | Selected export-safe checks |
|---|---|
| 03 | Compile final engines; finite theorem tests; 45 brute-force cross-checks; exact seed/reduced checks; independent polynomial exclusions; independent subset exclusion |
| 04 | Reconstruct the 684 retained nine-generator matrices with Smith/Hermite forms; **not** rerun both broad classifications |
| 05 | Independent retained finite dual audit and algebraic mechanism checks |
| 06 | Independent retained dual audit, sparse-generator identities, faithful generic-evaluation tests, sharpness check |
| 07 | Independent retained certificate audit and seed-coordinate identity check |
| 08 | Audit all five complete closure certificates and structural/finite witness checks |
| 09 | All four retained graph/component/negative-control/Pareto checks |
| 10 | Original `run_all.py`: identities, forests, tree contractions, triangle, Bellman certificate, separated-message identities, inherited lower certificates |

The wrapper records command arguments, environment, return code, elapsed time,
and combined stdout/stderr. A failure is reported, not repaired by silently
changing mathematics or archived data. Original historical logs remain separate.

## 4. Full reproduction and regeneration

Regeneration runs existing algorithms; it is deliberately opt-in. It may perform
large finite enumerations or overwrite output files in the **working copy**.
No claim is made that every generation path was rerun during export.

```sh
python tools/run_checks.py --profile regenerate --allow-regeneration \
  --module 04_distance6_obstruction --output .work/d6-full --timeout 0
```

The distance-six original pipeline rebuilds both exhaustive enumerations,
including 34,826,760 direct pairing checks, the roughly 19 MB omitted historical
intermediate `rank2_candidates.jsonl`, filtering, explicit certificates, full-
matrix checking, and 4,000 finite power-cycle tests. The source and retained final
certificate data are present; that omitted intermediate was already omitted in
the original bundle and is not needed for the lightweight retained-data audit.

For the compact minima:

```sh
python tools/run_checks.py --profile regenerate --allow-regeneration \
  --module 08_slope21_shortening --output .work/compact-full --timeout 0
```

For the latest Bellman certificate, regeneration needs NumPy:

```sh
python tools/run_checks.py --profile regenerate --allow-regeneration \
  --module 10_nonlocal_exchange --output .work/bellman-full --timeout 0
```

Round 03's `verify_all.py` re-audits every retained search instance and recomputes
base exclusions; it is more work than the selected audit. Its original discovery
scans are separate. See that round's preserved README for `BB_EXECUTABLE` and the
historical pre-packing engine. Do not expect node counts or capped discoveries
to remain identical after changing engine version or branch order.

The other round-specific full commands are recorded by
`python tools/run_checks.py --profile regenerate --list`. No regeneration profile
claims to reproduce the unavailable original first-round ZIP or its missing raw
logs.

## 5. Recovered early source

The early sources in `history/recovered_round1/` and `history/recovered_round2/`
have a different provenance class: they were transcribed from visible tool-call
source text, not recovered original file bytes. Their READMEs state exact scope
and commands. Do not run the random/template discovery scripts merely to audit
the current theorem ledger. Export-time checks of the recovered seed and d=4
programs are under `checks/export_2026-09-06/recovered_*`.

## 6. Interpreting reproduction differences

Timings are diagnostics. Several original JSON logs include elapsed times, so
byte differences after reruns do not imply a different mathematical result.
Original source hashes are never updated to match a fresh run. The export records
which working-copy outputs differed; the source archive remained unchanged.

For exact searches, `found=true` is an upper witness; `found=false, cutoff=false`
can be a lower exclusion only within the proved search scope. `cutoff=true` is
unresolved. For primal/dual audits, nonboundary is proved but minimum distance
is not unless an independent lower argument is also supplied. For closure or
Bellman certificates, inspect both transition completeness and the accepting
homology test, not only the attaining word.

## 7. Rebuild the release container

For unchanged delivered files, the deterministic packaging helper verifies the
release manifest and creates a ZIP plus an external SHA-256 checksum:

```sh
python tools/package_release.py --output .work/release/repository.zip
```

After intentionally adding or changing documentation or a new research round,
review those changes before using `--write-manifest`. That option updates only
the top-level release manifest; it never rewrites the historical per-round
manifests. ZIP entry metadata is fixed for this archival release and is not
presented as a discovery timestamp.
