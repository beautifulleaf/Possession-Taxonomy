import json,copy,sys,re
sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/V4_H1_HAIRBODY')
from data import *
R='/home/user/Possession-Taxonomy/rebuild/'
H=json.load(open(R+'out/H1.json'))
NAMES={'Hair':'H','Shaving & hair removal':'S','Oral care':'O','Bath, body & hygiene':'B','Comfort & massage':'C'}
old={d['n']:copy.deepcopy(d) for d in H['depts'] if d['n'] in NAMES}
BK={'H':('Hair-care brand','hair-care'),'S':('Shaving & grooming brand','shaving and grooming'),'O':('Oral-care brand','oral-care'),'B':('Body-care & hygiene brand','body-care and hygiene')}
SHELF={'H':'Wash & care','S':'Razors & blades','O':'Brushes','B':'Bath, shower & deodorant'}
SAME={'Wig','Hairpiece','Hair dryer','Multi-styler','Hot brush','Hair straightener','Curling iron','Hair dryer attachments & spare parts','Hairbrush','Comb','Hair tie','Hair clip','Hair towel',
'Double-edge safety razor','Single-edge safety razor','Safety razor blade','Cartridge razor','Straight razor','Shavette','Razor hone','Razor strop','Shaving brush','Electric shaver','Beard trimmer','Hair clipper','Shaver & clipper spare parts','Tweezers','Epilator','IPL hair-removal device','Facial razor',
'Electric toothbrush','Toothbrush head','Water flosser','Loofah, sponge & bath mitt','Toiletry & make-up bag','Period underwear','Handheld massager','Massage gun','Massage chair','Manual toothbrush','Bar soap'}
# product kinds whose x entries (with mk) move to the brand kind: everything not in SAME
OWNMAP={}
for b in B:
    OWNMAP.setdefault(b['n'].lower(),b)
DEV_OWN={'braun':(PGn,'','Global group'),'oral-b':(PGn,'','Global group'),'waterpik':(CDn,'2017','Global group'),'philips sonicare':('Philips','2000','Independent'),'gillette':(PGn,'','Global group')}
def ownfields(name):
    b=OWNMAP.get(name.lower())
    if b:
        return b['own'],b['own_y'],b['cty']
    k=DEV_OWN2.get(name.lower())
    if k: return k[0],k[1],''
    return '','',''
def tier(own,name):
    if name=='Natura': return 'National champion'
    if own in TIER_GLOBAL: return 'Global group'
    if own: return 'Independent'
    return ''
sources=[]
USED=set()
rep={}
parts_depts=[];newbrands={}
def gname(e):
    own=e.get('own','')
    if not own: return 'Owner not stated'
    if own in GROUPS or own==HULn: return 'Global group: '+(UNn if own==HULn else own)
    return 'Independents and national champions'
def gkey(e):
    g=gname(e)
    if g.startswith('Global group: '):
        o=g[14:]; return (0,GROUPS.index(o),e['n'].lower())
    if g.startswith('Indep'): return (1,0,e['n'].lower())
    if g.startswith('Craft'): return (1,1,e['n'].lower())
    return (2,0,e['n'].lower())
