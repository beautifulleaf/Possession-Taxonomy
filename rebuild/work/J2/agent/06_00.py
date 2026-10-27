import json,os
def A(n,d,s,mk="",y="",dt="",a="",v=None):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"dt":dt}
    if v: x["v"]=v
    return x
KA="https://en.wikipedia.org/wiki/Kamaboko"
K=[
{"n":"Kamaboko","a":"fish cake · narutomaki · hanpen","d":"Steamed, formed cake of fish paste.","t":["red and white","grilled","steamed","sliced"],"s":"https://www.weee.com/en/grocery-near-me/lang-en/explore/kamaboko-fish-cake",
 "x":[A("Narutomaki","Semicylindrical loaf with a pink spiral on each slice, named after the Naruto whirlpools.",KA,dt="ramen topping"),
 A("Sasa-kamaboko","Miyagi's pale white kamaboko shaped like a bamboo leaf and often lightly grilled.",KA,dt="Miyagi Prefecture")]},
{"n":"Chikuwa","a":"tube fish cake","d":"Tube of fish paste cooked on a rod or by roasting.","t":["grilled","with cheese","small"],"s":"https://www.weee.com/en/grocery-near-me/lang-en/explore/kamaboko-fish-cake","m":[["Ichimasa Chikuwa","Ichimasa"],["Takebue Chikuwa","Kibun"]]},
{"n":"Satsuma-age","a":"fried fish cake · tenpura","d":"Formed cake of seasoned fish paste deep-fried without batter or crumb, not filled or sauced.","t":["plain","with burdock","with vegetables"],"s":"https://www.weee.com/en/grocery-near-me/lang-en/explore/satsuma-age"},
{"n":"Crab stick","a":"kanikama · surimi stick · imitation crab","d":"Stick of formed and seasoned fish paste, not coated, filled or sauced.","t":["sticks","flakes","chunks"],"s":"https://www.weee.com/en/grocery-near-me/lang-en/explore/surimi",
 "x":[A("Kanikama","Surimi stick shaped like snow-crab leg meat, patented in 1975 by Osaki Suisan after Sugiyo's flake type of 1974; mostly Alaska pollock.",  "https://en.wikipedia.org/wiki/Crab_stick",dt="red-coloured outside",a="Sea Legs · Krab sticks")],
 "m":[["Hobo Kani","Kanetetsu"],["Kanizanmai","Kibun"]]},
{"n":"Fish ball","a":"Teochew fish ball · fiskeboller","d":"Round ball of ground fish paste, not coated, filled or sauced.","t":["Teochew (eel base)","Norwegian","fresh","frozen","tinned"],"s":"https://www.weee.com/en/grocery-near-me/lang-en/explore/fish-ball",
 "x":[A("Teochew fish ball","Fish ball with an eel base often mixed with mackerel, bound with sweet potato starch, spread across Southeast Asia by the Teochew.","https://www.chowhound.com/1760192/what-are-fish-balls/",dt="noodle soup"),
 A("Norwegian fiskeboller","Fish balls of cheap white fish stabilised with potato starch for a mild taste.","https://www.chowhound.com/1760192/what-are-fish-balls/",dt="Norway")]},
{"n":"Fish sausage","a":"osakana sausage","d":"Sausage-shaped formed fish paste in a casing.","t":["salt-reduced","MSC","children's snack"],"s":"https://my-best.com/4756","m":[["Osakana Sausage (Bessho Kamaboko)","Bessho Kamaboko"],["Osakana no Sausage","Nissui"],["Sokkin Tanpaku Sausage Salt-reduced MSC","Nissui"],["Osakana de Tsukutta Sausage","Toyo Suisan"],["Risara Fish Sausage","Umios"]]}
]
B=[{"n":"Nissui","c":"Japan","f":"1911","seg":"Mainstream","kf":"frozen seafood and surimi","d":"Japanese seafood company founded at Shimonoseki as the fishery division of Tamura Steamship; owns Gorton's of Gloucester.","lines":[],"eras":[],"sig":[],"sc":[],"rel":["Gorton's"],"s":"https://en.wikipedia.org/wiki/Nissui"}]
out={"kinds":K,"brands":B,"traditions":[],"notes":"Tier shelf, all 6 planned kinds kept. Narutomaki and Sasa-kamaboko moved from flat models to archetypes. Fish sausage trimmed from 8 models and one range to 5 models (Nissui Hokkaido Sausage, Sokkin Tanpaku Wiener and Umios 1-second OPEN dropped as SKU duplicates; range Sokkin Tanpaku dropped). Not added for lack of a retrieved page: Odawara kamaboko (the retrieved pages do not describe it), Toyohashi chikuwa, Kagoshima satsuma-age, hanpen as separate entry (listed in the kamaboko page only as a related product)."}
p='work/J2/shelves/06_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1);os.replace(p+'.tmp',p)
