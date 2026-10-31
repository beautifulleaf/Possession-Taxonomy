"""Merge verified BRANDLAYER results into the live registers.
For category C reads ../verify/work/BRANDLAYER/VERIFY_<C>.json and writes:
  out/<C>_brands.json : new brands (shown, not already present) with tier ('quality'|'cultural'|'seller'|'listed'),
                        rg (renowned regional division, if any), s (source), kf (dept), d (note); known brands named
                        in the verify file or its cross_tag list get a minimal entry so merge.py adds category C, plus
                        tier/rg where they had none.
  out/<C>.json key 'rg': regional divisions whose source page states renown: {n, sp, s, q, b:[brand names shown]}.
Backups in work/BRANDLAYER_MERGE/. Brands listed for C in any MOVES_<X>.json are merged too.
Usage: python3 tools/brandlayer_merge.py A1 A2 ..."""
import json,sys,os,re,shutil,unicodedata
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); V=f'{R}/../verify/work/BRANDLAYER'
os.makedirs(f'{R}/work/BRANDLAYER_MERGE',exist_ok=True)
def norm(s):
    s=''.join(c for c in unicodedata.normalize('NFKD',s) if not unicodedata.combining(c))
    s=s.lower().replace('&','and'); s=re.sub(r'\(.*?\)','',s); return re.sub(r'[^a-z0-9]','',s)
glob_idx={norm(r[0]):r[0] for r in json.load(open(f'{R}/reader/_brand_index.json'))['b']}
RANK={'quality':0,'cultural':1,'seller':2,'listed':3}
for c in sys.argv[1:]:
    v=json.load(open(f'{V}/VERIFY_{c}.json'))
    import glob as _g
    for mp in sorted(_g.glob(f'{V}/MOVES_*.json')):  # brands verified in another category's pass that belong here
        md=json.load(open(mp)); mv=md.get('to',{}).get(c,[]); det=md.get('detail',{})
        mv=[x if isinstance(x,dict) else {'n':x,'src':det.get(x,{}).get('src',''),'note':det.get(x,{}).get('verified',''),
            'tier':'cultural' if 'wikipedia.org/wiki/' in det.get(x,{}).get('src','') else 'listed'} for x in mv]
        for b in mv: b.setdefault('shown',True); b['note']=(b.get('note','')+f' [moved from {os.path.basename(mp)[6:-5]}]').strip()
        v['brands']=v['brands']+mv
    bp=f'{R}/out/{c}_brands.json'; cp=f'{R}/out/{c}.json'
    for p in (bp,cp): shutil.copy(p,f'{R}/work/BRANDLAYER_MERGE/{os.path.basename(p)}.before')
    B=json.load(open(bp)); cat=json.load(open(cp))
    here={norm(b['n']):b for b in B['b']}
    regs=[r for r in v.get('regions',[]) if r.get('renown')]
    reg_of={}
    for r in regs:
        for n in r.get('brands',[]): reg_of.setdefault(norm(n),r['region'])
    new=upd=cross=0
    for b in v['brands']:
        if not b.get('shown',True): continue
        keys=[norm(b['n'])]+[norm(a) for a in b.get('aliases',[])]
        tier=b.get('tier','listed'); rg=b.get('region') or next((reg_of[k] for k in keys if k in reg_of),'')
        src=b.get('src2') or b.get('src') or ''
        homo=b.get('homonym')
        hit=None if homo else next((here[k] for k in keys if k in here),None)
        if hit:
            if 'tier' not in hit or RANK.get(tier,3)<RANK.get(hit['tier'],3): hit['tier']=tier
            if rg and not hit.get('rg'): hit['rg']=rg
            if b.get('legal') and not hit.get('legal'): hit['legal']=str(b['legal'])[:240]
            if b.get('scene'):
                sc=hit.get('sc') or []
                if b['scene'] not in sc: hit['sc']=sc+[b['scene']]
            upd+=1; continue
        g=None if homo else next((glob_idx[k] for k in keys if k in glob_idx),None)
        if g:  # known in another category: add C with a minimal entry (merge.py unions cats)
            e={'n':g,'tier':tier}; 
            if rg: e['rg']=rg
            if b.get('legal'): e['legal']=str(b['legal'])[:240]
            if b.get('scene'): e['sc']=[b['scene']]
            B['b'].append(e); here[norm(g)]=e; cross+=1; continue
        e={'n':b['n'],'c':b.get('country',''),'seg':'','kf':(b.get('dept') or '')[:40],'d':(b.get('note') or '')[:240],'s':src,'tier':tier}
        if b.get('aliases'): e['an']=' · '.join(b['aliases'])
        if rg: e['rg']=rg
        if b.get('legal'): e['legal']=str(b['legal'])[:240]
        if b.get('scene'): e['sc']=[b['scene']]; e['seg']=b['scene']
        if b.get('owner'): e['rel']=[str(b['owner'])]; e['d']=(e.get('d') or '')[:200]+('' if 'owner' in (e.get('d') or '').lower() else ' Owner: '+str(b['owner'])+'.')
        if b.get('role')=='seller' or tier=='seller': e['role']='seller'
        B['b'].append(e); here[b['n'].lower() if homo else norm(b['n'])]=e; new+=1
    for n in v.get('cross_tag',[]):
        nm=n if isinstance(n,str) else n.get('n')
        g=glob_idx.get(norm(nm))
        if g and norm(g) not in here: B['b'].append({'n':g}); here[norm(g)]=B['b'][-1]; cross+=1
    for am in v.get('alias_merges',[]):  # extra aliases for a brand (merged duplicates, product lines)
        if isinstance(am,list): am={'n':am[0],'add_aliases':list(am[1:])}
        if 'n' not in am and 'keep' in am: am={'n':am['keep'],'add_aliases':[am['alias']] if isinstance(am.get('alias'),str) else am.get('alias',[])}
        k=norm(am['n']); e=here.get(k)
        if e is None:
            g=glob_idx.get(k)
            if not g: continue
            e={'n':g}; B['b'].append(e); here[k]=e
        have=[a for a in (e.get('an') or '').split(' · ') if a]
        for a in am.get('add_aliases',[]):
            if a not in have: have.append(a)
        if have: e['an']=' · '.join(have)
    shown_names={norm(b['n']) for b in B['b']}
    cat['rg']=[{'n':r['region'],'sp':r.get('speciality',''),'s':r.get('src',''),'q':r.get('quote',''),
                'b':[n for n in r.get('brands',[]) if norm(n) in shown_names or norm(n) in glob_idx]} for r in regs]
    json.dump(B,open(bp,'w'),ensure_ascii=False,indent=1); json.dump(cat,open(cp,'w'),ensure_ascii=False,indent=1)
    print(c,'new',new,'updated',upd,'cross-tagged',cross,'regions',len(cat['rg']))
