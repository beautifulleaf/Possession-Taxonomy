import json,os
def A(n,d,s,mk="",y="",dt="",a="",v=None):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"dt":dt}
    if v: x["v"]=v
    return x
W="https://en.wikipedia.org/wiki/"
K=[
{"n":"Smoked salmon","a":"cold-smoked salmon · Räucherlachs · saumon fumé","d":"Salmon cured and smoked at low temperature, sold sliced or in pieces, ready to eat without cooking.",
 "t":["sliced","whole side","D-cut","hand-carved","wild","farmed","organic"],
 "s":"https://www.thefishsociety.co.uk/collections/smoked-cured",
 "x":[
 A("London Cure Smoked Salmon PGI","Salmon cured and smoked by H. Forman & Son in east London; first smoked salmon to get PGI, announced July 2017 after a four-year application.","https://www.jewishnews.co.uk/uk-smoked-salmon-business-protected-status/",mk="H. Forman & Son",y="2017",dt="kosher certified · family firm since 1905"),
 A("Loch Fyne Bradan Orach","Hand-salted Scottish salmon smoked up to 24 hours longer than the industry standard over oak from aged whisky casks.","https://thefishsite.com/articles/more-than-just-oysters",mk="Loch Fyne Oysters",dt="Gaelic for golden salmon · drier, meatier texture"),
 A("Severn & Wye smoked salmon","Hand-graded and cut salmon smoked over its own chipped oak near the Forest of Dean, with a Royal Warrant.","https://www.abelandcole.co.uk/producer/279/severn-wye-smokery",mk="Severn & Wye Smokery",dt="organic and land-based farmed salmon · also trout, mackerel, gravadlax"),
 A("Belvelly hung-smoked salmon","Salmon hung for smoking at the Belvelly Smoke House, Co. Cork.","https://www.castlemartyrresort.ie/activities/hedermans-smokehouse/",mk="Frank Hederman",dt="hung smoking"),
 A("Petrossian smoked salmon","Smoked salmon from the Paris caviar house, which opened a smokehouse in the 1930s.","https://en.wikipedia.org/wiki/Petrossian_(business)",mk="Petrossian",y="1930s"),
 A("Nova lox","Salmon cured in a mild brine then cold-smoked and thinly sliced; Nova names the style, not the fish's origin.","https://en.wikipedia.org/wiki/Lox",dt="New York bagel style",a="Nova Scotia salmon"),
 A("Belly lox","Paper-thin fatty salmon belly, traditionally dry-cured in salt and unsmoked; mass-produced versions add cold smoke.","https://en.wikipedia.org/wiki/Lox",dt="very salty",a="lox")
 ],
 "m":[["Bio-verde Nord Atlantik Lachs Bio","Bio-verde"],["Aldi Almare Seafood Norwegischer Räucherlachs","Aldi"]]},
{"n":"Hot-smoked salmon","a":"kiln-roasted salmon · flaked smoked salmon","d":"Salmon smoked at a temperature that cooks it, sold as fillets, portions or flakes.","t":["fillet","portion","flaked","wild","farmed"],"s":"https://www.thefishsociety.co.uk/collections/smoked-cured"},
{"n":"Gravlax","a":"gravad lax · gravlaks · cured salmon","d":"Salmon cured in salt and sugar, often with dill, not smoked, sold chilled and sliced.","t":["dill","beetroot","mustard-dill sauce","sliced","whole side"],"s":"https://www.thefishsociety.co.uk/products/sliced-salmon-beetroot-gravadlax",
 "x":[A("Scandinavian gravad lax","Nordic salmon cured in salt, sugar and dill for 12 hours to a few days; earliest cited reference 1348.","https://en.wikipedia.org/wiki/Gravlax",dt="served thinly sliced with mustard-dill sauce (hovmästarsås)")]}
]
B=[
{"n":"H. Forman & Son","c":"United Kingdom","f":"1905","seg":"Heritage manufactory","kf":"London Cure","d":"London family smokehouse, holder of the London Cure PGI.","lines":["London Cure"],"eras":[],"sig":["London Cure Smoked Salmon PGI"],"sc":[],"rel":[],"s":"https://www.jewishnews.co.uk/uk-smoked-salmon-business-protected-status/"},
{"n":"Loch Fyne Oysters","c":"United Kingdom","f":"1978","seg":"Premium","kf":"Scottish oysters and smoked salmon","d":"Argyll oyster farm with restaurant, deli and smokehouse.","lines":["Bradan Orach"],"eras":[],"sig":["Loch Fyne Bradan Orach"],"sc":[],"rel":[],"s":"https://thefishsite.com/articles/more-than-just-oysters"},
{"n":"Severn & Wye Smokery","c":"United Kingdom","f":"","seg":"Premium","kf":"oak-smoked salmon","d":"Gloucestershire smokery near the Forest of Dean with a Royal Warrant.","lines":[],"eras":[],"sig":["Severn & Wye smoked salmon"],"sc":[],"rel":[],"s":"https://www.abelandcole.co.uk/producer/279/severn-wye-smokery"},
{"n":"Frank Hederman","c":"Ireland","f":"","seg":"Artisan & independent","kf":"hung-smoked fish","d":"Belvelly Smoke House, Co. Cork, run by Frank and Caroline Hederman.","lines":[],"eras":[],"sig":["Belvelly hung-smoked salmon"],"sc":[],"rel":[],"s":"https://www.castlemartyrresort.ie/activities/hedermans-smokehouse/"},
{"n":"Petrossian","c":"France","f":"1920","seg":"Premium","kf":"caviar and smoked salmon","d":"Paris house founded by the Armenian Petrossian brothers; smoked fish added in the 1930s.","lines":[],"eras":[],"sig":["Petrossian smoked salmon"],"sc":[],"rel":[],"s":"https://en.wikipedia.org/wiki/Petrossian_(business)"}]
out={"kinds":K,"brands":B,"traditions":[],"notes":"Discounter SKU list cut to the two Stiftung Warentest 2024 products named in sources: Bio-verde (organic Testsieger per search reports; test.de page itself only says an organic salmon won) and Aldi Almare (price tip). Dropped Friedrichs, Krone, Mein Lieblings (not winners). Not added for lack of a retrieved page: Hebridean Smokehouse, Ummera, Burren, Balik, Kinsale, Ducktrap. Hot-smoked salmon has no archetypes. Brand founding years left blank where not on a retrieved page."}
p='work/J2/shelves/02_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1);os.replace(p+'.tmp',p)
