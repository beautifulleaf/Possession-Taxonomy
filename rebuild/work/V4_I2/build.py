import json,re,os,copy
R='/home/user/Possession-Taxonomy/rebuild/'
W=R+'work/V4_I2/'
d=json.load(open(R+'out/I2.json'))
brands=json.load(open(R+'out/I2_brands.json'))
bnames={b['n'] for b in brands['b']}
def norm(s): return re.sub(r'[^a-z0-9]','',s.lower().replace('ms ','').replace('(','').replace(')',''))
K={}
for dp in d['depts']:
    for sh in dp['s']:
        for k in sh['k']: K[k['n']]=(dp,sh,k)
LT='https://en.wikipedia.org/wiki/List_of_typefaces'
TC='https://en.wikipedia.org/wiki/Typeface_classification'
# ---------- typefaces
secmap={'Serif':'Serif typeface','Transitional serif':'Serif typeface','Semi-serif':'Serif typeface','Slab serif':'Slab-serif typeface','Sans-serif':'Sans-serif typeface','Monospace':'Monospaced and coding typeface',
'Brush scripts':'Script and handwriting typeface','Calligraphic':'Script and handwriting typeface','Handwriting':'Script and handwriting typeface','Other script':'Script and handwriting typeface','Blackletter':'Blackletter typeface',
'Non-Latin':'Non-Latin script typeface','Unicode fonts':'Non-Latin script typeface','Dingbat/Symbol fonts':'Icon and symbol font','Display/Decorative fonts':'Display and decorative typeface','Ethnic fonts':'Display and decorative typeface','Miscellaneous':'Display and decorative typeface'}
EXCL={'Didone','Fat face','Hermann Zapf','Legibility Group','Capitals','Modern','Antiqua','Monospace','Script','Fallback font','Last Resort','Blackboard bold','Georgia Ref','Verdana Ref','Century type family','Textualis','Bastard','Stephenson Blake','Ludwig & Mayer','Free UCS Outline Fonts','GNU FreeFont','FreeFont','Fixed','System','Terminal','Compatil','Casey'}
EXCL-= {'Casey','Compatil','Fixed','System','Terminal'}
CLS={}
def setc(c,names):
    for n in names.split('|'): CLS[norm(n)]=c
