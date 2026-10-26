import json, os
NIKE_PEG = "https://about.nike.com/en/magazine/how-nike-created-the-pegasus-running-shoe"
VAPOR = "https://coachweb.com/gear/running-gear/running-shoes/nike-vaporfly"
VAM = "https://collections.vam.ac.uk/item/O1575827"
FF = "https://en.wikipedia.org/wiki/Vibram_FiveFingers"
UB = "https://en.wikipedia.org/wiki/Adidas_Ultraboost"
KAY = "https://www.complex.com/sneakers/2011/11/the-complete-history-of-the-asics-gel-kayano"
HOKA = "https://en.wikipedia.org/wiki/Hoka_(brand)"
ADR = "https://www.confluencerunning.com/pages/brooks-adrenaline-history"
KIN = "https://www.saucony.com/en/kinvara-1/61214U.html"
NB = "https://runrepeat.com/new-balance-fresh-foam-x-1080-v14"
CASC = "https://www.advnture.com/trail-running/running-shoes/a-literal-trailblazer-brooks-reissues-iconic-cascadia-1-trail-shoe-that-powered-scott-jurek-to-multiple-podiums"
SG = "https://www.irunfar.com/from-karl-meltzer-to-the-hoka-speedgoat-6-the-speedgoat-legacy"
PER = "https://www.irunfar.com/saucony-peregrine-13-review"
BUSH = "https://www.irunfar.com/la-sportiva-bushido-review"
BONDI = "https://gearpatrol.com/2019/05/22/hoka-one-one-bondi-b-revival/"
NIM = "https://www.asics.com/sg/en-sg/mk/blog/article/a-look-at-the-all-new-gel-nimbus-twenty-five"
CLIF = "https://www.fleetfeet.com/s/chicago/news/hoka-one-one-clifton-2014-irra-shoe-of-the-year"
SPX = "https://runblogger.com/2015/10/salomon-speedcross-pro-review.html"
VG = "https://birthdayshoes.com/vapor-glove-merrell-barefoot-initial-review"
VIVO = "https://en.wikipedia.org/wiki/Vivobarefoot"
ALTRA = "https://en.wikipedia.org/wiki/Altra_Running"
WHICH = "https://www.which.co.uk/reviews/outdoor-clothing/article/best-walking-shoes-aaBhy3k4D26L"
XERO = "https://www.xeroshoes.eu/xero-shoes-story/"
CR = "https://www.consumerreports.org/media-room/press-releases/2010/08/walking-shoes-asics-gel-tech-walker-neo-tops-ratings-in-mens-and-womens-categories/"
RIDE = "https://www.sneakerfreaker.com/features/saucony-progrid-ride-1-feature-spns"
ADZ = "https://endclothing.com/au/features/adidas-adizero-the-pursuit-of-fast"
GHOST = "https://www.fleetfeet.com/browse/shoes/brooks-ghost"
VJ = "https://runninginsight.com/vj-shoes"


def X(n, d, mk, y, s, v=(), a="", dt=""):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s,
            "v": [dict(zip(("n", "mk", "y", "d"), t)) for t in v], "dt": dt}


