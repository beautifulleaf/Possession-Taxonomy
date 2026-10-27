import sys; sys.path.insert(0,'work/C4/agent')
from rb_lib import *
GF='https://thegraphicsfairy.com/what-is-a-sizzix-big-shot-machine/'
HA='https://heroarts.com/blogs/hero-arts-blog/1970s?page=51'
AL='https://altenew.com/pages/about-us'
DI='https://www.vaessen-creative.com/en/brands/ranger-ink/distress-ink'
TS='https://www.cassart.co.uk/tsukineko'
FI='https://www.deserres.ca/collections/fiskars'
SP='https://spellbinders.com/pages/about-us'
EM='https://artfulanalog.com/how-to-heat-emboss/'
OLD={'stamp':'https://www.dickblick.com/categories/paper/crafts/rubber-stamping/','craft':'https://www.dickblick.com/categories/paper/crafts/','mach':'https://www.dickblick.com/categories/crafts/machines/','sb':'https://www.scrapbook.com/store/'}
kinds=[
{'n':'Craft stamp','a':'rubber stamp · clear stamp · photopolymer stamp','d':'Decorative rubber, clear or wooden stamp made for paper craft.','t':['red rubber on wood','cling rubber','clear photopolymer','layering (coordinating) set','background stamp'],
 'm':[['Letters Woodblock Stamp Sets','Hero Arts'],['Paper Poetry ABC and Numbers Stamp Set','Rico Design']],'s':OLD['stamp'],
 'x':[X('Hero Arts rubber stamps','Berkeley rubber-stamp house begun in 1974 selling handmade stamps at craft fairs.','Hero Arts',HA,'1974',dt='mount (wood, cling) · set or single · image theme'),
      X('Altenew layering stamps','Clear photopolymer stamp sets whose layered images build up flowers; the company began with floral layering stamps.','Altenew',AL,'2014',dt='layer count · coordinating dies and stencils · set size')]},
{'n':'Ink pad','a':'stamp pad','d':'Ink pad made for decorative stamps.','t':['dye','pigment','watermark (embossing)','solvent (permanent)','alcohol-based','hybrid'],
 'm':[['Just For Kids Jumbo Ink Pad','Hero Arts'],['Archival Ink Pads','Ranger'],['Emboss It Ink Pad','Ranger']],'s':OLD['stamp'],
 'x':[X('Distress ink','Water-based dye ink pad designed to give paper and photos a weathered, vintage look; designed by Tim Holtz for Ranger.','Ranger',DI,v=[('Distress Ink Pads','Ranger'),('Distress Spray Stain','Ranger','spray form')],dt='colour · pad size · related Distress products'),
      X('VersaMark','Tsukineko watermark ink pad, described by a retailer as the original watermark stamp pad and used under embossing powder.','Tsukineko',TS,dt='clear or tinted · pad size'),
      X('VersaFine Clair','Tsukineko quick-drying pigment ink for detailed, waterproof stamping.','Tsukineko',TS,v=[('VersaFine Clair Ink Pads','Tsukineko')],dt='colour · pad size'),
      X('VersaColor','Tsukineko pigment ink line, described as its most colourful range.','Tsukineko',TS,dt='colour · pad size')]},
{'n':'Embossing powder','a':'','d':'Powder melted by heat over stamped ink to raise a design.','t':['clear','detail (fine)','ultra-thick','glitter','metallic','colour'],'m':[],'s':OLD['craft'],
 'x':[X('Heat embossing','Technique of stamping with slow-drying ink, covering with powder and melting it with a heat tool so the image rises.','',EM,dt='powder grain (detail, regular, thick) · colour · ink used')]},
{'n':'Embossing heat tool','a':'heat gun','d':'Hot-air tool made to melt embossing powder.','t':['craft heat tool','craft heat gun'],'m':[],'s':OLD['craft']},
{'n':'Cutting die','a':'thin die · metal die','d':'Shaped metal die used in a die-cutting machine to cut paper.','t':['thin metal die','steel-rule die','nesting die','framelit (stamp-matched) die','embossing folder'],
 'm':[['Lawn Cuts','Lawn Fawn']],'s':OLD['sb'],
 'x':[X('Spellbinders Nestabilities','Spellbinders nesting dies, one of the first products of the company, which sought patent protection for its die templates in 2003 (per a company page).','Spellbinders',SP,dt='shape · nesting set size · edge detail'),
      X('Sizzix Thinlits','Thin metal dies for shapes, which can be layered for 3D effects, used in Sizzix machines.','Sizzix',GF,v=[('Framelits','Sizzix','thin dies cutting around stamped outlines'),('Steel rule dies','Sizzix','sharp dies with foam-protected blade')],dt='shape · set size · compatible machine')]},
{'n':'Manual die-cutting machine','a':'die-cutter · embossing machine','d':'Hand-cranked roller press that cuts paper with cutting dies.','t':['manual','electric','compact','wide-format'],'m':[],'s':OLD['mach'],
 'x':[X('Sizzix Big Shot','Hand-cranked tool for die cutting and embossing cardstock, foam and fabric; no electricity or software needed.','Sizzix',GF,v=[('Big Shot (manual)','Sizzix','original hand-cranked model'),('Big Shot Pro','Sizzix','embossing folders up to 12 by 14 inches'),('Big Shot Express','Sizzix','electric counterpart'),('Sidekick','Sizzix','smaller, lower-cost machine')],dt='opening width · manual or electric · plate sandwich'),
      X('Spellbinders Platinum','Spellbinders die-cutting and embossing machine line.','Spellbinders',SP,dt='opening width (Platinum 6 and larger) · platform')]},
{'n':'Craft paper punch','a':'paper punch','d':'Punch that cuts a decorative shape or border from paper.','t':['single shape','border','corner','lever (squeeze)','large-format'],'m':[],'s':OLD['craft']},
{'n':'Craft paper trimmer','a':'paper cutter · guillotine','d':'Sliding or rotary trimmer made for cutting paper and card in paper craft.','t':['rotary','guillotine','portable 12 inch','scoring'],'m':[],'s':OLD['craft'],
 'x':[X('Fiskars portable paper trimmer','Fiskars 12-inch trimmer whose blade interlocks with the rail (TripleTrack system).','Fiskars',FI,v=[('Portable Paper Trimmer','Fiskars','TripleTrack, 12 in cut'),('Rotary Blade Paper Trimmer','Fiskars','12 in, 8-sheet capacity')],dt='cut length · blade type · sheet capacity')]},
]
brands=[
B('Sizzix','United States','','Mainstream','die-cutting','Die-cutting and embossing machine and die brand.',s='knowledge'),
B('Spellbinders','United States','2003','Mainstream','dies, Nestabilities','Paper-craft die and machine maker with Platinum machines.',s=SP,sig=['Spellbinders Nestabilities','Spellbinders Platinum']),
B('Ranger','United States','','Mainstream','inks','Craft ink maker behind Tim Holtz Distress products.',s=DI,sig=['Distress ink']),
B('Tsukineko','Japan','1952','Specialist','craft inks','Japanese ink-pad maker with VersaMark, VersaFine and VersaColor.',s=TS,sig=['VersaMark','VersaFine Clair','VersaColor']),
B('Hero Arts','United States','1974','Mainstream','rubber stamps','Berkeley stamp company begun by Jackie Leventhal in 1974.',s=HA,sig=['Hero Arts rubber stamps']),
B('Altenew','United States','2014','Mainstream','layering stamps','Syracuse, NY stamp, ink and die company.',s=AL,sig=['Altenew layering stamps']),
B('Fiskars','Finland','1649','Mainstream','scissors, trimmers','Finnish maker of orange-handled scissors and paper trimmers.',s=FI,sig=['Fiskars portable paper trimmer']),
]
save('04_01',kinds,brands,[],'Kept all 8 planned kinds. No traditions. Sizzix and several details not on fetched pages left out (founding years).')
