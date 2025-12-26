from pathlib import Path
from calanthor_system import load_unified

def test_unified_loads():
    root = Path(__file__).resolve().parents[1]
    u = load_unified(root / "data" / "calanthor_unified_v2.json")
    assert u["kernel"]["id"].endswith("v2")
    assert "procedure_checks" in u["packs"]["regions"][0]
