import json, os, shutil, re
R='/home/user/Possession-Taxonomy/rebuild/'
BAK=R+'work/STR_F6/bak/F6.json'   # always rebuild from the backup (idempotent)
d=json.load(open(BAK))
W='https://en.wikipedia.org/wiki/'
kinds={}; loc={}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            kinds[k['n']]=k
before=dict(depts=len(d['depts']),shelves=sum(len(x['s']) for x in d['depts']),kinds=len(kinds),
            arch=sum(len(k.get('x',[])) for k in kinds.values()))
oldb=[dp.get('b',[]) for dp in d['depts']]
renames={}

def newk(n,dd,s,a='',tt=None):
    k={'n':n,'a':a,'d':dd,'s':s}
    if tt: k['tt']=tt
    kinds[n]=k; return k

# ---------- demotions (generic archetypes become models in m, versions kept) ----------
DEM={
'Natural diamond':['Colourless to light-colour diamond','Fancy red, green, black and grey diamond'],
'Lab-grown diamond':['HPHT lab-grown diamond','CVD lab-grown diamond','Treated pink and green lab-grown diamond'],
'Lab-created coloured gemstone':['Hydrothermal synthetic emerald'],
'Moissanite and diamond simulants':['Synthetic white sapphire','Glass paste and white zircon'],
'Ruby':['Star ruby'],
'Sapphire':['Fancy and parti-colour sapphire','Star sapphire','Colour-change sapphire'],
'Cut spinel':['Red and pink spinel'],
'Pearl':['Keshi pearl','Baroque pearl'],
'Jet':['Jet imitations'],
'Amber':['Pressed and imitation amber'],
'Ammolite':['Ammolite doublet and triplet'],
'Dinosaur egg & eggshell':['Dinosaur egg'],
'Trace fossil':['Dinosaur footprint','Coprolite','Gastrolith','Fossil burrow'],
'Belemnite':['Jurassic belemnite guards'],
'Basalt':['Columnar basalt'],'Limestone':['Fossiliferous limestone'],'Fulgurite':['Sand fulgurite'],
'Geode and thunder egg':['Brazilian amethyst geode'],
'Giant clam shell':['Giant clam'],'Chambered nautilus shell':['Chambered nautilus'],'Brachiopod shell':['Lamp shell'],
'Conch and stromb shell':['Spider conch'],'Harp shell':['Harpa'],'Dried starfish':['Sea star','Brittle star'],
'Sea urchin test':['Heart urchin'],
'Taxidermy mammal mount':['Indian tiger and leopard trophy mount'],
'Taxidermy bird mount':['Study skin'],'Taxidermy fish mount':['Skin mount','Reproduction mount'],
'Taxidermy reptile mount':['Celluloid-finished reptile mount'],
'Animal skull':['European skull mount'],
'Antler or horn':['Shed antler','Ram and buffalo horn'],
'Tusk specimen':['Warthog tusk','Elephant, walrus and hippo ivory'],
'Shark or fish jaw':['Great white shark jaw'],
'Egg or nest specimen':['Ostrich egg','Oological egg collection'],
'Feather specimen':['Contour and flight feather'],'Fluid-preserved specimen':['Ethanol wet specimen'],
'Element cube':['Bismuth density cube','Rhenium density cube'],
'Element ampoule':['Noble gas glow ampoule','Uranium ampoule'],
'Encased element sample':['Lucite element cube'],
'Element crystal':['Bismuth hopper crystal','Gallium'],
'Native gold':['Gold nugget','Wire gold','Leaf gold','Crystallised gold','Dendritic gold'],
'Native silver':['Slab silver'],'Native platinum':['Platinum nugget'],'Native bismuth':['Lab-grown hopper bismuth'],
'Pyrite':['Pyrite concretion','Pyritised fossil'],
'Corundum':['Large corundum crystals'],'Beryl':['Giant beryl crystals'],
'Biotite':['Biotite books'],'Muscovite':['Sheet mica book'],'Chabazite':['Chabazite rhombs'],
'Magnetite':['Magnetite octahedra'],'Uraninite':['Uraninite crystals'],'Prehnite':['Prehnite botryoids'],
'Scheelite':['Synthetic scheelite'],'Jadeite':['Synthetic jadeite'],'Kyanite':['Blue kyanite blades'],
'Lapis lazuli and lazurite':['Lazurite crystals'],'Fluor-liddicoatite':['Liddicoatite slice'],
'Clinochlore':['Chlorite quartz'],'Benitoite':['Benitoite from other claims'],
'Rhodochrosite':['Colorado rhodochrosite (other mines)'],'Vivianite':['Bolivian vivianite (other mines)'],
'Charoite':['Chara River name'],'Serandite':["Sérand's mineral"],'Brochantite':['Brochantite pseudomorph'],
'Haüyne':['Gem haüyne'],'Apatite':['Gem-colour apatite'],'Chrysocolla':['Gem chrysocolla'],
'Orthoclase':['Madagascan gem orthoclase'],
}
demoted=[]
for kn,xs in DEM.items():
    k=kinds[kn]; keep=[]; m=[list(t) for t in (k.get('m') or [])]
    have={tuple(t) for t in m}
    for x in k.get('x',[]):
        if x['n'] in xs:
            for e in [[x['n'],x.get('mk','')]]+[[v['n'],v.get('mk','')] for v in x.get('v',[]) or []]:
                if tuple(e) not in have: m.append(e); have.add(tuple(e))
            demoted.append(kn+': '+x['n'])
        else: keep.append(x)
    assert len(keep)+len(xs)==len(k.get('x',[])), kn
    k['x']=keep
    if m: k['m']=m
# Cowrie / conch / abalone species named in old types move to m
for kn,ms in {'Cowrie':['Atlantic deer cowrie','Chestnut cowrie']}.items():
    k=kinds[kn]; m=k.setdefault('m',[]); 
    for e in ms:
        if [e,''] not in m: m.append([e,''])
# Sand dollar archetype moves with its kind (as model)
sd=[x for x in kinds['Sea urchin test']['x'] if x['n']=='Sand dollar']
kinds['Sea urchin test']['x']=[x for x in kinds['Sea urchin test']['x'] if x['n']!='Sand dollar']

