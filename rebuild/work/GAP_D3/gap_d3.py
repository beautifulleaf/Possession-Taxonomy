import json, re, os
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'out/D3.json'))
brands=json.load(open(R+'out/D3_brands.json'))
W=lambda t:'https://en.wikipedia.org/wiki/'+t
CTRY={'AKG':'Austria','Beyerdynamic':'Germany','Sennheiser':'Germany','Stax':'Japan','Grado':'United States','Sony':'Japan','Technics':'Japan','KEF':'United Kingdom','Bowers & Wilkins':'United Kingdom','Tannoy':'United Kingdom','Klipsch':'United States','JBL':'United States','McIntosh':'United States','Marantz':'United States','Naim':'United Kingdom','Rega':'United Kingdom','Pro-Ject':'Austria','Thorens':'Switzerland','Nakamichi':'Japan','Revox':'Switzerland','Bang & Olufsen':'Denmark','Apple':'United States'}
kinds={}
for dp in d['depts']:
  for sh in dp['s']:
    for k in sh['k']: kinds[k['n']]=k
norm=lambda s:re.sub(r'[^a-z0-9]','',s.lower())
log=[]
def add(kind,mk,n,y,desc,src,vers=(),g=None):
  k=kinds[kind]; x=k.setdefault('x',[])
  if any(norm(e['n'])==norm(n) or norm(e['n'])==norm(mk+n) or norm(mk+e['n'])==norm(n) for e in x):
    log.append('skip dup '+n); return
  x.append({'n':n,'a':'','d':desc,'mk':mk,'y':y,'s':src,'v':[{'n':a,'mk':mk,'y':b,'d':c} for a,b,c in vers],'g':g or CTRY[mk]})
def ver(kind,ent,vers,mk=None):
  e=next(e for e in kinds[kind]['x'] if e['n'].startswith(ent))
  have={norm(v['n']) for v in e['v']}
  for a,b,c in vers:
    if norm(a) in have or norm(e['mk']+a) in have: continue
    e['v'].append({'n':a,'mk':e['mk'],'y':b,'d':c}); have.add(norm(a))
