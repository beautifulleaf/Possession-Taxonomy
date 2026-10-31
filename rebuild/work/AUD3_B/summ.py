import json,sys
c=sys.argv[1]; R='/home/user/Possession-Taxonomy/rebuild/reader/'
d=json.load(open(R+c+'.json'))
print(c, d.get('lead'))
tk=tx=0
for dp in d['depts']:
    nk=sum(len(s['k']) for s in dp['s']); na=sum(len(k.get('x',[])) for s in dp['s'] for k in s['k'])
    print(f"\n## DEPT {dp['n']} [{dp.get('mode')}] kinds={nk} arch={na} note={dp.get('note','')}")
    for s in dp['s']:
        print(f"  -- {s['n']} ({len(s['k'])})")
        for k in s['k']:
            tk+=1; x=k.get('x',[]); tx+=len(x)
            xs=', '.join(a['n']+('['+str(len(a.get('v',[])))+'v]' if a.get('v') else '') for a in x)
            print(f"    * {k['n']} | t={len(k.get('t',[]))} x={len(x)} m={len(k.get('m',[]))} r={len(k.get('r',[]))} tg={k.get('tg','')}")
            if k.get('t'): print('       t:', '; '.join(k['t'])[:250])
            if xs: print('       x:', xs[:450])
            if k.get('m'): print('       m:', '; '.join(f'{a[0]} ({a[1]})' for a in k['m'])[:160])
            if k.get('r'): print('       r:', '; '.join(f'{a[0]} ({a[1]})' for a in k['r'])[:160])
print('\nTOTAL kinds',tk,'arch',tx)
for sub in ['brands','traditions']:
    try:
        b=json.load(open(R+sub+'/'+c+'.json'))
        key='b' if sub=='brands' else 't'
        L=b.get(key,b if isinstance(b,list) else [])
        print(f'\n{sub}: {len(L)}')
        print('; '.join(f"{x['n']}({x.get('c','') or x.get('r','')}|{x.get('seg','') or x.get('g','')})" for x in L))
    except Exception as e: print(sub,'none',e)
