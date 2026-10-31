import json,os
p='rebuild/out/B5.json'
d=json.load(open(p))
W='https://en.wikipedia.org/wiki/'
new=[
("Val Saint Lambert","Belgium","1826","Lead crystal glassware maker at Seraing near Liège; the page gives 1826, with the site bought in 1825.",W+"Val_Saint_Lambert",None,None),
("Glasi Hergiswil","Switzerland","1817","Swiss glassworks in Nidwalden founded by the Siegwart brothers; visitors can watch the glass being made.",W+"Glasi_Hergiswil",None,None),
("Rona","Slovakia","1892","Lead-free crystal drinking glasses from Lednické Rovne, for households and catering.",W+"Rona_glassworks",None,None),
("Paşabahçe","Turkey","1935","Glassware, dishware and kitchen accessories maker founded in Beykoz and now a Şişecam company.",W+"Pa%C5%9Fabah%C3%A7e","Şişecam","National champion"),
("Borosil","India","1962","Indian maker of microwave-safe kitchenware and laboratory glass, mainly owned by the Kheruka family.",W+"Borosil",None,None),
("Mdina Glass","Malta","1968","Handmade glassware and paperweights, founded as Maltese Glass Industries by Michael Harris and Eric Dobson.",W+"Mdina_Glass",None,None),
]
for dp in d['depts']:
  for sh in dp['s']:
    for k in sh['k']:
      if k['n']=='Glassware house':
        have={e['n'] for e in k['x']}
        for n,c,y,dd,s,own,tier in new:
            if n in have: continue
            e={"n":n,"a":"","d":dd,"mk":"","y":y,"s":s,"v":[],"g":c,"cty":c}
            if own: e["own"]=own;e["tier"]=tier
            idx=max([i for i,x in enumerate(k['x']) if x['g']==c],default=None)
            if idx is None: k['x'].append(e)
            else: k['x'].insert(idx+1,e)
        k['sel']=k['sel'].split(' Covers 101 houses')[0].rstrip()+" Also read: the Wikipedia pages for the Belgian, Swiss, Slovak, Turkish, Indian and Maltese categories; Chinese and Bangladeshi, Azerbaijani and Japanese categories hold only industrial or art-glass firms (Liuli Gongfang is a studio, so visual art). Complete: %d of %d tableware and decorative makers on the Category:Glassmaking_companies tree by country, the defunct list and the Murano article; Czech Bohemia, Hungary and Spain are covered only through the pages those lists name."%(len(k['x']),len(k['x']))
json.dump(d,open(p+'.tmp','w'),ensure_ascii=False,indent=1);os.rename(p+'.tmp',p)
