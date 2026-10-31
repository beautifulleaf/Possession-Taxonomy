import json,copy,os
SRC='../../out/H3.json'
d=json.load(open('bak/H3.json'))
K={}
for dep in d['depts']:
    for s in dep['s']:
        for k in s['k']: K[k['n']]=k
WIKI='https://en.wikipedia.org/wiki/Sex_toy'
IMP='https://en.wikipedia.org/wiki/Impact_play'
BON='https://en.wikipedia.org/wiki/Bondage_(BDSM)'
VIB='https://en.wikipedia.org/wiki/Vibrator_(sex_toy)'
ren={}
def kind(n,dd,tt,a=None,**kw):
    k=K.pop(n) if n in K else {'n':n,'a':'','m':[]}
    k['d']=dd; k.pop('t',None)
    k['tt']=tt
    if a is not None:k['a']=a
    k.update(kw)
    for f in ('m','r','x'):
        if f in k and not k[f]: k.pop(f)
    if not k.get('a'):k.pop('a',None)
    return k
def new(n,dd,tt,s,a=''):
    k={'n':n,'d':dd,'tt':tt,'s':s}
    if a:k['a']=a
    return k
def shelf(n,t,ax,ks):
    s={'n':n,'t':t,'k':ks}
    if ax:s['ax']=ax
    return s
def dep(old,t,ax,shelves,note=None):
    o=[x for x in d['depts'] if x['n']==old][0]
    r={k:v for k,v in o.items() if k not in('s',)}
    r['t']=t;r['ax']=ax;r['s']=shelves
    if note:r['note']=note
    return r
D=[]
# ---- Vibrators
wand=kind('Wand vibrator','Long-handled vibrator with a large rounded head, for the outside of the body, such as the Magic Wand; one sold as a general massager is in Personal Care & Beauty.',
 [['Power source',['Mains (corded)','Rechargeable']],['Size',['Full size','Compact (mini, micro)']],['Head material',['Silicone','Vinyl']]],
 see=[['H1','Handheld massager','sold as a general massager']])
ext=K.pop('External vibrator')
mods={m[0]:m for m in ext['m']}
def pick(*n): return [mods[x] for x in n]
bullet=kind('Bullet vibrator','Small, slim vibrator for the outside of the body, shaped like a bullet or lipstick, such as a Pocket Rocket.',
 [['Power source',['Battery','Rechargeable']],['Water resistance',['Splashproof','Waterproof']],['Control',['Button','Remote','App']]],
 a='pocket rocket · mini vibrator',m=pick('Zee Bullet Vibrator','Classic Bullet Vibe','Riot Bullet Vibrator','Pocket Rocket'),s=ext['s'])
palm=kind('Palm vibrator','Flat, rounded or mouse-shaped vibrator held in the palm or pressed to the body, such as a Vibe Personal Massager.',
 [['Shape',['Mouse-shaped','Flat pebble','Flicking tip']],['Power source',['Rechargeable','Battery']],['Material',['Silicone']]],
 a='mouse vibrator · flicking vibrator',m=pick('Vibe Personal Massager','Plump Palm Vibrator','Klitty','Fluttering Arouser'),s=ext['s'])
finger=new('Finger vibrator','Small vibrator worn on the fingertip or hand, so that the hand itself touches.',
 [['Fit',['Fingertip sleeve','Ring or band','Glove-style']],['Power source',['Battery','Rechargeable']]],VIB,a='fingertip vibrator')
worn=new('Wearable vibrator','Vibrator worn in underwear or on the body, with remote or phone control; a worn insertable egg is on the next shelf.',
 [['Control',['Remote','App','Remote and app']],['Fit',['Panty clip','Waistband or strap','Adhesive']]],VIB,a='panty vibrator')
cush=new('Vibrating cushion','Cushion or pad with a motor inside, on which the user sits or lies.',
 [['Shape',['Cushion','Pad']],['Power source',['Mains','Rechargeable']]],VIB)
s1=shelf('External vibrators','Vibrators used on the outside of the body, from the long-handled wand to the small bullet and the worn type; an insertable vibrator is on the next shelf.',
 'kinds by size and how the hand holds them: wand, bullet, palm, finger, worn, cushion',[wand,bullet,palm,finger,worn,cush])
