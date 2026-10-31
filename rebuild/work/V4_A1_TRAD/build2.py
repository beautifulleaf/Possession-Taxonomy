import json,re
R='/home/user/Possession-Taxonomy/rebuild/'
P=R+'out/A1_parts/TRAD.json'
part=json.load(open(P)); dep=part['depts'][0]
W='https://en.wikipedia.org/wiki/'
K={k['n']:k for s in dep['s'] for k in s['k']}
CL=' Cloth traditions are not entries: the Cloth attribute names them and the visual-art taxonomy covers cloth and textile traditions.'
def ent(kn,n,d,u,g,a='',y='',role=None,v=None,cty=None):
    k=K[kn];k.setdefault('x',[])
    if any(e['n'].lower()==n.lower() for e in k['x']): return
    e={'n':n,'a':a,'d':d,'mk':'','y':y,'s':W+u if not u.startswith('http') else u,'g':g}
    if role:e['role']=role
    if v:e['v']=v
    k['x'].append(e)
def setg(kn,mp,default=None):
    for e in K[kn]['x']:
        if e['n'] in mp: e['g']=mp[e['n']]
        elif default and not e.get('g'): e['g']=default
def fin(kn,order,nl,sel,xg):
    k=K[kn]
    miss=[e['n'] for e in k['x'] if not e.get('g')]
    assert not miss,(kn,miss)
    k['x'].sort(key=lambda e:order.index(e['g']) if e['g'] in order else 99)
    unk={e['g'] for e in k['x']}-set(order)
    assert not unk,(kn,unk)
    k['nl']=nl; k['xg']=xg
    k['sel']=sel.replace('{n}',str(len(k['x'])))+(CL if k.get('ve') else '')
def V(n,d,y=''): return {'n':n,'y':y,'mk':'','d':d}
# ---------- Kebaya
ID,MY,BR='Indonesia','Malaysia','Brunei'
setg('Kebaya',{'Kebaya Kartini':ID,'Kebaya Kutubaru':ID,'Balinese kebaya':ID,'Sundanese kebaya':ID,'Keraton kebaya':ID,'Kebaya Bandung':ID,'Kebaya Madura':ID,'Kebaya Kerancang':ID,'Kebaya Encim':ID,'Nyonya kebaya':MY,'Kebaya Labuh':MY,'Kebaya Saloma':MY,'Kebaya Kota Bharu':MY})
for n,g,d in [('Javanese kebaya',ID,'Simple V-neck, semi-transparent, worn over a kemben or corset.'),('Batak kebaya',ID,'North Sumatra wedding and church dress, worn with ulos or songket.'),('Ambon kebaya',ID,'Includes white long-sleeved and black church versions.'),('Minahasa kebaya',ID,'North Sulawesi white lace or brocade, worn for church or weddings.'),('Mongondow kabaya',ID,'Blouse paired with a skirt called daing; small floral patterns.'),('Jumputan kebaya',ID,'Made from Javanese tie-dye with a contrasting angkin or stagen sash.'),('Lurik kebaya',ID,'Yogyakarta kebaya made from coarse dark woven lurik cloth.'),('Noni (Indo) kebaya',ID,'Light white cotton and lace, adopted by European and Indo women in the Dutch East Indies.'),
('Kebaya Riau-Pahang (Kebaya Turki)',MY,'Pahang style with a buttoned cekak musang collar.'),('Kebaya Selangor',MY,'Long, loose style with four front pleats, worn with a sarong.'),('Kebaya Setengah Tiang',MY,'Negeri Sembilan mid-length kebaya with bell sleeves.'),('Kebaya Perlis',MY,'Loose cut sewn without shoulder seams.'),('Kebaya Chetti',MY,'Sarong kebaya of the Chetti Melaka community.'),('Kebaya Jawi Pekan',MY,'Sarong kebaya of the Jawi Peranakan community of Penang.'),('Kebaya Kristang',MY,'Sarong kebaya of the Kristang community of Malacca; the long form is kebaya kompridu, the short dabaia kurtu.'),('Kebaya Cocos (Kebayak and Baskat)',MY,'Cocos Malay dress with a European-inspired frill collar.'),('Kuyu kebaya',MY,'Black velvet kebaya of the Murut community in Borneo.'),
('Kebaya panjang (Brunei)',BR,'Long, knee-length Brunei blouse; the article also covers kebaya labuh, kebaya pendek and kebaya Bandung there.')]: ent('Kebaya',n,d,'Kebaya',g)
fin('Kebaya',[ID,MY,BR],"One entry is a named regional or community kebaya, as Wikipedia's Kebaya article lists them; fabric and fastening are versions or attributes.",
 "Regional kebayas named in Wikipedia's Kebaya article (whole page read, 225,776 characters), sectioned by country. Complete: {n} of {n} named forms; modern kebaya is a general style, and lace, kerawang and embroidered kebaya are fabric attributes.",'by country')
