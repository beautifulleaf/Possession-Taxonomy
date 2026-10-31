import json,re,sys,os,copy
R='/home/user/Possession-Taxonomy/rebuild/'
D=json.load(open(R+'out/D3.json'));B=json.load(open(R+'out/D3_brands.json'))
reg={x['n'].lower():x for x in B['b']}
def country(mk):
    if not mk: return ''
    k=mk.lower()
    if k in reg and reg[k].get('c'): return reg[k]['c']
    for n,x in reg.items():
        if x.get('c') and (n.startswith(k) or k.startswith(n)): return x['c']
    return MAN.get(mk,'')
MAN={'Revox':'Switzerland','Fostex':'Japan','Victor Talking Machine Company':'United States','Koss Corporation':'United States','Stax Ltd':'Japan','Etymotic Research':'United States','Campfire Audio':'United States','64 Audio':'United States','JH Audio':'United States','Moondrop Audio':'China','Truthear':'China','Quad':'United Kingdom','Magnepan':'United States','MartinLogan':'United States','Avantgarde Acoustic':'Germany','Altec Lansing':'United States','Klipsch':'United States','Bowers & Wilkins':'United Kingdom','Linn':'United Kingdom','Wilson Audio':'United States','Philco':'United States','Garrard':'United Kingdom','Thorens':'Switzerland','EMT':'Germany','Lenco':'Switzerland','Michell':'United Kingdom','Micro Seiki':'Japan','Rega':'United Kingdom','Pro-Ject':'Austria','SME':'United Kingdom','Ortofon':'Denmark','Denon':'Japan','Shure':'United States','Grado Labs':'United States','Audio-Technica':'Japan','Leak':'United Kingdom','Naim':'United Kingdom','Mark Levinson':'United States','Threshold':'United States','Pass Labs':'United States','Accuphase':'Japan','Luxman':'Japan','Cyrus':'United Kingdom','Arcam':'United Kingdom','NAD':'Canada','McIntosh':'United States','Sansui':'Japan','Pioneer':'Japan','Marantz':'Japan','dCS':'United Kingdom','Benchmark':'United States','Chord Electronics':'United Kingdom','Schiit':'United States','RME':'Germany','Woo Audio':'United States','Musical Fidelity':'United Kingdom','Little Dot':'China','TEAC':'Japan','Akai':'Japan','Nakamichi':'Japan','Tandberg':'Norway','Meridian':'United Kingdom','Slim Devices':'United States','Diamond Multimedia':'United States','Creative':'Singapore','iRiver':'South Korea','Microsoft':'United States','SaeHan Information Systems':'South Korea','Compaq':'United States','Archos':'France','Aiwa':'Japan','Toshiba':'Japan','Panasonic':'Japan','JVC':'Japan','Conion':'Japan','Sharp':'Japan','Ekco':'United Kingdom','Roberts Radio':'United Kingdom','Tivoli Audio':'United States','Regency':'United States','Braun':'Germany','Zenith':'United States','Grundig':'Germany','Tecsun':'China','Brionvega':'Italy','Wurlitzer':'United States','Seeburg':'United States','Orphéau':'France','Bang & Olufsen':'Denmark','Kodak':'United States','Leica':'Germany','Braun Foto Technik':'Germany','Rollei':'Germany','Bolex':'Switzerland','Oppo Digital':'United States','Magnetar':'China','Kaleidescape':'United States','Philips':'Netherlands','Spendor':'United Kingdom','Harbeth':'United Kingdom','ProAc':'United Kingdom','KEF':'United Kingdom','Wharfedale':'United Kingdom','Yamaha':'Japan','Acoustic Research':'United States','Advent':'United States','JBL':'United States','Dynaudio':'Denmark','Tannoy':'United Kingdom','Sennheiser':'Germany','Beyerdynamic':'Germany','AKG':'Austria','Audeze':'United States','HiFiMAN':'China','Focal':'France','Apple':'United States','Bose':'United States','Sony':'Japan','Stax':'Japan','Beats':'United States','Samsung':'South Korea','Technics':'Japan','Shokz':'China','Michell Engineering':'United Kingdom','Dual':'Germany','Mitsubishi':'Japan','Sound United':'United States'}

