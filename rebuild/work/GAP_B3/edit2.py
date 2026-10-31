import json,os
p='/home/user/Possession-Taxonomy/rebuild/out/B3_brands.json'
B=json.load(open(p))
for b in B['b']:
    if b['n']=='Anglepoise':
        b['d']=b['d'].rstrip('.')+'; owned by the Terry family.'
        b['s']='https://www.thembsgroup.co.uk/internal/anglepoise/'
    if b['n']=='Fritz Hansen':
        b['d']=b['d'].rstrip('.')+'; wholly owned by Chr. Augustinus Fabrikker through Skandinavisk Holding since 1 July 2025.'
        b['s']='https://www.interiordaily.com/article/9746637/fritz-hansen-is-fully-acquired-by-danish-investment-firm/'
json.dump(B,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
