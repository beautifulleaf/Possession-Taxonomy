import sys; sys.path.insert(0,'work/F6/agent')
from lib import *
P=W+"Pearl"
kinds=[
K("Pearl","Loose undrilled pearl, natural or cultured, differing by the water it grew in, with size, shape and colour as options.","",[
 X("Natural Gulf pearl","Pearl from wild oysters fished in the Persian Gulf off Bahrain, praised by Pliny; extremely rare and found only by opening many shells.",P,a="natural pearl",
   dt="no nucleus · lab report needed to prove natural origin"),
 X("Akoya pearl","Saltwater cultured pearl from Pinctada fucata in Japan and China, typically 2–10 mm; large-scale cultivation began in the early twentieth century.",P,
   mk="Mikimoto",y="early 20th century",v=[("Nishikawa pearl-culture patent","1916","Granted to Tokichi Nishikawa; Mikimoto used the technology")],dt="2–10 mm · lustre most important · white to cream"),
 X("South Sea pearl","The largest and rarest cultured pearls, from the Pinctada maxima oyster, farmed off north-western Australia.",P,mk="Paspaley",
   dt="large · white to golden"),
 X("Tahitian pearl","Black cultured pearl from Pinctada margaritifera in Tahiti and other Pacific islands, one pearl nucleated at a time.",W+"Tahitian_pearl",a="black pearl",
   dt="dark body colours · one nucleus per oyster"),
 X("Freshwater cultured pearl","Pearl grown in freshwater mussels; cultivation began in Lake Biwa in 1914 and China is now the commercial producer.",W+"Cultured_freshwater_pearls",y="1914",
   dt="tissue-nucleated · many shapes · sorted by A grades for shape, lustre, surface, colour, matching"),
 X("Keshi pearl","Pearl composed entirely of nacre, formed when mantle tissue slips off the bead during culturing; small and irregular.",W+"Keshi_pearl",dt="all nacre · small"),
 X("Baroque pearl","Cultured or natural pearl of highly irregular shape, valued for individuality.",W+"Baroque_pearl",dt="irregular shapes"),
 X("Conch and melo pearl","Rare non-nacreous natural pearls from the queen conch (often pink with a flame pattern) and from the Melo bailer shell.",P,a="conch pearl · melo pearl",
   dt="no nacre · flame pattern · lacks the lustre of nacreous pearls"),
 ],t=["Saltwater pearl","Freshwater pearl","Natural","Cultured"]),
K("Precious coral","Red and pink coral skeleton of the genus Corallium, worked as beads and cabochons.",W+"Precious_coral",[
 X("Mediterranean red coral","Corallium rubrum, the first described species, from the Mediterranean and Atlantic coasts, including the caves of Alghero in Sardinia.",W+"Precious_coral",
   a="Sardinian coral",dt="pale pink to deep red · cabochons and beads · Mohs 3.5"),
 X("Pacific Corallium","Other Corallium species from the western Pacific around Japan and Taiwan, at depths of 350 to 1,500 m.",W+"Precious_coral",dt="the genus has 31 species"),
 X("Torre del Greco coral","Coral worked in Torre del Greco near Naples, which set up a coral society in 1790 and its first factory in 1805.",W+"Precious_coral",y="1790",dt="Victorian-era jewellery centre"),
 ]),
K("Jet","Black lignite gem material cut and polished for jewellery, best known as Whitby jet.",W+"Jet_(gemstone)",[
 X("Whitby jet","Jet from the Jet Rock near Whitby, England, about 181 million years old, made fashionable for Victorian mourning jewellery.",W+"Jet_(gemstone)",
   y="1850s",v=[("Queen Victoria's mourning","1850s","Fashion began after she wore it in mourning; Whitby production peaked in the early 1870s")],dt="warm to touch · brown streak on porcelain"),
 X("Spanish (Asturian) jet","Jet from northern Spain, about 155 million years old, worked at Santiago de Compostela into pilgrims' amulets.",W+"Jet_(gemstone)",dt="religious objects and amulets"),
 X("Acoma jet","Jet used by Navajo and Pueblo peoples in New Mexico.",W+"Jet_(gemstone)",dt="Southwestern United States"),
 X("Jet imitations","French jet or Vauxhall glass, ebonite (vulcanite), anthracite and bog oak, sold as jet at its peak.",W+"Jet_(gemstone)",a="French jet · vulcanite",dt="glass feels cool; ebonite fades"),
 ]),
]
brands=[
 B("Mikimoto","Japan","",  "Premium","cultured pearls","Pearl jeweller founded by Kokichi Mikimoto, who used pearl-culture technology patented by Nishikawa in 1916.",W+"Kokichi_Mikimoto"),
 B("Paspaley","Australia","","Premium","South Sea pearls","Major producer of South Sea pearls off north-western Australia.",P),
]
save("01_02",kinds,brands,"Old 'Loose pearl' became Pearl; old models Akoya, South Sea and Tahitian pearl became archetypes. CITES note left out (no retrieved page). Edison pearls omitted (page does not cover them, no source). Amber stays in Fossils. Gem labs are in shelf 01_00.")
