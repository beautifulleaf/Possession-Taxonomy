import json, os
def w(job, obj):
    p = f'/home/user/Possession-Taxonomy/rebuild/work/E2/shelves/{job}.json'
    t = p + '.tmp'; json.dump(obj, open(t, 'w'), ensure_ascii=False, indent=1); os.replace(t, p)
def V(n, mk, y="", d=""):
    v = {"n": n, "mk": mk}
    if y: v["y"] = y
    if d: v["d"] = d
    return v
LS = "Louisville Slugger"; RA = "Rawlings"; WI = "Wilson"; MZ = "Mizuno"; MA = "Marucci Sports"; DM = "DeMarini"; EA = "Easton"; MI = "Miken"; WO = "Worth"
GLW = "https://en.wikipedia.org/wiki/Baseball_glove"
BBW = "https://en.wikipedia.org/wiki/Baseball_bat"
LSW = "https://en.wikipedia.org/wiki/Louisville_Slugger"
RAW = "https://en.wikipedia.org/wiki/Rawlings_(company)"
MAW = "https://en.wikipedia.org/wiki/Marucci_Sports"
DMW = "https://en.wikipedia.org/wiki/DeMarini"
EAW = "https://en.wikipedia.org/wiki/Easton_Sports"
A2K = "https://www.catchershome.com/wilson-a2000-catchers-mitts/"
MZP = "https://www.whatproswear.com/baseball/news/origins-how-a-baseball-glove-is-made-at-the-mizuno-pro-glove-factory/"
MZW = "https://usa.mizuno.com/baseball-gww-40haga-world-win-11-5-baseball-glove/"
PRIME = "https://abca.org/magazine/2016-3-Summer/Last_Inning_Louisville_Slugger_Introduces_its_Most_Innovative_Wood_Bat_Lineup_Yet_MLB_PRIME.aspx"
COB = "https://www.closeoutbats.com/bat-shop.html"
PSU = "https://www.acs.psu.edu/drussell/bats/compalum.html"
MACH = "https://www.teamexpress.com/rawlings-mach-matte-batting-helmet"
BBR = "https://www.baseball-reference.com/bullpen/Batting_helmets"

glove = {"n": "Baseball glove", "a": "baseball mitt · fielding glove", "d": "Padded leather glove or mitt with a webbed pocket, made for catching in baseball or softball.",
 "t": ["catcher's mitt (32–34 in)", "first baseman's mitt", "infield (11–12 in)", "outfield (12–12¾ in)", "pitcher's (closed web)", "fastpitch softball", "left-hand throw", "youth"],
 "s": "https://www.closeoutbats.com/glove-shop.html",
 "x": [
  {"n": "A2000", "a": "", "d": "Wilson's pro glove, the first popular glove with a deep pocket and hinge that closes like jaws.", "mk": WI, "y": "1957", "s": A2K,
   "v": [V("1786 pattern", WI, "", "infield pattern"), V("CM33", WI, "", "33 in catcher's mitt"), V("1790 SuperSkin", WI, "2017", "34 in catcher's mitt"),
         V("M1 SuperSkin", WI, "2017", "33.5 in catcher's mitt"), V("Pudge", WI, "", "32.5 in catcher's mitt"), V("A2000 SuperSkin fastpitch", WI, "2017", "fastpitch catcher's mitt")],
   "dt": "pattern number · size · web · leather (Pro Stock, SuperSkin) · colourway"},
  {"n": "Heart of the Hide", "a": "HOH", "d": "Rawlings pro-grade leather glove series.", "mk": RA, "s": RAW, "v": [], "dt": "pattern · size · web · colourway"},
  {"n": "Pro Preferred", "a": "", "d": "Rawlings premium glove series.", "mk": RA, "s": RAW, "v": [], "dt": "pattern · size · web"},
  {"n": "Mizuno Pro", "a": "", "d": "Mizuno's top glove, made at its Haga factory in Japan, which supplies about 40% of Japanese professional players.", "mk": MZ, "s": MZP, "v": [],
   "dt": "pattern · size · web · made in Haga"},
  {"n": "World Win", "a": "", "d": "Mizuno's position-specific glove series of 1974, reissued from Haga.", "mk": MZ, "y": "1974", "s": MZW,
   "v": [V("GWW-40HAGA", MZ, "", "reissue to the original 1974 specification; Victory Cup cross web")], "dt": "11.5 in · natural leather"}],
 "r": [["A1000", WI], ["Gold Glove", RA], ["Heritage Pro", RA]]}

