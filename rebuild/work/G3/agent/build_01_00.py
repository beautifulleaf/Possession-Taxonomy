import json, os
W = 'https://en.wikipedia.org/wiki/'
BT, BD, CT, FT, SH = W+'Bathtub', W+'Bidet', W+'Composting_toilet', W+'Flush_toilet', W+'Shower'
NEO = 'https://totousa.com/blog/neorest-the-apex-of-smart-toilet-design-and-sustainability'
WAS = 'https://www.totousa.com/washlet-new'
GEB = 'https://geberit.co.uk/bathroom-products/wcs-urinals/shower-toilets-geberit-aquaclean/why-geberit-aquaclean/experience'
TARA = 'https://www.sieger-design.com/en/projects/a-timeless-icon/'
KV1 = 'https://www.stylepark.com/en/news/vola-kv1-fitting'
LB = 'https://sadecor.co.za/interior-design-blog/bathrooms/mercury-fittings-a-century-of-classics-with-lefroy-brooks/'
AX = 'https://hoteldesigns.net/member-news/axor-x-starck-celebrating-a-design-partnership-of-30-years/'
KAL = 'https://www.kaldewei.com/press/releases/newsdetails/news/the-future-needs-a-past-four-generations-of-kaldewei-3-1/'
VA = 'https://houseofrohl.design/en-gb/victoria-albert-baths/our-story/'
DR = 'https://www.drummonds-uk.com/product/spey-cast-iron-bath-tub-with-ball-claw-feet/'
CR = 'https://www.catchpoleandrye.com/?p=4076'
AQ = 'https://www.aqualisa.co.uk/about-aqualisa'

def X(n, d, s, mk='', y='', a='', v=(), dt=''):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s,
            "v": [dict(zip(("n", "mk", "y", "d"), t)) for t in v], "dt": dt}

