import json
SRC="https://en.wikipedia.org/wiki/List_of_grape_varieties"
reg={"France":"French","Italy":"Italian","Spain":"Spanish","Portugal":"Portuguese",
"Germany":"German, Austrian & Swiss","Austria":"German, Austrian & Swiss","Switzerland":"German, Austrian & Swiss",
"Greece":"Greek, Cypriot, Maltese & Turkish","Cyprus":"Greek, Cypriot, Maltese & Turkish","Malta":"Greek, Cypriot, Maltese & Turkish","Turkey":"Greek, Cypriot, Maltese & Turkish",
"Georgia":"Caucasus","Armenia":"Caucasus","Azerbaijan":"Caucasus",
"United States":"New World & Asian","Argentina":"New World & Asian","South Africa":"New World & Asian","Australia":"New World & Asian","China":"New World & Asian","Japan":"New World & Asian","Israel":"New World & Asian"}
for c in "Hungary,Czech Republic,Slovakia,Slovenia,Croatia,Serbia,Montenegro,Bosnia and Herzegovina,North Macedonia,Bulgaria,Romania,Moldova,Ukraine,Russia".split(","): reg[c]="Central & Eastern European"
reg[""]="Origin not stated"
col={"R":("Red varieties","red"),"W":("White varieties","white"),"P":("Pink and grey varieties","pink")}
order=["French","Italian","Spanish","Portuguese","German, Austrian & Swiss","Central & Eastern European","Greek, Cypriot, Maltese & Turkish","Caucasus","New World & Asian","Origin not stated"]
rows=[l.rstrip("\n").split("|") for l in open("data.txt") if l.strip()]
shelves=[]
for c in "RWP":
    sh=[]
    for r in order:
        es=[x for x in rows if x[3]==c and reg[x[2]]==r]
        if not es: continue
        es.sort(key=lambda x:(x[2],x[0].lower()))
        xs=[]
        for n,a,cty,_ in es:
            e={"n":n,"a":a.replace(", "," · "),"d":f"{col[c][1].capitalize()} wine grape variety"+(f" of {cty} origin." if cty else ", origin not stated in the list."),"mk":"","y":"","s":SRC,"g":cty or "Origin not stated"}
            xs.append(e)
        word="varieties" if c!="P" else "varieties"
        kn=f"{r} {col[c][1]} varieties" if r not in("Origin not stated",) else f"{col[c][1].capitalize()} varieties of unstated origin"
        if r=="French": kn=f"French {col[c][1]} varieties"
        sh.append({"n":kn,"a":"","d":f"{col[c][1].capitalize()} wine grape varieties whose listed country of origin is in this region.","s":SRC,
         "nl":"One entry is a wine grape variety under its main name; its other names are aliases.",
         "sel":"Follows the red, white and rosé Vitis vinifera wine sections of Wikipedia's List of grape varieties; this part holds only the rows the fetch returned (see report), not yet the full list.",
         "xg":"country of origin","tt":[["Berry colour",[col[c][1]]]],"x":xs})
    shelves.append({"n":col[c][0],"t":f"Wine grapes with {col[c][1]} berries, grouped by the region where the variety originated.","ax":"kinds by home region of the variety","k":sh})
dept={"n":"Grape varieties","mode":"variety",
"t":"Wine grape varieties, each a named variety rather than a wine; a wine sold under its place name → the wine departments; a table grape is food, not wine.",
"ax":"What colour are the berries, and where did the variety originate?",
"note":"Second way into wine, by grape. Appellations for each variety are not yet filled in.",
"s":shelves}
json.dump({"depts":[dept],"brands":[],"renames":{},"moves":[]},open("/home/user/Possession-Taxonomy/rebuild/out/J7_parts/GRAPES.json","w"),ensure_ascii=False,indent=1)
print(len(rows))
