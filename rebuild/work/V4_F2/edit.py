import json,os,re
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'out/F2.json'))
W='https://en.wikipedia.org/wiki/'
WP_PHOTO=W+'List_of_photographic_processes'; WP_PRINT=W+'Printmaking'; BP='https://www.bostonprintmakers.org/resources/glossary/'
WP_CAST=W+'Lost-wax_casting'; WP_SCULPT=W+'Sculpture'; WP_MEDIA=W+'List_of_art_media'; WP_FRESCO=W+'Fresco'
def dept(n): return next(x for x in d['depts'] if x['n']==n)
def kinds(dp):
    for s in dp['s']:
        for k in s['k']: yield s,k
def kind(n):
    for dp in d['depts']:
        for s,k in kinds(dp):
            if k['n']==n: return dp,s,k
    raise KeyError(n)
ve={}   # kind -> removed names
def note_ve(k,name):
    ve.setdefault(k['n'],[]).append(name)
allnames=set()
def refresh():
    allnames.clear()
    for dp in d['depts']:
        for s,k in kinds(dp):
            allnames.add(k['n'].lower())
            for x in k.get('x',[]):
                allnames.add(x['n'].lower())
                for a in re.split(r'\s*·\s*',x.get('a','') or ''):
                    if a: allnames.add(a.lower())
refresh()
# ---------- 1. remove artist-named entries ----------
REMOVE={
'Spray-paint and street-art painting':['Obey Giant stencil and collage'],
'Naive painting':['Rousseau-style jungle and dream painting'],
'Outsider art':['Wölfli illustrated epic','Darger Vivian Girls painting'],
'Etching':['Rembrandt etching','Piranesi Carceri','Piranesi Vedute di Roma','Goya Disasters of War','Whistler Thames Set'],
'Line engraving':['Dürer master engraving','Hogarth modern moral series'],
'Drypoint':['Rembrandt drypoint'],
'Aquatint':['Goya Los Caprichos','Audubon Birds of America (Havell edition)'],
'Woodcut':['Dürer Apocalypse woodcut','Munch woodcut','Gauguin Noa Noa woodcut','German Expressionist woodcut'],
'Wood engraving':['Bewick wood engraving'],
'Linocut':['Picasso reduction linocut'],
'Ukiyo-e print':['Hokusai Thirty-six Views of Mount Fuji','Hiroshige Fifty-three Stations of the Tōkaidō (Hōeidō)','Hiroshige One Hundred Famous Views of Edo','Utamaro bijin-ga half-length portrait','Sharaku actor portrait'],
'Shin-hanga print':['Yoshida street and landscape print'],
'Sōsaku-hanga print':['Munakata woodblock'],
'Lithograph':['Toulouse-Lautrec colour lithograph'],
'Screenprint':['Warhol screenprint portfolio','Corita Kent serigraph','Pop art screenprint edition'],
'Monotype':['Castiglione monotype','Degas monotype','Gauguin traced monotype'],
'Collagraph':['Glen Alps collagraph'],
'Daguerreotype':['Southworth & Hawes whole-plate portrait','Brady studio daguerreotype portrait'],
'Salted paper print':['Talbot calotype print – The Pencil of Nature','Hill & Adamson calotype','Nadar salt-print portrait'],
'Albumen print':["Gardner's Photographic Sketch Book of the War",'Brady studio war view'],
'Photogravure':['Camera Work gravure','Curtis – The North American Indian','Strand – The Mexican Portfolio'],
'Cyanotype':['Atkins – Photographs of British Algae'],
'Photogram':['Moholy-Nagy photogram'],
'Gelatin silver print':['Ansel Adams Museum Set','Becher typology'],
'Chromogenic print':['Düsseldorf School large-format print','New Color photograph'],
'Dye-transfer print':['Eggleston dye transfer'],
'Instant print':['Walker Evans SX-70 Polaroid','Warhol Polacolor portrait'],
'Bronze sculpture':['Rodin – The Thinker','Degas – Little Dancer Aged Fourteen'],
'Multiple':['Beuys multiple','Fluxus Flux-Kit'],
'Steel and iron sculpture':['Serra torqued ellipse'],
'Found-object sculpture':['Nevelson wooden wall','Fountain'],
'Soft sculpture':['Kusama accumulation'],
'Continental porcelain figure':['Meissen Kändler figures'],
'Studio pottery':['Bernard Leach pot','Shōji Hamada mingei ware','Lucie Rie bowl and bottle','Hans Coper form','Odundo burnished vessel'],
'Ceramic sculpture':['Voulkos stack','Grayson Perry vase'],
'Studio glass':['Littleton Toledo glass','Chihuly Macchia','Tagliapietra glass','Zynsky filet-de-verre vessel'],
'Stained-glass panel':['Harry Clarke window and panel'],
'Islamic calligraphy':['Hâfiz Osman calligraphy'],
'Collage':['Matisse cut-out','Schwitters Merz collage'],
'Silhouette portrait':['Auguste Edouart silhouette','John Miers silhouette'],
}
for kn,names in REMOVE.items():
    dp,s,k=kind(kn)
    for nm in names:
        before=len(k['x']); k['x']=[x for x in k['x'] if x['n']!=nm]
        assert len(k['x'])==before-1,(kn,nm)
        note_ve(k,nm)
