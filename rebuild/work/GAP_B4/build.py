import json,os,sys
P='/home/user/Possession-Taxonomy/rebuild/out/B4.json'
d=json.load(open(P))
def kinds():
    for D in d['depts']:
        for S in D['s']:
            for i,k in enumerate(S['k']): yield D,S,i,k
def K(name):
    for D,S,i,k in kinds():
        if k['n']==name: return D,S,i,k
    raise KeyError(name)
W='https://en.wikipedia.org/wiki/'
def E(n,d_,s,g,mk='',y='',a='',v=None,dt='',role=None,**kw):
    e={"n":n,"a":a,"d":d_,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt,"g":g}
    if role: e['role']=role
    e.update(kw); return e
def add(kind,entries,sel):
    D,S,i,k=K(kind)
    ex={e['n'].lower() for e in k.get('x',[])}
    k.setdefault('x',[])
    for e in entries:
        if e['n'].lower() in ex: continue
        k['x'].append(e)
    k['sel']=sel
    k.setdefault('xg','by region')
    k.setdefault('nl',"One entry is a named type or example of this object; variants are versions.")
    return k
def setsel(kind,sel):
    K(kind)[3]['sel']=sel

# Paperweights
add('Glass paperweight',[
 E('Baccarat classic paperweight','Classic-period French weight of the 1845-1860 years, made at the Baccarat factory.',W+'Paperweight','France','Baccarat','1845-1860'),
 E('Clichy classic paperweight','Classic-period French weight of the 1845-1860 years, made at the Clichy factory.',W+'Paperweight','France','','1845-1860'),
 E('Paul Ysart paperweight','Weight by Paul Ysart, a pioneer of Scottish paperweight work from the 1930s.',W+'Paperweight','Scotland','','1930s onward'),
 E("Kaziun lampwork weight","Lampwork paperweight by Charles Kaziun, who also made buttons, inkwells and bottles from 1940.",W+'Paperweight','United States','','1940'),
 E('Victorian advertising paperweight','Glass weight with a milk-glass portrait or advertisement, made in Pittsburgh under an 1882 patent.',W+'Paperweight','United States','','1882'),
 E('New England Glass Company paperweight','Weight comparable to the best French ones, made by the New England Glass Company.',W+'Paperweight','United States'),
],"Follows Wikipedia's Paperweight article, read in full. Covers 8 named makers and forms of about 10 the article names; swirl, marbrie and California-style are styles, and the studio revival artists (Stankard, Whittemore and others) are named without a single work.")
# Nianhua kind
D,S,i,k=K('Spring Festival couplet')
nk={"n":"Nianhua","a":"New Year picture","d":"Coloured woodblock print hung at the Chinese New Year, showing nature, religion and folklore.","s":W+'Nianhua',
 "tt":[["Making",["Woodblock print","Hand-coloured print"]],["Subject",["Door god","Fu Lu Shou","Folklore scene"]]],
 "x":[
  E('Yangliuqing nianhua','Tianjin prints that the article calls the most prominent and influential New Year pictures.',W+'Nianhua','China (Tianjin)',role='landmark'),
  E('Taohuawu nianhua','Suzhou prints, one of the Four Great centres; they took in some European techniques.',W+'Nianhua','China (Suzhou, Jiangsu)','','Song dynasty'),
  E('Zhujian nianhua','Folk woodblock prints from Zhujian Town, Kaifeng, one of the Four Great centres.',W+'Nianhua','China (Kaifeng, Henan)','','Tang dynasty origins'),
  E('Yangjiaobei nianhua','Prints from Yangjiaobei, Weifang, one of the Four Great centres; a Ming-period workshop is linked to local production.',W+'Nianhua','China (Weifang, Shandong)','','Ming dynasty'),
  E('Yangjiabu nianhua','Shandong prints listed among the best-known production sites; the article does not say whether the place is the same as Yangjiaobei.',W+'Nianhua','China (Shandong)'),
  E('Wuqiang nianhua','Hebei prints listed among the best-known production sites.',W+'Nianhua','China (Hebei)'),
  E('Fengxiang nianhua','Shaanxi prints listed among the best-known production sites.',W+'Nianhua','China (Shaanxi)'),
  E('Mianzhu nianhua','Sichuan prints listed among the best-known production sites.',W+'Nianhua','China (Sichuan)'),
 ],
 "nl":"One entry is a named nianhua printing centre; its prints are the object.",
 "sel":"Follows Wikipedia's Nianhua article, read in full. Complete: 8 of 8 centres it names (the article does not say whether Yangjiabu and Yangjiaobei are one place).","xg":"by region"}
