import json,copy
O='out/'
d=json.load(open(O+'H1.json')); B=json.load(open(O+'H1_brands.json'))
loc={}
for dp in d['depts']:
    for s in dp['s']:
        for i,k in enumerate(s['k']): loc[k['n']]=(s,k)
def K(n): return loc[n][1]
def rm(n):
    s,k=loc.pop(n); s['k'].remove(k)
def dropm(n,pairs):
    k=K(n); k['m']=[m for m in k.get('m',[]) if m not in pairs]
# H1-1
W='https://en.wikipedia.org/wiki/Electric_shaver'
k=K('Hair clipper'); 
k['x']=[
 {"n":"Wahl Magic Clip","a":"5 Star Magic Clip","d":"Wahl's professional clipper with a vibration motor and adjustable cutting head, sold in the 5 Star series.","mk":"Wahl","y":"","s":"https://en.strihacistrojky.cz/products/wahl-magic-clip","v":[{"n":"5 Star Magic Clip (corded)","mk":"Wahl","y":"","d":"vibration motor, adjustable 0.8–2.5 mm head"}],"dt":"corded or cordless · adjustable or fixed blade · guard combs"},
 {"n":"Oster Classic 76","a":"Oster 76","d":"Oster's universal-motor professional clipper, a barbershop staple with detachable blades.","mk":"Oster","y":"","s":"https://madegooddesigns.com/oster-clippers-brand-guidelines/","v":[],"dt":"universal motor · detachable blades · blade sizes"},
 {"n":"Andis Master","a":"","d":"Andis professional clipper line made in Racine and Sturtevant, Wisconsin, and sold corded and cordless.","mk":"Andis","y":"","s":"https://en.strihacistrojky.cz/products/andis-master-cordless-lithium-ion-clipper","v":[{"n":"Master Cordless Li","mk":"Andis","y":"","d":"lithium-ion cordless version, 7,200 rpm"}],"dt":"corded or cordless · adjustable blade · guard combs"}]
dropm('Hair clipper',[["5 Star Magic Clip","Wahl"],["Master","Andis"],["Classic 76","Oster"]])
k=K('Electric shaver')
k['x']=[
 {"n":"Braun S 50","a":"","d":"Braun's first electric shaver, designed in 1938 and released after the Second World War.","mk":"Braun","y":"1951","s":"https://en.wikipedia.org/wiki/Braun_(company)","v":[],"dt":"foil head · mains powered"},
 {"n":"Braun Sixtant","a":"Sixtant SM 2","d":"Braun's foil shaver line, begun with the SM 2 designed by Hans Gugelot and Richard Fischer.","mk":"Braun","y":"1963","s":W,"v":[{"n":"Sixtant SM 2","mk":"Braun","y":"1963","d":"Gugelot and Fischer design"}],"dt":"foil head · corded or cordless"},
 {"n":"Braun Micron","a":"","d":"Braun shaver of the late 1970s, shown in the article as model 5410.","mk":"Braun","y":"1977","s":"https://en.wikipedia.org/wiki/Braun_(company)","v":[{"n":"Model 5410","mk":"Braun","y":"1977","d":"design credited to Roland Ullmann"}],"dt":"foil head"},
 {"n":"Philishave","a":"Philips Norelco rotary","d":"Philips rotary shaver line, sold as Philishave outside the US and as Norelco in the US.","mk":"Philips","y":"1939","s":"https://en.wikipedia.org/wiki/Philips_Norelco","v":[{"n":"Two-headed model","mk":"Philips","y":"1951","d":"first big commercial success"},{"n":"Philips Norelco branding","mk":"Philips","y":"2005","d":"Philishave name dropped in 2006"}],"dt":"rotary heads · wet and dry · cleaning station"}]
