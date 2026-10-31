import json,os,re
P='rebuild/out/E1.json'
d=json.load(open(P))
K={}
for dp in d['depts']:
    for sh in dp['s']:
        for k in sh['k']: K[k['n']]=k
def ent(n):
    for k in K.values():
        for e in k.get('x') or []:
            if e['n']==n: yield e
def upd(n,**kw):
    c=0
    for e in ent(n):
        c+=1
        for a,b in kw.items():
            if a in('own','tier','own_y') :
                if a=='own' and e.get('own') not in(None,'','owner not stated'): break
                e[a]=b
            elif not e.get(a): e[a]=b
    return c
print(upd('Gund bears',own='Spin Master',own_y='2018',tier='Global group',cty='United States',y='1898'))
print(upd('Beanie Babies',own='Ty Inc.',tier='Independent',cty='United States'))
print(upd('Britains hollow-cast soldiers',own='Tomy',own_y='2011',tier='Independent',cty='United Kingdom'))
print(upd('Lundby',cty='Sweden'), upd('Lundby furniture',cty='Sweden'))
print(upd('Merrythought bears',own='Holmes family',own_y='2011',tier='Independent',cty='United Kingdom',y='1930'))
print(upd('Madame Alexander Doll Company',cty='United States',y='1923'))
print(upd('Schleich figures',own='Partners Group',own_y='2019',tier='Independent',cty='Germany',y='1935'))
# Polly Pocket origin
print(upd('Polly Pocket',cty='United Kingdom'))
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P)