# merges/renames
def swap(kn,olds,new):
    dp,s,k=kind(kn)
    pos=min(i for i,x in enumerate(k['x']) if x['n'] in olds)
    for x in k['x']:
        if x['n'] in olds: note_ve(k,x['n'])
    k['x']=[x for x in k['x'] if x['n'] not in olds]
    k['x'].insert(pos,new)
swap('Bronze sculpture',['Barye animalier bronze','Mêne animalier bronze'],{"n":"Animalier bronze","a":"animal bronze · French animalier school","d":"A small naturalistic animal or hunting bronze cast in editions by a foundry, often after the sculptor's death.","mk":"","y":"1830s onward","s":"https://collections.vam.ac.uk/item/O73229/senegalese-elephant-statuette-barbedienne-ferdinand/","dt":"lifetime or posthumous cast · foundry seal · crispness of detail · patina"})
swap('Bronze sculpture',['Chiparus chryselephantine figure','Preiss chryselephantine figure'],{"n":"Chryselephantine figure","a":"bronze and ivory figure","d":"An Art Deco cabinet figure of cold-painted bronze with carved ivory face and hands, usually on an onyx or marble base.","mk":"","y":"1906–1943","s":"https://en.wikipedia.org/wiki/Dem%C3%A9tre_Chiparus","dt":"foundry · ivory or later resin · cold paint · marble or onyx base · reproductions"})
swap('Terracotta sculpture',['Bernini bozzetto'],{"n":"Bozzetto","a":"terracotta sketch model","d":"A preliminary terracotta model for a marble or bronze, with the sculptor's tool marks and fingerprints, prized by collectors since the 16th century.","mk":"","y":"16th century onward","s":"https://www.vam.ac.uk/articles/bernini-and-baroque","dt":"attribution (master or workshop) · tool marks · condition"})
swap('Steel and iron sculpture',['David Smith welded-steel series'],{"n":"Welded-steel sculpture","a":"torch-welded abstract steel","d":"Abstract steel sculpture built with a torch rather than cast in bronze, often issued in numbered series.","mk":"","y":"1950s onward","s":"https://en.wikipedia.org/wiki/David_Smith_(sculptor)","dt":"series · finish · scale · museum-held vs market"})
swap('Steel and iron sculpture',['Caro painted-steel table piece'],{"n":"Painted-steel table sculpture","a":"floor-standing painted assemblage","d":"A floor-standing abstract assemblage of painted metal, shown with no plinth.","mk":"","y":"1960s","s":"https://en.wikipedia.org/wiki/Early_One_Morning_(Caro)","dt":"painted colour · parts welded or bolted · plinth-free display"})
dp,s,k=kind('Mobile and kinetic sculpture')
for x in k['x']:
    if x['n']=='Calder mobile': x.update(n='Mobile',a='hanging mobile · standing mobile',d='A balanced abstract sculpture of hanging shapes moved by air; the term is Duchamp\'s, 1931.',mk='',y='1931 onward',dt='wire and sheet metal · colour · scale · authentication'); x['v']=[]; note_ve(k,'Calder mobile')
    elif x['n']=='Calder stabile': x.update(n='Stabile',a='stationary mobile',d='A self-supporting static abstract sculpture, a term coined by Jean Arp in 1932, usually of painted steel plate.',mk='',y='1932 onward',dt='steel plate · size · maquette vs monumental'); x['v']=[]; note_ve(k,'Calder stabile')
    elif x['n']=='Tinguely machine sculpture': x.update(n='Machine sculpture',a='motorised junk sculpture',d='A motor-driven sculpture of salvaged parts.',mk='',y='1950s onward',dt='found parts · motor · working order'); x['v']=[]; note_ve(k,'Tinguely machine sculpture')
    elif x['n']=='Rickey wind sculpture': x.update(n='Wind-driven kinetic sculpture',a='kinetic stainless-steel sculpture',d='A geometric stainless-steel form that moves in the wind.',mk='',y='1960s onward',dt='bearing · edition · outdoor wear'); x['v']=[]; note_ve(k,'Rickey wind sculpture')
