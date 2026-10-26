import json, os
W = "https://en.wikipedia.org/wiki/"
FB = "https://favourbrook.com/collections/double-breasted-waistcoats?page=1"
def X(n,a,d,mk,y,s,v,dt): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}

suit = {"n":"Business suit","a":"suit · lounge suit · two-piece · three-piece · skirt suit · trouser suit",
 "d":"Tailored jacket with matching trousers or skirt, sometimes with a waistcoat, for business and formal day wear.",
 "t":["single-breasted","double-breasted","two-piece","three-piece (with waistcoat)","skirt suit","trouser suit (pantsuit)","bespoke","made-to-measure","ready-to-wear","suit separates"],
 "s":W+"Suit",
 "x":[
  X("Savile Row structured cut","English cut · Savile Row suit","Close-fitting London bespoke cut with high armholes, built-up canvassed shoulders and a suppressed waist.","","19th century–present",W+"Savile_Row_tailoring",
    [("Henry Poole & Co","Henry Poole & Co","1806","Founded by James Poole; at 15 Savile Row from 1846."),
     ("Huntsman one-button coat","H. Huntsman & Sons","1960s–1980s","Slim one-button coat with a long waist and flared skirt; refined under head cutter Colin Hammick."),
     ("Kilgour built-up shoulder","Kilgour","20th century","Heavily canvassed, built-up shoulders and V-shaped torso."),
     ("Gieves & Hawkes military-rooted cut","Gieves & Hawkes","1771 roots","No. 1 Savile Row house built on Army and Royal Navy tailoring.")],
    "single or double-breasted · cloth weight and pattern · bespoke or ready-to-wear"),
  X("English drape suit","drape cut · London cut · blade cut","Roomy cut with extra cloth over the shoulder blades and chest, light padding and full sleeves, forming soft drapes.","Anderson & Sheppard","late 1920s–1930s",W+"Drape_suit",
    [("Scholte drape","","1930s","Developed by London tailor Frederick Scholte; worn by Edward VIII, which spread it to America."),
     ("Anderson & Sheppard London cut","Anderson & Sheppard","from 1906 house","Peter Gustav Anderson's development of Scholte's soft style: high small armhole, generous upper sleeve."),
     ("American drape","","1930s","Smooth sleeve-head and more tapered waist than the British version."),
     ("Bold Look","","1950s","Post-war evolution of the drape, often double-breasted.")],
    "single or double-breasted · pleated wide trousers · peak or notch lapel"),
  X("Sack suit","Ivy League suit · natural-shoulder suit · No. 1 sack","Undarted, boxy American jacket, typically three-roll-two with a hooked vent, worn with plain belted trousers.","Brooks Brothers","1895",W+"Sack_suit",
    [("Brooks Brothers No. 1 Sack Suit","Brooks Brothers","1895","The original American sack suit."),
     ("J. Press Newport Model suit","J. Press","","Three-button sack cut from the New Haven Ivy outfitter."),
     ("Ivy League mainstream","","1950s","About 70% of suits sold in 1957–58 were in the Ivy style.")],
    "3/2 roll or two-button · natural shoulder · hooked vent · flannel, tweed, poplin"),
  X("Neapolitan soft suit","Neapolitan jacket · giacca napoletana","Light, unpadded Naples jacket with spalla camicia shoulder, barchetta breast pocket, patch pockets and minimal lining.","","1920s",W+"Neapolitan_tailoring",
    [("Rubinacci London House jacket","Rubinacci","1932","Gennaro Rubinacci's loose jackets without structure or lining."),
     ("Cesare Attolini","Cesare Attolini","1930","House founded by Vincenzo Attolini, credited with the Neapolitan silhouette."),
     ("Kiton","Kiton","1968","Ciro Paone's Naples house; hand-cut and basted suits."),
     ("Isaia","","","Neapolitan ready-to-wear tailoring house.")],
    "spalla camicia or roped shoulder · unlined or half-lined · deep side vents"),
  X("Bar suit","Bar jacket · New Look suit","Nipped-waist, padded-hip jacket over a full mid-calf skirt; the emblem of the New Look.","Dior","1947",W+"Dior",
    [("Original Bar suit","Dior","1947","First collection, 12 February 1947, Spring–Summer; Pierre Cardin of the tailoring atelier contributed.")],
    "jacket in shantung or wool · pleated full skirt · reinterpretations by later Dior creative directors"),
  X("Chanel suit","Chanel jacket · cardigan suit","Collarless cardigan-style jacket with trim and gold buttons over a knee-length skirt, often weighted with a hem chain.","Chanel","by 1953",W+"Chanel_suit",
    [("1960s Chanel suit","Chanel","1965","Woollen suit with chain sewn in to weigh the hem."),
     ("Lagerfeld-era suit","Chanel","1983–2019","Tweed, gold accents and chains reworked under Karl Lagerfeld.")],
    "tweed or knitted wool · braid trim · gold buttons · chain hem"),
  X("Armani deconstructed suit","unstructured suit · soft suit","Minimally padded, softly constructed jacket and suit in fluid cloth that redefined 1980s tailoring.","Giorgio Armani","from 1975",W+"Giorgio_Armani",
    [("American Gigolo wardrobe","Giorgio Armani","1980","Armani costumes for Richard Gere's character Julian Kaye.")],
    "soft shoulder · fluid wools and blends · neutral colours"),
  X("Mod mohair suit","mod suit · sharkskin suit","Slim-fitting mohair or sharkskin suit from 1960s London and Milan, adopted by the mods.","","1960s",W+"Suit",
    [],"mohair, sharkskin · narrow lapels · slim trousers"),
  X("Women's trouser suit","pantsuit · trouser suit","Woman's suit of trousers with a matching jacket, widespread from the 1960s.","","1960s",W+"Pantsuit",
    [("Ossie Clark trouser suit","","1964","Offered in London two years before Saint Laurent's design."),
     ("Le Smoking","Yves Saint Laurent","1966","Evening trouser suit based on the tuxedo (see Tuxedo).")],
    "single or double-breasted · day or evening · matching or coordinating jacket")],
 "m":[["Plume","Brioni"],["Abito #1","Zegna"],["Leader","Corneliani"],["Ludlow suit","J.Crew"],["Crosby suit","J.Crew"]],
 "r":[["Brunico","Brioni"],["Lipari","Brioni"]]}