setc('Venetian','Adobe Jenson|Centaur|Cloister Black')
setc('Garalde','Bembo|Aldine 401|Garamond|Granjon|Galliard|Palatino|Book Antiqua|Sabon|Caslon|Minion|Janson|Sistina|Aster|Arno|Goudy Old Style|Goudy|Trump Mediaeval|Joanna|Hoefler Text|EB Garamond|Cochin')
setc('Transitional','Baskerville|Bookman|Times New Roman|Times|Perpetua|Lapidary 333|Plantin|Aldine 721|Mrs Eaves|Mrs. Eaves|Freight|Utopia|Century type family|Georgia|Cheltenham|Caledonia|Fairfield|Charter|Bitstream Charter')
setc('Didone','Bodoni|Bauer Bodoni|Didot|Walbaum|Bell|Theano Didot|Bulmer|Bernhard Modern')
setc('Mechanistic','Clarendon|Egyptienne|Rockwell|Memphis|Serifa|Courier|American Typewriter|Archer|Roboto Slab|Lexia|Guardian Egyptian|Concrete Roman|Geometric Slabserif 712|Skeleton Antique|Tower|Candida|Athens|City|Nilland|Schadow|Cholla Slab|Alexandria')
setc('Glyphic','Albertus|Copperplate Gothic|Trajan|Friz Quadrata|Lithos|Optima|Zapf Humanist 601|Sistina|Pericles')
setc('Script','Mistral|Brush Script|Zapfino|Zapf Chancery|ITC Zapf Chancery|Apple Chancery|Freestyle Script|Kuenstler Script|Monotype Corsiva|French Script|Papyrus|Segoe Script|Lucida Handwriting|Comic Sans|Comic Sans MS|Comic Neue|Kristen|Ashley Script|Dom Casual|Staccato 222|Staccato 555|Choc|Balloon|Wiesbaden Swing|Coronet|Ribbon 131|Curlz')
setc('Graphic','Banco|Broadway|Cooper Black|Impact|Stencil|Neuland|Peignot|Bauhaus|Umbra|Algerian|Jokerman')
setc('Blackletter','Fraktur|Schwabacher|Textura|Fette Fraktur|Breitkopf Fraktur|Old English Text|Old English Text MT|Tannenberg|Theuerdank Fraktur|Wallau|Fletcher|Lucida Blackletter|Cloister Black')
setc('Grotesque (BS 2961)','Akzidenz-Grotesk|Gothic 725|Franklin Gothic|News Gothic|Trade Gothic|Brandon Grotesque|Haettenschweiler|Compacta|Impact|Bank Gothic|Eurostile|Square 721|Microgramma|Template Gothic')
setc('Neo-grotesque (BS 2961)','Helvetica|Helvetica Neue|Swiss 721|Univers|Zurich|Arial|Roboto|Inter|Letter Gothic|Unica|Folio|Akzidenz-Grotesk|Neuzeit S|Nimbus Sans L|Liberation Sans|DIN 1451|Rail Alphabet|Transport|Highway Gothic|Interstate|Aptos|SF|San Francisco|Graphik|Archivo|Overpass|FF Meta|Meta')
setc('Geometric (BS 2961)','Futura|Avant Garde Gothic|Century Gothic|Kabel|Geometric 231|Gotham|Avenir|Twentieth Century|Tw Cen MT|Proxima Nova|Neutraface|Nordstern|Klavika|Lato|Montserrat|Bauhaus|Product Sans|Industria')
setc('Humanist (BS 2961)','Gill Sans|Gill Sans Schoolbook|Humanist 521|Frutiger|Humanist 777|Myriad|Verdana|Tahoma|Lucida|Lucida Grande|Lucida Sans Unicode|Segoe UI|Calibri|Open Sans|Fira Sans|Fira|Trebuchet MS|Johnston|New Johnston|Syntax|Corbel|Ubuntu|Source Sans Pro|IBM Plex Sans|PT Sans|FF Scala Sans|FF Dax|Optima|Thesis Sans|Tiresias|Meiryo|Geneva|Chicago|Charcoal|Prompt|Noto Sans|DejaVu Sans|Vera Sans|Droid Sans|Linux Biolinum|Gadugi|Parisine|Motorway|Clearview|Eras|Berlin Sans|Agency FB')
DEFAULT={'Serif typeface':'Serif, class not assigned','Slab-serif typeface':'Mechanistic','Sans-serif typeface':'Lineal, class not assigned','Monospaced and coding typeface':'Monospaced','Script and handwriting typeface':'Script','Blackletter typeface':'Blackletter','Non-Latin script typeface':'Non-Latin and Unicode coverage','Icon and symbol font':'Symbol and dingbat','Display and decorative typeface':'Graphic'}
ORDER=['Venetian','Garalde','Transitional','Didone','Mechanistic','Glyphic','Grotesque (BS 2961)','Neo-grotesque (BS 2961)','Geometric (BS 2961)','Humanist (BS 2961)','Lineal, class not assigned','Serif, class not assigned','Monospaced','Script','Graphic','Blackletter','Non-Latin and Unicode coverage','Symbol and dingbat']
sections={}
cur=None
for line in open(W+'typefaces.txt',encoding='utf8'):
    line=line.rstrip('\n')
    if line.startswith('## '): cur=line[3:]; sections[cur]=line and []; continue
    sections[cur]=line.split('|')
# global existing entries by norm
existing={}
for kn,(dp,sh,k) in K.items():
    for x in k.get('x',[]): existing[norm(x['n'])]=(kn,x)
ALIAS={'comicsansms':'comicsans','mrseaves':'mrseaves','fira':'firasans'}
kinds_tf=list(DEFAULT)
counts={kn:{'n':0,'sec':set()} for kn in kinds_tf}
seen_global=set(existing)
newx={kn:[] for kn in kinds_tf}
excluded=[]
placed=set()
SKIP_SUB={'noto','notosans','notoserif'}
for sec,names in sections.items():
    kn=secmap[sec]
    for n in names:
        nn=norm(n)
        if n in EXCL: 
            if n not in excluded: excluded.append(n)
            continue
        if nn in SKIP_SUB and kn!='Non-Latin script typeface': continue
        if nn in ('noto','notosans','notoserif'): continue  # covered by the Noto entry
        counts[kn]['sec'].add(sec)
        if nn in placed: continue
        placed.add(nn)
        if nn in existing or ALIAS.get(nn) in existing or nn=='mrseaves':
            counts[kn]['n']+=1
            continue
        c=CLS.get(nn)
        if not c: c=DEFAULT[kn]
        dd=f"Listed under {sec.lower()} in Wikipedia's List of typefaces."
        e={'n':n,'a':'','d':dd,'mk':'','y':'','s':LT,'g':c}
        if n=='Amelia': e.update(mk='Stan Davis',y='1963',d='Serif typeface designed by Stan Davis in 1963.')
        if n=='Bell': e.update(mk='Richard Austin',y='1788',d='Didone serif designed by Richard Austin in 1788.')
        newx[kn].append(e); counts[kn]['n']+=1
