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
A="Apple"; S="Samsung"; G="Garmin"; F="Fitbit"; P="Polar"; GO="Google"
AW=WP+"Apple_Watch"; FL=WP+"List_of_Fitbit_products"; PE=WP+"Polar_Electro"
sw = [
 X("Apple Watch", A, "2015", AW, "Apple's smartwatch line, numbered by Series; the best-selling smartwatch family.",
   [V("Apple Watch (1st generation)",A,"2015","original, later called Series 0"), V("Apple Watch Edition",A,"2015","gold case at launch"), V("Apple Watch Hermès",A,"2015","Hermès straps and faces"),
    V("Apple Watch Nike+",A,"2016"), V("Series 4",A,"2018"), V("Series 5",A,"2019"), V("Series 6",A,"2020"), V("Series 7",A,"2021"), V("Series 8",A,"2022"),
    V("Series 9",A,"2023"), V("Series 10",A,"2024"), V("Series 11",A,"2025"), V("Series 12",A,"2026")], dt="case size · aluminium, steel, titanium · GPS or cellular · bands"),
 X("Apple Watch SE", A, "2020", AW, "Lower-priced Apple Watch line.",
   [V("Apple Watch SE (1st generation)",A,"2020","original"), V("Apple Watch SE (2nd generation)",A,"2022"), V("Apple Watch SE 3",A,"2025")]),
 X("Apple Watch Ultra", A, "2022", AW, "Apple's large titanium watch for outdoor sport and diving.",
   [V("Apple Watch Ultra",A,"2022","original"), V("Apple Watch Ultra 2",A,"2023"), V("Apple Watch Ultra 3",A,"2025"), V("Apple Watch Ultra 4",A,"2026")]),
 X("Galaxy Watch", S, "2018", WP+"Samsung_Galaxy_Watch", "Samsung's round smartwatch line, successor to the Gear watches.",
   [V("Galaxy Gear",S,"","predecessor"), V("Gear S2",S), V("Gear S3",S), V("Galaxy Watch",S,"2018","first under the name"), V("Galaxy Watch Active",S), V("Galaxy Watch Active 2",S),
    V("Galaxy Watch 3",S), V("Galaxy Watch 4",S), V("Galaxy Watch 5",S), V("Galaxy Watch 6",S), V("Galaxy Watch 7",S), V("Galaxy Watch Ultra",S), V("Galaxy Watch8",S), V("Galaxy Watch 9",S), V("Galaxy Watch FE",S)],
   dt="Classic rotating bezel · Bluetooth or LTE · size"),
 X("Pebble", "Pebble", "2013", WP+"Pebble_(watch)", "Kickstarter-funded e-paper smartwatch with week-long battery; a collector icon revived in 2025.",
   [V("Pebble",  "Pebble","2013","original, plastic"), V("Pebble Steel","Pebble","2014"), V("Pebble Time","Pebble","2015","colour e-paper"), V("Pebble Time Steel","Pebble","2015"),
    V("Pebble Time Round","Pebble"), V("Pebble 2","Pebble","2016","last before 2016 closure"), V("Pebble 2 Duo","Core Devices","2025","revival"), V("Pebble Time 2","Core Devices","2025","revival")]),
 X("Pixel Watch", GO, "2022", WP+"Pixel_Watch", "Google's Wear OS smartwatch with Fitbit health tracking.",
   [V("Pixel Watch",GO,"2022","original"), V("Pixel Watch 2",GO,"2023"), V("Pixel Watch 3",GO), V("Pixel Watch 4",GO), V("Pixel Watch 5",GO)]),
 X("Fitbit Versa", F, "2018", FL, "Fitbit's square smartwatch line.",
   [V("Ionic",F,"2017","predecessor"), V("Versa",F,"2018","original"), V("Versa Lite Edition",F,"2019"), V("Versa 2",F,"2019"), V("Versa 3",F,"2020"), V("Versa 4",F,"2022")]),
 X("Fitbit Sense", F, "2020", FL, "Fitbit's health-sensor smartwatch, adding stress and ECG sensors.",
   [V("Sense",F,"2020","original"), V("Sense 2",F,"2022")]),
]
gps = [
 X("Forerunner", G, "2003", WP+"Garmin_Forerunner", "Garmin's running and triathlon GPS watch line, the long-running reference.",
   [V("Forerunner 101",G,"2003","original"), V("Forerunner 201",G,"2003"), V("Forerunner 305",G,"2006"), V("Forerunner 405",G,"2008"), V("Forerunner 310XT",G,"2009","triathlon"),
    V("Forerunner 910XT",G,"2011"), V("Forerunner 920XT",G,"2014"), V("Forerunner 935",G,"2017"), V("Forerunner 945",G,"2019"), V("Forerunner 255",G,"2022"), V("Forerunner 965",G,"2023"),
    V("Forerunner 165",G,"2024"), V("Forerunner 570",G,"2025"), V("Forerunner 970",G,"2025"), V("Forerunner 170",G,"2026")], dt="Music, Solar and LTE editions · size"),
 X("fēnix", G, "2012", WP+"Garmin_Fenix", "Garmin's steel and titanium outdoor multisport watch.",
   [V("fēnix",G,"2012","original"), V("fēnix 2",G,"2014"), V("fēnix 3",G,"2015"), V("fēnix Chronos",G,"2016","luxury variant"), V("fēnix 5",G,"2017"), V("fēnix 6 / 6 Pro",G,"2019"),
    V("fēnix 7",G,"2022"), V("fēnix 8",G,"2024"), V("fēnix E",G,"2024"), V("fēnix 8 Pro",G,"2025"), V("fēnix 9 / 9 Pro",G,"2026")], a="fenix", dt="S / standard / X sizes · Solar · Sapphire"),
 X("epix", G, "2022", WP+"Garmin_Fenix", "AMOLED-screen sibling of the fēnix.", [V("epix",G,"2022"), V("epix Pro",G,"2023")]),
 X("Enduro", G, "", "https://the5krunner.com/2026/10/06/garmin-enduro-4-specifications/", "Garmin's ultra-endurance watch built for battery life.",
   [V("Enduro",G), V("Enduro 2",G), V("Enduro 3",G,"2024"), V("Enduro 4",G,"2026")]),
 X("Instinct", G, "2018", WP+"Garmin_Forerunner", "Garmin's rugged polymer outdoor GPS watch.", [V("Instinct",G,"2018","original"), V("Instinct 2 / 2S",G,"2022")]),
 X("Suunto Ambit", "Suunto", "2012", WP+"Suunto", "Suunto's GPS outdoor watch line that followed its altimeter watches.",
   [V("Vector","Suunto","1998","forerunner: first ABC outdoor watch"), V("Core","Suunto","2007","ABC watch"), V("Ambit","Suunto","2012","original"), V("Ambit2","Suunto"), V("Ambit3","Suunto"), V("Ambit3 Vertical","Suunto","2016"),
    V("Traverse","Suunto","2015"), V("Kailash","Suunto","2015","travel GPS")]),
 X("Polar Vantage", P, "2018", PE, "Polar's multisport training watch line.",
   [V("Vantage V",P,"2018","original"), V("Vantage M",P,"2018"), V("Vantage V2",P,"2020"), V("Vantage M2",P,"2021"), V("Vantage V3",P,"2023"), V("Vantage M3",P,"2024")]),
 X("Polar Grit X", P, "2020", PE, "Polar's outdoor and trail GPS watch.",
   [V("Grit X",P,"2020","original"), V("Grit X Pro",P,"2021"), V("Grit X2 Pro",P,"2024"), V("Grit X2",P,"2025")]),
 X("Polar Pacer", P, "2022", PE, "Polar's lighter running watch.", [V("Pacer",P,"2022"), V("Pacer Pro",P,"2022")]),
 X("COROS PACE", "COROS", "2018", WP+"COROS_Wearables_Inc", "COROS's light running watch, its first GPS watch.",
   [V("PACE","COROS","2018","original"), V("PACE 2","COROS","2020"), V("PACE 3","COROS","2023"), V("PACE Pro","COROS","2024"), V("PACE 4","COROS","2025")]),
 X("COROS APEX", "COROS", "2018", WP+"COROS_Wearables_Inc", "COROS's long-battery trail watch.",
   [V("APEX","COROS","2018","original"), V("APEX Pro","COROS","2019"), V("APEX 2 / 2 Pro","COROS","2022"), V("APEX 4","COROS","2025","42 and 46 mm")]),
 X("COROS VERTIX", "COROS", "2019", WP+"COROS_Wearables_Inc", "COROS's flagship expedition watch.",
   [V("VERTIX","COROS","2019","original"), V("VERTIX 2","COROS","2021"), V("VERTIX 2S","COROS","2024")]),
]
band = [
 X("Fitbit Charge", F, "2014", FL, "Fitbit's best-known band with a small screen.",
   [V("Charge",F,"2014","original"), V("Charge HR",F,"2015","heart rate"), V("Charge 2",F,"2016"), V("Charge 3",F,"2018","SpO2 sensor"), V("Charge 4",F,"2020","built-in GPS"), V("Charge 5",F,"2021"), V("Charge 6",F,"2023")]),
 X("Fitbit Inspire", F, "2019", FL, "Fitbit's slim entry band.", [V("Inspire",F,"2019","original"), V("Inspire HR",F,"2019"), V("Inspire 3",F,"2022")]),
 X("Fitbit clip-on trackers", F, "2009", WP+"Fitbit", "Fitbit's early clip and wristband trackers that started the category.",
   [V("Tracker",F,"2009","first product"), V("Ultra",F,"2011"), V("One",F,"2012"), V("Flex",F,"2013")], a="Fitbit Tracker"),
 X("Xiaomi Smart Band", "Xiaomi", "2014", WP+"Xiaomi_Mi_Band", "Xiaomi's low-cost band, among the best-selling trackers.",
   [V("Mi Band","Xiaomi","2014","original"), V("Mi Band 1S","Xiaomi","2015","heart rate"), V("Mi Band 2","Xiaomi","2016"), V("Mi Band 3","Xiaomi"), V("Mi Band 4","Xiaomi"), V("Mi Band 5","Xiaomi"),
    V("Mi Band 6","Xiaomi"), V("Smart Band 7","Xiaomi"), V("Smart Band 8","Xiaomi"), V("Smart Band 9","Xiaomi"), V("Smart Band 10","Xiaomi")], a="Mi Band"),
]
hyb = [
 X("Withings Activité", "Withings", "", WP+"Withings", "Analogue watch with a hidden activity tracker; the first smartwatch styled as a classic watch.",
   [V("Activité","Withings","","original"), V("Steel HR","Withings","","heart rate; sold as Nokia during Nokia ownership 2016–2018")], a="Nokia Steel"),
 X("ScanWatch", "Withings", "2020", WP+"Withings", "Withings hybrid watch with ECG and blood-oxygen sensing.",
   [V("ScanWatch","Withings","2020","original"), V("ScanWatch 2","Withings","2023"), V("ScanWatch Light","Withings"), V("ScanWatch Nova","Withings")]),
 X("vívomove", G, "2016", "https://www.newatlas.com/garmin-vivomove-fitness-tracker/43175", "Garmin's analogue watch with activity tracking.",
   [V("vívomove Classic",G,"2016"), V("vívomove Premium",G,"2016","steel case"), V("vívomove Sport",G,"2016","original Sport"), V("Vivomove Sport",G,"","later model, old data")]),
]
scr = [
 X("Whoop", "Whoop", "2015", WP+"Whoop_(company)", "Subscription strap with no screen, built around recovery and strain scores.",
   [V("Whoop 1.0","Whoop","2015","original"), V("Whoop 4.0","Whoop","2021"), V("Whoop 5.0","Whoop","2025"), V("Whoop MG","Whoop","2025","medical grade")]),
 X("Polar Loop", P, "2025", PE, "Polar's screen-free band, a subscription-free rival to Whoop.", [V("Loop (Gen 2)",P,"2025")]),
 X("Amazfit Helio Strap", "Amazfit", "2025", WP+"Amazfit", "Amazfit's screen-free recovery strap.", [V("Helio Strap","Amazfit","2025")]),
]
kinds = [
 {"n":"Smartwatch","a":"","d":"Wrist device with a display that runs apps and shows phone notifications; dedicated multisport GPS watches are a separate kind.",
  "s":"https://www.att.com/buy/wearables/browse/apple_at&t_samsung_google/","x":sw,"m":[["Bounce","Garmin"]]},
 {"n":"Multisport GPS watch","a":"GPS sports watch · running watch","d":"GPS watch for running, cycling, swimming and hiking with training metrics.","t":["running","triathlon","outdoor","golf","aviation"],
  "s":"https://trackbetter.com/collections/multisport-watches","x":gps,"m":[["Approach S72","Garmin"],["D2 Mach 2 Pro","Garmin"]]},
 {"n":"Fitness band","a":"smart band · fitness tracker · activity tracker","d":"Slim wrist band with a small display that tracks activity, sleep and heart rate.",
  "s":"https://www.engadget.com/best-fitness-trackers-133053484.html?src=rss","x":band,"m":[["vivosmart 5","Garmin"]]},
 {"n":"Hybrid smartwatch","a":"smart analogue watch","d":"Analogue-hand watch with built-in sensors and phone connection.",
  "s":"https://www.wareable.com/smartwatches/best-smart-analogue-watch","x":hyb,"m":[["Instinct Crossover Solar","Garmin"]]},
 {"n":"Screenless band","a":"screen-free tracker","d":"Wrist band with sensors and no display, read through a phone app.",
  "s":"https://techradar.com/health-fitness/fitness-trackers/amazfit-helio-strap-vs-polar-loop-vs-whoop-5-0-which-should-you-buy","x":scr},
]
K="knowledge"
def B(n, c, f, seg, kf, d, sig, s=K, rel=None):
    b = {"n": n, "c": c, "f": f, "seg": seg, "kf": kf, "d": d, "sig": sig, "s": s}
    if rel: b["rel"] = rel
    return b
