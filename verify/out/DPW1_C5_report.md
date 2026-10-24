# DPW1_C5 report: Office & Stationery decision pass (wave 3, offline)

Inputs: HV_C5_1 and HV_C5_2 "missing kind?" lists, split into single items, plus shop categories from the "gave" column of both fetch logs. There is no DPMK_1_C5 file. All 88 tree kinds are in data, so each new id is the next free number after the tree's ids (R-58).

## Task 1: 45 candidates (verify/out/DPW1_C5_kinds.tsv)
- 16 new kinds, 14 covered, 6 attributes, 9 other categories, 0 named forms.
- New kinds:
  - C5.1.5.03 Lead holder
  - C5.2.3.09 Index card
  - C5.3.1.06 Desk organiser
  - C5.3.2.03 Clipboard
  - C5.3.2.04 Chalkboard
  - C5.3.4.07 Treasury tag
  - C5.3.4.08 Paper fastener
  - C5.3.4.09 Rubber band
  - C5.3.4.10 Office magnet
  - C5.3.5.04 Folder
  - C5.3.5.05 Punched pocket
- New leaf C5.5.8 For office machines (axis: object served, as section 14 did for C5.5.7):
  - C5.5.8.01 Laminating pouch
  - C5.5.8.02 Binding comb or spine
  - C5.5.8.03 Binding cover
  - C5.5.8.04 Shredder bag
  - C5.5.8.05 Calculator ink roller
- Other categories:
  - stylus → D2 (step 24 note, R-30)
  - postcard → F5 (step 19)
  - sketchbook, origami paper, comic pens → C4
  - key tag → A4
  - staple gun → C1
  - bookends → B1
  - dictaphone → E3.3.2.04 (portable audio recorder)

## Task 2: 8 named forms flagged (verify/out/DPW1_C5_moves.tsv)
- **move_kind 2:** POSCA and OHTO Graphic Liner go to C4.1.1.10, because the rows themselves say paint marker and drawing pen (K-170).
- **to_line 5:**
  - Maruman Mnemosyne, onto its existing line
  - Sunny Light (the maker's name; the line covers notebooks and refills)
  - Fisher Space Pen
  - Faber-Castell Textliner
  - Bungubox Original (a shop's own-label range)
- **drop 1:** Eboya Ebonite (maker name plus a material).

## Task 3: navigation
The way in from R-116 is confirmed: type of object first, with the house as a second door. Every fetched shop (JetPens, Goulet, Cult Pens, Ryman, Officeworks, Staples) opens on the instrument or paper type. The harvest supports this:
- 365 named forms from 147 makers, and no house leads anywhere except fountain pens (Parker 12, Pilot 5, Sheaffer 4 of 70).
- The deep, house-driven sets (fountain pens, notebooks, planners) are exactly the way-in scope of maker_roles.tsv.

Sketch of the first three levels:
1. The eight display groups: Pens; Pencils, erasers and correction; Ink, refills and pen parts; Notebooks and journals; Diaries, planners and calendars; Paper, cards and post; Desk, filing and office supplies; Calculators and office machines. The new kinds join the groups by leaf; C5.5.8 joins Calculators and office machines.
2. Kinds in tree order. For example, Pens → fountain, dip, ballpoint, gel, rollerball, multi, fineliner, marker, highlighter, brush pen, calligraphy brush and ink.
3. Depends on the maker role:
   - **Way-in kinds** list houses, then their named forms (Fountain pen → Parker → 51, Vacumatic, Duofold; Notebook → Midori → MD Notebook).
   - **Owner kinds** list named forms with maker and price band (Gel pen → Pilot G2, Signo UM-151, Sarasa Nano).

A "Pen and paper houses" tab and the price-band view of fountain pens sit alongside, as R-116 proposed.

## Rules applied
C2(a), C2(b), C2(d), C3, C11, C12, S3, K-170, P4, P5, R-58, R-70(a), R-116, R-122(c), and the tree's attribute list (ink properties, nib shape, drive, size, `reusable`).

## Notes for the apply step
- **No † claims:** no decision here rests on one.
- **Dictaphone:** this is the weakest call. The key names no dictation recorder, so it should be reviewed against the key.
- **Calls a reviewer may question:** laminating sheets are put under the laminating pouch kind, and foldback clips under bulldog clip. These are judgment calls.
- **Duplicate lines need a merge:** L-hobonichi-techo and L-hobonichi-hobonichi-techo; L-uni-jetstream, L-uni-ball-one and L-uni-ball-zento against their L-mitsubishi-pencil-… twins. The moves file has no action for re-pointing line_id, so the merge has to be done separately.
- **Fetch status strings:** HV_C5_1 logs status as "full (Parallel)". tools/apply_dp.py only matches the exact words full or partial, so C5.1.5.03 (JetPens Pencils page, logged only by HV_C5_1) will go to the attestation worklist instead of loading. The other 15 cite pages that HV_C5_2 logged as plain full or partial.
- **Sources not checked:** source URLs are the ones the harvesters gave for each item. This pass was offline and did not check the page contents.
