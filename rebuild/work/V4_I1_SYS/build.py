# -*- coding: utf-8 -*-
import json,re,copy,sys,os
sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/V4_I1_SYS')
from data1 import *
from data2 import *
from data3 import WLIN
R='/home/user/Possession-Taxonomy/rebuild/'
old=json.load(open(R+'out/I1.json'))
NAMES=['Operating systems & system tools','Security & privacy','Office & productivity','Internet & AI','Developer tools','Classic software']
depts=[copy.deepcopy(d) for d in old['depts'] if d['n'] in NAMES]
assert len(depts)==6
def norm(s):
    s=s.lower().replace('\\_','_')
    s=re.sub(r'\(.*?\)','',s); s=re.sub(r'[^a-z0-9]','',s)
    for suf in ('linux','os'):
        if s.endswith(suf) and len(s)>len(suf)+2: s=s[:-len(suf)]
    return s
ALIASN={'lfs':'linuxfromscratch','netscapenavigatorv14':'netscapenavigator'}
def nk(s):
    k=norm(s); return ALIASN.get(k,k)
# ---------- market ----------
GLOBAL={'Microsoft','Apple','Google','Adobe','Oracle','IBM','Amazon','Meta AI','Gen Digital','Broadcom','Cisco','Symantec'}
OWNOV=[('Norton','Gen Digital'),('Avast','Gen Digital'),('AVG','Gen Digital'),('Avira','Gen Digital'),('CCleaner','Gen Digital'),('VMware','Broadcom'),('Piriform','Gen Digital'),('Symantec','Gen Digital')]
NC={'Yandex':'Russia','Kaspersky':'Russia','Doctor Web':'Russia','Baidu':'China','Tencent':'China','Alibaba Group':'China','Kingsoft':'China','Qihoo 360':'China','Hancom':'South Korea','Naver Corporation':'South Korea','Huawei':'China','Xiaomi':'China','Oppo':'China','Sberbank':'Russia','ByteDance':'China','Moonshot AI':'China','Z.ai':'China','Trend Micro':'Japan','AhnLab':'South Korea','Quick Heal':'India','Zoho':'India','Zoho Corp.':'India','Samsung Electronics':'South Korea','Samsung':'South Korea','INCA Internet':'South Korea','Meizu':'China'}
CTY={'Microsoft':'United States','Apple':'United States','Google':'United States','Adobe':'United States','Oracle':'United States','IBM':'United States','Amazon':'United States','Meta AI':'United States','Gen Digital':'United States','Broadcom':'United States','Cisco':'United States','Symantec':'United States','Mozilla':'United States','Mozilla Foundation':'United States','Brave Software':'United States','Opera Software':'Norway','Vivaldi Technologies':'Norway','OpenAI':'United States','Anthropic':'United States','xAI':'United States','Perplexity':'United States','Canonical':'United Kingdom','Red Hat':'United States','SUSE':'Germany','Bitdefender':'Romania','ESET':'Slovakia','F-Secure':'Finland','G Data CyberDefense':'Germany','Sophos':'United Kingdom','Panda Security':'Spain','Malwarebytes':'United States','McAfee':'United States','Avira':'Germany','Proton':'Switzerland','Proton AG':'Switzerland','JetBrains':'Czechia','Mullvad':'Sweden','SoftMaker':'Germany','Corel':'Canada','Dropbox':'United States','Evernote Corporation':'United States','Mistral AI':'France','DeepSeek':'China','Notion Labs':'United States','Intego':'United States','Check Point':'Israel','Webroot':'United States','Comodo Group':'United States','Cylance':'United States','Parallels':'United States','Parallels, Inc.':'United States','Embarcadero Technologies':'United States','Wingware':'United States','Cincom':'United States'}
CTY.update(NC)
def mkt(e):
    mk=e.get('mk','')
    if not mk: return
    own=mk
    for pre,o in OWNOV:
        if e['n'].startswith(pre) or mk.startswith(pre): own=o;break
    if own not in GLOBAL and own not in NC and mk not in CTY and own not in CTY: return
    e['own']=own
    e['tier']='Global group' if own in GLOBAL else ('National champion' if (own in NC or mk in NC) else 'Independent')
    c=CTY.get(mk) or CTY.get(own)
    if c: e['cty']=c
