import json, os
W='https://en.wikipedia.org/wiki/'
def V(n,mk,y='',d=''):
    o={'n':n,'mk':mk}
    if y: o['y']=y
    if d: o['d']=d
    return o
def X(n,mk,y,s,d,v,dt,a=''):
    return {'n':n,'a':a,'d':d,'mk':mk,'y':y,'s':s,'v':v,'dt':dt}
S,C,N,F,P,O,L,H='Sony','Canon','Nikon','Fujifilm','Panasonic','Olympus','Leica','Hasselblad'
mirrorless={'n':'Mirrorless camera','a':'mirrorless interchangeable-lens camera · MILC',
 'd':'Digital stills and video body with exchangeable lenses and no reflex mirror; any sensor size, medium format included.',
 't':['full frame','APS-C','Micro Four Thirds','medium format'],
 's':'https://www.keh.com/shop/cameras/digital-cameras/mirrorless.html',
 'x':[
  X('Panasonic Lumix G / GH',P,'2008',W+'Micro_Four_Thirds_system','Panasonic Micro Four Thirds bodies from the first MFT camera on; GH is the video-led branch.',
    [V('Lumix DMC-G1',P,'2008','first Micro Four Thirds camera'),V('Lumix GH1',P,'2009','adds HD video'),V('Lumix GH2',P,'2010'),V('Lumix GH3',P),V('Lumix GH4',P),
     V('Lumix GH5',P,'2017'),V('Lumix GH5S',P,'','filmmaking sister model'),V('Lumix GH5 II',P,'2021'),V('Lumix GH6',P,'2022'),V('Lumix GH7',P),V('Lumix G9',P)],
    'Micro Four Thirds mount · Four Thirds sensor 17.3 × 13 mm · stills or video-first bodies'),
  X('Olympus OM-D E-M5',O,'2012',W+'Olympus_OM-D_E-M5','Compact Micro Four Thirds body below the E-M1.',
    [V('OM-D E-M5',O,'2012'),V('OM-D E-M5 Mark II',O),V('OM-D E-M5 Mark III',O),V('OM-5',O)],
    'Micro Four Thirds mount · 16–20 MP Four Thirds sensor'),
  X('Olympus OM-D E-M1',O,'2013',W+'Olympus_OM-D_E-M1','Flagship weather-sealed Micro Four Thirds body; first in the system with on-sensor phase detection.',
    [V('OM-D E-M1',O,'2013'),V('OM-D E-M1 Mark II',O,'2016'),V('OM-D E-M1 Mark III',O),V('OM-D E-M1X',O,'','integrated grip'),V('OM-1',O)],
    'Micro Four Thirds mount · 16–20 MP Four Thirds sensor · grip size'),
  X('Sony α7',S,'2013',W+'Sony_α7','The first full-frame mirrorless series; base, high-resolution R, low-light/video S and compact C branches.',
    [V('α7',S,'2013'),V('α7R',S,'2013'),V('α7S',S,'2014'),V('α7 II',S,'2014'),V('α7R II',S,'2015'),V('α7S II',S,'2015'),V('α7R III',S,'2017'),
     V('α7 III',S,'2018'),V('α7R IV',S,'2019'),V('α7S III',S,'2020'),V('α7C',S,'2020'),V('α7 IV',S,'2021'),V('α7R V',S),V('α7C II',S),V('α7CR',S),V('α7 V',S)],
    'Sony E-mount · full-frame sensor · base / R / S / C branch · generation I–V',a='Alpha 7 · a7'),
  X('Sony α1',S,'2021',W+'Sony_α1','Sony flagship full-frame body with a 50 MP stacked sensor.',
    [V('α1',S,'2021'),V('α1 II',S,'2024')],'Sony E-mount · full-frame stacked sensor',a='Alpha 1 · a1'),
  X('Sony α6000',S,'2014',W+'Sony_α6000','Compact rangefinder-style APS-C body and the long a6000 family that followed it.',
    [V('α6000',S,'2014'),V('α6300',S,'2016'),V('α6500',S,'2016'),V('α6400',S,'2019'),V('α6100',S),V('α6600',S),V('α6700',S,'2023')],
    'Sony E-mount · APS-C sensor 23.5 × 15.6 mm · stabilised or not',a='a6000 series'),
  X('Fujifilm X-Pro',F,'2012',W+'Fujifilm_X-Pro1','Rangefinder-style APS-C body with a hybrid optical/electronic viewfinder; launched the X-mount.',
    [V('X-Pro1',F,'2012'),V('X-Pro2',F,'2016'),V('X-Pro3',F)],'Fujifilm X-mount · APS-C X-Trans sensor · hybrid viewfinder'),
  X('Fujifilm X-T',F,'2014',W+'Fujifilm_X-T1','SLR-style APS-C body, the core X-mount series.',
    [V('X-T1',F,'2014'),V('X-T2',F,'2016'),V('X-T3',F),V('X-T4',F),V('X-T5',F),V('X-T10 / X-T20 / X-T30 / X-T50',F,'','smaller sister line')],
    'Fujifilm X-mount · APS-C X-Trans sensor'),
  X('Fujifilm X-E',F,'',W+'Fujifilm_X-mount','Slim rangefinder-style APS-C body below the X-Pro.',
    [V('X-E1',F),V('X-E2',F),V('X-E2s',F),V('X-E3',F),V('X-E4',F),V('X-E5',F)],'Fujifilm X-mount · APS-C sensor'),
  X('Fujifilm X-H',F,'',W+'Fujifilm_X-mount','DSLR-style APS-C body, the largest X-mount series.',
    [V('X-H1',F),V('X-H2',F),V('X-H2S',F)],'Fujifilm X-mount · APS-C sensor'),
  X('Canon EOS R full frame',C,'2018',W+'Canon_RF_mount','Canon full-frame mirrorless bodies built on the RF mount.',
    [V('EOS R',C,'2018','first RF body'),V('EOS RP',C,'2019'),V('EOS R5',C,'2020'),V('EOS R6',C,'2020'),V('EOS R5 C',C,'2022'),V('EOS R6 Mark II',C),
     V('EOS R5 Mark II',C,'2024')],'Canon RF mount · full-frame sensor · resolution vs speed models',a='EOS R5 · EOS R6'),
  X('Canon EOS R APS-C',C,'2022',W+'Canon_EOS_R7','Canon APS-C mirrorless bodies on the RF mount using RF-S lenses.',
    [V('EOS R7',C,'2022'),V('EOS R10',C,'2022'),V('EOS R50',C)],'Canon RF mount (RF-S lenses) · APS-C sensor'),
  X('Nikon Z full frame',N,'2018',W+'Nikon_Z-mount','Nikon FX mirrorless bodies on the wide 16 mm-flange Z mount.',
    [V('Z6',N,'2018'),V('Z7',N,'2018'),V('Z5',N,'2020'),V('Z6II',N,'2020'),V('Z7II',N,'2020'),V('Z9',N,'2021','flagship without a mechanical shutter'),
     V('Zf',N,'2023','retro dials'),V('Z8',N,'2023','Z9-generation in a smaller body'),V('Z6III',N,'2024'),V('Z5II',N,'2025')],
    'Nikon Z mount · FX full-frame sensor 24.5 or 45.7 MP'),
  X('Nikon Z DX',N,'2019',W+'Nikon_Z-mount','Nikon APS-C (DX) mirrorless bodies on the Z mount.',
    [V('Z50',N,'2019'),V('Zfc',N,'2021','retro dials'),V('Z30',N,'2022'),V('Z50II',N,'2024')],'Nikon Z mount · DX (APS-C) 20.9 MP sensor'),
  X('Leica SL',L,'2015',W+'Leica_SL','Leica full-frame mirrorless system camera that gave the L-mount its name.',
    [V('SL (Typ 601)',L,'2015'),V('SL2',L,'2019'),V('SL2-S',L),V('SL3 (Type 5404)',L)],'Leica L-mount · full-frame sensor'),
  X('Leica T / CL',L,'2014',W+'L-Mount','Leica APS-C mirrorless bodies; the T introduced the mount later named L-mount.',
    [V('T (Typ 701)',L,'2014'),V('TL',L),V('TL2',L),V('CL (Typ 7323)',L,'2017','rangefinder-style with built-in viewfinder')],'Leica L-mount · APS-C sensor'),
  X('Panasonic Lumix S',P,'2019',W+'Panasonic_Lumix_DC-S1','Panasonic full-frame L-mount bodies from the L-Mount Alliance.',
    [V('Lumix S1',P,'2019'),V('Lumix S1R',P,'2019'),V('Lumix S1H',P,'2019','video-oriented'),V('Lumix S5',P),V('Lumix S5 II',P),V('Lumix S1 II',P)],
    'Leica L-mount · full-frame sensor 24 or 47 MP'),
  X('Fujifilm GFX',F,'',W+'Fujifilm_G-mount','Fujifilm medium-format mirrorless bodies on the G mount.',
    [V('GFX 50S',F),V('GFX 50R',F),V('GFX100',F),V('GFX100S',F),V('GFX50S II',F),V('GFX100 II',F),V('GFX100S II',F),V('GFX100RF',F,'','fixed-lens')],
    'Fujifilm G mount · 43.8 × 32.9 mm medium-format sensor'),
  X('Hasselblad X',H,'2016',W+'Hasselblad_X1D','Hasselblad compact medium-format mirrorless bodies on the XCD mount.',
    [V('X1D-50c',H,'2016'),V('X1D II 50C',H,'2019'),V('907X 50C',H,'2019','modular body with CFV II 50C back'),V('X2D 100C',H,'2022'),V('907X 100C',H,'2024')],
    'Hasselblad XCD mount · 43.8 × 32.9 mm medium-format sensor 50 or 100 MP'),
 ],
 'm':[['fp','Sigma']]}
