# Calanthor Starter Bestiary (v1.0)
*12 ready-to-run monsters generated from: Chassis + Grafts + Counterplay + Domain Thresholds.*

Design goals:
- **D&D-readable** statblocks
- **Calanthor-unique** pressure via overlays (Track 2/4/6)
- **Mandatory counterplay** so hazards feel fair

**Included set**
- Harsh dominions (2 each): **Kaldraun, Khalsarra, Charnelix, Varook** = 8
- Border creatures (4): Verdant edge, Ember edge, Sky edge, Mire edge = 4

> GM note: Treat “Track 2/4/6” lines as the monster’s *interaction with the relevant domain overlay*, per the Domain Overlay Operating Rules.

---

## KALDRAUN (Frozen Tundra) — Dark Pet
### 1) Driftglass Whelp (Scout, CR 1)
Small beast, unaligned  
**AC** 13 | **HP** 27 (6d6+6) | **Speed** 40 ft  
STR 10 DEX 15 CON 12 INT 2 WIS 12 CHA 6  
**Skills** Perception +3, Stealth +4, Survival +3  
**Senses** darkvision 60 ft | **CR** 1  

**Tags:** ICE; motifs: WHITEOUT, HUNT; domain: KALDRAUN_STASIS; region: frozen_tundra

### Traits
**Whiteout Veil.** In snow/fog, the whelp can Hide as a bonus action. *(I-T1)*

### Actions
**Bite.** *Melee Weapon Attack:* +4 to hit, reach 5 ft, one target. *Hit:* 6 (1d6+3) piercing.  
**Frost Numb.** One creature the whelp can see within 30 ft must succeed on a **DC 12 CON save** or have disadvantage on its next weapon attack. *(I-A1)*

### Bonus Action
**Shatter Step (1/Short Rest).** The whelp moves 10 ft without provoking opportunity attacks; creatures adjacent at start or end take 2 cold damage. *(I-X2, capped)*

### Overlay Interaction (KALDRAUN_STASIS — Whiteout Hunter Package)
- **Track 2:** On a hit (1/round), target has disadvantage on its next Perception check this scene.  
- **Track 4:** The whelp gains a 10-ft whiteout aura (enemies lightly obscured) while not in bright light.  
- **Track 6 Event:** Veil gust: creatures within 20 ft DC 12 STR save or pushed 10 ft and knocked prone; aura ends.

### Counterplay
- **Resource:** **Bright Line** — a torch/bonfire within 10 ft reduces the aura/ends Whiteout Veil for 1 round.  
- **Skill/Action:** **Cairn Reading** — DC 14 Survival (action) prevents the next Track 2 effect this obstacle.

---

### 2) Cairn-Sealer Sentinel (Bruiser, CR 5)
Large construct, lawful neutral  
**AC** 14 | **HP** 120 (16d10+32) | **Speed** 30 ft  
STR 18 DEX 10 CON 14 INT 6 WIS 12 CHA 7  
**Saves** STR +7, CON +5 | **Skills** Athletics +7  
**Damage Resistances** cold  
**Senses** darkvision 60 ft | **CR** 5  

**Tags:** ICE/EARTH; motifs: STASIS, SHELTER; domain: KALDRAUN_STASIS; region: frozen_tundra

### Traits
**Brittle Aura.** Enemies within 10 ft have their speed reduced by 10 while in the aura. *(I-T2)*  
**Anchored Stance.** Advantage on STR saves vs forced movement. *(E-T1)*

### Actions
**Multiattack.** The sentinel makes two **Stonefist Slam** attacks.  
**Stonefist Slam.** *Melee Weapon Attack:* +7 to hit, reach 5 ft. *Hit:* 13 (2d8+4) bludgeoning; target DC 15 STR save or prone. *(E-A1)*  
**Rime Shackles (Recharge 5–6).** One creature within 30 ft DC 15 CON save or restrained until end of its next turn; success: speed -10. *(I-A2)*

### Reaction
**Cold Brace (1/Scene).** Negate one application of Chilled/Minor Strain from cold hazard on self or ally within 10 ft. *(I-X1)*

### Overlay Interaction (KALDRAUN_STASIS — Stasis Mark Package)
- **Track 2:** First time a creature becomes Chilled this scene, it also loses reactions for 1 round.  
- **Track 4:** Chilled creatures within 30 ft have speed -10.  
- **Track 6 Event:** One creature DC 15 WIS save or restrained for 1 round (tell: frost sigil forms).

