import sys; sys.path.insert(0,'work/I2/agent')
from put import put
W='https://en.wikipedia.org/wiki/'
def A(n,mk,y,s,d,v=(),a='',dt=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s if s.startswith('http') else W+s,"v":[dict(n=i[0],mk=i[1],y=i[2],d=i[3]) for i in v]}
    if dt: x["dt"]=dt
    return x
EP="https://www.epicgames.com/help/en-US/c-202300000001636/c-202300000001721/a202300000011084"
kinds=[
{"n":"Weapon skin","a":"gun skin · finish","d":"A finish that changes the look of an in-game weapon.","t":["Factory New to Battle-Scarred wear","StatTrak","Souvenir","Variant colours","Upgrade levels (VFX, animation, finisher)"],"s":"https://cs.trade/cs2",
 "x":[
  A("AWP | Dragon Lore","Valve","2014","https://csgoskins.gg/items/awp-dragon-lore","Covert Custom Paint Job AWP skin from the Cobblestone collection, the best-known rare CS skin.",[
   ("Souvenir Dragon Lore","Valve","2014","Souvenir version with its own price tiers"),
   ("Operation Breakout release","Valve","2014","Released 1 July 2014")],"","wear 0.00-0.70 · Factory New 0.00-0.07 to Battle-Scarred 0.45-0.70"),
  A("Prime","Riot Games","2020","https://valorant.fandom.com/wiki/Prime_Collection","Valorant's first store bundle, released in patch v1.0, with four weapons and a melee.",[
   ("Prime Classic","Riot Games","","1,775 VP; variants orange, blue, yellow; four upgrade levels"),
   ("Prime Spectre","Riot Games","",""),("Prime Guardian","Riot Games","",""),("Prime Vandal","Riot Games","",""),
   ("Prime Axe","Riot Games","","Melee"),("Prime//2.0","Riot Games","","Later 2.0 collection, with its own page")]),
  A("Reaver","Riot Games","","https://valorant.fandom.com/wiki/Reaver_Collection","Valorant collection sold in several limited bundles: EP 1, EP 5 and V26.",[
   ("Reaver Sheriff","Riot Games","","EP 1 bundle, 1,775 VP; red, black, white variants"),
   ("Reaver Guardian","Riot Games","",""),("Reaver Vandal","Riot Games","",""),("Reaver Operator","Riot Games","",""),
   ("Reaver 3.0","Riot Games","","Evolves tier; Bandit and Butterfly Knife per Dexerto's bundle list")])],
 "m":[["AK-47 | Bloodsport","Valve"],["AWP | Medusa","Valve"],["M4A1-S | Cyrex","Valve"],["M4A1-S | Fade","Valve"],["Desert Eagle | Midnight Storm","Valve"],["Oni Vandal","Riot Games"],["RGX 11Z Pro Vandal","Riot Games"],["Prime 2.0 Odin","Riot Games"],["Elderflame Operator","Riot Games"],["Magepunk Phantom","Riot Games"]],
 "r":[["Oni","Riot Games"],["Glitchpop","Riot Games"],["Glitchpop 2.0","Riot Games"],["Kuronami","Riot Games"],["Kuronami 2.0","Riot Games"],["RGX 11z Pro","Riot Games"],["Prime 2.0","Riot Games"],["Reaver 2.0","Riot Games"],["Magepunk 2.0","Riot Games"],["Gaia's Vengeance","Riot Games"]]},
{"n":"Knife skin","a":"bayonet skin · karambit","d":"Skins for in-game knives and bayonets.","t":["Vanilla (no finish)","Solid and patterned","High-gloss anodized","Doppler phases"],"s":"https://csdb.gg/weapon/classic-knife/",
 "x":[
  A("Karambit","Valve","","https://steamdb.com/en/skins/cs2/knives/karambit","The most traded CS knife model; finish families set the price.",[
   ("Doppler","Valve","","Phases 1-4 plus Ruby, Sapphire, Black Pearl; Chroma Case; Factory New and Minimal Wear only"),
   ("Gamma Doppler","Valve","","Phases 1-4 plus Emerald; Gamma Case"),
   ("Fade","Valve","","Valued by fade percentage; CS:GO Weapon Case"),
   ("Case Hardened","Valve","","Blue gem seeds valued highest"),
   ("Marble Fade","Valve","","Fire and Ice layout prized; Chroma Case"),
   ("Tiger Tooth","Valve","","High-gloss anodized; Chroma Case"),
   ("Slaughter","Valve","","Solid finish")]),
  A("M9 Bayonet","Valve","","https://www.steamdb.com/en/skins/cs2/knives/m9-bayonet","Bayonet-style knife model with 25 finishes, including Doppler and Gamma Doppler phases.")],
 "m":[["Bayonet | Doppler","Valve"],["Butterfly Knife | Fade","Valve"],["M9 Bayonet | Fade","Valve"],["Skeleton Knife | Tiger Tooth","Valve"],["Talon Knife | Damascus Steel","Valve"]]},
{"n":"Glove skin","a":"gloves · hand wraps","d":"Skins for in-game gloves worn on a character's hands.","t":["Model","Finish","Float limited by wear band"],"s":"https://steamdb.com/en/skins/cs2/gloves",
 "x":[A("CS2 gloves","Valve","2016","https://steamdb.com/en/skins/cs2/gloves","Glove models whose price is set by model, finish and float; no StatTrak, name tags or stickers.",[
   ("Glove Update models","Valve","2016","Bloodhound, Driver, Hand Wraps, Moto, Specialist and Sport Gloves"),
   ("Hydra Gloves","Valve","2017","With Operation Hydra"),
   ("Broken Fang Gloves","Valve","2020","With Operation Broken Fang")])],
 "m":[["Bloodhound Gloves | Snakebite","Valve"],["Driver Gloves | King Snake","Valve"],["Driver Gloves | Overtake","Valve"],["Hand Wraps | Cobalt Skulls","Valve"],["Hydra Gloves | Case Hardened","Valve"]]},
{"n":"Tool and glider skin","a":"pickaxe · glider · trails","d":"An item that changes the look of an in-game tool or traversal gear (pickaxe, glider, trails).","s":"https://fortnite-archive.fandom.com/wiki/Galaxy_(set)",
 "x":[A("Fortnite pickaxe and glider","Epic Games","2017",W+"Fortnite_Battle_Royale","Cosmetic harvesting tool and descent glider sold in the item shop or battle pass.")],
 "m":[["Celestial (contrail)","Epic Games"],["Discovery (glider)","Epic Games"],["Stellar Axe","Epic Games"]],"r":[["Galaxy","Epic Games"]]},
{"n":"Vehicle skin","a":"car body · wheels · decal","d":"An item that changes the body or parts (wheels) of an in-game vehicle.","t":["Car body","Wheels","Decal","Paint finish","Boost","Licensed crossover car"],"s":EP,
 "x":[A("Rocket League car cosmetics","Psyonix","2015",W+"Rocket_League","Cosmetic car bodies, wheels, decals, paint finishes and boosts for the 2015 Psyonix game.")]},
{"n":"Wrap","a":"surface finish","d":"A finish applied across the surfaces of vehicles, weapons or other items.","t":["Weapon wrap","Vehicle wrap"],"s":EP},
]
def B(n,c,f,seg,kf,d,s): return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s}
brands=[
 B("Valve","United States","1996","Professional & flagship","Counter-Strike skins","Developer and publisher of Counter-Strike 2, with its Steam Community Market.","knowledge"),
 B("Riot Games","United States","2006","Professional & flagship","Valorant skins","Maker of Valorant and League of Legends, selling skin bundles.","knowledge"),
 B("Epic Games","United States","","Professional & flagship","Fortnite cosmetics","Fortnite developer, selling cosmetics through an item shop.",W+"Fortnite_Battle_Royale"),
 B("Psyonix","United States","2000","Specialist","Rocket League cosmetics","Rocket League developer, founded 2000 and acquired by Epic Games in 2019.",W+"Psyonix"),
]
put('I2','02_00',{"kinds":kinds,"brands":brands,"traditions":[],"notes":"Replaced the Riot (37) and Valve (17) skin SKU lists with archetypes: Dragon Lore, Prime and Reaver for weapon skins; Karambit and M9 Bayonet finish families for knives. Short m and r ranges kept. CS2 glove models taken in as their own kind. Howl, Asiimov, Fade (rifle), Doppler (rifle), Medusa, Elderflame, Oni, Glitchpop, Kuronami and RGX 11z Pro as archetypes dropped: no retrieved page named them (Valorant fandom pages gave 402 on WebFetch; Prime and Reaver established via the Firecrawl retry, others not). Fortnite pickaxes and Rocket League cars are broad archetypes without named items; licensed crossover cars left out because they carry film titles. Vehicle skin and Wrap keep the old Epic help source."})