kinds = [
 {"n": "Bathtub", "a": "Bath · Tub",
  "d": "Fixed or freestanding tub for bathing in, made in many materials, shapes and period styles.",
  "t": ["Built-in", "Freestanding", "Sunken", "Bath panel (front or end)", "Acrylic", "Enamelled steel", "Cast iron",
        "Stone resin", "Copper", "Victorian style", "Art Deco style", "Left-, right- or centre-drain"],
  "s": "https://kohler.ca/en/products/bathtubs/shop-alcove-bathtubs",
  "x": [
   X("Roll-top clawfoot bath", "Freestanding bath on claw feet with a rolled rim, one end rounded and one fairly flat.", BT,
     y="1880s–1930s", a="Roll-top bath · Clawfoot tub",
     v=[("Spey", "Drummonds", "", "Cast-iron roll-top on ball-and-claw feet; the maker's most spacious cast-iron bath"),
        ("Cast-iron reproductions", "Catchpole & Rye", "", "Copies of late-19th-century baths cast near Ashford, Kent")],
     dt="cast iron lined with porcelain enamel, or modern acrylic/fibreglass · feet styles · raw, primed, painted or polished exterior"),
   X("Slipper bath", "Clawfoot bath with one end raised and sloped for lounging.", BT, a="Slipper bathtub"),
   X("Double slipper bath", "Clawfoot bath with both ends raised and sloped.", BT),
   X("Double-ended bath", "Clawfoot bath with both ends rounded so two can sit at either end.", BT),
   X("Pedestal bath", "Bath resting on a solid pedestal base, often in Art Deco style.", BT),
   X("Enamelled steel bath", "Bath pressed from sheet steel and coated with vitreous enamel.", KAL, mk="Kaldewei", y="1934",
     v=[("Anker", "Kaldewei", "1934", "First Kaldewei enamelled bath, welded from several parts"),
        ("Seamless single-sheet bath", "Kaldewei", "1957", "Pressed from one sheet of steel on hydraulic presses"),
        ("Cono family", "Kaldewei", "1995", "Premium line designed with Ettore Sottsass")]),
   X("Stone-resin freestanding bath", "Moulded freestanding bath of volcanic limestone bound with resin.", VA,
     mk="Victoria + Albert Baths", y="1996", a="QUARRYCAST bath"),
   X("Whirlpool bath", "Bath with built-in water jets for massage.", BT, mk="Jacuzzi", y="1968",
     v=[("Spa Whirlpool", "Jacuzzi", "1968", "")]),
   X("Furo", "Short, deep Japanese-style tub in which the bather sits upright.", BT, a="Japanese soaking tub · Ofuro"),
  ],
  "m": [["Halite Adjustable Front Bath Panel", "Highlife Bathrooms"]],
  "r": [["Archer", "Kohler"], ["Devonshire", "Kohler"], ["Underscore", "Kohler"], ["Villager", "Kohler"],
        ["AXOR Suite", "Hansgrohe"]]},
 {"n": "Washbasin", "a": "Basin · Bathroom sink",
  "d": "Basin for washing hands and face; some are sold built into their cabinet.",
  "t": ["Pedestal", "Semi-pedestal", "Wall-hung", "Vessel (countertop)", "Inset or undermount", "Vanity unit",
        "Cloakroom", "Vitreous china", "Enamelled steel", "Stone"],
  "s": "https://www.wickes.co.uk/Wickes-Galeria-Ceramic-1-Tap-Hole-Basin-With-Full-Pedestal---550mm/p/233360",
  "m": [["Wickes Galeria", "Wickes"], ["AXOR Suite washbasin", "Hansgrohe"]]},
 {"n": "Flush toilet", "a": "Cistern-flush toilet · Water closet · WC",
  "d": "Toilet flushed by water from a cistern.",
  "t": ["Close-coupled", "Low-level cistern", "Back-to-wall", "Wall-hung", "Pedestal", "Washdown bowl", "Siphonic bowl",
        "Dual flush"],
  "s": "https://www.wickes.co.uk/p/233416",
  "x": [
   X("Washout closet", "Toilet with a shallow water pool flushed by a jet from behind; a Victorian form.", FT, y="1852",
     v=[("Jennings patent pan", "", "1852", "George Jennings' one-piece pan and trap"),
        ("National", "Twyford", "1879", "Thomas William Twyford's wash-out water closet")]),
   X("High-level cistern toilet", "Toilet with the cistern above head height, flushed by a pull chain.", FT,
     a="High suite · Pull-chain toilet", y="Victorian"),
   X("Dual-flush toilet", "Toilet whose cistern offers a small flush for liquids and a full flush for solids.", FT,
     mk="Caroma", y="1980", v=[("Duoset", "Caroma", "1980", "Two-button, two-volume cistern")]),
   X("Wall-hung toilet with concealed cistern", "Bowl hung on the wall, with the cistern hidden in a frame behind it.",
     W+'Geberit', mk="Geberit"),
  ],
  "m": [["Wickes Oxford", "Wickes"], ["WASHLET+ G5A", "TOTO"]]},
 {"n": "Shower toilet and bidet seat", "a": "Washlet · Warm-water toilet seat · Electronic bidet · Smart toilet",
  "d": "Toilet or powered seat that washes the user with warm water; integrated units add drying and automatic flushing.",
  "t": ["Integrated shower toilet", "Bidet seat (fits existing toilet)", "Non-electric bidet attachment", "Heated seat",
        "Warm-air dryer", "Remote control", "Auto open and close"],
  "s": WAS,
  "x": [
   X("Sanitarina", "First commercial electronic bidet toilet.", BD, mk="INAX", y="1967",
     v=[("Sanitarina 61", "INAX", "1967", ""), ("Sanitarina F1", "INAX", "1976", "Added a heated seat")]),
   X("Washlet", "Electronic bidet seat with a warm-water wand, operated from the seat or a remote.", WAS, mk="TOTO", y="1980",
     v=[("Washlet G", "TOTO", "1978–1980", "First Washlet, developed 1978–80"),
        ("S7A", "TOTO", "", "Fully automated, remote control, heated seat, EWATER+ bowl cleaning"),
        ("S7", "TOTO", "", ""), ("S5", "TOTO", "", ""), ("S2", "TOTO", "", ""),
        ("S550e", "TOTO", "", "Sensor-operated, auto open and close, night light"),
        ("C5", "TOTO", "", ""), ("C2", "TOTO", "", ""), ("A2", "TOTO", "", ""), ("K300", "TOTO", "", "")],
     dt="seat shape (round, elongated) · controls (side panel, remote) · dryer, deodoriser, night light"),
   X("Neorest", "Tankless toilet with an integrated Washlet seat and electronic controls.", NEO, mk="TOTO", y="1993",
     v=[("Neorest EX", "TOTO", "1993", "First tankless model"),
        ("Neorest NX", "TOTO", "", "All-in-one smart toilet; Red Dot award 2018"),
        ("Neorest AH / RH", "TOTO", "", "iF award 2019"),
        ("Neorest 700H", "TOTO", "", ""), ("Neorest 750H", "TOTO", "", "ACTILIGHT"), ("Neorest NX2", "TOTO", "", "ACTILIGHT"),
        ("Neorest WX1", "TOTO", "", ""), ("Neorest LS", "TOTO", "", ""), ("Neorest AS", "TOTO", "", ""),
        ("Neorest RS", "TOTO", "", "")]),
   X("AquaClean", "Geberit's shower toilets and shower-toilet seats.", GEB, mk="Geberit", y="1978",
     v=[("Geberella", "Geberit", "1978", "Shower seat for standard toilets"),
        ("Geberit-O-Mat", "Geberit", "1979", "First Geberit WC with integrated shower"),
        ("Balena", "Geberit", "1985", "First wall-hung integrated shower toilet in Switzerland"),
        ("AquaClean Sela", "Geberit", "", "First shower toilet not obviously looking like one"),
        ("AquaClean Mera Comfort", "Geberit", "", ""), ("AquaClean Tuma Comfort", "Geberit", "", ""),
        ("AquaClean Alba", "Geberit", "", "")]),
  ],
  "m": [["Bio Bidet 1000 (BB-1000)", "Bio Bidet"], ["Bio Bidet 800 Prestige", "Bio Bidet"], ["Swash 1000", "Brondell"],
        ["Clean Sense DIB-1500", "Clean Sense"], ["Clessence", "INAX"], ["Luscence", "INAX"],
        ["Infinity Bidet 3000", "Infinity"], ["Blooming Bidet Seat", "Blooming Bidet"], ["Feel Fresh", "HomeTech"]]},
 {"n": "Bidet", "a": "", "d": "Separate low basin, or a hand spray, for washing the lower body.",
  "t": ["Floor-standing", "Wall-hung", "Over-rim tap", "Spray jet"],
  "s": "https://www.kohler.com/en/products/toilets/shop-toilets/amaretto-horizontal-spray-bidet-with-3-faucet-holes-4864",
  "x": [X("Bidet shower", "Hand-held trigger spray beside the toilet, used for cleansing.", BD, a="Shattaf · Health faucet")],
  "m": [["Amaretto", "Kohler"]]},
 {"n": "Waterless or composting toilet", "a": "Compost toilet · Dry toilet",
  "d": "Toilet that uses no flush water, composting or storing the waste.",
  "t": ["Self-contained", "Split-system", "Urine-diverting", "Fan-assisted", "Heated"],
  "s": "https://thesolarstore.com/collections/sun-mar-composting-toilets",
  "x": [
   X("Clivus Multrum", "Composting toilet with a large chamber below the seat that also takes kitchen waste.", CT,
     mk="Clivus Multrum"),
   X("Self-contained composting toilet", "Unit that composts waste in a container within the toilet, sometimes with fan and heater.",
     CT, v=[("Excel", "Sun-Mar", "", ""), ("Spacesaver", "Sun-Mar", "", "")]),
   X("Urine-diverting dry toilet", "Dry toilet that separates urine from solids to control moisture.", CT),
  ],
  "m": [["Centrex 1000", "Sun-Mar"], ["Centrex 2000", "Sun-Mar"], ["Centrex 3000", "Sun-Mar"], ["GTG", "Sun-Mar"]]},
 {"n": "Bath and basin tap", "a": "Tap · Faucet · Mixer tap",
  "d": "Hand-operated valve that delivers water at a basin or bath; mixer taps and outside taps included.",
  "t": ["Pillar taps", "Monobloc basin mixer", "Bridge mixer", "Wall-mounted", "Bath filler", "Bath shower mixer",
        "Floor-standing bath filler", "Cross-head handles", "Lever handles", "Outside tap", "Edwardian style", "Art Deco style"],
  "s": "https://www.screwfix.com/c/bathrooms-kitchens/bathroom-taps/cat7310006?page_size=100",
  "x": [
   X("KV1", "Single-lever mixer with a double swivel spout, mechanics hidden, designed by Arne Jacobsen.", KV1, mk="Vola",
     y="1968", v=[("HV1", "Vola", "", "Washstand fitting"), ("111", "Vola", "", "Modular wall fitting")],
     dt="chrome, brass, stainless steel and 14 colours · kitchen or bathroom"),
   X("Tara", "Minimalist tap with cross handles and a slender semicircular spout, by sieger design.", TARA, mk="Dornbracht",
     y="1992", v=[("Refined Tara", "Dornbracht", "2007", "Slimmer handles and collars, slightly taller"),
                  ("Tara Black Edition / White Edition", "Dornbracht", "", "First matt black and matt white finishes"),
                  ("New finishes", "Dornbracht", "2022", "Dark chrome, champagne and brushed champagne (22-carat gold)")],
     dt="washstand, bath, shower and kitchen fittings · finishes"),
   X("AXOR Starck", "Philippe Starck's tap collection for AXOR, Hansgrohe's design brand.", AX, mk="Hansgrohe", y="1994",
     v=[("AXOR Starck Organic", "Hansgrohe", "2012", ""), ("AXOR Starck V", "Hansgrohe", "2015", "")]),
   X("1900 Classic", "Lefroy Brooks' Edwardian-style solid brass range with exposed workings and porcelain accents.", LB,
     mk="Lefroy Brooks", y="1900s style", a="Edwardian range",
     dt="solid brass, hand polished and plated · cross-head or lever"),
   X("Single-lever mixer tap", "Mixer that sets flow and temperature with one lever.", W+'Grohe', mk="Moen",
     v=[("Moen mixing faucet under licence", "Grohe", "1962", "Grohe gained exclusive production rights")]),
  ],
  "r": [["1930s Art Deco range", "Lefroy Brooks"], ["1935 Janey Mac", "Lefroy Brooks"], ["Edition 2000", "Dornbracht"],
        ["Downtown", "Aqualisa"], ["Uptown", "Aqualisa"]]},
 {"n": "Shower", "a": "",
  "d": "Shower unit or set for washing under running water; electric, mixer, power and digital types.",
  "t": ["Electric shower", "Mixer shower", "Power shower", "Digital shower", "Thermostatic", "Rain head", "Handset and riser rail",
        "Exposed bar valve", "Concealed valve"],
  "s": "https://www.wickes.co.uk/Products/Bathrooms/Showers%2BEnclosures/Showers/c/1074006",
  "x": [
   X("Thermostatic shower valve", "Mixing valve that holds a set water temperature automatically.", W+'Grohe',
     v=[("Skalatherm", "Grohe", "1956", "Automatic mixing valve with integrated thermostat"),
        ("Grohmix", "Grohe", "1979", "Thermostat line")]),
   X("Electric shower", "Shower that heats cold mains water electrically in the unit.", SH,
     v=[("T80 Easi-Fit+", "Triton Showers", "", ""), ("T80 Pro-Fit", "Triton Showers", "2017", "")]),
   X("Digital shower", "Mixer or power shower set through an electronic control panel.", AQ, mk="Aqualisa",
     v=[("Quartz", "Aqualisa", "", "Smart digital range: Quartz Touch, Classic, Blue"), ("Optic Q", "Aqualisa", "", ""),
        ("HOST", "Triton Showers", "2017", "Wireless digital mixer")]),
   X("Adjustable hand shower", "Hand shower on a hose whose spray can be adjusted.", W+'Hansgrohe', mk="Hansgrohe", y="1968",
     v=[("Hand shower", "Hansgrohe", "1928", "First affordable hand shower"), ("Adjustable-jet hand shower", "Hansgrohe", "1968", "")]),
   X("Rain shower head", "Large overhead head that lets water fall like rain at low or medium pressure.", SH),
  ],
  "m": [["Triton Asta", "Triton Showers"], ["Aquastream", "Aqualisa"], ["Midas 220", "Aqualisa"],
        ["AXOR ShowerComposition", "Hansgrohe"]]},
 {"n": "Shower filter", "a": "Shower head filter",
  "d": "Filter that treats water at the shower outlet only, mainly to reduce chlorine.",
  "t": ["Inline filter", "Filter shower head", "Replacement cartridge"],
  "s": "https://www.uk-water-filters.co.uk/pages/all-types-of-water-filters"},
]
# fix: Adjustable hand shower first version from Bidet page
kinds[7]["x"][3]["v"][0] = {"n": "Hand shower", "mk": "Hansgrohe", "y": "1928", "d": "First affordable hand shower (Hans Grohe, Schiltach)"}

