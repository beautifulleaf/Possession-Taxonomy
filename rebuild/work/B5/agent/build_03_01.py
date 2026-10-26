import json, os
W='https://en.wikipedia.org/wiki/'
ATK_SM='https://www.americastestkitchen.com/equipment_reviews/2593-the-best-stand-mixers'
ATK_HM='http://www.americastestkitchen.com/equipment_reviews/2355-hand-mixers'
ATK_BL='https://www.americastestkitchen.com/equipment_reviews/2640'
ATK_IB='https://www.americastestkitchen.com/equipment_reviews/2450-immersion-blenders'
ATK_FP='http://www.americastestkitchen.com/equipment_reviews/2194-food-processors'
ATK_IC='http://www.americastestkitchen.com/equipment_reviews/1698-ice-cream-makers'
FNAC='https://leclaireur.fnac.com/article/cp59612-lhistoire-de-magimix-la-cuisine-francaise-a-portee-de-main/'
def v(n,mk,y='',d=''): return {"n":n,"mk":mk,"y":y,"d":d}
kinds=[
{"n":"Stand mixer","a":"kitchen machine · food mixer · planetary mixer","d":"Countertop mixer with a bowl and a motor head that drives beaters, whisk or dough hook.",
 "t":["tilt-head","bowl-lift","rotating-bowl (Assistent type)","spiral dough mixer","mini / compact","with heating or cooking function","attachment hub (mincer, pasta roller, grain mill)"],
 "s":"https://www.kitchenaid.com/countertop-appliances/stand-mixers",
 "x":[
  {"n":"KitchenAid tilt-head (Model K lineage)","a":"KitchenAid Artisan · Classic · K45","d":"Planetary-action tilt-head mixer with the streamlined silhouette Egmont Arens gave the Model K; the reference home stand mixer.","mk":"KitchenAid","y":"1937","s":ATK_SM,
   "v":[v("H-5","KitchenAid","1922","First home model with a five-quart bowl, built by Hobart."),v("Model G","KitchenAid","1928","About half the weight of the H-5."),v("Model K","KitchenAid","1937","Egmont Arens's tilt-head design; colours added 1955."),v("Classic K45 (K45SSWH)","KitchenAid","","4.5-quart tilt-head; ATK best mid-priced pick."),v("Artisan (KSM150)","KitchenAid","","5-quart tilt-head, the best-known model."),v("Artisan Mini (KSM3316X)","KitchenAid","","3.5-quart compact version; ATK best small mixer."),v("Artisan Plus (KSM50P)","KitchenAid","","Updated 5-quart tilt-head.")],
   "dt":"bowl 3.3–4.8 L (3.5–5 qt) · tilt-head · enamel colours and special editions · front attachment hub"},
  {"n":"KitchenAid bowl-lift","a":"KitchenAid Pro · Professional","d":"Heavier KitchenAid planetary mixer where the bowl is raised to the fixed head on side arms, for large batches.","mk":"KitchenAid","y":"","s":ATK_SM,
   "v":[v("7 Quart Bowl-Lift (KSM70)","KitchenAid","","ATK highly recommended.")],"dt":"bowl 5.5–6.6 L (6–7 qt) · bowl-lift arms · attachment hub"},
  {"n":"Kenwood Chef","a":"Kenwood Electric Chef · Chef Major · Titanium","d":"British planetary-action kitchen machine shown at the 1950 Ideal Home Exhibition, with high- and slow-speed attachment outlets.","mk":"Kenwood","y":"1950","s":W+"Kenwood_Chef",
   "v":[v("A700","Kenwood","1950","First Electric Chef."),v("A701","Kenwood","1960","Kenneth Grange redesign that set the familiar shape."),v("A901","Kenwood","mid-1970s","Streamlined restyle."),v("Chef Excel","Kenwood","c. 1983",""),v("KM001 / Titanium","Kenwood","2004","Redesign including the Titanium series."),v("Chef Major","Kenwood","","Larger 6-litre bowl version."),v("Cooking Chef","Kenwood","","Major-type machine with cook-and-stir heating.")],
   "dt":"bowl 4.6–6.7 L · planetary action · Chef vs Major size · attachment outlets"},
  {"n":"Ankarsrum Assistent","a":"Electrolux Assistent · Ankarsrum Original · Magic Mill","d":"Swedish mixer with a rotating steel bowl driven from below, a roller and scraper instead of planetary beaters; strong on bread dough.","mk":"Ankarsrum","y":"1940","s":W+"Electrolux_Assistent",
   "v":[v("NG1","Electrolux","1940","First model, 250 W, designed by Alvar Lenning."),v("N1","Electrolux","1945","Post-war model."),v("N3","Electrolux","c. 1950","Plastic roller and paddle, 275 W."),v("N4","Electrolux","1954","New mixer socket design."),v("Assistent Original 7 L (AKM 6230)","Ankarsrum","","ATK winner; made in Ankarsrum since 1969.")],
   "dt":"7 L stainless bowl · roller & scraper, dough hook, whisk bowl · motor up to 1500 W · colours"},
  {"n":"Sunbeam Mixmaster","a":"Mixmaster","d":"American stand mixer with twin beaters and a turntable bowl that made electric mixing a mass-market product.","mk":"Sunbeam","y":"1930","s":W+"Sunbeam_Products",
   "v":[v("Mixmaster","Sunbeam","1930","Co-invented by Ivar Jepson and Bernard Alton Graham in 1928.")],"dt":"twin beaters · turntable bowl · detachable hand unit on later models"}],
 "m":[["Universal Plus","Bosch"],["the Bakery Chef","Breville"],["Artiste","NutriMill"],["Precision Master SM-50","Cuisinart"],["7-Speed Stand Mixer 4 qt","Hamilton Beach"]]},
{"n":"Hand mixer","a":"handheld mixer · electric whisk · beater","d":"Handheld electric mixer with twin beaters for batters, cream and egg whites.",
 "t":["corded","cordless","with stand / bowl","with dough hooks"],"s":W+"Mixer_(appliance)",
 "m":[["Handy Mix Scraper (BHM800)","Breville"],["Power Advantage Plus 9 Speed (HM-90S)","Cuisinart"],["5-Speed Ultra Power (KHM512)","KitchenAid"],["9-Speed (KHM9212)","KitchenAid"]]},
{"n":"Blender","a":"liquidiser · jug blender · countertop blender","d":"Appliance with a jar and fast spinning blade that purées, blends and crushes food and drink.",
 "t":["countertop jug","high-performance","personal / single-serve","vacuum","heated (soup)"],"s":"https://shopping.yahoo.co.jp/products/760ad2b9f3",
 "x":[
  {"n":"Waring Blendor","a":"Miracle Mixer","d":"Fred Waring's bar-and-kitchen blender, developed from Fred Osius's design, that popularised the jug blender.","mk":"Waring","y":"1937","s":W+"Blender_(appliance)",
   "v":[v("Miracle Mixer","Waring","1933","Osius design financed by Fred Waring."),v("Waring Blendor","Waring","1937","Redesigned release.")],"dt":"glass jug on motor base · chrome or coloured base"},
  {"n":"Vitamix high-performance blender","a":"Vita-Mix · Vitamix 5200 · Ascent","d":"Powerful American blender with a tall container and variable speed, the reference high-performance blender.","mk":"Vitamix","y":"1937","s":W+"Vitamix",
   "v":[v("The Blender (Vita-Mix)","Vitamix","1937","Reinforced model with stainless jar."),v("Mark 20","Vitamix","1950","Variable speeds."),v("3600","Vitamix","1970","More powerful motor."),v("5000 Total Nutrition Center","Vitamix","1992",""),v("5200","Vitamix","","ATK long-standing winner."),v("7500","Vitamix","2012",""),v("Ascent series (e.g. X2)","Vitamix","2016","First Smart System blenders."),v("Explorian E310","Vitamix","","Lower-priced line; ATK highly recommended."),v("Vitamix One","Vitamix","2021","")],
   "dt":"container 1.4–2 L · variable speed dial vs presets · tamper"},
  {"n":"Osterizer","a":"Oster blender","d":"John Oster's mass-market blender, later part of Sunbeam.","mk":"Oster","y":"1946","s":W+"Blender_(appliance)","v":[],"dt":"glass jar · push-button or dial speeds"},
  {"n":"Blendtec","a":"Total Blender · Designer","d":"High-performance blender with a blunt wing blade and square WildSide jar, known for the Will It Blend? campaign.","mk":"Blendtec","y":"1996","s":W+"Blendtec",
   "v":[v("WildSide jar","Blendtec","1996","Five-sided jar."),v("Total Blender Classic","Blendtec","",""),v("Classic 575","Blendtec","",""),v("Designer 650","Blendtec","",""),v("Professional 800","Blendtec","","")],"dt":"WildSide, FourSide and Twister jars · touch controls"},
  {"n":"Magic Bullet / NutriBullet","a":"Magic Bullet · NutriBullet","d":"Compact personal blender that blends into a cup you drink from.","mk":"NutriBullet","y":"2003","s":W+"NutriBullet",
   "v":[v("Magic Bullet","NutriBullet","2003",""),v("NutriBullet","NutriBullet","",""),v("NutriBullet Balance","NutriBullet","",""),v("Full Size Blender","NutriBullet","","ATK recommended with reservations.")],"dt":"cup size · motor wattage · lids and to-go cups"}],
 "m":[["Fresh & Furious","Breville"],["TriForce Power Blender","Braun"],["Professional Plus with Auto-iQ (BN701)","Ninja"],["K400","KitchenAid"]]},
{"n":"Immersion blender","a":"stick blender · hand blender · wand blender","d":"Handheld blender with a blade at the end of a shaft, used directly in the pot or jug.",
 "t":["corded","cordless","with chopper and whisk set"],"s":W+"Immersion_blender",
 "x":[
  {"n":"Bamix","a":"bamix","d":"Swiss original hand blender, named from French 'battre et mixer', with interchangeable blade heads.","mk":"Bamix","y":"1950","s":W+"Bamix",
   "v":[v("Patent","Bamix","1950","Roger Perrinjaquet's patent of 6 March 1950."),v("Mono","Bamix","",""),v("Classic","Bamix","",""),v("DeLuxe","Bamix","",""),v("SwissLine","Bamix","",""),v("Gastro","Bamix","","Professional version.")],"dt":"wattage · blade heads (multi, beater, whisk) · stand and accessories"},
  {"n":"Braun MultiQuick","a":"MultiQuick","d":"Braun's hand-blender line, the long-running test winner.","mk":"Braun","y":"","s":ATK_IB,
   "v":[v("MultiQuick 5 (MQ505)","Braun","","ATK winner."),v("MultiQuick 7 (MQ7035X)","Braun","","ATK highly recommended.")],"dt":"speed control · accessories (chopper, whisk, beaker)"}],
 "m":[["Control Grip (BSB510XL)","Breville"],["Ultra-Stick","Mueller"]]},
{"n":"Food processor","a":"robot · magimix · kitchen robot","d":"Appliance with a bowl and interchangeable blades and discs for chopping, slicing, grating and mixing.",
 "t":["full-size","compact","mini chopper","heated (thermal) food processor","with dicing kit","with juicer or blender attachment"],"s":"https://www.thebrick.com/products/cuisinart-custom-14-cup-food-processor-dfp-14bcnyc?view=print",
 "x":[
  {"n":"Robot-Coupe / Magimix","a":"Le Magi-Mix · Robot-Coupe","d":"French bowl-and-revolving-blade processor from Pierre Verdun and Robert Comte; Magimix is the domestic version.","mk":"Magimix","y":"1971","s":FNAC,
   "v":[v("Robot-Coupe","Magimix","1961","Verdun and Comte's machine for caterers, Montceau-les-Mines."),v("Magimix (first domestic model)","Magimix","1971",""),v("Model 1800","Magimix","1974","Arrives in the UK; base of the first Cuisinart."),v("Compact 4200 XL","Magimix","","ATK recommended."),v("CS range","Magimix","","Multi-bowl processors; first multi-bowl model 1988."),v("Cook Expert","Magimix","","Heated cooking processor.")],"dt":"bowl sizes · induction motor · nested bowls · discs"},
  {"n":"Cuisinart food processor","a":"Cuisinart Custom 14","d":"American processor launched by Carl Sontheimer from the Robot-Coupe design; brought food processors to US homes.","mk":"Cuisinart","y":"1973","s":W+"Cuisinart",
   "v":[v("Original (rebadged Robot-Coupe/Magimix 1800)","Cuisinart","1973","Shown at a Chicago trade show."),v("Marc Harrison redesign","Cuisinart","1978","Larger lettering, handles and buttons."),v("Custom 14 (DFP-14BCNY)","Cuisinart","","ATK winner."),v("Pro Custom 11 (DLC-8SY)","Cuisinart","","ATK best buy.")],"dt":"capacity 7–14 cups · discs · pulse/on/off paddles"},
  {"n":"Braun KM 3","a":"KM 3/31","d":"Braun kitchen machine designed by Gerd A. Müller, made almost unchanged for decades.","mk":"Braun","y":"1957","s":W+"Braun_(company)",
   "v":[v("KM 3/31","Braun","1957","Design little changed until 1993.")],"dt":"white housing · mixer, blender and processor attachments"},
  {"n":"Starmix","a":"Electrostar Starmix","d":"Early German electric food processor with many accessories.","mk":"Electrostar","y":"1946","s":W+"Food_processor",
   "v":[v("MX3","Electrostar","1960s","Designed by Albrecht von Goertz.")],"dt":""},
  {"n":"Thermomix","a":"Vorwerk Thermomix · TM","d":"Heated food processor that chops, blends and cooks in one jug, sold by direct demonstration.","mk":"Vorwerk","y":"1971","s":W+"Thermomix",
   "v":[v("VKM5","Vorwerk","1961","Predecessor."),v("VM 2000","Vorwerk","1971","First Thermomix, launched in France."),v("TM 21","Vorwerk","1996",""),v("TM 31","Vorwerk","2004",""),v("TM 5","Vorwerk","2014",""),v("TM 6","Vorwerk","2019",""),v("TM 7","Vorwerk","2025","")],"dt":"heated jug · touchscreen and guided recipes (TM5 on)"}],
 "m":[["Sous Chef 16","Breville"],["13-Cup (KFP1318)","KitchenAid"]]},
{"n":"Juicer","a":"juice extractor · juice press","d":"Appliance that separates juice from fruit and vegetables, by spinning, slow pressing or reaming.",
 "t":["centrifugal","masticating / slow (vertical)","masticating (horizontal)","twin-gear (triturating)","citrus press / reamer","steam juice extractor"],"s":W+"Juicer",
 "x":[
  {"n":"Hurom slow juicer","a":"Hurom H-AA · H310","d":"Korean vertical auger juicer using slow-squeeze technology, which started the vertical slow-juicer genre.","mk":"Hurom","y":"2005","s":"https://hurom.com/pages/about",
   "v":[v("First SST slow juicer","Hurom","2005",""),v("H-AA","Hurom","",""),v("H310 Easy Clean","Hurom","","Compact model.")],"dt":"vertical auger · rpm · chute width · colours"},
  {"n":"Omega J8006","a":"Omega 8006","d":"Horizontal single-auger masticating juicer running at about 80 rpm; also makes nut butters and extrudes pasta.","mk":"Omega","y":"","s":"https://techcrunch.com/2012/05/18/gadget-of-the-week-the-omega-j8006-juicer","v":[],"dt":"horizontal auger · nozzles for pasta and nut butter"}],
 "r":[["Juice Expert","Magimix"],["Juice Fountain","Breville"]],
 "m":[["Slow juicers","Kuvings"],["Juicers","Champion"]]},
{"n":"Pasta machine","a":"pasta maker · pasta roller","d":"Machine that rolls and cuts fresh pasta dough, or extrudes shaped pasta.",
 "t":["manual roller with cutters","motorised roller","stand-mixer roller attachment","electric extruder"],"s":"https://reviewed.com/cooking/best-right-now/the-best-pasta-makers",
 "x":[{"n":"Marcato Atlas","a":"Atlas 150","d":"Italian hand-crank roller with clamp and cutter heads, made in Campodarsego; the standard home pasta roller.","mk":"Marcato","y":"1965","s":"https://www.culinaris.de/en/BRANDS/Marcato/",
   "v":[v("Atlas","Marcato","1965","Launch of the Atlas line."),v("Atlas 150","Marcato","","150 mm rollers; Reviewed best overall.")],"dt":"roller width · cutter heads · colours · motor option"}],
 "m":[["Pasta Maker","Imperia"],["3-Piece Pasta Roller and Cutter Attachment","KitchenAid"]]},
{"n":"Ice cream maker","a":"ice cream machine · sorbetière","d":"Machine that churns and freezes a mix into ice cream, sorbet or frozen yoghurt.",
 "t":["freezer-bowl (canister)","compressor (self-refrigerating)","ice-and-salt","hand-cranked","frozen-pint processor (Creami type)","stand-mixer attachment"],"s":W+"Ice_cream_maker",
 "x":[
  {"n":"Hand-cranked ice-and-salt freezer","a":"Johnson patent freezer","d":"Bucket of ice and salt round a cranked canister; the first home ice cream machine.","mk":"","y":"1843","s":W+"Ice_cream_maker",
   "v":[v("Johnson Patent Ice-Cream Freezer","","1843","Nancy Johnson's patent, produced by William Young from 1848.")],"dt":"bucket size · wood or plastic tub"},
  {"n":"Cuisinart freezer-bowl maker","a":"Cuisinart ICE-21","d":"Countertop machine with a pre-frozen coolant canister; the reference budget ice cream maker.","mk":"Cuisinart","y":"","s":ATK_IC,
   "v":[v("ICE-21","Cuisinart","","ATK best canister-style."),v("ICE-30BCP1 Pure Indulgence","Cuisinart","","2-quart."),v("ICE-100","Cuisinart","","Compressor version.")],"dt":"bowl 1.5–2 qt · freezer bowl vs compressor"},
  {"n":"Ninja CREAMi","a":"Creami","d":"Machine that shaves a pre-frozen pint with a spinning blade instead of churning.","mk":"Ninja","y":"2021","s":"https://www.nbcnews.com/select/shopping/ninja-creami-review-rcna95316",
   "v":[v("CREAMi (NC301)","Ninja","2021",""),v("CREAMi Deluxe (NC501)","Ninja","","24 oz pints, more programmes."),v("CREAMi Breeze (NC201)","Ninja","","16 oz pints.")],"dt":"pint size · programmes"}],
 "m":[["ICM-201SB 2.1 qt compressor","Whynter"],["Smart Scoop (BCI600XL)","Breville"],["Ice Cream Maker Attachment (KSMICM)","KitchenAid"]]},
{"n":"Meat grinder","a":"mincer · meat mincer","d":"Appliance whose screw pushes food against a blade and holed plate to mince meat.",
 "t":["manual hand-crank","electric","stand-mixer attachment","sausage stuffer"],"s":W+"Meat_grinder",
 "m":[["Metal Food Grinder attachment","KitchenAid"],["Mighty Bite #8","LEM"],["Big Bite #22","LEM"],["#22 1 HP","Meat!"]]},
{"n":"Coffee and spice grinder (blade)","a":"blade grinder · blade mill · spice grinder","d":"Small electric grinder with a spinning blade that chops coffee or spices unevenly, unlike a burr mill.",
 "t":["coffee","spice","removable bowl"],"s":W+"Burr_mill"}]
