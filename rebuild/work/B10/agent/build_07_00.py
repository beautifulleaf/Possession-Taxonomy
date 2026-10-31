import json, os
W='https://en.wikipedia.org/wiki/'
NG='https://www.northerngecko.net/collections/exo-terra/products/exo-terra-glass-terrarium'
TPP='https://www.thatpetplace.com/reptibreeze-aluminum-screen-cage-16in-16in-20in'
VIV='https://www.reptilecentre.com/products/vivexotic-reptihome-vivarium-maxi-large-115x49x56cm'
PVC='https://shop.reptifiles.com/products/36x24x18-premium-pvc-reptile-enclosure'
MK='https://reptilecentre.com/products/mistking-starter-misting-system-v50'
RM='https://reptilesmagazine.com/exo-terra-and-zoo-med-win-pet-product-news-international-editors-choice-awards/'
CAL='https://www.thatpetplace.com/repashy-calcium-plus-6-oz'
ZCAL='https://www.thevetshed.com.au/buy/zoo-med-repti-calcium-with-d3/EXTCD3'
MRP='https://dubiaroaches.com/products/repashy-crested-gecko-mrp-diet-food-6-oz'
PAN='https://www.completeaquatics.co.uk/pangea-complete-gecko-diet-8oz-p-red8'
TC='https://thetarantulacollective.com/supplies'
ANT='https://antkeepers.com/pages/ytong-formicarium'
def v(n,mk,y='',d=''): return {"n":n,"mk":mk,"y":y,"d":d}
kinds=[
{"n":"Vivarium","a":"terrarium · reptile enclosure · viv","d":"An empty enclosure in which reptiles or amphibians are kept.",
 "t":["front-opening glass terrarium","wooden (melamine-faced board) vivarium","PVC or ABS enclosure","aluminium screen cage","paludarium (land and water)","bioactive set-up","tortoise table and outdoor house","flat breeder or rack tub"],
 "s":"https://charterhouse-aquatics.com/blogs/reptiles/setting-up-a-reptile-vivarium-a-step-by-step-guide",
 "x":[
  {"n":"Exo Terra Glass Terrarium","a":"front-opening glass terrarium","d":"All-glass terrarium with dual front-opening doors, escape lock, removable full-screen top and raised waterproof base for a substrate heater.","mk":"Exo Terra","y":"","s":NG,
   "v":[v("Glass Terrarium (PT2612 and other sizes)","Exo Terra","","12 × 12 × 12 in up to 24 × 18 × 24 in at this retailer"),v("Exo Terra Natural Terrarium","Exo Terra"),v("Exo Terra Panoramic Terrarium","Exo Terra"),v("Exo Terra Aquatic Terrarium","Exo Terra"),v("Exo Terra Pro Terrarium","Exo Terra")],
   "dt":"footprint and height (nano, small, medium, large; wide or tall) · background · screen inlets for cables and tubing"},
  {"n":"Zoo Med ReptiBreeze","a":"screen cage","d":"Open-air cage of black anodised aluminium screen with a large front door and a bottom door for substrate removal, for chameleons and other arboreal lizards.","mk":"Zoo Med","y":"","s":TPP,
   "v":[v("ReptiBreeze NT-10","Zoo Med","","16 × 16 × 20 in"),v("Zoo Med ReptiBreeze Double Door","Zoo Med"),v("Zoo Med ReptiBreeze LED Deluxe","Zoo Med"),v("Zoo Med ReptiBreeze IguanArium","Zoo Med"),v("Zoo Med Nano Breeze","Zoo Med"),v("Exo Terra Screen Terrarium","Exo Terra","","rival screen design")],
   "dt":"size · single or double door · aluminium screen colour"},
  {"n":"Wooden vivarium","a":"flat-pack viv · Repti-Home","d":"Flat-pack enclosure of 15 mm wood-effect boards with sliding toughened-glass doors and cable vents; holds heat well for basking species.","mk":"Vivexotic","y":"","s":VIV,
   "v":[v("Vivexotic Repti-Home Maxi Large","Vivexotic","","115 × 49 × 56 cm"),v("Vivexotic Repti-Home Large","Vivexotic","","115 × 37.5 × 42 cm"),v("Vivexotic AAL Vivarium Bearded Dragon","Vivexotic")],
   "dt":"length and depth · finish (oak, walnut, grey, black) · stacking cabinet"},
  {"n":"PVC reptile enclosure","a":"PVC cage · PVC kage","d":"Rigid expanded-PVC box with tempered-glass sliding front doors; light, moisture-proof and holds humidity, often built bioactive-ready.","mk":"Kages","y":"","s":PVC,
   "v":[v("36 × 24 × 18 in Premium PVC Reptile Enclosure","Kages","","1/2 in expanded PVC, rear slit venting, handmade in the USA")],
   "dt":"size from 12 in cubes to 8 × 4 × 4 ft · side vents · belly-heat recess · screen panel"},
  {"n":"Paludarium","a":"riparium","d":"Vivarium holding both land and water areas, either side by side or as an island surrounded by water.","mk":"","y":"","s":W+"Paludarium",
   "v":[v("Exo Terra Pro Paludarium","Exo Terra"),v("Zoo Med Paludarium","Zoo Med")],
   "dt":"land-to-water ratio · waterfall or stream · background"},
  {"n":"Bioactive vivarium","a":"bioactive terrarium","d":"Planted terrarium with a living soil and clean-up crew such as springtails and isopods that break down waste.","mk":"","y":"","s":W+"Vivarium",
   "v":[v("Zoo Med Naturalistic Terrarium","Zoo Med"),v("Zoo Med ReptiHabitat Designer Terrarium","Zoo Med")],
   "dt":"drainage layer · substrate mix · live plants · clean-up crew"}],
 "m":[["Zoo Med Low Boy Breeder Flat Terrarium","Zoo Med"],["Zoo Med Skyscraper Terrarium","Zoo Med"],["Zoo Med ReptiHabitat PRO 120","Zoo Med"],["Zoo Med Tortoise House","Zoo Med"],["Zoo Med Deluxe Outdoor Double Walled Tortoise House","Zoo Med"],["Zoo Med Tortoise Play-Pen","Zoo Med"],["Vivexotic Repti-Home","Vivexotic"]]},
{"n":"Reptile substrate","a":"bedding · vivarium substrate","d":"Floor material for a reptile enclosure.",
 "t":["coconut fibre and husk","bark and wood chips","aspen shavings","sand and calcium sand","clay burrowing substrate","bioactive soil mix","moss","reptile carpet"],
 "s":"https://www.petsmart.com/reptile/substrate-and-bedding/exo-terra-reptile-sand-mat-31914.html",
 "m":[["Zoo Med Eco Earth Coconut Fiber Substrate","Zoo Med"],["Zoo Med Eco Earth Coconut Chips","Zoo Med"],["Zoo Med ReptiBark","Zoo Med"],["Zoo Med Forest Floor Bedding","Zoo Med"],["Zoo Med Aspen Snake Bedding","Zoo Med"],["Zoo Med ReptiSand","Zoo Med"],["Zoo Med Excavator Clay Burrowing Substrate","Zoo Med"],["Zoo Med Tropical Bioblend","Zoo Med"],["Zoo Med ReptiSoil","Zoo Med"],["Zoo Med New Zealand Sphagnum Moss","Zoo Med"],["Zoo Med Eco Carpet","Zoo Med"],["Exo Terra Plantation Soil","Exo Terra"],["Exo Terra Coco Husk","Exo Terra"],["Exo Terra Forest Floor","Exo Terra"] if False else ["Exo Terra Tropical Forest Floor","Exo Terra"],["Exo Terra Bamboo Forest Floor","Exo Terra"],["Thrive Desert Natural Calcium Sand","Thrive"]]},
{"n":"Reptile hide","a":"hide · cave · shelter","d":"A shelter in which a reptile hides.",
 "t":["resin rock cave","coconut shell","cork bark","wooden hut","humid hide"],
 "s":"https://www.petsmart.com/reptile/habitats-and-decor/habitat-decor/thrive-rainforest-cave---reptile-hide-decor-91485.html",
 "m":[["Exo Terra Reptile Cave","Exo Terra"] if False else ["Exo Terra Reptile Den","Exo Terra"],["Exo Terra Gecko Cave","Exo Terra"],["Exo Terra Snake Cave","Exo Terra"],["Exo Terra Corner Cave","Exo Terra"],["Exo Terra Coconut Cave","Exo Terra"],["Exo Terra Tortoise Cave","Exo Terra"],["Exo Terra Rock Outcrops","Exo Terra"],["Exo Terra Canopy Cave","Exo Terra"],["Thrive Rainforest Cave","Thrive"],["Zoo Med Wooden Reptile Habba Hut","Zoo Med"]]},
{"n":"Misting and fogging system","a":"misting system · rain system · fogger","d":"A pump, timer and nozzles that spray water into an enclosure on a schedule to keep humidity up.",
 "t":["pump misting system","ultrasonic fogger","drip system"],"s":MK,
 "x":[
  {"n":"MistKing misting system","a":"MistKing","d":"Timer-driven 24 V diaphragm-pump misting kit with check-valved fine-spray nozzles, fed from any bucket reservoir; the hobby's reference system.","mk":"MistKing","y":"","s":MK,
   "v":[v("Starter Misting System v5.0","MistKing","","24 V pump for up to 10 nozzles, ST-24 seconds timer, 15 ft tubing"),v("Advanced Misting System","MistKing","","for setups above 10 nozzles"),v("Ultimate Misting System","MistKing","","for setups above 10 nozzles")],
   "dt":"nozzle count · reservoir size · timer type"},
  {"n":"Exo Terra Monsoon","a":"Monsoon RS400","d":"Compact programmable rain system with a built-in reservoir that mists several times a day; won a Pet Product News International Editor's Choice award.","mk":"Exo Terra","y":"2011","s":RM,
   "v":[v("Monsoon RS400","Exo Terra","2011","8.5 × 8.5 × 9 in, 4 L reservoir, optional remote")],
   "dt":"reservoir size · number of nozzles"}]},
{"n":"Reptile food","a":"reptile diet · gecko diet · pellets","d":"Prepared food made for reptiles and amphibians.",
 "t":["meal-replacement powder","pellets and sticks","gel diet","canned insects","flower food topper"],
 "s":"https://www.petsmart.com/reptile/reptile-shop/gecko-and-lizard/food",
 "x":[
  {"n":"Crested gecko meal-replacement powder","a":"MRP · CGD · complete gecko diet","d":"Fruit-based powder mixed one part to two parts water as the staple diet of crested, gargoyle and day geckos.","mk":"Repashy","y":"","s":MRP,
   "v":[v("Repashy Crested Gecko MRP Diet","Repashy","","the long-established original formula, min 23% protein"),v("Repashy Grubs 'N' Fruit Gecko Diet","Repashy"),v("Repashy Banana Cream Pie","Repashy"),v("Pangea Fruit Mix With Insects Complete Gecko Diet","Pangea Reptile","","over 60% fruit, cricket and black soldier fly larvae protein"),v("Pangea Fruit Mix Watermelon Complete Gecko Diet","Pangea Reptile"),v("Pangea Fruit Mix Banana Papaya Complete Gecko Diet","Pangea Reptile"),v("Zoo Med Crested Gecko Food","Zoo Med"),v("Exo Terra Crested Gecko Food","Exo Terra"),v("Fluker's Crested Gecko Banana and Mealworm Puree Diet","Fluker's")],
   "dt":"flavour · with or without insects · pot size"}],
 "m":[["Zoo Med Bearded Dragon Food","Zoo Med"],["Zoo Med Grassland Tortoise Food","Zoo Med"],["Zoo Med ReptiSticks Floating Aquatic Turtle Food","Zoo Med"],["Zoo Med Leopard Gecko Food","Zoo Med"],["Zoo Med Iguana Food","Zoo Med"],["Zoo Med Box Turtle Food","Zoo Med"],["Zoo Med Axolotl Food","Zoo Med"],["Zoo Med Pacman Frog Food","Zoo Med"],["Zoo Med Zoo Menu Blue Tongue Skink & Tegu Food","Zoo Med"],["Repashy Grassland Grazer","Repashy"],["Repashy Grub Pie","Repashy"],["Repashy Meat Pie","Repashy"],["Repashy Bluey Buffet","Repashy"],["Mazuri Tortoise Diet","Mazuri"],["Mazuri Bearded Dragon Diet","Mazuri"],["Hikari LeopaGel Leopard Gecko Diet","Hikari"],["Exo Terra Soft Pellets Bearded Dragon Food","Exo Terra"],["Exo Terra Dragon Grub","Exo Terra"]]},
{"n":"Frozen feeder animal","a":"frozen-thawed feeders · frozen rodents","d":"A dead frozen animal sold as food for reptiles; live feeders are not included.",
 "t":["mouse (pinkie to adult)","rat","day-old chick","quail","guinea pig","rabbit"],"s":"https://www.laynelabs.com/product/frozen-mice"},
{"n":"Reptile calcium and vitamin supplement","a":"calcium dust · D3 supplement · multivitamin","d":"Calcium and vitamin powder dusted onto feeder insects or food to prevent metabolic bone disease.",
 "t":["calcium without D3","calcium with D3","all-in-one calcium and multivitamin","multivitamin"],"s":CAL,
 "x":[
  {"n":"Repashy Calcium Plus","a":"","d":"All-in-one calcium dust with added vitamins, trace minerals and carotenoids, used at every insect feeding.","mk":"Repashy","y":"","s":CAL,
   "v":[v("Calcium Plus 6 oz","Repashy")],"dt":"pot size"},
  {"n":"Zoo Med Repti Calcium","a":"Repti Calcium with D3","d":"Phosphorus-free ultra-fine precipitated calcium carbonate dust with vitamin D3.","mk":"Zoo Med","y":"","s":ZCAL,
   "v":[v("Repti Calcium with D3","Zoo Med","","38–43% calcium, 85 g and 227 g")],"dt":"pot size"}]},
{"n":"Invertebrate enclosure","a":"tarantula enclosure · insect enclosure · mantis cage","d":"A small, escape-proof enclosure for tarantulas, scorpions, mantises and other invertebrates.",
 "t":["terrestrial","arboreal (tall)","fossorial (deep substrate)","sliding-lid acrylic","mesh mantis cage","plastic breeding box"],"s":TC,
 "x":[
  {"n":"Acrylic tarantula enclosure","a":"Tarantula Cribs","d":"Clear acrylic box made for tarantula keeping, with cross-ventilation and a sliding or hinged lid.","mk":"Tarantula Cribs","y":"","s":TC,
   "v":[v("Tarantula Cube","Tarantula Cribs"),v("Small Slider Crib Clear Edition","Tarantula Cribs"),v("The Canopy Sliding Lid","Tarantula Cribs")],
   "dt":"terrestrial, arboreal or fossorial layout · size · lid style"}]},
{"n":"Formicarium","a":"ant farm · ant nest · outworld","d":"A nest for keeping an ant colony, usually joined to a foraging area called an outworld.",
 "t":["sandwich (soil between panes)","acrylic","3D-printed","plaster","autoclaved aerated concrete (Ytong)","gel","test tube set-up","outworld"],"s":W+"Formicarium",
 "x":[
  {"n":"Sandwich ant farm","a":"Janet nest · Ant Farm","d":"Thin glass or plastic box filled with soil or sand so tunnels show; devised by Charles Janet, shown in Paris in 1900, sold commercially from about 1929.","mk":"","y":"1900","s":W+"Formicarium",
   "v":[v("Frank Eugene Austin formicarium","Frank Eugene Austin","1929","first commercially sold formicarium; patented 1931"),v("Uncle Milton Ant Farm","Uncle Milton Industries","1956","trademarked Ant Farm")],
   "dt":"fill (soil, sand, gel) · frame scenery"},
  {"n":"Ytong formicarium","a":"AAC nest","d":"Nest carved into an aerated concrete block with a glued glass top and a water hole to keep it damp.","mk":"","y":"","s":ANT,
   "v":[],"dt":"block size · water reservoir · connection to an outworld"}]}]
