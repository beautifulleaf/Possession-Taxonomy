import json,os,re
P='/home/user/Possession-Taxonomy/rebuild/out/D4.json'
d=json.load(open(P))
kinds={k['n']:k for dep in d['depts'] for sh in dep['s'] for k in sh['k']}
W='https://en.wikipedia.org/wiki/'
def N(n,mk,y,desc,s,vers,g,**kw):
    e={'n':n,'a':'','d':desc,'mk':mk,'y':y,'s':s,'v':[{'n':a,'mk':mk,'y':b,'d':c} for a,b,c in vers],'dt':'','g':g}
    e.update(kw); return e
r=kinds['Rugged compact camera']
if not r.get('x'):
    r['x']=[N('Olympus Tough','Olympus','2017','Olympus waterproof, shockproof compacts; the TG-6 is rated to 15 m and a 2.1 m drop, and the TG-7 carries the OM System name.',W+'Olympus_Tough_TG-6',[('TG-5','2017','May 2017'),('TG-6','2019','announced 22 May 2019'),('TG-7','2023','OM System; announced 13 September 2023')],'Olympus')]
    r['nl']='One entry is a rugged compact camera line sold under one name; successive bodies are versions.'
    r['xg']='by maker'
c=kinds['Compact camera']
if not any(x['n']=='Nikon Coolpix' for x in c['x']):
    c['x'].append(N('Nikon Coolpix','Nikon','2009','Nikon compact line in many variants; the S1000pj was the first compact with a built-in projector and the S800c the first with Android.',W+'Nikon_Coolpix_S1000pj',[('Coolpix S1000pj','2009','built-in projector'),('Coolpix P7000','2010','enthusiast compact with manual controls'),('Coolpix S800c','2012','first compact with Android')],'Nikon'))
FILMDIS="https://en.wikipedia.org/wiki/List_of_discontinued_photographic_films"
FILMCUR="https://en.wikipedia.org/wiki/List_of_photographic_films"
BODY=['Mirrorless camera','DSLR camera','Digital rangefinder camera','Digital back','Film SLR camera','Film rangefinder camera','Medium-format SLR camera','Medium-format rangefinder camera']
FILM=['Colour negative film','Black-and-white film','Slide film','Black-and-white reversal film','Infrared film','Cine colour negative film','Integral instant film','Peel-apart instant film']
n_done=0
for dep in d['depts']:
  for sh in dep['s']:
    for k in sh['k']:
      if not k.get('x'): continue
      sel=k.get('sel','') or ''
      sel=re.sub(r'\s*(Mount coverage checked|Tail of the discontinued list|Not included:|mounts in that list that this edition).*$','',sel,flags=re.S).strip()
      if k['n'] in FILM:
        base=("Every film of this type in Wikipedia's List of photographic films ("+FILMCUR+") and List of discontinued photographic films ("+FILMDIS+"), sections by maker. A series is one entry and its speeds, relaunches and renamed editions are versions. ")
        cov=("Complete: both lists were read to their end (the discontinued list ends with the Valca section) and every maker section that has a film of this type is entered at series level. "
             "Left out: the lists' bulleted Kodachrome and Ektachrome Lumiere notes, which repeat entered series, and films the lists give no type for.")
        if k['n'].startswith('Infrared'): cov=cov.replace('Left out:','Left out: Kodak Aerochrome codes beyond the Aerochrome entry (folded as versions);')
        k['sel']=base+cov
      elif k['n'] in BODY:
        k['sel']=("Model lines on the mounts and makers named in Wikipedia's List of lens mounts ("+W+"List_of_lens_mounts), grouped by mount, plus the model pages cited on each entry. "
                  "No complete list exists of camera bodies, so this follows that mount list and the pages cited. Left out: mounts used only by lenses or accessories (Visoflex, DJI DL), mounts whose body page did not load (Contax N1 and NX, Samsung Kenox film bodies), and Tamron adapter mounts.")
      elif k['n'] in('Prime lens','Zoom lens','Macro lens','Fisheye lens','Tilt-shift lens','Mirror lens','Anamorphic lens','Special-effect lens'):
        k['sel']="No complete list exists; follows the maker and lens-family pages cited on each entry. Lines are listed only where a fetched page names them; single lens models are not entries."
      elif k['n']=='Light meter':
        k['sel']="No complete list exists; follows the Weston, Gossen and Sekonic pages cited on each entry. Gossen's own site gives no historic models or years, so its versions carry none."
      else:
        k['sel']="No complete list exists; follows the manufacturer and Wikipedia pages cited on each entry, grouped by maker or mount. Lines are listed only where a fetched page names them."
      k['sel']=re.sub(r'\s+',' ',k['sel']).strip()
      n_done+=1
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P); print(n_done)
