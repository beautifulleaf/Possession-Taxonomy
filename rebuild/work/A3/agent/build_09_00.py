import json, os
W = 'https://en.wikipedia.org/wiki/'
MS = W + 'Mangalsutra'
TAN = 'https://blog.bluestone.com/what-is-tanmaniya-jewellery-meaning-history-and-cultural-significance/'
LONDE = 'https://londejewellers.com/guides/maharashtrian-bridal-jewellery-nagpur'
SKYT = 'https://skyjems.ca/pages/encyclopedia-maang-tikka-tradition'
KUSH = 'https://www.kushals.com/blogs/fashion-jewellery-blog/types-of-jhumkas-earrings'
EXO = 'https://www.exoticindia.com/blog/meet-jhumka-the-history-of-indian-earrings'
CHB = 'https://www.caratlane.com/blog/chandbali-earring-designs-that-will-blow-your-mind/'
NATH = 'https://www.mygoldguide.in/golden-naths'
MP = 'https://blog.bluestone.com/how-to-wear-a-matha-patti-styles-designs-and-inspiration/'
AZA = 'https://www.azafashions.com/blog/kamarbandh-is-back/'
VAD = 'https://blog.bluestone.com/what-is-vaddanam-types-designs-and-bridal-significance/'
BELT = 'https://www.mygoldguide.in/traditional-gold-waist-belts'
MANG = 'https://mangatrai.com/blogs/resources/heritage-pearl-necklace-designs-from-india-satlada-rani-haar-and-choker-explained'
OLD = 'https://www.tanishq.co.in/shop/jewellery'

def X(n, d, s, a='', y='', v=None, dt='', mk=''):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": v or [], "dt": dt}

