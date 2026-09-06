# Research map and chronology

Dates below are **UTC user-message timestamps initiating each stage**, not invented creation or completion times. Original ZIP member timestamps are retained in the source containers. Each stage keeps its own original README, proof, code, case data, and outputs.

| Stage | Starting message | Direction and substantive role | Source entry |
|---|---|---|---|
| 00 | 2026-09-05 16:36:47 | Arbitrary-term degradation; four-term vanishing family, unrestricted order $N^{-1}$, filling/transfer metric, provisional seed audit. Source package absent. | [public report](../context/conversation/00-arbitrary-term-public-report.md) |
| 01 | 2026-09-05 18:56:20 | Strict-trinomial weight-six classification; $D_6=56$; false two-check filling lemma; unbounded filling without a short alternative lift. | [proof](../research/01-weight-six/proof.md) |
| 02 | 2026-09-05 19:43:47 | Weight-eight quotient theorem $D_8=96$; cubic pairing graphs, exact relation catalogues, nilpotent cases. | [proof](../research/02-weight-eight/proof.md) |
| 03 | 2026-09-06 03:04:00 | Symbolic all-weight degradation theorem $d\le4d_2^3$; geometric size bound; no dependence on earlier finite enumerations for the main cubic result. | [proof](../research/03-structural-degradation/proof.md) |
| 04 | 2026-09-06 03:41:21 | Quadratic bottleneck narrowed to visible 2-primary torsion; odd-torsion compact descent; cofactor and specialization counterchecks. | [proof](../research/04-quadratic-bottleneck/proof.md) |
| 05 | 2026-09-06 05:01:09 | Actual finite-local two-bit nilpotent lengths and cover maps; abstract classification is not a sparse metric theorem. | [proof](../research/05-visible-two-primary/proof.md) |
| 06 | 2026-09-06 05:41:20 | Physical quadratic descent for the deck-involution strip subclass; retained-involution countercheck to using the wrong quotient. | [proof](../research/06-sparse-deck-descent/proof.md) |
| 07 | 2026-09-06 09:26:29 | Direction explicitly switches to amplification. Complete rank-one Laurent parameterization; parity replacements; stabilization; exact $8\to14$ family. | [proof](../research/07-rank-one-amplification/proof.md) |
| 08 | 2026-09-06 11:35:38 | Mixed-parity full optimization; arithmetic-progression factor-two subclass; nonconstant-message cancellation. | [proof](../research/08-mixed-laurent/proof.md) |
| 09 | 2026-09-06 13:09:47 | Fixed-$c$ product-weight bound; quadratic amplification; exact monomial-orbit reduction; inadmissible five-term control; half-generator lemma remains open. | [proof](../research/09-fixed-c-product-bound/proof.md) |
| Export | 2026-09-06 14:17:06 | Preservation and reproducibility checks only; no new mathematical exploration. | [export report](EXPORT_REPORT.md) |

## Logical dependencies, without merging unlike claims

The weight-six theorem uses the supplied prior weight-two/weight-four exclusions as described in its note. The weight-eight theorem does not need the weight-six enumeration for its individual $D_8$ statement; its combined ratio corollary does use the earlier exclusions. The structural cubic proof is symbolic and explicitly independent of both catalogues; retaining their sharper individual bounds is a separate consequence.

Stages 04–06 refine the degradation cubic bottleneck but do not establish a global quadratic replacement. Stage 05 concerns actual finite support groups of rank at most two, not arbitrary four-generated universal incidence groups. Stage 06 additionally needs the incidence involution to be the actual deck element and a weight-preserving compact lift.

Stages 07–09 concern amplification. Stage 07 provides the all-message cover parameterization and period-stabilization input used by 08 and 09. Stage 08 does not prove the whole mixed-parity inequality; stage 09 fixes the quadratic common divisor and proves a product-weight estimate, still not factor three.

## Material worth retaining even though it is not the endpoint

The weight-six package includes `finite_scan.py`, `finite_scan_results.json`, `classify_rank_two.py`, and `rank_two_certificates.json`. These optional discovery/audit artifacts remain present but are not automatically run by the export checker.

The weight-eight package retains graph automorphisms, coloring representatives, raw high- and low-rank TSV catalogues, category counts, exact fillings, intermediate generator progress logs, and independent arithmetic checkers. A concise verification summary is not a replacement for these files.

The rank-one package retains both C++ shortest-path generation code and the two binary Bellman potentials. The independent checker does not need to rerun the optimization, but the generation path is still available.

The structural, quadratic-bottleneck, visible-torsion, sparse-descent, and later Laurent packages retain negative controls and scope audits precisely because they rule out false shortcuts. See [failed approaches](FAILED_APPROACHES.md).
