import json,os
W='https://en.wikipedia.org/wiki/'
d=json.load(open('out/E4.json'))
def find(n):
    for dp in d['depts']:
        for s in dp['s']:
            for i,k in enumerate(s['k']):
                if k['n']==n: return dp,s,i,k
    raise KeyError(n)
def A(n,a,dd,mk,y,s,v=None,dt=None):
    r={"n":n,"a":a,"d":dd,"mk":mk,"y":y,"s":s,"v":v or []}
    if dt: r["dt"]=dt
    return r
def V(n,mk="",y="",dd=""): return {"n":n,"mk":mk,"y":y,"d":dd}
# E4-2
find('Bolt-action rifle')[3]['x'].insert(1,A("Springfield M1903","'03 Springfield","US .30-calibre bolt-action service rifle adopted in 1903, based on Mauser designs.","Springfield Armory","1903",W+"M1903_Springfield",[V("M1903A1","Springfield Armory","1929–1939","pistol-grip stock"),V("M1903A3","","1942–1944","receiver aperture sight, stamped parts"),V("M1903A4","","1942","sniper version")],".30-03 or .30-06 · maker (Springfield, Rock Island, Remington, Smith Corona)"))
find('Single-action revolver')[3]['x'].insert(1,A("Colt 1851 Navy","Navy Colt","Samuel Colt's .36 percussion revolver, made 1851–1873.","Colt","1851",W+"Colt_1851_Navy_Revolver",[V("Thuer conversion","Colt","","first Colt metallic-cartridge revolver"),V("Richards-Mason conversion","Colt","after 1869",".38 rimfire or centrefire")],".36 (rarely .34) · squareback or round trigger guard"))
x=find('Double-action revolver')[3]['x']
x.insert(1,A("Webley revolver","Webley Mk VI","British break-top service revolver in .455, in service 1887–1963.","Webley & Scott","1887",W+"Webley_Revolver",[V("Mk I","Webley & Scott","1887"),V("Mk II","","1895"),V("Mk IV","","1899","Boer War model"),V("Mk V","","1913"),V("Mk VI","","1915","best-known model, 6-inch barrel")],".455 Webley · .38/200 on later marks"))
x.insert(2,A("Nagant M1895","Nagant revolver","Russian 7.62×38mmR gas-seal revolver designed by Léon Nagant, adopted 1895.","","1895",W+"Nagant_M1895",[V("Officer's model","","","double-action"),V("Private's model","","","single-action"),V("TOZ-36","","1962","civilian"),V("Swedish M1887","","","7.5 mm")],"7.62×38mmR · military or civilian"))
find('Semi-automatic rifle')[3]['x'].append(A("AK-pattern rifle","Kalashnikov rifle","Mikhail Kalashnikov's 7.62×39 mm rifle family, adopted by the Soviet Army in 1949.","","1949",W+"AK-47",[V("AK-47 Type 1","","1948","stamped receiver"),V("AK-47 Type 2","","1951","milled receiver"),V("AK-47 Type 3","","1954","lightened milled receiver"),V("AKM","","1959","stamped receiver"),V("AK-74","","1974","5.45×39 mm"),V("Type 56","Norinco","","Chinese copy")],"calibre · receiver type · furniture"))
# E4-6 musket
dp,s,i,k=find('Muzzle-loading shotgun')
bb=k['x'].pop(0); k['a']='fowler'
_,rs,ri,_=find('Muzzle-loading rifle')
rs['k'].insert(ri+1,{"n":"Musket","a":"flintlock musket · Brown Bess","d":"Smoothbore muzzle-loading military long gun, fired by matchlock, flintlock or percussion lock.","t":["matchlock","flintlock","percussion"],"s":bb['s'],"x":[bb]})
# crossbow
dp,s,i,k=find('Recurve crossbow')
s['k'].insert(i,{"n":"Historical crossbow","a":"medieval crossbow","d":"Crossbow of the medieval and later periods, drawn by hand, windlass or cranequin.","t":["hand-spanned","windlass","cranequin"],"s":W+"Crossbow","x":[A("Arbalest","","Heavy European crossbow, 12th century on; later steel-prod crossbows needing windlass or cranequin.","","12th century",W+"Crossbow",[V("Windlass-spanned","","13th century"),V("Cranequin-spanned","","14th century")])]})
# E4-3 cartridges
def cart(kn,items):
    k=find(kn)[3]; k['x']=[]
    for n,a,dd,mk,y,src in items:
        k['x'].append(A(n,a,dd,mk,y,W+src))
        k['m']=[m for m in k['m'] if m[0]!=n]
cart('Centrefire handgun cartridge',[
 ("9mm Luger","9×19mm Parabellum","Rimless 9 mm pistol cartridge designed by Georg Luger.","","1901","9%C3%9719mm_Parabellum"),
 (".45 ACP","","John Moses Browning's .45 self-loading pistol cartridge.","","1904",".45_ACP"),
 (".38 Special","","Revolver cartridge designed by Smith & Wesson.","Smith & Wesson","1898",".38_Special"),
 (".357 Magnum","","Revolver cartridge by Elmer Keith, Phillip Sharpe and Douglas Wesson.","","1934",".357_Magnum"),
 (".44 Magnum","","Revolver cartridge developed by Elmer Keith and Smith & Wesson; production from 1956.","","1950s",".44_Magnum")])