### Counterplay
- **Resource:** **Bright Line** — strong light/heat within 10 ft suppresses Brittle Aura for 1 round.  
- **Skill/Action:** **Breath Discipline** — DC 15 CON or Survival (action) lets you ignore speed penalties from aura for 1 round.

---

## KHALSARRA (Cracked Earth) — Dark Pet
### 3) Dustbound Skirmisher (Skirmisher, CR 3)
Medium humanoid, neutral  
**AC** 14 | **HP** 58 (9d8+18) | **Speed** 40 ft  
STR 12 DEX 16 CON 14 INT 10 WIS 12 CHA 10  
**Skills** Acrobatics +5, Athletics +3  
**Senses** passive Perception 11 | **CR** 3  

**Tags:** EARTH; motifs: WEIGHT, AMBUSH; domain: KHALSARRA_WEIGHT; region: cracked_earth

### Traits
**Anchored Stance.** Advantage on STR saves vs forced movement. *(E-T1)*

### Actions
**Multiattack.** Two **Stonefist** attacks.  
**Stonefist.** *Melee Weapon Attack:* +5 to hit. *Hit:* 8 (1d8+4) bludgeoning.  
**Anchor Field (Recharge 5–6).** 15-ft radius becomes difficult terrain until start of skirmisher’s next turn; creatures starting inside DC 13 STR save or can’t Dash this turn. *(E-A2)*

### Bonus Action
**Gravel Skitter (PB/Long Rest).** Create one 10-ft square difficult terrain (1 round). *(E-X2)*

### Overlay Interaction (KHALSARRA_WEIGHT — Oathstone Burden Package)
- **Track 2:** Weighed targets also take -2 to social checks this scene.  
- **Track 4:** Aura/fields expand (+5 ft); enemies have disadvantage to resist forced movement.  
- **Track 6 Event:** One 10-ft square becomes an Anchor Field: DC 13 STR save or restrained 1 round.

### Counterplay
- **Resource:** **Witness Chalk** — mark a boundary; inside gain advantage vs Weighed for 1 round.  
- **Skill/Action:** **Break the Anchor** — DC 13 Athletics/Ritecraft (action) ends one 10-ft difficult-terrain patch for 1 round.

---

### 4) Oathstone Brute (Bruiser, CR 7)
Large humanoid, lawful neutral  
**AC** 15 | **HP** 170 (20d10+60) | **Speed** 30 ft  
STR 20 DEX 10 CON 18 INT 8 WIS 12 CHA 11  
**Saves** STR +9, CON +8 | **Skills** Athletics +9, Insight +5  
**CR** 7  

**Tags:** EARTH; motifs: VOW, DESPAIR, WEIGHT; domain: KHALSARRA_WEIGHT; region: cracked_earth

### Traits
**Sacred Weight.** Creatures that start within 10 ft have speed -5 until start of their next turn.  
**Anchored Stance.** Advantage on STR saves vs forced movement. *(E-T1)*

### Actions
**Multiattack.** Two **Stonefist Slam** attacks.  
**Stonefist Slam.** +9 to hit. *Hit:* 16 (2d10+5) bludgeoning; DC 16 STR save or prone. *(E-A1 scaled)*  
**Pillar Lift (1/Short Rest).** DC 16 DEX save or lifted 10 ft and prone; success: pushed 5 ft. *(E-A3)*

### Reaction
**Brace Ally (1/Scene).** Prevent push or prone on ally within 10 ft. *(E-X1)*

### Overlay Interaction (KHALSARRA_WEIGHT — Grief Law Package)
- **Track 2:** When a creature breaks a declared vow/purpose, the brute heals 7 HP (1/scene cap).  
- **Track 4:** The brute has advantage on attacks vs creatures that moved >20 ft this round.  
- **Track 6 Event:** Judgment step: DC 16 WIS save or frightened until end of its next turn (tell: stone chant).

### Counterplay
- **Skill/Action:** **Witness Line** — DC 16 Ritecraft/Persuasion (action) prevents the next Track 4 upgrade this obstacle.  
- **Choice/Bargain:** **Declare Purpose** — vow + act immediately to reduce weight pressure by 1 step (cost: Minor Strain if vow later broken).

