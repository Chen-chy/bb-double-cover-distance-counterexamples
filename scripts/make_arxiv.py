#!/usr/bin/env python3
"""Build a clean TeX source tarball and a self-contained anc/reproducibility tree.

No upload is performed. Publication mode requires author approvals; --draft
allows a technically compilable source package with explicitly pending metadata.
"""
import argparse
import gzip
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tarfile

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_SUFFIXES = {'.pyc','.pyo','.pdf','.tex','.aux','.toc','.out','.synctex','.zip'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT/'dist/arxiv-source.tar.gz')
    parser.add_argument('--draft', action='store_true', help='Allow pending author/rights approvals; never submit automatically')
    args = parser.parse_args()
    check_command = [sys.executable, str(ROOT/'scripts/check_release.py')]
    if not args.draft:
        check_command.append('--publication')
    subprocess.run(check_command, check=True)
    files = {}
    for p in sorted((ROOT/'paper').rglob('*.tex')):
        files[str(p.relative_to(ROOT/'paper'))] = p.read_bytes()
    # All retained mathematical/code evidence is ancillary. No TeX or third-party PDFs enter anc/.
    for folder in ('bbcover','tests','certificates','archive','research','results','provenance','data','docs'):
        for p in sorted((ROOT/folder).rglob('*')):
            if p.is_file() and p.suffix not in EXCLUDED_SUFFIXES and not any(
                    part.startswith('.') or part == '__pycache__' for part in p.relative_to(ROOT).parts):
                files['anc/reproducibility/'+str(p.relative_to(ROOT))] = p.read_bytes()
    for name in ('scripts/reproduce.py', 'scripts/verify_lattice_transport.py',
                 'requirements-research.txt', 'NOTICE.md', 'README.md', 'README.zh-CN.md',
                 'publication.json'):
        files['anc/reproducibility/'+name] = (ROOT/name).read_bytes()
    # Release summaries and fresh outputs, but not compiler caches or materialized working trees.
    for p in sorted((ROOT/'checks/release').rglob('*')):
        rel = p.relative_to(ROOT)
        if p.is_file() and 'work' not in rel.parts and '__pycache__' not in rel.parts and p.suffix not in {'.pdf','.pyc','.tex'}:
            files['anc/reproducibility/'+str(rel)] = p.read_bytes()
    files['anc/README.txt'] = (
        'Reproduction: cd reproducibility; python scripts/reproduce.py --profile core --output checks/local\n'
        'The paper TeX files are at the submission root. No code executes during TeX compilation.\n'
        'The companion proof notes are under reproducibility/research at the paths cited in the paper.\n'
        'This source package does not constitute an upload, license grant, or author approval.\n'
    ).encode()
    ancillary = {name: data for name, data in files.items() if name.startswith('anc/reproducibility/')}
    prefix = 'anc/reproducibility/'
    manifest = ''.join(hashlib.sha256(data).hexdigest()+'  '+name[len(prefix):]+'\n'
                       for name, data in sorted(ancillary.items()))
    files[prefix+'ANCILLARY_SHA256SUMS.txt'] = manifest.encode()
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    # Stable tar metadata; source-byte or content changes remain visible in checksums.
    with output.open('wb') as raw:
        with gzip.GzipFile(fileobj=raw, mode='wb', filename='', mtime=0) as gz:
            with tarfile.open(fileobj=gz, mode='w') as tar:
                for name, data in sorted(files.items()):
                    info = tarfile.TarInfo(name)
                    info.size = len(data)
                    info.mtime = 1788739200
                    info.mode = 0o644
                    tar.addfile(info, io.BytesIO(data))
    print(json.dumps({'output': str(output), 'files': len(files), 'bytes': output.stat().st_size,
                      'mode': 'draft_pending_author_approval' if args.draft else 'approved_local_package',
                      'sha256': hashlib.sha256(output.read_bytes()).hexdigest()}, indent=2))


if __name__ == '__main__':
    main()
