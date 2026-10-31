import json, os
WK="https://en.wikipedia.org/wiki/"; DT="https://deskthority.net/wiki/"
def v(n,mk="",y="",d=""): 
    o={"n":n,"mk":mk}
    if y:o["y"]=y
    if d:o["d"]=d
    return o
C="Cherry"
sw={"n":"Keyboard switches","a":"keyswitches · mechanical switches","d":"Loose keyboard switches sold in packs, chosen by feel: linear, tactile bump or audible click.",
 "t":["Linear keyboard switch","Tactile keyboard switch","Clicky keyboard switch","Silent (dampened)","Hall-effect magnetic"],
 "x":[
 {"n":"Cherry MX","a":"MX switch","d":"Cross-stem mechanical switch whose stem and footprint became the standard copied by most keyboard switches.","mk":C,"y":"c. 1985","s":WK+"Cherry_(company)",
  "v":[v("Cherry MX Black",C,"","linear, 0.60 N"),v("Cherry MX Red",C,"","linear, 0.45 N"),v("Cherry MX Brown",C,"","tactile, 0.45 N"),v("Cherry MX Blue",C,"","clicky, 0.50 N"),v("Cherry MX Clear",C,"","tactile, 0.55 N"),
       v("Cherry MX Green",C,"","clicky, 0.70 N; larger keys"),v("Cherry MX Silent Red",C,"","silent linear"),v("Cherry MX Silent Black",C,"","silent linear"),v("Cherry MX Speed Silver",C,"","linear, 1.2 mm actuation"),
       v("Cherry MX Nature White",C,"","linear, 0.55 N"),v("Cherry MX Purple",C,"","tactile, 0.35 N"),v("Cherry MX Linear Grey",C,"","linear, 0.80 N; larger keys"),v("Cherry MX Tactile Grey",C,"","tactile, 0.80 N; larger keys"),v("Cherry MX Low Profile Red",C,"","low-profile linear")],
  "dt":"linear, tactile, clicky · actuation 0.35–0.80 N · silent, speed and low-profile variants"},
 {"n":"IBM buckling spring","a":"Model M switch · Model F switch","d":"Spring that buckles under the key to snap a contact, giving the loud click of IBM keyboards.","mk":"IBM","y":"1978","s":WK+"Buckling_spring",
  "v":[v("Model F (patent 4,118,611)","IBM","1978","patent issued 1978"),v("Model M (patent 4,528,431)","IBM","","the commoner of the two"),v("IBM/Unicomp buckling spring","Unicomp","","current Model M-type production")],
  "dt":"Model F vs Model M · keyboard-integrated, not sold loose"},
 {"n":"Alps SKCL/SKCM","a":"complicated Alps · Alps Bigfoot","d":"Alps Electric slider switch family of the 1980s–90s, the commonest Alps type in computer keyboards.","mk":"Alps Alpine","y":"1983–1990s","s":DT+"Alps_SKCL/SKCM_series",
  "v":[v("SKCL Green","Alps Alpine","1983–1989","original linear"),v("SKCM Blue","Alps Alpine","1985–1988","earliest clicky"),v("SKCM Orange","Alps Alpine","1987–1991","tactile"),v("SKCM Salmon","Alps Alpine","1988–1992","tactile"),
       v("SKCM White","Alps Alpine","1988–1996","clicky"),v("SKCM Cream","Alps Alpine","","tactile, 70 gf"),v("SKCM Black","Alps Alpine","1988–1996","tactile"),v("SKCM Ivory (cream damped)","Alps Alpine","1988–1994","damped tactile"),v("SKCM White Damped","Alps Alpine","c. 1995","Apple Extended Keyboard II")],
  "dt":"linear, tactile, clicky, damped · slider colour"},
 {"n":"Topre capacitive","a":"Topre electrocapacitive","d":"Capacitive switch with a conical spring under a rubber dome, known for a soft tactile feel.","mk":"Topre","y":"late 1970s","s":WK+"Topre_Corporation",
  "v":[v("Realforce","Topre","","Topre's own keyboards"),v("Happy Hacking Keyboard","","","HHKB, uses Topre switches")],"dt":"weight · keyboard-integrated, not sold loose"},
 {"n":"Gateron KS-3","a":"Gateron","d":"Gateron's Cherry MX-compatible switch series, popular as smooth, low-cost alternatives.","mk":"Gateron","y":"","s":DT+"Gateron_KS-3_series",
  "v":[v("Gateron Yellow","Gateron","","linear, 50 gf"),v("Gateron Red","Gateron","","linear, 45 gf"),v("Gateron Black","Gateron","","linear, 50 gf"),v("Gateron Clear","Gateron","","linear, 35 gf"),v("Gateron Brown","Gateron","","tactile, 45 gf"),
       v("Gateron Blue","Gateron","","clicky, 55 gf"),v("Gateron Green","Gateron","","clicky, 80 gf"),v("Gateron White","Gateron","","old data")],"dt":"translucent (PCB-mount) or black (plate-mount) shell"},
 {"n":"Kailh BOX","a":"CPG151101F series","d":"MX-compatible switch with its contacts enclosed in a box around the stem, keeping dust out.","mk":"Kailh","y":"2017","s":DT+"Kailh_BOX",
  "v":[v("Kailh BOX White","Kailh","","clicky"),v("Kailh BOX Jade","Kailh","","clicky, with NovelKeys"),v("Kailh BOX Navy","Kailh","","clicky, heavy, with NovelKeys"),v("Kailh BOX Pale Blue","Kailh","","clicky, with NovelKeys"),
       v("Kailh BOX Royal","Kailh","","tactile, with NovelKeys"),v("Kailh BOX Burnt Orange","Kailh","","tactile, with NovelKeys"),v("Kailh BOX Dark Yellow","Kailh","","linear, with NovelKeys"),v("Kailh BOX Brown","Kailh","","tactile"),
       v("Kailh BOX Red","Kailh","","linear"),v("Kailh BOX Black","Kailh","","linear"),v("Kailh BOX Crystal","Kailh","","tactile, 62 g / 67 g"),v("Kailh BOX Pink","Kailh","","old data")],"dt":"linear, tactile, clicky · click bar · spring weight"},
 {"n":"Holy Panda","a":"","d":"Tactile hybrid of a Halo stem in a Panda housing, first assembled by enthusiasts and later sold ready-made.","mk":"","y":"by 2018","s":DT+"Holy_Panda",
  "v":[v("Original Holy Panda","","","Kailh-made Halo stem in Invyr Panda housing"),v("Drop pre-assembled Holy Panda","Drop","2018–2019","Halo stems in re-tooled housings"),v("Drop x Invyr Holy Panda","Drop"),v("Glorious Panda","Glorious","2020","clone with improved stem")],
  "dt":"stem and housing source · factory-lubed or not"},
 {"n":"Zealio","a":"Zealios","d":"Boutique tactile switch made by Gateron exclusively for Zeal PC, with purple stems by weight.","mk":"Zeal PC","y":"2015","s":DT+"Zealio",
  "v":[v("Zealio V1","Zeal PC","2015","tactile, 62–78 g"),v("Zealio V1 Redux","Zeal PC","","old data"),v("Zealio V2","Zeal PC","2018","larger tactile bump"),v("Zilent","Zeal PC","","dampened tactile"),v("Tealio","Zeal PC","","linear, 67 g"),v("Healio","Zeal PC","2018","dampened linear")],
  "dt":"weight 62, 65, 67, 78 g"},
 {"n":"NovelKeys Cream","a":"NK Cream","d":"All-POM linear switch made by Kailh for NovelKeys, known for its clack after breaking in.","mk":"NovelKeys","y":"2018","s":DT+"Novelkeys_cream","v":[],"dt":"55 g actuation · 70 g bottom-out"},
 {"n":"Wooting Lekker","a":"Lekker L60","d":"Contactless Hall-effect magnetic linear switch with adjustable actuation, for Wooting analog keyboards.","mk":"Wooting","y":"","s":"https://wooting.io/product/lekker-switch-l60-v2",
  "v":[v("Lekker L60 V2","Wooting","","40–60 gf linear, 4 mm travel")],"dt":"Hall-effect boards only"}],
 "m":[["Drop Halo Clear","Drop"],["Drop Halo True","Drop"],["Kailh Speed Silver","Kailh"],["Kailh Speed Copper","Kailh"],["Kailh Speed Bronze","Kailh"],["Logitech GL Linear","Logitech"],["Logitech GL Tactile","Logitech"],["Logitech GL Clicky","Logitech"],
      ["Logitech Romer-G Linear","Logitech"],["Logitech Romer-G Tactile","Logitech"],["Razer Optical Red","Razer"],["Razer Optical Purple","Razer"],["Razer Yellow","Razer"],["Razer Orange","Razer"],["Razer Green","Razer"],
      ["Roccat Titan Linear","Roccat"],["Roccat Titan Tactile","Roccat"],["Outemu Red","Outemu"],["Outemu Brown","Outemu"],["Outemu Blue","Outemu"]],"s":""}