S=lambda t:W(t)
OE,ON='Over-ear headphones','On-ear headphones'
add(OE,'Beyerdynamic','Beyerdynamic DT 48 / DT 49','1930s','Early Beyerdynamic dynamic headphones: DT 48 from the late 1930s and the DT 49 "Stielhörer" of the 1950s.',S('Beyerdynamic'),[('DT 48','late 1930s',''),('DT 49 Stielhörer','1950s','')])
add(OE,'Beyerdynamic','Beyerdynamic Amiron / Aventho','2017','Hi-fi home headphone line: Amiron Home (2017), wired Byron (2017), wireless Aventho (2018), with 300 models in 2025.',S('Beyerdynamic'),[('Amiron Home','2017',''),('Byron','2017','wired'),('Aventho','2018','wireless'),('AMIRON 300','2025',''),('AVENTHO 300','2025','')])
ver(OE,'Beyerdynamic T1',[('T1 3rd Generation','2020',''),('T5 3rd Generation','2020','closed-back sibling'),('T90 Jubilee','2014','special edition')])
ver(OE,'Beyerdynamic DT 770',[('DT 770 PRO X','2024','limited edition, permanent line May 2025'),('DT 770 M','','')])
ver(OE,'Beyerdynamic DT 880',[('DT 880 PRO','',''),('DT 990 PRO','','')])
ver(OE,'Beyerdynamic DT 770',[('DT 270 PRO','2025','')])
add(OE,'AKG','AKG K120 / K50','1949','Early AKG dynamic headphones: K120 DYN (1949) and K50 (1959).',S('AKG_(company)'),[('K120 DYN','1949',''),('K50','1959','')])
ver(OE,'AKG K240',[('K240 Monitor','',''),('K280 Parabolic','','')])
add(OE,'AKG','AKG K812 / K845 BT','','Later AKG reference and wireless headphones named on the maker page: K812 and K845 BT.',S('AKG_(company)'),[('K812','',''),('K845 BT','','')])
ver(OE,'AKG K701',[('K66','','')]) if False else None
add(ON,'AKG','AKG Y50','2017','On-ear AKG headphone cited for a 2017 award.',S('AKG_(company)'))
add(OE,'Grado','Grado Reference and Statement series','','Grado top lines: Reference (RS1, RS2x, GS1000, PS500, PS1000) and Statement (GS2000e, GS3000, PS2000e).',S('Grado_Labs'),[('RS1','',''),('RS2x','',''),('GS1000','',''),('PS500e','',''),('PS1000','',''),('GS2000e','',''),('GS3000','',''),('PS2000e','','')])
add(OE,'Grado','Grado Alessandro Music Series','','Grado collaboration line with Alessandro: MS1, MS2 and MS Pro.',S('Grado_Labs'),[('MS1','',''),('MS2','',''),('MS Pro','','')])
add(OE,'Stax','Stax SR-00x and SR-007 earspeakers','','Stax electrostatic earspeaker line: SR-001, SR-002, SR-003 and SR-007 with revisions, up to SR-009 and SR-X9000 (December 2022).',S('Stax_Ltd.'),[('SR-001 / SR-001mk2','',''),('SR-002','',''),('SR-003 / SR-003mk2','',''),('SR-007 / SR-007A','',''),('SR-009','',''),('SR-X9000','2022-12','')])
add(OE,'Stax','Stax SR-L series','','Stax electrostatic earspeakers SR-L300, SR-L300 Limited, SR-L500 and SR-L700.',S('Stax_Ltd.'),[('SR-L300','',''),('SR-L300 Limited','',''),('SR-L500','',''),('SR-L700','','')])
ver(OE,'Sennheiser HD 800',[('HD 800 S','','')])
# Loudspeakers
BS,FS,HN,ES='Bookshelf speakers','Floor-standing speakers','Horn loudspeakers','Electrostatic and planar loudspeakers'
ver(BS,'KEF LS50',[('LS50 Wireless','2017',''),('LS50 Meta','2020',''),('LS50 Wireless II','2020',''),('LSX','',''),('LSX II','2022',''),('LS60 Wireless','2022','')])
add(BS,'KEF','KEF Celeste and early KEF models','1962','KEF K1 Slimline, the first KEF loudspeaker, and the Celeste built on the 1962 B139 woofer.',S('KEF'),[('K1 Slimline','',''),('Celeste','1962','')])
add(BS,'KEF','KEF Cantata / Calinda / Corelli','1976','Three KEF loudspeaker models launched in 1976.',S('KEF'),[('Corelli','1976',''),('Calinda','1976',''),('Cantata','1976','')])
add(FS,'KEF','KEF Reference series','1973','Long-running KEF top range from Model 104 (1973) to Model 105 (1977), 107 (1986), 109 and 207/2.',S('KEF'),[('Reference Model 104','1973',''),('Reference Model 105','1977',''),('Model 105.2','1979',''),('Model 104/2','1984',''),('Model 107','1986',''),('Reference Series Model 109','',''),('Reference Series Model 105/3','',''),('Reference Series Model 207/2','early 2000s',''),('Reference 5 Meta','','')])
add(FS,'KEF','KEF Muon','2007','Technology-reference KEF loudspeaker developed in 2005 and launched in 2007.',S('KEF'))
add(BS,'Bowers & Wilkins','Bowers & Wilkins DM series','1968','B&W DM1 and DM3 (1968), DM2 (1972), DM6 (1976), DM7 (1977), and DM70 (1970, listed under electrostatic).',S('Bowers_%26_Wilkins'),[('DM1','1968',''),('DM3','1968',''),('DM2','1972',''),('DM6','1976',''),('DM7','1977','')])
add(FS,'Bowers & Wilkins','Bowers & Wilkins P1 / P2','1967','Early B&W loudspeakers P1 (1967) and P2 (1970).',S('Bowers_%26_Wilkins'),[('P1','1967',''),('P2','1970','')])
add(FS,'Bowers & Wilkins','Bowers & Wilkins Matrix and Silver Signature','1980s','B&W Matrix 1, 2 and 3 (1980s), Matrix Series (1986), CM1 Concept 90 (1987) and Silver Signature (1991).',S('Bowers_%26_Wilkins'),[('Matrix 1, 2 and 3','1980s',''),('Matrix Series','1986',''),('CM1 Concept 90','1987',''),('Silver Signature','1991','')])
ver(FS,'Bowers & Wilkins 800',[('801','1979',''),('John Bowers Active One','1984',''),('800 series Matrix','1987',''),('Nautilus 800 series','1998',''),('800D','2005',''),('803D','2005',''),('801 Abbey Road Limited Edition','2025','')])
add(FS,'Bowers & Wilkins','Bowers & Wilkins CM and XT series','2005','B&W XT series (2005) and CM series (2006).',S('Bowers_%26_Wilkins'),[('XT series','2005',''),('CM series','2006','')])
ver(HN,'Klipschorn',[('60th Anniversary Klipschorn','2006',''),('70th Anniversary Klipschorn','2016','')]) if False else None
ver(HN,'Klipschorn',[('60th Anniversary Klipschorn','2006',''),('70th Anniversary Klipschorn','2016',''),('kO-R1 Limited Edition','2024','')])
ver(HN,'Klipsch Heritage',[('Model K','',''),('La Scala','',''),('Cornwall','',''),('Heresy','','')])
add(FS,'Klipsch','Klipsch Palladium','2007','Klipsch flagship floor-standing range launched in 2007.',S('Klipsch_Audio_Technologies'))
add(FS,'Klipsch','Klipsch Icon, Synergy and Reference lines','','Klipsch Icon (X, W, V), Synergy and Reference ranges, with Reference Premiere from 2015.',S('Klipsch_Audio_Technologies'),[('Icon Series X','',''),('Icon Series W','',''),('Icon Series V','',''),('Synergy','',''),('Reference','',''),('Reference Premiere','2015','')])
add(BS,'Tannoy','Tannoy Little Gold Monitor','c. 1990','Compact Tannoy dual-concentric monitor, earliest of the Gold line.',S('Tannoy'))
add(BS,'Tannoy','Tannoy Classic, Red and Little Red Monitors','','Tannoy monitor lines Classic Monitor, Super Red Monitor and Little Red, with matching kits.',S('Tannoy'),[('Classic Monitor','',''),('K3838 kit','',''),('Super Red Monitor','',''),('K3808 kit','',''),('Little Red','','')])
add(FS,'Tannoy','Tannoy Gold, Definition and Eclipse series','','Tannoy series named on the maker page: Gold, Definition, Eclipse, Mercury, Cheviot, Reveal, Surrey, Plus, Sixes, Profile, Precision, Revolution, Dimension and Eyris.',S('Tannoy'),[('Gold Series','',''),('Definition Series','',''),('Eclipse Series','',''),('Mercury Series','',''),('Revolution Series','',''),('Dimension Series','',''),('Eyris Series','','')])
add(FS,'Tannoy','Tannoy Wildcats','1984','Tannoy series launched in 1984.',S('Tannoy'))
add(HN,'JBL','JBL Paragon and Hartsfield','1958','JBL horn-loaded home loudspeakers: Paragon (1958) and Hartsfield.',S('JBL'),[('Paragon','1958',''),('Hartsfield','','')])
ver(BS,'JBL 4310',[('4320','',''),('4400','1981',''),('L26','late 1970s',''),('L100T','mid-1980s','')])
ver(BS,'JBL 4310',[('4300 Series','1973','')])
add(FS,'JBL','JBL K2 and Everest','','JBL flagship floor-standing ranges named on the maker page: K2 and Everest.',S('JBL'),[('K2','',''),('Everest','','')])
add(FS,'McIntosh','McIntosh ML1 / XRT20','1970','McIntosh loudspeakers: ML1, ML2 and ML4 (1970) and the XRT20 system (1980).',S('McIntosh_Laboratory'),[('ML1 / ML2 / ML4','1970',''),('XRT20','1980','')])
add(BS,'Technics','Technics SB-F1 monitors','late 1970s','Technics monitor speakers SB-F1, SB-F01, SB-F2 and SB-F3.',S('Technics_(brand)'),[('SB-F1','late 1970s',''),('SB-F01','late 1970s',''),('SB-F2','late 1970s',''),('SB-F3','late 1970s','')])
add(FS,'Technics','Technics SB-7000 / SB-10000 / SST-1','mid-1970s','Technics large loudspeakers: SB-7000 (mid-1970s), SB-10000 (late 1970s) and SST-1 (1991).',S('Technics_(brand)'),[('SB-7000','mid-1970s',''),('SB-10000','late 1970s',''),('SST-1','1991','')])
add(FS,'Revox','Revox Series 46 / Symbol B / Scala','1970','Revox loudspeakers: Series 46 (1970), AX (1976), BX (1977), BR (1980), Symbol B (1983), Agora B active (1986), Scala 4.7 (1994) and Scala 3.6 (1996).',S('Revox'),[('Series 46','1970',''),('AX','1976',''),('BX','1977',''),('BR','1980',''),('Symbol B','1983',''),('Agora B','1986',''),('Scala 4.7','1994',''),('Scala 3.6','1996','')])
add(FS,'Naim','Naim SBL','','Naim Separate Box Loudspeaker.',S('Naim_Audio'))
add(FS,'Bang & Olufsen','Bang & Olufsen BeoLab 5','','Large B&O floor-standing active loudspeaker named on the B&O page.',S('Bang_%26_Olufsen'))
# Turntables
TT='Turntable'
add(TT,'Technics','Technics SL-1100','1971','Direct-drive Technics turntable that preceded the SL-1200.',S('Technics_(brand)'),[('SL-1100','1971','')])
ver(TT,'Technics SL-1200',[('SL-1200G','2016','')])
ver(TT,'Technics SP-10',[('SP-10R','2018','')])
add(TT,'Technics','Technics SL-10 linear tracking','1980','Linear-tracking Technics turntable line SL-10 (1980–1984), with SL-15, SL-7, SL-6, SL-5 and SL-V5.',S('Technics_(brand)'),[('SL-10','1980',''),('SL-15','',''),('SL-7','',''),('SL-6','',''),('SL-5','',''),('SL-V5','','')])
add(TT,'Technics','Technics SL-20 / SL-23 belt drive','1976','Technics belt-drive turntables SL-20 and SL-23 of 1976.',S('Technics_(brand)'),[('SL-20','1976',''),('SL-23','1976','')])
add(TT,'Technics','Technics SL-1300 to SL-1800','late 1970s','Late-1970s Technics direct-drive range SL-1300 to SL-1800 with Mk2 versions.',S('Technics_(brand)'),[('SL-1300','',''),('SL-1400','',''),('SL-1500','',''),('SL-1600','',''),('SL-1700','',''),('SL-1800','','')])
add(TT,'Pro-Ject','Pro-Ject 1 and Pro-Ject 6','1991','Early Pro-Ject turntables: Pro-Ject 1 (1991, based on the Tesla NC-500) and Pro-Ject 6 (1994).',S('Pro-Ject_Audio_Systems'),[('Pro-Ject 1','1991',''),('Pro-Ject 6','1994','')])
add(TT,'Pro-Ject','Pro-Ject Artist Collection','2015','Limited-edition Pro-Ject turntables since 2015, including Yellow Submarine.',S('Pro-Ject_Audio_Systems'),[('Yellow Submarine','','')])
ver(TT,'Pro-Ject Debut',[('Debut Carbon EVO','2020',''),('Debut PRO','2021',''),('Debut III','','')])
add(TT,'Thorens','Thorens TD 125 / TD 126','1972','Thorens turntables TD 125 Mk II (1972–1975) and TD 126 Mk III (1979–1986).',S('Thorens'),[('TD 125 Mk II','1972',''),('TD 126 Mk III','1979','')])
add(TT,'Thorens','Thorens TD 320','1984','Thorens turntable of 1984.',S('Thorens'))
add(TT,'Thorens','Thorens TD 850 / TD 309','2004','Later Thorens turntables: TD 850 mass-drive (2004), TD 309 sub-chassis (2012), TD 190/170 (1999).',S('Thorens'),[('TD 190/170','1999',''),('TD 850','2004',''),('TD 309','2012','')])
ver(TT,'Thorens TD 150',[('TD 160','1972','')])
add(TT,'Bang & Olufsen','Bang & Olufsen Beogram 1000','1950s','Early B&O record player; the company history page dates its first turntable to 1929.','https://www.bang-olufsen.com/en/au/story/turntables')
ver(TT,'Bang & Olufsen Beogram 4000',[('Beogram 4000c Recreated Classic Edition','2020','')])
ver(TT,'Rega Planar',[('Planar 3','',''),('RP3','','')])
add(TT,'Revox','Revox B790','1977','Linear-tracking Revox record player, 1977–1982.',S('Revox'))
add(TT,'Revox','Revox Studiomaster T700','2020','Belt-driven Revox turntable.',S('Revox'))
add(TT,'Nakamichi','Nakamichi Dragon-CT','','Nakamichi turntable of the CD era after 1983.',S('Nakamichi'))
TA='Tonearm'
add(TA,'Thorens','Thorens TP13a','1965','Thorens tonearm made 1965–1972.',S('Thorens'))
add(TA,'Naim','Naim ARO','','Naim uni-pivot tonearm.',S('Naim_Audio'))
add(TA,'Pro-Ject','Pro-Ject EVO tonearms','2023','Pro-Ject tonearm family of 24 models from 2023.',S('Pro-Ject_Audio_Systems'))
PC='Phono cartridge'
add(PC,'Rega','Rega Elys','','Rega moving-magnet cartridge; the page names the Elys 2.',S('Rega_Research'),[('Elys 2','','')])
ver(PC,'Grado Prestige',[('Reference Series','',''),('Series 4','2026','')])
# Amplifiers
PA,IA,PRE,RC='Power amplifier','Integrated amplifier','Preamplifier','Stereo receiver'
add(PA,'McIntosh','McIntosh 50W-1 / A116 / MC30','1949','Early McIntosh valve power amplifiers: 50W-1 (1949), A116 (1953) and MC30 (1954).',S('McIntosh_Laboratory'),[('50W-1','1949',''),('A116','1953',''),('MC30','1954','')])
ver(PA,'McIntosh MC275',[('MC240','1960',''),('MC275 Mark V','2004','')])
add(PA,'McIntosh','McIntosh MC250 to MC2505','1965','McIntosh solid-state power amplifiers MC250 (1965), MC2100, MC2105 and MC2505 (1967).',S('McIntosh_Laboratory'),[('MC250','1965',''),('MC2100','1967',''),('MC2105','1967',''),('MC2505','1967','')])
add(PA,'McIntosh','McIntosh MC3500','1968','McIntosh tube power amplifier of 1968, reissued as MC3500 MkII for the 50th anniversary of Woodstock (2019).',S('McIntosh_Laboratory'),[('MC3500 MkII','2019','')])
ver(PA,'McIntosh MC2300',[('MC2500','1980',''),('MC2600','c. 1990','')])
add(PA,'McIntosh','McIntosh MC501 / MC2KW / MC1.25KW','2003','McIntosh modern flagship power amplifiers: MC501 (2003), MC2KW (2006), MC1.25KW (2017) and MC451 (2023).',S('McIntosh_Laboratory'),[('MC501','2003',''),('MC2KW','2006',''),('MC1.25KW','2017',''),('MC451','2023','')])
ver(IA,'McIntosh MA series',[('MA252','',''),('MA8900','',''),('MA8950','','')])
ver(PRE,'McIntosh C-series',[('AE-1','1950',''),('C108','1953',''),('C4','1954',''),('C24','1964',''),('C47','',''),('C52','','')])
add(PRE,'McIntosh','McIntosh C8 Audio Compensator','1955','McIntosh preamplifier of 1955.',S('McIntosh_Laboratory')) if False else None
add('FM/DAB tuner','McIntosh','McIntosh MR and MX tuners','1957','McIntosh tuners MR55 (1957), MX110 (1962), MR67 and MR71 (1963), MX112 (1968) and MR78 (1972).',S('McIntosh_Laboratory'),[('MR55','1957',''),('MX110','1962',''),('MR67','1963',''),('MR71','1963',''),('MX112','1968',''),('MR78','1972','')])
add(RC,'Marantz','Marantz 2600','','Marantz receiver the page calls the brand’s most powerful.',S('Marantz'))
add('FM/DAB tuner','Marantz','Marantz 150 tuner','1975','Marantz tuner made 1975–1978.',S('Marantz'))
add(IA,'Marantz','Marantz PM-KI Ruby','','Marantz two-channel integrated amplifier.',S('Marantz'))
add(PA,'Naim','Naim NAP 160 and NAP 500','','Naim power amplifiers: NAP160 (the first product), NAP 250 (1975) and NAP500 (2000).',S('Naim_Audio'),[('NAP160','',''),('NAP500','2000','')])
add(PRE,'Naim','Naim NAC 12 / 32 / 42 / 52','','Naim preamplifiers NAC12, NAC32, NAC42 and NAC52, with Hi-Cap power supply and NAXO crossover.',S('Naim_Audio'),[('NAC12','',''),('NAC32','',''),('NAC42','',''),('NAC52','',''),('Hi-Cap','','power supply')])
add(PA,'Technics','Technics SE-A series','late 1970s','Technics power amplifiers SE-A1, SE-A3, SE-A5, SE-A7 and SE-9060.',S('Technics_(brand)'),[('SE-A1','late 1970s',''),('SE-A3','late 1970s',''),('SE-A5','late 1970s',''),('SE-A7','early 1980s','')])
add(IA,'Technics','Technics SU-V series','early 1980s','Technics integrated amplifiers SU-V3 to SU-V9 and the Class AA SU-V40 to SU-V60 (1986).',S('Technics_(brand)'),[('SU-V3 to SU-V9','early 1980s',''),('SU-V40 / V50 / V60','1986','')])
add(RC,'Technics','Technics SA receivers','late 1970s','Technics receivers SA-100 to SA-1000, quadraphonic SA-6800X (1973) and SA-8500X.',S('Technics_(brand)'),[('SA-6800X','1973',''),('SA-8500X','mid-1970s',''),('SA-100 to SA-1000','late 1970s','')])
add(PA,'Nakamichi','Nakamichi PA-5 / PA-7','','Nakamichi power amplifiers PA-5 and PA-7.',S('Nakamichi'),[('PA-5','',''),('PA-7','','')])
add(RC,'Nakamichi','Nakamichi SR and TA receivers','','Nakamichi receiver series SR and TA.',S('Nakamichi'))
add(IA,'Revox','Revox A78','','Revox integrated amplifier, with A750 amplifier (1977) and B250.',S('Revox'),[('A750','1977',''),('B250','','')])
# Sources
add('Reel-to-reel tape deck','Nakamichi','Nakamichi Fidela','1957','Nakamichi three-head open-reel stereo tape deck.',S('Nakamichi'))
add('Reel-to-reel tape deck','Technics','Technics RS-1500 / RS-1700','late 1970s','Technics open-reel tape decks.',S('Technics_(brand)'))
add('Reel-to-reel tape deck','Revox','Revox PR99 / C270','','Revox professional recorders: PR99, PR99 Mk2 (about 1985) and C270 multitrack series.',S('Revox'),[('PR99','',''),('PR99 Mk2','c. 1985',''),('C270','',''),('C274','',''),('C278','','')])
ver('Reel-to-reel tape deck','Revox 36',[('T26','1952',''),('A36','1954',''),('B36','1956',''),('D36','1960',''),('G36','1967','')])
ver('Reel-to-reel tape deck','Revox A77',[('A700','1970s',''),('B77 MK3','2024','')])
CD_='Cassette deck'
add(CD_,'Nakamichi','Nakamichi 500 / 550 / 600','1974','Nakamichi two-head decks 500 and 600 and the portable 550 (1974).',S('Nakamichi'),[('500','',''),('550','1974','portable'),('600','','wedge-shaped')])
add(CD_,'Nakamichi','Nakamichi 580M and ZXL','c. 1978','Nakamichi 580M (metal tape, c. 1978) and 1000ZXL, 700ZXL and 700ZXE (c. 1980).',S('Nakamichi'),[('580M','c. 1978',''),('1000ZXL','c. 1980',''),('700ZXL','c. 1980',''),('700ZXE','c. 1980','')])
add(CD_,'Nakamichi','Nakamichi CR and LX series','','Nakamichi cassette decks CR-1 to CR-7 and LX-3, LX-5, plus Cassette Deck 1.',S('Nakamichi'),[('CR-1','',''),('CR-2','',''),('CR-3','',''),('CR-4','',''),('CR-5','',''),('CR-7','',''),('LX-3','',''),('LX-5','',''),('Cassette Deck 1','','')])
ver(CD_,'Nakamichi 1000',[('1000-II','late 1970s',''),('700-II','late 1970s',''),('600-II','late 1970s','')])
add(CD_,'Technics','Technics RS-M series','1980','Technics cassette decks RS-M205 (1980), RS-M212 (1981), RS-M216 (1982), RS-M95, and earlier RS-277US (1972) and RS-279US (1973).',S('Technics_(brand)'),[('RS-277US','1972',''),('RS-279US','1973',''),('RS-M205','1980',''),('RS-M212','1981',''),('RS-M216','1982')[:2]+('',)])
add(CD_,'Revox','Revox H1 / B710','','Revox cassette recorders H1 (Studer-designed), B710 and the rebadged H11 and C115.',S('Revox'),[('H1','',''),('B710','',''),('H11','','rebadged Philips'),('C115','','rebadged Philips')])
add('CD player','Technics','Technics SL-P2','c. 1985','Technics CD player, with the SL-MC 60+1 CD changers (1998–2002).',S('Technics_(brand)'),[('SL-P2','c. 1985',''),('SL-MC59','1998','')])
add('CD player','Naim','Naim CD 5','2009','Naim single-box CD players CD 5 XS (2009) and CD5si (2012).',S('Naim_Audio'),[('CD 5 XS','2009',''),('CD5si','2012','')])
ver('CD player','Naim CDS',[('CDS2','1998',''),('CDS3','2002','')])
ver('CD player','Revox B225',[('B226','',''),('B226 Signature','','')])
add('Network streamer','Revox','Revox Joy and M51','2002','Revox network and multiroom products: M51 (2002), M117 (2011) and Joy S118 to S120 (2012).',S('Revox'),[('M51','2002',''),('M117','2011',''),('Joy S118','2012',''),('Joy S119','2012',''),('Joy S120','2012','')])
add('Network streamer','Naim','Naim Mu-so','2014','Naim all-in-one wireless speaker system; second generation 2019.',S('Naim_Audio'),[('Mu-so','2014',''),('Mu-so 2nd Generation','2019',''),('Mu-so Qb 2nd Generation','2019','')])
add('Compact hi-fi system','Bowers & Wilkins','Bowers & Wilkins Zeppelin','2007','B&W iPod speaker system launched in 2007.',S('Bowers_%26_Wilkins'))
add('Compact hi-fi system','Technics','Technics SC mini systems','1990s','Technics mini hi-fi series SC-EH, SC-CA, SC-CH, SC-DV and SC-HD.',S('Technics_(brand)'))
add('Portable radio','Bang & Olufsen','Bang & Olufsen Beolit 39','1938','Early B&O portable radio.',S('Bang_%26_Olufsen'))
# Walkman and portable
def parse(txt):
  out=[]
  for l in txt.strip().splitlines():
    n,_,y=l.partition(' – ')
    out.append((n.strip(),'' if 'not listed' in y else y.strip(),''))
  return out
