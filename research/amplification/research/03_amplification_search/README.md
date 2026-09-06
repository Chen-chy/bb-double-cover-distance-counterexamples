# BB amplification research round

Read `REPORT.md` first. Principal status: **CONSTANT_BOUND_STILL_OPEN**.

The main symbolic results are the sharp univariate one-block dichotomy and the complete split-cover reduction with an exact physical-weight functional. The exact finite counterexample is to an intermediate reduced-distance lemma, not a new strict-trinomial BB amplification record.

## Reproduce the final evidence

Requirements: Python 3.10 or later, and a C++17 compiler named `g++`. The final verification path uses only the Python standard library; no mathematical solver or external package is required.

From this directory, run:

```sh
python verify_all.py
```

This compiles the final search engines, checks the finite theorem instances, runs 45 brute-force cross-checks, reproduces the exact seed and reduced-code certificates, runs the independent polynomial-oracle exclusions and independent meet-in-the-middle exclusion, and independently audits every retained cover witness used in the completed search conclusions.

The one-block and split-cover theorems have symbolic proofs in the report. Their finite checks are supplementary, not proofs by extrapolation. None of the results is claimed to have been formalized in a proof assistant or independently referee-reviewed.

## Important interpretation of records

`found=true` certifies only the existence of the displayed nonboundary at or below the supplied bound. It is not, by itself, an exact distance.

`found=false, cutoff=false` with positive k certifies exhaustive exclusion through the supplied bound.

`found=false, cutoff=true` is unresolved and is never a lower bound. In particular, the partial distance-eight scans contain such cases and do not certify larger amplification.

The C++ engines print search diagnostics such as node counts and elapsed seconds. Closed-cycle encounters are not canonical counts of matroid circuits. The independent implementations use different branch orders and need not have equal diagnostic counts.

The reduced-code meet-in-the-middle certificate is separate: it enumerates all 1,505,583 subsets of size at most four and checks all equal-syndrome pairs. Its retained counts are part of a complete finite calculation.

## Files

`search.cpp` is the final strict-trinomial exact circuit engine on C_l x C_m. Its line protocol is:

```text
l m ax0 ay0 ax1 ay1 ax2 ay2 bx0 by0 bx1 by1 bx2 by2 bound node_budget
```

A zero budget means no cutoff. At most 512 group elements, hence 1024 qubits, are supported. `BB_ORDER` optionally changes deterministic branch order.

`search_general.cpp` allows up to twenty total terms between the two check polynomials. Its protocol adds `number_of_A_terms number_of_B_terms` immediately after `l m`, followed by the corresponding coordinate lists, bound, and budget. It is used for the non-strict reduced code, not to enlarge the claimed BB search class.

`independent_search.py` uses Python integers and a Bezout normal-form boundary oracle. `mitm.cpp` supplies the separate reduced-code subset certificate. `algebra.py` builds independent finite matrices and group-algebra operations.

`verify_theorems.py`, `verify_search.py`, `audit_batch.py`, and `audit_templates.py` verify the principal claims and retained data. `base_certificates_*.json` contain fresh exhaustive base lower bounds and attaining witnesses. `audited_*.jsonl.gz` contain independently checked cover upper witnesses. The five `audit_*.json` files and `template_audit.json` give the table counts in the report.

The remaining scan, probe, template, and revisit files document discovery. Their selection is not an exhaustive classification of all BB codes. Many cover parameter sets are equivalent; counts are instances, not inequivalent codes.

## Historical search version

`search_before_packing.cpp` retains the engine before the odd-row packing lower bound was added. Initial batches 9301 through 9304 used that pruning level; batch 9305 and the final certifications used the final engine. Re-running a capped discovery scan with stronger pruning can change which cases hit its node budget. This does not change the validity of its retained explicit witnesses or of final cutoff-free certificates.

For reproducing an old capped discovery run, compile the retained version and select it with `BB_EXECUTABLE`:

```sh
g++ -O3 -std=c++17 search_before_packing.cpp -o search_discovery
BB_EXECUTABLE="$PWD/search_discovery" python scan.py 9301 2500
```

The final audit path does not depend on reproducing discovery cutoffs or timings.

## Baseline source

The attached continuation brief supplies the established infinite 7/3 family, special-case bounds, and the O(N^(3/4)) size-dependent bound. The published cover convention is Theorem 3.1 of Symons, Rajput, and Browne, *Sequences of Bivariate Bicycle Codes from Covering Graphs*, arXiv:2511.13560v3. The report does not attribute this project's 7/3 family to that paper.
