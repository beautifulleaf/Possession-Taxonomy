import json,os,re,copy
O='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(O+'J2.json'))
kinds={}
for dep in d['depts']:
    for s in dep['s']:
        for k in s['k']: kinds[k['n']]=k
G='Protected and regional names'
CAL='https://www.regione.calabria.it/wp-content/uploads/2023/06/DOP__IGP_e_STG_Registrati_agg_23.03.23.pdf'
def ent(n,d_,y,s,mk='',a='',dt=''):
    e={"n":n,"a":a,"d":d_,"mk":mk,"y":y,"s":s,"v":[],"g":G}
    if dt:e['dt']=dt
    return e
new={
 'Trout & char':[
  ent('Salmerino del Trentino IGP','Alpine char from Trentino and Brescia, Italy; one of the six Italian fish and mollusc names in the national DOP and IGP register.','',CAL,dt='IGP · Trento and Brescia'),
  ent('Schwarzwaldforelle PGI','Trout name from the Black Forest, Germany, entered in the EU register of protected geographical indications.','','https://www.wipo.int/wipolex/en/text/473857')],
 'Carp':[ent('Tinca Gobba Dorata del Pianalto di Poirino PDO','Golden tench from the Poirino plateau in Piedmont, Italy; EU PDO under Regulation 160/2008 of 21 February 2008.','2008',CAL,dt='PDO · Torino, Asti and Cuneo')],
 'Lamprey':[ent('Carnikavas nēģi PGI','Lamprey from Carnikava, Latvia; entered in the EU register as a PGI by Regulation 2015/269 of 13 February 2015.','2015','https://www.legislation.gov.uk/eur/2015/269/data.html',dt='PGI · Latvia')],
 'Whitefish & vendace':[ent('Kitkan viisas PDO','Finnish fish name entered in the EU register as a PDO in March 2013; the regulation gives no species.','2013','https://lexaris.de/library/tableofcontents/2117258',dt='PDO · Finland')],
 'Smoked haddock':[ent('Traditional Grimsby Smoked Fish PGI','Smoked fish of Grimsby, England; EU PGI from 22 October 2009, carried into the UK scheme on 31 December 2020.','2009','https://www.Gov.uk/protected-food-drink-names/traditional-grimsby-smoked-fish',dt='PGI · Grimsby')],
 'Crayfish':[ent('Yancheng Long Xia PGI (盐城龙虾)','Chinese name entered in the EU register as a PGI by Regulation 743/2012 of 9 August 2012.','2012','https://www.lexaris.de/library/tableofcontents/2117416',dt='PGI · China')],
 'Native flat oyster':[ent('Whitstable Oysters PGI','Oysters from beds near Whitstable, Kent; the specification names native Ostrea edulis and cultivated Crassostrea gigas.','',
   'https://assets.publishing.service.gov.uk/media/5fd369628fa8f54d6249ea1c/pfn-whitstable-oysters.pdf',dt='PGI · native and cultivated')],
 'Atlantic salmon':[ent('Scottish Wild Salmon PGI','Wild Salmo salar caught in Scottish rivers and up to 1,500 metres off the coast, sold fresh, whole and boxed in ice.','',
   'https://assets.publishing.service.gov.uk/media/5fd366978fa8f54d6249ea19/pfn-scottish-wild-salmon-pgi.pdf',dt='PGI · wild, in-river and coastal fisheries')],
 'Eel':[ent('Lough Neagh Eel PGI','Eel from Lough Neagh, Northern Ireland; awarded EU PGI status in October 2011.','2011','https://www.afbini.gov.uk/node/1028',dt='PGI · wild lough fishery')],
}
added=[]
for kn,es in new.items():
    k=kinds[kn]
    if 'x' not in k:
        k['x']=[]
        k['nl']="One entry is a named regional product, protected name or variety of this kind; a maker's version of it is a version."
        k['xg']='by registration or origin'
        k['sel']='No whole-space reference exists for this kind; the list follows the pages cited on its entries.'
    for e in es:
        if e['n'].lower() not in [x['n'].lower() for x in k['x']]:
            k['x'].append(e); added.append((kn,e['n']))
