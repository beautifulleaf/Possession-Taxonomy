import json,re,os
W='/home/user/Possession-Taxonomy/rebuild/work/CARS_ADD_EUROPE/'
norm=lambda s:re.sub(r'[^a-z0-9]','',s.lower())
exist={norm(x) for x in open(W+'existing_names.txt',encoding='utf-8').read().split('\n')}
KIND={'sports car':'Sports car','supercar':'Supercar','grand tourer':'Grand tourer','roadster':'Roadster','city car':'City car','microcar':'Microcar','three-wheeler':'Three-wheeled car','three-wheeled automobile':'Three-wheeled car','off-road vehicle':'Off-roader','coupe':'Coupé','sedan':'Saloon','sports sedan':'Saloon','luxury vehicle':'Luxury saloon','crossover':'SUV'}
NS='Car, body style not stated'
PRE=['Austin-Healey','Austin','Morris','Wolseley','Riley','MG','Triumph','Standard','Rover','Range Rover','Sunbeam','Hillman','Humber','Vauxhall','Lanchester','Daimler','Lagonda','Jensen','Bristol','TVR','Singer','Alvis','Armstrong Siddeley','Allard','Reliant','Noble','Ginetta','Marcos','Ascari','Ariel','Caparo','Lister','Westfield','Ultima','Radical','Sinclair','AC','Bowler','Jowett','Talbot','Bugatti','Delahaye','Delage','Amilcar','Salmson','Panhard','Matra','Facel Vega','Simca','Ligier','Aixam','Hispano-Suiza','Panhard','Ford','Lancia','Autobianchi','Innocenti','De Tomaso','Bizzarrini','Iso','Isotta Fraschini','Pagani','Bandini','Siata','Zagato','Vignale','Nardi','ATS','Dallara','Saab','Polestar','DAF','Donkervoort','Spyker','Tatra','Dacia','Lada','Moskvitch','Moskvich','GAZ','ZIL','ZIS','UAZ','LuAZ','Izh','IZH','VAZ','Aurus','Zastava','Yugo','ARO','Togg','Rimac','Wartburg','Trabant','Horch','DKW','Auto Union','Adler','Glas','Goggomobil','NSU','Lloyd','Gutbrod','Goliath','Hanomag','Heinkel','Messerschmitt','Alpina','Ruf','Gumpert','Isdera','Lotec','Melkus','Artega','Borgward','Monteverdi','Rinspeed','Puch','Zbrojovka','Mikrus','FSO','Polski Fiat','Syrena','Biscuter','Pininfarina','Automobili Pininfarina','Italdesign','TechArt','Microlino','Anadol','Tofaş','Devrim','UMM','Marussia','Aspid','Arrinera','Leopard','Vencer','Jösse','Canta','Silence','NEVS','SMZ','TagAZ','Tarpan','FSM','Jawa','Malaxa','Mobilize','Vespa','Exagon','SECMA','Bolloré','Monica','DB','Ford','MTX','Rába','Neorion','AWZ','Sachsenring','Thulin','Avia','Chevron','David Brown','E.R.A.','LTI','LEVC','Dax','GTM','Grinnall','Enfield','Mini','Lightning','Vanden Plas','Nash','BMC','Princess','Chrysler Sunbeam','Hillman']
def gof(model,field):
    for p in sorted(set(PRE),key=len,reverse=True):
        if model==p or model.startswith(p+' ') or model.startswith(p+'-'): return {'Moskvich':'Moskvitch','ZIS':'ZIL','VAZ':'Lada','IZH':'Izh','Range Rover':'Land Rover','Chrysler Sunbeam':'Sunbeam','Princess':'Austin','Polski Fiat':'FSO','Syrena':'FSO','Automobili Pininfarina':'Pininfarina','Ford':'Ford France','Moskvitch':'Moskvitch'}.get(p,p)
    return field
