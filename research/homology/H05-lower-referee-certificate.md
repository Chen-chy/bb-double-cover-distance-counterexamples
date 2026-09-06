**The remaining lower-bound conjecture is false.** There is a valid binary BB double cover
\[
\boxed{[[156,4,14]]\longrightarrow[[312,8,12]],\qquad 12<14.}
\]

The decisive construction uses the previous \(156\)-qubit code as the new base and doubles the other period:
\[
\begin{aligned}
(\ell,m)&=(78,1),&
A&=1+x^8+x^{25},&
B&=1+x^2+x^{13},\\
(\widetilde\ell,\widetilde m)&=(78,2),&
\widetilde A&=1+x^8y+x^{25},&
\widetilde B&=1+x^2y+x^{13}.
\end{aligned}
\]

The weight-\(12\) cover logical has a short algebraic nontriviality certificate. Its projection is precisely the weight-\(12\) base boundary that arose in the preceding rounds. Thus this is a counterexample **in the transfer sector**, not a failure to account for projected logicals.

The finite distance exclusions were reproduced by two standalone exact implementations. Both succeeded, independently obtaining identical matrices and complete circuit sets.

[Complete counterexample certificate](sandbox:/mnt/data/bb_lower_counterexample_certificate.zip)

The package contains the [mathematical certificate](sandbox:/mnt/data/bb_lower_counterexample/CERTIFICATE.md), [bitset verifier](sandbox:/mnt/data/bb_lower_counterexample/verify_lower_bitset.py), [independent polynomial verifier](sandbox:/mnt/data/bb_lower_counterexample/verify_lower_polynomial.py), execution transcripts, reconstructed matrices, exhaustive circuit lists, and an integrity manifest. Neither verifier loads any previous result.

## 1. The valid BB double cover

Work in
\[
R=\mathbb F_2[x]/(1+x^{78}),
\qquad
\widetilde R=\mathbb F_2[x,y]/(1+x^{78},1+y^2).
\]
Use the established Koszul convention
\[
\partial_1(u,v)=Au+Bv,\qquad
\partial_2h=(Bh,Ah),
\]
and its tilded counterpart.

The projection is
\[
p(x^iy^j)=x^i.
\]
The periods satisfy
\[
\widetilde\ell=\ell,\qquad \widetilde m=2m,
\]
and the monomial exponent pairs reduce term by term:
\[
\begin{aligned}
\widetilde A &: (0,0),(8,1),(25,0)
   \longmapsto (0,0),(8,0),(25,0),\\
\widetilde B &: (0,0),(2,1),(13,0)
   \longmapsto (0,0),(2,0),(13,0).
\end{aligned}
\]
These are exactly the conditions of Theorem 3.1, with \(u=1,t=2\). The period-one convention is the same one already fixed in the earlier rounds: \(y=1\) in the base ring. Each defining polynomial still has three distinct monomials. fileciteturn0file1

Directly, every Tanner vertex has two preimages, and reduction gives a bijection on every neighborhood. Both programs check those neighborhood bijections for both check types and both qubit blocks.

This is not a disconnected duplication. Both Tanner graphs are connected. The constant terms connect the four vertex types within each cell; the \(x^{25}\) and \(x^{13}\) connections generate all \(x\)-positions because
\[
\gcd(25,13,78)=1.
\]
The \(x^8y\) connection additionally connects the two \(y\)-positions in the cover.

## 2. An explicit nontrivial cover logical of weight twelve

Set
\[
\sigma=1+x^{39}y,
\]
\[
\zeta_L=1+x^8y+x^{16}+x^{25},
\qquad
\zeta_R=1+x^{11}y,
\]
and define
\[
\boxed{w=\sigma(\zeta_L,\zeta_R).}
\]

Its supports, written as exponent pairs \((i,j)\) for \(x^iy^j\), are
```text
left  = [(0,0),(8,1),(16,0),(25,0),
         (39,1),(47,0),(55,1),(64,1)]

right = [(0,0),(11,1),(39,1),(50,0)]
```
All twelve positions are distinct.

