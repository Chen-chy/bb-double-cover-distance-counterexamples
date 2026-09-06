# Open problems at the export boundary

This page preserves the latest target. It is not a new proof attempt.
The factor-three statement below, the stronger half-weight completion lemma,
and finiteness of C_* remain unresolved.

## 1. The full slope-(2,1) minimum

Use

\[
A=1+X+Y,\quad B=1+XH^2+YH,
\quad X=z^r,\ Y=z^{2s},\ H=z^{2g},\quad r\text{ odd},
\]

with c=ej, a_0=A/c, b_0=B/c, G=e^2j, and a nonconstant selected divisor E_0|e.
Let

\[
P_0=(AB+A+B)/G,\quad S_0=(A+B)/G,\quad Q_0=A^2/G.
\]

Every compact cover cycle has physical coordinates

\[
C(\phi,h)=
(P_0\phi+(B+1)h,\ S_0\phi+h,\ Q_0\phi+(A+1)h,\ h).
\]

Survival in the selected compact finite image is E_0 not dividing phi. The full
minimum ranges over **all** such phi and all h, not one generator, one transfer,
one universal factor, or one fixed polynomial message.

Set

\[
\ell=r-2s,\quad m=\ell+2g,\quad K=1+z^\ell,\quad J=1+z^m,
\quad\theta=Y^{-2}H^{-1},
\]
\[
\alpha=(YH)^{-1}P_0\phi,\quad\beta=Y^{-1}Q_0\phi,\quad\sigma=S_0\phi.
\]

The complete common-message conditions are exactly

\[
K\alpha+J\beta=\theta\sigma,\qquad
H\alpha+\beta+K\sigma=0,\qquad E_0\nmid\beta.
\]

Let F be the sign-one edge set of the universal graph with steps ell,m and
S=supp(sigma). For a choice x of source spins, let Gamma_{phi,x} be the graph of
eligible finite zero-sign tree components after removing sources, with adjacency
where two trees conflict. Its independence number is denoted iota.

The latest theorem gives

\[
\widehat\Delta=
\min_{E_0\nmid\phi}\left[
|\sigma|+\min_{x\subseteq S}
\bigl(|F\triangle\delta x|-2\iota(\Gamma_{\phi,x})\bigr)
\right].
\]

The active conjecture is

\[
\boxed{\widehat\Delta\le3\Delta},\qquad
\Delta=\min_{E_0\nmid f}(|b_0f|+|a_0f|).
\]

The inherited construction gives factor four at this slope. No improvement to
three and no full-minimum ratio above three was obtained in the archived rounds.

## 2. Stronger sufficient half-weight lemma

The earlier projection formula is

\[
\widehat\Delta=
\min_{\substack{j\mid f\\E_0\nmid f}}
\bigl(|b_0f|+|a_0f|+2\kappa(b_0f,a_0f)\bigr),
\]

where kappa counts the minimum filling support outside the projected word.
A sufficient statement would choose a minimum base representative z of weight
Delta and a universal base boundary beta with

\[
w=P_ez+\beta,\qquad |w|\le2\Delta,\qquad\kappa(w)\le\Delta/2.
\]

It has not been proved or refuted. Its failure would not automatically refute
the full inequality because the unrestricted optimum may use a different class.
In the explicit all-cycle parameterization, pinning the projected class of a
minimum message f_0 requires

\[
ja_0\phi\equiv f_0\pmod e,
\]

not merely modulo E_0. See round 09 §8 for the exact weight constraints.

## 3. Information from global base minimality

For a globally minimum surviving base cycle z=(b_0f_0,a_0f_0), define

\[
N(\tau)=(b_0E_0\tau,a_0E_0\tau).
\]

Every tau satisfies

\[
2|\operatorname{supp}z\cap\operatorname{supp}N(\tau)|\le|N(\tau)|.
\]

These moves include universal boundaries and universal classes killed by the
chosen finite specialization. A cover move preserving the selected compact class
has delta-phi=E_0 lambda and delta-h=mu, changing the projected base message by

\[
\delta f_{\rm proj}=jE_0\bigl(a_0\lambda+(e/E_0)\mu\bigr).
\]

Those are exactly the jE_0-multiple messages. Tree removal alone is the special
case lambda=0, mu=1_T; it does not determine overlap with z. The exact 74N family
shows why optimality only in h is not enough.

## 4. The selected next lemma

**Packing-deficit transfer lemma — unproved.** If the full tree-packing expression
at a jointly optimal message exceeds 3Delta, construct a Laurent polynomial tau
such that

\[
2|\operatorname{supp}z\cap\operatorname{supp}N(\tau)|>|N(\tau)|,
\]

contradicting global base minimality.

The construction must use both complete common-message equations and permit
message-changing exchanges. The size of a tree at a fixed phi cannot provide the
contradiction by itself. The conflict graph can contain odd cycles, so an
unjustified bipartite matching replacement is not available.

## 5. What a counterexample would have to certify

A genuine refutation must establish the full minimum hat-Delta>3Delta, after all
messages and all boundary adjustments. The established large-period realization
theorem then converts such rank-one compact data into actual finite-distance
violations at sufficiently large compatible periods, with winding classes
excluded by a symbolic weight bound.

An expensive chosen generator, a restricted-sector minimum, a conditional 74N
minimum, or a failed finite search is not enough. None of the preserved negative
controls meets the full-counterexample requirement.

The broader program still needs universal linear control of the remaining
low-rank and finite-check mechanisms. The graph conversion extends to general
primitive resonance slopes, but the factor-three claim does not automatically
extend. A fixed slope has the reported factor 2m construction; uniform control
as the primitive slope grows remains open.
