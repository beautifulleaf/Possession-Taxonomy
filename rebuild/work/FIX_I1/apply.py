import json,re,copy,os
P='out/I1.json'
d=json.load(open(P)); br=json.load(open('out/I1_brands.json'))
K={}
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']: K[k['n']]=(dp,s,k)
cnt0=(sum(len(s['k']) for dp in d['depts'] for s in dp['s']),sum(len(k.get('x',[])) for _,_,k in K.values()))
log=[]
# 1/2 dissolve catch-alls
pat=re.compile(r'^(independent distributions|other saturators|other repair tools|mastering chains from other makers|modular and ai strips|vocal effects and suites|tape plug-ins|character delays|dynamic eq plug-ins|single-game mod managers|multi-network clients)$|emulators$',re.I)
for n,(dp,s,k) in K.items():
  keep=[];m=k.setdefault('m',[]);have={x[0] for x in m}
  for a in k.get('x',[]):
    if pat.search(a['n']):
      for v in a.get('v',[]):
        if v['n'] not in have: m.append([v['n'],v.get('mk','')]);have.add(v['n'])
      log.append('dissolved '+a['n'])
    else: keep.append(a)
  if 'x' in k: k['x']=keep
  if not m: del k['m']
# Arch/Mandriva mk
for a in K['Linux distribution'][2]['x']:
  if a['n']=='Arch lineage': a['mk']='Arch Linux'
  if a['n']=='Mandriva lineage': a['mk']='Mandriva'
  if a['n']=='Slackware lineage': pass
ldv={a['n']:[v['n'] for v in a.get('v',[])] for a in K['Linux distribution'][2]['x']}
print({k:[x for x in v if x in('Ubuntu','Linux Mint','Fedora Linux','Fedora')] for k,v in ldv.items()})
# 3 trim
def trim(n,keep):
  k=K[n][2]; mm={x[0]:x for x in k['m']}
  k['m']=[mm[x] for x in keep if x in mm]
  assert len(k['m'])==len(keep),(n,[x for x in keep if x not in mm])
trim('File manager',['File Explorer','Finder','Files by Google','Total Commander','Directory Opus','XYplorer','Dolphin','Midnight Commander'])
trim('Terminal emulator',['Windows Terminal','Terminal.app','iTerm2','GNOME Terminal','Konsole','Alacritty','kitty','WezTerm'])
trim('AI coding assistant',['Tabnine','Amazon Q Developer','Cline','Aider','Continue','Zed Agent','Devin','Sourcegraph Cody','Google Antigravity'])
trim('Code editor plug-in',['ESLint','Prettier','GitLens','Live Server','IdeaVim','SonarLint','Error Lens','Gemini Code Assist'])
trim('Backup software',['Time Machine','Windows Backup and Restore','Acronis True Image','Macrium Reflect','Carbon Copy Cloner','Retrospect','Clonezilla','Restic','BorgBackup'])
# fill obvious makers from the entry itself where the maker is the product name's own company
for n,fix in {'Backup software':{'Carbon Copy Cloner':'Bombich Software'}}.items():
  for x in K[n][2]['m']:
    if x[0] in fix and not x[1]: x[1]=fix[x[0]]
# 4 merges
def merge(dst,src,tname,take):
  D=K[dst][2];S=K[src][2]
  D.setdefault('t',[]).append(tname)
  have={x[0] for x in D.get('m',[])}
  for x in S.get('m',[])[:take]:
    if x[0] not in have: D.setdefault('m',[]).append(x);have.add(x[0])
  if S.get('a'): D['a']=(D.get('a','')+' · '+S['a']).strip(' ·')
  sh=K[src][1]; sh['k']=[k for k in sh['k'] if k['n']!=src]
  log.append(f'merged {src} into {dst}')
for src,tn in [('Word processor','word processor'),('Spreadsheet software','spreadsheet'),('Presentation software','presentation')]:
  merge('Office suite',src,tn,3)
merge('Media player','Music player','music player',6)
K['Media player'][2]['m']=K['Media player'][2]['m'][:6]+[x for x in K['Media player'][2]['m'][6:]] 
D=K['Media player'][2]; D['m']=[x for x in D['m'] if True]
trim_ok=None
merge('Screen recorder and streaming software','Screenshot tool','screenshot tool',4)
D=K['Screen recorder and streaming software'][2]; D['m']=D['m'][:8]+[x for x in D['m'][8:] if x[0] in('Snipping Tool','Snagit','Greenshot','CleanShot X')]
merge('Diagramming software','Online whiteboard','online whiteboard',3)
# media player m cap
D=K['Media player'][2]; D['m']=[x for x in D['m'] if x[0] in('VLC media player','Windows Media Player','QuickTime','Kodi','mpv','Plex Media Player','PotPlayer','iTunes','Winamp','foobar2000','MusicBee','AIMP')]
# out of scope
for n in ['Computer-assisted translation tool','Accounting software','Survey and form software','Show-control software']:
  k=K[n][2]; k.pop('m',None); k.pop('x',None); log.append('bare '+n)
sc=K['Scientific and statistics software'][2]
sc['x']=[a for a in sc['x'] if a['n'] not in('SPSS','Stata')]
sc['m']=[x for x in sc['m'] if x[0] not in('SAS','JMP','Minitab')]
json.dump(d,open('work/FIX_I1/stage1.json','w'),ensure_ascii=False,indent=1)
print(log)