def B(n, c, f, seg, d, s, lines=(), sig=(), rel=(), eras=()):
    return {"n": n, "c": c, "f": f, "seg": seg, "d": d, "lines": list(lines), "eras": list(eras), "sig": list(sig),
            "sc": [], "rel": list(rel), "s": s}

brands = [
 B("TOTO", "Japan", "1917", "Sanitaryware", "Kitakyushu maker of toilets and the Washlet electronic bidet seat.", W+'Toto_Ltd.',
   lines=["WASHLET", "NEOREST", "WASHLET+"], sig=["Washlet", "Neorest"], rel=["INAX", "Geberit"]),
 B("Geberit", "Switzerland", "1874", "Sanitary systems", "Rapperswil-Jona maker of concealed cisterns, piping and AquaClean shower toilets.",
   W+'Geberit', lines=["AquaClean"], sig=["AquaClean", "Wall-hung toilet with concealed cistern"], rel=["TOTO"],
   eras=["Founded by Caspar Melchior Gebert, 1874"]),
 B("Dornbracht", "Germany", "1950", "Luxury bathroom fittings", "Iserlohn family maker of high-end taps and showers.", W+'Dornbracht',
   lines=["Tara", "Edition 2000"], sig=["Tara"], rel=["Vola", "Hansgrohe"], eras=["Aloys F. and Helmut Dornbracht, from 1950"]),
 B("Vola", "Denmark", "", "Design taps", "Family-run Danish maker of the Arne Jacobsen tap system.", KV1,
   lines=["KV1", "HV1", "111"], sig=["KV1"], rel=["Dornbracht"]),
 B("Lefroy Brooks", "United Kingdom", "", "Period bathroom brassware", "British maker of solid brass taps in decade-by-decade period ranges.",
   LB, lines=["1900 Classic", "1930s Art Deco range", "1935 Janey Mac"], sig=["1900 Classic"]),
 B("Hansgrohe", "Germany", "1901", "Taps and showers", "Schiltach maker of taps and showers; AXOR is its designer brand (1993).",
   W+'Hansgrohe', lines=["AXOR", "hansgrohe"], sig=["AXOR Starck", "Adjustable hand shower"], rel=["Grohe", "Dornbracht"],
   eras=["AXOR founded 1993; Philippe Starck collections from 1994"]),
 B("Grohe", "Germany", "1936", "Taps and showers", "Hemer/Düsseldorf maker of taps, thermostats and shower fittings.", W+'Grohe',
   lines=["Skalatherm", "Grohmix", "Ladylux", "Europlus"], sig=["Thermostatic shower valve"], rel=["Hansgrohe"],
   eras=["Friedrich Grohe from 1936"]),
 B("Kaldewei", "Germany", "1918", "Steel-enamel baths", "Ahlen family maker of enamelled steel baths, shower trays and basins.", KAL,
   lines=["Anker", "Cono"], sig=["Enamelled steel bath"], eras=["Franz Kaldewei 1918; Heinrich 1952; Franz-Dieter 1973; Franz 2008"]),
 B("Victoria + Albert Baths", "United Kingdom", "1996", "Freestanding baths",
   "UK-based maker of freestanding baths and basins in QUARRYCAST, produced in South Africa.", VA,
   sig=["Stone-resin freestanding bath"]),
 B("Drummonds", "United Kingdom", "", "Cast-iron baths", "Maker of cast-iron, brass and copper baths and bathroom fittings.", DR,
   sig=["Roll-top clawfoot bath"], rel=["Catchpole & Rye"]),
 B("Catchpole & Rye", "United Kingdom", "", "Cast-iron baths", "Kent maker of cast-iron baths, with a foundry near Ashford and workshop in Pluckley.",
   CR, sig=["Roll-top clawfoot bath"], rel=["Drummonds"], eras=["Founded by Tony O'Donnell"]),
 B("Kohler", "United States", "1873", "Kitchen and bath", "Wisconsin maker whose first bath was an enamelled cast-iron trough (1883); owns Mira Showers.",
   W+'Kohler_Co.', lines=["Archer", "Devonshire", "Villager", "Kohler Konnect"], rel=["Mira"]),
 B("Aqualisa", "United Kingdom", "1977", "Showers", "Westerham shower maker that began with a thermostatic valve and claims the first digital shower.",
   AQ, lines=["Quartz", "Optic Q", "Midas", "Aquastream"], sig=["Digital shower"], rel=["Triton Showers"]),
 B("Triton Showers", "United Kingdom", "1975", "Electric showers", "Nuneaton maker of electric and mixer showers, owned by Norcros since 1987.",
   W+'Triton_Showers', lines=["T80", "HOST", "DuElec"], sig=["Electric shower"], rel=["Aqualisa"]),
]
notes = ("Bath panel merged into Bathtub as a type (model kept). TOTO Washlet SKU list cut to archetype versions; Washlet range moved "
         "from Flush toilet to Shower toilet; WASHLET+ G5A kept as a flush-toilet model. Kohler bath ranges trimmed to four. "
         "Not added (no retrievable page): Mira Showers brand entry and Leonard thermostatic valve, Drummonds Usk bateau, Separett Villa, "
         "Dornbracht MEM, Kaldewei Conoduo/Puro, V+A model names, Clos-o-Mat. Jacuzzi, Caroma, INAX, Moen, Clivus Multrum appear as "
         "archetype makers without register entries. Brand founding years left blank where pages gave none (Vola, Lefroy Brooks, "
         "Drummonds, Catchpole & Rye). No craft traditions needed for this shelf.")
out = {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes}
p = 'work/G3/shelves/01_00.json'; os.makedirs('work/G3/shelves', exist_ok=True)
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('ok', len(kinds), sum(len(k.get('x', [])) for k in kinds), len(brands))
