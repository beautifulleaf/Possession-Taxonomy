import json,os
P='out/H3.json'
d=json.load(open(P))
def find(n):
    for dp in d['depts']:
        for s in dp['s']:
            for i,k in enumerate(s['k']):
                if k['n']==n: return dp,s,i,k
    raise KeyError(n)
def rm(n):
    dp,s,i,k=find(n); s['k'].pop(i); return k
def dropm(k,names):
    k['m']=[m for m in k.get('m',[]) if m[0] not in names]
    if not k['m']: k.pop('m')
WP='https://en.wikipedia.org/wiki/'
# wand
k=find('Wand vibrator')[3]
dropm(k,{'Magic Wand Original','Magic Wand Rechargeable','Magic Wand Mini'})
k['x']=[{"n":"Magic Wand","a":"Hitachi Magic Wand · Original Magic Wand · HV-250R","d":"Corded mains wand massager with a large round head, listed in 1968; the reference wand for the kind.","mk":"Vibratex","y":"1968","s":WP+"Hitachi_Magic_Wand",
 "v":[{"n":"Original (corded)","mk":"Vibratex","y":"1968","d":"Hitachi HV-250R; mains-powered, two speeds; sold as Original Magic Wand from 2013"},
 {"n":"Rechargeable","mk":"Vibratex","y":"2015","d":"Battery-powered, four speeds, silicone head"},
 {"n":"Plus","mk":"Vibratex","y":"2019","d":"Plug-in, separate up and down buttons"},
 {"n":"Mini","mk":"Vibratex","y":"2022","d":"Compact, three power levels"}],
 "dt":"mains or rechargeable · silicone or vinyl head · full size, mini or micro"}]
# external vibrator fold
b=rm('Bullet vibrator'); pa=rm('Palm vibrator'); fl=rm('Flicking vibrator'); gl=rm('Glans vibrator'); wp=rm('Wearable panty vibrator'); vc=rm('Vibrating cushion')
dp,s,i,_=find('Wand vibrator')
keep={'Zee Bullet Vibrator','Classic Bullet Vibe','Riot Bullet Vibrator','Pocket Rocket','Vibe Personal Massager'}
ms=[m for m in b['m'] if m[0] in keep]+pa['m']+[m for m in fl['m'] if m[0] in('Klitty','Fluttering Arouser')]
ev={"n":"External vibrator","a":"bullet vibrator · pocket rocket · finger vibrator · palm vibrator · panty vibrator",
 "d":"Small vibrator for use on the outside of the body, made in bullet, palm, flicking-tip, head-worn and wearable forms. A vibrating cushion or pad also counts here.",
 "t":["Bullet","Finger-worn","Palm (mouse-shaped)","Flicking tip","Head-worn (glans)","Wearable panty vibrator, remote or app control","Vibrating cushion or pad","Rechargeable","Waterproof"],
 "m":ms,"s":b['s']}
s['k'].insert(i+1,ev)
# rabbit
k=find('Rabbit vibrator')[3]
dropm(k,{'Rabbit Pearl','Rampant Rabbit','Jack Rabbit'})
k['x']=[{"n":"Rabbit Pearl","a":"original rabbit vibrator","d":"First rabbit vibrator, with rotating pearls in the shaft and an animal-shaped external arm; Vibratex imported the type from Japan.","mk":"Vibratex","y":"1984","s":WP+"Rabbit_vibrator","dt":"rotating pearls · animal-shaped arm · jelly or silicone"},
 {"n":"Rampant Rabbit","a":"","d":"Ann Summers' dual-action rabbit vibrator, one of the imitations that followed the Rabbit Pearl.","mk":"Ann Summers","y":"","s":WP+"Rabbit_vibrator","dt":"rotating shaft · external arm"},
 {"n":"Jack Rabbit","a":"","d":"Rabbit vibrator designed by Susan Colvin for the magazine company CPLC in the mid-1980s.","mk":"","y":"mid-1980s","s":WP+"Rabbit_vibrator","dt":"rotating shaft · external arm"}]