dslr={'n':'DSLR camera','a':'digital single-lens reflex camera','d':'Digital body with exchangeable lenses and a mirror-and-prism optical viewfinder.',
 't':['full frame','APS-C','APS-H','Four Thirds'],'s':'https://www.bhphotovideo.com/c/product/1274705-REG/canon_eos_5d_mark_iv.html',
 'x':[
  X('Canon EOS-1D',C,'2001',W+'Canon_EOS-1D','Canon professional flagship DSLR line with integrated grip.',
    [V('EOS-1D',C,'2001'),V('EOS-1Ds',C,'2002'),V('EOS-1D Mark II',C,'2004'),V('EOS-1Ds Mark II',C),V('EOS-1D Mark II N',C),V('EOS-1D Mark III',C),
     V('EOS-1D Mark IV',C),V('EOS-1D X',C),V('EOS-1D X Mark II',C),V('EOS-1D X Mark III',C)],'Canon EF mount · APS-H or full-frame sensor · Ds = high resolution'),
  X('Canon EOS 5D',C,'2005',W+'Canon_EOS_5D','Canon full-frame DSLR line below the EOS-1D flagships.',
    [V('EOS 5D',C,'2005'),V('EOS 5D Mark II',C,'2008'),V('EOS 5D Mark III',C,'2012'),V('EOS 5DS / 5DS R',C,'2015'),V('EOS 5D Mark IV',C,'2016')],
    'Canon EF mount · full-frame sensor'),
  X('Nikon D3',N,'2007',W+'Nikon_D3','Nikon first full-frame (FX) professional DSLR.',
    [V('D3',N,'2007'),V('D3X',N,'2008','24.5 MP'),V('D3S',N,'2009'),V('D4',N,'2012','successor')],'Nikon F mount · FX full-frame sensor'),
  X('Nikon D700 / D800 / D850',N,'2008',W+'Nikon_D850','Nikon smaller full-frame DSLR line, from the D3-sensored D700 to the 45 MP D850.',
    [V('D700',N,'2008','D3 sensor'),V('D800',N,'2012'),V('D810',N,'2014'),V('D850',N,'2017')],'Nikon F mount · FX full-frame sensor 12–45 MP'),
  X('Pentax K-1','Pentax','2016',W+'Pentax_K-1','Pentax full-frame DSLR for the K mount.',
    [V('K-1','Pentax','2016'),V('K-1 Mark II','Pentax','2018')],'Pentax K mount (KAF2) · full-frame sensor'),
  X('Pentax K-3','Pentax','2013',W+'Pentax_K-3','Pentax high-end APS-C DSLR.',
    [V('K-3','Pentax','2013'),V('K-3 II','Pentax'),V('K-3 Mark III','Pentax')],'Pentax K mount (KAF3/KAF2) · APS-C sensor'),
 ],
 'm':[['N Digital','Contax'],['Digilux 3','Leica'],['E-300','Olympus'],['DMC-L1','Panasonic']]}
