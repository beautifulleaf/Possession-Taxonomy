import json,os
R='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(R+'B8.json'));br=json.load(open(R+'B8_brands.json'))
removed=set()
LS='https://www.lockwiki.com/index.php/High_security_locks'
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      keep=k['n'] in('High-security lock cylinder','Antique lock & key')
      if not keep:
        for m in k.pop('m',[]): removed.add(m[1])
        for m in k.pop('r',[]): removed.add(m[1])
        for x in k.pop('x',[]):
          if x.get('mk'): removed.add(x['mk'])
      if k['n']=='High-security lock cylinder':
        k['nl']="One entry is a high-security lock cylinder line sold under its own name; later generations and variants of the same mechanism are versions."
        k['sel']="Follows LockWiki's list 'High security locks' (18 locks, all in scope, a subjective editors' list) and its category of the same name, grouped by mechanism. Medeco M3, Mul-T-Lock MT5+ and the other lines kept from the earlier pass are sourced from lpubelts.com and LockWiki pages; no whole-space reference exists beyond these lists."
        k['xg']=["Disc detainer","Sidebar and pin tumbler","Lever","Magnetic","Dimple"]
        gm={'Abloy Protec2':0,'Abloy Classic':0,'Rosengrens RKL-10':0,'Abloy Easy':0,
            'Mul-T-Lock MT5+':1,'Mul-T-Lock Interactive':1,'Medeco M3':1,'Medeco Biaxial':1,'ASSA Twin':1,'BiLock':1,'Kaba expert':1,'Schlage Primus':1,'EVVA 3KS':1,'EVVA ICS':1,
            'Fichet 787':2,'Opnus Memolis':2,'STUV Ivox 4.19.97':2,
            'EVVA MCS':3,'WEST 917':4,'GOAL V18':4}
        by={x['n']:x for x in k['x']}
        def V(n,mk,y,dd): return {"n":n,"mk":mk,"y":y,"d":dd}
        # added versions from LockWiki list
        by['BiLock']['v'].append(V("BiLock NG","Australian Lock Company","1998","Dual-sidebar, twelve sliders in two rows of six; still in production"))
        by['Schlage Primus']['s2']=None
        def new(n,a,dd,mk,y,s,dt):
          by[n]={"n":n,"a":a,"d":dd,"mk":mk,"y":y,"s":s,"v":[],"dt":dt}
        new('Abloy Easy','Abloy Easy',"Disc-detainer lock whose key turns in one direction only, for spring bolts, padlocks and cam locks; announced in April 2021 and successor to the Abloy Sento.","Abloy","2021","https://www.lockwiki.com/index.php/Abloy_Easy","format (spring bolt, padlock, cam lock)")
        new('EVVA ICS','ICS',"Pin-tumbler lock with ten pin-tumblers and two sidebars.","EVVA","","https://www.lockwiki.com/index.php/EVVA_ICS","keying · format")
        new('Fichet 787','787',"French lever cylinder with 8 or 10 levers and gears that engage a fence, mixing lever, combination and disc-detainer ideas; made from 1986.","Fichet","1986","https://www.lockwiki.com/index.php/Fichet_787","lever count 8 or 10")
        new('Opnus Memolis','Memolis',"Lever cylinder with fourteen levers, twelve of them re-keyable, and a horizontal, centred keyhole closed at both edges.","Opnus","","https://www.lockwiki.com/index.php/Opnus_Memolis","re-keyable levers")
        new('Rosengrens RKL-10','RKL-10',"Disc-detainer safe lock by Rosengrens; Technical Entry published a decoding method for it in 2012.","Rosengrens","","https://www.lockwiki.com/index.php/Rosengrens_RKL-10","keying")
        new('STUV Ivox 4.19.97','Ivox · STUV Ivox',"Lever lock with a plastic curtain and eight levers, six possible heights per lever and no control lever.","STUV","","https://www.lockwiki.com/index.php/STUV_Ivox_4.19.97","lever heights")
        new('WEST 917','917',"Pin-tumbler cylinder by the Japanese company WEST, opened with a dimple key.","WEST","","https://www.lockwiki.com/index.php/WEST_917","keying")
        by['Schlage Primus'].pop('s2')
        for n in by: removed.add(by[n]['mk'])
        # GOAL V18 / Kromer Protector: LockWiki pages not fetched, so not added as entries
        out=[]
        for n,x in by.items():
          if n in gm: x['g']=k['xg'][gm[n]]
          else: raise SystemExit('no g '+n)
          out.append(x)
        out.sort(key=lambda x:(gm[x['n']],x['n']))
        for x in out:
          if x['n'] in('Abloy Protec2','EVVA MCS'): x['role']='landmark'
        k['x']=out
      if k['n']=='Antique lock & key':
        k['nl']="One entry is a historic lock type known by its inventor or period, such as the Bramah or Chubb lock; maker's variants are versions."
        k['sel']="No whole-space reference exists; the entries are the lock types named in Wikipedia's Lock and key, Padlock, Bramah lock and Chubb detector lock articles, grouped by period."
        k['xg']=["Ancient","18th century","19th century"]
        for x in k['x']:
          y=x['y']; x['g']='Ancient' if 'ancient' in y or 'BC' in y else ('18th century' if y.startswith('17') else '19th century')
          if x['n']=='Egyptian pin lock': x['role']='origin'
          if x['n']=='Barron double-acting lever lock': x['role']='origin'
        order=['Ancient','18th century','19th century']
        k['x'].sort(key=lambda x:(order.index(x['g']),x['y']))
