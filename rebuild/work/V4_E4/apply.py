exec(open('/home/user/Possession-Taxonomy/rebuild/work/V4_E4/lib.py').read())
W='/home/user/Possession-Taxonomy/rebuild/work/V4_E4/'
for p in ('p1_swords','p2_blades','p3_bows','p4_ammo','p5_firearms','p6_armour'):
    exec(open(W+p+'.py').read())
# catch-all removal of remaining loose models
for kn,k in KIND.items():
    if k.get('m'): dropm(kn,'Retail product or unsourced piece; removed as out of scope')
# generic nl/sel for remaining kinds with entries
for kn,k in KIND.items():
    if k.get('x'):
        if not k.get('nl'): k['nl']=f"One entry is a named pattern, make or model of the {kn.lower()}; variants are versions."
        if not k.get('sel'): k['sel']=f"Entries cited from their own Wikipedia or maker pages; no whole-space list of the {kn.lower()} exists, so the list names the best-documented ones."
        if k.get('xg'):
            miss=[x['n'] for x in k['x'] if not x.get('g')]
            if miss: print('MISSING g',kn,miss)
D2=copy.deepcopy(SRC)
json.dump(SRC,open(W+'E4.new.json','w'),ensure_ascii=False,indent=1)
json.dump(REMOVED,open(W+'removed.json','w'),ensure_ascii=False,indent=1)
print(sum(len(k.get('x',[])) for k in KIND.values()))