With monomials indexed by \(2i+j\), and the right block offset by \(156\), its flat physical support is
```text
[0,17,32,50,79,94,111,129,156,179,235,256]
```

### The cycle identity

In \(\mathbb F_2[x,y]/(1+y^2)\), before reducing the \(x\)-period, direct multiplication gives
\[
\boxed{
\widetilde A\zeta_L+\widetilde B\zeta_R
=\sigma y(x^2+x^{11}).
}
\tag{1}
\]
Also,
\[
\sigma^2=1+x^{78}y^2=1+x^{78}.
\]
Therefore
\[
\widetilde\partial_1w
=\sigma^2y(x^2+x^{11})
=0
\quad\text{in }\widetilde R.
\]

The relevant square-zero element is **not** the natural transfer element \(1+y\). It is the mixed element \(1+x^{39}y\). Writing
\[
t=1+x^{39},\qquad \varepsilon=1+y,
\]
we have
\[
t^2=\varepsilon^2=0,\qquad
\sigma=t+\varepsilon+t\varepsilon.
\]

### An algebraic nontriviality certificate

Let
\[
T=\mathbb F_4[\eta]/(\eta^2),
\qquad
\mathbb F_4=\mathbb F_2(\omega),
\qquad
\omega^2+\omega+1=0.
\]
Define
\[
\phi(x)=\omega+\eta,\qquad
\phi(y)=1+\omega\eta.
\]
Because
\[
(\omega+\eta)^{78}=1,\qquad
(1+\omega\eta)^2=1,
\]
this defines a ring homomorphism
\[
\phi:\widetilde R\longrightarrow T.
\]

Its values on the check monomials are
\[
\phi(x^8y)=\phi(x^2y)=\omega^2+\eta,
\]
\[
\phi(x^{25})=\phi(x^{13})=\omega+\eta.
\]
Consequently,
\[
\boxed{\phi(\widetilde A)=\phi(\widetilde B)=0.}
\tag{2}
\]
Both coordinates of every cover boundary
\[
(\widetilde Bh,\widetilde Ah)
\]
therefore map to zero.

On the other hand,
\[
\phi(\sigma)=\eta,
\qquad
\phi(\zeta_L)=\omega,
\qquad
\phi(\zeta_R)\equiv\omega\pmod{\eta}.
\]
Hence
\[
\boxed{
\phi(w_L)=\phi(w_R)=\omega\eta\ne0.
}
\tag{3}
\]
Thus \(w\) is not a boundary.

Equations (1)–(3) prove, without a distance search,
\[
\boxed{d_{Z,2}\le12.}
\]

## 3. Dimensions: \(k=4\) and \(k_2=8\)

Let
\[
g=1+x+x^2.
\]
Polynomial Euclidean division gives
\[
\gcd(A,B,1+x^{78})=g.
\]
Therefore
\[
\dim_{\mathbb F_2}R/(A,B)=2.
\]
Equivalently, the simultaneous annihilator has basis
\[
\frac{1+x^{78}}g,\qquad
x\frac{1+x^{78}}g.
\]
Both boundary maps have rank \(78-2=76\), and
\[
k=156-76-76=4.
\]

For the cover, eliminate \(y\) using \(\widetilde B=0\):
\[
y=x^{-2}(1+x^{13}).
\]
The relation \(y^2=1\) becomes \(B(x)^2=0\), while \(\widetilde A=0\) becomes
\[
C=A+x^6B
=1+x^6+x^{19}+x^{25}
=(1+x^6)(1+x^{19}).
\]
Thus
\[
\widetilde R/(\widetilde A,\widetilde B)
\cong
\mathbb F_2[x]/(1+x^{78},B^2,C).
\]
The common gcd is
\[
\boxed{
\gcd(1+x^{78},B^2,C)=g^2=1+x^2+x^4.
}
\tag{4}
\]
This quotient has binary dimension four.

The BB inversion-and-block-swap permutation identifies the two boundary-map ranks, so
\[
k_2=2\dim_{\mathbb F_2}
\widetilde R/(\widetilde A,\widetilde B)=8.
\]

