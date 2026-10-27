import json, os
W="https://en.wikipedia.org/wiki/"
def X(n,d,s,a="",y="",v=None,dt="",mk=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[{"n":q[0],"mk":"","y":q[1],"d":q[2]} for q in (v or [])],"dt":dt}
GG="https://www.minerals.net/mineral/gold/gallery"; NS=W+"Native_silver"; NC=W+"Native_copper"
BI="https://minerals.net/Image/10/32/Bismuth.aspx"; SU="https://www.minerals.net/mineral/sulfur/gallery"
gold={"n":"Native gold","a":"gold specimen · gold nugget",
 "d":"Native gold sold as a mineral specimen: nugget, crystal, leaf or wire, on or off matrix. A refined bar, round or coin sold by weight is in Coins, Stamps, Medals & Trading Cards.",
 "t":["on matrix","in quartz","loose"],"s":W+"Native_gold","x":[
 X("Gold nugget","Naturally occurring lump of native gold, usually from placer deposits.",W+"Gold_nugget",
   v=[("Welcome Stranger, Moliagul, Victoria","1869","about 71 kg net; widely held the largest ever found"),
      ("Welcome Nugget, Bakery Hill, Ballarat","1858","69 kg"),
      ("Sierra Buttes, California","1869","largest California nugget, 49.5 kg"),
      ("Hand of Faith, Kingower, Victoria","1980","27.2 kg; largest found with a metal detector"),
      ("Canaã nugget, Serra Pelada, Brazil","1983","60.8 kg; largest surviving nugget")],
   dt="grain, flake, nugget · water-worn or crystalline · purity varies by region"),
 X("Crystallised gold","Gold in distinct crystals: octahedra, skeletal or cuboctahedral forms, often in quartz.",GG,
   v=[("Mount Kare, Papua New Guinea","","octahedrons"),("Icabaru, Bolívar, Venezuela","","skeletal crystals"),
      ("Mockingbird Mine, Mariposa County, California","","crystals in quartz"),("Pontes e Lacerda, Mato Grosso, Brazil","","crystal clusters"),
      ("Windy Point Mine, Humboldt County, Nevada","","")],
   dt="thumbnail to cabinet · on quartz or loose · crystal sharpness and lustre"),
 X("Leaf gold","Thin natural sheets of flattened gold crystals.","https://sothebys.com/en/buy/auction/2021/natural-history-2/crystalline-gold",
   v=[("Round Mountain Mine, Nye County, Nevada","mid-1990s–","the most prolific source of crystalline gold specimens for nearly 20 years; wavy leaves with cuboctahedral crystals"),
      ("El Dorado County, California","","")],dt="leaf or sheet · loose or on matrix"),
 X("Dendritic gold","Branching, tree-like growths of gold crystals.",GG,v=[("Eagle's Nest Mine, Placer County, California","","dendritic gold, also on quartz")],dt="dendrite on quartz or loose"),
 X("Wire gold","Gold in thin wires or curved wire crystals.",GG,
   v=[("Olinghouse Mine, Washoe County, Nevada","","wires and crystals on matrix"),("Ibex Mine, Lake County, Colorado","","wire mass"),("Chocó District, Colombia","","curved wire crystal")],dt="wire on matrix or loose"),
 X("Electrum","Native gold with more than 20% silver, golden-silvery to silvery in colour.",W+"Native_gold",dt="nugget or grain · silver content sets colour"),
]}
silver={"n":"Native silver","a":"wire silver",
 "d":"Native silver mineral specimen (wires, crystals, sheets, on or off matrix).","t":["on matrix","loose"],"s":NS,"x":[
 X("Kongsberg wire silver","Thick curved wires of native silver from the Kongsberg mines, Norway, the benchmark for wire silver.",NS,y="1623–1958",
   v=[("Kongsberg, Norway","1623–1958","mining period")],dt="thick filiform wire · tarnishes dark grey to black"),
 X("Imiter silver","Lustrous, sharply crystallised, heavily twinned silver from Imiter, Morocco, often with acanthite or chlorite.",NS,
   dt="crystal groups and wires · on acanthite"),
 X("Herringbone silver","Dendritic silver in herringbone patterns set in white calcite.",NS,v=[("Batopilas, Mexico","","")],dt="dendrites in calcite"),
 X("Freiberg silver","Dendritic and arborescent silver with proustite and stephanite from Saxony.",NS,
   v=[("Freiberg, Saxony, Germany","",""),("Himmelsfürst mine, Germany","","wire and rope silver")],dt="arborescent, wire, rope"),
 X("Slab silver","Large slabs of native silver intergrown with arsenides.",NS,v=[("Cobalt, Ontario, Canada","1903","discovered 1903")],dt="slab, polished section"),
 X("Silver amalgam","High-mercury natural silver.",NS,dt="crystals or masses"),
]}
copper={"n":"Native copper","a":"",
 "d":"Native copper mineral specimen (arborescent, crystalline or sheet copper, on or off matrix).","t":["crystallised","arborescent","massive","float copper"],"s":NC,"x":[
 X("Keweenaw copper","Native copper from the basalt-hosted deposits of Michigan's Keweenaw Peninsula, the world's largest native copper deposits.",NC,y="1840s–",
   v=[("Keweenaw Peninsula mines, Michigan","1840s","first commercial mines"),("Isle Royale, Lake Superior","",""),
      ("Ontonagon Boulder","","glacier-carried mass, held by the Smithsonian")],dt="crystals, masses, sheets · on or off matrix"),
 X("Halfbreed copper","Copper-silver nugget with native silver alongside copper.",NC,v=[("Keweenaw County, Michigan","","")],dt="nugget, polished face"),
 X("Dendritic copper","Branching, tree-like native copper.",NC,
   v=[("Itauz Mine, Kazakhstan","",""),("Mission Mine, Arizona","","encased in gypsum"),("Broken Hill, New South Wales","","covered in verdigris"),("Ray Mine, Arizona","","")],
   dt="arborescent spray · bright or patinated"),
 X("Coro Coro copper","Native copper from the major deposit at Coro Coro, Bolivia.",NC,dt=""),
 X("Tsumeb copper","Native copper from Tsumeb, Namibia.",NC,dt=""),
]}
plat={"n":"Native platinum","a":"platinum nugget",
 "d":"Native platinum mineral specimen (crystal, nugget or grain, on or off matrix).","s":"https://www.irocks.com/minerals/specimen/54195","x":[
 X("Platinum nugget","Placer nugget of native platinum; nuggets of this size are rare.","https://hyperphysics.gsu.edu/hbase/minerals/platinum.html",
   v=[("Nizhniy Tagil, Urals, Russia","","444.4 g nugget, about 5 cm, Smithsonian"),("Chocó, Colombia","","536.7 g nugget, about 5 cm, Smithsonian")],dt="grain to nugget"),
 X("Kondyor platinum","Alluvial platinum from the ring-shaped Kondyor Massif, Khabarovsk Krai, Russia.",W+"Kondyor_Massif",y="1984–",
   v=[("Artel Starateley 'Amur'","1984","has worked the deposit since 1984")],dt="crystals and nuggets"),
]}
bis={"n":"Native bismuth","a":"bismuth crystal",
 "d":"Bismuth specimen: natural native bismuth, or the iridescent lab-grown hopper crystals sold widely, which are not natural.",
 "t":["natural","lab-grown hopper crystal"],"s":"https://earthwonders.com/specimens/67646","x":[
 X("Lab-grown hopper bismuth","Stepped, iridescent hopper crystals grown from molten bismuth; synthetic, not a mineral specimen.",BI,dt="hopper staircase · oxide-film colours"),
 X("Saxony bismuth","Native bismuth from the Erzgebirge, Saxony.",BI,
   v=[("Schneeberg, Erzgebirge, Germany","","typical native and dendritic forms"),("Pohla-Tellerhäuser Mine, Saxony","","large crystal cluster")],dt="dendritic, platy, crystals"),
 X("Bolivian bismuth","Native bismuth from Potosí Department, Bolivia.",BI,
   v=[("Huallatani Mine","","lustrous crystals"),("Chorolque Mine","","rounded nugget")],dt="crystals, nuggets"),
 X("Kingsgate bismuth","Masses of bismuth crystals from Kingsgate, Glen Innes, New South Wales.",BI,dt="crystal mass"),
]}
sul={"n":"Sulfur","a":"sulphur · native sulfur",
 "d":"Native sulfur mineral specimen (yellow crystals and clusters, on or off matrix).","s":"https://www.fossilera.com/minerals-for-sale","x":[
 X("Sicilian sulfur","Classic bright yellow sulfur crystals from the Agrigento (Girgenti) mines of Sicily, often on aragonite.",SU,
   v=[("Girgenti / Agrigento District","","crystals, some with bitumen, on aragonite"),("Racalmuto","","sharp crystals on matrix"),("Cozzodizi","","well-formed single crystals")],
   dt="single crystal to cabinet cluster · on aragonite matrix"),
 X("El Desierto sulfur","Dense clusters and hollow crystals of sulfur from the El Desierto Mine, San Pablo de Napa, Potosí, Bolivia.",SU,dt="cluster, hollow crystal"),
 X("Maybee sulfur","Pyramidal sulfur crystals from the quarries of Maybee, Monroe County, Michigan.",SU,v=[("Scofield Quarry","","")],dt="pyramidal crystals"),
 X("Perticara sulfur","Sulfur crystals from the Perticara Mine, Pesaro-Urbino, Italy.",SU,dt="single crystal"),
 X("Machów sulfur","Small rounded sulfur crystals from the Machów Mine, Tarnobrzeg, Poland.",SU,dt="small crystals"),
 X("Volcanic sulfur","Sulfur deposited at volcanic vents.",SU,v=[("Kilauea, Hawaii","",""),("Steamboat Springs, Nevada","","dipyramidal hopper crystal")],dt="crusts, hopper crystals"),
]}
notes=("Six old kinds kept one-to-one. Archetypes = classic habit/locality types sourced from Wikipedia (Gold nugget, Native gold, Native silver, Native copper, Kondyor Massif), "
 "minerals.net galleries, Sotheby's and HyperPhysics. Bismuth separates lab-grown hopper crystals (type and archetype) from natural bismuth. "
 "Left out: Eagle's Nest production years (NMT abstract returned 503), Kongsbergite and Urals isoferroplatinum not attested on fetched pages. No brands or traditions apply.")
out={"kinds":[gold,silver,copper,plat,bis,sul],"brands":[],"traditions":[],"notes":notes}
p="work/F6/shelves/00_01.json"; json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