brands=[
 {"n":"KitchenAid","c":"United States","f":"1919","seg":"Kitchen appliances","d":"Hobart's home-mixer brand, owned by Whirlpool since 1986.","lines":["Artisan","Classic","bowl-lift","ProLine"],"eras":["Hobart, 1919–1986","Whirlpool, 1986–"],"sig":["KitchenAid tilt-head (Model K lineage)"],"sc":[],"rel":["Hobart"],"s":W+"KitchenAid"},
 {"n":"Kenwood","c":"United Kingdom","f":"1947","seg":"Kitchen appliances","d":"Founded by Kenneth Wood in Woking; maker of the Kenwood Chef; owned by De'Longhi since 2001.","lines":["Chef","Chef Major","Cooking Chef"],"eras":["Kenneth Wood, 1947–","De'Longhi, 2001–"],"sig":["Kenwood Chef"],"sc":[],"rel":["De'Longhi"],"s":W+"Kenwood_Limited"},
 {"n":"Ankarsrum","c":"Sweden","f":"2009","seg":"Kitchen appliances","d":"Ankarsrum Industries makes the Assistent mixer, an Electrolux design built in Ankarsrum since 1969.","lines":["Assistent Original"],"eras":["Electrolux, 1940–2001","Ankarsrum Industries, 2009–"],"sig":["Ankarsrum Assistent"],"sc":[],"rel":["Electrolux"],"s":W+"Electrolux_Assistent"},
 {"n":"Sunbeam","c":"United States","f":"1897","seg":"Kitchen appliances","d":"Founded as the Chicago Flexible Shaft Company; maker of the Mixmaster; owned by Newell Brands.","lines":["Mixmaster"],"eras":[],"sig":["Sunbeam Mixmaster"],"sc":[],"rel":["Oster"],"s":W+"Sunbeam_Products"},
 {"n":"Vitamix","c":"United States","f":"1921","seg":"High-performance blenders","d":"Ohio blender maker founded by William Grover Barnard.","lines":["Classic (5200)","Ascent","Explorian","Propel"],"eras":[],"sig":["Vitamix high-performance blender"],"sc":[],"rel":["Blendtec"],"s":W+"Vitamix"},
 {"n":"Blendtec","c":"United States","f":"1975","seg":"High-performance blenders","d":"Utah blender maker founded by Tom Dickson, known for Will It Blend? videos.","lines":["Classic","Designer","Professional"],"eras":[],"sig":["Blendtec"],"sc":[],"rel":["Vitamix"],"s":W+"Blendtec"},
 {"n":"NutriBullet","c":"United States","f":"","seg":"Personal blenders","d":"Personal-blender brand of Homeland Housewares, grown from the 2003 Magic Bullet.","lines":["Magic Bullet","NutriBullet","Baby Bullet"],"eras":[],"sig":["Magic Bullet / NutriBullet"],"sc":[],"rel":[],"s":W+"NutriBullet"},
 {"n":"Bamix","c":"Switzerland","f":"1954","seg":"Hand blenders","d":"Brand of the original hand blender, patented by Roger Perrinjaquet in 1950.","lines":["Mono","Classic","DeLuxe","SwissLine","Gastro"],"eras":[],"sig":["Bamix"],"sc":[],"rel":[],"s":W+"Bamix"},
 {"n":"Braun","c":"Germany","f":"1921","seg":"Small appliances","d":"Frankfurt maker founded by Max Braun, known for Dieter Rams-era design; owned by Procter & Gamble.","lines":["MultiQuick","TriForce","KM 3"],"eras":["Dieter Rams head of design, 1961–1995"],"sig":["Braun MultiQuick","Braun KM 3"],"sc":[],"rel":[],"s":W+"Braun_(company)"},
 {"n":"Cuisinart","c":"United States","f":"1971","seg":"Kitchen appliances","d":"Founded by Carl Sontheimer; introduced the food processor to US homes in 1973; owned by Conair.","lines":["Custom 14","ICE ice cream makers"],"eras":["Sontheimer, 1971–1989","Conair, 1989–"],"sig":["Cuisinart food processor","Cuisinart freezer-bowl maker"],"sc":[],"rel":["Magimix"],"s":W+"Cuisinart"},
 {"n":"Magimix","c":"France","f":"1971","seg":"Kitchen appliances","d":"Domestic brand of the Robot-Coupe processor from Montceau-les-Mines; family-run French maker.","lines":["Compact","CS","Cook Expert","Juice Expert"],"eras":["Verdun and Comte, 1961–"],"sig":["Robot-Coupe / Magimix"],"sc":[],"rel":["Robot-Coupe","Cuisinart"],"s":FNAC},
 {"n":"Breville","c":"Australia","f":"1932","seg":"Kitchen appliances","d":"Sydney appliance maker; sold as Sage in the UK and Europe.","lines":["Sous Chef","Handy Mix Scraper","Fresh & Furious","Smart Scoop"],"eras":[],"sig":[],"sc":[],"rel":["Sage"],"s":W+"Breville"},
 {"n":"Ninja","c":"United States","f":"1994","seg":"Kitchen appliances","d":"Appliance brand of SharkNinja, founded by Mark Rosenzweig as Euro-Pro.","lines":["CREAMi","Professional blenders"],"eras":[],"sig":["Ninja CREAMi"],"sc":[],"rel":["Shark"],"s":W+"SharkNinja"},
 {"n":"Hurom","c":"South Korea","f":"1974","seg":"Juicers","d":"Korean kitchen-appliance maker that introduced slow-squeeze vertical juicers in 2005.","lines":["H-AA","H310"],"eras":[],"sig":["Hurom slow juicer"],"sc":[],"rel":[],"s":"https://hurom.com/pages/about"},
 {"n":"Marcato","c":"Italy","f":"1930","seg":"Pasta machines","d":"Founded by Otello Marcato; makes pasta machines in Campodarsego near Padua.","lines":["Atlas"],"eras":[],"sig":["Marcato Atlas"],"sc":[],"rel":["Imperia"],"s":"https://www.culinaris.de/en/BRANDS/Marcato/"},
 {"n":"Vorwerk","c":"Germany","f":"","seg":"Direct-sales appliances","d":"German maker of the Thermomix, built in France and Wuppertal.","lines":["Thermomix"],"eras":[],"sig":["Thermomix"],"sc":[],"rel":[],"s":W+"Thermomix"},
 {"n":"Hamilton Beach","c":"United States","f":"1910","seg":"Kitchen appliances","d":"Founded in Racine by Frederick Osius; began with the Cyclone drink mixer.","lines":["mixers","blenders","food processors"],"eras":[],"sig":[],"sc":[],"rel":[],"s":W+"Hamilton_Beach_Brands"}]
notes=("Kept all 3 old kinds (Stand mixer, Blender, Food processor; old s kept) and added 8 planned kinds. Old flat KitchenAid models became versions of the tilt-head archetype. "
"Thermomix placed as a heated food processor archetype; if the Multicooker shelf also lists it, keep one. Coffee and spice grinder (blade) kept as a kind: Burr_mill page attests blade grinders as distinct. "
"Left out: Philips pasta extruder, Breville/Kenwood hand-mixer archetypes, Omega company facts, Waring and Oster brand entries (no page retrieved, only search snippets); Vitamix 5200 launch year and Braun MultiQuick year not confirmed. Juicer m entries are brand ranges from CHOICE's juicer brand list.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/B5/shelves/03_01.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p); print('ok')
