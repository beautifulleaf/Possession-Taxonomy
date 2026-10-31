import json,copy,os
R='/home/user/Possession-Taxonomy/rebuild/'
src=json.load(open(R+'work/STR_H4/bak/H4.json'))
K={}
for dp in src['depts']:
    for s in dp['s']:
        for k in s['k']: K[k['n']]=k
def X(kn,an):
    return [x for x in K[kn].get('x',[]) if x['n']==an][0]
def demote(kn,an,mode):
    k=K[kn]; x=X(kn,an); k['x']=[a for a in k['x'] if a['n']!=an]
    mk=(x.get('mk') or '').strip()
    k.setdefault('m',[])
    def addm(n):
        t=[n,mk]
        if t not in k['m']: k['m'].append(t)
    for v in x.get('v',[]) or []: addm(v['n'])
    if mode=='m': addm(x['n'])
    if mode=='r':
        k.setdefault('r',[]); k['r'].append([x['n'],mk])
for kn,an,mode in [
 ('Attar (deg-bhapka distillate)','Mogra and jasmine attar','tt'),('Attar (deg-bhapka distillate)','Kesar (saffron) attar','tt'),
 ('Oud oil (dehn al oud)','Hindi (Indian) oud oil','tt'),('Oud oil (dehn al oud)','Cambodi oud oil','tt'),('Oud oil (dehn al oud)','Malaysian and Indonesian oud oil','tt'),
 ('Rose oil & Taif rose','Turkish rose oil','tt'),
 ('Antique scent bottle','Double-ended scent bottle','tt'),('Antique scent bottle','Cameo glass scent bottle','tt'),('Antique scent bottle','Silver-mounted scent bottle','tt'),('Antique scent bottle','Chatelaine scent bottle','tt'),
 ('Czech crystal perfume bottle','Jewelled Czech bottle','tt'),
 ('Czech crystal perfume bottle','Vogel & Zappe intaglio bottle','r'),('Czech crystal perfume bottle','Josef Schmidt bottle','r'),
 ('Attar bottle','Egyptian hand-blown perfume bottle','tt'),
 ('Perfume organ',"Professional perfumer's organ",'tt'),('Perfume organ','Compact amateur organ','tt'),('Perfume organ','Tiered pine organ rack','tt'),
 ('Hair perfume','Honey Infused Hair Perfume','m'),('Hair perfume',"L'Eau Papier Hair Mist",'m'),
 ('Solid perfume','Lush solid perfume','r'),('Solid perfume','Diptyque refillable solid perfume','r'),
 ('Body mist','Axe / Lynx body spray','r'),
 ('Discovery set','Le Labo Discovery Set','r'),('Discovery set','Diptyque Discovery Set','r'),('Discovery set','Byredo Discovery Set','r'),('Discovery set','Olfactive Studio Discovery Kit','r'),
 ('Perfume miniature','Chanel No. 5 miniature','m'),('Perfume miniature','Chantilly purse size','m'),
 ('Collectible perfume bottle','Lalique for Coty','r'),('Collectible perfume bottle',"Lalique for D'Orsay",'r'),
 ('Essential oil','Rose otto','tt'),('Absolute & CO2 extract','Rose absolute','tt'),
]: demote(kn,an,mode)
# tidy range names
for kn,old,new in [('Czech crystal perfume bottle','Vogel & Zappe intaglio bottle','Vogel & Zappe intaglio bottles'),('Czech crystal perfume bottle','Josef Schmidt bottle','Josef Schmidt bottles'),('Solid perfume','Lush solid perfume','Lush solid perfumes'),('Solid perfume','Diptyque refillable solid perfume','Diptyque refillable solid perfumes'),('Body mist','Axe / Lynx body spray','Axe / Lynx body sprays'),('Discovery set','Le Labo Discovery Set','Le Labo discovery sets'),('Discovery set','Diptyque Discovery Set','Diptyque discovery sets'),('Discovery set','Byredo Discovery Set','Byredo discovery sets'),('Discovery set','Olfactive Studio Discovery Kit','Olfactive Studio discovery kits'),('Collectible perfume bottle','Lalique for Coty','Lalique bottles for Coty'),('Collectible perfume bottle',"Lalique for D'Orsay","Lalique bottles for D'Orsay")]:
    for r in K[kn]['r']:
        if r[0]==old: r[0]=new
