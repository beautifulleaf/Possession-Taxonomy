import json,re,sys
old=json.load(open('/home/user/Possession-Taxonomy/rebuild/work/F6/old.json'))
names={k['id']:k['n'] for d in old['depts'] for s in d['s'] for k in s['k']}
def K(n,old=(),brief=None):
    if isinstance(old,str): old=[old]
    d={"n":n,"old":list(old)}
    if brief: d["brief"]=brief
    return d
def ids(spec):  # "1,2,7" -> ['k1','k2','k7']
    return ['k%d'%int(x) for x in str(spec).split(',')]
def S(n,brief,kinds,web=True): return {"n":n,"web":web,"brief":brief,"k":kinds}

MIN_BRIEF=("Kind = mineral species (IMA name, Mindat-linked). Under each species add archetypes for named varieties and classic "
 "locality types (e.g. a famous mine or district habit), ordered by significance; versions = notable localities/finds with years; "
 "dt = habit, size class (thumbnail, miniature, small cabinet, cabinet, museum), matrix, colour, fluorescence, treatments. "
 "Source each archetype from Mindat, Wikipedia or a museum/reference page. ")
minerals=[
 S("Quartz, chalcedony & opal",MIN_BRIEF+"Quartz absorbs the crystal-shop varieties: rock crystal, amethyst, citrine (note heated amethyst), smoky, rose, ametrine, Herkimer diamond, Japan-law twin; geodes and points as dt. Agate gets classic agate types (Lake Superior, Laguna, Botswana, Fairburn, Condor, Dryhead, crazy lace); jasper named jaspers (ocean, picture, Biggs; note that 'bumblebee jasper' is a trade name for a volcanic rock). Opal: precious vs common, Coober Pedy, Lightning Ridge, Yowah, Ethiopian Welo, hyalite.",
  [K("Quartz",ids("1,2,7,8,9"),"Merge of rock crystal, amethyst, rose, smoky and citrine kinds; varieties become archetypes."),
   K("Agate and chalcedony",ids(3),"Chrysoprase, carnelian, onyx, blue lace as chalcedony varieties."),
   K("Jasper",ids(4)),K("Opal",ids(5))]),
 S("Native elements",MIN_BRIEF+"Gold: nuggets, crystallised gold, wire, leaf (California, Australia); silver wires (Kongsberg, Imiter); copper (Michigan Keweenaw); bismuth: separate natural from lab-grown hopper crystals (type); sulfur (Sicily Agrigento, Bolivia); platinum nuggets (Urals, Kondyor).",
  [K("Native gold",ids(180)),K("Native silver",ids(182)),K("Native copper",ids(181)),K("Native platinum",ids(186)),K("Native bismuth",ids(184)),K("Sulfur",ids(183))]),
 S("Sulfides & sulfosalts",MIN_BRIEF+"Add Cinnabar (Hunan/Guizhou twins). Icons: Navajún pyrite cubes, Huanzala pyrite, Dalnegorsk/Trepča galena and sphalerite, Xikuangshan/Ichinokawa stibnite, Shimen realgar, Quiruvilca orpiment, Chañarcillo proustite, Herodsfoot bournonite.",
  [K("Pyrite",ids(165)),K("Galena",ids(170)),K("Sphalerite",ids(175)),K("Chalcopyrite",ids(168)),K("Stibnite",ids(176)),
   K("Cinnabar",[],"New species kind."),K("Realgar",ids(174)),K("Orpiment",ids(172)),K("Marcasite",ids(171)),K("Pyrrhotite",ids(173)),
   K("Bournonite",ids(166)),K("Proustite",ids(179)),K("Chalcocite",ids(167)),K("Stephanite",ids(178))]),
 S("Halides & borates",MIN_BRIEF+"Fluorite: Rogerley/Weardale, Elmwood, Berbes, Dal'negorsk, Chinese, Illinois Cave-in-Rock, blue john (Derbyshire) as archetype. Halite: Searles Lake hoppers, blue halite. Ulexite 'TV stone'. Painite and jeremejevite as famous rarities.",
  [K("Fluorite",ids(187)),K("Halite",ids(188)),K("Ulexite",ids(340)),K("Borax",ids(338)),K("Colemanite",ids(339)),K("Painite",ids(355)),K("Jeremejevite",ids(357))]),
 S("Oxides",MIN_BRIEF+"Add Chrysoberyl (alexandrite, cat's-eye, trillings). Corundum specimens (ruby in matrix, sapphire crystals; ruby-zoisite and ruby-in-fuchsite move here from old Ruby as rock varieties). Hematite (Rose of iron, Elba, kidney ore), magnetite (lodestone), rutile (rutilated quartz), spinel (Mogok), cuprite (chalcotrichite), uraninite (radioactivity note), cassiterite.",
  [K("Corundum",ids(152)),K("Spinel",ids(161)),K("Chrysoberyl",[],"New species kind."),K("Hematite",ids(153)),K("Magnetite",ids(157)),
   K("Rutile",ids(160)),K("Cassiterite",ids(155)),K("Cuprite",ids(164)),K("Goethite",ids(156)),K("Bixbyite",ids(154)),K("Uraninite",ids(162))]),
 S("Carbonates",MIN_BRIEF+"Icons: Sweet Home and N'Chwaning rhodochrosite, Elmwood and Dalnegorsk calcite, Iceland spar, Congo and Israeli malachite, Bisbee/Milpillas azurite, Tsumeb cerussite and smithsonite, Brumado magnesite, Spanish aragonite twins, Eugui dolomite.",
  [K("Calcite",ids(140)),K("Rhodochrosite",ids(149)),K("Malachite",ids(141)),K("Azurite",ids(142)),K("Aragonite",ids(143)),K("Smithsonite",ids(151)),
   K("Cerussite",ids(145)),K("Aurichalcite",ids(144)),K("Dolomite",ids(146)),K("Siderite",ids(150)),K("Magnesite",ids(148))]),
 S("Sulfates, chromates & tungstates",MIN_BRIEF+"Gypsum: selenite, desert rose, Naica, satin spar. Celestine geodes (Madagascar), anhydrite (angelite). Wulfenite (Red Cloud, Los Lamentos, Ojuela), crocoite (Dundas, Tasmania), scheelite (Tong Bei), ferberite/hübnerite (Peru, Pasto Bueno).",
  [K("Barite",ids(193)),K("Celestine",ids(195)),K("Gypsum",ids(194)),K("Anhydrite",ids(196)),K("Anglesite",ids(197)),K("Brochantite",ids(206)),
   K("Linarite",ids(214)),K("Cyanotrichite",ids(212)),K("Wulfenite",ids(226)),K("Crocoite",ids(227)),K("Scheelite",ids(225)),K("Ferberite",ids(230)),K("Hübnerite",ids(231)),K("Ettringite",ids(201))]),
 S("Phosphates",MIN_BRIEF+"Add Variscite (Utah, Fairfield). Turquoise: mine names (Sleeping Beauty, Kingman, Bisbee, Lander Blue, Persian Nishapur), stabilised vs natural, block/reconstituted fakes. Apatite merges apatite, fluorapatite, hydroxylapatite (one kind, species as types). Torbernite merges metatorbernite (radioactivity note).",
  [K("Turquoise",ids(233)),K("Apatite",ids("234,235,236"),"Species names as types."),K("Vivianite",ids(238)),K("Wavellite",ids(237)),K("Variscite",[],"New species kind."),
   K("Brazilianite",ids(239)),K("Lazulite",ids(240)),K("Torbernite",ids("241,242")),K("Ludlamite",ids(255)),K("Strengite",ids(256)),K("Phosphosiderite",ids(257)),
   K("Libethenite",ids(299)),K("Pseudomalachite",ids(300))]),
 S("Arsenates & vanadates",MIN_BRIEF+"Icons: Ojuela adamite, Mibladen and ACF vanadinite, Bunker Hill and Daoping pyromorphite, Santa Eulalia/Tsumeb mimetite, Bou Azzer erythrite and roselite, Ojuela legrandite, Tsumeb descloizite, Cornish olivenite and clinoclase.",
  [K("Vanadinite",ids(249)),K("Pyromorphite",ids(247)),K("Mimetite",ids(248)),K("Descloizite",ids(250)),K("Adamite",ids(315)),K("Legrandite",ids(316)),
   K("Olivenite",ids(311)),K("Clinoclase",ids(312)),K("Conichalcite",ids(314)),K("Erythrite",ids(324)),K("Annabergite",ids(325)),K("Scorodite",ids(326)),K("Roselite",ids(328))]),
 S("Beryl, topaz & gem silicates",MIN_BRIEF+"Beryl varieties as archetypes: emerald (Muzo, Chivor), aquamarine (Shigar, Erongo, Santa Maria), morganite, heliodor, goshenite, red beryl (Wah Wah). Topaz (Ouro Preto imperial, Thomas Range, Volodarsk), zircon, kyanite (Brazil blades), andalusite (chiastolite), benitoite (San Benito), staurolite (fairy crosses), olivine/forsterite (peridot, Pakistan), grandidierite as a gem rarity.",
  [K("Beryl",ids(22)),K("Topaz",ids(23)),K("Zircon",ids(24)),K("Olivine (forsterite)",ids(129),"Peridot as the gem variety."),K("Benitoite",ids(32)),
   K("Kyanite",ids(25)),K("Andalusite",ids(26)),K("Staurolite",ids(34)),K("Danburite",ids(28)),K("Cordierite",ids(29),"Iolite."),K("Euclase",ids(30)),
   K("Phenakite",ids(31)),K("Axinite",ids(35),"Ferro-axinite and other species as types."),K("Grandidierite",ids(133))]),
 S("Tourmaline & garnet groups",MIN_BRIEF+"Group → species. Elbaite absorbs generic tourmaline: rubellite, indicolite, watermelon, Paraíba, verdelite; Himalaya Mine, Pederneira, Paprok. Schorl (Erongo), dravite (Yinnietharra), fluor-liddicoatite (Madagascar slices). Almandine absorbs generic garnet (Gore Mountain, Wrangell); grossular (hessonite, tsavorite, Jeffrey Mine), andradite (demantoid, melanite, topazolite), spessartine (Loliondo, Tongbei), uvarovite (Outokumpu, Saranovskii).",
  [K("Elbaite",ids("10,12"),"Merge with generic tourmaline."),K("Schorl",ids(13)),K("Dravite",ids(14)),K("Uvite",ids(15)),K("Fluor-liddicoatite",ids(16)),
   K("Almandine",ids("11,17"),"Merge with generic garnet."),K("Grossular",ids(19)),K("Andradite",ids(18)),K("Spessartine",ids(20)),K("Uvarovite",ids(21))]),
 S("Feldspars & feldspathoids",MIN_BRIEF+"Old 'Feldspar' kind becomes Labradorite (plagioclase: labradorite, spectrolite, sunstone); moonstone under orthoclase, amazonite under microcline (Pikes Peak with smoky quartz), cleavelandite under albite. Lapis merges lazurite (Sar-e-Sang, Chile). Haüyne (Eifel), sodalite (Bancroft, hackmanite).",
  [K("Labradorite",ids(36),"Generic feldspar kind becomes plagioclase/labradorite; other feldspars by species."),K("Microcline",ids(37)),K("Orthoclase",ids(38)),
   K("Albite",ids(40)),K("Lapis lazuli and lazurite",ids("44,45")),K("Sodalite",ids(42)),K("Haüyne",ids(43))]),
 S("Micas, chlorite & serpentine",MIN_BRIEF+"Add Lepidolite. Muscovite (books, fuchsite variety), clinochlore (seraphinite), talc (soapstone), serpentine merges lizardite (antigorite, williamsite as types).",
  [K("Muscovite",ids(47)),K("Lepidolite",[],"New species kind."),K("Biotite",ids(48)),K("Phlogopite",ids(49)),K("Clinochlore",ids(52)),K("Talc",ids(51)),
   K("Serpentine",ids("55,56"),"Lizardite, antigorite as types.")]),
 S("Zeolites",MIN_BRIEF+"Deccan Traps (Pune, Nashik, Jalgaon) and Iceland/Faroes as classic localities; add Heulandite.",
  [K("Stilbite",ids(61)),K("Heulandite",[],"New species kind."),K("Scolecite",ids(62)),K("Natrolite",ids(60)),K("Mesolite",ids(63)),K("Chabazite",ids(65)),
   K("Analcime",ids(64)),K("Laumontite",ids(66)),K("Harmotome",ids(67))]),
 S("Apophyllite, prehnite & datolite",MIN_BRIEF+"Apophyllite on stilbite (Deccan), okenite puffballs, cavansite (Wagholi), prehnite (Mali, Australia), pectolite with larimar (Dominican Republic) as variety archetype, datolite (Michigan, Charcas).",
  [K("Apophyllite",ids(74),"Fluorapophyllite-(K) and related species as types."),K("Okenite",ids(75)),K("Cavansite",ids(77)),K("Prehnite",ids(76)),
   K("Pectolite",ids(79),"Larimar."),K("Datolite",ids(86))]),
 S("Pyroxenes & amphiboles",MIN_BRIEF+"Add Jadeite (jade rough: Myanmar, Guatemala); nephrite noted as a tremolite–actinolite rock. Spodumene (kunzite, hiddenite), diopside (chrome diopside, Merelani), rhodonite (Broken Hill), serandite (Mont Saint-Hilaire), neptunite with benitoite, babingtonite.",
  [K("Spodumene",ids(93)),K("Diopside",ids(88)),K("Jadeite",[],"New species kind; nephrite as a tremolite–actinolite note."),K("Rhodonite",ids(94)),
   K("Actinolite",ids(96)),K("Tremolite",ids(97)),K("Serandite",ids(95)),K("Neptunite",ids(101)),K("Babingtonite",ids(102))]),
 S("Epidote, vesuvianite & hemimorphite",MIN_BRIEF+"Epidote (Green Monster Mtn, Knappenwand), zoisite (tanzanite crystals, thulite, anyolite/ruby-zoisite), vesuvianite (Jeffrey Mine), ilvaite, hemimorphite (Mapimí).",
  [K("Epidote",ids(103)),K("Zoisite",ids(105)),K("Vesuvianite",ids(107)),K("Hemimorphite",ids(109)),K("Ilvaite",ids(108))]),
 S("Dioptase, charoite & other silicates",MIN_BRIEF+"Dioptase (Tsumeb, Kaokoveld, Congo), charoite (Murun), sugilite (Wessels), chrysocolla (gem silica), willemite (Franklin fluorescent), eudialyte (Kola), titanite (sphene).",
  [K("Dioptase",ids(119)),K("Chrysocolla",ids(121)),K("Charoite",ids(117)),K("Sugilite",ids(118)),K("Willemite",ids(120)),K("Eudialyte",ids(123)),K("Titanite",ids(124)),K("Inesite",ids(85)),K("Afwillite",ids(83))]),
]
REG="rare species: goes to the Mindat-linked species register (rule keeps ~150–250 popular collector species in the tree)"
GEM_BRIEF=("Kind = GIA gem species or variety; archetypes = named varieties and trade/origin types (e.g. Kashmir sapphire, Paraíba tourmaline, Mexican fire opal), "
 "famous named stones may be versions only where a sourced page exists; dt = carat range, cut, colour, treatment. Source from GIA Gem Encyclopedia pages, Wikipedia or lab pages. "
 "Add brand-register entries (seg 'Gem laboratory') for GIA, AGS, IGI, HRD, Gübelin, SSEF, GRS, AGL, and for lab-grown producers where notable. ")
