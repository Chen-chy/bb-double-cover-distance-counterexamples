[全部研究结果](../README.md) · [逐项结论](../CLAIMS.md) · [原始完整文本](../../research/degradation/research/04-quadratic-bottleneck/proof.md)

> 完整研究笔记的 GitHub 阅读版；仅调整数学分隔符、引用标记与链接。历史状态、限制和证明内容均保留。当前结论以总登记表中的逐项状态为准；这里的“验证”不等于独立同行评审。

# The quadratic bottleneck: compact descent and the remaining 2-primary obstruction

Date: 2026-09-06.

**Principal status: TRINOMIAL_STILL_OPEN.** This note does not prove or refute a universal quadratic distance bound. It proves a linear descent result for an entire class of incidence presentations, isolates a necessary 2-primary obstruction to superquadratic examples, gives exact compact-specialization formulas, and disproves a purely arithmetic shortcut to a quadratic bound. None of the finite computations below is a distance-degradation record.

## 0. Scope, conventions, and inherited inputs

The chain complex over a binary finite abelian group algebra is



$$
\mathcal C(A,B):\quad R\xrightarrow{s\mapsto(Bs,As)}R^2
\xrightarrow{(u,v)\mapsto Au+Bv}R.
$$



Both polynomials have exactly three distinct supported monomials in the actual cover and in the base. The group quotient matches the three terms individually in each polynomial. A binary double cover has a group kernel of order two. The results about descent below also allow any finite 2-group kernel.

This is the convention in Symons, Rajput, and Browne, *Sequences of Bivariate Bicycle Codes from Covering Graphs*, arXiv:2511.13560v3, Sections 2--4 and Theorem 3.1:
https://arxiv.org/html/2511.13560v3

The supplied current proof state establishes the following inputs; they are not new claims of this note:

* A minimum logical has circuit support. A syndrome-incidence pairing gives a connected cubic graph and a finite-support universal cycle over a presentation $H=\mathbb Z^4/L$. Its four generators are the normalized check translations. The actual support groups upstairs and downstairs are images of $H$.
* If the minimum cover weight is $w$, pure presentations and the surviving mixed free-rank-two presentations imply $d\le 2w^2$. Mixed free rank at least three cannot support a surviving universal cycle.
* The remaining finite/strip presentations give $d\le4w^3$.
* The ambient estimate is $d\le C_0n^{3/4}$, where $C_0=(16/3)(12/\pi^2)^{3/4}$.
* The established small-weight bounds are $d_2=6\Rightarrow d\le56$ and $d_2=8\Rightarrow d\le96$.

The inherited proof file is `strict_trinomial_structural/proof.md` in the preceding research package. This note separates its new conclusions from those inputs.

Throughout, “compact homology in a finite quotient” means the image of the homology of the infinite group-algebra complex. It does **not** mean all finite-quotient homology.

## 1. A squarefree gcd lemma forced by strict trinomials

Let $K$ be a field of characteristic two, and let



$$
P(z)=1+\alpha z^a+\beta z^b,\qquad \alpha,\beta\ne0,
$$



with integer exponents. If at least one of $a,b$ is odd, then every nonzero root of $P$ is simple.

Indeed,



$$
zP'(z)=(a\bmod2)\alpha z^a+(b\bmod2)\beta z^b.
$$



If exactly one exponent is odd, the right side is a nonzero monomial at a nonzero root. If both are odd, it equals $P+1$, hence equals 1 at a root. This also handles coincident free-coordinate exponents: the conclusion is about the actual sum after cancellation. In the degenerate case of a constant nonzero polynomial there are no roots.

Now let



$$
H=T\oplus\mathbb Z,
$$



where $|T|$ is odd, and assume that the four normalized check translations generate $H$. The group algebra splits as a product



$$
\mathbb F_2[H]\cong\prod_\chi K_\chi[z^{\pm1}],
$$



where each $K_\chi$ is a finite field. In a character component the checks have the form



