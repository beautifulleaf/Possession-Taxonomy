import json,copy
J=json.load(open('out/J8.json')); B=json.load(open('out/J8_brands.json'))
bl=B['b']; reg={x['n']:x for x in bl}
def kind(n):
    for dp in J['depts']:
        for s in dp['s']:
            for k in s['k']:
                if k['n']==n: return k
def mkbrand(n,**kw):
    e={"n":n,"c":"","f":"","seg":"","d":"","lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":"","kf":""}
    e.update(kw); bl.append(e); reg[n]=e
# --- J8-7 merges
merge={"Arnott's Group":"Arnott's","Barry Callebaut":"Callebaut","Kellanova":"Kellogg's","Lotte Wellfood":"Lotte","Meiji Seika":"Meiji","Frito Company":"Frito-Lay"}
for old,new in merge.items():
    o=reg[old]; n=reg[new]
    for r in o['rel']:
        if r!=new and r not in n['rel']: n['rel'].append(r)
    if old not in n['rel']: n['rel'].append(old)
    n['rel']=[r for r in n['rel'] if r!=new]
    bl.remove(o); del reg[old]
def remap(x):
    if isinstance(x,dict):
        if x.get('mk') in merge: x['mk']=merge[x['mk']]
        for v in x.values(): remap(v)
    elif isinstance(x,list):
        for i,v in enumerate(x):
            if isinstance(v,str) and i==1 and v in merge and len(x)==2: x[i]=merge[v]
            else: remap(v)
remap(J['depts'])
# --- J8-6
for dp in J['depts']:
    if dp['n']=='Confectionery traditions': dp['n']='Sweets & confectionery'
# --- J8-5
k=kind('Croissant & viennoiserie'); k['x']=[a for a in k['x'] if a['n']!='Brioche']
k=kind('Countline & chocolate bar snack'); k['x']=[a for a in k['x'] if a['n']!='Toblerone']
# --- J8-3
k=kind('Ice cream tub')
flav=['Vanilla ice cream','Chocolate ice cream','Strawberry ice cream','Neapolitan ice cream','Mint chocolate chip','Cookies and cream','Cookie dough','Rocky road','Cherry ice cream','Butter pecan','Pistachio ice cream','Rum raisin','Tutti frutti']
keep=[a for a in k['x'] if a['n'] not in flav]
for a in k['x']:
    if a['n'] in flav:
        t="flavour: "+a['n'].replace(' ice cream','').lower()
        if t not in k['t']: k['t'].append(t)
W="https://en.wikipedia.org/wiki/"
mak=[
 {"n":"Ben & Jerry's pints","a":"","d":"Vermont super-premium pints known for chunky mix-ins and named flavours, founded 1978.","mk":"Ben & Jerry's","y":"1978","s":W+"Ben_%26_Jerry%27s",
  "v":[{"n":"Cherry Garcia","mk":"Ben & Jerry's","y":"1987","d":"cherries and chocolate; named for Jerry Garcia"},{"n":"Chocolate Fudge Brownie","mk":"Ben & Jerry's","y":"1988","d":"developed after first ordering brownies from Greyston Bakery"},{"n":"Chocolate Chip Cookie Dough","mk":"Ben & Jerry's","y":"","d":"won a 2013 public survey of the maker's flavours"}],"dt":"flavour · mix-ins · dairy-free line"},
 {"n":"Häagen-Dazs pints","a":"","d":"Super-premium pints founded in the Bronx in 1960 with three flavours: vanilla, chocolate and coffee.","mk":"Häagen-Dazs","y":"1960","s":W+"H%C3%A4agen-Dazs",
  "v":[{"n":"Vanilla Swiss Almond","mk":"Häagen-Dazs","y":"","d":"brand-specific flavour"},{"n":"Rum Raisin","mk":"Häagen-Dazs","y":"","d":"brand-specific flavour"}],"dt":"flavour · pint or minicup"},
 {"n":"Jeni's pints","a":"","d":"Columbus, Ohio artisan pints, from a North Market stall opened in 2002.","mk":"Jeni's","y":"2002","s":W+"Jeni%27s_Splendid_Ice_Creams",
  "v":[{"n":"Salty Caramel","mk":"Jeni's","y":"","d":"early flavour"},{"n":"Wildberry Lavender","mk":"Jeni's","y":"","d":"early flavour"},{"n":"Queen City Cayenne","mk":"Jeni's","y":"","d":"early flavour"}],"dt":"flavour · seasonal and partner rotations"},
 {"n":"Salt & Straw pints","a":"","d":"Portland, Oregon scoop shop and pint maker known for unusual flavours, founded 2011.","mk":"Salt & Straw","y":"2011","s":W+"Salt_%26_Straw",
  "v":[{"n":"Double fold vanilla","mk":"Salt & Straw","y":"","d":"classic-style flavour"},{"n":"Honey Bear","mk":"Salt & Straw","y":"2015","d":"vanilla custard with chocolate honeycomb; school partnership flavour"},{"n":"Stop, Guac & Roll","mk":"Salt & Straw","y":"2015","d":"avocado-vanilla with cinnamon-sugar fried tortillas"}],"dt":"flavour · seasonal series"}]
