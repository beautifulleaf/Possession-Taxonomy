import json,os,copy,re
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'work/FIX_E3/bak/E3.json'))
bd=json.load(open(R+'work/FIX_E3/bak/E3_brands.json'))
mv=json.load(open(R+'work/FIX_E3/bak/E3_moves.json'))
def A(n,mk,y,dsc,s,v=None,dt='',a=''):
    return {"n":n,"a":a,"d":dsc,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
def V(n,mk='',y='',dsc=''): return {"n":n,"mk":mk,"y":y,"d":dsc}
def K(n,a,dsc,s,x,t=None,tg=None):
    k={"n":n,"a":a,"d":dsc,"s":s,"x":x}
    if t: k['t']=t
    return k
def find(name):
    for dp in d['depts']:
        for s in dp['s']:
            for i,k in enumerate(s['k']):
                if k['n']==name: return dp,s,i,k
def shelf(dept,sh):
    for dp in d['depts']:
        if dp['n']==dept:
            for s in dp['s']:
                if s['n']==sh: return s
def remove(name):
    dp,s,i,k=find(name); s['k'].pop(i); return k
W='https://en.wikipedia.org/wiki/'

# ---- E3-4 cymbals
cy_shelf=shelf('Drums & percussion','Cymbals')
voices=[('Ride cymbal','Ride'),('Crash cymbal','Crash'),('Hi-hat cymbal','Hi-hat'),('China cymbal','China'),('Splash cymbal','Splash'),('Effects and stack cymbal','Effects and stack')]
series_map=[ # (old name -> series)
('Zildjian K ride','Zildjian K'),('Zildjian K Constantinople ride','Zildjian K Constantinople'),('Zildjian K Constantinople crash','Zildjian K Constantinople'),
('Zildjian Kerope ride','Zildjian Kerope'),('Zildjian K Custom ride','Zildjian K Custom'),('Zildjian A ride','Zildjian A'),('Zildjian A Custom crash','Zildjian A Custom'),
('Paiste Formula 602 flat ride','Paiste Formula 602'),('Paiste Formula 602 Classic ride','Paiste Formula 602'),('Paiste Formula 602 Classic crash','Paiste Formula 602'),
('Paiste 2002 ride','Paiste 2002'),('Paiste 2002 crash','Paiste 2002'),('Paiste 2002 hi-hat','Paiste 2002'),('Paiste 2002 Novo China','Paiste 2002'),
('Paiste Signature ride','Paiste Signature'),('Paiste Signature crash','Paiste Signature'),('Paiste Signature hi-hat','Paiste Signature'),('Paiste Signature china','Paiste Signature'),
('Paiste Sound Edge hi-hat','Paiste Sound Edge'),
('Sabian HH ride','Sabian HH'),('Sabian HH hi-hats','Sabian HH'),('Sabian HHX ride','Sabian HHX'),
('Sabian AA crash','Sabian AA'),('Sabian AA Chinese','Sabian AA'),('Sabian AA splash','Sabian AA'),('Sabian AAX crash','Sabian AAX'),
('Sabian Stratus hi-hats','Sabian Stratus'),('Sabian Rocktagon','Sabian Rocktagon'),
('Meinl Byzance ride','Meinl Byzance'),('Meinl Byzance Vintage crash','Meinl Byzance'),
('Istanbul Agop ride','Istanbul Agop'),('Bosphorus ride','Bosphorus'),
('Traditional Chinese cymbal','Traditional Chinese cymbal'),('Krupa traditional splash','Zildjian traditional splash'),('Copeland-era Paiste splash','Paiste Copeland-era'),
('Zildjian FX Oriental China Trash','Zildjian FX'),('Zildjian FX stack','Zildjian FX'),('Sabian Max Stax','Sabian Max Stax'),('Sabian O-Zone','Sabian O-Zone'),
('Paiste bell and cup chime','Paiste bell and cup chime'),('Zildjian L80 Low Volume','Zildjian L80 Low Volume')]
smap=dict(series_map)
ser={}; before=0
for kn,vo in voices:
    k=find(kn)[3]
    for x in k['x']:
        before+=1
        sn=smap[x['n']]
        if sn not in ser:
            ser[sn]=A(sn,x['mk'],x['y'],x['d'],x['s'],[],x.get('dt',''),x.get('a',''))
        t=ser[sn]
        if not t['y'] and x['y']: t['y']=x['y']
        if x.get('dt') and x['dt'] not in t['dt']: t['dt']=(t['dt']+' · '+x['dt']).strip(' ·')
        if x.get('a') and x['a'] not in t['a']: t['a']=(t['a']+' · '+x['a']).strip(' ·')
        if x['v']:
            for v in x['v']:
                v2=dict(v); v2['n']=f"{vo}: {v['n']}"; t['v'].append(v2)
        else: t['v'].append(V(vo,x['mk'],x['y']))
# if series has versions only for some voices fine
cy_t=['ride','crash','hi-hat','china','splash','effects and stack','flat ride (no bell)','sizzle ride','crash/ride','swish / pang','mini hats (10–12 in)','stack (layered cymbals)','vented or holed','low-volume (perforated practice)','6–26 in by voice','thin','medium-thin','medium','medium-heavy','heavy','traditional (lathed) finish','brilliant (buffed) finish','unlathed / raw','patina / dark finish','B20 bell bronze','B8 bronze','B12 bronze','brass','phosphor bronze (Paiste Signature Bronze)']
cym=K('Cymbal','cymbals · ride · crash · hi-hats','Thin round plate of copper alloy struck with sticks or against another cymbal; series are the archetypes, voice and size the version.',W+'Cymbal',list(ser.values()),cy_t)
cy_shelf['k']=[cym]
cy_after=len(ser)

# ---- E3-5 saxophones
sx_shelf=shelf('Orchestral & band instruments','Saxophones')
sv=[('Alto saxophone','Alto'),('Tenor saxophone','Tenor'),('Soprano saxophone','Soprano'),('Baritone saxophone','Baritone')]
sax={}; sm=[]; st=[]; sb=0
for kn,vo in sv:
    k=find(kn)[3]
    for x in k['x']:
        sb+=1; key=x['n']
        if key not in sax:
            sax[key]=dict(x); sax[key]['v']=[]; sax[key]['_vo']=set()
        t=sax[key]
        if not t.get('y') and x.get('y'): t['y']=x['y']
        t['_vo'].add(vo)
        names={v['n'] for v in t['v']}
        for v in x['v']:
            if v['n'] not in names:
                t['v'].append(v); names.add(v['n'])
        if not x['v'] and vo not in names: t['v'].append(V(vo+' model',x['mk'],x['y']))
    for m in k.get('m',[]):
        if m not in sm: sm.append(m)
    for tt in k.get('t',[]):
        if tt not in st: st.append(tt)
for t in sax.values(): t.pop('_vo')
order=['Selmer Mark VI','Conn M series \'Naked Lady\'','Selmer Balanced Action','Selmer Super Balanced Action','King Super 20','Selmer Super Action 80 Series II','Selmer Series III','Selmer Reference 54','Yamaha 62 series','Yamaha Custom Z','Yanagisawa 901 / 902 series','Yanagisawa 99x soprano','Yanagisawa WO baritone','Keilwerth SX90R']
assert set(order)==set(sax), set(sax)^set(order)
sx_t=['soprano · alto · tenor · baritone (voice as version)']+[x for x in st if not x.startswith('student') or True]
sx=K('Saxophone','sax · saxophones','Single-reed woodwind with a conical brass body; model line is the archetype, voice (soprano, alto, tenor, baritone) the version.',W+'Saxophone',[sax[n] for n in order],['voice: soprano · alto · tenor · baritone']+st)
sx['m']=sm
sx_shelf['k']=[sx]
sax_after=len(order)

# ---- dups Helix / POG
def merge_dup(keep,drop,an):
    kk=find(keep)[3]; dd=find(drop)[3]
    a=[x for x in kk['x'] if x['n']==an][0]; b=[x for x in dd['x'] if x['n']==an][0]
    names={v['n'] for v in a['v']}
    for v in b['v']:
        if v['n'] not in names: a['v'].append(v)
    dd['x']=[x for x in dd['x'] if x['n']!=an]
merge_dup('Amp modeller','Multi-effects processor','Line 6 Helix')
merge_dup('Octave pedal','Pitch-shifter pedal','Electro-Harmonix POG')

# ---- E3-8 Subwoofer
remove('Subwoofer')

# ---- E3-7 partial moves
harp=remove('Harp')
os_=shelf('Orchestral & band instruments','Orchestral strings')
idxb=[i for i,k in enumerate(os_['k']) if k['n']=='Double bass'][0]
os_['k'].insert(idxb+1,harp)
xy=find('Xylophone')[3]
trad=[x for x in xy['x'] if x['n'] in('Balafon','Gyil','Amadinda')]
xy['x']=[x for x in xy['x'] if x['n'] not in('Balafon','Gyil','Amadinda')]
for x in trad:
    x['s']=W+'Xylophone'
    x['d']={'Balafon':'West African xylophone of the Mande peoples, with bars set over gourd resonators.','Gyil':'Pentatonic xylophone of Gur-speaking peoples, with 14 wooden keys over calabash resonators and a buzzing spider-silk membrane.','Amadinda':'Ugandan xylophone-like instrument of twelve pentatonic logs, with no gourd resonators, usually played by three people.'}[x['n']]
    x['v']=x.get('v',[]); x['mk']=''
tx=K('Traditional xylophone','balafon · gyil · log xylophone','Wooden-bar xylophone of African traditions, often with gourd resonators.',W+'Xylophone',trad,['gourd resonators','no resonators (log)'])
shelf('Drums & percussion','Hand & world percussion')['k'].append(tx)

# ---- E3-3
semi=find('Semi-hollow electric guitar')[3]
semi['x']+= [A('Gibson ES-345','Gibson','1959','Upscale ES-335 with stereo wiring and Varitone circuit; sits between the ES-335 and ES-355.',W+'Gibson_ES-345',[V('ES-345TD (sunburst)','Gibson','1959'),V('ES-345TDC (cherry)','Gibson','1959'),V('ES-345TDN (natural)','Gibson','1959'),V('ES-355TD-SV','Gibson','','fancier version of the 335 and 345')],'sunburst · cherry · natural · Varitone · stereo wiring',a='ES-345 · ES-355'),
 A('Epiphone Sheraton','Epiphone','1958','Thinline semi-hollow double-cutaway Epiphone with a Frequensator tailpiece and tree-of-life headstock inlay.',W+'Epiphone_Sheraton',[V('Original Sheraton','Epiphone','1958','New York single-coils, mini-humbuckers from 1961'),V('Sheraton II','Epiphone','1986–2014','fixed stop bar replaces Frequensator'),V('Sheraton II Pro','Epiphone','2014','ProBucker humbuckers with coil-splitting')],'natural · sunburst · cherry · ebony')]
hb=find('Hollow-body electric guitar')[3]
hb['x'].append(A('Gretsch 6122 Country Gentleman','Gretsch','','Gretsch hollow-body listed among the Chet Atkins-era models alongside the 6120.',W+'Gretsch_Country_Gentleman',[],''))
po=find('Pipe organ')[3]
po['x']=[A('Portative organ','','Middle Ages','Small lightweight pipe organ played with one hand while the other worked the bellows.',W+'Pipe_organ'),
 A('Positive organ','','Middle Ages','Larger than the portative but still portable pipe organ.',W+'Pipe_organ'),
 A('Theatre organ','','early 20th century','Pipe organ installed in theatres to accompany silent films, also in auditoria and wealthy homes.',W+'Pipe_organ'),
 A('Cavaillé-Coll organ','Aristide Cavaillé-Coll','19th century','Romantic-period organ that used the Barker lever to ease key action at higher wind pressures.',W+'Pipe_organ'),
 A('Schnitger organ','Arp Schnitger','Baroque','Baroque organ with balanced mechanical action, distinctive reeds and large Pedal and Rückpositiv divisions.',W+'Pipe_organ')]
ney=find('Ney')[3]
ney['x']=[A('Arabic ney','','','Seven-hole end-blown reed flute played with no mouthpiece.',W+'Ney'),
 A('Turkish ney','','','Seven-hole ney, often with a brass, horn or plastic mouthpiece at the top.',W+'Ney'),
 A('Persian ney','','','Six-hole ney with one hole on the back.',W+'Ney')]
hi=find('Hichiriki')[3]
hi['t']=['bamboo, about 18 cm','flat double reed','gagaku court instrument']

# ---- E3-1 new kinds
SG=shelf('Guitars & basses','Electric guitars')
d['depts'][0]['s'].insert(2,{"n":"Steel guitars","k":[
 K('Lap steel guitar','Hawaiian guitar · steel guitar','Pedal-less steel guitar played flat across the lap, with pitch changed by sliding a steel bar along the strings.',W+'Lap_steel_guitar',[
  A('Rickenbacker A22 "Frying Pan"','Rickenbacker','1935','Early solid electric Hawaiian guitar with a round body and long neck.',W+'Lap_steel_guitar',[V('Electro Bakelite Hawaiian 7-string','Rickenbacker','c. 1938'),V('B-6','Rickenbacker','1936')],'',a='Frying Pan · A25'),
  A('Fender Stringmaster','Fender','','Fender electric lap steel in multi-neck and eight-string forms.',W+'Lap_steel_guitar',[V('Fender Deluxe-8 (8-string)','Fender'),V('Champion','Fender')],'single or multiple necks · 6 or 8 strings'),
  A('Gibson double-neck lap steel','Gibson','','Double-neck E6/B11 lap steel of the type Don Helms played on Hank Williams recordings.',W+'Lap_steel_guitar',[],'E6 and B11 necks')],['6 or 8 strings','single neck · double neck · console (multi-neck)']),
 K('Pedal steel guitar','pedal steel','Seated horizontally mounted electric steel guitar whose foot pedals and knee levers change string pitches while notes sound.',W+'Pedal_steel_guitar',[
  A('Gibson Electraharp','Gibson','1940','Pedal-operated electric steel guitar based on Alvino Rey\'s design; only 43 sold.',W+'Pedal_steel_guitar'),
  A('Bigsby pedal steel','Bigsby','late 1940s','Paul Bigsby\'s cable-and-pulley pedal steel; his first, built in 1948 for Speedy West.',W+'Pedal_steel_guitar',[V('Emmons split-pedal Bigsby','Bigsby','c. 1954','split Bud Isaacs\' single pedal in two, standard in E9 tuning')]),
  A('Harlin Brothers Multi-Kord','Harlin Brothers','c. 1947','Indianapolis pedal steel whose pedals could raise or lower any combination of strings.',W+'Pedal_steel_guitar'),
  A('Sho-Bud','Sho-Bud','1957','Pedal steel maker founded by Buddy Emmons and Harold "Shot" Jackson, the first devoted solely to pedal steel.',W+'Pedal_steel_guitar')],['E9 · C6 tuning','single or double neck'])]})
folk=shelf('Folk & world instruments','Harps, zithers & bowed folk strings')
folk['k']+=[
 K('Autoharp','chord zither','Zither with chord bars whose damping pads mute every string outside the chosen chord.',W+'Autoharp',[
  A('Zimmermann autoharp','Charles F. Zimmermann','1882','Earliest damped-chord zither, from US Patent 257808 (filed 1881); small models by about 1885.',W+'Autoharp'),
  A('Oscar Schmidt autoharp','Oscar Schmidt','','Mainstream American autoharp; the 36-string chromatic type has 12, 15 or 21 chord bars.',W+'Autoharp',[V('Model A (1930 example)','Oscar Schmidt','1930')],'12, 15 or 21 chord bars · 36 strings'),
  A('Orthey Autoharp No. 136','','','Rare 48-string model tuned to G and D major.',W+'Autoharp')],['21-bar chromatic','Chromaharp "Caroler" (43 strings)']),
 K('Hurdy-gurdy','vielle à roue · Drehleier','Bowed string instrument in which a hand-cranked rosined wheel rubs the strings while keys press tangents against them.',W+'Hurdy-gurdy',[
  A('Organistrum','','early medieval','Large guitar-shaped early form that originally needed two players.',W+'Hurdy-gurdy'),
  A('Symphonia','','13th century','Smaller box-shaped medieval form with three strings and a diatonic keyboard.',W+'Hurdy-gurdy'),
  A('Vielle à roue','','18th century','Best-known modern French style with six strings: two melody and four drone.',W+'Hurdy-gurdy'),
  A('Tekerőlant','','','Hungarian hurdy-gurdy using a wedge-controlled buzzing bridge.',W+'Hurdy-gurdy')],['buzzing bridge (chien)','with or without sympathetic strings'])]
tun=shelf('Drums & percussion','Tuned & orchestral percussion')
tun['k'].append(K('Steelpan','steel drum · pan','Tuned percussion instrument from Trinidad and Tobago, made from cut-down oil drums and played with rubber-tipped sticks.',W+'Steelpan',[
 A('Ping Pong (single tenor)','','1940s','Soprano-range lead pan invented by Winston "Spree" Simon.',W+'Steelpan'),
 A('Double second','','','Alto-range pan pairs designed by Ellie Mannette.',W+'Steelpan'),
 A('Double tenor','','','Mezzo-soprano pan pairs by Bertie Marshall.',W+'Steelpan'),
 A('Cello pan','','','Baritone pan set designed by Ellie Mannette.',W+'Steelpan'),
 A('Six bass','','','Bass pan set of six drums designed by Ellie Mannette.',W+'Steelpan')],['circle-of-fifths note layout (lead)','chromed or painted']))
syn=shelf('Pianos & keyboards','Synthesizers')
syn['k']+=[
 K('Mellotron','tape keyboard','Electro-mechanical keyboard in which each key presses a length of magnetic tape against a playback head.',W+'Mellotron',[
  A('Chamberlin Music Master','Chamberlin','','Harry Chamberlin\'s California keyboard-driven tape instrument that inspired the Mellotron.',W+'Mellotron',[V('Music Master 600','Chamberlin')]),
  A('Mellotron Mark II','Mellotronics','1964','Double-manual Mellotron with banks and stations of sounds; about 160 made.',W+'Mellotron',[V('Mellotron Mk I','Mellotronics','1963','about 10 made')],'double manual'),
  A('Mellotron M400','Streetly Electronics','1970','35-note single-manual model, the most common and portable, with about 1,800 made.',W+'Mellotron',[V('M300','Mellotronics','1968','52-note single manual'),V('M4000','Streetly Electronics','2007','24 sounds, revival model')],'35 notes')],['tape frames','single or double manual']),
 K('Keytar','strap synthesizer','Electronic keyboard worn on a strap like a guitar, either with its own sound engine or as a controller.',W+'Keytar',[
  A('Moog Liberation','Moog Music','1980','Considered the first mass-produced strap synthesizer.',W+'Keytar'),
  A('Yamaha SHS-10','Yamaha','1987','32-minikey FM keytar with 25 voices and six-note polyphony.',W+'Keytar',[V('SHS-200','Yamaha','1988','49 keys')]),
  A('Roland AX-7','Roland','2001','45-key keytar with an infrared D-Beam effects interface.',W+'Keytar',[V('AX-Synth','Roland','2009'),V('Lucina AX-09','Roland','2010')]),
  A('Alesis Vortex','Alesis','2012','USB/MIDI keytar controller with eight drum pads and accelerometer tilt control.',W+'Keytar')],['onboard sounds','controller only']),
 K('Vocoder','voice synthesizer','Instrument that imposes the spectral shape of a voice on a synthesizer carrier signal.',W+'Vocoder',[
  A('Sennheiser VSM201','Sennheiser','','Hardware vocoder used by Neil Young on most of Trans (1982).',W+'Vocoder'),
  A('EMS Vocoder 2000','EMS','','Hardware vocoder used for the Cylon voices in the 1978 Battlestar Galactica.',W+'Vocoder'),
  A('Roland VP-330','Roland','','Keyboard vocoder and string machine used for the Soundwave voice in Transformers.',W+'Vocoder')],['filter-bank (channel) vocoder','keyboard vocoder'])]
nov=shelf('Folk & world instruments','Mechanical & novelty instruments')
nov['k']+=[
 K('Omnichord','','Suzuki electronic autoharp-like instrument with a touch-sensitive strum plate producing harp-like arpeggios.',W+'Omnichord',[
  A('Suzuki Omnichord OM-27','Suzuki','1981','Original Omnichord; production ran 1981–1996.',W+'Omnichord',[V('OM-36','Suzuki','1984'),V('OM-84','Suzuki','1984'),V('OM-250','Suzuki','1989','MIDI out'),V('OM-300','Suzuki','early 1990s','MIDI in and chord sequencer'),V('Q-Chord','Suzuki','1999','redesigned re-release'),V('OM-108','Suzuki','2024','new analogue model')])],['strum plate']),
 K('Stylophone','','Miniature stylus-played analogue synthesizer invented by Brian Jarvis in 1967.',W+'Stylophone',[
  A('Dubreq Stylophone','Dubreq','1967','Original pocket synthesizer sold in standard, treble and bass versions; about three million sold.',W+'Stylophone',[V('350S','Dubreq','1971','more keys, wah-wah, two styluses'),V('S1','Dubreq','2007','revival model'),V('Beatbox','Dubreq','2009'),V('S2','Dubreq','2012','limited analogue edition'),V('Gen X-1','Dubreq','2017')])],['stylus keyboard'])]
# E3-2
rs=shelf('Recording & live sound','Interfaces, mixers & recorders')
rs['k']+=[
 K('Outboard processor','studio compressor · channel EQ','Rack or module processor for compression, equalisation or preamplification in a recording chain.',W+'1176_Peak_Limiter',[
  A('UREI 1176','UREI','1967','Bill Putnam\'s FET peak limiter that replaced the tube 175 and 176.',W+'1176_Peak_Limiter',[V('Blue stripe (Rev A and AB)','UREI','1967'),V('1176LN (Rev C)','UREI','1970','low noise, black faceplate'),V('Rev H','UREI','','silver faceplate, last of the original company'),V('Universal Audio reissue','Universal Audio','2000'),V('Rev AE Anniversary Edition','Universal Audio','2008','limited to 500')],'revisions A–H'),
  A('Teletronix LA-2A','Teletronix','1962','Hand-wired valve leveling amplifier designed by Jim Lawrence.',W+'LA-2A_Leveling_Amplifier',[V('Gray version','Teletronix','mid-1960s'),V('Silver version','UREI','late 1960s'),V('UREI reissue','UREI','1979'),V('Harman/JBL reissue','Harman','1992'),V('Universal Audio reissue','Universal Audio','1999')],'production ended 1969'),
  A('Neve 1073','Neve','1970','Rupert Neve\'s class-A mic/line preamplifier with three-band EQ, made for the A88 console.',W+'Neve_Electronics',[V('1081','Neve','1973','for the 8048 console'),V('1084','Neve')],'rack-mounted standalone'),
  A('Pultec EQP-1A','Pultec','1961','Passive tube equaliser; updated EQP-1 with extra low and high settings.',W+'Pultec',[V('EQP-1','Pultec','1956'),V('EQP-1A3','Pultec','1971','2U version'),V('Pulse Techniques LLC reissue','Pultec','2000'),V('Tube-Tech PE 1A','Tube-Tech','1985','inspired'),V('Manley','Manley','1990','inspired')])],['compressor · limiter · EQ · preamp']),
 K('Multitrack recorder','Portastudio · tape multitracker','Recorder that stores several tracks separately for later mixing, on reel tape or cassette.',W+'Portastudio',[
  A('Ampex Sel-Sync 8-track','Ampex','1955','First Sel-Sync multitrack, an 8-track one-inch machine Les Paul called the Octopus.',W+'Multitrack_recording'),
  A('TEAC 2340','TEAC','1973','Home four-track reel recorder.',W+'Multitrack_recording'),
  A('TEAC 144 Portastudio','TEAC','1979','First four-track cassette Portastudio, with a built-in four-channel mixer.',W+'Portastudio',[V('TASCAM 244','TASCAM','1982','parametric EQ, dbx Type II'),V('TASCAM 424','TASCAM','c. 1996','MkII and MkIII versions')],'4-track cassette'),
  A('Fostex Multitracker','Fostex','1981','Fostex line of cassette multitrack recorders.',W+'Portastudio',[V('Fostex 250','Fostex','1981')]),
  A('Yamaha MT1X','Yamaha','1986','Yamaha cassette multitrack Portastudio.',W+'Portastudio')],['reel-to-reel','cassette','digital'])]
# Marshall
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      for x in k.get('x',[]):
        if x['mk']=='Marshall': x['mk']='Marshall Amplification'
        for v in x['v']:
          if v.get('mk')=='Marshall': v['mk']='Marshall Amplification'
# brands
B=bd['b']
names={b['n'].lower() for b in B}
B[:]=[b for b in B if b['n']!='Marshall']
for b in B:
    if b['n']=='Marshall Amplification' and "Guv'nor" not in b['sig']: b['sig'].append("Guv'nor")
    if 'Marshall' in b.get('rel',[]): b['rel']=['Marshall Amplification' if r=='Marshall' else r for r in b['rel']]
def Br(n,c,f,seg,kf,dsc,s,sig=None):
    if n.lower() in {b['n'].lower() for b in B}: return
    B.append({"n":n,"c":c,"f":f,"seg":seg,"d":dsc,"lines":[],"eras":[],"sig":sig or [],"sc":[],"rel":[],"s":s,"kf":kf})
AR='Artisan & independent'
Br('Theobald Boehm','','',AR,'Boehm flute','Flautist and silversmith who patented the key system of the modern flute in 1847.',W+'Western_concert_flute')
Br('Albert Cooper','','',AR,'flute scale','Flute maker who adapted the Boehm flute in the 1950s with an A440 scale and reshaped embouchure hole.',W+'Western_concert_flute')
Br('Johan Brögger','','',AR,'flute design','Flute maker who refined the Boehm design in the 1980s, fixing key alignment and spring issues.',W+'Western_concert_flute')
Br('Eva Kingma','','',AR,'Kingma system flutes','Flute maker associated with the Kingma System flute.',W+'Brannen_Brothers')
Br('Peter Bressan','','',AR,'baroque recorders','Baroque recorder maker whose instruments are widely copied.',W+'Peter_Bressan')
Br('Jacob Denner','','',AR,'baroque recorders','Early 18th-century woodwind maker whose recorders are widely copied.',W+'Jacob_Denner')
Br('Jean-Hyacinth Rottenburgh','','',AR,'baroque recorders','Woodwind maker of the Rottenburgh family, active 1672–1756.',W+'Rottenburgh_family')
Br('Fred Morgan','','',AR,'Ganassi-type recorders','Recorder maker linked to the Ganassi-type recorder.',W+'Recorder_(musical_instrument)')
Br('Peter Harlan','','',AR,'German-fingering recorders','Developed German fingering for the recorder in the early twentieth century.',W+'Recorder_(musical_instrument)')
Br('Colin Ross','','',AR,'Scottish smallpipes','Pipemaker who helped redevelop the Scottish smallpipe, in its modern form since the early 1980s.',W+'Scottish_smallpipes')
Br('Giuseppe Donati','Italy','',AR,'ocarinas','Italian inventor of the modern ocarina, made in 1853 at Budrio near Bologna.',W+'Ocarina')
Br('John Taylor','United Kingdom','',AR,'English-fingering ocarina','English maker who in 1964 devised the four-hole English fingering for pendant ocarinas.',W+'Ocarina')
Br('Aristide Cavaillé-Coll','','',AR,'Romantic organs','Romantic-period organ builder who introduced the Barker lever.',W+'Pipe_organ')
Br('Arp Schnitger','','',AR,'Baroque organs','Baroque organ builder known for balanced mechanical actions and distinctive reeds.',W+'Pipe_organ')
Br('Sho-Bud','United States','1957','Specialist','pedal steel guitars','Pedal steel maker founded by Buddy Emmons and Harold "Shot" Jackson.',W+'Pedal_steel_guitar')
Br('Harlin Brothers','United States','',AR,'Multi-Kord','Indianapolis maker of the c. 1947 Multi-Kord pedal steel.',W+'Pedal_steel_guitar',['Multi-Kord'])
Br('Oscar Schmidt','United States','','Specialist','autoharps','Autoharp maker, now a division of U.S. Music Corporation.',W+'Autoharp')
Br('Charles F. Zimmermann','','',AR,'autoharp patent','Patentee of the damped-chord zither (US Patent 257808, 1882).',W+'Autoharp')
Br('Dubreq','United Kingdom','','Specialist','Stylophone','London maker of the Stylophone.',W+'Stylophone')
Br('Mellotronics','United Kingdom','1963','Specialist','Mellotrons','Birmingham maker (as Bradmatic/Mellotronics) of the original Mellotrons, renamed Streetly Electronics in 1970.',W+'Mellotron')
Br('Streetly Electronics','United Kingdom','1970','Specialist','Mellotrons','Made the Mellotron 1970–1986 and again from 2007.',W+'Mellotron')
Br('Chamberlin','United States','',AR,'tape keyboards','Harry Chamberlin\'s California company, maker of the first commercial keyboard-driven tape instruments.',W+'Mellotron')
Br('Moog Music','','','Premium','analog synthesizers','Maker of the Moog Liberation strap synthesizer (1980).',W+'Keytar')
Br('EMS','','','Specialist','synthesizers, vocoders','Maker of the EMS Vocoder 2000.',W+'Vocoder')
Br('UREI','','','Professional & flagship','studio compressors','Built the original 1176 limiter units from 1967.',W+'1176_Peak_Limiter')
Br('Universal Audio','United States','1958','Professional & flagship','studio compressors','Founded 1958 by Bill Putnam Sr. and refounded in 1999; reissued the 1176 and LA-2A.',W+'LA-2A_Leveling_Amplifier')
Br('Teletronix','United States','1958','Specialist','LA-2A','Pasadena company founded by Jim Lawrence, maker of the LA-2A leveling amplifier (1962).',W+'LA-2A_Leveling_Amplifier')
Br('Neve','','','Professional & flagship','consoles and preamps','Maker of the 1073 preamplifier and equaliser, designed by Rupert Neve in 1970.',W+'Neve_Electronics')
Br('Pultec','United States','1953','Specialist','passive equalisers','Pulse Techniques, founded 1953 in Teaneck, New Jersey; revived in 2000.',W+'Pultec')
Br('Tube-Tech','','','Specialist','valve equalisers','Maker of the PE 1A, a Pultec-inspired equaliser (1985).',W+'Pultec')
Br('Manley','','','Specialist','valve processors','Maker of a Pultec-inspired equaliser (1990).',W+'Pultec')
Br('Ampex','','','Professional & flagship','tape recorders','Developed the first Sel-Sync multitrack recorder in 1955.',W+'Multitrack_recording')
Br('TEAC','','','Specialist','tape recorders','Made the 1979 TEAC 144, the first cassette Portastudio.',W+'Portastudio')
Br('TASCAM','','','Specialist','Portastudio','Owner of the Portastudio trademark.',W+'Portastudio')
Br('Fostex','','','Specialist','Multitracker','Maker of the Multitracker cassette recorders from 1981.',W+'Portastudio')
mv['out']=mv.get('out',[])
json.dump(d,open(R+'work/FIX_E3/E3.new.json','w'),ensure_ascii=False,indent=1)
json.dump(bd,open(R+'work/FIX_E3/E3_brands.new.json','w'),ensure_ascii=False,indent=1)
print('cymbal archetypes',before,'->',cy_after,'sax',sb,'->',sax_after,'brands',len(B))