NOUN=lambda k:k
def conv(name,mk,kind,src,y='',g=None,d=None):
    e={'n':name,'a':'','d':d or ((f"{kind} by {mk}." if mk else f"{kind}.")),'mk':mk,'y':y,'s':src,'v':[]}
    if g: e['g']=g
    return e
def pad(d):
    return d if d.endswith('.') else d+'.'
seen_global=set()   # per-dept dedupe set filled lazily
dropped=[]; report={}
def cov(kind,n_before,n_after,ref):
    report[kind]=(n_before,n_after,ref)
def dept_seen(dept):
    s=set()
    for sh in dept['s']:
        for k in sh['k']:
            for e in k.get('x',[]): s.add(nk(e['n'])); [s.add(nk(a)) for a in e.get('a','').split('·') if a.strip()]
    return s
SPECIAL_REMOVE={'Debian lineage','Red Hat and Fedora lineage','Arch lineage','openSUSE lineage','Mandriva lineage','Gentoo lineage','OS/2 continuations','Microsoft Plus! savers','Windows built-in savers','Visual Studio Code extensions','JetBrains Marketplace plug-ins','Windows built-in savers'}
def do_dept(d,fn):
    sn=dept_seen(d)
    for sh in d['s']:
        for k in sh['k']:
            fn(d,sh,k,sn)
def take_m(k,sn,d_noun=None,g=None):
    """convert m and r lists to entries; dedupe across dept."""
    out=[]
    for key in ('m','r'):
        for t in k.get(key,[]) or []:
            name,mk=t
            if name in SPECIAL_REMOVE:
                dropped.append((k['n'],name,'family or group label, not a product'));continue
            if nk(name) in sn:
                dropped.append((k['n'],name,'already an entry in another kind of the department')); continue
            sn.add(nk(name))
            out.append(conv(name,mk,d_noun or k['n'],k.get('s','')))
        k.pop(key,None)
    return out
def addnew(k,sn,rows,src,kind_noun,sectionf=None,yidx=True,alias=None,skipdup=True):
    """rows: tuples (n,mk,y,sec). returns list of entries added"""
    out=[];n_skip=0
    for r in rows:
        n,mk,y,sec=(list(r)+['']*4)[:4]
        name=(alias or {}).get(n,n)
        if nk(name) in sn:
            n_skip+=1; continue
        sn.add(nk(name))
        e=conv(name,mk,kind_noun,src,y)
        e['d']=pad(e['d']) 
        if sec or sectionf: e['g']=sectionf(sec) if sectionf else sec
        out.append(e)
    return out,n_skip
def fill_y(e,y):
    if y and not e.get('y'): e['y']=y
# ---------- spec for sel/nl ----------
NL={}; 
def setk(k,nl,sel,xg=None):
    k['nl']=nl; k['sel']=sel
    if xg: k['xg']=xg
def finalize_kind(k, ref_text, cov_text, nl, xg=None, extra_fix=None):
    for e in k.get('x',[]):
        mkt(e)
    setk(k,nl,ref_text+' '+cov_text,xg)
