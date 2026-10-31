import json, os, copy
R='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(R+'F1.json')); br=json.load(open(R+'F1_brands.json'))
WP='https://en.wikipedia.org/wiki/'
def dept(n): return [x for x in d['depts'] if x['n']==n][0]
def shelf(dn,sn): return [s for s in dept(dn)['s'] if s['n']==sn][0]
def kind(n):
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']:
                if k['n']==n: return k
    raise KeyError(n)
def decade(y):
    y=int(str(y)[:4]); return f"{y//10*10}s"
def ent(n,y,d_,s,mk='',g=None,**kw):
    e={'n':n,'a':kw.pop('a',''),'d':d_,'mk':mk,'y':str(y),'s':s,'v':kw.pop('v',[]),'dt':kw.pop('dt','')}
    if g: e['g']=g
    e.update(kw); return e
def setnl(k,nl,sel,xg=None):
    k['nl']=nl; k['sel']=sel
    if xg: k['xg']=xg
def mkkind(n,a,d_,s,x,nl,sel,xg,tt):
    k={'n':n,'a':a,'d':d_,'s':s,'x':x,'tt':tt}
    setnl(k,nl,sel,xg); return k
GEN_NL="One entry is a named series, line or object type within this kind that has its own identity; its variants are versions."
GEN_SEL="No complete reference list exists for this space. The entries are those named by the source cited on each entry and are not a complete canon; a later pass is needed."

# ---- 1. generic nl/sel for existing kinds with entries (set later if specific)
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            if k.get('x') and 'nl' not in k: setnl(k,GEN_NL,GEN_SEL)

# ---- 2. commodity trim: blank cassette brands
k=kind('Compact cassette')
removed_cass=[x['n'] for x in k['x'] if x['n']!='Philips Compact Cassette']
k['x']=[x for x in k['x'] if x['n']=='Philips Compact Cassette']
k['x'][0]['role']='origin'
setnl(k,"One entry is the original cassette format; branded blank tapes (TDK, Maxell and others) are a commodity and are not named.",
 "Commodity kind: only the origin entry is kept, the Philips Compact Cassette of 1963 as stated by Wikipedia's Magnetic tape sound recording. Blank-tape brand lines were removed under the icon rule in BRIEF.md.")
k['x'][0]['s']=WP+'Magnetic_tape_sound_recording'

# ---- 3. private presses (complete list on Wikipedia Private press)
P=[("John Hunter's private press","United Kingdom","1786"),("Laboratory Press","United States","1923"),("Püterschein-Hingham private press","","1947"),("Ashendene Press","United Kingdom",""),("Kelmscott Press","United Kingdom","1891"),
("Holloway Press","New Zealand","1994"),("Wai-te-ata Press","New Zealand",""),("Otakou Press","New Zealand",""),
("Abattoir Editions","United States",""),("Appledore Private Press","United States","1867"),("Arion Press","United States","1974"),("Ashantilly Press","United States","1954"),("Bird & Bull Press","United States","1952"),("Black Rock Press","United States","1965"),("Gehenna Press","United States","1942"),("Hammer Creek Press","United States","1954"),("Mosher Press","United States","1891"),("Perishable Press","United States","1964"),("Roycroft Press","United States","1895"),("Something Else Press","United States","1963"),("Stone Wall Press","United States","1957"),("Stratford Press (Cincinnati)","United States","1920"),("Trovillion Private Press","United States","1908"),
("M. Bernard Loates, A Private Press","Canada","1968"),("Locks' Press","Canada","1979"),("Dun Emer Press","Ireland","1903"),
("Daniel Press","United Kingdom","1874"),("Doves Press","United Kingdom","1900"),("Essex House Press","United Kingdom","1897"),("Golden Cockerel Press","United Kingdom","1920"),("Gregynog Press","United Kingdom","1922"),("Happy Dragons' Press","United Kingdom","1969"),("Hogarth Press","United Kingdom","1917"),("Jericho Press","United Kingdom","1985"),("Kynoch Press","United Kingdom","1876"),("Nonesuch Press","United Kingdom","1922"),("Officina Typographica","United Kingdom","1963"),("Gaetano Polidori's private press","United Kingdom","c. 1800"),("Rampant Lions Press","United Kingdom","1924"),("Stanbrook Abbey Press","United Kingdom",""),("Strawberry Hill Press","United Kingdom",""),
("Black Sun Press","France","1927"),("Contact Publishing Company","France","1923"),("Harrison of Paris","France","1930"),("Hours Press","France","1928"),("Plain Edition Press","France","c. 1930"),
("Finlay Press","Australia","1997"),("Private Press of Ariel Wardi","Israel","1989")]
reg={"Kelmscott Press":"Founded by William Morris.","Doves Press":"Founded by T. J. Cobden-Sanderson and Emery Walker.","Golden Cockerel Press":"Founded by Harold Midgley Taylor.","Nonesuch Press":"Founded by Francis Meynell, Vera Meynell and David Garnett.","Hogarth Press":"Founded by Leonard and Virginia Woolf.","Arion Press":"Founded by Andrew Hoyem.","Gregynog Press":"Founded by Gwendoline and Margaret Davies."}
order={'United Kingdom':0,'Ireland':1,'United States':2,'Canada':3,'France':4,'New Zealand':5,'Australia':6,'Israel':7,'':8}
xs=[]
for n,c,y in P:
    g=c or 'Country not stated'
    xs.append(ent(n,y if y else '', reg.get(n,"Private press listed by Wikipedia."), WP+'Private_press', g=g, mk=n))
