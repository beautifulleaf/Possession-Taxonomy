import json
d=json.load(open('out/J4.json'))
print(json.dumps(d['b'])[:600])
for D in d['depts']:
    print('\n##',D['n'],D.get('mode'),[k for k in D if k not in('n','s')])
    for S in D['s']:
        print(' -',S['n'],len(S['k']))
        for K in S['k']:
            print('     ',K['n'],'| x',len(K.get('x',[])),'m',len(K.get('m',[])),'r',len(K.get('r',[])),'t',len(K.get('t',[])), [x['n'] for x in K.get('x',[])][:6])
