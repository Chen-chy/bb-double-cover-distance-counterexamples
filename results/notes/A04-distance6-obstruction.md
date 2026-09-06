> **先看当前采用状态：** 小重量分类、单块定理和 Frobenius 机制应按各自范围引用；保留审计不等于重跑完整分类空间。
> [主报告](../../REPORT.md) · [逐项采用／排除表](../STATUS.md)。本篇为保留过程，不是整篇无条件有效的定理集合。

[全部研究结果](../README.md) · [逐项结论](../CLAIMS.md) · [原始完整文本](../../research/amplification/research/04_distance6_obstruction/REPORT.md)

> 完整研究笔记的 GitHub 阅读版；仅调整数学分隔符、引用标记与链接。历史状态、限制和证明内容均保留。当前结论以总登记表中的逐项状态为准；这里的“验证”不等于独立同行评审。

# A fixed-distance-six obstruction for binary BB double covers

## STATUS: FIXED_DISTANCE_OBSTRUCTION_PROVED

This round continues the supplied strict-trinomial BB amplification problem. It does not concern distance degradation. The new result is:

> **Theorem A (uniform, computer-assisted).** Every valid binary strict-trinomial BB double cover with positive base dimension satisfies
> 

$$
> \boxed{d=6\quad\Longrightarrow\quad d_2\le112.}
>
$$



The result includes univariate and bivariate codes, either doubled coordinate, even or odd periods, and term-matched changed-polynomial lifts. In fact, the proof works for arbitrary finite abelian double-cover homomorphisms with three distinct terms in each base check polynomial. The constant 112 is not claimed optimal.

The particularly relevant structural conclusion is stronger than the numerical bound: **a genuinely higher-free-rank mixed weight-six minimum circuit cannot generate amplification above two.** After excluding universal boundaries and cases that already have base distance at most four, its presentation has one of two forms: an odd-order-three symmetry or a matched-square relation. Both give a cover logical of weight at most twelve. The larger constant in Theorem A comes exclusively from bounded-size or bounded-width cases, and from the already bounded one-block case.

Two symbolic lemmas explain these higher-rank mechanisms: a general power-cycle lifting lemma and odd-subgroup descent. They are proved below, including their nonboundary assertions in the actual finite codes.

The result does **not** establish a finite universal amplification constant. The supplied record $C_*\ge7/3$, the connected $6\to14$ family, and the unresolved thresholds $7/3,5/2,3$ remain unchanged. No new exact distance record is claimed. Combining Theorem A with the supplied results at distances two and four excludes unbounded cover distance for every base distance at most six. Since all strict-trinomial cycle weights are even, eight is the next possible fixed base distance.

## 1. Conventions and source of the baseline

For a finite abelian group $G$, let $R=\mathbf F_2[G]$. The BB complex is


$$
R\xrightarrow{h\mapsto(Bh,Ah)}R^2
\xrightarrow{(u,v)\mapsto Au+Bv}R.
$$


The polynomials $A,B$ each have three distinct monomials. A logical is a cycle not of the form $(Bh,Ah)$. Group inversion and block exchange identify the X and Z distance problems, so the minimum nonboundary weight in this complex is the quantum distance. The dimension is $k=2\dim R/(A,B)$.

A double cover is an epimorphism $\widetilde G\to G$ with kernel $\{1,t\}$, together with term-matched polynomials $A',B'$. Put $\epsilon=1+t$. Then


$$
\epsilon^2=0,\qquad \operatorname{ann}_{\widetilde R}(\epsilon)=\epsilon\widetilde R.
$$


The transfer of a chain is $\epsilon$ times any lift, and its weight doubles. Projection is a chain map. Thus a lifted cycle whose projection is a base nonboundary cannot be a cover boundary.

The existing $7/3$ family, dimension relations, $d=2\Rightarrow d_2\le4$, $d=4\Rightarrow d_2\le48$, and the failure of the transfer-sector metric bound are taken from the supplied continuation materials and prior report. None is attributed here to a newly checked publication. The new distance-six proof below is otherwise self-contained, including a proof of the one-block estimate it uses.