WM=parse("""TPS-L2 – 1979
WM-1 – 1981
WM-2 – 1981
WM-3 – 1981
WM-5 – 1982
WM-7 – 1982
WM-DD – 1982
WM-F2 – 1982
WM-R2 – 1982
WM-20 – 1983
WM-F20 – 1983
WM-4 – 1983
WM-9 – 1983
WM-10 – 1983
WM-6 – 1984
WM-F8 – 1984
WM-16 – 1984
WM-22 – 1984
WM-F15 – 1984
WM-24 – 1985
WM-25 – 1985
WM-30 – 1985
WM-75 – 1985
WM-101 – 1985
WM-34 – 1986
WM-35 – 1986
WM-F35 – 1986
WM-55 – 1986
WM-60 – 1986
WM-F16 – 1986
WM-F107 – 1986
WM-33 – 1987
WM-36 – 1987
WM-38 – 1987
WM-F38 – 1987
WM-41 – 1987
WM-43 – 1987
WM-51 – 1987
WM-F66 – 1987
WM-102 – 1987
WM-B10 – 1988
WM-B12 – 1988
WM-F404 – 1988
WM-B52 – 1988
WM-503 – 1989
WM-701 – 1989
WM-AF54 – 1989
WM-3000 – 1990
WM-3060 – 1990
WM-106 – 1990
WM-B603 – 1991
WM-FX513 – 1993
WM-EX102 – 1994
WM-FX221 – 1995
WM-GX320 – 1998
WM-EX670 – 1999
WM-GX400 – 2001
WM-FX290W – 2004
WM-EX194 – 2004""")
ver('Portable cassette player','Sony Walkman (cassette)',WM)
ver('Portable cassette player','Sony Walkman Professional',[('WM-D3','1985','')])
ver('Portable cassette player','Sony Walkman (cassette)',[('SRF-40 FM Walkman','1980','radio'),('SRF-A1 FM/AM Stereo Walkman','1983','radio')])
ver('Portable cassette player','Sony Walkman (cassette)',[('Sports Walkman WM-SXF33','1990s','')])
add('Portable CD player','Sony','Sony Discman D-NE series','2003','Sony Discman D-NE models, rebranded CD Walkman in 1997.',S('List_of_Sony_Walkman_products'),parse("""D-NE1 – 2003
D-NE9 – 2003
D-NE510 – 2003
D-NE10 – 2004
D-NE900 – 2004
D-NE800 – 2004
D-NE20 – 2004
D-NE920 – 2004
D-NE820 – 2004
D-NE720 – 2005
D-NE830 – 2005"""))
MZ=parse("""MZ-1 – 1992
MZ-2P – 1992
MZ-R2 – 1993
MZ-R3 – not listed
MZ-B3 – 1995
MZ-E50 – 1996
MZ-E500 – 2000
MZ-E700 – 2000
MZ-E900 – 2000
MZ-R900 – 2000
MZ-B50 – 2000
MZ-N1 – 2001
MZ-E909 – 2001
MZ-R909 – 2001
MZ-E10 – 2002
MZ-N10 – 2002
MZ-N707 – 2002
MZ-N910 – 2003
MZ-NH1 – 2004
MZ-NH3D – 2004
MZ-EH1 – 2004
MZ-DH10P – 2005
MZ-RH910 – 2005
MZ-RH10 – 2005
MZ-RH1 – 2006
MZ-B100 – not listed
MZ-B10 – not listed
MZ-G750 / MZ-G755 – not listed""")
ver('Portable MiniDisc player','Sony MiniDisc Walkman',MZ)
NW=parse("""NW-MS7 – 1999
NW-E3 – 2000
NW-MS9 – 2000
NW-MS11 – 2001
NW-S4 – 2001
NW-MS10 – 2002
NW-MS70D – 2002
NW-MS90D – 2002
NW-S23 – 2004
NW-S21 – not listed
NW-HD1 – 2004
NW-HD3 – 2004
NW-HD5 – 2005
NW-A1000 – 2005
NW-A3000 – 2005
NWZ-E300 / E200 – 2005
NW-S700 – 2006
NWZ-S610 – 2007
NWZ-A800 / A810 – 2007
NWZ-E010 – 2007
NWD-B100 / B103 / B105 – 2007
NWZ-B130 – 2008
NWZ-S630 – 2008
NWZ-W202 – 2009
NWZ-A840 – 2009
NWZ-E440 – 2009
NWZ-B140 – 2009
X Series – 2009
NWZ-B150 – 2010
NWZ-S760 – 2011
NWZ-B160 – 2011
Z1000 – 2011
W260 – 2011
NW-E060 – 2012
NWZ-B170 – 2012
NW-F800 – 2012
NWZ-B180 / B183 – 2014
NW-W270 / W273 / W274 – 2013
NW-WH505 / WH303 – 2013
NW-M505 – 2013
NW-F887 – 2013
WS610 / WS615 – 2014
NWZ-A10 – 2014
WS410 / WS413 / WS414 – 2016
WS620 / WS623 / WS625 – 2017""")
ver('MP3 player','Sony Walkman (digital',NW)
# iPod
IP=W('IPod')
ver('MP3 player','Apple iPod',[('iPod (classic) 1st generation','2001-11-10',''),('2nd generation','2002-08',''),('3rd generation','2003-05-02',''),('4th generation','2004-07-19',''),('5th generation','2005-10',''),('6th generation','2007-09-05','')])
add('MP3 player','Apple','Apple iPod mini','2004','Smaller iPod: 1st generation 20 February 2004, 2nd generation 23 February 2005.',IP,[('1st generation','2004-02-20',''),('2nd generation','2005-02-23','')])
add('MP3 player','Apple','Apple iPod nano','2005','Flash iPod in seven generations from 7 September 2005 to 12 September 2012.',IP,[('1st generation','2005-09-07',''),('2nd generation','2006-09-12',''),('3rd generation','2007-09-05',''),('4th generation','2008-09-09',''),('5th generation','2009-09-09',''),('6th generation','2010-09-01',''),('7th generation','2012-09-12','')])
add('MP3 player','Apple','Apple iPod shuffle','2005','Screenless iPod in four generations from 11 January 2005 to 1 September 2010.',IP,[('1st generation','2005-01-11',''),('2nd generation','2006-09-12',''),('3rd generation','2009-03-11',''),('4th generation','2010-09-01','')])
add('MP3 player','Apple','Apple iPod touch','2007','Touch-screen iPod in seven generations from 5 September 2007 to 28 May 2019.',IP,[('1st generation','2007-09-05',''),('2nd generation','2008-09-09',''),('3rd generation','2009-09-09',''),('4th generation','2010-09-01',''),('5th generation','2012-09-12',''),('6th generation','2015-07-15',''),('7th generation','2019-05-28','')])
# sort entries by g then mk then y then n
def keyf(e): return (e.get('g',''),e.get('mk',''),e.get('y','') or 'zzzz',e['n'])
for k in kinds.values():
  if k.get('x'):
    mk=k['xg'].startswith('by maker')
    if mk: k['x'].sort(key=keyf)
