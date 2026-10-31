import json,collections
W="https://en.wikipedia.org/wiki/"
K=collections.defaultdict(list)
def a(kind,mk,n,y,page=None,v=None,own=None,cty=None):
    e={"n":n,"mk":mk,"y":y,"g":mk,"s":W+(page or n).replace(" ","_"),"v":v or []}
    if own:e["own"]=own
    if cty:e["own_y"]="";e["cty"]=cty
    K[kind].append(e)
US="United States"
def m(kind,mk,n,y,page=None,v=None,own=None,cty=US): a(kind,mk,n,y,page,v,own,cty)
GM="General Motors"
m("Muscle car","Oldsmobile","Oldsmobile 442","1964",own=GM)
m("SUV","Oldsmobile","Oldsmobile Bravada","1991",own=GM)
m("MPV","Oldsmobile","Oldsmobile Silhouette","1990",own=GM)
m("Estate","Oldsmobile","Oldsmobile Vista Cruiser","1964",own=GM)
m("Saloon","Oldsmobile","Oldsmobile Intrigue","1997",own=GM)
m("Luxury saloon","Oldsmobile","Oldsmobile Aurora","1994",own=GM)
m("Saloon","Oldsmobile","Oldsmobile Achieva","",own=GM)
m("Saloon","Saturn","Saturn Aura","2006",own=GM)
m("Saloon","Saturn","Saturn L-Series","2000",own=GM)
m("SUV","Saturn","Saturn Outlook","",own=GM)
m("MPV","Saturn","Saturn Relay","2005",own=GM)
m("SUV","Saturn","Saturn Vue","",own=GM)
m("Off-roader","Hummer","Hummer H1","")
m("SUV","Hummer","Hummer H2","2002")
m("Off-roader","Hummer","Hummer H3","2005")
m("SUV","GMC","GMC Acadia","")
m("SUV","GMC","GMC Envoy","1998")
m("Utility coupé","GMC","GMC Caballero","1978")
m("Estate","Edsel","Edsel Bermuda","1958")
m("Estate","Edsel","Edsel Roundup","1958")
m("Estate","Edsel","Edsel Villager","1958")
m("Coupé","Studebaker","Studebaker Avanti","1962")
m("Estate","Studebaker","Studebaker Conestoga","1954")
m("Utility coupé","Studebaker","Studebaker Coupe Express","1937")
m("Coupé","Studebaker","Studebaker Golden Hawk","1956")
m("Grand tourer","Studebaker","Studebaker Gran Turismo Hawk","1962")
m("Coupé","Studebaker","Studebaker Power Hawk","1956")
m("Coupé","Studebaker","Studebaker Sky Hawk","1956")
m("Estate","Studebaker","Studebaker Wagonaire","1963")
m("Coupé","Packard","Packard Mayfair","1951")
m("Coupé","Hudson","Hudson Italia","1954")
m("Sports car","Nash","Nash-Healey","1951")
m("Coupé","Eagle","Eagle Talon","")
m("Saloon","Eagle","Eagle Vision","1992")
m("Estate","Mercury","Mercury Colony Park","1957")
m("Estate","Mercury","Mercury Commuter","1957")
m("Muscle car","Mercury","Mercury Cyclone Spoiler II","1969")
m("SUV","Mercury","Mercury Mariner","2005")
m("Saloon","Mercury","Mercury Milan","2006")
m("SUV","Mercury","Mercury Mountaineer","1996")
m("MPV","Mercury","Mercury Villager","1993")
m("Estate","Mercury","Mercury Voyager","1957")
m("Hot rod and custom car","Mercury","Hirohata Merc","")
m("SUV","Pontiac","Pontiac Aztek","2001")
m("Estate","Pontiac","Pontiac Grand Safari","1971")
m("MPV","Pontiac","Pontiac Montana","1997")
m("Saloon","Pontiac","Pontiac G8","")
m("Estate","Pontiac","Pontiac Safari","1955")
m("Roadster","Pontiac","Pontiac Solstice","2005")
m("Muscle car","Pontiac","Pontiac Can Am","")
m("Saloon","Plymouth","Plymouth Acclaim","1989")
m("Coupé","Plymouth","Plymouth Duster","1969")
m("Coupé","Plymouth","Plymouth Laser","1989")
m("Sports car","Plymouth","Plymouth Prowler","1997")
m("Muscle car","Plymouth","Plymouth Road Runner","1968")
m("Saloon","Plymouth","Plymouth Caravelle","1983")
m("Hatchback","Dodge","Dodge Caliber","2007")
m("Saloon","Dodge","Dodge Attitude","2006")
m("Saloon","Dodge","Dodge Avenger","")
m("Muscle car","Dodge","Dodge Challenger (2008)","2008")
m("Saloon","Dodge","Dodge Charger (2006)","2005")
m("Hatchback","Dodge","Dodge Charger (1981)","1981")
m("MPV","Dodge","Dodge Caravan","1984",v=[{"n":"Chrysler minivans (S)","y":"1984","d":"1984-1990 model years"},{"n":"Chrysler minivans (AS)","y":"1991","d":"1991-1995"},{"n":"Chrysler minivans (NS)","y":"1996","d":"1996-2000"},{"n":"Chrysler minivans (RS)","y":"2001","d":"2001-2007"},{"n":"Chrysler minivans (RT)","y":"2008","d":"from model year 2008"}])
m("SUV","Rivian","Rivian R1S","")
m("SUV","Rivian","Rivian R2","")
m("SUV","Rivian","Rivian R3","")
m("Luxury saloon","Lucid","Lucid Air","")
m("SUV","Lucid","Lucid Gravity","2024")
m("Luxury saloon","Fisker","Fisker Karma","2011")
m("SUV","Fisker","Fisker Ocean","")
m("Sports car","Shelby","Shelby Daytona","")
m("Roadster","Shelby","Shelby Series 1","")
m("Sports car","Saleen","Saleen S7","")
m("Sports car","Saleen","Saleen S1","")
m("SUV","Saleen","Saleen XP8","1998")
m("City car","Gurgel","Gurgel BR-800","1988",cty="Brazil")
m("SUV","Gurgel","Gurgel Carajás","1984",cty="Brazil")
m("City car","Gurgel","Gurgel Supermini","1992",cty="Brazil")
m("Off-roader","Troller","Troller T4","",own="Ford do Brasil",cty="Brazil")
m("Kit car","Mastretta","Mastretta Unidiseño","",cty=None)
def q(n):return "https://www.wikidata.org/wiki/"+n
B=[("GMC","United States","Q28993"),("Oldsmobile","United States","Q204327"),("Saturn","United States","Q569235"),("Hummer","United States","Q213487"),("Studebaker","United States","Q938876"),("Packard","","Q40971"),("Hudson","United States","Q1313428"),("Nash","United States","Q1081459"),("DeSoto","United States","Q27558"),("Edsel","United States","Q1287696"),("Imperial","United States","Q668822"),("Eagle","United States","Q1203417"),("Geo","United States","Q1502806"),("Duesenberg","United States","Q27582"),("Cord","United States","Q869084"),("Auburn","United States","Q758549"),("DeLorean","United States","Q1241608"),("Shelby","United States","Q1045210"),("Rivian","United States","Q7338847"),("Lucid","United States","Q28027517"),("Fisker","United States","Q1420893"),("Mercury","United States","Q613883"),("Gurgel","Brazil","Q1555170"),("Troller","Brazil","Q1504331"),("Felino","Italy","Q100808")]
brands=[{"n":n,"c":c,"s":q(i)} for n,c,i in B if c]
bu={"Oldsmobile":{"own":GM,"c":US},"Saturn":{"own":GM,"c":US},"Auburn":{"own":"Cord Automobile","c":US},"Nash":{"own":"Nash-Kelvinator Corporation","c":US},"Troller":{"own":"Ford do Brasil","c":"Brazil"},
"Buick":{"own":GM,"c":US},"Cadillac":{"own":GM,"c":US},"Chevrolet":{"own":GM,"c":US},"Dodge":{"own":"Stellantis North America","c":US},"Jeep":{"own":"Stellantis North America","c":US},
"Ram":{"c":"United States; Canada"},"Ford":{"c":US},"Tesla":{"c":US},"Lincoln":{"c":US},"AMC":{"c":US},"GMC":{"c":"United States; Canada"}}
for n,c,i in B:
    if n not in bu and c: bu[n]={"c":c}

