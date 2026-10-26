import json, os
W='https://en.wikipedia.org/wiki/'
HS='Herm. Sprenger'; NS='Neue Schule'
def X(n,d,s,a='',mk='',y='',v=(),dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(n=a1,mk=b,y=c,d=e) for a1,b,c,e in v],"dt":dt}
kinds=[]
kinds.append({"n":"Bridle","a":"headstall · headpiece","d":"Leather or synthetic headgear holding the bit (or noseband) and reins by which a ridden horse is steered.",
 "t":["English (browband, cavesson)","Western headstall","bitted","bitless","show","working","pony / cob / full / warmblood sizes","gag bridle","quick-change fittings"],
 "s":"https://www.smartpakequine.com/horse-tack-supplies-and-equipment-687pc",
 "x":[
  X("Snaffle bridle","One-bit English bridle with browband and a cavesson-type noseband on its own sliphead, ridden with one pair of reins.",W+"Bridle",a="English bridle · hunter bridle",
    v=[("Plain cavesson noseband","","","most common English noseband, 1–2 in below the cheekbone"),
       ("Flash noseband","","","cavesson with extra strap under the chin; also called Aachen"),
       ("Drop noseband","","","sits at the chin groove; credited to the Spanish Riding School"),
       ("Figure-eight (grackle) noseband","","","crosses over the nose and under the chin; also crossed or Mexican"),
       ("Crank noseband","","","leveraged buckle, used with double bridles in dressage; also Swedish cavesson"),
       ("Kineton (Puckle) noseband","","","metal half-rings behind the bit; from racing")],
    dt="noseband type · leather colour (black, brown, havana) · padded or flat · browband (plain, clincher, diamanté) · fittings (buckle, hook stud)"),
  X("Double bridle","Bridle carrying two bits, a bradoon and a Weymouth curb on separate headpieces, with four reins and a cavesson.",W+"Double_bridle",a="Weymouth bridle · full bridle",
    v=[("FEI dressage double bridle","","","required at Prix St Georges, Intermediate and Grand Prix"),("Show hack / show hunter double","","","common in UK and Australian showing")],
    dt="bradoon sliphead · curb chain · crank or plain cavesson · rein widths (bradoon wider, curb thinner)"),
  X("Pelham bridle","English bridle for a single pelham bit, ridden with two pairs of reins or with roundings.",W+"Bridle",
    dt="two reins or bit converter (roundings) · cavesson"),
  X("Micklem bridle","Anatomical English bridle by William Micklem whose padded headpiece and high noseband avoid the facial nerves and molars; the bit can clip to the noseband.","https://blog.doversaddlery.com/?p=1934",
    a="Micklem Multibridle",mk="Horseware Ireland",y="2007",
    v=[("Micklem Multibridle","Horseware Ireland","2007","works as bridle, lunge cavesson and bitless bridle")],dt="sizes · black, brown · competition and multi versions"),
  X("Western headstall","American western bridle, usually without noseband and often with a one-ear (split-ear) strap instead of a browband.",W+"Bridle",a="western bridle · browband headstall · one-ear headstall",
    v=[("Basketweave Browband Headstall","Billy Cook Saddlery","","basketweave tooled browband"),
       ("Rawhide Braid Browband Headstall","Billy Cook Saddlery","",""),
       ("Harness Leather One Ear Headstall","Schneiders","","one-ear style"),
       ("ProTack Quick Change Rolled Single Ear Headstall","Weaver Leather","","single-ear, quick-change bit ends"),
       ("Daisetta Browband Headstall","Circle Y Saddles","",""),
       ("Oiled Hermann Oak Leather Browband Headstall","Billy Royal","",""),
       ("Basketweave Futurity Browband Ranch Headstall","Schneiders","","")],
    dt="browband, one-ear or split-ear · tooling (basketweave, floral, buckstitch) · conchos · harness or latigo leather · quick-change ends"),
  X("Barcoo bridle","Australian stock-horse bridle, usually without noseband, with crownpiece, browband and throatlatch meeting at a ring by each ear.",W+"Bridle",a="Barcoo ringhead bridle · ringhead bridle",dt="leather width · buckle or stitched bit ends"),
  X("Halter bridle","Trail and endurance headcollar with quick-release cheekpieces that carry a bit, so the bit can come off at rest stops.",W+"Bridle",a="trail bridle · endurance bridle · combination bridle",
    v=[("Deluxe Trail Halter Bridle Combo","Billy Royal","","")],dt="nylon or biothane · leather · rein clips"),
  X("Driving bridle","Harness bridle with blinkers (winkers) on the cheekpieces and a noseband built into the bridle.",W+"Bridle",a="harness bridle · blinker bridle",dt="square, round or D blinkers · overcheck or sidecheck · single or pair"),
 ],
 "m":[["Arabian Training Bridle","Premier"],["Draft Horse Browband Bridle Set","Weaver Leather"],["Pony Browband Bridle Set","Weaver Leather"],["Work Bridle","Billy Royal"],["Python Pass Browband Headstall","Circle Y Saddles"],["Horizons Browband Headstall","Weaver Leather"]]})

