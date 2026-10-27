import json,os
W='https://en.wikipedia.org/wiki/'
CB='https://www.conchology.be/?t=255'
def x(n,d,s,y='',v=None,dt='',a=''):
    return {"n":n,"a":a,"d":d,"mk":"","y":y,"s":W+s,"v":v or [],"dt":dt}
def v(n,d,y=''): return {"n":n,"mk":"","y":y,"d":d}
SZ="size in mm · grade (gem, F+++, F++, F+, F) · locality data · colour form"
def kd(n,d,s,xs,a="",t=None,tg=None):
    k={"n":n,"d":d,"s":s,"x":xs}
    if a:k["a"]=a
    if t:k["t"]=t
    return k
def out(job,kinds,notes):
    p=f'work/F6/shelves/{job}'
    json.dump({"kinds":kinds,"brands":[],"traditions":[],"notes":notes},open(p+'.tmp','w'),ensure_ascii=False,indent=1)
    os.rename(p+'.tmp',p+'.json')

# ---- 05_00
k=[]
k.append(kd("Cowrie","Shell of a cowrie (Cypraeidae); glossy, egg-shaped, from 5 mm to about 19 cm.",CB,[
 x("Tiger cowrie","Large Indo-Pacific cowrie with dark-spotted back; once common, now scarcer from collecting and dynamite fishing.","Cypraea_tigris","",[v("Schilderiana form","larger variety at 10–13 cm, from Hawaii, Johnston Island and Vietnam")],SZ+" · up to 15 cm","Cypraea tigris"),
 x("Golden cowrie","Large orange-brown Pacific cowrie, uncommon to rare; worn as a rank badge (bulikula) by Fijian chiefs.","Callistocypraea_aurantium","",[],SZ+" · 80–100 mm","Cypraea aurantium · Callistocypraea aurantium"),
 x("Money cowrie","Small flattened Indo-Pacific cowrie used as currency in Africa, Asia and the Pacific until the late 19th century.","Monetaria_moneta","",[v("Maldives","main source of trade cowries")],SZ+" · up to 30 mm","Monetaria moneta")],
 t=["Atlantic deer cowrie","chestnut cowrie"]))
k[0]["m"]=[["Tiger cowrie",""]]
k.append(kd("Cone shell","Shell of a cone snail (Conidae); live animals are venomous, so collect empty shells only.",CB,[
 x("Glory-of-the-sea cone","Slender Indo-Pacific cone (Conus gloriamaris), once the world's most prized shell; prices fell after its habitat was found in 1969.","Conus_gloriamaris","habitat found 1969",[v("Solomon Islands centre","range from the Philippines to Fiji and Samoa")],SZ+" · to 16 cm","Conus gloriamaris"),
 x("Textile cone","Common Indo-Pacific cone with a lace-like pattern; its sting has killed people, so live animals must not be handled.","Conus_textile","",[],SZ+" · 9–10 cm typical","Conus textile")],a="cone snail"))
k[1]["m"]=[]
k.append(kd("Murex shell","Shell of a murex or rock snail (Muricidae); over 1,700 living species.",CB,[
 x("Venus comb murex","Indo-Pacific murex with a very long siphonal canal and over a hundred fragile spines; perfect shells are hard to find.","Venus_comb_murex","",[v("Madagascar, Mascarenes, Queensland","largest populations")],SZ+" · 10–15 cm","Murex pecten")],a="rock snail"))
k.append(kd("Volute shell","Shell of a volute (Volutidae).",CB,[
 x("Cymbiola volutes","Genus of large Indo-Pacific volutes with thin boat-shaped shells, including Cymbiola nobilis, imperialis and vespertilio.","Cymbiola","",[v("Cymbiola imperialis","museum specimens on record")],SZ),
 x("Hunter's marbled volute","Largest Amoria, a deep-water Australian volute; Amoria zebra and A. damonii are other collector Amoria.","Amoria_hunteri","described 1931",[v("New South Wales and Queensland","deep water, 90–190 mm")],SZ+" · 90–190 mm","Amoria hunteri"),
 x("Amoria","Genus of glossy Australian volutes with brown pattern lines over a white, yellow or pink base.","Amoria_(gastropod)","",[],SZ+" · 20 to over 200 mm")]))
k[3]["m"]=[]
k.append(kd("Conch and stromb shell","Shell of a true conch (Strombidae): queen conch and the spider conchs (Lambis).",W+"Aliger_gigas",[
 x("Queen conch","Large Caribbean conch, CITES Appendix II; taking is banned in Florida, so check provenance and permits.","Aliger_gigas","CITES Appendix II",[v("Strombus gigas","earlier accepted name"),v("Conch pearl","about 1 in 10,000; pink valued")],SZ+" · 15–31 cm, max 35.2 cm","Strombus gigas · Eustrombus gigas"),
 x("Giant spider conch","Largest and heaviest spider shell, up to 40 cm, from the Indian Ocean and Philippines.","Lambis_truncata","",[],SZ),
 x("Spider conch","Indo-West Pacific conch with six hollow digitations; male and female digitations differ.","Lambis_lambis","",[],SZ+" · average 18 cm, max 29 cm","Lambis lambis")],a="strombus · Lambis",t=["spider conch"]))