Both implementations independently reconstruct the binary matrices and obtain:

| Code | Qubits | \(\operatorname{rank}H_X\) | \(\operatorname{rank}H_Z\) | \(k\) |
|---|---:|---:|---:|---:|
| Base | 156 | 76 | 76 | 4 |
| Cover | 312 | 152 | 152 | 8 |

No distance inequality is inferred from these dimensions.

## 4. Exact distances: \(14\) downstairs and \(12\) upstairs

The \(156\)-qubit base is checked directly in the new verifiers. Its distance is not accepted merely because it appeared in the earlier counterexample.

### A weight-fourteen base logical

Take
\[
v_L=x^{39}(1+x^8+x^{16}+x^{25}),
\]
\[
v_R=1+x^{11}
 +(1+x^{39})(x^9+x^{22}+x^{35}+x^{37}).
\]
Its supports are
```text
left  = [39,47,55,64]
right = [0,9,11,22,35,37,48,61,74,76]
```
The ordinary polynomial identity
\[
Av_L+Bv_R=(1+x^{78})(1+x^2+x^9)
\]
proves it is a cycle.

Modulo \(g\), both coordinates equal \(x\ne0\), whereas both coordinates of every boundary vanish modulo \(g\). Therefore \(v\) is nontrivial and
\[
d_Z\le14.
\]

### Circuit reduction and parity

Every column of either check matrix has weight three. Hence every \(Z\)-cycle and every \(X\)-cycle has even weight.

A minimum-weight non-boundary cycle must have circuit support. Indeed, a proper nonempty subcycle is either a smaller logical, or a boundary whose removal gives a smaller representative of the original nonzero class.

More generally, every binary cycle decomposes into support-disjoint circuits. Consequently,
\[
\text{all circuits through weight }b\text{ are boundaries}
\]
implies
\[
\text{all cycles through weight }b\text{ are boundaries}.
\]

For an already verified cycle with support \(S\), the circuit test is exactly
\[
\operatorname{rank}(H_X|_S)=|S|-1.
\]

It therefore suffices to classify base circuits through weight \(12\) and cover circuits through weight \(10\). Odd weights \(13\) and \(11\), respectively, are impossible.

### Complete base classification through weight twelve

The complete base circuit list consists of translates of
\[
\partial_2(1),
\]
\[
\partial_2(1+x^a),
\qquad a\in\{2,8,11,13,17,25\},
\]
and
\[
\partial_2(A),\qquad
\partial_2(B),\qquad q,
\]
where
\[
q=(1+x^{39})(1+x^8+x^{16}+x^{25},\,1+x^{11}).
\]

The first nine translation orbits have size \(78\); the orbit of \(q\) has size \(39\). Their weights and counts are:

| Weight | Number of base circuits |
|---:|---:|
| 6 | 78 |
| 10 | 468 |
| 12 | 195 |
| Total | 741 |

All are boundaries. For \(q\), an explicit two-chain \(H\) has exponent support
```text
[1,8,9,10,11,12,13,15,16,17,18,19,20,23,24,25,27,28,31,32,
 34,37,38,41,43,44,46,48,51,53,54,57,61,63,65,66,68,74]
```
Direct multiplication modulo \(1+x^{78}\) gives
\[
BH=1+x^8+x^{16}+x^{25}+x^{39}+x^{47}+x^{55}+x^{64},
\]
\[
AH=1+x^{11}+x^{39}+x^{50}.
\]
Thus
\[
\boxed{\partial_2H=q.}
\tag{5}
\]

Circuit reduction and parity prove
\[
d_Z\ge14.
\]
Together with \(v\),
\[
\boxed{d_Z=14.}
\]

### Complete cover classification through weight ten

All cover circuits through weight \(10\) are translates of
\[
\widetilde\partial_2(1)
\]
and
\[
\widetilde\partial_2(1+x^ay^b),
\]
where
\[
(a,b)\in
\{(2,1),(8,1),(11,1),(13,0),(17,1),(25,0)\}.
\]

Every one of these seven orbits has size \(156\). Thus:

