import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(P+'A4.json'))
LENS=["sun","polarised","prescription","photochromic","plano"]
def dept(n): return next(x for x in d['depts'] if x['n']==n)
def shelf(dn,sn): return next(s for s in dept(dn)['s'] if s['n']==sn)
def kind(n):
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']:
                if k['n']==n: return k
def rmkind(n):
    for dp in d['depts']:
        for s in dp['s']:
            s['k']=[k for k in s['k'] if k['n']!=n]
def A(n,a,dsc,mk,y,s,v=None,dt=''):
    return {"n":n,"a":a,"d":dsc,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
V=lambda n,mk,y='',d_='':{"n":n,"mk":mk,"y":y,"d":d_}
cnt0=(sum(len(s['k']) for dp in d['depts'] for s in dp['s']),sum(len(k.get('x',[])) for dp in d['depts'] for s in dp['s'] for k in s['k']))

# A4-6 structure
sh=kind('Shoulder bag'); xs={a['n']:a for a in sh['x']}
flap=[xs[n] for n in ['Chanel 2.55','Chanel Boy','Chanel 19','Gucci Horsebit 1955','Celine Triomphe']]
sh['x']=[a for a in sh['x'] if a not in flap and a['n']!='Half-moon bag' and a['n']!='Coach Tabby']
saddle_extra=[xs['Half-moon bag'],xs['Coach Tabby']]
flap_kind={"n":"Flap bag","a":"classic flap · envelope bag","d":"Bag closed by a front flap, usually on a chain or leather shoulder strap.","t":["chain strap","leather strap","turn-lock","magnetic closure"],"s":"https://en.wikipedia.org/wiki/Chanel_2.55","x":flap}
# new archetypes
flap_kind['x'].insert(5,A("Constance","Hermès Constance","Hermès shoulder bag with a large H clasp, created by in-house designer Catherine Chaillet and named after her daughter.","Hermès","1959","https://madisonavenuecouture.com/blogs/news/hermes-bag-names-the-stories-behind-them",[V("Constance (original)","Hermès","1959","Catherine Chaillet for Jean-Louis Dumas")],"size · leather · hardware (the H clasp has changed over time)"))
flap_kind['x'].append(A("Loulou","Saint Laurent Loulou","Y-quilted flap bag with Cassandre hardware, named for Yves Saint Laurent's muse Loulou de la Falaise.","Saint Laurent","2017","https://www.fashionphile.com/blogs/academy/loulou-bag-styles-sizes",[V("Loulou Toy","Saint Laurent","2017","removable leather strap, about 18 cm wide"),V("Loulou Small","Saint Laurent","","adjustable chain strap"),V("Loulou Medium","Saint Laurent","","adjustable chain strap"),V("Loulou Large","Saint Laurent","","adjustable chain strap"),V("Loulou Puffer","Saint Laurent","","different quilt pattern from the Y quilt")],"Toy, Small, Medium, Large · calfskin, lambskin, velvet, denim"))
flap_kind['x'].append(A("Gucci Dionysus","Dionysus","Shoulder bag closed by a horseshoe clasp ending in tiger heads, first shown in Alessandro Michele's 2015 collection.","Gucci","2015","https://www.ngv.vic.gov.au/essay/dionysus-bag/",[V("Dionysus (2015)","Gucci","2015","Alessandro Michele; autumn-winter 2015-16")],"size · GG Supreme, suede, python, crocodile"))
for i,pos in enumerate(sh['t']): pass
# insert Flap bag before Shoulder bag's following kinds: put right after Shoulder bag in shelf
shf=shelf('Handbags','Shoulder & crossbody bags'); 
idx=[k['n'] for k in shf['k']].index('Shoulder bag'); shf['k'].insert(idx,flap_kind)
sh['d']="Bag on a single strap worn on one shoulder, without a front flap or a hobo or saddle shape."
sh['t']=["chain strap","leather strap","zip top"]
# Saddle & half-moon
sd=kind('Saddle bag'); sd['n']='Saddle & half-moon bag'; sd['a']='saddle bag · crescent bag · half-moon bag'
sd['d']="Bag with a curved saddle or crescent body, often with a flap, on a short strap."
sd['x']+=saddle_extra
# Bowling & Boston (absorb Barrel), Doctor -> Top-handle
bw=kind('Bowling bag'); bw['n']='Bowling & Boston bag'; bw['a']='bowling bag · Boston bag · bowler bag · barrel bag'
bw['d']="Domed or cylindrical zip-top bag with two handles, modelled on bowlers' and travel bags."
bw['x']+=kind('Barrel bag')['x']; rmkind('Barrel bag')
th=kind('Top-handle bag'); doc=kind('Doctor bag'); th['x']+=doc['x']; rmkind('Doctor bag')
th['x'].append(A("Lindy","","Slouchy Hermès bag whose handles sit perpendicular to the body, with a detachable shoulder strap; designed by Frédéric Vidal.","Hermès","2007","https://madisonavenuecouture.com/blogs/news/hermes-bag-names-the-stories-behind-them",[V("Lindy (2007)","Hermès","2007","first shown in the spring-summer 2007 collection")],"size · leather · colour"))
# A4-1 others
kind('Crossbody bag')['x']=[A("Evelyne","Hermès Evelyne","Hermès messenger-style bag with a perforated H on the back, made with Hermès's riding department as a grooming-tool carrier.","Hermès","1978","https://madisonavenuecouture.com/blogs/news/hermes-bag-names-the-stories-behind-them",[V("Evelyne (original)","Hermès","1978","Evelyne Bertrard, head of the riding department")],"size · leather · colour")]
kind('Bucket bag')['x'].append(A("Picotin","Picotin Lock","Hermès bucket bag named for the French measure of horse feed, with loops that fit over the handles.","Hermès","","https://madisonavenuecouture.com/blogs/news/hermes-bag-names-the-stories-behind-them",[V("Picotin (original)","Hermès"),V("Picotin Lock","Hermès","2002","adds the Kelly lock and key")],"size · leather · colour"))
kind('Hobo bag')['x'].insert(1,A("Balenciaga City","Motorcycle bag · Classic City","Soft lambskin bag with studs, tassels and buckles, shown as the Motorcycle bag by Nicolas Ghesquière.","Balenciaga","2001","https://etoile-luxuryvintage.com/blogs/the-history-of/history-of-the-bag-balenciaga-classic-city-bag",[V("Motorcycle City (prototype)","Balenciaga","2001","25 made for models and editors"),V("Classic City","Balenciaga","","studs in gold, palladium or rose gold"),V("Giant 12 City","Balenciaga","","larger studs, same proportions"),V("Giant 21 City","Balenciaga","","oversized studs, buckles and patches")],"mini, small, City sizes · lambskin · colour"))
tote=kind('Tote bag')['x']
tote.append(A("Celine Luggage","Luggage Tote","Boxy, structured tote with winged sides, a front zip and a detachable strap, by Phoebe Philo.","Celine","2010","https://leprix.com/en/blog/a-guide-to-celine-113",[V("Luggage Tote","Celine","2010","Phoebe Philo era")],"four sizes · calfskin, nubuck, crocodile"))
tote.append(A("Telfar Shopping Bag","Bushwick Birkin","Vegan-leather shopping tote with a debossed T logo, shown at Telfar's Fall/Winter 2014 show.","Telfar","2014","https://www.rebag.com/thevault/?p=9239",[V("Original colours","Telfar","","tan, black, white"),V("Resized range","Telfar","2018","sizes changed in 2018")],"small, medium, large · vegan leather · colour"))
# A4-2
wk=shelf('Handbags','Totes & bucket bags')
nxt={"n":"Basket & woven bags","s":[]}
woven={"n":"Basket & woven bag","a":"straw bag · string bag · basket bag","d":"Bag made by weaving, looping or crocheting fibre into a basket-like or net body.","t":["market basket","looped string bag","crocheted shoulder bag"],"s":"https://en.wikipedia.org/wiki/Kiondo","x":[
 A("Wayuu mochila","mochila","Crocheted shoulder bag made by Wayuu women of the Guajira Peninsula in Colombia and Venezuela.","","","https://en.wikipedia.org/wiki/Wayuu_people",[],"acrylic thread today, dyed cotton traditionally · pattern · size"),
 A("Bilum","","Looped string bag from Papua New Guinea; the name also covers the knotless looping technique.","","","https://rotterdam.wereldmuseum.nl/en/collection-stories/bilum-multifunctional-bag-which-everything-fits",[],"plant fibre, wool, cotton or yarn · carryall or small amulet bag"),
 A("Kiondo","chondo","Handwoven Kenyan bag of vegetable twine with leather trim, made by Taita, Kikuyu and Kamba peoples.","","","https://en.wikipedia.org/wiki/Kiondo",[],"sisal twine · leather trim · size")]}
shl=dept('Handbags')['s']; shl.insert([s['n'] for s in shl].index('Totes & bucket bags')+1,{"n":"Basket & woven bags","k":[woven]})
# A4-4
rmkind('Wristlet bag')
for k in [k for dp in [dept('Eyewear')] for s in dp['s'] for k in s['k']]:
    if k.get('t')==LENS: del k['t']
dept('Eyewear')['note']="ONE department for all frames: sunglasses, optical frames and readers. Kinds are frame shapes; every frame kind comes in sun, polarised, prescription, photochromic or plano lenses (a lens type, not a kind)."
# A4-5
pg=kind('Prescription glasses'); pg['m']=[]; pg['r']=[["Own frame designs","Specsavers"],["In-house frames","Zenni Optical"],["In-house frames","Warby Parker"]]
pg['d']="Glasses with lenses made to the wearer's prescription, including prescription sunglasses; frames from EssilorLuxottica brands such as Ray-Ban and Oakley are bought for glazing."
rg=kind('Reading glasses'); rg['m']=[]; rg['r']=[["Ready-made readers","Foster Grant"]]
# A4-3
sq=kind('Square & rectangular frames'); sq['x'].insert(0,A("Cazal 607","Cazzy","Square, full-rim frame in thick acetate, one of Cazal's best-selling classics.","Cazal","","https://www.eyeons.com/cazal-607",[V("607 Black","Cazal"),V("607 Black Matte","Cazal"),V("607 Crystal","Cazal")],"56-18-140 mm · acetate colour"))
rd=kind('Round & panto frames'); rd['x'].append(A("Ray-Ban Round Metal","Round Metal","Thin round metal frame with a curved brow bar and adjustable nose pads.","Ray-Ban","","https://india.ray-ban.com/round-metal-optics.html",[V("Round Metal optics 3447V","Ray-Ban","","50 mm lens, gold")],"lens 47–53 mm · gold, black metal"))
# antique eyewear shelf
ant=[
{"n":"Monocle","a":"single eyeglass","d":"Single circular lens held in the eye socket, often on a cord; common among men from the 1830s to the early 1900s.","t":["slotted loop (1830s)","gallery frame (1890s)","frameless cut glass"],"s":"https://en.wikipedia.org/wiki/Monocle"},
{"n":"Pince-nez","a":"nose glasses","d":"Glasses without earpieces, gripping the bridge of the nose; popular in Europe from the 1840s and at their peak around 1880–1900.","t":["C-bridge","astig (bar-spring)","Fits-U","Oxford spectacles","rivet spectacles"],"s":"https://en.wikipedia.org/wiki/Pince-nez","x":[A("Fits-U","","Hard-bridge pince-nez with finger-piece levers, patented by Jules Cottet in 1893 and marketed by American Optical.","American Optical","1893","https://en.wikipedia.org/wiki/Pince-nez",[],"gold-filled or steel · lens shape")]},
{"n":"Lorgnette","a":"lorgnon","d":"Pair of spectacles on a handle, held to the eyes; used from about 1770 and favoured at the opera and theatre.","t":["standard","fan lorgnette","double lorgnette"],"s":"https://en.wikipedia.org/wiki/Lorgnette"}]
dept('Eyewear')['s'].append({"n":"Antique eyewear","k":ant})
# A4-7
for o,n in [('Wallet on chain','Wallet on chain (bag)'),('Chain wallet','Biker chain wallet')]: kind(o)['n']=n
tz=kind('Trapezoid frames'); tz['n']='Wayfarer-style frames'; tz['a']='trapezoid frames · trapezoidal frames'
kind('Wallet on chain (bag)')['d']="Small bag-like wallet carried on a shoulder or cross-body chain, unlike a biker chain wallet."
kind('Biker chain wallet')['d']="Wallet fixed by a chain to a belt loop, unlike a wallet on chain bag."
json.dump(d,open(P+'A4.json.tmp','w'),ensure_ascii=False,indent=1)
os.replace(P+'A4.json.tmp',P+'A4.json')
cnt1=(sum(len(s['k']) for dp in d['depts'] for s in dp['s']),sum(len(k.get('x',[])) for dp in d['depts'] for s in dp['s'] for k in s['k']))
print(cnt0,cnt1)
# traditions
t=json.load(open(P+'A4_traditions.json')); 
t['t']+= [
{"n":"Wayuu mochila","g":"Textiles & rugs","r":"Guajira Peninsula, Colombia and Venezuela","p":"","d":"Crocheted bags made by Wayuu women, who learn the craft young; men make the straps.","tech":"crochet","mat":"acrylic thread today; plant-dyed cotton traditionally","forms":["Wayuu mochila"],"ctr":["Wayuu communities"],"auth":"made by Wayuu weavers; acrylic thread is standard today, not cotton","s":"https://en.wikipedia.org/wiki/Wayuu_people"},
{"n":"Bilum looping","g":"Textiles & rugs","r":"Papua New Guinea; also western New Guinea and the Solomon Islands","p":"","d":"Looped string bags, mostly made by women and sold in markets; the name also covers the technique.","tech":"knotless looping, fibre spun as it is looped","mat":"plant fibre, fur, wool, cotton, commercial yarn","forms":["Bilum"],"ctr":["Mount Hagen (Melpa)"],"auth":"looped, not knitted or crocheted; the fabric does not unravel round a break","s":"https://rotterdam.wereldmuseum.nl/en/collection-stories/bilum-multifunctional-bag-which-everything-fits"},
{"n":"Kiondo weaving","g":"Textiles & rugs","r":"Kenya","p":"","d":"Handwoven bags of vegetable twine with leather trim, indigenous to the Taita, Kikuyu and Kamba peoples.","tech":"hand weaving","mat":"vegetable twine, leather trim","forms":["Kiondo"],"ctr":["Taita, Kikuyu and Kamba communities"],"auth":"","s":"https://en.wikipedia.org/wiki/Kiondo"}]
json.dump(t,open(P+'A4_traditions.json.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'A4_traditions.json.tmp',P+'A4_traditions.json')
