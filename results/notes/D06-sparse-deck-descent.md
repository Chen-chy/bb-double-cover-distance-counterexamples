[全部研究结果](../README.md) · [逐项结论](../CLAIMS.md) · [原始完整文本](../../research/degradation/research/06-sparse-deck-descent/proof.md)

> 完整研究笔记的 GitHub 阅读版；仅调整数学分隔符、引用标记与链接。历史状态、限制和证明内容均保留。当前结论以总登记表中的逐项状态为准；这里的“验证”不等于独立同行评审。

# Sparse physical descent for a deck involution

Date: 2026-09-06

Principal status: **TRINOMIAL_STILL_OPEN**.

This note proves a uniform quadratic physical replacement theorem for one
subclass of the remaining visible-2-primary obstruction. It neither proves nor
refutes the global assertion `d <= C d_2^2`. The inherited global cubic theorem
and asymptotic degradation bounds are not re-proved here.

## 1. Conventions and the new theorem

For a group algebra R, write K(A,B;R) for the complex

    R --(B,A)^T--> R^2 --[A B]--> R.

Weights always count nonzero coefficients in the original binary monomial
basis, in both qubit blocks. Strict trinomials have exactly three distinct
supported terms in each actual code. The quotient must match those terms
individually; equality after polynomial reduction alone is not enough.
These are the group-algebra and covering conventions of [1].

A **compact cycle** here means a finite-support cycle over the specified
infinite group algebra, subsequently mapped into the actual finite code.
It does not mean every finite-code homology class. In particular, this note
never identifies compact homology with all homology after specialization.

### Theorem 1 (physical quadratic descent for a deck involution)

Let

    H = T x C_2(s) x Z(z),

where T is a finite abelian group of odd order. Suppose the four normalized
check term differences generate H. Let

    H -> G_tilde -> G

be finite realizations, with the second map having kernel of order two.
Assume s maps to the nonidentity element of that kernel. The actual base and
cover checks must both be strict trinomials with valid termwise matching.
Let Y be a finite-support universal cycle whose image upstairs is a
nonboundary, and whose projection downstairs is a boundary. If the universal
weight of Y is w, then an explicit physical binary base nonboundary Z can be
constructed with

    |Z| <= 3 w^2.

The minimum weight of the base is therefore at most 3 w^2. In particular,
if a minimum cover logical of weight w=d_2 has a weight-preserving incidence
lift satisfying these hypotheses, then

    d <= 3 d_2^2.

No assertion is made that every cover circuit has such a presentation.
The required hypothesis is about the group in which the short cycle lifts,
not just about the abstract local module of the actual finite code.

The bound does not require Y to be a distinguished transfer representative,
or require transfer to be injective. Arbitrary boundary adjustments to Y are
allowed. The construction does not Fourier-transform the physical chain,
compute an idempotent, or divide a physical polynomial by a gcd.

### Scope

If formal 2-primary torsion has larger order but its entire actual image is
exactly the deck subgroup C_2, factor out the invisible part first. Likewise,
odd torsion killed in the actual cover may first be factored out. These
factorizations preserve a weight-preserving incidence lift: a collision
there would also be a collision in the actual physical support.

The theorem does NOT cover:

* an involution retained in the base, with the cover doubling a period;
* a larger visible 2-primary subgroup;
* a finite, rather than virtually cyclic, incidence presentation.

In particular, the first of these is already a genuine remaining case; see
Section 8 for an exact warning against applying the operator in the wrong
quotient.

## 2. Sparse normalization

Set S=F_2[T][z,z^{-1}], so F_2[H]=S[s]/(s^2+1).
Multiplying a defining check by a monomial, with the corresponding
monomial block/check shifts, preserves physical weights and the code.
Exchange the checks when needed.

