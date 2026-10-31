import json,sys,os,copy
sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/V4_D1')
from data1 import *
from data2 import *
P='/home/user/Possession-Taxonomy/rebuild/out/D1.json'
B='/home/user/Possession-Taxonomy/rebuild/work/V4_D1/bak/D1.json'
d=json.load(open(B))  # always rebuild from the backup
kinds={}
for dep in d['depts']:
    for s in dep['s']:
        for k in s['k']: kinds[k['n']]=(dep,s,k)
stats={}
def yr(e):
    t=''.join(c for c in str(e.get('y','')) if c.isdigit())[:4]
    return int(t) if t else 9999
def order(xs,groups):
    gi={g:n for n,g in enumerate(groups)}
    return sorted(xs,key=lambda e:(gi.get(e.get('g'),99),yr(e),e['n']))
# stats of before
for n,(dp,s,k) in kinds.items(): stats[n]={'before_x':len(k.get('x',[]) or []),'m':len(k.get('m',[]) or []),'r':len(k.get('r',[]) or [])}
# --- Processor
_,_,k=kinds['Processor']; old={x['n']:x for x in k['x']}
keep=[]
for nm in CPU_KEEP:
    if nm=='Ryzen Threadripper': continue
    x=copy.deepcopy(old[nm]); x['g']=GO if nm=='Apple M-series' else GI; keep.append(x)
for x in keep:
    if x['n']=='Intel 4004': x['role']='origin'
    if x['n']=='Intel 8086': x['role']='landmark'
k['x']=order(keep+INTEL_NEW+AMD_NEW,[GI,GA,GO])
k['nl']='One entry is a processor microarchitecture or product generation from one maker; the individual models sold on it are versions.'
k['sel']="Intel entries follow Wikipedia's List of Intel CPU microarchitectures (x86 and Atom lines; Itanium, XScale and other non-consumer designs are left out) and the generation mapping in List of Intel Core processors; AMD entries follow List of AMD CPU microarchitectures with release years from List of AMD processors. Sections are by maker, then year."
k['xg']='by maker, then year'
k['r']=[]; k['m']=[]
# --- Graphics card
_,_,k=kinds['Graphics card']; old={x['n']:x for x in k['x']}
v=copy.deepcopy(old['3dfx Voodoo']); v['g']=GOt
k['x']=order(GPU_NEW+[v],[GN,GR,GIn,GOt])
k['nl']='One entry is a consumer graphics architecture or generation from one maker; the cards of its series are versions. Board-partner models are not entries.'
k['sel']="Nvidia generations follow Wikipedia's List of Nvidia graphics processing units and GeForce article, AMD and ATI generations follow List of AMD graphics processing units, Intel follows the Intel Arc article; workstation, data-centre and mobile-only lines are left out."
k['xg']='by maker, then year'
k['r']=[]; k['m']=[]
# --- Home computer
dp,s,k=kinds['Home computer']; _,_,kv=kinds['Vintage desktop computer']
oldx={x['n']:x for x in k['x']+kv['x']}
rowname={}
for n,old_n in MAP.items():
    if old_n: rowname[old_n]=n
new=[]; used=set()
for (n,mk,y) in ROWS:
    if n in SKIP_ROWS: continue
    ex=None
    if n in rowname: ex=oldx[rowname[n]]; used.add(rowname[n])
    if ex:
        e=copy.deepcopy(ex); e['n']=n; e['g']=era(y)
    else:
        dd=(f"{mk} home computer of {y}" if mk else f"Home computer of {y}")+", listed in Wikipedia's List of home computers."
        e=E(n,mk,y,dd,HC,era(y))
    new.append(e)
for nm in EXTRA_EXISTING:
    e=copy.deepcopy(oldx[nm]); e['g']=era('1983'); new.append(e); used.add(nm)
# any other old home-computer entries not in the list stay
for nm,ex in oldx.items():
    if nm in used or nm in ('MITS Altair 8800','Apple Lisa'): continue
    if nm in MAP.values() or nm in MAP: continue
    e=copy.deepcopy(ex); e['g']=era(str(ex.get('y') or '1983')[:4]); new.append(e); print('extra kept',nm)