kinds = [
 {"n": "Mangalsutra", "a": "Mangala sutra · tali · thali · mangalyam",
  "d": "Marriage necklace of black beads on a gold chain or thread, usually with a pendant, tied on the bride at a Hindu wedding.",
  "t": ["long", "short (daily wear)", "black-bead chain", "turmeric thread", "diamond pendant"],
  "s": OLD,
  "x": [
   X("Tanmaniya", "Maharashtrian mangalsutra: two strands of black and gold beads joined by a gold pendant, classically a two-cup vati.", TAN,
     a="Tanmani · vati mangalsutra",
     v=[{"n": "Vati pendant", "d": "two gold cups, one for each spouse"},
        {"n": "Khod pendant", "d": "stone setting of typically 5 or 7 stones with pearl capping and pearl latkans"},
        {"n": "Modern pendant", "d": "floral, geometric or solitaire designs, often diamond-set, sometimes removable"}],
     dt="22K or 18K gold · strand count · pendant style · length"),
   X("Lakshmi tali", "Telugu tali pendant design.", MS, dt="gold pendant · thread or chain"),
   X("Minnu", "Kerala tali; the Saint Thomas Christian minnu carries a cross.", MS, a="Ela tali",
     dt="small gold leaf-shaped or cross pendant · thread"),
   X("Kumbha tali", "Tali design worn by Tamil Kshatriya communities.", MS, dt="gold pendant"),
   X("Kali poath", "Black-bead marriage necklace worn by Deccani Muslim women.", MS, dt="black beads · gold elements"),
  ]},
 {"n": "Maang tikka", "a": "Mang tikka · tikka · tika",
  "d": "Ornament hung on a chain along the hair parting with a pendant resting on the forehead.",
  "t": ["kundan", "polki", "pearl", "temple gold", "oxidised silver"],
  "s": OLD,
  "x": [
   X("Borla", "Rajasthani maang tikka with a ball-shaped pendant instead of a flat or drop pendant.", SKYT, a="Rakhdi",
     dt="ball size · gold or silver · kundan or plain"),
   X("Passa", "Side-hanging ornament pinned at the temple, often worn with a central maang tikka.", SKYT, a="Jhoomar · jhumar",
     dt="pearl or gem strings · fan width"),
  ]},
 {"n": "Jhumka", "a": "Jhumki · jhumkas",
  "d": "Bell- or dome-shaped hanging earring, often with a fringe of small beads.",
  "t": ["gold", "oxidised silver", "pearl", "kundan", "meenakari", "polki", "diamond"],
  "s": OLD,
  "x": [
   X("Temple jhumka", "Jhumka modelled on temple jewellery, decorated with miniature deity figures.", KUSH,
     dt="gold or gold-plated · deity motif · kemp stones"),
   X("Hanging jhumka", "Bell drop hanging from a separate decorative stud.", EXO,
     v=[{"n": "Drop jhumka", "d": "stud and drop of similar size"},
        {"n": "Kanphool with sankali", "d": "Mughal-era form: stud linked by a chain to the hair, with pearl tassels"}],
     dt="stud shape · bell size · bead fringe"),
   X("Jhumar", "Chandelier-shaped jhumka falling to just above the shoulder.", EXO, dt="tiers · length"),
   X("Hoop jhumka", "Gold hoop carrying one or more small bells.", EXO, dt="hoop diameter · bell count"),
   X("Ear-cuff jhumka", "Jhumka joined to an ear cuff, often in a peacock design.", KUSH, dt="cuff motif · bell size"),
  ]},
 {"n": "Chandbali", "a": "Chand bali · chaand baali",
  "d": "Crescent-moon-shaped earring, usually gold or silver and often stone-set; the name means 'moon earring'.",
  "t": ["antique (beads and pendants)", "contemporary bridal", "everyday small", "pearl", "kundan", "diamond"],
  "s": CHB},
 {"n": "Nath", "a": "Nathni · nathuli · bridal nose ring",
  "d": "Large bridal nose ring, often chained to the hair or ear.",
  "t": ["with chain (nathni)", "without chain", "pearl", "ruby", "gold", "silver"],
  "s": NATH,
  "x": [
   X("Maharashtrian nath", "Large curved nose ring covering the side of the face, usually gold set with pearls or stones.", NATH,
     dt="size small 2–4 cm to ceremonial 8–12 cm · pearls · ruby · chain"),
   X("Tehri nath", "Giant gold Garhwali bridal nose ring with peacock and floral motifs, part of the bride's dowry.", NATH, a="Garhwali nath",
     dt="diameter · motifs · beads, rubies, pearls · chain"),
   X("Kumaoni nath", "Smaller, more petite bridal nath from Kumaon.", NATH, dt="diameter · gold"),
   X("Bengali nath", "Bridal nath worn through a septum piercing in the middle of the nose.", NATH, dt="gold · pendant drop"),
  ]},
 {"n": "Matha patti", "a": "Mathapatti · sheesh patti",
  "d": "Forehead ornament with a central pendant and side chains running along the hairline.",
  "t": ["pearl", "kundan", "polki", "single-strand", "multi-strand"],
  "s": MP,
  "x": [
   X("Borla matha patti", "Matha patti with a round Rajasthani borla as the central pendant.", MP, dt="borla size · chain strands"),
   X("Mundavalya", "Maharashtrian wedding forehead ornament of jasmine flowers or gold coins tied across the forehead.", LONDE,
     dt="flowers, pearls or gold coins · strand count"),
  ]},
 {"n": "Kamarbandh", "a": "Kamarband · kardhani · oddiyanam · vaddanam · waist belt",
  "d": "Bridal waist belt ornament worn over a saree or other drape.",
  "t": ["rigid", "flexible", "chain", "temple (kemp)", "antique finish", "diamond"],
  "s": AZA,
  "x": [
   X("Oddiyanam", "Rigid South Indian gold waist belt fastened at the back, part of the bridal set.", VAD, a="Vaddanam",
     v=[{"n": "Temple jewellery vaddanam", "d": "goddess, peacock and lotus motifs with kemp stones"},
        {"n": "Antique gold vaddanam", "d": "darkened, oxidised finish"},
        {"n": "Diamond vaddanam", "d": "brilliant-cut diamonds on white or yellow gold"}],
     dt="gold weight · motif · stones · hollow or solid"),
   X("Arapatta", "Flexible South Indian waist belt.", BELT, dt="link type · gold"),
   X("Kardhani", "Rajasthani gold girdle, rigid or flexible, now also worn as a belly chain.", BELT, dt="rigid or flexible · gold or silver"),
   X("Maharashtrian kamarband", "Thin gold waist chain that holds the saree pleats.", LONDE, a="Kandora", dt="chain weight · gold"),
  ]},
 {"n": "Haar and rani haar", "a": "Rani haar · queen's necklace · lada necklace",
  "d": "Long layered bridal necklace, usually falling below the chest.",
  "t": ["kundan", "polki", "pearl", "filigree gold", "temple gold"],
  "s": MANG,
  "x": [
   X("Rani haar", "Long necklace falling below the chest, anchored by an ornate gold pendant or clasp.", MANG,
     y="Mughal era", dt="length · pendant · kundan, polki or filigree"),
   X("Satlada", "Seven-strand necklace of pearls in graduated lengths, a Deccan Mughal and Nawabi bridal piece.", MANG,
     v=[{"n": "Nizam of Hyderabad's satlada", "y": "19th century", "d": "seven strings of Basra pearls, 465 pearls"},
        {"n": "Panchlada", "d": "five strands"},
        {"n": "Teenlada", "d": "three strands"}],
     dt="strand count · pearl type and size · clasp"),
   X("Laxmi haar", "Long Maharashtrian necklace with a Lakshmi deity pendant.", LONDE, dt="gold · coin or deity pendant"),
  ]},
]

