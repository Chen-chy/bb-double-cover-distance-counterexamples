#!/usr/bin/env python3
"""Create deterministic, complete research source archives, not Python-only wheels."""
from __future__ import annotations
import argparse
import gzip
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tarfile
import zipfile
from write_manifest import ROOT, included


def source_files() -> list[Path]:
    paths = sorted(p for p in ROOT.rglob('*') if included(p))
    manifest = ROOT / 'SHA256SUMS.txt'
    if not manifest.is_file():
        raise ValueError('Run scripts/write_manifest.py before packaging')
    paths.append(manifest)
    for p in paths:
        if p.is_symlink():
            raise ValueError('Release archives do not follow symlinks: ' + str(p))
    return sorted(paths)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'dist')
    args = parser.parse_args()
    out = args.output.resolve()
    # Only dist/ or a directory wholly outside the checkout may hold build artifacts.
    if out == ROOT or (out.is_relative_to(ROOT) and not out.is_relative_to(ROOT / 'dist')):
        parser.error('Output must be dist/ (or its descendant) or outside the source checkout')
    for script in ('check_repository.py', 'check_release.py'):
        proc = subprocess.run([sys.executable, str(ROOT / 'scripts' / script)], cwd=ROOT)
        if proc.returncode: return proc.returncode
    try:
        paths = source_files()
        manifest_paths = {line.split('  ', 1)[1] for line in (ROOT / 'SHA256SUMS.txt').read_text().splitlines()}
        actual = {str(p.relative_to(ROOT)) for p in paths if p.name != 'SHA256SUMS.txt' or p.parent != ROOT}
        if actual != manifest_paths:
            raise ValueError('Manifest membership is stale; refresh it before packaging')
    except ValueError as exc:
        parser.error(str(exc))
    metadata = json.loads((ROOT / 'repository.json').read_text())
    prefix = metadata['name']
    out.mkdir(parents=True, exist_ok=True)
    zip_path = out / f'{prefix}.zip'
    tar_path = out / f'{prefix}.tar.gz'
    if any(p.exists() for p in (zip_path, tar_path)):
        parser.error('Archive already exists; use a new output directory rather than silently overwriting')
    with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for p in paths:
            name = prefix + '/' + p.relative_to(ROOT).as_posix()
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, p.read_bytes())
    with tar_path.open('wb') as raw:
        with gzip.GzipFile(filename='', mode='wb', fileobj=raw, mtime=0, compresslevel=9) as gz:
            with tarfile.open(fileobj=gz, mode='w', format=tarfile.PAX_FORMAT) as archive:
                for p in paths:
                    data = p.read_bytes()
                    info = tarfile.TarInfo(prefix + '/' + p.relative_to(ROOT).as_posix())
                    info.size = len(data)
                    info.mode = 0o644
                    info.mtime = 0
                    archive.addfile(info, io.BytesIO(data))
    report = {'status': 'passed', 'version': metadata['version'], 'files': len(paths),
              'scope': 'Complete standalone research source; no Git history. Git bundle is produced separately.',
              'artifacts': [{'name': p.name, 'bytes': p.stat().st_size,
                             'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in (zip_path, tar_path)]}
    (out / 'archive-report.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