SQ=lambda ent:len(ent)
MS={}
nonlinux_dw={'FreeBSD','OpenBSD','NetBSD','DragonFly','GhostBSD','MidnightBSD','HardenedBSD','OpenIndiana','OmniOS','Tribblix','SmartOS','Solaris','ReactOS','Redox','KolibriOS','ToaruOS','Haiku','Sculpt','GrapheneOS','CalyxOS','Murena','iodéOS','Plop'}
DWDISP={'Mint':'Linux Mint','Zorin':'Zorin OS','Rocky':'Rocky Linux','Oracle':'Oracle Linux','Pop!_OS':'Pop!_OS','elementary':'elementary OS','Tiny Core':'Tiny Core Linux','Puppy':'Puppy Linux','Void':'Void Linux','Arch':'Arch Linux','Gentoo':'Gentoo Linux','Alpine':'Alpine Linux','Kali':'Kali Linux','Ubuntu':'Ubuntu','Mageia':'Mageia','LFS':'Linux From Scratch','Debian':'Debian','Fedora':'Fedora','Red Hat':'Red Hat Enterprise Linux','SUSE':'SUSE Linux Enterprise','deepin':'Deepin','Deepin':'Deepin','Chimera':'Chimera Linux','Solus':'Solus','Guix System':'Guix System','CRUX':'CRUX','Source Mage':'Source Mage','GoboLinux':'GoboLinux'}
dw=json.load(open(R+'work/V4_I1_SYS/dw12.json'))
DW=[(int(rk),n.replace('\\_','_'),b or '') for rk,n,slug,b,h in dw]
DWHITS={n.replace('\\_','_'):int(h) for rk,n,slug,b,h in dw}

# ================= main =================
D={d['n']:d for d in depts}
def kind(dn,kn):
    for sh in D[dn]['s']:
        for k in sh['k']:
            if k['n']==kn: return sh,k
    raise KeyError(kn)
def newkind(dn,shelf,k,after=None):
    sh=[s for s in D[dn]['s'] if s['n']==shelf][0]
    sh['k'].append(k); return k
SN={dn:dept_seen(D[dn]) for dn in D}
CNT={}
def sect_order(entries):
    pass
OS='Operating systems & system tools'; SEC='Security & privacy'; OFF='Office & productivity'; NET='Internet & AI'; DEV='Developer tools'; CLS='Classic software'
# step A: convert every m/r into entries (dedupe)
for dn,d in D.items():
    for sh in d['s']:
        for k in sh['k']:
            k['_before']=len(k.get('x',[]) or [])
            k['_mcount']=len(k.get('m',[]) or [])+len(k.get('r',[]) or [])
            if k.get('m') or k.get('r'):
                add=take_m(k,SN[dn])
                k.setdefault('x',[]).extend(add)
# step B: kind-specific additions
def kx(dn,kn): return kind(dn,kn)[1]
# --- Linux distributions ---
k=kx(OS,'Linux distribution'); sn=SN[OS]
def famtok(b):
    t=(b or 'Independent').split(',')[0].split('(')[0].strip(); return t or 'Independent'
fams={}
for rk,n,b in DW: fams[famtok(b)]=fams.get(famtok(b),0)+1
def famlabel(b):
    t=famtok(b)
    if t=='Independent': return 'Independent (DistroWatch)'
    return f'{t} family' if fams[t]>=3 else 'Other families'
FREEBSD_TOK={'FreeBSD','OpenBSD','OpenSolaris','Solaris','Haiku'}
dwdisp=lambda n: DWDISP.get(n,n)
moved_dw=[]
existing={nk(e['n']):e for e in k['x']}
to_alt=[]; to_mobile=[]
newlin=[]
for rk,n,b in DW:
    tok=famtok(b); disp=dwdisp(n)
    if n in ('GrapheneOS','CalyxOS','Murena','iodéOS'):
        to_mobile.append((rk,n,b)); continue
    if n in nonlinux_dw or tok in FREEBSD_TOK:
        to_alt.append((rk,disp,b)); continue
    key=nk(disp)
    based=b if b else 'not stated'
    if key in existing:
        e=existing[key]; e['g']=famlabel(b); e.setdefault('dt','')
        continue
    if key in sn:  # converted earlier from m
        pass
    sn.add(key)
    newlin.append({'n':disp,'a':'','d':f"Free operating system ranked {rk} by DistroWatch page hits over the last 12 months; based on {based}.",'mk':'','y':'','s':SRC['dw'],'v':[],'g':famlabel(b),'_rk':rk})
