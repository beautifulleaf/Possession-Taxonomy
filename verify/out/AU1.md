# AU1 — Cold audit of CATEGORIES_R1.md (top level only)

Source audited: `audit/CATEGORIES_R1.md` (Top-Level Categories v0). No other repository file was opened. Offline; no web, no git.

Conventions: "Step n" = placement key step n. "→ X" = where the key as written sends the object. Severity reflects how many common objects are misfiled and how hard the fix becomes once stage 2 builds on the top level.

---

## Findings

### 1. Step 2 "protect" captures most protective gear, armour, sport helmets and safety objects
- **Type:** Key-order trap / Overlap / Wording
- **Severity:** High
- **Examples:** cycling helmet, motorcycle helmet, riding hat (E2 claims "protective gear made for one sport"; step 2 runs first → H2); bulletproof vest, stab vest, medieval armour (step 8 claims "armour of any use"; step 2 first → H2); hi-vis vest, hard hat, safety boots, welding mask (A1 claims "protective clothing"; → H2); sunglasses (A4 says "sunglasses stay here"; they protect the eyes → H2); life jacket (E2 water sports → H2); child car seat (S3 example sends it to Vehicles; step 2 precedes step 6 → H2); condoms (H3 → H2); sunscreen, insect repellent (H1 → H2); smoke alarm, fire extinguisher, air purifier, mosquito net (B6/B4 → H2 on a literal reading).
- **Also "monitor":** fitness tracker, smartwatch with heart-rate or ECG, smart ring, bathroom scale. D2 lists fitness trackers and smartwatches, but step 2 runs before steps 11/15 → H2.
- **Problem:** Step 2 is the first function step, and "protect … the body's health or function" covers nearly everything worn for safety. Seven category texts are contradicted by it.
- **Fix (replace step 2):** "2. Made to **diagnose, treat, monitor or compensate for an illness, injury or disability**, or for first aid: medical devices and monitors, medicines and medical supplies, mobility and assistive aids (including ones installed in a home, such as a stairlift), hearing aids, spectacles and contact lenses that correct vision, first-aid kits? **H2 Health, Medical & Mobility**. (Protective gear goes by what it is: gear made for one sport → E2; armour → E4; other protective garments → A1, footwear → A2, eyewear → A4. A device that counts steps or heart rate for fitness is not a medical monitor: step 15.)"

