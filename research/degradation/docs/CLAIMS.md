# Claim register and evidence types

This register preserves the status and scope of the source claims; it is not a new referee decision. “Proof supplied” means the archived note contains a symbolic argument. “Exact check” of a displayed witness or identity is not synonymous with an exact minimum-distance certificate. Uniform computer-assisted exclusions require both the symbolic completeness argument and their enumeration records. Original proofs take precedence over this navigation summary.

| Label | Meaning |
|---|---|
| `symbolic-proof-and-exact-checks` | Uniform proof in a supplied note, with separate finite identity or witness checks. |
| `computer-assisted-theorem` | Uniform statement with a finite exhaustive classification and independent arithmetic certificates. |
| `exact-minimum-certificate` | Retained all-degree lower-bound certificate plus attaining words for a specific complete optimization. |
| `symbolic-plus-exact-minimum-certificate` | Parametric conclusion combines a uniform proof with a retained exact minimum certificate. |
| `symbolic-exact-small-minimum` | Specific minimum established in the source by a short symbolic exclusion argument. |
| `disproved-approach` | A proposed shortcut is refuted; its scope is not automatically the main conjecture. |
| `exact-inadmissible-counterfamily` | Exact result outside the target cover hypotheses, kept as a negative control. |
| `reported-proof-only` | Public proof/derivation retained, but its linked original source package is unavailable. |
| `inherited-input` / `inherited-branch-assertion` | Claim supplied from an earlier or other branch; its original certificate is not present. |
| `open` | Unproved and unrefuted in this archive unless explicitly qualified otherwise. |

A machine-readable version is in [metadata/claims.json](../metadata/claims.json).

## A00 — reported-proof-only

Four-term family [[8a^2+4a,2,2a+1]] -> [[16a^2+8a,4,2]] for a>=2.

**Scope:** Arbitrary-term extension, exactly four terms each.

**Limitation:** Original source/verifier/output package absent; public derivation retained. Not a strict-trinomial construction.

**Evidence:** [context/conversation/00-arbitrary-term-public-report.md](../context/conversation/00-arbitrary-term-public-report.md)

## A01 — reported-proof-only

gamma_all(N)=Theta(N^-1), with 4/N <= gamma_all(N) < 160/N for sufficiently large N.

**Scope:** Term counts may grow.

**Limitation:** Not a result for the strict-trinomial class; source code package absent.

**Evidence:** [context/conversation/00-arbitrary-term-public-report.md](../context/conversation/00-arbitrary-term-public-report.md)

## I01 — inherited-input

[[78,4,6]] -> [[156,4,14]], ratio 7/3, for the supplied A,B and periods 39->78.

**Scope:** Reported strict-trinomial finite example.

**Limitation:** Independent exact-distance certificates are not present in the available filesystem.

**Evidence:** [context/conversation/INHERITED_INPUTS.md](../context/conversation/INHERITED_INPUTS.md); [context/input/Pasted text.txt](../context/input/Pasted text.txt)

## I02 — inherited-input

[[156,4,14]] -> [[312,8,12]] and the stated infinite 14->12 family; ratio 6/7.

**Scope:** Reported strict-trinomial degrading covers.

**Limitation:** Early report checks a weight-12 nonboundary and dimensions, not both exact distances. Later stages inherit exactness; original independent source package absent.

**Evidence:** [context/input/Pasted text.txt](../context/input/Pasted text.txt); [context/input/Pasted markdown.md](../context/input/Pasted markdown.md); [context/conversation/INHERITED_INPUTS.md](../context/conversation/INHERITED_INPUTS.md)

## I03 — inherited-input

d>4 implies d_2>=6, with the stated stronger no-small-cycle fact.

**Scope:** Strict-trinomial starting assumptions.

**Limitation:** Prior weight-two/weight-four package unavailable; preserve the original supplied scope.

**Evidence:** [context/input/Pasted markdown.md](../context/input/Pasted markdown.md)

## D01 — computer-assisted-theorem

d_2=6 implies d<=56; combined with the stated small-weight inputs, d>56 implies d_2>=8.