W='https://en.wikipedia.org/wiki/'
CH='https://www.channelnews.com.au/samsung-dominated-tv-market-in-2024-gained-oled-share-from-lg/'
EQ='https://equalocean.com/news/2025022421338-combined-shipments-chinese-tv-brands-surpassed-south-korea-first-time'
SB='https://t2online.in/tech/tech-news/samsung-holds-global-soundbar-lead-for-12th-straight-year/2004164'
TWS='https://m.gsmarena.com/canalys_global_tws_market_grows_18_as_apple_remains_undisputed_leader-amp-67892.php'
TC='https://techcrunch.com/2020/02/17/smart-speaker-sales-reached-new-record-of-146-9m-in-2019-up-70-from-2018/'
SN=W+'Sixteen'  # placeholder unused
def V(n,mk,y='',d=''): return {'n':n,'mk':mk,'y':y,'d':d}
def E(n,d,mk,y,s,own,tier,cty,g,v=None,a='',own_y='',role=None):
    e={'n':n,'a':a,'d':d,'mk':mk,'y':y,'s':s,'own':own,'tier':tier,'cty':cty,'own_y':own_y,'g':g}
    if v: e['v']=v
    if role: e['role']=role
    return e
GG='Global group';NC='National champion';IN='Independent'
# facts for roles from pages fetched this batch
ROLE={'Sony MDR-V6 / MDR-7506':('landmark',W+'Sony_MDR-7506','Sony introduced the MDR-V6 in 1985; reviewers called it almost the industry standard for location sound and "the industry favorite".'),
'Technics SL-1200':('landmark',W+'Technics_SL-1200','Introduced in 1972; since 1979 the SL-1200MK2 and its successors have been the most common turntables for DJing, with sales above 3 million.'),
'Linn Sondek LP12':('landmark',W+'Linn_Sondek_LP12','Introduced in 1972 with a suspended sub-chassis; Hi-Fi Choice called it the most important hi-fi component ever sold in the UK.'),
'BBC LS3/5A':('landmark',W+'LS3/5A','Compact monitor derived from the BBC LS3/5 in 1974; eleven companies held licences to build it.'),
'Quad ESL':('origin',W+'Quad_Electrostatic_Loudspeaker','Launched in 1957 as the world\'s first production full-range electrostatic loudspeaker.'),
'Koss SP/3 and Pro4':('origin',W+'Headphones','John C. Koss produced the first stereo headphones in 1958.'),
'Sony Walkman (cassette)':('origin',W+'Walkman','The TPS-L2 of 1979 is described as the world\'s first low-cost personal stereo.'),
'Apple iPod':('landmark',W+'IPod','Released in November 2001; Apple called it the best-selling digital music player of all time in 2007.')}
VADD={'Quad ESL':[V('ESL-57','Quad','1957','original, produced until 1985'),V('ESL-63','Quad','1981','launched at CES, last built 1999'),V('ESL-988 / ESL-989','Quad','','successors after 1999')]}
CTYFIX={'BBC LS3/5A':'United Kingdom'}
def yk(y):
    m=re.search(r'\d{4}',str(y));return int(m.group()) if m else 9999
removed={}
def nl_for(kn): return f"One entry is a {kn.lower()} model line or lineage that a cited reference lists or calls classic; generations and revisions are versions."
def sel_for(kn,n): return (f"No whole-space reference for {kn.lower()} lines was fetched. The list follows the lineages named by the page cited on each entry (Wikipedia, maker, review and museum pages), cut to lines such a page treats as notable; current catalogue models are not entries. Covers {n} lines; no fetched reference counts the whole space.")
for dp in D['depts']:
    for s in dp['s']:
        for k in s['k']:
            if k.get('m'): removed[k['n']]=len(k['m'])
            k.pop('m',None)
# market kinds
def kind(name):
    for dp in D['depts']:
        for s in dp['s']:
            for k in s['k']:
                if k['n']==name: return k,s,dp
    raise KeyError(name)
