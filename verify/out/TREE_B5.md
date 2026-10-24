# B5 Kitchen & Dining: decided tree

Category: B5 Kitchen & Dining (domain B, Home). Membership test (CATEGORIES_v0_7, step 30, first branch): made to prepare, cook, cool, store or serve food and drink, powered or not, domestic or commercial: cookware, kitchen tools and machines, kitchen scales and thermometers, cooking appliances, grills, refrigerators and wine fridges, dishwashers, vending machines for food and drink, tableware, glassware, barware, decanters, tea and coffee equipment, food storage and lunch bags, oven gloves and aprons, kitchen timers. Every plate and tray made to hold food is B5, whatever it is kept for, and display is a tag (S5, K-182). Structure (B-6, Candidate A): sub-family (the stage of kitchen work the object serves: cook, prepare, cool and store, serve and drink at table, make drinks, clean-up and remainder; closed by the parts sub-family B5.7, exempt from that axis, CV-17), then leaf (the product family as sold, stated per sub-family; B5.3, B5.6 and B5.7 have no leaf, C5(b)), then kind (vessel form, pattern, operating mode, appliance type or piece type, at the level where buyers compare quality or makers), with named forms below the kind (models, lines, shapes, patterns, and non-maker forms such as gyuto, bunka and kiritsuke under chef's knife and Yixing under teapot; tetsubin under kettle, provisional). Each object gets one kind. Cookware material, ply count, coating, hob compatibility, oven safety, power source and fuel, technology and connectivity, installation (built-in or freestanding, rule M), market (`market = commercial`), steel and hardness, handle style, length and other sizes, stemmed or stemless, lead crystal, burr size, certification (SCA), region, era, setting, user, maker and price band are attributes, tags or views, never kinds (rules T, R, M; B-21). Section 14 adds the stored attributes `hob_compatibility`, `cookware_material`, `oven_safe_c`, `set_contents`, `steel_hardness_hrc`, `handle_style` and `heating_technology` (rice-cooker technology tiers conventional, micom, IH and pressure IH are this attribute on named forms, shown as the rice-cooker ladder, never kinds). Quality markers (proposals.tsv B5, display only): cookware by heat evenness, food release, construction, hob compatibility and oven safety; knives by construction, steel and hardness, edge geometry, handle and maker line; rice cookers by technology tier, inner pot and capacity; espresso machines and grinders by the capability ladder and burr size; stemware by shape for the drink and maker tier; vintage cast iron by maker, mark and era. Sets (S3a, K-1): a set of one kind is that kind; a mixed set is filed by its item of greatest value with `set_contents` listed; the cookware set is the one set kind (section 14). Makers (maker_roles.tsv B5, owner, provisional): cookware and knife models carry the maker; shoppers choose a type and model, makers enter through lines and named forms, and knife, cast-iron, espresso and stemware buyers are served by a makers side view, not a way-in. Display only (section 14, with proposals.tsv B5): the stage-of-work sub-families stay the placement index and the display groups follow shop families (Cookware; Bakeware; Kitchen appliances; Large kitchen appliances; Knives and boards; Kitchen tools and measuring; Food storage; Dinnerware and serveware; Glassware and drinkware; Coffee and tea; Bar and home brewing; Clean-up and kitchen wear; parts show as Replacement parts, the proposals.tsv name, since section 14 names no group for B5.7). Each leaf names its group; a group never moves a home or an id. A kind marked † is named only by the key, a search excerpt, the domain review or a decision, and needs a fetched page in the stage-3 harvest before it enters the data; a † kind that cannot be attested leaves the tree.

Ids (R-58): B5.n is a sub-family and B5.n.m a leaf; a kind is B5.n.m.kk, or B5.n.kk where a sub-family has no leaf.

## B5.1 Cook
Leaf axis: product family as sold (vessels for heat; heating appliances); a final mixed kind at leaf 0.

### B5.1.1 Pans
Kind axis: vessel form. Display group: Cookware.
- B5.1.1.01 Frying pan or skillet: shallow, flat-bottomed pan with sloped sides and a long handle, for frying and searing; material is an attribute.
- B5.1.1.02 Wok: deep, round-bottomed or flat-bottomed pan with high flaring sides, for stir-frying.
- B5.1.1.03 Grill pan or griddle: pan with a ridged or flat cooking plate, for grilling or searing on a hob.
- B5.1.1.04 Saute pan: a wide pan with straight or high sides and usually a lid, for frying, braising and reducing (section 14).

### B5.1.2 Pots
Kind axis: vessel form. Display group: Cookware.
- B5.1.2.01 Saucepan: deep round pot with one long handle, for boiling and making sauces.
- B5.1.2.02 Stockpot: tall, large pot with two handles, for stock, soup and boiling in quantity. †
- B5.1.2.03 Dutch oven or casserole: heavy lidded pot, often cast iron, for braising and slow cooking on the hob or in the oven.
- B5.1.2.04 Pressure cooker: sealed pot that cooks under steam pressure; stovetop or electric is a power-source tag.

### B5.1.3 Ovenware and bakeware
Kind axis: use. Display group: Bakeware.
- B5.1.3.01 Roasting pan: deep, open oven pan for roasting meat and vegetables. †
- B5.1.3.02 Baking tray: flat oven sheet with low or no rim, for baking.
- B5.1.3.03 Gastronorm pan: container made to the gastronorm size standard for commercial kitchens and serving counters (`market = commercial`, B-20).

### B5.1.4 Heating appliances and heat sources
Kind axis: appliance type; gas, electric, induction and other power sources are tags (rule T); built-in or freestanding is an installation attribute (rule M). Display group: Kitchen appliances; B5.1.4.03 and B5.1.4.04 display in Large kitchen appliances.
- B5.1.4.01 Air fryer: countertop appliance that cooks food in a basket by circulating hot air.
- B5.1.4.02 Toaster: appliance that browns slices of bread with radiant elements.
- B5.1.4.03 Oven: enclosed cooking appliance that bakes and roasts by heating the air in a chamber. †
- B5.1.4.04 Hob or cooktop: cooking surface of burners or heating zones on which pans are set. †
- B5.1.4.05 Barbecue grill: grill that cooks food over a fire, charcoal, gas or electric heat; fuel is a tag. †
- B5.1.4.06 Rice cooker: appliance that cooks rice in an inner pot under automatic control; `heating_technology` (conventional, micom, IH, pressure IH) is an attribute (section 14). †
- B5.1.4.07 Bain-marie: heated water bath that keeps food warm or cooks it gently (`market = commercial`, B-20).

### B5.1.0 Mixed (leaf = null, section 14)
Display group: Cookware.
- B5.1.0.01 Cookware set: a set of pots and pans of one maker line, sold and rated as one object; the pieces are listed in `set_contents` (S3a, K-1, section 14).

## B5.2 Prepare
Leaf axis: product family as sold (knives, boards and sharpeners, hand tools, measuring, food machines).

### B5.2.1 Kitchen knives
Kind axis: pattern; steel, hardness, handle and length are attributes; gyuto, bunka and kiritsuke are non-maker named forms of chef's knife (B-20). Display group: Knives and boards.
- B5.2.1.01 Chef's knife: general-purpose kitchen knife with a broad, curved blade for chopping, slicing and mincing.
- B5.2.1.02 Santoku: Japanese general-purpose knife with a flat edge and a sheep's-foot tip.
- B5.2.1.03 Nakiri: Japanese vegetable knife with a straight, rectangular blade.
- B5.2.1.04 Paring knife: small knife with a short blade for peeling and fine work in the hand.
- B5.2.1.05 Kitchen utility knife [petty]: mid-size kitchen knife between the paring and the chef's knife (not the trade utility knife of C1).
- B5.2.1.06 Bread knife: long knife with a serrated edge for cutting bread.
- B5.2.1.07 Boning knife: narrow, flexible or stiff knife for taking meat and fish off the bone.
- B5.2.1.08 Slicer [sujihiki]: long, narrow knife for slicing cooked meat and raw fish.
- B5.2.1.09 Cleaver: heavy, broad, rectangular blade for chopping through bone or, in the Chinese form, for all-purpose cutting.
- B5.2.1.10 Deba: thick, single-bevel Japanese knife for butchering fish (rule R).
- B5.2.1.11 Yanagiba: long, single-bevel Japanese knife for slicing raw fish (rule R).
- B5.2.1.12 Usuba: thin, single-bevel Japanese vegetable knife with a straight edge (rule R).

### B5.2.2 Cutting boards and sharpeners
Kind axis: the tool itself. Display group: Knives and boards.
- B5.2.2.01 Cutting board: board of wood, plastic or composite to cut food on.
- B5.2.2.02 Knife sharpener: stone, rod or device that sharpens or hones a kitchen knife's edge.

### B5.2.3 Hand tools
Kind axis: the tool itself. Display group: Kitchen tools and measuring.
- B5.2.3.01 Grater: hand tool with a surface of sharp-edged holes for shredding food.
- B5.2.3.02 Colander or strainer: perforated or mesh bowl for draining or sieving food.
- B5.2.3.03 Spatula: hand tool with a flat, broad blade for turning, lifting or scraping food.
- B5.2.3.04 Spice or pepper mill: hand mill that grinds pepper or spices; a grinder made for coffee is B5.5.1.06. †

Kinds to look for (no id, R-96 c): kitchen shears †, named only as an example in boundary 1 (K-171: a cutting tool made to cut food is B5); the memo places it in no leaf, and this leaf is its likely home.

### B5.2.4 Measuring
Kind axis: quantity measured. Display group: Kitchen tools and measuring.
- B5.2.4.01 Kitchen scale: scale for weighing ingredients; app connection is an attribute.
- B5.2.4.02 Kitchen thermometer: thermometer for the temperature of food, oil or an oven.
- B5.2.4.03 Kitchen timer: timer that signals when a set cooking time has passed.
- B5.2.4.04 Pocket scale: small portable scale for weighing small amounts (K-167). †

### B5.2.5 Food machines
Kind axis: operation (appliance type). Display group: Kitchen appliances.
- B5.2.5.01 Stand mixer: countertop mixer with a bowl and a head that drives beaters, whisk or dough hook.
- B5.2.5.02 Food processor: appliance with a bowl and interchangeable blades and discs for chopping, slicing and mixing.

## B5.3 Cool and store (no leaf)
Kind axis: function (cool, or keep food and drink). Display group: Food storage; B5.3.01 and B5.3.02 display in Large kitchen appliances.
- B5.3.01 Refrigerator: insulated, powered cabinet that keeps food and drink cold; built-in or freestanding is an installation attribute. †
- B5.3.02 Wine fridge: refrigerated cabinet made to keep wine at storage or serving temperature. †
- B5.3.03 Food storage container: lidded container for keeping food.
- B5.3.04 Lunch bag: insulated bag for carrying a meal and keeping it cool; "cool bag" is its synonym row (K-131). †
- B5.3.05 Drink bottle: reusable bottle for carrying a drink, whether or not made for a sport (K-161).
- B5.3.06 Hydration bladder: flexible drink reservoir with a drinking tube, sold on its own (K-161). †

## B5.4 Serve, eat and drink at table
Leaf axis: piece family in the place setting (dinnerware, flatware, glassware, cups, serveware and table accessories); kinds are piece types in place-setting order.

### B5.4.1 Dinnerware
Kind axis: piece type. Display group: Dinnerware and serveware.
- B5.4.1.01 Dinner plate: large flat plate on which a main meal is served and eaten; a commemorative or display plate is this plate with a display tag (S5, K-182).

Kinds to look for (no id, R-96 c): the other plate piece types and bowls of the Replacements piece guide [S35] †; the memo names none of them.

### B5.4.2 Flatware
Kind axis: piece type. Display group: Dinnerware and serveware.
- B5.4.2.01 Table fork: fork laid at the place setting for eating (replaces the memo placeholder "Table flatware"). †
- B5.4.2.02 Spoon: spoon laid at the place setting for eating (replaces the memo placeholder "Table flatware"). †
- B5.4.2.03 Table knife: knife laid at the place setting for eating (replaces the memo placeholder "Table flatware"). †
- B5.4.2.04 Steak knife: sharp, often serrated table knife for cutting meat at the plate (B-20).
- B5.4.2.05 Butter knife: blunt table knife for spreading butter (B-20). †

### B5.4.3 Glassware
Kind axis: piece type; stemmed or stemless and lead crystal are attributes. Display group: Glassware and drinkware.
- B5.4.3.01 Wine glass: glass with a bowl shaped for drinking wine, stemmed or stemless.
- B5.4.3.02 Tumbler: flat-bottomed glass without a stem.
- B5.4.3.03 Decanter: glass vessel into which wine or spirits are poured to serve. †

### B5.4.4 Cups
Kind axis: piece type. Display group: Glassware and drinkware.
- B5.4.4.01 Mug: large cup with a handle, used without a saucer.
- B5.4.4.02 Cup [tea or coffee cup]: handled cup for tea or coffee, usually used with a saucer; a cup and saucer sold together is filed here (S3a).
- B5.4.4.03 Saucer: small shallow dish on which a cup stands. †

### B5.4.5 Serveware and table accessories
Kind axis: piece type. Display group: Dinnerware and serveware.
- B5.4.5.01 Serving tray: tray made to carry and serve food and drink (K-182, K-191). †
- B5.4.5.02 Hard placemat: rigid mat set under a place setting; a textile placemat is B2 (B5-O1).
- B5.4.5.03 Coaster: small hard mat set under a glass or cup (B5-O1).

## B5.5 Make drinks
Leaf axis: drink made (coffee, tea, water, bar, home brewing and winemaking); B5.5 holds only the objects that make the drink, never a drinking vessel.

### B5.5.1 Coffee equipment
Kind axis: brew method, then operating mode (the three espresso modes are kinds under rule T(b)). Display group: Coffee and tea.
- B5.5.1.01 Semi-automatic espresso machine: espresso machine with a pump in which the user grinds, doses, tamps and starts and stops the shot.
- B5.5.1.02 Super-automatic espresso machine: espresso machine with a built-in grinder that grinds, doses, tamps and brews at one touch.
- B5.5.1.03 Manual lever espresso machine: espresso machine in which a hand lever drives the water through the coffee.
- B5.5.1.04 Drip coffee maker: machine that drips hot water over ground coffee in a filter into a carafe.
- B5.5.1.05 Moka pot: stovetop pot that pushes boiling water by steam pressure up through ground coffee. †
- B5.5.1.06 Coffee grinder: burr or blade grinder made for coffee beans; hand or electric is a tag, burr size an attribute.

### B5.5.2 Tea equipment
Kind axis: vessel form. Display group: Coffee and tea.
- B5.5.2.01 Teapot: lidded vessel with a spout and handle for brewing and pouring tea; Yixing is a non-maker named form.
- B5.5.2.02 Kyusu: Japanese teapot with a side handle (rule R).
- B5.5.2.03 Gaiwan: lidded bowl on a saucer for brewing tea (rule R).

### B5.5.3 Water
Kind axis: appliance type. Display group: Coffee and tea.
- B5.5.3.01 Kettle: vessel that boils water; stovetop or electric is a tag; tetsubin is a provisional non-maker named form.
- B5.5.3.02 Water filter jug: jug with a filter cartridge that treats water for drinking (B-33; the cartridge is B7, K-11). †

### B5.5.4 Bar tools
Kind axis: bar tool. Display group: Bar and home brewing.
- B5.5.4.01 Cocktail shaker: closed vessel in which a cocktail is shaken with ice. †
- B5.5.4.02 Jigger: double-ended measure for spirits. †

### B5.5.5 Home brewing and winemaking
Kind axis: drink made (beer, wine, cider). Display group: Bar and home brewing. No kind is decided in the memo (K-58 sends the equipment to B5); the kinds come from the stage-3 harvest, and the leaf dissolves into its host if the harvest finds none.

## B5.6 Clean-up, kitchen wear and remainder (no leaf)
Kind axis: function (kinds the key sends to B5 that fit no stage above). Display group: Clean-up and kitchen wear; B5.6.01 displays in Large kitchen appliances.
- B5.6.01 Dishwasher: appliance that washes and dries dishes, cookware and cutlery. †
- B5.6.02 Dish rack: rack on which washed dishes stand to drain and dry (B-33). †
- B5.6.03 Oven glove: insulated glove or mitt for handling hot cookware. †
- B5.6.04 Apron: garment worn over clothes to protect them while cooking. †
- B5.6.05 Vending machine for food and drink: machine that dispenses food or drink on payment. †

## B5.7 Parts and accessories made for one kitchen object (no leaf)
Kind axis: the part itself; leaf axis when needed: object served (`leaf = null` while it holds about 12 kinds or fewer, CV-17, C5(d)). Display group: Replacement parts. No kind is decided in the memo; the sub-family dissolves into its host if the harvest finds none. Kinds to look for (no id, R-96 c), the memo's examples of what S3 sends here, each †: a coffee machine's portafilter, water tank or drip tray; the jar of one blender; the lid or base of one kettle; a lid made for one pot; a rack made for one appliance (section 14).

## Precedence inside B5

- Stage of work first: an object is filed by the stage of kitchen work it serves (cook B5.1, prepare B5.2, cool and store B5.3, serve and drink at table B5.4, make drinks B5.5, clean-up and remainder B5.6); a part made for one kitchen object is B5.7. The display groups (section 14) are display only and move no id.
- A grinder made for coffee is the coffee grinder (B5.5.1.06), hand or electric; a spice or pepper mill is the hand tool B5.2.3.04. Every vessel one drinks from at the table (glass, mug, cup) is B5.4, whatever the drink; B5.5 holds only the objects that make the drink, and a teacup is the cup (B5.4.4.02).
- A kettle, stovetop or electric, is one kind (B5.5.3.01), power source a tag; a tetsubin is a regional named form under it, provisionally.
- Steak and butter knives are flatware (B5.4.2.04, B5.4.2.05), not kitchen knives (B-20). Gyuto, bunka and kiritsuke are non-maker named forms of the chef's knife (B5.2.1.01); a Japanese knife maker is a ledger row, not a kind.
- The three espresso operating modes (B5.5.1.01 to B5.5.1.03) are kinds under rule T(b); if the harvest finds sellers that do not separate them, they become named forms of one espresso machine kind. No capsule or pod machine kind is created; capsule systems are compatibility-ledger rows linked to J6 (J-14).
- A saute pan has straight or high sides and usually a lid (B5.1.1.04); a sloped-sided pan is the frying pan (B5.1.1.01).
- Sets (S3a, K-1): a set of one kind is that kind (a set of wine glasses is B5.4.3.01; a steak-knife set is B5.4.2.04). A cookware set of one maker line sold and rated as one object is B5.1.0.01, with `set_contents` listed. A dinner set, a knife-block set and a cup and saucer sold together are mixed sets filed by their item of greatest value with contents listed (a cup and saucer is B5.4.4.02), until a fetched tester compares them as one object.
- Rice-cooker technology tiers (conventional, micom, IH, pressure IH) are the attribute `heating_technology` on named forms of B5.1.4.06, never kinds (rule T).
- Commercial-only forms are ordinary kinds with `market = commercial`: the gastronorm pan B5.1.3.03 and the bain-marie B5.1.4.07 (B-20).
- Every plate and tray made to hold food is B5, whatever it is kept for, and display is a tag (S5, K-182): a commemorative plate or a painted plate made to be hung, such as Kosiv ware, is the plate piece type it matches (B5.4.1.01 where it is a dinner plate). A tray made to serve is B5.4.5.01; a tray made to hold small items on a surface is B1 (K-191).
- A hard placemat (B5.4.5.02) and a coaster (B5.4.5.03) are B5; textile placemats, table runners, napkins, tablecloths, tea towels and kitchen towels are B2; oven gloves (B5.6.03) and aprons (B5.6.04) are B5.
- A knife made to cut or prepare food at a board or table is B5 (B5.2.1, B5.4.2); a knife made for trade, craft or pocket use (box cutter, pocket knife, multi-tool, everyday-carry locking folder) is C1; a fighting, hunting, butterfly or automatic knife is E4 (K-83). A cutting tool made to cut food (kitchen shears) is B5; general household scissors are C5 (K-171).
- A dishwasher (B5.6.01), a refrigerator (B5.3.01), a wine fridge (B5.3.02), a dish rack (B5.6.02) and a water filter jug (B5.5.3.02) are B5, not B6 or B7; washing-up liquid, sponges, brushes, a kitchen bin, kitchen and oven cleaner, descalers, dishwasher salt and cleaning tablets are B6; filter cartridges, including those for a water filter jug, and plumbed water filters are B7 (B-33, K-11).
- A bowl, plate or vessel made to hold or serve food is B5, however decorative or collected, while a vase or a bowl made only to be looked at is B4; a decanter (B5.4.3.03) and a cocktail shaker (B5.5.4.01) are B5; a wine rack, bar cart, kitchen cabinet, kitchen island, shelf or humidor is B1.
- Racks and rails that hold several kitchen objects are B1.5.2 (racks, hooks and hangers); the dish rack stays B5.6.02; a rack made for one appliance is a part in B5.7 (section 14).
- Coffee beans, tea leaves and wine are J, but the equipment to brew, grind, pour and drink them is B5; home-brewing and winemaking ingredients are J5 and their equipment is B5.5.5 (K-58); honey extraction and bottling gear is B10 (K-106).
- A camping stove, pan or mug is B5 by what it does, camping a setting. Drink bottles (B5.3.05) and hydration bladders (B5.3.06) are B5 whether or not made for a sport; a hydration pack sold with its bag is A4 (K-161). An insulated lunch bag or cool bag is B5.3.04 (K-131). A scale goes with its task, and a pocket scale is B5.2.4.04 (K-167).
- A connected oven, scale or kettle is B5 by its task (step 24 note); a smart display or voice assistant in a kitchen is D3.
- A toy kitchen or play food that cannot cook or serve to the real object's standard is E1; a real pan, knife or cup made in a child's size stays B5, with size and user as attributes and tags (C15).
- A component, lid, jar or attachment made to be fitted to one kitchen object is B5.7 and follows that object; cases and covers are parts only when made for one object at a time; racks and shelves that hold several objects are B1 (S3, CV-17).