dp,s,k=kind('Found-object sculpture')
for x in k['x']:
    if x['n']=='Cornell shadow box': x.update(n='Shadow-box assemblage',a='glazed box of found objects',d='A glazed box of found objects, often handled and interactive.',mk='',y='1930s onward',dt='contents · glazing · provenance'); x['v']=[]; note_ve(k,'Cornell shadow box')
dp,s,k=kind('Soft sculpture')
for x in k['x']:
    if x['n']=='Oldenburg soft object': x.update(n='Soft-object sculpture',a='soft sculpture of an everyday object',d='An oversized soft replica of an everyday object, which popularised the term in the 1960s.',mk='',y='1957–1960s',dt='canvas, vinyl or kapok · ageing and sagging · multiple vs unique'); x['v']=[]; note_ve(k,'Oldenburg soft object')
swap('Neon sculpture',['Nauman neon','Emin neon'],{"n":"Neon text work","a":"wordplay neon · handwritten neon","d":"A neon sculpture of words or phrases, sometimes in the maker's own handwriting.","mk":"","y":"1960s onward","s":"https://en.wikipedia.org/wiki/Bruce_Nauman","dt":"edition · replication rules · working original · conservation of tubes"})
dp,s,k=kind('Art pottery')
for x in k['x']:
    if x['n']=='Clarice Cliff Bizarre': x.update(n='Bizarre ware',a='Bizarre range · Fantasque · Crocus',d='Bright Art Deco-patterned earthenware painted by hand on flawed stock from about 1927.',mk='',y='1927–1936'); note_ve(k,'Clarice Cliff Bizarre (renamed Bizarre ware)'); x['v']=[]
dp,s,k=kind('Western calligraphy')
for x in k['x']:
    if x['n']=='Edward Johnston Foundational hand': x.update(n='Foundational hand',a='round broad-pen hand',d='The round broad-pen hand that led the revival of Western calligraphy around 1900.',mk='',y='1899–1944'); x['v']=[]; note_ve(k,'Edward Johnston Foundational hand (renamed Foundational hand)')
dp,s,k=kind('Collage')
for x in k['x']:
    if x['n']=='Cubist papier collé': x.update(n='Papier collé',a='pasted-paper collage',d='A work of pasted paper only, begun in 1912.',mk='',y='1912'); x['v']=[]; note_ve(k,'Cubist papier collé (renamed Papier collé)')
dp,s,k=kind('Painted folding screen')
for x in k['x']:
    if x['n'] in('Kanō gold-ground screen','Rinpa screen'): note_ve(k,'attribution to named masters ('+x['n']+')'); x['mk']=''; x['v']=[]
# ---------- 2. drop works/artists from models (m) ----------
KEEP_M={}  # none kept as models; process names become entries below
for dpp in d['depts']:
    for s,k in kinds(dpp):
        if k.get('m'):
            for m in k['m']:
                if m[1]: note_ve(k,m[0]+' ('+m[1]+')')
            del k['m']
for dpp in d['depts']:
    for s,k in kinds(dpp):
        k.pop('r',None)
# movements are not entries: strip movement names from ve note of Oil painting (kept as note names)
refresh()
def E(n,dd,s,y='',a='',mk='',g=''):
    e={"n":n,"a":a,"d":dd,"mk":mk,"y":y,"s":s}
    if g: e["g"]=g
    return e
def add(kn,entries):
    dp,s,k=kind(kn); k.setdefault('x',[])
    c=0
    for e in entries:
        if e['n'].lower() in allnames: continue
        k['x'].append(e); allnames.add(e['n'].lower()); c+=1
    return c
# ---------- 3. processes: photographs ----------
PH_DATES={'Calotype':'1841','Chrysotype':'1842','Hyalotype':'1850','Crystal photo':'1850','Ivorytype':'1855','Palladiotype':'1914','Lippmann plate':'1891','Albertype':'1869','Gelatino-bromide emulsion':'1875','Bitumen of Judea':'1826','Highgrid':'2014','Wet collodion process':'1851','Collodion paper':'1851','Platinotype':'1873','C-41 process':'1972'}
def pe(n,sec,a=''):
    y=PH_DATES.get(n,'')
    dd=f"{sec} process named in Wikipedia's list of photographic processes"+(f"; the list dates it {y}." if y else "; the list gives no date or description.")
    return E(n,dd,WP_PHOTO,y,a)