gems=[
 S("Diamonds, lab-grown & simulants",GEM_BRIEF+"Diamond: colourless D–Z, fancy colours (champagne/cognac as trade names for browns, pink Argyle, blue, yellow canary), shapes as types; famous stones only as context. Lab-grown: HPHT vs CVD as archetypes. Simulants: moissanite (Charles & Colvard), cubic zirconia (Swarovski Zirconia), white sapphire, YAG/GGG as historic.",
  [K("Natural diamond",ids(389)),K("Lab-grown diamond",[],"New kind."),K("Lab-created coloured gemstone",[],"New kind: synthetic ruby, sapphire, emerald (Chatham, Gilson), spinel, alexandrite, opal; flame-fusion vs flux vs hydrothermal."),
   K("Moissanite and diamond simulants",[],"New kind.")]),
 S("Coloured gemstones",GEM_BRIEF+"Ruby: Burmese/Mogok 'pigeon's blood', Thai/Cambodian, Mozambique, star ruby; ruby-zoisite and ruby-in-fuchsite go to Corundum/Zoisite specimens as rocks, not cut gems. Sapphire: Kashmir, Ceylon, padparadscha, Montana Yogo, fancy colours, star. Emerald: Colombian Muzo/Chivor, Zambian, trapiche. Topaz: imperial, irradiated blues (London/Swiss/Sky as types). Garnet: pyrope, rhodolite, Malaya, tsavorite, demantoid, hessonite, spessartite, colour-change. Tourmaline: rubellite, Paraíba, chrome, bicolour. Opal: black (Lightning Ridge), boulder, white, crystal, fire opal, Ethiopian. Quartz gems: amethyst, citrine, ametrine, prasiolite. Add Aquamarine & beryl, Alexandrite & chrysoberyl, Peridot and Jade (jadeite imperial, nephrite).",
  [K("Ruby",ids(392)),K("Sapphire",ids(391)),K("Emerald",ids(393)),K("Aquamarine and other beryl",[],"New kind: aquamarine, morganite, heliodor, red beryl."),
   K("Cut spinel",ids(399)),K("Alexandrite and chrysoberyl",[],"New kind."),K("Tanzanite",ids(400)),K("Cut tourmaline",ids(397)),
   K("Cut garnet",ids(396)),K("Cut topaz",ids(394)),K("Cut amethyst, citrine and quartz gems",ids(395)),
   K("Cut opal",ids(398)),K("Peridot",[],"New kind."),K("Jade",[],"New kind: jadeite and nephrite, carved and cabochon; grading (Type A/B/C).")]),
 S("Pearls & organic gems",GEM_BRIEF+"Pearl: natural (Gulf/Basra), saltwater cultured akoya, South Sea, Tahitian, freshwater (Edison), keshi, baroque, conch and melo as rare natural non-nacreous; value factors as dt (lustre, surface, shape, size, nacre). Precious coral: Corallium red/pink (Sardinian, Aka, Momo), CITES note. Jet: Whitby jet. Amber stays in Fossils.",
  [K("Pearl",ids(390),"Loose pearl; renamed."),K("Precious coral",[],"New kind."),K("Jet",[],"New kind.")]),
]
FOS_BRIEF=("Kind = taxon group; archetypes = named genera/species and classic Lagerstätten or formations (locality/formation is the organising detail, as in the finding). "
 "Versions = notable finds or locality types; dt = matrix, preparation, restoration/composite, size. Source from Wikipedia, PBDB or museum pages. ")
