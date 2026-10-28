import json,os,copy
R='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(R+'B10.json')); B=json.load(open(R+'B10_brands.json')); T=json.load(open(R+'B10_traditions.json'))
def cnt(d):
    k=a=m=0
    for dp in d['depts']:
        for s in dp['s']:
            for x in s['k']:
                k+=1;a+=len(x.get('x',[]));m+=len(x.get('m',[]))+len(x.get('r',[]))
    return k,a,m
before=cnt(d);print('before',before)
D={dp['n']:dp for dp in d['depts']}
def shelf(dp,n): return next(s for s in D[dp]['s'] if s['n']==n)
def kind(sh,n): return next(k for k in sh['k'] if k['n']==n)
def dedupe(l):
    o=[]
    for i in l:
        if i not in o:o.append(i)
    return o
def interleave(lists,cap=8):
    out=[];i=0
    while len(out)<cap and any(i<len(l) for l in lists):
        for l in lists:
            if i<len(l) and len(out)<cap and l[i] not in out: out.append(l[i])
        i+=1
    return out
# B10-6 ADA merge
def fixmk(o):
    if isinstance(o,dict):
        for k,v in o.items():
            if k=='mk' and v=='Aqua Design Amano': o[k]='ADA'
            else: fixmk(v)
    elif isinstance(o,list):
        for v in o: fixmk(v)
fixmk(d)
bs=B['b']; ada=next(x for x in bs if x['n']=='ADA'); ada2=next(x for x in bs if x['n']=='Aqua Design Amano')
for f in('lines','eras','sig','sc','rel'): ada[f]=dedupe(ada.get(f,[])+ada2.get(f,[]))
ada['d']="Aqua Design Amano, founded by Takashi Amano; makers of Nature Aquarium tanks, lights, soils and supplies and organisers of the International Aquatic Plant Layout Contest."
bs.remove(ada2)
# B10-4 dog food
sh=shelf('Dogs','Dog food & treats'); ks={k['n']:k for k in sh['k']}
dry,wet,fresh,fd,vet=[ks[n] for n in('Dry dog food','Wet dog food','Fresh, frozen and raw dog food','Freeze-dried and air-dried dog food','Veterinary dog food')]
food={"n":"Dog food","a":"complete dog food","d":"Complete food made for dogs, sold as dry, wet, fresh, freeze-dried or veterinary diets.",
 "t":["dry (kibble)","wet","fresh, frozen and raw","freeze-dried and air-dried","veterinary","puppy","adult","senior","small breed","large breed","grain-free","single protein","hypoallergenic"],
 "s":dry['s'],"m":dry['m'][:3]+wet['m'][:2]+fresh['m'][:1]+fd['m'][:1]+vet['m'][:1],"r":dry.get('r',[])}
tr,dc,lc=ks['Dog treats'],ks['Dog dental chews'],ks['Long-lasting dog chews']
treats={"n":"Dog treats and chews","a":"dog treats · dental chews · long-lasting chews","d":"Complementary snacks and chews for dogs, not intended as a complete diet.",
 "t":dedupe(["treats","dental chews","long-lasting chews"]+tr.get('t',[])+lc.get('t',[])),"s":tr['s'],"m":tr['m'][:3]+dc['m'][:3]+lc['m'][:2]}
sh['k']=[food,treats]
# B10-5 dog toys
sh=shelf('Dogs','Toys, sport & clean-up'); ks={k['n']:k for k in sh['k']}
names=['Dog chew toys','Dog fetch toys','Dog puzzle and treat-dispensing toys','Plush dog toys','Dog rope and tug toys']
src=[ks[n] for n in names]
toy={"n":"Dog toy","a":"chew toys · fetch toys · puzzle toys · plush toys · tug toys","d":"A toy made for a dog to chew, fetch, tug or work at for food.",
 "t":dedupe(["chew","fetch","puzzle and treat-dispensing","plush","rope and tug"]+[t for k in src for t in k.get('t',[])]),
 "s":src[0]['s'],"x":[a for k in src for a in k.get('x',[])],
 "m":interleave([k.get('m',[]) for k in src]),"r":[r for k in src for r in k.get('r',[])]}
if not toy['r']: del toy['r']
# agility
ag=ks['Dog agility equipment']
ag['t']=dedupe([a['n'] for a in ag['x']]+ag['t']); del ag['x']
ag['n']='Agility equipment'
i=sh['k'].index(ks['Dog chew toys'])
sh['k']=[toy]+[k for k in sh['k'] if k['n'] not in names]
D['Dogs']['note']="Agility and gundog training are pursuits; their obstacles and gear are listed here as objects and cross-link to the Physical pursuits taxonomy."
# reptile heat lamp
sh=shelf('Reptiles, amphibians & invertebrates','Heating & lighting'); ks={k['n']:k for k in sh['k']}
src=[ks[n] for n in('Basking lamp','Deep heat projector','Ceramic heat emitter')]
lamp={"n":"Reptile heat lamp","a":"basking lamp · heat lamp · deep heat projector · ceramic heat emitter","d":"A lamp or emitter that gives a reptile a heated basking spot or background warmth.",
 "t":dedupe(["basking spot lamp","deep heat projector","ceramic heat emitter"]+src[0].get('t',[])),"s":src[0]['s'],
 "x":[a for k in src for a in k.get('x',[])],"m":dedupe([m for k in src for m in k.get('m',[])])}
