import json,re,os
P='/home/user/Possession-Taxonomy/rebuild/out/E4.json'
d=json.load(open(P))
K={}
for dep in d['depts']:
  for sh in dep['s']:
    for k in sh['k']: K[k['n']]=k
def ent(n,desc,url,g=None,mk='',y=''):
  e={"n":n,"a":"","d":desc,"mk":mk,"y":y,"s":url,"v":[]}
  if g: e["g"]=g
  return e
def add(kn,es):
  k=K[kn]; have={re.sub(r'\W','',e['n'].lower()) for e in k['x']}
  c=0
  for e in es:
    if re.sub(r'\W','',e['n'].lower()) not in have: k['x'].append(e); c+=1
  return c
LS='https://en.wikipedia.org/wiki/List_of_shotguns'
LP='https://en.wikipedia.org/wiki/List_of_semi-automatic_pistols'
LA='https://en.wikipedia.org/wiki/List_of_armour_types'
pd=lambda n,g,mk='':ent(n,"Semi-automatic pistol listed in Wikipedia's List of semi-automatic pistols.",LP,g,mk)
cnt={}
cnt['pist']=add('Semi-automatic pistol',[pd("Erika Pistol","Early pistols"),pd("Raven MP-25","Late 20th century","Raven Arms"),pd("Ruger Security-9","21st century","Ruger"),pd("Type 70","Late 20th century"),pd("Type 80 (pistol)","Late 20th century"),pd("Type 64 (silenced pistol)","Mid century"),pd("Type 67 (silenced pistol)","Mid century"),pd("Claridge Hi-Tec/Goncz Pistol","Late 20th century")])
sd=lambda n,g,a,mk='':ent(n,a,LS,g,mk)
cnt['pump']=add('Pump-action shotgun',[sd("Remington Model 870","Remington","Pump-action shotgun listed in Wikipedia's List of shotguns.","Remington"),sd("Stevens Model 520/620","Stevens","Pump-action shotgun listed in Wikipedia's List of shotguns.","Stevens"),sd("Norinco HP9-1","Norinco","Pump-action shotgun listed in Wikipedia's List of shotguns.","Norinco"),sd("MAG-7","MAG-7","Pump-action shotgun listed in Wikipedia's List of shotguns."),sd("NeoStead 2000","NeoStead","Pump-action shotgun listed in Wikipedia's List of shotguns.")])
sa="Semi-automatic shotgun listed in Wikipedia's List of shotguns."
cnt['semi']=add('Semi-automatic shotgun',[sd("Atchisson Assault Shotgun","Atchisson",sa),sd("AAI CAWS","AAI",sa),sd("Daewoo Precision Industries USAS-12","Daewoo",sa),sd("Heckler & Koch CAWS","Heckler & Koch",sa),sd("Franchi SPAS-12","Franchi","Dual-mode shotgun that works as a pump-action or a semi-automatic, listed in Wikipedia's List of shotguns."),sd("Franchi SPAS-15","Franchi","Dual-mode shotgun that works as a pump-action or a semi-automatic, listed in Wikipedia's List of shotguns."),sd("Fabarm SDASS Tactical","Fabarm",sa),sd("Pancor Jackhammer","Pancor",sa)])
cg="Combination gun listed in Wikipedia's List of shotguns."
cnt['comb']=add('Combination gun',[ent(n,cg,LS) for n in ["Marble Game Getter","M6 aircrew survival weapon","Chiappa M6 survival gun","TP-82","Chiappa Double Badger"]])
pc=lambda n,dsc,g:ent(n,dsc,LA,g)
cnt['plate']=add('Plate carrier',[pc("HRM tactical vest","Armour system listed in Wikipedia's List of armour types.","Twenty-first century"),pc("FSBE AAV QR","Armour system listed in Wikipedia's List of armour types.","Twenty-first century"),pc("SPCS","Armour system listed in Wikipedia's List of armour types.","Twenty-first century"),pc("SPC","Armour system listed in Wikipedia's List of armour types.","Twenty-first century"),pc("MSV","Armour system listed in Wikipedia's List of armour types.","Twenty-first century"),pc("PRU-70","Armour system listed in Wikipedia's List of armour types.","Late twentieth century")])
h="Combat helmet listed in Wikipedia's List of armour types."
old=["CG634","M92","GOLFO","M90 (Iraq)","JK 96","M59/85","M87","Hełm wz. 93","Hełm wz. 2000","Sfera","SPECTRA","6B7"]
new=["A2 Helmet","BK-3 helmet","QGF-03","ECH (Australia)","ECH (US)","6B47","Hełm wz. 2005","Hełm HBT-02","Hełm HP-05","IHPS","Kaska-1M","KH-B2000","Kolpak-20","Mk 7"]
cnt['helm']=add('Ballistic helmet',[pc(n,h,"Late twentieth century") for n in old]+[pc(n,h,"Twenty-first century") for n in new])
# coverage lines
def tot(kn): return len(K[kn]['x'])
def setcov(kn,txt):
  k=K[kn]; s=k['sel'].rstrip()
  s=re.sub(r'\s*(Complete|Covers)[^.]*(\.[^.]*)?$','',s) if False else s
  k['sel']=s+(' ' if not s.endswith(' ') else '')+txt
# strip old "Covers ..." sentences for partial kinds first
for kn in ['Semi-automatic pistol','Single-shot shotgun','Side-by-side shotgun','Over-under shotgun','Pump-action shotgun','Semi-automatic shotgun']:
  K[kn]['sel']=re.sub(r'\s*Covers \d+ entries from that reference;.*$','',K[kn]['sel'])
n=tot('Semi-automatic pistol')
setcov('Semi-automatic pistol',f"Complete: {n} entries for the page's rows, read in full in five windows (about 590 names); rows that are range or slash rows (for example Walther PP / PPK, Beretta 92G-SD/96G-SD, DHP9 and DSP9 sets) are one entry or left to their parent, and the Colt M1911 row is the M1911 entry.")
shot="Covers {n} of the page's about 270 shotgun rows; the page gives no action column, so only rows whose action is known without guessing are placed here. The rest are bolt-action, lever-action, revolving, military or unplaced rows, listed in the GAP_E4 report."
for kn in ['Single-shot shotgun','Side-by-side shotgun','Over-under shotgun','Pump-action shotgun','Semi-automatic shotgun']:
  K[kn]['sel']=K[kn]['sel'].replace('military, combination-gun and revolving shotguns are left out','combination-gun and revolving shotguns are left out; tactical and military pump and semi-automatic shotguns are now included')
  setcov(kn,shot.format(n=tot(kn)))
setcov('Plate carrier',f"Covers {tot('Plate carrier')} of the 18 rows of the armour-systems section of Wikipedia's List of armour types (read in full, 103,004 characters); the Kelly gang armour, Brewster Body Shield and Steel Bib rows are historic one-off armours, not carriers, and are left out.")
setcov('Ballistic helmet',f"Complete: {tot('Ballistic helmet')} of 31 rows in the two combat-helmet sections (1980-2000 and 2001 onward) of that page, counting the PASGT and FAST rows already here.")
# generic coverage line for kinds with entries lacking one
for dep in d['depts']:
  for sh in dep['s']:
    for k in sh['k']:
      if k.get('x') and not re.search(r'Complete:|Covers \d|No complete list exists',k['sel']):
        k['sel']=k['sel'].rstrip()+" No complete list exists; follows the overviews named above."
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1)
os.replace(P+'.tmp',P)
print(cnt)
