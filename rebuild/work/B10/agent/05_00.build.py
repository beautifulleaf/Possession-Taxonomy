import json,os
Z="https://zooplus.co.uk/shop/birds/cage_accessories"
K=[]
K.append({"n":"Bird cage","a":"birdcage · parrot cage · flight cage","d":"A wire cage in which a pet bird is kept indoors.",
 "t":["small-bird flight cage","parrot cage","dome top","play top","open top","square/flat top","table-top","on stand","stainless steel","powder-coated","bar spacing by species"],
 "s":"https://www.omlet.us/guide/parakeets/parakeet_cages/",
 "m":[["Hagen Vision Bird Cage","Rolf C. Hagen"],["Prevue Hendryx Cockatiel & Parakeet Flight Cage","Prevue Pet Products"],["Prevue Hendryx Bird Flight Cage with Stand","Prevue Pet Products"],["Prevue Hendryx Playtop Bird Cage","Prevue Pet Products"],["Prevue Hendryx Powder Coated Parrot Cage","Prevue Pet Products"],["Prevue Hendryx Stainless Steel Small Parrot Cage","Prevue Pet Products"],
      ["Ferplast Piano 6 Bird Cage","Ferplast"],["Montana Sydney I","Montana"],["A&E Cage Company Elegant Flight Cage","A&E Cage Company"],["A&E Cage Company Triple Top Victorian Cage","A&E Cage Company"],
      ["HQ Cages Dome Top Parrot Cage","HQ Cages"],["HQ Cages Play Top Parrot Cage","HQ Cages"],["HQ Cages Superior Series Extra Flight Cage","HQ Cages"],["Omlet Geo Bird Cage","Omlet"]]})
K.append({"n":"Aviary","a":"outdoor aviary · garden aviary · flight and shelter","d":"A walk-in enclosure large enough for birds to fly, usually a wire-mesh flight with a covered shelter.",
 "t":["outdoor flight with shelter","indoor aviary","grounded (concrete base)","suspended","wooden frame","metal frame","double aviary"],
 "s":"https://en.wikipedia.org/wiki/Aviary",
 "m":[["Montana Sydney I","Montana"],["Savic Gite Aviary","SAVIC"]]})
K.append({"n":"Cage-bird food","a":"bird seed · parrot pellets · egg food · millet spray","d":"Seed mix, pellets, egg food, nectar or treats made for pet cage and aviary birds; wild-bird food is under Wild bird food.",
 "t":["seed mix","pellets / extruded","egg food","lory nectar","millet spray","treats","hand-rearing formula"],
 "s":"https://www.petco.com/category/bird",
 "m":[["Versele-Laga Prestige Premium Budgie","Versele-Laga"],["Versele-Laga Prestige Premium Parrots","Versele-Laga"],["Versele-Laga Prestige Tropical Finches","Versele-Laga"],["NutriBird P15 Original","Versele-Laga"],["NutriBird A21","Versele-Laga"],
      ["Harrison's Adult Lifetime","Harrison's Bird Foods"],["Harrison's High Potency","Harrison's Bird Foods"],
      ["ZuPreem FruitBlend","ZuPreem"],["ZuPreem Natural","ZuPreem"],["Roudybush Daily Maintenance","Roudybush"],
      ["Lafeber Nutri-Berries Original","Lafeber Company"],["Kaytee Supreme Cockatiel","Kaytee"],["Hari Tropican High Performance","Rolf C. Hagen"],["Hari Tropimix","Rolf C. Hagen"],
      ["Psittacus Maintenance High Energy","Psittacus Catalonia"],["Psittacus Lory Nectar","Psittacus Catalonia"],["TOP's Organic Parrot Food","TOP's Parrot Food"],["Higgins Sunburst Gourmet Blend","Higgins Premium Pet Foods"],["Vitakraft Menu Budgie","Vitakraft pet care"]]})
K.append({"n":"Cage-bird feeder or drinker","a":"seed cup · bird bowl · water bottle","d":"A cup, dish, hopper or drinker fitted to a bird cage.",
 "t":["clip-on cup","stainless crock","hooded / mess-less feeder","seed silo","tube drinker","aviary hopper"],
 "s":Z,
 "m":[["Hagen Vision Seed/Water Cup","Rolf C. Hagen"],["Lixit Stainless Steel Cage Crock Bowl With Bracket","Lixit"],["JW Pet InSight Clean Cup Feed and Water Cup","JW Pet"],["JW Pet InSight Clean Seed Silo Bird Feeder","JW Pet"],["Living World XL Seed Cup with Wire Hooks","Living World"],["Featherland Paradise Mess-Less Hooded Bird Feeder","Featherland Paradise"],["Featherland Paradise Easy Sure Lock Bird Cup","Featherland Paradise"],["Parrot Lumber Bird Diner","Parrot Lumber"],["Riga White Plastic Aviary Feeder","Riga"]]})
K.append({"n":"Bird perch","a":"perch · play stand","d":"A rod, branch or platform fitted in a cage for a bird to stand on.",
 "t":["natural wood branch","rope","sand / grooming","concrete / pumice","platform / shelf","calcium perch"],
 "s":Z,
 "m":[["A&E Cage Company Java Multi-Branch Coffee Wood Perch","A&E Cage Company"],["JW Pet Comfy Rope Perch","JW Pet"],["JW Pet Sand Perch","JW Pet"],["Polly's Pet Products Feather Weight Nail Perch","Polly's Pet Products"],["Polly's Pet Products Tooty Fruity Bee Pollen Calcium Perches","Polly's Pet Products"],["Prevue Hendryx Birdie Basics Perches","Prevue Pet Products"],["Parrot Lumber Corner Perch Parrot Platform","Parrot Lumber"],["Zoo-Max Cage Corner Shelf Perch","Zoo-Max"],["Living World Multi-Coloured Cotton Perch","Living World"]]})
