import json,copy
O='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(O+'D3.json')); br=json.load(open(O+'D3_brands.json')); mv=json.load(open(O+'D3_moves.json'))
def find(n):
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']:
                if k['n']==n: return dp,s,k
    raise KeyError(n)
def drop(n):
    dp,s,k=find(n); s['k'].remove(k); return k
def dd(l):
    seen=[];[seen.append(x) for x in l if x not in seen]; return seen
def merge(base,others,name,alias,dfn,t=None):
    ks=[base]+others
    base['n']=name
    base['a']=' · '.join(dd([x for k in ks for x in (([k['n']] if k is not base else [])+(k.get('a','').split(' · ') if k.get('a') else []))]+[alias] if alias else []))if False else base.get('a','')
    for k in others: drop(k['n'])
    base['x']=[a for k in ks for a in k.get('x',[])]
    base['m']=dd([m for k in ks for m in k.get('m',[])])
    r=dd([m for k in ks for m in k.get('r',[])])
    if r: base['r']=r
    base['t']=dd((t or [])+[x for k in ks for x in k.get('t',[])])
    base['d']=dfn
    if not base['m']: del base['m']
    if not base.get('a'): base.pop('a',None)
# --- D3-5 headphones
_,_,ob=find('Open-back headphones'); cb=find('Closed-back headphones')[2]; nc=find('Wireless noise-cancelling headphones')[2]
old=[ob['n'],cb['n'],nc['n']]
merge(ob,[cb,nc],'Over-ear headphones',None,'Headphone whose cups enclose the ear, open or sealed at the back; acoustic design, driver and connectivity are types.',
  ['open-back','closed-back','semi-open','noise-cancelling (wireless)','wired','wireless'])
ob['a']=' · '.join(old)
ob['t']=[x for x in ob['t'] if x not in('dynamic','planar magnetic')]+['dynamic','planar magnetic']
ob['t']=dd(ob['t'])
find('On-ear headphones')[2]['d']='Headphone whose pads rest on the ear; open or closed designs, such as the Grado SR and Sennheiser HD 25, are types.'
# --- D3-4 fold empties
_,_,st=find('Headphone stand'); drop('Headphone stand')
sp=find('Headphone & earbud spare parts')[2]; sp['t']=dd(sp['t']+['headphone stand or hanger'])
sp['d']='Replacement part made for one headphone or earbud model, such as ear pads, ear tips or a charging case, or a stand to hold headphones.'
# home cinema speakers
hc=find('Home cinema speaker system')[2]
others=[find(n)[2] for n in ['Centre speaker','Surround speakers','In-wall and in-ceiling speakers','On-wall speakers']]
merge(hc,others,'Home cinema speakers','Home cinema speaker system · Centre speaker · Surround speakers · In-wall speakers · On-wall speakers',
 'Speaker or speaker package for a surround system: front, centre, surround and height channels, free-standing or built into the wall.',
 ['package system','centre channel','surround (side, rear)','height (Atmos-enabled)','in-wall / in-ceiling','on-wall'])
hc['a']='Home cinema speaker system · Centre speaker · Surround speakers · In-wall speakers · On-wall speakers'
# portable BT + party
drop('Party speakers')
pb=find('Portable Bluetooth speakers')[2]
pb['t']=['pocket','mid-size','party speaker','waterproof']
pb['d']='Battery-powered speaker made to carry around, usually Bluetooth and often waterproof; party speakers are the largest.'
pb['m']=dd(pb.get('m',[])+[['Flip 7','JBL'],['Charge 6','JBL'],['Boombox 4','JBL'],['PartyBox 720','JBL'],['WONDERBOOM 4','Ultimate Ears'],['MEGABOOM 4','Ultimate Ears'],['SoundLink Flex (2nd Gen)','Bose'],['SoundLink Max','Bose'],['SRS-XB100','Sony'],['Soundcore Boom 2','Anker']])
pb['s']='https://www.rtings.com/speaker/reviews/best/by-feature/bluetooth'
# master clock -> DAC
drop('Master clock'); dac=find('DAC')[2]; dac['t']=dd(dac['t']+['master clock (external reference)'])
# AV
drop('Multichannel power amplifier'); drop('Video processor')
ap=find('AV processor')[2]; ap['t']=['surround processor','video processor','multichannel power amplifier (companion)']
# screen
drop('Projector screen'); pr=find('Projector')[2]; pr['t']=['projector screen (accessory)']
# --- audio figure move
af=drop('Audio figure')
mv['out'].append({'to':'E1','dept':'Baby & toddler toys','kind':af})
# --- archetypes
def ins(kind,i,a): k=find(kind)[2]; k['x'].insert(i,a)
def pos(kind,after):
    k=find(kind)[2]; return [x['n'] for x in k['x']].index(after)+1
