import json, glob, os, re, shutil
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'out/B2.json'))
W='https://en.wikipedia.org/wiki/'
kinds={}; dept_of={}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']: kinds[k['n']]=k
def new(n,a,dsc,src,tg=None,tt=None):
    k={'n':n,'a':a,'d':dsc,'s':src,'x':[],'m':[],'r':[]}
    if tg: k['tg']=tg
    if tt: k['tt']=tt
    kinds[n]=k
def demote(kn,names,mk_to='tt',group=None,types=None):
    k=kinds[kn]; k['x']=[x for x in k.get('x',[]) if x['n'] not in names]

# ---- demotions of generic archetypes (types are given in tt below) ----
demote('Towel',{'Terry towel'})
demote('Tablecloth',{'Damask tablecloth','Indian block-print tablecloth'})
demote('Tea towel',{'Irish linen tea towel'})
demote('Bedspread',{'Matelassé bedspread','Candlewick bedspread','Chenille bedspread','Indian block-printed bedspread'})
demote('Hide rug',{'Cowhide rug','Sheepskin rug'})
demote('Rag rug',{'Braided rug','Proggy mat'})
demote('Hooked rug',{'Latch-hook rug','Stamped-pattern rug'})
dr=kinds['Designer rug']
dr['r']=[['Märta Måås-Fjetterström rugs','Märta Måås-Fjetterström'],['Kasthall rugs','Kasthall'],['nanimarquina rugs','nanimarquina'],['The Rug Company rugs','The Rug Company']]
dr['x']=[]
kinds['Valance']['a']='bed skirt · dust ruffle · bed ruffle'
kinds['Body pillow']=None
# ---- new kinds (each with a fetched source) ----
new('Comforter','','A filled bed cover with its fill sewn in, used without a separate cover.',W+'Bedding')
new('Coverlet','','A light decorative bed cover, smaller than a bedspread, laid over the sheets.',W+'Bedding')
new('Afghan','crocheted blanket · knitted throw','A knitted or crocheted blanket, often worked in squares or stripes.',W+'Blanket',tt=[['Technique',['Crocheted','Knitted']]])
new('Sleeved blanket','wearable blanket','A blanket with sleeves, worn over the shoulders while sitting.',W+'Blanket')
new('Baby blanket','','A small soft blanket for a cot or pram.',W+'Blanket',tg=['baby'],tt=[['Cloth',['Cotton cellular','Knitted','Fleece','Muslin']]])
new('Body pillow','long pillow','A long pillow held along the body for support in sleep, including pregnancy pillows.',W+'Pillow',tt=[['Shape',['Straight','U-shaped','C-shaped']],['Fill',['Fibre','Memory foam']]])
new('Bolster','neck roll','A long narrow cylindrical pillow, filled with down, feathers or fibre.',W+'Bedding',tt=[['Use',['Bed bolster','Sofa bolster']],['Fill',['Down or feather','Fibre']]])
new('Panel blind','sliding panel blind','A blind of wide fabric panels that slide across the window on a track.',W+'Window_blind',tt=[['Light control',['Standard','Blackout']]])
new('Pelmet and valance','window valance','A board or length of fabric across the head of a window that hides the curtain heading.',W+'Window_covering',tt=[['Make',['Fabric valance','Shaped board pelmet']]])
new('Poncho towel','hooded towel','A hooded towel worn like a poncho for changing at the beach or pool.',W+'Towel')
new('Sports towel','golf towel · gym towel','A small light towel for the gym or the golf course.',W+'Towel',tt=[['Cloth',['Microfibre','Cotton terry']]])
new('Baby towel','hooded baby towel','A hooded towel sized for drying a baby after a bath.',W+'Towel',tg=['baby'])
new('Doily','','A small decorative mat of lace or crochet laid under a dish or vase.',W+'Tablecloth',tt=[['Technique',['Lace','Crochet','Embroidered']]])
new('Table protector','table pad · moulton','A thick pad laid under a tablecloth to guard the table from heat and knocks.',W+'Tablecloth',tt=[['Material',['Felt','Foam-backed']]])

