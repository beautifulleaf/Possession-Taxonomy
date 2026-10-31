import json,os,re
from urllib.parse import urlparse
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'out/J4.json')); b=json.load(open(R+'out/J4_brands.json'))
removed={}; stats=[]
APPLE='https://en.wikipedia.org/wiki/List_of_apple_cultivars'
PEAR='https://en.wikipedia.org/wiki/List_of_pear_cultivars'
STR='https://en.wikipedia.org/wiki/List_of_strawberry_cultivars'
POT='https://en.wikipedia.org/wiki/List_of_potato_cultivars'
MAN='https://en.wikipedia.org/wiki/List_of_mango_cultivars'
def E(n,a,y,s,dd,mk=''): return {"n":n,"a":a,"d":dd,"mk":mk,"y":y,"s":s,"v":[]}
promo={
 'Apple':[E('Baldwin','','1740',APPLE,'Old American apple from Wilmington, Massachusetts; the page dates it to about 1740.'),
          E('Winesap','','1817',APPLE,'Old American apple listed from about 1817.'),
          E('Golden Russet','Bertanne','1850',APPLE,'Russet-skinned apple from New York, recorded before 1850.')],
 'Pear':[E('Seckel','','',PEAR,'Small pear from the Philadelphia area, dated to the late 17th century.')],
 'Strawberry':[E('Cambridge Favourite','','1947',STR,'University of Cambridge strawberry from Fragaria chiloensis x Blakemore.','University of Cambridge'),
  E('Earliglow','','1975',STR,'USDA strawberry bred in Maryland from MDUS 2359 x MDUS 2713.','USDA'),
  E('Tristar','','1981',STR,'Day-neutral strawberry from the Maryland station and USDA-ARS.','USDA-ARS'),
  E('Allstar','','1981',STR,'USDA and University of Maryland strawberry from US 4419 x MDVS 3184.','USDA'),
  E('Jewel','','1985',STR,'Cornell strawberry from (Senga Sengana x NYE58) x Holiday.','Cornell University'),
  E('Strawberry Festival','','2000',STR,'Florida station strawberry from Rosa Linda x Oso Grande.','University of Florida'),
  E('Flamenco','','2002',STR,'East Malling strawberry from Evita x EMR77.','East Malling Research'),
  E('Darselect','','1998',STR,'French strawberry from Parker x Elsanta.','Société Civile Darbonne'),
  E('Portola','','2009',STR,'University of California strawberry from Cal 97.93-7 x Cal 97.209-1.','University of California')],
 'Mango':[E('Totapuri','','',MAN,'Indian mango listed on the page of mango cultivars.'),
  E('Amrapali','','',MAN,'Indian mango noted for taste and a strong aroma in its leaves.'),
  E('Badami','','',MAN,'Karnataka mango called the Alphonso of Karnataka.'),
  E('Palmer','','',MAN,'Mango grown in Australia, Brazil and the United States.')],
}
over={'Truffle':'a truffle species or regional truffle','Wild shoots & fiddleheads':'a wild shoot or fiddlehead species','Porcini':'a protected regional porcini product','Fresh wasabi':'a wasabi cultivar or regional product','Chilli':'a chilli cultivar or pod type','Pumpkin & winter squash':'a squash cultivar or fruit type'}
fetched={
 'Apple':(APPLE,'about 7,500 known cultivars; no complete list is practical'),
 'Pear':(PEAR,'about 155 table rows of over 3,000 known cultivars'),
 'Strawberry':(STR,'about 156 table rows'),
 'Potato':(POT,'cultivars of the table-potato trade'),
 'Mango':(MAN,'about 185 table rows plus national lists'),
}
club={'Cripps Pink':dict(own='Department of Primary Industries and Regional Development (Western Australia)',tier='Independent',cty='Australia',own_y='',role=None,
   note='Bred 1973 by John Cripps from Lady Williams x Golden Delicious. The Pink Lady trade mark is managed by Apple and Pear Australia Limited (APAL); in the US and Mexico by Pink Lady America.'),
 'Jazz':dict(own='',tier='Independent',cty='New Zealand',own_y=''),
 'SweeTango':dict(own='University of Minnesota',tier='Independent',cty='United States',own_y=''),
 'Cosmic Crisp':dict(own='Washington State University',tier='Independent',cty='United States',own_y=''),
 'Kanzi':dict(own='',tier='Independent',cty='Belgium',own_y='')}
CERT=' Organic and fair-trade certifications are tags on a product, not kinds.'
for dp in d['depts']:
  if dp['n']!='Fruit gifts' and CERT not in dp['t']: dp['t']=dp['t'].rstrip()+CERT
  for s in dp['s']:
    for k in s['k']:
      n=k['n']; m=k.pop('m',[]); r=k.pop('r',[])
      xs=k.get('x') or []
      have={x['n'].lower() for x in xs}
      pm=[e for e in promo.get(n,[]) if e['n'].lower() not in have]
      if pm: xs+=pm; k['x']=xs
      pn={e['n'].lower() for e in promo.get(n,[])}
      rem=[t for t in m if t[0].lower() not in pn]
      if rem or r: removed[n]={'m':rem,'r':r}
      if xs:
        low=n.lower()
        what=over.get(n,f'a named {low} cultivar, club variety or protected regional product')
        k['nl']=f"One entry is {what}; sports, clones and regional names are aliases or versions."
        if n in fetched:
          u,sc=fetched[n]
          k['sel']=f"Follows the cultivars named by Wikipedia's list at {u} ({sc}), cut to cultivars with a trade or collector role; entries added from it carry origin and year as the page states. Pages cited on each entry supply the rest. Not claimed complete."
        else:
          hosts=[]
          for x in xs:
            h=urlparse(x['s']).netloc
            if h and h not in hosts: hosts.append(h)
          k['sel']=f"No whole-space reference for {low} cultivars was fetched. The list follows the cultivars named by the page cited on each entry ({', '.join(hosts[:3])}), cut to cultivars with a trade or collector role. Not claimed complete."
        stats.append((n,len(xs)-len(pm),len(xs),len(rem)))
        for x in xs:
          if x['n'] in club and n=='Apple':
            c=club[x['n']]
            for f in('own','tier','cty','own_y'):
              if c.get(f) is not None: x[f]=c[f]
            if c.get('note'): x['d']=x['d'].rstrip('.')+'. '+c['note']
      else:
        stats.append((n,0,0,len(m)))
