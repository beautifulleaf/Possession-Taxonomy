import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(P+'E2.json')); br=json.load(open(P+'E2_brands.json')); reg={b['n']:b for b in br['b']}
OW={'Scarpa':('Italy','Parisotto family','Independent','1956'),'CAMP':('Italy',None,'Independent',None),'Grivel':('Italy',None,None,None),'Select':('Denmark',None,None,None),
'Lange':('United States',None,None,None),'Hi-Tec':('Netherlands',None,None,None),'Kelly Kettle':('Ireland',None,None,None),'Look':('France',None,None,None)}
n=0
for dpt in d['depts']:
  for m in dpt.get('ms') or []:
    if m.get('yr') is None: m['yr']='not stated'
  for s in dpt['s']:
    for kk in s['k']:
      for e in kk.get('x',[]):
        f=OW.get(e.get('mk'))
        if f:
          for key,val in zip(('cty','own','tier','own_y'),f):
            if val and not e.get(key): e[key]=val; n+=1
for mk,f in OW.items():
  b=reg.get(mk)
  if b:
    for key,val in zip(('c','own','tier'),f[:3]):
      if val and not b.get(key): b[key]=val
for fn,o in (('E2.json',d),('E2_brands.json',br)):
  t=P+fn+'.tmp'; json.dump(o,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,P+fn)
print(n)
