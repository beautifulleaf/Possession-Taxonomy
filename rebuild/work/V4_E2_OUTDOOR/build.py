import json,csv,re,collections,sys
R='/home/user/Possession-Taxonomy/'
old=json.load(open(R+'rebuild/work/V4_E2_OUTDOOR/old.json'))
rows=[r for r in csv.DictReader(open(R+'data/named_forms.tsv'),delimiter='\t') if r['kind_id'].startswith('E2.')]
idx=collections.defaultdict(list)
for r in rows: idx[r['name'].lower()].append(r)
brands={b['n'] for b in json.load(open(R+'rebuild/out/E2_brands.json'))['b']}
WP='https://en.wikipedia.org/wiki/'
# owner facts from fetched pages: maker -> (own, tier, cty, own_y)
OWN={
 'Shimano':('Shimano','National champion','Japan',''),
 'G. Loomis':('Shimano','Global group','United States','1997'),
 'Rapala':('Rapala VMC Corporation','Global group','Finland',''),
 'Storm':('Rapala VMC Corporation','Global group','',"1999"),
 'Abu Garcia':('Pure Fishing','Global group','Sweden','2019'),
 'Berkley':('Pure Fishing','Global group','United States','2019'),
 'Penn Fishing':('Pure Fishing','Global group','United States','2019'),
 'Penn':('Pure Fishing','Global group','United States','2019'),
 'Shakespeare':('Pure Fishing','Global group','United States','2019'),
 'Black Diamond':('Clarus Corporation','Independent','United States','2010'),
 'Pieps':('Clarus Corporation','Independent','','' ),
 'Petzl':('Petzl','Independent','France',''),
 'Burton':('Burton Snowboards','Independent','United States',''),
 'The North Face':('VF Corporation','Global group','United States','2000'),
 'Timberland':('VF Corporation','Global group','','2011'),
 'Smartwool':('VF Corporation','Global group','','2011'),
 'JanSport':('VF Corporation','Global group','','1986'),
 'Salomon':('Amer Sports','Global group','France','2005'),
 'Atomic':('Amer Sports','Global group','Austria','1994'),
 "Arc'teryx":('Amer Sports','Global group','',''),
 'Scubapro':('Johnson Outdoors','Global group','','1997'),
 'Jetboil':('Johnson Outdoors','Global group','United States','2012'),
 'Eureka':('Johnson Outdoors','Global group','','1973'),
 'Old Town':('Johnson Outdoors','Global group','','2004'),
 'Humminbird':('Johnson Outdoors','Global group','United States',''),
 'Minn Kota':('Johnson Outdoors','Global group','',''),
}
def ownkeys(mk):
    for k,v in OWN.items():
        if mk and (mk==k or mk.startswith(k+' ') or k==mk.replace(' Fishing','')):
            return v
    return None
# new canon entries: kind -> list of entry dicts
def E(n,d,g,mk='',y='',s='',role=None,a='',v=None):
    e={'n':n,'a':a,'d':d,'mk':mk,'y':y,'s':s,'v':v or [],'g':g}
    if role: e['role']=role
    return e
