import json
P='/home/user/Possession-Taxonomy/rebuild/out/A1_parts/TRAD.json'
part=json.load(open(P)); dep=part['depts'][0]
K={k['n']:k for s in dep['s'] for k in s['k']}
W='https://en.wikipedia.org/wiki/'
CL=' Cloth traditions are not entries: the Cloth attribute names them and the visual-art taxonomy covers cloth and textile traditions.'
def ent(k,n,d,u,g,a='',role=None,v=None):
    if any(e['n'].lower()==n.lower() for e in k.setdefault('x',[])): return
    e={'n':n,'a':a,'d':d,'mk':'','y':'','s':u if u.startswith('http') else W+u,'g':g}
    if role:e['role']=role
    if v:e['v']=v
    k['x'].append(e)
def V(n,d): return {'n':n,'y':'','mk':'','d':d}
# ---- Hanbok: tail read
k=K['Hanbok']
for n,g,d in [('Myeonbok','Court and official dress','King\'s formal ceremonial robe.'),('Jeokui','Court and official dress','Queen\'s equivalent of the myeonbok, often embroidered with pheasants.'),('Aengsam','Court and official dress','Formal clothing for students during state exams and ceremonies.'),('Ayam','Outerwear','Garment worn for protection from the cold.'),('Chosŏnot','Upper garments and skirts','North Korean name for hanbok; the chima-jeogori is still the official women\'s outfit there.')]: ent(k,n,d,'Hanbok',g)
for e in k['x']:
    if e['n']=='Cheollik': e['d']='Military robe combining a blouse and kilt, derived from the Mongol terlig; allowed horseback riding and archery.'
k['sel']="Garments named in Wikipedia's Hanbok article (whole page read: 0 to 267,384 characters), sectioned by use. Complete: %d of %d garments; headwear (gat, jokduri, neoul, gache), hairpins, ornaments (norigae, binyeo, daenggi) and shoes (danghye, onhye) are named in the article but belong to the hats, jewellery and footwear taxonomies."%(len(k['x']),len(k['x']))
order=['Upper garments and skirts','Lower garments','Outerwear','Court and official dress','Wedding and ritual dress']
k['x'].sort(key=lambda e:order.index(e['g']))
# ---- tails: coverage lines
def setcov(kn,old,new):
    s=K[kn]['sel']; assert old in s,(kn,old); K[kn]['sel']=s.replace(old,new)
