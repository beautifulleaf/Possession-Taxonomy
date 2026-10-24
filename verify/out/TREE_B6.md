# B6 Cleaning & Laundry: decided tree

Category: B6 Cleaning & Laundry (domain B, Home). Membership test (key step 30, B6 branch, tried after B5 and before B7, B8, B3, B1, B2 and B4; S3 with K-10 and K-11): made to clean, wash or dry the home, its surfaces or textiles, or to collect waste: vacuum cleaners, floor machines, mops, brooms, cloths, sponges and brushes, window and steam machines, cleaning and care products whatever they are used in (dishwasher salt, rinse aid, descalers and cleaning tablets, shoe and textile waterproofing and care sprays, sex-toy cleaners included), washing machines, dryers (a bathroom or ceiling unit made to dry laundry and a free-standing heated airer included), irons and steamers, airers, pegs and laundry baskets, laundry products, waste bins, bin bags and waste machines, together with parts and accessories made for one kind of B6 machine (S3). Not here: dishwashers and dish racks (B5); water-softener salt, filter cartridges, moisture absorbers, heated towel rails, dehumidifiers and fans (B7); mothballs and moth repellents (B8); room fragrance (B4); towels (B2); decorative storage baskets and boxes (B1); garment bags (A4); natural sponges, loofahs and pumice sold for the body (H1); cat litter (B10); pressure washers, pool-cleaning equipment, leaf blowers, garden blower-vacuums and compost bins (C2); workshop dust extractors, parts washers, wire, paint and decorating brushes, drain snakes and plungers (C1); fixed central-vacuum piping (C8); sewing machines and fabric dye (C4); cleaning, laundry and dry-cleaning services (out). Structure (Candidate A, decided B-7, CV-16, CV-17; memo sections 3, 10, 12 and 14): sub-family by what is cleaned or cared for, never the room (B6.1 to B6.5), then the closing parts sub-family B6.6, exempt from that axis (C5(d)); then leaf by product type (object served in B6.6), null in B6.4 (C5(b)), so its kind ids carry no leaf part; then kind by the axis each leaf states (body form and use, action on the floor, head form, drum arrangement and function, moisture removal, appliance type, physical form, soil or action, object cared for, part type). Each object gets one kind. Dust handling (bagged, bagless, cyclonic, water filter; `dust_handling`), `power` (corded, cordless) and run time, brush type (Bürstsauger), `mop_system`, `dock_level` (1 charging, 2 auto-empty, 3 mop wash and dry), `navigation`, HEPA class, capacity, spin speed, auto-dosing, energy and spin class (EU label), noise, condenser against heat pump, soleplate and cordless (irons), heated (airers), head material (mops), opening mechanism and compartments (bins), `detergent_enzyme` (bio or non-bio), `fragrance`, surface, eco claim, region, market, era and price band are attributes, tags, ledgers or views, never kinds (rule T, C10; R, C11). A washer and dryer sold as one offer is a unit-of-sale attribute over two kinds (K-1). Maker role (maker_roles.tsv, provisional): owner for the whole category (machines and products are chosen by type and task; the maker enters through model lines and named products, Dyson V-series, Roomba, Beat Wash, and through consumable brand lines, Ariel, Fairy, Cif, which are lines rows, never named forms); a brand tab for vacuums and robot vacuums only. Pending kinds: the memo marks 17 kinds † (no fetched page behind them; section 10 attestation list) and section 14 adds seven provisional kinds (robot mop; four washing-machine and dryer parts; two iron and steam-generator parts), also marked †; their ids are allocated here in memo order, each line ending in †, and a † kind enters the data only when a fetched page attests it. Leaves B6.6.2 and B6.6.3 hold only † kinds and are created only when one of their kinds is attested (section 14). Regional kinds twin-tub (B6.3.1.04), bathroom clothes-drying unit (B6.3.2.04) and bedding dryer (B6.3.2.05) are kinds with a provisional level (C11 two-region tie-break). Display groups (navigation proposal, display only, never moving a home; no group ids issued): Vacuums and floor machines (B6.1.1, B6.1.2); Mops, brooms and floor tools (B6.1.3, B6.1.4); Washing machines and dryers (B6.3.1, B6.3.2; B6.3.7 shown here by this tree's reading, the proposal names no group for it); Irons, steamers and drying (B6.3.3, B6.3.4); Laundry detergents and care products (B6.3.5, B6.3.6); Household cleaners (B6.2.4, B6.2.5; B6.1.5 shown here by this tree's reading); Cloths, sponges, brushes and window or steam cleaners (B6.2.1, B6.2.2, B6.2.3); Dishwashing products (B6.4); Bins and bin bags (B6.5.1, B6.5.2, B6.5.3); Bags, filters and spare parts (B6.6). Use cases (pet hair, carpet, stairs, cluttered homes) are filter shortcuts, not groups. Quality markers (display, judged on the named form, never on the kind): machines by cleaning result first (stain removal, suction, dust pick-up on carpet and hard floor), then rinsing and spin-drying, handling and ease of use, energy and water per cycle or per kg (EU A-G label), programme length, noise, durability and reliability; robot vacuums add navigation and obstacle avoidance, mopping, carpet and threshold climbing and dock level; consumables by cleaning performance in tests, then value, with no grade ladder. Quality signals (schemes and tier entries, C4): Which? Best Buy, Great Value, Eco Buy and Don't Buy, and the Which? brand reliability survey (a tier entry on the maker, scope = kind; section 14); Stiftung Warentest grades; RTINGS lab scores and robot tiers; Consumer Reports Overall Score, valid only within a type; EU energy label A-G (washers, washer-dryers, dryers) and EN/IEC 60312-1 dust pick-up and HEPA H12-H14 as standards on the object; price-defined bands are never tiers.

