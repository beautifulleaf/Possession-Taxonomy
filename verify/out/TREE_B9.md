# B9 Smoking & Vaping: decided tree

Category: B9 Smoking & Vaping (domain B, Home). Membership test (placement key step 27): tobacco, nicotine and cannabis products in any form, and other plant products taken for a stimulant or psychoactive effect rather than as food or drink (cigarettes, cigars, loose, pipe and chewing tobacco, snuff, snus and nicotine pouches, heated-tobacco sticks, e-liquids and pods, cannabis flower, resin, concentrates, edibles, drinks, tinctures and CBD products, herbal smoking blends, betel quid and areca nut sold for chewing, khat, kratom), or implements made for smoking, vaping or preparing these (pipes, bongs, hookahs and hookah coals, vapes, pocket lighters, ashtrays, cigar cutters, cigarette cases, rolling papers and machines, herb grinders), and the parts and accessories made for one B9 object. Structure (B-10, Candidate A): sub-family (the role of the object to its owner: a product that contains the substance, or an empty implement made to hold, burn, heat, light, roll, cut or carry it; then the closing parts sub-family, exempt from that axis, CV-17), then leaf (products by the form of the product; implements by the job done in use; no leaf for parts), then kind (the generic type buyers compare on quality or maker). Each object gets one kind. Substance (tobacco, non-tobacco nicotine, cannabinoid, other plant) is a required tag on every product kind and named form and a generated view, never a leaf; route is a tag and a view. Maker, brand and brand lines (cigarette and e-liquid lines are maker-ledger lines, CV-46), cannabis cultivar (shared variety table, CV-44), platform and compatibility (C13), legal status and legal class (jurisdiction ledger, C17), origin, wrapper shade, cigar strength and size (length, ring gauge), construction, tobacco cut (flake, ribbon, plug), in production, draw style (MTL, DTL), cannabinoid content, nicotine strength, portion size, paper size, material, finish, grain, stem length (churchwarden), price band, tier, scene and era are attributes, tags, ledgers or views, never kinds. Display only (proposals.tsv row B9): the level-1 groups (Cigars and cigarillos; Pipes and pipe tobacco; Cigarettes and roll-your-own; Vapes and e-liquids; Heated tobacco; Snus, nicotine pouches and other oral products; Cannabis and hemp; Hookah and shisha; Lighters, cutters, ashtrays and cases; Other plant products) regroup the role-first leaves for shoppers and never move a home; each leaf names its group. Inside Cigars, "Parejos" and "Figurados" are display groups only; figurado is never a kind. A kind marked † is named only by the key, a decision or a search excerpt and needs a fetched page before it enters the data; several kinds are provisional (noted in their lines).

Ids (R-58): B9.n is a sub-family and B9.n.m a leaf; a kind is B9.n.m.kk, or B9.n.kk where a sub-family has no leaf.

## B9.1 Products
Leaf axis: the form of the product (the object contains the substance and is used up or taken); substance is a required tag, never a leaf (B-10).

### B9.1.1 Cigarettes & pre-rolls
Kind axis: construction. Display group: Cigarettes and roll-your-own; pre-rolls are displayed in Cannabis and hemp.
- B9.1.1.01 Filtered cigarette: manufactured cigarette of cut tobacco in a paper tube with a filter tip.
- B9.1.1.02 Plain cigarette: manufactured cigarette with no filter.
- B9.1.1.03 Clove cigarette [kretek]: cigarette of tobacco blended with cloves.
- B9.1.1.04 Pre-roll: ready-rolled smoke of cannabis or other plant material, including the joint and the pre-rolled blunt.
- B9.1.1.05 Infused pre-roll: pre-roll whose material is coated or mixed with a concentrate.
- B9.1.1.06 Bidi: thin hand-rolled smoke of tobacco wrapped in a leaf and tied with thread (provisional until attested, B-31). †

