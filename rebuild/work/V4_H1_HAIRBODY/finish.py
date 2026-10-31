import json,re,subprocess
R='/home/user/Possession-Taxonomy/rebuild/'
st=json.load(open(R+'work/V4_H1_HAIRBODY/stage1.json'))
U=__import__('sys').path.insert(0,R+'work/V4_H1_HAIRBODY')
from data import U
SEC=U['SEC'];BM=U['BM']
PG=U['PGARS'];GD=U['GD'];RP=U['RP']
def pg(m,share,note=''): return {"mkt":m,"who":"Procter & Gamble","share":share,"yr":2026,"s":PG,"note":("fiscal year ended June 2026, company statement; "+note).strip('; ')}
MS={'Oral care':([
 {"mkt":"Global toothpaste","who":"Colgate-Palmolive","share":"41.1 %","yr":2023,"s":SEC,"note":"year to date, company statement based on third-party data and internal estimates"},
 {"mkt":"Global manual toothbrushes","who":"Colgate-Palmolive","share":"31.5 %","yr":2023,"s":SEC,"note":"year to date, company statement"},
 {"mkt":"US toothpaste","who":"Colgate-Palmolive","share":"33.7 %","yr":2023,"s":SEC,"note":"year to date, dollar sales, company statement"},
 {"mkt":"US manual toothbrushes","who":"Colgate-Palmolive","share":"41.1 %","yr":2023,"s":SEC,"note":"year to date, company statement"},
 pg("Global oral care","nearly 30 %","behind Crest and Oral-B"),
 {"mkt":"Global electric toothbrushes","who":"Philips Oral Healthcare","share":"39.8 %","yr":2024,"s":RP,"note":"Report Prime ranking from revenue estimates; method not stated, treat as indicative"},
 {"mkt":"Global electric toothbrushes","who":"Procter & Gamble (Oral-B)","share":"30.8 %","yr":2024,"s":RP,"note":"same ranking"},
 {"mkt":"Global electric toothbrushes","who":"Colgate-Palmolive","share":"8.2 %","yr":2024,"s":RP,"note":"same ranking"},
 {"mkt":"Global electric toothbrushes","who":"Panasonic Healthcare","share":"4.8 %","yr":2024,"s":RP,"note":"same ranking"},
 {"mkt":"Global electric toothbrushes","who":"FOREO","share":"3.9 %","yr":2024,"s":RP,"note":"same ranking"},
 {"mkt":"Global electric toothbrushes","who":"Waterpik","share":"3.0 %","yr":2024,"s":RP,"note":"same ranking"},
 {"mkt":"China toothpaste","who":"Yunnan Baiyao","share":"fifth by sales revenue (500 million yuan)","yr":2008,"s":U['YB'],"note":"Wikipedia marks this claim as needing a citation"}],
 "Colgate-Palmolive states it leads toothpaste and manual toothbrushes worldwide and in the United States (2023 year to date); P&G puts its own oral care at nearly 30 % worldwide (fiscal 2026). Electric-toothbrush shares come from one third-party ranking. No fetched page gave shares for the UK, Japan, India, Brazil, Germany or France."),
 'Shaving & hair removal':([
 {"mkt":"US razor and blade market","who":"Gillette (Procter & Gamble)","share":"47.3 %","yr":2018,"s":BM,"note":"Euromonitor figure quoted in a May 2019 article, 'last year'; about 70 % in 2010"},
 {"mkt":"US razor and blade market","who":"Edgewell top brands (Schick, Wilkinson Sword)","share":"13.6 %","yr":2018,"s":BM,"note":"same article; year not stated, taken as 2018"},
 {"mkt":"US razor and blade market","who":"Dollar Shave Club","share":"8.5 %","yr":2018,"s":BM,"note":"same article; year not stated, taken as 2018"},
 {"mkt":"US razor and blade market","who":"Harry's","share":"2.6 %","yr":2018,"s":BM,"note":"same article; year not stated, taken as 2018"},
 pg("Global grooming","more than 50 %"),
 pg("Global blades and razors","more than 60 %","behind Gillette and Venus"),
 pg("Global male electric shavers","nearly 30 %","sold under Braun")],
 "Gillette still leads US razors but fell from about 70 % in 2010 to 47.3 % in 2018, as direct-to-consumer brands took share. P&G reports more than 60 % of blades and razors worldwide and nearly 30 % of male electric shavers (fiscal 2026). No fetched page gave shares outside the United States, or for hair dryers and clippers."),
 'Hair':([
 pg("Global retail hair care","about 20 %","behind Head & Shoulders and Pantene"),
 {"mkt":"Western Europe hair care","who":"L'Oréal","share":"26.5 %","yr":2020,"s":GD,"note":"value share, GlobalData summary"},
 {"mkt":"Western Europe hair care","who":"Henkel","share":"13.5 %","yr":2020,"s":GD,"note":"value share, GlobalData summary"},
 {"mkt":"Western Europe hair care","who":"Procter & Gamble","share":"10.2 %","yr":2020,"s":GD,"note":"value share, GlobalData summary"},
 {"mkt":"Western Europe hair care","who":"Coty","share":"7.4 %","yr":2020,"s":GD,"note":"value share, GlobalData summary"},
 {"mkt":"Western Europe hair care","who":"Unilever","share":"6.9 %","yr":2020,"s":GD,"note":"value share, GlobalData summary"}],
 "P&G holds about 20 % of retail hair care worldwide (fiscal 2026); in Western Europe L'Oréal led with 26.5 % in 2020. No fetched page gave hair-care shares for the US, UK, Japan, China, India, Brazil or Germany, or for hair dryers and stylers."),
 'Bath, body & hygiene':([
 pg("Global personal care (deodorant and body care)","about 20 %","number two position, behind Old Spice, Native, Secret and Safeguard"),
 pg("Global feminine care","nearly 30 %"),
 pg("Global menstrual care","nearly 35 %","behind Always and Tampax"),
 pg("Global baby care (diapers and wipes)","more than 30 %","behind Pampers")],
 "P&G reports about 20 % of global personal care, nearly 35 % of menstrual care and more than 30 % of baby care (fiscal 2026). No fetched page gave soap, body-wash or deodorant shares for other companies or national markets."),
 'Comfort & massage':([],"Massage and warmth devices are sold by device makers, not by the global groups, and no fetched page gave a market share.")}