# entries converted from m: give family if in DW
for e in k['x']:
    if 'g' in e: continue
    key=nk(e['n'])
    for rk,n,b in DW:
        if nk(dwdisp(n))==key:
            e['g']=famlabel(b); e['d']=f"Free operating system ranked {rk} by DistroWatch page hits over the last 12 months; based on {b or 'not stated'}."; e['s']=SRC['dw']; break
    else:
        e['g']='Not in DistroWatch ranking'
k['x'].extend(newlin)
# Wikipedia-only
wcount=0
for head,names in WLIN.items():
    for n in names.split('|'):
        key=nk(n)
        if key in sn or key in {nk(dwdisp(x[1])) for x in DW}: continue
        sn.add(key); wcount+=1
        k['x'].append({'n':n,'a':'','d':f"Listed in Wikipedia's List of Linux distributions under {head}; not in DistroWatch's current 12-month ranking.",'mk':'','y':'','s':SRC['linux'],'v':[],'g':'Wikipedia list only'})
# Ubuntu entry with versions
ub=[e for e in k['x'] if e['n']=='Ubuntu'][0]
ub['mk']='Canonical'; ub['y']='2004'; ub['s']=SRC['ubuntu']
ub['d']='Debian-based desktop and server distribution from Canonical, released every April and October; ranked by DistroWatch page hits.'
UB='''4.10 Warty Warthog|20 October 2004
5.04 Hoary Hedgehog|8 April 2005
5.10 Breezy Badger|12 October 2005
6.06 LTS Dapper Drake|1 June 2006
6.10 Edgy Eft|26 October 2006
7.04 Feisty Fawn|19 April 2007
7.10 Gutsy Gibbon|18 October 2007
8.04 LTS Hardy Heron|24 April 2008
8.10 Intrepid Ibex|30 October 2008
9.04 Jaunty Jackalope|23 April 2009
9.10 Karmic Koala|29 October 2009
10.04 LTS Lucid Lynx|29 April 2010
10.10 Maverick Meerkat|10 October 2010
11.04 Natty Narwhal|28 April 2011
11.10 Oneiric Ocelot|13 October 2011
12.04 LTS Precise Pangolin|26 April 2012
12.10 Quantal Quetzal|18 October 2012
13.04 Raring Ringtail|25 April 2013
13.10 Saucy Salamander|17 October 2013
14.04 LTS Trusty Tahr|17 April 2014
14.10 Utopic Unicorn|23 October 2014
15.04 Vivid Vervet|23 April 2015
15.10 Wily Werewolf|22 October 2015
16.04 LTS Xenial Xerus|21 April 2016
16.10 Yakkety Yak|13 October 2016
17.04 Zesty Zapus|13 April 2017
17.10 Artful Aardvark|19 October 2017
18.04 LTS Bionic Beaver|26 April 2018
18.10 Cosmic Cuttlefish|18 October 2018
19.04 Disco Dingo|18 April 2019
19.10 Eoan Ermine|17 October 2019
20.04 LTS Focal Fossa|23 April 2020
20.10 Groovy Gorilla|22 October 2020
21.04 Hirsute Hippo|22 April 2021
22.04 LTS Jammy Jellyfish|April 2022
24.04 LTS Noble Numbat|April 2024
26.04 LTS Resolute Raccoon|April 2026'''
ub['v']=[{'n':'Ubuntu '+a,'mk':'Canonical','y':b.split()[-1],'d':'released '+b} for a,b in (l.split('|') for l in UB.split('\n'))]
k['x'].sort(key=lambda e:(e.get('_rk',0) if e.get('_rk') else 99999))
GORD=sorted({e['g'] for e in k['x']},key=lambda g:(g=='Wikipedia list only',g=='Not in DistroWatch ranking',g=='Other families',-sum(1 for e in k['x'] if e['g']==g)))
k['x'].sort(key=lambda e:(GORD.index(e['g']),e.get('_rk',99999)))
for e in k['x']: e.pop('_rk',None)
dw_in_linux=len(DW)-len(to_alt)-len(to_mobile)
# --- Alternative OS ---
k=kx(OS,'Alternative & hobby operating system'); sn=SN[OS]
for e in k['x']:
    if 'g' not in e:
        e['g']={'FreeBSD':'Unix and BSD','Haiku':'Hobby and research','RISC OS':'Amiga, Atari and Acorn lines','OS/2':'OS/2 lines','AmigaOS':'Amiga, Atari and Acorn lines','ReactOS':'Hobby and research','SerenityOS':'Hobby and research','FreeDOS':'DOS family'}.get(e['n'],'Hobby and research')
