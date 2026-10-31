import json, os
H="https://www.handbookofmineralogy.org/pdfs/"; H2="https://handbookofmineralogy.org/pdfs/"
PG="https://minerals.net/mineral/pyrite/gallery"; SG="https://www.minerals.net/mineral/stibnite/gallery"
FE="https://www.fossilera.com/minerals-for-sale"
def X(n,d,s,a="",y="",v=None,dt=""):
    return {"n":n,"a":a,"d":d,"mk":"","y":y,"s":s,"v":[{"n":q[0],"mk":"","y":"","d":q[1]} for q in (v or [])],"dt":dt}
def K(n,d,s,xs,a="",t=None):
    k={"n":n,"a":a,"d":d,"s":s,"x":xs}
    if t: k["t"]=t
    return k
kinds=[
K("Pyrite","Iron sulfide mineral specimen (cubes, clusters, suns, on or off matrix).",FE,[
 X("Navajún pyrite cubes","Pyrite cubes and sculptural crystal groups from Navajún, La Rioja, Spain.",PG,
   v=[("Victoria mine (Mina Ampliación a Victoria), Navajún","cubes in matrix, intergrown cubes"),("Ambasaguas, Spain","sculptural crystal groups")],
   dt="single cube to cabinet group · on or off matrix · penetration twins"),
 X("Huanzala pyrite","Pyrite groups and octahedra from the Huanzala mine, Huallanca, Peru.",PG,
   v=[("Huanzala mine","crystal groupings, octahedra, parallel growths")],dt="miniature to cabinet · often with quartz"),
 X("Quiruvilca pyrite","Exceptional pyrite crystal clusters from the Quiruvilca mine, La Libertad, Peru.",H+"pyrite.pdf",dt="cluster"),
 X("Elba pyrite","Classic pyritohedral pyrite from Rio Marina, Elba, Italy.",H+"pyrite.pdf",v=[("Rio Marina, Elba","")],dt="pyritohedron, striated"),
 X("Pyrite sun","Flat radiating pyrite disc ('sun') from Sparta, Illinois.",H+"pyrite.pdf",v=[("Sparta, Randolph County, Illinois","sold as suns or dollars")],dt="disc"),
 X("Pyrite concretion","Rounded nodule, sphere or radiating concretion of pyrite from sedimentary rocks.",PG,
   v=[("Volga River near Ulyanovsk, Russia","iridescent ('rainbow') concretions"),("Dongchuan, Yunnan, China","spheres on shale")],dt="nodule, sphere"),
 X("Pyritised fossil","Fossil replaced by pyrite.",PG,v=[("near Moscow, Russia","pyrite pseudomorph after fossil")],dt="pseudomorph"),
],t=["cube","pyritohedron","octahedron","cluster","on matrix"]),
K("Galena","Lead sulfide mineral specimen (cubes, octahedra, clusters, on or off matrix).",FE,[
 X("Tri-State galena","Galena cubes from the Joplin–Picher Tri-State district of Missouri, Kansas and Oklahoma.",H2+"galena.pdf",
   v=[("Joplin, Jasper County, Missouri",""),("Galena, Cherokee County, Kansas",""),("Picher, Ottawa County, Oklahoma","")],dt="cube"),
 X("Sweetwater galena","Brilliant galena crystals from the Viburnum Trend, Missouri.",H2+"galena.pdf",v=[("Sweetwater (Milliken) mine, Reynolds County","")],dt="cubo-octahedra"),
 X("Naica and Santa Eulalia galena","Galena from the Chihuahua mining districts of Mexico.",H2+"galena.pdf",dt="cubes"),
 X("European classic galena","Galena from historic European mining districts.",H2+"galena.pdf",
   v=[("Příbram, Czech Republic",""),("Freiberg, Saxony",""),("Neudorf and Clausthal, Harz",""),("Alston Moor, Cumbria",""),("Wanlockhead, Scotland",""),("Mogul mine, Silvermines, Ireland","")],dt="cube, octahedron, skeletal"),
],t=["cube","cubo-octahedron","octahedron","cleavage"]),
K("Sphalerite","Zinc sulfide mineral specimen (crystals, clusters, on or off matrix).",FE,[
 X("Picos de Europa sphalerite","Transparent sphalerite crystals from the Aliva mine, Cantabria, Spain.",H+"sphalerite.pdf",v=[("Aliva mine, Picos de Europa","")],dt="transparent crystals, cleavage pieces"),
 X("Dalnegorsk sphalerite","Sphalerite crystals from Dalnegorsk, Primorsky Krai, Russia.",H+"sphalerite.pdf",dt="cabinet groups"),
 X("Tri-State sphalerite","Sphalerite crystals from the Joplin–Baxter Springs–Picher district.",H+"sphalerite.pdf",
   v=[("Joplin, Missouri",""),("Baxter Springs, Kansas",""),("Picher, Oklahoma","")],dt="crystals"),
 X("Elmwood sphalerite","Sphalerite crystals from the Elmwood mine, Carthage, Tennessee.",H+"sphalerite.pdf",dt="crystals"),
 X("Santa Eulalia and Naica sphalerite","Sphalerite from Chihuahua, Mexico.",H+"sphalerite.pdf",dt="crystal groups"),
 X("Lengenbach colourless sphalerite","Colourless sphalerite crystals from the Lengenbach quarry, Binntal, Switzerland.",H+"sphalerite.pdf",dt="micro to thumbnail"),
],t=["tetrahedral crystal","cleavage piece","with galena"]),
K("Chalcopyrite","Copper iron sulfide mineral specimen (crystals, clusters, on or off matrix).",FE,[
 X("Groundhog chalcopyrite","Large chalcopyrite crystals from the Groundhog mine, Vanadium, New Mexico.",H+"chalcopyrite.pdf",dt="large crystals"),
 X("French Creek chalcopyrite","Chalcopyrite crystals from French Creek, Chester County, Pennsylvania.",H+"chalcopyrite.pdf",dt="crystals"),
 X("Nababiep chalcopyrite","Large chalcopyrite crystals from the Nababiep mine, Cape Province, South Africa.",H+"chalcopyrite.pdf",dt="large crystals"),
 X("Japanese chalcopyrite","Chalcopyrite from the Ani and Arakawa mines, Akita Prefecture.",H+"chalcopyrite.pdf",dt="crystals"),
 X("Huaron chalcopyrite","Chalcopyrite from Huaron, Peru.",H+"chalcopyrite.pdf",dt="crystals"),
],t=["tetrahedral crystal","massive","massive ore"]),
K("Stibnite","Antimony sulfide mineral specimen (blade and needle clusters, on or off matrix).",FE,[
 X("Ichinokawa stibnite","Magnificent groups of stibnite crystals from the Ichinokawa mine near Saijo, Ehime, Japan.",H+"stibnite.pdf",
   v=[("Ichinokawa mine, Ehime Prefecture","classic groups, twinned and curved crystals")],dt="single blade to museum group · crystals to 0.65 m in the species"),
 X("Xikuangshan stibnite","Bladed stibnite groups from the Xikuangshan mine, Lengshuijiang, Hunan, China, economically very important.",H+"stibnite.pdf",dt="interconnected blades, elongated groups"),
 X("Wuling stibnite","Huge stibnite crystal groups and sword-like crystals from the Wuling antimony mine, Jiangxi, China.",SG,dt="large groups, crosses"),
 X("Baia Mare stibnite","Stibnite from Baia Sprie and Herja, Maramureș, Romania.",H+"stibnite.pdf",v=[("Baia Sprie (Felsőbánya)","acicular sprays"),("Herja (Kisbánya)","radiating groups")],dt="sprays, radiating groups"),
 X("Nevada stibnite","Stibnite crystals from the White Caps mine (Manhattan) and Murray mine, Nevada.",H+"stibnite.pdf",dt="terminated clusters"),
],t=["blade","needle spray","on matrix"]),
K("Cinnabar","Mercury sulfide mineral specimen: bright red crystals, twins or massive ore, on or off matrix.",H+"cinnabar.pdf",[
 X("Hunan twinned cinnabar","Exceptional twinned cinnabar crystals from the Tsar Tien mine, Hunan, China.",H+"cinnabar.pdf",dt="contact twins"),
 X("Guizhou cinnabar","Cinnabar crystals from Tongren (Tongrin), Wanshanchang and elsewhere in Guizhou, China.",H+"cinnabar.pdf",dt="twins and crystals on matrix"),
 X("Almadén cinnabar","Cinnabar ore from Almadén, Ciudad Real, Spain.",H+"cinnabar.pdf",dt="massive, granular"),
 X("Idrija cinnabar","Cinnabar from Idrija, Slovenia.",H+"cinnabar.pdf",dt="massive"),
 X("New Almaden cinnabar","Cinnabar from New Almaden and New Idria, California.",H+"cinnabar.pdf",dt="massive, crystals"),
],t=["twinned crystal","on matrix","massive ore"]),
K("Realgar","Arsenic sulfide mineral specimen (red crystals, massive pieces, on or off matrix).",FE,[
 X("Shimen realgar","Red realgar crystals from the Shimen mine, Hunan, China.",H+"realgar.pdf",dt="crystals · disintegrates on long exposure to light"),
 X("Getchell realgar","Fine large realgar crystals from the Getchell mine, Humboldt County, Nevada.",H+"realgar.pdf",dt="crystals"),
 X("Romanian realgar","Realgar from Baia Sprie, Cavnic and Săcărâmb, Romania.",H+"realgar.pdf",dt="crystals"),
 X("Allchar realgar","Realgar from Alšar (Allchar), North Macedonia.",H+"realgar.pdf",dt="crystals"),
],t=["crystal","massive","with orpiment"]),
K("Orpiment","Arsenic sulfide mineral specimen (yellow crystals, massive pieces, on or off matrix).",FE,[
 X("Quiruvilca orpiment","Exceptional orpiment specimens from the Quiruvilca mine, La Libertad, Peru.",H+"orpiment.pdf",dt="crystals on matrix"),
 X("Twin Creeks orpiment","Fine orpiment from the Twin Creeks mine, Humboldt County, Nevada.",H+"orpiment.pdf",dt="crystals"),
 X("Shimen orpiment","Large orpiment crystals from the Shimen mine, Hunan, China.",H+"orpiment.pdf",dt="large crystals, with realgar"),
 X("Zarshuran orpiment","Fine orpiment crystals from the Zarshuran gold deposit, north of Takab, Iran.",H+"orpiment.pdf",dt="crystals"),
],t=["crystal","foliated mass"]),
K("Marcasite","Iron sulfide (orthorhombic) mineral specimen (cockscomb, spearhead, nodules, on or off matrix).",FE,[
 X("Cockscomb marcasite","Twinned marcasite in cockscomb or spearhead groups.",H+"marcasite.pdf",
   v=[("Tri-State district (Joplin, Picher, Baxter Springs)",""),("Kent chalk, Folkestone–Dover, England","")],dt="cockscomb, spearhead groups"),
 X("Czech marcasite","Marcasite from the coal basins of North Bohemia.",H+"marcasite.pdf",v=[("Vintířov",""),("Most",""),("Osek","")],dt="nodules, crystals"),
 X("Cap Blanc-Nez marcasite","Marcasite nodules from the chalk of Cap Blanc-Nez, Pas-de-Calais, France.",H+"marcasite.pdf",dt="nodule"),
],t=["cockscomb","spearhead","nodule"]),
K("Pyrrhotite","Iron sulfide mineral specimen (tabular crystals, clusters, on or off matrix).",FE,[
 X("Dalnegorsk pyrrhotite","Very large pyrrhotite crystals from Dalnegorsk, Primorsky Krai, Russia.",H+"pyrrhotite.pdf",dt="tabular crystals, rosettes"),
 X("Trepča pyrrhotite","Pyrrhotite from the Stari Trg mine, Trepča.",H+"pyrrhotite.pdf",dt="rosettes"),
 X("Morro Velho pyrrhotite","Large pyrrhotite crystals from the Morro Velho gold mine, Nova Lima, Minas Gerais, Brazil.",H+"pyrrhotite.pdf",dt="large crystals"),
 X("Herja pyrrhotite","Well-crystallised pyrrhotite from Herja, Baia Mare, Romania.",H+"pyrrhotite.pdf",dt="crystals"),
 X("Santa Eulalia pyrrhotite","Pyrrhotite from the Potosí and San Antonio mines, Santa Eulalia, Mexico.",H+"pyrrhotite.pdf",dt="crystals"),
],t=["tabular crystal","rosette"]),
K("Bournonite","Lead copper antimony sulfosalt mineral specimen (cogwheel twins, crystals on matrix).",FE,[
 X("Herodsfoot bournonite","Exceptional bournonite crystals from the Herodsfoot mine, Lanreath, Cornwall.",H2+"bournonite.pdf",dt="cogwheel twins"),
 X("Wheal Boys bournonite","Bournonite from its type locality, Wheal Boys, St Endellion, Cornwall.",H2+"bournonite.pdf",dt="crystals"),
 X("Yaogangxian bournonite","Bournonite from the Yaogangxian mine, Chenzhou, Hunan, China.",H2+"bournonite.pdf",dt="crystals"),
 X("Bolivian bournonite","Fine bournonite crystals from the Víboras mine, Machacamarca, Potosí, and other Bolivian mines.",H2+"bournonite.pdf",dt="crystals"),
 X("Quiruvilca bournonite","Bournonite from the Quiruvilca mine, La Libertad, Peru.",H2+"bournonite.pdf",dt="crystals"),
],t=["cogwheel twin","crystal on matrix"]),
K("Proustite","Silver arsenic sulfosalt mineral specimen (red crystals, on or off matrix).",FE and "https://www.mineralauctions.com/items/proustite-with-imiterite-xanthoconite-et-al-113619",[
 X("Chañarcillo proustite","Exceptional proustite crystals from Chañarcillo, south of Copiapó, Atacama, Chile.",H+"proustite.pdf",dt="crystals"),
 X("Saxony proustite","Proustite from the Himmelsfürst mine near Freiberg and Niederschlema, Saxony.",H+"proustite.pdf",dt="crystals"),
 X("Sainte-Marie-aux-Mines proustite","Proustite from Sainte-Marie-aux-Mines, Alsace, France.",H+"proustite.pdf",dt="crystals"),
 X("Batopilas proustite","Proustite from Batopilas, Chihuahua, Mexico.",H+"proustite.pdf",dt="crystals"),
],t=["crystal","on matrix"]),
K("Chalcocite","Copper sulfide mineral specimen (crystals, massive pieces, on or off matrix).",FE,[
 X("Bristol chalcocite","Exceptional chalcocite crystals from Bristol, Hartford County, Connecticut.",H+"chalcocite.pdf",dt="crystals"),
 X("Cornish chalcocite","Fine chalcocite crystals from St Just, St Ives, Camborne and Redruth, Cornwall.",H+"chalcocite.pdf",dt="crystals"),
 X("Flambeau chalcocite","Chalcocite crystals from the Flambeau mine, Ladysmith, Wisconsin.",H+"chalcocite.pdf",dt="crystals"),
 X("Nababiep and Messina chalcocite","Large chalcocite crystals from South Africa.",H+"chalcocite.pdf",dt="large crystals"),
 X("Butte chalcocite","Chalcocite from Butte, Montana.",H+"chalcocite.pdf",dt="crystals, massive"),
],t=["crystal","massive"]),
K("Stephanite","Silver antimony sulfosalt mineral specimen (black crystals, on or off matrix).","https://www.mineralauctions.com/items/stephanite-with-polybasite-and-pyrargyrite-112462",[
 X("St Andreasberg stephanite","Exceptional stephanite crystals from St Andreasberg, Harz, Germany.",H+"stephanite.pdf",dt="crystals"),
 X("Freiberg stephanite","Stephanite from its type locality, Freiberg, Saxony.",H+"stephanite.pdf",dt="crystals"),
 X("Husky mine stephanite","Fine stephanite from the Husky mine, Elsa, Yukon.",H+"stephanite.pdf",dt="crystals"),
 X("Mexican stephanite","Large stephanite crystals from Arizpe, Sonora, and from Guanajuato and Fresnillo.",H+"stephanite.pdf",dt="crystals"),
 X("Monte Narba stephanite","Fine stephanite twins from Monte Narba, Sarrabus, Sardinia.",H+"stephanite.pdf",dt="twins"),
],t=["crystal","pseudohexagonal twin"]),
]
notes=("13 old kinds kept one-to-one, Cinnabar added as a new species kind. Archetypes are classic localities from the Handbook of Mineralogy distribution lists (MSA/Mineral Data Publishing PDFs, text read via pdftotext) "
 "and minerals.net pyrite and stibnite galleries. Left out: Trepča galena and sphalerite and Dalnegorsk galena (not named in the fetched Distribution lists; Trepča appears only for pyrrhotite); "
 "No makers, so no brands; no artisan traditions apply.")
p="work/F6/shelves/00_02.json"; json.dump({"kinds":kinds,"brands":[],"traditions":[],"notes":notes},open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
