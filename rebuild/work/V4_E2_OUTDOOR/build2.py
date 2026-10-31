import re,json,collections,os
src=open('/home/user/Possession-Taxonomy/rebuild/work/V4_E2_OUTDOOR/build.py').read()
head=src[:src.index('def conv_kind')]
tail=src[src.index('MS={'):]
exec(head)
LINE={'Spinning rod','Casting rod','Fly rod','Sea and surf rod','Carp rod','Spinning reel','Spincast reel','Baitcasting reel','Multiplier reel','Centrepin reel','Fly reel','Hard lure','Soft plastic lure','Spoon and spinner','Artificial fly',
 'Tent','Bell tent','Camping hammock','Sleeping mat','Sleeping bag','Backpacking quilt','Camping stove','Storm kettle','Metal detector',
 'Climbing harness','Climbing shoe','Climbing rope','Carabiner','Quickdraw','Belay device','Camming device','Climbing nut','Tricam','Piton','Ice axe','Ice tool','Crampon','Ice screw',
 'Wetsuit','Competition swimsuit','Swim fins','Regulator','BCD','Dive computer','Surfboard','Kitesurf kite','Traction kite','Wing-foil wing','Windsurf sail','Windsurf board','Hydrofoil','Kiteboard','Stand-up paddleboard','Paraglider','Hang glider','Free-flight harness','Skydiving parachute','Automatic activation device','Wingsuit',
 'Alpine ski','Ski binding','Ski boot','Cross-country ski','Touring ski','Snowboard','Snowboard binding','Snowboard boot','Splitboard','Ice skate','Skateboard','Longboard','Skateboard deck','Skateboard trucks','Skateboard wheels','Skateboard bearings','Roller skate','Inline skate','Kick scooter','Unicycle','Cycling computer'}
U=dict(
 shim='https://www.tacklewarehouse.com/Shimano_Spinning_Reels/catpage-RLSSHIMANO.html',
 bass='https://www.bassmaster.com/guide-shimano-reel-lineup',
 daiwa='https://www.tacklewarehouse.com/catpage-DAIWARELLS.html',
 penn='https://www.tacklewarehouse.com/catpage-PENNREELS.html',
 spin='https://www.tacklewarehouse.com/catpage-SPINREEL.html',
 abu='https://www.abugarcia.com/collections/reels',
 msr='https://www.rei.com/b/msr/c/tents',
 nemo='https://www.mec.ca/en/products/brands/nemo/camping-and-hiking/tents-and-shelters',
 ba='https://www.campmor.com/collections/big-agnes/main-category_tents',
 hil='https://www.nordicoutdoor.co.uk/pages/hilleberg-tent-guide',
 bdbel='https://blackdiamondequipment.com/collections/belay-and-rappel',
 bdcar='https://blackdiamondequipment.com/collections/carabiners',
 bdclimb='https://blackdiamondequipment.com/collections/climb-equipment',
 wcf='https://www.wildcountry.com/en-us/climbing-friends',
 wcg='https://www.wildcountry.com/en-us/rock-climbing-gear',
 petcar='https://www.petzl.com/us/en/sport/products/carabiners-quickdraws-slings',
 petbel='https://www.petzl.com/US/en/Operators/Belay-Devices-And-Descenders',
 burton='https://www.burton.com/nz/en/c/explore-mens-snowboards',
 lib='https://www.lib-tech.com/snowboard/mens-snowboards',
 atomic='https://www.atomic.com/en-us/shop/men/men-alpine-skiing/ski.html',
 salomon='https://www.salomon.com/en-us/c/men/winter-equipment/skiing/skis',
 ross='https://www.rossignol.com/us-en/sports/alpine-ski/skis',
 k2='https://k2snow.com/en-us/c/ski/',
 dhv='https://www.dhv.de/en/type-inspection/classification/')
# canon lines: kind -> [(line, maker, url, fact)]
C=collections.defaultdict(list)
def add(kind,maker,url,names,fact=None):
    for n in names:
        C[kind].append((n,maker,url,(fact or {}).get(n,'')))
