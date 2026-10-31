import json,os,copy
O='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(O+'H4.json')); B=json.load(open(O+'H4_brands.json'))
DT="concentration (EDC, EDT, EDP, parfum/extrait) · reformulation and batch · bottle size and edition"
kinds={k['n']:k for dp in d['depts'] for s in dp['s'] for k in s['k']}
MAP={'Rabanne':'Paco Rabanne','Kniže & Comp.':'Knize','Jōvan':'Jovan','By Kilian':'Kilian Paris','Christian Dior':'Dior','Al Rasasi':'Rasasi','Aramis (Estée Lauder)':'Aramis','Shiseido-Serge Lutens':'Serge Lutens','Jo Malone':'Jo Malone London','Kayali Fragrances':'Kayali','Prada Beauty':'Prada','Brocard and Co. (now Novaya Zarya)':'Novaya Zarya'}
def fix(o):
    if isinstance(o,dict):
        if 'mk' in o and o['mk'] in MAP: o['mk']=MAP[o['mk']]
        for v in o.values(): fix(v)
    elif isinstance(o,list):
        if len(o)==2 and all(isinstance(z,str) for z in o) and o[1] in MAP: o[1]=MAP[o[1]]
        for v in o: fix(v)
fix(d)
# empty mk
for k in kinds.values():
    for x in k.get('x',[]):
        if x['n']=='Knize Ten': x['mk']='Knize'
        if x['n']=='Jovan Musk': x['mk']='Jovan'
        if x['n']=='Calone': x['mk']=''
        for v in x.get('v',[]):
            if v.get('mk')=='Pfizer': v['mk']=''
# Deer musk: single home in raw materials
mo=kinds['Musk oil']; mo['x']=[x for x in mo['x'] if x['n']!='Deer musk']
dm=[x for x in kinds['Animalic & resin material']['x'] if x['n']=='Deer musk'][0]
dm['v']=[{"n":"Deer Musk (house oil)","mk":"Abdul Samad Al Qurashi","d":"named in the house range of musk oils"}]
# Floral m/r duplicates
fl=kinds['Floral fragrance']; fl.pop('r',None)
# Body mist
bm=kinds['Body mist']; bm['m']=[["Warm Vanilla Sugar","Bath & Body Works"],["Marshmallows Hair & Body Fragrance Mist","Ellis Brooklyn"],["Peach Skin Hair and Body Fragrance Mist","PHLUR"],["Saffron & Cedar Body Mist","Salt & Stone"]]
# Oud rename
od=kinds['Oud fragrance (Western niche)']; od['n']='Oud fragrance'
kinds['Oud fragrance']=od
od['d']="Alcohol-based perfume built around agarwood (oud), real or synthetic, from Western and Arabian houses; oil ouds sit with attars."
od['a']="oud · agarwood perfume · oud eau de parfum"
# clone t on family kinds
for n in ['Floral fragrance','Chypre fragrance','Fougère fragrance','Amber fragrance','Woody fragrance','Citrus & eau de cologne','Gourmand fragrance','Leather fragrance','Aquatic & ozonic fragrance','Green fragrance','Musk & skin scent','Oud fragrance']:
    t=kinds[n].setdefault('t',[])
    if 'inspired-by (clone)' not in t: t.append('inspired-by (clone)')
def A(kind,n,a,dd,mk,y,s,v,):
    kinds[kind].setdefault('x',[]).append({"n":n,"a":a,"d":dd,"mk":mk,"y":y,"s":s,"v":v,"dt":DT})
