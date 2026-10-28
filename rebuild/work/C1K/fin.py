import json,shutil,os
R='/home/user/Possession-Taxonomy/rebuild/out/'
W='/home/user/Possession-Taxonomy/rebuild/work/C1K/'
def wr(p,o):
    json.dump(o,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
shutil.copy(W+'C1.new.json',R+'C1.json.tmp'); os.replace(R+'C1.json.tmp',R+'C1.json')
b=json.load(open(W+'bak/C1_brands.json'))
have={x['n'].lower() for x in b['b']}
def B(n,c,f,seg,kf,d,s,sig=()): return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"lines":[],"eras":[],"sig":list(sig),"sc":[],"rel":[],"s":s}
new=[B("ESEE","","","Specialist","bushcraft fixed blades","Knife maker that grew from Randall's Adventure & Training survival school, known for numbered 1095 fixed blades.","https://bladereviews.com/esee-4-review/",["ESEE-4"]),
 B("Ka-Bar","United States","","Heritage manufactory","fixed blades","Fixed-blade maker whose Becker line, designed by Ethan Becker, includes the BK2 Companion.","https://www.messerworld.de/en/ka-bar/becker-companion-bk2.html",["Ka-Bar Becker BK2 Companion"]),
 B("Fisher Space Pen","United States","","Specialist","pressurised pens","Maker of pressurised-cartridge pens developed by Paul C. Fisher, patented 1965.","https://en.wikipedia.org/wiki/Fisher_Space_Pen",["Fisher Bullet Space Pen"]),
 B("Tuff-Writer","United States","","Specialist","tactical pens","Maker of machined aluminium tactical pens with pressurised cartridges.","https://soldiersystems.net/2008/10/08/tuff-writer-tactical-pens/",["Tuff-Writer Frontline"]),
 B("Nite Ize","","","Mainstream","keyring tools","Maker of keyring accessories including the DoohicKey tool.","https://hiconsumption.com/best-keychain-multi-tools/",["Nite Ize DoohicKey"])]
for x in new:
    assert x['n'].lower() not in have
    b['b'].append(x)
wr(R+'C1_brands.json',b)
t=json.load(open(W+'bak/C1_traditions.json'))
def T(n,r,p,d,tech,mat,forms,ctr,auth,s): return {"n":n,"g":"Metal & blades","r":r,"p":p,"d":d,"tech":tech,"mat":mat,"forms":forms,"ctr":ctr,"auth":auth,"s":s}
t['t']+= [
 T("Laguiole knife","Laguiole village and Thiers, France","1829–present","Slim French slip-joint pocket knife with a tapered blade and ornamented backspring.","slip-joint assembly, forged or stamped blade","cattle horn, wood, aluminium; stainless or carbon steel (XC75, XC100)",["Laguiole"],["Laguiole (Forge de Laguiole)","Thiers"],"'Laguiole' is a generic name, not a protected one; French makers often stamp their mark and steel type on the blade.","https://en.wikipedia.org/wiki/Laguiole_knife"),
 T("Opinel and Savoie knives","Savoie, France","1890–present","Savoie folding knives made by Opinel in numbered sizes, with the Virobloc collar from 1955.","turning-collar lock, XC90 or 12C27M blade","beech and other woods; carbon or stainless steel",["Opinel No. 8"],["Opinel, Savoie"],"numbered blade size and Opinel logo stamped on the blade.","https://en.wikipedia.org/wiki/Opinel_knife"),
 T("Sheffield cutlery","Sheffield, England","1297 record; Cutlers' Company 17th century–present","England's principal cutlery centre, source of crucible steel (1740s) and stainless steel (1912).","grinding on water-powered stones; crucible steel","steel, horn, bone",["Barlow knife"],["Sheffield","Company of Cutlers in Hallamshire"],"","https://en.wikipedia.org/wiki/Sheffield"),
 T("Solingen cutlery","Solingen, Germany","medieval–present","German cutlery centre known for swords, knives, scissors and razors; home to Zwilling J. A. Henckels and Böker.","","steel",[],["Solingen"],"","https://en.wikipedia.org/wiki/Solingen")]
wr(R+'C1_traditions.json',t)
