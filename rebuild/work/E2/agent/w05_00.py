import json, os
def w(job, obj):
    p = f'/home/user/Possession-Taxonomy/rebuild/work/E2/shelves/{job}.json'
    t = p + '.tmp'; json.dump(obj, open(t, 'w'), ensure_ascii=False, indent=1); os.replace(t, p)
def V(n, mk, y="", d=""):
    v = {"n": n, "mk": mk}
    if y: v["y"] = y
    if d: v["d"] = d
    return v
BP = "BEARPAW"; EA = "Easton Archery"; AAE = "Arizona Archery Enterprises"; FW = "Fairweather"; FV = "Fivics"
QW = "https://en.wikipedia.org/wiki/Quiver"
BRW = "https://en.wikipedia.org/wiki/Bracer"
TRW = "https://en.wikipedia.org/wiki/Thumb_ring"
KYW = "https://en.wikipedia.org/wiki/Kyūdō"
FS = "https://www.fieldandstream.com/outdoor-gear/hunting-gear/bow-hunting/best-archery-targets"
FWT = "https://www.bow-international.com/reviews/fairweather-tab/"
AAEP = "https://lancasterarchery.com/products/aae-elite-finger-tab-with-cordovan-face"
SAK = "https://www.merlinarchery.co.uk/fivics-saker-plus-epr-tab.html"
EEQ = "https://www.merlinarchery.co.uk/easton-elite-takedown-hip-quiver.html"
EGG = "https://www.geargeek.com/blog/the-rise-and-fall-of-easton-hockey-a-look-back-by-guest-blogger-james-duerr"

quiver = {"n": "Quiver", "a": "", "d": "Case worn on the body, set on the ground or fixed to the bow to carry arrows.",
 "t": ["back quiver", "belt or hip quiver (target)", "field quiver", "pocket quiver", "bow quiver", "ground quiver", "leather", "synthetic"],
 "s": "https://b2bportal.bearpaw-products.com/en/collections/quiver",
 "x": [
  {"n": "Yebira", "a": "", "d": "Japanese open-frame quiver used by ceremonial and traditional archers.", "mk": "", "s": KYW, "v": [], "dt": "lacquer · arrow count"},
  {"n": "Yazutsu", "a": "", "d": "Cylindrical quiver in which kyūdō archers normally keep their arrows.", "mk": "", "s": KYW, "v": [], "dt": "length · decoration"},
  {"n": "Arrow bag", "a": "", "d": "Drawstring cloth sack with a leather spacer at the top, used by medieval English longbowmen.", "mk": "", "s": QW, "v": [], "dt": "linen or canvas · leather spacer"},
  {"n": "Elite Takedown Hip Quiver", "a": "", "d": "Easton target hip quiver whose moulded body separates from the belt loop.", "mk": EA, "s": EEQ, "v": [], "dt": "right or left hand · colour · belt 18–47 in"}],
 "m": [["Back quiver Adventure", BP], ["Back quiver Back Pack Traditional", BP], ["Back quiver Bearpaw Long", BP], ["Back quiver Crazy Horse", BP],
       ["Back quiver DOA", BP], ["Back quiver Dark", BP], ["Back quiver Dynamic", BP], ["Back quiver Indian Summer", BP], ["Back quiver Junior Ranger", BP],
       ["Back quiver Raven", BP], ["Side quiver Basic", BP], ["Side quiver Easy", BP], ["Side quiver Mountain", BP], ["Side quiver Tube", BP]]}

target = {"n": "Archery target", "a": "boss · butt · bale", "d": "Boss, butt or block made to stop arrows, with or without a target face.",
 "t": ["foam block", "layered foam", "3D animal", "straw boss", "bag", "competition bale", "broadhead-rated"],
 "s": "https://www.lancasterarchery.com/targets.html",
 "m": [["18-1", "Rinehart Targets"], ["Buck XL 3D", "Blackout"], ["Block Range 48", "Block"], ["Supreme Range", "Morrell"], ["Hurricane Bag", "Field Logic"]]}

tab = {"n": "Archery finger tab", "a": "", "d": "Leather or synthetic pad worn on the drawing fingers to hold and release the string.",
 "t": ["cordovan face", "kangaroo or calf leather", "adjustable ledge", "plate (metal or plastic)", "simple leather"],
 "s": "https://www.kygunco.com/category/archery/archery-accessories/tabs-slings-and-guards/finger-tabs",
 "x": [
  {"n": "Elite Finger Tab", "a": "AAE Elite", "d": "AAE recurve tab with an anodised aluminium plate, adjustable ledge and replaceable cordovan face.", "mk": AAE, "s": AAEP,
   "v": [V("Elite Finger Tab with Cordovan Face", AAE)], "dt": "S–XL · right or left hand"},
  {"n": "Fairweather tab", "a": "", "d": "Tab designed by Olympic champion Simon Fairweather, held together by a single screw, with kangaroo leather and a middle-finger ring.", "mk": FW, "y": "2014", "s": FWT,
   "v": [], "dt": "plate S–XL · ring 18–25 mm · leather length"},
  {"n": "Saker", "a": "", "d": "Fivics recurve tab with adjustable ledge, weight and angle settings.", "mk": FV, "s": SAK,
   "v": [V("Saker Plus EPR", FV, "", "H Company cordovan; three weight and five angle settings")], "dt": "S–L · right or left hand"}],
 "m": [["Contour", "Axcel Archery"], ["Contour Pro", "Axcel Archery"], ["Beginner Finger Tab", EA]]}

