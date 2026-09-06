[研究结果总目录](../README.md) · [结论登记表](../CLAIMS.md) · [上一章](06-certificate-algorithms.md)

> 本章包含完整论证，可独立于 PDF 阅读。符号、范围和引用见正文；GitHub 版命题编号独立于排版稿。

<a id="app-reproduction"></a>

# Reproduction and evidence boundaries

The accompanying repository separates new mathematical exposition, unchanged certificate implementations, archived exploratory work, and freshly generated execution reports. The principal commands, run from the repository root, are

```
python -m unittest discover -s tests -v
python scripts/reproduce.py --profile core --output checks/local
python scripts/reproduce.py --profile extended --output checks/extended
python scripts/build_paper.py
```

The core profile needs only the Python standard library. It runs the new interface tests and cofactor-transport identities, executes all four standalone certificate programs, and cross-compares their matrices and full circuit outputs. An explicit timeout is recorded as incomplete, never as a successful exclusion. The original verifiers have no shared dependency on the convenience package.

The extended profile additionally requires SymPy and a C++ compiler and invokes the two archived audit drivers on materialized working copies. It reruns the retained exact verification commands, including higher-rank replacements and rank-one optimization certificates. It does not claim to regenerate every exploratory scan or every expensive classification from scratch. The precise commands, return codes, execution times, interpreter information, source hashes, and output hashes are retained. Machine checks of determinant identities support implementation review; they do not constitute a formal proof of the universal theorems.

The input inventory records each member of the three supplied archives with a content hash and either its retained destination or an explicit omission reason. Duplicate nested archives, generated caches and binaries, private conversation exports, and an unrelated third-party source PDF are excluded from the public package. The cited source paper is identified by version and hash instead of redistributed. Archived source files are not silently rewritten to make their historical status agree with the new manuscript.

Two distinctions matter for independent review. First, older research summaries referred to unavailable early certificate bundles; the later supplied certificate archive repairs the two finite counterexamples, but does not regenerate every earlier infinite-family or small-weight classification. Second, the constant $32$ belongs to the archived general upper-bound proof, whereas the constant $8$ and improved truncated amplification constant are derived in this manuscript by Lemma [8](03-polynomial-bounds.md#lem-transport). These are proof-based consolidation additions, not previously recorded numerical results. The author list, affiliations, acknowledgments, software license, and publication metadata must be supplied or approved by the research authors before public submission.
