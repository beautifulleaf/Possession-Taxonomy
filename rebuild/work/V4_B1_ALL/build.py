import json,re,sys
sys.path.insert(0,'.')
from rows import R,LC,CP
import rows2, rows3, rows4
base=json.load(open('../../out/B1.json'))
MKT={
"IKEA":("Inter IKEA Systems B.V.","Own label","Sweden",""),
"Knoll":("MillerKnoll","Global group","United States","2021"),
"Herman Miller":("MillerKnoll","Global group","United States",""),
"HAY":("MillerKnoll","Global group","Denmark",""),
"Muuto":("MillerKnoll","Global group","Denmark","2018"),
"Vitra":("Vitra (Fehlbaum family)","Independent","Switzerland",""),
"Artek":("Vitra","Independent","Finland","2013"),
"Fritz Hansen":("Fritz Hansen (privately held)","Independent","Denmark",""),
"Carl Hansen & Søn":("Knud Erik Hansen","Independent","Denmark",""),
"Cassina":("Poltrona Frau Group","Independent","Italy","2005"),
"Kartell":("Felofin","Independent","Italy",""),
"Thonet":("Thonet GmbH","Independent","Germany",""),
"B&B Italia":("Busnelli family","Independent","Italy",""),
"Ligne Roset":("Roset family","Independent","France",""),
"Poltrona Frau":("Haworth Group","Global group","Italy","2014"),
"Flexform":("Galimberti family","Independent","Italy",""),
"Stokke":("NXMH","Independent","Norway","2014"),
}
CH="https://en.wikipedia.org/wiki/"
ROLE={ # (kind,name)->role
("Dining chair","Panton Chair"):"origin",
("Upholstered lounge chair","Eames Lounge Chair and Ottoman"):"landmark",
("Bookcase","Billy"):"landmark",("Armchair","Poäng"):"landmark",
("Bean bag chair","Sacco"):"landmark",("Dining chair","683 chair"):"landmark",("Office chair","Vertebra"):"landmark",
}
SRCFIX={("Bookcase","Billy"):CH+"Billy_(bookcase)",("Armchair","Poäng"):CH+"Po%C3%A4ng",
("Upholstered lounge chair","Eames Lounge Chair and Ottoman"):CH+"Eames_Lounge_Chair",
("Bean bag chair","Sacco"):CP,("Office chair","Vertebra"):CP}
def yearkey(y):
    m=re.search(r'(1[0-9]{3}|20[0-9]{2})',y or '')
    if m: return int(m.group(1))
    m=re.search(r'(\d+)(st|nd|rd|th) century',y or '')
    if m: return (int(m.group(1))-1)*100+50
    if re.search(r'early 1970',y or ''): return 1970
    return None
def grp(yk):
    if yk is None: return "Undated"
    if yk<1900: return "Before 1900"
    return f"{yk//10*10}s"
PATCH={'Mandarin chair':{'y':'1986'},'GJ Chair':{'y':'1963'},'S chair':{'y':'1991'}}
for r in R:
    if r['n'] in PATCH: r.update(PATCH[r['n']])
