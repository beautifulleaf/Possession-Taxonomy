import json, os
def w(job, obj):
    p = f'/home/user/Possession-Taxonomy/rebuild/work/E2/shelves/{job}.json'
    t = p + '.tmp'; json.dump(obj, open(t, 'w'), ensure_ascii=False, indent=1); os.replace(t, p)
def V(n, mk, y="", d=""):
    v = {"n": n, "mk": mk}
    if y: v["y"] = y
    if d: v["d"] = d
    return v
TM = "TaylorMade Golf"; CA = "Callaway Golf Company"; TI = "Titleist"; SR = "Srixon"; WI = "Wilson Sporting Goods"; KS = "Kirkland Signature"
TIW = "https://en.wikipedia.org/wiki/Titleist"
ZS = "https://www.golfmagic.com/equipment/balls-accessories/srixon-z-star-golf-ball-review"
GM21 = "https://www.golfmagic.com/equipment-news/callaway-chrome-soft-taylormade-tp5-what-best-golf-ball-2021"
KIRK = "https://thegolfnewsnet.com/ryan_ballengee/2016/10/08/costco-kirkland-signature-golf-balls-99678/"
TG = "https://www.todays-golfer.com/equipment/best/golf-push-trolleys/"
GC = "https://golf.com/gear/golf-accessories/best-electric-golf-push-carts/"
GL = "https://golfinsideruk.com/footjoy-stasof-golf-glove-review/"

ball = {"n": "Golf ball", "a": "", "d": "Dimpled ball made to the rules of golf.",
 "t": ["two-piece distance", "soft-feel", "multi-layer urethane tour ball", "coloured or alignment print"],
 "s": "https://www.andrewmorrisgolf.ie/collections/multi-buy-golf-ball-offer?page=1",
 "x": [
  {"n": "Pro V1", "a": "Pro V1x", "d": "Titleist's multi-layer urethane-covered tour ball, the benchmark premium ball.", "mk": TI, "y": "2000", "s": TIW,
   "v": [V("Pro V1", TI, "2000", "tour debut October 2000, on sale December 2000"), V("Pro V1x", TI, "", "firmer, higher-spin sibling, about three years later")],
   "dt": "compression · white or yellow · alignment print"},
  {"n": "Z-Star", "a": "", "d": "Srixon's three-piece urethane-covered tour ball.", "mk": SR, "y": "2011", "s": ZS,
   "v": [V("Z-Star", SR, "2025", "ninth generation"), V("Z-Star XV", SR, "", "faster, higher compression"), V("Z-Star Diamond", SR, "", "tour-oriented"),
         V("Z-Star Divide", SR, "2025", "two-tone white and yellow")],
   "dt": "compression · white, yellow or two-tone"},
  {"n": "Chrome Soft", "a": "", "d": "Callaway's soft-feel urethane tour ball, since superseded by Chrome Tour.", "mk": CA, "s": ZS,
   "v": [V("Chrome Soft X", CA), V("Chrome Soft XLS", CA), V("Chrome Tour", CA, "", "successor")], "dt": "compression · white or yellow"},
  {"n": "TP5", "d": "TaylorMade's five-layer tour ball.", "mk": TM, "s": GM21, "v": [], "dt": "compression · white or yellow"},
  {"n": "Kirkland Signature Four-Piece", "a": "Costco ball", "d": "Low-priced four-piece urethane ball sold by Costco that rivalled premium tour balls.", "mk": KS, "y": "2016", "s": KIRK,
   "v": [V("Four-Piece Urethane Cover", KS, "2016", "made by Nassau Golf of South Korea; 360 dimples")], "dt": "sold in two-dozen packs"}],
 "m": [["AVX", TI], ["Tour Soft", TI], ["Trufeel", TI], ["Velocity", TI], ["Tour Response", TM], ["SpeedSoft", TM], ["Distance+", TM],
       ["Supersoft", CA], ["Soft Feel", SR], ["AD333", SR], ["Duo Soft", WI]],
 "r": [["Pro V1 family", TI]]}

bag = {"n": "Golf bag", "a": "", "d": "Bag that carries one set of golf clubs.", "t": ["stand bag", "cart bag", "tour (staff) bag", "pencil (Sunday) bag", "travel cover"],
 "s": "https://www.golfdiscount.com/collections/golf-bags?page=1",
 "m": [["Hybrid 14", TI], ["Traverse", "Ping"], ["Eclipse E-2.5", "Sun Mountain"], ["Loma", "Sunday Golf"], ["El Camino", "Sunday Golf"], ["The Big Rig", "Sunday Golf"]]}

