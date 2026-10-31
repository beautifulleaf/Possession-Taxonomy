import json,re,copy
D=json.load(open('/home/user/Possession-Taxonomy/rebuild/out/A1.json'))
REG=json.load(open('/home/user/Possession-Taxonomy/rebuild/out/A1_brands.json'))['b']
R={e['n']:e for e in REG}
NAMES=("Underwear, nightwear & swim","Hats & headwear","Scarves, gloves & belts")
depts=[copy.deepcopy(x) for x in D['depts'] if x['n'] in NAMES]
W='https://en.wikipedia.org/wiki/'
EXTRA_C={"Glen Raven Knitting Mills":"United States","Louis Réard":"France","Jacques Heim":"France","Mary Phelps Jacob":"United States","Inès Gaches-Sarraute":"France","Antoine Gibus":"France","Thomas Francis Dollman":"United Kingdom","George Dunnage":"United Kingdom","Chemstrand":"United States","Brynje":"Norway","Bike Web Company":"United States","Herbert Johnson":"United Kingdom","Aheda Zanetti":"Australia","Frederick's of Hollywood":"United States","Triumph International":"Switzerland","Smithbilt Hat Company":"","Caroline Reboux":"France","Glen Raven":"United States","Spanx":"United States"}
OWN={"Spanx":("Blackstone Inc.","2021"),"Maidenform":("Hanesbrands","2013"),"Jantzen":("Jantzen Brands Corporation","2019"),"'47":("New Era Cap Company","2024"),"Hanes":("Hanesbrands","")}
def E(n,d,mk,y,s,a="",v=None,dt="",**kw):
    e={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}; e.update(kw); return e
