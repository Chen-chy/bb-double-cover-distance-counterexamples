#!/usr/bin/env python3
"""Run retained verification programs in disposable, fully materialized round trees.

The audit profile checks existing certificates and bounded identity tests. It
does not run the broad discovery scans or the two exhaustive d=6 classifications.
Regeneration is explicit and may be substantially more expensive. A timeout is
an INCOMPLETE CHECK, never a mathematical lower-bound certificate.
"""
from __future__ import annotations
import argparse
import datetime as dt
import importlib.metadata
import json
import os
from pathlib import Path
import platform
import shutil
import signal
import subprocess
import sys
import time
from archive_common import ROOT, modules
from materialize import materialize

AUDIT = {
 '03_amplification_search': [
    ['g++', '-O3', '-std=c++17', 'search.cpp', '-o', 'search'],
    ['g++', '-O3', '-std=c++17', 'search_general.cpp', '-o', 'search_general'],
    ['g++', '-O3', '-std=c++17', 'mitm.cpp', '-o', 'mitm'],
    ['{python}', 'verify_theorems.py'],
    ['{python}', 'verify_search.py'],
    ['{python}', 'independent_search.py'],
    ['./mitm'],
 ],
 '04_distance6_obstruction': [['{python}', 'verify_presentations_sympy.py']],
 '05_compact_survival': [['{python}', 'audit_finite_certificates.py'],
                         ['{python}', 'verify_mechanisms.py']],
 '06_linear_compact_replacement': [
    ['{python}', 'audit_replacement_certificates.py'],
    ['{python}', 'verify_sparse_generators.py'],
    ['{python}', 'verify_embeddings.py'],
    ['{python}', 'verify_sharpness.py'],
 ],
 '07_rank_one_resonance': [['{python}', 'audit_certificates.py'],
                          ['{python}', 'check_seed_coordinates.py']],
 '08_slope21_shortening': [['{python}', 'audit_certificates.py'],
                          ['{python}', 'verify_structure.py']],
 '09_joint_completion': [['{python}', 'verify_graph.py'],
                         ['{python}', 'verify_components.py'],
                         ['{python}', 'verify_majority_control.py'],
                         ['{python}', 'verify_pareto.py']],
 '10_nonlocal_exchange': [['{python}', 'run_all.py']],
}
REGENERATE = {
 '03_amplification_search': [['{python}', 'verify_all.py']],
 '04_distance6_obstruction': [['{python}', 'run_all.py']],
 '05_compact_survival': [['{python}', 'run_all.py']],
 '06_linear_compact_replacement': [['{python}', 'run_all.py']],
 '07_rank_one_resonance': [['{python}', 'run_all.py']],
 '08_slope21_shortening': [['{python}', 'run_exact.py'], ['{python}', 'audit_certificates.py'],
                          ['{python}', 'verify_structure.py']],
 '09_joint_completion': AUDIT['09_joint_completion'],
 '10_nonlocal_exchange': [['{python}', 'make_fixed_certificate.py'], ['{python}', 'run_all.py']],
}

def stamp() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()

