import json, os
def w(job, obj):
    p = f'/home/user/Possession-Taxonomy/rebuild/work/E2/shelves/{job}.json'
    t = p + '.tmp'; json.dump(obj, open(t, 'w'), ensure_ascii=False, indent=1); os.replace(t, p)
def V(n, mk, y="", d=""):
    v = {"n": n, "mk": mk}
    if y: v["y"] = y
    if d: v["d"] = d
    return v
TM = "TaylorMade Golf"; CA = "Callaway Golf Company"; PI = "Ping (Karsten Manufacturing)"; TI = "Titleist"
SC = "Scotty Cameron"; MZ = "Mizuno"; OD = "Odyssey Golf"; CO = "Cobra Golf"; SR = "Srixon"; CL = "Cleveland Golf"
WI = "Wilson Sporting Goods"; XX = "XXIO"; TE = "Tour Edge Golf"; LAB = "L.A.B. Golf"
NCG = "https://www.nationalclubgolfer.com/equipment/drivers/40-years-of-game-changing-technology-how-taylormade-revolutionised-the-driver-industry"
UPG = "https://www.underpargoals.com/callaway-drivers-by-year/"
R7 = "https://en.wikipedia.org/wiki/R7_Quad"
PINGW = "https://en.wikipedia.org/wiki/Ping_(golf)"
PINGI = "https://www.golfwrx.com/603722/greatest-ping-irons-of-all-time"
MIZ = "https://golfwrx.com/602872/greatest-mizuno-blade-irons-of-all-time/"
VOK = "https://nextroundgolf.com/blogs/news/vokey-wedges-through-the-years-from-spin-milled-to-sm10"
NEW = "https://www.scottycameron.com/articles/the-collectors-corner-the-evolution-of-the-newport/"
CAW = "https://en.wikipedia.org/wiki/Callaway_Golf_Company"
TIW = "https://en.wikipedia.org/wiki/Titleist"
TMW = "https://en.wikipedia.org/wiki/TaylorMade_Golf"

driver = {"n": "Golf driver", "a": "1-wood", "d": "Lowest-lofted wood with the largest head, made to hit the ball off the tee for maximum distance.",
 "t": ["standard", "low-spin", "draw-biased", "lightweight", "mini driver"],
 "s": "https://www.wwgolf.com/drivers-1/",
 "x": [
  {"n": "Pittsburgh Persimmon", "a": "1Metal · metalwood driver", "d": "Steel-headed metalwood that began the move away from persimmon drivers.", "mk": TM, "y": "1979", "s": NCG,
   "v": [V("1Metal / Pittsburgh Persimmon", TM, "1979", "first metalwood; renamed 1980"), V("Burner", TM, "1983", "side dimpling"),
         V("Titanium Bubble Shaft", TM, "1995", "first TaylorMade titanium driver"), V("R300 series", TM, "2001", "300 Ti, 320 Ti, 360 Ti heads"),
         V("R5", TM, "2002", "Inverted Cone face")],
   "dt": "head material steel, then titanium · head size · loft"},
  {"n": "Big Bertha", "a": "Great Big Bertha", "d": "Oversized-head driver that made large, forgiving metal drivers mainstream.", "mk": CA, "y": "1991", "s": UPG,
   "v": [V("Big Bertha", CA, "1991", "original oversized steel head"), V("Great Big Bertha", CA, "1995"), V("Big Bertha War Bird", CA, "1995"),
         V("Biggest Big Bertha", CA, "1997"), V("Big Bertha Titanium 454", CA, "2005"), V("Big Bertha Alpha 815", CA, "2014"), V("Great Big Bertha", CA, "2022")],
   "dt": "head size 190–460 cc · steel or titanium · loft"},
  {"n": "R7 Quad", "a": "r7", "d": "Driver with four movable weight screws that let the owner change ball flight.", "mk": TM, "y": "2004", "s": R7,
   "v": [V("R7 Quad", TM, "2004", "movable weight technology"), V("R7 425", TM, "2005", "425 cc head"), V("R7 460", TM, "2006", "460 cc, two weights"),
         V("R7 Superquad", TM, "2007", "four weights, 460 cc"), V("R7 CGB Max", TM, "2008"), V("R9", TM, "2009", "adds adjustable hosel"),
         V("R7 Quad Mini", TM, "", "modern mini-driver revival")],
   "dt": "weight ports and cartridges · head size 400–460 cc"},
  {"n": "M-series and carbon-face TaylorMade drivers", "a": "M1 · SIM · Stealth · Qi", "d": "TaylorMade's multi-material driver line, moving to a carbon face with Stealth.", "mk": TM, "y": "2016", "s": NCG,
   "v": [V("M1 and M2", TM, "2016", "multi-material head"), V("M3 and M4", TM, "2018", "Twist Face"), V("M5 and M6", TM, "2019", "tuning resin"),
         V("SIM and SIM Max", TM, "2020", "asymmetric sole"), V("SIM2", TM, "2021", "forged ring chassis"),
         V("Stealth", TM, "2022", "60-layer carbon face"), V("Stealth 2", TM, "2023"), V("Qi4D", TM, "", "with LS, Max and Max Lite heads")],
   "dt": "carbon or titanium face · LS / standard / Max heads · sliding or fixed weights"},
  {"n": "Epic", "a": "Great Big Bertha Epic", "d": "Callaway's tour-level driver family, succeeded by Paradym and Quantum.", "mk": CA, "y": "2017", "s": UPG,
   "v": [V("Great Big Bertha Epic", CA, "2017", "also Sub Zero"), V("Rogue", CA, "2018"), V("Epic Flash", CA, "2019"), V("Mavrik", CA, "2020"),
         V("Epic Speed / Epic MAX", CA, "2021"), V("Rogue ST MAX", CA, "2022"), V("Paradym", CA, "2023", "also X and Triple Diamond"),
         V("Quantum Max", CA, "", "with Triple Diamond and Max D heads")],
   "dt": "Max, Sub Zero / Triple Diamond and draw heads · loft"},
  {"n": "975D", "a": "", "d": "Titleist titanium driver designed by Terry McCabe.", "mk": TI, "s": TIW,
   "v": [V("GT2", TI, "", "current Titleist line"), V("GT4", TI), V("GTS2", TI), V("GTS3", TI)], "dt": "head size · loft · adjustable hosel"}],
 "m": [["G440 Max", PI], ["G440 LST", PI], ["G440 SFT", PI], ["OPTM X", CO], ["OPTM LS", CO], ["ZXi", SR], ["ZXi LS", SR],
       ["JPX ONE", MZ], ["Exotics C725", TE]],
 "r": [["G440", PI], ["GT", TI], ["OPTM", CO], ["Qi4D", TM], ["Quantum", CA], ["ZXi", SR]]}