byk={}
for r in R: byk.setdefault(r['k'],[]).append(r)
MAT=[
dict(n="Tempur-Pedic",a="TEMPUR",mk="Tempur-Pedic",y="1992",d="Memory-foam brand introduced in the US in 1992; Tempur-Pedic acquired Sealy in 2012.",s=CH+"Mattress",own="Somnigroup International",tier="Global group",cty="United States",g="Global group",v=[{"n":"TEMPUR-Adapt","d":"range"},{"n":"TEMPUR-Breeze","d":"range"},{"n":"TEMPUR-Cloud","d":"range"}]),
dict(n="Sealy",a="",mk="Sealy",y="1881",d="US mattress maker bought by Tempur-Pedic in 2012.",s=CH+"Somnigroup",own="Somnigroup International",tier="Global group",cty="United States",own_y="2012",g="Global group",v=[{"n":"Posturepedic","d":"line"},{"n":"Blackwood Elevate Posturepedic","d":"range"}]),
dict(n="Sleep Number",a="Select Comfort",mk="Sleep Number",y="1987",d="Founded as Select Comfort; renamed Sleep Number in November 2017; adjustable air beds.",s=CH+"Sleep_Number",own="SNBR Inc. (Sleep Country Canada)",tier="Independent",cty="United States",own_y="2026",g="Independent"),
dict(n="Casper",a="",mk="Casper",y="2014",d="Direct-to-consumer brand founded 22 April 2014; revenue $439.258 million in 2019.",s=CH+"Casper_Sleep",own="Carpenter Co.",tier="Independent",cty="United States",own_y="2024",g="Independent"),
dict(n="Simba",a="Simba Sleep",mk="Simba",y="2015",d="London-based online mattress brand, privately held.",s=CH+"Simba_Sleep",own="Simba Sleep",tier="Independent",cty="United Kingdom",g="Independent",v=[{"n":"Hybrid","d":"range"},{"n":"Hybrid Luxe","d":"range"},{"n":"Hybrid Essential","d":"range"}]),
dict(n="Hypnos",a="Hypnos Beds",mk="Hypnos",y="1904",d="British bed maker with a royal warrant held without a break since 1929.",s=CH+"Hypnos_Beds",own="owner not stated",tier="Independent",cty="United Kingdom",g="Independent"),
dict(n="Vispring",a="Vi-Spring",mk="Vispring",y="1901",d="Plymouth maker of handmade pocket-coil beds, formerly Vi-Spring.",s=CH+"Vispring",own="owner not stated",tier="Independent",cty="United Kingdom",g="Independent"),
dict(n="Hästens",a="Hastens",mk="Hästens",y="1852",d="Swedish bed maker founded by Pehr Adolf Janson as a saddlery; royal purveyor since 1952.",s=CH+"H%C3%A4stens",own="Jan Ryde (family-owned)",tier="Independent",cty="Sweden",g="Independent"),
dict(n="Leesa",a="",mk="Leesa",y="2014",d="US online brand whose Reserve model was a Consumer Reports side-sleeper pick.",s="https://www.hunker.com/2268800/consumer-reports-best-mattress-for-side-sleepers-2026/",own="owner not stated",tier="Independent",cty="United States",g="Independent",v=[{"n":"Reserve","d":"model"}]),
dict(n="Nectar",a="",mk="Nectar",y="2016",d="Online memory-foam brand whose Ultra Hybrid was a Consumer Reports side-sleeper pick.",s="https://www.hunker.com/2268800/consumer-reports-best-mattress-for-side-sleepers-2026/",own="owner not stated",tier="Independent",cty="United States",g="Independent",v=[{"n":"Ultra Hybrid","d":"model"}]),
dict(n="Emma",a="Emma – The Sleep Company",mk="Emma",y="2013",d="Frankfurt direct-to-consumer mattress brand; Haniel agreed to buy 50.1% in April 2020.",s="https://tech.eu/2020/04/06/haniel-buys-emma/",own="Haniel",tier="Independent",cty="Germany",own_y="2020",g="Independent"),
dict(n="Serta",a="",mk="Serta",y="1931",d="US mattress brand under common ownership with Simmons after a private-equity buyout.",s=CH+"Mattress",own="owner not stated",tier="",cty="United States",g="Others"),
dict(n="Simmons",a="Beautyrest",mk="Simmons",y="1870",d="US mattress maker under common ownership with Serta.",s=CH+"Mattress",own="owner not stated",tier="",cty="United States",g="Others",v=[{"n":"Beautyrest","d":"pocket-coil line"}]),
]
KS={ # kind -> (nl, sel, ref, total)
}
CHAIRREF="Wikipedia's List of chairs (first 100,000 of 124,675 characters read; the rest are references) and the 38 Wikidata chairs with a designer (P287)"
def kindtxt(kname,n,ref,total,kindnl,extra=""):
    return kindnl, f"Named designs of {ref} that belong to this kind; generic chair types in the list (barber's, dentist's, electric, sedan, historic styles such as Windsor variants) are types, not entries. {extra}Covers {n} of about {total} in {ref}; Vitra, MoMA, V&A and Design Museum collection lists were not fetched."
