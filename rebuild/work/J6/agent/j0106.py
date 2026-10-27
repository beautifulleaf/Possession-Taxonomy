import json
W='https://en.wikipedia.org/wiki/'
def A(n,a,d,mk,y,s,v=None,dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
def V(n,mk="",y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
E=W+'Earl_Grey_tea'; T=W+'Tea_blending_and_additives'; rs="https://www.rishi-tea.com/collections/loose-leaf-teas?page=1"
eg=[
 A("Earl Grey","classic bergamot Earl Grey","Black tea flavoured with bergamot oil or peel; the Earl Grey name is not a trademark and its origin story is disputed.","","1824 (earliest bergamot tea reference); 1880s 'Earl Grey' ads",E,[V("Twinings Earl Grey","Twinings","","Brand claims a mandarin-gift origin story"),V("Jacksons of Piccadilly","Jacksons of Piccadilly","1830","Claims Lord Grey gave the recipe to George Charlton"),V("Earl Grey Supreme","Rishi Tea & Botanicals","","From old data")],"base: Chinese black tea · bergamot from Calabria (about 90% of world oil)"),
 A("Lady Grey","","Twinings trademark: bergamot black tea with lemon and orange peel, sometimes cornflower, made for Northern European markets.","Twinings","early 1990s",W+'Lady_Grey_(tea)',[V("Norway launch","Twinings","1994","First sold"),V("Britain launch","Twinings","1996","")],"adds lemon and orange peel"),
 A("Russian Earl Grey","","Earl Grey variant adding citrus peels and lemon grass.","","",E,[],"citrus peel, lemon grass"),
 A("Earl Grey Crème","cream Earl Grey","Earl Grey variant with lavender and vanilla.","","",E,[],"lavender, vanilla"),
]
jas=[
 A("Fuzhou jasmine tea","Mo Li Hua Cha","Green tea layered with fresh jasmine for 20-24 hours; Fuzhou is regarded as the origin of the process and a FAO GIAHS since 2014.","","Tang dynasty; GIAHS April 2014",W+'Jasmine_tea',[V("Jasmine dragon pearls","","","Hand-rolled balls that unfurl slowly"),V("Scenting rounds","","","Top grades scented six or seven times")],"scented 3-7 times · 110,000 t in 2011"),
 A("Osmanthus tea","","Osmanthus flowers with black or green tea, mild and peachy; China's second most popular scented tea.","","",T,[],"flower: osmanthus"),
 A("Rose congou","rose black tea","Rose-scented black tea.","","",T,[],"flower: rose"),
]
fl=[
 A("Mariage Frères Marco Polo","Marco Polo","Iconic flavoured blend of Mariage Frères, the Paris tea house founded in 1854.","Mariage Frères","",W+'Mariage_Fr%C3%A8res',[],"maker iconic blend"),
 A("Russian Caravan smoked blend","Russian Caravan","Lapsang souchong-based blends tied to the Russia-China tea trade.","","",T,[],"smoked"),
 A("Moroccan mint tea","Maghrebi mint tea","Green tea mixed with mint.","","",T,[],"green tea + mint"),
 A("Fruit and floral blends","","Tea blended with mango, peach, berries or flowers.","","",T,[],"fruit, floral"),
]
mc=[
 A("Masala chai","spiced tea · chai","Black tea, often Assam, boiled with milk and spices such as cardamom, ginger and cinnamon.","","1830s tea in India",W+'Masala_chai',[V("Kashmiri chai","","","Green tea base, pinch of salt and baking soda, turns pink"),V("Chai Karak","","","Gulf style popularised by South Asian expatriates"),V("Starbucks chai tea latte","Starbucks","1998","Popularised chai in US coffee shops")],"spices: cardamom, ginger, cinnamon, cloves, star anise, pepper"),
]
bl=[A("Flowering tea","blooming tea · tea bulbs","Bundle of dried tea leaves wrapped around dried flowers, developed in China in the 1980s and usually from Yunnan.","","1980s",W+'Flowering_tea',[],"flowers: globe amaranth, chrysanthemum, jasmine, lily, hibiscus, osmanthus · 2-3 steeps")]
kinds=[
 {"n":"Earl Grey & bergamot tea","a":"Earl Grey","d":"Black tea flavoured with bergamot, with variants such as Lady Grey and Russian Earl Grey.","s":E,"x":eg},
 {"n":"Jasmine & scented tea","a":"jasmine pearls · jasmine green tea","d":"Tea scented with jasmine blossoms, loose, as pearls or pressed, and other flower-scented tea.","s":"https://redblossomtea.com/collections/jasmine-tea","x":jas,"m":[["Jasmine tea",""]]},
 {"n":"Flavoured tea","a":"blended tea · flavoured black tea","d":"Tea of any base type scented or blended with fruit, flowers, smoke or mint.","t":["fruit","vanilla/caramel","smoked","mint","floral"],"s":rs,"x":fl},
 {"n":"Masala chai blends","a":"chai · spiced tea blend","d":"Tea blended with spices to brew as chai.","s":rs,"x":mc,"m":[["Masala Chai",""]]},
 {"n":"Blooming tea","a":"flowering tea · tea bulbs","d":"Tea leaves tied around flowers that unfurl when steeped.","s":"https://redblossomtea.com/collections/blossoming","x":bl},
]
B=lambda n,c,f,seg,kf,d,s,**k: dict({"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s},**k)
brands=[
 B("Mariage Frères","France","1854","Premium","Paris tea house","Gourmet tea house founded by Henri and Edouard Mariage; retail since 1983.",W+'Mariage_Fr%C3%A8res'),
 B("Kusmi Tea","France","1867","Premium","Russian-style blends","Founded by Pavel Kousmichoff in St Petersburg, moved to France in 1917; Groupe Orientis since 2003.",W+'Kusmi_Tea'),
 B("Jacksons of Piccadilly","United Kingdom","","Heritage manufactory","Earl Grey","Claims to have originated Earl Grey.",E),
 B("Twinings","United Kingdom","1706","Mainstream","Lady Grey","London tea house; trademark owner of Lady Grey.",W+'Twinings'),
]
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":"Genmaicha moved to its own kind on shelf 01_02. Left out unsourced: Kusmi Anastasia/Prince Vladimir, Harney Hot Cinnamon Spice, Wagh Bakri, Earl Grey Imperial (not on page), Moli Hua Cha as separate item, Jasmine Silver Needle, lychee black tea. Blooming tea names no makers on the retrieved page."}
json.dump(out,open('01_06.src.json','w'),ensure_ascii=False)
