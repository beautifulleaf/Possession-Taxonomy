import json,sys
c=sys.argv[1]
d=json.load(open(f'reader/{c}.json'))
print(c, d.get('lead'))
print('top keys',list(d.keys()))
tk=ta=0
for dp in d.get('depts',[]):
    nk=sum(len(s.get('k',[])) for s in dp.get('s',[]))
    print(f"\n## DEPT {dp['n']} mode={dp.get('mode')} kinds={nk} note={dp.get('note','')}")
    for s in dp.get('s',[]):
        print(f"  # SHELF {s['n']} ({len(s.get('k',[]))})")
        for k in s.get('k',[]):
            tk+=1; x=k.get('x',[]); ta+=len(x)
            print(f"    - {k['n']} | x={len(x)} t={len(k.get('t',[]))} m={len(k.get('m',[]))} r={len(k.get('r',[]))} | T: {'; '.join(k.get('t',[]))[:200]} | X: {'; '.join(a['n']+('('+a.get('mk','')+')' if a.get('mk') else '') for a in x)[:300]}")
print('\nTOTAL kinds',tk,'archetypes',ta)
