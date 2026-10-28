import json
d=json.load(open('out/I1.json'))
for di,dp in enumerate(d['depts']):
  for si,s in enumerate(dp['s']):
    for k in s['k']:
      x=k.get('x',[]);m=k.get('m',[])
      print(f"{di}|{dp['n']}|{s['n']}|{k['n']}|x={len(x)}|m={len(m)}|r={len(k.get('r',[]))}")
