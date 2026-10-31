import json, os
H="https://www.handbookofmineralogy.org/pdfs/"; H2="https://handbookofmineralogy.org/pdfs/"; W="https://en.wikipedia.org/wiki/"
FE="https://www.fossilera.com/minerals-for-sale"
def X(n,d,s,a="",y="",v=None,dt=""):
    return {"n":n,"a":a,"d":d,"mk":"","y":y,"s":s,"v":[{"n":q[0],"mk":"","y":q[1],"d":q[2]} for q in (v or [])],"dt":dt}
def K(n,d,s,xs,a="",t=None):
    k={"n":n,"a":a,"d":d,"s":s,"x":xs}
    if a=="" : k.pop("a")
    if t: k["t"]=t
    return k
C=H+"corundum.pdf"
kinds=[
K("Corundum","Uncut corundum specimen, including ruby and sapphire crystals on or off matrix and ruby-bearing rocks. Cut stones and cutting rough are under Sapphire and Ruby in Gemstones & pearls.",FE,[
 X("Mogok ruby crystal","Red gem corundum crystal from the Mogok district, Myanmar.",C,dt="crystal on matrix or loose · thumbnail to cabinet"),
 X("Ruby in zoisite","Metamorphic rock of green zoisite, dark pargasite and opaque ruby crystals, used for carvings and decorative pieces.",W+"Anyolite",a="anyolite · ruby zoisite · Tanganyika artstone",y="1954",
   v=[("Mundarara Mine, near Longido, Tanzania","1954","first discovery")],dt="rough, slab, sphere, carving"),
 X("Ruby in fuchsite","Ruby crystals in green chromium mica (fuchsite) schist from Karnataka, India.","https://www.gia.edu/articles/spring-2014-gemnews-indian-ruby-mining",
   v=[("Madikeri, Karnataka","","corundum-fuchsite-mica schist")],dt="slab, sphere, tumbled"),
 X("Ratnapura corundum","Gem corundum from the gem gravels of Ratnapura, Sri Lanka.",C,dt="water-worn crystals"),
 X("Jegdalek ruby","Ruby in marble from Jegdalek near Sorobi, Afghanistan.",C,dt="crystals in marble"),
 X("Longido and Morogoro ruby","Ruby from Merkestein near Longido and the Morogoro district, Tanzania.",C,dt="crystals"),
 X("Yogo sapphire","Sapphire from Yogo Gulch, Fergus County, Montana.",C,dt="small crystals"),
 X("Large corundum crystals","Large common corundum crystals from classic North American and African localities.",C,
   v=[("Hogback Mountain and Buck Creek, North Carolina","","large crystals"),("Bancroft and Haliburton, Ontario","",""),("Soutpansberg, South Africa","","large crystals")],
   dt="large crystals"),
],t=["ruby","sapphire","common corundum","in matrix"]),
K("Spinel","Magnesium aluminium oxide mineral specimen: octahedral crystals, on or off matrix. Cut stones are under Cut spinel.",FE,[
 X("Mogok spinel","Red and pink spinel octahedra from Mogok, Myanmar, the classic source; vivid 'glowing' pink and blue since 2000.",W+"Spinel",dt="octahedra, usually twinned"),
 X("Lục Yên spinel","Gem spinel from the marbles of Lục Yên District, Vietnam; blue spinel there is coloured by cobalt.",W+"Spinel",dt="octahedra in marble"),
 X("Mahenge spinel","Vivid pink spinel from Mahenge, Tanzania.",W+"Spinel",dt="crystals"),
 X("Badakhshan spinel","Red and pink spinel from the historic mines of Badakhshan (Afghanistan) and Gorno-Badakhshan (Tajikistan).",W+"Spinel",
   v=[("Black Prince's Ruby","","red spinel in the British Crown Jewels"),("Timur Ruby","","red spinel in the British Crown Jewels")],dt="crystals in marble"),
],t=["octahedron","twin (flat triangular plate)","in marble"]),
K("Chrysoberyl","Beryllium aluminium oxide mineral specimen, including cyclic 'trilling' twins and the colour-change variety alexandrite. Cut stones are under Alexandrite and chrysoberyl.",W+"Chrysoberyl",[
 X("Alexandrite","Chromium-bearing chrysoberyl that looks green in daylight and reddish under incandescent light.",W+"Chrysoberyl",
   v=[("Ural Mountains, Russia","","traditional source; named for the future Alexander II"),("Andhra Pradesh, India","",""),("Madagascar","",""),("Tanzania","","")],
   dt="crystal, trilling · colour change"),
 X("Chrysoberyl trilling","Cyclic twin of three chrysoberyl crystals at 120°, looking hexagonal.",W+"Chrysoberyl",dt="trilling or V-twin · yellow to green"),
 X("Cymophane","Translucent yellowish chatoyant chrysoberyl showing a cat's-eye from rutile needles.",W+"Chrysoberyl",a="cat's eye",
   v=[("Sri Lanka placers","",""),("Brazil placers","","")],dt="pebble, cabochon rough"),
]),
K("Hematite","Iron oxide mineral specimen (specular, botryoidal or rose crystals, tumbled pieces).",FE,[
 X("Kidney ore","Botryoidal, mammillary or reniform hematite.",W+"Hematite",v=[("Cumbria, England","","botryoidal hematite"),("Cleator Moor, Cumbria","","")],dt="botryoidal mass, polished section"),
 X("Iron rose","Rosette of bladed hematite crystals.",W+"Hematite",
   v=[("Fibbia, St Gotthard, Uri","","exceptional crystals"),("Cavradi, Tavetsch, Graubünden","",""),("Binntal, Valais","","")],dt="rosette"),
 X("Specularite","Specular hematite with a bright, mirror-like sheen.",W+"Hematite",a="specular hematite",dt="micaceous mass, crystals"),
 X("Elba hematite","Hematite crystals from Rio Marina, Elba, mined since Etruscan times.",H2+"hematite.pdf",dt="lustrous crystals"),
 X("Brazilian hematite","Large hematite crystals and blades from Minas Gerais and Bahia, Brazil.",H2+"hematite.pdf",
   v=[("Mesa Redonda and Congonhas do Campo","",""),("Itabira","",""),("Brumado mine, Bahia","","")],dt="crystals, blades"),
 X("Martite","Hematite pseudomorphs after magnetite.",W+"Hematite",dt="octahedral pseudomorphs"),
],t=["botryoidal","specular","crystal","tumbled stone"]),
K("Magnetite","Iron oxide mineral specimen (octahedra, clusters, on or off matrix).",FE,[
 X("Lodestone","Naturally magnetised magnetite that attracts iron; the first compasses used it.",W+"Lodestone",dt="rough mass · found near the surface"),
 X("Magnetite octahedra","Sharp magnetite octahedra from classic localities.",H2+"magnetite.pdf",
   v=[("Zillertal, Tirol, Austria","",""),("Binntal, Valais","",""),("Tilly Foster mine, Brewster, New York","",""),("Cerro de Mercado, Durango, Mexico","",""),("Magnet Cove, Arkansas","","")],
   dt="octahedra on matrix or loose"),
],t=["octahedron","lodestone","massive"]),
K("Rutile","Titanium oxide mineral specimen (needles, crystals, rutilated pieces, on or off matrix). Rutilated quartz is under Quartz.",FE,[
 X("Graves Mountain rutile","Rutile crystals from Graves Mountain, Lincoln County, Georgia.",H+"rutile.pdf",dt="crystals"),
 X("Alpine rutile","Rutile crystals from Cavradi (Graubünden) and Lodrino (Ticino), Switzerland.",H+"rutile.pdf",dt="crystals"),
 X("Brazilian rutile","Large rutile crystals from Conquista and Ibitiara, Bahia, Brazil.",H+"rutile.pdf",dt="large crystals"),
 X("Magnet Cove rutile","Rutile from Magnet Cove, Arkansas.",H+"rutile.pdf",dt="crystals"),
],t=["needle","crystal","twin","rutilated piece"]),
K("Cassiterite","Tin oxide mineral specimen (crystals, twins, on or off matrix).",FE,[
 X("Bolivian cassiterite","Fine cassiterite crystals from Araca, Oruro, Potosí, Huanuni and Llallagua, Bolivia.",H+"cassiterite.pdf",dt="crystals"),
 X("Cornish cassiterite","Cassiterite from the tin mines of Cornwall.",H+"cassiterite.pdf",dt="crystals"),
 X("Erzgebirge cassiterite","Cassiterite from Saxony and Bohemia: Marienberg, Altenberg, Cínovec (Zinnwald), Horní Slavkov.",H+"cassiterite.pdf",dt="crystals"),
 X("Panasqueira cassiterite","Cassiterite from Panasqueira, Portugal.",H+"cassiterite.pdf",dt="crystals"),
 X("Xuebaoding cassiterite","Cassiterite from the Xue Bao Diang (Xuebaoding) Mountains, Sichuan, China.",H+"cassiterite.pdf",dt="crystals"),
 X("Fazenda do Funil cassiterite","Large cassiterite crystals from Fazenda do Funil, Ferros, Minas Gerais.",H+"cassiterite.pdf",dt="large crystals"),
],t=["crystal","twin"]),
K("Cuprite","Copper oxide mineral specimen (red crystals, chalcotrichite, on or off matrix).","https://earthwonders.com/specimens/95206",[
 X("Onganja cuprite","Large, gem-quality cuprite crystals from Onganja near Seeis, Namibia, found in the 1970s and since mined out.",W+"Cuprite",y="1970s",dt="large crystals"),
 X("Chalcotrichite","Cuprite in greatly elongated hair-like crystals.",W+"Cuprite",v=[("Ray, Arizona","","")],dt="hair-like mats on matrix"),
 X("Bisbee cuprite","Large cuprite crystals from Bisbee, Arizona.",H+"cuprite.pdf",dt="crystals"),
 X("Tsumeb cuprite","Cuprite from Tsumeb, Namibia.",H+"cuprite.pdf",dt="crystals"),
 X("Ural cuprite","Cuprite from Bogoslovsk, Nizhny Tagil and Yekaterinburg, Urals.",H+"cuprite.pdf",dt="crystals"),
 X("Red Dome cuprite","Large cuprite crystals from the Red Dome mine, Chillagoe, Queensland.",H+"cuprite.pdf",dt="large crystals"),
],t=["octahedron","chalcotrichite","on copper"]),
K("Goethite","Iron oxyhydroxide mineral specimen (botryoidal, crystalline or pseudomorph pieces).",FE,[
 X("Cornish goethite","Exceptional goethite crystals from the Restormel mine (Lanlivery) and Botallack mine (St Just), Cornwall.",H+"goethite.pdf",dt="crystals"),
 X("Pikes Peak goethite","Goethite from the Pikes Peak district and Florissant, Colorado.",H+"goethite.pdf",dt="crystals"),
 X("Siegerland goethite","Goethite from Siegen, North Rhine-Westphalia, Germany.",H+"goethite.pdf",dt="botryoidal"),
],t=["botryoidal","pseudomorph","crystal"]),
K("Bixbyite","Manganese iron oxide mineral specimen (black cubic crystals, on or off matrix).",FE,[
 X("Thomas Range bixbyite","Black cubic bixbyite crystals from the Thomas Range, Juab County, Utah; it occurs in lithophysal cavities in rhyolite.",H+"bixbyite.pdf",dt="cubes on rhyolite"),
 X("Black Range bixbyite","Bixbyite from the Black Range, New Mexico.",H+"bixbyite.pdf",dt="cubes"),
 X("Otjiwarongo bixbyite","Large bixbyite crystals from the Otjiwarongo district, Namibia.",H+"bixbyite.pdf",dt="large crystals"),
]),
K("Uraninite","Uranium oxide mineral specimen (pitchblende, crystals or botryoidal pieces; radioactive).",FE,[
 X("Pitchblende","Massive, often botryoidal uraninite; mildly radioactive, so avoid dust and wash hands after handling.","https://www.fossilera.com/minerals/1-2-uraninite-pitchblende-specimen-uranium-based",
   v=[("Jáchymov (Joachimsthal), Czech Republic","",""),("Great Bear Lake, Northwest Territories","",""),("Shinkolobwe, Katanga, Congo","","")],dt="massive, botryoidal · radioactive"),
 X("Uraninite crystals","Uraninite crystals, notably from granite pegmatites.",H2.replace("pdfs/","")+"wp-content/uploads/2022/07/uraninite.pdf",
   v=[("Standpipe Hill, Topsham, Maine","","fine crystals"),("Sierra Albarrana, Córdoba, Spain","","large crystals"),("Wilberforce, Ontario","",""),("Spruce Pine, North Carolina","","")],dt="crystals · radioactive"),
],t=["radioactive"]),
]
notes=("Ten old kinds kept, Chrysoberyl added as new species kind (alexandrite, trillings, cymophane). Ruby-in-zoisite and ruby-in-fuchsite now sit under Corundum. Sources: Handbook of Mineralogy distribution lists (pdftotext), "
 "Wikipedia (Spinel, Chrysoberyl, Hematite, Lodestone, Cuprite, Anyolite), GIA, FossilEra uraninite handling note. Rutilated quartz is cross-referenced to Quartz (shelf 00_00). "
 "No years attached to famous spinels (none on fetched page). No brands or traditions.")
p="work/F6/shelves/00_04.json"; json.dump({"kinds":kinds,"brands":[],"traditions":[],"notes":notes},open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