# ---------- Hanbok
J,L,O,C,B='Upper garments and skirts','Lower garments','Outerwear','Court and official dress','Wedding and ritual dress'
setg('Hanbok',{'Jeogori and chima':J,'Jeogori and baji':J,'Durumagi':O,'Dangui':C,'Wonsam':C,'Hwarot':B})
for n,g,d in [('Sokchima',L,'Underskirt or petticoat layer.'),('Po',O,'Generic outer robe or overcoat.'),('Baeja (kwaeja)',O,'Sleeveless outer garment.'),('Magoja',O,'Outer jacket introduced in the late 19th century.'),('Jokki',O,'Vest.'),('Jeonbok',O,'Long vest worn over children\'s outerwear.'),('Dopo',O,'Men\'s overcoat.'),('Jungchimak',O,'Long-sleeved travelling coat banned in the 19th century.'),('Simui',O,'Confucian scholar\'s robe from the Song dynasty.'),('Gwanbok (Danryeong)',C,'Official\'s round-collar robe.'),('Dallyeong (Danryunpo)',C,'Round-collar robe adopted from Tang China.'),('Dragon robe',C,'Royal formal robe.'),('Ochaebok',C,'Goguryeo royal attire.'),('Cheollik',C,'Garment of Mongolian origin described as Ming gifts or military uniforms.'),('Jangsam and dansam',O,'Women\'s outer garments.'),('Minbok',J,'Undyed white clothing of commoners.')]: ent('Hanbok',n,d,'Hanbok',g)
for e in K['Hanbok']['x']:
    if e['n']=='Durumagi': e['v']=(e.get('v') or [])+[V('Kkachi durumagi','children\'s colourful overcoat worn at New Year and first birthdays')]
fin('Hanbok',[J,L,O,C,B],"One entry is a named Korean garment or piece of court dress within the hanbok, as Wikipedia's Hanbok article lists them; sleeve, fabric and colour are versions.",
 "Garments named in Wikipedia's Hanbok article, sectioned by use. Covers {n} of the garments in characters 0 to 100,000 of 267,384 read (up to the Headdresses section); headwear, shoes and the later sections were not read and belong in the hats and footwear taxonomies.",'by use')
# ---------- Hakama
D,UD,F,CT,AR='Divided-leg and working','Undivided','Formal men\'s','Court and ceremonial','Historical and armoured'
setg('Hakama',{'Umanori':D,'Field hakama':D,'Andon-bakama':UD,'Sendaihira':F,'Naga-bakama':CT,'Ōguchi and ue-no-bakama':CT,'Sashinuki':CT,'Karusan-bakama':AR})
ent('Hakama','Yoroi hakama','Armoured trousers with small plates or mail sewn in; worn by samurai.','Hakama',AR,v=[V('Kikko kobakama','short armoured trousers with kikko armour')])
fin('Hakama',[D,UD,F,CT,AR],"One entry is a named type of hakama, as Wikipedia's Hakama article lists them; fabric and colour are attributes.",
 "Types named in Wikipedia's Hakama article (whole page read), sectioned by use. Complete: {n} of {n}; tattsuke-hakama and nu-bakama are alternate names, and the field hakama is the article's mountain umanori.",'by use')
# ---------- Obi
OW,OI,OM,OC='Women\'s formal','Women\'s informal','Men\'s','Children\'s'
setg('Obi',{'Maru obi':OW,'Fukuro obi':OW,'Nagoya obi':OW,'Darari obi':OW,'Hanhaba obi':OI,'Heko obi':OI,'Tsuke obi':OI,'Kaku obi':OM})
for n,g,d,a in [('Fukuro nagoya obi',OW,'Nagoya-style obi sewn in two only at the knot end, for the two-layer drum knot.','Hassun nagoya obi'),('Kyōbukuro obi',OW,'Invented in Nishijin in the 1970s; between nagoya and fukuro in formality.',''),('Manaita obi',OW,'Flat, front-tied, heavily padded obi of courtesans and kabuki actors.',''),('Odori obi',OW,'Dance obi with large metallic motifs, narrower for men.',''),
('Hoso obi',OI,'Collective term for informal half-width sashes; the kobukuro obi is the unlined form.','Kobukuro obi'),('Hara-awase obi',OI,'Informal obi with differently coloured sides.','Chūya obi'),('Hitoe obi',OI,'Single-layer obi stiff enough not to need lining; includes the hakata-ori obi.','Hakata-ori obi'),('Sakiori obi',OI,'Narrow informal obi woven from strips of recycled cloth.',''),('Tenga obi',OI,'Hanhaba-like obi in fancier celebratory fabric.',''),
('Sanjaku obi',OC,'Short easy-to-wear obi about 38 cm long, tied in a koma musubi.',''),('Shigoki obi',OC,'Decorative cloth ribbon worn in the Shichi-Go-San outfit of a seven-year-old girl.','')]: ent('Obi',n,d,'Obi_(sash)',g,a=a)
fin('Obi',[OW,OI,OM,OC],"One entry is a named type of obi by width, construction and formality, as Wikipedia's Obi article lists them; fabric is an attribute.",
 "Types named in Wikipedia's Obi (sash) article (characters 0 to 100,000 of 101,237 read; the last 1,237 characters unread), sectioned by wearer and formality. Covers {n} named obi; alternate names (tsukuri obi, kantan obi, kyūsun nagoya obi) are aliases.",'by wearer and formality')
# ---------- Haori
setg('Haori',{"Kuro-montsuki haori":'Haori',"Merchant's lined haori":'Haori',"Women's haori":'Haori','Hanten':'Related jackets','Happi':'Related jackets'})
ent('Haori','Hifu','Sleeveless padded outer vest worn by young children over their kimono.','Haori','Related jackets')
ent('Haori','Michiyuki','Double-breasted overcoat with a square neckline and dual fastenings.','Haori','Related jackets')
fin('Haori',['Haori','Related jackets'],"One entry is a named haori or related Japanese jacket, as Wikipedia's Haori article lists them.",
 "Haori forms and the related jackets in the See also section of Wikipedia's Haori article (whole page read). Complete: {n} of {n}.",'haori and related jackets')