Ids (R-58): B6.n is a sub-family and B6.n.m a leaf; a kind is B6.n.m.kk, or B6.n.kk where a sub-family has no leaf.

## B6.1 Floors

Leaf axis: product type as a shopper's category names it (vacuum cleaners, floor machines, mops, brooms and sweepers, floor products).

### B6.1.1 Vacuum cleaners
Kind axis: body form and use, large then small, then special use (Consumer Reports order). Robot is one kind; stick and handheld are two (B-22).
- B6.1.1.01 Upright vacuum: vacuum cleaner whose motor, dust container and powered floor head form one standing body pushed across the floor.
- B6.1.1.02 Cylinder vacuum (canister): vacuum cleaner with a body on wheels or runners pulled behind on a hose and wand.
- B6.1.1.03 Stick vacuum: light vacuum cleaner with the motor and dust container on a long wand ending in a floor head.
- B6.1.1.04 Handheld vacuum: small vacuum cleaner held in one hand and used without a floor wand, including car and mattress vacuums.
- B6.1.1.05 Robot vacuum: self-driving vacuum cleaner that navigates the floor on its own and returns to a dock; mopping and dock functions are attributes.
- B6.1.1.06 Wet-and-dry vacuum (shop vacuum): vacuum cleaner made to pick up liquids as well as dry dirt and debris, wherever it is used.
- B6.1.1.07 Central vacuum: vacuum unit installed in a building and used through hose inlets connected by fixed piping.
- B6.1.1.08 Backpack vacuum: vacuum cleaner whose body is carried on the user's back on a harness.

### B6.1.2 Floor machines
Kind axis: action on the floor (wet scrubbing, extraction, polishing). Whether floor washer and floor scrubber name one kind or two, and the target of the German alias Waschsauger, are open until a definition is fetched.
- B6.1.2.01 Floor washer (wet-dry scrubber, 洗地机): cordless upright machine that wets the floor, scrubs it with a powered roller and sucks the dirty water back into a tank.
- B6.1.2.02 Carpet cleaning machine (carpet extractor): machine that sprays cleaning solution into carpet or upholstery and extracts it with the loosened dirt.
- B6.1.2.03 Floor scrubber: machine with powered pads or brushes that scrubs hard floors with water and solution.
- B6.1.2.04 Floor polisher: machine with rotating pads or brushes that polishes or buffs hard floors.

### B6.1.3 Mops
Kind axis: head form; head material (microfibre, cotton) is an attribute. Steam mop is a kind under rule T (C10(b)); the robot mop enters by memo section 14.
- B6.1.3.01 Dry mop (dust mop): mop with a wide dry head that collects dust from hard floors.
- B6.1.3.02 Flat mop (wet mop): mop with a flat rectangular pad on a swivel plate for wet cleaning.
- B6.1.3.03 Sponge mop: mop with a sponge head, usually wrung by a lever on the handle.
- B6.1.3.04 Steam mop: powered mop whose body carries a steam generator and cleans the floor with steam through a pad.
- B6.1.3.05 Spin mop: mop with a round head wrung by spinning it in a basket of its bucket. †
- B6.1.3.06 Cloth mop (Cuban mop): floor cloth worked over the floor with a squeegee or T-shaped stick.
- B6.1.3.07 Spray mop: flat mop with a refillable tank that sprays cleaning liquid ahead of the head.
- B6.1.3.08 Robot mop: self-driving floor cleaner that mops with a driven pad or roller, carries a water tank and has no suction; a robot vacuum that also mops is B6.1.1.05 (section 14, provisional). †