T = "Jewellery & metalwork"
trads = [
 {"n": "Kundan", "g": T, "r": "Rajasthan and Gujarat, India", "p": "ancient; flourished in the Mughal era",
  "d": "Gem setting in which gold foil is burnished between the stone and its mount, mainly for elaborate necklaces.",
  "tech": "ghaat framework, wax paadh, khudai stone fitting, meenakari, pakai foil setting, chillai polishing",
  "mat": "pure gold, gold foil, uncut diamonds, coloured gemstones; silver copies",
  "forms": ["Haar and rani haar", "Maang tikka", "Matha patti", "Jhumka"],
  "ctr": ["Jaipur"], "auth": "", "s": W + "Kundan"},
 {"n": "Polki", "g": T, "r": "Rajasthan, India", "p": "Rajput courts",
  "d": "Natural diamonds cleaved from rough and lightly polished, not faceted, set foil-backed in gold.",
  "tech": "kundan foil setting behind the stone; enamelled reverse", "mat": "natural uncut diamonds, 22–24K gold, gold foil",
  "forms": ["Haar and rani haar", "Chandbali", "Maang tikka"], "ctr": ["Jaipur"],
  "auth": "genuine diamonds of irregular outline with flat foil-backed underside; meenakari reverse (a plain back suggests a shortcut piece)",
  "s": "https://www.jkdiamondsinstitute.com/blog/kundan-vs-polki-vs-jadau"},
 {"n": "Jadau", "g": T, "r": "North India; Rajasthan", "p": "peak under the Mughals, 16th–17th c.; Rajput courts 17th–18th c.; living",
  "d": "Prong-free setting of uncut and table-cut gems in gold, each stone locked by pressed kundan foil.",
  "tech": "24K kundan foil pressed cold around each stone into a chased 18–22K gold body; stones set last; reverse enamelled",
  "mat": "gold, polki, table- and flat-cut diamonds, foiled coloured stones, carved gem panels",
  "forms": ["Haar and rani haar", "Maang tikka", "Kamarbandh"], "ctr": ["Jaipur", "Bikaner", "Jodhpur", "Udaipur"],
  "auth": "no prongs; visible kundan border round each stone; enamelled reverse; flat-cut or uncut stones, not brilliants; watch for brilliant-cut replacements",
  "s": "https://skyjems.ca/pages/encyclopedia-jadau"},
 {"n": "Meenakari", "g": T, "r": "Iran; India (Rajasthan, Gujarat)", "p": "Safavid style c. 15th c.; brought to India by the Mughals",
  "d": "Enamelling of metal by fusing coloured powdered glass onto the surface.",
  "tech": "powdered glass fused at about 750–850 °C", "mat": "gold, silver, copper; coloured glass enamel",
  "forms": ["Jhumka", "Maang tikka", "Haar and rani haar"], "ctr": ["Rajasthan", "Gujarat"], "auth": "", "s": W + "Meenakari"},
 {"n": "Temple jewellery of Nagercoil", "g": T, "r": "Nagercoil, Kanniyakumari district, Tamil Nadu", "p": "traced to the Chola dynasty, 9th c. CE",
  "d": "Gold jewellery set with stones, first made to adorn temple deities and now worn by brides and Bharatanatyam dancers.",
  "tech": "", "mat": "gold; red and green kuchu kal (kemp) stones",
  "forms": ["Jhumka", "Kamarbandh", "Bangle"], "ctr": ["Nagercoil"],
  "auth": "Geographical Indication registered 2007–08", "s": W + "Temple_Jewellery_of_Nagercoil"},
 {"n": "Thewa", "g": T, "r": "Pratapgarh district, Rajasthan", "p": "Rajput era; invention credited to Nathu ji Soni, 1767 (unconfirmed)",
  "d": "Finely worked 23-carat gold sheet fused onto coloured glass.",
  "tech": "freehand etching of gold sheet on a lac base, fused onto treated glass", "mat": "23K gold sheet, coloured glass, lac resin",
  "forms": ["Jewellery", "Jewellery boxes", "Photo frames"], "ctr": ["Pratapgarh", "Raj-Soni family (Mahesh Raj Soni, Padma Shri 2015)"],
  "auth": "", "s": W + "Thewa"},
 {"n": "Tarakasi", "g": T, "r": "Cuttack, Odisha", "p": "more than 500 years old",
  "d": "Silver filigree made from fine drawn wire shaped and soldered by hand.",
  "tech": "silver cast into rod, drawn into wire, hand-shaped and soldered with borax; granulation", "mat": "silver of 90% purity or more",
  "forms": ["Anklet", "Toe ring", "Armlet", "Necklace", "Brooch", "Pendant", "Earrings", "Hairpin"],
  "ctr": ["Cuttack"], "auth": "", "s": W + "Tarakasi"},
]

notes = ("All three old kinds kept (Mangalsutra, Maang tikka, Jhumka) with old s; old model 'Tanmaniya Mangalsutra' became the Tanmaniya archetype. "
         "Five planned new kinds added with retrieved sources. No brands: archetypes here are maker-free regional forms. "
         "Left out: Wikidata was rate-limited (429); kalyanjewellers.net returned 406, so not used. Chandbali has types only (no sourced named archetypes). "
         "Nath forms like Rajasthani/Punjabi bulaq not added (no retrieved page). Thushi choker and Kolhapuri saaj seen on the Maharashtrian guide belong to "
         "Choker/Necklace shelves, not added here. Cuttack tarakasi recorded as 'Tarakasi' (Wikipedia title); GI status not confirmed so left blank.")

out = {"kinds": kinds, "brands": [], "traditions": trads, "notes": notes}
p = '/home/user/Possession-Taxonomy/rebuild/work/A3/shelves/09_00.json'
tmp = p + '.tmp'
json.dump(out, open(tmp, 'w'), ensure_ascii=False, indent=1)
os.replace(tmp, p)
print('written')
