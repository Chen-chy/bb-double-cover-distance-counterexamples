#!/usr/bin/env python3
"""Run archived checks in disposable copies without changing original evidence.

This wrapper adds no mathematical tests. Commands are the existing package
verifiers (verify mode) or original reproduction pipelines (rebuild mode).
"""
from __future__ import annotations
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def snapshot(directory: Path) -> dict[str, str]:
    return {str(p.relative_to(directory)): sha(p) for p in sorted(directory.rglob('*'))
            if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc'}


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mode', choices=('verify', 'rebuild'), default='verify')
    parser.add_argument('--stage', action='append', help='Repeat to select stage IDs; default: all.')
    parser.add_argument('--output', default='checks/local', help='Report directory, relative to repository or absolute.')
    parser.add_argument('--timeout', type=float, default=1800, help='Maximum seconds for each existing command.')
    parser.add_argument('--list', action='store_true', help='Print selected commands without executing.')
    args = parser.parse_args()
    specs = json.loads((ROOT/'metadata/checks.json').read_text())
    known = {s['id'] for s in specs}
    if args.stage and set(args.stage) - known:
        parser.error('Unknown stage(s): '+', '.join(sorted(set(args.stage)-known)))
    specs = [s for s in specs if not args.stage or s['id'] in args.stage]
    if args.list:
        for s in specs:
            print(s['id'])
            for command in s[args.mode]:
                print('  '+' '.join(command))
        return 0
    out = Path(args.output)
    out = out if out.is_absolute() else ROOT/out
    out = out.resolve()
    if out == ROOT or ROOT/'research' in out.parents or out == ROOT/'research':
        parser.error('Output must not replace original research files.')
    out.mkdir(parents=True, exist_ok=True)
    if (out/'report.json').exists():
        parser.error('Output already contains report.json; choose a fresh directory to preserve that run.')
    env = os.environ.copy()
    env['PYTHONDONTWRITEBYTECODE'] = '1'
    env['PYTHONUNBUFFERED'] = '1'
    env['PATH'] = str(Path(sys.executable).parent)+os.pathsep+env.get('PATH', '')
    report: dict = {
        'purpose': 'Execution of existing archived verification commands; not a new mathematical audit.',
        'mode': args.mode,
        'started_utc': now(),
        'python': sys.version,
        'platform': platform.platform(),
        'byteorder': sys.byteorder,
        'stages': [],
        'original_evidence_modified': False,
    }
    try:
        import sympy
        report['sympy_version'] = sympy.__version__
    except ImportError:
        report['sympy_version'] = None
    def save() -> None:
        (out/'report.json').write_text(json.dumps(report, indent=2)+'\n')
    save()
    all_ok = True
    for spec in specs:
        source = ROOT/spec['directory']
        before_source = snapshot(source)
        stage_out = out/spec['id']
        stage_out.mkdir(exist_ok=True)
        entry: dict = {'id': spec['id'], 'source_directory': spec['directory'], 'commands': [], 'passed': True}
        report['stages'].append(entry)
        print(f'CHECKING {spec["id"]}', flush=True)
        with tempfile.TemporaryDirectory(prefix='bb-archival-check-') as tmp:
            cwd = Path(tmp)/'package'
            shutil.copytree(source, cwd)
            for index, template in enumerate(spec[args.mode], 1):
                substitutions = {'{python}': sys.executable, '{cxx}': os.environ.get('CXX', 'g++')}
                command = [substitutions.get(arg, arg) for arg in template]
                stdout = stage_out/f'{index:02d}-stdout.log'
                stderr = stage_out/f'{index:02d}-stderr.log'
                record = {'command_template': template, 'command': command, 'started_utc': now(),
                          'stdout': str(stdout.relative_to(out)), 'stderr': str(stderr.relative_to(out))}
                start = time.monotonic()
                print('  '+' '.join(template), flush=True)
                try:
                    with stdout.open('wb') as f_out, stderr.open('wb') as f_err:
                        result = subprocess.run(command, cwd=cwd, env=env, stdout=f_out, stderr=f_err,
                                                timeout=args.timeout, check=False)
                    record['returncode'] = result.returncode
                    record['passed'] = result.returncode == 0
                except subprocess.TimeoutExpired:
                    record.update(returncode=None, passed=False, error='timeout')
                except OSError as exc:
                    record.update(returncode=None, passed=False, error=f'{type(exc).__name__}: {exc}')
                record['elapsed_seconds'] = round(time.monotonic()-start, 6)
                record['finished_utc'] = now()
                record['stdout_sha256'] = sha(stdout)
                record['stderr_sha256'] = sha(stderr)
                entry['commands'].append(record)
                if not record['passed']:
                    entry['passed'] = False
                    all_ok = False
                    print('  FAILED (see logs)', flush=True)
                    break
                print('  passed', flush=True)
                save()
            after = snapshot(cwd)
            changes = []
            for rel, digest in after.items():
                if before_source.get(rel) == digest:
                    continue
                file = cwd/rel
                # Keep reproducibility outputs, not newly compiled executable files.
                retain = file.suffix in {'.json', '.tsv', '.log', '.txt', '.bin', '.md', '.csv'}
                item = {'file': rel, 'before_sha256': before_source.get(rel), 'after_sha256': digest,
                        'retained_as_export_output': retain}
                if retain:
                    target = stage_out/'outputs'/rel
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(file, target)
                    item['output_path'] = str(target.relative_to(out))
                changes.append(item)
            entry['changed_or_new_workcopy_files'] = changes
            entry['deleted_workcopy_files'] = sorted(set(before_source)-set(after))
        entry['original_files_unchanged'] = snapshot(source) == before_source
        if not entry['original_files_unchanged']:
            entry['passed'] = False
            all_ok = False
            report['original_evidence_modified'] = True
        save()
    report['finished_utc'] = now()
    report['all_selected_commands_passed'] = all_ok
    report['command_count'] = sum(len(s['commands']) for s in report['stages'])
    save()
    print('All selected existing commands passed.' if all_ok else 'One or more checks failed.', flush=True)
    return 0 if all_ok else 1

if __name__ == '__main__':
    raise SystemExit(main())
