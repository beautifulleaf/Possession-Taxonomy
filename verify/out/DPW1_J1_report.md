# DPW1_J1 report (J1 Meat & Poultry)

**Input.** All 44 harvest-report "missing kind?" items were already decided in DPMK_1, so they are skipped. Task 1 used 46 generic types from the fetch logs' "gave" column that the tree lacks.

**Counts (DPW1_J1_kinds.tsv).** new_kind 21, covered 14, named_form 5, attribute 4, other_category 2 (rillettes to J5, P8; pâté en croûte to Culinary, P1).

**New kinds.** Next free ids (R-58), checked against data, tree map and the reserved DPMK_1 ids.
- Pork: J1.1.3.16 Pork primal or side.
- Goat: J1.1.5.02 chops, .03 shank, .04 leg, .05 ground, .06 shaped raw mince.
- Duck: J1.1.8.06 Ground duck.
- Venison: J1.1.10.04 haunch, .05 fillet, .06 rack, .07 ground, .08 shaped raw mince.
- Rabbit: J1.1.11.03 saddle, .04 leg.
- Horse: J1.1.13.02 ribeye steak, .03 tenderloin, .04 sirloin steak, .05 flank steak, .06 ground.
- Sausages: J1.3.3.03 Smoked scalded sausage (kielbasa); J1.3.4.03 White pudding.

White pudding has no URL (the page shows only hogs pudding) and goes to HV_NK; the other 20 have logged full URLs.

**Moves (DPW1_J1_moves.tsv).** 6 drops, no to_line, no move_kind.
- Scotch Beef PGI, Agneau de Sisteron, Welsh Lamb: each spans several kinds, so it is a tag (JC1).
- Salt Marsh Lamb: a feeding attribute.
- Herdwick hogget: a breed (varieties table) plus an age attribute.
- Wiener: restates the kind name; Vienna sausage becomes an alias.

None is a maker or shop.

**Navigation.** The R-116 way in is confirmed: animal for fresh meat, product type for made meats. Fetched shops agree:
- Game shops and D'Artagnan list by species, then cut.
- farmfetch, Waitrose, Ditalia and Olympia split bacon, sausage, cured meat, ham, cooked meats and pâté, and fresh sausage from salami.

Proposed: G-J1-8 Sausages & salami gets level-2 groups (fresh sausages; salami and dry sausages; frankfurters, smoked and cooked sausages); every sausage shop fetched splits them. Ibérico stays a filter, not a group.

View sketch:
- **L1:** Beef & veal · Pork · Lamb & goat · Chicken · Turkey, duck & other poultry · Game & other meats · Ham, bacon & cured meats · Sausages & salami · Deli, cooked & tinned · Mixed meat boxes.
- **L2:** e.g. Beef: steaks / roasts and primals / slow-cook / mince / offal. Ham: dry-cured / bacon and pancetta / cooked ham / jerky and cured fat.
- **L3:** kinds, then named forms.

New kinds still need display groups (verify/work/DPW1_J1/group_adds.tsv); pork lacks an offal group.

**Rules applied.**
- J-1 and memo 4b: a named cut is a kind on one fetched page, including goat, venison, rabbit and horse. Mince and shaped mince are kinds per animal; J-3 makes primals kinds.
- C2(b), C3: portion, joint, breed and feeding are attributes. JC1: multi-kind designations are tags.
- C11, memo 4b: regional varieties and sub-cuts are named forms.
- Conflict: the addendum's "none"-role rule would bar cut names as named forms, but decided memo J-1 keeps them (tomahawk, NY strip). They are kept.
- Definition note: Salt beef (silverside) sits under "Corned beef brisket" (definition should allow other cuts).

**† claims.** None.