# owners
NOM='https://en.wikipedia.org/wiki/Nomad_Foods'
for e in kinds['Fish fingers']['x']:
    if e['n'] in('Findus','Birds Eye fish fingers'):
        e['own']='Nomad Foods'; e['tier']='Independent'; e['own_y']=2015; e['g']='Independent: Nomad Foods'
        if e['n']=='Findus': e['d']='Swedish frozen food brand sold in the UK from 1958; Nomad Foods bought the continental European Findus business in 2015.'
        else: e['d']='Commercialised in 1953 under the Birds Eye label by General Foods; the UK name came from a poll of workers. Nomad Foods owns Birds Eye in Europe since 2015.'
for kn,k in kinds.items():
    for e in k.get('x',[]):
        if e['n']=='Ramón Peña':
            e['own']='Conservas Ramón Peña (family company)'; e['tier']='Independent'; e['g']='Independent: Conservas Ramón Peña'
            e['d']='Cambados-founded family cannery (1920, José Peña Oubiña), now at Ribadumia and led by the third generation; carries the Pesca de Rías seal.'
# coverage lines
for kn,k in kinds.items():
    if 'x' not in k or not k['x']: continue
    n=len(k['x']); p=sum(1 for e in k['x'] if e.get('g','').startswith('Protected'))
    base=re.split(r' Covers \d+ named entries;',k['sel'])[0]
    base=re.sub(r'Protected names follow the harvest from EU, MAFF and Korean registers; the EU eAmbrosia register could not be read as a list this pass\.','Protected names follow the EU, MAFF and Korean registers as harvested, plus EU names added from regulation texts and the Italian national register.',base)
    if 'Nomad Foods' in json.dumps(k['x']) and 'Nomad' not in base: base+=' Nomad Foods ownership from the fetched Wikipedia page on Nomad Foods.'
    if p:
        tail=f" Covers {p} protected names in this kind; the EU registers about 51 fish and mollusc names across all kinds (Qualivita count, via Dissapore), but the register itself is JavaScript-only and Wikidata models none of it, so the rest are not itemised."
        if n>p: tail+=f" The other {n-p} entries are brands and makers: no complete list exists; they follow the pages cited."
    else:
        tail=" No complete list exists; follows the brand and maker pages cited on its entries."
    k['sel']=base+tail
# market facts
dp={x['n']:x for x in d['depts']}
dp['Fish cakes, fingers & surimi']['ms']=dp['Fish cakes, fingers & surimi'].get('ms',[])+[{"mkt":"Western Europe savoury frozen food","who":"Nomad Foods (Birds Eye, Findus, Iglo)","share":"about 15 %","yr":2025,"s":NOM,"note":"estimated share of a EUR 26.3 billion market, more than double the nearest rival; the Wikipedia page carries a conflict-of-interest notice, so the figure is the company's"}]
json.dump(d,open(O+'J2.json.tmp','w'),ensure_ascii=False,indent=1); os.replace(O+'J2.json.tmp',O+'J2.json')
b=json.load(open(O+'J2_brands.json'))
names={x['n'] for x in b['b']}
for x in b['b']:
    if x['n']=='Birds Eye': x['d']='Frozen food brand that commercialised fish fingers under General Foods in 1953; owned by Nomad Foods in Europe since 2015.'
    if x['n']=='José Gourmet': x['d']='Canned-fish brand of 100 Mistérios (Perafita, Porto), established 2008 to revive Portuguese canned fish.'
def br(n,c,f,seg,kf,dd,s): return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":dd,"lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":s}
for nb in [br('Nomad Foods','','','Mainstream','frozen food','Frozen food group that bought Iglo Group (with Birds Eye) in 2015 and the continental Findus business later that year.',NOM),
           br('100 Mistérios','Portugal','2008','Premium','Portuguese conservas','Portuguese company that owns the José Gourmet canned-fish brand.','https://www.gourmets.net/salon-gourmets/2024/exhibitors-catalogue/jose-gourmet-by-100-misterios')]:
    if nb['n'] not in names: b['b'].append(nb)
json.dump(b,open(O+'J2_brands.json.tmp','w'),ensure_ascii=False,indent=1); os.replace(O+'J2_brands.json.tmp',O+'J2_brands.json')
print(added)
