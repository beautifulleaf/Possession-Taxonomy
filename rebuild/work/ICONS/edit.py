import json, os, re, collections
R='/home/user/Possession-Taxonomy/rebuild/out/'
def load(p): return json.load(open(p))
def save(p,d):
    t=p+'.tmp'; json.dump(d,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
def kinds(d):
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']: yield k
def kind(d,n):
    return [k for k in kinds(d) if k['n']==n][0]
NL="One entry is the first product of its kind or a design-collection landmark."
def sel(pages):
    return ("Follows only the fetched pages named here: "+pages+". Coverage: at most one origin entry (the first of its kind, where a fetched page says so) "
            "and items held by a named design collection (MoMA, V&A, Design Museum London, Cooper Hewitt, Vitra Design Museum) or given a major design award "
            "(Compasso d'Oro, Red Dot Best of the Best, iF Gold), each confirmed on a fetched page; no other models are listed.")
def ent(n,d,mk,y,s,role,g="Origin and design-canon entries",a="",dt=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[],"dt":dt,"g":g,"role":role}
def addbrands(code,items):
    p=R+code+'_brands.json'; b=load(p); have={x['n'] for x in b['b']}
    for n,c,d,s,kf in items:
        if n in have: continue
        b['b'].append({"n":n,"c":c,"f":"","seg":"Mainstream","d":d,"lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":s,"kf":kf})
    save(p,b)
def setk(k,entries,pages,keepnl=False):
    k['x']=entries
    k['xg']="Entry type"
    if keepnl and k.get('nl'): k['nl']=k['nl'].rstrip()+" It also holds design-collection landmarks."
    else: k['nl']=NL
    k['sel']=sel(pages)
MOMA='https://www.moma.org/collection/works/'
# ---- B6
p=R+'B6.json'; d=load(p)
setk(kind(d,'Robot vacuum cleaner'),[ent("Electrolux Trilobite","First robotic vacuum cleaner, according to Wikipedia's Robotic vacuum cleaner article.","Electrolux","1996","https://en.wikipedia.org/wiki/Robotic_vacuum_cleaner","origin",g="Origin")],"Wikipedia, Robotic vacuum cleaner")
setk(kind(d,'Upright vacuum cleaner'),[ent("Dyson Dual Cyclone DC02","Dual-cyclone upright vacuum cleaner held by MoMA, Architecture and Design.","Dyson","1994–1995",MOMA+'88172',"landmark",g="Design collection",dt="MoMA")],"MoMA collection page for the Dyson DC02")
kind(d,'Upright vacuum cleaner')['x'][0]['d']="Dual-cyclone vacuum cleaner held by MoMA, Architecture and Design (MoMA)."
setk(kind(d,'Cylinder vacuum cleaner'),[ent("Spalter electric vacuum cleaner","Vacuum cleaner by Achille and Pier Giacomo Castiglioni held by MoMA, Architecture and Design (MoMA).","R.E.M. di Rossetti Enrico","1956",MOMA+'1367',"landmark",g="Design collection",dt="MoMA")],"MoMA collection page for the Spalter Electric Vacuum Cleaner")
setk(kind(d,'Wet and dry vacuum cleaner'),[ent("Bidone Lavatutto","Wet and dry vacuum cleaner and floor scrubber by Francesco Trabucco and Marcello Vecchi; Compasso d'Oro, XV edition, 1989.","Alfatec","1989","https://www.adidesignmuseum.org/en/collection/bidone-lavatutto-vacuum-cleaner-liquid-vacuum-cleaner-floor-cleaner/","landmark",g="Design award",dt="Compasso d'Oro 1989")],"ADI Design Museum collection page for the Bidone Lavatutto")
save(p,d)
addbrands('B6',[("R.E.M. di Rossetti Enrico","Italy","Manufacturer of the Spalter electric vacuum cleaner held by MoMA.",MOMA+'1367',"cylinder vacuum cleaner"),
 ("Alfatec","","Producer of the Bidone Lavatutto wet and dry vacuum cleaner, Compasso d'Oro 1989.","https://www.adidesignmuseum.org/en/collection/bidone-lavatutto-vacuum-cleaner-liquid-vacuum-cleaner-floor-cleaner/","wet and dry vacuum cleaner")])
# ---- B7
p=R+'B7.json'; d=load(p)
k=kind(d,'Electric fan (design & vintage)')
beh=ent("Behrens fan model GB1","Electric fan designed by Peter Behrens for A.E.G. and held by MoMA, Architecture and Design (MoMA).","Allgemeine Elektricitäts Gesellschaft (A.E.G.)","c. 1908",MOMA+'1603',"landmark",g="Early electric fans, 1890s to 1950s",dt="MoMA")
ari=ent("Ariante fan","Table fan by Marco Zanuso for Vortice Elettrosociali; Compasso d'Oro, 1979 (Compasso d'Oro).","Vortice Elettrosociali","1979","https://www.adidesignmuseum.org/en/collection/ariante-fan","landmark",g="Design-award fans",dt="Compasso d'Oro 1979")
xs=k['x']; 
xs.insert(1,beh)
i=[j for j,x in enumerate(xs) if x['n']=='Vornado air circulator'][0]
xs.insert(i+1,ari)
k['nl']=k['nl'].rstrip()+" It also holds design-collection landmarks."
k['sel']=k['sel'].rstrip()+" Added from fetched collection and award pages: MoMA (Behrens fan GB1) and the ADI Design Museum (Ariante). Coverage: only first-of-kind origins and design-collection or major-award landmarks are added."
k['dt']=k.get('dt','')
setk(kind(d,'Fan heater'),[ent("Braun Heater-Ventilator H 3","Heater-ventilator by Dieter Rams for Braun held by MoMA, Architecture and Design (MoMA).","Braun","1962",MOMA+'4135',"landmark",g="Design collection",dt="MoMA")],"MoMA collection page for the Heater-Ventilator (model H 3)")
setk(kind(d,'Portable air conditioner'),[ent("Candyzionatore","Air conditioner by Joe Colombo for Candy; Compasso d'Oro, 1970 (Compasso d'Oro).","Candy","1970","https://www.adidesignmuseum.org/en/collection/air-conditioner-candyzionatore/","landmark",g="Design award",dt="Compasso d'Oro 1970")],"ADI Design Museum collection page for the Candyzionatore")
save(p,d)
addbrands('B7',[("Braun","Germany","German appliance maker; the Heater-Ventilator H 3 by Dieter Rams (1962) is held by MoMA.",MOMA+'4135',"fan heater"),
 ("Vortice Elettrosociali","","Producer of the Ariante fan, Compasso d'Oro 1979.","https://www.adidesignmuseum.org/en/collection/ariante-fan","electric fan"),
 ("Candy","","Producer of the Candyzionatore air conditioner, Compasso d'Oro 1970.","https://www.adidesignmuseum.org/en/collection/air-conditioner-candyzionatore/","portable air conditioner"),
 ("Allgemeine Elektricitäts Gesellschaft (A.E.G.)","Germany","Maker of the Behrens fan model GB1 held by MoMA.",MOMA+'1603',"electric fan")])
# ---- B8
p=R+'B8.json'; d=load(p)
setk(kind(d,'Baby monitor'),[ent("Zenith Radio Nurse","First baby monitor, according to Wikipedia's Baby monitor article; developed by Eugene F. McDonald and designed by Isamu Noguchi.","Zenith Radio","1937","https://en.wikipedia.org/wiki/Baby_monitor","origin",g="Origin")],"Wikipedia, Baby monitor")
save(p,d)
addbrands('B8',[("Zenith Radio","United States","Maker of the Radio Nurse, named as the first baby monitor.","https://en.wikipedia.org/wiki/Baby_monitor","baby monitor")])
# ---- H2
p=R+'H2.json'; d=load(p)
setk(kind(d,'Hearing aid'),[ent("Akouphone","First electric hearing aid, according to Wikipedia's Hearing aid article; created by Miller Reese Hutchison.","Miller Reese Hutchison","c. 1895","https://en.wikipedia.org/wiki/Hearing_aid","origin",g="Origin")],"Wikipedia, Hearing aid")
k=kind(d,'Manual wheelchair')
g0=k['x'][0].get('g','Milestone lines')
k['x'].append(ent("Carna folding wheelchair","Titanium folding wheelchair by Kazuo Kawasaki held by MoMA, Architecture and Design (MoMA).","SIG Workshop","1989",MOMA+'1512',"landmark",g="Design collection",dt="MoMA"))
k['x'].append(ent("Bob Hall racing wheelchair","Racing wheelchair by Bob Hall held by MoMA, Architecture and Design (MoMA).","Hall's Wheels","1986",MOMA+'2533',"landmark",g="Design collection",dt="MoMA"))
k['nl']=k['nl'].rstrip()+" It also holds design-collection landmarks."
k['sel']=k['sel'].rstrip()+" Added from fetched MoMA collection pages: the Carna folding wheelchair and the Bob Hall racing wheelchair. Coverage: only first-of-kind origins and design-collection or major-award landmarks are added."
save(p,d)
addbrands('H2',[("SIG Workshop","Japan","Manufacturer of the Carna folding wheelchair held by MoMA.",MOMA+'1512',"manual wheelchair"),
 ("Hall's Wheels","United States","Manufacturer of the Bob Hall racing wheelchair held by MoMA.",MOMA+'2533',"manual wheelchair")])
# ---- C8: tradition group
p=R+'C8.json'; d=load(p)
trad=["Delft","Encaustic","Zellige","Majolica and Talavera","Azulejo","İznik","Cuerda seca","Cement tile"]
for n in ('Wall tile','Floor tile'):
    k=kind(d,n)
    k.setdefault('tt',[]).append(["Tradition",trad])
    k.setdefault('see',[]).append(["F2","Tile traditions","Delft, encaustic, zellige, majolica and similar traditions belong to the visual-art taxonomy; they are types here, not entries"])
save(p,d)
print('ok')
