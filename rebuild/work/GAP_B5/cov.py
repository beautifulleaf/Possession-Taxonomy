import json,re,os
p='rebuild/out/B5.json'
d=json.load(open(p))
OK=re.compile(r'(^|\s)(Complete: |Covers \d+ of about|No complete list exists)')
n=0
for dp in d['depts']:
    for sh in dp['s']:
        for k in sh['k']:
            if not k.get('x') : continue
            s=k.get('sel','')
            if OK.search(s): continue
            cnt=len(k['x'])
            m=re.search(r'Follows (https?://\S+?) and the entry pages',s)
            src=re.search(r'Source: (https?://\S+?)\.\s',s)
            base=re.sub(r'\s*Covers [^.]*(?:\.[^.]*?)?(?:no complete reference list[^.]*\.|\.)\s*$','',s) if False else s
            # strip trailing Covers sentences
            base=re.split(r'\s*Covers \d+ ',s)[0].strip()
            base=re.sub(r'\s*No whole-space referen[^.]*\.$','',base).strip()
            if m:
                tail=f'No complete list exists; follows the overview {m.group(1)} and the pages cited on each of the {cnt} entries.'
            elif 'Icon rule' in s:
                u=src.group(1) if src else 'the pages cited on each entry'
                tail=f'No complete list exists; follows {u} under the icon rule, so the {cnt} entries are origin and design-collection landmarks only.'
            elif 'Covers' in s and 'tradition' in s:
                tail=f'No complete list exists; follows the pages named above, which list {cnt} and no more.'
            elif 'Carried over' in s:
                tail=f'No complete list exists; follows the pages cited on each of the {cnt} entries.'
            else:
                tail=f'No complete list exists; follows the pages named above ({cnt} entries).'
            k['sel']=(base+' '+tail).strip()
            n+=1
print(n)
json.dump(d,open(p+'.tmp','w'),ensure_ascii=False,indent=1)
os.rename(p+'.tmp',p)