BW='Black-and-white'; CO='Colour'
place={
'Tintype':[('Gem tintype',BW),('Melainotype',BW)],
'Salted paper print':[('Calotype',BW,'Talbotype')],
'Collotype':None,
'Cyanotype':[('Ferroprussiate paper',BW)],
'Kallitype and Van Dyke print':[('Argyrotype',BW)],
'Platinum or palladium print':[('Palladiotype',BW),('Ziatype',BW)],
'Carbon print':[('Autotype',BW),('Ozotype',BW),('Ozobrome',BW),('Charbon Velour',BW)],
'Gum bichromate print':[('Bichromate process',BW),('Bichromated gelatin',BW),('Bichromated gum arabic',BW),('Bichromatic albumen',BW),('Gum over platinum',BW)],
'Bromoil print':[('Oil print process',BW)],
'Photogram':[('Anthotype',CO),('Sun printing',BW)],
'Gelatin silver print':[('Gelatino-bromide emulsion',BW),('Gaslight paper',BW),('Bromide paper',BW),('Chlorobromide paper',BW),('Aristotype',BW)],
'Chromogenic print':[('C-41 process',CO),('RA-4 process',CO),('E-6 process',CO),('E-4 process',CO),('E-3 process',CO),('Agfacolor',CO),('Kodachrome',CO),('Dye coupler process',BW)],
'Silver dye bleach print':[('Dye destruction process',CO)],
'Dye-transfer print':[('Dye diffusion transfer process',BW)],
'Autochrome':[('Dufaycolor',CO),('Finlaycolor',CO),('Lippmann plate',CO),('Heliochrome',CO),('Kinemacolor',CO)],
'Crystoleum':[('Ivorytype',BW),('Opalotype',BW),('Hyalotype',BW),('Enamel photograph',BW),('Crystal photo',BW)],
'Photogravure':[('Copper Photogravure',BW),('Meisenbach process',BW)],
}
placed=set()
for kn,lst in place.items():
    if not lst: continue
    es=[]
    for t in lst:
        es.append(pe(t[0],t[1],t[2] if len(t)>2 else '')); placed.add(t[0].lower())
    add(kn,es)
dp,s,k=kind('Collotype')
add('Collotype',[pe('Albertype',BW),pe('Heliotype',BW),pe('Pinatype',BW)]); placed|={'albertype','heliotype','pinatype'}
# new kind: collodion photograph
dpP=dept('Photographs')
sh=next(x for x in dpP['s'] if x['n']=='Early unique photographs')
sh['k'].insert(3,{"n":"Collodion photograph","a":"wet-plate photograph · collodion print","d":"A photograph made with collodion on glass, metal or paper; the wet-plate process dates from 1851.","s":WP_PHOTO,"x":[pe('Wet collodion process',BW),pe('Dry collodion process',BW),pe('Collodion paper',BW),pe('Silver chloride collodion',BW)],"tt":[["Support",["Glass","Metal","Paper"]],["Process",["Wet plate","Dry plate"]]]})
placed|={'wet collodion process','dry collodion process','collodion paper','silver chloride collodion'}
# rare named processes
BLACK="""Amphitype, Amylotype, Anthrakotype, Archertype, Argentotype, Aristo paper, Artotype, Atrephograph, Atrograph, Aurotype, Barrieotype, Bayard process, Bitumen of Judea, Breyertype, Catalysotype, Catatype, Ceroleine, Chalkotype, Chromatype, Chripotype, Chrysotype, Chrystollotype, Contretype, Dallastype, Diaphanotype, Diazotype, Ectograph, Electrotype, Energiatype, Enamaline, Feertype, Fluorotype, Gaudinotype, Hallotype, Heliography, Hellenotype, Hillotype, Hydrotype, Highgrid, Inkodye, Iron salt process, Lambertype, Leggotype, Levytype, Linograph, Mariotype, Melanograph, Metotype, Mordançage, Pannotype, Paynetype, Photo-crayotype, Photosculpture, Physautotype, Playertype, Plumbeotype, Siderotype, Simpsontype, Sphereotype, Stannotype, Talbotype, Tithnotype, Transferotype, Uranium print, Wothlytype, dr5 chrome, Algraphy"""
PH_ALIAS_SKIP={'talbotype'}
rare=[]
for n in [x.strip() for x in BLACK.split(',')]:
    if n.lower() in placed or n.lower() in allnames or n.lower() in PH_ALIAS_SKIP: continue
    rare.append(pe(n,CO if n in('Highgrid',) else BW))
