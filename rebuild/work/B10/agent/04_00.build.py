import json, os
old = {k['target_kind']: k for k in json.load(open('work/B10/agent/04_00.old.json'))}
used = set()
def mk_of(kind, model):
    for m, b in old[kind]['m']:
        if m == model: used.add((kind, m)); return b
    raise SystemExit('missing ' + model)
def V(kind, model, d=''):
    return {"n": model, "mk": mk_of(kind, model), "y": "", "d": d}
def rest(kind, skip_generic=True):
    return [[m, b] for m, b in old[kind]['m'] if (kind, m) not in used and b]
W_ES='https://en.wikipedia.org/wiki/English_saddle'; W_WS='https://en.wikipedia.org/wiki/Western_saddle'
HC='https://www.hermes.cn/cn/en/story/116261-bespoke-equestrian'
ES='English saddle'; WS='Western saddle'; AS='Australian stock saddle'
TREE='tree: laminated wood, spring tree, synthetic · adjustable gullet on some models · seat size · leather or synthetic'
eng = {"n":ES,"a":"","d":"A saddle of the English riding tradition: no horn, padded panels, girthed on billets under the flaps.","s":old[ES]['s'],
 "x":[
  {"n":"Close-contact jumping saddle","a":"jumping saddle · hunter saddle","d":"Forward-cut flap for the short stirrups of show jumping, hunter and cross-country riding.","mk":"","y":"","s":W_ES,
   "v":[{"n":"Vivace","mk":"Hermès","y":"","d":"flat seat; successor to the Steinkraus and Allegro"},
        {"n":"Cavale II","mk":"Hermès","y":"","d":"mid-depth seat; with Simon Delestre"},
        {"n":"Faubourg","mk":"Hermès","y":"","d":"deep seat; with Jérôme Guéry"},
        V(ES,"PASSIERBLU Motion close contact saddle"),V(ES,"Amerigo DJ Close Contact Jumping Saddle"),V(ES,"Amerigo Vega Special Close Contact Jump Saddle"),
        V(ES,"Bates Elevation+ Jump Saddle"),V(ES,"Bates Elevation DS+ Jump Saddle"),V(ES,"Henri de Rivel Evolution Close Contact Saddle"),
        V(ES,"Henri de Rivel Equipe Covered Close Contact Saddle"),V(ES,"M. Toulouse Premia Close Contact Saddle"),V(ES,"M. Toulouse Annice Close Contact Saddle"),
        V(ES,"M. Toulouse Prague Platinum Close Contact Saddle")],
   "dt":"seat: flat, mid, deep · flap: forward-cut, monoflap · "+TREE},
  {"n":"Dressage saddle","a":"","d":"Long, straight flap and deep seat for the long leg of flatwork.","mk":"","y":"","s":W_ES,
   "v":[{"n":"Arpège","mk":"Hermès","y":"","d":"extra-deep seat; with Jessica von Bredow-Werndl"},
        V(ES,"Passier GG Extra Dressage Saddle"),V(ES,"Passier Compact Comfort Dressage Saddle"),V(ES,"Amerigo Cortina Dressage Saddle"),
        V(ES,"Amerigo Pasubio Pinerolo Dressage Saddle"),V(ES,"Amerigo Vega Monoflap Dressage Saddle"),V(ES,"Henri de Rivel Parisian Monoflap Dressage Saddle")],
   "dt":"seat depth · flap: straight, monoflap · knee blocks · "+TREE},
  {"n":"General-purpose saddle","a":"all-purpose saddle · eventing saddle","d":"Deep seat and moderately forward flap, a compromise for jumping and flatwork.","mk":"","y":"","s":W_ES,
   "v":[V(ES,"Bates All Purpose+ Saddle"),V(ES,"Bates All Purpose SC+ Saddle"),V(ES,"Wintec 2000 All Purpose Saddle"),V(ES,"Wintec 250 All Purpose Saddle"),
        V(ES,"Wintec DLux All Purpose Saddle"),V(ES,"Wintec Lite All Purpose Saddle")],
   "dt":TREE},
  {"n":"Endurance saddle","a":"","d":"Derived from military and police saddles: padded seat, extended panels and many dee rings for long rides.","mk":"","y":"","s":W_ES,
   "v":[V(ES,"Bates Kimberly Outback Heritage Endurance Saddle")],"dt":""},
  {"n":"Showing saddle","a":"","d":"Flat seat, little padding and a straight flap to show off the horse's shoulder; descends from the hunting saddle.","mk":"","y":"","s":W_ES,"v":[],"dt":""},
  {"n":"Saddle seat saddle","a":"cutback saddle","d":"Long flat seat and cut-back pommel for high-action and gaited horses, mainly in North America.","mk":"","y":"","s":W_ES,"v":[],"dt":""},
  {"n":"Racing saddle","a":"","d":"Very light half-tree saddle with a long, dipless seat and extremely forward flaps.","mk":"","y":"","s":W_ES,"v":[],"dt":""},
  {"n":"Polo saddle","a":"","d":"Flat seat and long, fairly straight flaps with little padding, for freedom of movement.","mk":"","y":"","s":W_ES,"v":[],"dt":""}],
 }
