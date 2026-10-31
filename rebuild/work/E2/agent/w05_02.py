import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/E2/agent')
from write import w, K
def A(n,a,d,mk,y,s,v=None,dt=""):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s}
    if v: x["v"]=[dict((k,val) for k,val in zip(("n","mk","y","d"),vv) if val) for vv in v]
    if dt: x["dt"]=dt
    return x
CH19="https://patrickchaplin.com/2019/05/22/the-nodor-winmau-story/"
CH22="https://patrickchaplin.com/2022/02/22/record-deal-announced-as-the-professional-darts-corporation-and-winmau-team-up-with-official-partnership/"
UNI="https://doubletopdartshop.com/blogs/news/the-history-of-unicorn-darts"
PR="https://predatorcues.com/pages/our-story"; MZ="https://miki-mezz.com/english/?p=15"
U="Unicorn Darts"; T="Target Darts"; P="Predator Cues"; M="Mezz"; B="Brunswick Billiards"; O="Olhausen Billiards"
dart=K("Dartboard","","Target board made for darts, of bristle, cork or electronic segments.","https://en.wikipedia.org/wiki/Dartboard",
  [("Quadro 240","Harrows")],None,["bristle (sisal)","electronic (soft-tip)","cork or coiled paper","elm (historical)","with cabinet"])
dart["x"]=[
 A("Original Bristle Dartboard","Nodor bristle board","Sisal-fibre board bound in a metal ring, devised by Ted Leggatt and publican Frank Dabbs; darts part the fibres instead of pocking wood.","Nodor","1935",CH19,
   [("Original Bristle","Nodor","1935","replaced soaked elm boards"),("Supabull","Nodor","1984","first staple-free bullseye")],"spider: staple-free or round, triangular, blade wire · numbering ring"),
 A("Blade","Winmau Blade","Winmau's bristle board with thin blade wiring sold as no-bounce; the PDC board.","Winmau","1997",CH22,
   [("Blade","Winmau","1997","'ultimate no-bounce dartboard'"),("Blade 6 Triple Core","Winmau","2021","three-part sisal core; PDC board 2022–2027"),("Blade 6 Triple Core Carbon","Winmau","","carbon-reinforced version")],"core: single, dual, triple · carbon · PDC branding"),
 A("Eclipse","","Unicorn's tournament bristle board line.","Unicorn Darts","",UNI,
   [("Eclipse Pro 2","Unicorn Darts","",""),("Eclipse Ultra 2.0","Unicorn Darts","","")],"wire profile · cabinet bundle")]
darts=K("Darts","dart set","Set of three throwing darts of barrel, shaft and flight, with steel or soft tips.","https://en.wikipedia.org/wiki/Darts",
  [("Elysian Archetype 43",T)],None,["steel-tip","soft-tip","brass barrel","nickel-silver barrel","tungsten alloy 80–95%","up to 50 g"])
darts["x"]=[
 A("Silver Comet","","Frank Lowy's first Unicorn darts, sold as a matched set of three of equal weight.","Unicorn Darts","1937",UNI,None,"matched weight · alloy shafts"),
 A("Phil Taylor Power 9Five","Power 9Five","Target's 95% tungsten signature darts for Phil Taylor, released in numbered generations.","Target Darts","",
   "https://aviddarts.com.au/products/target-phil-taylor-gen-10-darts-swiss-point-steel-tip-95-tungsten-22g-24g-26g",
   [("Power 9Five G5","Target Darts","","made after his 2018 retirement from the PDC"),("Power 9Five G10","Target Darts","","Swiss Point removable points")],"22 g, 24 g, 26 g · steel or soft tip"),
 A("Wraith","","Unicorn's Wraith barrel line used for player signature darts, e.g. Gary Anderson Phase 6.","Unicorn Darts","",UNI,
   [("Wraith Phase 6 (Gary Anderson)","Unicorn Darts","",""),("Wraith Phase 2 (James Wade)","Unicorn Darts","","")],"weight · grip pattern")]
cue=K("Pool cue","cue · cue stick","Tapered stick used to strike the balls in pool, snooker and billiards.","https://www.pooldawg.com/pool-cues",
  [("AVID Chroma Highlands","Cuetec Cues"),("AVID Surge Break","Cuetec Cues"),("EBM02","Eight Ball Mafia"),("Heavy 27oz Banned Break","Elite Pool Cues"),("Power Piston 2","Meucci Originals"),("TL11","Talon Cues")],None,
  ["pool","snooker (ash, three-quarter jointed)","carom","break","jump","massé","one-piece","two-piece","sneaky pete"])
