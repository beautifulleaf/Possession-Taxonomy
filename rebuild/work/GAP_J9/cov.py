import json,os,collections
P='/home/user/Possession-Taxonomy/rebuild/out/J9.json'
d=json.load(open(P))
names={'List_of_soft_drinks_by_country':'"List of soft drinks by country"','List_of_bottled_water_brands':'"List of bottled water brands"','List_of_Coca-Cola_brands':'"List of Coca-Cola brands"','Keurig_Dr_Pepper':'the Keurig Dr Pepper page','List_of_PepsiCo_brands':'"List of PepsiCo brands"','List_of_brand_name_soft_drink_products':'"List of brand name soft drink products"','Craft_soda':'"Craft soda"','best-craft-soda-brands-market':'The Daily Meal craft-soda list'}
for dp in d['depts']:
  for sh in dp['s']:
    for k in sh['k']:
      if not k['x']: continue
      refs=[];other=0
      for x in k['x']:
        u=x.get('s','')
        hit=[v for a,v in names.items() if u.endswith(a)]
        if hit:
          if hit[0] not in refs: refs.append(hit[0])
        else: other+=1
      txt=', '.join(refs)
      if other: txt+=(', and ' if txt else '')+f'{other} brand page{"s" if other>1 else ""}'
      line=f' No complete list exists; follows {txt}, as the entries cite them.'
      s=k['sel'].rstrip()
      if 'No complete list exists' in s or 'Complete:' in s or 'Covers ' in s: continue
      k['sel']=s+line
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1)
os.replace(P+'.tmp',P)
