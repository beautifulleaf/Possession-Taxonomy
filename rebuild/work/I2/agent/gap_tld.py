import json,os
p='work/I2/shelves/04_00.json'
d=json.load(open(p))
k=[x for x in d['kinds'] if x['n']=='Domain name'][0]
add=[[".net","Verisign"],[".org","Public Interest Registry"],[".io","Internet Computer Bureau Ltd"],[".co",".CO Internet S.A.S."],[".eu","EURid"]]
have={tuple(m) for m in k['m']}
for m in add:
    if tuple(m) not in have: k['m'].append(m)
d['notes']+=" Gap pass 2026-10-27: added .net (Verisign), .org (Public Interest Registry), .io (Internet Computer Bureau Ltd), .co (.CO Internet S.A.S.) and .eu (EURid) as endings; registries per the Wikipedia List of Internet top-level domains and the .net, .io, .co and .eu pages (retrieved and logged; the IANA root database page itself was not fetched)."
json.dump(d,open(p+'.tmp','w'),ensure_ascii=False,indent=1)
os.replace(p+'.tmp',p)