cue["x"]=[
 A("Balabushka cue","Bushka","Plain straight-grain maple cue with steel joint and ebony-ivory 'Bushka rings', made in Brooklyn; the most coveted collector cue.","George Balabushka","1959–1975","https://en.wikipedia.org/wiki/George_Balabushka",
   [("Balabushka original","George Balabushka","1959–1975","Titlist, Burton Spain, then Szamboti blanks"),("Adam Balabushka replica","Adam Custom Cue Company","1980s","licensed by his family"),("GB23","Balabushka Cues","","")],"blank era · wrap · rings · length 57½ in"),
 A("Predator 314 shaft","314","Pie-spliced low-deflection shaft with a light front end, Predator's founding product.","Predator Cues","1994",PR,
   [("314","Predator Cues","1994",""),("Z","Predator Cues","2003",""),("Vantage","Predator Cues","2014","stiffer"),("REVO","Predator Cues","2016","carbon fibre composite")],"tip size · joint type"),
 A("Predator BK break cue","BK","Predator's dedicated break cue line.","Predator Cues","2001",PR,
   [("BK","Predator Cues","2001",""),("BK2","Predator Cues","2005",""),("BK3","Predator Cues","2012",""),("BK-Rush","Predator Cues","2017",""),("BK-Rush+","Predator Cues","2020","break/jump")]),
 A("Predator Air jump cue","Air","Predator's short, light jump cue line.","Predator Cues","2007",PR,
   [("Air","Predator Cues","2007",""),("Air II","Predator Cues","2013",""),("Air Rush","Predator Cues","2021","")]),
 A("McDermott cue","","Two-piece production cue from Menomonee Falls, Wisconsin.","McDermott Cue Manufacturing","1975","https://cbs58.com/news/wisconsin-a-melting-pot-of-pool-cue-makers-like-mcdermott-cue",
   [("G206","McDermott Cue Manufacturing","","")],"series · inlays · shaft"),
 A("Mezz cue","","Japanese cue line from the Miki workshop in Tomioka, known for its Hybrid and carbon shafts.","Mezz","1995",MZ,
   [("Power Break","Mezz","2002","composite-wood break cue"),("ACE series","Mezz","2008",""),("WX900 shaft","Mezz","2013",""),("AXI-15","Mezz","2015",""),("Ignite 12.2 carbon shaft","Mezz","2019",""),("EC-9","Mezz","2019","")],"series · shaft: Hybrid, WX, Ignite carbon"),
 A("Parris snooker cue","John Parris cue","Hand-made snooker cue from John Parris's Forest Hill workshop, used by many world champions.","Parris Cues","1984","https://en.wikipedia.org/wiki/Parris_Cues",None,"ash shaft · splicing · tip size")]
table=K("Pool table","billiard table","Cloth-covered slate or board table with cushions, with or without pockets, made for pool, snooker or billiards.","https://billiardfactory.com/all-pool-tables",
  [("Dameron",B),("Parsons",B),("Sagrada",B),("Soho",B),("Viking","C.L. Bailey Billiards"),("Cordoba","California House Billiards"),("Augusta",O),("Breckenridge",O),("Luxor",O),("Metro",O),("Townhouse",O),("Beaumont","Plank & Hide Co."),("Deco","Plank & Hide Co."),("Kalahari","Presidential Billiards"),("Amerigo","True Billiards"),("Telluride","True Billiards"),("Velocity Pro","Velocity Billiards"),("Velocity Tournament","Velocity Billiards")],None,
  ["American pool (7, 8, 9 ft)","English pool (6–7 ft)","snooker (12 × 6 ft)","carom (pocketless)","slate or board bed"])
table["x"]=[
 A("Gold Crown","","Brunswick's tournament pool table, with doweled slate and Super Speed cushions.","Brunswick Billiards","1961","https://brunswickbilliards.com/pages/gold-crown-vii",
   [("Gold Crown I",B,"1961",""),("Gold Crown II",B,"1974",""),("Gold Crown III",B,"1976",""),("Gold Crown IV",B,"1998","embedded levellers"),("Gold Crown V",B,"2008",""),("Gold Crown VI",B,"2016",""),("Gold Crown VII",B,"2025","8 ft and 9 ft")],"size 8 ft, 9 ft · finish"),
 A("Riley snooker table","","Full-size slate snooker table from E.J. Riley of Accrington, once among the largest billiard table makers.","E.J. Riley","1890s","https://snookerheritage.co.uk/company-histories/ej-riley/",None,"full-size or smaller · five-piece slate")]
case=K("Cue case","cue tube","Hard, soft or leather case holding cue butts and shafts, sized by count (e.g. 2x4).","https://www.pooldawg.com/brand/pool-cue-cases",
  [("Proline 2x4 Hard","Cuetec Cues"),("3x7 Geo Leather","Instroke"),("4x7 Hard/Soft Hybrid","McDermott Cue Manufacturing"),("Metro 2x4",P),("Camo 2x4 Soft","Poison"),("Special Edition 2x4","Purex")],None,
  ["1x1","2x2","2x4","3x5","4x8","hard","soft","leather"])
