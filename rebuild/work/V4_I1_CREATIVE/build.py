import json,re,copy,sys
sys.path.insert(0,'.')
from data import K,R
OLD=json.load(open('../../out/I1.json'))
NAMES=["Photo, design & 3D","Video & animation","Music & audio","Audio plug-ins & virtual instruments","Hobbies, science & sky"]
depts=[copy.deepcopy(d) for d in OLD['depts'] if d['n'] in NAMES]
# extra rows with other refs
EXTRA={'Software synthesiser':[('FabFilter Twin@FF','FabFilter','2005',''),('FabFilter One@FF','FabFilter','2004',''),
 ('Stylus RMX@SP','Spectrasonics','',''),('Atmosphere@SP','Spectrasonics','2002',''),('Trilogy@SP','Spectrasonics','',''),('Serum 2@XF','Xfer Records','2025','')]}
TOT={'RA':('Wikipedia, Comparison of raster graphics editors',95),'VE':('Wikipedia, Comparison of vector graphics editors',33),'L3D':('Wikipedia, List of 3D computer graphics software',125),
'VID':('Wikipedia, Comparison of video editing software',54),'DAW':('Wikipedia, Comparison of digital audio editors (main table)',37),'PL':('Wikipedia, Planetarium software',26),
'SS':('Wikipedia, Software synthesizer',50),'SC':('Wikipedia, Comparison of scorewriters',35),'GIS':('Wikipedia, Comparison of geographic information systems software',38),
'GEN':('Wikipedia, Genealogy software',60),'SW':('Wikipedia, List of screenwriting software',19),'CAD':('Wikipedia, Comparison of computer-aided design editors',70),
'EDA':('Wikipedia, Comparison of EDA software',40),'SCR':('Wikipedia, Comparison of screencasting software',40),'AUD':('Wikipedia, Comparison of audio player software',46),
'VPL':('Wikipedia, Comparison of video player software',48),'STAT':('Wikipedia, Comparison of statistical packages',60),'T2I':('Wikipedia, Text-to-image model',31),
'AP':('Wikipedia, Audio plug-in',13),'WA':('Wikipedia, Waves Audio',31),'NI':('Wikipedia, Native Instruments',16),'FF':('Wikipedia, FabFilter',14),'SP':('Wikipedia, Spectrasonics',6),'UA':('Wikipedia, Universal Audio (company)',11),'XF':('Wikipedia, Xfer Records',2),'MUS':('',0)}
MAKERN={'Adobe Inc.':'Adobe','Adobe Systems':'Adobe','Avid':'Avid Technology','Microsoft Corporation':'Microsoft','Corel Corporation':'Corel','Serif Europe':'Serif (Europe)','Serif':'Serif (Europe)',
'Propellerhead Software':'Reason Studios','Waves':'Waves Audio','Xfer':'Xfer Records','Maxon':'Maxon','MAGIX':'MAGIX','Magix':'MAGIX','Foundry':'The Foundry'}
DROP={'Quad Cortex','Gardena','Lexicon 224 and 480L','Valhalla reverbs','Tokyo Dawn Labs free dynamics','Neural DSP plug-ins','Mastering The Mix metering','Mastering The Mix meters'}
def nm(m): return MAKERN.get(m,m)
def key(s): return re.sub(r'[^a-z0-9]','',s.lower())
seen=set()
for d in depts:
    for sh in d['s']:
        for k in sh['k']:
            for x in k.get('x',[]) or []:
                seen.add(key(x['n']))
                for a in re.split(r'\s*·\s*',x.get('a','') or ''):
                    if a: seen.add(key(a))
