import json, os
DIP="https://en.wikipedia.org/wiki/Diptyque"
MB="https://www.maison-berger.com/pages/about-us"
MBB="https://maison-berger.com/blogs/inspirations/over-120-years-of-beauty-and-function"
kinds=[
 {"n":"Reed diffuser","a":"reed diffuser set · scent surround diffuser","d":"Vessel of scented oil with reeds that draw it up and release it into a room.",
  "t":["glass vessel","ceramic vessel","rattan reeds","fibre reeds","refillable set"],
  "s":"https://www.target.com/c/candles-home-fragrance-decor/wood/-/N-5xtuaZ5y6vh",
  "m":[["Baies reed diffuser","Diptyque"],["Pomegranate Noir Scent Surround Diffuser","Jo Malone London"],["Reed diffuser","Maison Berger Paris"]]},
 {"n":"Electric diffuser","a":"aroma diffuser · plug-in diffuser · mist diffuser","d":"Powered device that releases fragrance or essential oil into a room.",
  "t":["ultrasonic (water mist)","nebulising (pure oil, no water)","plug-in scented oil","automatic timed spray","battery or USB"],
  "s":"https://www.centrepointstores.com/kw/en/buy-embellished-unscented-wall-plugin-diffuser/p/168336215",
  "x":[
   {"n":"Ultrasonic aroma diffuser (MUJI)","a":"MUJI aroma diffuser","d":"White cylindrical ultrasonic diffuser turning water and oil into cool mist, with built-in ambient lamp and timer.",
    "mk":"MUJI","y":"","s":"https://www.gardenista.com/products/ultrasonic-aroma-diffuser",
    "v":[{"n":"Original aroma diffuser","mk":"MUJI","y":"","d":"smaller tank"},{"n":"Large aroma diffuser","mk":"MUJI","y":"","d":"larger tank, about three times the output; 30/60/120/180-minute timer"}],
    "dt":"tank size · light settings · timer"},
   {"n":"Hourglass diffuser","a":"","d":"Diptyque's electric home fragrance diffuser shaped as an hourglass, using scent cartridges.",
    "mk":"Diptyque","y":"","s":DIP,"v":[],"dt":"scent cartridge"}],
  "m":[["Scented Oils plug-in","Air Wick"],["Essential Mist Diffuser","Air Wick"],["Freshmatic automatic spray","Air Wick"],["NOTICEables plug-in oil","Febreze"],["ScentPlug","Yankee Candle"],["Mist diffuser","Maison Berger Paris"]]},
 {"n":"Catalytic fragrance lamp","a":"Lampe Berger · catalytic lamp · fragrance lamp","d":"Glass or ceramic lamp whose heated catalytic burner diffuses fragrance from alcohol-based oil and destroys odours, without a flame.",
  "t":["crystal or glass body","porcelain or ceramic body","designer edition"],"s":MBB,
  "x":[{"n":"Lampe Berger","a":"diffuseur fumivore hygiénique","d":"The original catalytic lamp, designed by pharmacist Maurice Berger in 1898 to purify hospital air, later given a perfuming function.",
    "mk":"Maison Berger Paris","y":"1898","s":MB,
    "v":[{"n":"Crystal lamps with Lalique, Baccarat and Daum","mk":"Maison Berger Paris","y":"1930s","d":"glassmaker collaborations; over 100 lamp styles"},
         {"n":"Hand-painted porcelain and earthenware lamps","mk":"Maison Berger Paris","y":"post-war","d":"made when crystal was scarce"},
         {"n":"Lolita Lempicka collection","mk":"Maison Berger Paris","y":"","d":"designer partnership"},
         {"n":"Art Edition","mk":"Maison Berger Paris","y":"","d":"featured collection"}],
    "dt":"body material (crystal, glass, porcelain) · designer edition · burner and fragrance"}]},
 {"n":"Wax melt","a":"wax tart · wax cube","d":"Scented wax piece made to be melted in a warmer, not burned.","t":["clamshell","bar","cube"],
  "s":"https://www.target.com/c/candles-home-fragrance-decor/wood/-/N-5xtuaZ5y6vh",
  "m":[["Wax melts","Yankee Candle"],["Wax melts","Febreze"]]},
 {"n":"Wax warmer","a":"wax burner · oil burner · wickless candle warmer","d":"Burner or electric warmer made to melt wax melts or oil.",
  "t":["electric hotplate","bulb warmer","tealight burner","plug-in warmer"],
  "s":"https://www.target.com/c/candles-home-fragrance-decor/wood/-/N-5xtuaZ5y6vh",
  "m":[["Wax warmer","Scentsy"],["Wax warmer","Yankee Candle"]]},
 {"n":"Room spray","a":"room mist · air freshener spray","d":"Aerosol or pump spray made to scent a room.","t":["aerosol","pump spray","odour-neutralising"],
  "s":"https://spotlightstores.com/home/lighting/decorative-string-lights",
  "m":[["Air Effects","Febreze"],["Aerosol Spray","Air Wick"],["Room spray","Yankee Candle"],["Room spray","Diptyque"],["Bibliothèque Room Spray","Byredo"]]},
 {"n":"Diffuser oil","a":"fragrance oil · essential oil · diffuser refill","d":"Essential or fragrance oil sold for a diffuser or burner (an oil sold to treat a condition is in Health, Medical & Mobility).",
  "t":["essential oil","fragrance oil","reed diffuser refill","plug-in refill","catalytic lamp fragrance"],
  "s":"https://www.target.com/c/candles-home-fragrance-decor/wood/-/N-5xtuaZ5y6vh"},
 {"n":"Potpourri","a":"","d":"Mixture of dried scented plant material displayed to scent a room.","s":"https://www.ikea.com/gb/en/cat/home-fragrance-42926/"},
 {"n":"Scented sachet","a":"drawer sachet · lavender bag","d":"Small bag or pouch of scented material made to scent a drawer, wardrobe or room (an odour absorber is in Cleaning & Laundry).",
  "s":"https://www.ikea.com/gb/en/cat/home-fragrance-42926/"}]
