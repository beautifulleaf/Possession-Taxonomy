import json, os
W = 'https://en.wikipedia.org/wiki/'
GETA, ZORI, KOL, PESH, JUT, PAD = W+'Geta_(footwear)', W+'Z%C5%8Dri', W+'Kolhapuri_chappal', W+'Peshawari_chappal', W+'Jutti', W+'Paduka'
KLOMP, VAL, MUK, OPA, JIKA = W+'Klompen', W+'Valenki', W+'Mukluk', W+'Opanak', W+'Jika-tabi'
BAB, TRC = 'https://el-fenn.com/the-story-of-babouche/', 'https://www.trc-leiden.nl/trc-needles/individual-textiles-and-textile-types/footwear/girls-slippers-morocco'

def X(n, d, s, a='', mk='', y='', v=None, dt=''):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": v or [], "dt": dt}

kinds = [
 {"n": "Geta", "a": "raised wooden sandal", "d": "Japanese thonged sandal on a raised wooden base, usually standing on teeth.",
  "t": ["Two-tooth", "Three-tooth", "One-tooth", "Toothless", "Oval (women's)", "Rectangular (men's)"], "s": GETA,
  "x": [X("Two-tooth geta", "The everyday geta: flat wooden base on two teeth with a cloth thong.", GETA, a="ni-mai-ba geta",
          dt="paulownia (kiri) base · natural, stained or lacquered · hanao cotton, vinyl or leather · rubber or metal soles"),
        X("Ashida", "Tall geta for rain and wet streets.", GETA, a="rain geta", dt="tall teeth (about 18 cm pictured) · wooden base"),
        X("Tengu geta", "Very high geta on a single central tooth.", GETA, dt="single tooth · height about 20 cm"),
        X("Okobo", "Tall one-piece geta without teeth, worn by maiko; girls' pairs often red with a bell in the sole.", GETA,
          a="pokkuri · koppori", dt="one-piece block · plain or lacquered · red for girls"),
        X("Mitsu-ashi geta", "Tall lacquered three-legged geta worn by oiran in parades.", GETA, a="three-legged geta", dt="three teeth · lacquered")],
  "m": [["Koma-geta", ""], ["Takageta", ""]]},
 {"n": "Zōri", "a": "zori · setta", "d": "Flat-soled Japanese thonged sandal, the slip-on descendant of the waraji.",
  "t": ["White hanao (formal)", "Black hanao (informal)"], "s": ZORI,
  "x": [X("Wara-zōri", "Zōri woven from rice straw.", ZORI, a="straw zōri", dt="rice straw sole and straps"),
        X("Setta", "Men's zōri with a leather sole and woven upper of bamboo sheath or rush.", ZORI, dt="leather sole · takegawa or igusa cover"),
        X("Igusa zōri", "Casual zōri covered in woven rush, the tatami material.", ZORI, a="tatami omote", dt="rush cover · various soles"),
        X("Formal brocade or vinyl zōri", "Raised, covered zōri worn with formal kimono; brocade for weddings and funerals.", ZORI, dt="brocade or vinyl · white straps for formal wear"),
        X("Gomu zōri", "Rubber or elastomer zōri, often for bathrooms.", ZORI, a="rubber zōri", dt="rubber"),
        X("Shigure zōri", "Rain zōri with a toe cover.", ZORI, dt="toe cover · waterproof sole")]},
 {"n": "Jika-tabi", "a": "split-toe work boot · tabi boot", "d": "Japanese split-toe boot with a fabric upper and flexible rubber sole, reaching about mid-calf.",
  "t": ["Steel toe", "Knee-high all-rubber"], "s": JIKA,
  "x": [X("Rubber-soled jika-tabi", "Outdoor tabi with a rubber sole, credited to Tokujirō and Shōjirō Ishibashi, founders of Bridgestone.", JIKA, y="1922",
          dt="height ankle to mid-calf · cotton upper · hook fastening · steel-toe versions"),
        X("Tabi (Margiela)", "Designer split-toe shoe and boot launched on the Maison Margiela runway.", JIKA, mk="Maison Margiela", y="1988", dt="boot or flat · leather")]},
 {"n": "Kolhapuri chappal", "a": "Kolhapuris · Kolhapuri sandal", "d": "Hand-made braided leather slip-on sandal from Kolhapur, with a toe loop and no fastenings.",
  "t": ["House (light)", "Farm (heavy)"], "s": KOL,
  "x": [X("Kanwali", "Early thinner Kolhapuri with two side flaps.", KOL, a="chappal with ears", dt="side flaps · thin sole"),
        X("T-strap Kolhapuri", "Open-toe T-strap sandal with toe loop and foot loop, nailless and vegetable-tanned.", KOL,
          dt="buffalo hide · plain or hand-decorated · GI-tagged districts only"),
        X("Double-strap Kolhapuri", "Variant with two straps across the foot.", KOL, dt="leather")]},
 {"n": "Peshawari chappal", "a": "kheri · Peshawari kheri", "d": "Pakistani leather sandal with two crossing straps and a buckled heel strap, often on a tyre-rubber sole.",
  "t": ["Tyre sole", "Leather-on-rubber sole", "Embroidered (zari)"], "s": PESH,
  "x": [X("Peshawari kheri", "Classic semi-closed kheri refined in Peshawar after 1947.", PESH, dt="crossed straps · buckle heel strap · tyre or rubber sole"),
        X("Kaptaan chappal", "Later modern version of the kheri.", PESH, a="Captaan chappal", dt="leather"),
        X("Zari chappal", "Decorated kheri embroidered with gold or silver thread.", PESH, dt="metal-thread embroidery"),
        X("Chakwali chappal", "Kheri associated with Chakwal.", PESH),
        X("Kohati chappal", "Kheri associated with Kohat.", PESH)]},
 {"n": "Jutti", "a": "mojari · khussa", "d": "Embroidered flat leather slip-on of the Punjab, with no left or right and often an upturned toe.",
  "t": ["Men's (pointed nokh)", "Women's (backless)", "Rubber sole"], "s": JUT,
  "x": [X("Punjabi jutti", "Men's jutti with a sharp upward-curved tip (nokh) and heavy embroidery.", JUT, dt="leather · gold or silver thread embroidery · nokh toe"),
        X("Tilla jutti", "Metal-thread embroidered jutti associated with Patiala.", JUT, dt="tilla (metallic thread) work"),
        X("Mojari", "Name for the jutti in India outside Punjab.", JUT),
        X("Khussa", "Pakistani name for the closely related slip-on.", JUT),
        X("Jalsa jutti", "Plain, often blackish everyday jutti.", JUT, dt="plain leather")]},
 {"n": "Paduka", "a": "khadau · karrow · kharawan", "d": "Ancient Indian toe-knob sandal: a sole with a post gripped between the first two toes, no straps.",
  "t": ["Footprint-shaped", "Fish-shaped", "Hourglass"], "s": PAD,
  "x": [X("Wooden paduka", "Everyday wooden toe-knob sandal.", PAD, a="khadau", dt="teak, ebony or sandalwood · ivory or wire inlay"),
        X("Ceremonial paduka", "Silver, ivory or brass paduka for royalty, saints and ritual, sometimes with bells.", PAD, dt="silver, ivory, bronze, brass · bells · lotus knobs")]},
 {"n": "Babouche", "a": "baboosh · belgha · babouch", "d": "Heel-less leather slipper of Morocco and the former Ottoman world, open at the back.",
  "t": ["Plain", "Embroidered"], "s": BAB,
  "x": [X("Pointed (Arab) babouche", "Moroccan babouche with a pointed toe.", BAB, dt="cow, camel or goat hide · natural dyes"),
        X("Round-toe (Amazigh) babouche", "Moroccan babouche with a rounder Amazigh toe.", BAB, dt="leather · plain or decorated"),
        X("Embroidered babouch", "Leather slipper with hand cotton embroidery, for occasions such as Eid and weddings.", TRC, y="late 20th century", dt="leather · cotton embroidery")]},
 {"n": "Wooden clog (klomp)", "a": "klomp · klompen · Dutch clog", "d": "Whole-foot clog carved from a single block of wood, a Dutch national symbol.",
  "t": ["Plain", "Painted"], "s": KLOMP,
  "x": [X("Dutch klomp", "Whole-foot Dutch clog hollowed from willow or poplar; all-wood pairs are CE-marked as safety shoes.", KLOMP,
          dt="willow or poplar · hand- or machine-carved · plain or painted")]},
 {"n": "Valenki", "a": "Russian felt boot", "d": "Soleless Russian winter boot made of felted wool, often worn with galoshes.",
  "t": ["Brown", "Black", "Grey", "White", "Dyed"], "s": VAL,
  "x": [X("Unsoled valenki", "Traditional felt boot without an outer sole, worn with galoshes.", VAL, y="early 18th century", dt="felt · undyed colours"),
        X("Soled valenki", "Valenki fitted with a leather or rubber sole for wear.", VAL, dt="felt · leather or rubber sole")]},
 {"n": "Mukluk", "a": "kamik · kamak", "d": "Soft Arctic boot of sealskin or caribou skin, made by Inuit, Iñupiat and Yup'ik peoples.",
  "t": ["Summer", "Winter"], "s": MUK,
  "x": [X("Summer sealskin kamik", "Watertight boot with ringed seal upper and bearded seal sole, sinew blind-stitched.", MUK, dt="sealskin · sinew stitching"),
        X("Winter caribou kamik", "Insulated boot of caribou leg fur with fur lining.", MUK, dt="caribou leg fur · caribou, hare or fox lining")]},
 {"n": "Opanak", "a": "opanci · opinci · tsarvuli · opinki", "d": "Laceless leather peasant shoe of south-eastern Europe, now worn mostly with folk costume.",
  "t": ["Horn toe", "Curly toe", "Flat toe", "Sharp toe"], "s": OPA,
  "x": [X("Šumadija opanak", "Serbian opanak with a beak-like toe (s kljunom) or without (bez kljuna).", OPA, a="šumadijski opanak", dt="tanned leather · beak toe marks region"),
        X("Crveni opanci", "Western Serbian opanci of half-tanned oxhide dyed red with bark.", OPA, a="red opanci", dt="oxhide"),
        X("Tsarvuli", "Bulgarian opanak.", OPA, a="tsârvouli · opinki", dt="leather"),
        X("Tsarouhi", "Greek form of the opanak.", OPA),
        X("Točkaši", "Opanci made from old tyres after the Second World War.", OPA, dt="tyre rubber")]},
]

