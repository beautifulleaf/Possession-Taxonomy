# Stage 2 domain review: B Home (B1 to B10)

*Batch S2R_B. Cold, offline review (no web, no git) of memos framework/structure/B1.md to B10.md and their sources files verify/out/S2_B1_sources.tsv to S2_B10_sources.tsv, against BRIEF.md and framework/CATEGORIES_v0_6.md. Reviewer's judgement, not an owner decision. Severity: **high** = breaks a shared rule or would file the same object in two places across many objects; **medium** = one rule break, one contradiction or a clear split; **low** = wording, evidence or tidy-up.*

**Mechanical checks.** Every memo's source list matches its TSV row for row: B1 differs only by a tracking parameter on furniturerow.com, and B8 only by two URLs cut short in the memo (`Category:Locks_(security_device)`, `163.com …?spss=dy_author`). B10's memo has no URL key; its S-ids are TSV row numbers, which I checked (S1 to S5, S24, S35). All ten memos recommend four levels below the category (sub-family, leaf, kind, named form). None uses content genre. Every memo labels the claims it read from search excerpts. That is good practice, and I list those claims in the findings only where a structural choice depends on them.

## 1. Verdict table

| Code | Verdict | Top three issues |
|---|---|---|
| B1 Furniture & Storage | minor fixes | (1) Items the key names (fitted kitchen cabinetry, humidor, hangers, display stands and shop fittings, pop-up gazebo, playpen, lap desk, rolling cart) have no place in the tree, and B1.6 holds one kind. (2) Kinds defined by region (tansu, zaisu). (3) "Futon" names two objects (US futon sofa vs Japanese shiki-futon), and the shiki-futon that B2 sends to B1 has no B1 kind. |
| B2 Soft Furnishings | minor fixes | (1) A leaf defined by region ("Futon bedding (Japan)"). (2) Tea and kitchen towels sit under "Body textiles". (3) Blanket and Throw appear as two kinds, while the text says they are one. |
| B3 Lighting | minor fixes | (1) Kinds defined by technology or power source (LED tube vs fluorescent tube, CFL, linear halogen, filament bulb, solar lantern, solar garden light), against the memo's own facet rule. (2) EDC and duty/tactical flashlights overlap in output and rest on one source. (3) Design families that span kinds (PH, Akari) have no convention, and Akari ceiling models are filed as flush lights although they are pendants. |
| B4 Decor | minor fixes | (1) Sub-family B4.5 "Festive & party" is named by occasion, and two of its kinds are defined by occasion and region (hina doll set, koinobori). (2) The "decorative plate" kind conflicts with S5 ("a commemorative plate is a plate"). (3) Sign kinds split by material (enamel), and the neon sign and LED candle sit outside B4.9 Decorative lighting. |
| B5 Kitchen & Dining | minor fixes | (1) The "Serve and eat" and "Drink" sub-families overlap: a teacup can go to either. (2) The tier vocabulary mixes tier with market ("commercial"), and each of the three tier pockets rests on one source. (3) Kinds defined by region and material (Yixing teapot), and the tree is thin (cool and store has 3 kinds; appliances are key text only). |
| B6 Cleaning & Laundry | minor fixes | (1) Dryer and washer kinds by technology wait on a cross-category rule. (2) The water-filter vacuum is a kind, though bagged and bagless are attributes. Bin kinds (pedal, sensor, multi-compartment) contradict the memo's own 4b table. (3) Chemical-cleaner kinds are named by room. |
| B7 Climate, Water & Energy | minor fixes | (1) Heater kinds are defined by fuel (kerosene stove, fuel-fired fan heater), against the memo's own "fuel is a tag", and the infrared kinds overlap. (2) Portable generators are proposed for B7 or D2, but the key's step 32 already puts them in C1. (3) The electric handheld fan conflicts with A4 (step 17 is tried before step 30). Rack vs wall home batteries split by installation. |
| B8 Home Safety & Security | needs rework | (1) Sub-family B8.3 "Young-child hazards" is defined by the user, against Appendix A and BRIEF. (2) The door-lock kinds "smart lock" and "keypad lock" contradict the memo's own 4b table (connectivity and opening method are attributes). (3) The safe kinds mix protection grade (fire, burglary) with installation (wall, floor), so one safe has three homes. |
| B9 Smoking & Vaping | minor fixes | (1) The product leaves split by substance, while section 10 makes substance a tag. Tobacco-free pouches and tobacco-free shisha follow opposite rules. (2) Internal leaf codes (A1 to A14, B1 to B7) collide with category codes. (3) Objects the key names (ashtray, hookah coals, cigarette case, betel, areca, khat, herbal blends) have no kinds. |
| B10 Animal Equipment | ready for owner | (1) The "several animals" group starts at three animal groups, so dog-and-cat objects split. (2) Hive systems are shown both as named forms and as platform tags. (3) Bee suits sit in B10 with no precedence sentence against A1 PPE. The feed tier rests on one rating site. |