rf={'n':'Digital rangefinder camera','a':'','d':'Digital body with a rangefinder focusing and framing window and exchangeable lenses.',
 't':['APS-H','APS-C','full frame','monochrome sensor'],'s':'https://www.keh.com/shop/leica-m11-digital-camera-body-black-finish-60mp-20200.html',
 'x':[
  X('Leica M digital',L,'2006',W+'Leica_M8','The digital continuation of the Leica M rangefinder, generation by generation.',
    [V('M8',L,'2006','APS-H, 1.33 crop'),V('M8.2',L,'2008'),V('M9',L,'2009','first full-frame digital M, Kodak CCD'),V('M9 Titanium',L,'2010','500 made'),V('M9-P',L,'2011'),
     V('M-E',L,'2012'),V('M (Typ 240)',L,'2012','CMOS sensor'),V('M-P (Typ 240)',L,'2014'),V('M (Typ 262)',L),V('M-D (Typ 262)',L),
     V('M10',L,'2017'),V('M10-P',L,'2018'),V('M10-D',L,'2018'),V('M10-R',L,'2020'),V('M11',L,'2022','60 MP BSI'),V('M11 (Type 2416)',L)],
    'Leica M mount · APS-H then full-frame sensor · black or silver chrome'),
  X('Leica M Monochrom',L,'2012',W+'Leica_M_Monochrom','Leica M with a black-and-white-only sensor, no colour filter array.',
    [V('M Monochrom',L,'2012','M9-based CCD'),V('M Monochrom (Typ 246)',L,'2015'),V('M10 Monochrom',L,'2020','41 MP')],'Leica M mount · full-frame monochrome sensor'),
  X('Epson R-D1','Epson','2004',W+'Epson_R-D1','The first commercially produced digital rangefinder, built with Cosina.',
    [V('R-D1','Epson','2004'),V('R-D1s','Epson','2006','firmware upgrade'),V('R-D1x','Epson','2009','Japan only'),V('R-D1xG','Epson','2009','removable grip')],
    'Leica M mount · APS-C CCD 1.53 crop · analogue-style dials'),
  X('Pixii','Pixii','2020',W+'Pixii_(cameras)','Screenless, upgradeable French digital rangefinder that relies on a phone app.',
    [V('A1112','Pixii','2020','12 MP, global shutter'),V('A1571','Pixii','2021','26 MP'),V('A2572','Pixii','2022'),V('A2572+ (Pixii+)','Pixii','2023'),V('Pixii Max','Pixii','2024','full frame')],
    'Leica M mount · APS-C or full-frame sensor · internal storage only'),
 ]}
