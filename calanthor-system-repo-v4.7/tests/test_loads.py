from pathlib import Path
from calanthor_system import load_unified

def test_unified_loads():
    root = Path(__file__).resolve().parents[1]
    u = load_unified(root / "data" / "calanthor_unified_v4.7.1_no_pressure.json")
    assert u["kernel"]["id"].endswith("v4.7.1_no_pressure")
    assert "procedure_checks" in u["packs"]["regions"][0]
