import json,os
R='/home/user/Possession-Taxonomy/rebuild/'
KEEP={'Royal Doulton','Swarovski','Lladro','Polaroid','Meissen','Goebel','Lumière','Fujifilm','D. Brucciani & Co.','Rookwood','Tiffany Studios','Walt Disney Productions','Platinotype Company','Bergmann','Leach Pottery','Wedgwood','Steuben','Gallé','Studio Ghibli','Watanabe Shōzaburō','Mourlot Studios','Universal Limited Art Editions','Gemini G.E.L.','Ilford','Capodimonte','Lomonosov Porcelain Factory','Beswick','Ralph Wood','Lalique','Daum','Lilliput Lane','Moorcroft','Grueby','Raku','Loetz','Gobelins','Papunya Tula','Buku-Larrnggay Mulka Centre','Injalak Arts','Tingatinga Arts Cooperative Society','Courvoisier Galleries','Warner Bros.','Tamarind Lithography Workshop','Currier and Ives','Pictures on Walls','Jean Saudé','Tyler Graphics','WPA Federal Art Project','King & McGaw','Nash Editions','James Ambrose Cutting','Hamilton L. Smith','V. M. Griswold','Ciba-Geigy','Impossible Project','Nymphenburg','Herend','Bing & Grøndahl','Wade Ceramics','Manufaktur Rödental','Hummel Manufaktur','Enesco','Enoch Wood','Baccarat','Kosta Boda','Royal Selangor','Demdaco','David Winter','Martin Brothers','Venini','Morris & Co.','Dovecot Studios','Vatican Mosaic Studio','Precious Moments','Nishimuraya Yohachi','Hōeidō','Real Academia de Bellas Artes de San Fernando','Ellis and Green','Etling','Les Neveux de J. Lehmann','Barbedienne','Rudier','Valsuani','Hébrard','Gladenbeck','Factory Additions','Da Capo Press','Heritage Auctions','Hans P. Kraus Jr.','Goldscheider','Royal Crown Derby','IKEA','Desenio','Society6','Sunday B. Morning','Harry Clarke Studios','Magnum Photos','Royal Copenhagen','Bing & Grøndahl','Fiskars','PHI Industrial Acquisitions','Free State of Saxony'}
d=json.load(open(R+'out/F2.json')); ve=json.load(open(R+'work/V4_F2/ve_names.json'))
cnt=0
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            for x in k.get('x',[]):
                if x.get('mk') and x['mk'] not in KEEP:
                    k.setdefault('ve',[]).append(x['mk']); x['mk']=''
                if x.get('v'):
                    nv=[v for v in x['v'] if not v.get('mk') or v['mk'] in KEEP]
                    for v in x['v']:
                        if v not in nv: k.setdefault('ve',[]).append(v['mk']+': '+v['n']); cnt+=1
                    if nv: x['v']=nv
                    else: x.pop('v')
            if k.get('ve'): k['ve']=sorted(set(k['ve']))
b=json.load(open(R+'out/F2_brands.json'))
rem=[x['n'] for x in b['b'] if x['n'] not in KEEP]
b['b']=[x for x in b['b'] if x['n'] in KEEP]
seg=next(x['seg'] for x in b['b'] if x['n']=='Royal Doulton')
have={x['n'] for x in b['b']}
W='https://en.wikipedia.org/wiki/'
new=[("Hummel Manufaktur","Germany","","Maker of Hummel figurines in Rödental; bought by Bernd Foertsch after its 2017 bankruptcy.",W+'Hummel_figurines'),
("Fiskars","Finland","1649","Finnish listed company that bought Royal Copenhagen from Axcel in December 2012.",W+'Royal_Copenhagen'),
("PHI Industrial Acquisitions","","","Took a majority stake in the Lladró Group in 2016.",W+'Lladr%C3%B3'),
("Free State of Saxony","Germany","","Sole owner of Staatliche Porzellan-Manufaktur Meissen.",W+'Meissen_porcelain')]
for n,c,f,dd,s in new:
    if n not in have: b['b'].append({"n":n,"c":c,"f":f,"seg":seg,"kf":"owner","d":dd,"s":s})
for fn,o in (('F2.json',d),('F2_brands.json',b)):
    t=R+'out/'+fn+'.tmp'; json.dump(o,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,R+'out/'+fn)
json.dump({'removed_versions':cnt,'removed_register':rem},open(R+'work/V4_F2/ve_register.json','w'),ensure_ascii=False,indent=1)
print(cnt,len(rem),len(b['b']))
