# DPW1_C5 report: Office & Stationery decision pass (wave 3, offline)

Inputs: the HV_C5_1 and HV_C5_2 "missing kind?" lists (split into single items) and shop categories from the fetch logs. No DPMK_1_C5 file exists. All 88 tree kinds are in data, so new ids take the next free number (R-58).

## Task 1: 45 candidates (DPW1_C5_kinds.tsv)
16 new kinds, 14 covered, 6 attributes, 9 other categories, 0 named forms.

- **New kinds:**
  - C5.1.5.03 Lead holder; C5.2.3.09 Index card; C5.3.1.06 Desk organiser
  - C5.3.2.03 Clipboard; C5.3.2.04 Chalkboard
  - C5.3.4.07 Treasury tag; .08 Paper fastener; .09 Rubber band; .10 Office magnet
  - C5.3.5.04 Folder; .05 Punched pocket
- **New leaf C5.5.8 For office machines** (axis: object served, as for C5.5.7): .01 Laminating pouch; .02 Binding comb or spine; .03 Binding cover; .04 Shredder bag; .05 Calculator ink roller.
- **Other categories:**
  - stylus → D2 (R-30); postcard → F5
  - sketchbook, origami paper, comic pens → C4
  - key tag → A4; staple gun → C1; bookends → B1
  - dictaphone → E3.3.2.04

## Task 2: 8 named forms flagged (DPW1_C5_moves.tsv)
- **move_kind 2:** POSCA and OHTO Graphic Liner go to C4.1.1.10. Their own rows say paint marker and drawing pen (K-170).
- **to_line 5:** Maruman Mnemosyne (onto its existing line), Sunny Light, Fisher Space Pen, Faber-Castell Textliner, Bungubox Original.
- **drop 1:** Eboya Ebonite (maker name plus a material).

## Task 3: navigation
R-116 is confirmed: type first, house as the second door. Every fetched shop opens on the instrument or paper type. In the harvest, 365 named forms come from 147 makers. A house leads only in fountain pens (Parker has 12 of 70), which is already a way-in scope.

First three levels:
1. The eight display groups. The new kinds join by leaf; C5.5.8 goes under Calculators and office machines.
2. Kinds, for example Pens → fountain, dip, ballpoint, gel, rollerball …
3. For way-in kinds, houses then their models (Fountain pen → Parker → 51, Duofold). For owner kinds, models with maker and price band (Gel pen → Pilot G2, Signo UM-151).

A tab of pen and paper houses sits alongside.

## Rules applied
C2(a), C2(b), C2(d), C3, C12, S3, K-170, P4, P5, R-58, R-70(a), R-116, and the tree's attribute list.

## Notes
- No decision rests on a † claim.
- **Dictaphone** is the weakest call: the key names no dictation recorder.
- **Judgment calls:** laminating sheets go under the pouch kind, and foldback clips under bulldog clip.
- **Duplicate lines need a merge outside this file:** L-hobonichi-techo and L-hobonichi-hobonichi-techo; L-uni-jetstream, L-uni-ball-one and L-uni-ball-zento and their L-mitsubishi-pencil-… twins.
- **Lead holder will not load directly:** HV_C5_1 logs its status as "full (Parallel)", and apply_dp.py only matches exact "full" or "partial". So C5.1.5.03 goes to the worklist. The other 15 cite pages logged plainly in HV_C5_2.
- The source URLs are the harvesters'. I did not check them offline.
