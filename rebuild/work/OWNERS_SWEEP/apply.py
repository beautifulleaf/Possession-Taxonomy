import json,os,sys
sys.path.insert(0,'.')
from lib import entries
R='../../out/'
out={}
for c in ['E2','H1','J9']:
    rows=[l.rstrip('\n').split('\t') for l in open(f'res_{c}.tsv')][1:]
    rows=[r+['']*(6-len(r)) for r in rows if r and r[0]]
    d=json.load(open(R+f'{c}.json')); b=json.load(open(R+f'{c}_brands.json'))
    es=entries(d)
    before=sum(1 for o in es if o['mk'] and not o.get('own'))
    nset=0; nb=0
    for mk,res,own,tier,oy,note in rows:
        for o in es:
            if o['mk']==mk and not o.get('own'):
                o['own']=own; nset+=1
                if tier and tier!='-' and not o.get('tier'): o['tier']=tier
                if oy and not o.get('own_y'): o['own_y']=oy
        for x in b['b']:
            if x['n']==mk and not x.get('own'):
                x['own']=own; nb+=1
                if tier and tier!='-' and not x.get('tier'): x['tier']=tier
    after=sum(1 for o in es if o['mk'] and not o.get('own'))
    for fn,obj in ((f'{c}.json',d),(f'{c}_brands.json',b)):
        tmp=R+fn+'.tmp'
        json.dump(obj,open(tmp,'w'),ensure_ascii=False,indent=json.load(open(R+fn)) and None) if False else None
    out[c]=(before,after,nset,nb,len(rows))
    print(c,before,after,nset,nb,len(rows))
    # write preserving original formatting style
    for fn,obj in ((f'{c}.json',d),(f'{c}_brands.json',b)):
        raw=open(R+fn).read()
        ind=2 if raw.startswith('{\n') else None
        tmp=R+fn+'.tmp'
        with open(tmp,'w') as f: json.dump(obj,f,ensure_ascii=False,indent=ind)
        os.replace(tmp,R+fn)