kinds.append({"n":"Snaffle bit","a":"snaffle · bradoon","d":"Bit acting by direct rein pressure without leverage, sorted by cheek or ring type and mouthpiece.",
 "t":["single-jointed","French link (double-jointed)","lozenge","Dr Bristol","mullen mouth","straight bar","Waterford","slow twist","twisted wire","roller","hollow mouth","rubber or plastic mouth","copper / sweet iron / stainless / alloy (Aurigan, Sensogan)","western training snaffle"],
 "s":"https://www.smartpakequine.com/horse-tack-supplies-and-equipment-687pc",
 "x":[
  X("Loose-ring snaffle","Snaffle whose rings slide through the mouthpiece ends, letting the bit move and encouraging the horse to relax its jaw.",W+"Snaffle_bit",a="loose ring",
    v=[("KK Ultra Loose Ring Snaffle",HS,"1999","45°-angled middle link; developed from Kannemeier & Koch bits"),
       ("Dynamic RS Loose Ring Snaffle",HS,"2005",""),
       ("Novocontact Loose Ring Snaffle",HS,"","oval mouthpiece"),
       ("Turnado Loose Ring Snaffle",HS,"",""),("WH Ultra Loose Ring Snaffle",HS,"",""),
       ("Verbindend Loose Ring Snaffle",NS,"",""),("Tranz Lozenge Loose Ring Snaffle",NS,"",""),
       ("Turtle Top Loose Ring",NS,"",""),("Team Up Loose Ring Snaffle",NS,"",""),("Demi-Anky Loose Ring",NS,"",""),
       ("Equikind Ripple Loose Ring","Shires","",""),("Twisted Wire Dogbone Loose Ring Snaffle","Reinsman","","western")],
    dt="ring diameter · mouthpiece width and thickness · joint type · metal"),
  X("Eggbutt snaffle","Snaffle with barrel-hinged rings fixed to the mouthpiece, so it sits still and cannot pinch the lips.",W+"Snaffle_bit",a="barrel head · eggbutt",
    v=[("KK Ultra Eggbutt",HS,"1999",""),("Dynamic RS Eggbutt Snaffle",HS,"2005",""),("Novocontact Eggbutt with Lozenge",HS,"",""),
       ("Tranz Lozenge Eggbutt Snaffle",NS,"",""),("Turtle Top with Flex Eggbutt",NS,"",""),
       ("Round Ring Jointed Eggbutt Snaffle","Happy Mouth","","plastic mouth"),("Hollow Mouth Eggbutt Snaffle","Shires","",""),("Equikind Jointed Eggbutt Flat Ring","Shires","","")],
    dt="flat or round ring · mouthpiece · metal"),
  X("D-ring snaffle","Snaffle with D-shaped rings that stop the bit rotating; the straight side gives lateral guidance.",W+"Snaffle_bit",a="racing snaffle · dee ring",
    v=[("KK Ultra D Ring Snaffle",HS,"1999",""),("Jointed Pro King Dee","Happy Mouth","",""),("Double Jointed Pro King Dee","Happy Mouth","",""),("Dee Ring Jointed Port Snaffle","Centaur","","")],
    dt="dee size · mouthpiece · metal"),
  X("Full-cheek snaffle","Snaffle with long cheek arms above and below the mouthpiece for lateral guidance; stops the bit sliding through the mouth.",W+"Snaffle_bit",a="full cheek",
    v=[("NATHE Full Cheek Snaffle with Flexible Mullen Mouth",HS,"","flexible synthetic mullen"),("Turtle Top Full Cheek",NS,"",""),
       ("Full Cheek Snaffle","Happy Mouth","",""),("Equi-Kind Mullen Full Cheek Snaffle","Shires","",""),
       ("Full Cheek Waterford Snaffle","Korsteel","",""),("Full Cheek Eggbutt Dr Bristol Mouth Snaffle","Centaur","","")],
    dt="cheek keepers · mouthpiece · metal"),
  X("Fulmer snaffle","Full-cheek bit with loose rings, combining lateral guidance with the movement of a loose ring.",W+"Snaffle_bit",a="Australian loose-ring cheek"),
  X("Half-cheek snaffle","Snaffle with a single (usually lower) cheek arm, common in racing and driving as it is less likely to snag.",W+"Snaffle_bit",a="half cheek"),
  X("Baucher snaffle","Snaffle with a hanging cheek: a small upper ring takes the bridle cheekpiece, holding the mouthpiece very still.",W+"Snaffle_bit",a="hanging cheek · Baucher"),
  X("Bradoon","Small-ringed, thinner snaffle used with a curb in the double bridle.",W+"Double_bridle",a="bridoon",dt="loose ring or eggbutt · jointed or lozenge"),
 ],
 "m":[["Avila Training Snaffle Bit","Professional's Choice"],["Equisential Half and Half Loose Ring Snaffle Bit","Professional's Choice"],["Low Port Barrel Training Snaffle","Metalab"],["Diamond R Copper Argentine Snaffle","Reinsman"],["Copper Lozenge Sweet Iron Snaffle","Shires"],["Flexible Rubber Mouth Snaffle","Shires"],["Tongue Plate Loose Ring Bit","Winning"],["Teardrop 3-Piece Copper Snaffle Bit","Weaver Leather"]],
 "r":[["Equisential","Professional's Choice"],["Copper Plus",HS],["Duo",HS],["Dynamic RS",HS],["KK Ultra",HS],["Novocontact",HS]]})

