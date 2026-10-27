import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/E2/agent')
from write import w, K
def A(n,a,d,mk,y,s,v=None,dt=""):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s}
    if v: x["v"]=[dict((k,val) for k,val in zip(("n","mk","y","d"),vv) if val) for vv in v]
    if dt: x["dt"]=dt
    return x
INN="https://www.innovadiscs.com/?p=23438"; HB="Hammer Bowling"; HE="Henselite"; DGA="Disc Golf Association"
pet=K("Pétanque boules","boules · jack (cochonnet)","Set of hollow steel balls, 70.5–80 mm and 650–800 g, thrown towards a small wooden jack.","https://en.wikipedia.org/wiki/Pétanque",
  [("La Boule Noire","Obut"),("JB Vintage","Obut")],None,["competition (FIPJP-approved)","leisure","carbon steel","stainless steel","pointer · all-rounder · shooter","striated or plain"])
pet["x"]=[
 A("ATX","","Obut's top competition boule in treated stainless steel, offered as pointer, all-rounder or shooter.","Obut","","https://obut.com/en/competition-boules/23-atx.html",
   [("ATX striated 1","Obut","",""),("ATX striated 0","Obut","",""),("ATX 3-Star","Obut","","groove 0 or 6; replacing starless ATX")],"diameter 71–76, 80 mm · 650–800 g · hardness · striation"),
 A("MATCH","","Obut's carbon-steel, black-satin competition boule for new competitors.","Obut","","https://obut.com/en/competition-boules/90-match.html",None,"diameter 71–76 mm · 650–730 g")]
lb=K("Lawn bowls","bowls · woods","Set of four biased composite balls rolled towards a jack on a green.","https://en.wikipedia.org/wiki/Bowls",
  [("Professional","Drakes Pride"),("XP","Drakes Pride"),("Fineline","Drakes Pride"),("d-tec","Drakes Pride"),("Ace","Taylor Bowls"),("Vector VS","Taylor Bowls"),("GrooVe","Aero Bowls"),("Optima","Aero Bowls")],None,
  ["flat green","crown green","indoor","size 0–7","dimpled grip","lignum vitae (vintage)"])
lb["x"]=[A("Henselite composite bowl","Henselite","The first solid plastic (phenolic) bowl, which replaced lignum vitae woods; developed through many bias models.","Henselite","1931","https://henselite.co.uk/history",
   [("Henselite",HE,"1931","inserted coloured discs"),("Uni-disc",HE,"1937","later 'Standard'"),("Championship",HE,"1959","Super Grip"),("Classic II",HE,"1989","narrower bias"),("Maestro",HE,"1992",""),("ABT-2000",HE,"1994",""),("Dreamline",HE,"2003",""),("Tiger",HE,"2003","UK market"),("Tiger II",HE,"",""),("Tiger Pro",HE,"",""),("ABT-evo",HE,"2006","")],"bias · size · weight · colour")]
tb=K("Tenpin bowling ball","bowling ball","Drilled ball of up to 16 lb with a weight block core and a plastic, urethane or reactive resin cover.","https://en.wikipedia.org/wiki/Bowling_ball",
  None,None,["polyester (plastic)","urethane","reactive resin: solid, pearl, hybrid","particle","symmetric core","asymmetric core","6–16 lb"])
tb["x"]=[
 A("Hammer urethane ball","Hammer · Purple Hammer","Faball's original urethane ball, named for its striking power; the Purple Hammer is its best-known colour.","Hammer Bowling","1981","https://en.wikipedia.org/wiki/Hammer_Bowling",
   [("Hammer",HB,"1981","urethane"),("Purple Hammer",HB,"","2016–17 batches banned by USBC in 2022"),("Purple Pearl Urethane",HB,"",""),("Nu Blue Hammer",HB,"","")]),
 A("3D Offset","","Hammer ball described as the first asymmetric-core bowling ball on the market.","Hammer Bowling","1997","https://en.wikipedia.org/wiki/Hammer_Bowling"),
 A("Black Widow","","Hammer's reactive line built round the asymmetric 'Gas Mask' core.","Hammer Bowling","2006","https://www.bowling.com/knowledge-hub/brands/hammer/hammer-black-widow-line-still-dominates-after-twenty-years",
   [("Black Widow",HB,"2006",""),("Black Widow Pearl",HB,"",""),("Black Widow Legend",HB,"",""),("Black Widow Ghost",HB,"",""),("Black Widow 2.0 Hybrid",HB,"2020s",""),("Black Widow 3.0 Solid",HB,"",""),("Black Widow 3.0 Dynasty",HB,"2026","20th anniversary")],"coverstock: solid, pearl, hybrid · weight")]