A strict trinomial has either no relative s-dependence or a 2+1 split by
s-parity. In the latter case, multiplying it by s if needed, and dividing by
the monomial in its singleton part, puts it in the form s+a, where a is a
binomial. At least one check has such a split, since otherwise the term
differences would not generate the C_2 factor.

We can therefore write

    A_tilde = s+a,
    B_tilde = b+s c,
    c in {0,1}.

Here a has two terms; b has two terms when c=1 and three when c=0.
The actual base checks are

    A = 1+a,             B = b+c.

Introduce the auxiliary polynomial

    C = b+ac = B+cA.

It has at most four terms. It is not a new physical defining check. The
physical base code is still defined by the original strict trinomials A,B.
The elementary shear

    Theta(u,v) = (u+c v,v)

identifies K(A,B) with K(A,C). Its inverse is the same shear; it increases
weight by at most a factor two.

Call a normalized check **free-primitive modulo two** when at least one of
its free term differences is odd. The four term differences generate the
free Z factor, so some check is free-primitive. If a twisted check is
free-primitive, choose it as A_tilde. Otherwise there is just one twisted
check and the untwisted check B=C is free-primitive. Both cases are proved
below.

## 3. An explicit universal chain contraction

Split a universal chain as

    u = u_0+s u_1,       v = v_0+s v_1,

and define

    Phi_1(u,v) = (U,V) = (u_1+c v_1, v_0+a v_1).

The effective complex over S is K(A^2,C). A direct expansion of the two
s-coefficients in A_tilde u+B_tilde v gives

    A^2 U+C V=0

for every universal cycle. Conversely, put

    Psi_1(U,V) = (A_tilde U+cV, V).

This takes effective cycles to original universal cycles. For a cycle Y,

    Y + Psi_1 Phi_1(Y) = partial_2(v_1).

Thus these maps identify universal H_1, by an explicitly sparse homotopy.
For completeness, the other chain maps are

    Phi_2(h_0+s h_1)=h_1,
    Phi_0(q_0+s q_1)=q_0+a q_1,
    Psi_2(h)=A_tilde h,
    Psi_0(q)=q.

For an arbitrary chain Y with syndrome q_0+s q_1, not necessarily a cycle,

    Y + Psi_1 Phi_1(Y) = partial_2(v_1)+(q_1,0).

This is the full degree-one homotopy identity. Also Phi Psi is the identity.

Projection, after the base shear, and transfer, after contraction, have
particularly simple formulas:

    p_red(U,V) = (A U,V),
    tau_red(X,H) = (X,A H).

These are universal chain-map formulas. They do not assert that every
finite quotient complex is the effective complex over the base coefficient
ring. That assertion is generally false for a nonproduct period.

### Physical weight bounds

Translate Y by s if necessary so that its s-odd sheet contains at most w/2
qubits. Translation preserves its nonzero homology class and the condition
that its projection is a boundary. Put u=|U| and v=|V|. Then

    u <= w/2,       v <= 3w/2,       u v <= 3w^2/4.

Indeed, U uses only the odd-sheet coefficients, while V uses v_0 plus at most
two translates of v_1. No quotient or local-coordinate sparsity assumption
is used here.

## 4. Coefficient selectors and the first physical replacements

The squaring map is a permutation of T because T has odd order. Every
f in S has a unique expression

    f = C_0(f)^2 + z C_1(f)^2.

To compute C_i(f), keep only the terms with z-exponent congruent to i modulo
two, subtract i from that exponent, halve it, and take the unique square
root of its T-coordinate. This is an actual operation on binary supported
monomials, including negative Laurent exponents. In particular,

    |C_i(f)| <= |f|,
    C_i(g^2 f) = g C_i(f).

For clarity write

    C = c_0^2+z c_1^2,
    T_i = C_i(UV).

Multiplying A^2 U+C V=0 by V and applying the two selectors proves

    A T_i = c_i V.                                    (4.1)

If A is a nonzerodivisor, multiplying this identity by C and cancelling A
also proves

    A(c_i U)+C T_i=0.