blazer = {"n":"Blazer","a":"sport coat · sports jacket · club blazer",
 "d":"Tailored jacket worn without matching trousers, from navy and club blazers to tweed sport coats.",
 "t":["single-breasted","double-breasted","navy","striped","patch pockets","metal buttons","tweed","hopsack","linen","corduroy"],
 "s":W+"Blazer",
 "x":[
  X("Boating & club blazer","rowing blazer · cricket blazer · college blazer","Brightly coloured or striped jacket with a club or college badge, from rowing and cricket clubs.","","1825 onwards",W+"Blazer",
    [("Lady Margaret Boat Club jacket","","19th century","Red flannel boating jacket of St John's College, Cambridge; the original 'blazer'."),
     ("Rowing Blazers club blazer","Rowing Blazers","2017","Blazers made for rowing clubs, college crews and societies."),
     ("Merc boating blazer","Merc London","","Striped boating blazer.")],
    "stripe colours · piping · badge · flannel"),
  X("Navy double-breasted blazer","reefer · nautical blazer","Double-breasted navy jacket with naval-style gold metal buttons, a classic since the 1930s.","","1930s",W+"Blazer",
    [("Reefer jacket","","19th century","Short double-breasted naval jacket whose descendants are called blazers.")],
    "six- or four-button · gold or silver buttons · serge, hopsack, flannel"),
  X("Ivy sack blazer","sack sport coat · Ivy blazer","Undarted natural-shoulder blazer or sport coat on the American sack pattern.","Brooks Brothers","1895 pattern",W+"Sack_suit",
    [("No. 1 Sack Sport Coat","Brooks Brothers","",""),
     ("Ivy Model sport coat and blazer","J. Press","","Three-button sack cut.")],
    "3/2 roll · hooked vent · navy, tweed, madras"),
  X("School blazer","uniform blazer","Usually single-breasted blazer in school colours, often piped and badged.","","20th century",W+"Blazer",
    [],"colour · piping · crest"),
  X("Tweed sport coat & hacking jacket","sports jacket · hacking jacket","Sturdy wool, often tweed, jacket from country sports; the hacking jacket has three buttons and a single vent.","","19th century",W+"Sport_coat",
    [("Hacking jacket","","","Riding sport coat with three buttons and a single vent."),
     ("Donegal tweed sport coat","","","Sport coat in Irish Donegal tweed.")],
    "tweed, flannel, corduroy · slanted pockets · vent")],
 "m":[["Games Blazer","Drake's"],["The Cloud Jacket","Brooks Brothers"],["Kei","Canali"],["Butterfly","Caruso"],["Belgravia Blazer","Jade Holland Cooper"],["Alison Long Blazer","Bouguessa"]]}

