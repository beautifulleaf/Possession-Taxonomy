import json,copy
P='out/A5.json'
d=json.load(open(P))
def find(kn):
    for dp in d['depts']:
        for s in dp['s']:
            for i,k in enumerate(s['k']):
                if k['n']==kn: return dp,s,i,k
def pop_arch(kind,name):
    k=find(kind)[3]
    for i,a in enumerate(k['x']):
        if a['n']==name: return k['x'].pop(i)
    raise KeyError(name)
def kind(n,dd,s,a='',**kw):
    k={"n":n,"a":a,"d":dd,"s":s}; k.update(kw); return k

# A5-7 rename
for kn,old,new in [('Dive watch','Submariner','Rolex Submariner'),('Dive watch','Oyster Prince Submariner','Tudor Submariner'),
                   ('Dive watch','Seamaster 300','Omega Seamaster 300'),('Dive watch','Seamaster Diver 300M','Omega Seamaster Diver 300M')]:
    for a in find(kn)[3]['x']:
        if a['n']==old:
            a['n']=new; a['a']=(old+' · '+a['a']) if a.get('a') else old
# A5-6
dive=find('Dive watch')[3]; field=find('Field watch')[3]
dive['x'].append(pop_arch('Everyday watch','Yacht-Master'))
field['x'].insert(3,pop_arch('Everyday watch','Milgauss'))
field['x'].insert(4,pop_arch('Everyday watch','Railmaster'))
dp,sh,idx,dress=find('Dress watch')
everyday=find('Everyday watch')[3]
shaped=[pop_arch('Dress watch',n) for n in ['Tank','Reverso','Crash','Tortue','Tonneau','Golden Ellipse','Historiques American 1921']]
prest=[pop_arch('Everyday watch',n) for n in ['Datejust','Oyster Perpetual']]+[pop_arch('Dress watch',n) for n in ['Day-Date','Lange 1','Pasha de Cartier','Ballon Bleu de Cartier']]+[pop_arch('Everyday watch','Seamaster Aqua Terra')]
pk=kind('Prestige everyday watch',"Luxury round watch built for daily wear in all settings, usually with date and a bracelet.",
        'https://en.wikipedia.org/wiki/Rolex_Datejust','daily luxury watch',x=prest)
sk=kind('Shaped watch',"Wristwatch with a non-round case such as rectangular, tonneau, curved or asymmetric.",
        'https://en.wikipedia.org/wiki/Cartier_Tank','non-round watch · form watch',x=shaped)
# Cellini
dress['x'].insert(1,{"n":"Cellini","d":"Rolex line of non-Oyster dress watches with slim gold cases, begun in the late 1960s and discontinued in 2023.","mk":"Rolex","y":"1968","s":"https://www.swisswatchexpo.com/thewatchclub/2023/01/18/rolex-cellini-ultimate-guide/","dt":"case 39 mm in later models · white or Everose gold · non-Oyster case"})
# one-hand into dress m
oh=find('One-hand watch')[3]
dress['m']=dress.get('m',[])+oh.get('m',[])
find('One-hand watch')[2]
s=sh['k']; s.remove(oh)
s.insert(s.index(dress)+1,pk); s.insert(s.index(pk)+1,sk)
# A5-5 complications
def merge(kn_list,newname,dd,al,t,src):
    base=find(kn_list[0])[3]; x=[];m=[]
    ks=[find(n)[3] for n in kn_list]
    for k in ks: x+=k.get('x',[]); m+=k.get('m',[])
    sh=find(kn_list[0])[1]
    pos=sh['k'].index(base)
    for k in ks: sh['k'].remove(k)
    nk=kind(newname,dd,src,al,t=t)
    if x: nk['x']=x
    if m: nk['m']=m
    sh['k'].insert(pos,nk)
merge(['Annual-calendar watch','Perpetual-calendar watch','Moon-phase watch'],'Calendar watch',
 "Wristwatch showing date information beyond the day and date: annual, perpetual or moon-phase calendar.",'complicated calendar watch',
 ['annual calendar','perpetual calendar','moon phase','triple calendar'],'https://en.wikipedia.org/wiki/Patek_Philippe')
merge(['Minute-repeater watch','Sonnerie watch'],'Chiming watch',
 "Wristwatch that strikes the time, on demand as a repeater or by itself as a sonnerie.",'striking watch · repeater',
 ['minute repeater','petite sonnerie','grande sonnerie'],'https://www.thetimepiececollection.com/spaceone.html')
# world time into GMT
g=find('GMT watch')[3]; w=find('World-time watch')
g['n']='GMT & world-time watch'; g['a']='dual-time watch · world-time watch'
g['t']=['GMT','world time']
g['x']+=w[3]['x']; g['m']=g.get('m',[])+w[3].get('m',[])
w[1]['k'].remove(w[3])
# A5-4
for n in ['Tower clock','Time clock']:
    r=find(n); r[1]['k'].remove(r[3])
