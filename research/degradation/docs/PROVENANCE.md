# Provenance and preservation policy

## What was physically available

At the beginning of this export, `/mnt/data` contained nine research ZIPs, matching standalone proof/summary/audit attachments, and two task attachments. The machine-readable [source inventory](../provenance/source_inventory.json) records original runtime paths, member paths, file sizes, SHA-256 digests, and their repository locations.

All 137 non-directory members of the nine ZIPs are present under `research/`. Each is byte-identical to its source archive member. Every original ZIP is preserved under `provenance/source_archives/`, byte-for-byte. No original research member was excluded. There were no cache or compiled-executable members requiring removal from those original packages. The `.bin` files are mathematical Bellman certificates, not executable clutter.

Separately attached copies that exactly match an archived member are represented by that canonical extracted file. Their original names and hashes are still in the inventory. This is exact deduplication, not a choice between conflicting revisions. No differing loose proof revision was found.

The two unique original task attachments are in `context/input/`. Their contents were not rewritten. A [per-file index](FILE_INDEX.md) and [standalone path-alias table](PATH_ALIASES.md) supplement the machine-readable inventory.

## Canonical path map

| Original runtime or archive prefix | Canonical repository prefix |
|---|---|
| `trinomial_research/` or `strict_trinomial_weight_six/` | `research/01-weight-six/` |
| `weight8_research/` or `strict_trinomial_weight_eight/` | `research/02-weight-eight/` |
| `strict_trinomial_structural/` | `research/03-structural-degradation/` |
| `quadratic_bottleneck/` | `research/04-quadratic-bottleneck/` |
| `visible2_research/` | `research/05-visible-two-primary/` |
| `sparse_descent_research/` | `research/06-sparse-deck-descent/` |
| `rank1_amplification/` or flat rank-one ZIP | `research/07-rank-one-amplification/` |
| `mixed_laurent_research/results/` | `research/08-mixed-laurent/` |
| `fixed_c_research/results/` or flat fixed-$c$ ZIP | `research/09-fixed-c-product-bound/` |

Proofs occasionally refer to old `/mnt/data/...` paths. Those strings are intentionally unchanged in archival sources. Use this table or the full member mapping in the JSON inventory; there is no need to recreate the old sandbox paths to run the package code.

## Original versus added material

**Original evidence:** all files under `research/`, all source ZIPs, and both input attachments. Their bytes are covered by source hashes.

**Public-conversation preservation:** files under `context/conversation/`. These are identified transcriptions/extracts or source-derived handoffs from the public conversation, not recovered original filesystem files and not hidden reasoning traces. The early arbitrary-term report is retained because its underlying source package is absent. No unseen transcript, command log, or scratch file was reconstructed.

**Export additions:** root documentation, `docs/`, `metadata/`, `scripts/`, the GitHub workflow, and `checks/export/`. These add navigation, provenance checks, and orchestration of existing commands. They do not edit research proofs, repair mathematical arguments, or select a new theorem.

## Hashes and checks

Original package manifests are retained and checked in addition to a root `MANIFEST.sha256`. The root manifest covers the final repository files except itself. The archive file has a separate external SHA-256 sidecar, avoiding self-reference.

`source_inventory.json` maps each original source object. The root manifest is a snapshot-integrity tool, not a mathematical signature or independent certification. The new runner uses temporary copies so that timing fields and regenerated summaries cannot overwrite original observations. Export-time outputs are explicitly separated from the corresponding original files.

## Intentional redundancy and exclusions

The original ZIP and extracted member are both retained: the former is the exact submitted source container; the latter is the immediately runnable repository. Identical standalone uploads do not create a third copy. Original execution logs, discovery scripts, redundant independent implementations, and intermediate certificates have research value and remain present.

Temporary export staging, Python caches, new compiled executables, and disposable verification copies are excluded. No hidden `.git` history, environment cache, or unrelated workspace directory is included. No font files or external library installations are bundled.

## Limits

The export does not acquire files from other conversation windows or recreate missing original certificates. The [gap ledger](KNOWN_GAPS.md) distinguishes available derivations from unavailable packages. All external references are preserved bibliographically; no web research or downloading of literature was performed during the export.
