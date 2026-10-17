# AU3 — Cold audit of the new scope rules (step 1 OUT, step 3 / J, step 5 / I, B9, B10)

Source read: `audit/CATEGORIES_R4.md` (v0.3) only. Offline, no other repository file opened.
Notation: `S1 -> OUT` means "stops at step 1, outside scope". "Split" means two careful readers following the printed key can reach different answers. Quotations are from the file.

Status: COMPLETE (25 findings, 72 tested examples, top five changes).

---

## Part 1 — Tricky examples run against the printed key

| # | Object or purchase | Path through the printed key | Result now | Verdict | Finding |
|---|---|---|---|---|---|
| 1 | Kimchi (jar) | S1 lead: "made to be eaten as it is" fits; S1 note sends groceries to S3; S3 lead "fermented" fits; J4 needs "fresh"; J5 "pickles and preserves" | J5 | OK, but only because the note wins over the lead | F1 |
| 2 | Frozen peas | S3 lead fits ("preserved"); J4 says "**fresh** fruit, vegetables"; J5 lists tinned and jarred, not frozen; no branch fits, so S1a says continue; nothing later fits | X0 | **Gap** | F2 |
| 3 | Smoked salmon | S1 lead fits (eaten as is); note sends to S3; J2 "smoked" | J2 | OK via note | F1 |
| 4 | Fresh egg tagliatelle | J5 "dried and fresh pasta" | J5 | OK | — |
| 5 | Fresh spinach ravioli / tortellini | J5 "fresh pasta" vs S1 "frozen dumplings and other prepared dishes" | J5 or OUT | **Split** | F4 |
| 6 | Sourdough loaf | S1 "bread and bakery" | OUT | OK | — |
| 7 | Ready-rolled puff pastry, pizza dough | S1 "bakery"? or J5 "baking ingredients"? | OUT or J5 | **Split** | F4 |
| 8 | Meal-kit subscription (weekly box) | S5 I3 "subscription boxes"; the delivered kit is a set "filed by its main contents" (undefined) | I3 (plan); kit split J1/J5/OUT | Plan OK, goods unclear | F5, F16 |
| 9 | Wine club membership | S3 no (not a drink); S5 I3 "club memberships", "subscription boxes" | I3; bottles J7 | OK, but double role of I3 | F16 |
| 10 | Spotify Family plan | S5: I1? (an app is used) or I3 "music streaming" | I3 (most readers) | OK; seat type is a modifier | F15 |
| 11 | Xbox Game Pass Ultimate | S5 note "video games are D5 on any carrier or as downloads" vs I3 "game streaming or catalogue subscriptions"; D5 note names only "game streaming subscriptions" | I3 or D5 | **Split** | F14 |
| 12 | Netflix gift card (plastic) | S1 note: "payment cards are step 19"; but S5 (paid access) is met first if the note is read as "continue" | F5 or I3 | Split on note semantics | F18 |
| 13 | Netflix gift code by e-mail | S1 "gift-card value" | OUT | OK | F13 |
| 14 | Password manager family plan | I1 "password managers ... subscription" | I1 | OK | — |
| 15 | Kindle Unlimited | I1 (Kindle app)? I3 "catalogue subscription"; borrowed e-books are "part of that subscription" | I3 | OK once I1/I3 line is fixed | F12 |
| 16 | Audible credit | I2 entitlement? S1 "stored value"/"loyalty points"? I3 (comes with membership)? | I2, I3 or OUT | **Split** | F13 |
| 17 | Cloud photo library (iCloud+ / Google One 2 TB) | I1 is tried first: "software of any kind ... subscription"; I3 "cloud storage" reached only if a reader says storage is not software | I1 or I3 | **Split (key-order)** | F12 |
| 18 | The photos in that library | I2 "photograph files"; prints of own life are F5 | I2 | OK, axis note | F25 |
| 19 | VPN subscription | I1 "security and VPN software" | I1 | OK (explicit) | F12 |
| 20 | Coffee subscription box | I3 "subscription boxes"; beans J6 | I3 + J6 | OK, axis note | F16 |
| 21 | Bottled sparkling water | S1 "bottled waters" | OUT | OK | — |
| 22 | Oat milk | S1 lead: drink "drunk as it is", like juices; note: is it "minimally processed"? no; J3 says "milk" (dairy); J5 "soy staples" (not oat) | OUT, J3 or J5 | **Split** | F8 |
| 23 | Protein bar | S1 "snacks" -> OUT; S1 note "supplements are step 2"; S2 lists only "sports-nutrition **powders**" | OUT or H2 | **Split** | F7 |
| 24 | Infant formula | S2 (before S3): "compensate for ... breastfeeding"; J3 lists formula; S3 lead "raw or minimally processed" does not fit formula | H2 or J3 | **Split (key-order)** | F7, F1 |
| 25 | Honeycomb | J5 "sugar, honey" | J5 | OK (not honeycomb toffee, which is OUT) | — |
| 26 | Dry-aged ribeye | J1 "cut and grade ... ageing" | J1 | OK | — |
| 27 | Whole live crab | S1 "a living animal" | OUT | **Scope break**: live shellfish is ordinary seafood retail | F3 |
| 28 | Live oysters, mussels, clams | always sold alive: S1 | OUT | **Scope break** | F3 |
| 29 | Christmas ham, cooked and glazed, ready to carve | J1 "hams"; S3 lead "not made into a dish"; glazing and cooking = dish? | J1 or OUT | **Split** | F1 |
| 30 | Sake gift set (bottle + two cups) | S3 note: "set filed by its main contents" | J7 | OK if "main" means the sake; undefined | F5 |
| 31 | Christmas hamper (wine, cheese, crackers, chocolates, basket) | "main contents" undefined; crackers and chocolates are OUT | J7, J3 or OUT | **Split** | F5 |
| 32 | Ketchup, mayonnaise, stock cubes | J5 lists sauces and condiments, but S3 lead requires "raw or minimally processed"; S1 lead "eaten as it is"? | J5 or OUT | **Split** (lead vs branch) | F1 |
| 33 | Fish sauce, oyster sauce, anchovy paste | J2 is tried before J5: "fish and seafood ... preserved" | J2 or J5 | **Split (branch order)** | F5 |
| 34 | Jar of bolognese sauce with beef | J1 first (contains meat)? J5 sauces? S1 ready meal? | J1, J5 or OUT | **Split** | F5 |
| 35 | Tinned tomato soup, tinned ravioli | J5 "tinned and jarred goods" vs S1 "ready meals ... prepared dishes" | J5 or OUT | **Split** | F4 |
| 36 | Dried apricots, Medjool dates | J4 "fresh"; J5 has nuts, seeds, preserves, no dried fruit | J5 or X0 | **Split / gap** | F2 |
| 37 | Dried porcini, nori, kombu | J4 "fresh ... edible fungi"; seaweed named nowhere | X0 | **Gap** | F2 |
| 38 | Muesli, cornflakes | J5 "grains"? S1 "snacks"/finished food? | J5 or OUT | **Split** | F2 |
| 39 | Beyond Burger, seitan, tempeh | J1 is by species; J5 "tofu and soy staples" covers tempeh only | X0 / J5 | **Gap** | F2 |
| 40 | Beef jerky, biltong | J1 "cured" / S3 "dried" vs S1 "snacks" | J1 or OUT | **Split** | F6 |
| 41 | Salted roasted cashews (snack bag) | J5 "nuts" vs S1 "snacks" | J5 or OUT | **Split** | F6 |
| 42 | Ice cream tub | J3 (dairy)? S1 (dessert, not named) | J3 or OUT | **Split** | F1 |
| 43 | Ghee, lard, dripping | J3 "butter"? J1 (animal)? J5 "oils"? | three answers | **Split** | F5 |
| 44 | Mirin, Shaoxing cooking wine, Angostura bitters | J5 (condiment) is tried before J7 (alcoholic drink) | J5 by order | OK by order but unstated | F23 |
| 45 | Canned gin and tonic (RTD) | S1 "soft drinks"? note: alcoholic in sealed container -> J7 | J7 | OK | — |
| 46 | Alcohol-free beer | J7 needs "alcoholic"; S1 "soft drinks" | OUT | OK, worth stating | F23 |
| 47 | En primeur Bordeaux (bought, not yet bottled) | S1 "right, claim" | OUT | OK, unstated | F23 |
| 48 | Balut (fertilised duck egg, food) | S1 "fertilised eggs" | OUT | Wrong by intent | F3 |
| 49 | Snus, nicotine pouches | S27 "smoked, vaped, chewed or snuffed": a pouch is neither chewed nor snuffed | B9 or X0 | **Split (wording)** | F19 |
| 50 | Cannabis gummies | S1 "sweets" is met first; S1 note sends only "smoking products" to S27 | OUT or B9 | **Split** | F19 |
| 51 | CBD oil drops | S2 "dietary supplements" or S27 | H2 or B9 | **Split** | F19 |
| 52 | Areca nut / betel quid, khat leaves, kratom powder | S3 "nuts and seeds", J4 "fresh herbs", J6 "leaves ... brewed as infusions" are all met before S27 | J5/J4/J6 or B9 | **Key-order trap** | F19 |
| 53 | Zippo or disposable pocket lighter | S27 "cigar and pipe lighters"; S32 C8 "utility lighters"; S17 note: "a lighter ... is filed by what it does" | B9 or C8 | **Split** | F20 |
| 54 | Herb grinder (cannabis) | not named in S27; S30 B5 "kitchen tools" | B5 or B9 | **Split** | F20 |
| 55 | Wild-bird seed, fat balls | S3 "nuts and seeds" (lead says "food", not "food for people"); S3 note names only "pet food" | J5 or B10 | **Split** | F21 |
| 56 | Hay for a horse; bulk cattle feed | S12 C7 "made for agricultural production" is met before S13 unless the S1 note is a direct jump | C7 or B10 | **Split (key-order)** | F21, F18 |
| 57 | Frozen feeder mice | J1 "meat" vs B10 "pet food" | J1 or B10 | Split | F21 |
| 58 | Live mealworms for a lizard | S1 "living animal (including live bait)" | OUT | OK, state it | F21 |
| 59 | Mobile phone contract, broadband, electricity tariff | S5 I3 "paid ... ongoing access to a service"; the scope paragraph's "for enjoyment or quality of life" is not in the key | I3 by key | **Scope break** | F10 |
| 60 | Weekly cleaner on contract, monthly piano lessons | S1 OUTs only "a one-off service or course"; recurring service -> I3 | I3 by key | **Scope break** | F10 |
| 61 | Amazon Prime, Costco membership | I3 "access to a ... benefit" | I3 | Unbounded wording | F10 |
| 62 | Microsoft 365 Family (apps + 1 TB), Apple One | I1 (software) or I3 (storage, catalogue) | I1 or I3 | **Split** | F12 |
| 63 | Marina berth vs yacht-club membership; allotment tenancy vs community-garden membership; parking permit; storage unit; coworking membership | S1 OUTs a "licence ... to use a place"; S5 I3 "membership ... access to a ... place" | OUT or I3 per reader | **Overlap** | F11 |
| 64 | Ten-class yoga card; 10-journey rail carnet | not "a single event or journey" (OUT) and not "ongoing" (I3) | OUT or I3 | **Gap** | F17 |
| 65 | Monthly rail season ticket | I3 "season tickets and annual passes" | I3 | OK by key, out of the stated scope "for enjoyment" | F10 |
| 66 | Fortnite V-Bucks | I2 "in-game ... currencies" vs S5 note "fungible money tokens are OUT" and S1 "stored value" | I2 or OUT | **Overlap** | F13 |
| 67 | Game DLC expansion; Fortnite battle pass | D5 "video game ... download"; I2 "in-game items"; I3 "season ... passes" | D5, I2 or I3 | **Split** | F14 |
| 68 | World of Warcraft monthly subscription; PlayStation Plus | D5 (the game) or I3 | D5 or I3 | **Split** | F14 |
| 69 | Tesla FSD / heated-seat subscription | S5 note "software built into a device is part of the device" vs I1 "however licensed ... subscription" vs I3 | G1, I1 or I3 | **Split** | F17 |
| 70 | DAZN / NFL Sunday Ticket; Crunchyroll | "never by genre" would forbid a "sports" or "anime" class, but "genre" is not defined and I3 itself names "news" | OK at top level; inner split risk | Axis risk | F15 |
| 71 | Potted living basil; living microgreens tray | S3 note: "living plant in a pot is C3"; S6 note: "microgreens sold to eat are step 3" | C3 or J4 | Split (tray) | F24 |
| 72 | Dried baker's yeast; kefir grains | J5 "baking ingredients" (S3, met first); S1 note: cultures "kept to grow or propagate" are S6 | J5 / C3 | OK, distinction holds | F24 |