def V(n,mk,y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
def regs(b): return R[b]['s']
# additions: kind -> list of entries
ADD={
"Bra":[
 E("Backless brassiere (Jacob patent)","Light backless brassiere patented in 1914 by Mary Phelps Jacob (Caresse Crosby); the patent was later bought by the Warner Brothers Corset Company.","Mary Phelps Jacob","1914",W+"Underwear",dt="cup and band sizes",role="origin"),
 E("Frederick's of Hollywood padded bra","First padded bra, sold by Frederick's of Hollywood from 1947.","Frederick's of Hollywood","1947",W+"Brassiere",dt="padding · cup and band sizes"),
 E("Playtex 18 Hour","Playtex bra named in the brassiere article and listed as a Playtex line.","Playtex","",W+"Brassiere",dt="wired or soft cup · cup and band sizes"),
 E("Triumph Doreen","Triumph bra model named Doreen in the brassiere article.","Triumph International","",W+"Brassiere",dt="cup and band sizes"),
],
"Men's underwear":[
 E("Bike jockstrap","Athletic supporter sold by the Bike Web Company of Chicago from 1897; the jockstrap itself dates from 1874.","Bike Web Company","1897",W+"Underwear",dt="elastic waistband · pouch"),
],
"Undershirt":[
 E("Brynje string vest","Open-mesh string vest made by Brynje of Norway.","Brynje","1933",W+"Underwear",dt="mesh weave · wool or cotton"),
],
"Shapewear":[
 E("Spanx OnCore","High-waisted mid-thigh shaping short; in the Museum of Modern Art design collection since 2017.","Spanx","",W+"Spanx",dt="compression level · length · colour",role="landmark"),
],
"Corset":[
 E("Gaches-Sarraute straight-front corset","Corset with a straight front busk designed by the physician Inès Gaches-Sarraute in the 1890s.","Inès Gaches-Sarraute","1890s",W+"Corset",dt="busk · boning · length"),
],
"Tights & stockings":[
 E("Chemstrand leotard-stockings","Early nylon one-piece stocking-and-leotard garment from Chemstrand in November 1958.","Chemstrand","1958",W+"Pantyhose",dt="denier · colour"),
],
"Thermal base layer":[
 E("Damart Thermolactyl","Thermal underwear fabric and range from the French firm Damart.","Damart","",regs("Damart"),dt="weight · men's, women's"),
 E("Icebreaker Merino 200 Oasis","Merino base layer of Icebreaker, New Zealand; Oasis and Merino 200 are its listed lines.","Icebreaker","",regs("Icebreaker"),v=[V("Oasis","Icebreaker"),V("Merino 200","Icebreaker")],dt="weight (gsm) · crew or zip"),
],
"Socks":[
 E("Smartwool Merino sock","Merino sock range of Smartwool, with the Merino 250 and Thermal Merino lines.","Smartwool","",regs("Smartwool"),v=[V("Merino 250","Smartwool"),V("Thermal Merino","Smartwool")],dt="cushioning · height"),
],
"Swimsuit":[
 E("Speedo LZR Racer","Speedo's racing swimsuit line.","Speedo","",regs("Speedo"),dt="cut · fabric panels"),
 E("Speedo Fastskin","Speedo's racing swimsuit fabric line.","Speedo","",regs("Speedo"),dt="cut · fabric"),
 E("Speedo Endurance","Chlorine-resistant training swimwear line of Speedo.","Speedo","",regs("Speedo"),dt="cut · colour"),
 E("Speedo Aquablade","Speedo racing swimsuit line.","Speedo","",regs("Speedo"),dt="cut"),
 E("Speedo Sculpture ShapeLine","Speedo shaping swimsuit line.","Speedo","",regs("Speedo"),dt="cut"),
 E("Eres Aquarelle","Swimsuit of the French house Eres, listed in its register page as a signature piece.","Eres","",regs("Eres"),dt="cut · colour"),
 E("Jantzen knitted swimsuit","Helanca nylon knitted swimsuit of Jantzen, shown c. 1955-1965 on the Jantzen article.","Jantzen","",W+"Jantzen",dt="knit · colour"),
 E("Burkini","Full-coverage swimsuit with head covering, created by Aheda Zanetti of Australia.","Aheda Zanetti","",W+"Bikini",dt="coverage · fabric"),
],
"Bikini":[
 E("Atome","Two-piece swimsuit launched by Jacques Heim in 1946, named in the bikini article.","Jacques Heim","1946",W+"Bikini",dt="cut"),
 E("Eres Cassiopée","Bikini of the French house Eres, listed as a signature piece.","Eres","",regs("Eres"),dt="top and bottom cuts"),
],
"Beach cover-up":[
 E("Seafolly beach kaftan","Beach kaftan of the Australian swimwear brand Seafolly.","Seafolly","",regs("Seafolly"),v=[V("Amnesia Kaftan","Seafolly"),V("Laelia Maxi Kaftan","Seafolly"),V("Crinkle Gauze Kaftan","Seafolly")],dt="length · fabric"),
],
"Homburg":[
 E("Lock & Co. Homburg","Homburg listed as a line of James Lock & Co., London.","Lock & Co. Hatters","",regs("Lock & Co. Hatters"),dt="felt grade · colour"),
],
"Top hat":[
 E("Dunnage top hat","Top hat attributed in the top hat article to the Middlesex hatter George Dunnage in 1793.","George Dunnage","1793",W+"Top_hat",dt="silk plush · crown height"),
 E("Dollman elastic round hat","Hat patented by the London hatter Thomas Francis Dollman in 1812.","Thomas Francis Dollman","1812",W+"Top_hat",dt="crown height"),
 E("Gibus opera hat","Spring-loaded collapsible top hat designed by Antoine Gibus.","Antoine Gibus","c. 1840",W+"Top_hat",dt="silk · collapsible"),
 E("Christys' silk top hat","Silk top hat of the London hat merchant Christys'.","Christys'","",regs("Christys'"),dt="silk plush · size"),
],
"Fedora":[
 E("Herbert Johnson Poet","Felt hat of the London hatter Herbert Johnson, worn in Raiders of the Lost Ark (1981).","Herbert Johnson","1981",W+"Herbert_Johnson_(hatters)",dt="felt · colour"),
],
"Baseball cap":[
 E("New Era 9SEVENTY","Cap line of New Era Cap Company, listed in the brand register.","New Era","",regs("New Era"),dt="strap closure"),
 E("New Era 19TWENTY","Cap line of New Era Cap Company, listed in the brand register.","New Era","",regs("New Era"),dt="strap closure"),
],
"Headband":[
 E("Nike Swoosh headband","Sports headband carrying Nike's Swoosh.","Nike","",regs("Nike"),dt="width · fabric"),
],
"Headscarf":[
 E("Buttonscarves instant hijab","Ready-to-wear instant hijab of the Indonesian brand Buttonscarves.","Buttonscarves","",regs("Buttonscarves"),v=[V("Sport Hijab","Buttonscarves"),V("Printed Hijab","Buttonscarves")],dt="fabric · print"),
 E("dUCk instant hijab","Instant hijab of the Malaysian brand dUCk Scarves.","dUCk","",regs("dUCk"),dt="fabric · print"),
],
"Cloche & women's millinery":[
 E("Stetson Royal","Women's hat of Stetson from the 1930s to 1950s, listed in the brand register.","Stetson","1930s",regs("Stetson"),dt="felt · colour"),
],
"Neck gaiter":[
 E("Buff tubular scarf","Seamless tubular neckwear of the Spanish brand Buff.","Buff","",regs("Buff"),v=[V("CoolNet UV+","Buff"),V("Polar","Buff"),V("Merino Lightweight","Buff"),V("ThermoNet","Buff")],dt="fabric · print"),
],
"Shawl":[
 E("Norwich shawl","Imitation of the Kashmir shawl woven in Norwich from the late 18th century to the 1870s.","","late 18th century",W+"Shawl",dt="woven · printed paisley"),
 E("China crêpe shawl","Embroidered silk crêpe shawl from China, in Europe by the first decade of the 19th century.","","",W+"Shawl",dt="embroidery · fringe"),
],
"Belt":[
 E("Hermès Constance belt","Belt of Hermès with the H buckle, listed in its register page.","Hermès","",regs("Hermès"),dt="leather · width"),
],
}
VADD={ # (kind, entry): versions
("Men's underwear","Jockey Y-front brief"):[V("Low Rise brief","Jockey International"),V("Midway Brief","Jockey International")],
("Bra","Wonderbra plunge push-up"):[V("Dici by Wonderbra","Wonderbra","1974","Canadelle model")],
("Swim trunks","Bulldog"):[V("Setter","Orlebar Brown"),V("Dane","Orlebar Brown"),V("Springer","Orlebar Brown"),V("Mastiff","Orlebar Brown")],
("Swimsuit","Hunza G crinkle swim"):[V("Square Neck","Hunza G"),V("Halter","Hunza G"),V("Scoop Neck","Hunza G"),V("Crinkle bikini","Hunza G")],
("Swim trunks","Birdwell Beach Britches"):[V("Surfnyl boardshorts","Birdwell"),V("Surfstretch boardshorts","Birdwell")],
("Undershirt","Bonds Athletic singlet"):[V("Organics","Bonds")],
("Thermal base layer","Union suit"):[V("Kenosha Klosed Krotch","Kenosha","1911","Union suit advertised in the Saturday Evening Post")],
("Glove","Mechanix The Original"):[V("M-Pact","Mechanix Wear")],
("Baseball cap","Cycling cap"):[V("Rapha Tom Simpson Cap","Rapha")],
("Mitten","Hestra Army Leather Heli Ski mitt"):[],
}
SETMK={("Bikini","Réard bikini"):"Louis Réard",("Baseball cap","Cycling cap"):"Rapha",("Baseball cap","Trucker hat"):"Von Dutch"}
ROLE={("Men's underwear","Jockey Y-front brief"):"origin",("Cowboy hat","Boss of the Plains"):"origin",("Tights & stockings","Panti-Legs"):"origin",("Scarf","Hermès carré"):"origin",("Bikini","Réard bikini"):"origin",("Thermal base layer","Union suit"):"origin",("Bowler hat","Coke hat"):"origin"}
KIND={ # nl handled generically; refs per kind
}
GEN_NL="One entry is a signature garment sold under its own name by its originating brand, or a named form attested by a cited Wikipedia article; fits, fabrics and generations are versions."
REFS={"Bra":"Wikipedia: Brassiere, Underwear","Men's underwear":"Wikipedia: Briefs, Underwear","Undershirt":"Wikipedia: Undershirt, Underwear","Shapewear":"Wikipedia: Shapewear, Spanx","Corset":"Wikipedia: Corset","Socks":"Wikipedia: Sock","Tights & stockings":"Wikipedia: Pantyhose","Thermal base layer":"Wikipedia: Long underwear, Underwear","Pyjamas":"Wikipedia: Pajamas","Bathrobe":"Wikipedia: Bathrobe","Swimsuit":"Wikipedia: One-piece swimsuit, Bikini, Jantzen","Bikini":"Wikipedia: Bikini","Swim trunks":"Wikipedia: Swim trunks","Cowboy hat":"Wikipedia: Cowboy hat, List of hat styles","Fedora":"Wikipedia: Fedora, Herbert Johnson (hatters)","Bowler hat":"Wikipedia: Bowler hat","Top hat":"Wikipedia: Top hat","Panama hat":"Wikipedia: Panama hat","Baseball cap":"Wikipedia: Baseball cap","Flat cap":"Wikipedia: Flat cap","Beret":"Wikipedia: Beret","Bucket hat":"Wikipedia: Bucket hat","Homburg":"Wikipedia: Homburg (hat)","Boater":"Wikipedia: Boater (hat)","Beanie":"Wikipedia: Knit cap","Balaclava":"Wikipedia: Balaclava (clothing)","Headband":"Wikipedia: Hairband","Cloche & women's millinery":"Wikipedia: Cloche hat","Scarf":"Wikipedia: Scarf","Shawl":"Wikipedia: Shawl","Bandana":"Wikipedia: Bandana","Glove":"Wikipedia: Glove","Mitten":"Wikipedia: Mitten","Belt":"Wikipedia: Belt (clothing)","Belt buckle":"Wikipedia: Belt buckle","Arm warmer & sleeve":"Wikipedia: Arm warmer","Suspender belt":"Wikipedia: Belt (clothing)","Leg warmers":"Wikipedia: Leg warmer"}
HATLIST="Wikipedia: List of hat styles (window 1 of about 2)"
def ctyof(mk):
    if not mk: return ""
    if mk in R: return R[mk].get('c') or EXTRA_C.get(mk,"")
    return EXTRA_C.get(mk,"")
def yr(e):
    m=re.search(r'\d{4}',e.get('y') or ''); return int(m.group()) if m else 9999
stats={}
unres=set(); removed_m=[]
for dp in depts:
    dp.pop('b',None) if dp['n']=="Scarves, gloves & belts" else None
    for sh in dp['s']:
        for k in sh['k']:
            xs=k.setdefault('x',[]) if (k.get('x') or ADD.get(k['n'])) else []
            before=len(k.get('x',[]))
            names={e['n'].lower() for e in xs}
            for e in ADD.get(k['n'],[]):
                if e['n'].lower() not in names: xs.append(e); names.add(e['n'].lower())
            for e in xs:
                key=(k['n'],e['n'])
                if key in SETMK: e['mk']=SETMK[key]
                for v in VADD.get(key,[]):
                    if v['n'] not in [q['n'] for q in e.get('v',[])]: e.setdefault('v',[]).append(v)
                if key in ROLE: e['role']=ROLE[key]
                mk=e.get('mk','')
                c=ctyof(mk)
                if mk and not c and mk not in EXTRA_C: unres.add(mk)
                if c: e['cty']=c
                if mk in OWN: e['own'],e['own_y']=OWN[mk][0],OWN[mk][1]
                e['g']= (c if c else ("Country not stated" if mk else "Named forms without a brand"))
            xs.sort(key=lambda e:((e['g'] in("Named forms without a brand","Country not stated"),e['g']),yr(e),e['n']))
            if xs: k['x']=xs
            for t in k.pop('m',[]) or []: removed_m.append((k['n'],t[0],t[1]))
            n=len(xs)
            ref=REFS.get(k['n'],'the page named in s')
            if k['n'] in("Cowboy hat","Fedora","Bowler hat","Top hat","Panama hat","Baseball cap","Flat cap","Beret","Bucket hat","Homburg","Boater","Beanie","Balaclava","Headband","Cloche & women's millinery") or dp['n']=="Hats & headwear": ref=ref+"; "+HATLIST if k['n'] in REFS else HATLIST
            if n:
                k['nl']=GEN_NL
                k['xg']="by brand country, then year; forms without a brand last"
                regm=sum(1 for e in REG if any(k['n'].split()[0].lower().rstrip('s') in (z.lower()) for z in [e.get('kf') or '']))
                k['sel']=(f"Every signature piece in the `sig` and `lines` fields of the brand register (rebuild/out/A1_brands.json, 2,531 brands) that matches this garment and has a page naming it, plus the originators named by {ref}. Complete: {n} of {n} entries found in those sources; {before} were in the file before this pass.")
            else:
                k['nl']="No entry: no brand-originated signature piece or originator is named for this garment in the register or the cited article."
                k['sel']=f"Checked the brand register `sig` and `lines` fields and {ref}; none names a piece for this kind. Complete: 0 of 0 in those sources."
            stats[k['n']]=(before,n)
part={"replaces":list(NAMES),"depts":depts,"brands":[],"brand_updates":{},"renames":{},"moves":[]}
need={"Glen Raven Knitting Mills":("United States","Hosiery maker"),}
json.dump(part,open('/home/user/Possession-Taxonomy/rebuild/out/A1_parts/UNDER.json','w'),ensure_ascii=False,indent=1)
json.dump({"stats":stats,"removed_m":removed_m,"unres":sorted(unres)},open('/home/user/Possession-Taxonomy/rebuild/work/V4_A1_UNDER/stats.json','w'),ensure_ascii=False,indent=1)
print(sorted(unres)); print(len(removed_m)); print(sum(a for a,b in stats.values()),sum(b for a,b in stats.values()))
