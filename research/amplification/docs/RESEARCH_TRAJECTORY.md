# Research trajectory and dependency map

This is a reading order, not a claim that every intermediate snapshot was
originally assigned these numeric directory names. Round labels 03–10 identify
the eight intact archived bundles. Early reports survive as conversation-derived
material. Older “next target” sections are historical, not the current agenda.

## 1. Seed, repeated roots, and the first failed transfer route

The initial question concerned asymptotic amplification, not just the original
factor-two conjecture. The seed A=1+x^8+x^25, B=1+x^2+x^13 gave 6->14 after exact
finite checks. Its connected parametric family was recognized as a fixed-range
strip under a cyclic automorphism; raw exponent growth did not produce growing
cover distance. Gcd/Bezout homology formulas explained how transfer could kill
one entire logical sector.

The early no-winding and finite-specialization arguments are preserved in
[History 01](../history/01_initial_family_and_baseline.md). Some original logs
are unavailable, but the finite seed was subsequently independently rechecked
in round 03.

## 2. Fixed distance four and the transfer-metric counterexample

Small support forced finitely many abelian incidence mechanisms, yielding
`d=4 => d_2<=48`. A one-block circuit gave a finite subgroup bound. In parallel,
A=1+x+x^2, B=A^2 at L=3q, q odd, gave d=d_2=4 but mu=q+1 and
lambda_3=lambda_4=q+1. This invalidated using only expensive surviving transfer
sectors as evidence for distance amplification.

The [proof transcription](../history/02_distance4_and_transfer_metric.md) and
[recovered verifier source](../history/recovered_round2/README.md) preserve this
stage. The original ZIP, hashes, and raw sampled six-column outputs are absent.

## 3. Full split-cover reduction and broad exact searches

[Round 03](../research/03_amplification_search/REPORT.md) proves the univariate
one-block factor-two theorem and reduces the full split-cover homology to a
half-size code with an exact physical norm W_delta. The tempting ordinary
reduced-distance comparison fails: a [[78,4,6]] base gives a reduced [[78,4,9]]
code. The reduced check is not a strict-trinomial cover and is not an amplification
record.

Completed d=4,6 scans certify 16,384 parameter instances within the 7/3 threshold.
The d=8 corpus has 2,800 instances, 1,020 unresolved at that threshold. Cutoff
records are explicitly retained as unresolved; witness-only results are upper
bounds. Historical search code before the packing prune is preserved because
rerunning capped scans with the new engine can change which cases hit a cutoff.

## 4. All mixed weight-six mechanisms are bounded

[Round 04](../research/04_distance6_obstruction/REPORT.md) exhausts the six-column
incidence presentations, using two enumeration methods and a third full-matrix
arithmetic audit. Higher-rank possibilities reduce to matched powers or odd-
subgroup descent, or are excluded as units/boundaries/smaller logicals. The
uniform result is d=6 => d_2<=112. The larger constant comes from low-rank size
and strip bounds; surviving higher-rank mechanisms give at most twelve.

The next question became compact survival rather than simply enumeration at
weight eight.

## 5. Compact survival at arbitrary weight

[Round 05](../research/05_compact_survival/REPORT.md) gives noncollinear Laurent
trinomial rigidity, a torsion–Frobenius normal form, a cyclic universal compact
H_1 module, and a finite nonboundary argument. This resolves the specified
higher-rank compact-survival problem at all weights. It also gives polynomial
f(d) bounds and a square-root Gamma(N) bound.

An explicit square-zero Koszul example outside the BB hypotheses shows why
Noetherianity or tensoring universal H_1 is not enough: every compact cover class
can specialize to zero while finite homology is newly created.

## 6. Exact higher-rank compact metric: factor two, not merely three

[Round 06](../research/06_linear_compact_replacement/REPORT.md) proves the exact
compact minimum and constructs a shortest generator of the whole compact module.
Two faithful generic evaluations supply lower bounds for every representative.
The possible compact cover ratios are 1, 3/2, 2. A subgroup norm shortens the old
power generator; its apparently superlinear cost was a representative artifact.
The global polynomial bound improves to d_2<=32d^3. Low-rank and finite-check
linear control remains separate.

## 7. Rank-one cancellation and finite realization

[Round 07](../research/07_rank_one_resonance/REPORT.md) proves derivative lifts
for one-sided and most two-sided defects, reduces the remainder to odd-order
cyclotomic resonance, and gives factor 2m for fixed primitive slope. It supplies
an exact all-message/all-boundary encoder and an exact sequence retaining the
specialization-created sector.

The large-period realization theorem is strategically important: a violation
by the *full* compact minimum produces actual finite-distance violations along
compatible long periods. Expensive fixed generators are still insufficient.

## 8. Slope (2,1): sector-first purification loses the cancellation

[Round 08](../research/08_slope21_shortening/REPORT.md) uses the two-binomial and
unit Bezout identities to construct sparse homology projectors. Their factor-two
purification cost is sharp. Exact arbitrary-support closure certificates give
base full/pure/complement minima 6/12/10 and cover full/pure minima 14/16.
The killed universal component is necessary in a minimum cover representative.
The joint projection/completion formula retains it rather than choosing sectors
first.

## 9. Full signed-graph formulation and joint frontier

[Round 09](../research/09_joint_completion/REPORT.md) parameterizes every compact
cover cycle by a message phi and boundary h. The physical weight becomes a
signed-cut energy with common-message constraints; half of h can be eliminated
exactly by independent odd-vertex majority. This is an exact partial minimization,
not a greedy optimality heuristic.

The complete record Pareto frontier is {(12,1),(14,0)}. A separate weight-182
circuit, stable under every single stabilizer flip, defeats a restricted majority
construction (550>546), but it is an explicitly exhibited boundary. Global
nonboundary minimality cannot be replaced by circuit/local stability tests.

## 10. Nonlocal exchanges and the current unresolved coupling

[Round 10](../research/10_nonlocal_exchange/REPORT.md) completes the common-message
constraints with a second local equation. At fixed message/source spins, every
occupied nonsource component is a canonical tree, each giving an all-or-nothing
two-unit improvement. The full source-free field minimum is an independent-set
problem on compatible trees. A genuine message yields a triangular conflict
graph, ruling out a bipartite matching shortcut.

The conditional 74N family has optimal fixed-message fields but remains in a
universal class of minimum fourteen. An explicit boundary connects the shown
74-word to a 14-word. Tree size/cost at fixed phi cannot contradict base
minimality by itself. The unresolved step must combine message-changing cover
exchanges with the full nonlocal inequalities supplied by a globally minimum
base class.

The [current packing-deficit target](OPEN_PROBLEMS.md) is the endpoint of this
trajectory. No new mathematical research was undertaken in assembling it.