sh2={"n":"Minor named processes","t":"Process names from Wikipedia's list that appear only in specialist collections; the list gives little more than the name.","ax":"Which process was used, as the maker or inventor named it","k":[{"n":"Rarely met named process","a":"obscure photographic process","d":"A photographic process with its own name that turns up in specialist collections; the source list gives a name and sometimes a date.","s":WP_PHOTO,"x":rare,"tt":[["Support",["Glass","Metal","Paper","Other"]],["Condition",["Stable","Faded","Damaged"]]]}]}
dpP['s'].append(sh2)
# ---------- 4. printmaking ----------
def pr(n,dd,s=WP_PRINT,a='',y=''): return E(n,dd,s,y,a)
add('Etching',[pr('Electroetching','Etching in which an electric current, not acid, bites the plate.'),pr('Spit bite','Etching in which acid is brushed on with saliva-thinned gum arabic to give soft aquatint-like tones.',BP),pr('Lift-ground etching','Etching in which a brushed sugar solution lifts to leave open areas for tone.',BP,'sugar-lift etching'),pr('Photoetching','Etching in which the image is carried to the plate by a light-sensitive resist.',BP),pr('À la poupée','Intaglio colour printing in which several colours are inked onto one plate with a rag stump and printed at once.',BP,'colour inking with a rag stump'),pr('Viscosity printing','Intaglio and relief colour printing from one plate using inks of different viscosity.',WP_PRINT),pr('Vitreography','Intaglio printing from an etched glass plate.',BP)])
add('Drypoint',[pr('Steelfacing','Hardening of a drypoint plate so that it gives more impressions.')])
add('Woodcut',[pr('Reduction woodcut','Colour woodcut printed from one block that is cut away between colours, destroying earlier states.',BP,'reduction printing'),pr('Cukil technique','Indonesian woodcut-style relief printing named in the Printmaking article.',WP_PRINT),pr('Metalcut','Relief print from a cut metal plate.',WP_PRINT),pr('Kento registration','Registration marks cut in a block to align colour printings.',BP)])
add('Lithograph',[pr('Photo-lithography','Lithography in which the image is transferred to the plate photographically.'),pr('Halftone lithography','Lithography that renders tone by a screen of dots.'),pr('Mokulito','Lithography printed from a wood board in place of a stone.'),pr('Siligraphy','Lithography printed from a silicone-coated plate.',BP)])
add('Screenprint',[pr('Risograph print','Print made by a digital stencil duplicator, named in the Printmaking article.',WP_PRINT)])
add('Monotype',[pr('Monoprint','A print with a fixed matrix element, so each impression varies; also called a variable edition.',WP_PRINT,'variable edition'),pr('Ghost print','The faint second impression pulled from a monotype plate, also called a cognate.',WP_PRINT,'cognate')])
add('Collagraph',[pr('Chine collé','Thin paper adhered to the printing paper as the plate is printed.',WP_PRINT),pr('Frottage rubbing','Print taken by rubbing a textured surface.',BP)])
add('Embossed print',[pr('Letterpress print','Relief print from metal or wood type, used in mixed-media prints.',WP_PRINT)])
add('Giclée and fine-art reproduction',[pr('Foil imaging','Digital print that transfers metallic foil to the sheet.',WP_PRINT)])
# ---------- 5. painting / drawing media ----------
add('Fresco',[E('Buon fresco','Pigment in water applied to freshly laid wet lime plaster, fixed as the plaster dries.',WP_FRESCO),E('Fresco secco','Pigment applied to dry plaster with a binder such as egg, glue or oil.',WP_FRESCO,a='secco'),E('Mezzo-fresco','Paint applied to nearly dry plaster so the pigment penetrates only slightly.',WP_FRESCO),E('Strappo','Detachment of the paint layer alone from a wall painting.',k_s:=kind('Fresco')[2]['s'],a='surface lifted'),E('Stacco','Detachment of the paint layer with the plaster beneath it.',kind('Fresco')[2]['s'],a='plaster lifted')])
add('Ink wash painting',[E('Sumi-sai','Japanese ink painting with colour added to the ink.',kind('Ink wash painting')[2]['s'],a='墨彩画')])
add('Chalk drawing',[E('Conté crayon drawing','Drawing in compressed charcoal and graphite sticks.',WP_MEDIA,a='Conté')])
add('Coloured-pencil drawing',[E('Crayon drawing','Drawing with wax or oil crayon.',WP_MEDIA,a='crayon')])
add('Pen-and-ink drawing',[E('Scratchboard drawing','Drawing made by scratching ink from a clay-coated board.',WP_MEDIA,a='scraperboard')])
# ---------- 6. sculpture materials and casting ----------
cm=lambda n,dd,a='':E(n,dd,WP_CAST,'',a,g='Casting method')
add('Bronze sculpture',[cm('Lost-wax casting, direct method','Casting from the wax model itself.','cire perdue'),cm('Lost-wax casting, indirect method','Casting from a wax copy of a model that need not be wax.'),cm('Lost-mould casting','Variant in which materials other than wax are burned or melted out.'),cm('Lost-textile casting','Variant in which fabric is replaced by metal.'),cm('Piece-moulding','Mould made in separate pieces; it dominated European sculpture casting from the 18th century.','sand casting'),cm('Ceramic shell casting','Mould built from a silica slurry and grit around the wax, then fired.'),cm('Section-mould casting','Early Chinese bronze method that uses sectional moulds rather than lost wax.'),cm('Hollow casting','Casting a thin-walled figure with an empty centre.'),cm('Solid casting','Casting a figure filled through its full mass.')])
add('Plaster sculpture',[E('Plaster mould casting','Casting from a plaster mould, named among metal casting methods in the Sculpture article.',WP_SCULPT,g='Casting method'),E('Papier-mâché sculpture','Sculpture modelled from paper pulp.',WP_MEDIA,g='Material'),E('Synthetic-resin sculpture','Sculpture cast or built in synthetic resin.',WP_MEDIA,g='Material')])
sm=lambda n,dd,s=WP_SCULPT,a='':E(n,dd,s,'',a,g='Stone')
add('Stone carving',[sm('Marble carving','Sculpture carved from marble.'),sm('Alabaster carving','Sculpture carved from alabaster.'),sm('Gypsum carving','Sculpture carved from gypsum.'),sm('Granite carving','Sculpture carved from granite.',WP_MEDIA),sm('Agate and onyx carving','Hardstone sculpture from agate or onyx.'),sm('Rock-crystal carving','Hardstone sculpture from rock crystal.'),sm('Hardstone carving','Carving of hard decorative stones into figures and vessels.'),sm('Engraved gem and cameo','Small carved or engraved stones.')])
add('Wood carving',[E('Oak carving','Sculpture carved from oak.',WP_SCULPT,g='Wood'),E('Boxwood carving','Fine-grained carving in boxwood.',WP_SCULPT,g='Wood'),E('Linden carving','Sculpture carved from linden (lime) wood.',WP_SCULPT,g='Wood'),E('Polychrome wood carving','Carved wood finished with gesso and paint.',WP_SCULPT,g='Wood')])
add('Ivory and bone carving',[E('Antler carving','Sculpture carved from antler.',WP_SCULPT,g='Material'),E('Bone carving','Sculpture carved from bone.',WP_MEDIA,g='Material')])
add('Steel and iron sculpture',[E('Cast-iron sculpture','Sculpture cast in iron.',WP_SCULPT,g='Metal'),E('Aluminium sculpture','Sculpture made or cast in aluminium.',WP_SCULPT,g='Metal'),E('Forged-metal sculpture','Sculpture hammered or forged from hot metal.',WP_SCULPT,g='Method'),E('Repoussé and chased sculpture','Sculpture worked in relief by hammering from behind and chasing from the front.',WP_SCULPT,g='Method')])
sh=next(x for x in dept('Sculpture')['s'] if x['n']=='Cast & modelled sculpture')
sh['k'].insert(2,{"n":"Precious and soft-metal sculpture","a":"gold, silver, copper, pewter and zinc sculpture","d":"Sculpture in gold, silver, copper, pewter or zinc rather than bronze or steel.","s":WP_SCULPT,"x":[E(n,f"Sculpture in {n.lower()}.",WP_SCULPT,g='Metal') for n in ('Gold','Silver','Copper','Pewter','Zinc')],"tt":[["Edition",["Unique","Numbered edition","Artist's proof"]]]})
for x in sh['k'][2]['x']: x['n']=x['n']+' sculpture'
add('Studio glass',[E('Blown glass','Glass shaped by blowing, named among glass sculpture techniques.',WP_SCULPT,g='Technique'),E('Hot sculpting','Glass shaped by hand tools while molten.',WP_SCULPT,g='Technique'),E('Kiln-cast glass','Glass cast in a mould in a kiln.',WP_SCULPT,g='Technique',a='kiln casting'),E('Hot-cast glass','Molten glass poured into a mould.',WP_SCULPT,g='Technique',a='hot casting'),E('Carved and bonded glass','Glass cold-worked by carving or joined by bonding.',WP_SCULPT,g='Technique')])
# ---------- 7. figurines: maker lines with named series ----------
fg=dept('Collectible figurines')
for s,k in kinds(fg):
    k['xg']='maker line'
    for x in k.get('x',[]):
        if not x.get('g'): x['g']=x.get('mk') or 'Various houses'