cr=K("Croquet set","","Set of mallets, coloured balls, hoops and a peg or stakes for croquet.","https://en.wikipedia.org/wiki/Croquet",
  None,None,["garden","association (six hoops, peg)","nine-wicket","four-ball or six-ball","wood, plastic or composite balls"])
cr["x"]=[A("Jaques croquet set","","Croquet set from the London games maker that published early croquet rules (1857, 1860, 1864) and helped popularise the game.","Jaques of London","1850s","https://en.wikipedia.org/wiki/Jaques_of_London",None,"mallet wood · ball material · garden or association")]
ch=K("Cornhole set","bean bag toss","Pair of 2 × 4 ft sloped boards with a 6 in hole, and eight bags in two colours.","https://en.wikipedia.org/wiki/Cornhole",
  None,None,["regulation (ACL)","tailgate or junior size","corn-filled bags","resin-filled bags"])
fd=K("Flying disc","frisbee","Plastic disc with a curled rim thrown for catch, ultimate or freestyle.","https://en.wikipedia.org/wiki/Frisbee",
  None,None,["ultimate (175 g, 27.3 cm)","freestyle (about 160 g)","recreational","foam"])
fd["x"]=[
 A("Frisbee","Pluto Platter","Fred Morrison's Pluto Platter, sold to Wham-O and renamed Frisbee: the archetype of the modern flying disc.","Wham-O","1957","https://en.wikipedia.org/wiki/Frisbee",
   [("Flyin-Saucer","Fred Morrison","1948","first plastic disc"),("Pluto Platter","Fred Morrison","1955",""),("Frisbee","Wham-O","1957","name adopted 1957–58"),("Frisbee professional model","Wham-O","1964","Headrick's thicker rim and 'Rings of Headrick'")]),
 A("Ultra-Star","","Discraft's 175 g disc used in USA Ultimate championship play.","Discraft","","https://en.wikipedia.org/wiki/Discraft",None,"175 g · colour · printed design")]
dg=K("Disc golf disc","golf disc","Small, dense flying disc shaped as a driver, mid-range or putter for disc golf.","https://en.wikipedia.org/wiki/Disc_golf",
  [("Teebird","Innova")],None,["distance driver","fairway driver","mid-range","putter","stability: turn and fade","premium or base plastic"])
dg["x"]=[
 A("Eagle","","Dave Dunipace's disc with a triangular (bevelled) rim, a first for disc golf, which founded Innova.","Innova","1983",INN),
 A("Aviar","Aviar Putt & Approach","Innova's first putter, its most popular disc.","Innova","1984",INN),
 A("Roc","","Innova's classic mid-range disc.","Innova","1987",INN),
 A("Leopard","","Innova's first iconic fairway driver.","Innova","1999",INN),
 A("Destroyer","","Innova's widely used distance driver.","Innova","2007",INN,None,"plastic: Champion, Star, DX · weight")]
bk=K("Disc golf basket","pole hole · disc golf target","Metal basket under hanging chains on a pole, the target in disc golf.","https://en.wikipedia.org/wiki/Basket_(disc_golf)",
  None,None,["permanent","portable","practice","championship, standard or basic rating"])
bk["x"]=[A("Mach Disc Pole Hole","Mach","Ed Headrick's chain-and-basket target, the first formal disc golf target and the basis of PDGA standards.","Disc Golf Association","","https://en.wikipedia.org/wiki/Basket_(disc_golf)",
   [("Mach 1",DGA,"","first chain basket"),("Mach 2 Pro",DGA,"","24 chains, entry level"),("Mach 5",DGA,"","24 chains"),("Mach 7",DGA,"","28 chains, visibility ring"),("Mach X",DGA,"","40 chains"),("Mach X Pro",DGA,"","banded, championship"),("Mach Lite",DGA,"","collapsible practice"),("Mach Shift",DGA,"","3-in-1 practice")],"chain count and rows · galvanised or powder-coated")]
boo=K("Boomerang","","Curved throwing wing made to return to the thrower or fly for distance, in every form.","https://planetcorroboree.com.au/products/14-returning-boomerang",
  None,None,["returning","long-distance","maximum time aloft (MTA)","fast catch (tri-blade)","kylie (non-returning)","wood, birch plywood or composite"])
