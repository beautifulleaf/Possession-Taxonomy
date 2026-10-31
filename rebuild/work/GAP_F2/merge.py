import json,os,re,sys
sys.path.insert(0,'.')
exec(open('adds.py').read())
SRC='/home/user/Possession-Taxonomy/rebuild/out/F2.json'
d=json.load(open(SRC))
W='https://en.wikipedia.org/wiki/'
REST_OVR={
 'Western calligraphy':"Merovingian script, Humanist minuscule, Antiqua and Textura are named without description and are not entries; the page was read in full",
 'East Asian calligraphy':"the article was read to its end; oracle bone script and bronze inscriptions are historical scripts, not display styles, and scroll formats are not on the page",
 'Islamic calligraphy':"the article was read to its end; Pseudo-Kufic is an influence, not a style",
 'Tapestry':"the page was read to its end; rugs and flatweaves (Kilim, Navajo, Ryijy), studios without a distinct product, institutions and restoration workshops are not tapestry kinds",
 'Persian and Indian miniature painting':"the page was read to its end; individual manuscripts are works, not kinds, and Ottoman, Arabic and Mughal miniature are named without description. The Indian schools follow earlier fetched pages",
 'Aboriginal Australian painting':"the article was read to its end; art centres and peak bodies are institutions, not kinds",
 'Art quilt':"the page was read to its end; bed-quilt traditions without wall display (Ralli, Godadi, Razai, Kawandi), techniques (patchwork, trapunto, sashiko, kantha) and named modern works are not entries",
 'Plaster sculpture':"the article was read to character 400,000 of 407,686 (the rest is references); ephemeral media (ice, snow, butter, gas, light, sound) and environmental works are not owned objects",
}
for k_ in ('Bronze sculpture','Stone carving','Terracotta sculpture','Ivory and bone carving','Jade carving'):
    REST_OVR[k_]="the article was read to character 400,000 of 407,686 (the rest is references); monuments, architecture and ephemeral media are not owned objects"
OVR_ENTRY={
 'Merry Wanderer':('https://en.wikipedia.org/wiki/Hummel_figurines','Goebel','Goebel'),
 'Little Pals':(W+'Lladr%C3%B3','Lladro','Lladro'),
 'Guitar Girl':(W+'Lladr%C3%B3','Lladro','Lladro'),
 'Fisherboy 4809':(W+'Lladr%C3%B3','Lladro','Lladro'),
}
def all_names(k):
    s=set()
    for e in k.get('x',[]):
        s.add(e['n'].lower())
        for z in (e.get('a') or '').split(' · '): 
            if z: s.add(z.lower())
    return s
log=[]
def find_kind(n):
    for dep in d['depts']:
        for sh in dep['s']:
            for k in sh['k']:
                if k['n']==n: return k
def stats_sel(k):
    sel=k.get('sel','')
    for cut in (' Covers ','. Covers'):
        i=sel.find(cut)
        if i>0: sel=sel[:i]; break
    sel=sel.rstrip()
    if sel and not sel.endswith('.'): sel+='.'
    return sel
OVR_SEL={}
for kn,v in A.items():
    if v is None: continue
    k=find_kind(kn)
    if k is None: print('missing kind',kn); continue
    slug,label,m,rest,adds=v
    have=all_names(k); xs=k.setdefault('x',[])
    added=0
    for (n,y,desc,alias) in adds:
        if n.lower() in have or (alias and alias.lower() in have): continue
        s=W+slug
        mk=''; g=None
        if n in OVR_ENTRY: s,mk,g=OVR_ENTRY[n]
        e={'n':n,'a':alias,'d':desc,'mk':mk,'y':y,'s':s}
        if k.get('xg'): e['g']=g or 'Various houses'
        xs.append(e); have.add(n.lower()); added+=1
    log.append((kn,added))
    n_ref=sum(1 for e in xs if slug.split('%')[0] in e.get('s','').replace('%C3%AF','') or slug in e.get('s',''))
    mm=max(m,n_ref)
    rest=REST_OVR.get(kn,rest)
    if mm==n_ref: cov=f"Complete: {n_ref} of {n_ref} in {label}; {rest}."
    else: cov=f"Covers {n_ref} of about {mm} in {label}; {rest}."
    OVR_SEL[kn]=cov
