import json, os, sys
os.chdir('/home/user/Possession-Taxonomy/rebuild')
S={'LH':'Luxury house','HM':'Haute maison','IM':'Independent maker','DS':'Designer','PR':'Premium','MS':'Mainstream','VA':'Value','BA':'Bespoke & artisan','TR':'Traditional & regional'}
src=dict(l.split(' ',1) for l in open('work/_harvest/A3_work/src.txt').read().split('\n') if l.strip())
p='work/_harvest/A3.json'
out=json.load(open(p))['b'] if os.path.exists(p) else []
have={b['n'].lower() for b in out}
for l in open('work/_harvest/A3_work/brands.txt'):
    l=l.rstrip('\n')
    if not l or l.startswith('#'): continue
    f=l.split('|')
    assert len(f)==7,l
    n,c,y,sg,kf,s,d=f
    if n.lower() in have: continue
    b={'n':n}
    if c: b['c']=c
    if y: b['f']=y
    b['seg']=S[sg]
    if kf: b['kf']=kf
    if d: b['d']=d
    b['s']=src[s].strip()
    out.append(b); have.add(n.lower())
json.dump({'b':out},open(p+'.tmp','w'),ensure_ascii=False,indent=0)
os.replace(p+'.tmp',p)
print(len(out))
