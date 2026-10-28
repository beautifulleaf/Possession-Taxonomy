import json,copy
P='out/F6.json'
d=json.load(open(P))
W='https://en.wikipedia.org/wiki/'
def find(shelf):
    for dp in d['depts']:
        for s in dp['s']:
            if s['n']==shelf: return dp,s
    raise KeyError(shelf)
def kind(shelf,name):
    for k in find(shelf)[1]['k']:
        if k['n']==name: return k
    raise KeyError(name)
def arch(n,dsc,s,y="",mk="",v=None,dt="",a=""):
    return {"n":n,"a":a,"d":dsc,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
def ver(n,dsc,y=""): return {"n":n,"mk":"","y":y,"d":dsc}
allnames={k['n'] for dp in d['depts'] for s in dp['s'] for k in s['k']}
# F6-1
new=[
("Sulfides & sulfosalts","Bornite","peacock ore · peacock copper","Copper-iron sulfide (Cu5FeS4) that tarnishes to an iridescent blue and purple; also a copper ore.",W+"Bornite",[]),
("Sulfides & sulfosalts","Molybdenite","","Soft, graphite-like molybdenum disulfide (MoS2), the chief ore of molybdenum.",W+"Molybdenite",[]),
("Halides & borates","Atacamite","","Bright to dark green copper hydroxychloride, Cu2Cl(OH)3, named after Chile's Atacama Desert.",W+"Atacamite",[]),
("Halides & borates","Boleite","","Deep-blue cube-forming halide mineral from El Boleo, Santa Rosalía, Mexico; crystals often twin into pseudocubes.",W+"Boleite",
  [arch("Boleo and Santa Rosalía boleite","Deep-blue pseudocubic crystals from the type locality, El Boleo mine near Santa Rosalía, Baja California Sur, Mexico.",W+"Boleite",y="described 1891",dt="cube size · twinned pseudocubes · matrix")]),
("Halides & borates","Creedite","","Rare calcium aluminium hydroxyl-fluoride sulfate, colourless, white, violet or orange, often in radiating sprays.",W+"Creedite",
  [arch("Navidad Mine creedite","Radiating sprays of creedite from the Navidad Mine, Santa Eulalia district, Chihuahua, Mexico.",W+"Creedite",dt="spray size · colour · matrix")]),
("Carbonates","Witherite","","Barium carbonate (BaCO3) of the aragonite group, named for William Withering; fluoresces blue under ultraviolet.",W+"Witherite",
  [arch("Hexham witherite","Witherite from lead-ore veins at Hexham, Northumberland, England.",W+"Witherite",dt="crystal habit · associated galena or barite")]),
("Sulfates, chromates & tungstates","Hanksite","","Colourless to pale yellow sulfate carbonate evaporite, first described in 1888 from Searles Lake, California; water-soluble.",W+"Hanksite",
  [arch("Searles Lake hanksite","Short hexagonal prismatic crystals from the type locality, Searles Lake, California.",W+"Hanksite",y="1888",dt="crystal size · tabular or prismatic · halite or trona association")]),
("Sulfates, chromates & tungstates","Chalcanthite","","Blue, water-soluble copper sulfate pentahydrate (CuSO5·5H2O) from oxidised copper deposits; fragile, and easily grown synthetically.".replace("CuSO5·5H2O","CuSO4·5H2O"),W+"Chalcanthite",[]),
("Pyroxenes & amphiboles","Aegirine","acmite","Dark green to greenish-black sodium iron pyroxene, NaFe3+Si2O6, found in alkaline igneous rocks and pegmatites.",W+"Aegirine",
  [arch("Mont Saint-Hilaire aegirine","Dark green prismatic aegirine crystals from Mont Saint-Hilaire, Quebec, Canada.",W+"Aegirine",dt="crystal length · lustre · associated minerals")]),
("Dioptase, charoite & other silicates","Astrophyllite","","Rare brown to golden-yellow potassium iron titanium silicate whose bladed crystals radiate in star-like aggregates.",W+"Astrophyllite",[]),
("Oxides","Zincite","","Zinc oxide mineral, (Zn,Mn)O; red natural crystals come from Franklin and Sterling Hill, New Jersey, and synthetic crystals form in zinc smelting.",W+"Zincite",[]),
("Oxides","Anatase","","Tetragonal titanium dioxide, TiO2, a polymorph of rutile; sharp dark blue to black octahedra or honey-yellow crystals.",W+"Anatase",[]),
]
for sh,n,a,dsc,s,x in new:
    assert n not in allnames,n
    k={"n":n,"a":a,"d":dsc,"s":s}
    if x: k["x"]=x
    find(sh)[1]['k'].append(k)
# F6-2
sh="Vertebrate fossils"
vf=find(sh)[1]['k']
old=kind(sh,"Dinosaur fossil"); ox={a['n']:a for a in old['x']}
tooth={"n":"Dinosaur tooth","a":"dinosaur teeth","d":"Fossil tooth of a dinosaur, listed by taxon; collecting and sale rules vary with country and land ownership.","s":old['s'],"x":[
 arch("Tyrannosaurus tooth","Robust, banana-shaped tooth of T. rex, named by Osborn in 1905; the largest known is about 30.5 cm including the root.",W+"Tyrannosaurus",y="Late Maastrichtian",dt="Hell Creek Formation, Montana · crown length · root present or absent"),
 ox["Spinosaurus tooth"],ox["Carcharodontosaurus tooth"],
 {**ox["Hadrosaur material"],"n":"Hadrosaur tooth","d":"Tooth of a duck-billed dinosaur, stacked with others in a dental battery; Late Cretaceous of Alberta and Montana.","dt":"battery blocks · single teeth · Dinosaur Park Formation"}]}
claw={"n":"Dinosaur claw & bone","a":"dinosaur claw · dinosaur bone","d":"Fossil claw, horn, vertebra or other bone of a dinosaur, listed by taxon.","s":old['s'],"x":[
 arch("Allosaurus","Large Late Jurassic theropod named by Marsh in 1877; most remains come from the Morrison Formation of North America.",W+"Allosaurus",y="1877",
      v=[ver("Big Al (MOR 693)","About 95% complete subadult found in 1991 at Howe Ranch Quarry, Wyoming","1991")],dt="Morrison Formation · tooth, claw or bone"),
 arch("Raptor sickle claw","Large curved claw on the second toe of dromaeosaurids such as Velociraptor; its function is debated.",W+"Dromaeosauridae",dt="claw length · sheath cast or bone core · restoration"),
 ox["Triceratops"]]}
egg={"n":"Dinosaur egg & eggshell","a":"dinosaur egg · eggshell","d":"Fossil egg, nest or eggshell fragment of a dinosaur.","s":old['s'],"x":[
 ox["Dinosaur egg"],
 arch("Hypselosaurus egg","Large eggs, about 30 cm long, found in Provence, France since 1846; the genus is now regarded as dubious.",W+"Hypselosaurus",y="1846",dt="Provence · egg length · shell thickness")]}
i=vf.index(old); vf[i:i+1]=[tooth,claw,egg]
mr=kind(sh,"Marine reptile fossil")
mr['x'].append(arch("Ichthyosaur","Dolphin-like marine reptile of the Triassic to Cretaceous; first skeleton found at Lyme Regis, with over 4,000 skeletons from Holzmaden, Germany.",W+"Ichthyosauria",y="c. 250–94 million years ago",
  v=[ver("Lyme Regis ichthyosaur","Skull found by Joseph Anning in 1811; Mary Anning secured the torso in 1812","1811"),ver("Holzmaden ichthyosaur","Posidonia Shale of the Early Jurassic, many with soft tissue preserved")],dt="Lyme Regis · Holzmaden · vertebrae, paddle bones, skeleton"))
# F6-3
rock=find("Rocks, nodules & teaching sets")[0]
rock['s'].append({"n":"Viewing stones","k":[{"n":"Viewing stone","a":"suiseki · gongshi · scholar's rock","d":"Natural stone appreciated for the landscape or form it suggests, displayed on a base or tray rather than cut or polished.","s":W+"Suiseki","t":["landscape stone","object stone"],"x":[
 arch("Suiseki","Japanese viewing stone, unaltered except for a base, usually dark and subdued; displayed on a daiza or in a suiban.",W+"Suiseki",y="from c. 600 AD in Japan",
   v=[ver("Landscape stone (sansui keijō-seki)","Suggests scenery such as distant mountains, islands or waterfalls"),ver("Object stone (keishō-seki)","Suggests a figure, animal, hut or boat")],dt="daiza (carved wooden base) · suiban (tray with sand or water) · colour · place of origin"),
 arch("Gongshi (scholar's rock)","Chinese viewing stone prized for thinness, openness, perforation and wrinkling; set on a carved wooden pedestal.",W+"Scholar%27s_rock",y="Tang dynasty onward",
   v=[ver("Taihu stone","Limestone from Lake Tai, Jiangsu; one of three main Chinese sources with Lingbi and Yingde stones")],dt="pedestal (rosewood) · size · source")]}]})
# F6-6
dp,tr=find("Trilobites & arthropods")
fi=kind("Amber & copal","Fossil insect"); find("Amber & copal")[1]['k'].remove(fi)
tr['k'].append(fi); tr['n']="Arthropods & insects"
# F6-4
sk=find("Skulls & skeletons")[1]['k']
ms=kind("Skulls & skeletons","Mammal skull")
euro=[a for a in ms['x'] if a['n']=="European skull mount"][0]
sk=[k for k in sk if k['n'] not in("Mammal skull","Bird skull","Reptile skull","Fish skull")]
a=arch(euro['n'],euro['d'],euro['s'],dt="boiled or beetle-cleaned · plaque · with or without horns")
skull={"n":"Animal skull","a":"cleaned skull","d":"Cleaned real skull of a mammal, bird, reptile or fish kept as a specimen. Legality varies; protected species and CITES listings restrict trade.","s":ms['s'],
 "t":["mammal","bird","reptile","fish"],"x":[a]}
sh_=find("Skulls & skeletons")[1]; sh_['k']=[skull]+sk
# taxidermy mount types
tm=kind("Taxidermy mounts","Taxidermy mammal mount")
tm['x']=[x for x in tm['x'] if x['n'] not in("Full mount","Shoulder mount","Skull mount")]
tm['t']=["full mount","shoulder mount","head mount","skull mount","freeze-dried mount","study skin"]
tm['d']="Mammal skin preserved and mounted as in life; the Akeley method of clay model, plaster mould and fitted hide became standard. CITES and wildlife law apply."
# F6-5
ds=find("Display domes & stands")[1]
disp={"n":"Specimen display","a":"display dome · stand · frame case · thumbnail box","d":"Dome, stand, frame case or single-specimen box made to hold and show one specimen. A box holding several is in Furniture & Storage.",
 "s":"https://store.smm.org/products/glass-dome-with-wood-base",
 "t":["glass or acrylic dome with base","acrylic riser","museum putty","floating frame","Riker mount","perky box","thumbnail box","gem jar"]}
ds['k']=[disp]
json.dump(d,open('out/F6.tmp','w'),ensure_ascii=False,indent=1)
