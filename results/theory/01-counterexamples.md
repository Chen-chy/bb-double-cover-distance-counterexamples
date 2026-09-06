[研究结果总目录](../README.md) · [结论登记表](../CLAIMS.md) · [下一章](02-homology.md)

> 本章包含完整论证，可独立于 PDF 阅读。符号、范围和引用见正文；GitHub 版命题编号独立于排版稿。

<a id="sec-examples"></a>

# Two counterexamples to the double-cover distance bounds

Symons, Rajput, and Browne define term-matched group-algebra covers of bivariate bicycle (BB) codes and conjecture $d\le d_h\le hd$ for an $h$-cover [SRB, Theorem 3.1 and Section 4.3](../REFERENCES.md#ref-SRB). Their proved odd-degree statements do not cover binary double covers. We begin with two counterexamples to the conjectured even-degree extension. The code appearing upstairs in the first example is exactly the code appearing downstairs in the second.

<a id="conventions-and-the-three-codes"></a>

## Conventions and the three codes

For a finite abelian group $G$, put $R=\mathbb F_2[G]$ and use its group elements as the physical coordinate basis. A pair of commuting polynomials gives the complex

<a id="eq-complex"></a>

$$
R\xrightarrow{\partial_2}R^2\xrightarrow{\partial_1}R,
 \qquad \partial_2h=(Bh,Ah),\qquad \partial_1(u,v)=Au+Bv.
$$

If $M_P$ is the multiplication matrix of $P$, our CSS matrices are

<a id="eq-matrices"></a>

$$
H_X=(M_A\ M_B),\qquad H_Z=(M_B^T\ M_A^T).
$$

Thus $H_XH_Z^T=0$. A $Z$ logical is a cycle not in $\operatorname{im}\partial_2$. We always minimize Hamming weight in the displayed group basis, not in an abstract module basis. The inversion-and-block-swap permutation

<a id="eq-J"></a>

$$
J(u,v)=(v^\star,u^\star),\qquad g^\star=g^{-1},
$$

identifies the $Z$ and $X$ homologies isometrically. Consequently $d_X=d_Z=d$.

Write $Q(A,B;\ell,m)$ when $G=\mathbb Z_\ell\times\mathbb Z_m$. The monomial $x^iy^j$ has index $im+j$ in each block; the right block has offset $\ell m$. Every polynomial below has exactly three distinct supported monomials. Period $m=1$ means $y=1$, not a lost monomial: the three $x$ powers remain distinct. This case is explicitly allowed by the group-algebra definition and occurs among the examples in [SRB, Remark 5 and Tables 2–4](../REFERENCES.md#ref-SRB).

Set

<a id="eq-AB"></a>

$$
A=1+x^8+x^{25},\qquad B=1+x^2+x^{13},
$$

and, for the second cover, set

<a id="eq-ABtilde"></a>

$$
A'=1+x^8y+x^{25},\qquad B'=1+x^2y+x^{13}.
$$
<a id="thm-examples"></a>

**Theorem 1** (Two exact, computer-assisted counterexamples). The following are connected, valid term-matched binary BB double covers:

<a id="eq-upcase"></a>
<a id="eq-downcase"></a>

$$
\begin{aligned}
 Q(A,B;39,1)&=[[78,4,6]]
       \longrightarrow Q(A,B;78,1)=[[156,4,14]],\\
 Q(A,B;78,1)&=[[156,4,14]]
       \longrightarrow Q(A',B';78,2)=[[312,8,12]].
\end{aligned}
$$

They give $d_2/d=7/3>2$ and $d_2/d=6/7<1$, respectively.

The algebraic parts of the proof follow below. The only computer-assisted parts are the complete short-circuit exclusions, whose branching completeness and pruning safety are proved in Appendix [6](06-certificate-algorithms.md#app-algorithms). Two standalone implementations regenerate, rather than read, each complete circuit set.

For [\[eq:upcase\]](01-counterexamples.md#eq-upcase), the covering map is $x^i\mapsto x^{i\bmod39}$ and the polynomials are unchanged. For [\[eq:downcase\]](01-counterexamples.md#eq-downcase), it is $x^iy^j\mapsto x^i$. Terms match individually in both cases. The induced maps on the four vertex types of the full Tanner graph have two preimages per vertex and are bijective on each neighborhood. In particular these are graph covers, not merely coefficient reductions that happen to commute with a differential. Constant terms connect all vertex types within a cell. Since $\gcd(8,25,39)=\gcd(8,25,78)=1$, the first two graphs are connected. In the last graph, $x^{25}$ and $x^{13}$ generate all $x$ shifts, and $x^8y$ supplies the remaining $y$ shift.

<a id="dimensions"></a>

## Dimensions

Let $g=1+x+x^2$ and $F_L=1+x^L$. Polynomial division gives $\gcd(A,B)=g$. For an explicitly checkable Bezout identity $UA+VB=g$, the supports are

$$
\begin{aligned}
 \operatorname{supp}U&=\{1,2,4,5,6,9,10\},\\
 \operatorname{supp}V&=\{0,2,5,6,7,8,9,10,11,13,14,16,17,18,21,22\}.
\end{aligned}
$$

Since $g\mid F_{39},F_{78}$, the cokernel of $\partial_1$ has dimension two in both cyclic codes. In general, inversion identifies the two check ranks and gives

<a id="eq-k-coker"></a>

$$
k=2\dim_{\mathbb F_2}R/(A,B).
$$

Thus both cyclic codes have $k=4$. This argument includes the repeated-root period $78$.

For the $(78,2)$ code, eliminate $y$ using $B'=0$:

$$
y=x^{-2}(1+x^{13}),\qquad
 C=A+x^6B=(1+x^6)(1+x^{19}).
$$

It follows that

$$
\mathbb F_2[x,y]/(F_{78},1+y^2,A',B')
 \cong\mathbb F_2[x]/(F_{78},B^2,C).
$$

The common gcd is $g^2=1+x^2+x^4$, so the quotient has dimension four and $k_2=8$. Independent binary elimination gives the same ranks:

| Code            | Qubits | $\operatorname{rank}H_X$ | $\operatorname{rank}H_Z$ | $k$ |
|:----------------|-------:|-------------------------:|-------------------------:|----:|
| $Q(A,B;39,1)$   |     78 |                       37 |                       37 |   4 |
| $Q(A,B;78,1)$   |    156 |                       76 |                       76 |   4 |
| $Q(A',B';78,2)$ |    312 |                      152 |                      152 |   8 |

No minimum-distance conclusion is inferred from these ranks.

<a id="a-weight-six-base-logical-and-a-weight-fourteen-cover-logical"></a>

## A weight-six base logical and a weight-fourteen cover logical

Put $F=1+x^{39}$ and

$$
z=(z_L,z_R)=(1+x^8+x^{16}+x^{25},\ 1+x^{11}),\qquad c=x^2+x^{11}.
$$

Ordinary polynomial multiplication gives

<a id="eq-zsyndrome"></a>

$$
Az_L+Bz_R=Fc.
$$

The two coordinates of $z$ are both $x$ modulo $g$, whereas every boundary coordinate is zero modulo $g$. Thus $z$ is a weight-six nonboundary modulo $F$.

Now let $P=x^9+x^{22}+x^{35}+x^{37}$. The further identity

$$
Az_L+BP+c=F(1+x^2+x^9)
$$

shows that

<a id="eq-w14"></a>

$$
w_{14}=(x^{39}z_L,\ z_R+FP)
$$

is a cycle modulo $F^2=1+x^{78}$. Its supports are

$$
\begin{aligned}
 \operatorname{supp}(w_{14})_L&=\{39,47,55,64\},\\
 \operatorname{supp}(w_{14})_R&=\{0,9,11,22,35,37,48,61,74,76\}.
\end{aligned}
$$

Its projection is the literal chain $z$. Since projection takes boundaries to boundaries, $w_{14}$ is a nonboundary. This proves the upper estimates $d\le6$ and $d_2\le14$ for [\[eq:upcase\]](01-counterexamples.md#eq-upcase).

The tempting weight-twelve transfer $Fz$ is instead a boundary. To make the obstruction concrete, let $H$ have support

$$
\begin{gathered}
\{1,8,9,10,11,12,13,15,16,17,18,19,20,23,24,25,27,28,31,32,\\
34,37,38,41,43,44,46,48,51,53,54,57,61,63,65,66,68,74\}.
\end{gathered}
$$

Then

<a id="eq-transfer-boundary"></a>

$$
(BH,AH)=Fz\pmod{F^2}.
$$

This is an actual two-chain filling, not an argument based only on a vanishing homological label.

<a id="a-weight-twelve-logical-in-the-distance-decreasing-cover"></a>

## A weight-twelve logical in the distance-decreasing cover

In $\mathbb F_2[x,y]/(1+x^{78},1+y^2)$ define

$$
\sigma=1+x^{39}y,\qquad
 \zeta_L=1+x^8y+x^{16}+x^{25},\qquad
 \zeta_R=1+x^{11}y,
$$

and set $w_{12}=\sigma(\zeta_L,\zeta_R)$. Before reduction of the $x$ period,

$$
A'\zeta_L+B'\zeta_R=\sigma y(x^2+x^{11}),\qquad
 \sigma^2=1+x^{78}.
$$

Hence $w_{12}$ is a cycle. Its two supports, in exponent-pair coordinates, are

$$
\begin{aligned}
 L:\ &\{(0,0),(8,1),(16,0),(25,0),(39,1),(47,0),(55,1),(64,1)\},\\
 R:\ &\{(0,0),(11,1),(39,1),(50,0)\}.
\end{aligned}
$$

All twelve positions are distinct.

For a direct nonboundary certificate use

$$
T=\mathbb F_4[\eta]/(\eta^2),\quad \omega^2+\omega+1=0,\qquad
 \phi(x)=\omega+\eta,\quad \phi(y)=1+\omega\eta.
$$

These images satisfy the two period relations and

$$
\phi(A')=\phi(B')=0,\quad
 \phi(\sigma)=\eta,\quad
 \phi(\zeta_L)=\omega,\quad
 \phi(\zeta_R)=\omega\pmod\eta.
$$

Both boundary coordinates map to zero, but

<a id="eq-dual-numbers"></a>

$$
\phi((w_{12})_L)=\phi((w_{12})_R)=\omega\eta\ne0.
$$

Thus $w_{12}$ is nontrivial. Notice that its projection is exactly $Fz=(BH,AH)$ from [\[eq:transfer-boundary\]](01-counterexamples.md#eq-transfer-boundary). The short cover class therefore projects to a base boundary, as it must in a distance-decreasing example.

<a id="complete-distance-exclusions"></a>

## Complete distance exclusions

A minimum-weight nonboundary has circuit support: a proper subcycle is either a smaller nonboundary or a boundary whose removal shortens the same nonzero class. Every column of either check has odd weight three, so every cycle has even weight. To certify the three distances it is therefore enough to exclude nonboundary circuits through weights $4,12,10$, respectively.

The independently regenerated complete $Z$-circuit counts are

| Code            | Search cutoff | Weight 6 | Weight 10 | Weight 12 | Total |
|:----------------|--------------:|---------:|----------:|----------:|------:|
| $Q(A,B;39,1)$   |             4 |        — |         — |         — |     0 |
| $Q(A,B;78,1)$   |            12 |       78 |       468 |       195 |   741 |
| $Q(A',B';78,2)$ |            10 |      156 |       936 |         — |  1092 |

Every enumerated circuit is a boundary. For the middle code, their translation orbits are precisely the orbits of

$$
\partial_2(1),\quad
 \partial_2(1+x^a)\ (a\in\{2,8,11,13,17,25\}),\quad
 \partial_2(A),\quad\partial_2(B),\quad\partial_2(H).
$$

The first nine orbits have size $78$, while $\partial_2(H)=Fz$ has orbit size $39$. For the last code the seven orbits are those of

$$
\partial'_2(1),\qquad \partial'_2(1+x^ay^b),
$$

where $(a,b)$ ranges over

$$
\{(2,1),(8,1),(11,1),(13,0),(17,1),(25,0)\}.
$$

Each has size $156$. These classifications are outputs of the searches, never assumptions used in pruning. The unrestricted exclusions, cycle parity, and attaining words prove Theorem [1](01-counterexamples.md#thm-examples). Both implementations also search the $X$ sector directly, in addition to checking the isometry [\[eq:J\]](01-counterexamples.md#eq-J).
