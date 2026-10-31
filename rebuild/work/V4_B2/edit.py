import json,os,copy
P='rebuild/out/B2.json'
d=json.load(open(P))
W='https://en.wikipedia.org/wiki/'
def kinds():
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']: yield dp,s,k
K={k['n']:k for _,_,k in kinds()}
removed=[]
for dp,s,k in kinds():
    if k.get('m'):
        removed.append((k['n'],len(k['m'])))
# Zanjan becomes an entry; others removed
def E(n,dsc,url,g,a="",y="",mk=""):
    return {"n":n,"a":a,"d":dsc,"mk":mk,"y":y,"s":url,"v":[],"g":g}
def setg(kind,mapping,default=None):
    for x in K[kind]['x']:
        g=mapping.get(x['n'],default)
        if g: x['g']=g
def add(kind,items):
    have={x['n'].lower() for x in K[kind]['x']}|{al.strip().lower() for x in K[kind]['x'] for al in x.get('a','').split('·')}
    for it in items:
        if it['n'].lower() not in have: K[kind]['x'].append(it)
def sortx(kind,order):
    K[kind]['x'].sort(key=lambda x:(order.index(x.get('g')) if x.get('g') in order else 99))
def fin(kind,nl,sel,xg,order=None):
    k=K[kind]; k['nl']=nl; k['sel']=sel; k['xg']=xg
    if order: sortx(kind,order)

# Persian
add('Persian rug',[
 E('Zanjan','Handmade carpet from Zanjan in north-west Iran.',W+'Zanjan_rug','North-west Iran'),
 E('Ahar','Persian carpet from Ahar, former capital of the Karadagh Khanate, named after the city and region.',W+'Ahar_rug','North-west Iran'),
 E('Karadagh','Rug made in or near Qarajeh village in the Qareh Dagh region near the Azerbaijan border.',W+'Karadagh_rug','North-west Iran'),
 E('Bakhshayish','Tapestry rugs and carpets from the mountain village of Bakhshayish, about 48 km east of Tabriz.',W+'Bakhshayish','North-west Iran'),
 E('Aghajly','Persian carpets of the Tabriz type, named for their composition rather than their place of production.',W+'Aghajly','North-west Iran'),
 E('Shahsevan','Iranian-style rug or kilim made by the Shahsevan people of Iran\'s Azerbaijan region.',W+'Shahsevan_rug','North-west Iran'),
 E('Borujerd','Persian rug woven in Borujerd, western Iran, distinct from Luri rugs and rugs from Arak.',W+'Borujerd_rug','West and west-central Iran'),
 E('Jozan','Quality rugs made near Jozan village in the Malayer area, usually in the Sarouk style.',W+'Jozan_rug','West and west-central Iran'),
 E('Seraband','Floor rug from the Ser-e Band district south-west of Arak, with a mir design of pear or leaf shapes in diagonal rows.',W+'Seraband_rug','West and west-central Iran',a='Mir'),
 E('Lilihan','Carpets woven by Armenians in Lilihan village in the former Kamareh district, now Khomeyn.',W+'Lilihan_carpets_and_rugs','West and west-central Iran'),
 E('Kurdish rug','Rugs woven by Kurds in Kurdistan, which in the rug trade usually means Iranian Kurdistan.',W+'Kurdish_rugs','Kurdistan'),
 E('Abadeh','Persian carpet made in the town of Abadeh.',W+'Abadeh_rug','Central Iran'),
 E('Varamin','Carpets and rugs woven in Varamin and nearby areas south-east of Tehran, often seen as traditional in style and motif.',W+'Varamin_carpet','Central Iran'),
 E('Shiraz','Rugs made in villages around Shiraz in Fars province, often using designs of tribal weavers such as the Qashqai and Afshar.',W+'Shiraz_rug','South and south-east Iran'),
 E('Pictorial carpet','Decorative rug meant to hang on walls, often framed, with designs unlike those of floor rugs.',W+'Pictorial_carpet','Pictorial and court carpets'),
])
pm={'Heriz':'North-west Iran','Serapi':'North-west Iran','Tabriz':'North-west Iran','Ardabil design':'North-west Iran',
'Sultanabad':'West and west-central Iran','Mahal':'West and west-central Iran','Farahan':'West and west-central Iran','Sarouk':'West and west-central Iran','Malayer':'West and west-central Iran','Hamadan':'West and west-central Iran',
'Bijar':'Kurdistan','Senneh':'Kurdistan','Kashan':'Central Iran','Isfahan':'Central Iran','Nain':'Central Iran','Qom':'Central Iran',
'Kerman':'South and south-east Iran','Ravar':'South and south-east Iran','Mashad':'North-east Iran',
'Qashqai':'Tribal rugs','Gabbeh':'Tribal rugs','Khamseh':'Tribal rugs','Afshar':'Tribal rugs','Luri':'Tribal rugs','Bakhtiari':'Tribal rugs'}
setg('Persian rug',pm)
fin('Persian rug',"One entry is a Persian rug type named by its weaving town, district or tribe, as a fetched Wikipedia category of Persian rugs and carpets lists it.",
 "Follows the Wikipedia category 'Persian rugs and carpets' (https://en.wikipedia.org/wiki/Category:Persian_rugs_and_carpets) and the Persian carpet article, and keeps every rug-type page of the category; the Carpet Museum, companies, people and single named carpets (Ardabil, Baharestan, Coronation) are left out. Complete: 31 of 31 rug-type pages in the category, counting Heriz, Seraband and Kurdish rugs, with Arak held as Sultanabad and Mehraban left out for lack of a fetched page.",
 "Region of Iran",['North-west Iran','West and west-central Iran','Kurdistan','Central Iran','South and south-east Iran','North-east Iran','Tribal rugs','Pictorial and court carpets'])
