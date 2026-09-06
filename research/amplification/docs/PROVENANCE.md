# Provenance and preservation policy

## Original payloads

`provenance/source_inventory.json` is the authoritative map from eight source
ZIPs to canonical repository files. It records original archive hashes, original
member names and ZIP timestamps, sizes, CRCs, content SHA-256 hashes, stored paths,
and standalone attachment matches. ZIP timestamps describe the retained
containers; they are not inferred timestamps of mathematical discovery.

`provenance/original_manifest_checks.json` records the successful checks of all
eight supplied manifests before reorganization. `tools/check_repository.py`
rechecks those original manifests against the mapped bytes even when a repeated
file is stored elsewhere. No original source code was patched to accommodate the
new layout.

## Deduplication without changing runtime semantics

Only byte-identical files were deduplicated. This includes repeated inherited
closure tables, repeated auditor source, a prior report nested in a later round,
and stdout files identical to a JSON result. Different implementations,
different output schemas, and semantically similar but nonidentical records
remain separate.

The map in `provenance/deduplicated_paths.json` recreates all 27 repeated paths.
The archive deliberately does **not** use symlinks for this: some historical
scripts call `Path(__file__).resolve()` to locate their own local certificate
files. A symlink to another round would change those semantics. Materialization
instead makes ordinary byte-identical copies in a disposable working tree.
Thus source bytes occur once in the repository, while the original program
layout is faithfully restored for execution.

## Conversation-derived recovery

`provenance/recovered_sources.json` identifies the separate provenance class of
recovered early code and proof reading copies. They are source-text recoveries,
not authenticated original payloads. Original logs or full sampled datasets are
not synthesized. See [coverage and gaps](ARCHIVE_GAPS.md).

The historical research reports retain their original status labels, vocabulary,
proof scopes, and unresolved next steps. New overview documents distinguish what
was later resolved or superseded. They do not edit old reports to make them look
as though the latest theorem was already known.

## Original runs and export-time runs

Original JSON summaries and logs under `research/` are unchanged. Export checks
ran in disposable materialized copies. Their command lines, stdout/stderr,
return codes, environments, and elapsed times are in
`checks/export_2026-09-06/`. Changed working-copy outputs, largely timings, are
listed there; they did not overwrite original evidence.

Some claim-specific certificates are binary or compressed. They are retained
as research data, not replaced by narrative summaries. Deterministic lower
certificates are distinguished from capped discovery traces.

## Release integrity

The final top-level `SHA256SUMS` covers all delivered files except itself. The
external ZIP digest in the release checksum file authenticates the delivered
container. Checking either hash manifest is an integrity check, not a proof of
mathematical validity. Generated working directories and caches are excluded.

No repository-wide authorship or license assignment is implied by preserving
content. Bibliographic attributions stay with their sources; independent code
paths are not described as human peer review.
