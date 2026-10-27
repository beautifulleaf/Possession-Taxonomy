import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/E2/agent')
from write import w
def X(n,a,d,mk,y,s,v=(),dt=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
BP="Bullpadel"; PF="https://www.padel.fyi/articles/bullpadel-padel-rackets-2023/"; BA="Babolat"; H="Head"; J="JOOLA"
padel={"n":"Padel racket","a":"padel bat · pala","d":"Solid, stringless perforated racket made for padel; sold with or without a cover.",
 "t":["round","teardrop","diamond","racket cover"],"s":"https://www.tenniswarehouse-europe.com/catpage-PADELBRA-EN.html",
 "x":[
  X("Bullpadel Vertex","Vertex","Bullpadel's diamond-shaped flagship line, with control and comfort variants.",BP,"",PF,
    [("Vertex 03",BP,"2023","diamond"),("Vertex 03 CTR",BP,"2022","round, control"),("Vertex 03 Comfort",BP,"2022","diamond, softer"),("Vertex 05",BP,"","")],"diamond · round CTR · Comfort"),
  X("Bullpadel Hack","Hack","Bullpadel's second diamond-shaped flagship, made with Paquito Navarro for agile attacking play.",BP,"",PF,
    [("Hack 03",BP,"2022","Paquito Navarro"),("Hack 03 Comfort",BP,"2022","")],"diamond"),
  X("adidas Metalbone","Metalbone","adidas power racket line played by Alejandro Galán.","adidas","","https://www.padelkiwi.com/en-us/blogs/kiwipedia/ale-galan-player-history",
    [("Metalbone 3.1","adidas","2022","Galán's titles of 2022"),("Metalbone 3.2","adidas","2023","Galán's titles of 2023")],""),
  X("Nox AT10 Genius","AT10","Agustín Tapia's signature Nox line in teardrop, round and diamond Attack versions.","Nox","","https://padelusa.com/pages/pros/agustin-tapia",
    [("AT10 Genius 18K Alum","Nox","","teardrop, Tapia's racket"),("AT10 Genius 12K Alum Xtreme Lite","Nox","","round"),("AT10 Genius Attack 18K Alum","Nox","","diamond"),("AT10 Luxury Genius 12K","Nox","2025","teardrop")],"18K / 12K carbon · teardrop, round, diamond"),
  X("Babolat Viper","Technical Viper","Babolat's attacking padel line and the official racket of Juan Lebrón.",BA,"","https://www.babolat.com/at/news-articles-blog-juan-lebron-racquet/juan-lebron-racquet.html",
    [("Technical Viper Juan Lebrón",BA,"2022","365 g, carbon"),("Technical Viper",BA,"",""),("Air Viper",BA,"",""),("Counter Viper",BA,"",""),("Viper Soft Juan Lebron",BA,"","")],""),
  X("Head Alpha","Alpha Pro","Head teardrop padel racket for advanced players, used by Sanyo Gutiérrez.",H,"","https://www.tennisnerd.net/?p=27335",
    [("Graphene 360+ Alpha Pro",H,"","teardrop, 375 g, power foam core")],"")],
 "m":[["Speed Pro",H],["Radical Pro",H],["Extreme Motion",H],["Arturo Coello Pro",H],["Diablo Pro","Siux"],["Trilogy Pro","Siux"],["Pegasus Pro","Siux"],
      ["Triton Power+","Starvie"],["Astrum+","Starvie"],["Drax+","Starvie"],["XPLO",BP],["Stima Spirit",BA],["Curva Speed","Tecnifibre"],["Bela V3","Wilson"],["Blade V4 padel","Wilson"],
      ["Pure Pro+","Oxdog"],["Arrow Hit","adidas"],["Standard Padel Cover","Wilson"]],
 "r":[["Head Radical",H],["Head Speed",H]]}
pball={"n":"Padel ball","a":"","d":"Pressurised felt ball made for padel, slightly less pressurised than a tennis ball.","s":"https://padelshop.com/en-be/collections/head-padel-balls/products/head-padel-pro-s-balls-box-24-x-3-pieces-padel-balls",
 "m":[["Padel Pro+",H]]}
paddle={"n":"Pickleball paddle","a":"","d":"Solid, flat-faced paddle made for pickleball.","t":["standard","elongated","widebody","hybrid","carbon fibre","fibreglass","wood"],
 "s":"https://www.pickleballwarehouse.com/_Top_Paddles_of_2025_/catpage-TOPPAD25PIC.html",
 "x":[
  X("JOOLA Perseus","Ben Johns Perseus","JOOLA carbon paddle line associated with Ben Johns.",J,"","https://pickleheads.com/pickleball-gear/pro-pickleball-paddles",
    [("Ben Johns Perseus CFS 16mm",J,"",""),("Ben Johns Perseus Pro IV",J,"","predecessor of Pro V"),("Perseus Pro V",J,"","")],"14–16 mm core"),
  X("JOOLA Hyperion","Ben Johns Hyperion","JOOLA carbon paddle line, offered as a sister shape to the Perseus.",J,"","https://www.gearpatrol.com/sports/a38568902/best-pickleball-paddles/",
    [("Ben Johns Hyperion 3S",J,"",""),("Simone Jardim Hyperion CFS 16mm",J,"",""),("Hyperion Pro V",J,"","")],"")],
 "m":[["Amped S2","Selkirk Sport"],["Power Air Invikta","Selkirk Sport"],["LABS Boomstik Elongated","Selkirk Sport"],["SLK ERA Power Elongated","Selkirk Sport"],
      ["Pursuit EX 6.0","Engage Pickleball"],["Alpha Pro","Engage Pickleball"],["Tempest Wave II","Paddletek"],["Bantam TKO-C","Paddletek"],["TruFoam Genesis 4","CRBN Pickleball"],
      ["C45 Carbon Fiber Hybrid","Franklin Sports"],["ALW C45 Aurelius","Franklin Sports"],["CX14 Elongated","Gearbox Pickleball"],["Radical Elite",H],["Graphite Z5","Onix"],
      ["Double Black Diamond","Six Zero Pickleball"],["Aura Pro","Friday"]],
 "r":[["LABS","Selkirk Sport"],["SLK ERA","Selkirk Sport"],["Six Zero Coral","Six Zero Pickleball"]]}
pkball={"n":"Pickleball ball","a":"","d":"Perforated plastic ball made for pickleball.","t":["indoor","outdoor"],"s":"https://www.pickleballwarehouse.com/Franklin_Pickleball_Balls/catpage-TPFRPB.html",
 "m":[["X-40 Outdoor","Franklin Sports"],["X-26 Indoor","Franklin Sports"],["Fast-40","Dura"],["LT Pro 48","Life Time"],["Fuse Indoor","Onix"],["Fuse G2 Outdoor","Onix"],["Pro S1","Selkirk Sport"],["Photon Indoor","Gamma"]],
 "r":[["Franklin X","Franklin Sports"]]}
pshoe={"n":"Pickleball shoe","a":"","d":"Court shoe sold as a performance model with a pickleball-specific sole. An everyday sneaker is in Footwear.","s":"https://runrepeat.com/catalog/head-tennis-shoes"}
def B(n,c,f,seg,kf,d,s="knowledge",**kw):
    b={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d}; b.update(kw); b["s"]=s; return b
brands=[B(BP,"Spain","1995","Specialist","padel rackets","Padel-only brand founded by padel professionals; owned by Aguirre y Cía since 2015.",s=PF,lines=["Vertex","Hack","Ionic","Elite","Flow"],sig=["Bullpadel Vertex","Bullpadel Hack"]),
 B("Nox","Spain","","Specialist","padel rackets","Spanish padel brand known for Agustín Tapia's AT10 rackets.",lines=["AT10"],sig=["Nox AT10 Genius"]),
 B("adidas","Germany","1949","Mainstream","sportswear","German sportswear maker with a padel racket range.",lines=["Metalbone"],sig=["adidas Metalbone"]),
 B(BA,"France","1875","Specialist","strings & rackets","Lyon racket-sports maker with tennis and padel lines.",lines=["Viper"],sig=["Babolat Viper"]),
 B(H,"Austria","1950","Specialist","rackets & skis","Sports-equipment maker with tennis and padel rackets.",lines=["Alpha","Speed","Radical","Extreme"],sig=["Head Alpha"]),
 B(J,"Germany","","Mainstream","table tennis & pickleball","German table tennis brand with a leading pickleball paddle range.",lines=["Perseus","Hyperion"],sig=["JOOLA Perseus","JOOLA Hyperion"]),
 B("Selkirk Sport","United States","","Specialist","pickleball paddles","American pickleball paddle maker.",lines=["Vanguard","LABS","SLK","Amped"]),
 B("Franklin Sports","United States","","Mainstream","pickleball balls","American sporting-goods maker whose X-40 is a standard outdoor pickleball.",lines=["X-40"])]
w('E2','02_03',{"kinds":[padel,pball,paddle,pkball,pshoe],"brands":brands,"traditions":[],
 "notes":"Padel racket cut from 47 flat SKUs to 6 archetypes (Bullpadel Vertex, Hack; adidas Metalbone; Nox AT10 Genius; Babolat Viper; Head Alpha) plus 18 flat models; Padel racket cover merged in as t 'racket cover' with the Wilson cover kept in m. Dropped Babolat Air Vertuo, Veron Juan Lebron; Head Evo Extreme, Evo Speed, Flash Pro, Gravity Team, Radical Motion, Radical Team, Speed One, Speed One X, Speed Pro X, Vibe, Zephyr UL; Oxdog Hyper/Ultimate Woman Air; Siux Astra Hybrid, Fenix Pro, Trilogy Elite; Starvie Black Titan, Phantom; Tecnifibre Curva Soft; Wilson Defy Pro SE; adidas old 'Metalbone' (now archetype). Head Delta not added: the only page found (padelcentrum.nl) was blocked. Maker 'Wilson Sporting Goods' normalised to 'Wilson'. Pickleball paddle: JOOLA Perseus and Hyperion archetypes; others flat (Selkirk, Engage, Paddletek, CRBN, Franklin, Gearbox, Head, Onix, Six Zero, Friday); dropped GX2 Power Hybrid, Six Zero Coral models, Black Opal, Andre Agassi Pro IV, Boomstik Widebody, SLK ERA Widebody. Pickleball ball: added Dura Fast-40, Life Time LT Pro 48, Onix Fuse, Selkirk Pro S1, Gamma Photon. Pickleball shoe kept without models. Onix Pure 2 not added (search snippet only)."})
