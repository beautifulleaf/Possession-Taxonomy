import json, os
W='https://en.wikipedia.org/wiki/'
SS='https://thesolesupplier.co.uk/news/the-history-of-vans/'
def X(n,d,mk,y,s,v=(),dt='',a=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
skate={"n":"Skate shoe","a":"skateboarding shoe · skate sneaker","d":"Shoe with a durable upper and flat grip sole made for skateboarding.",
 "t":["vulcanised sole","cupsole","low-top","mid-top","high-top","suede upper","canvas upper"],
 "s":"https://sneakerhistory.com/skate-shoe-brands/",
 "x":[
  X("Era","Low-top canvas lace-up with padded collar, the first shoe Vans made for skateboarders.","Vans","1976",SS,
    [("Style 95","Vans","mid-1970s","original number; designed with Tony Alva and Stacy Peralta")],"canvas or suede · colourways",a="Style 95 · #95"),
  X("Old Skool","Low-top skate shoe with leather panels and the first Vans side stripe.","Vans","1977",SS,
    [("Style 36","Vans","1977","original number; debut of the 'jazz stripe'")],"canvas and suede · colourways · checkerboard prints",a="Style 36 · #36"),
  X("Sk8-Hi","High-top version of the side-stripe skate shoe, cut high for ankle protection.","Vans","1978",SS,[],
    "canvas and suede · colourways",a="Style 38"),
  X("Half Cab","Mid-top Steve Caballero pro model with padded tongue and double-stitched suede upper.","Vans","1992",SS,
    [("Half Cab","Vans","1992","mid-top counterpart to the high-top Caballero")],"suede · colourways"),
  X("SB Dunk","Skateboarding version of the Nike Dunk with padded tongue and collar and Zoom Air insole.","Nike","2002",W+"Nike_SB",
    [("SB Dunk Low","Nike","2002","launched with Nike SB"),("Dunk Low Pro SB 'Tiffany'","Nike","2005",""),
     ("Staple 'NYC Pigeon' Dunk Low","Nike","2005","release caused a riot"),("Ben & Jerry's 'Chunky Dunky'","Nike","2020","collaboration")],
    "low · mid · high · collaboration colourways",a="Nike SB Dunk · Dunk SB"),
  X("Accel","Base skate model from éS with reinforced ollie area; Tom Penny's de facto shoe.","éS","1995","https://esskateboarding.com/pages/designing-the-accel",
    [("Accel (original)","éS","1995","designed by Pierre André Sénizergues; dropped mid-2000s"),("Accel OG","éS","mid-2000s","bulkier update, returned 2014"),
     ("Accel Slim","éS","c. 2015","")],"suede · colourways"),
  X("D3","Skate shoe designed by pro skater Dave Mayhew; his third Osiris model.","Osiris","late 1990s",
    "https://nssmag.com/en/fashion/14991/the-story-of-osiris-d3-and-the-return-of-the-skate-shoe",[],"colourways"),
  X("Skytop","High-top skate shoe, Chad Muska's first Supra signature model.","Supra","2007","https://www.complex.com/sneakers/a/brandon-edler/the-complete-history-of-the-supra-skytop",
    [("Skytop","Supra","2007","co-designed by Chad Muska, Angel Cabada and Josh Brubaker"),("Skytop II","Supra","",""),
     ("Skytop III","Supra","2011","lower mid-top"),("Skytop IV","Supra","2013","removable collar")],"colourways"),
  X("Busenitz","Dennis Busenitz pro model based on the adidas Copa Mundial football boot.","adidas","2006",
    "https://www.complex.com/sneakers/a/gerald-flores/adidas-busenitz-samples",
    [("Busenitz Pro","adidas","","cupsole original"),("Busenitz Vulc","adidas","","vulcanised version"),("Busenitz Pure Boost","adidas","2016","10th-anniversary pack, Boost midsole")],
    "suede · colourways"),
 ],
 "m":[["CTAS Pro","Converse"],["One Star Pro","Converse"],["Reynolds","Emerica"]]}
slip={"n":"Slip-on sneaker","a":"laceless sneaker","d":"Laceless athletic-style shoe with elastic panels or a stretch collar.",
 "s":"https://www.footlocker.com/product/vans-classic-slip-on-mens/0011999.html",
 "x":[X("Classic Slip-On","Laceless canvas sneaker with elastic side gores and waffle sole; the originating slip-on sneaker.","Vans","1977",SS,
    [("Style 98","Vans","1977","original number"),("Checkerboard Slip-On","Vans","","worn by Jeff Spicoli in Fast Times at Ridgemont High")],
    "canvas · checkerboard and other prints · colourways",a="Style 98 · #98")]}
des={"n":"Designer sneaker","a":"luxury sneaker · minimalist sneaker","d":"Sneaker from a fashion house or design-led label, sold at luxury prices.",
 "t":["minimalist leather","chunky / dad","high-top","low-top"],"s":W+"Common_Projects",
 "x":[
  X("Achilles Low","Minimal low-top leather sneaker with gold-foil style, size and colour numbers on the heel.","Common Projects","",W+"Common_Projects",[],
    "Italian Nappa leather, suede · white, black, colours · low and mid"),
  X("Triple S","Chunky trainer on a stacked sole unit by Demna Gvasalia.","Balenciaga","2017",
    "https://collections.vam.ac.uk/item/O1504106/shoes-demna-gvasalia",
    [("Triple S first drop","Balenciaga","2017","shown in Paris January 2017, on sale September; designed by Demna Gvasalia")],"colourways"),
  X("Super-Star","Sneaker with a deliberately distressed, vintage finish and star logo.","Golden Goose","2007",W+"Golden_Goose_Deluxe_Brand",[],
    "star colours · distressing"),
  X("Geobasket","Rick Owens high-top sneaker that replaced his earlier Dunk.","Rick Owens","",W+"Rick_Owens",
    [("Dunk","Rick Owens","2005","predecessor, shown in Moog FW05")],"leather · black, white · high-top"),
  X("Replica","Shoes from Maison Margiela's Replica line, which reproduces existing designs.","Maison Margiela","1994",W+"Maison_Margiela",[],
    "line 22 · leather, suede · colourways"),
  X("Oversized","Low-top sneaker on an oversized midsole.","Alexander McQueen","2015","https://stockx.com/news/a-perfect-fit-alexander-mcqueen-oversized/",
    [("Oversized (men's)","Alexander McQueen","2015","Spring/Summer collection"),("Oversized (women's)","Alexander McQueen","","added later")],"colourways"),
  X("LV Trainer","Luxury trainer by Virgil Abloh from his first Louis Vuitton collection, made in Italy.","Louis Vuitton","2018","https://www.houyhnhnm.jp/en/news/306688/",
    [("LV Trainer","Louis Vuitton","SS 2019","Abloh's debut collection"),("LV Trainer Hi-Top city edition","Louis Vuitton","","limited, nine city colours")],"low and high · colourways"),
  X("B23","High-top sneaker introduced in Kim Jones's debut Dior men's collection.","Dior","2018","https://www.papermag.com/dior-men-b27-sneaker",
    [],"high-top · colourways"),
  X("B27","Low- and high-top Oblique sneaker drawing on 1980s tennis and skate shoes.","Dior","2020","https://www.papermag.com/dior-men-b27-sneaker",
    [],"Oblique jacquard or perforated leather · white, black, grey"),
  X("Ace","Sneaker line defined by Gucci's green-red-green Web stripe.","Gucci","","https://www.houyhnhnm.jp/en/news/89992/",
    [("Ace with patches","Gucci","","tiger, cat and bee patches under Alessandro Michele")],"Web stripe · patches, embroidery, studs"),
 ]}
K="knowledge"
def B(n,c,f,seg,d,s,sig=(),eras=(),rel=()):
    b={"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":[],"eras":list(eras),"sig":list(sig),"sc":[],"rel":list(rel),"s":s}
    return b
brands=[
 B("Vans","United States","1966","Skate and casual footwear","Founded in Anaheim, California, as the Van Doren Rubber Company.",W+"Vans",["Era","Old Skool","Sk8-Hi","Half Cab","Classic Slip-On"]),
 B("Nike","United States","1964","Athletic footwear and apparel","Sportswear company whose skateboarding line is Nike SB (2002).",K,["SB Dunk"]),
 B("adidas","Germany","1949","Athletic footwear and apparel","German sportswear company with a skateboarding programme.",K,["Busenitz"]),
 B("Converse","United States","1908","Canvas and athletic footwear","American shoe company owned by Nike.",K,[],[],["Nike"]),
 B("éS","United States","","Skate footwear","Skate shoe brand begun by Pierre André Sénizergues as a breakaway from etnies; part of Sole Technology.","https://esskateboarding.com/pages/designing-the-accel",["Accel"],[],["Etnies","Emerica"]),
 B("Emerica","United States","1996","Skate footwear","Skate shoe brand of Sole Technology, sold to Nidecker Group in 2024.",W+"Emerica",[],[],["Etnies","éS"]),
 B("Etnies","France","1986","Skate footwear","Skate shoe brand founded in France and developed in Southern California.",W+"Etnies",[],[],["éS","Emerica"]),
 B("DC Shoes","United States","1994","Skate footwear","Skate shoe brand founded by Damon Way, Ken Block and Clayton Blehm; owned by Authentic Brands Group.",W+"DC_Shoes"),
 B("Osiris","United States","","Skate footwear","Skate shoe brand known for Dave Mayhew's D3.","https://nssmag.com/en/fashion/14991/the-story-of-osiris-d3-and-the-return-of-the-skate-shoe",["D3"]),
 B("Supra","United States","","Skate and lifestyle footwear","Footwear brand founded by Angel Cabada with pro skater Chad Muska.","https://www.complex.com/sneakers/a/brandon-edler/the-complete-history-of-the-supra-skytop",["Skytop"]),
 B("Common Projects","United States","2004","Minimalist designer sneakers","Founded by Prathan Poopat and Flavio Girolami; shoes made in Italy.",W+"Common_Projects",["Achilles Low"]),
 B("Golden Goose","Italy","2000","Luxury distressed sneakers","Founded in Marghera near Venice by Alessandro Gallo and Francesca Rinaldo.",W+"Golden_Goose_Deluxe_Brand",["Super-Star"]),
 B("Balenciaga","Spain","1919","Luxury fashion house","Founded in San Sebastián by Cristóbal Balenciaga, later based in Paris.",W+"Balenciaga",["Triple S"],
   ["Cristóbal Balenciaga, 1919–1968","Nicolas Ghesquière, 1997–2012","Alexander Wang, 2013–2015","Demna Gvasalia, 2015–2025","Pierpaolo Piccioli, 2025–"]),
 B("Rick Owens","United States","1994","Avant-garde designer fashion","Designer label launched in Los Angeles by Rick Owens.",W+"Rick_Owens",["Geobasket"]),
 B("Maison Margiela","France","1988","Luxury fashion house","Founded in Paris by Martin Margiela and Jenny Meirens.",W+"Maison_Margiela",["Replica","Tabi"],
   ["Martin Margiela, 1988–2009","John Galliano, 2014–2024","Glenn Martens, 2025–"]),
 B("Alexander McQueen","United Kingdom","1992","Luxury fashion house","British luxury fashion house founded by Lee Alexander McQueen.",K,["Oversized"]),
 B("Louis Vuitton","France","1854","Luxury fashion house","French luxury house; Virgil Abloh was men's artistic director from 2018.",K,["LV Trainer"]),
 B("Dior","France","1946","Luxury fashion house","French couture house; Kim Jones designed menswear from 2018.",K,["B23","B27"]),
 B("Gucci","Italy","1921","Luxury fashion house","Italian luxury house founded in Florence.",K,["Ace"]),
]
notes=("Vans Authentic left to the canvas-sneaker shelf (cross-ref). Left out for lack of a retrieved page: Balenciaga Speed Trainer; "
 "Margiela GAT lineage (Replica sourced only as the 1994 line 22); launch years for Achilles, Geobasket, Gucci Ace and Osiris D3. "
 "Emerica Reynolds and Converse CTAS Pro / One Star Pro kept as flat models (no retrieved history). DC Shoes and Etnies in the brand register only (no model pages retrieved). "
 "vans.com, louisvuitton.com, behance and flightclub returned 403; not retried.")
out={"kinds":[skate,slip,des],"brands":brands,"traditions":[],"notes":notes}
p='work/A2/shelves/00_02.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