K['Persian rug']['see'].append(['F2','Rug design and textile art','design, pattern and motif of rugs belong to visual art'])
# Anatolian
add('Anatolian rug',[
 E('Isparta','Carpets of Isparta, a weaving tradition developed towards the end of the 19th century.',W+'Carpet_weaving_in_Isparta','Weaving centres'),
 E('Mamluk carpet','Carpets of debated origin made from the late 15th to the mid-16th century, continuing after the Ottoman conquest of Egypt in 1517.',W+'Mamluk_carpets','Early carpets (14th–17th century)'),
 E('Caucasian dragon carpet','Early Caucasian pile carpets of the 16th and 17th centuries with stylised dragon motifs.',W+'Caucasian_dragon_carpets','Early carpets (14th–17th century)')])
am={}
for n in ['Holbein carpet','Lotto carpet','"Transylvanian" rug','White-ground (Selendi) rug','Animal carpet','Ottoman Cairene']: am[n]='Early carpets (14th–17th century)'
for n in ['Yürük','Yağcıbedir']: am[n]='Nomadic rugs'
setg('Anatolian rug',am,'Weaving centres')
# dragon carpets belong to Caucasian; move
dr=[x for x in K['Anatolian rug']['x'] if x['n']=='Caucasian dragon carpet'][0]
K['Anatolian rug']['x'].remove(dr)
fin('Anatolian rug',"One entry is an Anatolian rug type named by its weaving town, region or period group, as a fetched Wikipedia category of Turkish rugs lists it.",
 "Follows the Wikipedia category 'Turkish rugs and carpets' (https://en.wikipedia.org/wiki/Category:Turkish_rugs_and_carpets), which has 15 pages, and the Mamluk carpets page; Dobag, Elibelinde, the Ghiordes knot and Kilim motifs are techniques or motifs, not rug types, and Kayseri is left out for lack of a fetched page. Complete: 10 of 10 rug-type pages in the category (Konya, Bergama, Hereke, Lotto, Milas, Ushak, Yürük, Early Anatolian animal carpets, Isparta, Anatolian rug), plus Mamluk.",
 "Period or setting",['Early carpets (14th–17th century)','Weaving centres','Nomadic rugs'])
