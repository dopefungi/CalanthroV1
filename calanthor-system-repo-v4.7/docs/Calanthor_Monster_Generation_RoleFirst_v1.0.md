# Calanthor Monster Generation — Role-First System (v1.0)
*D&D-style statblocks, driven by Calanthor tags + domain overlays, with counterplay baked in.*

This is the **Monster Gen v1** spec. It produces monsters that:
- read like 5e statblocks
- feel region-specific (Kaldraun/Khalsarra/Charnelix, etc.)
- interact with overlay tracks (2/4/6)
- always include player counterplay (so pressure is gameplay, not punishment)

---

## 1) Monster Gen v1 output (what every generated monster includes)
### A) Core Statblock (5e compatible)
- Name, size, type, alignment
- AC, HP, Speed
- Ability scores
- Saves, Skills (optional)
- Resistances/Immunities/Vulnerabilities (sparingly)
- Senses, Languages, CR (or CR estimate)
- Traits
- Actions (and bonus/reactions if appropriate)

### B) Calanthor Tag Bundle
- `primary_element`: FIRE/AIR/WATER/ICE/EARTH/VERDANT or None
- `motifs[]`: e.g., WHITEOUT, DESPAIR, SPORES, VOW, SILENCE, MEMORY
- `domain[]`: e.g., KALDRAUN_STASIS, KHALSARRA_WEIGHT, CHARNELIX_BLIGHT
- `region_source[]`: e.g., "frozen_tundra", "cracked_earth", "sable_mire"

### C) Role Package (encounter role drives design)
Each monster has a role that determines its mechanics budget:
- **SCOUT**: mobility, perception, ambush, disengage
- **BRUISER**: HP, melee pressure, simple control
- **CONTROLLER**: zones, conditions, forced movement, debuffs (low damage)
- **SKIRMISHER**: hit-and-run, repositioning, reactions
- **SUPPORT**: buffs, heals, summons, debuff cleanses
- **ELITE**: upgraded version of any role (extra reactions/legendary-ish without full legendary)
- **BOSS**: 2–3-phase fight, overlay-like behaviors, lair actions (optional)

**Role-first rule:** Build the monster’s gameplay loop from its role first; then fit CR.

### D) Overlay Interaction (threshold play)
Every monster tied to a domain overlay includes:
- **Track 2 effect:** light pressure (minor condition, small zone, tell)
- **Track 4 effect:** meaningful pressure (stronger zone, reaction denial, healing penalty)
- **Track 6 event:** dramatic behavior (summon, storm break, bloom surge)

### E) Counterplay Hooks (mandatory)
Every monster must have at least **2 counters**, each from different categories:
- **Resource counter** (antitoxin, shelter kit, fire, rope, salt, etc.)
- **Action/skill counter** (Ritecraft, Survival, Athletics, Persuasion, etc.)
- **Choice counter** (retreat, detour, bargain, vow, destroy an anchor)

Counterplay is explicitly written as “If the PCs do X, then Y happens.”

---

## 2) Tag → mechanics mapping (v1.0 heuristics)
Use these as generator defaults; explicit monster design can override.

### Element baseline
- **FIRE:** reaction denial, vision flare, heat strain, modest burst damage
- **AIR:** forced movement, prone, reaction denial, ranged defense
- **WATER:** cleanse, pull, prone, mist/obscure, bind
- **ICE:** slow/restrain, chilled, stasis, brittle defenses
- **EARTH:** cover, anchor, difficult terrain, shove prevention, weight
- **VERDANT:** restrain, poison, blight synergy, living barriers, mutualism

### Domain pressure baseline
- **KALDRAUN_STASIS:** Chilled, Whiteout, speed loss, stasis marks
- **KHALSARRA_WEIGHT:** Weighed, despair pressure, vow tests, anchor fields
- **CHARNELIX_BLIGHT:** Blighted, spores, healing interference, contamination zones
- **VAROOK_SILENCE:** Silenced, Haunted, fear/memory tricks
(Other domains can follow the same pattern.)

### “Condition budget” rule (prevents frustration)
- Minions/low CR: at most **one** condition rider, short duration.
- Controllers/elite: can apply conditions but must show counterplay and have lower damage.
- Boss: conditions are fine if they come with visible tells and counterplay.

---

