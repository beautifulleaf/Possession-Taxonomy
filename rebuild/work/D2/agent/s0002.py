import sys; sys.path.insert(0, '/home/user/Possession-Taxonomy/rebuild/work/D2/agent')
from write import w
WP = 'https://en.wikipedia.org/wiki/'
def V(n, mk, y='', d=''):
    v = {"n": n, "mk": mk, "y": y}
    if d: v["d"] = d
    return v
def X(n, mk, y, s, d, vs, a='', dt=''):
    x = {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": vs}
    if dt: x["dt"] = dt
    return x
WE = "Western Electric"
land = [
 X("Candlestick telephone", "", "1890s–1940s", WP+"Candlestick_telephone", "Upright desk telephone with the mouthpiece on a stem and a separate hook-hung earpiece.",
   [V("#20B Desk Phone", WE, "1904", "first tube-shaft candlestick"), V("Type A handset mounting", WE, "1927", "shortened candlestick with handset cradle")],
   a="stick phone", dt="makers: Western Electric, Automatic Electric, Kellogg, Stromberg-Carlson"),
 X("Model 500", WE, "1949", WP+"Model_500_telephone", "Henry Dreyfuss-designed Bell System desk phone, the standard North American home telephone 1950–1984.",
   [V("Model 302", WE, "1936", "predecessor"), V("Model 500", WE, "1949", "original; colours from 1954"), V("Model 554", WE, "", "wall version"),
    V("Model 1500", WE, "1963", "first Touch-Tone"), V("Model 2500", WE, "1968", "Touch-Tone with * and #")], dt="rotary or push-button · desk or wall · colours"),
 X("Princess telephone", WE, "1959", WP+"Princess_telephone", "Small oval bedroom phone with a light-up dial, designed by Henry Dreyfuss.",
   [V("701B", WE, "1959", "original, no ringer"), V("702B", WE, "", "rotary with ringer"), V("1702B", WE, "", "ten-button Touch-Tone"), V("2702B", WE, "", "twelve-button"),
    V("Signature Princess", "AT&T", "1993", "last redesign")], dt="colours · lighted or plain dial"),
 X("Ericofon", "Ericsson", "1954", WP+"Ericofon", "One-piece plastic 'cobra' telephone with the dial in the base of the handset.",
   [V("Ericofon", "Ericsson", "1954", "original rotary"), V("Ericofon (North Electric)", "North Electric", "", "US version in 18 colours"), V("Ericofon touch-tone", "North Electric", "1967"),
    V("Ericofon 700", "Ericsson", "1976", "push-button, squarer")], a="cobra telephone", dt="colours (never black)"),
 X("Trimphone", "STC", "1964", WP+"Trimphone", "Lightweight British phone by Martyn Rowlands with an electronic warble ringer and glowing dial.",
   [V("712", "STC", "1964", "original"), V("722", "STC", "1971", "definitive all-figure dial"), V("766 push-button", "STC", "", "Snowdon Collection captioned 1982"), V("786 Touch-tone", "STC", "1979")],
   a="Tone Ring Illuminator Model", dt="two-tone green, grey and white"),
 X("GPO 746", "GPO", "1967", WP+"GPO_telephones", "Standard British Post Office rotary desk phone of the late 1960s–80s.",
   [V("Tele. 332", "GPO", "1937", "predecessor, Bakelite"), V("Tele. 706", "GPO", "1959", "predecessor"), V("Tele. 746", "GPO", "1967", "original"), V("Tele. 8746", "GPO", "", "New Plan socket version")],
   dt="black, red, two-tone green, two-tone grey, topaz yellow, concorde blue, ivory, brown"),
]
kinds = [
 {"n": "Landline phone", "a": "corded phone · cordless phone · DECT phone · home phone",
  "d": "Telephone for a fixed line, corded or cordless (DECT), including classic and vintage designs.",
  "t": ["corded", "cordless DECT", "DECT repeater (extends a cordless base's range)"],
  "s": "https://www.galaxus.at/en/s1/product/gigaset-desk-400-corded-bw-phones-24114536", "x": land,
  "m": [["Desk 400", "Gigaset"], ["KX-TG6761GB", "Panasonic"], ["FRITZ!DECT Repeater 100", "AVM"]]},
 {"n": "Satellite phone", "a": "satphone", "d": "Handheld phone that places calls through satellites rather than a cellular network.",
  "s": "https://satellitephonestore.com/catalog/sale/details/inmarsat-isatphone-2-satellite-phone",
  "m": [["Iridium Extreme 9575", "Iridium"], ["Iridium 9555", "Iridium"], ["IsatPhone 2", "Inmarsat"], ["X5-Touch", "Thuraya"], ["XT Lite", "Thuraya"], ["GSP-1600", "Globalstar"]]},
]
K = "knowledge"
def B(n, c, f, seg, kf, d, sig, s=K, rel=None):
    b = {"n": n, "c": c, "f": f, "seg": seg, "kf": kf, "d": d, "sig": sig, "s": s}
    if rel: b["rel"] = rel
    return b
brands = [
 B("Western Electric", "United States", "", "Heritage manufactory", "Bell telephones", "Manufacturing arm of AT&T's Bell System, maker of classic American telephones.", ["Candlestick telephone", "Model 500", "Princess telephone"], rel=["AT&T"]),
 B("Ericsson", "Sweden", "1876", "Heritage manufactory", "telephones", "Swedish telecoms company, maker of the Ericofon.", ["Ericofon"], rel=["North Electric"]),
 B("STC", "United Kingdom", "", "Heritage manufactory", "Trimphone", "Standard Telephones and Cables, British maker of the Trimphone.", ["Trimphone"], s=WP+"Trimphone"),
 B("GPO", "United Kingdom", "", "Institution & issuer", "Post Office telephones", "British General Post Office, which issued standard home telephones.", ["GPO 746"], s=WP+"GPO_telephones"),
 B("Gigaset", "Germany", "", "Mainstream", "DECT phones", "German maker of cordless DECT home phones.", []),
 B("Panasonic", "Japan", "1918", "Mainstream", "cordless phones", "Japanese electronics maker with a large cordless-phone range.", []),
 B("AVM", "Germany", "1986", "Specialist", "FRITZ!Box", "German maker of FRITZ! routers and DECT accessories.", []),
 B("Iridium", "United States", "", "Specialist", "global satphones", "Satellite network operator with a pole-to-pole low-orbit constellation and own handsets.", []),
 B("Inmarsat", "United Kingdom", "1979", "Specialist", "satellite service", "British geostationary satellite operator, maker of IsatPhone handsets.", []),
 B("Thuraya", "United Arab Emirates", "", "Specialist", "regional satphones", "UAE regional satellite phone operator.", []),
 B("Globalstar", "United States", "", "Specialist", "satellite service", "American low-orbit satellite network operator.", []),
]
notes = ("DECT repeater merged into Landline phone as a type (AVM model kept). Classic collector designs added as archetypes: candlestick, Western Electric Model 500, Princess, Ericofon, Trimphone, GPO 746. "
 "Bell Trimline not added (no fetched page). BT and Philips landline models not added (none retrieved). "
 "Satellite phone kept as tier: 4 old models plus Thuraya XT Lite and Globalstar GSP-1600 from Wikipedia 'Satellite phone' (fetched). A 2015 Scripps satphone chart 404'd.")
w('D2', '00_02', {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes})