n=lambda kn:len(K[kn]['x'])
setcov('Kimono',"(characters 0 to 200,000 of 217,652 read; the last 17,652, references and navigation, unread)","(whole page read, 217,652 characters)")
setcov('Kimono',"Covers %d types, every type named in the text read;"%n('Kimono'),"Complete: %d of %d types named;"%(n('Kimono'),n('Kimono')))
setcov('Obi',"(characters 0 to 100,000 of 101,237 read; the last 1,237 characters unread)","(whole page read, 101,237 characters)")
setcov('Obi',"Covers %d named obi;"%n('Obi'),"Complete: %d of %d named obi;"%(n('Obi'),n('Obi')))
setcov('Barong Tagalog',"(characters 0 to 100,000 of 104,085 read; the last 4,085 unread)","(whole page read, 104,085 characters)")
setcov('Barong Tagalog',"Covers %d styles."%n('Barong Tagalog'),"Complete: %d of %d styles."%(n('Barong Tagalog'),n('Barong Tagalog')))
setcov('Kilt',"(characters 0 to 100,000 of 126,472 read; the last 26,472 unread)","(whole page read, 126,472 characters)")
setcov('Kilt',"Covers %d kilt forms."%n('Kilt'),"Complete: %d of %d kilt forms."%(n('Kilt'),n('Kilt')))
setcov('Vyshyvanka',"(characters 0 to 100,000 of 126,069 read; the last 26,069 unread)","(whole page read, 126,069 characters)")
setcov('Vyshyvanka',"Covers %d styles."%n('Vyshyvanka'),"Complete: %d of %d styles."%(n('Vyshyvanka'),n('Vyshyvanka')))
setcov('Mamianqun',"Covers %d skirts in characters 0 to 100,000 of 131,292 read; the last 31,292 characters were not read."%n('Mamianqun'),"Complete: %d of %d skirts named (whole page read, 131,292 characters; the tail names only the lower-garment navigation list, whose Qun, Maweiqun and ruqun types are other kinds or unspecified)."%(n('Mamianqun'),n('Mamianqun')))
# ---- Bunad by county
k=K['Bunad']
counties={
'Østfold':['Østfoldbunad','Løkendrakt','Smaalenenes mannsbunad','Fredrikstaddrakt','Eidsbergdrakt','Hobøldrakt','Hvalerdrakt','Mossedrakt','Festdrakt til Østfoldrosen'],
'Oslo and Akershus':['Romeriksbunad','Hurdalsbunad','Eidsvollsbunad','Lillestrømsdrakt','Follobunad','Bærumsbunad','Askerbunad','Akerdrakt','Oslodrakt','Sørkedalsbunad'],
'Hedmark':['Hedmarksbunad','Vallsetbunad','Østerdalsbunad','Sør-Østerdalsbunad','Nord-Østerdalsbunad','Kviknebunad','Folldalsbunad','Dalåsstakk','Lødrupbunad','Maria Aaen-bunad','Alvdalsbunad','Trysilbunad','Solør og Odalsbunad','Finnskogsbunad','Lundebydrakt','Vålerdrakt','Brattfossdrakt','Lunderseterdrakt','Hedemarksbunad (1955 model)','Hedemarksbunad (1985 model)','Rekonstruert kvinnebunad fra Hedemarken'],
'Oppland':['Gudbrandsdalsbunad','Lesjabunad','Grafferbunad','Gausdalsbunad','Dovrebunad','Jordebunad','Lillehammerbunad','Hadelandsbunad','Totendrakt','Vestopplandbunad','Valdresbunad','Etnedalskjolen','Rondastakk og rutaliv','Trykktykjol','Gudbrandsdalens mannsbunad','Kvinnebunad fra Gudbrandsdalen','Gudbrandsdalens festbunad','Damask-kjol','1700-talls bunad fra Gudbrandsdalen','Landingsdrakt','Den gamle Valdresbunaden','Den nye Valdresbunaden','Rutastakken fra Valdres','Mannsbunad fra Valdres'],
'Buskerud':['Stakker fra Hallingdal','Mannsbunad fra Hallingdal','Festbunad fra Nedre Hallingdal','Brudebunad fra Hallingdal','Ringeriksbunad','Den gamle Ringeriksdrakt','Flesbergstakk','Skjælingskleda fra Øvre Numedal','Gråtrøye','Rundtrøye','Bergmannsdrakt fra Kongsberg'],
'Vestfold':['Vestfold Husflidslags kvinnebunad (1932 model)','Vestfold Husflidslags kvinnebunad (1956 model)','Vestfold Husflidslags mannsbunad'],
'Telemark':['Øst-Telemark stakk og liv','Øst-Telemark raudtrøyebunad','Øst-Telemark beltestakk','Øst-Telemark Tinn-bunad','Øst-Telemark gråtrøye','Kvinnebunad fra Vest-Telemark','Vest-Telemark bringerklutbunad','Vest-Telemark gråtrøye','Vest-Telemark svart modell og rundtrøye'],
'Aust-Agder':['Åmlibunad for kvinner','Åmlibunad for menn'],
'Vest-Agder':['Mannsdrakt fra Vest-Agder','Kvinnedrakt fra Vest-Agder, stripestakk','Kvinnedrakt fra Vest-Agder','Rynkestakk og plissestakk','Brudedrakt fra Vest-Agder','Øyebunaden'],
'Rogaland':['Rogalandsbunad herre','Husflidens Rogalandsbunad, mønster Løland','Kronebunad fra Rogaland'],
'Hordaland':['Askøybunad','Fanabunad','Nordhordlandsbunad','Sunnhordalandsbunad','Vinterbunad fra Voss','Konebunad fra Voss','Jentebunad fra Voss','Brudebunad fra Voss'],
'Sogn og Fjordane':['Nordfjordbunad','Sognebunad','Sunnfjordbunad'],
'Møre og Romsdal':['Nordmørsbunaden','Norddalsbunaden','Ørskogbunaden','Skodjebunaden','Strandabunaden','Hjørundfjordbunaden','Jentebunaden fra Sunnmøre','Sykkylvsbunaden','Vigrabunaden','Søre Sunnmørebunaden','Mannsbunad fra Sunnmøre','Guttebunad fra Sunnmøre','Brun mannsbunad fra Sunnmøre','Kvinnedrakt fra Sunnmøre','Kronebunad fra Sunnmøre','Rindalsbunaden','Brudedrakt for Nordmøre','Ørstabunaden'],
'Sør-Trøndelag':['Oppdalsbunaden','Trønderbunaden','Tydalsdrakten','Selbubunad','Aure/Hemnebunad'],
'Nord-Trøndelag':['Nord-trønderbunad'],
'Nordland':['Nordlandsbunaden','Hamarøybunaden','Lofotbunaden','Mannsbunad for Nordland og Troms','Ofotbunaden'],
'Troms':['Tromsbunaden for kvinner','Kvænangsbunaden','Målselvbunaden','Lenvikdrakten','Senjadrakten'],
'Finnmark':['Finnmarksbunad','Kvendrakta (Kven costume)'],
'Svalbard':['Svalbardbunad']}
LST='https://en.wikipedia.org/wiki/List_of_national_costumes_of_Norway'
cmap={'Hardangerbunad':'Hordaland','Setesdalsbunad':'Aust-Agder','Telemarksbunad':'Telemark','Østtelemark bunad':'Telemark','Oslobunad':'Oslo and Akershus'}
for e in k['x']: e['g']=cmap[e['n']]
for c,l in counties.items():
    for n in l: ent(k,n,'Costume listed under %s in the Wikipedia list of national costumes of Norway.'%c,LST,c)