### B9.1.2 Cigars
Kind axis: the generic vitola (shape and size class), parejos by size, then figurados (section 14). Display group: Cigars and cigarillos; inside it, B9.1.2.01 to B9.1.2.11 display as "Parejos" and B9.1.2.12 to B9.1.2.16 as "Figurados".
- B9.1.2.01 Corona: the benchmark straight-sided cigar, about 5.5 to 6 inches by ring gauge 42 to 44.
- B9.1.2.02 Petit corona [Mareva]: short straight-sided corona-gauge cigar.
- B9.1.2.03 Corona gorda: corona-length cigar of a thicker gauge.
- B9.1.2.04 Lonsdale: long, slender straight-sided cigar (provisional until a page shows it, section 14). †
- B9.1.2.05 Robusto: short, thick straight-sided cigar.
- B9.1.2.06 Toro: medium-long straight-sided cigar of a thick gauge.
- B9.1.2.07 Churchill [Julieta No. 2]: long straight-sided cigar of a medium-thick gauge.
- B9.1.2.08 Double corona: very long straight-sided cigar of a thick gauge.
- B9.1.2.09 Gordo [Grande]: straight-sided cigar of a very large ring gauge.
- B9.1.2.10 Panatela: long, thin straight-sided cigar.
- B9.1.2.11 Lancero: very long, very thin straight-sided cigar.
- B9.1.2.12 Torpedo [Pyramid, Pirámide]: figurado tapering to a pointed head.
- B9.1.2.13 Belicoso: figurado with a short tapered, rounded head.
- B9.1.2.14 Perfecto: figurado tapered at both ends, bulging in the middle.
- B9.1.2.15 Diadema [Salomón]: very large figurado with a tapered head and a closed or tapered foot.
- B9.1.2.16 Culebra: three thin cigars braided together and sold as one.

### B9.1.3 Cigarillos & little cigars
Kind axis: the object itself. Display group: Cigars and cigarillos.
- B9.1.3.01 Cigarillo: small, thin cigar.
- B9.1.3.02 Little cigar: cigarette-sized cigar wrapped in tobacco leaf or leaf-based paper, usually filtered.

### B9.1.4 Pipe tobacco
Kind axis: blend family (section 14). Display group: Pipes and pipe tobacco.
- B9.1.4.01 Virginia blend: pipe tobacco blend led by Virginia leaf.
- B9.1.4.02 Virginia/Perique blend: Virginia-led blend with Perique leaf.
- B9.1.4.03 Burley-based blend [American blend]: pipe tobacco blend led by Burley leaf (merge with American blend provisional, section 14).
- B9.1.4.04 English blend [Balkan]: unflavoured blend with Latakia and oriental leaf.
- B9.1.4.05 Aromatic blend: pipe tobacco blend flavoured or cased for aroma.

### B9.1.5 Loose plant material
Kind axis: material and cut. Display group: fine-cut and kizami in Cigarettes and roll-your-own; flower in Cannabis and hemp; the other kinds in Other plant products.
- B9.1.5.01 Fine-cut roll-your-own tobacco: loose finely cut tobacco sold for hand-rolling or filling tubes.
- B9.1.5.02 Kizami [kizami]: Japanese very fine-cut tobacco leaf for the kiseru (regional kind, C11; provisional until attested in a second region).
- B9.1.5.03 Flower: dried cannabis flower sold loose.
- B9.1.5.04 Kratom powder: dried and ground kratom leaf, the dried leaf included.
- B9.1.5.05 Herbal smoking blend: loose non-tobacco herbal mixture sold for smoking (provisional until attested, B-31). †
- B9.1.5.06 Dried opium: dried opium poppy product taken for a psychoactive effect (K-168; provisional until attested). †
- B9.1.5.07 Salvia: dried salvia divinorum leaf or extract taken for a psychoactive effect (K-168; provisional until attested). †
- B9.1.5.08 Psychoactive mushroom product: dried psychoactive mushroom material (K-168; provisional until attested). †

### B9.1.6 Hookah shisha
Kind axis: the object itself. Display group: Hookah and shisha.
- B9.1.6.01 Shisha tobacco: moist, usually flavoured tobacco for smoking in a hookah.
- B9.1.6.02 Tobacco-free shisha: shisha of non-tobacco material for the hookah, filed with the form it imitates.

### B9.1.7 Heated tobacco
Kind axis: the object itself. Display group: Heated tobacco.
- B9.1.7.01 Heating stick: tobacco or tobacco-free stick made to be heated, not burned, in a heated-tobacco device.
- B9.1.7.02 Capsule-type heated product: heated product in which vapour passes through a tobacco capsule.

