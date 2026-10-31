import json,os,copy
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'out/F4.json'))
K={}
for D in d['depts']:
    for S in D['s']:
        for k in S['k']: K[k['n']]=k
W='https://en.wikipedia.org/wiki/'
def setk(n,nl,sel):
    K[n]['nl']=nl; K[n]['sel']=sel
removed=[]
# ---- Tarot
t=K['Tarot deck']
for m in t['m']: removed.append(('Tarot deck',m[0]))
t['m']=[]
X={x['n']:x for x in t['x']}
for n,g in [('Visconti-Sforza tarot','Historical decks (before 1900)'),('Sola Busca tarot','Historical decks (before 1900)'),('Tarot de Marseille','Historical decks (before 1900)'),('Etteilla tarot','Historical decks (before 1900)'),('Rider-Waite-Smith tarot','Occult and modern decks (1900 onwards)'),('Thoth tarot','Occult and modern decks (1900 onwards)')]:
    X[n]['g']=g
X['Etteilla tarot']['role']='origin'; X['Rider-Waite-Smith tarot']['role']='landmark'
new=[
 {"n":"Swiss Tarot (1JJ)","a":"JJ Tarot · Troccas deck","d":"78-card deck derived from the Tarot de Besançon, first made 1831-1838 at Johann Georg Rauch's card factory; Juno and Jupiter replace two trumps.","mk":"J. G. Rauch","y":"1831-1838","s":W+"Swiss_Tarot","g":"Historical decks (before 1900)","dt":"printed pack · Juno and Jupiter trumps","v":[{"n":"Rauch original","mk":"J. G. Rauch","y":"1831-1838","d":"first version"},{"n":"Johannes Müller version","mk":"Johannes Müller","y":"until 1860","d":"unaltered production in Diessenhofen"},{"n":"A.G. Müller 1JJ reprint","mk":"A.G. Müller","y":"1965","d":"cleaner lines; source of the 1JJ name"},{"n":"Sursilvan-captioned pack","mk":"A.G. Müller","y":"2016","d":"printed for Troccas players for Radiotelevisiun Svizra Rumantscha"}]},
 {"n":"Oswald Wirth Tarot","a":"Wirth tarot","d":"Symbolic reworking of the 22 Major Arcana of the Tarot of Marseilles by Oswald Wirth, with Hebrew letters and Kabbalistic and alchemical symbols.","mk":"","y":"1889","s":W+"Oswald_Wirth_Tarot","g":"Historical decks (before 1900)","dt":"trumps only at first · hand-coloured limited editions","v":[{"n":"Original Major Arcana","mk":"","y":"1889","d":"limited, hand-coloured editions"},{"n":"Revised Major Arcana","mk":"","y":"1926","d":"second version of the trumps"}]},
 {"n":"B.O.T.A. tarot deck","a":"Builders of the Adytum tarot","d":"Deck designed by Paul Foster Case with artist Jessie Burns Parke, close to the Rider-Waite-Smith deck but with some cards drawn from the Marseilles pattern.","mk":"Builders of the Adytum","y":"","s":W+"B.O.T.A._tarot_deck","g":"Occult and modern decks (1900 onwards)","dt":"full 78 cards or trumps only","v":[{"n":"Standard deck","mk":"Builders of the Adytum","y":"","d":"illustrated trumps, suit-symbol minor cards"},{"n":"Major Arcana colouring edition","mk":"Builders of the Adytum","y":"","d":"black-and-white trumps to colour in"},{"n":"Coloured Major Arcana edition","mk":"Builders of the Adytum","y":"","d":"issued after Case's death"}]},
 {"n":"Motherpeace Tarot","a":"","d":"Round-card deck by Karen Vogel and Vicki Noble, late 1970s, with mainly female figures and renamed court cards (Daughter, Son, Priestess, Shaman).","mk":"","y":"late 1970s","s":W+"Motherpeace_Tarot","g":"Occult and modern decks (1900 onwards)","dt":"round cards","v":[]},
 {"n":"Salvador Dalí's Tarot","a":"Dalí Universal Tarot","d":"78 surrealist paintings by Salvador Dalí begun in 1973, published as a deck in 1984 by the Spanish printer Naipes Comas.","mk":"Naipes Comas","y":"1984","s":W+"Salvador_Dali's_Tarot","g":"Occult and modern decks (1900 onwards)","dt":"78 paintings with collage","v":[]},
]
t['x']+=new
order={'Visconti-Sforza tarot':0,'Sola Busca tarot':1,'Tarot de Marseille':2,'Etteilla tarot':3,'Swiss Tarot (1JJ)':4,'Oswald Wirth Tarot':5,'Rider-Waite-Smith tarot':6,'Thoth tarot':7,'Motherpeace Tarot':8,'Salvador Dalí\'s Tarot':9,'B.O.T.A. tarot deck':10}
t['x'].sort(key=lambda x:order[x['n']])
t['xg']=['Historical decks (before 1900)','Occult and modern decks (1900 onwards)']
setk('Tarot deck',"One entry is a named tarot pattern or published deck for divination, with its printings as versions.",
 "Follows the Wikipedia categories Divination Tarot decks (6 pages) and Tarot decks (2 pages), plus the historical Visconti-Sforza and Sola Busca decks and Etteilla from the earlier pass. Playing-card tarot patterns for games (Minchiate, Tarocco, Tarot Nouveau and others) belong to the playing-cards shelf. Complete: 8 of 8 divination pages in those categories; of 21 pages across the divination and tarot-playing-card categories, 10 are kept and 11 game patterns are left out. Modern commercial decks are not a canon and are not listed.")
