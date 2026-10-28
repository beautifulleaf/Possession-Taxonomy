import json,sys,re
d=json.load(open('out/A1.json'))
pat=re.compile(sys.argv[1],re.I)
for D in d['depts']:
  for S in D['s']:
    for k in S['k']:
      if pat.search(k['n']) or (len(sys.argv)>2 and pat.search(json.dumps(k))):
        print(D['n'],'|',S['n'],'|',k['n'],'| t',len(k.get('t',[])),'x',len(k.get('x',[])),'m',len(k.get('m',[])),'r',len(k.get('r',[])))
