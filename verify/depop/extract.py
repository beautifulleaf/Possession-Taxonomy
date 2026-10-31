"""Pull the owner's pasted Depop letter pages out of the session transcript into verify/depop/<letter>.txt.
Usage: python3 extract.py <transcript.jsonl>"""
import json,re,sys,os
OUT='/home/user/Possession-Taxonomy/verify/depop/'
seen={}
for line in open(sys.argv[1]):
    try: o=json.loads(line)
    except Exception: continue
    if o.get('type')!='user': continue
    c=o.get('message',{}).get('content')
    texts=[c] if isinstance(c,str) else [x.get('text','') for x in (c or []) if isinstance(x,dict) and x.get('type')=='text']
    for t in texts:
        names=re.findall(r'^\* \[(.+?)\]\(https://www\.depop\.com/brands/([^)]*)\)',t,re.M)
        if len(names)<20: continue
        head=t.strip().split('\n')[0].strip()
        letter=head.lower() if re.fullmatch(r'[A-Za-z]|other|0-9',head) else names[0][1][0].lower()
        if letter=='0-9': letter='other'
        seen[letter]=names
for letter,names in seen.items():
    out=[]; s=set()
    for n,slug in names:
        if n not in s: s.add(n); out.append(n)
    open(OUT+letter+'.txt','w').write('\n'.join(out)+f'\n#END {len(out)}\n')
    print(letter,len(names),'unique',len(out))