Consequently the original physical base vector

    Z_i = (c_i U+c T_i, T_i)                          (4.2)

is a cycle. Its transfer, in the effective coordinates, is exactly

    tau_red(c_i U,T_i)=(c_i U,A T_i)=c_i(U,V).

Therefore, whenever c_i is a monomial, Z_i is a base nonboundary: its
transfer is a monomial translate of the nonzero cover class. This argument
uses neither transfer injectivity nor survival of the projection of Y.
Its weight satisfies

    |Z_i| <= |c_i| u+(1+c)u v.                        (4.3)

### The nonprimitive twisted-check corner

If the twisted check is not free-primitive, the untwisted C=B is primitive.
Its normalized three terms occupy both parity classes, one of which is a
single monomial. Select that class in (4.2).

One must NOT cancel A blindly: it can vanish identically in an odd-character
component. Work only for this verification in the decomposition of
F_2[T] into finite fields. In every component C is a nonzero Laurent
polynomial. Where A=0, the universal cycle equation forces V=0; hence T_i=0,
and the proposed base cycle still has zero syndrome. In every other
component cancellation is valid. This establishes (4.2) globally.

Thus the singleton construction already proves the required quadratic
bound in the nonprimitive corner. The verifier includes an example with
A=1+t+t^2, t^3=1, where A really is zero in a nontrivial character component.

## 5. A derivative replacement that detects ramified compact loss

It remains to treat a free-primitive twisted check. Let

    D = z d/dz.

On the binary monomial basis, D simply discards the terms of even free
exponent. It does not increase weight. Since D(C)=z c_1^2, differentiating
the effective cycle equation and using (4.1) gives

    A X+C H=0,

where

    X = A D(U)+z c_1 T_1,
    H = D(V).

Thus the explicit original physical base vector is

    Z_D = (A D(U)+z c_1 T_1+c D(V), D(V)).             (5.1)

It uses only coefficient selection, monomial multiplication, multiplication
by checks with bounded support, and the single product UV. The latter is
the sole source of a quadratic weight cost.

Zero syndrome is not the main issue. The next section proves that (5.1)
is an actual base nonboundary whenever the finite cover class survives but
its projection is a boundary. In particular, it detects the double-root
sectors for which both singleton-free Cartier replacements can disappear.

## 6. Nontriviality after actual finite specialization

This section uses field components and gcds only as certificates. None of
these operations is used to construct the binary vector (5.1).

### 6.1 Squarefreeness supplied by a strict trinomial

In a finite-field component K of F_2[T], a normalized primitive check is

    A=1+alpha z^i+beta z^j,

with alpha,beta nonzero, and at least one of i,j odd. If exactly one is odd,
D(A) is a monomial. If both are odd, D(A)=A+1. Hence, at every nonzero root of
A, D(A) is nonzero. The polynomial A is nonzero and squarefree (or a unit)
in K[z,z^{-1}]. Repeated free exponents and cancellations in an odd-character
component do not invalidate this argument.

Work in one such Laurent PID component. Set

    g=gcd(A,C),        g_+=gcd(A^2,C),
    ell=g_+/g,        r=g/ell,
    a_1=A/g,          c_1'=C/g.