# market panels
for dp in d['depts']:
  if dp['n']=='Locks & door security':
    dp['ms']=[{"mkt":"Global consumer smart locks","who":"ASSA ABLOY","share":"21 %","yr":2021,"s":"https://www.securityworldmarket.com/int/News/Business-News/research-shows-assa-abloy-is-in-the-driving-seat-for-smart-locks","note":"Strategy Analytics estimate; the report names Yale, Kwikset and Schlage as the power players and expected 35 % for ASSA ABLOY if it bought Kwikset"}]
    dp['msum']="Consumer smart locks are led by ASSA ABLOY, whose brands include Yale and August; Allegion's Schlage was the other independent power player in 2022. No share figure was found for mechanical locks."
    removed|={'ASSA ABLOY','Allegion','Spectrum Brands'}
  if dp['n']=='Alarms, cameras & doorbells':
    dp['ms']=[{"mkt":"US and Canada residential monitored security","who":"ADT","share":"about 30 %","yr":2018,"s":"https://www.sec.gov/Archives/edgar/data/0001703056/000119312518011953/d501902ds1a.htm","note":"ADT's own estimate in its January 2018 filing; about five times the next largest residential competitor"}]
    dp['msum']="ADT leads professionally monitored home security in the United States and Canada by its own estimate. No current share figure for cameras or doorbells was found."
    removed.add('ADT')
json.dump(d,open(R+'B8.json.tmp','w'),ensure_ascii=False,indent=1)
os.replace(R+'B8.json.tmp',R+'B8.json')
have={b['n'] for b in br['b']}
cty={'Fichet':'France','WEST':'Japan','Australian Lock Company':'Australia'}
add=[]
for n in sorted(removed-have):
  if not n: continue
  add.append({"n":n,"c":cty.get(n,""),"f":"","seg":"Mainstream","d":"","lines":[],"eras":[],"sig":[],"sc":["Home security"],"rel":[],"s":"","kf":""})
br['b']+=add
json.dump(br,open(R+'B8_brands.json.tmp','w'),ensure_ascii=False,indent=1)
os.replace(R+'B8_brands.json.tmp',R+'B8_brands.json')
print('added brands',[a['n'] for a in add])