brands = [{"n": "Maison Margiela", "c": "France", "f": "1988", "seg": "Designer fashion",
           "d": "Paris fashion house founded by Martin Margiela; known for the split-toe Tabi.", "sig": ["Tabi (Margiela)"], "s": "knowledge"}]

G = "Footwear & leather"
traditions = [
 {"n": "Japanese geta and zōri making", "g": G, "r": "Japan", "p": "Heian period onwards; professional from the Edo period",
  "d": "Wooden geta and woven or covered zōri with replaceable hanao thongs.", "tech": "carving paulownia bases; weaving straw, rush or bamboo sheath; fitting hanao",
  "mat": "paulownia (kiri), rice straw, rush (igusa), bamboo sheath, cotton, brocade", "forms": ["Geta", "Zōri", "Okobo", "Setta"], "ctr": [],
  "auth": "hanao fitted through flaps in the sole and adjustable to the wearer", "s": ZORI},
 {"n": "Kolhapuri chappal craft", "g": G, "r": "Maharashtra and Karnataka, India", "p": "",
  "d": "Hand-made, nailless braided leather sandals protected by a geographical indication since 2019.",
  "tech": "vegetable tanning, skiving, hand cutting, stitching, punching and braiding", "mat": "buffalo hide, thread",
  "forms": ["Kolhapuri chappal", "Kanwali"], "ctr": ["Kolhapur", "Sangli", "Satara", "Solapur", "Belgavi", "Dharwad", "Bagalkot", "Bijapur"],
  "auth": "GI tag (July 2019): only pairs from the listed districts may be sold as Kolhapuri chappal", "s": KOL},
 {"n": "Peshawari chappal (kheri) craft", "g": G, "r": "Khyber Pakhtunkhwa and northern Punjab, Pakistan", "p": "colonial era; refined in Peshawar after 1947",
  "d": "Moulded leather sandal with crossed straps, regarded as Pakistan's national footwear.", "tech": "stretching uppers on a mould; tyre or rubber soling; zari embroidery",
  "mat": "leather, tyre rubber, gold or silver thread", "forms": ["Peshawari chappal", "Kaptaan chappal", "Zari chappal"],
  "ctr": ["Peshawar", "Hazro", "Chakwal", "Sargodha", "Dera Ismail Khan", "Talagang", "Kohat"], "auth": "", "s": PESH},
 {"n": "Punjabi jutti", "g": G, "r": "Punjab, India and Pakistan", "p": "",
  "d": "Embroidered leather slip-ons with straight lasts and upturned toes, worn at weddings and daily.", "tech": "hand embroidery, including gold and silver thread (tilla)",
  "mat": "leather, metallic thread", "forms": ["Jutti", "Mojari", "Khussa", "Tilla jutti"], "ctr": ["Amritsar", "Patiala"], "auth": "", "s": JUT},
 {"n": "Moroccan babouche making", "g": G, "r": "Morocco", "p": "",
  "d": "Heel-less leather slippers in pointed Arab and rounded Amazigh shapes, plain or embroidered.", "tech": "hand-stitching; natural dyes; embroidery",
  "mat": "cow, camel or goat hide; cotton embroidery thread", "forms": ["Babouche"], "ctr": ["Marrakech"], "auth": "hand-stitched, naturally dyed leather rather than factory-made", "s": BAB},
 {"n": "Dutch klompen making", "g": "Woodwork & furniture", "r": "Netherlands", "p": "",
  "d": "Whole-foot wooden clogs carved from willow or poplar blocks.", "tech": "splitting, rough shaping by hand or copying machine, hollowing, drying for weeks, sanding, painting",
  "mat": "willow, poplar", "forms": ["Wooden clog (klomp)"], "ctr": ["International Wooden Shoe Museum, Eelde"], "auth": "all-wood pairs carry the CE safety-shoe mark", "s": KLOMP},
 {"n": "Russian valenki felting", "g": "Textiles & rugs", "r": "Russia, Belarus, Ukraine", "p": "early 18th century onwards",
  "d": "Seamless felted wool winter boots.", "tech": "felting", "mat": "wool felt", "forms": ["Valenki"],
  "ctr": ["Semenov (Nizhny Novgorod)", "Kineshma (Kostroma)", "Kukmor (Kazan)"], "auth": "", "s": VAL},
 {"n": "Inuit and Yup'ik skin boots", "g": G, "r": "Arctic North America, Greenland", "p": "",
  "d": "Soft sealskin and caribou boots sewn by Arctic peoples.", "tech": "scraping, washing and drying skins; sinew blind-stitching for watertight seams",
  "mat": "ringed and bearded sealskin, caribou leg fur, fox and hare fur", "forms": ["Mukluk"], "ctr": [], "auth": "sinew-sewn seams; grain oriented for grip", "s": MUK},
 {"n": "Balkan opanci making", "g": G, "r": "Serbia, Croatia, Bosnia and Herzegovina, Bulgaria, North Macedonia, Romania, Albania, Greece", "p": "workshops by about 1900",
  "d": "Laceless leather peasant shoes whose toe shape marks the region.", "tech": "shaping hide on a wooden mould; bark dyeing; oputa lacing",
  "mat": "oxhide, pigskin, untanned or half-tanned hide", "forms": ["Opanak", "Tsarvuli", "Tsarouhi"], "ctr": ["Vrnjačka Banja"], "auth": "toe shape (beak, horn, curl) identifies the region", "s": OPA},
]

notes = ("Old Geta (k53) kept; its old models Tengu geta and Okobo became archetypes, Koma-geta and Takageta stay as old flat models (the retrieved page "
         "does not describe them, so no archetype). Added Peshawari chappal (moved from flat strap sandal per brief; sandal worker should not keep it), Jika-tabi "
         "(brief's cross-ref, now its own kind incl. Margiela Tabi) and Paduka: 12 kinds. Babouche sourced from el-fenn.com and TRC Leiden; the en-wiki "
         "'Babouche' page is a surname page and vikidia returned 403. Prince Albert slipper not here (evening slipper, Dress shoes shelf). Klomp variant names, "
         "geta production centres and makers not found on retrieved pages, so left out. Wikipedia API was rate-limited (429); pages fetched via WebFetch.")

out = {"kinds": kinds, "brands": brands, "traditions": traditions, "notes": notes}
p = 'work/A2/shelves/06_00.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('ok', len(kinds))