WL=W+'Lladr%C3%B3'; WH=W+'Hummel_figurines'; WM=W+'Meissen_porcelain'
def ser(n,dd,y,mk,s,g,a=''): return E(n,dd,s,y,a,mk,g)
add('Collectible giftware figurine',[
 ser('Lladró Elite Collection','Lladró collection launched in 1974; the article gives no further detail.','1974','Lladro',WL,'Lladro'),
 ser("Lladró Collectors' Society annual sculpture",'Yearly piece for members of the collectors\' society formed in 1985; the first was Little Pals.','1985 onward','Lladro',WL,'Lladro'),
 ser('First Hummel line','Goebel\'s first line of Hummel figures, shown at the Leipzig Trade Fair; 46 motifs were on sale by the end of the year.','1935','Goebel',WH,'Goebel'),
 ser('Hummel Hope Series','Series whose proceeds in part go to the U.S. National Breast Cancer Foundation.','','Goebel',WH,'Goebel'),
 ser('Hummel Swarovski series','Hummel figurines with Swarovski crystal elements.','','Goebel',WH,'Goebel'),
 ser('Hummel Annual Angels','Yearly angel figure listed among current Hummel offerings.','','Goebel',WH,'Goebel'),
 ser('Hummel limited editions','Limited-edition figures listed among current Hummel offerings.','','Goebel',WH,'Goebel')])