WIKI='https://en.wikipedia.org/wiki/Fragrance_wheel'
HA='https://www.homesandantiques.com/antiques/collecting-guides-antiques/collecting-perfume-bottles/'
STC='https://surrendertochance.com/perfume-sample-sets'
def new(n,a,d,s): return {'n':n,'a':a,'d':d,'s':s,'x':[],'m':[],'r':[]}
K['Fruity fragrance']=new('Fruity fragrance','fruity perfume','Perfume whose main impression is fruit other than citrus, such as berry, peach, apple or tropical fruit.',WIKI)
K['Sampler set']=new('Sampler set','themed sample set · perfume sampler','Retailer-made set of small decants chosen by theme or level, such as a vanilla sampler or a beginner classic and niche set.',STC)
K['Non-commercial scent bottle']=new('Non-commercial scent bottle','empty scent bottle','Scent bottle sold empty for the owner to fill, made of silver, porcelain, cut crystal, agate or similar.',HA)
K['Novelty & figural bottle']=new('Novelty & figural bottle','novelty perfume packaging','Perfume sold in a novelty bottle or pack, such as a film tie-in bottle or a scent in a cigarette-carton box.',HA)
O=[["Origin of the scent",["Original house composition","Inspired-by (clone) of a classic"]]]
TT={
'Floral fragrance':[["Floral character",["Single floral","Floral bouquet","White floral","Aldehydic floral","Powdery floral"]]]+O,
'Fruity fragrance':[["Fruit",["Berry","Stone fruit","Apple and pear","Tropical fruit"]],["Pairing",["Fruity floral","Fruity gourmand","Fruity chypre"]]]+O,
'Amber fragrance':[["Style",["Soft amber","Floral amber","Spicy amber","Woody amber"]]]+O,
'Gourmand fragrance':[["Sweet note",["Vanilla","Praline and caramel","Fruity gourmand","Boozy gourmand"]]]+O,
'Oud fragrance':[["Style",["Rose-oud","Smoky oud","Woody oud"]]]+O,
'Musk & skin scent':[["Musk",["White musk","Animalic musk","Single-molecule musk"]],["Wear",["Skin scent"]]]+O,
'Woody fragrance':[["Wood or material",["Sandalwood","Cedar","Vetiver","Woody aromatic","Woody aroma-chemical (Iso E Super, ambroxan)"]]]+O,
'Chypre fragrance':[["Style",["Classic chypre","Fruity chypre","Floral chypre","Green chypre","Leather chypre"]]]+O,
'Leather fragrance':[["Style",["Russian leather","Suede","Leather chypre","Tobacco-leather"]]]+O,
'Citrus & eau de cologne':[["Style",["Classic cologne","Citrus aromatic","Eau fraîche"]]]+O,
'Green fragrance':[["Green note",["Galbanum green","Fig","Tea and leaf","Grassy"]]]+O,
'Aquatic & ozonic fragrance':[["Style",["Marine","Ozonic","Aquatic floral","Salty mineral"]]]+O,
'Fougère fragrance':[["Style",["Classic fougère","Aromatic fougère","Sweet fougère"]]]+O,
'Alcohol-based perfume':[["Concentration",["Parfum (extrait)","Eau de parfum","Eau de toilette","Eau de cologne","Eau fraîche"]],["Size",["Travel","Standard","Large"]]],
'Attar (deg-bhapka distillate)':[["Plant or source",["Rose","Vetiver","Kewra","Jasmine (mogra)","Saffron (kesar)","Earth (mitti)"]],["Base",["Sandalwood base","Liquid paraffin base"]],["Season",["Cool (summer) attar","Warm (winter) attar"]]],
'Rose oil & Taif rose':[["Origin",["Taif","Bulgarian","Turkish"]],["Method",["Otto (steam-distilled)","Absolute (solvent-extracted)","Attar (distilled into sandalwood)"]]],
'Oud oil (dehn al oud)':[["Origin",["Indian (Assam, Nagaland, Manipur, Meghalaya)","Cambodian","Malaysian and Indonesian"]],["Growth",["Wild","Cultivated (inoculated)","Aged"]],["Distillation",["Hydro-distilled","Steam-distilled"]]],
'Musk oil':[["Musk",["Synthetic white musk","Natural deer musk (CITES-controlled)"]],["Form",["Oil","Powder","Solid stone"]]],
'Mukhallat (blended oil)':[["Main note",["Oud","Rose","Amber","Saffron","Musk"]]],
'Perfume oil':[["Applicator",["Roll-on","Dab-on stick bottle"]],["Source",["Modern brand perfume oil","Oil version of a fine fragrance"]]],
'Body mist':[["Where sprayed",["Body","Hair and body"]],["Form",["Fine fragrance mist","Aerosol body spray (deodorant-fragrance)"]],["Size",["Travel size","Full size"]]],
'Hair perfume':[["Form",["Hair mist","Hair perfume"]],["Size",["Travel size","Full size"]]],
'Solid perfume':[["Container",["Refillable compact","Tin","Stick"]],["Base",["Wax","Butter"]]],
'Fragrance rollerball & pen spray':[["Applicator",["Rollerball (roll-on)","Pen spray"]],["Fill",["Pre-filled","Refillable"]],["Base",["Alcohol","Oil"]]],
'Sample vial':[["Applicator",["Dab vial","Spray vial","Scent card or strip insert"]],["Size",["1–2 ml"]],["Filled by",["Factory","Retailer decant"]]],
'Decant':[["Size",["Partial vial (¼–½ ml)","1 ml","2–3 ml","5 ml","8–10 ml","30 ml travel decant"]],["Applicator",["Dab vial","Glass spray"]],["Pack",["Single decant","Build-your-own decant set"]]],
'Perfume miniature':[["Age",["Vintage","Modern"]],["Dispensing",["Splash","Mini spray"]],["Pack",["Boxed","Unboxed","Graduated set in case"]],["Condition",["Sealed","Opened"]]],
'Discovery set':[["Format",["Vial set (1.5–2 ml)","Spray set (4–10 ml)"]],["Choice of scents",["Fixed","Pick-your-own"]],["Redemption",["With full-bottle voucher","Without voucher"]]],
'Sampler set':[["Theme",["Beginner classic and niche","Single note (vanilla, sandalwood)","Gourmand","Tea"]],["Count",["7 to 18 samples"]]],
'Gift set (coffret)':[["Contents",["Full bottle + travel spray","Full bottle + body lotion or shower gel","Miniature coffret","Collection of mid-size bottles","Spray + refill set","Layering or accord set"]]],
'Antique scent bottle':[["Period",["Georgian (1714–1837)","Victorian","Art Nouveau"]],["Glass",["Cut glass","Bristol blue","Opaline","Cameo glass","Cranberry overlay"]],["Mount",["Silver overlay","Silver-gilt mount","Silver-mounted"]],["Form",["Double-ended","Chatelaine"]]],
'Non-commercial scent bottle':[["Material",["Silver","Hand-painted porcelain","Ivory","Cut crystal","Agate","Carnelian","Carved nut"]]],
'Collectible perfume bottle':[["Condition",["Full with perfume","Empty"]],["Pack",["Boxed","Unboxed"]],["Edition",["Standard","Limited edition"]],["Size",["Extrait or parfum size"]],["Marking",["Signed (etched maker's mark)"]]],
'Czech crystal perfume bottle':[["Stopper",["Intaglio","Double intaglio","Dauber"]],["Decoration",["Jewelled metalwork","Enamelled"]],["Glass",["Coloured glass"]]],
'Attar bottle':[["Make",["Hand-blown glass","Gilt decoration"]],["Closure",["Dipper stopper"]],["Size",["Miniature"]],["Set",["Silver box set"]]],
'Factice (display dummy)':[["Size",["Oversized (giant)","Standard-size dummy"]],["Fill",["Sealed with coloured liquid","Empty"]]],
'Novelty & figural bottle':[["Theme",["Novelty packaging","Film tie-in"]]],
'Bulb atomiser':[["Bulb",["Netted bulb","Tasselled bulb","Bulb only (replacement)"]],["Glass",["Art glass","Cut glass"]]],
'Refillable travel atomiser':[["Fill method",["Pump-fill (bottom-fill)","Funnel-fill"]],["Body",["Glass","Aluminium case"]],["Size",["5 ml"]]],
'Essential oil':[["Extraction",["Steam-distilled","Cold-pressed (expressed)"]],["Origin",["Single origin"]],["Dilution",["Neat","Pre-diluted"]]],
'Absolute & CO2 extract':[["Method",["Absolute (solvent extraction)","Concrete (waxy first extract)","Enfleurage","CO2 extract (supercritical)","Resinoid"]]],
'Animalic & resin material':[["Material",["Animal-derived","Plant resin or balsam"]],["Form",["Raw material","Tincture","Absolute or resinoid","Synthetic reconstitution"]],["Legal status",["Varies by country"]]],
'Aroma chemical':[["Dilution",["Neat","10% in DPG or ethanol"]],["Origin",["Synthetic","Natural isolate"]],["Supply",["Captive (house-exclusive)","Commodity"]],["Regulation",["IFRA-restricted"]]],
"Perfumer's alcohol & carrier oil":[["Diluent",["Perfumer's alcohol (denatured ethanol)","Rectified spirit (ethanol-water)","Dipropylene glycol (DPG)","Jojoba oil","Fractionated coconut oil","Almond oil"]]],
'Smelling strip (mouillette)':[["End",["Pointed end for dipping","Square or paddle end for spraying"]],["Holder",["Strip holder or fan rack"]]],
'Perfume organ':[["Size",["Professional desk","Compact amateur (a few dozen bottles)"]],["Build",["Semicircular desk","Tiered wooden rack"]],["Order",["By family","By volatility (top, heart, base)"]]],
'Perfumery lab kit':[["Component",["Precision balance (0.001 g)","Disposable 1 ml pipettes","Glass beakers","Metal spatulas","Sample bottles (10–15 ml)","Labels","Perfumer's alcohol bottle"]]],
'Perfume-making kit':[["Contents",["Accord or base kit (pre-made bases)","Raw-materials training kit"]],["Course link",["Course-linked kit (booklet, software)"]],["Audience",["Adult","Children's"]]],
}
for n,tt in TT.items():
    k=K[n]; k.pop('t',None); k['tt']=tt