depts=st['depts']
for d in depts:
    ms,sm=MS[d['n']]; d['ms']=ms; d['msum']=sm
    d['note']=(d.get('note','')+' ' if d.get('note') else '')+'Brands lead on the first shelf; powered devices and tools list maker lines with models as versions.' if d['n']!='Comfort & massage' else d.get('note','')
    for s in d['s']:
        for k in s['k']:
            for x in k.get('x',[]) or []:
                x.setdefault('a',''); x.setdefault('y','')
                if x.get('tier')=='' : x.pop('tier')
                if x.get('own')=='' : x.pop('own',None);x.pop('tier',None);x.pop('own_y',None);x.pop('cty',None)
                for f in ('own_y','cty'):
                    if f in x and not x[f]: x.pop(f)
for d in depts:
    for sh in d['s']:
        for k in sh['k']:
            for x in k.get('x',[]) or []:
                x['d']=x['d'].replace(' is a oral-care',' is an oral-care')
                vs=x.get('v') or []
                same=[v for v in vs if v['n'].lower()==x['n'].lower()]
                for v in same:
                    if ' brand' in x['d'] and (' of ' in x['d'] or 'no fetched' in x['d']) and v.get('d'): x['d']=v['d']
                    if v.get('y') and not x.get('y'): x['y']=v['y']
                    vs.remove(v)
                if 'v' in x and not x['v']: x.pop('v')
part={"replaces":["Hair","Shaving & hair removal","Oral care","Bath, body & hygiene","Comfort & massage"],"depts":depts,"brands":[],"brand_updates":{},"renames":{},"moves":[]}
# brand register
reg=json.load(open(R+'out/H1_brands.json'))['b']
have={b['n'].lower():b for b in reg}
allb=json.load(open(R+'work/V4_H1_HAIRBODY/brands_all.json'))
owners={}
for e in allb:
    low=e['n'].lower()
    if e.get('own'): owners.setdefault(e['own'],e['s'])
    if low in have:
        if e.get('own'): part['brand_updates'][have[low]['n']]={'own':e['own'],'tier':e.get('tier',''),'c':e.get('cty','')}
    else:
        part['brands'].append({'n':e['n'],'c':e.get('cty',''),'f':'','seg':'','d':e['d'],'s':e['s']})
        have[low]=1
for o,s in owners.items():
    if o.lower() not in have:
        part['brands'].append({'n':o,'c':'','f':'','seg':'','d':'Owner company named on a fetched brand page.','s':s}); have[o.lower()]=1
import os
os.makedirs(R+'out/H1_parts',exist_ok=True)
json.dump(part,open(R+'out/H1_parts/HAIRBODY.json','w'),ensure_ascii=False,indent=1)
print(os.path.getsize(R+'out/H1_parts/HAIRBODY.json'),len(part['brands']),len(part['brand_updates']))