**Scope:** All valid strict-trinomial double covers in the supplied proof.

**Limitation:** Uniform conclusion requires the proof and exhaustive completeness argument, not only retained-catalogue checking.

**Evidence:** [research/01-weight-six/proof.md](../research/01-weight-six/proof.md); [research/01-weight-six/mixed_presentations.tsv](../research/01-weight-six/mixed_presentations.tsv); [research/01-weight-six/presentation_verification.json](../research/01-weight-six/presentation_verification.json); [research/01-weight-six/pure_six_results.json](../research/01-weight-six/pure_six_results.json); [research/01-weight-six/classify_six.cpp](../research/01-weight-six/classify_six.cpp); [research/01-weight-six/verify_presentations.py](../research/01-weight-six/verify_presentations.py)

## D02 — symbolic-proof-and-exact-checks

The weight-six two-check coefficient-filling lemma is false. For L=4^j, |q|=6 and minimum coefficient filling is 3*9^j.

**Scope:** Explicit connected strict-trinomial family; L<=d<=4L.

**Limitation:** Base distances are intervals, not asserted exact distances.

**Evidence:** [research/01-weight-six/proof.md](../research/01-weight-six/proof.md); [research/01-weight-six/verify_family.py](../research/01-weight-six/verify_family.py); [research/01-weight-six/family_verification.json](../research/01-weight-six/family_verification.json)

## D03 — symbolic-proof-and-exact-checks

For that specified cover, 2+2*9^j <= Fill(q) <= 6+6*9^j.

**Scope:** Lifted filling of the particular weight-six boundary.

**Limitation:** Every cover cycle above that q also obeys the lower bound. Not a vanishing-ratio family.

**Evidence:** [research/01-weight-six/proof.md](../research/01-weight-six/proof.md); [research/01-weight-six/family_verification.json](../research/01-weight-six/family_verification.json)

## D04 — computer-assisted-theorem

d_2=8 implies d<=96.

**Scope:** Term-preserving finite abelian quotients with positive-dimensional base, not only doubles.

**Limitation:** No new exact ratio record. Combined d>96 => d_2>=10 uses earlier exclusions.

**Evidence:** [research/02-weight-eight/proof.md](../research/02-weight-eight/proof.md); [research/02-weight-eight/verification_summary.json](../research/02-weight-eight/verification_summary.json); [research/02-weight-eight/highrank_certificates.json](../research/02-weight-eight/highrank_certificates.json); [research/02-weight-eight/low_free_lattices.tsv](../research/02-weight-eight/low_free_lattices.tsv); [research/02-weight-eight/verify_summary.py](../research/02-weight-eight/verify_summary.py)

## D05 — symbolic-proof-and-exact-checks

d<=4*d_2^3.

**Scope:** Strict-trinomial doubles, extended as stated to finite abelian quotients with 2-group kernel.

**Limitation:** Symbolic theorem independent of earlier incidence catalogues; finite tests are not its proof.

**Evidence:** [research/03-structural-degradation/proof.md](../research/03-structural-degradation/proof.md); [research/03-structural-degradation/verification_summary.json](../research/03-structural-degradation/verification_summary.json)

## D06 — symbolic-proof-and-exact-checks

gamma_3(N)>=max(min(1/12,20/N),N^(-2/3),pi*3^(1/6)/(2^(13/3)*sqrt(N))).

**Scope:** Degradation scale; first term uses earlier small-weight inputs.

**Limitation:** Not a positive universal ratio and not a sharp asymptotic equivalence.

**Evidence:** [research/03-structural-degradation/proof.md](../research/03-structural-degradation/proof.md); [research/03-structural-degradation/verify_geometry.py](../research/03-structural-degradation/verify_geometry.py); [research/03-structural-degradation/geometry_verification.json](../research/03-structural-degradation/geometry_verification.json)

## D07 — symbolic-proof-and-exact-checks

Compact projection is injective for support-generated rank-one odd-torsion presentations under the stated 2-group quotients.

