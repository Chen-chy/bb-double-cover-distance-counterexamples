# Claim ledger

The labels below describe evidence recorded by the research. They do not turn
export-time test success into an independent proof review. Hypotheses and
limitations remain in the linked original report. Historical bounds are kept
with `current=false` in the machine-readable ledger.

Machine-readable index: [claim_ledger.json](../provenance/claim_ledger.json).

## BASE-01 — Connected uniform family [[252j+78,4,6]] -> [[504j+156,4,14]], j>=0; record ratio 7/3

**Evidence:** conversation-derived uniform proof plus certified seed. **Scope:** Unchanged polynomials, univariate cyclic double cover.

**Source:** [history/01_initial_family_and_baseline.md](../history/01_initial_family_and_baseline.md), section 1.

**Data/programs:** [research/03_amplification_search/search_verification.json](../research/03_amplification_search/search_verification.json), [research/03_amplification_search/independent_exclusions.json](../research/03_amplification_search/independent_exclusions.json).

**Limit:** Original early full archive/fixed-box logs unavailable; finite seed has intact later verification.

## BASE-02 — k<=k2<=2k; ranks of transfer and projection are k2/2; k2=2k implies d2<=2d

**Evidence:** inherited symbolic baseline. **Scope:** Binary BB double covers.

**Source:** [history/01_initial_family_and_baseline.md](../history/01_initial_family_and_baseline.md), section 3.

**Limit:** Not a metric theorem for a killed chosen class.

## BASE-03 — d=2 implies d2<=4

**Evidence:** inherited symbolic baseline. **Scope:** Weight-six BB double covers.

**Source:** [history/01_initial_family_and_baseline.md](../history/01_initial_family_and_baseline.md), section 3.

**Limit:** Original full early report is unavailable; downstream reports identify this as input.

## D4-01 — d=4 implies d2<=48

**Evidence:** uniform computer-assisted; recovered-source provenance. **Scope:** All stated term-matched weight-six covers.

**Source:** [history/02_distance4_and_transfer_metric.md](../history/02_distance4_and_transfer_metric.md), section 2-4.

**Data/programs:** [history/recovered_round2/verify4_independent.py](../history/recovered_round2/verify4_independent.py), [history/recovered_round2/verify_weight_four_sympy.py](../history/recovered_round2/verify_weight_four_sympy.py).

**Limit:** Recovered text is not authenticated original source bytes; not an optimality claim.

## METRIC-01 — For A=1+x+x^2, B=A^2, L=3q, q>=3 odd: d=d2=4, k=k2=4, mu=lambda3=lambda4=q+1

**Evidence:** symbolic exact family; recovered finite checker. **Scope:** Transfer-sector metric, not amplification.

**Source:** [history/02_distance4_and_transfer_metric.md](../history/02_distance4_and_transfer_metric.md), section 6.

**Data/programs:** [history/recovered_round2/verify_metric_family.py](../history/recovered_round2/verify_metric_family.py).

## R3-01 — Univariate one-block restricted distance doubles or does not increase according to the support-lift gcd dichotomy; a one-block logical w gives d2<=2w

**Evidence:** symbolic proof. **Scope:** Univariate strict-trinomial term-matched doubles.

**Source:** [research/03_amplification_search/REPORT.md](../research/03_amplification_search/REPORT.md), section 2.

**Data/programs:** [research/03_amplification_search/verify_theorems.py](../research/03_amplification_search/verify_theorems.py).

**Limit:** Does not imply factor two for mixed-block minima.

## R3-02 — Full split-cover homology reduces to (P^2,Q+delta P) with exact physical W_delta

**Evidence:** symbolic exact reduction. **Scope:** Split group extensions.

**Source:** [research/03_amplification_search/REPORT.md](../research/03_amplification_search/REPORT.md), section 3.

**Data/programs:** [research/03_amplification_search/theorem_checks.json](../research/03_amplification_search/theorem_checks.json).

**Limit:** Ordinary reduced Hamming distance is not physical cover distance.

## R3-03 — A [[78,4,6]] base has auxiliary reduced code [[78,4,9]]

