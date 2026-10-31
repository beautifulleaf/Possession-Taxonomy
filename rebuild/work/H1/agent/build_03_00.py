import json, os
W='https://en.wikipedia.org/wiki/'
SR=W+'Safety_razor'; GW=W+'Gillette'; GCA='https://gillette.ca/en-ca/perfect-shave/shaving-tips/the-history-of-the-safety-razor'
GA='https://gilletteadjustable.com/fatboy/'; SCH=W+'Schick_(razors)'; ASR=W+'American_Safety_Razor_Company'; WS=W+'Wilkinson_Sword'
def X(n,d,mk,y,s,v=(),a='',dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
de = {"n":"Double-edge safety razor","a":"DE razor · safety razor · wet-shaving kit",
 "d":"Guarded razor holding a replaceable blade with two cutting edges.",
 "t":["three-piece","two-piece","twist-to-open (butterfly, TTO)","adjustable","closed comb (safety bar)","open comb","slant head","starter or wet-shaving kit (razor, brush and soap)","chrome-plated brass or zinc","stainless steel","aluminium","titanium"],
 "s":"https://www.westcoastshaving.com/shop-brands",
 "x":[
  X("Gillette Safety Razor","The original disposable-blade double-edge razor patented by King C. Gillette.","Gillette","1901 (filed) · 1904 (patent)",SR,
    [("Old Type","Gillette","1921","original pattern renamed and sold cheaply, incl. 'Brownie' sets, after the New Improved launch"),("Original Double Ring","Gillette","","old-data model")],
    a="Old Type",dt="finish (nickel, gold) · case and set"),
  X("Gillette New Improved & Aristocrat","Redesigned three-piece razor launched ahead of the 1921 patent expiry, sold in many cases and finishes.","Gillette","1921",GW,
    [("Aristocrat","Gillette","c. 1921","long-running premium model"),("Aristocrat Jr","Gillette","","old-data model")],
    dt="finish · case"),
  X("Gillette twist-to-open razor","One-piece razor whose butterfly doors open by twisting the handle, so the head need not be detached.","Gillette","1934",GW,
    [("Rocket","Gillette","","old-data model"),("Parat","Gillette","","old-data model")],a="TTO · butterfly",dt="handle length · finish"),
  X("Gillette Tech","Three-piece Gillette razor with a simpler blade-loading head; long-lived worldwide.","Gillette","1938",'https://www.vintage-razor.com/gillette-tech/',
    [("Tech Military","Gillette","1938","USA"),("Contract Tech","Gillette","1939","USA"),("Tech Traveller","Gillette","1958","England"),("G1000 Tech","Gillette","1970s","plastic-handled"),("Modern Tech-style razor","Gillette","current","sold as 7 O'Clock, Nacet, Minora, Rubie and others (per Gillette article)")],
    dt="fat or thin handle · open or closed comb · country of make"),
  X("Gillette Super Speed","Twist-to-open Gillette razor; 1955 versions coded closeness by handle-tip colour.","Gillette","1947",GW,
    [("Colour-tip Super Speed","Gillette","1955","versions shaving more or less closely, marked by tip colour"),("Black-handle Super Speed","Gillette","1966–1988","black resin-coated handle"),("Knack","Gillette","1966–1975","longer plastic handle; in Europe Slim Twist and G2000")],
    a="Superspeed",dt="tip colour · date code"),
  X("Gillette 195 Adjustable (Fatboy)","Gillette's first adjustable twist-to-open razor with a nine-position dial.","Gillette","1958–1962",GA,
    [("Version 1","Gillette","1958","nickel collar, black band"),("Version 2","Gillette","c. 1959","blued collar, no band"),("Version 4","Gillette","c. 1961","crimped cap, no service notches")],
    a="Fat Boy · 195",dt="date code (D-3 to H-1) · dial 1–9 · 79 g"),
  X("Gillette Slim Adjustable","Longer, slimmer, lighter adjustable that followed the Fatboy.","Gillette","1962",GA,
    [("Aristocrat Slim","Gillette","","gold-tone companion model")],a="Slim",dt="date code · dial knurling"),
  X("Merkur 34C HD","Compact two-piece closed-comb razor with a heavy brass handle, a standard beginner pick.","Merkur","",'https://merkurshave.com/merkur-de-safety-razor-34c-hd-straight-guard-43mm-german-34101/',
    [("34C HD","Merkur","","chrome, 78 g, 34101"),("34G HD","Merkur","","gold"),("34 MATT HD","Merkur","","matte chrome"),("34 INOX Special Edition 1896","Merkur","","stainless steel")],
    a="34C Heavy Duty · Merkur 34",dt="finish · 81 mm length"),
  X("Merkur 42C '1904'","Merkur straight-guard razor in the early Gillette style.","Merkur","",'https://merkurshave.com/merkur-safety-razors/',
    [("Classic 1904 closed comb","Merkur","","old-data name")],a="Merkur 1904 · 1904/1906",dt="finish"),
  X("Edwin Jagger DE89","Sheffield-made three-piece razor sharing Edwin Jagger's standard head across handle styles.","Edwin Jagger","",'https://newenglandshaving.com/products/edwin-jagger-de89-double-edge-safety-razor-chrome',
    [("DE89 chrome","Edwin Jagger","","brass handle, 68 g"),("Chatsworth","Edwin Jagger","","handle style (old data)"),("Georgian","Edwin Jagger","","handle style (old data)"),("Bulbous","Edwin Jagger","","handle style (old data)")],
    dt="handle style · finish"),
  X("Mühle R89","Closed-comb Mühle razor with a wavy guard; mild and popular with beginners.","Mühle","",'https://www.muehle-shaving.com/en/Blog/How-to-shave/Facts-about-the-safety-razor/',
    dt="handle material · finish"),
  X("Mühle R41","Open-comb Mühle razor with high blade exposure for heavy beards.","Mühle","",'https://www.muehle-shaving.com/en/Blog/How-to-shave/Facts-about-the-safety-razor/',
    dt="handle material · finish"),
  X("Rockwell 6C / 6S","Razor with three reversible base plates giving six blade-gap settings.","Rockwell Razors","",'https://getrockwell.com/products/rockwell-6s-adjustable-safety-razor',
    [("6C","Rockwell Razors","","entry version"),("6S","Rockwell Razors","","316L stainless steel"),("2C","Rockwell Razors","","two settings"),("T2","Rockwell Razors","","adjustable dial")],
    dt="plates 1–6 · finish"),
  X("Henson AL13","Aerospace-machined aluminium razor holding the blade at a fixed 30° with minimal exposure.","Henson Shaving","",'https://hensonshaving.com/products/henson-al13-in-aircraft-aluminum',
    dt="anodised colour · 37 g"),
  X("Wolfman WR1","Small-workshop stainless-steel razor machined and hand-polished in Alberta.","Wolfman Razors","",'https://www.razoremporium.net/products/wolfman-wr1-stainless-steel-safety-razor-made-in-canada',
    [("WR1","Wolfman Razors","","316L stainless"),("WR2","Wolfman Razors","","old-data model"),("WR3","Wolfman Razors","","old-data model")],
    dt="blade gap · polish")],
 "m":[["Krona","Schick"],["Platinum","Schick"],["Lady Gillette","Gillette"],["Double Six Minor","Souplex"],["Bedford","Wardonia"],["Black Prince","Wardonia"],["Devon","Wardonia"],["Oxford","Wardonia"],["Classic","Wilkinson Sword"]]}
se = {"n":"Single-edge safety razor","a":"SE razor · injector razor",
 "d":"Guarded razor holding a blade with one cutting edge.",
 "t":["GEM-style (rib-back blade)","injector","artist club (AC) blade","proprietary blade (OneBlade, Leaf)","pivoting head"],
 "s":"https://www.westcoastshaving.com/shop-brands",
 "x":[
  X("Star Safety Razor","Early American hoe-shaped guard razor patented by the Kampfe brothers.","Kampfe Brothers","1880",SR,dt="finish · case"),
  X("GEM razor","Single-edge razor taking the rib-back blade introduced by American Safety Razor in 1906.","American Safety Razor Company","1898 (Gem Cutlery) · 1906",ASR,
    [("Gem Safety Razor","Gem Cutlery Company","1898","first Gem, derived from the Star")],a="Gem",dt="head type · finish"),
  X("Schick Injector","Razor loaded by pushing a blade straight in from a dispenser, never handling the blade.","Schick","1935–early 2000s",SCH,dt="handle material · type letter"),
  X("OneBlade","Modern pivoting single-edge razor taking thick Feather FHS blades.","OneBlade","",'https://onebladeshave.com/products/feather-fhs10-blades',
    [("Genesis","OneBlade","","luxury model"),("Element","OneBlade","",""),("Dawn","OneBlade","","women's model")],dt="finish"),
  X("Leaf razor","Pivoting-head razor holding several individually guarded single-edge blades.","Leaf Shave","",'https://leafshave.com/',
    [("Leaf Two","Leaf Shave","","two blades, magnetic loading"),("Branch Single Edge","Leaf Shave","","all-metal head")],dt="blade count · finish")]}
bl = {"n":"Safety razor blade","a":"DE blade · SE blade · razor blades",
 "d":"Replaceable blade for a safety razor, sold in packs by blade standard.",
 "t":["double-edge (DE)","single-edge rib-back (GEM)","injector","artist club (AC)","Feather FHS (OneBlade)","carbon steel","stainless steel","platinum or PTFE coated"],
 "s":"https://www.westcoastshaving.com/shop-brands",
 "x":[
  X("Gillette Blue Blade","Blue-lacquered Gillette carbon blade, one of the most recognised blades.","Gillette","1932",GW,a="Blue Super Blade"),
  X("Wilkinson Sword stainless blade","Coated stainless double-edge blade that lasted about a week and won market share.","Wilkinson Sword","1962",WS),
  X("Personna stainless blade","Personna blade with which American Safety Razor became the first maker of stainless steel blades (per its history).","American Safety Razor Company","1963",ASR,
    [("Personna 74","American Safety Razor Company","1970","first tungsten steel blade"),("Platinum Chrome","Personna","","old-data model")]),
  X("Feather Hi-Stainless","Japanese double-edge blade by Feather, known as one of the sharpest.","Feather","",'https://www.classicshaving.com/products/feather-hi-stainless-platinum-double-edge-blades-10-pack',
    [("Black Platinum","Feather","","old-data model")],dt="pack size"),
  X("Astra Superior Platinum","Mild-to-moderate platinum-coated Gillette-group blade.","Astra","",'https://www.coifferie.com/us/go/product/70847269',dt="country of make"),
  X("Gillette 7 O'Clock Super Platinum","Platinum-edged Gillette double-edge blade in the black pack, made in India.","Gillette","",'https://www.therazorcompany.com/products/gillette-7-oclock-black-super-platinum-double-edge-razor-blades',dt="pack size"),
  X("GEM rib-back blade","Single-edge blade with a folded steel spine, still the GEM standard.","American Safety Razor Company","1906",ASR),
  X("Feather FHS","Thick single-edge Feather blade (0.23 mm) made for OneBlade razors.","Feather","",'https://onebladeshave.com/products/feather-fhs10-blades',dt="pack of 10, 30 or 90")],
 "m":[["Super Platinum","Dovo"],["Platinum","Gillette"],["Silver Blue","Gillette"],["Super Platinum Coated","Merkur"],["Super Chrome","Shark"]]}
ca = {"n":"Cartridge razor","a":"system razor · disposable razor · razor cartridge",
 "d":"Razor with a handle taking replaceable multi-blade cartridges; fully disposable razors included.",
 "t":["refill cartridge","disposable razor","powered (vibrating) razor","women's razor","pivoting head"],
 "s":"https://www.wegmans.com/shop/product/690834-ProGlide-Razor-for-Men-Handle-2-Blade-Refills",
 "x":[
  X("Wilkinson Sword Bonded Shaving System","Early cartridge with the blade bonded into a plastic housing.","Wilkinson Sword","1970",SR),
  X("Gillette Trac II","First twin-blade razor.","Gillette","1971",GW,[("Good News","Gillette","1976","disposable twin-blade; later Blue II")]),
  X("Gillette Atra","Twin-blade system with a pivoting head that follows the face.","Gillette","1977",GCA,[("Atra Plus","Gillette","1985","first lubricating strip")],a="Contour"),
  X("Bic disposable razor","Entirely disposable one-piece razor.","Bic","1974",SR),
  X("Gillette Sensor","Twin blades individually mounted on springs.","Gillette","1990",GCA,[("Sensor3","Gillette","","third blade added")]),
  X("Gillette Mach3","First triple-blade cartridge.","Gillette","1998",GW,[("M3Power","Gillette","","powered version")]),
  X("Schick Quattro","First four-blade cartridge, Schick's answer to the Mach3.","Schick","2003",SCH,[("Quattro Titanium","Schick","2008","coated blades")]),
  X("Gillette Fusion","Five-blade cartridge system, launched in manual and powered versions.","Gillette","2006",GCA,
    [("Fusion ProGlide","Gillette","2010","thinner blades"),("ProGlide FlexBall","Gillette","2014","multi-pivot handle"),("Fusion5 ProShield","Gillette","2015","lubrication strips both sides"),("Fusion5 ProGlide","Gillette","","current handle and refills (old data)")]),
  X("Schick Hydro","Five-blade system with skin guards, hydrating gel and flip trimmer; sold as Wilkinson Sword Hydro in Europe.","Schick","2010",SCH,[("Hydro 3","Schick","2010","three blades, no trimmer"),("Hydro 5 Power Select","Schick","2012","powered")]),
  X("Harry's razor","Direct-to-consumer cartridge razor with blades from its own Feintechnik factory in Eisfeld.","Harry's","2013",'https://www.gearpatrol.com/?p=139027'),
  X("Dollar Shave Club razor","Mail-order subscription razors, mostly resold Dorco handles and cartridges.","Dollar Shave Club","2011",W+'Dollar_Shave_Club',
    [("The Humble Twin","Dollar Shave Club","","two blades"),("The 4X","Dollar Shave Club","","four blades"),("The Executive","Dollar Shave Club","","six blades")])],
 "m":[["Guard single edge cartridge refill","Gillette"]]}
B=lambda n,c,f,seg,d,s,lines=(),sig=(),rel=(),eras=():{"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":list(lines),"eras":list(eras),"sig":list(sig),"sc":["Wet shaving"],"rel":list(rel),"s":s}
brands=[
 B("Gillette","United States","1901","Mass-market razors and blades","Boston razor maker founded as the American Safety Razor Company and renamed Gillette Safety Razor Company in 1904; part of Procter & Gamble since 2005.",GW,
   ["Tech","Super Speed","Adjustable","Trac II","Sensor","Mach3","Fusion","7 O'Clock"],["Gillette Safety Razor","Gillette Tech","Gillette Super Speed","Gillette Mach3","Gillette Fusion"],["Schick","Wilkinson Sword"]),
 B("Schick","United States","1926","Mass-market razors and blades","American razor brand founded by Jacob Schick; owned by Energizer from 2003 and Edgewell from 2015.",SCH,["Injector","Krona","Quattro","Hydro","Intuition"],["Schick Injector","Schick Quattro","Schick Hydro"],["Wilkinson Sword","Gillette"]),
 B("Wilkinson Sword","United Kingdom","1772","Mass-market razors and blades","British sword and gun maker turned razor brand; stainless blades from 1962; paired with Schick since the 1990s.",WS,["Classic","Hydro","Quattro"],["Wilkinson Sword stainless blade"],["Schick"]),
 B("American Safety Razor Company","United States","1906","Single-edge razors and blades","Merger of Gem and Ever-Ready; maker of GEM, Ever-Ready and Personna blades, now part of Edgewell.",ASR,["GEM","Ever-Ready","Personna","Treet"],["GEM razor","GEM rib-back blade","Personna stainless blade"]),
 B("Merkur","Germany","","Classic safety razors","Solingen maker of two-piece, adjustable and slant double-edge razors.",'https://merkurshave.com/merkur-safety-razors/',["34C","37C slant","Futur","Progress","42C 1904"],["Merkur 34C HD","Merkur 42C '1904'"],["Mühle","Edwin Jagger"]),
 B("Edwin Jagger","United Kingdom","","Classic safety razors and brushes","Sheffield maker of traditional safety razors and matching brushes.",'https://www.edwinjagger.com/shaving-products/razors/traditional-safety-razors/',["DE89","Chatsworth","Georgian"],["Edwin Jagger DE89"],["Merkur","Mühle"]),
 B("Mühle","Germany","1945","Brushes and safety razors","Family firm in Stützengrün, Ore Mountains, that began with hand-made shaving brushes in 1945.",'https://www.muehle-shaving.com/en/Family-Business',["Traditional R89","Traditional R41","Rocca"],["Mühle R89","Mühle R41"],["Merkur","Edwin Jagger"]),
 B("Rockwell Razors","","","Adjustable safety razors","Maker of plate-adjustable double-edge razors.",'https://getrockwell.com/pages/products',["6C","6S","2C","T2"],["Rockwell 6C / 6S"]),
 B("Henson Shaving","Canada","","Machined safety razors","Razors made at an aerospace machining plant in Ontario.",'https://hensonshaving.com/products/henson-al13-in-aircraft-aluminum',["AL13"],["Henson AL13"]),
 B("Wolfman Razors","Canada","","Artisan safety razors","One-machinist workshop in Alberta making high-end stainless razors.",'https://www.razoremporium.net/products/wolfman-wr1-stainless-steel-safety-razor-made-in-canada',["WR1","WR2","WR3"],["Wolfman WR1"]),
 B("OneBlade","","","Single-edge razors","Maker of pivoting single-edge razors using Feather FHS blades.",'https://onebladeshave.com/products/feather-fhs10-blades',["Genesis","Element","Dawn"],["OneBlade"],["Feather"]),
 B("Leaf Shave","United States","","Multi-blade safety razors","Leaf Shave Company maker of pivoting razors loaded with single-edge blades.",'https://leafshave.com/',["Leaf Two","Branch"],["Leaf razor"]),
 B("Harry's","United States","2013","Direct-to-consumer razors","Razor start-up by Jeff Raider and Andy Katz-Mayfield; bought the Feintechnik blade factory in Eisfeld in 2014.",'https://www.gearpatrol.com/?p=139027',[],["Harry's razor"],["Dollar Shave Club"]),
 B("Dollar Shave Club","United States","2011","Subscription razors","Venice, California mail-order razor club; Unilever bought it in 2016 and sold a majority in 2023.",W+'Dollar_Shave_Club',["Humble Twin","4X","Executive"],["Dollar Shave Club razor"],["Harry's"]),
]
trads=[
 {"n":"English wet shaving","g":"Grooming traditions","r":"London (St James's), England","p":"19th century to present",
  "d":"London barbers' and perfumers' tradition of the hot-towel shave and brush-lathered soaps and creams.",
  "tech":"hot-towel wet shave; brush lathering of soap or cream","mat":"shaving soap and cream, badger brushes, razors",
  "forms":["Shaving soap","Shaving brush","Double-edge safety razor","Straight razor"],
  "ctr":["Truefitt & Hill, St James's Street (est. 1805)"],"auth":"house name and royal warrant on product and shop","s":W+'Truefitt_%26_Hill'},
 {"n":"Italian wet shaving","g":"Grooming traditions","r":"Florence, Italy","p":"20th century to present",
  "d":"Italian barbershop tradition of pre- and after-shave creams used by barbers first, then home shavers.",
  "tech":"barbershop wet shave with pre-shave cream","mat":"shaving creams and soaps",
  "forms":["Pre-shave","Shaving cream","Aftershave"],"ctr":["Martelli family, Florence (Proraso; firm 1908, pre-shave cream 1948)"],
  "auth":"family firm branding","s":'https://proraso-usa.com/pages/a-beautiful-italian-store'}]
notes=("Merged: Wet-shaving kit into Double-edge safety razor as a type; DE and SE blades into Safety razor blade; Razor cartridge into Cartridge razor as a type. "
 "Old models without a confirmable archetype stay in m (Schick Krona/Platinum, Lady Gillette, Souplex, Wardonia, Dovo/Merkur/Shark blades). "
 "Left out: Gillette Tech exact launch is from vintage-razor.com (1938); no page retrieved linking Wardonia to Gillette, so not made a version; Solingen tradition not repeated (already in shelf 03_01); "
 "Feather brand register entry not repeated (in 03_01). Leaf placed under single-edge (uses single-edge blades). No founding years for Merkur, Edwin Jagger, Rockwell, OneBlade, Leaf (not on retrieved pages). "
 "Gillette Fusion ProGlide range from old data kept as a Fusion version.")
out={"kinds":[de,se,bl,ca],"brands":brands,"traditions":trads,"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/H1/shelves/03_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
