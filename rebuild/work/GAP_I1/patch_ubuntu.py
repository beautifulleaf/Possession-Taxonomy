import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/I1.json'
d=json.load(open(P))
U="https://en.wikipedia.org/wiki/Ubuntu_version_history"
rel=[("21.10","Impish Indri","2021","14 October 2021",0),("22.04","Jammy Jellyfish","2022","21 April 2022",1),("22.10","Kinetic Kudu","2022","20 October 2022",0),("23.04","Lunar Lobster","2023","20 April 2023",0),("23.10","Mantic Minotaur","2023","12 October 2023",0),("24.04","Noble Numbat","2024","25 April 2024",1),("24.10","Oracular Oriole","2024","10 October 2024",0),("25.04","Plucky Puffin","2025","17 April 2025",0),("25.10","Questing Quokka","2025","9 October 2025",0),("26.04","Resolute Raccoon","2026","23 April 2026",1),("26.10","Stonking Stingray","2026","15 October 2026",0)]
for dp in d['depts']:
  for sh in dp['s']:
    for k in sh['k']:
      for e in k.get('x') or []:
        if e['n']=='Ubuntu':
            vs=e['v']
            def find(num): 
                for v in vs:
                    if v['n'].startswith('Ubuntu '+num): return v
            for num,cn,y,date,lts in rel:
                nm=f"Ubuntu {num}{' LTS' if lts else ''} {cn}"
                v=find(num)
                if v is None:
                    v={"n":nm}; vs.append(v)
                v.update({"n":nm,"y":y,"d":f"released {date}"})
            vs.sort(key=lambda v:[int(p) for p in v['n'].split()[1].split('.')])
            print(len(vs))
tmp=P+'.tmp'; json.dump(d,open(tmp,'w'),ensure_ascii=False); os.replace(tmp,P)
