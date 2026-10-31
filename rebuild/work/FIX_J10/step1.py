import json
P='out/J10.json';d=json.load(open(P))
B=json.load(open('out/J10_brands.json'));br={x['n']:x for x in B['b']}
def K(n):
    for D in d['depts']:
        for S in D['s']:
            for k in S['k']:
                if k['n']==n: return k,S
def rm(n):
    k,S=K(n);S['k'].remove(k);return k
# J10-6 briar
bk,_=K('Briar pipe')
shapes=[];mk=[]
for a in bk['x']:
    (mk if a.get('mk') else shapes).append(a)
for a in mk:
    if a['n']=='Peterson System':
        dub=[s for s in shapes if s['n']=='Dublin'][0]
        dub['v'].insert(0,{"n":"Peterson System","mk":"Peterson","y":"1894","d":"Dublin pipe with a moisture reservoir in the shank, patented as the 'Dry System'"})
    else:
        b=br.get(a['mk'])
        if b is not None:
            for v in [a['n']]+[v['n'] for v in a['v']]:
                if v!=b['n'] and v not in b.setdefault('lines',[]): b['lines'].append(v)
bk['x']=shapes
bk['d']=bk['d'].replace('makers\' own shape references as versions','maker lines are listed on the brand register')
# J10-6 Swisher dup
mm,_=K('Machine-made cigar'); mm['x']=[a for a in mm['x'] if a['n']!='Swisher Sweets']
# J10-5 fold empties
def fold(n,into,typ=None):
    k=rm(n);t=K(into)[0].setdefault('t',[]);t.append(typ or k['n'])
fold('Molasses catcher','Hookah spare parts')
fold('Herbal smoking blend','Herbal & other plant products' if False else 'Kratom','Herbal smoking blend') if False else None
json.dump(d,open('/tmp/x','w')) if False else None
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1);import os;os.replace(P+'.tmp',P)
json.dump(B,open('out/J10_brands.json.tmp','w'),ensure_ascii=False,indent=1);os.replace('out/J10_brands.json.tmp','out/J10_brands.json')