# ---------- new kinds ----------
newk('Arsenopyrite','Silvery iron arsenic sulfide in striated prismatic crystals; the chief ore of arsenic.',W+'Arsenopyrite')
newk('Covellite','Indigo-blue copper sulfide, often iridescent, found as platy masses and crusts.',W+'Covellite')
newk('Tetrahedrite','Grey copper antimony sulfosalt in tetrahedral crystals; the name of a group that includes silver ores.',W+'Tetrahedrite')
newk('Millerite','Nickel sulfide in hair-fine brassy needles, often as radiating sprays in cavities.',W+'Millerite')
newk('Cryolite','White to colourless sodium aluminium fluoride, famous from Ivittuut in Greenland; once used in aluminium smelting.',W+'Cryolite')
newk('Ilmenite','Black metallic iron titanium oxide; the main ore of titanium.',W+'Ilmenite')
newk('Pyrolusite','Black manganese dioxide that forms dendrites and soft sooty masses; a main manganese ore.',W+'Pyrolusite')
newk('Brucite','Magnesium hydroxide in pearly, translucent sheets and plates, found in serpentine rock.',W+'Brucite')
newk('Chromite','Black metallic iron chromium oxide, the only ore of chromium, found in layered igneous rocks.',W+'Chromite')
newk('Strontianite','White to pale green strontium carbonate in sprays and crusts, named for Strontian in Scotland.',W+'Strontianite')
newk('Hydrozincite','White to pale zinc carbonate crust that glows blue-white under ultraviolet light.',W+'Hydrozincite')
newk('Jarosite','Yellow to brown potassium iron sulfate crusts, found in oxidised ore and also on Mars.',W+'Jarosite')
newk('Pyrope','Deep red magnesium aluminium garnet, found in kimberlite and peridotite; the red end of the garnet group.',W+'Pyrope')
newk('Petalite','Colourless to pink lithium aluminium silicate; a lithium ore, also cut as a collector gem.',W+'Petalite')
newk('Thomsonite','Zeolite that forms radiating white sprays and banded nodules; Lake Superior material is cut as cabochons.',W+'Thomsonite',tt=[["Habit",["Radiating spray","Nodule"]]])
newk('Cut kunzite','Pink to lilac gem variety of spodumene, cut from large clean crystals.',W+'Kunzite','kunzite · hiddenite')
newk('Cut zircon','Zirconium silicate gem in blue, colourless, yellow, brown and red; unrelated to cubic zirconia.',W+'Zircon','zircon gem · jargoon')
newk('Tusk shell','Tooth-shaped tubular shell of a scaphopod, open at both ends.',W+'Scaphopoda','scaphopod shell · dentalium')
newk('Sand dollar','Flat, round test of a burrowing sea urchin, marked with a five-petal pattern.',W+'Sand_dollar')
kinds['Sand dollar']['m']=[[x['n'],''] for x in sd]
newk('Cuttlebone','Chalky internal shell of a cuttlefish, kept as a specimen.',W+'Cuttlebone','cuttlefish bone')
newk('Chiton shell','Shell of eight overlapping plates from a chiton, kept whole or as loose plates.',W+'Chiton','coat-of-mail shell')
RK=W+'List_of_rock_types'
for n,dd in [('Gabbro','Coarse, dark intrusive igneous rock rich in pyroxene and plagioclase.'),
 ('Andesite','Fine-grained grey volcanic rock between basalt and rhyolite, common in mountain arcs.'),
 ('Pumice','Light, frothy volcanic glass full of gas bubbles, light enough to float.'),
 ('Tuff','Rock made of compacted volcanic ash.'),
 ('Conglomerate','Sedimentary rock of rounded pebbles set in a finer cement.'),
 ('Shale','Fine, layered sedimentary rock of compacted mud that splits into thin flakes.'),
 ('Chert and flint','Hard, fine-grained silica rock that breaks with sharp edges; flint is the nodular form found in chalk.'),
 ('Schist','Metamorphic rock with visible flaky minerals aligned in layers.'),
 ('Gneiss','Coarse metamorphic rock with light and dark mineral bands.'),
 ('Quartzite','Hard metamorphic rock formed from sandstone, mostly quartz.')]:
    newk(n,dd,RK)
newk('Element coin','Coin or medal struck from a pure element such as copper, titanium or niobium, sold for element collectors.',W+'Element_collecting','element medal')
# display kinds (split from Specimen display)
old=kinds.pop('Specimen display'); S0=old['s']; renames['Specimen display']='Display dome'
newk('Display dome','Glass or acrylic dome on a base that covers a single specimen.',S0,'bell jar · cloche',tt=[["Material",["Glass","Acrylic"]],["Base",["Wood","Plastic"]]])
newk('Specimen stand','Small stand, riser or frame that props a specimen for viewing.',S0,'riser · floating frame',tt=[["Style",["Acrylic riser","Floating frame","Wire stand"]]])
newk('Museum putty','Reusable tacky putty that holds a specimen in place on a shelf or base.',S0,'')
newk('Gem jar','Small lidded glass or plastic jar for a loose gem or crystal.',S0,'')
newk('Perky box','Small clear hinged plastic box with a foam base for a micromount or small crystal, also sold as thumbnail boxes.',
     'https://www.minerals.net/glossary/perky-box','thumbnail box · micromount box',tt=[["Size",["Micromount","Thumbnail"]]])
newk('Riker mount','Shallow glass-topped box padded with cotton, used to display pinned insects, fossils, minerals and small objects.',
     'https://kk.org/cooltools/?p=25799','Riker box')
kinds['Riker mount'].pop('a'); kinds['Riker mount']['a']='Riker box'
for n in ('Display dome','Specimen stand','Museum putty','Gem jar'): pass
kinds['Gem jar']['a']='gem bottle'; kinds['Museum putty']['a']='mounting putty'

