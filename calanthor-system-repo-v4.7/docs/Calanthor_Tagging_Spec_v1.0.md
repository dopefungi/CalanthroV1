# Calanthor Tagging Spec (v1.0)
*A consistent, generator-friendly way to tag spells, features, hazards, monsters, and regions.*

This spec exists so your content and generators don’t argue about what counts as Fire vs Ice, or what “Blight” means mechanically.

---

## 1) Tag families (what tags exist)
### A) Element Tags (primary)
Use these to describe **energy/affinity** and region resonance:
- **FIRE**
- **AIR**
- **WATER**
- **ICE** (Ice/Winter; distinct from WATER for mechanics)
- **EARTH**
- **VERDANT** (life/growth/biomass; not “nature” as a school)

### B) Domain Pressure Tags (Great Pet overlays)
Use these to describe **mythic pressure** (track systems), not raw element:
- **NYVAKIRA_HEAT** (Heat Debt)
- **KEAIRVARI_GALE** (Altitude Strain)
- **SHAKORA_TIDE** (Tide Owed)
- **GAIANOK_BLOOM** (Covenant Balance)
- **KHALSARRA_WEIGHT** (Sacred Weight / Despair)
- **KALDRAUN_STASIS** (Frost Lock)
- **VAROOK_SILENCE** (Memory Strain)
- **CHARNELIX_BLIGHT** (Blight Track)

### C) Motif Tags (secondary flavor + monster generation)
Motifs describe “how it plays,” often used to pick conditions/grafts:
- **SILENCE**, **MEMORY**, **FEAR**
- **DISEASE**, **SPORES**, **WEB**, **DECAY**
- **STORM**, **ALTITUDE**, **WHITEOUT**
- **DESPAIR**, **VOW**, **ECHO**
- **LAVA**, **ASH**, **OBSIDIAN**
- **MUTUALISM**, **POLLEN**, **VINES**

### D) Mechanical Tags (optional)
Use sparingly. These inform immunities/resistances and generator heuristics:
- **POISON**, **COLD**, **FIRE_DAMAGE**, **NECROTIC**, **PSYCHIC**, **FORCED_MOVEMENT**, **REST_DENIAL**

---

## 2) Core rule: explicit tags win
### Preferred workflow (best for consistency)
- Your content (spells/features/items/monster abilities) should include **explicit tags**.
- Use the fallback mapping only when you must tag legacy 5e content quickly.

**If explicit tags and fallback mapping disagree, explicit tags are authoritative.**

---

## 3) How many tags?
- Most things should have **1 primary element tag**.
- Some can have **2** if truly hybrid (e.g., ICE+WATER, AIR+ICE, EARTH+FIRE magma).
- Domain Pressure tags are added only when relevant (overlay scenes, sacred sites, Great Pet attention).

---

## 4) FIRE vs VERDANT vs “Nature”
- **VERDANT** is *life biomass*: vines, pollen, fungal bloom, rapid regrowth, mutualism, overgrowth.
- “Nature-y” magic that’s really **weather** is usually **AIR** or **WATER**.
- “Nature-y” that’s **stone/metal** is **EARTH**.
- “Nature-y” that’s **plants** is **VERDANT**.

---

## 5) WATER vs ICE (important)
In Calanthor, **ICE is mechanically distinct** from WATER.

- **WATER**: flow, cleansing, healing currents, tides, fog, steam (if not primarily heat).
- **ICE**: stasis, brittleness, winter, preservation, freezing, whiteout, frostbite.

### Rule of thumb
If it **freezes / preserves / locks**, it’s ICE.
If it **moves / cleanses / carries**, it’s WATER.

Hybrid example:
- “Ice knife” might be **ICE**.
- “Create or Destroy Water” is **WATER**.
- “Sleet storm” is **ICE + AIR** (winter storm) if you want two tags.

---

## 6) AIR vs “Storm damage types”
- **Thunder** and **Lightning** default to **AIR** (storm).
- If lightning is explicitly “skyfire” or volcanic discharge, it may be **FIRE + AIR** (rare).
- If thunder is subterranean quake-burst, it may be **EARTH** (rare).

---

## 7) Shadow / Silence / Memory: where do they live?
These are primarily **VAROOK_SILENCE** domain motifs, not a core element.

### Tagging rule
- Psychic/fear/illusion effects get motif tags (**MEMORY/FEAR/SILENCE**) and can get the domain tag **VAROOK_SILENCE** only when the fiction is specifically Varook-like (Gloomwood, hush rites, intrusions).

---

## 8) Blight / Disease / Rot: where do they live?
These are primarily **CHARNELIX_BLIGHT** domain motifs, not a core element.

### Tagging rule
- Poison/disease/necrotic effects get motif tags (**DISEASE/DECAY/SPORES/WEB**) and can get **CHARNELIX_BLIGHT** domain tag when the fiction is specifically Charnelix-like (Mire, outbreak cult, intrusion).

---

## 9) Fallback auto-tagging map (for 5e imports)
Use this only when explicit tags are missing.

### A) By damage type
- fire → FIRE
- cold → ICE
- lightning/thunder → AIR
- poison → (motif) DISEASE; optional domain CHARNELIX_BLIGHT if setting-linked
- necrotic → (motif) DECAY; optional domain CHARNELIX_BLIGHT if setting-linked
- psychic → (motif) MEMORY/FEAR; optional domain VAROOK_SILENCE if setting-linked
- bludgeoning/force involving stone → EARTH (GM discretion)

### B) By spell theme
- water manipulation, purification, healing waters → WATER
- freezing, winter, stasis, brittle breath → ICE
- wind, pressure, storm routing, soundwaves → AIR
- plants, pollen, vines, fungal bloom → VERDANT
- stone shaping, metal, gravity-like weight → EARTH

---

## 10) Region resonance usage (small, non-breaking)
When a spell/feature shares the region’s primary element tag, once per scene the caster may gain **one**:
- advantage on the spell attack roll, OR
- +1 spell save DC, OR
- ignore one minor environmental penalty for that spell

This is intentionally modest.

---

## 11) Generator requirements (minimum)
For generator consistency, every generated object should include:
- `tags.primary_element` (one of FIRE/AIR/WATER/ICE/EARTH/VERDANT) OR `None`
- `tags.motifs[]` (0+)
- `tags.domain[]` (0+)
- `source` (region/ecoregion/overlay IDs that contributed tags)

