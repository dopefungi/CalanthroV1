from pathlib import Path
from calanthor_system import load_unified

def main():
    root = Path(__file__).resolve().parents[2]
    u = load_unified(root / "data" / "calanthor_unified_v2.json")

    # Show one procedure check example (Frozen Tundra)
    region = next(p for p in u["packs"]["regions"] if p["id"] == "region.frozen_tundra_kaldraun")
    proc = region["procedure_checks"][0]

    print("Region:", region["display_name"])
    print("Procedure:", proc["name"])
    print("Trigger:", proc["trigger"])
    print("Check:", proc["check"])
    print("DC default:", proc["dc"]["default"])
    print("On success:", proc["outcomes"]["success_at_dc"])
    print("On success by 5:", proc["outcomes"]["success_by_5"])
    print("On failure:", proc["outcomes"]["failure"])

if __name__ == "__main__":
    main()