| Weight | Number of cover circuits |
|---:|---:|
| 6 | 156 |
| 10 | 936 |
| Total | 1092 |

All are explicit boundaries. There are no circuits of other positive weights at most ten. Therefore
\[
d_{Z,2}\ge12.
\]
The logical \(w\) attains this:
\[
\boxed{d_{Z,2}=12.}
\]

### Why the finite enumeration is exhaustive

The first verifier searches circuits rooted at the identity qubit in each block. Translation is transitive within each block, so every circuit has such a translate.

A state records a selected support \(U\), forbidden support \(E\), and exact syndrome. At a nonzero syndrome, it chooses an odd check and branches on the first still-available incident variable belonging to a completion. Earlier candidates are forbidden only in later branches.

For any target circuit containing the root, this gives a continuing branch with
\[
U\subseteq C,\qquad E\cap C=\varnothing.
\]
A proper subset of \(C\) cannot have zero syndrome, so the branch reaches the entire circuit.

The only pruning rules are exhausted weight budget, an odd check with no available neighbor, and
\[
|\text{syndrome}|>3(\text{remaining weight budget}).
\]
The last rule is valid because each additional column affects at most three checks. At zero syndrome, boundary membership is checked before applying the circuit filter.

The second verifier uses a different partition: it branches on **every odd-cardinality subset** of the undecided neighbors of an odd check and fixes the remaining neighbors to zero. It represents polynomials by exponent sets and tests boundary membership using polynomial Bézout congruences, not the first implementation’s binary boundary-span oracle.

The exact \(Z\)-sector node counts are:

| Code | Root | Bound | Bitset implementation | Polynomial implementation |
|---|---:|---:|---:|---:|
| Base | 0 | 12 | 985001 | 1602436 |
| Base | 78 | 12 | 991809 | 1559534 |
| Cover | 0 | 10 | 84843 | 153347 |
| Cover | 156 | 10 | 87785 | 155951 |

Every non-boundary-leaf count is zero. Both programs generate the circuit classifications **after** the searches; those classifications never guide pruning.

The independently generated \(741\)-circuit base files and \(1092\)-circuit cover files agree byte-for-byte. Full pruning counters and separate \(X\)-sector searches are included in the execution reports.

## 5. The \(X/Z\) issue

For either period choice, define
\[
f^\star(x,y)=f(x^{-1},y^{-1}),
\qquad
J(u,v)=(v^\star,u^\star).
\]
As a physical coordinate permutation,
\[
L_{i,j}\longleftrightarrow
R_{-i\bmod\ell,\,-j\bmod m}.
\]

For a \(Z\)-cycle,
\[
B^\star v^\star+A^\star u^\star
=(Au+Bv)^\star=0,
\]
so \(J\) gives an \(X\)-cycle. For a boundary,
\[
J(Bh,Ah)
=(A^\star h^\star,B^\star h^\star),
\]
which is an \(X\)-boundary.

Since \(J\) is a weight-preserving involution, it preserves nontriviality and identifies the two sector distances. Both verifiers check these identities on every basis vector and also repeat the distance exclusions directly in the \(X\) sector.

Consequently,
\[
\boxed{
d_X=d_Z=14,\qquad
\widetilde d_X=\widetilde d_Z=12.
}
\]

For a general CSS Pauli logical, at least one pure-sector component is nontrivial, and its support is contained in the Pauli support. Thus these are also the full quantum distances.

## 6. The transfer-sector obstruction is now an explicit counterexample

The natural projection of the new logical is
\[
\boxed{p(w)=q=\partial_2H.}
\]
It is a nonzero base boundary of weight twelve, not a base logical.

Write
\[
\varepsilon=1+y.
\]
For this double cover,
\[
\widetilde A=A+\varepsilon x^8,\qquad
\widetilde B=B+\varepsilon x^2,
\]
so the audited triangular form has
\[
D_1=(x^8\ \ x^2),\qquad
D_2=\binom{x^2}{x^8}.
\]

