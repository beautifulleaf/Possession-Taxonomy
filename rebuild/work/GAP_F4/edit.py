import json,os
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'out/F4.json'))
W='https://en.wikipedia.org/wiki/'
K={k['n']:k for dp in d['depts'] for sh in dp['s'] for k in sh['k']}
def add(kind,rows,src,sel,nl=None):
    k=K[kind]; have={e['n'].lower() for e in k['x']}|{(e.get('a') or '').lower() for e in k['x']}
    for r in rows:
        n,y,desc=r[:3]; role=r[3] if len(r)>3 else None
        if n.lower() in have: continue
        e={'n':n,'a':'','d':desc,'mk':'','y':y,'s':src,'dt':'','v':[]}
        if role: e['role']=role
        k['x'].append(e)
    k['sel']=((k.get('sel') or '').rstrip()+' '+sel).strip()
    if nl and not k.get('nl'): k['nl']=nl
# Rosary
add('Rosary',[
('Chaplet of the Divine Mercy','','Five-decade devotion said on ordinary rosary beads.'),
('Chaplet of the Sacred Heart','','Thirty-three small beads, six large beads, a centrepiece, a crucifix and a Sacred Heart medal.'),
('Chaplet of the Precious Blood','','Thirty-three beads in seven groups, composed by Dom Francesco Albertini.'),
('Bridgettine rosary','','Six decades of ten beads with three further beads at the end.'),
('Chaplet of Saint Michael the Archangel','','Nine groups of four beads for the nine choirs of angels.'),
('Chaplet of Saint Joseph','','Fifteen groups of four beads, each one white and three purple.'),
('Little Crown of the Infant Jesus','','Three beads and twelve beads.'),
('Chaplet of Saint Anthony','','Thirteen sets of three beads.'),
('Chaplet of Saint Patrick','','Twelve beads for the twelve perils of Saint Patrick.'),
('Chaplet of Saint Philomena','','Three white beads and thirteen red beads.'),
('Chaplet of Saint Kateri Tekakwitha','','Eight brown, eight red and eight crystal beads.'),
('Chaplet of Our Lady of Tears','','Based on reported visions of the nun Amalia of Jesus Flagellated.'),
('Chaplet of the Holy Face','','Little chaplet honouring the Five Wounds: a cross, six large beads and thirty-three small beads.'),
('Chaplet of the Five Wounds of Jesus','','Chaplet of the Five Wounds; the page gives no bead count.'),
('Chaplet of the Holy Wounds','','Based on reported visions of Marie Martha Chambon.'),
('Chaplet of Our Lady of Czestochowa','','Nine beads, a crucifix and a medal of Our Lady of Czestochowa.'),
('Chaplet of Our Lady, Star of the Sea','','A Mount Carmel medal, three separate beads and twelve more.'),
('Crown of Stars','','Chaplet of the Immaculate Conception: three groups of four beads and a medal.'),
('Little Flower chaplet','','One large bead and twenty-four smaller beads.'),
('Chaplet of the Way of the Cross','','Fifteen groups of three beads among other elements.'),
('Blessed Sacrament beads','','A common chaplet; the page gives no details.'),
('Chaplet of the Holy Infant of Good Health','','Said on the standard Dominican rosary.'),
('Chaplet of Saint Anna Schaeffer','','One large bead and twenty-four smaller beads.'),
],W+'Chaplet_(prayer)','Chaplet_(prayer) lists 24 chaplets: Complete: 24 of 24 (the Seven Sorrows chaplet is the Servite rosary already listed).')
# Scapular
add('Scapular',[
('Scapular of the Most Blessed Trinity','1193','White scapular, one of the 18 small scapulars the article lists as approved.'),
('Scapular of Our Lady of Ransom','1218','White scapular, one of the 18 approved small scapulars.'),
('Scapular of the Seven Sorrows of Mary','1255','Black scapular tied to the Servite confraternity.'),
('Blue Scapular of the Immaculate Conception','1617','Blue scapular with many indulgences attached.'),
('Scapular of the Most Precious Blood','','Red scapular; the article gives no year.'),
('Black Scapular of the Passion','1720','One of the 18 approved small scapulars.'),
('Red Scapular of the Passion','1846','One of the 18 approved small scapulars.'),
('Scapular of Help of the Sick','1860','Black scapular tied to the confraternity of St Camillus de Lellis.'),
('Scapular of the Immaculate Heart of Mary','1877','One of the 18 approved small scapulars; the article gives conflicting colours.'),
('Scapular of Saint Michael the Archangel','1880','Blue and black scapular.'),
('Scapular of Saint Benedict','1882','One of the 18 approved small scapulars.'),
('Scapular of the Holy Face','1885','Christ-centred scapular, also called the Veronica.'),
('Scapular of Our Lady of Good Counsel','1893','White scapular.'),
('Scapular of Saint Joseph','1898','White scapular.'),
('Scapular of the Sacred Heart of Jesus','1900','White scapular.'),
('Scapular of the Sacred Hearts of Jesus and Mary','1901','One of the 18 approved small scapulars.'),
('Scapular of Saint Dominic','1903','White scapular.'),
('Fivefold Scapular','','Named in the article with its own page; no year given.'),
('Scapular of Our Lady of Walsingham','','Popular devotion in the Anglican Church.'),
],W+'Scapular','Complete: 21 of 21 scapulars named in the article (Brown and Green were already listed).')
# Evil eye
add('Evil-eye charm',[
('Cornicello','','Twisted horn-shaped amulet of red coral, gold or silver from southern Italy.'),
('Cimaruta','','Italian evil-eye amulet.'),
('Lunula','','Italian evil-eye amulet.'),
('Fascinus','','Ancient Roman phallic charm worn as pendant or ring, or carved on buildings.'),
('Kitab','','Amulet made by a debtera and worn by Ethiopian Christians against buda.'),
('Muska','','Turkish triangular packet holding a sacred verse.'),
('Gris-gris','','Senegalese talisman made by a marabout.'),
('Cowrie shell bracelet','','Senegalese bracelet said to absorb negative energy.'),
('Azabache bracelet','','Puerto Rican bracelet with a fist-shaped black or red coral amulet.'),
('Jumbie beads','','Trinidadian jewellery of rosary pea seeds against maljo.'),
('Drishti bommai','','Picture of a fierce ogre hung in Indian homes or vehicles.'),
('Albanian thunderstone pendant','','Worn by cattle or pregnant women for luck and against the evil eye.'),
('Dordolec','','Albanian protective house doll in human or animal form.'),
('Ta\'awiz','','Pakistani amulet against the evil eye.'),
('Red string bracelet','','Kabbalistic bracelet worn against the evil eye.'),
('Assyrian blue bead','','Blue or turquoise bead with eye-like holes worn on a necklace.'),
],W+'Evil_eye','Evil eye page read to character 200,000 (all but the references); 18 charms are named with a description; the closing navigation box lists further names (Corno, Witch ball, Takrut, Palad khik and others) with no description and these are not added. Covers 18 of the described charms.')
# Crucifix
add('Crucifix & devotional cross',[
('Altar cross','9th century (manuscript); 12th century (earliest extant)','Cross on a flat base that stands on a church altar; earliest extant example is at the Great Lavra, Mount Athos.'),
('Blessing cross','','Hand cross used by priests of Eastern Catholic and Orthodox churches to bless the faithful.'),
('Processional cross','','Cross carried at the head of religious processions.'),
('Lalibela cross','','Ethiopian processional cross named as a sub-type.'),
('Pectoral cross','','Large cross worn on the chest by some clergy.'),
('Crux gemmata','','Gem-inlaid cross with Alpha and Omega hanging from its arms.'),
('Rood','','Large crucifix set high in a medieval church, often on a rood screen.'),
('Cross necklace','','Small cross or crucifix worn as a pendant.'),
('Wolf cross','c. 11th century','Silver pendant from Foss, Iceland, that may be a cross or Thor\'s hammer.'),
('Nestorian cross','','Church of the East cross shown on a stele.'),
('Coptic Orthodox blessing cross','','Blessing cross of the Coptic Orthodox tradition.'),
],W+'Christian_cross_variants','Page read in full (200,000 characters): 16 of its 94 variants are made as objects and now listed (the 5 from the earlier pass plus 11); the rest are heraldic shapes, symbols and monuments such as high, wayside and battlefield crosses.')
K['Crucifix & devotional cross']['sel']=K['Crucifix & devotional cross']['sel'].replace('Covers 5 of 94.','')
# Incense burner
add('Incense burner',[
('Hill censer','Han dynasty, popular under Emperor Wu (141-87 BCE)','Chinese boshanlu shaped like a mountain so the smoke looks like mist round a peak.'),
('Scenting globe','1st century BCE','Chinese xiangqiu: pierced metal globe with an incense cup on gimbals, used to perfume bedding.'),
('Shoulu','medieval','Long-handled Chinese hand censer for Buddhist and Daoist ritual.'),
('Koro','late 17th century (Kakiemon example)','Japanese globular three-footed incense burner used at tea ceremonies.'),
('Mabkhara','11th-13th century (bronze, brass)','Openwork Islamic burner, often lynx or lion shaped.'),
('Dabqaad','','Somali incense burner similar to the mabkhara.'),
('Incensario','Teotihuacan 100-600 CE; Maya 600-900 CE','Ceramic Mesoamerican incense burner.'),
('Dhunachi','','Hindu earthen censer with a flared body and curved handle.'),
('Pastille burner','early 19th century','Ceramic burner for incense pastilles, used in British homes.'),
('Perfuming pan','','Flat long-handled vessel carried in English churches to scent services.'),
('Xunlu','','Chinese brazier for fumigating and perfuming.'),
('Tiangong censer','','Chinese censer used in worship of the Jade Emperor.'),
('Egyptian incense burner','Fifth Dynasty (oldest example)','Early Egyptian burner.'),
],W+'Censer','Censer and Incense pages read (100,000 characters of Incense): Covers 14 of the 19 burner types in Censer; the rest are thuribles (listed under Thurible & hand censer), a ritual tripod (ting) and a Qing animal-shaped burner.')
# Thurible
add('Thurible & hand censer',[
('Western thurible','','Metal vessel on chains, about the size of a coffee pot, used in Catholic, Anglican and some Lutheran churches.'),
('Botafumeiro','','Silver censer about 1.5 m tall and 55 kg, swung from the ceiling of Santiago de Compostela cathedral.'),
('Katzion','','Greek Orthodox hand censer without chains, used on Mount Athos.'),
('Gozbert censer','medieval','Thurible at Trier cathedral in an architectural form inspired by the Temple of Solomon.'),
],W+'Censer','Complete: 5 of 5 Christian censers in Censer (the chain censer is the Orthodox kadilo).')
# Ritual incense
add('Ritual incense',[
('Bakhoor','','Arabian paste incense chips or blocks burned for weddings, Fridays and household perfuming.'),
('Neriko','','Japanese kneaded paste incense.'),
('Incense coil','','Chinese extruded coreless incense that can burn for hours to days.'),
('Incense cone','1800s','Quick-burning Japanese incense form.'),
('Cored incense stick','','Incense on a bamboo or sandalwood core; the joss stick of Chinese folk religion.'),
('Dhoop','','Coreless incense stick that can be broken for portion control.'),
('Incense paper','','Resin-infused paper such as Papier d\'Armenie, folded, lit and blown out.'),
('Tibetan incense rope','','Powder rolled into twisted paper rope.'),
('Moskolibano','','Rolled Greek Orthodox incense resin, rose or jasmine scented.'),
('Dragon incense stick','','Large pillar-like stick burned outdoors at the Ghost Festival.'),
('Spiral incense','','Long-burning Chinese coil hung from temple ceilings.'),
('Ketoret','','Jewish Temple incense of stacte, onycha, galbanum and frankincense.'),
('Athonite paste incense','','Ground frankincense with essential oils, from the Mount Athos tradition.'),
],W+'Incense','Covers 15 of the 21 forms in the Incense article read to 100,000 characters; unburnt raw, powdered and hand-dipped forms and mosquito coils are treatments or products, not forms.')
# Joss paper
add('Joss paper',[
('Dabai Shoujin','','Large squares with a gold rectangle showing the Fu, Lu and Shou star gods, offered to heavenly deities.'),
('Yijin','','Large gold-rectangle squares offered to deities of any rank.'),
('Jiujin','','Large squares popular in southern Taiwan, now used for ancestors and earth guardians.'),
('Xiaoyin','','Small silver-rectangle squares burned for close relatives and spirits.'),
('Jingyi','','Paper printed with clothes, shoes and other items the dead need.'),
('Copper cash money','','Joss paper given to the newly deceased and unknown spirits.'),
('Gold paper','','Folded into gold ingot shapes before burning in Taiwan and Macau.'),
('Zhizha','','Papier-mache offerings of houses, cars, clothes and servants.'),
],W+'Joss_paper','Complete: 9 of 10 types named in the page (the Westernised paper goods row restates Hell Bank Notes).')
# Oil lamp
add('Oil lamp for worship',[
('Deepalakshmi','','Small South Indian brass lamp with one wick and a figure of Lakshmi on the back piece.'),
('Nilavilakku','','Tall South Indian brass or bronze lamp on a stand.'),
('Paavai vilakku','','Brass lamp shaped like a woman holding a vessel; large stone versions stand at temples.'),
('Thooku vilakku','','Brass or bronze lamp hung from a chain, often with several wicks.'),
('Kamba vilakku','','Raised brass lamp tower in some South Indian temples.'),
('Deepastambha','','Wooden or stone tower of light holding many lamps before temples.'),
('Deepavriksha','','Tree of light for homes: metal stand with lamp-bearing arms.'),
('Diya','','Basic earthen oil lamp used at Diwali.'),
('Five-wick lamp','','North Indian temple lamp with five wicks, fuelled with ghee, used in puja.'),
],W+'Oil_lamp','Covers 11 of the 23 lamps named in the Oil lamp article (read to 100,000 of 119,293 characters); the archaeological types (Herodian, Samaritan, Chi Rho, Byzantine, early Islamic) are not owned worship objects.')
add('Sanctuary lamp & lampada',[
('Orthodox sanctuary lamp','','Oil lamp kept burning in an Orthodox church, lit by the bishop at consecration.'),
('Kandili','','Oil lamp placed on the altar to light icons, used in Orthodox and Catholic churches.'),
],W+'Oil_lamp','Complete: 2 of 2 in Oil lamp.','One entry is a named form of sanctuary or altar lamp.')
# Spirit board
add('Spirit board',[],W+'Talking_board','Talking board article read: it names only the Ouija board as a product; the planchette is a part, and fuji writing is a practice. Complete: 1 of 1.')
# Book of Shadows
add('Book of Shadows',[
('Ye Booke of Ye Art Magical','before 1949','Gerald Gardner\'s handwritten first draft, with sections based on Ordo Templi Orientis rituals.'),
('Valiente\'s Book of Shadows','1950s','Doreen Valiente\'s rewrite of Gardner\'s text, which became the traditional Gardnerian text.'),
('The Tree','','Name of the Book of Shadows in Seax-Wica.'),
('The Book of Ways','','Name of the Book of Shadows in Devotional Wicca.'),
],W+'Book_of_Shadows','Complete: 5 of 5 real texts in the article (fictional books left out).')
# Lenormand
add('Lenormand deck',[('Das Spiel der Hoffnung','c. 1799','German game of chance by Johann Kaspar Hechtel; the Petit Lenormand is modelled on it.')],W+'Lenormand_cards','Complete: 2 of 2 named decks in Lenormand cards (the Grande Tableau is a layout).')
# Murti
add('Murti',[
('Utsava murti','','Festival image carried in annual processions.'),
('Yoni','','Aniconic symbol shaped into a murti, linked with Devi.'),
('Arcavatara','','Consecrated temple murti of Sri Vaishnavism, regarded as an accessible form of God.'),
('Vithoba murti','','Image of a form of Vishnu enshrined at Pandharpur.'),
('Istalinga','','Small Shiva emblem worn on the body by Virashaiva Lingayats.'),
],W+'Murti','Murti article read in full (175,695 characters): Covers 9 forms; terms (vigraha, bimba), moods (ugra, saumya), materials and single deities are not object types.')
# Buddha image
add('Buddha image',[
('Mathura Buddha','from 1st century CE','Early Indian image style, often in very thin robes.'),
('Sarnath Buddha','c. 475 CE','Gupta-period Buddha preaching his first sermon in the teaching mudra.'),
('Reclining Buddha','','Buddha lying down, usually at his death.'),
('Dharmachakra Buddha image','','Teaching gesture at the chest; linked with Vairochana.'),
('Bhumisparsa Buddha image','','Right hand touching the earth; linked with Akshobhya.'),
('Varada Buddha image','','Open right hand granting a boon; linked with Ratnasambhava.'),
('Dhyana Buddha image','','Hands resting in the lap in meditation; linked with Amitabha.'),
('Abhaya Buddha image','','Raised palm for fearlessness; linked with Amoghasiddhi.'),
],W+'Buddha_in_art','Buddha in art article read: Covers 10 forms; styles (Gupta, Amaravati) belong to visual art, and named monuments such as the Kamakura and Wat Traimit statues are single objects.')
# Devotional statue
add('Devotional statue',[
('Spanish vested image','1555 (Infant Jesus of Prague)','Mannequin-style religious figure dressed in ornate clothing.'),
('Philippine santo','1521 (Santo Nino de Cebu)','Vested saint image, historically owned by wealthy families; ivory and santol wood are used.'),
('Puerto Rican santo','','Wooden saint figure by santeros of the Cordillera Central.'),
('New Mexican bulto','','Small wooden saint figure of cottonwood, pine or aspen from northern New Mexico and southern Colorado.'),
('Mexican santo','','Saint figure of a living tradition with tinwork accessories and processional carriages.'),
],W+'Santo_(art)','Santo article read: Complete: 8 of 8 regional traditions it names (Santo, Val Gardena and Oberammergau from earlier passes are named in other articles).')
# Reliquary
add('Reliquary',[
('Feretory','medieval','Portable reliquary holding a saint\'s relics.'),
('Theca','','Brooch-like container for a very small relic.'),
('Box reliquary','','Simple box or box built on an architectural design.'),
('Cross reliquary','from 9th century','Cross-shaped container in gold or silver for True Cross relics.'),
('Head reliquary','from c. 1000','Reliquary shaped like a head.'),
('Arm reliquary','from c. 1000','Reliquary shaped like an arm.'),
('Philatory','late 15th century','Transparent reliquary with a viewing portal.'),
('Monstrance-form reliquary','later Middle Ages','Relic in a crystal or glass capsule on a column above a base.'),
('Holy Thorn reliquary','later Middle Ages','Metalwork jewellery housing tiny relics such as Holy Thorn.'),
('Wax-mastic reliquary','','Eastern Orthodox reliquary with slots holding wax-mastic discs with relics.'),
('Pendant or ring reliquary','','Simple small reliquary.'),
],W+'Reliquary','Reliquary article read: Covers 12 of the 21 rows; the others are single objects (Domnach Airgid, Bimaran and Kanishka caskets), stupas and halls.')
# Miniature stupa
add('Miniature stupa',[
('Lotus Blossom chorten','','Marks the Buddha\'s birth; circular base with four steps and lotus petals.'),
('Enlightenment chorten','','Marks the enlightenment at Bodh Gaya.'),
('Chorten of Many Doors','','Marks the first teachings near Sarnath; doors on each side of the steps.'),
('Chorten of Descent from the God Realm','','Marks the descent from Tushita; triple steps on each side.'),
('Chorten of Great Miracles','','Marks the miracles at age 50.'),
('Chorten of Reconciliation','','Marks resolution of a dispute in the sangha; four octagonal steps.'),
('Chorten of Complete Victory','','Marks the prolonging of life by three months; three circular unadorned steps.'),
('Nirvana chorten','','Bell-shaped, usually unornamented; marks the parinirvana.'),
('Kalachakra chorten','','Ninth kind, symbolising the Kalachakra Tantra.'),
],W+'Chorten','Chorten read to 100,000 of 166,181 characters: Complete: 9 of 9 Tibetan chorten types; relic, object, votive and symbolic stupas are classes of monument, not small devotional objects.')
# Damaru
add('Damaru',[('Skull damaru','','Tibetan damaru made of two joined skull bones with cured skins, played with a bell.')],W+'Damaru','Complete: 2 of 2 damaru types in the article.')
# Altar handbell
K['Altar handbell']['sel']+=' Altar bell article read: names only the altar bell; the altar gong is a gong, not a handbell. Complete: 2 of 2 handbell forms.'
# Ofuda
add('Ofuda',[
('Oharai Taima','','Earlier Ise talisman, originally a purification wand handed out by travelling preachers.'),
('Kenharai','','Oharai Taima as a wood sliver folded in paper shaped like a sword blade.'),
('Kakuharai','','Thin rectangular plaque in an envelope-like casing; the common Jingu Taima today.'),
('Daikakuharai','','Larger kakuharai.'),
('Shinsatsu','','Shrine-issued talisman bearing the shrine or deity name and seal, kept on household altars.'),
('Kitofuda','','Wooden talisman received after formal prayers at a shrine or temple.'),
('Goofu','','Protective talisman; the Kumano goofu was a paper talisman with stylised crows.'),
('Kamadogami ofuda','','Hearth-deity ofuda placed in the kitchen.'),
('Sanbo-Kojin ofuda','','Buddhist hearth-deity ofuda placed in the kitchen.'),
('Tsuno Daishi','','Protective talisman showing Ryogen as a horned figure, placed at doorways.'),
('Chintaku Reifu','','Series of seventy-two Daoist-origin home-protection talismans.'),
('Sakasafuda','','Handmade anti-theft talisman displayed upside down.'),
('Ujigami ofuda','','Ofuda of a household\'s local tutelary deity.'),
('Kajikimen','','Talisman from Suwa Shrine thought to let the bearer eat meat without impurity.'),
],W+'Ofuda','Ofuda article read: Covers 15 of 26 rows; omamori, ema, omikuji, shuin and senjafuda have their own kinds or are not cards, and the Nichiren disease talisman and Ususama talisman are temple-specific.')
# Gutka & pothi
add('Gutka & pothi',[
('Sanchipat','7th century','Assamese manuscript of agarwood-bark strips strung like a pothi.'),
('Lontar','','Palm-leaf manuscript of Indonesia, especially Bali.'),
('Pesa','12th century (Bagan)','Burmese palm-leaf manuscript for religious texts.'),
('Kammavaca','1683 (earliest)','Decorated Burmese lacquered palm-leaf manuscript, gilded.'),
('Sleuk rith','','Khmer palm-leaf manuscript used until the 20th century.'),
],W+'Pothi','Palm-leaf and bark manuscript forms of the Pothi article; Covers 7 forms.')
# Torah finials
add('Torah finials',[('Keter','at least 9th century','Torah crown, a single crown covering both handles; the first silver crown commissioned in 1203.')],'https://www.chabad.org/library/article_cdo/aid/5283839/jewish/Why-Do-Torah-Scrolls-Have-Silver-Crowns.htm','Torah ornaments searched on Wikipedia (Torah ark has none), Chabad and a Hebrew Union College page: the shield or breastplate (tas) and the mantle have no kind here and are left for the owner queue. Covers 2 forms.')
# Alms box
K['Alms box']['nl']='One entry is a named regional form of alms or offering box.'
K['Alms box']['sel']='No complete list exists; the one entry follows the Wikipedia article Saisen. Covers 1 form.'
# Butsudan sections
b=K['Butsudan']; seen=[]
for e in b['x']:
    if e.get('g') and e['g'] not in seen: seen.append(e['g'])
b['xg']=seen
json.dump(d,open(R+'work/GAP_F4/t.json','w'),ensure_ascii=False,indent=1); os.replace(R+'work/GAP_F4/t.json',R+'out/F4.json')
print({k['n']:len(k['x']) for k in K.values() if k['x']})