ins=kind('Insertable vibrator','Vibrator made to be inserted, with a curved or straight shaft; a curved tip reaches the front vaginal wall.',
 [['Shaft shape',['G-spot curve','Straight classic','Realistic']],['Material',['Silicone','Glass']],['Power source',['Rechargeable','Battery']]],a='G-spot vibrator · realistic vibrator · vibrating dildo',
 see=[['H3','Dildo','same shape without a motor']])
egg=kind('Egg vibrator','Small egg-shaped vibrator for insertion or wear, joined to a control by a wire or controlled by remote or app.',
 [['Control link',['Wired','Wireless remote','App']]],see=[['H3','Wearable vibrator','worn on the outside']])
anal=kind('Anal vibrator','Vibrating anal insertable with a flared base that is not a prostate massager.',
 [['Shape',['Flared base','Plug-shaped']],['Control link',['Wired','Wireless']]],see=[['H3','Butt plug','same shape without a motor']])
s2=shelf('Insertable vibrators','Vibrators made for insertion, differing in shaft shape and in where they sit: vaginal, small egg or anal.',
 'kinds by shape and fit: shaft, egg, flared base',[ins,egg,anal])
rab=kind('Rabbit vibrator','Insertable vibrator with an external arm that stimulates the clitoris at the same time.',
 [['Shaft action',['Rotating shaft','Thrusting','Fixed']],['Control',['Buttons','App']]],see=[['H3','Couples vibrator','also works two areas at once']])
cou=kind('Couples vibrator','Vibrator made to be worn or used by two partners at once during intercourse.',
 [['Shape',['Wearable C-shape']],['Control',['Remote','App']]],see=[['H3','Rabbit vibrator','dual action for one user']])
s3=shelf('Dual-action & couples vibrators','Vibrators that work two areas at once, either for one user (rabbit type) or worn during sex by two partners.',
 None,[rab,cou])
D.append(dep('Vibrators','Products whose main action is a motor that vibrates, used on the outside, inside or both; a motor that moves the toy or a sleeve is a machine, an air-pulse stimulator is in the next department.',
 'Where on the body is it used: outside, inside, or both areas at once?',[s1,s2,s3],
 note='Powered vibration; where on the body it is used splits the department, material is a detail.'))
# ---- Air-pulse
ap=kind('Air-pulse stimulator','Stimulator that works with pulses of air or suction over the clitoris, without contact pressure, such as a Womanizer.',
 [['Form',['Handheld','Wearable']],['Power source',['Rechargeable']],['Water resistance',['Splashproof','Waterproof']]],a='clitoral air-pulse stimulator · suction stimulator')
sp=kind('Suction pump','Hand or powered vacuum pump with a cup placed over the vulva or nipples.',
 [['Power source',['Hand pump','Powered pump']],['Cup size',['Small','Medium','Large']]],see=[['H3','Penis pump','same principle, other body part']])
pp=kind('Penis pump','Cylinder placed over the penis with a hand or powered vacuum pump; one whose maker states a medical purpose is in Health, Medical & Mobility.',
 [['Power source',['Hand pump','Electric pump','Bulb pump']],['Fill',['Air','Water (hydro)']]],see=[['H2','Vacuum erection device','sold for a medical purpose']])
D.append(dep('Air-pulse, suction & pumps','Products that act through air pressure or a vacuum rather than vibration: air-pulse stimulators and vacuum pumps; a medical vacuum device is in Health, Medical & Mobility.',
 'What acts on the skin: pulses of air, or a held vacuum in a cup or cylinder?',
 [shelf('Air-pulse stimulators','Stimulators that move pressure waves over the skin without touching it, such as a Womanizer.',None,[ap]),
  shelf('Vacuum pumps','Pumps that draw skin into a cup or cylinder, by hand or motor.',None,[sp,pp])],note='Stimulation by air pressure or vacuum rather than vibration.'))
# ---- Machines
sm=kind('Sex machine','Motor on a frame or base that drives an attachment back and forth.',
 [['Frame',['Table-top','Floor frame','Foldable']],['Control',['Wired','App']],['Stroke',['Fixed length','Adjustable length']]],a='thrusting machine')
sa=kind('Saddle machine','Saddle the user sits astride, with a vibrating or rotating insert or pad.',
 [['Insert action',['Rotating shaft','Vibrating ridge']],['Control',['Wired remote']]],a='riding saddle machine')
