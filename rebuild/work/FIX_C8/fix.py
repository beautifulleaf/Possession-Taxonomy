import json,copy
P='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(P+'C8.json')); mv=json.load(open(P+'C8_moves.json'))
def find(n):
    for dp in d['depts']:
        for s in dp['s']:
            for i,k in enumerate(s['k']):
                if k['n']==n: return dp,s,i,k
    raise KeyError(n)
def pop(n):
    dp,s,i,k=find(n); s['k'].pop(i); return k
def dedupe(l):
    o=[]
    for x in l:
        if x not in o:o.append(x)
    return o
def merge(target,names,newname=None,extra_t=(),drop_t=(),d_=None,alias=None):
    """merge kinds `names` into kind `target` (kept in place)"""
    dp,s,i,k=find(target)
    others=[pop(n) for n in names]
    t=list(k.get('t',[]))
    for o in others:
        t+= o.get('t',[]) or [o['n'].lower()]
        for key in ('m','r'):
            if o.get(key): k[key]=dedupe(k.get(key,[])+o[key])
        if o.get('x'): k['x']=k.get('x',[])+o['x']
    t+=list(extra_t)
    k['t']=[x for x in dedupe(t) if x not in drop_t]
    if newname: k['n']=newname
    if d_: k['d']=d_
    if alias: k['a']=alias
    return k
def A(n,a,dsc,mk,y,s,v=None,dt=None):
    x={"n":n,"a":a,"d":dsc,"mk":mk,"y":y,"s":s,"v":v or []}
    if dt: x["dt"]=dt
    return x