waist = {"n":"Waistcoat","a":"vest (US)",
 "d":"Fitted sleeveless tailored garment worn under a jacket or alone.",
 "t":["single-breasted","double-breasted","lapelled","matching (suit)","contrasting (odd)","day","evening"],
 "s":W+"Waistcoat",
 "x":[
  X("Suit waistcoat","three-piece waistcoat","Waistcoat in the same cloth as the jacket and trousers, the third piece of a three-piece suit.","","1666 (Charles II's vest)",W+"Waistcoat",
    [],"single-breasted, bottom button left undone · lapelled or plain"),
  X("Odd waistcoat","fancy waistcoat · contrasting waistcoat","Waistcoat in a contrasting colour or cloth, such as buff or dove grey with day dress.","","17th century–present",W+"Waistcoat",
    [("Double-breasted shawl-lapel waistcoat","Favourbrook","","Wool, linen or velvet; for weddings, Royal Ascot and morning dress.")],
    "colour · silk, linen, wool, velvet · single or double-breasted"),
  X("Evening waistcoat","dress waistcoat · tuxedo waistcoat","Low-cut waistcoat for evening dress: white with white tie, black with black tie.","","19th century",W+"Waistcoat",
    [("Tuxedo waistcoat","","","Black low-cut waistcoat worn instead of a cummerbund with black tie."),
     ("White-tie waistcoat","","","White waistcoat worn with the evening tailcoat.")],
    "low cut · fully buttoned · black or white")]}

tux = {"n":"Tuxedo","a":"dinner jacket · dinner suit · black tie · smoking",
 "d":"Formal evening suit with satin or grosgrain facings, worn with a bow tie.",
 "t":["shawl lapel","peak lapel","notch lapel","single-breasted","double-breasted","black","midnight blue","satin facings","grosgrain facings"],
 "s":W+"Tuxedo",
 "x":[
  X("Dinner jacket","DJ · tuxedo jacket","Tailless evening jacket with silk-faced lapels, worn with a low-cut waistcoat or a cummerbund.","Henry Poole & Co","1860s",W+"Henry_Poole_%26_Co",
    [("Prince of Wales smoking jacket","Henry Poole & Co","1860s","Short evening jacket made for the future Edward VII."),
     ("Tuxedo Park tailless dress coat","","1886","Worn at the Tuxedo Club ball, giving the American name."),
     ("Midnight blue dinner suit","","mid-1930s","Rivalled black by the mid-1930s; revived in the 21st century.")],
    "shawl or peak lapel · one button · satin or grosgrain · black or midnight blue"),
  X("Double-breasted dinner jacket","DB dinner jacket","Double-breasted evening jacket, worn without waistcoat or cummerbund.","","20th century",W+"Tuxedo",
    [],"peak or shawl lapel · button arrangement"),
  X("White dinner jacket","ivory dinner jacket · tropical dinner jacket","Ivory warm-weather dinner jacket with self-faced lapels, worn with black trousers.","","20th century",W+"Tuxedo",
    [],"ivory · self-faced shawl or peak lapel"),
  X("Le Smoking","women's tuxedo","Women's tuxedo suit with narrowed waist and leg-lengthening trousers.","Yves Saint Laurent","1966",W+"Le_Smoking",
    [("Original Le Smoking","Yves Saint Laurent","1966","Saint Laurent's first evening trouser suit for women.")],
    "jacket and trousers · blouse · satin facings")],
 "m":[]}
