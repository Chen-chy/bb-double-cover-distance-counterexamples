# A binary BB double cover with distance greater than twice the base distance

## Result

Over F2, use the same two trinomials

    A = 1 + x^8 + x^25,
    B = 1 + x^2 + x^13.

At periods (ell,m)=(39,1) the code has parameters [[78,4,6]]. At periods
(78,1), with the same polynomials, the code has parameters [[156,4,14]].
It is therefore a valid Theorem 3.1 double cover, and

    d_cover = 14 > 12 = 2*d_base.

This is a computer-assisted counterexample. The only distance-exclusion
step is an exact, exhaustive circuit classification. Its completeness is
proved below. The programs use integer binary arithmetic, not an optimizer,
a heuristic decoder, or a probabilistic test.

`verify_counterexample.py` is standalone and uses the Python standard library
only. Run it with Python 3.10 or later:

    python3 verify_counterexample.py

`run_output.txt` records the output produced in this computation.

## Chain complexes and dimensions

For period L, let R_L=F2[x]/(x^L+1), with its usual monomial basis. Put

    partial_1(u,v)=A*u+B*v,
    partial_2(h)=(B*h,A*h).

The CSS matrices are H_X=(A B) and H_Z^T=(B A). Their composition is zero.
Projection from period 78 to 39 is reduction modulo x^39+1, on both blocks.
It is a chain map because the defining polynomials are unchanged.

Let g=1+x+x^2. Exact polynomial Euclidean division gives gcd(A,B)=g.
Since g divides both period polynomials, H_0 has dimension 2 at either
period. The simultaneous annihilator H_2 has dimension 2 as well. Euler
characteristic gives k=4. Independent binary matrix reduction gives

    period 39: rank(H_X)=rank(H_Z)=37,
    period 78: rank(H_X)=rank(H_Z)=76.

Both Tanner graphs are connected: the differences 2 and 13 between the
monomials of B generate the cyclic group at either period, and the constant
monomials connect the different check/qubit types.

## Explicit nontrivial cycles

Set

    F = 1+x^39,
    z_L = 1+x^8+x^16+x^25,
    z_R = 1+x^11,
    c = x^2+x^11,
    R = x^9+x^22+x^35+x^37.

As ordinary polynomials, direct multiplication gives

    A*z_L+B*z_R = F*c,
    A*z_L+B*R+c = F*(1+x^2+x^9).

Consequently z=(z_L,z_R) is a weight-six base cycle, and

    w=(x^39*z_L, z_R+F*R)

is a weight-fourteen cover cycle: its syndrome is
F^2*(1+x^2+x^9), zero modulo x^78+1=F^2. Its projection is exactly z.

Let omega^2+omega+1=0. Evaluation at x=omega annihilates A and B and therefore
both coordinates of every boundary. But z evaluates to (omega,omega).
Thus z is nontrivial, and w is nontrivial because it projects to z.

## The class is killed by full transfer

Write A=g*a, B=g*b, F=g*f. Since gcd(a,b)=1, choose ordinary polynomials U,V
with U*a+V*b=1. The program computes and verifies such a Bezout identity.
Since g divides c, the first displayed identity implies

    a*z_L+b*z_R = 0 modulo F.

Put v=U*z_R+V*z_L modulo F and h=f*v modulo F^2. Then

    b*v=z_L modulo F,
    a*v=z_R modulo F,
    (B*h,A*h)=(F*z_L,F*z_R)=tau(z) modulo F^2.

Thus the minimum class alpha=[z] belongs to ker(tau_*)=im(beta_2).
This conclusion does not assume transfer preserves nontriviality.

The base period is odd, so its ring is square-free. Its Koszul homology is
identified by evaluation with F4^2: the g factor contributes F4^2 and the
other factors are acyclic. Exactly 39 weight-six non-boundary cycles occur;
they are the translates of z. Their classes are the three nonzero diagonal
classes (lambda,lambda), lambda in F4*. They are all killed by transfer.

## Exact distance-exclusion certificate

A nonempty binary cycle has **circuit support** when no proper nonempty
subset of its support is a cycle. The following elementary fact is central.

**Circuit reduction lemma.** A minimum-weight non-boundary cycle has circuit
support. Indeed, if it contains a proper subcycle, that subcycle either is a
smaller non-boundary or is a boundary whose removal leaves a smaller
non-boundary.

Translations act transitively on each qubit block and preserve cycles and
boundaries. It therefore suffices to examine circuits containing index 0 of
the left block, and index 0 of the right block.

