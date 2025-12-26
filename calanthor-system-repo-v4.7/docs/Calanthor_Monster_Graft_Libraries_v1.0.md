# Calanthor Monster Gen v1 — Graft Libraries (v1.0)
*Plug-and-play traits/actions/reactions and overlay threshold packages keyed to elements + domains.*

**What is a graft?**  
A graft is a modular monster component (Trait, Action, Bonus Action, Reaction, or Threshold effect) that:
- carries tags (element/motif/domain)
- includes a clear mechanical payload
- has notes on role fit + control tier
- can be combined with the Role Chassis Tables to produce consistent, fun monsters

This library is written for fast generation:
- pick 1–2 grafts from the monster’s **primary element**
- add 0–2 from **secondary motifs**
- if domain-linked, add a **threshold package** (track 2/4/6)
- always add counterplay separately (next doc), but many grafts suggest it

---

## 0) Graft rules (official)
### 0.1 Component limits (to prevent overstuffing)
**Standard monster:**  
- 1 Signature Trait  
- 1 Signature Action  
- 1 Twist (bonus/reaction/movement rider)

**Controller:** may trade DPR for an extra twist.  
**Elite/Boss:** may add 1 extra twist, but must add more counterplay.

### 0.2 Control tier labeling
Each graft has a **Control Tier**:
- **Soft:** terrain, -10 speed, disadvantage on 1 roll, no reactions (1 round)
- **Medium:** prone/blind/restrain/silence (1 round) or stronger zone
- **Hard:** multi-round locks (boss-gated)

### 0.3 Save DC guidance
Use the chassis DC (or +1 for controllers) unless the graft specifies otherwise.

### 0.4 “Tell” requirement
Any graft that blinds/restrains/silences should include a **tell**:
- visible wind-up
- audible rattle
- glowing spores
- shifting stones

---

# 1) Element Grafts
Each element includes:
- Traits (passives)
- Actions (primary move)
- Twists (bonus/reaction/mobility)

Each graft lists: **Role Fit** and **Control Tier**.

## FIRE grafts
**Theme:** flare, fear pressure, reaction denial, heat strain, forging wards.

### Traits
**F-T1 — Heat Haze Aura (Trait)**  
Enemies within 10 ft have disadvantage on Perception checks relying on sight.  
Role Fit: Scout/Controller | Control: Soft | Motifs: VISION, HEAT

**F-T2 — Scorchproof (Trait)**  
Resistance to fire. (If taken, reduce HP by ~10% OR reduce control.)  
Role Fit: Bruiser/Elite | Control: None

**F-T3 — Panic Flare (Trait, 1/Scene)** *(Tell: sudden bright pulse)*  
When first bloodied (≤50% HP), creatures within 10 ft make CON save or cannot take reactions until end of their next turn.  
Role Fit: Skirmisher/Elite | Control: Soft/Medium

### Actions
**F-A1 — Searing Lash (Action)**  
Melee attack; on hit add 1d6 fire and target can’t take reactions until start of its next turn (CON save negates rider).  
Role Fit: Skirmisher/Bruiser | Control: Soft

**F-A2 — Flashburst (Action, Recharge 5–6)** *(Tell: ember swell)*  
15-ft cone; CON save or blinded until end of monster’s next turn (success: disadvantage on next attack only).  
Role Fit: Controller/Elite | Control: Medium

**F-A3 — Cinder Line (Action)**  
10-ft by 30-ft line becomes lightly obscured and difficult terrain until end of monster’s next turn. Creatures entering take small fire (PB-equivalent for CR band).  
Role Fit: Controller | Control: Soft

### Twists
**F-X1 — Ember Step (Bonus, 1/Short Rest)**  
Move 15 ft without OAs; first creature you pass takes small fire (no save).  
Role Fit: Scout/Skirmisher | Control: Soft

**F-X2 — Furnace Parry (Reaction, PB/Long Rest)**  
When hit by melee, reduce damage by PB-equivalent and deal same amount as fire back (cap by CR band).  
Role Fit: Bruiser/Elite | Control: None