for dn,code in NAMES.items():
    d=old[dn]; reg={}
    def brand(name,src,d_=None,y=''):
        k=name.lower()
        if k in reg: return reg[k]
        e={'n':name,'a':'','d':d_ or '', 'mk':name,'y':y,'s':src,'v':[]}
        reg[k]=e; return e
    if code!='C':
        for b in B:
            if b['dept']!=code: continue
            e=brand(b['n'],U[b['src']],b['d'])
            e['own']=b['own'];e['own_y']=b['own_y'];e['cty']=b['cty']
            if b.get('tier_o'): e['tier_o']=b['tier_o']
            if b.get('g_o'): e['g_o']=b['g_o']
            if b.get('d') and not e['d']: e['d']=b['d']
    cnt={'moved_x':0,'m_ver':0,'m_ent':0,'r_drop':0}
    samekinds=[]
    for sh in d['s']:
        for k in sh['k']:
            kn=k['n']; ks=k.get('s','')
            xs=k.pop('x',[]) or []; ms=k.pop('m',[]) or []; rs=k.pop('r',[]) or []
            if kn in SAME or code=='C':
                keep=[]
                # existing x: keep, add owner fields
                for x in xs:
                    if kn=='Bar soap' and x.get('mk'):
                        e=brand(x['mk'],x.get('s',ks)); 
                        e['v'].append({'n':x['n'],'y':x.get('y',''),'d':x.get('d','')}); cnt['moved_x']+=1; continue
                    mk=x.get('mk','')
                    if mk:
                        o,oy,c=ownfields(mk)
                        if o: x['own']=o;x['tier']=tier(o,mk);x['cty']=c;x['own_y']=oy
                    x['g']=mk or 'Traditional'
                    keep.append(x)
                # m grouped by maker
                bym={}
                for mod,mk in ms: bym.setdefault(mk or 'Unattributed',[]).append(mod)
                rname={}
                for rn,rm in rs: rname.setdefault(rm,rn)
                if kn=='Electric toothbrush':
                    EB={'Oral-B iO':('Oral-B',['iO Series 9 / iO Series 10','iO3']),'Oral-B Pro':('Oral-B',['Pro 1000']),'Oral-B Vitality':('Oral-B',['Vitality Pro']),
                        'Philips Sonicare DiamondClean':('Philips Sonicare',['DiamondClean 9000']),'Philips Sonicare ProtectiveClean':('Philips Sonicare',['ProtectiveClean','4100 Series']),
                        'Philips Sonicare Prestige':('Philips Sonicare',['9900 Prestige']),'Philips One by Sonicare':('Philips Sonicare',['Philips One']),
                        'Ordo Sonic':('Ordo',['Sonic+','Sonic Kids']),'SURI':('SURI',['SURI 2.0'])}
                    for en,(mk,vs) in EB.items():
                        keep.append({'n':en,'a':'','d':'Electric toothbrush line by '+mk+'.','mk':mk,'y':'','s':ks,'g':mk,'v':[{'n':v,'y':'','d':''} for v in vs]}); cnt['m_ent']+=1
                else:
                    taken={e['n'].lower() for e in keep}
                    for mk,mods in bym.items():
                        en=rname.pop(mk,None)
                        if not en or en.lower() in taken or en.lower() in USED: en=(mk+' '+kn.lower()) if mk!='Unattributed' else kn+' (maker not stated)'
                        taken.add(en.lower()); USED.add(en.lower()) if False else None
                        keep.append({'n':en,'a':'','d':(mk+' '+kn.lower()+' range.') if mk!='Unattributed' else 'Item without a stated maker.','mk':'' if mk=='Unattributed' else mk,'y':'','s':ks,'g':mk,'v':[{'n':v,'y':'','d':''} for v in mods]}); cnt['m_ent']+=1
                    for mk,en in rname.items():  # ranges with no models
                        if en.lower() in taken: continue
                        taken.add(en.lower())
                        keep.append({'n':en,'a':'','d':(mk+' '+kn.lower()+' range.'),'mk':mk,'y':'','s':ks,'g':mk,'v':[]}); cnt['m_ent']+=1
                    # owner fields
                    for e in keep:
                        if 'own' in e: continue
                        o,oy,c=ownfields(e.get('mk','')) if e.get('mk') else ('','','')
                        if o: e['own']=o;e['tier']=tier(o,e['mk']);e['cty']=c;e['own_y']=oy
                if kn=='Heat pack & hand warmer':
                    keep.append({'n':'MegRhythm','a':'','d':'Kao steam-warming eye and body sheets; listed among Kao brands.','mk':'MegRhythm','y':'','s':U['KAO'],'g':'Kao Corporation','own':KAn,'tier':'Global group','cty':'','own_y':''})
                if keep:
                    keep.sort(key=lambda e:(e.get('g','').lower(),e['n'].lower()))
                    k['x']=keep
                    k['nl']='One entry is a maker\'s named line or model of this kind sold under its own name; generations, sizes and variants are versions.'
                    k['sel']=('No whole-space reference lists this kind. Entries follow the retail, maker and community pages read in the structure pass (cited per entry), with maker ranges from the same pages; every earlier loose model is now a version of its maker\'s entry. '
                              'Covers %d entries; no reference lists every maker, so the kind is not complete.'%len(keep))
                    k['xg']='by maker'
                    samekinds.append((kn,len(keep)))
            else:
                # product kind: move entries into brand kind
                for x in xs:
                    mk=x.get('mk') or x['n']
                    e=brand(mk,x.get('s',ks))
                    if x['n'].lower()==mk.lower():
                        e['d']=x.get('d','') or e['d']; e['y']=x.get('y','') or e['y']; e['s']=x.get('s',e['s']) if not e['s'] or e['s'] in (U['CSH'],U['CSO']) else e['s']
                        e['v']=e['v']+x.get('v',[])
                        if x.get('a'): e['a']=x['a']
                    else:
                        e['v'].append({'n':x['n'],'y':x.get('y',''),'d':(kn+': '+x.get('d','')).strip()})
                        for vv in x.get('v',[]): e['v'].append({'n':vv['n'],'y':vv.get('y',''),'d':vv.get('d','')})
                        if not e['d']: e['d']=x.get('d','')
                    cnt['moved_x']+=1
                for mod,mk in ms:
                    e=brand(mk or 'Unattributed '+kn,ks)
                    e['v'].append({'n':mod,'y':'','d':kn}); cnt['m_ver']+=1
                for rn,rm in rs:
                    brand(rm,ks); cnt['r_drop']+=1
    # finish brands
    ents=[]
    for e in reg.values():
        if not e['d']:
            bt=BK[code][1] if code!='C' else ''
            ow=e.get('own','')
            e['d']=(e['n']+' is a '+bt+' brand of '+ow+'.') if ow else (e['n']+' is a '+bt+' brand; no fetched page names its owner.')
            if e.get('own_y'): e['d']=e['d'][:-1]+', acquired '+e['own_y']+'.'
        e['mk']=e['n']
        e['tier']=e.pop('tier_o',None) or tier(e.get('own',''),e['n'])
        if not e.get('own'): e.pop('own',None);e.pop('tier',None)
        if not e.get('own_y'): e.pop('own_y',None)
        if not e.get('cty'): e.pop('cty',None)
        if not e['v']: e.pop('v')
        e['g']=e.pop('g_o',None) or gname(e)
        ents.append(e)
    # roles
    for e in ents:
        if e['n'] in ('Colgate',) and code=='O': e['role']='landmark'
        if e['n']=='Gillette' and code=='S': e['role']='landmark'
    if code!='C':
        ents.sort(key=gkey)
        bn,btxt=BK[code]
        n_g=sum(1 for e in ents if e['g'].startswith('Global'))
        kind={'n':bn,'a':'','d':'A %s brand sold under its own name, grouped by who owns it.'%btxt,'s':U['CP'],'x':ents,
              'nl':'One entry is a %s brand sold under its own name; product lines, formulations and variants within it are versions.'%btxt,
              'sel':('Follows the brand lists on the Wikipedia pages of the twelve global groups (Procter & Gamble, Unilever, L\'Oréal, Colgate-Palmolive, Haleon, Kenvue, Beiersdorf, Henkel, Edgewell, Kao, Church & Dwight; Lion from its own product page), '
                     'cut to %s brands, with independents and owner-not-stated brands from the Wikipedia toothpaste, shampoo and soap lists and from earlier retail pages. Group sections follow the order of the owner list. '
                     'Covers %d brands, %d of them in the twelve group portfolios as those pages list them; the groups\' own brand pages were not read, so portfolios may be incomplete.')%(btxt,len(ents),n_g),
              'xg':'by owner tier and group'}
        shelf={'n':'Brands by market','t':'%s brands grouped by owner, from the global groups to independents; product types are on the shelves below.'%btxt.capitalize(),'ax':'brands by owner tier, then owner group','k':[kind]}
        d['s'].insert(0,shelf)
    rep[dn]=(cnt,samekinds,len(ents) if code!='C' else 0)
    for e in ents: newbrands[(e['n'])]=e
    parts_depts.append(d)
json.dump({'depts':parts_depts},open(R+'work/V4_H1_HAIRBODY/stage1.json','w'),ensure_ascii=False)
json.dump({k:(v[0],v[1],v[2]) for k,v in rep.items()},open(R+'work/V4_H1_HAIRBODY/rep1.json','w'),ensure_ascii=False,indent=1)
json.dump(list(newbrands.values()),open(R+'work/V4_H1_HAIRBODY/brands_all.json','w'),ensure_ascii=False)
print(json.dumps(rep,ensure_ascii=False,indent=1)[:3000])