running = {
    "n": "Running shoe", "a": "road running shoe · trainer",
    "d": "Cushioned shoe for running on roads and paths.",
    "t": ["neutral", "stability", "max-cushion", "carbon-plate racer"],
    "s": "https://www.rei.com/rei-garage/b/hoka-one-one/c/mens-road-running-shoes",
    "x": [
        X("Pegasus", "Nike's long-running neutral daily trainer, first with a heel Air unit and Tomilite EVA foam.", "Nike", "1982", NIKE_PEG,
          [("Pegasus (first model)", "Nike", "1982", "introduced at the New York City Marathon; wider release 1983; heel Air unit, waffle outsole"),
           ("Air Pegasus '89", "Nike", "1989", "favourite among long-time wearers"),
           ("Pegasus 35", "Nike", "", "later generation")],
          a="Air Pegasus · Air Zoom Pegasus", dt="generation number · width · colourway"),
        X("Gel-Kayano", "ASICS's premium stability trainer for high-mileage runners, named after designer Toshikazu Kayano.", "ASICS", "1993", KAY,
          [("GEL-Kayano Trainer (TN310)", "ASICS", "1993", "original"),
           ("GEL-Kayano (TN001)", "ASICS", "2000", "introduced the IGS stability system"),
           ("GEL-Kayano XII (TN600)", "ASICS", "2006", "Space Trusstic System and Solyte foam"),
           ("GEL-Kayano 14 (TN800)", "ASICS", "2008", "memory-foam heel"),
           ("GEL-Kayano 18 (T200N)", "ASICS", "2012", "lightest Kayano to that date")],
          a="Kayano", dt="generation · reference code · colourway"),
        X("Adrenaline GTS", "Brooks's best-selling stability shoe; GTS originally meant 'Go-To Shoe'.", "Brooks", "1999", ADR,
          [("Adrenaline GTS 1", "Brooks", "1999", "original"),
           ("Adrenaline GTS 4", "Brooks", "2002", "Progressive Diagonal Rollbar"),
           ("Adrenaline GTS 19", "Brooks", "", "switch to GuideRails support"),
           ("Adrenaline GTS 25", "Brooks", "2025", "DNA LOFT v3, 10 mm drop")],
          dt="generation · width"),
        X("Gel-Nimbus", "ASICS's high-cushion neutral trainer, built for comfort on long runs.", "ASICS", "1999", NIM,
          [("GEL-Nimbus (first model)", "ASICS", "1999", "GEL cushioning for neutral runners"),
           ("GEL-Nimbus 25", "ASICS", "2023", "25th anniversary; PureGEL and FF BLAST PLUS ECO foam")],
          a="Nimbus", dt="generation · width"),
        X("Ghost", "Brooks's neutral daily trainer with DNA LOFT foam.", "Brooks", "2008", GHOST, [], dt="generation · width"),
        X("Ride", "Saucony's everyday neutral trainer line.", "Saucony", "2008", RIDE,
          [("ProGrid Ride 1", "Saucony", "2008", "originator of the line; ProGrid cushioning, webbed shank cage"),
           ("ProGrid Ride 1 reissue", "Saucony", "2026", "archive re-release")],
          dt="generation · width"),
        X("Kinvara", "Saucony's light, low-profile trainer, launched as a minimalist running shoe.", "Saucony", "2010", KIN,
          [("Kinvara 1", "Saucony", "2010", "original; later reissued as a retro style")], dt="generation"),
        X("Bondi", "Hoka's maximum-cushion road shoe; the Bondi B was the brand's first road model.", "Hoka", "", BONDI,
          [("Bondi B", "Hoka", "", "first Hoka road model; limited reissue announced 2019")], dt="generation · width"),
        X("Clifton", "Hoka's light, highly cushioned daily trainer with Meta-Rocker geometry.", "Hoka", "2014", CLIF,
          [("Clifton (first model)", "Hoka", "2014", "IRRA Shoe of the Year 2014; about 7.7 oz men's"),
           ("Clifton 6", "Hoka", "", "later generation")], dt="generation · width"),
        X("Ultraboost", "adidas running shoe line built on Boost foam with a knitted upper.", "adidas", "2015", UB,
          [("Ultraboost 1.0", "adidas", "2015", "Primeknit upper, plastic side cage"),
           ("Ultraboost ST", "adidas", "2015", "Engineered Stability sole break"),
           ("Ultraboost Uncaged", "adidas", "2016", "no side cage"),
           ("Ultraboost X", "adidas", "2017", "women's model"),
           ("Ultraboost Light", "adidas", "2023", "lighter Boost foam")],
          a="Ultra Boost", dt="version · colourway"),
        X("1080", "New Balance's soft, high-cushion neutral daily trainer.", "New Balance", "", NB,
          [("Fresh Foam X 1080 v14", "New Balance", "", "Fresh Foam X midsole, 6 mm drop"),
           ("1080 v15", "New Balance", "", "successor")],
          a="Fresh Foam 1080", dt="version · width"),
        X("Vaporfly", "Nike carbon-plate road racer with ZoomX (PEBA) foam; the first 'super shoe'.", "Nike", "2017", VAPOR,
          [("Zoom Vaporfly 4%", "Nike", "2017", "original"),
           ("Vaporfly NEXT%", "Nike", "", ""),
           ("Vaporfly NEXT% 2", "Nike", "", ""),
           ("Vaporfly 3", "Nike", "2023", "launched March 2023")],
          dt="generation · colourway"),
        X("Alphafly", "Nike carbon-plate marathon racer with forefoot Air pods, developed from the Vaporfly.", "Nike", "2020", VAM,
          [("Air Zoom Alphafly NEXT%", "Nike", "2020", "carbon plate, ZoomX foam, Atomknit upper, two forefoot Air pods"),
           ("Alphafly NEXT% 2", "Nike", "", "")],
          dt="generation · colourway"),
        X("Adizero Adios", "adidas racing line; the first Adios carried Haile Gebrselassie's 2008 Berlin world record.", "adidas", "2008", ADZ,
          [("Adizero Adios 1", "adidas", "2008", "Gebrselassie's 2:03:59 Berlin world record"),
           ("Adios OG", "adidas", "", "lifestyle reissue of the 2008 shoe"),
           ("Adizero Adios Pro Evo 1", "adidas", "", "138 g supershoe with Lightstrike Pro")],
          a="Adios", dt="generation · colourway"),
    ],
    "m": [["Mach", "Hoka"], ["Arahi", "Hoka"], ["Gaviota", "Hoka"], ["Fresh Foam X 880", "New Balance"]],
}