sh['k']=[lamp]+[k for k in sh['k'] if k not in src]
# B10-7 bird bath
sh=shelf('Birds','Wild bird food, baths & nest boxes'); sh['k']=[k for k in sh['k'] if k['n']!='Bird bath']; sh['n']='Wild bird food & nest boxes'
D['Birds']['note']="Bird baths are listed under Garden ornaments (B4)."
# B10-4 cap horse and aquarium lists
for dn in('Horses & riding','Aquariums & ponds'):
    for s in D[dn]['s']:
        for k in s['k']:
            if len(k.get('m',[]))>8: k['m']=k['m'][:8]
            if len(k.get('r',[]))>8: k['r']=k['r'][:8]
# B10-1 aquarium kinds
ctl={"n":"Aquarium controller","a":"reef controller · aquarium computer","d":"Unit that monitors probes and switches pumps, heaters and lights, with alarms and remote access.",
 "t":["pH probe","ORP probe","temperature probe","salinity probe","expansion modules"],"s":"https://www.bulkreefsupply.com/content/post/a-buyers-guide-to-neptune-systems-apex-aquarium-controllers",
 "x":[{"n":"Neptune Apex","a":"Apex","d":"Reef controller family with Apex Fusion app control and expansion modules.","mk":"Neptune Systems","y":"","s":"https://www.bulkreefsupply.com/content/post/a-buyers-guide-to-neptune-systems-apex-aquarium-controllers",
   "v":[{"n":"A2 Apex","mk":"Neptune Systems","y":"","d":"previous generation, out of production"},{"n":"A2 ApexEL","mk":"Neptune Systems","y":"","d":"previous generation, entry level"},{"n":"A3 Apex Pro","mk":"Neptune Systems","y":"","d":"4 FMM inputs, built-in ORP and level monitoring, Ethernet"},{"n":"A3 Apex","mk":"Neptune Systems","y":"","d":"3 FMM inputs, 8 controllable outlets"},{"n":"A3 Apex Jr","mk":"Neptune Systems","y":"","d":"entry model, 2 FMM inputs"}],
   "dt":"probes (pH, ORP, temperature, salinity) · outlets via Energy Bar · expansion modules"},
  {"n":"GHL ProfiLux","a":"ProfiLux","d":"German aquarium controller for lighting, water chemistry, pumps, dosing and feeding.","mk":"GHL","y":"1998","s":"https://www.aquariumcomputer.com/products/profilux-4/",
   "v":[{"n":"ProfiLux 3","mk":"GHL","y":"","d":"earlier generation, takes expansion cards"},{"n":"ProfiLux 4","mk":"GHL","y":"","d":"32 lighting channels, 16 pump channels, WiFi"},{"n":"ProfiLux 4.1","mk":"GHL","y":"","d":"adds a LAN port"}],
   "dt":"probes (temperature, pH, redox, conductivity) · expansion cards · GHL Doser and KH Director"}]}