# ---- tt by hand, kind by kind ----
TT={
'Persian rug':[['Pile material',['Wool','Silk','Wool and silk']],['Weaving setting',['City or workshop','Village','Nomadic or tribal']]],
'Caucasian rug':[['Format',['Main carpet','Runner','Small rug']]],
'Anatolian rug':[['Weaving setting',['Village','Workshop','Nomadic']],['Pile material',['Wool','Silk']]],
'Turkmen rug':[['Item woven',['Main carpet','Tent bag','Door hanging','Camel trapping']]],
'Tibetan rug':[['Place made',['Tibet','Nepal or India, Tibetan style']]],
'Moroccan rug':[['Surface',['Pile','Flatweave','Rag-woven']],['Age',['Antique','Vintage','New']]],
'Aubusson & Savonnerie carpet':[['Construction',['Knotted pile','Tapestry-woven flatweave']],['Age',['Antique','Reproduction']]],
'Rya rug':[['Use',['Floor rug','Wall hanging']],['Age',['Vintage','New']]],
'European workshop rug':[['Age',['Antique','New','Reproduction']]],
'Designer rug':[['Construction',['Hand-knotted','Hand-tufted','Flatweave']],['Age',['Vintage','New']]],
'Flatweave rug':[['Weave structure',['Slit-tapestry','Interlocked tapestry','Weft-wrapped (soumak)','Supplementary weft (zili)','Strip-woven (jajim)']],['Age',['Antique','New','Reproduction']]],
'Navajo rug':[['Dye',['Vegetal','Aniline']],['Age',['Antique','Contemporary']]],
'Hooked rug':[['Material',['Yarn','Fabric strip']],['Tool',['Rug hook','Latch hook']],['Pattern',['Freehand','Stamped pattern printed on the backing']],['Supply',['Made-up rug','Kit']]],
'Felt rug':[['Method',['Felt ball','Pressed felt','Stitched felt']]],
'Rag rug':[['Method',['Woven','Braided','Hooked','Proddy or clippy']]],
'Hide rug':[['Hide',['Cowhide','Sheepskin']],['Finish',['Natural','Dyed','Printed','Patchwork']]],
'Machine-made rug':[['Construction',['Wilton','Axminster','Machine-tufted','Flatwoven']],['Pile height',['Flat','Low','Shag (high pile)']],['Care and use',['Machine-washable','Indoor/outdoor']]],
'Rug pad':[['Material',['Felt and rubber','Rubber grip','Memory foam','PVC mesh']]],
'Door mat':[['Material',['Coir','Rubber']],['Position',['Indoor','Outdoor']]],
'Bath mat':[['Material',['Cotton pile','Memory foam']],['Backing',['Non-slip','Plain']]],
'Kitchen mat':[['Shape',['Mat','Runner']],['Support',['Anti-fatigue','Plain']]],
'Chair mat':[['Floor',['For carpet','For hard floor']]],
'Sheet':[['Form',['Flat (top) sheet','Fitted (bottom) sheet','Sheet set']],['Weave',['Percale','Sateen','Flannel','Jersey knit']],['Fibre',['Cotton','Linen','Silk charmeuse','Bamboo or lyocell','Microfibre','Cotton-polyester blend']],['Fitted depth',['Standard','Deep-pocket']]],
'Pillowcase':[['Style',['Housewife (flap closure)','Oxford (flanged border)','Plain (open end)','Sham (decorative, back opening)']],['Closing',['Open end','Zip or button']],['Fibre or weave',['Silk','Percale','Sateen','Linen']]],
'Duvet cover':[['Closure',['Buttons','Poppers','Zip','Ties']],['Cloth',['Percale','Sateen','Linen','Flannel','Jersey','Waffle']],['Design',['Plain','Reversible']]],
'Valance':[['Style',['Platform valance (sheet with skirt)','Fitted valance sheet']],['Skirt',['Box-pleated','Gathered or ruffled','Tailored']]],
'Duvet':[['Fill',['Goose down','Duck down','Feather and down','Synthetic hollowfibre','Wool','Silk']],['Warmth',['4.5 tog (summer)','10.5 tog','13.5 tog (winter)','All-season 3-in-1']],['Stitching',['Box-stitched','Channel-stitched']]],
'Quilt':[['Construction',['Pieced (patchwork)','Appliqué','Wholecloth','Strippy']],['Stitching',['Hand-quilted','Machine-quilted']],['Fibre',['Cotton','Wool','Silk']],['Age',['Antique','Vintage','New']]],
'Bedspread':[['Weave or finish',['Matelassé','Candlewick','Chenille','Jacquard','Plain woven']],['Decoration',['Block-printed','Plain']],['Fit',['Fitted','Throw-over']]],
'Blanket':[['Fibre',['Wool','Cashmere','Cotton cellular','Linen','Fleece']],['Construction',['Woven','Knitted']]],
'Electric blanket':[['Form',['Underblanket (heated mattress pad)','Overblanket','Heated throw']],['Controls',['Single','Dual']],['Voltage',['Mains','Low-voltage']]],
'Swaddle':[['Form',['Muslin wrap','Receiving blanket','Winged swaddle (fastened)','Sleep sack']]],
'Kotatsu futon':[['Part',['Shitagake (under-cover)','Kotatsu-gake (top cover)','Kotatsushiki (floor mat)']]],
'Bed pillow':[['Fill',['Down','Feather','Synthetic fibre','Memory foam','Latex','Buckwheat']],['Firmness',['Soft','Medium','Firm']]],
'Travel pillow':[['Shape',['U-shaped']],['Construction',['Inflatable','Memory foam']]],
'Positioning cushion':[['Shape',['Wedge','Ramp','U or C-shaped (pregnancy)']]],
'Mattress topper':[['Fill',['Memory foam','Latex','Fibre','Down','Feather']],['Thickness',['Thick topper','Thin quilted pad']]],
'Mattress protector':[['Style',['Fitted','Encasement']],['Barrier',['Waterproof','Standard']]],
'Pillow protector':[['Barrier',['Waterproof','Anti-allergy']]],
'Scatter cushion':[['Sold as',['Cover only (removable)','Cushion with insert']]],
'Cushion pad':[['Fill',['Feather','Synthetic fibre']]],
'Chair pad':[['Fixing',['Ties','Non-slip back']]],
'Floor cushion':[['Form',['Zafu (round or crescent)','Zabuton (flat padded mat)','Pouffe-style','Pillow stack']]],
'Sofa cover':[['Fit',['Fitted (made for one sofa model)','Stretch','Throw-over']]],
'Chair cover':[['Fit',['Fitted (made for one chair model)','Stretch','Throw-over']],['Chair',['Dining chair','Event chair']]],
'Printed & embroidered furnishing textile':[['Decoration',['Printed','Resist-dyed (ikat)','Embroidered']],['Sold as',['By the metre','Ready-made hanging']]],
'Curtain':[['Heading',['Pencil pleat','Eyelet','Tab top','Pinch pleat']],['Lining',['Lined','Unlined','Blackout','Thermal']],['Sheerness',['Opaque','Sheer or voile']]],
'Shower curtain':[['Material',['Fabric','Plastic']],['Liner',['With liner','Without liner']]],
'Roller blind':[['Light control',['Standard','Blackout','Day and night']],['Operation',['Hand-operated','Motorised']]],
'Roman blind':[['Light control',['Standard','Blackout']],['Operation',['Corded','Cordless tie-up shade (hand-gathered)','Motorised']]],
'Venetian blind':[['Slat material',['Aluminium','Wood','Faux wood']],['Operation',['Corded','Motorised']]],
'Vertical blind':[['Light control',['Standard','Blackout']],['Operation',['Corded','Motorised']]],
'Pleated blind':[['Light control',['Standard','Blackout']],['Mounting',['Standard','Top-down bottom-up']]],
'Cellular shade':[['Light control',['Standard','Blackout']],['Operation',['Corded','Cordless','Motorised']]],
'Curtain pole':[['Material',['Metal','Wood']],['Fixing',['Bracket','Tension rod']],['Length',['Fixed','Extendable']]],
'Curtain track':[['Control',['Corded','Hand-drawn']],['Shape',['Straight','Bendable']],['Fixing',['Ceiling-fixed','Wall-fixed']]],
'Curtain fittings':[['Part',['Rings','Hooks','Gliders','Clips','Tiebacks','Holdbacks']]],
'Towel':[['Size',['Washcloth','Hand towel','Bath towel','Bath sheet','Foot towel']],['Cloth',['Terry','Linen or linen-blend terry (sauna)']]],
'Beach towel':[['Weave',['Terry','Velour','Flat-woven']]],
'Flat-woven towel':[['Fibre',['Cotton','Linen']],['Edge',['Fringed ends','Hemmed']]],
'Tablecloth':[['Fibre',['Linen','Cotton','Linen-cotton blend','Polyester']],['Weave or finish',['Damask or jacquard','Coated (wipe-clean)','Plain']],['Decoration',['Block-printed (Indian)','Plain']],['Shape',['Rectangular','Square','Round','Oval']]],
'Table runner':[['Fibre',['Linen','Cotton']],['Weave or print',['Jacquard','Printed']]],
'Cloth napkin':[['Fibre or weave',['Linen','Cotton','Damask']],['Size',['Dinner','Cocktail']]],
'Fabric placemat':[['Fibre',['Linen','Cotton']],['Construction',['Woven','Quilted']]],
'Tea towel':[['Fibre',['Linen','Irish linen','Cotton','Linen-cotton union']],['Weave',['Plain','Waffle']],['Print',['Printed or lettered']]],
}
for n,t in TT.items():
    k=kinds[n]; k['tt']=t; k.pop('t',None)
