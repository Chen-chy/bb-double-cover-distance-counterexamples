#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 verify.py
python3 verify_independent.py
python3 verify_cyclic_strip.py
python3 make_summary.py
