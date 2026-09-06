[全部研究结果](../README.md) · [逐项结论](../CLAIMS.md) · [原始完整文本](../../research/homology/H03-class-metrics-and-exchange.md)

> 完整研究笔记的 GitHub 阅读版；仅调整数学分隔符、引用标记与链接。历史状态、限制和证明内容均保留。当前结论以总登记表中的逐项状态为准；这里的“验证”不等于独立同行评审。

> 历史研究报告：初稿中尚未解决的距离猜想已被 H03/H05 的精确反例推翻；报告中的候选引理与最终定理须分开阅读。有关 Bockstein 的四重厚化证明适用于文中规定的矩形周期覆盖，不自动推广到任意覆盖。旧附件链接只在可确认对应材料时重定向；文中的 current/latest 指历史撰写时点，不表示本次做了最新文献排查。原文件引用标记转换为参考文献中的 supplied v3。

**The original upper-bound conjecture is false—not only the Class-Lift Inequality.**

Take the same two trinomials at both periods:


$$
\boxed{
A=1+x^8+x^{25},\qquad B=1+x^2+x^{13}.
}
$$


Then


$$
\boxed{
Q(A,B,39,1)=[[78,4,6]],
\qquad
Q(A,B,78,1)=[[156,4,14]].
}
$$


The second code is a valid Theorem 3.1 double cover of the first, but


$$
\boxed{d_2=14>12=2d.}
$$



For a minimum base class $\alpha$ in this example,


$$
\boxed{
\alpha\in\operatorname{im}\beta_2,\qquad
\delta(\alpha)=6,\qquad
\mu(\alpha)=14.
}
$$


Thus allowing the projected chain to change by arbitrary base boundaries does **not** restore the proposed inequality.

This is a **computer-assisted counterexample**. The cycles, nontriviality arguments, transfer boundary, and polynomial identities below are explicit. The distance-exclusion step is an exact exhaustive circuit classification, with its completeness argument given below. Two independently implemented exact checks agree.

The [standalone verifier](../../archive/early_counterexample/verify_counterexample.py) requires only Python’s standard library. The [complete certificate package](../../archive/early_counterexample/MATHEMATICAL_CERTIFICATE.md) includes the mathematical certificate, an independent equivalent bivariate check, the previous-family audit, and the actual verification outputs.

## 1. Audit of the previous infinite family

The previous family


$$
[[18j,4,4]]\longrightarrow[[36j,4,6]],\qquad j\ge2,
$$


survives the audit.

The gcd calculation, classification of weight-four base cycles, $\mathbb F_4$ projection with $u^q=\omega$, and min-plus calculation remain valid. In particular, the wrap condition is


$$
v_{\mathrm{initial}}=\omega v_{\mathrm{final}},
$$


not an untwisted periodic condition. The parameter-uniform identity


$$
T_2\otimes M^{\otimes3}=T_2+2
$$


still gives


$$
\rho(z)=2j-1.
$$


The transfer-killing statement and the absence of cover cycles below weight six also survive. The $X/Z$ identification is a weight-preserving permutation, so it does not change those distances.

At class level, the family does satisfy


$$
\delta([z])=4,\qquad \mu([z])=6.
$$


I derive the general boundary transformation establishing this in Section 6.

There is, however, an important correction to the proposed interpretation of that family: its weight-preserving lift is **not** a lift into the particular fixed low sheet used in the definition of $\nu$. In that section,


$$
\boxed{
\nu([z])=
\begin{cases}
10j,&j\ \text{even},\\
\infty,&j\ \text{odd}.
\end{cases}}
$$


Thus the family supports the distinction between fixed projection and projected homology class, but it does not support the stronger $\nu$-inequality.

## 2. The counterexample: polynomials, dimensions, and explicit logicals

### Theorem

Let


$$
R_L=\mathbb F_2[x]/(x^L+1),
$$


