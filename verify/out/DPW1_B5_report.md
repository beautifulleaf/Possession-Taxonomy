# DPW1_B5 report (B5 Kitchen & Dining, wave 3, offline)

Inputs: 17 "missing kind?" items from HV_B5_1 and HV_B5_2, plus 13 generic types from the fetch logs' "gave" column. There is no DPMK_1_B5 file. Outputs: verify/out/DPW1_B5_kinds.tsv and DPW1_B5_moves.tsv.

## Task 1: 30 candidates
new_kind 12, named_form 8, covered 7, attribute 3, other_category 0.

**New kinds** (next free ids, R-58):
- B5.1.2.05 Steamer
- B5.1.4.08 Countertop oven
- B5.1.4.09 Deep fryer
- B5.1.4.10 Microwave oven (no source yet)
- B5.2.3.05 Kitchen shears
- B5.2.3.06 Ladle
- B5.2.3.07 Cooking spoon
- B5.2.5.03 Blender (no source yet)
- B5.5.1.07 French press
- B5.7.01 Portafilter
- B5.7.02 Coffee machine water tank
- B5.7.03 Blender jar or lid

**Named forms:** tava, kadhai, handi, pasta cooker, shotoh, takobiki, oroshigane, French-door refrigerator.

**Covered:** multi-cooker, sauce pot, casserole dish, honing steel, turner, IH cooktop, hot plate.

**Attributes:** combi oven, domino hob, cast-iron teapot.

## Task 2: 8 named-form flags
- **to_line (7):** Philips Series 3200 LatteGo, Miyabi 6000MCT, Eden Classic Damast, U-Line 5 Class, Zephyr Presrv, KINTO CAST, LIDO. Each is a range covering several models or kinds.
- **drop (1):** Muvna "Lever Coffee Machine", which is only the kind's name.
- Hawkins pressure-cooker designs stay named forms; their sizes and coatings are variants.

## Task 3: navigation
**Confirmed: type of object, opening on shop families (R-116).**
- The 76 full or partial fetches are mostly shop pages for one product type.
- The 157 named forms spread over 65 makers.
- No scene vocabulary turned up.
- Makers matter only for knives, cast iron, espresso and stemware, so they get a side view, not the way in.

**First three levels:**
1. **Groups:** Cookware & bakeware; Knives & cutting; Kitchen tools & measuring; Cooking & food appliances; Fridges & dishwashers; Coffee, tea & water; Bar & home brewing; Tableware & serveware; Glasses, cups & mugs; Food storage & on-the-go; Aprons, gloves & clean-up; Replacement parts.
2. **Memo leaf**, for example Pans or Pots.
3. **Kind**, for example Frying pan, Saute pan or Steamer, each with a "What makes the best" box.

The new kinds go into their matching groups (appliances, cookware, kitchen tools, coffee, replacement parts).

## Rules applied
C2(a)/(b)/(d), C3, C6, rule T, rule R, rule M, S3/CV-17, K-171, B-21, R-58, R-70 a, R-116.

## Weak points and † claims
- **Microwave and blender:** these rest on my reading of the harvester's labels "range" and "mixer" on Kakaku's partial navigation page. source_url is empty and both go to HV_NK.
- **Kitchen shears (K-171 †) and steamer:** their logged pages do not clearly show the item. Confirm in HV_NK.
- **Espresso modes:** shops sell them separately, so they stay three kinds.
- **Decanter:** still rests on a "carafe" page.
- **Gap, no id given:** an open baking dish. Look for it in the next harvest (R-96 c).
- **Unchecked:** the 6000MCT, CAST and LIDO line moves rest on what I know about those makers' ranges, not on the logged pages.