# couples
k=find('Couples vibrator')[3]
dropm(k,{'We-Vibe 4 Plus'})
k['x']=[{"n":"We-Vibe","a":"","d":"Small U- or C-shaped vibrator worn by one partner during intercourse; the first model came in 2008.","mk":"We-Vibe","y":"2008","s":WP+"We-Vibe",
 "v":[{"n":"Original","mk":"We-Vibe","y":"2008","d":"First couples vibrator of the brand"},{"n":"4 Plus","mk":"We-Vibe","y":"2014","d":"Bluetooth and app control"}],"dt":"C-shape · silicone · app or remote control"}]
# air pulse
k=find('Air-pulse stimulator')[3]
dropm(k,{'Womanizer W100','Womanizer OG','Womanizer Premium Eco'})
k['x']=[{"n":"Womanizer","a":"pressure-wave stimulator","d":"German air-pulse stimulator range that began the kind, using Pleasure Air Technology without contact pressure.","mk":"Womanizer","y":"2014","s":WP+"Womanizer_(pressure_wave_vibrator)",
 "v":[{"n":"W100","mk":"Womanizer","y":"2014","d":"First model"},{"n":"OG","mk":"Womanizer","y":"","d":"Adds internal vibration to air-pulse stimulation"},{"n":"Premium Eco","mk":"Womanizer","y":"","d":"Made from biodegradable material"}],"dt":"handheld · rechargeable · waterproof"}]
# handheld masturbator
k=find('Handheld masturbator')[3]
dropm(k,{'Fleshlight sleeve'})
k['x']=[{"n":"Fleshlight","a":"","d":"Sleeve of soft material inside a hard case shaped like a torch, patented in 1998; the first of its type to sell widely.","mk":"Fleshlight","y":"1998","s":WP+"Fleshlight",
 "v":[{"n":"Classic collection","mk":"Fleshlight","y":"1998","d":"Original line"},{"n":"Freak and Alien collections","mk":"Fleshlight","y":"","d":"Fantasy and science-fiction designs"}],"dt":"sleeve texture and channel · case · material firmness"}]
# disposable
k=find('Disposable masturbator')[3]
k['x']=[{"n":"Tenga Cup","a":"","d":"Single-use cup-shaped masturbator with a valve for suction; first product of Tenga.","mk":"TENGA","y":"2005","s":WP+"Tenga_(company)","dt":"texture and firmness"},
 {"n":"Tenga Egg","a":"","d":"Single-use stretchy egg-shaped sleeve with 18 textures; the cheapest Tenga line.","mk":"TENGA","y":"","s":WP+"Tenga_(company)","dt":"texture; pack"}]