eng["m"] = rest(ES)
WSV=lambda m,d='':V(WS,m,d)
west = {"n":WS,"a":"stock saddle (US) · cowboy saddle","d":"A saddle of the Western riding tradition, from vaquero saddles: horn, deep seat, high cantle and wide fenders.","s":old[WS]['s'],
 "x":[
  {"n":"Wade saddle","a":"Wade tree","d":"Slick-fork ranch saddle with a low, dally-friendly horn, built on a tree copied from Clifford Wade's saddle.","mk":"Hamley & Company","y":"1939–40","s":"https://www.cowboyshowcase.com/wade-saddle-history.html",
   "v":[{"n":"Hamley tree by Walt Youngman for Tom Dorrance","mk":"Hamley & Company","y":"1940","d":"modified original tree"},
        {"n":"Ray Hunt saddle by Dale Harwood","mk":"","y":"1962","d":"popularised the Wade at clinics"},WSV("Billy Cook Light Weight Wade Saddle")],"dt":"tree · horn cap and lip · seat · tooling"},
  {"n":"Roping saddle","a":"","d":"Heavy, sturdy saddle with a thick horn, low cantle and slick fork for quick dismounts.","mk":"","y":"","s":W_WS,
   "v":[WSV("Circle Y Bandera Ranch Roper Saddle"),WSV("Dakota Saddlery Roper Saddle")],"dt":""},
  {"n":"Barrel racing saddle","a":"barrel saddle","d":"Lightweight saddle with wide swells and a high cantle for sprints and tight turns.","mk":"","y":"","s":W_WS,
   "v":[WSV("Billy Cook Barrel Saddle 1524"),WSV("Circle Y Montana Barrel Saddle"),WSV("Dakota Saddlery RO Barrel Saddle"),WSV("Royal King Dublin Barrel Saddle"),
        WSV("King Series Stratford Barrel Saddle"),WSV("High Horse Lindale Barrel Saddle"),WSV("Silver Royal Moulton Barrel Saddle")],"dt":""},
  {"n":"Reining saddle","a":"","d":"Deep seat with free-swinging fenders for leg movement in reining.","mk":"","y":"","s":W_WS,"v":[],"dt":""},
  {"n":"Cutting saddle","a":"","d":"Deep seat and wide swells to keep the rider secure through sharp stops and turns.","mk":"","y":"","s":W_WS,"v":[],"dt":""},
  {"n":"Bronc saddle","a":"hornless bronc saddle","d":"Hornless, deep-seated rodeo saddle with wide swells and small fenders; first made by Earl W. Bascom.","mk":"","y":"1922","s":W_WS,"v":[],"dt":""},
  {"n":"Trail saddle","a":"pleasure saddle","d":"Deep, padded seat for comfort on long rides at slower paces.","mk":"","y":"","s":W_WS,
   "v":[WSV("Circle Y Alpine Flex2 Western Trail Saddle"),WSV("Billy Cook BW Trail Saddle"),WSV("Tucker Horizon North Star Trail Saddle"),
        WSV("Abetta Comfort Synthetic Gaited Western Trail Saddle"),WSV("Fabtron Lightweight Draft Saddle"),WSV("High Horse Lockhart Trail Saddle")],"dt":"leather or synthetic · gaited or draft trees"},
  {"n":"Western endurance saddle","a":"","d":"Lighter, often hornless saddle whose tree spreads weight for faster long rides.","mk":"","y":"","s":W_WS,
   "v":[WSV("Tucker Horizon Outpost Endurance Trail Saddle"),WSV("High Horse Highbank Endurance Saddle")],"dt":""},
  {"n":"Western show saddle","a":"equitation saddle","d":"Built on other trees with added tooling and silver; equitation versions have a very deep seat.","mk":"","y":"","s":W_WS,
   "v":[WSV("High Horse Gladewater Show Saddle")],"dt":"tooling · silver conchos and corners"},
  {"n":"Ranch saddle","a":"","d":"Hard-seated working saddle for everyday ranch riding.","mk":"","y":"","s":W_WS,"v":[WSV("Silver Royal Bodie Hard Seat Ranch Saddle")],"dt":""},
  {"n":"McClellan saddle","a":"","d":"US Army cavalry saddle designed by George B. McClellan: rawhide-covered open seat, centre-fire rigging, wooden stirrups.","mk":"","y":"1859","s":"https://en.wikipedia.org/wiki/McClellan_saddle",
   "v":[{"n":"M1859","mk":"","y":"1859","d":"original; Civil War"},{"n":"M1904","mk":"","y":"1904","d":"adjustable rigging; most common, both World Wars"},
        {"n":"M1913","mk":"","y":"1913","d":"packers' version"},{"n":"M1928","mk":"","y":"1928","d":"English rigging and fenders; last US service variant"}],"dt":"seat 11–12½ in"}]}
