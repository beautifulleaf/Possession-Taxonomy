import json, os
W='https://en.wikipedia.org/wiki/'
LB=W+'Low-alcohol_beer'
def v(n,mk,y='',d=''): return {"n":n,"mk":mk,"y":y,"d":d}
kinds=[
{"n":"Alcohol-free beer","a":"Non-alcoholic beer · Low-alcohol beer · 0.0 beer · NA beer",
 "d":"Beer brewed to taste like beer with little or no alcohol, usually 0.5% ABV or less.",
 "t":["0.0% ABV","≤0.5% ABV","Low-alcohol (≤1.2% ABV)","Dealcoholised (vacuum or reverse osmosis)","Limited fermentation","Lager","Wheat beer","IPA & pale ale","Stout"],
 "s":LB,
 "x":[
  {"n":"Heineken 0.0","a":"Heineken Zero","d":"Alcohol-free version of Heineken lager, close in taste to the full-strength beer; the mass-market reference.","mk":"Heineken","y":"2017","s":W+"Heineken_Lager_Beer","v":[],"dt":"can · bottle · draught"},
  {"n":"Erdinger Alkoholfrei","a":"Erdinger alcohol-free","d":"Alcohol-free Bavarian wheat beer (<0.5% ABV), marketed since 2015 as a post-exercise sports drink.","mk":"Erdinger","y":"","s":W+"Erdinger",
   "v":[v("Erdinger Alkoholfrei","Erdinger","","wheat beer, <0.5% ABV"),v("Erdinger Helles Alkoholfrei","Erdinger","","alcohol-free lager"),v("Erdinger Alkoholfrei Zitrone","Erdinger","","shandy with lemonade"),v("Erdinger Alkoholfrei Grapefruit","Erdinger","","shandy with grapefruit juice")],
   "dt":"wheat beer · lager · citrus shandy"},
  {"n":"Guinness 0.0","a":"Guinness Zero","d":"Zero-alcohol version of Guinness stout; withdrawn after a 2020 launch due to contamination and relaunched in 2021.","mk":"Guinness","y":"2020","s":W+"Guinness",
   "v":[v("Guinness 0.0 (relaunch)","Guinness","2021","pubs from July, cans from August")],"dt":"can · draught"},
  {"n":"Athletic Brewing","a":"Athletic Brewing Company","d":"US craft brewery making only non-alcoholic beer; its IPAs won open competitions against alcoholic beers.","mk":"Athletic Brewing Company","y":"2017","s":W+"Athletic_Brewing_Company",
   "v":[v("Run Wild IPA","Athletic Brewing Company","2018","flagship IPA"),v("Upside Dawn Golden Ale","Athletic Brewing Company","2018",""),v("Free Wave IPA","Athletic Brewing Company","","Supreme Champion, International Beer Challenge 2020")],
   "dt":"IPA · golden ale · seasonal styles"}],
 "m":[["Clausthaler","Radeberger Group"],["Budweiser Prohibition Brew","Anheuser-Busch"],["Beck's Blue","Beck's"],["Estrella Galicia 0,0","Estrella Galicia"],["Gösser NaturGold Alkoholfrei","Gösser"],["Lucky Saint","Lucky Saint"],["Anchor Small Beer","Anchor Brewing Company"],["sörzero","sörzero"]]},
{"n":"Alcohol-free wine","a":"Non-alcoholic wine · Dealcoholised wine · Low-alcohol wine · 0.0 wine",
 "d":"Wine made in the usual way and then dealcoholised, typically to 0.5% ABV or below.",
 "t":["White","Red","Rosé","0.0% ABV","≤0.5% ABV","Low-alcohol"],
 "s":W+"Non-alcoholic_wine",
 "x":[{"n":"Torres Natureo","a":"Natureo","d":"Familia Torres range presented in 2008 as Spain's first dealcoholised wine.","mk":"Familia Torres","y":"2008","s":"https://www.corresponsables.com/actualidad/familia-torres-consigue-el-reconocimiento-al-mejor-elaborador-internacional-de-vinos-00",
   "v":[v("Natureo Muscat","Familia Torres","","white"),v("Natureo Chardonnay","Familia Torres","","white"),v("Natureo Garnacha Syrah","Familia Torres","","red"),v("Sangre de Toro Rosé 0,0","Familia Torres","","rosé; Sangre de Toro brand")],
   "dt":"grape · colour · vintage"}]},
{"n":"Alcohol-free sparkling wine","a":"Non-alcoholic sparkling wine · Alcohol-free fizz · 0.0 sparkling",
 "d":"Sparkling wine dealcoholised and then carbonated, a stand-in for Champagne, cava or prosecco.",
 "t":["White","Rosé","Brut & extra dry","Organic"],
 "s":"https://www.abelandcole.co.uk/thomson-scott-noughty-alcohol-free-sparkling-wine",
 "x":[{"n":"Noughty","a":"Thomson & Scott Noughty","d":"Organic alcohol-free sparkling Chardonnay (0%) from Thomson & Scott.","mk":"Thomson & Scott","y":"","s":"https://www.abelandcole.co.uk/thomson-scott-noughty-alcohol-free-sparkling-wine","v":[],"dt":"white · rosé"},
  {"n":"Natureo Sparkling","a":"","d":"Sparkling member of Familia Torres's dealcoholised Natureo range.","mk":"Familia Torres","y":"","s":"https://www.corresponsables.com/actualidad/familia-torres-consigue-el-reconocimiento-al-mejor-elaborador-internacional-de-vinos-00","v":[],"dt":""}]},
{"n":"Non-alcoholic spirit","a":"Alcohol-free spirit · Spirit alternative · Zero-proof spirit · NA spirit",
 "d":"Distilled or macerated botanical drink without alcohol, used in place of gin, rum, whisky or other spirits in mixed drinks.",
 "t":["Distilled botanical","Gin alternative","Rum alternative","Whisky & bourbon alternative","Tequila alternative","Aperitif-style"],
 "s":W+"Seedlip",
 "x":[{"n":"Seedlip","a":"","d":"Plant-based distilled spirit substitutes billed as the world's first distilled non-alcoholic spirits; Diageo majority-owned since 2019.","mk":"Seedlip","y":"2014","s":W+"Seedlip",
   "v":[v("Seedlip Garden 108","Seedlip","","peas and garden herbs"),v("Seedlip Spice 94","Seedlip","","spices, citrus peels, barks"),v("Seedlip Grove 42","Seedlip","","citrus and spices"),v("Seedlip Notas de Agave","Seedlip","","prickly pear, lime, agave")],
   "dt":"botanical blend · 70 cl bottle"},
  {"n":"Lyre's","a":"Lyre's Non-Alcoholic Spirits","d":"Broad range of alcohol-free analogues for classic spirits, liqueurs and vermouths.","mk":"Lyre's","y":"","s":"https://lyres.com/help-center/about-lyres-faq/",
   "v":[v("Lyre's Classico","Lyre's","","sparkling"),v("Lyre's Italian Orange","Lyre's","","bitter orange aperitif"),v("Lyre's Italian Spritz","Lyre's","",""),v("Lyre's Orange Sec","Lyre's","","triple sec alternative"),v("Lyre's Pink Gin","Lyre's","","")],
   "dt":"spirit style analogue · ready-to-drink cans"},
  {"n":"Pentire","a":"Pentire Drinks","d":"Cornish alcohol-free botanical spirits distilled from coastal plants.","mk":"Pentire","y":"2019","s":"https://food4media.com/showPRPreview/100079838",
   "v":[v("Pentire Adrift","Pentire","2019","founding spirit"),v("Pentire Seaward","Pentire","2021","pink grapefruit, sea rosemary; core from March 2021")],
   "dt":"70 cl bottle · coastal botanicals"}]},
{"n":"Alcohol-free aperitif","a":"Non-alcoholic aperitif · Aperitivo analcolico · Alcohol-free bitter",
 "d":"Bitter or bittersweet pre-dinner drink without alcohol, served on ice or as a spritz.",
 "t":["Red bitter","Orange bitter","Botanical cordial","Single-serve bottle"],
 "s":W+"Crodino",
 "x":[{"n":"Sanbittèr","a":"Bitter Sanpellegrino · Sanbitter","d":"Red non-alcoholic bitter from Sanpellegrino, described as Italy's first non-alcoholic aperitif; renamed Sanbittèr in 1985.","mk":"Sanpellegrino","y":"1961","s":"https://www.diffordsguide.com/beer-wine-spirits/7384/sanbitter-rosso",
   "v":[v("Sanbittèr Rosso","Sanpellegrino","","")],"dt":"small single-serve bottle"},
  {"n":"Crodino","a":"","d":"Orange non-alcoholic bitter of herbal extracts in a 10 cl crown-capped bottle, named after Crodo; made by Campari since 1995.","mk":"Campari Group","y":"1965","s":W+"Crodino","v":[],"dt":"10 cl bottle"},
  {"n":"Everleaf","a":"","d":"British non-alcoholic botanical aperitif made for spritzes by conservation biologist and bartender Paul Mathew.","mk":"Everleaf","y":"","s":"https://www.diffordsguide.com/bws/1238/everleaf/story",
   "v":[v("Everleaf Forest","Everleaf","","the original; 14 botanicals; bittersweet"),v("Everleaf Marine","Everleaf","","16 botanicals; crisp"),v("Everleaf Mountain","Everleaf","","12 botanicals; aromatic")],
   "dt":"botanical blend · 50 cl bottle"}]}]