# Caucasian
add('Caucasian rug',[
 E('Armenian carpet','Tufted or knotted rugs woven in Armenia or by Armenians from pre-Christian times, with some flat-woven textiles.',W+'Armenian_carpet','Armenia'),
 E('Caucasian dragon carpet','Early Caucasian pile carpets of the 16th and 17th centuries with stylised dragon motifs.',W+'Caucasian_dragon_carpets','Early carpets'),
 E('Arran','Variety of Karabakh carpet.',W+'Arran_(carpet)','Karabakh school'),
 E('Buynuz','Pile carpets from Karabakh known as horn carpets.',W+'Buynuz_carpets','Karabakh school',a='Horn carpet'),
 E('Garagoyunlu','Carpets from the Ganja-Gazakh and Karabakh weaving centres, named after the Garagoyunlu tribes.',W+'Garagoyunlu_carpets','Karabakh school'),
 E('Gasimushaghi','Pile carpets of the Jabrayil group of the Karabakh school.',W+'Gasimushaghi_carpets','Karabakh school'),
 E('Shabalyt buta','Pile carpets of the Karabakh group, part of the complex Karabakh designs.',W+'Shabalyt_buta_carpet','Karabakh school'),
 E('Shedde','Lint-free carpets of the Karabakh group, made mainly in Nakhchivan and several other districts.',W+'Shedde','Karabakh school'),
 E('Borchaly','Sub-category of the Gazakh group, named after the Borchaly region, now in Georgia.',W+'Borchaly_(carpet)','Gazakh and Ganja groups'),
 E('Demirchilar','Carpets of the Gazakh group, named after a village west of Gazakh.',W+'Demirchilar_(carpet)','Gazakh and Ganja groups'),
 E('Garachop','Pile carpets of the Gazakh group, named after villages north-west of Gazakh, now in Georgia.',W+'Garachop_carpet','Gazakh and Ganja groups'),
 E('Chukhanlu','Carpet type of the Shirvan group of the Guba-Shirvan weaving centre.',W+'Chukhanlu_carpets','Guba and Shirvan school'),
 E('Gadim Minaret','Carpets of the Guba carpet-weaving school.',W+'Gadim_Minaret_carpets','Guba and Shirvan school'),
 E('Gollu-chichi','Carpets of the Guba school, also called Gollu carpets.',W+'Gollu-chichi_carpets','Guba and Shirvan school'),
 E('Jek','Lint-free and pile carpets woven by the Jek people in Quba, counted in the Kuba group.',W+'Jek_carpets','Guba and Shirvan school'),
 E('Absheron','Carpets of the Absheron weaving school, covering several Absheron villages and the Khyzy region.',W+'Absheron_carpet_weaving_school','Absheron school'),
 E('Khila-Afshan','Pile carpets of the Baku group of the Absheron school.',W+'Khila-Afshan_carpets','Absheron school'),
])
cm={'Karabagh':'Karabakh school','Gendje':'Gazakh and Ganja groups','Kazak':'Gazakh and Ganja groups','Shirvan':'Guba and Shirvan school','Kuba':'Guba and Shirvan school','Derbent':'Dagestan','Daghestan':'Dagestan'}
setg('Caucasian rug',cm)
fin('Caucasian rug',"One entry is a Caucasian rug type named by its weaving school, region or village group, as a fetched Wikipedia category lists it.",
 "Follows the Wikipedia category 'Azerbaijani rugs and carpets' (https://en.wikipedia.org/wiki/Category:Azerbaijani_rugs_and_carpets, 25 pages) with the Armenian carpet category and the Caucasian dragon carpets page; museums, the Azerbaijani carpet weaving overview, Chul (held under Central Asian rugs), Shahsevan (held under Persian rugs) and the Ganja rugs page (held as Gendje) are not separate entries. Complete: 20 of 20 carpet-type pages in the Azerbaijani category, Armenian carpet and Caucasian dragon carpets.",
 "Weaving school or region",['Karabakh school','Gazakh and Ganja groups','Guba and Shirvan school','Absheron school','Dagestan','Armenia','Early carpets'])
# Turkmen -> Central Asian
add('Turkmen rug',[
 E('Uzbek carpet','Among the best-known handmade carpets made by Uzbeks, closely tied to other Uzbek crafts.',W+'Uzbek_carpet','Uzbek rugs'),
 E('Asmalyk','Five-sided, sometimes seven-sided, Turkmen textile hung during wedding processions, pile-woven or embroidered.',W+'Asmalyk','Tribal textiles'),
 E('Chul','Thick woollen horse cover, often pile-woven, with intricate designs.',W+'Chul_(carpet)','Tribal textiles')])
setg('Turkmen rug',{},'Turkmen tribes')
for x in K['Turkmen rug']['x']:
    if x['n'] in('Uzbek carpet',): x['g']='Uzbek rugs'
    if x['n'] in('Asmalyk','Chul'): x['g']='Tribal textiles'
fin('Turkmen rug',"One entry is a Central Asian carpet type named by its Turkmen tribe, by Uzbek weaving or by the object woven, as a fetched Wikipedia category lists it.",
 "Follows the Wikipedia category 'Turkic rugs and carpets' (https://en.wikipedia.org/wiki/Category:Turkic_rugs_and_carpets, 11 pages) and its Uzbekistani subcategory; Gul is a motif and Yomut carpet is held as Yomut. Complete: 9 of 9 carpet-type pages in the category (Turkmen rug, Yomut, Ersari, Asmalyk, Chul, Uzbek carpet and the tribes Tekke, Salor, Saryk, Chodor held from the Turkmen rug article).",
 "Tribe or object",['Turkmen tribes','Tribal textiles','Uzbek rugs'])
