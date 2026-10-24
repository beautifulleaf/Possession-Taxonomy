# DPW1_J1 report (J1 Meat & Poultry)

**Input.** All 44 "missing kind?" items in HV_J1_1 and HV_J1_2 were already decided in DPMK_1_J1_kinds.tsv and are skipped. Task 1 used the 46 generic types in the fetch logs' "gave" column that the tree lacks.

**Counts (DPW1_J1_kinds.tsv).** new_kind 21, covered 14, named_form 5, attribute 4, other_category 2 (rillettes to J5, P8; pâté en croûte to Culinary, P1).

**New kinds.** Ids are the next free numbers per R-58, checked against data/kinds.tsv, the tree map and the reserved DPMK_1 ids.
- Pork: J1.1.3.16 Pork primal or side.
- Goat: J1.1.5.02 chops, .03 shank, .04 leg, .05 ground, .06 shaped raw mince.
- Duck: J1.1.8.06 Ground duck.
- Venison: J1.1.10.04 haunch, .05 fillet, .06 rack, .07 ground, .08 shaped raw mince.
- Rabbit: J1.1.11.03 saddle, .04 leg.
- Horse: J1.1.13.02 ribeye steak, .03 tenderloin, .04 sirloin steak, .05 flank steak, .06 ground.
- Sausages: J1.3.3.03 Smoked scalded sausage (kielbasa); J1.3.4.03 White pudding.

White pudding has no URL (the page shows only hogs pudding), so it goes to HV_NK. The other 20 have a URL the harvester logged as full.

**Moves (DPW1_J1_moves.tsv).** 6 drops, no to_line, no move_kind.
- Scotch Beef PGI, Agneau de Sisteron, Welsh Lamb: each spans several kinds, so it is a tag (JC1).
- Salt Marsh Lamb: a feeding attribute.
- Herdwick hogget: a breed (varieties table) plus an age attribute.
- Wiener: restates the kind name; Vienna sausage becomes an alias.

No named form is a maker or shop.

**Navigation.** The R-116 way in is confirmed: animal for fresh meat, product type for made meats. The shops fetched group the same way:
- Swaledale, Salter & King, Fine Food Specialist and D'Artagnan list by species, then cut.
- farmfetch has separate bacon, sausage, cured-meat, ham-and-gammon and pâté collections.
- Waitrose, Ditalia and Olympia split cooked meats from pâté, and fresh sausage from salami.

Proposed change: G-J1-8 Sausages & salami gets level-2 groups (fresh sausages; salami and dry sausages; frankfurters, smoked and cooked sausages), because every sausage shop fetched splits them this way. Ibérico stays a filter, not a group.

View sketch:
- **L1:** Beef & veal · Pork · Lamb & goat · Chicken · Turkey, duck & other poultry · Game & other meats · Ham, bacon & cured meats · Sausages & salami · Deli, cooked & tinned · Mixed meat boxes.
- **L2:** e.g. Beef: steaks / roasting joints and primals / slow-cook / mince and burgers / offal. Ham: dry-cured ham and pieces / bacon and pancetta / cooked ham, pastrami and corned beef / jerky, cured fat and pickled.
- **L3:** kinds, each with "what makes the best" (grade, breed, feeding, ageing) and "who vouches" (USDA, JMGA/BMS, PDOs), then the named forms.

The kinds new since DPMK_1 still need display groups (verify/work/DPW1_J1/group_adds.tsv). Pork lacks an offal group.

**Rules applied.**
- J-1 and memo 4b: a named cut is a kind on one fetched page, including goat, venison, rabbit and horse. Mince and shaped mince are kinds per animal; J-3 makes primals kinds.
- C2(b), C3: portion, joint, breed and feeding are attributes. JC1: multi-kind designations are tags.
- C11 and memo 4b: regional varieties and sub-cuts are named forms. P1, P8 and R-58 also applied.
- Conflict: the addendum's "none"-role rule would bar cut names as named forms, but decided memo J-1 keeps them (tomahawk, NY strip). They are kept.
- Definition note: Salt beef (silverside) sits under "Corned beef brisket", so that kind's definition should allow other cuts.

**† claims.** None underlie a decision.
