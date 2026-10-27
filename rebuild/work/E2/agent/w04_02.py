import json, os
def w(job, obj):
    p = f'/home/user/Possession-Taxonomy/rebuild/work/E2/shelves/{job}.json'
    t = p + '.tmp'; json.dump(obj, open(t, 'w'), ensure_ascii=False, indent=1); os.replace(t, p)
def V(n, mk, y="", d=""):
    v = {"n": n, "mk": mk}
    if y: v["y"] = y
    if d: v["d"] = d
    return v
GN = "Gray-Nicolls"; GM = "Gunn & Moore"; KB = "Kookaburra"; SS = "SS"; SG = "SG"; DK = "Dukes"; DF = "Duncan Fearnley"
NB = "New Balance"; MA = "Masuri"; PU = "PUMA"; SZ = "Slazenger"; SU = "Stuart Surridge"; NW = "Newbery"; MO = "Mongoose"
BATW = "https://en.wikipedia.org/wiki/Cricket_bat"
BALLW = "https://en.wikipedia.org/wiki/Cricket_ball"
GNW = "https://en.wikipedia.org/wiki/Gray-Nicolls"
GMW = "https://en.wikipedia.org/wiki/Gunn_%26_Moore"
KBW = "https://en.wikipedia.org/wiki/Kookaburra_Sport"
SGW = "https://en.wikipedia.org/wiki/Sanspareils_Greenlands"
SSW = "https://en.wikipedia.org/wiki/Sareen_Sports_Industries"
DKW = "https://en.wikipedia.org/wiki/British_Cricket_Balls_Ltd"
KIT = "https://www.cricket.com.au/news/3314762/kit-week-greatest-ever-aussies-and-their-bats"
WIS = "https://www.wisden.com/cricket-news/gear-of-the-year-cricket-equipment-showcase-2019-part-two"
OWZ = "https://www.owzat-cricket.co.uk/blog/top-cricket-helmets-for-2025-protect-your-head-in-style"
TCR = "https://www.thecricketer.com/topics/grassroots/owzatcricket_end_of_season_kit_tips.html"
ART = "https://gray-nicolls.co.uk/blogs/the-game/the-art-of-batmaking"
ESX = "https://www.essexgardenstrust.org.uk/exotic-incomers"
OLD = "https://www.kingsgrovesports.com.au/cricket/accessories.html"

bat = {"n": "Cricket bat", "a": "", "d": "Flat-faced willow bat with a spliced cane handle, made to the size limits of the Laws of Cricket.",
 "t": ["English willow (retailer grades 1–4)", "Kashmir willow", "short handle", "long handle", "junior sizes"],
 "s": "https://kookaburrasport.co.uk/turf-cricket-ball",
 "x": [
  {"n": "Scoop", "a": "GN100 Scoop", "d": "Gray-Nicolls bat with wood scooped from the back centre, often named cricket's most famous bat.", "mk": GN, "y": "1974", "s": BATW,
   "v": [V("GN100 Scoop", GN, "1974", "original; used by Greg Chappell"), V("Scoop re-release", GN, "2012", "reissued for the English season"),
         V("Powerscoop", GN, "", "current range")],
   "dt": "weight · handle length · willow grade"},
  {"n": "Kahuna", "a": "", "d": "Kookaburra bat associated with Ricky Ponting through his prime years.", "mk": KB, "s": KIT,
   "v": [V("Kahuna", KB, "", "Ponting's bat at the 2003 World Cup and the 2005 and 2006–07 Ashes"),
         V("Kahuna Pro", KB, "2019", "developed with Ricky Ponting")],
   "dt": "weight · handle length · willow grade"},
  {"n": "Diamond", "a": "", "d": "Gunn & Moore's leading bat range, used by Ben Stokes.", "mk": GM, "s": WIS,
   "v": [V("Diamond Original LE", GM, "2019", "as used by Ben Stokes")], "dt": "weight · handle length · willow grade"},
  {"n": "Sunridges", "a": "", "d": "SS's best-known bat line from Meerut.", "mk": SS, "y": "1976", "s": SSW, "v": [], "dt": "English or Kashmir willow"},
  {"n": "Magnum", "a": "", "d": "Duncan Fearnley bat used by Allan Border from 1985.", "mk": DF, "y": "1985", "s": KIT, "v": [], "dt": "weight · willow grade"},
  {"n": "Turbo", "a": "", "d": "Stuart Surridge bat made from two pieces of willow; Graham Gooch made 333 with one in 1990.", "mk": SU, "y": "1980s", "s": BATW, "v": [], "dt": "weight"},
  {"n": "V100", "a": "", "d": "Slazenger bat used by Mark Waugh from 1991 and later by Steve Smith.", "mk": SZ, "y": "1991", "s": KIT,
   "v": [V("V800", SZ, "1999", "Mark Waugh from the 1999 World Cup"), V("V900", SZ, "", "Michael Clarke's Test debut bat")], "dt": "weight · willow grade"},
  {"n": "Ridgeback", "a": "Ridge Back", "d": "Kookaburra bat used by Dean Jones, Adam Gilchrist and Ricky Ponting in the 1990s.", "mk": KB, "y": "1990s", "s": KIT, "v": [], "dt": "weight"},
  {"n": "Kaboom", "a": "", "d": "Gray-Nicolls bat used by David Warner from around 2008.", "mk": GN, "y": "2008", "s": KIT, "v": [], "dt": "weight · willow grade"},
  {"n": "Uzi", "a": "", "d": "Newbery Twenty20 bat with a truncated blade and longer handle.", "mk": NW, "y": "2004", "s": BATW, "v": [], "dt": "weight"},
  {"n": "Mi3", "a": "", "d": "Mongoose Twenty20 bat with a blade about a third shorter and a handle about 43% longer.", "mk": MO, "y": "2009", "s": BATW, "v": [], "dt": "weight"}],
 "m": [["Classic", GN], ["Gem", GN], ["Neocore", GN], ["Revel", GN], ["Stratos", GN], ["Ventus", GN], ["Havoc", GN], ["Legend", GN],
       ["Icon SE", GM], ["Noir Original LE", GM], ["Ghost 7.1", KB], ["Prism 9.1", KB], ["Ikon", "SS TON"], ["Magnum", "SS TON"],
       ["DC 1080", NB], ["DC 1280", NB], ["TC 1260", NB], ["Heritage", NB], ["Super Tusker", "Symonds"]],
 "r": [["Ghost", KB], ["Glare", KB], ["Nickel", KB], ["Prism", KB], ["Rapid", KB]]}