with the usual monomial basis, and use the Koszul complex


$$
R_L\xrightarrow{\partial_2}R_L^2\xrightarrow{\partial_1}R_L,
$$


where


$$
\partial_2h=(Bh,Ah),\qquad
\partial_1(u,v)=Au+Bv.
$$


For


$$
A=1+x^8+x^{25},\qquad B=1+x^2+x^{13},
$$


the codes at $L=39$ and $L=78$ have parameters


$$
[[78,4,6]]\quad\text{and}\quad[[156,4,14]],
$$


respectively.

The covering conditions are immediate: $78=2\cdot39$, $m=1$ is unchanged, and every lifted monomial reduces to the corresponding base monomial. Indeed, the defining polynomials themselves are unchanged. These are precisely the polynomial and period conditions in Theorem 3.1. [SRB, supplied v3](../REFERENCES.md#ref-SRB)

### Dimension calculation

Put


$$
g=1+x+x^2.
$$


Polynomial Euclidean division gives


$$
\gcd(A,B)=g.
$$


Since $g$ divides both $x^{39}+1$ and $x^{78}+1$,


$$
H_0(C_L)=R_L/(A,B)
$$


has dimension two for either period. The simultaneous annihilator


$$
H_2(C_L)=\operatorname{ann}_{R_L}(A,B)
$$


also has dimension two. Euler characteristic therefore gives


$$
\dim H_1(C_L)=4.
$$



Independent binary row reduction gives


$$
\begin{array}{c|cc}
L&\operatorname{rank}H_X&\operatorname{rank}H_Z\\ \hline
39&37&37\\
78&76&76
\end{array}
$$


and hence $k=k_2=4$.

Neither example depends on disconnected components. The monomial differences $2$ and $13$ in $B$ generate the cyclic group at both periods, and the constant monomials connect the different check and qubit types.

### A weight-six base logical

Define


$$
\begin{aligned}
F&=1+x^{39},\\
z_L&=1+x^8+x^{16}+x^{25},\\
z_R&=1+x^{11},\\
c&=x^2+x^{11}.
\end{aligned}
$$


Direct multiplication in the ordinary polynomial ring gives


$$
\boxed{Az_L+Bz_R=Fc.}
\tag{1}
$$


Thus


$$
z=(z_L,z_R)
$$


is a base cycle of weight six.

Let $\omega^2+\omega+1=0$. Both $A$ and $B$ vanish at $x=\omega$, so both coordinates of every boundary vanish there. But


$$
z(\omega)=(\omega,\omega)\ne(0,0).
$$


Therefore $z$ is a nontrivial logical.

The exact exclusion of smaller logicals is given below; it establishes $d=6$.

### A weight-fourteen cover logical

Put


$$
R=x^9+x^{22}+x^{35}+x^{37}.
$$


A second ordinary polynomial identity is


$$
\boxed{
Az_L+BR+c=F(1+x^2+x^9).
}
\tag{2}
$$



Define the cover vector


$$
\boxed{
w=\bigl(x^{39}z_L,\ z_R+FR\bigr).
}
\tag{3}
$$


Using $x^{39}=1+F$, Equations (1) and (2) give


$$
\begin{aligned}
\widetilde\partial_1w
&=Ax^{39}z_L+B(z_R+FR)\\
&=F(c+Az_L+BR)\\
&=F^2(1+x^2+x^9).
\end{aligned}
$$


This vanishes in $R_{78}$, because


$$
F^2=1+x^{78}.
$$



The left support is


$$
\{39,47,55,64\},
$$


and the right support is


$$
\{0,9,11,22,35,37,48,61,74,76\}.
$$


Consequently,


$$
|w|=4+10=14.
$$



Most importantly,


$$
p(w)=z
$$


as a **literal chain**, not merely in homology. Since $p$ is a chain map and $[z]\ne0$, $w$ is nontrivial.

### The minimum base class is killed by transfer

This can be certified without inferring anything from dimensions.

Write


$$
A=ga,\qquad B=gb,\qquad F=gf.
$$


Since $\gcd(a,b)=1$, choose ordinary polynomials $U,V$ satisfying


$$
Ua+Vb=1.
$$


Also, $g\mid c$, because


$$
c=x^2(1+x^9).
$$


Dividing Equation (1) by $g$ therefore gives


$$
az_L+bz_R=0\pmod F.
$$



Set


$$
v=Uz_R+Vz_L\pmod F.
$$


Then


$$
bv=z_L\pmod F,\qquad av=z_R\pmod F.
$$


Now take the cover two-chain


$$
H=fv\pmod{F^2}.
$$


It satisfies


$$
\begin{aligned}
BH&=Fz_L\pmod{F^2},\\
AH&=Fz_R\pmod{F^2}.
\end{aligned}
$$


Hence


$$
\boxed{\widetilde\partial_2H=\tau(z).}
\tag{4}
$$



Thus


$$
\boxed{[z]\in\ker\tau_*=\operatorname{im}\beta_2.}
$$


The verifier computes the Bézout polynomials and checks Equation (4) directly.

## 3. Exact exclusion of all cover logicals of weight at most twelve

This is the computer-assisted part of the proof.

### Why circuit enumeration suffices

Call the support of a nonzero binary cycle a *circuit* if it contains no proper nonempty cycle support.

**Circuit reduction lemma.** A minimum-weight non-boundary cycle has circuit support.

Indeed, suppose a logical $y$ contains a proper nonempty subcycle $c$. If $c$ is nontrivial, it is a smaller logical. If $c$ is a boundary, then $y+c$ is a smaller representative of the same nonzero logical class. Both contradict minimality.

Therefore, to exclude logicals of weight at most twelve, it suffices to show that every circuit of weight at most twelve is a boundary.

Translations preserve cycles and boundaries and are transitive on each of the two qubit blocks. It consequently suffices to enumerate circuits containing the identity qubit in the left block and those containing the identity qubit in the right block.

### Completeness of the enumeration

The search maintains a chosen set $U$, a forbidden set $E$, and the syndrome


$$
\sigma=H_X1_U.
$$



When $\sigma\ne0$, choose an odd check. Any completion to a cycle must contain at least one additional available qubit incident to that check. Order those candidates. Branch on the first candidate belonging to the completion, forbidding earlier candidates in the later branches.

This partitions all possible completions: none is omitted.

The only nontrivial weight pruning condition is


$$
|\sigma|>3(b-|U|),
$$


where $b$ is the search bound. This is valid because every added column has weight three.

A branch stops when its syndrome becomes zero. That cannot truncate a proper subset of a circuit, by the definition of a circuit. Every zero-syndrome leaf is then tested directly for membership in the binary span of the boundary columns.

There is no heuristic decoder, floating-point optimization, assumed logical basis, or unproved pruning rule in this exclusion.

### Complete circuit classification

For the period-$78$ cover, the complete list of circuit types through weight twelve is as follows. Here $\widetilde\partial_2$ is the cover boundary map, and translations of the displayed vectors are understood.

| Weight | Translation-orbit representatives | Total distinct circuits |
|---:|---|---:|
| $6$ | $\widetilde\partial_2(1)$ | $78$ |
| $10$ | $\widetilde\partial_2(1+x^a)$, $a\in\{2,8,11,13,17,25\}$ | $468$ |
| $12$ | $\widetilde\partial_2(A)$, $\widetilde\partial_2(B)$, $\tau(z)$ | $195$ |

There are no circuits of any other positive weight at most twelve.

The first nine orbit types are manifest boundaries. The last type, $\tau(z)$, is a boundary by Equation (4). Its translation orbit has size $39$; the other nine orbits have size $78$. Thus all


$$
78+468+195=741
$$


circuits through weight twelve are boundaries.

For reproducibility, the direct $Z$-sector enumeration produced:

| Root | Search nodes | Zero-syndrome leaves | Non-boundary leaves |
|---:|---:|---|---:|
| Left identity | $985001$ | $3$ of weight $6$, $30$ of weight $10$, $66$ of weight $12$ | $0$ |
| Right identity | $991809$ | $3$ of weight $6$, $30$ of weight $10$, $56$ of weight $12$ | $0$ |

Some zero-syndrome leaves are not circuits; these are harmless additional checks. Filtering by


$$
\operatorname{rank}\bigl(H_X|_{\operatorname{supp}y}\bigr)=|y|-1
$$


and expanding translations gives exactly the classification above.

The base search through weight four finds no nonzero cycles.

Finally, every column has odd weight three, so every cycle has even weight. Consequently, there are no weight-five base cycles or weight-thirteen cover cycles. Combining the exclusions with the explicit witnesses,


$$
\boxed{d_Z=6,\qquad d_{Z,2}=14.}
$$



### The $X/Z$ issue

Let


$$
f^\star(x)=f(x^{-1}),\qquad
J(u,v)=(v^\star,u^\star).
$$


This is an invertible weight-preserving permutation. It sends a $Z$-cycle to an $X$-cycle because


$$
B^\star v^\star+A^\star u^\star=(Bv+Au)^\star.
$$


It sends a $Z$-boundary to an $X$-boundary:


$$
J(Bh,Ah)=(A^\star h^\star,B^\star h^\star).
$$


Therefore


$$
d_X=d_Z,\qquad d_{X,2}=d_{Z,2}.
$$


The program additionally checks both $X$-sector exclusions directly.

This completes the computer-assisted proof that


$$
\boxed{
[[78,4,6]]\longrightarrow[[156,4,14]]
}
$$


is a valid counterexample.

Exchanging $x$ and $y$ gives the corresponding counterexample with


$$
(\ell,m)=(1,39)\longrightarrow(1,78).
$$



## 4. The class-level variational formula is valid

The counterexample does **not** invalidate the proposed definition of $\mu$ or its second-order formula.

### Class-level variational theorem

Let $\alpha\ne0$ be projectable. Every cover chain has unique triangular coordinates $(q,r)$, with physical sheets $(q+r,r)$. It is a cycle precisely when


$$
\partial_1q=0,\qquad \partial_1r=D_1q.
$$


Its projected homology class is $[q]$. Therefore


$$
\boxed{
\mu(\alpha)=
\min_{\substack{\partial_1q=0,\ [q]=\alpha\\
\partial_1r=D_1q}}
\bigl(|q+r|+|r|\bigr)
}
\tag{5}
$$


is exactly the minimum over all cover cycles $y$ satisfying


$$
p_*[y]=\alpha.
$$


In particular, no choice of a literal projected representative is being fixed.

Now suppose


$$
\alpha=\beta_2[h],\qquad \partial_2h=0.
$$


Every representative of $\alpha$ has the form


$$
q=D_2h+\partial_2s.
$$


Using the audited identities,


$$
\begin{aligned}
D_1q
&=D_1D_2h+D_1\partial_2s\\
&=\partial_1E_2h+\partial_1D_2s.
\end{aligned}
$$


Hence a particular correction is


$$
r_0=E_2h+D_2s.
$$


Every other correction differs from it by an arbitrary base cycle. Thus every admissible pair, and only an admissible pair, has the form


$$
\boxed{
q=D_2h+\partial_2s,\qquad
r=E_2h+D_2s+c,\qquad c\in Z_1.
}
\tag{6}
$$


Substituting into the physical weight proves


$$
\boxed{
\begin{aligned}
\mu(\alpha)=
\min_{\substack{s\in C_2\\c\in Z_1}}
\Bigl(
&|D_2h+\partial_2s+E_2h+D_2s+c|\\
&+|E_2h+D_2s+c|
\Bigr).
\end{aligned}}
\tag{7}
$$



### Independence of the Bockstein preimage

Let $h'=h+g$ be another preimage. Then


$$
\partial_2g=0,\qquad D_2g=\partial_2u
$$


for some $u$.

Replace


$$
s\mapsto s+u,\qquad
c\mapsto c+E_2g+D_2u.
$$


The added term in $c$ is a cycle:


$$
\partial_1(E_2g+D_2u)
=D_1D_2g+D_1\partial_2u=0.
$$


These replacements preserve the actual $q$ and $r$. They therefore give a bijection between the two parameterizations and prove that Equation (7) is independent of $h$.

### What happens in the counterexample

For $\alpha=[z]$,


$$
\delta(\alpha)=6.
$$


Every cover cycle projecting to $\alpha\ne0$ is nontrivial, so the exact cover distance gives


$$
\mu(\alpha)\ge14.
$$


The explicit vector $w$ achieves weight fourteen and projects literally to $z$. Therefore


$$
\boxed{\mu(\alpha)=14>12=2\delta(\alpha).}
\tag{8}
$$



This is not confined to an unfortunate choice of minimum class. The base has exactly $39$ minimum logical representatives, all translates of $z$. They represent the three nonzero diagonal classes


$$
(\lambda,\lambda)\in\mathbb F_4^2,\qquad \lambda\ne0.
$$


All three are killed by transfer, and all three satisfy


$$
\delta=6,\qquad \mu=14.
$$



The four possible escape routes in the question are consequently excluded here. No other minimum class helps. A heavier representative cannot help. No alternative normal-form representative is omitted. A nonzero transfer-sector logical cannot have weight at most twelve either, because the exclusion covers **every** cover logical, not merely those with nonzero projection.

## 5. Exchange identities and the exact quotient-metric formulation

The coupled transformations remain useful, but they do not imply the proposed factor-two bound.

Let


$$
w_0=q+r,\qquad w_1=r.
$$


Adding a low-sheet cover boundary associated with $s\in C_2$ changes these sheets by


$$
b_0=(\partial_2+D_2)s,\qquad b_1=D_2s.
$$


The exact weight change is


$$
\boxed{
\Delta W=
|b_0|+|b_1|
-2\bigl(|w_0\cap b_0|+|w_1\cap b_1|\bigr).
}
\tag{9}
$$


This holds for a single elementary two-chain and for every sum of elementary two-chains.

For elementary $s$, the lifted trinomial Koszul boundary has weight six. Thus a weight-minimizing representative overlaps every elementary cover check in at most three positions. That is a necessary local condition, not a sufficient global metric estimate.

Adding $\tau(c)=(c,c)$, $c\in Z_1$, gives another exact identity:


$$
\boxed{
\Delta W=
2\left(
|c\setminus(\operatorname{supp}q\cup\operatorname{supp}r)|
-
|c\cap(\operatorname{supp}r\setminus\operatorname{supp}q)|
\right).
}
\tag{10}
$$



For the global quotient, define the binary subspace


$$
\mathcal K
=
\{y:\widetilde\partial_1y=0,\ py\in B_1\}.
$$


Exactness gives


$$
\boxed{
\mathcal K=\widetilde B_1+\tau Z_1.
}
\tag{11}
$$


Indeed, if $py=\partial_2s$, adding a lifted boundary makes its literal projection zero, after which it equals $\tau(c)$ for a base cycle $c$.

For any cover cycle $y_\alpha$ projecting to $\alpha$,


$$
\boxed{
\mu(\alpha)=\operatorname{dist}_H(y_\alpha,\mathcal K).
}
\tag{12}
$$


Thus the optimization really does include both the coupled boundary moves and the complete additional cycle freedom.

There is an exact binary dual:


$$
\boxed{
\mathcal K^\perp
=
\operatorname{im}\widetilde\partial_1^{\,T}
+\tau B_1^\perp.
}
\tag{13}
$$


For a candidate support $S$, a representative of the coset $y_\alpha+\mathcal K$ can be supported on $S$ if and only if


$$
a\cdot y_\alpha=0
$$


for every $a\in\mathcal K^\perp$ that vanishes on $S$. Consequently,


$$
\boxed{
\mu(\alpha)>b
\iff
\begin{array}{l}
\text{for every }S,\ |S|\le b,\text{ there exists }a\in\mathcal K^\perp\\
\text{with }a|_S=0\text{ and }a\cdot y_\alpha=1.
\end{array}}
\tag{14}
$$


This is an exact binary separation statement, rather than a dimension argument or an assumed real-valued norm duality.

There is also an exact circuit interpretation. Every binary cycle decomposes into support-disjoint circuits. Label each cover circuit by its projected homology class and assign it its physical weight. Then $\mu$ equals the shortest-path metric on the additive group of projectable classes generated by those labelled circuits. One inequality follows by taking symmetric differences of circuit representatives; the reverse follows by decomposing a minimum representative into disjoint circuits.

This interpretation was decisive in the search: in the counterexample, **every circuit through weight twelve is a boundary**, so neither a projected-class construction nor a transfer-sector construction can produce a logical within that budget.

## 6. The exact transformation in the previous family

Retain the previous notation


$$
q=3j,\qquad L=3q,\qquad X=x^q,\qquad
T=1+X+X^2,
$$


and


$$
z=(x+X,1+x),\qquad q_0=(T,T).
$$


Put


$$
\boxed{
s_j=x^2\,\frac{T+x^2+xX}{1+x+x^2}.
}
\tag{15}
$$


The numerator is divisible by $1+x+x^2$. This is an ordinary polynomial quotient, not division by a nonunit in the quotient ring.

Then, for every $j\ge2$,


$$
\boxed{
q_0+xz=\partial_2s_j.
}
\tag{16}
$$



Here is the polynomial verification. Since $B=x^{-2}g$ in the base ring, with $g=1+x+x^2$,


$$
Bs_j=T+x^2+xX.
$$


For the second coordinate, use


$$
\begin{aligned}
&(x^2+xX+X^2)(T+x^2+xX)
+g(T+x+x^2)\\
&\hspace{35mm}=(X+1)(X^3+1).
\end{aligned}
$$


Because $g\mid X+1$, division by $g$ leaves a multiple of the period polynomial $X^3+1$. Thus


$$
As_j=T+x+x^2,
$$


which proves Equation (16).

Now let


$$
P=1+x^{2q}+x^{4q}.
$$


The weight-six cover cycle


$$
(P,P)
$$


projects to $q_0$, so Equation (16) proves


$$
\mu([xz])=6.
$$


Translation gives


$$
\boxed{\mu([z])=6.}
$$



In triangular coordinates, that good lift is


$$
\boxed{(q,r)=\bigl(q_0,(X,X)\bigr).}
\tag{17}
$$


In particular,


$$
D_1q_0=\partial_1(X,X)\ne0.
$$


It is a one-per-fibre lift, but it is not a lift into the fixed low sheet.

Adding the cover boundary associated with $s_j$ turns Equation (17) into a pair with literal projection $xz$:


$$
\bigl(xz,\ (X,X)+D_2s_j\bigr).
$$


Conversely, an arbitrary correction for $xz$ differs from this correction by a base cycle. Equations (11) and (12) therefore capture exactly the freedom that keeps the class-level cost at six while the fixed-projection cost grows.

The invariant that remains small is


$$
\operatorname{dist}_H(y_\alpha,\widetilde B_1+\tau Z_1)=6,
$$


not $\nu(\alpha)$. For the specified class $[z]$, the complete low-sheet cycle space is two-dimensional; its three nonzero vectors have weights


$$
10j+2,\quad10j,\quad10j.
$$


Their class images give


$$
\nu([z])=10j
$$


for even $j$, and no vector in that class for odd $j$. The certificate package includes the explicit basis and a parameter-uniform polynomial-matrix verification of the two-dimensional kernel.

## 7. A smallest counterexample to the stronger $\nu$-inequality

The stronger inequality already fails at the smallest possible trinomial base size.

Take base period $3$,


$$
A=B=g=1+x+x^2,
$$


and cover period $6$,


$$
\widetilde A=x^2g,\qquad \widetilde B=g.
$$


These codes have parameters


$$
[[6,4,2]]\longrightarrow[[12,4,2]].
$$



For


$$
z=(x,1),
$$


the cover vector


$$
(x^4,1)
$$


is a weight-two cycle projecting to $z$. Also,


$$
\widetilde\partial_2(x+x^2)=\tau(z).
$$


Hence $[z]$ is killed, but


$$
\delta([z])=\mu([z])=2,\qquad \rho(z)=0.
$$



Nevertheless,


$$
\boxed{\nu([z])=\infty.}
$$



To see this, a fixed-low-sheet cycle has $\deg u,\deg v<3$ and satisfies


$$
g(x^2u+v)=0\pmod{x^6+1}.
$$


Since $\deg(x^2u+v)\le4$,


$$
x^2u+v
$$


must be either zero or


$$
\frac{x^6+1}{g}=1+x+x^3+x^4.
$$


The complete low-sheet cycle space is therefore generated by


$$
(1,x^2),\qquad(g,g).
$$


The latter is a base boundary, and the class of the former is not $[(x,1)]$. Thus the desired class has no representative satisfying $D_1q=0$.

This also shows why $\nu$ must be treated cautiously: unlike $\mu$, it depends on the particular physical section designated as “the low sheet.”

## 8. Exact metrics in the principal test cases

All $\nu$-values below use the standard low-monomial section in the stated presentation.

| Example and specified class | $\delta$ | $\rho$ of the specified minimum representative | $\mu$ | $\nu$ |
|---|---:|---:|---:|---:|
| Smallest $[[6,4,2]]\to[[12,4,2]]$, $z=(x,1)$ | $2$ | $0$ | $2$ | $\infty$ |
| Previous $[[30,4,4]]\to[[60,4,6]]$ example | $4$ | $1$ | $6$ | $20$ |
| Previous infinite family, $\alpha=[(x+x^{3j},1+x)]$ | $4$ | $2j-1$ | $6$ | $10j$ for even $j$; $\infty$ for odd $j$ |
| New $[[78,4,6]]\to[[156,4,14]]$ counterexample | $6$ | $4$ | $14$ | $22$ |

For the new counterexample, $\rho=4$ is certified by the explicit correction


$$
r=(z_L,R)
$$


and exhaustive exclusion of corrections with at most three positions outside $\operatorname{supp}z$, after quotienting syndromes by the support columns of $z$.

The value $\nu=22$ has a particularly direct polynomial certificate. Since both cover polynomials have degree below $39$, a low-sheet cycle satisfies


$$
Au+Bv=0
$$


as an **ordinary polynomial identity**: its syndrome has degree below $78$. Writing $A=ga$, $B=gb$, all such solutions are


$$
(u,v)=(bf,af),\qquad \deg f<16.
$$


The verifier exhausts all $2^{16}$ possibilities. Each of the three nonzero projectable classes has minimum low-sheet weight $22$.

The class-level variational theorem, coupled exchange identities, quotient metric, and binary dual formulation are all valid. What fails is the proposed universal metric estimate. There is no remaining lemma that can establish $d_2\le2d$ under the stated hypotheses: the unchanged-polynomial double cover above has $d_2=14>12$.

STATUS: CLASS_LIFT_INEQUALITY_FALSE
