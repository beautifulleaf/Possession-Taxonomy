# DPW1_E4 report (E4 Weapons & Armour, wave 3, offline)

Inputs: HV_E4_1/2 reports and fetch logs, TREE_E4 and map (105 kinds, all in data), memo §12–14, 410 named forms, 18 lines. No DPMK_1_E4 file exists.

## Task 1: 68 candidates (`DPW1_E4_kinds.tsv`)
new_kind 25 · named_form 17 · covered 12 · attribute 9 · other_category 5.

**New kinds** (next free id per parent, R-58; each with a logged harvester URL):
- Firearms: E4.1.1.02 Single-shot or derringer pistol; E4.1.4.06 Single-shot shotgun.
- Swords: E4.4.1.04 Short sword; E4.4.2.07 Falchion; E4.4.3.03 Sword cane.
- Polearms, impact: E4.6.1.05 Poleaxe; E4.6.2.03 Fighting sickle (kama); E4.6.4.07 Pronged truncheon (sai).
- Armour: E4.8.1.03 Gorget; E4.8.2.05 Mail shirt; .06 Cuirass; .07 Brigandine.
- Reloading: E4.9.13 Cartridge case; E4.9.14 Shotshell wad.
- Parts: E4.10.1.02 Iron sight; .03 Barrel; .04 Trigger; .05 Suppressor; E4.10.2.03 Bow riser; .04 Arrowhead; E4.10.3.04 Hilt collar and pommel cap (fuchi-kashira); .05 Scabbard pocket fitting (kozuka, kogai); E4.10.4.05 Red-dot sight; .06 Scope mount; .07 CO2 capsule.

**Other categories:** kukri machete and parang to C2 (R-16a); personal alarm to B8 (K-88); bowfishing bow to E2 (§14 E4-8); Vorderlader-Böller OUT (a saluting mortar, K-85). I am not sure of the Böller call; it needs a check.

## Task 2: 7 moves (`DPW1_E4_moves.tsv`)
- **move_kind (3):** Trailblazer LifeCard to E4.1.1.02; Hoyt ILF riser to E4.10.2.03; Seax to E4.5.03 (single-edged).
- **drop (2):** the duplicate Pedersoli side-by-side under E4.1.4.02 (E-21); Spyderco BaliYo, a bladeless toy.
- **to_line (2):** Boker Kalashnikov to L-boker-kalashnikov; ASP Friction Loc to a new line, L-asp-friction-loc.

No named form is a maker or a shop.

For a maker pass:
- Makers under two ids: M-hanwei and M-hanwei-paul-chen; M-baltimore-knife-sword and M-baltimore-knife-and-sword; M-thompson-center and M-thompson-center-arms; M-winchester and M-winchester-repeating-arms; M-jts and M-jts-airguns.
- Tizona (NF-E4.4.3.01-002) is an LK Chen product but is stored as not maker-bound.
- The Colt Defender CO2 pistol needs a licensor.

## Task 3: navigation
**Confirmed: type of object first** (R-116), with the use view beside it.
- Shops shelve by family, then form or action (Kult of Athena, Pyramyd, Lancaster, Sportsman's, Frankonia).
- Firearms, air guns, bows and ammunition: 186 named forms, almost all maker-bound models, so the model leads (maker role: owner).
- Swords and knives: 150 named forms from 40 makers, and shops also shelve these makers apart. So blades and armour keep a makers-and-smiths tab (way in). No scene structure shows in the data.

View:
1. Ten display groups (Firearms … Parts, optics & fittings), with the "What is it for?" use view beside them.
2. Leaves, for example Swords → Straight double-edged · Single-edged · Thrusting. Knives and Self-defence go straight to kinds.
3. Kinds, for example Single-edged → Sabre · Falchion · Cutlass · Katana …, then named forms. Where makers are the way in, a Makers & smiths tab sits beside the kinds, with the nihonto school table.

## Rules applied
C2(a)(b)(d), C3, C10(b), C11, C14(b), C15, S3, K-83 to K-88, K-163, R-16a, E-4, E-21, CV-19, R-19, R-58, §14.

## Provisional or † items
- Multi-pump stays an attribute until a C10(b) source ranks it (memo † item).
- The kind level of kama, sai, fuchi-kashira and kozuka/kogai is provisional (R-19).
- E4.9 now holds 14 kinds, above the "about 12" of C5(b): the next build should add a reloading leaf by role, keeping the ids.
- New kinds are attested in HV_NK.