ball = {"n": "Cricket ball", "a": "", "d": "Hard, leather-covered cork-core ball with a raised seam, made for cricket.",
 "t": ["red", "white", "pink", "four-piece (hand-stitched)", "two-piece", "men's 156–163 g", "women's and junior (lighter)"],
 "s": "https://kookaburrasport.co.uk/turf-cricket-ball",
 "x": [
  {"n": "Dukes", "a": "Duke ball", "d": "Hand-stitched English ball with a six-row seam, used in Tests in England, Ireland and the West Indies.", "mk": DK, "y": "1760", "s": DKW,
   "v": [V("first six-seam ball", DK, "1780"), V("triple-sewn ball", DK, "1851", "prize medal at the Great Exhibition"),
         V("white Dukes", DK, "1999", "for the 1999 World Cup")],
   "dt": "red, pink or white · Alumtine finish"},
  {"n": "Kookaburra Turf", "a": "Turf", "d": "Australian ball with machine-stitched outer seams, used in most Test nations and all white-ball internationals.", "mk": KB, "s": KBW,
   "v": [V("red Turf", KB, "", "Tests in Australia, New Zealand and elsewhere"), V("white Turf", KB, "", "ODIs and T20 internationals"), V("pink Turf", KB, "", "day/night Tests")],
   "dt": "red, white or pink · weight grade"},
  {"n": "SG Test", "a": "", "d": "Hand-stitched Indian ball with a prominent seam, used in all Tests in India since 1994.", "mk": SG, "y": "1994", "s": SGW, "v": [], "dt": "red or pink"}],
 "m": [["Supreme Crown", KB], ["Super Coach Technique Soft", KB]]}

pads = {"n": "Cricket batting pads", "a": "leg guards", "d": "Leg guards worn by a cricket batter.", "t": ["traditional cane", "lightweight foam", "ambidextrous"], "s": OLD,
 "m": [["Kahuna Pro", KB], ["Diamond", GM], ["TC860", NB]]}
gloves = {"n": "Cricket batting gloves", "a": "", "d": "Padded gloves worn by a cricket batter.", "t": ["sausage finger", "split finger"], "s": OLD,
 "m": [["Select 600", GN], ["Diamond Original", GM], ["Kahuna Pro", KB]]}
helmet = {"n": "Cricket helmet", "a": "", "d": "Helmet with face grille made for cricket batting and close fielding; current UK standard BS 7928:2013.",
 "t": ["steel grille", "titanium grille", "with neck guard"], "s": OLD,
 "m": [["VS Elite Titanium", MA], ["OS2 Test", MA], ["T-LINE Steel", MA], ["T-LINE Plus", MA], ["Atomic 360", GN], ["Pro 600f", KB]]}
wk = {"n": "Wicket-keeping gloves", "a": "keeping gloves", "d": "Webbed padded gloves worn by a cricket wicket-keeper.", "s": OLD,
 "m": [["2000L", KB], ["Shockwave 2000", GN], ["Original LE", GM], ["evo SE", PU]]}
stumps = {"n": "Cricket stumps", "a": "wicket set", "d": "Set of stumps and bails, fixed or on a base, made for cricket.", "t": ["wooden (in-ground)", "spring-back on a base"], "s": OLD}