# ---------- Ao dai
PRE,MOD='Before the modern áo dài','Modern áo dài (1930s onward)'
setg('Ao dai',{'Áo ngũ thân':PRE,'Áo tứ thân':PRE,'Áo gấm':PRE,'Áo dài Le Mur':MOD,'Raglan-sleeve áo dài':MOD,'Boat-neck áo dài':MOD,'Áo dài hippy':MOD})
for n,g,d in [('Áo tấc',PRE,'Loose shirt of the older designs.'),('Áo đối khâm',PRE,'Parallel-flap robe.'),('Áo viên lĩnh',PRE,'Round-collar robe, shown on a 14th-century figure.'),('Áo giao lĩnh',PRE,'Cross-collar robe worn by all social classes before the 19th century.'),('Áo trực lĩnh',PRE,'Straight-collar robe.'),('Áo tứ điên',PRE,'Early 17th century Lê dynasty garment shown in the Sancai Tuhui.'),('Áo dài mini',MOD,'Practical version with slits above the waist and panels to the knee, 1960s–70s.'),('Áo dài cách tân',MOD,'Recent version with shorter flaps just below the knee.')]: ent('Ao dai',n,d,'%C3%81o_d%C3%A0i',g)
fin('Ao dai',[PRE,MOD],"One entry is a named historical garment or style of the áo dài, as Wikipedia's Áo dài article lists them.",
 "Garments and styles named in Wikipedia's Áo dài article (whole page read, 120,098 characters), sectioned by period. Complete: {n} of {n}; áo nhật bình is a related women's garment and áo dài Việt Nam a name, not a cut.",'by period')
# ---------- Baju kurung
for e in K['Baju kurung & baju Melayu']['x']:
    e['g']={'Teluk Belanga':'Johor','Cekak Musang':'Johor','Baju Kurung Kedah':'Kedah','Baju Kurung Riau-Pahang':'Pahang','Baju Puteri Perak':'Perak','Baju Kurung Moden':'Modern','Kebarung':'Modern'}[e['n']]
ent('Baju kurung & baju Melayu','Baju Melayu','Men\'s counterpart of the baju kurung, in cekak musang and teluk belanga versions that differ mainly in pocket placement.','Baju_kurung','Men\'s')
fin('Baju kurung & baju Melayu',['Johor','Kedah','Pahang','Perak','Modern',"Men's"],"One entry is a named regional style of the baju kurung or baju Melayu, as Wikipedia's Baju kurung article lists them.",
 "Styles named in Wikipedia's Baju kurung article (whole page read), sectioned by Malaysian state; Kebarung follows the Kebaya article. Complete: {n} of {n}.",'by region')
# ---------- Sherwani
setg('Sherwani',{'Lucknowi sherwani':'India','Achkan':'India'})
ent('Sherwani','Balaba (chapkan)','Persian cape; the earliest ancestor of the sherwani.','Sherwani','Ancestors and namesakes',role='origin')
ent('Sherwani','Chokha','Folk dress of the Shirvan region of Azerbaijan, resembling the sherwani and a possible source of its name.','Sherwani','Ancestors and namesakes')
fin('Sherwani',['India','Ancestors and namesakes'],"One entry is a named form of the sherwani or a garment the article gives as its ancestor.",
 "Forms named in Wikipedia's Sherwani article (whole page read). Angarkha, Nehru jacket and Jodhpuri have their own kinds. Complete: {n} of {n}.",'by origin')
# ---------- Bandhgala
setg('Bandhgala & Nehru jacket',{'Jodhpuri bandhgala':'Jodhpur','Nehru jacket':'Nehru jacket'})
for n,d in [('Bago','Court tunic adopted under Raja Udai Singh in Jodhpur.'),('Dagali','Structured layered over-garment later used in Jodhpur.'),('Gudadi','Structured layered over-garment later used in Jodhpur.')]: ent('Bandhgala & Nehru jacket',n,d,'Jodhpuri','Jodhpur court ancestors')
fin('Bandhgala & Nehru jacket',['Jodhpur court ancestors','Jodhpur','Nehru jacket'],"One entry is the bandhgala, its Nehru derivative or a Jodhpur court garment the article names as an ancestor.",
 "Forms named in Wikipedia's Jodhpuri article (whole page read) plus the Nehru jacket article. Jama and angrakha are named as ancestors and not separate entries here (Angarkha has its own entry under Kurta). Complete: {n} of {n}.",'by origin')
# ---------- Lehenga
LC='Lehenga choli'
setg(LC,{'Ghagra choli':'North and west India'})
for n,g,d,u in [('Chaniya choli','Gujarat','Gujarat form linked to Garba festival wear.',''),('Rogan-painted ghagra choli','Gujarat','Hand-painted rogan work for festivals and weddings.',''),('Luanchari','Himachal Pradesh','Gaddi dress with the choli stitched to the lehenga, making a one-piece garment.',''),('Gunyu choli (Faria)','Nepal','Khas Nepali variant.',''),('Langa voni','South India','Unmarried girls\' coming-of-age garment.',''),('Ghagri','Historical','Ancient narrow skirt about 6 feet long, still seen on Jain nuns.',''),('Bhairnivasani','Historical','Ancient skirt that preceded the ghagri.','')]: ent(LC,n,d,'Gagra_choli',g)
fin(LC,['Historical','North and west India','Gujarat','Himachal Pradesh','Nepal','South India'],"One entry is a named regional or historical form of the ghagra or lehenga choli, as Wikipedia's Ghagra choli article lists them.",
 "Forms named in Wikipedia's Gagra choli article (whole page read), sectioned by region; pavadai is the Tamil skirt name and lehenga-style sari and gharara are mentioned without description. Complete: {n} of {n}.",'by region')