## 3) CR sanity rules (v1.0)
We’ll be “5e-ish” without obsessing over perfect math:
- **Damage**: keep expected DPR aligned with comparable 5e creatures.
- **Control**: if you add strong control, reduce damage or limit uses.
- **Resistances**: 0–1 common resistance for most monsters; more only for elites/bosses.

---

## 4) Generator workflow (recommended)
1) Pick **Region** → choose primary element + motifs + domain (optional)
2) Choose **Role** (scout/bruiser/controller/etc.)
3) Choose **CR band** (1–2 / 3–5 / 6–10 / 11+)
4) Apply **Role chassis**:
   - AC/HP target
   - Speed/mobility tools
   - Action economy (reactions for skirmishers/controllers)
5) Apply **Tag package**:
   - 1 signature trait
   - 1 signature action
6) Add **Overlay thresholds** (if domain-linked)
7) Add **2 counterplays**
8) Final pass: clarity, fun, “one obstacle” pacing

---

# Exemplars (v1.0)
These are “gold standard” examples for the generator.

## EX1 — Kaldraun Whiteout Hunter (SCOUT, CR 3)
**Frostveil Stalker**  
Medium humanoid (tundra-born), neutral  
**AC** 14 (hide + frostwrap)  
**HP** 52 (8d8+16)  
**Speed** 35 ft  

STR 12 (+1) DEX 16 (+3) CON 14 (+2) INT 10 (+0) WIS 14 (+2) CHA 8 (-1)  
**Skills** Perception +4, Stealth +5, Survival +4  
**Senses** darkvision 60 ft, passive Perception 14  
**Languages** Common (or local cant)  
**CR** 3 (700 XP)  

**Tags:** ICE; motifs: WHITEOUT, HUNT; domain: KALDRAUN_STASIS; region: frozen_tundra

### Traits
**Whiteout Step.** While in snow, fog, or wind-driven ice, the stalker can take the Hide action as a bonus action.  
**Cold Nerves.** The stalker has advantage on saving throws against being frightened.

### Actions
**Multiattack.** The stalker makes two **Iceknife** attacks.  
**Iceknife.** *Melee Weapon Attack:* +5 to hit, reach 5 ft, one target. *Hit:* 7 (1d8+3) piercing plus 3 (1d6) cold.  
**Veil Snare (Recharge 5–6).** One creature the stalker can see within 30 ft must succeed on a **DC 13 CON save** or become **Chilled** until end of its next turn and cannot take reactions until the start of its next turn.

### Reaction
**Slip Into White (1/Short Rest).** When the stalker is hit, it halves the damage and moves up to 10 ft without provoking opportunity attacks (must end in light or heavy obscurity).

### Overlay Interaction (KALDRAUN_STASIS)
- **Track 2:** The stalker’s Veil Snare also imposes disadvantage on the target’s next Perception check this scene.  
- **Track 4:** The stalker gains a 10-ft **whiteout aura** (lightly obscured for enemies) while it is not in bright light.  
- **Track 6 Event:** A **veil gust** splits the party’s lines: each creature within 20 ft must succeed on a DC 13 STR save or be pushed 10 ft and knocked prone (then the aura ends).

### Counterplay (mandatory)
- **Resource:** Bright flame (torch, bonfire, etc.) within 10 ft ends the stalker’s Whiteout Step until end of its next turn.  
- **Skill/Action:** A DC 15 **Survival** check (as an action) identifies its wind-path; the next attack against it before end of next turn has advantage.

---

## EX2 — Khalsarra Monolith Binder (BRUISER, CR 5)
**Oathstone Brute**  
Large humanoid (monolith-bound), lawful neutral  
**AC** 15 (stone plates)  
**HP** 95 (10d10+40)  
**Speed** 30 ft  

STR 18 (+4) DEX 10 (+0) CON 18 (+4) INT 8 (-1) WIS 12 (+1) CHA 10 (+0)  
**Saving Throws** STR +7, CON +7  
**Skills** Athletics +7, Insight +4  
**Senses** passive Perception 11  
**Languages** Common, Terran (optional)  
**CR** 5 (1,800 XP)  

**Tags:** EARTH; motifs: VOW, DESPAIR, WEIGHT; domain: KHALSARRA_WEIGHT; region: cracked_earth

### Traits
**Sacred Weight.** Creatures that start their turn within 10 ft of the brute have their speed reduced by 5 ft until the start of their next turn (no save).  
**Vowbound.** The brute has advantage on saves against being charmed, and it cannot be compelled to break a declared order.