if not any(x['n']=='Nianhua' for x in S['k']): S['k'].insert(i+1,nk)
setsel('Spring Festival couplet',"Follows Wikipedia's Chinese New Year article, read in full (272,995 characters). Complete: 1 of 1 couplet tradition the article names; nianhua has its own kind, and the article describes no regional couplet styles.")
setsel('Paper-cut window decoration',"Follows Wikipedia's Chinese New Year article, read in full. Complete: 1 of 1 paper-cut form the article names; it gives no regional styles.")
setsel('Red lantern',"Follows Wikipedia's Chinese New Year article, read in full. Complete: 1 of 1 New Year lantern type; Lantern Festival lanterns belong to a separate festival.")
add('New Year entrance decoration',[E('Fu character','Red diamond-shaped blessing character on a home entrance, hung upside down to signal arriving luck (not in Cantonese communities).',W+'Chinese_New_Year','China')],
 "Follows Wikipedia's Chinese New Year article and Kadomatsu article. Covers 2 entries; no complete list of entrance decorations exists.")
setsel('Engimono',"Follows a retailer's list of 50 Japanese lucky charms, read to the end. Covers 10 of 50 items that are made decor objects; the others are creatures, plants, stones or materials, and the last five are a bow and arrow (see Hamaya), a salt cone, a tumbler, a scroll and postcards.")
# sundial
add('Garden sundial',[
 E('Shadow clock','Earliest known sundial, from the Valley of the Kings in Egypt, about 1500 BC.',W+'Sundial','Egypt','','c. 1500 BC',role='origin'),
 E('Armillary sphere dial','Sundial built as a skeleton sphere of rings with an equiangular dial surface; a common garden centrepiece.',W+'Sundial','Not stated'),
 E('Analemmatic sundial','Flat dial with hour markers on an ellipse and a vertical gnomon moved each day; large ones are laid out in gardens.',W+'Sundial','Not stated'),
 E('Equatorial bow sundial','Semicircular dial with the gnomon parallel to the earth axis; the article cites Hasselt, France and Jaipur (1727-1733).',W+'Sundial','Not stated'),
 E('Heliochronometer','Sundial that corrects to mean or standard time, devised by Philipp Hahn about 1763 and improved by Abbe Guyoux about 1827.',W+'Sundial','Not stated','Philipp Hahn','c. 1763'),
 E('Sunquest sundial','Sundial designed by Richard L. Schmoyer in the 1950s to correct for the equation of time.',W+'Sundial','United States','','1950s'),
 E('Bifilar sundial','Dial with two non-intersecting threads whose shadows cross at the time, devised by Hugo Michnik in 1922.',W+'Sundial','Germany','Hugo Michnik','1922'),
 E('Vertical wall dial','Dial fixed to a wall, as on town halls and church towers.',W+'Sundial','Not stated'),
],"Follows Wikipedia's Sundial article, read in full (214,193 characters). Covers 9 of about 40 types; portable and indoor dials (ring, Capuchin, diptych, navicula, shepherd's) are not garden ornaments and are left out.")
# wind chime
add('Wind chime',[
 E('Feng ling','Chinese metal wind bell hung from shrines and pagodas, developed after Chinese bell casting, from about 1100.',W+'Wind_chime','China','','after c. 1100'),
 E('Pagoda wind bell','Small bell hung at pagoda and temple corners to ward off birds and evil spirits, recorded from the 2nd century in India.',W+'Wind_chime','India','','2nd century'),
],"Follows Wikipedia's Wind chime article, read in full. Covers 6 named traditions and 4 brands from the maker pages; the article names no complete list.")
# weathervane
add('Weathervane',[
 E('Gallo di Ramperto','Oldest surviving rooster-shaped vane, dated 820, now in the Museo di Santa Giulia, Brescia.',W+'Weather_vane','Italy','','820'),
 E('Tower of the Winds Triton','Bronze Triton whose rod turned with the wind, on the Tower of the Winds in Athens.',W+'Weather_vane','Greece','','c. 50 BC'),
 E('Söderala vane','Gilded Viking-era vane of about 1050, later used for church purposes.',W+'Weather_vane','Sweden','','c. 1050'),
 E('Old Thomas','Iconic vane on the town hall of Tallinn.',W+'Weather_vane','Estonia'),
 E('Tio Pepe vane','Sherry advertisement in Jerez that the article lists as the world largest working weather vane.',W+'Weather_vane','Spain'),
],"Follows Wikipedia's Weather vane article, read in full. Covers 9 named vanes and types; the article lists some 20 vanes and places, and the rest are single buildings or museum pieces.")
# snow globe
add('Snow globe',[E('Garaja underwater globe','Underwater fish version of the snow globe, made by Novelty Pool Ornaments in 1929 after Joseph Garaja of Pittsburgh filed the first US patent (1927).',W+'Snow_globe','United States','Novelty Pool Ornaments','1929')],
 "Follows Wikipedia's Snow globe article, read in full. Covers 4 makers and types of about 6 named; the rest are film, art and luxury-brand uses.")