### B6.1.4 Brooms, sweepers and buckets
Kind axis: product class.
- B6.1.4.01 Broom: brush of bristles or fibres on a long handle for sweeping floors.
- B6.1.4.02 Carpet sweeper: unpowered push sweeper whose rotating brushes, driven by its wheels, lift dirt from carpet into a box.
- B6.1.4.03 Dustpan: flat scoop, often with a hand brush, into which sweepings are brushed.
- B6.1.4.04 Mop bucket: bucket made to hold water for a mop, often with a wringer.

### B6.1.5 Floor products
Kind axis: product class. Named apart from the machine B6.1.2.02 (duplicate-name rule, C-7).
- B6.1.5.01 Floor and carpet cleaning product: liquid, foam or powder made to clean floors and carpets.

## B6.2 Surfaces, windows and objects

Leaf axis: product type; chemical cleaners are a leaf whose kinds go by soil or action, never the room; the care-products leaf goes by the object cared for. Covers everything hard or leathery that is cleaned, other than floors, textiles and dishes, and every object the key and S3 send to B6 for care (B-7).

### B6.2.1 Cloths and dusters
Kind axis: product class. Microfibre cloth and chamois may merge at harvest into one kind "cleaning cloth" with a material attribute if no fetched source compares them separately (applied by default, section 12).
- B6.2.1.01 Microfibre cloth: cleaning cloth of fine split synthetic fibres that picks up dust and grease.
- B6.2.1.02 Chamois: soft absorbent leather or leather-like cloth used to dry and polish glass and paintwork.
- B6.2.1.03 Feather duster: bundle of feathers or fibres on a handle for dusting.
- B6.2.1.04 Dishcloth: cloth made for washing dishes and wiping kitchen surfaces.

### B6.2.2 Sponges, scourers and brushes
Kind axis: product class. A sponge or brush made for dishes is the same kind, shown under Dishes in a generated view (C14(b)).
- B6.2.2.01 Sponge or scourer: absorbent or abrasive pad used by hand to wipe and scrub surfaces and dishes.
- B6.2.2.02 Scrub brush: stiff-bristled hand brush made for household scrubbing.
- B6.2.2.03 Squeegee: rubber-bladed tool drawn across glass or tiles to remove water.

### B6.2.3 Window and steam machines
Kind axis: product class. The steam cleaner serves floors and surfaces; one home here, listed under Floors in a generated view (C14(b)).
- B6.2.3.01 Window vacuum (Fenstersauger): handheld battery device with a squeegee blade that sucks water off windows and tiles.
- B6.2.3.02 Window-cleaning robot: self-driving device that holds itself to a window and cleans the glass.
- B6.2.3.03 Steam cleaner: appliance that cleans floors and hard surfaces with steam through a hose or nozzle.

### B6.2.4 Chemical cleaners
Kind axis: soil or action, never the room (the room-named retail lines are aliases); scent, surface and eco claim are attributes.
- B6.2.4.01 Multi-purpose cleaner: cleaning product made for most hard surfaces in the home.
- B6.2.4.02 Bleach and disinfectant: product made to kill germs, bleach or sanitise surfaces.
- B6.2.4.03 Glass cleaner: product made to clean glass and mirrors without streaks.
- B6.2.4.04 Toilet cleaner: product made to clean and descale the toilet bowl. †
- B6.2.4.05 Limescale remover: product made to dissolve limescale on taps, tiles and sanitaryware. †
- B6.2.4.06 Degreaser and oven cleaner: product made to dissolve grease and baked-on soil on hobs, ovens and kitchen surfaces. †
- B6.2.4.07 Mould remover: product made to remove mould and mildew from surfaces.

