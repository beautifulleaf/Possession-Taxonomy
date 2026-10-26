import json, os
W = 'https://en.wikipedia.org/wiki/'
kinds = [
 {"n":"Protein bar","a":"high-protein bar","d":"Snack bar sold for its high protein content, from whey, milk or plant protein, often low in sugar.",
  "t":["whey or milk protein","plant-based (vegan)","layered crisp bar","soft bar","vitamin-fortified"],
  "s":"https://www.questnutrition.com/collections/protein-bars",
  "m":[["Quest Protein Bar","Quest Nutrition"],["Grenade High Protein Bar (formerly Carb Killa)","Grenade"],["Barebells Protein Bar","Barebells"],["Barebells Vegan Protein Bar","Barebells"],["Fulfil Vitamin & Protein Bar","Fulfil"],["ONE x Hershey's Double Chocolate","ONE Brands"],["Clif Builder's","Clif Bar & Company"],["Nature Valley Protein bar","Nature Valley"]]},
 {"n":"Protein snack","a":"protein chips · protein cookie","d":"Snack other than a bar (chips, crisps, cookies, brownies) sold for its protein.",
  "t":["protein chips","protein crisps","protein cookie","protein brownie","savoury protein snack"],
  "s":"https://www.vitaminshoppe.com/t/quest-nutrition-protein-chips/categories/snacks",
  "m":[["Quest Protein Chips","Quest Nutrition"],["Quest Protein Cookie","Quest Nutrition"],["The Complete Cookie","Lenny & Larry's"],["Strong & Kind","Kind"]]},
 {"n":"Roasted & salted nuts","a":"salted peanuts · mixed nuts · monkey nuts (in shell)","d":"Peanuts, tree nuts or mixed nuts roasted and usually salted, sold as a ready-to-eat snack.",
  "t":["salted","lightly salted","unsalted","dry-roasted","oil-roasted","in shell","mixed nuts","peanuts","almonds","cashews","pistachios"],
  "s":W+"Mixed_nuts",
  "m":[["KP Nuts","KP Snacks"],["Planters peanuts","Planters"],["Blue Diamond roasted almonds","Blue Diamond Growers"]]},
 {"n":"Coated nuts","a":"honey-roasted nuts · glazed nuts · wasabi peas","d":"Nuts or legumes with a sweet, savoury or spicy coating, such as honey-roasted peanuts or wasabi peas.",
  "t":["honey-roasted","sweet-and-salty glazed","seasoned dry-roasted","wasabi-coated peas"],
  "s":W+"Honey-roasted_peanuts",
  "m":[["Planters Honey Roasted Peanuts","Planters"],["Honey roasted peanuts","The Sun Valley Nut Co."],["Honey roasted peanuts","King Nut"],["Beer Nuts","Beer Nuts"],["Hapi Wasabi Green Peas","Hapi"]]},
 {"n":"Trail mix","a":"snack mix","d":"Mix of nuts, dried fruit and sometimes granola or chocolate, made to carry on hikes.",
  "t":["nuts and raisins","with chocolate","tropical fruit","sweet and salty"],
  "s":W+"Trail_mix",
  "m":[["DAVID trail mix","David Sunflower Seeds"],["Graze snack mixes","Graze"]]},
 {"n":"Seed snack","a":"sunflower seeds · pumpkin seeds · pepitas","d":"Roasted, usually salted sunflower or pumpkin seeds, eaten in or out of the shell.",
  "t":["in shell","kernels","sunflower","pumpkin (pepitas)","flavoured (BBQ, ranch)"],
  "s":W+"Sunflower_seed",
  "m":[["DAVID Sunflower Seeds","David Sunflower Seeds"],["DAVID Pumpkin Seeds","David Sunflower Seeds"]]},
 {"n":"Granola & cereal bar","a":"cereal bar · muesli bar · breakfast bar","d":"Bar of oats or other cereals bound with syrup or honey, crunchy or chewy, sometimes coated.",
  "t":["crunchy","chewy","chocolate-coated","soft-baked breakfast bar","crisped-rice marshmallow square"],
  "s":W+"Granola",
  "m":[["Nature Valley Oats and Honey","Nature Valley"],["Nutri-Grain breakfast bar","Kellanova"],["Rice Krispies Treats","Kellanova"],["Rice Krispies Squares","Kellogg"],["Corny chocolate cereal bar","Corny"],["Kind Healthy Grains bar","Kind"],["Eat Natural cereal bar","Eat Natural"],["Jordans cereal bar","Jordans"]]},
 {"n":"Energy & sports bar","a":"energy bar · sports bar","d":"Cereal-based bar made to supply quick food energy, mainly for sport and endurance activity.",
  "t":["oat-based","high-carbohydrate race bar","women's bar"],
  "s":W+"Energy_bar",
  "m":[["Clif Bar","Clif Bar & Company"],["PowerBar","PowerBar"],["Luna Bar","Clif Bar & Company"]]},
 {"n":"Fruit & nut bar","a":"date bar · nut bar · raw bar","d":"Bar made mostly of dried fruit and nuts pressed together, often without added sugar.",
  "t":["date-based","whole-nut","cold-pressed","no added sugar"],
  "s":"https://en.wikipedia.org/wiki/L%C3%A4rabar",
  "m":[["Lärabar","Lärabar"],["Nakd raw fruit & nut bar","Nakd"],["Kind Fruit & Nut","Kind"],["Kind Nuts & Spices","Kind"],["Nature Valley Fruit and Nut","Nature Valley"]]},
 {"n":"Flapjack","a":"oat bar · oat slice","d":"Baked British oat bar of rolled oats, butter, brown sugar and golden syrup, cut into squares.",
  "t":["plain golden syrup","fruit","chocolate-topped","protein flapjack"],
  "s":W+"Flapjack_(oat_bar)"},
]
B = lambda n,c,f,seg,d,lines,sig,rel,s,eras=None: {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":lines,"eras":eras or [],"sig":sig,"sc":[],"rel":rel,"s":s}
brands = [
 B("Quest Nutrition","United States","2010","Protein bars and snacks","Protein bar, chip and cookie maker founded by Tom Bilyeu, Mike Osborn and Ron Penna; owned by Simply Good Foods since 2019.",["Quest Protein Bar","Quest Protein Chips","Quest Protein Cookie"],[],["Atkins Nutritionals"],W+"Quest_Nutrition",["Founders, 2010–2019","The Simply Good Foods Company, from 2019"]),
 B("Grenade","","2010","Protein bars","Protein bar and supplement brand whose bar, formerly Carb Killa, has been the best-selling in its segment since 2016; Mondelez brand.",["High Protein Bar (formerly Carb Killa)","protein shakes","protein spreads"],[],["Mondelez International"],"https://www.mondelezinternational.com/our-brands/grenade/"),
 B("Barebells","Sweden","2016","Protein bars","Swedish protein bar and milkshake brand of the Vitamin Well group, sold in about forty markets.",["Protein Bars","Soft Protein Bars","Vegan Protein Bars","Protein Milkshakes"],[],["Vitamin Well"],"https://barebells.co.uk"),
 B("Fulfil","Ireland","2016","Protein bars","Irish vitamin and protein bar brand; bars carry nine vitamins and 15–20 g protein.",["Fulfil Vitamin & Protein Bar"],[],[],"https://www.nutraingredients.com/Article/2019/09/09/How-Fulfil-took-the-protein-snack-market-by-storm/"),
 B("Lenny & Larry's","United States","1993","Protein snacks","California maker of protein cookies, brownies, bars and muffins.",["The Complete Cookie"],[],[],"https://www.foodbusinessnews.net/articles/6262-q-a-protein-cookie-company-on-the-cutting-edge"),
 B("KP Snacks","United Kingdom","1853","Nuts and savoury snacks","British snack maker ('Kenyon Produce') owned by Intersnack since 2012; brands include KP Nuts, Hula Hoops and McCoy's.",["KP Nuts","Hula Hoops","McCoy's","Tyrrells"],[],["Intersnack"],W+"KP_Snacks"),
 B("Planters","United States","","Nuts","American processed-nut brand known for its Mr. Peanut mascot; owned by Hormel Foods.",["Planters peanuts","Planters Honey Roasted Peanuts"],[],["Hormel Foods"],W+"Planters"),
 B("Blue Diamond Growers","United States","1910","Almonds","Sacramento almond-growers' cooperative selling roasted almonds, almond milk and crackers.",["roasted almonds","almond milk"],[],[],W+"Blue_Diamond_Growers"),
 B("Beer Nuts","United States","","Nuts","American brand of sweet-and-salty glazed peanuts sold as a bar snack.",["Beer Nuts"],[],[],W+"Beer_Nuts"),
 B("David Sunflower Seeds","United States","1926","Seeds","Fresno seed brand founded by David Der Hairabedian; owned by Conagra since 2001.",["Sunflower Seeds with Shells","Pumpkin Seeds","trail mix"],[],["Conagra Brands"],"https://en.wikipedia.org/wiki/David_Sunflower_Seeds"),
 B("Nature Valley","United States","","Granola and cereal bars","General Mills brand of crunchy, protein and fruit-and-nut bars.",["Oats and Honey","Fruit and Nut","Protein bars"],[],["General Mills","Lärabar"],W+"Nature_Valley"),
 B("Clif Bar & Company","United States","1992","Energy bars","Emeryville maker of Clif Bar, Luna and Builder's; owned by Mondelez since 2022.",["Clif Bar","Luna Bar","Clif Builder's"],[],["Mondelez International"],"https://en.wikipedia.org/wiki/Clif_Bar",["Gary Erickson and Kit Crawford","Mondelez International, from 2022"]),
 B("PowerBar","United States","1986","Energy bars","Energy bar, gel and drink brand; Nestlé from 2000, Post Holdings/BellRing Brands from 2014.",["PowerBar"],[],["Premier Protein","Dymatize"],W+"PowerBar"),
 B("Kind","United States","2004","Fruit and nut bars","New York snack company founded by Daniel Lubetzky; a Mars subsidiary since 2020.",["Kind Fruit & Nut","Kind Nuts & Spices","Kind Healthy Grains","Strong & Kind"],[],["Mars Inc."],"https://en.wikipedia.org/wiki/Kind_(company)"),
 B("Lärabar","United States","","Fruit and nut bars","General Mills brand of fruit-and-nut energy bars.",["Lärabar"],[],["General Mills","Nature Valley"],"https://en.wikipedia.org/wiki/L%C3%A4rabar"),
 B("Eat Natural","United Kingdom","1997","Cereal bars","Essex maker of cereal bars, toasted muesli and granola.",["cereal bars","granola"],[],[],W+"Eat_Natural"),
]
notes = ("Tier shelf: both old kinds kept (Protein bar, Protein snack, old s retained); 8 new kinds sourced from Wikipedia pages retrieved via the wiki API. "
 "Models only where a retrieved page names them. Left out: Pure Protein (no reliable page retrieved), Quaker Chewy, Tracker, Trek and Nakd maker details (pages 403 or snippet-only), "
 "Corny founding year (snippet only), any Which?/test winners (no independent test found). Flapjack has no models (no retrieved page named a brand). "
 "Rice-crispy bars sit as a type of Granola & cereal bar. Chocolate-coated nuts belong to the Chocolate department. No archetypes (tier kinds) and no traditions.")
out = {"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='work/J8/shelves/05_00.json'; json.dump(out, open(p+'.tmp','w'), ensure_ascii=False, indent=1); os.replace(p+'.tmp', p)
