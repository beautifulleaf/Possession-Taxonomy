import json, os
CH = "https://en.wikipedia.org/wiki/Jewelry_chain"
def X(n, d, s, a="", mk="", y="", v=None, dt=""):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": v or [], "dt": dt}
kinds = [
 {"n": "Necklace chain", "a": "chain necklace", "d": "Linked metal chain worn on its own or with a pendant, named by its link pattern.",
  "t": ["yellow gold", "white gold", "rose gold", "sterling silver", "platinum", "stainless steel", "solid", "hollow"],
  "s": "https://www.tanishq.co.in/shop/jewellery",
  "x": [
   X("Cable chain", "Oval or round links of round wire joined in a simple alternating sequence, copying ship's anchor chain.", CH, a="anchor chain · trace",
     v=[{"n": "Trace chain", "mk": "", "y": "", "d": "slender cable with small uniform round or oval links"},
        {"n": "Belcher chain", "mk": "", "y": "", "d": "rolo; each link wider than it is thick"},
        {"n": "Faceted cable", "mk": "", "y": "", "d": "links with flattened, faceted sides"}],
     dt="link size · round or oval links · fine to heavy gauge"),
   X("Curb chain", "Twisted links that interlock and lie flat; made from a few millimetres to over four centimetres wide.", CH, a="Cuban · twisted",
     dt="width 2–40 mm+ · diamond-cut or plain"),
   X("Figaro chain", "Curb variation: a set of usually three short links followed by one elongated link.", CH, dt="link ratio (3+1, 1+1) · width"),
   X("Box chain", "Square-section chain of looser, rectangular box links.", CH,
     v=[{"n": "Venetian chain", "mk": "", "y": "", "d": "tighter, square-linked version"}], dt="width · square or round box"),
   X("Snake chain", "Tightly joined chain with a round or square cross-section and a smooth, slight zigzag look.", CH, dt="round or square section · diameter"),
   X("Herringbone chain", "Flat chain of short angled segments set flush in a continuous V-pattern, like a herring's skeleton.",
     "https://robinsonsjewelers.com/blogs/news/what-is-a-herringbone-chain-and-why-is-it-delicate-spoiler-its-the-drama-queen-of-your-jewelry-box",
     dt="width · flat profile; prone to kinking"),
   X("Singapore chain", "Fine twisted curb-style chain that keeps a natural curve and a liquid look.", CH, dt="gauge · twisted or flat"),
   X("Spiga chain", "Twisted interlocking links resembling plaited wire or an ear of wheat; durable and snag-free for pendants.", CH, a="wheat chain"),
   X("Anchor chain with bar", "Oval links each crossed by a bar, after ship's mooring chain.", CH, a="mariner · marina · stud link",
     v=[{"n": "Chaîne d'ancre", "mk": "Hermès", "y": "1938", "d": "drawn by Robert Dumas from boat anchor chains on the Normandy coast; first made in silver by the artisan De Percin; later in gold and as long sautoirs"}],
     dt="interlinks curb or trace · alternating plain links"),
   X("Franco chain", "Square-cut curb-type chain with V-shaped links, named after its Italian designer.", CH, dt="width · solid or hollow"),
   X("Byzantine chain", "Woven chain in which each link connects to four others.", CH, a="Turkish chain"),
   X("Ball chain", "Small metal balls joined by short lengths of wire.", CH, a="bead chain", dt="ball diameter · faceted or smooth"),
   X("Paperclip chain", "Long, open cable links shaped like paper clips.", CH, dt="link length · flat or round wire"),
   X("Omega chain", "Not a true chain: metal plates mounted on wire or mesh to look like a smooth collar of links.", CH),
   X("Foxtail chain", "V-shaped pattern of two rows of oval rings joined by flat rings.", CH),
  ]},
 {"n": "Pearl necklace", "a": "pearl strand", "d": "Strand of pearls worn as a necklace, named by length and pearl type.",
  "t": ["collar (25–33 cm)", "choker (36–41 cm)", "princess (43–48 cm)", "matinée (51–61 cm)", "opera (71–89 cm)", "rope (over 110 cm)",
        "Akoya", "South Sea", "Tahitian", "freshwater", "keshi", "baroque", "natural", "single strand", "multi-strand", "graduated"],
  "s": "https://anumerton.com/product/pearl-strands-stack-builders",
  "x": [
   X("Cultured Akoya pearl strand", "Strand of round cultured Akoya pearls, the type Mikimoto developed and sold from his Ginza shop.", "https://en.wikipedia.org/wiki/K%C5%8Dkichi_Mikimoto",
     mk="Mikimoto", y="1893 (first cultured pearls); round pearls c. 1905",
     dt="pearl size 2–10 mm · cream or white · length from collar to opera"),
  ]},
 {"n": "Tennis necklace", "a": "rivière · tennis chain", "d": "Flexible line of evenly set stones worn round the neck.",
  "t": ["four-prong", "bezel", "buttercup", "channel", "graduated", "uniform", "natural diamond", "lab-grown diamond", "moissanite", "cubic zirconia"],
  "s": "https://www.borsheims.com/round-diamond-3-prong-riviera-tennis-necklace-in-white-gold-17-1017-cttw",
  "x": [
   X("Rivière", "Single row of individually set stones of one variety, traditionally graduated from the centre, with no other ornament.", "https://www.antiquejewel.com/glossary/riviere",
     v=[{"n": "Double rivière", "mk": "", "y": "", "d": "two rivières worn together, one longer than the other"},
        {"n": "Victorian amethyst rivière", "mk": "", "y": "Victorian", "d": "lesser gemstones such as amethyst"}],
     dt="diamonds in silver or platinum · amethyst and other gemstones · graduated stones"),
   X("Tennis chain", "Hip-hop line necklace of individually prong-set stones, sold as iced-out bling.", "https://www.hiphopbling.com/collections/tennis-chains",
     dt="width 2–20 mm · 16–36 in · diamond, moissanite or CZ · gold, silver or stainless steel · combined with Cuban or rope links"),
  ]},
 {"n": "Choker", "a": "", "d": "Necklace that fits closely round the neck, usually 36–41 cm long.",
  "t": ["velvet", "ribbon", "lace", "leather", "beaded", "metal", "with pendant"],
  "s": "https://www.thejewelryjunkie.com/collections/choker/leather-beaded-necklace",
  "x": [
   X("Dog collar", "Broad jewelled choker of diamonds, pearls, lace or velvet, made fashionable around 1900 by Queen Alexandra.", "https://en.wikipedia.org/wiki/Choker",
     a="collier de chien", y="c. 1900; revived 1920s–1940s", dt="multi-row pearls · diamond plaques · velvet band"),
   X("Ribbon choker", "Plain thin band of red or black ribbon tied at the throat, as in Manet's Olympia (1861).", "https://en.wikipedia.org/wiki/Choker",
     y="19th century", dt="colour · width · with or without a small pendant"),
  ]},
 {"n": "Collar necklace", "a": "broad collar", "d": "Flat, wide necklace that lies round the base of the neck and over the collarbone.",
  "s": "https://www.thejewelryjunkie.com/collections/choker/leather-beaded-necklace",
  "x": [
   X("Usekh collar", "Ancient Egyptian broad collar of tube and teardrop beads in curved rows, with end pieces and often a counterweight.", "https://en.wikipedia.org/wiki/Usekh",
     a="wesekh · broad collar", y="Old Kingdom onwards (c. 2670 BC)", dt="faience, glass, stone or metal beads · rows · end pieces"),
   X("Livery collar", "Heavy gold chain of office or allegiance worn over the shoulders.", "https://en.wikipedia.org/wiki/Livery_collar",
     a="chain of office", y="14th century onwards",
     v=[{"n": "Collar of Esses", "mk": "", "y": "14th century", "d": "repeated S-shaped links; Lancastrian badge, still worn by heralds"}],
     dt="links · pendant badge"),
  ]},
 {"n": "Statement necklace", "a": "bib necklace", "d": "Large necklace of fixed ornamental elements, stones or metalwork across its front, worn as the focal point of an outfit.",
  "t": ["bib", "cluster", "beaded", "crystal", "metal"],
  "s": "https://www.bloomingdales.com/shop/jewelry-accessories/womens-fashion-statement-necklaces/Color_normal/Silver?id=1005660"},
 {"n": "Lariat", "a": "Y-necklace", "d": "Long necklace without a clasp, worn looped, knotted or threaded through itself.",
  "t": ["chain", "pearl", "beaded", "Y-drop with clasp"],
  "s": "https://jennifermillerjewelry.com/collections/lariat",
  "x": [
   X("Sautoir", "Very long chain or rope falling below the waist and ending in a tassel or pendant.", "https://josephjewelry.com/guide/glossary/sautoir",
     y="1920s (Art Deco)", dt="pearl strands · twisted ropes · tassel or pendant end"),
  ]},
 {"n": "Beaded necklace", "a": "", "d": "Necklace of beads strung together, of glass, stone, wood or other material.",
  "t": ["glass", "gemstone", "wood", "seed bead", "shell", "single strand", "multi-strand"],
  "s": "https://www.thejewelryjunkie.com/collections/choker/leather-beaded-necklace",
  "x": [
   X("Love beads", "Single strand of stone or glass beads.", "https://en.wikipedia.org/wiki/Necklace", dt="bead material · length"),
   X("Chaozhu", "Qing dynasty court necklace of 108 beads, also used for counting.", "https://en.wikipedia.org/wiki/Necklace", y="Qing dynasty",
     dt="bead material · counter strings"),
  ]},
 {"n": "Neck ring", "a": "torc · torque", "d": "Rigid ring of metal worn round the neck, open or closed.",
  "s": "https://shopdelapaix.com/products/torque-18kt-gold-necklace",
  "x": [
   X("Celtic torc", "Large rigid neck ring of a single piece or twisted strands, usually open at the front, of Iron Age Europe.", "https://en.wikipedia.org/wiki/Torc",
     y="8th century BC – 3rd century AD",
     v=[{"n": "Vix torc", "mk": "", "y": "c. 480 BC", "d": "gold, winged horses; France"},
        {"n": "Glauberg torc", "mk": "", "y": "c. 400 BC", "d": "gold, animal decoration; Germany"},
        {"n": "Snettisham Torc", "mk": "", "y": "1st century BC", "d": "multi-stranded electrum; Norfolk"},
        {"n": "Broighter torc", "mk": "", "y": "1st century BC", "d": "hollow, relief decoration; Ireland"}],
     dt="gold, electrum, silver or bronze · twisted or hollow · terminals"),
   X("Viking neck ring", "Torc-style silver neck ring of the Viking Age.", "https://en.wikipedia.org/wiki/Torc", y="Viking Age", dt="twisted silver rods"),
  ]},
 {"n": "Station necklace", "a": "Saturn chain · bobble chain", "d": "Fine chain with stones, beads or discs set at intervals along it.",
  "t": ["bezel-set diamonds", "pearls", "beads", "regular or irregular spacing"],
  "s": "https://deutschhouston.com/blog/diamonds-by-the-yard",
  "x": [
   X("Diamonds by the Yard", "Round diamonds in individual bezels set at intervals along a fine chain, designed by Elsa Peretti.", "https://deutschhouston.com/blog/diamonds-by-the-yard",
     mk="Tiffany & Co.", y="1974", dt="18k gold or platinum · number of stations · length"),
   X("Saturn chain", "Chain with evenly spaced beads, discs or ovals.", CH, a="bobble chain"),
  ]},
]
brands = [
 {"n": "Hermès", "c": "France", "f": "1837", "seg": "Luxury house", "d": "Paris saddlery house turned luxury goods maker.", "lines": ["Chaîne d'ancre"],
  "eras": ["Robert Dumas"], "sig": ["Chaîne d'ancre"], "sc": [], "rel": [], "s": "https://www.journalduluxe.fr/fr/hbjo/chaine-d-ancre-une-success-story-hermes"},
 {"n": "Tiffany & Co.", "c": "United States", "f": "1837", "seg": "Luxury jeweller", "d": "New York jeweller and silversmith.", "lines": ["Elsa Peretti"],
  "eras": ["Elsa Peretti, from 1974"], "sig": ["Diamonds by the Yard"], "sc": [], "rel": [], "s": "knowledge"},
 {"n": "Mikimoto", "c": "Japan", "f": "1899", "seg": "Pearl jeweller", "d": "Tokyo pearl jeweller founded by Kōkichi Mikimoto, pioneer of cultured Akoya pearls.",
  "lines": [], "eras": ["Kōkichi Mikimoto, 1899"], "sig": ["Cultured Akoya pearl strand"], "sc": [], "rel": [], "s": "https://en.wikipedia.org/wiki/Mikimoto_(company)"},
]
notes = ("All 9 old kinds kept; Station necklace added (new, sourced). Mangalsutra not here (South Asian shelf). "
 "Rope chain left out of Necklace chain archetypes because the Hip-hop shelf has its own Rope chain kind; Cuban kept only as a Curb alias for the same reason. "
 "Left out for lack of a retrieved source: Mikimoto named strand versions, the tennis chain's origin story, Cartier/Duchess of Windsor bib (1947), J. Crew statement necklace (Jenna Lyons popularised the term in the early 2010s per Wikipedia, not added as an archetype), "
 "Hermès Punk/other Chaîne d'ancre necklace models, Tiffany Diamonds by the Yard stone counts. Pearl lengths and pearl types are t attributes (Pearl article). No traditions on this shelf (handled by the regional shelves).")
out = {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes}
p = "/home/user/Possession-Taxonomy/rebuild/work/A3/shelves/02_00.json"
os.makedirs(os.path.dirname(p), exist_ok=True)
json.dump(out, open(p + ".tmp", "w"), ensure_ascii=False, indent=1); os.replace(p + ".tmp", p)
print("ok", sum(len(k.get("x", [])) for k in kinds))