fossils=[
 S("Ammonites & cephalopods",FOS_BRIEF+"Ammonites: Madagascar Cleoniceras (cut pairs), Dactylioceras (Whitby), Asteroceras, pyritised Lyme Regis, Placenticeras, heteromorphs (Baculites, Didymoceras); ammolite from Placenticeras (Korite) as gem. Nautiloids: Orthoceras (Moroccan, move the alias here from belemnite), Cenoceras. Belemnites: Belemnitella, Jurassic guards.",
  [K("Ammonite",ids(363)),K("Ammolite",ids(366)),K("Fossil nautiloid",ids(365),"Takes Orthoceras."),K("Belemnite",ids(364),"Drop the Orthoceras alias.")]),
 S("Trilobites & arthropods",FOS_BRIEF+"Trilobites: Elrathia kingii (Utah), Moroccan (Phacops, Walliserops, Dicranurus), Russian (Asaphus kowalewskii), Calymene (Dudley bug), Isotelus, Ogygiocarella; note fakes and casts. Crustaceans: Eryma, Mecochirus (Solnhofen), Green River shrimp. Add Eurypterid (Eurypterus remipes) and Fossil horseshoe crab (Mesolimulus).",
  [K("Trilobite",ids(367)),K("Fossil crustacean",ids(368)),K("Eurypterid",[],"New kind: sea scorpions."),K("Fossil horseshoe crab",[],"New kind.")]),
 S("Marine invertebrate fossils",FOS_BRIEF+"Add Crinoid (Crawfordsville, Seirocrinus plates, LeGrand). Echinoderms: echinoids (Micraster, Clypeaster), starfish, blastoids. Brachiopods (Spirifer), bivalves (Gryphaea 'devil's toenail', Exogyra), gastropods (Turritella agate), corals (horn coral, Petoskey stone, Favosites), bryozoans (Archimedes), graptolites, sponges (Ventriculites).",
  [K("Crinoid",[],"New kind."),K("Echinoderm fossil",ids(370),"Echinoids, starfish, blastoids."),K("Fossil brachiopod",ids(371)),K("Fossil bivalve",ids(372)),
   K("Fossil gastropod",ids(373)),K("Fossil coral",ids(369)),K("Bryozoan fossil",ids(374)),K("Graptolite",ids(375)),K("Fossil sponge",ids(376))]),
 S("Vertebrate fossils",FOS_BRIEF+"Shark teeth: Otodus megalodon, Otodus obliquus, Cretoxyrhina, Squalicorax; localities (Peace River, Lee Creek, Khouribga). Fish: Knightia and Diplomystus (Green River), Lebanese fish, Santana concretions. Dinosaurs: Spinosaurus and Carcharodontosaurus teeth (Kem Kem), hadrosaur and Triceratops material, eggs; legality notes. Add Marine reptile fossil (mosasaur teeth/jaws from Morocco, plesiosaur, ichthyosaur). Mammals: woolly mammoth (tusk, tooth), cave bear, Smilodon; reptiles/amphibians: crocodilians, pterosaurs, synapsids, Permian amphibians.",
  [K("Fossil shark tooth",ids(377)),K("Fossil fish",ids(381)),K("Dinosaur fossil",ids(378)),K("Marine reptile fossil",[],"New kind split from reptiles."),
   K("Fossil reptile or amphibian",ids(380)),K("Fossil mammal",ids(379))]),
 S("Plant, wood & trace fossils",FOS_BRIEF+"Petrified wood (Arizona Petrified Forest-origin rules, Madagascar, Indonesian opalised), plant fossils (Mazon Creek ferns, Glossopteris, Ginkgo, Green River leaves), stromatolites (Bolivia, Australia), trace fossils (dinosaur footprints, burrows, coprolites as archetype, gastroliths).",
  [K("Petrified wood",ids(382)),K("Plant fossil",ids(383)),K("Stromatolite",ids(384)),K("Trace fossil",ids(385),"Coprolites and footprints as archetypes.")]),
 S("Amber & copal",FOS_BRIEF+"Amber by deposit: Baltic, Dominican (blue), Burmese (burmite; ethics note), Mexican (Chiapas), Lebanese; inclusions as dt; pressed/reconstituted and fake amber. Copal: Colombian, Madagascan. Fossil insects: Green River, Crato Formation compression fossils, amber inclusions.",
  [K("Amber",ids(386)),K("Copal",ids(387)),K("Fossil insect",ids(388))]),
]
MET_BRIEF=("Kind = meteorite class (Meteoritical Bulletin classification); archetypes = official meteorite names (Meteoritical Bulletin Database record as source) in order of fame; "
 "versions = falls/find years and notable masses; dt = slice, etched, endcut, individual, crust, TKW, weight. Dealer/certifier register: IMCA and notable dealers if sourced. ")
