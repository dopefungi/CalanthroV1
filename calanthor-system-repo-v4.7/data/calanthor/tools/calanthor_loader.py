"""
Utility loaders for Calanthor datasets.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Iterable, Set

ROOT = Path(__file__).resolve().parents[3]
DEFAULT_UNIFIED = ROOT / "data" / "calanthor" / "data" / "unified" / "calanthor_unified_v2.json"
DEFAULT_ATLAS = ROOT / "data" / "calanthor" / "data" / "atlas" / "calanthor_atlas_latest.json"


def _load_json(path: str | Path) -> Dict[str, Any]:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {p}")
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_unified(path: str | Path | None = None) -> Dict[str, Any]:
    """Load the unified Calanthor dataset.

    Args:
        path: Optional explicit path. Defaults to the canonical repository location.
    """
    return _load_json(path or DEFAULT_UNIFIED)


def load_atlas(path: str | Path | None = None) -> Dict[str, Any]:
    """Load the atlas dataset (regions, ecoregions, overlays)."""
    return _load_json(path or DEFAULT_ATLAS)


def collect_ids(entries: Iterable[dict]) -> Set[str]:
    """Collect ids from a list of atlas entries, ignoring malformed rows."""
    ids: Set[str] = set()
    for entry in entries:
        if isinstance(entry, dict) and "id" in entry:
            ids.add(str(entry["id"]))
    return ids