Tally of the 72: 23 decide cleanly ("OK"), the other 49 split, fall into a key-order trap, leave a gap or break the stated scope. The splits cluster on four hinges: the step 1 / step 3 food line (F1–F8), the I1 / I3 / OUT line (F10–F17), the meaning of a binding note (F18), and the late position of B9 (F19).

---

## Part 2 — Findings

### A. Step 1 OUT and step 3 / domain J (groceries)

**F1. The step 1 "prepared food" test and the step 3 "minimally processed" test do not match the J branches.** Type: key-order trap / overlap. Severity: **high**.
- Step 1 OUTs any "finished food or drink made to be eaten or drunk as it is". Cheese, yoghurt, ham, smoked salmon, caviar, kimchi, honey, jam and pickles all meet that test. They are saved only by step 1's note ("groceries, meaning ingredients and raw or minimally processed foods ... are step 3") and S1b ("the note wins").
- The note and the step 3 lead then test "raw or minimally processed ... not made into a dish". Many things the J branches list explicitly fail that test: ketchup, mayonnaise, stock cubes, sauces, baking chocolate, tofu, infant formula, milk powders. A reader who applies the lead first (S1a: "When a step's lead question is yes ...") never reaches the branch that names them.
- Things neither list names are left to the reader's sense of "dish": ice cream, cooked and glazed Christmas ham, hot-smoked mackerel, rotisserie chicken, breakfast cereal.
- Examples: #1, #3, #24, #29, #32, #42.
- Fix: replace the step 1 prepared-food clause with:
  > a **prepared food or drink**: a dish, baked good, confection, dessert, snack product or non-alcoholic drink, made by cooking or combining ingredients into something eaten or drunk as it is: bread and other bakery, cakes and pastries, sweets, chocolate bars and other confectionery, ice cream and frozen desserts, crisps, crackers, popcorn and other snack products, ready meals, soups, filled pasta, dumplings and other prepared dishes, sandwiches, salads and baby-food meals, soft drinks, juices, bottled waters, ready-to-drink coffee and tea, kombucha. These are left to the Culinary taxonomy. Curing, smoking, ageing, fermenting, drying, salting, pickling, tinning, freezing or plain cooking of one main ingredient does not make a food prepared: cheese, yoghurt, butter, hams (raw or cooked, glazed or not), sausages and charcuterie, smoked and tinned fish, pickles and kimchi, jams, honey, and every product named in step 3's branches are groceries;
