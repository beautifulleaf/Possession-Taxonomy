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
 S("Quartz, chalcedony & opal",MIN_BRIEF+"Quartz absorbs the crystal-shop varieties: rock crystal, amethyst, citrine (note heated amethyst), smoky, rose, ametrine, Herkimer diamond, Japan-law twin; geodes and points as dt. Agate gets classic agate types (Lake Superior, Laguna, Botswana, Fairburn, Condor, Dryhead, crazy lace); jasper named jaspers (ocean, picture, bumblebee is not jasper—note). Opal: precious vs common, Coober Pedy, Lightning Ridge, Yowah, Ethiopian Welo, hyalite.",
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
   K("Rutile",ids(160)),K("Cassiterite",ids(155)),K("Cuprite",ids(164)),K("Goethite",ids(156)),K("Uraninite",ids(162))]),
 S("Carbonates",MIN_BRIEF+"Icons: Sweet Home and N'Chwaning rhodochrosite, Elmwood and Dalnegorsk calcite, Iceland spar, Congo and Israeli malachite, Bisbee/Milpillas azurite, Tsumeb cerussite and smithsonite, Brumado magnesite, Spanish aragonite twins, Eugui dolomite.",
  [K("Calcite",ids(140)),K("Rhodochrosite",ids(149)),K("Malachite",ids(141)),K("Azurite",ids(142)),K("Aragonite",ids(143)),K("Smithsonite",ids(151)),
   K("Cerussite",ids(145)),K("Aurichalcite",ids(144)),K("Dolomite",ids(146)),K("Siderite",ids(150)),K("Magnesite",ids(148))]),
 S("Sulfates, chromates & tungstates",MIN_BRIEF+"Gypsum: selenite, desert rose, Naica, satin spar. Celestine geodes (Madagascar), anhydrite (angelite). Wulfenite (Red Cloud, Los Lamentos, Ojuela), crocoite (Dundas, Tasmania), scheelite (Tong Bei), ferberite/hübnerite (Peru, Pasto Bueno).",
  [K("Barite",ids(193)),K("Celestine",ids(195)),K("Gypsum",ids(194)),K("Anhydrite",ids(196)),K("Anglesite",ids(197)),K("Brochantite",ids(206)),
   K("Linarite",ids(214)),K("Cyanotrichite",ids(212)),K("Wulfenite",ids(226)),K("Crocoite",ids(227)),K("Scheelite",ids(225)),K("Ferberite",ids(230)),K("Hübnerite",ids(231))]),
 S("Phosphates",MIN_BRIEF+"Add Variscite (Utah, Fairfield). Turquoise: mine names (Sleeping Beauty, Kingman, Bisbee, Lander Blue, Persian Nishapur), stabilised vs natural, block/reconstituted fakes. Apatite merges apatite, fluorapatite, hydroxylapatite (one kind, species as types). Torbernite merges metatorbernite (radioactivity note).",
  [K("Turquoise",ids(233)),K("Apatite",ids("234,235,236"),"Species names as types."),K("Vivianite",ids(238)),K("Wavellite",ids(237)),K("Variscite",[],"New species kind."),
   K("Brazilianite",ids(239)),K("Lazulite",ids(240)),K("Torbernite",ids("241,242")),K("Ludlamite",ids(255)),K("Strengite",ids(256)),K("Phosphosiderite",ids(257)),
   K("Libethenite",ids(299)),K("Pseudomalachite",ids(300))]),
 S("Arsenates & vanadates",MIN_BRIEF+"Icons: Ojuela adamite, Mibladen and ACF vanadinite, Bunker Hill and Daoping pyromorphite, Santa Eulalia/Tsumeb mimetite, Bou Azzer erythrite and roselite, Tsumeb legrandite? (no: Ojuela legrandite), Tsumeb descloizite, Cornish olivenite and clinoclase.",
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
  [K("Dioptase",ids(119)),K("Chrysocolla",ids(121)),K("Charoite",ids(117)),K("Sugilite",ids(118)),K("Willemite",ids(120)),K("Eudialyte",ids(123)),K("Titanite",ids(124))]),
]
REG="rare species: goes to the Mindat-linked species register (rule keeps ~150–250 popular collector species in the tree)"
reg_ids=[6]  # placeholder removed below
