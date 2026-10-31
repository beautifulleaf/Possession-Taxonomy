import sys; sys.path.insert(0,'work/F6/agent')
from lib import *
FE="https://www.fossilera.com/fossils-for-sale"
kinds=[
K("Trilobite","Fossil trilobite, prepared on or off matrix.",FE,[
 X("Elrathia kingii (Utah)","Middle Cambrian trilobite from the Wheeler Formation of Utah, among the most common trilobites in the US and dug commercially in large numbers.",W+"Elrathia",
   y="Middle Cambrian",dt="16–40 mm · on shale slabs · House Range, Utah"),
 X("Moroccan Devonian trilobites","Spiny and eyed trilobites from the Devonian of the Anti-Atlas, Morocco, including Phacops, Walliserops with its trident, and Dicranurus with curled horns.",W+"Walliserops",
   v=[("Phacops","Late Ordovician–Devonian","Schizochroal eyes; Morocco specimen is Eifelian",""),("Walliserops","Early–Middle Devonian","Trident on the glabella; Foum Zguid, Morocco",""),("Dicranurus","Early–Middle Devonian","Curled horn-like spines; Oklahoma, New York, Morocco","")],
   dt="prepared from nodules · the Moroccan trade has caused controversy over restoration · casts exist of some trilobites"),
 X("Asaphus kowalewskii","Middle Ordovician trilobite from the Volkhov area near St Petersburg, Russia, with eyestalks up to 5 cm; popular with collectors since the 1990s.",W+"Asaphus_kowalewskii",
   y="1856",dt="long eyestalks · Duboviki Formation, Baltic Klint"),
 X("Calymene blumenbachii (Dudley bug)","Silurian trilobite from the Wenlock Limestone at Dudley, England, named the Dudley Bug by 18th-century quarrymen.",W+"Calymene_blumenbachii",
   a="Dudley Bug · Dudley Locust",y="Silurian",dt="Wren's Nest, Dudley · Much Wenlock"),
 X("Isotelus","Large Ordovician trilobite, the state fossil of Ohio since 1985; I. rex reached about 72 cm.",W+"Isotelus",y="Ordovician",
   v=[("Isotelus rex","","Holotype about 72 cm from Churchill, Manitoba, the largest complete trilobite found")],dt="Cincinnatian strata of Ohio · Ontario · Manitoba"),
 X("Ogygiocarella","Middle Ordovician trilobite of Wales and Shropshire; O. debuchii is the most common trilobite in the Shelve inlier.",W+"Ogygiocarella",
   v=[("Ogygiocarella debuchii","1822","Type species with eleven pygidial ribs")],dt="Welsh and Shropshire shale"),
 ]),
K("Fossil crustacean","Fossil crab, lobster, shrimp or other crustacean, usually in a nodule or on matrix.",FE,[
 X("Eryma","Extinct lobster-like decapod genus with 44 species from the Permian to the Cretaceous, found in Europe and North America.",W+"Eryma",
   v=[("Eryma mandelslohi","","Pictured from the Upper Brown Jura at Bissingen unter Teck, Germany")],dt="often small · in nodules or limestone"),
 X("Mecochirus (Solnhofen)","Long-clawed decapod from the Late Jurassic into the Cenomanian; the type species is known from the Solnhofen limestones.",W+"Mecochirus",
   v=[("Mecochirus longimanatus","","Type species, from Solnhofen limestone")],dt="plattenkalk slab"),
 ]),
K("Eurypterid","Fossil sea scorpion, usually a moulted exoskeleton on shale.",W+"Eurypterid",[
 X("Eurypterus remipes","Silurian sea scorpion, 13–20 cm long, the first eurypterid discovered and New York's state fossil (1984).",W+"Eurypterus",
   y="Silurian",v=[("Bertie Formation specimen","","First specimen came from near Westmoreland, Oneida County, New York","")],dt="moulted exoskeletons · New York and Ontario"),
 X("Eurypterus tetragonophthalmus","Eurypterus species from the Rootsiküla Formation of Saaremaa, Estonia.",W+"Eurypterus",dt="Estonia"),
 ]),
K("Fossil horseshoe crab","Fossil horseshoe crab, most often Mesolimulus from the Solnhofen limestone, sometimes with its trackway.",W+"Mesolimulus",[
 X("Mesolimulus walchi (Solnhofen)","Late Jurassic horseshoe crab of the Solnhofen limestone, whose preservation of soft parts is unusually good.",W+"Mesolimulus",
   y="Late Jurassic",v=[("Kouphichnium walchi trackway","","Trackways with the animal at the end, some showing a circling death trace","")],dt="Kimmeridgian to Early Tithonian · plattenkalk slabs"),
 ]),
]
save("02_01",kinds,[],"Fakes and casts: only a casting mention for Isotelus rex and a note about Morocco restoration controversy found on retrieved pages; no forgery page retrieved. Green River shrimp not confirmed on the retrieved page, so left out. Eurypterus remipes localities as stated on Wikipedia.")