# ---------- types (tt), written by hand ----------
def T(n,*g): kinds[n].pop('t',None); kinds[n]['tt']=[[a,b] for a,b in g]
T('Quartz',("Habit",["Single point","Cluster","Double-terminated crystal","Geode"]),("Worked form",["Sphere","Tower","Tumbled stone"]))
T('Agate and chalcedony',("Piece",["Whole nodule","Cut nodule","Slab","Geode half"]),("Worked form",["Tumbled stone","Sphere"]))
T('Jasper',("Pattern",["Picture","Orbicular","Brecciated"]),("Colour",["Red"]))
T('Opal',("Grade",["Precious opal","Common opal (potch)"]),("Behaviour in water",["Hydrophane","Non-hydrophane"]))
T('Native gold',("Form",["Nugget","Crystallised","Dendritic","Wire","Leaf"]),("Association",["On matrix","In quartz","Loose"]))
T('Native silver',("Form",["Wire","Crystallised","Dendritic","Slab"]),("Association",["On matrix","Loose"]))
T('Native copper',("Form",["Crystallised","Arborescent","Massive"]),("Occurrence",["In place","Float copper"]))
T('Native bismuth',("Origin",["Natural","Lab-grown hopper crystal"]))
T('Pyrite',("Crystal form",["Cube","Pyritohedron","Octahedron"]),("Grouping",["Single crystal","Cluster","On matrix"]),("Replacement",["Concretion","Pyritised fossil"]))
T('Galena',("Crystal form",["Cube","Cubo-octahedron","Octahedron"]),("Piece",["Whole crystal","Cleavage piece"]))
T('Sphalerite',("Piece",["Tetrahedral crystal","Cleavage piece"]),("Association",["With galena"]))
T('Chalcopyrite',("Piece",["Tetrahedral crystal","Massive ore"]))
T('Stibnite',("Habit",["Blade","Needle spray"]),("Association",["On matrix"]))
T('Cinnabar',("Piece",["Twinned crystal","Massive ore"]),("Association",["On matrix"]))
T('Realgar',("Piece",["Crystal","Massive"]),("Association",["With orpiment"]))
T('Orpiment',("Piece",["Crystal","Foliated mass"]))
T('Marcasite',("Habit",["Cockscomb","Spearhead","Nodule"]))
T('Pyrrhotite',("Habit",["Tabular crystal","Rosette"]))
T('Bournonite',("Habit",["Cogwheel twin","Single crystal"]),("Association",["On matrix"]))
T('Proustite',("Piece",["Crystal","On matrix"]))
T('Chalcocite',("Piece",["Crystal","Massive"]))
T('Stephanite',("Habit",["Crystal","Pseudohexagonal twin"]))
T('Fluorite',("Crystal form",["Cube","Octahedron"]),("Property",["Fluorescent"]),("Worked form",["Polished sphere","Polished tower"]))
T('Halite',("Crystal form",["Cube","Hopper"]),("Colour",["Colourless","Pink","Blue"]))
T('Corundum',("Variety",["Ruby","Sapphire","Common corundum"]),("Association",["In matrix"]))
T('Spinel',("Crystal form",["Octahedron","Flat triangular twin"]),("Association",["In marble"]))
T('Hematite',("Habit",["Botryoidal","Specular","Crystal"]),("Worked form",["Tumbled stone"]))
T('Magnetite',("Habit",["Octahedron","Massive"]))
T('Rutile',("Habit",["Needle","Crystal","Twin"]),("Association",["Rutilated piece"]))
T('Cassiterite',("Habit",["Crystal","Twin"]))
T('Cuprite',("Habit",["Octahedron","Acicular"]),("Association",["On copper"]))
T('Goethite',("Habit",["Botryoidal","Crystal"]),("Replacement",["Pseudomorph"]))
T('Uraninite',("Handling",["Radioactive"]))
T('Calcite',("Crystal form",["Scalenohedron","Rhombohedron","Twin"]),("Habit",["Fibrous (lublinite)"]),("Property",["Fluorescent"]))
T('Rhodochrosite',("Habit",["Rhomb","Banded stalactite"]),("Worked form",["Polished slice"]))
T('Malachite',("Habit",["Botryoidal","Fibrous","Stalactitic"]),("Replacement",["Pseudomorph after azurite"]),("Worked form",["Polished piece"]))
T('Azurite',("Habit",["Rosette","Nodule","Stalactite"]),("Association",["Azurite-malachite"]))
T('Aragonite',("Habit",["Twin","Cave formation"]))
T('Smithsonite',("Habit",["Botryoidal","Crystalline"]),("Colour",["Blue","Pink","Yellow","Green","White"]))
T('Cerussite',("Habit",["Twin","Reticulated","Acicular"]))
T('Dolomite',("Habit",["Saddle","Rhomb","Massive"]))
T('Siderite',("Habit",["Rhomb","Spherulitic","Massive"]))
T('Magnesite',("Texture",["Crystalline","Cryptocrystalline"]),("Treatment",["Dyed"]))
T('Barite',("Habit",["Bladed","Tabular","Rosette"]),("Colour",["Blue"]))
T('Gypsum',("Habit",["Crystal","Fibrous","Rosette","Massive"]))
T('Scheelite',("Property",["Fluorescent"]),("Origin",["Natural","Synthetic"]))
T('Turquoise',("Treatment",["Natural untreated","Stabilised","Waxed or oiled","Zachery-treated","Dyed"]),("Make-up",["Natural","Reconstituted block"]))
T('Apatite',("Form",["Gem-colour crystal","Cat's-eye cabochon","Crystal on matrix"]))
T('Vivianite',("Habit",["Blades","Earthy"]))
T('Torbernite',("Handling",["Radioactive: keep in an airtight jar"]))
T('Descloizite',("Habit",["Crust","Prismatic crystal"]))
T('Adamite',("Property",["Fluorescent"]),("Composition",["Cuprian","Manganoan"]))
T('Beryl',("Variety",["Emerald","Aquamarine","Morganite","Heliodor","Goshenite","Red beryl"]),("Habit",["Trapiche"]))
T('Topaz',("Variety",["Imperial","Colourless"]),("Treatment",["Treated blue","Mystic coated"]))
T('Elbaite',("Colour variety",["Rubellite","Indicolite","Verdelite","Achroite"]),("Colour pattern",["Watermelon","Bicolour"]),("Trade type",["Paraíba-type"]))
T('Labradorite',("Flash colour",["Blue","Gold","Multi-colour"]),("Worked form",["Polished slab","Tumbled"]))
T('Lapis lazuli and lazurite',("Form",["Lapis lazuli rock","Lazurite crystal"]))
T('Stilbite',("Species",["Stilbite-Ca","Stilbite-Na"]))
T('Jadeite',("Treatment",["Natural untreated (A)","Bleached and polymer-impregnated (B)"]))
kinds['Almandine'].pop('t',None)
T('Natural diamond',("Modern cut",["Round brilliant","Princess","Cushion","Oval","Pear","Marquise","Emerald cut","Asscher","Radiant","Heart"]),("Antique cut",["Rose cut","Old European cut"]),("Colour class",["Colourless to light","Fancy colour"]))
kinds['Lab-grown diamond']['tt']=[["Growth method",["HPHT","CVD"]],["Treatment",["As grown","Treated pink or green"]]]
kinds['Lab-created coloured gemstone']['tt']=[["Growth method",["Flame-fusion","Flux-grown","Hydrothermal"]],["Species",["Corundum","Emerald"]]]
T('Ruby',("Treatment",["Untreated","Heated","Lead-glass filled"]),("Optical effect",["Star"]))
T('Sapphire',("Treatment",["Untreated","Heated","Diffusion-treated"]),("Optical effect",["Star","Colour-change"]),("Colour",["Fancy colour","Parti-colour"]))
T('Emerald',("Treatment",["Oiled","Resin-filled","Untreated"]))
T('Tanzanite',("Treatment",["Heated","Unheated"]))
T('Cut opal',("Construction",["Solid","Doublet","Triplet"]))
T('Jade',("Treatment grade",["Type A (untreated)","Type B (bleached and resin-impregnated)","Type C (dyed)","Type B+C","Type D (composite)"]))
T('Pearl',("Water",["Saltwater","Freshwater"]),("Origin",["Natural","Cultured"]),("Shape",["Round","Baroque","Keshi"]))
T('Ammolite',("Construction",["Solid","Doublet","Triplet"]))
T('Amber',("Finish",["Raw","Polished"]),("Content",["Clear","With inclusion"]),("Treatment",["Untreated","Oil-clarified"]),("Make-up",["Natural","Pressed"]))
kinds['Trace fossil']['tt']=[["Trace type",["Footprint","Burrow","Coprolite","Gastrolith"]]]
T('Iron meteorite',("Structure",["Octahedrite","Hexahedrite","Ataxite"]),("Specimen type",["Slice","Etched slice","Endcut","Individual"]))
T('Ordinary chondrite',("Group",["H chondrite","L chondrite","LL chondrite"]))
T('Carbonaceous chondrite',("Group",["CI","CM","CV","CO","CK","CR"]))
T('Enstatite chondrite',("Group",["EH","EL"]))
T('Martian meteorite',("Class",["Shergottite","Nakhlite","Chassignite","Orthopyroxenite"]))
T('Asteroidal achondrite',("Class",["Aubrite","Ureilite","Angrite","Brachinite"]))
T('Tektite',("Form",["Splash form","Button"]),("Structure",["Muong Nong layered"]))
T('Impactite and shatter cone',("Material",["Suevite","Impact melt rock","Shocked quartz"]))
T('Granite',("Piece",["Polished slab","Hand specimen"]))
T('Basalt',("Texture",["Columnar","Vesicular"]))
T('Obsidian',("Colour",["Black"]),("Piece",["Raw nodule","Arrowhead blank"]))
T('Rhyolite',("Texture",["Spherulitic","Tuff"]))
T('Limestone',("Variety",["Fossiliferous","Oolitic","Chalk","Travertine"]))
T('Slate',("Use",["Writing slate","Roofing slate"]))
T('Fulgurite',("Parent material",["Sand","Rock","Soil"]))
T('Geode and thunder egg',("Interior",["Amethyst","Agate"]),("Piece",["Whole","Cut half"]))
T('Rock and mineral teaching set',("Contents",["Rock set","Mineral set","Fossil set"]))
T('Viewing stone',("Shape",["Landscape stone","Object stone"]))
kinds['Cowrie'].pop('t',None)
T('Conch and stromb shell',("Species group",["Queen conch","Spider conch"]))
T('Abalone shell',("Species",["Red abalone","Green abalone","Black abalone"]))
T('Coral skeleton',("Group",["Sea fan","Gorgonian"]))
T('Taxidermy mammal mount',("Mount style",["Full mount","Shoulder mount","Head mount","Skull mount","Freeze-dried mount","Study skin"]))
T('Taxidermy bird mount',("Mount style",["Dome mount","Flying mount"]),("Preparation",["Study skin"]))
T('Animal skull',("Animal group",["Mammal","Bird","Reptile","Fish"]))
T('Pinned butterfly or moth',("Presentation",["Framed","Papered"]))

