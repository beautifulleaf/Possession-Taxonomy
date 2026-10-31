import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/E2/agent')
from write import w
def X(n,a,d,mk,y,s,v=(),dt=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
WS="https://au.wilson.com/pages/the-history-of-the-wilson-pro-staff-tennis-racket"
PR="https://www.head.com/en/rs/stories/head-prestige-right-on-point-from-day-one/"
RA="https://www.head.com/en/rs/stories/history-of-the-head-radical-series"
racket={"n":"Tennis racket","a":"tennis racquet","d":"Strung racket made for tennis; head size, weight and balance vary.",
 "t":["wood","aluminium","graphite composite","midsize","midplus","oversize"],
 "s":"https://www.tennis-warehouse.com/catpage-BABPDRACS.html",
 "x":[
  X("Jack Kramer Autograph","Kramer Autograph","Laminated wooden racket named for Jack Kramer; the best-selling racket of all time, with over 20 million made over about 30 years.","Wilson","1948","https://tennisfame.com/hall-of-famers/inductees/jack-kramer",dt="wood frame"),
  X("Prince oversize","Prince Classic","Aluminium oversize-head racket developed by Howard Head; the first oversize racket to be patented.","Prince","1970s","https://en.wikipedia.org/wiki/Prince_Sports",dt="aluminium · oversize head"),
  X("Dunlop Max 200G","Max 200G","85 sq in widebody frame of carbon fibre and nylon, the first graphite racket made by injection moulding; played by John McEnroe and Steffi Graf.","Dunlop","","https://www.tennis-warehouse.com/learning_center/racquet_reviews/MW200Greview.html",
    [("Revelation 200g Pro","Dunlop","1997","revived the 200g name"),("Muscle Weave 200g Midplus","Dunlop","","95 sq in player's frame"),("Muscle Weave 200g Oversize","Dunlop","","108 sq in game-improvement frame")],"85 sq in · 22 mm beam · 355 g"),
  X("Wilson Pro Staff","Pro Staff","Player's racket line launched with 85, 110 and 125 sq in heads, used by Edberg, Sampras and Federer.","Wilson","1983",WS,
    [("Pro Staff 85","Wilson","1983","original 85 sq in"),("Pro Staff Classic (Six.One)","Wilson","1992","Edberg"),("Pro Staff Tour 90","Wilson","2003","Federer's first major"),("nCode nSix.One Tour","Wilson","2004","90 sq in"),("(K) Factor Six.One Tour","Wilson","2007","90 sq in"),("BLX Six.One Tour","Wilson","2010",""),("RF97 Autograph","Wilson","2014","97 sq in, Federer"),("Pro Staff v13","Wilson","2020","")],"85–100 sq in · 90 sq in Tour · 97 sq in"),
  X("Head Prestige","Prestige","Thin-beam control racket with a dense string pattern, upgraded and relaunched 15 times since 1987.","Head","1987",PR,
    [("Prestige Pro","Head","1987","original, Twaron and CAP system"),("Prestige Pro 600","Head","1991","green design"),("Prestige Tour 660","Head","1993",""),("Prestige Classic Mid","Head","1999",""),("i.Prestige","Head","2001","Ivanisevic, Kuerten"),("Liquidmetal Prestige","Head","2004",""),("Microgel Prestige","Head","2008","Safin"),("Prestige Graphene","Head","2014",""),("Prestige Auxetic","Head","2021",""),("Prestige Classic 2.0","Head","2023","limited reissue")],"Mid · Midplus · MP · Pro · Tour · S"),
  X("Head Radical","Radical","All-court racket first made for Andre Agassi, nicknamed the Bumblebee for its black and yellow design.","Head","1993",RA,
    [("Radical Tour 630 / 690","Head","1993","Agassi 'Bumblebee'"),("Ti. Radical","Head","1999","titanium"),("i.Radical","Head","2001",""),("LM Radical","Head","2003",""),("FXP Radical","Head","2005",""),("YT IG Radical","Head","2012","Andy Murray"),("Graphene Radical","Head","2014",""),("Auxetic Radical","Head","2023",""),("Auxetic 2.0 Radical","Head","2025","")],"MP · Pro · S · Oversize"),
  X("Babolat Pure Drive","Pure Drive","100 sq in power racket of about 300 g, launched in 1994 and issued in ten versions; played by Carlos Moyá and Rafael Nadal.","Babolat","1994","https://tennishead.net/iconic-rackets-the-babolat-pure-drive-the-perfect-weapon-for-club-players-and-pros/",
    [("Pure Drive","Babolat","",""),("Pure Drive Plus","Babolat","","extended length"),("Pure Drive 98","Babolat","",""),("Pure Drive 107","Babolat","",""),("Pure Drive Team","Babolat","",""),("Pure Drive Lite","Babolat","",""),("Pure Drive Super Lite","Babolat","","")],"98–107 sq in · Lite, Team, Plus"),
  X("Babolat Pure Aero","AeroPro Drive","Spin racket with an aerodynamic beam, developed with Rafael Nadal; sold as the AeroPro Drive until 2016.","Babolat","2004","https://www.tennisnerd.net/?p=21958",
    [("AeroPro Drive Original","Babolat","2004","Nadal"),("AeroPro Drive Cortex","Babolat","2007",""),("AeroPro Drive GT","Babolat","2010",""),("AeroPro Drive (Active Cortex)","Babolat","2013",""),("Pure Aero","Babolat","2016","renamed"),("Pure Aero","Babolat","2019",""),("Pure Aero VS","Babolat","","98 sq in")],""),
  X("Head Speed","Speed","Around-100 sq in tour racket line endorsed by Novak Djokovic and Alexander Zverev.","Head","","https://www.tennisnerd.net/gear/racquets/new-head-graphene-360-speed-racquets/7963",
    [("Graphene 360 Speed Pro","Head","2018","310 g"),("Graphene 360 Speed MP","Head","2018",""),("Graphene 360 Speed MP Lite","Head","2018","")],"Pro · MP · MP Lite · S"),
  X("Yonex EZONE","EZONE","Isometric-head power racket line launched in 2010; played by Naomi Osaka and Nick Kyrgios.","Yonex","2010","https://tenniscompanion.org/yonex-ezone-98/",
    [("EZONE","Yonex","2010","100 sq in"),("EZONE Xi","Yonex","2012","first EZONE 98"),("EZONE Ai","Yonex","2014",""),("EZONE DR","Yonex","2015",""),("EZONE","Yonex","2017",""),("EZONE","Yonex","2020","")],"98 · 100 · 105 · 108 sq in"),
  X("Yonex VCORE","VCORE","Isometric-head spin racket line, updated about every two years; played by Denis Shapovalov.","Yonex","2011","https://tenniscompanion.org/yonex-vcore-98/",
    [("VCORE 98 D","Yonex","2011",""),("VCORE Xi 98","Yonex","2013",""),("VCORE Si 98","Yonex","2014",""),("VCORE SV 98","Yonex","2016",""),("VCORE 98","Yonex","2018",""),("VCORE 98","Yonex","2021","")],"95 · 98 · 100 sq in")]}
string={"n":"Tennis string","a":"","d":"String sold to string a tennis racket, by the set or the reel.",
 "t":["natural gut","synthetic gut","multifilament","polyester / co-poly"],"s":"https://doittennis.com/collections/tennis-string?page=3",
 "x":[X("Babolat VS natural gut","VS Touch","Natural gut string made from cow gut in Lyon; Babolat first made gut tennis string in 1875 and the VS name came from the Four Musketeers in the 1920s.","Babolat","1875","https://www.tennis-warehouse.com/learning_center/gear_guides/tennis_string/babolat_natural_gut_the_original_tennis_string.html",dt="set · reel"),
      X("Luxilon ALU Power","Big Banger ALU Power","Polyester-based monofilament with added aluminium fibres; the reference polyester string on tour.","Luxilon","","https://luxilon.be/sport/alu-power",
        [("ALU Power 125","Luxilon","","1.25 mm"),("ALU Power 130","Luxilon","","1.30 mm"),("ALU Power 125 Rough","Luxilon","","textured"),("ALU Power 125 Soft","Luxilon","",""),("ALU Power Spin 127","Luxilon","","")],"1.15–1.30 mm · colours"),
      X("Solinco Hyper-G","Hyper-G","Shaped co-polyester monofilament made for spin.","Solinco","","https://www.tennis-warehouse.com/Hyper_GStrings/catpage-HYPERG.html",
        [("Hyper-G","Solinco","","shaped"),("Hyper-G Soft","Solinco","","softer"),("Hyper-G Round","Solinco","","round profile")],"1.05–1.30 mm")],
 "m":[["Natural Gut 120","Luxilon"],["4G","Luxilon"],["Hawk Touch","Head"],["Confidential","Solinco"],["Tour Bite","Solinco"],["NXT Control","Wilson"],["NXT Power","Wilson"],["Revolve Spin","Wilson"],["PolyTour Fire","Yonex"],["PolyTour Spin","Yonex"]],
 "r":[["PolyTour","Yonex"]]}
ball={"n":"Tennis ball","a":"","d":"Felt-covered rubber ball made for tennis; pressurised or pressureless.","t":["pressurised","pressureless","extra duty (hard court)","regular duty (clay)"],
 "s":"https://www.tennis-warehouse.com/descpage-USOC.html",
 "m":[["US Open","Wilson"],["Roland Garros Clay","Wilson"],["Extra Duty Championship","Penn"],["Coach Practice","Penn"],["Wimbledon","Slazenger"],["Fort All Court Tournament","Dunlop"],["ATP Championship","Dunlop"],["Team","Head"],["Gold Academy","Babolat"]]}
shoe={"n":"Tennis shoe","a":"","d":"Court shoe sold as a performance model with a court-specific sole for tennis. An everyday tennis-style sneaker is in Footwear.",
 "t":["all-court","clay","grass"],"s":"https://runrepeat.com/catalog/head-tennis-shoes",
 "m":[["Gel Resolution","Asics"],["Solution Speed FF","Asics"],["Court FF","Asics"],["Vapor Pro","Nike"],["GP Challenge Pro","Nike"],["Barricade","adidas"],["Adizero Ubersonic","adidas"],["Solematch Control","adidas"],["Jet Mach","Babolat"],["Hypercourt Express","K-Swiss"],["Wave Exceed Tour","Mizuno"],["Fresh Foam X CT-Rally","New Balance"]]}
bag={"n":"Racket bag","a":"racket case · racket cover","d":"Bag, case or cover that carries one or more rackets, for any racket sport.","t":["single-racket cover","racket bag","racket backpack"],
 "s":"https://www.wilson.com/en-gb/products/standard-padel-cover-wr8904300"}
def B(n,c,f,seg,kf,d,s="knowledge",**kw):
    b={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d}; b.update(kw); b["s"]=s; return b
brands=[
 B("Wilson","United States","1913","Mainstream","rackets & balls","American sporting-goods maker of tennis rackets, balls and strings.",lines=["Pro Staff","Blade","Clash","Ultra"],sig=["Wilson Pro Staff","Jack Kramer Autograph"]),
 B("Babolat","France","1875","Specialist","strings & rackets","Lyon racket-sports maker that began with natural gut string.",lines=["Pure Drive","Pure Aero","Pure Strike"],sig=["Babolat Pure Drive","Babolat Pure Aero","Babolat VS natural gut"]),
 B("Head","Austria","1950","Specialist","rackets & skis","Sports-equipment maker founded by Howard Head, known for tennis rackets and skis.",lines=["Prestige","Radical","Speed","Extreme","Boom"],sig=["Head Prestige","Head Radical","Head Speed"]),
 B("Yonex","Japan","1946","Specialist","badminton & tennis","Japanese racket maker known for isometric head shapes.",lines=["EZONE","VCORE","Percept"],sig=["Yonex EZONE","Yonex VCORE"]),
 B("Prince","United States","1970","Mainstream","oversize racket","Racket maker founded by Robert McClure as a ball-machine maker; introduced the patented oversize racket.",s="https://en.wikipedia.org/wiki/Prince_Sports",sig=["Prince oversize"]),
 B("Dunlop","United Kingdom","","Mainstream","rackets & balls","British-origin sports brand of tennis and squash rackets and balls.",sig=["Dunlop Max 200G"]),
 B("Luxilon","Belgium","","Specialist","polyester string","Belgian maker of polyester tennis strings.",s="https://luxilon.be/sport/alu-power",sig=["Luxilon ALU Power"]),
 B("Solinco","United States","","Specialist","co-poly string","American maker of tennis strings and rackets.",sig=["Solinco Hyper-G"]),
 B("Slazenger","United Kingdom","1881","Heritage manufactory","tennis balls","British sports brand, long-time supplier of Wimbledon balls."),
 B("Penn","United States","","Mainstream","tennis balls","American tennis-ball brand.")]
w('E2','02_00',{"kinds":[racket,string,ball,shoe,bag],"brands":brands,"traditions":[],
 "notes":"Tennis racket rebuilt as 11 archetypes (Kramer Autograph, Prince oversize, Max 200G, Pro Staff, Prestige, Radical, Pure Drive, Pure Aero, Speed, EZONE, VCORE); old Pure Drive models became Pure Drive versions. Strings: VS gut, ALU Power, Hyper-G as archetypes; flat list trimmed (dropped Confidential Soft, Hyper-G variants now versions, Mach-10, PolyTour Air). Balls: added Slazenger Wimbledon, Dunlop Fort/ATP, Head Team, Babolat Gold Academy (coachweb review); Wilson Sporting Goods normalised to Wilson; dropped duplicate Wilson Extra Duty Championship and Practice. Shoes trimmed 25->12 (tier). Racket case renamed Racket bag. Max 200G launch year not confirmed; Speed origin year not confirmed. Wilson Pro Staff history page 404 on wilson.com; used au.wilson.com."})