del tux["m"]

morning = {"n":"Morning dress & tailcoat","a":"morning suit · morning coat · tails · white tie · formal day dress",
 "d":"Tailcoats for the most formal dress codes: the cutaway morning coat by day and the evening tailcoat for white tie.",
 "t":["black","Oxford grey","morning grey","striped (cashmere) trousers","check trousers","contrasting waistcoat","bought or hired"],
 "s":W+"Morning_dress",
 "x":[
  X("Morning coat","cutaway · morning suit","Single-breasted cutaway day coat with curved fronts sloping into knee-length tails, worn with striped trousers.","","19th century",W+"Morning_dress",
    [("Black morning coat","","Edwardian era","Black or Oxford grey herringbone coat with striped trousers; replaced the frock coat as day full dress."),
     ("Morning grey","","","All-grey morning suit traditional at Royal Ascot and weddings.")],
    "black or grey · peak lapel · one button or link · waistcoat colour"),
  X("Evening tailcoat","dress coat · tails · swallowtail · white-tie coat","Waist-length evening coat squarely cut away at the front with knee-length tails, worn for white tie.","","late 1790s; evening-only by 1850s",W+"Tailcoat",
    [("White-tie ensemble","","","With wing-collar shirt, white bow tie and waistcoat, and braided black trousers.")],
    "black · silk-faced peak lapel · braided trousers")]}