meteor=[
 S("Meteorites",MET_BRIEF+"Irons: Gibeon, Campo del Cielo, Sikhote-Alin, Canyon Diablo, Muonionalusta, Nantan, Dronino. Pallasites: Imilac, Seymchan, Esquel, Brenham, Fukang, Admire, Sericho. Mesosiderites: Vaca Muerta, Estherville. Ordinary chondrites: Chelyabinsk, NWA, Holbrook, Pultusk, L'Aigle. Carbonaceous: Allende, Murchison, Aguas Zarcas. Add Enstatite chondrite (Abee). HED: NWA eucrites, Millbillillie, Tatahouine. Lunar/Martian: NWA and named finds (Tissint, Zagami, NWA 7034 'Black Beauty'). Other achondrites: aubrites (Norton County), ureilites, angrites.",
  [K("Iron meteorite",ids(401)),K("Pallasite",ids(402)),K("Mesosiderite",ids(403)),K("Ordinary chondrite",ids(404)),K("Carbonaceous chondrite",ids(405)),
   K("Enstatite chondrite",[],"New kind."),K("HED meteorite",ids(407)),K("Lunar meteorite",ids(408)),K("Martian meteorite",ids(409)),K("Other achondrite",ids(406),"Aubrites, ureilites, angrites, brachinites.")]),
 S("Tektites & impact glass",MET_BRIEF+"Tektites by strewn field: moldavite (Czech), indochinites, australites (buttons), bediasites, georgiaites, philippinites; moldavite fakes. Impact glass: Libyan Desert Glass, Darwin glass, Wabar glass, Atacamaite. Impactites: suevite, shatter cones (Sudbury, Kentland), Muong Nong-type.",
  [K("Tektite",ids(410),"Split: tektites only."),K("Impact glass",[],"New kind split from old Tektite and impactite."),K("Impactite and shatter cone",[],"New kind.")]),
]
rocks=[
 S("Rocks, nodules & teaching sets","Kind = rock type (BGS/USGS rock classification); archetypes = named decorative or collector varieties with locality (orbicular granite, larvikite, snowflake obsidian, mahogany obsidian, rainbow obsidian, Chinese writing stone, picture sandstone, Picasso marble, Carrara marble, Coconino/Paesina picture stones, Petoskey is a coral—not here). Add Limestone (fossiliferous, Paesina landscape stone), Geode and thunder egg (Keokuk, Brazilian, Oregon thunder eggs), Septarian nodule (Utah, Madagascar). Fulgurite moves here from minerals (natural glass). Teaching sets: types by school level and brands only if sourced. Sources: Wikipedia, BGS, USGS.",
  [K("Granite",ids(411)),K("Basalt",ids(412)),K("Obsidian",ids(413)),K("Rhyolite",ids(414),"Rainforest jasper and wonderstone as archetypes."),K("Porphyry",ids(415)),
   K("Sandstone",ids(416)),K("Limestone",[],"New kind."),K("Marble",ids(417)),K("Slate",ids(418)),K("Fulgurite",ids(6)),
   K("Geode and thunder egg",[],"New kind."),K("Septarian nodule",[],"New kind."),K("Rock and mineral teaching set",ids(419))]),
]
SH_BRIEF=("Kind = family (WoRMS accepted name in brief/aliases); archetypes = collector-icon species by significance (WoRMS or Wikipedia record as source); "
 "dt = size in mm, grade (Gem, F+++, F++, F+, F), locality data, colour form. Note CITES/protected status where relevant (giant clams, Charonia, some Conus). ")