fairway = {"n": "Fairway wood", "a": "3-wood · 5-wood", "d": "Wood with more loft and a smaller head than the driver, made to be hit from the fairway or tee.",
 "s": "https://www.golfdiscount.com/collections/golf-clubs-fairway-woods-mens?page=3",
 "m": [["Quantum Max Fast", CA], ["Quantum Triple Diamond", CA], ["OPTM Max", CO], ["G440 LST", PI], ["Qi4D Tour", TM], ["Qi10 Tour", TM],
       ["GT1", TI], ["GT3", TI], ["TSR3", TI], ["DYNAPWR Max", WI], ["XXIO 14", XX]],
 "r": [["Dynapower", WI], ["G440", PI], ["GT", TI], ["OPTM", CO], ["Qi4D", TM], ["Quantum", CA]]}

hybrid = {"n": "Hybrid", "a": "utility · rescue", "d": "Club with a compact wood-like head that replaces a long iron.",
 "s": "https://www.scheels.com/c/golf-hybrids-and-utility-irons",
 "m": [["Elyte", CA], ["Elyte X", CA], ["Quantum Max", CA], ["OPTM", CO], ["G440", PI], ["ZXi", SR], ["Qi4D Rescue", TM], ["GT1", TI], ["GT2", TI], ["XXIO 13", XX]],
 "r": [["G440", PI], ["GT", TI], ["OPTM", CO], ["Qi4D", TM], ["Quantum", CA], ["ZXi", SR]]}

irons = {"n": "Golf iron set", "a": "irons", "d": "Matched set of irons of graded loft with flat-faced heads.",
 "t": ["blade (muscle back)", "cavity back", "players distance", "game-improvement", "combo set"],
 "s": "https://shop.foremostgolf.com/sets-of-golf-irons",
 "x": [
  {"n": "Eye 2", "a": "Ping Eye2", "d": "Cast perimeter-weighted cavity-back iron; long-running best seller and centre of the square-groove dispute.", "mk": PI, "y": "1982", "s": PINGI,
   "v": [V("69 irons", PI, "1961", "Karsten Solheim's first irons; cavity milled later"), V("K1", PI, "late 1960s", "stainless cast steel set"),
         V("Eye", PI, "1978", "eye-shaped cavity"), V("Eye 2", PI, "1982", "V grooves, U grooves from 1984"),
         V("Eye 2 square-groove model", PI, "1985", "grandfathered 1985–1989 heads"), V("ISI", PI, "1998"), V("i3", PI, "2000", "blade and O-Size"),
         V("S59", PI, "2003"), V("Rapture", PI, "2006", "multi-material, first made overseas")],
   "dt": "colour-coded lie dot · groove type · stainless or beryllium copper"},
  {"n": "MP forged blade", "a": "Mizuno Pro · MS Pro", "d": "Mizuno's Grain Flow forged carbon-steel muscle-back blades for better players.", "mk": MZ, "s": MIZ,
   "v": [V("MS Pro line", MZ, "", "three blade shapes; MS name later became MP"), V("TN-87", MZ, "1988", "named for Tommy Nakajima; re-released 2014"),
         V("MP-29", MZ, "1992", "sold until 2000"), V("MP-14", MZ), V("MP-33", MZ, "", "curved muscle back"), V("MP-32", MZ, "", "cut-muscle cavity"),
         V("MP-20", MZ, "", "copper underlay")],
   "dt": "muscle-back or cut-muscle · copper underlay · chrome or satin finish"}],
 "m": [["Forged ZXi5", SR], ["Forged ZXi7", SR], ["ZXiR HL", SR], ["Qi Max", TM], ["Quantum Max", CA], ["Quantum Max OS", CA],
       ["Dynapower Forged", WI], ["Dynapower Max", WI], ["Staff Model CB", WI], ["Staff Model XB", WI]],
 "r": [["Dynapower", WI], ["Quantum", CA], ["ZXi", SR]]}

