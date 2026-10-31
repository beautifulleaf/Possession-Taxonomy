import json,os,copy
P='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(P+'H2.json')); br=json.load(open(P+'H2_brands.json')); mv=json.load(open(P+'H2_moves.json'))
def dept(n): return next(x for x in d['depts'] if x['n']==n)
def shelf(dn,sn): return next(x for x in dept(dn)['s'] if x['n']==sn)
def kind(n):
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']:
                if k['n']==n: return k,s
def rm(n):
    k,s=kind(n); s['k'].remove(k); return k
def mkcount():
    return sum(len(s['k']) for dp in d['depts'] for s in dp['s'])
before=mkcount()
# H2-5 one per maker
def onepm(n):
    k,_=kind(n); seen=set(); out=[]
    for m in k['m']:
        if m[1] in seen: continue
        seen.add(m[1]); out.append(m)
    k['m']=out
for n in ['Portable ramp','Alerting system','Pregnancy test','Nicotine replacement']: onepm(n)
# H2-4 kind level only
for n in ['Leg prosthesis','Arm prosthesis','Implant sound processor','Spectacle lens','Patient lift']:
    k,_=kind(n); k.pop('m',None); k.pop('r',None)
# H2-3 hearing aids
hs=['Receiver-in-canal hearing aid','Behind-the-ear hearing aid','In-the-ear hearing aid','In-the-canal hearing aid']
ks=[kind(n)[0] for n in hs]
ric=ks[0]
ha={"n":"Hearing aid","a":"RIC hearing aid · RITE · BTE · ITE · ITC · CIC · IIC · miniRITE","d":"Prescription device worn in or behind the ear that amplifies sound for a person with hearing loss; form factor varies.","t":["receiver-in-canal (RIC/RITE)","behind-the-ear (BTE, miniBTE, power BTE)","in-the-ear (full or half shell)","in-the-canal (ITC)","completely-in-canal (CIC)","invisible-in-canal (IIC)","extended-wear (placed by a professional)","rechargeable","disposable battery (312, 13, 10 or 675)","CROS/BiCROS version","paediatric"],"s":ric['s']}
pick=["Phonak Audéo Infinio","Phonak Naída Lumity","Phonak Virto Infinio","Oticon Intent miniRITE R","Oticon Xceed","Oticon Zeal","ReSound Vivia","ReSound Enzo IA","Signia Pure Charge&Go IX","Signia Insio IX","Widex SmartRIC","Widex Moment CIC","Starkey Omega AI mRIC R","Starkey Omega AI ITE R"]
allm={m[0]:m for k in ks for m in k['m']}
ha['m']=[allm[p] for p in pick if p in allm]
seenr=set();r=[]
for k in ks:
    for x in k.get('r',[]):
        if x[1] in seenr: continue
        seenr.add(x[1]); r.append(x)
ha['r']=r
sh=shelf('Hearing','Hearing aids')
idx=sh['k'].index(kind(hs[0])[0])
for n in hs: rm(n)
sh['k'].insert(idx,ha)
# joint support
js=['Knee support','Ankle support','Back support','Wrist & hand support','Elbow support','Neck support']
jk=[kind(n)[0] for n in js]
sh=shelf('First aid & supports','Braces, supports & insoles')
idx=sh['k'].index(jk[0])
allm={m[0]:m for k in jk for m in k['m']}
pick=["GenuTrain","MalleoTrain","ManuTrain","EpiTrain","Genumedi","Performance Knee Stabilizer","Easy Adjustable Back Support","Deluxe Wrist Stabilizer","Defiance III","Velocity ES","Push Med Back Brace","Smartspine Universal Collar"]
jt={"n":"Joint support / brace","a":"knee brace · ankle brace · back brace · wrist splint · elbow strap · cervical collar · lumbar support","d":"Elastic, strapped or hinged support worn to steady or protect a joint or the spine; body part is the main variant.","t":["knee (sleeve, strapped, hinged, unloader)","ankle (sleeve, lace-up, stirrup, walker boot)","back (lumbar belt, rigid-stay brace, posture corrector)","wrist & hand (sleeve, splint, thumb stabiliser)","elbow (sleeve, epicondylitis strap, hinged)","neck (soft or rigid collar)"],"s":jk[0]['s'],"m":[allm[p] for p in pick if p in allm]}
for n in js: rm(n)
sh['k'].insert(idx,jt)
# H2-7
k=rm('Grab bar')
mv['out'].append({"to":"G3","dept":"Bath & wellness","kind":k})
k=rm('Medical app')
mv['out'].append({"to":"I1","dept":"Hobbies, science & sky","kind":k})
k=rm('Delay spray'); shelf('Sexual health & family','Intimate health devices')['k'].append(k)
dp=dept('Medicines & remedies')
s=shelf('Medicines & remedies','Quit smoking & traditional remedies')
nic=kind('Nicotine replacement')[0]; s['k'].remove(nic)
s['n']='Traditional remedies'
i=dp['s'].index(s); dp['s'].insert(i,{"n":"Quit smoking","k":[nic]})
sl=rm('Sleep aid')
s=shelf('Breathing, sleep & therapy','Breathing & sleep apnoea'); s['n']='Breathing & sleep'; s['k'].append(sl)
# H2-2 wheelchairs
W='https://en.wikipedia.org/wiki/Wheelchair'
mw,_=kind('Manual wheelchair')
mw['x']=[
 {"n":"Quickie","a":"Quickie rigid-frame chair","d":"Lightweight, adjustable aluminium-frame chair launched as a custom active-user wheelchair.","mk":"Sunrise Medical","y":"1980","s":"https://en.wikipedia.org/wiki/Marilyn_Hamilton","dt":"co-founded by Marilyn Hamilton, Jim Okamoto and Don Helman · aluminium frame · colour options"},
 {"n":"Küschall Competition","a":"Champion 3000 (US name)","d":"Ultralight competition chair designed by Rainer Küschall, about 14 kg against the usual 25 kg.","mk":"Küschall","y":"1985","s":"https://en.wikipedia.org/wiki/Rainer_K%C3%BCschall","v":[{"n":"Champion 3000","mk":"Küschall","y":"","d":"US sales name"}],"dt":"MoMA collection, first medical device in it · rigid frame"},
 {"n":"TiLite titanium rigid chair","a":"TiFit custom chair","d":"Custom ultralight rigid-frame chair, built in titanium, aluminium or carbon fibre and fitted per user.","mk":"TiLite","y":"1988","s":"https://en.wikipedia.org/wiki/TiLite","v":[{"n":"CrossSport","mk":"TiLite","y":"","d":"early model"}],"dt":"titanium, aluminium or carbon-fibre frame · TiFit measured build"},
 {"n":"Everest & Jennings folding chair","a":"","d":"First lightweight, steel, folding, portable wheelchair; the first mass-market wheelchair.","mk":"","y":"1933","s":W,"dt":"steel folding frame · 1937 patent"}]