for e in new:
    if e['n']=='Commodore 64': e['role']='landmark'
    if e['n']=='IBM Personal Computer': e['role']='landmark'
    if e['n']=='Honeywell 316 Kitchen Computer': e['role']='origin'
    if e['n']=='Apple II': e['role']='origin'
k['x']=order(new,['Pioneers (to 1979)','Early 1980s (1980–1982)','Mid 1980s (1983–1985)','Late period (1986 onward)'])
k['nl']='One entry is a home or personal computer platform sold under its own name; revisions and close variants are versions.'
k['sel']="Every row of Wikipedia's List of home computers, grouped by year of introduction (siblings such as the Apple IIe or Atari TT are versions or listed beside their family); the standard MSX is kept as one platform. Sections are by era."
k['xg']='by era'; k['m']=[]
kv['x']=[copy.deepcopy(oldx[n]) for n in ('MITS Altair 8800','Apple Lisa')]
for e in kv['x']: e['g']='Before 1984'
kv['nl']='One entry is a historic desktop microcomputer or business machine that is not a home computer on the Wikipedia list.'
kv['sel']="No whole-space reference exists; the machines on Wikipedia's List of home computers moved to Home computer, and the two remaining entries keep the structure pass's sources."
kv['xg']='by era'
kv['d']='Historic microcomputer or kit-built machine with a separate system unit or built-in screen, outside the home-computer list.'
kv['m']=[]
# --- Keyboard switches
_,_,k=kinds['Keyboard switches']; xs=[]
for x in k['x']:
    x=copy.deepcopy(x); x['g']=KS_GROUP[x['n']]; xs.append(x)
for (n,mk,y,dd,grp,vv) in KS_NEW: xs.append(E(n,mk,y,dd,KD,grp,[]))
mm={tuple(t)[0]:t[1] for t in k['m']}
for (n,mk,dd,grp,names) in KS_MAKER_ENTRIES:
    vv=[V(nm,'','',mk=mk) for nm in names]; assert all(nm in mm for nm in names),n
    xs.append(E(n,mk,'',dd,KD,grp,vv))
for x in xs:
    if x['n']=='Cherry MX': x['role']='landmark'
    if x['n']=='IBM buckling spring': x['role']='origin'
k['x']=order(xs,['Metal-contact mechanical','Buckling spring','Capacitive','Magnetic and optical','Dome and membrane'])
k['nl']='One entry is a keyboard switch family or technology; the colour or model variants sold within it are versions.'
k['sel']="Every switch technology named in Wikipedia's Keyboard technology (membrane, scissor, Cherry MX, Gateron, Kailh, Topre, buckling spring, capacitive, Hall-effect, optical, reed), plus the enthusiast families from the structure pass; loose retail models became versions of their maker's family. Sections are by mechanism."
k['xg']='by mechanism'; k['m']=[]
# --- Laptops
_,_,k=kinds['Laptop']
for x in k['x']: x['g']=LAPTOP_G.get(x['n'],'Other makers')
k['x']=order(k['x'],['IBM and Lenovo','Apple','Toshiba and Dynabook','Panasonic','Dell','HP','ASUS','Razer','Microsoft','Framework'])
k['xg']='by maker'
# --- commodity peripherals: no entries
for nm in ('Mouse','Trackball','Pen tablet','Everyday keyboard','Macro pad','Mouse pad or desk mat'):
    kinds[nm][2]['x']=[]
