import json,os,re
P='../../out/J3.json'
d=json.load(open(P))
CH=("Covers {n} of about 375 in Wikidata's cheese class (https://www.wikidata.org/wiki/Q10943), which is shared by all cheese kinds; "
"the class was read in full and the rest belong to other kinds, are dishes or classes, or have no usable description. "
"Also read: the German, Dutch and Italian national lists in full (named cheeses with a stated milk, type or protected status placed), the French list to its end except its 'Other cheeses' section, and the Belgian, Austrian and Danish list pages do not exist (404); no complete world list of cheeses exists.")
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      x=k.get('x',[])
      if not x: continue
      sel=k.get('sel','')
      if 'Wikipedia' in sel and 'cheeses' in sel:
        head=sel.split(' Covers ')[0].rstrip('.')
        k['sel']=head+'. '+CH.format(n=len(x))
        # unify italy label
      else:
        head=re.split(r' Covers \d+ entries',sel)[0].rstrip()
        if k['n']=='Butter':
          k['sel']=head.replace('No complete list of this kind was fetched; ','')+" Covers 2 of 5 in Wikidata's butter class (https://www.wikidata.org/wiki/Q34172): Beurre d'Ardenne and Bresse butter; Smen is placed under ghee and clarified butter, and goat butter and chivry butter have no description to source. The other entries are protected-name and brand pages."
        else:
          k['sel']="No complete list exists; follows the protected-name and brand pages cited on each entry and the overviews listed for the department."
      if k['n']=='Italian mountain cheese':
        for e in x:
          if e.get('g')=='Italy': e['g']='Other Italian regions'
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1);os.replace(P+'.tmp',P)
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      if k['n'] in('Butter','Skyr','Brie'): print(k['sel'],'\n')
