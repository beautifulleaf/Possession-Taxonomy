import json, os
W = "https://en.wikipedia.org/wiki/"
MAC = "https://madisonavenuecouture.com/blogs/news/a-brief-history-of-the-kelly-bag-a-classic-icon-by-hermes"
ROME = "https://romestation.ca/blogs/news/kelly-depeches-kelly-briefcases-executive-ready-hermes"
FIL = "https://rushfaster.com.au/blogs/au/the-filson-original-briefcase-rugged-heritage-work-bag"
POR = "https://sonofastag.com/products/porter-yoshida-co-tanker-2-way-briefcase-black-1"
MUL = "https://www.lyst.co.uk/bags/mulberry-heritage-briefcase/"
RAKE = "https://therake.com/stories/invest-ettinger-heritage-st-james-attache"
TUA = "https://www.abt.com/TUMI-Alpha-Brief-Pack-in-Deep-Pine-158957B186/p/239399.html"
ETTB = "https://ettingerlondon.com/products/metropolitan-bakerloo-portfolio-case"
GAL = "https://www.galenleather.com/collections/zippered-leather-portfolio"
K24 = "https://www.koffer24.de/en/business/pilot-x27-s-case/"

def X(n, d, mk, y, s, v=(), a="", dt=""):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s,
            "v": [dict(zip(("n", "mk", "y", "d"), q)) for q in v], "dt": dt}