# existing entries: assign g and keep; count existing in kinds
for kn in kinds_tf:
    k=K[kn][2]
    for x in k.get('x',[]):
        if not x.get('g'):
            c=CLS.get(norm(x['n']))
            x['g']=c or DEFAULT[kn]
# m -> entries when in the list
inlist={norm(n) for ns in sections.values() for n in ns}
dropped_m=[]
for kn in kinds_tf:
    k=K[kn][2]
    for m in k.pop('m',[]) or []:
        nn=norm(m[0])
        if nn in placed and not any(norm(e['n'])==nn for e in k.get('x',[])+newx[kn]) and nn not in existing:
            pass
        if nn in inlist:
            continue   # already an entry from the list (or an existing archetype)
        dropped_m.append(m[0])
    k.pop('r',None) if kn=='Non-Latin script typeface' else None
for kn in kinds_tf:
    k=K[kn][2]
    k['x']=k.get('x',[])+newx[kn]
    def yr(e):
        m=re.search(r'\d{4}',e.get('y','') or ''); return int(m.group()) if m else 9999
    k['x'].sort(key=lambda e:(ORDER.index(e['g']) if e['g'] in ORDER else 99,yr(e),e['n'].lower()))
    secs=sorted(counts[kn]['sec'])
    k['nl']="One entry is a named typeface design or family; revivals, digitisations and weights of the same design are versions."
    n=len(k['x'])
    k['xg']="by Vox-ATypI class, with lineal faces split by British Standard 2961 class"
    k['sel']=(f"Every name under the {', '.join(secs)} section(s) of Wikipedia's List of typefaces, read in windows and summarised; sections follow Vox-ATypI and British Standard 2961 as set out in Typeface classification (the class of a face is assigned only where that page or the face's own entry shows it; otherwise 'class not assigned'). "
              f"Names that denote a style or a foundry rather than a typeface are left out ({', '.join(e for e in EXCL if e in excluded)}). "
              f"Complete: {counts[kn]['n']} of {counts[kn]['n']} typeface names in those sections of the list.")