bat = {"n": "Baseball bat", "a": "", "d": "Rounded wooden or metal bat made for baseball, certified to the standard of the league it is used in.",
 "t": ["ash", "maple", "aluminium alloy", "composite", "hybrid", "BBCOR (high school and college)", "USA Baseball (youth)", "USSSA big barrel"],
 "s": "https://www.closeoutbats.com/bat-shop.html",
 "x": [
  {"n": "R43", "a": "Babe Ruth model", "d": "Louisville Slugger's model number for Babe Ruth's bats.", "mk": LS, "y": "1920s", "s": LSW, "v": [], "dt": "ash · length · weight"},
  {"n": "MLB Prime", "a": "", "d": "Louisville Slugger's top wood bat line, from pro-grade ink-dot wood with a hardened finish.", "mk": LS, "y": "2016", "s": PRIME,
   "v": [V("MLB Prime with EXOARMOR", LS, "2016", "finish said to make the bat twice as hard")], "dt": "turning model · maple or ash · length · finish"},
  {"n": "CAT", "a": "", "d": "Marucci's alloy bat series for BBCOR and USSSA baseball.", "mk": MA, "s": MAW,
   "v": [V("Cat 6", MA), V("Cat 7", MA), V("Cat 8", MA), V("Cat 8 Connect", MA, "", "two-piece"), V("Cat 9", MA), V("Cat 9 Connect", MA, "", "two-piece"), V("Cat 9 composite", MA)],
   "dt": "BBCOR, USSSA or USA · length · drop"},
  {"n": "Voodoo", "a": "F2", "d": "DeMarini bat series that began as the F2.", "mk": DM, "s": DMW, "v": [], "dt": "BBCOR, USSSA or USA · drop"},
  {"n": "CF", "a": "", "d": "DeMarini's composite bat series.", "mk": DM, "s": DMW, "v": [], "dt": "BBCOR, USSSA or USA · drop"}],
 "m": [["Supra", LS], ["TVT Pro Exclusive Maple", MA], ["F5", MA], ["Nitro", DM], ["Diablo", DM], ["Coastal Collective Uluwatu Spec-H1", "Combat"]]}

sbat = {"n": "Softball bat", "a": "", "d": "Long, light bat made for fastpitch or slowpitch softball, certified by softball governing bodies.",
 "t": ["fastpitch", "slowpitch", "aluminium single-wall", "aluminium double-wall", "composite", "two-piece"],
 "s": PSU,
 "x": [
  {"n": "Velocit-E Ultra", "a": "Ultra", "d": "Miken composite slowpitch bat, banned by the ASA after its 2002 release for exceeding the performance limit.", "mk": MI, "y": "2002", "s": PSU,
   "v": [V("Ultra II", MI, "", "also illegal for ASA league play")], "dt": "slowpitch · composite"},
  {"n": "Genesis", "a": "", "d": "Louisville Slugger composite slowpitch bat.", "mk": LS, "s": PSU,
   "v": [V("SB34", LS, "", "early version"), V("SB103", LS, "", "thicker wall, more durable")], "dt": "slowpitch · composite"},
  {"n": "EST", "a": "", "d": "Worth double-wall aluminium slowpitch bat, overall winner of the 2001 Bat Wars test.", "mk": WO, "y": "2001", "s": PSU, "v": [], "dt": "slowpitch · double-wall aluminium"}],
 "m": [["Halo", RA], ["Super Freak Highlighter", MI], ["Synergy", EA]]}