# ornaments
add('Tree ornament',[
 E('Polish bombka','Hand-painted glass bauble; the article says Poland is the largest producer of glass bauble ornaments, from the 19th century.',W+'Christmas_ornament','Poland','','19th century'),
 E('Tlalpujahua glass ornament','Glass-blown ornament made year-round at Tlalpujahua, Michoacan, and exported.',W+'Christmas_ornament','Mexico (Michoacan)'),
 E('Chignahuapan ornament','Glass-blown ornament from Chignahuapan, Puebla.',W+'Christmas_ornament','Mexico (Puebla)'),
 E('Dresden die-cut ornament','Fibreboard ornament from Dresden, popular with families with small children.',W+'Christmas_ornament','Germany (Dresden)'),
],"Follows Wikipedia's Christmas ornament article, read in full, and the maker pages cited. Covers 8 of about 12 forms and makers it names; DeMuth (1870), Woolworth, silver ornaments and tinsel are makers or trade facts, not objects.")
# nutcracker
D,S,i,k=K('Nutcracker figure')
for e in k['x']:
    if e['n'].startswith('Steinbach'):
        e['v'].append({"n":"Restart after insolvency","mk":"Steinbach","y":"2016","d":"factory in Marienberg restarted in March 2016 with 35 employees; Rico Paul of Dresden bought the firm"})
        e['s2']=None; e.pop('s2')