case["s"]="https://seyberts.com/blogs/news/best-pool-cue-cases"
w('E2','05_02',{"kinds":[dart,darts,cue,table,case],
 "brands":[
  {"n":"Nodor","c":"United Kingdom","f":"1919","seg":"Heritage manufactory","kf":"bristle dartboards","d":"Ted Leggatt's company that launched the bristle dartboard in 1935 and the staple-free Supabull; owns Winmau since 2002.","sig":["Original Bristle Dartboard"],"rel":["Winmau"],"s":CH19},
  {"n":"Winmau","c":"United Kingdom","f":"1945","seg":"Professional & flagship","kf":"dartboards","d":"Welsh dart and dartboard maker begun by Harry Kicks; PDC board supplier.","sig":["Blade"],"rel":["Nodor"],"s":"https://en.wikipedia.org/wiki/Winmau"},
  {"n":"Unicorn Darts","c":"United Kingdom","f":"1937","seg":"Heritage manufactory","kf":"darts, dartboards","d":"London darts maker founded by Frank Lowy with the Silver Comet matched set.","sig":["Silver Comet","Eclipse","Wraith"],"rel":["Target Darts","Winmau"],"s":UNI},
  {"n":"Target Darts","c":"United Kingdom","seg":"Professional & flagship","kf":"tungsten darts","d":"British darts brand making Phil Taylor's and Luke Littler's darts.","sig":["Phil Taylor Power 9Five"],"rel":["Unicorn Darts","Red Dragon"],"s":"https://dartsworld.com/2025/09/target-darts-pop-ups-innovation-egos-and-600-screwdrivers/"},
  {"n":"Red Dragon","c":"United Kingdom","f":"1975","seg":"Mainstream","kf":"tungsten darts","d":"Bridgend tungsten dart brand started by two former Ford engineers, sold direct to players.","rel":["Target Darts"],"s":"https://www.reddragondarts.com/blogs/news/red-dragon-darts-marks-50-years-with-launch-of-limited-classics"},
  {"n":"George Balabushka","c":"United States","f":"1959","seg":"Artisan & independent","kf":"collector pool cues","d":"Brooklyn cue maker (1959–1975) whose plain cues are the most sought after.","sig":["Balabushka cue"],"s":"https://en.wikipedia.org/wiki/George_Balabushka"},
  {"n":"Predator Cues","c":"United States","f":"1994","seg":"Professional & flagship","kf":"low-deflection shafts","d":"Jacksonville cue maker that popularised low-deflection and carbon shafts.","lines":["314","Z","REVO","BK","Air"],"sig":["Predator 314 shaft"],"s":PR},
  {"n":"McDermott Cue Manufacturing","c":"United States","f":"1975","seg":"Mainstream","kf":"pool cues","d":"Wisconsin pool cue maker founded by Jim McDermott.","sig":["McDermott cue"],"s":"https://cbs58.com/news/wisconsin-a-melting-pot-of-pool-cue-makers-like-mcdermott-cue"},
  {"n":"Mezz","c":"Japan","f":"1995","seg":"Premium","kf":"cues, carbon shafts","d":"Cue brand of Miki Company of Tomioka, Gunma; Exceed is its top line.","lines":["Exceed","ACE","AXI","EC","Power Break","Ignite"],"sig":["Mezz cue"],"s":MZ},
  {"n":"Parris Cues","c":"United Kingdom","f":"1984","seg":"Artisan & independent","kf":"snooker cues","d":"John Parris's Forest Hill workshop making snooker cues for professionals.","sig":["Parris snooker cue"],"s":"https://en.wikipedia.org/wiki/Parris_Cues"},
  {"n":"Brunswick Billiards","c":"United States","f":"1845","seg":"Heritage manufactory","kf":"pool tables","d":"Billiard table maker founded by J. M. Brunswick in Cincinnati; sold to KPS Capital Partners in 2019.","sig":["Gold Crown"],"rel":["Olhausen Billiards"],"s":"https://en.wikipedia.org/wiki/Brunswick_Corporation"},
  {"n":"E.J. Riley","c":"United Kingdom","f":"1878","seg":"Heritage manufactory","kf":"snooker tables","d":"Accrington billiard and snooker table maker; the original firm collapsed in 2002 but the name lives on.","sig":["Riley snooker table"],"s":"https://snookerheritage.co.uk/company-histories/ej-riley/"},
  {"n":"Olhausen Billiards","c":"United States","f":"1972","seg":"Mainstream","kf":"pool tables","d":"Pool table maker founded by brothers Butch and Don Olhausen, now in Portland, Tennessee.","lines":["Traditional","Modern","Rustic","Tournament"],"rel":["Brunswick Billiards"],"s":"https://www.olhausenbilliards.com/olhausen-story"}],
 "traditions":[],
 "notes":"All three old kinds kept; Darts and Cue case added. Dartboard: archetypes Nodor Original Bristle, Winmau Blade, Unicorn Eclipse (old Eclipse Pro 2 became a version). Darts: Silver Comet, Phil Taylor Power 9Five, Unicorn Wraith. Pool cue: Balabushka, Predator 314/BK/Air, McDermott, Mezz, Parris; GB23 and G206 became versions; 'Sneaky Pete' (no maker) became a type. Pool table: Gold Crown (I–VII; old Gold Crown VI now a version) and Riley snooker table; other old models kept. Not added for lack of a retrieved source: Meucci and Peradon as archetypes (Grace's Guide 503, Snooker Heritage Peradon page empty), Diamond Billiards, Red Dragon signature lines (no page naming them), Riley cues."})