AF=WP+'Artificial_fly'
fly=[]
for sec,items in [
 ('Dry fly',[('Royal Wulff','Dry fly created by Lee Wulff.','Lee Wulff'),('Blue-Winged Olive','Dry fly imitating the blue-winged olive mayfly.',''),('Orange Stimulator','Dry attractor fly in orange.',''),('Stimulator','Attractor dry fly of the Stimulator style.',''),('Tasmanian Red Tag','Dry fly with a red tag.',''),('Blue-Winged Olive Quill','Quill-bodied dry fly of the blue-winged olive.','')]),
 ('Wet fly',[('Alexandra','Classic wet fly.',''),('Grizzly King','Classic soft-hackle wet fly.',''),('Woolly Worm','Hackled wet fly with a chenille body.',''),('Professor','Classic wet fly.',''),('Partridge and Orange','Soft-hackle wet fly with a partridge hackle.',''),('Coachman','Wet trout fly credited to Tom Bosworth.','Tom Bosworth')]),
 ('Nymph',[("Brook's Montana Stonefly Nymph",'Stonefly nymph by Charles Brooks.','Charles Brooks'),('Bead Head Prince Nymph','Weighted bead-head nymph.',''),("Gold Ribbed Hare's Ear Nymph",'Classic nymph.',''),('Pheasant Tail Nymph','Classic mayfly nymph.',''),('Copper John','Weighted nymph by John Barr.','John Barr')]),
 ('Streamer',[('Royal Coachman Bucktail','Streamer version of the Royal Coachman.',''),('Mickey Finn','Bucktail streamer.',''),('Black Conehead Egg Sucking Leech','Weighted leech streamer.',''),("Schenk's White Minnow",'Minnow streamer.','')]),
 ('Saltwater fly',[("Lefty's Deceiver",'Saltwater streamer by Lefty Kreh.','Lefty Kreh'),('Cockroach Deceiver','Deceiver variant by Lefty Kreh.','Lefty Kreh'),('Gold Bendback Shrimp Fly','Shrimp pattern for saltwater.',''),('Surf Candy','Saltwater baitfish pattern.',''),('Crazy Charlie','Bonefish fly by Charlie Smith.','Charlie Smith'),('Bonefish Shrimp Fly','Shrimp pattern for bonefish.',''),('Stu Apte Tarpon Fly','Classic tarpon fly by Stu Apte.','Stu Apte')]),
 ('Salmon fly',[('Durham Ranger','Classic Atlantic salmon fly.',''),('Green Highlander','Salmon fly dated 1914 by the article.',''),('Jock Scott','Salmon fly dated 1850 by the article.','')]),
 ('Terrestrial and warm-water fly',[("Dave's Hopper",'Grasshopper pattern by Dave Whitlock.','Dave Whitlock'),('Mouse Fly','Mouse pattern.',''),('Red Bass Popper','Popper for bass and panfish.',''),("Barry's Carp Fly",'Carp pattern.',''),("Parks' Salmonfly",'Salmonfly pattern by Merton Parks.','Merton Parks'),('Carey Special','Pattern by Colonel Carey.','Colonel Carey'),('Dahlberg Diver','Diver pattern by Larry Dahlberg.','Larry Dahlberg')]),
]:
    for n,d,mk in items:
        y={'Green Highlander':'1914','Jock Scott':'1850'}.get(n,'')
        fly.append(E(n,d,sec,mk,y,AF))
