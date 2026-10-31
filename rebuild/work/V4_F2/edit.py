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
                if m[1] and m[0] not in('Strappo','Stacco','Stacco a massello'): pass
                note_ve(k,m[0]+(' ('+m[1]+')' if m[1] else '')) if (m[1] or m[0] not in ('Strappo','Stacco','Stacco a massello','sumi-sai (墨彩画)','Macchiaioli')) else None
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