# body pillow was a type of bed pillow; keep it only as its own kind
for k in kinds.values():
    if k is None: continue
    assert not (k.get('t') and not k.get('tt')) , k['n']
kinds={n:k for n,k in kinds.items() if k}

# ---- see links ----
SEE={
'Hooked rug':[['C4','Needlework and yarn kit','rug-hooking kits']],
'Aubusson & Savonnerie carpet':[['F2','Tapestry','woven wall tapestry']],
'Quilt':[['F2','Art quilt','quilts made as art'],['E2','Backpacking quilt','camping quilt']],
'Blanket':[['H2','Weighted blanket','therapy weighted blanket']],
'Bed pillow':[['H2','Orthopaedic pillow','therapy pillow']],
'Positioning cushion':[['H2','Pressure-relief cushion','care cushion']],
'Mattress topper':[['B1','Mattress','the mattress below']],
'Mattress protector':[['B1','Mattress','the mattress it guards']],
'Travel pillow':[['E2','Camp pillow','camping pillow']],
'Floor cushion':[['B1','Bean bag chair','floor seat']],
'Sheet':[['E2','Sleeping bag liner','camping sheet']],
'Swaddle':[['A1','Baby sleeping bag','worn sleep bag']],
'Towel':[['G3','Heated towel rail','fixed towel warmer'],['G1','Drying towel','car-drying towel']],
'Beach towel':[['A1','Beach cover-up','worn beach wrap']],
'Roller blind':[['G3','Motorised blinds and shading','built-in motorised shading']],
'Venetian blind':[['B8','Blind cord safety device','cord safety']],
'Shower curtain':[['G3','Shower enclosure or screen','fixed screen']],
'Cloth napkin':[['B5','Napkin ring','holds the napkin']],
'Fabric placemat':[['B5','Hard placemat','hard mats']],
'Printed & embroidered furnishing textile':[['C4','Quilting and printed cotton','fabric by the metre']],
'Chair mat':[['D1','Mouse pad or desk mat','desk mat']],
'Persian rug':[['F4','Prayer rug','rugs made for prayer']],
'Tea towel':[['B5','Oven glove','other kitchen textiles']],
}
idx=set()
for f in glob.glob(R+'reader/[A-J]*.json'):
    if '/_' in f: continue
    try: o=json.load(open(f))
    except: continue
    for dp in o.get('depts',[]):
        for s in dp['s']:
            for k in s['k']: idx.add((o['c'],k['n']))
