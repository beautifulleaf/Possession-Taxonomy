import sys,re,json
t=open(f'work/J4/prompts/{sys.argv[1]}.txt').read()
i=t.index('```json\n')+8; j=t.index('\n```',i)
for k in json.loads(t[i:j]):
    print(k['target_kind'],'|',k.get('d'),'|',k.get('s'),'|M:',', '.join(a if not b else a+' ('+b+')' for a,b in k['m']),'|R:',k['r'])
