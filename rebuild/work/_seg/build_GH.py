import json,sys,collections
B='/home/user/Possession-Taxonomy/rebuild/'
codes={'P':'Professional & flagship','PR':'Premium','M':'Mainstream','V':'Value','H':'Heritage manufactory','A':'Artisan & independent','S':'Specialist','O':'Own-label & retailer','I':'Institution & issuer'}
voc=json.load(open(B+'SEGMENTS.json'))['domains']
for g in sys.argv[1:]:
    W=B+'work/_seg/'
    todo=[l.rstrip('\n').split('\t') for l in open(W+g+'.todo.tsv',encoding='utf-8')][1:]
    dec={}
    for l in open(W+g+'.dec.txt',encoding='utf-8'):
        if not l.strip(): continue
        n,c,k=l.rstrip('\n').split('|'); dec[n]=(codes[c],k)
    names=[r[0] for r in todo]
    miss=[n for n in names if n not in dec]; extra=[n for n in dec if n not in names]
    print(g,'missing',miss,'extra',extra)
    if miss: continue
    with open(W+g+'.map.tsv.tmp','w',encoding='utf-8') as f:
        f.write('name\tseg\tkf\n')
        for r in todo: f.write(f'{r[0]}\t{dec[r[0]][0]}\t{dec[r[0]][1]}\n')
    import os; os.replace(W+g+'.map.tsv.tmp',W+g+'.map.tsv')
    # verify
    m=[l.rstrip('\n').split('\t') for l in open(W+g+'.map.tsv',encoding='utf-8')][1:]
    dom={r[0]:r[1] for r in todo}
    c=collections.Counter(x[0] for x in m)
    assert all(c[n]==1 for n in names) and len(m)==len(names)
    for n,s,k in m:
        assert s in voc[dom[n]]['segs'],(n,s); assert k and k==k.lower() and 1<=len(k.split())<=3,(n,k)
    print(g,'OK',len(m)); print(collections.Counter(x[1] for x in m).most_common())