xs.sort(key=lambda e:(order.get(e['g'] if e['g']!='Country not stated' else '',8), e['y'].replace('c. ','') or '9999', e['n']))
k=kind('Private press book'); old=[x['n'] for x in k['x']]
k['x']=xs
setnl(k,"One entry is a private press, a press run for its owner's taste rather than for the trade, whose books are collected as a body; its books are not listed.",
 "Every press named in a list entry of Wikipedia's Private press, grouped by country. Complete: 48 of 48 in Private press. Individual books (Kelmscott Chaucer, Doves Bible) are titles and are out of scope.","by country")
k['xg']="by country"

# ---- 4. edition classes
EC=[("Editio princeps","The first printed edition of a classical or medieval work."),
("First edition","The first print run of the first edition, also called first edition, first impression."),
("First trade edition","The earliest edition of a book offered for sale to the general public in bookshops."),
("New edition","A new iteration not substantially different from the previous one, numbered as the next edition."),
("Revised edition","An edition that was editorially revised and is labelled revised rather than as the next numbered edition."),
("Revised and updated edition","A non-fiction edition updated after further research."),
("Critical edition","A scholarly edition with commentary and the developmental history of the work."),
("Co-edition","The same edition of a book published by two publishing houses, usually in different countries."),
("Library edition","A copy from the same setting with a stronger binding and hinges for heavy library use."),
("Cheap edition","An edition on low-cost paper, typically a paperback."),
("Colonial edition","A cheap edition of a British novel made for sale in the colonies."),
("Cadet edition","A cut-down, more simply written version of a book."),
("Large-print edition","A library-style edition with much larger text for readers with poor eyesight.")]
xs=[ent(n,'',dd,WP+'Edition_(book)',dt='') for n,dd in EC]
k=mkkind('Edition class',"","A class of edition named by what the publisher changed or intended, which collectors and dealers use to describe a copy.",WP+'Edition_(book)',xs,
 "One entry is a named class of edition as defined in Wikipedia's Edition (book); the book club edition has its own kind.",
 "Every edition class that Wikipedia's Edition (book) defines, except the book club edition (its own kind here), the e-dition (not an object) and the Sustainers' Edition (one title). Complete: 13 of 13 defined classes in scope in Edition (book).",
 "by purpose",[["Copy state",["Sealed","Used"]],["Printing",["First printing","Later printing"]]])
shelf('Books','Publisher special editions')['k'].append(k)

