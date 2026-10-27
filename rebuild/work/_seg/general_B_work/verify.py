import csv,json,collections
B='/home/user/Possession-Taxonomy/rebuild/work/_seg/'
voc=json.load(open(B+'../../SEGMENTS.json'))['domains']
todo=list(csv.DictReader(open(B+'general_B.todo.tsv',encoding='utf-8'),delimiter='\t'))
m=list(csv.DictReader(open(B+'general_B.map.tsv',encoding='utf-8'),delimiter='\t'))
tn=collections.Counter(r['name'] for r in todo); mn=collections.Counter(r['name'] for r in m)
assert tn==mn, (tn-mn, mn-tn)
dom={r['name']:r['domain'] for r in todo}
for r in m:
  assert r['seg'] in voc[dom[r['name']]]['segs'], r
  assert r['kf'] and r['kf']==r['kf'].lower() and 1<=len(r['kf'].split())<=3, r
print('OK',len(m)); print(collections.Counter(r['seg'] for r in m).most_common())