# C8-1 paint colours
_,_,_,k=find('Wall and ceiling paint')
FB='https://www.farrow-ball.com/paint/elephants-breath'
k['x']=[
 A("Elephant's Breath No. 229","Elephant's Breath","Mid-tone warm grey named by John Fowler and sold by Farrow & Ball.","Farrow & Ball","",FB,
   [{"n":"Estate Emulsion","mk":"Farrow & Ball","y":"","d":"wall finish"},{"n":"Modern Emulsion","mk":"Farrow & Ball","y":"","d":"wall finish"},{"n":"Dead Flat","mk":"Farrow & Ball","y":"","d":"ultra-matt finish"}],
   "colour number · finish · sheen"),
 A("Hague Blue No. 30","Hague Blue","Strong deep blue with green undertones, named from Dutch woodwork colours.","Farrow & Ball","","https://www.farrow-ball.com/ca/paint/hague-blue/estate-eggshell",[],"colour number · finish · sheen"),
 A("Railings No. 31","Railings","Soft black with blue undertones, named after ironwork.","Farrow & Ball","","https://www.farrow-ball.com/paint/railings",[],"colour number · finish · sheen"),
 A("Obsidian Green 216","Obsidian Green","Off-black with deep green undertones, light reflectance value about six; sold by Little Greene.","Little Greene","","https://rabart.co.uk/pages/little-greene-obsidian-green-216",
   [{"n":"Absolute Matt Emulsion","mk":"Little Greene","y":"","d":"wall finish"},{"n":"Intelligent Matt Emulsion","mk":"Little Greene","y":"","d":"wall finish"}],"colour number · finish · sheen"),
 A("Hale Navy HC-154","Hale Navy","Deep navy from Benjamin Moore's Historical Colors collection, light reflectance value 8.36.","Benjamin Moore","","https://www.benjaminmoore.com/paint-colors/color/hc-154/hale-navy",[],"colour number · finish · sheen"),
]
k['dt']="named colour and number · finish · sheen"
# C8-2 ironmongery
_,_,_,k=find('Latch')
LS='https://www.suffolklatchcompany.com/blogs/news/different-types-of-latches'
k['x']=[
 A("Suffolk latch","","Thumb-operated lever latch for ledged and braced timber doors and gates, with no back plate on the original form.","","16th century (Suffolk)","https://en.wikipedia.org/wiki/Latch",
   [{"n":"Penny-end","mk":"","y":"","d":"rounded end detail"},{"n":"Gothic (arrow end)","mk":"","y":"","d":"pointed ends"},{"n":"T-bar","mk":"","y":"","d":"T-shaped handle on the other face"}],"penny or arrow end · finish · size"),
 A("Norfolk latch","","Thumb latch whose handle is fitted to a back plate separately from the thumbpiece.","","c. 1800–1820 (Norfolk)","https://en.wikipedia.org/wiki/Latch",[],"finish · size"),
 A("Tuscan latch","","Works like a Suffolk latch but with a pointed arrow-end design.","","",LS,[],"finish · size"),
 A("Cottage latch","","Latch lifted by turning a pair of ring turns instead of a thumb lever.","","",LS,[],"handed · cast iron · finish"),
]
_,_,_,k=find('Door knocker')
k['x']=[
 A("Sanctuary knocker","Sanctuary ring","Heavy ring on a church or cathedral door, meant to be grasped; the Durham Cathedral example is a 12th-century bronze.","","12th century (Durham)","https://en.wikipedia.org/wiki/Sanctuary_knocker",[{"n":"Durham Cathedral north door replica","mk":"","y":"1980","d":"replica ring on the door; original in the cathedral museum"}]),
 A("Lion-head knocker","","Knocker with a ring held in a cast lion's head; the form appears on doors such as the Raczyński Library, Poland.","","","https://en.wikipedia.org/wiki/Door_knocker",[],"cast iron or brass · size"),
 A("Hamsa knocker","","Hand-shaped knocker linked to the hand of Fatima, found in Morocco.","","","https://en.wikipedia.org/wiki/Door_knocker",[],"hand-shaped · brass or iron"),
]
_,_,_,k=find('Door hinge')
H='https://en.wikipedia.org/wiki/Hinge'
k['x']=[
 A("Butt hinge","mortise hinge","Hinge set into a door or door frame; the standard door hinge.","","",H,[],"size · material · finish · ball-bearing or plain"),
 A("H hinge","","Barrel hinge shaped like a capital H, used on flush-mounted doors.","","",H,[],"size · finish"),
 A("HL hinge","","H hinge with an extra arm on one side, common on passage and room doors in the 17th to 19th centuries.","","17th–19th century",H,[],"size · finish"),
 A("Parliament hinge","butterfly hinge","Hinge that holds the leaf flush with the surface when opened 180 degrees.","","",H,[],"size · finish"),
 A("Piano hinge","continuous hinge","Continuous barrel hinge running the full length of a door, panel or box.","","",H,[],"length · material"),
]
for h in k['t'][:]:
    if h in ('butt','H','parliament','butterfly'): k['t'].remove(h)
# spray paint
_,_,_,k=find('Spray paint')
MU='https://www.montana-cans.com/Products/'
k['m']=[m for m in k['m'] if m[0] not in('Montana BLACK','Montana GOLD')]
k['x']=[
 A("Montana GOLD","","Low-pressure, quick-drying artist acrylic spray paint with a wide colour range, for fine art and murals.","Montana Cans","",MU,[],"colour · 400 ml can · low pressure"),
 A("Montana BLACK","","High-pressure Nitro-Combi graffiti spray paint for fast work on large surfaces.","Montana Cans","",MU,[],"colour · 400 ml can · high pressure"),
]
# C8-3 merges
merge('Wood screw',['Decking screw','Drywall screw','Masonry screw','Coach screw','Self-tapping screw','Machine screw'],newname='Screw',
      extra_t=['wood','decking','drywall','masonry','coach','self-tapping','machine'],drop_t=['decking screw','drywall screw','masonry screw','coach screw','self-tapping screw','machine screw'],
      d_="Threaded fastener driven or turned into timber, plasterboard, masonry or metal.",alias="wood screw · fixing screw")
merge('Bolt',['Nut','Washer','Rivet'],newname='Bolt, nut, washer and rivet',
      extra_t=['rivet'],drop_t=['nut','washer'],d_="Threaded or riveted fasteners that join parts with a nut, washer or peen.",alias="nut · washer · rivet")