**Scope:** Compact homology image; gives linear descent for a nonboundary compact lift.

**Limitation:** Not a statement that all finite homology is compact. Visible 2-primary torsion remains.

**Evidence:** [research/04-quadratic-bottleneck/proof.md](../research/04-quadratic-bottleneck/proof.md); [research/04-quadratic-bottleneck/verify.py](../research/04-quadratic-bottleneck/verify.py); [research/04-quadratic-bottleneck/verify_independent.py](../research/04-quadratic-bottleneck/verify_independent.py); [research/04-quadratic-bottleneck/cases.json](../research/04-quadratic-bottleneck/cases.json)

## D08 — disproved-approach

Short relation rows do not imply a quadratic cofactor bound; changing their integral basis does not repair the example.

**Scope:** Saturated rank-one lattice example.

**Limitation:** Not an actual code-distance counterexample.

**Evidence:** [research/04-quadratic-bottleneck/proof.md](../research/04-quadratic-bottleneck/proof.md); [research/04-quadratic-bottleneck/summary.json](../research/04-quadratic-bottleneck/summary.json)

## D09 — disproved-approach

A torsion-changing strict-trinomial quotient can kill the compact image even when universal H1 is simple/semisimple.

**Scope:** Specified C3 x C2 x Z example and its finite realization.

**Limitation:** Not a degradation counterfamily; there is an independent short base logical.

**Evidence:** [research/04-quadratic-bottleneck/proof.md](../research/04-quadratic-bottleneck/proof.md); [research/04-quadratic-bottleneck/verify.py](../research/04-quadratic-bottleneck/verify.py); [research/04-quadratic-bottleneck/summary.json](../research/04-quadratic-bottleneck/summary.json)

## D10 — symbolic-proof-and-exact-checks

For principal-period doubles, compact loss is fH1/f^2H1; the cyclic-torsion subclass has the specified exact gcd criterion.

**Scope:** Requires the stated nonzerodivisor-period hypotheses.

**Limitation:** The specialization-created term remains separate; not applicable unchanged to a zerodivisor torsion quotient.

**Evidence:** [research/04-quadratic-bottleneck/proof.md](../research/04-quadratic-bottleneck/proof.md); [research/04-quadratic-bottleneck/verify_cyclic_strip.py](../research/04-quadratic-bottleneck/verify_cyclic_strip.py); [research/04-quadratic-bottleneck/cyclic_strip_cases.json](../research/04-quadratic-bottleneck/cyclic_strip_cases.json)

## D11 — symbolic-proof-and-exact-checks

Active finite local H1 is N_m^2, H0=H2=N_m; m has one or two nonzero binary digits, with the stated cover projection and transfer forms.

**Scope:** Actual support-generated finite BB groups of rank at most two.

**Limitation:** Not arbitrary universal rank-four incidence groups; normalizing maps are not Hamming isometries.

**Evidence:** [research/05-visible-two-primary/proof.md](../research/05-visible-two-primary/proof.md); [research/05-visible-two-primary/local_cases.json](../research/05-visible-two-primary/local_cases.json); [research/05-visible-two-primary/structured_verification.json](../research/05-visible-two-primary/structured_verification.json); [research/05-visible-two-primary/verify_local.py](../research/05-visible-two-primary/verify_local.py)

## D12 — symbolic-proof-and-exact-checks

High-contact family has exact base distance 4 and cover distance at most 6, despite unbounded nilpotent lengths.

**Scope:** Q=4^j family; parameters and hypotheses in source.

**Limitation:** No exact cover distance claimed; not an unbounded-degradation family.

**Evidence:** [research/05-visible-two-primary/proof.md](../research/05-visible-two-primary/proof.md); [research/05-visible-two-primary/verify_family.py](../research/05-visible-two-primary/verify_family.py); [research/05-visible-two-primary/family_verification.json](../research/05-visible-two-primary/family_verification.json)

## D13 — symbolic-proof-and-exact-checks

d<=3*d_2^2 for the deck-involution strip subclass.

