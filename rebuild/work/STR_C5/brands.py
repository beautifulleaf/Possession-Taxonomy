import json,os
R='/home/user/Possession-Taxonomy/rebuild/'
b=json.load(open(R+'work/STR_C5/bak/C5_brands.json'))
drop={'Waterman ink','J. Herbin Encre','Oblique pen holder','Coloured ink stick','Herbin brass wax seal','J. Herbin sealing wax'}
for x in b['b']:
    x['sig']=['Atoma disc-bound system' if s=='Disc-bound notebook' else s for s in x.get('sig',[]) if s not in drop]
    if x['n']=='Olivetti' and 'Olivetti Tes 501' not in x['sig']: x['sig'].append('Olivetti Tes 501')
    if x['n']=='Smith Corona' and 'Smith-Corona Coronamatic' not in x['sig']: x['sig'].append('Smith-Corona Coronamatic')
    if x['n']=='IBM' and 'IBM Electromatic Model 04' not in x['sig']: x['sig'].append('IBM Electromatic Model 04')
TW='https://en.wikipedia.org/wiki/Typewriter'
b['b'].append({'n':'Rasmus Malling-Hansen','c':'Denmark','f':'','seg':'Heritage manufactory','kf':'writing ball','d':'Danish pastor who invented the Hansen Writing Ball, the first commercially sold typewriter, in 1865.','lines':[],'eras':[],'sig':['Hansen Writing Ball'],'sc':[],'rel':[],'s':'https://en.wikipedia.org/wiki/Hansen_Writing_Ball'})
b['b'].append({'n':'Hammond Typewriter Company','c':'United States','f':'','seg':'Heritage manufactory','kf':'curved-keyboard typewriters','d':'Maker of the Hammond typewriter, with a curved keyboard and interchangeable type sectors, released in 1884.','lines':[],'eras':[],'sig':['Hammond Typewriter'],'sc':[],'rel':[],'s':TW})
p=R+'out/C5_brands.json.tmp'; json.dump(b,open(p,'w'),ensure_ascii=False,indent=1); os.replace(p,R+'out/C5_brands.json')
print(len(b['b']))
