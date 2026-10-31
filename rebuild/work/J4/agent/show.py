import sys,re,json
t=open(f'work/J4/prompts/{sys.argv[1]}.txt').read()
i=t.index('YOUR SHELF')
s=t[i:]
j=s.index('Old data for this shelf')
print(s[:j])
k=s.index('```json');e=s.index('```',k+7)
d=json.loads(s[k+7:e])
for x in d:
    print('##',x['target_kind'],'|',x['n'],'|',x.get('d'),'|',x.get('s'))
    print('; '.join(m[0] if not m[1] else m[0]+' ['+m[1]+']' for m in x['m']), '| R:', x.get('r'))
