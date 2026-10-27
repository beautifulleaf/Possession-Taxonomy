import sys; sys.path.insert(0, '/home/user/Possession-Taxonomy/rebuild/work/D2/agent')
from write import w
WP = 'https://en.wikipedia.org/wiki/'
IP = WP + 'List_of_iPad_models'
KD = WP + 'Amazon_Kindle_devices'
KB = WP + 'Kobo_Inc.'
OX = WP + 'Onyx_Boox'
SN = 'https://ewritable.net/brands/ratta-supernote/tablets/'
def V(n, mk, y='', d=''):
    v = {"n": n, "mk": mk, "y": y}
    if d: v["d"] = d
    return v
def X(n, mk, y, s, d, vs, a='', dt=''):
    x = {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": vs}
    if dt: x["dt"] = dt
    return x
A = "Apple"; S = "Samsung"; AM = "Amazon"
tab = [
 X("iPad", A, "2010", IP, "Apple's base tablet line; the 2010 original defined the modern tablet.",
   [V("iPad (1st generation)",A,"2010","original"), V("iPad 2",A,"2011"), V("iPad (3rd generation)",A,"2012","first Retina display"), V("iPad (5th generation)",A,"2017"),
    V("iPad (9th generation)",A,"2021"), V("iPad (10th generation)",A,"2022"), V("iPad (A16)",A,"2025")], dt="Wi-Fi or cellular · storage · colours"),
 X("iPad mini", A, "2012", IP, "Apple's small tablet, about 8 inches.",
   [V("iPad mini (1st generation)",A,"2012","original"), V("iPad mini 2",A,"2013"), V("iPad mini 4",A,"2015"), V("iPad mini (6th generation)",A,"2021"), V("iPad mini (A17 Pro)",A,"2024"), V("iPad mini (A20 Pro)",A,"2026")]),
 X("iPad Air", A, "2013", IP, "Apple's thin mid-range tablet line.",
   [V("iPad Air (1st generation)",A,"2013","original"), V("iPad Air 2",A,"2014"), V("iPad Air (4th generation)",A,"2020"), V("iPad Air (M2)",A,"2024","adds 13-inch"), V("iPad Air (M3)",A,"2025"), V("iPad Air (M4)",A,"2026")]),
 X("iPad Pro", A, "2015", WP+"IPad_Pro", "Apple's high-end tablet line for Pencil and keyboard work.",
   [V("iPad Pro 12.9-inch (1st generation)",A,"2015","original"), V("iPad Pro 9.7-inch",A,"2016"), V("iPad Pro 10.5-inch",A,"2017"), V("iPad Pro 11-inch (1st generation)",A,"2018","Face ID, no home button"),
    V("iPad Pro (M1)",A,"2021"), V("iPad Pro (M4)",A,"2024","OLED"), V("iPad Pro (M5)",A,"2025")], dt="11 / 12.9–13 inch · storage · cellular"),
 X("Galaxy Tab S", S, "2014", WP+"Samsung_Galaxy_Tab_S_series", "Samsung's flagship Android tablet line, with S Pen since the Tab S3.",
   [V("Galaxy Tab S 8.4 / 10.5",S,"2014","original"), V("Galaxy Tab S3",S,"2017","S Pen returns"), V("Galaxy Tab S4",S,"2018","DeX"), V("Galaxy Tab S7 / S7+",S,"2020"),
    V("Galaxy Tab S8 Ultra",S,"2022"), V("Galaxy Tab S9",S,"2023"), V("Galaxy Tab S10 Lite",S,"2025"), V("Galaxy Tab S11 / S11 Ultra",S,"2025"), V("Galaxy Tab S12",S,"2026")],
   dt="standard, Plus, Ultra, FE, Lite"),
 X("Amazon Fire", AM, "2011", WP+"Amazon_Fire", "Amazon's low-cost Fire OS tablets, formerly Kindle Fire.",
   [V("Kindle Fire",AM,"2011","original"), V("Kindle Fire HD",AM,"2012"), V("Kindle Fire HDX",AM,"2013"), V("Fire 7",AM,"2015"), V("Fire HD 10",AM,"2015"), V("Fire HD 8",AM,"2016"), V("Fire Max 11",AM,"2023")],
   a="Kindle Fire", dt="Kids editions · storage"),
]
erd = [
 X("Sony Reader", "Sony", "2006", WP+"Sony_Reader", "Sony's E Ink reader line, among the first; discontinued after 2013.",
   [V("PRS-500","Sony","2006","original"), V("PRS-505","Sony","2007"), V("PRS-700","Sony","2008","touch"), V("PRS-900","Sony","2009"), V("PRS-T1","Sony","2011"), V("PRS-T3","Sony","2013","last")]),
 X("Kindle", AM, "2007", KD, "Amazon's e-reader, the market-leading line since 2007.",
   [V("Kindle (1st generation)",AM,"2007","original"), V("Kindle 2",AM,"2009"), V("Kindle DX",AM,"2009","large screen"), V("Kindle Keyboard",AM,"2010"), V("Kindle Touch",AM,"2011","first touchscreen"),
    V("Kindle (11th generation)",AM,"2022"), V("Kindle (2024)",AM,"2024")], dt="with or without ads · storage · colours"),
 X("Kindle Paperwhite", AM, "2012", KD, "Mid-range front-lit Kindle.",
   [V("Kindle Paperwhite (1st generation)",AM,"2012","original"), V("Kindle Paperwhite (4th generation)",AM,"2018","waterproof"), V("Kindle Paperwhite (5th generation)",AM,"2021"), V("Kindle Paperwhite (6th generation)",AM,"2024")]),
 X("Kindle Voyage", AM, "2014", KD, "Premium Kindle with pressure page-turn sensors.", [V("Kindle Voyage",AM,"2014")]),
 X("Kindle Oasis", AM, "2016", KD, "Top Kindle with an asymmetric grip and page-turn buttons.",
   [V("Kindle Oasis (1st generation)",AM,"2016","original"), V("Kindle Oasis (2nd generation)",AM,"2017"), V("Kindle Oasis (3rd generation)",AM,"2019")]),
 X("Kindle Colorsoft", AM, "2024", KD, "First colour E Ink Kindle.", [V("Kindle Colorsoft Signature Edition",AM,"2024","original"), V("Kindle Colorsoft",AM,"2025")]),
 X("Nook", "Barnes & Noble", "2009", WP+"Barnes_&_Noble_Nook", "Barnes & Noble's E Ink reader line.",
   [V("Nook 1st Edition","Barnes & Noble","2009","original"), V("Nook Simple Touch","Barnes & Noble","2011"), V("Nook GlowLight","Barnes & Noble","2013"), V("Nook GlowLight Plus","Barnes & Noble","2015"),
    V("Nook GlowLight 3","Barnes & Noble","2017"), V("Nook GlowLight 4","Barnes & Noble","2021"), V("Nook GlowLight 4 Plus","Barnes & Noble","2023")]),
 X("Kobo eReader", "Kobo", "2010", KB, "Rakuten Kobo's reader family: Clara, Libra, Sage and Forma lines.",
   [V("Kobo eReader","Kobo","2010","original"), V("Forma","Kobo"), V("Clara HD","Kobo","2018"), V("Libra H2O","Kobo","2019"), V("Sage","Kobo","2021"), V("Libra 2","Kobo","2021"),
    V("Clara 2E","Kobo","2022"), V("Clara Colour","Kobo","2024"), V("Libra Colour","Kobo","2024"), V("Clara BW","Kobo")], dt="6-inch Clara · 7-inch Libra · 8-inch Sage/Forma"),
 X("PocketBook", "PocketBook", "2009", WP+"PocketBook_International", "Swiss-based maker's reader range, from the 360 to the Era and InkPad.",
   [V("PocketBook 360","PocketBook","2009"), V("PocketBook 360 Plus","PocketBook","2011"), V("InkPad","PocketBook","2014"), V("PocketBook Color","PocketBook","2020","first E Ink Kaleido reader"),
    V("Era","PocketBook","2022"), V("Verse","PocketBook","2023"), V("InkPad Color 3","PocketBook","2023")]),
 X("Cybook", "Bookeen", "2003", WP+"Bookeen", "French e-reader line from Bookeen.",
   [V("Cybook Gen1","Bookeen","2003","original"), V("Cybook Gen3","Bookeen","2007","first E Ink Cybook"), V("Cybook Opus","Bookeen","2009"), V("Cybook Orizon","Bookeen"), V("Cybook Muse","Bookeen","2014"), V("Cybook Ocean","Bookeen","2014")]),
 X("Boox reader", "Onyx", "", OX, "Onyx's Android E Ink readers.",
   [V("Boox Poke","Onyx","2018"), V("Boox Nova","Onyx","2018"), V("Boox Leaf","Onyx","2021"), V("Boox Palma","Onyx","2023","phone-sized"), V("Boox Go Color 7","Onyx","2024")]),
]
write = [
 X("Sony Digital Paper", "Sony", "2013", WP+"Sony_Digital_Paper", "Sony's large E Ink PDF and note-taking tablet.",
   [V("DPT-S1","Sony","2013","original"), V("DPT-RP1","Sony","2017"), V("DPT-CP1","Sony","2018")], a="DPT"),
 X("reMarkable", "reMarkable", "2017", WP+"ReMarkable_(manufacturer)", "Norwegian paper-like E Ink writing tablet.",
   [V("reMarkable 1","reMarkable","2017","original"), V("reMarkable 2","reMarkable","2020"), V("reMarkable Paper Pro","reMarkable","2024","colour, front-lit"), V("reMarkable Paper Pro Move","reMarkable","2025","7.3-inch")]),
 X("Supernote", "Ratta", "", SN, "Ratta's E Ink writing tablets with a ceramic-nib pen.",
   [V("Supernote A6 X","Ratta","","7.8-inch"), V("Supernote A5 X","Ratta","","10.3-inch"), V("Supernote A6 X2 Nomad","Ratta","","7.8-inch"), V("Supernote A5 X2 Manta","Ratta","","10.7-inch")]),
 X("Boox Note", "Onyx", "2016", OX, "Onyx's large Android E Ink note-taking tablets.",
   [V("Boox Max","Onyx","2016","13.3-inch"), V("Boox Note","Onyx","2018"), V("Boox Note Air","Onyx","2020"), V("Boox Tab Ultra","Onyx","2022"), V("Boox Go 10.3","Onyx","2024")]),
 X("Kindle Scribe", AM, "2022", KD, "Amazon's writing Kindle with pen.", [V("Kindle Scribe",AM,"2022","original"), V("Kindle Scribe (2024)",AM,"2024"), V("Kindle Scribe Colorsoft",AM,"2025")]),
 X("Kobo Elipsa", "Kobo", "2021", KB, "Kobo's 10.3-inch E Ink reader for notes and markup.", [V("Elipsa","Kobo","2021","original"), V("Elipsa 2E","Kobo")]),
]
kinds = [
 {"n":"Tablet","a":"slate tablet","d":"Touchscreen computer in one flat body, sold without a keyboard; an optional keyboard cover is sold separately.","s":"https://www.coolblue.nl/tablets","x":tab,
  "m":[["Galaxy Tab A11","Samsung"],["Galaxy Tab A11 Plus","Samsung"],["Xiaomi Pad 7","Xiaomi"],["Redmi Pad 2","Xiaomi"],["Idea Tab Pro Gen 2","Lenovo"],["Yoga Tab","Lenovo"],["OnePlus Pad 2 Pro","OnePlus"],["Honor MagicPad 3 Pro 13.3","Honor"]]},
 {"n":"E-reader","a":"e-book reader","d":"Device sold for reading e-books, usually on an E Ink screen.","t":["black-and-white","colour E Ink"],
  "s":"https://www.galaxus.nl/en/s1/producttype/toplist/brand/ereaders-1138/kobo-5063","x":erd,
  "m":[["WISEreader N518","Hanvon"],["Story HD","iriver"]]},
 {"n":"E-paper writing tablet","a":"e-ink notebook · digital paper","d":"E Ink device sold for taking notes and handwriting with a stylus.","s":"https://www.slashgear.com/1723406/remarkable-2-best-alternatives/","x":write,
  "m":[["Quaderno A5","Fujitsu"],["P78 Pro","Haoqing MeeBook"],["Wave Color","MobiScribe"]]},
]
K = "knowledge"
def B(n, c, f, seg, kf, d, sig, s=K, rel=None):
    b = {"n": n, "c": c, "f": f, "seg": seg, "kf": kf, "d": d, "sig": sig, "s": s}
    if rel: b["rel"] = rel
    return b
brands = [
 B("Apple","United States","1976","Premium","iPad","American maker of the iPad, iPhone and Mac.",["iPad","iPad mini","iPad Air","iPad Pro"]),
 B("Samsung","South Korea","1969","Mainstream","Galaxy Tab","South Korean electronics maker.",["Galaxy Tab S"]),
 B("Amazon","United States","1994","Mainstream","Kindle","American retailer making Kindle e-readers and Fire tablets.",["Kindle","Kindle Paperwhite","Kindle Oasis","Amazon Fire","Kindle Scribe"]),
 B("Sony","Japan","1946","Premium","electronics","Japanese electronics group; early E Ink reader maker.",["Sony Reader","Sony Digital Paper"]),
 B("Barnes & Noble","United States","1886","Own-label & retailer","Nook","American bookseller whose own-label reader is the Nook.",["Nook"]),
 B("Kobo","Canada","2009","Mainstream","e-readers","Toronto e-book company owned by Rakuten since 2012.",["Kobo eReader","Kobo Elipsa"],s=KB),
 B("PocketBook","Switzerland","2007","Specialist","e-readers","E-reader maker founded in Kyiv, based in Lugano since 2012.",["PocketBook"],s=WP+"PocketBook_International"),
 B("Bookeen","France","2003","Specialist","Cybook","Paris e-reader maker, acquired by Vivlio in 2022.",["Cybook"],s=WP+"Bookeen"),
 B("Onyx","China","","Specialist","Boox","Chinese maker of Android E Ink Boox devices.",["Boox reader","Boox Note"],s=OX),
 B("reMarkable","Norway","2013","Specialist","writing tablets","Oslo maker of paper-like E Ink writing tablets.",["reMarkable"],s=WP+"ReMarkable_(manufacturer)"),
 B("Ratta","","","Artisan & independent","Supernote","Small independent maker of Supernote writing tablets.",["Supernote"],s=SN),
]
notes = ("Long flat lists turned into line->generation archetypes. Old models attached as versions: iPad Pro, iPad mini, Galaxy Tab S10 Lite/S11/S11 Ultra, Kindle DX/Keyboard/Touch/Paperwhite/Voyage/Oasis/Colorsoft, "
 "Nook Simple Touch, Cybook Opus/Orizon, Kobo Clara BW/Colour/Forma/Libra Colour/Sage, PocketBook 360 Plus, PRS-T1, Kindle Scribe, Elipsa/Elipsa 2E, Go 10.3, Supernote Manta, DPT-CP1, reMarkable 2. "
 "Onyx 'Boox 60' dropped (not on the fetched Onyx page). Xiaomi Pad not made an archetype (no page fetched for it); Xiaomi/Lenovo/OnePlus/Honor tablets kept in m. "
 "Kindle Scribe and Kobo Elipsa sit under writing tablets; Kindle 'range' entries removed from kinds (brand register holds Amazon).")
w('D2', '01_00', {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes})