---

## AIR grafts
**Theme:** forced movement, prone, deflection, silence slices, storm tells.

### Traits
**A-T1 — Wind-Read (Trait)**  
Advantage on Perception in open terrain; cannot be surprised by creatures relying on movement noise (GM).  
Role Fit: Scout | Control: None

**A-T2 — Slipstream Defense (Trait)**  
Ranged attacks against it have disadvantage beyond 30 ft.  
Role Fit: Skirmisher/Controller | Control: Soft

### Actions
**A-A1 — Gust Shove (Action)**  
STR save or pushed 10 ft; on fail target can’t take reactions until start of its next turn.  
Role Fit: Controller/Scout | Control: Soft

**A-A2 — Ridgebreaker Sweep (Action, Recharge 5–6)** *(Tell: air pressure drops)*  
DEX save or knocked prone; on success speed -10 until end of next turn.  
Role Fit: Bruiser/Controller | Control: Medium(Prone)

**A-A3 — Thin-Air Cut (Action, PB/Long Rest)** *(Tell: throat-tightening whistle)*  
CON save or silenced until end of target’s next turn (no verbal casting).  
Role Fit: Controller/Elite | Control: Medium(Silence)

### Twists
**A-X1 — Updraft Leap (Bonus, 1/Short Rest)**  
Leap/move vertically; ignores difficult terrain for the move; no OAs.  
Role Fit: Scout/Skirmisher | Control: None

**A-X2 — Deflecting Current (Reaction, 1/Scene)**  
Impose disadvantage on a ranged attack against an ally within 15 ft.  
Role Fit: Support/Elite | Control: Soft

---

## WATER grafts
**Theme:** pull, bind, mist, cleansing, tideguard.

### Traits
**W-T1 — Slick Flow (Trait)**  
It ignores difficult terrain from mud, shallow water, slick stone.  
Role Fit: Skirmisher/Scout | Control: None

**W-T2 — Mist Shroud (Trait, 1/Scene)** *(Tell: vapor bloom)*  
Create a 10-ft lightly obscured zone for 1 round when it takes damage.  
Role Fit: Controller/Scout | Control: Soft

### Actions
**W-A1 — Riptide Pull (Action)**  
STR save or pulled 10 ft; if pulled adjacent, target is knocked prone (DEX save negates prone).  
Role Fit: Controller | Control: Medium (prone)

**W-A2 — Undertow Bind (Action, Recharge 5–6)** *(Tell: water coils)*  
STR save or restrained until end of target’s next turn (success: speed -10).  
Role Fit: Controller/Elite | Control: Medium

**W-A3 — Cleansing Surge (Action, 1/Short Rest)**  
Ends one minor condition on an ally (Minor Strain/Chilled/poisoned nonmagical) and grants it +2 AC vs next attack (1 round).  
Role Fit: Support | Control: Soft

### Twists
**W-X1 — Tideguard (Reaction, 1/Scene)**  
Reduce damage to ally within 15 ft by PB-equivalent; ally moves 5 ft without OA.  
Role Fit: Support/Controller | Control: Soft

**W-X2 — Flow-Step (Bonus, PB/Long Rest)**  
Move 10–15 ft without OAs.  
Role Fit: Skirmisher | Control: None

---

## ICE grafts
**Theme:** stasis, chilled, slows, whiteout zones.

### Traits
**I-T1 — Whiteout Veil (Trait)**  
In snow/fog, it can Hide as bonus action.  
Role Fit: Scout | Control: None

**I-T2 — Brittle Aura (Trait)** *(Tell: rime crackle)*  
Enemies within 10 ft have -10 speed (no save) until they leave the aura.  
Role Fit: Bruiser/Controller | Control: Soft

### Actions
**I-A1 — Frost Numb (Action)**  
CON save or target has disadvantage on next weapon attack; on success no effect.  
Role Fit: Controller | Control: Soft