# --- nl/sel for remaining kinds with entries
NLSEL={
 'Laptop':('One entry is a laptop line from one maker; its generations or models are versions.',"No whole-space reference exists (Wikipedia's list of laptops could not be fetched); entries are the lines named by each maker's Wikipedia article, from the structure pass."),
 'Convertible laptop':('One entry is a convertible laptop line; generations are versions.','No whole-space reference exists; the entry keeps the structure pass source.'),
 'Detachable 2-in-1':('One entry is a detachable 2-in-1 line; generations are versions.','No whole-space reference exists; entries keep the structure pass sources.'),
 'Chromebook':('One entry is a Chromebook line; generations are versions.','No whole-space reference exists; entries keep the structure pass sources.'),
 'Netbook':('One entry is a netbook line; models are versions.','No whole-space reference exists; the entry keeps the structure pass source.'),
 'Tower PC':('One entry is a branded desktop line; generations are versions.','No whole-space reference exists; the entry keeps the structure pass source.'),
 'All-in-one PC':('One entry is an all-in-one line; generations are versions.','No whole-space reference exists; the entry keeps the structure pass source.'),
 'Small-form-factor desktop':('One entry is a business desktop line; generations are versions.','No whole-space reference exists; the entry keeps the structure pass source.'),
 'Mini PC':('One entry is a mini PC line; generations are versions.','No whole-space reference exists; entries keep the structure pass sources.'),
 'Barebone kit':('One entry is a barebone kit line; generations are versions.','No whole-space reference exists; the entry keeps the structure pass source.'),
 'Workstation':('One entry is a workstation line; generations are versions.','No whole-space reference exists; entries keep the structure pass sources.'),
 'Home server':('One entry is a small server line owned at home; generations are versions.','No whole-space reference exists; entries keep the structure pass sources.'),
 'Vintage workstation':('One entry is a vintage workstation line; models are versions.','No whole-space reference exists; entries keep the structure pass sources.'),
 'Luggable & vintage portable':('One entry is a vintage portable computer line; models are versions.','No whole-space reference exists; entries keep the structure pass sources.'),
 'Pocket computer':('One entry is a pocket computer line; models are versions.','No whole-space reference exists; entries keep the structure pass sources.'),
 'Trainer & single-board kit (vintage)':('One entry is a vintage trainer or single-board computer; variants are versions.',"No whole-space reference exists; Wikipedia's List of home computers has a hobby, kit and trainer section (not extended here); entries keep the structure pass sources."),
 'Retro computer re-creation':('One entry is a modern re-creation of an old computer; editions are versions.','No whole-space reference exists; entries keep the structure pass sources.'),
 'CRT monitor':('One entry is a CRT monitor model made for old computers.','No whole-space reference exists; entries keep the structure pass sources.'),
 'Floppy disk drive':('One entry is a floppy drive line for old computers; models are versions.','No whole-space reference exists; entries keep the structure pass sources.'),
 'Sound card':('One entry is a PC sound card line; models are versions.','No whole-space reference exists; entries keep the structure pass sources.'),
 'Video capture device':('One entry is a capture device line; models are versions.','No whole-space reference exists; the entry keeps the structure pass source.'),
 'PC case':('One entry is an enthusiast PC case line; models are versions.','No whole-space reference exists; entries keep the structure pass sources.'),
 'Thermal paste & pads':('One entry is a thermal interface product line.','No whole-space reference exists; the entry keeps the structure pass source.'),
 'CPU air cooler':('One entry is a CPU air cooler line; models are versions.','No whole-space reference exists; entries keep the structure pass sources.'),
 'AIO liquid cooler':('One entry is an all-in-one liquid cooler line; models are versions.','No whole-space reference exists; entries keep the structure pass sources.'),
 'Mechanical keyboard':('One entry is a keyboard line or model family; revisions are versions.','No whole-space reference exists; entries keep the structure pass sources.'),
 'Split & ergonomic keyboard':('One entry is a split or ergonomic keyboard line; revisions are versions.','No whole-space reference exists; entries keep the structure pass sources.'),
 'Keyboard kit':('One entry is a keyboard kit line; revisions are versions.','No whole-space reference exists; entries keep the structure pass sources.'),
 'Keycap set':('One entry is a keycap profile or set family.','No whole-space reference exists; entries keep the structure pass sources.'),
 'Label printer':('One entry is a label printer line.','No whole-space reference exists; the entry keeps the structure pass source.'),
 '3D printer':('One entry is a 3D printer line or open design; models are versions.','No whole-space reference exists; entries keep the structure pass sources.'),
 '3D-printer upgrade parts':('One entry is a hot-end or upgrade part line.','No whole-space reference exists; the entry keeps the structure pass source.'),
 'Security key':('One entry is a security key line; models are versions.','No whole-space reference exists; entries keep the structure pass sources.'),
 'Hardware wallet':('One entry is a hardware wallet line; models are versions.','No whole-space reference exists; entries keep the structure pass sources.'),
 'Single-board computer':('One entry is a single-board computer family; boards are versions.','No whole-space reference exists; entries keep the structure pass sources.'),
 'Microcontroller board':('One entry is a microcontroller board family; boards are versions.','No whole-space reference exists; entries keep the structure pass sources.'),
 'Maker add-on board':('One entry is an add-on board standard; boards are versions.','No whole-space reference exists; entries keep the structure pass sources.'),
}
for n,(dp,s,k) in kinds.items():
    if n in NLSEL and k.get('x'):
        k['nl'],k['sel']=NLSEL[n]
    elif k.get('x') and not k.get('nl'): raise SystemExit('missing nl '+n)
