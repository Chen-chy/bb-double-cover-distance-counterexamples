# Citing this repository

Use the repository title, version tag and the exact commit used for the computation:

> *BB double-cover research: complete results, proofs, certificates and code*. Version 0.2.0. Git tag `v0.2.0`; include the actual repository URL and commit SHA from the copy used.

Obtain the exact revision with `git rev-parse HEAD`. Cite a claim by its stable identifier, for example `CEX-UP`, `DIST-UPPER`, `AMP-LINEAR-01` or `DEG-P15`, and identify the relevant proof and verifier. A run-specific claim should also identify `report.json` and its SHA-256.

No human author list, affiliation, DOI, arXiv identifier for this work or remote repository URL has been invented. The authors can add an approved `CITATION.cff` later; an optional manuscript template is under `paper/`. The Git packaging identity is not a research-author attribution.

External research is cited separately in [results/REFERENCES.md](results/REFERENCES.md). The earlier three supplied archives and all retained members are attributed by [provenance/import_map.json](provenance/import_map.json).

The initial local packaging commit uses the non-author identity `BBcover repository build <repository-build@invalid>`. This records the assembly step only. It must not be copied into research-author metadata.