NL={
"Sofa":"One entry is a sofa design, named by its maker or designer; sizes and finishes are versions.",
"Armchair":"One entry is an armchair design; sizes and covers are versions.",
"Upholstered lounge chair":"One entry is an upholstered lounge chair design with its maker and designer; shell, leather and size options are versions.",
"Tubular & wire-frame lounge chair":"One entry is a tubular-steel or wire lounge chair design; licensed editions and finishes are versions.",
"Moulded, shell & bentwood lounge chair":"One entry is a moulded, shell or bentwood lounge chair design; materials and editions are versions.",
"Chaise longue":"One entry is a chaise longue design; editions are versions.",
"Dining chair":"One entry is a dining or side chair design with its maker and designer; reissues, colours and sizes are versions.",
"Office chair":"One entry is an office chair design; size and generation changes are versions.",
"Stool":"One entry is a stool design; editions are versions.",
"Dining table":"One entry is a table design; sizes are versions.",
"Coffee table":"One entry is a low-table design; editions are versions.",
"Bed frame":"One entry is a bed design; sizes are versions.",
"Bookcase":"One entry is a bookcase design; sizes and finishes are versions.",
"Mattress":"One entry is a mattress brand sold under its own name; named ranges are versions.",
"Garden bench":"One entry is a garden seat design.",
"Adirondack chair":"One entry is a named garden chair design; regional variants are versions.",
}
def process_entry(x,kname,mkrow=None):
    x=dict(x)
    if x.get('mk') in MKT:
        o,t,c,oy=MKT[x['mk']]; x['own']=o;x['tier']=t;x['cty']=c
        if oy:x['own_y']=oy
    k=(kname,x['n'])
    if k in ROLE: x['role']=ROLE[k]
    if k in SRCFIX: x['s']=SRCFIX[k]
    return x
import re as _re
def nz(x): return _re.sub(r'[^a-z0-9]','',x.lower())
GN=set()
for dp in base['depts']:
    for sh in dp['s']:
        for k in sh['k']:
            for x in k.get('x',[]):
                GN.add(nz(x['n']))
                for al in str(x.get('a','')).split('·'): GN.add(nz(al))
seen=set(GN);keep=[]
for r in R:
    ks={nz(r['n'])}|{nz(t) for t in str(r.get('a','')).split('·') if t.strip()}
    if ks&seen: continue
    seen|=ks;keep.append(r)
R[:]=keep
byk={}
for r in R: byk.setdefault(r['k'],[]).append(r)
cnt={}
for dp in base['depts']:
    for s in dp['s']:
        for k in s['k']:
            k.pop('m',None);k.pop('r',None)
            kn=k['n']
            xs=[dict(x) for x in k.get('x',[])]
            if kn=="Mattress":
                xs=[dict(x) for x in MAT]
            for r in byk.get(kn,[]):
                if r['n'].lower() in {x['n'].lower() for x in xs}: continue
                xs.append({kk:vv for kk,vv in r.items() if kk!='k' and vv not in ("",None,[])} | {"v":r['v']})
            if kn=="Bookcase":
                for x in xs:
                    if x['n']=="Billy": x['d']="IKEA bookcase by Gillis Lundgren, first in the 1979 catalogue; over 140 million sold by 2023."
            if kn=="Armchair":
                for x in xs:
                    if x['n']=="Poäng": x['d']="IKEA armchair by Noboru Nakamura, launched 1976 as Poem; about 30 million made by 2016."
            if not xs:
                continue
            out=[]
            for x in xs:
                x=process_entry(x,kn)
                x.setdefault('v',[]); x.setdefault('a',x.get('a',''))
                if kn!="Mattress":
                    x['g']=grp(yearkey(x.get('y','')))
                for v in x['v']:
                    v.setdefault('d','')
                out.append(x)
            gk=lambda x:(yearkey(x.get('y','')) is None, yearkey(x.get('y','')) or 0, x['n'].lower())
            if kn!="Mattress": out.sort(key=gk)
            k['x']=out
            n=len(out)
            k['nl']=NL.get(kn,"One entry is a named furniture design with its maker and designer; editions and sizes are versions.")
            if kn=="Mattress":
                k['xg']="by market tier"
                k['sel']=("Brands named by the fetched Wikipedia Mattress article (Tempur Sealy, Sleep Number, Casper, Simba, Vispring, Hästens, Serta, Simmons), plus Hypnos, Leesa, Nectar and Emma from their own fetched pages. Covers "+str(n)+" of about 13 brands named; no complete brand list was fetched, so the long tail is missing.")
            else:
                k['xg']="by decade of design"
                k['sel']=(f"Designs named in Wikipedia's List of chairs and Category:Chairs, the Wikidata chairs and museum-held furniture items, MoMA's Design collection searched for chair (3 of 3 pages), table (6 of 8), sofa, stool, bench, shelf, cabinet, desk, bed and screen (page 1 each), the Vitra Design Museum collection searched for chair (page 1 of 1,191 results; the site pages client-side, so later pages could not be read) and for chair with Panton, Jacobsen, Aalto, Breuer, Rietveld, Prouvé, Corbusier, Starck and Colombo (first 30 each), plus table, shelf, bed and cabinet; the V&A API with plywood as material and 1900 onwards (103 chair records and 168 furniture records, read to the end); the Compasso d'Oro page, designer pages and maker pages (Knoll, Herman Miller, Cassina, Fritz Hansen, Artek, B&B Italia, Ligne Roset, Poltrona Frau, Flexform, Vitsœ, HAY, USM, de Sede, &Tradition, GUBI) that belong to this kind. Generic types and historic styles are see-notes. Covers {n} designs in this kind. Not covered: Vitra Design Museum chair results beyond those queries, MoMA pages 2 onward for cabinet, desk, bed and screen (blocked when Firecrawl credits ran out), V&A pieces in other materials, and Thonet, String and Muuto product designs (Thonet 404, String 403, Muuto page names families without designers).")
            cnt[kn]=n
