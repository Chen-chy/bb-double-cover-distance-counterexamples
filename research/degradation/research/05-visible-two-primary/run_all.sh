#!/bin/sh
set -eu
cd "$(dirname "$0")"
python3 verify_contact.py
python3 verify_local.py
python3 verify_structured.py
python3 verify_family.py
python3 make_summary.py