kinds.append({"n":"Curb bit","a":"leverage bit","d":"Bit with shanks and a curb chain or strap that adds leverage on the poll and chin groove.",
 "t":["solid or ported mouthpiece","jointed (cowboy snaffle)","fixed or loose cheek","shank length (Tom Thumb ≈ 2 in)","curb chain or strap"],
 "s":"https://www.smartpakequine.com/horse-tack-supplies-and-equipment-687pc",
 "x":[
  X("Weymouth","English curb with straight shanks and usually a low-port solid mouthpiece, worn with a bradoon in the double bridle.",W+"Curb_bit",a="Weymouth curb · Weymouth bit",
    v=[("KK Weymouth",HS,"",""),("HO Weymouth",HS,"",""),("Bemelmans Weymouth",HS,"",""),("FC Weymouth Aurigan",HS,"","Aurigan alloy (patented 1993)"),
       ("Aachen Weymouth",NS,"",""),("Slimma Weymouth",NS,"",""),("Turtle Tilt Weymouth",NS,"",""),("Warmblood Weymouth",NS,"",""),("Weymouth Low Port","Happy Mouth","","")],
    dt="shank length (FEI lower shank limit) · port height · fixed or sliding cheek"),
  X("Pelham","Single curb bit with snaffle rings beside the mouthpiece, ridden with two pairs of reins or a converter.",W+"Pelham_bit",
    v=[("Hard Rubber Mouth Pelham","Shires","",""),("Angle cheek pelham","","","cavalry pattern, e.g. Australian Light Horse"),("Driving pelham","","","synthetic mouthpiece for driving"),("Cowboy pelham","","","western loose-jawed curb with extra rings")],
    dt="mullen to medium port · jointed · shank length · roundings"),
  X("Kimblewick","Hybrid curb with a D-shaped snaffle-type ring and curb chain giving slight leverage on one rein.",W+"Bit_(horse)",a="Kimberwick · Kimberwicke",
    v=[("Slotted Cheek Port Mouth Kimblewick","Shires","","rein slots alter leverage")],dt="plain or slotted cheek · port or jointed"),
  X("Western curb","Traditional western curb with a solid, usually medium-port mouthpiece and shanks, ridden on a loose rein.",W+"Curb_bit",a="cowboy curb · grazing bit",
    v=[("Grazing bit","","","shanks swept back almost 90°"),("Cowboy snaffle","","","jointed-mouth curb, harsher than a ported solid curb"),
       ("Diamond R Medium Port Cowboy Shank Bit","Reinsman","",""),("Diamond R C Bit","Reinsman","",""),
       ("Equisential Performance Short Shank Bit","Professional's Choice","",""),("Bob Avila Correction Bit","Professional's Choice","",""),
       ("Pro Series Correction Copper Port Bit","Weaver Leather","",""),("Tom Thumb Bit","Shires","","shortest shank"),("Draft Low Port Curb Bit","Weaver Leather","","")],
    dt="port height · shank shape · engraved or silver-mounted cheeks · copper or sweet iron"),
  X("Spade bit","Vaquero curb with straight decorated shanks and a spoon-shaped plate above a narrow port, for finished bridle horses.",W+"Spade_bit_(horse)",a="spade",y="vaquero tradition",
    dt="spoon, cricket and braces · silver inlay and engraving · cheek pattern"),
  X("Liverpool bit","Curb with several rein slots on the cheeks to set the leverage; mainly for harness horses.",W+"Curb_bit",a="Liverpool",dt="slot used · smooth or rough side of a reversible mouthpiece"),
 ],
 "m":[["Chifney Anti-Rearing Bit","Shires"]],
 "r":[["Equisential","Professional's Choice"],["KK Ultra",HS]]})

