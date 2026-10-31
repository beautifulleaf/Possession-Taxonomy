import json,os
R='/home/user/Possession-Taxonomy/rebuild/'
g=json.load(open(R+'out/G2.json')); bj=json.load(open(R+'out/G2_brands.json')); B=bj['b']
have={x['n'] for x in B}
makers=[]
BR='Serviced & branded residence'
WB='https://en.wikipedia.org/wiki/Branded_residence'
STY=["Period original","Period-style new build","Contemporary"]
styledeps={'Houses','Flats & apartments','Unusual & converted properties'}
for dep in g['depts']:
  for s in dep['s']:
    for k in s['k']:
      for key in 'mr':
        for t in k.pop(key,[]) or []:
          if t[1] and t[1] not in makers: makers.append(t[1])
      if k['n']!=BR: k.pop('x',None)
      if dep['n'] in styledeps and k.get('tt') is not None:
        tt=k['tt']; done=False
        for gr in tt:
          if gr[0] in('Age','Style'): gr[0]='Period or style'; done=True
        if not done and not any(gr[0]=='Period or style' for gr in tt): tt.append(['Period or style',STY])
  if dep['n']=='Houses': dep['t']+=' Architectural style is a period-or-style attribute here; the styles themselves belong to the visual-art taxonomy.'
  if dep['n']=='Unusual & converted properties': dep['t']+=' Building style is an attribute only; styles belong to the visual-art taxonomy.'
  if dep['n']=='Flats & apartments': dep['t']+=' Building style is an attribute only; styles belong to the visual-art taxonomy.'

def ent(n,d,mk,y,g_,role=None,own=None,tier=None,cty=None,v=None,a=''):
  e={'n':n,'a':a,'d':d,'mk':mk,'y':y,'s':WB,'v':v or [],'g':g_}
  if role:e['role']=role
  if own:e['own']=own
  if tier:e['tier']=tier
  if cty:e['cty']=cty
  return e
old={}
for dep in g['depts']:
  for s in dep['s']:
    for k in s['k']:
      if k['n']==BR:
        for e in k['x']: old[e['n']]=e
        kk=k
fs=old['Four Seasons Private Residences']; am=old['Aman Residences']
fs.update(g='Hotel brands',role='origin',own='Four Seasons Hotels and Resorts',tier='Independent',cty='Canada',s=fs['s']); am.update(g='Hotel brands',own='Aman Resorts',tier='Independent',cty='Switzerland')
H='Hotel brands';F='Fashion brands';C='Car and design brands'
x=[fs,am,
 ent('Ritz-Carlton Residences','Residences sold under the Ritz-Carlton name; the brand began offering residences in 2000, starting in Washington, D.C.','Ritz-Carlton','2000',H,tier='Independent'),
 ent('Mandarin Oriental Residences','Privately owned homes sold under the Mandarin Oriental hotel name, with its services; named an early proponent of premium branding.','Mandarin Oriental','',H,tier='Independent'),
 ent('Trump International Residences','Residences sold under the Trump International hotel name; named an early proponent of premium branding.','Trump International','',H,tier='Independent'),
 ent('Fairmont Residences','Residences offered under the Fairmont hotel name.','Fairmont','',H),
 ent('St Regis Residences','Residences offered under the St Regis hotel name.','St Regis','',H),
 ent('Banyan Tree Residences','Residences offered under the Banyan Tree hotel name.','Banyan Tree','',H),
 ent('Kempinski Residences','Residences offered under the Kempinski hotel name.','Kempinski','',H),
 ent('Marriott International residences','Residences from Marriott International, named among the largest groups by number of branded schemes.','Marriott International','',H,tier='Global group'),
 ent('Accor residences','Residences from Accor, named among the largest groups by number of branded schemes.','Accor','',H,tier='Global group'),
 ent('Hilton residences','Residences from Hilton, named among the largest groups by number of branded schemes.','Hilton','',H,tier='Global group'),
 ent('Banyan Group residences','Residences from Banyan Group, named among the largest groups by number of branded schemes.','Banyan Group','',H),
 ent('Armani residences','Homes sold under a fashion house\'s name and interior design.','Armani','',F),
 ent('Elie Saab residences','Homes sold under a fashion house\'s name and interior design.','Elie Saab','',F),
 ent('Missoni residences','Homes sold under a fashion house\'s name and interior design.','Missoni','',F),
 ent('Aston Martin residences','Homes sold under a car maker\'s name.','Aston Martin','',C),
 ent('Pininfarina residences','Homes sold under a car-design house\'s name.','Pininfarina','',C),
 ent('Tonino Lamborghini residences','Homes sold under a Lamborghini family brand name.','Tonino Lamborghini','',C),
 ent('YOO residences','Homes sold under a design company\'s name rather than a hotel; Knight Frank credits YOO with pioneering branded residences not tied to a hotel.','YOO','1999','Design companies',role='origin',cty='United Kingdom',v=[]),
]
x[-1]['dt']='designer interiors · fees'
x[0]['dt']=fs.get('dt')
kk['x']=x
kk['nl']='One entry is a residence brand under which homes are sold with the brand\'s name and services; individual developments are versions.'
kk['sel']='Every brand the fetched Wikipedia article Branded residence names as a branded-residence brand (hotel, fashion, car and design brands), plus Aman, which the article does not list. The two early apartment hotels it names (Sherry-Netherland, Carlyle) are precedents, not brands, and are left out.'
kk['xg']='by brand type'
kk['s']=WB
kk.pop('m',None)
for e in x:
  if not e.get('dt'): e.pop('dt',None)
