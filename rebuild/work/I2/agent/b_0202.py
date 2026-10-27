import sys; sys.path.insert(0,'work/I2/agent')
from put import put
def A(n,mk,y,s,d,v=(),a='',dt=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(n=i[0],mk=i[1],y=i[2],d=i[3]) for i in v]}
    if dt: x["dt"]=dt
    return x
kinds=[
{"n":"In-game sticker, patch or charm","a":"sticker · patch · weapon charm · keychain","d":"A sticker, patch or charm applied to an in-game item.","t":["Team sticker","Autograph sticker","Patch (agent)","Weapon charm"],"s":"https://cs.trade/cs2","x":[
 A("CS2 sticker","Valve","","https://csdb.gg/cs2-sticker-grades/","Sticker with a finish (Paper, Glitter, Holo, Foil, Gold, Lenticular) and a separate rarity grade set by each capsule.",[
  ("Paper","Valve","","No bracket in the name"),("Holo","Valve","",""),("Foil","Valve","",""),("Glitter","Valve","",""),("Gold","Valve","",""),("Lenticular","Valve","","Added later")],"","grades High Grade, Remarkable, Exotic, Extraordinary · finish does not fix grade"),
 A("CS2 weapon charm","Valve","2024","https://steamdb.com/en/skins/cs2/charms","Dangling keychain trinket added on 2 October 2024; one slot per weapon, freely moved, still tradeable.",[
  ("Missing Link","Valve","2024","First charm collection"),("Small Arms","Valve","2024","Charms shaped like weapons")])],
 "m":[["Patch | Howl","Valve"],["Patch | Phoenix","Valve"],["Patch | Dragon","Valve"],["Patch | Koi","Valve"]]},
{"n":"Spray or graffiti","a":"graffiti","d":"An image a player places on surfaces in the game world.","t":["Sealed graffiti","Colour tint","Fortnite spray"],"s":"https://csgoskins.gg/categories/graffiti","x":[
 A("CS2 graffiti","Valve","","https://csgoskins.gg/categories/graffiti","Image spray-painted on the surface a player aims at; sold sealed and in tints such as Dust Brown and Shark White.")],
 "m":[["Llamalaxy","Epic Games"]],"r":[["Galaxy","Epic Games"]]},
{"n":"Music kit","a":"lobby music · MVP anthem","d":"An item that replaces a game's music, including the menu track and the MVP anthem.","t":["Standard kit","StatTrak kit (counts MVPs)"],"r":[["CS2 music kits","Valve"]],"s":"https://www.thespike.gg/counter-strike-2/music-kits","x":[
 A("CS2 music kit","Valve","2014","https://www.thespike.gg/counter-strike-2/music-kits","Cosmetic that swaps menu, round, bomb and MVP music; introduced in the CS:GO era and carried into CS2.",[("StatTrak music kit","Valve","","Counts MVPs earned while equipped")])]},
]
put('I2','02_02',{"kinds":kinds,"brands":[],"traditions":[],"notes":"Titles out: the 63 titled CS2 music-kit entries (artist and track) dropped, leaving the kind, one CS2 range and a StatTrak type. 40 titled patches cut to four m entries from the old list. 15 graffiti cut to a Fortnite one plus the CS2 graffiti archetype. The steamanalyst sticker guide returned 403, so sticker finishes come from csdb.gg."})
