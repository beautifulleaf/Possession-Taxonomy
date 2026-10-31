import json
d=json.load(open('F1.step2.json'))
K={k['n']:k for dp in d['depts'] for sh in dp['s'] for k in sh['k']}
k=K['Edition class']
gm={'Editio princeps':'Origin','First edition':'Origin','First trade edition':'Origin','New edition':'Revision','Revised edition':'Revision','Revised and updated edition':'Revision','Critical edition':'Revision'}
for e in k['x']: e['g']=gm.get(e['n'],'Market and audience')
k['xg']='by purpose'
k=K['Private press book']
byn={e['n'].lower():e for e in k['x']}
out=[]
for e in k['x']:
    if e['n'].endswith(' book') and e['n'][:-5].lower() in byn:
        t=byn[e['n'][:-5].lower()]
        t.setdefault('v',[])
        for v in e.get('v',[]):
            if v['n'].lower() not in [a['n'].lower() for a in t['v']]: t['v'].append(v)
        continue
    out.append(e)
for e in out:
    if not e.get('g'): e['g']={'Cranach Presse':'Germany','Grabhorn Press':'United States'}.get(e['n'].replace(' book',''),'Country not stated')
k['x']=out
k=K['LP record']; k['xg']='by kind of release'
for e in k['x']:
    e['g']='Direct-to-disc' if 'direct' in e['n'].lower() else 'Retail event' if 'Record Store' in e['n'] else 'Audiophile reissue'
json.dump(d,open('F1.final.json','w'),ensure_ascii=False,indent=1)
print(len(k['x']),len(K['Private press book']['x']))
