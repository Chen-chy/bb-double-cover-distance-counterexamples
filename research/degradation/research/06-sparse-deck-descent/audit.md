# Adversarial scope and correctness audit

## Claims that were checked rather than assumed

1. **Universal versus finite homology.** The argument uses the natural
   injection M/F_s M into finite H_1. It never substitutes M/F_s M for the
   whole finite homology group. F_s is explicitly a nonzerodivisor.
2. **Nonproduct periods.** The universal action of s is a on compact H_1,
   so the effective period is z^P+a^epsilon t_0, not automatically z^P+t_0.
   Actual finite binary matrices with epsilon=1 are included in the tests.
3. **Ramification.** A squared common factor can survive upstairs with a
   coefficient divisible by that factor. The derivative removes precisely
   one factor. The initial coefficient selectors alone do not prove this.
4. **Cancelling a check.** A can be a zerodivisor in the nonprimitive
   corner. The proof treats its zero character components separately,
   using that the primitive untwisted C is nonzero and hence V=0 there.
   Four executed examples have an identically zero A component.
5. **Physical weights.** The constructed operators are coefficient
   selectors and polynomial products over the binary monomial basis.
   Field decomposition and gcds are used only to certify nontriviality.
   No sparsity is assigned to a Fourier or Bezout transformation.
6. **Boundary adjustments.** The derivative certificate is proved for
   an arbitrary universal representative. The test inputs include added
   universal boundaries, not just compact module generators.
7. **Actual weight versus lift weight.** The theorem uses the weight of
   the compact lift. To conclude d<=3d_2^2, the minimum physical cover
   logical must have a lift of the same weight. This is an explicit
   hypothesis. All 93 successful finite verification witnesses have no
   collisions under specialization.
8. **Wrong deck subgroup.** The retained-involution period family has
   a genuine compact kernel class but the derivative replacement for
   s=1 has nonzero syndrome in its actual s-retaining base. This extension
   of the operator is false.
9. **Controlling the entire distance.** The proposed period-doubling
   counterfamily also has an independent weight-eight base nonboundary.
   It is not a growing-distance degradation family.
10. **Exact distance.** No new exact minimum distance or ratio is claimed.
    The numerical work certifies ranks, displayed logical witnesses,
    projection membership, and constructed replacement weights.

## What has not been verified or proved

The global quadratic theorem, the remaining higher visible torsion cases,
the finite incidence presentations, and general retained-involution
period-doubling descent are not resolved. The inherited global cubic bound
and the inherited exact 6/7 distance record were not independently re-run.
The new proof is not externally refereed or proof-assistant formalized.