Monomial gauges, block exchange, and common translations preserve distance. They will be used without identifying non-weight-preserving polynomial transformations with code equivalences.

## 2. A symbolic lifting lemma for matched Frobenius powers

This lemma is not restricted to six-column circuits.

**Lemma B (power-cycle lifting).** Let $m=2^a$, $n=2^b$, and suppose


$$
A^m=B^n
$$


in the base group algebra. Assume that the canonical cycle


$$
z=(A^{m-1},B^{n-1})
$$


is a nonboundary. Then every term-matched double cover has a nonboundary of weight at most


$$
\boxed{2(3^a+3^b).}
$$


In particular,


$$
\boxed{A^2=B^2,\ [(A,B)]\ne0\quad\Longrightarrow\quad d_2\le12.}
$$


The nonboundary hypothesis on the canonical cycle is essential; the equality of powers alone is not being treated as a certificate of that class.

### Proof

Because the base has a nontrivial logical, neither $A$ nor $B$ is a unit. Consequently $A^m=B^n$ has three distinct terms. If two of the three Frobenius images collided, the polynomial would reduce to a monomial; that would make $A$, and hence the code, invertible/trivial.

The three terms of $A'^m$ and $B'^n$ project to the same three distinct base terms. Therefore


$$
B'^n+A'^m=\epsilon D,
$$


where $D$ is a subset of the three monomials of $A'^m$.

If $D=0$, the cycle


$$
(A'^{m-1},B'^{n-1})
$$


projects to $z$, so it is nontrivial. If $D=A'^m$, then $B'^n=tA'^m$, and


$$
(tA'^{m-1},B'^{n-1})
$$


is a cycle with the same nontrivial projection.

Otherwise, $D$ has one or two terms. Consider


$$
Z=(\epsilon A'^{m-1},\epsilon B'^{n-1}).
$$


It is a cycle because $\epsilon(A'^m+B'^n)=0$. Suppose it were a boundary, so


$$
B'f=\epsilon A'^{m-1},\qquad
A'f=\epsilon B'^{n-1}.
$$


Multiplying the equations by $B'^{n-1}$ and $A'^{m-1}$, respectively, gives


$$
\epsilon Df=0.
$$


The second boundary equation also gives $\epsilon A'^m f=0$. Either $D$, or $D+A'^m$, is a monomial unit. Hence $\epsilon f=0$, and $f=\epsilon r$. Projecting the resulting equations yields


$$
B\,p(r)=A^{m-1},\qquad A\,p(r)=B^{n-1},
$$


contradicting the assumed nontriviality of $z$.

Finally,


$$
A'^{2^a-1}=\prod_{j=0}^{a-1} A'^{2^j}
$$


has at most $3^a$ terms, and similarly for $B'^{2^b-1}$. This proves the bound. It does not assume that the powers have the same Hamming weights before and after lifting. $\square$

For $m=n=1$, the lemma says that a mixed weight-two logical for monomial-equivalent checks has a cover logical of weight at most four. For $m=2,n=1$, it recovers the bound eight for $B=A^2$.

## 3. Odd symmetry descends the actual finite homology

**Lemma C (odd-subgroup descent).** Let $H\le G$ have odd order $h$. Suppose a finite base nonboundary $z$ is invariant under multiplication by every element of $H$. Its image in the quotient code on $G/H$ is a nonboundary of weight $\operatorname{wt}(z)/h$. Any logical of weight $w$ in the induced quotient double cover lifts to a logical of weight $hw$ in the original cover.

### Proof

Put $e_H=\sum_{g\in H}g$. Since $h$ is odd,


$$
e_H^2=e_H.
$$


The group algebra splits as $e_HR\oplus(1-e_H)R$, and $e_HR$ is isomorphic to $\mathbf F_2[G/H]$. The isomorphism sends a quotient monomial to its full $H$-coset sum. It is a chain map, with projection as a left inverse. It therefore injects on homology.

An invariant chain is a union of complete $H$-orbits in each qubit block. Its quotient weight is exactly its weight divided by $h$. If its quotient were a boundary, the invariant chain would be a boundary as well.

