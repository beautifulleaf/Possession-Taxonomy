import json, os
G='https://gununiversity.com/best-reloading-press/'; W='https://en.wikipedia.org/wiki/Handload'
D='https://gununiversity.com/?p=32062'; AL='https://www.brownells.com/brands/alliant-powder/reloading'
H='Hodgdon Powder Company'
kinds=[
{"n":"Reloading press","a":"loading press · reloading machine","d":"Bench press that drives cases into dies to resize, prime, seat and crimp home-loaded cartridges.",
 "t":["single-stage","turret","progressive","shotshell press"],"s":W,
 "m":[["Rock Chucker Supreme","RCBS"],["Classic Turret","Lee Precision"],["Lock-N-Load AP","Hornady"],["XL 750","Dillon Precision"],["RL 550B","Dillon Precision"],["Big Boss II","Redding"],["All American 8","Lyman"],["600 Jr Mark V","MEC"]]},
{"n":"Reloading die set","a":"loading dies · sizing die · seating die","d":"Matched set of screw-in dies for one cartridge that size, expand, seat and crimp cases in a press.",
 "t":["2-die set (bottleneck)","3-die set (straight-wall)","4-die set","carbide","bushing / match"],"s":D,
 "m":[["Type S Match Bushing Full Die Set","Redding"],["Gold Medal Match Die Set","RCBS"],["Series II Taper Crimp Die Set","Hornady"],["Deluxe Pistol 4 Die Set","Lee Precision"],["Carbide Deluxe Rifle 3 Die Set","Lyman"]]},
{"n":"Smokeless powder","a":"reloading powder · propellant","d":"Smokeless propellant sold in canisters for loading cartridges and shotshells.",
 "t":["pistol","rifle","shotshell","ball","extruded"],"s":"https://www.basspro.com/l/primers-powder",
 "m":[["Hodgdon H4350",H],["Hodgdon H110",H],["Hodgdon Titegroup",H],["Alliant Bullseye","Alliant Powder"],["Alliant Unique","Alliant Powder"],["Alliant Reloder 16","Alliant Powder"],["Alliant Red Dot","Alliant Powder"],["Vihtavuori N140","Vihtavuori"],["Accurate No. 5","Accurate"],["Ramshot TAC","Ramshot"],["Winchester 296","Winchester"],["Winchester 748","Winchester"]]},
{"n":"Primer","a":"percussion primer · shotshell primer","d":"Ignition cap sold on its own for loading cartridges.","t":["small pistol","large pistol","small rifle","large rifle","magnum","209 shotshell"],
 "s":"https://www.basspro.com/l/primers-powder",
 "m":[["CCI Benchrest Large Rifle Primer","CCI"],["CCI Standard Large Pistol Magnum Primer","CCI"],["CCI Standard Small Pistol Magnum Primer","CCI"],["Winchester 209 Shotshell Primer","Winchester"]]},
{"n":"Loose bullet","a":"reloading bullet · projectile","d":"Bullet sold on its own for loading cartridges.","t":["full metal jacket","hollow point","polymer tip","match"],
 "s":"https://www.gunmade.com/accessories/other/hornady/eld-x-rifle-bullets/",
 "m":[["ELD-X","Hornady"],["A-Max","Hornady"],["SST","Hornady"],["GameKing","Sierra"],["TNT","Speer"],["Scenar","Lapua"]]},
{"n":"Cartridge case","a":"brass · once-fired brass","d":"Empty case, new or once-fired, sold on its own for loading cartridges.","t":["new","once-fired","brass","nickel-plated"],
 "s":"https://www.sportsmans.com/shooting-gear-gun-supplies/ammunition-ammo-for-hunting-shooting-sports/c/cat100112"},
{"n":"Shotshell wad","a":"","d":"Plastic or fibre wad sold on its own for loading shotshells or muzzle-loaders.","t":["plastic","fibre"],
 "s":"https://www.sportsmans.com/shooting-gear-gun-supplies/ammunition-ammo-for-hunting-shooting-sports/c/cat100112"},
{"n":"Black powder","a":"black powder substitute","d":"Black powder and its substitutes for muzzle-loading guns.","t":["loose","pellets"],"s":"https://shop.hodgdon.com/pyrodex-p-pistol-powder/",
 "m":[["Pyrodex P",H],["Pyrodex RS",H],["Pyrodex Select",H],["Blue MZ 50/50 Muzzleloading Pellets","Alliant Powder"]],"r":[["Pyrodex",H]]},
{"n":"Muzzle-loading projectile","a":"round ball · conical · sabot","d":"Ball or conical bullet loaded from the muzzle.","s":"https://muzzle-loaders.com/collections/traditional-muzzleloader-bullets",
 "m":[["Round ball",""],["Maxi-Ball","Thompson/Center Arms"],["Maxi-Hunter","Thompson/Center Arms"],["Great Plains conical","Hornady"],["PA Conical","Hornady"],["RedZone Conical","Traditions"]]},
]
K='knowledge'
def b(n,c,f,seg,kf,d):
    x={"n":n,"c":c,"seg":seg,"kf":kf,"d":d,"s":K}
    if f: x["f"]=f
    return x
brands=[
b(H,"United States","1952","Specialist","reloading powder","Kansas powder company selling Hodgdon, IMR and Pyrodex propellants to handloaders."),
b("Alliant Powder","United States","","Specialist","smokeless powder","Maker of Bullseye, Unique, Red Dot and Reloder powders, descended from Hercules."),
b("Vihtavuori","Finland","","Specialist","smokeless powder","Finnish maker of N-series reloading powders."),
b("Accurate","United States","","Specialist","smokeless powder","Reloading powder brand with numbered pistol and rifle powders."),
b("Ramshot","United States","","Specialist","smokeless powder","Reloading powder brand sold alongside Accurate."),
b("Winchester","United States","1866","Mainstream","ammunition","American firearms and ammunition brand that also sells powders and primers."),
b("CCI","United States","1951","Mainstream","primers","Idaho maker of primers and rimfire ammunition."),
b("Hornady","United States","1949","Mainstream","bullets, reloading","Nebraska maker of bullets, ammunition and reloading equipment."),
b("RCBS","United States","1943","Mainstream","reloading presses","Californian maker of reloading presses, dies and tools."),
b("Dillon Precision","United States","","Specialist","progressive presses","Arizona maker of progressive reloading presses."),
b("Lee Precision","United States","1958","Value","reloading tools","Wisconsin maker of low-cost reloading presses and dies."),
b("Redding","United States","","Premium","reloading dies","Maker of precision reloading dies and presses."),
b("Lyman","United States","1878","Mainstream","reloading tools","Long-established maker of sights, reloading tools and manuals."),
b("MEC","United States","","Specialist","shotshell presses","Mayville Engineering Company, maker of shotshell reloading presses."),
]
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":"Two new kinds (Reloading press, Reloading die set) sourced from the Wikipedia Handload article and Gun University roundups. Smokeless powder trimmed from 27 SKUs to 12 across Hodgdon, Alliant, Vihtavuori, Accurate, Ramshot and Winchester (Alliant names from a Brownells brand page). Powder/primer/bullet/case attribute variants moved into t. Bullets extended with models named on the Wikipedia Handload page. No traditions apply. Thompson/Center and Traditions left without register entries (minor makers on one kind)."}
p='work/E4/shelves/03_01.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
