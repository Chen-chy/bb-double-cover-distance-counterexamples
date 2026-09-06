# Mixed-parity Laurent certificate

Run `sh run_all.sh` using Python 3.10 or newer. This runs both the sparse-set verifier and the separate bit-polynomial audit. No external packages are needed.

`proof.md` gives the uniform proofs. `verification_summary.json` records the executed checks. The theorem compares complete Laurent minima for the stated arithmetic-progression subclass. It is not a proof or refutation of factor three for all mixed-parity pairs.

The verification script deliberately does not label decoder or heuristic outputs as minima. Its finite matrix calculations certify witnesses, not full finite distances.
