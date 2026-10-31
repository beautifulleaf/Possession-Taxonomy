import json,re
d=json.load(open('work/FIX_I1/stage1.json')); br=json.load(open('out/I1_brands.json'))
W='https://en.wikipedia.org/wiki/'
def A(n,mk,y,dd,s,a='',dt=''):
  r={'n':n,'a':a,'d':dd,'mk':mk,'y':y,'s':W+s}
  if dt: r['dt']=dt
  return r
def find(dn,sn=None):
  dp=[x for x in d['depts'] if x['n']==dn][0]
  if sn is None: return dp
  return [s for s in dp['s'] if s['n']==sn][0]
def shelf(dn,sn):
  dp=find(dn)
  for s in dp['s']:
    if s['n']==sn: return s
  s={'n':sn,'k':[]};dp['s'].append(s);return s
tr_src=W+'Tracker_(music_software)'
new=[
('Operating systems & system tools','Home server & self-hosting',{
 'n':'Home server software','a':'self-hosted server · NAS software','d':'Software that turns a spare computer or NAS box into a media, storage or home-automation server.',
 't':['home automation','NAS operating system','media server'],'s':W+'Home_Assistant',
 'x':[A('Home Assistant','Open Home Foundation','2013','Open-source home-automation hub that runs locally and links smart-home devices.','Home_Assistant'),
  A('TrueNAS','iXsystems','2005','NAS operating system that began as FreeNAS; Legacy and Community editions plus a commercial Enterprise line.','TrueNAS',a='FreeNAS'),
  A('Unraid','Lime Technology','2005','Commercial NAS and virtualisation operating system that pools mixed-size drives.','Unraid'),
  A('Plex Media Server','Plex','2008','Media server that streams a personal library to client apps; closed-source with a paid tier.','Plex_(company)'),
  A('Jellyfin','Jellyfin Team','2018','Free GPLv2 media server forked from Emby.','Jellyfin')]}),
('Operating systems & system tools','Desktop customisation & automation',{
 'n':'Desktop customisation tool','a':'desktop skin · automation scripting','d':'Windows software that restyles the desktop or automates keystrokes and tasks.',
 't':['desktop skin','live wallpaper','keystroke scripting'],'s':W+'Rainmeter',
 'x':[A('Rainmeter','Kimmo Pekkola','2001','Free desktop-customisation tool that displays skins such as clocks and system meters.','Rainmeter'),
  A('Wallpaper Engine','Kristjan Skutta','2016','Windows live-wallpaper app sold on Steam, with a companion Android app.','Wallpaper_Engine'),
  A('AutoHotkey','Chris Mallett','2003','Free scripting language for hotkeys and task automation on Windows.','AutoHotkey')]}),
('Music & audio','Music making & notation',{
 'n':'Modular and visual audio environment','a':'patching environment · visual programming for audio','d':'Software where users build synths and effects by wiring modules or objects on a canvas.',
 's':W+'VCV_Rack',
 'x':[A('Max','Cycling \'74','1990','Visual programming environment for music and multimedia, begun by Miller Puckette at IRCAM; first commercial version 1990.','Max_(software)',a='Max/MSP'),
  A('Pure Data','Miller Puckette','1996','Open-source visual programming language for audio, written by the original author of Max.','Pure_Data',a='Pd'),
  A('VCV Rack','Andrew Belt','2019','Open-source virtual Eurorack-style modular synthesiser; version 1.0.0 in 2019.','VCV_Rack')]}),
('Music & audio','Music making & notation',{
 'n':'Music tracker','a':'module tracker','d':'Sequencer that places notes and samples in channels down a vertical, pattern-based timeline.',
 's':tr_src,
 'x':[A('Ultimate Soundtracker','Karsten Obarski','1987','First tracker, released by EAS Computer Technik for the Amiga.','Tracker_(music_software)'),
  A('FastTracker 2','Triton','1994','PC tracker by Fredrik Huss and Magnus Högdahl of the demogroup Triton, released November 1994.','FastTracker_2'),
  A('Impulse Tracker','Jeffrey Lim','1995','PC tracker by Jeffrey "Pulse" Lim.','Impulse_Tracker'),
  A('OpenMPT','OpenMPT Project','1997','Open-source tracker that grew from ModPlug Tracker (1997); BSD-licensed since 2009.','OpenMPT',a='ModPlug Tracker'),
  A('Renoise','Renoise','2002','Modern tracker-based DAW; version 1.0 in June 2002.','Renoise')]}),
('Hobbies, science & sky','Hobby & home software',{
 'n':'SDR software','a':'software-defined radio software','d':'Programs that tune and decode radio signals from an SDR receiver on a computer.',
 's':W+'GNU_Radio',
 'x':[A('GNU Radio','GNU Radio Community','2001','Free toolkit for building software-defined radio signal-processing flowgraphs; created by Eric Blossom.','GNU_Radio')],
 'm':[['SDR#',''],['Gqrx',''],['SDRangel',''],['HDSDR','']]}),
('Office & productivity','Notes, tasks & calendars',{
 'n':'Long-form writing app','a':'manuscript software · writing studio','d':'Writing software that organises a book-length manuscript with research, outline and drafts together.',
 's':W+'Scrivener_(software)',
 'x':[A('Scrivener','Literature & Latte','2007','Manuscript-organising writing app for macOS, Windows and iOS; first released January 2007.','Scrivener_(software)')]}),
]
brands={}
for dn,sn,k in new:
  shelf(dn,sn)['k'].append(k)
  for a in k.get('x',[]): brands.setdefault(a['mk'],[]).append(a['n'])
