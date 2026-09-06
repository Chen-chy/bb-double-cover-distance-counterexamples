# Failed approaches, exact negative controls, and what they do not refute

These results are part of the research, not discarded clutter. The links lead
to the preserved proof, certificate, or conversation source. None of the items
below proves a ratio above three for the full finite BB distance.

| Proposed inference or shortcut | Recorded obstruction | Exact scope and evidence |
|---|---|---|
| A minimum base logical survives transfer | The seed's light class transfers to a boundary | Finite membership checks in [round 03](../research/03_amplification_search/README.md); repeated-root normal form in history |
| Large mu/d or lambda_k/d forces distance amplification | A=1+x+x^2, B=A^2, L=3q odd has d=d_2=4, k=k_2=4, mu=lambda_3=lambda_4=q+1 | Uniform symbolic family; [history and recovered trellis](../history/02_distance4_and_transfer_metric.md) |
| Infinite-strip nonboundary automatically survives finite period | The weight-12 epsilon multiple of the strip base word is universally nontrivial but becomes a boundary at the selected periods | [Initial proof history](../history/01_initial_family_and_baseline.md) |
| A primitive gcd/cofactor word gives quantum distance | (B,A) is always a BB boundary; divided generators can be nonminimum | Baseline and all later exact representative formulas |
| Raw exponent growth makes growing interaction scale | The 7/3 family is permutation-equivalent to a fixed-range strip | [History 01](../history/01_initial_family_and_baseline.md) |
| Frobenius squaring of a base cycle proves factor three | (Au^2,Bv^2) can be homologous to a killed transfer | Explicit identity in [history](../history/01_initial_family_and_baseline.md); not a counterexample to factor three |
| Ordinary distance of the split reduced code is <= base distance | Base [[78,4,6]] gives reduced [[78,4,9]] | Exact finite lower/upper certificates and independent meet-in-the-middle exclusion in [round 03 §4](../research/03_amplification_search/REPORT.md); reduced B has four terms |
| Universal homology tensoring proves survival | The non-BB pair (g,g(1+c)) and its epsilon deformation lose all compact cover classes at g=c=0 while finite homology remains | Symbolic specialization/Tor negative control in [round 05 §2](../research/05_compact_survival/REPORT.md) |
| The old power generator's weight is the compact minimum | Subgroup norm replacement shrinks it; e.g. weights 54 versus true compact 24 in a case with base compact 16 | Exact shortest-generator theorem in [round 06](../research/06_linear_compact_replacement/REPORT.md) |
| A generic kernel-distance proof can use arbitrary finite-field coefficients | A finite-field specialization gives distance 6 where the transcendental kernel distance is 9 | Classical, not quantum, negative control in [round 06](../research/06_linear_compact_replacement/odd_resonance_negative_control.json) |
| Purify universal homology sectors before optimizing with negligible cost | Record base minimum 6 becomes resonance-pure 12; complement minimum 10 | Exact arbitrary-support closure certificates in [round 08](../research/08_slope21_shortening/exact_results.json) |
| A killed universal component cannot help a surviving representative | Full cover compact minimum 14 is strictly below resonance-pure cover minimum 16 | Same complete certificates; 16 is not actual cover distance |
| Minimize completion cost kappa first, then projected weight | Complete Pareto frontier is {(12,1),(14,0)} | [Round 09 Pareto proof](../research/09_joint_completion/pareto_verification.json); zero-cost completion breaks the projection cap 12 |
| Circuit support, strict single-stabilizer stability, and local majority imply factor three | Explicit weight-182 boundary circuit gives restricted optimized output 550>546 | [Round 09 §6](../research/09_joint_completion/REPORT.md); it is a boundary, not a minimum logical |
| The tree-conflict problem is bipartite because the original graph is | A genuine common-message input produces a triangle after contraction | [Round 10 triangle certificate](../research/10_nonlocal_exchange/triangle_certificate.json) and independent auditor |
| Optimal h at a fixed message plus global base minimality implies a short cover word | Fixed-message minima 74N, N positive odd, occur in one universal class of minimum 14 | [Round 10 §7](../research/10_nonlocal_exchange/REPORT.md), Bellman certificate, explicit universal boundary, and separator proof |
| Removing a large source-free tree automatically shortens the minimum base word | The direct tree boundary has weight 26 and changes a minimum weight-6 word to weight 26 | Exact polynomial identity in the [fixed-message audit](../research/10_nonlocal_exchange/fixed_message_audit.json) |

## Search failures are not mathematical negative results

Round 03 keeps capped discovery searches and partial d=8 follow-ups. A returned
witness supplies an upper bound. A stopped search with no witness supplies no
lower bound. No historical timeout was converted into a distance claim during
export. The full run status and cutoff flags remain in the source data.

Some early six-column heuristic samples were formal circuits but not finite
logical certificates. Later exhaustive classification explicitly filters sums
of two or three boundaries, not merely single cofactor boundaries. That
correction is preserved in the distance-six report and its algebraic certificates.

## Why these failures are still useful

They progressively narrow the missing argument: it must optimize over actual
finite cover logicals or the justified full compact image; retain all message and
boundary variables; respect specialization; and use genuine global base
minimality, not only local support conditions. The latest tree-packing reduction
is exact, but fixed-message tree cost alone has been conclusively separated from
the minimum over a universal class.