vac={"n":"Gravel vacuum","a":"aquarium siphon · gravel cleaner","d":"Tube and hose that siphons waste out of the substrate during a water change.","t":["gravity siphon","battery-powered","pump-driven"][:1]+[],"s":"https://aquariumcoop.com/blogs/aquarium/aquarium-siphon"}
vac['t']=["tube and hose siphon"]
mag={"n":"Algae magnet","a":"magnetic algae scraper · magnetic glass cleaner","d":"Two-part magnet scraper: an outer magnet dragged over the glass moves the inner scraper that removes algae.","t":["glass","acrylic","floating inner magnet"],"s":"https://www.bulkreefsupply.com/mag-float-350-large-glass-aquarium-cleaner-mag-float.html"}
net={"n":"Aquarium net","a":"fish net · breeder net","d":"Handled frame and mesh for catching fish or lifting out debris.","t":["coarse nylon","fine mesh","soft fabric","breeder net","extended handle"],"s":"https://www.furrycritter.com/pages/articles/fish/fish_nets.htm"}
D['Aquariums & ponds']['s'].insert(2,{"n":"Controllers & maintenance","k":[ctl,vac,mag,net]})
# B10-2 yard shelf
yard=[{"n":"Tack trunk","a":"tack box · show trunk","d":"Storage chest for saddles, bridles, pads and boots, often on wheels for shows.","t":["rolling","wooden","plastic","with shelves and pull-outs"],"s":"https://proequinegrooms.com/tips/equipment-and-tack/tack-trunks/"},
{"n":"Saddle rack","a":"saddle bracket","d":"Wall-mounted or portable support that holds a saddle off the floor.","t":["wall-mount collapsible","portable show rack","carousel (rotary)"],"s":"https://www.sstack.com/blogs/stable/top-tack-racks-for-small-tack-rooms"},
{"n":"Bridle rack","a":"bridle bracket","d":"Hooks or arms that hold bridles and halters on a wall or stall.","t":["swivel multi-hook","horseshoe","basket and hooks","portable"],"s":"https://www.sstack.com/blogs/stable/top-tack-racks-for-small-tack-rooms"},
{"n":"Mounting block","a":"mounting step","d":"Raised platform, often with steps, that helps a rider mount with less strain on the stirrup and saddle.","s":"https://en.wikipedia.org/wiki/Mounting_block"},
{"n":"Show jump and cavaletti","a":"jump poles · jump standards","d":"Poles on upright standards, and small cavaletti, set up for schooling and jumping horses at home.","t":["cavaletti","vertical","oxer","poles and standards"],"s":"https://en.wikipedia.org/wiki/Show_jumping"}]
D['Horses & riding']['s'].append({"n":"Yard & tack room","k":yard})
# brands
bs+= [{"n":"Neptune Systems","c":"United States","f":"","seg":"Professional & flagship","d":"Maker of Apex aquarium controllers and Energy Bar power modules.","lines":["Apex","Energy Bar"],"eras":[],"sig":["Neptune Apex"],"sc":[],"rel":[],"s":"https://www.neptunesystems.com/","kf":"reef controllers"},
 {"n":"GHL","c":"Germany","f":"","seg":"Professional & flagship","d":"German maker of ProfiLux aquarium controllers, developed since 1998.","lines":["ProfiLux","Doser","KH Director"],"eras":[],"sig":["GHL ProfiLux"],"sc":[],"rel":[],"s":"https://www.aquariumcomputer.com/products/profilux-4/","kf":"aquarium controllers"}]
bs.sort(key=lambda x:x['n'].lower())
# traditions
T['t']+=[
{"n":"Nishikigoi breeding (Niigata)","g":"Animal breeding","r":"Nijūmuragō, Ojiya and Yamakoshi, Niigata Prefecture, Japan","p":"from the 1820s","d":"Farmers in the 'twenty villages' bred red and white carp with black ones to produce the first coloured koi.","tech":"selective breeding","mat":"","forms":["Kōhaku","Taishō Sanshoku","Shōwa Sanshoku"],"ctr":["Ojiya","Yamakoshi"],"auth":"","s":"https://en.wikipedia.org/wiki/Nishikigoi"},
{"n":"Vaquero saddlery","g":"Leather & saddlery","r":"Iberia, New Spain (Mexico), south-west United States","p":"16th to 19th centuries","d":"Horseback herding equipment brought from Iberia to New Spain, the basis of North American cowboy tack.","tech":"hand-worked leather and rawhide","mat":"leather, rawhide, horsehair","forms":["Western saddle","Bosal and mecate","Spade bit","Reata and romal"],"ctr":[],"auth":"","s":"https://en.wikipedia.org/wiki/Vaquero"},
{"n":"Buckaroo tack (California and Great Basin)","g":"Leather & saddlery","r":"California and the Great Basin, United States","p":"19th century to present","d":"Californian cowboy (buckaroo) tradition that kept vaquero methods and gear in use in the Great Basin.","tech":"","mat":"leather, rawhide","forms":["Bosalito","Spade bit"],"ctr":[],"auth":"","s":"https://en.wikipedia.org/wiki/Vaquero"},
{"n":"Paniolo saddlery (Hawaii)","g":"Leather & saddlery","r":"Hawaii","p":"from 1832","d":"Hawaiian ranching tradition that grew after Mexican vaqueros were invited in 1832, with its own saddle, the noho lio.","tech":"","mat":"leather","forms":["Noho lio"],"ctr":[],"auth":"","s":"https://en.wikipedia.org/wiki/Vaquero"},
{"n":"Australian stock saddlery","g":"Leather & saddlery","r":"Australia","p":"1830s to present","d":"Saddlery developed from the English park saddle, with deeper seat, higher cantle and knee pads for rough country.","tech":"stuffed knee rolls, English-style panels","mat":"leather","forms":["Australian stock saddle","Wagga saddle","Poley"],"ctr":["Wagga Wagga","Miriam Vale, Queensland"],"auth":"","s":"https://en.wikipedia.org/wiki/Australian_stock_saddle"},
{"n":"Sheridan Western leatherwork","g":"Leather & saddlery","r":"Sheridan, Wyoming, United States","p":"","d":"Wyoming town whose King's Saddlery Museum displays Western leather work, especially saddles.","tech":"","mat":"leather","forms":["Western saddle"],"ctr":["King's Saddlery Museum"],"auth":"","s":"https://en.wikipedia.org/wiki/Sheridan,_Wyoming"}]
after=cnt(d);print('after',after)
for f,o in(('B10.json',d),('B10_brands.json',B),('B10_traditions.json',T)):
    json.dump(o,open(R+f+'.tmp','w'),indent=1,ensure_ascii=False); os.replace(R+f+'.tmp',R+f)
