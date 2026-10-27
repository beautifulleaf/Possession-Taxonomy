import json
W='https://en.wikipedia.org/wiki/'
TP=W+"Tobacco_pipe"
def x(n,mk,y,s,d,v=None):
    r={"n":n,"a":"","d":d,"mk":mk,"y":y,"s":s}
    if v: r["v"]=[{"n":a,"mk":b,"y":c,"d":e} for a,b,c,e in v]
    return r
def sv(*names): return [(n,"","","") for n in names]
briar=[
x("Billiard","","",TP,"Straight pipe with a cylindrical bowl and straight shank, the baseline shape.",[("Brandy","","","Billiard variant"),("Chimney","","","Billiard variant"),("Pot","","","Billiard variant"),("Nose Warmer","","","Billiard variant"),("Panel","","",""),("Oom Paul","","","")]),
x("Bulldog","","",TP,"Pipe with an angular, tapering bowl and a diamond-section shank.",sv("Rhodesian","Bull Moose","Bullcap","Ukulele")),
x("Apple","","",TP,"Pipe with a rounded, apple-shaped bowl.",sv("Prince","Author","Diplomat","Egg","Hawkbill","Tomato")),
x("Canadian","","",TP,"Pipe with a long oval shank and short stem.",sv("Liverpool","Lovat","Lumberman")),
x("Dublin","","",TP,"Pipe with a conical bowl widening toward the rim.",sv("Acorn","Cutty","Devil Anse","Zulu")),
x("Cavalier","","",TP,"Pipe whose bowl rises from a long horizontal shank chamber.",sv("Pseudo-cavalier")),
x("Sitter","","",TP,"Flat-based pipe that stands upright on its own, the poker included.",sv("Poker","Duke","Tankard","Cherrywood")),
x("Churchwarden","","",W+"Churchwarden_pipe","Long-stemmed pipe, stem up to about 16 in (40 cm), giving cooler smoke."),
x("Vest pocket","","",TP,"Small, flat pipe made to fit a waistcoat pocket."),
x("Peterson System","Peterson","1894",W+"Peterson_Pipes","Dublin pipe with a moisture reservoir in the shank, patented in 1894 as the 'Dry System'; Peterson's best-known design.",[("Standard System","Peterson","",""),("Deluxe System","Peterson","","")]),
x("Peterson Sherlock Holmes","Peterson","",W+"Peterson_Pipes","Peterson's Sherlock Holmes series of pipes with silverwork."),
x("Savinelli","Savinelli","1876",W+"Savinelli_Pipes","Italian maker of machine-made and hand-carved briar pipes, Milan, with a factory at Barasso."),
x("Stanwell","Stanwell","1942","https://pipedia.org/wiki/Stanwell","Danish maker founded by Poul Nielsen; Sixten Ivarsson designed shapes cut in the factory.",[("Royal Danish","Stanwell","",""),("Danish Quaint","Stanwell","",""),("Sorn","Stanwell","","")]),
x("Comoy's","Comoy's","1825","https://pipedia.org/wiki/Chapuis-Comoy","Pipe house founded in Saint-Claude by François Comoy; the Chapuis-Comoy group also makes Chacom and Ropp."),
x("Dunhill","Dunhill","1906","https://pipemuseum.nl/en/bruyeres-klassiek-of-curieus","London house that entered the pipe market in 1906 and set up its own factory, first ordering pipes from Charatan; white dot on the stem."),
]
free=[
x("Danish freehand","","","https://pipedia.org/wiki/Jess_Chonowitsch","Free-form briar pipe carved to the grain, taught through Copenhagen workshops: Suhr's, W.Ø. Larsen, Sixten Ivarsson and Poul Rasmussen's.",
 [("Sixten Ivarsson","Sixten Ivarsson","","Originator of modern Danish pipe making"),("Jess Chonowitsch","Jess Chonowitsch","1970","Own workshop from 1970, often with bamboo"),("Tom Eltang","","","Danish carver in the same lineage"),("Lars Ivarsson","","","Carver named in the same lineage")]),
x("Blowfish","","",TP,"Freehand form with a swollen bowl."),
x("Volcano","","",TP,"Freehand form with a cratered bowl top."),
x("Tomahawk","","",TP,"Freehand form with a long, angled bowl."),
x("Nautilus","","",TP,"Freehand form with a spiral bowl."),
x("Horn","","",TP,"Freehand form curved like a horn."),
]
kinds=[
{"n":"Briar pipe","a":"briar","d":"Pipe cut from the root burl of the tree heath (Erica arborea); classic shapes are named families, with makers' own shape references as versions.","t":["Smooth","Sandblasted","Rusticated","Straight","Bent"],"s":"https://www.smokingpipes.com/smokingpipesblog/glossary.cfm","x":briar},
{"n":"Freehand pipe","a":"","d":"Pipe shaped freely by the carver rather than to a classic shape; the Danish school set the model.","t":["Smooth freehand","Sandblasted freehand"],"s":"https://www.smokingpipes.com/smokingpipesblog/glossary.cfm","x":free,
 "m":[["Elephant's Foot",""],["Fig",""],["Olifant",""],["Pickaxe",""],["Ramses",""]]},
{"n":"Meerschaum pipe","a":"sepiolite pipe","d":"Pipe of sepiolite (meerschaum), carved from block or pressed from scraps, darkening to golden brown with use.","t":["Block meerschaum","Pressed meerschaum","Carved figural"],"s":W+"Meerschaum_pipe",
 "x":[x("Turkish carved meerschaum","","",W+"Eski%C5%9Fehir_Meerschaum_Museum","Hand-carved pipe from Eskişehir sepiolite; the region's deposits are among the richest in the world. Carved block smokes better than pressed.")]},
{"n":"Corn cob pipe","a":"cob","d":"Cheap pipe made from a corncob, needing no break-in.","t":["Standard","Straight","Bent"],"s":TP,
 "x":[x("Missouri Meerschaum cob pipe","Missouri Meerschaum","1869","https://pipedia.org/wiki/Missouri_Meerschaum","Corn cob pipes made from 1869 by Henry Tibbe; the world's oldest and largest cob pipe maker.",[("MacArthur","Missouri Meerschaum","","Shape linked to General Douglas MacArthur")])]},
{"n":"Clay pipe","a":"","d":"Moulded and fired clay pipe, the most widespread pipe in Europe historically; Irish ones are called dudeens.","t":["Long clay","Short clay"],"s":TP,
 "x":[x("Clay churchwarden","","",W+"Churchwarden_pipe","Long-stemmed clay pipe, common in taverns and in pioneer-era North America; breaks easily at the tenon.")]},
{"n":"Calabash pipe","a":"","d":"Pipe with a gourd-shaped body, traditionally a gourd with a meerschaum or porcelain cup; the briar calabash shape is an imitation.","t":["Gourd calabash","Reverse calabash","Briar calabash"],"s":"https://www.smokingpipes.com/smokingpipesblog/glossary.cfm",
 "x":[x("Calabash","","",TP,"Gourd-bodied pipe linked in popular image to Sherlock Holmes; Pioneer sold calabash-style pipes in the US from the late 1960s.")]},
{"n":"Tyrolean pipe","a":"Gesteckpfeife","d":"Alpine long pipe with a bowl set over a separate sump and a long stem.","t":[],"s":TP},
{"n":"Kiseru","a":"","d":"Japanese pipe with a small metal bowl, used for finely shredded kizami tobacco.","t":["Rau kiseru","Nobe kiseru"],"s":"https://www.sarudama.com/miscellaneous/kiseru/",
 "x":[x("Rau kiseru","","",W+"Kiseru","Kiseru in three parts: mouthpiece (suikuchi), stem (rau) and bowl shank (gankubi)."),
      x("Nobe kiseru","","",W+"Kiseru","Kiseru made from a single piece of metal.")],
 "m":[["Marugenke kiseru","Tanikawa Seijiro Shoten"]]},
{"n":"Midwakh","a":"medwakh","d":"Small Arabian pipe loaded by dipping the bowl into dokha, made mainly in the United Arab Emirates.","t":["Wooden midwakh","Metal midwakh"],"s":W+"Midwakh"},
]
def b(n,c,f,seg,kf,d,s,lines=None):
    r={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s}
    if lines: r["lines"]=lines
    return r
