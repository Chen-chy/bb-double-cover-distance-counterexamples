#!/usr/bin/env python3
"""Recreate a round's original layout, including byte-identical deduplicated files.

No source is downloaded, edited, regenerated, or executed. The result is a
writable working copy. Archived files and original execution logs stay intact.
"""
from __future__ import annotations
import argparse
import json
import shutil
from pathlib import Path
from archive_common import ROOT, modules, safe_path, verified_bytes

MARKER = '.bb_archive_materialization.json'

def materialize(module_id: str, output: Path, *, force: bool = False) -> Path:
    table = modules()
    if module_id not in table:
        raise ValueError(f'Unknown module {module_id!r}; choose from {", ".join(table)}')
    output = output.resolve()
    if output.is_relative_to(ROOT / 'research') or output.is_relative_to(ROOT / 'provenance'):
        raise ValueError('Refusing to materialize over archived source/provenance.')
    destination = output / module_id
    if destination.exists():
        if not force:
            raise FileExistsError(f'{destination} exists; choose a new output or pass --force')
        marker = destination / MARKER
        if not marker.is_file() or json.loads(marker.read_text()).get('module') != module_id:
            raise ValueError('Refusing to replace a directory not created by this tool.')
        shutil.rmtree(destination)
    destination.mkdir(parents=True)
    for record in table[module_id]['files']:
        dst = safe_path(destination, record['original_path'])
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(verified_bytes(record))
    (destination / MARKER).write_text(json.dumps({
        'module': module_id,
        'source_archive_sha256': table[module_id]['source_archive_sha256'],
        'notice': 'Writable recreation of the original source layout; changes here do not update the archive.'
    }, indent=2) + '\n')
    return destination

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--module', choices=list(modules()))
    group.add_argument('--all', action='store_true')
    parser.add_argument('--output', type=Path, default=ROOT / '.work')
    parser.add_argument('--force', action='store_true', help='Replace only previously materialized module directories.')
    args = parser.parse_args()
    for mid in modules() if args.all else [args.module]:
        print(materialize(mid, args.output, force=args.force))

if __name__ == '__main__':
    main()