k['x']=mak+keep
k['m']=[m for m in k['m'] if m[1] not in ("Ben & Jerry's","Jeni's Splendid Ice Creams","Salt & Straw","Häagen-Dazs")]
# --- J8-1
k=kind('Single-origin dark chocolate')
old={a['n']:a for a in k['x']}
cl=old['Michel Cluizel plantation bars']; pr=old['Pyramide des Tropiques']; to=old['Arriba Nacional']
dom=old['Criollo varietal bars']; mar=old['Vietnamese provincial origins']; dan=old['Two-ingredient origin bar']
ch=old['Chuao']; po=old['Porcelana']
amedei={"n":"Amedei single-origin bars","a":"","d":"Tuscan bean-to-bar maker's Venezuelan origin bars, including the Chuao village bar that popularised single-origin chocolate.","mk":"Amedei","y":"","s":po['s'],
 "v":ch['v']+po['v'],"dt":"origin · cocoa % · award year"}
amedei['v'][0]['d']=ch['d']
to=dict(to); to['n']="To'ak Pure Nacional"; to['mk']="To'ak Chocolate"; to['d']="Ecuadorian bars from old Nacional groves found and DNA-confirmed in the Piedra de Plata valley."
dom=dict(dom); dom['n']='Domori Criollo range'; dom['d']='Criollo-variety bars, including a 100% criollo bar without lecithin or flavourings.'
mar=dict(mar); mar['n']='Marou provincial origin bars'; mar['a']=''; mar['mk']='Maison Marou'
dan=dict(dan); dan['n']='Dandelion origin bars'; dan['d']='Single-origin bars made from only cocoa beans and organic cane sugar.'
new=[
 {"n":"Askinosie single-origin bars","a":"","d":"Springfield, Missouri bean-to-bar maker with fully traceable beans from Ecuador, the Philippines and Tanzania.","mk":"Askinosie","y":"2007","s":"https://en.wikipedia.org/wiki/Askinosie_Chocolate","v":[],"dt":"origin (Zamora, San Jose del Tambo, Davao, Mababu) · cocoa %"},
 {"n":"Pacari bars","a":"","d":"Ecuadorian biodynamic-certified bean-to-bar bars, including the Piura-Quemazon origin bar and a raw 70% bar.","mk":"Pacari","y":"2002","s":"https://en.wikipedia.org/wiki/Pacari_Chocolate",
  "v":[{"n":"Piura-Quemazon","mk":"Pacari","y":"2013","d":"International Chocolate Awards world final, overall gold"},{"n":"70% Raw Bar","mk":"Pacari","y":"2012","d":"International Chocolate Awards world final, overall gold"}],"dt":"origin · raw or roasted · flavoured"},
 {"n":"Friis-Holm Nicaraguan bars","a":"","d":"Danish bean-to-bar bars from Nicaraguan cocoa; the company is listed as defunct from February 2023.","mk":"Friis-Holm","y":"2007","s":"https://en.wikipedia.org/wiki/Friis-Holm",
  "v":[{"n":"Dark Milk 65%","mk":"Friis-Holm","y":"2014","d":"International Chocolate Awards gold"},{"n":"Johe 70%","mk":"Friis-Holm","y":"2014","d":"International Chocolate Awards bronze"},{"n":"Nicaliso 70%","mk":"Friis-Holm","y":"2014","d":"International Chocolate Awards bronze"}],"dt":"bean variety · cocoa %"},
 {"n":"Fruition bars","a":"","d":"Catskill Mountains small-batch bean-to-bar maker that roasts and grinds selected beans slowly.","mk":"Fruition Chocolate Works","y":"","s":"https://thechocolatelife.com/profile-fruition-chocolate-works/","v":[],"dt":"origin · cocoa %"},
 {"n":"Menakao Madagascar bars","a":"","d":"Tree-to-bar chocolate made in Madagascar from organic cacao of a family plantation near Ambanja.","mk":"Menakao","y":"2013","s":"https://criolloquetzal.ch/en/product/menakao-dark-chocolate-63-with-cacao-nibs-and-fleur-de-sel/","v":[],"dt":"cocoa % · inclusions (nibs, fleur de sel)"}]
