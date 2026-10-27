import sys; sys.path.insert(0,'work/I2/agent')
from put import put
W='https://en.wikipedia.org/wiki/'
def A(n,mk,y,s,d,v=(),a='',dt=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s if s.startswith('http') else W+s,"v":[dict(n=i[0],mk=i[1],y=i[2],d=i[3]) for i in v]}
    if dt: x["dt"]=dt
    return x
G="https://fortnite-archive.fandom.com/wiki/Galaxy_(set)"
kinds=[
{"n":"Character outfit or skin","a":"agent · costume","d":"An item that changes the look of a player's character or agent.","t":["Shop outfit","Battle-pass outfit","Licensed collaboration outfit","Agent by faction"],"s":G,
 "x":[A("Dota 2 cosmetic sets","Valve","2013","Dota_2","Hero armour and weapon sets sold in the Dota Store, from the Compendium and Dota Plus, with community Workshop entries."),
      A("Roblox avatar items","Roblox","2004","https://en.wikipedia.org/wiki/Builder's_Club","Avatar clothing and accessories bought with Robux; some are scarce limiteds and since 2019 some are community-made.",[
        ("Limited item","Roblox","","Few copies; price set by supply and demand; resellable"),
        ("UGC item","Roblox","2019","Selected users may upload accessories, later animations and bundles")]),
      A("Fortnite outfit","Epic Games","2017","Fortnite_Battle_Royale","Outfits sold in the daily item shop or earned from a battle pass.")],
 "m":[["Galaxy (Fortnite outfit)","Epic Games"],["Agent | Getaway Sally","Valve"],["Agent | Number K","Valve"],["Agent | Sir Bloody Miami Darryl","Valve"],["Agent | Safecracker Voltzmann","Valve"]],"r":[["Galaxy","Epic Games"],["Operation Broken Fang Agents","Valve"]]},
{"n":"Avatar accessory","a":"back bling · hat · backpack","d":"A worn add-on item for a character, such as back items, shoes, hats or banners.","t":["Back bling","Hat","Banner","Limited accessory"],"s":G,"m":[["Galactic Disc","Epic Games"]],"r":[["Galaxy","Epic Games"]]},
{"n":"Emote","a":"dance","d":"An animation or dance a player's character performs on command.","t":["Dance","Gesture","Licensed emote"],"s":"https://www.epicgames.com/help/en-US/c-202300000001636/c-202300000001721/a202300000011084"},
{"n":"Companion or pet","a":"pet · sidekick","d":"A pet or sidekick that accompanies a player's character.","t":["Minion","Collectible pet","Promotional pet"],"s":"https://fortnite.gg/shop"},
{"n":"Mount","a":"ridable creature · vehicle","d":"A ridable creature or vehicle a character rides, often collected account-wide.","t":["Ground mount","Flying mount","Promotional mount"],"s":W+"World_of_Warcraft:_Wrath_of_the_Lich_King","x":[
  A("World of Warcraft flying mounts","Blizzard Entertainment","2008","World_of_Warcraft:_Wrath_of_the_Lich_King","Mounts ridden in the air; in Wrath of the Lich King, from level 80 in Northrend.",[("Wrath of the Lich King release","Blizzard Entertainment","2008","13 November 2008 in Europe and North America")]),
  A("Final Fantasy XIV chocobo mount","Square Enix","","Final_Fantasy_XIV","Chocobo mount given to long-time subscribers through the Legacy Campaign.")]},
{"n":"Housing and décor item","a":"furniture · player home item","d":"Furniture and decoration for a player's home or plot.","t":["Furniture","Wallpaper and floor","Garden item","Player-made virtual good"],"s":W+"Animal_Crossing","x":[
  A("Animal Crossing furniture","Nintendo","2001","Animal_Crossing","Furniture bought and collected for placement anywhere in the house, with changeable wallpaper and floors."),
  A("Final Fantasy XIV housing","Square Enix","2013","Final_Fantasy_XIV","Houses bought in residential districts, first by Free Companies in patch 2.1 on 16 December 2013, then decorated."),
  A("Second Life virtual goods","Linden Lab","","Economy_of_Second_Life","Player-made buildings, vehicles, clothing and furniture traded for Linden Dollars.")]},
]
def B(n,c,f,seg,kf,d,s): return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s}
brands=[
 B("Roblox","United States","2004","Mainstream","avatar items","Platform with Robux-bought avatar items, limiteds and community-made items.","https://en.wikipedia.org/wiki/Builder's_Club"),
 B("Nintendo","Japan","","Professional & flagship","Animal Crossing","Maker of the Animal Crossing series, begun in 2001.",W+"Animal_Crossing"),
 B("Square Enix","Japan","","Professional & flagship","Final Fantasy XIV","Publisher of Final Fantasy XIV.","knowledge"),
 B("Blizzard Entertainment","United States","","Professional & flagship","World of Warcraft","Maker of World of Warcraft and its mounts.","knowledge"),
 B("Linden Lab","United States","","Specialist","Second Life","Operator of Second Life and the Linden Dollar economy.",W+"Economy_of_Second_Life"),
]
put('I2','02_01',{"kinds":kinds,"brands":brands,"traditions":[],"notes":"Trimmed the CS2 agent list (13 agents) to a short m of four plus the Operation Broken Fang range; CS2 gloves moved to the Glove skin shelf (five glove models removed from Avatar accessory). Not sourced and so left out: Renegade Raider, Black Knight, Skull Trooper, League of Legends skin lines, Dota 2 arcanas (Dota 2 page does not mention arcana), Roblox Dominus, named WoW rare mounts. Mount and Housing kinds added from retrieved pages. Emote and Companion have no archetypes."})
