# A weight-eight quotient bound for strict-trinomial BB codes

**Principal status: D2_EQ_8_UNBOUNDED_BASE_EXCLUDED.**

## 1. The result, its scope, and its dependencies

**Theorem 1 (computer-assisted).** Let \(\pi:\widetilde G\twoheadrightarrow G\) be a surjection of finite abelian groups. Let \(\widetilde A,\widetilde B\in\mathbb F_2[\widetilde G]\) each have exactly three supported monomials, and suppose their images \(A,B\in\mathbb F_2[G]\) also each have exactly three supported monomials. Assume that the base code has positive dimension. Then

\[
 d(\widetilde Q)=8\quad\Longrightarrow\quad d(Q)\le96.
\]

In particular, a valid strict-trinomial binary BB double cover satisfies

\[
 \boxed{d_2=8\Longrightarrow d\le96.}
\]

Thus **96 is a valid universal choice of \(D_8\)**. It is not asserted to be the least such choice. The proof actually does not require that the kernel of the group projection have order two.

Theorem 1 is proved below independently of the earlier weight-six classification and of the earlier weight-two/weight-four exclusions. Those earlier results enter only the following combined consequences:

\[
 \boxed{d>96\Longrightarrow d_2\ge10,}
\]

and

\[
 \boxed{\gamma_-^{(3)}(N)\ge\min\{1/12,20/N\}.}
\]

In particular, \(\gamma_-^{(3)}(N)\ge20/N\) for \(N\ge240\). The previously supplied \(6/7\) upper construction is retained as an input, not independently distance-certified here. Combining it with the new bound gives

\[
 20/N\le\gamma_-^{(3)}(N)\le6/7\qquad(N\ge636).
\]

This note proves neither a universal positive lower constant nor a vanishing-ratio family. The smallest bounded cover distance not yet excluded for unbounded base distance is now ten. This is an exclusion frontier, not an existence claim.

The BB complex and termwise cover convention are those of Symons, Rajput, and Browne, *Sequences of Bivariate Bicycle Codes from Covering Graphs*, arXiv:2511.13560v3, Section 2.4 and Theorem 3.1. For the new proof it suffices to use the more general finite-abelian quotient formulation above.

## 2. Algebraic setup

For a finite abelian group \(G\), write \(R=\mathbb F_2[G]\). Use

\[
 R\xrightarrow{\partial_2}R^2\xrightarrow{\partial_1}R,
 \qquad
 \partial_2s=(Bs,As),\qquad \partial_1(u,v)=Au+Bv.
\]

Physical weight is the sum of the two monomial-support weights. Group inversion, followed by interchange of the two qubit blocks, identifies the two CSS homologies weight-preservingly. Thus the two CSS distances agree.

The same inversion and block interchange show that the two check ranks agree. Consequently, with \(M=|G|\),

\[
 k=2M-2\operatorname{rank}[A\ B]
   =2\dim_{\mathbb F_2} R/(A,B).
\tag{1}
\]

In particular, positive dimension is equivalent to the ideal \((A,B)\) being proper.

Multiplying either check polynomial by a monomial is a weight-preserving chain equivalence. More explicitly, if \(A'=mA\) and \(B'=nB\), the qubit map \((u,v)\mapsto(m^{-1}u,n^{-1}v)\), together with the coefficient map \(s\mapsto(mn)^{-1}s\), is a chain isomorphism. Such normalizations commute with the group quotient when the normalizing monomials are projected as well.

We can therefore normalize the checks to

\[
 A=1+a_1+a_2,\qquad B=1+b_1+b_2.
\]

Exponent relations below are integral relations in an abelian group; they are not linear relations modulo two.

Two elementary observations will be used. First, the augmentation of each strict trinomial is one, so every cycle has even physical weight. Second, a term difference of two-power order makes a trinomial a unit. Indeed, after division by its remaining monomial, the polynomial has form \(1+u(1+t)\), where \(t\) has two-power order. The second summand is nilpotent, so this polynomial is invertible. Such a check cannot occur in a positive-dimensional code.

## 3. Minimum logicals give a finite presentation problem

### 3.1 Circuit support, without any small-weight exclusion hypothesis

Let \(Y\) be a minimum-weight nonboundary cycle. Its support contains no nonzero proper subcycle. Otherwise, if \(Z\) is such a subcycle, both \(Z\) and \(Y+Z\) are smaller cycles. At least one must be a nonboundary, since their sum is the nonboundary \(Y\). This contradicts minimality.