for n,l in SEE.items():
    for c,kn,_ in l: assert (c,kn) in idx,(c,kn)
    kinds[n]['see']=l

# ---- structure ----
def sh(n,t,ax,ks): return {'n':n,'t':t,'ax':ax,'k':[kinds[x] for x in ks]} if ax else {'n':n,'t':t,'k':[kinds[x] for x in ks]}
old={dp['n']:dp for dp in d['depts']}
def dept(n,t,ax,shelves):
    o=old[n]; o['t']=t; o['ax']=ax; o['s']=shelves; return o
depts=[
dept('Rugs & mats','Loose floor coverings: hand-made rugs named by weaving tradition, machine-made rugs and small mats for one spot; fitted carpet → C8, a prayer rug → F4, a wall tapestry → F2.',
 'How was it made, and is it a rug for a room or a mat for one spot?',[
 sh('Oriental knotted-pile rugs','Hand-knotted pile rugs from Iran, the Caucasus, Anatolia, Central Asia, China, Tibet and South Asia, named by region or tribe; a flat-woven kilim → Flatweave, hooked & folk rugs.','kinds by weaving region, from Iran eastwards and back through Anatolia',['Persian rug','Caucasian rug','Anatolian rug','Turkmen rug','Afghan & Baluch rug','Chinese rug','Tibetan rug','Indian & Pakistani rug']),
 sh('European & world pile rugs','Pile rugs from Morocco, French and Scandinavian courts, European workshops and named designers; an Asian knotted rug → Oriental knotted-pile rugs.','kinds by workshop tradition, from North Africa to designer studios',['Moroccan rug','Aubusson & Savonnerie carpet','Rya rug','European workshop rug','Designer rug']),
 sh('Flatweave, hooked & folk rugs','Rugs with no cut pile: woven flat, hooked, felted, made from rags or left as a hide; a knotted rug → the pile shelves.','kinds by how the surface is made: woven flat, hooked, felted, rag-strip, hide',['Flatweave rug','Navajo rug','Hooked rug','Felt rug','Rag rug','Hide rug']),
 sh('Everyday rugs','Factory-made rugs sold by size and fibre, and the pads laid under rugs; a hand-made rug → the shelves above.',None,['Machine-made rug','Rug pad']),
 sh('Mats','Small mats for one spot on the floor, such as at a door, bath, sink or desk chair; a yoga mat → E2.','kinds by where the mat lies: door, bath, kitchen, desk chair',['Door mat','Bath mat','Kitchen mat','Chair mat']),
]),
dept('Bedding','What goes on or in a bed: linen, filled covers, blankets, pillows and mattress protection; the mattress and frame → B1, a sleeping bag → E2, a therapy blanket → H2.',
 'Which layer of the bed is it: next to the sleeper, a filled cover, an unfilled cover, under the head or between sheet and mattress?',[
 sh('Bed linen','Washable fabric that dresses the bed: sheets, pillowcases, duvet covers, valances and headboard covers; a filled cover itself → Duvets, quilts & bedspreads.','kinds by the part of the bed dressed: mattress, pillow, duvet, bed base, headboard',['Sheet','Pillowcase','Duvet cover','Valance','Headboard cover']),
 sh('Duvets, quilts & bedspreads','Filled or decorative covers laid over the sleeper, from loose-filled duvets to stitched quilts and bedspreads; an unfilled blanket → Blankets & throws.','kinds from the warmest cover to the purely decorative: duvet, comforter, quilt, bedspread, coverlet',['Duvet','Comforter','Quilt','Bedspread','Coverlet']),
 sh('Blankets & throws','Covers with no fill, for a bed or sofa: woven, knitted, wearable, heated and baby blankets; a filled cover → Duvets, quilts & bedspreads.','kinds by purpose: general, hand-made, wearable, heated, baby, over a heated table',['Blanket','Afghan','Sleeved blanket','Electric blanket','Baby blanket','Swaddle','Kotatsu futon']),
 sh('Pillows','Stuffed supports for the head or body in bed: bed, body and travel pillows, bolsters and shaped cushions; a decorative cushion → Cushions & covers.','kinds by what is supported: head, whole body, neck roll, travelling head, a posture',['Bed pillow','Body pillow','Bolster','Travel pillow','Positioning cushion']),
 sh('Mattress toppers & protectors','Layers between mattress and sheet, or under a pillowcase, that change the feel or guard against spills and allergens; the mattress → B1.',None,['Mattress topper','Mattress protector','Pillow protector']),
]),
dept('Cushions & covers','Loose stuffed cushions, seat pads, furniture covers and furnishing fabric; bed pillows → Bedding, a bean bag or sofa → B1.',
 'Is it a stuffed cushion or pad, a cover that fits furniture, or cloth sold for hangings and upholstery?',[
 sh('Cushions & seat pads','Stuffed cushions for sitting or decoration: scatter cushions, plain pads, chair pads and floor cushions; a bed pillow → Pillows.','kinds by use: decoration, filling, chair seat, floor seat',['Scatter cushion','Cushion pad','Chair pad','Floor cushion']),
 sh('Covers & slipcovers','Removable fabric covers that fit a sofa or chair; a cushion cover is sold with its cushion above.',None,['Sofa cover','Chair cover']),
 sh('Furnishing fabrics','Patterned cloth for hangings, covers and upholstery, by the metre or ready-made; dress fabric → C4.',None,['Printed & embroidered furnishing textile']),
]),
dept('Curtains & blinds','Fabric and slatted coverings for windows and doors, with the poles, tracks and fittings that hang them; built-in shutters → G3, a window film → G3.',
 'Does it hang as fabric panels, close as a blind, or hold and trim the covering?',[
 sh('Curtains','Fabric panels hung from a pole or track across a window, door or shower; a blind that rolls or folds → Blinds & shades.',None,['Curtain','Shower curtain']),
 sh('Blinds & shades','Window coverings that roll, fold, tilt or slide rather than drape: roller, Roman, Venetian, vertical, panel, pleated and cellular blinds.','kinds by how the blind moves: roll, fold, tilt slats, slide, pleat, trap air',['Roller blind','Roman blind','Venetian blind','Vertical blind','Panel blind','Pleated blind','Cellular shade']),
 sh('Poles, tracks & fittings','Hardware and trim that hang or dress curtains: poles, tracks, rings and tiebacks, and the pelmet across the top.','kinds by what holds or trims the curtain: pole, track, small fittings, header',['Curtain pole','Curtain track','Curtain fittings','Pelmet and valance']),
]),
dept('Towels','Absorbent and flat-woven cloths for drying the body: bath, beach, sports and baby towels and wraps; a bathrobe → A1, a hair wrap → H1, a tea towel → Table & kitchen linen.',
 'Is it a looped terry towel for the body, or a flat-woven or wrap cloth?',[
 sh('Bath & body towels','Looped terry or velour towels for drying the body: bath, beach, poncho, sports and baby towels; a flat-woven towel → Flat-woven & wrap cloths.','kinds by use: bathroom, beach, changing, sport, baby',['Towel','Beach towel','Poncho towel','Sports towel','Baby towel']),
 sh('Flat-woven & wrap cloths','Thin cloths without terry loops: flat-woven towels such as the peshtemal, and square cloths that wrap goods.',None,['Flat-woven towel','Carry cloth']),
]),
dept('Table & kitchen linen','Cloths that dress the table or serve in the kitchen: tablecloths, runners, napkins, placemats and tea towels; hard placemats and coasters → B5.',
 'Does it dress the table or work in the kitchen?',[
 sh('Dressing the table','Fabric laid on or at the table: protector pads, cloths, runners, doilies, placemats and napkins; a hard placemat → B5.','kinds from the table surface up: protector, cloth, runner, doily, place setting, napkin',['Table protector','Tablecloth','Table runner','Doily','Fabric placemat','Cloth napkin']),
 sh('Kitchen cloth','Cloth for drying dishes and hands at the sink; an oven glove → B5.',None,['Tea towel']),
]),
]
d['depts']=depts
used={k['n'] for dp in depts for s in dp['s'] for k in s['k']}
assert used==set(kinds),(set(kinds)-used,used-set(kinds))
d['ax']='Which part of the home does the textile dress: the floor, the bed, seats, windows, the bath or the table?'
d['key']=[
'1. Does it lie loose on the floor to be walked on or stood on (rug, runner, door or bath mat)? → Rugs & mats',
'2. Does it go on or in a bed (sheet, duvet, blanket, pillow, topper)? → Bedding',
'3. Is it a loose stuffed cushion or pad, a cover that fits a sofa or chair, or cloth sold for hangings? → Cushions & covers',
'4. Does it hang at or cover a window or door (curtain, blind, pole, track)? → Curtains & blinds',
'5. Is it a cloth for drying the body (bath, beach or baby towel, wrap)? → Towels',
'6. Is it a cloth for the table or the kitchen (tablecloth, napkin, tea towel)? → Table & kitchen linen',
'<i>Precedence: a bed pillow is bedding (step 2) before a scatter cushion (step 3); a bath mat is a mat (step 1) before a towel (step 5); a shower curtain is a curtain (step 4).</i>']
out=R+'out/B2.json'
json.dump(d,open(out+'.tmp','w'),ensure_ascii=False,indent=1)
os.replace(out+'.tmp',out)
print('written',os.path.getsize(out))