NEW={
 'Artificial fly':fly,
 'Surfboard':[E(n,d,'Board shape',mk,y,WP+'Surfboard') for n,d,mk,y in [
  ('Shortboard','Board 180 to 210 cm long; rise linked to the late 1960s urethane foam.','',''),
  ('Hybrid surfboard','Board 180 to 260 cm with a rounder profile.','',''),
  ('Mid-length surfboard','Board 177 to 200 cm long.','',''),
  ('Funboard','Board 210 to 240 cm long.','',''),
  ('Gun','Big-wave board 210 to 370 cm long.','',''),
  ('Longboard surfboard','Single-fin board 270 to 370 cm long.','',''),
  ('2+1 longboard','Longboard with a centre fin and two side fins.','',''),
  ('Mini tanker','Shortened longboard.','',''),
  ('Malibu','Narrower longboard named after Malibu, California.','',''),
  ('Tandem surfboard','Oversized longboard for two riders.','','')]],
 'Kitesurf kite':[E(n,d,'Kite class',mk,y,WP+'Kitesurfing') for n,d,mk,y in [
  ('Leading edge inflatable (C-kite)','C-shaped inflatable kite with a narrow wind range.','Bruno and Dominique Legaignoux','1987'),
  ('Bow kite','Flat inflatable kite with a concave trailing edge that depowers fully; developed 2005.','','2005'),
  ('Delta kite','Bow kite with a straight trailing edge and a triangular outline.','',''),
  ('Supported leading edge kite (SLE hybrid)','Second-generation flat inflatable kite; developed 2006.','','2006'),
  ('Foil kite','Fabric kite with air cells and a fixed bridle, like a paraglider.','','')]],
 'Kiteboard':[E(n,d,'Board type',mk,y,WP+'Kitesurfing') for n,d,mk,y in [
  ('Twin-tip kiteboard','Bidirectional board like a wakeboard; the easiest to learn on.','',''),
  ('Directional kiteboard','Surf-style board for waves.','',''),
  ('Wakestyle kiteboard','Board with bindings for wakestyle tricks.','',''),
  ('Hybrid kiteboard','Board that goes either way but performs better in one.','',''),
  ('Skim-type kiteboard','Board of skim type.','',''),
  ('Race kiteboard','Directional board with long fins for course racing.','','')]],
 'Paraglider':[E(n,d,'Wing class','','',WP+'Paragliding') for n,d in [
  ('Recreational paraglider','Wing with a glide ratio of about 9.3.'),
  ('Competition paraglider','Wing with a glide ratio of about 11.3, up to 13 in some cases.'),
  ('Tandem paraglider','Larger wing for a pilot and one passenger.'),
  ('Speed wing','Small fast wing not normally able to soar.'),
  ('Parakite','Hybrid of paraglider and kite wing with a reflex profile.'),
  ('Hike-and-fly kit','Ultralight set-up that can weigh under 5 kg.')]],
 'Skateboard deck':[E(n,d,'Deck shape','','',WP+'Skateboard_deck') for n,d in [
  ('Popsicle deck','Common deck sold in widths of about 7.5 to 9 inches.'),
  ('Longboard deck','Deck usually over 36 inches long, for speed and rough surfaces.'),
  ('Penny board deck','Plastic deck about 22 inches long.'),
  ('Nickel board deck','Larger penny-style deck over 27 inches long.'),
  ('Old-school deck','Wider deck of the 1970s and 1980s shape, often with one kicktail.')]],
 'Snowboard':[E(n,d,g,mk,y,WP+'Snowboard',role) for n,d,g,mk,y,role in [
  ('Sims','Snowboard maker founded by Tom Sims; released reverse camber in 1985.','Maker','Sims','1985',None),
  ('Barfoot Snoboards','Snowboard maker founded by Chuck Barfoot in 1981.','Maker','Barfoot Snoboards','1981',None),
  ('Garski','First fibreglass snowboard with binding, built by Gary Tracy.','Maker','Gary Tracy','1982',None),
  ('Kemper Snowboards','Snowboards built by David Kemper from 1983.','Maker','Kemper Snowboards','1983',None),
  ('Flite Snowboards','Pressed the first closed-moulded boards in the mid-1980s.','Maker','Flite Snowboards','',None),
  ('GROMEL','First Russian snowboard maker, founded 1988.','Maker','GROMEL','1988',None),
  ('Powder snowboard','Highly directional board with a rockered nose and tapered shape.','Board shape','','',None),
  ('Park and jib snowboard','Twin-tip board for park and jib riding.','Board shape','','',None)]],
 'Camming device':[E(n,d,'Maker or lineage',mk,y,WP+'Spring-loaded_camming_device') for n,d,mk,y in [
  ('Abalakov Cam','Cam credited to Vitaly Abalakov.','Vitaly Abalakov',''),
  ('Technical Friend','Cam named on the article.','',''),
  ('Metolius Power Cam','Cam named on the article.','Metolius',''),
  ('DMM 4CU','Cam named on the article.','DMM',''),
  ('Trango FlexCam','Cam named on the article.','Trango','')]],
 'Belay device':[E(n,d,'Maker or lineage',mk,y,WP+'Belay_device') for n,d,mk,y in [
  ('Figure-eight','Descender and belay device; DMM sells a variant, the cardiac arrester.','',''),
  ('Petzl GriGri 2','Newer, smaller GriGri.','Petzl',''),
  ('Cinch','Belay device named on the article.','',''),
  ('Silent Partner','Self-belay device sold by Wren Industries.','Wren Industries','')]],
}
SKIP_ROLE={'Wild Country Friend':'origin','Snurfer':'origin'}
def kl(n): return n[0].lower()+n[1:] if not n[:2].isupper() else n
def first_url(s):
    m=re.search(r'https?://\S+',s or ''); return m.group(0).rstrip(';,') if m else ''