t['see']=t.get('see',[])
# ---- Oracle
o=K['Oracle deck']
for m in o['m']: removed.append(('Oracle deck',m[0]))
o['m']=[]; o['r']=[]
# ---- Spirit board
setk('Spirit board',"One entry is a talking-board product line.","No whole-space reference exists; only the Ouija board, as described on the Wikipedia Ouija article (patent 10 February 1891). The article does not call it the first. Covers 1 form.")
# ---- Hanukkah lamp
h=K['Hanukkah lamp']
for m in h['m']: removed.append(('Hanukkah lamp',m[0]))
h['m']=[]
h['x']=[
 {"n":"Rounded-branch hanukkiah","a":"curved-branch lamp","d":"The more common style, with rounded branches that the article links to Second Temple-period depictions.","mk":"","y":"","s":W+"Hanukkah_menorah","dt":"","v":[]},
 {"n":"Chabad-style straight-branch hanukkiah","a":"","d":"Upward-angled straight branches, following the Rebbe's 1982 reading of a 12th-century drawing by Maimonides.","mk":"","y":"1982","s":W+"Hanukkah_menorah","v":[]},
 {"n":"Lindo lamp","a":"","d":"Hanukkah lamp in the Jewish Museum London, named in the article as a regional example.","mk":"","y":"","s":W+"Hanukkah_menorah","v":[]},
 {"n":"Lemberg lamp","a":"","d":"Hanukkah lamp from Lemberg in the Jewish Museum, New York, named in the article.","mk":"","y":"","s":W+"Hanukkah_menorah","v":[]},
 {"n":"Moroccan hanukkiah","a":"","d":"Lamp with a Tree of Life (Etz Chaim) motif.","mk":"","y":"","s":W+"Hanukkah_menorah","v":[]},
]
setk('Hanukkah lamp',"One entry is a named style or regional type of Hanukkah lamp.","Follows the Wikipedia Hanukkah menorah article. Covers 5 of the 15 named lamps and styles there; the rest are public monuments, gifts, a digital menorah and novelty items, which are not owned objects of a type. Retail lines are not listed.")
# ---- Other m removals
for kn,why in [('Seven-branch menorah','Sderot Menorah (7 Branch)'),('Torah finials','Bier Judaica 925 Sterling Silver Hammered Torah Finials'),('Monstrance',None),('Spice box',None),('Buddha image','Great Buddha of Kamakura')]:
    for m in K[kn]['m']:
        if m[0]!='Great Buddha of Kamakura' or kn=='Buddha image': removed.append((kn,m[0]))
    K[kn]['m']=[]