brands=[
 {"n":"Exo Terra","c":"Canada","f":"","seg":"Reptile and amphibian equipment","d":"Terrarium, heating, lighting and food brand of the Hagen group.","lines":["Glass Terrarium","Monsoon","Plantation Soil"],"eras":[],"sig":["Exo Terra Glass Terrarium","Exo Terra Monsoon"],"sc":[],"rel":["Zoo Med"],"s":"knowledge"},
 {"n":"Zoo Med","c":"United States","f":"","seg":"Reptile and amphibian equipment","d":"Californian maker of reptile enclosures, lighting, heating, substrates and foods.","lines":["ReptiBreeze","ReptiSun","Eco Earth","Repti Calcium"],"eras":[],"sig":["Zoo Med ReptiBreeze","Zoo Med Repti Calcium"],"sc":[],"rel":["Exo Terra"],"s":"knowledge"},
 {"n":"Vivexotic","c":"United Kingdom","f":"","seg":"Wooden vivaria","d":"British maker of flat-pack wooden vivaria and cabinets.","lines":["Repti-Home"],"eras":[],"sig":["Wooden vivarium"],"sc":[],"rel":[],"s":"knowledge"},
 {"n":"Kages","c":"United States","f":"","seg":"PVC reptile enclosures","d":"Handmade expanded-PVC reptile enclosures with glass sliding doors.","lines":["Premium PVC Reptile Enclosure"],"eras":[],"sig":["PVC reptile enclosure"],"sc":["bioactive"],"rel":[],"s":PVC},
 {"n":"MistKing","c":"","f":"","seg":"Misting systems","d":"Specialist maker of pump misting systems for terraria.","lines":["Starter","Advanced","Ultimate"],"eras":[],"sig":["MistKing misting system"],"sc":[],"rel":[],"s":MK},
 {"n":"Repashy","c":"United States","f":"","seg":"Reptile diets and supplements","d":"Maker of meal-replacement powders, gel diets and calcium supplements for reptiles.","lines":["Superfoods","Calcium Plus"],"eras":[],"sig":["Crested gecko meal-replacement powder","Repashy Calcium Plus"],"sc":[],"rel":["Pangea Reptile"],"s":MRP},
 {"n":"Tarantula Cribs","c":"","f":"","seg":"Acrylic invertebrate enclosures","d":"Acrylic tarantula enclosures made by tarantula keepers.","lines":["Tarantula Cube","Slider Crib"],"eras":[],"sig":["Acrylic tarantula enclosure"],"sc":[],"rel":[],"s":TC},
 {"n":"Uncle Milton Industries","c":"United States","f":"","seg":"Toy ant farms","d":"Milton Levine's company that trademarked the Ant Farm in 1956.","lines":["Ant Farm"],"eras":["Milton Levine, founder"],"sig":["Sandwich ant farm"],"sc":[],"rel":[],"s":W+"Formicarium"}]
notes=("Merged old Vivarium/substrate/hide/food/frozen feeder kinds; models that are versions of the Exo Terra glass terrarium, ReptiBreeze, Vivexotic, paludarium and gecko-diet archetypes moved into x. "
 "Trimmed SKU lists: substrate 25->16, hide 14->10, food 53 flat -> 9 versions + 18 flat (dropped duplicate Zoo Med Gourmet/Zoo Menu lines, flower toppers, treats). Frozen feeder animal had maker-less 'models' (mouse, rat, chick...) - now types. "
 "Dropped repeated 'Exo Terra reptile range' r entries (range repeated across kinds is a finding). Not added for want of a retrieved page: Animal Plastics (only forum mentions found), Zoo Med ReptiFogger, Arcadia supplements, Exo Terra Monsoon Solo/Multi II specs (retailer listings only in search), Tar Heel Ants/AntsCanada products. "
 "Brand founding years left blank where unconfirmed. Year 1900 for sandwich ant farm = Charles Janet's exhibit (Wikipedia).")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='work/B10/shelves/07_00.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
