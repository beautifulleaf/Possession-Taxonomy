# DPMK_1 report: "missing kind?" decision pass

Outputs: verify/out/DPMK_1_kinds.tsv (359 rows), DPMK_1_moves.tsv (18). Generator: verify/work/DPMK_1/build.py. Ids are next free per parent (R-58), checked against every id in data/, verify/out/, memos and audit/ (pending DPW1 and DS ids included).

## Counts (new_kind / named_form / attribute / covered / other_category)
- A5 1/0/5/6/0 · B3 1/0/0/1/2 · B10 6/5/0/7/0 · C6 1/1/1/4/2 · D5 2/1/0/10/0 · E3 4/0/0/4/2 · I1 2/0/0/9/1
- J1 31/8/2/4/0 · J2 51/2/1/62/2 · J4 16/2/0/1/0 · J5 42/3/2/4/0 · J6 12/0/0/2/0 · J7 12/3/3/16/0
- Total: 181 new kinds, 25 named forms, 14 attributes, 130 covered, 9 other category. H1: no missing kind found in the reports.

## New kinds
- B10.4.2.09 Gag bit; B10.2.2.03 Wall-mounted cat furniture; B10.2.3.02 Self-cleaning litter box; B10.2.3.03 Litter disposal pail; B10.8.2.09 Platform feeder; B10.9.3.06 Frame grip.
- B3.2.1.05 Monitor light bar. C6.5.1.16 Focus motor. D5.5.23 Flash cartridge; D5.2.3.09 Flight-sim control panel. I1.4.3.06 Music notation software; I1.3.14 Online whiteboard.
- E3.3.2.03 Microphone preamp and channel strip; E3.3.2.04 Portable audio recorder; E3.3.2.05 500-series module; E3.3.7.05 DAW control surface. A5.1.6.03 Sonnerie watch.
- J2: J2.1.1.56–.99 (44 finfish species or genus groups, from pink salmon, albacore, skipjack and bigeye to snoek and blue cod; names in the tsv); J2.1.2.14–.19 (pink, Crangon brown, Gulf brown, blue, royal red shrimp; squat lobster); J2.1.3.17 Conch.
- J4: J4.2.3.16–.20 parsnip, swede, celeriac, Jerusalem artichoke, salsify; J4.2.1.11 chard, .12 mizuna; J4.2.2.07–.09 pak choi, komatsuna, Chinese cabbage; J4.2.4.09 Welsh onion; J4.1.4.09–.11 gooseberry, redcurrant, elderberry; J4.1.1.06 quince; J4.2.6.05 broad bean.
- J7: J7.1.1.13 Cabernet Franc, .14 Carmenere; J7.1.2.08 Gruner Veltliner, .09 Semillon; J7.1.8.04 Aromatised wine-based drink; J7.2.2.02 Munich Dunkel, .03 Schwarzbier; J7.2.6.02 Dunkles Bock; J7.2.7.03 Kolsch; J7.4.09 Sparkling sake; J7.5.1.10 Canadian whisky, .11 Wheat whiskey.
- J1: beef J1.1.1.17–.26 (flank, hanger, tri-tip, rib roast, eye of round, top round, oxtail, liver, heart, kidney); veal J1.1.2.02–.03; pork J1.1.3.12–.15 (shoulder, loin joint, leg, stomach); lamb J1.1.4.05–.07; J1.1.6.04 chicken wings; J1.1.8.04–.05 duck leg, goose; J1.1.9.03–.07 quail, guinea fowl, grouse, wood pigeon, wild duck; J1.1.14.05 squirrel; J1.2.1.09 Gammon; J1.2.2.04 Cooked cured tongue; J1.3.4.02 Blood sausage.
- J5: grains J5.1.2.05–.08, J5.1.3.01 rolled oats, flours J5.1.4.10–.14; pulses J5.3.1.06–.10, J5.3.3.01, J5.3.4.03–.05; nuts J5.4.1.07–.10, J5.4.4.02; J5.5.3.09 distilled vinegar; salts J5.6.4.05–.07; J5.6.3.02 jal-jeera masala; sugars J5.7.1.04–.06, syrups J5.7.3.01–.02; table sauces J5.9.4.08–.13; pastes J5.9.6.01–.02.
- J6: J6.4.1.05–.13 (honeybush, guayusa, lemongrass, spearmint, mountain tea, nettle, birch, marjoram, kuding); J6.4.2.05–.07 (yarrow, calendula, chrysanthemum).
- 150 new kinds carry a harvester URL; the 31 without one go to HV_<CODE>_NK.

## Moves
- C6.5.2.04 objective series: 13 to_line (Evident UPLSAPO, PLAPON, UAPON, LUCPLFLN, UPLFLN; Zeiss A-Plan, ACHROPLAN, FLUAR, EC and LCI Plan-Neofluar, C-Apochromat; Leica HC and HCX PL APO); Plan-Apochromat dropped (generic class, objective_class attribute).
- FocusCube v3, SESTO SENSO 3 and ZWO EAF move to C6.5.1.16. FIB-SEM stays C6.1.5.06 (column_type attribute, no kind).
- Ring Floodlight Cam (NF-B3.1.4.05-K1015) moves to B8.1.6.3 Floodlight camera (tree id).

## Rules applied and flags
- J2 finfish = species (memo 4b), molluscs = animal type, crustaceans = commercial species. Minor taxa are grouped where a genus kind exists (dab, plaice relatives under flounder; brill under turbot; small tunas; Seriola). **J2.1.1 now ends at .99**: any further finfish needs a decision on three-digit ids or a leaf split (owner queue).
- J4 species test; greengage and damson are plum varieties. J1 J-1/J-3 (retail cut, organ per animal, species x joint). J7 J-16 grape kinds; age and origin are attributes.
- Other category: weapon light E4; video magnifiers H2 (K-38); robot kits E1 (K-149); smartwatch D2; console software I1; SCADAS C6; krill H2; seaweed J4.
- No decision rests on a † claim beyond the 31 unattested new kinds.