- In step 1's note, replace "groceries, meaning ingredients and raw or minimally processed foods, and alcoholic drinks in sealed containers, are step 3" with:
  > groceries, meaning the foods for people named in step 3 and its branches, and alcoholic drinks in sealed containers, are step 3
- Replace the step 3 lead with:
  > **Groceries**: food for people bought as an ingredient, as a raw, preserved or single-ingredient product, or as a dairy, pantry or drinks product named in the branches below, and not a prepared food or drink (step 1); or an **alcoholic drink in a sealed container** (bottle, can, keg, cask, box)?

**F2. Frozen and dried produce, seaweed, breakfast cereals, spreads and meat alternatives have no branch.** Type: gap. Severity: **high**.
- J4 reads "**fresh** fruit, vegetables, herbs and edible fungi". J5 lists "tinned and jarred goods" but not frozen or dried produce. Under S1a ("no branch fits ... continue"), frozen peas, frozen berries, frozen spinach, dried apricots, dates, raisins, dried porcini and shiitake fall through to X0.
- Seaweed (nori, kombu, wakame) is named nowhere, and "seafood" usually excludes it.
- Muesli and cornflakes split between J5 "grains" and step 1.
- Peanut butter, Nutella and Marmite are unnamed.
- Beyond Burger, seitan and Quorn: J1 is "by species", and J5 has only "tofu and soy staples".
- Examples: #2, #36–#39.
- Fix: replace J4 with:
  > **fruit, vegetables, herbs, edible fungi and seaweeds, fresh or frozen**, whole, cut or washed, but not dressed, sauced, fried or coated? **J4 Fruit & Vegetables**