def setmk(k,nl,sel,entries,xg):
    k['x']=entries;k['nl']=nl;k['sel']=sel;k['xg']=xg;k.pop('r',None)
    k['x'].sort(key=lambda e:(['Global group','National champion','Independent','Craft & indie','Own label'].index(e['tier']),yk(e['y']),e['n']))
for e_ in []: pass
# --- Television
k,s,dp=kind('Television')
k['tt']=[t for t in k['tt'] if t[0]!='Panel']
sony_s=k['s']
setmk(k,"One entry is a television brand sold under its own name; model ranges are versions, and panel technology is a kind of its own.",
"Market-first. Brands follow the Omdia 2024 shipment ranking as reported by channelnews.com.au and equalocean.com and Counterpoint's Q4 2024 order (Samsung, TCL, Hisense, LG), plus Vizio and Philips; owners and countries come from the Wikipedia page cited on each entry. Covers 8 brands; no fetched reference lists every television brand.",
[E('Samsung','South Korean maker that Wikipedia says has been the largest television maker by revenue every year since 2006.','Samsung','',W+'Samsung_Electronics','Samsung Electronics',GG,'South Korea','Global group: Samsung Electronics',[V('OLED S95F','Samsung'),V('OLED S90F','Samsung'),V('Neo QLED 4K QN80H','Samsung'),V('The Frame','Samsung')]),
 E('LG','South Korean maker owned by LG Corporation, which holds about a third of it.','LG','',W+'LG_Electronics','LG Electronics',GG,'South Korea','Global group: LG Electronics',[V('OLED C6','LG'),V('OLED G6','LG'),V('QNED86','LG'),V('Mini RGB MRGB86','LG')]),
 E('TCL','Chinese maker founded in 1981 and partly state-owned; TCL Electronics, a subsidiary, makes its televisions.','TCL','1981',W+'TCL_Technology','TCL Technology',GG,'China','Global group: TCL Technology',[V('QLED T6D','TCL')]),
 E('Hisense','Chinese maker from Qingdao; it agreed to buy 95 % of Toshiba Visual Solutions in November 2017.','Hisense','1969',W+'Hisense','Qingdao Hisense Electric Holdings Co., Ltd.',GG,'China','Global group: Hisense'),
 E('Toshiba TV','Japanese television brand run since the 2017 agreement as an independent subsidiary of Hisense.','Toshiba','',W+'Hisense','Hisense',GG,'Japan','Global group: Hisense',own_y='2017'),
 E('Sony BRAVIA','Japanese television range sold under the BRAVIA name.','Sony','',sony_s,'Sony',GG,'Japan','Global group: Sony',[V('BRAVIA 8 II','Sony'),V('BRAVIA 9 II','Sony'),V('BRAVIA 7 II','Sony')]),
 E('Xiaomi TV','Chinese maker founded in 2010; Omdia counts it with TCL and Hisense in a 31.3 % combined share of 2024 shipments.','Xiaomi','2010',W+'Xiaomi','Xiaomi',GG,'China','Global group: Xiaomi'),
 E('Vizio','American brand founded in 2002 as V Inc.; Wikipedia says it was the second largest seller of flat-panel televisions in the US in 2020.','Vizio','2002',W+'Vizio','Walmart',NC,'United States','National champion: United States',own_y='2024'),
 E('Philips TV','Dutch-origin brand whose televisions are made by TP Vision, a wholly owned subsidiary of TPV Technology.','Philips','',W+'TP_Vision','TP Vision (TPV Technology)',IN,'Netherlands','Independent: TPV Technology'),
],'by market tier, then owner group')
k['dept_ms']=True
dp['ms']=[{"mkt":"Global televisions, units shipped","who":"Samsung","share":"28.3 %","yr":2024,"s":CH,"note":"Omdia as quoted by channelnews.com.au, which says the figure is not in Omdia's newsroom; Samsung's 19th year at first"},
{"mkt":"Global televisions, units shipped","who":"TCL, Hisense and Xiaomi combined","share":"31.3 %","yr":2024,"s":EQ,"note":"Omdia; ahead of Samsung and LG combined for the first time"},
{"mkt":"Global televisions, units shipped","who":"Samsung and LG combined","share":"28.4 %","yr":2024,"s":EQ,"note":"Omdia, as summarised by equalocean.com"},
{"mkt":"US flat-panel televisions","who":"Vizio","share":"second largest seller","yr":2020,"s":W+'Vizio',"note":"ranking only; no share given"}]
del k['dept_ms']
# panel kinds
rp,_,_=kind('Rear-projection television')
def newkind(n,a,d,s_,tt,after='Television'):
    nk={'n':n,'a':a,'d':d,'s':s_,'tt':tt,'nl':'','sel':'','xg':''}
    return nk