driving = {"n": "Driving iron", "a": "utility iron", "d": "Long iron with a hollow or wide-soled head made to replace a long iron or hybrid.",
 "s": "https://www.scheels.com/c/golf-hybrids-and-utility-irons",
 "m": [["P-DHY utility iron", TM], ["P-UDI utility iron", TM]]}

wedge = {"n": "Golf wedge", "a": "pitching · gap · sand · lob wedge", "d": "High-lofted club made for short approach, pitch, chip and bunker shots.",
 "t": ["gap wedge", "sand wedge", "lob wedge", "full-face"],
 "s": "https://www.golfdiscount.com/collections/golf-clubs-wedges-sand-wedges",
 "x": [
  {"n": "Vokey Spin Milled", "a": "Vokey SM", "d": "Bob Vokey's milled-groove wedge family, sold in many loft, bounce and grind options.", "mk": TI, "s": VOK,
   "v": [V("Spin Milled", TI, "", "first generation"), V("SM4", TI, "2011"), V("SM5", TI, "2014"), V("SM6", TI, "2016", "progressive CG"),
         V("SM7", TI, "2018"), V("SM8", TI, "2020"), V("SM9", TI, "2022"), V("SM10", TI, "2024"), V("SM11", TI)],
   "dt": "loft 46–62° · bounce · sole grind · finish"}],
 "m": [["RTZ", CL], ["RTX 6 ZipCore", CL], ["CBZ", CL], ["Smart Sole Full-Face", CL], ["Opus", CA], ["Opus SP", CA], ["s159", PI], ["S259", PI],
       ["MG5", TM], ["Hi-Toe 5", TM], ["Pro T-1", MZ], ["King Black", CO], ["Hot Launch Max", TE]],
 "r": [["Opus", CA], ["RTZ", CL], ["Vokey SM", TI]]}

putter = {"n": "Putter", "a": "", "d": "Low-lofted club made to roll the ball on the green.",
 "t": ["blade", "mallet", "high-MOI mallet", "zero-torque"],
 "s": "https://andrewmorrisgolf.ie/collections/golf-putters?page=2",
 "x": [
  {"n": "Anser", "a": "Answer", "d": "Heel-toe weighted blade putter with a plumber's-neck offset hosel, the most copied putter shape.", "mk": PI, "y": "1966", "s": PINGW,
   "v": [V("1A", PI, "1959", "Solheim's first putter, centre-shafted predecessor"), V("Anser", PI, "1966", "patented 1967")],
   "dt": "neck style · head weight · finish"},
  {"n": "Newport", "a": "Classic I · Newport 2", "d": "Scotty Cameron's milled heel-toe blade, developed from the Classic I and made for Titleist since 1995.", "mk": SC, "y": "1995", "s": NEW,
   "v": [V("Classic I", SC, "1993", "won the 1993 Masters"), V("Newport", SC, "1995", "first Titleist version, 1995–1999"),
         V("Newport Teryllium", SC, "1997", "insert face; won the 1997 Masters"), V("Mil-Spec Newport", SC, "2000"), V("009", SC, "2004", "tour putter"),
         V("Studio Select Newport", SC, "2008", "first with interchangeable weights"), V("Newport Select", SC, "2012", "deep milling"),
         V("Special Select Newport", SC, "2021"), V("Super Select Newport", SC, "2024", "I-beam neck")],
   "dt": "carbon or stainless steel · neck (plumber's, slant, long) · weight 320–350 g"},
  {"n": "2-Ball", "a": "White Hot 2-Ball", "d": "Odyssey mallet with two ball-sized discs on top as an alignment aid.", "mk": OD, "y": "2002", "s": CAW,
   "v": [V("White Hot 2-Ball Mallet", OD, "2002", "White Hot insert line from 2000"), V("Ai-DUAL 2-Ball DB", OD)],
   "dt": "insert · neck · length"}],
 "m": [["Phantom 5", SC], ["Phantom 7", SC], ["Phantom 9R", SC], ["Phantom 11R OC", SC], ["Studio Style Fastback 2", SC], ["Studio Style Santa Fe", SC],
       ["Ai-DUAL #7", OD], ["Ai-DUAL Jailbird", OD], ["Ai-DUAL Square 2 Square #7", OD], ["Spider 5K-ZT", TM], ["DF3", LAB], ["DF2.1", LAB],
       ["3D Printed Agera RS", CO], ["M-Craft City Tokyo", MZ]],
 "r": [["Ai-DUAL", OD], ["M-Craft City Series", MZ], ["Phantom", SC], ["Studio Style", SC]]}

