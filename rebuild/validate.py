import json,sys,re
p=sys.argv[1]; d=json.load(open(p)); err=[]
def need(o,k,w):
    if not o.get(k): err.append(f"{w}: missing {k}")
if not re.match(r'^[A-J]\d+$',d.get('c','')): err.append('bad c')
names=set()
for i,dp in enumerate(d.get('depts',[])):
    need(dp,'n',f'dept {i}')
    if dp.get('mode') not in ('variety','tier','mixed'): err.append(f"dept {dp.get('n')}: mode")
    for s in dp.get('s',[]):
        need(s,'n','shelf')
        for k in s.get('k',[]):
            w=f"kind {k.get('n')}"; need(k,'n',w); need(k,'d',w)
            if k['n'].lower() in names: err.append(f"{w}: duplicate kind")
            names.add(k['n'].lower())
            if k['n'].lower().startswith('other '): err.append(f"{w}: catch-all name")
            for x in k.get('x',[]) or []:
                ww=f"{w} / arch {x.get('n')}"; need(x,'n',ww); need(x,'s',ww)
                if x.get('s') and not x['s'].startswith('http'): err.append(f"{ww}: bad source")
                for v in x.get('v',[]) or []:
                    if not isinstance(v,dict) or not v.get('n'): err.append(f"{ww}: bad version")
            for key in ('m','r'):
                for t in k.get(key,[]) or []:
                    if not (isinstance(t,list) and len(t)==2): err.append(f"{w}: bad {key}")
            seen=set()
            for t in (k.get('m') or []):
                if tuple(t) in seen: err.append(f"{w}: dup model {t}")
                seen.add(tuple(t))
print('\n'.join(err[:60]) or 'OK', f"({len(err)} errors, {len(names)} kinds, {sum(len(k.get('x',[]) or []) for dp in d['depts'] for s in dp['s'] for k in s['k'])} archetypes)")
sys.exit(1 if err else 0)