brands=[
{"n":"Athletic Brewing Company","c":"United States","f":"2017","seg":"Non-alcoholic craft brewery","d":"Milford, Connecticut brewery founded by Bill Shufelt and John Walker, making only non-alcoholic beer.","lines":["Run Wild IPA","Upside Dawn","Free Wave IPA"],"sig":["Athletic Brewing"],"s":W+"Athletic_Brewing_Company"},
{"n":"Familia Torres","c":"Spain","f":"","seg":"Wine producer","d":"Catalan family wine company; presented Spain's first dealcoholised wine, Natureo, in 2008.","lines":["Natureo","Sangre de Toro"],"sig":["Torres Natureo"],"s":"https://www.corresponsables.com/actualidad/familia-torres-consigue-el-reconocimiento-al-mejor-elaborador-internacional-de-vinos-00"},
{"n":"Thomson & Scott","c":"United Kingdom","f":"","seg":"Alcohol-free wine brand","d":"Maker of the organic alcohol-free sparkling Chardonnay Noughty.","lines":["Noughty"],"sig":["Noughty"],"s":"https://www.abelandcole.co.uk/thomson-scott-noughty-alcohol-free-sparkling-wine"},
{"n":"Seedlip","c":"United Kingdom","f":"2014","seg":"Non-alcoholic spirits","d":"Founded by Ben Branson; distilled plant-based spirit substitutes; Diageo majority stake since 2019.","lines":["Garden 108","Spice 94","Grove 42","Notas de Agave"],"sig":["Seedlip"],"rel":["Diageo"],"s":W+"Seedlip"},
{"n":"Lyre's","c":"","f":"","seg":"Non-alcoholic spirits","d":"Range of alcohol-free analogues of classic spirits, liqueurs, vermouths and premixed cocktails.","lines":["Spirit alternatives","Premixed cocktails"],"sig":["Lyre's"],"s":"https://lyres.com/help-center/about-lyres-faq/"},
{"n":"Pentire","c":"United Kingdom","f":"2019","seg":"Non-alcoholic spirits","d":"Founded by Alistair Frost and Edward Grieg-Gran; spirits distilled from plants of the North Cornish coast.","lines":["Adrift","Seaward"],"sig":["Pentire"],"s":"https://food4media.com/showPRPreview/100079838"},
{"n":"Everleaf","c":"United Kingdom","f":"","seg":"Non-alcoholic aperitif","d":"London Botanical Drinks brand founded by Paul Mathew, a conservation biologist and bar owner.","lines":["Forest","Marine","Mountain"],"sig":["Everleaf"],"s":"https://www.everleafdrinks.com/pages/doesn-t-taste-like-alcohol-doesnt-need-to"},
{"n":"Campari Group","c":"Italy","f":"","seg":"Spirits and aperitif group","d":"Italian drinks group; maker of Crodino since 1995.","lines":["Campari","Crodino"],"sig":["Crodino"],"rel":["Campari"],"s":W+"Crodino"},
{"n":"Sanpellegrino","c":"Italy","f":"","seg":"Mineral water and soft drinks","d":"Italian mineral-water and soft-drink company, part of Nestlé; maker of Sanbittèr.","lines":["Sanbittèr"],"sig":["Sanbittèr"],"s":"knowledge"}]
notes=("All five kinds new (no old data). Tier mainstream beer brands kept as m (Clausthaler, Budweiser Prohibition Brew, Beck's Blue etc., from the retrieved Low-alcohol beer/Radeberger pages). "
"Heineken, Guinness and Erdinger archetypes use the register names already created on the beer shelves (04_00, 04_03, 04_04); not re-added here. "
"Left out: Sanbittèr Dry and Fizz, Lyre's founding facts (2019, Mark Livings) and Pentire Coastal Spritz (search snippets only, page fetch did not confirm); Torres Natureo 0.5%->0.0% change (drinksbusiness 403); "
"Sanbittèr renaming year conflicts (1975 company PR vs 1985 Difford's) - used Difford's 1985. No traditions apply.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/J7/shelves/11_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