# Afghan
fin('Afghan & Baluch rug',"One entry is an Afghan or Baluch rug type or weaving centre as a fetched Wikipedia category lists it.",
 "Follows the Wikipedia category 'Afghan rugs and carpets' (https://en.wikipedia.org/wiki/Category:Afghan_rugs_and_carpets, 5 pages) with the Baluchi rug page. Complete: 3 of 3 rug-type pages (Afghan rug, Baluchi rug, War rug); Chul and Turkmen rug are held under Central Asian rugs; Shindand, Aqcha and Bezeheri are kept from the earlier pass.",
 "Weaving centre or type")
# Indian
add('Indian & Pakistani rug',[E('Amritsar','Rugs and carpets made in Amritsar in north-west India near Kashmir.',W+'Amritsar_rugs_and_carpets','India')])
im={'Mughal carpet':'Mughal period','Agra':'India','Jaipur':'India','Kashmir':'India','Bhadohi':'India','Amritsar':'India','Pak Persian':'Pakistan','Pakistani Bokhara':'Pakistan','Jaldar':'Pakistan','Chobi':'Pakistan','Lahore jail carpet':'Pakistan'}
setg('Indian & Pakistani rug',im)
fin('Indian & Pakistani rug',"One entry is an Indian or Pakistani rug type or weaving centre, as a fetched Wikipedia category lists it.",
 "Follows the Wikipedia categories 'Indian rugs and carpets', 'Pakistani rugs and carpets' and 'Oriental rugs and carpets' (https://en.wikipedia.org/wiki/Category:Indian_rugs_and_carpets). Companies (Obeetee, Jaipur Rugs, Karagheusian) and flatweaves (held under Flatweave rug and Navalgund) are not entries here. Complete: 6 of 6 pile-rug pages (Amritsar, Kashmiri rug, Mughal carpets, Pakistani rug, Chobi, Girdler's carpet counted as Mughal); the other entries are kept from the earlier pass.",
 "Country or period",['Mughal period','India','Pakistan'])
# Moroccan, Chinese etc: coverage
fin('Chinese rug',"One entry is a Chinese rug type named by its weaving centre or period.","No whole-space reference exists on Wikipedia for Chinese rugs; the four entries come from the earlier pass and each carries its own source. Covers 4 of an open set.","Centre or period")
fin('Tibetan rug',"One entry is a Tibetan rug type or weaving centre.","Follows the Tibetan rug page (https://en.wikipedia.org/wiki/Tibetan_rug) listed in the Wikipedia rugs category. Covers 3 of the types that page names.","Type or centre")
fin('Moroccan rug',"One entry is a Moroccan rug type named by its Berber group or town.","Follows the Moroccan rugs page (https://en.wikipedia.org/wiki/Moroccan_rugs) in the Wikipedia rugs category; Berber carpet and Margoum had no retrievable article text and are not added. Covers 7 of about 9 pages in the category on North African rugs; the rest are missing because their extracts were not fetched.","Berber group or town")
fin('Aubusson & Savonnerie carpet',"One entry is a French workshop carpet tradition.","Both traditions come from the earlier pass with their own sources; no whole-space reference exists. Complete: 2 of 2.","Workshop")
fin('Rya rug',"One entry is a Nordic rya or ryijy rug tradition.","Follows the Wikipedia pages Rya (rug) and Scandinavian rugs (https://en.wikipedia.org/wiki/Scandinavian_rugs). Covers 3 of the traditions those pages name; Danish and Norwegian traditions have no separate page in the category.","Country")
add('European workshop rug',[
 E('Arraiolos rug','Embroidered wool rug from Arraiolos in Portugal, dating to at least the 16th century and partly inspired by Persian carpets.',W+'Arraiolos_rug','Portugal'),
 E('Flokati','Thick, soft, shaggy woven wool rug.',W+'Flokati_rug','Greece'),
 E('Bessarabian rug','Pile and tapestry rugs from the Russian provinces, Ukraine and Moldova of the late 19th and early 20th century.',W+'Bessarabian_rugs_and_carpets','Eastern Europe'),
 E('Pirot carpet','Flat tapestry-woven rugs from Pirot in Serbia, seen as a national symbol.',W+'Pirot_carpet','Eastern Europe')])