kc={"n":"Keycap set","a":"keyset","d":"Matched set of keycaps for a keyboard, sold as base kits with add-on kits.","t":["Cherry profile","OEM profile","SA profile","DSA profile","DCS profile","MT3 profile","doubleshot ABS","dye-sublimated PBT"],
 "s":"https://mechanicalkeyboards.com/pages/keycap-brands",
 "x":[{"n":"GMK doubleshot ABS","a":"GMK set","d":"Cherry-profile doubleshot ABS sets from GMK, made on Cherry's original tooling and sold by group buy.","mk":"GMK","y":"2012–","s":DT+"GMK",
       "v":[v("GMK Olivia","GMK","2018","designer olivia; white with black and pink")],"dt":"base kit plus add-on kits · colourway · legends"},
      {"n":"Signature Plastics SA","a":"Spherical All","d":"Tall spherical keycap profile by Signature Plastics, later re-tooled into a sculpted shape.","mk":"Signature Plastics","y":"","s":DT+"Signature_Plastics_SA_family","v":[],"dt":"sculpted or uniform rows · doubleshot legends"},
      {"n":"MT3","a":"","d":"Deep-dish sculpted profile designed by Matt3o, inspired by IBM beam spring keycaps.","mk":"Drop","y":"2017","s":DT+"MT3_Profile","v":[v("/dev/tty","Drop","2017","first MT3 set, sold by Massdrop")],"dt":"colourway · legends"}]}