# ---- 5. book sheet formats
W=[("Folio","2º · fo",2,4),("Quarto","4º · 4to",4,8),("Imperial octavo","8º · 8vo",8,16),("Duodecimo","12º · 12mo",12,24),("Sextodecimo","16º · 16mo",16,32),("Octodecimo","18º · 18mo",18,36),("Trigesimo-secundo","32º · 32mo",32,64),("Quadragesimo-octavo","48º · 48mo",48,96),("Sexagesimo-quarto","64º · 64mo",64,128)]
xs=[ent(n,'',f"Book format of {l} leaves ({p} pages) to the sheet.",WP+'Book_size',a=a,g='Western formats',dt='') for n,a,l,p in W]
kw=mkkind('Western sheet format',"folding format · bibliographic format","Book named by how many times the printing sheet was folded: folio, quarto, octavo and the smaller sizes.",WP+'Book_size',xs,
 "One entry is a Western book format named by the number of leaves a folded sheet gives.",
 "Complete: 9 of 9 Western formats in the table of Wikipedia's Book size.","by leaves per sheet",[["Binding",["Hardback","Paperback"]],["Condition",["Fine","Used"]]])
J=[("B4判 (JIS B4)",8,16),("A4判 (ISO A4)",8,16),("AB判",16,32),("B5判 (JIS B5)",16,32),("菊判 (Kiku)",16,32),("A5判 (ISO A5)",16,32),("重箱判 (Jūbako)",20,40),("四六判 (Shi-Roku)",32,64),("B6判 (JIS B6)",32,64),("新書判 (Shinsho, B40)",40,80),("小B6判 (Small JIS B6)",32,64),("A6判 (ISO A6)",32,64),("三五判 (San-Go)",40,80)]
xs=[ent(n,'',f"Japanese book format of {l} leaves ({p} pages) to the sheet.",WP+'Book_size',g='Japanese formats') for n,l,p in J]
kj=mkkind('Japanese book format',"hanri · 判","Book named by one of the Japanese sheet sizes, such as Kiku, Shinsho or the A and B series.",WP+'Book_size',xs,
 "One entry is a Japanese book format named by a sheet size and the leaves it gives.",
 "Complete: 13 of 13 Japanese formats in the table of Wikipedia's Book size.","by leaves per sheet",[["Binding",["Hardback","Paperback"]],["Condition",["Fine","Used"]]])
d['depts'][0]['s'].append({'n':'Book formats','t':'Books named by the size and folding of the printing sheet, Western and Japanese.','ax':'Which sheet format names the book: a Western folded-sheet size or a Japanese standard size?','k':[kw,kj]})

# ---- 6. videotape formats
V=[l.split(' – ') for l in """Quadruplex – 1956 – Ampex
Simplex – 1953 – RCA
VERA – 1958 – BBC
Ampex 2 inch helical VTR – 1961 – Ampex
Sony 2 inch helical VTR – 1961 – Sony
Type A – 1965 –
CV-2000 – 1965 –
Akai – 1967 –
EIAJ-1 – 1969 –
Type B – 1976 –
Type C – 1976 –
Betacam – 1982 – Sony
Betacam SP – 1986 –
MII – 1986 – Panasonic
D1 – 1986 – Sony
D2 – 1988 – Sony
D3 – 1991 – Panasonic
DCT – 1992 – Ampex
Digital Betacam – 1993 – Sony
D5 – 1994 – Panasonic
Digital-S (D9) – 1995 – JVC
Betacam SX – 1996 – Sony
MPEG IMX – 2000 –
M – 1982 –
Sony HDVS – 1984 – Sony
UniHi – 1984 –
BCH 1000 – 1992 –
HDCAM – 1997 – Sony
D6 HDTV VTR – 2000 –
HDCAM SR – 2003 – Sony
DVCPRO – 1995 – Panasonic
DVCAM – 1996 – Sony
DVCPRO50 – 1997 – Panasonic
DVCPRO HD – 2000 – Panasonic
Philips VCR – 1972 – Philips
V-Cord – 1974 –
VX – 1974 –
IVC – 1975 –
Akai VK – 1977 –
SVR – 1979 –
Compact Video Cassette – 1980 –
S-VHS – 1987 –
S-VHS-C – 1987 –
Ruvi – 1998 –
W-VHS – 1994 –
D-VHS – 1998 –
HDV – 2003 –
MicroMV – 2001 – Sony""".split('\n')]
V=[([c.strip() for c in r]+['',''])[:3] if len(r)<3 else [c.strip() for c in r] for r in V]
V=[[r[0],r[1],r[2]] for r in V]
openreel=V[:11]; pro=V[11:34]; cons=V[34:]
def vx(rows,tag):
    out=[]
    for n,y,mk in sorted(rows,key=lambda r:(r[1],r[0])):
        out.append(ent(n,y,f"{n} is a {tag} videotape format introduced in {y}"+(f" by {mk}." if mk else "."),WP+'Videotape',mk=mk,g=decade(y)))
    return out
