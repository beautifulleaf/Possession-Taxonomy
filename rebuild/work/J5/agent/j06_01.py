from lib import *
def B(n,c,f,kf,d,s,seg="Mainstream",lines=(),sig=()):
    return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"lines":list(lines),"eras":[],"sig":list(sig),"sc":[],"rel":[],"s":s}
kinds=[
{"n":"Table olives","a":"","d":"Olives cured in brine, salt or by another cure.","t":["green","black","stuffed","pitted","lye-cured","brine-cured"],"s":W+"Kalamata_olive","m":[["Divina Castelvetrano Olives","Divina"]],
 "x":[
 X("Kalamata olive","Kalamon","Almond-shaped dark purple Greek olive cured in brine and wine vinegar; the Kalamata name is PDO, identical olives elsewhere are sold as Kalamon.",W+"Kalamata_olive",[],"dark purple · wine vinegar",y="PDO"),
 X("Nocellara del Belice","Castelvetrano olive","Large, mild, buttery green Sicilian table olive, sold as Castelvetrano in the US; table olive has a DOP.",W+"Nocellara_del_Belice",[V("Divina Castelvetrano Olives","Divina")],"green · Valle del Belice",y="DOP"),
 X("Manzanilla olive","","Spanish olive originally from Seville, sold whole, pitted or stuffed; California uses it for canned black olives.",W+"Manzanilla_olive",[],"stuffed · pitted"),
 X("Niçoise and Taggiasca olive","Cailletier","Small olive of the Nice and Ligurian area, key to salade niçoise; AOC Olive de Nice in France, protected Taggiasca in Italy.",W+"Cailletier",[V("Olive de Nice AOC"),V("Taggiasca DOP")],"small black",y="AOC / DOP"),
 X("Picholine","","French olive from the Gard, lye-cured then brine-fermented up to a year; the classic cocktail olive.",W+"Picholine",[],"lye-cured · brined"),
 ]},
{"n":"Gherkins","a":"cornichons","d":"Small cucumbers pickled in vinegar.","t":["cornichon (tarragon vinegar)","sweet gherkin","dill","Spreewald"],"s":W+"Pickled_cucumber","m":[["Maille Original Cornichons","Maille"]],
 "x":[X("Spreewälder Gurken","Spreewald gherkins","Sour, spicy pickled cucumbers from Brandenburg with EU PGI since March 1999; flavoured with a secret blend of leaves.",W+"Spreewald_gherkins",[],"basil · lemon balm · grape and cherry leaves",y="PGI 1999")]},
{"n":"Pickled peppers","a":"","d":"Peppers pickled in vinegar.","t":["pepperoncini","cherry pepper","jalapeño","banana pepper","lacto-fermented"],"s":W+"Pickled_pepper","m":[["Mezzetta Golden Greek Peperoncini","Mezzetta"]]},
{"n":"Capers","a":"caperberries","d":"Preserved flower buds of the caper bush, in salt or brine; the fruit are caperberries.","t":["salt-packed","brined","caperberries"],"s":W+"Caper","m":[]},
{"n":"Sauerkraut","a":"","d":"Salt-fermented shredded cabbage.","t":["raw","pasteurised","with caraway"],"s":W+"Sauerkraut","m":[["Wildbrine Organic Green Sauerkraut","Wildbrine"]]},
{"n":"Kimchi","a":"","d":"Salt- and chilli-fermented vegetables, usually napa cabbage.","t":["jar","tub","vegan"],"s":W+"Kimchi","m":[["Jongga Mat Kimchi","Jongga"],["Lucky Foods Spicy Seoul Kimchi","Lucky Foods"],["Mother In Law's House Napa Cabbage Kimchi","Mother In Law's Kimchi"],["Sunja's All Natural Medium Spicy Kimchi","Sunja's"]],
 "x":[X("Baechu kimchi","napa cabbage kimchi","The most common kimchi, whole napa cabbage leaves in a chilli paste; over 70% of marketed kimchi in 2004.",W+"Kimchi",[],"napa cabbage"),
      X("Kkakdugi","radish kimchi","Spicy kimchi of cubed Korean radish with fermented shrimp.",W+"Kimchi",[],"radish cubes"),
      X("Oi-sobagi","cucumber kimchi","Cucumber kimchi stuffed with seafood and chilli paste, popular in spring and summer.",W+"Kimchi",[],"cucumber")]},
{"n":"Japanese pickles","a":"tsukemono","d":"Salt-, bran- or vinegar-pickled vegetables and fruit served with rice.","t":["umeboshi","takuan","nukazuke","beni shōga"],"s":W+"Tsukemono",
 "x":[X("Umeboshi","pickled ume","Very salty and sour salt-pickled, sun-dried ume fruit, eaten with rice; honey-sweetened versions exist.",W+"Umeboshi",[],"red shiso · honey"),
      X("Takuan","pickled daikon","Pickled daikon radish, a favourite tsukemono with rice.",W+"Tsukemono",[],"daikon")]},
{"n":"Indian pickles","a":"achar","d":"Spiced oil- or brine-based pickles of mango, lime and other produce.","t":["oil-based","no-oil (brine)","mango","lime"],"s":W+"South_Asian_pickle",
 "x":[X("Mango pickle","aam ka achar","Raw-mango pickle in whole baby, cut, avakaya (Andhra) and kadumanga (Kerala) styles.",W+"Mango_pickle",[V("Avakaya","","","Mustard powder, chilli, salt, gingelly oil; matures four to eight weeks"),V("Kadumanga","","","Tender whole mangoes from Kerala"),V("Amba","","","Tangy pickled green mango popular in the Middle East")],"mustard oil · fenugreek"),
      X("Lime pickle","lemon pickle","Whole or cut limes or lemons pickled with salt, mustard seed and turmeric; Maharashtra pickles whole lemons.",W+"South_Asian_pickle",[],"salt · mustard seed")]},
{"n":"Chutneys and relishes","a":"","d":"Sweet-sour cooked fruit and vegetable condiments, from mango chutney to British pickle.","t":["mango chutney","sweet pickle","relish"],"s":W+"Mixed_pickle","m":[["Branston Original Pickle","Branston"]],
 "x":[X("Branston Pickle","","Relish-like British mixed pickle of diced vegetables in a tomato, apple and vinegar sauce, introduced by Crosse & Blackwell in 1922.",W+"Branston_(brand)",[V("Branston Original","Branston","1922")],"diced vegetables · sweet-sour",mk="Branston",y="1922")]},
]
brands=[B("Branston","United Kingdom","1922","pickle","Pickle brand introduced by Crosse & Blackwell in 1922; owned by Mizkan since 2012.",W+"Branston_(brand)",sig=["Branston Pickle"])]
trads=[{"n":"Gimjang","g":"Food & drink","r":"Korea","p":"UNESCO 2013","d":"Making and sharing kimchi for winter over about a month from the tenth lunar month, inscribed by UNESCO in 2013.","tech":"salting and fermenting vegetables, once in earthenware jars buried in the ground","mat":"napa cabbage, radish, chilli, salt","forms":["baechu kimchi","kkakdugi","oi-sobagi"],"ctr":[],"auth":"Practice inscribed, not kimchi itself; North Korea's tradition inscribed separately in 2015","s":"https://en.wikipedia.org/wiki/Gimjang"}]
notes="Nyons, Lucques, Gordal and capers PGI (Pantelleria, Salina) not confirmed on retrieved pages so left out; Salina/Pantelleria not in the caper article as PGI. Achar sourced to South Asian pickle and Mango pickle. Maille/Mezzetta etc. kept from old data. Branston Original model name is the brand's product (page: Branston Pickle)."
write("06_01",kinds,brands,trads,notes)
