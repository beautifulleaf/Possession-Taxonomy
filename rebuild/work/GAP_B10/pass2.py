import json,os
p='out/B10.json'
d=json.load(open(p))
def ks():
    for dp in d['depts']:
        for s in dp.get('s',[]):
            for k in s.get('k',[]): yield k
def upd(n,**kw):
    c=0
    for k in ks():
        for e in k.get('x',[]):
            if e['n']==n: e.update(kw); c+=1
    assert c,n
upd('Orijen',cty='Canada',y='2005',own_y=2023)
upd('Nutro',cty='United States',y='1926',own_y=2007)
upd('Eukanuba',cty='United States',own_y=2014)
upd('Sheba',cty='Germany')
upd('Alpo',cty='United States',y='1936',own_y=1995)
upd('Beneful',y='2001')
upd('Felix',cty='United Kingdom')
upd('Wellness',own='Clearlake Capital Group L.P.',own_y=2020,cty='United States',y='1926')
upd('Natural Balance',own='Nexus Capital Management LP',own_y=2021,cty='United States',y='1989')
upd('Instinct',own='Agrolimen',own_y=2016,cty='United States',y='2005')
for k in ks():
    for e in k.get('x',[]):
        if e['n'] in('Wellness','Natural Balance','Instinct'):
            e['d']={'Wellness':'Natural pet food brand of the Wellness Pet Company, bought by Clearlake Capital in November 2020; the company dates from Old Mother Hubbard (1926).',
            'Natural Balance':'Pet food brand founded in 1989 by Dick Van Patten; J.M. Smucker sold it to Nexus Capital in 2021.',
            'Instinct':'Pet food brand of Nature\'s Variety (St. Louis), wholly owned by the Spanish company Agrolimen since 2016.'}[e['n']]
dogfood=next(k for k in ks() if k['n']=='Dog food')
have={e['n'] for e in dogfood['x']}
def ent(n,d_,s,g,own,tier,cty,y='',own_y=None):
    e={"n":n,"a":"","d":d_,"mk":n,"y":y,"s":s,"g":g,"own":own,"tier":tier,"cty":cty}
    if own_y: e["own_y"]=own_y
    return e
new=[
ent('Monge','Italian pet food maker, the largest in Italy by revenue; revenue about EUR 513 million in 2023.','https://it.wikipedia.org/wiki/Monge_(azienda)','National champions','Monge & C. S.p.A.','National champion','Italy','1963'),
ent('Drools','Indian pet food brand holding about 40 % of the domestic market; Nestlé took a minority stake.','https://globalpetindustry.com/news/interview-drools-targets-european-push-after-reaching-scale-in-india/','National champions','Drools','National champion','India'),
ent('Advance','Pet food brand of the Spanish company Affinity Petcare, sixth largest pet food company worldwide per Spanish Wikipedia.','https://es.wikipedia.org/wiki/Affinity_Petcare','Independent','Affinity Petcare (Agrolimen)','Independent','Spain'),
ent('Brekkies','Pet food brand of the Spanish company Affinity Petcare.','https://es.wikipedia.org/wiki/Affinity_Petcare','Independent','Affinity Petcare (Agrolimen)','Independent','Spain'),
ent('Ultima','Pet food brand of the Spanish company Affinity Petcare.','https://es.wikipedia.org/wiki/Affinity_Petcare','Independent','Affinity Petcare (Agrolimen)','Independent','Spain'),
ent('Vitakraft','German umbrella brand with about 2,000 products for birds, rodents, dogs and cats; part of Tiernahrung Deuerer since 2013.','https://de.wikipedia.org/wiki/Vitakraft','Independent','Tiernahrung Deuerer','Independent','Germany','1837',2013),
ent('animonda','German premium pet food brand of the Heristo group, fully owned by the Risken family.','https://de.wikipedia.org/wiki/Heristo','Independent','Heristo','Independent','Germany'),
ent('Forthglade','British natural pet food brand from Okehampton, Devon; IK Investment Partners took a majority stake in 2020.','https://globalpetindustry.com/news/ik-investment-partners-acquires-forthglade-uk/','Independent','Forthglade Foods Limited','Independent','United Kingdom','1971'),
ent("Butcher's","British pet food brand of Butcher's Pet Care, acquired by Inspired Pet Nutrition in a deal announced in August 2024.",'https://globalpetindustry.com/news/inspired-pet-nutrition-acquires-butchers-pet-care/','Independent','Inspired Pet Nutrition','Independent','United Kingdom','','2024'),
ent('Gambol','Chinese pet food company founded in 2006 with proprietary brands, listed on the Shenzhen exchange in August 2023.','https://globalpetindustry.com/news/gambol-pet-largest-public-pet-company-china/','Independent','Gambol Pet Group','Independent','China','2006'),
ent('Lyka','Australian direct-to-consumer fresh dog food company founded in 2018.','https://en.wikipedia.org/wiki/Lyka_(company)','Independent','Lyka','Independent','Australia','2018'),
]
for e in new:
    if e['n'] not in have: dogfood['x'].append(e)
dogs=d['depts'][0]
ms=[("Italian pet food","Monge & C. S.p.A.","EUR 513 million revenue",2023,'https://it.wikipedia.org/wiki/Monge_(azienda)',"largest Italian pet food company by revenue, per the page"),
("Indian pet food","Drools","about 40 % of the domestic market",None,'https://globalpetindustry.com/news/interview-drools-targets-european-push-after-reaching-scale-in-india/',"company figure as the article states it; year not stated; Nestlé holds a minority stake"),
("Spanish and world pet food","Affinity Petcare","sixth largest pet food company worldwide",None,'https://es.wikipedia.org/wiki/Affinity_Petcare',"ranking as stated on the page, no year")]
for mk,who,share,yr,s,note in ms:
    m={"mkt":mk,"who":who,"share":share,"s":s,"note":note}
    if yr: m["yr"]=yr
    dogs['ms'].append(m)
cats=("Dog food","Dog treats","Dry cat food","Wet cat food","Fresh, frozen and raw cat food","Veterinary cat food","Cat treats","Cat litter")
tot=sum(len(k['x']) for k in ks() if k['n'] in cats)
import re
for k in ks():
    if k['n'] in cats:
        k['sel']=re.sub(r"Lists \d+ brands",f"Lists {tot} brands",k['sel'])
        k['sel']+=" National champions found on fetched pages: Italy (Monge), India (Drools), with Spain (Affinity), Germany (Vitakraft, animonda), the United Kingdom (Forthglade, Butcher's), China (Gambol) and Australia (Lyka) as independents. Searched without a fetched source for Brazil, Mexico, Argentina, France, Poland, Japan, Thailand, South Africa, Turkey and Russia: market-share pages returned 403 or named no brands."
json.dump(d,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.rename(p+'.tmp',p)
print(tot)