$$
A_\chi=1+\alpha z^a+\beta z^b,
\qquad
B_\chi=1+\gamma z^c+\delta z^d.
$$



The four free exponents generate $\mathbb Z$, so at least one is odd. Therefore at least one check is squarefree on the multiplicative group, and



$$
g_\chi=\gcd(A_\chi,B_\chi)
$$



is squarefree up to Laurent units.

One check can be identically zero in a character component, but both cannot be zero: an identically zero trinomial must have all its terms at the same free position, whereas the four free exponents generate $\mathbb Z$. If one check is zero, the other still has an odd exponent and the same gcd conclusion holds.

## 2. Linear descent for odd-torsion strips

**Theorem 1 (compact descent).** Let $H=T\oplus\mathbb Z$, with $T$ finite of odd order, and let normalized strict-trinomial translations generate $H$. Let



$$
H\longrightarrow\widetilde G\longrightarrow G
$$



be finite images, with the second map having 2-group kernel. The induced projection is injective on the compact homology image. Consequently, if a finite-support universal cycle $Y$ maps to a nonboundary upstairs, its projection is a nonboundary downstairs and



$$
d(G)\le |pY|\le |Y|.
$$



The strict support and term-matching hypotheses are needed for the coding interpretation; the algebraic proof uses the normalized support-generated presentation.

**Proof.** Work in a character component $S=K[z^{\pm1}]$. Write



$$
A=ga,\qquad B=gb,\qquad (a,b)=S.
$$



Every universal cycle is $s(b,a)$, and the universal boundaries are the multiples of $g(b,a)$. This holds as well when one of $A,B$ is zero.

A surviving finite image of this component is $S/(F)$. The cycle $s(b,a)$ is a boundary there exactly when



$$
s\in(g,F).
$$



To see this, a boundary equation says $b(s-gr)=a(s-gr)=0$ modulo $F$; a Bézout combination of $a,b$ gives $s=gr$ modulo $F$. The converse is immediate. Thus the compact image is canonically



$$
S/(g,F).
$$



The group-algebra kernel of $\mathbb F_2[\widetilde G]\to\mathbb F_2[G]$ is nilpotent. In fact it is generated by $k-1$ for elements of the finite 2-group kernel; these generators commute and each is nilpotent. It follows that the two algebras have the same maximal ideals under projection, and the same surviving odd-character components. In a fixed component, the base and cover polynomials $F_1,F_2$ satisfy



$$
F_1\mid F_2,\qquad \sqrt{(F_1)}=\sqrt{(F_2)}.
$$



By Section 1, $g$ is squarefree. Hence



$$
(g,F_1)=(g,F_2).
$$



Projection therefore identifies the two compact images. This holds in every component and hence over $\mathbb F_2$. Finally, a group-algebra projection can only decrease physical Hamming weight. $\square$

This is not a monotonicity theorem for every finite logical in every strip parametrization. The infinite complex can acquire additional homology on imposing a period, and that contribution is not covered by Theorem 1. A circuit's own incidence presentation supplies precisely the finite-support universal cycle required by the theorem.

## 3. Visible 2-primary torsion is necessary for the unresolved case

Write $T_2(H)$ for the 2-primary torsion subgroup of $H$. If its image in the actual cover support group is trivial, all maps factor through $H/T_2(H)$.

If $H$ has rank one, this quotient has odd torsion, so Theorem 1 applies. If $H$ is finite, the quotient is an odd-order group. Its cover and base support groups then have odd order, so a surjection between them with 2-group kernel is an isomorphism. Again, projection cannot kill a nonboundary supported on that component.

**Corollary 2.** Subject to the inherited pure/free-rank-two results, a hypothetical strict-trinomial double cover with



$$
w=d_2,\qquad d>2w^2
$$



must have the following properties for every incidence pairing of its minimum logical:

1. the support is mixed;
2. its relation lattice has rational rank 3 or 4;
3. $T_2(H)$ has nontrivial image in the actual cover support group;
4. the projected logical is a base boundary.

