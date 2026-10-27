import json, os
def w(job, obj):
    p = f'/home/user/Possession-Taxonomy/rebuild/work/E2/shelves/{job}.json'
    t = p + '.tmp'; json.dump(obj, open(t, 'w'), ensure_ascii=False, indent=1); os.replace(t, p)
def V(n, mk, y="", d=""):
    v = {"n": n, "mk": mk}
    if y: v["y"] = y
    if d: v["d"] = d
    return v
def X(n, mk, d, s, vs, y="", a="", dt="flex · curve (blade pattern) · kick point · left or right"):
    x = {"n": n, "a": a, "d": d, "mk": mk}
    if y: x["y"] = y
    x["s"] = s; x["v"] = vs; x["dt"] = dt
    return x
BH = "Bauer Hockey"; CC = "CCM Hockey"; WH = "Warrior Hockey"; TH = "TRUE Hockey"; EA = "Easton"; SH = "Sherwood Hockey"; GR = "Grays"
ISW = "https://en.wikipedia.org/wiki/Ice_hockey_stick"
BHW = "https://en.wikipedia.org/wiki/Bauer_Hockey"
CCW = "https://en.wikipedia.org/wiki/CCM_(ice_hockey)"
EGG = "https://www.geargeek.com/blog/the-rise-and-fall-of-easton-hockey-a-look-back-by-guest-blogger-james-duerr"
NHL = "https://www.geargeek.com/nhl-totals"
FHW = "https://en.wikipedia.org/wiki/Field_hockey_stick"
GIW = "https://en.wikipedia.org/wiki/Grays_International"
LST = "https://Longstreth.com/products/grays-gr10000-jumbow-composite-field-hockey-stick"

ice = {"n": "Ice hockey stick", "a": "", "d": "Long-shafted stick with a flat, curved blade, made to carry and shoot the puck in ice hockey; now mostly one-piece composite.",
 "t": ["one-piece composite", "wood", "two-piece (shaft and replaceable blade)", "senior", "intermediate", "junior", "youth"],
 "s": "https://www.purehockey.com/product/ccm-jetspeed-ft8-grip-composite-hockey-stick-senior/itm/66529-41/",
 "x": [
  X("Synergy", EA, "Easton's one-piece carbon and glass composite stick, the first one-piece to be widely adopted in the NHL.", EGG,
    [V("Synergy", EA, "2001", "first NHL user Scott Gomez"), V("Synergy 5000", EA), V("Synergy 6000", EA), V("Synergy ST", EA), V("Synergy HTX", EA), V("Synergy GX", EA, "", "last generation, after the 2014 sale")], "2001"),
  X("Vapor", BH, "Bauer's best-selling stick line, the most used in the NHL.", NHL,
    [V("Vapor APX2", BH), V("Vapor 1X Lite", BH), V("Vapor HyperLite", BH), V("Vapor HyperLite 2", BH), V("Vapor FLYLITE", BH, "", "most used NHL stick, 17.9%"), V("Vapor FLYPRO", BH), V("Vapor ADV One", BH)]),
  X("Supreme", BH, "Bauer stick line, second for Bauer in NHL use.", NHL, [V("Supreme 2S Pro", BH), V("Supreme Fuse", BH)]),
  X("Jetspeed", CC, "CCM stick line, among the most used in the NHL.", NHL,
    [V("Jetspeed FT3 Pro", CC), V("Jetspeed FT7 Pro", CC), V("Jetspeed FT8", CC), V("Jetspeed FT8 Pro", CC), V("Jetspeed FT880", CC), V("Jetspeed FT9 Pro", CC), V("Jetspeed FTW Pro", CC)]),
  X("Tacks", CC, "CCM's stick line named after its signature skate.", NHL, [V("Super Tacks AS3 Pro", CC), V("Tacks XF Pro", CC), V("Tacks XF Ghost", CC), V("Tacks Recharge Pro", CC)]),
  X("Ribcor", CC, "CCM stick line used widely in the NHL.", NHL, [V("Ribcor Trigger 9 Pro", CC), V("Ribcor Trigger 10 Pro", CC), V("Ribcor Reckoner", CC), V("Ribcor Unleashed Pro", CC)]),
  X("Nexus", BH, "Bauer's third main stick line.", NHL, [V("Nexus Geo", BH), V("Nexus Sync", BH), V("Nexus Tracer", BH)]),
  X("Alpha", WH, "Warrior's most used stick line in the NHL.", NHL, [V("Alpha DX", WH), V("Alpha LX2 Pro", WH), V("Alpha LX3 Pro", WH)]),
  X("Covert", WH, "Warrior's second stick line.", NHL, [V("Covert Deluxe", WH), V("Covert QR5 Pro", WH), V("Covert QR6 Pro", WH), V("Covert QR7 Pro", WH), V("Covert QRE 10", WH)]),
  X("Stealth", EA, "Easton's light, quick-release stick line, renewed every year.", EGG, [V("Stealth S19", EA), V("Stealth CX", EA, "", "last generation")], "2004"),
  X("Catalyst", TH, "TRUE's main stick line.", NHL, [V("Catalyst 5X3", TH), V("Catalyst 9X3", TH), V("Catalyst Nitro", TH)]),
  X("HZRDUS", TH, "TRUE's second stick line.", NHL, [V("HZRDUS Smoke", TH), V("HZRDUS 9X4", TH)])],
 "m": [["Pulse 2", BH], ["Proto2", BH], ["Vizion", CC], ["Novium 3 Pro", WH], ["Project X", TH], ["RS", EA], ["V9", EA], ["Mako", EA],
       ["Code Photon Pro", SH], ["Rekker Morph Pro", SH]]}