STC='https://surrendertochance.com/'
A('Floral fragrance','Dior Homme','Dior Homme 2005',"Orris-led masculine with cacao, amber and leather that put iris into men's designer fragrance.",'Dior','2005','https://cafleurebon.com/cafleurebon-modern-masterpieces-dior-homme-give-that-man-a-floral/',[{"n":"Original","mk":"Dior","y":"2005","d":"Olivier Polge; leather and patchouli base"},{"n":"2011 reformulation","mk":"Dior","y":"2011","d":"François Demachy; base reduced to vetiver"}])
A('Floral fragrance','Eternity','','Calvin Klein floral of 1988, composed by Sophia Grojsman.','Calvin Klein','1988','https://en.wikipedia.org/wiki/List_of_perfumes',[{"n":"Original","mk":"Calvin Klein","y":"1988","d":"Sophia Grojsman"}])
A('Green fragrance','Vol de Nuit','','Guerlain scent of 1933 composed by Jacques Guerlain.','Guerlain','1933','https://en.wikipedia.org/wiki/List_of_perfumes',[{"n":"Original","mk":"Guerlain","y":"1933","d":"Jacques Guerlain"}])
A('Green fragrance','Grey Flannel','','Bracing violet-leaf men\'s cologne with oakmoss; the best-known Geoffrey Beene fragrance.','Geoffrey Beene','1975','https://thefragrantman.com/2013/04/24/scent-memory-grey-flannel-geoffrey-beane-1975-lelegance-est-un-rituel/',[{"n":"Original","mk":"Geoffrey Beene","y":"1975","d":"André Fromentin"}])
A('Chypre fragrance','Habanita','','Molinard scent first sold in 1921 to perfume cigarettes, then as a skin perfume in a black Lalique bottle.','Molinard','1924','https://kafkaesqueblog.com/2013/05/25/perfume-review-habanita-by-molinard-eau-de-toilette/',[{"n":"Cigarette-scenting sachets and liquid","mk":"Molinard","y":"1921"},{"n":"Skin perfume","mk":"Molinard","y":"1924","d":"black Lalique bottle"},{"n":"1980s eau de toilette","mk":"Molinard","d":"reformulated"},{"n":"2012 eau de parfum","mk":"Molinard","y":"2012","d":"reformulated"}])
A('Chypre fragrance','Hacivat','','Nishane chypre of pineapple and oakmoss, often compared with Creed Aventus.','Nishane','2017','https://scentadvice.com/hacivat-2017-nishane/',[{"n":"Extrait de parfum","mk":"Nishane","y":"2017","d":"Jorge Lee"}])
A('Chypre fragrance','Club de Nuit Intense Man','CDNIM','Armaf eau de toilette widely described as a clone of Creed Aventus; the best-known Arabian inspired-by.','Armaf','2015','https://bespokeunit.com/articles/fragrance/armaf-club-de-nuit-intense-man/',[{"n":"Eau de toilette","mk":"Armaf","y":"2015","d":"inspired-by of Aventus"}])
# Aventus cross-link
for x in kinds['Chypre fragrance']['x']:
    if x['n']=='Aventus':
        x['v'].append({"n":"Club de Nuit Intense Man (inspired-by)","mk":"Armaf","y":"2015","d":"clone widely compared with Aventus; listed as its own archetype"})