brands=[
b("Peterson","Ireland","1865","Heritage manufactory","System pipe","Dublin maker founded as Kapp Brothers; System pipe patented 1894.",W+"Peterson_Pipes",["System","Sherlock Holmes","Aran","Donegal Rocky"]),
b("Savinelli","Italy","1876","Premium","Italian briar","Milan maker of machine-made and hand-carved pipes, with a factory at Barasso.",W+"Savinelli_Pipes"),
b("Stanwell","Denmark","1942","Premium","Danish shapes","Founded by Poul Nielsen; Sixten Ivarsson designed its shapes.","https://pipedia.org/wiki/Stanwell"),
b("Comoy's","France","1825","Heritage manufactory","Saint-Claude briar","Founded by François Comoy; the Chapuis-Comoy group also makes Chacom and Ropp.","https://pipedia.org/wiki/Chapuis-Comoy"),
b("Dunhill","United Kingdom","1906","Premium","London pipes","London house that entered the pipe market in 1906 and later made its own pipes.","https://pipemuseum.nl/en/bruyeres-klassiek-of-curieus"),
b("Missouri Meerschaum","United States","1869","Heritage manufactory","corn cob pipes","Corn cob pipe maker begun by Henry Tibbe in 1869; company name from 1907.","https://pipedia.org/wiki/Missouri_Meerschaum"),
b("Sixten Ivarsson","Denmark","","Artisan & independent","Danish freehand","Originator of modern Danish pipe making.","https://pipedia.org/wiki/Stanwell"),
b("Jess Chonowitsch","Denmark","1970","Artisan & independent","freehand, bamboo","Danish pipe maker with his own workshop from 1970.","https://pipedia.org/wiki/Jess_Chonowitsch"),
]
trad=[
{"n":"Saint-Claude briar pipes","g":"Wood & smoking","r":"France (Jura)","p":"mid-19th century to present","d":"Town of the French Jura that became a centre of briar pipe manufacture from about 1854.","tech":"Turned and hand-finished briar","mat":"Briar","forms":["Briar pipe"],"ctr":["Comoy's","Chapuis-Comoy"],"auth":"Stamps of Saint-Claude houses.","s":"https://pipedia.org/wiki/Saint-Claude"},
{"n":"Danish freehand","g":"Wood & smoking","r":"Denmark (Copenhagen)","p":"1950s to present","d":"Free-form carving of briar to the grain, from Sixten Ivarsson's Copenhagen workshop and its pupils.","tech":"Free carving of briar","mat":"Briar","forms":["Freehand pipe"],"ctr":["Sixten Ivarsson","Jess Chonowitsch","Tom Eltang","Lars Ivarsson","W.Ø. Larsen"],"auth":"Maker's signature or stamp on the shank.","s":"https://pipedia.org/wiki/Jess_Chonowitsch"},
{"n":"Eskişehir meerschaum carving","g":"Stone & mineral","r":"Turkey (Eskişehir)","p":"18th century to present","d":"Carving of sepiolite pipes from the Eskişehir deposits.","tech":"Hand carving of soft sepiolite, then hardening by drying","mat":"Sepiolite (meerschaum)","forms":["Meerschaum pipe"],"ctr":["Eskişehir","Odunpazarı"],"auth":"Carved block rather than pressed pieces.","s":W+"Eski%C5%9Fehir_Meerschaum_Museum"},
{"n":"Japanese kiseru","g":"Metal & blades","r":"Japan","p":"16th century to present","d":"Metal smoking pipe for kizami tobacco, an Edo-period status object now made by few artisans.","tech":"Brass or silver beaten into shape and soldered","mat":"Brass, silver","forms":["Kiseru","Rau kiseru","Nobe kiseru"],"ctr":[],"auth":"Joined brass or silver parts.","s":W+"Kiseru"},
]
json.dump({"kinds":kinds,"brands":brands,"traditions":trad,"notes":"Old shape kinds folded into archetypes. Charatan, Barling, Castello, Ser Jacopo, Bo Nordh, W.Ø. Larsen product lines, Dutch Gouda clay, Legend cob and Rhodesian/Prince as separate archetypes not given own sources; Castello and others lacked a retrieved page. Pipedia blocked by WebFetch; fetched via Firecrawl once each."},open('s01_00.json','w'),ensure_ascii=False)
