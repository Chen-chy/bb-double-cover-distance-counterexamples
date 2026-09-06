#!/bin/sh
set -eu
cd "$(dirname "$0")"
python3 verify.py > verification_run.txt
python3 audit.py >> verification_run.txt
