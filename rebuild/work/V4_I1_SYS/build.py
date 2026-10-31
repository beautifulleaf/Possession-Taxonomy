# -*- coding: utf-8 -*-
import json,re,copy,sys,os
sys.path.insert(0,os.path.dirname(__file__))
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