The full inverse image of $H$ in $\widetilde G$ has a unique odd-order subgroup $H_0$ mapping isomorphically onto $H$. Thus


$$
\widetilde G/H_0\longrightarrow G/H
$$


is a double cover. Applying the same coset-sum inclusion for $H_0$ injects its homology into the original cover and multiplies physical weight by $h$. $\square$

In the application here, $h=3$ and $z$ has weight six with three terms in each block. The quotient contains a mixed weight-two nonboundary. Its two check polynomials are monomial-equivalent; Lemma B with $m=n=1$ gives a quotient-cover logical of weight at most four. Lifting it gives


$$
\boxed{d_2\le12.}
$$



No strict-trinomial hypothesis is silently lost in this descent. If a quotient trinomial had colliding terms, it would become a monomial and hence a unit. The quotient code could not then have the nonboundary just established. Thus the relevant quotient checks are again strict trinomials.

## 4. Three bounds for low-complexity presentations

### 4.1 A polynomial in a finite subgroup

Suppose, after a monomial gauge, $A\in\mathbf F_2[H]$, with $|H|=s$. Then every positive-k finite BB code satisfies


$$
d\le s.
$$


Indeed, $\operatorname{ann}_R(A)$ is spanned by vectors supported in individual $H$-cosets, each of weight at most $s$. Its one-block logical quotient is


$$
\operatorname{ann}(A)/B\operatorname{ann}(A).
$$


This quotient is nonzero: its dimension equals the kernel dimension of multiplication by $B$ on $\operatorname{ann}(A)$, namely


$$
\dim(\operatorname{ann}(A)\cap\operatorname{ann}(B))
=\dim R/(A,B)=k/2>0.
$$


The last equality uses the nondegenerate pairing that extracts the identity coefficient of a product in the finite group algebra. Some local spanning vector therefore has nonzero image in the logical quotient.

In a double cover, the inverse image of $H$ has size $2s$, so


$$
d_2\le2s.
$$



### 4.2 A bounded-width cyclic strip

Suppose $G'$ has a subgroup $H'$ of size $h$ with cyclic quotient. Let $z$ lift a generator of that quotient. Assume monomial gauges put all check terms in


$$
\bigcup_{j=0}^{\rho}z^jH'.
$$


Then


$$
\boxed{d\le4h\rho.}
$$


There are $2h$ qubits per cyclic site. A boundary twist $z^M\in H'$ only permutes the qubits within one site. Both X and Z generators have cyclic support diameter at most $\rho$.

If the circle has fewer than $2\rho$ sites, its total size already proves the bound. Otherwise partition it into an even number of consecutive blocks, each with between $\rho$ and $2\rho$ sites. Such a partition exists by choosing $2\lfloor M/(2\rho)\rfloor$ blocks and distributing the sites evenly.

If $d>4h\rho$, every block is correctable. No check generator meets two distinct blocks of the same parity. A commuting Pauli supported on the even blocks therefore restricts to a commuting Pauli on each individual block; each restriction is a stabilizer. Their union is correctable, and the same is true of the odd blocks. Two complementary correctable regions contradict $k>0$.

For completeness, the cleaning fact just used follows from finite-dimensional symplectic linear algebra. If $S$ is the stabilizer subspace and $V_E$ the coordinate space of a correctable region, then


$$
S^\perp\cap V_E=S\cap V_E.
$$


The orthogonal complement of the projection of $S$ to $V_E$ is $S^\perp\cap V_E$. Thus the restriction of any logical lies in that projection and can be removed by a stabilizer. Cleaning from one correctable region into its correctable complement would make every logical trivial.

In particular, if a base presentation is $U=\mathbf Z\oplus T$, and $\rho$ is the maximal exponent span of its two polynomials in a primitive free coordinate, every finite double cover satisfies


$$
\boxed{d_2\le8|T|\rho.}
$$


The image of $T$ has at most $|T|$ elements; its full cover preimage has at most $2|T|$ elements. The lifted free generator supplies the cyclic site coordinate. This construction allows nonsplit group extensions and arbitrary additional finite quotient relations.

### 4.3 One-block logicals of fixed weight

If a nonboundary is supported in one block and has weight at most $w$, then