k['x']=[amedei,cl,pr,dom,mar,to,dan]+new
k['a']+=" · maker origin bars"
for dp in J['depts']:
    if dp['n']=='Chocolate':
        dp['b'].append({"m":"Named and protected origins and vintages","v":"Chuao · Porcelana · Arriba Nacional · single-harvest vintage · two-ingredient bars","w":"Academy of Chocolate and International Chocolate Awards categories; maker labelling (concepts moved from archetypes under J8-1)"})
# brands
def add(n,c,f,s,kf,d):
    if n not in reg: mkbrand(n,c=c,f=f,seg="Artisan & independent",s=s,kf=kf,d=d)
add("Askinosie","United States","2007","https://en.wikipedia.org/wiki/Askinosie_Chocolate","bean-to-bar","Springfield, Missouri bean-to-bar maker.")
add("Pacari","Ecuador","2002","https://en.wikipedia.org/wiki/Pacari_Chocolate","biodynamic chocolate","Quito family chocolate company.")
add("Friis-Holm","Denmark","2007","https://en.wikipedia.org/wiki/Friis-Holm","Nicaraguan cocoa","Danish bean-to-bar maker, listed as defunct from February 2023.")
add("Fruition Chocolate Works","United States","","https://thechocolatelife.com/profile-fruition-chocolate-works/","bean-to-bar","Catskill Mountains small-batch bean-to-bar workshop.")
add("Menakao","Madagascar","2013","https://criolloquetzal.ch/en/product/menakao-dark-chocolate-63-with-cacao-nibs-and-fleur-de-sel/","tree-to-bar","Chocolate made in Madagascar from local organic cacao.")
add("Jeni's","United States","2002","https://en.wikipedia.org/wiki/Jeni%27s_Splendid_Ice_Creams","artisan pints","Columbus, Ohio ice cream maker (Jeni's Splendid Ice Creams).")
add("Salt & Straw","United States","2011","https://en.wikipedia.org/wiki/Salt_%26_Straw","unusual flavours","Portland, Oregon ice cream maker.")
# stubs for remaining unregistered mk
used={}
def walk(x,src=None):
    if isinstance(x,dict):
        if 's' in x and 'n' in x and 'mk' in x: src=x['s']
        mk=x.get('mk')
        if mk and mk not in reg: used.setdefault(mk,src)
        for v in x.values(): walk(v,src)
    elif isinstance(x,list):
        for v in x: walk(v,src)
walk(J['depts'])
for mk,s in used.items(): mkbrand(mk,s=(s or '').strip())
json.dump(J,open('work/FIX_J8/J8.new','w'),ensure_ascii=False,indent=1)
json.dump(B,open('work/FIX_J8/J8_brands.new','w'),ensure_ascii=False,indent=1)
print(len(used),len(bl))
