import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(P+'F3.json'))
ks={k['n']:k for dp in d['depts'] for sh in dp['s'] for k in sh.get('k',[])}
KM={'O':'Order of chivalry or state order','G':'Gallantry and merit decoration','S':'Gallantry and merit decoration','L':'Long-service and good-conduct medal','C':'Campaign medal'}
DS={'O':'Order of {c}','G':'Gallantry or bravery award of {c}','S':'Merit or service decoration of {c}','L':'Long-service award of {c}','C':'Campaign or service medal of {c}'}
cnt={}
for line in open('/home/user/Possession-Taxonomy/rebuild/work/GAP_F3/awards.txt',encoding='utf8').read().splitlines():
    if not line.strip(): continue
    c,page,t,rest=line.split('|',3)
    k=ks[KM[t]]
    have={e['n'].lower() for kk in ks.values() for e in kk.get('x',[])}
    for item in rest.split('||'):
        parts=item.split('|'); n=parts[0].strip(); y=parts[1].strip() if len(parts)>1 else ''
        if not n or n.lower() in have: continue
        have.add(n.lower())
        k['x'].append({"n":n,"a":"","d":DS[t].format(c=c)+", listed in Wikipedia's article on its orders, decorations and medals.","mk":"","y":y,"s":"https://en.wikipedia.org/wiki/"+page,"v":[],"g":c})
        cnt[k['n']]=cnt.get(k['n'],0)+1
add=" Round 2: the country articles 'Orders, decorations, and medals of' Brazil, Germany (Federal Republic), Argentina, Australia, Canada, China, India, Indonesia, Italy, Mexico, Russia, Saudi Arabia, South Africa, South Korea and Turkey were read (page windows of 100,000 characters for the longest, so late sections of Australia, Canada, Indonesia, Italy and Russia are unread); prizes, honorary titles and commemorative or jubilee medals are out of scope. Covers G20 states France, Japan, United Kingdom and United States from earlier passes and the fifteen above; the European Union has no such article."
for n in set(KM.values()):
    ks[n]['sel']=ks[n]['sel'].rstrip()+add
json.dump(d,open(P+'F3.json.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'F3.json.tmp',P+'F3.json')
print(cnt)
