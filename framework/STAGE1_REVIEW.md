# Stage 1 review — top-level categories

For owner review. The current framework is `framework/CATEGORIES_v0_6.md`. It holds 53 categories in 10 domains and an empty holding bin, with a 33-step placement key, shared rules S1 to S6, and a modifier appendix.

## Categories

| Domain | Categories |
|---|---|
| A Worn & Carried | A1 Clothing · A2 Footwear · A3 Jewellery · A4 Bags & Accessories · A5 Clocks & Watches |
| B Home | B1 Furniture & Storage · B2 Soft Furnishings · B3 Lighting · B4 Decor · B5 Kitchen & Dining · B6 Cleaning & Laundry · B7 Climate, Water & Energy · B8 Home Safety & Security · B9 Smoking & Vaping · B10 Animal Equipment |
| C Making, Growing & Work | C1 Tools & Workshop Equipment · C2 Garden & Grounds · C3 Plants & Living Cultures · C4 Craft & Art Supplies · C5 Office & Stationery · C6 Optical & Scientific Instruments · C7 Farm & Forestry Equipment · C8 Building Materials & Hardware |
| D Electronics | D1 Computers & Components · D2 Phones, Tablets & Personal Devices · D3 Audio & Video · D4 Cameras & Photography · D5 Video Games |
| E Play, Sport & Music | E1 Toys & Games · E2 Sports, Fitness & Recreation · E3 Musical Instruments & Music Gear · E4 Weapons & Armour |
| F Culture, Records & Meaning | F1 Media & Publications · F2 Art · F3 Coins, Stamps, Medals & Trading Cards · F4 Religious & Ceremonial Objects · F5 Documents & Personal Records · F6 Natural History & Specimens |
| G Vehicles & Property | G1 Vehicles · G2 Property & Structures |
| H Body | H1 Personal Care & Beauty · H2 Health, Medical & Mobility · H3 Adult Objects |
| I Software, Digital & Subscriptions | I1 Software · I2 Digital Media & Items · I3 Subscriptions, Memberships & Online Services |
| J Groceries & Cellar | J1 Meat & Poultry · J2 Fish & Seafood · J3 Dairy, Eggs & Alternatives · J4 Fruit & Vegetables · J5 Pantry Staples · J6 Coffee, Tea & Cocoa · J7 Wine, Beer & Spirits |

## How it was built and tested

The categories were built outside-in from 30 existing classifications, 4,007 category nodes in all. Grocery structure and grading came from a further harvest:
- Google and COICOP food branches;
- Waitrose, Whole Foods, Eataly, NTUC FairPrice and AEON;
- 29 grading schemes, among them USDA and JMGA beef grades, ISO 3632 saffron categories, SCA coffee scores, tea leaf grades, olive-oil grades, and wine and spirits appellations.

Each version was then tested blind by three independent placers and audited cold.

| Version | Blind placement | Other checks |
|---|---|---|
| v0 (37 categories) | 300 items: 96.0 % unanimous, κ 0.972 | 95.1 % of 3,848 outside nodes homed; audit 1 raised 35 findings |
| v0.1 (44) | 438 items: 98.4 %, κ 0.988 | crosswalk problems 4.9 % down to about 4.0 %; audit 2 raised 55 findings |
| v0.2 (44) | 698 items incl. 260 audit hard cases: 97.4 %, κ 0.982 | — |
| v0.4 (53, with domains I and J) | 857 items incl. 159 new grocery, software, media and subscription items: 99.1 %, κ 0.994; new items 100 % | audit 3 raised 25 findings on the new scope |
| v0.5 (53) | 953 items incl. 96 hard cases from audit 3: 99.0 %, κ 0.993, no splits | majority home matched the intended home on 94 of 96 hard cases |
| v0.6 (53) | adds one sentence for each item round 5 left in doubt; **not re-tested** | — |

## Scope, as decided with the owner

**In:**
- Every kind of physical object a person owns, including plants.
- Groceries as graded ingredients.
- Alcoholic drinks in sealed containers.
- Tobacco, nicotine and cannabis products.
- Pet food and feed.
- Supplements.
- Software of every type.
- Digital media and items.
- Paid subscriptions and memberships.
- Online utility services, free or paid.
- Physical money as objects.
- Physical cards and kept tickets.

**Out:**
- Animals.
- Prepared foods and drinks, which the Culinary taxonomy covers.
- Content genres and the internet as entertainment, which other taxonomies cover.
- Services, one-off or recurring.
- Single-event tickets.
- Balances, stored value, in-game currencies and cryptocurrency.
- Rights and financial instruments.
- Human remains.
- Changes to the body.

## Calls made without you, which you can reverse

- **Phone and broadband plans are in, as connectivity**, in I3. Home energy and water supply are out, as services.
- **Recurring personal services are out, like one-off services.** That covers a cleaner on contract and weekly lessons.
- **Commuter season tickets are in, with other passes**, in I3.
- **Vitamins, supplements and sports nutrition are in, under Health.** The alternative was the grocery domain.
- **Products are filed by what they are, not what they contain.** Fish sauce and lard are pantry staples; butter and ghee are dairy.
- **Hampers are filed by their most valuable item.**
- **Baby and child goods go to their functional homes.**
