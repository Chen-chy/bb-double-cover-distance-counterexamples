#!/usr/bin/env python3
"""Refresh the release manifest after intentional edits/builds, preserving imported source integrity."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def included(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    if path.name == 'SHA256SUMS.txt' and len(rel.parts) == 1:
        return False
    if any(part in {'.git', '.build', 'build', '.venv', 'venv', '__pycache__', 'dist', '.pytest_cache', '.mypy_cache'} or part.endswith('.egg-info')
           for part in rel.parts):
        return False
    if rel.parts[0] == 'checks' and 'work' in rel.parts:
        return False
    if path.suffix in {'.pyc', '.pyo'}:
        return False
    if rel.parts[0] == 'checks' and (len(rel.parts) < 2 or rel.parts[1] != 'release'):
        return False
    return path.is_file()


def main() -> None:
    source = json.loads((ROOT/'provenance/import_map.json').read_text())
    for record in source['files']:
        if record['stored_path']:
            p = ROOT/record['stored_path']
            if not p.is_file() or digest(p) != record['sha256']:
                raise SystemExit('Refusing to bless changed original source: '+record['stored_path'])
    paths = [p for p in sorted(ROOT.rglob('*')) if included(p)]
    manifest = ''.join(digest(p)+'  '+str(p.relative_to(ROOT))+'\n' for p in paths)
    (ROOT/'SHA256SUMS.txt').write_text(manifest)
    print(json.dumps({'manifest': 'SHA256SUMS.txt', 'files': len(paths),
                      'retained_original_source_integrity': 'passed'}, indent=2))


if __name__ == '__main__':
    main()