em={'Alcaraz carpet':'Spain','Alpujarra rug':'Spain','Hammersmith carpet':'Britain and Ireland','Donegal carpet':'Britain and Ireland'}
setg('European workshop rug',em)
fin('European workshop rug',"One entry is a European regional or workshop rug tradition, as a fetched Wikipedia category lists it.",
 "Follows the Wikipedia category 'Rugs and carpets' (https://en.wikipedia.org/wiki/Category:Rugs_and_carpets, 86 pages and 13 subcategories) for European pages. Complete for the pile and tapestry pages it holds: Alcaraz, Arraiolos, Bessarabian, Flokati, Pirot; Swedish and Scandinavian rugs are held under Rya rug; Pirot carpet is the same tradition as the Pirot kilim under Flatweave rug.",
 "Country",['Spain','Portugal','Britain and Ireland','Greece','Eastern Europe'])
# remove duplicate Pirot carpet (flatweave Pirot kilim exists)
K['European workshop rug']['x']=[x for x in K['European workshop rug']['x'] if x['n']!='Pirot carpet']
K['European workshop rug']['sel']=K['European workshop rug']['sel'].replace('Pirot; Swedish','; Swedish').replace(', Flokati, ; ',', Flokati; ').replace(', Flokati; ',', Flokati; ')
K['European workshop rug']['sel']=K['European workshop rug']['sel'].replace('Complete for the pile and tapestry pages it holds: Alcaraz, Arraiolos, Bessarabian, Flokati; Swedish','Complete: 4 of 4 pile and tapestry pages it holds (Alcaraz, Arraiolos, Bessarabian, Flokati) plus the earlier Hammersmith, Donegal and Alpujarra entries; Swedish')
# Designer rug
fin('Designer rug',"Maker ranges only: no named entries.","Commodity design kind: no canon of named entries; four maker ranges are listed in r and the loose models were removed. Complete: 0 of 0 named entries.","Maker")
K['Designer rug'].pop('xg');K['Designer rug'].pop('nl');
# Flatweave
add('Flatweave rug',[
 E('Verni','Sumak weave made without a pattern by Shahsevan and Arasbaran nomad women, also called the needle rug.',W+'Verni_(kilim)','Iran'),
 E('Navalgund durrie','Woven durries from Navalgund in Karnataka with geometric, bird and animal designs, registered as a geographical indication in 2011.',W+'Navalgund_durrie','India'),
 E('Bhavani Jamakkalam','Blankets and carpets made in Bhavani, Erode district, Tamil Nadu, recognised as a geographical indication in 2005–06.',W+'Bhavani_Jamakkalam','India'),
 E('Tat patti','Narrow floor covering of coarse jute made in the Punjab region.',W+'Tat_patti','India and Pakistan')])
fm={'Kilim':'Anatolia and the Balkans','Pirot kilim':'Anatolia and the Balkans','Chiprovtsi kilim':'Anatolia and the Balkans','Rölakan':'Anatolia and the Balkans','Soumak':'Caucasus and Iran','Jajim':'Caucasus and Iran','Zili':'Caucasus and Iran','Dhurrie':'India'}
setg('Flatweave rug',fm)
fin('Flatweave rug',"One entry is a flat-woven rug type or tradition, as a fetched Wikipedia category lists it.",
 "Follows the Wikipedia categories 'Rugs and carpets' and 'Oriental rugs and carpets' (https://en.wikipedia.org/wiki/Category:Oriental_rugs_and_carpets) and the Indian rugs category for flatweaves. Complete: 12 of 12 flatweave pages in those categories (Kilim, Chiprovtsi kilim, Pirot, Soumak, Jajim, Dhurrie, Verni, Navalgund durrie, Bhavani Jamakkalam, Tat patti, Zili, Rölakan); Khes had no retrievable text and is not added.",
 "Region",['Anatolia and the Balkans','Caucasus and Iran','India','Iran','India and Pakistan'])
K['Flatweave rug']['see']=[['F2','Rug design and textile art','flatweave design and motif belong to visual art']]
fin('Navajo rug',"One entry is a Navajo weaving style or regional pattern.","Entries come from the earlier pass, each with its own source, and follow the Navajo weaving article (https://en.wikipedia.org/wiki/Navajo_weaving); no whole-space list was fetched. Covers 12 of the styles that article names.","Style")
add('Rag rug',[
 E('Catalogne','Woven French-Canadian rag rug, also used as a blanket, with French origins and later development in Quebec.',W+'Catalogne_(rug)','Canada'),
 E('Braided rug','Staple of early Colonial American homes, made from scraps of clothing and other excess materials.',W+'Braided_rug','United States')])