def B(n,c,f,seg,d,lines,eras,sig,s,rel=()): return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":list(lines),"eras":list(eras),"sig":list(sig),"sc":[],"rel":list(rel),"s":s}
brands=[
 B("Brooks Brothers","United States","1818","American heritage clothier","New York clothier credited with the American sack suit and the button-down collar.",["Golden Fleece","Black Fleece (2007–2015)"],["Brooks family, to 1946","Marks & Spencer, 1988–2001","Retail Brand Alliance, 2001–2020","Authentic Brands Group & Simon Property Group, 2020–","Catalyst Brands, 2025–"],["Sack suit","Ivy sack blazer"],W+"Brooks_Brothers",["J. Press"]),
 B("J. Press","United States","1902","Ivy League clothier","New Haven clothier founded on the Yale campus, known for three-button sack jackets.",[],["Onward Kashiyama owner, 1986–"],["Sack suit","Ivy sack blazer"],W+"J._Press",["Brooks Brothers","Rowing Blazers"]),
 B("Henry Poole & Co","United Kingdom","1806","Savile Row bespoke tailor","Savile Row tailor credited with the first dinner jacket for the Prince of Wales.",[],[],["Dinner jacket","Savile Row structured cut"],W+"Henry_Poole_%26_Co"),
 B("H. Huntsman & Sons","United Kingdom","1849","Savile Row bespoke tailor","Savile Row tailor of riding origins known for its one-button coat.",[],["Colin Hammick, head cutter"],["Savile Row structured cut"],W+"H._Huntsman_%26_Sons"),
 B("Anderson & Sheppard","United Kingdom","1906","Savile Row bespoke tailor","Savile Row tailor associated with the soft English drape cut.",[],["Anda Rowland owner, 2004–"],["English drape suit"],W+"Anderson_%26_Sheppard"),
 B("Gieves & Hawkes","United Kingdom","1771","Savile Row tailor","No. 1 Savile Row tailor rooted in Army and Royal Navy uniform tailoring.",["bespoke","ready-to-wear"],["Frasers Group owner, 2022–"],["Savile Row structured cut"],W+"Gieves_%26_Hawkes"),
 B("Rubinacci","Italy","1932","Neapolitan bespoke tailor","Naples tailor, founded as London House by Gennaro Rubinacci, pioneer of the unlined soft jacket.",[],["Mariano Rubinacci, from 1961"],["Neapolitan soft suit"],W+"Rubinacci"),
 B("Cesare Attolini","Italy","1930","Neapolitan tailoring","Naples house founded by Vincenzo Attolini, credited with the Neapolitan silhouette.",[],[],["Neapolitan soft suit"],W+"Cesare_Attolini"),
 B("Kiton","Italy","1968","Neapolitan luxury tailoring","Naples-area luxury menswear house founded by Ciro Paone, known for hand-made suits.",[],[],["Neapolitan soft suit"],W+"Kiton"),
 B("Dior","France","1946","Haute couture house","Paris couture house whose 1947 New Look introduced the Bar suit.",[],["Christian Dior, 1947–1957","Yves Saint Laurent, 1957–1960","Marc Bohan, 1960–1989","Gianfranco Ferré, 1989–1997","John Galliano, 1997–2011","Raf Simons, 2012–2015","Maria Grazia Chiuri, 2016–2025","Jonathan Anderson, 2025–"],["Bar suit"],W+"Dior"),
 B("Chanel","France","1910","Haute couture house","Paris house founded by Coco Chanel, known for the tweed cardigan-jacket suit.",[],["Coco Chanel","Karl Lagerfeld, 1983–2019","Virginie Viard, 2019–2024","Matthieu Blazy, 2024–"],["Chanel suit"],W+"Chanel"),
 B("Giorgio Armani","Italy","1975","Luxury fashion house","Milan house known for soft, deconstructed tailoring.",["Giorgio Armani","Emporio Armani","AX Armani Exchange","Armani Junior"],["Giorgio Armani and Sergio Galeotti, founders"],["Armani deconstructed suit"],W+"Giorgio_Armani"),
 B("Zegna","Italy","1910","Luxury menswear and cloth mill","Trivero cloth mill turned luxury menswear house, renamed ZEGNA in 2021.",["ZEGNA","Thom Browne (owned)","Tom Ford Fashion (licence)"],["Alessandro Sartori, artistic director, 2016–"],[],W+"Zegna"),
 B("Brioni","Italy","1945","Roman luxury tailoring","Rome tailoring house known for James Bond suits from GoldenEye (1995).",[],["Brendan Mullane, 2013–2016","Norbert Stumpfl, 2018–2025","Kering owner, 2011–"],[],W+"Brioni_(brand)"),
 B("Canali","Italy","1934","Men's tailoring","Sovico men's tailoring firm founded by the Canali brothers.",[],[],[],W+"Canali"),
 B("Corneliani","Italy","1930","Men's tailoring","Mantua menswear maker best known for suits and sport coats.",[],[],[],W+"Corneliani"),
 B("Yves Saint Laurent","France","1961","Haute couture house","Paris house of Yves Saint Laurent and Pierre Bergé, originator of Le Smoking; ready-to-wear renamed Saint Laurent in 2012.",["Saint Laurent"],["Yves Saint Laurent","Tom Ford, 2000–2004","Stefano Pilati, 2004–2012","Hedi Slimane, 2012–2016","Anthony Vaccarello, 2016–"],["Le Smoking"],W+"Yves_Saint_Laurent_(fashion_house)"),
 B("Drake's","United Kingdom","1977","London haberdasher","London tie maker and haberdasher that also makes tailoring such as its Games blazers.",[],["Michael Drake, founder","Michael Hill, creative director"],[],W+"Drake%27s_(haberdashers)"),
 B("Rowing Blazers","United States","2017","Club and preppy clothing","New York brand founded by Jack Carlson making blazers for rowing clubs and colleges.",[],[],["Boating & club blazer"],W+"Rowing_Blazers",["J. Press"]),
 B("J.Crew","United States","1947","Mainstream specialty retailer","American retailer whose suiting covers the mainstream market.",[],[],[],W+"J.Crew"),
 B("Moss Bros","United Kingdom","1851","Formalwear retail and hire","London menswear chain specialising in formal dresswear, with a hire department since 1897.",[],[],[],W+"Moss_Bros_Group"),
 B("Ede & Ravenscroft","United Kingdom","1689","Robemaker and ceremonial dress","London robemaker for legal, academic and ceremonial dress, also hiring it out.",[],[],[],W+"Ede_%26_Ravenscroft"),
 B("Favourbrook","United Kingdom","","Formalwear and waistcoats","London formalwear house known for waistcoats for weddings, Royal Ascot and morning dress.",[],[],["Odd waistcoat"],FB),
]
trads=[
 {"n":"Savile Row bespoke tailoring","g":"Textiles & tailoring","r":"London, England","p":"early 19th century–present",
  "d":"Bespoke men's tailoring centred on Savile Row in Mayfair, the reference for the structured English suit.",
  "tech":"Pattern drafted for each customer, cut and fitted by hand; canvassed, built-up construction or the softer drape cut.",
  "mat":"wool and other suit cloths, canvas interlinings","forms":["Business suit","Tuxedo","Morning dress & tailcoat","Blazer"],
  "ctr":["Henry Poole & Co","H. Huntsman & Sons","Anderson & Sheppard","Gieves & Hawkes","Kilgour","Norton & Sons","Dege & Skinner"],
  "auth":"True bespoke is cut from the customer's own pattern, unlike made-to-measure (adjusted stock pattern) or ready-to-wear.",
  "s":W+"Savile_Row_tailoring"},
 {"n":"Neapolitan tailoring","g":"Textiles & tailoring","r":"Naples, Italy","p":"late 19th century–present; soft jacket from the 1920s",
  "d":"Soft, light Naples tailoring developed as an alternative to Savile Row structure.",
  "tech":"Unpadded shoulder, often spalla camicia; minimal or no lining; heavy hand work.",
  "mat":"light wools, linen, cotton","forms":["Business suit","Blazer"],
  "ctr":["Rubinacci","Cesare Attolini","Kiton","Isaia","Pino Peluso","Panico","Zizolfi","Manna","Orazio Luciano"],
  "auth":"Spalla camicia shoulder, barchetta breast pocket, curved patch pockets, short sleeves and deep side vents.",
  "s":W+"Neapolitan_tailoring"}]

