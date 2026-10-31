import json,os
p='rebuild/out/G3.json'
d=json.load(open(p))
n=0
for dp in d['depts']:
    for sh in dp['s']:
        for k in sh['k']:
            if k.get('x'):
                srcs=sorted({e.get('s','').split('/')[2] for e in k['x'] if e.get('s')})
                s=k.get('sel','')
                if 'No complete list exists' not in s:
                    k['sel']=s.rstrip()+' No complete list exists; follows the encyclopedia and maker pages cited on each entry ('+', '.join(srcs)+').'
                    n+=1
open(p+'.tmp','w').write(json.dumps(d,ensure_ascii=False,indent=1)); os.rename(p+'.tmp',p)
print(n)