# ---- Reliquary: chasse becomes entry
K['Reliquary']['m']=[]; removed.append(('Reliquary','Limoges enamel chasse (now an entry)'))
K['Reliquary']['x']=[{"n":"Limoges enamel chasse","a":"châsse","d":"House-shaped reliquary box of copper plates with champlevé enamel over a wooden core, made at Limoges from the 12th century into the 14th.","mk":"","y":"12th-14th century","s":W+"Chasse_(casket)","dt":"copper · champlevé enamel · wooden core","v":[]}]
setk('Reliquary',"One entry is a named type of reliquary container.","Follows the Wikipedia article Chasse (casket), which names 8 types (chasse, box reliquary, house-shaped shrine, cumdach, Monymusk Reliquary, Shrine of Saint Eleutherius, Shrine of the Three Kings, Becket Casket). Only the chasse form is kept; the named shrines are single museum or church objects. Covers 1 of 8.")
# ---- Murti
mu=K['Murti']; mu['m']=[]; removed.append(('Murti','Ganesh Chaturthi clay idol (now an entry)'))
mu['x'].append({"n":"Ganesha clay murti","a":"Ganesh Chaturthi idol","d":"Clay image of Ganesha made for the festival, from 20 mm for homes to over 20 m for public celebrations, and immersed in water at the end.","mk":"","y":"","s":W+"Ganesh_Chaturthi","dt":"clay · papier-mâché · plaster of Paris banned in some states","v":[]})
setk('Murti',"One entry is a named form of Hindu deity image, by deity or by festival use.","No whole-space reference exists. Follows the Wikipedia articles Murti, Nataraja and Ganesh Chaturthi. Covers 4 forms.")
setk('Buddha image',"One entry is a named type of Buddha or Buddhist figure image.","No whole-space reference exists. Follows the Wikipedia articles Buddha in art and Budai. Covers 2 forms. The Great Buddha of Kamakura is a monument and is left out.")
K['Buddha image']['m']=[]
# ---- Bible m -> Mushaf, Gutka
b=K['Bible']
for m in b['m']: removed.append(('Bible',m[0]))
b['m']=[]
K['Mushaf']['x']=[
 {"n":"Medina Quran","a":"Medina Mushaf","d":"Printed mushaf edition listed as the Medina Quran in the Wikipedia article on the Mushaf.","mk":"","y":"","s":W+"Mushaf","dt":"","v":[]},
 {"n":"Mushaf al-Tajwid","a":"tajwid mushaf","d":"Mushaf printed with colour-coded letters to help reading the Qur'an with tajwid.","mk":"","y":"","s":W+"Mushaf","dt":"colour-coded print","v":[]}]
setk('Mushaf',"One entry is a mushaf made as a distinct object, such as one printed with colour coding.","Follows the Wikipedia article Mushaf, which names 31 mushafs. Covers 2 of 31: the other 29 are early manuscripts and codices held in museums and library collections, or state and scholarly text editions, which belong to Literature.")
K['Gutka & pothi']['x']=[
 {"n":"Panj Granthi","a":"Pañj Granth","d":"Small booklet of five or more hymns from the Guru Granth Sahib, made for private recitation; printed editions date from the 1870s.","mk":"","y":"1874-1895 (printed)","s":W+"Panj_Granthi","dt":"booklet","v":[]},
 {"n":"Das Granthi","a":"Dasa Grathi","d":"Small booklet of selected compositions from the Dasam Granth for beginners; no standard contents, the SGPC version has eight texts.","mk":"","y":"","s":W+"Panj_Granthi","dt":"booklet","v":[]}]
