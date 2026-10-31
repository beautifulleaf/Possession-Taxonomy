import json, os
boot = {"n":"Hiking boot","a":"walking boot · trekking boot · backpacking boot",
 "d":"Lace-up boot covering the ankle, made for walking on rough ground: padded collar, lugged sole; not made for labour.",
 "t":["mid cut","high cut","lightweight hiking boot","backpacking boot","mountaineering boot (crampon-compatible)","leather","synthetic / fabric","waterproof membrane"],
 "s":"https://www.mec.ca/en/products/camping-and-hiking/hiking-gear/hiking-footwear/hiking-boots/mens",
 "x":[
  {"n":"Danner Light / Mountain Light","a":"Danner Light · Mountain Light","d":"Leather-and-nylon or all-leather hiking boot with Gore-Tex liner and Vibram Kletterlift sole, built in Portland, Oregon.",
   "mk":"Danner","y":"1979","s":"https://global.danner.com/productfamily/danner-light",
   "v":[{"n":"6490","mk":"Danner","y":"1970s","d":"early lightweight boot for day hikers and backpackers (Wikipedia, Hiking boot)"},
        {"n":"Danner Light","mk":"Danner","y":"1979","d":"original; stitchdown, Gore-Tex liner, Vibram Kletterlift; Khaki version in full-grain leather and nylon"},
        {"n":"Mountain Light","mk":"Danner","y":"1979","d":"one-piece full-grain leather upper, Gore-Tex liner; re-released to original specification, made in the USA (Silodrome)"}],
   "dt":"stitchdown construction · full-grain leather or leather/nylon · Gore-Tex liner · Vibram Kletterlift sole"},
  {"n":"Lowa Renegade","a":"Renegade GTX","d":"Nubuck leather mid-cut boot with Gore-Tex membrane, Mono Wrap frame and Vibram Evo sole; Lowa's best-selling outdoor boot.",
   "mk":"Lowa","y":"1997","s":"https://explore-mag.com/explores-outdoor-gear-pick-of-the-week-lowa-renegade-gtx-mid-hiking-boots/",
   "v":[{"n":"Renegade GTX Mid","mk":"Lowa","y":"","d":"reference version; men's and women's; leather-lined, wide and low-cut versions also made"},
        {"n":"Renegade Evo","mk":"Lowa","y":"","d":"later version (old data)"}],
   "dt":"cut low, mid · nubuck leather · Gore-Tex or leather lining · standard and wide fits"},
  {"n":"Salomon Quest 4D","a":"Quest","d":"Backpacking boot built on the XA Pro 3D running-shoe design, with Gore-Tex lining and shaped 4D chassis.",
   "mk":"Salomon","y":"2009","s":"https://www.militarytimes.com/off-duty/gearscout/2009/01/11/salomon-s-quest-hiking-boots-coming-in-cool-or-fugly",
   "v":[{"n":"Quest 4D GTX","mk":"Salomon","y":"2009","d":"original; announced January 2009"},
        {"n":"Quest 4D 2 GTX","mk":"Salomon","y":"","d":"second iteration"},
        {"n":"Quest 4D 3 GTX","mk":"Salomon","y":"","d":"third iteration; same shape and weight as 4D 2, new outsole lug pattern (Outdoors Magic)"}],
   "dt":"mid-weight backpacking · Gore-Tex · colourways"},
  {"n":"Scarpa Kailash","a":"Kailash GTX","d":"Mid-to-heavyweight leather backpacking boot made in Italy, with suede upper, Gore-Tex liner and Vibram sole.",
   "mk":"Scarpa","y":"","s":"https://www.packstack.io/reviews/footwear/scarpa-kailash-gtx",
   "v":[{"n":"Kailash GTX","mk":"Scarpa","y":"","d":"discontinued original"},
        {"n":"Kailash Trek GTX","mk":"Scarpa","y":"","d":"successor (also in old data)"},
        {"n":"Kailash Plus GTX","mk":"Scarpa","y":"","d":"successor"}],
   "dt":"suede leather upper · Gore-Tex · Vibram sole"}],
 "m":[["Vioz","Zamberlan"],["X Ultra","Salomon"],["Kopec","Arc'teryx"],["Pyrenees","Keen"],["Sawtooth","Oboz"],["Hedgehog","The North Face"]]}