**Evidence:** exact finite counterexample to an intermediate lemma. **Scope:** Auxiliary reduced code, not a strict-trinomial BB cover.

**Source:** [research/03_amplification_search/REPORT.md](../research/03_amplification_search/REPORT.md), section 4.

**Data/programs:** [research/03_amplification_search/reduced_code_mitm.json](../research/03_amplification_search/reduced_code_mitm.json), [research/03_amplification_search/mitm.cpp](../research/03_amplification_search/mitm.cpp), [research/03_amplification_search/independent_search.py](../research/03_amplification_search/independent_search.py).

## SEARCH-01 — 16,384 selected distance-four/six cover instances certified within 7/3

**Evidence:** retained exact finite audits on selected corpus. **Scope:** Parameter instances; no exhaustive coverage of BB class.

**Source:** [research/03_amplification_search/REPORT.md](../research/03_amplification_search/REPORT.md), section 5.1.

**Data/programs:** [research/03_amplification_search/final_verification_summary.json](../research/03_amplification_search/final_verification_summary.json).

**Limit:** Cover witnesses are upper bounds, not exact cover distances in every row.

## SEARCH-02 — 2,800 distance-eight instances; 1,020 unresolved at 7/3

**Evidence:** partial discovery with exact certified subset. **Scope:** Capped searches remain unresolved.

**Source:** [research/03_amplification_search/REPORT.md](../research/03_amplification_search/REPORT.md), section 5.2.

**Data/programs:** [research/03_amplification_search/RESULTS.json](../research/03_amplification_search/RESULTS.json).

**Limit:** No failed search is a lower exclusion.

## D6-01 — d=6 implies d2<=112; remaining higher-rank mixed mechanisms give d2<=12

**Evidence:** uniform computer-assisted. **Scope:** Finite abelian term-matched strict-trinomial covers.

**Source:** [research/04_distance6_obstruction/REPORT.md](../research/04_distance6_obstruction/REPORT.md), section 5-6.

**Data/programs:** [research/04_distance6_obstruction/verify6_all_pairings.cpp](../research/04_distance6_obstruction/verify6_all_pairings.cpp), [research/04_distance6_obstruction/highrank6_certificates.json](../research/04_distance6_obstruction/highrank6_certificates.json), [research/04_distance6_obstruction/verify_presentations_sympy.py](../research/04_distance6_obstruction/verify_presentations_sympy.py).

**Limit:** Full enumeration not rerun during export; retained full-matrix check rerun.

## D6-02 — Matched Frobenius powers with a nontrivial canonical base cycle give a bounded cover logical; odd-subgroup descent preserves relevant nontriviality

**Evidence:** symbolic proof. **Scope:** Power-cycle and odd-invariant mechanisms.

**Source:** [research/04_distance6_obstruction/REPORT.md](../research/04_distance6_obstruction/REPORT.md), section 2-3.

**Data/programs:** [research/04_distance6_obstruction/frobenius_verification.json](../research/04_distance6_obstruction/frobenius_verification.json).

**Limit:** Power equality alone is not a nonboundary certificate.

## ONEBLOCK-01 — A one-block logical of weight w gives d2<=2w^2

**Evidence:** symbolic proof. **Scope:** Finite abelian BB covers.

**Source:** [research/04_distance6_obstruction/REPORT.md](../research/04_distance6_obstruction/REPORT.md), section 4.3.

## COMPACT-01 — Genuinely higher-rank compact survival holds at all circuit weights through a torsion–Frobenius cyclic module

**Evidence:** symbolic proof with supplementary checks. **Scope:** Four check differences generate U; free rank>=2; neither check in a finite subgroup.

**Source:** [research/05_compact_survival/REPORT.md](../research/05_compact_survival/REPORT.md), section 3-6.

**Data/programs:** [research/05_compact_survival/finite_cover_certificates.json](../research/05_compact_survival/finite_cover_certificates.json), [research/05_compact_survival/audit_finite_certificates.py](../research/05_compact_survival/audit_finite_certificates.py).

**Limit:** Not an unrestricted homology base-change theorem.