notes=("Moved out of this shelf (planned elsewhere in A1): Zhongshan suit and Traje de charro -> Traditional dress (Zhongshan suit, Charro suit); "
 "Bandhgala -> Traditional (Bandhgala & Nehru jacket); Nehru jacket and Qurte (waistcoat models) -> Traditional. "
 "Zoot suit and Teddy Boy drape suit dropped as models: they are subculture styles for the scene register, not suit archetypes. "
 "Dropped as noise: Greiff ranges (Casual/Modern/Premium), Bouguessa line names, Arwa The Brand blazer SKUs. "
 "Not confirmed and left out: Chanel suit 1954 date (cited as 'by 1953' from the fetched page), a dated origin for Armani's unstructured jacket, "
 "Brooks Brothers 1901 sack date (page gives 1895). Drake's Games Blazer kept only as a model (no page retrieved for it). "
 "Moss Bros (hire since 1897) and Ede & Ravenscroft added to the brand register as formalwear hire and ceremonial-dress houses; "
 "Favourbrook founding year unknown. Kilgour, Isaia appear as version makers without register entries.")
out={"kinds":[suit,blazer,waist,tux,morning],"brands":brands,"traditions":trads,"notes":notes}
p="/home/user/Possession-Taxonomy/rebuild/work/A1/shelves/04_00.json"
open(p+".tmp","w").write(json.dumps(out,ensure_ascii=False,indent=1)); os.replace(p+".tmp",p); print("written")
