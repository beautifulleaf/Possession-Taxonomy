import sys; sys.path.insert(0, '/home/user/Possession-Taxonomy/rebuild/work/D2/agent')
from write import w
WP = 'https://en.wikipedia.org/wiki/'
LA = WP + 'List_of_Android_smartphones'
def V(n, mk, y, d=''):
    v = {"n": n, "mk": mk, "y": y}
    if d: v["d"] = d
    return v
def X(n, mk, y, s, d, vs, a='', dt=''):
    x = {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": vs}
    if dt: x["dt"] = dt
    return x

touch = [
 X("iPhone", "Apple", "2007", WP+"List_of_iPhone_models", "Apple's touchscreen smartphone line; the 2007 original set the full-screen slab template.",
   [V("iPhone (1st generation)","Apple","2007","original"), V("iPhone 3G","Apple","2008"), V("iPhone 4","Apple","2010"), V("iPhone 4s","Apple","2011"),
    V("iPhone 5","Apple","2012"), V("iPhone 6 / 6 Plus","Apple","2014"), V("iPhone SE (1st generation)","Apple","2016"), V("iPhone X","Apple","2017","first full-screen model without home button"),
    V("iPhone 12","Apple","2020"), V("iPhone 16","Apple","2024"), V("iPhone 17 / iPhone Air","Apple","2025"), V("iPhone 17 Pro","Apple","2025")],
   dt="sizes: mini, standard, Plus/Max · Pro tiers · colours · storage"),
 X("Galaxy S", "Samsung", "2010", WP+"Samsung_Galaxy_S_series", "Samsung's flagship Android line, one generation a year since 2010.",
   [V("Galaxy S","Samsung","2010","original"), V("Galaxy S II","Samsung","2011"), V("Galaxy S III","Samsung","2012"), V("Galaxy S4","Samsung","2013"),
    V("Galaxy S7","Samsung","2016"), V("Galaxy S8","Samsung","2017"), V("Galaxy S20","Samsung","2020"), V("Galaxy S22","Samsung","2022","Ultra gains the S Pen"),
    V("Galaxy S25","Samsung","2025"), V("Galaxy S26 / S26+ / S26 Ultra","Samsung","2026")], dt="standard, plus, Ultra · FE editions · colours"),
 X("Galaxy Note", "Samsung", "2011", WP+"Samsung_Galaxy_Note", "Discontinued large-screen Samsung line that shipped with the S Pen stylus.",
   [V("Galaxy Note","Samsung","2011","original"), V("Galaxy Note II","Samsung","2012"), V("Galaxy Note 3","Samsung","2013"), V("Galaxy Note Edge","Samsung","2014"),
    V("Galaxy Note 7","Samsung","2016"), V("Galaxy Note 8","Samsung","2017"), V("Galaxy Note 9","Samsung","2018"), V("Galaxy Note 20 / 20 Ultra","Samsung","2020","last generation")]),
 X("Pixel", "Google", "2016", WP+"Google_Pixel", "Google's own Android phone line, successor to Nexus.",
   [V("Pixel / Pixel XL","Google","2016","original"), V("Pixel 2","Google","2017"), V("Pixel 3a","Google","2019","first budget a-model"), V("Pixel 6 / 6 Pro","Google","2021"),
    V("Pixel 8 / 8 Pro","Google","2023"), V("Pixel 9 / 9 Pro / 9 Pro XL","Google","2024"), V("Pixel 10 / 10 Pro / 10 Pro XL","Google","2025"), V("Pixel 11 / 11 Pro / 11 Pro XL","Google","2026")],
   dt="standard, Pro, Pro XL, a-series"),
 X("Nexus", "Google", "2010", WP+"Google_Nexus", "Google-designed stock-Android phones built by partner makers, 2010–2016.",
   [V("Nexus One","HTC","2010","original"), V("Nexus S","Samsung","2010"), V("Galaxy Nexus","Samsung","2011"), V("Nexus 4","LG","2012"), V("Nexus 5","LG","2013"),
    V("Nexus 6","Motorola","2014"), V("Nexus 5X","LG","2015"), V("Nexus 6P","Huawei","2015")]),
 X("Xperia Z", "Sony", "2013", WP+"Sony_Xperia_Z_series", "Sony's water-resistant glass-backed flagship line of 2013–2016.",
   [V("Xperia Z","Sony","2013","original"), V("Xperia Z Ultra","Sony","2013"), V("Xperia Z1","Sony","2013"), V("Xperia Z2","Sony","2014"), V("Xperia Z3","Sony","2014"),
    V("Xperia Z5","Sony","2015"), V("Xperia Z5 Premium","Sony","2015")], dt="standard, Compact, Premium/Ultra"),
 X("OnePlus numbered series", "OnePlus", "2014", WP+"List_of_OnePlus_products", "OnePlus's numbered flagship line, launched with the OnePlus One.",
   [V("OnePlus One","OnePlus","2014","original"), V("OnePlus 2","OnePlus","2015"), V("OnePlus 3","OnePlus","2016"), V("OnePlus 5","OnePlus","2017","no 4"),
    V("OnePlus 8","OnePlus","2020"), V("OnePlus 11","OnePlus","2023"), V("OnePlus 13","OnePlus","2024"), V("OnePlus 15","OnePlus","2025")], dt="standard, Pro, T editions"),
 X("Xiaomi numbered series", "Xiaomi", "2011", WP+"List_of_Xiaomi_products", "Xiaomi's numbered flagship line, formerly Mi, from the 2011 Mi 1.",
   [V("Mi 1","Xiaomi","2011","original"), V("Mi 2","Xiaomi","2012"), V("Mi 3","Xiaomi","2013"), V("Mi 6","Xiaomi","2017"), V("Mi 9","Xiaomi","2019"), V("Mi 11","Xiaomi","2021"),
    V("Xiaomi 12","Xiaomi","2021","Mi prefix dropped"), V("Xiaomi 14","Xiaomi","2023"), V("Xiaomi 15","Xiaomi","2024"), V("Xiaomi 17","Xiaomi","2025")], a="Mi series"),
 X("Huawei P / Pura", "Huawei", "2012", WP+"Huawei_P_series", "Huawei's camera-led flagship line, renamed Pura in 2024.",
   [V("Ascend P1","Huawei","2012","original"), V("Ascend P6","Huawei","2013"), V("P9","Huawei","2016","first Leica co-engineered cameras"), V("P20","Huawei","2018"), V("P30","Huawei","2019"),
    V("P40","Huawei","2020"), V("P60","Huawei","2023"), V("Pura 70","Huawei","2024"), V("Pura 80","Huawei","2025")], a="P series · Pura series"),
 X("Huawei Mate", "Huawei", "2013", WP+"Huawei_Mate_series", "Huawei's large-screen business flagship line.",
   [V("Ascend Mate","Huawei","2013","original"), V("Ascend Mate 7","Huawei","2014"), V("Mate 9","Huawei","2016"), V("Mate 20","Huawei","2018"), V("Mate 30","Huawei","2019"),
    V("Mate 40","Huawei","2020"), V("Mate 60","Huawei","2023"), V("Mate 70","Huawei","2024"), V("Mate 80","Huawei","2025")]),
 X("HTC One", "HTC", "2013", LA, "HTC's aluminium-bodied flagship line of the mid-2010s.",
   [V("HTC One (M7)","HTC","2013","original"), V("HTC One (M8)","HTC","2014"), V("HTC One M9","HTC","2015")]),
 X("Moto G", "Motorola", "2013", LA, "Motorola's long-running affordable Android line.",
   [V("Moto G (1st generation)","Motorola","2013","original"), V("Moto G (2nd generation)","Motorola","2014"), V("Moto G (3rd generation)","Motorola","2015"),
    V("Moto G4","Motorola","2016"), V("Moto G5","Motorola","2017"), V("Moto G6","Motorola","2018"), V("Moto G7","Motorola","2019"), V("Moto G 5G","Motorola","2020")]),
 X("Fairphone", "Fairphone", "2013", LA, "Modular, repairable phone made with ethically sourced materials.",
   [V("Fairphone 1","Fairphone","2013","original"), V("Fairphone 2","Fairphone","2015","first modular model"), V("Fairphone 3","Fairphone","2019"), V("Fairphone 3+","Fairphone","2020"),
    V("Fairphone 4","Fairphone","2021"), V("Fairphone 5","Fairphone","2023")]),
]
keyb = [
 X("Nokia Communicator", "Nokia", "1996", WP+"Nokia_Communicator", "Clamshell phone that opens to a wide screen and full QWERTY keyboard; the first smartphone lineage.",
   [V("Nokia 9000 Communicator","Nokia","1996","original"), V("Nokia 9110 Communicator","Nokia","1998"), V("Nokia 9210 Communicator","Nokia","2001","first Symbian device"),
    V("Nokia 9300 Communicator","Nokia","2004"), V("Nokia 9500 Communicator","Nokia","2004"), V("Nokia E90 Communicator","Nokia","2007","last Communicator")]),
 X("Palm Treo", "Palm", "2002", WP+"Palm_Treo", "Palm OS and Windows Mobile phone-organiser with a thumb keyboard, begun by Handspring.",
   [V("Treo 180","Palm","2002","original, Handspring"), V("Treo 600","Palm","2003"), V("Treo 650","Palm","2004"), V("Treo 680","Palm","2006"), V("Treo 700w","Palm","2006","first Windows Mobile Treo"),
    V("Treo 755p","Palm","2007"), V("Treo Pro","Palm","2008","last Treo")]),
 X("BlackBerry Curve", "BlackBerry", "2007", WP+"List_of_BlackBerry_products", "Mid-range BlackBerry with a full QWERTY keyboard below the screen.",
   [V("Curve 8300","BlackBerry","2007","original"), V("Curve 8310","BlackBerry","2007")]),
 X("BlackBerry Bold", "BlackBerry", "2008", WP+"List_of_BlackBerry_products", "BlackBerry's flagship keyboard phone line, the collector icon of the brand.",
   [V("Bold 9000","BlackBerry","2008","original")]),
 X("BlackBerry Q10", "BlackBerry", "2013", WP+"List_of_BlackBerry_products", "BlackBerry 10 phone with a square screen above a keyboard.", [V("Q10","BlackBerry","2013")]),
 X("BlackBerry Passport", "BlackBerry", "2014", WP+"List_of_BlackBerry_products", "Wide square-screen BlackBerry 10 phone with a three-row keyboard.", [V("Passport","BlackBerry","2014")]),
 X("BlackBerry Key", "BlackBerry", "2017", WP+"List_of_BlackBerry_products", "Android BlackBerry keyboard phones.", [V("KeyOne","BlackBerry","2017","original"), V("Key2","BlackBerry","2018")], a="KeyOne · Key2"),
 X("Motorola Q", "Motorola", "2006", WP+"Motorola_Q", "Thin Windows Mobile phone with a landscape screen and QWERTY keyboard, a BlackBerry rival.",
   [V("Motorola Q","Motorola","2006","original"), V("Motorola Q9m","Motorola","2007"), V("Motorola Q9c","Motorola","2007")]),
 X("Unihertz Titan", "Unihertz", "2019", WP+"Unihertz_Titan", "Rugged Android phones with a BlackBerry-style QWERTY keyboard.",
   [V("Titan","Unihertz","2019","original"), V("Titan Pocket","Unihertz","2021"), V("Titan Slim","Unihertz","2022"), V("Titan 2","Unihertz","2025")]),
]
flip = [
 X("Galaxy Z Flip", "Samsung", "2020", WP+"Samsung_Galaxy_Z_series", "Samsung's clamshell foldable line.",
   [V("Galaxy Z Flip","Samsung","2020","original"), V("Galaxy Z Flip3","Samsung","2021"), V("Galaxy Z Flip4","Samsung","2022"), V("Galaxy Z Flip5","Samsung","2023"),
    V("Galaxy Z Flip6","Samsung","2024"), V("Galaxy Z Flip7","Samsung","2025"), V("Galaxy Z Flip7 FE","Samsung","2025"), V("Galaxy Z Flip8","Samsung","2026")]),
 X("Motorola razr (foldable)", "Motorola", "2019", LA, "Revival of the RAZR name as a flexible-screen clamshell.",
   [V("Motorola Razr (4G)","Motorola","2019","original"), V("Motorola Razr (5G)","Motorola","2020"), V("Motorola Razr 2024","Motorola","2024"), V("Motorola Razr 2025","Motorola","2025"),
    V("razr 60","Motorola",""), V("razr 70 Ultra","Motorola","")], a="razr 2019"),
]
book = [
 X("Galaxy Z Fold", "Samsung", "2019", WP+"Samsung_Galaxy_Z_series", "Samsung's book-style foldable line, from the 2019 Galaxy Fold.",
   [V("Galaxy Fold","Samsung","2019","original"), V("Galaxy Z Fold2","Samsung","2020"), V("Galaxy Z Fold3","Samsung","2021"), V("Galaxy Z Fold5","Samsung","2023"),
    V("Galaxy Z Fold7","Samsung","2025"), V("Galaxy Z Fold8","Samsung","2026"), V("Galaxy Z Fold8 Ultra","Samsung","2026")]),
 X("Huawei Mate X", "Huawei", "2019", WP+"Huawei_Mate_series", "Huawei's foldable line, including the tri-fold Mate XT.",
   [V("Mate X","Huawei","2019","original, outward fold"), V("Mate Xs","Huawei","2020"), V("Mate X2","Huawei","2021"), V("Mate X3","Huawei","2023"), V("Mate X5","Huawei","2023"),
    V("Mate X6","Huawei","2024"), V("Mate XT","Huawei","2024","tri-fold")]),
 X("Pixel Fold", "Google", "2023", WP+"Google_Pixel", "Google's book-style foldable Pixel.",
   [V("Pixel Fold","Google","2023","original"), V("Pixel 9 Pro Fold","Google","2024"), V("Pixel 10 Pro Fold","Google","2025"), V("Pixel 11 Pro Fold","Google","2026")]),
 X("Honor Magic V", "Honor", "2022", WP+"List_of_dual-touchscreen_devices", "Honor's thin book-style foldable line.",
   [V("Magic V","Honor","2022","original"), V("Magic Vs","Honor","2022"), V("Magic V2","Honor","2023"), V("Magic V6","Honor","")]),
]
dual = [
 X("Surface Duo", "Microsoft", "2020", WP+"List_of_dual-touchscreen_devices", "Microsoft's Android phone of two 5.6-inch screens on a 360-degree hinge.",
   [V("Surface Duo","Microsoft","2020","original"), V("Surface Duo 2","Microsoft","2021")]),
 X("Kyocera Echo", "Kyocera", "2011", WP+"List_of_dual-touchscreen_devices", "Early phone with two touchscreens that open into one larger screen.", [V("Echo","Kyocera","2011")]),
 X("ZTE Axon M", "ZTE", "2017", WP+"List_of_dual-touchscreen_devices", "Folding phone with two hinged touchscreens.", [V("Axon M","ZTE","2017")]),
 X("LG Wing", "LG", "2020", WP+"List_of_dual-touchscreen_devices", "LG phone whose main screen swivels to reveal a second screen.", [V("Wing","LG","2020")]),
]
gaming = [
 X("ROG Phone", "ASUS", "2018", LA, "ASUS's Republic of Gamers phone line with cooling and shoulder triggers.",
   [V("ROG Phone","ASUS","2018","original"), V("ROG Phone II","ASUS","2019"), V("ROG Phone 3","ASUS","2020"), V("ROG Phone 5","ASUS","2021"), V("ROG Phone 6","ASUS","2022"),
    V("ROG Phone 7","ASUS","2023"), V("ROG Phone 8","ASUS","2024"), V("ROG Phone 9","ASUS","2024")]),
 X("Red Magic", "Nubia", "2019", LA, "Nubia's gaming phone line with fans and capacitive triggers.",
   [V("Red Magic 3","Nubia","2019"), V("Red Magic 5G","Nubia","2020"), V("Red Magic 6","Nubia","2021"), V("Red Magic 8 Pro","Nubia","2022"), V("Red Magic 9 Pro","Nubia","2023"),
    V("Red Magic 10 Pro","Nubia","2024"), V("Red Magic 11 Pro","Nubia","")]),
 X("Black Shark", "Black Shark", "2018", LA, "Xiaomi-backed gaming phone line.",
   [V("Black Shark","Black Shark","2018","original"), V("Black Shark 2","Black Shark","2019"), V("Black Shark 3","Black Shark","2020"), V("Black Shark 4","Black Shark","2021"), V("Black Shark 5","Black Shark","2022")]),
]
G = "https://www.gsmarena.com/ulefone_armor_9-review-2174p6.php"
rugged = [
 X("Galaxy XCover", "Samsung", "2011", LA, "Samsung's rugged phone line with replaceable battery.",
   [V("Galaxy Xcover","Samsung","2011","original"), V("Galaxy Xcover 2","Samsung","2013"), V("Galaxy Xcover 3","Samsung","2015")]),
 X("Cat S-series", "Cat", "", G, "Caterpillar-branded rugged phones, some with FLIR thermal cameras.",
   [V("CAT S61","Cat","","thermal camera"), V("CAT S62 Pro","Cat","2020")]),
 X("Ulefone Armor", "Ulefone", "", G, "Low-cost rugged Android line with large batteries.",
   [V("Armor 7","Ulefone",""), V("Armor 9","Ulefone","","FLIR thermal camera"), V("Armor 9E","Ulefone","")]),
]
kinds = [
 {"n":"Touchscreen smartphone","a":"bar smartphone · slate","d":"Touchscreen smartphone in one rigid slab-shaped body.",
  "s":"https://www.kimovil.com/en/compare/apple-iphone-17-pro,samsung-galaxy-s26-plus","x":touch,
  "m":[["OnePlus Nord 4","OnePlus"],["Poco X7 Pro","Poco"],["Poco F8 Ultra","Poco"],["iQOO 15","iQOO"]]},
 {"n":"Keyboard smartphone","a":"keyboard-bar smartphone","d":"Smartphone with a fixed or folding physical QWERTY keyboard.","s":"https://en.wikipedia.org/wiki/Form_factor_(mobile_phones)","x":keyb},
 {"n":"Flip foldable phone","a":"flip foldable smartphone","d":"Smartphone whose flexible screen folds across its width into a compact square.","s":"https://www.harveynorman.com.au/mobile-phones-wearables/mobile-phones/flip-fold-phones","x":flip},
 {"n":"Book foldable phone","a":"book foldable smartphone","d":"Smartphone whose flexible screen folds along its length and opens like a book into a tablet-sized screen.","t":["tri-fold"],
  "s":"https://www.harveynorman.com.au/mobile-phones-wearables/mobile-phones/flip-fold-phones","x":book,"m":[["razr fold","Motorola"]]},
 {"n":"Dual-screen phone","a":"dual-screen smartphone","d":"Smartphone with two rigid touchscreens joined by a hinge, used apart or as one larger screen.","s":"https://en.wikipedia.org/wiki/Form_factor_(mobile_phones)","x":dual},
 {"n":"Gaming phone","a":"gaming smartphone","d":"Smartphone sold for mobile gaming, with fast screen, cooling and shoulder triggers.","s":"https://eu.redmagic.gg/products/redmagic-11-pro","x":gaming},
 {"n":"Rugged phone","a":"rugged smartphone","d":"Smartphone built to resist water, dust and drops.","s":"https://www.doogee.com/collections/rugged-phones","x":rugged,"m":[["S88 Pro","Doogee"]]},
]
K = "knowledge"
def B(n, c, f, seg, kf, d, sig, s=K, rel=None):
    b = {"n": n, "c": c, "f": f, "seg": seg, "kf": kf, "d": d, "sig": sig, "s": s}
    if rel: b["rel"] = rel
    return b
brands = [
 B("Apple","United States","1976","Premium","iPhone","American maker of the iPhone, Mac and iPad.",["iPhone"]),
 B("Samsung","South Korea","1969","Mainstream","Galaxy phones","South Korean electronics maker; largest Android phone maker.",["Galaxy S","Galaxy Note","Galaxy Z Flip","Galaxy Z Fold","Galaxy XCover"]),
 B("Google","United States","1998","Premium","Pixel","American company behind Android, selling its own Pixel phones.",["Pixel","Nexus","Pixel Fold"]),
 B("Sony","Japan","1946","Premium","Xperia","Japanese electronics group making Xperia phones.",["Xperia Z"]),
 B("OnePlus","China","2013","Mainstream","flagship value","Chinese phone maker known for value flagships.",["OnePlus numbered series"]),
 B("Xiaomi","China","2010","Value","value phones","Chinese electronics maker; also owns Redmi and Poco.",["Xiaomi numbered series"],rel=["Black Shark"]),
 B("Huawei","China","1987","Premium","camera phones","Chinese telecoms and phone maker.",["Huawei P / Pura","Huawei Mate","Huawei Mate X"]),
 B("HTC","Taiwan","1997","Mainstream","HTC One","Taiwanese phone maker, early Android pioneer.",["HTC One"]),
 B("Motorola","United States","1928","Mainstream","razr, Moto G","American phone pioneer, now owned by Lenovo.",["Moto G","Motorola razr (foldable)","Motorola Q"]),
 B("Fairphone","Netherlands","2013","Specialist","repairable phones","Dutch maker of modular, ethically sourced phones.",["Fairphone"]),
 B("BlackBerry","Canada","1984","Specialist","keyboard phones","Canadian maker (formerly Research In Motion) of keyboard smartphones.",["BlackBerry Bold","BlackBerry Curve","BlackBerry Q10","BlackBerry Passport"]),
 B("Palm","United States","1992","Specialist","PDAs, Treo","American maker of Palm PDAs and Treo smartphones.",["Palm Treo"]),
 B("Nokia","Finland","1865","Mainstream","mobile phones","Finnish company that led the mobile-phone market in the 1990s–2000s.",["Nokia Communicator"]),
 B("Unihertz","China","","Specialist","keyboard phones","Chinese maker of small and keyboard Android phones.",["Unihertz Titan"],s=WP+"Unihertz_Titan"),
 B("Microsoft","United States","1975","Premium","Surface","American software company that made the Surface Duo.",["Surface Duo"]),
 B("Kyocera","Japan","1959","Specialist","rugged phones","Japanese electronics and ceramics maker.",["Kyocera Echo"]),
 B("ZTE","China","1985","Value","telecoms","Chinese telecoms equipment and phone maker; owns Nubia.",["ZTE Axon M"],rel=["Nubia"]),
 B("LG","South Korea","1947","Mainstream","electronics","South Korean electronics maker that left phones in 2021.",["LG Wing"]),
 B("ASUS","Taiwan","1989","Mainstream","ROG gaming","Taiwanese computer maker; ROG is its gaming brand.",["ROG Phone"]),
 B("Nubia","China","","Specialist","gaming phones","Chinese phone brand linked to ZTE, maker of Red Magic.",["Red Magic"],rel=["ZTE"]),
 B("Black Shark","China","","Specialist","gaming phones","Chinese gaming-phone brand backed by Xiaomi.",["Black Shark"],rel=["Xiaomi"]),
 B("Honor","China","2013","Mainstream","foldables","Chinese phone brand spun off from Huawei.",["Honor Magic V"],rel=["Huawei"]),
 B("Cat","United States","","Specialist","rugged phones","Caterpillar-licensed rugged phone brand.",["Cat S-series"],s=G),
 B("Ulefone","China","","Value","rugged phones","Chinese maker of low-cost rugged phones.",["Ulefone Armor"],s=G),
 B("Doogee","China","","Value","rugged phones","Chinese maker of low-cost rugged phones.",[],s=G),
]
notes = ("Flat SKU lists turned into line->generation archetypes (GSMArena axis: maker, line, generation), sourced from Wikipedia list/series pages. "
 "Old models kept as versions where they attach (iPhone 4S/17 Pro, Galaxy S26+, Z Flip/Fold, Pixel Pro Folds, Magic V6, razr 60/70 Ultra, Curve 8310, Treo 650, Titan 2, Red Magic 11 Pro); "
 "Motorola Q made an archetype. Poco X6 Pro dropped as an older duplicate of Poco X7 Pro; other unattached old models kept in m. "
 "LG dual-screen V50/G8X not on the fetched list, so LG Wing used instead. Cat brand country/maker (Bullitt licence) not confirmed, left as Caterpillar licence only. Wikidata was rate-limited (429).")
w('D2', '00_00', {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes})
