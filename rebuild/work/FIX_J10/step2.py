import json,os
P='out/J10.json';d=json.load(open(P))
def K(n):
    for D in d['depts']:
        for S in D['s']:
            for k in S['k']:
                if k['n']==n: return k,S
def rm(n):
    k,S=K(n);S['k'].remove(k)
rm('Kief');K('Hashish')[0]['t'].append('kief (loose resin glands)')
rm('Distillate');K('Prefilled vape cartridge')[0]['t'].append('distillate')
rm('Tincture');c=K('Capsule or tablet')[0];c['n']='Tincture, capsule or tablet';c['a']='CBD oil · drops';c['t']=['tincture','capsule','tablet']
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1);os.replace(P+'.tmp',P)