The exact search maintains a chosen set U, a forbidden set E disjoint from
U, and syndrome H*1_U. At a nonzero syndrome it chooses an odd check and
branches on its available incident qubits, in a fixed order. In the branch
choosing the j-th candidate, the earlier candidates are forbidden. A
completion C containing U must contain at least one candidate; choosing the
first member of C in this order gives a branch compatible with C. This
partitions all possible completions.

There are only two weight stopping rules: stop at the requested weight
bound, or prune when the syndrome has more than three times the number of
remaining qubits. The latter is valid because every column has weight three.
When the syndrome becomes zero, the selected vector is recorded and tested
directly for membership in the binary span of the boundary columns. Ending
a branch at zero syndrome cannot truncate a proper subset of a circuit.
Thus every circuit through the root, up to the requested weight, is tested.

For the base, no cycles occur through either root at weight at most four.
For the cover, exhaustive enumeration through weight twelve gives:

| Sector | Root index | Search nodes | Zero-syndrome leaves by weight | Non-boundary leaves |
|---|---:|---:|---|---:|
| Z | 0 | 985001 | 6:3, 10:30, 12:66 | 0 |
| Z | 78 | 991809 | 6:3, 10:30, 12:56 | 0 |
| X | 0 | 941501 | 6:3, 10:30, 12:58 | 0 |
| X | 78 | 894576 | 6:3, 10:30, 12:58 | 0 |

The zero-syndrome leaves include some non-circuits; this causes no omission
and no incorrect exclusion. Filtering by rank(support columns)=weight-1 and
then expanding translations gives the following complete classification:

| Weight | Translation-orbit representatives | Total distinct circuits |
|---|---|---:|
| 6 | partial_2(1) | 78 |
| 10 | partial_2(1+x^a), a in {2,8,11,13,17,25} | 468 |
| 12 | partial_2(A), partial_2(B), tau(z) | 195 |

The first nine orbit types are manifest boundaries. The last is a boundary
by the explicit construction of h above. The last orbit has 39 elements;
the other nine have 78 elements each. All 741 circuits through weight twelve
are therefore boundaries. No non-boundary cycle of weight at most twelve
can exist, by the circuit reduction lemma.

Every column has odd weight three, so every cycle has even weight. The
base therefore has distance six, and the cover has distance fourteen.

For the X/Z identification, let f*(x)=f(x^(-1)). The permutation
J(u,v)=(v*,u*) sends Z cycles to X cycles and Z boundaries (B*h,A*h) to
X boundaries (A* h*,B* h*). It preserves weight and is invertible, so d_X=d_Z
at both periods. The code also independently checks both sectors above.
Swapping x and y gives a counterexample in the other double-cover orientation.

## Exact class metrics for the counterexample

For alpha=[z], the computations establish

    delta(alpha)=6,
    rho(z)=4,
    mu(alpha)=14,
    nu(alpha)=22.

The standard low-sheet section is used for rho and nu. Here D_1 is just the
carry part of ordinary multiplication; E_i=0 because each lifted monomial
has exponent below 39. The pair r=(z_L,R) has partial_1*r=D_1*z=c, and
exactly four correction positions outside supp(z). To rule out rho<=3, the
program quotients syndromes by the span of the six support columns of z
and exhausts all outside subsets of sizes 0,1,2,3. Their counts are
1,72,2556,59640. None realizes the required quotient syndrome.

For nu, a vector (u,v) entirely on the low sheet has deg u,deg v<39. Since
A and B have degrees 25 and 13, its syndrome has degree below 78. Thus it
is a cover cycle iff A*u+B*v=0 as ordinary polynomials. This is equivalent
to (u,v)=(b*f0,a*f0), where deg f0<16. All 65536 possibilities are enumerated.
Each of the three nonzero diagonal classes has minimum weight 22.

The equality mu=14 follows without any fixed-projection assumption: all
cover cycles projecting to a nonzero class are non-boundaries, hence have
weight at least 14; the explicit w achieves 14 and projects literally to z.
All three minimum classes have delta=6 and mu=14. No different minimum
class, heavier representative, different projectable class, or nonzero
transfer-sector logical can have cover weight at most twelve, since the
actual cover distance is fourteen.

## General second-order class variational theorem

For any audited BB double cover, let Z_1=ker(partial_1). The physical pair
associated with triangular coordinates (q,r) is (q+r,r). For a nonzero
projectable base class alpha,

    mu(alpha)=min W(q,r),
    W(q,r)=|q+r|+|r|,