kind('Manual wheelchair')[1]
mw['m']=[m for m in mw['m'] if m[0] not in('Küschall Champion',)]
dept('Mobility aids')['mode']='mixed'
dept('Mobility aids')['note']='Archetypes only for active wheelchairs and collector canes; the rest is tier.'
# H2-1 collector canes
C='https://en.wikipedia.org/wiki/Walking_stick'; S='https://en.wikipedia.org/wiki/Swordstick'
cane={"n":"Collector cane","a":"antique cane · gadget cane · dress cane · system cane","d":"Walking stick owned as a fashion accessory or curiosity rather than a mobility aid; includes hidden-fitting and gadget canes.","t":["silver-topped","carved or ivory-style handle","shaft: malacca, ash, blackthorn, bamboo","folding","hidden-compartment"],"s":C,
 "x":[
 {"n":"Malacca cane","a":"rattan cane","d":"Cane with a shaft of Malay rattan palm, historically the commonest cane shaft.","mk":"","y":"","s":S,"dt":"rattan shaft · sterling-silver or horn handle"},
 {"n":"Swordstick","a":"sword cane","d":"Cane whose shaft is a scabbard for a concealed blade; fashionable in the 18th and 19th centuries.","mk":"","y":"18th century","s":S,"dt":"blade length · handle as hilt · shaft wood · legal status varies"},
 {"n":"Gadget cane","a":"system cane","d":"Cane hiding a tool such as a compass or flask.","mk":"","y":"19th century","s":S,"dt":"compass, flask or tool fitting"},
 {"n":"Tippling cane","a":"tippler","d":"Cane with a hollow compartment near the top for a flask or vial of alcohol.","mk":"","y":"","s":C,"dt":"top compartment · stopper"},
 {"n":"Penang lawyer","a":"","d":"Stick of stripped, straightened and polished Licuala palm stem.","mk":"","y":"","s":C,"dt":"Licuala palm shaft"},
 {"n":"Makila","a":"makhila","d":"Basque staff, usually medlar wood, with gold or silver fittings that may conceal a steel blade.","mk":"","y":"","s":C,"dt":"medlar wood · metal fittings"},
 {"n":"Shooting stick","a":"","d":"Stick that opens into a single-legged seat.","mk":"","y":"","s":C,"dt":"folding seat top"}],
 "m":[],"r":[["Walking sticks and canes","Swaine Adeney Brigg"]]}
shelf('Mobility aids','Walking aids')
dept('Mobility aids')['s'].insert(1,{"n":"Collector canes","k":[cane]})
br['b'].append({"n":"Swaine Adeney Brigg","c":"United Kingdom","f":"1798","seg":"Heritage manufactory","kf":"canes, umbrellas, whips","d":"London maker of walking sticks, umbrellas, whips and leather goods, based in Piccadilly from 1798.","lines":["Brigg umbrellas","Walking sticks and canes"],"s":"https://en.wikipedia.org/wiki/Swaine_Adeney_Brigg"})
print(before,mkcount())
for f,o in(('H2',d),('H2_brands',br),('H2_moves',mv)):
    json.dump(o,open(P+f+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+f+'.tmp',P+f+'.json')