In particular, the relation lattice must have an even nonzero Smith invariant:



$$
\operatorname{rank}_{\mathbb F_2}(L\bmod2)
<\operatorname{rank}_{\mathbb Q}L.
$$



The Smith condition is necessary, not sufficient. Formal even torsion killed by the actual realization cannot produce the obstruction. This corollary eliminates the entire odd-Smith finite/strip class from the cubic bottleneck.

## 4. Cubic cofactors really occur with short rows

Let $L\ge2$, and consider the rank-three relation lattice generated by



$$
r_1=(L,-1,0,0),\quad
r_2=(0,L,-1,0),\quad
r_3=(0,0,L,-1).
$$



For the root-difference set



$$
\mathcal D=\{\pm e_1,\pm e_2,\pm(e_1-e_2),
\pm e_3,\pm e_4,\pm(e_3-e_4)\},
$$



the row lengths are $L,L+1,L$. The middle row has length $L+1$, because its two nonzero entries lie in different root blocks.

The last-three-column minor is -1. Thus the lattice is saturated and its quotient is torsion-free of rank one. Its primitive cofactor vector, up to an overall sign, is



$$
c=(1,L,L^2,L^3).
$$



Consequently the strip expression in the inherited proof is



$$
\max\{\operatorname{span}(0,c_1,c_2),
\operatorname{span}(0,c_3,c_4)\}=L^3.
$$



Any other independent integral triple in the same lattice is $UR$ for an integral 3-by-3 matrix $U$ of nonzero determinant. Its cofactor vector is $\det(U)c$, so its span cannot be smaller. In particular,



$$
\frac{L^3}{(L+1)^2}\longrightarrow\infty.
$$



This refutes a quadratic cofactor bound based only on short rows, even with freedom to change their basis and even for saturated relation lattices.

**It is not a code-distance counterexample.** No claim is made that this row lattice occurs as the complete incidence presentation of a minimum weight-$O(L)$ logical. If it did occur as a torsion-free rank-one circuit presentation, Theorem 1 would imply linear distance descent. The geometric strip-width loss is therefore not itself evidence of genuine degradation.

## 5. Exact specialization: compact and period-created homology

Let $R$ be a commutative ring, $\mathcal C$ a complex of free $R$-modules, and let $f$ be a nonzerodivisor on $R$. Put



$$
M=H_1(\mathcal C),\qquad N=H_0(\mathcal C),\qquad
\mathcal C_f=\mathcal C\otimes_R R/(f).
$$



The short exact sequence of complexes



$$
0\to\mathcal C\xrightarrow{f}\mathcal C\to\mathcal C_f\to0
$$



gives



$$
0\longrightarrow M/fM\longrightarrow H_1(\mathcal C_f)
\longrightarrow N[f]\longrightarrow0,
\tag{5.1}
$$



where $N[f]=\ker(f:N\to N)$. This follows from the standard long exact sequence of homology; see Stacks Project, Lemma 12.13.6, https://stacks.math.columbia.edu/tag/0111 .

For the natural period double $R/(f^2)\to R/(f)$, the exact rows form a commutative diagram. Its three vertical maps are respectively



$$
M/f^2M\longrightarrow M/fM,
\qquad
H_1(\mathcal C_{f^2})\longrightarrow H_1(\mathcal C_f),
\qquad
N[f^2]\xrightarrow{f}N[f].
\tag{5.2}
$$



The right map is multiplication by $f$, not the identity. For example, if a lifted cycle has differential $f^2b$, its connecting image after reduction modulo $f$ is $fb$.

**Theorem 3 (exact compact loss).** The kernel of projection restricted to the compact homology image is exactly



$$
\boxed{fM/f^2M.}
\tag{5.3}
$$



Indeed, the left injections in (5.1) are injective and the left vertical map is the natural quotient.

