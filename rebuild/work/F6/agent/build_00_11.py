from libf6a import *
kinds=[
K("Labradorite","Plagioclase feldspar mineral specimen showing labradorescence, a blue-green-gold iridescent schiller; sold as rough, slabs and cabochons.",W+"Labradorite",[
 X("Spectrolite","Highly iridescent labradorite from Ylämaa, Finland, showing pink, orange and purple flashes; the name is a brand name for Finnish material.",W+"Labradorite",y="1940",
   v=[("Ylämaa deposit found by Pekka Laitakari","1940",""),("First Ylämaa workshop cutting spectrolite for jewellery","1973","")],dt="polished slab, cabochon, sphere"),
 X("Labrador labradorite","Type-area labradorite from Paul's Island near Nain, Labrador, Canada.",W+"Labradorite",dt="slab, tumbled stone"),
 X("Madagascan labradorite","Major source of mainly blue-grey-green labradorite.",W+"Labradorite",dt="slab, cabochon"),
],t=["flash colour (blue, gold, multi-colour)","polished slab","tumbled"]),
K("Microcline","Potassium feldspar mineral specimen: white to cream crystals, the green variety being amazonite.",W+"Microcline",[
 X("Amazonite","Green microcline; despite the name it is not found in the Amazon Basin.",W+"Microcline",dt="crystals, tumbled, cabochon"),
 X("Perthite","Microcline or orthoclase with thin exsolved albite layers.",W+"Microcline",dt="polished slab"),
 X("Alpine and Baveno microcline","Microcline from St Gotthard, Mt Greiner (Zillertal) and Baveno, Piedmont.",H+"microcline.pdf",dt="crystals"),
 X("Pikes Peak microcline","Microcline from the Pikes Peak area and Crystal Peak, Colorado.",H+"microcline.pdf",dt="crystals with smoky quartz"),
 X("Ilmen microcline","Microcline from the Ilmen Mountains, Urals.",H+"microcline.pdf",dt="crystals"),
]),
K("Orthoclase","Potassium feldspar mineral specimen: Carlsbad-twinned crystals; adularia and moonstone are gem varieties.",W+"Orthoclase",[
 X("Adularia","Low-temperature feldspar first reported from the Adula Alps, Switzerland, described by Pini in 1781.",W+"Orthoclase",y="1781",dt="clear crystals · adularescence"),
 X("Moonstone","Gem intergrowth of orthoclase and albite showing adularescence.",W+"Orthoclase",dt="rough, cabochon"),
 X("Sanidine","Higher-temperature polymorph in rapidly cooled volcanic rocks.",W+"Orthoclase",dt="phenocrysts"),
 X("Carlsbad twin","Typical twinning of orthoclase; classic Carlsbad (Bohemia) crystals.",H+"orthoclase.pdf",dt="twinned crystals"),
 X("Madagascan gem orthoclase","Gem crystals from Ampandrandava and Itrongay, Madagascar.",H+"orthoclase.pdf",dt="yellow gem crystals"),
]),
K("Albite","Sodium feldspar mineral specimen: white, striated crystals and platy cleavelandite.",W+"Albite",[
 X("Cleavelandite","Platy, bladed albite from granitic pegmatites.",W+"Albite",dt="blades, rosettes"),
 X("Belomorite","Iridescent albite from the White Sea coast, identified in 1925 by Alexander Fersman.",W+"Albite",y="1925",dt="polished"),
 X("Alpine albite","Albite from St Gotthard, Tavetsch, Roc Tournée (Savoie) and Mt Greiner.",H+"albite.pdf",dt="crystals"),
 X("Pala albite","Albite from the Pala and Mesa Grande districts, San Diego County.",H+"albite.pdf",dt="cleavelandite with tourmaline"),
]),
K("Lapis lazuli and lazurite","Deep blue metamorphic rock of lazurite with calcite and pyrite, and the feldspathoid lazurite itself; rough, cabochons and carvings.",W+"Lapis_lazuli",[
 X("Sar-e-Sang lapis","Lapis from the Sar-i Sang mines in the Kokcha valley, Badakhshan, Afghanistan, worked for more than 6,000 years.",W+"Lapis_lazuli",
   v=[("Tutankhamun's funeral mask","1341–1323 BC","lapis used in the mask")],dt="rough, cabochon, carving"),
 X("Chilean lapis","Lapis from Ovalle, Chile, paler and often with calcite.",W+"Lapis_lazuli",dt="rough, cabochon"),
 X("Baikal lapis","Lapis from the Tultui deposit west of Lake Baikal, Russia.",W+"Lapis_lazuli",dt="rough"),
 X("Ultramarine","Pigment from ground lapis used in Renaissance and Baroque painting until synthetic ultramarine replaced it in the early 19th century.",W+"Lapis_lazuli",dt="pigment"),
 X("Lazurite crystals","Well-crystallised lazurite from Sar-e-Sang and Slyudyanka, Lake Baikal.",H+"lazurite.pdf",dt="dodecahedral crystals"),
],t=["lapis lazuli rock","lazurite crystal"]),
K("Sodalite","Sodium aluminium silicate chloride mineral specimen: royal blue masses with white veins; hackmanite changes colour in light.",W+"Sodalite",[
 X("Bancroft sodalite","Blue sodalite from the Princess Sodalite Mine, Bancroft, Ontario.",W+"Sodalite",dt="rough, cabochon, beads"),
 X("Hackmanite","Tenebrescent sodalite: violet when freshly quarried at Mont Saint-Hilaire and Greenland and fading to grey; Afghan and Myanmar material turns violet to pink-red in sunlight.",W+"Sodalite",dt="crystals · tenebrescence"),
 X("Ilimaussaq sodalite","Type-locality sodalite from the Ilimaussaq intrusion, Greenland, first described in 1811.",W+"Sodalite",y="1811",dt="crystals"),
 X("Namibian sodalite","Transparent sodalite crystals from northern Namibia.",W+"Sodalite",dt="transparent crystals"),
 X("Brazilian sodalite","Smaller deposits in Brazil.",W+"Sodalite",dt="rough"),
]),
K("Haüyne","Sodium calcium aluminium silicate sulfate mineral specimen: bright blue grains and rare gem crystals from volcanic rocks.",W+"Haüyne",[
 X("Laacher See haüyne","Blue haüyne in ejected hornblende-haüyne-scapolite rock from the Laacher See complex, Eifel, Germany.",W+"Haüyne",dt="blue grains in rock"),
 X("Lake Nemi haüyne","Type-locality haüyne from Lake Nemi, Alban Hills, Italy; named by Brunn-Neergard in 1807.",W+"Haüyne",y="1807",dt="grains"),
 X("Monte Somma haüyne","Haüyne from Monte Somma and Vesuvius lavas.",H+"hauyne.pdf",dt="crystals"),
 X("Gem haüyne","Rare faceted blue haüyne.",W+"Haüyne",dt="faceted"),
]),
]
notes=("All 7 planned kinds kept (kind 'Lapis lazuli and lazurite' covers both rock and mineral). Sources: Wikipedia and HOM (microcline, orthoclase, albite, lazurite, sodalite, hauyne). "
 "Not on fetched pages and omitted: Pikes Peak amazonite colour cause, peristerite, moonstone localities. No brands or traditions.")
finish("00_11",kinds,notes)