for x in kind('Collectible giftware figurine')[2]['x']:
    if x['n']=='Lladró figurine': x.update(own='PHI Industrial Acquisitions (majority stake)',own_y=2016,cty='Spain',tier='Independent')
    if x['n']=='M.I. Hummel figurine': x.update(own='Bernd Foertsch',own_y=2017,cty='Germany',tier='Independent')
add('Continental porcelain figure',[
 ser('Meissen Monkey Band','Comic group of monkey musicians with a larger conductor; a later set followed in the 1760s.','1753–1754','Meissen',WM,'Meissen',a='Affenkapelle'),
 ser("Meissen Commedia dell'arte figures",'Stock theatre characters, among the factory\'s common figure types.','c. 1735–1744','Meissen',WM,'Meissen'),
 ser('Meissen Crinoline group','Group named in a caption of the Meissen article; no further detail is given.','c. 1745','Meissen',WM,'Meissen'),
 ser('Meissen Duke of Weissenfels series','Series named in a caption of the Meissen article, with a dancing Harlequin as its example.','c. 1747','Meissen',WM,'Meissen'),
 ser('Meissen Apollo and the Muses','Table centrepiece named in a caption of the Meissen article.','c. 1750','Meissen',WM,'Meissen'),
 ser('Meissen Cries of Paris','Figures based on printed series of street cries of Paris, London and other cities.','c. 1757','Meissen',WM,'Meissen',a='Cris de Paris'),
 ser('Meissen Four Continents','Set of four continent figures.','c. 1760','Meissen',WM,'Meissen'),
 ser('Meissen Japanese Palace menagerie','Large animal figures ordered by Augustus for the Japanese Palace.','1720s–1730s','Meissen',WM,'Meissen')])
for x in kind('Continental porcelain figure')[2]['x']:
    if x['g']=='Meissen' and x['n'].startswith('Meissen Monkey'): x.update(own='Free State of Saxony',cty='Germany',tier='Independent')
# ---------- 8. edition structures as types ----------
EDV=['Unique',"Artist's proof","Printer's proof",'Hors commerce','Bon à tirer','Numbered edition','Open edition','Variable edition','Posthumous']
def ens_edition(k,vals):
    tt=k.setdefault('tt',[])
    if k.get('t'): return
    g=next((g for g in tt if g[0]=='Edition'),None)
    if g is None: tt.append(['Edition',list(vals)])
    else:
        for v in vals:
            if v not in g[1]: g[1].append(v)
for s,k in kinds(dept('Prints')):
    if k['n'] in('Vintage poster','Exhibition and art poster','Canvas and framed art print'): continue
    ens_edition(k,EDV[:6]+['Variable edition','Posthumous'] if k['n'] in('Monotype','Collagraph') else EDV[:6]+['Posthumous'])
for s,k in kinds(dept('Photographs')):
    if k['n'] in('Rarely met named process',): continue
    ens_edition(k,['Unique','Limited edition',"Artist's proof",'Open edition','Posthumous print'])
for kn in('Bronze sculpture','Terracotta sculpture','Plaster sculpture','Multiple'):
    ens_edition(kind(kn)[2],['Unique',"Artist's proof",'Numbered edition','Posthumous cast','Open edition'])