west["m"] = [x for x in rest(WS) if x[0] in ("Billy Cook Pleasure Training Saddle","Circle Y Roughout Trainer Western Saddle","Dakota Saddlery Trainer Roughout Western Saddle","Billy Cook Paycheck Supreme","Cashel Trail Saddle","Wintec All Rounder Western Saddle","Circle Y Salt River Trail Saddle","Abetta Comfort Synthetic Draft Western Pleasure Saddle","Royal King Sparks All Around Youth Western Saddle","Silver Royal Brisbee Youth Barrel Saddle")]
W_AS='https://en.wikipedia.org/wiki/Australian_stock_saddle'
aus = {"n":AS,"a":"","d":"A saddle of the Australian stock-riding tradition, with knee pads (poleys) and a deep seat.","s":old[AS]['s'],
 "x":[
  {"n":"Wagga saddle","a":"","d":"Raised, firmly packed knee pad and shortened seat; made by William Mitchell Jnr of Wagga Wagga.","mk":"","y":"c.1863","s":W_AS,"v":[],"dt":""},
  {"n":"Outlaws Master","a":"","d":"Jack Wieneke's design with very large knee and thigh pads, made for a difficult horse.","mk":"Jack Wieneke","y":"1898","s":W_AS,"v":[V(AS,"Jack Wieneke Outlaws Master")],"dt":""},
  {"n":"Poley saddle","a":"broken-neck saddle","d":"Flattened seat and knee pads raised near the pommel; attributed to Albert Cox of Miriam Vale, Queensland.","mk":"","y":"1920s","s":W_AS,"v":[V(AS,"Syd Hill Barkley Stock Saddle"),V(AS,"Bates Kimberley Stock Saddle")],"dt":""},
  {"n":"Half-breed saddle","a":"half breed","d":"Australian tree and seat with a Western-style swinging fender and stirrups.","mk":"","y":"","s":W_AS,
   "v":[V(AS,"Syd Hill Half Breed Saddle"),V(AS,"Bates Kimberley Halfbreed Saddle"),{"n":"Bates Kimberley HB Rough Out","mk":"Bates","y":"","d":"rough-out leather"}],"dt":""},
  {"n":"Swinging-fender stock saddle","a":"","d":"Traditional stock saddle with Western-style stirrup leathers that do not pinch the leg.","mk":"","y":"","s":W_AS,"v":[V(AS,"Wintec Pro Stock Swinging Fender Saddle")],"dt":""},
  {"n":"Cross-breed saddle","a":"","d":"Australian swells and deep seat combined with a horn or Western cantle.","mk":"","y":"","s":W_AS,"v":[],"dt":""}]}
used.add((AS,"Bates Kimberley HB Rough Out"))
side = {"n":"Side saddle","a":"sidesaddle · aside saddle","d":"A saddle on which the rider, traditionally a woman, sits with both legs on the near side.","s":"https://en.wikipedia.org/wiki/Sidesaddle",
 "x":[{"n":"Leaping-horn side saddle","a":"two-pommel side saddle","d":"Adds a second, lower pommel over the left thigh, letting riders gallop, hunt and jump; invented by Jules Pellier.","mk":"","y":"1830s","s":"https://en.wikipedia.org/wiki/Sidesaddle","v":[],"dt":"tree · balance strap · slipper or safety stirrup"},
      {"n":"Western side saddle","a":"","d":"Double-rigged Western side saddle developed by Charles Goodnight for his wife.","mk":"","y":"1870s","s":W_WS,"v":[],"dt":""}]}
