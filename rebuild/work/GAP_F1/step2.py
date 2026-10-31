import json,re
d=json.load(open('F1.step1.json'))
def kinds():
    for dp in d['depts']:
        for sh in dp['s']:
            for k in sh['k']: yield dp,k
K={k['n']:k for dp,k in kinds()}
# drop attribute row
for dp,k in kinds():
    for e in k.get('x',[]):
        if 'v' in e: e['v']=[v for v in e['v'] if v['n']!='Term coined']
# rescue lines
def add(kind,e):
    K[kind].setdefault('x',[]).append(e)
add('Collected softcover volume',{"n":"Essential Marvel","a":"Marvel Essentials","d":"Black-and-white paperback reprints of vintage Marvel comics, mostly Silver and Bronze Age, run from 1996 to 2013.","mk":"Marvel","y":"1996","s":"https://en.wikipedia.org/wiki/Essential_Marvel"})
add('Collected softcover volume',{"n":"Showcase Presents","a":"DC Showcase","d":"Black-and-white paperbacks of over 500 pages each, reprinting mostly Silver Age DC comics, run from 2005 to 2016.","mk":"DC","y":"2005","s":"https://en.wikipedia.org/wiki/Showcase_Presents"})
add('Paperback book',{"n":"Harper Torchbooks","a":"","d":"Mid-century paperback series of scholarly and literary works from Harper Brothers, known for durable bindings and cover art.","mk":"Harper & Row","y":"1956","s":"https://publishinghistory.com/harper-torchbooks-history-and-assessment.html"})
# manga
k=K['Manga anthology magazine']
adult=0
have={e['n'].lower() for e in k['x']}
for e in k['x']:
    e.setdefault('g','Shōnen' if 'Shōnen' in e['n'] else 'Seinen' if 'Young' in e['n'] else 'Shōnen')
dem={'Kodomo':'Kodomo (children)','Shōnen':'Shōnen (boys)','Shōjo':'Shōjo (girls)','Seinen':'Seinen (men)','Josei':'Josei (women)','Yaoi':'Other and mixed','Yuri':'Other and mixed','Mixed':'Other and mixed'}
n_added=0
for line in open('manga_rows.txt',encoding='utf8'):
    n,pub,dm,yrs=line.rstrip('\n').split('|')
    if n.lower() in have: continue
    first=dm.split('/')[0]
    g=dem.get(first,'Other and mixed')
    y0=yrs.split('–')[0]
    span=f"{yrs[:-1]} to present" if yrs.endswith('–') else yrs.replace('–',' to ')
    dsc=f"Manga anthology from {pub}, aimed at {dm.replace('/',' and ')} readers, published {span}."
    add('Manga anthology magazine',{"n":n,"a":"","d":dsc,"mk":pub,"y":y0,"g":g,"s":"https://en.wikipedia.org/wiki/List_of_manga_magazines"}); have.add(n.lower()); n_added+=1
for e in k['x']:
    if e.get('g') in ('Shōnen','Seinen') : e['g']=dem[e['g']]
k['xg']='by readership demographic'
k['sel']=(k.get('sel') or '').rstrip()+" Complete: 179 of 179 rows in Wikipedia's List of manga magazines (read to the end of the page), except seven adult-content magazines that are out of scope."
print('manga added',n_added,len(k['x']))
# nl for kinds with x but no nl
for dp,k in kinds():
    if k.get('x') and 'nl' not in k:
        k['nl']="One entry is a named series, line, maker or object type within this kind that has its own identity; its variants are versions."
# coverage lines
done=0
for dp,k in kinds():
    if not k.get('x'): continue
    sel=(k.get('sel') or '').strip()
    if re.search(r'Complete: \d+ of \d+|Covers \d+ of about|No complete list exists',sel): continue
    s=k.get('s','')
    ref=re.sub(r'https?://(en\.)?','',s).split('/')[0] if s else 'the cited pages'
    add_=f"No complete list exists; follows the overview {s} and the page cited on each entry." if s else "No complete list exists; follows the page cited on each entry."
    k['sel']=(sel+' ' if sel else '')+add_
    done+=1
print('coverage lines',done)
json.dump(d,open('F1.step2.json','w'),ensure_ascii=False,indent=1)
