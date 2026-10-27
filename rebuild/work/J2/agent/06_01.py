import json,os
def A(n,d,s,mk="",y="",dt="",a="",v=None):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"dt":dt}
    if v: x["v"]=v
    return x
FC="https://en.wikipedia.org/wiki/Fishcake"
FF="https://en.wikipedia.org/wiki/Fish_finger"
GF="https://en.wikipedia.org/wiki/Gefilte_fish"
K=[
{"n":"Fish fingers","a":"fish sticks · Fischstäbchen · bâtonnets de poisson","d":"Breaded rectangles of whitefish (cod, hake, haddock, pollock), sold frozen.","t":["cod","pollock","haddock","breaded","battered","fillet-based","minced-block"],"s":FF,
 "x":[A("Birds Eye fish fingers","Commercialised in 1953 under the Birds Eye label by General Foods; the UK name came from a poll of workers.",FF,mk="Birds Eye",y="1953",dt="named after a poll of Birds Eye workers",a="fish sticks")],
 "m":[["Birds Eye fish fingers","Birds Eye"],["Findus fish fingers","Findus"],["Iglo fish fingers","Iglo"],["Gorton's fish sticks","Gorton's"],["Frosta Fischstäbchen","Frosta"],["Alnatura Fischstäbchen","Alnatura"]]},
{"n":"Breaded & battered fish","a":"scampi · coated fillets · Backfisch","d":"Frozen coated fish fillets and scampi, breaded or battered.","t":["breaded","battered","fillet","portion","scampi","MSC-certified"],"s":FF,"m":[["Iglo Backfisch sticks","Iglo"]]},
{"n":"Fish cake","a":"fishcake · fish patty","d":"Western potato-and-fish patty, chilled or frozen.","t":["potato-and-fish","salmon","cod","breaded","chilled","frozen"],"s":FC,
 "x":[A("British potato fishcake","UK chippy fishcake of potato slices with fish offcuts, battered and fried; Castleford's parsley cake is fish, mashed potato and parsley.",FC,dt="Lancashire and Yorkshire chip shops"),
 A("Pastéis de bacalhau","Portuguese salt cod, potato, parsley and egg cakes.",FC,dt="Portugal",a="bolinhos de bacalhau (Brazil)"),
 A("Fiskekaker","Fried Norwegian fish cakes served with brown sauce.",FC,dt="Norway")]},
{"n":"Gefilte fish","a":"gefilte · jarred gefilte fish","d":"Ashkenazi poached fish balls or loaves, usually jarred in broth or jelly.","t":["sweet","peppery","jarred","frozen log","low-salt"],"s":GF,
 "x":[A("Jarred gefilte fish","Post-war canned or jarred patties and balls in fish-broth jelly; a 1963 jelly patent enabled mass distribution.",GF,dt="Mother's (late 1930s), Manischewitz, Mrs. Adler's, Rokeach",v=[{"n":"Mother's","mk":"Mother's","y":"1930s","d":"first brand"},{"n":"Manischewitz","mk":"Manischewitz","y":"","d":"jarred"},{"n":"Rokeach","mk":"Rokeach","y":"","d":"jarred"}]),
 A("Sweet and peppery styles","Galician sugar-sweet versus Litvak black-pepper gefilte fish, divided by the 'Gefilte Fish Line'.",GF,dt="regional taste divide")],
 "m":[["Manischewitz gefilte fish","Manischewitz"],["Rokeach gefilte fish","Rokeach"],["Mrs. Adler's gefilte fish","Mrs. Adler's"]]},
{"n":"Fish pâté & rillettes","a":"fish terrine · taramasalata · fish rillettes","d":"Pâté, terrine or galantine of fish sold as a loaf or slice to be cut; a spread or dip in a jar or tub is in Pantry Staples.","t":["pâté","terrine","rillettes","smoked mackerel pâté","taramasalata"],"s":"https://www.formanandfield.com/product/scottish-salmon-langoustine-terrine/",
 "x":[A("Taramasalata","Greek and Turkish meze spread of cured cod or carp roe with olive oil, lemon and bread or potato; good versions are beige, not pink.","https://en.wikipedia.org/wiki/Taramasalata",dt="served on Clean Monday in Greece")]}
]
B=[{"n":"Birds Eye","c":"United Kingdom","f":"","seg":"Mainstream","kf":"fish fingers","d":"Frozen food brand that commercialised fish fingers under General Foods in 1953.","lines":["Fish fingers"],"eras":[],"sig":["Birds Eye fish fingers"],"sc":[],"rel":["Findus","Iglo"],"s":"https://en.wikipedia.org/wiki/Fish_finger"},
{"n":"Findus","c":"Sweden","f":"1945","seg":"Mainstream","kf":"frozen fish","d":"Swedish frozen food brand sold in the UK from 1958.","lines":[],"eras":[],"sig":[],"sc":[],"rel":["Birds Eye"],"s":"knowledge"},
{"n":"Gorton's","c":"United States","f":"","seg":"Mainstream","kf":"fish sticks","d":"American frozen seafood brand, subsidiary of Nissui.","lines":[],"eras":[],"sig":[],"sc":[],"rel":["Nissui"],"s":"https://en.wikipedia.org/wiki/Nissui"},
{"n":"Manischewitz","c":"United States","f":"","seg":"Mainstream","kf":"kosher foods","d":"Kosher food brand selling jarred gefilte fish.","lines":[],"eras":[],"sig":["Jarred gefilte fish"],"sc":[],"rel":["Rokeach"],"s":"https://en.wikipedia.org/wiki/Gefilte_fish"}]
out={"kinds":K,"brands":B,"traditions":[],"notes":"Tier shelf: 5 kinds (4 new, Fish pâté & rillettes kept from k231). Test-winner models kept at brand level only: Stiftung Warentest (test 3/24, 21 Feb 2024) rated only two fish-finger products good, named as Frosta and Alnatura in a search snippet only (the test.de page is paywalled), so those two are listed tentatively. Which? results not found. Not added for lack of a retrieved page: Young's, La Belle-Iloise rillettes, smoked mackerel pâté. Fish fingers: the 1955 UK launch in the brief was not confirmed (the Wikipedia page gives 1953)."}
p='work/J2/shelves/06_01.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1);os.replace(p+'.tmp',p)