# brands
have={norm(b['n']) for b in brands['b']}
for b in ['Bang & Olufsen','Beyerdynamic']: pass
# coverage lines
for dp in d['depts']:
  for sh in dp['s']:
    for k in sh['k']:
      x=k.get('x')
      if not x: continue
      n=len(x)
      sel=k.get('sel','')
      sel=re.sub(r'\s*Covers [^.]*(?:\.[0-9][^.]*)*\.?\s*$','',sel).strip()
      if not sel.endswith('.'): sel+='.'
      wp=sorted({e['s'].split('/wiki/')[1].replace('_',' ') for e in x if '/wiki/' in e.get('s','')})
      wp=[w.split('(')[0].strip() for w in wp][:14]
      if k.get('xg','').startswith('by market'):
        sel+=f' No complete list exists; follows the market rankings and maker pages cited on the entries. Now {n} entries.'
      else:
        sel+=f' No complete list exists for this kind; follows the maker pages and overviews cited on the entries (Wikipedia: {", ".join(wp)}). Every model line those maker pages list for this kind is an entry or a version; the {n} entries are lineages, not catalogue models.'
      k['sel']=sel
json.dump(d,open(R+'work/GAP_D3/D3.new','w'),ensure_ascii=False,indent=1)
os.replace(R+'work/GAP_D3/D3.new',R+'out/D3.json')
print('\n'.join(log))
