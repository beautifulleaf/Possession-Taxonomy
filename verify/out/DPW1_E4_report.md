# DPW1_E4 report (E4 Weapons & Armour, wave 3, offline)

**Inputs:** HV_E4_1/2 reports and fetch logs, TREE_E4 and map (105 kinds, all in data), memo §12–14, 410 named forms, 18 lines. There is no DPMK_1_E4 file.

## Task 1: 68 candidates (`DPW1_E4_kinds.tsv`)
new_kind 25 · named_form 17 · covered 12 · attribute 9 · other_category 5.

**New kinds** (next free id under each parent, R-58; each has a full or partial logged harvester URL):
- Firearms: E4.1.1.02 Single-shot or derringer pistol; E4.1.4.06 Single-shot shotgun.
- Swords: E4.4.1.04 Short sword; E4.4.2.07 Falchion; E4.4.3.03 Sword cane.
- Polearms and impact weapons: E4.6.1.05 Poleaxe; E4.6.2.03 Fighting sickle (kama); E4.6.4.07 Pronged truncheon (sai).
- Armour: E4.8.1.03 Gorget; E4.8.2.05 Mail shirt; E4.8.2.06 Cuirass; E4.8.2.07 Brigandine.
- Ammunition and reloading: E4.9.13 Cartridge case; E4.9.14 Shotshell wad.
- Parts: E4.10.1.02 Iron sight; .03 Barrel; .04 Trigger; .05 Suppressor; E4.10.2.03 Bow riser; .04 Arrowhead; E4.10.3.04 Hilt collar and pommel cap (fuchi-kashira); .05 Scabbard pocket fitting (kozuka, kogai); E4.10.4.05 Red-dot sight; .06 Scope mount; .07 CO2 capsule.

**Other categories:** kukri machete and parang go to C2 (machete note, R-16a). Personal alarm goes to B8 (K-88). Bowfishing bow goes to E2 (fishing tackle, §14 E4-8). Vorderlader-Böller is OUT for now (a saluting mortar, K-85). I am not sure of that last call; the owner or the next pass should check it.

## Task 2: 7 moves (`DPW1_E4_moves.tsv`)
- **move_kind (3):** Trailblazer LifeCard goes to E4.1.1.02. The Hoyt ILF riser goes to E4.10.2.03. Seax goes to E4.5.03, because it is single-edged and the dagger kind is double-edged.
- **drop (2):** the duplicate Pedersoli side-by-side under E4.1.4.02 (it is already filed as a muzzle-loader, E-21). Spyderco BaliYo, a bladeless flipper toy.
- **to_line (2):** Boker Kalashnikov goes to the existing L-boker-kalashnikov. ASP Friction Loc goes to a new line, L-asp-friction-loc.

No named form turned out to be a maker or a shop.

Points for a maker pass, outside the moves file:
- Same makers stored under two ids: M-hanwei and M-hanwei-paul-chen; M-baltimore-knife-sword and M-baltimore-knife-and-sword; M-thompson-center and M-thompson-center-arms; M-winchester and M-winchester-repeating-arms; M-jts and M-jts-airguns.
- "Tizona" (NF-E4.4.3.01-002) is an LK Chen product but is stored as not maker-bound.
- The Colt Defender CO2 pistol needs a licensor.
- L-buck-knives-buck-fixed-blade-hunters reads like a harvester's label, not a Buck line.

## Task 3: navigation
**Confirmed: type of object first** (R-116 proposal), with the use view beside it.
- The harvest shows shops shelve by weapon family, then by form or action: Kult of Athena sword and armour categories, Pyramyd powerplants, Lancaster bow types, Sportsman's actions, Frankonia's Büchsen and Flinten.
- Firearms, air guns, bows and ammunition are 186 named forms, almost all maker-bound models, so the model leads there (maker role: owner).
- Swords and knives are 150 named forms from 40 makers, and the shops also shelve those makers apart. The blade and armour nodes therefore keep a maker-and-smith tab (way in), not a scene-first page. The harvest shows no scene structure.

View:
1. Ten display groups (Firearms … Parts, optics & fittings), with the "What is it for?" use view beside them.
2. Each group's leaves, for example Swords → Straight double-edged · Single-edged · Thrusting. Knives & daggers and Self-defence go straight to kinds.
3. Kinds, for example Single-edged → Sabre · Falchion · Cutlass · Katana … Below that come named forms. Where makers are the way in, a Makers & smiths tab sits beside the kinds, with the school table for nihonto.

## Rules applied
C2(a)(b)(d), C3, C10(b), C11, C14(b), C15, S3, K-83 to K-88, K-163, R-16a, E-4, E-21, CV-19, R-19, R-58, §14 E4-1 to E4-8.

## Provisional or † items
- Multi-pump air rifles stay an attribute until a C10(b) comparison source ranks them separately; this rests on the memo's † attestation item.
- The kind level of the regional-word kinds (kama, sai, fuchi-kashira, kozuka/kogai) is provisional under R-19 and CV-27.
- E4.9 now holds 14 kinds, more than the "about 12" of C5(b). The next tree build should add a reloading leaf by role (E4.9.10–14), keeping the ids.
- New kinds are attested in an HV_NK batch.
