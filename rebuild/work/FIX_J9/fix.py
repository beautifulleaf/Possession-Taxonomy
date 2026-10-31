import json,os,copy
P='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(P+'J9.json')); br=json.load(open(P+'J9_brands.json'))
W='https://en.wikipedia.org/wiki/'
dep={x['n']:x for x in d['depts']}
def kind(dn,sn,kn):
    for s in dep[dn]['s']:
        if s['n']==sn:
            for k in s['k']:
                if k['n']==kn: return k
def shelf(dn,sn): return [s for s in dep[dn]['s'] if s['n']==sn][0]
def arch(n,mk,y,s,dd,a='',v=None):
    r={"n":n,"a":a,"d":dd,"mk":mk,"y":y,"s":s}
    if v: r['v']=v
    return r
# J9-3
common={'regular (sugar or HFCS)','cane-sugar','diet / zero sugar','caffeine-free','glass bottle','can','PET bottle','fountain syrup'}
for k in shelf('Sodas','Colas & mainstream sodas')['k']:
    if k['n'] in ('Cola','Pepper & spiced soda','Lemon-lime soda','Citrus soda','Orange soda','Fruit soda','Root beer & birch beer','Cream soda'):
        k['t']=[t for t in k['t'] if t not in common]
dep['Sodas']['b'].append({"m":"Caffeine","v":"caffeinated · caffeine-free","w":"label; applies to every soda kind"})
dep['Sodas']['note']="Sweetener, Format and Caffeine apply to every soda kind and are listed once here, not repeated per kind."
# J9-1
reg=shelf('Sodas','Regional & heritage sodas')
reg['k'].insert(0,{"n":"Cola-orange mix (Spezi)","a":"Spezi · cola-mix · Schwip Schwap","d":"Soft drink blending cola and orange soda, a German-speaking-region category.","t":["sugar-free","glass bottle (licensed brewery bottlings)"],"s":W+"Spezi",
 "x":[arch("Spezi","Riegele","1965",W+"Spezi","Cola and orange soda first marketed by Riegele of Augsburg as Kola-Misch; made under licence by regional breweries.",v=[{"n":"Krombacher Spezi","mk":"","y":"","d":"licensed brewery version"},{"n":"Paulaner Spezi","mk":"","y":"","d":"licensed brewery version"}]),
      arch("Mezzo Mix","The Coca-Cola Company","1973",W+"Mezzo_Mix","Coca-Cola's cola-orange mix, officially sold in Germany, Switzerland and Austria.")]})
lem=kind('Sodas','Colas & mainstream sodas','Lemon-lime soda')
lem['x'].append(arch("Limca","Limca","1977",W+"Limca","Lemon-lime flavoured carbonated soft drink created in India by Ramesh Chauhan of Parle Bisleri; Coca-Cola bought the brand in 1992."))
fr=kind('Sodas','Colas & mainstream sodas','Fruit soda')
fr['x'].append(arch("Faygo","Faygo","1907",W+"Faygo","Detroit pop brand with fruit punch, strawberry and grape flavours; Rock & Rye is a 1920s flavour.",v=[{"n":"Rock & Rye","mk":"Faygo","y":"","d":"1920s flavour named after a Prohibition-era drink"}]))
cs=kind('Sodas','Regional & heritage sodas','Craft & prebiotic soda')
cs['x'].append(arch("Bionade","Bionade","1995",W+"Bionade","German range of non-alcoholic, organic, fermented carbonated drinks, developed at the Peter brewery in Bavaria."))
ga=kind('Tonic & mixers','Tonic & mixers','Ginger ale')
ga['x'].append(arch("Ale-8-One","Ale-8-One","1926",W+"Ale-8-One","Ginger-ale soft drink bottled in Winchester, Kentucky and sold mainly in Kentucky."))
# lactic
fs=shelf('Fermented soft drinks','Fermented soft drinks')
fs['k'].insert(0,{"n":"Lactic soft drink","a":"milk-based soda · Calpis","d":"Soft drink with a sour-milk flavour, sold as concentrate, ready-to-drink or carbonated.","t":["concentrate","ready-to-drink","carbonated"],"s":W+"Calpis",
 "x":[arch("Calpis / Calpico","Calpis","1919",W+"Calpis","Japanese lactic-fermented milk beverage sold as a concentrate; named Calpico in North America.",v=[{"n":"Calpis Water","mk":"Calpis","y":"","d":"pre-diluted drink"},{"n":"Calpis Soda","mk":"Calpis","y":"","d":"carbonated version"}]),
      arch("Milkis","Lotte Chilsung","1989",W+"Milkis","South Korean carbonated soft drink of sugar, soda water and milk; not fermented.")]})
