import csv,json,sys,collections
G=sys.argv[1]
V=json.load(open('../../SEGMENTS.json'))['domains']
todo=list(csv.DictReader(open(f'{G}.todo.tsv',encoding='utf-8'),delimiter='\t',quoting=csv.QUOTE_NONE))
mp=list(csv.DictReader(open(f'{G}.map.tsv',encoding='utf-8'),delimiter='\t',quoting=csv.QUOTE_NONE))
tn=collections.Counter(r['name'] for r in todo); mn=collections.Counter(r['name'] for r in mp)
err=[]
for n in tn:
    if mn[n]!=1: err.append(('count',n,mn[n]))
for n in mn:
    if n not in tn: err.append(('extra',n))
dom={r['name']:r['domain'] for r in todo}
for r in mp:
    d=dom.get(r['name'])
    if d and r['seg'] not in V[d]['segs']: err.append(('seg',r['name'],r['seg']))
    if not r['kf'] or len(r['kf'].split())>3 or r['kf']!=r['kf'].lower(): err.append(('kf',r['name'],r['kf']))
print('errors',err); print(len(todo),len(mp)); print(collections.Counter(r['seg'] for r in mp).most_common())