order=list(counties)
k['x'].sort(key=lambda e:order.index(e['g']))
k['nl']="One entry is a named Norwegian regional costume, mainly a bunad, as Wikipedia's List of national costumes of Norway names it; trim and jewellery are versions or attributes."
k['sel']="Every costume named in Wikipedia's List of national costumes of Norway (19 county sections, read through the page summariser county by county) plus the Hardangerbunad, Setesdalsbunad, Telemark and Oslo bunads of the Bunad article; sectioned by county. Complete: %d of %d named costumes. The Bunad article estimates about 200 bunads, so the list is the Wikipedia canon, not every bunad in use. The Sámi costumes listed under Nordland and Troms are the Gákti kind."%(len(k['x']),len(k['x']))
k['xg']='by county'
# ---- Zhongshan suit
k=K['Zhongshan suit']
k['x'][0]['g']='Republic of China'
ent(k,'Mao suit','Name that took hold after the 1949 founding of the People\'s Republic of China; also Mao tunic.','Zhongshan_suit','People\'s Republic of China',a='Mao tunic')
k['x'].sort(key=lambda e:['Republic of China',"People's Republic of China"].index(e['g']))
k['nl']="One entry is a named form or period name of the Zhongshan suit, as Wikipedia's Zhongshan suit article gives them."
k['sel']="Forms named in Wikipedia's Zhongshan suit article (whole page read), sectioned by period; Sun Yat-sen suit and Chinese tunic suit are aliases. Complete: %d of %d."%(len(k['x']),len(k['x']))
# ---- Toub
k=K['Toub']
for e in k['x']: e['g']='Urban and professional'
CS='Clothing_in_Sudan'
ent(k,'Zarag toub','Indigo-dyed cloth of northern Sudan and Nubian communities, linked to status.',CS,'Northern Sudan')
ent(k,'Central Sudan toub','Lighter, subtly embroidered toub of Sennar and the White Nile.',CS,'Central Sudan')
ent(k,'Western Sudan toub','Toub with layered wraps in bold colours and embroidery, in Darfur and Kordofan.',CS,'Western Sudan')
ent(k,'Melhfa','Related wrap that the article says toub variations spread to in the Sahel and West Africa.',CS,'Sahel and West Africa')
order=['Northern Sudan','Central Sudan','Western Sudan','Urban and professional','Sahel and West Africa']
k['x'].sort(key=lambda e:order.index(e['g']))
k['nl']="One entry is a named regional form of the toub, as Wikipedia's Clothing in Sudan article gives them."
k['sel']="Forms named in Wikipedia's Clothing in Sudan article (whole page read), sectioned by region. The page carries a notice that parts may be machine-generated, so details are less firmly attested. Men's jalabiya and jibba are separate garments (Thobe kind). Complete: %d of %d."%(len(k['x']),len(k['x']))
k['xg']='by region'
# ---- Kaba and slit
k=K['Kaba and slit']
k['x'][0]['g']='Ghana'
k['x'][0]['s']='https://collections.vam.ac.uk/item/O1637115/kaba-ensemble-akosombo-textiles-ltd'
k['x'][0]['v']=(k['x'][0].get('v') or [])+[V('Three-piece ensemble','kaba (sewn blouse), abosoo or slit (wrapped or sewn skirt) and akatasoo or second cloth (unsewn), 1990s example by Akosombo Textiles')]
k['nl']="One entry is the kaba and slit ensemble; its pieces and cloth are versions and attributes."
k['sel']="No Wikipedia article on the kaba and slit was found by search. The entry follows the V&A object record (collections.vam.ac.uk, O1637115) and the Jehovah's Witnesses article carried from the structure pass. No further named forms are attested. Complete: 1 of 1 attested form."+CL
# ---- Southern African
k=K['Southern African dress']
k['x'][0]['g']='Namibia'
FC='Folk_costume'
for n,g,d,u in [('Umbhaco','South Africa','Dress of Xhosa men and women; women\'s pieces include faskoti, ncebetha and ibhayi.',FC),('Isidwaba','South Africa','Zulu skirt named in the Folk costume article.',FC),('Umutsha','South Africa','Zulu loincloth named in the Folk costume article.',FC),('Ibheshu','South Africa','Zulu back apron named in the Folk costume article.',FC),('Tshega','Botswana','Garment named in the Folk costume article for Botswana.',FC),('Ieteisi','Botswana','Garment named in the Folk costume article for Botswana.',FC)]: ent(k,n,d,u,g)
ent(k,'Basotho blanket','Woollen garment worn by the Sotho people in Lesotho and South Africa.','Basotho_blanket','Lesotho',v=[V('Moholobela','fertility blanket for young men preparing for manhood'),V('Lekhokolo','worn after initiation to show adulthood'),V('Motlotlehi','former bride\'s wedding blanket'),V('Lingoetsi','bride\'s blanket that replaced the Motlotlehi'),V('Serope','given by a husband to his wife at their first child\'s birth'),V('Seana Marena','chief\'s blanket reserved for the king and chiefs'),V('Lehlosi','chiefly blanket with a wild cat or leopard pattern'),V('Victoria England','1897 design by Donald Fraser for the Diamond Jubilee'),V('Motlatsi','made for the birth of Prince Lerotholi'),V('Letlama','worn by initiated men and women'),V('Batho Ba Roma','commemorates the 1988 papal visit'),V('Kharetsa','named after an aloe of the Maloti Mountains'),V('Sefate and Morena','everyday blankets')])
order=['South Africa','Lesotho','Namibia','Botswana']
k['x'].sort(key=lambda e:order.index(e['g']))
k['nl']="One entry is a named people's garment of southern Africa, as Wikipedia's Folk costume and Basotho blanket articles give them; named blanket patterns are versions."
k['sel']="Garments named in the Southern Africa part of Wikipedia's Folk costume article (characters 0 to 100,000 of 257,837 read, which includes the Africa section) and in the Basotho blanket article (whole page read), sectioned by country. Hats (isicholo, otjikaiva, mokorotlo), the sling bag and settler dress are not entries; shweshwe is the Cloth attribute. Covers %d garments of the Southern Africa group."%len(k['x'])+CL
# ---- Trachtenjanker and Bombachas
k=K['Trachtenjanker']; k['x'][0]['g']='Alps'
k['sel']="No Wikipedia article on the Trachtenjanker or Janker was found by search (two searches returned retailer pages only), so the single entry from the structure pass stands and no list of named forms is attested. Complete: 1 of 1 attested form."
k=K['Bombachas & gaucho dress']
for e in k['x']: e['g']='Río de la Plata'
k['sel']="Garments named in the clothing section of Wikipedia's Gaucho article (whole page read, 158,881 characters): bombachas, chiripá, poncho (own kind) and the faja sash (the Item attribute). Pampero's Bombacha de campo follows its own product page. No Wikipedia article on bombachas was found by search. Complete: %d of %d."%(len(k['x']),len(k['x']))
json.dump(part,open(P,'w'),ensure_ascii=False,indent=1)
print(sum(len(x.get('x',[])) for x in K.values()), len(K['Bunad']['x']))
for kn,x in K.items():
    if x.get('x') and any(not e.get('g') for e in x['x']): print('no g',kn)