---

## CHARNELIX (Sable Mire) — Dark Pet
### 5) Mirelurk Sporeling (Scout, CR 2)
Small plant, neutral evil  
**AC** 13 | **HP** 45 (10d6+10) | **Speed** 30 ft, climb 20 ft  
STR 10 DEX 14 CON 12 INT 4 WIS 12 CHA 6  
**Skills** Stealth +4  
**Damage Resistances** poison | **Condition Immunities** poisoned  
**CR** 2  

**Tags:** VERDANT; motifs: SPORES, WEB; domain: CHARNELIX_BLIGHT; region: sable_mire

### Traits
**Spore Bloom.** Start within 10 ft: DC 13 CON save or Minor Strain. *(V-T1)*

### Actions
**Claw.** *Melee Weapon Attack:* +4 to hit. *Hit:* 6 (1d6+3) slashing.  
**Vine Tangle.** One creature within 30 ft DC 13 STR save or restrained until end of its next turn; success: speed -10. *(V-A1)*

### Bonus Action
**Web-Lane Shift (1/Short Rest).** Move 15 ft no OA; leave a 10-ft difficult-terrain patch (1 round). *(V-X2)*

### Overlay Interaction (CHARNELIX_BLIGHT — Contamination Web Package)
- **Track 2:** Difficult terrain patches persist +1 round.  
- **Track 4:** First time a creature enters a spore zone each round: DC 13 CON save or Minor Strain.  
- **Track 6 Event:** Spawn 2 blight minions (summon cap applies).

### Counterplay
- **Resource:** **Mask & Wash** — cloth mask/clean water grants advantage vs spores this scene.  
- **Skill/Action:** **Sac Targeting** — DC 13 Medicine/Nature (action) makes next spore effect give advantage on saves.

---

### 6) Blightcap Shepherd (Controller, CR 4)
Medium plant, neutral evil  
**AC** 13 | **HP** 75 (10d8+30) | **Speed** 25 ft  
STR 10 DEX 12 CON 16 INT 10 WIS 14 CHA 8  
**Saves** CON +5, WIS +4  
**Damage Resistances** poison | **Condition Immunities** poisoned  
**Senses** darkvision 60 ft | **CR** 4  

**Tags:** VERDANT; motifs: SPORES, DISEASE; domain: CHARNELIX_BLIGHT; region: sable_mire

### Traits
**Spore Bloom.** Start within 10 ft DC 14 CON save or Minor Strain. *(V-T1)*

### Actions
**Slam.** +3 to hit. *Hit:* 7 (1d10+1) bludgeoning.  
**Bloom Purge (Recharge 5–6).** 15-ft cone; DC 14 CON save or poisoned until end of target’s next turn; success: disadvantage on next CON save this scene. *(V-A2)*

### Bonus Action
**Web-Lane Shift (1/Short Rest).** Move 15 ft no OA; leave 10-ft difficult terrain patch (1 round). *(V-X2)*

### Overlay Interaction (CHARNELIX_BLIGHT — Blightwell Breath Package)
- **Track 2:** Spore aura radius +5 ft.  
- **Track 4:** Blighted/poisoned creatures in aura have speed -10.  
- **Track 6 Event:** Recharge Bloom Purge; 30-ft spores lightly obscure for 1 minute.

### Counterplay
- **Resource:** **Clean Water / Fire** — remove Blighted/poisoned (nonmagical) from one creature (Track 4+: DC 15 CON save).  
- **Skill/Action:** **Antidote Craft** — DC 16 Medicine (action) grants one ally advantage vs Blight saves to end of scene.

---

## VAROOK (Gloomwood Border) — Dark Pet
### 7) Hushline Sentry (Controller, CR 3)
Medium humanoid, neutral evil  
**AC** 14 | **HP** 60 (11d8+11) | **Speed** 30 ft  
STR 10 DEX 14 CON 12 INT 12 WIS 14 CHA 10  
**Skills** Insight +4, Stealth +4  
**CR** 3  

**Tags:** AIR; motifs: HUSH, DOUBT; domain: VAROOK_SILENCE; region: gloomwood_border

### Traits
**Slipstream Defense.** Ranged attacks against it have disadvantage beyond 30 ft. *(A-T2)*