setk('Gutka & pothi',"One entry is a named type of Sikh prayer booklet.","Follows the Wikipedia article Panj Granthi, which describes Panj Granthi and Das Granthi. Covers 2 forms. Sundar Gutka is not described on a page fetched in this pass and is left out.")
# ---- Nativity
n=K['Nativity set']
n['x']+= [
 {"n":"Czech betlém","a":"paper crèche","d":"Paper-cut and wood-carved Czech crib, including the crèche of the poor.","mk":"","y":"","s":W+"Nativity_scene","dt":"paper or wood","v":[]},
 {"n":"Moravian Christmas putz","a":"","d":"Nativity scene at the centre of a Moravian Church Christmas display in the United States.","mk":"","y":"","s":W+"Nativity_scene","dt":"","v":[]},
 {"n":"Caganer","a":"","d":"Figure of a person defecating, added to Catalan nativity scenes.","mk":"","y":"","s":W+"Nativity_scene","dt":"","v":[]}]
setk('Nativity set',"One entry is a regional tradition of nativity crib or figures.","Follows the Wikipedia article Nativity scene. Covers 7 of the 12 named traditions there (Neapolitan presepio, santons, szopki, belén, Czech betlémy, Moravian putz, caganer) plus the Alpine carved crib from the earlier pass; the living nativities, Krýza's crèche, gingerbread crèches, the Australian scene and Bethlehem Live are events or single exhibits.")
# ---- Rosary & beads
ro=K['Rosary']
ro['x'].append({"n":"Pater Noster cord","a":"paternoster","d":"Western Christian cord of traditionally 150 beads, used for counting prayers; forerunner of the rosary.","mk":"","y":"","s":W+"Prayer_beads","dt":"","v":[]})
setk('Rosary',"One entry is a named form of Catholic or Western Christian prayer-bead set.","Follows the Wikipedia articles Dominican rosary and Prayer beads. Covers 2 of the 4 Christian bead forms named in Prayer beads (Dominican rosary, Pater Noster cord) plus three chaplets from the Dominican rosary article.")
K['Prayer rope']['x'].append({"n":"Mequteria","a":"","d":"Oriental Orthodox (Coptic and Ethiopian) prayer beads, often 41, used to repeat Kyrie Eleison.","mk":"","y":"","s":W+"Prayer_beads","dt":"","v":[]})
setk('Prayer rope',"One entry is a named Orthodox prayer rope or bead cord.","Follows the Wikipedia articles Prayer beads and Lestovka. Covers 3 forms (komboskini, lestovka, mequteria).")
K['Anglican prayer beads']['x']=[{"n":"Wreath of Christ","a":"Lutheran prayer beads","d":"Lutheran set of 18 beads used for meditation and repetitive prayer.","mk":"","y":"","s":W+"Prayer_beads","dt":"","v":[]}]
setk('Anglican prayer beads',"One entry is a named Protestant prayer-bead set.","Follows the Wikipedia article Prayer beads. Covers 1 form beside the kind itself (Wreath of Christ). Prayer beads names 12 types in all: the Catholic and Orthodox ones are under Rosary and Prayer rope, the Muslim, Hindu, Buddhist and Sikh ones are under Tasbih and Mala and Juzu.")
K['Mala']['x']=[{"n":"Niànzhū","a":"Chinese Buddhist prayer beads","d":"Chinese Buddhist prayer beads.","mk":"","y":"","s":W+"Prayer_beads","dt":"","v":[]},{"n":"Sikh mala","a":"","d":"Sikh prayer beads, made of iron and worn on the wrist, used with scripture recitation.","mk":"","y":"","s":W+"Prayer_beads","dt":"","v":[]}]
setk('Mala',"One entry is a named regional or sectarian form of mala.","Follows the Wikipedia article Prayer beads. Covers 2 forms beside the kind itself. Complete for the 12 named types in that article across Rosary, Prayer rope, Anglican prayer beads, Tasbih, Mala and Juzu.")
# ---- Butsudan
bu=K['Butsudan']
removed.append(('Butsudan','maker ranges H PREMIUM, HASEGAWA Standard, LIVE-ing, MIND STYLE (commodity maker lines)'))
bu['r']=[]
ex={x['n']:x for x in bu['x']}
crafts=[('Hikone butsudan','Shiga',1975),('Kawanabe butsudan','Kagoshima',1975),('Iiyama butsudan','Nagano',1975),('Kyo butsudan','Kyoto',1976),('Kanazawa butsudan','Ishikawa',1976),('Nagoya butsudan','Aichi',1976),('Mikawa butsudan','Aichi',1976),('Yame Fukushima butsudan','Fukuoka',1977),('Hiroshima butsudan','Hiroshima',1978),('Nanao butsudan','Ishikawa',1978),('Yamagata butsudan','Yamagata',1980),('Niigata Shirone butsudan','Niigata',1980),('Nagaoka butsudan','Niigata',1980),('Sanjo butsudan','Niigata',1980),('Osaka butsudan','Osaka',1982)]
nx=[]
for nm,pref,yr in crafts:
    if nm in ex: x=ex[nm]; x['g']=pref+' prefecture'; x['y']=str(yr)
    else:
        x={"n":nm,"a":"","d":f"Butsudan made in {pref} Prefecture, designated a Japanese traditional craft in {yr}.","mk":"","y":str(yr),"s":W+"List_of_Traditional_Crafts_of_Japan","g":pref+" prefecture","dt":"","v":[]}
    nx.append(x)
