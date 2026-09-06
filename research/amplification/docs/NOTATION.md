# Notation, physical weights, and scope

The original reports use some letters differently between rounds. They are
preserved verbatim. This guide disambiguates the main objects without rewriting
those reports.

A BB complex over a binary group algebra R is

\[
R\xrightarrow{h\mapsto(Bh,Ah)}R^2
\xrightarrow{(u,v)\mapsto Au+Bv}R.
\]

A cycle satisfies Au+Bv=0. A logical is a cycle not in the boundary subspace.
An explicit logical of weight w proves d<=w only. Exact distance additionally
requires a complete lower certificate, a symbolic exclusion, or another rigorous
lower argument. k denotes encoded qubits, not the dimension of one arbitrary
chosen logical sector. The reports use the standard equality of BB X and Z
distance problems through inversion/block exchange.

The base physical length is n; the finite group has n/2 elements. Its double
cover has 2n physical qubits and n group elements. This distinction is essential
in the geometric bounds. Gamma(N) is the supremum of d_2/d over bases of physical
length at most N; C_* is the untruncated supremum.

“Strict trinomial” means three distinct surviving monomials per check. Some
auxiliary reduced codes have four terms in one check; their distances are not
new strict-trinomial BB cover records. Term matching means each lifted monomial
projects to its corresponding base monomial and the deck element remains
nonidentity. Monomial gauges, translations, block exchanges, and group
isomorphisms can change displayed supports without changing physical distance.

## Four different minima

| Quantity | Domain | Important warning |
|---|---|---|
| d, d_2 | All finite nonboundary cycles | Includes specialization-created or winding classes |
| Delta, hat-Delta | Universal finite-support cycles whose finite image survives, with every permitted message/boundary | Weight is taken before finite coordinate identification |
| A sector-restricted compact minimum | A specified universal homology component | May exceed the full compact and actual distance |
| min_h E_phi(h) | One fixed polynomial message phi | Not the minimum in the universal homology class; changing phi by an annihilator multiple may be a boundary |

The transfer-sector quantity mu(Q,K), K=ker(tau_hat), minimizes only classes
outside a kernel. It can diverge relative to d while d_2 stays constant. The
lambda_r values are weight thresholds for spanning r base homology directions;
they are not distances of all cover sectors.

## Repeated-root and compact specialization conventions

In one variable, P=F_2[z,z^-1], F_L=z^L+1, and period doubling replaces F by F^2
in characteristic two. With c=gcd(A,B), A=ca, B=cb, and ar+bs=1, the finite H_1
has two algebraic gcd coordinates. The Bezout transformation is not an isometry.

The deck basis is {1,t}, t^2=1. With epsilon=1+t, a component p+epsilon r has
physical sheets (p+r,r), not (p,r). Dropping this conversion gives incorrect
Hamming estimates. Binary ann(epsilon)=epsilon R is an algebraic identity, not
semisimplicity.

Universal homology and specialized homology differ. In general

\[
H_1(C)\otimes R/I\ne H_1(C\otimes R/I).
\]

A compact class can become a boundary and Tor terms can create finite homology.
Reports that establish survival use explicit module maps or nonboundary tests;
finite generation alone is not a proof. A large-period no-winding theorem must
be invoked with its root-data and locality hypotheses before identifying
compact minima with actual finite distances.

## Slope-(2,1) notation

\[
A=1+X+Y,\quad B=1+XH^2+YH,\quad
X=z^r,\quad Y=z^{2s},\quad H=z^{2g},\quad r\text{ odd}.
\]

Here H is a monomial. In the rank-one report, another H denotes a gcd controlling
finite compact specialization; context matters. Likewise U may denote a group
presentation, a qubit block, or one component of a word.

In the active hard-core setting, c=ej, a_0=A/c, b_0=B/c, and G=e^2j. E_0 is a
nonconstant selected compact survivor divisor of e. The source sigma and edge
signs alpha,beta are all determined by the same Laurent message phi; arbitrary
signed graphs are not valid replacements. The latest report gives two complete
linear constraints characterizing that common-message image.

The graph steps ell=r-2s and m=ell+2g are odd, so the universal graph is bipartite.
It is a multigraph if edge types share geometric endpoints. Contracted tree
conflict graphs need not be bipartite. The source-spin variable x in that model
is a vertex assignment, not necessarily the original Laurent variable x.
