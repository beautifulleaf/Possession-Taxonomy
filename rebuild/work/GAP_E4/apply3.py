import json,re,os,sys
sys.path.insert(0,'.')
from names import S,sp
P='/home/user/Possession-Taxonomy/rebuild/out/E4.json'
d=json.load(open(P))
K={};SH=None
for dep in d['depts']:
  for sh in dep['s']:
    if sh['n'].startswith('Shotguns'): SH=sh
    for k in sh['k']: K[k['n']]=k
LS='https://en.wikipedia.org/wiki/List_of_shotguns'
def url(t): return 'https://en.wikipedia.org/wiki/'+t.replace(' ','_')
def mkkind(n,desc,nl):
  return {"n":n,"a":"","d":desc,"s":LS,"nl":nl,"sel":"","xg":"by maker","x":[]}
NL="One entry is a firearm model line; marks and calibres are versions."
new={
 "Bolt-action shotgun":mkkind("Bolt-action shotgun","Smoothbore long gun loaded by working a bolt by hand for each shot.",NL),
 "Lever-action shotgun":mkkind("Lever-action shotgun","Smoothbore long gun loaded by working a lever under the action.",NL),
 "Revolving shotgun":mkkind("Revolving shotgun","Smoothbore gun that feeds its shells from a revolving cylinder or drum.",NL),
 "Shotgun, action not stated":mkkind("Shotgun, action not stated","Shotgun listed in Wikipedia's List of shotguns whose own page or the list does not name its action.",NL),
}
K.update(new)
# table: name -> (kind, page title or None, desc, year, maker group)
T=[
("Marlin Model 55","Bolt-action shotgun","Marlin Model 55","Bolt-action shotgun in 20, 16, 12 and 10 gauge with a two-round detachable box magazine.","","Marlin"),
("Marlin Model 25MG","Bolt-action shotgun","Marlin Model 25MG","Bolt-action smoothbore .22 WMR rifle for snake shot, sold as a garden pest gun.","","Marlin"),
("Mossberg 183","Bolt-action shotgun","Mossberg 183","Bolt-action .410 bore shotgun made by Mossberg from 1947 to 1986.","1947","Mossberg"),
("Mossberg 185","Bolt-action shotgun","Mossberg 185","Bolt-action 20-gauge shotgun made by Mossberg from 1948 to 1964.","1948","Mossberg"),
("MTs 20-01","Bolt-action shotgun","MTs 20-01","Soviet bolt-action shotgun.","","MTs"),
("Winchester Model 1887/1901","Lever-action shotgun","Winchester Model 1887","Lever-action shotguns designed by John Browning and made by Winchester in the late 19th and early 20th centuries.","1887","Winchester"),
("Armsel Striker","Revolving shotgun","Armsel Striker","Revolving 12-gauge riot and combat shotgun, also sold as the Protecta and Street Sweeper.","","Armsel"),
("Becker Revolving Shotgun","Revolving shotgun",None,"Revolving shotgun named in Wikipedia's List of shotguns (1899).","1899","Becker"),
("Colt Defender Mark I","Revolving shotgun","Colt Defender Mark I","Eight-barrel 20-gauge volley shotgun with a rotating striker, completed in 1967 and never adopted.","1967","Colt"),
("ENARM Pentagun","Revolving shotgun","ENARM Pentagun","Brazilian five-round revolving shotgun with a movable barrel that stops gas venting.","","ENARM"),
("MTs255","Revolving shotgun","MTs255","Russian revolver shotgun with a five-round swing-out cylinder.","","MTs"),
("Roper repeating shotgun","Revolving shotgun","Sylvester H. Roper","Revolving repeating shotgun invented by Sylvester H. Roper.","1867","Roper"),
("Manville gun","Revolving shotgun","Manville gun","Stockless revolver-type gun with a clockwork-driven cylinder, sold in three bore sizes until 1943.","1935","Manville"),
("Crye Six12","Revolving shotgun",None,"Revolving shotgun named in Wikipedia's List of shotguns (2014).","2014","Crye"),
("Bandayevsky RB-12","Pump-action shotgun","Bandayevsky RB-12","Russian pump-action shotgun with a folding stock.","","Bandayevsky"),
("Brixia PM-5","Pump-action shotgun","Brixia PM-5","Italian 12-gauge pump-action shotgun with a detachable box magazine.","","Brixia"),
("FN P-12","Pump-action shotgun","FN P-12","Pump-action 12-gauge shotgun made by FN Herstal and assembled in Portugal.","","FN"),
("Fosbery Pump Shotgun","Pump-action shotgun","Fosbery Pump Shotgun","16-gauge pump-action prototype designed in 1891, the first to use a multi-lug rotating bolt.","1891","Fosbery"),
("KS-23","Pump-action shotgun","KS-23","Russian pump-action carbine firing 23 mm shells, made at the Tula Arms Plant.","","KS"),
("Knight's Armament Company Masterkey","Pump-action shotgun","Knight's Armament Company Masterkey","Door-breaching pump shotgun built from a shortened Remington 870 that mounts under a rifle barrel.","","Knight's Armament"),
("Molot Bekas-M","Pump-action shotgun","Molot Bekas-M","Russian pump-action shotgun series sharing one receiver.","","Molot"),
("New Haven 600","Pump-action shotgun","New Haven 600","Pump-action shotgun made by Mossberg for retailers, identical to the Mossberg 500 apart from its magazine.","","New Haven"),
("RMB-93","Pump-action shotgun","RMB-93","Pump-action shotgun by KBP of Tula, the base model of the Rys series for special forces and police.","","RMB"),
("Rexio SpecOps","Pump-action shotgun","Rexio SpecOps","Argentine pump-action shotgun made by Rexio.","","Rexio"),
("MTs 21-12","Semi-automatic shotgun","MTs 21-12","Soviet semi-automatic shotgun.","","MTs"),
("QBS-09","Semi-automatic shotgun","QBS-09","Semi-automatic shotgun developed by Norinco, also known as the Type 09.","","Norinco"),
("SRM Arms Model 1216","Semi-automatic shotgun","SRM Arms Model 1216","Short delayed-blowback semi-automatic shotgun with a 16-round revolver magazine.","","SRM"),
("Smith & Wesson AS","Semi-automatic shotgun","Smith & Wesson AS","Prototype 12-gauge select-fire shotgun with an M16-like layout, built to rival the HK CAWS.","","Smith"),
("Walther automatic shotgun","Semi-automatic shotgun","Walther automatic shotgun","German self-loading shotgun resembling the Browning Auto-5.","","Walther"),
("IZhK","Single-shot shotgun","IZhK","Soviet single-shot break-action shotgun.","1955","IZh"),
("Cynergy Shotgun","Over-under shotgun","Cynergy Shotgun","Browning over-under shotgun range made in Japan that departed from the traditional design.","2004","Browning"),
("FN SC-1","Over-under shotgun","FN SC-1","Over-under double-barrelled sporting shotgun.","2011","FN"),
("IZh-56","Combination gun","IZh-56","Soviet double-barrelled combination gun, known as the Belka.","1956",None),
("MTs 30","Combination gun","MTs 30","Soviet custom hunting combination gun family.","",None),
("TOZ-28","Combination gun","TOZ-28","Soviet hunting combination gun.","",None),
("TOZ-250","Combination gun","TOZ-250","Soviet double-barrelled combination gun.","",None),
("Springfield Armory M6 Scout","Combination gun","Springfield Armory M6 Scout","Rifle-over-.410 combination gun derived from the M6 aircrew survival weapon, with longer barrels.","",None),
]
for n in ["IZh-12","IZh-59","IZh-94","TOZ-84","MTs 6","MTs 7","MTs 8","MTs 109","MTs 110","MTs 111"]:
  g=n.split()[0].split('-')[0]
  T.append((n,"Shotgun, action not stated",n,"Double-barrelled shotgun; the page does not say whether side-by-side or over-under.","",g))
