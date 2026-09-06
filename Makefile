PYTHON ?= python3
OUT ?= checks/local

.PHONY: test check core extended homology docs notes catalog manifest package paper arxiv manuscript-check

test:
	$(PYTHON) -m unittest discover -s tests -v

check:
	$(PYTHON) scripts/check_repository.py

core:
	$(PYTHON) scripts/reproduce.py --profile core --output $(OUT)

extended:
	$(PYTHON) scripts/reproduce.py --profile extended --output $(OUT)

homology:
	$(PYTHON) scripts/verify_homology_history.py --output $(OUT)

docs:
	$(PYTHON) scripts/build_theory.py
	$(PYTHON) scripts/build_notes.py
	$(PYTHON) scripts/build_catalog.py

notes:
	$(PYTHON) scripts/build_notes.py

catalog:
	$(PYTHON) scripts/build_catalog.py

manifest:
	$(PYTHON) scripts/write_manifest.py

package:
	$(PYTHON) scripts/check_repository.py
	$(PYTHON) scripts/write_manifest.py
	$(PYTHON) scripts/package_repository.py

# Optional manuscript outputs, not prerequisites for repository use.
paper:
	$(PYTHON) scripts/build_paper.py

arxiv:
	$(PYTHON) scripts/make_arxiv.py

manuscript-check:
	$(PYTHON) scripts/check_release.py --publication