k=K('Beard trimmer')
k['x']=[
 {"n":"Wahl Groomsman","a":"","d":"Wahl's beard and moustache trimmer, the first cordless consumer model of its kind.","mk":"Wahl","y":"1984","s":"https://en.wikipedia.org/wiki/Wahl_Clipper","v":[],"dt":"cordless · length combs"},
 {"n":"Philips Norelco OneBlade","a":"OneBlade","d":"Philips Norelco electric shaver-and-trimmer with a single oscillating blade.","mk":"Philips","y":"","s":"https://en.wikipedia.org/wiki/Philips_Norelco","v":[{"n":"OneBlade 360","mk":"Philips","y":"","d":"later version"}],"dt":"hybrid trimmer and shaver · clip-on combs"}]
dropm('Beard trimmer',[["OneBlade 360","Philips"]])
# H1-3 mk
loc['Lipstick'][1]
for kn,xn,mk in [('Lipstick','Clinique Almost Lipstick Black Honey','Clinique'),('Lipstick','Maybelline SuperStay Matte Ink','Maybelline'),('Lip balm','Laneige Lip Sleeping Mask','Laneige')]:
    for x in K(kn)['x']:
        if x['n']==xn: x['mk']=mk
have={b['n'].lower() for b in B['b']}
new=[("Astra","","","Value","blades","Gillette-group platinum-coated safety razor blades.","https://www.coifferie.com/us/go/product/70847269"),
("Aztec Secret","","","Mainstream","clay mask","Indian Healing Clay bentonite powder.","https://banish.com/blogs/article/aztec-secrets-indian-healing-clay-review"),
("CurrentBody","","","Premium","LED masks","Home LED light-therapy mask maker.","https://www.currentbody.us/products/currentbody-skin-led-light-therapy-mask"),
("DAFNI","","2015","Mainstream","heated brush","Heated ceramic straightening brush maker.","https://en.wikipedia.org/wiki/Hair_iron"),
("Dep","United States","","Value","hair gel","Hair-gel brand named in the hair gel article as the modern clear gel.","https://en.wikipedia.org/wiki/Hair_gel"),
("Kampfe Brothers","United States","1880","Heritage manufactory","safety razors","Maker of the Star Safety Razor, an early American guard razor.","https://en.wikipedia.org/wiki/Safety_razor"),
("Nizoral","","","Mainstream","anti-dandruff","Ketoconazole anti-dandruff shampoo brand.","https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a17b7424-ee7e-4fcc-b6b3-0904932ae319"),
("One Two Cosmetics","","2014","Specialist","magnetic lashes","Maker of magnetic false eyelashes.","https://en.wikipedia.org/wiki/False_eyelashes"),
("RevitaLash Cosmetics","","","Premium","lash serum","Maker of RevitaLash eyelash conditioner.","https://www.revitalash.com/blogs/discovery/15th-anniversary"),
("Stephanie Brooke Company","","1940s","Heritage manufactory","dry shampoo","Maker of Minipoo, the first commercial dry shampoo.","https://en.wikipedia.org/wiki/Dry_shampoo"),
("Trim","United States","1947","Heritage manufactory","nail clippers","Nail-clipper brand of W. E. Bassett.","https://en.wikipedia.org/wiki/Nail_clipper"),
("Williams","United States","1840","Heritage manufactory","shaving soap","American mug shaving soap produced since 1840.","https://en.wikipedia.org/wiki/Shaving_soap"),
("Oster","United States","1924","Mainstream","clippers","John Oster company, founded 1924 in Racine, Wisconsin; makes clippers.","https://madegooddesigns.com/oster-clippers-brand-guidelines/")]
for n,c,f,seg,kf,dd,s in new:
    if n.lower() in have: continue
    B['b'].append({"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":dd,"lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":s})
