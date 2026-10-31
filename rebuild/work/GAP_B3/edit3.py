import json,os
p='/home/user/Possession-Taxonomy/rebuild/out/B3_brands.json'
B=json.load(open(p))
for b in B['b']:
    if b['n']=='Foscarini':
        b['d']="Italian design-lighting maker, originally from Murano; an independent lighting house led by founder and president Carlo Urbinati."
        b['s']='https://www.homeaccentstoday.com/lighting/foscarini-acquires-german-lighting-maker-ingo-maurer'
    if b['n']=='Ingo Maurer':
        b['d']=b['d'].rstrip('.')+'; Foscarini bought 90% of the shares in May 2022 and Sarah Utermöhlen kept 10%.'
        b['s']=b.get('s') or 'https://www.homeaccentstoday.com/lighting/foscarini-acquires-german-lighting-maker-ingo-maurer'
json.dump(B,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