### Actions
**Knife.** *Melee Weapon Attack:* +4 to hit. *Hit:* 6 (1d6+3) piercing.  
**Thin-Air Cut (PB/Long Rest).** One creature within 30 ft DC 13 CON save or silenced until end of its next turn. *(A-A3)*

### Reaction
**Deflecting Current (1/Scene).** Impose disadvantage on a ranged attack against an ally within 15 ft. *(A-X2)*

### Overlay Interaction (VAROOK_SILENCE — Hushline Package)
- **Track 2:** Targets hit suffer disadvantage on their next Insight check this scene.  
- **Track 4:** 1/round impose no reactions on one target it can see (DC 13 CON save negates).  
- **Track 6 Event:** 20-ft hush burst: DC 13 CON save or silenced 1 round (tell: pressure drop).

### Counterplay
- **Resource:** **Name-Cord** — ignore one Silenced/Haunted application this scene.  
- **Skill/Action:** **Recall Anchor** — DC 13 Insight/History (action) reduces hush duration by one step.

---

### 8) Memory-Needle Harrower (Skirmisher, CR 6)
Medium fey, chaotic neutral  
**AC** 16 | **HP** 125 (17d8+51) | **Speed** 40 ft  
STR 12 DEX 18 CON 16 INT 12 WIS 14 CHA 12  
**Saves** DEX +7, WIS +5 | **Skills** Acrobatics +7, Insight +5, Stealth +7  
**CR** 6  

**Tags:** AIR; motifs: MEMORY, HAUNT; domain: VAROOK_SILENCE; region: gloomwood_border

### Traits
**Wind-Read.** Advantage on Perception in open terrain; not surprised by noise-movers (GM). *(A-T1)*

### Actions
**Multiattack.** Two **Gust Shove** attacks (as weapon-like strikes).  
**Gust Shove.** One target DC 15 STR save or pushed 10 ft and can’t take reactions until start of its next turn. *(A-A1, upgraded DC)*  
**Ridgebreaker Sweep (Recharge 5–6).** DC 15 DEX save or prone; success: speed -10 until end of next turn. *(A-A2)*

### Bonus Action
**Updraft Leap (1/Short Rest).** Move vertically/over obstacles; no OAs during the move. *(A-X1)*

### Overlay Interaction (VAROOK_SILENCE — Memory Needle Package)
- **Track 2:** When a creature fails a WIS save vs the harrower, it also suffers -10 speed for 1 round.  
- **Track 4:** 1/scene force reroll of a successful WIS save (within 30 ft).  
- **Track 6 Event:** Up to PB creatures DC 15 WIS save or become Haunted for 10 minutes (tell: whispering echo).

### Counterplay
- **Skill/Action:** **Read the Pattern** — DC 17 Insight (action) gives next ally advantage and negates one reroll effect this scene.  
- **Choice/Bargain:** **Speak the Truth** — confess a relevant truth to prevent the next Track 6 event this obstacle (story cost: omen mark).

---

## BORDER CREATURES (Mixed dominions)
### 9) Gaianok Bramblewarden (Support, CR 2)
Medium plant, neutral  
**AC** 13 | **HP** 45 (6d8+18) | **Speed** 25 ft  
STR 12 DEX 10 CON 16 INT 8 WIS 14 CHA 8  
**Skills** Medicine +4  
**Resistances** poison | **CR** 2  

**Tags:** VERDANT; motifs: MUTUALISM, COVER; region: verdant_valley_edge (Light Pet)

### Traits
**Living Resilience.** Resistance to poison; advantage vs disease/contamination procedures (GM). *(V-T2)*

### Actions
**Bramble Staff.** +3 to hit. *Hit:* 7 (1d8+3) bludgeoning.  
**Living Rampart (1/Short Rest).** Create 10-ft line half cover (1 minute). *(V-A3)*

### Reaction
**Symbiotic Guard (1/Scene).** When an ally within 15 ft is hit, grant it 3 temp HP and reduce attacker speed by 10 (no save). *(V-X1 cap)*

### Counterplay (for enemies / to keep it fair)
- **Resource:** Fire clears one 10-ft section of Living Rampart.  
- **Skill/Action:** DC 13 Nature (action) identifies weak roots; next attack vs rampart has advantage and deals double damage to it.

---

