import json,os
W='https://en.wikipedia.org/wiki/'
CS='https://cornerstone-edsupply.com/collections/geology/products/40_complete-rock-collection'
FE='https://www.fossilera.com/minerals-for-sale'
def x(n,d,s,y='',v=None,dt='',a=''):
    return {"n":n,"a":a,"d":d,"mk":"","y":y,"s":W+s,"v":v or [],"dt":dt}
def v(n,d,y=''): return {"n":n,"mk":"","y":y,"d":d}
kinds=[
{"n":"Granite","d":"Coarse-grained intrusive igneous rock sample.","s":CS,"t":["polished slab","hand specimen"],
 "x":[x("Orbicular granite","Granite holding concentric spherical orbicules; rare and prized as a display stone.","Orbicular_granite","",[v("Caldera, Chile","protected site, Jurassic body"),v("Kuru and Savitaipale, Finland","Finland holds about a third of known occurrences"),v("Mount Magnet, Western Australia","")],"polished slab · cut orbicule"),
      x("Luxullianite","Rare Cornish tourmalinised granite with radial tourmaline needles.","Luxullianite","",[v("Luxulyan, Cornwall","used in the Duke of Wellington's tomb")],"polished slab"),
      x("Rapakivi granite","Granite with feldspar ovoids rimmed by a second feldspar.","Granite","",[],"slab")],
 "m":[["K2 Granite",""]]},
{"n":"Basalt","d":"Fine-grained extrusive igneous rock sample.","s":CS,"t":["columnar basalt","vesicular basalt"],
 "x":[x("Columnar basalt","Basalt cooled into polygonal prisms; collected as column sections.","Basalt","",[v("Giant's Causeway, Northern Ireland","classic columnar site")],"hexagonal prism · length")]},
{"n":"Obsidian","d":"Natural volcanic glass sample.","s":CS,"t":["black obsidian","arrowhead blank"],
 "x":[x("Snowflake obsidian","Black obsidian with white cristobalite spherulites.","Obsidian","",[],"cabochon · tumbled · raw"),
      x("Rainbow obsidian","Banded Mexican obsidian coloured by hedenbergite nanorods.","Obsidian","",[],"cabochon · sphere"),
      x("Fire obsidian","Obsidian with iridescent magnetite nanoparticle sheen.","Obsidian","",[],"cabochon"),
      x("Sheen obsidian","Obsidian with a golden sheen from aligned gas bubbles.","Obsidian","",[],"cabochon · sphere"),
      x("Apache tears","Small rounded dark obsidian nodules (marekanite), often in perlite.","Apache_tears","",[v("Arizona and western Nevada","widely collected")],"tumbled · raw nodule","marekanite")]},
{"n":"Rhyolite","a":"rainforest jasper · wonderstone","d":"Fine-grained silica-rich extrusive igneous rock sample, including decorative spherulitic types.","s":FE,"t":["spherulitic rhyolite","rhyolitic tuff"]},
{"n":"Porphyry","a":"Chinese writing stone","d":"Igneous rock sample with large crystals in a fine-grained groundmass (e.g. Chinese writing stone).","s":FE,
 "x":[x("Imperial porphyry","Deep purple-red porphyry with plagioclase crystals, quarried in Roman Egypt for imperial monuments.","Porphyry_(geology)","Roman period",[v("Mons Porphyrites, Eastern Desert, Egypt","only source")],"polished piece"),
      x("Green porphyry","Greek green porphyry (lapis Lacedaemonius), now classed as serpentine.","Porphyry_(geology)","Roman period",[],"polished piece")]},
{"n":"Sandstone","d":"Sedimentary rock sample of cemented sand grains.","s":CS,
 "x":[x("Navajo Sandstone","Wind-deposited Colorado Plateau sandstone, the rock of Zion and Arches; source of Moqui Marbles.","Navajo_Sandstone","Early Jurassic",[v("Southern Utah","Zion, Arches, Capitol Reef")],"slab · hand specimen")],
 "m":[["Picture Sandstone",""]]},
{"n":"Limestone","a":"fossiliferous limestone · oolite","d":"Sedimentary carbonate rock sample, plain or fossil-bearing, often sold polished.","t":["fossiliferous","oolitic","travertine","chalk"],"s":W+"Limestone",
 "x":[x("Fossiliferous limestone","Limestone with conspicuous shells, crinoids or corals; polished slabs and tiles.","Fossiliferous_limestone","",[v("Solnhofen Plattenkalk, Germany",""),v("Indiana Limestone, USA","")],"polished slab · crinoidal · coralline")]},
{"n":"Marble","d":"Metamorphic rock sample of recrystallised carbonate.","s":CS,
 "x":[x("Carrara marble","White or blue-grey Tuscan marble, the sculptor's stone since Roman times.","Carrara_marble","Roman period",[v("Statuario","pure white, now exhausted"),v("Bianco Carrara","most common commercial grade"),v("Calacatta","exotic veined variety")],"slab · block · polished"),
      x("Parian marble","Pure white fine-grained marble from Paros, Greece.","Marble","",[],"slab")],
 "m":[["Picasso Marble",""]]},
{"n":"Slate","d":"Fine-grained foliated metamorphic rock sample.","s":CS,"t":["writing slate","roofing slate"]},
{"n":"Fulgurite","d":"Natural tube or crust of silica glass fused by lightning in sand or rock.","s":FE,"t":["sand fulgurite","rock fulgurite","soil fulgurite"],
 "x":[x("Sand fulgurite","Type I tube of fused quartz sand; the classic collector fulgurite.","Fulgurite","",[v("Sahara (Niger)","documented studies"),v("Drigg, Cumberland","tubes to 9.1 m recorded by Darwin")],"length · diameter · tube or crust"),
      x("Winans Lake fulgurite","Michigan site with the largest reported fulgurite mass, about 4.88 m long.","Fulgurite","",[],"section")]},
{"n":"Geode and thunder egg","a":"thunderegg · nodule","d":"Hollow geode or solid-centred thunder egg, sold whole or cut and polished.","t":["amethyst geode","agate geode","cut half"],"s":W+"Geode",
 "x":[x("Brazilian amethyst geode","Amethyst-lined geode from basalt of the Paraná traps in Brazil and Uruguay.","Geode","",[],"cut half · cathedral · size"),
      x("Oregon thunderegg","Rhyolite-hosted nodule with agate or chalcedony core; Oregon's state rock since 1965.","Thunderegg","state rock 1965",[v("Crook, Jefferson, Malheur, Wasco and Wheeler counties","")],"whole · cut half · polished"),
      x("Mendip potato stone","Geodes of the Mendip Hills, Somerset.","Geode","",[],"cut half")]},
{"n":"Septarian nodule","a":"septarian concretion · dragon stone","d":"Calcite-cemented concretion cracked into septa and filled with calcite, polished as ornaments.","s":W+"Septarian_nodule",
 "x":[x("Moeraki Boulders","Septarian concretions up to about 3 m on the New Zealand coast.","Septarian_nodule","",[v("Moeraki, South Island","Paleocene mudstone")],"in situ; not collected"),
      x("Moqui Marbles","Iron oxide concretions eroding from Navajo Sandstone in Utah.","Septarian_nodule","",[],"pair · cluster")]},
{"n":"Rock and mineral teaching set","d":"Kit of different labelled specimens (rocks, and minerals or fossils) sold as one standard set, usually for teaching. A mixed set not sold as a teaching kit goes with its most valuable item.","s":CS,"t":["rock set","mineral set","fossil set"]}]
json.dump({"kinds":kinds,"brands":[],"traditions":[],"notes":"Rainforest jasper and wonderstone kept as aliases of Rhyolite (not on retrieved rhyolite page, so no archetype). Larvikite, snowflake obsidian localities, mahogany obsidian, Picasso marble, picture sandstone, Coconino, Paesina and Madagascar septarian not confirmed on retrieved pages; Picasso and Picture kept as flat models from old data. Moqui Marbles cited via the Septarian nodule/concretion page. Teaching-set brands not sourced."},open('work/F6/shelves/04_00.tmp','w'),ensure_ascii=False,indent=1)
os.rename('work/F6/shelves/04_00.tmp','work/F6/shelves/04_00.json')
