import json,os,re
P='rebuild/out/B1.json'
d=json.load(open(P))
old="and Thonet, String and Muuto product designs (Thonet 404, String 403, Muuto page names families without designers)"
new="and Thonet and String product lists (Thonet's own pages 404; String's site returns 403 to WebFetch and is queued for Firecrawl); Muuto designs come from scandinaviandesign.com, which gives years for only three"
n=0
for dp in d['depts']:
    for sh in dp['s']:
        for k in sh['k']:
            x=k.get('x') or []
            if not x: continue
            s=k.get('sel','')
            s=s.replace(old,new)
            s=re.sub(r'Covers \d+ designs in this kind\.',f'Covers {len(x)} designs in this kind.',s)
            if any('ikeamuseum' in (e.get('s') or '') for e in x) and 'IKEA Museum' not in s:
                s+=" IKEA entries follow the IKEA Museum product-stories index, whose page lists stories to 2019 (no later ones shown); lamps, rugs, textiles, kitchens and tableware are out of scope here."
            if any('wikidata' in (e.get('s') or '') for e in x) and 'Wikidata maker' not in s:
                s+=" Wikidata items with a maker (furniture class, 208 rows read to the end) were checked."
            k['sel']=s; n+=1
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1);os.replace(P+'.tmp',P)
print(n)
