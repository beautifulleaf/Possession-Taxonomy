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

## 3. Cross-memo consistency and proposed shared conventions

### C-1 Ledgers (medium)

The memos agree that a maker ledger is needed, never as a level, but they propose eight different column sets:

| Memo | Ledger fields proposed |
|---|---|
| B1 | maker, known-for named forms, designer, country, era, licence status, scene tag, price band (no tier) |
| B2 | maker, known-for kinds, tier, country, era, scene tag (price band "free") |
| B3, B4, B6 | maker, known-for kinds, scene tags, tier, price band, country, era, attestation URL |
| B5 | as B3, plus a separate pattern ledger (tableware, crystal, flatware) |
| B7 | as B3, plus `made_by` (OEM behind the brand) |
| B8 | maker, known-for kinds, tier or grade ceiling, ecosystem/platform tag, scene tags, country, era (no price band) |
| B9 | maker, `maker_type`, known-for kinds, scene tags, tier, price band, country, era, `platform`, brand-owner and factory roles |
| B10 | as B3 |

**Proposed shared schema (C-1a), one table for all categories.** Columns:
- `maker_id`, `name`;
- `maker_type` (B9's list, extended with designer, workshop, OEM and own-label retailer);
- `role_of` (the parent or brand owner) and `made_by` (OEM or factory): B7, B9;
- `known_for_kinds` (kind ids), `known_for_named_forms` (ids);
- `designers` (B1);
- `scene_tags`;
- `tier`, a typed value (see C-1b);
- `price_band`;
- `country`; `era_from` and `era_to`;
- `licence_status` (authorised, licensed, original, reproduction maker: B1);
- `platforms` (ids from C-1c);
- `attestation_urls` (one per claim).

Leave a column empty where a category does not need it. Never drop it.

**Proposed shared tier object (C-1b).** It merges B6's "typed source", B7's "scheme plus value", B8's "standard plus grade" and B9's `rating_band`:
- Store `tier = {scheme, value, scope_kind, source_url, date}`, for example `{EN 1143-1, III, safe, …}` or `{Cigar Aficionado 100-point, 90-94, named form, …}`.
- Compare only within the stated kind (B6 [S14, S15] and B10 [S24] both say so).
- Keep `price_band` as a separate field with one shared vocabulary: budget, mid, premium, luxury. B4 uses mass, mid, premium, luxury; B5 uses entry, mid, prosumer/premium, commercial; B3 uses budget, mid, premium.
- `market` (domestic or commercial) is never a tier value (B5-2).
- A pass/fail mark (EN 14604, NSF/ANSI, SCA certified, child-gate EN 1930) is a `certification` field, not a tier (B7 and B8 already say this for NSF and EN 14604).

**Proposed compatibility ledger (C-1c).** Five memos describe a platform or fit system, each in its own way:
- B3: cap-and-standard table (E27, GU10 and the rest);
- B6: a `fits` field on vacuum parts;
- B7: battery and inverter matching, and indoor and outdoor units;
- B8: ecosystem tag (Ring, Nest), alarm interlink ranges;
- B9: heated-tobacco device families, coils;
- B10: hive systems (Langstroth, National, Zander);
- B5: capsule systems (not yet sourced).

One table covers them all: `platform_id, name, type (open standard | maker ecosystem), owner, dimension or spec, kinds_that_use_it, source_url`. Parts and consumables carry `fits = [platform_id]`, and named forms carry `platform = platform_id`. B3's cap table and B10's hive systems are its first rows.

**Named-form registers (C-1d).** For very large sets of designs inside one kind, the memos already propose side tables: national and state flags in B4 (about 900), tableware patterns in B5 (tens of thousands), cigar marca-and-vitola in B9, feed recipe lines in B10. Proposed rule: when one kind has more than about 50 attested named forms of the same type, they go in a register keyed by kind, and the tree shows only the iconic or canonical ones.

### C-2 Technology and power source as a kind (high: B2, B3, B4, B6, B7, B8)

Appendix A makes power source and technology a modifier. Yet every memo in this domain meets objects where the technology seems to make a different thing, and each resolves it differently:
- B3 makes LED tube vs fluorescent tube kinds, and solar lanterns too, against its own rule.
- B6 asks the owner (dryers, washers).
- B7 keeps the heat-pump water heater as a kind and asks the owner.
- B8 keeps smart lock and keypad lock against its own table.
- B4 puts the LED candle under candles.
- B2 keeps the electric blanket (the key names it).
- B6 keeps the sensor bin.

**Proposed rule T.** Power source, technology and connectivity are attributes. They define a kind only when (a) the placement key names that kind (electric blanket, heat pump), or (b) the technology changes the object's physical form or its installation needs, so that one cannot replace the other without new fittings, and a fetched comparison source tests or ranks the types separately.

Applied:
- **Kinds:** HID lamp (ballast); vented vs ventless dryer (duct); heat-pump water heater (compressor unit and space needs [CW, RM]); flued stove; electric shower (own circuit); robot vacuum (autonomous form).
- **Attributes:** LED vs fluorescent tube; condenser vs heat-pump ventless dryer; smart or keypad lock; sensor bin; solar vs battery lantern.
- **Not a candle at all:** the LED candle is a light (B4.9).

Owner question Q-X1.

### C-3 Regional names (medium: B1, B2, B4, B5, B6, B7, B8, B9)

Japanese and other regional words appear as kinds (tansu, zaisu, kotatsu, kake-futon, kotatsu futon, chochin, andon, hina doll set, koinobori, kyusu, Yixing teapot, yanagiba, twin-tub, bathroom drying unit, warm-water toilet seat, 補助錠 supplementary lock, kiseru, kizami, kretek, Balkonkraftwerk), as a leaf (B2 "Futon bedding (Japan)") or as named forms. Each memo uses its own test.

**Proposed rule R.** A regional name is a **kind** only when it names a form that no generic kind in the tree already covers, and its kind label is then the generic description, with the regional word as its name or synonym: warm-water toilet seat; kiseru (Japanese long pipe); kotatsu (heated low table). Where a generic kind exists, the regional name is a **named form** under it, tagged with the region: zaisu under floor chair; Yixing under teapot; koinobori under windsock; kake-futon under comforter; tansu types under their use kinds. A region never names a sub-family or a leaf.

Applied, this changes B1-2, B2-1, B4-1, B4-6 (jharokha) and B5-3. It confirms kotatsu, kyusu, gaiwan, yanagiba, deba and usuba (knife forms with no Western equivalent), twin-tub, kiseru, kizami, kretek and the bidet seat as kinds.

### C-4 Mounting vs the installation modifier (low: B3, B4, B7, B8)

B3 (fixed vs standing; ceiling, wall, ground), B7 (wall, floor, ceiling-cassette and window air conditioners; rack vs wall battery), B8 (hardware- vs pressure-mounted gate; wall and floor safes) and B4 (wall vs leaner mirror) all divide by where the object is fixed. Appendix A lists "installation (freestanding, built-in, fitted)" as a modifier.

**Proposed rule M.** Mounting defines a kind when (a) the object is made only for that mount and its body differs (pendant vs floor lamp; window vs split air conditioner; wall vs floor mirror stand), or (b) the mount changes what the object can safely do, as a fetched source states (top-of-stairs gate [S16]). When the same body is offered with different fixings (wall or floor safe, rack or wall battery, built-in or freestanding oven, fitted or loose carpet), mounting is the installation attribute.

Applied: B3 and the B7 air-conditioner kinds stand; the B8 safes and the B7 batteries merge (B8-3, B7-4); the B8 gates stand.

### C-5 Design series that span kinds (low: B1, B3, B5, B9)

The CH22 to CH26 series (B1), PH lamps and Akari (B3), Riedel lines and dinnerware patterns (B5), IKEA lines such as HEMNES and KALLAX that run across beds, shelving and desks (B1), and the Dunhill shape numbers (B9) are families that cross kinds.

**Proposed rule.** A series is a row in the maker ledger, as `series` with a maker id. Each member is a named form under its own kind, with `series_id`. A series is never a named form that spans two kinds.

### C-6 Material as the form (low: B1, B2, B7, B9)

Four memos ask the same question in four ways:
- latex mattress (B1, accepted as construction);
- hide rug (B2);
- hot tub "by construction material" (B7 Q8);
- pipe material vs shape (B9 Q2).

**Proposed test.** Material is the form only when changing the material changes the object's construction method and what a buyer compares, and a fetched source divides the kind that way (mattress construction [S21]; hide rug [S17]). Otherwise material is an attribute. On that test the hot tub kinds should be "hard-shell hot tub", "inflatable hot tub" and "wood-fired tub", with material as an attribute. Pipes stay shape-first, with briar, meerschaum, corn cob and clay as material attributes, unless the owner says otherwise.

### C-7 Boundaries between B memos: where the two sides agree or not

| # | Object | Side 1 | Side 2 | Status and proposed sentence |
|---|---|---|---|---|
| 1 | Shiki-futon | B2: B1 | B1: no kind | **Orphan.** Add the B1 kind (B1-3). |
| 2 | Tea and kitchen towel | B2: B2 (in Body textiles) | B5: B2 | Agree on the category; fix the B2 sub-family (B2-2). |
| 3 | Textile placemat and napkin | B2: B2 (held back) | B5: textile B2, hard B5 | Agree; attest them in B2. |
| 4 | Laundry basket | B1: B6 | B6: B6 | Agree. Add to the S3 "never parts" list: "laundry baskets are B6". |
| 5 | Locker, filing cabinet vs safe | B1: B1 / B8 | B8: same | Agree. |
| 6 | Gun cabinet | B1: open (E4 or B8) | B8: B8 ("safes for any contents") | **Settle as B8.** Delete it from B1's open list. |
| 7 | Security floodlight (light only) | B3: open (B8 or B3) | B8: B3; floodlight camera B8 | **Settle:** a light is B3; with a camera it is B8. |
| 8 | Candle holder, lantern-style holder | B3: candle lantern is a carried B3 kind; silent on holders | B4: holders B4, "lantern stays B3" | **Not agreed.** Proposed: "An open holder for a candle (candlestick, candelabrum, tealight holder, wall sconce for candles) is B4. An enclosed lantern with a handle, made to be carried as a light, is B3. A lantern made to stand or hang as decoration is B4." |
| 9 | LED strip, string lights | B3: open | B4: string lights in B4.9 (unattested) | **Not agreed.** Proposed: "A light strip sold to light a space (under-cabinet, cove) is B3; string, fairy and novelty lights made mainly as decoration are B4 (key note)." |
| 10 | Flameless candle | B3: B4 | B4: in Candles | Agree on the category; move it to B4.9 (B4-3). |
| 11 | Neon or LED sign | key: B4 decorative lighting | B4: B4.8 Signs | Category agreed; leaf fixed in B4-3. |
| 12 | Lighted makeup mirror | B4: H1 | B3: "mirror light" B3 | Agree if the B3 kind means a wall light over a mirror. State it. |
| 13 | Decorative or commemorative plate | B4: B4 if made to hang | B5 and S5: B5 | **Conflict.** Owner (B4-2, Q-B4c). |
| 14 | Room spray vs fabric freshener | B4: B4 vs B6 | B6: same | Agree. |
| 15 | Essential oil for a diffuser | B4: B4 or H2 open | none | Open. Proposed: B4 unless sold for therapy (H2). |
| 16 | Shower curtain | B2: open (B2 or B7) | B7: B2 | **Settle as B2.** |
| 17 | Bath mat | B2: B2 | B7: B2 | Agree. |
| 18 | Towel radiator | B7: B7 | B2: none | Agree. |
| 19 | Kotatsu, kotatsu cover | B1: kotatsu B1 | B2: cover B2; B7: kotatsu B1 | Agree. |
| 20 | Electric blanket, heated throw | B2: B2 | B7: B2 (key) | Agree. |
| 21 | Vanity unit with a built-in basin | B1: basin B7, cabinet B1 | B7: "a vanity unit is B1" | **Not agreed.** Proposed: "A washbasin sold built into its cabinet is B7 (washbasin, with cabinet as an attribute); a vanity cabinet sold without a basin is B1." |
| 22 | Dish rack | B6: B5 | B5: open | **Settle as B5** (holds tableware). |
| 23 | Water filter jug | B7: B5 | B5: open | **Settle as B5;** plumbed filters are B7. |
| 24 | Descaler | B6: B6 | B7: general descaler B6 | Agree. Softener salt is B7 under S3, and dishwasher salt is B6 (cleaning product). State both in one sentence. |
| 25 | Moisture absorber | B6: B7 | B7: no kind | **Orphan.** Add the B7 kind (B7-6). |
| 26 | Mothballs, moth repellent | B6: B8 | B8: no kind | **Orphan.** Add the B8 kind (B8-5). |
| 27 | Heated airer vs heated towel rail | B6: heated airer B6 | B7: towel radiator B7 | **Not agreed** for the plug-in heated towel rail. Proposed: "A heated rail made to warm and dry towels in a bathroom, plumbed or wired, is B7; a free-standing heated airer made to dry laundry is B6." |
| 28 | Ceiling fan with light | B3: B7 | B7: B7 | Agree. |
| 29 | Heat lamp | B3: B7 if sold as a heater | B7: none | Agree in principle; add "infrared heat lamp" to the B7 radiant heaters. |
| 30 | Pet bed, pet blanket | B1: B10 | B2: B10; B10: B10 | Agree. |
| 31 | Cat litter | B10: open (B6 or B10) | B6: silent | **Settle as B10** (made for the animal's toilet). Pet-stain cleaners are B6 under S3. |
| 32 | Bird bath, bird feeder | B4: open (B4, B10, C2) | B10: feeders B10, no bath | **Settle:** feeders, baths, nest boxes and feeding stations made for wild birds are B10; a fountain is B4 or C2. |
| 33 | Humidor; travel humidor, cigar case | B1: humidor B1 (not in tree) | B9: open | Add humidor to B1 (B1-1); cases per B9-4. |
| 34 | Aquarium and vivarium lamps, reptile thermostat | B10: B10 (S3) | B3: Q5 (special bulbs follow the appliance) | Agree if B3 Q5 is "yes". |
| 35 | Incense burner | B4: home-fragrance burner B4 | B9: not an implement | Agree; rite burners are F4. |
| 36 | Lanterns used camping, head torches | B3: B3 | (E2 not in batch) | Confirm with E2 (B3 Q3). |

**Duplicated kind names to keep apart** (rename the kinds so a builder cannot confuse them):
- "lantern": B3 fixed, B3 carried, B4 decorative;
- "spotlight": a B3 fitting and a B3 bulb;
- "futon": B1 sofa, B1 floor mattress, B2 quilt;
- "cot": B1 crib, B1 camp bed;
- "thermostat": B7 room thermostat, B10 reptile thermostat, both under S3;
- "utility knife": B5 kitchen, C1 trade (B5 boundary 1 handles it).

### C-8 Sets and kits (low: B1, B5, B6, B7, B8)

- B1 makes a set an attribute ("sold as a set").
- B5 makes it a unit-of-sale tag.
- B6 calls a washer-plus-dryer set two objects.
- B7 makes the balcony solar kit a kind.
- B8 has "burglar alarm system" and "camera system kit" as kinds.

**Proposed rule.** A set of separately usable kinds is a unit-of-sale tag, and each piece is filed as its kind. Step 3's "filed by its item of greatest value" applies only when the set is catalogued as one object. A kit is a kind only when its parts are sold to work together as one system and the trade rates or tests it as one: an alarm system graded as a system; a balcony solar kit sold under its own plug-in rules [AS]. Owner question Q-X4.

### C-9 Codes and citation format (low)

- Sub-family codes differ: B1.1 (B1), B4.1 (B4), B8.1 (B8), none (B6, B7), A1 to A14 and B1 to B7 (B9: collides). *Proposed:* `<category>.<sub-family>.<leaf>` with numbers only (B9.2.3).
- Source citation differs: S-ids (B1, B2, B5, B6, B9, B10), letter tags (B3, B7), and B10 has no URL key in the memo. *Proposed:* S-id equals the TSV row number, and every memo prints the S-id to URL key at its end, so an auditor can read the memo alone.

### C-10 Shared vocabularies between neighbours (low)

- **Bed and mattress sizes.** B1 (Sealy AU [S11], Wikipedia bed size [S25]) and B2 (bedding single to super king, Japanese semi-double [S15]) need one size table with national names, used by both.
- **Scent families.** B4 proposes the Edwards wheel, shared with H1. B9 (shisha flavour families, pipe aromatics) and J6 (tea and coffee flavour) should decide whether they join it. A smoking blend's flavour is not a scent family, so it stays a B9 attribute.
- **Order inside a leaf.** All ten memos say "canonical form first". Named forms are ordered by chronology (B1, B3, B4, B6), alphabetically (B2, B9 fallback) or by ascending grade (B8). *Proposed default:* chronology where dates are attested, ascending grade where a grade ladder exists, otherwise alphabetical.

## 4. Owner decisions raised by the B memos (merged, de-duplicated)

### Cross-category rules (decide once, apply to all B memos)

- **Q-X1.** Adopt rule T (C-2): technology and power source are attributes unless the key names the kind, or the technology changes form or installation and a source ranks the types separately? (yes / no)
- **Q-X2.** Adopt rule M (C-4) for mounting vs installation? (yes / no)
- **Q-X3.** Adopt rule R (C-3): a regional word is a kind only when no generic kind covers its form, and a region never names a sub-family or leaf? (yes / no)
- **Q-X4.** Sets and kits (C-8): set = unit-of-sale tag, and kit = kind only when rated or tested as one system? (yes / no)
- **Q-X5.** Material as the form (C-6). Choose for each case: latex mattress kind (yes / no); hide rug kind (yes / no); hot tub kinds by construction (hard-shell, inflatable, wood-fired) rather than by material (yes / no); pipes by shape (a) or by material (b)?
- **Q-X6.** Adopt one maker-ledger schema (C-1a) for every category? (yes / no) Scope per category. Choose (a) identity and platform makers only, or (b) also mass-market and consumable houses:
  - B1 designer-classic and modular makers only?
  - B6 appliance makers only, or also consumable houses?
  - B2 rug workshops and linen houses only?
- **Q-X7.** Store tiers as a typed object (scheme, value, scope, source, date), with one price-band vocabulary (budget, mid, premium, luxury), and keep market and certification out of tier? (yes / no)
- **Q-X8.** Adopt one compatibility ledger (C-1c) for caps, hive systems, device ecosystems, capsule and battery systems, with `fits` on parts? (yes / no)
- **Q-X9.** Hold large sets of named forms in registers keyed by kind (flags, tableware patterns, cigar marca-and-vitola, feed recipe lines), with only iconic ones in the tree? (yes / no)
- **Q-X10.** Brand product lines of consumables (cleaning products, e-liquids, feed recipes, cigarette brand families): named forms (a) or ledger only (b)?
- **Q-X11.** Design series that span kinds as a ledger `series`, with members as named forms per kind (C-5)? (yes / no)
- **Q-X12.** Record authenticity (licensed original, vintage original, reproduction) on named forms? (yes / no)

### Top-level axis of each category

- **Q-B1.** B1: function-first, six sub-families (yes / no). If yes, rename B1.6 "Display, division & shelter" (yes / no).
- **Q-B2.** B2: "what the textile dresses", six sub-families, with the Japan leaf removed (yes / no).
- **Q-B3.** B3: role, then placement (accepted under Q-X2), with bulbs by shape family and technology and cap as facets (yes / no).
- **Q-B4.** B4: nine ornamental families, with B4.5 re-axed to "temporary display" by form and occasion as a tag (yes / no).
- **Q-B5.** B5: stage of kitchen work, with "Serve, eat and drink at table" and "Make drinks" replacing "Serve and eat" and "Drink" (yes / no), and appliances as a generated view, never a sub-family (yes / no).
- **Q-B6.** B6: "what is cleaned or cared for", five sub-families (yes / no).
- **Q-B7.** B7: three media and twelve leaves (Candidate A) or flat job sub-families (Candidate B)?
- **Q-B8.** B8: hazard-first (A) or object-type (B)? If A: replace "Young-child hazards" with "Household injury hazards", with child as a user tag (yes / no).
- **Q-B9.** B9: role-first (products vs implements: A), substance-first (B) or route-first (C)? And Q-B9a: inside products, "substance and form" leaves (a) or form-only leaves with a substance tag (b)?
- **Q-B10.** B10: may the animal group be the first axis (yes / no)? Q-B10a: "several animals" from two groups (recommended) or three?

### Kind-level choices

- **B1.** Sofa bed and futon sofa in Seating and daybed in Sleeping (yes / no). Mattress kinds = five construction types, with German sub-types as attributes (yes / no). Traditional names (Chesterfield, Windsor, highboy) as named forms (yes / no). Nightstand in storage furniture, tables or beds? Fitted cabinetry as kinds, with installation as an attribute (yes / no).
- **B2.** Rug rule: construction = kind; city, village and tribal names = tags; travelling design names = named forms (yes / no). Blanket and throw as one kind (yes / no). Fitted carpet and rugs in one leaf (yes / no). Rug underlay: B2 or C8? Curtain poles, tracks and rings: B2 (S3) or C8? Store thread count, with the ply caveat (yes / no). Weighted blanket and orthopaedic pillow: B2 or H2?
- **B3.** Head torches, dive lights in B3, and weapon lights in E4 under S3 (yes / no). Special-purpose bulbs follow their appliance under S3 (yes / no). Non-electric lamps as placement kinds with a fuel tag (yes / no). Stone toro and unlit decorative lanterns: B4 or F4? Lamp cord sets and holders: B3; ceiling roses: C8 (yes / no). One handheld-flashlight kind with an output class (yes / no).
- **B4.** Decorative plate: (a) delete and file every plate in B5 under S5, or (b) keep a "wall plate" made only to hang in B4 (Q-B4c)? Cachepot and jardinière: C2 or B4? Shimenawa, kadomatsu, bon lanterns: B4 or F4? Fireworks and sparklers as kinds in festive and party (yes / no). Essential oils for diffusers B4, and therapy oils H2 (yes / no). Flagpole: part of the flag (S3) or C8? Regulatory and safety signs: B8 or C8? Edwards wheel as the scent vocabulary, shared with H1 (yes / no).
- **B5.** Gyuto: named form of chef's knife (a) or kind (b)? Steak and butter knives: Tableware (a) or Kitchen knives (b)? Commercial-only forms (gastronorm pan, bain-marie) as kinds with a market tag (yes / no). Sport drink bottle: B5 or E2?
- **B6.** Robot vacuum as one kind inside vacuums (yes / no). Stick and handheld as two kinds (yes / no). Washer-dryer as a kind of washing machine (yes / no). Parts (bags, filters, belts) as kinds with `fits` (a) or one parts leaf (b)? Shoe polish and waterproofing: B6 or A2? Hand-wash and antique tools as kinds now, or later?
- **B7.** Reversible split: "file by the medium delivered", with "heat pump" as a synonym (yes / no). Homes for boilers, furnaces, stoves and underfloor kits (B7 Heating, yes / no); hot-water cylinders and solar thermal (B7 Water heating, yes / no). Portable generators stay C1 per the key (yes / no). Portable power station: B7, D2 or C1? Air-quality monitor: C6 (yes / no). Shower trays, enclosures and bath panels: C8 or B7? Pool heat pumps: C2 (yes / no). Store efficiency as scheme plus value, not normalised (yes / no). Humidifier mechanism as an attribute (a) or kinds (b)? Powered handheld fan: B7, with a step 17 note (yes / no). Generated views "Period and heritage" and "Off-grid and DIY" (yes / no).
- **B8.** Personal attack alarm: B8 or E4? Fire blanket, water-leak and gas detectors: B8 (yes / no). NVR and DVR for security cameras: B8 under S3 or D1? Skin insect repellent: H1 or B8? Anti-burglar gravel, fence spikes, security film, bird spikes and netting: B8, C2 or C8? Letter plates in doors: C8, with freestanding letterboxes B8 (yes / no). Lock mechanisms as attributes (yes / no). Store only grade schemes that have a fetched source (yes / no).
- **B9.** Cigar case and travel humidor: B9 when carried, B1 when standing (yes / no). Gas cylinders and flints: C8, with hookah charcoal B9 (yes / no). Every cannabinoid consumer product is B9, intimate oils are H3 (yes / no). Loose 18650 cells: C8, with device batteries B9 (yes / no). Cannabis cultivars as named forms (yes / no). Research betel, areca, khat, bidi, herbal blends and other psychoactive plants in a follow-up round (yes / no). Cannabis scales, trays and stash jars: B9, or by task (B5, C5, B1)? Disposable vape filed as hardware (yes / no).
- **B10.** Saddle kinds by tradition, with discipline as a named form (yes / no). Poultry feed: starter, grower and layer as kinds (yes / no). Honey extraction and bottling gear: B10 or B5? Pet strollers and dog bike trailers: G1 (key order) or B10? GPS pet tracker and pet camera: D2, B8 or B10? Garden pond liners and pumps: C2 or B10? Bee suits and veils: A1 (step 13 note) or B10?

### Boundary settlements to confirm in one answer (from C-7)

Confirm all as proposed (yes / no):
- gun cabinet B8;
- light-only security floodlight B3;
- shower curtain B2;
- dish rack B5;
- water filter jug B5;
- cat litter B10;
- wild-bird feeders and baths B10;
- moisture absorber B7;
- mothballs B8;
- washbasin built into its cabinet B7;
- heated towel rail B7, with heated airer B6;
- candle holders B4, with carried lanterns B3;
- task LED strips B3, with decorative string lights B4.

## 5. Gaps the owner should know before approving

- **Markets not reached.** No memo in this domain reached China or India retail trees beyond guides. B6 and B7 used Zhihu and Sohu guides; B8 used one Baidu page and one consumer-media article.
- **Owner communities.** These are missing in B1, B4, B5 and B10; guides stand in for them.
- **Unattested kinds the key names.** Sunrise lamp (B3); fireworks, sparklers and fairy lights (B4); betel, areca, khat and herbal smoking blends (B9); energy meter (B7). These must be attested before the data phase or carried as named gaps.
- **Single-source tier and order claims.** Candle maker tiers (B4); knife steels, the espresso ladder and burr tiers (B5); bins (B6); tactical flashlight classes (B3); cigar ratings via a third-party explainer (B9); feed ratings (B10). These are adequate as modifiers with their source named. None should be presented as a consensus ladder yet.

## 6. Report

Ten B memos reviewed. All use four levels and keep tiers and makers off the tree. B10 is ready for owner review. B1 to B7 and B9 need minor fixes. B8 needs rework: its sub-family "Young-child hazards" is defined by the user, and its lock and safe kinds contradict its own choice-level table. The main issue across memos is technology and power source used as kinds in B3, B6, B7, B8 and B4 (rule T proposed). Regional words used as kinds or leaves come next (rule R), then mounting vs installation (rule M). The memos propose eight different maker-ledger schemas, so one schema, a typed tier object and a compatibility ledger are proposed. Thirteen boundaries between the B memos are settled or flagged, and five orphans are found: shiki-futon, moisture absorber, mothballs, humidor, ashtray. Owner questions are merged in section 4.