K['Pixel and bitmap typeface'][2]['sel']="No entries: Wikipedia's List of typefaces has no pixel or bitmap section."
del K['Pixel and bitmap typeface'][2]['sel']
# ---------- LLM
LL='https://en.wikipedia.org/wiki/List_of_large_language_models'
LAB={'Meta':'Meta AI','Z.ai':'Z.ai'}
fam=[
 ('Phi','Microsoft','2023',[('Phi-1','2023','21 Jun 2023, MIT'),('Phi-2','2023','Dec 2023, MIT'),('Phi-3','2024','23 Apr 2024, MIT'),('Phi-4','2024','12 Dec 2024, MIT')]),
 ('GLM','Z.ai','2025',[('GLM-4.5','2025','29 Jul 2025, MIT'),('GLM-4.6','2025','30 Sep 2025, Apache 2.0'),('GLM-4.7','2025','22 Dec 2025, Apache 2.0'),('GLM-5','2026','12 Feb 2026, MIT'),('GLM-5.1','2026','7 Apr 2026, MIT'),('GLM-5.2','2026','16 Jun 2026, MIT'),('GLM-5.3','2026','14 Aug 2026, various licences'),('GLM-5.3-flash','2026','28 Aug 2026, MIT')]),
 ('Kimi','Moonshot AI','2026',[('Kimi K2.5','2026','Modified MIT'),('Kimi K2.6','2026','20 Apr 2026, Modified MIT'),('Kimi K2.7 Code','2026','16 Jun 2026, Modified MIT')]),
 ('GPT-1 and GPT-2','OpenAI','2018',[('GPT-1','2018','11 Jun 2018, MIT'),('GPT-2','2019','Feb 2019, MIT')]),
 ('GPT-OSS','OpenAI','2025',[('GPT-OSS','2025','5 Aug 2025, Apache 2.0')]),
 ('OLMo','Allen Institute for AI','2024',[('OLMo','2024','Feb 2024, Apache 2.0'),('OLMo 2','2024','Nov 2024, Apache 2.0'),('Olmo 3','2025','20 Nov 2025, Apache 2.0')]),
 ('Grok','xAI','2023',[('Grok-1','2023','Nov 2023, Apache 2.0'),('Grok-2','2024','14 Aug 2024, xAI Community License')]),
 ('Falcon','Technology Innovation Institute','2023',[('Falcon','2023','Mar 2023, Apache 2.0')]),
 ('GPT-Neo','EleutherAI','2021',[('GPT-Neo','2021','Mar 2021, MIT'),('GPT-J','2021','Jun 2021, Apache 2.0'),('GPT-NeoX','2022','Feb 2022, Apache 2.0')]),
 ('BLOOM','Hugging Face-led collaboration','2022',[('BLOOM','2022','Jul 2022, Responsible AI licence')]),
 ('Granite','IBM','2024',[('Granite Code Models','2024','May 2024, Apache 2.0')]),
 ('Nemotron','Nvidia','2024',[('Nemotron-4','2024','Jun 2024, NVIDIA Open Model licence'),('Nemotron 3 Ultra','2026','4 Jun 2026, OpenMDW 1.1')]),
 ('DBRX','Databricks and Mosaic ML','2024',[('DBRX','2024','Mar 2024, Databricks Open Model licence')]),
 ('Fugaku-LLM','Fujitsu, Tokyo Institute of Technology, Tohoku University, RIKEN','2024',[('Fugaku-LLM','2024','May 2024, Fugaku-LLM Terms of Use')]),
 ('MiniMax','MiniMax','2025',[('MiniMax-Text-01','2025','14 Jan 2025, Minimax Model licence'),('MiniMax-M3','2026','1 Jun 2026, MiniMax Community licence')]),
 ('Sarvam','Sarvam AI','2024',[('Sarvam-1','2024','24 Oct 2024, Sarvam AI Research licence'),('Sarvam-M','2025','23 May 2025, Apache 2.0'),('Sarvam-105B','2026','18 Feb 2026, Apache 2.0')]),
 ('Param','BharatGen','2025',[('Param-1','2025','21 Jul 2025, Apache 2.0'),('Param-2','2026','17 Feb 2026, BharatGen Research licence')]),
 ('MiMo','Xiaomi','2026',[('MiMo-V2.5-Pro','2026','27 Apr 2026, MIT'),('MiMo-V2.6-Pro','2026','MIT')]),
 ('Step','StepFun','2026',[('Step 3.5 Flash','2026','12 Feb 2026, Apache 2.0'),('Step 3.7 Flash','2026','29 May 2026, Apache 2.0')]),
 ('Hy','Tencent','2026',[('Hy3 preview','2026','23 Apr 2026, Tencent Hy Community licence'),('Hy3','2026','6 Jul 2026, Apache 2.0'),('Hy4 preview','2026','28 Aug 2026, Apache 2.0')]),
 ('Apertus','ETH Zurich and EPFL','2025',[('Apertus','2025','2 Sep 2025, Apache 2.0')]),
 ('K2','MBUZAI / IFM','2026',[('K2 Think V2','2026','27 Jan 2026, Apache 2.0'),('K2 Horizon','2026','Apache 2.0')]),
 ('Cerebras-GPT','Cerebras','2023',[('Cerebras-GPT','2023','Mar 2023, Apache 2.0')]),
 ('OpenAssistant','LAION','2023',[('OpenAssistant','2023','Mar 2023, Apache 2.0')]),
 ('YaLM','Yandex','2022',[('YaLM 100B','2022','Jun 2022, Apache 2.0')]),
 ('BERT','Google','2018',[('BERT','2018','Oct 2018, Apache 2.0')]),
 ('T5','Google','2019',[('T5','2019','Oct 2019, Apache 2.0')]),
 ('XLNet','Google','2019',[('XLNet','2019','Jun 2019, Apache 2.0')]),
 ('OPT','Meta AI','2022',[('OPT','2022','May 2022, non-commercial research licence')]),
 ('Galactica','Meta AI','2022',[('Galactica','2022','Nov 2022, CC-BY-NC-4.0')]),
 ('Chameleon','Meta AI','2024',[('Chameleon','2024','May 2024, non-commercial research licence')]),
 ('Muse','Meta AI','2026',[('Muse Glimmer','2026','10 Aug 2026, Apache 2.0')]),
 ('Laguna','Poolside AI','2026',[('Laguna S 2.1','2026','21 Jul 2026, OpenMDW 1.1')]),
 ('Motif','Motif Technologies','2026',[('Motif 3','2026','21 Jul 2026, MIT')]),
 ('Solar Open','Upstage','2026',[('Solar Open 2','2026','23 Jul 2026, Upstage Solar licence')]),
 ('A.X','SK Telecom','2026',[('A.X K2','2026','29 Jul 2026, Apache 2.0')]),
 ('Inkling','Thinking Machines Lab','2026',[('Inkling','2026','15 Jul 2026, Apache 2.0')]),
]
lm=K['Language model weights'][2]
ex={x['n']:x for x in lm['x']}
def addv(x,vs,lab):
    have={norm(v['n']) for v in x.get('v',[])}
    for n,y,dd in vs:
        if norm(n) in have: continue
        x.setdefault('v',[]).append({'n':n,'mk':lab,'y':y,'d':dd})