If $M$ is finite dimensional over $\mathbb F_2$, (5.3) has dimension equal to the number of zero-eigenvalue Jordan blocks of multiplication by $f$ of length at least two. The invertible primary part contributes nothing. Thus a semisimple $M$ has no compact loss.

For a strip ring $R=\mathbb F_2[T][z^{\pm1}]$, a relation $f=z^P+t_0$ with $t_0\in T$ is a nonzerodivisor: its leading Laurent coefficient is a unit. The square $f^2=z^{2P}+t_0^2$ describes the corresponding period double, including a torsion seam.

These statements do not identify $M\otimes R/(f)$ with the entire finite homology. The term $N[f]$, which is $\operatorname{Tor}_1^R(N,R/(f))$, remains. Nor do (5.1)--(5.3) by themselves estimate the Hamming weight of any surviving or lost class.

## 6. A cyclic-torsion strip subclass with a complete gcd formula

Consider



$$
R=\mathbb F_2[t^{\pm1},z^{\pm1}]/(t^h+1),\qquad
A=1+t+z,
$$



and



$$
B=1+t^az^b+t^cz^d,
$$



with $b,d\ge0$; reducing $a,c$ modulo $h$ is harmless. Strictness is checked in the actual finite groups. Put



$$
m=2^{v_2(h)},\quad Q=t^h+1,\quad
Q_*=Q/(t+1)^m,
$$





$$
F=1+t^a(1+t)^b+t^c(1+t)^d,\qquad
 g=\gcd(Q_*,F).
\tag{6.1}
$$



Use $\gcd(Q_*,0)=Q_*$. The polynomial $Q_*$ is relatively prime to both $t$ and $t+1$.

**Theorem 4 (cyclic strip homology).** With $z$ acting as $1+t$,



$$
H_0(\mathcal C)\cong H_1(\mathcal C)
\cong \mathbb F_2[t]/(g)
\tag{6.2}
$$



as $R$-modules.

**Proof.** The check $A$ is a nonzerodivisor, since it is monic of degree one in $z$. Eliminating $z$ and remembering that it was invertible gives



$$
R/(A)\cong
\mathbb F_2[t^{\pm1},(1+t)^{-1}]/(Q)
\cong\mathbb F_2[t]/(Q_*).
$$



The other check reduces to $F$, so the cokernel is $\mathbb F_2[t]/(g)$.

For $H_1$, map a cycle $(u,v)$ to $v\bmod A$. The cycle equation makes this an element of $\operatorname{Ann}(F)$ in $R/(A)$. Every such annihilator element lifts to a cycle. If $v=Ar$, then $A(u+Br)=0$, hence $(u,v)=(Br,Ar)$. This proves



$$
H_1\cong\operatorname{Ann}_{\mathbb F_2[t]/(Q_*)}(F).
$$



This annihilator is generated by $Q_*/g$ and is isomorphic to $\mathbb F_2[t]/(g)$. $\square$

There is an explicit universal cycle that realizes this generator. Divide in $z$:



$$
B=F+A Q_B,
\qquad
S=Q/g\quad\text{in }\mathbb F_2[t]/(Q).
$$



Then $FS=0$, and



$$
W=(Q_BS,S)
\tag{6.3}
$$



is a universal cycle. Its module class generates (6.2), because the additional factor $(t+1)^m$ in $S$, compared with $Q_*/g$, is a unit on the active quotient.

Now impose $f=z^P+t^s$. It acts on (6.2) as



$$
f_0(t)=(1+t)^P+t^s.
$$



Set



$$
c_1=\deg\gcd(g,f_0),\qquad
c_2=\deg\gcd(g,f_0^2).
$$



**Corollary 5 (exact compact projection loss).** The compact dimensions in the base and cover are respectively $c_1,c_2$, and



$$
\boxed{\dim\ker(p_*\vert_{\rm compact})=c_2-c_1.}
\tag{6.4}
$$



Their full logical dimensions are $k=2c_1$ and $k_2=2c_2$, since the two terms in (5.1) have equal dimensions for the module in (6.2).

