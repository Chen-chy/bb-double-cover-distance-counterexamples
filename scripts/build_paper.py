#!/usr/bin/env python3
"""Compile the manuscript with ordinary PDFLaTeX, without shell escape."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT/'paper/main.pdf')
    args = parser.parse_args()
    executable = shutil.which('pdflatex')
    if executable is None:
        parser.error('pdflatex is required; use a TeX Live installation with the standard packages in main.tex')
    build = ROOT/'.build/paper'
    build.mkdir(parents=True, exist_ok=True)
    cmd = [executable, '-interaction=nonstopmode', '-halt-on-error', '-file-line-error',
           '-no-shell-escape', '-output-directory', str(build), 'main.tex']
    for run in range(1, 4):
        result = subprocess.run(cmd, cwd=ROOT/'paper', capture_output=True, text=True)
        (build/f'run-{run}.txt').write_text(result.stdout + result.stderr)
        if result.returncode:
            print(result.stdout[-8000:])
            raise SystemExit(f'LaTeX failed; see {build}/run-{run}.txt')
    log = (build/'main.log').read_text(errors='replace')
    fatal = ('There were undefined references', 'Citation `', 'Reference `')
    if any(s in log for s in fatal):
        raise SystemExit('Unresolved references/citations remain; inspect .build/paper/main.log')
    warnings = [line for line in log.splitlines() if 'Overfull' in line or 'Warning:' in line]
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(build/'main.pdf', output)
    print(json.dumps({'pdf': str(output), 'latex_warnings': warnings}, indent=2))


if __name__ == '__main__':
    main()