# xg for Rarely met and Bronze
k=find_kind('Rarely met named process')
iron={'Chrysotype','Aurotype','Siderotype','Iron salt process','Uranium print','Argentotype','Catalysotype','Catatype'}
mech={'Heliography','Bitumen of Judea','Electrotype','Photosculpture','Linograph','Stannotype','Algraphy','Photolithography','Wash-off relief','Pinatype','Photolithography','Levytype','Photo-crayotype'}
for e in k['x']:
    e['g']='Metal-salt processes' if e['n'] in iron else 'Relief and photomechanical processes' if e['n'] in mech else 'Named in the list only'
k['xg']='process family (grouping added for browsing; the list gives none)'
k=find_kind('Bronze sculpture')
meth={'Lost-wax casting, direct method','Lost-wax casting, indirect method','Lost-mould casting','Lost-textile casting','Piece-moulding','Ceramic shell casting','Section-mould casting','Hollow casting','Solid casting'}
for e in k['x']: e['g']='Casting method' if e['n'] in meth else 'Form or tradition'
k['xg']='casting method or form'
# coverage lines everywhere
MED="No complete list exists; follows Wikipedia's List of art media (all 8 painting media are kinds here) and the page cited for the kind."
DEF={
 0:MED,
 1:"No complete list exists; follows Wikipedia's List of art media (all 9 drawing materials are kinds here) and the page cited for the kind.",
 2:"Complete for this kind: every term of Wikipedia's Printmaking article and the Boston Printmakers glossary that belongs to it is an entry (34 of 37 terms across the department; paper marbling, direct-to-garment printing and collage are not print processes).",
 3:"Complete for this kind against Wikipedia's List of photographic processes, which was read to its end (both windows, to Ziatype); the 123 process entries across the department are spread over the kinds and Rarely met named process, and the rest of the list is aliases, film stocks, negatives, papers and darkroom steps.",
 4:"No complete list exists; follows Wikipedia's Sculpture article (read to character 400,000 of 407,686; the rest is references) and the page cited for the kind.",
 5:"No complete list exists; follows the fetched maker pages (Lladró, Hummel, Meissen, Staffordshire, Royal Doulton); the Royal Copenhagen and Royal Doulton pages name patterns and numbering, not figurine series, so those houses have no series entries.",
 6:"No complete list exists for studio pottery, art glass or stained glass as a whole; follows the Wikipedia articles cited for each kind and the department overviews.",
 7:"No complete list exists; follows the Wikipedia articles on tapestry, samplers, quilts and fibre art and the department overviews.",
 8:"No complete list exists; follows the Wikipedia articles cited for each kind and the department overviews.",
}
tot=0
for di,dep in enumerate(d['depts']):
    for sh in dep['s']:
        for k in sh['k']:
            if not k.get('x'): continue
            base=stats_sel(k)
            if k['n']=='Fresco':
                cov="Complete: 5 of 5 techniques and detachment methods in the Fresco article (Stacco a massello is omitted: no fetched page confirms it)."
            elif k['n']=='Indian folk painting':
                cov="No complete list exists; follows Wikipedia's Madhubani art article and the pages cited for each tradition (Warli, Gond, Kalighat, Pattachitra); other Indian folk styles (Kalamkari, Phad, Pichwai, Cheriyal) are not on a fetched page."
            elif k['n'] in OVR_SEL: cov=OVR_SEL[k['n']]
            elif k['n'] in ('Collage',):
                cov="No complete list exists; follows Wikipedia's Papier collé article and the department overviews."
            elif k['n']=='Studio pottery' and 'Studio pottery' in OVR_SEL: cov=OVR_SEL['Studio pottery']
            else: cov=DEF[di]
            k['sel']=(base+' '+cov).strip()
            tot+=1
print(log, tot)
tmp=SRC+'.tmp'
json.dump(d,open(tmp,'w'),ensure_ascii=False,indent=1)
os.replace(tmp,SRC)
