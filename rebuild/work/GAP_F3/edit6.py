import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(P+'F3.json'))
k=[k for dp in d['depts'] for sh in dp['s'] for k in sh.get('k',[]) if k['n']=='Definitive stamp'][0]
W='https://en.wikipedia.org/wiki/'
rows=[]
C=('Canada','Canadian_definitive_postage_stamps')
for n,y in [("Edward VII Maple Leaf design","1903"),("George V Admiral issue final series","1935"),("George VI 1937 series","1937"),("George VI War Issue","1942"),("George VI plain design","1949"),("Elizabeth II photograph series","1953"),("Elizabeth II Wilding portrait series","1954"),("Elizabeth II series of 1962","1962"),("Elizabeth II series with high-value pictorials","1967"),("Prime ministers series","1972"),("Flora series, small size","1977"),("Flora series, medium size","1977"),("Street scenes series","1978"),("National parks series","1979")]:
    rows.append((n+" (Canada)" if 'Canada' not in n else n,y,"Canadian definitive series, listed in Wikipedia's article on Canadian definitive postage stamps.",C[1],C[0]))
S=('Soviet postal administration','Definitive_stamps_of_the_Soviet_Union')
for i,(lab,y) in enumerate([("2nd issue","1927"),("3rd issue","1929"),("4th issue","1936"),("5th issue (steel foundryman)","1939"),("6th issue (miner)","1939"),("7th issue","1948"),("8th issue","1948"),("9th issue","1958"),("10th issue","1961"),("11th issue","1966"),("12th issue","1976"),("13th issue","1980"),("14th issue","1988")]):
    rows.append((f"Soviet definitive {lab}",y,"Soviet definitive series, listed in Wikipedia's article on definitive stamps of the Soviet Union.",S[1],S[0]))
rows+= [("Series of 1902 (United States)","1902","Set of fourteen US definitives, each with its own ornate design, replaced by the Washington-Franklin issues in 1908.","Series_of_1902_(United_States_postage_stamps)","United States"),
("Distinguished Americans series","2000","US definitive series begun in 2000 with a 10-cent stamp honouring General Joseph Stilwell.","Distinguished_Americans_series","United States"),
("Castle series (1955)","1955","First of two UK definitive series of Elizabeth II, showing castles of the four nations.","Castle_series_stamps","United Kingdom"),
("Castle series (1988)","1988","Second of two UK definitive series of Elizabeth II, showing castles of the four nations.","Castle_series_stamps","United Kingdom")]
have={e['n'].lower() for e in k['x']}; c=0
for n,y,dsc,page,g in rows:
    if n.lower() in have: continue
    k['x'].append({"n":n,"a":"","d":dsc,"mk":"","y":y,"s":W+page,"v":[],"g":g}); c+=1
k['sel']=k['sel'].replace("definitive series of other administrations are not yet covered.","definitive series of other administrations are not covered.").rstrip()+" Round 2: no Wikipedia list of definitive series exists (searched); the Canadian, Soviet, US 1902 and Distinguished Americans, and UK Castle articles were read and their series added. Covers the series of those administrations; others (Germany, Australia, Japan, Brazil) have no definitive-series article found, so are not covered."
# fix circulating coverage lines
for dp in d['depts']:
  for sh in dp['s']:
    for kk in sh.get('k',[]):
      if kk['n'] in('Circulation coin','Circulation banknote'):
        kk['sel']=kk['sel'].replace("Covers 20 issuing areas of about 200 in their Wikipedia currency articles, with every world region represented; the other issuers are not added because each needs its own article read and none is a whole-space list.","").rstrip()
        kk['sel']+=" Coverage: Complete for currencies (every currency of the list is an entry); series per currency are given only for the 20 issuers whose currency articles were read, so the other currencies show the currency as one entry without its series."
json.dump(d,open(P+'F3.json.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'F3.json.tmp',P+'F3.json')
print(c)