Thus a minimum logical has circuit support for the syndrome matrix. This argument does not require that every small cycle be nontrivial or that small boundaries have already been classified.

For a weight-eight cycle, there are 24 syndrome incidences. Pair incidences at each syndrome location. Multiplicities four, six, or higher are handled by arbitrary pairings at that location.

The resulting graph on the eight selected qubits is cubic. It has no loops, because the three terms of each check are distinct. It is connected, because any connected component would give a subcycle. A triple edge would isolate two vertices, so all edge multiplicities are at most two.

Consequently every minimum weight-eight logical is represented by a connected, loopless cubic multigraph on eight vertices with edge multiplicities at most two.

### 3.2 The presentation associated with a pairing

Choose the left/right block of each vertex and label its three incident ports by the three terms of the appropriate polynomial. For an edge joining ports \(i,j\) at vertices \(r,s\), impose

\[
 t_r+c_{r,i}=t_s+c_{s,j}.
\tag{2}
\]

A spanning tree determines seven relative qubit positions after setting the root position to zero. The remaining five edges give five integral relations on the four normalized translation generators \(a_1,a_2,b_1,b_2\). Therefore a mixed-block pairing gives

\[
 H=\mathbb Z^4/L,
\tag{3}
\]

where \(L\) is generated by five explicit relation rows.

Every actual finite realization is a quotient of this group on its normalized translation subgroup. Extra syndrome coincidences are further quotient relations and are not omitted. The projected base is another finite quotient of the same \(H\).

A pure-block pairing uses only the two translation differences of one check, giving \(H_A=\mathbb Z^2/L_A\).

### 3.3 Elementary shortening

Every elementary boundary has weight six. If such a boundary \(b\) overlaps a weight-eight logical \(Y\) in at least four qubits, then

\[
 |Y+b|=8+6-2|Y\cap b|\le6.
\tag{4}
\]

It represents the same nonzero homology class, contradicting minimum distance eight. Hence every relevant weight-eight logical overlaps every elementary boundary in at most three qubits.

This test is valid in any further admissible quotient: the elementary boundary still has six distinct physical qubits, and existing overlaps persist. We never infer that a cycle is a logical merely because it passes this test.

## 4. Exact enumeration and its separate verification

### 4.1 Graph and port completeness

There are **168,840 labelled connected graphs** of the required kind, in **20 graph-isomorphism classes**.

The generator in `graphs_eight.cpp` enumerates degree-three adjacency matrices with entries zero, one, or two, checks connectedness, and forms vertex-permutation orbits.

A separate checker, `verify_graphs.py`, establishes completeness differently. A cached degree-sequence recurrence counts 170,555 labelled cubic multigraphs of this type on eight vertices in total, of which 168,840 are connected. It independently checks pairwise nonisomorphism and all automorphism groups of the 20 representatives, and verifies

\[
 \sum_{\text{representatives }\Gamma}\frac{8!}{|\operatorname{Aut}(\Gamma)|}
 =168840.
\]

It also independently checks all block-colouring orbits.

After graph automorphisms, and block exchange in the balanced case, there are **877 mixed colourings**. A global permutation and monomial normalization of each check's three terms fixes the port permutation at one vertex of each block. Thus each mixed colouring has \(6^6\) normalized port assignments:

\[
 877\cdot6^6=40,917,312.
\]

The pure case has one global term-permutation normalization and therefore

\[
 20\cdot6^7=5,598,720
\]

assignments. Parallel-edge port orderings are not silently identified; the port enumeration covers them.

### 4.2 Separating free ranks

For mixed presentations, an exact modular-rank screen over \(\mathbb F_{101}\) separates most relation-rank-at-least-three cases. A rank at least three modulo 101 is a rigorous certificate of integral rank at least three. All cases not so certified undergo integer row reduction. The full run checks that none of these remaining cases has integral relation rank three or four. Thus no case is lost between the two scans.

The finite/strip scan retains **44,619 distinct relation lattices** before admissibility filtering:

| Free rank of \(H\) | Retained lattices | Verified maximum relevant bound |
|---|---:|---:|
| 0 | 36,590 | \(|H|\le56\) |
| 1 | 8,029 | \(4|T|R\le96\) |

Keeping inadmissible presentations in this part only enlarges the bound; it cannot omit a physical code.

The higher-free-rank scan discards formally repeated terms, repeated physical qubits, and checks that are units by the two-power criterion. After exact lattice and translated-cycle normalization, it retains **312 presentation–cycle pairs**. These are not claimed to be fully isomorphism-reduced.