w('E2','05_03',{"kinds":[pet,lb,tb,cr,ch,fd,dg,bk,boo],
 "brands":[
  {"n":"Obut","c":"France","f":"1955","seg":"Professional & flagship","kf":"pétanque boules","d":"Boule maker in Saint-Bonnet-le-Château, Loire.","lines":["ATX","MATCH"],"sig":["ATX"],"s":"https://www.obut.com/en/content/22-obut-history"},
  {"n":"Henselite","c":"Australia","f":"1918","seg":"Heritage manufactory","kf":"lawn bowls","d":"Bowls maker founded by William D. Hensell; made the first solid plastic bowl in 1931.","lines":["Classic II","Dreamline","Tiger"],"sig":["Henselite composite bowl"],"rel":["Drakes Pride","Taylor Bowls","Aero Bowls"],"s":"https://henselite.co.uk/history"},
  {"n":"Drakes Pride","c":"United Kingdom","seg":"Mainstream","kf":"lawn bowls","d":"Liverpool bowls brand.","rel":["Henselite"],"s":"https://www.bowlsworld.co.uk/blogs/lawn-bowls/best-lawn-bowls-brands-in-the-uk-a-comparison-guide"},
  {"n":"Taylor Bowls","c":"United Kingdom","seg":"Premium","kf":"lawn bowls","d":"Glasgow bowls maker, early user of computer-controlled lathes.","rel":["Henselite"],"s":"https://www.bowlsworld.co.uk/blogs/lawn-bowls/best-lawn-bowls-brands-in-the-uk-a-comparison-guide"},
  {"n":"Aero Bowls","c":"Australia","seg":"Premium","kf":"lawn bowls","d":"Newer Australian bowls brand built on precision manufacturing.","rel":["Henselite"],"s":"https://www.bowlsworld.co.uk/blogs/lawn-bowls/best-lawn-bowls-brands-in-the-uk-a-comparison-guide"},
  {"n":"Hammer Bowling","c":"United States","f":"1981","seg":"Professional & flagship","kf":"bowling balls","d":"Ball brand from Faball Enterprises; owned by Ebonite from 2002 and Brunswick from 2019.","lines":["Black Widow","Purple Hammer"],"sig":["Hammer urethane ball","3D Offset","Black Widow"],"rel":["Storm","Ebonite"],"s":"https://en.wikipedia.org/wiki/Hammer_Bowling"},
  {"n":"Storm","c":"United States","f":"1991","seg":"Professional & flagship","kf":"bowling balls","d":"Brigham City, Utah ball maker grown from High Score Products (1985); owns Roto Grip and 900 Global.","rel":["Hammer Bowling"],"s":"https://en.wikipedia.org/wiki/Storm_Products"},
  {"n":"Ebonite","c":"United States","f":"1905","seg":"Heritage manufactory","kf":"bowling balls","d":"Old bowling ball maker that owned Hammer and Track; assets bought by Brunswick in 2019.","rel":["Hammer Bowling"],"s":"https://www.bowlerx.com/resources/bowling-ball-manufacturers/"},
  {"n":"Jaques of London","c":"United Kingdom","f":"1795","seg":"Heritage manufactory","kf":"croquet, games","d":"Family games maker founded by Thomas Jaques; early croquet rule publisher and maker of the first Staunton chess sets.","sig":["Jaques croquet set"],"s":"https://en.wikipedia.org/wiki/Jaques_of_London"},
  {"n":"Wham-O","c":"United States","f":"1948","seg":"Mainstream","kf":"Frisbee","d":"Toy maker founded by Richard Knerr and Arthur Melin in South Pasadena; owner of the Frisbee.","sig":["Frisbee"],"rel":["Discraft"],"s":"https://en.wikipedia.org/wiki/Wham-O"},
  {"n":"Discraft","c":"United States","f":"1978","seg":"Specialist","kf":"ultimate, disc golf discs","d":"Flying disc maker begun in London, Ontario, now in Wixom, Michigan.","sig":["Ultra-Star"],"rel":["Wham-O","Innova"],"s":"https://en.wikipedia.org/wiki/Discraft"},
  {"n":"Innova","c":"United States","f":"1983","seg":"Professional & flagship","kf":"disc golf discs","d":"Disc golf maker co-founded by Dave Dunipace to make his bevelled-rim discs.","lines":["Champion","Star","DX"],"sig":["Eagle","Aviar","Destroyer"],"rel":["Discraft","Disc Golf Association"],"s":INN},
  {"n":"Disc Golf Association","c":"United States","f":"1976","seg":"Specialist","kf":"disc golf baskets","d":"First disc golf company, founded by Ed and Ken Headrick; maker of Mach baskets.","sig":["Mach Disc Pole Hole"],"s":"https://en.wikipedia.org/wiki/Disc_golf"}],
 "traditions":[],
 "notes":"New shelf: eight kinds added (Pétanque boules, Lawn bowls, Tenpin bowling ball, Croquet set, Cornhole set, Flying disc, Disc golf disc, Disc golf basket); old Boomerang kept with its source and given types. Archetypes from Obut, Henselite, Hammer/bowling.com, Jaques, Frisbee/Discraft and Innova pages. Left out for want of a retrieved page naming them: La Boule Bleue, Storm/Roto Grip/Brunswick/Ebonite ball models, Discraft Buzzz and MVP discs, DGA Mach 3 and other basket makers, cornhole board makers. Henselite 'Tiger II' and 'Tiger Pro' undated."})