dropped=[]; stats=collections.Counter()
newbrands=[]
def conv_kind(k,dname):
    k=json.loads(json.dumps(k)); x=k.get('x',[])
    have={e['n'].lower() for e in x}
    allnames=' '.join(have)
    for e in x:
        e.setdefault('g',e.get('mk') or 'Unattributed')
        if e['n'] in SKIP_ROLE: e['role']=SKIP_ROLE[e['n']]; stats['role']+=1
        o=ownkeys(e.get('mk',''))
        if o:
            e['own'],e['tier'],e['cty']=o[0],o[1],o[2]
            if o[3]: e['own_y']=o[3]
    srcfallback=k.get('s') or (x[0]['s'] if x else '')
    for name,mk in k.pop('m',[]) or []:
        full=name if (not mk or mk.lower().split()[0] in name.lower()) else f'{mk} {name}'
        if full.lower() in have or name.lower() in have: stats['dupm']+=1; continue
        rs=idx.get(name.lower(),[])
        src='';y=''
        for r in rs:
            u=first_url(r['sources'])
            if u: src=u; y=r['first_year'] if (r['first_year'] or '').isdigit() else ''; break
        if not src: src=first_url(k.get('s')) or ''; 
        if not src: dropped.append((k['n'],name,mk)); continue
        stats['m_ok' if rs else 'm_kindsrc']+=1
        e={'n':full,'a':'','d':f'{kl(k["n"]).capitalize()} model from {mk}.' if mk else f'{kl(k["n"]).capitalize()} model.','mk':mk,'y':y,'s':src,'v':[],'g':mk or 'Unattributed'}
        o=ownkeys(mk)
        if o:
            e['own'],e['tier'],e['cty']=o[0],o[1],o[2]
            if o[3]: e['own_y']=o[3]
        x.append(e); have.add(full.lower())
    for e in NEW.get(k['n'],[]):
        if e['n'].lower() in have or any(e['n'].lower()==h.split(' ',1)[-1] for h in have): stats['dupnew']+=1; continue
        x.append(e); have.add(e['n'].lower()); stats['new']+=1
    if x:
        k['x']=x
        if not k.get('s'): k['s']=x[0]['s']
        n=len(x)
        cat=collections.Counter(e['g'] for e in x)
        k['nl']=f'One entry is a named {kl(k["n"])} line, model or maker product sold under its own name; sizes and revisions are versions.'
        extra=''
        if k['n']=='Artificial fly': k['nl']='One entry is a named fly pattern tied to a recipe; size and colour variants are versions.'; extra=' Patterns named by the fetched Wikipedia article Artificial fly, by type. Covers %d patterns; no Wikipedia list-of-patterns page could be fetched (404), so the pattern canon is the article\'s named examples, not a complete list.'%n
        elif k['n'] in NEW: extra=' Classes and shapes named by a fetched Wikipedia article (see each entry); covers %d entries, not a complete canon of the field.'%n
        k['sel']=('Models and lines named by the retail catalogue pages and reference pages fetched in the structure and earlier passes (each entry carries its page); no whole-space reference lists this kind.'+extra+' Covers %d named entries.'%n) if True else ''
        k['xg']='by maker' if len(cat)>1 and not (k['n'] in NEW) else 'by section: '+', '.join(list(cat)[:6])
        # order within group by year then name
        x.sort(key=lambda e:(e['g'],e.get('y') or '9999',e['n']))
    else:
        k.pop('x',None)
    if k.get('r'):
        mks={e.get('mk') for e in x}
        k['r']=[r for r in k['r'] if r[1] in mks or any(r[0].split()[0].lower() in e['n'].lower() for e in x)]
        if not k['r']: k.pop('r')
    return k