$$
\boxed{d_2\le2w^2.}
$$


Choose a nonboundary circuit of weight $w'\le w$. Each positive check degree in its support is two, because there are only three possible incident columns from that block. The paired incidence graph is a connected cubic graph on $w'$ vertices.

Normalize the trinomial to $1+a+b$. A spanning tree expresses all column positions in the two generators $a,b$; non-tree edges give relations. Let $U$ be the resulting presented abelian group. The circuit supplies a nonzero annihilator of $1+a+b$ in $\mathbf F_2[U]$.

Write $U=T\oplus\mathbf Z^r$. If the three terms have different free exponents, a linear functional makes one term uniquely maximal. Its coefficient in $\mathbf F_2[T]$ is a group monomial, hence a unit. Such a Laurent polynomial is a non-zero-divisor, contradicting the annihilator. All terms have the same free exponent; because $a,b$ generate $U$, it follows that $U$ is finite.

Each fundamental graph cycle has length at most $w'$. Its relation vector lies in $w'$ times the hexagon with vertices


$$
(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1).
$$


Two vectors in this hexagon have determinant of absolute value at most one. Two independent fundamental relations therefore have determinant at most $(w')^2$. The index of the full relation lattice divides that determinant, so $|U|\le(w')^2$. The polynomial support in the actual base lies in an image of this finite group. Section 4.1 proves the cover bound.

For $w=6$, this gives $d_2\le72$, independently of the mixed-circuit classification.

## 5. The complete six-column presentation calculation

### 5.1 Why these presentations are exhaustive

A minimum nonboundary has circuit support. Otherwise split a dependent support into proper disjoint cycles; at least one must remain a nonboundary, contradicting minimality. Every cycle has even weight because every column has odd weight three.

For a mixed circuit of weight six, the possible support types up to block exchange are


$$
(5,1),\qquad(4,2),\qquad(3,3).
$$


Pair the incidences at each touched check. No pair joins two incidences of the same column, because check monomials are distinct. The pairing graph is a connected loopless cubic multigraph on six vertices. A disconnected component would itself specify a proper nonempty cycle. This remains true when a check originally had degree four or six.

Normalize the supports to


$$
A=\{0,a_1,a_2\},\qquad B=\{0,b_1,b_2\},
$$


and the first selected column position to zero. There are four monomial-difference generators and five other column-position generators. A paired incidence imposes


$$
p_i+q_{t_i,c}-p_j-q_{t_j,e}=0.
$$


Nine pairings give nine integer relations. A spanning tree eliminates the five positions and leaves a four-by-four relation matrix $R$ on $a_1,a_2,b_1,b_2$. The universal group is


$$
U=\mathbf Z^4/\operatorname{rowspan}_{\mathbf Z}R.
$$


Every actual finite circuit with that pattern gives a homomorphism $U\to G$. Additional finite coincidences impose extra quotient relations, not new uncovered cases. In a connected normalized base component, the four check differences generate the component, so this map is surjective.

There are 640 connected loopless labeled cubic multigraphs on six vertices. Globally permuting the three A terms and the three B terms allows the incidence permutation at the first vertex of each block to be fixed. The remaining four permutations give $6^4=1296$ checks per graph and support type. Thus the normalized implementation checks


$$
3\cdot640\cdot1296=2,488,320
$$


presentations.

The independent implementation does not use that graph count or normalization. It directly enumerates all 11,608,920 perfect pairings of the eighteen labeled incidences with no same-column pair, for each of the three support types. This gives 34,826,760 checks. Of these, 11,314,080 pairings per support type have connected pairing graphs.

### 5.2 Rank-zero and rank-one bounds

Write $r=\operatorname{rank}_{\mathbf Z}U$. For $r=0$, $|U|=|\det R|$. For $r=1$, write $U=\mathbf Z\oplus T$, choose a primitive integer null vector $w$ of $R$, and define


$$
\rho=\max\{\operatorname{span}(0,w_1,w_2),
\operatorname{span}(0,w_3,w_4)\}.
$$


The complete calculations give:

