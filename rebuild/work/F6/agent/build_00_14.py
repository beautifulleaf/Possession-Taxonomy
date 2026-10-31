from libf6a import *
kinds=[
K("Apophyllite","Hydrated potassium calcium silicate group specimen: clear to green pseudo-cubic crystals, often on zeolites; apophyllite-(K), -(Na).",W+"Apophyllite",[
 X("Fluorapophyllite-(K)","Fluorine-dominant apophyllite, formerly apophyllite-(KF), the common species.",W+"Apophyllite",dt="clear to green prisms · pyramid-capped"),
 X("Hydroxyapophyllite-(K)","Hydroxyl-dominant apophyllite, formerly apophyllite-(KOH).",W+"Apophyllite",dt="crystals"),
 X("Fluorapophyllite-(Na)","Sodium variant, formerly natroapophyllite.",W+"Apophyllite",dt="crystals"),
 X("Jalgaon apophyllite","Apophyllite from Jalgaon, India, the Deccan Traps source of many specimens.",W+"Apophyllite",dt="crystals with stilbite · cabinet"),
 X("Harz apophyllite","Apophyllite from the Harz Mountains, Germany.",W+"Apophyllite",dt="crystals"),
 X("Mont Saint-Hilaire apophyllite","Apophyllite from Mont Saint-Hilaire, Canada.",W+"Apophyllite",dt="crystals"),
]),
K("Okenite","Hydrated calcium silicate specimen: white fibrous 'cotton ball' balls in basalt geodes.",W+"Okenite",[
 X("Maharashtra okenite","Cotton-ball okenite from the Deccan Traps of Maharashtra.",W+"Okenite",dt="fibrous balls · bendable but fragile"),
 X("Disko Island okenite","Type-locality okenite from Disko Island, Greenland, described in 1828 and named for Lorenz Oken.",W+"Okenite",y="1828",dt="fibres"),
 X("Faroe and Irish okenite","Okenite from Bordoy and Streymoy, Faroe Islands, and Scawt Hill, Ireland.",H+"okenite.pdf",dt="fibres"),
 X("Chilean okenite","Okenite from Rio Putagan, Chile.",H+"okenite.pdf",dt="fibres"),
]),
K("Cavansite","Calcium vanadium silicate hydrate specimen: vivid sky-blue spherical rosettes on basalt, from Oregon and India.",W+"Cavansite",[
 X("Wagholi cavansite","Radiating sky-blue rosettes from quarries near Wagholi, Pune district, Maharashtra.",W+"Cavansite",dt="blue rosettes on stilbite · thumbnail to miniature"),
 X("Owyhee Dam cavansite","Cavansite from Owyhee Dam, Malheur County, Oregon, discovered 1967.",W+"Cavansite",y="1967",dt="rosettes"),
 X("Oregon cavansite (Chapman quarry)","Cavansite from the Chapman quarry, Columbia County, Oregon.",H+"cavansite.pdf",dt="rosettes"),
]),
K("Prehnite","Calcium aluminium silicate hydroxide specimen: light green botryoidal masses, rare square-section crystals; cut as gems.",W+"Prehnite",[
 X("Prehnite botryoids","Pale green botryoidal, reniform or stalactitic prehnite, first described in 1788 from Cradock, Eastern Cape.",W+"Prehnite",y="1788",dt="botryoidal masses"),
 X("Jeffrey mine prehnite","Square-section prehnite crystals from the Jeffrey mine, Asbestos, Quebec.",W+"Prehnite",dt="crystals"),
 X("Wave Hill prehnite","Gem-quality prehnite in basalt from Wave Hill Station, Northern Territory.",W+"Prehnite",dt="gem rough"),
 X("Orange prehnite","Rare orange prehnite found in the Kalahari Manganese Fields in April 2000.",W+"Prehnite",y="2000",dt="crystals"),
 X("Namibian prehnite","Prehnite from Copper Valley, Brandberg Mountains, Namibia.",H+"prehnite.pdf",dt="botryoidal"),
 X("Paterson prehnite","Prehnite from Paterson and Bergen Hill, New Jersey.",H+"prehnite.pdf",dt="botryoidal and crystalline"),
]),
K("Pectolite","Sodium calcium silicate hydroxide specimen: radiating white fibrous masses; the blue variety is larimar.",W+"Pectolite",[
 X("Larimar","Pale to sky-blue pectolite sought after as a gem stone, from the Dominican Republic.",W+"Pectolite",dt="polished stone, cabochon"),
 X("Alaska jade","Whitish pectolite sometimes marketed as Alaska jade.",W+"Pectolite",dt="carving"),
 X("Mount Baldo pectolite","First described in 1828 from Mount Baldo, Trento, Italy.",W+"Pectolite",y="1828",dt="fibrous masses"),
 X("Jeffrey mine pectolite","Fine pectolite crystals from the Jeffrey mine, Asbestos, Quebec.",H+"pectolite.pdf",dt="fibres"),
 X("Paterson pectolite","Pectolite from Paterson and Bergen Hill, New Jersey.",H+"pectolite.pdf",dt="radiating fibres"),
]),
K("Datolite","Calcium borosilicate hydroxide specimen: glassy colourless to pale green crystals and Lake Superior nodules.",W+"Datolite",[
 X("Lake Superior datolite","Fine-grained banded datolite nodules from the Michigan copper country, coloured by copper.",W+"Datolite",dt="nodule, polished"),
 X("Botryolite","Botryoidal form of datolite.",W+"Datolite",dt="botryoidal masses"),
 X("Dalnegorsk datolite","Exceptional datolite crystals from Dal'negorsk, Primorsky Krai.",H+"datolite.pdf",dt="crystals"),
 X("Charcas datolite","Very large datolite crystals from Charcas, San Luis Potosí.",H+"datolite.pdf",dt="very large crystals"),
 X("Westfield datolite","Large datolite crystals from the Lane quarry, Westfield, Massachusetts.",H+"datolite.pdf",dt="large crystals"),
 X("Arendal datolite","Type-locality datolite from Arendal, Norway; first observed in 1806 by Jens Esmark.",W+"Datolite",y="1806",dt="crystals"),
]),
]
notes=("All 6 planned kinds kept. HOM has no apophyllite file (apophyllite-KF 404); Wikipedia used. Sources: Wikipedia plus HOM (okenite, cavansite, prehnite, pectolite, datolite). "
 "Dominican Republic discovery years for larimar not on the page, omitted. Pune/Nashik apophyllite localities not on the apophyllite page; Jalgaon (India) used. No brands or traditions.")
finish("00_14",kinds,notes)
