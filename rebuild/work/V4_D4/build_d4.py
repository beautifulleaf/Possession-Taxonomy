import json,re,os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from films_data import R
ROOT='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open('/home/user/Possession-Taxonomy/rebuild/work/V4_D4/bak/D4.json'))
brands=json.load(open('/home/user/Possession-Taxonomy/rebuild/work/V4_D4/bak/D4_brands.json'))
LM='https://en.wikipedia.org/wiki/List_of_lens_mounts'
kinds={}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']: kinds[k['n']]=k
def yr(t):
    m=re.search(r'\d{4}',t or ''); return m.group(0) if m else ''
def status(y):
    y=y.strip()
    if y in('','?–?'): return ''
    if y=='avail': return 'listed as available'
    if y=='TBC': return 'date to be confirmed'
    if '–' in y:
        a,b=y.split('–',1)
        if b=='': return 'listed from '+a
        if a=='?': return 'made until '+b
        if b=='?': return 'made from '+a
        return 'made '+a+'–'+b
    return y
makers_extra={}
# ---------- camera systems
MOUNT={ # entry name -> section
 'Panasonic Lumix G / GH':'Micro Four Thirds','Olympus OM-D E-M5':'Micro Four Thirds','Olympus OM-D E-M1':'Micro Four Thirds',
 'Sony α7':'Sony E','Sony α1':'Sony E','Sony α6000':'Sony E',
 'Fujifilm X-Pro':'Fujifilm X','Fujifilm X-T':'Fujifilm X','Fujifilm X-E':'Fujifilm X','Fujifilm X-H':'Fujifilm X',
 'Canon EOS R full frame':'Canon RF','Canon EOS R APS-C':'Canon RF','Nikon Z full frame':'Nikon Z','Nikon Z DX':'Nikon Z',
 'Leica SL':'L-mount','Leica T / CL':'L-mount','Panasonic Lumix S':'L-mount','Fujifilm GFX':'Fujifilm G','Hasselblad X':'Hasselblad XCD',
 'Canon EOS-1D':'Canon EF','Canon EOS 5D':'Canon EF','Canon EOS Rebel (xxxD)':'Canon EF','Nikon D3':'Nikon F','Nikon D700 / D800 / D850':'Nikon F','Nikon D1':'Nikon F','Nikon D3000 series':'Nikon F',
 'Pentax K-1':'Pentax K','Pentax K-3':'Pentax K','Kodak DCS':'Nikon F and Canon EF (Kodak DCS)','Sony A-mount DSLR':'Sony A (Minolta A)',
 'Leica M digital':'Leica M','Leica M Monochrom':'Leica M','Epson R-D1':'Leica M','Pixii':'Leica M',
 'Kine Exakta':'Exakta','Asahiflex':'M37','Nikon F':'Nikon F','Nikon F2':'Nikon F','Nikon F3':'Nikon F','Nikon F4':'Nikon F','Nikon F5':'Nikon F','Nikon F6':'Nikon F','Nikon FM':'Nikon F','Nikkormat':'Nikon F',
 'Canon F-1':'Canon FD','Canon AE-1':'Canon FD','Canon A-1':'Canon FD','Canon EOS-1':'Canon EF','Olympus OM-1':'Olympus OM','Olympus OM-2':'Olympus OM',
 'Pentax Spotmatic':'M42','Pentax K1000':'Pentax K','Pentax MX':'Pentax K','Pentax LX':'Pentax K','Minolta SR-T':'Minolta SR','Minolta X-700':'Minolta SR','Minolta Maxxum 7000':'Minolta A (Minolta A)',
 'Contax RTS':'Contax/Yashica','Zenit':'M39 and M42','Praktica':'Praktica and M42','Leica R':'Leica R',
 'Leica screw-mount (Barnack)':'M39 (Leica thread)','Leica M':'Leica M','Zeiss Ikon Contax':'Contax RF','Argus C3':'Argus C3','Nikon S / SP':'Nikon S','Contax G':'Contax G',
 'Pentax 6×7 / 67':'Pentax 6x7','Mamiya RB67':'Mamiya RB67','Mamiya RZ67':'Mamiya RZ67','Bronica SQ':'Bronica SQA','Bronica ETR':'Bronica ETR','Pentax 645':'Pentax 645','Mamiya 645':'Mamiya 645','Rolleiflex SL66':'Rolleiflex SL66','Bronica GS-1':'Bronica GS1','Hasselblad V system':'Hasselblad','Mamiya 7':'Mamiya 7','Mamiya 6':'Mamiya 6','Bronica RF645':'Bronica RF','Hasselblad XPan':'Hasselblad Xpan',
}
MINOLTA={'Minolta Maxxum 7000':'Minolta A'}
BODY=['Mirrorless camera','DSLR camera','Digital rangefinder camera','Digital back','Film SLR camera','Film rangefinder camera','Medium-format SLR camera','Medium-format rangefinder camera']
for n in BODY:
    k=kinds[n]
    for x in k['x']:
        g=MOUNT.get(x['n'])
        if g=='Minolta A (Minolta A)': g='Minolta A'
        x['g']=g or x.get('mk') or 'Other makers'