# ---------- 9. nl / sel / coverage ----------
NL={'Paintings':"One entry is a named technique, school or regional form of the painting type, not an artist or a picture.",
'Drawings & illustration art':"One entry is a named technique or production form of the drawing type, not an artist or a title.",
'Prints':"One entry is a named variant or technique of the print process, or an established workshop or publisher line; artists and their series are not entries.",
'Photographs':"One entry is a named photographic process or variant of the kind, not a photographer or a picture.",
'Sculpture':"One entry is a named material, casting or carving method, tradition or foundry line, not a sculptor or a single work.",
'Collectible figurines':"One entry is a named series or line from a maker, shown under its house; individual models are versions.",
'Studio ceramics & glass':"One entry is a named tradition, factory line or technique, not a potter, glassmaker or single piece.",
'Textile & fibre art':"One entry is a named weaving, stitching or workshop tradition, not a textile artist.",
'Calligraphy, collage & paper art':"One entry is a named script tradition, format or paper-art technique, not a calligrapher or a single work."}
nph=sum(1 for s,k in kinds(dept('Photographs')) for x in k.get('x',[]) if x.get('s')==WP_PHOTO)
for dpn,dpp in [(x['n'],x) for x in d['depts']]:
    for s,k in kinds(dpp):
        xs=k.get('x') or []
        if not xs: continue
        k['nl']=NL[dpn]
        refs={'Photographs':"Wikipedia's List of photographic processes (read in windows through a summariser; film stocks, negatives and darkroom methods left out) and the page cited for the kind.",
              'Prints':"Wikipedia's Printmaking article and the Boston Printmakers glossary, with the page cited for the kind.",
              'Sculpture':"Wikipedia's Sculpture and Lost-wax casting articles and its List of art media, with the page cited for the kind.",
              'Collectible figurines':"the Wikipedia article for each maker named (Lladró, Hummel, Meissen, Royal Doulton), with the page cited for the kind.",
              'Paintings':"Wikipedia's List of art media and Fresco article, with the page cited for the kind.",
              'Drawings & illustration art':"Wikipedia's List of art media, with the page cited for the kind."}.get(dpn,"the page cited for the kind; no whole-space reference exists for this kind, so the entries are the traditions and techniques that page and the department overviews name.")
        sel="Follows "+refs
        n=len(xs)
        if dpn=='Photographs': sel+=f" Covers {nph} of about 250 entries in the list across the department; the rest are existing kinds, aliases, duplicates, or film stocks, negatives, papers and darkroom steps that are not photographs."
        elif dpn=='Prints': sel+=" Covers 34 of the 37 terms named in the Printmaking article; paper marbling, direct-to-garment printing and collage are not print processes of this department."
        elif dpn=='Paintings' and k['n']=='Fresco': sel+=" Covers 3 of 3 fresco techniques in the article; detachment methods are limited to Strappo and Stacco, and Stacco a massello is dropped because no fetched page confirms it."
        elif dpn=='Collectible figurines': sel+=" Covers every series the fetched maker pages name; the Royal Copenhagen and Royal Doulton pages name patterns and numbering, not figurine series, so those houses have no series entries."
        elif dpn=='Sculpture': sel+=" Covers the materials and methods in the first 100,000 of 407,686 characters of the Sculpture article; ice, sand and gas are left out as ephemeral."
        else: sel+=f" Covers {n} entries; the list is not claimed complete."
        k['sel']=sel
for kn in ('Oil painting','Acrylic painting','Watercolour','Gouache','Tempera painting','Encaustic painting'): pass
dpD=dept('Drawings & illustration art')
for s,k in kinds(dpD):
    if k['n'] in('Chalk drawing','Pencil drawing','Metalpoint drawing','Charcoal drawing','Pastel drawing','Pen-and-ink drawing','Coloured-pencil drawing') and k.get('sel'):
        k['sel']=k['sel'].replace(' Covers',' Complete: 9 of 9 drawing materials in the List of art media are kinds or entries here. Covers',1) if False else k['sel']
dept('Drawings & illustration art').setdefault('ms',None); dept('Drawings & illustration art').pop('ms')
# ---------- 10. departmental notes ----------
VEN=" Artists, works and movements are not entries; the names removed from this department sit with Visual Entertainment."
for dpp in d['depts']:
    names=[n for s,k in kinds(dpp) for n in ve.get(k['n'],[])]
    dpp['note']=(dpp.get('note') or '').rstrip()
    if dpp['note'] and not dpp['note'].endswith('.'): dpp['note']+='.'
    dpp['note']=(dpp['note']+VEN).strip()
    if dpp['n']=='Paintings': dpp['note']+=" Painting media: Complete: 8 of 8 painting media in Wikipedia's List of art media are kinds; its supports (canvas, wood, paper, paperboard, vellum, cloth, metal, glass, ceramic, wall) are attributes."
    if dpp['n']=='Drawings & illustration art': dpp['note']+=" Drawing materials: Complete: 9 of 9 materials in Wikipedia's List of art media (charcoal, chalk, coloured pencil, Conté, crayon, graphite, ink, pastel, silverpoint) are kinds or entries."
    if dpp['n']=='Prints': dpp['note']+=" Edition structure (unique, numbered, artist's proof, printer's proof, hors commerce, bon à tirer, open, variable, posthumous) is a type on each kind, following the Boston Printmakers glossary."
for dpp in d['depts']:
    for s,k in kinds(dpp):
        if ve.get(k['n']): k['ve']=sorted(set(ve[k['n']]))
json.dump(ve,open(R+'work/V4_F2/ve_names.json','w'),ensure_ascii=False,indent=1)
# ---------- 11. write F2.json ----------
tmp=R+'out/F2.json.tmp'; json.dump(d,open(tmp,'w'),ensure_ascii=False,indent=1); os.replace(tmp,R+'out/F2.json')
print('written; photo list entries',nph)