## COMPACT-02 — General d2<=2d^4 and refined subquartic bounds

**Evidence:** symbolic corollaries with inherited and geometric dependencies. **Scope:** All stated strict-trinomial covers.

**Source:** [research/05_compact_survival/REPORT.md](../research/05_compact_survival/REPORT.md), section 7-9.

**Limit:** Historical bound; later cubic bound is stronger asymptotically.

This is a preserved historical bound, not the latest best statement.

## GLOBAL-01 — d2<=32d^3

**Evidence:** symbolic corollary with external geometric dependency. **Scope:** General stated strict-trinomial BB double-cover class.

**Source:** [research/06_linear_compact_replacement/REPORT.md](../research/06_linear_compact_replacement/REPORT.md), section 7.

**Limit:** Polynomial in d, not a finite universal amplification constant.

## GLOBAL-02 — Gamma(N)<=24 sqrt(N)

**Evidence:** symbolic corollary with external geometric dependency. **Scope:** N is base physical length.

**Source:** [research/05_compact_survival/REPORT.md](../research/05_compact_survival/REPORT.md), section 9.

**Limit:** Size-dependent; does not prove C_* finite.

## PATHOLOGY-01 — A non-BB square-zero deformation loses every compact cover class under specialization while finite H1 remains

**Evidence:** explicit symbolic negative control. **Scope:** Outside BB trinomial hypotheses.

**Source:** [research/05_compact_survival/REPORT.md](../research/05_compact_survival/REPORT.md), section 2.

**Data/programs:** [research/05_compact_survival/mechanism_verification.json](../research/05_compact_survival/mechanism_verification.json).

## LINEAR-01 — Compact minimum o*2^(a-b)*3^b*(3^s+1); cover ratios exactly 1,3/2,2

**Evidence:** symbolic exact theorem. **Scope:** Torsion–Frobenius normal form with surviving compact image.

**Source:** [research/06_linear_compact_replacement/REPORT.md](../research/06_linear_compact_replacement/REPORT.md), section 2-5.

**Data/programs:** [research/06_linear_compact_replacement/sparse_generator_checks.json](../research/06_linear_compact_replacement/sparse_generator_checks.json), [research/06_linear_compact_replacement/embedding_checks.json](../research/06_linear_compact_replacement/embedding_checks.json).

**Limit:** Universal support weight, not an unqualified statement about every finite logical.

## LINEAR-02 — [[18,4,2]] -> [[36,4,4]] realizes compact factor-two sharpness

**Evidence:** exact finite example. **Scope:** Specific matched cover.

**Source:** [research/06_linear_compact_replacement/REPORT.md](../research/06_linear_compact_replacement/REPORT.md), section 6.1.

**Data/programs:** [research/06_linear_compact_replacement/sharpness_example.json](../research/06_linear_compact_replacement/sharpness_example.json), [research/06_linear_compact_replacement/verify_sharpness.py](../research/06_linear_compact_replacement/verify_sharpness.py).

## RANK1-01 — Exact cyclic universal module and compact specialization sequence retain the winding/Tor sector

**Evidence:** symbolic exact module calculation. **Scope:** Primitive rank-one Laurent setting, stated square-free gcd hypotheses.

**Source:** [research/07_rank_one_resonance/REPORT.md](../research/07_rank_one_resonance/REPORT.md), section 2.

**Data/programs:** [research/07_rank_one_resonance/structure_certificates.json](../research/07_rank_one_resonance/structure_certificates.json).

## RANK1-02 — One-sided defects and most two-sided parity patterns satisfy compact factor two

**Evidence:** symbolic proof. **Scope:** Primitive rank-one setting; finite nonboundary tests explicit.

**Source:** [research/07_rank_one_resonance/REPORT.md](../research/07_rank_one_resonance/REPORT.md), section 3-4.

**Data/programs:** [research/07_rank_one_resonance/lift_certificates.json](../research/07_rank_one_resonance/lift_certificates.json).

## RANK1-03 — Remaining odd-order resonance has fixed-slope bound 2m, m=max(|p|,|q|,|p-q|)