oled=newkind('OLED television','QD-OLED television','Television whose picture comes from self-lit organic diodes, so each pixel makes its own light.',CH,[['Emitter',['WOLED','QD-OLED']],['Size',['42–55 in','65–77 in','83 in and up']]])
lcd=newkind('LCD television (LED-backlit)','LED-LCD · QLED · Mini-LED','Television with a liquid-crystal panel lit from behind, in plain LED, quantum-dot (QLED) or Mini-LED form.',CH,[['Backlight',['LED','Quantum dot (QLED)','Mini-LED','RGB Mini-LED']],['Size',['32–43 in','50–65 in','75 in and up']]])
for nk in(oled,lcd):
    for f in('nl','sel','xg'): nk.pop(f)
s['k'][s['k'].index(k)+1:s['k'].index(k)+1]=[oled,lcd]
# --- Soundbar
k,s,dp2=kind('Soundbar')
setmk(k,"One entry is a soundbar brand sold under its own name; model ranges are versions.",
"Market-first. Brands follow the FutureSource 2025 ranking quoted by t2online.in and the maker pages cited on each entry. Covers 4 brands; no fetched reference lists every soundbar brand.",
[E('Samsung soundbars','South Korean maker that FutureSource ranks first in global soundbars for the twelfth year.','Samsung','',SB,'Samsung Electronics',GG,'South Korea','Global group: Samsung Electronics'),
 E('Sony soundbars','Japanese range that includes the BRAVIA Theater bars.','Sony','',k['s'],'Sony',GG,'Japan','Global group: Sony',[V('BRAVIA 9 Soundbar','Sony')]),
 E('Sonos soundbars','American maker of Wi-Fi soundbars; Playbar came in 2013, Beam in 2018 and Arc in 2020.','Sonos','2013',W+'Sonos','Sonos, Inc.',IN,'United States','Independent',[V('Playbar','Sonos','2013'),V('Beam','Sonos','2018'),V('Beam (Gen 2)','Sonos'),V('Arc','Sonos','2020'),V('Arc Ultra','Sonos','2024'),V('Ray','Sonos')]),
 E('Bose soundbars','American soundbar range from a privately held company majority-owned by MIT.','Bose','',W+'Bose_Corporation','Bose Corporation',IN,'United States','Independent')],'by market tier, then owner group')
