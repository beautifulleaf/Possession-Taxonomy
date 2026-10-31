import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/C5.json'
d=json.load(open(P))
K={};E={}
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      K[k['n']]=k
      for e in k.get('x',[]): E[e['n']]=e
c1="""Denim Blue|Misty Blue|Sargasso Sea|Aqua Lagoon|Eau de Nil|Twilight|Asa Blue|Havasu Turquoise|Beau Blue|Midnight|Blue Black|Kensington Blue|Turquoise|Oxford Blue|Prussian Blue|Mediterranean Blue|Aqua Blue|Majestic Blue|Florida Blue|Presidential Blue|Imperial Blue|Washable Blue|Indigo|China Blue|Steel Blue|Sapphire Blue|Royal Blue|Poppy Red|Pink|Claret|Crimson|Deep Magenta|Ruby|Amaranth|Flamingo Pink|Cerise|Scarlet|Maroon|Monaco Red|Brilliant Red|Passion Red|Syrah|Hope Pink|Classic Red|Oxblood|Red Dragon|Matador|Wild Strawberry|Meadow|Apple Glory|Classic Green|Green Black|Evergreen"""
c2="""Sherwood Green|Salamander|Marine|Woodland Green|Delamere Green|Soft Mint|Jade Green|Cool Green|Teal|Green Umber|Kelly Green|Ultra Green|Emerald|Spring Green|Yellow|Amber|Orange|Coral|Vermillion|Sunshine Yellow|Pumpkin|Blaze Orange|Sunset|Autumn Oak|Peach Haze|Eclipse|Graphite|Jet Black|Gray|Quartz Black|Onyx Black|Damson|Violet|Imperial Purple|Bilberry|Majestic Purple|Lavender|Amazing Amethyst|Grape|Merlot|Tyrian Purple|Ocher|Macassar|Rustic Brown|Ancient Copper|Saddle Brown|Burnt Sienna|Sepia|Warm Brown|Chocolate Brown|Golden Brown|Raw Sienna|Earl Gray|Honey Burst|Desert Burst|Cherry Sunburst|Tobacco Sunburst|Aurora Borealis|Monboddos Hat|Scribble Purple|Writers Blood|Pelham Blue|Celadon Cat"""
cols=(c1+"|"+c2).split("|")
E['Diamine']['v']=[{"n":c,"y":"","d":""} for c in cols]
E['Diamine']['d']="Liverpool-made dye inks; the standard range lists 116 colours on the retailer pages read."
E['Diamine']['s']="https://akkermandenhaag.nl/en/products/diamine-fountain-pen-ink"
h=E['J. Herbin 1670']
for n in["Caroube de Chypre","Bleu Ocean","Stormy Grey","Emerald of Chivor"]:
  h['v'].append({"n":n,"y":"","d":""})
ink=K['Fountain pen ink']
ink['x'].append({"n":"J. Herbin 1798","a":"","d":"Herbin ink line of the 1798 collection; three colours named on the retailer page read.","mk":"J. Herbin","y":"","s":"https://goldspot.com/collections/j-herbin","v":[{"n":n,"y":"","d":""} for n in["Amethyste de L'Oural","Cornaline d'Egypte","Kyanite du Nepal"]],"g":"France","own":"owner not stated","tier":"Independent","cty":"France"})
ink['x'].append({"n":"J. Herbin scented inks","a":"","d":"Herbin bottled inks with a scent; seven colours named on the retailer page read.","mk":"J. Herbin","y":"","s":"https://goldspot.com/collections/j-herbin","v":[{"n":n,"y":"","d":""} for n in["Brown Cocoa","Violet","Red Rose","Blue Lavender","Bleu Plenitude","Ambre Insouciance","Brun Prevenance"]],"g":"France","own":"owner not stated","tier":"Independent","cty":"France"})
E['Leuchtturm1917 Medium A5']['v'].append({"n":"Some Lines a Day, 5 year memory notebook","mk":"Leuchtturm1917","y":"","d":"one page per day for five years"})
K['Diary or planner']['x'].append({"n":"Leuchtturm1917 Weekly Planner & Notebook","a":"","d":"Dated annual planner with the week on the left page and a lined notes page on the right.","mk":"Leuchtturm1917","y":"","s":"https://www.gouletpens.com/blogs/fountain-pen-blog/leuchtturm1917-notebooks","v":[],"g":"Germany","own":"Leuchtturm Albenverlag","tier":"Independent","cty":"Germany"})
json.dump(d,open('/tmp/c5.tmp','w'),ensure_ascii=False,indent=1)
os.replace('/tmp/c5.tmp',P)
