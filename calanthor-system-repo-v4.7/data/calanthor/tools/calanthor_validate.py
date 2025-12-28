"""Validate Calanthor atlas/unified coherence."""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict, List

from calanthor_loader import collect_ids, load_atlas, load_unified


def validate(unified_path: Path, atlas_path: Path) -> List[str]:
    unified = load_unified(unified_path)
    atlas = load_atlas(atlas_path)

    errors: List[str] = []

    if not isinstance(unified, dict):
        errors.append("Unified data must be a JSON object.")
        return errors
    if "manifest" not in unified:
        errors.append("Unified manifest is missing.")
    if "packs" not in unified:
        errors.append("Unified packs section is missing.")

    if not isinstance(atlas, dict):
        errors.append("Atlas data must be a JSON object.")
        return errors

    for block in ("regions", "ecoregions", "overlays"):
        if block not in atlas:
            errors.append(f"Atlas missing '{block}' block.")
        elif not isinstance(atlas[block], list):
            errors.append(f"Atlas block '{block}' must be a list.")

    manifest = unified.get("manifest", {}) if isinstance(unified, dict) else {}
    active = manifest.get("active_packs", {}) if isinstance(manifest, dict) else {}

    for block, expected in active.items():
        atlas_entries = atlas.get(block, []) if isinstance(atlas, dict) else []
        atlas_ids = collect_ids(atlas_entries) if isinstance(atlas_entries, list) else set()
        missing = [pid for pid in expected if pid not in atlas_ids]
        if missing:
            errors.append(f"Active {block} missing definitions: {', '.join(missing)}")

    # detect duplicate ids per block
    for block in ("regions", "ecoregions", "overlays"):
        atlas_entries = atlas.get(block, []) if isinstance(atlas, dict) else []
        seen: Dict[str, int] = {}
        for entry in atlas_entries if isinstance(atlas_entries, list) else []:
            if not isinstance(entry, dict):
                continue
            entry_id = str(entry.get("id"))
            if entry_id in seen:
                errors.append(f"Duplicate id in {block}: {entry_id}")
            else:
                seen[entry_id] = 1

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Calanthor atlas/unified datasets")
    parser.add_argument("--unified", type=Path, required=True, help="Path to calanthor_unified JSON")
    parser.add_argument("--atlas", type=Path, required=True, help="Path to calanthor_atlas JSON")
    args = parser.parse_args()

    errors = validate(args.unified, args.atlas)
    if errors:
        for err in errors:
            print(f"[ERROR] {err}")
        return 1

    print("Validation succeeded: unified and atlas datasets are coherent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
