import sys,json
j=sys.argv[1]
t=open(f'/home/user/Possession-Taxonomy/rebuild/work/I1/prompts/{j}.txt').read()
i=t.index('YOUR SHELF'); k=t.index('Old data for this shelf')
print(t[i:k])
b=t[k:]; b=b[b.index('```json')+7:]; b=b[:b.index('```')]
for o in json.loads(b):
    print('##',o['target_kind'],'|',o['n'],'| s=',o.get('s'),'| t=',o.get('t'),'|a=',o.get('a'))
    print('  d:',o['d'])
    print('  m:','; '.join(f"{a} [{c}]" if c else a for a,c in o.get('m',[])))
    if o.get('r'): print('  r:',o['r'])