K['Alcohol-based perfume']['d']='Perfume sold and described by strength rather than by family: parfum, eau de parfum, eau de toilette or eau de cologne.'
K['Aroma chemical']['d']=K['Aroma chemical']['d']
SEE={
'Body mist':[['H1','Deodorant','aerosol body sprays sit between the two']],
'Citrus & eau de cologne':[['H1','Aftershave','splash cologne and aftershave overlap']],
'Essential oil':[['B4','Diffuser oil','same oils sold for room use']],
'Collectible perfume bottle':[['B4','Decorative bottle','a bottle kept only for display']],
'Attar (deg-bhapka distillate)':[['H4','Perfume oil','modern brand oils']],
'Oud fragrance':[['H4','Oud oil (dehn al oud)','neat oil, not alcohol']],
'Perfume miniature':[['H4','Sample vial','sample-size alternative']],
'Decant':[['H4','Sample vial','maker-filled vial']],
'Refillable travel atomiser':[['H4','Decant','hand-poured travel fill']],
'Fragrance rollerball & pen spray':[['H4','Perfume oil','oil roll-on']],
'Musk & skin scent':[['H4','Musk oil','traditional musk oil']],
'Antique scent bottle':[['H4','Non-commercial scent bottle','sold empty']],
}
for n,v in SEE.items(): K[n]['see']=v
def sh(n,t,ax,kinds): return {'n':n,'t':t,'ax':ax,'k':[K[x] for x in kinds]}
D=[]
oldD={d['n']:d for d in src['depts']}
def dep(old,n,t,ax,shelves):
    o=oldD[old]; d={'n':n,'mode':o['mode']}
    if 'note' in o and n==old: d['note']=o['note']
    if 'b' in o and n==old: d['b']=o['b']
    d['t']=t; d['ax']=ax; d['s']=shelves; D.append(d)