### B6.2.5 Care products for other objects
Kind axis: object cared for; surface and eco claim are attributes.
- B6.2.5.01 Furniture and upholstery cleaner: product made to clean or care for furniture surfaces and upholstery.
- B6.2.5.02 Shoe cleaner: product made to clean shoes.
- B6.2.5.03 Shoe polish and waterproofing: polish, conditioner or spray made to care for, colour or waterproof shoes (B-23, K-11(c)).
- B6.2.5.04 Car-wash shampoo: product made to wash a vehicle's paintwork. †
- B6.2.5.05 Descaler for kettles and machines: product or tablet made to remove limescale from kettles, coffee machines and other appliances (K-11(a)). †
- B6.2.5.06 Pet-stain cleaner: product made to clean stains and odours left by pets. †
- B6.2.5.07 Sex-toy cleaner: product made to clean sex toys (K-11(d)). †

## B6.3 Textiles (laundry)

Leaf axis: product type (washing machines, dryers, irons and boards, airers and baskets, detergents, other textile-care products, hand-wash tools).

### B6.3.1 Washing machines
Kind axis: drum arrangement and function; capacity, spin speed and auto-dosing are attributes. Agitator and impeller are two kinds; the washer-dryer is a kind of washing machine (B-22).
- B6.3.1.01 Front-load washer: washing machine with a horizontal drum loaded through a front door.
- B6.3.1.02 Top-load washer with agitator: top-loading washing machine with a central post that moves the wash.
- B6.3.1.03 Top-load washer with impeller (pulsator): top-loading washing machine with a low disc or cone at the bottom of the drum that moves the wash.
- B6.3.1.04 Twin-tub (2槽式): washing machine with separate tubs for washing and spin-drying (region tag JP; level provisional, C11).
- B6.3.1.05 Washer-dryer: washing machine that also dries the load in the same drum.
- B6.3.1.06 Mini washer: small portable washing machine for small loads.
- B6.3.1.07 Pedestal washer: small washing machine built into a pedestal set under a main washer.
- B6.3.1.08 Laundry center: washer and dryer stacked and built as one unit (one appliance, not a set, K-1).

### B6.3.2 Dryers
Kind axis: how moisture is removed, from vented to ventless (secondary key installation); condenser against heat pump, capacity and sensor are attributes.
- B6.3.2.01 Vented tumble dryer: tumble dryer that blows moist air out through a duct.
- B6.3.2.02 Ventless tumble dryer: tumble dryer that removes moisture from the air without a duct, by condenser or heat pump.
- B6.3.2.03 Spin dryer: machine that removes water from laundry by spinning it at high speed, without heat.
- B6.3.2.04 Bathroom clothes-drying unit: unit installed in a bathroom ceiling or wall made to dry laundry, even when it also ventilates (region tag JP; K-185; level provisional, C11).
- B6.3.2.05 Bedding dryer (futon dryer): appliance that blows warm air into a bag or mat to dry and warm bedding (region tag JP; level provisional, C11).

### B6.3.3 Irons, steamers and ironing boards
Kind axis: appliance type, then board; soleplate, wattage and cordless are attributes.
- B6.3.3.01 Steam iron: hand iron with a built-in water tank that steams through its soleplate.
- B6.3.3.02 Steam generator iron (steam station): iron connected by a hose to a separate base that boils water and supplies steam under pressure.
- B6.3.3.03 Garment steamer: appliance that removes creases from hanging clothes with a jet of steam.
- B6.3.3.04 Ironing board: folding padded board on which clothes are ironed.

### B6.3.4 Airers, pegs and baskets
Kind axis: function in the washing cycle; heated or not is an attribute of the airer.
- B6.3.4.01 Clothes airer: rack or line on which washing is hung to dry, heated or not.
- B6.3.4.02 Clothes peg: clip that holds washing on a line or airer.
- B6.3.4.03 Laundry basket: basket, hamper or bag made to hold or carry washing (K-10).

### B6.3.5 Laundry detergents
Kind axis: physical form; bio or non-bio, colour or white and sensitive are attributes.
- B6.3.5.01 Detergent powder: laundry detergent in powder form.
- B6.3.5.02 Detergent liquid: laundry detergent in liquid or gel form.
- B6.3.5.03 Detergent capsule (pod): pre-dosed laundry detergent in a dissolving film pouch.

### B6.3.6 Other laundry and textile-care products
Kind axis: product class.
- B6.3.6.01 Fabric conditioner: product added to the rinse to soften and scent fabrics.
- B6.3.6.02 Stain remover: product made to remove stains from textiles before or during washing.
- B6.3.6.03 Fabric freshener: spray made to remove odours from fabrics (boundary 16). †
- B6.3.6.04 Scent booster: beads or liquid added to the wash to add scent to laundry.
- B6.3.6.05 Washing-machine cleaner: product made to clean the inside of a washing machine.
- B6.3.6.06 Lint remover: roller, brush or powered shaver that removes lint, fluff and pilling from fabric.
- B6.3.6.07 Textile waterproofing and care spray: spray made to waterproof or protect textiles (K-11(c)). †

