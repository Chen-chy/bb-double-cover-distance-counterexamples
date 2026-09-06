#!/usr/bin/env python3
"""Check complete-repository structure, public-source integrity, and maintained links.

This is a technical and provenance gate, not an authorship, license, peer-review,
or formal-proof approval. Original research documents are preserved byte-for-byte;
strict link checking applies to maintained reading editions and repository guides.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def without_fences(text: str) -> str:
    return re.sub(r'^(`{3,}|~{3,})[^\n]*\n.*?^\1\s*$', '', text, flags=re.M | re.S)


def anchors(path: Path) -> set[str]:
    text = without_fences(path.read_text(encoding='utf-8'))
    found = set(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)', text))
    counts: dict[str, int] = {}
    for title in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', text, flags=re.M):
        title = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', title)
        title = re.sub(r'<[^>]+>', '', title).lower().strip()
        title = re.sub(r'[^\w\- ]', '', title, flags=re.UNICODE).replace(' ', '-')
        number = counts.get(title, 0)
        counts[title] = number + 1
        found.add(title + (f'-{number}' if number else ''))
    return found


def validate() -> dict:
    errors: list[str] = []
    warnings = ["Symbolic proofs and finite audits are not independent peer review or formal verification.",
                "Original historical records can reference unavailable material; see results/HISTORY_AND_LIMITS.md.",
                "No reuse license or research authorship is inferred by this technical check."]
    required = ['REPORT.md', 'REPORT.en.md', 'results/STATUS.md', 'results/review_policy.json', 'README.md', 'README.en.md', 'results/README.md', 'results/CLAIMS.md',
                'results/catalog.json', 'results/HISTORY_AND_LIMITS.md', 'results/OPEN_PROBLEMS.md',
                'docs/REPRODUCIBILITY.md', 'docs/PUBLISH_GITHUB.md', 'repository.json',
                'bbcover/catalog.json', 'scripts/package_repository.py', 'scripts/publish_github.py',
                '.github/workflows/ci.yml', '.github/workflows/research-audit.yml',
                '.github/workflows/release-source.yml']
    for name in required:
        if not (ROOT / name).is_file(): errors.append('Missing required file: ' + name)
    inventory = json.loads((ROOT / 'provenance/import_map.json').read_text())
    retained = set()
    member_count = 0
    for record in inventory['files']:
        name = record['stored_path']
        if not name: continue
        p = (ROOT / name).resolve()
        member_count += 1
        retained.add(name)
        if not p.is_relative_to(ROOT) or not p.is_file() or digest(p) != record['sha256']:
            errors.append('Imported source missing or changed: ' + name)
    data = json.loads((ROOT / 'results/catalog.json').read_text())
    rows = data['results']
    if len(rows) != 104 or len({r['id'] for r in rows}) != len(rows):
        errors.append('The complete claim register must contain 104 unique records')
    if (ROOT / 'results/catalog.json').read_bytes() != (ROOT / 'bbcover/catalog.json').read_bytes():
        errors.append('Installed and repository catalogs differ')
    references_checked = 0
    cache: dict[Path, set[str]] = {}

    def check_target(source: Path, target: str, label: str) -> None:
        nonlocal references_checked
        if urlsplit(target).scheme or target.startswith('//'): return
        if not target: return
        plain, _, frag = target.partition('#')
        p = (source.parent / unquote(plain)).resolve() if plain else source
        references_checked += 1
        if not p.is_relative_to(ROOT) or not p.exists():
            errors.append(f'{label}: missing or external local target {target}')
        elif frag and p.is_file() and p.suffix.lower() == '.md':
            if p not in cache: cache[p] = anchors(p)
            if unquote(frag) not in cache[p]:
                errors.append(f'{label}: missing heading/anchor {target}')

    for row in rows:
        for name in row['proofs'] + row['evidence']:
            check_target(ROOT / '_root_', name, row['id'])
    maintained = [p for p in ROOT.glob('*.md')]
    maintained += list((ROOT / 'docs').glob('*.md'))
    maintained += list((ROOT / 'results').rglob('*.md'))
    maintained += [ROOT / p for p in ('research/README.md', 'research/beyond-trinomials/README.md',
                                       'certificates/README.md', 'paper/README.md', 'provenance/README.md')]
    maintained = sorted(set(p for p in maintained if p.is_file() and str(p.relative_to(ROOT)) not in retained))
    for p in maintained:
        text = without_fences(p.read_text(encoding='utf-8'))
        for match in re.finditer(r'\[[^\]\n]+\]\(([^)\n]+)\)', text):
            target = match[1]
            if target.startswith('<') and '>' in target: target = target[1:target.index('>')]
            elif ' "' in target: target = target.split(' "', 1)[0]
            check_target(p, target, str(p.relative_to(ROOT)))
        # Absolute sandbox paths are not portable navigation targets.
        if re.search(r'\]\((?:sandbox:|/mnt/data/)', text):
            errors.append('Nonportable sandbox link: ' + str(p.relative_to(ROOT)))
    generated = {}
    for script in ('build_theory.py', 'build_notes.py', 'build_catalog.py', 'check_report.py'):
        proc = subprocess.run([sys.executable, str(ROOT / 'scripts' / script), '--check'],
                              cwd=ROOT, capture_output=True, text=True)
        generated[script] = 'passed' if proc.returncode == 0 else 'failed'
        if proc.returncode: errors.append('Stale generated output: ' + script + ': ' + proc.stdout[-1000:] + proc.stderr[-1000:])
    # Narrow, offline signature screen. It does not claim exhaustive secret detection.
    token_pattern = re.compile(rb'(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{50,}|-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----)')
    screened = 0
    for p in ROOT.rglob('*'):
        parts = p.relative_to(ROOT).parts
        if not p.is_file() or any(x in {'.git', '.build', 'build', '.venv', 'venv', '__pycache__', 'dist', 'work'} or x.endswith('.egg-info') for x in parts): continue
        if p.name in {'.env', 'id_rsa', 'id_ed25519'}:
            errors.append('Private credential filename in release tree: ' + str(p.relative_to(ROOT)))
        if p.suffix.lower() in {'.md', '.py', '.yml', '.yaml', '.json', '.tex', '.toml', '.txt', '.sh'}:
            screened += 1
            if token_pattern.search(p.read_bytes()):
                errors.append('Potential secret signature; inspect locally: ' + str(p.relative_to(ROOT)))
    theory = json.loads((ROOT / 'provenance/theory_render_audit.json').read_text())
    notes = json.loads((ROOT / 'provenance/note_render_audit.json').read_text())
    return {'status': 'passed' if not errors else 'failed', 'retained_member_mappings_checked': member_count,
            'unique_retained_source_files': len(retained), 'complete_result_records': len(rows),
            'maintained_markdown_files_checked': len(maintained), 'local_targets_checked': references_checked,
            'theory_chapters': theory['chapters'], 'display_math_coverage': [theory['display_math_rendered'], theory['display_math_in_source']],
            'full_research_notes': len(notes['notes']), 'generated_checks': generated,
            'narrow_secret_screen_files': screened, 'warnings': warnings, 'errors': errors}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = validate()
    text = json.dumps(result, indent=2, ensure_ascii=False) + '\n'
    if args.output:
        p = args.output.resolve()
        if not (ROOT / 'checks').resolve() in p.parents:
            parser.error('Check output must be inside checks/ to avoid overwriting source')
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding='utf-8')
    print(text, end='')
    return result['status'] != 'passed'


if __name__ == '__main__':
    raise SystemExit(main())