The witness is
\[
w=q+\varepsilon r,
\]
with
\[
r=
\left(
x^8+x^{39}+x^{55}+x^{64},
\ x^{11}+x^{39}
\right).
\]
Its two physical sheets are \(q+r\) and \(r\), each of weight six.

Define the base chain
\[
a=r+D_2H.
\]
The cycle identity and \(q=\partial_2H\) give
\[
\partial_1a=0.
\]
More decisively, there is the exact chain identity
\[
\boxed{
w+\widetilde\partial_2H
=\varepsilon(r+D_2H)
=\tau(a).
}
\tag{6}
\]
Since \(w\) is nontrivial, Equation (6) proves
\[
\tau_*[a]\ne0,\qquad [a]\ne0.
\]
In particular,
\[
\delta([a])\ge14.
\]

Now apply the transfer-sector metric from the earlier rounds:
\[
\lambda(\alpha)=
\min_{\substack{a'\in\alpha\\s\in R}}
\left(
|a'+D_2s|
+
|a'+(D_2+\partial_2)s|
\right).
\]
For \(\alpha=[a]\), choose \(a'=a\) and \(s=H\). The two terms become
\[
|r|=6,\qquad |r+q|=6.
\]
Since the cover distance is exactly twelve,
\[
\boxed{
\lambda([a])=12<14\le\delta([a]).
}
\tag{7}
\]

Thus the previously unresolved transfer-sector inequality is false in the BB/Koszul setting itself.

There is an additional distinction from the earlier failed arguments: **transfer is injective on all base logical classes for this new double cover.** The end-homology dimensions are two in the base and four in the cover. The long exact sequence forces \(\beta_2=0\), hence
\[
\ker\tau_*=0.
\]
The first verifier also checks this directly on a basis of \(H_2\).

The decrease therefore does not arise because the relevant base logical disappears. It arises because a surviving transfer class admits a cover representative shorter than every nontrivial base logical.

### What led to the counterexample

The useful necessary condition was a short-filling observation. If a nontrivial cover cycle \(Y\) projects to \(\partial_2s\), then, for every lifted two-chain \(\widehat s\),
\[
\boxed{
|Y|+|\widetilde\partial_2\widehat s|\ge2d.
}
\tag{8}
\]
Indeed,
\[
Y+\widetilde\partial_2\widehat s=\tau(b)
\]
for a nontrivial base cycle \(b\), so the left-hand side is at least
\[
|\tau(b)|=2|b|\ge2d.
\]

This protects short boundaries with short lifted fillings, but it does not protect the boundary \(q\). In the present example, every cover boundary with literal projection \(q\) must have weight at least
\[
2\cdot14-12=16,
\]
even though \(q\) itself has weight twelve. The chosen monomial voltages instead give the weight-twelve **logical** lift \(w\).

That is the precise information supplied by the earlier example: its short, nonlocal boundary became the target for a lower-bound counterexample in the next cover.

## 7. Verification artifacts and conclusion

Run either standalone file:
```sh
python3 verify_lower_bitset.py
python3 verify_lower_polynomial.py
```
Both require only Python 3.10 or later and the standard library. Their final line is
```text
BB_LOWER_BOUND_COUNTEREXAMPLE_VERIFIED
```
only after every check passes.

The finalized executions returned code zero. The [execution comparison](sandbox:/mnt/data/bb_lower_counterexample/EXECUTION_METADATA.json) records agreement of all four matrices, both complete circuit sets, ranks, and distances. The full transcripts are [the bitset run](sandbox:/mnt/data/bb_lower_counterexample/bitset_run.txt) and [the polynomial run](sandbox:/mnt/data/bb_lower_counterexample/polynomial_run.txt).

The resulting theorem is
\[
\boxed{
Q(1+x^8+x^{25},\,1+x^2+x^{13},\,78,1)
=[[156,4,14]],
}
\]
\[
\boxed{
Q(1+x^8y+x^{25},\,1+x^2y+x^{13},\,78,2)
=[[312,8,12]].
}
\]
These form a valid BB double cover, and
\[
\boxed{d_2=12<14=d.}
\]

STATUS: LOWER_BOUND_FALSE
