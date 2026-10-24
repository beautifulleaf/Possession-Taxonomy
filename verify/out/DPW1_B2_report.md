# DPW1_B2 report: B2 Soft Furnishings (wave 3, offline)

**Inputs:** HV_B2_1 report (7 "missing kind?" items, split into 11), the gave column of verify/work/HV_B2_1/fetched.tsv (17 more shop types), 66 kinds, 94 named forms. No DPMK_1_B2 file, no lines rows, no B2 rows in groups.tsv.

## Task 1: 28 candidates (DPW1_B2_kinds.tsv)
- **new_kind 6:** B2.1.1.05 Pillow protector (IKEA QA); B2.1.1.06 Bed frame or headboard cover (IKEA QA, weak: page says "bed covers"); B2.3.2.08 Tie-up shade (roll-up shade) (Wayfair guide); B2.4.08 Cushion pad (insert) (Dunelm); B2.7.05 Curtain tieback or holdback; B2.7.06 Curtain pole bracket or finial (both Dunelm fixtures page). Each is the next free number under its parent (data/kinds.tsv and TREE_B2_map.tsv agree; nothing reused). All need attestation in HV_NK. B2.7 grows to 6 kinds, still no leaf.
- **covered 10:** holdback, bracket (the new kinds); body or pregnancy pillow → B2.1.3.03 (definition should add full-length, U and C pillows of any fill); anti-fatigue or standing-desk mat → B2.2.2.03 (definition should add the standing desk); bath mat, seat pad, bed skirt, gym towel, face towel, track gliders.
- **attribute 6:** mini blind (slat width), rug runner (shape), silk (material), nomad (weaving_environment), hand-loomed (process), duvet cover set (unit of sale, K-1).
- **named_form 3** under B2.2.1.01: Ziegler, Berber, Patchwork (rug-wiki).
- **other_category 3:** swaddle or sleep sack A1 (wearable); coaster B5; fitness or yoga mat E2.
- Not attested and still open: B2.1.2.08 Kotatsu cover (HV_B2_1 found no product page).

## Task 2: 13 moves (DPW1_B2_moves.tsv)
- **drop 12:** six electric-blanket titles that only describe the product (Standard, Premium, Fully Fitted, Washable, Checkered Plush, Electric Heated Throw); the Delta "Pregnancy Support Wedge Pillow" (restates the kind and the user); Wellness Mats Granite, Linen, Bella, Trellis (surface patterns; they could come back as print variants of "Original", which is kept); IKEA FANTASTISK (a paper napkin, not cloth).
- **to_line 1:** IKEA VIDGA → L-ikea-vidga (track system, kinds B2.7.02;B2.7.03).
- **Kept:** the Persian and Turkish city, village and tribal names under knotted-pile rug, because memo §14 stores weaving_environment on rug named forms. Also kept: Forbo needlefelt ranges, Sunbeam models, Monastery Store zafu and zabuton (Cloud and Mountain Seat each span two kinds, so line rows could be added later) and the IKEA covers.

## Task 3: navigation
R-116 is **confirmed**: the main way in is the type of object, with the owner maker role. Every fetched retailer tree (IKEA US, SG, QA, OM, GB; Dunelm; John Lewis; THE ICONIC) opens on item type inside one textiles department. Named forms are mostly IKEA own-label, and 11 of the 13 makers are owner-only. Only handmade rugs are sought by tradition, and that is the existing side view.

Sketch:
1. **Bed linen & bedding** > bed linen (sheet, pillowcase, pillow protector, duvet cover, valance, bed frame cover), duvets and bed covers, pillows, mattress covers.
2. **Blankets & throws** > blanket or throw, electric blanket.
3. **Rugs & mats** > handmade rugs (knotted pile, flatweave, hooked), machine-made rugs and carpet (woven pile, tufted, needlepunched), hide, felt and rag rugs; mats.
4. **Curtains & blinds** > curtains (curtain, sheer, studio backdrop), blinds and shades (roller through tie-up).
5. **Cushions & seat covers** > cushions (scatter, cushion pad, chair pad, floor, meditation), covers (cushion, sofa, chair).
6. **Table & kitchen linen** > the five kinds.
7. **Towels & bath** > towels, bath mat, shower curtain.
8. **Curtain & rug fittings** > curtain fittings (pole, track, rings and hooks, tieback, pole bracket or finial), rug pad.

Level 3 is the quality filter for each group (fibre and weave; fill, fill power and tog; knot density, weave tradition and environment; EN 1307 class; lining and opacity). Rug side view: weaving environment > named weave > workshop.

## Rules applied
C2(a), C2(b), C2(d), C3, C11, S3 and CV-17 (B2.7), B2-O1 (furniture covers), K-1, B-15, R-58, R-116, memo §14.

## † and weak calls
- The FANTASTISK paper-napkin call and the reading of the four Wellness Mats names as patterns rest on Claude's knowledge, not on a fetched page. Recheck both.
- The material of the other IKEA placemats and napkins was not checked. Some may be paper or hard (B5).
- The bed frame cover rests on IKEA's "bed covers" label. The body pillow alias is † in the memo.
