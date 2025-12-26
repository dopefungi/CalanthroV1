# Calanthor Monster Gen v1 — Role Chassis Tables (v1.0)
*Role-first encounter design with 5e-ish outputs (AC/HP/DPR/to-hit/DC), plus control budgets.*

These tables power the Monster Gen v1 engine:
1) pick CR band
2) pick role (Scout/Bruiser/Controller/etc.)
3) apply chassis targets + role modifiers
4) graft tags/overlays/counterplay

This document is deliberately “good-enough 5e” for fast, consistent content.

---

## 0) Quick build sequence (official)
1. Choose **CR band** (or exact CR)
2. Choose **role**
3. Set targets from **Baseline Table**
4. Apply **Role Modifiers**
5. Add **signature** (1 trait + 1 action) from tags/domains
6. Add **overlay thresholds** (2/4/6) if domain-linked
7. Add **2 counterplays**
8. Sanity check: damage/control fairness

---

## 1) Baseline Table (by CR band)
These are *targets*, not laws. Stay close unless you have a clear reason.

**Key:**
- **AC**: average expected AC
- **HP**: typical hit point range
- **DPR**: expected damage per round (sustained; not spike)
- **Atk**: typical attack bonus
- **DC**: typical save DC for monster abilities

### CR Bands
| CR Band | AC | HP Range | DPR Target | Atk Bonus | Save DC |
|---|---:|---:|---:|---:|---:|
| 0–1 | 12–13 | 7–35 | 3–9 | +3 | 11–12 |
| 2–3 | 13–14 | 36–70 | 10–18 | +4 to +5 | 12–13 |
| 4–5 | 14–15 | 71–110 | 19–28 | +5 to +6 | 13–15 |
| 6–7 | 15–16 | 111–150 | 29–40 | +6 to +7 | 15–16 |
| 8–10 | 16–17 | 151–200 | 41–55 | +7 to +8 | 16–17 |
| 11–13 | 17–18 | 201–260 | 56–75 | +8 to +9 | 17–18 |
| 14–16 | 18–19 | 261–330 | 76–95 | +9 to +10 | 18–19 |
| 17–20 | 19–20 | 331–420 | 96–130 | +10 to +12 | 19–21 |

**Notes**
- If you add strong control (restraint/silence/blight), use the **lower end** of DPR.
- If you add resistances/immunities, reduce HP targets slightly or reduce control/damage.

---

## 2) Role Modifiers (apply after baseline)
Pick one role. Apply the modifier package to the baseline targets.

### SCOUT
- **HP:** -15% (lighter)  
- **Speed:** +10 ft (or climb/swim)  
- **DPR:** -10% (wins via positioning)  
- **Tools:** Hide as bonus action OR Disengage rider 1/scene; advantage on Perception/Stealth in home terrain

### BRUISER
- **HP:** +20%  
- **AC:** -1 (big target)  
- **DPR:** +10% (melee pressure)  
- **Tools:** shove/prone rider 1/short rest; simple aura (10 ft) allowed

### CONTROLLER
- **HP:** baseline  
- **DPR:** -20%  
- **DC:** +1 (their thing is control)  
- **Tools:** 1 zone effect + 1 condition rider; must include clear counterplay

### SKIRMISHER
- **HP:** baseline  
- **Speed:** +10 ft  
- **DPR:** baseline  
- **Tools:** reaction reposition OR hit-and-run (no OA) 1/short rest; prefers multi-target poke

### SUPPORT
- **HP:** -10%  
- **DPR:** -25%  
- **Tools:** heal/shield/buff allies; cleanse one condition 1/short rest; summons limited (see summon cap)

### ELITE (template, not a role)
Apply ELITE on top of another role:
- **HP:** +50%  
- **DPR:** +15%  
- **Extra:** +1 reaction/round OR 2 legendary actions (simple)  
- **Rule:** must include 2+ counterplays and a visible “tell” on big moves

### BOSS (template, not a role)
Apply BOSS on top of another role:
- **HP:** +100% (or “two bars”)  
- **DPR:** +25% (but avoid spike-kills)  
- **Extra:** 3 legendary actions OR 2-phase behavior (phase at 50% HP)  
- **Rule:** add **track 2/4/6** behavior as a built-in “lair pressure,” plus 3 counterplays

---

## 3) Control Budget (anti-frustration rule)
Control is the main way monsters feel unique. It must be budgeted.

### Control tiers
- **Soft control:** difficult terrain, -10 speed, disadvantage on 1 roll, no reactions (1 round)
- **Medium control:** prone, blinded (1 round), restrained (1 round), silenced (1 round)
- **Hard control:** restrained (repeat), incapacitate, long-duration silence, multi-round lock

### Budget by creature type
| Creature Type | Control Allowed |
|---|---|
| Minion / Swarm | soft control only (and short) |
| Standard | up to **1 medium** control per round *or* **2 soft** controls |
| Elite | up to **2 medium** controls per round, but DPR must be reduced accordingly |
| Boss | hard control allowed **only with** (a) tell, (b) counterplay, (c) limited uses/threshold gating |

**Hard rule:** if you apply **Medium/Hard** control, always add **counterplay** that can end/prevent it.

---

## 4) Summon Cap (keeps fights fast)
If a monster summons creatures:
- Standard monsters: **1 summon** (CR ≤ 1/4 each) OR **2 minions** max
- Elite: **2 summons** OR **4 minions** max
- Boss: **3 summons** OR **6 minions** max (prefer waves at phase changes)

Summons should be “simple statlines” (minion templates), not full complexity monsters.

---

## 5) Resistance/Immunity guideline
To avoid slog:
- Standard: **0–1** common resistance (poison/cold/fire)  
- Elite: up to **2** resistances, **1** immunity if lore-justified  
- Boss: resistances OK, but pair with counterplay that strips/ignores them

If you add **multiple resistances**, reduce HP by ~10–15% or reduce control.

---

## 6) “Signature package” checklist (every monster)
Every monster needs:
1) **Signature Trait** (passive identity)
2) **Signature Action** (main move)
3) **One twist** (reaction, bonus action, or movement rider)
4) **Overlay thresholds** if domain-linked (2/4/6)
5) **Two counterplays** (different categories)

---

## 7) Example: applying the chassis (quick)
**Goal:** CR 4–5 controller (Charnelix theme)
- Baseline CR 4–5: AC 14–15, HP 71–110, DPR 19–28, Atk +5/+6, DC 13–15
- Controller mods: DPR -20% → ~15–22; DC +1 → 14–16
- Add: spore zone + blight rider (medium control) → keep damage on low end
- Add counterplay: fire/water cleanse + medicine/ritecraft sac targeting

This matches our exemplar style.