bu['x']=nx
setk('Butsudan',"One entry is a regional butsudan craft designated as a Japanese traditional craft.","Follows the Wikipedia List of Traditional Crafts of Japan (244 designated crafts). Complete: 15 of 15 butsudan crafts in that list; two further rows (Kyo and Owari Buddhist ritual implements) are implements, not altars. Years are the designation years.")
# ---- Art-tradition kinds: drop painting traditions
for kn,keep in [('Icon',[]),('Thangka & scroll painting',[]),('Yantra',[]),('Calligraphy wall panel',['Hilya'])]:
    k=K[kn]
    for x in k['x']:
        if x['n'] not in keep: removed.append((kn,x['n']+' (art/content tradition)'))
    k['x']=[x for x in k['x'] if x['n'] in keep]
setk('Calligraphy wall panel',"One entry is a named type of calligraphic wall panel as an object.","Follows the Wikipedia article Islamic calligraphy. Covers 1 form (hilya). Scripts such as thuluth belong to the visual-art taxonomy.") 
for kn,msg in [('Icon','Icon-painting schools and iconographic types belong to the visual-art taxonomy; the object kind keeps no entries.'),('Thangka & scroll painting','Thangka painting styles belong to the visual-art taxonomy; the object kind keeps no entries.'),('Yantra','Yantra designs are diagrams (content); the object kind keeps no entries.')]:
    K[kn]['note']=msg
# ---- Scrying mirror, Qur'an box, Rehal single objects
for kn in ('Scrying mirror',"Qur'an box & cover",'Rehal'):
    for x in K[kn]['x']: removed.append((kn,x['n']+' (single museum object, no design-collection confirmation fetched)'))
    K[kn]['x']=[]