dp2['ms']=[{"mkt":"Global soundbars, revenue","who":"Samsung","share":"21.5 %","yr":2025,"s":SB,"note":"FutureSource Worldwide Home Audio Quarterly Tracker; twelfth year at first"},
{"mkt":"Global soundbars, units shipped","who":"Samsung","share":"19.7 %","yr":2025,"s":SB,"note":"FutureSource"}]
# Wi-Fi multiroom, portable BT
k,_,_=kind('Wi-Fi and multi-room speakers')
setmk(k,"One entry is a multi-room speaker brand sold under its own name; model ranges are versions.","Sonos is the only brand cited by a fetched page for this kind. Covers 1 brand; no fetched reference lists every multi-room speaker brand.",
[E('Sonos wireless speakers','American maker of the Wi-Fi speaker system; Play:5 began as the ZonePlayer S5 in 2009.','Sonos','2009',W+'Sonos','Sonos, Inc.',IN,'United States','Independent',[V('Play:5 (ZonePlayer S5)','Sonos','2009'),V('One','Sonos'),V('Era 100','Sonos'),V('Era 300','Sonos'),V('Five','Sonos')])],'by market tier, then owner group')
k,_,_=kind('Portable Bluetooth speakers')
setmk(k,"One entry is a portable speaker brand sold under its own name; model ranges are versions.","Only brands whose owner a fetched page states are entries. Covers 1 brand; no fetched reference lists every portable speaker brand.",
[E('JBL portable speakers','American brand of Harman International, which Samsung Electronics has owned since 2017.','JBL','1946',W+'Harman_International','Samsung Electronics (through Harman International)',GG,'United States','Global group: Samsung Electronics',[V('Flip 7','JBL'),V('Charge 6','JBL'),V('Boombox 4','JBL'),V('PartyBox 720','JBL')],own_y='2017')],'by market tier, then owner group')
# --- Smart speakers
k,s,dp3=kind('Smart speaker')
setmk(k,"One entry is a smart speaker brand or range sold under its own name; generations and sizes are versions.",
"Market-first. Brands follow the vendors that Strategy Analytics ranked for 2019 as reported by TechCrunch, with release years from the pages cited on each entry. Covers 7 ranges; no fetched reference lists every smart speaker.",
[E('Amazon Echo','Amazon\'s voice-assistant speaker range, announced in November 2014.','Amazon','2014',W+'Amazon_Echo','Amazon',GG,'United States','Global group: Amazon',[V('Echo Dot','Amazon','2016'),V('Echo Studio','Amazon','2019'),V('Echo Dot Max','Amazon','2025')]),
 E('Google Home and Nest speakers','Google\'s speaker range, sold under the Nest name since July 2018.','Google','',W+'Google_Nest','Alphabet Inc.',GG,'United States','Global group: Alphabet',[V('Google Home','Google'),V('Home Mini','Google'),V('Home Max','Google')]),
 E('Apple HomePod','Apple\'s Siri speaker, released in February 2018.','Apple','2018',W+'HomePod','Apple Inc.',GG,'United States','Global group: Apple',[V('HomePod','Apple','2018'),V('HomePod mini','Apple','2020'),V('HomePod (2nd generation)','Apple','2023')]),
 E('Harman Kardon Invoke','Cortana speaker from Harman Kardon, a Harman brand owned by Samsung since 2017.','Harman Kardon','',W+'Harman_International','Samsung Electronics (through Harman International)',GG,'United States','Global group: Samsung Electronics',own_y='2017'),
 E('Baidu smart speakers','Chinese vendor that Strategy Analytics said gained share in 2019.','Baidu','',TC,'Baidu',NC,'China','National champion: China'),
 E('Alibaba smart speakers','Chinese vendor that Strategy Analytics said gained share in 2019.','Alibaba','',TC,'Alibaba Group',NC,'China','National champion: China'),
 E('Xiaomi smart speakers','Chinese vendor that Strategy Analytics said gained share in 2019.','Xiaomi','',TC,'Xiaomi',NC,'China','National champion: China')],'by market tier, then owner group')
dp3['ms']=[{"mkt":"Global smart speakers, units shipped","who":"Amazon","share":"26.2 %","yr":2019,"s":TC,"note":"Strategy Analytics; 33.7 % in 2018"},
{"mkt":"Global smart speakers, units shipped","who":"Google","share":"20.3 %","yr":2019,"s":TC,"note":"Strategy Analytics; 25.9 % in 2018"},
{"mkt":"Global smart speakers, units shipped","who":"Apple","share":"4.7 %","yr":2019,"s":TC,"note":"Strategy Analytics; sixth place; Baidu, Alibaba and Xiaomi gained share but no figures given"}]
k,_,_=kind('Smart display')
setmk(k,"One entry is a smart display brand or range sold under its own name; sizes and generations are versions.","Follows the two ranges named by the pages cited on each entry. Covers 2 ranges; no fetched reference lists every smart display.",
[E('Amazon Echo Show','Amazon\'s screen-fronted Echo, introduced in May 2017.','Amazon','2017',W+'Amazon_Echo','Amazon',GG,'United States','Global group: Amazon',[V('Echo Show 5','Amazon'),V('Echo Show 8','Amazon'),V('Echo Show 15','Amazon'),V('Echo Show 21','Amazon')]),
 E('Google Nest Hub','Google\'s smart display; the Home Hub was renamed Nest Hub at I/O on 7 May 2019.','Google','2019',W+'Google_Nest','Alphabet Inc.',GG,'United States','Global group: Alphabet',[V('Nest Hub (2nd gen)','Google'),V('Nest Hub Max','Google','2019')])],'by market tier, then owner group')
