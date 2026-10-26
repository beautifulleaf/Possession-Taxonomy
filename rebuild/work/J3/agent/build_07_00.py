import json, os
W="https://en.wikipedia.org/wiki/"
def X(n,a,d,mk,y,s,v=(),dt=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
kinds=[
 {"n":"Tofu","a":"bean curd · doufu · 豆腐 · dubu","d":"Soy milk curdled and pressed into white blocks, from soft silken to firm, sold fresh, fried, dried or fermented.",
  "t":["silken (kinugoshi)","soft","firm (momen)","extra-firm (dougan)","thousand-layer sheet (baiye)","smoked","marinated","thick fried (atsuage)","thin fried pouch (aburaage)","frozen (kōri-dōfu)","freeze-dried","fresh chilled","aseptic shelf-stable","organic"],
  "s":W+"Tofu",
  "x":[
   X("Aseptic silken tofu","Mori-Nu","Silken tofu sealed in an aseptic carton so it keeps unrefrigerated until opened.","Mori-Nu","1985","https://well.ca/brand/mori-nu.html",
     [("Soft Silken Tofu","Mori-Nu","",""),("Firm Silken Tofu","Mori-Nu","",""),("Extra Firm Silken Tofu","Mori-Nu","","")],"firmness · carton about 300 g"),
   X("Smoked tofu","","Firm tofu smoked after pressing, eaten sliced or fried.","Taifun","","https://www.taifun-tofu.de/en",
     [("Smoked Tofu Classic","Taifun","",""),("Smoked Tofu Almonds & Sesame","Taifun","","")],"smoke · added nuts, seeds or herbs"),
   X("Kōya-dōfu","koya-dofu · freeze-dried tofu","Freeze-dried tofu from Mount Kōya, rehydrated before cooking.","","","https://en.wikipedia.org/wiki/Tofu",
     [("Shimidōfu","","","sun-dried frozen tofu of the Tōhoku region")],"block size · dried or rehydrated"),
   X("Fermented bean curd","furu · fǔrǔ · sufu · preserved tofu · tofu cheese","Cubes of tofu air-dried, fermented and kept in brine, rice wine or chilli; a condiment.","","","https://en.wikipedia.org/wiki/Fermented_bean_curd",
     [("White fermented bean curd","","","most common; rice-wine and salt brine, with or without chilli or sesame oil"),("Red fermented bean curd (nanru)","","","coloured with red yeast rice"),("Rose red fermented bean curd","Wangzhihe","",""),("Tofuyo","","","Okinawan red type pickled in awamori"),("Tofu misozuke","","","Japanese, aged in miso")],"white or red · chilli · jar size"),
   X("Stinky tofu","chòu dòufu","Tofu fermented in a vegetable and fish brine, strong-smelling and mild-tasting, usually fried.","","Qing dynasty (legend)","https://en.wikipedia.org/wiki/Stinky_tofu",
     [("Changsha black stinky tofu","","","Hunan; brine of bamboo shoots, koji and shiitake"),("Taiwanese fried stinky tofu","","","night-market style with pickled cabbage"),("Taiwanese steamed stinky tofu","","","most pungent"),("Shenkeng barbecued stinky tofu","","","skewered over charcoal")],"regional brine · fried, steamed or grilled"),
  ],
  "m":[["Plain Firm Tofu","Taifun"],["Extra Firm Plant-Based Tofu","Cauldron"],["Smoky BBQ Grillable Tofu","Cauldron"]]},
 {"n":"Tempeh","a":"tempe","d":"Indonesian cake of soybeans or other legumes bound together by a Rhizopus mould during fermentation.",
  "t":["soy","plain","marinated","leaf-wrapped","plastic-wrapped","fresh","frozen","pasteurised"],
  "s":W+"Tempeh",
  "x":[
   X("Soy tempe","tempe kedelai","Whole hulled soybeans fermented with Rhizopus into a firm white-bound cake; the original Javanese form.","","by about 1700","https://en.wikipedia.org/wiki/Tempeh",
     [("Tempe gódhóng","","","wrapped in teak or waru leaves"),("Tempe murni","","","plain, made in plastic wrap"),("Tempe semangit","","","aged, pungent"),("Tempe mondhol, wayu and bosok","","","named stages of maturity")],"wrapping · maturity"),
   X("Tempe gembus","","Tempeh made from soy pulp or tofu dregs.","","","https://en.wikipedia.org/wiki/Tempeh",[],""),
   X("Oncom","","West Javanese ferment of peanut press cake or soy dregs, related to tempeh.","","","https://en.wikipedia.org/wiki/Tempeh",[],"red or black mould"),
   X("Tempe menjes kacang","","Malang tempeh made with peanut dregs and other ingredients.","","","https://en.wikipedia.org/wiki/Tempeh",[],""),
   X("Oat tempeh","","Tempeh made from barley and oats instead of beans.","","2008","https://en.wikipedia.org/wiki/Tempeh",[],""),
  ],
  "m":[["Tempeh","Tofurky"]]},
 {"n":"Plant-based meat","a":"meat alternative · meat analogue · mock meat · meat substitute · vegetarian meat","d":"Plant-protein product made to look, cook and taste like meat or fish, such as burgers, mince, sausages and nuggets.",
  "t":["burger","mince","sausage","chicken-style pieces","nuggets","bacon-style","deli slices","roast","meatballs","steak","plant-based fish & seafood","chilled","frozen","pea protein","soy protein","wheat protein"],
  "s":W+"Meat_analogue",
  "x":[
   X("Beyond Burger","","Pea-protein burger patty designed to look and cook like raw beef.","Beyond Meat","2016","https://en.wikipedia.org/wiki/Beyond_Meat",
     [("Beyond Burger (original)","Beyond Meat","2016",""),("Beyond Burger 2.0","Beyond Meat","2019","meatier, less saturated fat"),("Beyond Burger 3.0","Beyond Meat","2021","lower fat and calories"),("Beyond Burger IV","Beyond Meat","2024","avocado oil replaces canola and coconut oil")],"patty size · pack count"),
   X("Impossible Burger","","Soy-based burger that uses heme (soy leghemoglobin) made by fermented yeast for a meaty taste.","Impossible Foods","2016","https://en.wikipedia.org/wiki/Impossible_Foods",
     [("Impossible Burger","Impossible Foods","2016","launched July 2016"),("Impossible Burger 2.0","Impossible Foods","2019","January 2019")],"patties or bulk mince"),
   X("Plant-based sausage","Beyond Sausage · Impossible Sausage","Sausage of plant protein made to brown and snap like a pork sausage.","Beyond Meat","2018","https://en.wikipedia.org/wiki/Beyond_Meat",
     [("Beyond Sausage","Beyond Meat","2018",""),("Beyond Breakfast Sausage","Beyond Meat","2020",""),("Impossible Sausage (Impossible Pork)","Impossible Foods","2020","wider launch January 2020")],"links or patties · flavour"),
   X("Plant-based mince","Beyond Mince · Beyond Beef Crumbles","Loose ground-meat substitute for sauces, tacos and meatballs.","Beyond Meat","2014","https://en.wikipedia.org/wiki/Beyond_Meat",
     [("Beyond Beef Crumbles","Beyond Meat","2014",""),("Beyond Meatballs","Beyond Meat","2020","retail"),("Beyond Mince","Beyond Meat","2021","UK")],""),
   X("Plant-based chicken","Beyond Chicken · Impossible Chicken","Chicken-style strips, pieces and nuggets of plant protein.","Beyond Meat","2012","https://en.wikipedia.org/wiki/Beyond_Meat",
     [("Beyond Chicken Strips","Beyond Meat","2012","first product, discontinued 2019"),("Beyond Chicken Nuggets","Beyond Meat","2022",""),("Impossible Chicken","Impossible Foods","2021","")],"strips, pieces or nuggets"),
   X("Tofurky roast","","Roast made from a blend of tofu and wheat gluten.","Tofurky","1995","https://en.wikipedia.org/wiki/Tofurky",[],""),
   X("Linda McCartney vegetarian range","","British frozen vegetarian sausages, burgers and pies sold under Linda McCartney's name.","Linda McCartney Foods","1991","https://en.wikipedia.org/wiki/Linda_McCartney_Foods",
     [("Beefless burgers","Linda McCartney Foods","1991","in the launch range"),("Vegetarian sausages","Linda McCartney Foods","","textured vegetable protein with parsley (1995 report)")],""),
   X("Protose","","Early meat substitute from John Harvey Kellogg's Sanitas Nut Food Co., advertised by 1900.","","by 1900","https://en.wikipedia.org/wiki/Meat_analogue",[],""),
  ],
  "m":[["Incogmeato","Morningstar Farms"],["Awesome Burger","Nestlé"],["Plant-Based Whopper patty (China)","The Vegetarian Butcher"],["Beyond Steak","Beyond Meat"]]},
 {"n":"Mycoprotein","a":"fungal protein · mycelium protein · Quorn","d":"Protein food grown from fungal mycelium, such as Fusarium venenatum, formed into mince, pieces and meat-style products.",
  "t":["mince","pieces","sausages","nuggets","fillets","burgers","vegetarian (egg-white binder)","vegan (potato-protein binder)"],
  "s":W+"Mycoprotein",
  "x":[
   X("Quorn","","Mycoprotein from Fusarium venenatum, the first fungal meat alternative sold to the public.","Quorn","1985","https://en.wikipedia.org/wiki/Quorn",
     [("Quorn (egg-albumen binder)","Quorn","1985","original vegetarian range"),("Quorn Vegan Burger","Quorn","2011","first vegan product, US"),("Quorn vegan range","Quorn","2015","eight products, UK")],"mince · pieces · sausages · ready meals"),
   X("Meati","MushroomRoom","Whole-cut mycelium steaks and fillets grown from Neurospora crassa.","","2022","https://en.wikipedia.org/wiki/Mycoprotein",[],""),
   X("Fy Protein","Nature's Fynd","Fungal protein from an extremophile fungus found in Yellowstone.","","","https://en.wikipedia.org/wiki/Mycoprotein",[],""),
  ]},
 {"n":"Seitan","a":"wheat gluten · wheat meat · mianjin · 麵筋 · fu · kaofu · milgogi · mì căn","d":"Chewy meat-like food made from washed wheat gluten, simmered, steamed, baked or fried.",
  "t":["block","sliced","marinated","in broth","dried","vital wheat gluten mix"],
  "s":W+"Seitan",
  "x":[
   X("Mianjin","miànjīn · mien chin","Chinese wheat gluten, recorded since the 6th century, made in baked, fried and steamed forms.","","535 (Qimin Yaoshu)","https://en.wikipedia.org/wiki/Seitan",
     [("Kaofu","","","baked spongy gluten"),("Youmianjin","","","oil-fried gluten balls"),("Zhengmianjin","","","steamed gluten sausage"),("Mianlun","","","sliced gluten wheels")],""),
   X("Fu","麩","Japanese wheat gluten, fresh or dry-baked.","","","https://en.wikipedia.org/wiki/Seitan",
     [("Nama-fu","","","raw, steamed gluten"),("Yaki-fu","","","dry-baked; also sukiyaki-fu"),("Fu-manjū","","","")],""),
   X("Mock duck","","Wheat gluten seasoned and shaped as a duck or poultry substitute.","","","https://en.wikipedia.org/wiki/Seitan",[],""),
   X("Seitan (macrobiotic)","","Gluten simmered in soy sauce, named by George Ohsawa and sold to the macrobiotic movement.","","1961","https://en.wikipedia.org/wiki/Seitan",
     [("Seitan","Marushima Shoyu","1962","first sold as seitan, Japan"),("Seitan","Erewhon","1969","imported to the West as a salty condiment"),("Tan Pups","","1972",""),("Wheatmeat","","1974","Boston, John Weissman")],""),
  ]},
 {"n":"Yuba","a":"tofu skin · beancurd skin · beancurd sheet · fupi · doufu pi · fuzhu · foo chuk","d":"Film lifted from heated soy milk, sold fresh or dried as sheets or sticks.",
  "t":["fresh","dried","sheet","stick","knot","roll"],
  "s":W+"Tofu_skin",
  "x":[
   X("Fupi sheet","yuba sheet · first skin","The first film lifted from the pan, the finest grade, sold fresh or dried flat.","","16th century","https://en.wikipedia.org/wiki/Tofu_skin",[],"fresh or dried · sheet size"),
   X("Fuzhu","beancurd stick","Later films hung to dry in stick form.","","","https://en.wikipedia.org/wiki/Tofu_skin",[],""),
   X("Tofu chicken","sù jī · 素雞","Tofu skin rolled around itself or a filling, tied and steamed or stewed.","","","https://en.wikipedia.org/wiki/Tofu_skin",[],""),
  ]},
]
def B(n,c,f,seg,d,s,lines=(),sig=(),rel=(),eras=()):
    return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":list(lines),"eras":list(eras),"sig":list(sig),"sc":[],"rel":list(rel),"s":s}
brands=[
 B("Beyond Meat","United States","2009","Plant-based meat","El Segundo, California maker of pea-protein meat alternatives, founded by Ethan Brown.",W+"Beyond_Meat",["Beyond Burger","Beyond Sausage","Beyond Mince","Beyond Chicken","Beyond Steak"],["Beyond Burger"],["Impossible Foods"]),
 B("Impossible Foods","United States","2011","Plant-based meat","Redwood City, California maker of heme-based meat alternatives, founded by Patrick O. Brown.",W+"Impossible_Foods",["Impossible Burger","Impossible Sausage","Impossible Chicken"],["Impossible Burger"],["Beyond Meat"]),
 B("Quorn","United Kingdom","1985","Mycoprotein","Mycoprotein brand from Stokesley, North Yorkshire, founded by Marlow Foods and owned by Monde Nissin since 2015.",W+"Quorn",["Quorn","Quorn vegan range"],["Quorn"]),
 B("Tofurky","United States","1980","Plant-based meat and tempeh","Hood River, Oregon company founded by Seth Tibbott as Turtle Island Foods; owned by Morinaga Nutritional Foods since 2023.",W+"Tofurky",["Tofurky roast","deli slices","sausages","tempeh"],["Tofurky roast"],["Mori-Nu"]),
 B("Mori-Nu","United States","1985","Shelf-stable tofu","Silken tofu brand of Morinaga Nutritional Foods of Torrance, California, sold in aseptic cartons since 1985.","https://well.ca/brand/mori-nu.html",["Soft, Firm and Extra Firm Silken Tofu"],["Aseptic silken tofu"],["Tofurky","House Foods"]),
 B("House Foods","Japan","1913","Food maker (tofu in the US)","Higashiōsaka food company whose House Foods America is the largest tofu supplier in the United States.",W+"House_Foods",["tofu (US)"],[],["Mori-Nu"]),
 B("Taifun","Germany","","Organic tofu","Freiburg tofu maker of plain and smoked tofu, tofu fillets and tofu sausages.","https://www.taifun-tofu.de/en",["Smoked Tofu Classic","Plain Firm Tofu","Tofu Filets","Tofu Sausages"],["Smoked tofu"],["Cauldron"]),
 B("Cauldron","","","Tofu","Tofu brand sold in UK supermarkets, with extra-firm and grillable marinated tofu.","https://www.cauldronfoods.co.uk/",["Extra Firm Plant-Based Tofu","Grillable Tofu"],[],["Taifun"]),
 B("Linda McCartney Foods","United Kingdom","1991","Vegetarian convenience food","British vegetarian food brand created by Linda McCartney; owned by Hain Celestial since 2006.",W+"Linda_McCartney_Foods",["sausages","burgers","pies"],["Linda McCartney vegetarian range"]),
 B("The Vegetarian Butcher","Netherlands","2010","Plant-based meat","Utrecht maker founded by Jaap Korteweg and Niko Koffeman; owned by Unilever from 2018 and JBS (via Vivera) from 2025.",W+"The_Vegetarian_Butcher",[],[],["Vivera"],["Unilever, 2018–2025","JBS via Vivera, 2025–"]),
 B("Morningstar Farms","United States","1974","Plant-based meat","US meatless frozen-food brand of Kellanova, owned by Kellogg from 1999.",W+"Morningstar_Farms",["Incogmeato"]),
]
traditions=[
 {"n":"Chinese tofu making","g":"Food & drink","r":"China","p":"Han dynasty onward; popular from the Song dynasty (960–1279)","d":"Making bean curd by coagulating soy milk and pressing the curds, credited by legend to Prince Liu An.","tech":"grinding soaked soybeans, boiling, coagulating with gypsum or bittern, pressing; fermenting and drying","mat":"soybeans, gypsum, nigari (bittern)","forms":["Tofu","Fermented bean curd","Stinky tofu","Yuba","Douhua"],"ctr":["Changsha (stinky tofu)","Shaoxing","Taiwan night markets"],"auth":"","s":W+"Tofu"},
 {"n":"Japanese tofu making","g":"Food & drink","r":"Japan","p":"after its spread from China","d":"Japanese tofu styles from silken kinugoshi and pressed momen to fried, frozen and freeze-dried forms.","tech":"gypsum-set unpressed (kinugoshi) or pressed (momen) curd; deep-frying; freezing and freeze-drying","mat":"soybeans, gypsum, nigari","forms":["Kinugoshi","Momen-dofu","Aburaage","Atsuage","Kōya-dōfu","Shimidōfu","Yuba"],"ctr":["Mount Kōya (kōya-dōfu)","Tōhoku (shimidōfu)"],"auth":"","s":W+"Tofu"},
 {"n":"Javanese tempe making","g":"Food & drink","r":"Java, Indonesia","p":"commonly eaten by about 1700","d":"Fermenting soybeans with Rhizopus mould into a bound cake; said to have begun in Bayat, Klaten, Central Java. Indonesia submitted it to UNESCO's intangible heritage list in March 2024 (pending).","tech":"soaking, dehulling and boiling beans, inoculating with Rhizopus and incubating in leaves or plastic","mat":"soybeans, Rhizopus oligosporus or R. oryzae, teak or waru leaves","forms":["Soy tempe","Tempe gembus","Tempe bongkrèk","Oncom"],"ctr":["Bayat, Klaten (Central Java)","Malang (tempe menjes)","West Java (oncom)"],"auth":"","s":"https://mataram.antaranews.com/berita/349839/tempeh-proposed-to-be-inscribed-on-unesco-cultural-heritage-list"},
]
notes=("All six kinds are new (moved in from J5) and sourced from Wikipedia pages fetched this session. Tofu types (silken, firm, extra-firm, smoked, fried, frozen) are in t; named forms with their own source (aseptic silken, smoked, kōya-dōfu, fermented bean curd, stinky tofu) are archetypes. "
 "Tempe bongkrèk was left out as an archetype (linked to fatal poisonings, not a retail product) but named in the tradition. Textured vegetable protein stays in J5. "
 "House Foods has a register entry but no named tofu product was confirmed on a retrieved page, so it has no model. Morningstar Farms' Grillers/Chik'n products were not confirmed and are left out; Gardein, Vivera and Boca were not sourced. "
 "Cauldron's country and founding year and Taifun's founding year were not stated on the retrieved pages. Tempeh UNESCO status: proposal submitted March 2024, pending (Antara); later reports disagree on dates, so no outcome is claimed. No independent test winners were sourced.")
out={"kinds":kinds,"brands":brands,"traditions":traditions,"notes":notes}
p="work/J3/shelves/07_00.json"; os.makedirs("work/J3/shelves",exist_ok=True)
json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