**Scope:** Requires a weight-preserving compact incidence lift over T_odd x C2 x Z, with that involution mapping to the actual deck transformation.

**Limitation:** Not a global quadratic theorem; retained-involution period doubles and higher/finite incidence mechanisms remain outside.

**Evidence:** [research/06-sparse-deck-descent/proof.md](../research/06-sparse-deck-descent/proof.md); [research/06-sparse-deck-descent/verify.py](../research/06-sparse-deck-descent/verify.py); [research/06-sparse-deck-descent/cases.json](../research/06-sparse-deck-descent/cases.json); [research/06-sparse-deck-descent/audit.md](../research/06-sparse-deck-descent/audit.md)

## D14 — disproved-approach

The deck-killing derivative operator can have nonzero syndrome in a retained-involution base.

**Scope:** Exact unchanged-check odd-period family in source.

**Limitation:** Its weight-14 kernel witness is not minimum; an independent base logical has weight at most 8.

**Evidence:** [research/06-sparse-deck-descent/proof.md](../research/06-sparse-deck-descent/proof.md); [research/06-sparse-deck-descent/verification_summary.json](../research/06-sparse-deck-descent/verification_summary.json)

## P01 — symbolic-proof-and-exact-checks

Every universal physical cover cycle is parameterized by k,h; finite compact nonboundary is exactly g_plus not dividing k.

**Scope:** No-universal-torsion rank-one setting, including the stated split/nonsplit seams.

**Limitation:** Retains separate specialization-created finite homology. No conclusion for arbitrary torsion presentations.

**Evidence:** [research/07-rank-one-amplification/proof.md](../research/07-rank-one-amplification/proof.md); [research/07-rank-one-amplification/verify.py](../research/07-rank-one-amplification/verify.py); [research/07-rank-one-amplification/audit.md](../research/07-rank-one-amplification/audit.md)

## P02 — symbolic-proof-and-exact-checks

Factor-three and factor-two replacement bounds hold for the specified single-parity and other resolved voltage subclasses.

**Scope:** Precise normalization and parity hypotheses in Sections 3-5.

**Limitation:** Not the entire residual mixed-parity inequality.

**Evidence:** [research/07-rank-one-amplification/proof.md](../research/07-rank-one-amplification/proof.md); [research/07-rank-one-amplification/verification_summary.json](../research/07-rank-one-amplification/verification_summary.json)

## P03 — symbolic-proof-and-exact-checks

Along fixed compatible gcd data and sufficiently large periods, d=mu0 and d_2=mu_plus.

**Scope:** Period stabilization for the exact full Laurent minima.

**Limitation:** Does not assert equality for arbitrary short periods.

**Evidence:** [research/07-rank-one-amplification/proof.md](../research/07-rank-one-amplification/proof.md); [research/07-rank-one-amplification/audit.md](../research/07-rank-one-amplification/audit.md)

## P04 — exact-minimum-certificate

mu0=8 and mu_plus=14 for A=1+z^2+z^7, B=1+z+z^8 with the stated twists.

**Scope:** All Laurent degrees and all admissible messages/boundaries.

**Limitation:** Independent Bellman edge checking gives the all-degree lower bounds. Finite matrix tests alone would not suffice.

**Evidence:** [research/07-rank-one-amplification/family_certificate.json](../research/07-rank-one-amplification/family_certificate.json); [research/07-rank-one-amplification/base_potential.bin](../research/07-rank-one-amplification/base_potential.bin); [research/07-rank-one-amplification/cover_potential.bin](../research/07-rank-one-amplification/cover_potential.bin); [research/07-rank-one-amplification/verify.py](../research/07-rank-one-amplification/verify.py)

## P05 — symbolic-plus-exact-minimum-certificate

[[2L,4,8]] -> [[4L,4,14]] for odd multiples of 3 with L>=105.

**Scope:** Combination of P03 and P04 in the supplied proof.

**Limitation:** Ratio 7/4 is not a new record or unbounded-amplification result.