VT="Videotape"
ko=mkkind('Open-reel videotape',"reel-to-reel videotape · VTR","Videotape on open reels played on a recorder, as used in early broadcast and home machines.",WP+VT,vx(openreel,'open-reel'),
 "One entry is an open-reel videotape format named by Wikipedia's Videotape.",
 "Open-reel formats of the list in Wikipedia's Videotape. Covers 11 of 70 rows; see Broadcast and professional videotape cassette and Minor consumer videotape cassette for the cassette rows.","by decade",[["Width",["2 inch","1 inch","1/2 inch"]],["Condition",["Sealed","Used"]]])
kp=mkkind('Broadcast and professional videotape cassette',"studio videotape","Videotape cassette made for broadcast and production use, from Betacam and the D-series to HDCAM and DVCPRO.",WP+VT,vx(pro,'professional'),
 "One entry is a broadcast or professional videotape cassette format named by Wikipedia's Videotape.",
 "Professional cassette rows of the list in Wikipedia's Videotape. Covers 23 of 70 rows.","by decade",[["Cassette size",["Small","Medium","Large"]],["Condition",["Sealed","Used"]]])
kc=mkkind('Minor consumer videotape cassette',"short-lived videotape cassette · prosumer videotape","Videotape cassette formats sold to consumers that are not VHS, Betamax or Video 2000, plus the S-VHS, D-VHS and HDV extensions.",WP+VT,vx(cons,'consumer or prosumer'),
 "One entry is a consumer or prosumer videotape cassette format named by Wikipedia's Videotape.",
 "Remaining cassette rows of the list in Wikipedia's Videotape. Covers 14 of 70 rows. Across the three videotape kinds and the existing kinds the list is covered except 12 file-based or disc rows (MOD, AVCHD, AVC-Intra, TOD, iFrame, XAVC, P2, SxS, MicroP2, XDCAM, GBA-TV, CamCutter Editcam), which belong to cameras; 10 rows are existing kinds (U-matic, Cartrivision, Betamax, VHS, Video 2000, VHS-C, Video8, Hi8, DV, Digital8). Total 48 + 10 + 12 = 70 rows.","by decade",[["Tape",["Standard","Super (S-VHS)"]],["Condition",["Sealed","Used"]]])
d['depts'][2]['s'].insert(1,{'n':'Open-reel & broadcast videotape','t':'Videotape formats made for studios, broadcasters and early open-reel recorders rather than for the living room.','ax':'Is the tape on open reels or in a cassette made for broadcast and professional use?','k':[ko,kp]})
shelf('Films & video','Videotape cassettes')['k'].append(kc)
tot=len(V); print('video counts',len(openreel),len(pro),len(cons),tot); assert (len(openreel),len(pro),len(cons))==(11,23,14), 'cnt'

