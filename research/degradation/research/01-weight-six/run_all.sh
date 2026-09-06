#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 graphs.py
python3 pure_six.py
"${CXX:-g++}" -O3 -std=c++17 classify_six.cpp -o classify_six
./classify_six . > mixed_run.log 2> mixed_progress.log
python3 verify_presentations.py
python3 verify_family.py 1 2
python3 - <<'PY'
import hashlib
from pathlib import Path
p=Path('mixed_presentations.tsv')
digest=hashlib.sha256(p.read_bytes()).hexdigest()
assert digest=='5d628c388525ffa3c78be0583cccdde43249e5d704fd425e72dc054d8692139f',digest
print('Complete catalogue hash verified:',digest)
PY