A('Fougère fragrance','Green Irish Tweed','GIT','Creed fougère of lemon verbena and violet leaf over iris and sandalwood.','Creed','1985','https://www.miamilivingmagazine.com/post/house-of-creed-green-irish-tweed',[])
A('Fougère fragrance','Naxos','XJ 1861 Naxos','Xerjoff scent of lavender, honey, cinnamon and tobacco leaf.','Xerjoff','2015',STC+'xerjoff-xj-1861-naxos/',[{"n":"Eau de parfum","mk":"Xerjoff","y":"2015"}])
A('Amber fragrance','Tobacco Vanille','','Tom Ford Private Blend of tobacco leaf, vanilla, cacao and tonka bean.','Tom Ford','2007','https://scentgrail.com/holy-grail-scents/tom-ford-tobacco-vanille-review/',[{"n":"Eau de parfum","mk":"Tom Ford","y":"2007","d":"Olivier Gillotin; Private Blend"}])
A('Amber fragrance','Interlude Man','','Amouage spicy oriental of oregano, incense, amber and leather.','Amouage','2012',STC+'amouage-interlude-man/',[{"n":"Eau de parfum","mk":"Amouage","y":"2012","d":"Pierre Negrin"}])
A('Amber fragrance','Gold Man','Amouage Gold','Amouage men\'s scent of rose, frankincense, myrrh and civet; a women\'s version exists as Gold Woman.','Amouage','1983',STC+'amouage-gold-man/',[{"n":"Gold Man eau de parfum","mk":"Amouage","y":"1983","d":"Guy Robert"},{"n":"Gold Woman","mk":"Amouage","d":"women's version; year not confirmed"}])
A('Amber fragrance','Layton','','Parfums de Marly scent of apple, lavender, vanilla and cardamom.','Parfums de Marly','2016',STC+'parfums-de-marly-layton/',[{"n":"Eau de parfum","mk":"Parfums de Marly","y":"2016","d":"Hamid Merati-Kashani"}])
A('Amber fragrance','9pm','Afnan 9pm','Afnan amber-vanilla with apple and cinnamon, a budget cult favourite.','Afnan','2020',STC+'afnan-9pm/',[{"n":"Eau de parfum","mk":"Afnan","y":"2020"}])
A('Leather fragrance','Tuscan Leather','','Tom Ford Private Blend leather with saffron, raspberry and black suede.','Tom Ford','2007',STC+'tom-ford-tuscan-leather/',[{"n":"Eau de parfum","mk":"Tom Ford","y":"2007","d":"Harry Fremont and Jacques Cavallier"}])
A('Aquatic & ozonic fragrance','Silver Mountain Water','SMW','Creed green-tea and blackcurrant scent with ozonic and musk notes.','Creed','1995','https://scentgrail.com/holy-grail-scents/silver-mountain-water/',[{"n":"Eau de parfum","mk":"Creed","y":"1995","d":"no flankers; reformulated"}])
A('Woody fragrance','Black Afgano','','Nasomatto resinous scent of cannabis, tobacco, coffee and oud.','Nasomatto','',STC+'nasomatto-black-afgano-sji6/',[{"n":"Original","mk":"Nasomatto","d":"Alessandro Gualtieri"}])
A('Gourmand fragrance','Khamrah','','Lattafa sweet gourmand of cinnamon, dates, praline and vanilla.','Lattafa','','https://aromatica.beehiiv.com/p/lattafa-khamrah-review',[])
json.dump(d,open(O+'H4.tmp','w'),ensure_ascii=False,indent=1)
# brands
bs=B['b']; names={b['n'] for b in bs}
for b in [
 {"n":"Fabergé","seg":"Mainstream","kf":"Brut cologne","c":"United States","f":"1937","d":"US perfume and cosmetics house of Samuel Rubin, maker of Brut, Babe and Tigress; later absorbed by Unilever.","s":"https://en.wikipedia.org/wiki/Faberg%C3%A9_(cosmetics)"},
 {"n":"Geoffrey Beene","seg":"Designer","kf":"Grey Flannel","c":"United States","f":"1963","d":"New York fashion house whose best-known fragrance is Grey Flannel (1975).","s":"https://en.wikipedia.org/wiki/Geoffrey_Beene"},
 {"n":"Gisou","seg":"Premium","kf":"hair perfume","c":"","f":"2013","d":"Honey-based hair care brand of Negin Mirsalehi; sells a Honey Infused Hair Perfume.","s":"https://cultbeauty.co.uk/p/gisou-honey-infused-hair-perfume-various-sizes/13526903/?rctxt=fbt"}]:
    if b['n'] not in names: bs.append(b)
json.dump(B,open(O+'H4_brands.tmp','w'),ensure_ascii=False,indent=1)
os.replace(O+'H4.tmp',O+'H4.json'); os.replace(O+'H4_brands.tmp',O+'H4_brands.json')
