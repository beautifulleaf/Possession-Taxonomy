import json
SRC="https://en.wikipedia.org/wiki/List_of_grape_varieties"
reg={"France":"French","Italy":"Italian","Spain":"Spanish","Portugal":"Portuguese",
"Germany":"German, Austrian & Swiss","Austria":"German, Austrian & Swiss","Switzerland":"German, Austrian & Swiss",
"Greece":"Greek, Cypriot, Maltese & Turkish","Cyprus":"Greek, Cypriot, Maltese & Turkish","Malta":"Greek, Cypriot, Maltese & Turkish","Turkey":"Greek, Cypriot, Maltese & Turkish",
"Georgia":"Caucasus","Armenia":"Caucasus","Azerbaijan":"Caucasus",
"United States":"New World & Asian","Argentina":"New World & Asian","South Africa":"New World & Asian","Australia":"New World & Asian","China":"New World & Asian","Japan":"New World & Asian","Israel":"New World & Asian"}
for c in "Hungary,Czech Republic,Slovakia,Slovenia,Croatia,Serbia,Montenegro,Bosnia and Herzegovina,North Macedonia,Bulgaria,Romania,Moldova,Ukraine,Russia".split(","): reg[c]="Central & Eastern European"
reg["Luxembourg"]="German, Austrian & Swiss";reg[""]="Origin not stated"
col={"H":("Hybrid varieties","hybrid"),"R":("Red varieties","red"),"W":("White varieties","white"),"P":("Pink and grey varieties","pink")}
order=["French","Italian","Spanish","Portuguese","German, Austrian & Swiss","Central & Eastern European","Greek, Cypriot, Maltese & Turkish","Caucasus","New World & Asian","Origin not stated"]
rows=[l.rstrip("\n").split("|") for l in open("data.txt") if l.strip()]
rows=[r for r in rows if r[3]!="P"]
rows.append(["Roesler","","Austria","R"])
idx={(r[0].lower(),r[3]):r for r in rows}
def add(fn,c):
    for l in open(fn):
        p=l.rstrip("\n").split("|")
        while len(p)<3:p.append("")
        k=(p[0].lower(),c)
        if k in idx:
            o=idx[k]
            if not o[1]:o[1]=p[1]
            if not o[2]:o[2]=p[2]
        else:
            r=[p[0],p[1],p[2],c];rows.append(r);idx[k]=r
add("new_white.txt","W");add("new_pink.txt","P")
HY=set()
for l in open("new_hybrid.txt"):
    p=l.rstrip("\n").split("|")
    if p[0]=="Roesler":continue
    HY.add(p[0].lower())
HYX={"alexander","baco noir","chambourcin","chancellor","chelois","cabernet cortis","cascade","orion","flora","l'acadie blanc"}
ALLHY=HY|HYX
names={r[0].lower() for r in rows}
for l in open("new_hybrid.txt"):
    p=l.rstrip("\n").split("|")
    if p[0]=="Roesler" or p[0].lower() in names:continue
    rows.append([p[0],p[1] if len(p)>1 else "","","H"]);names.add(p[0].lower())

shelves=[]
for c in "RWPH":
    sh=[]
    for r in order:
        es=[x for x in rows if x[3]==c and reg.get(x[2],'Origin not stated')==r]
        if not es: continue
        es.sort(key=lambda x:(x[2],x[0].lower()))
        xs=[]
        for n,a,cty,_ in es:
            hy=(c=="H" or n.lower() in ALLHY)
            e={"n":n,"a":a.replace(", "," · "),"d":(f"{col[c][1].capitalize()} wine grape variety"+(f" of {cty} origin." if cty else ", origin not stated in the list.") if c!="H" else "Hybrid wine grape variety bred from more than one Vitis species; berry colour not stated in the list.")+(" Hybrid." if hy and c!="H" else ""),"mk":"","y":"","s":SRC,"g":cty or "Origin not stated"}
            xs.append(e)
        word="varieties" if c!="P" else "varieties"
        kn=f"{r} {col[c][1]} varieties" if r not in("Origin not stated",) else f"{col[c][1].capitalize()} varieties of unstated origin"
        if c=="H": kn="Interspecific hybrid varieties"
        if r=="French": kn=f"French {col[c][1]} varieties"
        sh.append({"n":kn,"a":"","d":f"{col[c][1].capitalize()} wine grape varieties whose listed country of origin is in this region.","s":SRC,
         "nl":"One entry is a wine grape variety under its main name; its other names are aliases.",
         "sel":"Follows the Vitis vinifera wine sections (red, white, rosé) and the wine hybrid sections of Wikipedia's List of grape varieties, read in windows; table-only and labrusca-only varieties are out of scope.",
         "xg":"country of origin","tt":[["Berry colour",[col[c][1]]]] if c!="H" else [["Species",["interspecific hybrid"]]],"x":xs})
    shelves.append({"n":col[c][0],"t":f"Wine grapes with {col[c][1]} berries, grouped by the region where the variety originated." if c!="H" else "Wine grapes bred from more than one Vitis species; the list states no berry colour for them.","ax":"kinds by home region of the variety","k":sh})
dept={"n":"Grape varieties","mode":"variety",
"t":"Wine grape varieties, each a named variety rather than a wine; a wine sold under its place name → the wine departments; a table grape is food, not wine.",
"ax":"What colour are the berries, and where did the variety originate?",
"note":"Second way into wine, by grape. Appellations for each variety are not yet filled in.",
"s":shelves}
json.dump({"depts":[dept],"brands":[],"renames":{},"moves":[]},open("/home/user/Possession-Taxonomy/rebuild/out/J7_parts/GRAPES.json","w"),ensure_ascii=False,indent=1)
print(len(rows))