# H1-4
dropm('Styling cream',[["Complete Air Dry Cream","JVN"],["6-in-1 Styling Cream","Rizos Curls"]])
dropm('Heat protectant',[["Ultimate Repair 5-in-1 Protective Leave-In","Wella Professionals"],["Cream Heat Spray","Maria Nila"]])
dropm('Face powder',[["Cloud Set Loose Translucent Setting + Blurring Powder","Kosas"]])
dropm('Lip liner',[["Lassi Lips Staining Lip Liner","Kulfi"]])
K('Period underwear')['m']=[["Thinx Air","Thinx"],["Thinx Super","Thinx"],["Modibodi range","Modibodi"],["Knix range","Knix"],["Saalt range","Saalt"]]
K('Menstrual cup')['m']=[["Original Silicone Menstrual Cup (sizes A, B)","Mooncup"],["DIVA Cup Model 1","DivaCup"],["DIVA Cup Model 2","DivaCup"],["Saalt cup range","Saalt"],["TOM Organic cup range","TOM Organic"],["Cervix Cup","Hello Period"]]
# H1-5
st=K('Scalp treatment'); sc=K('Scalp scrub')
st['a']+=' · scalp scrub · scalp exfoliator'; st['t']+=['scalp scrub (salt, sugar or grain)']
st['d']='Serum, tonic, acid treatment or scrub applied to the scalp (detox, soothing, oil control); minoxidil medicines are not included.'
st['m']+=sc['m']; rm('Scalp scrub')
a=K('Acne spot treatment'); p=K('Pimple patch')
a['a']+=' · pimple patch · acne patch · hydrocolloid patch'; a['t']+=[t for t in p['t'] if t not in a['t']]
a['d']='Paste, gel, lotion, cream or hydrocolloid patch dabbed or stuck on a single blemish to dry or calm it.'
a['x']+=p['x']; a['m']+=p['m']; rm('Pimple patch')
mo=K('Hair mousse'); v=K('Volumising spray')
mo['n']='Hair mousse & volumising spray'; mo['a']=(mo['a']+' · '+v['a']); mo['t']+=[t for t in v['t'] if t not in mo['t']]
mo['d']='Foam or spray styling product worked into damp hair for volume, curl definition or light hold.'
mo['x']=v['x']; mo['m']+=v['m']; rm('Volumising spray'); loc['Hair mousse & volumising spray']=loc.pop('Hair mousse')
# H1-7
hs=loc['Hairbrush'][0]
hs['k'].append({"n":"Hair towel","a":"","d":"Towel or wrap shaped or sized for drying hair, often microfibre or turban-shaped.","m":[["The Hair Towel","Crown Affair"],["Microfibre Hair Towel","Only Curls"],["Towel Turban","Only Curls"]],"s":"https://onlycurls.com/collections/towel-turbans"})
ad=K('Anal douche'); ad['t']=['Handheld bulb','Tap or shower hose','Single-use saline bottle']; ad['s']='https://en.wikipedia.org/wiki/Anal_douche'
# H1-8
for x in K('Lip balm')['x'][:]:
    if x['n']=='Elizabeth Arden Eight Hour Cream': K('Lip balm')['x'].remove(x)
for x in K('Body lotion & butter')['x']:
    if x['n']=='Elizabeth Arden Eight Hour Cream': x['dt']+=' · also sold and used as a lip salve'
ey=K('Eyeliner'); koh=[x for x in K('Kohl & surma')['x'] if x['n']=='Kajal'][0]
ey['x']=[x for x in ey['x'] if x['n']!='Kajal']
koh['v']=[{"n":"Eyeconic Kajal","mk":"Lakmé","y":"","d":"intense black, waterproof pencil; listed under Eyeliner as a pencil type"}]
koh['d']=koh['d'].replace('modern pencils sit under Eyeliner','modern pencils are also sold as eyeliner (see Eyeliner, pencil type)')
json.dump(d,open('work/FIX_H1/H1.new.json','w'),ensure_ascii=False,indent=1)
json.dump(B,open('work/FIX_H1/H1_brands.new.json','w'),ensure_ascii=False,indent=1)
