# Calanthor Technique Library (v1.0)
*Elemental “bending complexity” as non-spell abilities — balanced, D&D-native, generator-ready.*

This library implements **Model C** from the Spell & Class Policy:
- **Spells remain standard 5e**
- **Techniques** add elemental identity for *casters and martials*
- Techniques focus on **positioning, defense, mobility, utility, and modest control**
- Techniques avoid becoming “free spells” or replacing class features

**Disciplines (the full elemental set):**
- FIRE / AIR / WATER / ICE / EARTH / VERDANT

---

## 1) Universal Technique rules (official)
### 1.1 What a technique is
A Technique is a defined **action / bonus action / reaction** (or 1-minute rite) with:
- an element tag
- a usage frequency
- D&D-native mechanics (attack roll, save DC, or skill check)

### 1.2 Usage frequencies (standard)
Techniques use one of these recharge patterns:
- **PB/Long Rest**
- **1/Short Rest**
- **1/Scene** (only for small utility effects; GM may treat scene as “one obstacle”)

### 1.3 Save DC and attack bonuses
If a technique requires a save or attack roll:
- **Technique Save DC = 8 + PB + relevant ability mod**
- **Technique Attack = PB + relevant ability mod**

Default abilities by discipline (recommended):
- FIRE: CHA or CON (choose on learning)
- AIR: DEX or WIS
- WATER: WIS or CHA
- ICE: CON or WIS
- EARTH: STR or CON
- VERDANT: WIS

### 1.4 Concentration and stacking
Techniques are intentionally light:
- They do **not** require concentration unless explicitly stated.
- A creature can be affected by **one “stance” technique** at a time (marked as *STANCE*).

### 1.5 Non-caster fairness
Techniques are designed so martials get cool options without needing spell slots.
Casters still have the strongest “big magic” via spells.

---

## 2) How characters learn disciplines
Choose one (campaign setting choice):
- **Feat-based** (recommended): Elemental Discipline Initiate → Adept → Master
- **Background seeds (light):** some culture backgrounds can grant a novice technique (optional)
- **Subclass modules:** if you later want deep bending subclasses

### Feat ladder (recommended)
**FEAT: Elemental Discipline Initiate** (prereq: none)  
- Choose one discipline; learn **2 Novice techniques** from it.
- Gain one Technique Focus ability (choose the discipline’s default).

**FEAT: Elemental Discipline Adept** (prereq: level 5+, Initiate)  
- Learn **2 more techniques** (Novice or Adept).

**FEAT: Elemental Discipline Master** (prereq: level 11+, Adept)  
- Learn **2 more techniques** (Adept or Master).

> Note: This is the same “logical place” approach as flight: earned depth, controlled power.

---

## 3) Discipline: FIRE
**Theme:** heat control, fear pressure, flare bursts, forging protection.  
**Balance:** modest damage, strong *zone shaping* and *tempo control*.

### Novice Techniques
**F1 — Ember Flick (Reaction)** *(1/Scene)*  
Trigger: You or an ally within 10 ft is hit by a melee attack.  
Effect: Reduce the damage by **PB** (minimum 1). Attacker takes **PB** fire damage.  
Tags: FIRE.

**F2 — Searing Step (Bonus Action)** *(PB/Long Rest)*  
Effect: Your speed increases by **10 ft** until end of turn and you ignore difficult terrain caused by ash/smoke/fire.  
If you move past a creature, it must succeed a **DEX save** or take **1d4** fire damage (no damage on success).  
Tags: FIRE.

**F3 — Forge Breath (Action)** *(PB/Long Rest)*  
Effect: Create a 10-ft line of heat. Creatures in line make a **DEX save** or take **1d6** fire damage and can’t take reactions until start of your next turn.  
Tags: FIRE.

### Adept Techniques
**F4 — Heat Ward (Action)** *(1/Short Rest)* *(STANCE)*  
Effect: For 1 minute, you gain resistance to fire damage, and allies within 5 ft ignore environmental heat penalties.  
Tags: FIRE.

**F5 — Flashflare (Action)** *(PB/Long Rest)*  
Effect: 15-ft cone. Creatures make a **CON save** or are **blinded** until end of your next turn. On success, they’re not blinded but have disadvantage on their next attack this round.  
Tags: FIRE.

