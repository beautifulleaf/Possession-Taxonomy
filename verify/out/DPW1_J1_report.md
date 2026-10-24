# DPW1_J1 report (J1 Meat & Poultry, wave-3 decision pass)

**Input.** All 44 "missing kind?" items in HV_J1_1 and HV_J1_2 were already decided in DPMK_1_J1_kinds.tsv, so they are skipped. Task 1 therefore ran on the generic types that the "gave" column of both fetch logs shows but the tree lacks: 46 candidates.

**Counts (verify/out/DPW1_J1_kinds.tsv).** new_kind 21, covered 14, named_form 5, attribute 4, other_category 2 (rillettes to J5 by P8; pâté en croûte to Culinary by P1).

**New kinds (next free id per R-58; ids checked against data/kinds.tsv, TREE_J1_map.tsv and the reserved DPMK_1 ids J1.1.1.18, J1.1.9.06, J1.1.14.05).**
- Pork: J1.1.3.16 Pork primal or side.
- Goat: J1.1.5.02 Goat chops, .03 Goat shank, .04 Goat leg, .05 Ground goat, .06 Shaped raw mince, goat.
- Duck: J1.1.8.06 Ground duck.
- Venison: J1.1.10.04 Venison haunch, .05 Venison fillet (tenderloin), .06 Venison rack, .07 Ground venison, .08 Shaped raw mince, venison.
- Rabbit: J1.1.11.03 Rabbit saddle, .04 Rabbit leg.
- Horse: J1.1.13.02 Horse ribeye steak, .03 Horse tenderloin, .04 Horse sirloin steak, .05 Horse flank steak, .06 Ground horse meat.
- Sausages: J1.3.3.03 Smoked scalded sausage (kielbasa); J1.3.4.03 White pudding. White pudding has no source_url: the fetched page shows only hogs pudding, so the kind goes to HV_NK. The other 20 kinds carry a URL that the harvester logged as full.

**Moves (verify/out/DPW1_J1_moves.tsv): 6 drops, no to_line, no move_kind.**
- Scotch Beef PGI, Agneau de Sisteron and Welsh Lamb: each designation spans several kinds, so it is a tag (JC1), not a named form.
- Salt Marsh Lamb: salt-marsh grazing is a feeding attribute.
- Herdwick hogget: Herdwick is a breed, which belongs in the varieties table (JC7); hogget is an age attribute.
- Wiener: the name restates the kind "Frankfurter / wiener"; Vienna sausage becomes an alias (C9).
- No named form is a maker or a shop. The Green Circle Chicken rows correctly sit in an existing line.

**Navigation.** The R-116 way in is confirmed: by type of object, meaning the animal for fresh meat and the product type for made meats. The harvested shops group the same way:
- Game sellers (Swaledale, Salter & King, Fine Food Specialist) and D'Artagnan list by species, then by cut.
- farmfetch has separate collections for bacon, sausages, cured meats, ham and gammon, and pâtés and terrines.
- Waitrose splits cooked meats from pâté; Ditalia splits salumi from fresh sausage; Olympia splits sausage from salami.

One change is proposed. G-J1-8 Sausages & salami should get level-2 groups (fresh sausages; salami and dry sausages; frankfurters, smoked and cooked sausages), because every sausage shop fetched splits them this way. Ibérico stays a filter (breed × feeding attribute), not a group.

View sketch:
- **L1:** Beef & veal · Pork · Lamb & goat · Chicken · Turkey, duck & other poultry · Game & other meats · Ham, bacon & cured meats · Sausages & salami · Deli, cooked & tinned · Mixed meat boxes.
- **L2:** Beef has steaks / roasting joints and primals / slow-cook / mince and burgers / offal. Ham has dry-cured ham and pieces / bacon and pancetta / cooked ham, pastrami and corned beef / jerky, cured fat and pickled. Sausages has the three groups above.
- **L3:** kinds (ribeye steak, venison haunch), each with "what makes the best" (grade, breed, feeding, ageing) and "who vouches" (USDA, JMGA/BMS, PDOs), then the named forms.

The kinds that the DPMK_1 and DPW1 passes added still need display-group places. They are listed in verify/work/DPW1_J1/group_adds.tsv. Pork also lacks an offal group for trotter and stomach.

**Rules applied.**
- J-1 and memo 4b: a named cut is a kind once one fetched page shows it sold, and that explicitly includes goat, venison, rabbit and horse.
- Mince and shaped raw mince are kinds per animal; J-3 makes primals and sides kinds.
- C2(a), C2(b), C3: portion, joint, breed and feeding are attributes.
- JC1: a designation that spans several kinds is a tag.
- C11, memo 4b: regional varieties (cotechino, Thai sour sausage) and national sub-cuts (abanico, pork picanha) are named forms.
- P1, P8 and K-44/45 boundaries; R-58 ids.
- Conflict noted: the addendum allows a "none" category only branded, variety, breed or protected-origin named forms, but decided memo J-1 keeps national cut names (tomahawk, NY strip) as named forms. They are kept.
- Definition note: Salt beef (silverside) sits under "Corned beef brisket", so the kind definition needs to allow other cuts.

**† claims.** No decision rests on a † claim. White pudding is a new kind waiting for its attestation page.