treeless = {"n":"Treeless saddle","a":"","d":"A saddle without a rigid internal tree, so it conforms to the horse's back.","s":"https://equisearch.com/articles/treeless_091003/",
 "x":[{"n":"Ansur","a":"","d":"Layered leather-and-foam treeless saddle designed by dressage trainer Peter DeCosemo; dressage, trail, endurance and cross-country models.","mk":"Ansur Saddlery","y":"","s":"https://equisearch.com/articles/treeless_091003/","v":[],"dt":""}]}
pack = {"n":"Pack saddle","a":"","d":"A frame saddle that carries a load, not a rider, on a pack animal.","t":["sawbuck","Decker","adjustable tree"],"s":old['Pack saddle']['s'],
 "m":[[m,"Outfitters Supply"] for m,b in old['Pack saddle']['m']]}
pad_keep=["Mattes"]
pad = {"n":"Saddle pad","a":"numnah · saddle cloth","d":"A pad or cloth worn under a saddle to protect the horse's back and absorb sweat.","t":["shaped numnah","square saddle cloth","half pad","sheepskin pad","gel or riser pad","Western saddle blanket"],"s":old['Saddle pad']['s'],
 "m":[["Mattes Half Pad All Purpose","EA Mattes"]]+[[m,b] for m,b in old['Saddle pad']['m'] if m in ("Acavallo Respira Gel Pad","Back on Track Haze Therapeutic Dressage Saddle Pad","Ecogold Secure Dressage Saddle Pad","Ecogold Secure Cross Country Saddle Pad","Equine Management Gel-Eze Wither Pad","Jacks Jumper Saddle Pad","Schockemöhle Nitro Jumping Close Contact Saddle Pad","Toklat Classics III Dressage Pad","Toklat Medallion AP Quilted Competition Pad","TuffRider All Purpose Saddle Pad","Weatherbeeta Prime Air-Tec All Purpose Saddle Pad","Woof Wear Vision Aura Saddle Pad","Woof Wear Elite Comfort Saddle Pad")]}
girth = {"n":"Horse girth","a":"cinch (Western)","d":"A strap under the horse's belly that holds the saddle on.","t":["Balding","Atherstone","overlay","threefold","dressage (Lonsdale)","anatomic","elastic-ended","belly-guard (stud) girth","Western cinch","overgirth"],"s":old['Horse girth']['s'],
 "m":[[m,b] for m,b in old['Horse girth']['m'] if m in ("Arma Supafleece anatomic girth","Arma memory foam dressage girth","EquiRoyal neoprene adjustable girth","Equitare shoulder relief synthetic English girth","JT International Aussie Air-Flow PVC nyloprene girth","LeMieux Integrated Web Wool dressage girth","Lettia CoolMax fleece lined girth","Micklem Long Comfort girth","Ovation Airform chafeless style girth","Schneiders Anatomic dressage girth","Stubben Equi-Soft dressage girth","Stubben Contoured Neoprene Coolmax short girth","Toklat T3 FlexForm Coolback dressage girth","Total Saddle Fit StretchTec Shoulder Relief girth","Collegiate anatomic girth","Joseph Sterling Pro Series dressage girth")]}
ST='Stirrup'; W_ST='https://en.wikipedia.org/wiki/Stirrup'
stir = {"n":"Stirrup","a":"stirrup iron · stirrup leather","d":"A foot rest hung from a saddle on a leather, for the rider.","t":["stainless steel","aluminium or composite","wide tread","stirrup leathers"],"s":old[ST]['s'],
 "x":[{"n":"Fillis iron","a":"","d":"Standard iron with a heavy tread and branches rising to the eye in a rounded triangle.","mk":"","y":"","s":W_ST,"v":[],"dt":"tread width · stainless steel · rubber tread"},
      {"n":"Prussian iron","a":"","d":"Rounder, lighter standard iron.","mk":"","y":"","s":W_ST,"v":[],"dt":""},
      {"n":"Safety stirrup","a":"","d":"Releases the foot in a fall, through a curved or breakaway outer branch.","mk":"","y":"","s":W_ST,"v":[V(ST,"Herm Sprenger Peacock stirrups"),V(ST,"Herm Sprenger AERO Safety stirrups")],"dt":""},
      {"n":"Jointed stirrup","a":"hinged · flexible stirrup","d":"Branches hinged or jointed so the stirrup flexes with the foot.","mk":"","y":"","s":W_ST,
       "v":[{"n":"Steeltec","mk":"Stübben","y":"2007","d":"recalled in 2007 over hinge failures"},V(ST,"Herm Sprenger FLEXCITE stirrups"),V(ST,"Herm Sprenger System 4 stirrups"),V(ST,"Herm Sprenger Bow Balance stirrups")],"dt":""},
      {"n":"Icelandic stirrup","a":"","d":"Hinged stirrup with the eye fixed at 90 degrees, easing tendons and lost stirrups.","mk":"","y":"","s":W_ST,"v":[],"dt":""},
      {"n":"Side-saddle stirrup","a":"","d":"Larger eye to take the thicker side-saddle leather.","mk":"","y":"","s":W_ST,"v":[],"dt":""}]}
