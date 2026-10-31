import json,re,os,copy
P='/home/user/Possession-Taxonomy/rebuild/out/H1.json'
d=json.load(open(P))
W='https://en.wikipedia.org/wiki/'
# name -> (own, tier, own_y, src, extra)
O={
 'Neutrogena':('Kenvue','Global group','',W+'Kenvue',{'cty':'United States','y':'1930'}),
 'Cetaphil':('Galderma','Independent','',W+'Galderma',{}),
 "Burt's Bees":('The Clorox Company','Global group','2007',W+'The_Clorox_Company',{}),
 'Elizabeth Arden':('Revlon','Independent','2016',W+'Revlon',{}),
 'The Body Shop':('Auréa Group','Independent','2024',W+'The_Body_Shop',{'cty':'United Kingdom','y':'1976'}),
 'Elemis':("Groupe L'Occitane",'Independent','',W+"L%27Occitane_en_Provence",{}),
 'Melvita':("Groupe L'Occitane",'Independent','',W+"L%27Occitane_en_Provence",{}),
 'Aveda':('The Estée Lauder Companies','Global group','1997',W+'Est%C3%A9e_Lauder_Companies',{}),
 'Bumble and bumble':('The Estée Lauder Companies','Global group','2006',W+'Est%C3%A9e_Lauder_Companies',{}),
 'Veet':('Reckitt','Global group','',W+'Reckitt',{}),
 'Mitchum':('Revlon','Independent','1970',W+'Revlon',{}),
 'Flex':('Revlon','Independent','',W+'Revlon',{}),
 'Clairol':('Wella Company','Independent','2020',W+'Coty,_Inc.',{}),
 'Wella':('Wella Company','Independent','2020',W+'Wella',{}),
 'Wella Professionals':('Wella Company','Independent','2020',W+'Wella',{}),
 'ghd':('Wella Company','Independent','2020',W+'Coty,_Inc.',{}),
 'Dollar Shave Club':('Nexus Capital Management','Independent','2023',W+'Dollar_Shave_Club',{}),
 'Degree':('Unilever','Global group','1996',W+'Unilever',{}),
 'Kotex':('Kimberly-Clark','Global group','',W+'Kimberly-Clark',{}),
 'Olaplex':('Henkel','Global group','2026',W+'Olaplex',{}),
 'Moroccanoil':('Carmen and Ofer Tal','Independent','2008',W+'Moroccanoil',{'cty':'Israel','y':'2003'}),
 'Weleda':('Weleda AG','Independent','',W+'Weleda',{'cty':'Switzerland','y':'1921'}),
 'ColourPop Cosmetics':('Seed Beauty','Independent','',W+'ColourPop_Cosmetics',{'y':'2014'}),
 'Anastasia Beverly Hills':('Anastasia Soare','Independent','',W+'Anastasia_Beverly_Hills',{'y':'1997'}),
 'Laura Mercier':('Advent International','Independent','2021',W+'Shiseido',{}),
 'Glossier':('Glossier','Independent','',W+'Glossier',{'y':'2014'}),
}
NC={ 'Ziaja':('Ziaja Ltd Zakład Produkcji Leków','2nd of 20 Polish cosmetics companies by 2023 revenue (PLN 460 million, Forbes Polska).'),
     'Bielenda':('Bielenda Group','5th of 20 Polish cosmetics companies by 2023 revenue (PLN 294 million, Forbes Polska).')}
FB='https://www.forbes.pl/rankingi/ranking-firm-kosmetycznych-piekny-biznes-z-pieknymi-zyskami-liczby-robia-wrazenie/whvzc6w'
NEW={'Skincare':[('Eveline Cosmetics','Eveline Cosmetics','1st of 20 Polish cosmetics companies by 2023 revenue (PLN 645 million, Forbes Polska).',''),
                ('Dr Irena Eris','Dr Irena Eris','6th of 20 Polish cosmetics companies by 2023 revenue (PLN 301 million, Forbes Polska).','')],
     'Make-up':[('Inglot','Inglot','15th of 20 Polish cosmetics companies by 2023 revenue (PLN 142 million, Forbes Polska); founded 1983.','1983')]}