add('Spinning reel','Shimano',U['shim'],['Stella','Sustain','Twin Power','Twin Power XD','Vanquish','Stradic','Vanford','Nexave','Catana','Miravel','Exsence','Nasci','Sahara','Sedona','Sienna','Spheros','Spirex','Ultegra'],{'Stella':"Shimano's flagship spinning reel, packed with its newest technologies and premium materials.",'Stradic':'A well-known name offered in aluminium-frame and lightweight carbon-graphite versions.','Sustain':'Restyled reel with an aluminium frame that balances strength and accuracy.'})
add('Spinning reel','Daiwa',U['daiwa'],['Exist','Certate','Saltiga','BG','Legalis','Fuego','Kage','Exceler','Laguna','Revros','Freams','Luvias','Strikeforce-B','Crossfire','Eliminator','Saltist','Regal','IPRIMI','Ballistic','Prorex'])
add('Spinning reel','Penn Fishing',U['penn'],['Battle','Clash','Pursuit','Slammer','Fierce'])
add('Spinning reel','Abu Garcia',U['abu'],['Revo','Max','Zenon'])
add('Baitcasting reel','Shimano',U['bass'],['Core','Chronarch','Curado','Citica','Caenen'],{'Curado':'A long-running Shimano favourite with updated internals and an aluminium body.','Core':'Very light low-profile reel with a magnesium frame.'})
add('Baitcasting reel','Daiwa',U['daiwa'],['Tatula','Steez','Ryoga','Zillion','Aird','Coastal','Millionaire'])
add('Baitcasting reel','Abu Garcia',U['abu'],['Revo','Ambassadeur','Max','Beast','Zenon'])
add('Multiplier reel','Penn Fishing',U['penn'],['Fathom','Squall'])
for nm,mk,u,names,fx in [
 ('Tent','MSR',U['msr'],['Hubba Hubba','Elixir','FreeLite','Access','Remote','Front Range'],{}),
 ('Tent','Nemo Equipment',U['nemo'],['Kunai','Dagger OSMO','Dragonfly OSMO','Aurora','Aurora Highrise','Hornet OSMO'],{}),
 ('Tent','Big Agnes',U['ba'],['Tiger Wall','Fly Creek','Salt Creek','Crag Lake','Blacktail','Big House','Sarvis VST','String Ridge VST','Pitchpine VST'],{'Tiger Wall':'Three-season, semi-freestanding, side-entry ultralight tent.','Fly Creek':'Three-season, semi-freestanding, front-entry ultralight tent.','Crag Lake':'Three-season, freestanding, sustainably produced superlight tent.','Blacktail':'Three-season, freestanding backpacking tent.','Big House':'Three-season, freestanding car-camping tent.','String Ridge VST':'Three-season, trekking-pole-supported premium ultralight tent.','Pitchpine VST':'Three-season, non-freestanding premium ultralight tent.'}),
 ('Tent','Hilleberg',U['hil'],['Keron','Nammatj','Tarra','Soulo','Nallo','Kaitum','Allak','Anjan','Niak','Enan','Altai','Atlas','Stalon','Akto','Staika','Unna'],{'Keron':'Black Label tunnel tent.','Nammatj':'Black Label tunnel tent.','Tarra':'Black Label tent.','Nallo':'Red Label tunnel tent.','Kaitum':'Red Label tunnel tent.','Allak':'Red Label tent.','Anjan':'Yellow Label tent.','Niak':'Yellow Label tent.','Enan':'Yellow Label tent.','Altai':'Blue Label tent.','Atlas':'Blue Label tent.','Stalon':'Blue Label tent.'}),
 ('Belay device','Black Diamond',U['bdbel'],['ATC-Pilot','ATC-Guide','ATC-XP','Big Air XP','Super 8'],{}),
 ('Belay device','Petzl',U['petbel'],['Neox','GriGri+','Reverso','Verso'],{}),
 ('Carabiner','Black Diamond',U['bdcar'],['MiniWire','RockLock','VaporLock','LiteWire','HotForge','Gridlock','Oval Keylock','LiteForge','PearLock','HotWire'],{}),
 ('Carabiner','Petzl',U['petcar'],['William','Am\'D','Sm\'D','OK','Attache','Rocha','Freino Z','Omni','Vertigo Wire-Lock','Ange S','Ange L'],{}),
 ('Carabiner','Wild Country',U['wcg'],['Helium 3.0','Astro','Xenon'],{}),
 ('Quickdraw','Wild Country',U['wcg'],['Session','Helium 3.0 quickdraw'],{}),
 ('Quickdraw','Black Diamond',U['bdclimb'],['HotForge Hybrid','MiniWire Alpine'],{}),
 ('Camming device','Black Diamond',U['bdclimb'],['Camalot C4','Camalot Z4','Ultralight Camalot'],{}),
 ('Camming device','Wild Country',U['wcf'],['Zero Friend','Offset Zero Friend'],{}),
 ('Climbing nut','Black Diamond',U['bdclimb'],['Stopper'],{}),
 ('Climbing harness','Black Diamond',U['bdclimb'],['Momentum','Solution','Zone'],{}),
 ('Snowboard','Burton',U['burton'],['Custom','Process','Ripcord','Blossom','Mystery Process','Cartographer','Counterbalance','Rewind','Family Tree','Spellbinder','Cultivator','3D Fish','Instigator','Good Company'],{}),
 ('Snowboard','Lib Tech',U['lib'],['Legitimizer','Off Ramp','Skate Banana','Skunk Ape','dPr','Dynamo','Cold Brew','Terrain Wrecker','Lib Rig','Jamie Lynn','Ejack Knife','T.Rice Pro','T.Rice Orca II','Golden Orca','Apex Orca','Mayhem','Doughboy'],{}),
 ('Splitboard','Lib Tech',U['lib'],['Escalator Split','Orca II Techno Split'],{}),
 ('Alpine ski','Atomic',U['atomic'],['Redster','Maverick','Bent','Volant'],{}),
 ('Touring ski','Atomic',U['atomic'],['Backland'],{}),
 ('Alpine ski','Salomon',U['salomon'],['QST','S/Lab','Stance','Equipe','Addikt','départ'],{}),
 ('Touring ski','Salomon',U['salomon'],['MTN'],{}),
 ('Alpine ski','Rossignol',U['ross'],['Experience','Blackops','Sender','Arcade','Forza','Hero','Nova','Savage','Soul'],{}),
 ('Touring ski','Rossignol',U['ross'],['Escaper'],{}),
 ('Alpine ski','K2',U['k2'],['Mindbender','Reckoner'],{}),
 ('Touring ski','K2',U['k2'],['Wayback'],{}),
]: add(nm,mk,u,names,fx)
# fly canon
OR='https://www.orvis.com/fly-fishing/flies/'
FLY=[
 ('Dry fly',OR+'dry-flies',["Rosenbauer's Rosenhopper","Rosenbauer's Sneaky Spinner","Rosenbauer's Eck Caddis",'Galactic Ant','Grumpy Frumpy','Palomino Caddis','Project Cicada','Elk Wing Caddis','NBK Caddis','Adams Parachute','Quick Sight Foam Ant','RS2','Sparkle Dun','Light Cahill',"Gibson's Dragonfly",'PMX',"Spotts' Western Green Drake",'Indicator Beetle','Chernobyl Ant','Foam Park Hopper',"Jenkins' Damsel",'WD-40','CDC Emerging Caddis','Bank Beetle','Irresistible','Blue Dun','Sulphur Parachute','Light Hendrickson','Holo Humpy','Klinkhammer','Chubby','Spotlight Caddis Emerger',"Schroeder's Parachute Hopper",'Travis Para Ant',"Birchell's Hatching Midge",'CDC Mayfly Emerger',"Griffith's Gnat","Rosenbauer's General T","Baile's Panther Creek Hopper",'White Wulff','Black Gnat','Hog Caller Hopper','Pale Morning Dun Thorax','Yellow Humpy','The Doculator',"Miller's Clueless Caddis","Olsen's Front End Loader Caddis",'Blue Winged Olive Parachute']),
 ('Wet fly',OR+'wet-flies',["Tunghead Soft Hackle Hare's Ear",'Sparkle Soft Hackle',"Rosenbauer's Soft Wire Hackle","Articulated Daddy's Money",'Shuggy Bugger','Green Weenie','Hornberg','Bead Head Flymph','March Brown Wet',"Enrico's Permit Crab"]),
 ('Nymph','https://www.orvis.co.uk/collections/nymph-flies',["Hare's Ear Nymph",'Mayfly Nymph','March Brown Nymph','Diawl Bach','Pheasant Tail Flashback']),
 ('Nymph','https://howtoflyfish.orvis.com/video-lessons/toms-short-tips/1703-the-12-must-have-trout-flies',['Frenchie Jig Nymph','Zebra Midge','Prince Nymph','Rubber Legs Nymph','White Zonker','Black Beadhead Woolly Bugger']),
 ('Streamer',OR+'streamer-flies',['Half N Half','Mousey McMouseface','Jiggy Fat Minnow','GD Spark Plug',"Whalley's Best Bet","Whalley's Tinker Peanut Bunker","Kraft's Kreelex",'Intruder',"Senyo's AI Intruder",'Meg A Egg Sucking Leech',"Burk's Hot Flash Minnow",'Freshwater Clouser',"Schultzy's S3 Sculpin","Kraft's Clawdad",'TeQueely Streamer','Black Ghost',"Mike's Meal Ticket","Enrico's Spawning Shrimp","Mikkleson's Epoxy Bait Fish",'Softy Minnow',"Wildwood's Wild Wobbler",'Black Nose Dace','Mini Dragon Tail',"George Daniels Sculpin Snack",'Gulley Ultra Craw','Conehead Bunny Muddler',"Whalley's Prison Bride",'Come at Me Cray',"Wildwood's 3M Minnow","Kraft's Baitfish",'Con-Man','Snake Bait','Skittal Mantis Shrimp','Weighted Minnow Changer']),
 ('Bass and panfish fly',OR+'bass-panfish-flies',['Swimming Frog','Boss Bug Popper','Boss Bug Slider','Turpin Messy Minnow','Bass Popper','Peeper Popper','Mouse Rat','Sneaky Pete Popper','Bully Bluegill Spider',"Cermele's Master Splinter","Kraft's Crittermite","Wilson's Brim Reaper","Cheech's Sculpin Slider",'Bluegill Bug','Bead Head Flash Zonker',"Mangum's Dragon Tail",'Hot Head Damsel',"Wilson's Bass Bully",'Swinging D','Dry Rind Frog Popper','Big-Eyed Panfish Bug','Hair Bass Bug',"Jan's Carp Tickler",'Dancing Frog',"May's Clearwater Crayfish"]),
]
def norm(s): return re.sub(r"[^a-z0-9]","",re.sub(r"^the ","",s.lower()).replace("'s",""))
removed=collections.defaultdict(list)
cnt=collections.defaultdict(dict)
def firstword(n): 
    w=re.split(r'[ \-/]',n.strip())[0]; return re.sub(r'\d+$','',w) or w