ma=kind('Machine attachment','Dildo, adapter or masturbator made to fit a sex machine\'s connector.',
 [['Attachment type',['Dildo','Adapter','Masturbator holder','Saddle attachment']]])
tv=kind('Thrusting vibrator','Hand-held insertable vibrator whose motor moves the shaft in and out; one that takes attachments through a standard mains-style connector is a sex machine.',
 [['Power source',['Rechargeable']],['Control',['Buttons','Remote']]],see=[['H3','Sex machine','frame and attachments']])
am=kind('Automatic masturbator','Masturbator whose motor moves, strokes or sucks the sleeve; it may come with a stand or mount.',
 [['Motion',['Stroking sleeve','Vibrating','Sucking']],['Control',['Buttons','App-synced']]],see=[['H3','Handheld masturbator','moved by the hand, no motor']])
D.append(dep('Thrusting & stroking machines','Products where a motor moves a shaft or sleeve: frame and saddle machines, hand-held thrusting toys and automatic masturbators; a toy that only vibrates is in Vibrators.',
 'What carries the motor: a frame or saddle, the user\'s hand, or a sleeve?',
 [shelf('Frame & saddle machines','Machines with a base, frame or saddle that holds the motor, and the attachments that fit them.','kinds by build: frame, saddle, attachment',[sa,sm,ma][::-1][::-1] if False else [sm,sa,ma]),
  shelf('Hand-held & automatic toys','Toys with a built-in motor that thrusts or strokes without a frame, held or placed by the user.',None,[tv,am])],
 note='Toys whose motor moves the toy or sleeve.'))
# ---- Dildos etc
dil=kind('Dildo','Solid non-powered insertable made for penetration; a powered one is an insertable vibrator.',
 [['Material',['Silicone','Glass (borosilicate)','Stainless steel']],['Shape',['Realistic','Non-realistic']],['Base',['Suction-cup base','Flared base','Harness-compatible']]],a='crystal dildo',
 see=[['H3','Insertable vibrator','with a motor']])
dd=kind('Double-ended dildo','Dildo with an insertable end at each side, for two users or two openings.',
 [['Flexibility',['Flexible','Rigid']],['Use',['Strap-on version','Hand-held']]])
fan=kind('Fantasy-form toy','Toy moulded as a fantasy creature or creature-inspired shape, sold by makers who also take customer designs for limited runs.',
 [['Shape theme',['Dragon','Horse','Tentacle']],['Production',['Standard','Custom or limited run']]])
har=kind('Strap-on harness','Harness that holds a dildo against the wearer\'s body, usually by an O-ring or a plug fitting.',
 [['Strap layout',['Two-strap','Three-strap (thigh straps)']],['Fitting',['O-ring fitting','Vac-u-lock fitting']],['Material',['Leather','Fabric','Latex or rubber']]],a='strap-on · harness')
plug=kind('Butt plug','Tapered insertable with a narrow neck and a flared base, made to be held in the anus.',
 [['Material',['Silicone','Glass','Steel']],['Base',['Plain flared','Jewelled']],['Power',['Non-powered','Vibrating']]],a='anal plug')
pro=kind('Prostate massager','Curved anal insertable shaped to press on the prostate, often with a flared base.',
 [['Power',['Non-powered','Vibrating']],['Fit',['Hands-free','Hand-held']],['Material',['Silicone','Steel','Glass']]],see=[['H3','Butt plug','plain plug shape']])
beads=kind('Anal beads','Three or more beads in a row on a cord or flexible stem, with a retrieval loop.',
 [['Strand',['Cord','Flexible stem']],['Bead sizing',['Same size','Graduated']],['Material',['Silicone']]])
keg=kind('Kegel balls','Weighted balls held in the vagina, with or without a retrieval cord; some are sold for pelvic-floor training.',
 [['Weight',['Single weight','Graduated set']],['Build',['Metal-covered','Silicone-coated','Duotone (ball in ball)']],['Link',['Single','Linked on a cord']],['Power',['Non-powered','Vibrating']]],
 see=[['H2','Pelvic-floor trainer','sold for pelvic-floor exercise']])
dil2=kind('Dilator','Graduated insertable sold as a sex toy; one whose maker states a medical purpose is in Health, Medical & Mobility.',
 [['Sizing',['Graduated set','Single size']],['Material',['Silicone']]],see=[['H2','Vaginal dilator','sold for a medical purpose']])