### Master Techniques
**F6 — Cinder Snare (Action)** *(PB/Long Rest)*  
Effect: Target within 60 ft makes a **STR save** or is **restrained** by ash-coals until end of your next turn. While restrained, it takes **1d6** fire damage at start of its turn.  
Tags: FIRE.

**F7 — Furnace Exchange (Reaction)** *(1/Short Rest)*  
Trigger: A creature within 30 ft deals fire damage or triggers a FIRE-tagged effect.  
Effect: You redirect part of it: one creature of your choice within 30 ft gains resistance to that instance; another creature takes **PB** fire damage (no save).  
Tags: FIRE.

**F8 — Renewal Rite (1 minute)** *(1/Long Rest)*  
Effect: End **Chilled** or **Minor Strain** on up to PB creatures, and each gains temporary HP equal to PB + your focus ability mod.  
Tags: FIRE.

---

## 4) Discipline: AIR
**Theme:** gust control, repositioning, deflection, storm-reading.  
**Balance:** mobility and defense, minimal raw damage.

### Novice Techniques
**A1 — Featherfall Kick (Reaction)** *(1/Scene)*  
Trigger: You fall or an ally within 30 ft falls.  
Effect: Reduce fall damage by **PB × 5** and allow 10 ft of horizontal drift.  
Tags: AIR.

**A2 — Gust Shove (Action)** *(PB/Long Rest)*  
Effect: One creature within 30 ft makes a **STR save** or is pushed **10 ft** and can’t take reactions until start of your next turn.  
Tags: AIR, FORCED_MOVEMENT.

**A3 — Wind Screen (Bonus Action)** *(PB/Long Rest)*  
Effect: Until start of your next turn, ranged weapon attacks against you have disadvantage.  
Tags: AIR.

### Adept Techniques
**A4 — Updraft Vault (Bonus Action)** *(1/Short Rest)*  
Effect: You leap up to **20 ft** vertically (or 10 ft if encumbered) and do not provoke opportunity attacks during this movement.  
Tags: AIR.

**A5 — Storm Sense (Action)** *(1/Scene)*  
Effect: Add +PB to a Perception/Survival/Procedure Check to predict wind shifts, incoming storm pressure, or safe ridge timing.  
Tags: AIR, STORM.

### Master Techniques
**A6 — Cyclone Parry (Reaction)** *(PB/Long Rest)*  
Trigger: You are targeted by a ranged attack or spell attack.  
Effect: Roll a d20 + PB + focus ability mod; if you meet or exceed the attack roll, the attack misses.  
Tags: AIR.

**A7 — Split the Formation (Action)** *(1/Short Rest)*  
Effect: 20-ft-long, 5-ft-wide “wind lane.” Creatures in lane make a **DEX save** or are pushed to either side (your choice) and knocked prone.  
Tags: AIR, FORCED_MOVEMENT.

**A8 — Thin-Air Denial (Action)** *(PB/Long Rest)*  
Effect: One creature within 60 ft makes a **CON save** or is **silenced** until end of your next turn (cannot cast verbal spells).  
Tags: AIR, SILENCE (motif).

---

## 5) Discipline: WATER
**Theme:** flow, cleansing, binding currents, recovery.  
**Balance:** support and control, not replacing healing spells.

### Novice Techniques
**W1 — Cleansing Splash (Action)** *(PB/Long Rest)*  
Effect: End one of the following on a creature within 30 ft: **poisoned** (if nonmagical), **Minor Strain**, or one “grime/contamination” hazard effect (GM).  
Tags: WATER, PURIFICATION.

**W2 — Current Step (Bonus Action)** *(PB/Long Rest)*  
Effect: You move up to **10 ft** without provoking opportunity attacks (you “flow” around threats).  
Tags: WATER.

**W3 — Binding Undertow (Action)** *(PB/Long Rest)*  
Effect: Target within 30 ft makes a **STR save** or its speed is reduced by **10 ft** until end of your next turn.  
Tags: WATER.

### Adept Techniques
**W4 — Mist Veil (Action)** *(1/Short Rest)*  
Effect: Create a 10-ft-radius mist for 1 minute. Area is lightly obscured; allies inside have advantage on Stealth checks.  
Tags: WATER.

**W5 — Tideguard (Reaction)** *(1/Scene)*  
Trigger: An ally within 30 ft takes damage.  
Effect: Reduce damage by **PB** and allow the ally to move 5 ft (no OA).  
Tags: WATER.