Their independently verified classification is:

| Category | Pairs | Consequence |
|---|---:|---|
| Elementary-boundary overlap at least four | 279 | Cannot be a minimum weight-eight logical |
| Monomial-associated check squares | 5 | Base distance at most 6 |
| Cyclic order-four relative check twists | 5 | Base distance at most 8 |
| Explicit universal boundaries | 12 | Boundary in every finite realization |
| One check supported on a group of order six | 6 | Base distance at most 6 |
| Involution-twisted square, including untwisted cases | 5 | Base distance at most 8 |
| Unresolved | 0 | |

The last row of algebraic cases consists of four ordinary Frobenius-multiple cases and one genuinely involution-twisted case.

Every retained pair of free rank at least three is in the elementary-shortening category. All 33 nonshortenable survivors have free rank two.

### 4.3 What the independent arithmetic checkers establish

`verify_highrank.py` reconstructs the original five relation rows from the stored graph, colouring, and port assignment for every retained pair. It verifies the integral lattice using Smith decompositions and unimodular transformations, checks the zero syndrome and translation normalization, recomputes all elementary overlaps, and verifies either the precise algebraic identity or an explicit coefficient filling.

`verify_low_and_pure.py` uses independently implemented integer determinants and greatest common divisors of minors for all 44,619 finite/strip lattices. It reconstructs the five original relation rows. Inclusion in the displayed lattice, equality of rank, and equality of saturation index certify equality of the original and displayed lattices. It then independently recomputes every primitive free coordinate and distance bound.

All arithmetic is exact. The C++ row operations are instrumented with checked 128-bit intermediates and explicit bounds before determinant evaluation; completion of the full run checks that these bounds are never exceeded. The Python verifiers use unbounded integers.

The retained catalogue hashes are:

- `highrank_eight.tsv`: `f327dabff670a0c513f07dac76d104252aaacd63fd6a6971992ba7bfeeab9132`;
- `low_free_lattices.tsv`: `4df3bebab227c231f186b553f335e6caca5c592a5120bfce86690a82d4628d43`;
- `pure_eight.tsv`: `53cac389e0de7eedc0788c2585e977ae709b157b1051b49a0cc132bc79fef92a`.

The hashes check reproduction, not mathematical correctness by themselves. Completeness comes from the circuit/pairing argument and the exhaustive graph, colouring, and port loops; the separate arithmetic verifiers check the retained certificates and all numerical bounds.

## 5. Finite and one-dimensional presentations force bounded base distance

### 5.1 One check supported on a finite subgroup

**Lemma 2.** If, after monomial normalization, one check is supported on a subgroup \(K\le G\), and \(k>0\), then

\[
 d\le |K|.
\tag{5}
\]

The group algebra is free over \(\mathbb F_2[K]\), so \(\ker A\) has an \(R\)-module generating set with each generator supported in one \(K\)-coset and of weight at most \(|K|\).

Positive dimension implies \(\ker A\cap\ker B\ne0\): transpose the nonsurjective map \([A\ B]\) and apply group inversion. Hence multiplication by \(B\) on the finite-dimensional space \(\ker A\) is singular and is not onto. Its image is an \(R\)-submodule. At least one of the stated generators, say \(u\), is outside \(B(\ker A)\). Then \((u,0)\) is a nonboundary cycle of weight at most \(|K|\).

Taking \(K=G\) also gives the universal BB bound \(d\le n/2\).

If the universal mixed group \(H\) is finite, both normalized checks are supported in its finite image in the base. Lemma 2 gives \(d\le|H|\le56\), even if the full Tanner graph has multiple components.

### 5.2 Rank-one presentations

Write

\[
 H=T\oplus\mathbb Z,
\]

and let \((v_1,v_2,v_3,v_4)\) be the primitive free coordinates of \(a_1,a_2,b_1,b_2\). Define

\[
 R=\max\bigl\{\operatorname{span}(0,v_1,v_2),
                 \operatorname{span}(0,v_3,v_4)\bigr\}.
\]

**Lemma 3.** Every positive-dimensional finite realization satisfies

\[
 d\le4|T|R.
\tag{6}
\]

