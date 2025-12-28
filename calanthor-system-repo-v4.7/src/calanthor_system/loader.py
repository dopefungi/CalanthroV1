import json
from pathlib import Path
from typing import Any, Dict

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_UNIFIED = ROOT / "data" / "calanthor" / "data" / "unified" / "calanthor_unified_v2.json"
DEFAULT_ATLAS = ROOT / "data" / "calanthor" / "data" / "atlas" / "calanthor_atlas_latest.json"


def _load_json(path: str | Path) -> Dict[str, Any]:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {p}")
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_unified(path: str | Path = DEFAULT_UNIFIED) -> Dict[str, Any]:
    """Load the unified system data (canonical default path)."""
    return _load_json(path)


def load_atlas(path: str | Path = DEFAULT_ATLAS) -> Dict[str, Any]:
    """Load the atlas data (regions/ecoregions/overlays)."""
    return _load_json(path)
