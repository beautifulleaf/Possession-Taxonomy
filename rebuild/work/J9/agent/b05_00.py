import json, os
W='https://en.wikipedia.org/wiki/'
K=[]
def k(n,a,d,s,t=None,m=None,x=None):
    o={"n":n,"a":a,"d":d}
    if t: o["t"]=t
    o["s"]=s
    if x: o["x"]=x
    if m: o["m"]=m
    K.append(o)
k("Kombucha","kombucha · tea fungus drink · booch","Sweetened black tea fermented with a SCOBY culture into a tart, lightly fizzy drink with a trace of alcohol.",W+"Kombucha",
  t=["original","flavoured (fruit, ginger, spice)","zero sugar","hard kombucha (over 5% ABV)"],
  x=[{"n":"GT's Kombucha","a":"GT's Living Foods","d":"Los Angeles-brewed kombucha that built the US bottled market and holds about 40% of it.","mk":"GT's Living Foods","y":"1995","s":W+"GT%27s_Living_Foods",
      "v":[{"n":"First sale to Erewhon Natural Foods","mk":"GT's Living Foods","y":"1995","d":"George Thomas Dave's first commercial kombucha"},{"n":"Whole Foods distribution","mk":"GT's Living Foods","y":"1997","d":"Gardena brewery opened"}],
      "dt":"flavour · glass bottle"},
     {"n":"Remedy Kombucha","a":"Remedy","d":"Sugar-free organic kombucha brewed in Melbourne and exported to some 20 countries.","mk":"Remedy Drinks","y":"2012","s":"https://austrade.gov.au/en/news-and-analysis/news/remedy-drinks-brews-export-success",
      "v":[{"n":"Kombucha","mk":"Remedy Drinks","y":"2012","d":"Founding product, kitchen-bench brewed by Sarah and Emmet Condon"},{"n":"Remedy Sodaly","mk":"Remedy Drinks","y":"","d":"Prebiotic soft drink spin-off"}],
      "dt":"flavour · can or bottle"}],
  m=[["KeVita","PepsiCo"]])
k("Jun","jun · xun · jun-kombucha","Kombucha-like drink fermented from green tea and honey instead of black tea and cane sugar.","https://en.wikipedia.org/wiki/Jun_(drink)",
  t=["plain","fruit or spice flavoured"])
k("Water kefir","water kefir · tibicos · tibi · sugar kefir · ginger beer plant (historic)","Sugar water or juice fermented with kefir grains into a lightly sparkling probiotic drink.",W+"Water_kefir",
  t=["plain","fruit-flavoured","home grains (culture)"])
k("Kvass","kvass · kvas · kwas chlebowy · gira · kali","Cloudy sweet-sour drink fermented from rye bread or malt, usually under 1.5% alcohol.",W+"Kvass",
  t=["bread kvass","white kvass","beetroot kvass","fruit kvass (apple, pear)","kvass-flavoured malt drink (unfermented)"],
  x=[{"n":"Nikola kvass","a":"Никола","d":"Russia's best-selling kvass brand, with about 39% of the market in 2014.","mk":"Deka","y":"","s":W+"Kvass","v":[],"dt":"bottle size"},
     {"n":"Kwas chlebowy sapieżyński","a":"Kodeń kvass","d":"Historic Polish bread kvass from Kodeń whose recipe dates to the 1500s.","mk":"","y":"1500s","s":W+"Kvass","v":[],"dt":"bottle"}],
  m=[["Ochakovsky","Ochakovo"],["Russky dar","PepsiCo"],["Khlebny kray","Carlsberg Group"],["Kruzhka i bochka","Coca-Cola"],["Iļģuciema kvass","Iļģuciema"],["Churin kvass","Harbin Churin Food"]])
k("Boza","boza · bosa · bozo · millet boza","Thick, slightly sour, sweet drink of fermented grain such as millet, wheat or maize, about 1% alcohol.",W+"Boza",
  t=["Turkish (thick, tart)","Albanian (white, sweet)","Bulgarian / Balkan","millet (Białystok style)"],
  x=[{"n":"Vefa boza","a":"Vefa Bozacısı","d":"Thick, tart Istanbul boza from the shop founded in 1876, the reference Turkish style.","mk":"Vefa","y":"1876","s":W+"Boza","v":[],"dt":"served with cinnamon and roasted chickpeas · bottled"}])
k("Tepache","tepache · tepache de piña","Lightly fermented Mexican drink of pineapple peel and piloncillo, often spiced.",W+"Tepache",
  t=["traditional","spiced (chilli, cinnamon)","tepache de tibicos"],
  m=[["Tepachito","Frumex"]])