**Evidence:** [research/07-rank-one-amplification/proof.md](../research/07-rank-one-amplification/proof.md); [research/07-rank-one-amplification/family_certificate.json](../research/07-rank-one-amplification/family_certificate.json); [research/07-rank-one-amplification/verify.py](../research/07-rank-one-amplification/verify.py)

## P06 — disproved-approach

The naive Frobenius weight-at-most-3w candidate is a multiplier of transfer and is killed whenever that transfer is killed.

**Scope:** Exact physical and homology identity.

**Limitation:** Disproves the proposed nonboundary argument, not factor three.

**Evidence:** [research/07-rank-one-amplification/proof.md](../research/07-rank-one-amplification/proof.md); [research/07-rank-one-amplification/verify.py](../research/07-rank-one-amplification/verify.py)

## P07 — symbolic-proof-and-exact-checks

For the specified arithmetic-progression mixed pairs, a+b<=mu0 and a+b<=mu_plus<=2(a+b); hence mu_plus<=2mu0.

**Scope:** a,b>0, distinct and coprime; both congruent 1 or both 5 modulo 6.

**Limitation:** Not exact distances for every pair and not the full mixed-parity class.

**Evidence:** [research/08-mixed-laurent/proof.md](../research/08-mixed-laurent/proof.md); [research/08-mixed-laurent/verify.py](../research/08-mixed-laurent/verify.py); [research/08-mixed-laurent/verification_summary.json](../research/08-mixed-laurent/verification_summary.json)

## P08 — disproved-approach

The four-term message cancellation family beats the constant message by a growing additive gap.

**Scope:** Explicit B_j,F_j polynomial identity for all j>=0.

**Limitation:** Only constructed message weights; not complete minima and not a factor-three counterexample.

**Evidence:** [research/08-mixed-laurent/proof.md](../research/08-mixed-laurent/proof.md); [research/08-mixed-laurent/verify.py](../research/08-mixed-laurent/verify.py); [research/08-mixed-laurent/verification_summary.json](../research/08-mixed-laurent/verification_summary.json)

## P09 — symbolic-proof-and-exact-checks

The fixed-c parameterization has an exact systematic four-output and off-support penalty form.

**Scope:** All Laurent messages and boundary adjustments retained.

**Limitation:** No restriction to base-minimizing F or fixed H is justified by the reformulation.

**Evidence:** [research/08-mixed-laurent/proof.md](../research/08-mixed-laurent/proof.md); [research/08-mixed-laurent/audit.py](../research/08-mixed-laurent/audit.py)

## P10 — symbolic-exact-small-minimum

mu0=10 for the small arithmetic-progression pair a=1,b=7.

**Scope:** Specific base Laurent minimum.

**Limitation:** Not an exact cover minimum or a new finite ratio record.

**Evidence:** [research/08-mixed-laurent/proof.md](../research/08-mixed-laurent/proof.md); [research/08-mixed-laurent/verification_summary.json](../research/08-mixed-laurent/verification_summary.json)

## P11 — symbolic-proof-and-exact-checks

span(B)<=4 wt(F) wt((B/c)F) for every c-nondivisible Laurent F.

**Scope:** Fixed c=1+z+z^2; E=6r+2 and O=6t+1, including negative exponents.

**Limitation:** Not a linear uncertainty bound. Uses actual strict-trinomial support structure.

**Evidence:** [research/09-fixed-c-product-bound/proof.md](../research/09-fixed-c-product-bound/proof.md); [research/09-fixed-c-product-bound/verify.py](../research/09-fixed-c-product-bound/verify.py); [research/09-fixed-c-product-bound/verification_summary.json](../research/09-fixed-c-product-bound/verification_summary.json)

## P12 — symbolic-proof-and-exact-checks

mu_plus<=mu0^2+2, and <=mu0^2 for positive E,O.

**Scope:** Full fixed-c Laurent minima; finite consequences only in the inherited stabilized regime.

**Limitation:** Not a global BB amplification bound and not the degradation inequality d<=C*d_2^2.

**Evidence:** [research/09-fixed-c-product-bound/proof.md](../research/09-fixed-c-product-bound/proof.md); [research/09-fixed-c-product-bound/audit.md](../research/09-fixed-c-product-bound/audit.md)