parts=[find(n) for n in ['Watch clasp','Watch spring bar','Watch crown']]
for p in parts: p[1]['k'].remove(p[3])
mod=find('Watch bezel & insert')[1]
mod['k'].append(kind('Small watch parts',"Clasps, spring bars and crowns sold separately to fit, repair or customise a watch.",
  'https://www.horoparts.com/','watch clasp · spring bar · crown',t=['clasp & buckle','spring bar','crown & tube']))
# A5-2 new watches
def add(kn,pos,a):
    k=find(kn)[3]; k['x'].insert(pos,a)
add('Integrated-bracelet sports watch',3,{"n":"PRX","d":"Tissot's integrated-bracelet sports watch, released in 1978 and relaunched by Swatch Group in 2021.","mk":"Tissot","y":"1978","s":"https://en.wikipedia.org/wiki/Tissot","v":[{"n":"original PRX","y":"1978","d":"first release, discontinued in the 1980s"},{"n":"PRX relaunch","y":"2021","d":"stainless steel with integrated bracelet"}],"dt":"integrated bracelet · stainless steel"})
add('Field watch',2,{"n":"Alpinist","d":"Seiko mountaineering watch with internal rotating compass bezel set by a crown at 4 o'clock.","mk":"Seiko","y":"1961","s":"https://wornandwound.com/review/video-missed-review-the-seiko-alpinist-sarb017/","v":[{"n":"Laurel Alpinist","y":"early 1960s","d":"first use of the name"},{"n":"red Alpinist SCVF","y":"1995","d":"Shigeo Sakai design, template for later models; 37 mm"},{"n":"SARB017","y":"2006","d":"almond green dial, 6R15, Japan-only; name retired later"}],"dt":"case 39 mm (SARB) · steel · green dial · compass bezel · 200 m"})
add('Chronograph',6,{"n":"Lunar Pilot","d":"Bulova chronograph worn by David Scott on the Moon during Apollo 15, with a tuning-fork movement.","mk":"Bulova","y":"1971","s":"https://au.bulova.com/pages/lunar-pilot","v":[{"n":"Apollo 15 original","y":"1971","d":"tuning-fork movement"},{"n":"50th Anniversary Limited Edition","y":"2021","d":"quartz 262 kHz movement, titanium case"}],"dt":"tuning-fork or high-frequency quartz · steel or titanium"})
add('Chronograph',7,{"n":"Camaro","d":"Heuer chronograph in a square cushion case, named after the Chevrolet; hand-wound only.","mk":"Heuer","y":"1968","s":"https://www.timeline.watch/watch/1968-heuer-camaro-45-ref-9220-s/?cat=2","v":[{"n":"9220","y":"1968–72","d":"Valjoux 92, 37 mm case, 45-minute counter"}],"dt":"case 37 mm · steel · manual-wind Valjoux"})
add('Dress watch',6,{"n":"Portofino","d":"IWC round dress family launched in 1984, led by the oversized moon-phase 5251.","mk":"IWC Schaffhausen","y":"1984","s":"https://robbreport.com.my/style/watches/iconic-iwc-portofino-collection-watches-1984/","v":[{"n":"5251","y":"1984","d":"\"Fried Egg\" moon phase at three o'clock, oversized case"}],"dt":"round case · Roman numerals · Breguet-style hands"})
# clocks
cc=find('Marine chronometer')[0]
cc['s'].append({"n":"Regional & period clocks","k":[
 kind('Wadokei',"Japanese clock of the Edo period that shows seasonal unequal hours, mostly weight-driven.",'https://en.wikipedia.org/wiki/Japanese_clock','Japanese clock',
  x=[{"n":"Pillar clock","a":"hashira-dokei","d":"Wadokei in which an indicator descends on a weight and movable markers are set for the seasons.","mk":"","y":"Edo period","s":"https://en.wikipedia.org/wiki/Japanese_clock","dt":"weight-driven · verge and foliot · seasonal hour markers"},
     {"n":"Inro clock","a":"inrō-dokei","d":"Small spring-driven wadokei carried in an inrō pouch.","mk":"","y":"Edo period","s":"https://en.wikipedia.org/wiki/Japanese_clock","dt":"spring-driven · pocket size"},
     {"n":"Pillow clock","a":"makura-dokei","d":"Wadokei in a box case, sometimes fitted with a music box.","mk":"","y":"Edo period","s":"https://en.wikipedia.org/wiki/Japanese_clock","dt":"box case · optional music box"}]),
 kind('American shelf clock',"Weight-driven shelf clock from the Connecticut industry that made clocks affordable, from wooden to brass movements.",'https://en.wikipedia.org/wiki/Eli_Terry','',
  x=[{"n":"Pillar and scroll","d":"Eli Terry's shelf clock case design with wooden movement, made in quantity from the early 1800s.","mk":"Eli Terry","y":"1810s","s":"https://en.wikipedia.org/wiki/Eli_Terry","dt":"wooden movement · mahogany case"},
     {"n":"OG clock","a":"ogee clock","d":"Rectangular brass-movement shelf clock with an S-curved (ogee) case moulding, mass-produced by Chauncey Jerome.","mk":"Chauncey Jerome","y":"1840s","s":"https://en.wikipedia.org/wiki/Chauncey_Jerome","dt":"30-hour or 8-day brass movement · veneered case"}]),
]})
cc['s'].append({"n":"Collectible electric & design clocks","k":[
 kind('Electric synchronous clock',"Mains-powered clock that keeps time from the alternating-current frequency, via a self-starting synchronous motor.",'https://en.wikipedia.org/wiki/Telechron','Telechron clock',
  x=[{"n":"Telechron clock","d":"Clock with Warren's self-starting synchronous motor, made in Ashland, Massachusetts, 1912–1992.","mk":"Telechron","y":"1920s","s":"https://en.wikipedia.org/wiki/Telechron","dt":"synchronous motor · bakelite, wood or metal cases"}]),
 kind('Split-flap clock',"Clock whose digits are printed on flaps that fall to show each new time, used in stations and airports.",'https://en.wikipedia.org/wiki/Solari_di_Udine','flip clock · Solari clock',
  x=[{"n":"Cifra","d":"Solari split-flap clock designed with Gino Valle; the Cifra 5 won the Compasso d'Oro in 1956.","mk":"Solari","y":"1956","s":"https://en.wikipedia.org/wiki/Solari_di_Udine","dt":"split-flap digits · desk, wall or station sizes"}]),
]})
# Vienna regulator
wr=find('Wall regulator')[3]
wr['x'].append({"n":"Vienna regulator","d":"Wall regulator first made in Vienna around 1780 and spread across the German-speaking world until about 1930.","mk":"","y":"c. 1780","s":"https://schifferbooks.com/products/vienna-regulator-clocks","dt":"walnut case · glass sides · early, Biedermeier, altdeutsch styles"})
json.dump(d,open('work/FIX_A5/A5.tmp','w'),ensure_ascii=False,indent=1)
# brands
bp='out/A5_brands.json'; b=json.load(open(bp))
b['b'].append({"n":"Solari","c":"Italy","f":"1725","seg":"Traditional & regional","kf":"split-flap displays","d":"Pesariis company that began with tower clocks and made split-flap clocks and station displays.","lines":["Cifra"],"sig":["Cifra"],"s":"https://en.wikipedia.org/wiki/Solari_di_Udine"})
json.dump(b,open('work/FIX_A5/b.tmp','w'),ensure_ascii=False,indent=1)
tp='out/A5_traditions.json'; t=json.load(open(tp))
G="Metal & mechanisms"
t['t']+=[
{"n":"Japanese wadokei clockmaking","g":G,"r":"Japan","p":"Edo period (1603–1868)","d":"Clocks adapted from European mechanisms to show seasonal unequal hours.","tech":"verge-and-foliot escapements, adjustable hour markers","mat":"brass, iron, wood","forms":["pillar clock","pillow clock","inro clock","bracket clock"],"ctr":["Tsuda Sukezaemon","Hosokawa Hanzo","Tanaka Hisashige"],"auth":"Unequal-hour dial with zodiac hour marks; Japanese maker signatures.","s":"https://en.wikipedia.org/wiki/Japanese_clock"},
{"n":"Vienna regulator clockmaking","g":G,"r":"Vienna, Austria and German-speaking lands","p":"c. 1780–c. 1930","d":"Wall regulators first made in Vienna and later in factories across the German-speaking world.","tech":"weight-driven precision movements in glazed cases","mat":"walnut and other veneers, brass, glass","forms":["Vienna regulator","wall regulator"],"ctr":["Vienna","Gustav Becker","Lenzkirch"],"auth":"Style period (early, Biedermeier, altdeutsch) and maker marks on movement and dial.","s":"https://schifferbooks.com/products/vienna-regulator-clocks"},
{"n":"American clock industry (Connecticut)","g":G,"r":"Connecticut, United States","p":"early 19th century–1850s onward","d":"Mass production of clocks with interchangeable parts that made them affordable, moving from wood to brass movements.","tech":"machine-made interchangeable parts, stamped brass movements","mat":"wood, brass, veneer","forms":["pillar and scroll shelf clock","OG clock","tower clock"],"ctr":["Eli Terry (Plymouth)","Chauncey Jerome (Bristol, New Haven)","Seth Thomas"],"auth":"Paper labels inside the case and movement stamps; wooden or brass works indicate period.","s":"https://en.wikipedia.org/wiki/Eli_Terry"},
{"n":"Soviet watchmaking","g":G,"r":"USSR (Moscow, Zlatoust, Chistopol)","p":"1930–1991","d":"State-run factories that began with the First State Watch Factory in 1930, later brands such as Poljot.","tech":"state-factory production, military and space watches","mat":"steel, chrome-plated brass","forms":["Pobeda wristwatch","Sturmanskie","Strela chronograph"],"ctr":["First Moscow Watch Factory","Poljot"],"auth":"Cyrillic dials and case backs, factory codes and dated movements.","s":"https://en.wikipedia.org/wiki/Poljot"}]
json.dump(t,open('work/FIX_A5/t.tmp','w'),ensure_ascii=False,indent=1)