A finite image is a cyclic strip, possibly with a torsion-twisted end identification, with at most \(|T|\) group elements and \(2|T|\) qubits per cell. Both stabilizer types can be made to have free-coordinate span at most \(R\) simultaneously. To see this, shift left-block qubits by minus the lower endpoint of the \(B\)-support and right-block qubits by minus the lower endpoint of the \(A\)-support. The two parts of a Z check then have the same lower endpoint; the two parts of an X check have the same upper endpoint.

If the circumference is below \(2R\), Lemma 2 already gives the desired bound. Otherwise partition the circle into an even number of alternating intervals, each of length between \(R\) and \(2R\). Such a partition is obtained by starting with \(2\lfloor P/(2R)\rfloor\) intervals of length \(R\) and distributing the remainder without exceeding \(2R\) per interval.

If \(d>4|T|R\), each interval is correctable because it contains fewer than \(d\) qubits. No stabilizer generator intersects two intervals of the same colour: the closest sites across an intervening interval of \(R\) cells are separated by \(R+1\).

The union of the intervals of one colour is therefore correctable. A Pauli supported on that union and commuting with every generator has separately commuting restrictions on the intervals; each restriction is a stabilizer. The same holds for the complementary colour. Cleaning a nontrivial logical off the first correctable colour would place it in the other correctable colour, a contradiction.

For completeness, cleaning follows from symplectic linear algebra. If a logical's restriction to a correctable region were not the restriction of a stabilizer, a separating linear functional on that region would give a Pauli supported there which commutes with every stabilizer but anticommutes with the logical. Correctability would make that Pauli a stabilizer, contradicting the logical's commutation with all stabilizers.

The exact maximum of (6) over the entire retained rank-one list is 96.

An independent way to compute this bound avoids rational arithmetic. For an integer basis of a rank-three relation lattice, form the alternating vector \(c\) of its four maximal minors. Then

\[
 \gcd(c_1,c_2,c_3,c_4)=|T|,
 \qquad v=c/|T|,
\]

up to an overall sign. Thus \(4|T|R\) is directly computable from the spans of the entries of \(c\). The independent verifier also computes the indices from the original five rows, rather than trusting the basis conversion.

### 5.3 Pure-block presentations

A normalized trinomial over a finitely generated abelian group generated by its two term differences is a nonzerodivisor whenever that group has positive free rank. Indeed, project its three terms to the free part. If at least two projected points differ, choose an integer linear functional for which one term has a unique maximal value. When two projected terms coincide, choose the unique third term to be maximal. Viewing the ring as a Laurent polynomial ring in that direction, the leading coefficient is a monomial and hence a unit. Multiplication by the trinomial is injective.

If all three projected points coincide, the group generated by the normalized term differences is finite. Consequently every admissible pure-block universal eight-cycle forces a finite check-translation group.

The pure enumeration retains twelve presentation–cycle pairs. Their groups are exactly

\[
 C_{12},\quad C_2\times C_6,\quad C_{14},\quad C_{15}.
\]

Thus Lemma 2 gives \(d\le15\), or \(d\le14\) using evenness. This is substantially below the mixed strip bound.

## 6. The algebraic cases of free rank two

These proofs concern actual finite group algebras. They do not infer nontriviality from a formal infinite presentation.

### 6.1 Associated squares

**Lemma 4.** If the squares of two strict-trinomial checks are monomial-associated and \(k>0\), then \(d\le6\).

Their squared supports are still strict trinomials: a cancellation would make the square, and hence the original check, a unit. Match squared terms and normalize one matched pair. It is enough to consider

\[
 B=1+x+y,\qquad A=1+tx+sy,
 \qquad t^2=s^2=1.
\]

Set \(C=A+B\). If \(C=0\), there is a weight-two logical. Otherwise the weight-six vector \((A,B)\) is a cycle. Under the change of coordinates \((u,v)\mapsto(u+v,u)\), the complex has check pair \((B,C)\), boundaries \((Cr,Br)\), and this cycle is homologous to \((0,C)\).

At any common maximal ideal of \((B,C)\), one has

\[
 \operatorname{Ann}(C)=CR.
\tag{7}
\]

Here and below annihilator statements can be localized at that maximal ideal. If \(t,s\) generate \(C_2^2\), put \(e=1+t,f=1+s\). The ring is free over \(\mathbb F_2[e,f]/(e^2,f^2)\), and \(C=ex+fy\). From \(Cr=0\), reduction modulo \(f\) gives \(r=ea+fb\). Then \(ef(ya+xb)=0\), so \(ya+xb=ec+fd\). Solving for \(b\) shows

\[
 r=C(x^{-1}a+fx^{-2}c),
\]