kinds.append({"n":"Gag bit","a":"gag snaffle · elevator","d":"Bit whose cheekpieces slide through rings on the mouthpiece so rein pressure raises it in the mouth (elevator or gag action).",
 "t":["loose ring","eggbutt","rope or leather gag cheeks","used with a gag bridle"],"s":"https://millbryhill.co.uk/collections/equestrian-tack-bits",
 "x":[
  X("Running gag","Snaffle-shaped gag whose rings are drilled so rounded cheekpieces run through them to the reins.",W+"Gag_bit",a="gag snaffle",
    v=[("Balding gag","","","loose-ring running gag"),("Cheltenham gag","","","eggbutt running gag")],dt="ring size · with or without second snaffle rein"),
  X("Dutch gag","Gag with a stack of rings on each cheek: bridle on the top ring, snaffle rein on the large ring, gag rein lower down.",W+"Gag_bit",a="three-ring · four-ring · Pessoa gag · Continental gag",dt="number of rings · rein position"),
  X("American gag","Elevator bit with an H-shaped cheek: bridle ring above, snaffle loop in the middle, gag rein on the lower shank.",W+"Gag_bit",a="elevator bit",dt="shank length · mouthpiece"),
 ]})

kinds.append({"n":"Bitless bridle","a":"hackamore","d":"Headgear that steers without a mouthpiece, acting on the nose, chin or poll.",
 "s":"https://www.smartpakequine.com/horse-tack-supplies-and-equipment-687pc",
 "x":[
  X("Bosal hackamore","Vaquero hackamore: a stiff rawhide noseband with a heel knot, ridden with a mecate and sometimes a fiador, used to start young horses.",W+"Hackamore",a="jáquima · bosal",y="1840s (Californio)",
    v=[("Tooled Futurity Bosal Headstall Set","Schneiders","","")],dt="bosal diameter · rawhide plait count · mecate (horsehair or mohair) · fiador"),
  X("Sidepull","Rope, rawhide or leather noseband with rein rings at the sides, giving direct lateral pressure.",W+"Bitless_bridle",dt="rope or leather · with or without browband"),
  X("Cross-under bitless bridle","Bridle whose reins cross under the jaw to the poll, spreading pressure over nose, jaw, cheek and poll.",W+"Bitless_bridle",a="figure-eight bitless · Dr Cook",y="1988",
    v=[("Buck cross-under design","","1988","first US-patented cross-under jaw/poll design (Edward Allan Buck)"),
       ("Dr. Cook Bitless Bridle","Dr. Cook","2001","Robert Cook's design, US patent 2001"),("Western Bitless Bridle","Dr. Cook","",""),("Beta Western Bitless Bridle","Dr. Cook","","synthetic"),("Spirit Bridle","","","")],
    dt="leather, beta or nylon · English or western style"),
  X("Mechanical hackamore","Bitless headgear with curb-style metal shanks between noseband and curb chain, acting by leverage.",W+"Hackamore",a="hackamore bit · English hackamore · brockamore",y="1950s patents",
    v=[("Short Shank Hackamore",HS,"",""),("Carol Goostree CG Hackamore","Classic Equine","",""),("Little S Hackamore","Diamond R","",""),
       ("Brittany Pozzi Hackamore","Professional's Choice","",""),("Hackamore Fleece Lined Chrome Plated Cheeks","Schneiders","","")],
    dt="shank length · noseband (rope, leather, fleece, bike chain) · curb chain"),
  X("Jumping cavesson","Heavy cable- or rope-cored leather noseband with rein rings at the side, used in English jumping.",W+"Hackamore",a="English hackamore · jumping hackamore"),
  X("Scawbrig","Bitless bridle whose reins pass through a noseband ring and under the chin to the opposite side; known in Germany as the Meroth.",W+"Bitless_bridle",a="Meroth"),
  X("Wheel hackamore","European bitless bridle with a six-spoked metal wheel each side giving mild leverage.",W+"Bitless_bridle",a="LG bridle · Glücksrad"),
 ],
 "m":[["Justin Dunn Bitless Browband Bridle","Weaver Leather"],["Nylon Rope Caveson","Dura-Tech"]]})