### 2. Step 15 sends music electronics to D3, and has no exit when no branch fits
- **Type:** Overlap / Key-order trap / Wording
- **Severity:** High
- **Examples:** guitar amplifier, effects pedal, mixing desk, studio monitor speakers, microphone, audio interface, DJ controller (step 15, branch "audio equipment … speakers" → D3, although E3 lists "amplifiers, effects, DJ and studio equipment" and E3's own precedence keeps only "hi-fi for listening" in D3); digital piano, synthesiser, drum machine, electronic drum kit (powered electronic devices; no branch fits).
- **No-exit cases:** power bank, electric torch, heated jacket and light-up trainers (step 11 sends any powered worn or carried device to 15), vape (also sent from step 11), electronic calculator (C5 lists it), label maker, shredder, GPS unit, robot toy, RC car, pinball machine. The step's question is answered *yes*, so S1 ("stop at the first yes") stops the key with no category.
- **Problem:** Step 15 runs before step 16, and its trigger ("a powered electronic device") is broader than its branches.
- **Fix:** (a) Move the current step 16 (music) so it runs **before** the current step 15. (b) Replace the step 15 lead line with: "15. A **powered electronic device whose main function is computing, communication, picture-taking, gaming, or playing or receiving sound and pictures**:" (c) Add as the last line of step 15: "(A powered device that fits none of these branches is not filed here: continue to step 16.)" (d) Add a general rule after S1: "**S1a Branches.** When a step's lead question is *yes* but none of its branches fits, the answer is *no*: continue to the next step."

### 3. Step 15 branch order: tablets and phones are "computers"; earbuds are "wearables"
- **Type:** Wording / Overlap
- **Severity:** Medium
- **Examples:** iPad, Android tablet, 2-in-1 convertible laptop, smartphone (all general-purpose computers → branch 1, D1, before branch 2, D2 is tested); wireless earbuds and over-ear Bluetooth headphones (worn → "wearable", branch 2, D2, although D3 lists "headphones and earbuds").
- **Fix:** Branch 1: "a **desktop, laptop or convertible computer**, its components, peripherals, storage or networking? **D1**". Branch 2: "a **phone, tablet, e-reader, smartwatch, fitness tracker or smart glasses**? **D2**". Branch 3: add "headphones and earbuds of every kind (they are D3, not wearables)".

### 4. Step 11 "or other personal accessory carried" swallows portable objects
- **Type:** Key-order trap / Wording
- **Severity:** High
- **Examples:** pocket knife, multi-tool (E4 precedence sends utility knives to C1 → A4); lighter, cigarette case (B7 → A4); water bottle, vacuum flask, lunchbox (B3 → A4); pen, pocket notebook (C5 → A4); hiking backpack, camping water bladder (E2 → A4 as "bag"); hand-held torch (no-exit case of finding 2, or A4); walking stick (A4 lists it, but step 2 "mobility aids" takes it first → H2).
- **Problem:** Almost anything small is "carried". The intended category is personal accessories by type, not portable things.
- **Fix (replace the last branch of step 11):** "- a **bag, luggage, wallet or purse, umbrella, sunglasses or non-corrective eyewear, hand fan, keyring, or fashion cane**? **A4 Bags & Accessories** (an object that is only portable, such as a pocket knife, lighter, pen or water bottle, is filed by what it does)." In A4, replace "walking sticks" with "fashion canes (walking aids made for support are H2)".

### 5. Step 11 "ornament worn on the body or hair" captures cosmetics, and the jump to step 15 captures heated garments
- **Type:** Key-order trap / Overlap
- **Severity:** Medium
- **Examples:** false eyelashes, press-on nails, hair extensions, body glitter, temporary tattoos (H1 cosmetics; step 11 runs before step 12 → A3); wig (headwear A1, ornament A3, or H1?); heated jacket, heated gloves, LED costume (A1 says "heated or lit garments stay here", but step 11's first line sends every powered worn device to step 15).
- **Fix:** Step 11 first line: "A **powered electronic device** worn or carried whose main function is computing, communication, sensing or media (smartphone, smartwatch, fitness tracker, earbuds, e-reader)? Go to step 15. (A garment, shoe or accessory with heating or lights is not such a device: continue below.)" Third branch: "an **ornament** worn on the body, hair or clothing (rings, necklaces, body jewellery, brooches, hair ornaments, cufflinks), or a watch? **A3**". Add to step 12: "including cosmetics applied to or attached to the body (false eyelashes, artificial nails, hair extensions, wigs and hairpieces)".

### 6. Step 3 "structure" and "fixed into one" take objects that other categories list
- **Type:** Overlap / Axis break (setting) / Key-order trap
- **Severity:** High
- **Examples:** greenhouse, polytunnel, potting shed (C2 lists greenhouses; step 3 "structure" / G2 "outbuildings" run first → G2); kennel, stable, chicken coop, hutch, bird house (B8 "housing" → G2); in-ground swing set, climbing frame, playhouse, treehouse (E1 "play equipment" → G2); built-in oven, integrated dishwasher, hard-wired smoke alarm, plumbed-in water softener, ceiling light fitting, fitted bathroom cabinet (B4/B6/B5 → G2), while the same freestanding machine is B4; built-in safe (B6 → G2); rooftop solar panels, wall-box EV charger, garden fence, flagpole.
- **Problem:** "Fixed into one so that it passes with it" is a conveyancing (legal) test, not a function test. It splits one object type by how it is installed: a dishwasher is B4 or G2 depending on the kitchen. That is the "setting" modifier that S4 rules out. "Structure" with no limit takes every small outbuilding whatever it is for.
- **Fix (replace step 3):** "3. **Land, or a building or other permanent structure made to be occupied, entered or enclosed** (house, flat, garage, barn, shed, garden room, carport), or a **building element** made to form part of one (walls, roofs, windows, doors, stairs, floors, fitted cabinetry, built-in baths and sanitaryware, fixed plumbing and wiring, in-ground pools); a vehicle or vessel made to **stay in one place as a dwelling** (houseboat, static caravan, tiny house on wheels); a burial plot? **G2 Property & Structures**. (A machine, device, lamp, safe or alarm that is installed keeps its own category: 'built-in' is a modifier. Structures made for growing plants (greenhouses, polytunnels) are C2; structures made for keeping animals (kennels, coops, stables) are B8; play structures are E1.)" In Appendix A add: "installation (freestanding, built-in, fitted)".

### 7. Timeshare (and burial plot) conflicts with the step 1 rule on rights
- **Type:** Scope / Rule contradiction
- **Severity:** Medium
- **Examples:** timeshare week (a contractual right of use), burial plot (in many places a right of interment, not freehold land), season ticket (OUT), festival pass (OUT), software licence (IN at I1), domain name (a renewable registration, close to a subscription, IN at I1), shares, bonds, insurance policies, patents and trademarks, air miles (none mentioned).
- **Problem:** Step 1 removes "a right to attend or travel (ticket)", "membership" and "subscription", but G2 and I1 accept rights of use. Financial instruments and intellectual property are not dealt with at all, so a share certificate goes to F5 by its paper while the shareholding has no rule.
- **Fix:** Add to step 1: "a **right, claim or financial instrument** in itself (ticket or pass, licence, membership, timeshare, share, bond, insurance policy, loyalty points, intellectual property). Their physical tokens are objects: a printed certificate or kept ticket is F5." Delete "timeshares" from step 3 and G2. Keep the burial plot only as "a burial plot held as land" and send "a right of burial" to OUT. For I1 see finding 8.

### 8. I1 Digital Goods mixes files, registrations, ledger tokens and account entries; step 1 makes most of it OUT
- **Type:** Scope / Rule contradiction / Granularity
- **Severity:** Medium
- **Examples:** e-book bought on a reading platform, purchased film on a streaming store, in-game skin (each exists only as an entitlement inside an **account**, which step 1 makes OUT); domain name (a registration); NFT (a ledger token, while the cryptocurrency holding beside it is OUT); a downloaded font file or a DRM-free MP3 (true data files); scanned personal photographs and digital letters (data, so step 4 → I1, not F5); a digital painting file (I1, not F2).
- **Problem:** The step 1 / step 4 line between "account" and "data" is not defined. I1 is also the only category set by mode of existence, a second axis that the file never declares (finding 19).
- **Fix (replace step 4):** "4. Exists **only as data** and is held by the owner as a **file, licence entitlement or registered token** (e-book, digital music or film, software, font, digital artwork or photograph file, in-game item, domain name, NFT)? **I1 Digital Goods**. (The account or platform it sits in is OUT under step 1; the item held in it is in. Fungible money tokens are OUT.)" Add to "How to read": "Steps 1 to 6 sort by what kind of thing the object is (outside scope, body-related, real property, data, living plant, part). They come before the function steps on purpose."

### 9. Step 13 "ceremony … festival and rite objects" takes secular seasonal and party goods
- **Type:** Overlap / Key-order trap / Wording
- **Severity:** High
- **Examples:** Christmas tree ornaments, artificial Christmas tree, Halloween decorations, Easter baskets, birthday candles, party balloons, wedding cake topper, graduation tassel, Chinese New Year lanterns (B5 lists "seasonal decorations"; step 13 runs before step 24 → F4); trophies, ceremonial mace, gavel, national flag (F4? F5? no rule); cremation urn, coffin (F4, unstated).
- **Problem:** "Ceremony" and "festival" reach into all secular celebration, so B5's "seasonal decorations" can never be reached. The religious object category turns into a holiday-goods category.
- **Fix (replace step 13):** "13. Made for **religious or spiritual practice**, or for a **rite of passage or funeral**, and not worn: altars, shrines, icons, prayer beads, ritual vessels and implements, incense burners, religious festival objects (menorah, Advent wreath, diya), cremation urns and grave goods? **F4 Religious & Ceremonial Objects**. (Secular seasonal and party decorations, such as Christmas baubles, Halloween props and balloons, are B5.)"

### 10. Step 14 "records or remembers" is too broad and runs before art, media and collectibles
- **Type:** Key-order trap / Overlap / Axis break (motive)
- **Severity:** High
- **Examples:** vinyl records, released films on VHS or DVD (a "record" that "records", so a literal reader sends them to F5 rather than F1); a commissioned oil portrait of a grandparent ("remembers", → F5 rather than F2); souvenirs, memorial plaques, baby's first shoe in a box (S4 makes memorabilia a motive, but step 14 "remembers" files by that motive); military campaign medals and sports medals awarded (they "certify", → F5, while F3 lists medals); blank diaries and notebooks (C5 → F5?); a framed family photo on the wall vs the same print in an album (step 14 "personal photographs" vs F2 "photographs for display": one object type split by where it is shown, a setting/motive split).
- **Fix (replace step 14):** "14. A **document issued to prove** identity, status, ownership or achievement (passport, licence, certificate, deed, diploma, award certificate), or a **personal record made by or for its owner and household** on paper or another physical carrier (letters, written diaries, photo albums, personal photographic prints, home recordings, scrapbooks)? **F5 Documents & Personal Records**. (Published works are F1. Pictures made as artworks, posters and fine-art photographs are F2. Souvenirs and keepsakes are filed by what they are (S5). Blank notebooks and diaries are C5.)" In F2, replace "photographs for display" with "photographs made as artworks or posters (personal photographs are F5 however they are shown)".

### 11. Physical money has no home; F3 mixes money, postage, awards and bullion under a "made to be collected" test that they fail
- **Type:** Gap / Scope / Axis break (motive: investment)
- **Severity:** High
- **Examples:** banknotes and coins in a wallet or cash box (step 1 removes "money held as a balance, stored value or currency holding", which a careful reader can take to cover physical cash or not; if they are in, circulating coins were made for spending, so they fail step 18's "made to be collected … and not used otherwise" and fall to step 27, though they are not tools); definitive postage stamps (made to be *used* for postage, so they fail step 18 → no home); gold bars and bullion coins (made as a store of value; "investment" is listed in S4 and Appendix A as a motive, yet bullion fixes F3); military decorations, Olympic medals, trophies (awarded, not "collected in a series"; worn decorations reach step 11 first → A3; trophies → B5 decor?); enamel pins "made for collecting" (pinned on clothing → step 11 → A3, so F3's "collector pins" never fire).
- **Problem:** The F3 test describes made-to-collect goods (commemorative issues, collector series). The list adds three other types (money, postage, awards), so the key and the list disagree.
- **Fix (replace step 18):** "18. **Money, postage or an award in physical form, or an object made only to be collected**: coins, banknotes and bullion (in circulation or not), postage stamps and postal stationery, medals, decorations and trophies, tokens, non-game trading cards, and series made for collecting (collector pins, commemorative issues)? **F3 Coins, Stamps, Medals & Collectibles**." Clarify step 1: "money held as an account balance, stored value or digital currency (bank balance, gift-card value, cryptocurrency). Physical coins and notes are objects: step 18." Move step 18 to run **before** step 11, or add to step 11: "(medals, decorations and pins made for collecting are F3 even when worn)."

### 12. Step 23 files food and drink by motive ("kept as a stock for ageing, collecting or display")
- **Type:** Axis break (motive) / Rule contradiction / Scope
- **Severity:** High
- **Examples:** a bottle of Bordeaux opened tonight (OUT, food or drink) and the same wine laid down for ten years (IN, B7); a pantry of tinned food or an emergency food store (OUT), a cellar of whisky (IN); aged pu-erh tea (IN), ordinary tea (OUT); cigars (IN, though consumed like food); humidor and wine rack (S3 says storage for a thing is not a part, so a humidor is B1 or B6, yet the category is named "Humidor").
- **Problem:** S5 says "test the object, not the motive", and S4 and Appendix A list collecting and investment as modifiers. Step 23 makes them the test. B7's precedence ("the drink as drink belongs to the Culinary taxonomy") also gives wine two homes, against S1.
- **Fix:** Make all food and drink OUT, with no stock exception. Step 1: "food or drink, whether for now or kept as a stock (the Culinary taxonomy covers it)". Replace step 23: "23. **Tobacco and other smoking or vaping products, and the implements for smoking or vaping** (cigars, pipe tobacco, pipes, hookahs, lighters, vapes, ashtrays, cigar cutters)? **B7 Tobacco & Smoking**." Put cellar and humidor storage where S3 already puts it: wine racks and humidors → B1 (or B6), wine fridges → B4, decanters → B3.

### 13. Step 8 "hunt or defend" and "of any use" catch fishing, pest control, hunting clothing and toys
- **Type:** Wording / Key-order trap / Axis break (form, not function)
- **Severity:** Medium
- **Examples:** fishing rod and reel (fishing is hunting fish; step 8 runs before step 21 → E4, though E2 lists fishing); hunting decoy, game call, tree stand, camouflage jacket ("made to hunt" → E4 rather than E2/A1); mousetrap, fly swatter ("made to injure … animals" → E4); burglar alarm, door chain ("defend" → E4); foam toy sword, toy bow and arrows (a "sword … or bow … of any use" → E4, not E1); stage-prop or decorative wall katana (E4 by shape; the rule follows form rather than function, against the axis rule).
- **Fix (replace step 8):** "8. **A weapon**: made to injure or kill a person or animal by striking, cutting, shooting or firing (firearms, air guns, bows and crossbows, swords and fighting or hunting knives, martial-arts weapons, pepper spray) or for target shooting or fencing with such a weapon; or **armour** made to protect against such weapons; and their ammunition? **E4 Weapons & Armour**. (Toy and foam replicas are E1; decorative and stage replicas that cannot injure are B5; fishing tackle and hunting accessories other than the weapon are E2; pest traps are B6; kitchen and utility knives are not weapons.)"

### 14. Step 9 propulsion clause excludes towed and animal-drawn vehicles, and "carry" takes in carts, mowers and boards
- **Type:** Wording / Key-order trap / Overlap
- **Severity:** High
- **Examples:** trailer, horse trailer, horse-drawn carriage, dog sled, sailing dinghy (not "under its own or human power", yet trailers are listed in step 9 and G1); wheelbarrow, sack truck, garden cart, shopping trolley (carry goods by moving, human power → G1, not C2/C1/B6); wheeled suitcase (→ G1, not A4); ride-on mower, garden tractor, forklift, excavator (carry their driver → G1, not C2/C1); skateboard, sledge, roller skates, surfboard, kayak (carry a person → G1 or E2?); ride-on toy car, balance bike, tricycle (→ G1 or E1?); baby sling and carrier (carries a person; prams and strollers are named → G1?).
- **Fix (replace step 9):** "9. Made **mainly to transport people or goods from place to place** on land, water, rail, snow or air, however moved (engine, motor, muscle, wind, animal or tow): cars, motorcycles, bicycles and e-bikes, e-scooters, boats and sailing craft, aircraft, trailers and caravans for touring, horse-drawn vehicles, prams and strollers? **G1 Vehicles**. (A machine that only carries its operator while it does other work, such as a ride-on mower, tractor or excavator, goes by that work. Hand carts and wheelbarrows are C2 or C1. Wheeled luggage is A4. Boards, skates, skis and sledges made for a sport are E2. Ride-on toys and balance bikes for play are E1. Baby carriers and slings are A4.)"

### 15. S3 / step 6 (parts follow the whole) conflicts with C2, A4, B6 and the category texts
- **Type:** Rule contradiction / Wording
- **Severity:** Medium
- **Examples:** plant pots, plant food, grow lights, plant stakes (they work only with plants, so S3 → C3, while C2 lists "planters and pots"); phone case, camera bag, guitar case, gun case, golf bag (a "part" that only works with one kind of object, or "storage for a thing"? S3 says storage is not a part, so they go to A4 or B6; a careful reader can do either); spectacle frames (A4 says frames "stay here", but they only work as spectacles → S3 → H2); bike lock (S3 → G1, or B6 "locks"); buttons, zips (they work only with garments → A1, though they are sewing supplies, C4); child car seat (S3 example → G1, but step 2 runs first → H2, finding 1); USB cable, charger, AA batteries, extension lead (they work with many kinds → no S3 home and no other step: finding 17).
- **Fix (replace S3):** "**S3 Parts follow the whole.** A component, attachment, accessory or consumable **made to be fitted to or used up in one kind of object** goes to that object's category (graphics card → Computers, lens → Cameras, guitar strings → Musical Instruments, printer ink → Computers, child car seat → Vehicles). **Cases, bags, covers and stands made to hold, carry or display one kind of object are parts too** (phone case → Phones; guitar case → Musical Instruments; golf bag → Sports). **Not parts:** furniture and storage made for a class of things (bookcase → Furniture; wine fridge → Appliances; safe → Household Goods), and **anything for growing plants** (pots, compost, plant food, grow lights → Garden & Grounds)." Move step 6 so that it runs **before** step 2, or add to step 2: "(a part that only works with a non-medical object follows that object: step 6)". Delete "frames … stay here" from A4 (see finding 25).

### 16. Step 24 gates six categories on a setting ("made for the home"), and B4 splits tasks by power source
- **Type:** Axis break (setting; power source as a material/technology modifier) / Granularity
- **Severity:** High
- **Examples (setting gate):** office chair, office desk, filing cabinet bought for an office (not "made for the home" → steps 25 to 27 → C1 Tools, or no home); camping stove and cool box (E2, acceptable), but a patio heater or garden parasol (home? outdoors?); caravan crockery; a stepladder or ironing board (made for the home, yet no branch fits → no exit, as in finding 2).
- **Examples (power split):** manual vs electric coffee grinder, hand whisk vs stand mixer, manual vs electric can opener, French press vs drip coffee maker (B3 vs B4); carpet sweeper or broom vs vacuum cleaner, clothes airer vs tumble dryer, mop vs steam mop (B6 vs B4); hand fan (A4) vs desk fan (B4); oil lamp vs electric lamp (both B5, so power source is *not* applied consistently).
- **Problem:** S4 lists "setting" as a modifier, yet step 24's lead line is a setting test. The B4/B3/B6 boundary sorts each household task by power source, so one task (making coffee, cleaning floors, drying laundry) is split across categories. Those categories will need the same inner structure twice in stage 2.
- **Fix (minimum):** Replace the lead line "24. Made for the **home**:" with "24. Made for a **household task, furnishing or domestic use**, wherever it is used (home, office, garden, caravan or boat):", and add "(If none of these branches fits, continue to step 25.)"
- **Fix (preferred; split by task, not size):** Reorganise B3, B4 and B6 by the task the object is made for, with power source as a modifier: **B3 Kitchen & Dining** (cookware, food preparation tools and machines, cooking appliances, refrigeration, dishwashers, tableware, glassware, food storage); **B4 Cleaning & Laundry** (powered or not: vacuum cleaners, brooms, mops, washing machines, irons, airers, cleaning products); **B6 Storage & Organisation** (boxes, baskets, shelving inserts, hooks); **B9 Climate & Water** (heaters, fans, air conditioners, dehumidifiers, air purifiers, water heaters, softeners and filters); **B10 Home Safety & Security** (locks, safes, smoke and CO alarms, extinguishers, security cameras, alarm systems). The branch text would read, for example: "- made to **prepare, cook, cool, store or serve food and drink**, powered or not? **B3 Kitchen & Dining**".

### 17. Step 27 is not a catch-all: everything that is not "a tool, instrument or machine for work" has no home
- **Type:** Gap
- **Severity:** High
- **Examples (natural objects, not made for anything):** fossils, minerals, loose gemstones, meteorites, seashells, pebbles, driftwood, antlers, pinned insects, taxidermy mounts, skulls and bones, hides. The key is built on "made to do", so these pass every step and fail step 27.
- **Examples (materials and generic consumables):** timber, bricks, tiles and paint kept for a project; nails, screws, bolts; glue and duct tape; AA batteries, chargers, USB and HDMI cables, extension leads, power banks; firewood, charcoal, propane cylinders, heating oil, jerry can of petrol; cleaning chemicals; bin bags, toilet paper.
- **Examples (other gaps):** flags and banners; globes, anatomical models, chemistry and lab glassware, weather stations; emergency and survival kits; picture frames (empty); signage; mannequins; party supplies (piñata → E1, confetti?); cremation ashes and other human remains (scope silent).
- **Fix:** (a) Replace step 27: "27. Otherwise a **tool, instrument or machine made to cut, shape, join, measure, test, lift, power or repair**, or **materials, hardware and fasteners** for building and repair (hand and power tools, workshop machines, ladders, measuring and testing instruments, generators, timber, fixings, adhesives, farm and trade machinery)? **C1 Tools, Machinery & Materials**." (b) Add a terminal step: "28. **None of the above. Hold in X0 Unplaced** and list the object in the stage-1 review log; X0 must be empty before stage 2 starts." (c) Add a category **F6 Natural History & Specimens**, "natural objects and specimens kept as found or prepared: minerals, fossils, gemstones (unset), shells, meteorites, skeletal and taxidermy specimens, herbarium sheets", with a key step placed before step 17: "Made by nature, not by people, and kept as found or prepared as a specimen? **F6**" (a split for function, since its inner structure is natural-history classification, not design). (d) Add to step 15 or D1: "power supplies, chargers, cables, batteries and power banks for electronic devices of any kind → D1" (or a new branch "electronic accessories").

### 18. Step 22 "as a craft or hobby" vs step 27 "for work" files tools by the owner's motive
- **Type:** Axis break (motive / user) / Overlap
- **Severity:** Medium
- **Examples:** wood-carving chisels, a small lathe, a scroll saw, a soldering iron, a pottery wheel, a leather punch, a jeweller's saw. Each is "for making things as a craft or hobby" (C4) when an amateur owns it and a "tool … for work" (C1) when a tradesperson does. A carpenter and a hobby woodworker own the same chisel. Also artists' pencils (C4) vs office pencils (C5) (step 22 vs step 25: "art supplies" vs "drawing on paper").
- **Problem:** "Hobby" and "work" describe the user and motive, which S4 ("user", "motive") and S5 rule out.
- **Fix (replace step 22):** "22. Made for **textile, fibre, paper, bead, clay, paint and other decorative crafts**: sewing and embroidery machines, knitting and needlework tools, yarn, fabric and notions, artists' paints, brushes, canvases and easels, model kits, beading, scrapbooking and paper-craft supplies, pottery tools and kilns? **C4 Craft & Art Supplies**. (Tools for shaping wood, metal and stone, and for electronics work, are C1 whoever uses them.)" In step 27 replace "for work" with the function wording in finding 17(a). In step 25 replace "writing, drawing on paper" with "writing, everyday drawing and desk work (artists' drawing materials are C4)".

### 19. The framework's own rules contradict each other on the axis; the non-function steps are not declared
- **Type:** Axis break / Rule contradiction
- **Severity:** Medium
- **Examples:** e-book (I1) vs paper book (F1): same designed function, split by mode of existence; digital photo (I1) vs print (F5); living plant (C3) vs artificial plant (B5): split by being alive; built-in vs freestanding oven (G2 vs B4: setting); wine to drink (OUT) vs wine kept (B7: motive); hobby vs trade chisel (C4 vs C1: user); B2 Home Textiles and A1 "garments and textile accessories" (named by material, which Appendix A lists as a modifier: a leather belt, rubber rain hat or metal hard hat is not a "textile accessory").
- **Problem:** The header states "One axis at the top: what the object is made to do", but steps 1 to 6 sort by something else. Several of those choices are defensible, but only if they are declared. Undeclared, each one reads as a breach of S4 and S5.
- **Fix:** Replace the axis paragraph's first sentence with: "**One axis at the top, after a short status filter.** Steps 1 to 6 first sort objects by status: outside scope, health-related, real property, data only, living plant, or part of another object. From step 7 on, an object is filed only by its primary designed function: what it is made to do, or to be, for its owner." In A1, replace "garments and textile accessories" with "garments and wearable accessories of any material". Rename B2 to "**B2 Soft Furnishings**: made to cover, soften or dress beds, floors, windows, seats and tables (bedding, rugs, curtains, cushions, throws, table linen), and towels for drying the body". Finding 20 settles the towel boundary with H1. Fix the setting, motive and user cases as in findings 6, 12 and 18.

### 20. Step 12 "used on the body" takes towels and bath textiles away from B2, and uses a use test
- **Type:** Overlap / Wording (use vs made)
- **Severity:** Low
- **Examples:** bath towel, hand towel, flannel, bath mat, bathrobe (robe → A1 first; towels "used on the body for hygiene" → H1 although B2 lists towels); a hand mirror or make-up mirror (H1 or B5?); massage gun and personal massager (H1, or H2 "treat"?).
- **Fix:** Step 12: "**Made to be used on the body** for grooming, hygiene, cosmetics or fragrance, including powered tools such as hair dryers, shavers and electric toothbrushes, and grooming mirrors? **H1**". Then choose one home for towels and state it in step 12: "(Towels of every kind for drying the body are B2, not H1; tea towels are B3.)" That keeps all body towels in B2, whichever setting they are used in (bath, beach, gym), so towels are not split by setting. Massagers: "massagers for comfort are H1; those made to treat a condition are H2."

### 21. Steps 20 and 21: play vs sport can be read two ways; "one sport" and "outdoor pursuit" are undefined
- **Type:** Wording / Overlap / Axis break (setting)
- **Severity:** Medium
- **Examples (E1 vs E2):** pool or snooker table, darts board, table-tennis table, table football, chess clock, garden trampoline, kite, frisbee, children's football, toy bow (see finding 13), toboggan. Step 20 "play … play equipment" runs first, so a reader can send all of them to E1, or send sport-like ones to E2 by reading "play" narrowly.
- **Examples ("made for one sport"):** running shoes vs "sneakers stay here" (A2); hiking boots (is hiking "one sport"?); swimsuits, yoga leggings, rash vests; padded cycling shorts (clear); golf umbrella (A4 or E2?).
- **Setting:** "outdoor pursuit" and the name "Sports, Fitness & Outdoor" use "outdoor", a setting that S4 and Appendix A list as a modifier; camping chairs and tables (E2) vs garden chairs (B1, "indoor or out").
- **Fix:** Step 20: "Made for **play or for games**: toys, dolls, figures, puzzles, board, card, dice and tile games (including trading card games), tabletop and coin-operated games, model railways, **children's play equipment** (swings, slides, climbing frames, playhouses, trampolines made for play), gambling equipment? **E1**." Step 21: "Made for a **sport, physical exercise, or an outdoor recreation such as camping, hiking, climbing, angling or snow sports**: balls, rackets, cues, darts and boards, fitness machines, tents, sleeping bags, camp furniture and stoves, climbing, fishing, winter and water sports gear, and garments, footwear and protective gear made for one sport or one of these recreations? **E2**." Add to step 11: "(**Made for one sport** means designed for that sport's specific demands: football boots, ski boots, swimming costumes, padded cycling shorts. General-purpose trainers, leggings and outdoor jackets stay A1/A2.)" Rename E2 "**Sports, Fitness & Recreation**".

### 22. Step 17 vs B5: art vs figurine is split by production mode and value
- **Type:** Axis break (maker, value, edition) / Wording
- **Severity:** Medium
- **Examples:** a porcelain figurine (B5 "mass-made figurines") vs a hand-made ceramic figure (F2 "sculpture made as an artwork"); a mass-printed IKEA canvas print (step 17 "prints and posters" → F2, which shows F2 is not really a unique-artwork class); a limited-edition bronze vs an open-edition resin cast of the same model; decorative wall plates (picture? tableware? collectible?); wall decals.
- **Problem:** "Mass-made" vs "made as an artwork" turns on maker, edition and price tier, all modifiers under S4 and Appendix A ("edition (limited, signed)"). Step 17 and B5 also both claim a three-dimensional figure made to be looked at.
- **Fix:** Use form for the boundary, not prestige. Step 17: "Made to be **looked at as a picture**, on a flat or hung surface (paintings, drawings, prints, posters, art photographs, calligraphy, tapestries and textile hangings), **or as free-standing sculpture**, whatever the edition or price? **F2 Art**." B5: "ornaments made to decorate a surface or room that are not pictures or sculpture: vases, bowls, decorative objects, candles, seasonal decorations". Add: "Figurines are F2 (sculpture); edition, maker and price are modifiers." If the project prefers figurines in B5, then define F2 as "pictures only" and send all sculpture to B5. Either way, use one test.

### 23. "Smart-home" in D3 is a technology modifier, not a function
- **Type:** Axis break / Overlap / Granularity
- **Severity:** Medium
- **Examples:** smart lock (B6 "locks" vs D3), smart thermostat (B4 "climate" vs D3), smart light bulb (B5 by S3 vs D3), smart plug, smart smoke alarm (B6 vs D3), robot vacuum (step 15's note sends household machines to step 24, but it is also a "smart-home device"), robot mower (C2 vs D3), video doorbell and security camera (B6 precedence: "networked cameras are D3").
- **Problem:** Being connected is a feature that any household object can have. Filing by it puts the same lock in two places and makes D3 hold two unrelated families (audio-visual and building control), which will need different structures in stage 2.
- **Fix:** In step 15 branch 3, replace "smart-home or home-security device" with "smart speaker, voice assistant or smart-home hub". Add to step 15: "(A connected version of a household object, such as a smart lock, thermostat, bulb, plug, alarm, camera or robot vacuum, is filed by its task: step 24; connectivity is a modifier.)" Rename D3 "**Audio & Video**". Add "connectivity (smart, connected)" to Appendix A.

### 24. D4 "Cameras & Optics" groups by technology (lenses), and scientific instruments are scattered
- **Type:** Axis break (technology/material) / Granularity / Wording
- **Severity:** Medium
- **Examples:** binoculars, opera glasses, rifle scope (S3 → E4), spotting scope, telescope, microscope, magnifying glass (H2 vision aid? C5? D4?), loupe; also weather station, thermometer, barometer, globe, chemistry set, lab glassware, compass (C1 "measuring instruments", E2, or no home).
- **Wording problem:** step 15's lead question is "a powered electronic device", but its D4 branch says "non-powered optics too". A non-powered pair of binoculars answers *no* at step 15 and never reaches the branch, so it goes on to step 27 (C1) or nowhere.
- **Fix:** Keep D4 as **Cameras & Photography** (cameras, lenses, flashes and lighting, tripods, film, darkroom kit, drones made for filming; powered or not). Create **C6 Optical & Scientific Instruments**: "made to observe, magnify or measure natural phenomena: binoculars, telescopes, microscopes, magnifiers, weather instruments, laboratory and science-education equipment, globes and orreries". Key step placed before step 15: "Made to **observe, magnify or measure** things or natural phenomena (binoculars, telescopes, microscopes, magnifiers, weather and lab instruments)? **C6**". This is a split for function: photography and observation differ in their inner structure. Make C1 "measuring instruments" read "measuring and testing tools for building and trade work (tape measures, levels, multimeters)".

### 25. Spectacles are split between H2 and A4, and the A4 rule contradicts S3
- **Type:** Rule contradiction / Overlap
- **Severity:** Low
- **Examples:** prescription glasses (step 2 → H2), their frames (A4: "frames … stay here", but S3 sends a part that only works with spectacles to the whole), prescription sunglasses (H2 or A4?), reading glasses from a chemist (H2), blue-light glasses with plain lenses (A4).
- **Fix:** A4 precedence: "Spectacles and contact lenses that correct vision, whole or as frames and lenses, are H2. Sunglasses and eyewear without corrective lenses are A4. Prescription sunglasses are H2."

### 26. Religious objects: the worn/not-worn test files one object type by how it is used
- **Type:** Axis break (use/motive) / Gap
- **Severity:** Low
- **Examples:** a mala or rosary worn on the wrist (A3) vs kept on a shrine (F4), the same object; tefillin (worn, not a garment or ornament → A4 "other accessory"); amulets and talismans (A3 or F4?); prayer shawl (A1, acceptable); incense and anointing oil (F4 vs H1 "fragrance").
- **Fix:** F4 precedence: "Prayer beads, tefillin, amulets and other objects made for religious practice are F4 **whether worn or not**. Religious dress and vestments are A1. Jewellery made in a religious form (a cross pendant) is A3." Move step 13 to run before step 11, with the wording in finding 9 but without "and not worn", and add to it "(religious dress and vestments are A1; religious-form jewellery is A3)."

### 27. Step 7 "sexual stimulation or restraint" can be read as any restraint
- **Type:** Wording
- **Severity:** Low
- **Examples:** police-style handcuffs, child safety harness, dog muzzle (B8 first), straitjacket (a reader can take "restraint" without "sexual"); fetish garments (step 7 runs before step 11, so a latex catsuit made for sexual use → H3, but the parenthetical says "other garments stay Clothing"); condoms (H3 or H2? see finding 1).
- **Fix:** "7. Made for **sexual stimulation**, or **for restraint during sexual activity**? **H3 Adult Objects**. (Garments of every kind, including lingerie and fetish wear, are A1; contraceptives are H2.)"

### 28. Step 1 OUT rules: "food or drink eaten as such", "body modification" and "living animal" settle edge cases badly
- **Type:** Scope / Wording
- **Severity:** Medium
- **Examples (food):** vitamins, supplements, cough syrup, baby formula (food eaten as such → OUT at step 1, or a medicine that "treats" → H2? Step 1 runs first, so the reader's view of "food" decides); pet food, hay, bird seed (eaten, though by animals → OUT? or a consumable for B8?); seeds and bulbs (sowing seed is C3, the same sunflower seeds sold for snacking are OUT: a use split); dried herbs (OUT) vs dried flowers (B5); chewing gum.
- **Examples (body):** dental implant, pacemaker, breast implant, cochlear implant (inside the body: body modification OUT, or H2 device?); dentures, prosthetic limb (H2, clear); piercing jewellery (A3, clear); hair extensions and permanent make-up (finding 5).
- **Examples (living, not plant or animal):** sourdough starter, kombucha SCOBY, mushroom grow kit, yeast and cheese cultures, live bait worms (an animal → OUT, though it is fishing tackle), fertilised eggs for hatching.
- **Fix (replace step 1's list):** "1. **Not an ownable object?** A living animal (including live bait and fertilised eggs); **food, drink or other substance made to be eaten or drunk by people or animals**, including supplements and pet food (medicines are H2); a service, membership, course, subscription or account; a right, claim or financial instrument (see finding 7); money held as a balance, stored value or digital currency; a **change made to the body itself** (tattoo, hairstyle, cosmetic surgery). **OUT**. (Devices implanted in the body are in: H2.)" Step 5: "A **living plant or fungus**, a living culture kept to be grown or propagated (sourdough starter, kombucha culture, mushroom spawn), a fresh-cut plant, or a seed, bulb or spore sold for growing? **C3 Plants & Living Cultures**."

### 29. Step 24 (B4, "cleaning … water") runs before step 26 and takes powered garden machines
- **Type:** Key-order trap
- **Severity:** Medium
- **Examples:** leaf blower, pressure washer, snow blower, pool pump and robotic pool cleaner, garden vacuum, electric patio heater (all "powered machines that do a household task: cleaning, … climate, water" → B4, although C2 is the home for keeping grounds); lawnmower (not listed in B4's tasks, so it reaches C2, which is inconsistent with the leaf blower); robot mower (finding 23); decorative indoor plant pot (step 24 "decoration" → B5 before step 26 "planters" → C2).
- **Fix:** Run step 26 (garden and grounds) **before** step 24, and word it: "26. Made for **growing plants or keeping gardens, grounds, paths, pools and drives**, powered or not: garden tools, mowers, trimmers, leaf blowers, pressure washers, snow clearers, planters and plant pots, plant care products, irrigation, greenhouses, compost bins, pool cleaning and pumps? **C2 Garden & Grounds**." In B4, restrict the task list to "indoor cooking, refrigeration, dishwashing, laundry, indoor floor and surface cleaning, indoor heating, cooling and air, and domestic water heating and treatment".

### 30. B5 holds three unrelated functions; clocks and watches belong together
- **Type:** Granularity
- **Severity:** Medium
- **Examples:** a vase, a ceiling pendant light and a longcase clock are all B5; a wristwatch is A3 beside earrings, and a pocket watch or carriage clock is split from it although both are timekeepers with the same movement types (mechanical, quartz), complications and makers.
- **Reasoning (not size):** decoration, lighting and timekeeping each need a different inner structure (form and motif; lamp type, fitting and light source; movement and case type). Watches share horological structure with clocks, not with jewellery.
- **Fix:** Split **B5** into **B5 Decor** ("ornaments, vases, figurines if not F2 (finding 22), mirrors, candles and holders, seasonal and party decorations, artificial and dried flowers, garden ornaments") and **B11 Lighting** ("lamps, light fittings, bulbs and lighting accessories"). Create **A5 Clocks & Watches** ("timepieces of every kind: wristwatches, pocket watches, clocks, timers made as timepieces; smartwatches are D2") and reduce A3 to "**A3 Jewellery**". Key wording in step 11: "- an ornament worn on the body, hair or clothing? **A3 Jewellery**; - a watch? **A5 Clocks & Watches**". In step 24, send "clocks" to A5. (A smaller alternative: keep A3 as it is and only split lighting out of B5.)

### 31. C1 and G2 are too broad to study as single units
- **Type:** Granularity
- **Severity:** Low
- **Examples (C1):** a screwdriver, a bench grinder, a ladder, a multimeter, a diesel generator, a combine harvester, a commercial espresso machine and a cash register are all C1, the last two because step 27 also catches trade equipment.
- **Examples (G2):** a plot of land, a flat, a fitted kitchen, an in-ground pool and a burial plot.
- **Reasoning (not size):** hand and power tools are structured by action (cut, drive, measure, shape). Farm and trade machinery is structured by sector and process. Real property is structured by tenure and building type, and building elements by building component. These are different inner structures.
- **Fix:** C1: keep "**C1 Tools, Workshop & Materials**" (hand and power tools, workshop machines, ladders, measuring and testing tools, generators, building materials and fixings; finding 17). Add "**C7 Farm & Trade Equipment**: machinery and equipment made for agriculture, forestry, a trade or a shop (tractors, harvesters, commercial catering and retail equipment)" with key step "Made for **farm, forestry, trade or shop work** and not for a household (tractors, harvesters, commercial kitchen machines, retail and vending equipment)? **C7**", placed before step 24. G2: after finding 6, keep land and buildings together and name building elements as an internal branch for stage 2; no top-level split needed. E2 (sport vs camping) and F3 (coins vs stamps vs collector series) can be handled by internal facets; no split proposed. H3 and B7 (after finding 12) are thin but each has its own designed function and its own inner structure; keep them.

### 32. Category texts and the key disagree in at least sixteen places
- **Type:** Rule contradiction
- **Severity:** Medium (each is a small fix, but together they mean the category texts cannot be used to check placements)
- **List (category text says → key does):**
  1. A1 "protective clothing", "heated or lit garments stay here" → step 2 / step 11 to 15 (findings 1, 5).
  2. A3 "brooches" vs F3 "collector pins" → step 11 takes both (finding 11).
  3. A4 "walking sticks", "frames and sunglasses stay here" → step 2 → H2 (findings 1, 4, 25).
  4. B1 "display" → step 24's furniture branch omits "display" (display cabinets fit under "store", but easels, plinths and plate stands do not).
  5. B2 "towels" → step 12 → H1 (finding 20).
  6. B5 "seasonal decorations" → step 13 → F4 (finding 9).
  7. B6 "smoke alarms", "locks" → step 3 (hard-wired), step 15 (smart) (findings 6, 23).
  8. B7 "Humidor" in the name → S3 says storage for a thing is not a part (finding 12).
  9. B8 "housing" → step 3 "structure" → G2 (finding 6).
  10. C2 "greenhouses", "planters and pots" → step 3 → G2; S3 → C3 (findings 6, 15).
  11. C5 "calculators", "office machines" → step 15 with no branch (finding 2).
  12. D2 "fitness trackers", "smartwatches" → step 2 "monitor" → H2 (finding 1).
  13. E2 "protective gear made for one sport" → step 2 → H2 (finding 1).
  14. E3 "amplifiers, effects, DJ and studio equipment" → step 15 → D3 (finding 2).
  15. E4 "armour" → step 2 → H2 (finding 1).
  16. G1 "trailers" → step 9 "under its own or human power" (finding 14).
- **Fix:** Add to "How to read": "**The placement key is authoritative.** Category descriptions and precedence notes restate the key and must give the same answer; where they differ, the key wins and the description is corrected." Then apply the findings above and check each description against the revised key line by line.

### 33. Step 19 "fixed work on a physical carrier" is unclear for printed matter that is used rather than read
- **Type:** Wording / Overlap
- **Severity:** Low
- **Examples:** colouring books, sticker books, puzzle books and activity books (F1 by step 19 before steps 20 and 22; a reader may say E1 or C4); printed calendars and planners (F1 or C5?); greeting cards and postcards, blank or written (C5, F5, F1 or F3?); jigsaw puzzles of artworks (E1, clear); globes (a map on a sphere: F1 or B5?).
- **Fix:** Step 19: "A **published work fixed on a physical carrier**, made to be read, viewed or listened to: books (including colouring, puzzle and activity books), comics, magazines, maps, atlases and globes, sheet music, records, CDs, tapes, films and discs? **F1**. (Calendars, planners, greeting cards and blank postcards are C5 while unused; once written and kept, they are F5.)" Note that the second sentence files by state, as the model-kit rule does (finding 35). If that is not wanted, file greeting cards and postcards always in C5.

### 34. Step 10 "keeping an animal" does not cover equipment for wild animals or animal-derived goods
- **Type:** Gap / Wording
- **Severity:** Low
- **Examples:** wild-bird feeder, nest box, bat box, bee hotel, hedgehog house (the animals are not "kept" → C2? B5? no home); beehive and beekeeping suit (keeping bees: B8, but the suit is a garment → step 10 runs first, so B8, acceptable); horse riding helmet (step 2 → H2, finding 1); fishing bait boxes; animal feed (finding 28).
- **Fix:** "10. Made for **keeping, feeding, housing, carrying, training or caring for animals, kept or wild**: housing, tack, carriers, beds, feeders, nest boxes, aquariums, beekeeping equipment, grooming and care equipment? **B8 Animal Equipment**. (Riders' clothing and helmets are E2.)"

### 35. Smaller edge cases the key settles oddly
- **Type:** Key-order trap / Wording
- **Severity:** Low
- **Examples and fixes:**
  - **Collectible figures** (Funko Pop, blind-box figures, Lego minifigure series): made to be both collected and played with or displayed, so step 18's "and not used otherwise" decides by marketing. Add to step 18: "(figures, dolls and vehicles sold as collectible series are E1.)"
  - **Model kits** (C4 while unbuilt, E1 once built): the same object changes category with its state. Add to C4: "Model kits are C4 built or unbuilt; ready-made models are E1."
  - **Liveaboard narrowboat, touring caravan, tiny house on a trailer:** "made to be lived in rather than to travel" is unclear when a craft is made for both. Use finding 6's wording "made to **stay in one place** as a dwelling"; anything made to tour is G1.
  - **Gun safe, fireproof document box:** S3's storage exclusion sends them to B6. That is acceptable, but state it in B6: "safes for any contents".
  - **Electric toothbrush heads, shaver foils, vape pods, coffee pods:** S3 sends them correctly (H1, H1, B7, B3/B4). No change needed beyond finding 15.

---

## Top five changes, in priority order

1. **Rewrite step 2 (finding 1).** Limit H2 to diagnosing, treating, monitoring or compensating for illness, injury or disability. Drop "protect". This step comes first and currently misfiles helmets, armour, protective clothing, sunglasses, life jackets, car seats, fitness trackers and safety equipment, and contradicts seven category texts.
2. **Make the key total (findings 2(d), 17).** Add S1a ("a *yes* lead question with no fitting branch counts as *no*"). Replace step 27 with a function-worded C1 that includes materials and fixings. Add the terminal step 28 X0 Unplaced holding bin. Add F6 Natural History & Specimens for objects not made by people. Give power accessories (cables, chargers, batteries) a home.
3. **Repair step 15 (findings 2, 3, 23).** Move music (step 16) ahead of it. Narrow its lead line to computing, communication, pictures, gaming and audio-video. Re-order the D1/D2 branches so tablets and phones reach D2 and earbuds reach D3. Drop "smart-home" so connected locks, thermostats and bulbs are filed by task.
4. **Remove the setting, motive and user tests from the key (findings 6, 12, 16, 18, 19).** Step 3 becomes land, buildings and building elements, with "built-in" as a modifier. Step 23 stops treating stocked food and drink as in; B7 becomes Tobacco & Smoking. Step 24's "made for the home" gate becomes a task gate, ideally with B3/B4/B6 re-cut by task rather than by power source. Craft vs trade tools are split by craft type, not by hobby vs work. The status filter of steps 1 to 6 is declared in the axis statement.
5. **Narrow the three over-broad early function steps (findings 4, 9, 10).** Step 11's "other personal accessory carried" becomes a closed list. Step 13's "ceremony … festival" becomes religious or spiritual practice, rites of passage and funerals, with secular seasonal goods in B5. Step 14's "records or remembers" becomes issued documents plus personal records made by or for the household. Then apply finding 32: declare the key authoritative and correct every category description to match it.
