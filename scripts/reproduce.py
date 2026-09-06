#!/usr/bin/env python3
"""Reproduce the finite counterexamples; optionally run all retained branch audits.

Every output directory is a new run. Failed or timed-out commands are never
reported as successful mathematical exclusions. Source verifiers are unchanged.
"""
from __future__ import annotations
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import signal
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stamp() -> str:
    return datetime.now(timezone.utc).isoformat()


def circuit_supports(path: Path) -> list[tuple[int, ...]]:
    lines = path.read_text().splitlines()
    if lines and lines[0] == "BB_CIRCUITS v1":
        _, count = map(int, lines[1].split())
        lines = lines[2:]
        if len(lines) != count:
            raise RuntimeError(f"Invalid circuit header: {path}")
    result = [tuple(map(int, line.split(','))) for line in lines if line]
    if len(result) != len(set(result)) or any(tuple(sorted(set(s))) != s for s in result):
        raise RuntimeError(f"Noncanonical circuit set: {path}")
    return sorted(result, key=lambda s: (len(s), s))


def cross_check(out: Path) -> dict:
    matrix_checks = []
    circuit_checks = []

    def matrices(a: Path, b: Path) -> None:
        if a.read_bytes() != b.read_bytes():
            raise RuntimeError(f"Matrix mismatch: {a} versus {b}")
        matrix_checks.append({"left": str(a.relative_to(out)), "right": str(b.relative_to(out)),
                              "sha256": sha(a)})

    def circuits(a: Path, b: Path, expected: dict[int, int]) -> None:
        sa, sb = circuit_supports(a), circuit_supports(b)
        counts = dict(sorted(Counter(map(len, sa)).items()))
        if sa != sb or counts != expected:
            raise RuntimeError(f"Circuit mismatch/count failure: {a} versus {b}; {counts}")
        circuit_checks.append({"left": str(a.relative_to(out)), "right": str(b.relative_to(out)),
                               "count": len(sa), "weight_histogram": counts})

    for name in ("L39_HX.txt", "L39_HZ.txt", "L78_HX.txt", "L78_HZ.txt"):
        matrices(out/'upper-bitset'/name, out/'upper-polynomial'/name)
    for name in ("base_HX.txt", "base_HZ.txt", "cover_HX.txt", "cover_HZ.txt"):
        matrices(out/'lower-bitset'/name, out/'lower-polynomial'/name)
    for sector in ("X", "Z"):
        matrices(out/'upper-bitset'/f'L78_H{sector}.txt',
                 out/'lower-bitset'/f'base_H{sector}.txt')
    middle = {6: 78, 10: 468, 12: 195}
    circuits(out/'upper-bitset/circuits.txt', out/'upper-polynomial/circuits.txt', middle)
    circuits(out/'lower-bitset/base_circuits.txt', out/'lower-polynomial/base_circuits.txt', middle)
    circuits(out/'upper-bitset/circuits.txt', out/'lower-bitset/base_circuits.txt', middle)
    circuits(out/'lower-bitset/cover_circuits.txt', out/'lower-polynomial/cover_circuits.txt',
             {6: 156, 10: 936})
    # A third, convenience implementation agrees on physical basis conventions.
    sys.path.insert(0, str(ROOT))
    from bbcover import get_example
    for name, folder, prefix in (("q39", "upper-bitset", "L39"),
                                  ("q78", "upper-bitset", "L78"),
                                  ("q78x2", "lower-bitset", "cover")):
        code, _, _ = get_example(name)
        for s in ("X", "Z"):
            if code.matrix_bytes(s) != (out/folder/f'{prefix}_H{s}.txt').read_bytes():
                raise RuntimeError("The convenience package has a different matrix convention")
    return {"status": "passed", "matrix_comparisons": matrix_checks,
            "circuit_comparisons": circuit_checks, "convenience_matrices_compared": 6,
            "shared_middle_code_identical": True}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profile', choices=('core', 'extended'), default='core')
    parser.add_argument('--output', type=Path, default=ROOT/'checks/local')
    parser.add_argument('--timeout', type=float, default=300,
                        help='Per-core-command and per-archived-command seconds; 0 disables core timeout')
    args = parser.parse_args()
    if sys.flags.optimize or os.environ.get('PYTHONOPTIMIZE'):
        parser.error('Do not use python -O or PYTHONOPTIMIZE; historical auditors use assertions')
    if args.timeout < 0:
        parser.error('Timeout must be nonnegative')
    out = args.output.resolve()
    if out == ROOT or any(out == ROOT/p or (ROOT/p) in out.parents for p in
                          ('archive', 'research', 'results', 'certificates', 'provenance', 'paper', 'bbcover', 'scripts', 'tests')):
        parser.error('Output may not overwrite source or evidence directories')
    if (out/'report.json').exists():
        parser.error('This directory contains an earlier run; select a fresh output directory')
    out.mkdir(parents=True, exist_ok=True)
    report = {'profile': args.profile, 'started_utc': stamp(), 'python': sys.version,
              'platform': platform.platform(), 'commands': [], 'status': 'running',
              'scope': 'exact counterexample regeneration and explicitly listed retained audits'}
    env = os.environ.copy()
    env['PYTHONDONTWRITEBYTECODE'] = '1'
    env['PYTHONUNBUFFERED'] = '1'

    def save():
        (out/'report.json').write_text(json.dumps(report, indent=2)+'\n')

    def run(name, tail, timeout=None):
        command = [sys.executable] + [str(x) for x in tail]
        record = {'name': name, 'command': command, 'started_utc': stamp(),
                  'log': name+'.log', 'script_sha256': None}
        source = ROOT/str(tail[0])
        if source.is_file(): record['script_sha256'] = sha(source)
        start = time.monotonic()
        print(f'[{name}] starting', flush=True)
        try:
            with (out/(name+'.log')).open('w') as log:
                process = subprocess.Popen(command, cwd=ROOT, env=env, stdout=log,
                                           stderr=subprocess.STDOUT, start_new_session=os.name == 'posix')
                try:
                    rc = process.wait(timeout=(args.timeout if timeout is None else timeout) or None)
                    record.update(returncode=rc, status='passed' if rc == 0 else 'failed')
                except subprocess.TimeoutExpired:
                    if os.name == 'posix': os.killpg(process.pid, signal.SIGKILL)
                    else: process.kill()
                    process.wait()
                    record.update(returncode=process.returncode, status='incomplete_timeout')
                    log.write('\nTIMEOUT: incomplete check, not a mathematical exclusion.\n')
        except OSError as exc:
            record.update(returncode=None, status='could_not_run', error=str(exc))
        record['seconds'] = round(time.monotonic()-start, 6)
        logfile = out/(name+'.log')
        record['log_sha256'] = sha(logfile) if logfile.exists() else None
        report['commands'].append(record)
        save()
        print(f'[{name}] {record["status"]} ({record["seconds"]:.3f}s)', flush=True)
        return record['status'] == 'passed'

    save()
    ok = run('unit-tests', ['-m', 'unittest', 'discover', '-s', 'tests', '-v'])
    ok = run('lattice-transport', ['scripts/verify_lattice_transport.py', '--output', out/'lattice.json']) and ok
    programs = [('upper-bitset', 'certificates/upper/verify_bitset.py'),
                ('upper-polynomial', 'certificates/upper/verify_polynomial.py'),
                ('lower-bitset', 'certificates/lower/verify_lower_bitset.py'),
                ('lower-polynomial', 'certificates/lower/verify_lower_polynomial.py')]
    for name, program in programs:
        ok = run(name, [program, '--output-dir', out/name]) and ok
    if ok:
        try:
            comparison = cross_check(out)
            report['cross_checks'] = comparison
            (out/'cross_checks.json').write_text(json.dumps(comparison, indent=2)+'\n')
        except Exception as exc:
            ok = False
            report['cross_checks'] = {'status': 'failed', 'error': repr(exc)}
    else:
        report['cross_checks'] = {'status': 'not_run', 'reason': 'A preceding core command did not pass'}
    save()
    if args.profile == 'extended':
        # Each archived driver applies its own per-command timeout and preserves source bytes.
        per_command = args.timeout or 1800
        outer_timeout = max(1800, 30*per_command)
        for name, script, mode in (
            ('amplification-audit', 'research/amplification/tools/run_checks.py', ['--profile', 'audit']),
            ('degradation-audit', 'research/degradation/scripts/run_checks.py', ['--mode', 'verify'])):
            ok = run(name, [script] + mode + ['--output', out/name, '--timeout', per_command],
                     timeout=outer_timeout) and ok
    report.update(status='passed' if ok else 'not_all_checks_passed', completed_utc=stamp())
    report['output_sha256'] = {str(p.relative_to(out)): sha(p) for p in sorted(out.rglob('*'))
                              if p.is_file() and p.name != 'report.json' and 'work' not in p.parts}
    save()
    print(json.dumps({'status': report['status'], 'report': str(out/'report.json')}, indent=2))
    return 0 if ok else 1


if __name__ == '__main__':
    raise SystemExit(main())