k("Mauby","mauby · mavi · mabi · maví","Bittersweet Caribbean drink of Colubrina bark and spices, fermented traditionally or sold as syrup or soda.",W+"Mauby",
  t=["fermented (mavi champán)","syrup / concentrate","carbonated"],
  m=[["Seybano","Grupo Taino"],["Cacheo","Grupo Taino"],["Mauby Fizzz","PepsiCo"],["Hairoun Mauby","St. Vincent Brewery"]])
k("Malta & malt soft drink","malta · maltin · malt drink","Lightly carbonated non-alcoholic drink brewed from barley, hops and water, popular in the Caribbean and West Africa.","https://en.wikipedia.org/wiki/Malta_(soft_drink)",
  t=["regular","light / low sugar","vitamin-enriched"],
  x=[{"n":"Malta India","a":"","d":"Puerto Rican malta brewed in Mayagüez, popular across the Caribbean.","mk":"Compañía Cervecera de Puerto Rico","y":"","s":"https://en.wikipedia.org/wiki/Malta_(soft_drink)","v":[],"dt":"bottle or can"},
     {"n":"Supermalt","a":"","d":"Caffeine-free malt drink first developed for the Nigerian Army, now made in Denmark.","mk":"Royal Unibrew","y":"1972","s":W+"Supermalt","v":[],"dt":"bottle or can"}],
  m=[["Maltín Polar","Maltín Polar"],["Malta Goya","Goya Foods"],["Pony Malta","Bavaria"],["Vitamalt","Vitamalt"]])
k("Brewed ginger beer","brewed ginger beer · traditional ginger beer · stone ginger beer","Ginger, sugar and water fermented with yeast or a ginger beer plant, then kept below 0.5% alcohol.",W+"Ginger_beer",
  t=["traditional brewed","spiced","diet","ginger beer plant (home culture)"],
  x=[{"n":"Fentimans Traditional Ginger Beer","a":"","d":"Botanically brewed English ginger beer fermented from milled ginger root in wooden vats.","mk":"Fentimans","y":"1905","s":W+"Fentimans",
      "v":[{"n":"Original recipe","mk":"Fentimans","y":"1905","d":"Recipe acquired by Thomas Fentiman, Cleckheaton"},{"n":"Re-established brand","mk":"Fentimans","y":"1988","d":"Revived by his great-grandson, brewed in Hexham"}],"dt":"275 ml or 750 ml bottle"},
     {"n":"Bundaberg Ginger Beer","a":"Bundy ginger beer","d":"Non-alcoholic brewed ginger beer from Bundaberg, Queensland, the brand's flagship.","mk":"Bundaberg Brewed Drinks","y":"1960","s":W+"Bundaberg_Brewed_Drinks",
      "v":[{"n":"Ginger Beer","mk":"Bundaberg Brewed Drinks","y":"","d":"Flagship"},{"n":"Diet Ginger Beer","mk":"Bundaberg Brewed Drinks","y":"","d":"Diet range"},{"n":"Spiced Ginger Beer","mk":"Bundaberg Brewed Drinks","y":"2014","d":"Seasonal"}],"dt":"bottle size · regular, diet or spiced"}],
  m=[["Remedy Ginger Beer","Remedy Drinks"]])
k("Rice & grain drink","amazake · sikhye · dansul · gamju · horchata","Sweet drinks of rice or grain broken down by koji or malt, such as Japanese amazake and Korean sikhye, sold bottled or canned.",W+"Sikhye",
  t=["amazake (rice koji)","amazake (sake lees)","sikhye","pumpkin sikhye","horchata (tiger nut or rice, unfermented)"],
  m=[["Vilac sikhye","Vilac"],["Korea Yakult sikhye","Korea Yakult"]])
