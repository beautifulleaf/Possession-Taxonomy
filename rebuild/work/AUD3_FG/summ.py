import json,sys
c=sys.argv[1]
d=json.load(open(f'rebuild/reader/{c}.json'))
print(c, d.get('lead'))
tk=tx=0
for dp in d['depts']:
    print(f"\n== DEPT {dp['n']} [{dp.get('mode')}] note={dp.get('note','')}")
    for sh in dp['s']:
        print(f"  -- SHELF {sh['n']} ({len(sh['k'])} kinds)")
        for k in sh['k']:
            tk+=1; x=k.get('x',[]); tx+=len(x)
            nv=sum(len(a.get('v',[])) for a in x)
            print(f"     * {k['n']} | x={len(x)} v={nv} t={len(k.get('t',[]))} m={len(k.get('m',[]))} r={len(k.get('r',[]))} tg={k.get('tg','')}")
            if k.get('t'): print("         t:", "; ".join(k['t'])[:400])
            if x: print("         x:", "; ".join(f"{a['n']}({a.get('mk','')})" for a in x)[:600])
            if k.get('m'): print("         m:", "; ".join(f"{m[0]}/{m[1]}" if len(m)>1 else m[0] for m in k['m'])[:300])
print(f"\nTOTAL kinds={tk} archetypes={tx}")
