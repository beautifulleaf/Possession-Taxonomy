import json,os
W='https://en.wikipedia.org/wiki/'
def x(n,d,s,y='',v=None,dt='',a='',mk=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":(s if s.startswith('http') else W+s),"v":v or [],"dt":dt}
def v(n,d,y='',mk=''): return {"n":n,"mk":mk,"y":y,"d":d}
def k(n,d,s,xs=None,a="",t=None,m=None):
    o={"n":n,"d":d,"s":s}
    if a:o["a"]=a
    if t:o["t"]=t
    if xs is not None:o["x"]=xs
    if m is not None:o["m"]=m
    return o
def out(job,kinds,brands,trads,notes):
    p=f'work/F6/shelves/{job}'
    json.dump({"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes},open(p+'.tmp','w'),ensure_ascii=False,indent=1)
    os.rename(p+'.tmp',p+'.json')
def B(n,c,f,seg,kf,d,s,**kw):
    b={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s}; b.update(kw); return b

# ---------- 06_00
LEG="Legal: CITES and national wildlife laws apply to many species; pre-Convention papers needed to trade older pieces."
k1=k("Taxidermy mammal mount","Mammal skin preserved and mounted as in life (full mount, shoulder or head mount). "+"Legality varies by species; CITES and domestic wildlife law apply.","https://www.1stdibs.com/furniture/more-furniture-collectibles/collectibles-curiosities/taxidermy/montana-buffalo-shoulder-mount/id-f_36681402",[
 x("Full mount","Whole animal on a mannequin; the Akeley method of a clay model, plaster mould and fitted hide became standard.","Carl_E._Akeley","method developed 1896–1909",[v("Akeley method","clay model, armature, plaster mould, papier-mâché mannequin")],"skin mount on mannequin · glass eyes · pose · "+LEG),
 x("Shoulder mount","Head, neck and shoulders mounted for wall display, a standard trophy form.","Tocher_and_Tocher_Taxidermists","",[v("Head and shoulder mount","offered by Tocher and Tocher"),v("Head-only mount","")],"wall pedestal · mount size · "+LEG,mk="Tocher and Tocher"),
 x("Skull mount","Only the skull displayed, with or without horns or antlers; cleaned by boiling or dermestid beetles.","Skull_mounts","",[],"European mount · boiled or beetle-cleaned · plaque","European mount"),
 x("Indian tiger and leopard trophy mount","Mysore trophy taxidermy with open-mouth snarl, moulded heads and hand-painted German glass eyes.","Van_Ingen_&_Van_Ingen","1890s–1999",[v("Van Ingen mounts","over 43,000 tiger and leopard trophies in under 90 years","",mk="Van Ingen & Van Ingen"),v("Tocher and Tocher rug with head mount","about 2.5 months of work","")],"snarling open mouth · rug with head mount · tiger or leopard · "+LEG,mk="Van Ingen & Van Ingen"),
 x("Rowland Ward big-game mount","London-made game head and animal furniture; Ward's firm also published Records of Big Game.","Rowland_Ward","1857 shop; Ltd 1891",[v("Macarte Lion","1874 mount","1874",mk="Rowland Ward"),v("Bear dumbwaiter","animal furniture","",mk="Rowland Ward")],"head mount · horn or tusk furniture · "+LEG,mk="Rowland Ward"),
 x("Anthropomorphic tableau","Dressed animals posed in human scenes, a late-Victorian novelty; Walter Potter's Kittens' Wedding (1890) sold for £21,150 in 2003.","Walter_Potter","late 19th century",[v("The Death and Burial of Cock Robin","about 1854; top seller at £23,500 in 2003","1854",mk="Walter Potter"),v("The Kittens' Wedding","1890","1890",mk="Walter Potter"),v("The Rabbit School","48 rabbits at slates","",mk="Walter Potter")],"scene size · number of animals · provenance",mk="Walter Potter")],
 t=["freeze-dried mount","study skin"])
k1["m"]=[]
k2=k("Taxidermy bird mount","Bird skin preserved and mounted as in life. Wild-bird mounts are restricted by migratory-bird laws such as the US Migratory Bird Treaty Act.","https://www.1stdibs.com/furniture/more-furniture-collectibles/collectibles-curiosities/taxidermy/vintage-ringneck-pheasant-bird-full-body-standing-mount-taxidermy-mancave/id-f_40887252",[
 x("Victorian cased bird","Birds mounted in a glass case or diorama, a staple of 19th-century homes; the Booth Museum in Brighton holds over 300 dioramas.","Booth_Museum_of_Natural_History","1874 museum opened",[v("Booth Museum dioramas","over 300, display fixed by the donation","1891")],"glass case · habitat setting · label · Migratory Bird Treaty Act applies to wild birds"),
 x("Rowland Ward bird mount","Bird taxidermy by Rowland Ward of Piccadilly.","Rowland_Ward","",[],"case or dome · provenance label",mk="Rowland Ward"),
 x("Study skin","Flat museum-style bird skin with no artificial eyes, used for research.","Zoological_specimen","",[],"label data · dry skin"),
 x("Death and Burial of Cock Robin","Potter's tableau using 98 British bird species.","Walter_Potter","about 1854",[],"98 species",mk="Walter Potter")],
 t=["dome mount","flying mount"])
k2["m"]=[]
k3=k("Taxidermy fish mount","Mounted fish, either a skin mount or a resin or fibreglass reproduction made from photographs and measurements.","https://en.wikipedia.org/wiki/Taxidermy",[
 x("Skin mount","Fish skin fitted on a form and painted; traditional trophy method.","Taxidermy","",[],"form · paint · pose"),
 x("Reproduction mount","Resin or fibreglass replica of a trophy fish from photos and measurements; used for catch-and-release.","Taxidermy","",[],"replica from photos · size")])
k4=k("Taxidermy reptile mount","Reptile skin preserved and mounted as in life (full mount or head). Crocodilians and many reptiles are CITES-listed.","https://odditiesforsale.com/product-category/natural-specimens/",[
 x("Celluloid-finished reptile mount","Mount whose colour and translucence is reproduced with synthetic materials such as celluloid.","History_of_taxidermy","",[],"snake · crocodilian · lizard · CITES paperwork")])
k4["m"]=[]
brands=[
 B("Rowland Ward","United Kingdom","1857","Heritage manufactory","taxidermy","London taxidermy firm of Piccadilly, known for game mounts and Records of Big Game.","https://en.wikipedia.org/wiki/Rowland_Ward",eras=["James Rowland Ward, 1848–1912","Taxidermy side closed mid-1970s"],sig=["Big-game head mount","Macarte Lion"]),
 B("Van Ingen & Van Ingen","India","1890s","Heritage manufactory","tiger trophies","Mysore taxidermy firm that mounted tens of thousands of tiger and leopard trophies.","https://en.wikipedia.org/wiki/Van_Ingen_&_Van_Ingen",eras=["Eugene Van Ingen, founder","Closed 1999"]),
 B("Tocher and Tocher","India","1906","Heritage manufactory","trophy mounts","Bangalore taxidermy firm founded by William Tocher, closed in the 1960s.","https://en.wikipedia.org/wiki/Tocher_and_Tocher_Taxidermists",eras=["William Tocher, to 1938","Herbert Tocher"]),
 B("Edward Gerrard & Sons","United Kingdom","1853","Heritage manufactory","taxidermy","Camden taxidermy firm that supplied museums; closed 1965 or 1967.","https://en.wikipedia.org/wiki/Edward_Gerrard_&_Sons"),
 B("Walter Potter","United Kingdom","1854","Artisan & independent","anthropomorphic tableaux","Sussex taxidermist (1835–1918) whose dressed-animal dioramas were sold at Bonhams in 2003.","https://en.wikipedia.org/wiki/Walter_Potter",sig=["Death and Burial of Cock Robin","The Kittens' Wedding"])]
trads=[
 {"n":"Victorian taxidermy","g":"Natural history & taxidermy","r":"Britain","p":"19th century","d":"Golden age of mounted animals as home decor, from glass-case birds to anthropomorphic tableaux.","tech":"skin mounts in cases and domes","mat":"skins, glass eyes, glass cases","forms":["cased bird","anthropomorphic tableau","game head"],"ctr":["Rowland Ward, London","Edward Gerrard & Sons, Camden","Walter Potter, Bramber"],"auth":"maker's label and case provenance","s":"https://en.wikipedia.org/wiki/History_of_taxidermy"},
 {"n":"Indian trophy taxidermy","g":"Natural history & taxidermy","r":"Mysore and Bangalore, India","p":"1890s–1990s","d":"Colonial-era studios mounting tiger, leopard and other game for hunters and royalty.","tech":"moulded heads, hand-painted glass eyes","mat":"skin, German glass eyes, plaster heads","forms":["tiger full mount","rug with head","snarling head"],"ctr":["Van Ingen & Van Ingen, Mysore","Tocher and Tocher, Bangalore"],"auth":"studio records and labels; tiger trade is CITES Appendix I","s":"https://en.wikipedia.org/wiki/Van_Ingen_&_Van_Ingen"}]
out('06_00',[k1,k2,k3,k4],brands,trads,"Peter Spicer and J. Cooper & Sons not found on retrieved pages so omitted; cased fish not sourced. Legal notes are general (CITES, Migratory Bird Treaty Act) as stated in retrieved pages; antique/pre-Convention rules vary by country. Reptile kind has one archetype only.")

# ---------- 06_01
SU="https://skullsunlimited.com"
a1=k("Mammal skull","Cleaned real skull of a mammal kept as a specimen. Legality varies; protected species and CITES listings restrict trade.","https://lenaturaliste.ca/products/crane-de-coyote",[
 x("Dermestid-cleaned skull","Flesh removed by dermestid beetles, then whitened with hydrogen peroxide; the museum and professional method.","Dermestarium","",[v("Skulls Unlimited cleaning service","about 25,000 specimens a year","",mk="Skulls Unlimited")],"beetle-cleaned · whitened · degreased"),
 x("European skull mount","Skull mounted on a plaque, with or without horns; boiling is the traditional method.","Skull_mounts","",[],"boiled or beetle-cleaned · plaque")],t=["coyote","deer","bear","beaver"])
a1["m"]=[]
a2=k("Bird skull","Cleaned real skull of a bird kept as a specimen. Wild-bird parts are restricted by migratory-bird laws.","https://lenaturaliste.ca/products/crane-de-corneille",[x("Dermestid-cleaned skull","Small bird skulls cleaned by dermestid beetles.","Dermestarium","",[],"beetle-cleaned")],t=["crow"])
a3=k("Reptile skull","Cleaned real skull of a reptile (alligator, turtle, snake, lizard) kept as a specimen.","https://www.wardsci.com/us/en/product/8887786/snake-skull",t=["alligator","snake"])
a4=k("Fish skull","Cleaned real skull of a bony fish kept as a specimen. A dried jaw or tooth set is under Fish jaw or teeth set.","https://skullsunlimited.com/products/real-piranha-small-skull",t=["piranha"])
a5=k("Articulated skeleton","Real animal skeleton, cleaned and articulated on a stand or in a case.",SU,[
 x("Museum of Osteology display skeleton","Articulated skeletons shown at the Oklahoma City museum, including a humpback whale (one of twelve fully articulated in North America) and a Javan rhinoceros.","Museum_of_Osteology","opened 2010",[v("Humpback whale","fully articulated"),v("Javan rhinoceros","rarest specimen in the collection")],"stand or hung · size · provenance",mk="Skulls Unlimited")])
a6=k("Replica skull and fossil cast","Cast copy of a skull or fossil in resin, such as hominid skulls; a replica, not a real specimen.","https://www.skullsunlimited.com/products/replica-lucy-skull-bh-021",[
 x("Lucy skull cast","1:1 polyurethane resin cast of Australopithecus afarensis, supplied by Bone Clones.","https://www.skullsunlimited.com/products/replica-lucy-skull-bh-021","",[v("Dark finish","Bone Clones BH-021T")],"1:1 scale · two-part cranium and jaw · tar or antique finish",mk="Bone Clones"),
 x("Hominid skull set","Set of nine casts: Homo habilis, Peking Man, Mrs Ples, La Chapelle Neanderthal, Nariokotome boy, Zinjanthropus, Taung Child, Kenyanthropus and Lucy.","https://www.boneclones.com/product/set-of-9-fossil-hominid-skulls","",[],"1:1 scale · display stand sold separately",mk="Bone Clones")])
brands=[
 B("Skulls Unlimited","United States","1986","Specialist","skulls & skeletons","Oklahoma City supplier of real and replica skulls and skeletons, with beetle cleaning services.","https://en.wikipedia.org/wiki/Skulls_Unlimited_International",eras=["Jay Villemarette, founder"],lines=["real skulls","replica skulls","cleaning service"]),
 B("Bone Clones","United States","","Specialist","skeletal casts","Chatsworth, California maker of polyurethane casts of skulls and skeletons, including hominid fossils.","https://www.boneclones.com/product/set-of-9-fossil-hominid-skulls",sig=["Lucy skull","hominid skull set"])]
out('06_01',[a1,a2,a3,a4,a5,a6],brands,[],"Reptile and fish skulls kept with old sources and type lists only. Deer, bear, beaver, alligator, piranha archetypes not sourced on retrieved pages so given as types. Bone Clones and Skulls Unlimited replica products sourced from their own product pages; Museum of Osteology from Wikipedia. Legal notes general.")

# ---------- 06_02
b1=k("Antler or horn","Real antler or horn kept as a specimen. An antler chew for dogs is in Animal Equipment.","https://www.skullsunlimited.com/products/real-kudu-horn-single-lq-13537",[
 x("Shed antler","Antler dropped naturally by deer, elk or moose; shed hunting is regulated, and removal is an offence in Canadian national parks.","Antler","",[v("Red deer, moose, elk","species with large antlers")],"shed or cut · points · weight · "+"Canada national parks fine up to C$25,000"),
 x("Kudu horn","Spiralled horn of the greater kudu; two and a half twists by about 6 years, record 187.64 cm.","Greater_kudu","",[v("Record horn","187.64 cm")],"single or pair · length · twists"),
 x("Ram and buffalo horn","Keratin-sheathed horn of sheep or water buffalo, used for carving, instruments and buttons.","Horn_(animal_anatomy)","",[],"length · curl")],m=[["Kudu horn",""]])
b2=k("Tusk specimen","Real tusk or tusk section kept as a specimen. Ivory rules apply.","https://www.skullsunlimited.com/products/real-warthog-tusk-lq-12149",[
 x("Warthog tusk","Upper canine of the common warthog, up to about 25.5 cm; carved tusks sold to tourists in Africa.","Common_warthog","",[],"upper or lower · length · carved or plain"),
 x("Elephant, walrus and hippo ivory","Restricted ivory: African elephant ivory trade banned January 1990; walrus, hippo and narwhal ivory regulated.","Ivory_trade","1989–1990",[v("CITES Appendix I listing","African elephant, October 1989","1989")],"legal papers · pre-ban provenance · tusk length")],m=[["Warthog tusk",""]])
b3=k("Claw or tooth specimen","Real modern animal claw, talon or tooth kept as a specimen. Fossil teeth are under Fossils & amber.",SU if False else "https://skullsunlimited.com",[
 x("Scrimshawed sperm whale tooth","Engraved whale tooth from the whaling era; sale of marine-mammal ivory made after 1973 is prohibited in the US.","Scrimshaw","from late 18th century",[v("Earliest dated sperm whale scrimshaw","1817","1817")],"engraving · pre-1973 provenance · size"),
 x("Bear claw","Claw of a bear; legality and trade depend on species and country.","Marine_Mammal_Protection_Act","",[],"check species and permits") ])
# bear claw archetype would not be sourced by MMPA page: drop it
b3["x"]=[b3["x"][0]]
b4=k("Shark or fish jaw","Dried jaw or set of teeth of a fish or shark kept as a specimen. Check CITES and national rules before buying.","https://www.skullsunlimited.com/collections/unique-offerings-at-skulls-unlimited",[
 x("Great white shark jaw","Jaw of about 300 triangular teeth, teeth up to 7.5 cm; jaws are loosely attached to the skull.","Great_white_shark","",[],"tooth size · rows · legal papers")])
b5=k("Egg or nest specimen","Blown or emptied eggshell, or a dried nest, kept as a specimen. An egg for hatching is not sold here. Wild-bird egg collecting is illegal in many places.","https://www.1stdibs.com/buy/egg-taxidermy",[
 x("Ostrich egg","Largest living bird egg, about 15 cm long and 1.4 kg; decorated and silver-mounted for centuries.","Ostrich_egg","",[],"decorated · silver-mounted · size"),
 x("Elephant bird egg","Subfossil egg of Aepyornis, the largest known amniote egg at 26–40 cm.","Elephant_bird","extinct about 1000 AD",[v("Scott River egg","Western Australia, found 1930s"),v("Cervantes egg","Western Australia, found 1992","1992")],"intact or fragment · authenticity"),
 x("Oological egg collection","Historic wild-bird egg collections; UK possession lawful only if taken before 1954 or under permit.","Oology","19th–20th century",[],"antique cabinet · provenance")],m=[["Elephant bird egg",""],["Emu egg",""],["Ostrich egg",""]])
out('06_02',[b1,b2,b3,b4,b5],[],[],"Moa/emu eggs, nests, bear claw and sperm-whale tooth legality beyond what retrieved pages say are not covered; emu egg kept as a flat model from old data. Legal notes only as stated: Oology, Ivory trade, Scrimshaw and Antler pages. Great white CITES status was not stated on the fetched page, so only a generic 'check CITES' note.")

# ---------- 06_03
c1=k("Pinned butterfly or moth","Dried, pinned or spread lepidopteran specimen, framed or unframed (a frame fixed to the one specimen is part of the object). Many birdwings are CITES Appendix II.","https://bicbugs.com/product/mixed-lot-craft-grade-frames/",[
 x("Menelaus blue morpho","Iridescent blue Neotropical butterfly of about 12 cm wingspan, long prized by collectors and artists.","Morpho_menelaus","",[],"framed or papered · wingspan · grade (A1)","Morpho menelaus"),
 x("Chimaera birdwing","New Guinea montane birdwing, wingspan up to 180 mm; CITES Appendix II.","Chimaera_birdwing","CITES Appendix II",[],"male or female · framed · permits","Ornithoptera chimaera"),
 x("Richmond birdwing","Australian birdwing, the second smallest birdwing; protected and under recovery.","Richmond_birdwing_butterfly","",[],"framed · permits","Ornithoptera richmondia")],t=["framed","papered"])
c2=k("Pinned beetle and other insect","Dried pinned insect or arachnid specimen, such as a rhinoceros beetle, Goliath beetle or tarantula.","https://en.wikipedia.org/wiki/Entomological_equipment_for_mounting_and_storage",[
 x("Hercules beetle","Neotropical rhinoceros beetle, males to 173 mm with horn; kept and collected worldwide.","Hercules_beetle","",[],"male or female · length with horn","Dynastes hercules"),
 x("Royal Goliath beetle","Large West African goliath beetle, males 50–115 mm.","Goliathus_regius","",[],"male or female · pronotum pattern","Goliathus regius")])
c3=k("Feather specimen","Feather kept and labelled as a specimen. Craft feathers are in Craft & Art Supplies. Possession of most native bird feathers is restricted in the US.","https://www.skullsunlimited.com/collections/unique-offerings-at-skulls-unlimited",[
 x("Contour and flight feather","Vaned body and wing feathers; type, species and legality decide collectability.","Feather","",[v("Migratory Bird Treaty Act 1918","criminalised possession of feathers of most native birds","1918"),v("Eagle feather law","limited to enrolled members of federally recognised tribes")],"flight, contour or down · species · legal status")])
c4=k("Herbarium sheet","Pressed, dried plant mounted on a sheet as a specimen. Dried flowers for decor are in Decor.","https://www.1stdibs.com/buy/herbarium-set",[
 x("Hortus siccus","Bound album of pressed plants in the manner of Luca Ghini (1490–1556); the oldest surviving herbarium is attributed to Gherardo Cibo, about 1532.","Herbarium","about 1532",[v("Petrus Cadé's hortus siccus","1566","1566")],"bound album · mounted sheet · label data"),
 x("Loose-sheet herbarium","Linnaeus's free sheets that can be reordered in cabinets.","Herbarium","18th century",[],"sheet · collector label")])
c5=k("Insect in resin","Real insect or small animal specimen embedded in a clear resin block.","https://odditiesforsale.com/product-category/natural-specimens/",[])
c6=k("Fluid-preserved specimen","Wet specimen of an animal or other organism kept in preserving fluid in a jar.","https://www.skullsunlimited.com/collections/unique-offerings-at-skulls-unlimited",[
 x("Ethanol wet specimen","Soft-bodied animal stored in 70% ethanol in borosilicate glass; antique jars used formalin first.","Zoological_specimen","",[],"jar · fluid · label")],a="wet specimen")
out('06_03',[c1,c2,c3,c4,c5,c6],[],[],"Insect in resin kept without archetypes (Baltic amber is a natural fossil resin, covered under Fossils & amber). Goliath beetle sourced via Goliathus regius; tarantulas, scorpions, Ornithoptera A1 grade and cleared-and-stained specimens not confirmed on retrieved pages. Legal notes only as stated on fetched pages.")
