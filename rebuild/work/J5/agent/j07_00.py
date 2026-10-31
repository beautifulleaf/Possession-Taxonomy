from lib import *
def B(n,c,f,kf,d,s,seg="Mainstream",lines=(),sig=()):
    return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"lines":list(lines),"eras":[],"sig":list(sig),"sc":[],"rel":[],"s":s}
kinds=[
{"n":"Dates","a":"","d":"Dried or semi-dried fruit of the date palm, sold by cultivar, soft to firm.","t":["whole with stone","pitted","paste","rolled in coconut"],"s":W+"Dried_fruit",
 "x":[
 X("Medjool","king of dates","Large, caramel-sweet cultivar from Morocco's Tafilalt, about 25% of world date trade.",W+"Medjool",[],"large soft",y="Tafilalt"),
 X("Deglet Nour","","Soft, pale, semi-transparent honey-flavoured date from Tolga, Algeria; leading date by export value.",W+"Deglet_Nour",[],"semi-dry · honey"),
 X("Ajwa","Medina date","Oval, dark-skinned date associated with Medina and eaten at iftar.",W+"Ajwa_(date)",[],"dark soft"),
 X("Sukkari","","Tender, very sugary yellow to golden-brown date from Al-Qassim, Saudi Arabia.",W+"Sukkari",[],"golden soft"),
 X("Khalas","","Brown Gulf date regarded as the region's original cultivar; among the dearest Emirati dates.",W+"Khalas_(date)",[],"brown"),
 X("Mazafati","Bam date","Dark, soft Iranian date of 32-35% moisture, mainly eaten fresh rather than dried.",W+"Mazafati",[],"fresh dark soft"),
 ]},
{"n":"Raisins, sultanas and currants","a":"","d":"Dried grapes: dark raisins, golden sultanas and tiny dark Zante currants.","t":["raisins","golden raisins (sulphur-treated)","sultanas","currants","muscat raisins"],"s":W+"Raisin",
 "x":[
 X("Thompson Seedless","sultana","The common American sultana type, dried as dark raisins or treated with sulphur dioxide for golden raisins.",W+"Raisin",[],"seedless · golden or dark"),
 X("Zante currant","Black Corinth","Small, dark, tart seedless dried grape; the name 'currant' comes from Corinth.",W+"Raisin",[],"tiny · tart"),
 X("Muscat raisin","","Larger and sweeter raisins from Muscat grapes.",W+"Raisin",[],"large · sweet"),
 X("Flame raisin","","Seedless raisin from the Flame grape.",W+"Raisin",[],"seedless"),
 ]},
{"n":"Dried apricots","a":"","d":"Apricots dried whole or in halves, sulphured (orange) or unsulphured (dark, coarse).","t":["sulphured","unsulphured","halves","whole (uryuk)","kuraga (halved, pitted)"],"s":W+"Dried_apricot",
 "x":[X("Malatya apricots","Turkish dried apricots","Dried apricots from Malatya Province, which supplies roughly 95% of Turkey's output; Turkey overtook California as top producer.",W+"Dried_apricot",[V("Sulphured","","","Bright orange, 2,500-3,000 ppm SO2"),V("Unsulphured","","","Darker, coarser texture")],"sun-dried · sulphur level")]},
{"n":"Prunes","a":"dried plums","d":"Dried plums from European plum (Prunus domestica) varieties that dry without fermenting.","t":["pitted","with stone","juice-infused"],"s":W+"Prune","m":[]},
{"n":"Dried figs","a":"","d":"Figs dried in sun or ovens, including the Turkish Lob Injir sold as Calimyrna.","t":["Calimyrna (Smyrna type)","Mission","fig paste","string"],"s":W+"Fig",
 "x":[X("Calimyrna fig","Lob Injir · Smyrna fig","Smyrna-type fig needing caprifig pollination, Turkish Lob Injir brought to California in the late 19th century.",W+"Fig",[],"Turkish dried figs")]},
{"n":"Dried cranberries and berries","a":"Craisins","d":"Sweetened dried cranberries and other berries, usually infused with sugar before drying.","t":["sweetened","juice-sweetened","oil-coated"],"s":W+"Dried_cranberry",
 "x":[X("Craisins","sweetened dried cranberries","Ocean Spray's registered trademark for sweetened dried cranberries, first seen in 1989 in a Ralston Purina cereal.",W+"Dried_cranberry",[V("Craisins","Ocean Spray","1989")],"sugar-infused",mk="Ocean Spray",y="1989")]},
{"n":"Dried tropical fruit","a":"","d":"Dried mango, pineapple, papaya and banana chips; many are sugar-infused or candied before drying.","t":["mango","pineapple","papaya","banana chips","sulphured"],"s":W+"Dried_fruit",
 "x":[X("Philippine dried mango","Cebu dried mango","Dried carabao mango, a Cebu speciality made in the Guadalupe and Kalunasan areas of Cebu City.",W+"Carabao_mango",[],"carabao mango · sweetener infused")]},
{"n":"Dried apple and pear","a":"apple rings","d":"Apples and pears dried as rings, slices or chips; sulphur dioxide is sometimes used to keep colour.","t":["rings","chips","slices","unsulphured"],"s":W+"Dried_fruit"},
]
brands=[B("Ocean Spray","United States","1930","cranberries","Cranberry growers' cooperative founded 1930 as Cranberry Canners, named Ocean Spray in 1957; owner of the Craisins trademark.",W+"Ocean_Spray_(cooperative)",sig=["Craisins"])]
notes="Pruneaux d'Agen IGP, Vostizza currants PDO, Aydın figs, Hunza and Blenheim apricots, d'Ente plum: no retrieved page confirmed them, so left out. Malaga muscatels merged as Muscat raisin (page describes Muscat raisins, not 'Malaga'). Candied fruit and nuts are in J8."
write("07_00",kinds,brands,[],notes)