**Evidence:** symbolic constructive bound. **Scope:** Coprime primitive resonance slopes.

**Source:** [research/07_rank_one_resonance/REPORT.md](../research/07_rank_one_resonance/REPORT.md), section 5.

**Data/programs:** [research/07_rank_one_resonance/divided_euler_cases.json](../research/07_rank_one_resonance/divided_euler_cases.json).

**Limit:** m is not universally bounded; slope (2,1) gives factor four.

## RANK1-04 — Along compatible long periods, actual finite distances equal full compact minima

**Evidence:** symbolic large-period realization. **Scope:** Fixed Laurent data and stable root divisors, explicit no-winding threshold.

**Source:** [research/07_rank_one_resonance/REPORT.md](../research/07_rank_one_resonance/REPORT.md), section 7.

**Limit:** Cannot be applied to restricted-sector or fixed-message minima.

## S21-01 — Delta<=Delta_e<=2Delta and exact projection/completion formula

**Evidence:** symbolic exact reduction. **Scope:** Slope (2,1) hard-core compact setting.

**Source:** [research/08_slope21_shortening/REPORT.md](../research/08_slope21_shortening/REPORT.md), section 2-4.

**Data/programs:** [research/08_slope21_shortening/structure_verification.json](../research/08_slope21_shortening/structure_verification.json).

## S21-02 — Exact base full/pure/complement minima 6/12/10; cover full/pure minima 14/16

**Evidence:** exact arbitrary-support compact minima. **Scope:** The explicitly gauged record example.

**Source:** [research/08_slope21_shortening/REPORT.md](../research/08_slope21_shortening/REPORT.md), section 5-6.

**Data/programs:** [research/08_slope21_shortening/exact_results.json](../research/08_slope21_shortening/exact_results.json), [research/08_slope21_shortening/audit_certificates.py](../research/08_slope21_shortening/audit_certificates.py).

**Limit:** 12,10,16 are restricted minima, not new finite BB distances.

## GRAPH-01 — Full compact energy is a common-message signed graph; half of the boundary spins eliminate exactly by majority

**Evidence:** symbolic exact reduction. **Scope:** Universal slope-(2,1) graph, all messages and boundaries retained.

**Source:** [research/09_joint_completion/REPORT.md](../research/09_joint_completion/REPORT.md), section 2-4.

**Data/programs:** [research/09_joint_completion/graph_verification.json](../research/09_joint_completion/graph_verification.json).

**Limit:** Alternating local updates are not claimed globally optimal.

## GRAPH-02 — Minimum-support optimal components satisfy b1<=number of sources, with a fixed-message support bound

**Evidence:** symbolic proof. **Scope:** Fixed message; no bound on message support.

**Source:** [research/09_joint_completion/REPORT.md](../research/09_joint_completion/REPORT.md), section 5.

**Data/programs:** [research/09_joint_completion/component_verification.json](../research/09_joint_completion/component_verification.json).

## PARETO-01 — Complete projected-weight/completion frontier {(12,1),(14,0)}

**Evidence:** exact Pareto theorem with inherited closure certificates. **Scope:** Record example.

**Source:** [research/09_joint_completion/REPORT.md](../research/09_joint_completion/REPORT.md), section 7.

**Data/programs:** [research/09_joint_completion/pareto_verification.json](../research/09_joint_completion/pareto_verification.json), [research/09_joint_completion/verify_pareto.py](../research/09_joint_completion/verify_pareto.py).

## MAJORITY-01 — Weight-182 locally stable circuit boundary gives restricted output 550>546

**Evidence:** exact counterexample to a restricted majority assertion. **Scope:** Input is explicitly a boundary.

**Source:** [research/09_joint_completion/REPORT.md](../research/09_joint_completion/REPORT.md), section 6.

**Data/programs:** [research/09_joint_completion/majority_control_verification.json](../research/09_joint_completion/majority_control_verification.json).

**Limit:** Not a counterexample for a minimum nonboundary or full cover distance.

## TREE-01 — Two local equations exactly characterize common-message data

