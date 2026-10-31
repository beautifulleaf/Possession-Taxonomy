import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/J8.json'
d=json.load(open(P))
G='Named forms and protected traditions'
IND='https://en.wikipedia.org/wiki/List_of_Indian_sweets_and_desserts'
WAG='https://en.wikipedia.org/wiki/Wagashi'
HAL='https://en.wikipedia.org/wiki/Halva'
MAR='https://en.wikipedia.org/wiki/Marzipan'
NOU='https://en.wikipedia.org/wiki/Nougat'
BAK='https://en.wikipedia.org/wiki/Baklava'
def ind(lst,region):
    return [(n,f"{c} sweet of {region} India, listed on Wikipedia's List of Indian sweets and desserts.",'',IND) for n,c in lst]
A={}
A['Mithai']=(
 ind([('Boondi','Gram-flour drops in syrup'),('Ghevar','Fried, syrup-soaked'),('Imarti','Fried, syrup-based'),('Kalakand','Milk-based fudge'),('Khirmohan','Syrup-based chhena'),('Makhan bada','Fried, syrup-based'),('Malpua','Fried pancake in syrup'),('Petha','Candied pumpkin'),('Singori','Milk-based, leaf-wrapped'),('Peda','Khoya')],'north and pan-Indian') +
 ind([('Cham cham','Milk-based chhena'),('Chhena gaja','Chhena'),('Chhena jalebi','Chhena'),('Chhena poda','Baked chhena cake'),('Ledikeni','Chhena'),('Pantua','Chhena'),('Rasabali','Chhena'),('Ras malai','Chhena'),('Sarbhaja','Fried, milk-based'),('Sitabhog','Fried, syrup-based'),('Mihidana','Fried, syrup-based'),('Chuda ghasa','Flattened-rice'),('Sirir naru','Jaggery and gram-flour')],'eastern') +
 ind([('Adhirasam','Fried rice'),('Bandar laddu','Gram-flour ball'),('Boorelu','Stuffed lentil'),('Kovilpatti kadalai mittai','Nut brittle'),('Dharwad pedha','Milk-based fudge'),('Gavvalu','Fried rice'),('Kakinada kaja','Fried, syrup-based'),('Srivilliputtur palkova','Milk-based fudge'),('Pootharekulu','Rice-paper'),('Kajjikayalu','Fried, jaggery-based')],'southern') +
 ind([('Anarsa','Fried rice'),('Mohanthal','Gram-flour fudge'),('Modak','Fried rice dumpling'),('Shankarpali','Fried flour'),('Sutar feni','Fried flour'),('Bebinca','Layered baked cake')],'western'))
