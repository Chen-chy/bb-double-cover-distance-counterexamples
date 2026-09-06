#!/usr/bin/env python3
"""Run the four preserved class-metric/family audits in an isolated working copy.

Full-family theorems depend on their written proofs. Finite audits do not certify
all parameter values. Each outcome is recorded; failures/timeouts are not passes.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import signal
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]


def stamp(): return datetime.now(timezone.utc).isoformat()
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'checks/homology-history')
    parser.add_argument('--timeout', type=float, default=300)
    args = parser.parse_args()
    if sys.flags.optimize or os.environ.get('PYTHONOPTIMIZE'):
        parser.error('Do not disable assertions')
    if args.timeout <= 0: parser.error('Timeout must be positive')
    out = args.output.resolve()
    if not (ROOT / 'checks').resolve() in out.parents:
        parser.error('Output must be a new directory under checks/')
    if out.exists(): parser.error('Select a new output directory')
    out.mkdir(parents=True)
    work = out / 'work'
    shutil.copytree(ROOT / 'archive/early_counterexample', work)
    report = {'status': 'running', 'started_utc': stamp(), 'python': sys.version,
              'platform': platform.platform(), 'commands': [],
              'scope': 'Four exact preserved finite/class-metric audits; symbolic infinite-family proofs are separate.'}
    def save(): (out / 'report.json').write_text(json.dumps(report, indent=2) + '\n')
    save()
    env = os.environ.copy()
    env.update(PYTHONDONTWRITEBYTECODE='1', PYTHONUNBUFFERED='1')
    for name in ('verify_previous_family.py', 'verify_auxiliary.py', 'verify_counterexample.py',
                 'independent_bivariate_check.py'):
        logfile = out / (Path(name).stem + '.log')
        record = {'program': 'archive/early_counterexample/' + name,
                  'script_sha256': sha(work / name), 'started_utc': stamp(), 'log': logfile.name}
        start = time.monotonic()
        with logfile.open('w') as log:
            process = subprocess.Popen([sys.executable, name], cwd=work, env=env,
                                       stdout=log, stderr=subprocess.STDOUT, start_new_session=os.name == 'posix')
            try:
                rc = process.wait(timeout=args.timeout)
                record.update(status='passed' if rc == 0 else 'failed', returncode=rc)
            except subprocess.TimeoutExpired:
                if os.name == 'posix': os.killpg(process.pid, signal.SIGKILL)
                else: process.kill()
                process.wait()
                record.update(status='incomplete_timeout', returncode=process.returncode)
                log.write('\nTIMEOUT: incomplete verification, not a mathematical exclusion.\n')
        record.update(seconds=round(time.monotonic()-start, 6), log_sha256=sha(logfile))
        report['commands'].append(record)
        save()
        print(name + ': ' + record['status'], flush=True)
    report.update(status='passed' if all(x['status'] == 'passed' for x in report['commands']) else 'not_all_checks_passed',
                  completed_utc=stamp())
    save()
    return report['status'] != 'passed'


if __name__ == '__main__':
    raise SystemExit(main())