### B9.1.8 Oral & nasal products
Kind axis: degree of processing, tobacco and non-tobacco together. Display group: Snus, nicotine pouches and other oral products; betel quid, areca nut and khat in Other plant products.
- B9.1.8.01 Chewing tobacco: loose leaf, plug or twist tobacco made for chewing.
- B9.1.8.02 Dry snuff: finely ground dry tobacco taken through the nose.
- B9.1.8.03 Moist snuff [dip]: moist ground tobacco placed between lip and gum.
- B9.1.8.04 Loose snus: moist, unportioned snus.
- B9.1.8.05 Original portion snus: snus in moist portion bags.
- B9.1.8.06 White portion snus: snus in drier, lighter portion bags.
- B9.1.8.07 Dissolvable: tobacco product made to dissolve in the mouth.
- B9.1.8.08 Nicotine pouch: tobacco-free portion pouch holding nicotine.
- B9.1.8.09 Nicotine pearl: small tobacco-free nicotine bead for the mouth.
- B9.1.8.10 Nicotine toothpick: toothpick infused with nicotine.
- B9.1.8.11 Betel quid: areca nut with additions wrapped in betel leaf, sold for chewing (provisional until attested, B-31). †
- B9.1.8.12 Areca nut: areca nut sold for chewing (provisional until attested, B-31). †
- B9.1.8.13 Khat: khat leaf sold for chewing (provisional until attested, B-31). †

### B9.1.9 E-liquids & prefilled cartridges
Kind axis: nicotine chemistry, then prefilled units. Display group: Vapes and e-liquids.
- B9.1.9.01 Freebase e-liquid: e-liquid with freebase nicotine.
- B9.1.9.02 Nic-salt e-liquid: e-liquid with nicotine salt.
- B9.1.9.03 Zero-nicotine e-liquid: e-liquid without nicotine, shortfill bottles included.
- B9.1.9.04 Prefilled pod: sealed pod filled with e-liquid for a pod device.
- B9.1.9.05 Prefilled vape cartridge: filled cartridge for a vape pen, the substance (nicotine or cannabinoid) being the tag.

### B9.1.10 Concentrates
Kind axis: process type, solventless first. Display group: Cannabis and hemp.
- B9.1.10.01 Kief: loose resin glands sifted from cannabis.
- B9.1.10.02 Ice water hash: resin glands separated with ice water and collected as hash.
- B9.1.10.03 Rosin: resin pressed from cannabis with heat and pressure, without solvent.
- B9.1.10.04 Shatter: solvent-extracted concentrate set as a brittle glassy sheet.
- B9.1.10.05 Badder [wax]: solvent-extracted concentrate whipped to a soft, waxy texture.
- B9.1.10.06 Live resin: solvent extract made from fresh-frozen cannabis.
- B9.1.10.07 Distillate: refined cannabinoid oil distilled to high purity.

### B9.1.11 Infused & dosed products
Kind axis: form of the dose; hemp-derived CBD and kratom products included. Display group: Cannabis and hemp.
- B9.1.11.01 Edible: food item infused with a cannabinoid, kratom or other B9 substance (gummies, chocolates, baked goods, mints).
- B9.1.11.02 Drink: beverage infused with a cannabinoid, kratom or other B9 substance, shots included.
- B9.1.11.03 Tincture: liquid extract taken by drops, CBD oil included.
- B9.1.11.04 Capsule or tablet: dosed capsule or tablet of a cannabinoid, kratom or other B9 substance.
- B9.1.11.05 Topical: balm, lotion or cream containing a cannabinoid, applied to the skin.

## B9.2 Implements & hardware
Leaf axis: the job the empty object does in use.

### B9.2.1 Pipes
Kind axis: shape family; Billiard first, then by degree of bend, Freehand after the other shape families, non-Western forms last. Display group: Pipes and pipe tobacco.
- B9.2.1.01 Billiard: straight pipe with a cylindrical bowl and a straight shank, the baseline shape.
- B9.2.1.02 Bulldog: pipe with a angular, tapering bowl and a diamond-section shank.
- B9.2.1.03 Canadian: pipe with a long oval shank and a short stem.
- B9.2.1.04 Freehand: pipe shaped freely by the carver rather than to a classic shape family (R-33).
- B9.2.1.05 Kiseru [kiseru]: Japanese long pipe with a small metal bowl and mouthpiece (regional kind, C11; provisional until attested in a second region).
- B9.2.1.06 Hand pipe and chillum: small dry pipe or straight conical pipe made for cannabis (shape axis not yet stated). †