JP="Japanese confection listed on Wikipedia's Wagashi article"
def w(n,t,y=''): return (n,f"{t}; {JP}.",y,WAG)
A['Wagashi']=[w('Anmitsu','Agar cubes with red bean paste and fruit'),w('Amanattō','Sugar-simmered dried beans'),w('Botamochi','Rice ball wrapped around sweet bean paste'),w('Domyoji','Bean paste wrapped in sticky rice'),w('Gokabou','Sweetened rice cake'),w('Hanabiramochi','Flat red-and-white mochi with bean paste and candied burdock'),w('Ikinari dango','Steamed bun with sweet potato and bean paste from Kumamoto'),w('Imagawayaki','Bean paste in a fried dough covering'),w('Kompeito','Crystal sugar candy introduced via Portugal'),w('Kusa mochi','Mugwort mochi around bean paste'),w('Kuzumochi','Starch cake'),w('Kuri kinton','Sweetened mashed chestnuts'),w('Mochi','Rice cake from glutinous rice'),w('Sakuramochi','Bean-paste rice cake wrapped in pickled cherry leaf'),w('Taiyaki','Fish-shaped bean-paste filled fried-dough cake'),w('Uirō','Steamed rice flour and sugar cake'),w('Warabimochi','Jelly-like cake served with kinako and kuromitsu'),w('Yubeshi','Citrus-based confection'),w('Karukan','Steamed sweet cake'),w('Kurobo','Brown sugar confection'),w('Mizu shingen mochi','Kanten and water cake from Yamanashi','2014'),w('Tsubakimochi','Rice cake wrapped in camellia leaves','Heian era'),w('Akumaki','Confection from Kagoshima Prefecture')]
H=lambda n,c,b,u=HAL:(n,f"Halva or halwa from {c}, made from {b}; listed on Wikipedia's Halva article.",'',u)
A['Halva']=[H('Un helvası','Turkey','wheat flour'),H('İrmik helvası','Turkey','semolina'),H('Suji ka halwa','India and Pakistan','semolina'),H('Shujir halua','Bangladesh','wheat semolina'),H('Pathein halawa','Pathein, Myanmar','rice flour and milk'),H('Halva ardeh','Iran','sesame paste'),H('Halva Farsalon','Farsala, Greece','cornflour'),H('Halawet al-mahya','Hama, Syria','semolina and qatir'),H("Ma'mounia",'Aleppo, Syria','semolina and butter'),H('Halawat smeed','Syria','semolina'),H('Xalwo','Somalia','sugar, oil and cornstarch'),H('Armenian halva','Armenia','semolina, sesame, honey and butter'),H('Albanian halva','Albania','flour, sugar and olive oil'),H('Kenyan halva','Kenya','flour, sugar, honey and butter'),H('Gajar ka halwa','India, Pakistan and Bangladesh','carrots'),H('Chana halva','India','chickpea'),H('Bhatkal banana halwa','Bhatkal, India','banana and nuts'),H('Udupi halwa','Udupi, India','banana, wheat, ash gourd or jackfruit'),H('Tirunelveli halwa','Tirunelveli, India','wheat'),H('Sanwin makin','Myanmar','semolina'),H('Persian halva','Iran','wheat flour, butter, saffron and rosewater')]
M=lambda n,c,t,y='':(n,f"{t} ({c}); listed on Wikipedia's Marzipan article.",y,MAR)
A['Marzipan']=[M('Persipan','general','Apricot or peach kernels replace the almonds'),M('Mozartkugel','Austria','Marzipan balls dipped in dark chocolate'),M('Marzipanbrot','Germany','Marzipan shaped as a loaf, given at Christmas'),M('Figolli','Malta','Easter treat with marzipan filling'),M('Maçapão','Algarve, Portugal','Fruit-shaped marzipan sweets'),M('Badem ezmesi','Turkey','Turkish almond marzipan, two regional forms registered'),M('Massepain','Saint-Léonard-de-Noblat, France','Biscuit-shaped local marzipan'),M('Mazapán de Amatitlán','Guatemala','Made with pumpkin seed, rice and sugar'),M('Mazapán de la Rosa','Mexico','Peanut-based commercial candy'),M('Goan marzipan','Goa, India','Cashew marzipan used for Easter eggs'),M('Mazapán de pili','Philippines','Marzipan from pili nuts'),M('Escalade marzipan vegetables','Geneva, Switzerland','Marzipan vegetables in a chocolate cauldron'),M('Træstammer','Denmark','Marzipan-based cake')]
N=lambda n,c,t,y='':(n,f"{t} ({c}); listed on Wikipedia's Nougat article.",y,NOU)
A['Nougat & turrón']=[N('Mandorlato','Veneto, Italy','Firm Venetian nougat'),N('Qubbajt','Malta','Maltese nougat'),N('Cubbàita','Sicily','Sicilian nougat'),N('Nāṭif','Baghdad and Harran','Early whipped-egg-white nougat','10th century'),N('Viennese nougat','Central and northern Europe','Soft crunchy brown nougat with ground almonds'),N('Gianduiotto','Turin, Italy','Chocolate and hazelnut confection by Caffarel','1852'),N('Minneapolis nougat','Minneapolis, USA','Airy nougat of the Pendergast Candy Company','early 1920s')]
B=lambda n,c,t,y='':(n,f"{t} ({c}); listed on Wikipedia's Baklava article.",y,BAK)
A['Baklava & syrup pastries']=[B('Pakhlava','Armenia','Layered with cinnamon-spiced walnuts, diamond-shaped'),B('Greek baklava','Greece','Walnut and cinnamon, traditionally 33 layers'),B('Plakous','Lesbos, Greece','Thin layered nut pastry in syrup'),B('Yazdi baklava','Yazd, Iran','Regional version, often topped with pistachio'),B('Sütlü Nuriye','Turkey','Hazelnut baklava with milk replacing syrup'),B('Kadayif','Turkey and the Levant','Shredded-dough pastry soaked in syrup'),B('Albanian baklava','Albania and Kosovo','Baklava for religious holidays'),B('Syrian baklava','Syria','24 layers of buttered filo with pistachio or walnut'),B('Warbat','Syria','Filo with semolina custard filling'),B('Balluriyeh','Levant','Layered baklava-family sweet'),B('Kanafeh','Levant and Romania','Kadayif-based syrup pastry'),B('Algerian baklawa','Constantine, Algeria','Made with malsouka or warqa and almonds'),B('Tenbel pakhlava','Azerbaijan','8 to 10 layers with a yolk-coated top'),B('Ganja pakhlava','Ganja, Azerbaijan','Almond, sugar and cardamom filling, 18 layers'),B('Guba pakhlava','Guba, Azerbaijan','Saffron-coated top, 50 rishta layers'),B('Sheki pakhlava','Sheki, Azerbaijan','Rice-flour dough with hazelnut and cardamom'),B('Baku pakhlava','Baku, Azerbaijan','Archaic form with noodle-paste layers'),B('Güllaç','Turkey','Filo in warm milk, eaten in Ramadan','1330')]
added={}
for dp in d['dp'] if 'dp' in d else d['depts']:
  for s in dp['s']:
    for k in s['k']:
      if k['n'] in A:
        have={e['n'].lower() for e in k['x']}|{a.strip().lower() for e in k['x'] for a in (e.get('a') or '').split('·')}
        c=0
        for n,dd,y,src in A[k['n']]:
          if n.lower() in have: continue
          have.add(n.lower())
          k['x'].append({"n":n,"a":"","d":dd,"mk":"","y":y,"s":src,"v":[],"g":G}); c+=1
        added[k['n']]=c
print(added)
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P)
