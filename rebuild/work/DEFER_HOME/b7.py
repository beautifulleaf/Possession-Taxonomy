import json
d=json.load(open('out/B7.json'))
def find(n,name):
    if isinstance(n,dict):
        if n.get('n')==name and n.get('x'): return n
        for k in('depts','s','k'):
            for x in n.get(k,[]) if isinstance(n.get(k),list) else []:
                r=find(x,name)
                if r: return r
fan=find(d,'Electric fan (design & vintage)'); fh=find(d,'Fan heater')
print(json.dumps(fan['x'][1],ensure_ascii=False)); print(fan['xg'], fan.get('nl'))
def E(n,mk,y,g,desc,url,**kw):
    e={"n":n,"a":"","d":desc,"mk":mk,"y":y,"s":url,"v":[],"dt":"MoMA","g":g}; e.update(kw); return e
M='https://www.moma.org/collection/works/?q=fan&classifications=3'
new=[
E("Pirali electric fan (1953)","Fabbriche Elettrotecniche Riunite (now Zerowatt)","1953","Early electric fans, 1890s to 1950s","Electric fan by Ezio Pirali, made of aluminium, chromed steel and rubber, held by MoMA, Architecture and Design.","https://www.moma.org/collection/works/3869"),
E("Ribbonaire fan","","c. 1935","Early electric fans, 1890s to 1950s","Ribbonaire fan by Wilfred O. Langille and Frederik Ljungström, held by MoMA's Design classification.",M),
E("Filterjet fan","","1951","Early electric fans, 1890s to 1950s","Fan by Peter Schlumbohm held by MoMA's Design classification (two records of the same design).",M),
E("Weiss desk fan HL1","","1961","Design-collection fans, 1960s to 1970s","Desk fan, model HL1, by Reinhold Weiss, held by MoMA's Design classification.",M),
E("Air Flow desk fan","G. Byrn Company, Copenhagen","c. 1965","Design-collection fans, 1960s to 1970s","Desk fan made by G. Byrn Company of Copenhagen, held by MoMA's Design classification.",M),
E("Zanuso table fan","","1973","Design-collection fans, 1960s to 1970s","Table fan by Marco Zanuso held by MoMA's Design classification.",M),
]
for e in new:
    if e['n']=="Pirali electric fan (1953)": e['n']="Pirali electric fan"
fan['x'].extend(new)
order={"Early electric fans, 1890s to 1950s":0,"Design-collection fans, 1960s to 1970s":1,"Design-award fans":2,"Designer fans, 2009 onward":3}
import re
def yr(e):
    m=re.search(r'\d{4}',e['y']); return int(m.group()) if m else 0
fan['x'].sort(key=lambda e:(order.get(e['g'],9),yr(e),e['n']))
fan['sel']=("No whole-space reference exists for collectable and designer fans. The list follows the maker histories on Wikipedia (Emerson Electric, Vornado Air, the Dyson Air Multiplier and Balmuda pages) and names one origin and three design landmarks of the kind. "
 "Added from fetched collection and award pages: MoMA's Design classification search for 'fan' (23 results, all read; the fans among them are entries: Behrens GB1, Pirali, Ribbonaire, Filterjet, Weiss HL1, Byrn Air Flow, Zanuso; a jet-engine fan blade, posters, a dress, a clock, a lamp and other non-fan results are left out), and the ADI Design Museum (Ariante). "
 "No complete list exists; follows the maker histories and design-collection pages named here.")
fh['x'].append(E("Barman electric fan heater","","c. 1934","Design collection","Chrome-plated electric fan heater by Christian Barman held by MoMA, Architecture and Design.","https://www.moma.org/collection/works/173628",role=None) if False else E("Barman electric fan heater","","c. 1934","Design collection","Chrome-plated electric fan heater by Christian Barman held by MoMA, Architecture and Design.","https://www.moma.org/collection/works/173628"))
fh['x'][-1]['role']="landmark" if False else ""
fh['x'][-1].pop('role')
fh['sel']=fh['sel'].replace("MoMA collection page for the Heater-Ventilator (model H 3).","MoMA collection pages for the Heater-Ventilator (model H 3) and the Barman electric fan heater (c. 1934).")
json.dump(d,open('work/DEFER_HOME/B7.new','w'),ensure_ascii=False,indent=1)
print(fh.get('xg'))
