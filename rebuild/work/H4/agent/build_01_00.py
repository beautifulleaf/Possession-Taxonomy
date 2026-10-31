import json, os
SC="https://www.scento.com/blog/best-perfume-discovery-sets-europe-picks-reviewed"
NST="https://nstperfume.com/2016/12/06/holiday-fragrance-gifts-2016-part-4"
BOHA="https://www.bohaglass.co.uk/intimate-history-miniature-perfume-bottles/"
kinds=[
{"n":"Sample vial","a":"perfume sample · manufacturer sample · tester vial","d":"Small manufacturer or retailer vial of a fragrance, given free at counters or with orders to try before buying.",
 "t":["dab vial (1–2 ml)","spray vial (1–2 ml)","scent card / scent strip insert","factory-filled vs retailer-decanted"],
 "s":"https://www.scento.com/what-is-a-perfume-decant"},
{"n":"Decant","a":"perfume decant · split · decant atomiser","d":"Genuine fragrance hand-poured from a full bottle into a small vial or glass atomiser, sold by the millilitre.",
 "t":["partial vial (¼–½ ml)","1 ml dab vial","glass spray 2–3 ml","glass spray 5 ml","glass spray 8–10 ml","30 ml travel decant","build-your-own decant set"],
 "s":"https://surrendertochance.com/perfume-decant-what-is-it/",
 "r":[["Decants & samples","Surrender to Chance"],["Decants & Discovery Picks (2–30 ml)","Scento"]]},
{"n":"Discovery set","a":"sampler set · fragrance wardrobe · scent library · discovery kit","d":"House-made boxed set of small vials or sprays covering part of a line, bought to explore before a full bottle.",
 "t":["vial set (1.5–2 ml)","spray set (4–10 ml)","pick-your-own set","set with full-bottle voucher"],
 "s":SC,
 "x":[
  {"n":"Le Labo Discovery Set","a":"","d":"Le Labo's boxed set of its fragrances in small sprays.","mk":"Le Labo","y":"","s":SC,
   "v":[{"n":"Signature Discovery Set","mk":"Le Labo","y":"","d":"3 × 7 ml"},{"n":"Exclusive Discovery Set","mk":"Le Labo","y":"","d":"4 × 5 ml"}],"dt":"vial count · spray size · city exclusives vs classics"},
  {"n":"Diptyque Discovery Set","a":"","d":"Diptyque's boxed set of five fragrances in 7.5 ml sprays.","mk":"Diptyque","y":"","s":SC,
   "v":[{"n":"Discovery Set (standard)","mk":"Diptyque","y":"","d":"5 × 7.5 ml"},{"n":"To Compose","mk":"Diptyque","y":"","d":"choose 5 from 11"}],"dt":"fixed or chosen selection · spray size"},
  {"n":"Replica Memory Box","a":"Replica discovery set","d":"Maison Margiela's sampler box of its Replica fragrances.","mk":"Maison Margiela","y":"","s":SC,
   "v":[{"n":"Memory Box","mk":"Maison Margiela","y":"","d":"10 × 2 ml"}],"dt":"number of Replica scents · vial size"},
  {"n":"Byredo Discovery Set","a":"","d":"Byredo's themed boxes of 2 ml vials.","mk":"Byredo","y":"","s":SC,
   "v":[{"n":"Nomade","mk":"Byredo","y":"","d":"6 × 2 ml"},{"n":"Floral","mk":"Byredo","y":"","d":"6 × 2 ml"},{"n":"Boisé","mk":"Byredo","y":"","d":"6 × 2 ml"},{"n":"La Grande Découverte","mk":"Byredo","y":"","d":"24 × 2 ml"}],"dt":"theme · vial count"},
  {"n":"Penhaligon's Scent Library","a":"","d":"Penhaligon's library-style boxes of 2 ml vials grouped by collection.","mk":"Penhaligon's","y":"","s":SC,
   "v":[{"n":"Classic Scent Library","mk":"Penhaligon's","y":"","d":"10 × 2 ml"},{"n":"Bestseller Library","mk":"Penhaligon's","y":"","d":"8 × 2 ml"},{"n":"Trade Routes Library","mk":"Penhaligon's","y":"","d":"8 × 2 ml"},{"n":"Portraits Library","mk":"Penhaligon's","y":"","d":"8 × 2 ml"}],"dt":"collection theme · vial count"},
  {"n":"Fragrance Wardrobe","a":"","d":"Maison Francis Kurkdjian's set of 2 ml sprays from its range.","mk":"Maison Francis Kurkdjian","y":"","s":SC,
   "v":[{"n":"Fragrance Wardrobe for Her / for Him","mk":"Maison Francis Kurkdjian","y":"","d":"8 × 2 ml"},{"n":"Custom set","mk":"Maison Francis Kurkdjian","y":"","d":"4 × 2 ml"}],"dt":"gendered or custom selection"},
  {"n":"Olfactive Studio Discovery Kit","a":"","d":"Olfactive Studio's kit of 4 ml minis covering its photography-themed line.","mk":"Olfactive Studio","y":"2016","s":NST,
   "v":[{"n":"Discovery Kit","mk":"Olfactive Studio","y":"2016","d":"7 × 4 ml"}],"dt":"vial count"}]},
{"n":"Gift set (coffret)","a":"coffret · fragrance gift set · holiday set","d":"Boxed fragrance set, often seasonal, pairing a bottle with minis, a travel spray or matching body products.",
 "t":["full bottle + travel spray","full bottle + body lotion / shower gel","miniature coffret","collection of mid-size bottles","spray + refill set","layering or accord set"],
 "s":NST,
 "m":[["Cologne Collection travel set","Hermès"],["L'Atelier de Givenchy set","Givenchy"],["Cologne Intense Collection","Jo Malone"],["Noël Miniatures Gift Set","Annick Goutal"],["La Panthère set","Cartier"],["Parfum Collection (dabbers)","Christian Louboutin"],["Graceful Arlésienne set","L'Occitane"]]},
{"n":"Perfume miniature","a":"perfume mini · miniature bottle · purse flacon","d":"Small retail bottle (typically 5–10 ml splash) replicating a full bottle, collected especially as vintage minis.",
 "t":["vintage miniature","modern miniature","splash vs mini spray","boxed vs unboxed","sealed vs opened","graduated set in case"],
 "s":BOHA,
 "x":[
  {"n":"Chanel No. 5 miniature","a":"No. 5 pocket flacon","d":"Small replica of the No. 5 bottle, the classic collectible perfume mini.","mk":"Chanel","y":"1934","s":BOHA,
   "v":[{"n":"Pocket flacon","mk":"Chanel","y":"1934","d":"smaller, cheaper purse bottle"},{"n":"Graduated set of three in fitted leather case","mk":"Chanel","y":"1940s–1960s","d":"sold as a cased trio"}],"dt":"size · parfum vs eau de toilette · case or box · fill level"},
  {"n":"Chantilly purse size","a":"","d":"Houbigant's Chantilly launched in a small bottle made to fit in a handbag.","mk":"Houbigant","y":"1941","s":BOHA,
   "v":[],"dt":"bottle and box condition"}]}
]
B=[
{"n":"Le Labo","c":"United States","f":"2006","seg":"Niche perfume house","d":"New York niche house founded by Eddie Roschi and Fabrice Penot; owned by Estée Lauder since 2014.","lines":[],"eras":[],"sig":["Santal 33","Thé Noir 29","Le Labo Discovery Set"],"sc":[],"rel":[],"s":"https://en.wikipedia.org/wiki/Le_Labo"},
{"n":"Diptyque","c":"France","f":"1961","seg":"Niche perfume & candle house","d":"Paris house started by Yves Coueslant, Christiane Gautrot and Desmond Knox-Leet; known for candles and eaux de toilette.","lines":[],"eras":[],"sig":["L'Eau","Philosykos","Do Son","Tam Dao","Diptyque Discovery Set"],"sc":[],"rel":["Byredo"],"s":"https://en.wikipedia.org/wiki/Diptyque"},
{"n":"Byredo","c":"Sweden","f":"2006","seg":"Niche perfume house","d":"Stockholm house founded by Ben Gorham; majority-owned by Puig since 2022.","lines":[],"eras":["Ben Gorham, 2006–2025"],"sig":["Green","Byredo Discovery Set"],"sc":[],"rel":["Penhaligon's"],"s":"https://en.wikipedia.org/wiki/Byredo"},
{"n":"Maison Margiela","c":"France","f":"1988","seg":"Fashion house with designer fragrance","d":"Paris fashion house founded by Martin Margiela and Jenny Meirens; sells the Replica fragrance line.","lines":["Replica"],"eras":["Martin Margiela, 1988–2009","John Galliano, 2014–2024","Glenn Martens, 2025–"],"sig":["Replica Memory Box"],"sc":[],"rel":[],"s":"https://en.wikipedia.org/wiki/Maison_Margiela"},
{"n":"Penhaligon's","c":"United Kingdom","f":"1870","seg":"Heritage perfume house","d":"London perfumer founded by court barber William Henry Penhaligon; owned by Puig since 2015.","lines":["Portraits","Trade Routes"],"eras":[],"sig":["Hammam Bouquet","Blenheim Bouquet","Penhaligon's Scent Library"],"sc":[],"rel":["Byredo"],"s":"https://en.wikipedia.org/wiki/Penhaligon%27s"},
{"n":"Houbigant","c":"France","f":"1775","seg":"Heritage perfume house","d":"Paris house founded by Jean-François Houbigant; Fougère Royale (1882) founded the fougère family.","lines":[],"eras":[],"sig":["Fougère Royale","Quelques Fleurs","Chantilly purse size"],"sc":[],"rel":[],"s":"https://en.wikipedia.org/wiki/Houbigant_Parfum"},
{"n":"Chanel","c":"France","f":"1910","seg":"Luxury fashion house with fine fragrance","d":"Paris house of Gabrielle Chanel, owned by the Wertheimer family; No. 5 (1921) is its defining perfume.","lines":["Les Exclusifs"],"eras":["Ernest Beaux, perfumer 1920–1961","Jacques Polge, perfumer 1978–2015","Olivier Polge, perfumer 2015–"],"sig":["No. 5","Chanel No. 5 miniature","Coco Mademoiselle","Bleu de Chanel"],"sc":[],"rel":[],"s":"https://en.wikipedia.org/wiki/Chanel"}]
notes=("New shelf (no old data). Ranges for decant services limited to the two services whose pages I retrieved (Surrender to Chance, Scento). "
 "Gift-set models are 2016 examples from one retrieved roundup, kept as illustrative, not market-covering. No archetypes for sample vial or gift set (no named patterns attested). "
 "Left out: Arcade ScentStrip (card sample origin; page fetch failed), vinaigrettes and perfume étuis (belong with Antique scent bottle on the Bottles shelf), "
 "brand entries for Maison Francis Kurkdjian and Olfactive Studio (no brand page retrieved; MFK Wikipedia 404). No traditions apply to this shelf. Discovery-set years unknown, left blank.")
out={"kinds":kinds,"brands":B,"traditions":[],"notes":notes}
p='work/H4/shelves/01_00.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
