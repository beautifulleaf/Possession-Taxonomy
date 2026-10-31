import json, os
WP = 'https://en.wikipedia.org/wiki/'
OK = WP + 'Oakeshott_typology'
def X(n, d, y, s, mk='', a='', v=None, dt=''):
    x = {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": v or []}
    if dt: x["dt"] = dt
    return x
def V(n, mk='', y='', d=''):
    return {"n": n, "mk": mk, "y": y, "d": d}
def M(*l): return [list(t) for t in l]
ALB = [["Museum Line", "Albion Swords"], ["Next Generation", "Albion Swords"], ["Squire Line", "Albion Swords"]]
kinds = [
 {"n": "Arming sword", "a": "knightly sword · one-handed sword", "d": "One-handed straight double-edged sword with a cross guard, the typical medieval knight's sword.",
  "s": "https://www.kultofathena.com/product-category/swords/arming-swords/",
  "x": [
   X("Oakeshott Type XII", "Tapering blade with a shortened fuller, better for the thrust; the classic crusade-era sword.", "13th c.", OK,
     v=[V("Sword of Saint Maurice", "", "13th c.", "original in Turin; brazil-nut pommel"), V("Sword of Saint Maurice replica", "Peter Johnsson", "2005", "reproduction"), V("Cawood sword", "", "", "original")],
     dt="blade c. 75–80 cm · pommel type · fuller length"),
   X("Oakeshott Type X", "Broad flat blade with a wide shallow fuller and rounded point; the Norman sword.", "late Viking age to 13th c.", OK, a="Norman sword", v=[V("Type Xa", "", "", "narrower fuller")]),
   X("Oakeshott Type XI", "Longer slender blade with an acute point and narrow fuller, made for slashing.", "c. 1100–1175", OK, v=[V("Type XIa", "", "", "broader, shorter blade")]),
   X("Oakeshott Type XIIIb", "Smaller single-handed form of the wide parallel-edged Type XIII blade.", "c. 1300", OK,
     v=[V("Tritonia sword", "", "c. 1300", "original, Museum of Medieval Stockholm; spherical pommel")]),
   X("Oakeshott Type XIV", "Short, broad, strongly tapering triangular blade with a flat section.", "c. 1270 – early 14th c.", OK,
     v=[V("Swordier Upgraded Type XIV Arming Sword", "Swordier", "", "reproduction")]),
   X("Oakeshott Type XV", "Straight tapering blade of diamond section with a sharp point, made to thrust against armour.", "14th–15th c.", OK,
     v=[V("Castillon sword", "", "", "Type XV original"), V("Deepeeka Castillon Arming Sword", "Deepeeka", "", "reproduction")]),
   X("Oakeshott Type XVI", "Flat blade with a clear ridge tapering to an acute point, 70–80 cm.", "14th–15th c.", OK),
   X("Oakeshott Type XVIII", "Tapering blade with a broad base, diamond section and short grip.", "14th–15th c.", OK),
  ],
  "m": M(["Knight Templar Arming Sword", "Balaur Arms"], ["Man At Arms Arming Sword", "Cold Steel"], ["Squire Sword", "Darksword Armory"],
         ["Comte de Nieuwekerke Sword", "Deepeeka"], ["Irish Gaelic Arming Sword", "Deepeeka"], ["Korsoygaden Viking Sword", "Deepeeka"], ["Militia Templi Sword", "Deepeeka"],
         ["Knights Sword", "Kingston Arms"], ["Guardian Arming Sword", "Krieger Armory"], ["HEMA Arming Sword A2", "Krieger Armory"],
         ["Richard Norman Sword", "VB Swordshop"], ["Crusader Mark II", "Valiant Armoury"]),
  "r": ALB},
 {"n": "Longsword", "a": "bastard sword · hand-and-a-half sword · war sword", "d": "Straight double-edged sword with a grip long enough for one or two hands, c. 1350–1550.",
  "s": WP + "Longsword",
  "x": [
   X("Oakeshott Type XVIIIa", "Narrow tapering diamond-section blade with a long grip; a reference late-medieval longsword.", "c. 1450–1480", OK,
     v=[V("Munich sword (XVIIIa.5)", "", "c. 1450–1480", "original, Bayerisches Nationalmuseum"), V("Albion Munich", "Albion Swords", "", "Next Generation line, after the Munich original")]),
   X("Oakeshott Type XVIa", "Classic longsword balancing cut and thrust: long blade, shorter fuller, extended grip.", "14th–15th c.", OK),
   X("Oakeshott Type XIIIa", "Long wide parallel-edged blade with a long grip; the knightly great or war sword.", "12th–15th c., mainly 14th c.", OK, a="great sword · war sword"),
   X("Oakeshott Type XIIa", "Longer, more massive two-handed version of Type XII.", "mid-13th c.", OK),
   X("Oakeshott Type XVa", "Slender, strongly tapered two-hander built for thrusting against plate.", "14th–15th c.", OK),
   X("Oakeshott Type XVII", "Long evenly tapering blade of hexagonal section with a two-handed grip.", "c. 1360–1420", OK,
     v=[V("Fitzwilliam Museum sword", "", "", "original, Cambridge")]),
   X("Oakeshott Type XVIIIb", "Bastard sword with a longer diamond-section blade and long grip.", "c. 1450–1520", OK, v=[V("Type XVIIIc", "", "", "shorter grip, broad blade c. 90 cm"), V("Type XVIIIe", "", "", "long narrow blade, extended ricasso")]),
   X("Oakeshott Type XX", "Nearly parallel hand-and-a-half or two-handed blade with two or three fullers.", "14th–15th c.", OK, v=[V("Type XXa", "", "", "narrower, more acute blade")]),
  ],
  "m": M(["Sword of Bannockburn", "Darksword Armory"], ["Vindaaris", "Darksword Armory"], ["Black Knight Longsword", "Deepeeka"], ["Practical Bastard Sword", "Kingston Arms"],
         ["Dragonwhisper Longsword", "Romance of Men"], ["Ranger's Oath Longsword", "Swordier"], ["Templar Knight Longsword", "Swordier"],
         ["Cedric Longsword", "VB Swordshop"], ["Ivanhoe Longsword", "VB Swordshop"]),
  "r": ALB},
 {"n": "Greatsword", "a": "two-handed sword · two-hander", "d": "Very large straight double-edged sword used with both hands, the last stage of the large-sword trend.",
  "s": "https://www.kultofathena.com/product-category/swords/longswords/",
  "x": [
   X("Zweihänder", "Huge two-handed sword of the Landsknechte with a long ricasso, often parrying hooks and side rings.", "16th c.", WP + "Zweih%C3%A4nder",
     a="Doppelhänder · Bidenhänder · Bihänder", v=[V("Flammenschwert", "", "16th c.", "wavy blade"), V("Feder", "", "", "modern training version")],
     dt="blade up to c. 2 m · parrying hooks · side rings · straight or wavy blade"),
   X("Two-handed claymore", "Scottish two-hander with forward-angled quillons ending in quatrefoils, wheel pommel and langets.", "c. 1400–1700", WP + "Claymore",
     a="claidheamh-mòr", v=[V("Clamshell-hilted claymore", "", "", "large round guards protecting the grip")]),
  ],
  "m": M(["Scottish Lowlander Greatsword", "Kingston Arms"])},
 {"n": "Viking sword", "a": "Carolingian sword · Viking Age sword", "d": "Early-medieval one-handed double-edged sword of the 8th–11th centuries, classified by hilt (Petersen types).",
  "s": WP + "Viking_sword",
  "x": [
   X("Ulfberht sword", "Frankish blade inlaid with the name +VLFBERH+T; about 170 known, of very uneven quality.", "9th–11th c.", WP + "Ulfberht_swords",
     v=[V("+VLFBERH+T inscription", "", "", "commonest class"), V("+VLFBERHT+ inscription", "", "", "second class")]),
   X("Petersen Type C", "Petersen hilt type of the 9th century.", "9th c.", WP + "Viking_sword", v=[V("Sæbø sword", "", "9th c.", "original, Norway")]),
   X("Petersen Type L", "Petersen hilt type; a variant is Evison's Wallingford Bridge type.", "10th c.", WP + "Viking_sword", v=[V("Lincoln sword (River Witham)", "", "10th c.", "original; blade inscribed Leutfrit")]),
   X("Petersen Type T", "Petersen hilt type of the 10th century.", "10th c.", WP + "Viking_sword", v=[V("Sword of Saint Stephen", "", "10th c.", "original, St Vitus Cathedral, Prague; walrus-tooth hilt")]),
  ],
  "dt": ""},
 {"n": "Short sword", "a": "gladius · xiphos · shortsword", "d": "Straight double-edged one-handed sword with a blade clearly shorter than an arming sword, often without a cross guard.",
  "s": "https://www.kultofathena.com/product-category/swords/",
  "x": [
   X("Gladius", "Roman legionary short sword for cut and thrust.", "c. 216 BC – 1st c. AD", WP + "Gladius",
     v=[V("Gladius Hispaniensis", "", "c. 216–20 BC", "longest, leaf-shaped blade 60–68 cm"), V("Mainz gladius", "", "early Empire", "waisted blade 50–55 cm, long triangular point"),
        V("Fulham gladius", "", "after 43 AD", "straight edges, long triangular point"), V("Pompeii gladius", "", "1st c. AD", "parallel edges, short triangular tip; most popular")]),
   X("Xiphos", "Greek leaf-shaped double-edged short sword, a secondary weapon behind spear and javelin.", "Iron Age Greece", WP + "Xiphos", dt="blade c. 45–60 cm; Spartan blades c. 30 cm"),
  ]},
 {"n": "Falchion", "a": "messer · grosse messer · langes messer", "d": "Broad single-edged one-handed European sword, straight or slightly curved, often widening towards the point.",
  "s": WP + "Falchion",
  "x": [
   X("Cleaver falchion", "Thin, light falchion with a cleaver-like profile.", "13th–14th c.", WP + "Falchion", v=[V("Conyers falchion", "", "", "original; best-known survivor")]),
   X("Cusped falchion", "Falchion with a cusped, clipped tip like a großes Messer.", "13th–16th c.", WP + "Falchion", v=[V("Thorpe falchion", "", "13th c.", "original, England; straight blade")]),
   X("Messer", "Single-edged sword with a knife-like slab-tang hilt, wooden grip plates and a Nagel nail guard.", "15th–16th c.", WP + "Messer_(sword)",
     a="langes Messer · großes Messer", v=[V("Langes Messer", "", "15th–16th c.", "one-handed self-defence sword"), V("Großes Messer", "", "15th–16th c.", "larger, sometimes with a longer grip"), V("Kriegsmesser", "", "15th–16th c.", "two-handed military form")]),
  ]},
 {"n": "Sabre", "a": "saber · szabla", "d": "Single-edged, usually curved cavalry sword; national and regional patterns are sold under their own names.",
  "s": "https://www.kultofathena.com/product-category/swords/sabres/",
  "x": [
   X("Hungarian sabre", "Early curved szabla of Hungary that gave the Western term.", "14th c.", WP + "Sabre"),
   X("Polish szabla", "Curved sabre of the Polish–Lithuanian Commonwealth.", "16th–18th c.", WP + "Sabre",
     v=[V("Polish cavalry sabre (17th century)", "", "17th c.", "Hussar"), V("Karabela", "", "late 17th c.", "szlachta nobility")]),
   X("1796 Pattern Light Cavalry Sabre", "British cavalry sabre with a widening curved blade and asymmetric point, designed by John Le Marchant with Henry Osborn.", "1796–1821", WP + "Pattern_1796_light_cavalry_sabre",
     v=[V("Prussian 1811 pattern (Blücher sabre)", "", "1811", "copy")]),
   X("Mameluke sword", "Scimitar-style sabre with Turkish kilij influence.", "1805 onward", WP + "Sabre", v=[V("1831 pattern British generals' sword", "", "1831", ""), V("US Marine Corps officers' sword", "", "", "still in use")]),
   X("Shashka", "Guardless Caucasian single-edged sabre, adopted by Cossacks and the Russian army.", "17th c. onward", WP + "Shashka",
     v=[V("Shashka M1881", "", "1881", "Cossack version without guard; dragoon version with knuckle-bow"), V("1927 pattern", "", "1927–1946", "Soviet")]),
   X("Model 1913 cavalry saber", "Straight thrust-centred US cavalry sword, known as the Patton saber.", "1913–1934", WP + "Sabre", a="Patton saber"),
  ],
  "m": M(["Light Dueling Saber", "Regenyei"], ["Tournament Saber", "Regenyei"], ["Honshu Boshin Saber", "United Cutlery"], ["Steppe Wind Ultralight Nomad Saber", "VB Swordshop"],
         ["Texas Dragoons Saber", "Windlass Steelcrafts"], ["British 1897 pattern infantry officer sword", ""], ["Dussack", ""], ["Mongolian sabre (Yuan)", ""], ["US Marine Corps NCO sword", ""])},
 {"n": "Cutlass", "a": "", "d": "Short, broad single-edged sword with a basket or cup guard, used at sea.",
  "s": "https://www.kultofathena.com/product-category/swords/cutlasses/",
  "x": [X("US Navy M1917 cutlass", "Last cutlass model adopted by the US Navy, based on the Dutch klewang.", "1917", WP + "Cutlass", v=[V("M1941", "", "1941", "slightly modified variant")])],
  "m": M(["Tactical Cutlass", "APOC"], ["Naval Cutlass", "Condor Tool & Knife"], ["Anix Cutlass", "Deepeeka"], ["Shell Guard Cutlass", "Kingston Arms"], ["Battlecry! Cutlass", "Windlass Steelcrafts"],
         ["Heritage Series Pirate Cutlass", "Windlass Steelcrafts"], ["Naval cutlass 1860 pattern", ""], ["Royal Navy 1804 pattern boarding cutlass", ""])},
 {"n": "Basket-hilted broadsword", "a": "broadsword · basket-hilted sword · backsword", "d": "Cut-and-thrust sword whose basket-shaped guard encloses the hand, 16th–18th centuries.",
  "s": WP + "Basket-hilted_sword", "t": ["broadsword (double-edged)", "backsword (single-edged)"],
  "x": [
   X("Scottish basket-hilted broadsword", "Highland basket-hilted sword of the Jacobite risings, often called a claymore.", "late 17th–18th c.", WP + "Basket-hilted_sword", a="claymore · claidheamh mòr"),
   X("Schiavona", "Venetian basket-hilted sword with a cat's-head pommel and leaf-shaped guard bars.", "16th–17th c.", WP + "Schiavona"),
   X("Mortuary sword", "English half-basket-hilted sword, some hilts bearing a face.", "c. 1625–1670", WP + "Basket-hilted_sword"),
   X("Walloon sword", "Half-basket sword with double shell guard and thumb-ring.", "17th c.", WP + "Basket-hilted_sword"),
   X("Sinclair hilt", "Scandinavian basket-hilted sword resembling Highland swords.", "17th–18th c.", WP + "Basket-hilted_sword"),
  ]},
 {"n": "Estoc", "a": "tuck", "d": "Long stiff thrusting sword with a sharp point and no real edge, made to pierce mail and plate.",
  "s": WP + "Estoc", "t": ["two-handed", "one-handed"],
  "x": [X("Boar sword", "Hunting estoc with a spear-shaped point and cross-bar to stop over-penetration.", "c. 1500", WP + "Estoc", a="boar-spear sword")]},
 {"n": "Rapier", "a": "", "d": "Long, slender sword with a complex hilt made mainly for the thrust.",
  "s": "https://www.kultofathena.com/product-category/swords/rapiers/",
  "x": [
   X("Side-sword", "Italian Renaissance cut-and-thrust ancestor of the rapier with a broader blade.", "16th c.", WP + "Side-sword", a="spada da lato"),
   X("Swept-hilt rapier", "Rapier with an open swept hilt, an Italian fashion.", "16th–17th c.", WP + "Rapier",
     v=[V("Swept Hilt Rapier", "Kingston Arms", "", "reproduction"), V("Vincentio Seven Ring Hilt Rapier", "LK Chen", "", "reproduction")]),
   X("Pappenheimer", "German rapier hilt form.", "17th c.", WP + "Rapier", a="Pappenheim-hilt rapier", v=[V("Pappenheimer rapier", "", "", "")]),
   X("Cup-hilt rapier", "Spanish rapier whose guard is a deep metal cup.", "early 1600s on", WP + "Rapier",
     v=[V("Tizona (17th century Spanish cup-hilt rapier)", "", "17th c.", ""), V("Cup Hilt Rapier", "VB Swordshop", "", "reproduction")]),
   X("War rapier", "Rapier hilt on a wider military blade.", "16th–17th c.", WP + "Rapier", v=[V("Sword of Gustavus Adolphus", "", "17th c.", "typical example")]),
  ],
  "m": M(["Duelist's Pierced Shell Hilt Rapier", "Baltimore Knife & Sword"], ["Cavalier Rapier", "Cold Steel"], ["Crown Basket Hilt Rapier", "Deepeeka"], ["Flamberge Rapier", "Deepeeka"],
         ["Saxony German Rapier", "LK Chen"], ["Brandenburg Rapier", "Windlass Steelcrafts"], ["Christus Imperat Rapier", "Windlass Steelcrafts"], ["Deschaux Rapier", "Windlass Steelcrafts"], ["Musketeer Rapier", "Windlass Steelcrafts"])},
 {"n": "Smallsword", "a": "small sword · court sword · claybeg · épée de cour", "d": "Light one-handed thrusting sword with a small shell guard, worn daily in the 18th century.",
  "s": WP + "Small_sword", "t": ["triangular hollow-ground blade", "colichemarde blade", "ceremonial cross-hilt"],
  "m": M(["Small Sword", "Cold Steel"])},
]
for k in kinds:
    k.pop("dt", None)
brands = [
 {"n": "Albion Swords", "c": "United States", "f": "1998", "seg": "Specialist", "kf": "European sword replicas", "d": "Wisconsin maker of European sword replicas, formerly Albion Armorers.",
  "lines": ["Museum Line", "Next Generation", "Squire Line", "Maestro Line"], "s": WP + "Albion_Swords"},
 {"n": "Windlass Steelcrafts", "c": "India", "seg": "Mainstream", "kf": "replica swords", "d": "Dehradun sword maker, owner of Museum Replicas Ltd.", "rel": ["Museum Replicas Ltd"], "s": WP + "Museum_Replicas_Ltd"},
 {"n": "Cold Steel", "c": "United States", "seg": "Mainstream", "kf": "knives and swords", "d": "American marketer of knives, swords and edged tools.", "s": "knowledge"},
 {"n": "Deepeeka", "c": "India", "seg": "Value", "kf": "replica swords and armour", "d": "Indian maker of replica swords and armour.", "s": "knowledge"},
 {"n": "Darksword Armory", "c": "Canada", "seg": "Specialist", "kf": "medieval swords", "d": "Canadian maker of functional medieval sword replicas.", "s": "knowledge"},
]
out = {"kinds": kinds, "brands": brands, "traditions": [],
 "notes": "All 9 old kinds kept; added Viking sword, Basket-hilted broadsword and Estoc. Oakeshott types as archetypes for Arming sword and Longsword (from Wikipedia Oakeshott typology); Petersen types and Ulfberht for Viking sword. Old typed models (Oakeshott XIV/XV/XII/XVI/XVIII, 1796, Hungarian, Polish, Shashka M1881, Pappenheimer, Tizona) folded into archetypes; replica SKUs kept as versions where they match an archetype, the rest in m with brand prefix removed. Arms & Armor, Regenyei-as-maker of named types, Kingston Arms and others not added as brands (no retrieved page). No sabre archetype for 1897 infantry, Dussack, Mongolian, USMC NCO (kept as m: not described on fetched pages). Pappenheimer Wikipedia page 404; cited Rapier article."}
p = '/home/user/Possession-Taxonomy/rebuild/work/E4/shelves/00_00.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('written')