**I-A2 — Rime Shackles (Action, Recharge 5–6)** *(Tell: ice threads)*  
CON save or restrained until end of target’s next turn; success: speed -10.  
Role Fit: Controller/Elite | Control: Medium

**I-A3 — Veilstorm Line (Action)**  
15-ft line becomes icy; entering requires DEX save or prone.  
Role Fit: Controller | Control: Medium(prone) (zone)

### Twists
**I-X1 — Cold Brace (Reaction, 1/Scene)**  
Negate one application of Chilled/Minor Strain from cold hazard on self or ally within 10 ft.  
Role Fit: Support/Elite | Control: None

**I-X2 — Shatter Step (Bonus, 1/Short Rest)**  
Move 10 ft; creatures adjacent at start/end take small cold (cap by CR).  
Role Fit: Skirmisher | Control: Soft

---

## EARTH grafts
**Theme:** anchor, cover, weight, terrain, shove prevention.

### Traits
**E-T1 — Anchored Stance (Trait)**  
Advantage on STR saves vs being pushed/pulled; cannot be knocked prone unless by Huge+ or magic (GM).  
Role Fit: Bruiser | Control: None

**E-T2 — Stone Cover (Trait, 1/Short Rest)** *(Tell: rumble)*  
As a reaction when hit, raise partial cover (+2 AC) until start of its next turn.  
Role Fit: Elite/Controller | Control: Soft

### Actions
**E-A1 — Stonefist Slam (Action)**  
Melee attack; on hit, STR save or target is knocked prone.  
Role Fit: Bruiser | Control: Medium(prone)

**E-A2 — Anchor Field (Action, Recharge 5–6)** *(Tell: dust ring)*  
15-ft radius becomes difficult terrain; creatures starting inside STR save or cannot Dash this turn.  
Role Fit: Controller/Bruiser | Control: Soft/Medium

**E-A3 — Pillar Lift (Action, 1/Short Rest)**  
DEX save or lifted 10 ft and knocked prone; success: pushed 5 ft.  
Role Fit: Controller/Elite | Control: Medium

### Twists
**E-X1 — Brace Ally (Reaction, 1/Scene)**  
Prevent push or prone on ally within 10 ft.  
Role Fit: Support/Bruiser | Control: None

**E-X2 — Gravel Skitter (Bonus, PB/Long Rest)**  
Create 10-ft square difficult terrain (1 round).  
Role Fit: Controller | Control: Soft

---

## VERDANT grafts
**Theme:** vines, spores, mutualism, blight synergy, living walls.

### Traits
**V-T1 — Spore Bloom (Trait)** *(Tell: pollen shimmer)*  
Creatures starting within 10 ft make CON save or gain Minor Strain.  
Role Fit: Controller | Control: Soft

**V-T2 — Living Resilience (Trait)**  
Resistance to poison; advantage vs disease/contamination procedures (GM).  
Role Fit: Support/Elite | Control: None

### Actions
**V-A1 — Vine Tangle (Action)**  
STR save or restrained until end of target’s next turn; success: speed -10.  
Role Fit: Controller | Control: Medium

**V-A2 — Bloom Purge (Action, Recharge 5–6)** *(Tell: sacs swell)*  
15-ft cone; CON save or poisoned until end of target’s next turn (success: disadvantage on next CON save this scene).  
Role Fit: Controller | Control: Medium

**V-A3 — Living Rampart (Action, 1/Short Rest)**  
Create 10-ft line of growth granting half cover (1 minute).  
Role Fit: Support/Controller | Control: Soft

### Twists
**V-X1 — Symbiotic Guard (Reaction, 1/Scene)**  
When ally within 15 ft is hit, grant temp HP PB-equivalent and reduce attacker speed by 10 (no save).  
Role Fit: Support | Control: Soft

**V-X2 — Web-Lane Shift (Bonus, 1/Short Rest)**  
Move 15 ft without OAs, leave 10-ft difficult terrain patch (1 round).  
Role Fit: Controller/Skirmisher | Control: Soft

