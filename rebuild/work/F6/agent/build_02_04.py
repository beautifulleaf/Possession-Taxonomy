import sys; sys.path.insert(0,'work/F6/agent')
from lib import *
FE="https://www.fossilera.com/fossils-for-sale"
PW=W+"Petrified_wood"
kinds=[
K("Petrified wood","Fossil wood replaced by silica or other minerals, rough, slab or polished.",FE,[
 X("Arizona petrified wood","Late Triassic logs (about 225–207 million years ago) of the Chinle Formation, mostly Araucarioxylon arizonicum; removal from Petrified Forest National Park is prohibited.",W+"Petrified_Forest_National_Park",
   y="Late Triassic",dt="iron-oxide colours · polished slabs"),
 X("Madagascar petrified wood","Silicified wood from the north-west coast of Madagascar.",PW,dt="polished slabs · rounds"),
 X("Indonesian petrified wood","Silicified wood from Banten and Mount Halimun Salak National Park area.",PW,dt="polished slabs · cabochons"),
 X("Patagonian petrified forests","Trunks over 3 m in diameter in the Sarmiento and Jaramillo Petrified Forests, Santa Cruz Province, Argentina.",PW,dt="large trunks"),
 X("Opalised wood","Wood replaced by opal, notably Chinchilla Red from Chinchilla, Queensland.",PW,a="wood opal",dt="Australian deposits · opal replacement"),
 ]),
K("Plant fossil","Fossil leaf, fern, frond, seed or cone, as an impression, compression or nodule. Petrified wood is separate.",FE,[
 X("Mazon Creek ferns","Fern and seed-fern fronds such as Pecopteris preserved in siderite concretions about 309 million years old from Illinois; the flora has over 400 species.",W+"Mazon_Creek_fossil_beds",
   y="Pennsylvanian",v=[("Tully monster","","Tullimonstrum gregarium, Illinois state fossil, known only from Mazon Creek")],dt="split ironstone nodules · permit needed at Braidwood State Fish and Wildlife Area"),
 X("Glossopteris","Permian seed-plant genus of Gondwana with tongue-shaped leaves 2–30 cm long; matching fossils across southern continents supported continental drift.",W+"Glossopteris",
   y="Permian",dt="leaf impressions · India, Australia, South America, Africa, Antarctica"),
 X("Fossil ginkgo leaves","Leaf fossils of Ginkgo, a living fossil whose genus first appears in the Middle Jurassic; localities include Scarborough (Jurassic) and McAbee, British Columbia (Eocene).",W+"Ginkgo_biloba",
   y="Middle Jurassic",dt="fan-shaped leaves"),
 X("Green River leaves","Fossil palm, fern and sycamore leaves of the Eocene Green River Formation, some showing insect damage.",W+"Green_River_Formation",y="Eocene",dt="Wyoming"),
 ]),
K("Stromatolite","Layered fossil structure built by microbial mats, rough or polished.",FE,[
 X("Strelley Pool stromatolites","About 3.4 billion-year-old stromatolites in the Strelley Pool chert of the Pilbara Craton, Western Australia.",W+"Stromatolite",y="3.4 billion years",dt="chert"),
 X("Shark Bay stromatolites","Living stromatolites at Hamelin Pool, Western Australia (protected, not collectable); the modern analogue for fossils.",W+"Stromatolite",dt="reference locality"),
 X("Collenia","Common Proterozoic stromatolite genus.",W+"Stromatolite",y="Proterozoic",dt="polished sections"),
 ]),
K("Trace fossil","Fossil track, footprint, burrow, boring or coprolite left by an organism rather than its body.",FE,[
 X("Dinosaur footprint","Fossil track of a walking dinosaur; a trackway is a sequence of tracks from a single animal. Famous sites include Lark Quarry, the Paluxy River and Ardley.",W+"Fossil_track",
   a="ichnite",v=[("Lark Quarry Dinosaur Trackways","","Queensland, Australia"),("Paluxy River, Dinosaur Valley State Park","1969","Texas, National Natural Landmark 1969"),("Ardley prints","","Oxfordshire; most survive only as replicas")],dt="slab or cast"),
 X("Coprolite","Fossilised droppings, named by William Buckland in 1829; mined for phosphate in nineteenth-century eastern England.",W+"Coprolite",y="1829",
   v=[("Lyme Regis bezoar stones","","Found by Mary Anning in ichthyosaur skeletons")],dt="polished sections reveal diet"),
 X("Gastrolith","Stomach or gizzard stone; real gastroliths are rounded, polished on high points and differ from local rock.",W+"Gastrolith",a="stomach stone",dt="polished · sauropods, plesiosaurs"),
 X("Fossil burrow","Burrows such as vertical Skolithos tubes and branching Thalassinoides systems, and borings in hard surfaces.",W+"Trace_fossil",dt="burrow casts · borings in shells"),
 ],a="ichnofossil"),
]
save("02_04",kinds,[],"Bolivian and Australian stromatolite sales, Madagascar petrified wood specifics and polished-slab details not confirmed by pages, so left generic. Coprolites and footprints are archetypes of Trace fossil as planned. Green River leaves cite the Green River Formation page retrieved in job 02_01.")
