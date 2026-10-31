import sys; sys.path.insert(0,'work/F6/agent')
from lib import *
FE="https://www.fossilera.com/fossils-for-sale"
kinds=[
K("Crinoid","Fossil sea lily: calyx and arms on matrix, plates, or loose stem segments (columnals).",W+"Crinoid",[
 X("Crawfordsville crinoids","Crinoids such as Actinocrinites gibsoni from the Lower Mississippian Edwardsville Formation around Crawfordsville, Indiana.",W+"Crinoid",
   y="Mississippian",dt="calyx with arms · on matrix"),
 X("Seirocrinus","Early Jurassic crinoid of the Posidonia Shale at Holzmaden, Germany; a pseudoplanktonic log-raft colonist reaching close to 30 m overall, the largest known crinoid.",W+"Seirocrinus",
   mk="",y="Jurassic",v=[("Seirocrinus subangularis","","Early Jurassic Posidonia Shale")],dt="large slabs and stem plates · up to 20–26 m stems"),
 X("Encrinite and columnals","Disarticulated stem segments so abundant they form rock called encrinite, used historically as beads (St Cuthbert's beads, Indian beads).",W+"Crinoid",
   a="St Cuthbert's beads · Indian beads",dt="Lower Carboniferous limestone near Clitheroe, England"),
 ]),
K("Echinoderm fossil","Fossil echinoderm (sea urchin, starfish, blastoid; crinoids are their own kind).",FE,[
 X("Micraster","Heart-shaped infaunal sea urchin of the Late Cretaceous to early Eocene, found in chalk across Europe, Africa, Antarctica and North America.",W+"Micraster",
   y="Late Cretaceous",dt="chalk flints · burrowing echinoid"),
 X("Clypeaster","Cake urchin or sea biscuit, a sand-dollar relative from the Late Eocene with living members.",W+"Clypeaster",a="cake urchin · sea biscuit",y="Late Eocene",dt="flattened test"),
 X("Blastoid","Extinct stalked echinoderm or 'sea bud' of the Ordovician to Permian, peaking in the Mississippian.",W+"Blastoid",a="Pentremites",
   v=[("Pentremites godoni","","Lower Carboniferous of Illinois","")],dt="five food grooves · Illinois · Wisconsin"),
 ]),
K("Fossil brachiopod","Fossil lamp shell (brachiopod), loose, pyritised or on matrix.",FE,[
 X("Spirifer","Carboniferous spiriferid brachiopod named by Sowerby in 1818, known from Great Britain and Canada.",W+"Spirifer",y="1818",dt="winged hinge line"),
 ],a="lamp shell"),
K("Fossil bivalve","Fossil clam, oyster, scallop or other bivalve shell, whole, opalised or on matrix.",FE,[
 X("Gryphaea (devil's toenail)","Curved Jurassic oyster, called devil's toenail; folklore held that carrying one prevented rheumatism.",W+"Gryphaea",a="devil's toenail",y="Late Triassic–Late Jurassic",
   v=[("Gryphaea arcuata","","Best-documented European species, Hettangian to Sinemurian Lias"),("Gryphaea gigantea","","Large species of the late Pliensbachian of England")],dt="Lias of England"),
 X("Exogyra","Cretaceous and Jurassic oyster cemented by a cupped left valve; Exogyra texana is from Texas.",W+"Exogyra",
   v=[("Exogyra texana","1849","Species described by Roemer")],dt="Texas Cretaceous"),
 ]),
K("Fossil gastropod","Fossil snail shell (gastropod), whole, agatised or on matrix.",FE,[
 X("Turritella agate","Agate packed with freshwater snail shells of Elimia tenera from the Eocene Green River Formation, Wyoming, first misnamed for the sea snail Turritella.",W+"Elimia_tenera",
   a="Elimia agate",y="1845",v=[("Fort Laclede Bed","","Laney Member, Green River Formation, Sweetwater County, Wyoming: best-preserved shells")],dt="chalcedony-rich rock · polished"),
 ]),
K("Fossil coral","Fossil coral, solitary or colonial, rough, polished or on matrix. A dead modern coral skeleton is under Coral skeleton.",FE,[
 X("Petoskey stone","Polished fossil rugose coral Hexagonaria percarinata, Devonian, found as glacial pebbles on Lake Michigan beaches; Michigan's state stone since 1965.",W+"Petoskey_stone",
   y="Devonian",dt="six-sided pattern shows when wet or polished · 25 lb limit on state lands"),
 X("Horn coral (Rugosa)","Rugose coral with a horn-shaped skeleton and wrinkled wall, abundant from the Middle Ordovician to the Late Permian.",W+"Rugosa",a="rugose coral",
   dt="solitary horns (Caninia, Streptelasma) · colonial Lithostrotion"),
 X("Favosites (honeycomb coral)","Tabulate coral with closely packed polygonal corallites, Late Ordovician to Late Permian, described by Lamarck in 1816.",W+"Favosites",a="honeycomb coral",y="1816",dt="worldwide except Antarctica"),
 ]),
K("Bryozoan fossil","Fossil bryozoan colony (moss animal), such as Archimedes screw or fenestrate lace, on or off matrix.",FE,[
 X("Archimedes","Carboniferous to Permian bryozoan whose mesh is wound round a corkscrew-shaped central axis, after Archimedes' screw.",W+"Archimedes_(bryozoan)",y="Tournaisian–Leonard",dt="screw axis isolated or with lace"),
 ]),
K("Graptolite","Fossil graptolite colony, usually on a shale slab.",FE,[
 X("Didymograptus","Tuning-fork-shaped graptolite, as in Didymograptus murchisoni; used to date Ordovician rocks.",W+"Graptolite",dt="carbon film on shale"),
 X("Dictyonema","Branching, dendritic graptolite.",W+"Graptolite",dt="fan-shaped colonies"),
 X("Welsh and Scottish graptolite shales","Classic shale localities for graptolites include Abereiddy Bay in Wales and Dob's Linn in Scotland.",W+"Graptolite",dt="black films, sometimes pyritised in three dimensions"),
 ]),
K("Fossil sponge","Fossil sponge, whole or sectioned, loose or on matrix.",FE,[
 X("Hexactinellid (glass) sponge","Silica-spicule sponges, common as fossils; Pattersonia ulrichi is an Ordovician example from near Cincinnati, Ohio.",W+"Hexactinellid",a="glass sponge",
   dt="silica spicules fossilise well"),
 ]),
]
save("02_02",kinds,[],"Ventriculites, LeGrand crinoids and starfish fossils left out: no retrieved page confirmed them (LeGrand page covers only a quarry town). Crinoid is a new kind split from Echinoderm fossil. Archimedes localities (Indiana/Kentucky) not confirmed on the page, so omitted.")
