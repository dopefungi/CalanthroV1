# Calanthor data layout

Canonical data for the Calanthor system lives under this directory.

## Files
- **Atlas (latest):** `data/calanthor/data/atlas/calanthor_atlas_latest.json`
- **Atlas (versioned):** `data/calanthor/data/atlas/calanthor_atlas_v2.json`
- **Unified source of truth:** `data/calanthor/data/unified/calanthor_unified_v2.json`

The unified file is treated as the source of truth; the atlas JSONs are derived from its `packs` section for convenience in tooling.

## Validation
Run the validator to ensure the atlas and unified files stay in sync:

```bash
python3 data/calanthor/tools/calanthor_validate.py \
  --unified data/calanthor/data/unified/calanthor_unified_v2.json \
  --atlas data/calanthor/data/atlas/calanthor_atlas_latest.json
```

## Tools
Supporting utilities live in `data/calanthor/tools/`:
- `calanthor_loader.py` provides helpers for loading the atlas/unified datasets.
- `calanthor_validate.py` checks for basic coherence between the manifest and atlas entries.

## Docs
Audit and validation notes would be placed in `data/calanthor/docs/` when provided.