CLN={'Daimler Company':'Daimler','Humber Limited':'Humber','Bristol Cars':'Bristol','Jensen Motors':'Jensen','Morris Motors':'Morris','Riley Motor':'Riley','Wolseley Motor Company':'Wolseley','Singer Motors':'Singer','Allard Motor Company':'Allard','Ariel Motor Company':'Ariel','Ascari Cars':'Ascari','Ginetta Cars':'Ginetta','Noble Automotive':'Noble','Marcos Engineering':'Marcos','Ruf Automobile':'Ruf','Artega Automobile':'Artega','AC Cars':'AC Cars','Ultima Sports':'Ultima','Westfield Sportscars':'Westfield','Radical Sportscars':'Radical','Sinclair Research':'Sinclair','NSU Motorenwerke':'NSU','Alvis Car and Engineering Company Ltd':'Alvis','Facel Vega':'Facel Vega','Lister Cars':'Lister','Lagonda':'Lagonda','Reliant':'Reliant','Bugatti Automobili':'Bugatti','Pagani Automobili':'Pagani','Iso Rivolta':'Iso','Automobili Turismo e Sport':'ATS','Covini Engineering':'Covini','Gordon Murray Automotive':'Gordon Murray Automotive','Ineos Automotive':'Ineos','Caterham Cars':'Caterham','Standard Motor Company':'Standard','Isdera':'Isdera','Spyker Cars':'Spyker','Talbot-Lago':'Talbot','Lightning Car Company':'Lightning','Rover Group':'Rover','SS Cars Ltd':'SS','British Leyland':'Austin','British Motor Corporation':'Austin','Caparo Vehicle Technologies':'Caparo','Enfield Automotive':'Enfield','Lotec':'Lotec','Melkus':'Melkus','Gumpert':'Gumpert','Brütsch':'Brütsch','Heinkel':'Heinkel','Hanomag':'Hanomag','Messerschmitt':'Messerschmitt','9ff':'9ff','Auto Union':'Auto Union','Benz & Cie.':'Benz','Daimler-Benz AG':'Mercedes-Benz','HWA AG':'Mercedes-Benz','Matra':'Matra','Simca':'Simca','Hispano-Suiza':'Hispano-Suiza','Ligier':'Ligier','Aixam':'Aixam','SECMA':'SECMA','ACMA':'Vespa','Mobilize':'Mobilize','Exagon Motors':'Exagon','Autobianchi':'Autobianchi','De Tomaso':'De Tomaso','Innocenti':'Innocenti','Lancia':'Lancia','Nardi':'Nardi','Piaggio':'Piaggio','Pininfarina':'Pininfarina','Vauxhall':'Vauxhall','Sunbeam':'Sunbeam','Triumph':'Triumph','TVR':'TVR','Hillman':'Hillman','Standard':'Standard','Ginetta':'Ginetta'}
ents={};order=[]
def add(mk,model,y,cls,title,src):
    k=norm(model)
    if k in exist: return
    if k in ents:
        e=ents[k]
        if not e['y'] and y: e['y']=y
        if cls and e['_c']=='' : e['_c']=cls
        return
    g=gof(model,CLN.get(mk,mk))
    ents[k]={'n':model,'mk':g,'y':y,'s':'https://en.wikipedia.org/wiki/'+(title or model).replace(' ','_'),'v':[],'g':g,'_c':cls}
def num(y): 
    y=(y or '').strip()
    return y if re.fullmatch(r'\d{4}',y) else ''
for f in ['rows_uk.txt','rows_de.txt','rows_fr.txt','rows_it.txt']:
    for l in open(W+f,encoding='utf-8'):
        p=[x.strip() for x in l.rstrip('\n').split('|')]
        if len(p)>=5: add(p[0],p[1],num(p[2]),p[3].split(',')[0],p[4],f)
for l in open(W+'rows_uk_all.txt',encoding='utf-8'):
    p=[x.strip() for x in l.rstrip('\n').split('|')]
    if len(p)>=5: add(p[0],p[1],num(p[2]),p[3].split(',')[0],p[4],'uk_all')
SKIP={'ABC','Wolseley Racing','Triumph 15/50x'}
for f in ['rows_uk2.txt','rows_de2.txt','rows_fr2.txt','rows_it2.txt','rows_oth.txt']:
    for l in open(W+f,encoding='utf-8'):
        p=l.rstrip('\n').split('|')
        mk,model=p[0],p[1]; title=p[2] if len(p)>2 and p[2] else model; y=num(p[3]) if len(p)>3 else ''
        add(mk,model,y,'',title,f)
# extra classed rows from first UK/others filtered query that were not in uk_all (e.g. ABC)
for mk,m,c,t in [('ABC Motors','ABC','sports car','ABC (1920 automobile)'),('Range Rover','Range Rover (1st generation)','off-road vehicle','Range Rover Classic')]:
    add(mk,m,'',c,t,'x')