brands=[
 {"n":"Diptyque","c":"France","f":"1961","seg":"Luxury fragrance & candle house","d":"Paris house founded by Yves Coueslant, Christiane Gautrot and Desmond Knox-Leet; scented candles from 1963; owned by Manzanita Capital since 2005.",
  "lines":["Candles","Reed diffusers","Room sprays","Hourglass diffuser","Car diffusers"],"eras":[],"sig":["Baies","Figuier","Hourglass diffuser"],"sc":[],"rel":["Byredo"],"s":DIP},
 {"n":"Jo Malone London","c":"United Kingdom","f":"1990","seg":"Luxury fragrance house","d":"London fragrance house founded by Jo Malone, owned by Estée Lauder Companies since 1999; known for perfumes, candles and room scents.",
  "lines":["Candles","Scent Surround diffusers","Room sprays"],"eras":[],"sig":["Wood Sage & Sea Salt"],"sc":[],"rel":[],"s":"https://en.wikipedia.org/wiki/Jo_Malone_London"},
 {"n":"Byredo","c":"Sweden","f":"2006","seg":"Luxury fragrance house","d":"Stockholm house founded by Ben Gorham; majority-owned by Puig since 2022.",
  "lines":["Candles","Room sprays"],"eras":["Ben Gorham, 2006–2025"],"sig":["Bibliothèque"],"sc":[],"rel":["Diptyque"],"s":"https://en.wikipedia.org/wiki/Byredo"},
 {"n":"Maison Berger Paris","c":"France","f":"1898","seg":"Home fragrance house","d":"Maker of the Lampe Berger catalytic lamp, designed by Maurice Berger in 1898; renamed from Lampe Berger in 2018.",
  "lines":["Catalytic lamps","Reed diffusers","Mist diffusers","Scented candles","Car diffusers"],"eras":[],"sig":["Lampe Berger"],"sc":[],"rel":[],"s":MBB},
 {"n":"MUJI","c":"Japan","f":"1980","seg":"No-brand household goods retailer","d":"Japanese retailer of plain household goods, clothing and food.","lines":["Aroma diffusers","Essential oils"],"eras":[],"sig":["Ultrasonic aroma diffuser"],"sc":[],"rel":[],"s":"knowledge"},
 {"n":"Yankee Candle","c":"United States","f":"1969","seg":"Mass-market candles & home fragrance","d":"Massachusetts candle maker founded by Michael Kittredge II, owned by Newell Brands.","lines":["Candles","Wax melts and warmers","ScentPlug","Room sprays","Car scents"],"eras":[],"sig":[],"sc":[],"rel":[],"s":"https://en.wikipedia.org/wiki/Yankee_Candle"},
 {"n":"Scentsy","c":"United States","f":"2003","seg":"Direct-sales wax warmers & home fragrance","d":"Idaho multi-level marketing company known for wickless candles and wax warmers.","lines":["Wax warmers","Wax"],"eras":[],"sig":[],"sc":[],"rel":[],"s":"https://en.wikipedia.org/wiki/Scentsy"},
 {"n":"Air Wick","c":"United States","f":"1943","seg":"Mass-market air care","d":"Air freshener brand created by Guy Paschal in 1943; owned by Advent International since 2025.","lines":["Scented Oils","Freshmatic","Essential Mist Diffuser","Aerosol Spray"],"eras":[],"sig":[],"sc":[],"rel":["Febreze"],"s":"https://en.wikipedia.org/wiki/Air_Wick"},
 {"n":"Febreze","c":"United States","f":"1996","seg":"Mass-market air care","d":"Procter & Gamble odour-elimination and air freshener brand, test-marketed 1996 and sold in the US since 1998.","lines":["Air Effects","NOTICEables","Candles","Wax melts"],"eras":[],"sig":[],"sc":[],"rel":["Air Wick"],"s":"https://en.wikipedia.org/wiki/Febreze"}]
notes=("All 8 old kinds kept; new kind Catalytic fragrance lamp (Lampe Berger, 1898). Electric diffuser types ultrasonic/nebulising/plug-in/automatic spray as t. "
 "Left out: Byredo reed diffuser (no retrieved page confirmed one; Byredo kept via Bibliothèque room spray); named Lampe Berger lamp models such as Alpha/Gravity (seen only in search snippets); "
 "Glade product lines (Wikipedia page did not confirm PlugIns etc.); Vitruvi/Pura and other smart diffusers (not researched); Papier d'Arménie belongs with Incense. No craft traditions apply to this shelf. Wikidata helper returned HTTP 429.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p="work/B4/shelves/02_01.json"; json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