for n,desc,g in [("Ares Companion","Shotgun","Ares"),("Ball and shot gun","Shotgun that fires both shot and a solid ball, first built by Holland and Holland.","Holland"),("Camp gun","Shotgun","Camp"),("Chiappa Little Badger","Family of survival rifles and shotguns by Chiappa.","Chiappa"),("Ciener Ultimate Over/Under","Shotgun mounted under an M16 or M4 rifle.","Ciener"),("GEN-12","Shotgun","GEN"),("Greener Police Gun","Shotgun","Greener"),("Hawk Industries Type 97","Chinese military and police shotgun patterned after the Remington Model 870.","Hawk"),("Hunt MH12","Shotgun","Hunt"),("K12 PUMA","Shotgun","K12"),("KUGS HD410","Shotgun","KUGS"),("M26 Modular Accessory Shotgun System","Underbarrel shotgun attachment for service rifles.","M26"),("Manufrance Rapid","Shotgun","Manufrance"),("MAUL (shotgun)","Underbarrel combat shotgun designed by Metal Storm.","Metal Storm"),("MTs 5","Soviet custom hunting guns with double barrels.","MTs"),("MTs 260","Shotgun","MTs"),("OTs-28","Shotgun","OTs"),("Pindad SG-1","12-gauge shotgun made by Pindad of Indonesia.","Pindad"),("Safir T-14","Shotgun made by Safir Arms of Turkey.","Safir"),("Winchester Liberator","Prototype four-barrelled derringer-style shotgun based on the Hillberg Insurgency Weapon.","Winchester")]:
  desc2 = desc if desc!="Shotgun" else "Shotgun listed in Wikipedia's List of shotguns; no page names its action."
  T.append((n,"Shotgun, action not stated",None,desc2,"",g))