K='knowledge'
brands=[
 {"n":"Hermès","c":"France","f":"1837","seg":"Luxury saddlery and leather goods","d":"Paris house founded by Thierry Hermès as a harness and saddle maker; still makes made-to-measure sport saddles.","lines":["Vivace","Cavale II","Faubourg","Arpège"],"eras":["Thierry Hermès, from 1837","Émile-Maurice Hermès, early 20th century"],"sig":["Close-contact jumping saddle","Dressage saddle"],"sc":["Show jumping","Dressage"],"rel":["Devoucoux","Butet","CWD"],"s":"https://en.wikipedia.org/wiki/Herm%C3%A8s"},
 {"n":"Devoucoux","c":"France","f":"1985","seg":"Luxury competition saddles","d":"Basque saddler founded by Jean-Michel Devoucoux in Sare; high-end jumping, eventing and dressage saddles.","lines":[],"eras":[],"sig":["Close-contact jumping saddle"],"sc":["Show jumping","Eventing"],"rel":["CWD","Butet","Hermès"],"s":"https://en.wikipedia.org/wiki/Devoucoux"},
 {"n":"Butet","c":"France","f":"1986","seg":"Luxury competition saddles","d":"Saumur saddler founded by Frédéric Butet; hand-made, custom-specified jumping saddles, capped at about 2,200 a year.","lines":[],"eras":[],"sig":["Close-contact jumping saddle"],"sc":["Show jumping"],"rel":["Devoucoux","CWD","Antares"],"s":"https://equnews.com/article/varia/butet-the-saddle-for-the-stars"},
 {"n":"CWD","c":"France","f":"","seg":"Luxury competition saddles","d":"French maker of high-end jumping and dressage saddles.","lines":[],"eras":[],"sig":["Close-contact jumping saddle"],"sc":["Show jumping"],"rel":["Devoucoux","Butet"],"s":K},
 {"n":"Antares","c":"France","f":"","seg":"Luxury competition saddles","d":"French maker of high-end jumping and dressage saddles.","lines":[],"eras":[],"sig":["Close-contact jumping saddle"],"sc":["Show jumping"],"rel":["Butet","Devoucoux"],"s":K},
 {"n":"Stübben","c":"Germany","f":"1894","seg":"Saddlery","d":"German family saddlery making saddles, bridles, girths and stirrups.","lines":["Steeltec"],"eras":[],"sig":["Dressage saddle","Jointed stirrup"],"sc":["Dressage","General riding"],"rel":["G. Passier & Sohn"],"s":K},
 {"n":"G. Passier & Sohn","c":"Germany","f":"","seg":"Saddlery","d":"German saddler best known for dressage saddles; PASSIERBLU is a newer line.","lines":["PASSIERBLU"],"eras":[],"sig":["Dressage saddle"],"sc":["Dressage"],"rel":["Stübben"],"s":K},
 {"n":"Bates","c":"Australia","f":"","seg":"Adjustable-tree saddles","d":"Australian saddle maker of English and stock saddles with interchangeable gullet systems; sister brand of Wintec.","lines":["Elevation","All Purpose","Kimberley"],"eras":[],"sig":["General-purpose saddle","Half-breed saddle"],"sc":["General riding"],"rel":["Wintec"],"s":K},
 {"n":"Wintec","c":"Australia","f":"","seg":"Synthetic saddles","d":"Australian maker of synthetic, adjustable-gullet saddles; sister brand of Bates.","lines":["2000","250","Lite","DLux"],"eras":[],"sig":["General-purpose saddle"],"sc":["General riding"],"rel":["Bates"],"s":K},
 {"n":"Syd Hill","c":"Australia","f":"","seg":"Stock saddles","d":"Australian stock-saddle maker.","lines":[],"eras":[],"sig":["Poley saddle","Half-breed saddle"],"sc":["Stock riding"],"rel":["Jack Wieneke"],"s":K},
 {"n":"Jack Wieneke","c":"Australia","f":"","seg":"Stock saddles","d":"Australian saddler whose 1898 Outlaws Master set a pattern for large-padded stock saddles.","lines":[],"eras":[],"sig":["Outlaws Master"],"sc":["Stock riding"],"rel":["Syd Hill"],"s":W_AS},
 {"n":"Hamley & Company","c":"United States","f":"","seg":"Western saddlery","d":"Pendleton, Oregon, saddle shop where the Wade tree was developed.","lines":[],"eras":[],"sig":["Wade saddle"],"sc":["Ranch riding"],"rel":[],"s":"https://www.cowboyshowcase.com/wade-saddle-history.html"},
 {"n":"Billy Cook Saddlery","c":"United States","f":"","seg":"Western saddles","d":"Texas maker of Western working, barrel and trail saddles.","lines":[],"eras":[],"sig":["Barrel racing saddle","Wade saddle"],"sc":["Western riding"],"rel":["Circle Y Saddles"],"s":K},
 {"n":"Circle Y Saddles","c":"United States","f":"","seg":"Western saddles","d":"Texas maker of Western trail, barrel and roping saddles.","lines":["Flex2"],"eras":[],"sig":["Trail saddle","Barrel racing saddle"],"sc":["Western riding"],"rel":["Billy Cook Saddlery"],"s":K},
 {"n":"Ansur Saddlery","c":"United States","f":"","seg":"Treeless saddles","d":"Washington-state maker of treeless saddles founded by Peter DeCosemo.","lines":["Classic","Excel"],"eras":[],"sig":["Ansur"],"sc":["Dressage","Endurance"],"rel":[],"s":"https://equisearch.com/articles/treeless_091003/"},
 {"n":"Herm. Sprenger Metallwarenfabrik","c":"Germany","f":"","seg":"Bits and stirrups","d":"German maker of bits, stirrups and spurs.","lines":["System 4","Bow Balance","FLEXCITE"],"eras":[],"sig":["Safety stirrup","Jointed stirrup"],"sc":["English riding"],"rel":[],"s":K}]
