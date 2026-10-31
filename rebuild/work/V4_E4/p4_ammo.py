import re
HC=WP+'List_of_handgun_cartridges';RC=WP+'List_of_rifle_cartridges';GA=WP+'Gauge_(firearms)'
def bore(n):
    m=re.match(r'^\.(\d+)',n)
    if m:
        v=int(m.group(1)); 
        v=v/1000 if v>=100 else v/100
        return v*25.4
    m=re.match(r'^(\d+(?:\.\d+)?)\s*[×x ]?\s*mm|^(\d+(?:\.\d+)?)mm|^(\d+(?:\.\d+)?)[×x]',n)
    if m:
        for q in m.groups():
            if q: return float(q)
    return None
def grp(n):
    b=bore(n)
    if b is None: return 'Other'
    if b<6.0: return 'Up to 6 mm (.22 class)'
    if b<7.0: return '6 to 6.9 mm (.25–.27 class)'
    if b<8.0: return '7 to 7.9 mm (.28–.31 class)'
    if b<9.0: return '8 to 8.9 mm (.32–.35 class)'
    if b<10.0: return '9 to 9.9 mm (.35–.38 class)'
    if b<11.0: return '10 to 10.9 mm (.40–.42 class)'
    if b<12.0: return '11 to 11.9 mm (.43–.45 class)'
    return '12 mm and over (.46 class and larger)'
def ent(names,src,kind,known):
    out=[]
    for n in names:
        n=n.strip()
        if not n: continue
        dd=known.get(n,kind)
        out.append(e(n,dd,'',g=grp(n),s=src))
    return out
HG="""4.6×30mm HK|.17 Hornady Magnum Rimfire|.22 Long Rifle|.22 Short|.22 WMR|5.7×28mm FN|.25 ACP|.30 Super Carry|.32 ACP|.32 H&R Magnum|.32 S&W Long|.32-20 Winchester|.327 Federal Magnum|7.62mm Tokarev|7.63mm Mauser|7.65 mm Parabellum|7.5 mm Swiss Army|7.62mm Nagant|8 mm Nambu|.380 ACP|9mm Largo|9mm Makarov|9×25mm Mauser|9×23mm Winchester|.38 Special|.38 Super|.38 S&W|.38 Long Colt|.357 Magnum|.357 SIG|.38-40 Winchester|.40 S&W|10mm Auto|.41 Magnum|.41 Long Colt|.44 Special|.44 Magnum|.44 Russian|.44-40 Winchester|.44 S&W American|.45 ACP|.45 GAP|.45 Colt|.45 Schofield|.45 Winchester Magnum|.455 Webley|.454 Casull|.460 S&W Magnum|.480 Ruger|.475 Linebaugh|.50 Action Express|.500 S&W Special|.500 S&W Magnum""".split('|')
known={'9mm Parabellum':'Rimless straight-walled pistol round introduced in 1902; the commonest handgun cartridge worldwide.','.45 ACP':'Rimless pistol round designed for the M1911 pistol.','.38 Special':'Revolver round of 1898, the .357 Magnum\'s parent.','.357 Magnum':'Longer, stronger version of the .38 Special for revolvers.','.22 Long Rifle':'Rimfire round used in rifles and pistols for small game and target shooting.','.44 Magnum':'Long, high-pressure revolver round of the 1950s.','.380 ACP':'Short pocket-pistol round, also called 9mm Short.','10mm Auto':'Rimless round of the 1980s with a long case for powerful pistols.','.40 S&W':'Rimless pistol round introduced in 1990.'}
HG_DESC='Handgun cartridge.'
add('Centrefire handgun cartridge',ent(HG,HC,HG_DESC,known),"One entry is a handgun cartridge by its common name; loads and bullet weights are versions.","Handgun cartridges of Wikipedia's List of handgun cartridges, cut to those in current sporting or collector use; wildcat, experimental and military-only rounds of the list are left out.",'by bore size')
RF="""4 mm Flobert Short|4 mm Flobert Long|9mm Flobert|.17 Hornady Magnum Rimfire|.17 Hornady Mach 2|.17 Winchester Super Magnum|.22 BB Cap|.22 CB Cap|.22 Short|.22 Long|.22 Long Rifle|.22 Extra Long|.22 Winchester Magnum Rimfire|.22 Winchester Rimfire|.22 Winchester Automatic|.22 Remington Automatic|5 mm Remington Rimfire Magnum|.25 Stevens|.32 rimfire|.38 rimfire|.41 rimfire|.44 Henry|.46 rimfire|.50 Remington Navy|.56-56 Spencer""".split('|')
add('Rimfire cartridge',ent(RF,RC,'Rimfire cartridge.',{'.22 Long Rifle':'The standard rimfire round, in use since 1887.','.22 Winchester Magnum Rimfire':'Longer, more powerful rimfire round than the .22 Long Rifle.'}),"One entry is a rimfire cartridge by its common name; loads are versions.","Rimfire cartridges of Wikipedia's List of rifle cartridges; handgun-only rimfires are under Centrefire handgun cartridge's list.")
for x in KIND['Rimfire cartridge']['x']:
    x['g']='Modern rimfire' if any(t in x['n'] for t in ('Magnum','Mach 2','.22 LR','Long Rifle','Short','Long','CB','BB','Extra','Flobert','Super','5 mm','Automatic','Winchester Rimfire')) else 'Historical rimfire'
