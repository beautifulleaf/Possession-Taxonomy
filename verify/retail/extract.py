"""Extract a pasted retailer brand directory from the session transcript.
usage: extract.py <transcript.jsonl> <domain e.g. www.ulta.com> <path-prefix e.g. /brand/> <out.txt>
Takes the LAST user message containing >=20 such links; keeps names in page order, de-duplicated."""
import json,re,sys
tr,dom,pre,out=sys.argv[1:5]
pat=re.compile(r'^\* \[(.+?)\]\(https://'+re.escape(dom)+re.escape(pre)+r'([^)]*)\)',re.M)
def texts(o):
    if isinstance(o,str): yield o
    elif isinstance(o,dict):
        for v in o.values(): yield from texts(v)
    elif isinstance(o,list):
        for v in o: yield from texts(v)
best=None
for line in open(tr):
    try: d=json.loads(line)
    except: continue
    if d.get('type') not in ('user','attachment','queue-operation'): continue
    for t in texts(d.get('message') or d.get('attachment') or d.get('content') or {}):
        f=pat.findall(t)
        if len(f)>=20: best=f
names=[];seen=set()
for n,s in (best or []):
    if n not in seen: seen.add(n);names.append((n,s))
open(out,'w').write(''.join(f'{n}\t{s}\n' for n,s in names)+f'#END {len(names)}\n')
print(len(best or []),'links',len(names),'unique')