back={'n':'Digital back','a':'','d':'Digital capture unit with sensor that replaces the film back of a medium- or large-format camera.',
 't':['colour','achromatic (monochrome)','multi-shot'],'s':'https://heritage-digitaltransitions.com/digital-backs/',
 'x':[
  X('Phase One P / IQ backs','Phase One','2004',W+'Phase_One_(company)','Phase One medium-format digital backs, from the P series to the IQ4.',
    [V('P20 / P25','Phase One','2004'),V('P45+','Phase One','2007'),V('P65+','Phase One','2008'),V('IQ180','Phase One','2011'),V('IQ260 Achromatic','Phase One','2013'),
     V('IQ3 100MP','Phase One','2016'),V('IQ3 100MP Trichromatic','Phase One','2017'),V('IQ4 150MP','Phase One','2018'),V('IQ4 150MP Achromatic','Phase One','2018'),
     V('IQ4 100MP Trichromatic','Phase One','2018')],'Phase One XF/XT camera systems and other medium-format bodies · colour, achromatic or trichromatic'),
  X('Hasselblad CFV',H,'2006',W+'Hasselblad','Digital backs that fit Hasselblad V-system film cameras.',
    [V('CFV-16',H,'2006','supplied with 503CWD'),V('CFV-50c',H,'2014'),V('CFV II 50C',H,'2019'),V('CFV 100C',H,'2024')],'Hasselblad V-system back interface · 50 or 100 MP medium-format sensor'),
 ]}