out=[]
MS={
 'Fishing & hunting':('Market facts for fishing tackle from the makers\' own Wikipedia pages, fetched on the date of this pass; no tackle-wide market report was fetched, so shares are not given.',[
  {'mkt':'Fishing tackle and bicycle components','who':'Shimano','share':'23.3 % of sales (US$2.872 billion total)','yr':2024,'s':WP+'Shimano','note':'fishing tackle share of company revenue; spinning reels are its top-selling fishing series'},
  {'mkt':'Fishing tackle','who':'Pure Fishing (Sycamore Partners)','share':'owner since January 2019','yr':2019,'s':WP+'Pure_Fishing','note':'brands named by the page: Abu Garcia, Berkley, Penn, Shakespeare, Ugly Stik; Svendsen Sport (Savage Gear, Prologic, Madcat, DAM) added February 2022'},
  {'mkt':'Fishing tackle','who':'Rapala VMC Corporation','share':'acquisitions 1999 to 2023','yr':2023,'s':WP+'Rapala','note':'brands named: VMC 2000, Storm 1999, Sufix 2008, Terminator 2007, Luhr Jensen 2005, 13 Fishing 2019 and 2023, Okuma (Europe and Russia) 2021'},
  {'mkt':'Fish finders and outboard trolling motors','who':'Johnson Outdoors','share':'US$592 million company sales','yr':2025,'s':WP+'Johnson_Outdoors','note':'infobox figure; the same page\'s introduction says "more than $315 million", so the two disagree; Humminbird, Minn Kota and Cannon are its brands'}]),
 'Camping & hiking':('Group ownership of camping brands from the owners\' Wikipedia pages.',[
  {'mkt':'Outdoor, active and work apparel and gear','who':'VF Corporation','share':'US$10.45 billion revenue','yr':2024,'s':WP+'VF_Corporation','note':'brands include The North Face (acquired 2000), JanSport (1986), Eastpak (2000), Napapijri (2004), Timberland (2011), Smartwool (2011), Icebreaker (2018)'},
  {'mkt':'Sporting goods and outdoor','who':'Amer Sports','share':'US$5.18 billion revenue','yr':2024,'s':WP+'Amer_Sports','note':'owners: Anta Sports 44.5 %, Chip Wilson 16.3 %, FountainVest 12.7 %, Tencent 4.5 %; brands include Salomon (2005), Atomic (1994), Arc\'teryx, Peak Performance (2018)'},
  {'mkt':'Camping and marine equipment','who':'Johnson Outdoors','share':'brands Jetboil (2012), Eureka! (1973), Old Town (2004)','yr':2025,'s':WP+'Johnson_Outdoors','note':'sold its North American Silva compass rights in 2018'}]),
 'Climbing & caving':('Climbing hardware ownership from the makers\' Wikipedia pages; no market share figure was fetched.',[
  {'mkt':'Climbing hardware','who':'Clarus Corporation (Black Diamond)','share':'bought for US$90 million','yr':2010,'s':WP+'Black_Diamond_Equipment','note':'Black Diamond founded 1989 from Chouinard Equipment assets; Clarus also owns Pieps; Gregory was bought in 2010 and sold in 2014'},
  {'mkt':'Climbing and headlamp equipment','who':'Petzl','share':'1,200 employees','yr':2025,'s':WP+'Petzl','note':'family-led company at Crolles near Grenoble; GriGri first produced in 1991'}]),
 'Water, wind & air sports':('Diving and water-sport ownership from the owners\' Wikipedia pages.',[
  {'mkt':'Diving equipment','who':'Johnson Outdoors (Scubapro)','share':'Scubapro merged with Uwatec 1997','yr':1997,'s':WP+'Johnson_Outdoors','note':'Subgear bought by Scubapro 2007; Ocean Kayak bought 1997'},
  {'mkt':'Sporting goods and outdoor','who':'Amer Sports','share':'US$5.18 billion revenue','yr':2024,'s':WP+'Amer_Sports','note':'Suunto sold in 2022 to Liesheng'}]),
 'Snow, ice & wheels':('Snow-sports market figures from the makers\' Wikipedia pages; the only share figures on those pages are Burton\'s.',[
  {'mkt':'Snowboard equipment, US','who':'Burton Snowboards','share':'40 to 45 % of a US$236 million market','yr':2013,'s':WP+'Burton_Snowboards','note':'estimate by Donna Carpenter as the page states; in 2008 the page gives US$487 million and a 40 to 70 % share by category'},
  {'mkt':'Bicycle components','who':'Shimano','share':'about 85 % by value','yr':2024,'s':WP+'Shimano','note':'the page says "estimated at 85 % of the global bicycle component market by value"; US$2.872 billion total revenue'},
  {'mkt':'Skis and winter sports','who':'Amer Sports (Atomic, Salomon)','share':'Atomic acquired 1994, Salomon 2005','yr':2024,'s':WP+'Amer_Sports','note':'group revenue US$5.18 billion'}]),
}
for dp in old:
    nd={k:v for k,v in dp.items() if k not in ('s',)}
    nd['s']=[]
    for sh in dp['s']:
        ns={k:v for k,v in sh.items() if k!='k'}
        ns['k']=[conv_kind(k,dp['n']) for k in sh['k']]
        nd['s'].append(ns)
    nd['msum'],nd['ms']=MS[dp['n']][0],MS[dp['n']][1]
    out.append(nd)
