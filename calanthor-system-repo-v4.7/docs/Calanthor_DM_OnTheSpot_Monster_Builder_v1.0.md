# Calanthor Monster Gen v1 — DM On-the-Spot Builder (v1.0)
*A 60–120 second algorithm for improvising a complete Calanthor monster at the table.*

This quick builder uses the existing Monster Gen v1 modules:
- **Role Chassis Tables** (AC/HP/DPR/Atk/DC targets)
- **Graft Libraries** (element traits/actions/twists + domain threshold packages)
- **Counterplay Templates** (resource/skill/choice)

You can either **pick** or **roll**.

---

## 0) The 60-second build (pick method)
1) **Pick CR band** (0–1 / 2–3 / 4–5 / 6–7 / 8–10 / 11–13 / 14–16 / 17–20)  
2) **Pick Role** (Scout / Bruiser / Controller / Skirmisher / Support)  
3) **Pick Region + Domain** (Kaldraun / Khalsarra / Charnelix / Varook / etc.)  
4) Pull baseline from chassis → apply role modifiers:
   - AC, HP, DPR, Atk Bonus, Save DC
5) Choose **Primary Element** (often equals region resonance)  
6) Choose grafts:
   - 1 **Trait**
   - 1 **Signature Action**
   - 1 **Twist** (bonus/reaction/mobility)
7) If domain-linked: add 1 **Threshold Package** (Track 2/4/6)  
8) Add **Counterplay**:
   - Standard: 2 (two categories)
   - Elite: 3
   - Boss: 4 (include bargain/choice)
9) Write the statblock in the template at the end. Done.

---

## 1) The 90-second build (roll method)
Roll:
- **1d8 Domain/Region**
- **1d6 Role**
- **1d8 CR Band** (or choose based on party level)

### 1.1 d8 Domain/Region table
1. **Kaldraun (Frozen Tundra)** — ICE, WHITEOUT, STASIS (Dark Pet)  
2. **Khalsarra (Cracked Earth)** — EARTH, WEIGHT, VOW (Dark Pet)  
3. **Charnelix (Sable Mire)** — VERDANT, SPORES, BLIGHT (Dark Pet)  
4. **Varook (Gloomwood Border)** — AIR/SHADOW motifs, HUSH, MEMORY (Dark Pet)  
5. **Gaianok (Verdant Valley)** — VERDANT, MUTUALISM, STEWARDSHIP (Light Pet)  
6. **Shakora (Waters)** — WATER, LAW, FLOW (Light Pet)  
7. **Keairvari (Skyward Peaks)** — AIR, STORM, PASSAGE (Light Pet)  
8. **Nyvakira (Emberwood)** — FIRE, FORGE, RENEWAL (Light Pet)

### 1.2 d6 Role table
1 Scout  
2 Bruiser  
3 Controller  
4 Skirmisher  
5 Support  
6 **Elite** (apply Elite template on top of a rerolled role)

### 1.3 d8 CR band table (fast)
1 CR 0–1  
2 CR 2–3  
3 CR 4–5  
4 CR 6–7  
5 CR 8–10  
6 CR 11–13  
7 CR 14–16  
8 CR 17–20  

---

## 2) Snap math for attacks and damage (fast and safe)
Use the chassis **DPR target** after role modifiers. Then pick one of these attack patterns:

### Pattern A — Two attacks (most common)
- Multiattack 2× (melee or ranged)
- Each hit should average about **(DPR ÷ 2)** damage.

### Pattern B — One heavy hit + rider
- One attack at **~70% DPR**
- One soft control rider (push/no reactions/difficult terrain) or a short recharge ability.

### Pattern C — Controller zone
- One modest attack **(~40–60% DPR)**
- One zone/control ability (recharge 5–6 or 1/scene)

### “Average damage” cheat
- d6 ≈ 3.5
- d8 ≈ 4.5
- d10 ≈ 5.5
- d12 ≈ 6.5

Example: If your per-hit target is ~11 damage, that’s roughly **2d8+2** (9+2=11) or **1d10+6** (5.5+6=11.5).

> If you accidentally overshoot DPR, reduce control or reduce HP—don’t keep all three high.

---

## 3) Choosing grafts (fast rules)
- Pick grafts from **Calanthor_Monster_Graft_Libraries_v1.0.md**
- Prefer:
  - **Scout:** mobility + perception, avoid medium control spam
  - **Bruiser:** prone/shove, aura small
  - **Controller:** 1 zone + 1 medium control, DPR low end
  - **Skirmisher:** hit-and-run twist + forced movement
  - **Support:** damage reduction/cleanse, low DPR
- If you choose **Medium control**, you must include a counterplay that can end it early.

---

## 4) Counterplay assignment (fast rules)
Pick from **Calanthor_Monster_Counterplay_Templates_v1.0.md**
- Choose 1 that targets the **signature action**
- Choose 1 that targets the **zone/condition** (if any)
- Ensure categories differ (resource + skill OR resource + choice, etc.)

**Elite/Boss:** include at least one **Choice/Bargain** counterplay.

---

## 5) Statblock template (copy/paste)
Use 5e formatting; keep it readable.

**NAME**  
Size type, alignment  
**AC** __ | **HP** __ | **Speed** __  
STR __ DEX __ CON __ INT __ WIS __ CHA __  
**Saves** __ | **Skills** __  
**Resist/Immune** __  
**Senses** __ | **Languages** __ | **CR** __  

**Tags:** primary_element __; motifs __; domain __; region __

### Traits
- **Signature Trait (graft):** …
- (Optional) **Secondary Trait:** …

### Actions
- **Multiattack:** …
- **Signature Action (graft):** …
- (Optional) **Recharge Action:** …

### Bonus Actions / Reactions
- **Twist (graft):** …

### Overlay Interaction (if domain-linked)
- **Track 2:** …  
- **Track 4:** …  
- **Track 6 Event:** …  

### Counterplay (mandatory)
- **Resource:** …  
- **Skill/Action:** …  
- **Choice/Bargain:** … (Elite/Boss required)

---

## 6) Micro-examples (showing the algorithm in action)
### Example: “I need a quick Khalsarra bruiser” (60 seconds)
- CR band 4–5 → baseline AC 14–15, HP 71–110, DPR 19–28, Atk +5/+6, DC 13–15  
- Role Bruiser → HP +20%, AC -1, DPR +10%  
- Primary element EARTH
- Grafts: **Anchored Stance (trait)** + **Stonefist Slam (action)** + **Brace Ally (reaction)**  
- Threshold: **Oathstone Burden Package**  
- Counterplay: **Witness Chalk (resource)** + **Break the Anchor (skill)**  
Now write the block.

### Example: “I need a quick Kaldraun scout”
- CR 2–3 Scout, ICE grafts, Kaldraun threshold, counterplay: Bright Line + Cairn Reading.

---

## 7) Optional: “instant naming” (2 seconds)
Combine 2 words:
- Domain word (Whiteout / Oathstone / Blightcap / Hushline)
- Creature word (Stalker / Brute / Shepherd / Warden / Skirmisher)
Example: **Hushline Warden**, **Oathstone Brute**, **Blightcap Shepherd**