trail = {
    "n": "Trail running shoe", "a": "trail shoe",
    "d": "Running shoe with a lugged outsole and protection for off-road ground.",
    "t": ["rock plate", "waterproof membrane", "mud/soft-ground lugs"],
    "s": "https://scandinavianoutdoor.com/shoes/mens-shoes/mens-trail-running-footwear",
    "x": [
        X("Cascadia", "Brooks's first trail shoe, designed with Scott Jurek, with rock plate and Pivot Posting System.", "Brooks", "2004", CASC,
          [("Cascadia 1", "Brooks", "2004", "original, zero drop"), ("Cascadia 1 reissue", "Brooks", "2025", "limited re-release")],
          dt="generation · GTX or not"),
        X("Speedcross", "Salomon's deep-lugged trail shoe for mud and soft ground, with speed laces.", "Salomon", "", SPX,
          [("Speedcross 3", "Salomon", "", "long-running best seller"),
           ("Speedcross Pro", "Salomon", "", "stitch-free upper with Endofit sleeve")],
          dt="generation · GTX · colourway"),
        X("Speedgoat", "Hoka's cushioned mountain trail shoe, developed with and named after Karl 'Speedgoat' Meltzer.", "Hoka", "2015", SG,
          [("Speedgoat (first model)", "Hoka", "2015", "original"),
           ("Speedgoat 6", "Hoka", "2024", "")],
          dt="generation · GTX · width"),
        X("Peregrine", "Saucony's trail-specific (not road-derived) shoe with low stack and aggressive tread.", "Saucony", "", PER,
          [("Peregrine 13", "Saucony", "", "PWRRUN foam, forefoot rock plate, 4 mm drop")],
          dt="generation · GTX"),
        X("Bushido", "La Sportiva's narrow, firm shoe for rough technical mountain ground, with forefoot rock plate.", "La Sportiva", "", BUSH,
          [("Bushido (first model)", "La Sportiva", "", "reviewed 2014; 6 mm drop")], dt="generation"),
        X("Lone Peak", "Altra's zero-drop, foot-shaped trail shoe.", "Altra", "", ALTRA,
          [("Lone Peak 1.5", "Altra", "2013", "Runner's World trail pick"),
           ("Lone Peak Neoshell", "Altra", "2015", "weatherproof version")], dt="generation · waterproof"),
    ],
    "m": [["Challenger ATR", "Hoka"], ["Sarva", "VJ"], ["MTL Long Sky", "Merrell"], ["Hierro", "New Balance"]],
}

minimal = {
    "n": "Minimalist shoe", "a": "barefoot shoe",
    "d": "Very thin, flexible, low or zero-drop sole shaped to the foot, including five-toe designs.",
    "t": ["five-toe", "zero-drop", "wide toe box"],
    "s": "https://wildfiresports.com.au/blog/our-blog/minimalist-shoe-brand-comparison-breakdown",
    "x": [
        X("FiveFingers", "Vibram's five-toe minimalist shoe, conceived by designer Robert Fliri.", "Vibram", "2005", FF,
          [("KSO Trek", "Vibram", "", ""), ("Spyridon LS", "Vibram", "", "trail model"),
           ("V-Soul", "Vibram", "", "ballet-flat / Mary Jane style")],
          a="toe shoes", dt="model · colourway"),
        X("Vapor Glove", "Merrell's ultra-minimal barefoot shoe with a thin Vibram outsole.", "Merrell", "2013", VG,
          [("Vapor Glove", "Merrell", "2013", "3.5 mm Vibram outsole over 2 mm EVA")], dt="generation"),
        X("Evo", "Vivobarefoot running shoe, the brand's best-known model in 2019.", "Vivobarefoot", "", VIVO, [], dt=""),
        X("Instinct", "Altra's zero-drop road shoe, Runner's World Best Debut 2012.", "Altra", "2012", ALTRA, [], dt="generation"),
    ],
    "m": [["Prio", "Xero Shoes"], ["Torin", "Altra"]],
}

walking = {
    "n": "Walking shoe", "a": "",
    "d": "Cushioned, flexible shoe made for everyday walking.",
    "s": "https://www.famousfootwear.com/shoes/mens/sneakers-and-athletic-shoes/walking-shoes",
    "m": [["GEL-Tech Walker Neo", "ASICS"]],
    "r": [["GO WALK", "Skechers"]],
}