# brand register
reg={x['n'].lower() for x in br['b']}
miss={}
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      for a in k.get('x',[]):
        if a.get('mk') and a['mk'].lower() not in reg: miss.setdefault(a['mk'],[]).append(a['n'])
HER=set('Moog Roland Sequential Circuits|Neve|EMT|Lexicon|Ampex|Studer|Teletronix|UREI|Fairchild|Tube-Tech|Pulse Techniques|Maestro|Binson|Sony|Bricasti|Millennia Corporation|Emagic|Mark of the Unicorn|Aldus Corporation|Encyclopaedia Britannica|Mandriva'.replace('Moog Roland Sequential Circuits','Moog|Roland|Sequential Circuits').split('|'))
PRO=set('IBM|Figma|Anthropic|Cognition|Serif (Europe)|Image-Line|Reason Studios|PreSonus|Slate Digital|Waves|Line 6|Final Draft|Side Effects Software|McNeel|Wilcom|Cockos|Cycling \'74|Plex'.split('|'))
INDIE=set('Open Home Foundation|iXsystems|Lime Technology|Jellyfin Team|Andrew Belt|Miller Puckette|GNU Radio Community|Kimmo Pekkola|Kristjan Skutta|Chris Mallett|Literature & Latte|OpenMPT Project|Renoise|Triton|Jeffrey Lim|Karsten Obarski|Arch Linux|Debian Project|Fedora Project|openSUSE Project|Gentoo Foundation|NixOS Foundation|Haiku Inc|ReactOS development team|Andreas Kling|KDE|GNU Project|LLVM Project|Linus Torvalds|Apache Software Foundation|R Foundation|Surge Synth Team|Matt Tytel|Brad Larsen|Jamie Zawinski|Decent Samples|Space Mushrooms|Youlean|Voxengo'.split('|'))
miss.update({k:v for k,v in brands.items() if k.lower() not in reg and k not in miss})
miss['Arch Linux']=['Arch lineage'];miss['Mandriva']=['Mandriva lineage']
known={"Plex":("United States","2009"),"Cycling '74":("United States","")}
for m,v in sorted(miss.items()):
  seg='Heritage manufactory' if m in HER else 'Professional & flagship' if m in PRO else 'Artisan & independent' if m in INDIE else 'Specialist'
  c,f=known.get(m,("",""))
  br['b'].append({'n':m,'c':c,'f':f,'seg':seg,'kf':v[0][:40],'d':'Maker of '+', '.join(v[:3])+'.','s':''})
json.dump(d,open('work/FIX_I1/stage2.json','w'),ensure_ascii=False,indent=1)
json.dump(br,open('work/FIX_I1/brands2.json','w'),ensure_ascii=False,indent=1)
print(len(miss))