ml=kind('Fermented soft drinks','Fermented soft drinks','Malta & malt soft drink')
ml['x'].append(arch("Fassbrause","","1908",W+"Fassbrause","Berlin fruit-and-malt-extract drink invented by Ludwig Scholvien; the name is not protected, so many brewery versions exist.",v=[{"n":"Rixdorfer Fassbrause","mk":"","y":"","d":"Berliner Kindl Brauerei"},{"n":"Gaffels Fassbrause","mk":"","y":"","d":"Gaffel Becker & Co"}]))
# Schorle
jd=kind('Juices & smoothies','Juices & smoothies','Juice drink')
jd['t']=[t for t in jd['t'] if not t.startswith('spritzer')]
sh=shelf('Juices & smoothies','Juices & smoothies')
sh['k'].insert(sh['k'].index(jd)+1,{"n":"Juice spritzer (Schorle)","a":"Saftschorle · Fruchtschorle · Apfelschorle","d":"Fruit juice mixed with carbonated mineral water, sold ready-mixed.","t":["apple (Apfelschorle)","other fruit","sparkling fruit juice"],"s":W+"Spritzer",
 "x":[arch("Apfelschorle","","","https://en.wikipedia.org/wiki/Spritzer","Apple juice with sparkling mineral water; described as one of Germany's most popular soft drinks."),
      arch("Appletiser","Appletiser","1966",W+"Appletiser","South African sparkling apple juice, made by mixing fruit juice with carbonated water.")]})
# J9-2
nm=kind('Water','Still & mineral water','Natural mineral water')
nm['x']+= [arch("Acqua Panna","Sanpellegrino","1880",W+"Acqua_Panna","Still water from a Tuscan Apennine spring at about 1,100 m, owned by Sanpellegrino."),
 arch("Spa","Spa","","https://en.wikipedia.org/wiki/Spa_(mineral_water)","Belgian water from the Hautes Fagnes, owned by Spadel; bottled since the end of the 16th century.",v=[{"n":"Spa Reine","mk":"Spa","y":"","d":"main source"}]),
 arch("Ramlösa","Ramlösa","1707",W+"Ramlösa","Swedish mineral water from a spring in Helsingborg, owned by Carlsberg."),
 arch("Tŷ Nant","Tŷ Nant","",W+"Ty_Nant","Welsh water bottled at source in Ceredigion, sold in cobalt blue glass.",v=[{"n":"Cobalt blue bottle","mk":"Tŷ Nant","y":"1989","d":""},{"n":"Tŷ Nant Too (crimson bottle)","mk":"Tŷ Nant","y":"1999","d":""}]),
 arch("Tipperary Natural Mineral Water","Tipperary Natural Mineral Water","1986",W+"Tipperary_Natural_Mineral_Water","Irish mineral water from Annerville, Clonmel, County Tipperary.")]
sp=kind('Water','Still & mineral water','Spring water')
sp['x']+= [arch("Mountain Valley Spring Water","Mountain Valley","1871",W+"Mountain_Valley_Spring_Water","American spring water bottled continuously since 1871; now owned by Primo Water."),
 arch("Malvern","","1622",W+"Malvern_Water","English spring water from the Malvern Hills; bottling recorded in 1622 and reclassified from mineral to spring water in 2006."),
 arch("Nongfu Spring","Nongfu Spring","1996",W+"Nongfu_Spring","Chinese packaged water company; first product in 1997 from Thousand-Island Lake.")]
sm=kind('Water','Sparkling water','Sparkling mineral water')
sm['x']+= [arch("Farris","Farris","1907",W+"Farris_(mineral_water)","Norwegian sparkling mineral water from the Kong Olav V spring in Larvik; named Salus until 1915."),
 arch("Sairme","Sairme","1945",W+"Sairme","Georgian naturally carbonated mineral water from the Tsablarastsqali gorge, Imereti.")]
# J9-5
dep['Syrups & cordials']['note']="Café and flavouring syrups for drinks stay here; pantry syrups and sauces sit in J5."
dep['Fermented soft drinks']['note']="Water kefir and kombucha cultures are non-dairy; dairy kefir is in J3."
# J9-4 brand merges
def rep(o):
    if isinstance(o,dict):
        for k,v in o.items():
            if k=='mk':
                if v=='Coca-Cola (Japan)': o[k]='The Coca-Cola Company'
                if v=='Bundaberg Brewed Drinks': o[k]='Bundaberg'
            else: rep(v)
    elif isinstance(o,list):
        for i in o: rep(i)