- Also rename the category to "J4 Fruit & Vegetables" in the category list.
- Replace the J5 branch with:
  > **pantry staples**: rice, grains, flours, oats and breakfast cereals, dried and fresh unfilled pasta and noodles, gnocchi, pulses, nuts and seeds, dried fruit, dried vegetables, dried mushrooms and dried seaweed, oils, cooking fats and vinegars, spices, dried herbs and salt, sugar, honey (including honeycomb) and syrups, sweet and savoury spreads, sauces, condiments, stocks and pastes from any source, pickles and preserves, tinned and jarred fruit, vegetables, pulses and tomatoes, baking ingredients (raising agents and dried yeast, baking chocolate, unbaked doughs and pastry), tofu, tempeh, seitan and other plant proteins and meat alternatives? **J5 Pantry Staples**

**F3. Live shellfish and crustaceans are OUT, and "fertilised eggs" catches a food.** Type: scope. Severity: **high**.
- Oysters, mussels, clams and langoustines are normally sold alive, and so are crabs and lobsters at fishmongers. The step 1 clause "a living animal" sends the core of J2 out of scope.
- Balut, a fertilised duck egg sold as food, is OUT by the words "fertilised eggs", though the intent is eggs for hatching.
- Examples: #27, #28, #48.
- Fix: in step 1, replace "A living animal (including live bait and fertilised eggs)" with:
  > A living animal (including live bait, live feeder insects and eggs for hatching), except shellfish and crustaceans sold alive to be eaten, such as oysters, mussels, clams, crabs and lobsters, which are groceries (step 3)
- In step 3's note, replace "a live animal is OUT" with:
  > a live animal is OUT, except shellfish and crustaceans sold alive to be eaten (J2)
- In J2, add "including shellfish and crustaceans sold alive".

**F4. Filled pasta, unbaked dough, and tinned or jarred dishes straddle step 1 and J5.** Type: overlap. Severity: medium.
- Fresh ravioli and tortellini are J5 ("fresh pasta"), yet gyoza and pierogi are OUT ("frozen dumplings"). Both are the same structure: a filled dough.
- Tinned soup, tinned ravioli and jarred curry are J5 "tinned and jarred goods", and also step 1 "ready meals ... prepared dishes".
- Puff pastry and pizza dough split between "bakery" (OUT) and "baking ingredients" (J5).
- Examples: #5, #7, #35.
- Fix: covered by the F1 and F2 wording ("filled pasta, dumplings ... soups" OUT; "unfilled pasta", "unbaked doughs and pastry", "tinned and jarred fruit, vegetables, pulses and tomatoes" J5). Also add to step 3's note:
  > Soups, stews, curries and pasta dishes in tins, jars or pouches are ready meals (step 1).

**F5. Branch order captures derived and composite products, and "main contents" is undefined.** Type: key-order trap. Severity: medium.
- J1 and J2 are tried before J5, so a reader who asks "is it fish?" files fish sauce, oyster sauce, shrimp paste, anchovy paste, Worcestershire sauce and dashi powder in J2.
- By the same reading: bolognese sauce, stock cubes, gelatin, lard and dripping go to J1, and ghee goes to J3 or J5.
- "A set or hamper is filed by its main contents" does not say whether "main" means value, volume or count. A hamper of wine, cheese, crackers and chocolates gets three answers, and the crackers and chocolates are OUT.
- Examples: #30, #31, #33, #34, #43.
- Fix: replace "A set or hamper is filed by its main contents." in step 3's note with:
  > A product is filed by what it is, not by what it contains: sauces, condiments, stocks, pastes and cooking fats are J5 whatever they are made from (fish sauce, oyster sauce, stock cubes, lard, dripping), except butter and ghee (J3). A set, gift box or hamper is filed by its item of greatest value, and is OUT if that item is a prepared food; a basket or box kept afterwards is filed as itself (B1).

**F6. "Snacks" (OUT) collides with nuts, dried fruit and dried meat (in).** Type: overlap. Severity: medium.
- Examples: salted roasted cashews, trail mix, beef jerky, biltong, dried squid and seaweed snacks.
- Examples in the table: #40, #41.
- Fix: add to step 3's note:
  > Nuts, seeds, dried fruit, and dried or cured meat and fish are groceries even when sold salted, roasted or as snacks (J5, J1, J2). Crisps, puffs, crackers, popcorn, bars and other snack products made from mixed ingredients are prepared foods (step 1).

**F7. Infant formula and sports nutrition: step 2 sits before step 3, and the form decides.** Type: key-order trap. Severity: medium.
- Step 2 ("compensate for ... breastfeeding") can take infant formula before J3 is reached. No note in step 2 sends it on.
- Step 2 lists "sports-nutrition **powders**", so protein powder is H2. A protein bar is a step 1 "snack" (OUT), and gels and ready-to-drink shakes are unclear. The same product line from the same maker ends up in three places.
- Examples: #23, #24.
- Fix: add to step 2's notes:
  > Infant formula and follow-on milks are J3, except formulas made for a medical condition (hypoallergenic, amino-acid and metabolic formulas), which are here. Sports-nutrition and meal-replacement products are here in every form: powders, protein bars, gels, ready-to-drink shakes and tablets.
- In step 1's note, after "medicines, vitamins and supplements", insert:
  > and sports-nutrition and meal-replacement products in any form

