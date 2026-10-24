# DPW1_G1 report (G1 Vehicles, wave 3)

Inputs: HV_G1_1 (land) and HV_G1_2 (rail, water, air; it finished and was loaded during this pass, so both are used). Data: 134 kinds, 674 named forms, 17 lines. There is no DPMK_1_G1 file.

## Task 1: missing kinds (65 items, DPW1_G1_kinds.tsv)
covered 32, attribute 14, new_kind 11, named_form 5, other_category 3 (park model to G2, balance bike to E1, paddleboard to E2).

New kinds (next free number per R-58):
- G1.1.6.07 Recumbent tricycle
- G1.1.6.08 Trailer bike (trailercycle)
- G1.1.8.11 Teardrop trailer
- G1.1.10.06 Stroller wagon
- G1.3.1.06 River raft
- G1.3.3.15 Performance powerboat
- G1.3.3.16 Bass boat
- G1.3.3.17 Ski and wakeboard boat
- G1.3.3.18 Deck boat
- G1.3.3.19 Flats and bay boat
- G1.4.2.10 Paramotor

source_url is the URL the harvester logged. For teardrop, stroller wagon, raft, flats boat and paramotor, that page's "gave" summary does not name the type, so HV_NK must confirm these five. The light-sport airplane is covered: it is a C17 class, and Controller's LSA list mixes several designs (section 14).

## Task 2: named forms (60 moves, DPW1_G1_moves.tsv)
- **to_line 28.** 26 caravan, campervan and motorhome ranges (G2-O1, memo section 6) from Swift, Bailey, Elddis, Adria, Forest River, Keystone, Jayco, Grand Design and Palomino. Layout-level forms stay named forms (Rimor Sarus, Voyager 494). Also Ifor Williams General Duty and Topper Topaz.
- **drop 7.** "Tipper" restates the kind. Kosmic is a brand. Diablo Bamboo is a material variant. E-Bullitt and e-Priam are assist variants. Two duplicate Burley trailer-strollers are dropped, since each product has one home.
- **move_kind 25.** 12 recumbent trikes to G1.1.6.07 (pending its attestation). 7 landplanes on optional floats to single-engine piston (C12). Dart 18 and Sprint 15 to beach catamaran. Marco Polo to campervan, 9-seat Trafic to window van (P15), Transporter to panel van, SuperSport 950 to sport.
- **Kept.** Snowmobile and RZR families stay named forms: they are model lines and their packages are trims (G1-O1).

## Task 3: navigation
R-116 is confirmed: type first, then make and model. Every harvested shop opens on type (Controller by engine class, boats.com by vessel type, Canyon by discipline). Makes appear only as owners of models (role: owner). One display-only tweak, no id change: a "Mountain bikes" heading over the five MTB kinds, and motor craft ordered by use.

First three levels:
1. 11 groups: Cars; Vans, trucks and buses; Motorcycles and powered light rides; Bicycles and other cycles; Off-road, snow and utility; Caravans, motorhomes and trailers; Boats; Aircraft; Rail and horse-drawn; Prams and strollers; Parts.
2. Kinds by each leaf's axis (Bicycles: road, gravel, mountain, BMX, city..., with an e-bike shortcut).
3. Models with a make tab (Jet: Cessna Citation CJ4, Gulfstream G650, Dassault Falcon 7X).

## Rules applied
C2, C3, C6, C11, C12, C17, P1, P3, P4, P13, P15, G-5, G-8, G1-O1, G2-O1, R-58, R-116.

## Claims marked †
No decision rests on a † claim. One call is weak: lifeboat as covered by the tender.