# ---- 7. optical discs
OD=[("WORM disc (Write Once Read Many)","1979–1984","0.2–6.0 GB"),("Electron Trapping Optical Memory (ETOM)","1987–1996","6.0–12.0 GB"),("Magneto-optical disc (MOD)","1990–present","0.1–16.7 GB"),("LIMDOW","1996–present","2.6 GB, 10 GB"),("GD-ROM","1997–2006","1.2 GB"),("Fluorescent Multilayer Disc","1998–2003","50–140 GB"),("Versatile Multilayer Disc (VMD)","1999–2010","5–20 GB, 100 GB"),("Hyper CD-ROM","1999–present","1 PB claimed, no working prototype"),("DataPlay","1999–2006","500 MB"),("Ultra Density Optical (UDO)","2000–present","30–60 GB"),("Forward Versatile Disc (FVD)","2005–2006","5.4–15 GB"),("Enhanced Versatile Disc (EVD)","2002–2004","DVD-class"),("BDXL","2010–present","100 GB, 128 GB, 1 TB"),("Professional Disc for Data (PDD)","2003–2006","23 GB"),("Professional Disc","2003–present","23–128 GB"),("Digital Multilayer Disk","2004–2007","22–32 GB"),("Multiplexed Optical Data Storage (MODS-Disc)","2004–present","250 GB–1 TB"),("Universal Media Disc (UMD)","2004–2014","0.9–1.8 GB"),("Holographic Versatile Disc (HVD)","2004–2012","6.0 TB"),("Protein-coated disc (PCD)","2005–2006","50 TB"),("M-DISC","2009–present","4.7 GB, 25 GB, 50 GB, 100 GB"),("Archival Disc","2014–2024","0.3–1 TB"),("Optical Disc Archive","2012–2024","0.3–5.5 TB")]
assert len(OD)==23
xs=[ent(n,yr[:4],f"Optical disc format sold or announced {yr.replace('–',' to ')}, capacity {cap}.",WP+'Optical_disc',g=decade(yr[:4])) for n,yr,cap in sorted(OD,key=lambda r:(r[1],r[0]))]
ks=mkkind('Specialist and archival optical disc',"data disc · game disc","Optical disc formats other than CD, DVD, Blu-ray, HD DVD, LaserDisc and MiniDisc, including game, archival and short-lived formats.",WP+'Optical_disc',xs,
 "One entry is an optical disc format named in the overview table of Wikipedia's Optical disc.",
 "Complete: 23 of 23 rows of the Overview of optical types table that are not already kinds here (the other 7 rows are LaserDisc, CD, MiniDisc, DVD, HD DVD, Blu-ray and Ultra HD Blu-ray). Read 100,000 of 144,989 characters of the page, which included the whole table. Data-storage rows belong with computer storage; placement flagged in the report.","by decade",[["Capacity",["Under 1 GB","1 GB to 100 GB","Over 100 GB"]],["Condition",["Sealed","Used"]]])
shelf('Records & audio','CDs & digital audio discs')['k'].append(ks)

# ---- 8. tape cartridges, film formats, record sizes
shelf('Records & audio','Magnetic tape')['k'] += [
 mkkind('RCA tape cartridge',"RCA cartridge","Audio tape cartridge made by RCA.",WP+'Magnetic_tape_sound_recording',[],"","",None,[["Content",["Pre-recorded","Blank"]]]),
 mkkind('Endless tape cartridge',"loop cartridge","Audio tape cartridge in which the tape runs as an endless loop.",WP+'Magnetic_tape_sound_recording',[],"","",None,[["Content",["Pre-recorded","Blank"]]])]
for kk in shelf('Records & audio','Magnetic tape')['k'][-2:]:
    for f in('x','nl','sel'): kk.pop(f,None)
kk=kind('Reel-to-reel tape'); kk['sel']+=" Audio tape rows of Wikipedia's Magnetic tape sound recording: covers 9 of 17 (reel-to-reel, 8-track, Compact Cassette, DCC, Microcassette, DAT, Elcaset, RCA cartridge, endless cartridge are kinds); the other 8 are pre-1950 experimental or studio tapes (Volta, Blattnerphone, Marconi-Stille, Magnetophon, Soundmirror and similar)."
shelf('Records & audio','Early & special-build records')['k'] += [
 {'n':'16⅔ rpm background-music record','a':'Seeburg Background Music System record','d':'Nine-inch record played at 16⅔ rpm in the Seeburg Background Music System of 1959.','s':WP+'Phonograph_record','tt':[["Condition",["Mint","Used"]]]},
 {'n':'V-Disc','a':'Victory Disc','d':'Twelve-inch vinyl record played at 78 rpm, made for the American forces in the Second World War.','s':WP+'Phonograph_record','tt':[["Condition",["Mint","Used"]]]}]
