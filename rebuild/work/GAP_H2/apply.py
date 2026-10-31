import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(P+'H2.json'))
cov={
'Collector cane':"Complete: 14 of 14 in-scope named types in Wikipedia's Walking stick article and the Swordstick article; shooting stick, alpenstock, pike staff and scout staff are tools and left out.",
'Manual wheelchair':"No complete list exists; follows Wikipedia's Wheelchair article (both windows read), the Marilyn Hamilton, Rainer Küschall and TiLite articles and two MoMA pages. Carbon Black (2011) is named but is neither an origin nor a design-collection item.",
'Hearing aid':"No complete list exists; follows Wikipedia's Hearing aid article (first 100,000 characters read). Only the origin is kept; Vactuphone and other models are not collection or award items.",
'Braille device':"No complete list exists; follows Wikipedia's Perkins Brailler article. Other braille devices are commodity products.",
}
own={'Quickie':('Sunrise Medical','1986',''),'Küschall Competition':('Invacare','1995','Switzerland'),
'TiLite titanium rigid chair':('Permobil','2014','United States'),'Everest & Jennings folding chair':('Graham-Field Health Products','1996','United States')}
srcs={'Quickie':'https://www.sunrisemedical-group.com/about/heritage','Küschall Competition':'https://en.wikipedia.org/wiki/K%C3%BCschall','TiLite titanium rigid chair':'https://en.wikipedia.org/wiki/TiLite','Everest & Jennings folding chair':'https://en.wikipedia.org/wiki/Everest_%26_Jennings'}
def walk(o):
  if isinstance(o,dict):
    if 'x' in o and o.get('n') in cov:
      s=o.get('sel','')
      if 'Complete:' not in s and 'No complete list' not in s[:40]:
        o['sel']=(s.rstrip('. ')+'. '+cov[o['n']]) if o['n']!='Collector cane' else s.rstrip()+' '+cov[o['n']]
      elif o['n']!='Collector cane': o['sel']=s.rstrip()+' '+cov[o['n']].split('; ',1)[-1] if False else s.rstrip()+' Coverage: '+cov[o['n']]
      for e in o['x']:
        if e['n'] in own:
          e['own'],e['own_y'],c=own[e['n']]
          if c: e['cty']=c
    for v in o.values(): walk(v)
  elif isinstance(o,list):
    for v in o: walk(v)
walk(d)
for dp in d['depts']:
  if dp['n']=='Medicines & remedies':
    H='https://www.sec.gov/Archives/edgar/data/1900304/000155837025003368/hln-20241231x20f.htm'
    dp['ms']=[{'mkt':m,'who':'Haleon','share':sh,'yr':2023,'s':H,'note':n} for m,sh,n in [
     ('Global pain relief','13 %','market leader; top five players about 35 %, Haleon own analysis'),
     ('Global respiratory health','5.6 %','joint leader; top five players 26 %'),
     ('Global digestive health','3.8 %','top five players about 23 %'),
     ('Global oral health','about 11 %','third largest player; top five over 60 %')]]
    dp['msum']="Haleon states shares for four non-prescription categories in 2023: 13 % of pain relief (leader), 5.6 % of respiratory (joint leader), 3.8 % of digestive and about 11 % of oral health. Johnson & Johnson (now Kenvue) and Bayer were long ranked first and second by Kline, but no current ranking was fetched."
  if dp['n']=='Hearing':
    dp['msum']=dp['msum'].rstrip()+" Wikipedia's Sonova article gives Sonova an estimated 24 % in 2013; no current share by maker was found."
json.dump(d,open(P+'H2.json.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'H2.json.tmp',P+'H2.json')
b=json.load(open(P+'H2_brands.json'))
L=b['b']; idx={x['n']:x for x in L}
upd={'Sonova':('Switzerland','1947','https://en.wikipedia.org/wiki/Sonova'),'Demant':('Denmark','1904','https://en.wikipedia.org/wiki/Demant'),
'GN Store Nord':('Denmark','1869','https://en.wikipedia.org/wiki/GN_Store_Nord'),'Haleon':('United Kingdom','2022','https://en.wikipedia.org/wiki/Haleon'),
'Sunrise Medical':('Germany','1983','https://www.sunrisemedical.eu/company-information/company-overview')}
for n,(c,f,s) in upd.items():
  x=idx[n]; x['c']=c; x['f']=f
  if n=='Sunrise Medical': x['c']=c
for n,(c,f,s,d_) in {'WS Audiology':('Denmark','2019','https://en.wikipedia.org/wiki/WS_Audiology','Hearing-aid group formed in 2019 by the merger of Sivantos and Widex.'),
 'Kenvue':('United States','2022','https://en.wikipedia.org/wiki/Kenvue','Consumer health company spun off from Johnson & Johnson in 2023.'),
 'Permobil':('Sweden','','https://en.wikipedia.org/wiki/TiLite','Swedish maker of power wheelchairs and seating systems; owns TiLite since 2014.'),
 'Invacare':('','','https://en.wikipedia.org/wiki/K%C3%BCschall','Owner group of Küschall since 1995.'),
 'Graham-Field Health Products':('United States','','https://en.wikipedia.org/wiki/Everest_%26_Jennings','Bought Everest & Jennings in 1996.')}.items():
  if n not in idx: L.append({'n':n,'c':c,'f':f,'seg':'Professional & flagship','lines':[],'sig':[],'s':s,'kf':'owner group','d':d_,'eras':[],'sc':[],'rel':[]})
json.dump(b,open(P+'H2_brands.json.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'H2_brands.json.tmp',P+'H2_brands.json')