# ---------- Shalwar extras
ent('Shalwar kameez','Saraiki shalwar suit','Suits of the Saraiki region of Pakistan; named in the navigation template.','Shalwar_kameez','Punjab')
ent('Shalwar kameez','Punjabi ghagra suit','Pakistani suit named in the navigation template.','Shalwar_kameez','Punjab')
K['Shalwar kameez']['sel']=K['Shalwar kameez']['sel'].replace(re.search(r'Covers \d+ of the styles.*?not read\.',K['Shalwar kameez']['sel']).group(0),'Page read to its end (187,298 characters). Complete: %d of %d styles named in the text and navigation template.'%(len(K['Shalwar kameez']['x']),len(K['Shalwar kameez']['x'])))
# ---------- Sarong: finish
for n,d in [('Kain panjang','Indonesian name for the sarong-type wrap cloth.')]: ent('Sarong & wrap cloth',n,d,'Sarong','Maritime Southeast Asia')
for e in K['Sarong & wrap cloth']['x']:
    if e['n']=='Jarik': e['a']='Kain jarik'
k=K['Sarong & wrap cloth'];k['sel']=re.sub(r'Covers \d+ of about 85 names there \(characters 0 to 100,000 of 134,695 read; the rest not read\)\.','Page read to its end (134,695 characters). Complete: %d of %d wrap-cloth garments named; the many synonyms and spellings the article lists (sarung, kain sarung, kikoy, pareo, izaar, maqtab, mewaz) are aliases of an entry or of the kind.'%(len(k['x']),len(k['x'])),k['sel'])
# ---------- Poncho / Kaftan / Kimono / Sari tails
k=K['Poncho'];k['sel']=re.sub(r'Covers (\d+) of the (\d+) regional ponchos in the text read\.',lambda m:'Page read to its end. Complete: %s of %s regional ponchos named.'%(m.group(1),m.group(2)),k['sel']).replace('(characters 0 to 100,000 of 109,474 read)','(whole page read)')
ent('Kaftan','Royal Algerian caftan','Algerian court form shown in the article image captions.','Kaftan','North Africa')
k=K['Kaftan'];k['sel']=re.sub(r'\(characters 0 to 100,000 of 138,879 read\)','(whole page read)',k['sel']);k['sel']=re.sub(r'Covers \d+ of the forms in the text read\.','Complete: %d of %d forms named.'%(len(k['x']),len(k['x'])),k['sel'])
k=K['Kimono'];k['sel']=re.sub(r'\(characters 0 to 100,000 of 217,652 read; the rest, including men\'s types, not read\)','(characters 0 to 200,000 of 217,652 read; the last 17,652, references and navigation, unread)',k['sel']);k['sel']=re.sub(r'Covers \d+ types\.','Covers %d types, every type named in the text read; juban and hadajuban are undergarments and not entries.'%len(k['x']),k['sel'])
k=K['Sari'];k['sel']=k['sel'].replace('(characters 0 to 200,000 of 205,520; the remaining 5,520 were not read)','(whole page read to its end)').replace('Covers %d of the sari forms in the article text read'%len(k['x']),'Complete: %d of %d sari forms in the article'%(len(k['x']),len(k['x'])))
# ---------- Dupatta
setg('Dupatta',{'Phulkari dupatta':'Punjab','Bandhani dupatta':'Gujarat and Rajasthan','Banarasi dupatta':'Uttar Pradesh','Kota Doria dupatta':'Gujarat and Rajasthan'})
ent('Dupatta','Khada dupatta','Distinct Hyderabad style of the Deccan, shown in a 20th-century photograph.','Dupatta','Deccan')
ent('Dupatta','Ghoonghat','Dupatta used to cover the head and face, customary for new brides.','Dupatta','Whole subcontinent')
ent('Dupatta','Pachaura','Nepali name for a dupatta or similar shawl.','Dupatta','Nepal')
fin('Dupatta',['Punjab','Uttar Pradesh','Gujarat and Rajasthan','Deccan','Whole subcontinent','Nepal'],"One entry is a named regional dupatta, as Wikipedia's Dupatta article lists them; weave and decoration are attributes.",
 "Types named in Wikipedia's Dupatta article (whole page read), sectioned by region; Kota Doria follows the Gaatha craft page. Regional synonyms (chunni, chunari, odhni, orna and others) are aliases. Complete: {n} of {n}.",'by region')
# ---------- Dhoti sel ok. Beizi
setg('Beizi',{'Song beizi':'China','Ming pifeng':'China','Half-sleeve beizi':'China','Sleeveless beizi':'China','Hechang':'China'})
for n,g,d in [('Changyi','China','Term for the beizi when worn by men.'),('Dachang','China','Version with large sleeves and front knotted ties.'),('Nüpi and pi','China','Chinese opera costumes, women\'s and men\'s formal forms derived from the Ming pifeng.'),('Hakchangui','Korea','Joseon-era Korean form of the hechang.'),('Áo nhật bình','Vietnam','Nguyen-dynasty casual outer garment derived from the Ming pifeng.')]: ent('Beizi',n,d,'Beizi',g)
fin('Beizi',['China','Korea','Vietnam'],"One entry is a named form of the beizi and its relatives, as Wikipedia's Beizi article lists them.",
 "Forms named in Wikipedia's Beizi article (whole page read), sectioned by country. Complete: {n} of {n}; chuozi is an alias of beizi.",'by country')
# ---------- Tang jacket
setg('Tang jacket',{'Magua':'Qing dynasty','APEC tangzhuang':'2001'})
ent('Tang jacket','2014 APEC Tang suit jacket','Updated maroon, green and blue style worn at the 2014 APEC summit.','Tangzhuang','2014')
fin('Tang jacket',['Qing dynasty','2001','2014'],"One entry is a named form of the Tang jacket (tangzhuang) as Wikipedia's Tangzhuang article describes it.",
 "Forms named in Wikipedia's Tangzhuang article (whole page read), sectioned by year. Complete: {n} of {n}; 'Tang suit', 'Chinese jacket' and 'new tangzhuang' are names, not styles.",'by year')
