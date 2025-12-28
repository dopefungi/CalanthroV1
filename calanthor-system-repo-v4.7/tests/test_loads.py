from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from calanthor_system import load_unified

def test_unified_loads():
    u = load_unified()
    assert u["kernel"]["id"].endswith("v2")
    assert "procedure_checks" in u["packs"]["regions"][0]
