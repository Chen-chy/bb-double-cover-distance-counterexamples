"""Read-only access to the archive's source inventory (standard library only)."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / 'provenance' / 'source_inventory.json'

def inventory() -> dict:
    return json.loads(INVENTORY.read_text(encoding='utf-8'))

def modules() -> dict[str, dict]:
    return {m['id']: m for m in inventory()['modules']}

def safe_path(root: Path, relative: str) -> Path:
    p = Path(relative)
    if p.is_absolute() or '..' in p.parts:
        raise ValueError(f'Unsafe inventory path: {relative!r}')
    result = (root / p).resolve()
    if not result.is_relative_to(root.resolve()):
        raise ValueError(f'Path escapes archive: {relative!r}')
    return result

def verified_bytes(record: dict) -> bytes:
    p = safe_path(ROOT, record['stored_path'])
    data = p.read_bytes()
    if len(data) != record['size'] or hashlib.sha256(data).hexdigest() != record['sha256']:
        raise ValueError(f'Archived source integrity failure: {record["stored_path"]}')
    return data