ring = {"n": "Archery thumb ring", "a": "thumb ring · zihgir", "d": "Ring worn on the drawing thumb to protect it from the string in the thumb draw used across Asia.",
 "t": ["leather", "horn or bone", "jade or hardstone", "metal", "plastic"], "s": TRW,
 "x": [
  {"n": "Manchu cylindrical ring", "a": "", "d": "Cylindrical thumb ring that gradually replaced pad-shaped rings under the Qing dynasty; often jade.", "mk": "", "y": "Qing dynasty", "s": TRW, "v": [], "dt": "jade, hardstone or metal · size"},
  {"n": "Flanged (pad) ring", "a": "", "d": "Ring with a flange covering the thumb pad, the older Asian form.", "mk": "", "s": TRW, "v": [], "dt": "material · size"}]}

glove = {"n": "Archery shooting glove", "a": "", "d": "Glove worn on the drawing hand to draw and release the string.",
 "t": ["three-finger leather glove", "Japanese yugake"], "s": "https://www.kygunco.com/category/archery/archery-accessories/tabs-slings-and-guards",
 "x": [{"n": "Yugake", "a": "kyūdō glove", "d": "Deerskin kyūdō glove with a hard or soft thumb that holds the string.", "mk": "", "s": KYW,
   "v": [V("Mitsugake", "", "", "three-finger, for bows under about 20 kg"), V("Yotsugake", "", "", "four-finger, for heavier bows"),
         V("Ippongake", "", "", "one-finger, for beginners"), V("Morogake", "", "", "five-finger, used by Ogasawara-ryū")],
   "dt": "hard or soft thumb · deerskin"}]}

arm = {"n": "Archery arm guard", "a": "bracer", "d": "Guard strapped to the bow arm that protects it from the bowstring.",
 "t": ["leather", "plastic", "vented", "long (full forearm)"], "s": "https://www.kygunco.com/category/archery/archery-accessories/tabs-slings-and-guards",
 "x": [{"n": "Ketoh", "a": "", "d": "Navajo and Hopi leather bow guard decorated with silver and turquoise, also worn as adornment.", "mk": "", "s": BRW, "v": [], "dt": "leather · silver · turquoise"}],
 "m": [["Guardian Vented Arm Guard", "30-06 Outdoors"], ["Pro Am Arm Guard", "30-06 Outdoors"], ["Shield Arm Guard", "30-06 Outdoors"], ["Guardian Arm Guard", "October Mountain Products"]]}

sling = {"n": "Archery bow sling", "a": "", "d": "Wrist or finger strap that keeps a bow in the archer's hand at release.", "t": ["wrist sling", "finger sling", "bow sling"],
 "s": "https://www.kygunco.com/category/archery/archery-accessories/tabs-slings-and-guards"}

brands = [
 {"n": EA, "c": "United States", "f": "1922", "seg": "Professional & flagship", "kf": "arrows, quivers", "d": "Archery company founded by Doug Easton, who made the first aluminium arrow in 1941; its spin-offs became Easton's bat and hockey brands.",
  "rel": ["Easton"], "s": EGG},
 {"n": AAE, "c": "United States", "seg": "Specialist", "kf": "tabs, fletching", "d": "Archery accessory maker (AAE) of the Elite recurve tab.", "sig": ["Elite Finger Tab"], "s": AAEP},
 {"n": FW, "c": "Australia", "f": "2014", "seg": "Artisan & independent", "kf": "finger tabs", "d": "Small company of Sydney 2000 Olympic champion Simon Fairweather, making his tab.", "sig": ["Fairweather tab"], "s": FWT},
 {"n": FV, "c": "South Korea", "seg": "Specialist", "kf": "recurve tabs", "d": "Recurve archery accessory maker of the Saker tabs.", "sig": ["Saker"], "s": "knowledge"},
 {"n": BP, "c": "Germany", "seg": "Specialist", "kf": "traditional archery", "d": "Traditional-archery brand of back and side quivers and leather accessories.", "s": "knowledge"},
 {"n": "Rinehart Targets", "c": "United States", "seg": "Specialist", "kf": "3D and foam targets", "d": "Target maker whose 18-1 was Field & Stream's best overall archery target.", "s": FS},
]

w('05_00', {"kinds": [quiver, target, tab, ring, glove, arm, sling], "brands": brands, "traditions": [],
 "notes": "All 6 kinds kept; Archery thumb ring added (Wikipedia). Target: the old generic m entries (3D, bag, competition bale, foam block) became t; models from Field & Stream's target test. Archetypes: Yebira, Yazutsu, Arrow bag, Easton Elite Takedown (quiver); AAE Elite, Fairweather, Fivics Saker (tab); Manchu cylindrical and flanged rings (thumb ring); Yugake with four versions (glove); Ketoh (arm guard). Old maker 'Easton Technical Products' renamed Easton Archery. Not added: Avalon and Legacy quivers, Black Widow tabs, Saker I/II (only search snippets). No tradition entry: no retrieved page named kyūdō or traditional-archery leather workshops or centres. Bows, arrows and bow parts are in E4."})