**Evidence:** symbolic exact characterization. **Scope:** Laurent PID slope-(2,1) setting.

**Source:** [research/10_nonlocal_exchange/REPORT.md](../research/10_nonlocal_exchange/REPORT.md), section 2.

**Data/programs:** [research/10_nonlocal_exchange/identity_verification.json](../research/10_nonlocal_exchange/identity_verification.json).

## TREE-02 — Canonical nonsource trees contract to all-or-nothing two-unit rewards; full fixed-message field optimum is independent-set packing

**Evidence:** symbolic exact reduction. **Scope:** All source assignments and boundary fields, fixed common-message input.

**Source:** [research/10_nonlocal_exchange/REPORT.md](../research/10_nonlocal_exchange/REPORT.md), section 3-5.

**Data/programs:** [research/10_nonlocal_exchange/forest_verification.json](../research/10_nonlocal_exchange/forest_verification.json), [research/10_nonlocal_exchange/tree_contraction_verification.json](../research/10_nonlocal_exchange/tree_contraction_verification.json).

## TREE-03 — A genuine compact message produces a triangular conflict graph

**Evidence:** exact constructive negative control. **Scope:** Not a minimum-distance assertion.

**Source:** [research/10_nonlocal_exchange/REPORT.md](../research/10_nonlocal_exchange/REPORT.md), section 6.

**Data/programs:** [research/10_nonlocal_exchange/triangle_certificate.json](../research/10_nonlocal_exchange/triangle_certificate.json), [research/10_nonlocal_exchange/audit_triangle.py](../research/10_nonlocal_exchange/audit_triangle.py).

## TREE-04 — Fixed-message minimum 74 with support 15; same universal class has full minimum 14

**Evidence:** exact conditional minimum plus unrestricted inherited certificate. **Scope:** One explicit message in the record code.

**Source:** [research/10_nonlocal_exchange/REPORT.md](../research/10_nonlocal_exchange/REPORT.md), section 7.2-7.3.

**Data/programs:** [research/10_nonlocal_exchange/fixed_message_certificate.json](../research/10_nonlocal_exchange/fixed_message_certificate.json), [research/10_nonlocal_exchange/fixed_message_potential.bin](../research/10_nonlocal_exchange/fixed_message_potential.bin), [research/10_nonlocal_exchange/audit_fixed_certificate.py](../research/10_nonlocal_exchange/audit_fixed_certificate.py).

**Limit:** 74 is not code distance; explicit boundary to 14 retained.

## TREE-05 — For positive odd N, conditional minimum 74N and support 15N in one universal class of minimum 14

**Evidence:** symbolic parametric negative control. **Scope:** Separated messages in one fixed code.

**Source:** [research/10_nonlocal_exchange/REPORT.md](../research/10_nonlocal_exchange/REPORT.md), section 7.4.

**Data/programs:** [research/10_nonlocal_exchange/parametric_verification.json](../research/10_nonlocal_exchange/parametric_verification.json).

**Limit:** Not an increasing-distance family.

## OPEN-01 — Full slope-(2,1) hat-Delta<=3Delta

**Evidence:** open conjecture. **Scope:** All admissible compact messages and all boundary adjustments.

**Source:** [research/10_nonlocal_exchange/REPORT.md](../research/10_nonlocal_exchange/REPORT.md), section 9.

**Limit:** Neither proved nor refuted; inherited bound is four.

## OPEN-02 — Half-weight completion after a minimum base class and boundary adjustment

**Evidence:** open sufficient lemma. **Scope:** Stronger class-pinned statement.

**Source:** [research/09_joint_completion/REPORT.md](../research/09_joint_completion/REPORT.md), section 8.

**Limit:** Failure would not by itself refute OPEN-01.

## OPEN-03 — Finiteness or infiniteness of C_*

**Evidence:** open problem. **Scope:** Entire stated strict-trinomial BB double-cover class.

**Source:** [docs/OPEN_PROBLEMS.md](../docs/OPEN_PROBLEMS.md), section 5.

**Limit:** No numerical universal linear upper bound and no unbounded-ratio family established.