# ---- Remaining kinds with x: nl and sel
rest={
 'Devotional statue':("One entry is a regional tradition of carved saint figures.","No whole-space reference exists. Follows the Wikipedia articles Santo (art), Val Gardena and Oberammergau. Covers 3 forms; no reference counts the carving traditions."),
 'Crucifix & devotional cross':("One entry is a named form of cross made as a devotional object.","No whole-space reference of cross objects exists. The Wikipedia article Christian cross variants names 94 variants, mostly symbols and heraldic shapes; only the five made as crucifixes and devotional crosses are kept. Covers 5 of 94."),
 'Home altarpiece & triptych':("One entry is a named form of folding altarpiece.","Follows the Wikipedia article Triptych. Covers 1 form."),
 'Miniature stupa':("One entry is a named form of small stupa kept as a devotional object.","Follows the Wikipedia article Chorten. Covers 1 form."),
 'Altar handbell':("One entry is a named form of hand bell used at an altar.","Follows the Wikipedia articles Altar bell and Ghanta. Covers 2 forms."),
 'Damaru':("One entry is a named type of damaru.","Follows the Wikipedia article Damaru. Covers 1 form."),
 'Devotional medal':("One entry is a named devotional medal.","No whole-space reference exists. Follows the Wikipedia articles Miraculous Medal and Saint Benedict Medal. Covers 2 medals."),
 'Scapular':("One entry is a named devotional scapular.","Follows the Wikipedia articles Scapular of Our Lady of Mount Carmel and Devotional scapular. Covers 2 scapulars."),
 'Evil-eye charm':("One entry is a named type of evil-eye charm.","Follows the Wikipedia articles Nazar (amulet) and Hamsa. Covers 2 forms."),
 'Ofuda':("One entry is a named type of Shinto talisman card.","Follows the Wikipedia article Ofuda. Covers 1 form."),
 'Bible':("One entry is a named form of Bible kept as an object.","Follows the Wikipedia article Family Bible. Covers 1 form. Editions and translations belong to the literature taxonomy."),
 'Sutra book':("One entry is a named binding form of sutra book.","Follows the Wikipedia article Orihon. Covers 1 form."),
 'Ketubah':("One entry is a named regional style of ketubah as an object.","Follows the Wikipedia article Ketubah. Covers 2 styles."),
 'Torah finials':("One entry is a named form of Torah finial.","Follows the Wikipedia article Torah finials. Covers 1 form (rimonim)."),
 'Torah pointer':("One entry is a named form of Torah pointer.","Follows the Wikipedia article Yad. Covers 1 form."),
 'Phurba':("One entry is a named form of phurba.","Follows the Wikipedia article Vajrakilaya. Covers 1 form."),
 'Oil lamp for worship':("One entry is a named form of worship oil lamp.","Follows the Wikipedia articles Diya (lamp) and Nachiarkoil lamp. Covers 2 forms."),
 'Seven-branch menorah':("One entry is a named form of seven-branch menorah.","Follows the Wikipedia article Temple menorah. Covers 1 form."),
 'Advent wreath':("One entry is a named form of Advent wreath.","Follows the Wikipedia article Advent wreath. Covers 1 form."),
 'Ritual incense':("One entry is a named regional form of ritual incense.","Follows the Wikipedia articles Nippon Kodo and Incense in India. Covers 2 forms."),
 'Incense burner':("One entry is a named form of ritual incense burner.","Follows the Wikipedia article Incense. Covers 1 form."),
 'Thurible & hand censer':("One entry is a named form of thurible.","Follows the Wikipedia article Thurible. Covers 1 form."),
 'Joss paper':("One entry is a named type of joss paper.","Follows the Wikipedia article Joss paper. Covers 1 type."),
 'Lenormand deck':("One entry is a named Lenormand pattern.","Follows the Wikipedia article on Johann Kaspar Hechtel, source of the Petit Lenormand. Covers 1 pattern."),
 'Book of Shadows':("One entry is a named Book of Shadows.","Follows the Wikipedia article Book of Shadows. Covers 1 text."),
 'I Ching set':("One entry is a named I Ching set.","No canon exists; the kind is a commodity and keeps no entries."),
}
for kn,(nl,sel) in rest.items(): setk(kn,nl,sel)
K['Gardnerian'] if False else None
for x in K['Book of Shadows']['x']:
    if x['n']=='Gardnerian Book of Shadows': x['role']='origin'
for x in K['Advent wreath']['x']:
    if x['n']=='Wichern Advent wreath': x['role']='origin'
for x in K['Torah finials']['x']: pass
K['I Ching set']['m']=[]; removed.append(('I Ching set','I Ching Complete Divination Kit'))
del K['I Ching set']['nl'], K['I Ching set']['sel']
# Monstrance / spice box removed names
for kn in ('Monstrance','Spice box'): removed.append((kn,'single heritage objects (Belem monstrance, Diamond Monstrance; Frankfurt spice box)'))
# fix: ensure not duplicate tarot see
d_out=R+'work/V4_F4/F4.new.json'
json.dump(d,open(d_out,'w'),ensure_ascii=False,indent=1)
os.replace(d_out,R+'out/F4.json')
json.dump(removed,open(R+'work/V4_F4/removed.json','w'),ensure_ascii=False,indent=1)
print(len(removed))