for dp in base['depts']:
    for sh in dp['s']:
        for k in sh['k']:
            for x in k.get('x',[]):
                if x['n']=='Panton Chair' and not any('275' in v['n'] for v in x['v']): x['v'].append({"n":"Thonet Model 275","y":"1965","d":"first production, Thonet; Vitra relaunched it in 1990","mk":"Thonet"})
                if x['n']=='Togo': x['d']='Seating by Michel Ducaroy for Ligne Roset, 1973.'
# nursery entries: ensure market fields
# departments ms
def ms(mkt,who,share,yr,s,note): return {"mkt":mkt,"who":who,"share":share,"yr":yr,"s":s,"note":note}
for dp in base['depts']:
    if dp['n']=="Sofas & armchairs":
        dp['msum']="Furniture is led by retailers and office-furniture groups. IKEA sells the most; MillerKnoll combined Herman Miller and Knoll in 2021 and holds HAY and Muuto. Figures are company revenue, not market share."
        dp['ms']=[
          ms("Global furniture retail","IKEA (Inter IKEA / Ingka)","€45.1 billion",2024,CH+"IKEA","goods sold, financial year 2024; €44.6 billion revenue in 2025"),
          ms("US furniture","Ashley Furniture","US$10.3 billion",2022,CH+"Ashley_Furniture","revenue per the page's infobox; privately owned by Ron and Todd Wanek"),
          ms("US home furnishings retail","Williams-Sonoma, Inc.","US$7.81 billion",2025,CH+"Williams-Sonoma,_Inc.","revenue; brands include Pottery Barn, West Elm"),
          ms("Office and home design furniture","MillerKnoll (Herman Miller, Knoll, HAY, Muuto)","US$3.84 billion",2026,CH+"Herman_Miller_(manufacturer)","revenue, fiscal year ended 30 May 2026"),
        ]
    if dp['n']=="Beds & mattresses":
        dp['msum']="Mattresses are led by Somnigroup (Tempur-Pedic, Sealy) in the US; online brands and British and Swedish makers sit beside it. Figures are revenue or industry size."
        dp['ms']=[
          ms("Global mattress industry","All makers","US$28.5 billion",2018,CH+"Mattress","industry size cited from Grand View Research"),
          ms("Mattresses (Tempur-Pedic, Sealy, Stearns & Foster)","Somnigroup International (Tempur Sealy)","US$4.930 billion",2021,CH+"Somnigroup","revenue, fiscal 2021; renamed Somnigroup in February 2025"),
          ms("US adjustable air beds","Sleep Number","US$1.856 billion",2021,CH+"Sleep_Number","revenue; assets sold to SNBR Inc. in July 2026"),
          ms("US online mattresses","Casper","US$439.258 million",2019,CH+"Casper_Sleep","revenue; owned by Carpenter Co. since 2024"),
        ]
    # kinds without x: empty racks etc. drop 'tt' unchanged