snd=kind('Urethral sound','Smooth rod made to be inserted into the urethra for sexual stimulation.',
 [['Material',['Stainless steel']],['Sizing',['Single rod','Graduated set']]])
D.append(dep('Dildos, plugs & insertables','Non-powered insertables and the harness that holds one: dildos, anal plugs, weights and graduated sizes; a vibrating insertable is in Vibrators, a latex garment is in Clothing.',
 'What is it made for: general penetration, anal wear, or a weighted or graduated size?',
 [shelf('Dildos & harnesses','Solid shaped insertables for penetration, and the harness that holds one on the body.','kinds from the plain dildo to forms and harnesses',[dil,dd,fan,har]),
  shelf('Anal toys','Insertables made for anal wear, all with a stop at the end: plugs, beads and prostate massagers; a vibrating one is in Vibrators.','kinds by shape: plug, curved, beads',[plug,pro,beads]),
  shelf('Weighted & graduated insertables','Insertables whose point is weight or stepped size: vaginal weights, dilator sets and urethral rods.','kinds by use: weight, graduated vagina set, urethral',[keg,dil2,snd])],
 note='Non-powered insertables; material (silicone, glass, steel) is a type.'))
# ---- Masturbators
hm=kind('Handheld masturbator','Reusable sleeve with an inner channel, held in the hand, such as a Fleshlight.',
 [['Opening',['Splits open for washing','Sealed']],['Case',['Sleeve in a case','Sleeve only']],['Inner texture',['Smooth','Textured channel']]],a='stroker · pocket pussy',
 see=[['H3','Automatic masturbator','motor-driven']])
dm=kind('Disposable masturbator','Single-use sleeve in a closed shell, made to be used once and thrown away, such as a Tenga Cup.',
 [['Shell',['Cup','Egg']]])
sm_=kind('Penis sleeve','Open sleeve worn over the penis to add length, girth or texture.',
 [['Material',['Silicone','TPE']],['Surface',['Smooth','Textured']]])
pr=kind('Penis ring','Ring worn at the base of the penis, or the penis and testicles, to keep an erection. Some vibrate.',
 [['Material',['Silicone','Steel']],['Fit',['Fixed','Adjustable']],['Ring count',['Single','Triple ring']],['Add-on',['Scrotum strap','Vibrating']]],
 see=[['H2','Erection ring','sold for a medical purpose']])
D.append(dep('Masturbators, sleeves & rings','Non-powered products made for the penis: masturbators held in the hand, and rings and sleeves worn on it; a motor-driven masturbator is in the machines department.',
 'Is it stroked by the hand, or worn on the penis?',
 [shelf('Masturbators','Sleeves in which the penis is stroked by the hand, reusable or single use.',None,[hm,dm]),
  shelf('Rings & sleeves worn on the penis','Items worn on the penis during use: rings at the base and sleeves over the shaft.',None,[pr,sm_])],
 note='Non-powered products for the penis.'))
# ---- Dolls
sd=kind('Solid body doll','Life-size body replica of solid silicone or TPE on an internal frame, such as a RealDoll.',
 [['Material',['Platinum-cure silicone','TPE']],['Inner structure',['Foam core','Articulated skeleton']]])
inf=kind('Inflatable doll','Inflatable life-size body replica made for sexual use, usually with the surface of vinyl.',
 [['Material',['Vinyl','Latex']]],see=[['H3','Solid body doll','solid body']])
st=kind('Stationary masturbator','Large, heavy masturbator moulded as a torso, lower body or breast form.',
 [['Body part',['Torso','Hips','Breast-form']]],see=[['H3','Handheld masturbator','held in the hand']])
D.append(dep('Dolls & body-form toys','Body-shaped products for sexual use, from the life-size doll to the heavy torso form; a plain sleeve is in the masturbators department, a mannequin or art doll is not in scope here.',
 'Is the body a full figure, or only a part?',
 [shelf('Full-size dolls','Life-size body replicas, solid or inflatable, such as RealDoll.','kinds by build: solid or inflatable',[sd,inf]),
  shelf('Part-body forms','Heavy forms shaped as a torso, hips or breast, usually kept in one place.',None,[st])]))
# ---- Bondage
cuffs=kind('Bondage cuffs','Pair of wrist or ankle cuffs, joined or with fixing points, made to restrain.',
 [['Material',['Leather','Neoprene','Metal','Silicone']],['Mounting',['Free pair','Door cuffs']]])