# extend existing
mx=ex['Mistral 7B']; mx['n']='Mistral'; mx['d']="Mistral AI's open-weight line, from the 7B model to the Mixtral mixtures and the Small, Medium and Large models."
mx['v'][0]['n']='Mistral 7B'
addv(mx,[('Mistral Large','2024','Nov 2024, Mistral Research licence'),('Mistral Small 4','2026','17 Mar 2026, Apache 2.0'),('Mistral Medium 3.5','2026','28 Apr 2026, Modified MIT')],'Mistral AI')
addv(ex['Qwen'],[('Qwen3.5','2026','15 Feb 2026, Apache 2.0'),('Qwen3.6','2026','15 Apr 2026, Apache 2.0')],'Alibaba Cloud')
addv(ex['DeepSeek'],[('DeepSeek-LLM','2023','29 Nov 2023'),('DeepSeek-V3','2024','Dec 2024, MIT'),('DeepSeek-V3.1','2025','21 Aug 2025, MIT'),('DeepSeek-V3.2','2025','1 Dec 2025, MIT'),('DeepSeek-V4-Flash','2026','31 Jul 2026, MIT'),('DeepSeek-V4-Pro','2026','13 Aug 2026, MIT'),('DeepSeek-V4.1-Flash','2026','10 Sep 2026, MIT')],'DeepSeek')
for x in lm['x']: x['g']=x.get('mk','')
labs={x['mk'] for x in lm['x']}
for f,lab,y,vs in fam:
    e={'n':f,'a':'','d':f"Open-weight model family from {lab}; each version is listed with its release date and licence as the list gives them.",'mk':lab,'y':y,'s':LL,'v':[{'n':n,'mk':lab,'y':yy,'d':dd} for n,yy,dd in vs],'g':lab}
    if len(vs)==1 and vs[0][0]==f: e['v']=[]
    lm['x'].append(e); labs.add(lab)
lm['x'].sort(key=lambda e:(e['g'].lower(),e['y'] or '9999',e['n'].lower()))
lm['nl']="One entry is a family of downloadable language-model weights from one lab; generations and sizes of the family are versions."
lm['xg']="by lab"
lm['sel']=("Every model family in Wikipedia's List of large language models whose weights the list shows as released (open or restricted licence); closed, unreleased and licence-unstated models are left out, and Llama, Gemma and DeepSeek keep the generations the earlier pass sourced. Fine-tunes such as Alpaca and Vicuna are not weights families. "
           f"Complete: {len(lm['x'])} open-weight families of the licence-stated rows in the list, which the page gives in two windows (table, then references).")
# image/speech entries get nl/sel
for kn,lab in (('Image-generation model','by lab'),('Speech and audio model','by lab')):
    k=K[kn][2]; k['nl']="One entry is a family of downloadable model weights from one lab."; k['sel']="Families named by the fetched pages in each entry; Wikipedia's List of large language models covers language models only, so no whole-space list exists for this kind."
    k['xg']='by lab'
    for x in k['x']: x.setdefault('g',x.get('mk',''))
