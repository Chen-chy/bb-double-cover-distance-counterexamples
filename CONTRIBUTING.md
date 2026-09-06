# Contributing

Use a pull request for code or mathematical corrections. Identify the claim ID, state the exact group/check hypotheses, distinguish full distance from restricted minima, and include a reproducible command or a complete symbolic argument.

Do not modify imported mathematical source files in place merely to update their historical status. Add a versioned correction and an explicit catalog overlay, preserving the source inventory. The two independent verifier implementations must remain independent; a convenience refactor is not a reason to make both depend on one shared oracle.

Before proposing changes, run the unit tests, `scripts/check_repository.py`, and the core profile. Changes affecting original audits should also run the extended profile with a fresh output directory. Record incomplete searches and timeouts honestly. For a new exact minimum, provide an attaining word, nonboundary proof, exhaustive or all-degree lower certificate, and an explanation of completeness.

Publication authority and any license change must be approved by the actual rights holders. See `NOTICE.md` and `docs/DEVELOPMENT.md`.
