import sys; sys.path.insert(0,'work/F6/agent')
from lib import *
FE="https://www.fossilera.com/fossils-for-sale"
kinds=[
K("Fossil shark tooth","Fossil tooth of a shark or ray, loose or in a display, graded by size and root and enamel condition.",FE,[
 X("Megalodon tooth","Triangular, robust, serrated tooth of Otodus megalodon (Early Miocene to Early Pliocene), the largest of any shark, over 180 mm in slant height.",W+"Megalodon",a="Otodus megalodon · Carcharocles megalodon",
   y="Miocene–Pliocene",v=[("Aurora, North Carolina phosphate-mine tooth","","Teeth from the Aurora phosphate mine; Aurora Fossil Museum displays one"),("Bone Valley, Florida tooth","","Florida's Bone Valley Formation, proposed nursery area")],
   dt="V-shaped neck · no lateral denticles"),
 X("Otodus obliquus","Paleocene to Early Eocene lamnoid shark (about 65–54 million years ago) with a cosmopolitan range; teeth are the main fossils.",W+"Otodus_obliquus",y="Paleocene–Eocene",dt="cartilage skeleton · teeth and vertebrae only"),
 X("Cretoxyrhina (Ginsu shark)","Late Cretaceous shark nicknamed Ginsu shark in 1999; teeth typically 3–4 cm, known from the Niobrara Formation of Kansas.",W+"Cretoxyrhina",
   y="107–73 million years ago",dt="teeth 3–4 cm · Kansas chalk skeletons"),
 X("Squalicorax (crow shark)","Cretaceous lamniform crow shark with small serrated teeth 2.5–3 cm high, found in Europe, North Africa and North America.",W+"Squalicorax",
   y="Albian–Maastrichtian",v=[("Squalicorax pristodontus","","Recorded in North America, France, the Netherlands, Egypt, Morocco and Madagascar"),("Squalicorax volgensis","","Oldest species, Europe and Texas")],dt="curved serrated crown"),
 X("Peace River (Florida) shark teeth","Shark teeth sifted from the gravel of the Peace River in the Bone Valley area; Wauchula, Zolfo Springs and Arcadia are the access points.",W+"Peace_River_(Florida)",
   dt="Miocene and Pleistocene river gravel · mammal bones too"),
 ],a="shark teeth"),
K("Fossil fish","Fossil fish, whole or partial, usually on matrix.",FE,[
 X("Knightia (Green River)","Herring-like Eocene freshwater fish of the Green River Formation, Wyoming, the most commonly excavated fossil fish in the world; Wyoming's state fossil.",W+"Knightia",
   y="Eocene",dt="K. eocaena up to 25 cm, most under 15 cm · K. alta 6–10 cm"),
 X("Diplomystus","Predatory clupeomorph fish; D. dentatus of Fossil Butte, Wyoming reached 65 cm, often preserved with Knightia in its mouth, and Lebanese species are Late Cretaceous.",W+"Diplomystus",
   v=[("Diplomystus dentatus","Early Eocene","Freshwater, Green River Formation, Wyoming"),("Diplomystus birdi","Cenomanian","Marine, Lebanon")],dt="Fossil Butte · Lebanon"),
 X("Haqel Lebanese fish","Marine fish from the Cenomanian of Lebanon (about 98 million years ago), including the collection of Lebanon's first marine-fossil museum at Haqel.",W+"Haqel",
   y="Cenomanian",dt="limestone slabs"),
 X("Santana (Romualdo) fish","Fish from the Albian Romualdo Formation of the Santana Group, Brazil, which also yields pterosaurs and dinosaurs.",W+"Santana_Group",y="Albian",dt="Brazil"),
 ]),
K("Dinosaur fossil","Fossil tooth, bone, claw or egg of a dinosaur; collecting and sale rules vary with country and land ownership.",FE,[
 X("Spinosaurus tooth","Straight, conical, unserrated or lightly serrated tooth of Spinosaurus, named by Stromer in 1915 and known from the Kem Kem beds of Morocco.",W+"Spinosaurus",y="Cenomanian",dt="Kem Kem beds · Tafilalt"),
 X("Carcharodontosaurus tooth","Thin, recurved, serrated blade-like tooth (about 18–20 serrations per cm) of Carcharodontosaurus from the Kem Kem beds.",W+"Carcharodontosaurus",y="Cenomanian",dt="serrated both edges · Kem Kem beds"),
 X("Hadrosaur material","Teeth, eggshell, coprolites and bones of duck-billed dinosaurs, whose teeth are stacked into dental batteries; Late Cretaceous of Alberta and Montana.",W+"Hadrosauridae",a="duck-billed dinosaur",y="Late Cretaceous",dt="teeth · juvenile bones · Dinosaur Park Formation"),
 X("Triceratops","Late Maastrichtian horned dinosaur described by Marsh in 1889; horn and frill material from the Hell Creek Formation.",W+"Triceratops",y="1889",
   v=[("Holotype YPM 1820","1888","Collected in Wyoming by John Bell Hatcher")],dt="brow horns about 1 m · frill fragments"),
 X("Dinosaur egg","Fossil egg or eggshell; first recognised scientifically from Mongolia in 1923; dealers often expose only the bottom of the egg.",W+"Dinosaur_egg",y="1923",
   dt="Gobi · elongated theropod eggs · spherical sauropod and hadrosaur eggs · plaster-jacketed nests"),
 ],a="dinosaur teeth · dinosaur bone"),
K("Marine reptile fossil","Fossil jaw, tooth, vertebra or skeleton of a mosasaur, plesiosaur, ichthyosaur or other marine reptile.",W+"Mosasaur",[
 X("Mosasaur jaw and teeth","Late Cretaceous marine lizard with double-hinged jaws and constantly replaced teeth; Morocco's Upper Cretaceous phosphates are rich in finds.",W+"Mosasaur",
   y="94–66 million years ago",v=[("Globidens","","Blunt, rounded crushing teeth, Moroccan phosphates"),("Thalassotitan atrox","","Upper Maastrichtian phosphates, Morocco"),("Maastricht skull","1764","First mosasaur fossil, found near Maastricht")],dt="jaws · teeth · Moroccan phosphates · Kansas"),
 X("Plesiosaur","Long-necked marine reptile of the Late Triassic to Late Cretaceous; Mary Anning's family found a nearly complete skeleton at Lyme Regis in 1823.",W+"Plesiosaur",
   y="1823",v=[("Lyme Regis plesiosaur","1823","Described by Conybeare in 1824"),("Gastroliths","1877","Stomach stones first reported by Seeley")],dt="vertebrae · paddle bones · gastroliths"),
 ]),
K("Fossil reptile or amphibian","Fossil tooth, bone or skeleton of a non-dinosaur, non-marine reptile, amphibian or synapsid.",FE,[
 X("Kem Kem crocodyliforms","Crocodile relatives such as Elosuchus, Hamadasuchus and Aegisuchus from the Cenomanian Kem Kem beds of Morocco.",W+"Kem_Kem_Group",y="Cenomanian",dt="teeth · skulls · composite risk in the Kem Kem trade"),
 X("Pterosaur remains","Pterosaur bones from the Kem Kem beds, and a rich assemblage in the Crato and Romualdo formations of Brazil.",W+"Santana_Group",dt="Kem Kem · Crato · Romualdo"),
 X("Permian temnospondyl amphibians","Large Permian amphibians such as Eryops, and Prionosuchus of Brazil, over 5.5 m, the largest non-amniote tetrapod.",W+"Temnospondyli",y="Permian",dt="skeletons · Eryops"),
 ],a="synapsid"),
K("Fossil mammal","Fossil tooth, bone or other part of a mammal, such as mammoth, cave bear or sabre-toothed cat.",FE,[
 X("Woolly mammoth","Pleistocene mammoth known from permafrost carcasses; tusks up to 4.05 m and molars with up to 26 enamel ridges are the main collectables.",W+"Woolly_mammoth",
   dt="tusk 2.4–2.7 m typical male · molars · Siberian ivory"),
 X("Cave bear","Pleistocene bear that died out about 24,000 years ago, whose remains come mainly from caves; Drachenloch in Switzerland yielded more than 30,000 skeletons.",W+"Cave_bear",
   dt="broad domed skulls · large teeth · caves of Central Europe"),
 X("Smilodon","Sabre-toothed cat of the Pleistocene; canines up to about 28 cm in S. populator; Rancho La Brea has the largest collection.",W+"Smilodon",
   dt="La Brea since 1875 · canines · South America"),
 ]),
]
save("02_03",kinds,[],"Santana concretions, Khouribga teeth (page covers only phosphate mining) and ichthyosaurs (page is a disambiguation) not sourced, so left out as archetypes. Legality kept as a note in the Dinosaur fossil definition; Wikipedia Fossil collecting notes SVP position, private-land permission and stolen-fossil/smuggling cases only. Moroccan mosasaur teeth under Marine reptile fossil. Peace River kept as a locality archetype, since localities organise shark teeth.")