ak={"n":"Artisan keycap","a":"artisan","d":"Hand-made single keycap, often cast in resin, sold in limited runs.","t":["resin","metal","clay"],"s":"https://mechanicalkeyboards.com/collections/Artisan-Keycaps?page=1",
 "m":[["HKP Hannya Bloody Red","Hot Keys Project"],["HKP Astronskull","Hot Keys Project"],["HKP Specter","Hot Keys Project"],["HKP Raven Backlit","Hot Keys Project"],["Dwarf Factory x MK Rainbow Llama","Dwarf Factory"],["Varmilo Siamese Kitty Paw","Varmilo"]]}
pl={"n":"Keyboard plate","a":"switch plate","d":"Plate that holds the switches in a keyboard and shapes its feel and sound.","t":["aluminium","brass","FR4","polycarbonate","POM"],"s":"https://divinikey.com/products/kbdfans-65-polycarbonate-plate"}
st={"n":"Keyboard stabiliser","a":"stabs","d":"Wire stabiliser that keeps long keys such as the space bar level.","t":["plate-mounted","PCB clip-in","PCB screw-in","Costar-style"],"s":"https://divinikey.com/products/durock-v3-stabilizers-screw-in","m":[["Durock V3 Stabilizers Screw-in","Durock"]]}
cb={"n":"Coiled keyboard cable","a":"aviator cable","d":"Custom coiled USB cable for a keyboard, often with a detachable aviator connector.","t":["aviator connector","USB-C device end","USB-A or USB-C host end","paracord sleeve"],"s":"https://apos.audio/products/aviator-coiled-usb-c-cable","m":[["Aviator Coiled USB C Cable","Pwnage"]]}
K="knowledge"
brands=[
 {"n":"Cherry","c":"Germany","f":"1953","seg":"Heritage manufactory","kf":"MX switches","d":"Switch and keyboard maker founded in Illinois, now based in Auerbach, Germany; originator of the MX switch.","lines":["Cherry MX"],"sig":["Cherry MX"],"s":WK+"Cherry_(company)"},
 {"n":"IBM","c":"USA","f":"1911","seg":"Professional & flagship","kf":"Model M","d":"Computer company whose Model F and Model M keyboards made the buckling spring famous.","sig":["IBM buckling spring"],"rel":["Unicomp"],"s":K},
 {"n":"Alps Alpine","c":"Japan","f":"1948","seg":"Mainstream","kf":"Alps switches","d":"Japanese component maker (Alps Electric until 2019) whose SKCL/SKCM switches filled 1980s–90s keyboards.","sig":["Alps SKCL/SKCM"],"s":WK+"Alps_Alpine"},
 {"n":"Topre","c":"Japan","f":"1935","seg":"Premium","kf":"capacitive switches","d":"Tokyo engineering company whose capacitive switches power Realforce and HHKB keyboards.","lines":["Realforce"],"sig":["Topre capacitive"],"s":WK+"Topre_Corporation"},
 {"n":"Gateron","c":"China","seg":"Value","kf":"MX-compatible switches","d":"Huizhou switch maker known for smooth Cherry MX-compatible switches and boutique switches made for others.","sig":["Gateron KS-3"],"rel":["Zeal PC"],"s":DT+"Gateron"},
 {"n":"Kailh","c":"China","f":"1990","seg":"Mainstream","kf":"BOX switches","d":"Kaihua Electronics of Dongguan, maker of Kailh switches including the BOX series.","sig":["Kailh BOX"],"rel":["NovelKeys"],"s":DT+"Kailh"},
 {"n":"Drop","c":"USA","f":"2012","seg":"Own-label & retailer","kf":"group buys","d":"Group-buy store founded as Massdrop, renamed Drop in 2019 and bought by Corsair in 2023.","sig":["MT3"],"s":DT+"Drop"},
 {"n":"Zeal PC","c":"Canada","seg":"Artisan & independent","kf":"Zealio switches","d":"Richmond, BC enthusiast parts company selling Zealio switches, stabilisers and springs.","sig":["Zealio"],"rel":["Gateron"],"s":DT+"Zeal_PC"},
 {"n":"NovelKeys","c":"USA","seg":"Artisan & independent","kf":"switches and keycaps","d":"Enthusiast keyboard vendor known for switches made with Kailh.","sig":["NovelKeys Cream"],"rel":["Kailh"],"s":K},
 {"n":"Wooting","c":"Netherlands","seg":"Specialist","kf":"analog keyboards","d":"Dutch maker of Hall-effect analog keyboards and Lekker switches.","sig":["Wooting Lekker"],"s":K},
 {"n":"GMK","c":"Germany","f":"1992","seg":"Premium","kf":"doubleshot keycaps","d":"Wernberg-Köblitz keycap maker that took over Cherry's doubleshot tooling.","sig":["GMK doubleshot ABS"],"s":DT+"GMK"},
 {"n":"Signature Plastics","c":"USA","seg":"Specialist","kf":"SA keycaps","d":"Keycap moulder known for the SA and DSA profiles.","sig":["Signature Plastics SA"],"s":K}]
notes="All old kinds kept (k63-k66). Old flat switch models folded into Cherry MX, Gateron KS-3, Kailh BOX, Holy Panda, Zealio and buckling-spring versions; gaming-brand switches (Razer, Logitech, Roccat, Outemu, Kailh Speed) and Drop Halo stay in m. Not added for lack of a retrieved page: Gateron Ink, GMK Laser/8008/Red Samurai, ePBT, PBTfans, Keychron OSA, Jelly Key, Keycult, Cherry/Zeal/TX stabiliser models, Kailh Silent Box. Keycap profiles are types, not kinds."
out={"kinds":[sw,kc,ak,pl,st,cb],"brands":brands,"traditions":[],"notes":notes}
p="work/D1/shelves/04_01.json"; json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