setsel('Nutcracker figure',"Follows Wikipedia's Nutcracker article and the Erzgebirge maker pages cited. Covers 3 entries; the article names Sonneberg and Seiffen workshops and the carvers Junghanel, Mertens, Kolbe and Petersen without any figure. Steinbach has no fetched founding year (searched: founding, history); Ulbricht was founded in 1928 in Seiffen by a 2025 company interview, whose founder is not named.")
# incense
inc="Follows Wikipedia's Incense article, read in full (152,590 characters), and the maker pages cited. "
add('Stick incense',[
 E('Agarbatti','Incense stick made by rolling paste around a bamboo core; the main incense form of India.',W+'Incense','India'),
 E('Joss stick','Incense stick used in East, South and South-East Asia; the word joss comes from Chinese pidgin English.',W+'Incense','East and South-East Asia'),
 E('Dhoop stick','Solid stick incense without a bamboo core, easily broken for portion control.',W+'Incense','Japan and Tibet'),
],inc+"Covers 7 entries; no complete list of stick incenses exists.")
add('Cone incense',[E('Japanese cone incense','Cone of incense that burns relatively quickly, invented in Japan in the 1800s.',W+'Incense','Japan','','1800s',role='origin')],inc+"Complete: 1 of 1 cone form the article names.")
add('Coil incense',[E('Chinese coil incense','Spiral of incense that burns for hours to days, used in Chinese cultures.',W+'Incense','China')],inc+"Complete: 1 of 1 coil form the article names.")
add('Incense rope & paper',[
 E('Tibetan rope incense','Long-lasting rope incense, used for centuries in Tibet and Nepal and easy to transport.',W+'Incense','Tibet and Nepal'),
 E('Moskolibano','Rolled resin incense from Mount Athos, pink (rose) or green (jasmine).',W+'Incense','Greece (Mount Athos)'),
 E("Papier d'Armenie",'Resin-infused paper that is lit and blown out; first sold as a disinfectant.',W+'Incense','Not stated'),
],inc+"Complete: 3 of 3 rope and paper forms the article names.")
add('Loose incense',[
 E('Frankincense','Resin of Boswellia sacra, the name meaning pure incense; used in Eastern Orthodox blends and the Ketoret.',W+'Incense','Oman'),
 E('Myrrh','Resin of Commiphora myrrha from Somalia, a non-combustible incense known in the West.',W+'Incense','Somalia'),
 E('Ketoret','Temple incense mixture of stacte, onycha, galbanum and frankincense, from the Exodus account.',W+'Incense','Jerusalem'),
],inc+"Covers 7 entries; the article names resins and woods (chenxiang, tanxiang, jinko, byakudan) as materials, which are held as materials not entries.")
add('Paste incense',[E('Neriko','Kneaded paste incense of Japan, also called awaseko.',W+'Incense','Japan')],inc+"Covers 2 entries; the article names no other paste forms.")
add('Incense burner',[
 E('Qustul incense burner','Burner of the A-Group culture, about 3300-3000 BCE; the article gives it as the earliest documented incense use.',W+'Incense','Nubia (Sudan)','','c. 3300-3000 BCE',role='origin'),
 E('Thurible','Hanging censer used in Christian liturgy, listed in the article as a liturgical burner.',W+'Incense','Not stated'),
],inc+"Covers 4 entries; the article names burners only in passing.")
# pinata
add('Piñata',[
 E('Pentolaccia','Earthenware pot broken in a game held on the first Sunday of Lent; the pot reached Italy in the 14th century.',W+'Pi%C3%B1ata','Italy','','14th century'),
 E('Posada piñata','Clay-pot piñata used by Augustinian monks at Acolman for a mid-December festival, from 1586.',W+'Pi%C3%B1ata','Mexico (Acolman)','','1586'),
 E('Spring ox piñata','Ox or cow piñata filled with five seeds at Chinese New Year; the ashes are kept for luck.',W+'Pi%C3%B1ata','China'),
],"Follows Wikipedia's Piñata article, read in full. Covers 5 entries; the page also names games (Dahi Handi, suikawari, hampas-palayok) that break a pot or fruit, which are not piñatas.")
# sparkler / fountain
add('Sparkler',[E('Morning Glory sparkler','Sparkler that emits small pyrotechnic stars during part of the burn.',W+'Sparkler','Not stated')],"Follows Wikipedia's Sparkler article, read in full. Covers 3 entries; the article names no makers.")
add('Fountain & wheel',[E('Fountain candle','Chemicals packed in a cardboard tube instead of coated on a wire; also called Bengal light, candle or fountain.',W+'Sparkler','Not stated')],"Follows Wikipedia's Sparkler article. Covers 1 entry; the article gives no further fountain or wheel types.")
setsel('Firecracker & banger',"Follows Wikipedia's Firecracker article, read in full, and the pages cited on each entry. Covers 5 entries; the article names flash powder (c. 1924) and Mandarin crackers but no other branded types.")
# garden
add('Bird bath',[E('Pulman bird bath','First purpose-built bird bath, credited to the garden design firm Abraham Pulman & Sons in the 1830s.',W+'Bird_bath','United Kingdom','Abraham Pulman & Sons','1830s',role='origin')],"Follows Wikipedia's Bird bath article, read in full. Complete: 2 of 2 forms it names (purpose-built Pulman bath and the moulded two-piece pedestal bath).")
add('Gazing ball',[E("Jardin d'Eau et de Lumiere sphere",'Illuminated stained-glass sphere at the centre of a modernist garden, shown in Paris in 1925.',W+'Gazing_ball','France','','1925')],"Follows Wikipedia's Gazing ball article, read in full. Covers 3 entries; the Herrenchiemsee lawn balls are marked 'said to' and are not entered.")
add('Rain chain',[E('Kusari-doi','Chain-gutter widely used in Japan and on temples to guide rainwater down.',W+'Rain_chain','Japan',v=[{"n":"Cup type","mk":"","y":"","d":"metal cups strung together, each with a hole in its base"},{"n":"Link type","mk":"","y":"","d":"chain links hanging vertically to guide water"}])],"Follows Wikipedia's Rain chain article, read in full. Complete: 1 of 1 named tradition; cup and link are its versions.")
add('Moravian star',[E('Moravian star','Folded paper-and-glass star first known from the 1830s at the Moravian Boys School in Niesky, a geometry project; the first mentioned was a 110-point star.',W+'Moravian_star','Germany (Niesky, Herrnhut)','','1830s',role='origin',v=[{"n":"Herrnhut Star Factory","mk":"","y":"","d":"founded by Harry Verbeek; main source of stars until the First World War"},{"n":"Abraham Duerninger Company","mk":"","y":"","d":"Moravian Church firm that regained the factory after an East German takeover in the 1950s and still makes the stars"}])],"Follows Wikipedia's Moravian star article, read in full. Complete: 1 of 1 star the article describes.")
# vases
add('Porcelain vase',[E('David Vases','Pair of Yuan-dynasty blue-and-white porcelain vases with a 1351 inscription, held in the British Museum.',W+'Vase','China','','1351')],"No complete list of decorative vases exists; follows Wikipedia's Vase article (read in full), V&A and house pages. Covers 3 named designs.")
add('Decorative urn',[E('Torlonia Vase','Garden vase cited with the Medici Vase as an example of the form.',W+'Vase','Italy')],"No complete list of decorative urns exists; follows Wikipedia's Vase article. Covers 3 named designs.")
# owners
D,S,i,k=K('Glass vase')
for e in k['x']:
    if e.get('mk')=='Orrefors':
        e.update({"own":"New Wave Group","tier":"Independent","own_y":"2005"})
