import json, os
def w(job, obj):
    p = f'/home/user/Possession-Taxonomy/rebuild/work/E2/shelves/{job}.json'
    t = p + '.tmp'; json.dump(obj, open(t, 'w'), ensure_ascii=False, indent=1); os.replace(t, p)
def V(n, mk, y="", d=""):
    v = {"n": n, "mk": mk}
    if y: v["y"] = y
    if d: v["d"] = d
    return v
SP = "Spalding"; WI = "Wilson Sporting Goods"; MI = "Mikasa"; SE = "Select"; STX = "STX"; BR = "Brine"
BB = "https://en.wikipedia.org/wiki/Basketball_(ball)"
EVO = "https://www.hoopsbeast.com/?p=1506"
HOOP = "https://www.hoopsbeast.com/?p=3065"
VB = "https://en.wikipedia.org/wiki/Volleyball_(ball)"
NB = "https://en.wikipedia.org/wiki/Netball"
HB = "https://abargenteuil.fr/blog/ballon-handball-select-ultimate-taille-3/"
LS = "https://en.wikipedia.org/wiki/Lacrosse_stick"
LX = "https://laxallstars.com/articles/top-25-lacrosse-heads"
HU = "https://en.wikipedia.org/wiki/Hurley_(stick)"
HG = "https://en.wikipedia.org/wiki/Hurling"

basketball = {"n": "Basketball", "a": "", "d": "Inflated ball with a pebbled cover made for basketball; size 7 men's, size 6 women's, smaller for youth.",
 "t": ["indoor leather or composite", "outdoor rubber", "size 7 / 6 / 5", "3x3 ball"], "s": BB,
 "x": [
  {"n": "NBA official game ball", "a": "", "d": "Genuine-leather game ball of the NBA, sold in official and replica grades.", "mk": SP, "y": "1983", "s": BB,
   "v": [V("NBA game ball", SP, "1983", "supplied the NBA 1983–2021; a composite version was tried and dropped in 2006–07"),
         V("NBA game ball", WI, "2021", "Wilson supplier since 2021")], "dt": "leather or composite · official or replica"},
  {"n": "Evolution", "a": "Wilson Evolution", "d": "Composite-leather indoor ball widely used in high-school and college play.", "mk": WI, "s": EVO,
   "v": [], "dt": "size 6 (28.5 in) or size 7 (29.5 in) · colourway"}]}

hoop = {"n": "Basketball hoop", "a": "basketball system", "d": "Backboard, rim and net on a pole or wall mount for playing basketball at home.",
 "t": ["portable (filled base)", "in-ground", "wall-mounted", "poolside"], "s": HOOP,
 "m": [["Silverback NXT 54", "Goalrilla"], ["Ultimate Hybrid", SP], ["Momentous EZ Assembly", SP], ["The Beast", SP], ["71522 Competition XL", "Lifetime"],
       ["51550", "Lifetime"], ["90040", "Lifetime"], ["Splash & Shoot", "Dunn-Rite"]]}

volley = {"n": "Volleyball", "a": "", "d": "Light inflated ball made for volleyball, in indoor and slightly larger, softer beach versions.",
 "t": ["indoor", "beach", "youth"], "s": VB,
 "x": [{"n": "FIVB official ball", "a": "", "d": "Mikasa's official ball of the FIVB and CEV for indoor and beach play.", "mk": MI, "y": "2008", "s": VB,
   "v": [V("FIVB indoor ball", MI, "2008", "dimpled eight-panel design adopted by the FIVB")], "dt": "indoor or beach · panel count · colourway"}]}

netball = {"n": "Netball", "a": "netball ball", "d": "Leather or rubber ball about 22 cm across made for netball.", "t": ["match", "training", "size 4 / 5"], "s": NB}

handball = {"n": "Handball", "a": "handball ball", "d": "Small panelled ball gripped in one hand, made for team handball; sizes 0–3 by age and sex.",
 "t": ["size 0 / 1 / 2 / 3", "match", "replica", "street"], "s": HB,
 "x": [{"n": "Ultimate", "a": "Select Ultimate", "d": "Select's hand-sewn match ball used in the EHF Champions League and many top leagues.", "mk": SE, "s": HB,
   "v": [V("Ultimate LNH", SE, "", "French league edition"), V("Ultimate Replica", SE, "", "cheaper replica")], "dt": "size · league edition · colourway"}],
 "m": [["Goalcha", SE], ["Kids Soft", SE]]}