kk=kind('LP record'); kk['sel']+=" Format coverage: the 10 size-and-speed rows of the standard-formats table in Wikipedia's Phonograph record are all kinds here (16 inch transcription; 12 inch LP, maxi single and 78; 10 inch LP, EP and 78; 7 inch EP and single); plus the 16⅔ rpm and V-Disc rows from its text. Read 100,000 of 219,400 characters."
sh=shelf('Films & video','Film prints')
fx=[("CinemaScope","1953"),("VistaVision","1954"),("Technirama","1956"),("Modern anamorphic","1957"),("Techniscope","1960"),("Super 35","1982"),("Todd-AO","1955"),("Ultra Panavision 70","1957"),("Super Panavision 70","1959"),("IMAX","1970"),("Cinerama","1952"),("Kinopanorama","1958"),("Cinemiracle","1958")]
xs=[ent(n,y,f"{n} is a film format introduced in {y}.",WP+'Film_format',g=decade(y)) for n,y in sorted(fx,key=lambda r:(r[1],r[0]))]
sh['k'].append(mkkind('Large and widescreen film format',"wide-gauge film · widescreen print","Film print made in a named large-negative, anamorphic or multi-strip system for cinema projection.",WP+'Film_format',xs,
 "One entry is a named cinema film format from Wikipedia's Film format.",
 "Complete: 13 of 13 formats in the Film formats section of Wikipedia's Film format as read.","by decade",[["Gauge",["35 mm","70 mm"]],["Condition",["Mint","Used"]]]))
for n in('17.5 mm print','70 mm print'):
    sh['k'].append({'n':n,'a':n.replace(' print',' film'),'d':f"Cinema film print on {n.split()[0]} mm gauge film.",'s':WP+'Film_format','tt':[["Condition",["Mint","Used"]]]})

# ---- 9. collector lines
A='https://en.wikipedia.org/wiki/'
k=kind('Hardback book')
k['x'].append(ent('Folio Society','1947','London publisher of illustrated hardback editions of classics, with hand-numbered limited editions.',A+'Folio_Society',mk='Folio Society',a='The Folio Society',
 v=[{'n':'Limited Editions','mk':'Folio Society','y':'','d':'hand-numbered, sometimes with prints or signatures'}],dt='slipcase · illustrator · numbering',own='Folio Society employee ownership trust',own_y='2021',tier='Independent',cty='United Kingdom'))
k=kind('Subscription collector edition')
k['x']=[ent('Easton Press','1975','American maker of leather-bound collector editions sold by series.',A+'Easton_Press',mk='Easton Press',a='',
 v=[{'n':n,'mk':'Easton Press','y':'','d':'series'} for n in ["The Greatest Books Ever Written","Masterpieces of American Literature","The Library of American Presidents","The Library of American History","Roger Tory Peterson Field Guides","Library of Fly-Fishing Classics","Signed Modern Classics","Flyway of Life","The Masterpieces of Science Fiction"]],
 dt='series · leather grade · signed or unsigned',own='MBI, Inc.',tier='Independent',cty='United States')]
setnl(k,"One entry is a publisher of subscription collector editions; its numbered series are versions.","Easton Press, from Wikipedia's Easton Press (the page gives the founding year as 1975 in the infobox and conflicts elsewhere). No whole-space list of collector-edition publishers was fetched; Franklin Library is in the brand register.")
k=kind('LP record')
for x in k['x']:
    if x['mk']=='Mobile Fidelity Sound Lab': x.update(own='Music Direct',own_y='2001',tier='Independent',cty='United States')
    if x['mk']=='Analogue Productions': x.update(own='Acoustic Sounds, Inc.',tier='Independent',cty='United States')