Equivalently, compact loss occurs exactly when some irreducible polynomial $p$ obeys



$$
0<v_p(f_0)<v_p(g).
\tag{6.5}
$$



Its contribution to (6.4) is



$$
\deg(p)\,[\min\{v_p(g),2v_p(f_0)\}
-\min\{v_p(g),v_p(f_0)\}].
$$



Squarefree $g$ therefore rules out compact loss even if the torsion order $h$ is even. A nonsquarefree $g$ need not cause loss: the period can already saturate its multiplicities.

This is an exact algebraic classification for the displayed subclass, not a classification of all mixed even-torsion incidence presentations. In particular, an incidence presentation can have noncyclic torsion and a double cover can change torsion rather than only square one period relation.

## 7. A strict-trinomial test showing the torsion hypothesis is needed

Let



$$
H=C_3(t)\times C_2(s)\times\mathbb Z(z),
\qquad
A=1+st+z,\quad B=1+t+sz,\quad e=1+s.
$$



The four normalized support translations generate $H$. Since



$$
A+B=e(t+z),\qquad e^2=0,
$$



$(e,e)$ is a universal cycle. Adding the elementary boundary $(B,A)$ gives



$$
Y=(B+e,A+e),\qquad |Y|=6.
$$



Impose $z^3=1$ and project $s\mapsto1$. The projected cycle is



$$
pY=(1+t+z,1+t+z),
$$



an elementary base boundary.

A concrete rectangular BB realization is



$$
\widetilde G=C_6(x)\times C_3(y),\quad
 t=x^2,\ s=x^3,\ z=y,
$$



with



$$
\widetilde A=1+x^5+y,\qquad
\widetilde B=1+x^2+x^3y.
$$



The base is $C_3(x)\times C_3(y)$, with $A=B=1+x^2+y$. Termwise supports are distinct and match. The support generators generate the whole cover group.

There is a symbolic nonboundary certificate. Map the finite cover algebra into



$$
D=\mathbb F_4[\epsilon]/(\epsilon^2),\qquad
 t\mapsto\omega,\ s\mapsto1+\epsilon,\ z\mapsto\omega^2,
$$



where $\omega^2+\omega+1=0$. The checks become $\omega\epsilon$ and $\omega^2\epsilon$. The linear functional



$$
\ell(u,v)=\omega u+\omega^2v
$$



annihilates every mapped boundary but gives $\ell(\epsilon,\epsilon)=\epsilon\ne0$. Thus $(e,e)$, and hence $Y$, is a nonboundary. The exact matrix verifier checks this independently, checks the projected boundary, and verifies the dual-number calculation for every element of $D$. It also checks the dimensions and excludes every cover weight-two cycle. For completeness, the base has distance two and the cover has distance four.

There is a further warning here: the **universal** module $M=H_1(\mathcal C)$ in this example is already semisimple. In the trivial odd character $t=1$, $A=z+e$ is a unit and there is no homology. In the $\mathbb F_4$ component $t=\omega$, eliminate $A$ to obtain



$$
z=\omega^2+\omega e,\qquad B=e.
$$



Consequently



$$
M\cong\operatorname{Ann}_{\mathbb F_4[e]/(e^2)}(e)
=e\mathbb F_4\cong\mathbb F_4,
$$



with $eM=0$ and $z$ acting as $\omega^2$. It is a simple module over the active component. Nevertheless the torsion quotient $s\mapsto1$ kills the entire compact homology image. In particular,



$$
M\otimes_R R/(e)\cong M\ne0
$$



while its natural map to $H_1(\mathcal C\otimes_R R/(e))$ is zero. The period-only assertion in Section 5 is not contradicted: multiplication by $e$ is a zerodivisor on $R$, so its short exact sequence of free complexes does not apply. This supplies an explicit strict-trinomial example in which even semisimplicity of universal homology does not imply compact survival for a torsion-changing quotient.

