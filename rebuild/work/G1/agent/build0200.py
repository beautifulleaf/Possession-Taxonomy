import json, os
W='https://en.wikipedia.org/wiki/'
MH=W+'Motorcycle_helmet'; BS=W+'Bell_Sports'
RZ='https://www.revzilla.com/common-tread/the-bell-moto-3'
def X(n,mk,y,s,d,v=(),dt='',a=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
kinds=[
{"n":"Full-face helmet","a":"full face · integral helmet","d":"Motorcycle helmet with a fixed chin bar enclosing the whole head and face, with a visor that swivels up and down.",
 "t":["polycarbonate shell","fibreglass composite shell","Kevlar or carbon-fibre composite shell","round, intermediate-oval or long-oval fit","race (FIM-homologated)","sport-touring","retro"],
 "s":"https://www.revzilla.com/modular-motorcycle-helmets",
 "x":[
  X("Bell Star","Bell Sports","1968",BS,"The first full-face motorcycle helmet on the market, launched by Bell in 1968.",
    [("Star MIPS","Bell Sports","","entry-level model of the Star line with a slip-plane EPS liner")],"shell material · liner (MIPS) · graphics"),
  X("Bell Bullitt","Bell Sports","2013","https://ridermagazine.com/bell-bullitt-motorcycle-helmet-review/","Retro low-profile full-face with a wide eyeport, a modern reimagining of Bell's Star.",
    [("Bullitt (fibreglass)","Bell Sports","","fibre composite shell, magnetic leather shield tab"),("Bullitt Carbon","Bell Sports","","carbon-fibre shell version"),("Bullitt TT","Bell Sports","","white with red circles, bubble shield")],
    "fibreglass or carbon shell · bubble or flat shield · solid colours and graphics"),
  X("AGV X3000","AGV","1960s","https://bikereview.com.au/news/agv-launches-x3000-x70-helmets-oz/","Giacomo Agostini's racing full-face, developed with Gino Amisano, with a low tapered chin guard for tucking in.",
    [("X3000 (Legends reproduction)","AGV","","modern reproduction alongside the X70 open-face")],"fibreglass shell · Agostini and period race graphics"),
  X("AGV Pista GP","AGV","","https://bikereview.com.au/new-product-agv-pista-gp-r-rossi-20-years/","AGV's MotoGP racing full-face, worn by Valentino Rossi.",
    [("Pista GP R","AGV","","full carbon-fibre shell, evolution of the Pista GP"),("Pista GP R Rossi 20 Years","AGV","2018","limited replica of Rossi's 1997 sun/moon title graphic")],"carbon shell · rider replica graphics"),
  X("Arai RX-7","Arai","1977","https://www.moto.it/accessori/arai-rx-7v.html","Arai's racing full-face line; R for racing, X for full-face, 7 for the first full-face racer.",
    [("RX-7 Racing","Arai","1977","first CLC complex-laminate shell"),("RX-7R","Arai","1990","S-CLC shell"),("RX-7RR","Arai","1991","introduced the diffuser shape"),("Corsair","Arai","","later generation of the line"),("RX-7GP","Arai","","predecessor of the RX-7V"),("RX-7V","Arai","2015","VAS variable-axis visor, PB-SNC shell"),("RX-7V Evo","Arai","2022","ECE 22.06 update of the RX-7V")],
    "laminate shell generations · visor system · replica graphics"),
  X("Shoei RF series","Shoei","1984","https://ridermagazine.com/shoei-rf-1400-first-look-review/","Shoei's long-running sport-touring full-face line, introduced in 1984.",
    [("RF-1100","Shoei","","predecessor of the RF-1200"),("RF-1200","Shoei","2013","lighter, tighter-fitting generation"),("RF-1400","Shoei","2021","Multi-Ply Matrix AIM+ shell, 4% less drag than RF-1200")],"shell sizes · CWR shield · graphics"),
  X("Shoei X-Fourteen","Shoei","","https://motoiq.com/tested-shoei-x-fourteen-helmet","Shoei's race-focused full-face with a scoop-fed central top vent and a sliding visor lock.",
    [],"race and replica graphics")],
 "m":[["Supertech R10","Alpinestars"],["S3","Schuberth"],["V10","HJC"],["Skwal i3","Shark"],["Shoei Glamster","Shoei"],["Biltwell Gringo","Biltwell"],["Airstrike-X","Acerbis"]]},
{"n":"Modular helmet","a":"flip-up helmet · system helmet","d":"Motorcycle helmet whose chin bar pivots up or can be removed, combining full-face and open-face use.",
 "t":["P/J double-homologated","internal sun visor","intercom-ready"],
 "s":"https://www.revzilla.com/modular-motorcycle-helmets",
 "x":[
  X("Nolan N100","Nolan","1998","https://ridermagazine.com/nolan-n100-5-modular-helmet-gear-review/","Nolan's flip-up touring helmet line with a Lexan polycarbonate shell, introduced in 1998.",
    [("N101","Nolan","",""),("N102","Nolan","",""),("N103","Nolan","",""),("N104","Nolan","",""),("N104 EVO","Nolan","",""),("N100-5","Nolan","","more compact shell, larger vents"),("N100-6","Nolan","","successor of the N100-5")],"polycarbonate shell · N-Com intercom · graphics"),
  X("Schuberth C-series","Schuberth","1998","https://www.rad.eu/en/c/p/70300-schuberth-c5-grey.htm","Schuberth's flip-up line, from its first flip-up of 1998 to the C3 and C5.",
    [("C3","Schuberth","2008","landmark flip-up"),("C5","Schuberth","","about 1640 g, ECE 22.06 with P/J double homologation")],"shell sizes · colours"),
  X("BMW System helmet","BMW Motorrad","",MH,"BMW Motorrad's flip-up helmet line, dual-certified as full-face and open-face.",
    [("System 6","BMW Motorrad","","dual-certified full face and open face")],"")],
 "m":[["E2","Schuberth"]]},
{"n":"Open-face helmet","a":"three-quarter helmet · jet helmet","d":"Motorcycle helmet with no chin bar, covering the crown, ears, cheeks and back of the head.",
 "t":["three-quarter (jet)","half helmet (shorty, pudding basin)","with snap-on visor or bubble shield"],
 "s":"https://www.revzilla.com/modular-motorcycle-helmets",
 "x":[
  X("Bell 500","Bell Sports","1954",BS,"Bell's first production helmet: hand-laminated fibreglass shell over a foam liner.",
    [("500-TX","Bell Sports","","one of the most copied helmet designs"),("Custom 500","Bell Sports","","modern open-face successor")],"fibreglass shell · stripes and solid colours"),
  X("AGV X70","AGV","","https://bikereview.com.au/news/agv-launches-x3000-x70-helmets-oz/","Fibreglass open-face jet from AGV's Legends collection, recalling the jet helmets AGV made from the 1950s.",
    [],"fibreglass shell · period graphics"),
  X("Davida Jet","Davida","","https://www.webbikeworld.com/davida-classic-jet/","English-made open-face jet with a hand-laid fibreglass composite shell.",
    [("Classic Jet","Davida","","hand-laid fibreglass, DOT certified"),("Jet","Davida","","ECE 22.05"),("Speedster","Davida","","Nordic-standard version")],"single shell size · many colours and graphics")],
 "m":[["J2","Schuberth"],["Hedon Heroine","Hedon"]]},
{"n":"Off-road helmet","a":"motocross helmet · MX helmet · enduro helmet","d":"Full-face helmet with a long chin bar, peak and open eye port for goggles, made for motocross and enduro.",
 "t":["fibreglass composite shell","carbon-fibre shell","MIPS or rotational-impact liner"],
 "s":MH,
 "x":[
  X("Bell Moto-3","Bell Sports","2016",RZ,"Retro dirt-street full-face with a large goggle eye port and no face shield.",[],"fibreglass shell · classic colours"),
  X("Fox V-series","Fox Racing","","https://www.atv.com/parts-gear/fox-v3-helmet-everything-need-know","Fox Racing's motocross helmet family, from the V1 up to the V3.",
    [("V1","Fox Racing","",""),("V3","Fox Racing","","carbon and fibre-reinforced shell, dual-density EPS, Fluid Inside pods"),("V3 RS","Fox Racing","","adds MIPS")],"shell material · graphics"),
  X("Troy Lee Designs SE","Troy Lee Designs","","https://www.speedaddicts.com/motorcycle/troy-lee-designs-se5-carbon-helmet-team-red","Troy Lee Designs' flagship motocross helmet line.",
    [("SE5","Troy Lee Designs","","composite or carbon shell, MIPS Integra, EPP chin bar")],"composite or carbon shell · team graphics")]},
{"n":"Dual-sport helmet","a":"adventure helmet · ADV helmet","d":"Helmet combining a full-face visor with an off-road peak and chin bar, for adventure and mixed riding.",
 "t":["removable peak","goggle-compatible eye port"],
 "s":"https://transmoto.com.au/product-we-rate-arai-tour-x5-helmet/",
 "x":[
  X("Arai Tour-X","Arai","","https://transmoto.com.au/product-we-rate-arai-tour-x5-helmet/","Arai's adventure helmet with removable peak and visor that can give way to goggles.",
    [("Tour-X4","Arai","","long-running predecessor"),("Tour-X5","Arai","2024","complete redesign, ECE 22.06")],"composite shell · peak on or off"),
  X("Shoei Hornet","Shoei","","https://billyscrashhelmets.co.uk/review-shoei-hornet-adv-dual-sports-adventure-crash-helmet/","Shoei's top dual-sport helmet: fibreglass shell, full-face visor and detachable peak.",
    [("Hornet","Shoei","","original model"),("Hornet ADV","Shoei","","tool-free visor, redesigned vented peak")],"fibreglass shell · peak on or off")]}]
brands=[
 {"n":"Bell Sports","c":"United States","f":"1923","seg":"Helmets (motorcycle, cycling, racing)","d":"Californian helmet maker that began as Bell Auto Parts and built its first helmet, the 500, in 1954.","lines":["Star","Bullitt","Custom 500","Moto-3"],"sig":["Bell Star","Bell 500","Bell Bullitt"],"s":BS},
 {"n":"Shoei","c":"Japan","seg":"Premium motorcycle helmets","d":"Japanese maker specialising in motorsport helmets.","lines":["X-Fourteen","RF","Hornet","Glamster"],"sig":["Shoei RF series","Shoei X-Fourteen"],"rel":["Arai"],"s":W+"Shoei"},
 {"n":"Arai","c":"Japan","seg":"Premium motorcycle helmets","d":"Japanese helmet maker producing motorcycle helmets since 1952.","lines":["RX-7","Tour-X"],"sig":["Arai RX-7","Arai Tour-X"],"rel":["Shoei"],"s":W+"Arai_Helmet"},
 {"n":"AGV","c":"Italy","f":"1947","seg":"Motorcycle helmets","d":"Italian helmet maker founded by Gino Amisano in Valenza; part of Dainese since 2007.","lines":["Pista GP","Legends (X3000, X70)"],"sig":["AGV X3000","AGV Pista GP"],"s":W+"AGV_(helmet_manufacturer)"},
 {"n":"Schuberth","c":"Germany","f":"1922","seg":"Motorcycle and safety helmets","d":"German helmet maker founded in Braunschweig, now in Magdeburg, known for flip-up helmets.","lines":["C-series","E-series","S-series","J-series"],"sig":["Schuberth C-series"],"s":W+"Schuberth"},
 {"n":"Fox Racing","c":"United States","f":"1974","seg":"Motocross and mountain-bike gear","d":"American motocross apparel and protective-equipment brand.","lines":["V-series"],"sig":["Fox V-series"],"rel":["Troy Lee Designs"],"s":W+"Fox_Racing"},
 {"n":"Troy Lee Designs","c":"United States","f":"1981","seg":"Motocross and mountain-bike gear","d":"Californian action-sports apparel and custom-paint company.","lines":["SE"],"sig":["Troy Lee Designs SE"],"rel":["Fox Racing"],"s":W+"Troy_Lee_Designs"},
 {"n":"Alpinestars","c":"Italy","seg":"Motorsport safety equipment","d":"Motorsport and action-sports safety equipment maker based in Asolo.","lines":["Supertech"],"s":W+"Alpinestars"},
 {"n":"Acerbis","c":"Italy","seg":"Motorcycle racing gear","d":"Italian maker of motorcycle racing suits, helmets, protectors and boots.","s":W+"Acerbis"},
 {"n":"Davida","c":"United Kingdom","seg":"Classic open-face helmets","d":"English maker of hand-laid fibreglass open-face helmets.","lines":["Classic Jet","Jet","Speedster"],"sig":["Davida Jet"],"s":"https://www.webbikeworld.com/davida-classic-jet/"},
 {"n":"Nolan","c":"Italy","seg":"Motorcycle helmets","d":"Italian helmet maker known for the N100 flip-up line.","lines":["N100"],"sig":["Nolan N100"],"s":"knowledge"},
 {"n":"HJC","c":"South Korea","seg":"Motorcycle helmets","d":"South Korean helmet maker covering a large share of the mass market.","s":"knowledge"},
 {"n":"Shark","c":"France","seg":"Motorcycle helmets","d":"French motorcycle helmet maker.","s":"knowledge"},
 {"n":"BMW Motorrad","c":"Germany","seg":"Motorcycles and rider equipment","d":"BMW's motorcycle division, which sells its own System flip-up helmets.","s":"knowledge"}]
notes=("Merged 'Other motorcycle helmets' (k152) into Full-face; its open-face models (Bell Custom 500 -> Bell 500 archetype, Schuberth J2, Hedon Heroine) moved to Open-face, "
 "modular ones (Nolan N100-6 -> N100 archetype, Schuberth C5 -> C-series, E2) to Modular; AGV X3000 and Bell Bullitt became archetypes. Dropped generic placeholder models "
 "('Full face helmet', 'System helmet'). Left out unconfirmed: Bell Star 1966 date (Wikipedia gives 1968), Bell Moto-3 original 1970s date, Shoei X-Spirit naming and X-Fourteen year, "
 "TLD SE4/earlier SE, Fox V1/V2 details, Pista GP launch year, Arai Corsair/RX-7GP dates (rideapart, bennetts, MXA blocked). Shell material and fit as types. No craft traditions apply.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='work/G1/shelves/02_00.json'; os.makedirs('work/G1/shelves',exist_ok=True)
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