### B9.2.2 Water pipes
Kind axis: the object itself. Display group: hookah in Hookah and shisha; bong and dab rig in Cannabis and hemp.
- B9.2.2.01 Hookah: water pipe with a bowl, body, water base and one or more hoses, for shisha.
- B9.2.2.02 Bong: water pipe with a bowl and a tube, drawn through water, for dry material.
- B9.2.2.03 Dab rig: water pipe made to vaporise concentrates on a heated nail or banger.

### B9.2.3 Vape & heating hardware
Kind axis: device architecture, simplest first (provisional: a comparison source is still needed, C10(b)). Display group: Vapes and e-liquids; the heated-tobacco device in Heated tobacco; the vaporizer in Cannabis and hemp.
- B9.2.3.01 Disposable vape [big puff]: sealed vape sold prefilled and charged, used up and discarded.
- B9.2.3.02 Refillable pod kit: device with a battery body and refillable or replaceable pods.
- B9.2.3.03 Box mod kit: box-shaped battery device with a separate tank, adjustable output.
- B9.2.3.04 Heated-tobacco device: device that heats tobacco sticks or capsules without burning them.
- B9.2.3.05 Portable or desktop vaporizer: device that vaporises dry herb or concentrate by heat.

### B9.2.4 Lighters
Kind axis: ignition mechanism or use class. Display group: Lighters, cutters, ashtrays and cases; the pipe lighter is also shown in Pipes and pipe tobacco and the cigar lighter in Cigars and cigarillos.
- B9.2.4.01 Pocket lighter: lighter carried on the person.
- B9.2.4.02 Table lighter: lighter made to stand on a table.
- B9.2.4.03 Pipe lighter: lighter with a side flame for lighting a pipe bowl.
- B9.2.4.04 Cigar lighter: lighter made for lighting cigars (the torch or jet flame wording needs a fetched page). †

### B9.2.5 Rolling & grinding
Kind axis: the object itself. Display group: Cigarettes and roll-your-own; the grinder in Cannabis and hemp.
- B9.2.5.01 Rolling paper: thin paper for hand-rolling a cigarette or joint; empty blunt wraps included.
- B9.2.5.02 Grinder: device with teeth for grinding herb or tobacco.
- B9.2.5.03 Rolling machine: hand device for rolling cigarettes or joints.
- B9.2.5.04 Rolling tray: tray made for rolling and holding material.

### B9.2.6 Cutters, ashtrays & carry
Kind axis: the object itself. Display group: Lighters, cutters, ashtrays and cases; the cigar cutter, cigar case and travel humidor are also shown in Cigars and cigarillos.
- B9.2.6.01 Cigar cutter: tool for cutting the cap of a cigar.
- B9.2.6.02 Ashtray: receptacle for ash and stubs.
- B9.2.6.03 Cigarette case: case for carrying cigarettes on the person.
- B9.2.6.04 Cigar case: case for carrying cigars on the person.
- B9.2.6.05 Travel humidor: portable humidified box for carrying cigars.
- B9.2.6.06 Tobacco pouch: pouch for carrying loose or roll-your-own tobacco.

## B9.3 Parts and accessories made for one B9 object (no leaf)
Exempt from the level-1 axis (CV-17); axis: the object served, vapes first, then water pipes; stores leaf = null. Display group: vape parts in Vapes and e-liquids; hookah bowl and charcoal in Hookah and shisha.
- B9.3.01 Vape coil: replaceable heating coil for a vape tank or pod.
- B9.3.02 Vape tank: refillable tank or clearomizer for a vape device.
- B9.3.03 Vape pen battery: battery made for one vape pen or cartridge.
- B9.3.04 Refillable pod: empty pod for a pod device, filled by the user.
- B9.3.05 Hookah bowl: bowl that holds shisha on a hookah, the phunnel included.
- B9.3.06 Hookah charcoal [hookah coals]: charcoal made to heat shisha on a hookah.

## Precedence inside B9

