#!/bin/sh
set -eu
cd "$(dirname "$0")"
python3 verify.py | tee run_output.txt