### Master Techniques
**W6 — Purification Circle (1 minute)** *(1/Long Rest)*  
Effect: In a 10-ft circle, end **Blighted** on up to PB creatures (they still must succeed a DC 15 CON save if the source is severe); also restore 1 expended Hit Die each (max 1).  
Tags: WATER, PURIFICATION.

**W7 — Riptide Pull (Action)** *(PB/Long Rest)*  
Effect: Creature within 30 ft makes a **STR save** or is pulled 10 ft and knocked prone.  
Tags: WATER, FORCED_MOVEMENT.

**W8 — Borrowed Breath (Reaction)** *(1/Short Rest)*  
Trigger: A creature within 30 ft fails a CON save.  
Effect: That creature rerolls the save and takes the new result. If it still fails, you gain **Minor Strain**.  
Tags: WATER.

---

## 6) Discipline: ICE
**Theme:** stasis, winter control, brittle breath, slow and lock.  
**Balance:** strong tempo control with clear counters (heat, shelter, movement).

### Novice Techniques
**I1 — Frost Numb (Action)** *(PB/Long Rest)*  
Effect: Target within 30 ft makes a **CON save** or has disadvantage on its next weapon attack before end of its next turn.  
Tags: ICE.

**I2 — Whiteout Glimmer (Bonus Action)** *(1/Scene)*  
Effect: Add +PB to a Stealth/Survival/Procedure Check in snow, fog, or low-visibility winter terrain.  
Tags: ICE, WHITEOUT.

**I3 — Ice Grip (Reaction)** *(PB/Long Rest)*  
Trigger: A creature within 10 ft moves willingly.  
Effect: Reduce its speed by **10 ft** until end of its turn (no save).  
Tags: ICE.

### Adept Techniques
**I4 — Rime Shell (Action)** *(1/Short Rest)* *(STANCE)*  
Effect: For 1 minute, you gain temp HP equal to **PB + focus ability mod** at the start of each of your turns (does not stack; refreshes).  
Tags: ICE.

**I5 — Freeze the Ground (Action)** *(PB/Long Rest)*  
Effect: 10-ft square becomes icy until end of your next turn. Creatures entering must succeed a **DEX save** or fall prone.  
Tags: ICE.

### Master Techniques
**I6 — Stasis Mark (Action)** *(1/Short Rest)*  
Effect: Target within 60 ft makes a **WIS save** or cannot take reactions and its speed is reduced by 10 ft for 1 minute (save ends at end of each of its turns).  
Tags: ICE, KALDRAUN_STASIS (domain synergy optional).

**I7 — Veilstorm Brace (Reaction)** *(1/Scene)*  
Trigger: You would gain Chilled, Minor Strain from cold exposure, or an overlay tick due to winter hazard.  
Effect: Negate that application for yourself (or an ally within 10 ft).  
Tags: ICE.

**I8 — Winter’s Stillness (Action)** *(PB/Long Rest)*  
Effect: 15-ft cone. Creatures make a **CON save** or are **restrained** until end of your next turn. On success, speed is reduced by 10 ft.  
Tags: ICE.

---

## 7) Discipline: EARTH
**Theme:** stability, cover, binds, weight, shock control.  
**Balance:** battlefield shaping and restraint; limited damage.

### Novice Techniques
**E1 — Stone Brace (Reaction)** *(1/Scene)*  
Trigger: You or an ally within 10 ft would be knocked prone or pushed.  
Effect: Prevent the push/knockdown.  
Tags: EARTH.

**E2 — Gravel Skitter (Bonus Action)** *(PB/Long Rest)*  
Effect: Create difficult terrain in a 10-ft square until end of your next turn.  
Tags: EARTH.

**E3 — Weighty Grip (Action)** *(PB/Long Rest)*  
Effect: Target within 30 ft makes a **STR save** or its speed is reduced by 10 ft until end of your next turn.  
Tags: EARTH, KHALSARRA_WEIGHT (motif synergy optional).

### Adept Techniques
**E4 — Earthen Cover (Action)** *(1/Short Rest)*  
Effect: Raise low cover in a 5-ft-by-10-ft line (or a 5-ft cube) lasting 1 minute.  
Tags: EARTH.

**E5 — Seismic Sense (Action)** *(1/Scene)*  
Effect: Add +PB to Perception/Investigation checks to detect movement through ground, hollow spaces, or structural weakness.  
Tags: EARTH.

