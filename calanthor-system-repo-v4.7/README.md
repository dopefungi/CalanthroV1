# Calanthor System (D&D-dominant, DC-based Procedures)

A rules-and-content **kernel + pack library** for running the Calanthor realm with:
- **D&D-style combat** as the dominant layer (AC/HP/actions/saves/spells remain your D&D baseline)
- **Structured exploration/social/ritual checks** as **Procedure Checks**:
  - still just normal D&D rolls (d20 + mods)
  - with **DC guidance** and **defined outcomes**
  - optional **margin rules** (success by 5 / fail by 5)

This repo supports **monster/encounter generation** via:
- region identity (hazards, motifs, complications)
- domain overlays (one per Great Pet) with tracks (0–6)
- eco-region hooks (encounter bias, hazard lists, monster graft traits)

## Files

### `data/calanthor/data/unified/calanthor_unified_v2.json` (ACTIVE)
Single authoritative system file containing:
- Rules Kernel v2 (DC-based procedures + flight progression + Aerial Strain)
- Region Packs (Shakora, Verdant, Emberwood, Skyward Peaks, Cracked Earth, Frozen Tundra)
- EcoRegion Packs (Gloomwood, Sable Mire)
- Domain Overlays (one per Great Pet)
- Manifest (authoritative IDs)

### `data/calanthor/data/atlas/calanthor_atlas_latest.json`
Derived atlas data (regions, eco-regions, overlays) extracted from the unified packs.

### `data/deprecated/calanthor_unified_v1.json`
Prior version that used Move tiers (15+/10–14/≤9). Kept for history only.

## Procedure Checks (how to use)
A Procedure Check is a named, repeatable check for travel/rites/negotiation/hazards.

**Roll:** d20 + ability mod + proficiency (if a fitting skill/tool applies)  
**DC:** use 10/15/20/25 depending on conditions.

Optional margin:
- **Success by 5+**: extra benefit
- **Fail by 5+**: harsher consequence

## Data validation
To confirm the atlas/unified datasets are coherent, run:

```
python3 data/calanthor/tools/calanthor_validate.py \
  --unified data/calanthor/data/unified/calanthor_unified_v2.json \
  --atlas data/calanthor/data/atlas/calanthor_atlas_latest.json
```

## Flight balancing
Kernel v2 includes an **Aerial Mastery** ladder (Jump→Glide→Burst→Sustained→Tactical→Mastery) and an **Aerial Strain** track to keep flight cinematic but fair at low levels.

## License
MIT (see `LICENSE`).


## Docs
- `docs/Calanthor_DnD_Baseline_v1.0.md`
- `docs/Calanthor_Procedure_Check_Usage_Rules_v1.0.md`
- `docs/Calanthor_Flight_Official_Options_v1.0.md`


## Docs (extended)
- `docs/Calanthor_Tagging_Spec_v1.0.md`
- `docs/Calanthor_Conditions_Appendix_v1.0.md`

- `docs/Calanthor_Domain_Overlay_Operating_Rules_v1.0.md`

- `docs/Calanthor_Species_and_Culture_Framework_v1.0.md`

- `docs/Calanthor_Official_Lineages_and_Backgrounds_v1.0.md`

- `docs/Calanthor_Spell_and_Class_Policy_v1.0.md`

- `docs/Calanthor_Class_Edge_Catalog_v1.0.md`

- `docs/Calanthor_Technique_Library_v1.0.md`

- `docs/Calanthor_Elemental_Discipline_Feats_v1.0.md`

- `docs/Calanthor_Monster_Generation_RoleFirst_v1.0.md`

- `docs/Calanthor_Feat_Compendium_v1.0.md`

- `docs/Calanthor_Spirit_Alignment_Rules_v1.0.md`

- `docs/Calanthor_Species_Reskin_List_v1.0.md`

- `docs/Calanthor_Monster_Role_Chassis_Tables_v1.0.md`

- `docs/Calanthor_Monster_Graft_Libraries_v1.0.md`

- `docs/Calanthor_Monster_Counterplay_Templates_v1.0.md`

- `docs/Calanthor_DM_OnTheSpot_Monster_Builder_v1.0.md`

- `docs/Calanthor_Starter_Bestiary_v1.0.md`

- `docs/Calanthor_Weapons_and_Implements_v1.0.md`

- `docs/Calanthor_Equipment_Tiers_Crafting_Loadouts_v1.0.md`

- `docs/Calanthor_Core20_Arms_List_v1.0.md`

- `docs/Calanthor_Background_Starting_Gear_Matrix_v1.0.md`

- `docs/Calanthor_Social_Interaction_Framework_v1.0.md`

- `docs/Calanthor_Exploration_Travel_Procedure_v1.0.md`

- `docs/Calanthor_Quick_Start_Guide_v1.0.md`

- `docs/Calanthor_First_Adventure_The_Frostcrack_Witness_v1.0.md`

- `docs/Calanthor_Condition_Appendix_v1.0.md`

- `docs/Calanthor_Master_GM_Reference_Sheet_v1.0.pdf`

- `docs/Calanthor_Master_GM_Reference_Sheet_v1.0.md`

- `docs/Calanthor_Cartographer_Commission_Brief_v1.0.md`