K = lambda: "knowledge"
brands = [
    {"n": "Nike", "c": "United States", "f": "1964", "seg": "Sportswear", "d": "American sportswear company; founded as Blue Ribbon Sports.", "sig": ["Pegasus", "Vaporfly", "Alphafly"], "s": "knowledge"},
    {"n": "ASICS", "c": "Japan", "f": "1949", "seg": "Running", "d": "Japanese sportswear maker, founded as Onitsuka.", "sig": ["Gel-Kayano", "Gel-Nimbus"], "s": "knowledge"},
    {"n": "Brooks", "c": "United States", "f": "1914", "seg": "Running", "d": "American running-shoe maker owned by Berkshire Hathaway.", "sig": ["Ghost", "Adrenaline GTS", "Cascadia"], "s": "knowledge"},
    {"n": "Saucony", "c": "United States", "f": "1898", "seg": "Running", "d": "American running-shoe maker.", "sig": ["Kinvara", "Ride", "Peregrine"], "s": "knowledge"},
    {"n": "Hoka", "c": "France / United States", "f": "2009", "seg": "Running", "d": "Maximal-cushion running brand founded in Annecy by Nicolas Mermoud and Jean-Luc Diard; owned by Deckers since 2013.", "sig": ["Bondi", "Clifton", "Speedgoat"], "rel": ["Salomon"], "s": HOKA},
    {"n": "adidas", "c": "Germany", "f": "1949", "seg": "Sportswear", "d": "German sportswear company.", "sig": ["Ultraboost", "Adizero Adios"], "s": "knowledge"},
    {"n": "New Balance", "c": "United States", "f": "1906", "seg": "Sportswear", "d": "American athletic-footwear maker.", "sig": ["1080"], "s": "knowledge"},
    {"n": "Salomon", "c": "France", "f": "1947", "seg": "Outdoor", "d": "French outdoor and ski equipment maker based in Annecy.", "sig": ["Speedcross"], "s": "knowledge"},
    {"n": "La Sportiva", "c": "Italy", "f": "1928", "seg": "Mountain footwear", "d": "Italian climbing and mountain-footwear maker.", "sig": ["Bushido"], "s": "knowledge"},
    {"n": "Altra", "c": "United States", "f": "2009", "seg": "Running", "d": "Zero-drop, foot-shaped running-shoe brand; owned by VF Corporation since 2018.", "sig": ["Lone Peak", "Instinct"], "s": ALTRA},
    {"n": "Vibram", "c": "Italy", "f": "1937", "seg": "Soles / minimalist footwear", "d": "Italian rubber-sole maker known for FiveFingers.", "sig": ["FiveFingers"], "rel": ["Merrell"], "s": "knowledge"},
    {"n": "Merrell", "c": "United States", "f": "1981", "seg": "Outdoor", "d": "American outdoor-footwear maker.", "sig": ["Vapor Glove"], "s": "knowledge"},
    {"n": "Vivobarefoot", "c": "United Kingdom", "seg": "Minimalist footwear", "d": "British minimalist-shoe company; its technology was developed by Terra Plana.", "sig": ["Evo"], "s": VIVO},
    {"n": "Xero Shoes", "c": "United States", "f": "2009", "seg": "Minimalist footwear", "d": "Barefoot-shoe and huarache-sandal maker founded by Steven Sashen and Lena Phoenix as Invisible Shoes.", "s": XERO},
    {"n": "VJ", "c": "Finland", "seg": "Trail / orienteering", "d": "Finnish orienteering and trail-shoe maker known for butyl-rubber outsoles.", "s": VJ},
]

notes = ("All four planned kinds kept (old ids k6, k7, k8, k9; old s retained). Hoka flat list trimmed to families: Bondi and Clifton as "
         "archetypes, Mach/Arahi/Gaviota left in m. Carbon-plate racers handled as archetypes (Vaporfly, Alphafly, Adizero Adios) plus type 'carbon-plate racer'. "
         "Walking shoe kept kind-level: GEL-Tech Walker Neo was Consumer Reports' 2010 top pick (dated); Which? 2025 survey rates brands only "
         "(Recommended: Grisport, Meindl, Scarpa, Nike ACG, Clarks, Ecco, Merrell, mostly hiking-style), so only Skechers GO WALK range added. "
         "Left out (no retrievable page; brooksrunning.com, salomon.com, roadtrailrun.com, blisterreview.com and adidas.co.uk returned 403, hoka.com could not be fetched): "
         "New Balance 880 as an archetype (kept in m), Altra Torin history, Xero models beyond Prio, Speedcross launch year, Bondi launch year, "
         "Peregrine and Bushido launch years, Ghost versions, Vaporfly NEXT% years. Merrell MTL Long Sky, New Balance Hierro and VJ Sarva kept as flat models from old data.")

out = {"kinds": [running, trail, minimal, walking], "brands": brands, "traditions": [], "notes": notes}
p = "work/A2/shelves/01_00.json"
tmp = p + ".tmp"
json.dump(out, open(tmp, "w"), ensure_ascii=False, indent=1)
os.replace(tmp, p)
print("written")