where partial_1*q=0, [q]=alpha, and partial_1*r=D_1*q. This is exactly the
minimum weight over all cover cycles with projected homology class alpha;
q is not fixed.

If alpha=beta_2[h], partial_2*h=0, every representative is
q=D_2*h+partial_2*s. From

    partial_1*E_2+D_1*D_2+E_1*partial_2=0,
    partial_1*D_2+D_1*partial_2=0,

one obtains every correction, and only those corrections, as

    r=E_2*h+D_2*s+c,  c in Z_1.

Hence the exact formula is

    mu(alpha)=min_{s in C_2,c in Z_1}
      ( |D_2*h+partial_2*s+E_2*h+D_2*s+c|
        +|E_2*h+D_2*s+c| ).

For another preimage h'=h+g, choose u with D_2*g=partial_2*u. Replacing
s by s+u and c by c+E_2*g+D_2*u preserves the actual q and r; the added
term in c is a cycle by the two identities. Thus the formula is independent
of h. It remains valid in this counterexample: the false statement is the
metric inequality mu<=2*delta, not the variational formula.

## Previous family and the stronger one-sheet claim

`verify_auxiliary.py` rechecks the previously claimed family and its uniform
F4/min-plus certificate. For q=3j, L=9j, put X=x^q, T=1+X+X^2,

    z=(x+X,1+x),
    q0=(T,T),
    s_j=x^2*(T+x^2+x*X)/(1+x+x^2).

The quotient is an ordinary polynomial and

    q0+x*z=partial_2*s_j.

The weight-six cover cycle (P,P), P=1+x^(2q)+x^(4q), projects to q0. Thus
mu([z])=6 for every j>=2, while delta([z])=4 and rho(z)=2j-1.

Its triangular coordinates are q0 and r=(X,X), not r=0. A genuine
one-per-fibre lift must not be confused with a lift to the particular fixed
low sheet used by nu. In that fixed section,

    nu([z])=10j for even j, and infinity for odd j.

The auxiliary program includes a parameter-uniform two-dimensional
low-sheet-kernel certificate. Splitting each low-sheet polynomial into
three blocks of length q gives the six-by-six polynomial matrix C listed
in the source. Its inverse numerator ADJ satisfies C*ADJ=D*I with
D=x^2*(x+1)*(1+x+x^2)^3. The nine binary carry coefficients admit exactly
four possibilities. Divisibility repeats with q modulo 12 because
x^(q+12)=x^q modulo D for q>=2, and the degree constraint is independent
of q. Four exact 512-case tables therefore establish kernel dimension two
for every j>=2. The explicit basis in the program has nonzero weights
10j+2,10j,10j; direct evaluation at a root of 1+x+x^2 gives the stated
parity-dependent class images. The basis identities follow from
(1+x^3)*(1+x^3+...+x^(3j-3))=1+x^q.

The old [[30,4,4]] -> [[60,4,6]] example has delta=4, rho=1, mu=6, nu=20.

The smallest possible trinomial base already disproves the universal nu
inequality. At base period 3 take A=B=1+x+x^2; at cover period 6 take
A~=x^2*(1+x+x^2), B~=1+x+x^2. For z=(x,1),

    delta=mu=2, rho=0, nu=infinity.

Indeed (x^4,1) is a weight-two cover cycle projecting to z, and
partial_2(x+x^2)=tau(z). The low-sheet cover-cycle space is generated by
(1,x^2) and (g,g); its projected classes do not contain [z].

## Files

- verify_counterexample.py: standalone exact main certificate.
- independent_bivariate_check.py: an independently constructed, equivalent
  (ell,m)=(3,13) -> (6,13) instance, with direct boundary membership checks.
- verify_previous_family.py: prior standard-library uniform min-plus verifier.
- verify_auxiliary.py: class-level family identity, low-sheet certificate,
  smallest nu counterexample, and old 30-to-60 example.
- run_output.txt, auxiliary_output.txt, independent_output.txt: actual outputs.

The equivalent genuinely bivariate presentation in the independent checker is

    A=1+x*y^12+x^2*y^8,
    B=1+x*y^2+x^2,
    A~=A,
    B~=1+x*y^2+x^5.

The group-generator change x=u^13, y=u^66, followed by multiplication of B
by u^13 and the corresponding qubit/check permutations, gives the unchanged
cyclic polynomials at the start of this document.
