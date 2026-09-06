# BB double-cover distance counterexamples

**The conjectured double-cover distance bound $d\le d_2\le2d$ fails for binary BB codes. Exact counterexamples, cubic replacement bounds, complete proofs, and certificates. Version 0.2.1.**

## [Read first: principal results and evidence report](REPORT.en.md)

**104 records are not 104 valid or independent theorems.** [The report](REPORT.en.md) collects the exact counterexamples, current bounds, proof scope and excluded approaches. [The status register](results/STATUS.md) separates headline results, scoped statements, negative results, gaps, searches and open questions. Historical notes are not endorsed wholesale.

[中文首页](README.md) · [Complete mathematical contents](results/README.md) · [104 research records](results/CLAIMS.md) · [Reproduction](docs/REPRODUCIBILITY.md)

This is an independent research repository, not an arXiv ancillary tree. Seven theory chapters and twenty-five complete research notes are readable directly on GitHub. The optional manuscript in `paper/` is a typeset exposition of selected results, not the authority for the whole research record.

## Exact counterexamples

For $A=1+x^8+x^{25}$ and $B=1+x^2+x^{13}$:

| Cover | Exact parameters | Failure |
|---|---|---|
| $(39,1)\to(78,1)$ with unchanged checks | $[[78,4,6]]\to[[156,4,14]]$ | $14>2\cdot6$ |
| $(78,1)\to(78,2)$ with $A'=1+x^8y+x^{25}$, $B'=1+x^2y+x^{13}$ | $[[156,4,14]]\to[[312,8,12]]$ | $12<14$ |

The middle code is identical. Both covers are connected and term-matched, with bijective full Tanner-graph neighborhoods. Each counterexample retains two independent, unchanged exact verifiers. Their searches regenerate all relevant circuits; they do not trust supplied circuit lists as pruning assumptions. [The full proof](results/theory/01-counterexamples.md) includes attaining logicals and explicit nonboundary arguments; [the algorithm chapter](results/theory/06-certificate-algorithms.md) proves completeness.

## Two-sided replacement bounds

Assume binary coefficients, finite abelian groups, a term-preserving quotient with kernel $C_2$, three distinct terms in each check both before and after projection, and $k>0$. Let $n$ be the BASE qubit count. The consolidated symbolic proof gives

$$d\le4d_2^3,\qquad d_2\le8d^3.$$

Set $C_0=\frac{16}{3}(12/\pi^2)^{3/4}$. Then

$$
2\left\lceil\frac{(d/4)^{1/3}}2\right\rceil
\le d_2\le
2\left\lfloor\frac{\min\{8d^3,n,C_0(2n)^{3/4}\}}2\right\rfloor.
$$

When $k_2=2k$, also minimize the upper endpoint with $2d$. [The complete proof](results/theory/03-polynomial-bounds.md) treats the relation-lattice, finite-check and higher-rank/torsion branches. [The size-bound chapter](results/theory/04-size-bounds.md) includes the ambient and truncated distortion estimates. Constant 8 is a previously added consolidation corollary; the source branches' constant 32 remains explicitly historical. Neither optimality nor independent human referee review is asserted.

## Complete research scope

The [104-entry register](results/CLAIMS.md) merges 16 main results, 10 homology/class-metric results, all 38 amplification entries and all 40 degradation entries. It retains original statuses and adds explicit current-status overlays. Topics include projection/transfer ranks, spanning thresholds, small-weight classifications, torsion–Frobenius compact metrics, rank-one resonance and Bellman certificates, visible two-primary obstructions, sparse deck descent, Laurent product bounds, common-message graph optimization, Pareto frontiers, and negative controls.

The recovered arbitrary-term report is included in full, separately labeled as outside the strict-trinomial class. Its original verifier package has not been recovered. Restricted-sector minimum 16, fixed-message minimum $74N$, and a five-term lift are not advertised as new full-distance counterexamples in the target class. Universal linear amplification, a positive size-independent degradation ratio, and a global quadratic degradation improvement remain unresolved in this record.

## Reproduce

Python 3.10+ with only the standard library suffices for the core profile.

```bash
python -m unittest discover -s tests -v
python scripts/check_repository.py
python scripts/reproduce.py --profile core --output checks/local
python -m bbcover compare upper
python -m bbcover compare lower
python -m bbcover results DIST-UPPER
python -m bbcover bounds 14 --n 156 --k 4 --k2 8
```

`inspect` and `compare` reconstruct matrices, dimensions, covers and a witness; they do not recompute the exhaustive distance lower bound. `bounds` returns a theorem interval, not an exact distance. It evaluates integer-safe cubic, length and transfer caps, not a floating-point rounding of the analytic cap.

The extended profile needs SymPy and a C++17 `g++` compiler. It reruns 23 amplification and 24 degradation retained-audit commands, not every historical discovery scan or expensive classification generator.

```bash
python -m pip install -r requirements-research.txt
python scripts/reproduce.py --profile extended --output checks/extended
```

Use a fresh output directory. Timeout means incomplete, never excluded. Do not use optimized Python for original auditors.

## Layout and publication

`results/` is the full reading edition; `research/` contains original proofs, all retained code and data; `certificates/` contains the four independent exact implementations; `bbcover/` provides the installable interface. `scripts/`, `tests/`, `.github/`, and `docs/` support maintenance, CI, reproducibility and release. `provenance/` records every supplied member and the byte-preserving reorganization. `paper/` is optional.

[GitHub publishing instructions](docs/PUBLISH_GITHUB.md) cover the provided Git bundle and clean source ZIP. No `anc/` wrapper is used. CI definitions are supplied; successful local checks do not imply a remote Actions run. [Citation](CITATION.md) and [rights notice](NOTICE.md) avoid inventing authors, affiliations, repository URLs, DOIs, or a reuse license.

The [five homology and class-metric reports](results/README.md#homology) include the Bockstein square-zero theorem, deck Jordan structure, support-obstruction family, variational metric and exact binary dual. Historical conjectures disproved in later reports remain explicitly historical.