cart('Centrefire rifle cartridge',[
 (".30-06 Springfield","7.62×63mm","US service rifle cartridge designed by Springfield Armory.","Springfield Armory","1906",".30-06_Springfield"),
 (".308 Winchester","7.62×51mm NATO","Short-action rifle cartridge branded by Winchester, from Frankford Arsenal T65 experiments.","Winchester","1952",".308_Winchester"),
 (".223 Remington","","Rifle cartridge developed by Remington with Fairchild Industries.","Remington","1957",".223_Remington"),
 ("5.56x45mm NATO","5.56×45mm","Rifle cartridge developed by FN Herstal and standardised in 1980.","FN Herstal","1980","5.56%C3%9745mm_NATO"),
 ("6.5 Creedmoor","","Rifle cartridge designed by Dave Emary of Hornady with Dennis DeMille.","Hornady","2007","6.5mm_Creedmoor")])
cart('Rimfire cartridge',[(".22 Long Rifle",".22 LR","Rimfire cartridge by J. Stevens Arms & Tool Company.","","1887",".22_Long_Rifle")])
# E4-4 merges
def remove(n):
    dp,s,i,k=find(n); s['k'].pop(i); return s,i,k
s,i,_=remove('Barrel')
for n in ('Trigger','Suppressor','Iron sight'): remove(n)
s['k'].insert(i,{"n":"Firearm upgrade part","a":"barrel · trigger · iron sight · suppressor","d":"Replacement or upgrade part made to fit a firearm model or platform.","t":["barrel","trigger","front sight","rear sight","suppressor"],"s":"https://www.basspro.com/l/guns"})
s,i,t=remove('Taser-type stun gun'); _,_,_,c=find('Contact stun gun'); 
c['n']='Stun gun'; c['a']='Taser-type · electroshock weapon · TASER'; c['d']='Device that delivers an incapacitating electric shock, by wired darts (Taser-type) or by contact electrodes.'; c['t']=['projectile (Taser-type)','contact']; c['m']=t['m']+c['m']; c['s']=t['s']
s,i,sv=remove('Soft ballistic vest')
_,_,_,hp=find('Hard ballistic plate'); _,_,_,sr=find('Stab-resistant vest'); pc=find('Plate carrier')[3]
for n in ('Hard ballistic plate','Stab-resistant vest','Plate carrier'): remove(n)
s['k'].insert(i,{"n":"Body armour","a":"ballistic vest · bulletproof vest · plate carrier","d":"Worn protection against bullets or blades: soft vest, hard plate or plate carrier.","t":["soft ballistic vest (NIJ IIA, II, IIIA)","hard plate (NIJ III, IV; steel, ceramic, polyethylene)","plate carrier","stab-resistant vest"],"s":sv['s'],"m":sv['m']+hp['m']+sr['m']})
# E4-6 tosogu
dp,s,i,k=find('Sword guard'); sh=[x for x in dp['s'] if x['n']=='Sword fittings & mounts'][0]
ren={'Hilt collar and pommel cap':('Fuchi-kashira','hilt collar and pommel cap'),'Sword grip ornament':('Menuki','sword grip ornament'),'Scabbard pocket fitting':('Kozuka and kōgai','scabbard pocket fitting · kozuka · kogai')}
tos=[]
for old,(new,al) in ren.items():
    kk=find(old)[3]; kk['n']=new; kk['a']=al; tos.append(kk); sh['k']=[x for x in sh['k'] if x is not kk]
hb=[x for x in sh['k'] if x['n']=='Habaki'][0]; sh['k'].remove(hb); tos.append(hb)
idx=dp['s'].index(sh)
dp['s'].insert(idx+1,{"n":"Japanese sword fittings (tosogu)","k":tos})
# E4-7
nv=find('Night-vision and thermal sight')[3]; nv['d']+=' Handheld viewers: see Observing & Measuring (E6).'
# E4-1
d['depts'].append({"n":"Militaria & replicas","mode":"mixed","note":"Deactivated and non-firing pieces; Decorative replica weapon and Deactivated ordnance arrive from B4.","b":[{"m":"Status","v":"non-firing replica · deactivated (certified) · antique","w":"EU Implementing Regulation 2015/2403 on deactivation."}],
 "s":[{"n":"Deactivated & replica firearms","k":[
  {"n":"Deactivated firearm","a":"deac · inert firearm","d":"Real firearm made permanently inoperable under a certified standard and kept for display or collecting.","t":["EU-certified (from 8 April 2016)","earlier national standard"],"s":"https://www.legislation.gov.uk/eur/2015/2403/data.xht"},
  {"n":"Non-firing replica firearm","a":"display replica","d":"Copy of a firearm built so it cannot fire ammunition, made for collectors, reenactors and film use.","t":["historical (flintlock, percussion)","Wild West","world-war"],"s":"https://www.deltamike.co.nz/brand/denix/","r":[["Denix replicas","Denix"]]}]}]})
json.dump(d,open('out/E4.json.tmp','w'),ensure_ascii=False,indent=1); os.replace('out/E4.json.tmp','out/E4.json')
b=json.load(open('out/E4_brands.json'))
b['b'].append({"n":"Denix","c":"Spain","seg":"Specialist","kf":"replica weapons","d":"Maker of non-firing replica firearms and edged weapons for collectors and reenactors.","s":"https://www.deltamike.co.nz/brand/denix/"})
b['b'].sort(key=lambda x:x['n'].lower())
json.dump(b,open('out/E4_brands.json.tmp','w'),ensure_ascii=False,indent=1); os.replace('out/E4_brands.json.tmp','out/E4_brands.json')
