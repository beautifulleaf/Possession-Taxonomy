from adds import add,R,A,_mv
from data import *
TAY=W+'Taylor_Guitars';PRS=W+'PRS_Guitars';GUI=W+'Guild_Guitar_Company';OVA=W+'Ovation_Guitar_Company'
SCH=W+'Schecter_Guitar_Research';MM=W+'Music_Man_(company)';WAS=W+'Washburn_Guitars';TAK=W+'Takamine_Guitars'
HOF=W+'H%C3%B6fner';DAN=W+'Danelectro';SQU=W+'Squier';WAR=W+'Warwick_(guitar_manufacturer)';SPE=W+'Spector_(company)'
STB=W+'Steinberger_bass';ORA=W+'Orange_Music_Electronic_Company';PEA=W+'Peavey_Electronics';AMP=W+'Ampeg'
YEM=W+'Yamaha_electric_guitar_models';VMS='https://vintagemartin.com/sizes.html'
def L(kind,mk,src,rows,d):
    out=[]
    for r in rows:
        n,y=(r if isinstance(r,tuple) else (r,''))
        out.append(R(n,mk,y,d.format(n=n,y=y) if '{' in d else d,src))
    add(kind,out)
# Taylor
L('Steel-string acoustic guitar','Taylor',TAY,[('Taylor 100 series',''),('Taylor 200 series',''),('Taylor 300 series',''),('Taylor 400 series',''),('Taylor 500 series',''),('Taylor 914',''),('Taylor Pallet Guitar','1995'),('Taylor Gold Label','2025'),('Taylor Steven Curtis Chapman Signature','2010'),('Taylor Richie Sambora Signature','')],'Taylor acoustic series or model named on the Taylor page.')
L('Solid-body electric guitar','Taylor',TAY,[('Taylor ES-T','')],'Taylor electric model named on the Taylor page.')
# PRS
L('Solid-body electric guitar','PRS',PRS,[('Custom 22','1993'),('PRS Guitar','1986'),('Standard','1987'),('Signature','1987–1991'),('CE','1988'),('EG','1990'),('EG II','1992'),('Dragon 1','1992'),('Dragon 2','1993'),('Dragon 3','1994'),('Dragon 2000','1999'),('McCarty','1994'),('Santana','1995'),('Private Stock','1996'),('SE','2000'),('S2','2014'),('Starla','2014'),('Mira','2014'),('NF 53','2023'),('Golden Eagle',''),('MT',''),('DG Custom 30',''),('HDRX',''),('Studio',''),('NF3',''),('Fiore',''),('Chleo','')],'PRS model or series named on the PRS Guitars page.')
L('Amp head','PRS',PRS,[('Archon','2007')],'PRS amplifier named on the PRS Guitars page.')
# Guild
L('Steel-string acoustic guitar','Guild',GUI,[('D-40','early 1960s'),('D-50','early 1960s'),('F-50','2009'),('D40-C','1972'),('Guild Standard Series','2010'),('Guild Traditional Series','2009'),('Guild Westerly Collection','2015'),('M-20','2016'),('D-20','2016'),('GAD series','early 2000s')],'Guild acoustic model or series named on the Guild page.')
L('Hollow-body electric guitar','Guild',GUI,[('Starfire','1960s')],'Guild Starfire I to VI, named on the Guild page.')
L('Solid-body electric guitar','Guild',GUI,[('Flyer','1980s'),('Aviator','1980s'),('Liberator','1980s'),('Detonator','1980s'),('T-200','1980s'),('T-250','1980s'),('Newark Street','2015'),('GSR Starfire VI','2003')],'Guild model named on the Guild page.')
L('Electric bass guitar','Guild',GUI,[('Pilot Bass','1980s')],'Guild bass named on the Guild page.')
# Ovation
L('Steel-string acoustic guitar','Ovation',OVA,[('Kaman Ovation 1612-4','mid-1970s'),('Celebrity',''),('Applause',''),('Deacon','')],'Ovation model named on the Ovation page.')
L('Solid-body electric guitar','Ovation',OVA,[('Breadwinner','1972'),('Deacon','')],'Ovation electric named on the Ovation page.')
# Schecter
L('Solid-body electric guitar','Schecter',SCH,[('C-1','2000'),('S-1','2001'),('006 Elite','2008'),('007 Elite','2000–2007'),('Banshee','2007'),('Gryphon','2008'),('Hellcat','2008'),('Hellraiser','2013'),('Tempest','2003'),('Vengeance','2007'),('Avenger','2007'),('PT','2004'),('Ultra','2006'),('Diamond Series','1998'),('S Series','1995'),('USA Production Series','2013'),('Aviation Series','2006')],'Schecter model or series named on the Schecter page.')
L('Electric bass guitar','Schecter',SCH,[('Ultrabass','2005'),('Jazz-6','2002'),('Jazz-7','2001'),('Jazz Elite','2005')],'Schecter bass named on the Schecter page.')
# Music Man
L('Solid-body electric guitar','Music Man',MM,[('StingRay 1 (guitar)','1976'),('Sabre (guitar)','1978'),('Cutlass',''),('St. Vincent HHH','2016'),('St. Vincent HH','2018'),('St. Vincent Goldie','2021'),('Mariposa','2019'),('Kaizen','2022')],'Music Man guitar named on the Music Man page.')
L('Electric bass guitar','Music Man',MM,[('Music Man Sabre bass','1978'),('Music Man StingRay Special','2018'),('Music Man StingRay II','2025'),('Music Man Sterling','1993'),('Music Man Bongo','2003'),('Music Man Big Al','2009'),('Music Man SUB','2003–2006')],'Music Man bass named on the Music Man page.')
L('Combo amp','Music Man',MM,[('Music Man Sixty Five','1974')],'Music Man amplifier named on the Music Man page.')
# Washburn
Wg=[('Washburn Jazz','1989–date'),('Washburn Bantam','1984–1986'),('Washburn Centurian','1997–2002'),('Washburn Culprit','1998–2000'),('Washburn Dime','1995–2004'),('Washburn Force','1983–1988'),('Washburn Hard Rock','2000–2002'),('Washburn Nextar','2002–2003'),('Washburn Poptop','2000–2002'),('Washburn Rogue Star','2000–2002'),('Washburn Idol','1999–2010'),('Washburn HM','2008–2010'),('Washburn Wavepoint','2008–2010'),('Washburn Vee','2008–2010'),('Washburn Jennifer Batten','2000–2004'),('Washburn Chicago','1989–1991'),('Washburn Laredo','1992–1994'),('Washburn Magnum','1997–2000'),('Washburn Maverick','1995–2002'),('Washburn Maya','2005–2010'),('Washburn Mercury','1992–1996'),('Washburn Nick Catanese','2005–2009'),('Washburn Nuno Bettencourt','1990–2025'),('Washburn Paul Stanley','1998–2016'),('Washburn RX','2011–date'),('Washburn Scott Ian','2005–2010'),('Washburn Stage','1980–1986'),('Washburn Extended Cutaway','1988–1991'),('Washburn Steve Stevens','1993–1994'),('Washburn Tour','1984–1994'),('Washburn Wing','1978–1985'),('Washburn X','2002–2010'),('Washburn XM','2011–date'),('Washburn Sonamaster','2016–date'),('Washburn Parallaxe','2013–date'),('Washburn Tabu','2009'),('Washburn Lyon','1994–1995')]
L('Solid-body electric guitar','Washburn',WAS,Wg,'Washburn electric series named on the Washburn page.')
L('Hollow-body electric guitar','Washburn',WAS,[('Washburn Hollow Body','1981–date')],'Washburn hollow-body series named on the Washburn page.')
L('Electric bass guitar','Washburn',WAS,[('Washburn Wing Bass','1980–1981'),('Washburn Stage Bass','1981–1984'),('Washburn Force Bass','1983–1986'),('Washburn ABT','1987–1989'),('Washburn Axxess','1990–1991'),('Washburn Bantam Bass','1994–2006'),('Washburn Mercury Bass','1992–1993'),('Washburn RB','1999–2003'),('Washburn Shadow','1997–1999'),('Washburn Status 1000','1988–1993'),('Washburn Stu Hamm','2012–2016'),('Washburn Taurus','2002–date'),('Washburn Bootsy Collins Space Bass','2002–2006'),('Washburn CB','2007–2010'),('Washburn DB','2000'),('Washburn M','2002–2003'),('Washburn Festival','1988–date')],'Washburn bass series named on the Washburn page.')
L('Steel-string acoustic guitar','Washburn',WAS,[('Washburn D dreadnought','1978–2010'),('Washburn WD','2011–date'),('Washburn F folk','1978–2010'),('Washburn WF','2012–date'),('Washburn WG','2011–date'),('Washburn J jumbo','1991–2010'),('Washburn SJ','2004–2005'),('Washburn WB','2007–2010'),('Washburn WJ','2011–date'),('Washburn PS','2007'),('Washburn PR Prairie State','2002–2003'),('Washburn DC','1987–1994'),('Washburn RW Roger Waters','2004'),('Washburn 125th Anniversary','2008–2009')],'Washburn acoustic series named on the Washburn page.')
# Takamine
L('Steel-string acoustic guitar','Takamine',TAK,[('Takamine EF400S','1977'),('Takamine F340S','1978'),('Takamine PT-007S','1979'),('Takamine Hirade',''),('Takamine G Series',''),('Takamine Nashville',''),('Takamine Tradition',''),('Takamine Limited Edition','1987')],'Takamine model or series named on the Takamine page.')
# Hofner
L('Archtop acoustic guitar','Höfner',HOF,[('Höfner 465s','1953'),('Höfner Ambassador',''),('Höfner Chancellor',''),('Höfner Congress',''),('Höfner President',''),('Höfner Senator',''),('Höfner Committee',''),('Höfner Jazzica Custom',''),('Höfner New President',''),('Höfner Vice-President','')],'Höfner archtop named on the Höfner page.')
L('Semi-hollow electric guitar','Höfner',HOF,[('Höfner Club 40','1959'),('Höfner Club 50',''),('Höfner Club 60',''),('Höfner Verithin',''),('Höfner Verythin Classic',''),('Höfner Verythin Standard','')],'Höfner thinline named on the Höfner page.')
L('Solid-body electric guitar','Höfner',HOF,[('Höfner Colorama',''),('Höfner Galaxie',''),('Höfner V Series',''),('Höfner Shorty','1982'),('Höfner Violin guitar',''),('Höfner H5',''),('Höfner Icon / Ignition','')],'Höfner model named on the Höfner page.')
L('Steel-string acoustic guitar','Höfner',HOF,[('Höfner Razerwood S7L',''),('Höfner HAS series','')],'Höfner acoustic named on the Höfner page.')
L('Electric bass guitar','Höfner',HOF,[('Höfner 500/2 Club Bass',''),('Höfner 500/5',''),('Höfner Ed Sullivan Series',''),('Höfner Club Bass reissue','')],'Höfner bass named on the Höfner page.')
# Danelectro
L('Solid-body electric guitar','Danelectro',DAN,[('Danelectro C','1954–1955'),('Danelectro U1','1956–1958'),('Danelectro U3','1956–1958'),('Danelectro Shorthorn','1959'),('Danelectro \'56 Pro','2006'),('Danelectro \'56 Single Cutaway','2010')],'Danelectro model named on the Danelectro page.')
L('Electric bass guitar','Danelectro',DAN,[('Danelectro UB-2','1956')],'Danelectro bass named on the Danelectro page.')
L('Distortion pedal','Danelectro',DAN,[('Danelectro FAB Distortion','2005'),('Danelectro FAB Metal','2005')],'Danelectro pedal named on the Danelectro page.')
L('Overdrive pedal','Danelectro',DAN,[('Danelectro FAB Overdrive','2005')],'Danelectro pedal named on the Danelectro page.')
# Squier
L('Electric bass guitar','Squier',SQU,[('Squier Jazz Bass',''),('Squier Bass','1989')],'Squier bass named on the Squier page; made in Korea from 1989.')
# Warwick
L('Electric bass guitar','Warwick',WAR,[('Warwick Corvette',''),('Warwick Streamer',''),('Warwick Thumb SC',''),('Warwick Dolphin',''),('Warwick Alien',''),('Warwick Thumb BO','2001'),('Warwick FNA Jazzman','2002'),('Warwick Infinity',''),('Warwick Thumb NT',''),('Warwick Star Bass',''),('Warwick Fortress',''),('Warwick Vampyre',''),('Warwick Triumph',''),('Warwick Rockbass Alien',''),('Warwick SpaceBass','')],'Warwick bass named on the Warwick page.')
L('Combo amp','Warwick',WAR,[('Warwick BC 10',''),('Warwick BC 20',''),('Warwick BC 40',''),('Warwick BC 80',''),('Warwick BC 150',''),('Warwick BC 300','')],'Warwick bass combo named on the Warwick page.')
L('Amp head','Warwick',WAR,[('Warwick WA 300',''),('Warwick WA 600',''),('Warwick LWA 1000',''),('Warwick Hellborg',''),('Warwick ProFet',''),('Warwick Quad',''),('Warwick Tubepath',''),('Warwick X-Treme','')],'Warwick amplifier named on the Warwick page.')
L('Speaker cabinet','Warwick',WAR,[('Warwick WCA 115',''),('Warwick WCA 410',''),('Warwick WCA 610',''),('Warwick JH Club Cab',''),('Warwick JH Lo Cab',''),('Warwick JH HC',''),('Warwick JH BC','')],'Warwick cabinet named on the Warwick page.')
# Spector, Steinberger
L('Solid-body electric guitar','Spector',SPE,[('Spector G-1','1976')],'Original Spector guitar.')
L('Electric bass guitar','Spector',SPE,[('Spector SB-1','1976'),('Spector NS-1','1977'),('Spector NS-2','1979'),('Spector NS-5',''),('Spector SD',''),('Spector Euro',''),('Spector Performer','')],'Spector bass named on the Spector page.')
L('Electric bass guitar','Steinberger',STB,[('Steinberger Spirit','1992'),('Steinberger Synapse','2006'),('Steinberger Transcale','2006'),('Steinberger Q-series','1990')],'Steinberger line named on the Steinberger page.')
# Yamaha
YG=[('Yamaha SG3','1965'),('Yamaha SG5','1966–1971'),('Yamaha SG7','1966'),('Yamaha SGV300','2000'),('Yamaha SG800','2000')]
L('Solid-body electric guitar','Yamaha',YEM,YG,'Yamaha SG model named on the Yamaha electric guitar models page.')
L('Solid-body electric guitar','Yamaha',YEM,[('Yamaha RGX 110',''),('Yamaha RGX 120D','1994–1998'),('Yamaha RGX 211',''),('Yamaha RGX 312','1987–1993'),('Yamaha RGX 603','1987–1990'),('Yamaha RGX 610m','1987–1990'),('Yamaha RGX 611m','1987–1990'),('Yamaha RGX 612s','1987–1990'),('Yamaha RGX 420DZ','1994–1998'),('Yamaha RGX 421D','1994–1998'),('Yamaha RGX 621D',''),('Yamaha RGX 820R','1993–1995'),('Yamaha RGX 821','1994–1996'),('Yamaha RGX 121S','2002'),('Yamaha RGX 420S','2003'),('Yamaha RGX 320FZ','2005'),('Yamaha RGX 520FZ','2005'),('Yamaha RGX-TT','2000'),('Yamaha RGZ 112P',''),('Yamaha RGZ 321P',''),('Yamaha RGZ 611M','1989–1991'),('Yamaha RGZ 612P',''),('Yamaha RGZ Custom',''),('Yamaha RGZ-211M',''),('Yamaha RGZ-820R','')],'Yamaha RGX or RGZ model named on the Yamaha electric guitar models page.')
L('Solid-body electric guitar','Yamaha',YAM,[('Yamaha PAC912','1990'),('Yamaha PAC1221','1990'),('Yamaha PAC1412','1990'),('Yamaha PAC1421','1990'),('Yamaha PAC904','1994'),('Yamaha Pacifica USA1','1995'),('Yamaha Pacifica USA2','1995'),('Yamaha PAC303-12','1996'),('Yamaha PAC311MS','1997'),('Yamaha PAC1511MS','1997'),('Yamaha PAC1512CD','1999'),('Yamaha PAC510','2011'),('Yamaha PAC311','2011'),('Yamaha PAC611','2011'),('Yamaha PAC120','2011'),('Yamaha PAC1611MS',''),('Yamaha PAC012',''),('Yamaha PAC112',''),('Yamaha PAC212',''),('Yamaha PAC311H',''),('Yamaha Pacifica Standard Plus','2024'),('Yamaha Pacifica Professional','2024')],'Yamaha Pacifica model named on Yamaha\'s Pacifica history.')
L('Electric bass guitar','Yamaha',YEM,[('Yamaha RBX5',''),('Yamaha RBX755A',''),('Yamaha RBX550',''),('Yamaha RBX600',''),('Yamaha RBX800',''),('Yamaha RBX1000',''),('Yamaha RBX6JM',''),('Yamaha RBX-JM2','')],'Yamaha RBX bass series (introduced 1987) named on the Yamaha electric guitar models page.')
# Martin sizes
L('Steel-string acoustic guitar','Martin',VMS,[('Martin 0','1854'),('Martin 00 Grand Concert','1873'),('Martin 000','1902'),('Martin 0-18','1945'),('Martin 00-18','1945'),('Martin 000-28','1928'),('Martin OM-28','1930'),('Martin 000-17',''),('Martin 000-44',''),('Martin 000-45',''),('Martin 00-21',''),('Martin 1-17','')],'Martin body size or model named on the vintagemartin.com sizes page.')
# amps
L('Combo amp','Orange',ORA,[('Orange Jimmy Bean','1970s'),('Orange Custom Reverb Twin','1970s'),('Orange AD30','1998'),('Orange AD15','1998'),('Orange Rocker 32','')],'Orange combo named on the Orange page.')
L('Amp head','Orange',ORA,[('Orange OMEC Digital','1975'),('Orange Series Two Super Bass','1979'),('Orange Overdrive 120','1994'),('Orange Graphic 80','1994'),('Orange Overdrive 80','1994'),('Orange Super Bass 120','1990s'),('Orange OTR','late 1990s'),('Orange Rockerverb','2003'),('Orange Tiny Terror','2006'),('Orange OR15',''),('Orange OR30',''),('Orange OR100',''),('Orange TH100',''),('Orange Gain Baby 100',''),('Orange AD200','')],'Orange amplifier named on the Orange page.')
L('Combo amp','Peavey',PEA,[('Peavey Bandit','1980'),('Peavey Classic 20','1994'),('Peavey 6534+','2010'),('Peavey Nano Vypyr','2012'),('Peavey Vypyr VIP','2013'),('Peavey ValveKing','2005')],'Peavey combo named on the Peavey page.')
L('Amp head','Peavey',PEA,[('Peavey MKIII Bass Head','1979'),('Peavey MKIV Bass Head','1981')],'Peavey bass head named on the Peavey page.')
L('Solid-body electric guitar','Peavey',PEA,[('Peavey Wolfgang',''),('Peavey HP2','2017')],'Peavey guitar named on the Peavey page.')
L('Combo amp','Ampeg',AMP,[('Ampeg Reverberocket','1961'),('Ampeg Gemini II G-15L','1965–1968'),('Ampeg GT-10','1971–1980'),('Ampeg BT-15','1966'),('Ampeg Portaflex PF-350','2011'),('Ampeg VT-22','1970'),('Ampeg VT-40','1970')],'Ampeg combo named on the Ampeg page.')
L('Amp head','Ampeg',AMP,[('Ampeg V-2','1970'),('Ampeg V-3','1970'),('Ampeg V-4','1970s'),('Ampeg V-4B','1970s'),('Ampeg V-22',''),('Ampeg B-25','1969'),('Ampeg SVT-VR',''),('Ampeg SVT-HD','1987'),('Ampeg SVT-100',''),('Ampeg SVT-350H',''),('Ampeg SVT-3 Pro',''),('Ampeg SVT-6 Pro',''),('Ampeg PortaBass 800',''),('Ampeg B-200R','')],'Ampeg head named on the Ampeg page.')
L('Speaker cabinet','Ampeg',AMP,[('Ampeg SVT-410HLF',''),('Ampeg SVT-610HLF','')],'Ampeg cabinet named on the Ampeg page.')
L('Electric bass guitar','Ampeg',AMP,[('Ampeg Baby Bass','1962'),('Ampeg Devil Bass','1966–1969'),('Ampeg AEB-1 Horizontal Bass',''),('Ampeg Big Stud','1973–1975')],'Ampeg bass named on the Ampeg page.')
L('Solid-body electric guitar','Ampeg',AMP,[('Ampeg Little Stud','')],'Ampeg guitar named on the Ampeg page.')
L('Combo amp','Fender',FAMP,[('Fender Princeton Reverb','1963')],'Blackface Princeton Reverb; silverface 1967 to 1981.')
