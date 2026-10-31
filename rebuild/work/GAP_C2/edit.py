import json,os,re
P='rebuild/out/C2.json'; B='rebuild/out/C2_brands.json'
d=json.load(open(P)); b=json.load(open(B))
K={}
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']: K[k['n']]=k
def ent(kn,n): return next(e for e in K[kn]['x'] if e['n']==n)
W='https://en.wikipedia.org/wiki/'
e=ent('Rotary mower','Victa rotary mower'); e['own']='Roy Gripske & Sons'; e['own_y']='2025'
e=ent('Gas grill','Napoleon Prestige'); e['own']='Wolf Steel Ltd. (Schroeter family)'; e['s']=W+'Napoleon_(company)' if False else e['s']
e=ent('Flat-top griddle','Blackstone griddle'); e['own']='Weber Blackstone'; e['own_y']='2025'
for kn in K:
  for e in K[kn].get('x',[]) or []:
    if e.get('mk')=='Weber': e['own']='Weber Blackstone'; e['own_y']='2025'
e=ent('Pellet grill','Recteq Bullseye Deluxe'); e['own']='Norwest Equity Partners'; e['own_y']='2021'
e=ent('Robotic mower','Mammotion LUBA'); e['y']='2022'
R='https://en.wikipedia.org/wiki/Robotic_lawn_mower'
K['Robotic mower']['x']+=[
 {"n":"FireFly Automatix AMP","d":"Electric autonomous reel mower line for sports turf, named on Wikipedia's robotic mower page.","mk":"FireFly Automatix","y":"2023","s":R,"v":[],"tier":"Independent"},
 {"n":"AM Robots Storm","d":"Robotic mower named on Wikipedia's robotic mower page.","mk":"AM Robots","y":"2024","s":R,"v":[],"tier":"Independent"},
 {"n":"HOOKII robotic mower","d":"Robotic mower brand named on Wikipedia's robotic mower page.","mk":"HOOKII","y":"","s":R,"v":[],"tier":"Independent"}]
K['Cylinder mower']['x'].append({"n":"Archimedean reel mower","d":"First United States reel mower patent, granted to Amariah Hills in 1868; his company followed in 1871.","mk":"Archimedean Lawn Mower Co.","y":"1868","cty":"United States","s":W+'Lawn_mower',"v":[]})
K['Rotary mower']['x'].append({"n":"Kut Kwick out-front rotary mower","d":"Described on Wikipedia as the first out-front rotary mower, converted from a pulp saw.","mk":"Kut Kwick","y":"","s":W+'Lawn_mower',"v":[]})
def cov(kn,t):
  k=K[kn]; s=k['sel']; i=s.rfind('Covers')
  j=s.rfind('Complete')
  i=max(i,j)
  if i>=0: s=s[:i].rstrip()
  s=s.rstrip('; ').rstrip()
  if s and not s.endswith('.'): s+='.'
  k['sel']=(s+' '+t).strip()
n=lambda kn:len(K[kn]['x'])
cov('Rotary mower',f"Covers {n('Rotary mower')} of about 5 lines named on Wikipedia's Lawn mower page (Victa, Kut Kwick, Honda, Hayter); other rotary makers sit under Powered garden equipment brand, as their lines are not named on any page read.")
cov('Cylinder mower',f"Complete: {n('Cylinder mower')} of {n('Cylinder mower')} cylinder or reel lines named on Wikipedia's Lawn mower page; modern Allett ranges are held in the brand register.")
cov('Riding mower',"Complete: 1 of 1 riding lines named on Wikipedia's Lawn mower page (Ideal Triplex); Deere and Toro ride-on ranges appear as brands only because the page names no model.")
cov('Robotic mower',f"Complete: 10 of 10 robotic lines named on Wikipedia's Robotic lawn mower page (now {n('Robotic mower')} entries with Mammotion LUBA and Segway Navimow from other fetched pages).")
cov('Powered garden equipment brand',f"Covers {n('Powered garden equipment brand')} brands of the owner groups named on the Report Prime 2024 ranking and Wikipedia group pages; Bosch, Ryobi and Einhell sit in the brand register because no fetched page lists their brands.")
for kn,ref in [('Kamado grill','Wikipedia Kamado and maker pages'),('Offset smoker','maker pages'),('Gas grill','Weber history pages and a Consumer Reports page'),('Pellet grill','Wikipedia Pellet grill (Traeger, Louisiana Grills, Pit Boss; Firecraft and Camp Chef appear there only as a file name and a reference title) and maker pages'),('Flat-top griddle','the Blackstone maker page'),('Portable grill','Wikipedia Barbecue grill and Weber history pages'),('Pizza oven','Wikipedia Ooni (company) and maker pages; Wikipedia Pizza oven names only commercial ovens')]:
  cov(kn,f"No complete list exists; follows {ref}. {n(kn)} lines.")
json.dump(d,open(P+'.tmp','w'),indent=1,ensure_ascii=False); os.replace(P+'.tmp',P)
bb={x['n']:x for x in b['b']}
bb['Recteq']['f']='2009'; bb['Recteq']['c']='United States'; bb['Recteq']['d']+=' Owned by Norwest Equity Partners since 2021.'
bb['Honda']['f']='1946'
bb['Victa']['d']+=' Owned by Roy Gripske & Sons since 2025.'
bb['Napoleon']['d']=bb['Napoleon']['d']
for nm,c,f,s in [('FireFly Automatix','',"",R),('AM Robots','','',R),('HOOKII','','',R),('Kut Kwick','','',W+'Lawn_mower'),('Archimedean Lawn Mower Co.','United States','1871',W+'Lawn_mower')]:
  if nm not in bb: b['b'].append({"n":nm,"c":c,"f":f,"seg":"Mainstream","d":"Mower maker named on a fetched Wikipedia page.","lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":s,"kf":"mowers"})
json.dump(b,open(B+'.tmp','w'),indent=1,ensure_ascii=False); os.replace(B+'.tmp',B)