for n,kn,title,desc,y,g in T:
  k=K[kn]
  e={"n":n,"a":"","d":desc,"mk":"","y":y,"s":url(title) if title else LS,"v":[]}
  if kn!="Combination gun": e["g"]=g
  if not any(re.sub(r'\W','',x['n'].lower())==re.sub(r'\W','',n.lower()) for x in k['x']): k['x'].append(e)
# blunderbuss
bb=K['Blunderbuss']; bb.update({"nl":NL,"sel":"Wikipedia's List of shotguns names one blunderbuss; no complete list of the form exists.","x":[{"n":"Blunderbuss","a":"","d":"Short wide-barrelled muzzle-loader with a flared muzzle, an early predecessor of the shotgun.","mk":"","y":"","s":url("Blunderbuss"),"v":[]}]})
bb.pop("xg",None)
# insert new kinds
ks=SH['k']; i=[k['n'] for k in ks].index('Semi-automatic shotgun')+1
for kn in ["Bolt-action shotgun","Lever-action shotgun","Revolving shotgun"]: ks.insert(i,new[kn]); i+=1
ks.insert([k['n'] for k in ks].index('Combination gun')+1,new["Shotgun, action not stated"])
N=len(sp(S))
msg=f"Complete: all {N} rows of the page are placed in the shotgun kinds of this shelf (by action, in Combination gun, in Blunderbuss, or under Shotgun, action not stated); RGA-86 is left out because its own article calls it a grenade launcher. Actions come from each row's own Wikipedia page (MediaWiki API extracts)."
for kn in ['Single-shot shotgun','Side-by-side shotgun','Over-under shotgun','Pump-action shotgun','Semi-automatic shotgun','Bolt-action shotgun','Lever-action shotgun','Revolving shotgun','Shotgun, action not stated','Combination gun']:
  k=K[kn]
  k['sel']=re.sub(r'\s*Covers \d+ of the page.*$','',k['sel']).replace('; combination-gun and revolving shotguns are left out; tactical and military pump and semi-automatic shotguns are now included','').strip()
  k['sel']=(k['sel']+' ' if k['sel'] else "Shotguns of Wikipedia's List of shotguns. ")+msg
k=K['Combination gun']
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P)
print(N,{kn:len(K[kn]['x']) for kn in new})
