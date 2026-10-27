import sys; sys.path.insert(0,'work/F6/agent')
from lib import *
FE="https://www.fossilera.com/fossils-for-sale"
kinds=[
K("Ammonite","Fossil ammonoid shell, whole, split, polished or on matrix, including unworked stones kept for a religious tradition.",FE,[
 X("Cleoniceras (Madagascar)","Involute, high-whorled Albian ammonite from Madagascar, Europe and the Transcaspian region, often sold split and polished.",W+"Cleoniceras",y="Albian",dt="Madagascar · split and polished · whole"),
 X("Dactylioceras","Widespread Lower Jurassic ammonite (about 180 million years old) with strong forward-leaning ribs; an index fossil.",W+"Dactylioceras",y="Early Jurassic",
   dt="about 65 mm across · about 70 species · England, Germany · mass-mortality slabs"),
 X("Asteroceras (Lyme Regis)","Lower Jurassic ammonite from Lyme Regis, Dorset, collected from the obtusum zone of the Upper Sinemurian.",W+"Asteroceras",y="Early Jurassic",
   v=[("Asteroceras obtusum","1817","Species described by Sowerby")],dt="Dorset · coastal collecting"),
 X("Placenticeras","Late Cretaceous ammonite from Asia, Europe and the Americas, source of most gem ammolite.",W+"Placenticeras",y="Late Cretaceous",
   v=[("Placenticeras meeki","","Species also found in the Pierre Shale of Montana and South Dakota"),("Placenticeras intercalare","","Species of the Bearpaw Formation, Alberta")],dt="iridescent shell · South Dakota · Alberta"),
 X("Baculites","Almost straight heteromorph ammonite of the Late Cretaceous, named by Lamarck in 1799; common in rock shops.",W+"Baculites",y="1799",dt="straight shell · intricate suture line"),
 X("Didymoceras","Bizarrely shaped heteromorph ammonite from about 76 million years ago whose shell spirals upwards into a hooked tip.",W+"Didymoceras",y="Late Cretaceous",dt="spiral heteromorph · rare complete"),
 X("Shaligram","Ammonite stone collected from the Kali Gandaki river in Nepal and India and worshipped in Hinduism as a form of Vishnu.",W+"Shaligram",a="shaligrama shila",dt="unworked river stone · religious object"),
 ]),
K("Ammolite","Gem-quality iridescent ammonite shell material, rough or cut.",FE,[
 X("Alberta ammolite","Iridescent aragonite shell of Placenticeras ammonites from the Bearpaw Formation, mined mostly along the St. Mary River in southern Alberta.",W+"Ammolite",
   mk="Korite",y="1981",v=[("CIBJO gem status","1981","Official gemstone status granted and commercial mining began")],
   dt="red and green most common · blue and purple rarer · grades AAA to A− (not standardised)"),
 X("Ammolite doublet and triplet","Composite stones: thin ammolite on a dark backing (doublet) with a transparent convex cap (triplet).",W+"Ammolite",
   dt="backing of matrix, onyx or glass · cap of synthetic spinel, corundum, quartz or glass"),
 ],t=["Doublet","Triplet","Solid"]),
K("Fossil nautiloid","Fossil coiled nautiloid shell, whole, split or polished. Straight-shelled nautiloids such as Orthoceras are listed here too; belemnites are a different group.",FE,[
 X("Orthoceras","Straight-shelled nautiloid; strictly Orthoceras regulare of the Middle Ordovician limestones of Sweden and the Baltic, though the name was long used for many orthocones.",W+"Orthoceras",
   a="orthocone · straight cephalopod",y="Middle Ordovician",dt="simple suture line · often confused with Baculites in shops"),
 X("Cenoceras","Extinct genus of the nautilid family Nautilidae, described by Hyatt in 1884; type species Cenoceras intermedium.",W+"Cenoceras",y="1884",dt="coiled shell"),
 ]),
K("Belemnite","Fossil belemnite guard, the solid calcite tip of an extinct squid-like cephalopod.",FE,[
 X("Belemnitella","Late Cretaceous belemnite of Europe and North America; the state fossil of Delaware since 1996.",W+"Belemnitella",y="Late Cretaceous",dt="guard (rostrum)"),
 X("Jurassic belemnite guards","Guards of genera such as Cylindroteuthis and Hibolithes, found from the Jurassic into the Early Cretaceous.",W+"Belemnitida",
   v=[("Cylindroteuthis","","Early Jurassic to Early Cretaceous; Asia, Europe, North America, New Zealand",""),("Hibolithes","","Middle Jurassic to Early Cretaceous; many continents","")],
   dt="called thunderbolts in folklore · polished sections"),
 ]),
]
brands=[B("Korite","Canada","","Specialist","ammolite","Calgary-based miner and the largest commercial producer of gem ammolite, supplying over 90% of it.",W+"Korite")]
save("02_00",kinds,brands,"Orthoceras alias moved from Belemnite to Fossil nautiloid. Moroccan Orthoceras and pyritised Lyme Regis ammonites not covered: no retrieved page confirmed them. Ammonite kept as one kind with Shaligram as the religious-stone archetype.")