# market panel
tr=[d_ for d_ in d['depts'] if d_['n']=='Tropical & subtropical fruit'][0]
WB='https://en.wikipedia.org/wiki/Banana_industry'; FAO='https://www.fao.org/newsroom/detail/The-changing-face-of-global-banana-trade/en'
tr['ms']=[
 {"mkt":"World banana exports","who":"Chiquita, Dole and Del Monte together","share":"36.6 %","yr":2013,"s":FAO,"note":"share of global exports; 65.3 % in the 1980s"},
 {"mkt":"World banana exports","who":"Top five companies","share":"44.4 %","yr":2013,"s":FAO,"note":"share of global exports; 70 % in 2002"},
 {"mkt":"International banana trade","who":"Chiquita","share":"13 %","yr":2025,"s":WB,"note":"Bananalink figure as tabled on the page"},
 {"mkt":"International banana trade","who":"Del Monte","share":"12 %","yr":2025,"s":WB,"note":"Bananalink figure as tabled on the page"},
 {"mkt":"International banana trade","who":"Dole plc","share":"11 %","yr":2025,"s":WB,"note":"Bananalink figure as tabled on the page"},
 {"mkt":"International banana trade","who":"Fyffes","share":"6 %","yr":2025,"s":WB,"note":"Bananalink figure as tabled on the page"}]
tr['msum']="Four multinationals held 42 % of the international banana trade in 2025 and the top three about 37 % in 2013; the page figures come from different sources and methods."
tp=[d_ for d_ in d['depts'] if d_['n']=='Temperate fruit'][0]
tp['ms']=[{"mkt":"UK apples","who":"Pink Lady","share":"third by value","yr":2012,"s":"https://en.wikipedia.org/wiki/Cripps_Pink","note":"the brand replaced Granny Smith in third place; no other figure given"}]
tp['msum']="The Pink Lady brand ranked third by value among apples in the UK in 2012. No further shares were found on fetched pages."
# brands
def reg(n,c=None,f=None,dd=None,s=None):
  e=[x for x in b['b'] if x['n']==n]
  if e: e=e[0]
  else: e={"n":n,"c":"","f":"","seg":"Specialist","kf":"","d":"","s":""}; b['b'].append(e)
  if c: e['c']=c
  if f: e['f']=f
  if dd: e['d']=dd
  if s: e['s']=s
reg('Dole','Ireland','1851','Fruit and vegetable group tracing to Castle & Cooke (1851); Dole plc formed in 2021 from Dole Food Company and Total Produce.','https://en.wikipedia.org/wiki/Dole_plc')
reg('Chiquita','Switzerland','1870','Banana brand tracing to 1870; owned since 2014 by Cutrale and Safra Group.','https://en.wikipedia.org/wiki/Chiquita')
reg('Zespri','New Zealand',None,'Grower co-operative marketing New Zealand kiwifruit (Green, Organic, SunGold); the page gives both 1988 and 1997 as origin.','https://en.wikipedia.org/wiki/Zespri')
reg('Fresh Del Monte Produce',None,None,'Revenue US$4.32 billion in 2023; holds the global rights to the Del Monte brand.','https://en.wikipedia.org/wiki/Fresh_Del_Monte_Produce')
reg('Apple and Pear Australia Limited','Australia',None,'Owns and manages the Pink Lady trade marks, registered in over 80 territories.','https://en.wikipedia.org/wiki/Cripps_Pink')
reg('Pepin Heights Orchards','United States',None,'Minnesota orchard with exclusive marketing rights to SweeTango; formed the Next Big Thing grower co-operative.','https://en.wikipedia.org/wiki/SweeTango')
reg('Washington State University','United States',None,'Owns the Cosmic Crisp patent; growing is limited to Washington State under an agreement to March 2027.','https://en.wikipedia.org/wiki/Cosmic_Crisp')
reg('Department of Primary Industries and Regional Development (Western Australia)','Australia',None,'Owns and licenses the Cripps Pink cultivar and holds plant breeders\' rights.','https://en.wikipedia.org/wiki/Cripps_Pink')
reg('Fyffes','Ireland','1888',None,None)
def dump(o,p):
  json.dump(o,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.rename(p+'.tmp',p)
dump(d,R+'out/J4.json'); dump(b,R+'out/J4_brands.json'); dump(removed,R+'work/V4_J4/removed_m.json')
dump(stats,R+'work/V4_J4/stats.json')
print(sum(len(v['m']) for v in removed.values()),'m removed; kinds',len(removed))