**F8. Plant milks and other "drink or ingredient" products have no home.** Type: gap / overlap. Severity: medium.
- Oat, almond and rice milk are "drunk as it is" like juices (step 1), but are bought and used as milk. J3 says "milk" and means dairy. J5's "soy staples" catches soy milk only.
- The same problem applies to plant yoghurts, vegan cheeses and coconut milk. Coconut milk in a tin is arguably J5, but in a carton it is a drink.
- Kefir and drinking yoghurt are fine in J3 but are not named.
- Examples: #22.
- Fix: replace the J3 branch with:
  > **milk, cream, butter and ghee, yoghurt and kefir, cheese and eggs**, milk powders and infant formula, and plant-based alternatives to them (oat, soy, almond and other plant milks, plant yoghurts and plant cheeses)? **J3 Dairy, Eggs & Alternatives**
- Add "coconut milk and cream" to the J5 sauces list.

**F9. The J category lines drift from the key, and J7 tests motive.** Type: wording. Severity: low.
- J1's line says "fresh or cured", while the key says "fresh, frozen, cured or smoked".
- J7's line says "kept as stock". That tests why the owner keeps it, which breaks S5 and Appendix A ("motive"): a bottle bought for tonight is still J7.
- J4's line still says "fresh fruit".
- Fix, in the category list:
  - J1: "**J1 Meat & Poultry** — meat, poultry and game as bought, fresh, frozen, cured, smoked or cooked, including charcuterie and hams, divided by species, cut and grade (for example USDA and JMGA grades, breed, feeding and ageing)."
  - J3: "**J3 Dairy, Eggs & Alternatives** — milk, cream, butter and ghee, yoghurt, cheese, eggs, milk powders and infant formula, and plant-based alternatives to them."
  - J4: "**J4 Fruit & Vegetables** — fruit, vegetables, herbs, edible fungi and seaweeds, fresh or frozen, by species and cultivar."
  - J7: "**J7 Wine, Beer & Spirits** — alcoholic drinks in sealed containers, by style, appellation and age."

### B. Step 5 and domain I (software, digital items, subscriptions)

**F10. The I3 key question is far wider than the stated scope: recurring services, utilities and "benefits" all qualify.** Type: scope. Severity: **high**.
- The scope paragraph limits subscriptions to those held "for enjoyment or quality of life". The key, which wins ("Where they differ, the key wins"), asks only for "paid ongoing access to a service, catalogue, place or benefit".
- Step 1 OUTs only "a one-off service or course", so every recurring service falls into I3. That includes a mobile contract, broadband, an electricity tariff, a water-delivery plan, a weekly cleaner, monthly piano lessons, childcare, a lawn-care plan, AppleCare or roadside assistance (insurance-like), a professional body or union membership, and a commuter season ticket.
- "Benefit" also admits Amazon Prime shipping, Costco, airline lounge access and credit-card annual fees.
- Examples: #59–#61, #65.
- Fix (1): in step 1, replace "a one-off service or course" with:
  > a service, one-off or recurring, performed for the person or supplied to their home (cleaning, care, lessons and courses, repairs, deliveries, utilities and energy, phone, mobile and broadband contracts), and insurance, warranty and assistance plans, except the subscriptions and memberships named in step 5
- Fix (2): replace the I3 branch's question with:
  > a **paid subscription or membership** giving ongoing or periodic access to (a) a catalogue of content or play: music and audio, audiobooks and podcasts, film and TV, text, news and magazines, comics, recorded and streamed classes, and game catalogues, streaming and online play; (b) hosted storage or backup; (c) a shared place, club or venue open to members: gym, sports, social and hobby clubs, museums, parks and attractions, season tickets and passes for venues, events or travel valid for a period or a number of visits; or (d) a recurring delivery of goods chosen or curated by the provider (subscription boxes, wine and coffee clubs, meal-kit plans)? **I3 Subscriptions & Memberships**
- Fix (3): add to I3's notes:
  > A membership that gives only discounts, shipping or points is OUT (step 1). A bundle is filed by the component it is named and sold for: Microsoft 365 (office software) I1; iCloud+, Google One and Dropbox (storage) I3; Apple One and Amazon Prime (catalogue access) I3.
- Fix (4): change the scope paragraph's "for enjoyment or quality of life" to "of the kinds step 5 names".

**F11. Rights to a place (OUT) and memberships giving access to a place (I3) overlap.** Type: overlap. Severity: medium.
- Step 1 OUTs "a licence, tenancy or timeshare to use a place ... allotment tenancy, mooring or timeshare week". I3 takes "membership giving ongoing access to a ... place".
- Pairs where readers split: a marina berth vs a yacht-club membership; an allotment tenancy vs a community-garden membership; a parking permit vs a monthly car-park subscription; a self-storage unit; a coworking desk; a holiday-club points scheme vs a timeshare week.
- Examples: #63.
- Fix: in step 1, replace the bracket "(a licence, tenancy or timeshare to use a place the person does not hold as land, a building or a burial plot, such as an allotment tenancy, mooring or timeshare week; ...)" with:
  > (a licence, tenancy, permit, rental, timeshare week or timeshare points giving the person a specific place or space for their own use that they do not hold as land, a building or a burial plot, such as an allotment, mooring or berth, parking space or permit, storage unit or dedicated desk; ...)
- Add to I3's notes:
  > Shared access to a place open to all members (a club, gym, golf course, coworking hot desk, museum or park) is here; a specific place for the person's own use is a right (step 1).