bed=kind('Bed restraint set','Straps that run under or around a mattress with cuffs at the corners.',
 [['Fixing',['Under the mattress','Around the bedframe']],['Material',['Fabric','Leather']]])
rope=kind('Bondage rope & tape','Soft rope, or tape that sticks only to itself, sold for binding a part of the body.',
 [['Material',['Cotton rope','Jute rope','Hemp rope','Nylon rope']],['Form',['Rope','Self-adhesive tape']]])
col=kind('Restraint collar & leash','Neck collar made with fixing points to restrain, with or without a leash.',
 [['Parts',['Collar','Leash','Collar and leash set']],['Material',['Leather','Fabric']]])
spr=new('Spreader bar','Rigid bar with cuffs at each end that holds the wrists or ankles apart.',
 [['Material',['Steel','Wood','Leather-covered']],['Length',['Fixed','Adjustable']]],BON)
body=kind('Body restraint','Harness or sleeve that restrains the body or binds the arms, such as an armbinder.',
 [['Form',['Restraint harness','Armbinder']]],a='restraint harness · armbinder')
bl=kind('Blindfold','Blindfold that covers only the eyes; a hood or mask is in Clothing.',
 [['Material',['Satin','Leather']],['Build',['Flat','Padded']]],see=[['A1','Gloves & hand coverings','hoods and masks are clothing']] if False else None)
if not bl.get('see'): bl.pop('see',None)
gag=kind('Gag','Object held in the mouth by a strap to stop speech.',
 [['Type',['Ball gag','Bit gag','Ring gag']]])
ch=kind('Chastity device','Locking cage or belt that prevents touching of the genitals.',
 [['Form',['Cage','Belt']],['Material',['Steel','Resin','Silicone']]])
sw=kind('Sex swing','Swing or sling hung from a frame, door or ceiling that supports a person.',
 [['Mounting',['Door','Ceiling','Frame-mounted']]])
rf=kind('Restraint furniture','Bench, cross or frame made to restrain a person; a cushion that only positions is a positioning wedge.',
 [['Form',['Bench','Cross','Frame']]])
pw=kind('Positioning wedge','Angled foam wedge or pillow that supports the body in different positions.',
 [['Form',['Wedge','Ramp','Wedge and ramp set','Bondage pillow']],['Cover',['Standard','Waterproof']]])
D.append(dep('Bondage & restraints','Products that bind the body, limit sight, speech or touch, or carry the body in position; a latex garment or hood is in Clothing, a striking implement is in the next department.',
 'Does it bind the body, limit a sense or access, or carry the body?',
 [shelf('Restraints','Items that hold wrists, ankles, neck or the whole body: cuffs, bed straps, rope, collars, spreader bars and harnesses.','kinds by what is held: wrists and ankles, bed, any limb, neck, apart, torso',[cuffs,bed,rope,col,spr,body]),
  shelf('Blindfolds, gags & chastity','Items that limit sight, speech or touch.','kinds by what is limited: sight, speech, touch',[bl,gag,ch]),
  shelf('Sex furniture & swings','Swings, benches and wedges that carry the body.','kinds by how they carry: hung, fixed, laid',[sw,rf,pw])]))
# ---- Impact
pad=kind('Paddle','Flat, rigid striking implement with a handle, for impact play.',[['Material',['Leather','Wood','Silicone']]])
flo=kind('Flogger','Handle with many falls of leather or other material, for impact play.',[['Material',['Leather','Suede','Rubber']]])
crop=kind('Riding crop','Stiff single-tail striking implement with a flap at the end.',[['Tip',['Slapper','Loop','Tassel']]],a='crop',s=K['Crop & whip']['s'])
whip=new('Whip','Flexible single-tail striking implement, from short whips to the long bullwhip.',[['Length',['Short','Long (bullwhip)']],['Material',['Leather','Nylon']]],IMP)
cane=new('Cane','Thin straight rod used for striking, typically rattan.',[['Material',['Rattan','Acrylic','Wood']]],IMP)
ren['Crop & whip']='Riding crop'
fe=kind('Feather tickler','Feather or soft-tipped wand for light sensation play.',[['Material',['Natural feather','Faux feather']]])
nc=kind('Nipple clamp','Adjustable clamp applied to the nipples, often joined by a chain.',[['Clamp action',['Tweezer','Clover']],['Add-on',['Vibrating']]])
ek=kind('Electro-stimulation kit','Control unit with pads or insertable electrodes made for sexual electrical stimulation.',
 [['Electrode',['Pads','Insertable electrode','Ring electrode']],['Unit',['Made-for-play unit']]],a='e-stim',see=[['H2','TENS/EMS unit','medical muscle stimulation']])