rep(d)
B={b['n']:b for b in br['b']}
br['b']=[b for b in br['b'] if b['n'] not in ('Coca-Cola (Japan)','Bundaberg Brewed Drinks')]
B={b['n']:b for b in br['b']}
def addrel(n,r):
    b=B[n]; b['rel']=(b.get('rel') or [])
    if r not in b['rel']: b['rel'].append(r)
addrel('Coca-Cola','The Coca-Cola Company'); addrel('Pepsi','PepsiCo'); addrel('Fanta','The Coca-Cola Company')
addrel('The Coca-Cola Company','Coca-Cola'); addrel('PepsiCo','Pepsi')
B['Bundaberg']['sig']=['Bundaberg brewed soft drinks','Bundaberg Ginger Beer']
def nb(n,c,f,seg,kf,dd,s,sig):
    if n in B: return
    br['b'].append({"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":dd,"lines":[],"eras":[],"sig":sig,"sc":[],"rel":[],"s":s}); B[n]=br['b'][-1]
nb("Riegele","Germany","","Heritage manufactory","Spezi","Augsburg brewery that launched Spezi.",W+"Spezi",["Spezi"])
nb("Calpis","Japan","1916","Mainstream","lactic drink","Japanese maker of Calpis, sold as Calpico in North America.",W+"Calpis",["Calpis / Calpico"])
nb("Lotte Chilsung","South Korea","","Mainstream","Milkis","South Korean beverage company that makes Milkis.",W+"Milkis",["Milkis"])
nb("Limca","India","1977","Mainstream","lemon-lime soda","Indian lemon-lime soda, now owned by Coca-Cola.",W+"Limca",["Limca"]); B['Limca']['rel']=['The Coca-Cola Company']
nb("Faygo","United States","1907","Specialist","Detroit pop","Detroit soft drink company, subsidiary of National Beverage.",W+"Faygo",["Faygo"])
nb("Ale-8-One","United States","1926","Specialist","Kentucky ginger ale","Winchester, Kentucky ginger-ale bottler.",W+"Ale-8-One",["Ale-8-One"])
nb("Bionade","Germany","1995","Specialist","organic fermented soda","German organic fermented soft drinks from the Peter brewery.",W+"Bionade",["Bionade"])
nb("Appletiser","South Africa","1966","Mainstream","sparkling apple juice","South African sparkling apple juice brand.",W+"Appletiser",["Appletiser"])
nb("Spa","Belgium","","Mainstream","Belgian mineral water","Belgian mineral water brand owned by Spadel.",W+"Spa_(mineral_water)",["Spa"])
nb("Ramlösa","Sweden","1707","Mainstream","Swedish mineral water","Swedish mineral water from Helsingborg, owned by Carlsberg.",W+"Ramlösa",["Ramlösa"])
nb("Tŷ Nant","United Kingdom","","Premium","blue glass bottle","Welsh spring water in cobalt blue glass.",W+"Ty_Nant",["Tŷ Nant"])
nb("Tipperary Natural Mineral Water","Ireland","1986","Mainstream","Irish mineral water","Irish mineral water from County Tipperary.",W+"Tipperary_Natural_Mineral_Water",["Tipperary Natural Mineral Water"])
nb("Mountain Valley","United States","1871","Premium","Arkansas spring water","American spring water bottled since 1871.",W+"Mountain_Valley_Spring_Water",["Mountain Valley Spring Water"])
nb("Nongfu Spring","China","1996","Mainstream","Chinese bottled water","Chinese packaged water company.",W+"Nongfu_Spring",["Nongfu Spring"])
nb("Farris","Norway","","Mainstream","Norwegian sparkling water","Norwegian sparkling mineral water owned by Ringnes.",W+"Farris_(mineral_water)",["Farris"])
nb("Sairme","Georgia","","Mainstream","Georgian mineral water","Georgian naturally carbonated mineral water.",W+"Sairme",["Sairme"])
json.dump(d,open(P+'J9.json.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'J9.json.tmp',P+'J9.json')
json.dump(br,open(P+'J9_brands.json.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'J9_brands.json.tmp',P+'J9_brands.json')