W='https://en.wikipedia.org/wiki/'
ins('Bookshelf speakers',1,{'n':'Yamaha NS-10','a':'NS-10M','d':'Two-way sealed bookshelf speaker with white-cone woofer that became a nearfield studio monitor.','mk':'Yamaha','y':'1978','s':W+'Yamaha_NS-10',
 'v':[{'n':'NS-10M Studio','mk':'Yamaha','y':'1987','d':'Studio version'},{'n':'NS-10M Pro','mk':'Yamaha','y':'1987','d':'Pro version'},{'n':'NS-10T','mk':'Yamaha'},{'n':'NS-10M X','mk':'Yamaha'},{'n':'NS-10MC','mk':'Yamaha'},{'n':'NS-10MT','mk':'Yamaha'},{'n':'NS-10MM','mk':'Yamaha'}],'dt':'sealed cabinet · white-cone woofer'})
k=find('Bookshelf speakers')[2]; k['x'].append({'n':'Wharfedale Diamond','a':'Diamond series','d':'Small two-way bookshelf speaker that launched the Diamond range as a budget hi-fi benchmark.','mk':'Wharfedale','y':'1982','s':'https://hifihalloffame.com/equipment/wharfedale-diamond-loudspeaker/','v':[{'n':'Diamond','mk':'Wharfedale','y':'1982','d':'24 cm, 5.2 litre cabinet, launched at £65'}],'dt':'compact two-way · now in its twelfth generation'})
k=find('Floor-standing speakers')[2]; k['x'].append({'n':'Dynaudio Contour','a':'Contour series','d':'Long-running Dynaudio series of stand-mount, floorstanding and centre speakers.','mk':'Dynaudio','y':'','s':'https://dynaudio.com/discontinued-models/contour',
 'v':[{'n':n,'mk':'Dynaudio'} for n in ['Contour 1.3','Contour 1.3 MK II','Contour 1.8','Contour 2.8','Contour 3.0','Contour 3.3','Contour T 2.5']],'dt':'stand-mount · floorstanding · centre'})
T='https://en.wikipedia.org/wiki/Technics_(brand)'
tt=find('Turntable')[2]
i=pos('Turntable','Thorens TD 124')
tt['x'].insert(i,{'n':'EMT 927','a':'EMT 930 · EMT 928','d':'Broadcast studio turntable with idler-wheel drive and large platter for 16-inch transcription discs.','mk':'EMT','y':'1951','s':W+'Elektromesstechnik',
 'v':[{'n':'EMT 927','mk':'EMT','y':'1951','d':'Idler-wheel drive, 997 arm from 1974'},{'n':'EMT 930','mk':'EMT','d':'Smaller sibling keeping the idler-wheel drive'},{'n':'EMT 928','mk':'EMT','y':'1968','d':'Belt-drive design based on the Thorens TD125'}],'dt':'idler drive · broadcast chassis'})
tt['x'].insert(i+1,{'n':'Lenco L75','a':'Lenco','d':'Swiss-origin turntable made for almost two decades; an enthusiast base for custom plinths.','mk':'Lenco','y':'1967–1985','s':W+'Lenco_Turntables','dt':'platter · plinth'})
j=[x['n'] for x in tt['x']].index('Technics SL-1200')+1
tt['x'].insert(j,{'n':'Technics SP-10','a':'SP-10 Mk2','d':'First direct-drive turntable on the professional market, sold as a drive unit without arm or plinth.','mk':'Technics','y':'1969','s':T,'v':[{'n':'SP-10','mk':'Technics','y':'1969','d':'Matsushita, from Shuichi Obata\'s invention'}],'dt':'drive unit · plinth sold separately'})
j=[x['n'] for x in tt['x']].index('Michell GyroDec')+1
tt['x'].insert(j,{'n':'Micro Seiki SX-8000','a':'Micro Seiki','d':'Very heavy Japanese reference turntable sold as a separate drive unit (RY-5500) without tonearm.','mk':'Micro Seiki','y':'1981–1984','s':'https://hifi-wiki.com/index.php/Micro_Seiki_SX-8000','dt':'106.5 kg · drive unit RY-5500'})
pc=find('Phono cartridge')[2]
pc['x'][2:2]=[
 {'n':'Shure V15','a':'V-15','d':'Moving-magnet cartridge series with a Micro-Ridge stylus, widely used as a benchmark.','mk':'Shure','y':'1964','s':W+'Shure',
  'v':[{'n':'V15','mk':'Shure','y':'1964'},{'n':'V15 Type II','mk':'Shure','y':'1966'},{'n':'V15 Type IV','mk':'Shure','y':'1978'},{'n':'V15 Type V','mk':'Shure','d':'Ultra-thin beryllium stylus shank'},{'n':'V15 VxMR','mk':'Shure','d':'Series discontinued 2004'}],'dt':'moving magnet · stylus profile'},
 {'n':'Koetsu','a':'Koetsu moving coil','d':'Hand-built Japanese moving-coil cartridges with exotic bodies of metal, wood, lacquer or stone.','mk':'Koetsu','y':'late 1960s','s':'https://www.stereonet.com/features/koetsu-an-appreciation',
  'v':[{'n':'Koetsu Black','mk':'Koetsu'},{'n':'Koetsu Rosewood','mk':'Koetsu','y':'mid-1980s'},{'n':'Koetsu Rosewood Signature','mk':'Koetsu'},{'n':'Koetsu Urushi','mk':'Koetsu'},{'n':'Koetsu Onyx Platinum','mk':'Koetsu'}],'dt':'body: metal, wood, lacquer, stone'},
 {'n':'Lyra moving coil','a':'Lyra','d':'Tokyo-based moving-coil range from entry Delos through Kleos and Atlas to Titan i.','mk':'Lyra','y':'','s':'https://radar.stereonet.com/brand/lyra',
  'v':[{'n':n,'mk':'Lyra'} for n in ['Delos','Kleos','Atlas','Titan i','SPT']],'dt':'moving coil · body material'}]
