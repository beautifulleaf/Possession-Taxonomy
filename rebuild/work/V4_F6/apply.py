import json,re,os
p='../../out/F6.json'
d=json.load(open(p))
REF={'handbookofmineralogy.org':'the Handbook of Mineralogy sheet for the species','wikipedia.org':'the Wikipedia article for the species','minerals.net':'the minerals.net gallery','gia.edu':'the GIA gem encyclopedia','fossilera.com':'the Fossilera catalogue','skullsunlimited.com':'the Skulls Unlimited catalogue','boneclones.com':'the Bone Clones catalogue','luciteria.com':'the Luciteria catalogue'}
NL={
'Minerals: non-silicates':'One entry is a classic collector occurrence of the species (a locality, habit or trade name); sizes and matrix are details.',
'Minerals: silicates':'One entry is a classic collector occurrence of the species (a locality, habit or trade name); sizes and matrix are details.',
'Gemstones & pearls':'One entry is a named gem variety or trade type of the stone; cut, carat weight and treatment are details.',
'Fossils & amber':'One entry is a named taxon or fossil locality collected under its own name; size, prep and completeness are details.',
'Meteorites & impact glass':'One entry is a named fall, find or strewn field; specimen type and weight are details.',
'Rocks & teaching sets':'One entry is a named rock type or locality stone; size and polish are details.',
'Shells & coral':'One entry is a species or form collected under its own name; grade and size are details.',
'Taxidermy, bones & preserved specimens':'One entry is a named kind of specimen or maker of casts; mount, size and condition are details.',
'Element samples':'One entry is a named element-sample series; purity and mass are details.',
'Display domes & stands':'One entry is a named type of display case.'}
removed=0;kinds=0;ex=[]
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            if 'm' in k:
                removed+=len(k['m']); ex.append((dp['n'],k['n'],len(k['m'])))
                del k['m']
            if k.get('x'):
                ds=[]
                for x in k['x']:
                    h=re.sub(r'https?://(www\.)?([^/]+)/.*',r'\2',x.get('s',''))
                    for key,v in REF.items():
                        if h.endswith(key) and v not in ds: ds.append(v)
                k['nl']=NL[dp['n']]
                k['sel']=('Follows '+' and '.join(ds) if ds else 'Follows the cited page')+'. No complete list of every occurrence exists in one reference, so entries are those these pages name; localities and forms they do not name are left out.'
                kinds+=1
json.dump(d,open(p+'.tmp','w'),ensure_ascii=False,indent=1)
os.replace(p+'.tmp',p)
print(removed,kinds)
json.dump(ex,open('removed_m.json','w'))