### Actions
**Multiattack.** The brute makes two **Stonefist** attacks.  
**Stonefist.** *Melee Weapon Attack:* +7 to hit, reach 5 ft, one target. *Hit:* 13 (2d8+4) bludgeoning.  
**Grief Press (Recharge 5–6).** One creature within 15 ft must succeed on a **DC 15 WIS save** or become **Weighed** until end of its next turn. While Weighed this way, the creature cannot take the Dash action.

### Bonus Action
**Anchor Stomp (PB/Long Rest).** The brute stomps; the ground in a 10-ft radius becomes difficult terrain until the start of its next turn.

### Overlay Interaction (KHALSARRA_WEIGHT)
- **Track 2:** Grief Press also gives the target disadvantage on its next Persuasion check this scene (despair fog).  
- **Track 4:** Sacred Weight radius increases to 15 ft; enemies in the radius have disadvantage on checks to resist forced movement.  
- **Track 6 Event:** A monolith “answers”: one 10-ft square becomes an **Anchor Field** for 1 round—creatures inside must succeed on DC 15 STR save or be restrained until end of their next turn.

### Counterplay (mandatory)
- **Choice:** If a PC declares a **purpose/vow** aloud (free, once per round) and follows it with an action consistent with it, the brute loses Sacred Weight until end of its next turn.  
- **Skill/Action:** A DC 15 **Ritecraft** check (action) marks a “witness line.” Until the end of the scene, the first time any creature would become Weighed from the brute, it ignores that condition.

---

## EX3 — Charnelix Spore Shepherd (CONTROLLER, CR 4)
**Blightcap Shepherd**  
Medium plant, neutral evil  
**AC** 13 (natural armor)  
**HP** 75 (10d8+30)  
**Speed** 25 ft  

STR 10 (+0) DEX 12 (+1) CON 16 (+3) INT 10 (+0) WIS 14 (+2) CHA 8 (-1)  
**Saving Throws** CON +5, WIS +4  
**Skills** Medicine +4, Stealth +3  
**Damage Resistances** poison  
**Condition Immunities** poisoned  
**Senses** darkvision 60 ft, passive Perception 12  
**Languages** understands Common but can’t speak  
**CR** 4 (1,100 XP)  

**Tags:** VERDANT; motifs: SPORES, DISEASE, WEB; domain: CHARNELIX_BLIGHT; region: sable_mire

### Traits
**Spore Bloom.** Creatures that start their turn within 10 ft of the shepherd must succeed on a **DC 14 CON save** or gain **Minor Strain** (no effect on success).  
**Blight Resilience.** The shepherd has advantage on saving throws against spells that would cure disease or end poison (it resists being “fixed”).

### Actions
**Slam.** *Melee Weapon Attack:* +3 to hit, reach 5 ft, one target. *Hit:* 7 (1d10+1) bludgeoning.  
**Spore Net (Recharge 5–6).** 20-ft cone. Creatures in the cone must succeed on a **DC 14 CON save** or become **Blighted** for 10 minutes. A creature that succeeds is not Blighted but has disadvantage on its next CON save this scene.

### Bonus Action
**Web-Lane Shift (1/Short Rest).** The shepherd moves up to 15 ft without provoking opportunity attacks and leaves behind a 10-ft patch of slick growth that counts as difficult terrain until end of its next turn.

### Overlay Interaction (CHARNELIX_BLIGHT)
- **Track 2:** Spore Bloom radius becomes 15 ft.  
- **Track 4:** Creatures that are Blighted in the bloom also have their speed reduced by 10 ft.  
- **Track 6 Event:** A blightwell “breathes”: the shepherd immediately recharges Spore Net and the area within 30 ft becomes lightly obscured by spores for 1 minute (wind disperses it).

### Counterplay (mandatory)
- **Resource:** Fire or strong cleansing water (at least 1 gallon + action) removes Blighted from one creature in the bloom (still requires DC 15 CON save if Track 4+).  
- **Skill/Action:** A DC 15 **Medicine** or **Ritecraft** check (action) identifies the spore sacs; the next time the shepherd uses Spore Net this scene, targets have advantage on the save.

---

## 5) Next steps for Monster Gen v1 (what we build next)
1) Role chassis tables (AC/HP/DPR targets per CR band)
2) Tag-to-trait library (“grafts”) per element and domain
3) Region pack integration (hazards + common motifs feed monster gen)
4) Generator code: `generate_monster(region, role, cr_band, domain_state)`