# automatic
k=find('Automatic masturbator')[3]
dropm(k,{'Fleshlight Launch','Onyx+','Storm','FLIP 0 (ZERO) ELECTRONIC VIBROTATION'})
k['m'].append(['Flip 0 (Zero)','TENGA'])
k['x']=[{"n":"Fleshlight Launch","a":"","d":"Interactive device, developed with KIIROO, that moves a Fleshlight sleeve and can sync with video or compatible toys.","mk":"Fleshlight","y":"2017","s":WP+"Fleshlight","v":[{"n":"Quickshot Launch","mk":"Fleshlight","y":"2019","d":"Later release"}],"dt":"motor stroke · app sync"}]
# saddle
k=find('Saddle machine')[3]
dropm(k,{'Sybian'})
k['x']=[{"n":"Sybian","a":"","d":"Saddle machine with vibrating and rotating attachments, invented by Dave Lampert and released in 1987.","mk":"Sybian","y":"1987","s":WP+"Sybian","dt":"attachments (synthetic rubber) · sizes and shapes · wired control"}]
# toy cleaner
k=find('Toy cleaner')[3]
keep={'LELO Premium Cleaning Spray','Lovehoney Fresh Toy Cleaner','System JO Foaming Toy Cleaner','Doc Johnson Toy Cleaner Antibacterial','b-Vibe UV Light Sterilizer Bag','Hand + Vibe Cleaner'}
k['m']=[m for m in k['m'] if m[0] in keep]
# sounds
k=find('Urethral sound')[3]
k['t']=["Stainless steel","Graduated sets in medical shapes (Dittel, Hegar, Pratt, Van Buren)"]
# spreaders into body restraint
rm('Spreader bar'); rm('Labia spreader')
k=find('Body restraint')[3]
k['d']="Harness or sleeve that restrains the body or binds the arms, or a bar or strap set that holds the limbs apart. A strap-on harness is a separate kind in Dildos, plugs & insertables."
k['t']=["Restraint harness","Armbinder","Spreader bar","Labia spreader"]
# new kinds
dp,s,i,_=find('Kegel balls')
s['k'].insert(find('Dildo')[2]+1,{"n":"Strap-on harness","a":"strap-on · harness","d":"Harness that holds a dildo against the wearer's body, usually by an O-ring or a plug fitting.","t":["Two-strap","Three-strap (thigh straps)","O-ring fitting","Vac-u-lock fitting","Leather","Fabric","Latex or rubber"],"s":WP+"Strap-on_dildo"})
dp,s,i,_=find('Dildo')
s['k'].insert(i+2,{"n":"Fantasy-form toy","a":"creature toy","d":"Toy moulded as a fantasy creature or creature-inspired shape, sold by makers who also take customer designs for limited runs.","t":["Dragon","Horse","Tentacle","Custom or limited run"],"r":[["Bad Dragon range","Bad Dragon"]],"s":WP+"Bad_Dragon"})
dp,s,i,_=find('Sex swing')
s['k'].append({"n":"Positioning wedge","a":"sex pillow · positioning cushion · ramp","d":"Angled foam wedge or pillow that supports the body in different positions.","t":["Wedge","Ramp","Wedge and ramp set","Bondage pillow","Waterproof cover"],
 "x":[{"n":"Liberator Wedge","a":"","d":"Angled foam positioning pillow, the maker's core product, sold alone or in a wedge-and-ramp set.","mk":"Liberator","y":"","s":"https://www.liberator.com/","v":[{"n":"Wedge Ramp Combo","mk":"Liberator","y":"","d":"Wedge sold with a ramp"}],"dt":"foam density · cover fabric · waterproof option"}],"s":WP+"Sex_furniture"})
# oil to care
oil=rm('Intimate oil')
find('Toy cleaner')[1]['k'].append(oil)
# dolls dept
dolls=[rm('Solid body doll'),rm('Stationary masturbator'),rm('Inflatable doll')]
dolls[0]['x']=[{"n":"RealDoll","a":"","d":"Life-size silicone doll on a poseable skeleton with steel joints, made by Abyss Creations in Las Vegas.","mk":"Abyss Creations","y":"1996","s":WP+"RealDoll",
 "v":[{"n":"Face-X system","mk":"Abyss Creations","y":"2003","d":"Interchangeable faces on one body"},{"n":"RealDoll 2","mk":"Abyss Creations","y":"2009","d":"Removable inserts, magnetic faces, platinum silicone"}],"dt":"body type · silicone or TPE · skeleton"}]
dropm(dolls[0],{'RealDoll'})
for dp in d['depts']:
    dp['s']=[s for s in dp['s'] if s['k']]
idx=[x['n'] for x in d['depts']].index('Masturbators, sleeves & rings')
d['depts'].insert(idx+1,{"n":"Dolls & body-form toys","mode":"tier","s":[{"n":"Dolls & body-form toys","k":dolls}]})
d['lead']=d['lead'].rstrip()+" Latex fetish wear is in Clothing (A1)."
tmp=P+'.tmp'; json.dump(d,open(tmp,'w'),ensure_ascii=False,indent=1); os.replace(tmp,P)
# brands
BP='out/H3_brands.json'; bd=json.load(open(BP))
names={b['n'].lower() for b in bd['b']}
new=[{"n":"Bad Dragon","c":"United States","f":"2008","seg":"Specialist","kf":"fantasy-form toys","d":"Maker of fantasy-creature toys, founded in 2008, that also produces customer designs in limited runs.","s":WP+"Bad_Dragon"},
{"n":"TENGA","c":"Japan","f":"2005","seg":"Mainstream","kf":"design-led masturbators","d":"Tokyo maker founded in 2005 by Koichi Matsumoto; first product the Tenga Cup.","s":WP+"Tenga_(company)"}]
for n in new:
    if n['n'].lower() not in names: bd['b'].append(n)
json.dump(bd,open(BP+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(BP+'.tmp',BP)
