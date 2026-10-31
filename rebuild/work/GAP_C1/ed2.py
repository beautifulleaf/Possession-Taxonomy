import json,os
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'out/C1.json'))
def K(n): return [k for dp in d['depts'] for s in dp['s'] for k in s['k'] if k['n']==n][0]
# ---- Swiss
sw=K('Swiss Army knife')
seen={e['n'].lower() for e in sw['x']}
for e in sw['x']:
    for v in e.get('v',[]): seen.add(v['n'].lower())
SRC={
'74 mm':("https://sakwiki.com/Victorinox+74mm","Ambassador;Cigar Cutter;Director;Escort;Executive;Money Clip;Prince;Swiss Beat MP3 Tool;Windsor;Accountant;Beginner;Student"),
'65 mm (Wenger)':("https://sakwiki.com/Wenger+65mm","AirTraveler;EvoGrip 81;Swiss Clipper AT;Bernina Mini Spot Light;Bottle Mate;Chairman;Crusader;Crusader Money Clip;Esquire;Esquire Money Clip;Executive Golf Pro;Lithos;Macao;OptiTool;Pocket Tech;Pocket Tool Chest;Swiss Clipper"),
'85 mm (Wenger and Delémont)':("https://sakwiki.com/Wenger+85mm+6plus+Layer+Models","Classic 30;Deer;Duck;Master Tool 13;Mountain Bike;Seafarer;SGT Shortix Plus;Survivor;Wenger 1.21.13;Wenger 1.22.03;Colonel;Lancelot;Monarch;Tool Chest;Champ;Matterhorn Original;Snap Shackle Large;Matterhorn Plus;SGT Fix-It;Serrated Tool Chest;Tool Chest Plus;Giant Knife;"
 "Bernina 504;Biker 36;Catch and Release;Deluxe Backpacker;Evolution 52;Evolution S557;Major;Master;Minathor;Shredder;Sierra;Swiss Outdoorsman;Troller;"
 "Apprentice 85;Canyon;Classic 66;Cigar Cutter Slimline;Commander;Evolution 10;Evolution 11;Footballer 32;Golf Pro;Highlander;Hobbyist;Ivanhoe;Junior 04;Junior 09;Junior S10 Scout;Junior S11 Scout;Junior 13;Pointer;RollerBlade;Signal;Titanium 2;Toilet Paper SAK;Trailblazer;Viking;"
 "Entree;Evolution 64;Junior 08;Junior 10;Patriot;Pheasant;Picnic;Premier;Titanium 1;Watchmaker 60;"
 "19th Hole Cigar Cutter;Alpine Backpacker;Wenger Angler;Backpacker;Backpacker II;Cascade;Cigar Cutter Standard;Classic 132;Classic 16;Computer Wiz;Cyclist;Deluxe Golf Pro;EVO S13;EVO 14;EVO 16;Footballer 30;Galahad Packlock;Gawain;Wenger Golfer;Highlander with Choke Tube Tool;Journeyman;Junior 02;Mustang;Orthodontic SAK;Pocket Mountain Bike;Snap Shackle Small;Snowboard;Spot Light;Swiss Sportsman;STGW 90;Teton;Titanium Ueli Steck;Traveler;Wenger Whistle;"
 "Cigar Cutter with Scissors;Double Blade;Evolution 17;Evolution 18;Evo Hunter 505;Fly Fisherman;Footballer 31;Junior 03;Junior EvoGrip 574;Laser with Scissors;Pathfinder;Safari;Sailfish;Skier;Skitour;Snowboarder;Spot Light with Scissors;Swiss Roller;Urban Survivor;Waterfowler;Zermatt;"
 "Evolution S101;Evolution S111;Evolution S13;Evolution 23;Evolution S52;Evolution 28;Evolution S54;Cigar 36 and 79"),
'130 mm (Wenger)':("https://sakwiki.com/Wenger+130mm+1+Layer+Models","Alinghi Rescue Knife;Ranger 51;Ranger 52;Ranger 53;Ranger 54;Ranger 60;Ranger 61;RangerWood 161;Swiss-Star Oboe Knife;Ranger 50;Ranger 80;Ranger 55;Ranger 56;Ranger 71 Gardener;Ranger 70 Handyman;Ranger 73 Electrician;Ranger 75 Handyman;Ranger 74 Handyman;Ranger 174 Touring;RangerGrip 182 Spearfishing;Alinghi 176;Alinghi 177;Alinghi 181;Mike Horn Ranger;Ranger 57 Hunter;Ranger 58 Hunter;RangerGrip 86 East Ranger;RangerGrip 90"),
'93 mm':("https://sakwiki.com/Victorinox+93mm+1+Layer+Models","Onefold Alox")}
new=[];n_add=0
for cls,(url,spec) in SRC.items():
    for nm in spec.split(';'):
        nm=nm.strip()
        if not nm or nm.lower() in seen: continue
        seen.add(nm.lower())
        mk='Victorinox' if cls in('74 mm','93 mm') else 'Wenger'
        new.append({"n":nm,"d":f"{mk} {cls.split(' (')[0]} Swiss Army knife model listed on SAKWiki.","mk":mk,"y":"","s":url,"g":cls,"v":[]})