This is **not** a distance-degradation counterexample and is not used as a ratio result. It only shows that Theorem 1 cannot be extended to all even-torsion compact classes. In particular, compact projection failure is weaker than degradation of the minimum distance.

## 8. Exact verification and independent checks

Run `./run_all.sh` with Python 3. No third-party package is required.

`verify.py` constructs 512 support-generated odd-torsion strip instances, with torsion orders 1, 3, 5, 7, 9 and cover sizes up to 432 qubits. It computes universal syzygies by finite-field factorization and CRT, checks squarefree gcds, specializes the universal generators, and computes their homology spans and projection ranks by exact binary elimination. All 512 have a nonzero compact image; 313 use a nonzero seam. All compact projection maps are injective.

`verify_independent.py` uses a separate construction: binary nullspaces of a finite **universal** Laurent-coordinate window, followed by low-pivot raw rank increments modulo actual boundary columns. It uses neither the finite-field gcds nor CRT from the first verifier. The window contains all semisimple component syzygy generators, since the degree of each divided check is bounded by the original degree. It reproduces the compact ranks in all 512 cases.

`verify_cyclic_strip.py` checks 256 positive-dimensional cyclic-torsion cases, with torsion order up to 24. It verifies the universal syndrome of (6.3) before imposing any period, then compares the specialized compact ranks and full dimensions against (6.4). There are 62 cases with compact projection loss, 174 with squarefree $g$, and 20 nonsquarefree cases without loss. Every matrix dimension agrees with the polynomial formula. No minimum-distance claim is inferred from these 256 tests.

The scripts also check the cofactor family, a finite collection of the Jordan formulas, and the even-torsion countercheck in Section 7. All arithmetic is exact. These finite tests are consistency checks, not substitutes for the uniform proofs above. They do not exhaust the even-torsion presentations, and there is no new exact degradation record.

The final source and result files are hashed in `manifest.json`. The argument has not been externally refereed or formalized in a proof assistant.

## 9. What remains unchanged

No universal quadratic constant has been proved. No counterfamily to such a constant, and no strict-trinomial vanishing-ratio family, has been constructed.

The inherited global bounds remain



$$
d\le4d_2^3,
$$





$$
\gamma_-^{(3)}(N)\ge
\max\left\{
\min\left(\frac1{12},\frac{20}{N}\right),
N^{-2/3},
\frac{\pi3^{1/6}}{2^{13/3}\sqrt N}
\right\}.
$$



The inherited exact upper construction still gives ratio 6/7, in particular



$$
[[4h,4,14]]\longrightarrow[[8h,8,12]],
\quad h>156,\quad 3\mid h,\quad 7\nmid h.
$$



Its certification status is inherited; this note does not re-run its minimum-distance certificates. Thus the retained upper bound is $\gamma_-^{(3)}(N)\le6/7$ for $N\ge636$. There is no new ratio record.

The cubic theorem already excludes every bounded $d_2$ when $d\to\infty$. The established weight-six and weight-eight results and the failure of the two-check weight-six filling lemma remain unchanged.

## 10. The narrowed next lemma

**Visible-2-torsion circuit descent.** There is an absolute constant $C$ with the following property. Let $Y$ be a minimum nonboundary cover cycle of weight $w$ in a valid strict-trinomial binary BB double cover with positive-dimensional base. Suppose its mixed incidence presentation $H=\mathbb Z^4/L$ has $\operatorname{rank}_{\mathbb Q}L\in\{3,4\}$, that $T_2(H)$ has nontrivial image in the actual cover support group, and that $pY$ is a base boundary. Then the base distance satisfies $d\le Cw^2$.

Together with the inherited quadratic cases and Theorem 1, this is sufficient for a universal quadratic theorem. A counterexample to the universal quadratic statement must occur here. The unresolved point is a **Hamming-distance bound** for these surviving nilpotent mechanisms; the existence or dimension of $fM/f^2M$, or cubic growth of a cofactor, does not supply such a bound or a counterexample.