kinds.append({"n":"Reins","a":"horse reins","d":"Pair of straps or a rope fixed to the bit or noseband, by which a rider or driver steers; sold apart from the bridle.",
 "t":["closed (loop) reins","laced","plaited","rubber-grip","web with hand stops","double-bridle curb and bradoon reins","roping / barrel reins","draw / running reins","driving reins","leather, nylon, rope, biothane"],
 "s":"https://horze.eu/rubber-reins",
 "x":[
  X("Split reins","Two long separate western reins with unconnected ends that drop without tangling the horse's feet.",W+"Reins",
    v=[("Rawhide Braid End Split Reins","Billy Cook Saddlery","",""),("Quick Change Leather Split Reins","Circle Y Saddles","",""),("Working Cowboy Split Reins","Weaver Leather","",""),("Split Reins Single Ply","Tory Leather","","")],
    dt="harness or latigo leather · weight · water-loop or quick-change ends"),
  X("Romal reins","Vaquero closed reins ending in a long quirt (romal), held in one hand.",W+"Reins",a="romal",
    v=[("Rawhide Romal Reins","Professional's Choice","",""),("Ranch Heavy Oil Romal Reins","Professional's Choice","",""),("Harness Leather Romel Reins","Weaver Leather","","")],dt="rawhide or leather · braiding · silver"),
  X("Mecate","Single long rope used with a bosal that forms both a closed rein and a lead rope.",W+"Reins",a="McCarty",dt="horsehair or mohair · length"),
 ],
 "m":[["X-Line Rubber Lined Leather Reins","Waldhausen"],["Leather Double Bridle Curb Reins","Waldhausen"],["Plaited Reins","Joseph Sterling"],["Thumb Grip Rubber Reins","Horseware Ireland"],["Laced Rein","Premier"],["Cotton Web Reins","Premier"],["Laced Leather Reins with Rubber Grip Lining","Schneiders"],["Braided Nylon Barrel Rein","Weaver Leather"],["Emerald Twist Latigo Roping Reins","Professional's Choice"],["Adjustable Trail Rein","Circle Y Saddles"],["Stacy Westfall ProTack Western Dressage Rein","Weaver Leather"]]})

kinds.append({"n":"Martingale and breastplate","a":"martingale · breastplate · breastcollar · tiedown","d":"Straps from the girth that limit head carriage (martingale) or stop the saddle slipping back (breastplate).",
 "t":["standing martingale","running martingale","Irish martingale","German martingale (Market Harborough)","western tiedown","hunting breastplate","racing / polo breastcollar","elastic breastgirth","western breast collar","combined breastplate with martingale attachment"],
 "s":"https://www.smartpakequine.com/horse-tack-supplies-and-equipment-687pc",
 "m":[["Standing martingale","Pinnacle"],["Raised fancy stitched standing martingale","Premier"],["Raised standing martingale with fancy stitching","Schneiders"]]})