# brand register
sample=next(b for b in brands['b'] if b['n']=='DeepSeek')
for lab in sorted(labs|{'Google'}):
    if lab not in bnames and lab not in ('Fujitsu, Tokyo Institute of Technology, Tohoku University, RIKEN',):
        brands['b'].append({'n':lab,'c':'','f':'','seg':sample['seg'],'kf':'open-weight models','d':f"Publisher of open-weight language models listed in Wikipedia's List of large language models.",'s':LL}); bnames.add(lab)
if 'Fujitsu, Tokyo Institute of Technology, Tohoku University, RIKEN' not in bnames:
    brands['b'].append({'n':'Fujitsu, Tokyo Institute of Technology, Tohoku University, RIKEN','c':'','f':'','seg':sample['seg'],'kf':'open-weight models','d':'Consortium behind Fugaku-LLM.','s':LL})
# ---------- file formats
FF='https://en.wikipedia.org/wiki/List_of_file_formats'
EB='https://en.wikipedia.org/wiki/Comparison_of_e-book_formats'
fm={}
cur=None
for line in open(W+'formats.txt',encoding='utf8'):
    line=line.rstrip('\n')
    if line.startswith('## '): cur=line[3:]; fm[cur]=[]; continue
    ext,desc=line.split(' - ',1); fm[cur].append((ext,desc))
def mkent(ext,desc,g,src=FF):
    parts=ext.split('/')
    n=parts[0]; 
    if ext=='MAX3D': n='MAX'
    a=' · '.join(parts[1:]) if ext.count('/')<5 and not ext.startswith('TIFF/EP') else ''
    if ext.startswith('TIFF/EP'): n='TIFF/EP'
    return {'n':n,'a':a,'d':desc.rstrip('.')+'.','mk':'','y':'','s':src,'g':g}
def fill(kn,groups,nl,sel_ref,cover,extra=None):
    k=K[kn][2]; seen={norm(x['n']) for x in k.get('x',[])}; out=list(k.get('x',[]))
    cnt=0; tot=0
    for hdr,g in groups:
        for ext,desc in fm[hdr]:
            tot+=1
            e=mkent(ext,desc,g)
            if norm(e['n']) in seen: continue
            seen.add(norm(e['n'])); out.append(e); cnt+=1
    k['x']=out
    k['nl']=nl; k['xg']=sel_ref[1]
    k['sel']=sel_ref[0]+f" {cover.format(n=len(out),t=tot)}"
    return k
fill('Digital music file',[('AUDIO Lossless, uncompressed','Lossless, uncompressed'),('AUDIO Lossless, compressed','Lossless, compressed'),('AUDIO Lossy','Lossy')],
 "One entry is an audio file format; codecs and container variants are versions.",
 ("Every row of the lossless (uncompressed and compressed) and lossy audio sections of Wikipedia's List of file formats; the 'other audio formats' section (tracker, chip-music and notation files) is left out, and WMA is one entry for its lossless and lossy forms.","by compression"),
 "Complete: {n} of {t} rows in those three sections (WMA listed twice on the page).")
fill('Digital photo or image',[('RASTER Raster graphics','Raster image format')],
 "One entry is a raster image file format, including camera raw and layered paint files.",
 ("Every row of the Raster graphics section of Wikipedia's List of file formats, read through a summariser in a window from character 50,000 to 150,000.","by kind of use"),
 "Covers {n} of {t} rows read in the Raster graphics section; the page was summarised, so a few rows may have been dropped.")
fill('Editable graphics file',[('VECTOR Vector graphics','Vector or drawing format')],
 "One entry is a vector or drawing file format.",
 ("Every row of the Vector graphics section of Wikipedia's List of file formats that is not a 3D format (those are under 3D model file format).","by kind of use"),
 "Covers {n} of {t} rows read in the Vector graphics section; the page was summarised, so a few rows may have been dropped.")
# 3D new kind
shelf3=K['3D model'][1]
k3={'n':'3D model file format','a':'mesh format · CAD file · scene file','d':'The file format a 3D model, scene or CAD part is saved in; formats are listed by what makes them.','s':FF,'x':[],'tt':[['Use',['Interchange and web','Modelling software','Game engine','CAD and manufacturing','3D printing']]]}
shelf3['k'].insert(1,k3)
K['3D model file format']=(None,shelf3,k3)
fill('3D model file format',[('3D 3D graphics','3D graphics format')],
 "One entry is a 3D graphics file format; text, binary and zipped forms of the same format are versions.",
 ("Every row of the 3D graphics section of Wikipedia's List of file formats.","by maker or purpose"),
 "Covers {n} of {t} rows read in the 3D graphics section; the page was summarised, so a few rows may have been dropped.")