# ms
for dep in g['depts']:
  if dep['n']=='Houses':
    U='https://eyeonhousing.org/2025/07/top-ten-builder-share-rises-again-in-2024/'
    dep['ms']=[{"mkt":"US single-family home closings","who":w,"share":sh,"yr":2024,"s":U,"note":"share of new single-family closings, NAHB/BUILDER ranking"+(" (93,311 closings)" if w=="D.R. Horton" else "")} for w,sh in [("D.R. Horton","13.6 %"),("Lennar","11.7 %"),("PulteGroup","4.6 %"),("NVR","3.3 %"),("Meritage Homes","2.3 %"),("SH Residential Holdings","2.2 %"),("KB Home","2.1 %"),("Taylor Morrison","1.9 %"),("Century Communities","1.6 %"),("Toll Brothers","1.6 %")]]
    dep['ms'].append({"mkt":"UK housebuilding","who":"Persimmon","share":"10,664 homes completed","yr":2024,"s":"https://en.wikipedia.org/wiki/Persimmon_plc","note":"completions, not a share"})
    dep['msum']='The ten largest US builders closed a record 44.7 % of new single-family homes in 2024, led by D.R. Horton (NAHB). In the UK, Vistry overtook Barratt as the largest builder in September 2024; Barratt then merged with Redrow in October 2024.'
  if dep['n']=='Flats & apartments':
    S=WB
    dep['ms']=[{"mkt":"Branded residences, completed schemes worldwide","who":"All brands","share":"903 schemes","yr":2025,"s":S,"note":"Knight Frank, end of 2025; up from 354 in 2015"}]
    dep['msum']='Completed branded-residence schemes rose from 354 in 2015 to 903 at the end of 2025 (Knight Frank). Hotel brands run about 70 % of operational schemes; Dubai has the most schemes of any city. Savills found a premium of about 35 % over comparable unbranded homes in 2019.'
# brands
newb={'Trump International':'Hotel brand named as an early proponent of branded residences.','Fairmont':'Hotel brand that offers residences.','St Regis':'Hotel brand that offers residences.','Banyan Tree':'Hotel brand that offers residences.','Kempinski':'Hotel brand that offers residences.','Marriott International':'Hotel group among the largest by number of branded-residence schemes.','Accor':'Hotel group among the largest by number of branded-residence schemes.','Hilton':'Hotel group among the largest by number of branded-residence schemes.','Banyan Group':'Hotel group among the largest by number of branded-residence schemes.'}
for n,d in newb.items():
  if n not in have: B.append({'n':n,'c':'','f':'','seg':'Premium','d':d,'lines':[],'eras':[],'sig':[],'sc':['branded residences'],'rel':[],'s':WB,'kf':'branded residences'})
for n in ['Kropf Industries','Canterbury RV','Elevation Park Models','Tiny House Building Company']:
  if n not in have and n in makers: B.append({'n':n,'c':'','f':'','seg':'Mainstream','d':'Maker of park models and tiny homes listed in the earlier edition; origin not sourced.','lines':[],'eras':[],'sig':[],'sc':[],'rel':[],'s':'https://www.minimalistehouses.com/tiny-homes-on-wheels','kf':'small homes'})
print('missing makers',[m for m in makers if m not in {b['n'] for b in B}])
for f,o in(('G2',g),('G2_brands',bj)):
  t=R+f'out/{f}.json.tmp'; json.dump(o,open(t,'w'),indent=1,ensure_ascii=False); os.rename(t,R+f'out/{f}.json')