**F12. I1 is tried first and its wording swallows hosted services, so I3's "cloud storage" is reached only by chance.** Type: key-order trap. Severity: **high**.
- I1 takes "software of any kind ... however it is licensed or delivered (download, subscription ...)". Every hosted service comes with an app, so a strict reader files iCloud+, Google One, Dropbox, Kindle Unlimited and Spotify in I1 before I3 is tried.
- Readers will therefore split on cloud photo libraries, storage plans and catalogue apps, and also on bundles (Microsoft 365, Apple One).
- VPN is decided explicitly as I1. That is acceptable, but it is the only service that is.
- Examples: #15, #17, #62.
- Fix: replace the I1 branch with:
  > **software**: a program or app, or a hosted tool whose value is what the program does for the user (password managers, security and VPN software, operating systems, creative, productivity and finance programs, AI assistants, apps), however it is licensed or delivered (download, subscription, licence key, boxed disc, web), including a separately paid licence or feature unlock for software in a device? **I1 Software** (Note: a hosted service whose value is the storage, catalogue, place or play it gives access to, such as cloud storage, a streaming catalogue or online play, is I3, even when an app is used to reach it.)

**F13. Stored value, credits and in-game currency are split between I2 and OUT.** Type: overlap. Severity: medium.
- I2 lists "in-game items **and currencies**".
- Step 5's note says "fungible money tokens are OUT", and step 1 OUTs "stored value", "gift-card value" and "loyalty points".
- So V-Bucks or Robux are I2, while Steam wallet balance and a Netflix gift code are OUT. An Audible credit (redeemable for any one title) gets three answers.
- Examples: #13, #16, #66.
- Fix: in I2, replace "in-game items and currencies" with:
  > in-game items (characters, skins, cosmetic and consumable items)
- In step 1, replace "(bank balance, gift-card value, cryptocurrency)" with:
  > (bank balance, gift-card, gift-code and wallet value, in-game and platform currencies, credits redeemable for a choice of items such as audiobook credits, cryptocurrency)

**F14. Games: catalogue passes, DLC, battle passes and single-game subscriptions have no settled home.** Type: overlap / key-order. Severity: medium.
- Step 5's note sends "video games ... on any carrier or as downloads" to D5. A Game Pass catalogue delivers downloads, but the D5 note names only "game streaming subscriptions" as I3. PlayStation Plus is online play plus a catalogue.
- A World of Warcraft subscription is access to one game.
- A DLC expansion is "a video game ... as a download" (D5) or an in-game item (I2).
- A battle pass or "season pass" collides with I3's "season tickets and annual passes".
- Examples: #11, #67, #68.
- Fix: replace D5's branch note "(Note: games are divided by platform and carrier here, never by genre; game streaming subscriptions are I3.)" with:
  > (Note: games are divided by platform and carrier here, never by genre. Expansions and downloadable content that add to one game are D5 with the game; cosmetic and consumable in-game items are I2; game subscriptions and passes are I3: catalogue and streaming subscriptions (Xbox Game Pass, PlayStation Plus), online-play memberships, single-game subscriptions, and in-game battle and season passes.)
- In step 5's note, replace "video games are D5 on any carrier or as downloads" with:
  > video games and their expansions are D5 on any carrier or as downloads; game subscriptions and passes are I3

**F15. "Never by genre" is not defined, and I3's own list breaks it.** Type: axis break / wording. Severity: medium.
- The rule is repeated for F1, D5, I2 and I3, but "genre" is never defined.
- I3 itself lists "news", which is a content type, not a carrier. Stage-2 builders will then ask whether sports streaming (DAZN), kids' (Disney+), anime (Crunchyroll), fitness (Peloton) or faith services are permitted classes.
- I2 is to be divided "by format", but domain names, NFTs and in-game items have no format in the file-format sense.
- Examples: #10, #70.
- Fix: replace I3's note "subscriptions are divided by the kind of access they give, never by the genre of the content" with:
  > subscriptions are divided by the kind of access they give, never by content. Kind of access means the medium the catalogue holds (music and audio, audiobooks and podcasts, film and TV, text and news periodicals, comics, classes, games), how it is delivered (stream, download, physical delivery, entry to a place) and the seat structure (individual, family, student). The subject, genre, sport or audience of the content (sport, children, anime, crime, fitness, faith) never divides a category: a sports streaming service is film-and-TV streaming.
- In I2's line, replace "by format, never by genre" with:
  > by kind and file format, never by genre or subject

