import json,os
p='work/H3/shelves/05_02.json'
d=json.load(open(p))
ks={x['n']:x for x in d['kinds']}
def addm(kn,m):
    if m not in ks[kn]['m']: ks[kn]['m'].append(m)
addm('Restraint furniture',["The Tantra Chair","Zen By Design"])
addm('Sex swing',["Sex Swing Door Jam Kit","Sportsheets"])
have={b['n'] for b in d['brands']}
new=[
 {"n":"Zen By Design","c":"United States","f":"","seg":"Artisan & independent","kf":"Kama Sutra-inspired chairs","d":"Maker of The Tantra Chair, founded by AJ Vitaro, shipped worldwide.","s":"https://www.vice.com/en/article/sex-furniture-makers-liberator-ikea-hacks/"},
 {"n":"Sportsheets","c":"United States","f":"1993","seg":"Specialist","kf":"bondage and door swings","d":"Huntington Beach maker of bondage and sex products, including a door-mounted swing kit.","s":"https://en.wikipedia.org/wiki/Sportsheets_International,_Inc."},
]
for b in new:
    if b['n'] not in have: d['brands'].append(b)
d['notes']+=" Gap pass 2026-10-27: added Zen By Design (The Tantra Chair; Apartment Therapy via Firecrawl retry, and Vice) and Sportsheets (Sex Swing Door Jam Kit; The Skimm and Wikipedia) as makers beyond Liberator. A third maker (Shots, via a retailer listing) could not be retrieved."
json.dump(d,open(p+'.tmp','w'),ensure_ascii=False,indent=1)
os.replace(p+'.tmp',p)