All gcds may be chosen monic after clearing Laurent units. Squarefreeness of
A implies ell divides g, and g=r ell is squarefree. In particular r and ell
are coprime. Every universal effective cycle has the form

    (U,V)=((c_1'/ell) k, r a_1^2 k),                  (6.1)

and its universal homology class is k modulo g_+.
The base K(A,C) generator is (c_1',a_1), with coefficient modulo g.
Projection of (6.1) has base coefficient

    r a_1 k.                                        (6.2)

The derivative cycle in (5.1), before undoing the shear, has base coefficient

    a_1 D(r k).                                     (6.3)

Indeed its second coordinate is D(r a_1^2 k)=a_1^2 D(rk), and the first is
then fixed by the cycle equation. This also handles C=0.

### 6.2 The finite period, including a nonproduct seam

First quotient any odd torsion invisible in the actual cover. Then T and s
inject upstairs, and every remaining finite realization has a presentation

    G_tilde = <T,s,z | s^2=1, z^P=s^epsilon t_0>,
    G       = <T,z   | z^P=t_0>,

with epsilon in {0,1} and t_0 in T. This follows by taking the least positive
free exponent of a relation; after removing its torsion value it generates
the relation kernel.

The Laurent polynomial

    F_s=z^P+s^epsilon t_0

is a nonzerodivisor on S[s]/(s^2+1), since its highest coefficient and constant
coefficient are units. The short exact sequence of free complexes for
multiplication by F_s gives a natural injection

    M/F_s M -> H_1(K(A_tilde,B_tilde; R/(F_s))),

where M is universal H_1. This is the compact image, not the full finite
homology. It is the relevant portion of the long exact homology sequence
for a short exact sequence of complexes [2].

Multiplication by A_tilde is nullhomotopic on its Koszul complex; therefore
s acts on M as a. The actual compact cover image in the field component is

    K[z,z^{-1}]/(g_+, z^P+a^epsilon t_0).

The compact base image is

    K[z,z^{-1}]/(g, z^P+t_0).

At every root of g, A=0 and a=1. Thus an active cover factor is also an
active base factor. Naturality makes the compact projection the coefficient
map (6.2).

### 6.3 Factorwise nonboundary certificate

Because Y is nonzero in finite homology and is compact, choose an
irreducible factor q where its compact cover class is nonzero.
There are two possibilities.

**q divides r.** Its exponent in g_+ is one. Hence k is nonzero modulo q.
The polynomial r is squarefree, so D(r) is nonzero modulo q. Formula (6.3)
is therefore

    a_1 D(r) k != 0 mod q.

**q divides ell.** Its exponent in g_+ is two. Formula (6.2) and the
hypothesis that the base projection is a boundary force q to divide k.
For the cover class still to be nonzero, its finite compact factor must
retain exponent two, and k must have q-adic valuation exactly one.
Therefore D(k) is nonzero modulo q, while r and a_1 are units there.
Formula (6.3) becomes

    a_1 r D(k) != 0 mod q.

In either case the compact base class of Z_D is nonzero. Since the compact
image injects into actual finite H_1, Z_D is an actual physical base
nonboundary.

This proof is deliberately sensitive to the finite quotient. Merely
showing a universal class nonzero would not suffice. It also explains why
the derivative is necessary: it removes the single q factor from a
ramified kernel coefficient without dividing the physical chain by q.

## 7. The uniform constant

When a parity part c_i of C is a monomial, use Z_i. Its weight is at most

    u+2uv <= w/2+3w^2/2 <= 3w^2.

When all free exponents in C are even, c_1=0 and (5.1) is linear-cost.
When all are odd, (4.1) and the original cycle equation imply

    z c_1 T_1=A U,

by cancellation of the nonzerodivisor A. Then X=A(DU+U), also linear-cost.
These two cases cost at most 3u+2v <= 9w/2.

The only remaining parity pattern for a polynomial with at most four
supported terms is 2+2. In that case |c_1|=2, and

    |Z_D| <= 3u+2uv+2v
           <= (3/2)w^2+(9/2)w
           <= 3w^2                 for w>=4.

Every universal strict-trinomial cycle has even weight, by augmentation.
For w=2 one may argue directly. A cross-block two-cycle forces the actual
checks to be monomial-associated, and a positive-dimensional base then has
a weight-two logical. A same-block two-cycle makes its three-term support
invariant under a translation of order three; this subgroup survives an
order-two quotient. The normalized check is a monomial times 1+t+t^2,
and ker(A) is generated as a group-algebra module by 1+t. Positive dimension
makes multiplication by the other check non-surjective on this kernel,
so the weight-two generator is a nonboundary. Thus d<=2 in this case too.

This completes Theorem 1 with the universal constant 3.

## 8. An exact counterfamily attempt in the remaining period-doubling case

The next example disproves an extension of the replacement operator, not
quadratic distance descent. It also shows why a compact kernel witness is
not enough: a different base class can stay uniformly short.

Let H=C_2(s) x Z(z) and use unchanged checks

    A_tilde=s+z+z^2,
    B_tilde=s+z^7+z^8.

Set

    p=1+z+z^2,
    a=z+z^2,
    C=z+z^2+z^7+z^8=p^2 D_0,
    D_0=z+z^2+z^3+z^4.

The universal contraction is K(p^2,p^2 D_0), whose compact H_1 is
S/(p^2). The universal physical cycle

    X=((s+a)D_0+1,1)

has weight eight and represents coefficient 1. Explicitly its first block
has s-even support {0,2,6} and s-odd support {1,2,3,4}. Put

    Y=pX.

It has weight fourteen and represents coefficient p. Its first block has
s-even support {0,1,3,4,6,7,8} and s-odd support {1,3,4,6}; its second block
is p.

For every odd P>8 divisible by 3, take the rectangular, term-preserving cover

    C_2(s) x C_P(z) <- C_2(s) x C_{2P}(z).

In BB period notation this is (2,P)->(2,2P). The involution s is retained in
the base; the deck transformation is z^P. The checks have three distinct
terms in both actual groups. No term is cancelled. Their normalized
translations generate both groups.

The compact base image is S/(p), since p has multiplicity one in z^P+1.
The compact cover image is S/(p^2), since the cover period is (z^P+1)^2.
Therefore X is a nonboundary both downstairs and upstairs, while Y is a
nonboundary upstairs and becomes a boundary downstairs.

In fact, with

    u_P = (p+z(z^P+1))/p^2,

one has the exact base coefficient filling

    Y=partial_2(u_P A_tilde) mod (z^P+1).

The quotient is an ordinary polynomial: write P=3J with J odd, so
(z^P+1)/p=(1+z) sum_{i=0}^{J-1} z^{3i}; modulo p, multiplication by z sends
this to 1. Hence the numerator is divisible by p^2.

Eliminating s from the check ideal gives

    R/(A_tilde,B_tilde) = S/(p^2, z^P+1)

in the base, and the analogous doubled period in the cover. Their dimensions
are 2 and 4, so the parameters established here are

    base:  [[4P,4,d]],     d<=8,
    cover: [[8P,8,d_2]],   d_2<=8.

These are upper bounds, NOT claimed exact distances. Y is not a minimum
cover logical, since X is shorter. This family does not yield a vanishing
ratio or an unbounded-distance base.

### The derivative operator has the wrong target for this family

Applying (5.1) to Y yields the physical vector appropriate to the quotient
s=1. Its coordinates are

    (z+z^2+z^4+z^5+z^7, z).

In the actual base, where s remains nontrivial, its syndrome is

    (1+s)(z^2+z^4+z^5+z^7),

which is nonzero for every P>8. Thus it is not even a cycle there.

This is a direct algebraic counterexample to silently extending Theorem 1
to retained-involution period doubling. The obstruction is a change of the
physical target code, not just a missing homology-dimension argument.

### A limited further reduction within product period doubles

When A is primitive, the effective compact annihilator gcd(A^2,C) has
multiplicities at most two. For a product base period z^P+t_0 with P even,
every period factor has multiplicity at least two, so passing to the square
of that period does not enlarge the compact image. Its projection is
injective. If the untwisted C is primitive instead, the compact gcd is
squarefree and the same injectivity holds for any product period.

Thus the simplest remaining product-period case already has P odd, a
primitive twisted A, and a squared common factor of A^2 and C. The example
above lies precisely there. Twisted seams and larger visible 2-primary
subgroups are not claimed resolved by this observation.

## 9. Exact verification

`verify.py` uses two representations. Universal polynomials are sets of
Laurent monomials, with exact symmetric-difference addition. Independently,
finite multiplication and boundary columns are bit-packed binary vectors;
boundary membership uses exact Gaussian elimination. No decoder or
floating-point distance computation is used.

The executed record contains:

* 96 full universal chain-homotopy and projection/transfer diagram tests;
* 299 finite tests, including 93 cases where the cover class is a nonboundary
  and its actual base projection is a boundary;
* among those 93, 74 derivative cases and 19 singleton-Cartier cases;
* 22 odd-torsion cases and 22 nonproduct-period cases;
* four cases where A vanishes identically in a character component;
* a successful case with negative Laurent exponents;
* all 93 successful witnesses have identical universal and finite weights;
* successful covers as large as 1,260 qubits.

The tests include arbitrary added universal boundaries before constructing
the replacement. For all successful cases, the output was independently
checked for zero actual base syndrome, exclusion from the actual base
boundary span, and the stated weight bound.

The retained-involution family was checked at P=9,15,21,33,45,63. Exact
binary ranks give k=4 and k_2=8. The weight-eight class, the weight-fourteen
kernel class, the explicit filling, and the nonzero wrong-target syndrome
were all checked.

These computations check the symbolic theorem; they are not a complete
classification and do not certify any new exact minimum distance. The
argument has not been externally refereed or formalized in a proof assistant.

## 10. Global status and the next sharply defined problem

The global quadratic theorem is neither proved nor refuted here. The
inherited global theorem remains d<=4d_2^3. In particular, no bounded d_2 is
compatible with d tending to infinity, within that inherited theorem's
scope. The inherited sharp small-weight bounds and failure of the two-check
filling lemma are unchanged.

The strongest retained global lower bound is

    gamma(N) >= max{ min(1/12,20/N), N^(-2/3), c0/sqrt(N) },
    c0 = pi*3^(1/6)/2^(13/3).

The retained exact degradation construction has ratio 6/7 for N>=636.
Its exact-distance certification is inherited, not rerun in this note.
There is no new strict-trinomial vanishing-ratio family or finite ratio
record here.

The new result removes the one-visible-involution strip case WHEN that
involution is the deck kernel. Any counterfamily to a universal quadratic
bound must avoid this case, in addition to the previously resolved cases.

**Next lemma (retained-involution period descent).** Let
H=T x C_2(s) x Z(z), with T odd, carry support-generating strict trinomials.
Let the actual cover double a finite period while retaining s in the base.
Suppose a minimum weight-w cover logical has a weight-preserving compact
lift and projects to a base boundary. Prove or refute the existence of an
absolute C and a physical binary nonboundary of the actual s-retaining
base of weight at most C w^2. The simplest unresolved product-period
subclass has odd period and a squared common factor in the effective
K(A^2,C) complex. A replacement in the smaller quotient s=1 does not count.

This lemma is not asserted to settle all higher-2-torsion or finite
presentations by itself.

## References and provenance

[1] B. C. B. Symons, A. Rajput, D. E. Browne, *Sequences of Bivariate Bicycle
Codes from Covering Graphs*, arXiv:2511.13560v3. Used for BB and term-preserving
cover conventions, not for the new sparse-descent theorem.
https://arxiv.org/html/2511.13560v3

[2] Stacks Project, Lemma 12.13.6, tag 0111: the long exact homology sequence
of a short exact sequence of complexes.
https://stacks.math.columbia.edu/tag/0111

Inherited project results: `/mnt/data/strict_trinomial_structural/proof.md`,
`/mnt/data/quadratic_bottleneck/proof.md`, and
`/mnt/data/visible2_research/proof.md`. These are preceding research notes,
not externally refereed citations. The new theorem above is proved directly
and does not assume the preceding finite-local classification.