shells=[
 S("Sea snail shells",SH_BRIEF+"Cypraeidae (tiger, money, golden cowrie, Leucodon), Conidae (glory-of-the-sea Conus gloriamaris, textile cone), Muricidae (Venus comb, Murex pecten), Volutidae (Cymbiola, Amoria), Strombidae (queen conch, spider conch Lambis), Olividae, Cassidae (helmet, bonnet), Charoniidae (triton's trumpet), Harpidae, Mitridae, Haliotidae (paua, abalone), Epitoniidae (precious wentletrap), and land snails (Polymita, Liguus, Papustyla).",
  [K("Cowrie",ids(420)),K("Cone shell",ids(421)),K("Murex shell",ids(422)),K("Volute shell",ids(423)),K("Conch and stromb shell",[],"New kind."),K("Olive shell",[],"New kind."),
   K("Helmet and bonnet shell",[],"New kind."),K("Triton shell",[],"New kind."),K("Harp shell",[],"New kind."),K("Mitre shell",[],"New kind."),
   K("Abalone shell",[],"New kind."),K("Wentletrap shell",[],"New kind."),K("Land snail shell",[],"New kind.")]),
 S("Bivalves, nautilus & other shells",SH_BRIEF+"Pectinidae (lion's paw, Pecten maximus), Spondylidae (thorny oysters), Tridacnidae (giant clam; CITES), Cardiidae (heart cockle), Nautilidae (chambered nautilus; CITES Appendix II since 2016—verify), Argonautidae (paper nautilus), and living brachiopods (lamp shells).",
  [K("Scallop shell",ids(424)),K("Thorny oyster",[],"New kind."),K("Giant clam shell",[],"New kind."),K("Cockle shell",[],"New kind."),
   K("Chambered nautilus shell",[],"New kind."),K("Paper nautilus",[],"New kind."),K("Brachiopod shell",ids(425))]),
 S("Corals, urchins & sea stars",SH_BRIEF+"Coral skeletons (brain coral, staghorn, sea fans/gorgonians; CITES for stony corals), urchin tests (sand dollars, pencil urchins, heart urchins as archetypes), dried starfish and brittle stars.",
  [K("Coral skeleton",ids(426)),K("Sea urchin test",ids(427)),K("Dried starfish",ids(428))]),
]
TAX_BRIEF=("Note legality in each kind (CITES, ivory bans, migratory-bird and protected-species laws; antique/pre-Convention papers). Archetypes = named forms and recognised maker traditions "
 "(e.g. Victorian cased birds; Rowland Ward, Peter Spicer, Van Ingen, Walter Potter anthropomorphic tableaux) with sources; add tradition entries for Victorian taxidermy and Indian Van Ingen if sourced. ")