### B6.3.7 Hand-wash and manual textile tools
Kind axis: product class (B-23); era (antique) is a modifier.
- B6.3.7.01 Washboard: ridged board on which clothes are scrubbed by hand. †
- B6.3.7.02 Wash copper: large vessel in which laundry is boiled. †
- B6.3.7.03 Carpet beater: hand tool used to beat dust out of carpets and rugs.

## B6.4 Dishes

No leaf (about 12 kinds or fewer, leaf = null); kind ids carry no leaf part. Kind axis: use (hand washing, then machine washing). Holds only consumables: the dishwasher is B5; a dish sponge, brush or cloth is B6.2.
- B6.4.01 Washing-up liquid: liquid detergent for washing dishes by hand.
- B6.4.02 Dishwasher tablet: pre-dosed detergent tablet for a dishwasher.
- B6.4.03 Dishwasher rinse aid: liquid added to a dishwasher to help water run off and dishes dry.
- B6.4.04 Dishwasher salt: salt that regenerates a dishwasher's built-in water softener (K-11(a)).

## B6.5 Waste

Leaf axis: product type (bins, bags and liners, waste machines).

### B6.5.1 Bins
Kind axis: form and place of use; opening mechanism (pedal, swing, touch, sensor), compartments and capacity are attributes.
- B6.5.1.01 Kitchen bin: lidded bin made for household waste in the kitchen.
- B6.5.1.02 Wheelie bin (outdoor bin): large wheeled bin kept outdoors for collection. †
- B6.5.1.03 Waste-paper basket: small open bin for paper and dry waste. †
- B6.5.1.04 Food-waste caddy: small lidded bin made to collect food waste for composting or collection. †

### B6.5.2 Bags and liners
Kind axis: product class.
- B6.5.2.01 Bin liner (bin bag): plastic or paper bag made to line a bin and hold waste.

### B6.5.3 Waste machines
Kind axis: product class; installed machines keep their own category.
- B6.5.3.01 Garbage disposer: electric unit fitted under a sink that grinds food waste into the drain. †
- B6.5.3.02 Trash compactor: appliance that compresses household waste into a smaller volume. †

## B6.6 Parts and accessories made for one object

Leaf axis: object served (C5(d), CV-17); the only sub-family exempt from the level-1 axis. Kind axis in every leaf: part type; the fitting model or platform sits in the compatibility ledger (C13) and the part carries a `fits` relation (B-23). Leaves B6.6.2 and B6.6.3 are section-14 additions from memory, provisional, and created only when one of their kinds is attested.

### B6.6.1 Vacuum cleaner parts
- B6.6.1.01 Vacuum bag: disposable or reusable dust bag made for a vacuum cleaner.
- B6.6.1.02 Vacuum filter: filter made for a vacuum cleaner (HEPA class is an attribute).
- B6.6.1.03 Vacuum belt: drive belt made for a vacuum cleaner's brush roll.
- B6.6.1.04 Vacuum battery: battery pack made for a cordless or robot vacuum cleaner.
- B6.6.1.05 Nozzle and attachment: floor head, brush, nozzle or tool made to fit a vacuum cleaner.

### B6.6.2 Washing-machine and dryer parts
- B6.6.2.01 Lint filter: filter made to catch lint in a washing machine or dryer. †
- B6.6.2.02 Inlet or drain hose: hose made to feed water to or drain it from a washing machine. †
- B6.6.2.03 Door seal: rubber seal made for a washing-machine door. †
- B6.6.2.04 Dryer belt: drive belt made for a tumble dryer's drum. †

### B6.6.3 Iron and steam-generator parts
- B6.6.3.01 Anti-scale cartridge: cartridge made to fit an iron or steam generator and remove scale from its water. †
- B6.6.3.02 Water tank: water tank made for an iron or steam generator. †

## Precedence inside B6