newbrands={}
reg={key(b['n']) for b in json.load(open('../../out/I1_brands.json'))['b']}
used=set()
report=[]
def mkentry(n,mk,y,a,src,kindnoun,ref=None,note=''):
    mk=nm(mk)
    d=(f"{n}, a {kindnoun} from {mk}" if mk else f"{n}, a {kindnoun}")+(f", first released {y}." if y else ".")
    e={'n':n,'a':a,'d':d,'mk':mk,'y':y,'s':src,'v':[],'dt':''}
    if mk:
        e['own']=mk
        used.add(mk)
    return e
def grp(e):
    return e.get('mk') or 'Independent and community projects'
def yk(e):
    m=re.search(r'\d{4}',e.get('y','') or ''); return int(m.group()) if m else 9999
# create new kinds
def newkind(dept,shelf,after,kd):
    for d in depts:
        if d['n']==dept:
            if shelf not in [s['n'] for s in d['s']]:
                d['s'].append({'n':shelf,'t':kd.pop('shelf_t'),'ax':kd.pop('shelf_ax'),'k':[]})
            for s in d['s']:
                if s['n']==shelf: s['k'].append(kd)
newkind('Photo, design & 3D','3D, CAD & making',None,{'n':'3D renderer','a':'renderer · rendering engine','d':'Program that turns a 3D scene into a finished image or animation, alone or inside a modelling program.','s':R['L3D'],'x':[],'tt':[['Method',['Ray tracing','Path tracing','Unbiased']],['Processor',['CPU','GPU']]],'see':[],'shelf_t':'','shelf_ax':''})
newkind('Audio plug-ins & virtual instruments','Formats & bundles',None,{'n':'Plug-in format','a':'plug-in standard · plug-in API','d':'Interface standard that lets a plug-in run inside a host such as a digital audio workstation.','s':R['AP'],'x':[],'tt':[['Platform',['Windows','macOS','Linux']],['Host',['Pro Tools','Logic Pro','Any DAW']]],'shelf_t':'The standards plug-ins are built to and the bundles that gather them.','shelf_ax':'kinds from the format a plug-in uses to the bundle it is sold in'})
newkind('Audio plug-ins & virtual instruments','Formats & bundles',None,{'n':'Instrument & effect bundle','a':'plug-in suite · collection','d':'Collection of instruments and effects sold together under one name.','s':R['NI'],'x':[],'tt':[['Content',['Instruments','Effects','Both']]]})
newkind('Hobbies, science & sky','Home, family & health',None,{'n':'Online family-tree service','a':'genealogy website','d':'Website that holds family trees and records for its members to search and build on.','s':R['GEN'],'x':[],'tt':[['Access',['Free','Subscription']]]})
for d in depts:
    for sh in d['s']:
        if sh['n']=='3D, CAD & making' : pass
