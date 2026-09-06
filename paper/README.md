# Optional typeset manuscript

The complete research product is the GitHub repository: [results/](../results/README.md), [research/](../research/README.md), code, data and certificates. This directory provides a typeset exposition of selected core results. It is not the only proof source and does not replace the full research notes.

Build with `python scripts/build_paper.py` from the repository root (PDFLaTeX required). Source publication metadata and `metadata.tex` remain author controlled; no author or affiliation is invented. Optional arXiv packaging remains available as an export operation, separate from GitHub source publishing.

To regenerate the full core-theory GitHub chapters, use `python scripts/build_theory.py` (Pandoc required only for regeneration, not reading or verification).