**F16. "Subscription boxes" in I3 makes a way of buying into a category, and blurs the plan and the goods.** Type: axis break. Severity: medium.
- Appendix A lists "how acquired" as a modifier.
- A coffee subscription box, a wine club or a meal-kit plan is partly a membership and partly a standing order for physical goods. The key never says that the delivered coffee, wine or kit is filed by what it is. A reader can therefore file a cellar of club-delivered wine under I3, or count it twice.
- Examples: #8, #9, #20.
- Fix: add to I3's notes:
  > A subscription box, wine or coffee club or meal-kit plan is filed here as the plan; each item delivered is filed by what it is (wine J7, coffee J6, a meal kit under step 3's set rule). A repeat order at a fixed price, with no curation, membership or access, is only a way of buying the goods (Appendix A, how acquired) and is not filed.

**F17. Passes for several visits, and paid feature unlocks for a device, fall between the clauses.** Type: gap. Severity: low–medium.
- A ten-class yoga card or a 10-journey carnet is not "a single event or journey" (OUT) and not "ongoing" (I3).
- A paid unlock or subscription for a feature of a device, such as Tesla FSD, heated seats or BMW ConnectedDrive, meets step 5's note "software built into a device is part of the device", and also I1 and I3.
- Examples: #64, #69.
- Fix: covered by F10's "valid for a period or a number of visits" and F12's "separately paid licence or feature unlock for software in a device". Also add to step 5's note, after "software built into a device is part of the device":
  > unless it is paid for separately, as a licence, unlock or subscription, which is I1
- Travel season tickets stay I3 under F10's wording. If the owner wants commuting excluded, the clause should say "for venues and events" instead.

### C. Note semantics (affects every new addition)

**F18. S1b does not say whether a note jumps directly or continues the key.** Type: key-order trap. Severity: **high** (structural).
- The new additions rest on step 1's notes: "groceries ... are step 3", "pet food and animal feed are step 13", "smoking products are step 27", "payment cards are step 19".
- S1b says a note "takes the objects it names out of that step and sends them to the step or category it names". It does not say whether the steps in between are skipped. If they are tried:
  - infant formula can stop at step 2 (F7);
  - farm feed and hay stop at step 12, C7 "made for agricultural production" (F21);
  - a Netflix gift card stops at step 5 as prepaid access (#12);
  - areca nut and herbal smoking blends stop at step 3 (F19).
- Examples: #12, #24, #52, #56.
- Fix: replace S1b's second sentence with:
  > It takes the objects it names out of that step and files them directly at the step or category it names; the steps in between are not tried. If the named step has branches and none fits, continue from the step after the named step.

### D. B9 Smoking & Vaping

**F19. B9's verbs miss pouches, edibles and tinctures, and step 27 comes after steps that catch chewed plant products.** Type: key-order trap / gap. Severity: **high**.
- Snus and nicotine pouches are held in the mouth: neither "chewed" nor "snuffed".
- Cannabis gummies meet step 1 "sweets" first. Step 1's note rescues only "smoking products". Cannabis drinks meet "soft drinks".
- CBD oil meets step 2 "dietary supplements".
- Before step 27 is reached, areca nut and betel meet J5 ("nuts and seeds"), khat meets J4 ("fresh herbs"), and kratom and coca leaf meet J6 ("leaves ... brewed as infusions").
- Herbal smoking blends look like J5 "dried herbs".
- The scope paragraph says "tobacco, cannabis" are in, without limiting form, so the key and the scope disagree on edibles.
- Examples: #49–#52.
- Fix: replace step 27 with:
  > **Tobacco, nicotine and cannabis products in any form, and other plant products taken for a stimulant or psychoactive effect rather than as food or drink**: cigarettes, cigars, loose, pipe and chewing tobacco, snuff, snus and nicotine pouches, heated-tobacco sticks, e-liquids and pods, cannabis flower, resin, concentrates, edibles, drinks, tinctures and CBD products, herbal smoking blends, betel quid and areca nut sold for chewing, khat, kratom; or **implements made for smoking, vaping or preparing these** (pipes, bongs, hookahs and hookah coals, vapes, pocket lighters, ashtrays, cigar cutters, cigarette cases, rolling papers and machines, herb grinders)? **B9 Smoking & Vaping** (Notes: medicinal nicotine, and cannabis prescribed or licensed as a medicine, are H2; CBD products are here even when sold as supplements. Hemp seeds and hemp oil sold as food are J5. Coffee, tea and kava are J6; alcoholic drinks are J7. Humidors are B1. Long utility and candle lighters, matches and firelighters are C8.)
- In step 1's note, replace "smoking products are step 27" with:
  > tobacco, nicotine and cannabis products and the other products step 27 names are step 27 in any form, including edibles, drinks and supplements
- In step 3's note, add:
  > areca nut, khat, kratom and the other products step 27 names are B9
- B9's category line: "**B9 Smoking & Vaping** — tobacco, nicotine and cannabis products in any form, other plant products taken for a stimulant or psychoactive effect, and implements for smoking, vaping or preparing them."
- Also amend the scope paragraph to match.

**F20. Lighters, grinders and cases split across B9, C8, B5 and A4.** Type: overlap. Severity: low–medium.
- Step 27 names "cigar and pipe lighters", step 32 names "utility lighters", and step 17's note says "a ... lighter ... is filed by what it does". A Zippo or a disposable Bic therefore has two answers.
- A cannabis herb grinder is unnamed, so it falls to B5 "kitchen tools".
- A cigarette case holds many cigarettes, so it is not an S3 part. It may stop at step 17 as a personal accessory, where no branch fits, and then reach step 27. That works only by luck.
- Examples: #53, #54.
- Fix: covered by F19's list ("pocket lighters", "herb grinders", "cigarette cases"). In C8's branch, replace "matches, firelighters and utility lighters" with:
  > matches, firelighters, and long utility and candle lighters (pocket lighters are B9)

### E. B10 pet food and feed

**F21. Animal food is defined only as "pet food" where it matters, and farm feed meets C7 first.** Type: key-order trap / wording. Severity: medium.
- Step 3's lead says "food", not "food for people". Its note excludes only "pet food". So wild-bird seed, sunflower hearts and peanuts for birds, fat balls, fish food, hay and forage can be read as J5 or J4 groceries.
- Bulk cattle, poultry or horse feed is "made for agricultural production" (step 12, C7), which is tried before step 13. It escapes only if step 1's note is read as a direct jump (F18).
- Frozen feeder mice and chicks meet J1 "meat".
- Live feeders (mealworms, crickets) are rightly OUT as living animals, but this is not stated.
- Examples: #55–#58.
- Fix: in step 3's lead, "food for people" (already in F1's wording). In step 3's note, replace "pet food is B10" with:
  > food made for animals, kept or wild, is B10: pet food and treats, bird seed and fat balls, fish food, hay and forage, livestock and poultry feed, frozen feeder animals
- In step 12's note, add:
  > Animal feed in any quantity is B10.
- In step 13's list, replace "pet food and animal feed" with:
  > pet food and animal feed of every kind (including bird seed, hay and frozen feeder animals; live feeders are OUT)

### F. Boundary with the Culinary taxonomy, alcohol, cultures, files

**F22. The hand-off to Culinary assumes coverage that a dish taxonomy may not have.** Type: scope / wording. Severity: low–medium.
- Step 1 sends "bread and bakery, cakes, sweets and chocolate bars, snacks ... soft drinks, juices, bottled waters, kombucha" out with "which the Culinary taxonomy covers".
- A dish taxonomy rarely covers branded packaged products: crisps, chocolate bars, bottled water, energy drinks. Nothing here records what happens if Culinary lacks a kind, so such products can fall out of both taxonomies.
- The phrase "linked to the Culinary kind where one exists" is right, but it does not say which side owns the record when both describe the same thing (kimchi, smoked salmon, ham).
- Fix: in the scope paragraph, replace "Prepared foods and dishes are out: the Culinary taxonomy covers them." with:
  > Prepared foods and drinks (step 1) are out and left to the Culinary taxonomy; any packaged prepared kind that Culinary lacks is recorded in the review log, not filed here. A grocery that Culinary also describes (kimchi, smoked salmon, ham) is filed once here, as the product as bought, and Culinary links to it.

**F23. Alcohol edge cases are decided only by branch order or not at all.** Type: wording. Severity: low.
- Mirin, Shaoxing and cooking wines, Angostura bitters and vanilla extract reach J5 before J7 only by branch order. A reader may treat "wine, ... and other alcoholic drinks" as decisive instead.
- Alcohol-free beer and wine and non-alcoholic spirits are OUT. That is correct, but it is unstated.
- En primeur wine is a claim (OUT) until delivered.
- Examples: #44, #46, #47.
- Fix: add to step 3's note:
  > Wines and spirits made for cooking or flavouring (mirin, cooking wine, bitters, extracts) are J5. Alcohol-free beer, wine and spirits are prepared drinks (step 1). Wine or spirits bought but not yet delivered (en primeur) are a claim (step 1).

**F24. A living plant sold to eat: the step 3 and step 6 notes disagree.** Type: overlap. Severity: low.
- Step 3's note sends "a living plant in a pot" to C3, but step 6's note sends "microgreens sold to eat" to step 3. A living microgreen tray or a cress punnet still growing gets both answers.
- Yeast (J5) vs starter (C3) is handled well by "kept to grow or propagate", and should stay.
- Examples: #71, #72.
- Fix: replace step 6's note "fresh vegetables, herbs, sprouts and microgreens sold to eat are step 3" with:
  > cut vegetables, herbs, sprouts and microgreens sold to eat are step 3; a plant sold still growing in a pot, tray or mat is here even when sold to eat (potted basil, living microgreens)

**F25. The owner's own photos and home videos change category with the carrier.** Type: axis break (minor). Severity: low.
- Prints and home recordings of the owner's own life are F5 "personal records". The same photos in a cloud library are I2, filed with "digital artwork and photograph files".
- This follows the status-first design and is defensible, but it is unstated, so a stage-2 builder of F5 will reasonably claim the files.
- Examples: #18.
- Fix: add to I2's branch:
  > (Note: the owner's own photographs, home videos and scanned records held as files are here, not F5: the carrier decides.)

---

## Part 3 — Top five changes, in priority order

1. **Rewrite the food line: the step 1 prepared-food clause, the step 1 grocery note, and the step 3 lead (F1, with F4 and F6).** Use one closed definition of "prepared" (cooked or combined into a dish, baked good, confection, dessert, snack product or non-alcoholic drink), state that preserving or plainly cooking one ingredient does not make a food prepared, and make the step 3 lead admit exactly what the J branches name. This one change resolves most of the 20-plus food splits (#1, #5, #7, #29, #32, #35, #40–#42).
2. **Fix S1b so a note files directly at the step it names (F18).** Every new rule depends on step 1's notes. Without this, infant formula (step 2), farm feed (step 12), gift cards (step 5) and chewed plant products (step 3) are caught early.
3. **Narrow and structure I3, and draw the I1/I3 line (F10, F12, with F11 and F16).** OUT recurring services, utilities and telecom. List I3's four kinds of access (catalogue, hosted storage, shared place, curated delivery). Define I1 as a program or tool whose value is its function, with hosted storage, catalogues and play in I3, and a bundle rule. File delivered goods by what they are.
4. **Close the grocery gaps and fix the live-seafood scope break (F2, F3, F8).** Frozen and dried produce, seaweed, cereals, spreads, plant milks and meat alternatives, and live oysters, mussels, crabs and lobsters as J2.
5. **Rewrite step 27 (B9) by substance and effect, in any form, and name animal food as B10 everywhere it is tested (F19, F21).** Pouches, edibles, tinctures, CBD, betel, khat and kratom go to B9; pocket lighters and grinders are named; bird seed, hay, fish food and farm feed are B10, ahead of J5 and C7.

Next tier, all medium: F5 (product filed by what it is, not what it contains; hamper rule), F7 (formula and sports nutrition in any form), F13 (all stored value and in-game currency OUT), F14 (game passes and DLC), F15 (define "genre" and the allowed facets).

Note on testing: none of these wordings has been through a blind placement round. The 72 examples in Part 1 are a ready test set for the next round. With all 25 fixes applied, each of the 72 is meant to decide to one answer; the next round should check that.