| Mixed support | Maximum finite order for r=0 | Maximum torsion order times range for r=1 |
|---|---:|---:|
| (5,1) | 12 | 10 |
| (4,2) | 24 | 14 |
| (3,3) | 27 | 12 |

These bounds were checked before removing invalid-term or non-circuit presentations, so they hold on a superset of the admissible inputs.

The rank-one quantity is computed exactly in the independent verifier. The torsion order is the greatest common divisor of all three-by-three minors of $R$. A nonzero cofactor vector divided by its coordinate gcd gives the primitive free vector $w$. The normalized implementation separately bounds the quantity using the cofactor vectors from the four triples of rows.

For rank zero, the base component has at most 27 group elements and its double cover at most 108 physical qubits. This gives $d_2\le108$ without invoking a sharper coding bound. For rank one, Section 4.2 gives


$$
d_2\le8|T|\rho\le112.
$$



### 5.3 Higher-rank cases and explicit algebraic certificates

Reject a presentation if two check terms coincide in $U$, or if the six selected columns fail to have binary rank five. These tests are necessary: a forced term collision cannot become a strict trinomial in a quotient, and a proper universal subcycle would remain a proper subcycle of any actual six-column circuit.

A one-generator cofactor boundary is then removed. For every remaining higher-rank presentation, exact integer quotient arithmetic gives one of the following certificates:

| Case | (5,1) | (4,2) | (3,3) |
|---|---:|---:|---:|
| Unit trinomial | 120 | 0 | 36 |
| Sum of two boundaries | 0 | 192 | 0 |
| Frobenius square | 0 | 24 | 0 |
| Odd-order-three invariant cycle | 0 | 0 | 50 |
| Single-involution offset | 0 | 0 | 234 |
| Polynomial supported in an order-three subgroup | 0 | 0 | 16 |
| Sum of three boundaries | 0 | 0 | 6 |
| Matched-square canonical cycle with two involutions | 0 | 0 | 6 |

These are 684 retained labeled presentation checks, not inequivalent codes. Every one has free rank exactly two; no admissible higher-free-rank alternative remains after the stated boundary filters.

Here are the meanings and uses of the certificates.

**Unit cases.** Two terms of a polynomial differ by an involution. After a monomial factor the polynomial is $1+u(1+h)$, with $h^2=1$; its square is one. Thus $k=0$. If the involution collapses in a finite quotient, the same expression is still a unit.

**Boundary sums.** The certificate stores an explicit two-term or three-term polynomial $f$ satisfying $(u,v)=(Bf,Af)$ in the universal group algebra. Such a cycle remains a boundary in every finite quotient. The two-boundary cases were precisely why removing only single cofactor vectors was insufficient.

**Square cases.** After monomial gauges and block exchange, $B=A^2$. Positive dimension then supplies the nonboundary $(A,1)$ of weight four. These cases cannot have minimum distance six.

**Single-involution offset.** After gauges,


$$
A=1+x+y,\qquad B=1+x+hy,\qquad h^2=1.
$$


For nonidentity $h$, put $N=1+h$. The weight-four cycle $(N,N)$ is nontrivial whenever $k>0$. If it were a boundary from $f$, then $Nyf=0$, so $f=Nr$. The remaining equation implies $1\in(A,N)=(A,B)$, a contradiction. If $h=1$, the checks are equal and $(1,1)$ is a weight-two logical. These cases are therefore excluded by $d=6$, without requiring a cover argument.

**Finite-polynomial cases.** One normalized check lies in a subgroup of order at most three. Section 4.1 gives base distance at most three. These cannot have $d=6$.

**Odd-three cases.** The universal torsion group has order three, the check supports become monomial-equivalent in the free quotient, and the actual six-term cycle is invariant under its order-three translation. The invariant-cycle equality is checked in the full integer group, not only in a rational free quotient. Lemma C gives $d_2\le12$.

**Double-involution cases.** The universal group has torsion $C_2\times C_2$. The certificate gives a monomial gauge and common translation for which


$$
A^2=B^2,\qquad (u,v)=(A,B).
$$


In other words, it certifies the selected circuit itself as the canonical matched-square cycle, not merely an equality between the check squares. Since the selected finite cycle is a nonboundary, Lemma B applies and gives $d_2\le12$.

