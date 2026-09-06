#!/usr/bin/env python3
"""Preview, or explicitly execute, creation of a NEW GitHub repository using local gh.

No credentials are read by this script. Authorization remains with the user's
GitHub CLI. Existing repositories/remotes are never overwritten or force-pushed.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', required=True, help='New NAME or OWNER/NAME')
    visibility = parser.add_mutually_exclusive_group(required=True)
    visibility.add_argument('--public', action='store_true')
    visibility.add_argument('--private', action='store_true')
    parser.add_argument('--execute', action='store_true', help='Actually create the remote and push')
    args = parser.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]*(?:/[A-Za-z0-9][A-Za-z0-9_.-]*)?', args.repo):
        parser.error('Use a repository NAME or OWNER/NAME, not a URL or shell expression')
    command = ['gh', 'repo', 'create', args.repo, '--source=.', '--remote=github',
               '--public' if args.public else '--private', '--push']
    if not args.execute:
        print(json.dumps({'mode': 'preview_only', 'working_directory': str(ROOT),
                          'command': shlex.join(command), 'remote_created': False,
                          'required_checks': ['complete-repository integrity', 'clean Git commit',
                                              'authorized gh', 'new destination', 'unused github remote'],
                          'optional_tag_command': 'git push github v0.2.0'}, indent=2))
        return 0
    for executable in ('git', 'gh'):
        if not shutil.which(executable): parser.error(f'Required executable is unavailable: {executable}')
    for script in ('check_repository.py', 'check_release.py'):
        proc = subprocess.run([sys.executable, str(ROOT / 'scripts' / script)], cwd=ROOT)
        if proc.returncode: return proc.returncode
    def run(arguments):
        return subprocess.run(arguments, cwd=ROOT, capture_output=True, text=True)
    commit = run(['git', 'rev-parse', '--verify', 'HEAD'])
    if commit.returncode: parser.error('Create an initial Git commit before publishing')
    state = run(['git', 'status', '--porcelain'])
    if state.returncode or state.stdout.strip(): parser.error('Working tree is not clean; commit intentional changes first')
    remotes = run(['git', 'remote'])
    if remotes.returncode or 'github' in remotes.stdout.splitlines(): parser.error('The github remote is already present; refusing to overwrite it')
    auth = run(['gh', 'auth', 'status'])
    if auth.returncode: parser.error('GitHub CLI is not authorized; run gh auth login in your own environment')
    probe = run(['gh', 'repo', 'view', args.repo, '--json', 'nameWithOwner'])
    if probe.returncode == 0: parser.error('Destination repository exists; refusing to overwrite it')
    # A failed existence probe might be a network/authorization error. The create
    # operation below will fail safely rather than switching to an update/push.
    proc = subprocess.run(command, cwd=ROOT)
    if proc.returncode: return proc.returncode
    remote = run(['git', 'remote', 'get-url', 'github'])
    if remote.returncode: parser.error('Creation returned success but no github remote could be read; inspect gh output')
    print(json.dumps({'status': 'created_and_pushed', 'remote': remote.stdout.strip(),
                      'commit': commit.stdout.strip(), 'optional_tag_command': 'git push github v0.2.0'}, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
