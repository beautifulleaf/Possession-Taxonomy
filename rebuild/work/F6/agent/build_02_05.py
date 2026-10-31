import sys; sys.path.insert(0,'work/F6/agent')
from lib import *
FE="https://www.fossilera.com/fossils-for-sale"
kinds=[
K("Amber","Fossilised tree resin, raw, polished or cut, with or without insects or other inclusions; organised by deposit.",FE,[
 X("Baltic amber","Eocene amber (succinite, 3–8% succinic acid) from the Prussian Formation; over 90% of the world's amber comes from Kaliningrad Oblast, and it has been traded since the Neolithic.",W+"Baltic_amber",
   a="succinite",y="Eocene",v=[("Kaliningrad Amber Combine output","2015","400 tonnes extracted in 2015")],dt="insects over 98% of animal inclusions · mosses and liverworts · feathers and reptiles rare"),
 X("Dominican amber","Almost always transparent amber from the Dominican Republic, with rare fluorescent blue amber reported mostly from Palo Quemado, and many ant, termite and plant inclusions.",W+"Dominican_amber",
   a="blue amber",dt="Cordillera Septentrional, Bayaguana, Sabana de la Mar · Miocene to about 40 Ma estimates · blue fluorescence"),
 X("Burmese amber (burmite)","Mid-Cretaceous amber (about 100 million years old) from the Hukawng Valley, Kachin State, Myanmar, with rich arthropod and some vertebrate inclusions; ethics concerns over conflict funding.",W+"Burmese_amber",
   a="burmite · Kachin amber",y="Cretaceous",v=[("Society of Vertebrate Paleontology moratorium proposal","2017","Proposed no publication on specimens bought from Myanmar sources after June 2017")],
   dt="Tengchong main market · Myitkyina trade · ethical provenance issues"),
 X("Mexican (Chiapas) amber","Miocene amber from Simojovel and other Chiapas mines, protected designation of origin, comparable in quality to Dominican amber; Mexican law recognises 17 colourations.",W+"Mexican_amber",
   a="Chiapas amber",y="Miocene",dt="Simojovel produces about 95% · white to red, green, blue, black"),
 X("Lebanese amber","Early Cretaceous amber (about 130–125 million years ago) from the Grès du Liban, the oldest amber with a significant number of inclusions.",W+"Lebanese_amber",y="Early Cretaceous",
   dt="small pieces · arthropod inclusions"),
 X("Pressed and imitation amber","Pressed amber (ambroid) made by heating and compressing fragments; also copal, kauri gum, celluloid, Bakelite and acrylic fakes.",W+"Amber",a="ambroid · reconstituted amber",
   dt="pressed amber shows interference colours in polarised light · tests: infrared spectroscopy"),
 ],t=["Raw","Polished","With inclusion","Treated (oil-clarified)"]),
K("Copal","Young, partly fossilised tree resin, sold beside amber.","https://ukfossils.com/product-category/insects/",[
 X("Colombian and Madagascan copal","Subfossil copal found in Colombia, Madagascar, Japan and the Dominican Republic, often with insect inclusions.",W+"Copal",a="young amber",
   dt="lighter citrine colour than amber · acetone or chloroform makes the surface tacky"),
 X("Kauri gum","Well-known subfossil copal from the New Zealand kauri Agathis australis.",W+"Copal",dt="New Zealand"),
 X("East African copal","Subfossil resin of Hymenaea verrucosa from East Africa, lying one or two metres below living trees.",W+"Copal",dt="harder varnish resin"),
 ]),
K("Fossil insect","Fossil insect or other land arthropod preserved in rock. An insect in amber or copal is under Amber or Copal.",FE,[
 X("Crato Formation insects","Compression fossils in limestone from the Aptian Crato Formation, Brazil (about 113 million years ago), with abundant dragonflies and damselflies.",W+"Crato_Formation",
   y="Aptian",dt="limestone nodules and slabs · soft tissue preserved · illegal trade concerns"),
 X("Green River insects","Often complete insects preserved in the Eocene Green River Formation of Wyoming.",W+"Green_River_Formation",y="Eocene",dt="shale slabs"),
 ]),
]
save("02_05",kinds,[],"Inclusion types are detail axes (dt) in Amber. Lebanese amber age differs inside the Wikipedia article (Hauterivian vs Barremian), so given as Early Cretaceous. Green River shrimp and Colombian/Madagascan copal specifics (only the list of localities) are minimal. Insect-in-amber inclusions are not separate kinds.")