- A vacuum cleaner has one home in B6.1.1 whatever it cleans: a handheld car or mattress vacuum is B6.1.1.04; a wet-and-dry shop vacuum is B6.1.1.06 wherever it is used (K-18); a central vacuum unit is B6.1.1.07 and its fixed piping C8; a workshop dust extractor is C1, a garden blower-vacuum C2.
- A robot vacuum that also mops is B6.1.1.05, with `mop_system` and `dock_level` as attributes; a self-driving mop with no suction is B6.1.3.08 (section 14). A window-cleaning robot is B6.2.3.02; a pool robot and a robot lawn mower are C2.
- Bagged, bagless, cyclonic and water-filter vacuums, corded and cordless vacuums and brush-roll (Bürstsauger) vacuums are values of attributes on their body-form kind, never kinds (rule T).
- The steam cleaner serves floors and surfaces and has one home, B6.2.3.03; the steam mop, whose body carries a steam generator, is B6.1.3.04 (rule T). The multi-purpose cleaner is B6.2.4.01; a product made only for floors and carpets is B6.1.5.01, and the machine that extracts carpets B6.1.2.02.
- Floor scrubber (B6.1.2.03) and floor washer (B6.1.2.01) stay two kinds until a fetched definition shows whether they are one; the German Waschsauger is an alias of B6.1.2.01 or B6.1.2.02, its target unresolved.
- A washer-dryer is a washing machine (B6.3.1.05); a laundry center stacked and built as one unit is B6.3.1.08; a washer and a dryer sold together as two machines in one offer are filed as their two kinds with a unit-of-sale attribute (K-1). A heat-pump or condenser dryer is B6.3.2.02; a dryer that needs a duct is B6.3.2.01.
- A free-standing heated airer is B6.3.4.01 (heated = yes), and a bathroom or ceiling unit made to dry laundry is B6.3.2.04 even when it also ventilates (K-185); a heated rail made to warm and dry towels, plumbed or wired, a dehumidifier and a fan are B7.
- A laundry basket, hamper or laundry bag that holds dirty washing is B6.3.4.03 (K-10), as the clothes peg is B6.3.4.02; a decorative storage basket or box is B1 and a garment bag A4.
- A sponge, scourer or brush made for washing dishes is B6.2.2.01 or B6.2.2.02, and a dishcloth B6.2.1.04 (C14(b), B-33); a dish rack or drainer and the dishwasher are B5. Washing-up liquid, dishwasher tablets, rinse aid and dishwasher salt are B6.4.01 to B6.4.04; water-softener salt and filter cartridges for B7 objects are B7 (K-11(a)).
- A descaler or cleaning tablet made for a kettle or coffee machine is B6.2.5.05 and the machine B5; a product made to clean the inside of a washing machine is B6.3.6.05.
- A brush, scraper or scrubber made for household cleaning is B6.2.2.02; a brush made to prepare or finish work (wire brush, paint scraper, decorating brush), a drain snake and a plumber's plunger are C1, as are parts washers (B6-O1).
- A cleaning sponge or scourer is B6.2.2.01; a natural sponge, loofah or pumice sold for the body is H1. A towel of any kind is B2.
- Shoe cleaners are B6.2.5.02 and shoe polish, conditioner and waterproofing B6.2.5.03 (B-23, K-11(c)); textile waterproofing and care sprays are B6.3.6.07; a sex-toy cleaner is B6.2.5.07 (K-11(d)); car-wash shampoo is B6.2.5.04 and a car vacuum B6.1.1.04.
- A cleaner made for pet stains is B6.2.5.06; cat litter is B10.
- A product made to remove odour from, or clean, a fabric or surface is B6 (fabric freshener B6.3.6.03, scent booster B6.3.6.04); a product made to scent a room (spray, plug-in, diffuser) is B4 (B4-O3). A moisture absorber is B7; mothballs and insect-proofing products are B8.
- Fabric dye for home use is C4 (B6-O1), and sewing machines are C4, however a retailer shelves them.
- A countertop food-waste caddy is B6.5.1.04; a garden compost bin is C2. A garbage disposer (B6.5.3.01) and a trash compactor (B6.5.3.02) are B6, made to collect waste (B6-O1).
- A pressure washer, pool-cleaning equipment and a leaf blower are C2 (K-176).
- A part made for one kind of B6 machine follows it into B6.6: vacuum bags, filters, belts, batteries and nozzles are B6.6.1, with the fitting platform in the compatibility ledger (C13); washer and dryer parts go to B6.6.2 and iron and steam-generator parts to B6.6.3 once attested (section 14). A consumable cleaning product used in a machine (washing-machine cleaner, descaler, dishwasher salt) is a product kind, not a part.
- Microfibre cloth (B6.2.1.01) and chamois (B6.2.1.02) stay two kinds as S11 words them; a fetched source that does not compare them separately would merge them into one cleaning-cloth kind with a material attribute at harvest. Head material of a mop is an attribute.