add,_=addnew(k,sn,ALTOS,SRC['os'],'Operating system')
k['x'].extend(add)
for rk,disp,b in to_alt:
    if nk(disp) in sn: 
        continue
    sn.add(nk(disp))
    k['x'].append({'n':disp,'a':'','d':f"Free Unix-like system ranked {rk} by DistroWatch page hits over the last 12 months; based on {b or 'not stated'}.",'mk':'','y':'','s':SRC['dw'],'v':[],'g':'Unix and BSD'})
ORD=['Unix and BSD','Commercial Unix','DOS family','Amiga, Atari and Acorn lines','OS/2 lines','Hobby and research']
k['x'].sort(key=lambda e:ORD.index(e['g']))
# --- Mobile OS kind ---
mk_=newkind(OS,'Operating systems',{'n':'Mobile operating system','a':'phone OS · tablet OS · wearable OS','d':'Operating system that runs a phone, tablet, watch or TV box, including custom Android builds that replace the maker\'s system.','s':SRC['os'],'tt':[['Basis',['Android','Linux','Proprietary']],['Device',['Phone','Tablet','Watch','TV']]],'see':[['D2','Smartphone','the handset']],'x':[]})
add,_=addnew(mk_,sn,MOBILE,SRC['os'],'Operating system')
mk_['x'].extend(add)
for rk,n,b in to_mobile:
    if n=='iodéOS': mk_['x'].append({'n':n,'a':'','d':'Android-based privacy system ranked by DistroWatch page hits.','mk':'','y':'','s':SRC['dw'],'v':[],'g':'Custom Android builds'})
mobord=['Phone and tablet systems','Android manufacturer skins','Custom Android builds','Wearables, TV and other devices','Retired systems']
mk_['x'].sort(key=lambda e:mobord.index(e['g']))
MY={'ChatGPT':'2022','Claude':'2023'}
# --- virtual machines ---
k=kx(OS,'Virtual machine software'); sn=SN[OS]
add,_=addnew(k,sn,VIRT,SRC['virt'],'Virtual machine software'); k['x'].extend(add)
# --- Office ---
k=kx(OFF,'Office suite'); sn=SN[OFF]
add,_=addnew(k,sn,OFFICE,SRC['office'],'Office suite'); k['x'].extend(add)
lo=[e for e in k['x'] if e['n']=='LibreOffice'][0]
LO='''3.3|25 January 2011
3.4|3 June 2011
3.5|14 February 2012
3.6|8 August 2012
4.0|7 February 2013
4.1|25 July 2013
4.2|30 January 2014
4.3|30 July 2014
4.4|29 January 2015
5.0|5 August 2015
5.1|10 February 2016
5.2|3 August 2016
5.3|1 February 2017
5.4|28 July 2017
6.0|31 January 2018
6.1|8 August 2018
6.2|7 February 2019
6.3|8 August 2019
6.4|29 January 2020
7.0|5 August 2020
7.1|3 February 2021
7.2|19 August 2021
7.3|3 February 2022
7.4|18 August 2022
7.5|2 February 2023'''
lo['v']=lo.get('v',[])+[{'n':'LibreOffice '+a,'mk':'The Document Foundation','y':b.split()[-1],'d':'released '+b} for a,b in (l.split('|') for l in LO.split('\n'))]
lo['s']=SRC['libreoffice']
# --- Password managers, VPN ---
k=kx(SEC,'Password manager'); add,_=addnew(k,SN[SEC],PW,SRC['pw'],'Password manager'); k['x'].extend(add)
k=kx(SEC,'VPN'); add,_=addnew(k,SN[SEC],VPN,SRC['vpn'],'VPN service'); k['x'].extend(add)
# --- Antivirus ---
k=kx(SEC,'Antivirus software'); k.pop('r',None)
for e in k['x']: e['g']='Current'
add,_=addnew(k,SN[SEC],[r for r in AV if r[0] not in ('Avira',)],SRC['av'],'Antivirus software'); 
for e in add: e['g']=[r for r in AV if r[0]==e['n']][0][3].strip()
k['x'].extend(add)
k['x'].sort(key=lambda e:e['g']!='Current')
# --- browsers ---
k=kx(NET,'Web browser'); sn=SN[NET]
for e in k['x']:
    e['g']='Retired' if e['n'] in ('Internet Explorer','Netscape Navigator') else 'Current'
