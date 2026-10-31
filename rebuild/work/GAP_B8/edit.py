import json,os
R='/home/user/Possession-Taxonomy/rebuild/'
load=lambda p: json.load(open(R+p))
def save(p,o):
    t=R+p+'.tmp'; json.dump(o,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,R+p)
d=load('out/B8.json'); br=load('out/B8_brands.json'); B={x['n']:x for x in br['b']}
wd=lambda q:'https://www.wikidata.org/wiki/'+q
for n,q,c,f in [('Syngenta','Q688613','Switzerland','2000'),('Spectrum Brands','Q771865','United States',None),('Allegion','Q16738121','Ireland','2013'),('Amerex','Q4742463','United States','1971'),('Raid','Q1473883',None,'1956')]:
    x=B[n]
    if c:x['c']=c
    if f:x['f']=f
    if not x.get('s'): x['s']=wd(q)
WL='https://www.lockwiki.com/index.php/'
def add(n,d_,mk,y,s,g,a=''):
    return {"n":n,"a":a,"d":d_,"mk":mk,"y":y,"s":s,"v":[],"dt":"keying","g":g}
new=[
 add("GOAL V18","Dimple pin-tumbler cylinder by GOAL with up to 19 active pins, rated UL 437 and fitted with a click-ball core-centering bearing.","GOAL","",WL+"Goal_V18","Dimple","V18"),
 add("Kromer Protector","Wafer-tumbler lock with eleven wafers and asymmetric double-bitted keys, patented in Prussia in 1874 and made for over 125 years.","Kromer","1874","https://en.wikipedia.org/wiki/Protector_lock","Wafer","Protector"),
 add("Abloy Profile","Disc-detainer cylinder by Abloy with 5 to 14 discs engaging a sidebar, made from 1977 to 2000.","Abloy","1977–2000",WL+"Abloy_Profile","Disc detainer","Profile"),
 add("ASSA dp4400","Six-pin cylinder by ASSA with a sidebar, graded EN 1303 Security Grade 6, with false gates and drill resistance.","ASSA","",WL+"ASSA_dp4400","Sidebar and pin tumbler","dp4400"),
 add("DOM ix TwinStar","Pin-tumbler cylinder by DOM with a collapsible sidebar and dimple key, rated EN 1303:2015.","DOM","",WL+"DOM_ix_TwinStar","Sidebar and pin tumbler","ix TwinStar"),
 add("DOM ix Saturn","Dimple pin-tumbler cylinder by DOM whose key has a moveable element, rated EN 1303:2015.","DOM","",WL+"DOM_ix_Saturn","Dimple","ix Saturn"),
 add("MIWA 3800","Hybrid dimple and pin-tumbler cylinder with magnetic sliders, made by MIWA in Japan with Ankerslot in the Netherlands.","MIWA","",WL+"MIWA_3800","Dimple","3800"),
 add("Fichet F3D","Push-type disc-detainer hybrid cylinder by Fichet with six disc components, made since 2003 as the successor to the Fichet 787.","Fichet","2003",WL+"Fichet_F3D","Disc detainer","F3D"),
 add("Corbin Emhart","UL 437 pin-tumbler cylinder by Corbin Russwin with six interlocking pin stacks and a grooved plug, made from 1978.","Corbin Russwin","1978",WL+"Corbin_Emhart","Pin tumbler","Emhart"),
 add("DOM RS 8","Pin-tumbler cylinder by DOM listed by LockWiki among high security locks.","DOM","",WL+"DOM_RS_8","Pin tumbler","RS 8"),
 add("Hi-Shear LK 1200","Restricted-keyway pin-tumbler cylinder by Hi-Shear built to MIL-P-43607E, made in 1982 and 1983.","Hi-Shear","1982–1983",WL+"Hi-Shear_LK_1200","Pin tumbler","LK 1200"),
 add("Sargent & Greenleaf 951","Restricted-keyway pin-tumbler cylinder meeting MIL-DTL-43607J, sold only to authorised government agencies.","Sargent & Greenleaf","",WL+"S%26G_951","Pin tumbler","S&G 951"),
]
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      if not k.get('x'): continue
      if k['n']=='High-security lock cylinder':
        have={e['n'] for e in k['x']}
        k['x']+= [e for e in new if e['n'] not in have]
        k['xg']=['Disc detainer','Sidebar and pin tumbler','Pin tumbler','Dimple','Lever','Wafer','Magnetic']
        order={g:i for i,g in enumerate(k['xg'])}
        k['x'].sort(key=lambda e:(order[e['g']],e['y'][:4] or '9999',e['n']))
        k['sel']=k['sel'].rstrip()+" Complete: 18 of 18 locks in LockWiki's High security locks list (ASSA Twin V-10 and Combi, BiLock Exclusive and NG, and Everest are versions) and 15 of 15 lock pages in its category of the same name; seven lines from other fetched pages sit outside both."
      elif k['n']=='Baby monitor' or k['n']=='Antique lock & key':
        k['sel']=k['sel'].rstrip()+(" No complete list exists; follows the Wikipedia articles named here." if k['n']!='Baby monitor' else " No complete list exists; follows the Wikipedia article named here.")
L,A=d['depts'][0],d['depts'][3]
L['ms']+=[
 {"mkt":"Cylindrical door locks, worldwide","who":"Allegion plc","share":"over 28.5 %","yr":2025,"s":"https://www.gminsights.com/industry-analysis/cylindrical-door-lock-market","note":"market share as the page states it; top five (with ASSA ABLOY, dormakaba, Taiwan Fu Hsing, Miwa) 68.3 %"},
 {"mkt":"Mechanical locks, worldwide","who":"ASSA ABLOY, Allegion, dormakaba","share":"50 % together","yr":2025,"s":"https://www.futuremarketinsights.com/reports/mechanical-locks-market-share-analysis","note":"combined share as the page states it; the page's own tier tables disagree on the smaller brands"}]
save('out/B8.json',d); save('out/B8_brands.json',br)
