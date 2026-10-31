import json,os,re
d=json.load(open('out/D4.json'))
SKIP={'Lucky SHD','Isopan and Isochrom','ORWO NP and PAN','Rera Pan 100','Silberra Orta and Cinema','Svema Foto and FN','Svema and Tasma colour negative','Konica Sakuracolor and later films','Konica slide films','ORWO Color negative','ORWO Color and ORWO Chrom slide','Rera Chrome 100','Rollei discontinued slide films','Svema and Tasma colour slide','Negracolor','Lucky colour negative','Gevacolor negative','Agfacolor Negativfilm','Agfacolor Umkehrfilm','Polaroid peel-apart Types','Polaroid Originals Spectra film','Fuda Color','Fudapan'}
SKIP|={'ORWO Color and ORWO Chrom slide','Rollei discontinued slide films'}
KIND={'bw':'Black-and-white film','col':'Colour negative film','slide':'Slide film','peel':'Peel-apart instant film','integral':'Integral instant film'}
fam=[];cur=None
for l in open('work/CMP_DEV/film_raw.txt'):
    l=l.rstrip('\n')
    if l.startswith('@'):
        k,n,mk,dd=l[1:].split('||'); cur={'k':KIND[k],'n':n,'mk':mk,'d':dd,'v':[]}; fam.append(cur)
    elif l: m,y=l.split('|'); cur['v'].append((m,y))
src='https://en.wikipedia.org/wiki/List_of_discontinued_photographic_films'
kinds={}
for de in d['depts']:
  for s in de['s']:
    for k in s['k']: kinds[k['n']]=k
added=0;nv=0
for f in fam:
    if f['n'] in SKIP: continue
    # first year
    ys=[int(x) for v in f['v'] for x in re.findall(r'\b(1[89]\d\d|20\d\d)\b',v[1].split('–')[0])]
    k=kinds[f['k']]
    if any(x['n'].lower()==f['n'].lower() for x in k['x']): continue
    e={'n':f['n'],'a':'','d':f['d'],'mk':f['mk'],'y':str(min(ys)) if ys else '','s':src,'v':[{'n':m,'mk':f['mk'],'y':y,'d':''} for m,y in f['v']],'g':f['mk']}
    xs=k['x']; idx=max([i for i,x in enumerate(xs) if x.get('g')==f['mk']],default=len(xs)-1)+1
    k['x']=xs[:idx]+[e]+xs[idx:]; added+=1; nv+=len(e['v'])
# version merges into existing entries
def addv(kind,name,vs):
    for x in kinds[kind]['x']:
        if x['n']==name:
            have={v['n'].lower() for v in x['v']}
            for m,y in vs:
                if m.lower() not in have: x['v'].append({'n':m,'mk':x.get('mk',''),'y':y,'d':''}); globals()['nv']+=1
addv('Colour negative film','Gevacolor N5',[('Gevacolor N5 Mask','?–?'),('Gevacolor N3','?–?')])
addv('Colour negative film','Fuda Color 100',[('Color GA 100','c1990–?')])
addv('Black-and-white film','Luckyfilm SHD',[('New SHD 100','2017–2019')])
add_note=" Tail of the discontinued list read to its end (the page ends with Valca): Foma, Forte, Foton, Fotoimpex, Gigabit, Maco, Negra, Gevaert, Tasma, SPUR, Factory No. 5 and Polaroid slide films were added; Fujifilm, Ilford, Kodak and Konica discontinued rows beyond those already in this kind, and the Rollei lines whose type the page does not state, are still not itemised."
for kn in ['Colour negative film','Black-and-white film','Slide film']:
    k=kinds[kn]; k['sel']=k['sel'].replace(", and the last part of the discontinued list (after Valca), which was not read",'')+add_note