tax=[
 S("Taxidermy mounts",TAX_BRIEF+"Mammal: shoulder mount, full mount, head, rug, European mount; bird: cased, dome, flying; reptile: snake, crocodilian; add Fish mount (skin vs replica, Rowland Ward/ J. Cooper & Sons cased fish).",
  [K("Taxidermy mammal mount",ids(429)),K("Taxidermy bird mount",ids(430)),K("Taxidermy fish mount",[],"New kind."),K("Taxidermy reptile mount",ids(431))]),
 S("Skulls & skeletons",TAX_BRIEF+"Skull archetypes by animal (deer, bear, beaver, crow, alligator, piranha); preparation (beetle-cleaned, whitened) as dt. Add Replica skull and fossil cast (Bone Clones, Skulls Unlimited replicas, museum casts of hominid and dinosaur skulls).",
  [K("Mammal skull",ids(432)),K("Bird skull",ids(433)),K("Reptile skull",ids(434)),K("Fish skull",ids(435)),K("Articulated skeleton",ids(436)),
   K("Replica skull and fossil cast",[],"New kind.")]),
 S("Horns, tusks, teeth & eggs",TAX_BRIEF+"Antlers (sheds, red deer, moose, elk), horns (kudu, ram, buffalo), tusks (warthog, hippo, walrus—legal notes; elephant ivory restricted), claws and teeth (bear claw, sperm whale tooth/scrimshaw note), shark jaws (great white restricted), eggs (ostrich, emu, elephant bird) and nests; oology legality.",
  [K("Antler or horn",ids(437)),K("Tusk specimen",ids(438)),K("Claw or tooth specimen",ids(439)),K("Shark or fish jaw",ids(440)),K("Egg or nest specimen",ids(441))]),
 S("Insects, plants & wet specimens",TAX_BRIEF+"Pinned Lepidoptera (Morpho, birdwings—CITES, Ornithoptera), framed vs papered (A1 grade); add Pinned beetle and other insect (Goliath beetle, Hercules beetle, rhinoceros beetle, scorpions, tarantulas); feathers (legal issues), herbarium sheets (antique pressed-plant albums), resin-embedded specimens, fluid-preserved (antique wet specimens, cleared-and-stained).",
  [K("Pinned butterfly or moth",ids(442)),K("Pinned beetle and other insect",[],"New kind."),K("Feather specimen",ids(443)),K("Herbarium sheet",ids(444)),
   K("Insect in resin",ids(445)),K("Fluid-preserved specimen",ids(446))]),
]
elem=[S("Element samples","Element collecting hobby. Archetypes: element sets and periodic-table displays (Theodore Gray periodic table table and cards, Luciteria element cubes and sets), noble-gas glow ampoules, high-purity crystals (bismuth, gallium, osmium bead) as versions. Add Periodic table element collection (complete or partial sets in display). dt: purity, mass, size (10 mm/25.4 mm/1 in cube). Safety notes for radioactive and reactive elements.",
  [K("Element cube",ids(447)),K("Element ampoule",ids(448)),K("Encased element sample",ids(449)),K("Element crystal",ids(450)),K("Periodic table element collection",[],"New kind.")])]