# ---------- structure ----------
def S(n,t,ax,names):
    ks=[kinds[x] for x in names]
    s={'n':n,'t':t}
    if len(ks)>3: s['ax']=ax
    elif ax: s['ax']=ax
    s['k']=ks; return s
placed=set()
def D(n,mode,note,t,ax,b,shelves):
    for s in shelves:
        for k in s['k']: assert k['n'] not in placed,k['n']; placed.add(k['n'])
    return {'n':n,'mode':mode,'note':note,'b':b,'t':t,'ax':ax,'s':shelves}
bm=oldb[0]
depts=[]
depts.append(D('Minerals: non-silicates','variety',
 'Chemical class (Nickel–Strunz) → species → variety or locality; about 190 popular collector species in the tree, all other species in a Mindat-linked register.',
 'Single mineral species that are not silicates, as crystals, clusters or massive pieces; a silicate → Minerals: silicates; a cut stone → Gemstones & pearls.',
 'Which chemical class is the mineral: native element, sulfide, halide, oxide, carbonate or borate, sulfate, phosphate or arsenate? (Quartz and opal sit with the oxides, as dealers list them.)',bm,[
 S('Native elements','Minerals that occur as an uncombined element, such as gold, copper or sulfur; a nugget sold as bullion → Precious metals.',
   'kinds by element: metals by value, then the semi-metal bismuth, then the non-metal sulfur',
   ['Native gold','Native silver','Native copper','Native platinum','Native bismuth','Sulfur']),
 S('Sulfides & sulfosalts','Metal–sulfur minerals that are often the ores, such as pyrite, galena and cinnabar, plus silver and copper sulfosalts such as proustite.',
   'kinds by main metal: iron, lead and zinc, copper, molybdenum and nickel, then arsenic, antimony and mercury, then sulfosalts',
   ['Pyrite','Marcasite','Pyrrhotite','Galena','Sphalerite','Chalcopyrite','Bornite','Chalcocite','Covellite','Molybdenite','Millerite','Arsenopyrite','Stibnite','Cinnabar','Realgar','Orpiment','Tetrahedrite','Bournonite','Proustite','Stephanite']),
 S('Halides','Salts of chlorine, fluorine and related elements, such as fluorite, halite and atacamite.',
   'kinds from the common fluoride and chloride salts to rarer copper and lead halides',
   ['Fluorite','Halite','Cryolite','Atacamite','Boleite','Creedite']),
 S('Oxides, hydroxides & silica','Metal oxides and hydroxides plus silicon dioxide: quartz and its chalcedony and opal forms, corundum, hematite, rutile and similar.',
   'kinds from silica to oxides by main metal: aluminium, iron, titanium, tin, copper, zinc, manganese, chromium, uranium, then hydroxides',
   ['Quartz','Agate and chalcedony','Jasper','Opal','Corundum','Spinel','Chrysoberyl','Hematite','Magnetite','Goethite','Ilmenite','Rutile','Anatase','Cassiterite','Cuprite','Zincite','Bixbyite','Pyrolusite','Chromite','Uraninite','Brucite']),
 S('Carbonates & borates','Minerals built on the carbonate or borate group, such as calcite, malachite, azurite, ulexite and borax.',
   'kinds by group: calcite group, aragonite group, copper and zinc carbonates, then borates',
   ['Calcite','Dolomite','Magnesite','Siderite','Rhodochrosite','Smithsonite','Aragonite','Witherite','Strontianite','Cerussite','Malachite','Azurite','Aurichalcite','Hydrozincite','Ulexite','Borax','Colemanite','Painite','Jeremejevite']),
 S('Sulfates, chromates & tungstates','Minerals built on the sulfate, chromate, molybdate or tungstate group, such as barite, gypsum, crocoite, wulfenite and scheelite.',
   'kinds by anion: sulfates (barium and strontium, lead, calcium, copper, others), then chromates and molybdates, then tungstates',
   ['Barite','Celestine','Anglesite','Gypsum','Anhydrite','Brochantite','Linarite','Cyanotrichite','Chalcanthite','Jarosite','Ettringite','Hanksite','Crocoite','Wulfenite','Scheelite','Ferberite','Hübnerite']),
 S('Phosphates','Minerals built on the phosphate group, such as turquoise, apatite, variscite and vivianite.',
   'kinds from the apatite group through aluminium and iron phosphates to copper and uranium phosphates',
   ['Apatite','Turquoise','Variscite','Strengite','Phosphosiderite','Vivianite','Ludlamite','Lazulite','Wavellite','Brazilianite','Torbernite','Libethenite','Pseudomalachite']),
 S('Arsenates & vanadates','Minerals built on the arsenate or vanadate group, such as vanadinite, mimetite, adamite and erythrite.',
   'kinds by main metal: lead, zinc, copper, cobalt and nickel, then iron',
   ['Pyromorphite','Mimetite','Vanadinite','Descloizite','Adamite','Legrandite','Olivenite','Clinoclase','Conichalcite','Erythrite','Roselite','Annabergite','Scorodite']),
]))
depts.append(D('Minerals: silicates','variety',
 'Silicon–oxygen structure → species → variety or locality; the largest class of collector minerals.',
 'Single silicate mineral species as crystals, clusters or massive pieces, including zeolites and feldspars; a non-silicate → Minerals: non-silicates; a cut stone → Gemstones & pearls.',
 'How are the silicon–oxygen units linked: single units, pairs, rings, chains, sheets or frameworks?',bm,[
 S('Single-unit silicates','Silicates whose silicon–oxygen units stand alone, such as garnets, zircon, olivine, topaz and kyanite.',
   'kinds by group: garnets, zircon and olivine, aluminium silicates and topaz, then rarer species',
   ['Pyrope','Almandine','Spessartine','Grossular','Andradite','Uvarovite','Zircon','Olivine (forsterite)','Kyanite','Andalusite','Staurolite','Topaz','Titanite','Phenakite','Willemite','Euclase','Datolite','Grandidierite','Afwillite']),
 S('Paired-unit silicates','Silicates built from pairs of silicon–oxygen units, such as epidote, zoisite, vesuvianite and hemimorphite.',
   'kinds by group: epidote group, vesuvianite, zinc and iron silicates, then axinite',
   ['Epidote','Zoisite','Vesuvianite','Hemimorphite','Ilvaite','Axinite']),
 S('Ring silicates','Silicates built from rings of silicon–oxygen units, such as beryl, tourmaline, dioptase and benitoite.',
   'kinds by group: beryl and cordierite, tourmalines, then other ring silicates',
   ['Beryl','Cordierite','Elbaite','Schorl','Dravite','Uvite','Fluor-liddicoatite','Benitoite','Dioptase','Eudialyte','Sugilite']),
 S('Chain silicates','Silicates built from chains of silicon–oxygen units, such as spodumene, jadeite, rhodonite and tremolite.',
   'kinds by chain type: pyroxenes, related pyroxenoids, amphiboles, then other chain silicates',
   ['Spodumene','Diopside','Aegirine','Jadeite','Rhodonite','Serandite','Pectolite','Babingtonite','Actinolite','Tremolite','Inesite','Astrophyllite','Charoite']),
 S('Sheet silicates','Silicates built from layers of silicon–oxygen units, such as micas, chlorite, talc, serpentine and apophyllite.',
   'kinds by group: micas, chlorite, talc and serpentine, then apophyllite-type and other sheet minerals',
   ['Muscovite','Lepidolite','Biotite','Phlogopite','Clinochlore','Talc','Serpentine','Apophyllite','Okenite','Cavansite','Prehnite','Petalite','Neptunite','Chrysocolla']),
 S('Framework silicates & zeolites','Silicates built as a three-dimensional framework: feldspars, feldspathoids such as sodalite, and water-bearing zeolites.',
   'kinds by group: feldspars, feldspathoids, danburite, then zeolites',
   ['Orthoclase','Microcline','Albite','Labradorite','Sodalite','Haüyne','Lapis lazuli and lazurite','Danburite','Natrolite','Mesolite','Scolecite','Thomsonite','Stilbite','Heulandite','Chabazite','Analcime','Laumontite','Harmotome']),
]))
depts.append(D('Gemstones & pearls','variety',oldb and d['depts'][1]['note'],
 'Cut, polished or drilled stones and pearls sold as gems; rough crystals and specimens → the Minerals departments; amber → Fossils & amber.',
 'Is it diamond or a stand-in for it, one of the classic coloured gems, another mineral gem, or an organic gem grown by a living thing?',oldb[1],[
 S('Diamonds, lab-grown & simulants','Diamond in all its forms, lab-grown stones and look-alikes such as moissanite and cubic zirconia.',
   'kinds from natural diamond to lab-grown diamond, other lab-made gems, then simulants',
   ['Natural diamond','Lab-grown diamond','Lab-created coloured gemstone','Moissanite and diamond simulants']),
 S('Ruby, sapphire, emerald & beryl','The classic coloured gems of corundum and beryl, cut and sold with treatment disclosed.',
   'kinds by species: corundum (ruby, sapphire), then beryl (emerald, aquamarine and others)',
   ['Ruby','Sapphire','Emerald','Aquamarine and other beryl']),
 S('Other coloured gemstones','Cut stones of the other well-known gem species, such as spinel, tourmaline, garnet, opal and jade.',
   'kinds by trade standing: rarer collector gems first (spinel, alexandrite, tanzanite), then tourmaline, garnet, topaz, quartz, opal, peridot, kunzite, zircon and jade',
   ['Cut spinel','Alexandrite and chrysoberyl','Tanzanite','Cut tourmaline','Cut garnet','Cut topaz','Cut amethyst, citrine and quartz gems','Cut opal','Peridot','Cut kunzite','Cut zircon','Jade']),
 S('Pearls & organic gems','Gems made by living things: pearls, precious coral and jet; amber → Fossils & amber.',None,['Pearl','Precious coral','Jet']),
]))
depts.append(D('Fossils & amber','variety',d['depts'][2]['note'],
 'Remains and traces of ancient life preserved in stone or resin, sold as specimens; a mineral that replaces a fossil keeps the fossil name; a modern shell → Shells & coral.',
 'Which group of life left it: cephalopods, arthropods, other sea invertebrates, vertebrates, plants and traces, or tree resin?',oldb[2],[
 S('Ammonites & other cephalopods','Fossil shells of ammonites, nautiloids and belemnites, and gem ammolite made from ammonite shell.',
   'kinds from coiled ammonites to their gem form, then straight and internal shells',['Ammonite','Ammolite','Fossil nautiloid','Belemnite']),
 S('Arthropods & insects','Fossil trilobites, crustaceans, eurypterids, horseshoe crabs and insects.',
   'kinds from the most collected (trilobites) to other jointed-legged animals',['Trilobite','Fossil crustacean','Eurypterid','Fossil horseshoe crab','Fossil insect']),
 S('Marine invertebrate fossils','Fossil echinoderms, shelled animals, corals, graptolites and sponges other than cephalopods and arthropods.',
   'kinds by phylum: echinoderms and shelled animals first, then colonial animals and sponges',
   ['Crinoid','Echinoderm fossil','Fossil brachiopod','Fossil bivalve','Fossil gastropod','Fossil coral','Bryozoan fossil','Graptolite','Fossil sponge']),
 S('Vertebrate fossils','Fossil teeth, bones, eggs and skeletons of fish, dinosaurs, marine reptiles and mammals.',
   'kinds by animal group, from fish and sharks to dinosaurs, marine reptiles, other reptiles and mammals',
   ['Fossil shark tooth','Fossil fish','Dinosaur tooth','Dinosaur claw & bone','Dinosaur egg & eggshell','Marine reptile fossil','Fossil reptile or amphibian','Fossil mammal']),
 S('Plant, wood & trace fossils','Fossil plants, petrified wood, stromatolites and traces such as footprints and coprolites.',
   'kinds from plant remains to microbial mats and animal traces',['Petrified wood','Plant fossil','Stromatolite','Trace fossil']),
 S('Amber & copal','Fossil tree resin (amber) and younger resin (copal), raw or polished, with or without inclusions.',None,['Amber','Copal']),
]))
depts.append(D('Meteorites & impact glass','variety',d['depts'][3]['note'],
 'Rock and metal that fell from space, and the glass and rock made when something hit the Earth; a cut meteorite gem → Gemstones & pearls.',
 'What is it made of and how did it form: stone with chondrules, stone without them, metal, or glass made in an impact?',oldb[3],[
 S('Chondrites','Stony meteorites containing chondrules, the oldest solar-system material: ordinary, carbonaceous and enstatite.',None,['Ordinary chondrite','Carbonaceous chondrite','Enstatite chondrite']),
 S('Achondrites','Stony meteorites without chondrules, from melted asteroids, the Moon or Mars.',
   'kinds by parent body: Vesta, the Moon, Mars, then other asteroids',['HED meteorite','Lunar meteorite','Martian meteorite','Asteroidal achondrite']),
 S('Irons & stony-irons','Meteorites of nickel-iron metal, alone or mixed with stone, such as Gibeon, pallasites and mesosiderites.',None,['Iron meteorite','Pallasite','Mesosiderite']),
 S('Tektites & impact glass','Glass and rock formed by meteorite impacts on Earth, such as moldavite, Libyan Desert glass and suevite.',None,['Tektite','Impact glass','Impactite and shatter cone']),
]))
depts.append(D('Rocks & teaching sets','variety','Rock family (igneous, sedimentary, metamorphic) → named rock → locality; curiosities and teaching sets last.',
 'Rocks made of several minerals, collected as hand specimens, slabs or sets; a single mineral species → Minerals; a rock from space → Meteorites & impact glass.',
 'Which rock family is it: igneous, sedimentary, metamorphic, or a rock curiosity or teaching set?',[],[
 S('Igneous rocks','Rocks that cooled from melt, such as granite, basalt and obsidian.',
   'kinds from coarse deep-cooled rocks to fine volcanic rocks, then glass and fragmental volcanic rocks',
   ['Granite','Gabbro','Basalt','Andesite','Rhyolite','Porphyry','Obsidian','Pumice','Tuff']),
 S('Sedimentary rocks','Rocks laid down from grains, mud or dissolved minerals, such as sandstone and limestone.',
   'kinds from coarse grains to fine mud, then chemical rocks',['Conglomerate','Sandstone','Shale','Limestone','Chert and flint']),
 S('Metamorphic rocks','Rocks changed by heat and pressure, such as slate, schist and marble.',
   'kinds by rising metamorphic grade, then rocks made from sandstone and limestone',['Slate','Schist','Gneiss','Quartzite','Marble']),
 S('Rock curiosities & teaching sets','Natural oddities and educational sets: lightning glass, geodes, nodules, viewing stones and boxed collections.',
   'kinds from natural oddities to shaped stones and then sets',['Fulgurite','Geode and thunder egg','Septarian nodule','Viewing stone','Rock and mineral teaching set']),
]))
depts.append(D('Shells & coral','variety',d['depts'][5]['note'],
 'Shells and hard skeletons of sea and land animals kept as specimens; a fossil shell → Fossils & amber; a shell made into jewellery or décor belongs with those objects.',
 'Which animal made it: a snail, a bivalve or other mollusc, a cephalopod, or a coral, echinoderm or lamp shell?',oldb[5],[
 S('Snail shells','Shells of sea snails and land snails: cowries, cones, volutes, conchs, abalone and land snails.',
   'kinds by family, from smooth glossy shells (cowries, cones, olives, mitres) to ribbed and spined shells, then wentletraps, abalone and land snails',
   ['Cowrie','Cone shell','Olive shell','Mitre shell','Volute shell','Harp shell','Murex shell','Conch and stromb shell','Helmet and bonnet shell','Triton shell','Wentletrap shell','Abalone shell','Land snail shell']),
 S('Bivalves, tusk shells & chitons','Shells of two-valved molluscs, tooth-shaped tusk shells and plated chitons.',
   'kinds by mollusc class: bivalves, then tusk shells, then chitons',['Scallop shell','Thorny oyster','Giant clam shell','Cockle shell','Tusk shell','Chiton shell']),
 S('Cephalopod shells','Shells and bones of nautilus, argonaut and cuttlefish relatives.',None,['Chambered nautilus shell','Paper nautilus','Cuttlebone']),
 S('Corals, urchins, sea stars & lamp shells','Hard skeletons of corals and echinoderms, and brachiopod shells.',
   'kinds by animal group: corals, then sea urchins, sand dollars and starfish, then lamp shells',['Coral skeleton','Sea urchin test','Sand dollar','Dried starfish','Brachiopod shell']),
]))
depts.append(D('Taxidermy, bones & preserved specimens','variety',d['depts'][6]['note'],
 'Animals and plants kept after death as mounts, bones, horns, eggs, pinned insects or pressed plants; fossil bone → Fossils & amber; a shell → Shells & coral.',
 'How is the specimen kept: mounted whole, as bone, as horn, tooth, feather or egg, or as a small pinned, pressed or fluid specimen?',oldb[6],[
 S('Taxidermy mounts','Skinned and mounted animals shown whole or in part, such as game heads, cased birds and fish mounts.',
   'kinds by animal group: mammals, birds, fish, reptiles',['Taxidermy mammal mount','Taxidermy bird mount','Taxidermy fish mount','Taxidermy reptile mount']),
 S('Skulls & skeletons','Cleaned bone: single skulls, articulated skeletons and replica casts.',None,['Animal skull','Articulated skeleton','Replica skull and fossil cast']),
 S('Horns, teeth, feathers & eggs','Hard and keratin parts kept on their own: antlers, tusks, teeth, jaws, feathers and eggs.',
   'kinds from horn and tusk to teeth and jaws, then feathers and eggs',['Antler or horn','Tusk specimen','Claw or tooth specimen','Shark or fish jaw','Feather specimen','Egg or nest specimen']),
 S('Pinned, pressed & wet specimens','Small specimens kept pinned, pressed, in resin or in fluid: insects, herbarium sheets and wet preparations.',
   'kinds by preservation method: pinned, pressed, set in resin, then in fluid',['Pinned butterfly or moth','Pinned beetle and other insect','Herbarium sheet','Insect in resin','Fluid-preserved specimen']),
]))
depts.append(D('Element samples','variety','Form of sample → element; purity and mass are details.',
 'Pure samples of chemical elements kept for the periodic table; a mineral that contains the element → the Minerals departments.',
 'Is it a single sample of one element, or a set that covers the periodic table?',[],[
 S('Single element samples','One element held as a cube, sealed ampoule, resin block, crystal or coin.',
   'kinds by how the sample is held: solid cube, sealed glass, set in resin, grown crystal, struck coin',
   ['Element cube','Element ampoule','Encased element sample','Element crystal','Element coin']),
 S('Element sets','Many elements arranged together, usually as a periodic table.',None,['Periodic table element collection']),
]))
depts.append(D('Display domes & stands','tier','Cases, boxes and mounts for showing specimens.',
 'Covers, boxes and mounts made to hold and show one specimen; a cabinet or shelf for many → Furniture & Storage.',
 'Does it cover the specimen, hold it in a box or jar, or prop it up?',[],[
 S('Domes, boxes & jars','Containers that cover or enclose a specimen: domes, Riker mounts, perky boxes and gem jars.',
   'kinds from large covers to small boxes and jars',['Display dome','Riker mount','Perky box','Gem jar']),
 S('Stands & mounts','Supports that hold a specimen up or in place: stands, risers, frames and putty.',None,['Specimen stand','Museum putty']),
]))
depts[2]['note']=d['depts'][1]['note']
d['depts']=depts
d['ax']='Is the object a mineral, a cut gem, a fossil, a rock from space, an ordinary rock, a shell, a preserved animal or plant, a pure element sample, or something that shows specimens?'
d['key']=[
 '1. Is it a pure sample of a chemical element (cube, ampoule, coin, crystal, periodic table set)? → Element samples',
 '2. Is it a dome, box, jar, stand or mount made to show a specimen? → Display domes & stands',
 '3. Did it fall from space, or form when something hit the Earth (meteorite, tektite, impact glass)? → Meteorites & impact glass',
 '4. Is it the remains or trace of ancient life, or fossil resin such as amber? → Fossils & amber',
 '5. Is it a shell, or the hard skeleton of a coral, sea urchin or starfish? → Shells & coral',
 '6. Is it an animal or plant kept after death (mount, skull, horn, egg, pinned insect, pressed plant)? → Taxidermy, bones & preserved specimens',
 '7. Is it a cut, polished or drilled stone or pearl sold as a gem? → Gemstones & pearls',
 '8. Is it a rock of several minerals, a rock curiosity or a teaching set? → Rocks & teaching sets',
 '9. Is it a single silicate mineral species (garnet, tourmaline, feldspar, mica, zeolite)? → Minerals: silicates',
 '10. Is it any other single mineral species (metal, sulfide, oxide including quartz, carbonate, sulfate, phosphate)? → Minerals: non-silicates',
 '<i>Precedence: a cut stone leaves the mineral shelves for Gemstones; amber is a fossil even when polished as a gem; petrified wood stays a fossil; quartz and opal are oxides here, as dealers list them.</i>']
