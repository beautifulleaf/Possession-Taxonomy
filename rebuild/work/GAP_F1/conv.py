import json,copy,os,sys
def idx(path):
    b=json.load(open(path)); out={}
    def rec(o,par):
        if isinstance(o,dict):
            if 'n' in o and 'depts' not in o and ('s' in o or 'd' in o or 'mk' in o): out.setdefault(o['n'].lower(),[]).append((o,par))
            for v in o.values(): rec(v,o if ('n' in o) else par)
        elif isinstance(o,list):
            for v in o: rec(v,par)
    rec(b,None); return out
srcs=[idx('../STR_F1/bak/F1.json'),idx('../V4_F1/bak/F1.json'),idx('../F1/old.json')]
d=json.load(open('bak/F1.json'))
STORAGE='Storage & protection'
log={'entry':[],'version':[],'removed':[]}
def clean(o):
    e={k:v for k,v in o.items() if k in('n','a','d','mk','y','s','dt','v','role')}
    e.setdefault('d',''); e.setdefault('mk',''); e.setdefault('y','')
    return e
for dp in d['depts']:
  for sh in dp['s']:
    for k in sh['k']:
      ms=k.pop('m',None)
      if not ms: continue
      x=k.setdefault('x',[])
      byname={e['n'].lower():e for e in x}
      kind=k['n']
      for n,mk in ms:
        if dp['n']==STORAGE:
            log['removed'].append((kind,n,'commodity SKU')); continue
        f=None
        for i in srcs:
            if n.lower() in i: f=i[n.lower()][0]; break
        if not f:
            log['removed'].append((kind,n,'no fetched source for the line')); continue
        o,par=f
        if n.lower() in byname:
            continue
        if o.get('s'):
            e=clean(o); 
            if not e.get('mk'): e['mk']=mk
            x.append(e); byname[n.lower()]=e; log['entry'].append((kind,n)); continue
        # version record
        if par is None or not par.get('s') or par['n'].lower() in (kind.lower(),) or par['n'].lower().startswith('depts'):
            log['removed'].append((kind,n,'attribute or unsourced sub-row')); continue
        pe=byname.get(par['n'].lower())
        if pe is None:
            pe=clean(par); pe['v']=[]; x.append(pe); byname[par['n'].lower()]=pe; log['entry'].append((kind,par['n']+' (parent)'))
        v=pe.setdefault('v',[])
        if n.lower() not in [a['n'].lower() for a in v]:
            v.append({'n':n,'mk':o.get('mk') or mk,'y':o.get('y',''),'d':o.get('d','')}); log['version'].append((kind,n,par['n']))
json.dump(d,open('F1.step1.json','w'),ensure_ascii=False,indent=1)
json.dump(log,open('step1.log.json','w'),ensure_ascii=False,indent=1)
print({k:len(v) for k,v in log.items()})
for r in log['removed']:
    if r[2]!='commodity SKU': print(r)
print([ (a,b,c) for a,b,c in log['version']][:300])
