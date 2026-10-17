# Stage 1 review — top-level categories

For owner review. The current framework is `framework/CATEGORIES_v0_3.md`. It holds 44 categories in 9 domains and an empty holding bin, with a 32-step placement key, shared rules S1 to S6, and a modifier appendix.

## Categories

| Domain | Categories |
|---|---|
| A Worn & Carried | A1 Clothing · A2 Footwear · A3 Jewellery · A4 Bags & Accessories · A5 Clocks & Watches |
| B Home | B1 Furniture & Storage · B2 Soft Furnishings · B3 Lighting · B4 Decor · B5 Kitchen & Dining · B6 Cleaning & Laundry · B7 Climate, Water & Energy · B8 Home Safety & Security · B9 Cellar & Smoking · B10 Animal Equipment |
| C Making, Growing & Work | C1 Tools & Workshop Equipment · C2 Garden & Grounds · C3 Plants & Living Cultures · C4 Craft & Art Supplies · C5 Office & Stationery · C6 Optical & Scientific Instruments · C7 Farm & Forestry Equipment · C8 Building Materials & Hardware |
| D Electronics | D1 Computers & Components · D2 Phones, Tablets & Personal Devices · D3 Audio & Video · D4 Cameras & Photography · D5 Video Games |
| E Play, Sport & Music | E1 Toys & Games · E2 Sports, Fitness & Recreation · E3 Musical Instruments & Music Gear · E4 Weapons & Armour |
| F Culture, Records & Meaning | F1 Media & Publications · F2 Art · F3 Coins, Stamps, Medals & Trading Cards · F4 Religious & Ceremonial Objects · F5 Documents & Personal Records · F6 Natural History & Specimens |
| G Vehicles & Property | G1 Vehicles · G2 Property & Structures |
| H Body | H1 Personal Care & Beauty · H2 Health, Medical & Mobility · H3 Adult Objects |
| I Digital | I1 Digital Goods |

## How it was built and tested

The categories were built outside-in from 30 existing classifications, 4,007 category nodes in all. Those sources include:
- Google, Shopify and GS1;
- Getty AAT and Nomenclature 4.0;
- COICOP, UNSPSC, HS and the US Consumer Price Index;
- eleven marketplaces;
- auction houses and resale apps;
- insurance and estate inventories.

Each version was then tested blind and audited cold.

| Version | Blind placement (3 independent placers) | Source crosswalk | Cold audit |
|---|---|---|---|
| v0 (37 categories) | 300 items: 96.0 % unanimous, κ 0.972 | 95.1 % of 3,848 in-scope nodes homed; 2.5 % no home, 2.4 % two homes | 35 findings |
| v0.1 (44) | 438 items: 98.4 % unanimous, κ 0.988; 138 fresh items 96.4 % | 160 of 190 problem nodes resolved; estimated 4.0 % no home or two homes | 55 findings |
| v0.2 (44) | 698 items, including 260 hard cases drawn from both audits: 97.4 % unanimous, κ 0.982, no three-way splits; 438 probes 98.4 %, 260 hard cases 95.8 % | not re-run | — |
| v0.3 (44) | adds one sentence for each of the 18 items round 3 left non-unanimous; **not re-tested** | — | — |

## Decisions made without you, which you can reverse

- **The top axis is designed function**, after a short status filter covering out of scope, health, property, data, living things, natural specimens and parts. Material, power source, setting, installation, market, user, occasion, connectivity, brand, tier, scene, era and motive are all modifiers.
- **Baby and child goods have no category of their own.** The user's age is a modifier, so a cot is Furniture, a pram is a Vehicle and a pacifier is Personal Care. Retailers do group baby goods, and that grouping could become a generated view.
- **Protective gear goes by form.** Work protective equipment and motorcycle and cycling helmets are Clothing. Gear made for one sport is Sports. Armour against weapons is Weapons.
- **Building products are filed by what they are, installed or not.** Property holds land and whole buildings only.
- **Rights and financial instruments are out.** That covers tickets, timeshares, shares and cryptocurrency holdings. Their paper or card tokens are Documents. Physical cash is in, under Coins.
- **Human remains are out.** Urns and coffins are Religious & Ceremonial.