disp=[S("Display domes & stands","Restraint only: no new kinds; aliases: Riker mount → frame case; perky box, gem jar, thumbnail box → single-specimen box; acrylic risers and museum putty as types of stand. Keep a few makers only if already present.",
  [K("Specimen display dome",ids(451)),K("Specimen stand",ids(452)),K("Specimen frame case",ids(453),"Riker mount alias."),K("Single-specimen box",ids(454))],web=False)]

plan={"lead":"Natural objects people collect—minerals, gemstones, fossils, meteorites, rocks, shells, taxidermy and other specimens, element samples and their displays—organised by scientific classification (mineral class → group → species, gem species → variety, taxon → locality/formation, meteorite class → official name, shell family → species), with dealers and gem laboratories in the brand register.",
 "b":[{"m":"Correct identification","v":"species/variety name per Mindat, GIA, WoRMS or the Meteoritical Bulletin","w":"Each field values a piece by its accepted name first; mislabelled and trade-name stock is common."},
      {"m":"Locality and provenance","v":"exact locality and old collection labels > country only > none","w":"Collectors price classic localities and documented provenance; locality is the main detail axis."},
      {"m":"Natural vs treated, restored or fake","v":"natural untreated > disclosed treatment/restoration > undisclosed","w":"Dyed, heated, irradiated, reconstituted and composite pieces and casts must be disclosed."},
      {"m":"Legal to own and move","w":"CITES, ivory and protected-species laws and national export rules (e.g. fossils, meteorites) govern many specimens."}],
 "depts":[
  {"n":"Minerals & crystals","mode":"variety","note":"Mineral class (Nickel–Strunz) → group → species → variety; ~170 popular collector species in the tree, all other species in a Mindat-linked species register.",
   "b":[{"m":"Size class","v":"micromount, thumbnail, miniature, small cabinet, cabinet, museum","w":"Standard collector size classes used by dealers and shows."},
        {"m":"Condition and aesthetics","v":"damage-free, sharp, lustrous, well-placed on matrix > dinged or repaired","w":"Mineral dealers and competition judging criteria."}],
   "s":minerals},
  {"n":"Gemstones & pearls","mode":"variety","note":"GIA gem species → variety → origin/trade type; lab-grown and simulants kept separate; gem laboratories in the brand register.",
   "b":[{"m":"Diamond 4Cs","v":"colour D–Z, clarity FL–I3, cut Excellent–Poor, carat","w":"GIA grading system, used worldwide."},
        {"m":"Lab report and treatment disclosure","v":"independent lab report (GIA, AGS, IGI, Gübelin, SSEF, GRS) with origin > seller's word","w":"Treatments and synthetics are undetectable by eye; reports set price."},
        {"m":"Coloured stone quality","v":"hue, tone, saturation, clarity type, cut, size, origin","w":"GIA coloured-stone grading approach."}],
   "s":gems},
  {"n":"Fossils & amber","mode":"variety","note":"Taxon → genus/species → locality and formation; restoration, composites and casts disclosed.",
   "b":[{"m":"Preparation and restoration","v":"natural, fully prepared > restored > composite > cast/fake","w":"Moroccan trilobites and Chinese fossils are often restored or faked."},
        {"m":"Locality, formation and legality","w":"Formation and Lagerstätte define value; export bans and public-land rules decide legality."}],
   "s":fossils},
  {"n":"Meteorites & impact glass","mode":"variety","note":"Class → official meteorite name (Meteoritical Bulletin) → specimen type.",
   "b":[{"m":"Official name and classification","v":"approved name in Meteoritical Bulletin Database > provisional (NWA number) > unclassified","w":"The Meteoritical Society names and classifies meteorites."},
        {"m":"Specimen type","v":"fusion-crusted individual > endcut > slice; etched for irons","w":"Dealer and collector convention."}],
   "s":meteor},
  {"n":"Rocks & teaching sets","mode":"variety","note":"Rock type (igneous, sedimentary, metamorphic) → named variety and locality.","b":[],"s":rocks},
  {"n":"Shells & coral","mode":"variety","note":"Family (WoRMS) → species → form; grade and size are details.",
   "b":[{"m":"Shell grade","v":"Gem, F+++, F++, F+, F, F-","w":"Conchological dealer grading convention."},{"m":"Collection data","v":"locality, depth, date > none","w":"Scientific value and price follow data."}],
   "s":shells},
  {"n":"Taxidermy, bones & preserved specimens","mode":"variety","note":"Animal group → specimen type; legality and preparation are details.",
   "b":[{"m":"Legal provenance","v":"captive-bred, natural death or pre-Convention antique with papers","w":"CITES and national wildlife laws."},
        {"m":"Preparation quality","v":"anatomy, eyes, sewing, no pest damage","w":"Taxidermy competition and dealer criteria."}],
   "s":tax},
  {"n":"Element samples","mode":"variety","note":"Sample form → element; purity and mass are details.","b":[],"s":elem},
  {"n":"Display domes & stands","mode":"tier","note":"Cases and mounts for showing specimens.","b":[],"s":disp},
 ],
 "moves":[], "drop":[]}

used=set()
for d in plan['depts']:
    for s in d['s']:
        for k in s['k']:
            for o in k['old']:
                assert o not in used,o; used.add(o)
for i in range(1,455):
    kid='k%d'%i
    if kid not in used:
        assert i<=362, (kid,names[kid])
        plan['drop'].append({"old":kid,"why":REG})
assert len(used)+len(plan['drop'])==454
json.dump(plan,open('plan.json','w'),ensure_ascii=False,indent=1)
nk=sum(len(s['k']) for d in plan['depts'] for s in d['s'])
new=sum(1 for d in plan['depts'] for s in d['s'] for k in s['k'] if not k['old'])
ns=sum(len(s['k']) for s in minerals)
print('depts',len(plan['depts']),'shelves',sum(len(d['s']) for d in plan['depts']),'kinds',nk,'new',new,'mineral species',ns,'drops',len(plan['drop']))
print('max shelf',max(len(s['k']) for d in plan['depts'] for s in d['s']))
print(', '.join(names[x['old']] for x in plan['drop']))