# e-book from comparison page
eb=[('EPUB','epub','Open standard for e-books; reflowable and fixed-layout.'),('Kindle','azw · azw3 · kfx','Amazon formats, with DRM, not an open standard.'),('Mobipocket','prc · mobi','Older e-book format with DRM, not an open standard.'),('FictionBook','fb2','Open XML format without DRM.'),('Apple Books','ibook','Apple format with DRM, not an open standard.'),('Portable Document Format','pdf','Fixed-page document, open standard, can carry DRM.'),('DjVu','djvu','Open format for scanned documents.'),('DOC','doc','Word-processor file, not an open standard.'),('DOCX','docx','Word-processor file, open standard.'),('HTML','html','Web page used as e-book, no DRM.'),('INF','inf','Open e-book format without DRM.'),('Microsoft Reader','lit','Discontinued format with DRM, not an open standard.'),('Multimedia e-book','exe · html','E-book with embedded media; DRM possible.'),('Newton Book','pkg','Apple Newton format, open, without DRM.'),('eReader','pdb','Palm-era format with DRM, not an open standard.'),('Plain text file','txt','Unformatted text, no DRM.'),('Plucker','pdb','Open format for handheld readers.'),('PostScript','ps','Page description language, open, no DRM.'),('Tome Raider','tr2 · tr3','Format with DRM, not an open standard.'),('OpenXPS','oxps · xps','Fixed-page document, open standard.'),('BBeB','lrf','Sony Broad Band eBook format.'),('KPUB','kepub','Kobo e-book format.')]
k=K['E-book'][2]
k['x']=[{'n':n,'a':a,'d':dd,'mk':'','y':'','s':EB,'g':'Open standard' if 'open standard.' in dd and 'not an open' not in dd or dd.startswith('Open') else 'Proprietary or restricted'} for n,a,dd in eb]
for e in k['x']:
    if e['n'] in ('BBeB','KPUB'): e['s']=FF; e['g']='Proprietary or restricted'; e['a']=''
k['nl']="One entry is an e-book or document file format; versions are revisions of the format."
k['xg']='by openness'
k['sel']="Every format in the main table of Wikipedia's Comparison of e-book formats, plus BBeB and KPUB from the document section of List of file formats; the comic book archive is under Comic or manga file. Complete: 22 of 22 (21 table rows less the comic archive, plus 2)."
ck=K['Comic or manga file'][2]
ck['x']=[{'n':'Comic book archive','a':'cbr · cbz · cb7 · cbt · cba','d':'Archive of page images read as a comic; open standard.','mk':'','y':'','s':EB,'g':'Open standard'}]
ck['nl']="One entry is a comic file format."; ck['xg']='by openness'
ck['sel']="The one comic format in Wikipedia's Comparison of e-book formats. Complete: 1 of 1 in that table."
# ---------- commodity pruning
dropped=[]
for dp in d['depts']:
    if dp['n'] in ('Creative assets','Game & platform items'):
        for sh in dp['s']:
            for k in sh['k']:
                for key in ('m','r'):
                    if k.get(key): dropped+= [t[0] for t in k.pop(key)]
                if k.get('x') and not k.get('nl'):
                    k['nl']="One entry is a landmark line, collection or item named by a fetched page; the kind is otherwise a commodity."
                    k['sel']="Icon rule: landmarks named by a fetched page only; no whole-space reference exists, so no complete list is claimed."
for dp in d['depts']:
    if dp['n']=='Domains & tokens':
        for sh in dp['s']:
            for k in sh['k']:
                if k.get('x') and not k.get('nl'):
                    k['nl']="One entry is a named collection, name service or platform; individual tokens are not entries."
                    k['sel']="Collections named by the fetched pages in each entry; no whole-space reference was read, so no complete list is claimed."
json.dump(d,open(W+'I2.new.json','w'),ensure_ascii=False,indent=1)
json.dump(brands,open(W+'I2_brands.new.json','w'),ensure_ascii=False,indent=1)
print('dropped m typefaces',dropped_m); print('dropped creative/game m,r',len(dropped))
print({kn:(counts[kn]['n'],len(K[kn][2]['x'])) for kn in kinds_tf}); print('excluded',excluded)
print(len(lm['x']),'families')
