import json,re
d=json.load(open('out/B1.json'))
def find(n,name):
    if isinstance(n,dict):
        if n.get('n')==name and n.get('x'): return n
        for k in('depts','s','k'):
            for x in n.get(k,[]) if isinstance(n.get(k),list) else []:
                r=find(x,name)
                if r: return r
new=json.load(open('work/DEFER_HOME/vitra_new.json'))
drop={'Plexiglas Chair (VB 101 w)','La Fonda Side Chair (1700-1)','Upholstered Stacking Chair (with armrest) (0716-1)','Chair from the Hommage à Verner Panton edition','Stool from the Hommage à Verner Panton edition','Catenary Group No. 6380','Loose Cushion Group No. 5681'}
new=[e for e in new if e['n'] not in drop]
dc=find(d,'Dining chair')
def yr(e):
    m=re.search(r'\d{4}',e.get('y','')); return int(m.group()) if m else 9999
ex=dc['x']
for e in new:
    pos=len(ex)
    cand=[i for i,x in enumerate(ex) if x.get('g')==e['g']]
    if cand:
        pos=cand[-1]+1
        for i in cand:
            if yr(ex[i])>yr(e): pos=i; break
    else:
        for i,x in enumerate(ex):
            if x.get('g','~')>e['g'] and x.get('g')!='Date not stated': pos=i; break
    ex.insert(pos,e)
print(len(ex))
ms=find(d,'Modular shelving system')
for e in ms['x']:
    if e['n']=='String':
        e['d']="Wall shelving of two wire side ladders and thin shelves, winner of Bonnier's 1949 bookshelf competition. Peter Erlandsson and Pär Josefsson bought the rights to make and sell it in 2004."
        e['s']="https://www.stringfurniture.com/en/our-world/the-string-story"
        e['own']="String Furniture AB"; e['tier']="Independent"; e['cty']="Sweden"; e['own_y']="2004"
def E(n,dd,mk,y,s,g): return {"n":n,"a":"","d":dd,"mk":mk,"y":y,"s":s,"v":[],"dt":"","g":g,"own":"String Furniture AB","tier":"Independent","cty":"Sweden"}
cat="https://media.stringfurniture.com/media/storyblok/f/281765/x/0121dbfa9f/string-furniture-anniversary-catalogue.pdf"
ms['x'].append(E("String Pocket","Compact wall shelf sold as one unit of two wall panels and three shelves; Nisse Strinning's last design, with a metal version added in 2020.","String Furniture","2005","https://www.stringfurniture.com/en/series/pocket","2000s"))
ms['x'].append(E("String Museum","Display shelving in the String range, designed by TAF Studio.","String Furniture","2018",cat,"2010s"))
ms['x'].append(E("String Pira G2","Shelving in the String range, designed by Anna von Schewen and Björn Dahlström.","String Furniture","2023",cat,"2020s"))
ms['x'].sort(key=lambda e:(e.get('g','~'),yr(e),e['n']))
for e in find(d,'Mattress')['x']:
    if e['n']=='Nectar':
        e['d']="Online memory-foam brand launched in 2017 by Resident (then DreamCloud Holding); Ashley Home bought Resident Home in March 2024. Ultra Hybrid was a Consumer Reports side-sleeper pick."
        e['s']="https://www.retaildive.com/news/ashley-home-acquires-resident-nectar-dreamcloud/709587"
        e['own']="Resident Home Inc. (Ashley Home, Inc.)"; e['own_y']="2024"
def fix(s):
    s=s.replace("MoMA's Design collection searched for chair (3 of 3 pages), table (6 of 8), sofa, stool, bench, shelf, cabinet, desk, bed and screen (page 1 each)","MoMA's Design collection searched for chair (3 of 3 pages), table (6 of 8), sofa, stool, bench and shelf (page 1 each), and for cabinet, desk, bed and screen (all pages: page 2 returns nothing for cabinet, desk and bed, and the screen results beyond page 1 are textiles and posters, not furniture)")
    s=s.replace("Corbusier, Starck and Colombo (first 30 each)","Corbusier, Starck and Colombo (first 30 each) and with Saarinen, Nelson, Pesce, Magistretti, Wegner, Juhl, Sottsass, Arad, Morrison and Eames (every result for each except Eames, whose 74 results were read to the first 32; the Nelson sofa groups are left out)")
    s=s.replace("MoMA pages 2 onward for cabinet, desk, bed and screen (blocked when Firecrawl credits ran out), ","Eames chair results 33 to 74 at the Vitra Design Museum, ")
    s=s.replace("and Thonet and String product lists (Thonet's own pages 404; String's site returns 403 to WebFetch and is queued for Firecrawl)","and the full Thonet product list (the Design Museum's page for the No. 14 was read, Thonet's own pages 404) and the String Outdoor and Center Center ranges (the String story, Pocket and Works pages and the anniversary catalogue were read)")
    return s
def rec(n):
    if isinstance(n,dict):
        if isinstance(n.get('sel'),str): n['sel']=fix(n['sel'])
        for k in('depts','s','k'):
            for x in n.get(k,[]) if isinstance(n.get(k),list) else []: rec(x)
rec(d)
json.dump(d,open('out/B1.json.tmp','w'),ensure_ascii=False,indent=1)
b=json.load(open('out/B1_brands.json'))
for x in b['b']:
    if x['n']=='String Furniture':
        x['d']="Swedish maker of the String shelving system by Nisse and Kajsa Strinning; String Furniture AB was founded in 2004 by Peter Erlandsson and Pär Josefsson, who bought the rights to make and sell it."
        x['s']="https://www.stringfurniture.com/en/our-world/about-string-furniture"
        x['lines']=["String System","String Pocket","Museum","Works","Pira","Relief","Center Center"]
    if x['n']=='Resident Home':
        x['d']="Online mattress group (Nectar, DreamCloud, Awara, Siena), bought by Ashley Home, Inc. in March 2024."
        x['s']="https://www.ashleyfurnitureindustriesllc.com/news/03-04-2024ashleyandresidentannounceacquisition"
json.dump(b,open('out/B1_brands.json.tmp','w'),ensure_ascii=False,indent=1)
