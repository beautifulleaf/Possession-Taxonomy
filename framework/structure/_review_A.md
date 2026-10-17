# Stage 2 domain review — A (Worn & Carried)

*Batch S2R_A. Cold, offline review (no web, no git) of the memos A1 Clothing, A2 Footwear, A3 Jewellery, A4 Bags & Accessories and A5 Clocks & Watches, and their sources files verify/out/S2_A1..A5_sources.tsv. Read against BRIEF.md, framework/CATEGORIES_v0_6.md and framework/STAGE2_MEMO_TEMPLATE.md. This review does not change any memo, data or owner decision. Verdicts mean: **ready for owner** (it can go as written); **minor fixes** (the structure stands, but named defects need fixing first); **needs rework** (a level must be redesigned before the owner sees it).*

## 1. Summary table

| Code | Verdict | Top three issues |
|---|---|---|
| A1 Clothing | **minor fixes** | (1) Leaf 3.4 "Uniform sets and costumes" is set by role and occasion, which are Appendix A modifiers, and the memo admits the leaf axis "bends" there. (2) Protective equipment is "placed by body zone", but the tree gives a home only to the motorcycle helmet. Safety glasses, respirators, ear defenders, life jackets, hi-vis and chainsaw trousers have no leaf. Tailoring jackets, waistcoats, sleepwear, gloves and the baby sleeping bag are also missing. (3) The sub-family axis "coverage and layer" is two axes: Tops against Outerwear splits overshirts, fleeces and cardigans. Several kinds are also named by material (down jacket, fleece jacket, denim jacket, leather jacket). |
| A2 Footwear | **needs rework (levels 1 and 2 only)** | (1) Level 1 mixes form families with a setting ("Slippers and indoor footwear") and a use or market ("Work and safety footwear"). A safety boot is a boot by form, so it has two candidate homes. (2) The Boots leaves (ankle height; calf height and work; weather; tall) mix height, use and season, and do not follow the memo's own leaf axis ("closure or cut"). (3) The boot kinds overlap (lace-up, work, combat, hiking, motorcycle). Kinds and attributes are mixed: brogue is a kind and also "an attribute", and penny loafer sits beside loafer. Regional generic types (klompen, sabot) are named forms beside a maker model (Crocs). |
| A3 Jewellery | **minor fixes** | (1) The piercing-fit rule contradicts itself. Section 3.1 sends a nose pin sold by a jeweller to "its site", but there is no nose site. The edge-object list then sends the same nose pin to piercing-fit. The test also rests on the sales channel ("studio" against "jeweller"), which is a market modifier. (2) The tier "fine / demi-fine / fashion" is put "on the kind", but a generic kind such as a hoop earring has no tier. The tier vocabulary rests on one US retailer blog and a two-value filter. (3) The watch chain and fob are put in A3, but S3 (step 8, tried before step 17) sends a chain made for a pocket watch to A5. Regional generic types (borla, mandoria, ucu) and the kihei chain are named forms, against the memo's own rule that link patterns are attributes. |
| A4 Bags & Accessories | **minor fixes** | (1) The kinds overlap across sub-families: crossbody, messenger (A4.1) and sling (A4.2); tote and shopper; duffel, Boston and wheeled duffel; the wristlet (handbag or wallet); the Birkin (tote or top-handle). Builders will split these. (2) A4.8 "Carriers & attachments" is a catch-all (baby carriers, keyrings, canes, shopping trolleys), and canes and trolleys have no attested kind. (3) The maker tier (luxury / premium / mainstream) has no fetched source. Luggage size class is made a kind, while A1 and A2 treat size as an attribute. Regional generic types (uchiwa, sensu, sporran, furoshiki) are named forms. |
| A5 Clocks & Watches | **minor fixes** | (1) The level-2 watch precedence rule ("environment beats complication beats style") contradicts the memo's own tree. Applied as written, it would move the Daytona to racing, the GMT-Master II to pilot and the Yacht-Master to sailing. (2) The style leaves ("Dress & formal", "Sports & tough") are named by occasion and setting, and "jewellery watch" and "skeleton watch" are kinds named by decoration and finish. None has a form test. (3) Most of the border cases in owner question 4 are already decided by key order (chess clock, attendance clock, atomic clock, tower clock, pulse watch), so only the sensor-led watch needs the owner. Named forms are ordered alphabetically, while A1 to A4 order them by maker, then chronology. |

Overall: all five memos choose form as the first axis, keep makers in a ledger, and route scenes, regions, users and occasions to tags and views. That shared core is sound and well evidenced. The defects are local: mixed axes at one level, kinds that overlap, and named forms used for different things in different memos. Section 4 proposes one convention for each concept the memos handle differently.

## 2. Findings by memo

Each finding gives its severity, the memo or memos, the evidence (section or line of the memo, or the framework rule), and an exact proposed fix. Findings that span several memos are in section 3.

### A1 Clothing

**F1. (high) Leaf 3.4 "Uniform sets and costumes" is set by role and occasion.** A1, section 3 (tree 3.4) and edge object 3: "Defined by purpose (school, military, dress-up), not by form … the one place the leaf axis bends." Role, occasion and market are Appendix A modifiers, and S4 bars them from every level. *Fix:* delete leaf 3.4. File each uniform garment by its form: a school blazer under jackets, a chef's jacket under jackets, uniform trousers under trousers. Tag it `uniform: school | military | chef | …`. File a costume by its form where it has one (dress, jumpsuit, cape). Add one kind, "costume (dress-up outfit sold as a set)", under 3.2 Jumpsuits and one-piece garments, for outfits sold as a set with no single garment form. Generate "Uniforms" and "Costumes" as views. Owner question 6 then becomes yes/no on this fix.

