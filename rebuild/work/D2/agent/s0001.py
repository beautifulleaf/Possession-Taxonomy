import sys; sys.path.insert(0, '/home/user/Possession-Taxonomy/rebuild/work/D2/agent')
from write import w
WP = 'https://en.wikipedia.org/wiki/'
FF = WP + 'Form_factor_(mobile_phones)'
BS = WP + 'List_of_best-selling_mobile_phones'
def V(n, mk, y='', d=''):
    v = {"n": n, "mk": mk, "y": y}
    if d: v["d"] = d
    return v
def X(n, mk, y, s, d, vs, a='', dt=''):
    x = {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": vs}
    if dt: x["dt"] = dt
    return x

keypad = [
 X("Nokia 3310", "Nokia", "2000", WP+"Nokia_3310", "Compact, famously tough monochrome Nokia bar phone with Snake II; 126 million sold.",
   [V("Nokia 3310","Nokia","2000","original"), V("Nokia 3315","Nokia","2002"), V("Nokia 3330","Nokia","","adds WAP"), V("Nokia 3390","Nokia","","North American GSM 1900"),
    V("Nokia 3310 (2017)","HMD Global","2017","colour-screen revival"), V("Nokia 3310 3G","HMD Global")], dt="Xpress-on covers · colours"),
 X("Nokia 5110", "Nokia", "1998", WP+"Nokia_5160", "Consumer GSM bar phone that introduced Xpress-on covers and Snake.",
   [V("Nokia 5110","Nokia","1998","original"), V("Nokia 5130","Nokia","","1800 MHz version"), V("Nokia 5190","Nokia","","North American 1900 MHz"), V("Nokia 6110","Nokia","","business sibling on the same platform")],
   a="5110 · 6110"),
 X("Nokia 1100", "Nokia", "2003", BS, "Basic Nokia bar phone, among the best-selling phones ever.", [V("Nokia 1100","Nokia","2003")]),
 X("N-Gage", "Nokia", "2003", WP+"N-Gage", "Nokia's 'taco'-shaped phone and handheld game system.",
   [V("N-Gage","Nokia","2003","original"), V("N-Gage QD","Nokia","2004")]),
 X("Sony Ericsson W800 Walkman", "Sony Ericsson", "2005", WP+"Sony_Ericsson_W800", "First Walkman-branded music phone, a twin of the K750 camera phone.",
   [V("W800i","Sony Ericsson","2005","original"), V("K750i","Sony Ericsson","2005","camera-phone twin"), V("W700","Sony Ericsson","2006"), V("W810","Sony Ericsson")], a="W800i · K750i"),
]
flipk = [
 X("StarTAC", "Motorola", "1996", WP+"StarTAC", "Motorola's small flip-up clamshell, the first wearable-sized flip phone hit.",
   [V("StarTAC","Motorola","1996","original"), V("StarTAC 6500","Motorola","1996"), V("StarTAC 8600","Motorola","1997"), V("StarTAC 70 / Rainbow","Motorola","1997"),
    V("StarTAC 130","Motorola","1998"), V("StarTAC 2004","Motorola","2004","Korean revival"), V("StarTAC III","Motorola","2007")]),
 X("RAZR V3", "Motorola", "2004", WP+"Motorola_Razr_V3", "Ultra-thin metal clamshell, the best-selling flip phone; spiritual successor to the StarTAC.",
   [V("RAZR V3","Motorola","2004","original"), V("RAZR V3x","Motorola","2005","3G"), V("RAZR V3i","Motorola","2005"), V("RAZR V3c","Motorola","2005","CDMA"), V("RAZR V3xx","Motorola","2006")],
   dt="colours (silver, pink, black) · special editions"),
 X("MicroTAC", "Motorola", "1989", WP+"MicroTAC", "Motorola's flip-down pocket phone that replaced the brick.",
   [V("MicroTAC 9800X","Motorola","1989","original"), V("MicroTAC Lite","Motorola","1991"), V("MicroTAC Ultra Lite","Motorola","1992"), V("MicroTAC Elite","Motorola","1994"),
    V("International 8200","Motorola","1995","GSM"), V("International 8700","Motorola","1996")]),
]
slider = [
 X("Nokia 8110", "Nokia", "1996", WP+"Nokia_8110", "Curved 'banana' phone with a sliding keypad cover; the first slider.",
   [V("Nokia 8110","Nokia","1996","original"), V("Nokia 8110i","Nokia"), V("Nokia 8810","Nokia","1998"), V("Nokia 7110","Nokia","1999","spring-loaded slide, first WAP phone"), V("Nokia 8110 4G","HMD Global","","revival")],
   a="banana phone"),
 X("Nokia N95", "Nokia", "2007", WP+"Nokia_N95", "Two-way slider multimedia phone with GPS and a 5-megapixel camera.",
   [V("N95","Nokia","2007","original"), V("N95 8GB","Nokia","2007"), V("N95-3","Nokia","2007","North American")]),
]
swivel = [
 X("Motorola V70", "Motorola", "", FF, "Round-faced phone whose cover swivels 180 degrees to show the keypad.", [V("V70","Motorola","","original"), V("V80","Motorola")]),
 X("Nokia 7370", "Nokia", "2006", FF, "Nokia fashion phone whose top half swivels to reveal the keypad.", [V("Nokia 7370","Nokia","2006")]),
]
early = [
 X("DynaTAC", "Motorola", "1983", WP+"DynaTAC", "First commercial handheld cellular phone, the original 'brick'.",
   [V("DynaTAC 8000X","Motorola","1983","original; on sale 1984"), V("DynaTAC 6000XL","Motorola"), V("DynaTAC Classic II","Motorola","1993","last model")]),
 X("Mobira Cityman", "Nokia", "1987", WP+"Mobira_Cityman_900", "Nokia-Mobira's NMT brick phone, the 'Gorba'.",
   [V("Cityman 450","Nokia","1985"), V("Cityman 900","Nokia","1987","760 g, NMT 900")]),
 X("NEC P9100", "NEC", "1988", FF, "Early NEC brick phone.", [V("P9100","NEC","1988")]),
]
lux = [
 X("Vertu Signature", "Vertu", "2002", WP+"Vertu", "Vertu's first phone: hand-built, titanium chassis, sapphire screen, ruby-bearing keys.",
   [V("Signature","Vertu","2002","original"), V("Signature Touch","Vertu","2014","Android")], dt="precious metals · leathers · gem-set editions"),
 X("Vertu Ascent", "Vertu", "2004", WP+"Vertu", "Sports-car-styled Vertu in steel and leather.", [V("Ascent","Vertu","2004","original"), V("Ascent Ti","Vertu","2007","titanium")]),
 X("Vertu Constellation", "Vertu", "2006", WP+"Vertu", "Aviation-inspired Vertu line; the Quest was the first Vertu smartphone.",
   [V("Constellation","Vertu","2006","original"), V("Constellation Quest","Vertu","2010","Symbian smartphone")]),
 X("Vertu Ti", "Vertu", "2013", WP+"Vertu", "Vertu's first Android phone, titanium case and sapphire screen.", [V("Ti","Vertu","2013"), V("Aster","Vertu","2014")]),
]
kinds = [
 {"n":"Keypad phone","a":"bar feature phone · candybar · taco","d":"Basic mobile phone in one rigid body with a keypad and no smartphone features; taco and other one-piece shapes included.",
  "s":"https://www.phonescoop.com/articles/article.php?a=19719","x":keypad,"m":[["Nokia 3300","Nokia"],["Nokia 5510","Nokia"],["Siemens S25","Siemens"]]},
 {"n":"Flip phone","a":"flip feature phone · clamshell","d":"Non-smartphone mobile phone whose body folds on a hinge (clamshell).","t":["flip-up","flip-down"],
  "s":"https://www.bestbuy.ca/en-ca/shop/best-flip-phones","x":flipk,"m":[["Backflip","Motorola"]]},
 {"n":"Slider phone","a":"","d":"Mobile phone whose screen half slides over the keypad half.","s":"https://en.wikipedia.org/wiki/Form_factor_(mobile_phones)","x":slider,
  "m":[["Torch 9800","BlackBerry"],["Droid","Motorola"],["SGH-D500","Samsung"],["Chocolate KG800","LG"]]},
 {"n":"Swivel phone","a":"","d":"Mobile phone whose screen half rotates on a pivot to show the keypad.","s":"https://en.wikipedia.org/wiki/Form_factor_(mobile_phones)","x":swivel,
  "m":[["U900","LG"],["Sidekick II","T-Mobile"]]},
 {"n":"Early mobile phone","a":"brick phone · bag phone","d":"Large handheld or bag-carried mobile phone of the 1980s and early 1990s.","s":WP+"DynaTAC","x":early},
 {"n":"Luxury phone","a":"","d":"Mobile phone made in precious materials and sold as a luxury good.","t":["hand-built luxury phone","precious-material edition of a mainstream phone"],"s":WP+"Vertu","x":lux},
]
K = "knowledge"
def B(n, c, f, seg, kf, d, sig, s=K, rel=None):
    b = {"n": n, "c": c, "f": f, "seg": seg, "kf": kf, "d": d, "sig": sig, "s": s}
    if rel: b["rel"] = rel
    return b
brands = [
 B("Nokia","Finland","1865","Mainstream","mobile phones","Finnish company that led the mobile-phone market in the 1990s–2000s.",["Nokia 3310","Nokia 8110","Nokia N95","Mobira Cityman"],rel=["HMD Global","Vertu"]),
 B("Motorola","United States","1928","Mainstream","flip phones","American phone pioneer, now owned by Lenovo.",["DynaTAC","MicroTAC","StarTAC","RAZR V3"]),
 B("Sony Ericsson","","2001","Mainstream","Walkman phones","Sony and Ericsson phone joint venture, later Sony Mobile.",["Sony Ericsson W800 Walkman"]),
 B("HMD Global","Finland","2016","Value","Nokia revivals","Finnish company selling Nokia-branded phones, including retro revivals.",[],rel=["Nokia"]),
 B("NEC","Japan","1899","Mainstream","electronics","Japanese electronics maker.",["NEC P9100"]),
 B("Vertu","United Kingdom","1998","Premium","luxury phones","Luxury phone maker founded by Nokia in England; hand-assembled in Hampshire until 2017.",["Vertu Signature","Vertu Ascent","Vertu Constellation"],s=WP+"Vertu",rel=["Nokia"]),
]
notes = ("Flat lists turned into collector-icon archetypes with versions, sourced from Wikipedia. Nokia 8110 'banana' placed in Slider phone (Wikipedia: first slider) with the 7110 as a version; "
 "Nokia 6110 attached as the business sibling of the 5110. Old 'razr' range removed from Flip phone (the 2019 razr is a flip foldable on the Smartphones shelf). "
 "Sony Ericsson K750i/W800i now one archetype. Vertu is the only luxury maker attested; precious-material editions of mainstream phones are a type. "
 "Motorola V70 year left blank (not on a fetched page). Siemens, LG, Samsung, T-Mobile models kept as flat m.")
w('D2', '00_01', {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes})