FACT={ # marque: (cty, own, own_y, source note)  sourced from Wikidata P17/P749 fetched 2026-10-31
'Lagonda':('United Kingdom','Aston Martin Lagonda','' ),'NSU':('Germany','Volkswagen',''),'Daimler':('United Kingdom','Tata Motors Limited','2008'),'Volvo':('Sweden','Geely',''),'Polestar':('Sweden','',''),'Simca':('France','Chrysler Europe',''),'MG':('United Kingdom','SAIC Motor',''),'DAF':('Netherlands','PACCAR','1996'),'Vauxhall':('United Kingdom','Stellantis','2021'),'Panhard':('France','Arquus',''),'Facel Vega':('France','Bronzavia Industrie',''),'Singer':('United Kingdom','Rootes Group',''),'Bristol':('United Kingdom','Kamkorp',''),'Matra':('France','Lagardère Group',''),'Ginetta':('United Kingdom','',''),'Talbot':('United Kingdom','',''),'Wolseley':('United Kingdom','',''),'Riley':('United Kingdom','',''),'Morris':('United Kingdom','',''),'Delahaye':('France','',''),'Spyker':('Netherlands','',''),'Noble':('United Kingdom','',''),'Hillman':('United Kingdom','',''),'Humber':('United Kingdom','',''),'Sunbeam':('United Kingdom','',''),'Lynk & Co':("China",'',''),'Bugatti':('France','',''),'Donkervoort':('Netherlands','',''),'Horch':('Germany','',''),'Jensen':('United Kingdom','',''),'Koenigsegg':('Sweden','',''),'Lotus':('United Kingdom','',''),'TVR':('United Kingdom','',''),'Saab':('Sweden','',''),
'Smart':('Germany','Mercedes-Benz Group; Geely',''),'smart':('Germany','Mercedes-Benz Group; Geely',''),'Lada':('Russia','',''),'Alpine':('France','Renault',''),'Dacia':('Romania','Renault','1999'),'FSO':('Poland','',''),'Škoda':('Czech Republic','Volkswagen Group','1991'),'Abarth':('Italy','Stellantis','2021'),'Alfa Romeo':('Italy','Stellantis','2021'),'Fiat':('Italy','Stellantis','2021'),'Lancia':('Italy','Stellantis','2021'),'Maserati':('Italy','Stellantis','2021'),'Opel':('Germany','Stellantis','2021'),'Armstrong Siddeley':('United Kingdom','Armstrong Siddeley Development',''),'Autobianchi':('Italy','Fiat','1955'),'UAZ':('Russia','Sollers JSC',''),'GAZ':('Russia','GAZ Group',''),'DKW':('Germany','Auto Union',''),'Lamborghini':('Italy','Audi AG','1998'),'ZIL':('Russia','Government of Moscow',''),'Moskvitch':('Russia','Government of Moscow',''),'Innocenti':('Italy','British Leyland',''),'Messerschmitt':('Germany','',''),'Heinkel':('Germany','',''),'De Tomaso':('Italy','',''),'Ruf':('Germany','',''),'Reliant':('United Kingdom','',''),'Glas':('Germany','',''),'Allard':('United Kingdom','',''),'Pagani':('Italy','',''),'Morgan':('United Kingdom','',''),'Togg':('Turkey','',''),'Rimac':('Croatia','',''),'Aurus':('Russia','',''),'Zastava':('Serbia','',''),'AC Cars':('United Kingdom','',''),'Alvis':('United Kingdom','',''),'ARO':('Romania','',''),'Auto Union':('Germany','',''),'Ferrari':('Italy','','')}
GLOBAL={'Stellantis','Volkswagen','Volkswagen Group','Geely','Tata Motors Limited','SAIC Motor','Mercedes-Benz Group; Geely','Renault','Audi AG','Mercedes-Benz Group'}
bu={}
for m,(c,o,y) in FACT.items():
    d={'c':c}
    if o: d['own']=o; d['tier']='Global group' if o in GLOBAL else 'Independent'
    if y: d['own_y']=y
    bu[m]=d
# attach to entries
kinds={}
for k,e in ents.items():
    c=e.pop('_c')
    kind=KIND.get(c,NS)
    f=FACT.get(e['g'])
    if f:
        e['cty']=f[0]
        if f[1]: e['own']=f[1]; e['tier']='Global group' if f[1] in GLOBAL else 'Independent'
        if f[2]: e['own_y']=f[2]
    kinds.setdefault(kind,[]).append(e)
for k in kinds: kinds[k].sort(key=lambda e:(e['g'],e['y'] or '9999',e['n']))
reg=sorted({(m,d['c']) for m,d in bu.items()})
brands=[{'n':n,'c':c} for n,c in reg]
out={'kinds':kinds,'brands':brands,'brand_updates':bu}
json.dump(out,open('/home/user/Possession-Taxonomy/rebuild/out/G1_parts/cars_add/EUROPE.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print({k:len(v) for k,v in kinds.items()}, sum(len(v) for v in kinds.values()))
import collections
print(collections.Counter(e['g'] for v in kinds.values() for e in v).most_common(80))
