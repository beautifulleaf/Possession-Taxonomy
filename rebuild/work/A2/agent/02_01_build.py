import json, os
SL='https://en.wikipedia.org/wiki/Slip-on_shoe'
EG='https://www.edwardgreen.com/node/254'
def A(n,a,d,mk,y,s,v=(),dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),x)) for x in v],"dt":dt}
loafer={"n":"Loafer","a":"slip-on loafer · moccasin loafer","d":"Laceless low shoe with a moccasin-style apron toe and a closed heel, slipped on without fastening.",
 "t":["unlined","lined","calf","suede","shell cordovan","hand-sewn moccasin","Goodyear-welted","side-gored dress loafer"],
 "s":SL,
 "x":[A("Penny loafer","Weejun · saddle loafer","Loafer with a leather saddle strap across the vamp cut with a slit or diamond said to hold a penny.","G.H. Bass","1936",SL,
   [("Weejun","G.H. Bass","1936","Originating penny loafer from Wilton, Maine"),("Leavitt Penny","G.H. Bass","1993","Classic Penny in the Weejuns collection renamed"),
    ("Weejun Larson","G.H. Bass","",""),("986 Leisure Handsewn","Alden","","Van last, shell cordovan Color 8"),
    ("Piccadilly","Edward Green","","184 loafer last"),("180 Mocassin","J.M. Weston","","Weston's classic penny loafer")],
   "leather: calf, suede, shell cordovan · lined or unlined · last and toe shape · sole: leather or rubber"),
  A("Horsebit loafer","Gucci loafer","Loafer with a metal horsebit across the vamp, which took the loafer into formal wear.","Gucci","1953","https://www.gentlemansgazette.com/is-it-worth-gucci-loafers/",
   [("Horsebit 1953","Gucci","1953","Original black loafer without visible logos"),("Jordaan","Gucci","","Slimmer current version"),("Brixton","Gucci","","Collapsible soft heel")],
   "calf, suede, crocodile · black, brown, navy · gold or silver-tone bit"),
  A("Tassel loafer","tasselled loafer","Loafer trimmed with a lace round the collar ending in tassels on the vamp.","Alden","1957",SL,
   [("663 Tassel Loafer","Alden","","Aberdeen last, burgundy calf"),("Belgravia","Edward Green","","184 last, plaited trim"),("Greenwich","Edward Green","","Plain trim, often cordovan")],
   "calf, suede, cordovan · plain or plaited trim · last"),
  A("Belgian loafer","Belgian shoe","Soft hand-stitched loafer sewn inside out with a fine seam and a small bow on the vamp.","Belgian Shoes","1955","https://en.wikipedia.org/wiki/Belgian_Shoes",
   [],"suede, calf, velvet · bow or tassel · many colours"),
  A("Kiltie loafer","kiltie","Loafer with a fringed kilt-style flap over the vamp, tied with a leather string or tassels.","","1950s",SL,[],"calf, suede · fringe colour · tassel or bow tie"),
  A("Aurland shoe","Aurland moccasin · Norwegian moccasin","Norwegian slip-on with a raised seam on the upper and a narrow cutout on the saddle, an early loafer forerunner.","","about 1908",SL,[],"leather colour · sole"),
  A("Wildsmith loafer","Harrow · 582","London slip-on with a serrated seam, reinforced toe box and vertical toe stitching, made as a country-house shoe.","Wildsmith Shoes","1926",SL,
   [("582","Wildsmith Shoes","1926","Original model number")],"calf leather · colour")],
 "m":[["Tiverton","Church's"],["Polperro","Edward Green"],["Bradley","George Cleverley"],["Hendra","John Lobb"],["Brighton","Loake"],["Princeton","Loake"],["Reims","Paraboot"]]}
moc={"n":"Moccasin & driving shoe","a":"moccasin · moc · driving moc · camp moc","d":"Soft shoe whose sole wraps up to form the sides, closed by a plug or apron at the toe; includes driving and camp mocs.",
 "t":["soft sole","rubber-pebble driving sole","lug or crepe sole","unlined","suede","fringed","beaded"],
 "s":"https://en.wikipedia.org/wiki/Moccasin",
 "x":[A("Driving moccasin","driving moc · car shoe","Moccasin loafer whose sole is studded with small rubber nubs that wrap up the heel for grip on pedals.","Car Shoe","1963","https://en.wikipedia.org/wiki/The_Original_Car_Shoe",
   [("Car Shoe driving moccasin","Car Shoe","1963","Patented by Gianni Mostile"),("Gommino","Tod's","1979","Suede pebble-sole loafer, Tod's flagship"),
    ("P.W. Driving Moc","Minnetonka","",""),("Westbrook Driving Moc","Rancourt & Co.","",""),("Camp Driver","Quoddy","","")],
   "suede, calf · pebble pattern · penny strap, tassel or bit · colours"),
  A("Camp moccasin","camp moc","Hand-sewn moccasin with a leather lace running through the collar and plug, on a rubber sole.","L.L.Bean","1936","https://www.rancourtandcompany.com/blogs/blog/a-history-of-our-most-famous-shoe",
   [("Gilman Camp-Moc","Rancourt & Co.","","Unlined Horween Chromexcel, polyurethane sole")],"unlined full-grain leather · sole colour · lace"),
  A("Wallabee","Wallabee moccasin","Crepe-soled moccasin shoe based on the Sioux Grasshopper, in low and boot heights.","Clarks","1967","https://en.wikipedia.org/wiki/Wallabee",
   [("Wallabee","Clarks","1967","Made at Padmore and Barnes, Kilkenny")],"suede or leather · low or boot · crepe sole · colours"),
  A("Soft-sole moccasin","house moccasin","Unstructured one-piece moccasin with a soft leather sole, often fringed or beaded, worn indoors and out.","","","https://en.wikipedia.org/wiki/Moccasin",
   [("Classic Moc","Minnetonka","",""),("Thunderbird Animikii","Minnetonka","",""),("Pile Lined Softsole","Minnetonka","","")],"suede or deerskin · fringe, beads · lined or unlined")],
 "m":[["Campsides","Sebago"]]}
