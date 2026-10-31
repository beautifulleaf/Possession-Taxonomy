import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/D4.json'
d=json.load(open(P))
Y={'X-Pro3':'2019','X-E4':'2021','X-E5':'2025','X-T3':'2018','X-T4':'2020','X-T5':'2022','X-H1':'2018','X-H2':'2022','X-H2S':'2022',
'α7R V':'2022','α7C II':'2023','α7CR':'2023','α6100':'2019','α6600':'2019',
'Lumix GH7':None,'OM-1':'2022','EOS-1D X':'2012','EOS-1D X Mark II':'2016','EOS-1D X Mark III':'2020','EOS-1D Mark III':'2007','EOS-1D Mark IV':'2009'}
n=0
for dep in d['depts']:
  for sh in dep['s']:
    for k in sh['k']:
      for e in k.get('x',[]):
        if e['g'] in ('Fujifilm X','Sony E','Canon EF','Micro Four Thirds','Fujifilm G') or True:
          for v in e.get('v',[]):
            y=Y.get(v['n'])
            if y and not v.get('y'): v['y']=y; n+=1
        if e['n']=='Fujifilm X-E' and not e.get('y'): e['y']='2012'
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P); print(n)