k['sel']="Audiophile and collector reissue lines of Mobile Fidelity, Analogue Productions, Blue Note and Craft Recordings, from the pages cited on each entry; no whole-space list was fetched. Mobile Fidelity: founded 1977, assets bought by Music Direct in 2001 (Wikipedia). Analogue Productions: founded 1992, a division of Acoustic Sounds, Inc. (Wikipedia). "+k['sel'] if 'Format coverage' not in k['sel'] else "Audiophile and collector reissue lines of Mobile Fidelity, Analogue Productions, Blue Note and Craft Recordings, from the pages cited on each entry; no whole-space list was fetched. Mobile Fidelity: founded 1977, assets bought by Music Direct in 2001. Analogue Productions: founded 1992, a division of Acoustic Sounds, Inc. (Wikipedia). "+k['sel']
k['nl']="One entry is a collector or audiophile LP line of a label or reissuer; its pressings are versions."
k=kind('Library of America') if False else kind('Hardback book')
for x in k['x']:
    if x['n']=='Library of America': x.update(own='Literary Classics of the United States, Inc.',tier='Independent',cty='United States')
    names={v['n'].lower() for v in x['v']}
    for vn in ('Special anthologies','American Poets Project'):
        if vn.lower() not in names: x['v'].append({'n':vn,'mk':'Library of America','y':'','d':'series named on the Wikipedia page'})
k=kind('Paperback book')
for x in k['x']:
    if x['n']=='Penguin Classics':
        x.update(own='Penguin Random House',tier='Global group',cty='United Kingdom')
        have=' '.join(v['n'].lower() for v in x['v'])
        for vn in ["Penguin Nature Classics","Penguin Enriched Classics","Penguin Popular Classics","Penguin Classics Deluxe Edition","Penguin Designer Classics","Penguin Mini Modern Classics","Penguin Little Black Classics","Pocket Penguins","Penguin Clothbound Classics","Penguin Crime & Espionage"]:
            if vn.lower() not in have and vn.lower().replace('penguin ','') not in have: x['v'].append({'n':vn,'mk':'Penguin Books','y':'','d':'line named on the Wikipedia page'})
k=kind('DVD')
kb=mkkind('Boutique label edition',"collector video label · Criterion-style edition","Film release on disc by a specialist label that adds restoration, commentary and booklets.",A+'Criterion_Collection',
 [ent('Criterion Collection','1984','American label of restored films, first releasing Citizen Kane on LaserDisc in December 1984.',A+'Criterion_Collection',mk='Criterion Collection',
   v=[{'n':n,'mk':'Criterion Collection','y':'','d':'series or sub-label'} for n in ("Eclipse","Essential Art House","Janus Contemporaries","Merchant Ivory")]+[{'n':'LaserDisc','mk':'Criterion Collection','y':'1984','d':'1984 to 1999'},{'n':'DVD','mk':'Criterion Collection','y':'1998','d':'1998 to present'},{'n':'Blu-ray','mk':'Criterion Collection','y':'2008','d':'2008 to present'},{'n':'Ultra HD Blu-ray','mk':'Criterion Collection','y':'2021','d':'2021 to present'}],
   dt='spine number · format · edition',own='Steven Rales',own_y='2024',tier='Independent',cty='United States'),
  ent('Arrow Video','2009','British label of cult, horror and world-cinema releases, created in 2009 inside Arrow Films.',A+'Arrow_Films',mk='Arrow Films',
   v=[{'n':'Arrow Academy','mk':'Arrow Films','y':'','d':'world cinema, merged into Arrow Video in 2021'},{'n':'Arrow TV','mk':'Arrow Films','y':'','d':'Nordic noir, merged in 2021'},{'n':'ArrowDrome','mk':'Arrow Films','y':'2011','d':'budget DVDs'}],
   dt='limited edition · format',own='THG Ingenuity',tier='Independent',cty='United Kingdom')],
 "One entry is a boutique home-video label; its sub-labels and format runs are versions.",
 "Criterion Collection and Arrow Video, from their Wikipedia pages. No whole-space list of boutique labels was fetched; Arrow Films was sold to THG plc in 2021 and the owner is recorded as THG Ingenuity as the page states.","by country",[["Format",["LaserDisc","DVD","Blu-ray","Ultra HD Blu-ray"]],["Edition",["Standard","Limited"]]])
for e in kb['x']: e['g']='United States' if e['cty']=='United States' else 'United Kingdom'
shelf('Films & video','Video discs')['k'].append(kb)