boat={"n":"Boat shoe","a":"deck shoe · top-sider","d":"Low leather or canvas shoe with a siped non-marking sole, usually with a leather lace running round the upper.",
 "t":["2-eye","3-eye","1-eye","canvas","leather","loafer style"],"s":"https://en.wikipedia.org/wiki/Boat_shoe",
 "x":[A("Sperry Authentic Original","Top-Sider · A/O","The first boat shoe: moccasin upper with rawhide lace and a siped sole cut to grip a wet deck.","Sperry","1935","https://en.wikipedia.org/wiki/Sperry_(brand)",
   [("Authentic Original 2-Eye","Sperry","","Classic two-eyelet version"),("1-Eye","Sperry","",""),("Authentic Original Harbor Loafer","Sperry","","Laceless loafer version"),("Gold Cup","Sperry","","Premium range")],
   "leather or canvas · eyelets · colours · white or gum sole"),
  A("Sebago Docksides","Docksides","Hand-sewn moccasin boat shoe that became a 1980s campus fashion staple.","Sebago","","https://en.wikipedia.org/wiki/Sebago_(company)",[],"leather colour · sole"),
  A("Timberland 3-Eye Classic Lug","3-Eye Lug","Hand-sewn leather boat shoe with three eyelets, 360° rawhide lacing and a rubber lug sole.","Timberland","","https://www.stuartslondon.com/en-au/products/timberland-3-eye-classic-lug-shoe-mid-brown",[],"full-grain leather · colourways · collaborations")]}
eve={"n":"Evening slipper","a":"dress slipper · smoking slipper · formal pump","d":"Light low formal slip-on worn with evening dress or at home, such as the velvet Albert slipper and patent opera pump.",
 "t":["velvet","patent leather","embroidered crest or motif","quilted silk lining","grosgrain bow"],
 "s":"https://www.thefield.co.uk/country-house/luxury-country-house/luxury-dress-slippers-25107",
 "x":[A("Albert slipper","Prince Albert slipper · velvet slipper","Velvet slip-on with a quilted lining and leather sole, often embroidered, named after Queen Victoria's consort.","","19th century","https://www.thefield.co.uk/country-house/luxury-country-house/luxury-dress-slippers-25107",
   [("Albert dress slipper","Bowhill & Elliott","","Made to order or ready-to-wear, Norwich"),("Lion Rampant","Crockett & Jones","","Black velvet"),("Velvet slipper","Stubbs & Wootton","","Cotton velvet, grosgrain trim, made in Spain")],
   "velvet colour · embroidery or monogram · lining silk · sole"),
  A("Opera pump","opera slipper · evening pump","Low-vamp whole-cut shoe in patent leather with a grosgrain bow, worn with white tie.","","late 18th century","https://en.wikipedia.org/wiki/Court_shoe",
   [],"patent or calf · pinched or flat bow · quilted silk or leather lining · glued or sewn sole")]}
B=[]
def b(n,c,f,seg,d,lines,sig,s,rel=()):
    B.append({"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":lines,"eras":[],"sig":sig,"sc":[],"rel":list(rel),"s":s})