dep('Perfume','Perfume',"Fragrance in an alcohol base sprayed on the skin, grouped by the fragrance wheel; a scent in oil, mist or wax → Oils, attars & body fragrance; a small vial or set → Samples, decants & sets.",
 "Which wheel family gives the main impression: floral, warm, woody or fresh, or none stated?",[
 sh('Floral & fruity',"Perfumes led by flowers or fruit, from single flowers to fruity florals; a floral that is warm and resinous → Warm & sweet.","kinds from flowers to fruit",['Floral fragrance','Fruity fragrance']),
 sh('Warm & sweet',"Perfumes of resins, vanilla, oud and musk, such as Shalimar, Angel or Molecule 01; a woody dry-down → Woody & mossy.","kinds from resinous amber to sweet, dark oud and skin-close musk",['Amber fragrance','Gourmand fragrance','Oud fragrance','Musk & skin scent']),
 sh('Woody & mossy',"Perfumes of woods, oakmoss and leather, such as Vétiver, Mitsouko or Tabac Blond; a fresh green → Fresh.","kinds from clean woods to mossy chypre and leather",['Woody fragrance','Chypre fragrance','Leather fragrance']),
 sh('Fresh',"Light perfumes of citrus, leaves, water and lavender, such as Eau Sauvage, Vent Vert or Cool Water; a heavier floral → Floral & fruity.","kinds from citrus to green, water and lavender fougère",['Citrus & eau de cologne','Green fragrance','Aquatic & ozonic fragrance','Fougère fragrance']),
 sh('By concentration',"Perfume described only by strength, such as parfum, eau de parfum or eau de toilette, with no family given.","kinds by strength, richest first",['Alcohol-based perfume']),
])
dep('Perfume','Oils, attars & body fragrance',"Fragrance worn without an alcohol spray: oils and attars, mists, solid and hair scents; an alcohol perfume → Perfume.","What carries the scent: an oil or attar, or a light spray, wax or applicator?",[
 sh('Attar & traditional oils',"Oil perfumes with no alcohol, from Kannauj attars to Taif rose and oud oil; a modern brand oil is the last kind.","kinds by main material: flower distillates, rose, oud, musk, blends, then modern brand oils",['Attar (deg-bhapka distillate)','Rose oil & Taif rose','Oud oil (dehn al oud)','Musk oil','Mukhallat (blended oil)','Perfume oil']),
 sh('Body, hair & solid fragrance',"Light and portable formats: body mist, hair perfume, solid perfume and rollerballs; deodorant → H1.","kinds by how it is applied: body spray, hair spray, rubbed-on wax, pocket applicator",['Body mist','Hair perfume','Solid perfume','Fragrance rollerball & pen spray']),
])
dep('Samples, decants & sets','Samples, decants & sets',"Small containers and boxed sets for trying or giving scents; a full-size bottle → Perfume; a bottle kept as an object → Bottles & atomisers.","Is it one scent in a small container, or several scents boxed together?",[
 sh('Small vials & miniatures',"One scent in a small container: maker vials, hand-poured decants and retail miniatures.","kinds by who filled it: the maker, a decanter or a retailer",['Sample vial','Decant','Perfume miniature']),
 sh('Boxed sets',"Several scents or items boxed together: house discovery sets, retailer samplers and gift coffrets.","kinds by who assembled the set and why: a house, a retailer, a gift",['Discovery set','Sampler set','Gift set (coffret)']),
])
dep('Bottles & atomisers','Bottles & atomisers',"Scent bottles kept as objects and devices that dispense or carry perfume; a decorative bottle with no scent use → B4.","Is the bottle kept and valued as an object, or used to dispense and carry perfume?",[
 sh('Collectible & antique bottles',"Bottles valued for glass, maker and age: antique scent bottles, designer flacons, Czech crystal and shop dummies.","kinds by how the bottle was made and sold: antique hand-made, sold empty, made for a house, regional glass, display, novelty",['Antique scent bottle','Non-commercial scent bottle','Collectible perfume bottle','Czech crystal perfume bottle','Attar bottle','Factice (display dummy)','Novelty & figural bottle']),
 sh('Atomisers & refillables',"Devices that spray or carry perfume: vanity bulb atomisers and refillable travel sprays; a decant vial → Samples, decants & sets.","kinds from vanity to travel",['Bulb atomiser','Refillable travel atomiser']),
])
dep('Perfumery materials','Perfumery materials',"Raw materials for blending perfume, sold to hobby perfumers; home fragrance products → B4; the finished scent → Perfume.","What is the material made from: plant extract, resin or animal product, synthetic molecule, or diluent?",[
 sh('Natural extracts',"Oils and extracts taken from plants by distillation, pressing or solvent: essential oils, absolutes, CO2 extracts.","kinds by extraction: distilled or pressed oils, then solvent and CO2 extracts",['Essential oil','Absolute & CO2 extract']),
 sh('Resins & animal materials',"Resins, balsams and animal-derived fixatives such as ambergris, labdanum and frankincense.","one kind",['Animalic & resin material']),
 sh('Aroma chemicals & diluents',"Single molecules and the liquids that dilute them, such as Hedione or DPG.","kinds from the molecule to its diluent",['Aroma chemical',"Perfumer's alcohol & carrier oil"]),
])
dep('Perfumery materials',"Perfumer's tools & kits","Equipment for smelling, storing and blending perfume at home, and boxed kits; the materials themselves → Perfumery materials.","Is it used to smell and keep materials, or to weigh and blend them?",[
 sh('Smelling & storage',"Strips and organs for evaluating and storing materials.","kinds from the strip to the cabinet",['Smelling strip (mouillette)','Perfume organ']),
 sh('Blending & kits',"Bench equipment and boxed starter kits for making perfume.","kinds from bench tools to boxed kits",['Perfumery lab kit','Perfume-making kit']),
])
# fix 'Perfumery materials' dept keeps note
for d in D:
    if d['n']=='Perfumery materials': d['note']=oldD['Perfumery materials']['note']
    if d['n']=='Perfume': d['note']=oldD['Perfume']['note']; d['b']=oldD['Perfume']['b']
    if d['n']=='Samples, decants & sets': d['note']=oldD['Samples, decants & sets']['note']