# ---- 10. market panel and grading notes
U=lambda s:s
dept('Records & audio')['ms']=[
 {"mkt":"US recorded music, LP/EP","who":"LP/EP records","share":"$1,442.9 million","yr":2024,"s":"https://www.riaa.com/wp-content/uploads/2025/03/RIAA-2024Year-End-Revenue-Report.pdf","note":"Estimated retail value, net after returns; 43.6 million units; vinyl was nearly three quarters of physical revenue, which was $2 billion."},
 {"mkt":"US recorded music, CD","who":"CD","share":"$541.1 million","yr":2024,"s":"https://www.riaa.com/wp-content/uploads/2025/03/RIAA-2024Year-End-Revenue-Report.pdf","note":"Estimated retail value; 32.9 million units shipped; total US recorded music was $17.7 billion."},
 {"mkt":"UK recorded music, vinyl albums","who":"Vinyl albums","share":"£196 million","yr":2024,"s":"https://www.officialcharts.com/chart-news/uk-music-consumption-new-high-2024/","note":"Up 10.5 percent, as the Official Charts Company reports; physical was nearly 14 percent of revenues."},
 {"mkt":"UK recorded music, CD albums","who":"CD albums","share":"£126.2 million","yr":2024,"s":"https://www.officialcharts.com/chart-news/uk-music-consumption-new-high-2024/","note":"Flat on the year."}]
dept('Records & audio')['note']+=" Condition register: the Goldmine Grading Guide grades records and sleeves Mint (M), Near Mint (NM or M-), Very Good Plus (VG+) or Excellent (E), Very Good (VG), Good (G), Good Plus (G+) or Very Good Minus (VG-), and Poor (P) and Fair (F); values are quoted against Near Mint (https://www.goldminemag.com/collector-resources/record-grading-101)."
dept('Comics & manga')['note']+=" Condition register: CGC grades comics from 0.5 to 10 (Gem Mint 10, Mint 9.9, NM/M 9.8, down to Poor), sealed in a slab with a label colour: Universal blue, Conserved, Restored purple, Qualified green, Signature Series yellow (https://en.wikipedia.org/wiki/Certified_Guaranty_Company)."

# ---- 11. register
have={b['n'].lower() for b in br['b']}
def addb(n,c,f,seg,kf,dd,s):
    if n.lower() not in have: br['b'].append({'n':n,'c':c,'f':f,'seg':seg,'kf':kf,'d':dd,'s':s}); have.add(n.lower())
addb('Criterion Collection','United States','1984','Specialist','restored films','American label that released Citizen Kane on LaserDisc in 1984.',A+'Criterion_Collection')
addb('Steven Rales','','','Specialist','owner','Owner of the Criterion Collection from 2024 according to Wikipedia.',A+'Criterion_Collection')
addb('THG Ingenuity','United Kingdom','','Specialist','owner','Owner of Arrow Films after the 2025 spin-off from THG plc.',A+'Arrow_Films')
addb('MBI, Inc.','United States','','Specialist','owner','Parent of Easton Press.',A+'Easton_Press')
addb('Music Direct','United States','','Specialist','owner','Bought the assets of Mobile Fidelity Sound Lab in 2001.',A+'Mobile_Fidelity_Sound_Lab')
addb('Literary Classics of the United States, Inc.','United States','1979','Specialist','publisher','Publisher of the Library of America.',A+'Library_of_America')
addb('Penguin Random House','','','Mainstream','publisher','Owner of the Penguin Classics imprint.',A+'Penguin_Classics')
addb('Acoustic Sounds, Inc.','United States','','Specialist','owner','Parent of Analogue Productions.',A+'Analogue_Productions')
for n,c,y in P:
    if y or c: addb(n,c,y.replace('c. ',''),'Specialist','private press','Private press listed by Wikipedia.',A+'Private_press')
json.dump(d,open('/home/user/Possession-Taxonomy/rebuild/work/V4_F1/F1.new.json','w'),ensure_ascii=False,indent=1)
json.dump(br,open('/home/user/Possession-Taxonomy/rebuild/work/V4_F1/F1_brands.new.json','w'),ensure_ascii=False,indent=1)
print('removed cassette',removed_cass,'old presses',old)