# ---------- Mamianqun
setg('Mamianqun',{'Ming mamianqun':'Ming dynasty'})
for n,g,d in [('Yuehuaqun','Qing dynasty','Qing skirt with 12 gores, each a different colour.'),('Fengweiqun','Qing dynasty','Qing skirt recorded no later than c. 1750 and worn into the Republic.'),('Yulinqun','Qing dynasty','Late 19th-century skirt, popular in Beijing and still worn in Peking opera.'),('Langanqun','Qing dynasty','Skirt with sharp, usually black trims shaped like railings.'),('Mangqun','Qing dynasty','Bridal skirt with an embroidered mang.'),('Baidiequn','Song dynasty','Second prototype from the tomb of Huang Sheng.'),('Liangpianqun (xuanqun)','Song dynasty','Unpleated two-piece wrap skirt.'),('Ganshangqun','Song dynasty','Southern Song skirt, later called shangmaqun and maqun.')]: ent('Mamianqun',n,d,'Mamianqun',g)
fin('Mamianqun',['Song dynasty','Ming dynasty','Qing dynasty'],"One entry is a named Chinese skirt, the mamianqun and the skirts the Mamianqun article lists beside it.",
 "Skirts named in Wikipedia's Mamianqun article, sectioned by dynasty. Covers {n} skirts in characters 0 to 100,000 of 131,292 read; the last 31,292 characters were not read.",'by dynasty')
# ---------- Ruqun
setg('Ruqun',{})
for e in K['Ruqun']['x']: e['g']={'Qixiong ruqun':'Sui–Tang','Qiyao ruqun':'Sui–Tang','Gaoyao ruqun':'Sui–Tang','Aoqun':'Qing','Shanqun':'Sui–Tang','Qungua':'Qing and modern','Xiuhefu':'Qing and modern'}[e['n']]
ent('Ruqun','Tanling ruqun','Ruqun with a U-shaped upper garment.','Ruqun','Sui–Tang')
fin('Ruqun',['Sui–Tang','Qing','Qing and modern'],"One entry is a named type of ruqun, as Wikipedia's Ruqun article lists them.",
 "Types named in Wikipedia's Ruqun article (whole page read) plus the types carried from the structure pass, sectioned by period. Complete: {n} of {n} for the article's Types section (Qixiong, Qungua, Tanling, Xiuhefu); other entries are earlier forms from the same article.",'by period')
# ---------- Qipao
for e in K['Qipao']['x']: e['g']='China'
K['Qipao']['x'][2]['a']='Cantonese-style · Guangdong style'
ent('Qipao','Jiangnan cheongsam','Su-style cheongsam from the Jiangnan water towns, with calligraphy and painting motifs and floral embroidery.','Cheongsam','China')
fin('Qipao',['China'],"One entry is a named regional style of the qipao (cheongsam), as Wikipedia's Cheongsam article lists them.",
 "Regional styles named in Wikipedia's Cheongsam article (whole page read, 168,264 characters). Complete: {n} of {n}; Qi Lolita is a Lolita fashion variant, not a regional style.",'by city')
# ---------- Barong, Terno
for e in K['Barong Tagalog']['x']: e['g']='19th century' if e['n'] in('Classic barong','Barong mahaba','Baro cerrada','Pinukpok barong') else '20th century'
fin('Barong Tagalog',['19th century','20th century'],"One entry is a named style of the barong tagalog, as Wikipedia's Barong tagalog article lists them.",
 "Styles named in Wikipedia's Barong tagalog article (characters 0 to 100,000 of 104,085 read; the last 4,085 unread), sectioned by century. Covers {n} styles.",'by period')
for e in K['Terno & Filipiniana']['x']: e['g']={"Baro't saya":'Baro\'t saya','Traje de mestiza':'Baro\'t saya','Terno':'Terno','Balintawak':'Terno','Kimona':'Visayas'}[e['n']]
fin('Terno & Filipiniana',["Baro't saya",'Terno','Visayas'],"One entry is a named variant of the baro't saya (Filipiniana), as Wikipedia's Baro't saya article lists them.",
 "Variants named in Wikipedia's Baro't saya article (whole page read); Filipiniana is the collective term. Complete: {n} of {n}.",'by form')
# ---------- Yukata: dyeing methods out
k=K['Yukata']
gone=[e['n'] for e in k.pop('x')]
k['tt'].append(['Cloth',['Chūsen dyeing','Nagaita-chūgata dyeing']])
k['ve']={'t':'Named cloths covered by the visual-art taxonomy','items':[{'n':'Yukata dyeing methods','e':gone}]}
k['nl']="This kind has no named entries."
k['sel']="Wikipedia's Yukata article (whole page read) names no yukata types, only the dyeing methods chūsen and nagaita-chūgata; these are textile techniques, now values of the Cloth attribute and covered by the visual-art taxonomy. Complete: 0 of 0 types."+CL.replace('Cloth traditions are not entries: the Cloth attribute names them and the','')
k.pop('xg',None)
# ---------- Charro
for e in K['Charro suit']['x']: e['g']='Charro grades'
setg('Charro suit',{})
ent('Charro suit','Traje de media gala','Second level in the 1960 ranking of the National Charro Federation, above faena.','Charro_outfit','Charro grades')
ent('Charro suit','Traje de gran gala','Fourth level in the same ranking.','Charro_outfit','Charro grades')
ent('Charro suit','Traje de etiqueta','Highest and most formal level.','Charro_outfit','Charro grades')
for g in K['Charro suit']['tt']:
    if g[0]=='Grade' and 'Etiqueta' not in g[1]: g[1].append('Etiqueta')
