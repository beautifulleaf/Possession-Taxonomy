import json, os
H="https://www.handbookofmineralogy.org/pdfs/"
FE="https://www.fossilera.com/minerals-for-sale"; MF="https://www.minfind.com/search.php?cf_searcher_page=2&cform_is_valid=1&partner=10&qs=The%20Arkenstone"
HG="https://minerals.net/mineral/halite/gallery"
def X(n,d,s,a="",y="",v=None,dt=""):
    return {"n":n,"a":a,"d":d,"mk":"","y":y,"s":s,"v":[{"n":q[0],"mk":"","y":q[1],"d":q[2]} for q in (v or [])],"dt":dt}
def K(n,d,s,xs,a="",t=None):
    k={"n":n,"a":a,"d":d,"s":s,"x":xs}
    if t: k["t"]=t
    return k
F=H+"fluorite.pdf"
kinds=[
K("Fluorite","Calcium fluoride mineral specimen (crystals, clusters, octahedra, specimens on matrix, polished pieces).",FE,[
 X("Rogerley fluorite","Green fluorite cubes from the Rogerley mine, Weardale, County Durham, famous for turning purplish in sunlight (daylight fluorescence).",
   "https://gia.edu/gems-gemology/winter-2018-microworld-quarterly-crystal-bubble-in-fluorite",
   dt="twinned cubes on matrix · bright bluish-white under long-wave UV · thumbnail to cabinet"),
 X("Weardale fluorite","Fluorite from the Weardale orefield, County Durham, England.",F,dt="cubes on matrix"),
 X("Blue John","Banded purple-blue and yellowish fluorite found only under Treak Cliff, Castleton, Derbyshire.","https://en.wikipedia.org/wiki/Blue_John_(mineral)",
   a="Derbyshire Spar",y="earliest written reference 1766",
   v=[("Blue John Cavern and Treak Cliff Cavern","","still worked on a small scale, about half a ton a year"),
      ("Matthew Boulton vases","1768","sought a lease to make ormolu-mounted vases"),
      ("Treak Cliff 'lost' deposit","2013","rediscovered; a new vein followed in 2015")],
   dt="rough, polished slab, bowl, jewellery"),
 X("Cave-in-Rock fluorite","Fluorite from the Rosiclare and Cave-in-Rock district, Hardin County, Illinois.",F,dt="cubes"),
 X("Elmwood fluorite","Fluorite from the Elmwood mine, Smith County, Tennessee.",F,dt="cubes"),
 X("Berbes fluorite","Fluorite from around Berbes, Asturias, Spain.",F,dt="cubes on matrix"),
 X("Dalnegorsk fluorite","Fluorite from the Nikolaev mine, Dalnegorsk, Russia.",F,dt="crystals on matrix"),
 X("Xianghuapu fluorite","Fluorite from Xianghuapu, Hunan, China.",F,dt="crystals"),
 X("Pink octahedral fluorite","Fluorite from Mont Blanc near Chamonix and the Göscheneralp, Uri.",F,
   v=[("Mont Blanc, Chamonix, France","",""),("Göscheneralp, Uri, Switzerland","","")],dt="octahedra"),
 X("Okorusu fluorite","Fluorite from Okorusu, Namibia.",F,dt="cubes"),
 X("Nagar fluorite","Fluorite from Nagar near Karimabad, Gilgit, Pakistan.",F,dt="crystals"),
],t=["cube","octahedron","fluorescent","polished sphere or tower"]),
K("Halite","Sodium chloride mineral specimen (cubic crystals, coloured or clear).",FE,[
 X("Searles Lake pink halite","Pink hopper crystals of halite from Searles Lake, San Bernardino County, California.",HG,dt="hopper crystals · soluble: keep dry"),
 X("Blue halite","Blue halite from the potash mines of Carlsbad, New Mexico, sometimes on sylvite.",HG,
   v=[("PCA Mine, 10th Ore Zone, Carlsbad","",""),("Intrepid Potash East Mine, Carlsbad","","deep blue, crystals on sylvite")],dt="crystals, on sylvite"),
 X("Wieliczka halite","Halite cubes from the Wieliczka salt mine, Poland, known for large crystals.",H+"halite.pdf",dt="cubes on matrix"),
 X("Stassfurt halite","Classic halite cubes from Stassfurt, Saxony-Anhalt, Germany.",HG,dt="cubes"),
 X("Dead Sea halite","Halite masses and encrusting cubes from the Dead Sea.",HG,v=[("Ein Bokek, Israel","","cubes encrusting rock")],dt="mass, crust"),
],t=["cube","hopper","coloured"]),
K("Ulexite","Ulexite mineral specimen (borate; crystals, clusters or pieces, on or off matrix); species collected mainly as specimens.","https://www.irocks.com/minerals/specimen/53801",[
 X("TV stone","Polished slab of fibrous ulexite whose parallel fibres carry an image to the top surface like optical fibres.",
   "https://cs.uwaterloo.ca/~shallit/ulexite/tvstone.html",a="television stone",y="1963",
   v=[("Boron, California","","probably the most famous locality"),("Satin spar gypsum sold as ulexite","","imitation, apparently from Morocco; heavier and blurs at low angles")],
   dt="polished slab or cube · fibre orientation · beware satin spar"),
 X("Cotton-ball ulexite","Ulexite as soft rounded masses from playa and salt-marsh deposits.",H+"ulexite.pdf",
   v=[("Kramer borate deposit, Boron, Kern County","",""),("Death Valley, Inyo County","","")],dt="nodular mass"),
 X("Turkish ulexite","Ulexite from the immense Bigadiç and Kirka borate deposits, Turkey.",H+"ulexite.pdf",dt="fibrous masses"),
]),
K("Borax","Borax mineral specimen (borate; crystals, clusters or pieces, on or off matrix); species collected mainly as specimens.",MF,[
 X("California borax","Borax crystals from the borate lakes and deposits of California.",H+"borax.pdf",
   v=[("Kramer deposit, Boron, Kern County","",""),("Searles Lake","",""),("Borax Lake, Lake County","",""),("Furnace Creek, Death Valley","","")],
   dt="crystals · loses water quickly in air: keep sealed"),
 X("Tincalayu borax","Borax from the Tincalayu deposit, Salar del Hombre Muerto, Salta, Argentina.",H+"borax.pdf",dt="crystals"),
]),
K("Colemanite","Colemanite mineral specimen (borate; crystals, clusters or pieces, on or off matrix); species collected mainly as specimens.","https://www.irocks.com/minerals/specimen/39865",[
 X("Death Valley colemanite","Fine colemanite crystals from the Thompson and Boraxo mines, Furnace Creek district, Death Valley.",H+"colemanite.pdf",dt="crystals"),
 X("Calico Hills colemanite","Colemanite from Borate, Calico Hills, San Bernardino County, California.",H+"colemanite.pdf",dt="crystals"),
 X("Turkish colemanite","Large colemanite crystals from Bigadiç (Balıkesir) and Mustafakemalpaşa (Bursa), Turkey.",H+"colemanite.pdf",dt="large crystals"),
]),
K("Painite","Painite mineral specimen (borate; crystals, clusters or pieces, on or off matrix); species collected mainly as specimens.",MF,[
 X("Mogok painite","Orange-red to brownish-red borate from gem gravels near Mogok, Myanmar; once among the rarest minerals known.","https://en.wikipedia.org/wiki/Painite",y="1957",
   v=[("Type material, near Ohngaing, Sagaing, Mogok district","1957","described as a new mineral; named for Arthur C. D. Pain"),
      ("New Mogok occurrences","","yielded several thousand specimens")],dt="single crystal, on matrix with corundum · pleochroic"),
]),
K("Jeremejevite","Jeremejevite mineral specimen (borate; crystals, clusters or pieces, on or off matrix); species collected mainly as specimens.",MF,[
 X("Namibian jeremejevite","Blue gem crystals of jeremejevite from Namibia.",H+"jeremejevite.pdf",
   v=[("Prospect near Cape Cross","",""),("Mile 72, north of Swakopmund","",""),("Ameib, Erongo Mountains","","")],dt="crystals, colourless to blue"),
 X("Mt Soktui jeremejevite","Large jeremejevite crystals from the type area, Mt Soktui, Nerchinsk district, Siberia.",H+"jeremejevite.pdf",dt="large crystals"),
 X("Eifel jeremejevite","Jeremejevite from Wannerköpfe and Emmelberg near Üdersdorf, Eifel, Germany.",H+"jeremejevite.pdf",dt="crystals"),
]),
]
notes=("Seven old kinds kept one-to-one. Archetypes from the Handbook of Mineralogy distribution lists (PDF text via pdftotext), minerals.net halite gallery, GIA (Rogerley), "
 "Wikipedia (Blue John, Painite) and a University of Waterloo TV-stone page. Blue John is an archetype under Fluorite. No makers, so no brands; no craft tradition recorded "
 "(Blue John working is a candidate tradition but no source on the craft itself was fetched).")
p="work/F6/shelves/00_03.json"; json.dump({"kinds":kinds,"brands":[],"traditions":[],"notes":notes},open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
