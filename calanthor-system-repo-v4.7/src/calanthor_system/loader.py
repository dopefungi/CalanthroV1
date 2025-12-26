import json
from pathlib import Path
from typing import Any, Dict

def load_unified(path: str | Path) -> Dict[str, Any]:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Unified file not found: {p}")
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)