rf = {"n": "Golf rangefinder", "a": "laser rangefinder", "d": "Handheld laser rangefinder made to measure the distance to the flag. Golf GPS units are in Phones, Tablets & Personal Devices.",
 "t": ["with slope", "without slope", "laser-GPS hybrid"],
 "s": "https://www.golfdiscount.com/collections/electronics-golf-devices-rangefinders",
 "m": [["Pro X3+", "Bushnell"], ["Tour V6 Shift", "Bushnell"], ["A1 Slope", "Bushnell"], ["COOLSHOT PRO II Stabilized", "Nikon"], ["Approach Z82", "Garmin"],
       ["Approach Z30", "Garmin"], ["SL3", "Voice Caddie"], ["Anarch", "Vortex"], ["Pro L2", "Shot Scope"], ["NX10 Slope", "Precision Pro Golf"],
       ["Series 4 Ultra", "Blue Tees Golf"], ["GenePro G1", "Mileseey Golf"], ["Sureshot Pinloc 6000iM", "MGI Golf"]]}

trolley = {"n": "Golf trolley", "a": "golf cart · push cart · caddy", "d": "Wheeled frame that carries a golf bag round the course, pushed by hand or battery-driven.",
 "t": ["push (two- or three-wheel)", "electric", "remote or follow"], "s": TG,
 "m": [["Clicgear 4.0", "Clicgear"], ["Cube Push", "Motocaddy"], ["Autofold FF", "Big Max"], ["DLX-Lite FF", "PowaKaddy"], ["R1-S", "Stewart Golf"],
       ["Nitron", "BagBoy"], ["M7 Remote", "Motocaddy"], ["Q Follow", "Stewart Golf"], ["Zip Navigator", "MGI Golf"], ["X4 Sport", "Batcaddy"]]}

glove = {"n": "Golf glove", "a": "", "d": "Thin close-fitting glove worn on the lead hand to improve grip on the club.",
 "t": ["cabretta leather", "synthetic", "hybrid", "rain glove (pair)"], "s": GL,
 "m": [["StaSof", "FootJoy"], ["Players Flex", TI], ["Cabretta Premium", SR], ["Staff Model", WI], ["RainGrip", "FootJoy"], ["Weather Spann", CA]]}

brands = [
 {"n": KS, "c": "United States", "seg": "Own-label & retailer", "kf": "value tour ball", "d": "Costco's own label; its golf balls are made by contract factories such as Nassau Golf.", "s": KIRK},
 {"n": "FootJoy", "c": "United States", "seg": "Premium", "kf": "golf gloves, shoes", "d": "Acushnet golf footwear and glove brand, sister to Titleist.", "rel": [TI], "s": "knowledge"},
 {"n": "Bushnell", "c": "United States", "seg": "Specialist", "kf": "laser rangefinders", "d": "Sports-optics maker whose golf laser rangefinders lead the category.", "s": "knowledge"},
 {"n": "Motocaddy", "c": "United Kingdom", "seg": "Mainstream", "kf": "electric trolleys", "d": "British maker of push and electric golf trolleys.", "s": "knowledge"},
 {"n": "Stewart Golf", "c": "United Kingdom", "seg": "Premium", "kf": "follow trolleys", "d": "British maker of push and remote or follow-mode electric trolleys.", "s": "knowledge"},
]

w('03_01', {"kinds": [ball, bag, rf, trolley, glove], "brands": brands, "traditions": [],
 "notes": "Kept Golf ball, Golf bag, Golf rangefinder; added Golf trolley (push/electric types) and Golf glove as new kinds. Ball: 12 flat models became 5 archetypes (Pro V1, Z-Star, Chrome Soft, TP5, Kirkland Signature) with 11 flat models kept. Bridgestone Tour B left out: no retrieved page named it. Rangefinder 20->13, dropping MGI, Blue Tees and Mileseey near-duplicates and CaddyTalk; added the MyGolfSpy 2024 test winners (Nikon COOLSHOT PRO II Stabilized, Vortex Anarch, Shot Scope Pro L2, Voice Caddie SL3). Trolleys come from Today's Golfer and Golf.com test lists. Gloves come from Golf Insider's 17-glove test. Clubmaker brands are registered in shelf 03_00."})
