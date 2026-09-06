# Current state, with directions and evidence separated

This is an editorial index to the source snapshots, not a replacement proof. Mathematical statuses below are **the statuses stated in the archived research**. Export-time execution checks do not elevate a stated proof to external certification or resolve an open gap.

## Latest active problem: amplification, fixed quadratic divisor

Work over $S=\mathbb F_2[z^{\pm1}]$. The latest stage fixes

$$c=1+z+z^2,\quad B=1+z^E+z^O,\quad E=6r+2,\quad O=6t+1,$$

$$b=B/c,\quad P=(B+c)/c^2=(b+1)/c.$$

Both exponents may be negative. Each check must retain three distinct supported terms, and a finite cover must match terms individually. The two minima optimize all admissible Laurent messages and all universal boundary adjustments:

$$\mu_0=\min_{c\nmid F}(|bF|+|F|),$$

$$\mu_+=\min_{\substack{F,H\in S\\c\nmid F}}
\bigl(|(b+P)F+bH|+|PF+bH|+|F+H|+|H|\bigr).$$

**Open:** $\mu_+\le3\mu_0$; any universal linear bound for this remaining class; a genuine strict-trinomial full-minimum counterexample; and global finiteness of $C_*=\sup d_2/d$.

The [latest supplied proof](../research/09-fixed-c-product-bound/proof.md) states the following results.

* For every admissible message, $R=\operatorname{span}(B)\le4|bF||F|$.
* If a minimizing base word has block weights $a,m$, then $\mu_+\le R+2\le4am+2\le\mu_0^2+2$. For $E,O>0$, $\mu_+\le4am\le\mu_0^2$.
* All twelve admissible residue classes in the cover are physical monomial translates. This gives a single-coset minimization with an unrestricted boundary variable, not constant-message optimality.
* If $\beta=|b|+1$, then the explicit cover-generator weight is at most $3\beta/2$. A factor-three violation therefore requires $\mu_0<\beta/2$.
* The same systematic identity without the strict term-matching condition permits exact minima $\mu_0=2$, $\mu_+=4N+2$. Its second lifted check has five terms: this is an inadmissible control, not a BB counterexample.

The sufficient **half-generator lower bound** $\mu_0\ge(|b|+1)/2$ is itself unproved and unrefuted. Refuting it would not certify a factor-three violation.

## Earlier amplification progress retained

The [rank-one stage](../research/07-rank-one-amplification/proof.md) supplies the complete $(k,h)$ physical parameterization, an exact compact nonboundary criterion, factor-three and factor-two subclasses, and period stabilization. It explicitly retains specialization-created finite homology rather than replacing it by compact homology.

Its retained all-degree Bellman certificates prove $\mu_0=8$, $\mu_+=14$ for

$$A=1+z^2+z^7,\qquad B=1+z+z^8,$$

with both constant terms twisted to the deck involution upstairs. Together with its stabilization proof, this gives

$$[[2L,4,8]]\longrightarrow[[4L,4,14]],\quad 3\mid L,\ L\text{ odd},\ L\ge105.$$

This is an exact family in the source package, not an unbounded-ratio result or an improvement of the inherited $7/3$ example.

The [mixed-Laurent stage](../research/08-mixed-laurent/proof.md) proves $\mu_+\le2\mu_0$ for arithmetic-progression supports $1+z^a+z^{2a}$ and $1+z^b+z^{2b}$ with the specified coprimality and congruence hypotheses. It also gives an exact nonconstant-message cancellation family. That family only supplies upper-bound words, not the full minima needed for an amplification counterexample.

## Degradation branch: retained, not superseded by the opposite-direction work

The [structural stage](../research/03-structural-degradation/proof.md) states the uniform theorem

$$d\le4d_2^3$$

for valid strict-trinomial binary BB double covers with $k>0$, and more generally the stated term-preserving finite-abelian quotients with 2-group kernel. It does **not** prove $d_2\le4d^3$.

The strongest retained lower bound on the degradation function is

$$\gamma_-^{(3)}(N)\ge
\max\left\{\min\left(\frac1{12},\frac{20}{N}\right),\ N^{-2/3},\
\frac{\pi3^{1/6}}{2^{13/3}\sqrt N}\right\}.$$

The first term uses earlier small-weight exclusions; the other terms come from the structural proof. Its consequences exclude every fixed $d_2$ as $d\to\infty$, but do not exclude $d_2\to\infty$ with $d_2=o(d)$.

The proposed global quadratic degradation bound $d\le C d_2^2$ remains unresolved. Progress includes odd-torsion compact descent, the finite-local nilpotent classification, and the restricted physical theorem $d\le3d_2^2$ when a weight-preserving compact incidence lift has a torsion involution mapping to the actual deck transformation. This last hypothesis does not include retained-involution period doubling or arbitrary finite incidence presentations.

No strict-trinomial vanishing-ratio family or universal positive lower constant is established in the supplied record. The $14\to12$ family and ratio $6/7$ are retained as inherited exact inputs, not independently distance-certified by the available packages. The often quoted size range is $N\ge636$ for the inherited infinite family; this is not a claim that 636 is the smallest seed size.

## Earlier arbitrary-term result: different class and weaker archival availability

The public early report states

$$[[8a^2+4a,2,2a+1]]\longrightarrow[[16a^2+8a,4,2]],\quad a\ge2,$$

with four terms in each polynomial, and $\gamma_-^{\rm all}(N)=\Theta(N^{-1})$ when term counts may grow. These are not strict-trinomial results. The visible derivations are preserved in [the early report](../context/conversation/00-arbitrary-term-public-report.md); its original verifier and output files are missing from the available runtime.

## Do not reinterpret historical endpoints as current endpoints

The weight-six stage ended with $d_2=8$ as its next unexplored weight; the weight-eight stage then resolved that case; the structural theorem later excluded every bounded $d_2$. These historical endpoints remain in the unchanged source notes. They are not contradictions requiring edits.

Likewise, the transition to amplification was an explicit later user instruction. The earlier attached prompts that prohibit amplification are historical task context, not a current restriction that erases the later branch.
