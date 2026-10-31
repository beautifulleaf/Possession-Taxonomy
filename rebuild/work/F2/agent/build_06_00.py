import json,os
W='https://en.wikipedia.org/wiki/'
def V(n,mk="",y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
def B(n,c,f,seg,kf,d,s,sig=None):
    b={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s}
    if sig: b["sig"]=sig
    return b
def T(n,g,r,p,d,tech,mat,forms,ctr,auth,s): return {"n":n,"g":g,"r":r,"p":p,"d":d,"tech":tech,"mat":mat,"forms":forms,"ctr":ctr,"auth":auth,"s":s}
SP=W+"Studio_pottery"; AP=W+"Art_pottery"; JP=W+"Japanese_pottery_and_porcelain"
kinds=[
 {"n":"Studio pottery","a":"studio pottery vessel · studio ceramics","d":"Hand-made pottery by an individual or small group, unique or in short runs, from tableware to sculptural vessels.",
  "t":["thrown stoneware","salt-glazed","celadon or tenmoku glaze","burnished and carbonised","unglazed","tableware","signed unique vessel"],
  "s":SP,
  "x":[
   {"n":"Leach Pottery Standard Ware","a":"St Ives Standard Ware","d":"Everyday hand-thrown stoneware made at Bernard Leach's St Ives pottery, sold partly by mail order.","mk":"Leach Pottery","y":"1946–1979","s":W+"Leach_Pottery",
    "v":[V("Celadon glaze","Leach Pottery"),V("Tenmoku glaze","Leach Pottery"),V("Oatmeal glaze with brown and blue overpainting","Leach Pottery")],
    "dt":"glaze · potter's seal · maker (Leach or apprentice) · V&A holds examples"},
   {"n":"Bernard Leach pot","a":"Leach studio piece","d":"Pots by Bernard Leach (1887–1979), the 'father of British studio pottery', blending Eastern and Western traditions.","mk":"Bernard Leach","y":"1920–1979","s":W+"Bernard_Leach",
    "v":[V("A Potter's Book","Bernard Leach","1940","his craft philosophy")],
    "dt":"exhibition piece vs standard ware · BL seal · glaze"},
   {"n":"Shōji Hamada mingei ware","a":"Mashiko ware","d":"Pots by Shōji Hamada (1894–1978), a central mingei figure who made Mashiko a pottery centre using local materials.","mk":"Shōji Hamada","y":"1923–1978","s":W+"Sh%C5%8Dji_Hamada",
    "v":[V("Living National Treasure designation","Shōji Hamada","1955","first craftsman so honoured")],
    "dt":"Mashiko clay · glaze · box inscription"},
   {"n":"Lucie Rie bowl and bottle","a":"Rie porcelain","d":"Finely potted bowls, bottles and vases by Lucie Rie (1902–1995), known for glaze and firing experiments.","mk":"Lucie Rie","y":"1930s–1990s","s":W+"Lucie_Rie",
    "v":[V("Paris International Exhibition silver medal","Lucie Rie","1937")],
    "dt":"glaze · form · studio mark · museum comparison (MoMA, V&A)"},
   {"n":"Hans Coper form","a":"Coper pot","d":"Unglazed sculptural forms by Hans Coper (1920–1981), who worked with Rie from 1946 and opened his own studio in 1958.","mk":"Hans Coper","y":"1946–1981","s":W+"Hans_Coper",
    "v":[V("Spade form","Hans Coper"),V("Bud form","Hans Coper"),V("Cup form","Hans Coper"),V("Egg form","Hans Coper"),V("Coventry Cathedral candlesticks","Hans Coper","1962","six seven-foot candlesticks")],
    "dt":"named form · surface · impressed seal"},
   {"n":"Odundo burnished vessel","a":"Magdalene Odundo vase","d":"Hand-coiled, burnished and carbonised vessels by Magdalene Odundo (b. 1950), fired red-orange or black.","mk":"Magdalene Odundo","y":"1970s onward","s":W+"Magdalene_Odundo",
    "v":[V("Resonance and Inspiration exhibition","Magdalene Odundo","2006"),V("The Journey of Things exhibition","Magdalene Odundo","2019")],
    "dt":"oxidation-fired red or reduction-fired black · height · museum provenance"}]},
 {"n":"Ceramic sculpture","a":"sculptural ceramics · ceramic art","d":"Clay worked as sculpture rather than as a vessel, in stoneware, porcelain or earthenware.",
  "t":["stoneware","porcelain","earthenware","glazed","unglazed","installation element"],
  "s":W+"Peter_Voulkos",
  "x":[
   {"n":"Voulkos stack","a":"Voulkos stoneware","d":"Peter Voulkos's gestural, non-utilitarian stoneware works, after he turned to raw, gashed clay at Black Mountain College in 1953.","mk":"Peter Voulkos","y":"1953–2002","s":W+"Peter_Voulkos",
    "v":[V("Black Mountain College summer course","Peter Voulkos","1953"),V("Untitled (Stack)","Peter Voulkos","1980","stoneware"),V("Stack with Peter Callas","Peter Voulkos","1998")],
    "dt":"scale · firing · studio vs private provenance"},
   {"n":"Grayson Perry vase","a":"Perry pot","d":"Coiled classical-form vases with bright colours and decoration at odds with their look; Perry won the 2003 Turner Prize.","mk":"Grayson Perry","y":"1990s onward","s":W+"Grayson_Perry",
    "v":[V("Mad Kid's Bedroom Wall Pot","Grayson Perry","1996"),V("Using My Family","Grayson Perry","1998"),V("We've Found the Body of Your Child","Grayson Perry","2000"),V("Turner Prize","Grayson Perry","2003","first ceramic artist to win")],
    "dt":"transfer print · coiled · edition vs unique"}]},
 {"n":"Art pottery","a":"art pottery vase","d":"Decorative pottery made in small quantities, mostly 1870–1930, usually vases and bowls sold singly.",
  "t":["Arts and Crafts","Art Nouveau","Art Deco","matte glaze","tubelined","saltglaze stoneware","lustre"],
  "s":AP,
  "x":[
   {"n":"Moorcroft Florian Ware","a":"Moorcroft tubelined","d":"Moorcroft's first major range, Art Nouveau in style and tubelined by hand; gold medal at St Louis in 1904.","mk":"Moorcroft","y":"1897 onward","s":W+"Moorcroft",
    "v":[V("Florian Ware","Moorcroft","1897 onward","won gold medal at the 1904 St Louis world's fair"),V("W. Moorcroft Limited founded","Moorcroft","1913","Burslem")],
    "dt":"pattern · signature or initials · size"},
   {"n":"Rookwood Pottery glaze","a":"Rookwood Standard · Iris · Vellum","d":"Cincinnati art pottery founded in 1880 by Maria Longworth Nichols Storer, known for its glaze lines.","mk":"Rookwood","y":"1880–1967","s":W+"Rookwood_pottery",
    "v":[V("Standard Glaze","Rookwood","","yellow-tinted high gloss"),V("Iris glaze","Rookwood","1894"),V("Sea Green glaze","Rookwood","1894"),V("Vellum glaze","Rookwood","1904","matte")],
    "dt":"glaze · decorator (Shirayamadani, Fry, Hurley, Sax) · shape number"},
   {"n":"Grueby matte green vase","a":"Grueby Faience","d":"Revere, Massachusetts art pottery with a matte cucumber-green glaze introduced in 1897–98.","mk":"Grueby","y":"1894–1920","s":W+"Grueby_Faience_Company",
    "v":[V("First vases designed by George Prentiss Kendrick","Grueby"),V("Lamp bases for Tiffany Studios","Grueby")],
    "dt":"glaze · designer (Kendrick, LeBoutillier, Langenbeck) · Tiffany retail"},
   {"n":"Martinware bird","a":"Wally bird · Martin Brothers","d":"Whimsical stoneware bird jars by the Martin Brothers, with lift-off heads, made 1873–1914.","mk":"Martin Brothers","y":"1873–1914","s":W+"Martin_Brothers",
    "v":[V("Wallace Martin bird (tobacco jar)","Martin Brothers","c. 1880–1900","large beak, human-like eyes")],
    "dt":"saltglaze stoneware · incised mark · Fulham, Southall"},
   {"n":"Clarice Cliff Bizarre","a":"Original Bizarre · Crocus · Fantasque","d":"Bright Art Deco-patterned earthenware painted by Clarice Cliff on flawed stock from about 1927.","mk":"Clarice Cliff","y":"1927–1936","s":W+"Clarice_Cliff",
    "v":[V("Original Bizarre (triangle patterns)","Clarice Cliff","c. 1927–1928"),V("Crocus","Clarice Cliff","1928"),V("Fantasque","Clarice Cliff","1928–1934"),V("Purple Crocus","Clarice Cliff","1932"),V("Blue Crocus","Clarice Cliff","1935")],
    "dt":"pattern · shape · Bizarre backstamp (1928–early 1936) · Wedgwood reproductions 1992–2002"},
   {"n":"Wedgwood Fairyland Lustre","a":"Daisy Makeig-Jones lustre","d":"Daisy Makeig-Jones's glowing fantasy-scene lustre ware for Wedgwood, sold in the 1920s and withdrawn in 1929.","mk":"Wedgwood","y":"1915–1929","s":W+"Daisy_Makeig-Jones",
    "v":[V("Ghostly Wood covered Malfrey pot","Wedgwood","c. 1920"),V("Fairyland Sunset","Wedgwood"),V("Candlemas","Wedgwood")],
    "dt":"pattern · lustre colour · shape · repair"}]},
 {"n":"Asian art ceramics","a":"Chinese porcelain · Japanese ceramics · Korean ceramics","d":"Collectible ceramics of China, Japan and Korea, from imperial porcelain to tea wares and folk jars.",
  "t":["imperial reign mark","celadon","blue and white","famille verte or rose","tea bowl","export porcelain","studio revival piece"],
  "s":W+"Jingdezhen_porcelain",
  "x":[
   {"n":"Chinese imperial porcelain","a":"reign-mark porcelain · Jingdezhen imperial ware","d":"Court porcelain from the Jingdezhen imperial kilns, identified by reign marks first used under the Yongle Emperor.","mk":"","y":"1369–1850s","s":W+"Jingdezhen_porcelain",
    "v":[V("Imperial kilns at Zhushan","","1369","Hongwu reign"),V("Reign marks introduced","","1402–1424","Yongle reign"),V("Kangxi revival of the imperial kilns","","","six kilns, 23 workshops; famille verte then famille rose"),V("Official kilns destroyed in the Taiping Rebellion","","1850s")],
    "dt":"reign mark (can honour an earlier emperor) · palette · glaze · size"},
   {"n":"Longquan celadon","a":"Chinese celadon","d":"Jade-green glazed ware first made at Longquan in Zhejiang from the Northern Song, flourishing under the Southern Song.","mk":"","y":"from 960","s":W+"C%C3%A9ladony",
    "v":[V("Northern Song true celadon","","960–1127"),V("Imperial Longquan kilns closed","","mid-15th century","celadon out of fashion")],
    "dt":"glaze tone · crackle · kiln"},
   {"n":"Goryeo celadon","a":"Korean celadon · sanggam","d":"Korean celadon of the Goryeo period, with sanggam inlay of black or white clay.","mk":"","y":"10th–13th century","s":W+"C%C3%A9ladony",
    "v":[V("Glaze refinement","","10th–11th century"),V("Peak","","12th–early 13th century")],
    "dt":"inlay · form · provenance"},
   {"n":"Korean moon jar","a":"dalhangari","d":"Large round Joseon white porcelain jar, often thrown in two halves and joined at the middle.","mk":"","y":"late 1600s–mid 1700s","s":W+"Moon_jar",
    "v":[V("Joseon moon jar","","late 1600s–mid 1700s","about 20 survivors over 40 cm; three National Treasures"),V("Modern moon jars","Kim Se-yong","","also Shin Sang-ho, Kang Min-soo")],
    "dt":"height · seam · glaze tone"},
   {"n":"Raku tea bowl","a":"Raku chawan","d":"Hand-shaped, low-fired lead-glazed tea bowl from the Raku family, begun by Chōjirō for Sen no Rikyū in the 16th century.","mk":"Raku","y":"16th century onward","s":W+"Raku_ware",
    "v":[V("Chōjirō bowls","Raku","16th century"),V("Raku Kichizaemon XVI","Raku","","sixteenth generation"),V("Western raku","Paul Soldner","20th century","popularised in America")],
    "dt":"generation · glaze (red or black) · box inscription"},
   {"n":"Bizen ware","a":"Bizen-yaki","d":"Reddish-brown unglazed stoneware of Bizen, Okayama, one of the Six Ancient Kilns.","mk":"","y":"from the 6th century (believed)","s":W+"Six_Ancient_Kilns",
    "v":[V("Bizen in the tea ceremony","","")],
    "dt":"kiln marks · ash effects · form"},
   {"n":"Imari and Kakiemon porcelain","a":"Arita ware · Ko-Imari","d":"Arita porcelain shipped from Imari: early blue-and-white Ko-Imari and the Kakiemon enamel style.","mk":"","y":"17th–18th century","s":W+"Imari_ware",
    "v":[V("Arita kaolin discovered by Yi Sam-pyeong","","1616"),V("Kakiemon-style Imari","","c. 1700","about 50 years; dominated the European market"),V("Imari export peak","","1659–1740")],
    "dt":"palette · period · Dutch East India Company export"},
   {"n":"Satsuma ware","a":"export Satsuma","d":"Korean-influenced earthenware of c. 1600 that became ornate gilded enamel ware for Western export in the 19th century.","mk":"","y":"c. 1600; 19th century export","s":JP,
    "v":[V("Early Satsuma earthenware","","c. 1600"),V("19th-century export Satsuma","","19th century")],
    "dt":"enamel · gilding · signature · quality range"}]}
]
brands=[
 B("Leach Pottery","United Kingdom","1920","Artisan & independent","studio pottery","St Ives pottery founded by Bernard Leach and Shōji Hamada; Standard Ware 1946–1979.",W+"Leach_Pottery",["Leach Pottery Standard Ware"]),
 B("Moorcroft","United Kingdom","1913","Heritage manufactory","tubelined pottery","Burslem pottery founded by William Moorcroft in 1913.",W+"Moorcroft",["Moorcroft Florian Ware"]),
 B("Rookwood","United States","1880","Heritage manufactory","glazed art pottery","Cincinnati art pottery founded in 1880, closed 1967, revived 2004.",W+"Rookwood_pottery",["Rookwood Pottery glaze"]),
 B("Grueby","United States","1894","Artisan & independent","matte green glaze","Revere, Massachusetts art pottery, 1894–1920.",W+"Grueby_Faience_Company",["Grueby matte green vase"]),
 B("Martin Brothers","United Kingdom","1873","Artisan & independent","stoneware birds","London studio pottery of four brothers, 1873–1914.",W+"Martin_Brothers",["Martinware bird"]),
 B("Wedgwood","United Kingdom","1759","Heritage manufactory","jasperware, lustre","English pottery; Daisy Makeig-Jones's Fairyland Lustre debuted in 1915.","knowledge",["Wedgwood Fairyland Lustre"]),
 B("Raku","Japan","","Heritage manufactory","tea bowls","Family line of tea-bowl potters, now in its 16th generation.",W+"Raku_ware",["Raku tea bowl"])]
trad=[
 T("Mingei","Ceramics","Japan","1920s onward","Folk-craft movement of everyday objects by anonymous craftsmen, founded by Yanagi Sōetsu with Hamada and Kawai.","hand-thrown, natural glazes","local clay, ash",["Mashiko ware"],["Mashiko","Japan Folk Crafts Museum"],"Studio pieces by named potters vs anonymous folk ware",W+"Mingei"),
 T("Raku","Ceramics","Kyoto, Japan","16th century onward","Low-fired hand-shaped tea bowls made by the Raku family for the wabi tea ceremony.","hand-built, lead glaze, removed hot","clay",["Raku tea bowl"],["Raku family"],"Family generation and box inscription; Western raku is a separate studio technique",W+"Raku_ware"),
 T("Bizen","Ceramics","Okayama, Japan","from the 6th century (believed)","Reddish-brown unglazed stoneware of Bizen, one of the Six Ancient Kilns.","long wood firing","iron-rich clay",["Bizen ware"],["Bizen"],"Kiln effects, regional provenance",W+"Six_Ancient_Kilns"),
 T("Jingdezhen porcelain","Ceramics","Jingdezhen, Jiangxi, China","1369 onward (imperial kilns)","Chinese porcelain centre with court kilns from the Ming; reign marks from the Yongle reign.","wheel-thrown and painted porcelain","kaolin, porcelain stone",["Chinese imperial porcelain"],["Zhushan imperial kilns"],"Reign mark can honour an earlier emperor; later copies common",W+"Jingdezhen_porcelain"),
 T("Korean celadon","Ceramics","Korea","10th–13th century","Goryeo jade-green glazed ware with sanggam inlay.","inlaid clay, celadon glaze","clay",["Goryeo celadon","Korean moon jar"],[],"Provenance and technical analysis",W+"C%C3%A9ladony")]
notes="Old data empty. Built from retrieved Wikipedia pages. Left out: dinnerware and decor vases (other shelves), Kakiemon and Satsuma beyond the Japanese ceramics page, Hamada and Leach apprentices. Art pottery term comes from the Art pottery page. Wedgwood brand entered as knowledge."
json.dump({"kinds":kinds,"brands":brands,"traditions":trad,"notes":notes},open('work/F2/shelves/06_00.tmp','w'),ensure_ascii=False,indent=1)
os.rename('work/F2/shelves/06_00.tmp','work/F2/shelves/06_00.json')
