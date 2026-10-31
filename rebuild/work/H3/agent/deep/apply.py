import json,os,sys
RV='https://reviewed.com/health/best-right-now/best-vibrators-tested'
PS='https://www.popsci.com/gear/best-sex-toys/'
VI='https://www.vice.com/en/via/best-sex-toys-for-women/'
MN='https://www.mumsnet.com/swearsby/best-wand-vibrators'
PC='https://www.popsci.com/gear/best-sex-toys-for-couples/'
LD='https://lastingthedistance.com/automatic-strokers/'
DG='https://www.dapperandgroomed.com/blog/best-male-masturbators-tested'
AS='https://www.autostraddle.com/best-butt-plugs-queer-sex/'
BU='https://www.bustle.com/p/13-best-sex-toys-for-anal-stimulation-17857502'
LB='https://reviewed.com/health/content/lelo-beads-review-best-ben-wa-balls'
CR='https://reviewed.com/health/best-right-now/best-cock-rings'
CD='https://global.chinadaily.com.cn/a/202503/25/WS67e20462a3101d4e4dc2a9e9.html'
AU='https://www.autostraddle.com/?p=559194'
WL='https://en.wikipedia.org/wiki/Liberator_Shapes'
PW='https://www.purewow.com/wellness/best-sex-toy-cleaners'
SR='https://storerotica.com/avn-hall-of-fame-inducts-jiro-takashima-inventor-and-founder-of-aneros'
def B(n,kf,d,s,c=''): return {"n":n,"c":c,"f":"","seg":"Specialist","kf":kf,"d":d,"s":s}
J={
'00_00':dict(
 drop={'Wand vibrator':['Magic Wand Plus','Magic Wand Micro']},
 add={'Wand vibrator':[['Smart Wand 2','LELO'],['Moregasm+ Wand','Ann Summers'],['Doxy Die Cast','Doxy'],['Ollie Wand Vibrator','Unbound'],['Extra Powerful Multispeed Mains Powered Magic Wand','Lovehoney'],['Domi','Lovense'],['Le Wand Submersible','Le Wand'],['3-Speed Micro Magic Wand','Lovehoney']],
      'Bullet vibrator':[['Vibe Personal Massager','Maude'],['Personal Massager','plusOne']],
      'Flicking vibrator':[['Fluttering Arouser','plusOne']]},
 brands=[B('Le Wand','wands','Maker of the Le Wand Submersible, picked as best wand by Vice.',VI),
         B('Maude','body-safe basics','Maker of the Vibe Personal Massager, Reviewed best bullet vibrator.',RV),
         B('plusOne','budget toys','Maker of budget-pick vibrators in PopSci tests.',PS),
         B('Unbound','beginner toys','Maker of the Ollie wand and Squish vibrator, named in a Mumsnet and a PopSci roundup.',MN)],
 note="Deepening pass 2026-10-27: tested pages Reviewed 'best vibrators tested' (Magic Wand Rechargeable best overall; Maude Vibe best bullet), PopSci best sex toys (plusOne picks), Vice best sex toys for women (Le Wand Submersible best wand), Mumsnet Swears By best wand vibrators (LELO Smart Wand 2, Ann Summers, Doxy Die Cast, Unbound Ollie, Lovehoney x2, Lovense Domi; editorial picks, not lab tests). Wand models trimmed to 12: old Magic Wand Plus and Micro dropped to make room for sourced picks. Wirecutter, Strategist and Cosmopolitan pages could not be retrieved, so none cited."),
'00_01':dict(
 add={'Rabbit vibrator':[['Soraya Wave','LELO'],['On Repeat','Playboy Pleasure']],
      'Insertable vibrator':[['Poco','MysteryVibe']],
      'Couples vibrator':[['Chorus','We-Vibe'],['Sync O','We-Vibe'],['Sync Go','We-Vibe']],
      'Egg vibrator':[['Lush 4','Lovense']],
      'Anal vibrator':[['Ditto+','We-Vibe'],['Ditto','We-Vibe'],['Rimming Plug 2','b-Vibe']]},
 note="Deepening pass: Reviewed tested roundup (LELO Soraya Wave best rabbit; Dame Arc best G-spot; We-Vibe Ditto+ best anal; We-Vibe Sync O best hands-free), PopSci (Chorus, Sync O, Sync Go, MysteryVibe Poco), Vice (Playboy Pleasure On Repeat best rabbit; Lovense Lush 4 best G-spot egg), Bustle is logged under the dildo shelf (Rimming Plug 2). Glans vibrator still has no sourced model."),
'01_00':dict(
 add={'Air-pulse stimulator':[['Premium 2','Womanizer'],['Next','Womanizer'],['Lem','Hello Nancy']]},
 note="Deepening pass: Womanizer Premium 2 (Reviewed best suction vibrator), Womanizer Next (Vice best clit sucker; PopSci best for women), Hello Nancy Lem (Vice beginner pick). Womanizer OG was already listed (PopSci best overall). Satisfyer Pro 2 Gen 3 is PopSci/Vice pick; kept as the existing Satisfyer Pro 2 entry. Arcwave Ion: a T3 review could not be fetched (page returned navigation only), so not added."),
'02_00':dict(
 add={'Automatic masturbator':[['Keon','Kiiroo'],['Max 2','Lovense'],['Onyx+','Kiiroo'],['The Handy','Handy'],['Storm','BestVibe']]},
 brands=[B('Kiiroo','app-linked strokers','Maker of the Keon automatic stroker, top pick of Lasting The Distance.',LD)],
 note="Deepening pass: Lasting The Distance (own 5-point scores, not lab tests: Keon top pick, Lovense Max 2 best value, Kiiroo Onyx+), Dapper and Groomed (single-author multi-week test: Lovense Solace Pro best overall, Kiiroo Keon, BestVibe Storm), PopSci (The Handy, best for phalluses). Arcwave Ion not added: its only review page fetched (T3) returned no article text."),
'03_00':dict(
 add={'Butt plug':[['The Bootie','Fun Factory'],['Snug Plug','b-Vibe'],['Pure Plug','nJoy'],['Pfun Plug','nJoy'],['Devata Glass Butt Plug','Prisms']],
      'Double-ended dildo':[['Sharevibe','Fun Factory'],['Fun Wand','nJoy'],['Rusé Double Dildo','Blush Novelties']],
      'Dildo':[['BI Stronic Fusion','Fun Factory']],
      'Prostate massager':[['Hugo','LELO'],['Vector','We-Vibe']],
      'Anal beads':[['Cinco Anal Beads','b-Vibe']],
      'Kegel balls':[['Beads','LELO']]},
 brands=[B('nJoy','steel toys','Maker of the Pure Plug and Fun Wand, named in Autostraddle and Bustle roundups.',AS),
         B('Aneros','prostate massagers','Founded around inventor Jiro Takashima; started with a device for prostate-related issues.',SR)],
 note="Deepening pass: Autostraddle butt-plug guide (Fun Factory Bootie, b-Vibe Snug Plug, nJoy Pure Plug and Fun Wand, We-Vibe Vector, Prisms), Bustle anal-toy guide (LELO Hugo, nJoy Pfun Plug, Fun Factory Sharevibe and BI Stronic Fusion, b-Vibe Cinco, Blush Rusé; retailer-linked editorial lists, not tests), Reviewed LELO Beads review (Mini, Classic, Plus; Classic tested over several years). Men's Health UK prostate roundup could not be fetched, so Njoy Pure Wand and Aneros models are not added; Aneros brand entry rests on the AVN Hall of Fame article (country and exact year not stated). Icicles: no page found. Reviewed lists We-Vibe Ditto+ as best anal vibrator (see shelf 00_01)."),
'04_00':dict(
 add={'Handheld masturbator':[['Manta','Fun Factory']],
      'Penis ring':[['Diamo','Lovense'],['Tor 2','LELO'],['SVR','TENGA'],['Pivot','We-Vibe'],['The Big O','Screaming O'],['Verge','We-Vibe'],['Band','Maude'],['Nōs','Fun Factory'],['Tandem Couples Vibrating Ring','Trojan']]},
 brands=[B('Screaming O','vibrating rings','Maker of The Big O, named best for beginners in a Reviewed ring test.',CR)],
 note="Deepening pass: Reviewed cock-ring test (two months; vibration, noise, battery, water and heat measured: Lovense Diamo best overall, LELO Tor 2 best value, TENGA SVR best basic, We-Vibe Pivot best hybrid, Screaming O The Big O best for beginners; Verge, Maude Band, Fun Factory Nos, Trojan Tandem listed without award; Screaming O Ohare rated avoid, not added), PopSci couples roundup (Fun Factory Manta best for men). Oxballs not on any fetched page (only a reader comment on another page), so not added. LELO Tor 2 is the Tor successor."),
'04_01':dict(
 add={}, ranges={'Solid body doll':[['MetaBox','WM Doll']]},
 brands=[B('WM Doll','TPE dolls','Zhongshan, Guangdong maker founded in 2010; began with TPE body models and made TPE dolls from 2012.',CD,'China')],
 note="Deepening pass: WM Doll added from a China Daily article (Zhongshan, 2010, founder Liu Jiangxia, TPE dolls from 2012, MetaBox AI-enhanced series). Brand founding year entered 2010 from that page. Sino Doll: no page found."),
'05_00':dict(
 add={'Bed restraint set':[['Under the Bed Restraint System','Sportsheets']]},
 note="Deepening pass: Autostraddle review of the Sportsheets Under the Bed Restraint System (four adjustable cuffs and four straps). No independent test of other restraint makers was found."),
'05_02':dict(
 add={},
 brands=[B('Liberator','sex furniture','Liberator Inc., also called OneUp Innovations; Atlanta firm known for the Wedge and Ramp positioning pillows.',WL,'United States')],
 note="Deepening pass: Liberator brand added from Wikipedia (Liberator Shapes). The Wedge and Ramp are positioning pillows and stay in Soft Furnishings, so no models added here. AOL swing roundup (Bondage Boutique Deluxe Fetish, Whipsmart, Screamer, Sportsheets Door Jam Kit) names no makers except Sportsheets, so only the existing Sportsheets kit is confirmed; the page was fetched but not cited for new models."),
'06_00':dict(add={},note="Deepening pass: no new sourced items found; no independent test for impact or sensation toys was retrieved."),
'06_01':dict(add={},note="Deepening pass: ElectraStim only surfaced on retailer listings (one 404, others unfetched), so not added; no test source found."),
'07_00':dict(
 add={'Toy cleaner':[['Shibari Toy Cleaner','Shibari'],['IntiMD Multi-Purpose Hygienic Cleaner','IntiMD'],['Hand + Vibe Cleaner','Dame'],['Home Play UV Cleaner','Uvee'],['The Clean Kit','Maude'],['Cake Toy Cleaner','Cake'],['Green Toy Cleaner','Intimate Earth']]},
 note="Deepening pass: PureWow roundup of 11 cleaners (Shibari best overall, IntiMD best spray, Dame best dual purpose, Uvee best high-tech, Maude best kit, Cake best foaming, Intimate Earth best natural); editorial list, not a lab test, makers inferred from product names except LELO. PopSci also names the Hello Cake cleaner. Toy cleaner now at the 12-model cap. Marie Claire UK page returned only a title."),
}
for job,c in J.items():
    p=f'work/H3/shelves/{job}.json'; d=json.load(open(p))
    ks={k['n']:k for k in d['kinds']}
    for kn,names in c.get('drop',{}).items():
        ks[kn]['m']=[m for m in ks[kn]['m'] if m[0] not in names]
    for kn,ms in c.get('add',{}).items():
        have={tuple(m) for m in ks[kn].get('m',[])}
        ks[kn].setdefault('m',[]).extend(m for m in ms if tuple(m) not in have)
    for kn,ms in c.get('ranges',{}).items():
        ks[kn].setdefault('r',[]).extend(ms)
    have={b['n'] for b in d['brands']}
    d['brands']+= [b for b in c.get('brands',[]) if b['n'] not in have]
    d['notes']=d['notes']+' | '+c['note']
    for b in d['brands']:
        if b['n']=='WM Doll': b['f']='2010'
    open(p+'.tmp','w').write(json.dumps(d,ensure_ascii=False,indent=1)); os.replace(p+'.tmp',p)
