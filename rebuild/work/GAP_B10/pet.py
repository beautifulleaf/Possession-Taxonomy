import json,os
p='out/B10.json'
d=json.load(open(p))
T='https://truthaboutpetfood.com/2024-us-pet-food-sales/'
def allk():
    for dp in d['depts']:
        for s in dp.get('s',[]):
            for k in s.get('k',[]): yield dp,k
def upd(name,**kw):
    n=0
    for dp,k in allk():
        for e in k.get('x',[]):
            if e['n']==name or e.get('mk')==name and e['n']==name:
                e.update(kw); n+=1
    assert n,name
upd('Royal Canin',cty='France',y='1968',own_y=2002)
upd('Iams',cty='United States',own_y=2014)
upd('Whiskas',cty='United States',own_y=1968)
upd('Friskies',cty='United States',y='1934')
ind=[('Diamond Pet Foods','Diamond','1.5 billion'),('Wellness','Wellness Pet Company','700 million'),('Instinct','Instinct','200 million'),
('Redbarn','Redbarn Pet Products','168 million'),('Solid Gold','Solid Gold Pet','105 million'),('Primal','Primal Pet Group','95.3 million'),
('Natural Balance','Natural Balance Pet Foods','74.3 million'),("Stella & Chewy's","Stella & Chewy's",'52.4 million'),('The Honest Kitchen','The Honest Kitchen','45 million'),
('Halo','Halo, Purely for Pets','41.11 million'),('JustFoodForDogs','JustFoodForDogs','40 million'),('Weruva','Weruva Pet Foods','30.4 million'),
('Bil-Jac','Bil-Jac Foods','22.1 million'),('Canidae','Canidae Pet Foods','20.6 million'),("Evanger's","Evanger's Dog & Cat Food Co. Inc",'18 million'),
('Canine Caviar','Canine Caviar','14.65 million'),('Health Extension','Health Extension Pet Care','5.6 million')]
dogfood=next(k for dp,k in allk() if k['n']=='Dog food')
have={e['n'] for e in dogfood['x']}
for n,own,rev in ind:
    if n in have: continue
    dogfood['x'].append({"n":n,"a":"","d":f"Pet food brand of an independent US company that Truth About Pet Food lists with 2024 sales of US${rev}.","mk":n,"y":"","s":T,"g":"Independent","own":own,"tier":"Independent"})
dogs=d['depts'][0]
for who,rev in [('Nestlé Purina PetCare','US$22.4 billion'),('Mars Petcare','US$22 billion'),("Hill's Pet Nutrition",'US$4.4 billion'),('General Mills','US$2.3 billion'),('Diamond Pet Foods','US$1.5 billion'),('Freshpet','US$975 million'),('Wellness Pet Company','US$700 million')]:
    dogs['ms'].append({"mkt":"United States pet food company sales","who":who,"share":rev,"yr":2024,"s":T,"note":"company sales as Truth About Pet Food lists them; owner and brand columns not given"})
cats=("Dog food","Dog treats","Dry cat food","Wet cat food","Fresh, frozen and raw cat food","Veterinary cat food","Cat treats","Cat litter")
tot=sum(len(k['x']) for dp,k in allk() if k['n'] in cats)
for dp,k in allk():
    if k['n'] in cats:
        k['sel']=k['sel'].split(' Covers 47')[0]+f" Covers {tot} brands across the pet-food kinds: the Mars, Purina and Smucker brand pages, Hill's and Blue Buffalo, and 17 independent US companies from Truth About Pet Food's 2024 sales list. Not listed: the Latin American and other national champions (the Petfood Industry lists returned 403 and are queued for Firecrawl), multi-brand companies on the sales list with no stated consumer brand (Simmons, Spectrum, Alphia, Sunshine Mills, Tuffy's and others), and Mars and Purina brands whose kind could not be fetched. No complete list of pet-food brands exists."
        k['sel']=k['sel'].replace("Covers "+str(tot)+" brands","Covers "+str(tot)+" of about 100 brands")
json.dump(d,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.rename(p+'.tmp',p)
print(tot)
