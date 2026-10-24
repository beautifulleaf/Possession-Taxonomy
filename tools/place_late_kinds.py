"""Place stored kinds missing from their category's display groups into the group of a leaf sibling (session 9).
usage (from the repo root): python3 tools/place_late_kinds.py BATCH CODE[,CODE...]  -> verify/out/BATCH_groups_changes.tsv, then tools/apply_groups_changes.py BATCH"""
import sys; sys.path.insert(0,'tools')
from common import read_tsv, write_tsv
b=sys.argv[1]; codes=sys.argv[2].split(',')
G=read_tsv('framework/structure/navigation/groups.tsv'); K=read_tsv('data/kinds.tsv')
mem={}
for g in G:
    for m in g['members'].split('; '):
        if m: mem[m]=g
out={}
for k in K:
    if k['code'] not in codes or k['kind_id'] in mem: continue
    leaf=k['leaf'] or k['sub_family']
    sib=[x for x in K if (x['leaf'] or x['sub_family'])==leaf and x['kind_id'] in mem]
    if not sib: print('no sibling group:',k['kind_id'],k['name']); continue
    g=mem[sib[0]['kind_id']]
    out.setdefault(g['group_id'],dict(code=g['code'],group_id=g['group_id'],action='move_members',group_name=g['group_name'],level=g['level'],parent_group=g['parent_group'],members=[],reason='kind attested after the group pass; placed with its leaf siblings'))['members'].append(k['kind_id'])
rows=[dict(r,members='; '.join(r['members'])) for r in out.values()]
if rows: write_tsv(f'verify/out/{b}_groups_changes.tsv',rows,list(rows[0].keys()))
print(sum(len(r['members'].split('; ')) for r in rows),'placed')
