import sys; sys.path.insert(0,'work/I2/agent')
from put import put
def A(n,mk,y,s,d,v=(),a='',dt=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(n=i[0],mk=i[1],y=i[2],d=i[3]) for i in v]}
    if dt: x["dt"]=dt
    return x
C="https://csdb.gg/cases/"; L="https://en.wikipedia.org/wiki/Loot_box"
kinds=[
{"n":"Loot case, crate or capsule","a":"loot box · container · sticker capsule · graffiti box","d":"An item that opens to give one or more random items.","t":["Weapon case (needs key)","Sticker capsule (most open without a key)","Graffiti box","Patch capsule","Music kit box","Tournament souvenir package"],"s":"https://counterstrike.fandom.com/wiki/Skill_Groups_Sticker_Capsule","x":[
 A("CS:GO Weapon Case","Valve","2013",C,"The original Counter-Strike weapon case, added in August 2013; the first of three numbered cases.",[
  ("CS:GO Weapon Case 2","Valve","2013","Second numbered case"),("CS:GO Weapon Case 3","Valve","2014","Third numbered case")]),
 A("eSports case series","Valve","2013",C,"Tournament-themed cases.",[
  ("eSports 2013 Case","Valve","2013",""),("eSports 2013 Winter Case","Valve","2013",""),("eSports 2014 Summer Case","Valve","2014","")]),
 A("Operation cases","Valve","2013",C,"Eight operation-linked cases between 2013 and 2021.",[
  ("Operation Bravo Case","Valve","",""),("Operation Phoenix Weapon Case","Valve","",""),("Operation Breakout Weapon Case","Valve","",""),("Operation Hydra Case","Valve","",""),("Operation Broken Fang Case","Valve","","")]),
 A("Chroma series","Valve","2015",C,"Numbered cases Chroma, Chroma 2 and Chroma 3.",[
  ("Chroma Case","Valve","2015",""),("Chroma 2 Case","Valve","2015",""),("Chroma 3 Case","Valve","2016","")]),
 A("Gamma series","Valve","2016",C,"Two numbered cases.",[("Gamma Case","Valve","2016",""),("Gamma 2 Case","Valve","2016","")]),
 A("Spectrum series","Valve","2017",C,"Two numbered cases.",[("Spectrum Case","Valve","2017",""),("Spectrum 2 Case","Valve","2017","")]),
 A("Prisma series","Valve","2019",C,"Two numbered cases.",[("Prisma Case","Valve","2019",""),("Prisma 2 Case","Valve","2020","")]),
 A("Tournament sticker capsule","Valve","","https://csdb.gg/capsules/","Capsules of team and autograph stickers sold in-game during Majors, usually in Champions, Legends and Challengers variants."),
 A("Team Fortress 2 crate","Valve","2010",L,"Random crates added in September 2010, opened with purchased keys."),
 A("Overwatch loot box","Blizzard Entertainment","2016",L,"Crate given on each level-up; cosmetic only; dropped with Overwatch 2 and returned in February 2025.")],
 "m":[["Glove Case","Valve"],["Fracture Case","Valve"],["Kilowatt Case","Valve"],["Recoil Case","Valve"],["Shattered Web Case","Valve"]]},
{"n":"Crate key","a":"unlock key","d":"An item that opens a loot container.","t":["Case key","Team Fortress 2 key"],"s":C,"x":[
 A("CS case key","Valve","","https://csdb.gg/cases/","One key opens each of the 42 weapon cases, priced at $2.49 on the page's snapshot."),
 A("Team Fortress 2 key","Valve","2010",L,"Key bought to open Team Fortress 2 crates; fixed Steam price of $2.18 per Wikipedia.")]},
]
put('I2','02_03',{"kinds":kinds,"brands":[],"traditions":[],"notes":"Merged Sticker capsule into Loot case, crate or capsule as a type. The 42 weapon cases cut to series (originator CS:GO Weapon Case 2013, eSports, operation, Chroma, Gamma, Spectrum, Prisma) plus five standalone m cases; the 25 sticker capsule SKUs dropped to one tournament-capsule archetype. Souvenir packages are a type with no source page. Key prices are snapshots."})