## 2. Findings by memo

Each finding gives severity, memo, evidence and an exact proposed fix.

### B1 Furniture & Storage

**B1-1 (medium) Membership items with no place in the tree.** The B1 test and the key's notes name fitted kitchen cabinetry (step 4: "kitchen and wardrobe cabinetry is B1"), humidors (step 27), hangers, lap desks, rolling carts, plant stands, display stands, counters and shop fittings, playpens and pop-up gazebos (steps 4 and 30). None of these is a kind in the worked tree. B1.6 "Display & division" holds a single kind (room divider), and its axis ("show and divide") cannot hold a pop-up gazebo. *Fix:* add these kinds:
- B1.4 Cupboards & cabinets: "kitchen cabinet (fitted or freestanding)", "bathroom vanity cabinet", "humidor".
- B1.5 Racks & hooks: "clothes hanger", "coat rack".
- B1.3 Desks & work tables: "lap desk". A new leaf "Carts & islands" holds "rolling cart" and "kitchen island", following Google [S16].
- B1.2 Beds & cots: "playpen".
- B1.6, renamed "Display, division & shelter": "display stand", "plant stand", "shop counter and fitting", "folding screen" and "pop-up gazebo".
- Attest each before it enters the data.

**B1-2 (medium) Kinds defined by region.** "tansu" (under cupboards) and "zaisu floor chair" are kinds whose name is a region's word for a generic form. The memo itself shows that tansu types follow ordinary uses: step chest, kitchen cabinet, clothing chest, wheeled chest [S36]. *Fix:* rename the kind "floor chair", with zaisu as its named form and the tag region=Japan. Delete the kind "tansu". File kaidan tansu as a named form of "chest of drawers"; mizuya tansu as a named form of "kitchen cabinet" (new kind, B1-1); isho tansu as a named form of "chest of drawers"; kuruma tansu as a named form of "blanket chest". Keep "kotatsu", because the heated table is a distinct form and the key names it. Apply the shared regional-name rule (C-3).

**B1-3 (medium) "Futon" splits.** The kind "futon" under Sofas & settees is the US convertible sofa [S26]. B2 (section 9.1) sends the Japanese shiki-futon, the floor mattress, to B1 "under the mattress rule", but B1 has no kind for it. Two builders given "futon (shikibuton)" would file it under Sofas, under Mattresses, or in B2. *Fix:* rename the B1 kind "futon sofa". Add the kind "floor mattress (shiki-futon)" under Mattresses, with the precedence sentence: "A mattress made to lie on the floor and be folded away (shiki-futon) is B1; the quilt laid over it (kake-futon) is B2."

**B1-4 (low) Airbed vs camping sleeping mat.** The kind "airbed" [S21] and the E2 boundary ("air mattresses sold as beds are B1; sleeping mats are E2") leave a self-inflating camping mat or a camping air mattress unclear. *Fix:* "An inflatable mattress sold as a bed for a room is B1 (airbed); an inflatable or foam pad sold for camping or outdoor sleeping is E2 (sleeping mat)."

**B1-5 (low) "Cot" means two things.** "cot (crib)" and "camp cot" use the UK and US senses of the same word. *Fix:* rename the kinds "baby cot (crib)" and "camp bed".

**B1-6 (low) Evidence.** No owner forum, and no Chinese or French market. The memo states both. The choice level for mattresses is well argued [S3, S8, S21]. No change is needed before owner review. The data phase should add one mattress or woodworking community source.

**Objects that would split (B1):** sofa bed, daybed (Seating vs Sleeping); nightstand (memo Q5); storage ottoman and storage bench (Stools vs Chests); kitchen island and bar cart (no leaf); futon; camping air mattress; vanity unit with built-in basin (see C-7, row 21).

### B2 Soft Furnishings