k.append(kd("Olive shell","Glossy cylindrical shell of an olive snail (Olividae).",W+"Oliva_porphyria",[
 x("Tent olive","Large eastern Pacific olive with angular chestnut marks; its pattern is studied as a Turing pattern.","Oliva_porphyria","",[v("Panama to Peru","30–135 mm")],SZ,"Oliva porphyria"),
 x("Lettered olive","Atlantic olive, South Carolina's state shell.","Lettered_olive","",[v("North Carolina to Texas","usually 6 cm, max 9.1 cm")],SZ,"Oliva sayana")]))
k.append(kd("Helmet and bonnet shell","Heavy shell of a helmet or bonnet snail (Cassidae).",W+"Cassis_cornuta",[
 x("Horned helmet","Largest helmet shell, up to 41 cm, with horn-like knobs; strictly protected in Queensland.","Cassis_cornuta","",[],SZ,"Cassis cornuta"),
 x("King helmet","Western Atlantic helmet, reported as a cameo shell; to 30 cm.","Cassis_tuberosa","",[],SZ,"Cassis tuberosa"),
 x("Checkerboard bonnet","Indian Ocean bonnet with rows of squarish red-brown spots on white.","Phalium_areola","",[],SZ+" · 35–130 mm","Phalium areola")]))
k.append(kd("Triton shell","Large spiral shell of a triton snail (Charoniidae), used as a trumpet.",W+"Charonia_tritonis",[
 x("Triton's trumpet","Indo-Pacific giant triton up to 60 cm; blown as a conch trumpet (horagai, pūtātara); a CITES listing proposal was withdrawn in 1994.","Charonia_tritonis","",[],SZ,"Charonia tritonis")],a="triton's trumpet"))
k.append(kd("Harp shell","Ribbed shell of a harp snail (Harpidae).",W+"Harpa",[
 x("Harpa","Genus of harp shells with a large body whorl: major, articularis, davidis, doris and costata.","Harpa","",[v("Harpa major","large harp, 60–130 mm")],SZ)]))
k.append(kd("Mitre shell","Slender spired shell of a mitre snail (Mitridae).",W+"Mitridae",[
 x("Episcopal mitre","Indo-Pacific mitre, white with spiral rows of orange-red spots, up to 18 cm.","Mitra_mitra","",[],SZ,"Mitra mitra")]))
k.append(kd("Abalone shell","Ear-shaped nacre-lined shell of an abalone (Haliotidae).",W+"Abalone",[
 x("Pāua","New Zealand blackfoot abalone, iridescent shell central to Māori and Kiwi craft.","Haliotis_iris","",[],SZ+" · 80–170 mm","Haliotis iris · blackfoot pāua")],t=["red abalone","green abalone","black abalone"]))
k.append(kd("Wentletrap shell","Spiral shell of a wentletrap (Epitoniidae).",W+"Epitonium_scalare",[
 x("Precious wentletrap","Ribbed spiral shell once sold for large sums in the 17th–18th centuries.","Epitonium_scalare","described 1758",[v("Red Sea to Japan","25–72 mm")],SZ,"Epitonium scalare")]))
k.append(kd("Land snail shell","Shell of a land snail kept for colour forms.",W+"Polymita_picta",[
 x("Cuban painted snail","Brightly banded Cuban tree snail; CITES Appendix I and protected since 1943.","Polymita_picta","",[],SZ+" · to 20 mm","Polymita picta"),
 x("Florida tree snail","Tree snail with 52 Florida colour forms and over 70 in Cuba.","Liguus_fasciatus","",[],SZ+" · 42–68 mm","Liguus fasciatus"),
 x("Papustyla","Genus of Manus Island tree snails, including the emerald green snail (P. pulcherrima).","Papustyla","",[],SZ)]))
out('05_00',k,"All new kinds sourced from Wikipedia species/family pages retrieved. Venus comb murex, Cymbiola and other aliases given as Wikipedia names. Cowrie leucodon, Murex troscheli, Conus geographus and Amoria zebra were not fetched so only named in definitions or omitted. CITES notes only where a retrieved page states them.")

# ---- 05_01
k=[]
k.append(kd("Scallop shell","Shell or valve of a scallop (Pectinidae).",CB,[
 x("Great scallop","Northeast Atlantic scallop, the St James shell carried by pilgrims to Santiago de Compostela.","Pecten_maximus","",[],SZ+" · to 21 cm","Pecten maximus · St James shell"),
 x("Lion's paw scallop","Knobbed Atlantic scallop in red, orange, purple or yellow.","Nodipecten_nodosus","",[],SZ+" · 6.4–15.2 cm","Nodipecten nodosus")]))
