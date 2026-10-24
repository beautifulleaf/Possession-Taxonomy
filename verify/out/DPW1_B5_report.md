# DPW1_B5 report (B5 Kitchen & Dining, wave 3, offline)

Inputs: HV_B5_1 and HV_B5_2 "missing kind?" lists (split into 17 items), plus 13 generic types taken from the "gave" column of the fetch logs and the harvested rows. There is no DPMK_1_B5 file. Files: verify/out/DPW1_B5_kinds.tsv and DPW1_B5_moves.tsv.

## Task 1: 30 candidates
new_kind 12; named_form 8; covered 7; attribute 3; other_category 0.

New kinds. Each takes the next free number under its parent (R-58; checked against data/kinds.tsv and TREE_B5_map.tsv):
- B5.1.2.05 Steamer
- B5.1.4.08 Countertop oven [toaster oven]
- B5.1.4.09 Deep fryer
- B5.1.4.10 Microwave oven (source_url empty)
- B5.2.3.05 Kitchen shears
- B5.2.3.06 Ladle
- B5.2.3.07 Cooking spoon
- B5.2.5.03 Blender (source_url empty)
- B5.5.1.07 French press [cafetiere]
- B5.7.01 Portafilter
- B5.7.02 Coffee machine water tank
- B5.7.03 Blender jar or lid

These are the first kinds in the parts sub-family B5.7, which therefore stays.

Named forms:
- tava under B5.1.1.03
- kadhai ("deep fry pan") under B5.1.1.02
- handi under B5.1.2.03
- pasta cooker under B5.1.2.02
- shotoh under B5.2.1.04
- takobiki under B5.2.1.11
- oroshigane under B5.2.3.01
- French-door refrigerator under B5.3.01

Covered:
- multi-cooker and sauce pot: B5.1.2.02
- casserole dish: B5.1.2.03
- honing steel: B5.2.2.02
- turner: B5.2.3.03
- IH cooktop: B5.1.4.04
- Japanese hot plate (an electric griddle, so power source is a tag): B5.1.1.03

Attributes:
- combi oven: steam is a technology on the oven (rule T)
- domino hob: width and module format (C6)
- cast-iron teapot: material (B-21)

## Task 2: 8 named-form flags
- **to_line (7):**
  - Philips Series 3200 LatteGo
  - Zwilling Miyabi 6000MCT
  - Eden Classic Damast (line already stored)
  - U-Line 5 Class
  - Zephyr Presrv
  - KINTO CAST
  - Orphan Espresso LIDO

  Each is a maker's tier or range that covers several models or kinds (C1, C2(d), R-70 a). The models inside them are still to be harvested.
- **drop (1):** Muvna "Lever Coffee Machine". The name is just the kind's name.
- **Kept:** the Hawkins pressure-cooker designs stay named forms. Their sizes, coatings and finishes are variants (C3).
- Under the owner maker role, no row is a maker or a shop.

## Task 3: navigation
**Confirmed: R-116 "type of object", opening on shop families.** The harvest supports it:
- The 61 fetch-log rows that returned something are almost all shop category pages for a product type (IKEA, Tramontina, Kakaku, Siemens hobs, Breville ovens, Riedel and Zalto glasses).
- The 157 named forms spread across about 70 makers, and no maker dominates more than one family.
- No scene vocabulary turned up.
- Maker depth appears only in knives, cast iron, espresso and stemware. That fits the owner maker role, with a Makers & lines side view.

View sketch, first three levels:
1. **What are you buying?** Twelve groups (proposals.tsv): Cookware & bakeware; Knives & cutting; Kitchen tools & measuring; Cooking & food appliances; Fridges & dishwashers; Coffee, tea & water; Bar & home brewing; Tableware & serveware; Glasses, cups & mugs; Food storage & on-the-go; Aprons, gloves & clean-up; Replacement parts.
2. **Which family?** The memo leaf, for example Pans, Pots, Ovenware.
3. **Which type?** The kind, for example Frying pan, Wok, Saute pan, Steamer. Each kind has a "What makes the best" box: material and construction, then hob compatibility; for knives, pattern then steel and HRC.

The new kinds join these groups:
- countertop oven, deep fryer, microwave, blender: Cooking & food appliances
- steamer: Cookware
- shears, ladle, cooking spoon: Kitchen tools
- French press: Coffee, tea & water
- B5.7 kinds: Replacement parts

## Rules applied
C2(a)/(b)/(d), C3, C6, C10 (rule T), C11 (rule R), C12 (rule M, countertop oven), S3/CV-17 (parts), K-171 (shears), B-21, R-58, R-70 a, R-116, R-118 a.

## Weak points and † claims
- **Microwave oven and blender:** these rest on my reading of the harvester's English labels for Kakaku categories ("range" read as レンジ, "mixer" as ミキサー). Kakaku is a partial navigation page, so source_url is left empty and both go to HV_NK for attestation.
- **Kitchen shears (K-171 †):** the Victorinox set page is the source, but the logged "gave" column does not name the shears, so HV_NK should confirm.
- **Steamer:** the logged Tramontina page is unconfirmed for this item, and the OXO page that shows "Steamers" was nav-only. Confirm in HV_NK.
- **Espresso operating modes († risk in the memo):** EspressoSpecDB and the lever shops sell the modes separately, so they stay three kinds.
- **Decanter:** still rests on a page that calls it a carafe (partial).
- **Open gap, no id given:** an open ceramic or glass baking dish. Look for it in the next harvest (R-96 c).
- **Unchecked from the logs:** three of the line moves rest on what I know about those makers' ranges rather than on what the logged pages show: Miyabi 6000MCT, KINTO CAST and LIDO. The Philips, Eden, U-Line and Zephyr moves rest on the harvesters' own notes or on lines already stored.