fin('Charro suit',['Charro grades'],"One entry is a named grade of the charro outfit, as Wikipedia's Charro outfit article ranks them.",
 "Grades named in Wikipedia's Charro outfit article (whole page read), by formality. Complete: {n} of {n} (faena, media gala, gala, gran gala, etiqueta; the mariachi gala version is the second version of the gala).",'by formality')
# ---------- Guayabera
for e in K['Guayabera']['x']: e['g']='Cuba and Yucatán'
for n,g,d in [('Chacabana','Caribbean','Dominican Republic name for the guayabera.'),('Shirt-jac','Caribbean','Guyanese similar or identical shirt.'),('Bush jacket (Jamaica)','Caribbean','Jamaican local name for the guayabera.')]: ent('Guayabera',n,d,'Guayabera',g)
fin('Guayabera',['Cuba and Yucatán','Caribbean'],"One entry is a named regional form or local name of the guayabera, as Wikipedia's Guayabera article gives them.",
 "Forms and names in Wikipedia's Guayabera article (whole page read), sectioned by region. Complete: {n} of {n}; the baróng tagalog and the Western shirt are named as related garments and are not entries.",'by region')
# ---------- Huipil
HC,HO,HG,HM='Chiapas','Oaxaca','Guatemala','Other Mexico'
setg('Huipil',{'Chiapas Maya huipil':HC,'Oaxaca huipil':HO,'Guatemalan Maya huipil':HG})
for n,g,d in [('Santa María Magdalena ceremonial huipil',HC,'Used by high-ranking women and to dress saints.'),('Zinacantán ceremonial huipil',HC,'White cotton with feather work.'),('Tzotzil ceremonial huipil',HC,'White feathers on chest and hem.'),
('Chinanteca gala huipil',HO,'Red wedding huipil of Ojitlán; the pavo is the special-occasion huipil and pájaros y palomas the most economical.'),('Isthmus of Tehuantepec huipil',HO,'Short velvet huipil for everyday wear, white face-framing huipil for special occasions, huipil de tapar (bidaniro) as head covering and a blouse huipil about 60 cm long.'),('Pinotepa Nacional wedding huipil',HO,'White wedding huipils of Pinotepa Nacional; Chopan and Cotzocón make similar ones.'),('Mixtec wool huipil',HO,'Wool huipils of Ocotepec and Cuquila, high in the Mixtec mountains.'),('Yalaltec huipil',HO,'Simple huipil decorated only on chest and back panels.'),('Jamiltepec huipil',HO,'Women from other areas taboo from wearing it.'),('Amuzgo huipil',HO,'Brocade huipils of the Amuzgo people, including Xochistlahuaca.'),('Tlapanec huipil',HM,'Huipil of the Tlapanec people, c. 1908 image caption.'),('La Malinche huipil',HM,'18th-century huipil in the National Museum of Anthropology.'),
('Patzún huipil',HG,'Guatemalan huipil, 1875–1890 image caption.'),('San Juan Sacatepéquez huipil',HG,'Kakchiquel Maya huipil, 1930s image caption.')]: ent('Huipil',n,d,'Huipil',g)
fin('Huipil',[HC,HO,HM,HG],"One entry is a named huipil of one people or town, as Wikipedia's Huipil article lists them; length and cloth are versions.",
 "Huipils named in Wikipedia's Huipil article (whole page read), sectioned by region. Complete: {n} of {n} named; local names for the garment (huanengo, b'ujk, nip, xighu, dzico) are aliases.",'by region')
# ---------- Pollera
setg('Pollera',{'Pollera de gala':'Panama','Pollera montuna':'Panama','Bolivian cholita pollera':'Bolivia and Peru'})
for e in K['Pollera']['x']:
    if e['n']=='Pollera de gala': e['v']=(e.get('v') or [])+[V('Talco al sol','gala variation using coloured fabric cutwork'),V('Talco en sombra','rarer gala variation with work beneath the fabric'),V('Santeña gala de labor','the most expensive gala de labor style')]
ent('Pollera','Pollera congo','Afro-Panamanian tradition, especially in Colón.','Pollera','Panama')
ent('Pollera','Pollera con basquiña','Worn in several Panamanian regions, without shoes in Darién.','Pollera','Panama')
ent('Pollera','Man-tumble skirt','Striped regional variation associated with Villa de Los Santos.','Pollera','Panama')
ent('Pollera','Peruvian pollera','Pleated skirt linked to Indigenous and mestizo women of Peru.','Pollera','Bolivia and Peru')
fin('Pollera',['Panama','Bolivia and Peru'],"One entry is a named type of pollera, as Wikipedia's Pollera article lists them; gala cutwork styles are versions.",
 "Types named in Wikipedia's Pollera article (whole page read), sectioned by country; pollera zaraza is an alias of the montuna. Complete: {n} of {n}.",'by country')
# ---------- Boubou
setg('Boubou & agbada',{'Grand boubou':'Senegal and Sahel','Agbada':'Nigeria','Babban riga':'Nigeria'})
for n,g,d in [('Tilbi','Senegal and Sahel','Intricately embroidered boubou of French West Africa, linked to Muslim marriage traditions.'),('Deraa','Mauritania','White or blue robe signalling Moor identity, with gold embroidery; the female variant is the caftan.'),('Babaringa','Senegal and Sahel','Named in the article as distinct from the agbada and grand boubou.')]: ent('Boubou & agbada',n,d,'Boubou_(clothing)',g)
fin('Boubou & agbada',['Senegal and Sahel','Mauritania','Nigeria'],"One entry is a named regional form of the boubou and its relatives, as Wikipedia's Boubou article lists them.",
 "Forms named in Wikipedia's Boubou article (whole page read), sectioned by region; the dashiki and Ghanaian smock have their own kinds, and the face-covering turbans (alasho, tagelmust, litham) are headwear. Complete: {n} of {n}.",'by region')
