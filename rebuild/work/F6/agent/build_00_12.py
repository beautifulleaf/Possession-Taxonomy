from libf6a import *
kinds=[
K("Muscovite","Potassium aluminium mica mineral specimen: silvery sheets and books, plus chromium-green fuchsite.",W+"Muscovite",[
 X("Fuchsite","Green chromium-rich muscovite.",W+"Muscovite",dt="rough, slab, sphere"),
 X("Mariposite","Chromium-rich mica variety.",W+"Muscovite",dt="slab"),
 X("Roscoelite","Vanadium-rich muscovite.",W+"Muscovite",dt="scaly mass"),
 X("Sheet mica book","Large sheets of muscovite from pegmatites; Nellore, India has produced sheets up to 5 × 3 m.",W+"Muscovite",dt="book, sheet"),
 X("Mount Mica muscovite","Muscovite from Mt Mica, Maine, and other New England pegmatites.",H+"muscovite.pdf",dt="crystals"),
 X("Slyudyanka muscovite","Muscovite from Slyudyanka, near Lake Baikal.",H+"muscovite.pdf",dt="crystals"),
]),
K("Lepidolite","Lithium mica mineral specimen: pink, purple or lilac scaly masses, the commonest lithium mineral.",W+"Lepidolite",[
 X("Brazilian lepidolite","Lepidolite from Brazil, often with tourmaline.",W+"Lepidolite",dt="scaly mass, tumbled"),
 X("Tanco lepidolite","Lepidolite from the Tanco mine, Bernic Lake, Manitoba, also a source of rubidium.",W+"Lepidolite",dt="masses"),
 X("Madagascan lepidolite","Lepidolite from Madagascar.",W+"Lepidolite",dt="masses"),
 X("Urals lepidolite","Lepidolite from the Ural Mountains, Russia.",W+"Lepidolite",dt="masses"),
]),
K("Biotite","Dark mica group specimen (annite-phlogopite series): black to brown books and plates.",W+"Biotite",[
 X("Biotite books","Large black biotite sheets; recorded crystals reach about 7 m² at Iveland, Norway.",W+"Biotite",dt="books, plates"),
 X("Vesuvius biotite","Biotite from the lava of Mount Vesuvius.",W+"Biotite",dt="crystals"),
 X("Bancroft biotite","Biotite crystals from Bancroft and Sudbury, Ontario.",W+"Biotite",dt="crystals"),
]),
K("Phlogopite","Magnesium mica mineral specimen: brown to golden books, the largest single crystals known are phlogopite.",W+"Phlogopite",[
 X("Lacey mine phlogopite","Phlogopite from the Lacey mine, Ontario, where a single crystal of about 330 tonnes was found.",W+"Phlogopite",dt="giant crystal · books"),
 X("Franklin and Edwards phlogopite","Phlogopite from Franklin, New Jersey and Edwards, Pierrepont, St Lawrence County, New York.",H+"phlogopite.pdf",dt="crystals in marble"),
 X("Slyudyanka phlogopite","Phlogopite from the Slyudyanka region, Lake Baikal.",H+"phlogopite.pdf",dt="crystals"),
 X("Quebec phlogopite","Phlogopite from Perkin's Mills and Gatineau County, Quebec.",H+"phlogopite.pdf",dt="crystals"),
]),
K("Clinochlore","Magnesium chlorite mineral specimen: green platy crystals; seraphinite is a decorative variety.",W+"Clinochlore",[
 X("Seraphinite","Massive compact clinochlore with feathery silver-green sheen, from the Korshunovskoye deposit, Irkutsk, Russia; used for carving.",W+"Clinochlore",dt="polished slab, cabochon"),
 X("Ripidolite","Variety of clinochlore.",W+"Clinochlore",dt="platy"),
 X("Zillertal and Ala clinochlore","Clinochlore from the Zillertal, Tirol and the Ala Valley, Piedmont.",H+"clinochlore.pdf",dt="crystals"),
 X("Tilly Foster clinochlore","Clinochlore from the Tilly Foster mine, Brewster, New York.",H+"clinochlore.pdf",dt="crystals"),
 X("Chlorite quartz","Quartz with chlorite inclusions from Minas Gerais, Brazil.",W+"Clinochlore",dt="included quartz"),
]),
K("Talc","Hydrated magnesium silicate, Mohs 1: the softest mineral; soapstone is the massive carving rock.",W+"Talc",[
 X("Soapstone","Coarse grey-green high-talc rock used for stoves, sinks, carvings and lab tops.",W+"Talc",a="steatite",dt="carving, block, polished"),
 X("Trimouns talc","Talc from the Trimouns deposit near Luzenac, Ariège, France.",W+"Talc",dt="massive"),
 X("Mount Seabrook talc","Talc from Mount Seabrook, Western Australia.",W+"Talc",dt="massive"),
 X("Alpine talc","Talc from Mt Greiner, Zermatt and the Pfitschtal.",H+"talc.pdf",dt="platy masses"),
]),
K("Serpentine","Serpentine-group specimen (antigorite, lizardite, chrysotile): green to yellow carving and ornamental stones.",W+"Serpentine_group",[
 X("Bowenite","Apple-green antigorite, hardness about 5.5, used for carving and jewellery; Rhode Island state mineral.",W+"Serpentine_group",dt="carving, cabochon"),
 X("Williamsite","Oil-green antigorite with black chromite or magnetite inclusions, mainly from Maryland and Pennsylvania.",W+"Serpentine_group",dt="cabochon, bead"),
 X("Connemara marble","Green serpentinite marble from Connemara, Ireland, used as decorative stone.",W+"Serpentine_group",dt="slab, carving"),
 X("Chrysotile","Fibrous serpentine, a major asbestos mineral; handle with care.",W+"Serpentine_group",dt="fibre specimen"),
 X("Lizardite","Platy low-temperature serpentine, hardness about 2.5.",W+"Serpentine_group",dt="massive"),
 X("The Lizard serpentine","Serpentinite from The Lizard, Cornwall.",W+"Serpentine_group",dt="polished"),
]),
]
notes=("All 7 planned kinds kept. Sources: Wikipedia and HOM (muscovite, phlogopite, clinochlore, talc). HOM has no lepidolite/biotite/serpentine file used. Kämmererite and leuchtenbergite not on the fetched clinochlore page so omitted; sericite not covered. No brands or traditions.")
finish("00_12",kinds,notes)
