# Optional manuscript submission checklist

The primary deliverable is the standalone research repository described in [the root README](../README.md). This checklist applies only to the optional typeset manuscript in `paper/` and its separate arXiv export; it is not the GitHub publication checklist. No author metadata, license, DOI, or successful remote submission is inferred.

## Required author-controlled decisions

Replace `paper/metadata.tex` with the approved author list and affiliations. Review the full manuscript, especially the new constant-8 consolidation proof and the scope of companion results. Confirm authorship of recovered mathematical notes and all imported code, choose appropriate licenses for code and manuscript, and settle acknowledgments/contribution statements. Update `publication.json` only after these decisions have actually been made. After intentional metadata edits or rebuilding the PDF, run `python scripts/write_manifest.py` to refresh the release snapshot; it first checks that retained original source bytes are unchanged. Complete citation metadata and any repository URL after a real public record exists.

`python scripts/check_release.py --publication` deliberately reports the currently missing approvals. The ordinary integrity check does not falsely require an arXiv identifier for an unpublished draft. A source archive can be produced using `--draft`, but that flag is not an approval or a claim of publication readiness in every administrative respect.

## Technical packaging

Build using `python scripts/build_paper.py`; inspect the resulting PDF. The manuscript uses ordinary PDFLaTeX and standard packages, no shell-escape computation, no external figures, and a directly included bibliography. The source package relocates the contents of `paper/` to its root, so `main.tex` is a top-level document and relative `\input` paths work from the submission root.

Use `python scripts/make_arxiv.py --draft` for the unapproved draft, or without `--draft` after the publication gate passes. The tarball contains TeX source and `anc/reproducibility/` with code, data, companion proofs, and exact verification reports. No executable is invoked by the paper build. No TeX source is placed inside the ancillary directory, and compiled manuscript PDFs and TeX intermediate files are excluded from the submission source archive.

After extracting the package, independently compile from its root with `pdflatex main.tex` three times. To reproduce the mathematics from the ancillary package, change directory to `anc/reproducibility` and run the core reproduction command. Companion-note paths cited in the bibliography are relative to this reproduction root. The independent GitHub source ZIP, built by `scripts/package_repository.py`, is the complete research product; its primary proofs and research programs do not live under `anc/`.

## Official sources checked on 6 September 2026

- arXiv, **Submit TeX/LaTeX**: https://info.arxiv.org/help/submit_tex.html
- arXiv, **Ancillary Files (data, code, images)**: https://info.arxiv.org/help/ancillary_files.html

The current official instructions support collections of TeX files, require correct root-relative paths, discourage extraneous/intermediate/output files, and specify the root `anc` directory for ancillary material. They require the submitter to inspect the system-generated PDF. The repository does not rely on the outdated claim that arXiv cannot process BibTeX; it simply uses an inline bibliography to reduce dependencies.

Technical compilation and local checks do not guarantee acceptance, endorsement, moderation outcome, or a particular arXiv category. Those decisions and the actual upload remain with the submitting authors.