brands=[
 {"n":HS,"c":"Germany","f":"1872","seg":"bit, spur and stirrup maker","d":"Family firm in Iserlohn making bits, spurs and stirrups by hand; developed Aurigan and Sensogan alloys and the KK Ultra bit.",
  "lines":["KK Ultra (1999)","Dynamic RS (2005)","Novocontact","WH Ultra","Turnado","Aurigan (1993)","Sensogan (2013)"],"eras":["Founded by Hermann Sprenger, 1872","Acquired Kannemeier & Koch, 1992"],
  "sig":["Loose-ring snaffle","Weymouth"],"sc":["dressage","show jumping"],"rel":[NS],"s":"https://sprenger.de/en/history"},
 {"n":NS,"c":"","f":"","seg":"specialist bit maker","d":"Bit maker known for ergonomically shaped mouthpieces; Official Bit of US Equestrian since 2015.",
  "lines":["Verbindend","Tranz Lozenge","Turtle Top","Team Up","Slimma"],"eras":[],"sig":["Loose-ring snaffle","Weymouth"],"sc":["dressage","show jumping","eventing"],"rel":[HS],"s":"https://usef.org/media/press-releases/neue-schule-official-bit-of-us-equestrian"},
 {"n":"Myler","c":"United States","f":"","seg":"specialist bit maker","d":"Bits designed by brothers Dale, Ron and Bob Myler, made at their shop in Marshfield, Missouri.",
  "lines":[],"eras":[],"sig":[],"sc":["western","English"],"rel":[],"s":"https://blog.cheshirehorse.com/2015/04/13/myler-bit-clinic-april-18th/"},
 {"n":"Horseware Ireland","c":"Ireland","f":"","seg":"horse rugs and tack","d":"Irish equestrian firm led by Tom MacGuinness that took on William Micklem's bridle in 2007.",
  "lines":["Micklem","Rambo"],"eras":[],"sig":["Micklem bridle"],"sc":["eventing"],"rel":[],"s":"https://blog.doversaddlery.com/?p=1934"},
 {"n":"Dr. Cook","c":"United States","f":"","seg":"bitless bridles","d":"Cross-under bitless bridle developed by Robert Cook, US patent 2001.",
  "lines":["Beta Western Bitless Bridle"],"eras":[],"sig":["Cross-under bitless bridle"],"sc":["trail","endurance"],"rel":[],"s":W+"Bitless_bridle"},
 {"n":"Stübben","c":"Germany","f":"1894","seg":"saddlery and bridles","d":"Family saddlery founded in Krefeld making saddles, bridles and leather tack.",
  "lines":[],"eras":[],"sig":[],"sc":["dressage","show jumping"],"rel":[],"s":"knowledge"},
]
notes=("Bridle: old flat headstall SKUs folded into archetypes (Western headstall versions) or kept as ≤6 models; bridle names (snaffle, double, pelham, Barcoo, halter, driving) became archetypes; gag bridle is a type. "
 "Nosebands are versions of the snaffle bridle (sourced from Bridle/Noseband pages). Snaffle bit: cheek types are archetypes, mouthpieces are types; Waterford kept as type. "
 "Curb bit: Weymouth, pelham, kimblewick, western curb, spade, Liverpool as archetypes; Chifney (an in-hand anti-rearing bit) kept as one model. "
 "Martingale kind kept tier-style with martingale and breastplate types, as briefed. Left out: Myler and Neue Schule product archetypes (no retrieved product page; Myler page 404), Stübben (brand only, from knowledge), Micklem award year, Neue Schule country/founding (not on a retrieved page). "
 "Old 'Horse reins' renamed 'Reins'. Weaver Equine maker names normalised to Weaver Leather; Herm. Sprenger Metallwarenfabrik shortened to Herm. Sprenger.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/B10/shelves/04_01.json'
os.makedirs(os.path.dirname(p),exist_ok=True)
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p); print('ok')