B=[
 {"n":"GT's Living Foods","c":"United States","f":"1995","seg":"Kombucha","d":"Los Angeles kombucha maker founded by George Thomas Dave, holding about 40% of the US market.","sig":["GT's Kombucha"],"s":W+"GT%27s_Living_Foods"},
 {"n":"Remedy Drinks","c":"Australia","f":"2012","seg":"Kombucha & prebiotic soda","d":"Melbourne maker of sugar-free kombucha founded by Sarah and Emmet Condon.","lines":["Kombucha","Sodaly","Ginger Beer"],"sig":["Remedy Kombucha"],"s":"https://austrade.gov.au/en/news-and-analysis/news/remedy-drinks-brews-export-success"},
 {"n":"Vefa","c":"Turkey","f":"1876","seg":"Boza shop","d":"Istanbul boza shop founded by Hacı İbrahim and Hacı Sadık, still run by the family.","sig":["Vefa boza"],"s":W+"Boza"},
 {"n":"Deka","c":"Russia","seg":"Kvass","d":"Russian maker of Nikola, the market-leading kvass brand.","sig":["Nikola kvass"],"s":W+"Kvass"},
 {"n":"Royal Unibrew","c":"Denmark","seg":"Beer & soft drinks","d":"Danish brewer that makes Supermalt.","sig":["Supermalt"],"s":W+"Supermalt"},
 {"n":"Compañía Cervecera de Puerto Rico","c":"Puerto Rico","seg":"Beer & malta","d":"Mayagüez brewer of Malta India.","sig":["Malta India"],"s":"https://en.wikipedia.org/wiki/Malta_(soft_drink)"},
 {"n":"Fentimans","c":"United Kingdom","f":"1905","seg":"Botanically brewed soft drinks","d":"Hexham maker of brewed ginger beer, lemonades and mixers, revived in 1988.","lines":["Curiosity Cola","Victorian Lemonade","Rose Lemonade"],"sig":["Fentimans Traditional Ginger Beer"],"s":W+"Fentimans"},
 {"n":"Bundaberg Brewed Drinks","c":"Australia","f":"1960","seg":"Brewed soft drinks","d":"Queensland maker of non-alcoholic brewed ginger beer and other brewed sodas.","sig":["Bundaberg Ginger Beer"],"s":W+"Bundaberg_Brewed_Drinks"},
]
T=[
 {"n":"Kvass","g":"Food & drink","r":"Russia, Ukraine, Belarus, Poland, Baltics","p":"first recorded 988; commercial from the late 19th century","d":"Low-alcohol rye bread or malt drink brewed at home and sold from street barrels and bottles.","tech":"rye bread or malt soaked in hot water, short fermentation with yeast and lactic bacteria","mat":"rye bread, rye malt, sugar, yeast, berries or herbs","forms":["bread kvass","beetroot kvass","white kvass"],"ctr":["Kodeń (Poland)","Riga (Latvia)","Harbin (China)"],"auth":"fermented from bread or malt, under about 1.2–1.5% alcohol; unfermented malt-extract drinks are kvass-style beverages","s":W+"Kvass"},
 {"n":"Boza","g":"Food & drink","r":"Turkey, Balkans, Volga, Caucasus","p":"recorded in the 11th century; golden age under the Ottomans","d":"Thick fermented grain drink sold by boza makers and street vendors in winter.","tech":"ground cereal fermented and kept cool","mat":"millet, wheat, bulgur, maize, sugar","forms":["Turkish boza","Albanian boza","Białystok millet boza"],"ctr":["Vefa, Istanbul (1876)","Białystok"],"auth":"thick, tart, about 1% alcohol; served cold in winter","s":W+"Boza"},
 {"n":"Tepache","g":"Food & drink","r":"Mexico","p":"pre-Columbian (Nahua); pineapple-based later","d":"Quick street-vendor ferment of pineapple peel, once made from maize.","tech":"wild fermentation of peel with sugar for one to two days, sometimes in barrels","mat":"pineapple peel and rind, piloncillo, cinnamon, chilli","forms":["tepache","tepache de tibicos"],"ctr":["central Mexico street vendors"],"auth":"slight fizz and tartness from live fermentation; sold chilled","s":W+"Tepache"},
 {"n":"Mauby","g":"Food & drink","r":"Caribbean","p":"traditional; now mostly a soft drink","d":"Bittersweet bark drink, once fermented in small batches, now often syrup or soda.","tech":"bark and spices boiled, bottled and sun-warmed, fermented up to a week with a previous batch","mat":"Colubrina bark, cinnamon, cloves, aniseed, orange peel, brown sugar","forms":["fermented mavi champán","mauby syrup","carbonated mauby"],"ctr":["Puerto Rico","Dominican Republic","Haiti","Trinidad and Tobago"],"auth":"bitter bark taste; fermented versions foam","s":W+"Mauby"},
]
notes=("All 10 planned kinds kept (no old data). Left out: Equinox kombucha (no page retrieved), KeVita founding facts (wiki 404; kept as m from kombucha page), Loving Foods jun (retail snippets only), "
"Maltina and Vitamalt details (not on retrieved pages; Vitamalt kept as m), chicha morada and switchel (no evidence of bottled sale retrieved), horchata brands (none on page; horchata kept as an unfermented type). Tepachito details are uncited on Wikipedia.")
import sys; sys.path.insert(0,"/home/user/Possession-Taxonomy/rebuild/work/J9/agent"); from segfix import fix; fix(B)
out={"kinds":K,"brands":B,"traditions":T,"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/J9/shelves/05_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