k,_,_=kind('Smart-home hub')
k['r']=[];k['x']=[];k.pop('r')
# --- True wireless earbuds
k,s,dp4=kind('True wireless earbuds')
own={'Apple AirPods':('Apple Inc.',GG,'United States'),'Apple AirPods Pro':('Apple Inc.',GG,'United States'),'Sony WF-1000X':('Sony',GG,'Japan'),'Samsung Galaxy Buds':('Samsung Electronics',GG,'South Korea'),'Bose QuietComfort Earbuds':('Bose Corporation',IN,'United States')}
for x in k['x']:
    o=own[x['n']];x['own'],x['tier'],x['cty']=o;x['own_y']='';x['g']=o[1]+': '+o[0]
k['x']+=[E('Xiaomi earbuds','Chinese range; Canalys had Xiaomi second in Q1 2025 with 11.5 % of TWS shipments.','Xiaomi','',TWS,'Xiaomi',GG,'China','Global group: Xiaomi'),
 E('Huawei FreeBuds','Chinese range; Canalys had Huawei fourth in Q1 2025 with 6.0 % of TWS shipments.','Huawei','',TWS,'Huawei',GG,'China','Global group: Huawei'),
 E('boAt Airdopes','Indian brand; Canalys had boAt fifth in Q1 2025 with 4.9 % of TWS shipments.','boAt','',TWS,'owner not stated',NC,'India','National champion: India'),
 E('Beats earbuds','American brand founded in 2006 and bought by Apple in 2014.','Beats','2006',W+'Beats_Electronics','Apple Inc.',GG,'United States','Global group: Apple',own_y='2014')]
k['nl']="One entry is a true wireless earbud brand or range sold under its own name; generations are versions."
k['sel']="Market-first. Brands follow the Canalys Q1 2025 ranking quoted by GSMArena (Apple, Xiaomi, Samsung, Huawei, boAt) plus the earlier entries; owners come from the pages cited on each entry. Covers 9 ranges; no fetched reference lists every earbud brand."
k['xg']='by market tier, then owner group'
dp4['ms']=[{"mkt":"Global true wireless earbuds, units shipped","who":w,"share":sh,"yr":2025,"s":TWS,"note":"Canalys, Q1 2025, 78.3 million units in all"} for w,sh in [("Apple","23.3 %"),("Xiaomi","11.5 %"),("Samsung","7.1 %"),("Huawei","6.0 %"),("boAt","4.9 %")]]
done={'Television','Soundbar','Wi-Fi and multi-room speakers','Portable Bluetooth speakers','Smart speaker','Smart display','True wireless earbuds','Smart-home hub'}
# --- lineage kinds
for dp in D['depts']:
    for s in dp['s']:
        for k in s['k']:
            if k['n'] in done: continue
            xs=k.get('x',[])
            if not xs:
                k.pop('r',None);continue
            for x in xs:
                c=CTYFIX.get(x['n']) or country(x.get('mk',''))
                x['g']=c or 'Open designs (no maker)'
                if x['n'] in ROLE:
                    r,u,t=ROLE[x['n']];x['role']=r;x['s']=u;x['d']=t
                for ex in VADD.get(x['n'],[]):
                    if not any(ex['n'].split()[0] in v['n'] for v in x.get('v',[])): x.setdefault('v',[]).append(ex)
            xs.sort(key=lambda x:(x['g'],x.get('mk',''),yk(x.get('y','')),x['n']))
            k['nl']=nl_for(k['n']);k['sel']=sel_for(k['n'],len(xs));k['xg']='by maker country, then maker'
json.dump(D,open('D3.new.json','w'),indent=1,ensure_ascii=False)
print(removed)
