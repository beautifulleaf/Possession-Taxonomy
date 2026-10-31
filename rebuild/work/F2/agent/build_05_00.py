import json,os
W='https://en.wikipedia.org/wiki/'
def V(n,mk="",y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
ME=W+"Meissen_porcelain"; RD=W+"List_of_Royal_Doulton_figurines"
def B(n,c,f,seg,kf,d,s,sig=None): 
    b={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s}
    if sig: b["sig"]=sig
    return b
doulton_m=[["Coralie","Royal Doulton"],["Darling","Royal Doulton"],["Delight","Royal Doulton"],["Dunce","Royal Doulton"],["Jovial Sitting Jester","Royal Doulton"],["Madonna of the Square","Royal Doulton"],["Milking Time","Royal Doulton"],["Pantalettes","Royal Doulton"],["Pedlar Wolf","Royal Doulton"],["Picardy Peasant","Royal Doulton"],["Pussy (The Black Cat)","Royal Doulton"],["Queen Philippa of Hainault","Royal Doulton"],["Rachel","Royal Doulton"],["Sleepy Scholar","Royal Doulton"],["The Coquette","Royal Doulton"],["The Crinoline","Royal Doulton"],["The Lawyer","Royal Doulton"]]
lladro_m=[["Jester (Clown's Head)","Lladro"],["Santa's Magic Touch","Lladro"],["Summer Stroll","Lladro"],["Venetian Fantasy","Lladro"],["Waiting for the Bell","Lladro"]]
kinds=[
 {"n":"Porcelain and bone china figurine","a":"glazed earthenware sculpture · stoneware sculpture · bone china figurine · porcelain sculpture","d":"Figurines of porcelain, bone china or glazed pottery, organised by house, then series, then piece.",
  "t":["Glazed pottery figurine","Earthenware figurine","Hard-paste porcelain figurine","Soft-paste porcelain figurine","Bone china figurine","Biscuit (unglazed) porcelain figurine","limited edition","annual or club piece"],
  "s":"",
  "x":[
   {"n":"Meissen Kändler figures","a":"Meissen figures · Kändler models","d":"Figures modelled by Johann Joachim Kändler, chief modeller at Meissen from 1733, first made to decorate grand dining tables.","mk":"Meissen","y":"1733–1775","s":ME,
    "v":[V("Monkey Band (Affenkapelle)","Meissen","1753–1754","modelled by Kändler and Reinicke; later set in the 1760s"),V("Commedia dell'arte figures","Meissen","c. 1735–1744","Kändler; precursors by Balthasar Permoser c. 1710–12")],
    "dt":"model number · crossed-swords mark (introduced 1720) · period vs later issue · restoration"},
   {"n":"Royal Doulton HN figure","a":"HN series · Royal Doulton figurines","d":"Royal Doulton's numbered figure series; HN stands for Harry Nixon and numbering began with HN1 Darling in 1913.","mk":"Royal Doulton","y":"1913 onward","s":RD,
    "v":[V("Darling (HN1)","Royal Doulton","1913","designed by Charles Vyse"),V("Elizabeth Fry (HN2)","Royal Doulton","1913–1938","designed by Charles Vyse"),V("The Old Balloon Seller (HN1315)","Royal Doulton","1929–1998","designed by Leslie Harradine; other versions HN1912 and HN2129"),V("Maureen (HN1770)","Royal Doulton","1936–1959","Leslie Harradine"),V("The Gaffer (HN2053)","Royal Doulton","1950–1959","Leslie Harradine")],
    "dt":"HN number · colourway variant (A suffix) · years in production · designer"},
   {"n":"Lladró figurine","a":"Lladro","d":"Hard-paste porcelain sculptures from the Lladró brothers' Valencia workshop; titles can change during a run.","mk":"Lladro","y":"1956 onward","s":W+"Lladr%C3%B3",
    "v":[V("Chit-Chat","Lladro"),V("On The Move","Lladro"),V("Shepherd at Rest","Lladro"),V("The Debutante","Lladro"),V("Elite Collection","Lladro","1974","a Lladró collection named in the article")],
    "dt":"title · sculptor · retired or current · Collectors' Society piece"},
   {"n":"M.I. Hummel figurine","a":"Hummel · Goebel Hummel","d":"Porcelain figures based on drawings by Maria Innocentia Hummel, first made by Goebel in 1935.","mk":"Goebel","y":"1935 onward","s":W+"Hummel_figurines",
    "v":[V("First Goebel line, shown at the Leipzig Trade Fair","Goebel","1935"),V("Production at Manufaktur Rödental","Manufaktur Rödental","2009"),V("Production at Hummel Manufaktur GmbH","Hummel Manufaktur","2014")],
    "dt":"Goebel trademark mark (TMK stage, to verify) · figure number · size · club edition"},
   {"n":"Nymphenburg commedia dell'arte figures","a":"Bustelli figures","d":"Franz Anton Bustelli's rococo commedia dell'arte figures, showpieces of the Nymphenburg museum.","mk":"Nymphenburg","y":"1754 onward","s":W+"Nymphenburg_Porcelain_Manufactory",
    "v":[V("Commedia dell'arte series","Nymphenburg","","Bustelli joined the factory in 1754")],
    "dt":"model by Bustelli · hand-made · period vs current edition"},
   {"n":"Capodimonte figure","a":"Naples porcelain figure","d":"Moulded figures from the Naples Real Fabbrica di Capodimonte (1743–1759), and the many later 'Capodimonte' imitations.","mk":"Capodimonte","y":"1743–1759","s":W+"Capodimonte_porcelain",
    "v":[V("Royal factory soft-paste figures","Capodimonte","1743–1759","chief modeller Giuseppe Gricci; blue fleur-de-lys mark"),V("Naples porcelain","Capodimonte","1771–1806")],
    "dt":"fleur-de-lys mark · period vs 19th–20th-century imitation"},
   {"n":"Herend Hungarian figures","a":"Herend figures","d":"Figures from the Herend manufactory, including interwar replicas of Hungarian sculptors' work.","mk":"Herend","y":"interwar","s":W+"Herend_Porcelain_Manufactory",
    "v":[V("Hungarian figures","Herend","1918–1939","replicas of Hungarian sculptors' work")],
    "dt":"hand painting · mark · size"},
   {"n":"Precious Moments figurine","a":"","d":"Collectible porcelain figures of children with teardrop eyes, from Samuel J. Butcher's company.","mk":"Precious Moments","y":"1978 onward","s":W+"Precious_Moments,_Inc.",
    "v":[V("Enesco-distributed figurines","Enesco","1978–2004","licensing contract ended 2004")],
    "dt":"series · year mark · boxed or unboxed"},
   {"n":"Beswick animal","a":"John Beswick animals","d":"Porcelain and china farm, horse and wild-animal figures from the Longton pottery.","mk":"Beswick","y":"1894 onward","s":W+"Beswick_Pottery",
    "v":[V("Gredington horsemen set (190 figures)","Beswick","","Arthur Gredington"),V("Beatrix Potter characters, starting with Jemima Puddle-Duck","Beswick","1948")],
    "dt":"model number · gloss or matt · backstamp era (Doulton from 1969; factory closed 2002)"}],
  "m":[["Malin","Gustavsberg"]]+lladro_m+doulton_m},
 {"n":"Staffordshire figure","a":"Staffordshire pottery figure · flatback","d":"English earthenware figures made mainly in Staffordshire from the 18th century, many unmarked.",
  "t":["flatback","press-moulded","slip-cast","spill vase group","pastille burner","pair"],
  "s":W+"Staffordshire_figure",
  "x":[
   {"n":"Victorian flatback","a":"flatbacks · mantelpiece figure","d":"Victorian figures modelled only on the front and sides to stand on a shelf or mantelpiece.","mk":"","y":"1837–1900","s":W+"Staffordshire_figure",
    "v":[V("Press-moulded flatback"),V("Slip-cast flatback")],
    "dt":"subject · size · unmarked · gilding · fakes common"},
   {"n":"Staffordshire spaniel pair","a":"Staffordshire dogs · hearth spaniels · wally dogs","d":"Matching pairs of King Charles spaniel figures for mantelpieces.","mk":"","y":"1720s–1920s","s":W+"Staffordshire_dog_figurine",
    "v":[V("Pair of spaniels","","","linked to Queen Victoria's dog Dash"),V("Scottish bulk production at Pollokshaws and Portobello")],
    "dt":"early models better quality · pair completeness · reproductions still made in 2009"},
   {"n":"Ralph Wood figure","a":"Wood family figures","d":"Late-18th-century figures by three generations of the Wood modelling family.","mk":"Ralph Wood","y":"late 18th century","s":W+"Staffordshire_figure",
    "v":[V("Demosthenes model","Enoch Wood","c. 1785")],
    "dt":"modeller · colouring · marks"}]},
 {"n":"Character and Toby jug","a":"face jug · Fillpot","d":"A jug shaped as a seated figure (Toby) or as a head and shoulders (character jug).",
  "t":["Toby jug (seated figure)","character jug (head only)","miniature","limited edition"],
  "s":W+"Toby_Jug",
  "x":[
   {"n":"Ralph Wood Toby jug","a":"Toby Fillpot","d":"The seated-figure jug popularised by Burslem potter Ralph Wood.","mk":"Ralph Wood","y":"c. 1782–1795","s":W+"Toby_Jug",
    "v":[V("Toby jug by Ralph Wood the Younger","Ralph Wood","c. 1782–1795")],
    "dt":"colouring · figure type · period vs reproduction"},
   {"n":"Royal Doulton character jug","a":"Doulton Toby","d":"Brightly coloured head-and-shoulders jugs introduced by Doulton in 1934.","mk":"Royal Doulton","y":"1934","s":W+"Charles_Noke",
    "v":[V("John Barleycorn","Royal Doulton","1934","Charles Noke's own design")],
    "dt":"size (large, small, miniature) · character · years in production"}]}
]
brands=[
 B("Meissen","Germany","1709","Heritage manufactory","hard-paste porcelain","First European hard-paste porcelain manufactory, founded in 1709.",ME),
 B("Royal Doulton","United Kingdom","1815","Heritage manufactory","figures, bone china","English pottery founded in 1815, maker of HN figures and character jugs.",W+"Royal_Doulton",["Royal Doulton HN figure","Royal Doulton character jug"]),
 B("Lladro","Spain","1953","Premium","porcelain sculpture","Valencian maker of hard-paste porcelain figures, founded in 1953 by the Lladró brothers.",W+"Lladr%C3%B3",["Lladró figurine"]),
 B("Goebel","Germany","","Mainstream","Hummel figures","German porcelain maker that licensed M.I. Hummel's art and issued the first line in 1935.",W+"Hummel_figurines",["M.I. Hummel figurine"]),
 B("Nymphenburg","Germany","1747","Heritage manufactory","Bustelli figures","Bavarian porcelain manufactory founded in 1747, in Munich since 1761.",W+"Nymphenburg_Porcelain_Manufactory"),
 B("Capodimonte","Italy","1743","Heritage manufactory","Naples figures","Royal Naples porcelain factory 1743–1759, known for moulded figures.",W+"Capodimonte_porcelain"),
 B("Herend","Hungary","1826","Heritage manufactory","hand-painted porcelain","Hungarian manufactory founded in 1826 near Veszprém.",W+"Herend_Porcelain_Manufactory"),
 B("Precious Moments","United States","1978","Mainstream","child figurines","Missouri giftware company founded by Samuel J. Butcher in 1978.",W+"Precious_Moments,_Inc."),
 B("Beswick","United Kingdom","1894","Heritage manufactory","animal figures","Longton pottery founded 1894; factory closed 2002; brand now with Dartington Crystal.",W+"Beswick_Pottery"),
 B("Gustavsberg","Sweden","1826","Heritage manufactory","porcelain","Swedish porcelain maker begun in 1826.",W+"Gustavsberg_porcelain"),
 B("Royal Copenhagen","Denmark","1775","Heritage manufactory","blue-fluted porcelain","Royal porcelain factory founded in Copenhagen in 1775, marked with three wavy lines.",W+"Royal_Copenhagen"),
 B("Royal Crown Derby","United Kingdom","","Heritage manufactory","Imari patterns","English maker of ornamental and table porcelain, tracing its origin to about 1750.",W+"Royal_Crown_Derby")]
notes="Swarovski items from old k42 (crystal) go to shelf 05_01, as its brief says. Old Doulton/Lladro/Gustavsberg models kept: five as versions per house, the rest in m. Left out for lack of retrieved support: Pretty Ladies series, Royal Copenhagen and Royal Crown Derby paperweight archetypes (houses recorded in the register only), Hummel TMK marks (flagged to verify). Earthenware is a t of the porcelain kind. Staffordshire page confirms flatbacks, Ralph Wood, Enoch Wood."
json.dump({"kinds":kinds,"brands":brands,"traditions":[],"notes":notes},open('work/F2/shelves/05_00.tmp','w'),ensure_ascii=False,indent=1)
os.rename('work/F2/shelves/05_00.tmp','work/F2/shelves/05_00.json')