def newx(n,mk,y,desc,src,vers,g,**kw):
    x={'n':n,'a':'','d':desc,'mk':mk,'y':y,'s':src,'v':[{'n':a,'mk':mk,'y':b,'d':c} for a,b,c in vers],'dt':'','g':g}
    x.update(kw); return x
mir=kinds['Mirrorless camera']; dsl=kinds['DSLR camera']
mir['x']+= [
 newx('Canon EOS M','Canon','2012','Canon APS-C mirrorless line on the EF-M mount, from the 2012 EOS M.','https://en.wikipedia.org/wiki/Canon_EOS_M',
   [('EOS M','2012',''),('EOS M2','2013',''),('EOS M3','',''),('EOS M10','2015',''),('EOS M5','',''),('EOS M6','',''),('EOS M100','2017',''),('EOS M6 Mark II','',''),('EOS M50','',''),('EOS M200','2019',''),('EOS M50 Mark II','','')],'Canon EF-M'),
 newx('Samsung NX','Samsung','2010','Samsung mirrorless line on the NX mount; the NX10 was the first model.','https://en.wikipedia.org/wiki/Samsung_NX_series',
   [(n,y,'') for n,y in [('NX10','2010'),('NX5','2010'),('NX100','2010'),('NX11','2010'),('NX200','2011'),('NX20','2012'),('NX210','2012'),('NX1000','2012'),('NX300','2013'),('NX1100','2013'),('NX2000','2013'),('Galaxy NX','2013'),('NX300M','2013'),('NX30','2014'),('NX mini','2014'),('NX3000','2014'),('NX1','2014'),('NX500','2015'),('NX3300','2015')]],'Samsung NX'),
 newx('Nikon 1','Nikon','2011','Nikon compact mirrorless system with a 1-inch sensor, sold 2011 to 2018.','https://en.wikipedia.org/wiki/Nikon_1',
   [(n,y,'') for n,y in [('V1','2011'),('J1','2011'),('J2','2012'),('V2','2012'),('J3','2013'),('S1','2013'),('AW1','2013'),('V3','2014'),('J4','2014'),('S2','2014'),('J5','2015')]],'Nikon 1'),
 newx('Pentax Q','Pentax','2011','Pentax ultra-compact mirrorless system with four bodies.','https://en.wikipedia.org/wiki/Pentax_Q',
   [('Pentax Q','2011',''),('Pentax Q10','',''),('Pentax Q7','',''),('Pentax Q-S1','','')],'Pentax Q'),
 newx('Sigma fp','Sigma','','Compact full-frame mirrorless body on the L-mount, from the Sigma fp line.','https://en.wikipedia.org/wiki/L-Mount',
   [('Sigma fp','',''),('Sigma fp L','',''),('Sigma BF','','')],'L-mount'),
]
mir['x'][-1]['y']=''
dsl['x']+= [
 newx('Olympus E-System','Olympus','2003','Olympus Four Thirds DSLR line; the E-1 was the first Four Thirds body.','https://en.wikipedia.org/wiki/Four_Thirds_system',
   [(n,y,'') for n,y in [('E-1','2003'),('E-300','2004'),('E-500','2005'),('E-330','2006'),('E-400','2006'),('E-410','2007'),('E-510','2007'),('E-3','2007'),('E-420','2008'),('E-520','2008'),('E-30','2008'),('E-620','2009'),('E-450','2009'),('E-600','2009'),('E-5','2010')]],'Four Thirds',role='origin'),
 newx('Panasonic Lumix L','Panasonic','2006','Panasonic Four Thirds DSLRs, the DMC-L1 and DMC-L10.','https://en.wikipedia.org/wiki/Four_Thirds_system',[('DMC-L1','2006',''),('DMC-L10','2007','')],'Four Thirds'),
 newx('Leica Digilux 3','Leica','2006','Leica Four Thirds DSLR of 2006.','https://en.wikipedia.org/wiki/Four_Thirds_system',[],'Four Thirds'),
]
# order
def ykey(x): 
    v=yr(x.get('y',''));return int(v) if v else 9999