K.append({"n":"Bird toy","a":"parrot toy · foraging toy","d":"An object made for a cage bird to chew, forage, climb or play with.",
 "t":["chew / shredding","foraging","swing","ladder","bell and mirror","preening","rattle / ball"],
 "s":Z,
 "m":[["Wesco Pet Original Bird Kabob","Wesco Pet"],["Wesco Pet Mini Bird Kabob","Wesco Pet"],["All Living Things Refillable Foraging Bird Toy","All Living Things"],["All Living Things Knots & Blocks Bird Toy","All Living Things"],["All Living Things Sola Ball Bird Toy","All Living Things"],["All Living Things Seagrass Ball Bird Toy","All Living Things"],["All Living Things Vine Mat Bird Foraging Toy","All Living Things"],["All Living Things Pinata Bird Toy","All Living Things"]]})
K.append({"n":"Cage-bird nest box","a":"nest box · nest pan","d":"A nest box or nest pan fitted to a cage or aviary for breeding birds.",
 "t":["wooden box","plastic box","L-shaped box","cane / wicker nest","coconut nest","nest pan"],
 "s":Z,
 "m":[["Prevue Hendryx Parakeet (Budgie) Nest Box","Prevue Pet Products"],["Prevue Hendryx Cockatiel Nest Box","Prevue Pet Products"],["Prevue Hendryx Lovebird Nest Box","Prevue Pet Products"],["Hagen Parakeet Nest Box","Rolf C. Hagen"],["2GR Nido Paradise Plastic Nest Box","2GR"],["Exotic Wings L-Nest Box","Exotic Wings"],["AviaryPlus Gouldian/Finch Nesting Box","AviaryPlus"],["Brooklands Cane Canary Nest","Brooklands"],["Brooklands Plastic Nest Pans","Brooklands"],["Brooklands Coconut Finch Nest","Brooklands"]]})
B=[
 {"n":"Rolf C. Hagen","c":"Canada","seg":"Pet supplies","d":"Canadian pet-supply maker whose bird lines include Vision cages and Hari Tropican food.","lines":["Vision","Hari","Tropican"],"s":"knowledge"},
 {"n":"Prevue Pet Products","c":"United States","seg":"Bird cages and accessories","d":"US maker of bird cages, perches and nest boxes under the Prevue Hendryx name.","lines":["Prevue Hendryx"],"s":"knowledge"},
 {"n":"Ferplast","c":"Italy","seg":"Pet supplies","d":"Italian pet-supply maker of cages, aquariums and accessories.","lines":["Piano"],"s":"https://www.zooplus.co.uk/shop/birds/bird_cages_and_accessories/ferplast/2123735"},
 {"n":"Montana","seg":"Bird cages and aviaries","d":"Brand of large parrot cages and indoor aviaries, expandable with extension kits.","lines":["Sydney"],"s":"https://www.interzoo.com/en/exhibitors/wagner-pet-products-group-2499768/premium-aviary-new-sydney-i-bird-cage-for-parakeets-and-small-parrots-2328781"},
 {"n":"Versele-Laga","c":"Belgium","seg":"Animal food","d":"Belgian animal-food maker; Prestige seed mixes and NutriBird pellets for cage birds.","lines":["Prestige","NutriBird"],"s":"knowledge"},
 {"n":"Harrison's Bird Foods","c":"United States","seg":"Bird food","d":"Certified-organic pelleted bird food sold mainly through vets.","lines":["Adult Lifetime","High Potency"],"s":"knowledge"},
 {"n":"ZuPreem","c":"United States","seg":"Bird and small-animal food","d":"US maker of extruded pellet diets for parrots and other birds.","lines":["FruitBlend","Natural","VeggieBlend"],"s":"knowledge"},
 {"n":"Roudybush","c":"United States","seg":"Bird food","d":"US maker of pelleted bird diets.","s":"knowledge"}]
notes=("Kept all 6 old kinds; added Aviary (new, sourced to Wikipedia 'Aviary'; Omlet aviary guide for flight/shelter layout). Tier shelf: no archetypes. "
 "Trimmed SKU lists: Bird cage 19 to 14 (added Ferplast Piano 6 and Montana Sydney I from retrieved pages; Savic Gite Aviary moved to Aviary); food 61 to 19 across Versele-Laga, Harrison's, ZuPreem, Roudybush, Lafeber, Kaytee, Hagen, Psittacus, TOP's, Higgins, Vitakraft; "
 "bird toys 37 to 8 (33 All Living Things variants cut); smaller trims to feeders, perches, nest boxes; attributes moved to t. "
 "No Montana Paradiso/Arkansas models named (Arkansas page 404, Paradiso only seen in search snippets). Prevue aviary/flight products not added (not retrieved). YPC retailer page 403. No traditions apply.")
out={"kinds":K,"brands":B,"traditions":[],"notes":notes}
p='work/B10/shelves/05_00.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
