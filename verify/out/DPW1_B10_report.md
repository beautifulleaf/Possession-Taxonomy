# DPW1_B10: B10 Animal Equipment decision pass

## Task 1: missing kinds (41 items)
new_kind 28, covered 8, named_form 2, attribute 1, other_category 2.

New kinds (R-58 next free ids; new leaves also take the next free number):
- Dogs: B10.1.4.04 muzzle; B10.1.7.01 waste bag (new leaf Care and hygiene).
- Cats: B10.2.2.02 scratcher.
- Horses: B10.4.1.04 Australian stock saddle; .05 pack saddle; B10.4.2.06 martingale; .07 lunge line; B10.4.3.05 cooler rug; .06 fly rug; .07 overreach boot; B10.4.4.02 curry comb.
- Fish: B10.5.3.08 air pump; B10.5.5.02 water treatment.
- Cage birds (new leaves): B10.7.1.01 feeder or drinker; B10.7.2.01 cage; B10.7.2.02 nest box; B10.7.3.01 perch; B10.7.4.01 toy.
- Wild birds: B10.8.2.08 hummingbird feeder.
- Bees: B10.9.5.01 varroa treatment (new leaf Health and veterinary).
- Poultry: B10.10.4.02 brooder heating plate.
- Several animals: B10.11.2.02 water fountain; .03 automatic feeder; B10.11.3.03 pet door or cat flap.
- Parts: B10.12.1.03 queen excluder; .04 comb foundation; B10.12.2.02 stirrup; B10.12.4.01 feeder hook (new leaf Bird feeder).

Covered: bowls, carriers, pens, gates, parasite treatments, bird wormer, girths, feeder pole. Bee suit and veil go to A1 (K-105). Named forms: McClellan saddle, bird swing. Attribute: smart camera feeder.

## Task 2: named forms (18 of 386 flagged)
- **drop 9:** five hive systems (C13 platform values, as the memo decided); braided-leather and chain leads (material); rain sheet (fill weight); Exo Terra Heat Mat PTC (variant).
- **to_line 6:** KONG Squeezz; four Herm Sprenger bit lines; TetraMin (C2(e)).
- **move_kind 3:**
  - a Burgess timothy hay goes to hay B10.11.1.01 (possible duplicate);
  - two RSPB suet-pellet and peanut feeders go to peanut mesh feeder B10.8.2.05.
  - both lines then need the new kind in `kinds`.

## Task 3: navigation by shopper path
B10 is not scene-driven. Retailer trees in six regions open with the animal, then the need; AAFCO says choose by species first. Brands are pockets: 126 makers, five of them hold 74 of the 294 maker-bound forms, and accessories and wild-bird gear have scattered makers. Disciplines and water type change kinds, not brands: filters and secondary tabs.

View:
1. **Which animal?** Ten groups. "Several animals" items show under each through `applies_to`.
2. **What do you need?** Feed, feeding, housing, habitat set-up, beds, saddlery, tack and walking, wear, care, health, toys and training, travel, ID.
3. **Which type?** Kinds, then named forms and makers, with fit filters (horse size, tank volume, hive system).

## Rules applied
R-58, K-102, rule 3.1, C2(b)(c)(e), R-35, R-70(a), C3, C5(d), C10, C11, C13, memo §4b, K-101, K-103, K-105, B-33.

## Unverified claims
- No URL in the report: cat flap and scratcher. Each needs a fetched page before loading.
- From memory, not a fetched page: KK Ultra spanning curb bits; TetraMin having several products; the McClellan filing (provisional).
- Rule T(b) needs a fetched comparison: water fountain; smart camera feeder (attribute until then).
- Gaps:
  - cage-bird food (not a candidate);
  - Arcadia LumenIZE, filed under UVB lamp, looks like a daylight lamp with no UVB. Check it.