# --- clear remaining loose models
for n,(dp,s,k) in kinds.items():
    if k.get('m'):
        stats[n]['m_removed']=len(k['m']); k['m']=[]
# --- market summaries
G='https://www.gartner.com/en/newsroom/press-releases/2026-4-10-gartner-says-worldwide-pc-shipments-increased-4-percent-in-first-quarter-of-2026'
ID='https://9to5mac.com/2026/10/08/idc-mac-shipments-drop-11-in-q3-as-global-pc-market-slides-20/'
MR='https://www.techspot.com/news/113569-amd-crosses-30-client-cpu-market-share-against.html'
JP='https://pbxscience.com/nvidia-dominates-90-q2-desktop-graphics-card-shipments-reach-12-5-million-units-amd-only-8/'
def ms(mkt,who,share,y,s,note): return {"mkt":mkt,"who":who,"share":share,"yr":y,"s":s,"note":note}
dep={x['n']:x for x in d['depts']}
dep['Computers']['ms']=[ms('Worldwide PC shipments, Q1 2026 (Gartner)',w,sh,2026,G,'units shipped, preliminary') for w,sh in [('Lenovo','26.5 %'),('HP Inc.','19.3 %'),('Dell','16.5 %'),('Apple','10.6 %'),('ASUS','6.7 %'),('Acer','6.4 %')]]+\
 [ms('Worldwide PC shipments, Q3 2026 (IDC)',w,sh,2026,ID,'units shipped, preliminary') for w,sh in [('Lenovo','23.8 %'),('HP','16.5 %'),('Dell','12.1 %'),('Apple','9.5 %'),('ASUS','8.7 %')]]
dep['PC components']['ms']=[
 ms('x86 client processors, Q2 2026 (Mercury Research)','Intel','69.7 %',2026,MR,'share of client CPU shipments'),
 ms('x86 client processors, Q2 2026 (Mercury Research)','AMD','30.3 %',2026,MR,'share of client CPU shipments'),
 ms('Desktop graphics cards, Q2 2026 (Jon Peddie Research)','Nvidia','about 90 %',2026,JP,'add-in-board shipments, 12.5 million units, as reported by a secondary page'),
 ms('Desktop graphics cards, Q2 2026 (Jon Peddie Research)','AMD','about 8 %',2026,JP,'add-in-board shipments, as reported by a secondary page'),
 ms('Desktop graphics cards, Q2 2026 (Jon Peddie Research)','Intel','about 2 %',2026,JP,'add-in-board shipments, as reported by a secondary page')]
# stats after
for n,(dp_,s,k) in kinds.items(): stats[n]['after_x']=len(k.get('x',[]) or [])
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P)
json.dump(stats,open('/home/user/Possession-Taxonomy/rebuild/work/V4_D1/stats.json','w'),indent=1)
# brands
bp='/home/user/Possession-Taxonomy/rebuild/out/D1_brands.json'
br=json.load(open('/home/user/Possession-Taxonomy/rebuild/work/V4_D1/bak/D1_brands.json'))
have={b['n'].lower() for b in br['b']}
mks=set()
def walk(x):
    for e in x:
        mks.add(e.get('mk','')); 
        for v in e.get('v',[]): mks.add(v.get('mk',''))
for n,(dp_,s,k) in kinds.items(): walk(k.get('x',[]) or [])
newb=[m for m in sorted(mks) if m and m.lower() not in have]
print('new brands',newb)
for m in newb: br['b'].append({"n":m,"c":"","f":"","d":"","s":""})
json.dump(br,open(bp+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(bp+'.tmp',bp)
