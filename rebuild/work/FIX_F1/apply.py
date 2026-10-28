import json,copy
W='https://en.wikipedia.org/wiki/'
d=json.load(open('out/F1.json'))
brands=json.load(open('out/F1_brands.json'))
moves=json.load(open('out/F1_moves.json'))
def A(n,d_,mk='',y='',s='',v=None,dt='',a=''):
    return {"n":n,"a":a,"d":d_,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
def find(name):
    for dp in d['depts']:
        for sh in dp['s']:
            for i,k in enumerate(sh['k']):
                if k['n']==name: return dp,sh,i,k
    raise KeyError(name)
def remove(name):
    dp,sh,i,k=find(name); sh['k'].pop(i); return k
def insert_after(name,kind):
    dp,sh,i,k=find(name); sh['k'].insert(i+1,kind)
def shelf(dept,sname):
    for dp in d['depts']:
        if dp['n']==dept:
            for sh in dp['s']:
                if sh['n']==sname: return sh
    raise KeyError(sname)

# ---- F1-1 comics
dp,sh,i,k=find('Single-issue comic')
cgc=[a for a in k['x'] if a['n']=='CGC-graded comic'][0]
k['t']=[t for t in k['t'] if not t.startswith('CGC')]
k['t'].insert(5,'third-party graded slab (see F3 grading register)')
k['x']=[
 A('US standard comic book','Stapled periodical comic of 32 or so pages; sold through newsstands or, from the early 1970s, direct-market comic shops.','','1930s',W+'Comic_book',
   v=[{"n":"Newsstand edition","mk":"","y":"","d":"returnable copies sold through periodical distributors"},
      {"n":"Direct edition","mk":"","y":"1972","d":"non-returnable copies sold direct to comic shops, from Phil Seuling's 1972 approach to publishers"}],
   dt='printing · newsstand or direct · cover variant · condition'),
 A('Giant-Size comic','Extra quarterly issue of a regular Marvel title, about 48 pages, run from 1974 for roughly a year.','Marvel','1974','https://theslingsandarrows.com/giant-size-marvel/',dt='title · issue number · page count'),
 A('Comic annual','Hardcover annual of repackaged or commissioned material; British Christmas annuals are A4-size.','','',W+'Comic_book',dt='publisher · year · size'),
 A('Treasury edition','Oversized 10 × 14 inch tabloid comic, mostly reprints; Marvel Treasury Edition ran 28 issues from 1974 to 1981.','Marvel','1974',W+'Marvel_Treasury_Edition',dt='publisher line · issue number · size 10 × 14 in'),
 A('Prestige-format comic','Squarebound single issue on glossy paper with a light card cover and more pages than a standard comic.','DC','1986',W+'Prestige_format',dt='binding · paper · page count'),
 A('Digest comic','Pocket-size black-and-white comic of about 100 to 132 pages, the usual Italian monthly format.','','1950',W+'Comic_book',dt='page count · size · colour or black and white'),
 A('Bonelli-format albo','Italian pocket-book comic of 98 black-and-white pages with a complete story, from Sergio Bonelli Editore.','Sergio Bonelli Editore','',W+'Sergio_Bonelli_Editore',dt='series · number · page count'),
]
# BD
dp,sh,i,k=find('Bande dessinée album')
k['m']=[]; 
std=k['x'][0]
def bd(n,mk,y,desc,src):
    return A(n,desc,mk,y,src,dt='édition originale · tirage de tête · album number')
k['x']=[std,
 bd('Dupuis album','Dupuis','1922','Albums from the Marcinelle publisher of Spirou, Gaston and The Smurfs.',W+'Dupuis'),
 bd('Dargaud album','Dargaud','1936','Albums from the Paris publisher of Asterix, Lucky Luke and Blueberry.',W+'Dargaud'),
 bd('Casterman album','Casterman','1934','Albums from the Tournai publisher of Tintin since 1934 and Corto Maltese.',W+'Casterman'),
 bd('Le Lombard album','Le Lombard','1946','Albums from the Brussels publisher launched with Tintin magazine; Blake and Mortimer, Thorgal.',W+'Le_Lombard'),
 bd('Glénat album','Glénat','1972','Albums from the Grenoble publisher known for mature historical series and manga.',W+'Gl%C3%A9nat_%C3%89ditions'),
]
moves['out'].append({"to":"F3","dept":"Grading services & slabs","kind":{
  "n":"Graded comic slab","a":"CGC slab · slabbed comic","d":"Comic graded on a 0.5–10 scale and sealed in a tamper-evident holder with a colour-coded label.",
  "t":["Universal (blue label)","Signature Series (yellow label)","Qualified (green label)","Restored (purple label)","Conserved"],
  "s":W+'Certified_Guaranty_Company',"x":[cgc]}})

# ---- F1-2
sh=shelf('Records & audio','Tapes & other audio carriers')
dp,_,i,k=find('8-track cartridge')
k['n']='Tape cartridge (4- and 8-track)'
k['a']='8-track · Stereo 8 · eight-track tape · 4-track cartridge · Stereo-Pak'
k['d']='Endless-loop tape cartridge for car and home players, in four-track (Stereo-Pak) and eight-track forms.'
k['t']=['4-track','8-track stereo','Quad-8 (quadraphonic)','blank','pre-recorded','sealed']
for a in k['x']:
    if a['n']=='Stereo-Pak':
        a['d']="Earl Muntz's four-track cartridge, adapted from the Fidelipac broadcast cartridge with George Eash, which Lear's eight-track replaced."
        a['y']='1962'; a['s']=W+'Stereo-Pak'; a['a']='4-track cartridge'; a['dt']='four-track · label · shell'
k['x'].reverse() if False else None
k['x']=[a for a in k['x'] if a['n']=='Stereo 8']+[a for a in k['x'] if a['n']=='Stereo-Pak']
dp,_,i,k=find('LP record'); k['t'].append('test pressing')
piano=dict(n='Piano roll',a='player-piano roll · pianola roll · reproducing roll',
 d='Perforated paper roll that plays a player piano; reproducing rolls also encode touch and dynamics.',
 t=['65-note','72-note (German)','88-note','standard 11¼-inch width (1908)','reproducing roll','hand-played roll','arranged (non-reproducing) roll'],
 s=W+'Piano_roll',
 x=[A('Welte-Mignon roll','Rolls of the earliest reproducing piano system, recorded from performances between 1905 and 1932.','','1905',W+'Piano_roll',dt='roll number · artist · condition'),
    A('Duo-Art roll','Rolls for the Aeolian Company reproducing system, with recordings made 1913 to 1925.','Aeolian','1913',W+'Duo-Art',dt='roll number · artist · hand-played or arranged'),
    A('Ampico roll','Rolls for the American Piano Company reproducing system, offered from 1914 and discontinued in 1941.','American Piano Company','1914',W+'Ampico',dt='roll number · artist'),
    A('QRS roll','Rolls from the roll maker founded in 1900, still adding new titles.','QRS Music','1900',W+'QRS_Music_Technologies',dt='88-note · title · era')])
wire=dict(n='Dictation and wire recording',a='wire spool · Dictabelt · magnetic wire',
 d='Voice and office recording media outside the tape cassette: steel wire on spools and the Dictaphone plastic belt.',
 t=['wire spool (15 or 30 min)','heavy-duty Armour spool','plastic belt (about 15 min)','blank','recorded'],
 s=W+'Wire_recording',
 x=[A('Wire recorder spool','Fine steel wire magnetised by the recorder, used from 1903 and at its peak about 1946 to 1954.','Webster-Chicago','1946',W+'Wire_recording',
       v=[{"n":"Webster-Chicago Model 7","mk":"Webster-Chicago","y":"1948","d":"postwar home wire recorder"}],dt='spool length · recorder make'),
    A('Dictabelt','Plastic belt about 3.5 inches wide and 12 inches around with a helical groove, holding about 15 minutes.','Dictaphone','1947',W+'Dictabelt',dt='length · recorded or blank')])
sh['k'][0:0]=[]  # placeholder
insert_after('Microcassette',piano)
insert_after('Piano roll',wire)
# F1-4 merge
dp,sh2,i,vhs=find('VHS cassette')
vhs['a']+=' · S-VHS · Super VHS · W-VHS · Wide-VHS'
vhs['t']+=['S-VHS (1987, needs S-VHS deck for full resolution)','W-VHS (1993, analogue high-definition)']
remove('S-VHS cassette'); remove('W-VHS cassette')
remove('VHS-C cassette'); remove('MiniDV cassette'); e8=remove('8 mm video cassette')
cam=dict(n='Camcorder cassette',a='VHS-C · Video8 · Hi8 · Digital8 · MiniDV',
 d='Small tape cassette made for camcorders, mostly blank or home-recorded, in compact VHS, 8 mm and DV forms.',
 t=['VHS-C (1982)','S-VHS-C','VHS-C with adapter','Video8 (1984)','Hi8 (1989)','Digital8 (1999)','MiniDV (1995)','HDV (2003)','SP or LP recording'],
 s=W+'8_mm_video_format')
insert_after('Video 2000 cassette',cam)
dat=remove('DAT cassette'); dcc=remove('Digital Compact Cassette'); elc=remove('Elcaset')
late=dict(n='Digital and late analogue cassette',a='DAT · Digital Audio Tape · DCC · Elcaset',
 d='Short-lived hi-fi cassette formats beyond the compact cassette: DAT, Digital Compact Cassette and the large Elcaset.',
 t=['DAT (16-bit, 15–180 min)','DDS (computer data)','DCC (PASC compression, plays analogue cassettes)','Elcaset (¼-inch tape, 1976–1980)','blank','pre-recorded'],
 s=dat['s'])
insert_after('Microcassette',late) if False else None
sh_t=shelf('Records & audio','Tapes & other audio carriers')
sh_t['k'].insert([k['n'] for k in sh_t['k']].index('Dictation and wire recording')+1,late)
# F1-3 popular shelf
pop={"n":"Popular & cheap fiction formats","k":[
 dict(n='Dime novel',a='nickel novel · story paper',d='Inexpensive American paperbound fiction series of the late 19th and early 20th centuries.',t=['6.5 × 4.25 in, about 100 pages','weekly, 32 pages','thick book reprint','coloured cover'],s=W+'Dime_novel',
  x=[A('Beadle\'s Dime Novels',"Beadle's ten-cent series of about 100 pages, from June 1860; the series ran 321 issues.",'Beadle & Adams','1860',W+'Dime_novel',v=[{"n":"New Dime Novels","mk":"Beadle & Adams","y":"1874","d":"colour covers; ran to 1885"}],dt='number · cover · condition'),
     A('Five-cent weekly','8.5 × 11 inch weekly of 32 pages with coloured cover, sold for five cents by Tousey and Street & Smith.','Street & Smith','1896',W+'Dime_novel',dt='publisher · series · number'),
     A('Thick book series','About 4.75 × 7 inch reprint volumes of 150 to 200 pages gathering weekly stories.','','',W+'Dime_novel',dt='series · number')]),
 dict(n='Penny dreadful',a='penny blood · penny serial',d='Cheap sensational British weekly serial of 8 to 16 pages, from 1836.',t=['weekly part','story paper','booklet library','bound volume'],s=W+'Penny_dreadful',
  x=[A('Penny serial part','Weekly one-penny instalment on wood-pulp paper with illustrations, aimed at young working-class readers.','','1836',W+'Penny_dreadful',dt='publisher · title · part number'),
     A('Halfpenny boys\' paper','Alfred Harmsworth\'s halfpenny weekly that challenged the dreadfuls from 1893.','','1893',W+'Penny_dreadful',dt='title · issue')]),
 dict(n='Yellowback',a='mustard-plaster novel · railway novel',d='Cheap British novel of the later 19th century with brightly coloured printed covers.',t=['chromoxylographed cover','reprint of cloth edition','railway library','sensation fiction'],s=W+'Yellowback',
  x=[A('Routledge Railway Library','George Routledge\'s series, launched 1848 and running to 1,277 titles over 50 years.','George Routledge','1848',W+'Yellowback',dt='series number · cover · condition')]),
 dict(n='Big Little Book',a='Whitman tall-and-thick book',d='Small thick American children\'s book with text facing a captioned picture on each page.',t=['3⅝ × 4½ in','212–432 pages','10 cent','15 cent'],s=W+'Big_Little_Book',
  x=[A('Big Little Book','Whitman\'s 1932 format, text pages facing captioned illustrations.','Whitman Publishing','1932',W+'Big_Little_Book',v=[{"n":"Better Little Books","mk":"Whitman Publishing","y":"1938","d":"renamed series, continued into the 1960s"}],dt='number · cover · condition')]),
 dict(n='Children\'s annual',a='Christmas annual · hardcover annual',d='Hardcover yearly collection for children, often A4-size and mostly repackaged or commissioned material.',t=['A4','dated year','Christmas gift'],s=W+'Comic_book',x=[]),
]}
dpb=[x for x in d['depts'] if x['n']=='Books'][0]
dpb['s'].insert(3,pop)
# photobook & catalogue
for kn,kind in [('Artist\'s book',dict(n='Photobook',a='photo book · photographic book',d='Book in which photographs make a significant contribution to the content.',t=['tipped-in prints','offset printed','case bound','personalised digital print'],s=W+'Photobook',
   x=[A('Tipped-in photographic book','Early book with real photographic prints tipped in, often issued in parts and in very small editions.','','1843',W+'Photobook',dt='prints · parts · edition size'),
      A('Personalised photo book','Case-bound book printed on digital colour printers with the customer\'s pictures and text.','','',W+'Photobook',dt='size · binding')])),
   ('Hardback book',dict(n='Exhibition catalogue',a='museum catalogue · gallery catalogue',d='Printed or digital document made to display, promote and record an exhibition.',t=['handlist','descriptive catalogue','multi-volume catalogue','paperback','trade fair directory'],s=W+'Exhibition_catalogue',
   x=[A('Descriptive catalogue','Book-sized catalogue with colour plate of each item, description, essays and bibliography.','','1960s',W+'Exhibition_catalogue',dt='essays · plates · volumes'),
      A('Handlist','Plain list of exhibits, the usual form before cheap colour printing in the 1960s.','','',W+'Exhibition_catalogue',dt='sheets · pages'),
      A('Trade fair catalogue','Directory of exhibitors with floor plan, profiles and advertisements.','','',W+'Exhibition_catalogue',dt='booklet or directory')]))]:
    insert_after(kn,kind)
# F1-6 sheet music
dp,sh,i,k=find('Songbook')
perf=dict(n='Performing edition (urtext / practical)',a='urtext edition · critical edition · classical edition',d='Classical score published as an urtext or practical edition, compared by publisher and editor.',
 t=['urtext edition','practical (edited) edition','with fingering','paperbound','clothbound'],s=k['s'],x=k['x'])
k['x']=[]
k['a']='collection · album · fake book'
k['d']='Bound volume of popular songs in notation for voice, piano or guitar, from lead-sheet books to easy arrangements.'
k['t']=['piano/vocal/guitar (PVG)','lead-sheet book (fake book)','easy arrangement','with audio','paperbound','spiral-bound']
sh['k'].insert(i,perf)
fake=dict(n='Fake book',a='Real Book · lead-sheet book',d='Collected volume of lead sheets giving melody, lyrics and chord symbols.',t=['photocopied','retyped','licensed edition'],s=W+'Fake_book',
 x=[A('Tune-Dex card','3 × 5 inch index card with lyrics, melody, chord symbols and copyright data; the direct predecessor, from 1942.','','1942',W+'Fake_book'),
    A('Real Book','Berklee musicians\' fake book of 1974–75 with a more contemporary repertoire, widely copied.','','1974',W+'Fake_book',dt='edition · licensed or unlicensed')])
insert_after('Songbook',fake)
# F1-5 storage
for dp in d['depts']:
    if dp['n']=='Storage & protection':
        for sh in dp['s']:
            for k in sh['k']:
                if k.get('m'):
                    by={}
                    for n_,mk in k['m']: by.setdefault(mk,[]).append(n_)
                    new=[]
                    for mk,ns in by.items():
                        nm=ns[0] if len(ns)==1 else {'Comic bag':'Comic bags','Backing board':'Comic backing boards','Record inner sleeve':'Inner sleeves','Record outer sleeve':'Outer sleeves','Record storage box':'Storage boxes'}.get(k['n'],ns[0].split()[0]+' range')
                        if k['n']=='Comic bag' and mk=='E. Gerber': nm='Mylites'
                        if k['n']=='Backing board' and mk=='E. Gerber': nm='Backing boards'
                        new.append([nm,mk])
                    k['m']=new
dp,sh,i,k=find('CD-R')
k['t']=['74- or 80-minute','gold archival (phthalocyanine dye)','music CD-R','CD-RW (rewritable)']
# brands
def B(n,c,f,seg,kf,dd,s,**kw):
    b={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":dd,"s":s,"lines":[],"eras":[],"sig":[],"sc":[],"rel":[]};b.update(kw);return b
have={b['n'] for b in brands['b']}
new=[B('Glénat','France','1972','Mainstream','bande dessinée','Grenoble publisher of comic albums and manga, founded by Jacques Glénat.',W+'Gl%C3%A9nat_%C3%89ditions'),
 B('Sergio Bonelli Editore','Italy','1940','Mainstream','Italian comics','Italian publisher of pocket-format black-and-white comics, founded as Casa Audace Editrice.',W+'Sergio_Bonelli_Editore'),
 B('QRS Music','United States','1900','Specialist','piano rolls','Maker of player-piano rolls, founded in 1900 as the Q•R•S Music Company.',W+'QRS_Music_Technologies'),
 B('American Piano Company','United States','1908','Heritage manufactory','Ampico','Piano maker formed 1908 whose Ampico reproducing system began in 1914.',W+'Ampico'),
 B('Aeolian','United States','','Heritage manufactory','Duo-Art','Maker of the Duo-Art reproducing piano system, introduced 1913.',W+'Duo-Art'),
 B('Webster-Chicago','United States','','Mainstream','wire recorders','Maker of postwar wire recorders such as the Model 7 (1948).',W+'Wire_recording'),
 B('Beadle & Adams','United States','1860','Specialist','dime novels','Publisher of Beadle\'s Dime Novels from 1860.',W+'Dime_novel'),
 B('George Routledge','United Kingdom','1848','Mainstream','yellowbacks','Publisher who launched the Railway Library of yellowbacks in 1848.',W+'Yellowback'),
 B('Whitman Publishing','United States','','Mainstream','children\'s books','Racine, Wisconsin publisher of the Big Little Book from 1932.',W+'Big_Little_Book')]
for b in new:
    if b['n'] not in have: brands['b'].append(b)
for b in brands['b']:
    if b['n']=='Dupuis': b['s']=W+'Dupuis'
for fn,o in [('out/F1.json',d),('out/F1_brands.json',brands),('out/F1_moves.json',moves)]:
    json.dump(o,open(fn+'.tmp','w'),ensure_ascii=False,indent=1)
