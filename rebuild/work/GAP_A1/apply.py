import json,os
R='/home/user/Possession-Taxonomy/rebuild/out/'
def load(f): return json.load(open(R+f))
def save(f,o):
    json.dump(o,open(R+f+'.tmp','w'),ensure_ascii=False); os.replace(R+f+'.tmp',R+f)
B=load('A1_brands.json'); bm={x['n']:x for x in B['b']}
def upd(n,**kw):
    if n in bm: bm[n].update(kw)
    else:
        x={'n':n,'c':'','f':'','seg':'','d':'','lines':[],'eras':[],'sig':[],'sc':[],'rel':[],'kf':''}; x.update(kw); B['b'].append(x); bm[n]=x
W='https://en.wikipedia.org/wiki/'
upd('Brooks Brothers',own='Authentic Brands Group',tier='Global group',own_y=2020,s=W+'Brooks_Brothers')
upd('J.Crew',own='Anchorage Capital Group and Leonard Green & Partners',tier='Independent')
upd('Supreme',own='EssilorLuxottica',tier='Global group',own_y=2024)
upd('Fila',own='Misto Holdings',tier='Independent')
upd('Russell Athletic',own='Berkshire Hathaway (via Fruit of the Loom)',tier='Global group',own_y=2006)
upd('Dickies',own='Bluestar Alliance',tier='Independent',own_y=2025)
upd('Lee',own='Kontoor Brands',tier='Independent',own_y=2019)
upd('Sergio Tacchini',own='Billy Ngok',tier='Independent',own_y=2008)
upd('Lewis Leathers',own='Saaya Harris Nohara',tier='Independent')
upd('Hestra',own='Magnusson family',tier='Independent')
upd('Dockers',own='Authentic Brands Group',tier='Global group',own_y=2025)
upd('Shanghai Tang',own='UTAN Group',tier='Independent',own_y=2020)
upd('Eres',own='Chanel',tier='Global group')
upd('J. Press',own='Onward Kashiyama',tier='Independent',own_y=1986)
upd('Bean Pole',own='Samsung C&T Fashion Group',tier='National champion',s='https://www.koreatimes.co.kr/business/companies/20220625/legacy-fashion-brands-overshadowed-by-sportswear-luxury-goods-makers')
upd('Hazzys',c='South Korea',seg='Contemporary & premium',own='LF',tier='Independent',s='https://www.koreatimes.co.kr/business/companies/20220625/legacy-fashion-brands-overshadowed-by-sportswear-luxury-goods-makers')
upd('Matahari',c='Indonesia',f='1958',seg='High street',d='Indonesian department store chain founded by Hari Darmawan; described as the largest retail platform in Indonesia.',own='Auric Digital Retail',own_y=2021,tier='National champion',s=W+'Matahari_(department_store)')
for n in ['SUKO','ZES','Nevada','Connexion','COLE','Little M']:
    upd('Matahari '+n if n in('Nevada',) else n,c='Indonesia',seg='High street',d='Private label sold only through Matahari.',own='Matahari',tier='Own label',s=W+'Matahari_(department_store)')
upd('Alhokair',c='Saudi Arabia',f='1989',seg='High street',d='Saudi franchise retailer (Fawaz Abdulaziz Alhokair Group) holding local rights to Zara, Banana Republic, Gap, Nine West and Topshop; Arab News calls it Saudi Arabia\'s biggest retail franchise group.',own='Fawaz Abdulaziz Alhokair Group',tier='National champion',s='https://www.arabnews.com/business/pandemic-closes-stores-at-saudi-arabias-biggest-retail-franchise-group-1698231')
upd('Mitra Adiperkasa',c='Indonesia',seg='High street',d='Indonesian retailer and franchise holder of Starbucks, Zara and Nine West; described as one of Indonesia\'s leading retail companies.',own='Mitra Adiperkasa',tier='Independent',s='https://www.indonesia-investments.com/news/todays-headlines/mitra-adiperkasa-one-of-indonesias-leading-retail-companies/item955')
for n in ['Dalydress','Premoda']:
    upd(n,c='Egypt',seg='High street',d='Egyptian clothing brand of SETA Textiles; Ezdehar Management bought over 80 % in 2024.',own='SETA Textiles (over 80 % Ezdehar Management)',own_y=2024,tier='Independent',s='https://enterpriseam.com/egypt/2024/01/10/ezdehar-acquires-majority-stake-in-apparel-player-behind-dalydress-and-premoda/')
for n in ['Weekend','Non-Stop','Contempo','La Mode','Metropolis','Gianfranco Dunna']:
    upd('Suburbia '+n,c='Mexico',seg='High street',d='Private label of Suburbia.',own='Suburbia',tier='Own label',s=W+'Suburbia_(department_store)')
upd('Suburbia',c='Mexico',f='1970',s=W+'Suburbia_(department_store)')
upd('Cheeky',c='Argentina',seg='Children',d='Argentine children\'s clothing brand that calls itself the leading children\'s apparel brand in Argentina.',own='Cheek S.A.',tier='Independent',s='https://www.lanacion.com.ar/economia/negocios/la-paradoja-de-la-moda-argentina-ropa-cara-marcas-buscadas-en-el-exterior-nid16032024/')
upd('Rapsodia',c='Argentina',seg='Contemporary & premium',d='Argentine women\'s fashion brand controlled by the De Narváez group and the fund L Catterton.',own='De Narváez group and L Catterton',tier='Independent',s='https://www.lanacion.com.ar/economia/negocios/la-paradoja-de-la-moda-argentina-ropa-cara-marcas-buscadas-en-el-exterior-nid16032024/')
save('A1_brands.json',B)

