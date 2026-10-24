# DPW1_J6 report (J6 Coffee, Tea & Cocoa; offline Opus pass, wave 3)

## Task 1: 12 candidates (verify/out/DPW1_J6_kinds.tsv)
covered 5, attribute 4, named_form 2, other_category 1, new_kind 0.

- The 14 HV_J6_2 items (honeybush, guayusa, lemongrass and the rest) were already decided in DPMK_1_J6. They are skipped: 12 of them are now kinds J6.4.1.05–13 and J6.4.2.05–07.
- From HV_J6_1:
  - Dried cacao pod (husk tea) and cacao tea bags are covered by J6.3.03.
  - Coated nibs are confectionery, so OUT.
- From the "gave" column of the fetch logs:
  - Covered: ceremonial cacao (J6.3.04), flavoured rooibos (J6.4.1.03, K-46), herbal chai (J6.4.0.01).
  - Attributes: black cocoa, deodorised cocoa butter, roasted yerba mate, con palo or despalada.
  - Named forms of yerba mate J6.4.1.04: chimarrão (memo §7) and barbacuá.
- Tea capsules, instant tea and tea concentrate were not seen. J-14 stays open and they get no id.

## Task 2: 2 of 76 named forms flagged (verify/out/DPW1_J6_moves.tsv)
- **move_kind:** NF-J6.2.2.01-004 Iribancha/Kyobancha goes to Roasted green tea J6.2.2.04. "Iri" means roasted; this is roasted bancha.
- **drop:** NF-J6.3.07-004 Van Houten Chocolate Drink. The fetched page lists sugar first, which makes it a sugar-led mix and OUT (K-49).
- **to_line:** none. Every maker-bound row (Ippodo, Rishi, Summit, Tee Gschwendner, Taragui, Kawahara Seifun, Westrock, Van Houten, Ghirardelli, Guittard, Cadbury, Domori) is a single branded product inside one kind. The maker role is none, so branded products are allowed.
- **Makers or shops filed as named forms:** none found.

Not flagged, but needing follow-up:
- **Cadbury Drinking Chocolate and Ghirardelli Double Chocolate Hot Cocoa** may also be sugar-led (†, from my own knowledge). Before either is dropped, a fetched ingredient list is needed.
- **Café de Colombia, Jamaica Blue Mountain and Kona** cover green and roasted coffee. When designations are harvested, each becomes a designation row with binds = tag (JC1). The roasted named forms stay meanwhile.
- **Kenya AA:** the "AA" is a grade attribute, but the row is kept as the origin's trade name.

## Task 3: navigation, confirming R-116
The way in is by type of object (plant, then the form or tea type as sold), then what makes the best, then who vouches, then the named best. The harvested data supports this:
- 49 of the 76 named forms are teas named by type and origin. The CNPP "ten famous teas" and the Tao Tea Leaf menu (white, green, yellow, oolong, pu-erh, scented, blooming, chai, mate, rooibos, herbal) both run plant first, then processing.
- Coffee forms are origins and grades (Blue Mountain grades, Kona grades, Kenya AA, Excelso).
- Shop menus are split by format (beans, capsules, instant, green).
- Makers show up only as single branded products, so there is no case for opening by brand. No scenes are tagged, so there is no case for opening by scene.

One display fix is needed: the 12 DPMK_1 kinds go into groups. J6.4.1.05–13 go to G-J6-23, and J6.4.2.05–07 to G-J6-24 (tools/apply_groups_changes.py).

View sketch:
1. Coffee · Tea · Cocoa & drinking chocolate · Herbal & other infusions.
2. Display groups:
   - Coffee: beans and ground, capsules and pods (by machine system), instant and concentrate, green for home roasting.
   - Tea: white, green and matcha, yellow, oolong, black, pu-erh and dark, flavoured and chai.
   - Cocoa: powder and drinking chocolate; beans, nibs, paste and butter.
   - Infusions: leaves (rooibos, mate, mint, nettle and others), flowers, fruit, roots and grains, blends.
3. The kind, with its quality ladder and named best:
   - Roasted coffee by SCA score and traceability, then origins.
   - Pan-fired green tea by season, then Longjing and Bi Luo Chun.
   - Black tea by flush and grade, then Darjeeling and Assam.

Filters: roast, process, flush, certification, decaf. Origin is a filter only, never a level.

## Rules applied
C2(b), C3, C13, JC1, JC4, J-14, K-46, K-49, R-35, R-58, R-115 b, R-116, memo §7 and §14, and the tree's precedence notes.

## Resting on † claims
- Iribancha being roasted, based on the meaning of the name; the harvested page does not state it.
- The sugar-first concern for Cadbury and Ghirardelli. These are not acted on.
- Barbacuá counting as a sold style name. The yerbatica types page lists it, but no shop page was checked.