brands = [
 {"n": GN, "c": "United Kingdom", "f": "1855", "seg": "Heritage manufactory", "kf": "cricket bats", "d": "English bat maker in Robertsbridge, East Sussex, formed by merging H.J. Gray and Sons with L.J. Nicolls; owned by Grays International.",
  "sig": ["Scoop", "Kaboom"], "rel": [GM, KB], "s": GNW},
 {"n": GM, "c": "United Kingdom", "f": "1885", "seg": "Heritage manufactory", "kf": "cricket bats", "d": "Nottingham bat maker founded by William Gunn and Thomas James Moore; part of the Unicorn Group since 1968.",
  "sig": ["Diamond"], "rel": [GN], "s": GMW},
 {"n": KB, "c": "Australia", "f": "1890", "seg": "Professional & flagship", "kf": "cricket balls, bats", "d": "Melbourne maker whose Turf ball is used in most Test nations; bats since the mid-1980s.",
  "sig": ["Kookaburra Turf", "Kahuna", "Ridgeback"], "rel": [DK, SG], "s": KBW},
 {"n": DK, "c": "United Kingdom", "f": "1760", "seg": "Heritage manufactory", "kf": "cricket balls", "d": "Hand-stitched cricket ball begun by the Duke family at Penshurst, Kent; made by British Cricket Balls Ltd, owned by Dilip Jajodia since 1987.",
  "sig": ["Dukes"], "rel": [KB, SG], "s": DKW},
 {"n": SG, "c": "India", "f": "1931", "seg": "Professional & flagship", "kf": "Test balls", "d": "Sanspareils Greenlands: Meerut maker, founded in Sialkot, whose ball is used in all Tests in India; Featherlite protective gear since 1972.",
  "sig": ["SG Test"], "rel": [SS, KB], "s": SGW},
 {"n": SS, "c": "India", "f": "1969", "seg": "Mainstream", "kf": "cricket bats", "d": "Sareen Sports Industries, Meerut bat maker founded by N.K. Sareen; TON is its top bat label.", "lines": ["TON"],
  "sig": ["Sunridges"], "rel": [SG], "s": SSW},
 {"n": DF, "c": "United Kingdom", "seg": "Heritage manufactory", "kf": "cricket bats", "d": "English cricket bat maker whose Magnum was used by Allan Border.", "sig": ["Magnum"], "s": "knowledge"},
 {"n": SU, "c": "United Kingdom", "seg": "Heritage manufactory", "kf": "cricket bats", "d": "English bat maker; Percy Stuart Surridge developed a reinforced toe in 1900.", "sig": ["Turbo"], "s": BATW},
 {"n": NW, "c": "United Kingdom", "seg": "Specialist", "kf": "T20 bats, carbon handles", "d": "Bat maker behind the Uzi Twenty20 bat and the C6 carbon handle.", "sig": ["Uzi"], "s": BATW},
 {"n": MO, "seg": "Specialist", "kf": "T20 bats", "d": "Maker of the Mi3 short-blade, long-handle Twenty20 bat.", "sig": ["Mi3"], "s": BATW},
 {"n": MA, "c": "United Kingdom", "seg": "Professional & flagship", "kf": "cricket helmets", "d": "British cricket helmet specialist whose Vision and Original series are widely worn by Test players.", "s": "knowledge"},
 {"n": NB, "c": "United States", "f": "1906", "seg": "Mainstream", "kf": "athletic shoes, cricket kit", "d": "Boston athletic footwear and apparel brand with a cricket bat and kit line.", "s": "knowledge"},
 {"n": PU, "c": "Germany", "f": "1948", "seg": "Mainstream", "kf": "athletic shoes", "d": "Herzogenaurach sportswear brand.", "s": "knowledge"},
]

trad = [{"n": "English willow bat-making", "g": "Woodwork & sports craft", "r": "England (willow from Essex and East Anglia; workshops in Sussex and Nottingham)", "p": "17th century–present",
 "d": "Making cricket bats from cleft English cricket bat willow, pressed and hand-finished.",
 "tech": "butt cut to length and split into clefts · dried · pressed · cane handle spliced in · hand shaped, balanced and polished",
 "mat": "cricket bat willow (Salix alba var. caerulea), cane handle",
 "forms": ["Cricket bat"], "ctr": ["J S Wright (Great Leighs, Essex; willow supplier)", "Gray-Nicolls (Robertsbridge)", "Gunn & Moore (Nottingham)"],
 "auth": "Straight, even grains (about 8–12 visible) on the face; English and Kashmir willow are the same species, so origin cannot be told reliably from the wood.",
 "s": ART}]

w('04_02', {"kinds": [bat, ball, pads, gloves, helmet, wk, stumps], "brands": brands, "traditions": trad,
 "notes": "All 7 kinds kept. Bat: 12 flat models + 6 ranges became 11 archetypes (Scoop, Kahuna, Diamond, Sunridges, Magnum, Turbo, V100, Ridgeback, Kaboom, Uzi, Mi3) with 19 flat models and 5 Kookaburra ranges kept; willow type and handle length as t. Ball: archetypes Dukes, Kookaburra Turf, SG Test with colours as t. Protective kit tier models from Wisden Gear of the Year 2019, Owzat 2025 helmet guide and The Cricketer kit tips. Slazenger is registered in shelf 02_00. Shrey helmets and New Balance DC 580 pads left out: no retrieved page. Symonds kept only as a flat model maker (no register entry). Masuri company page blocked (403, Firecrawl failed); registered from knowledge."})