trads=[{"n":"Walsall saddlery","g":"Leather & saddlery","r":"Walsall, West Midlands, England","p":"19th century to present; peak c.1900","d":"Town that grew from a market town into an international saddle- and bridle-making centre, employing about 10,000 in leather around 1900.","tech":"hand-stitched saddlery and bridlework","mat":"leather","forms":["English saddle","Bridle"],"ctr":["Walsall Leather Museum (opened 1988)","about 40 saddle and bridle makers today"],"auth":"maker's stamp and Walsall origin","s":"https://en.wikipedia.org/wiki/Walsall_Leather_Museum"}]
notes=("Kept all 7 old kinds (Saddle stirrup renamed Stirrup) and added Side saddle and Treeless saddle. Generic old model names became archetypes. "
 "Trimmed: English saddle keeps Ovation San Telmo, M. Toulouse Annice Jr and Premia Wide in m; Western: 55 models down to 30 versions plus 10 in m (repeat colourways or near-duplicates dropped: some Abetta, Fabtron, High Horse, Royal King, Tucker models); saddle pads 27 to 14 (Quarter sheet dropped: it is an exercise rug, not a pad); girths 24 to 16. "
 "McClellan placed under Western saddle as the American military archetype. Left out (no page retrieved or site blocked): Hermès Steinkraus/Allegro as separate versions (named only as predecessors), Devoucoux/CWD/Butet/Antares/Voltaire/Prestige/Albion model names (official sites redirected in loops or 403), Mayhew and Champion & Wilton side saddles, Barefoot treeless, Ogilvy pads, MDC and Freejump stirrups, Saumur saddlery tradition (no page describes it as a tradition). Brand stubs marked knowledge carry only facts I am confident of.")
out={"kinds":[eng,west,aus,side,treeless,pack,pad,girth,stir],"brands":brands,"traditions":trads,"notes":notes}
tmp='work/B10/agent/04_00.tmp.json'; json.dump(out,open(tmp,'w'),ensure_ascii=False,indent=1); os.replace(tmp,'work/B10/shelves/04_00.json')
print('ok', len(eng['m']), len(west['m']), [len(k.get('m',[])) for k in out['kinds']])
