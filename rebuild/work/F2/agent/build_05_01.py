import json,os
W='https://en.wikipedia.org/wiki/'
def V(n,mk="",y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
def B(n,c,f,seg,kf,d,s,sig=None):
    b={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s}
    if sig: b["sig"]=sig
    return b
SW=W+"Swarovski"
kinds=[
 {"n":"Crystal and glass figurine","a":"crystal animal · glass figurine · Murano glass animal","d":"A figure of cut or moulded crystal or glass, usually an animal, bird or flower.",
  "t":["lead crystal","Murano hot-worked glass","lampwork glass","pâte de verre","frosted crystal","annual edition","limited edition"],
  "s":SW,
  "x":[
   {"n":"Swarovski Mouse","a":"replica mouse","d":"Swarovski's first figurine, a stylised crystal mouse; a smaller 'replica mouse' is still sold.","mk":"Swarovski","y":"","s":SW,
    "v":[V("Replica mouse","Swarovski")],"dt":"size · packaging · period"},
   {"n":"Swarovski Idyllia","a":"","d":"Swarovski series of crystal animals paired with plants or small creatures.","mk":"Swarovski","y":"","s":SW,
    "v":[V("Idyllia Baby Owl","Swarovski"),V("Idyllia Fox and Butterfly","Swarovski"),V("Idyllia Hedgehog","Swarovski"),V("Idyllia Toucan","Swarovski"),V("Idyllia Flamingo","Swarovski")],
    "dt":"animal · colour accent · size"},
   {"n":"Swarovski Florere","a":"","d":"Swarovski series of crystal flowers.","mk":"Swarovski","y":"","s":SW,
    "v":[V("Florere Rose","Swarovski"),V("Florere Camellia","Swarovski"),V("Florere Lily of the Valley","Swarovski"),V("Florere Daffodil","Swarovski")],
    "dt":"flower · colour"},
   {"n":"Swarovski Asian Symbols","a":"","d":"Swarovski series of crystal figures of lucky Asian symbols.","mk":"Swarovski","y":"","s":SW,
    "v":[V("Asian Symbols Golden Carp","Swarovski"),V("Asian Symbols Leaping Horse","Swarovski"),V("Asian Symbols Lucky Cat","Swarovski")],
    "dt":"animal · gold-plated accents"},
   {"n":"Swarovski Crystal Myriad","a":"","d":"Swarovski series of crystal pieces in many small elements.","mk":"Swarovski","y":"","s":SW,
    "v":[V("Crystal Myriad Pomegranate","Swarovski"),V("Crystal Myriad Tropical Scene","Swarovski")],"dt":"subject"},
   {"n":"Swarovski Signum and Jungle Beats","a":"","d":"Two further Swarovski animal series.","mk":"Swarovski","y":"","s":SW,
    "v":[V("Signum Swan","Swarovski"),V("Jungle Beats Parakeet Couple Fife & Fifer","Swarovski")],"dt":"animal"},
   {"n":"Lalique glass figure","a":"Lalique crystal figure","d":"Figures from René Lalique's glassworks, such as the 1920 mermaid and the 1922 Firebird; after 1945 production moved to lead crystal.","mk":"Lalique","y":"1920s onward","s":W+"Lalique",
    "v":[V("Sirène (mermaid statuette)","Lalique","1920"),V("Oiseau de Feu (Firebird)","Lalique","1922")],
    "dt":"period (René vs post-1945 crystal) · signature · frosting"},
   {"n":"Murano glass figure","a":"Venetian glass animal","d":"Hot-worked glass figures from the island of Murano, Venice's glass centre since 1291.","mk":"","y":"from 1291","s":W+"Venetian_glass",
    "v":[V("Artistic Glass Murano trademark","","1994","certifies Murano origin; imitations hold 40–45% of the market")],
    "dt":"technique · maker (furnace) · signed or not · trademark"}]},
 {"n":"Pewter and cast-metal figurine","a":"cast-metal figurine · Vienna bronze","d":"An ornamental figure cast in pewter, zinc, tin, or small cold-painted bronze rather than fine-art bronze.",
  "t":["pewter","cold-painted bronze","zinc spelter","tin","hand-finished"],
  "s":"https://whamond.com/en-eu/collections/royal-selangor",
  "x":[
   {"n":"Vienna cold-painted bronze","a":"Bergmann bronze · Namgreb","d":"Small bronzes cast in Vienna and coloured with layers of unfired dust paint, mostly animals and Orientalist figures.","mk":"Bergmann","y":"1860–1930s","s":W+"Franz_Xaver_Bergmann",
    "v":[V("Bronze factory founded by Franz Bergmann","Bergmann","1860"),V("New foundry opened by Franz Xaver Bergmann","Bergmann","1900"),V("Foundry closed in the Depression","Bergmann","1930")],
    "dt":"mark: 'B' in an urn cartouche or 'Nam Greb' · paint layers · animal vs erotic figure with mechanism"},
   {"n":"Royal Selangor pewter","a":"","d":"Malaysian pewter maker, founded 1885, whose range includes tankards, tea sets and gifts.","mk":"Royal Selangor","y":"1885","s":W+"Royal_Selangor",
    "v":[V("Centenary giant tankard","Royal Selangor","1985","world's largest pewter tankard")],
    "dt":"pewter grade · hand-finished · gift ranges"}]},
 {"n":"Resin figurine","a":"resin sculpture · collectible resin figurine","d":"A cast resin figure, usually painted, sold as a collectible.",
  "t":["hand-painted resin","stone resin","limited edition","pop-culture statue (see Toys, E1)"],
  "s":"https://www.singulart.com/en/sculpture",
  "x":[
   {"n":"Willow Tree figurine","a":"Susan Lordi figurines","d":"Faceless hand-painted resin people and angels cast from Susan Lordi's carved clay originals.","mk":"Demdaco","y":"2000","s":W+"Willow_Tree_(figurines)",
    "v":[V("Willow Tree line created by Susan Lordi","Demdaco","January 2000")],
    "dt":"subject · emotion theme · resin · gift-shop retail"}]}
]
brands=[
 B("Swarovski","Austria","1895","Premium","crystal","Crystal maker in Wattens, Tyrol, founded in 1895 by Daniel Swarovski; its first figurine was a stylised mouse.",SW,["Swarovski Idyllia","Swarovski Florere"]),
 B("Lalique","France","1888","Premium","glass and crystal","Founded in Paris in 1888 by René Lalique; after 1945 production moved from glass to lead crystal.",W+"Lalique"),
 B("Baccarat","France","1764","Heritage manufactory","lead crystal","Lorraine crystal glassworks authorised in 1764.",W+"Baccarat,_Meurthe-et-Moselle"),
 B("Royal Selangor","Malaysia","1885","Premium","pewter","Pewter maker founded by Yong Koon in 1885, based in Kuala Lumpur.",W+"Royal_Selangor"),
 B("Bergmann","Austria","1860","Artisan & independent","Vienna bronze","Viennese bronze factory founded in 1860 by Franz Bergmann, run later by Franz Xaver Bergmann.",W+"Franz_Xaver_Bergmann"),
 B("Demdaco","United States","","Mainstream","Willow Tree","Distributor and marketer of Susan Lordi's Willow Tree figurines.",W+"Willow_Tree_(figurines)")]
notes="Swarovski series are taken from the old k42 model list and the Swarovski company page. Left out for lack of retrieved support: Swarovski Crystal Society annual editions, Daum, Border Fine Arts, Country Artists, Britains-style figures (toy soldiers stay in E1). Baccarat and Daum animals unconfirmed; Baccarat in register only. Pop-culture statues are cross-linked to E1 in t. Old Swarovski items sit as versions under series."
json.dump({"kinds":kinds,"brands":brands,"traditions":[],"notes":notes},open('work/F2/shelves/05_01.tmp','w'),ensure_ascii=False,indent=1)
os.rename('work/F2/shelves/05_01.tmp','work/F2/shelves/05_01.json')
