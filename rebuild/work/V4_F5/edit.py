import json,os,re,collections
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'out/F5.json')); B=json.load(open(R+'out/F5_brands.json'))
W='https://en.wikipedia.org/wiki/'
def U(t): return W+t
# (name, aliases, desc, country, year, wikititle, role, dt)
P=[
("Raphael Tuck & Sons","Tuck","London publisher of pictures, greetings cards and postcards, prominent in the late-1890s postcard boom.","United Kingdom","1866","Raphael_Tuck_%26_Sons","landmark"),
("A. & G. Taylor","","London photographic business making cabinet cards and cartes de visite, later picture postcards.","United Kingdom","1866","A._%26_G._Taylor",""),
("Gale & Polden","","Printer and publisher founded in Brompton, later in Aldershot; closed in 1981.","United Kingdom","1868","Gale_%26_Polden",""),
("J Salmon Ltd","Salmon · Joseph Salmon","Sevenoaks printer and publisher, Britain's oldest established postcard and calendar publisher; founded by the bookseller Joseph Salmon (1844–1923).","United Kingdom","1880","J_Salmon_Ltd",""),
("Valentine & Sons","","Dundee printing company that became Scotland's leading picture postcard maker.","United Kingdom","1851","Valentine_%26_Sons","landmark"),
("Siegmund Hildesheimer","Hildesheimer","German-born publisher (1832–1896) in London and Manchester, known for greeting cards and postcards.","United Kingdom","","Siegmund_Hildesheimer",""),
("Frederick Hartmann","","London postcard publisher and leading proponent of the divided-back card.","United Kingdom","c. 1902–1909","Frederick_Hartmann",""),
("Edward Gordon Smith","","London photographer and publisher (1857–1906) of views and transport subjects; began postcards in late 1902.","United Kingdom","1902","Edward_Gordon_Smith",""),
("W. J. Nigh","","Ventnor, Isle of Wight, firm founded as a postcard publisher; later toys, giftware and stationery.","United Kingdom","1903","W._J._Nigh",""),
("Judges Postcards","Judges Ltd","St Leonards-on-Sea picture postcard maker begun by Fred Judge; called Judges Limited from 1910 to 1984.","United Kingdom","1903","Judges_Postcards",""),
("John White","J. White & Son","Littlehampton photographer and postcard publisher (1850–1932); the business was J. White & Son by 1903.","United Kingdom","by 1903","John_White_(photographer)",""),
("Bamforth & Co Ltd","Bamforth","Publishing, film and illustration company based in Holmfirth, West Yorkshire.","United Kingdom","","Bamforth_%26_Co_Ltd",""),
("C. W. Faulkner","C. W. Faulkner & Co.","Printer and publisher that began with Christmas cards; incorporated as C. W. Faulkner & Co. in 1905.","United Kingdom","1905","C._W._Faulkner",""),
("Alexander Brash","","British bookseller, stationer and postcard publisher (1874–1943).","United Kingdom","","Alexander_Brash",""),
("John Beagles","J. Beagles & Co.","English printer and publisher (1844–1907), known for real photo postcards.","United Kingdom","","John_Beagles",""),
("G. P. Abraham","George Perry Abraham","British photographer, postcard publisher and mountaineer (1846–1923).","United Kingdom","","G._P._Abraham",""),
("Charles Emeny","","English photographer and postcard publisher (1846–1924) based in Felixstowe, Suffolk.","United Kingdom","","Charles_Emeny",""),
("F. G. O. Stuart","","Scottish photographer born in Braemar (c. 1843–1923) who published postcards.","United Kingdom","","F._G._O._Stuart",""),
("A. H. Hawke","","Photographer and postcard publisher (1881–1958) of Helston, Cornwall.","United Kingdom","","A._H._Hawke",""),
("James Henderson","James Henderson & Sons Ltd","Newspaper and magazine proprietor (1823–1906) who also published postcards through James Henderson & Sons.","United Kingdom","","James_Henderson_(publisher)",""),
("Arthur Lewis","","Welsh photographer and postcard publisher (1885–1952), born in Aberystwyth.","United Kingdom","","Arthur_Lewis_(photographer)",""),
("William Harwood","","Photographer and postcard collector (1883–1976) of the Criccieth region of Wales.","United Kingdom","","William_Harwood_(photographer)",""),
("J. Arthur Dixon","","Greetings card and postcard maker founded by John Arthur Dixon (1897–1958), born in Cross Hills, Yorkshire.","United Kingdom","","J._Arthur_Dixon",""),
("John Hinde","","English photographer (1916–1997) whose nostalgic colour style shaped postcard photography.","United Kingdom","","John_Hinde_(photographer)",""),
("Anthony Byatt","Tony Byatt","English postcard publisher, photographer and writer (1928–2014).","United Kingdom","","Anthony_Byatt",""),
("W. S. Cowell Ltd.","Cowell","British printing company of Ipswich, founded in 1818.","United Kingdom","1818","W._S._Cowell_Ltd.",""),
("Aerofilms","","Britain's first commercial aerial photography company, founded in 1919 by Francis Wills and Claude Graham White.","United Kingdom","1919","Aerofilms",""),
("Athena (retailer)","Athena","British art retailer founded in 1964, selling art prints and cards.","United Kingdom","1964","Athena_(retailer)",""),
("King and McGaw","","British art publisher and online retailer of art prints.","United Kingdom","","King_and_McGaw",""),
("Evelyn Wrench","","British author and journalist (1882–1966), editor of The Spectator, listed among postcard publishers.","United Kingdom","","Evelyn_Wrench",""),
("Cardall","Cardall Ltd","Irish postcard publisher based at Cope Street, Temple Bar, Dublin.","Ireland","","Cardall",""),
("Detroit Publishing Company","Phostint","American photographic publisher best known for photochrom colour postcards.","United States","","Detroit_Publishing_Company",""),
("Curt Teich","Curt Teich & Co.","American publisher of German descent (1877–1974), known for colour postcards of American life and an offset printing pioneer.","United States","","Curt_Teich",""),
("E. A. Bishop Postcard Company","","Postcard publisher and wholesaler in Racine, Wisconsin, active mainly in the first three decades of the 20th century.","United States","early 20th century","E._A._Bishop_Postcard_Company",""),
("V. O. Hammon Publishing Company","","Chicago postcard maker for the Great Lakes region; from 1915 it bought only postcard rights to photographers' negatives.","United States","early 20th century","V._O._Hammon_Publishing_Company",""),
("Hugh C. Leighton Company","Leighton","Portland, Maine, publisher and printer of postcards, mainly of New England scenes.","United States","1906–1909","Hugh_C._Leighton_Company",""),
("Tichnor Brothers","","Boston graphic arts and printing company.","United States","1908–1987","Tichnor_Brothers",""),
("Edward H. Mitchell","","San Francisco businessman (1867–1932) and prolific postcard publisher.","United States","","Edward_H._Mitchell",""),
("Stanley Piltz","","San Francisco photographer and publisher (1887–1973) who issued linen-type postcards in the 1930s to 1950s.","United States","1930s–1950s","Stanley_Piltz",""),
("Sawyer's","","Portland, Oregon, maker of slide projectors, scenic slides, View-Master reels and postcards.","United States","","Sawyer%27s",""),
("Fred Harvey","","Entrepreneur (1835–1901) behind the Harvey House restaurants, shops and hotels on US railways; listed among postcard publishers.","United States","","Fred_Harvey_(entrepreneur)",""),
("Stengel & Co","Stengel & Markert","Dresden printer, founded as Stengel & Markert in 1885, that became the world's largest postcard maker in the 1900s.","Germany","1885","Stengel_%26_Co","landmark"),
("Arthur Vogel","","German merchant, photographer and publisher (1868–1962) of Ore Mountain picture postcards.","Germany","","Arthur_Vogel_(photographer)",""),
("Purger & Co.","","Munich printing house.","Germany","","Purger_%26_Co.",""),
("Léon & Lévy","Lévy et fils","Paris printer and photograph publisher known for stereoscopic views and postcards.","France","1864","L%C3%A9on_%26_L%C3%A9vy",""),
("Émile Hamonic","","Saint-Brieuc photographer and publisher (1861–1943), one of the first great editors of picture postcards.","France","1893","%C3%89mile_Hamonic","origin"),
("Adeline Boutain","","French photographer and postcard publisher (1862–1946).","France","","Adeline_Boutain",""),
("Alex. Vincents Kunstforlag","Vincents","Copenhagen publisher of prints and postcards, founded by Alexander Vincent and continued by his family after 1916.","Denmark","1890","Alex._Vincents_Kunstforlag","landmark"),
("Stenders Kunstforlag","Stenders","Leading Copenhagen publisher of postcards and artwork reproductions.","Denmark","","Stenders_Kunstforlag",""),
("Mary Willumsen","","Danish photographer (1884–1961) who sold postcards of women in revealing poses at a Copenhagen beach establishment from 1916.","Denmark","1916","Mary_Willumsen",""),
("Aspioti-ELKA","Elpis","Greek publishing and printing firm founded in Corfu in 1873 as a playing-card factory; merged with ELKA and folded in 1997.","Greece","1873","Aspioti-ELKA",""),
("Scherer, Nabholz & Co.","","Moscow photography company formed in the 1860s by Martin Scherer and Gottlieb Nabholz.","Russia","1860s","Scherer,_Nabholz_%26_Co.",""),
("Guillaume Berggren","Pehr Vilhelm Berggren","Swedish photographer (1835–1920) active in Istanbul.","Turkey","","Guillaume_Berggren",""),
("Eliyahu Brothers Postcards","","Postcards published by Matityahu and Yossef Eliyahu from the early 1920s to 1939, mostly views of Israel.","Mandatory Palestine","1920s–1939","Eliyahu_Brothers_Postcards",""),
("G. Kolff & Co.","Kolff","Bookselling, publishing and printing firm of Batavia (now Jakarta).","Dutch East Indies","","G._Kolff_%26_Co.",""),
("Bill Dane","","North American street photographer, born in 1938, who funded his work by selling photographic postcards.","Country not stated","","Bill_Dane",""),
("JOB Collection","","Calendars, posters and postcards advertising the JOB rolling paper factory in the Art Nouveau period.","Country not stated","","JOB_Collection",""),
("Association of Mouth and Foot Painting Artists of the World","AMFPA","For-profit international group that sells artwork, including cards, by artists who paint with mouth or foot.","International","","Association_of_Mouth_and_Foot_Painting_Artists_of_the_World",""),
]
order=["United Kingdom","Ireland","United States","Germany","France","Denmark","Greece","Russia","Turkey","Mandatory Palestine","Dutch East Indies","International","Country not stated"]
def ykey(y):
    m=re.search(r'\d{4}',y); 
    if m: return int(m.group())
    m=re.search(r'(\d{2})th century',y); return 1900 if m else 9999