---

# 2) Domain Threshold Packages (Track 2/4/6)
These are overlay-linked “packages” monsters can inherit when tied to a domain.
Pick **one** package per monster (or per boss phase).

## KALDRAUN_STASIS packages
**K-TH1 — Whiteout Hunter Package**  
- **Track 2:** Once per round, when the monster hits, target has disadvantage on next Perception check this scene.  
- **Track 4:** Gains a 10-ft whiteout aura (lightly obscured for enemies) while not in bright light.  
- **Track 6 Event:** Veil gust: STR save or pushed 10 ft and prone in 20 ft radius; aura ends.

**K-TH2 — Stasis Mark Package** *(Tell: frost sigil forms)*  
- **Track 2:** First time a creature is Chilled this scene, it also loses reactions for 1 round.  
- **Track 4:** Chilled creatures have speed -10 while within 30 ft of the monster.  
- **Track 6 Event:** One creature becomes “Marked”: WIS save or restrained for 1 round (boss/elite only).

## KHALSARRA_WEIGHT packages
**KH-TH1 — Oathstone Burden Package**  
- **Track 2:** Weighed targets also take -2 to social checks in this scene (despair fog).  
- **Track 4:** Aura radius +5 ft; enemies have disadvantage on checks to resist forced movement.  
- **Track 6 Event:** Anchor Field square restrains on STR save (1 round).

**KH-TH2 — Grief Law Package** *(Tell: stone chant)*  
- **Track 2:** When a creature breaks a declared vow/purpose, the monster heals PB-equivalent HP (1/scene cap).  
- **Track 4:** The monster gains advantage on attacks vs creatures that have moved more than 20 ft this round.  
- **Track 6 Event:** “Judgment step”: one creature makes WIS save or is frightened until end of its next turn (soft if boss).

## CHARNELIX_BLIGHT packages
**C-TH1 — Blightwell Breath Package**  
- **Track 2:** Spore aura radius +5 ft.  
- **Track 4:** Blighted creatures in aura have speed -10.  
- **Track 6 Event:** Recharge a spore action; 30-ft area lightly obscured for 1 minute (wind disperses).

**C-TH2 — Contamination Web Package** *(Tell: strands glisten)*  
- **Track 2:** Difficult terrain patches persist 1 extra round.  
- **Track 4:** First time a creature enters a spore zone each round, CON save or Minor Strain.  
- **Track 6 Event:** Spawn 2 blight minions (summon cap applies).

## VAROOK_SILENCE packages
**V-TH1 — Hushline Package**  
- **Track 2:** Targets hit suffer disadvantage on their next Insight check this scene (doubt).  
- **Track 4:** Once per round, monster can impose **no reactions** on one target it can see (1 round; CON save negates).  
- **Track 6 Event:** 20-ft hush burst: CON save or silenced 1 round (boss/elite).

**V-TH2 — Memory Needle Package** *(Tell: whispering echo)*  
- **Track 2:** When a creature fails a WIS save vs the monster, it also suffers -10 speed for 1 round.  
- **Track 4:** One creature within 30 ft must reroll a successful WIS save (1/scene).  
- **Track 6 Event:** Apply Haunted to up to PB creatures (WIS save negates) for 10 minutes (counterplay required).

---

# 3) Minimal graft selection heuristics (for the generator)
- **Scout:** prefer mobility twists + perception traits; avoid hard control.
- **Bruiser:** prefer HP/anchor traits + prone riders; keep zones small.
- **Controller:** prefer zones + 1 medium control; reduce DPR; add counterplay.
- **Support:** prefer reactions that reduce damage/cleanse; avoid “save or lose.”
- **Elite/Boss:** add threshold package + visible tells + extra counterplay.

---

## Next doc (recommended): Counterplay Template Library
This graft library intentionally pairs with a dedicated counterplay template set:
- resource counters
- skill/action counters
- choice/bargain counters