kinds = [
 {"n": "Briefcase", "a": "work bag · document bag · laptop brief", "d": "Flat bag with a top handle for carrying papers, a laptop and work items.",
  "t": ["soft-sided", "structured", "expandable", "detachable shoulder strap", "leather", "nylon", "canvas"],
  "s": "https://www.rimowa.com/sg/en/luggage-collection-size-guide",
  "x": [
   X("Sac à dépêches", "Hermès dispatch bag adapted by Robert Dumas from the Haut à courroies; carried large as a briefcase by men such as John F. Kennedy.", "Hermès", "1928", MAC,
     [("Kelly Dépêches", "Hermès", "", "boxy briefcase with turnlock and short top handle, no shoulder strap; sizes 34, 36, 38 (38 discontinued)")],
     a="dispatch bag", dt="size 34–38 · Togo, Barenia, Epsom, Evergrain, alligator · palladium or gold-plated hardware"),
   X("James Bond briefcase", "Swaine Adeney Brigg's briefcase made for James Bond in the 1963 film From Russia with Love, faithful to Fleming's 1957 novel.", "Swaine Adeney Brigg", "1963", W + "Swaine_Adeney_Brigg",
     [], a="From Russia with Love briefcase", dt="leather"),
   X("Original Briefcase", "Filson's soft briefcase in water-resistant Rugged Twill with bridle-leather handles and a brass zip under a storm flap.", "Filson", "", FIL,
     [], a="Filson 256", dt="Rugged Twill · bridle leather trim · YKK brass zip · fits up to 16-inch laptop · colours"),
   X("Heritage Briefcase", "Mulberry's men's leather briefcase with laptop pocket, front document pocket and detachable strap.", "Mulberry", "", MUL,
     [], dt="38 × 28 × 8 cm · Small Classic Grain cow leather · black, other colours"),
   X("Alpha", "Tumi's business line in FXT ballistic nylon, covering briefcases, brief packs and travel pieces.", "Tumi", "", TUA,
     [("Alpha Brief Pack", "Tumi", "", "25 L briefcase-backpack, padded 15-16-inch laptop compartment")],
     dt="FXT ballistic nylon · leather trim · black and seasonal colours"),
   X("Tanker 2Way Briefcase", "Porter's nylon briefcase from the Tanker series, inspired by the MA-1 flight jacket, with rescue-orange lining.", "Porter", "", POR,
     [("622-79311-10", "Porter", "", "black, 41 × 30 × 7 cm, detachable shoulder strap")],
     dt="nylon twill · black, sage green · made in Japan"),
  ],
  "r": [["Alpha Bravo", "Tumi"], ["Arrivé", "Tumi"], ["Harrison", "Tumi"], ["Voyageur", "Tumi"]]},
 {"n": "Attaché case", "a": "attaché · hard briefcase", "d": "Hard-sided, box-shaped briefcase with a hinged lid.",
  "t": ["aluminium", "leather", "combination locks", "key locks"],
  "s": "https://www.1stdibs.com/buy/attache-case",
  "x": [
   X("Zero Halliburton aluminium case", "Sealed aluminium case first commissioned by Erle P. Halliburton for rough oil-field travel; used for Apollo 11 moon samples.", "Zero Halliburton", "1938", W + "Zero_Halliburton",
     [("Nuclear football", "Zero Halliburton", "", "modified case covered in black leather")],
     a="Halliburton case", dt="aluminium shell · silver, black · sizes"),
   X("St James Attaché", "Ettinger's made-to-order bridle-hide attaché modelled on a prototype by founder Gerry Ettinger.", "Ettinger", "", RAKE,
     [], a="Heritage St James Attaché", dt="nut bridle hide · blue skiver leather lining"),
   X("Rimowa Attaché", "Rimowa's grooved-aluminium attaché case, now a vintage piece that inspired Daniel Arsham's eroded suitcase series.", "Rimowa", "", W + "Rimowa",
     [], a="Attaché", dt="grooved aluminium · vintage"),
  ]},
 {"n": "Pilot case", "a": "pilot's case · flight case · business trolley", "d": "Deep, box-shaped hard case with a top opening and a handle, sometimes on wheels.",
  "t": ["wheeled", "hand-carried"], "s": K24,
  "m": [["NEXT Business Trolley", "Travelite"], ["LONDON 2.0 Business Trolley", "Paradise by CHECK.IN"], ["Rolling Tote Pro-DLX5 XS", "Samsonite"]]},
 {"n": "Document folio", "a": "portfolio · zip folio · padfolio · document case", "d": "Slim zip or flap leather case for papers or a laptop, carried in the hand.",
  "t": ["zip-around", "flap", "with writing pad", "A4", "A5", "B5"], "s": W + "Briefcase",
  "m": [["Metropolitan Bakerloo Portfolio Case", "Ettinger"], ["Zippered Leather Portfolio", "Galen Leather"]]},
]
brands = [
 {"n": "Hermès", "c": "France", "f": "1837", "seg": "Luxury house", "d": "Paris saddler turned luxury house, family-controlled through H51.",
  "lines": ["Kelly", "Birkin", "Sac à dépêches"], "eras": ["Robert Dumas, 1951–1978", "Jean-Louis Dumas, 1978–2005", "Pierre-Alexis Dumas, 2005–present"],
  "sig": ["Sac à dépêches", "Kelly", "Birkin"], "sc": [], "rel": [], "s": W + "Herm%C3%A8s"},
 {"n": "Swaine Adeney Brigg", "c": "United Kingdom", "f": "1798", "seg": "Heritage leather goods", "d": "London maker of leather goods, Brigg umbrellas and Herbert Johnson hats, rooted in an 18th-century whip maker.",
  "lines": ["Brigg umbrellas", "Herbert Johnson hats"], "eras": [], "sig": ["James Bond briefcase"], "sc": [], "rel": [], "s": W + "Swaine_Adeney_Brigg"},
 {"n": "Filson", "c": "United States", "f": "1897", "seg": "Heritage outdoor", "d": "Seattle maker of outdoor clothing and bridle-trimmed twill luggage.",
  "lines": [], "eras": [], "sig": ["Original Briefcase"], "sc": [], "rel": [], "s": W + "Filson_(company)"},
 {"n": "Mulberry", "c": "United Kingdom", "f": "1971", "seg": "Luxury leather goods", "d": "Somerset leather-goods house founded by Roger Saul and his mother Joan.",
  "lines": [], "eras": ["Stuart Vevers, 2005–2007", "Emma Hill, 2007–2013", "Johnny Coca, 2015–2020"],
  "sig": ["Heritage Briefcase"], "sc": [], "rel": [], "s": W + "Mulberry_(company)"},
 {"n": "Tumi", "c": "United States", "f": "1975", "seg": "Premium luggage", "d": "New Jersey luggage and bag maker known for black ballistic nylon, owned by Samsonite since 2016.",
  "lines": ["Alpha", "Alpha Bravo", "Arrivé", "Harrison", "Voyageur"], "eras": [], "sig": ["Alpha"], "sc": [], "rel": ["Samsonite"], "s": W + "Tumi_Inc."},
 {"n": "Ettinger", "c": "United Kingdom", "f": "1934", "seg": "Heritage leather goods", "d": "Family-owned London leather-goods maker known for bridle hide, holding royal warrants.",
  "lines": ["Bridle Hide", "Heritage", "Metropolitan"], "eras": [], "sig": ["St James Attaché"], "sc": [], "rel": [], "s": "https://ettingerlondon.com/pages/about-us"},
 {"n": "Rimowa", "c": "Germany", "f": "1898", "seg": "Premium luggage", "d": "Cologne luggage maker known for grooved aluminium shells since 1950, majority-owned by LVMH.",
  "lines": ["Original", "Classic", "Essential", "Hybrid", "Distinct"], "eras": [], "sig": ["Rimowa Attaché"], "sc": [], "rel": [], "s": W + "Rimowa"},
 {"n": "Zero Halliburton", "c": "United States", "f": "1938", "seg": "Aluminium luggage", "d": "Aluminium case maker founded on Erle P. Halliburton's commission, owned by Japan's ACE since 2006.",
  "lines": [], "eras": [], "sig": ["Zero Halliburton aluminium case"], "sc": [], "rel": [], "s": W + "Zero_Halliburton"},
]
notes = ("Tumi ranges kept once on Briefcase (Alpha as archetype, others as r) and in the Tumi brand entry; dropped Tumi Alpha/Alpha Bravo duplication. "
         "Old 'Kelly' range (Hermès) folded into the Sac à dépêches archetype; Kelly Dépêches is its version. "
         "Porter brand entry not added here (already registered by shelf 03_00). No year confirmed for Filson Original Briefcase, Mulberry Heritage, Tumi Alpha, Rimowa Attaché (sources conflict or silent). "
         "Pilot case kept QoL with 3 models from the koffer24 page (Gucci preloved listing left out). Document folio is new; source is the Briefcase article (portfolio/padfolio). No traditions apply.")
out = {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes}
p = "work/A4/shelves/05_00.json"; t = p + ".tmp"
json.dump(out, open(t, "w"), ensure_ascii=False, indent=1); os.replace(t, p)
