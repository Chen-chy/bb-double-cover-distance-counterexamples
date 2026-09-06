# Recovered earlier source text — not an original mounted snapshot

The original distance-four report/ZIP and original output files are not present
in this runtime. The three Python programs here are archival transcriptions of
complete source visible in earlier tool-call messages in this conversation.
`verify4_independent.py` includes the later visible portability edit changing its
output to `Path(__file__).with_name(...)`. These are recoveries of existing work,
not newly designed proof/search algorithms.

There is no original-file hash against which to authenticate the transcription.
Their present hashes are recorded in the release manifest and recovery inventory.
Export-time rerun outputs are separately labeled; they are not old logs.

`verify4_independent.py` exhausts 10,044 incidence-pairing checks with exact integer
arithmetic. `verify_weight_four_sympy.py` uses the independent normalized
2,016-presentation HNF/SNF calculation. `verify_metric_family.py` checks the
four-state certificate and finite instances of the mu=L/3+1 separation family.
The [conversation-derived report](../02_distance4_and_transfer_metric.md) supplies
the uniform proof and interpretation.

Run in a writable copy, not in the archival source directory:

```sh
mkdir -p .work
cp -R history/recovered_round2 .work/recovered_round2
cd .work/recovered_round2
python verify4_independent.py
python verify_weight_four_sympy.py
python verify_metric_family.py
```

Python 3.10+ is required. Only the second program needs SymPy. Do not run with
`python -O`; exact assertions are part of the checks. The two broad distance-six
enumerations in the later intact bundle are separate programs and are not run
by these recovered checks.