lax = {"n": "Lacrosse stick", "a": "crosse", "d": "Stick with a netted triangular head used to carry, pass and shoot the ball in lacrosse.",
 "t": ["attack or midfield", "defence long pole", "goalie", "women's", "wooden (hickory)", "complete stick or head only"], "s": LS,
 "x": [
  {"n": "Plastic lacrosse head", "a": "", "d": "Moulded plastic head that replaced wooden sticks.", "mk": STX, "y": "1970", "s": LS,
   "v": [V("first plastic head", STX, "1970", "patented"), V("Stallion", STX), V("Surgeon", STX), V("Hammer", STX), V("X10", STX)], "dt": "head shape · stiffness · mesh pocket"},
  {"n": "Offset head", "a": "", "d": "Head set below the shaft line to improve hold and release.", "mk": BR, "y": "1995", "s": LS,
   "v": [V("offset head patent", BR, "1995"), V("Clutch X", BR)], "dt": "offset · face shape"}],
 "m": [["Torq", "Gait"], ["CEO", "Nike"], ["Noz X", "Warrior"], ["Evo 4x", "Warrior"], ["Optik U", "Maverik"], ["Mark 1", "StringKing"],
       ["Rebel Offense", "ECD"], ["Hawk", "Epoch"], ["Command X", "Under Armour"]]}

hurley = {"n": "Hurley", "a": "hurl · camán · hurling stick", "d": "Ash stick with a flat curved bas used to strike the sliotar in hurling and camogie.",
 "t": ["ash", "bamboo", "synthetic", "camogie (no band)"], "s": HU,
 "m": [["bamboo hurley", "Torpey"]]}

sliotar = {"n": "Sliotar", "a": "hurling ball", "d": "Leather-covered cork-centred ball 69–72 mm across used in hurling and camogie.",
 "t": ["white", "optic yellow"], "s": HG}

brands = [
 {"n": SP, "c": "United States", "f": "1876", "seg": "Mainstream", "kf": "basketballs, hoops", "d": "American sporting-goods brand; NBA ball supplier 1983–2021.", "sig": ["NBA official game ball"], "s": "knowledge"},
 {"n": MI, "c": "Japan", "seg": "Specialist", "kf": "volleyballs", "d": "Japanese ball maker; official ball of the FIVB.", "sig": ["FIVB official ball"], "s": "knowledge"},
 {"n": "Molten", "c": "Japan", "seg": "Specialist", "kf": "balls", "d": "Japanese ball maker of basketballs and volleyballs.", "s": "knowledge"},
 {"n": SE, "c": "Denmark", "seg": "Specialist", "kf": "handballs, footballs", "d": "Danish ball maker known for handballs.", "sig": ["Ultimate"], "s": "knowledge"},
 {"n": STX, "c": "United States", "seg": "Specialist", "kf": "lacrosse", "d": "American lacrosse maker that patented the first plastic head.", "sig": ["Plastic lacrosse head"], "rel": [BR, "Warrior"], "s": "knowledge"},
 {"n": BR, "c": "United States", "seg": "Specialist", "kf": "lacrosse", "d": "American lacrosse maker that patented the offset head.", "sig": ["Offset head"], "rel": [STX], "s": "knowledge"},
]

trads = [{"n": "Hurley making", "g": "Woodwork & furniture", "r": "Ireland", "p": "traditional, ongoing",
  "d": "Local craftsmen shape hurleys from ash, using the butt of the tree near the root.", "tech": "sawing and shaping ash planks; steel band on the bas; splicing repairs",
  "mat": "ash; bamboo since 2020", "forms": ["Hurley"], "ctr": ["Torpey"], "auth": "cut from the root end of an ash butt", "s": HU}]

w('04_01', {"kinds": [basketball, hoop, volley, netball, handball, lax, hurley, sliotar], "brands": brands, "traditions": trads,
 "notes": "New shelf; all 7 planned kinds added, each sourced to a retrieved page. Sliotar added as its own kind beside Hurley. Archetypes: NBA official game ball (Spalding, then Wilson), Wilson Evolution, Mikasa FIVB ball, Select Ultimate, STX plastic head, Brine offset head. Not added for lack of a retrieved page: Molten GG7X and BG series, Mikasa V200W model name, Gilbert netballs, Cúl4 and other hurley makers, Goalrilla in-ground hoops. Hurley-making tradition added from the Hurley article. Molten (USA Volleyball, NCAA indoor) and Wilson (AVP, NCAA beach) named in the Volleyball ball article as official suppliers, without model names."})
