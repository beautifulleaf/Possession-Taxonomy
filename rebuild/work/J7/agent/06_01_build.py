import json, os
W='https://en.wikipedia.org/wiki/'
def X(n,d,mk,y,s,v=(),dt='',a=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[{"n":a_,"mk":b,"y":c,"d":e} for a_,b,c,e in v],"dt":dt}
def B(n,c,f,seg,d,s,lines=(),sig=(),rel=(),eras=()):
    return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":list(lines),"eras":list(eras),"sig":list(sig),"sc":[],"rel":list(rel),"s":s}
kinds=[
{"n":"Molasses rum","a":"rum from molasses · rum · ron · traditional rum",
 "d":"Rum distilled from molasses or other sugar-cane by-products, the common rum type.",
 "t":["Jamaican style (pot still, high ester)","Demerara / Guyanese style (full-bodied)","Barbados style (pot and column blend)","Cuban / Spanish style (light, column, filtered)","White · gold · dark · aged","Overproof","Single estate · blended"],
 "s":"https://www.masterofmalt.com/rum/",
 "x":[
  X("Appleton Estate","Jamaican estate rum blended from pot and column distillates, distilled and aged in Jamaica.","Appleton Estate","1825",W+"Appleton_Estate",
    [("Appleton Estate Signature","Appleton Estate","","no age statement"),("Appleton Estate Reserve","Appleton Estate","","8-year-old blend"),("Appleton Estate Rare Casks 12","Appleton Estate","","12-year age statement; formerly 12 Year Old"),("Appleton Estate 15 Black River Casks","Appleton Estate","2021","15 years old"),("Appleton Estate 17 Year Old Legend","Appleton Estate","2023","tribute to Wray & Nephew 17 Years"),("Appleton Estate 21 Year Old","Appleton Estate","","21 years old"),("Appleton Estate 50 Year Old","Appleton Estate","2012","")],
    "age statement 8–51 years · blend vs. limited edition","Joy Spence blends"),
  X("Wray & Nephew White Overproof","Unaged Jamaican white rum bottled at 63% ABV.","Appleton Estate","",W+"Rum",[],"strength 63% ABV"),
  X("Hampden Estate","Trelawny estate making pot-still-only, high-ester Jamaican rum fermented in open wooden vats and muck pits.","Hampden Estate","1743",W+"Hampden_Estate",
    [("Hampden Aged 8 Years","Hampden Estate","2018","46% ABV; first estate bottling"),("Hampden Overproof","Hampden Estate","2018","60% ABV"),("Hampden HLCF Classic","Hampden Estate","","60% ABV; ester mark 400–600 g/hLAA"),("Hampden Pagos","Hampden Estate","","52% ABV, sherry-cask aged"),("Hampden Great House","Hampden Estate","2019","annual vintage blend"),("Rum Fire","Hampden Estate","2010","unaged white overproof, 63% ABV")],
    "ester mark (OWH → DOK) · age · cask · strength"),
  X("El Dorado","Guyanese Demerara rum blended from heritage wooden stills, including the Port Mourant and Versailles pot stills and the Enmore wooden Coffey still.","El Dorado","1992",W+"Demerara_Distillers",
    [("El Dorado 12 Year Old","El Dorado","","minimum 12 years"),("El Dorado 15 Year Old","El Dorado","","minimum 15 years"),("El Dorado 3 Year Old","El Dorado","","white"),("El Dorado 5 Year Old","El Dorado","",""),("El Dorado 8 Year Old","El Dorado","",""),("El Dorado 21 Year Old","El Dorado","",""),("El Dorado 25 Year Old","El Dorado","","")],
    "age 3–25 years · still marque (PM, VSG, EHP)"),
  X("Mount Gay","Barbados rum from the company whose oldest deed is dated 1703, claimed as the oldest commercial rum distillery.","Mount Gay","1703",W+"Mount_Gay_Rum",
    [("Mount Gay Eclipse","Mount Gay","1911","named for the 1910 eclipse and Halley's comet"),("Mount Gay Black Barrel","Mount Gay","","finished in charred bourbon casks"),("Mount Gay XO","Mount Gay","","blend of 8–15-year casks")],"age · cask finish"),
  X("Planteray","Rum brand of Maison Ferrand, formerly Plantation, made with the West Indies Rum Distillery in Barbados and finished in cognac casks in France.","Planteray","",W+"Rum",[],"origin island · age · finish","Plantation"),
  X("Havana Club","Cuban light-style aged rum created in 1934 by the Arechabala family of Cárdenas; Cuban version sold by Pernod Ricard, a US version by Bacardi.","Havana Club","1934",W+"Havana_Club",
    [("Havana Club Añejo 3 Años","Havana Club","","aged 3 years"),("Havana Club Añejo 7 Años","Havana Club","","dark, aged 7 years"),("Havana Club Añejo Especial","Havana Club","",""),("Havana Club Añejo 15 Años","Havana Club","",""),("Havana Club Selección de Maestros","Havana Club","",""),("Havana Club Máximo Extra Añejo","Havana Club","","about 1,000 bottles"),("Havana Club Clásico (Bacardi, US)","Bacardi","","made in Puerto Rico since 1994")],
    "age · Cuban vs. US (Bacardi) version"),
  X("Bacardi Superior","Light, column-distilled white rum, the flagship of the company founded in Santiago de Cuba in 1862.","Bacardi","1862",W+"Bacardi",
    [("Bacardi Carta Blanca","Bacardi","",""),("Bacardi 8 (Reserva Ocho)","Bacardi","",""),("Bacardi Gran Reserva","Bacardi","",""),("Bacardi 151","Bacardi","","overproof")],"white · gold · dark · aged"),
  X("Diplomático Reserva Exclusiva","Venezuelan aged rum blending pot-still and light rum, the flagship of Distilerías Unidas (DUSA).","Diplomático","",
    "https://houseofmalt.co.uk/brand/diplomatico/",
    [("Diplomático Planas","Diplomático","","6 years old"),("Diplomático Mantuano","Diplomático","","8 years old"),("Diplomático Ambassador","Diplomático","","")],"age · sold as Botucal in Germany","Botucal"),
 ]},
{"n":"Spiced rum","a":"spiced rum-based spirit · black spiced rum",
 "d":"Rum compounded with spices and usually sweetened, sold as spiced rum.",
 "t":["Gold spiced","Black spiced","Overproof spiced","Rum-based spirit drink (below rum strength)"],
 "s":"https://www.masterofmalt.com/rum/",
 "x":[
  X("Captain Morgan Original Spiced","Flagship spiced rum-based spirit drink, the brand behind the 1980s US spiced-rum boom; owned by Diageo.","Captain Morgan","1984",W+"Captain_Morgan",
    [("Captain Morgan Original Spiced Gold","Captain Morgan","1984","US introduction"),("Captain Morgan 100 Proof Spiced","Captain Morgan","",""),("Captain Morgan Black Spiced","Captain Morgan","",""),("Captain Morgan Private Stock","Captain Morgan","",""),("Captain Morgan Spiced Gold 0.0%","Captain Morgan","","alcohol-free")],"strength · gold vs. black"),
  X("Kraken Black Spiced","Caribbean black spiced rum blended with cinnamon, ginger and clove, sold in a bottle with a sea-monster label.","Kraken","2010",W+"Kraken_Rum",
    [("Kraken Black Spiced Rum","Kraken","2010","47% ABV"),("Kraken Gold Spiced","Kraken","2023","35% ABV")],"strength · black vs. gold"),
  X("Sailor Jerry Spiced","Blended rum-based spirit with vanilla, lime and spices, named after tattoo artist Norman 'Sailor Jerry' Collins.","Sailor Jerry","",
    "https://www.diffordsguide.com/beer-wine-spirits/756/sailor-jerry",
    [("Sailor Jerry Spiced (UK relaunch)","Sailor Jerry","2010","41% ABV, later 40%")],"strength by market"),
 ]},
{"n":"Rhum agricole","a":"rum from cane juice · cane-juice rum · rhum",
 "d":"Rum distilled from fresh sugar-cane juice, chiefly in the French Caribbean.",
 "t":["AOC Martinique","Blanc · élevé sous bois · vieux","VSOP · XO · vintage (millésime)","Brut de colonne"],
 "s":"https://www.masterofmalt.com/style/rhum-agricole/",
 "x":[
  X("Rhum J.M","AOC Martinique rhum agricole from the Fonds-Préville distillery at Macouba, at the foot of Mount Pelée.","Rhum J.M","1845",
    "https://www.diffordsguide.com/producer/1218/rhum-jm/about",
    [("Rhum J.M Blanc 50%","Rhum J.M","",""),("Rhum J.M VSOP","Rhum J.M","",""),("Rhum J.M XO","Rhum J.M","",""),("Rhum J.M Terroir Volcanique","Rhum J.M","",""),("Rhum J.M Shrubb","Rhum J.M","","orange liqueur")],"blanc · aged grade · vintage"),
  X("Rhum Clément","Martinique rhum agricole house dating from 1887.","Rhum Clément","1887",W+"Rhum_Cl%C3%A9ment",[],"blanc · aged grade"),
  X("Neisson","Family distillery at Le Carbet, Martinique, known for its white rhum and aged AOC rhums.","Neisson","1931",
    "https://www.rhumattitude.com/en/marque/neisson",
    [("Rhum par Neisson 52.5°","Neisson","","classic white; also organic"),("L'Esprit de Neisson","Neisson","","brut de colonne white"),("Le Vieux par Neisson","Neisson","","45°"),("Le XO par Neisson","Neisson","",""),("Neisson Clos Godinot","Neisson","","52.5°")],"white · aged · single-plot · vintage"),
  X("Clairin","Unfiltered Haitian cane spirit from native cane, spontaneously fermented and distilled in small Creole stills by guildive micro-distilleries.","","",W+"Clairin",
    [("Clairin Sajous 2023","Distillerie Chelo","2023","")],"village distillery · cane variety · vintage"),
 ],
 "m":[["Chamarel Premium White Rum","La Rhumerie de Chamarel"],["Chamarel XO Rum","La Rhumerie de Chamarel"]]},
{"n":"Cachaça","a":"pinga · caninha",
 "d":"Brazilian spirit distilled from fermented sugar-cane juice and bottled at 38–48% ABV.",
 "t":["Branca / prata (clear)","Amarela / ouro (aged, coloured)","Envelhecida · premium · extra premium","Wood: oak · amburana · native Brazilian woods","Industrial (column) · artisanal (alambique)"],
 "s":"https://www.masterofmalt.com/cachaca/",
 "x":[
  X("Cachaça 51","Best-selling industrial cachaça from Pirassununga, São Paulo, made by Companhia Müller de Bebidas.","Cachaça 51","1959",W+"Cacha%C3%A7a_51",[],"","Caninha 51 · Pirassununga 51"),
  X("Ypióca","Cachaça from Ceará made by the Ypióca group, owned by Diageo since 2012; some aged in ex-bourbon oak.","Ypióca","",W+"Ypi%C3%B3ca",
    [("Ypióca Crystal","Ypióca","",""),("Ypióca Gold","Ypióca","",""),("Ypióca 150","Ypióca","","")],"clear vs. gold"),
  X("Avuá","Single-estate artisanal cachaça from a family farm in Brazil, made by a female distiller.","Avuá","",
    "https://coolhunting.com/food-drink/avua-cachaca/",
    [("Avuá Prata","Avuá","","unaged"),("Avuá Amburana","Avuá","","two years in amburana casks")],"unaged vs. native-wood aged"),
 ],
 "m":[["Yaguara Cachaca Still Strength","Yaguara"],["Novo Fogo Organic Silver Cachaca","Novo Fogo"],["Leblon Cachaca","Leblon"],["Pitú","Pitú"],["Velho Barreiro","Velho Barreiro"],["Sagatiba Pura","Sagatiba"],["Santo Grau","Santo Grau"],["Cachaça 61","Cachaça 61"]]},
{"n":"Arrack","a":"arak (Asian) · Batavia arrack · Ceylon arrack · coconut arrack · palm spirit",
 "d":"South and Southeast Asian spirit distilled from coconut-flower sap, sugar cane or rice, depending on country.",
 "t":["Batavia (Java, cane with red-rice starter)","Ceylon (coconut-flower sap)","Premium aged (halmilla vats) · premium clear · common"],
 "s":"https://www.masterofmalt.com/arrack/",
 "x":[
  X("Batavia arrack","Pot-distilled Javanese cane spirit whose fermentation is started with wild yeast on red-rice cakes, named after Batavia (Jakarta).","","",W+"Arrack",
    [("By The Dutch White Batavia Arrack","By The Dutch","","48% ABV; rested 8–12 months in teak vats on Java"),("KWT","Batavia Arak Maatschappij","","historic brand"),("OGL","Batavia Arak Maatschappij","","historic brand"),("Batavia-Arrack van Oosten","","","")],
    "white vs. cask-aged · strength"),
  X("Ceylon arrack","Sri Lankan spirit of fermented coconut-flower sap and water, made premium aged in halmilla vats, premium clear, or blended.","","",W+"Arrack",
    [("Ceylon Arrack","Rockland Distilleries","",""),("White Lion VSOA","","","export (US market)")],"grade (aged · clear · common) · age in halmilla vats"),
 ]},
]
brands=[
 B("Appleton Estate","Jamaica","1825","Rum distillery","Jamaican estate rum of J. Wray & Nephew, a Campari Group subsidiary; master blender Joy Spence since 1997.",W+"Appleton_Estate",["Appleton Estate","Wray & Nephew","Kingston 62"],["Appleton Estate","Wray & Nephew White Overproof"],["Hampden Estate"],["Joy Spence, master blender, 1997–"]),
 B("Hampden Estate","Jamaica","1743","Rum distillery","Trelawny estate distilling pot-still, high-ester Jamaican rum; own bottlings with Velier since 2018.",W+"Hampden_Estate",["Hampden","Rum Fire"],["Hampden Estate"],["Appleton Estate"]),
 B("El Dorado","Guyana","1992","Rum brand","House rum brand of Demerara Distillers Ltd, made from heritage wooden stills in Guyana.",W+"Demerara_Distillers",[],["El Dorado"]),
 B("Mount Gay","Barbados","1703","Rum distillery","Barbados rum company, majority owned by Rémy Cointreau since 1989.",W+"Mount_Gay_Rum",["Eclipse","Black Barrel","XO"],["Mount Gay"]),
 B("Planteray","France","","Rum brand","Maison Ferrand's rum brand, renamed from Plantation in 2024, blended from Caribbean rums with a Barbados distillery.","https://www.thespiritsbusiness.com/2026/06/inside-the-planteray-rebrand-with-alexandre-gabriel/",[],["Planteray"]),
 B("Havana Club","Cuba","1934","Rum brand","Cuban rum brand made by Corporación Cuba Ron with Pernod Ricard; a separate US version is made by Bacardi.",W+"Havana_Club",["Añejo 3 Años","Añejo 7 Años"],["Havana Club"],["Bacardi"]),
 B("Bacardi","Bermuda","1862","Spirits group","Family-owned spirits company founded in Santiago de Cuba by Facundo Bacardí Massó, headquartered in Hamilton, Bermuda.",W+"Bacardi",["Superior","Carta Blanca","Gran Reserva"],["Bacardi Superior"],["Havana Club"]),
 B("Diplomático","Venezuela","","Rum brand","Venezuelan aged rum made by Distilerías Unidas (DUSA); sold as Botucal in Germany.","https://houseofmalt.co.uk/brand/diplomatico/",["Reserva Exclusiva","Mantuano","Planas","Ambassador"],["Diplomático Reserva Exclusiva"]),
 B("Captain Morgan","US Virgin Islands","1944","Spiced rum brand","Diageo rum brand, launched by Seagram in 1944, best known for Original Spiced.",W+"Captain_Morgan",["Original Spiced","Black Spiced","Private Stock"],["Captain Morgan Original Spiced"]),
 B("Kraken","United States","2010","Spiced rum brand","Black spiced rum brand of Proximo Spirits, Jersey City.",W+"Kraken_Rum",["Black Spiced","Gold Spiced"],["Kraken Black Spiced"]),
 B("Sailor Jerry","United Kingdom","","Spiced rum brand","Spiced rum-based spirit of William Grant & Sons, named after tattoo artist Norman Collins.","https://www.diffordsguide.com/beer-wine-spirits/756/sailor-jerry",[],["Sailor Jerry Spiced"]),
 B("Rhum J.M","Martinique","1845","Rhum agricole distillery","Fonds-Préville distillery at Macouba, owned by G.B.H since 2002.","https://www.diffordsguide.com/producer/1218/rhum-jm/about",["Blanc","VSOP","XO","L'Atelier des Rhums"],["Rhum J.M"],["Neisson","Rhum Clément"]),
 B("Rhum Clément","Martinique","1887","Rhum agricole house","Martinique rhum agricole brand.",W+"Rhum_Cl%C3%A9ment",[],["Rhum Clément"],["Rhum J.M","Neisson"]),
 B("Neisson","Martinique","1931","Rhum agricole distillery","Family distillery at Le Carbet making AOC Martinique rhum agricole, including organic and aged expressions.","https://www.rhumattitude.com/en/marque/neisson",["Rhum par Neisson","L'Esprit","Le Vieux","XO"],["Neisson"],["Rhum J.M","Rhum Clément"]),
 B("Cachaça 51","Brazil","1959","Cachaça brand","Cachaça of Companhia Müller de Bebidas, Pirassununga, founded by Guilherme Müller.",W+"Cacha%C3%A7a_51",["51 Ice"],["Cachaça 51"]),
 B("Ypióca","Brazil","","Cachaça brand","Cachaça brand from Ceará, acquired by Diageo in 2012.",W+"Ypi%C3%B3ca",["Ypióca Gold","Ypióca Crystal","Ypióca 150"],["Ypióca"]),
 B("Avuá","Brazil","","Cachaça brand","Single-estate artisanal cachaça brand.","https://coolhunting.com/food-drink/avua-cachaca/",["Prata","Amburana"],["Avuá"]),
 B("By The Dutch","Netherlands","","Spirits brand","Dutch brand bottling Batavia arrack distilled on Java, blended in Amsterdam and bottled in Schiedam.","https://www.bythedutch.com/white-indonesian-rum-batavia-arrack/",[],["Batavia arrack"]),
]
trads=[
 {"n":"Haitian clairin","g":"Food & drink","r":"Haiti","p":"18th century – present","d":"Artisan cane spirit made by some 500–600 village micro-distilleries (guildives).","tech":"Spontaneous fermentation of cane juice or syrup; distillation in Creole stills; no filtration","mat":"Native non-hybrid sugar cane","forms":["Clairin"],"ctr":["Guildive micro-distilleries","La Maison & Velier (export promotion)"],"auth":"HaïRum certification mark","s":W+"Clairin"},
 {"n":"Sri Lankan coconut arrack","g":"Food & drink","r":"Sri Lanka","p":"","d":"Spirit distilled from fermented sap of unopened coconut flowers.","tech":"Sap tapping, fermentation, distillation; ageing in halmilla wood vats","mat":"Coconut-flower sap, water","forms":["Ceylon arrack"],"ctr":["DCSL","IDL","Rockland Distilleries","Acme Lanka"],"auth":"Only coconut sap and water in premium grades; common grades blended with molasses or neutral spirit","s":W+"Arrack"},
]
notes=("Kinds kept: all 5 planned (Arrack renamed from 'Arrack & palm spirit'). Rum style traditions (Jamaican, Demerara, Barbados, Cuban/Spanish) are types, not kinds. "
 "Clairin placed as an archetype under Rhum agricole (cane-juice spirit; old Clairin Sajous model kept as its version). Chamarel models kept in m. "
 "Old cachaça models without makers given their brand name as maker (Yaguara, Novo Fogo, Leblon, Pitú, Velho Barreiro, Sagatiba, Santo Grau, Cachaça 61). "
 "Left out: Planteray versions (no retrieved page listed expressions; drinksint fetch returned empty); Rhum Clément expressions (page lists none); "
 "Diplomático founding year (sources only say late 1950s); Sailor Jerry launch year (not found). Wikipedia El Dorado_rum, Diplomático and Sailor Jerry articles 404. "
 "Rhum Clément page mentions no founder. Charanda (Mexico) and other world cane spirits not added.")
out={"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes}
p='work/J7/shelves/06_01.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