# ---------- Dashiki
for e in K['Dashiki']['x']: e['g']='Print'
ent('Dashiki','Dashiki suit','Formal set of dashiki, sokoto drawstring trousers and matching kufi; the usual groom\'s outfit.','Dashiki','Sets',v=[V('Traditional dashiki suit','thigh-length shirt'),V('Long dashiki suit','knee-length or longer shirt'),V('Lace dashiki suit','shirt of lace')])
fin('Dashiki',['Print','Sets'],"One entry is a named print or set of the dashiki, as Wikipedia's Dashiki article gives them.",
 "Forms named in Wikipedia's Dashiki article (whole page read): the Angelina print (also Miriam Makeba, Ya Mado) and the dashiki suit. Grand boubou, agbada and Senegalese kaftan sit in their own kinds. Complete: {n} of {n}.",'by form')
# ---------- Habesha
for e in K['Habesha kemis']['x']: e['g']='Shewa'
for n,g,d in [('Weraj tilet','Shewa','Vertical border running from chest to hem.'),('Gemash tilet','Shewa','Border on the lower half of the back.'),('Bale albo kemis','Shewa','Two-piece set with embroidered cotton trousers.'),('Gojjam Amhara dress','Gojjam','Dress of north-west Ethiopia with Zege embroidery.'),('Gondar Amhara dress','Gondar','Dress of north-west Ethiopia.'),('Wollo Amhara dress','Wollo','Dress of north-east Ethiopia, in raya and dir-mag weaves.'),('Tiftif dress','Shewa','Worn with a tiftif mekenet; region not stated in the article.')]: ent('Habesha kemis',n,d,'Habesha_kemis',g)
fin('Habesha kemis',['Shewa','Gojjam','Gondar','Wollo'],"One entry is a named regional form of the habesha kemis, as Wikipedia's Habesha kemis article lists them.",
 "Forms named in Wikipedia's Habesha kemis article (whole page read), sectioned by region; the fabrics (menen, saba, fetel) are cloth traditions for the visual-art taxonomy. Complete: {n} of {n}.",'by region')
# ---------- Abaya
setg('Abaya',{'Manteau':'Iran','Bisht':'Arabian Peninsula'})
for n,g,d in [('Jilbab (Indonesia)','Indonesia','Indonesian style worn with a headscarf, often brightly coloured or patterned.'),('Black Gulf abaya','Arabian Peninsula','Gulf states abayas tend to be black.'),('Emirati abaya','Arabian Peninsula','Light crêpe, georgette and chiffon in beige and white.')]: ent('Abaya',n,d,'Abaya',g)
fin('Abaya',['Arabian Peninsula','Iran','Indonesia'],"One entry is a named regional form of the abaya, as Wikipedia's Abaya article gives them; front opening and fabric are attributes.",
 "Forms named in Wikipedia's Abaya article (whole page read) with Manteau and Bisht from the structure pass, sectioned by region. Complete: {n} of {n}; front-open, front-closed, caftan-cut and embroidered abayas are attributes.",'by region')
# ---------- Dirndl
DT,DR='Dirndl types','Regional tracht'
setg('Dirndl',{'Wallach fashion dirndl':DT,'Tracht dirndl':DT})
for n,g,d in [('Wedding dirndl',DT,'Ceremonial version worn by brides in Alpine Germany, Austria and South Tyrol.'),('Winter dirndl',DT,'Heavier skirts and sleeves in brown, deep green or dark blue.'),('Sisi dress',DT,'Rustic dress based on the peasant dirndl, promoted by Empress Elisabeth around 1875.'),('African dirndl',DT,'Fusion design in African printed fabric, shown at Oktoberfest in 2019.'),
('Wachauer Tracht',DR,'Blue polka-dotted regional dress of the Wachau, Austria; the everyday version is the Wachauer Dirndl.'),('Miesbacher Tracht',DR,'Official Alpine tracht type in Bavaria.'),('Werdenfelser Tracht',DR,'Official Alpine tracht type in Bavaria.'),('Inntaler Tracht',DR,'Official Alpine tracht type in Bavaria.'),('Chiemgauer Tracht',DR,'Official Alpine tracht type in Bavaria.'),('Berchtesgadener Tracht',DR,'Official Alpine tracht type in Bavaria.'),('Isarwinkler Tracht',DR,'Official Alpine tracht type in Bavaria.'),('Heiligen Tracht',DR,'Holy folk costume of Tyrol, not worn on secular occasions involving drinking.'),('Bernese Tracht',DR,'Swiss regional tracht from Bern, worn at national and seasonal festivities.'),('Liechtenstein national dress',DR,'Black skirt and white blouse with silver-embroidered bodice.'),('Gutach valley tracht',DR,'Black Forest tracht sometimes mistaken for a dirndl.')]: ent('Dirndl',n,d,'Dirndl',g)
fin('Dirndl',[DT,DR],"One entry is a named dirndl type or regional tracht, as Wikipedia's Dirndl article lists them; length and bodice are attributes.",
 "Types named in Wikipedia's Dirndl article (whole page read, 158,739 characters), sectioned into dirndl types and regional tracht. Complete: {n} of {n}; Trachtenmode, Landhausmode, Wiesntracht and the dirndl skirt and bra are general terms or accessories, not entries.",'by kind')