proving (7). If the involution subgroup has order two, \(C\) is an involutory nilpotent times \(x\), \(y\), or \(x+y\). The first two are units, and \(x+y=1+B\) is a unit at the common maximal ideal, giving the same conclusion.

If \((0,C)\) were a boundary, \(Cr=0\) and \(Br=C\). Equation (7) gives \(r=Ca\), then \(C(Ba+1)=0\), so \(Ba+1\in CR\). This contradicts that \(B,C\) lie in the chosen maximal ideal. Hence the weight-six cycle is nontrivial. The identity persists under projection to the base.

### 6.2 A cyclic two-power twist lemma

The following statement is useful beyond weight eight.

**Lemma 5.** Let \(t\) have two-power order in a finite abelian group, and suppose

\[
 B=1+x+y,\qquad A=1+t^a x+t^b y.
\]

If the code has positive dimension, then

\[
 \boxed{d\le2|\langle t^a,t^b\rangle|.}
\tag{8}
\]

If the subgroup is trivial, the checks agree and \((1,1)\) is a weight-two logical. Otherwise write the subgroup as \(\langle s\rangle\) of order \(M=2^r\), and write the two coefficients as \(s^\alpha,s^\beta\), with at least one of \(\alpha,\beta\) odd.

Put

\[
 e=1+s,\qquad J=1+s+\cdots+s^{M-1}=e^{M-1}.
\]

Then \((J,J)\) is a cycle of weight \(2M\). Write

\[
 C=A+B=eF.
\]

Modulo \(e\), \(F\) is \(x\), \(y\), or \(x+y\). At a common maximal ideal of \(A,B\), these are units, because \(x,y\) are monomials and \(x+y=1+B\). Therefore \(F\) is a unit after localization.

Freeness over \(\mathbb F_2[\langle s\rangle]\) gives

\[
 \operatorname{Ann}(e)=e^{M-1}R,
 \qquad \operatorname{Ann}(e^{M-1})=eR,
\]

and these identities survive localization. If \((J,J)=(Br,Ar)\), then \(Cr=0\), hence \(r=Jq\). The equation \(Br=J\) yields \(J(Bq+1)=0\), so \(Bq+1\in eR\), impossible at the common maximal ideal. Thus the cycle is nontrivial.

All five order-four survivors have the form in Lemma 5, after monomial normalization and matching of the free-coordinate supports. Their torsion generator has order dividing four in every projected base, so (8) gives \(d\le8\).

This explicitly handles loss of order under projection. If a four-term norm projects to zero because the order-four generator becomes an involution, one uses the shorter norm of the image subgroup. One does not assume that the original witness survives projection.

### 6.3 An involution-twisted Frobenius square

**Lemma 6.** Suppose

\[
 A=1+x+y,\qquad B=1+t(x^2+y^2),\qquad t^2=1.
\]

For a positive-dimensional code, \(d\le8\). If \(t=1\), the stronger bound \(d\le4\) holds.

When \(t=1\), \(B=A^2\), and \((A,1)\) is a nonboundary cycle: a boundary representation with second entry one would make \(A\) invertible.

Otherwise let \(e=1+t\), so \(e^2=0\). The vector

\[
 W=(eA,e)
\tag{9}
\]

has weight at most eight and is a cycle, since

\[
 B+A^2=e(A^2+1),\qquad A(eA)+Be=0.
\]

If \(W=(Br,Ar)\), then \(Ar=e\) and \((B+A^2)r=0\). Localize at a common maximal ideal of \(A,B\). The factor \(A^2+1\) is a unit there, so \(er=0\). Freeness over the involution subgroup gives \(\operatorname{Ann}(e)=eR\); hence \(r=eq\). The equation \(Ar=e\) forces \(Aq+1\in eR\), a contradiction at that maximal ideal.

The identity projects to the base. If the involution is killed, the untwisted weight-four logical replaces (9). Again, the proof does not require that the projected cover witness be nontrivial, or even nonzero.

### 6.4 The remaining finite-check and boundary cases

Six survivors have one check supported on a torsion group of order six. Lemma 2 bounds the base distance by six.

The twelve remaining survivors have explicit coefficient fillings over their universal groups, each using three or four checks. The verifier multiplies the displayed coefficients by both check polynomials and obtains the candidate vector exactly. Therefore these candidates remain boundaries in every finite quotient.

An illustrative four-check identity is