# candle market
D,S,i,k=K('Container candle')
ms=D.setdefault('ms',[])
if not any(m.get('mkt')=='Global candle market' for m in ms):
    ms.append({"mkt":"Global candle market","who":"All suppliers","share":"","yr":2025,"s":"https://www.imarcgroup.com/candle-market-statistics","note":"valued at US$11.0 billion; North America the largest region; the page names 14 leading companies but gives no company shares"})
tmp=P+'.tmp'
json.dump(d,open(tmp,'w'),ensure_ascii=False,indent=1)
os.replace(tmp,P)
b=json.load(open('/home/user/Possession-Taxonomy/rebuild/out/B4_brands.json'))
names={x['n'] for x in b['b']}
for n,c,f,s,kf in [('New Wave Group','','','https://nwg.se/en/about-new-wave-group/history','brands and gifts')]:
    if n not in names:
        b['b'].append({"n":n,"c":c,"f":f,"seg":"Owner group","d":"Acquired the Orrefors Kosta Boda group in 2005.","lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":s,"kf":kf})
        for x in b['b']:
            if x['n']=='Orrefors': x['d']=(x.get('d') or '')
        json.dump(b,open('/home/user/Possession-Taxonomy/rebuild/out/B4_brands.json.tmp','w'),ensure_ascii=False,indent=1)
        os.replace('/home/user/Possession-Taxonomy/rebuild/out/B4_brands.json.tmp','/home/user/Possession-Taxonomy/rebuild/out/B4_brands.json')
print('ok')