ORD=["Soldier's knives","58 mm","65 mm (Wenger)","74 mm","84 mm","85 mm (Wenger and Delémont)","91 mm","93 mm","100 mm","111 mm","130 mm (Wenger)","Other civilian models"]
sw['x']=sorted(sw['x']+new,key=lambda e:ORD.index(e['g']) if e['g'] in ORD else 99)
n=len(sw['x'])
sw['sel']=("Follows the Victorinox article on Wikipedia (owner Victorinox-Stiftung 90 % and Carl und Elise Elsener-Gut Stiftung 10 %; Wenger taken over 26 April 2005) and the SAKWiki model pages for Victorinox 58, 74, 84 (1 to 4 layers), 91, 93, 100 and 111 mm and for Wenger 65, 85 (1 to 6+ layers) and 130 mm (1 to 4 layers). "
 f"Complete: {n} of {n} models on those pages. SAKWiki gives a year for only a few models; a name used at two lengths (Golfer, Companion, Picnicker, Pocket Pal, Director) is listed once. Left out: limited editions, sets, aliases, and the Delémont 65 and 130 mm pages, which re-badge Wenger models already listed. SAKWiki has no 75 mm or 84 mm five-layer page (it files the 84 and 85 mm knives under 84 mm to 4 layers and 85 mm).")
# ---- Veritas router plane
for e in K('Router plane')['x']:
    if e['n']=='Stanley No. 71':
        e.setdefault('v',[]).append({"n":"Veritas Router Plane","mk":"Veritas","y":"","d":"Veritas design based on the Stanley No. 71, with a closed mouth only, per a Machine Atlas review."}); e['dt']=e.get('dt') or 'maker version · year'
for n_ in ['Router plane']:
    k=K(n_); k['sel']=k['sel'].replace('Record and Veritas versions are not added','Veritas is added only for the router plane (Machine Atlas review); Lee Valley pages returned 429, so other Veritas planes and Record versions are not added')
# ---- Lockback
lb=K('Lockback folder')
lb['xg']='Maker'
def ent(n,mk,y,d,s,g,v=None):
    e={"n":n,"d":d,"mk":mk,"y":y,"s":s,"g":g,"v":v or []}
    if v: e['dt']='version · year'
    return e
lb['x']+= [
 ent('Buck 112 Ranger','Buck','',"Smaller Buck lockback folder, 4.25 in closed, with a 420HC clip blade.",'https://www.knifecountryusa.com/store/product/100177.100183/buck-112-ranger-lockback-folding-pocket-knife.html','Buck'),
 ent('Cold Steel Recon 1','Cold Steel','2000',"Cold Steel folder; redesigned with the Tri-Ad lock, a back lock with a stop pin, designed with Andrew Demko.",'https://www.offgridweb.com/gear/cold-steel-recon-1/','Cold Steel',[{"n":"Recon 1 with Tri-Ad lock","mk":"Cold Steel","y":"2018","d":"redesign ten years after the Tri-Ad lock appeared in 2008, per the article"}]),
 ent('Cold Steel Voyager','Cold Steel','',"Cold Steel folder sold with the Tri-Ad lock; the Large Voyager has a 4 in AUS-10A clip blade.",'https://www.knifecountryusa.com/store/product/326919.326924/cold-steel-29acz-large-voyager-tri-ad-lock.html','Cold Steel'),
 ent('Spyderco Delica','Spyderco','1990',"Spyderco folder with a back lock, made in Japan; redesigned as the Delica 4 in 2006.",'https://varusteleka.com/en/products/spyderco-delica-4-lightweight-folding-knife','Spyderco',[{"n":"Delica 4","mk":"Spyderco","y":"2006","d":"complete redesign of the Delica"}])]
lb['x'].sort(key=lambda e:(e['g'],e['y'] or '9999'))
lb['sel']=("No complete list exists; follows the Buck Knives and Cold Steel articles on Wikipedia, the Lock knife article (Buck popularised the lockback in the 1960s) and one retailer or review page per added model. "
 "Cold Steel's Tri-Ad lock is a back lock with a stop pin. Kershaw Leek: retailer pages disagree (frame lock on one, liner lock on others), so it is not placed. Spyderco Worker (first folder, 1981): no fetched page states its lock (Spyderco catalogue URLs returned 404).")
# ---- Mora
k=K('Fixed-blade EDC & bushcraft knife')
k['sel']=k['sel'].replace(' (searched twice: Mora knife article, Morakniv search; no year found)',' (searched four times: Mora knife article, two searches and Morakniv\'s own history page, which dates the Mora 2000 to 1991 and the Jagaren to 1975 but gives no year for the models listed)')
for e in k['x']:
    pass
# Mora Outdoor 2000 year 1991
for e in k['x']:
    if e['n']=='Mora Outdoor 2000':
        e['y']='1991'; e['s']='https://www.morakniv.com/en-ca/blogs/knife-history/about-morakniv'; e['d']=(e['d'].rstrip('.')+'; Morakniv\'s history page dates the Mora 2000 outdoor knife to 1991.')
json.dump(d,open(R+'work/GAP_C1/t.tmp','w'),ensure_ascii=False,indent=1);os.replace(R+'work/GAP_C1/t.tmp',R+'out/C1.json')
print(len(new),n)