P.sort(key=lambda p:(order.index(p[3]),ykey(p[4]),p[0]))
assert len(P)==58,len(P)
ents=[]
for n,a,desc,c,y,wt,role in P:
    e={"n":n,"a":a,"d":desc,"mk":"","y":y,"s":U(wt),"v":[],"dt":"series number · place · back type","g":c}
    if n=="Stengel & Co": e["v"]=[{"n":"Stengel & Markert","y":"1885","mk":"","d":"original name of the firm"}]
    if role: e["role"]=role
    ents.append(e)
# brands
have={b['n'] for b in B['b']}
def addb(name,kf,src,seg="Specialist"):
    name=name.strip()
    if not name or name in have: return
    have.add(name)
    B['b'].append({"n":name,"c":"","f":"","seg":seg,"kf":kf,"d":f"Maker or issuer of {kf}.","lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":src or "https://en.wikipedia.org/wiki/Category:Postcard_publishers","stub":True})
removed=collections.OrderedDict(); report=[]
KEEP={"Picture postcard"}
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      nx=len(k.get('x') or []); nm=len(k.get('m') or []); nr=len(k.get('r') or [])
      if k['n']=="Picture postcard":
          for x in k['x']:
              if x.get('mk'): addb(x['mk'],"postcards",x.get('s'),"Heritage manufactory")
              for v in x.get('v') or []:
                  if v.get('mk'): addb(v['mk'],"postcards",x.get('s'),"Heritage manufactory")
          k['x']=ents
          k['nl']="One entry is a firm or person that published picture postcards under its own name; the founder's name and later company names are aliases."
          k['sel']="Every page in Wikipedia's Category:Postcard publishers (59 pages), with Joseph Salmon merged into J Salmon Ltd; grouped by the country each page places the publisher in, then by the year the page gives for the business, then by name. No wider canon of postcard publishers was found."
          k['xg']="by country"
          report.append((k['n'],nx,len(ents),nm,nr)); continue
      if nx or nm or nr:
          kf=k['n'].lower()
          for x in k.get('x') or []:
              for mk in [x.get('mk')]+[v.get('mk') for v in x.get('v') or []]:
                  if mk: addb(mk,kf,x.get('s'))
          for t in k.get('m') or []:
              if len(t)==2 and t[1]:
                  addb(re.sub(r'^issued by ','',t[1]),kf,None)
          for t in k.get('r') or []:
              if len(t)==2 and t[1]: addb(re.sub(r'^issued by ','',t[1]),kf,None)
          report.append((k['n'],nx,0,nm,nr))
      for key in ('x','m','r','nl','sel','xg'):
          k.pop(key,None)
tmp=R+'out/F5.json.tmp'; json.dump(d,open(tmp,'w'),ensure_ascii=False,indent=1); os.replace(tmp,R+'out/F5.json')
tmp=R+'out/F5_brands.json.tmp'; json.dump(B,open(tmp,'w'),ensure_ascii=False,indent=1); os.replace(tmp,R+'out/F5_brands.json')
for r in report: print(r)
print(len(B['b']))