for n in BODY:
    k=kinds[n]; first={}
    for x in k['x']: first[x['g']]=min(first.get(x['g'],9999),ykey(x))
    k['x'].sort(key=lambda x:(first[x['g']],x['g'],ykey(x),x['n']))
    k['xg']='by lens mount (Wikipedia list of lens mounts), or by maker where the body has no mount named there'
    k['nl']='One entry is a camera model line sold under one name on one lens mount, such as Nikon F or Sony α7; each body in the line is a version.'
    if n.startswith('Medium'): k['nl']='One entry is a medium-format camera system or model line sold under one name; bodies and generations are versions.'
    k['sel']=("Model lines on the mounts and makers named in Wikipedia's List of lens mounts ("+LM+"), grouped by mount. No single reference lists every body, so each line rests on the page cited on its entry; "
              "mounts in that list that this edition has not sourced yet (for example Konica AR and Contax N) have no entry.")
# ---- other camera kinds: g, nl, sel
OTHER={'Premium fixed-lens camera':'Fixed-lens cameras sold as a named model line, such as Ricoh GR or Fujifilm X100',
'Compact camera':'Compact fixed-lens cameras sold as a named line','Bridge camera':'Fixed-lens superzoom cameras sold as a named line'}
for n,t in OTHER.items():
    k=kinds[n]
    k['nl']='One entry is a fixed-lens camera model line sold under one name, such as Ricoh GR; successive bodies are versions.'
    k['sel']='Lines named by the maker or Wikipedia pages cited on each entry. No reference lists every fixed-lens camera, so the set is a selection of the best-known lines, grouped by maker.'
    k['xg']='by maker'
    for x in k['x']: x['g']=x.get('mk') or 'Other makers'
    k['x'].sort(key=lambda x:(x['g'],ykey(x),x['n']))
PROCS=['35 mm compact film camera','Half-frame camera','Subminiature camera','Cartridge-film camera','Twin-lens reflex camera','Box camera','Folding camera','View camera','Press camera','Integral instant camera','Peel-apart instant camera','Hybrid instant camera','Panoramic film camera','Toy camera','Pinhole camera','Single-use camera','Super 8 camera','Double 8 camera','16 mm cine camera','Camcorder','Pocket gimbal camera']
nlmap={'Integral instant camera':'One entry is an integral instant camera system (camera and film format), such as Polaroid SX-70 or instax mini; models are versions.',
'Peel-apart instant camera':'One entry is a peel-apart instant camera line, such as the Polaroid pack-film Land Camera; models are versions.',
'Hybrid instant camera':'One entry is an instant camera that also records digitally, sold as a named line; models are versions.',
'Camcorder':'One entry is a camcorder line sold under one name; successive models are versions.',
'Pocket gimbal camera':'One entry is a handheld gimbal camera line; generations are versions.'}
for n in PROCS:
    k=kinds[n]
    k['nl']=nlmap.get(n,'One entry is a named camera model line of this type; bodies and generations are versions.')
    k['sel']='Lines named by the Wikipedia or camera-wiki pages cited on each entry. No reference lists every camera of this type, so the set is a selection of the best-known lines, grouped by maker.'
    k['xg']='by maker'
    for x in k['x']: x['g']=x.get('mk') or 'Other makers'
    k['x'].sort(key=lambda x:(x['g'],ykey(x),x['n']))
# ---------- lenses
for n in ['Prime lens','Zoom lens','Macro lens','Fisheye lens','Tilt-shift lens','Mirror lens','Anamorphic lens','Special-effect lens']:
    k=kinds[n]
    k['nl']='One entry is a notable lens line or family from one maker, such as Zeiss Planar or Leica Summilux; generations and focal lengths are versions.'
    k['sel']='No whole-space reference lists lens lines; lines kept from the earlier pass, each resting on the page cited. Lines are listed per mount only where a fetched page lists them; single lens models are not entries.'
    k['xg']='by maker'
    for x in k['x']: x['g']=x.get('mk') or 'Maker not stated'
    k['x'].sort(key=lambda x:(x['g'],ykey(x),x['n']))
# ---------- films
KM={'CN':'Colour negative film','BW':'Black-and-white film','CR':'Slide film','BR':'Black-and-white reversal film','IR':'Infrared film','CINE':'Cine colour negative film','INT':'Integral instant film','PEEL':'Peel-apart instant film'}
TL={'CN':'Colour negative film','BW':'Black-and-white film','CR':'Colour slide film','BR':'Black-and-white reversal film','IR':'Infrared film','CINE':'Colour negative film for motion-picture cameras','INT':'Integral instant film','PEEL':'Peel-apart instant film'}
seen={k:{x['n'].lower() for x in kinds[v].get('x',[])} for k,v in KM.items()}
cnt={}
for src,kc,mk,name,yrs,vs in R:
    k=kinds[KM[kc]]
    if name.lower() in seen[kc]: continue
    seen[kc].add(name.lower())
    st=status(yrs)
    desc=f"{TL[kc]} from {mk}"+(f", {st}" if st else '')+'.'
    vers=[]
    for v in [t for t in vs.split(';') if t.strip()]:
        p=v.split('@'); vn=p[0].strip(); vy=p[1].strip() if len(p)>1 else ''; note=p[2].strip() if len(p)>2 else ''
        sv=status(vy) if vy else ''
        vers.append({'n':vn,'mk':mk,'y':yr(vy),'d':(note or sv)})
    x={'n':name,'a':'','d':desc,'mk':mk,'y':yr(yrs),'s':src,'v':vers,'dt':'','g':mk}
    k.setdefault('x',[]).append(x); cnt[kc]=cnt.get(kc,0)+1