goalie = {"n": "Goalie stick", "a": "", "d": "Hockey stick with a widened lower shaft (paddle), a lower lie and a large blade, made for the goalie in ice hockey.",
 "t": ["composite", "wood", "paddle length"], "s": "https://www.goaliemonkey.com/equipment/sticks/sr-goalie-sticks/brand/ccm.html",
 "m": [["CCM Extreme Flex E5.9 Goalie Stick", CC], ["CCM Tacks Pro Goalie Stick", CC], ["CCM Vizion Goalie Stick", CC], ["CCM XF Pro Goalie Stick", CC]]}

puck = {"n": "Hockey puck", "a": "", "d": "Vulcanised rubber disc struck in ice hockey; mini and training pucks are variants.",
 "t": ["regulation", "mini", "training (weighted or light)", "roller or street"], "s": "https://www.purehockey.com/c/hockey-accessories-puck-balls"}
goal = {"n": "Hockey goal", "a": "hockey net", "d": "Steel-framed goal with netting set on the ice or floor for ice or street hockey; replacement net is a part.",
 "t": ["regulation steel", "street or folding", "mini"], "s": "https://www.purehockey.com/c/hockey-accessories-goals"}
pad = {"n": "Hockey shooting pad", "a": "shooting tile", "d": "Slick synthetic sheet laid on the floor for practising stickhandling and shooting off the ice.",
 "t": ["roll-up pad", "interlocking tiles"], "s": "https://www.anthem-sports.com/brands/winnwell/winnwell-ice-hockey-shooting-pad-w-handle.html",
 "m": [["Winnwell Shooting Pad with Handle", "Winnwell"]]}

field = {"n": "Field hockey stick", "a": "", "d": "Stick with a flat face and a hooked head, played on one side only, made for field hockey; most are now composite.",
 "t": ["standard bow", "mid bow", "low bow", "high, mid or low carbon", "wood", "indoor", "goalkeeper"],
 "s": "https://www.decathlon.co.uk/sports/field-hockey/hockey-sticks?from=320",
 "x": [{"n": "Hook", "a": "hook head", "d": "Grays head with an upturned toe that set the shape of the modern stick head.", "mk": GR, "y": "1983", "s": FHW,
        "v": [V("Grays Hook", GR, "1986", "original hook stick, head about 124 mm long")], "dt": "head shape · bow · weight"}],
 "m": [["AC1000 DBS", GR], ["DB10", GR], ["AC500 DynaBow-S", GR], ["AC800 Jumbow-S", GR], ["Dynabow 8", GR], ["GT 5", GR],
       ["Exa", "Dita"], ["Giga", "Dita"], ["Terra", "Dita"], ["Pro Tour 70", "Osaka"]]}

bandy = {"n": "Bandy stick", "a": "", "d": "Light slim stick with a long, curved narrow blade, made for bandy.", "s": "https://www.sportimex.com/en/ccm-bandy-stick-sr-p4.html"}

brands = [
 {"n": BH, "c": "United States", "f": "1934", "seg": "Professional & flagship", "kf": "sticks, skates", "d": "Ice hockey maker of Canadian origin, now based in Exeter, New Hampshire; the most used stick brand in the NHL.",
  "lines": ["Vapor", "Supreme", "Nexus"], "sig": ["Vapor", "Supreme", "Nexus"], "rel": [CC, WH], "s": BHW},
 {"n": CC, "c": "Canada", "f": "1899", "seg": "Professional & flagship", "kf": "skates, sticks", "d": "Montreal ice hockey maker founded in Weston, Ontario; Tacks and Jetspeed are its skate and stick lines.",
  "lines": ["Jetspeed", "Tacks", "Ribcor"], "sig": ["Jetspeed", "Tacks", "Ribcor"], "rel": [BH], "s": CCW},
 {"n": WH, "c": "United States", "seg": "Premium", "kf": "sticks, gloves", "d": "American lacrosse and ice hockey brand, third in NHL stick use.", "lines": ["Alpha", "Covert", "Novium"], "sig": ["Alpha", "Covert"], "s": "knowledge"},
 {"n": TH, "seg": "Specialist", "kf": "composite sticks", "d": "Composite stick and skate maker with the Catalyst and HZRDUS lines.", "sig": ["Catalyst", "HZRDUS"], "s": NHL},
 {"n": SH, "c": "Canada", "seg": "Heritage manufactory", "kf": "wood sticks", "d": "Stick maker that once dominated the NHL and has made a comeback.", "s": "knowledge"},
 {"n": GR, "c": "United Kingdom", "f": "1858", "seg": "Heritage manufactory", "kf": "field hockey sticks", "d": "Grays Hockey, formed in 1940 when H.J. Gray & Sons merged with stick maker J. Hazells; part of Grays International, Robertsbridge.",
  "sig": ["Hook"], "rel": ["Gray-Nicolls"], "s": GIW},
]

w('04_04', {"kinds": [ice, goalie, puck, goal, pad, field, bandy], "brands": brands, "traditions": [],
 "notes": "All 7 kinds kept. Ice hockey stick: 14 flat models + 7 ranges became 12 line archetypes (Synergy, Vapor, Supreme, Jetspeed, Tacks, Ribcor, Nexus, Alpha, Covert, Stealth, Catalyst, HZRDUS) with generations as versions from GearGeek's NHL stick totals and its Easton history; 10 flat models left. Field hockey stick: Grays Hook archetype; old Grays/Dita/Osaka models kept plus 2 current Grays. adidas, JDH and Osaka lines not added: no retrieved page named them. Easton is registered in shelf 04_03. Goalie sticks, pucks, goals, shooting pad and bandy stick stay kind-level."})