# camera bodies
CAM=[
 ('Film SLR camera','Konica Autoreflex','Konica','1965','Konica AR','Konica 35 mm SLR range made until 1988, all on the Konica AR bayonet mount.','https://en.wikipedia.org/wiki/Konica_Autoreflex',[('Auto-Reflex','1965–1968'),('Auto-Reflex P','1966–1968'),('Autoreflex T','1968–1970'),('Autoreflex A','1968–1971'),('Autoreflex T2','1970–1973'),('Autoreflex A2','1971–1972'),('Autoreflex A1000','1972–1973'),('Autoreflex T3','1973–1975'),('Autoreflex A3','1973'),('Autoreflex T3N','1975–1978'),('Autoreflex TC','1976–1982'),('Autoreflex T4','1978–1979'),('TC-X','1985–1987')]),
 ('Film SLR camera','Konica F','Konica','1960','Konica F','Konica first 35 mm SLR, with built-in coupled metering and a top shutter speed of 1/2000 s.','https://en.wikipedia.org/wiki/Konica_F',[('F','1960'),('FS','1962'),('FSW','1962'),('FP','1963'),('FM','1965')]),
 ('Film SLR camera','Canon Pellix','Canon','1965','Canon FL','Manual-focus 35 mm SLR with a fixed semi-transparent mirror, on the Canon FL mount.','https://en.wikipedia.org/wiki/Canon_Pellix',[('Pellix','1965'),('Pellix QL','1966')]),
 ('Film SLR camera','Icarex 35','Zeiss Ikon','1966','Icarex BM','Mid-range manual-focus 35 mm SLR family on the Icarex BM bayonet, below the Contarex.','https://en.wikipedia.org/wiki/Icarex',[('Icarex 35','1966–1972'),('Icarex 35 CS','1968'),('Icarex 35 S','1969–1972'),('Icarex SL 706','1971–1972')]),
 ('Film SLR camera','Rolleiflex SL35','Rollei','1970','Rolleiflex SL35','35 mm SLR line made by Rollei from 1970 to 1982 on the QBM bayonet.','https://en.wikipedia.org/wiki/Rolleiflex_SL35',[('SL35','1970'),('SL350','1974'),('SL35 M and SL35 ME','1976'),('SL35 E','1978')]),
 ('Film SLR camera','Praktiflex','Kamera-Werkstätten','1939','Praktiflex','Dresden 35 mm SLR whose layout became the template for later 35 mm SLRs, with an instant-return mirror.','https://en.wikipedia.org/wiki/Praktiflex',[('Praktiflex','1939'),('Praktiflex II','1947')]),
 ('Film SLR camera','Miranda T','Miranda','','Miranda bayonet/M44','Japanese 35 mm SLR maker active until 1976, known for interchangeable prisms on the Miranda T and Sensorex.','https://en.wikipedia.org/wiki/Miranda_Camera_Company',[('Miranda T',''),('Miranda Sensorex','')]),
 ('Film SLR camera','Minolta Vectis S','Minolta','','Minolta V','Compact APS film SLR cameras on the Vectis V mount, with a mirror viewfinder instead of a prism.','https://en.wikipedia.org/wiki/Minolta_Vectis_S-1',[('Vectis S-1',''),('Vectis S-100','')]),
 ('Film SLR camera','Olympus Pen F','Olympus','1963','Olympus Pen F','Half-frame 35 mm film SLR with interchangeable lenses, among the smallest SLR systems built.','https://en.wikipedia.org/wiki/Olympus_Pen_F',[('Pen F','1963–1966'),('Pen FT','1966–1972'),('Pen FV','1967–1970')]),
 ('Film rangefinder camera','Hasselblad XPan','Hasselblad','1998','Hasselblad Xpan','35 mm rangefinder designed and built by Fujifilm that uses the full film area for panoramic or standard frames.','https://en.wikipedia.org/wiki/Hasselblad_XPan',[('XPan','1998'),('XPan II','2003')]),
 ('Medium-format SLR camera','Pentacon Six','Pentacon','1966','Pentacon Six','East German 6×6 medium-format SLR system made from 1966 to 1992 on a breech-lock bayonet.','https://en.wikipedia.org/wiki/Pentacon_Six',[('Praktisix',''),('Pentacon Six',''),('Pentacon Six TL','')]),
 ('Cartridge-film camera','Pentax Auto 110','Pentax','1978','Pentax Auto 110','Fully automatic SLR for Kodak 110 cartridges, sold as Pentax System 10 until 1985.','https://en.wikipedia.org/wiki/Pentax_Auto_110',[('Auto 110','1978'),('Auto 110 Super','1982')]),
 ('DSLR camera','Contax N Digital','Contax','2002','Contax N','Six-megapixel digital SLR on the Contax N mount, the first full-frame digital SLR.','https://en.wikipedia.org/wiki/Contax_N_Digital',[('N Digital','2002')]),
 ('DSLR camera','Sigma SD1','Sigma','2011','Sigma SA','Digital SLR with a Foveon X3 sensor on the Sigma SA mount, sibling to the SD9, SD10, SD14 and SD15.','https://en.wikipedia.org/wiki/Sigma_SD1',[('SD1','2011'),('SD1 Merrill','2012')]),
 ('Mirrorless camera','Samsung NX mini','Samsung','2014','Samsung NX mini','Rangefinder-style mirrorless camera with a 1-inch sensor on the NX-M mount.','https://en.wikipedia.org/wiki/Samsung_NX_mini',[('NX mini','2014')]),
 ('Compact camera','Sony Mavica','Sony','1981','Sony Mavica','Sony camera brand that saved images to removable disks, first as analog still video and later digital.','https://en.wikipedia.org/wiki/Sony_Mavica',[('Mavica prototype','1981'),('MVC-FD5','1997'),('MVC-FD7','1997'),('MVC-FD88','1999'),('MVC-CD1000','2000'),('MVC-FD100','2002'),('MVC-CD400','2002'),('MVC-CD500','2003')]),
]
cadd=0
for kn,n,mk,y,g,dd,u,vs in CAM:
    k=kinds[kn]
    if any(x['n'].lower()==n.lower() for x in k['x']): continue
    e={'n':n,'a':'','d':dd,'mk':mk,'y':y,'s':u,'v':[{'n':m,'mk':mk,'y':yy,'d':''} for m,yy in vs],'g':g}
    xs=k['x']; idx=max([i for i,x in enumerate(xs) if x.get('g')==g],default=len(xs)-1)+1
    k['x']=xs[:idx]+[e]+xs[idx:]; cadd+=1
kinds['Film SLR camera']['sel']=kinds['Film SLR camera']['sel'].replace('(for example Konica AR and Contax N)','(for example Contax N1, Fujica ST701, Petriflex and Praktina, whose Wikipedia pages did not load)')
note=" Mount coverage checked against every still-camera mount in Wikipedia's List of lens mounts: mounts with a fetched model page now have an entry; Contax N1 and NX, Fujica X, Kowa Six, Petriflex, Praktina, Visoflex, Alpa, Samsung Kenox and DJI DL have none because the page found for them did not load; Tamron adapter mounts and mounts used only by lenses have no body."
for kn in ['Film SLR camera','DSLR camera','Mirrorless camera','Film rangefinder camera','Medium-format SLR camera','Compact camera','Cartridge-film camera']:
    kinds[kn]['sel']+=note
json.dump(d,open('work/CMP_DEV/D4.tmp','w'),ensure_ascii=False,indent=1)
os.replace('work/CMP_DEV/D4.tmp','out/D4.json'); print(added,nv,cadd)