All these assertions are in the full presented abelian group. None discards two-primary torsion or assumes semisimplicity over characteristic two.

## 6. Completion of the distance-six theorem

Choose a weight-six minimum nonboundary in a positive-k base component.

If it is one-block, Section 4.3 gives $d_2\le72$. If it is mixed, form its incidence presentation. Rank zero gives $d_2\le108$; rank one gives $d_2\le112$. At higher rank, the complete certified list in Section 5.3 either contradicts minimum distance six or supplies a cover logical of weight at most twelve. Therefore


$$
\boxed{d=6\Longrightarrow d_2\le112.}
$$



For a disconnected code, after monomial gauges the check differences generate a subgroup whose cosets are isomorphic components. A cover component maps to a base component with degree one or two. Degree one gives an isomorphic distance-six component; degree two is covered by the argument above. Hence connectedness is not required.

The proof constructs or guarantees an actual finite cover nonboundary in every case. It does not infer finite nontriviality from an infinite-strip class. It does not control only transferred sectors. In Lemma B, one branch uses projection and another proves transfer survival; Lemma C constructs a quotient-cover logical and lifts it through an odd subgroup; the low-rank cases use finite-code correctability.

## 7. Verification, exactness, and reproducibility

The independent all-pairings verifier reports the following classification counts after its different enumeration and boundary tests:

| Case | (5,1) | (4,2) | (3,3) |
|---|---:|---:|---:|
| Unit | 1,080 | 0 | 324 |
| Two-boundary sum | 0 | 864 | 0 |
| Square | 0 | 864 | 0 |
| Odd-three invariant | 0 | 0 | 288 |
| Single involution | 0 | 0 | 2,592 |
| Finite polynomial | 0 | 0 | 576 |
| Three-boundary sum | 0 | 0 | 216 |
| Double involution | 0 | 0 | 216 |

It also removes invalid terms, non-circuits, and single boundaries explicitly. The different counts are expected: one method normalizes global term permutations and uses multigraph edge lists, while the other counts all labeled perfect pairings, with different multiplicities from parallel edges.

`enumerate6_bounded.cpp` uses a fixed spanning tree for each normalized graph and exact minors. `verify6_all_pairings.cpp` uses neither the supplied graph list nor its normalization. It eliminates positions with additive-potential union-find and computes integer quotient coordinates through separate unimodular row/column operations. It computes rank-one torsion-range products using all minors. Both are exhaustive and have no node or time stopping rule.

A third check, `verify_presentations_sympy.py`, reconstructs the full nine-generator, nine-relation incidence matrix for every retained higher-rank presentation. SymPy Smith normal form independently confirms its rank and torsion order; Hermite normal form checks the relation map. This covers all 684 retained normalized checks.

The symbolic power-cycle lemma was additionally tested on 4,000 finite term-matched covers in 125 base instances where its canonical base cycle is nontrivial. Both doubling directions and even/odd periods were exercised. The branches were:

| Branch | Finite checks |
|---|---:|
| Identical lifted powers; nontrivial projection | 938 |
| Deck-associated lifted powers; nontrivial projection | 174 |
| Nontrivial transfer, checked by exact boundary membership | 2,888 |

These 4,000 checks are witness/homology tests, not exact distance computations and not a search for a new amplification record. All their reported cover vectors are checked against independently constructed finite boundary spaces.

The artifact contains complete source code, exact presentation certificates, output logs, and a reproduction script. The standalone C++ all-pairings verifier needs no Python package. The normalized verifier requires Python; the third arithmetic check requires SymPy. `run_all.py` reproduces everything. No solver estimate, floating-point rank, or decoder failure is used.

“Computer-assisted theorem” here means a symbolic reduction plus supplied exhaustive finite calculations. It does not mean a proof-assistant formalization, an independent human referee report, or a claim of literature priority.

## 8. What was not proved, and what failed

No finite universal bound on $C_*$ was obtained. The supplied $7/3$ infinite family remains the record established in this research program. No exact example above $7/3$, $5/2$, or $3$ was constructed in this round; no claim about their optimality follows from the new fixed-distance theorem.

