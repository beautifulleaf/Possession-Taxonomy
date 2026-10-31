import json,csv,re,copy
BASE='/home/user/Possession-Taxonomy/'
P=json.load(open(BASE+'rebuild/out/A1_parts/UNDER.json'))
REG={e['n']:e for e in json.load(open(BASE+'rebuild/out/A1_brands.json'))['b']}
NF=json.load(open(BASE+'rebuild/work/V4_A1_UNDER/nf_check.json'))
rows=list(csv.DictReader(open(BASE+'data/named_forms.tsv'),delimiter='\t',quoting=csv.QUOTE_NONE))
W='https://en.wikipedia.org/wiki/'
LIST=W+'List_of_hat_styles'
def E(n,d,mk,y,s,a="",v=None,dt="",g=None,**kw):
    e={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
    if g: e['g']=g
    e.update(kw); return e
def V(n,mk,y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
K={}
for dp in P['depts']:
    for sh in dp['s']:
        for k in sh['k']: K[k['n']]=(dp,sh,k)
def allnames():
    s=set()
    for dp,sh,k in K.values():
        s.add(k['n'].lower())
        for e in k.get('x',[]):
            s.add(e['n'].lower())
            for a in re.split(r'\s*·\s*',e.get('a') or ''): 
                if a: s.add(a.lower())
    return s
def add(kind,e):
    dp,sh,k=K[kind]
    xs=k.setdefault('x',[])
    if e['n'].lower() in {x['n'].lower() for x in xs}: return False
    xs.append(e); return True
def newkind(shelf,name,d,tt,s,a=""):
    for dp in P['depts']:
        for sh in dp['s']:
            if sh['n']==shelf:
                k={"n":name,"a":a,"d":d,"s":s,"tt":tt,"x":[]}
                sh['k'].append(k); K[name]=(dp,sh,k); return
    raise Exception(shelf)
# --- new kinds
newkind("Regional, ceremonial & uniform headwear","Regional brimmed hat","Brimmed hat tied to a region or country, such as the sombrero, the chupalla or the Chinese damao.",[["Material",["Straw","Felt","Bamboo","Cloth"]],["Region",["Americas","Europe","East Asia","South Asia","Middle East"]]],LIST,"national brimmed hat")
newkind("Regional, ceremonial & uniform headwear","Regional cap","Close-fitting or brimless cap tied to a region, people or court, such as the Glengarry, the songkok or the Chinese guapi mao.",[["Material",["Wool","Felt","Fur","Cloth"]],["Region",["Europe","Middle East","South Asia","Southeast Asia","East Asia","Africa"]]],LIST,"national cap")
newkind("Regional, ceremonial & uniform headwear","Novelty & costume hat","Hat worn for celebration, costume, school punishment or a trade, such as the party hat, the dunce cap or the chef's toque.",[["Use",["Celebration","Costume","Trade","Punishment"]]],LIST,"party hat · costume hat")
# --- restore from named_forms.tsv
rm=json.load(open(BASE+'rebuild/work/V4_A1_UNDER/stats.json'))['removed_m']
ridx={}
for r in rows: ridx.setdefault((r['name'].strip().lower()),[]).append(r)
def nfrow(kind,name,mk):
    mkn=re.sub(r'[^a-z0-9]','',mk.lower())
    for r in ridx.get(name.strip().lower(),[]):
        mm=re.sub(r'[^a-z0-9]','',r['maker_id'].lower())
        if mkn and (mkn in mm or mkn[:4] in mm): return r
        if mk=='Björn Borg' and r['maker_id']=='M-bjorn-borg': return r
    return None
restored=[];dropped=[]
have=lambda kind,name:any(x['n'].lower()==name.lower() or any(v['n'].lower()==name.lower() for v in x.get('v',[])) for x in K[kind][2].get('x',[]))
onia=[]
for kind,name,mk in rm:
    r=nfrow(kind,name,mk)
    if not r or kind not in K: dropped.append((kind,name,mk)); continue
    url=r['sources'].split(' | ')[0]; y=r['first_year']
    if mk=='Onia': onia.append((name,url)); continue
    if have(kind,name): restored.append((kind,name,mk,'already present')); continue
    if mk=='Jockey International':
        for x in K[kind][2]['x']:
            if x['mk']==mk and name in('Low Rise brief','Midway Brief'): x['v'].append(V(name,mk,y)); break
        else: add(kind,E(f"{mk} {name}",'',mk,y,url,dt=''))
        restored.append((kind,name,mk,'version')); continue
    n=name if (mk.lower().split()[0] in name.lower() or len(name.split())>=3) else f"{mk} {name}"
    add(kind,E(n,(f"First listed {y}." if y else ""),mk,y,url,a=name if n!=name else ""))
    restored.append((kind,name,mk,'entry'))
if onia:
    add("Swim trunks",E("Onia swim trunks","",'Onia',"",onia[0][1],v=[V(n,'Onia') for n,u in onia]))
    restored.append(('Swim trunks','Onia x4','Onia','entry+versions'))
# --- unplaced lines
for x in K["Flat cap"][2]['x']:
    if x['n']=="Kangol 504":
        x['v']+= [V("Tropic","Kangol","","fabric option on the 504"),V("Furgora","Kangol","","angora-wool fabric option on the 504")]
add("Flat cap",E("Lock & Co. Whitebridge","",'Lock & Co. Hatters',"",REG['Lock & Co. Hatters']['s']))
add("Socks",E("Heat Holders thermal sock","",'Heat Holders',"","https://www.heatholders.com/collections/womens-headbands-earmuffs",v=[V("Alta","Heat Holders"),V("Jordan","Heat Holders")],dt="thermal pile lining"))
add("Cowboy hat",E("Resistol cowboy hat","",'Resistol',"",W+'Resistol',v=[],dt="felt grade · straw"))
# braces kind
dp,sh,_=K["Belt"]
braces={"n":"Braces","a":"suspenders","d":"Pair of straps worn over the shoulders to hold trousers up.","s":REG['Albert Thurston']['s'],"tt":[["Fastening",["Clip","Button"]],["Material",["Elastic webbing","Boxcloth","Barathea","Leather"]]],"x":[
 E("Albert Thurston braces","",'Albert Thurston',"",REG['Albert Thurston']['s'],v=[V("Boxcloth braces","Albert Thurston"),V("Barathea braces","Albert Thurston")],dt="button or clip"),
 E("Trafalgar braces","",'Trafalgar',"","https://www.trafalgarstore.com/collections/braces-suspenders",dt="elastic · width")]}
sh['k'].append(braces); K["Braces"]=(dp,sh,braces)
# --- hat list
HL=[ # kind,name,region,desc
("Regional brimmed hat","Breton","Brittany, France","Women's hat with a round crown and a deep, upturned brim."),
("Regional brimmed hat","Buntal hat","Philippines","Finely woven buri palm straw hat, often mistaken for the Panama hat."),
("Regional brimmed hat","Chupalla","Chile","Straw hat made in Chile."),
("Regional brimmed hat","Damao","China","Traditional Chinese men's hat in many styles."),
("Regional brimmed hat","Humao","China","Brimmed hat worn by Chinese men and women when riding."),
("Regional brimmed hat","Gaitou hat","China","Traditional Chinese women's hat worn when riding or trading cloth."),
("Regional brimmed hat","Liangmao","China","Traditional Chinese women's hat."),
("Regional brimmed hat","Weimao","China","Wide-brimmed Chinese hat with a shoulder-length veil."),
("Regional brimmed hat","Jaapi","Assam, India","Traditional Assamese hat, plain or decorated."),
("Regional brimmed hat","Kova tembel","Israel","Cloth hat worn by Israeli pioneers and kibbutzniks."),
("Regional brimmed hat","Mathal","Bangladesh","Bamboo farmer's hat with a conical top."),
("Regional brimmed hat","Sombrero","Mexico","Embroidered felt hat with a conical crown and very wide brim."),
("Regional brimmed hat","Sombrero cordobés","Córdoba, Spain","Flat-brimmed, flat-topped hat linked to flamenco."),
("Novelty & costume hat","Umbrella hat","",""),
("Historical hat & bonnet","Capotain","England and north-west Europe","Tall-crowned, narrow-brimmed conical hat worn from the 1590s to the 1640s."),
("Historical hat & bonnet","Cavalier hat","17th-century Europe","Wide-brimmed hat popular in 17th-century Europe."),
("Historical hat & bonnet","Hennin","Medieval Europe","Women's medieval hat, including conical princess styles."),
("Historical hat & bonnet","Bicorne","Europe","Folded-brim felt hat linked to Napoleon-era officers."),
("Historical hat & bonnet","Bycocket","Robin Hood tradition","Hat turned up behind and pointed in front."),
("Historical hat & bonnet","Coal scuttle bonnet","","Woman's bonnet with a stiffened brim and flat back."),
("Historical hat & bonnet","Poke bonnet","","Woman's bonnet with a small crown and wide rounded brim."),
("Historical hat & bonnet","Tricorne","18th-century Europe","Soft hat pinned up on three sides to form a triangle."),
("Historical hat & bonnet","Boudoir cap","","Decorative cap worn with sleepwear or lingerie in the 19th and early 20th centuries."),
("Historical hat & bonnet","Widow's cap","","Cap worn by women after their husbands' deaths."),
("Historical hat & bonnet","Smoking cap","","Soft embroidered cap worn by men while smoking."),
("Cloche & women's millinery","Cartwheel hat","","Wide, shallow-crowned hat worn at an angle; peaked in the 1940s and 1950s."),
("Cloche & women's millinery","Halo hat","","Semi-circular design that frames the face."),
("Cloche & women's millinery","Mushroom hat","","Hat with a downward brim resembling a mushroom."),
("Cloche & women's millinery","Picture hat","","Elaborate wide-brimmed women's hat, also called a Gainsborough."),
("Cloche & women's millinery","Peach basket hat","","Women's hat shaped like an upturned fruit basket, early 1900s."),
("Cloche & women's millinery","Half hat","","Millinery covering only half the head, popular in the 1950s."),
("Cloche & women's millinery","Fascinator","","Small decorative hat of feathers, flowers or beads."),
("Cloche & women's millinery","Pillbox hat","","Small hat with upright sides and a flat crown, no brim."),
("Sun hat","Wideawake","","Broad-brimmed felt countryman's hat with a low crown."),
("Sun hat","Planter's hat","","Lightweight straw hat with a wide brim and dented crown."),
("Sun hat","Legionnaire","","Hat that protects the forehead, ears and neck from the sun."),
("Sun hat","Sailor hat","","Flat-crowned straw hat inspired by 19th-century sailors' headgear."),
("Clerical hat","Cappello romano","Roman Catholic clergy","Round, wide-brimmed hat worn by traditional Catholic clergy."),
("Clerical hat","Shovel hat","Anglican clergy","Wide-brimmed hat curving forward and back, linked to clergy."),
("Clerical hat","Mitre","Catholic, Orthodox and Anglican churches","Hat worn by bishops."),
("Clerical hat","Capirote","Spain","Conical penitent's hat worn in Holy Week processions."),
("Uniform headwear","Campaign hat","United States","Broad-brimmed felt or straw hat with a four-corner pinched crown."),
("Uniform headwear","Hardee hat","United States (Civil War)","Regulation hat for Union soldiers in the Civil War."),
("Uniform headwear","Slouch hat","Military","Wide-brimmed hat with a felt crown often worn by military leaders."),
("Uniform headwear","Custodian helmet","United Kingdom","Helmet traditionally worn by British police on foot patrol."),
("Uniform headwear","Budenovka","Soviet Union","Woollen hat covering the ears and neck, worn by Soviet troops."),
("Uniform headwear","Garrison cap","Military","Foldable cloth cap with straight sides and a creased crown."),
("Uniform headwear","Patrol cap","Military","Soft field cap with a stiff visor, worn when combat helmets are not needed."),
("Uniform headwear","Peaked cap","Military","Sloping-crown cap with a band and peak, used by militaries and uniformed services."),
("Uniform headwear","Rogatywka","Poland","Polish field cap worn by partisans and officers."),
("Uniform headwear","Utility cover","United States Navy","Eight-pointed hat used by US Navy branches."),
("Uniform headwear","Busby","Military","Small fur military hat."),
("Uniform headwear","Sailor cap (gob cap)","Navies","White canvas cap with an upright brim."),
("Uniform headwear","Sailor cap (round)","Navies","Round, flat, visorless sailor's hat."),
("Academic cap","Student cap","Europe","Cap worn by university students in several European countries."),
("Academic cap","Tudor bonnet","United Kingdom","Soft academic cap with a stiff brim and tasselled cord."),
("Flat cap","Ascot cap","","Hard men's cap dating to the 1900s."),
("Flat cap","Newsboy cap","","Casual cap with a rounder eight-panel body and stiff peak."),
("Flat cap","Gatsby cap","New York","Eight-panel soft cap popular after 1900, also called the newsboy cap."),
("Baseball cap","Cricket cap","","Soft cap traditionally worn by cricket players."),
("Visor","Sports visor","","Crownless headgear similar to a baseball cap."),
("Visor","Green eyeshade","","Visored eyeshade once worn by office clerks."),
("Fur hat","Karakul","Central and South Asia","Hat made from Karakul sheep fur."),
("Fur hat","Kołpak","Polish-Lithuanian Commonwealth","Nobleman's fur hat with a front cut forming two horns."),
("Fur hat","Kolpik","Hasidic Judaism","Cylindrical brown fur hat worn by some rabbis."),
("Fur hat","Telpek","Turkmenistan","Traditional sheepskin and fur headgear."),
("Fur hat","Šubara","Balkans","Conical or cylindrical black lamb-fur headgear."),
("Fur hat","Coonskin cap","North America","Raccoon-skin hat associated with 18th and 19th-century frontiersmen."),
("Beanie","Tuque","Canada","Knitted winter hat, also called a knit or ski cap."),
("Beanie","Chilote cap","Chiloé, Chile","Woven wool cap usually topped with a pom-pom."),
("Beret","Caubeen","Ireland","Irish beret."),
("Turban & head-wrap","Draped turban","","Fabric draped over the head, hiding most of the hair."),
("Turban & head-wrap","Gaung Paung","Burma","Headwrap worn by several Burmese peoples."),
("Turban & head-wrap","Tengkolok","Malay world","Songket cloth folded and tied into a set style."),
("Headscarf","Ghutrah","Arab world","Scarf of the three-piece keffiyah set with a skullcap and black band."),
("Regional cap","Ayam","Korea","Traditional winter cap worn mainly by Joseon-era women."),
("Regional cap","Balmoral bonnet","Scotland","Traditional Scottish bonnet worn with Highland dress."),
("Regional cap","Barretina","Catalonia","Floppy pull-on hat; the red version symbolises Catalan identity."),
("Regional cap","Bhadgaunle topi","Nepal","Typical Nepali cap."),
("Regional cap","Birke topi","Western Nepal","Short flat cylindrical hat, now mostly worn at festivals."),
("Regional cap","Blangkon","Java, Indonesia","Traditional Javanese men's hat."),
("Regional cap","Börk","Ottoman Empire","Tall cap worn by janissaries as a sign of devotion."),
("Regional cap","Guapi mao","China","Traditional Chinese men's skullcap."),
("Regional cap","Jeongjagwan","Korea","Horsehair hat popular among Joseon-era yangban."),
("Regional cap","Dhaka topi","Nepal","Nepali cap of dhaka fabric with hand-spun cotton weaving."),
("Regional cap","Gandhi cap","India","White cotton cap named after Mahatma Gandhi."),
("Regional cap","Glengarry","Scotland","Boat-shaped Scottish hat with a toorie and ribbons."),
("Regional cap","Icelandic tail-cap","Iceland","Part of Iceland's national costume."),
("Regional cap","Kłobuk","Poland","Tall felt highlander's hat."),
("Regional cap","Kofia","East Africa","Brimless cylindrical cap with a flat crown."),
("Regional cap","Kolah namadi","Iran","Felt hat worn by men in rural Iran."),
("Regional cap","Kupiah","Aceh, Indonesia","Traditional cap from Aceh."),
("Regional cap","Liuheyitong mao","China","Traditional Chinese men's hat from which the guapi mao evolved."),
("Regional cap","Labbadeh","Lebanon","Conical felt cap worn by rural Lebanese men."),
("Regional cap","Lika cap","Croatia","Wool cap with a red top, black rim and tassels."),
("Regional cap","Montenegrin cap","Montenegro","Wool cap with a red top and black rim."),
("Regional cap","Montera","Spain","Crocheted hat worn by bullfighters."),
("Regional cap","Pakul","Pakistan and Afghanistan","Round rolled wool hat with a flat top."),
("Regional cap","Phrygian cap","","Soft conical cap symbolising freedom and liberty."),
("Regional cap","Šajkača","Serbia","Serbian national and traditional hat."),
("Regional cap","Sami hat","Sámi people","Traditional men's hat, also called the Four Winds hat."),
("Regional cap","Songkok","Southeast Asia","Cap worn mostly by Muslim men in Malay-speaking regions."),
("Regional cap","Tam o' Shanter","Scotland","Scottish wool hat originally worn by men."),
("Regional cap","Upe","Bougainville","Headdress of tightly wound straw."),
("Regional cap","Wushamao","China","Traditional official's hat, spread to vassal states."),
("Regional cap","Yishan guan","China","Traditional men's hat worn by emperors and princes."),
("Regional cap","Zhanjiao futou","China","Official's hat also worn by the emperor."),
("Regional cap","Baishamao","China","Men's hat popular among royalty and aristocracy."),
("Novelty & costume hat","Party hat","","Conical celebration hat, often with patterns or messages."),
("Novelty & costume hat","Santa hat","Christmas","Floppy pointed red hat trimmed with white fur."),
("Novelty & costume hat","Dunce cap","","Tall conical hat used to punish school pupils."),
("Novelty & costume hat","Printer's hat","","Folded paper box-shaped hat worn by tradesmen."),
("Novelty & costume hat","Toque","","Tall, pleated, brimless chef's hat."),
("Novelty & costume hat","Makapili hat","Philippines","Bamboo basket hood worn by Japanese collaborators in the Second World War."),
("Novelty & costume hat","Whoopee cap","","Skullcap made from a felt fedora with a scalloped brim."),
("Novelty & costume hat","Wizard or witch hat","Fiction","Tall pointed hat with a wide brim and crooked top."),
]
HL=[r for r in HL if r[3]]
UMB=("Novelty & costume hat","Umbrella hat","","Hat made from an umbrella strapped to the head.")
HL.append(UMB)
SKIP_LIST_EXISTING=["Akubra","Boater","Boonie hat","Boss of the Plains","Bowler hat","Bucket hat","Cloche hat","Fedora","Gat","Homburg","Kalpak","Mortarboard","Panama","Pith helmet","Porkpie","Sou'wester","Stetson","Sun hat","Top hat","Trilby","Tyrolean hat","Vueltiao","Baseball cap","Flat cap","Kepi","Shako","Trucker hat","Bearskin","Beanie","Beret","Biretta","Chullo","Fez","Kippah","Kufi","Mobcap","Papakha","Qeleshe","Rastacap","Salakot","Shtreimel","Taqiyah","Tubeteika","Turban","Ushanka","Zucchetto","Deerstalker","Kasa","Casquette","Conical Asian hat","Keffiyah"]
added_hats=0
for kind,name,reg,desc in HL:
    if add(kind,E(name,desc,"","",LIST,g=(reg or "Type only, no region stated"))): added_hats+=1
# list count: 166 rows read, of which present before + added + 1 excluded (hard hat)
# --- regional garment forms
RG=[
("Scarf","Dupatta","India",W+'Scarf',"Long scarf worn by women in South Asia, named in the scarf article."),
("Scarf","Khata","Himalayan Buddhist tradition",W+'Scarf',"Ceremonial scarf of Himalayan Buddhism."),
("Scarf","Slendang","Indonesia and Malaysia",W+'Scarf',"Scarf of Indonesia and Malaysia named in the scarf article."),
("Scarf","Academic scarf","United Kingdom and Ireland",W+'Scarf',"Striped scarf in university or college colours."),
("Bandana","Oramal","Central Asia and the Caucasus",W+'Bandana',"Square headcloth of Uzbekistan, Kazakhstan and Kyrgyzstan."),
("Bandana","Bandhani","India",W+'Bandana',"Tie-dyed bandana from India."),
("Socks","Tabi","Japan",W+'Sock',"Japanese split-toe sock worn with thonged footwear."),
("Socks","Beoseon","Korea",W+'Sock',"Traditional Korean sock."),
("Mitten","Latvian mittens","Latvia",W+'Mitten',"Patterned mittens, with finds dated to around 1000 AD."),
("Mitten","Greenland Inuit mitts","East Greenland",W+'Mitten',"Mitts of the East Greenland Inuit."),
("Mitten","Naskapi leather mittens","Canada",W+'Mitten',"Leather mittens of the Naskapi, early 20th century."),
("Mitten","Saami mittens","Sápmi",W+'Mitten',"Mittens of the Saami."),
("Glove","Berlin gloves","19th-century Europe",W+'Glove',"Glove type named in the glove article."),
("Glove","Limerick gloves","Limerick, Ireland",W+'Glove',"Fine gloves made in Limerick in the 17th century."),
("Glove","Gauntlet","Medieval Europe",W+'Glove',"Armoured or long-cuffed glove of the Middle Ages."),
("Glove","Pontifical gloves","Frankish kingdom and Rome",W+'Glove',"Episcopal gloves of the 10th and 11th centuries."),
("Glove","Evening gloves","",W+'Glove',"Long formal glove."),
("Glove","Fingerless gloves","",W+'Glove',"Glove with the fingertips left bare, also called glovelettes."),
("Glove","Driving gloves","",W+'Glove',"Glove for driving, named in the glove article."),
("Shawl","Shahtoosh","Tibet",W+'Shawl',"Shawl from the under-fleece of the Tibetan antelope; now banned."),
("Shawl","Faroese lace shawl","Faroe Islands",W+'Shawl',"Lace shawl of the Faroe Islands."),
("Shawl","Haapsalu shawl","Estonia",W+'Shawl',"Lace shawl named in the shawl article."),
("Shawl","Galway shawl","Ireland",W+'Shawl',"Shawl named in the shawl article."),
("Shawl","Kullu shawl","Himachal Pradesh, India",W+'Shawl',"Shawl named in the shawl article."),
("Shawl","Spanish shawl","Spain",W+'Shawl',"Embroidered shawl revived in the 1920s."),
("Shawl","Shalli","",W+'Shawl',"Handwoven twill of angora goat hair."),
("Belt","Obi","Japan",W+'Belt_(clothing)',"Sash worn with the kimono."),
("Belt","Sam Browne belt","",W+'Belt_(clothing)',"Belt with a diagonal shoulder strap."),
("Belt","Cummerbund","",W+'Belt_(clothing)',"Pleated waist sash worn with evening dress."),
("Belt","Haramaki","Japan",W+'Belt_(clothing)',"Japanese waist wrap."),
("Belt","Stable belt","United Kingdom",W+'Belt_(clothing)',"Striped elasticated belt."),
("Belt","Sansabelt","United States",W+'Belt_(clothing)',"Belt-free waistband trouser system named in the belt article."),
("Belt","Studded belt","",W+'Belt_(clothing)',"Belt set with metal studs."),
("Belt","Bullet belt","",W+'Belt_(clothing)',"Belt styled on an ammunition belt."),
]
for kind,name,reg,src,desc in RG:
    add(kind,E(name,desc,"","",src,g=(reg or "Region not stated")))
# --- own / tier
OWNT={"Spanx":("Blackstone Inc.","2021","Independent"),"Jantzen":("Jantzen Brands Corporation","2019","Independent"),"'47":("New Era Cap Company","2024","Independent"),
"Wonderbra":("Gildan Activewear","2025","Global group"),"Bonds":("Gildan Activewear","2025","Global group"),"Arena":("Descente","1990","Independent"),"Icebreaker":("VF Corporation","","Global group"),"Smartwool":("VF Corporation","","Global group"),
"Gucci":("Kering","","Global group"),"Orlebar Brown":("Chanel","2018","Global group"),"Quiksilver":("Authentic Brands Group","","Global group"),"Seafolly":("L Catterton","2014","Independent"),
"Speedo":("Pentland Group","","Global group"),"Uniqlo":("Fast Retailing","","Global group"),"Nelson Knitting Company":("Fox River Mills","1992","Independent"),"Hanes":("Gildan Activewear","2025","Global group"),"Maidenform":("Gildan Activewear","2025","Global group")}
def yr(e):
    m=re.search(r'\d{4}',e.get('y') or ''); return int(m.group()) if m else 9999
for dp,sh,k in K.values():
    xs=k.get('x',[])
    for e in xs:
        mk=e.get('mk','')
        if mk in OWNT: e['own'],e['own_y'],e['tier']=OWNT[mk][0],OWNT[mk][1],OWNT[mk][2]
        if mk and not e.get('cty'):
            c=(REG.get(mk) or {}).get('c')
            if c: e['cty']=c
        if not e.get('g'):
            e['g']=e.get('cty') or ("Country not stated" if mk else "Named forms without a brand")
    FORMS=("Named forms without a brand","Country not stated","Region not stated","Type only, no region stated")
    xs.sort(key=lambda e:((e['g'] in FORMS,e['g']),yr(e),e['n']))
    if not xs: k.pop('x',None)
# --- sel
HATK=[k for k in K if K[k][0]['n']=="Hats & headwear"]
for name,(dp,sh,k) in K.items():
    xs=k.get('x',[]); n=len(xs)
    if not xs: continue
    if 'sel' not in k or k.get('nl','').startswith('No entry') or 'Complete: 0 of 0' in k['sel']:
        k['nl']="One entry is a signature garment sold under its own name by its originating brand, or a named form attested by a cited Wikipedia article; fits, fabrics and generations are versions."
        k['sel']="Signature pieces in the `sig` and `lines` fields of the brand register (rebuild/out/A1_brands.json, 2,531 brands) that match this garment, and the forms named by the cited Wikipedia articles and the earlier harvest."
    base=k['sel'].split(' Covers ')[0].rstrip()
    extra=" Entries restored from the earlier harvest (data/named_forms.tsv) cite the page recorded there." if any('rm' for _ in [0]) else ""
    m_=re.search(r'of about (\d+)',k['sel']); m_=max(int(m_.group(1)) if m_ else n,n)
    s=f"{base} Covers {n} of about {m_} in the register and those articles; the {m_} counts register brands known for this garment, most of which name no single piece."
    if dp['n']=="Hats & headwear": s+=" Wikipedia's List of hat styles was read in full (about 166 entries in the Brimmed, Caps, Brimless and Other sections); every style is a kind or an entry here except Hard hat, a helmet that goes to Sports and Tools."
    if name in("Scarf","Bandana","Socks","Mitten","Glove","Shawl","Belt"): s+=" Regional forms are those named by the garment's Wikipedia article."
    k['sel']=s
    if any(e.get('g') and e['g'] not in("Named forms without a brand",) for e in xs) and 'by' not in k.get('xg',''): k['xg']="by brand country or region, then year"
    else: k['xg']="by brand country or region, then year; forms without a brand last"
# kind nl for new kinds
for nm in("Regional brimmed hat","Regional cap","Novelty & costume hat","Braces"):
    k=K[nm][2]; k['nl']="One entry is a named hat or cap form listed in Wikipedia's List of hat styles, grouped by region as the list gives it; a brand's version of it is a version." if nm!="Braces" else "One entry is a braces model sold under its own name by its brand; widths and fastenings are versions."
# --- market summary
dp0=[d for d in P['depts'] if d['n']=="Underwear, nightwear & swim"][0]
dp0['ms']=[
 {"mkt":"US intimates category (bras and panties)","who":"Victoria's Secret (with PINK)","share":"about 20 %","yr":2023,"s":"https://www.marketbeat.com/earnings/reports/2024-3-6-victorias-secret-stock","note":"company-reported by its chief executive on the fourth-quarter 2023 earnings call of 7 March 2024; 'remains at about 20%'"},
 {"mkt":"US innerwear","who":"Hanesbrands (Hanes, Maidenform, Bali, Playtex)","share":"No. 1 seller of innerwear (no percentage given)","yr":2024,"s":"https://www.sec.gov/Archives/edgar/data/1359841/000135984125000008/hbi-20241228.htm","note":"fiscal 2024 10-K: leading maker of men's and children's underwear; Maidenform 'America's number one shapewear brand'; Gildan completed its acquisition on 8 December 2025 (https://printandpromomarketing.com/?p=169080)"},
 {"mkt":"Australian underwear, panties, children's underwear and socks","who":"Bonds","share":"No. 1 (no percentage given)","yr":2024,"s":"https://www.sec.gov/Archives/edgar/data/1359841/000135984125000008/hbi-20241228.htm","note":"fiscal 2024 10-K, International segment"},
 {"mkt":"Global hosiery","who":"Europe (region)","share":"more than 34 %","yr":2016,"s":"https://knittingindustry.com/?p=65614","note":"Research and Markets figure reported by Knitting Industry on 23 August 2016; the year of the figure is not stated"}]
dp0['msum']="Intimates are led by Victoria's Secret and Hanesbrands in the US; swimwear and hosiery have no company share figures on any fetched page, only fragmented-market claims from paid reports."
bu={}
for mk,(o,oy,t) in OWNT.items():
    r=REG.get(mk)
    if r and r.get('c'): bu[mk]={"own":o,"tier":t,"c":r['c']}
    else: bu[mk]={"own":o,"tier":t}
P['brand_updates']=bu
json.dump(P,open(BASE+'rebuild/out/A1_parts/UNDER.json','w'),ensure_ascii=False,indent=1)
json.dump({"restored":restored,"dropped_final":dropped,"hats_added":added_hats},open(BASE+'rebuild/work/V4_A1_UNDER/restore.json','w'),ensure_ascii=False,indent=1)
print(len(restored),len(dropped),added_hats)