import re,json as _j
KM={"S":"Saloon","E":"Estate","M":"MPV","U":"SUV","MC":"Muscle car","SP":"Sports car","R":"Roadster","C":"Coupé","H":"Hatchback","LS":"Luxury saloon","GT":"Grand tourer","L":"Limousine","CV":"Convertible","N":"Car, body style not stated"}
cars=_j.load(open("/home/user/Possession-Taxonomy/rebuild/out/G1_parts/CARS.json"))
ex=set()
for dp in cars["depts"]:
  for sh in dp["s"]:
    for k in sh["k"]:
      for e in k.get("x",[]): ex.add(e["n"].lower())
import re
def full(mk,n):
    n=n.lower(); m=mk.lower()
    if n.startswith(m): n=n[len(m):]
    n=re.sub(r"^[\s\-]*(rambler)?","",n) if mk=="AMC" else n
    return re.sub(r"[^a-z0-9()]","",n)
def stem(mk,n): return re.sub(r"\(.*?\)","",full(mk,n))
FULL=set();STEM=set()
for dp in cars["depts"]:
  for sh in dp["s"]:
    for k in sh["k"]:
      for e in k.get("x",[]):
        FULL.add((e["g"],full(e["g"],e["n"])));STEM.add((e["g"],stem(e["g"],e["n"])))
SKIPPED=[]
def dup(mk,n):
    f=full(mk,n);st=stem(mk,n)
    if (mk,f) in FULL: return True
    if "(" not in n and (mk,st) in STEM: return True
    return False
