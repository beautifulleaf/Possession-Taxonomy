import json,os
W='https://en.wikipedia.org/wiki/'
def V(n,mk="",y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
DS=W+"David_Smith_(sculptor)"; EM=W+"Early_One_Morning_(Caro)"; RS=W+"Richard_Serra"; AC=W+"Alexander_Calder"; KA=W+"Kinetic_art"
kinds=[
 {"n":"Steel and iron sculpture","a":"welded steel sculpture · Corten sculpture","d":"Steel, iron or other ferrous metal welded, forged, cut or bent to form.",
  "t":["welded steel","stainless steel","weathering (Corten) steel","rolled steel plate","cast iron","painted steel","indoor maquette","outdoor edition"],
  "s":"https://www.singulart.com/en/sculpture",
  "x":[
   {"n":"David Smith welded-steel series","a":"Cubi · Agricola · Forgings","d":"Welded abstract steel sculpture built with a torch rather than cast in bronze, in numbered series.","mk":"David Smith","y":"1951–1965","s":DS,
    "v":[V("Agricolas","David Smith","1951–59"),V("Forgings (eleven)","David Smith","1955–56"),V("Voltri-Bolton works","David Smith","1962–63"),V("Cubi series (28 stainless-steel pieces)","David Smith","1961–65","Cubi XXVIII sold for $23.8 million in 2005")],
    "dt":"series · finish (burnished stainless) · scale · museum-held vs market"},
   {"n":"Caro painted-steel table piece","a":"Early One Morning","d":"Anthony Caro's floor-standing abstract assemblage of painted metal, shown with no plinth.","mk":"Anthony Caro","y":"1962","s":EM,
    "v":[V("Early One Morning","Anthony Caro","1962","metal painted red; Tate since 1965")],
    "dt":"painted colour · parts welded or bolted · plinth-free display"},
   {"n":"Serra torqued ellipse","a":"Corten steel plate sculpture","d":"Richard Serra's large rolled and weathering-steel plate works, from prop pieces to torqued ellipses.","mk":"Richard Serra","y":"1969–2005","s":RS,
    "v":[V("One Ton Prop: House of Cards","Richard Serra","1969","four lead plates"),V("Tilted Arc","Richard Serra","1981","COR-TEN, 120 ft long; removed 1989"),V("Torqued Ellipses (seven) and Double Torqued Ellipses (four)","Richard Serra","1996–2004","rolled steel"),V("The Matter of Time","Richard Serra","2005","eight COR-TEN torqued-ellipse pieces, Guggenheim Bilbao")],
    "dt":"plate thickness · rust finish · installation site · museum scale"}]},
 {"n":"Mobile and kinetic sculpture","a":"mobile · stabile · kinetic art · wind sculpture","d":"A sculpture that moves, driven by air, motors, water or the viewer.",
  "t":["hanging mobile","standing mobile","stabile","motorised sculpture","wind-driven stainless steel","table-top maquette","edition"],
  "s":KA,
  "x":[
   {"n":"Calder mobile","a":"hanging mobile · standing mobile","d":"Alexander Calder's balanced abstract sculpture of hanging shapes moved by air; the term is Duchamp's, 1931.","mk":"Alexander Calder","y":"1931–1976","s":AC,
    "v":[V("Motorised abstract sculptures named 'mobiles'","Alexander Calder","1931","named by Marcel Duchamp"),V("Hanging mobiles moved by touch or air","Alexander Calder","1932"),V("Outdoor standing mobiles","Alexander Calder","1934")],
    "dt":"wire and sheet metal · colour · scale · Calder Foundation examination for authenticity"},
   {"n":"Calder stabile","a":"stationary Calder","d":"A self-supporting static abstract sculpture, term coined by Jean Arp in 1932, usually painted steel plate.","mk":"Alexander Calder","y":"1932 onward","s":AC,
    "v":[V("First stabiles named by Arp","Alexander Calder","1932")],
    "dt":"steel plate · 'Calder red' · size · maquette vs monumental · initialled at foundry"},
   {"n":"Tinguely machine sculpture","a":"motorised junk sculpture","d":"Jean Tinguely's motor-driven machines of salvaged parts.","mk":"Jean Tinguely","y":"1950s–1960","s":W+"Homage_to_New_York",
    "v":[V("Homage to New York","Jean Tinguely","1960","self-destroyed at MoMA, 17 March")],
    "dt":"found parts · motor · working order · survives or destroyed"},
   {"n":"Rickey wind sculpture","a":"kinetic stainless-steel sculpture","d":"George Rickey's geometric stainless-steel forms that move in the wind.","mk":"George Rickey","y":"1960s–1990s","s":W+"George_Rickey",
    "v":[V("Four Squares in Square Arrangement (Vier Vierecke im Geviert)","George Rickey","1969","Neue Nationalgalerie, Berlin"),V("Two Plane Vertical Horizontal Variation III","George Rickey","1973","Seattle"),V("Two Open Triangles Up Gyratory","George Rickey","1982","stainless steel"),V("Breaking Column","George Rickey","1988","stainless steel")],
    "dt":"series · bearing · edition · outdoor wear"}]},
 {"n":"Found-object sculpture","a":"assemblage","d":"A sculpture assembled from found, salvaged or discarded objects, or from several materials none of which governs.",
  "t":["box assemblage","wall assemblage","free-standing assemblage","readymade"],
  "s":"https://www.artsper.com/en-gb/contemporary-artworks/sculpture/assemblage",
  "x":[
   {"n":"Cornell shadow box","a":"Joseph Cornell box","d":"Joseph Cornell's glazed boxes of found objects, often handled and interactive.","mk":"Joseph Cornell","y":"1930s–1960s","s":W+"Joseph_Cornell",
    "v":[V("Medici Slot Machine boxes","Joseph Cornell"),V("Soap Bubble Sets","Joseph Cornell"),V("Hotel boxes","Joseph Cornell"),V("Aviary series","Joseph Cornell"),V("Space Object Boxes","Joseph Cornell")],
    "dt":"series · contents · glazing · estate provenance"},
   {"n":"Nevelson wooden wall","a":"Nevelson relief","d":"Louise Nevelson's wall-sized assemblages of boxes holding scraps, painted one colour, usually black.","mk":"Louise Nevelson","y":"1950s–1980s","s":W+"Louise_Nevelson",
    "v":[V("Bride of the Black Moon","Louise Nevelson","1955"),V("Sky Cathedral","Louise Nevelson","1958","her first wall piece"),V("Black Zag X","Louise Nevelson","1969","aluminium"),V("Sky Landscape","Louise Nevelson","1988")],
    "dt":"painted wood · Formica or aluminium later · modular boxes"},
   {"n":"Cubist construction and assemblage origins","a":"Picasso constructions","d":"The historical root of assemblage: Picasso's cubist constructions of 1912–14 and the 1961 MoMA 'Art of Assemblage'.","mk":"","y":"1912–1961","s":W+"Assemblage_(art)",
    "v":[V("Cubist constructions","Pablo Picasso","c. 1912–14"),V("Counter-reliefs","Vladimir Tatlin","1914"),V("The Art of Assemblage (MoMA)","William C. Seitz","1961","curator")],
    "dt":"found objects · substrate · museum vs market rarity"}]},
 {"n":"Soft sculpture","a":"fabric sculpture · stuffed sculpture","d":"A three-dimensional sculpture of fabric, fibre or other soft material, stuffed, wrapped or stitched.",
  "t":["stuffed vinyl","sewn canvas","wrapped","knitted or crocheted","unique","multiple"],
  "s":"https://www.artsy.net/categories",
  "x":[
   {"n":"Oldenburg soft object","a":"Floor Burger · soft sculpture","d":"Claes Oldenburg's oversized soft replicas of everyday objects, which popularised the term in the 1960s.","mk":"Claes Oldenburg","y":"1957–1960s","s":W+"Soft_sculpture",
    "v":[V("Sausage","Claes Oldenburg","1957","stocking stuffed with newspaper"),V("The Store (Floor Hamburger, Floor Cone, Floor Cake)","Claes Oldenburg","1961","Lower East Side shop")],
    "dt":"canvas, vinyl or kapok · ageing and sagging · multiple vs unique"},
   {"n":"Kusama accumulation","a":"Accumulation No. 1","d":"Yayoi Kusama's armchair covered in hand-sewn protrusions.","mk":"Yayoi Kusama","y":"1962","s":W+"Soft_sculpture",
    "v":[V("Accumulation No. 1","Yayoi Kusama","1962")],
    "dt":"found furniture · sewn stuffed forms"}]},
 {"n":"Neon sculpture","a":"light sculpture","d":"A sculpture in which a lit gas-discharge tube or an equivalent light source is the medium.",
  "t":["neon text","neon on panel","free-standing neon","LED neon-effect","edition of three with artist's proofs"],
  "s":"https://www.singulart.com/en/sculpture",
  "x":[
   {"n":"Nauman neon","a":"Nauman text neon","d":"Bruce Nauman's wordplay and spiral neon signs.","mk":"Bruce Nauman","y":"1967–1988","s":W+"Bruce_Nauman",
    "v":[V("The True Artist Helps the World by Revealing Mystic Truths","Bruce Nauman","1967"),V("Violins Violence Silence","Bruce Nauman","1981/82"),V("One Hundred Live and Die","Bruce Nauman","1984"),V("Vices and Virtues","Bruce Nauman","1988","UC San Diego")],
    "dt":"replication rules need artist or estate approval · working original · non-archival tubes"},
   {"n":"Emin neon","a":"handwritten neon","d":"Tracey Emin's neon phrases in her own handwriting.","mk":"Tracey Emin","y":"1998–2018","s":W+"Tracey_Emin",
    "v":[V("Is Anal Sex Legal","Tracey Emin","1998"),V("You Forgot To Kiss My Soul","Tracey Emin","2001"),V("Legs I and Legs IV","Tracey Emin","2007"),V("I Want My Time With You","Tracey Emin","2018","St Pancras Station")],
    "dt":"handwriting colour · edition · conservation of tubes"}]},
 {"n":"Sculpture stand","a":"plinth","d":"A base, plinth or stand made for one sculpture.","t":["wooden plinth","stone base","turntable stand","display column","vitrine"],"s":"https://www.1stdibs.com/buy/sculpture-display-stand/"}
]
brands=[]
for n,c,f in [("David Smith","United States",""),]: pass
notes="Archetypes are named artists' series taken from retrieved Wikipedia pages; artists belong to the artist register, so mk holds the artist and no brand entries are made. Sculpture stand left kind-level. Corten attestation via Tilted Arc and The Matter of Time pages. Calder edition/authentication: Calder Foundation examines, does not authenticate (Calder page)."
json.dump({"kinds":kinds,"brands":[],"traditions":[],"notes":notes},open('work/F2/shelves/04_03.tmp','w'),ensure_ascii=False,indent=1)
os.rename('work/F2/shelves/04_03.tmp','work/F2/shelves/04_03.json')