vw=kind('Violet wand','Hand-held high-voltage, low-current device that sends a spark through attachments.',[['Circuit',['Tesla coil (mechanical)','Solid-state']]])
D.append(dep('Impact & sensation play','Implements applied to the skin for sensation: striking, tickling, pinching or electrical stimulation; items that restrain are in Bondage & restraints.',
 'How does it touch the skin: a strike, a light touch or pinch, or an electric current?',
 [shelf('Striking implements','Tools that strike the skin, from broad paddles to single-tail whips and canes.','kinds by shape: flat, many-tail, single-tail, rod',[pad,flo,crop,whip,cane]),
  shelf('Light touch & pressure','Items that tickle or pinch rather than strike.',None,[fe,nc]),
  shelf('Electro-stimulation','Devices that apply electrical current or a spark.',None,[ek,vw])]))
# ---- Care
oil=kind('Intimate oil','Oil or gel made and labelled for intimate use to heighten sensation; a lubricant is in Personal Care & Beauty.',
 [['Format',['Oil','Gel']]],see=[['H1','Personal lubricant','a lubricant']])
cl=kind('Toy cleaner','Product made to clean sex toys.',[['Form',['Spray','Foam','Wipes']],['Method',['Cleaner','UV sanitiser (disinfects but does not clean)']]])
mc=kind('Masturbator care accessory','Replacement liner, warmer, drying stick or other accessory made for a masturbator.',[['Accessory',['Drying stick','Warmer','Renewing powder','Replacement liner']]])
sc=kind('Toy storage case','Lockable box or bag for keeping adult toys clean, dry and out of sight.',[['Form',['Lockable ventilated box','Satin or fabric pouch','UV sanitising pouch']]])
D.append(dep('Care & storage','Products used with the toys rather than being one: intimate oils, cleaners, care accessories and storage; a lubricant is in Personal Care & Beauty.',
 'When is it used: during play, after play, or between uses?',
 [shelf('Care & storage','Oil for use with toys, cleaners for after use and cases for between uses.','kinds by when used: during, after, between',[oil,cl,mc,sc])],
 note='Cleaning, drying, storage and accessories for intimate products.'))
assert not K or True
left=[n for n in K if n not in ('External vibrator','Crop & whip')]
print('LEFT',left)
ren['External vibrator']='Bullet vibrator'
d['depts']=D
d['ax']='What does the product do: vibrate, act by air or vacuum, move by motor, serve as a passive insertable, work on the penis, take the form of a body, restrain, give sensation, or care for the toys?'
d['key']=[
'1. Does it bind or hold the body, cover the eyes or mouth, or carry the body in position (cuffs, rope, swing, wedge)? → Bondage & restraints',
'2. Is it applied to the skin to strike, tickle, pinch or give a current (paddle, flogger, clamp, e-stim)? → Impact & sensation play',
'3. Is it a body-shaped form, life-size or a torso or breast form? → Dolls & body-form toys',
'4. Is it a cleaner, case, oil or other product used with the toys? → Care & storage',
'5. Does a motor thrust a shaft or stroke a sleeve (frame, saddle, automatic masturbator)? → Thrusting & stroking machines',
'6. Does it work by pulses of air or a vacuum (air-pulse stimulator, pump)? → Air-pulse, suction & pumps',
'7. Is it a sleeve, masturbator or ring made for the penis, with no motor? → Masturbators, sleeves & rings',
'8. Is its main action a vibrating motor? → Vibrators',
'9. Is it a non-powered insertable, weight, graduated rod or harness? → Dildos, plugs & insertables',
'<i>Precedence: a motor that moves the toy is a machine (step 5) before a vibrator (step 8); a ring, sleeve or plug that only vibrates stays with its shape; latex wear is in Clothing; a product sold for a medical purpose is in Health, Medical & Mobility.</i>']
json.dump(d,open('H3.new.json','w'),indent=1,ensure_ascii=False)
json.dump(ren,open('renames.new.json','w'),indent=1)
