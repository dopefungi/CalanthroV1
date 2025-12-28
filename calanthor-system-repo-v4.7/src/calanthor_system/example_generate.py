from calanthor_system import load_unified

def main():
    # Uses canonical data location under data/calanthor/data/unified
    u = load_unified()

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