out=copy.deepcopy(src); out['depts']=D
out['ax']="How is the fragrance used: worn as perfume, tried in small vials and sets, kept or carried in a bottle, or made from raw materials?"
out['key']=["1. Is it a scent you wear in alcohol, grouped by family (floral, warm, woody, fresh)? → Perfume",
"2. Is it an oil, attar, mist, solid or hair scent worn on the skin? → Oils, attars & body fragrance",
"3. Is it a small vial, decant, miniature or boxed set for trying or giving scents? → Samples, decants & sets",
"4. Is it a scent bottle valued as an object, or an atomiser that carries perfume? → Bottles & atomisers",
"5. Is it an oil, extract, resin or molecule used to make perfume? → Perfumery materials",
"6. Is it a strip, organ, balance or kit for smelling and blending? → Perfumer's tools & kits",
"<i>Precedence: a small sample-size bottle is a sample (step 3) before a bottle (step 4); a candle, diffuser or incense → B4; deodorant and aftershave → H1.</i>"]
tmp=R+'out/H4.json.tmp'
json.dump(out,open(tmp,'w'),ensure_ascii=False,indent=1); os.replace(tmp,R+'out/H4.json')
# check all kinds placed
placed={k['n'] for d in D for s in d['s'] for k in s['k']}
print(set(K)-placed)