helmet = {"n": "Batting helmet", "a": "", "d": "Hard-shell helmet with one or two ear flaps, made for batting and base running in baseball or softball.",
 "t": ["single ear flap", "double ear flap", "with face guard", "junior", "senior"], "s": "https://www.closeoutbats.com/rawlings.html",
 "m": [["Mach", RA]]}

catcher = {"n": "Catcher's gear", "a": "catcher's set", "d": "Catcher's helmet or mask, chest protector and leg guards, as a set or piece.",
 "t": ["hockey-style helmet", "traditional mask", "chest protector", "leg guards", "youth set"], "s": "https://www.closeoutbats.com/rawlings.html"}

brands = [
 {"n": LS, "c": "United States", "f": "1855", "seg": "Heritage manufactory", "kf": "wood bats", "d": "Louisville bat brand of Hillerich & Bradsby, sold to Wilson Sporting Goods in 2015; its factory and museum are in Louisville.",
  "sig": ["R43", "MLB Prime", "Genesis"], "rel": [WI, RA], "s": LSW},
 {"n": RA, "c": "United States", "f": "1887", "seg": "Professional & flagship", "kf": "gloves", "d": "St Louis baseball maker that bought Bill Doak's webbed glove design and sponsors the Gold Glove award; owner of Easton Diamond since 2020.",
  "lines": ["Gold Glove", "Heritage Pro", "Heart of the Hide", "Pro Preferred"], "sig": ["Heart of the Hide", "Pro Preferred"], "rel": [EA, WI], "s": RAW},
 {"n": MA, "c": "United States", "f": "2002", "seg": "Premium", "kf": "wood and alloy bats", "d": "Baton Rouge bat maker founded by Jack Marucci; owns Victus; official bat of Major League Baseball from 2025.",
  "sig": ["CAT"], "rel": [LS], "s": MAW},
 {"n": DM, "c": "United States", "f": "1989", "seg": "Premium", "kf": "composite bats", "d": "Oregon bat maker founded by Ray DeMarini, known for double-wall bats; a Wilson subsidiary.",
  "sig": ["Voodoo", "CF"], "rel": [WI], "s": DMW},
 {"n": EA, "c": "United States", "seg": "Mainstream", "kf": "alloy bats", "d": "Bat maker that began making aluminium bats in 1969; its Easton Diamond baseball unit was bought by Rawlings in 2020.",
  "rel": [RA], "s": EAW},
 {"n": MI, "c": "United States", "seg": "Specialist", "kf": "slowpitch bats", "d": "Softball bat maker whose composite Ultra changed slowpitch performance rules.", "sig": ["Velocit-E Ultra"], "s": PSU},
 {"n": WO, "c": "United States", "seg": "Specialist", "kf": "softball bats", "d": "Softball bat maker known for double-wall aluminium slowpitch bats.", "sig": ["EST"], "s": PSU},
]

w('04_03', {"kinds": [glove, bat, sbat, helmet, catcher], "brands": brands, "traditions": [],
 "notes": "All 4 old kinds kept; Softball bat added (source: Penn State bat physics page). Glove: archetypes A2000 (old 1786 pattern now a version), Heart of the Hide, Pro Preferred, Mizuno Pro, World Win; A1000 kept as range. Bat: archetypes R43, MLB Prime, Marucci CAT, DeMarini Voodoo and CF; Supra kept in m. Easton named-bat lines, Victus models, Rawlings Velo/Icon and S100/Mach Pro helmets left out: no retrieved page named them. Bat Digest award page came back empty, so no independent test winners. Wilson and Mizuno already registered in 02_00/03_00 (Wilson as 'Wilson')."})