**B2-1 (medium) Leaf defined by region.** "Futon bedding (Japan)" is a leaf named by region, which rule 1 forbids. *Fix:* delete the leaf. File "kake-futon" as a named form of "comforter" (sewn closed with its fill built in, which matches the Sleep Foundation's construction test [S24]), tagged region=Japan. File "kotatsu futon" as a kind "kotatsu cover" under Duvets and bed covers, because it is made to cover a kotatsu table, not a bed. If the owner wants it, the "dresses" axis can say "bed or heated table". The shiki-futon goes to B1 (B1-3).

**B2-2 (medium) Tea towel in the wrong sub-family.** "Kitchen or tea towel" is listed under B2.6 Body textiles, but it dries dishes, not the body. Both UNSPSC and HTS group kitchen linen with table linen [S32, S33]. *Fix:* move it to B2.5 and rename that sub-family "Table and kitchen linen", as it is already titled in the tree. The category stays B2, as the B5 memo agrees.

**B2-3 (low) Blanket and Throw.** Edge case 1 says "one kind Blanket/Throw", but the tree lists "Blanket" and "Throw" separately, and owner question 3 assumes one. *Fix:* use one kind "blanket or throw", with size and setting (bed, sofa) as attributes.

**B2-4 (low) Material and power in kind names.** "Hide rug" is named by material, and "Electric blanket" by power source. Both are acceptable under the exceptions: hide is the form, since the rug is the hide itself; and the key names electric blankets, as does HS 6301.10. *Fix:* record both as the named exceptions of rule T (C-2) and rule "material is the form" (C-6), so the same test is applied in B7 and B6.

**B2-5 (low) Orphan risk in table linen.** B2.5 has one kind (tablecloth), because napkin, placemat and table runner are held back for attestation. B5 relies on textile placemats being B2 (B5 boundary 2). *Fix:* make attesting napkin, placemat, table runner and floor cushion (zabuton) the first data-phase task for B2.

**Objects that would split (B2):** floor cushion (zabuton) vs zaisu (B1) vs scatter cushion; bath mat (floor sub-family, though it is used in the bath); shower curtain (memo Q6; B7 says B2, see C-7); weighted blanket (B2 vs H2).

### B3 Lighting

**B3-1 (high) Kinds defined by technology, against the memo's own rule.** Section 3 says "Technology (LED, halogen, incandescent) … [is a] tag and facet, never [a] level". Yet the tree has these kinds:
- "Linear fluorescent tube" and "LED tube": the same form, two technologies.
- "Compact fluorescent lamp".
- "High-intensity discharge lamp".
- "Linear halogen lamp (R7s)".
- "Filament (Edison-style) bulb": a look and a technology on a GLS, globe or candle shape.
- "LED panel light" and "LED strip light".
- By power source: "Electric lantern" vs "Solar lantern", and "Solar garden light" beside the bollard and spike lights.

Owner question 6 recommends a fuel tag for non-electric lamps, which the lantern kinds then ignore.

*Fix:*
- Merge the tubes into "linear tube lamp", tagged technology=fluorescent, LED or halogen; R7s becomes the cap attribute.
- Keep "compact fluorescent lamp" only if the owner adopts rule T(b) on the ground that it needs its own holder (G24/2G11 pin-base types). Otherwise move it to the shape attribute of general bulbs.
- Keep "high-intensity discharge lamp" under rule T(b): it needs a ballast and cannot be swapped.
- Make "filament style" an attribute of the GLS, globe and candle bulb kinds.
- Rename "LED panel light" to "panel light". Keep "strip light" as a kind, since the strip is the form.
- Merge "Solar lantern" into "Electric (battery or solar) lantern". Delete "Solar garden light" and tag the bollard, post and spike kinds power=solar.
- Keep mantle, wick (hurricane) and candle lanterns, because the burning mechanism changes the object.

**B3-2 (medium) Overlapping flashlight classes.** "Pocket (EDC) flashlight" (200 to 1,500 lm) and "Duty or tactical flashlight" (1,000 to 2,500 lm) overlap, rest on one retailer blog [TT], and "tactical" is a scene word. A 1,200 lm 18650 light fits both. *Fix:* use one kind "handheld flashlight", with output class (ANSI FL1 bands [RF]) and carry size as attributes, and tactical as a scene tag. Keep "penlight" and "keychain light" as kinds by form.

**B3-3 (medium) Design families that span kinds.** PH lamps (pendant and table), Akari (ceiling, floor, table) and the Tizio and Tolomeo families have no stated home. "Akari ceiling models" is filed as a named form of "Flush ceiling light", but the Akari ceiling pieces are hanging shades, so they belong under Pendant light [NG]. *Fix:* adopt the series convention (C-5). Move Akari ceiling models to Pendant light.

**B3-4 (low) Placement leaves and the installation modifier.** The memo itself asks this (Q1). The split "Fixed fittings vs Standing lamps" reads like the Appendix A installation modifier. *Fix:* adopt rule M (C-4). Under it, pendant vs floor lamp is a form difference, because the object is made only for that mount. The B3 tree then stands as written.

**B3-5 (low) Evidence gaps.** The sunrise lamp is named by the key but has no fetched page. The EU A-to-G scale and Regulation 2019/2015, and the BudgetLightForum cell boards, come only from search excerpts. The memo flags all of these. Nothing structural depends on them except the energy-class modifier.

**Objects that would split (B3):** table lamp vs desk lamp for a balanced-arm lamp on a base; clamp lamp vs clamp work light; lantern used as a fixed wall light vs a carried one (the memo's rule "by mount or carry" settles it if applied); LED strip (B3 vs B4); candle lantern (B3) vs lantern-style candle holder (B4: C-7, row 8); mirror light (B3) vs lighted vanity mirror (H1); plug-in security floodlight (B3 vs B8: settled by B8, C-7, row 7).

### B4 Decor

**B4-1 (medium) A sub-family named by occasion.** "B4.5 Festive & party decorations" is named by occasion, and Appendix A lists occasion (festival, season) as a modifier. Two of its kinds are defined by occasion and region: "hina doll set" (Hinamatsuri) and "koinobori" (Children's Day), both from one Japanese source [S25]. The key does list "seasonal, festival and party decorations" as B4 members, but membership is not an axis. *Fix:* restate the sub-family axis as "decorations made for temporary display", by form: hung and strung (bauble, garland, streamer, bunting, tree topper), standing displays (artificial tree, display set), and party consumables (cracker, popper, sparkler). Occasion stays a tag. File koinobori as a named form of "windsock or streamer" (B4.8). File the hina doll set as a named form of a new kind "festival doll display", tagged occasion=Hinamatsuri and region=Japan. File the tree ornament and the artificial Christmas tree as kinds, because the form exists only as that object; occasion=Christmas becomes a tag.

**B4-2 (medium) Decorative plate vs S5.** The tree has the kind "decorative plate", and boundary 5 files "a decorative plate made to hang" in B4. But S5 and the step 15 note say "a commemorative plate is a plate", and the B5 memo (boundary 4) says a plate is B5 "however decorative or collected". Collector and commemorative plates are mostly made to hang. *Fix (owner choice, see Q-B4c):* either (a) delete the B4 kind, so that every plate form is B5 and the display motive is a tag, as S5 implies; or (b) keep "wall plate" in B4 only for plates without a food-safe glaze or a foot ring, made only to hang, and add that sentence to step 30. Option (a) is simpler and matches S5.

**B4-3 (medium) Material and technology in kind names; neon in two places.** "Enamel (porcelain) sign" is named by material [S20]. "Neon sign" sits under B4.8 Signs, but the key's B3 note groups neon signs with decorative lighting, which is B4.9. "LED (flameless) candle" sits under Candles, but it is a battery light, and the B3 memo also calls it B4 decorative lighting. *Fix:* sign kinds by form: "hanging sign", "wall sign or plaque", "illuminated sign (neon or LED)", with material as an attribute and enamel as a named form or tag. Put the illuminated sign in B4.8, because its purpose is signage, and add the cross-reference "decorative light that spells a message → B4.8". Move "flameless candle" to B4.9 Decorative lighting.

**B4-4 (medium) Mirror kinds mix two axes.** The kinds are wall, leaner (floor), cheval, overmantel, convex and dresser. Overmantel is a placement, convex is a shape. A round convex wall mirror has two homes. *Fix:* kinds by placement only: wall mirror, floor (leaner) mirror, standing (cheval) mirror, table or dresser mirror. Convex, girandole, trumeau, pier and overmantel become named forms or shape attributes. Add the sentence "a mirror made to magnify or light the face for grooming is H1", which matches the memo's own boundary 15.

**B4-5 (medium) Tier claim rests on one source.** "Consensus-ranked by maker" for candles and home fragrance rests on one luxury-candle retailer's blog [S28], plus a mass vs premium market split [S24]. *Fix:* call it "preference with a maker price band" until a second independent ranking source is fetched. Keep the `tier` field on the ledger.

**B4-6 (low) Unattested and orphaned kinds.** Sparkler and firework (named by the key), string light (the only kind in B4.9) and jharokha (called a "kind" in section 7) are not in the tree. *Fix:* list these as the first data-phase attestation tasks. Add jharokha as a named form of "decorative wall panel" rather than as a kind, under the regional-name rule (C-3).

**Objects that would split (B4):** candle holder (B3 vs B4); lantern holding a candle; bird bath (B4 vs B10: C-7, row 32); cachepot (C2 vs B4); decorative plate; neon sign; snow globe (decorative object vs festive); round convex mirror.

### B5 Kitchen & Dining

**B5-1 (medium) "Serve and eat" overlaps "Drink".** "Cup and saucer set" is under B5.4 Tableware, while "Mug or tea cup" is under B5.5 Cups. "Wine glass" and "Tumbler" are in B5.5, though they are table service in the Replacements piece guides that the memo uses for B5.4 [S35, S36]. A teacup would be filed in either. The coffee grinder sits in Drink, while a pepper or spice mill would sit in Prepare (the memo's edge case 3). *Fix:* re-axis the two sub-families. B5.4 "Serve, eat and drink at table" holds tableware, flatware, glassware and cups, all as piece types. B5.5 "Make drinks" holds coffee equipment (including all coffee grinders), tea equipment, kettles and bar tools. File a spice mill or pepper mill under B5.2 Hand tools, and add the sentence "a grinder made for coffee is filed with coffee equipment".

**B5-2 (medium) Tier vocabulary and single-source tiers.** The proposed modifier is `tier = {entry, mid, prosumer/premium, commercial}`, but "commercial" is the Appendix A market modifier. Each tier pocket rests on one page: knife steels [S21], the espresso ladder from a retailer blog [S25], burr tiers [S26] (whose own author says geometry matters more), and stemware maker tiers [S37]. *Fix:* use `tier = {entry, mid, premium}` with the source named, and a separate `market = commercial` tag. Label each pocket "single source" until a second source agrees.

**B5-3 (low) Kind defined by region and material.** "Yixing teapot" is defined by region (Yixing) and by material (zisha clay). Kyusu (side handle) and gaiwan (lidded bowl) are forms. *Fix:* "Yixing" becomes a named form of "teapot", tagged region=China and material=zisha.

**B5-4 (low) Thin tree.** Cool and store has 3 kinds. Oven or hob, barbecue, fridge, wine fridge, dishwasher and decanter are key text only. Barware (shaker, jigger), vending machines, the moka pot and rice cooker are missing. Commercial equipment comes from one Australian supplier. The memo flags the gaps (section 1.6). *Fix:* before freezing the sub-family list, attest the large appliances, barware and the moka pot. These are breadth, not structure.

**B5-5 (low) Platform claim not sourced.** Capsule and pod systems are named as a platform but are not sourced, while J6 files capsules as groceries. *Fix:* source them, and record capsule systems in the shared compatibility ledger (C-1c), linked to J6 capsule kinds.

**Objects that would split (B5):** teacup; steak knife (kitchen knives vs table flatware, memo Q6); hand coffee grinder; stovetop vs electric kettle (settled by the memo: one kind); a Japanese tetsubin (kettle vs teapot); water filter jug (B5 vs B7: settled, C-7, row 23); dish rack (settled, C-7, row 22).

### B6 Cleaning & Laundry

**B6-1 (medium) Technology kinds.** The dryer kinds (vented, condenser, heat pump) and the top-load washer kinds (agitator, impeller) wait on owner question 2. *Fix:* decide them under the shared rule T (C-2). Under T(b), vented vs ventless is a kind, because the vented dryer needs a duct, which changes its installation. Condenser vs heat pump becomes an attribute of "ventless tumble dryer", with the EU label class as its spec. Agitator vs impeller stays a kind only if the owner accepts that the mechanism changes the drum's form (a central post); otherwise it is an attribute.

**B6-2 (low) Kinds that contradict the memo's own attribute rules.**
- "Water-filter vacuum" is a dust-handling method. The memo makes bagged, bagless and cyclonic attributes.
- The bins "pedal bin", "sensor bin" and "recycling bin, multi-compartment" are kinds, but the memo's own 4b table says "capacity and compartments are attributes"; the sensor is a powered opening; and the source is one guide [S29].

*Fix:* make "water filter" a value of the dust-handling attribute. Bin kinds by form: "kitchen bin", "wheelie (outdoor) bin", "waste-paper basket", "food-waste caddy", "bin liner". Opening mechanism (pedal, swing, touch, sensor) and compartments become attributes.

**B6-3 (low) Kinds named by room.** "Bathroom and toilet cleaner" and "kitchen and oven cleaner" are named by room, which the B1 memo treats as a setting. *Fix:* name them by soil or action, following the retail lines [S20, S22]: "limescale remover", "toilet cleaner", "degreaser and oven cleaner", "multi-purpose cleaner", "glass cleaner", "bleach and disinfectant".

**B6-4 (low) Shoe care is misread as an S3 conflict.** S3 already says "cleaning products are B6 … whatever they are used in". Shoe cleaners are B6 without a ruling; only polish, conditioner and waterproofing spray are open. *Fix:* narrow owner question 8 to "shoe polish and waterproofing: B6 (care product) or A2 (consumable for one kind of object)?".

**Objects that would split (B6):** handheld car or mattress vacuum (in "Floors"; harmless, because the leaf decides); steam cleaner (floors vs hard surfaces; the memo places it in surfaces); heated airer (B6) vs electric heated towel rail (B7), a cross-memo split (C-7, row 27); moisture absorber (B6 says B7, but B7 has no kind, C-7, row 25); cat litter (B10 vs B6; B6 is silent, C-7, row 31).

### B7 Climate, Water & Energy

**B7-1 (medium) Kinds by fuel, against the memo's own rule.** Section 4b says "the fuel stays a tag", yet the tree has these kinds:
- "kerosene stove" and "fuel-fired fan heater (kerosene or gas)" beside "fan heater (convection, ceramic)";
- "electric infrared panel heater" beside "infrared radiant heater" and "micathermic panel heater" [BH, CS], so a wall-hung infrared panel fits two kinds.

*Fix:* heater kinds by heating mechanism: "fan heater", "convector heater", "oil-filled radiator", "radiant heater (bar, quartz or halogen)", "infrared panel heater", "flued stove (solid fuel)", "flueless room heater (kerosene or gas)". Fuel is a tag. Micathermic becomes a named form or attribute of the panel heater. "Wood-burning or multifuel stove" stays under rule T(b), because the flue and firebox change installation.

**B7-2 (medium) Portable generators against the key.** Owner question 4 proposes portable generators and power stations for B7 or D2. Step 32 already lists "portable generators" in C1. *Fix:* keep portable generators in C1, as the key says. Ask only about the portable power station (a battery and inverter box), which the key does not name: B7 home battery, D2 power bank, or C1. My recommendation: B7 "home battery, portable", because it stores electricity for the home and step 24 puts only power banks in D2.

**B7-3 (medium) The electric handheld fan vs A4.** The air-movement leaf has "handheld fan" [KF]. Step 17 is tried before step 30, and A4 lists the "hand fan" as a personal accessory carried in hand. Its notes send only computing, communication and media devices onward to step 24, so a battery handheld fan reaches A4 first. *Fix:* add to the step 17 note: "a powered hand-held or neck fan is B7". Otherwise drop the kind from B7. I prefer the note, because a fan's job is air movement.

**B7-4 (low) Kinds by installation, power and set.**
- "home battery, rack-mounted" vs "wall-mounted or all-in-one" is the installation modifier.
- "shower unit; electric shower" splits by power source.
- "plug-in balcony solar kit" is a set (panel plus micro-inverter) made a kind.

*Fix:* one kind "home battery", with a form-factor attribute. "Electric shower" may stay a kind under T(b), since it carries its own heater and needs a dedicated circuit. Otherwise it is a power attribute of "shower". Decide the balcony kit under the shared set rule (C-8).

**B7-5 (low) Two filing rules disagree for US heat pumps.** The rule "file by the medium delivered at the output" puts an air-to-air mini-split under Cooling as an "air conditioner", but the US buyer's name for it is "heat pump" (ENERGY STAR lists "Heat Pumps" separately [ESF]). The memo uses both rules. *Fix:* keep only the medium rule, list "mini-split heat pump" as a synonym of "wall-mounted split air conditioner", and tag it reversible.

**B7-6 (low) Orphans B6 sends to B7.** The moisture absorber (desiccant tub) has no B7 kind. The bathroom clothes-drying unit is B6 per the B6 memo, and B7 should say so. *Fix:* add the kind "desiccant moisture absorber" under Air treatment. Add to B7 section 9: "a ceiling unit made to dry laundry is B6, even when it also ventilates."

**Objects that would split (B7):** a vanity unit with a built-in basin (B1 says the basin is B7 and the cabinet B1; B7 says "a vanity unit is B1"; see C-7, row 21); an infrared panel; a towel radiator vs a heated airer (C-7, row 27); a portable power station; a Dyson purifier-heater (the memo gives a rule).

### B8 Home Safety & Security

**B8-1 (high) Sub-family defined by the user.** "B8.3 Young-child hazards" divides the category by the user's age. BRIEF says "user age is a modifier", and Appendix A lists user (baby, child) as a modifier. The same stair gate is sold for dogs, and a cabinet latch also guards against adults who have dementia. *Fix:* rename the sub-family "Household injury hazards" (falls, entrapment, crushing, electric shock, burns), with child as a user tag. Under it, leaves by device job: gates and barriers; latches for cabinets and appliances; edge, socket and knob guards; window guards; door stops (this gives door stops a home, closing owner question 7). Move "video baby monitor" to B8.1 Security cameras as "room monitor (baby or pet)", or to a new B8 leaf "room monitors". It watches a room and does not stop an injury; the H2 line for health-sensing monitors stays.

**B8-2 (medium) Lock kinds that contradict the memo's own choice-level table.** The tree has "keypad (push-button) lock" and "smart door lock", while 4b lists "opening method (key, code, fingerprint); smart or not (connectivity)" as attributes, and the key says connectivity is a modifier. A smart euro cylinder is then both "euro cylinder" and "smart door lock". *Fix:* delete both kinds. Add the attributes opening method (key, code, card, fingerprint, app) and connectivity to the form kinds: mortice deadlock, mortice sashlock, night latch, euro cylinder, multipoint lock, deadbolt, rim lock and patio lock.

**B8-3 (medium) Safe kinds mix two axes.** "home (furniture) safe", "fire-resistant safe", "burglary-resistant safe", "wall safe" and "floor safe" mix protection grade with installation. A wall-mounted, fire-rated, EN 1143-1 grade I safe fits three kinds. *Fix:* one kind "safe", with the attributes installation (freestanding, furniture, wall, floor), burglary grade (standard plus grade) and fire class (standard plus minutes). Separate kinds only where the form differs: "key safe (outdoor key box)", "key cabinet", "cash box", "firearms cabinet", "fire-resistant document box or chest" (portable, lid-opening).

**B8-4 (low) Gate kinds by mounting.** "Hardware-mounted gate" vs "pressure-mounted gate" is the installation modifier, but Consumer Reports' rule that a hardware-mounted gate is required at the top of stairs [S16] shows that the mounting changes what the object does. *Fix:* keep both, as an example of rule M(b) (C-4).

**B8-5 (low) Thin leaves and evidence.** The B8.3 and B8.4 leaves hold one kind each in the tree. Burglar-alarm grading (EN 50131, VdS), EN 1303 and TS 008 come from search excerpts only, and the Chinese lock grades come from consumer media [S32]. The memo flags all of these. *Fix:* do not store any grade scheme that lacks a fetched source page. Add a moth-repellent kind (mothballs and cedar blocks) to B8.4, because the B6 memo sends mothballs to B8.

**Objects that would split (B8):** door stop; stair gate used for a dog; smart lock; wall safe; baby monitor; personal attack alarm (memo Q2); a lock box for keys vs a key cabinet; anti-burglar gravel (C2 vs B8).

### B9 Smoking & Vaping

**B9-1 (medium) Substance is a tag in one place and a leaf in another.** Section 10 makes substance a tag, and Candidate B is rejected because "a top split by substance would turn a modifier into a level". Yet these product leaves are defined by substance: "Nicotine pouches & other non-tobacco nicotine", "Cannabis flower & pre-rolls", "Cannabis concentrates & cartridges", "Cannabis infused products" and "Other plant products". The same form then splits:
- a prefilled nicotine pod (A10) vs a cannabis vape cartridge (A12);
- a cannabis gummy (A13) vs a kratom gummy (A14);
- an "All White" tobacco-free pouch (A9) vs white-portion snus (A8);
- tobacco-free shisha, which goes "with the form it imitates" (A6) under the memo's own rule 4, while tobacco-free pouches do not.

*Fix (owner choice, Q-B9a):*
- (a) State the leaf axis as "substance and form" and treat substance as product identity, as species is in J1. Then put tobacco-free shisha in a substance-correct leaf, or explicitly exempt it.
- (b) File products by form only: smoked rolls (cigarette, pre-roll, herbal cigarette), cigars, loose smoking material, heated sticks, oral pouches and smokeless, e-liquids and prefilled cartridges, concentrates, infused edibles and drinks, tinctures, topicals. Substance becomes a required tag.

Either works. The memo must use one. I lean to (b), which matches its own "file by the form it imitates" rule and the retail evidence that hardware and form lead [S7, S10, S11].

**B9-2 (low) Leaf codes collide with category codes.** The internal codes A1 to A14 and B1 to B7 read as category codes. Owner question 10 says a disposable vape "is filed by the device (B3)", which reads as B3 Lighting. *Fix:* use B9.P1 to B9.P14 and B9.H1 to B9.H7, or the shared code format (C-9).

**B9-3 (medium) Objects the key names that have no kind.** Step 27 names ashtrays, hookah coals and cigarette cases. The 4b table names table, pipe and cigar lighters. None is a kind in the tree. Betel quid, areca nut, khat, herbal smoking blends and bidi have no fetched source. *Fix:* add the kinds "ashtray", "hookah charcoal", "cigarette case", "cigar case", "table lighter", "pipe lighter", "torch (jet) lighter" and "rolling tray" to the implement leaves. Leave the plant products as named gaps for the data phase. A key-named kind should not stay empty at owner approval.

**B9-4 (low) Cigar case and travel humidor.** The memo's owner question 3 needs one sentence. *Fix:* "A case made to carry smoking products on the person (cigarette case, cigar case, travel humidor, tobacco pouch) is B9; a humidor, tobacco jar or cabinet that stands in a room is B1." This applies the A4 personal-carry logic and keeps the step 27 note.

**B9-5 (low) Pipe kinds are not one axis.** Billiard and Bulldog are shape families, but Churchwarden is a stem length and Freehand is a carving style (a Danish-school scene, per the memo's own section 7). *Fix:* keep these four as kinds only if the owner calls them "shape families" as Wikipedia does [S6]. Otherwise make Churchwarden a stem attribute and Freehand a named-form group. This sits next to the owner's material-vs-shape question.

**Objects that would split (B9):** disposable vape (hardware vs e-liquid; the memo gives a rule); cannabis cartridge vs nicotine pod; tobacco-free pouch; blunt (the memo gives a rule); kratom shot (drink) vs powder; CBD balm (the memo gives a rule).

### B10 Animal Equipment

**B10-1 (medium) "Several animals" starts at three groups.** Objects made for three or more groups go to "several animals". So a bowl, bed, carrier, brush or flea treatment sold "for dogs and cats" (two groups) has no single home, and two builders would put it under Dogs or Cats. Peppy and Pet Circle sell many of these as dog-and-cat items [S13, S14]. *Fix:* "an object made for more than one animal group goes to 'Several animals'." Every kind carries an `applies_to` tag that generates the per-animal views.

**B10-2 (low) Hive systems shown two ways.** In the tree, Langstroth, National, Dadant and Zander are "named forms" of "framed vertical hive". The 4b table calls them platform tags. *Fix:* treat them as platform (compatibility) values in the shared compatibility ledger (C-1c), carried on hive, box and frame kinds. Named forms are then Flow Hive, the Dartington long deep and similar designs.

**B10-3 (low) Bee suit vs A1.** "bee suit, jacket or veil" is in B10. Step 13 is tried before step 17, so the key does file it in B10. But the step 13 note sends only riders' clothing to step 17, and A1's test covers "protective clothing … made to protect the wearer from a hazard". The rule is invisible to an A1 builder. *Fix:* add to the step 13 note either "beekeeping suits, veils and gloves are B10" or "… are step 17 (A1 PPE)". I recommend A1, which matches the riders' clothing logic: worn by the person.

**B10-4 (low) Feed tier from one source.** Above the AAFCO or FEDIAF gate, the feed ordering rests on one rating site [S24]. *Fix:* record the rating as `rating(source=Dog Food Advisor, date)` on named forms only, with no category-wide tier. The required "complete or complementary" flag is good and should stay.

**Objects that would split (B10):** dog-and-cat bowl; hay (horse vs rabbit vs several animals); cat litter (C-7, row 31); bird bath (C-7, row 32); pond pump (C2 vs B10); pet stroller (G1 vs B10, memo Q8); GPS pet tracker (D2 vs B10); honey extractor (B10 vs B5).