OB={'Johnson Outdoors':('United States','Global group'),'VF Corporation':('United States','Global group'),'Amer Sports':('Finland','Global group'),'Pure Fishing':('United States','Global group'),'Rapala VMC Corporation':('Finland','Global group'),'Clarus Corporation':('United States','Independent'),'Burton Snowboards':('United States','Independent'),'Sycamore Partners':('United States','Independent')}
FD={'VF Corporation':'1899','Amer Sports':'1950','Rapala VMC Corporation':'1936','Clarus Corporation':'','Sycamore Partners':'2011','Burton Snowboards':'1977'}
SRC={'Johnson Outdoors':'Johnson_Outdoors','VF Corporation':'VF_Corporation','Amer Sports':'Amer_Sports','Pure Fishing':'Pure_Fishing','Rapala VMC Corporation':'Rapala','Clarus Corporation':'Black_Diamond_Equipment','Burton Snowboards':'Burton_Snowboards','Sycamore Partners':'Pure_Fishing'}
DESC={'Johnson Outdoors':'Owns Scubapro, Jetboil, Old Town, Eureka!, Humminbird and Minn Kota; company sales US$592 million in 2025.','VF Corporation':'Denver group; owns The North Face, JanSport, Eastpak, Napapijri, Timberland, Smartwool and Icebreaker; revenue US$10.45 billion in 2024.','Amer Sports':'Helsinki-based group; owns Salomon, Atomic, Arc\'teryx and Peak Performance; revenue US$5.18 billion in 2024.','Pure Fishing':'Tackle group owned by Sycamore Partners since 2019; brands include Abu Garcia, Berkley, Penn, Shakespeare and Ugly Stik.','Rapala VMC Corporation':'Finnish tackle group listed on Nasdaq Helsinki; owns VMC, Storm, Sufix, Luhr Jensen and 13 Fishing.','Clarus Corporation':'Owner of Black Diamond since May 2010 and of Pieps.','Burton Snowboards':'Burlington, Vermont snowboard maker founded 1977 by Jake Burton Carpenter; owned by Donna Carpenter.','Sycamore Partners':'New York private equity firm that bought Pure Fishing in 2019.'}
nb=[]
for n,(c,t) in OB.items():
    if n in brands: continue
    nb.append({'n':n,'c':c,'f':FD.get(n,''),'seg':'Specialist','d':DESC[n],'lines':[],'eras':[],'sig':[],'sc':[],'rel':[],'s':WP+SRC[n],'kf':'','own':n,'tier':t})
bu={}
for k,(o,t,c,y) in OWN.items():
    nm={'Penn':'Penn Fishing','Eureka':'Eureka!','Old Town':'Old Town'}.get(k,k)
    if nm in brands:
        bu[nm]={'own':o,'tier':t,'c':c or None}
        bu[nm]={a:b for a,b in bu[nm].items() if b}
part={'replaces':[d['n'] for d in old],'depts':out,'brands':nb,'brand_updates':bu,'renames':{},'moves':[]}
json.dump(part,open(R+'rebuild/out/E2_parts/OUTDOOR.json.tmp','w'),ensure_ascii=False)
import os; os.replace(R+'rebuild/out/E2_parts/OUTDOOR.json.tmp',R+'rebuild/out/E2_parts/OUTDOOR.json')
print(stats,len(dropped),dropped[:20])
json.dump(dropped,open(R+'rebuild/work/V4_E2_OUTDOOR/dropped.json','w'))