add,_=addnew(k,sn,BROWSERS,SRC['browsers'],'Web browser',alias=BROWSER_ALIAS); k['x'].extend(add)
k['x'].sort(key=lambda e:e['g']!='Current')
for e in k['x']:
    if e['n']=='Mosaic': e['mk']='NCSA'
# --- email, torrent, download ---
k=kx(NET,'Email client'); add,_=addnew(k,SN[NET],MAIL,SRC['mail'],'Email client'); k['x'].extend(add)
k=kx(NET,'BitTorrent client'); add,_=addnew(k,SN[NET],BT,SRC['bt'],'BitTorrent client'); k['x'].extend(add)
k=kx(OS,'File archiver'); add,_=addnew(k,SN[OS],ARCH,SRC['arch'],'File archiver'); k['x'].extend(add)
k=kx(OFF,'Note-taking app'); add,_=addnew(k,SN[OFF],NOTES,SRC['notes'],'Note-taking app'); k['x'].extend(add)
# --- AI assistants ---
k=kx(NET,'AI assistant'); sn=SN[NET]
VOICE={'Siri','Alexa','Google Assistant'}
CY={'ChatGPT':'2022','Gemini':'2023','Claude':'2023','Microsoft Copilot':'2023','Meta AI':'2023','Grok':'2023','DeepSeek':'2025','Doubao':'2023','Qwen':'2023','Siri':'2011','Google Assistant':'2016','Alexa':'2014'}
CMK={'ChatGPT':'OpenAI','Gemini':'Google','Claude':'Anthropic','Microsoft Copilot':'Microsoft','Meta AI':'Meta AI','Grok':'xAI','DeepSeek':'DeepSeek','Doubao':'ByteDance','Qwen':'Alibaba Group','Siri':'Apple','Alexa':'Amazon','Google Assistant':'Google'}
for e in k['x']:
    e['g']='Voice and general assistants' if e['n'] in VOICE else 'Large-language-model assistants'
    e['y']=CY.get(e['n'],e['y']); e['mk']=CMK.get(e['n'],e['mk']); e['s']=SRC['chat']
    e['d']=f"{e['g'][:-1] if False else 'Assistant'} from {e['mk']}, first released {e['y']}." 
add,_=addnew(k,sn,[(a,b,c,'Large-language-model assistants') for a,b,c,_x in CHAT_LLM],SRC['chat'],'Assistant'); k['x'].extend(add)
add,_=addnew(k,sn,[(a,b,c,'Voice and general assistants') for a,b,c,_x in CHAT_GEN],SRC['chat'],'Assistant',alias={'Amazon Alexa':'Alexa'}); k['x'].extend(add)
for e in k['x']:
    if e['y'] and e['mk']: e['d']=f"Assistant from {e['mk']}, first released {e['y']}."
