#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
CXX="${CXX:-g++}"
"$CXX" -O3 -std=c++17 graphs_eight.cpp -o graphs_eight
./graphs_eight 8 | tee graph_generation.log
python3 colorings.py
for name in classify_eight scan_low_free pure_eight; do
  "$CXX" -O3 -std=c++17 "$name.cpp" -o "$name"
done
./classify_eight . > classify_run.log 2> classify_progress.log
./scan_low_free . > low_free_run.log 2> low_free_progress.log
./pure_eight . > pure_run.log 2> pure_progress.log
python3 verify_graphs.py
python3 verify_highrank.py
python3 verify_low_and_pure.py
python3 verify_nilpotent_lemmas.py
python3 verify_summary.py