def conv_kind(k,dname):
    k=json.loads(json.dumps(k)); x=k.get('x',[]); kn=k['n']; ms=k.pop('m',[]) or []; k.pop('r',None)
    kfall=k.get('s') or ''
    if kn not in LINE:
        keep=[e for e in x if re.search(r'\bfirst\b',e.get('d','')) ]
        for e in x:
            if e not in keep: removed[kn].append(e['n'])
        for n,mk in ms: removed[kn].append(f'{n} ({mk})')
        for e in keep:
            e['role']='origin'; e.setdefault('g',e.get('mk') or 'Unattributed')
        if keep: k['x']=keep; k['nl']=f'One entry is the first product of its kind, named by a fetched page; this kind is otherwise a commodity and keeps no further entries.'; k['sel']='Origin entry only, per the icon rule for commodity kinds (BRIEF 2026-10-31): the first product of its kind as a fetched page states. Covers %d origin entries; named models of the kind were removed.'%len(keep); k['xg']='by maker'
        else: k.pop('x',None)
        return k
    # --- line kind
    for e in x:
        e.setdefault('g',e.get('mk') or 'Unattributed')
        if e['n'] in SKIP_ROLE: e['role']=SKIP_ROLE[e['n']]
        o=ownkeys(e.get('mk',''))
        if o: e['own'],e['tier'],e['cty']=o[0],o[1],o[2]; (o[3] and e.__setitem__('own_y',o[3]))
    ents={e['n'].lower():e for e in x}
    def find_line(mk,name):
        for ln,m,u,f in C.get(kn,[]):
            if m==mk and re.match(r'^'+re.escape(ln.lower())+r'(\b|\s|$)',name.lower()): return ln
        return None
    pages=[]
    # canon lines
    canon_added=0
    for ln,m,u,f in C.get(kn,[]):
        full=f'{m} {ln}'
        hit=[e for e in x if norm(ln) in norm(e['n']) and (m.lower().split()[0] in e['n'].lower() or e.get('mk')==m)]
        if hit:
            if not hit[0].get('d') and f: hit[0]['d']=f
            continue
        e={'n':full,'a':'','mk':m,'y':'','s':u,'v':[],'g':m}
        if f: e['d']=f
        o=ownkeys(m)
        if o: e['own'],e['tier'],e['cty']=o[0],o[1],o[2]; (o[3] and e.__setitem__('own_y',o[3]))
        x.append(e); ents[full.lower()]=e; canon_added+=1; pages.append(u)
    # fly canon + other NEW
    if kn=='Artificial fly':
        have={norm(e['n']) for e in x}
        for g,u,names in FLY:
            for n in names:
                if norm(n) in have: continue
                x.append({'n':n,'a':'','mk':'','y':'','s':u,'v':[],'g':g}); have.add(norm(n)); canon_added+=1; pages.append(u)
    # Wikipedia NEW
    wnew=0
    for e in NEW.get(kn,[]):
        if norm(e['n']) in {norm(z['n']) for z in x}: continue
        x.append(e); wnew+=1
    if kn=='Paraglider':
        for cl,d in [('A','Paragliders with good passive safety and forgiving flying characteristics.'),('B','Paraglider with good passive safety and forgiving flight characteristics.'),('C','Paragliders with moderate passive safety and with potentially dynamic reactions to turbulence and pilot errors.'),('D','Paragliders with demanding flying characteristics and potentially violent reactions to turbulence and pilot errors.')]:
            x.append({'n':f'LTF class {cl}','a':'','d':d,'mk':'DHV','y':'','s':U['dhv'],'v':[],'g':'DHV certification class'}); canon_added+=1
        pages.append(U['dhv'])
    # models
    makers=collections.OrderedDict(); strong=collections.defaultdict(list)
    for name,mk in ms:
        rs=idx.get(name.lower(),[]); src='';y=''
        for r in rs:
            u=first_url(r['sources'])
            if u: src=u; y=r['first_year'] if (r['first_year'] or '').isdigit() else ''; break
        full=name if (not mk or mk.lower().split()[0] in name.lower()) else f'{mk} {name}'
        if norm(full) in {norm(e['n']) for e in x} or norm(name) in {norm(e['n']) for e in x}: continue
        ln=find_line(mk,name)
        if ln:
            parent=[e for e in x if e.get('mk')==mk and norm(ln) in norm(e['n'])]
            if parent:
                parent[0]['v'].append({'n':name,'mk':mk,'y':y}); continue
        if src: strong[(mk,firstword(name))].append((name,mk,y,src))
        else: makers.setdefault(mk,[]).append((name,mk,y))
    def own(e):
        o=ownkeys(e['mk'])
        if o: e['own'],e['tier'],e['cty']=o[0],o[1],o[2]; (o[3] and e.__setitem__('own_y',o[3]))
    nstrong=0
    for (mk,fw),lst in strong.items():
        if len(lst)>=2:
            n=f'{mk} {fw}' if mk else fw
            e={'n':n,'a':'','mk':mk,'y':'','s':lst[0][3],'v':[{'n':a,'mk':mk,'y':y} for a,_,y,_ in lst],'g':mk or 'Unattributed'}
        else:
            a,_,y,s=lst[0]; n=a if (not mk or mk.lower().split()[0] in a.lower()) else f'{mk} {a}'
            e={'n':n,'a':'','mk':mk,'y':y,'s':s,'v':[],'g':mk or 'Unattributed'}
        own(e); x.append(e); nstrong+=1
    for mk,lst in makers.items():
        # weak: fold into maker entry; attach to existing maker-line entry if one exists
        e={'n':f'{mk} {kl(kn)} models' if mk else f'Unattributed {kl(kn)} models','a':'','mk':mk,'y':'','s':kfall or (x[0]['s'] if x else ''),'v':[{'n':a,'mk':mk,'y':y} for a,_,y in lst],'g':mk or 'Unattributed'}
        if not e['s']: removed[kn].extend(f'{a} ({mk}) [no source]' for a,_,y in lst); continue
        own(e); x.append(e)
    for e in x:
        e['v']=[v for v in e.get('v',[])]
        if not e['v']: e['v']=[]
    # dedupe by name
    seen=set(); xx=[]
    for e in x:
        if e['n'].lower() in seen: continue
        seen.add(e['n'].lower()); xx.append(e)
    x=xx
    if x:
        k['x']=x
        if not k.get('s'): k['s']=x[0]['s']
        k['nl']=f'One entry is a named {kl(kn)} line (a range sold under one name) or, where only models are known, a maker\'s group of models; sizes, capacities and years are versions.'
        if kn=='Artificial fly': k['nl']='One entry is a named fly pattern tied to a recipe; size and colour variants are versions.'
        pg=sorted({re.sub(r'^https?://(www\.)?','',u).split('/')[0] for u in pages})
        n=len(x); weak=sum(1 for e in x if e['s']==kfall and e['n'].endswith(' models'))
        sel=f'Lines read from fetched maker or retailer range pages ({", ".join(pg) if pg else "none for this kind"}), plus Wikipedia class and shape articles where noted, plus lines grouped from models of the earlier retail harvest (each group carries its page; models of a maker with no per-model page sit under one maker entry on the kind\'s retail category page).'
        sel+=f' Covers {canon_added+wnew} lines or classes read from range pages and {n-canon_added-wnew} entries from earlier pages ({weak} of them maker groups); no whole-space reference lists this kind, so this is not a complete list.'
        if kn=='Artificial fly': sel+=' The Orvis dry-flies and streamer-flies pages were cut off by the fetch (about 105 and 80 results listed); the nymph page is page 1 of 2.'
        k['sel']=sel; k['xg']='by section: '+', '.join(dict.fromkeys(e['g'] for e in x))[:90] if kn in ('Artificial fly','Paraglider','Surfboard','Kitesurf kite','Kiteboard','Skateboard deck') else 'by maker'
        x.sort(key=lambda e:(e['g'],e.get('y') or '9999',e['n']))
    else: k.pop('x',None)
    return k
exec(tail)
json.dump(removed,open('/home/user/Possession-Taxonomy/rebuild/work/V4_E2_OUTDOOR/removed.json','w'))
print({k:len(v) for k,v in removed.items()}, sum(len(v) for v in removed.values()))
