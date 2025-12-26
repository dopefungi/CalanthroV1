# Calanthor Spirit Alignment Rules (v1.0)
*Light- and Dark-alignment by Great Pet dominion, with “born under the Pet” logic.*

This module adds a setting-consistent “spirit alignment” layer that is:
- **lore-forward** (who you were born under matters)
- **mechanically light** (tags + social pressure + small, optional boons)
- **generator-ready**

Spirit alignment is **not** D&D alignment (LG/CE). It is **attunement** to Calanthor’s Great Pets.

---

## 1) Core rule: Born Under the Pet (official)
A character’s Spirit Alignment is determined by **the Great Pet dominion where they were born**.

- Born in a **Light Pet** region → **Light-aligned**
- Born in a **Dark Pet** region → **Dark-aligned**
- Born outside known dominions (rare) → GM chooses, or start **Unmarked** until the first Rite of Naming

> This applies to **any species**. If an elf is born in a Dark Pet region, that elf is **Dark-aligned**.
> Culture/background can differ; alignment is about *spirit imprint*, not upbringing.

---

## 2) The Great Pets: Light vs Dark (v1.0 canon mapping)
This mapping is a **playability default**. You can flip a Pet later if your lore evolves.

### Light Pets
- **Gaianok** (Verdant Valley) — mutualism, stewardship, life-as-duty
- **Shakora** (Waters) — treaty, flow, cleansing, mediation
- **Keairvari** (Skyward Peaks) — omen-wind, passage, watch, clarity
- **Nyvakira** (Emberwood) — renewal, forge, heat-as-life, courage

### Dark Pets
- **Varook** (Gloomwood) — hush, fear, memory pressure, name-taboo
- **Charnelix** (Sable Mire) — blight, disease, contamination, devouring ecology
- **Kaldraun** (Frozen Tundra) — stasis, whiteout, isolation, cold judgment
- **Khalsarra** (Cracked Earth) — sacred weight, grief law, despair trials, oath-burden

**Design note:** “Dark” does not mean evil. It means the dominion presses with harsh truths.

---

## 3) What Spirit Alignment does (balanced)
Spirit alignment provides **tags and story pressure** first, plus optional light mechanics.

### Always-on effects (mandatory, non-numeric)
- You gain one tag: **SPIRIT_LIGHT** or **SPIRIT_DARK**
- Certain rites, relics, and spirits may react differently (advantage/disadvantage is GM-facing, not automatic)

### Optional minor mechanical handle (recommended)
Once per **long rest**, when a Procedure Check consequence would apply, you may invoke your alignment to **change the consequence type** (not negate it):

- **Light Invocation:** convert a harsh consequence into a **resource cost** or **time cost** (your aid comes with duty)
- **Dark Invocation:** convert a consequence into a **complication** that reveals truth (omen/mark/attention) instead of pure loss

This is designed to keep the game fun on bad rolls without giving flat bonuses.

---

## 4) Changing alignment (rare; Rite of Rebinding)
Spirit alignment can change only through major story events:
- surviving a Cataclysm
- Great Pet bargain
- Rite of Rebinding performed at a sacred site

### Rite of Rebinding (framework)
- 1-hour rite (or longer)
- requires Ritecraft + a vow/payment (GM defines)
- on success: alignment shifts; you gain a visible mark
- on failure: success-with-cost (you shift, but owe duty / attract attention)

**Rule:** no casual “swap for the buffs.” Rebinding is a campaign event.

---

## 5) Marking species and subspecies with alignment
When presenting a species/subspecies in Calanthor materials:
- list the **common** birth dominions (likely alignment)
- but always include: **“Born Under the Pet overrides this.”**

Example formatting:
- **Monolith-Forged Dwarves (typical):** Dark-aligned (Khalsarra), but Born Under the Pet overrides.
- **Grove-Warden Elves (typical):** Light-aligned (Gaianok), but Born Under the Pet overrides.

This keeps the list readable while preserving your rule.

---

## 6) Generator fields (minimum)
Characters:
- `spirit_alignment`: LIGHT | DARK | UNMARKED
- `birth_dominion`: great_pet_id (e.g., gaianok, varook)
- `spirit_tags`: ["SPIRIT_LIGHT"] or ["SPIRIT_DARK"]

Regions/Pets:
- `great_pet.alignment`: LIGHT | DARK
- `region.primary_great_pet`: great_pet_id

