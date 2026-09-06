# Evidence taxonomy and certificate map

The source reports distinguish proof type, and this export preserves that
distinction. A file hash authenticates archived bytes, not a mathematical claim.
A passing program checks what it implements, not every theorem in its report.
“Independent implementation” here means separately written algorithms/arithmetic;
it is not independent human peer review.

## Evidence classes

**Symbolic proof:** a uniform argument in a report, with stated hypotheses and
possibly supplementary finite checks. Examples are the compact-survival theorem,
exact higher-rank compact metric, rank-one derivative constructions, and tree
packing reduction.

**Uniform computer-assisted proof:** a symbolic reduction to a completely
specified finite enumeration, with source and outputs. Examples are the d=4
(recovered-source provenance) and d=6 incidence classifications. Finite input
coverage, filters, and algebraic certificate semantics are part of the proof.

**Exact finite minimum:** an attaining nonboundary and complete lower exclusion
for the same optimization domain. Some are actual quantum distances; some are
restricted or conditional compact minima. The domain must always accompany the
number.

**Witness-only certificate:** a cycle and a separating dual prove nonboundary
and an upper bound. They do not establish that no smaller logical exists.

**Negative control/disproved shortcut:** an exact example violates a proposed
intermediate statement. It refutes only that statement. Several important
controls are boundaries or non-BB auxiliary complexes.

**Heuristic/discovery record:** selection, cutoffs, or a partial scan. Retain the
raw flags. Lack of a witness before a cutoff is not a lower bound.

## Main certificate pathways

| Claim/domain | Data and generator | Auditor and proof semantics |
|---|---|---|
| Seed [[78,4,6]] -> [[156,4,14]] | Round 03 `search_verification.json`; `search.cpp` | `verify_search.py` gives finite upper/lower checks; `independent_search.py` uses a separate Bezout oracle |
| Reduced non-BB [[78,4,9]] | Round 03 `search_verification.json`, `reduced_code_mitm.json`; `search_general.cpp`, `mitm.cpp` | Independent subset enumeration excludes all nonboundaries through eight; not a new BB cover ratio |
| Broad finite search corpus | Round 03 `base_certificates_*.json`, `audited_*.jsonl.gz`, scan/probe/revisit files | `audit_batch.py` reconstructs base exclusions and upper witnesses; cutoff flags remain unresolved |
| d=4 uniform classification | Conversation source plus `history/recovered_round2/` | Two transcribed algorithms, 10,044 direct pairings and 2,016 normalized checks; original source hashes absent |
| d=6 uniform classification | Round 04 `graphs6.*`, `retained6.json`, `highrank6_certificates.json` | Two exhaustive C++ enumerations; `verify_presentations_sympy.py` independently reconstructs 684 full incidence matrices |
| Compact-survival finite checks | Round 05 `finite_cover_certificates.json` | `audit_finite_certificates.py` verifies 1,056 primal/dual certificates; no distance lower claim |
| Exact higher-rank compact metric | Round 06 symbolic proof, sparse-generator and generic-evaluation records | `verify_sparse_generators.py`, `verify_embeddings.py`; finite logical audit is supplementary |
| Finite replacement witnesses | Round 06 `finite_replacement_certificates.json` | `audit_replacement_certificates.py` checks 2,322 primal/dual certificates, ranks, matches, and norms |
| Rank-one constructions | Round 07 `*_certificates.json`, `*_cases.json` | `audit_certificates.py` reconstructs finite groups and dual separation independently |
| Compact minima 6,12,10,14,16 | Round 08 `exact_results.json`, five `certificates/*.bin`; `trellis_exact.cpp` | `audit_certificates.py` checks a finite sublevel set is closed under **all** transitions and contains no forbidden accepting state; covers arbitrary finite Laurent length |
| Complete frontier {(12,1),(14,0)} | Round 09 `pareto_verification.json` plus inherited closure files | `verify_pareto.py` re-audits the needed lower certificates and both attaining constructions |
| Local-majority negative control | Round 09 `majority_control_verification.json` | `verify_majority_control.py` confirms circuit rank, strict one-flip stability, and explicit boundary multiplier |
| Non-bipartite conflict graph | Round 10 `triangle_certificate.json` | `audit_triangle.py` independently verifies the common-message and edge conditions; no distance minimum claim |
| Fixed-message minimum 74, support 15 | Round 10 `fixed_message_certificate.json`, `fixed_message_potential.bin` | `audit_fixed_certificate.py` checks all 358,400 Bellman lower inequalities and an attaining path; anchor theorem covers all finite fields |
| Same universal class minimum 14 | Round 10 explicit boundary and inherited full compact lower file | Exact boundary identity plus the original unrestricted compact certificate |
| Conditional 74N family | Round 10 report §7.4 and `parametric_verification.json` | Symbolic separators and same-class congruence; not a growing-distance family |

All paths above refer to a materialized round. Canonical storage links for
inherited duplicates appear in [FILE_INDEX.md](FILE_INDEX.md).

## Binary certificates are research data

Round 08's `.bin` files are sorted state/cost closure tables, not executables.
The accompanying auditor validates headers, hashes, transition semantics,
acceptance labels, and attaining words. Round 10's `.bin` is a lower Bellman
potential; an inequality check, not trust in a shortest-path generator, supplies
the lower bound. Both types are retained and tracked as binary files. They must
not be deleted as ordinary build products or converted through text tools.

## Export-time coverage versus original runs

The [export log](../checks/export_2026-09-06/README.md) lists the commands actually
rerun. It includes the finite seed/reduced-code checks, full-matrix d=6 retained
certificate check, symbolic test instances, independent finite dual audits,
all five compact closure minima, Pareto audits, and the latest retained audits.
The broad scans, full d=6 enumeration, full finite witness generators, and old
random discovery scripts were not rerun just to package the archive. Their
original sources and outputs are retained, and full reproduction commands are
provided. This difference is explicit rather than hidden in “all verified”.