k['x'].sort(key=lambda e:e['g']!='Large-language-model assistants')
newkind(NET,'AI assistants & agents',{'n':'Local AI model runner','a':'local LLM runner','d':'Program that downloads open-weight language models and runs them on the owner\'s own computer.','s':SRC['chat'],'tt':[['Interface',['Desktop app','Command line','Server']],['Hardware',['CPU','GPU']]],'x':[conv(n,mk,'Local model runner',SRC['chat']) for n,mk,_a,_b in LOCAL_RUNNERS]})
# --- IDE / editors ---
k=kx(DEV,'Code editor'); sn=SN[DEV]
for e in k['x']:
    if e['n']=='JetBrains IDEs':
        have={v['n'] for v in e.get('v',[])}
        e['v']=e.get('v',[])+[{'n':n,'mk':'JetBrains','d':'listed in the IDE comparison'} for n in JB_VERS if n not in have]
    if e['n']=='Eclipse':
        pass
for e in k['x']:
    if e['n']=='Eclipse':
        e['v']=e.get('v',[])+[{'n':n,'mk':'Eclipse Foundation','d':'language package listed in the IDE comparison'} for n in ECL_VERS]
ide_rows=[(a,b,'','') for a,b,_c,_d in IDE]
add,_=addnew(k,sn,ide_rows,SRC['ide'],'Development environment'); k['x'].extend(add)
for e in k['x']:
    if e['n']=='MonoDevelop': e['v']=[{'n':'Xamarin Studio','mk':'Microsoft','d':'successor name listed in the IDE comparison'}]
newte=newkind(DEV,'Writing & building code',{'n':'Text editor','a':'programmer\'s editor','d':'General-purpose editor for plain text and source code, from vi and Emacs to Notepad++, that has no project build system of its own.','s':SRC['te'],'tt':[['Interface',['Graphical','Terminal']],['Extension',['Plug-ins','Scripting','None']]],'x':[]})
add,_=addnew(newte,sn,[(a,b,c,'') for a,b,c,_d in TEXTED],SRC['te'],'Text editor'); newte['x'].extend(add)
for e in newte['x']: e['d']=f"Text editor by {e['mk']}, {e['y']}." if e['mk'] and e['y'] else (f"Text editor by {e['mk']}." if e['mk'] else 'Text editor.')
# --- Classic software ---
sh=[s for s in D[CLS]['s']][0]
for kn,rows,desc,srcs in [
 ('Classic word processor',CL_WP,'Word processor from the 1970s to 1990s, run on CP/M, DOS and early Mac or Apple machines.','hos'),
 ('Classic spreadsheet or database',CL_SS,'Spreadsheet or database program from the 1970s to 1990s that set up the early business use of personal computers.','hos'),
 ('Classic office suite',CL_SUITE,'Integrated or bundled office program from the 1980s to 2000s that has since been discontinued.','disc'),
 ('Classic graphics and publishing program',CL_GFX,'Paint, drawing or desktop-publishing program from early Mac, Apple and PC systems that has been discontinued.','disc'),
 ('Classic utility',CL_UTIL,'Disk, file, terminal or security utility from the DOS, Windows and early Mac era that has been discontinued.','disc'),
 ('Classic internet software',CL_NET,'Browser, web editor, server, chat or file-sharing program from the early web that has been discontinued.','disc')]:
    kk={'n':kn,'a':'','d':desc,'s':SRC[srcs],'tt':[['Platform',['CP/M','DOS','Classic Mac OS','Windows','Apple II']],['Condition',['Loose disks','Boxed','Sealed']]],'x':[]}
    sh['k'].append(kk)
    add,_=addnew(kk,SN[CLS],[(a,b,c,'') for a,b,c in rows] if len(rows[0])==3 else rows,SRC[srcs],kn)
    kk['x'].extend(add)
    for e in kk['x']:
        if not e['mk'] and not e['y']: e['d']='Discontinued program named in Wikipedia\'s Category:Discontinued software.' if srcs=='disc' else 'Early program named in Wikipedia\'s History of software.'
        elif srcs=='hos' and e['y']: e['d']=f"Early program, {e['y']}, named in Wikipedia's History of software."
        elif not e['y'] or not e['mk']: e['d']=(f"Discontinued program by {e['mk']}." if e['mk'] else 'Discontinued program.')