cset = {"n": "Complete golf set", "a": "package set · starter set", "d": "Packaged set of clubs, usually with a bag, sold as one product for beginners.",
 "s": "https://www.wwgolf.com/drivers-1/"}

def B(n, c, f, seg, kf, d, s, **kw):
    b = {"n": n, "c": c}
    if f: b["f"] = f
    b.update({"seg": seg, "kf": kf, "d": d}); b.update(kw); b["s"] = s; return b
brands = [
 B(TM, "United States", "1979", "Premium", "metalwood drivers", "Golf club maker founded by Gary Adams in McHenry, Illinois; now based in Carlsbad.", TMW,
   sig=["Pittsburgh Persimmon", "R7 Quad", "M-series and carbon-face TaylorMade drivers"], rel=["Callaway Golf Company", "Titleist"]),
 B(CA, "United States", "1982", "Premium", "drivers", "Golf company founded by Ely Callaway Jr., based in Carlsbad; owns Odyssey.", CAW,
   sig=["Big Bertha", "Epic"], rel=[OD, TM]),
 B(PI, "United States", "1959", "Premium", "putters, irons", "Golf club maker founded by Karsten Solheim in Redwood City; based in Phoenix.", PINGW,
   sig=["Anser", "Eye 2"], rel=[TI]),
 B(TI, "United States", "1932", "Premium", "balls, wedges", "Acushnet-owned golf brand founded by Philip E. Young in Fairhaven, Massachusetts.", TIW,
   lines=["Vokey", "Scotty Cameron"], sig=["Vokey Spin Milled", "975D"], rel=[SC]),
 B(SC, "United States", "", "Specialist", "milled putters", "Putter maker sold through Titleist since 1995.", NEW, sig=["Newport"], rel=[TI]),
 B(OD, "United States", "", "Specialist", "putters", "Putter brand owned by Callaway since 1997.", CAW, lines=["White Hot", "Ai-DUAL"], sig=["2-Ball"], rel=[CA]),
 B(MZ, "Japan", "1906", "Premium", "forged irons", "Japanese sporting-goods maker known in golf for Grain Flow forged irons.", "knowledge", sig=["MP forged blade"]),
 B(CO, "United States", "1973", "Mainstream", "drivers", "Golf club maker owned by Puma.", "knowledge"),
 B(SR, "Japan", "", "Mainstream", "irons, balls", "Golf brand of Sumitomo Rubber Industries.", "knowledge", rel=[CL, XX]),
 B(CL, "United States", "1979", "Specialist", "wedges", "Golf club maker known for wedges; part of Sumitomo Rubber Industries.", "knowledge", rel=[SR]),
 B(WI, "United States", "1914", "Mainstream", "Staff irons", "Chicago sporting-goods maker with a long-running golf range.", "knowledge"),
 B(XX, "Japan", "", "Premium", "lightweight clubs", "Sumitomo Rubber golf brand of lightweight clubs for moderate swing speeds.", "knowledge", rel=[SR]),
]

w('03_00', {"kinds": [driver, fairway, hybrid, irons, driving, wedge, putter, cset], "brands": brands, "traditions": [],
 "notes": "All 8 planned kinds kept. Driver: 33 flat models became 6 sourced archetypes (Pittsburgh Persimmon, Big Bertha, R7 Quad, TaylorMade M/SIM/Stealth line, Callaway Epic, Titleist 975D) with old models as versions plus 9 flat models; dropped Mini/Max Lite/Max D duplicates. Fairway 23->11, hybrid 14->10, irons 12->10 plus Ping Eye 2 and Mizuno MP blade archetypes; wedges 20->13 plus Vokey SM archetype; putters 38->14 plus Anser, Newport, 2-Ball archetypes. Not added for lack of a retrieved page: Titleist TSR/T-series irons, Ping G-series history, Callaway Elyte driver, Cobra, Srixon and PXG archetypes, Odyssey White Hot line beyond 2-Ball. Tour Edge and L.A.B. Golf kept as makers without register entries."})