setg('Rag rug',{'Trasmatta':'Sweden'})
fin('Rag rug',"One entry is a rag-rug tradition named by its country.","Follows the Wikipedia Rag rug page and the 'Rugs and carpets' category (https://en.wikipedia.org/wiki/Category:Rugs_and_carpets). Complete: 3 of 3 rag-rug pages in the category (Rag rug, Catalogne, Braided rug) with the Swedish Trasmatta from the earlier pass.","Country",['Sweden','Canada','United States'])
fin('Hooked rug',"One entry is a hooked-rug tradition named by its place.","Entries come from the earlier pass with their own sources and the Wikipedia Hooked rug article. Covers 3 of the traditions that article names.","Place")
fin('Felt rug',"One entry is a felt rug tradition of Central Asia.","Entries come from the earlier pass with their own sources. Covers 2 of the traditions found; no whole-space reference was fetched.","Tradition")
# non-rug canons: honest coverage
fin('Quilt',"One entry is a quilt tradition or pattern family named by place or style.","No whole-space reference was fetched; entries come from the earlier pass with their own sources. Quilt traditions also belong to visual art. Covers 13 of an open set.","Place or style")
fin('Blanket',"One entry is a named blanket tradition or trade blanket.","No whole-space reference was fetched; entries come from the earlier pass with their own sources. Covers 8 of an open set.","Place or maker")
fin('Printed & embroidered furnishing textile',"One entry is a named furnishing-textile tradition.","Textile traditions belong with visual art; entries come from the earlier pass with their own sources. Covers 4 of an open set.","Origin")
fin('Flat-woven towel',"One entry is a flat-woven towel or bath-cloth tradition.","Entries come from the earlier pass with their own sources. Complete: 2 of 2 found; no whole-space reference exists.","Country")
fin('Carry cloth',"One entry is a traditional wrapping or carry cloth.","Entries come from the earlier pass with their own sources. Complete: 2 of 2 found; no whole-space reference exists.","Country")
fin('Towel',"One entry is a named towel tradition.","Only the Imabari towel is kept, as the single design-collection or origin entry the icon rule allows; no whole-space reference exists. Complete: 1 of 1.","Origin")
fin('Tablecloth',"One entry is a named table-linen tradition.","Entries come from the earlier pass with their own sources; no whole-space reference exists. Covers 2 of an open set.","Origin")
# JL curtain
c=K['Curtain']; c['x']=[{"n":"JL curtain fabric","a":"Tessuto per tende JL","d":"Curtain fabric by Renata Bonfanti that won the 1962 Compasso d'Oro for its structural invention.","mk":"Renata Bonfanti","y":"1962","s":"https://www.adidesignmuseum.org/en/collection/jl-curtain-fabric/","v":[],"role":"landmark"}]
c['nl']="One entry is a curtain fabric held by a design collection or given a major design award."
c['sel']="Commodity kind: the icon rule allows design-award landmarks only; the ADI Design Museum collection page names the 1962 Compasso d'Oro winner. Complete: 1 of 1 found."
c['xg']="Award"
# remove models
for dp,s,k in kinds():
    k.pop('m',None)
# Market panel on Bedding
bd=[dp for dp in d['depts'] if dp['n']=='Bedding'][0]
G='https://www.globaldata.com/store/report/home-textiles-overview-market-analysis/'
bd['ms']=[
 {"mkt":"Global home textiles: bedroom linen share of market value","who":"Bedroom linen","share":"52.2 %","yr":2025,"s":G,"note":"revenue $62.5 billion of $119.8 billion, value"},
 {"mkt":"Global home textiles by region","who":"Asia-Pacific","share":"44.2 %","yr":2025,"s":G,"note":"value"},
 {"mkt":"Global home textiles by region","who":"Europe","share":"25.9 %","yr":2025,"s":G,"note":"value"},
 {"mkt":"Global home textiles by region","who":"North America","share":"23.2 %","yr":2025,"s":G,"note":"value"}]
# renames
ren={'Turkmen rug':'Central Asian rug'}
K['Turkmen rug']['n']='Central Asian rug'
json.dump(ren,open('rebuild/out/B2_renames.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P)
print(removed)
