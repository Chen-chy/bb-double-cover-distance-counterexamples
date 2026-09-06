#!/usr/bin/env python3
"""Check retained source integrity; optionally enforce author-controlled publication approvals."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--publication', action='store_true')
    parser.add_argument('--require-manifest', action='store_true', help='Reject a checkout without the release snapshot manifest')
    args = parser.parse_args()
    errors = []
    inventory = json.loads((ROOT/'provenance/import_map.json').read_text())
    retained = 0
    for record in inventory['files']:
        if record['stored_path']:
            p = ROOT/record['stored_path']
            retained += 1
            if not p.is_file() or sha(p) != record['sha256']:
                errors.append(f'Imported source bytes changed: {record["stored_path"]}')
    manifest = ROOT/'SHA256SUMS.txt'
    if args.require_manifest and not manifest.is_file():
        errors.append('Release manifest is missing; run scripts/write_manifest.py')
    if manifest.exists():
        for line in manifest.read_text().splitlines():
            digest, name = line.split('  ', 1)
            p = ROOT/name
            if not p.is_file() or sha(p) != digest:
                errors.append(f'Release manifest mismatch: {name}')
    if args.publication:
        status = json.loads((ROOT/'publication.json').read_text())
        for key in ('authors_and_affiliations_approved', 'rights_and_license_approved',
                    'manuscript_reviewed_by_authors'):
            if status.get(key) is not True:
                errors.append('Publication approval missing: '+key)
        if 'to be supplied' in (ROOT/'paper/metadata.tex').read_text():
            errors.append('Replace the author placeholder in paper/metadata.tex')
    print(json.dumps({'status': 'passed' if not errors else 'blocked',
                      'retained_member_mappings_checked': retained, 'errors': errors}, indent=2))
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
