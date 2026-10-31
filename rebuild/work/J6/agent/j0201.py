import json
W='https://en.wikipedia.org/wiki/'
kinds=[
 {"n":"Fruit tea","a":"dried-fruit blend","d":"Blend of dried fruit pieces sold for infusion.","t":["tea bag","loose","hibiscus-rose hip blend"],"s":"https://www.teegschwendner.de/Tee/Fruechtetee","m":[["Das gute Fruechtepfund","Tee Gschwendner"],["Hibiscus Delight blend","Lone Star Botanicals"]]},
 {"n":"Herbal blend","a":"herbal tea · tisane","d":"Blend of infusion plants from more than one plant part, none of which makes up half or more of its weight.","t":["relaxing","digestive","tea bag","loose"],"s":"https://www.rishi-tea.com/collections/loose-leaf-teas?page=1","m":[["Chamomile Medley","Rishi Tea & Botanicals"],["Turmeric Ginger","Rishi Tea & Botanicals"],["Ginseng Mint","Summit Tea Co"],["Sleepytime","Celestial Seasonings"],["Yogi Tea","East West Tea Company"]]},
 {"n":"Rose hip","a":"","d":"Dried rose hips sold for infusion.","t":["cut and sifted","blended with hibiscus"],"s":"https://mountainroseherbs.com/rosehips"},
 {"n":"Ginger, turmeric & spice infusions","a":"ginger tea · turmeric tea · salabat","d":"Dried ginger, turmeric and other spice roots sold for infusion; in a jar as a cooking spice they are in Pantry Staples.","t":["ginger","turmeric","cinnamon","liquorice root","instant powder"],"s":"https://onsullivan.com/products/ginger-root"},
]
B=lambda n,c,f,seg,kf,d,s,**k: dict({"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s},**k)
brands=[
 B("Celestial Seasonings","United States","1969","Mainstream","herbal tea","Boulder, Colorado herbal tea company founded by Mo Siegel and Wyck Hay; Sleepytime dates to 1972; part of Hain Celestial.",W+'Celestial_Seasonings'),
 B("Yogi Tea","United States","","Mainstream","Ayurvedic blends","Organic herbal, green and black blends; owned by East West Tea Company; infobox founding 1984, history section 1973.",W+'Yogi_Tea'),
 B("Pukka","United Kingdom","","Mainstream","organic herbal tea","Organic herbal tea brand.","knowledge"),
 B("Teekanne","Germany","","Mainstream","tea bags and fruit tea","German tea company.","knowledge"),
 B("Meßmer","Germany","","Mainstream","tea bags","German tea brand.","knowledge"),
 B("Traditional Medicinals","United States","","Specialist","medicinal herbal tea","US herbal tea company.","knowledge"),
 B("Tee Gschwendner","Germany","","Specialist","tea shops","German tea retailer.","knowledge"),
]
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":"Tier shelf: no Stiftung Warentest/Oeko-Test/Which? pages retrieved so no test-winner list; models limited to old data plus Sleepytime and Yogi Tea (named on retrieved pages). Ginger and turmeric merged into one kind as planned. Left out unsourced: Twinings/Clipper/Halssen & Lyon herbal ranges."}
json.dump(out,open('02_01.src.json','w'),ensure_ascii=False)
