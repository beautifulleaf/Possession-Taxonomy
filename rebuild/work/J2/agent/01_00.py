import json,os
W="https://en.wikipedia.org/wiki/"
K=[
{"n":"Pacific oyster","a":"Magallana gigas · Crassostrea gigas · huître creuse · Japanese oyster","d":"The most widely farmed oyster, sold live in the shell, on the half shell or shucked, named by growing area.",
 "t":["live","half-shell","shucked","size grade 0 to 5"],
 "s":"https://www.thefishsociety.co.uk/",
 "x":[
 {"n":"Marennes-Oléron PGI","a":"Huîtres Marennes Oléron PGI · claire oysters","d":"Oysters grown and finished in clay ponds (claires) of the Marennes-Oléron basin, Nouvelle-Aquitaine.","mk":"","y":"","s":"https://tastefrance.com/essentials/sea-food/marennes-oleron-oysters-pgi",
  "v":[{"n":"Fine de claire","mk":"","y":"","d":"28 days in a claire, lean"},{"n":"Spéciale de claire","mk":"","y":"","d":"selected for size and shape, plumper"},{"n":"Fine de claire verte","mk":"","y":"1989","d":"Label Rouge, green gills; first seafood product to get Label Rouge"},{"n":"Pousse en claire","mk":"","y":"","d":"Label Rouge, 4 to 8 months at low density"}],
  "dt":"size 0 (largest) to 5 · green gills from Blue Navicula algae"},
 {"n":"Gillardeau Spéciale","a":"Spéciale Gillardeau","d":"Branded Marennes-Oléron-basin oysters grown up to four years, laser-marked with a G.","mk":"Gillardeau","y":"1898","s":"https://www.secretsfinefood.com/farmer/gillardeau.html","dt":"grades N4, N3, N2 · laser-marked G"}
 ],
 "m":[["Breton and Charent Sea Born Oyster",""],["Huître de Normandie PGI",""],["고흥굴 GI",""]]},
{"n":"Native flat oyster","a":"Ostrea edulis · European flat oyster · huître plate · Colchester native · mud oyster","d":"The European flat oyster Ostrea edulis, round-shelled and prized raw, named by estuary.",
 "t":["live","half-shell","size grade"],
 "s":W+"Ostrea_edulis",
 "x":[
 {"n":"Belon","a":"Belon River oyster · huître de Belon","d":"Flat oysters cultivated in the Belon River estuary, Brittany, holding the protected Belon name; US 'Belon' is unrelated to the French product.","mk":"","y":"","s":W+"Ostrea_edulis","dt":"Brittany · Belon River · protected name"},
 {"n":"Colchester Native","a":"Colchester native oyster","d":"British and Irish name for the native flat oyster.","mk":"","y":"","s":W+"Ostrea_edulis","dt":"Great Britain and Ireland"},
 {"n":"Fal Oyster PDO","a":"Truro River oyster","d":"Native oysters dredged under sail and oar on the Fal, the last commercially viable native fishery in the UK.","mk":"","y":"","s":"https://cornwallgoodseafoodguide.org.uk/fish-guide/native-oyster.php","dt":"hand-hauled dredges · closed 1 April to 30 September · managed by Cornwall IFCA"},
 {"n":"Malostonska kamenica PDO","a":"Mali Ston oyster","d":"Oysters of Mali Ston Bay, Croatia, given EU PDO in October 2020.","mk":"","y":"2020","s":"https://www.croatiaweek.com/oysters-from-mali-ston-become-28th-croatian-product-awarded-eu-protection/","dt":"Mali Ston Bay, Pelješac"}
 ]},
{"n":"Eastern oyster","a":"Crassostrea virginica · American oyster · Atlantic oyster · East Coast oyster","d":"The oyster of eastern North America, sold under the name of its bay or town.",
 "t":["live","half-shell","shucked"],
 "s":W+"Eastern_oyster",
 "x":[
 {"n":"Blue Point","a":"","d":"Eastern oyster named for Blue Point, New York.","mk":"","y":"","s":W+"Eastern_oyster","dt":"Long Island"},
 {"n":"Wellfleet","a":"","d":"Eastern oyster named for Wellfleet, Cape Cod, Massachusetts.","mk":"","y":"","s":W+"Eastern_oyster","dt":"Cape Cod"},
 {"n":"Malpeque","a":"","d":"Eastern oyster from Malpeque Bay, Prince Edward Island.","mk":"","y":"","s":W+"Eastern_oyster","dt":"Prince Edward Island"},
 {"n":"Chesapeake Bay oyster","a":"","d":"Eastern oyster from Chesapeake Bay, long heavily harvested.","mk":"","y":"","s":W+"Eastern_oyster","dt":"Chesapeake Bay"},
 {"n":"Apalachicola","a":"","d":"Eastern oyster from Apalachicola, Florida.","mk":"","y":"","s":W+"Eastern_oyster","dt":"Gulf of Mexico"}
 ]},
{"n":"Kumamoto oyster","a":"Magallana sikamea · Crassostrea sikamea · Kumie","d":"Small, slow-growing oyster of Kumamoto, Japan, farmed on the US West Coast and noted for a fruity, melon-like flavour.",
 "t":["live","half-shell","shucked"],
 "s":W+"Kumamoto_oyster",
 "x":[{"n":"West Coast Kumamoto","a":"","d":"Kumamoto oysters cultured in Puget Sound, Humboldt Bay, Tomales Bay and Morro Bay since 1947.","mk":"","y":"1947","s":W+"Kumamoto_oyster","dt":"about 6 cm · about three years to market"}]},
{"n":"Sydney rock oyster","a":"Saccostrea glomerata","d":"Native Australian oyster farmed in the estuaries of New South Wales and southern Queensland, eaten freshly shucked.",
 "t":["live","half-shell","shucked"],
 "s":W+"Saccostrea_glomerata",
 "x":[{"n":"New South Wales estuary rock oyster","a":"","d":"Sydney rock oyster farmed in sheltered NSW and southern Queensland estuaries; Georges River farming ended in 2023.","mk":"","y":"","s":W+"Saccostrea_glomerata","dt":"two years to market after selective breeding"}]}
]
B=[{"n":"Gillardeau","c":"France","f":"1898","seg":"Premium","kf":"Spéciale oysters","d":"Family oyster house of the Marennes-Oléron basin, laser-marking each oyster with a G.","lines":["Spéciale Gillardeau"],"eras":[],"sig":["Gillardeau Spéciale"],"sc":[],"rel":[],"s":"https://www.secretsfinefood.com/farmer/gillardeau.html"}]
T=[{"n":"Marennes-Oléron claire affinage","g":"Food & drink","r":"Nouvelle-Aquitaine, France","p":"mid-19th century onward","d":"Finishing oysters in shallow clay ponds left from old salt marshes, where Blue Navicula algae colours the gills green.","tech":"affinage in claires, 28 days up to 8 months","mat":"clay ponds, tidal fresh and salt water","forms":["Fine de claire","Spéciale de claire","Fine de claire verte","Pousse en claire"],"ctr":["Marennes-Oléron basin"],"auth":"PGI and Label Rouge labels","s":"https://tastefrance.com/essentials/sea-food/marennes-oleron-oysters-pgi"}]
out={"kinds":K,"brands":B,"traditions":T,"notes":"Old Oyster kind became Pacific oyster; Fal and Malostonska moved to Native flat oyster as archetypes (species per brief). Breton and Charentes Sea Born, Normandie PGI and Goheung GI kept as flat models (no retrieved page). Not added for lack of a retrieved page: Kusshi, Fanny Bay, Kumiai, Galway, Limfjord, Island Creek. Coffin Bay is Pacific per brief, not added."}
p='work/J2/shelves/01_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1);os.replace(p+'.tmp',p)