A preliminary attempt to treat every higher-rank presentation through a general Laurent-trinomial common-factor theorem was not used in the proof. Handling the full torsion coefficient ring requires more than a torsion-free factorization argument. The completed six-column calculation instead supplies exact finite group-algebra identities, including the exceptional two-primary cases.

The first coarse high-rank filter was insufficient: six-term circuits can be sums of two or three BB boundaries, even when they are not single cofactor boundaries. Explicit short boundary multipliers eliminated these cases. A failed intermediate classification check also exposed the three-boundary sums among the order-three presentations; they were corrected and certified, not silently retained as logicals.

It would also be wrong to infer $d_2\le12$ merely from $A^2=B^2$. The selected canonical cycle must be nontrivial, and the classification explicitly verifies that it is the selected logical in the double-involution case. No universal claim is made for arbitrary classes from that polynomial relation alone.

The constant 112 leaves a large gap from the known lower bound 14 for the optimal fixed-distance-six cover bound. Closing that numerical gap is distinct from deciding whether bounded base distance can give unbounded cover distance. Theorem A settles the latter question at base distance six.

## 9. A precise next obstruction: finite survival of compact cover homology

The first remaining fixed base distance is eight. One-block circuits are already bounded by Section 4.3. For any fixed weight, there are finitely many incidence presentations. Rank-zero cases have bounded group order, and rank-one cases have bounded torsion-width products. Thus the unresolved fixed-distance-eight mechanism is mixed and higher rank.

Here is a module-theoretic reduction that does not ask only about transfer.

Fix an eight-column incidence presentation $U$, with its distinguished cycle $z$. For each choice of relation parities $\sigma$, form an abelian lift $\widetilde U_\sigma$ by adjoining $t$, imposing $2t=0$, and replacing each incidence relation $r_i=0$ by


$$
r_i=\sigma_i t.
$$


Discard choices forcing $t=0$. Every compatible finite double cover of a quotient of $U$ is a quotient of one such lift: lift the four check differences and the seven column positions, and record the deck parity of each relation.

Let $\mathcal C_\sigma$ be the BB complex over $\mathbf F_2[\widetilde U_\sigma]$. This coefficient ring is Noetherian, because $\widetilde U_\sigma$ is finitely generated abelian. Consequently $H_1(\mathcal C_\sigma)$ has a finite set of module generators represented by finite-support cycles.

Consider the following **unproved compact-survival lemma**, restricted to the remaining mixed higher-rank eight-column cases:

> For every compatible finite quotient double cover with base distance eight, if the distinguished base cycle remains a nonboundary, then
> 

$$
> \operatorname{im}\!\left[
> H_1(\mathcal C_\sigma)\longrightarrow H_1(C(\widetilde Q))
> \right]\ne0.
>
$$



This statement concerns the actual finite specialization of the entire compact cover homology. It does not assert that the transfer of the selected base cycle survives.

If this lemma holds for all remaining presentations, it implies a finite uniform bound at base distance eight. Choose finite-support module generators for each of the finitely many lifted presentations and take the largest of their weights. A nonzero specialized image forces at least one generator to remain nontrivial, supplying a cover logical with that bound. This is a conditional argument, not a proof of the lemma.

Conversely, in a fixed-pattern family with $d_2\to\infty$, every finite-support generator must eventually specialize to a boundary. Thus the entire displayed image must eventually be zero while the distinguished base logical still survives. Finding an expensive transferred class alone does not meet this necessary condition.

Even a counterexample to compact survival at one finite quotient would not by itself prove unbounded amplification. A genuine construction would additionally need a family excluding short winding cycles. For a sequence of quotients whose injectivity radii in the fixed lifted presentation tend to infinity, every circuit of any fixed weight eventually lifts to a compact circuit; if all compact homology images vanish, this would give the required growing distance. These additional hypotheses are not supplied by the present results.

**Single next target:** prove or refute the compact-survival lemma for the remaining mixed higher-rank eight-column presentations. It directly tests the full finite cover homology, including sectors unrelated to transfer, and it is the precise point at which a fixed-distance counterexample must defeat the new obstruction method.