# fix kind-level 'see' for removed Racks? none
part={"replaces":[d['n'] for d in base['depts']],"depts":base['depts'],"brands":[
 {"n":"Muuto","c":"Denmark","f":"2006","seg":"Premium","d":"Copenhagen design brand founded by Kristian Byrge and Peter Bonnen; bought by Knoll in 2018 for US$300 million.","s":CH+"Muuto","kf":"Scandinavian design"},
 {"n":"Hypnos","c":"United Kingdom","f":"1904","seg":"Premium","d":"British bed maker in Princes Risborough with a royal warrant since 1929.","s":CH+"Hypnos_Beds","kf":"handmade beds"},
 {"n":"Vispring","c":"United Kingdom","f":"1901","seg":"Premium","d":"Plymouth maker of handmade pocket-coil beds, formerly Vi-Spring.","s":CH+"Vispring","kf":"handmade beds"},
 {"n":"Hästens","c":"Sweden","f":"1852","seg":"Premium","d":"Köping bed maker founded as a saddlery; royal purveyor since 1952.","s":CH+"H%C3%A4stens","kf":"handmade beds"},
 {"n":"Tecno","c":"Italy","seg":"Premium","d":"Maker of the Nomos table and desk system, Compasso d'Oro 1987.","s":CP,"kf":"office furniture"},
 {"n":"Bonacina","c":"Italy","seg":"Premium","d":"Maker of Franco Albini's Gala armchair and Margherita chair per Wikidata.","s":"https://www.wikidata.org/wiki/Q60616602","kf":"woven furniture"},
 {"n":"Gispen","c":"Netherlands","seg":"Heritage manufactory","d":"Maker of Willem Hendrik Gispen's 407 chair.","s":"https://www.wikidata.org/wiki/Q26220572","kf":"tubular steel furniture"},
 {"n":"Fiam Italia","c":"Italy","seg":"Premium","d":"Maker of the Ghost chair by Cini Boeri and Tomu Katayanagi, 1987.","s":"https://www.wikidata.org/wiki/Q140429531","kf":"glass furniture"},
 {"n":"Studio Alchimia","c":"Italy","seg":"Designer","d":"Producer of Alessandro Mendini's Proust armchair, 1978.","s":"https://www.wikidata.org/wiki/Q21234427","kf":"radical design"},
 {"n":"Flexform","c":"Italy","f":"1959","seg":"Premium","d":"Meda furniture maker founded by the Galimberti brothers; family-run.","s":CH+"Flexform","kf":"upholstered furniture"},
 {"n":"Emma","c":"Germany","f":"2013","seg":"Mainstream","d":"Frankfurt online mattress brand; Haniel took 50.1% in 2020.","s":"https://tech.eu/2020/04/06/haniel-buys-emma/","kf":"mattresses"},
 {"n":"Isokon","c":"United Kingdom","seg":"Heritage manufactory","d":"Maker named for the Long Chair after Marcel Breuer, 1935-36.","s":CH+"Marcel_Breuer","kf":"plywood furniture"},
 {"n":"Adico","c":"Portugal","seg":"Heritage manufactory","d":"Maker of the Portuguese chair (5008) from the 1930s.","s":LC,"kf":"Portuguese chairs"},
],"brand_updates":{b:{"own":v[0],"tier":v[1],"c":v[2]} for b,v in MKT.items() if b not in("Muuto",)},"renames":{},"moves":[]}
# brand updates only for names in register
reg={b['n'] for b in json.load(open('../../out/B1_brands.json'))['b']}
part['brand_updates']={b:u for b,u in part['brand_updates'].items() if b in reg}
for b,u in [("Tempur-Pedic",("Somnigroup International","Global group","United States")),("Sealy",("Somnigroup International","Global group","United States")),("Sleep Number",("SNBR Inc. (Sleep Country Canada)","Independent","United States")),("Casper",("Carpenter Co.","Independent","United States")),("Simba",("Simba Sleep","Independent","United Kingdom"))]:
    if b in reg: part['brand_updates'][b]={"own":u[0],"tier":u[1],"c":u[2]}
json.dump(part,open('../../out/B1_parts/ALL.json','w'),ensure_ascii=False)
tot=sum(cnt.values());print(cnt,tot)