- Role first: an object that contains the substance is a product (B9.1); an empty object made to hold, burn, heat, light, roll, cut or carry it is an implement (B9.2); a part or accessory made for one B9 object is B9.3.
- Substance never moves an object: a prefilled nicotine pod and a prefilled cannabis cartridge are two kinds in one leaf (B9.1.9.04, B9.1.9.05); a cannabis gummy and a kratom gummy are both B9.1.11.01; tobacco-free pouches sit with snus (B9.1.8.08); tobacco-free shisha sits with shisha tobacco (B9.1.6.02); cannabis flower sits with the other loose plant material (B9.1.5.03); cannabis pre-rolls sit with cigarettes as smoked rolls (B9.1.1.04).
- A disposable vape is filed by the device (B9.2.3.01), because it is sold and bought as a device (B-30).
- A prefilled pod or prefilled cartridge carries the substance and is a product (B9.1.9.04, B9.1.9.05); an empty, refillable pod is a part (B9.3.04) (B-30).
- A blunt is filed by what is inside as sold: a pre-rolled blunt is a pre-roll (B9.1.1.04); an empty blunt wrap is a rolling item (B9.2.5.01).
- Tobacco-free shisha sits with the form it imitates (B9.1.6.02); a herbal smoking blend is loose plant material (B9.1.5.05).
- Kratom tea is a use of kratom powder (B9.1.5.04); kratom capsules, shots and gummies are B9.1.11.04, B9.1.11.02 and B9.1.11.01.
- A device, hand pipe, grinder, lighter or rolling paper that serves several substances is one kind in the hardware leaf whose job defines it (C14); the substance view lists it under each use.
- Cigars stop at the generic vitola: marca-and-vitola forms (Montecristo No. 2 under B9.1.2.12) live in a register keyed to the vitola kind (CV-45); Habanos factory names (Mareva, Julieta No. 2, Pirámide) are aliases of the vitola kinds; figurado is a display group, never a kind.
- Pipes stop at the shape family: material, finish, grain and stem length are attributes, so a churchwarden is a long-stem pipe of its shape family, not a kind (B-29); makers' freehand designs and Blowfish, Nautilus, Volcano and Tomahawk are named forms under B9.2.1.04 (R-33).
- Pipe tobacco is filed by blend family; American blend is an alias of B9.1.4.03 (provisional merge, section 14); flake, ribbon and plug are the tobacco_cut attribute, not blend kinds.
- Shortfill is a bottle-size class of B9.1.9.03, not a kind.
- A case made to carry smoking products on the person is B9 (B9.2.6.03 to B9.2.6.06); a humidor, tobacco jar or cabinet that stands in a room is B1; stash jars and boxes are B1 (K-164, K-167).
- A pocket, table, pipe or cigar lighter is B9 (B9.2.4); matches, firelighters, lighter fuel, gas cylinders, flints and long utility or candle lighters are C8; hookah charcoal is B9 (B9.3.06) (K-166, K-30).
- A battery or charger made for one vape device is B9 (B9.3.03); a loose standard-size cell, 18650 included, is C8, and a USB cable is D1 (K-4).
- Rolling trays are B9 (B9.2.5.04); a scale goes with its task, a pocket scale B5 (K-167).
- A nicotine pouch, toothpick or pearl sold as a consumer product, any CBD product (even sold as a supplement) and any cannabinoid consumer product, balm and lotion included, is B9 (B9.1.8.08 to B9.1.8.10, B9.1.11.05); nicotine or cannabis products are H2 only under step 2's H1/H2 sentence; skin care without a cannabinoid is H1; an intimate oil, cannabinoid or not, is H3 (K-165).
- A cannabis-, kratom- or areca-bearing edible, drink or tincture is B9 whatever its food form; coffee, tea and kava are J6, hemp seeds and hemp oil sold as food J5, alcoholic drinks J7. Every plant or fungus product taken for a psychoactive effect is B9 whatever its legal status (B9.1.5.06 to B9.1.5.08, K-168); seeds, clones and living plants and fungi are C3, grow equipment C2 (K-75).
- A pipe, incense burner or tobacco made for use in a rite is F4; the same form made for smoking is B9. An ashtray, pipe stand or novelty lighter is B9 even when decorative; a kitchen butane torch goes by its task (B5 or C1).