def environment() -> dict:
    packages = {}
    for name in ['sympy', 'numpy']:
        try:
            packages[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            packages[name] = None
    compiler = shutil.which('g++')
    version = subprocess.check_output([compiler, '--version'], text=True).splitlines()[0] if compiler else None
    return {'python': sys.version, 'platform': platform.platform(), 'packages': packages,
            'compiler': version, 'python_optimized': bool(sys.flags.optimize)}

def main() -> None:
    if sys.flags.optimize:
        raise SystemExit('Do not use python -O: historical auditors rely on assert statements.')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profile', choices=['audit', 'regenerate'], default='audit')
    parser.add_argument('--module', action='append', choices=list(modules()))
    parser.add_argument('--output', type=Path, default=ROOT / '.work' / 'check_runs')
    parser.add_argument('--timeout', type=float, default=300.0,
                        help='Per-command timeout in seconds; 0 disables it. Timeout means incomplete, not exclusion.')
    parser.add_argument('--allow-regeneration', action='store_true')
    parser.add_argument('--list', action='store_true', help='Print the planned commands without executing.')
    args = parser.parse_args()
    table = AUDIT if args.profile == 'audit' else REGENERATE
    selected = args.module or list(table)
    if args.list:
        print(json.dumps({m: table[m] for m in selected}, indent=2)); return
    if args.profile == 'regenerate' and not args.allow_regeneration:
        parser.error('Regeneration requires --allow-regeneration; it may rebuild exhaustive classifications.')
    out = args.output.resolve()
    if out.is_relative_to(ROOT / 'research') or out.is_relative_to(ROOT / 'provenance'):
        parser.error('Output may not overwrite archival source/provenance.')
    if (out / 'summary.json').exists():
        parser.error('This output already contains a run; select a fresh output directory.')
    out.mkdir(parents=True, exist_ok=True)
    summary = {'profile': args.profile, 'started_utc': stamp(), 'environment': environment(),
               'scope': 'Execution of the listed retained programs only; not an independent mathematical referee review.',
               'records': [], 'status': 'running'}
    env = os.environ.copy()
    for key in ['PYTHONOPTIMIZE', 'BB_EXECUTABLE', 'BB_ORDER']:
        env.pop(key, None)
    env['PYTHONDONTWRITEBYTECODE'] = '1'
    ok = True
    for mid in selected:
        work = materialize(mid, out / 'work')
        logs = out / 'logs' / mid
        logs.mkdir(parents=True, exist_ok=True)
        for i, template in enumerate(table[mid], 1):
            cmd = [sys.executable if x == '{python}' else x for x in template]
            start = time.monotonic()
            log = logs / f'{i:02d}_{Path(template[1] if template[0] == "{python}" else template[0]).stem}.log'
            rec = {'module': mid, 'command': template, 'started_utc': stamp(),
                   'stdout_stderr': str(log.relative_to(out)), 'status': 'running'}
            print(f'[{mid}] {" ".join(template)}', flush=True)
            proc = None
            try:
                with log.open('w', encoding='utf-8') as stream:
                    stream.write('Command: ' + ' '.join(template) + '\n\n'); stream.flush()
                    proc = subprocess.Popen(cmd, cwd=work, env=env, stdout=stream, stderr=subprocess.STDOUT,
                                            start_new_session=(os.name == 'posix'))
                    try:
                        code = proc.wait(timeout=args.timeout or None)
                        rec.update(returncode=code, status='passed' if code == 0 else 'failed')
                    except subprocess.TimeoutExpired:
                        if os.name == 'posix':
                            os.killpg(proc.pid, signal.SIGKILL)
                        else:
                            proc.kill()
                        proc.wait()
                        rec.update(returncode=proc.returncode, status='incomplete_timeout')
                        stream.write('\nTIMEOUT: this check is incomplete; no mathematical exclusion follows.\n')
            except (OSError, ValueError) as exc:
                rec.update(status='could_not_run', error=str(exc))
                log.write_text(str(exc) + '\n')
            rec['elapsed_seconds'] = round(time.monotonic() - start, 6)
            summary['records'].append(rec)
            ok &= rec['status'] == 'passed'
            (out / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
            print(f'  {rec["status"]} ({rec["elapsed_seconds"]:.3f}s)', flush=True)
            if rec['status'] != 'passed':
                # Continue other independent modules, not dependent commands in this one.
                break
    summary.update(status='passed' if ok else 'not_all_checks_passed', completed_utc=stamp())
    (out / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(json.dumps({'status': summary['status'], 'commands': len(summary['records']),
                      'summary': str(out / 'summary.json')}, indent=2))
    if not ok:
        raise SystemExit(1)

if __name__ == '__main__':
    main()