A=load('A1.json')
def kind(n):
    for dp in A['depts']:
        for s in dp['s']:
            for k in s['k']:
                if k['n']==n: return dp,s,k
dp,s,k=kind('Thobe'); k['sel']="Names in Wikipedia's Thawb article (whole page read) plus the Djellaba, Gandoura, Jellabiya and Kachabia articles from the structure pass, sectioned by region. Complete: 7 of 7 names the Thawb article gives as separate garments (thawb itself is the kind)."
dp,s,k=kind('Southern African dress'); k['sel']=k['sel'].replace('(characters 0 to 100,000 of 257,837 read, which includes the Africa section)','(whole article read to its end at 257,837 characters; the text after 200,000 is references and navigation boxes)').replace('Covers 8 garments of the Southern Africa group.','Complete: 8 of 8 garments of the Southern Africa group in those sources.')
dp,s,k=kind('Fur coat'); k['sel']=k['sel'].replace('Covers 1 entries; the article was read except its last 1,160 characters.','Complete: 1 of 1 in those sources; the Fur clothing article is read to its end and its fashion houses (Fendi, Dior, Hermès, Max Mara, Louis Vuitton) are brands that use fur, not named fur-coat forms.')
# kilt accessories
dp,s,k=kind('Kilt')
sp='https://en.wikipedia.org/wiki/Sporran'
new={'n':'Kilt accessories','a':'Highland dress accessories','d':'Items worn with the kilt in Highland dress: the purse-like sporran, the decorative kilt pin and the small sgian-dubh knife in the hose.','s':sp,
 'x':[
 {'n':'Sporran','a':'purse','d':'Pouch worn on a strap or chain in front of the groin, since the kilt has no pockets; the name is Gaelic for purse.','mk':'','y':'','s':sp,'g':'Highland dress','dt':'day or dress · fur, hair or leather · cantle',
  'v':[{'n':'Day sporran','mk':'','y':'','d':'Brown leather shovel pouch with simple Celtic or thistle designs and three or more tassels.'},
       {'n':'Dress sporran','mk':'','y':'','d':'Larger and more ornate, often with a metal cantle and fur or hair tassels; full-dress has a fur front and 3 to 6 tassels, semi-dress is shaped like the day sporran.'},
       {'n':'Full mask sporran','mk':'','y':'','d':'Made from an animal head and pelt such as badger, fox or pine marten; now mostly worn for re-enactments.'},
       {'n':'Horsehair sporran','mk':'','y':'','d':'One of the largest dress sporrans, mainly worn by pipers and drummers.'}]},
 {'n':'Kilt pin','a':'kilt-pin','d':'Piece of jewellery on the lower corner of the outer apron that adds weight to stop it blowing open; its origin is disputed.','mk':'','y':'','s':'https://en.wikipedia.org/wiki/Kilt_pin','g':'Highland dress','dt':'safety pin to silver and stone',
  'v':[{'n':'Blanket or safety pin','mk':'','y':'','d':'Plain pin for sports dress.'},{'n':'Silver pin with set stone','mk':'','y':'','d':'Evening wear.'},{'n':'Claw brooch','mk':'','y':'','d':'Often made from a grouse foot; can catch on a dancing partner\'s dress.'}]},
 {'n':'Sgian-dubh','a':'skean-dhu · skene-dhu','d':'Small single-edged knife tucked into the top of the kilt hose with the hilt showing; it may descend from the sgian-achlais carried under the armpit.','mk':'','y':'','s':'https://en.wikipedia.org/wiki/Sgian-dubh','g':'Highland dress','dt':'blade point · scabbard material','v':[]}],
 'tt':[['Occasion',['Day','Dress','Sports']],['Material',['Leather','Fur or hair','Silver','Stainless steel']]],
 'nl':"One entry is a named accessory of Highland dress, as the Sporran, Kilt pin and Sgian-dubh articles on Wikipedia give them; types of one accessory are versions.",
 'sel':"Wikipedia: Sporran, Kilt pin and Sgian-dubh (each read whole); none names a maker, so no brand is linked. Complete: 3 of 3 accessories of the kilt named in the Folk costume article's British Isles navigation box (Kilt, Sporran, Trews, Feather bonnet) that are not garments; trews and the feather bonnet are not entries here. Cloth traditions are not entries.",
 'xg':'by tradition'}
s['k'].append(new)
for dp in A['depts']:
    if dp['n']=='Tops':
        S='https://www.koreatimes.co.kr/business/companies/20220625/legacy-fashion-brands-overshadowed-by-sportswear-luxury-goods-makers'
        for who,sh in [('Beanpole (Samsung C&T Fashion Group)','2.3 %'),('Fila','2.1 %'),('adidas','2 %'),('Daks (LF)','1.9 %'),('Kolon Sport (Kolon FnC)','1.4 %')]:
            dp['ms'].append({'mkt':'South Korea fashion','who':who,'share':sh,'yr':2021,'s':S,'note':'Euromonitor via The Korea Times, brand share of a 43.3 trillion won market; Beanpole and Uniqlo were the top two for 2017 to 2021'})
        dp['ms'].append({'mkt':'Saudi Arabia fashion retail','who':'Fawaz Abdulaziz Alhokair Group','share':'','yr':2020,'s':'https://www.arabnews.com/business/pandemic-closes-stores-at-saudi-arabias-biggest-retail-franchise-group-1698231','note':'Arab News calls it Saudi Arabia\'s biggest retail franchise group; 1,580 stores in 100 malls in 13 countries; no share figure'})
        dp['ms'].append({'mkt':'Indonesia retail','who':'Matahari','share':'','yr':None,'s':W+'Matahari_(department_store)','note':'Wikipedia calls it the largest retail platform in Indonesia; no share figure'})
save('A1.json',A)