K='knowledge'
brands=[
 {'n':'Sony','c':'Japan','f':'1946','seg':'Mainstream to professional','d':'Electronics group whose Alpha cameras use the E-mount.','lines':['Alpha (E-mount)'],'sig':['Sony α7','Sony α1','Sony α6000'],'s':K},
 {'n':'Canon','c':'Japan','f':'1937','seg':'Mainstream to professional','d':'Camera and imaging maker with the EF and RF mounts.','lines':['EOS (EF, RF)'],'sig':['Canon EOS 5D','Canon EOS-1D','Canon EOS R full frame'],'rel':['Nikon'],'s':K},
 {'n':'Nikon','c':'Japan','f':'1917','seg':'Mainstream to professional','d':'Optics and camera maker with the F and Z mounts.','lines':['D (F mount)','Z'],'sig':['Nikon D3','Nikon Z full frame'],'rel':['Canon'],'s':K},
 {'n':'Fujifilm','c':'Japan','f':'1934','seg':'Enthusiast','d':'Film and imaging company making X (APS-C) and GFX (medium format) systems.','lines':['X','GFX'],'sig':['Fujifilm X-T','Fujifilm X-Pro','Fujifilm GFX'],'s':K},
 {'n':'Panasonic','c':'Japan','f':'1918','seg':'Mainstream to video','d':'Electronics group selling cameras as Lumix; co-founder of Micro Four Thirds and L-Mount Alliance member.','lines':['Lumix G','Lumix S'],'sig':['Panasonic Lumix G / GH','Panasonic Lumix S'],'rel':['Olympus','Leica'],'s':K},
 {'n':'Olympus','c':'Japan','f':'1919','seg':'Enthusiast','d':'Optics maker whose camera business continued as OM System from 2021.','lines':['OM-D'],'sig':['Olympus OM-D E-M1','Olympus OM-D E-M5'],'rel':['Panasonic'],'s':K},
 {'n':'Leica','c':'Germany','seg':'Luxury','d':'German camera maker of the M rangefinder and the L-mount SL system.','lines':['M','SL','CL / TL'],'sig':['Leica M digital','Leica M Monochrom','Leica SL'],'rel':['Panasonic'],'s':K},
 {'n':'Pentax','c':'Japan','seg':'Enthusiast','d':'Camera brand of the K-mount DSLR, owned by Ricoh.','lines':['K'],'sig':['Pentax K-1','Pentax K-3'],'s':K},
 {'n':'Hasselblad','c':'Sweden','f':'1841','seg':'Luxury medium format','d':'Swedish medium-format camera maker of the V, H and X systems.','lines':['V','H','X','907X'],'sig':['Hasselblad X','Hasselblad CFV'],'s':W+'Hasselblad'},
 {'n':'Epson','c':'Japan','seg':'Electronics','d':'Printer and electronics maker that produced the R-D1 rangefinder with Cosina.','lines':['R-D1'],'sig':['Epson R-D1'],'s':W+'Epson_R-D1'},
 {'n':'Pixii','c':'France','seg':'Independent','d':'French start-up making a screenless digital rangefinder for M-mount lenses.','sig':['Pixii'],'s':W+'Pixii_(cameras)'},
 {'n':'Phase One','c':'Denmark','seg':'Professional medium format','d':'Copenhagen maker of medium-format digital backs and camera systems.','lines':['P','P+','IQ','XF','XT'],'sig':['Phase One P / IQ backs'],'s':W+'Phase_One_(company)'},
]
notes=('Kept all four planned kinds. Flat old model lists became archetype versions (system/mount families). Removed old "r" ranges (now archetypes/brand lines). '
 'Dropped from old data only by merging: Sony a7 II/III/C/C II/R II/R III/R V/S III, a1, a6400/a6600, Canon R5 Mk II/R50/R6/R6 Mk II/R7, Fujifilm X-E4/X-E5/X-T2, Nikon Z50/Z6, Leica SL3, GH5, EOS 5D Mk IV, EOS-1Ds Mk II, D3, Leica M8–M11/Monochrom, R-D1/R-D1s, Pixii A1112, IQ4 backs all appear as versions. '
 'Left out: Sony a7R VI (year uncertain on page), Fujifilm entry-level X-A/X-M/X-S lines and Canon R3/R8/R1/R100 (no retrieved years and not in brief; could be added), Leica M11 variants (M11-P, M11 Monochrom, M11-D, M11-V: not on the retrieved page), Pentax K-3 Mark III Monochrome, Hasselblad H6D (camera system, not a back), OM System OM-3. '
 'Years omitted where retrieved pages gave none. Olympus kept as maker name for OM-D (OM System brand noted in register). Parallel web_fetch unavailable (402); all pages via WebFetch.')
out={'kinds':[mirrorless,dslr,rf,back],'brands':brands,'traditions':[],'notes':notes}
p='work/D4/shelves/00_00.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
print('archetypes',sum(len(k['x']) for k in out['kinds']))