**F2. (high) Protective equipment and several common garments have no home in the tree.** A1, section 3 edge object 1, section 4b "Protective gear", owner question 4. The memo recommends placing protective equipment "by body zone". But the tree places only the motorcycle helmet (under Headwear). Builders would split safety glasses, respirators and ear defenders (Headwear? Hands, neck and waist?), the life jacket (Vests?), hi-vis (Vests or Outerwear?) and chainsaw trousers (Trousers?). The following are also absent: blazers and sport coats (Grailed's "Tailoring" family, section 1.1), waistcoats, pyjamas and other sleepwear, bathrobes, gloves (sub-family 7 is named "Hands, neck and waist wear" but lists only scarf, necktie and belt), and the wearable baby sleeping bag that step 17 names. *Fix:* add these leaves and kinds.
- Under 5: a leaf "Sleepwear and loungewear" (pyjamas, nightdress, bathrobe, wearable baby sleeping bag) and a leaf "Hosiery" (socks, tights, stockings, leg warmers, gaiters).
- Under 3.3, renamed "Suits and tailoring": blazer and sport coat, waistcoat.
- Under 7: gloves and mittens (work, welding and fashion gloves as kinds; ski gloves are E2).
- Under 6: a leaf "Head, eye, ear and face protection" (hard hat, motorcycle helmet, cycling helmet, welding helmet, safety glasses, respirator, ear defenders).
- Life jacket and hi-vis vest go under 4.3 Vests and gilets, and chainsaw trousers under 2.2 Trousers. Each takes a `hazard_rating` attribute (EN or ISO class, to be sourced).

Then state the rule: "Protective clothing is filed by body zone and form; the hazard class is an attribute; a 'Protective equipment' view is generated."

**F3. (medium) The sub-family axis "coverage and layer" is two axes.** A1, section 3 Candidate A level table. Tops and Bottoms are set by coverage; Outerwear and Underwear are set by layer. Overshirts and shackets (placed in 1.2 Shirts), fleece pullovers against fleece jackets (4.1), cardigans against knit jackets, knit vests against 4.3 Vests, and corsets (Underwear, but worn as outerwear in goth dress; KS) all have two candidate homes. *Fix:* keep the seven sub-families and add a written tie-break to the level-1 definition: "Outerwear = a garment made to be worn over other clothing and fastened or opened at the front (jacket, coat, vest, cape); everything else is filed by coverage (Tops, Bottoms, Dresses). A garment sold under both names (shacket, overshirt) is Tops if it has shirt construction (collar, yoke, button cuffs), else Outerwear. Underwear = made to be worn under other clothing; a corset or bustier made to be worn visible is Tops." Add the same sentence to the alias table notes.

**F4. (medium) Leaf 3.5 "Robes, wraps and draped garments" is traditional dress under another name, and kimono kinds are split by formality.** A1, tree 3.5 and section 4b. The leaf holds the kurta (a long shirt), the lehenga choli (skirt and blouse set) and the ruqun (top and skirt). That is a regional grouping (Appendix A), not one of draping or wrapping. Furisode, houmongi, komon and tomesode are told apart mainly by formality and the occasion it suits (GA ranks them by "TPO"). Furisode alone differs in form (sleeve length). Yet "kimono" itself is not listed as a kind. The leaf name "Robes" will also attract bathrobes. *Fix:*
- Rename 3.5 "Draped and wrapped garments" and hold only garments made to be wrapped or draped rather than cut to fit: sari, kimono, yukata, sarong and kanga, dhoti, dupatta and stole as finished pieces.
- File the kurta under 1.2 Shirts (kind "kurta, kurti"), the lehenga choli and ruqun under 3.1 Dresses and sets as two-piece sets, and the hakama under 2.2 Trousers.
- Make "kimono" the kind. Make furisode, houmongi, komon, tomesode and iromuji named forms (non-maker designs) under it, with `formality` as an ordered attribute.
- Keep the generated "Traditional dress by region" view.

This answers owner questions 2 and 3.

**F5. (medium) Kinds are named by material.** A1, tree 4.1 to 4.3 (down jacket, down vest, fleece jacket, denim jacket, rider's or leather jacket). Mercari's "nylon" and "leather/rider's" leaves are cited as kinds in section 1.1. Material is an Appendix A modifier unless it is the form. A synthetic-fill puffer and a down puffer are the same form, and so are a trucker jacket in denim and one in corduroy. *Fix:* rename them by form: "puffer (quilted insulated) jacket" and "puffer vest", with `fill: down | synthetic` and `fill_power`; "trucker jacket", with `fabric: denim | …`; "rider's (biker) jacket", with `material: leather | …`. Keep "fleece jacket" only as a stated exception: "material is the form: a napped synthetic pile garment". Record the exception in the kind's definition.

**F6. (medium) The light-jacket and coat split rests on weight.** A1, tree 4.1 and 4.2. The tree puts the down jacket in Coats but the mountain parka and fleece in Light jackets. YA and GR have both "parka" and "heavy coats". "Light against heavy" is not a stated axis: no measurable threshold separates the two. *Fix:* divide by length: "4.1 Jackets (hip length or shorter)" and "4.2 Coats (below the hip)". This is the line Grailed draws between "Light Jackets" and "Heavy Coats" in its examples, and Mercari between jumper and blouson on one side and Chesterfield, trench and duffle on the other. The puffer jacket goes to 4.1 and the puffer coat to 4.2.

**F7. (low) The Shetland sweater contradicts the memo's own kind and named-form rule.** A1, tree 1.3 shows "[Shetland sweater (FIT, SV)]" as a named form, while section 4b says "if many makers make the type, it is a kind". *Fix:* apply the shared rule in section 4, C2: the Shetland sweater is a named form without a maker (`maker_bound = no`) under "pullover sweater", or a kind if a source shows buyers comparing Shetland sweaters against each other. Treat the OCBD, the sack jacket and the repp tie the same way, and close owner question 7 with the shared rule.

**F8. (medium) The evidence for deep outerwear kinds rests on Japan and Korea and on items marked †.** A1, section 4b "Outerwear". The deep choice level is evidenced by Mercari, Yahoo Auctions and Musinsa (JP/KR), and the Musinsa sub-category row is marked † (search excerpt only). Of the Western sources, only ASOS (Harrington, shacket, gilet) names cut-level jacket kinds. Grailed, Zalando and Vinted keep broad "jackets". Other claims are also marked †, or rest on leads: Carhartt WIP as an offshoot, Dickies' known-for kinds, the Mercari scene terms, the Zalando Designer department, the fill-power bands, and the Heddels buying order. *Fix:* in the sourcing pass, fetch one Western retailer page that lists cut-level jacket types (for example the ASOS jacket sub-tree or the Grailed outerwear leaves). Mark every kind in 4.1 whose only source is JP/KR resale as "attested in one region". Keep the deep choice level; the cut names are generic and made by many makers.

**F9. (low) The lolita print series is shown as a named form.** A1, tree note and section 7 ("Angelic Pretty 'Happy Cakes' jumperskirt"; "print series as named forms"). A print series spans several garment forms (JSK, OP, skirt) in the same way a Cartier collection spans rings and bracelets. A print is also closer to an edition or colourway than to a model. *Fix:* record a print series as a **line or collection** row in the maker ledger (convention C3). Record a release that is a specific cut in a print as a variant of the maker's JSK model, or as the named form only when the maker names the cut.

**F10. (summary of F1 to F6) Usability check, 20 objects.** Levi's 501, an OCBD, a shacket, a blazer, a suit waistcoat, a down puffer, a fleece pullover, a kurta, a lehenga choli, a kimono, a hakama, pyjamas, a bathrobe, a hi-vis vest, safety glasses, a respirator, a life jacket, a chef's jacket, a corset and a wearable baby sleeping bag. As the memo stands, **16 of 20 would split** between builders: only Levi's 501, the OCBD, the lehenga choli and the kimono (leaf 3.5) have a clear home. The shacket, blazer, waistcoat, down puffer, fleece pullover, kurta, hakama, hi-vis vest, chef's jacket and corset each have two candidate homes; pyjamas, the bathrobe, safety glasses, the respirator and the life jacket have no leaf; and the baby sleeping bag has no home. With F1 to F6 applied, every one of the 20 has a single home.

### A2 Footwear

**F11. (high) Level 1 mixes form families with a setting and a use.** A2, sections 3 and 10. Sub-families 1 to 4 are form families. Sub-family 5, "Slippers and indoor footwear", is set by where the shoe is worn: Appendix A lists "setting (indoor …)". Sub-family 6, "Work and safety footwear", is set by market and use, and holds the safety boot, the safety shoe and the safety wellington, which are a boot, a shoe and a wellington by form. The memo itself says that "certified-or-not is a spec test, not a use test" (owner question 3). Red Wing's uncertified "work boot" sits in Boots while an S3 boot sits in Work, and a chef's or nurse's clog sits in Work while "Clog" sits in Shoes. *Fix:*
- Drop sub-family 6. File every safety boot, shoe, wellington and clog by its form. Add the attribute `protection_class` (EN ISO 20345 SB, S1 to S5, plus marks; ASTM F2413 to be sourced) and generate a "Safety footwear" view.
- Keep the jika-tabi as a kind under a new leaf "Split-toe and tabi footwear" in sub-family 2, or under Boots if its shaft rises above the ankle.
- Redefine sub-family 5 by form, as "Slippers (soft, unstructured footwear without a rigid outsole)", so that the test is construction, not where it is worn.

This answers owner questions 2 and 3.

**F12. (high) The Boots leaves mix height, use and season.** A2, tree 3: "ankle height; calf height and work; weather; tall". Section 3 states the leaf axis as "closure or cut (lace-up, slip-on, strap, heel-led)", but Boots uses neither. A snow boot is calf height and also "weather"; a rain boot can be ankle height. *Fix:* make the Boots leaf axis **shaft height** only: Ankle (to the ankle bone); Mid (above the ankle, below mid-calf); Calf; Knee and over-knee. Kinds then sit by their canonical height (Chelsea and chukka at Ankle; lace-up, work, engineer, combat, hiking and motorcycle at Mid; cowboy, rain and snow at Calf). The kind keeps its name even when a model departs from the canonical height. Record height as an attribute on the named form.

**F13. (medium) The boot kinds overlap, and kinds are mixed with attributes.** A2, tree 2 and 3, and section 4b.
- The Dr. Martens 1460 and the Red Wing Iron Ranger are "lace-up boot", while the Logger and the Moc Toe are "work boot". Combat, hiking and motorcycle boots are also lace-up. The memo gives no test that separates "lace-up boot" from "work boot".
- "Brogue" is a kind under lace-up, yet the tree note and section 4b call broguing an attribute.
- "Penny loafer" is a kind beside "Loafer", but section 4b says that loafer is the kind, and Hockerty lists penny, tassel and horsebit as loafer types.

*Fix:* (a) Define "work boot" by construction, as a lace-up boot with a heavy lugged or wedge outsole made for labour (Goodyear-welted or stitchdown; Red Wing). Rename "lace-up boot" to "service and dress lace-up boot" (a plain, sleeker last). Combat, hiking and motorcycle boots stay kinds, each with a one-line form test. (b) Delete "Brogue" as a kind and make `broguing: full | semi | quarter | longwing` an attribute. (c) Make penny, tassel and horsebit loafers named forms (`maker_bound = no`) under "loafer". (d) Merge "Driving moccasin" into "Moccasin" as a named form.

**F14. (medium) Generic regional types are named forms beside a maker's model.** A2, tree 2: "Clog [Klompen; Sabot; Crocs]"; Chappal (Kolhapuri, Peshawari); section 7, "klompen, sabot, träskor as named forms". Crocs is one maker's model. Klompen and sabots are generic types made by many makers. A1's rule makes such types kinds, and A3 and A4 do the same thing in different ways. *Fix:* apply the shared convention C2 in section 4. Klompen, sabot and träskor are named forms with `maker_bound = no` and a region tag. "Crocs Classic Clog" is a maker-bound named form. The Kolhapuri and Peshawari chappals become kinds only if a fetched source shows buyers comparing makers of them.

**F15. (medium) Riding boots contradict the step-17 sport note.** A2, tree 3 (kind "Riding boot") and section 9, B10 row ("saddle shoes, riding boots and jodhpur boots worn by people are A2"). The step-17 note sends to E2 what is "made for the demands of one sport … and not suited to everyday wear", and it names "equestrian riding hats". An equestrian tall riding boot (smooth sole, spur rest) meets that test. A1 raises the same inconsistency for helmets. *Fix:* split the kind. "Equestrian riding boot (tall field and dress boot made for riding)" goes to E2. A "riding-style boot" made for everyday wear stays A2. Raise both the helmet and the boot case with the owner as one question (section 5, B2).

**F16. (medium) Several items in owner question 7 are already decided by the key.** A2, section 9 "Unresolved edge calls" and owner question 7.
- Shoe horns are made to be used with one kind of object (footwear), so step 8 and S3 send them to A2.
- Waders are made for angling (step 26 names angling and "fishing tackle") and are not suited to everyday wear, so they are E2.
- Overshoes and spats are worn on the feet, so they are A2 by the step-17 branch.

Only performance basketball and tennis shoes, and waterproofing sprays, need a ruling. Under S3, waterproofing spray is not a cleaning product (B6) and is used on more than one kind of object, so it goes to C8 unless the owner says otherwise. *Fix:* state the three decided cases as precedence sentences, and keep only the remaining two in the owner queue. Also say that orthotic inserts are H2 because step 2 is tried before step 8, so the S3 sentence about insoles does not take them.

**F17. (medium) Evidence gaps.**
- No Chinese or Korean source (the memo discloses this).
- The maker hierarchy rests on one Styleforum thread about English makers.
- The construction ranking rests on one retailer blog (Hockerty).
- EN ISO 20345 is read through a retailer blog (Colbrook), not the standard.
- Alden and Viberg appear only in search excerpts.
- The ABC-MART mapping from brand to series is inferred from position.

*Fix:* in the sourcing pass, get a second, independent source for the construction ladder (for example an r/goodyearwelt wiki page or a maker's construction page), and one Korean or Chinese retail footwear tree. Until then, label `construction` as an attribute, not a tier.

**F18. (summary) Usability check, 20 objects.** Air Force 1 Low, Air Jordan 1 High, Dr. Martens 1460, Red Wing Iron Ranger, Moc Toe 875, Timberland 6-inch, a steel-toe Chelsea boot, a Chelsea boot, a desert boot, Birkenstock Arizona, Crocs Classic Clog, Ugg Classic, a hiking boot, a trail runner, a penny loafer, a full-brogue oxford, Vans Slip-On, a backless loafer, a house slipper and an equestrian riding boot. As the memo stands, **10 of 20 would split**: the 1460, Iron Ranger, Timberland, steel-toe Chelsea, Crocs, Ugg (shearling boot or slipper), penny loafer, brogue oxford, backless loafer (mule or loafer) and riding boot. With F11 to F15 applied and a note "a backless shoe with a loafer upper is a mule", 1 of 20 would remain open: the Ugg, for which the owner question about slippers decides.

### A3 Jewellery

**F19. (high) The piercing-fit rule contradicts itself and rests on the sales channel.** A3, section 3.1. The exception paragraph says: "a decorative earring, nose pin or ear cuff sold through jewellers goes to its site". But Candidate A has no nose site, and the edge-object list says of the Tanishq nosepin against a nose stud: "the rule above sends both to Piercing-fit body jewellery". The tree also files "nose ring [Maharashtrian guchhedar nath]", a bridal ornament sold by jewellers, under piercing-fit. "Sold through jewellers" against "piercing-studio" is a market or channel test (Appendix A: market). Two builders will file a nose pin, a nath, a helix stud and an industrial bar differently. *Fix:* make the test the fitting, not the channel. "Sub-family 3 holds every ornament worn through a piercing **other than an earring made for the earlobe**: nose, lip, brow, tongue, navel, nipple and genital jewellery, cartilage barbells and labrets, and every stretched-ear piece (plug, tunnel, taper), whoever sells it. Sub-family 2 Ear holds earrings made for the lobe (hook, post-and-butterfly, hoop, huggie, clip-on, jhumka, chandbali), and ear cuffs and climbers." The nose pin, the nath and the nose ring then go to sub-family 3, renamed "Body and facial piercing jewellery". Owner question 2 becomes yes/no on this sentence.

**F20. (medium) The tier is put on the kind.** A3, section 5: "It should be a three-value tier modifier on the kind"; also "a modifier set on each kind or named form". A kind such as "hoop earring" is generic and exists at every tier. *Fix:* put `tier` (fine, demi-fine, fashion) on the named form and on the maker or line in the ledger, never on a kind (convention C4). Better still, derive it from attributes (`fineness`, plating, `stone`, `origin`) so that one reading of Borsheims cannot set it by hand. Label the vocabulary "US retail convention (Borsheims; 1stDibs two-value filter)". It needs a non-US source before it becomes a controlled list.

**F21. (medium) Watch chains and fobs conflict with S3.** A3, section 9 item 2: "a watch chain or fob worn as an ornament is A3". Step 8 (S3) is tried before step 17: "a part, attachment, accessory … made for one kind of object" goes to that object's category. A watch chain (Albert chain) is made to attach a pocket watch, so it is A5, as a watch strap is. A5 does not mention chains. *Fix:* in A3 and A5, use: "A watch chain, Albert or fob chain made to attach a pocket watch is A5 under S3; a decorative fob or seal worn on a chain without a watch is A3." Add "watch chain" to A5.5 Parts & accessories.

**F22. (medium) Named forms are used for generic regional types and for a link pattern.** A3, tree: maang tikka [Rajasthani borla, Maharashtrian mandoria]; beaded necklace [Zulu ucu]; collar necklace [Maasai beaded collar]; chain [kihei chain]. Section 4 says that "chain-link patterns (kihei, ball chain, station chain) … are attributes, not named forms", while section 4b recommends "kihei as a named form of chain". *Fix:* apply convention C2. The borla, mandoria, ucu and Maasai collar are named forms with `maker_bound = no` and a culture tag. Kihei is the value of the attribute `chain_pattern`, and Rakuten's chain-type facet supports this. Make the two sections agree.

**F23. (low) Several boundaries against neighbours in domain A are missing.**
- *Head ornaments against A1 headwear:* headbows (A1 lists lolita "KC/headbow" and "bonnet" in its alias table), fascinators, jewelled headbands and kanzashi.
- *Crowns:* the A3 "tiara; crown", the F3 "regalia and insignia of office" and the E1 "toy crowns".
- *Belt buckles sold loose:* A3 says "plain buckles are A1", but does not say where decorative buckles go.

*Fix:* (a) Adopt the boundary sentence H1 in section 3. (b) "A crown or tiara made to be worn as an ornament is A3; a crown that is regalia of an office is F3; a toy crown is E1." (c) "A buckle sold loose is made to be fitted to a belt and follows it to A1 under S3, however decorative; a buckle fixed to a belt is part of the belt." The last clause follows from S3 (step 8 before step 17).

**F24. (medium) The enthusiast evidence is thin.** A3, section 10 "Limits": no jewellery forum or wiki was reached. The Indian forms rest on culturalindia and on one retailer blog (Mirraw). The CHRIST product types come from a search excerpt. Pin badge, patch, lapel pin and hat pin are marked †. *Fix:* in the sourcing pass, fetch one jewellery community glossary (for example a costume-jewellery collectors' or a piercing community wiki). Fetch one Indian retail category page beyond Tanishq for the bridal forms, and one retailer page for pin badges and patches. Until then, mark them "named in the framework only".

**F25. (summary) Usability check, 20 objects.** A stud earring, hoop, nose pin, nath, helix barbell, ear cuff, Cartier Love bracelet, tennis bracelet, pendant necklace, Pandora Moments bracelet, locket, signet ring, engagement solitaire, brooch, lapel pin, patch, maang tikka, fascinator, body chain and bridal necklace set. As the memo stands, **7 of 20 would split**:
- the nose pin and the nath (F19);
- the Love bracelet (bangle or cuff bracelet: Cartier calls it a bracelet; the memo files it as a bangle);
- the pendant necklace (sold with its chain: pendant or necklace);
- the fascinator (A1 or A3);
- the body chain (waist chain or belly chain, which are two kinds for one form);
- the necklace set.

*Fix for the last three:* "A pendant sold on its chain is a pendant (necklaces are pieces whose ornament is the strand itself)"; merge belly chain into waist chain as aliases; file sets as in owner question 5. "Rigid and closed or hinged" is the bangle test, and the Love bracelet passes it, so it is a bangle; record "bracelet" as an alias from the maker.

### A4 Bags & Accessories

**F26. (high) The bag kinds overlap across sub-families.** A4, section 3 (A4.1 and A4.2) and the memo's own edge objects.
- The crossbody bag and messenger bag sit in A4.1, the sling bag in A4.2.
- Tote and shopper are both kinds.
- Duffel / Boston and wheeled duffel are kinds, and Zalando's "Sports bags" have no kind.
- The wristlet sits in Handbags and is also a wallet type in Wikipedia.
- The Birkin is a tote in Wikipedia and a top-handle bag in the retail typing.
- Briefcase sits in A4.4, while "laptop bag" (Zalando "Business & laptop bags") has no kind.

*Fix:* add one-line form tests and merge the near-duplicates.
1. "Shoulder bag = a single strap worn on one shoulder; crossbody bag = a strap worn across the body, a soft body, no flap fastening at the front; messenger bag = a crossbody bag with a full front flap and a wide gusset; sling bag = a single-strap pack worn on the back or chest." Move the sling bag to A4.1 beside crossbody, or move all three to A4.2, so that they are siblings.
2. Make "shopper" an alias of tote.
3. Make "sports bag" an alias of duffel.
4. File a laptop bag by form (messenger, briefcase or backpack), with `laptop_size` as an attribute.
5. The wristlet goes to A4.5 if it has card slots inside and no separate interior compartment, else to A4.1.
6. A named form goes under the kind its maker uses for it. Where the maker gives none, use the first retail category on a fetched maker page (the Birkin: to be read from Hermès' own bag pages, which the memo did not fetch).

**F27. (medium) A4.8 "Carriers & attachments" is a catch-all, and two of its members have no source.** A4, section 3 and the line "not in the tree for lack of any fetched source: fashion canes …". The sub-family holds baby carriers, keyrings, canes and shopping trolleys, which share no axis value. *Fix:* split it into "A4.8 Baby carriers" (wraps, slings, mei tai, soft structured carriers, hip seats) and "A4.9 Small carried accessories" (keyring, bag charm, fashion cane, shopping trolley). Mark the cane and the trolley "named in the framework; attestation pending".

**F28. (medium) The maker tier has no source, and luggage size is a kind.** A4, section 5: "No fetched page publishes a tier list". It proposes "luxury / premium / mainstream … one value per maker" and says that "a named form inherits the maker's tier". Section 4b makes the luggage size class (cabin, check-in) a kind, while A1 and A2 treat size strictly as an attribute. *Fix:* (a) Leave `tier` empty in the A4 ledger until a fetched source supplies one (convention C4). Do not let named forms inherit a tier: a house can have lines at several tiers. (b) Keep "suitcase" and "trunk" as kinds (trunk differs in form). Make `size_class: personal | cabin | check-in M | check-in L` an attribute, with a generated "Carry-on" view. This is the convention for size in C6. If the owner prefers size class as kinds (owner question 2), record it as a stated exception for luggage only.

**F29. (medium) Generic regional types are named forms, and one of them is not a bag.** A4, section 7: furoshiki and azumabukuro, sporran, nubi bag, bilum, lycée sac, uchiwa, sensu, tuanshan and zheshan are named forms. These are generic types made by many makers (convention C2: named forms with `maker_bound = no`). A furoshiki is a wrapping cloth, not a bag. Step 17 lists "a bag … of any kind", and the cloth reaches step 30 (B2 "made to cover … or wrap"), or C8 as packing material. *Fix:* apply C2. File the furoshiki at B2 with a cross-reference, or ask the owner whether a carry cloth counts as a bag (section 5, B5).

**F30. (low) Boundary items that the key already decides.**
- A pencil case holds several objects and is not "carried on the person as a personal accessory" in the key's sense, but step 17 lists "a bag … of any kind". The memo proposes A4.
- A toiletry or wash bag (Selfridges "Wash bags") is A4 by step 17, before H1.
- A bag charm hangs on a bag, not on the body, so it is not A3. It is an accessory made for one kind of object (bags), so step 8 and S3 send it to A4, and A3 already says so (A3, section 9 item 5).
- Clip-on sun lenses made to fit spectacles are parts of the spectacles (S3), so they are H2 when the spectacles correct vision, not A4 ("clip-on sunglasses" in A4.6).

*Fix:* write these as precedence sentences. Remove the bag-charm and toiletry-bag cases from owner question 5. Keep in the owner queue only lunch bags (already logged in _framework_conflicts.md), powered hand fans (A4 or B7) and standing umbrellas.

**F31. (low) Evidence.** The evidence is honestly disclosed but thin in places:
- the kind placement of named forms is "proposed, not attested";
- the Fashionphile and Vestiaire pages fetched thin;
- the Chinese view rests on one encyclopedia page;
- there is no source for umbrella quality, canes or trolleys.

*Fix:* in the sourcing pass, fetch the maker pages for the five most-cited named forms (Hermès Birkin and Kelly, Louis Vuitton Speedy, Chanel Classic Flap, Fendi Baguette) to attest their kind.

**F32. (summary) Usability check, 20 objects.** The Birkin, Speedy, Chanel Classic Flap, a messenger bag, a sling bag, a belt bag, a Fjällräven Kånken, a camera backpack, a Rimowa Original Cabin, a wheeled duffel, a laptop bag, a cardholder, a wristlet, a crossbody phone pouch, a Ray-Ban Wayfarer, clip-on sun lenses, a golf umbrella, an uchiwa, a toiletry bag and a tote/shopper. As the memo stands, **10 of 20 would split**:
- the Birkin, the Classic Flap (shoulder or crossbody), the messenger bag, the sling bag, the laptop bag, the wristlet, the tote/shopper and the clip-on lenses (each with two candidate kinds or categories);
- the camera backpack (left open by the memo);
- the phone pouch (A4, or D2 under S3).

With F26 and F30 applied and two more sentences, all 20 have a single home. For the phone pouch: "a pouch made to hold one phone is D2 under S3; a small bag with a phone pocket is A4". For the camera backpack: "a backpack made with fitted dividers to carry a camera and its lenses is a camera bag, D4 under S3, which names camera bags; a general backpack with a padded sleeve is A4".

### A5 Clocks & Watches

**F33. (high) The level-2 precedence rule contradicts the memo's own tree.** A5, section 3: "Environment beats complication beats style … Navitimer is a pilot's watch with a chronograph tag". Applied to the memo's own examples:
- The Rolex Daytona is a racing chronograph, and "racing watch" is a kind in A5.1.5, so the rule sends it to racing. The tree files it under A5.1.6 chronograph.
- The GMT-Master II has a pilot lineage and a multi-zone complication.
- The Yacht-Master would go to sailing watch, the Explorer to field watch, and the Santos to pilot.

The rule hangs on an "environment" judged from marketing lineage, which builders will read differently. *Fix:* adopt the memo's own alternative (owner question 2, option b) in a stricter form. Level 2 for wristwatches is the **defining complication or certified function**, tested on the object:
- *Dive:* a unidirectional timing bezel and at least 100 m, or ISO 6425.
- *Chronograph:* a chronograph mechanism.
- *Multi-zone:* a GMT or world-time display.
- *Calendar and astronomical:* an annual or perpetual calendar, or a moon phase.
- *Striking.*
- *Tourbillon and grande complication.*
- *Time-only and simple-date watches.*

Pilot, field, racing, sailing, military, dress and sports become `design_family` tags with views. The Navitimer, Speedmaster and Daytona are then chronographs, the Submariner a diver's watch, the GMT-Master II multi-zone, and the Santos, Tank, Explorer, Royal Oak and Datejust time-only. This gives one home per object without reading lineage.

**F34. (medium) The style leaves and some kinds are named by modifiers.** A5, tree A5.1.1 "Dress & formal" (occasion), A5.1.5 "Sports & tough" (setting), the "jewellery watch" (gem setting: material and decoration) and the "skeleton watch" (a finish). The F33 fix removes the first two. *Fix:* make `gem_set`, `skeleton` and `display: analogue | digital | ana-digi` attributes. Keep "digital watch" as a kind only under time-only, because its display is its form.

**F35. (medium) Most of owner question 4 is already decided by key order.**
- A chess or game clock "measures time" and step 16 is tried before step 25, so it is A5.
- An attendance clock: step 16 is tried before step 31, so A5.
- A laboratory atomic clock: step 16 is tried before step 23, so A5.
- A tower or turret clock fixed to a building: the step-4 note says "installed machines … keep their own category", so A5.
- A nurse's pulse watch made to monitor a patient: step 2 is tried before step 16, so H2.

Only the sensor-led outdoor watch (Rangeman-type, with altimeter, barometer and compass) needs a ruling. *Fix:* write these as precedence sentences, and keep only the sensor-led watch in the owner queue. A proposed default: "a watch whose main display is time and whose sensors are secondary is A5; a device whose main function is sensing or navigation is D2". That matches the step-17 note.

**F36. (low) Specifications are named forms.** A5, tree: "saturation-diver's watch [ISO 6425 Annex A]" and "military watch [MIL-W-46374]". A standard is not a model or a design. *Fix:* make `iso6425`, `iso6425_annex_a` and `mil_spec` attributes. MIL-W-46374 watches by named makers (for example a Marathon or Hamilton model, to be sourced) can be named forms.

**F37. (low) Named-form order differs from the other memos.** A5, section 8: "alphabetical order by maker then model, not by chronology". A1, A2, A3 and A4 use maker or chronology. *Fix:* adopt the shared convention C7 (by maker, then by introduction year, falling back to alphabetical when no year is attested). The memo's reason, that "model families have no clean date", is met by using the first-introduction year that the maker's own page attests.

**F38. (low) Evidence.**
- The brand-tier table compares three English-language dealer or brand blogs (Bob's Watches, The Watch Scanner, Soner). The memo rightly refuses to pick a winner.
- The point that the COSC certificate is optional, and the Chrono24 brand menu, come from search excerpts (disclosed).
- The GPHG categories come through Wikipedia.
- Some named forms in the tree have no source named (Greubel Forsey Nano Foudroyante, Vienna regulator as a named form).

*Fix:* add one non-English tier or hierarchy source (for example a Japanese or German enthusiast ranking) before tiers enter the data. Attest every named form in the tree from a fetched page, or mark it.

**F39. (summary) Usability check, 20 objects.** The Submariner, Daytona, Speedmaster, Navitimer, GMT-Master II, Royal Oak, Royal Oak Perpetual Calendar, Cartier Tank, Santos, Datejust, Explorer, Yacht-Master, G-Shock DW-5600, Casio F-91W, a Rangeman, a hunter pocket watch, a cuckoo clock, a Vienna regulator, a chess clock and an Albert watch chain. As the memo stands, **9 of 20 would split**:
- the Daytona, GMT-Master II, Santos, Datejust, Explorer and Yacht-Master (F33);
- the F-91W (digital watch or tough digital watch);
- the chess clock (left open);
- the Albert chain (A3 or A5, F21).

The Rangeman is open by the memo's own account, which makes 10. With F21, F33 and F35 applied, 1 of 20 remains open: the Rangeman, for the owner.

## 3. Cross-memo consistency findings

**X1. (high) "Named form" means five different things.** The memos use the same level for different objects:
- A1: a maker's model or an iconic design, with the rule "many makers → kind" (but the Shetland sweater is a named form; F7).
- A2: a model or an iconic design, but also generic regional types (klompen, sabot) and scene forms (bovver boot, brothel creeper, winklepicker). Colourways are explicitly *not* named forms.
- A3: a model, a collection piece, or a regional generic type (borla, ucu), plus the kihei link pattern.
- A4: a maker line or model, plus regional generic types (sporran, uchiwa, furoshiki).
- A5: a model family, specification classes (ISO 6425 Annex A, MIL-W-46374) and regional clock styles (Vienna, Black Forest). Reference numbers are left open.

BRIEF says that "specific product models, cuts and iconic designs are named forms under a kind", so a named form need not have a maker. But each memo draws the kind / named-form line differently. *Fix:* convention C2 below.

**X2. (high) Variants are handled four ways.**
- A1: the variant relation sits inside a named-form ledger (Lot 1001 / 1001XX), and print series are named forms.
- A2: a separate optional variant ledger keyed by style code, for colourways, collaborations and retros.
- A4: size variants are an attribute of the named form (Speedy 25/30).
- A5: reference numbers and colourways are an open question.

*Fix:* convention C3 (one variant ledger schema for all of domain A).

**X3. (high) Maker-ledger schemas differ.** All five memos recommend a maker ledger, with these field sets:

| Field | A1 | A2 | A3 | A4 | A5 |
|---|---|---|---|---|---|
| native-script name, aliases | yes | – | – | – | – |
| country | yes | yes | yes | yes | yes (and place) |
| founded / ended / era | yes | founded or era | era | founding era | founded, era |
| status (active, defunct, revived) | yes | – | – | – | – |
| parent group, licensee | yes | – | – | – | group |
| maker class or house type | – | – | yes | – | yes |
| lines or collections | separate table | in-house lines field | collections and the forms they span | line names | – (series in known-for) |
| known-for kinds / named forms | kinds | both | both | both | both |
| scene tags (core / adjacent) | yes, with strength | yes | yes | yes | yes |
| tier | one value | consensus tier with source; resale tier (dated) | one value | one value, inherited | per source, with a disputed flag |
| price band | yes | yes | yes | yes | yes |
| category-specific | – | construction | mark or hallmark notes | – | movement policy, certifications |
| sources | URL, second if any | per row | URL | URL | per row |

*Fix:* convention C1, one shared core schema with category extension columns.

**X4. (high) The tier is placed and stored differently.**
- A1: on maker and line, vocabulary open.
- A2: on the maker, with source, for dress shoes and boots only.
- A3: on the *kind* (F20).
- A4: one value per maker, inherited by named forms, and unsourced (F28).
- A5: one entry per source with a disputed flag.

Grailed's Core / Grails / Hype / Sartorial is a "consensus" tier in A1 and "not quality tiers" in A2. *Fix:* convention C4. A5's model is the right one, and Grailed's labels become a dated platform tag.

**X5. (medium) Regional and traditional forms are handled four ways.** As kinds (A1 sari and kimono types; A2 geta, zori and opanak; A3 maang tikka and mangalsutra), as named forms (A2 klompen; A3 borla and ucu; A4 sporran, uchiwa and furoshiki), and as a leaf of their own (A1 3.5). *Fix:* convention C2(c).

**X6. (medium) The leaf level and "one axis per level" are interpreted differently.**
- A1 skips the leaf in three sub-families.
- A2 uses the leaf only in Shoes and Boots ("maximum depth three, optional fourth").
- A3 always has four levels.
- A4 never has a leaf (maximum three).
- A5 uses a different leaf axis in different sub-families (function for watches, placement for clocks).

All of these stay within "at most four levels". But they read "one stated axis per level" as *one axis per level within each sub-family*, and that reading is not written down anywhere. *Fix:* convention C5, and an owner yes/no on that reading (section 5, A1).

**X7. (medium) S3 parts have a home in A5 only.** A5 has a parts sub-family (A5.5: straps, dials, movements, one-watch winders). A2 sends laces, insoles, shoe trees and heel grips to A2 under S3 (section 9) but its tree has no place for them. A4 does not mention replacement straps, bag organisers or bag charms (bag charms are A4, F30). A1 does not mention replacement hoods, detachable linings or collar stays. *Fix:* convention C5(c). Each A category gets a last sub-family, "Parts and accessories made for one <object>", with kinds such as laces, insoles, shoe trees and heel grips (A2); bag straps, organiser inserts and bag charms (A4); and straps, bracelets, dials, movements, crystals, cases, winders and watch chains (A5). A1 and A3 do the same only if the sourcing pass finds such parts sold on their own (detachable linings, replacement clasps). Otherwise they are C4 notions and findings.

**X8. (medium) Named-form order differs.** A1: maker, then year. A2: chronology. A3: chronology. A4: maker, then chronology. A5: alphabetical by maker, then model. *Fix:* convention C7.

**X9. (medium) Boundaries between neighbours in domain A that do not agree on both sides, or are stated on one side only.**

| Pair | A side | Other side | Proposed single sentence |
|---|---|---|---|
| A3 / A5 watch chains | A3: chain or fob → A3 | A5: silent | **W1.** "A watch chain or fob chain made to attach a pocket watch is A5 under S3; a fob, seal or charm worn without a watch is A3." (F21) |
| A1 / A3 head ornaments | A1: headbow (KC) and bonnet in the lolita alias table; P4 does not cover hair | A3: "hair ornaments"; owner question 9 on decorative hairbands | **H1.** "Worn on the head and held by its own band, crown, elastic or ties (hat, bonnet, headband, headbow on a band, fascinator on a band or headpiece) is A1 headwear; fixed into the hair by a pin, comb, clip or slide (hairpin, kanzashi, jewelled clip, hair comb, bow on a clip) is A3; plain functional clips, ties and bands are H1." |
| A1 / A3 buckles | A1: belts A1 | A3: "plain buckles are A1" | **K1.** "A belt buckle, plain or decorative, is a part of a belt and is A1 under S3." (F23) |
| A1 / A2 equestrian | A1: riding hats E2 (key) | A2: riding boots A2 | One rule for both (F15; owner question B2). |
| A1 / A2 hosiery | A1 P3: "hosiery is A1, anything else worn on the feet is A2" | A2: socks, tights, leg warmers and gaiters are A1; spats, galoshes and overshoes are A2 | Agree. Add "tabi socks are A1; jika-tabi with a rubber sole are A2" to both. |
| A3 / A4 bag charms | A3: "keyrings and bag charms are A4" | A4: "a charm hung on a bag has no named step (flag)" | Agree on A4. The reason is S3 (step 8): an accessory made for bags. Remove A4's flag. |
| A1 / A4 packs and vests | A1 P5: chest rigs and waist packs A4; vest-form garments with pockets A1 | A4: belt bags A4 | Agree. Copy P5 into A4 section 9. |
| A4 / A1 / H2 eyewear | A1 P6 | A4 boundary 2 | Agree. Add the clip-on lens sentence (F30) to both. |
| A4 / A5 watch storage | A4: watch straps follow the watch | A5: boxes and rolls for several watches B1, a winder for one watch A5 | Agree. Add "watch roll" to A5's B1 sentence. |
| A3 / A5 jewellery watches | A3: watches A5 | A5: a gem-set watch is A5 | Agree. |

**X10. (low) Duplicated or orphaned kinds across the domain.**
- *Orphans named by the key or by a memo's boundary text, with no kind in any tree:* the wearable baby sleeping bag, gloves, gaiters and leg warmers (A1; F2); overshoes, galoshes and spats (A2 says A2 but its tree has no kind); the fashion cane and the shopping trolley (A4; F27); shoe laces, insoles and shoe trees (A2; X7).
- *Possible duplicates:* "belly chain" and "waist chain" (A3); "longcase" and "grandfather clock" (A5 handles these as synonyms); "shopper" and "tote" (A4); "trench watch" (A5.1.4 kind) and "wristlet" (A4 handbag and wallet type). These are different objects under one word. Add the word to the alias table as a homonym with two targets.
- *Material-named kinds* in A1 (F5) and A2 ("shearling boot", "plimsoll and canvas shoe"): apply the same "material is the form" test in both. Rename the shearling boot "sheepskin-lined pull-on boot" or record it as a stated exception.

**X11. (low) Scene vocabularies overlap but are separate.** A1 sets up scene tags with governance (core or adjacent, sources from MFA and Subculture Wiki). A2 proposes scene labels (skate, workwear, punk, classic menswear, streetwear) that it says are "not attested". A4 uses courier, biker and workwear, and streetwear. A3 and A5 use maker-type and era tags instead. *Fix:* convention C8, one shared scene vocabulary for domain A.

## 4. Proposed shared conventions for domain A

These conventions resolve X1 to X11. Each is phrased so that the owner can approve it once for all five categories. Later domains can reuse them.

**C1. Maker ledger: one core schema and per-category extensions.**
- *Core columns (every category):* `maker_id`; `name`; `native_name`; `aliases`; `maker_class` (house or manufacture; independent; microbrand; retail own-label; licensee or diffusion; costume or fashion brand; artisan or atelier; supplier, such as a movement or fabric maker); `country`; `place`; `founded`; `ended`; `status` (active, defunct, revived); `parent_id` (group or licensor); `known_for_kinds` (kind ids); `scene_tags` (with `core` or `adjacent` strength, from C8); `price_band` (C4); `sources` (at least one fetched URL, and a second where available).
- *Separate tables, not columns:* **lines and collections** (`line_id`, `maker_id`, name, the kinds it spans, `tier` entries, years, sources: Momotaro Classic, Cartier Love, Seiko Prospex Sea, an Angelic Pretty print series, Rimowa Original); **tier entries** (C4); **named forms** (C2); **variants** (C3).
- *Extensions (category columns, optional):* A2 `construction_policy`; A3 `marks` (maker's marks and hallmark notes); A5 `movement_policy` and `certifications`.
- *Why:* A1's table is the fullest; A3 adds maker class and collections across forms; A5 adds per-source tiers. Putting known-for named forms in a column (as A2, A3, A4 and A5 do) duplicates the named-form ledger. Derive it from that ledger instead.

**C2. Kind against named form.**
- (a) The choice-level test in section 4b decides kind against named form. A **kind** is the level at which buyers compare quality or makers. A **named form** is a specific design below it. It is either **maker-bound** (a model or line: Levi's 501, Iron Ranger, Speedy, Submariner) or **not maker-bound** (a generic cut, iconic design or traditional variant that many makers make: penny loafer, Shetland sweater, klompen, furisode, kihei-style chain if kept, uchiwa, Vienna regulator). Record it with the field `maker_bound: yes | no`. This replaces A1's rule "many makers → kind". The number of makers is not the test; comparison is.
- (b) **Not named forms:** specifications and certifications (ISO 6425, MIL-W, EN ISO 20345 classes: attributes), link patterns, motifs and prints (attributes or variants), sizes (attributes), and colourways, reference numbers, collaborations and editions (variants, C3).
- (c) **Traditional and regional types** are kinds when a fetched source shows them sold or compared as their own category (sari, kurta, kimono, geta, maang tikka, mangalsutra, jhumka). Otherwise they are non-maker named forms under the nearest generic kind (borla under maang tikka; klompen under clog; uchiwa under rigid fan; sporran under pouch or belt bag). In both cases they carry a `region` or `culture` tag and appear in a generated "by tradition" view. Never put them in a leaf of their own (F4).

**C3. Variant ledger (optional, sparse, one schema).** Columns: `variant_id`, `named_form_id`, `variant_code` (maker's style code, lot or reference number: Lot 1001XX, IQ5495-005, a Submariner reference), `variant_type` (colourway; material; print; size; reference; retro or re-issue; collaboration; limited edition), `partner` (for collaborations), `year`, `sources`. A variant is never a level and never a kind. It is filled only where an owner-emphasis scene needs depth (sneakers, Japanese denim, lolita prints, watch references).

**C4. Tier and price band.**
- (a) A `tier` never sits on a kind. It sits on a maker, a line or a named form, as **tier entries**: (`subject_id`, `scheme`, `value`, `source_url`, `date`). A subject may have several entries from different sources, with a computed `disputed` flag (A5's model). A named form does not inherit a maker's tier unless an entry says so.
- (b) A spec ladder that is measured on the object (EN ISO 20345 class, COSC level, metal fineness, fill power, denim weight, Super number) is an **attribute** with its standard named, not a tier entry.
- (c) A platform's own segment labels (Grailed Core / Grails / Hype / Sartorial; StockX premium) are a dated `platform_tag`, not a tier.
- (d) A **price band** is one domain-wide scheme in one currency, so that A1 ($ to $$$$$), A5 (Jomashop USD bands) and A2, A3 and A4 (unspecified) share bands. Proposed: USD bands under 50, 50–150, 150–500, 500–1,500, 1,500–5,000, 5,000–15,000 and over 15,000. They are derived from a dated, sourced list price.
- (e) A tier scheme enters the data only with at least one fetched source, and preferably a second from another region (A3 and A4 fail this today).

**C5. Levels and axes.**
- (a) Fixed level names: category, sub-family, leaf, kind, named form. At most four levels below the category, and the named form counts as one of them.
- (b) A sub-family may skip the leaf level when it holds about 12 kinds or fewer. The data then stores the kind with `leaf = null`, not under a dummy leaf.
- (c) "One stated axis per level" is read as one axis per level **within each sub-family**. Each sub-family states the axis of its leaf level in its definition (A5: function for watches, placement for clocks; A2: shaft height in Boots, closure in Shoes).
- (d) Each A category ends with a sub-family "Parts and accessories made for one <object>" for the S3 items it receives (X7). It is the only sub-family exempt from the level-1 axis.

**C6. Size, fit and user.** Size (garment size, shoe size, ring size, case diameter, luggage size class, frame size) is always an attribute with its standard (ISO 8559-1, ISO 19407, ISO 8653, ISO 8624, airline bands). User (gender, child, baby, adapted) is always a tag with generated department views. Luggage size class is the only proposed exception (owner question A4-2).

**C7. Order inside a leaf.** Kinds go canonical form first, then the secondary key that the sub-family states (spec, height, formality or complexity). Named forms go by maker (in the order of the maker ledger's `name`), then by first-introduction year as attested, then alphabetically where no year is attested. Variants go by `variant_code` or year.

**C8. One scene vocabulary for domain A.** One controlled list of `scene_tags`, each with a definition source (an MFA style guide, a Subculture Wiki page, or a community wiki), `core` or `adjacent` strength, and tagging at the maker, kind and named-form levels, without automatic inheritance (A1, owner question 9). A2 and A4 use this list instead of their own labels. A tag that has no source is held back (A2 already says its labels are "not attested").

**C9. Alias and homonym table.** One table: `term`, `language` and `script`, `target_id`, `relation` (alias, regional name, homonym). For example: JSK = jumper dress; スカジャン = souvenir jacket; カバーオール = chore coat (JP), but coverall = boiler suit (US); longcase = grandfather clock; shopper = tote; wristlet → two targets. The labels are English, with a native-script label (A1, owner question 11).

## 5. Owner decisions raised by the memos (merged and de-duplicated)

Memo question numbers are given in brackets. Each one is phrased as yes/no or as a choice; where this review recommends an answer, the recommendation is given after the question.

### A. Shared conventions (decide once for domain A)
1. **Levels.** Approve C5: at most four levels below the category with the named form as one of them; the leaf level optional per sub-family; "one axis per level" read as one axis per level within each sub-family. Yes/no. [A1-13, A2 section 10, A4 section 3, A5 section 3]
2. **Kind against named form.** Approve C2: the choice-level test decides; named forms are maker-bound or not; specs, sizes, prints and colourways are never named forms. Yes/no. [A1-7, A2-5, A3-3, A4-7, A5-6]
3. **Traditional and regional forms.** Kinds when sold or compared as their own category, otherwise non-maker named forms; always with a region tag and a "by tradition" view; never a sub-family or leaf of their own. Yes/no. [A1-2, A2-6, A3-3]
4. **Historical-only styles** (poulaine, chopine, caliga; antique-only clock forms). In scope as kinds or named forms when people own replicas or originals, or only as a "historical" tag on existing kinds? Choice. [A2-6]
5. **Variant ledger.** Approve C3: one optional variant ledger for colourways, references, prints, collaborations and editions. Yes/no. [A2-5, A5-6, A1 named-form ledger]
6. **Tier storage.** Approve C4(a) to (c): tiers never on kinds; entries per source with a disputed flag; spec ladders as attributes; platform segments as dated tags. Yes/no. [A1-8, A3-8, A5-5]
7. **Tier vocabularies.** One domain-wide tier scale, or a scale per category (A1 mass … archive; A3 fine / demi-fine / fashion; A4 luxury / premium / mainstream; A5 per-source schemes)? Choice. Recommended: per category, stored per source.
8. **Price band.** One domain-wide USD band scheme (C4(d)), or bands per category? Choice.
9. **Maker ledger.** Approve the C1 core schema with category extensions and separate line, tier and named-form tables. Yes/no. [A1-10, A3-8, A2, A4, A5 section 6]
10. **Maker-ledger seed.** Seed from the makers named in the owner-emphasis scenes, or crawl retailer brand lists (Musinsa alone lists 3,708)? Choice. Include retailers' own labels (Uniqlo, ZARA) as makers without named forms? Yes/no. [A1-10]
11. **Scene vocabulary.** Approve C8: one shared, sourced list with core and adjacent strength, tagged at maker, kind and named-form level, with no automatic inheritance. Yes/no. [A1-9]
12. **Alias table and labels.** Approve C9 (English label plus native-script label; homonyms with two targets). Yes/no. [A1-11, A5-9]
13. **User and department.** Confirm that gender, child and baby are tags with generated department views in every A category, including children's clothing in A1. Yes/no. [A1-12, A5-8]
14. **Parts sub-family.** Approve C5(d): each A category ends with a parts sub-family for the S3 items it receives; boxes and rolls holding several items stay B1. Yes/no. [A5-3]

### B. Framework changes (for the next CATEGORIES revision)
1. **Swimwear.** The key sends "swimming costumes" to E2. Should this mean only competition and sport swimwear (racing suits, wetsuits), with bikinis, swim trunks and beachwear staying A1? Yes/no. [A1-5]
2. **Equestrian and cycling gear.** The key puts cycling helmets in A1 but equestrian riding hats in E2. Align them: either all riding and cycling helmets are A1 protective equipment, or equestrian helmets and tall riding boots are E2 and cycling helmets stay A1. Choice. [A1-5, F15]
3. **Watch chains and fobs.** Adopt W1 (watch chains A5 under S3; fobs worn without a watch A3). Yes/no. [F21]
4. **Head ornaments.** Adopt H1 (banded headwear including fascinators and headbows A1; pinned or clipped ornaments A3; plain clips, ties and bands H1). Yes/no. Separately: is a stick-on bindi or temporary jewel A3 or H1? Choice. [A3-9]
5. **Furoshiki and other carry cloths.** A bag (A4) or a wrapping textile (B2)? Choice. [F29]
6. **Lunch bags and cool bags** (already logged in _framework_conflicts.md). Adopt "insulated lunch and cool bags are B5". Yes/no. [A4-5]
7. **Pencil cases and toiletry bags.** A4 by step 17 (recommended), or C5 and H1? Choice. [A4-5]
8. **Powered handheld fans.** A4 (hand fan) or B7 (fans)? Choice. **Beach and patio umbrellas.** B1 or C2? Choice. [A4-5]
9. **Prescription sunglasses** are H2 because they correct vision. Confirm. Yes/no. [A4-5]
10. **Prayer-bead necklaces and malas.** F4 if sold as prayer beads, A3 if sold as a necklace (the memo's rule), or always F4? Choice. [A3-6]
11. **Gold-ingot pendants and coin jewellery.** A3 when made with a bail or loop for wearing, F3 when it is bullion or coin without a mount (a form test, not "kept as bullion")? Yes/no. [A3-7]
12. **Sensor-led outdoor watches** (altimeter, barometer, compass). A5 when time is the main display, D2 when sensing or navigation is the main function? Yes/no. [A5-4]
13. **Performance basketball and tennis shoes.** E2 only when sold as performance or court models with sport-specific soles; A2 for lifestyle retros? Yes/no. [A2-7]
14. **Shoe waterproofing sprays.** C8 (not a cleaning product, used on several kinds of object) or B6? Choice. [A2-7]

These are already decided by the key, so they need no owner decision; record them as precedence sentences:
- shoe horns (A2) and waders (E2) [F16];
- chess and game clocks, attendance clocks, laboratory atomic clocks and tower clocks (A5), and pulse watches made to monitor a patient (H2) [F35];
- bag charms (A4) and clip-on lenses for corrective spectacles (H2) [F30];
- loose belt buckles (A1) [F23].

### C. Per-category structure
- **A1-1** Adopt Candidate A (form-first, seven sub-families, with the F3 tie-break). Yes/no.
- **A1-2** Leaf 3.5 renamed "Draped and wrapped garments", holding draped and wrapped garments only, with the kurta in Shirts, the lehenga choli in Dresses and sets, the hakama in Trousers, and kimono types as named forms under "kimono" (F4). Yes/no. [A1-2, A1-3]
- **A1-3** Protective equipment filed by body zone and form, with `hazard_rating` and a generated view; no protective sub-family (F2). Yes/no. [A1-4]
- **A1-4** Delete the uniforms and costumes leaf, and file each garment by form with a uniform or costume tag (F1). Yes/no. [A1-6]
- **A1-5** Confirm that gaiters, leg warmers, arm sleeves, the obi and the dupatta are A1 (F2 places them). Yes/no. [A1-14]
- **A2-1** Adopt form families at level 1 (sneakers, shoes, boots, sandals, slippers by construction), with work and safety footwear as a certification attribute and view rather than a sub-family (F11). Yes/no. [A2-1, A2-2, A2-3]
- **A2-2** Dress-shoe kinds by lacing and cut (oxford, derby, monk, loafer), with broguing and toe-cap as attributes; or toe-cap patterns as kinds (ABC-MART)? Choice. [A2-4]
- **A2-3** Mules and clogs as kinds under Shoes, or with sandals? Choice. [A2-8]
- **A2-4** Minimalist and barefoot shoes as a kind in Sneakers, or an attribute? Choice. [A2-9]
- **A3-1** Two-step top (site, then form family) or flat form leaves (Candidate B)? Choice. [A3-1]
- **A3-2** Adopt the piercing-fit rule by fitting, not channel (F19). Yes/no. [A3-2]
- **A3-3** Wedding bands and engagement rings as occasion tags on band and solitaire rings (Appendix A), or as kinds? Choice. Recommended: tags. [A3-4]
- **A3-4** Jewellery sets filed under the principal piece with contents recorded, or as a kind "jewellery set"? Choice. [A3-5]
- **A4-1** Hardside and softside as an attribute (recommended) or as kinds? Choice. [A4-1]
- **A4-2** Luggage size class (cabin, check-in) as an attribute with a view (F28, C6), or as kinds as the memo proposes? Choice. [A4-2]
- **A4-3** Eyewear frame shape as a kind, shared by name with H2 frames, which are filed by whether they correct vision? Yes/no. [A4-3]
- **A4-4** Home rule for a named form that sources place under two kinds: the maker's own category on a fetched maker page (F26). Yes/no. [A4-4]
- **A4-5** One home each for the wristlet (by the F26 test) and for the two chain wallets (the belt-chain wallet in Wallets; the wallet on chain in Wallets as a named-form group). Yes/no. [A4-6]
- **A4-6** Rare silhouettes (Modalina's 104) as named forms unless a source compares them. Yes/no. [A4-7]
- **A4-7** Split A4.8 into Baby carriers and Small carried accessories (F27). Yes/no.
- **A5-1** Movement and power as attributes only, with no horology exception. Yes/no. [A5-1]
- **A5-2** Watch level 2 by defining complication or certified function, with pilot, field, racing, sailing, dress and sports as design-family tags (F33); or keep the memo's environment-first precedence? Choice. [A5-2]
- **A5-3** Fashion watches and tie-in or collaboration editions as maker-type and variant tags, not kinds. Yes/no. [A5-7]

## 6. Report

All five memos in domain A put garment or object form first, carry makers in ledgers, and send scenes, regions and users to tags and views. That core is sound and attested in several regions. Verdicts: A1, A3, A4 and A5 need minor fixes; A2 needs rework of levels 1 and 2 only.

The high-severity defects are:
- a role-based leaf, and protective equipment with no home (A1);
- setting and use sub-families, and mixed boot leaves (A2);
- a self-contradictory piercing rule (A3);
- overlapping bag kinds (A4);
- a watch precedence rule that contradicts its own tree (A5).

Across the memos, "named form", variants, tiers and the maker-ledger schema are handled inconsistently. Section 4 proposes nine shared conventions (C1 to C9). Section 5 merges 49 memo questions into 14 shared, 14 framework and 23 per-category decisions. Ten further cases are already decided by the key.