k=find('Portable cassette player')[2]
k['x']+= [
 {'n':'Aiwa HS-P','a':'HS-P05','d':'Aiwa personal cassette player series, a main rival to the Sony Walkman.','mk':'Aiwa','y':'mid-1980s','s':W+'Aiwa','v':[{'n':'HS-P05 Mk II','mk':'Aiwa','y':'mid-1980s'}],'dt':'playback or recording'},
 {'n':'Toshiba Walky','a':'KT-AS10','d':'Toshiba cassette player line; the KT-AS10 has a removable cassette-shaped radio tuner.','mk':'Toshiba','y':'mid-1980s','s':'https://www.core77.com/posts/116640/The-Most-Unusual-Walkman-Design-The-Toshiba-Walky','v':[{'n':'KT-AS10','mk':'Toshiba','y':'mid-1980s','d':'Removable radio module'}],'dt':'with or without radio'},
 {'n':'Panasonic RQ-S','a':'S-XBS','d':'Panasonic personal stereo cassette player series.','mk':'Panasonic','y':'','s':'https://collection.sciencemuseumgroup.org.uk/objects/co117618/panasonic-s-xbs-personal-stereo-cassette-player-model-no-rq-s44','v':[{'n':'RQ-S44 (S-XBS)','mk':'Panasonic','y':'1991'}],'dt':'bass boost · radio'}]
# brands
have={b['n'] for b in br['b']}
new=[
 ('Toshiba','Japan','','Mainstream','Walky cassette','Japanese electronics group whose Walky line answered the Sony Walkman.','https://www.core77.com/posts/116640/The-Most-Unusual-Walkman-Design-The-Toshiba-Walky',['Walky']),
 ('Aiwa','Japan','1951','Mainstream','personal cassette','Japanese brand founded as AIKO Denki Sangyo, renamed Aiwa in 1959 and absorbed by Sony in 2002.',W+'Aiwa',['HS-P05 Mk II']),
 ('Lenco','Switzerland','1946','Heritage manufactory','L75 turntable','Swiss firm founded in Burgdorf by Fritz and Marie Laeng with Bruno Grütter; name now owned by Commaxx.',W+'Lenco_Turntables',['Lenco L75']),
 ('EMT','Germany','1938','Professional & flagship','broadcast turntables','German audio maker (Elektromesstechnik) founded in Berlin by Wilhelm Franz, later in Lahr.',W+'Elektromesstechnik',['EMT 927']),
 ('Koetsu','Japan','','Artisan & independent','moving coil cartridges','Japanese cartridge maker founded by Yoshiaki Sugano, now run by his family.','https://www.stereonet.com/features/koetsu-an-appreciation',['Koetsu Rosewood']),
 ('Lyra','Japan','','Artisan & independent','moving coil cartridges','Tokyo cartridge maker founded by American, Japanese and Norwegian partners.','https://radar.stereonet.com/brand/lyra',['Kleos','Atlas']),
 ('Micro Seiki','Japan','','Specialist','reference turntables','Japanese maker of heavy turntables, drive units and tonearms.','https://hifi-wiki.com/index.php/Micro_Seiki_SX-8000',['SX-8000'])]
for n,c,f,seg,kf,dsc,s,sig in new:
    if n not in have: br['b'].append({'n':n,'c':c,'f':f,'seg':seg,'kf':kf,'d':dsc,'s':s,'sig':sig,'lines':[],'eras':[],'sc':[],'rel':[]})
for b in br['b']:
    if b['n']=='Yamaha': b['sig']=dd(b.get('sig',[])+['NS-10'])
    if b['n']=='Dynaudio': b['sig']=['Contour']
    if b['n']=='Wharfedale': b['sig']=['Diamond']
    if b['n']=='Shure': b['sig']=dd(b['sig']+['V15'])
    if b['n']=='Technics': b['sig']=dd(b['sig']+['SP-10'])
    if b['n']=='Panasonic': b['sig']=dd(b['sig']+['RQ-S'])
for n,f in [('D3',d),('D3_brands',br),('D3_moves',mv)]:
    json.dump(f,open(O+n+'.json.tmp','w'),indent=1,ensure_ascii=False)
import os
for n in ['D3','D3_brands','D3_moves']: os.replace(O+n+'.json.tmp',O+n+'.json')