KIND['Rimfire cartridge']['xg']='by era'
RFL="""5.56×45mm NATO|.17 Remington|.204 Ruger|.22 Hornet|.22-250 Remington|.220 Swift|.222 Remington|.223 Remington|.224 Valkyrie|.22 ARC|.22 Creedmoor|.218 Bee|.219 Zipper|.243 Winchester|.25-20 Winchester|.25-06 Remington|.250 Savage|.257 Roberts|.260 Remington|.264 Winchester Magnum|.270 Winchester|.270 Winchester Short Magnum|.280 Remington|.284 Winchester|.30 Carbine|.30-30 Winchester|.30-40 Krag|.30-06 Springfield|.300 AAC Blackout|.300 H&H Magnum|.300 Winchester Magnum|.300 Winchester Short Magnum|.300 Weatherby Magnum|.300 PRC|.300 Savage|.300 Norma Magnum|.300 Ruger Compact Magnum|.300 Remington Ultra Magnum|.303 British|.308 Winchester|.308 Norma Magnum|.32 Winchester Special|.325 Winchester Short Magnum|.338 Federal|.338 Lapua Magnum|.338 Winchester Magnum|.338 Norma Magnum|.338-06|.340 Weatherby Magnum|.348 Winchester|.35 Remington|.35 Whelen|.350 Legend|.358 Winchester|.375 H&H Magnum|.375 Ruger|.378 Weatherby Magnum|.404 Jeffery|.416 Rigby|.416 Remington Magnum|.444 Marlin|.45-70|.45-90 Sharps|.450 Bushmaster|.450 Marlin|.458 Winchester Magnum|.458 Lott|.460 Weatherby Magnum|.470 Nitro Express|.50 BMG|.50 Beowulf|.50-70 Government|.577 Snider|.577/450 Martini–Henry|.38-55 Winchester|5.45×39mm|6mm Creedmoor|6mm Remington|6mm ARC|6mm PPC|6.5mm Creedmoor|6.5 PRC|6.5×55mm Swedish|6.5mm Grendel|6.5×52mm Carcano|6.5×50mm Arisaka|6.8 Western|6.8mm Remington SPC|7mm-08 Remington|7mm Remington Magnum|7mm PRC|7mm Weatherby Magnum|7×57mm Mauser|7×64mm Brenneke|7.5×55mm Swiss|7.62×39mm|7.62×51mm NATO|7.62×54mmR|7.7×58mm Arisaka|7.92×57mm Mauser|8×57mm IS|8×50mmR Mannlicher|8mm Lebel|8mm Remington Magnum|9.3×62mm|9.3×74mmR|9.3×57mm|11×59mmR Gras""".split('|')
known2={'.223 Remington':'Small rifle round of 1964 from which the 5.56×45mm NATO military round was derived.','5.56×45mm NATO':'Military rifle round standardised by NATO from the .223 Remington.','.308 Winchester':'Short-action rifle round of 1952; the civilian form of 7.62×51mm NATO.','7.62×51mm NATO':'Military rifle round of the 1950s, the model for the .308 Winchester.','.30-06 Springfield':'US service rifle round adopted in 1906 and a hunting standard.','6.5mm Creedmoor':'Target and hunting rifle round introduced in 2007.','.270 Winchester':'Hunting rifle round of 1925.','.303 British':'British service rifle round, in use from 1889.','7.62×39mm':'Intermediate rifle round of the Soviet SKS and AK rifles.','.50 BMG':'Large machine-gun round also used in long-range target rifles.','.45-70':'Black-powder-era US service round, still loaded for lever-action rifles.'}
add('Centrefire rifle cartridge',ent(RFL,RC,'Rifle cartridge.',known2),"One entry is a rifle cartridge by its common name; loads and bullet weights are versions.","Rifle cartridges of Wikipedia's List of rifle cartridges, cut to those in current sporting, target or collector use; wildcat, experimental, artillery and machine-gun-only rounds of the list are left out.",'by bore size')
KIND['Centrefire rifle cartridge']['xg']='by bore size'; KIND['Centrefire handgun cartridge']['xg']='by bore size'
# Shotshell gauges
SG=[('4 gauge','1.052 in (26.7 mm)'),('8 gauge','0.835 in (21.2 mm)'),('10 gauge','0.775 in (19.7 mm)'),('11 gauge','0.751 in (19.1 mm)'),('12 gauge','0.729 in (18.5 mm)'),('14 gauge','0.693 in (17.6 mm)'),('16 gauge','0.662 in (16.8 mm)'),('18 gauge','0.637 in (16.2 mm)'),('20 gauge','0.615 in (15.6 mm)'),('24 gauge','0.579 in (14.7 mm)'),('28 gauge','0.550 in (14.0 mm)'),('32 gauge','0.526 in (13.4 mm)'),('.410 bore','')]
add('Shotshell',[e(n,('Shotgun gauge with a bore of %s.'%b) if b else 'Smallest common shotgun bore, measured in inches.','',g=('Large bores (4 to 11 gauge)' if n.split()[0] in('4','8','10','11') else 'Common bores (12 to 20 gauge)' if n.split()[0] in('12','14','16','18','20') else 'Small bores (24 gauge and smaller)'),s=GA) for n,b in SG],"One entry is a shotgun gauge or bore size; shell lengths and loads are versions.","The numbered gauges from 4 to 32 and the .410 bore on Wikipedia's Gauge (firearms) page; the page tabulates gauges to 50 from the Proof Act, which are left out as obsolete.",'by bore group')
dropm('Shotshell','Gauges became entries')
for kn in ('Rimfire cartridge','Centrefire handgun cartridge','Centrefire rifle cartridge'):
    KIND[kn].pop('m',None)
REMOVED.append(('Rimfire cartridge / Centrefire handgun cartridge / Centrefire rifle cartridge',['.22 WMR','.17 HMR','.380 ACP','.40 S&W','10mm Auto','.270 Winchester','.300 Winchester Magnum','.300 AAC Blackout'],'Became entries'))

KIND['Centrefire handgun cartridge']['x'][[x['n'] for x in KIND['Centrefire handgun cartridge']['x']].index('9mm Luger')]['a']='9mm Parabellum · 9×19mm'
for kn in ('Centrefire handgun cartridge','Centrefire rifle cartridge','Rimfire cartridge'):
    for x in KIND[kn]['x']:
        if not x.get('g'): x['g']=grp(x['n'])
