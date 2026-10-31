import json,sys
d=json.load(open('out/A1.json'))
for D in d['depts']:
  for S in D['s']:
    for k in S['k']:
      if k['n'] in sys.argv[1:]:
        print('=====',D['n'],'|',S['n']);print(json.dumps(k,indent=1,ensure_ascii=False))