### 10) Nyvakira Cinder-Runner (Scout, CR 4)
Medium humanoid, neutral  
**AC** 14 | **HP** 75 (10d8+30) | **Speed** 40 ft  
STR 10 DEX 16 CON 16 INT 10 WIS 12 CHA 12  
**Skills** Acrobatics +5, Perception +3  
**CR** 4  

**Tags:** FIRE; motifs: FORGE, FEAR; region: emberwood_edge (Light Pet)

### Traits
**Heat Haze Aura.** Enemies within 10 ft have disadvantage on sight-based Perception checks. *(F-T1)*

### Actions
**Multiattack.** Two **Searing Lash** attacks.  
**Searing Lash.** +6 to hit. *Hit:* 10 (1d8+3 + 1d6) fire; DC 14 CON save negates “no reactions until start of next turn.” *(F-A1)*  
**Cinder Line.** 30-ft line lightly obscured + difficult terrain 1 round; entering takes 4 fire damage. *(F-A3 cap)*

### Bonus Action
**Ember Step (1/Short Rest).** Move 15 ft no OA; first creature you pass takes 4 fire damage. *(F-X1 cap)*

### Counterplay
- **Resource:** **Smother & Starve** — wet ground/blanket ends Cinder Line for 1 round.  
- **Skill/Action:** **Vent the Heat** — DC 14 Ritecraft/Survival (action) prevents “no reactions” rider from the next FIRE hit this round.

---

### 11) Keairvari Stormkite (Skirmisher, CR 1/2)
Small beast, unaligned  
**AC** 13 | **HP** 18 (4d6+4) | **Speed** 10 ft, fly 40 ft  
STR 6 DEX 16 CON 12 INT 2 WIS 12 CHA 6  
**Skills** Perception +3  
**CR** 1/2  

**Tags:** AIR; motifs: STORM, PASSAGE; region: skyward_peaks_edge (Light Pet)

### Traits
**Slipstream Defense.** Ranged attacks against it have disadvantage beyond 30 ft. *(A-T2)*

### Actions
**Talons.** *Melee Weapon Attack:* +5 to hit. *Hit:* 6 (1d6+3) slashing.  
**Gust Shove.** DC 12 STR save or pushed 10 ft and can’t take reactions until start of next turn. *(A-A1)*

### Bonus Action
**Updraft Leap (1/Short Rest).** The stormkite moves up to 15 ft (including vertical) without provoking OAs. *(A-X1 cap)*

### Counterplay
- **Resource:** **Anchor Up** — rope/pitons grants advantage vs shove/push saves this scene.  
- **Choice:** **Give Ground** — accept the push to avoid the “no reactions” rider this time.

---

### 12) Mireline Carrion-Swallower (Bruiser, CR 5)
Large beast, unaligned  
**AC** 14 | **HP** 130 (15d10+45) | **Speed** 35 ft, swim 20 ft  
STR 18 DEX 12 CON 16 INT 3 WIS 12 CHA 6  
**Saves** CON +6  
**Resistances** poison | **CR** 5  

**Tags:** VERDANT/WATER; motifs: MIASMA, HUNGER; region: mire_border (Dark Pet influence nearby)

### Traits
**Spore Bloom.** Start within 10 ft DC 15 CON save or Minor Strain. *(V-T1 scaled)*  
**Slick Flow.** Ignores difficult terrain from mud/shallow water. *(W-T1)*

### Actions
**Multiattack.** Two **Bite** attacks.  
**Bite.** +7 to hit. *Hit:* 13 (2d8+4) piercing.  
**Undertow Bind (Recharge 5–6).** DC 15 STR save or restrained until end of target’s next turn; success: speed -10. *(W-A2)*

### Reaction
**Tideguard (1/Scene).** Reduce damage to an ally beast within 15 ft by 5; it moves 5 ft without OA. *(W-X1 cap)*

### Counterplay
- **Resource:** **Mask & Wash** — advantage on CON saves vs spores this scene.  
- **Skill/Action:** **Break the Bind** — DC 15 Athletics (action) downgrades restrained to -10 speed for this turn.

---

## Appendix: Fast bestiary use
- For **1–2 encounters**, use Standard creatures as written.  
- For **set-piece fights**, apply the **Elite** template to monster #2, #4, #6, or #8.  
- For a **boss**, combine an Elite with a Threshold Package and add 1–2 extra counterplays.