k=find('Bolt, nut, washer and rivet')[3]; k['t']=dedupe(k['t']+['nut','washer'])
merge('Wall plug',['Cavity fixing','Frame fixing','Steel anchor','Chemical anchor'],newname='Wall fixing',
      extra_t=['cavity fixing','frame fixing','steel anchor','chemical anchor'],drop_t=[],d_="Plug, anchor or bolt that holds a screw or load in masonry, plasterboard or concrete.",alias="wall plug · anchor · cavity fixing")
k=find('Wall fixing')[3]; k['t']=[x for x in k['t'] if x not in ('cavity fixing','frame fixing','steel anchor','chemical anchor') ]+['cavity fixing','frame fixing','steel anchor','chemical anchor']; k['t']=dedupe(k['t'])
# electrical
merge('Cable',['Flex','Conduit and trunking'],newname='Cable',extra_t=['flex'],d_="Insulated electrical cable or flex, with conduit and trunking to carry it.",alias="flex · conduit · trunking")
merge('Junction box',['Cable clip','Cable tie','Mains plug','Fuse'],newname='Electrical accessory',extra_t=['junction box','cable clip','cable tie','mains plug','fuse'],
      d_="Small fitting that joins, fixes, protects or plugs in electrical cable.",alias="junction box · cable clip · plug · fuse")
# move accessories shelf: put Electrical accessory into Cable shelf (it already is) fine
merge('Extension lead',['Plug adaptor'],newname='Extension lead and adaptor',extra_t=['plug adaptor'],d_="Mains lead with several sockets, or an adaptor that changes the plug or socket type.",alias="trailing socket · plug adaptor")
# C8-5 roofing
_,_,_,rt=find('Roof tile')
hm=pop('Handmade clay roof tile'); rc=pop('Reclaimed roof slate and tile')
slate=[x for x in rc['x'] if x['n']=='Welsh slate'][0]
plain=copy.deepcopy([x for x in hm['x'] if x['n']=='Plain tile'][0])
for x in rc['x']:
    if x['n']=='Plain clay tile': plain['v']=x['v']; plain['dt']=x['dt']
pan=copy.deepcopy([x for x in hm['x'] if x['n']=='Pantile'][0])
for x in rc['x']:
    if x['n']=='Pantile': pan['v']=x['v']
mars=[x for x in rc['x'] if x['n']=='Marseilles tile'][0]
mis=[x for x in hm['x'] if x['n']=='Mission tile'][0]; imb=[x for x in hm['x'] if x['n']=='Imbrex and tegula'][0]
rt['n']='Roof tile and slate'; rt['a']='slate · roof tile · pantile'
rt['d']='Clay, concrete or slate unit laid in overlapping courses as a roof covering, new, handmade or reclaimed.'
rt['t']=['clay plain tile','concrete interlocking','pantile','natural slate','fibre-cement slate','handmade','reclaimed','ridge and hip tile']
rt['x']=[slate,plain,pan,mars,mis,imb]
# stone
_,_,_,np_=find('Natural stone paving'); rf=pop('Reclaimed flagstone')
np_['t']=dedupe([x for x in np_['t'] if x!='York stone']+['reclaimed','kerb stone','slate flag'])
np_['x'][0]['dt']=np_['x'][0].get('dt','')+' · new or reclaimed'
np_['a']+=' · reclaimed flags'
# C8-6
ss=pop('Safety sign'); mv['out'].append({"to":"B8","dept":"Safety & signage","kind":ss})
dt_=pop('Duct tape'); find('Parcel tape')[1]['k'].insert(find('Parcel tape')[2]+1,dt_)
pk=pop('Packer'); find('Dowel')[1]['k'].insert(0,pk)
json.dump(d,open(P+'C8.json.tmp','w'),indent=1,ensure_ascii=False); json.dump(mv,open(P+'C8_moves.json.tmp','w'),indent=1,ensure_ascii=False)
