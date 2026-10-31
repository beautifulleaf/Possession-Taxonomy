import json,os
W='/home/user/Possession-Taxonomy/rebuild/work/GAP_A2/'
d=json.load(open(W+'A2.new.json')); B=json.load(open(W+'A2_brands.new.json'))
K={k['n']:k for dep in d['depts'] for sh in dep['s'] for k in sh['k']}
for e in K['Heritage running sneaker']['x']:
    if e['n']=='2002':
        e.update({'n':'2002','y':'2010','d':'High-performance New Balance running shoe, sold for a premium of US$250 on release.','s':'https://en.wikipedia.org/wiki/New_Balance_2002','v':[{'n':'2002R','mk':'New Balance','y':'2020','d':'Relaunch for the tenth anniversary, on the 860v2 sole'}]})
ox=K['Oxford']['x']
ox.append({'n':'Park Avenue','d':'Allen Edmonds cap-toe oxford dress shoe created in 1982.','mk':'Allen Edmonds','y':'1982','s':'https://investor.caleres.com/news/news-details/2022/An-Undeniable-Legacy-in-American-Hand-Crafted-Shoes-Allen-Edmonds-Marks-100-Years/default.aspx','v':[],'g':'United States · Allen Edmonds','own':'Caleres','tier':'Independent','cty':'United States','own_y':'2016'})
ox.append({'n':'City II','d':'John Lobb plain-toe ready-to-wear oxford on the 7000 last, introduced in 2007.','mk':'John Lobb','y':'2007','s':'https://openers.jp/en/fashion/fashion_men/796651','v':[],'g':'United Kingdom · John Lobb','own':'Hermès (Paris house, 1976); John Lobb Limited (London, family-owned)','tier':'Independent','cty':'United Kingdom','own_y':'1976'})
ox.sort(key=lambda e:(e.get('g',''), e.get('y') or '9999', e['n']))
K['Oxford']['sel']=K['Oxford']['sel'].replace('No complete list exists;','No complete list exists;',1)
b=K['Basketball sneaker']['sel'].replace(', Superstar, Forum)',', Superstar)'); K['Basketball sneaker']['sel']=b
old="Boot types come from Wikipedia's List of boots (all in-scope types for this kind held); makers' models follow the maker pages named on each entry. No complete list of makers' models exists."
for kn in ('Over-the-knee boot','Work boot','Combat & military boot','Cowboy boot','Equestrian riding boot'):
    K[kn]['sel']=K[kn]['sel'].replace(old,"Complete: all in-scope boot types of Wikipedia's List of boots are held (sport boots belong to E2). No complete list exists for makers' models; those follow the maker pages named on each entry.")
json.dump(d,open(W+'A2.final.json','w'),ensure_ascii=False,indent=1)
json.dump(B,open(W+'A2_brands.final.json','w'),ensure_ascii=False,indent=1)