b("G.H. Bass","United States","1876","American heritage","Wilton, Maine shoemaker founded by George Henry Bass, originator of the Weejun penny loafer.",["Weejuns"],["Penny loafer"],"https://en.wikipedia.org/wiki/G.H._Bass",["Sebago"])
b("Gucci","Italy","1921","luxury fashion house","Florentine luxury house whose 1953 horsebit loafer is its signature shoe.",["Horsebit 1953","Jordaan","Brixton"],["Horsebit loafer"],"knowledge")
b("Alden","United States","1884","heritage Goodyear-welted","Middleborough, Massachusetts shoemaker founded by Charles H. Alden; co-creator of the tassel loafer.",["986 Leisure Handsewn","663"],["Tassel loafer"],"https://en.wikipedia.org/wiki/Alden_Shoe_Company")
b("Edward Green","United Kingdom","1890","Northampton bench-made","Northampton maker of Goodyear-welted shoes; its 184 loafer last carries the Piccadilly and Belgravia.",["Piccadilly","Belgravia","Greenwich"],[],EG,["Crockett & Jones","Church's"])
b("J.M. Weston","France","1891","French luxury","Limoges shoemaker known for the 180 penny loafer.",["180 Mocassin","677 Chasse"],[],"https://en.wikipedia.org/wiki/J._M._Weston")
b("Church's","United Kingdom","1873","Northampton Goodyear-welted","Northampton shoemaker owned by Prada.",[],[],"knowledge",["Car Shoe"])
b("Belgian Shoes","United States","1955","hand-stitched loafers","Manhattan shop founded by Henri Bendel selling bow-trimmed loafers made in Izegem, Belgium.",[],["Belgian loafer"],"https://en.wikipedia.org/wiki/Belgian_Shoes")
b("Wildsmith Shoes","United Kingdom","","London bespoke","London shoemaker whose 1926 model 582 is an early loafer.",["582"],["Wildsmith loafer"],SL)
b("Car Shoe","Italy","1963","luxury driving shoes","Milan brand founded by Gianni Mostile, who patented the rubber-nubbed driving moccasin; owned by Prada since 2001.",[],["Driving moccasin"],"https://en.wikipedia.org/wiki/The_Original_Car_Shoe",["Tod's","Church's"])
b("Tod's","Italy","1920","Italian luxury","Della Valle family firm from the Marche whose 1979 Gommino is its flagship; sister brands Hogan and Fay.",["Gommino"],[],"https://en.wikipedia.org/wiki/Tod%27s",["Car Shoe"])
b("L.L.Bean","United States","1912","outdoor outfitter","Freeport, Maine outfitter whose founder Leon Leonwood Bean introduced the camp moccasin in 1936.",[],["Camp moccasin"],"knowledge",["Rancourt & Co."])
b("Rancourt & Co.","United States","","hand-sewn moccasins","Maine family shoemaker that has hand-sewn camp-mocs since 1967.",["Gilman Camp-Moc","Westbrook Driving Moc"],[],"https://www.rancourtandcompany.com/blogs/blog/a-history-of-our-most-famous-shoe",["L.L.Bean"])
b("Clarks","United Kingdom","1825","mainstream and Originals","Somerset shoemaker C. & J. Clark, maker of the Desert Boot and Wallabee.",["Originals"],["Wallabee"],"knowledge")
b("Minnetonka","United States","1946","moccasins","Minneapolis family firm that began as a souvenir business and became a moccasin maker.",["Classic Moc","Thunderbird"],[],"https://www.themodestman.com/minnetonka-brand-review/")
b("Sperry","United States","1935","boat shoes","Brand of Paul A. Sperry, inventor of the siped boat shoe; owned by Authentic Brands Group.",["Authentic Original","Gold Cup"],["Sperry Authentic Original"],"https://en.wikipedia.org/wiki/Sperry_(brand)",["Sebago","Timberland"])
b("Sebago","United States","1946","boat shoes and moccasins","Maine-founded maker of Docksides boat shoes and Campsides mocs, owned by BasicNet since 2017.",["Docksides","Campsides"],["Sebago Docksides"],"https://en.wikipedia.org/wiki/Sebago_(company)",["Sperry"])
b("Timberland","United States","1973","outdoor footwear","New Hampshire outdoor brand known for the yellow boot and 3-Eye boat shoe; owned by VF Corporation.",["3-Eye Classic Lug"],["Timberland 3-Eye Classic Lug"],"knowledge",["Sperry"])
b("Bowhill & Elliott","United Kingdom","1874","dress slippers","Norwich slipper maker specialising in Albert dress slippers, run by a descendant of the founder.",[],["Albert slipper"],"https://www.thefield.co.uk/country-house/luxury-country-house/luxury-dress-slippers-25107",["Stubbs & Wootton"])
b("Stubbs & Wootton","United States","1993","velvet slippers","Palm Beach brand founded by Percy Steinhart making velvet evening slippers in Spain.",[],[],"https://store.metmuseum.org/blog/the-velvet-touch-stubbs-and-wootton-slippers-at-the-met",["Bowhill & Elliott"])
b("Crockett & Jones","United Kingdom","1879","Northampton Goodyear-welted","Northampton shoemaker that also makes velvet Albert slippers.",["Lion Rampant"],[],"knowledge",["Edward Green"])
out={"kinds":[loafer,moc,boat,eve],"brands":B,"traditions":[],
 "notes":"Dissolved the 'Plain slip-on shoe' catch-all into Evening slipper (Albert slipper, opera pump); TOMS Alpargata belongs with Espadrille on the Mules, clogs & espadrilles shelf. Venetian/plain-vamp loafer left out (no retrieved page with details). Alden 563 not confirmed; Alden 663 tassel used instead. Del Toro, Quoddy and Eastland had no retrieved page (Quoddy kept only as old-data version). Old loafer models without a confirmed archetype stay in m. Timberland 3-Eye and Sebago Docksides years not confirmed, left blank. Parallel fetch unavailable (402); WebFetch used."}
p='work/A2/shelves/02_01.json'; os.makedirs('work/A2/shelves',exist_ok=True)
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