shoe = {"n":"Hiking shoe","a":"low hiking shoe · light hiker · approach-style hiker",
 "d":"Low-cut lace-up shoe made for walking on rough ground, with a flexible lugged sole.",
 "t":["waterproof membrane","vented / mesh","leather","synthetic","wide fit"],
 "s":"https://scandinavianoutdoor.com/shoes/mens-shoes/low-models",
 "x":[
  {"n":"Merrell Moab","a":"Moab","d":"Suede-and-mesh hiking shoe with Vibram sole and heel air cushion; Merrell calls it the bestselling hiker in the world.",
   "mk":"Merrell","y":"","s":"https://www.merrell.com/US/en_US/moab-3/52481M.html",
   "v":[{"n":"Moab 3","mk":"Merrell","y":"","d":"current generation; Vibram TC5+ outsole, 11.5 mm drop, 5 mm lugs, recycled materials; wide width"},
        {"n":"Moab Speed","mk":"Merrell","y":"","d":"lighter offshoot (old data); Moab Speed 2 Gore-Tex follows"}],
   "dt":"pig suede and mesh · waterproof or ventilated · regular and wide widths"},
  {"n":"Salomon X Ultra","a":"X Ultra","d":"Light hiking shoe with trail-runner grip, Advanced Chassis stability and Contagrip sole, designed around the Tour du Mont Blanc.",
   "mk":"Salomon","y":"2012","s":"https://fashiontechnews.zozo.com/en/articles/salomon_xultra360",
   "v":[{"n":"X Ultra","mk":"Salomon","y":"2012","d":"original; updated 2015 and 2018"},
        {"n":"X Ultra 4","mk":"Salomon","y":"2021","d":"fourth generation"},
        {"n":"X Ultra 360 Gore-Tex","mk":"Salomon","y":"2024","d":"derivative with EVA cushioning and Gore-Tex"}],
   "dt":"Gore-Tex or unlined · Contagrip outsole"},
  {"n":"Keen Targhee","a":"Targhee","d":"Keen's original hiker, a wide-toed waterproof hiking shoe and boot family.",
   "mk":"Keen","y":"2005","s":"https://www.keenfootwear.com/blogs/keen-blog/faq-targhee-ii-or-targhee-iii",
   "v":[{"n":"Targhee II","mk":"Keen","y":"","d":"traditional hiker feel, raised heel, deep lugs; waterproof boot"},
        {"n":"Targhee III","mk":"Keen","y":"","d":"sneaker-like, streamlined; waterproof shoe"},
        {"n":"Targhee IV","mk":"Keen","y":"","d":"KEEN.FUSION construction, Luftcell midsole; more durable outsole"}],
   "dt":"low and mid cuts · waterproof or vent"}],
 "m":[["Renegade Evo","Lowa"],["Innovo","Lowa"],["Kaduro","Hanwag"],["Siena","Meindl"],["Gastein","Meindl"],["L.I.M Horizon","Haglöfs"]]}
water = {"n":"Water shoe","a":"aqua shoe · river shoe","d":"Drainable shoe made for use in and beside water.",
 "t":["sock-style aqua shoe","laced river shoe","closed-toe sandal style"],
 "s":"https://www.outdoorgearlab.com/reviews/shoes-and-boots/water-shoes-men/speedo-surfwalker-pro-3-0",
 "m":[["Brewer 3.0","Astral"],["Surfwalker","Speedo"],["Surf Knit Pro","Speedo"],["3T","Body Glove"]]}
brands = [
 {"n":"Merrell","c":"United States","f":"1981","seg":"Outdoor footwear","d":"Michigan-based hiking footwear maker, owned by Wolverine World Wide since 1997.","sig":["Merrell Moab"],"rel":["Keen","Salomon"],"s":"https://en.wikipedia.org/wiki/Merrell_(company)"},
 {"n":"Salomon","c":"France","f":"1947","seg":"Outdoor and mountain sports","d":"Annecy-area mountain sports company, part of Amer Sports.","sig":["Salomon X Ultra","Salomon Quest 4D"],"rel":["Merrell"],"s":"https://en.wikipedia.org/wiki/Salomon_Group"},
 {"n":"Meindl","c":"Germany","f":"1928","seg":"Mountain and hiking boots","d":"Bavarian boot maker in Kirchanschöring, also known for military boots and clothing.","rel":["Lowa","Hanwag"],"s":"https://en.wikipedia.org/wiki/Meindl_(company)"},
 {"n":"Lowa","c":"Germany","f":"1923","seg":"Mountain and hiking boots","d":"Bavarian hiking and mountain boot maker.","sig":["Lowa Renegade"],"rel":["Meindl","Hanwag"],"s":"knowledge"},
 {"n":"Danner","c":"United States","f":"1932","seg":"Heritage hiking and work boots","d":"Boot maker based in Portland, Oregon, known for stitchdown leather boots.","sig":["Danner Light / Mountain Light"],"s":"knowledge"},
 {"n":"Scarpa","c":"Italy","f":"1938","seg":"Mountain and hiking footwear","d":"Mountain footwear maker from Asolo, Italy.","sig":["Scarpa Kailash"],"s":"knowledge"},
 {"n":"Keen","c":"United States","f":"2003","seg":"Outdoor footwear","d":"Portland-based outdoor footwear brand known for wide toe boxes and closed-toe sandals.","sig":["Keen Targhee"],"rel":["Merrell"],"s":"knowledge"},
 {"n":"Speedo","c":"Australia","f":"1914","seg":"Swimwear","d":"Swimwear brand that also makes aqua shoes.","s":"https://en.wikipedia.org/wiki/Speedo"}]
notes = ("Dropped Paraboot Avoriaz (no source placing it as a hiking boot; brief says drop unless sourced). Zamberlan Vioz kept as a flat model: maker and retailer pages "
 "(REI, Trailspace) blocked, so no archetype. Hanwag and Meindl kept as flat models only (no archetype page retrieved; Meindl Gastein added from Wikipedia). "
 "Merrell Moab launch year and 'originator' claim not confirmed, so y left blank; Moab 2 not confirmed on a fetched page. Salomon X Ultra Mid not confirmed so 'X Ultra' stays in boot models. "
 "Cut and weight classes are types (t). Water shoe is a tier kind with 4 old models; Keen water models not added (unsourced). No traditions apply.")
out = {"kinds":[boot,shoe,water],"brands":brands,"traditions":[],"notes":notes}
p = "work/A2/shelves/01_01.json"; os.makedirs("work/A2/shelves", exist_ok=True)
json.dump(out, open(p+".tmp","w"), ensure_ascii=False, indent=1); os.replace(p+".tmp", p)