SRCFIX={'Ziaja':FB,'Bielenda':FB}
changed=[];added=[]
def gname(dept,own,tier):
    skin=dept in('Skincare','Make-up')
    if tier=='Global group':
        short={'The Clorox Company':'The Clorox Company'}.get(own,own)
        return short if skin else 'Global group: '+short
    if tier=='Independent': return 'Independents' if skin else 'Independents and national champions'
    if tier=='National champion': return 'National champions' if skin else 'Independents and national champions'
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      x=k.get('x') or []
      if len(x)<=20: continue
      for e in x:
        n=e['n']
        if n in O and not e.get('own'):
          own,tier,oy,src,ex=O[n]
          e['own']=own;e['tier']=tier
          if oy: e['own_y']=oy
          for a,b in ex.items():
            if not e.get(a): e[a]=b
          e['g']=gname(dp['n'],own,tier)
          e['d']=(e.get('d','').rstrip('.')+'. Owner per '+src).strip() if 'Owner per' not in e.get('d','') else e['d']
          e['d']=e['d'].replace('Owner per '+src, 'Owner stated on '+src.split('/wiki/')[1].replace('_',' ')+' (Wikipedia)')
          changed.append((dp['n'],n,own))
        elif n in NC and not e.get('own'):
          own,dd=NC[n]; e['own']=own;e['tier']='National champion';e['g']='National champions' if dp['n'] in('Skincare','Make-up') else 'Independents and national champions'
          e['d']=dd;e['s']=FB;changed.append((dp['n'],n,own))
      for nm,own,dd,yy in NEW.get(dp['n'],[]):
        if not any(e['n'].lower()==nm.lower() for e in x):
          x.append({'n':nm,'a':'','d':dd,'y':yy,'s':FB,'v':[],'own':own,'tier':'National champion','cty':'Poland','g':'National champions'}); added.append((dp['n'],nm))
      # coverage line
      sel=k.get('sel','')
      sel=re.sub(r'Covers (\d+) brands; no whole-market list exists, so the total is unknown\.',lambda m:'No complete list exists; follows the group brand pages and market overviews cited per entry.',sel)
      if 'Owner pass 2026-10-31' not in sel:
        sel=sel.rstrip()+' Owner pass 2026-10-31: owners added from the Wikipedia pages of Kenvue, Galderma, Revlon, Coty, Church & Dwight, Henkel, Kao, Reckitt, Edgewell, Estée Lauder, Shiseido, Unilever, Beiersdorf, the Clorox Company, L\'Occitane and Wella; Unilever and Henkel brand lists are partial, so those portfolios are not confirmed complete.'
      k['sel']=sel
# other kinds' coverage line
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      if k.get('x') and len(k['x'])<=20:
        k['sel']=re.sub(r'Covers (\d+) entries; no reference lists every maker, so the kind is not complete\.','No complete list exists; follows the maker pages and Wikipedia overviews cited in each entry ('+r'\1'+' entries).',k.get('sel',''))
# ms
def addms(dept,rows):
  for dp in d['depts']:
    if dp['n']==dept:
      for r in rows:
        if r not in dp['ms']: dp['ms'].append(r)
PL=[('Eveline Cosmetics',645),('Ziaja',460),('Dr. Miele Cosmed Group',444),('Cosmo Group',379),('Dr Irena Eris',301),('Bielenda Group',294),('La Rive',280),('Oceanic',250),('Wibo',228),('Dramers',225)]
rows=[{'mkt':'Polish cosmetics companies by revenue, 2023','who':w,'share':f'PLN {v} million','yr':2023,'s':FB,'note':f'rank {i+1} of 20 in the Forbes Polska list as printed; whole cosmetics business, not skin care alone'} for i,(w,v) in enumerate(PL)]
rows.append({'mkt':'Japan skin care, leading companies','who':'KOSE, Shiseido, Kao','share':'top three; no share stated','yr':2019,'s':'https://www.globaldata.com/japans-skincare-sector-is-forecast-to-reach-us22-2bn-by-2024-says-globaldata/','note':'GlobalData; leading skin-care brands by value in 2019 were Moisture Mild, Sekkisei and Hyalocharge'})
rows.append({'mkt':'Japan cosmetics market rank','who':'Japan','share':'third-largest cosmetics market in the world','yr':2024,'s':'https://www.gtai.de/de/trade/japan/branchen/japans-kosmetikmarkt-setzt-erholung-fort-1886728','note':'GTAI citing Statista; skin care is by far the largest segment; suppliers named: Shiseido, Kao, Kosé, P&G, Pola Orbis, Fine Today, Unilever, L\'Oréal, Mandom, Fancl, no ranking given'})
addms('Skincare',rows)
json.dump(d,open('H1.new.json','w'),ensure_ascii=False,indent=None)
json.dump({'changed':changed,'added':added},open('applied.json','w'),ensure_ascii=False)
print(len(changed),added)
