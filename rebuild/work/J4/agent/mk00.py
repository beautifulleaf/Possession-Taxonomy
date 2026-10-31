import json
W="https://en.wikipedia.org/wiki/"
def x(n,mk,y,s,d,v=None,a="",dt=""):
    o={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v or []}
    if dt:o["dt"]=dt
    return o
def v(n,mk="",y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
X=[
x("Red Delicious","","1872",W+"Red_Delicious","Chance seedling found by Jesse Hiatt at Peru, Iowa; once the top US apple, with over 300 named strains.",
  [v("Hawkeye (Hiatt's original)","","1872","Name Hiatt gave it; Stark Nurseries renamed it Stark Delicious, then Red Delicious in 1914")],dt="dark red, elongated shape · many sports"),
x("Golden Delicious","","1905",W+"Golden_Delicious","Yellow chance seedling from Clay County, West Virginia (Mullins' Yellow Seedling); parent of Gala, Jonagold, Cripps Pink and Elstar.",
  [v("Mullins' Yellow Seedling","","1905","Local name before Stark Brothers bought the rights")],dt="yellow-green skin · sweet · bruises easily"),
x("Granny Smith","","1868",W+"Granny_Smith","Green apple from a chance seedling propagated by Maria Ann Smith at Eastwood, Sydney; a long-keeping export apple.",
  [v("Granny Smith's Seedling","","1891","Name when it won a cooking-apple prize")],dt="green skin · tart · long storage"),
x("McIntosh","","1811",W+"McIntosh_(apple)","Canada's national apple, a chance seedling found by John McIntosh at Dundela, Ontario; parent of Macoun, Cortland, Spartan and Empire.",
  [v("Macoun","","","McIntosh offspring"),v("Cortland","","","McIntosh offspring"),v("Spartan","","","McIntosh offspring"),v("Empire","","","McIntosh x Red Delicious")],dt="red-green skin · soft white flesh"),
x("Cox's Orange Pippin","","1830",W+"Cox_Orange_Pippin","English dessert apple raised by Richard Cox at Colnbrook, Buckinghamshire; the benchmark for flavour and parent of Elstar.",
  [v("Cherry Cox","","","sport"),v("Crimson Cox","","","sport"),v("King Cox","","","sport"),v("Queen Cox","","","sport")],a="Cox · Cox Orange Pippin",dt="orange-red flush · cherry and aniseed notes"),
x("Fuji","","1939",W+"Fuji_(apple)","Red Delicious x Ralls Janet cross bred at the Tohoku Research Station, Fujisaki, Aomori; named in 1962, now a world staple.",
  [v("Fuji from Aomori","","","Japan's main apple region, about 500,000 of Japan's roughly 900,000 annual tonnes")],dt="sweet, dense, keeps up to a year in cold store"),
x("Gala","","1939",W+"Gala_(apple)","New Zealand apple from Golden Delicious x Kidd's Orange Red, raised by J. H. Kidd; overtook Red Delicious in US output in 2018.",
  [v("Royal Gala","","1977","Redder sport, US plant patent 4121"),v("Galaxy","","1989","Gala sport"),v("Scarlet Gala","","1988","Gala sport")],dt="orange-striped · sweet, mild"),
x("Braeburn","","1952",W+"Braeburn","Chance seedling found by O. Moran near Motueka, Nelson, New Zealand; sweet-tart and a parent of Jazz, Kanzi and Envy.",
  dt="red over yellow · stores well · internal browning in long storage"),
x("Honeycrisp","University of Minnesota","1960",W+"Honeycrisp","University of Minnesota variety released in 1991; very crisp and juicy, and the parent of much of the newer breeding.",
  [v("MN1711","University of Minnesota","1974","Breeder code; patent expired 2008; plant-variety record for the C3 plants register")],dt="large cells · bruises easily · bitter pit"),
x("Cripps Pink","Pink Lady","1973",W+"Cripps_Pink","Golden Delicious x Lady Williams cross by John Cripps in Western Australia, sold under the Pink Lady trade mark.",
  [v("Cripps Pink (Pink Lady)","Pink Lady","1973","Base cultivar; owned and licensed by the WA Department of Primary Industries and Regional Development"),
   v("Cripps Red (Sundowner)","","","Redder Cripps cultivar sold as Sundowner")],a="Pink Lady",dt="PL-prefixed selection codes e.g. PLMAS98 (Maslin)"),
x("Jazz","Jazz","1985",W+"Jazz_(apple)","Braeburn x Royal Gala cross from Hawke's Bay, New Zealand, launched commercially in 2004.",
  [v("Scifresh (Jazz)","Jazz","2004","Cultivar name behind the Jazz trade mark")],dt="hard, crisp, juicy"),
x("Envy","Envy","2009",W+"Envy_(apple)","Braeburn x Royal Gala variety from New Zealand, very sweet and slow to brown.",
  [v("Scilate (Envy)","Envy","2009","Cultivar name; US plant patent PP20477")],dt="red with yellow specks · thick skin"),
x("Cosmic Crisp","Cosmic Crisp","2019",W+"Cosmic_Crisp","Honeycrisp x Enterprise apple bred by Washington State University and first sold in December 2019.",
  [v("WA 38 (Cosmic Crisp)","Cosmic Crisp","1997","Breeder code; WSU patent, growing limited to Washington until March 2027")],dt="wine-red skin with pale lenticels"),
x("Bramley's Seedling","","1809",W+"Bramley_apple","English cooking apple from a seedling planted in Southwell, Nottinghamshire; a triploid with RHS Award of Garden Merit.",
  [v("Armagh Bramley Apples PGI","","","County Armagh, Northern Ireland; EU Protected Geographical Indication, tarter than English fruit")],a="Bramley",dt="large, green, sharp · cooking"),
x("Belle de Boskoop","","1856",W+"Belle_de_Boskoop","Dutch chance seedling from Boskoop, tart and firm, holding shape when cooked; red, yellow and green types.",
  [v("Boskoop (Belle de Boskoop)","","1856","Old-data entry")],a="Boskoop · Goudrenet"),
x("Annurca","","",W+"Annurca","Old southern Italian apple from Campania that reddens on the ground after picking.",
  [v("Melannurca Campana PGI","","","Protected Geographical Indication; clones Standard and Rossa del Sud")],a="Melannurca · Mela Annurca"),
x("South Tyrol apples","","2005",W+"South_Tyrolean_Apple_PGI","Multi-cultivar PGI for apples grown in South Tyrol, mainly along the Adige valley; registered in 2005.",
  [v("Mela Alto Adige o Sudtiroler Apfel PGI","","2005","PGI name; permitted cultivars include Golden Delicious, Gala, Braeburn, Fuji, Granny Smith, Elstar and Jonagold")],a="Mela Alto Adige · Sudtiroler Apfel"),
x("Jonagold","","1943",W+"Jonagold","Golden Delicious x Jonathan cross from Geneva, New York, released in 1968; triploid and widely grown in Belgium and the Netherlands.",
  [v("Jonagored","","1985","Sport found in Belgium")]),
x("Elstar","","1950s",W+"Elstar","Dutch Ingrid Marie x Golden Delicious cross from Elst, popular in northern continental Europe.",dt="red over yellow · sweet-sharp"),
x("Sekai Ichi","","1930",W+"Sekai_Ichi","Very large Japanese premium apple (about 900 g), grown mainly in Aomori and sold as a luxury gift.",
  [v("Sekai Ichi from Morioka","","1930","First planted at Morioka; released to market 1974")],a="World's Number One"),
x("Kanzi","Kanzi","2006",W+"Kanzi_(apple)","Belgian Braeburn x Gala variety marketed under the Kanzi trade mark since 2006.",
  [v("Nicoter (Kanzi)","Kanzi","","Cultivar name behind the Kanzi trade mark")],dt="firm, crisp, mildly sharp"),
x("Rubens","Rubens","1985",W+"Civni_apple","Gala x Elstar cross by the Italian nursery consortium CIV of Ferrara, sold as Rubens.",
  [v("Civni","Rubens","","Cultivar name; US patent USPP14177 granted 2003")],a="Civni"),
x("SweeTango","SweeTango","2006",W+"SweeTango","Honeycrisp x Zestar apple from the University of Minnesota, grown only by members of a licensed grower cooperative.",
  [v("Minneiska (SweeTango)","SweeTango","2006","Cultivar name; breeder code MN 1914")],dt="managed (club) variety"),
]
old="""Akane Alkmene Ambrosia Antares Baldwin Cameo Cantared Charles Ross Cortland Criterion Discovery Empire Fiesta Gloster Gravenstein Haralson Idared Jonathan Laxtons_Fortune Lord_Lambourne Liberty Macoun Mutsu Opal Pinova Regent Rubinette Spartan Stayman Winesap Worcester Sturmer_Pippin""".split()
M=[["Akane",""],["Alkmene",""],["Ambrosia",""],["Antares",""],["Baldwin",""],["Cameo",""],["Charles Ross",""],["Cortland",""],["Discovery",""],["Elstar",""] ,["Fiesta",""],["Gloster",""],["Gravenstein",""],["Haralson",""],["Idared",""],["Jonathan",""],["Laxtons Fortune",""],["Lord Lambourne",""],["Macoun",""],["Opal",""],["Pinova",""],["Regent",""],["Rubinette",""],["Spartan",""],["Stayman",""],["Sturmer Pippin",""],["Winesap",""],["Worcester",""],["Northern Spy",""],["Reine des Reinettes (King of the Pippins)",""],["Bertanne (Golden Russet)",""],["Lady",""],["Ginger Gold",""],["Crispin (Mutsu)",""],["Maçã Bravo de Esmolfe PDO",""],["Mela Val di Non PGI",""],["Mele del Trentino PGI",""],["Mela Rossa Cuneo PGI",""],["Jabłka łąckie PGI",""],["Pomme du Limousin AOP",""]]
M=[m for m in M if m[0]!="Elstar"]
kind={"n":"Apple","a":"","d":"Fresh dessert, cooking or dual-purpose apple, organised by cultivar with its origin, club brand or breeder code.",
 "t":["dessert","cooking","dual-purpose","russet"],"s":"https://plu.pro/commodity/apples","x":X,"m":M}
B=lambda n,c,f,seg,kf,d,s,**k: dict(n=n,c=c,seg=seg,kf=kf,d=d,s=s,**({"f":f} if f else {}),**k)
brands=[
B("Pink Lady","Australia","","Specialist","club apple brand","Trade mark for Cripps Pink and related selections, managed by Apple and Pear Australia Limited and registered in over 80 territories.",W+"Cripps_Pink",sig=["Cripps Pink"],rel=["Cripps Red (Sundowner)"]),
B("Jazz","New Zealand","","Specialist","club apple brand","Trade mark for the Scifresh cultivar, a Braeburn x Royal Gala cross grown under licence in about ten countries.",W+"Jazz_(apple)",sig=["Jazz"],rel=["Envy","Kanzi"]),
B("Envy","New Zealand","","Specialist","club apple brand","Trade mark for the Scilate cultivar, distributed in North America from 2009 through the Oppenheimer Group and ENZA.",W+"Envy_(apple)",sig=["Envy"],rel=["Jazz"]),
B("Cosmic Crisp","United States","","Specialist","club apple brand","Trade mark for WA 38, the Washington State University variety with growing limited to Washington State.",W+"Cosmic_Crisp",sig=["Cosmic Crisp"]),
B("Kanzi","Belgium","","Specialist","club apple brand","Trade mark for the Nicoter cultivar, owned through Better3Fruits and Greenstar Kanzi Europe.",W+"Kanzi_(apple)",sig=["Kanzi"],rel=["Jazz"]),
B("Rubens","Italy","","Specialist","club apple brand","Trade mark for the Civni cultivar bred by the Consorzio Italiano Vivaisti of Ferrara.",W+"Civni_apple",sig=["Rubens"]),
B("SweeTango","United States","","Specialist","club apple brand","University of Minnesota trade mark for Minneiska, with marketing rights held by Pepin Heights Orchards and the Next Big Thing cooperative.",W+"SweeTango",sig=["SweeTango"],rel=["Honeycrisp"]),
B("University of Minnesota","United States","","Institution & issuer","apple breeding","Public university whose apple programme produced Honeycrisp (MN1711) and SweeTango (MN 1914).",W+"Honeycrisp",sig=["Honeycrisp","SweeTango"]),
]
for b in brands:
    if "c" in b: b["c"]=b["c"]
trad=[{"n":"English apple orchard heritage","g":"Food & drink","r":"England","p":"Medieval to present","d":"Grafted orchards of named local dessert and culinary apples, kept alive in estates, walled gardens and community orchards.",
 "tech":"grafting onto rootstocks; standard and espalier training","mat":"apple, pear, plum, cherry, damson trees","forms":["Ribston Pippin","Blenheim Orange","Ashmead's Kernel","Lane's Prince Albert","Bramley's Seedling","Cox's Orange Pippin"],
 "ctr":["English Heritage orchards at Walmer Castle, Mount Grace Priory, Barnard Castle, Osborne"],"auth":"Named cultivars propagated by grafting, not seed","s":"https://www.english-heritage.org.uk/learn/conservation/gardens-and-landscapes/orchard-conservation/"}]
notes="Kept Apple. Old cultivars not promoted to archetypes (no page fetched) kept as flat models, trimmed to 40: dropped breeder-code club lines (e.g. WA 2, DS 22, Regal D-codes, Howell TC2/TC3), Portuguese/Greek/Hungarian/Tunisian GIs and minor cultivars. Nagano Fuji not confirmed, left out. Mela Val di Non is a PDO per the EU; old-data spelling kept. Antiche mele groups, Etna and Sibillini not sourced, dropped. Honeycrisp, Cosmic Crisp, Envy plant-variety records noted in version text for C3 linking."
json.dump({"kinds":[kind],"brands":brands,"traditions":trad,"notes":notes},open("work/J4/shelves/00_00.tmp","w"),ensure_ascii=False,indent=1)
