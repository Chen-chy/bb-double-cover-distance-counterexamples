# Amplification branch (preserved)

Read each `research/*/REPORT.md` for proofs, assumptions, and failed approaches. The root of this branch was relocated without changing those source files. The convenience command from the overall repository root is:

```sh
python research/amplification/tools/run_checks.py --profile audit --output checks/amp-local
```

Use a fresh output directory. The driver materializes complete working copies, including declared prior-round dependencies. Its `regenerate` profile requires explicit permission and can be much more expensive. The original general constant 32 is superseded by the explicitly new consolidation proof of 8 in the main manuscript, not retroactively rewritten here.
