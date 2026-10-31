import json,sys
d=json.load(open('rebuild/out/E1.json'))
allx={}
for dp in d['depts']:
    for sh in dp['s']:
        for k in sh['k']:
            for e in k.get('x') or []:
                allx.setdefault(e['n'].lower(),k['n'])
print(len(allx))
for kn in sys.argv[1:]:
    for dp in d['depts']:
        for sh in dp['s']:
            for k in sh['k']:
                if k['n']==kn: print(kn,[e['n'] for e in k['x']])
