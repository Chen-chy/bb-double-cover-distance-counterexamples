# Early univariate tools recovered from visible source text

These files are archival transcriptions of complete source shown in the first
round's tool calls. The final visible edits (C++ capacity NW=16 and relative
Python paths) are incorporated. Original files, manifests, and most output logs
are unavailable; present hashes authenticate only this exported transcription.

`algebra.py`, `circuit_search.cpp`, and `independent_search.py` preserve the early
integer-polynomial, matrix, circuit, and independent polynomial-oracle tools.
The C++ interface is positional and differs from round 03's line protocol.
The independent Python program is restricted to the original seed periods.

`template_search.py` and `random_search.py` are **historical discovery scripts**.
They were not rerun for the export. The original template JSON and partial random
progress log are unavailable. In particular, the original random run did not
finish its entire intended range. The presence of a script is not evidence that
all its cases ran. Use intact round 03 records for preserved broad-search data.

A fresh, writable copy is required before running any of these tools:

```sh
mkdir -p .work
cp -R history/recovered_round1 .work/recovered_round1
cd .work/recovered_round1
g++ -O3 -std=c++17 circuit_search.cpp -o circuit_search
./circuit_search 39 0 8 25 0 2 13 4
./circuit_search 78 0 8 25 0 2 13 12
python independent_search.py 78 12
```

No original raw output is inferred or fabricated from these programs. The
later intact seed verifiers and their archived outputs remain the primary
reproducible evidence. These recovered predecessors preserve implementation
history, not a newly independent research result.

`verify_research.py` preserves the original all-in-one orchestration source. Its
full historical run additionally requires the unavailable `template_results.json`
and `random_progress.txt`. It was **not** rerun end-to-end, and no empty or
synthetic replacement files were supplied. Its direct seed dependencies are
present, but the intact round 03 audit is the recommended complete seed path.