# lead: keep (fits the rules); note phrasing fixed
d['lead']=d['lead'].replace('organised by scientific classification','organised by what the specimen is (mineral class, gem species, fossil group, meteorite class, rock family, shell family)')
leftover=set(kinds)-placed
assert not leftover, leftover

# ---------- cross-links ----------
SEE={
'Quartz':[('F6','Cut amethyst, citrine and quartz gems','cut stones')],
'Opal':[('F6','Cut opal','cut stones')],
'Corundum':[('F6','Ruby','cut stones'),('F6','Sapphire','cut stones')],
'Beryl':[('F6','Emerald','cut stones'),('F6','Aquamarine and other beryl','cut stones')],
'Topaz':[('F6','Cut topaz','cut stones')],
'Elbaite':[('F6','Cut tourmaline','cut stones')],
'Pyrope':[('F6','Cut garnet','cut stones')],'Almandine':[('F6','Cut garnet','cut stones')],'Grossular':[('F6','Cut garnet','cut stones')],
'Spinel':[('F6','Cut spinel','cut stones')],'Chrysoberyl':[('F6','Alexandrite and chrysoberyl','cut stones')],
'Zoisite':[('F6','Tanzanite','cut stones')],'Olivine (forsterite)':[('F6','Peridot','cut stones')],
'Jadeite':[('F6','Jade','cut stones')],'Spodumene':[('F6','Cut kunzite','cut stones')],'Zircon':[('F6','Cut zircon','cut stones')],
'Cut amethyst, citrine and quartz gems':[('F6','Quartz','crystals and clusters')],
'Cut opal':[('F6','Opal','rough and specimen opal')],'Ruby':[('F6','Corundum','crystals')],'Sapphire':[('F6','Corundum','crystals')],
'Emerald':[('F6','Beryl','crystals')],'Cut topaz':[('F6','Topaz','crystals')],'Cut tourmaline':[('F6','Elbaite','crystals')],
'Cut garnet':[('F6','Almandine','crystals')],'Peridot':[('F6','Olivine (forsterite)','crystals')],'Jade':[('F6','Jadeite','mineral')],
'Cut kunzite':[('F6','Spodumene','crystals')],'Cut zircon':[('F6','Zircon','crystals')],'Cut spinel':[('F6','Spinel','crystals')],
'Tanzanite':[('F6','Zoisite','crystals')],'Alexandrite and chrysoberyl':[('F6','Chrysoberyl','crystals')],
'Amber':[('F6','Insect in resin','insects set in resin'),('F6','Copal','younger resin')],
'Insect in resin':[('F6','Amber','fossil resin'),('F6','Fossil insect','fossil insects')],
'Fossil insect':[('F6','Insect in resin','modern insects in resin')],
'Ammonite':[('F6','Ammolite','gem shell')],'Ammolite':[('F6','Ammonite','whole fossil shell')],
'Fossil brachiopod':[('F6','Brachiopod shell','modern shell')],'Brachiopod shell':[('F6','Fossil brachiopod','fossil shell')],
'Fossil nautiloid':[('F6','Chambered nautilus shell','living relative')],'Chambered nautilus shell':[('F6','Fossil nautiloid','fossil relative')],
'Fossil coral':[('F6','Coral skeleton','modern coral')],'Coral skeleton':[('F6','Fossil coral','fossil coral')],
'Echinoderm fossil':[('F6','Sea urchin test','modern urchin')],'Sea urchin test':[('F6','Echinoderm fossil','fossil urchin')],
'Fossil shark tooth':[('F6','Claw or tooth specimen','modern teeth')],'Dinosaur egg & eggshell':[('F6','Egg or nest specimen','modern eggs')],
'Egg or nest specimen':[('F6','Dinosaur egg & eggshell','fossil eggs')],
'Geode and thunder egg':[('F6','Agate and chalcedony','agate nodules')],
'Agate and chalcedony':[('F6','Geode and thunder egg','geodes')],
'Tektite':[('F6','Impact glass','other impact glass')],'Impact glass':[('F6','Tektite','tektites')],
'Pallasite':[('F6','Peridot','pallasite peridot gems')],
'Native bismuth':[('F6','Element crystal','bismuth crystals as element samples')],
'Element crystal':[('F6','Native bismuth','natural bismuth')],
'Riker mount':[('F6','Pinned butterfly or moth','typical contents')],
'Pinned butterfly or moth':[('F6','Riker mount','display box')],
'Perky box':[('F6','Display dome','larger cover')],'Display dome':[('F6','Perky box','small box')],
'Marble':[('E1','Marble','toy glass marble, not the rock')],
'Jet':[('G1','Jet','the aircraft, not the gem')],
'Obsidian':[('F6','Tektite','natural glass of impact origin')],
'Serpentine':[('F6','Marble','Connemara marble is serpentine')],
}
names=set(kinds)
ext={}
for c in ('E1','G1'):
    dd=json.load(open(R+f'reader/{c}.json'))
    nm=set()
    def w(o):
        if isinstance(o,dict):
            if 'n' in o and isinstance(o['n'],str): nm.add(o['n'])
            for v in o.values(): w(v)
        elif isinstance(o,list):
            for v in o: w(v)
    w(dd); ext[c]=nm
nsee=0
for kn,lst in SEE.items():
    ok=[]
    for c,t,why in lst:
        assert (t in names) if c=='F6' else (t in ext[c]), (kn,c,t)
        ok.append([c,t,why])
    kinds[kn]['see']=ok; nsee+=len(ok)

# ---------- write ----------
after=dict(depts=len(d['depts']),shelves=sum(len(x['s']) for x in d['depts']),kinds=len(kinds),
           arch=sum(len(k.get('x',[])) for k in kinds.values()))
tmp=R+'out/F6.json.tmp'
json.dump(d,open(tmp,'w'),ensure_ascii=False,indent=1); os.replace(tmp,R+'out/F6.json')
ren=R+'out/F6_renames.json'
json.dump(renames,open(ren+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(ren+'.tmp',ren)
print('before',before,'after',after,'see',nsee,'demoted',len(demoted))
json.dump(demoted,open(R+'work/STR_F6/demoted.json','w'),indent=1)