# ---------- Lederhosen
for e in K['Lederhosen']['x']: e['g']='Alps'
ent('Lederhosen','Swabian lederhosen','Knee-length cuffed style from Swabia and the Black Forest, traditionally black, or yellow for winemakers.','Lederhosen','Swabia')
fin('Lederhosen',['Alps','Swabia'],"One entry is a named regional cut of the lederhosen, as Wikipedia's Lederhosen article lists them; seam count is an attribute.",
 "Cuts named in Wikipedia's Lederhosen article (whole page read), sectioned by region; Bundhosen is the long form and the 3, 5, 7 and 9-seam variants are the Seams attribute. Complete: {n} of {n}.",'by region')
# ---------- Kilt
for e in K['Kilt']['x']: e['g']='Highland' if e['n'] in('Belted plaid (great kilt)','Small kilt (fèileadh beag)','Eight-yard tailored kilt') else 'Contemporary'
for n,g,d in [('Irish pipe band kilt','Celtic nations','Solid-colour kilt, usually saffron or green, rather than tartan.'),('Welsh cilt','Celtic nations','Variant adopted in Wales as a Celtic identity garment.'),('Cornish cilt','Celtic nations','Variant adopted in Cornwall as a Celtic identity garment.'),('Utility kilt','Contemporary','US name for contemporary kilts, often for outdoor or workwear.'),('Contemporary hybrid kilt','Contemporary','Tartan-woven kilt blending traditional and modern features.'),('Lacrosse kilt','Contemporary','Simple kilt worn by female lacrosse and field hockey players over compression shorts.')]: ent('Kilt',n,d,'Kilt',g)
fin('Kilt',['Highland','Celtic nations','Contemporary'],"One entry is a named form of the kilt, as Wikipedia's Kilt article lists them; tartan is the Cloth attribute.",
 "Kilts named in Wikipedia's Kilt article (characters 0 to 100,000 of 126,472 read; the last 26,472 unread), sectioned by tradition; the 5.11 tactical duty kilt is workwear and left out. Covers {n} kilt forms.",'by tradition')
# ---------- Vyshyvanka
for e in K['Vyshyvanka']['x']: e['g']='Designer'
ent('Vyshyvanka','Bukovina-style vyshyvanka','Regional style from Bukovina shown in the article gallery.','Vyshyvanka','Regional')
fin('Vyshyvanka',['Regional','Designer'],"One entry is a named regional style or designer version of the vyshyvanka.",
 "Styles named in Wikipedia's Vyshyvanka article (characters 0 to 100,000 of 126,069 read; the last 26,069 unread) and the Vita Kin article. Covers {n} styles.",'by origin')
# ---------- Gakti
for e in K['Gákti']['x']: e['g']='Sápmi'
fin('Gákti',['Sápmi'],"One entry is a named Sámi garment form.",
 "Wikipedia's Gákti article (whole page read) names no regional types, only a Västerbotten embroidered collar pattern; the two entries follow the Gákti and Duodji articles. Complete: {n} of {n} named forms.",'by people')
# ---------- Bunad done. Wrap robe
W2='Wrap robe'
for e in K[W2]['x']: e['g']={'Deel':'Mongolia','Gho':'Bhutan','Chapan':'Central Asia'}[e['n']]
for n,g,d in [('Khalkha Mongol deel','Mongolia','Deel with round opening edges at the upper chest.'),('Buryat deel','Mongolia','Deel with square opening edges at the upper chest.'),('Nekhii deel','Mongolia','Western-design fur overcoat; sawkhin deel is the leather one.')]: ent(W2,n,d,'Deel_(clothing)',g)
for e in K[W2]['x']:
    if e['n']=='Chapan': e['v']=(e.get('v') or [])+[V('Chapan cape','Afghan cape form, often worn by Hamid Karzai')]
fin(W2,['Mongolia','Bhutan','Central Asia'],"One entry is a named wrap robe or regional form of it, as the Deel, Gho and Chapan articles give them.",
 "Forms named in Wikipedia's Deel, Gho and Chapan articles (all whole pages read), sectioned by country; the kira is mentioned in Gho without description, and the kera belt, tego jacket and kabney are accessories. Complete: {n} of {n}.",'by country')
# ---------- Pacific
for e in K['Pacific island dress']['x']: e['g']={'Holokū':'Hawaii','Muʻumuʻu':'Hawaii','Puletasi':'Samoa and Tonga','Robe mission':'New Caledonia','Meri blaus':'Papua New Guinea','Wau':'Marshall Islands','ʻAhu māmā rūʻau':'Tahiti'}[e['n']]
for n,g,d in [('Puletaha','Samoa and Tonga','Tongan two-piece form with a skirt.'),('ʻAhu tua','Tahiti','Older Tahitian name, referring to the colonial empire.'),('Mother Hubbard (Kiribati)','Kiribati','1960s–1970s garment of Tarawa worn with a lavalava or skirt.')]: ent('Pacific island dress',n,d,'Mother_Hubbard_dress',g)
fin('Pacific island dress',['Hawaii','Tahiti','Samoa and Tonga','New Caledonia','Marshall Islands','Kiribati','Papua New Guinea'],"One entry is a named Pacific form of the Mother Hubbard dress, as Wikipedia's Mother Hubbard dress article lists them.",
 "Forms named in Wikipedia's Mother Hubbard dress article (whole page read), sectioned by island group; robes popinées is an alias of the robe mission. Complete: {n} of {n}.",'by island group')
# ---------- remaining kinds: kinds not re-checked
for kn in ['Trachtenjanker','Bombachas & gaucho dress','Zhongshan suit','Toub','Kaba and slit','Southern African dress','Mamianqun']:
    pass
json.dump(part,open(P,'w'),ensure_ascii=False,indent=1)
tot=sum(len(k.get('x',[])) for k in K.values())
print('entries',tot)
# list kinds with x lacking g
for kn,k in K.items():
    if k.get('x') and any(not e.get('g') for e in k['x']): print('no g:',kn,len(k['x']))
