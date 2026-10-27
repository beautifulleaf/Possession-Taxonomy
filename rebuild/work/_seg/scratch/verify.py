import csv,json,sys,collections
B='/home/user/Possession-Taxonomy/rebuild/work/_seg/'
V=json.load(open('/home/user/Possession-Taxonomy/rebuild/SEGMENTS.json'))['domains']
for g in sys.argv[1:]:
    rd=lambda p: list(csv.reader(open(p,encoding='utf-8'),delimiter='\t',quoting=csv.QUOTE_NONE))
    todo=rd(B+g+'.todo.tsv'); m=rd(B+g+'.map.tsv')
    assert m[0]==['name','seg','kf'],m[0]
    dom={r[0]:r[1] for r in todo[1:]}
    cnt=collections.Counter(r[0] for r in m[1:]); errs=[]
    for n in dom:
        if cnt[n]!=1: errs.append(('count',n,cnt[n]))
    for r in m[1:]:
        if len(r)!=3 or r[0] not in dom: errs.append(('row',r)); continue
        if r[1] not in V[dom[r[0]]]['segs']: errs.append(('seg',r))
        if not r[2] or r[2]!=r[2].lower() or not 1<=len(r[2].split())<=3: errs.append(('kf',r))
    print(g,'rows',len(m)-1,'todo',len(dom),'errors',errs)
    for k,v in collections.Counter(r[1] for r in m[1:]).most_common(): print('  ',v,k)
