import json,copy,os
O='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(O+'B5.json'))
br=json.load(open(O+'B5_brands.json'))
tr=json.load(open(O+'B5_traditions.json'))
def count(d):
    ks=[k for dp in d['depts'] for s in dp['s'] for k in s['k']]
    return len(ks),sum(len(k.get('x',[])) for k in ks)
before=count(d); bb=len(br['b']); tb=len(tr['t'])
K={};S={}
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']: K[k['n']]=k; S[k['n']]=s
def shelf(n):
    for dp in d['depts']:
        for s in dp['s']:
            if s['n']==n: return s
# B5-1
ds=K['Dinner service']
pats=ds.pop('x')
for src,nm in [('Cup and saucer','Old Country Roses'),('Mug','Polka Dot')]:
    pats.append(K[src].pop('x')[0])
tp=K['Teapot']; tp['x']=[a for a in tp['x'] if a['n']!='Old Country Roses teapot']
W='https://en.wikipedia.org/wiki/'
def A(n,mk,y,s,dsc,v=None,dt='',a=''):
    return {"n":n,"a":a,"d":dsc,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
pats+= [
 A("Heirloom","Hornsea","1967",W+"Hornsea_Pottery","John Clappison's first full tableware range for Hornsea; collected with his later Saffron and Bronte.",dt="pieces by shape · brown or other colourways"),
 A("Saffron","Hornsea","",W+"Hornsea_Pottery","John Clappison range that followed Heirloom, among Hornsea's best-known lines.",dt="pieces by shape"),
 A("Galaxy","Midwinter","1950s",W+"Midwinter_Pottery","Hand-painted pattern by Jessie Tait for Midwinter.",dt="tea and dinner pieces"),
 A("Spanish Garden","Midwinter","1960s",W+"Midwinter_Pottery","Midwinter 1960s design, very successful on dinnerware and tea sets.",dt="tea and dinner pieces"),
 A("Jadeite (Fire-King)","Anchor Hocking","1945",W+"Fire-King","Opaque jade-green milk-glass dinnerware sold by Anchor Hocking; the most collected Fire-King colour.",
   v=[{"n":"Alice","mk":"Anchor Hocking","y":"1945–1949","d":"First Jade-ite dinnerware pattern."},
      {"n":"Jane Ray","mk":"Anchor Hocking","y":"c. 1945–1963","d":"Thinner dinnerware with a rayed rim."},
      {"n":"Restaurant Ware","mk":"Anchor Hocking","y":"c. 1948–c. 1967","d":"Thick, heavy shape made for diners and institutions."},
      {"n":"Charm","mk":"Anchor Hocking","y":"c. 1950–1956","d":"Square-format Jade-ite pattern."},
      {"n":"Shell","mk":"Anchor Hocking","y":"1965–1976","d":"Scalloped swirl edge."}],dt="Jade-ite, Peach Lustre, Turquoise Blue colours"),
 A("Pink Daisy","Pyrex","1956",W+"Pyrex","Vintage Pyrex printed pattern named among the valuable collectible patterns.",dt="bowls and casseroles"),
 A("Colonial Mist","Pyrex","1983",W+"Pyrex","Later Pyrex printed pattern named among the valuable collectible patterns.",dt="bowls and casseroles"),
]
# merge Old Country Roses duplicates already single; set dt
cp={"n":"China pattern","a":"china pattern · tableware pattern · crockery pattern","d":"A named decorative design on a ceramic or glass service, collected by house, then pattern, then piece.",
    "t":["dinner plate","side plate","bowl","cup and saucer","teapot","coffee pot","tureen","platter","gravy boat"],
    "s":"https://www.replacements.com/piece-guide","x":pats}
sh=shelf('Dinnerware'); i=[k['n'] for k in sh['k']].index('Dinner service'); sh['k'].insert(i,cp)
ds['d']="Matching set of plates, bowls and cups, sold by place setting; patterns are under China pattern."
# B5-5 teapot merge
tp['a']+=" · coffee pot · pattern teapot · chocolate pot"
tp['t']+=["service-piece teapot or coffee pot","chocolate pot","hot-water jug"]
sh=S['Teapot and coffee pot (tableware)']; sh['k']=[k for k in sh['k'] if k['n']!='Teapot and coffee pot (tableware)']
# grinder
eg=K['Electric coffee grinder']; eg['a']+=" · blade grinder · spice grinder"
sh=S['Coffee and spice grinder (blade)']; sh['k']=[k for k in sh['k'] if k['n']!='Coffee and spice grinder (blade)']
# weck
kc=K['Kitchen canister']; kc['x']=[a for a in kc['x'] if a['n']!='Weck jar']; kc['d']=kc['d'].rstrip('.')+'; Weck-style jars are under Preserving jar.'
# B5-2
RS="https://en.wikipedia.org/wiki/Coffee_roasting"
roaster={"n":"Home coffee roaster","a":"coffee bean roaster · green coffee roaster","d":"Countertop machine that roasts green coffee beans at home, by rotating drum or hot-air fluidised bed.","t":["drum roaster","hot-air (fluid-bed) roaster","profile-programmable","capacity 100 g–500 g"],"s":RS,
 "x":[A("Behmor 1600 Plus","Behmor","","https://royalcoffee.com/roasting-on-the-behmor-1600-plus/","Rotating-drum home roaster described as one of the most popular pieces of home roasting equipment.",v=[{"n":"1600AB Plus","mk":"Behmor","y":"","d":"Newer model with double-pane glass and a faster multi-speed motor."}],dt="roast sizes in pounds · preset profiles"),
      A("Gene Café CBR-101","Gene Cafe","","https://majestycoffee.com/products/gene-cafe-one-half-pound-coffee-roaster-cbr-101","Home roaster with a rotating glass chamber holding up to 250 g of green coffee per roast.",dt="250 g batch · viewable roast chamber"),
      A("Kaffelogic Nano 7","Kaffelogic","c. 2018","https://idealog.co.nz/design/2018/09/cup-programmable-logic-how-dunedin-start-kaffelogics-home-coffee-roaster-aims-disrupt-mornings","New Zealand programmable home roaster that loads roast profiles from a USB stick.",dt="roast profiles · voltage versions"),
      A("Siemens Sirocco","Siemens","1970s","https://en.wikipedia.org/wiki/Coffee_roasting","West German small fluid-bed roaster made for the home enthusiast.",dt="")]}
shelf('Coffee machines')['k'].append(roaster)
tort={"n":"Tortilla press","a":"puri press · tortilla maker","d":"Hinged pair of flat round plates, about 8 inches across, that flattens dough balls into tortillas.","t":["cast iron","cast aluminium","wood","non-stick coated"],"s":"https://en.wikipedia.org/wiki/Tortilla_press"}
shelf('Utensils & gadgets')['k'].append(tort)
# B5-3
def R(n,rs,keepm=None):
    k=K[n]; k['m']=keepm or []; k['r']=rs
R('Spatula',[['Good Grips','OXO'],['Flex-Core','Tovolo'],['Ultimate','GIR'],['Gourmet','Wüsthof']])
R('Cooking spoon',[['Good Grips','OXO'],['Revolution','Le Creuset'],['Ultimate','GIR']],[['Spootle',"Jonathan's Spoons"]])
R('Ladle',[['Good Grips','OXO'],['Ultimate','GIR'],['Parma','Küchenprofi']])
R('Whisk',[['Good Grips','OXO']])
R('Rolling pin',[['Good Grips','OXO']])
R('Dishwasher',[['300 Series','Bosch'],['800 Series','Bosch'],['G 5000 / G 7000','Miele'],['Bespoke','Samsung'],['Profile','GE Profile'],['Gallery','Frigidaire']])
K['Wine fridge']['m']=[]
R('Freestanding cooker',[['Rayburn','Rayburn'],['Profile','GE Profile'],['Signature','LG'],['Bespoke','Samsung'],['Masterpiece','Thermador']])
for k in [K['Spatula'],K['Cooking spoon'],K['Ladle'],K['Whisk'],K['Rolling pin'],K['Dishwasher'],K['Wine fridge'],K['Freestanding cooker']]:
    if not k['m']: k.pop('m')
# B5-4
for n,k in K.items():
    if 'x' in k or 't' in k:
        if 't' in k:
            k['t']=[t for t in k['t'] if not (t.startswith('steel:') or t.startswith('construction:'))]
rep={('Classic','Wüsthof'),('Classic Ikon','Wüsthof'),('Fibrox','Victorinox')}
for n in ['Paring knife','Bread knife','Kitchen utility knife','Boning knife','Carving knife']:
    k=K[n]; k['r']=[r for r in k['r'] if tuple(r) not in rep]
K["Chef's knife"]['r']=[['Classic','Wüsthof'],['Classic Ikon','Wüsthof'],['Fibrox','Victorinox']]+K["Chef's knife"]['r']
# brands
bn={b['n']:b for b in br['b']}
g=bn['Griswold Manufacturing']; o=bn.pop('Griswold')
for f in ('sig',):
    for x in o[f]:
        if x not in g[f]: g[f].append(x)
for x in o['rel']:
    if x not in g['rel']: g['rel'].append(x)
for k in K.values():
    for a in k.get('x',[]):
        if a.get('mk')=='Griswold': a['mk']='Griswold Manufacturing'
        for v in a.get('v',[]):
            if v.get('mk')=='Griswold': v['mk']='Griswold Manufacturing'
    for key in 'mr':
        for t in k.get(key,[]) or []:
            if t[1]=='Griswold': t[1]='Griswold Manufacturing'
br['b']=[b for b in br['b'] if b['n']!='Griswold']
def B(n,c,seg,kf,dsc,s,lines=None):
    return {"n":n,"c":c,"f":"","seg":seg,"d":dsc,"lines":lines or [],"eras":[],"sig":[],"sc":[],"rel":[],"s":s,"kf":kf}
names={b['n'].lower() for b in br['b']}
for b in [B("Hornsea","United Kingdom","Heritage manufactory","retro pottery","Yorkshire pottery known for John Clappison's Heirloom, Saffron and Bronte ranges.",W+"Hornsea_Pottery",["Heirloom","Saffron","Bronte"]),
          B("Midwinter","United Kingdom","Heritage manufactory","mid-century tableware","Staffordshire pottery known for Jessie Tait's Galaxy and the Spanish Garden pattern.",W+"Midwinter_Pottery",["Galaxy","Spanish Garden"]),
          B("Anchor Hocking","United States","Heritage manufactory","Fire-King glass","American glassmaker whose Fire-King Jade-ite dinnerware is widely collected.",W+"Fire-King",["Fire-King","Jade-ite"]),
          B("Behmor","United States","Specialist","home roasters","Maker of the Behmor 1600 Plus home drum coffee roaster.","https://royalcoffee.com/roasting-on-the-behmor-1600-plus/",["1600 Plus"]),
          B("Gene Cafe","South Korea","Specialist","home roasters","Maker of the CBR-101 home coffee roaster; US warranty service in Plymouth, MA.","https://majestycoffee.com/products/gene-cafe-one-half-pound-coffee-roaster-cbr-101",["CBR-101"]),
          B("Kaffelogic","New Zealand","Specialist","programmable roasters","Dunedin start-up making the Nano 7 programmable home coffee roaster.","https://idealog.co.nz/design/2018/09/cup-programmable-logic-how-dunedin-start-kaffelogics-home-coffee-roaster-aims-disrupt-mornings",["Nano 7"]),
          B("Siemens","Germany","Mainstream","appliances","German electrical maker whose Sirocco was a 1970s–80s home fluid-bed coffee roaster.","https://en.wikipedia.org/wiki/Coffee_roasting",["Sirocco"])]:
    if b['n'].lower() not in names: br['b'].append(b)
# wüsthof/victorinox lines already contain Classic, Classic Ikon, Fibrox
# traditions merge
T={t['n']:t for t in tr['t']}
def merge(keep,drop):
    a=T[keep]
    for n in drop:
        b=T.pop(n)
        for f in ('forms','ctr'):
            for x in b.get(f,[]):
                if x not in a.get(f,[]): a.setdefault(f,[]).append(x)
        for f in ('auth','tech','mat','d'):
            if not a.get(f) and b.get(f): a[f]=b[f]
merge('Nambu ironware',['Nambu tekki']); merge('Banko ware (Banko-yaki)',['Banko ware']); merge('Arita ware (incl. Imari, Kakiemon, Nabeshima)',['Arita ware'])
merge('Sheffield cutlery and plate',['Sheffield cutlery']); merge('Solingen cutlery',['Solingen blades']); merge('Thiers coutellerie',['Thiers cutlery'])
merge('Tsubame-Sanjo metalwork',['Tsubame-Sanjo metal polishing']); merge('Villedieu-les-Poêles copperwork',['Villedieu-les-Poêles copper'])
tr['t']=[T[t['n']] for t in tr['t'] if t['n'] in T]
for k in K.values():
    pass
for p,o2 in [('B5.json',d),('B5_brands.json',br),('B5_traditions.json',tr)]:
    json.dump(o2,open(O+p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(O+p+'.tmp',O+p)
print(before,count(d),bb,len(br['b']),tb,len(tr['t']))