### Master Techniques
**E6 — Anchor Field (Action)** *(PB/Long Rest)*  
Effect: 15-ft radius “heavy air.” Creatures of your choice treat the area as difficult terrain. Creatures that start their turn in the field must succeed a **STR save** or cannot take the Dash action this turn.  
Tags: EARTH, RESTRAIN (soft).

**E7 — Pillar Lift (Action)** *(1/Short Rest)*  
Effect: Lift a 5-ft pillar under a creature within 60 ft. Creature makes a **DEX save** or is lifted 10 ft and knocked prone.  
Tags: EARTH, FORCED_MOVEMENT.

**E8 — Oathstone Shelter (1 minute)** *(1/Long Rest)*  
Effect: Create a small shelter zone (10-ft radius) that counts as “proper shelter” for rest procedures and reduces one active overlay tick risk once (GM).  
Tags: EARTH, VOW.

---

## 8) Discipline: VERDANT
**Theme:** growth, mutualism, pollen, vines, living barriers, remediation.  
**Balance:** restraint/control and support; does not out-heal clerics.

*(And yes: Druids love this discipline. It’s built with them in mind.)*

### Novice Techniques
**V1 — Vine Tangle (Action)** *(PB/Long Rest)*  
Effect: Target within 30 ft makes a **STR save** or is **restrained** until end of your next turn.  
Tags: VERDANT, VINES.

**V2 — Pollen Screen (Bonus Action)** *(PB/Long Rest)*  
Effect: Until start of your next turn, you have advantage on Stealth checks and creatures have disadvantage on opportunity attacks against you (their senses blur).  
Tags: VERDANT, POLLEN.

**V3 — Field Remedy (Action)** *(1/Scene)*  
Effect: End **Minor Strain** or **Chilled** on a creature you touch, or grant advantage on its next CON save vs poison/disease.  
Tags: VERDANT, REMEDY.

### Adept Techniques
**V4 — Living Rampart (Action)** *(1/Short Rest)*  
Effect: Create a 10-ft line of thick growth that grants half cover for 1 minute.  
Tags: VERDANT.

**V5 — Symbiosis (Reaction)** *(PB/Long Rest)*  
Trigger: An ally within 30 ft is hit.  
Effect: Ally gains temp HP = PB, and the attacker’s speed is reduced by 10 ft until end of its next turn (no save).  
Tags: VERDANT.

### Master Techniques
**V6 — Bloom Purge (Action)** *(1/Short Rest)*  
Effect: 15-ft cone. Creatures make a **CON save** or are **poisoned** until end of your next turn. Creatures already Blighted make the save with disadvantage (GM discretion).  
Tags: VERDANT, SPORES.

**V7 — Rooted Sanctuary (1 minute)** *(1/Long Rest)*  
Effect: Create a 10-ft sanctuary. Allies inside have advantage on saves vs poison/disease and reduce healing penalty from Blighted by PB (min 1) for 1 hour.  
Tags: VERDANT, PURIFICATION.

**V8 — Verdant Recall (Action)** *(PB/Long Rest)*  
Effect: Choose one ally within 30 ft: end **Haunted** and grant advantage on its next concentration check.  
Tags: VERDANT, MEMORY (counterplay).

---

## 9) Druid integration (so they don’t get left out)
Druids interact with techniques in three clean ways:

### 9.1 Default access
- Druids are thematically best with **VERDANT** and **WATER** techniques.
- They may also learn **AIR** (storms) or **ICE** (winter druids) if it fits their circle.

### 9.2 Suggested “Druid bonus” (optional, balanced)
At level 5, a druid who has an Elemental Discipline feat may learn **one additional Novice technique** from VERDANT or WATER (your choice).  
This is a small identity nudge, not a power spike.

### 9.3 Wild Shape note
Techniques do not automatically carry into Wild Shape unless the technique is clearly physical/natural (GM discretion).  
Verdant/Wild techniques often do; arcane-style ones usually don’t.

---

## 10) Generator fields (minimum)
Each technique should store:
- id, name, discipline
- action type (action/bonus/reaction/1-minute)
- frequency (PB/LR, 1/SR, 1/Scene)
- mechanics (save/check/attack) and DC rules
- tags (element + motifs + optional domain tags)
- concise effect text

