#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python verify_twists.py
python verify_geometry.py
python verify_odd_sector.py