for d in depts:
  for sh in d['s']:
    # ensure new kinds with empty shelf_t
    for k in sh['k']:
        kn=k['n']; spec=K.get(kn)
        noun=kn.lower()
        src_k=k.get('s') or ''
        xs=k.get('x') or []
        for x in xs:
            x['mk']=nm(x.get('mk',''))
            if x['mk']: x.setdefault('own',x['mk'])
        existing_n=len(xs)
        # convert m
        for m in k.pop('m',None) or []:
            n,mk=m[0],m[1]
            if key(n) in seen or n in DROP or re.search(r'plug-ins$|reverbs$|delays$|meters$|metering$|free dynamics$|alignment tools$',n): continue
            seen.add(key(n))
            xs.append(mkentry(n,mk,'',' ',src_k or R['MUS'],noun)); xs[-1]['a']=''
        kept_from_m=len(xs)-existing_n
        rows=[]
        if spec:
            for r in spec['rows']:
                p=r.split('|'); p+=['']*(5-len(p))
                n,mk,y,a=p[0],p[1],p[2],p[3]
                ref=spec['ref']
                if '@' in n: n,ref=n.split('@')
                rows.append((n,mk,y,a,ref))
        for n,mk,y,a in EXTRA.get(kn,[]):
            ref='FF'
            if '@' in n: n,ref=n.split('@')
            rows.append((n,mk,y,a,ref))
        refcount={}
        for n,mk,y,a,ref in rows:
            if key(n) in seen: continue
            seen.add(key(n)); 
            for al in re.split(r'\s*·\s*',a):
                if al: seen.add(key(al))
            xs.append(mkentry(n.strip(),mk,y,a,R[ref],noun))
            refcount[ref]=refcount.get(ref,0)+1
        # roles
        for x in xs:
            if x['n']=='Neon': x['role']='origin'
            if x['n']=='Virtual Studio Technology': x['role']='origin'
            if x['n']=='Serum':
                if not any(v['n']=='Serum 2' for v in x.get('v',[])): x.setdefault('v',[]).append({'n':'Serum 2','mk':'Xfer Records','y':'2025','d':'Second generation'})
        for x in xs:
            x['g']=grp(x)
            x.setdefault('v',[])
            x.setdefault('dt','')
            x.setdefault('a','')
        if xs:
            # sort by group then year then name
            gs=sorted({x['g'] for x in xs},key=lambda g:(g=='Independent and community projects',g.lower()))
            xs.sort(key=lambda x:(gs.index(x['g']),yk(x),x['n'].lower()))
            k['x']=xs
            k['nl']=f"One entry is a {noun} sold or distributed under its own name; major releases and editions are versions."
            if kn in('Plug-in format',): k['nl']="One entry is a plug-in interface standard with its own name; revisions are versions."
            if kn=='Online family-tree service': k['nl']="One entry is a genealogy website under its own name."
            if kn=='Instrument & effect bundle': k['nl']="One entry is a named bundle of instruments and effects."
            if kn=='Media player': k['nl']="One entry is a program that plays music or video, or manages a music library, sold or distributed under its own name."
            if kn in ('AI image generator',): k['nl']="One entry is an image-generating model or service under its own name; numbered releases are versions."
            k['xg']="by maker, then year of first release, then name"
            if spec:
                parts=[]
                for ref,c in refcount.items():
                    t,tot=TOT[ref]
                    parts.append(f"{c} of about {tot} in {t}")
                refs='; '.join(sorted({TOT[r][0] for r in refcount})) or ''
                old=f" Entries from the previous edition ({existing_n} named products and {kept_from_m} former model-list items) are kept."
                base=f"Follows {refs}: every product on the page that is still sold or widely used, placed under this kind; discontinued products, libraries, servers and trade tools, and products placed in another kind, are left out.{old}"
                cov=' Covers '+'; '.join(parts)+'; the rest are discontinued, trade or placed in other kinds.' if parts else ''
                k['sel']=base+cov
            else:
                k['sel']=f"No whole-space reference list was fetched for this kind; the list follows the previous edition's sources ({src_k}), with former model-list items now entries ({kept_from_m}). Covers {len(xs)} entries kept or converted; no complete reference was read."
            report.append((kn,existing_n,kept_from_m,len(xs)-existing_n-kept_from_m,len(xs)))
        # drop empty x
        if not xs: k.pop('x',None)
        k.pop('shelf_t',None); k.pop('shelf_ax',None)
# fix shelf placeholders
for d in depts:
    for sh in d['s']:
        if not sh.get('t'): sh['t']=sh.get('t') or 'Programs of this kind.'
        sh.pop('shelf_t',None)
# market summary: none sourced
brands=[]
for mkr in sorted(used):
    if key(mkr) not in reg:
        brands.append({'n':mkr,'c':'','f':'','seg':'','kf':'','d':f"Maker or author of software listed in the creative departments of this category.",'s':''})
part={'replaces':NAMES,'depts':depts,'brands':brands,'brand_updates':{},'renames':{},'moves':[]}
json.dump(part,open('../../out/I1_parts/CREATIVE.json','w'),ensure_ascii=False,indent=0)
json.dump(report,open('report_counts.json','w'))
for r in report: print(r)
print(len(brands),'new brands')