brands = [
 B("Apple","United States","1976","Premium","Apple Watch","American maker of the iPhone and Apple Watch.",["Apple Watch","Apple Watch SE","Apple Watch Ultra"]),
 B("Samsung","South Korea","1969","Mainstream","Galaxy Watch","South Korean electronics maker.",["Galaxy Watch"]),
 B("Google","United States","1998","Mainstream","Pixel Watch","American technology company; owns Fitbit since 2021.",["Pixel Watch"],rel=["Fitbit"]),
 B("Fitbit","United States","2007","Mainstream","fitness trackers","San Francisco tracker maker, bought by Google in 2021.",["Fitbit Charge","Fitbit Versa","Fitbit Sense","Fitbit Inspire"],s=WP+"Fitbit",rel=["Google","Pebble"]),
 B("Pebble","United States","2012","Artisan & independent","e-paper smartwatch","Palo Alto start-up whose Kickstarter watches defined early smartwatches; closed 2016, revived by Core Devices in 2025.",["Pebble"],s=WP+"Pebble_(watch)",rel=["Core Devices","Fitbit"]),
 B("Core Devices","United States","2025","Artisan & independent","Pebble revival","Company founded by Pebble's founder to revive Pebble watches.",["Pebble"],s=WP+"Pebble_(watch)",rel=["Pebble"]),
 B("Garmin","United States","1989","Professional & flagship","GPS watches","GPS maker whose Forerunner and fēnix lines lead sports watches.",["Forerunner","fēnix","Enduro","Instinct","vívomove"]),
 B("Suunto","Finland","1936","Specialist","outdoor watches","Finnish compass and outdoor watch maker, owned by Liesheng since 2022.",["Suunto Ambit"],s=WP+"Suunto"),
 B("Polar","Finland","1977","Specialist","heart-rate training","Kempele maker of the first wireless heart-rate monitor (1982).",["Polar Vantage","Polar Grit X","Polar Loop"],s=PE),
 B("COROS","China","2014","Specialist","long-battery GPS watches","Sports watch maker based in Dongguan with a US domicile.",["COROS PACE","COROS APEX","COROS VERTIX"],s=WP+"COROS_Wearables_Inc"),
 B("Xiaomi","China","2010","Value","Smart Band","Chinese electronics maker.",["Xiaomi Smart Band"]),
 B("Withings","France","2008","Premium","hybrid health watches","Issy-les-Moulineaux health-device maker, Nokia-owned 2016–2018.",["Withings Activité","ScanWatch"],s=WP+"Withings"),
 B("Whoop","United States","2012","Specialist","screenless strap","Boston maker of the subscription Whoop strap.",["Whoop"],s=WP+"Whoop_(company)"),
 B("Amazfit","China","2015","Value","budget wearables","Wearables brand of Zepp Health (formerly Huami).",["Amazfit Helio Strap"],s=WP+"Amazfit"),
]
notes = ("Smartwatch definition no longer includes GPS sports watches: Garmin D2 Mach 2 Pro and Approach S72 moved to Multisport GPS watch (m); fenix range became the fēnix archetype. "
 "Old models attached as versions: Apple Watch SE 3/Series 11/Ultra 3, Galaxy Watch8/Ultra, Enduro 4, fenix 8 Pro and fenix 9, Charge 6, Inspire 3, Smart Band 9, ScanWatch 2/Light/Nova, Vivomove Sport, Whoop 5.0, Polar Loop, Helio Strap. "
 "Apple Watch Series 1-3, Gear S years, Galaxy Watch years, Mi Band 3+ years, Enduro 1-2 years left blank (not on fetched pages). Galaxy Watch Ultra kept as a version, not a separate archetype. "
 "Garmin vivosmart and Bounce kept in m (no page fetched for a line). Approach range and Garmin D2 not made archetypes (no fetched page). Withings Activité year unknown.")
w('D2','02_00',{"kinds":kinds,"brands":brands,"traditions":[],"notes":notes})