for kc,kn in KM.items():
    k=kinds[kn]
    for x in k['x']: x.setdefault('g',x.get('mk') or 'Maker not stated')
    k['x'].sort(key=lambda x:(x['g'].lower(),ykey(x),x['n']))
    k['xg']='by maker'
    k['nl']='One entry is a named film stock or product line; speeds, relaunches and renamed editions are versions.'
    k['sel']=("Every film of this type in Wikipedia's List of photographic films ("+'https://en.wikipedia.org/wiki/List_of_photographic_films'+") and, for Kodak, Fujifilm, Ilford, Agfa, Konica, ORWO, Polaroid, Ferrania and a few smaller makers, discontinued lines from the List of discontinued photographic films ("+'https://en.wikipedia.org/wiki/List_of_discontinued_photographic_films'+"). "
      "Not included: other makers' discontinued films, repackaged and expired stocks sold by the Film Photography Project, and the last part of the discontinued list (after Valca), which was not read.")
# ---------- light meter etc keep
lm=kinds['Light meter']
lm['nl']='One entry is a light-meter line collected or sold under one name; models are versions.'
lm['sel']='Lines named by the pages cited on each entry. No reference lists every light meter, so the set is a selection of the best-known lines, grouped by maker.'
lm['xg']='by maker'
for x in lm['x']: x['g']=x.get('mk') or 'Other makers'
# ---------- commodity: remove x from tripod/stabilisers
for n in ['Flexible and table-top tripod','Mechanical stabiliser']:
    k=kinds[n]
    for x in k.get('x',[]):
        makers_extra[x.get('mk') or x['n'].split()[0]]=x.get('s','')
    k['x']=[]
# ---------- m/r handling
REG=set()
for kn,k in kinds.items():
    for key in('m','r'):
        for t in k.get(key,[]) or []:
            if t[1]: makers_extra.setdefault(t[1],k.get('s',''))
    k['m']=[]; k['r']=[]
    if not k.get('x'):
        k.pop('x',None)
    # see: a FOUR THIRDS note
# ---------- Four thirds former models: now versions (Digilux 3, L1, E-300) -- covered above
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            if 'x' in k and not k['x']: k.pop('x')
# ---------- brand register
have={b['n'].lower() for b in brands['b']}
def addb(n,src=''):
    if n.lower() in have or not n.strip(): return
    have.add(n.lower()); b={'n':n}
    if src: b['s']=src
    brands['b'].append(b)
for n,s in makers_extra.items(): addb(n,s)
for kn,k in kinds.items():
    for x in k.get('x',[]):
        if x.get('mk'): addb(x['mk'],x.get('s',''))
        for v in x.get('v',[]):
            if v.get('mk'): addb(v['mk'],x.get('s',''))
brands['b'].sort(key=lambda b:b['n'].lower())

U='https://petapixel.com/2025/08/29/canon-had-the-top-camera-market-share-in-2024/'
note='Share of digital cameras sold by Japanese Nikkei 225 makers, in units; Leica, Hasselblad and Sigma are not covered'
dp=[x for x in d['depts'] if x['n']=='Digital cameras'][0]
dp['ms']=[{'mkt':'Global digital cameras (Nikkei 225 makers)','who':w,'share':sh,'yr':2024,'s':U,'note':note+'; '+u+' units'} for w,sh,u in [('Canon','43.2 %','3.53 million'),('Sony','28.5 %','2.33 million'),('Nikon','11.7 %','960,000'),('Fujifilm','9 %','740,000'),('Panasonic','3.4 %','280,000'),('OM Digital Solutions','1.9 %','160,000'),('Ricoh Imaging','0.8 %','70,000')]]
json.dump(d,open(ROOT+'D4.json.tmp','w'),ensure_ascii=False,indent=1)
json.dump(brands,open(ROOT+'D4_brands.json.tmp','w'),ensure_ascii=False,indent=1)
os.replace(ROOT+'D4.json.tmp',ROOT+'D4.json'); os.replace(ROOT+'D4_brands.json.tmp',ROOT+'D4_brands.json')
print(cnt, len(brands['b']))
