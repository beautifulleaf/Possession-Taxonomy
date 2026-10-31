import json
d=json.load(open('../../out/F1.json'))
rm={'Compact cassette':['Pre-recorded musicassette'],'Microcassette':['Microcassette'],'MiniDisc':['Recordable MiniDisc','Prerecorded MiniDisc'],
'Wire recording':['Wire recorder spool','Dictabelt'],'Reel-to-reel tape':['Ampex pre-recorded tape'],'Ultra HD Blu-ray':['Steelbook edition'],
'Bookazine':['Newsstand bookazine'],'Full score':['Dover full-score reprint'],'Choral octavo':['Novello octavo'],'Popular song sheet':[]}
vrm={'Bookazine':['Imagine bookazines','Made Simple','Handbook','Guru Guide','Technology Tips Guide'],'Popular song sheet':['Large size','War size','Standard size']}
out=[]
for dp in d['depts']:
  for sh in dp['s']:
    for k in sh['k']:
      n=k['n']; 
      if n in rm:
        before=len(k.get('x',[]))
        for e in list(k.get('x',[])):
          if e['n'] in rm[n]: k['x'].remove(e); out.append((n,e['n']))
      for e in k.get('x',[]):
        if n in vrm and 'v' in e:
          for v in list(e['v']):
            if v['n'] in vrm[n]: e['v'].remove(v); out.append((n,e['n']+' > '+v['n']))
      # Mook parent only remains
json.dump(d,open('F1.s4a.json','w'),ensure_ascii=False,indent=1)
print(out)