## P13 — symbolic-proof-and-exact-checks

All 12 admissible cover residue classes are physical monomial translates, yielding exact unrestricted boundary-coset minimizations.

**Scope:** Fixed c, actual monomial basis.

**Limitation:** The boundary variable remains arbitrary; does not imply constant-message optimality.

**Evidence:** [research/09-fixed-c-product-bound/proof.md](../research/09-fixed-c-product-bound/proof.md); [research/09-fixed-c-product-bound/verify.py](../research/09-fixed-c-product-bound/verify.py)

## P14 — symbolic-proof-and-exact-checks

A factor-three violation requires mu0 < (wt(b)+1)/2; unbounded ratios require both minimizing block weights to diverge.

**Scope:** Necessary conditions for the fixed-c strict-trinomial case.

**Limitation:** Necessary is not sufficient; still need a full cover lower bound.

**Evidence:** [research/09-fixed-c-product-bound/proof.md](../research/09-fixed-c-product-bound/proof.md)

## P15 — exact-inadmissible-counterfamily

The relaxed systematic problem has exact minima mu0=2, mu_plus=4N+2 for all N>=1.

**Scope:** Second lifted numerator has five supported terms.

**Limitation:** Invalid strict-trinomial termwise support matching. Not a target BB-cover counterexample.

**Evidence:** [research/09-fixed-c-product-bound/proof.md](../research/09-fixed-c-product-bound/proof.md); [research/09-fixed-c-product-bound/verify.py](../research/09-fixed-c-product-bound/verify.py); [research/09-fixed-c-product-bound/audit.md](../research/09-fixed-c-product-bound/audit.md)

## O01 — open

Universal strict-trinomial positive degradation constant, or a strict-trinomial family with d->infinity and d_2/d->0.

**Scope:** Global degradation question.

**Limitation:** Neither established in the available record.

**Evidence:** [research/03-structural-degradation/proof.md](../research/03-structural-degradation/proof.md)

## O02 — open

Universal quadratic degradation improvement d<=C*d_2^2.

**Scope:** Mixed finite/strip visible-2-primary obstruction outside the proved subclasses.

**Limitation:** Finite-local classification and the deck-involution subclass do not settle the global statement.

**Evidence:** [research/06-sparse-deck-descent/proof.md](../research/06-sparse-deck-descent/proof.md)

## O03 — open

mu_plus<=3*mu0 for all remaining fixed-c mixed-parity pairs.

**Scope:** Full F,H Laurent optimization.

**Limitation:** Unproved and unrefuted; no certified strict-trinomial full-minimum violation.

**Evidence:** [research/09-fixed-c-product-bound/proof.md](../research/09-fixed-c-product-bound/proof.md)

## O04 — open

Half-generator lower bound mu0 >= (wt(b)+1)/2.

**Scope:** Sufficient proposed fixed-c lemma.

**Limitation:** Unproved and unrefuted. Its failure alone would not prove factor-three failure.

**Evidence:** [research/09-fixed-c-product-bound/proof.md](../research/09-fixed-c-product-bound/proof.md)

## O05 — open

Finiteness of C_*=sup d_2/d.

**Scope:** Global amplification including remaining rank-one torsion and other mechanisms.

**Limitation:** No global universal linear bound or admissible unbounded-ratio family established here.

**Evidence:** [research/09-fixed-c-product-bound/proof.md](../research/09-fixed-c-product-bound/proof.md)

## I04 — inherited-branch-assertion

Genuinely higher-rank compact factor-two theorem described as resolved in a user handoff.

**Scope:** Other-window context; exact standalone hypotheses unavailable here.

**Limitation:** No standalone proof package for this assertion was available; not promoted to a repository theorem.

**Evidence:** [context/conversation/USER_HANDOFFS.md](../context/conversation/USER_HANDOFFS.md); [context/conversation/INHERITED_INPUTS.md](../context/conversation/INHERITED_INPUTS.md)