k.append(kd("Thorny oyster","Spiny, cemented bivalve (Spondylus), related to scallops, with a ball-and-socket hinge.",W+"Spondylus",[
 x("Regal thorny oyster","Western Pacific Spondylus with long spines.","Spondylus_regius","described 1758",[],SZ+" · to 156 mm","Spondylus regius"),
 x("Spondylus (Andean and Mediterranean)","Shells of S. crassisquama (Andean offering and currency) and S. gaederopus (Neolithic bangles).","Spondylus","",[],SZ)]))
k.append(kd("Giant clam shell","Shell of a giant clam (Tridacna); all giant clams are CITES Appendix II.",W+"Giant_clam",[
 x("Giant clam","Largest living bivalve, over 200 kg; CITES Appendix II, IUCN Critically Endangered; shells need permits.","Giant_clam","CITES Appendix II",[],SZ,"Tridacna gigas")]))
k.append(kd("Cockle shell","Shell of a cockle (Cardiidae).",W+"Corculum_cardissa",[
 x("Heart cockle","Translucent heart-shaped Indo-Pacific cockle that hosts algae.","Corculum_cardissa","",[],SZ,"Corculum cardissa")]))
k.append(kd("Chambered nautilus shell","Coiled pearly shell of a nautilus; all nautilus species are in CITES Appendix II since 2016.",W+"Chambered_nautilus",[
 x("Chambered nautilus","Pacific nautilus with shells up to 254 mm; CITES Appendix II (2016), IUCN Vulnerable.","Chambered_nautilus","CITES Appendix II 2016",[v("Nautilus pompilius pompilius","Andaman Sea to Fiji")],SZ,"Nautilus pompilius")]))
k.append(kd("Paper nautilus","Thin eggcase of a female argonaut octopus, not a true shell.",W+"Argonauta_argo",[
 x("Greater argonaut","Largest argonaut eggcase, to 300 mm; strands on South African and Australian coasts.","Argonauta_argo","",[],SZ,"Argonauta argo")]))
k.append(kd("Brachiopod shell","Shell of a living-species brachiopod (lamp shell) kept as a specimen. Fossil brachiopods are under Fossil brachiopod.",CB,[
 x("Lamp shell","Living brachiopods, mostly 10–30 mm; articulate types have hinge teeth.","Brachiopod","",[],SZ)],a="lamp shell"))
out('05_01',k,"Scallop shell and Brachiopod shell keep old sources; the rest sourced from retrieved Wikipedia. CITES statements: giant clam and nautilus per retrieved pages. Cardiidae/Tridacnidae relationship not stated on pages so not discussed. Living-species counts on the Brachiopod page differ (about 330–400).")

# ---- 05_02
k=[]
k.append(kd("Coral skeleton","Dead, dried skeleton of a coral. Living coral is not sold here; fossil coral is under Fossil coral. Stony corals are CITES Appendix II.","https://www.wardsci.com/us/en/product/8886943/sea-fan-coral-dry",[
 x("Staghorn coral","Branching Acropora skeleton of aragonite; Atlantic staghorn is IUCN Critically Endangered.","Staghorn_coral","",[],"branch length · colour (bleached white)","Acropora cervicornis"),
 x("Brain coral","Maze-patterned stony coral skeleton, such as Diploria labyrinthiformis.","Scleractinia","",[],"diameter · polished or natural"),
 x("Acropora","Genus of table, elkhorn and staghorn corals, over 149 species.","Acropora","",[],"branch · plate")],t=["sea fan","gorgonian"]))
k.append(kd("Sea urchin test","Dried, emptied shell (test) of a sea urchin.","https://www.catawiki.com/ja/l/105972437-no-reserve-price",[
 x("Sand dollar","Flat Clypeasteroida test, 80–100 mm; bleached tests wash ashore.","Sand_dollar","",[v("Keyhole sand dollars (Mellita)","Caribbean"),v("Eccentric sand dollar","Dendraster excentricus")],"diameter · lunules · bleached"),
 x("Slate pencil urchin","Cidaroid urchin with thick blunt spines; spines sold as 'pencils'.","Sea_urchin","",[v("Heterocentrotus mamillatus","slate pencil urchin")],"spine length · whole test"),
 x("Heart urchin","Oval irregular urchin test, such as Echinocardium.","Sea_urchin","",[],"length")]))
k.append(kd("Dried starfish","Dried whole starfish (sea star) kept as a specimen. A fossil starfish is under Echinoderm fossil; craft assortments are in Craft & Art Supplies.","https://www.catawiki.com/ja/l/105972437-no-reserve-price",[
 x("Sea star","Asteroidea, about 1,900 species, usually five arms, dried for display.","Starfish","",[v("Crown-of-thorns starfish","Acanthaster planci")],"arm span · species"),
 x("Brittle star","Ophiuroidea with disc 3–150 mm and slender arms up to 60 cm.","Brittle_star","",[],"disc diameter · arm length")],a="sea star"))
out('05_02',k,"Sea fan (gorgonian) kept as a type since no Wikipedia page was retrieved for it. Old sources kept for the three planned kinds. Urchin archetypes sourced to the Sea urchin article. Colour-form and grade axes noted in dt.")