\[
 A=1+x+x^2,\qquad B=1+y+y^2,\qquad s=(1+x)(1+y),
\]

for which

\[
 \partial_2s=
 \bigl((1+x)(1+y^3),(1+x^3)(1+y)\bigr).
\tag{10}
\]

This is a weight-eight boundary in the universal Laurent ring, although no elementary boundary overlaps it in more than two qubits. Thus passing elementary shortening does not certify a logical. Its finite realizations do not evade Theorem 1.

## 7. Proof of Theorem 1 and the new degradation bound

Take a minimum weight-eight cover logical, normalize its checks, and form one of its connected incidence pairings. The complete enumeration applies.

A pure case forces a finite check-translation subgroup and base distance at most 14. A mixed free-rank-zero case gives base distance at most 56. A mixed free-rank-one case gives base distance at most 96.

Among higher-free-rank cases, elementary shortening contradicts that the cover logical has minimum weight eight; universal boundaries contradict its nontriviality. Every remaining algebraic identity gives an actual nontrivial base logical of weight at most eight by Lemmas 2, 4, 5, or 6. Therefore the largest bound over all cases is 96.

This argument uses the cover-to-base map only to pass the universal exponent relations to a further finite quotient. It does not use the degree of the cover. This proves the stronger quotient theorem and, in particular, the desired double-cover statement.

To derive the ratio bound, now combine Theorem 1 with the earlier supplied exclusions:

- for \(d\le4\), the ratio is at least \(1/2\);
- for \(4<d\le56\), \(d_2\ge6\), giving ratio at least \(3/28\);
- for \(56<d\le96\), \(d_2\ge8\), giving ratio at least \(1/12\);
- for \(d>96\), evenness and the exclusions of cover distances two, four, six, and eight give \(d_2\ge10\). Since \(d\le n/2\), the ratio is at least \(20/n\).

Taking the infimum over \(n\le N\) gives

\[
 \gamma_-^{(3)}(N)\ge\min\{1/12,20/N\}.
\]

The earlier exact \(14\to12\) family gives the retained upper bound \(6/7\) for \(N\ge636\); no new exact-distance ratio record is claimed here.

## 8. Finite sanity checks, boundaries of the result, and reproduction

The uniform nilpotent proofs were also tested by independent binary matrix calculations in `verify_nilpotent_lemmas.py`. These tests verify zero syndrome, positive dimension, and nonboundary status. They do not claim exact minimum distances.

The cyclic two-power lemma was checked for 340 coefficient choices, with subgroup orders 2, 4, 8, and 16. The involution-twisted-square check covers 3,520 strict-trinomial instances on the tested finite groups; 2,912 have positive dimension, and every such witness was independently verified to be nontrivial.

No decoder output, unsuccessful distance search, or numerical stabilization is used in the uniform theorem. No family with growing base distance and vanishing ratio has been constructed. The earlier unbounded-filling example and the failure of the two-check filling lemma remain unchanged; they are not used to infer degradation here.

Run `bash run_all.sh` to regenerate the graph representatives, colourings, all mixed and pure port scans, and the separate arithmetic verifications. `verification_summary.json` records the final accounting and hashes. Auditing only the retained certificates is available by running the Python verifier scripts, but is not a substitute for the full enumeration when checking completeness.

The proof is computer-assisted, not a proof-assistant formalization or an external referee report. It supplies the full source, deterministic catalogues, original graph/port identifiers, independently implemented arithmetic checks, and the mathematical arguments that apply each certificate uniformly to all finite quotients.

**Next precise lemma.** There exists a finite constant \(D_{10}\) such that every valid strict-trinomial binary BB double cover with positive-dimensional base and \(d_2=10\) satisfies \(d\le D_{10}\).

## References and retained inputs

1. Benjamin C. B. Symons, Abhishek Rajput, and Dan E. Browne, *Sequences of Bivariate Bicycle Codes from Covering Graphs*, arXiv:2511.13560v3. Used for the BB and termwise covering conventions.
2. Sergey Bravyi and Barbara M. Terhal, *A no-go theorem for a two-dimensional self-correcting quantum memory based on stabilizer codes*, arXiv:0810.1983. Standard cleaning/locality background; the particular strip bound used here is proved explicitly above.
3. Supplied strict-trinomial research brief and preceding weight-six certificate. The previous small-distance exclusions and exact \(14\to12\) family are inputs to the combined degradation bounds, not inputs to Theorem 1 itself. The retained weight-six presentation verifier was rerun successfully in this work.