for kk in list(K):
    keep=[]
    for e in K[kk]:
        if dup(e["mk"],e["n"]): SKIPPED.append(e["n"]); continue
        FULL.add((e["mk"],full(e["mk"],e["n"])));STEM.add((e["mk"],stem(e["mk"],e["n"])));keep.append(e)
    K[kk]=keep
GG="Global group";IN="Independent"
META={"Oldsmobile":(GM,GG,US),"Saturn":(GM,GG,US),"Buick":(GM,GG,US),"Cadillac":(GM,GG,US),"Chevrolet":(GM,GG,US),"Dodge":("Stellantis North America",GG,US),"Jeep":("Stellantis North America",GG,US),"Chrysler":("Stellantis",GG,US),"Ford":("Ford Motor Company",GG,US),"Lincoln":("Ford Motor Company",GG,US),"Ram":("Stellantis",GG,US),"Troller":("Ford do Brasil",GG,"Brazil"),"Auburn":("Cord Automobile",IN,US),"Nash":("Nash-Kelvinator Corporation",IN,US),"Gurgel":("",IN,"Brazil")}
CT={"Brazil":["Puma","Brasinca","FNM","Santa Matilde","Dardo","Lobini","Gurgel","Troller"],"Argentina":["Anasagasti","Sero"]}
def meta(mk):
    if mk in META: return META[mk]
    c=US if mk in ("Hudson","Studebaker","Edsel","Imperial","Eagle","Geo","Duesenberg","Cord","DeLorean","Mercury","Plymouth","DeSoto","Hummer","GMC","AMC","Tesla","Shelby","Rivian","Lucid","Fisker") else ("Brazil" if mk in CT["Brazil"] else ("Argentina" if mk in CT["Argentina"] else ""))
    return ("",IN,c)
for line in open("work/CARS_ADD_AMERICAS/data2b.txt"):
    if line.startswith("#") or not line.strip(): continue
    kc,mk,n,y=line.rstrip("\n").split("|")
    if dup(mk,n): SKIPPED.append(n); continue
    FULL.add((mk,full(mk,n)));STEM.add((mk,stem(mk,n)))
    own,tier,c=meta(mk)
    e={"n":n,"mk":mk,"y":y,"g":mk,"s":"https://en.wikipedia.org/wiki/"+n.replace(" ","_"),"v":[],"tier":tier}
    if own:e["own"]=own
    if c:e["cty"]=c
    K[KM[kc]].append(e)
for k,v in K.items():
  for e in v:
    if "tier" not in e:
      own,tier,c=meta(e["mk"]); e["tier"]=tier
      if own: e["own"]=own
      if c: e["cty"]=c
out={"kinds":dict(K),"brands":brands,"brand_updates":bu}

for n,b in bu.items():
    o,t,c=meta(n) if n not in ("Ram",) else ("Stellantis",GG,US)
    b["tier"]=t if n not in ("Tesla","Lincoln","Jeep","Ford") else b.get("tier",t)
bu["Ford"]={"own":"Ford Motor Company","tier":GG,"c":US}
bu["Lincoln"]={"own":"Ford Motor Company","tier":GG,"c":US}
bu["Tesla"]["tier"]=IN
bu["Ram"]={"own":"Stellantis","tier":GG,"c":"United States; Canada"}
bu["Lincoln"]["own_y"]="1922"
print("skipped dup",len(SKIPPED),SKIPPED[:400])
bu["Jeep"]["tier"]=GG
bu["Chrysler"]={"own":"Stellantis","tier":GG,"c":US}
for n,c,u in [("Puma","Brazil","https://en.wikipedia.org/wiki/List_of_automobiles_manufactured_in_Brazil"),("Brasinca","Brazil","https://en.wikipedia.org/wiki/List_of_automobiles_manufactured_in_Brazil"),("FNM","Brazil","https://en.wikipedia.org/wiki/List_of_automobiles_manufactured_in_Brazil"),("Santa Matilde","Brazil","https://en.wikipedia.org/wiki/List_of_automobiles_manufactured_in_Brazil"),("Dardo","Brazil","https://en.wikipedia.org/wiki/List_of_automobiles_manufactured_in_Brazil"),("Lobini","Brazil","https://en.wikipedia.org/wiki/List_of_automobiles_manufactured_in_Brazil"),("Anasagasti","Argentina","https://en.wikipedia.org/wiki/List_of_car_models_commercialized_in_Argentina"),("Sero","Argentina","https://en.wikipedia.org/wiki/List_of_car_models_commercialized_in_Argentina")]:
    brands.append({"n":n,"c":c,"s":u}); bu[n]={"c":c,"tier":IN}
out["brands"]=brands;out["brand_updates"]=bu
json.dump(out,open("out/G1_parts/cars_add/AMERICAS.json","w"),ensure_ascii=False,indent=1)
print(sum(len(v) for v in K.values()))
