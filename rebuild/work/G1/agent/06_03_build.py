import json, os
WP='https://en.wikipedia.org/wiki/'
BW=WP+'Boston_Whaler'; GW='https://www.gradywhite.com/our-legacy/'; SK='https://boatingindustry.com/news/2022/07/28/skeeter-boats-celebrates-75-years/'
RG=WP+'Ranger_Boats'; HW='https://anglersjournal.com/boats-gear/new-boat-report-hewes-redfisher-21/'
B31='https://soundingsonline.com/features/the-legend-of-the-bertram-31/'; B31b='https://soundingsonline.com/boats/bertram-31/'
HT='https://www.hatterasyachts.com/our-story'; YM='https://www.yachtingmagazine.com/history-sportfishing-boats'
LU='https://boatingindustry.com/?p=11107'
kinds=[
{"n":"Centre console boat","a":"center console · CC","d":"Open single-deck powerboat with the helm on a console in the middle of the deck, usually outboard-powered.",
 "t":["inshore","offshore","bow cuddy cabin","single outboard","multiple outboards"],"s":WP+"Center_console_boat",
 "x":[
  {"n":"Boston Whaler Montauk","a":"Montauk","d":"Small foam-filled 'unsinkable' open centre-console boat; the classic 16 ft 7 in hull was a best seller into the late 1980s.","mk":"Boston Whaler","y":"classic hull to late 1980s; current range","s":BW,
   "v":[{"n":"classic 16 ft 7 in Montauk","mk":"Boston Whaler","y":"to late 1980s","d":"among the best-selling Whaler models"},
        {"n":"current Montauk range","mk":"Boston Whaler","y":"current","d":"15.4, 17.3, 19.3 and 21.3 ft; 40–200 hp outboards"}],
   "dt":"length 15–21 ft · outboard power · foam-cored hull"},
  {"n":"Boston Whaler Outrage","a":"Outrage","d":"Boston Whaler's offshore centre-console line built on the foam-filled hull principle.","mk":"Boston Whaler","y":"","s":BW,"v":[],"dt":"length 18.8–42.5 ft · single to multiple outboards"},
  {"n":"Grady-White Fisherman","a":"Fisherman series","d":"Grady-White's centre-console line on the SeaV2 hull, among the first with integrated boarding platforms.","mk":"Grady-White","y":"","s":GW,
   "v":[{"n":"Fisherman 216","mk":"Grady-White","y":"","d":"integrated boarding platform"},{"n":"Fisherman 236","mk":"Grady-White","y":"","d":"integrated boarding platform"}],"dt":"length · outboard power · SeaV2 hull"},
  {"n":"Grady-White Canyon","a":"Canyon series","d":"Grady-White's larger offshore centre-console line.","mk":"Grady-White","y":"","s":GW,
   "v":[{"n":"Canyon 326","mk":"Grady-White","y":"early 2020s","d":""},{"n":"Canyon 456","mk":"Grady-White","y":"","d":"largest Grady-White built"}],"dt":"length · twin to quad outboards"}]},
{"n":"Bass boat","a":"","d":"Low, flat-decked freshwater fishing boat with raised casting decks, livewells, a high-power outboard and a bow trolling motor.",
 "t":["fibreglass","aluminium","single console","dual console"],"s":"https://aceboater.com/boat-types",
 "x":[
  {"n":"Skeeter bass boat","a":"Skeeter","d":"The originating bass boat: Holmes Thurmond's 1948 Skeeter, called the first boat designed for bass fishing, later built in fibreglass.","mk":"Skeeter","y":"1948","s":SK,
   "v":[{"n":"original Skeeter","mk":"Skeeter","y":"1948","d":"Holmes Thurmond's first boat built for bass fishing"},
        {"n":"first fibreglass bass boat","mk":"Skeeter","y":"1961","d":"per Wikipedia (company material says 1950s)"},
        {"n":"FX series","mk":"Skeeter","y":"","d":""},{"n":"ZX series","mk":"Skeeter","y":"","d":""},{"n":"iClass","mk":"Skeeter","y":"","d":""},
        {"n":"FXR APEX","mk":"Skeeter","y":"2022","d":"75th-anniversary limited edition in gold and black"}],"dt":"length · outboard horsepower · single or dual console · colourway"},
  {"n":"Ranger bass boat","a":"Ranger","d":"Fibreglass bass boats from Forrest L. Wood's Flippin, Arkansas company, one of the best-known names in tournament fishing.","mk":"Ranger Boats","y":"1968","s":RG,"v":[],"dt":"length · outboard horsepower · console layout"}],
 "m":[["Stratos 285 Pro Elite","Stratos"]]},
{"n":"Flats boat","a":"flats skiff · poling skiff","d":"Shallow-draft open saltwater fishing boat with a poling or casting platform, made for tidal flats.",
 "t":["poling skiff","technical poling skiff","bay boat (deeper, larger hybrid)"],"s":"https://boatzon.com/boat-types/flats-boats",
 "x":[
  {"n":"Hewes Redfisher","a":"Hewes flats boat","d":"Flats skiff line from the Hewes name; Bob Hewes developed the modern flats skiff in the 1950s, and Maverick Boat Co. has built Hewes since 1989.","mk":"Hewes","y":"1950s (Hewes skiffs)","s":HW,
   "v":[{"n":"Redfisher 16","mk":"Hewes","y":"","d":"well-regarded earlier model"},
        {"n":"Redfisher 21","mk":"Hewes","y":"","d":"new design; 21 ft 6 in, 8 ft 6 in beam, 14 in draft"}],"dt":"length · draft · poling platform · outboard power"}]},
{"n":"Sport-fishing boat","a":"sportfisherman · sportfisher · convertible","d":"Powerboat made for offshore big-game fishing, with a working cockpit, outriggers and often a flybridge or tower.",
 "t":["convertible (flybridge)","express","open/walkaround","custom (cold-moulded)","production (fibreglass)"],"s":"https://yachtway.com/vessel-types/",
 "x":[
  {"n":"Rybovich sportfisherman","a":"Rybovich","d":"Custom tournament sportfishermen from the Rybovich yard in Florida, which set the pattern of the purpose-built offshore fishing boat.","mk":"Rybovich","y":"","s":YM,
   "v":[{"n":"Miss Chevy II","mk":"Rybovich","y":"","d":"34 ft, built for the Cat Cay Tuna Tournament"},{"n":"hull no. 13 Bimini Babe","mk":"Rybovich","y":"1960","d":"Sports Afield cover, February 1960"}],"dt":"custom build · length · teak and mahogany joinery"},
  {"n":"Bertram 31","a":"Bertram 31","d":"Fibreglass deep-V sportfisher with Ray Hunt's 24-degree constant-deadrise hull, launched after a record 1960 Miami–Nassau race win.","mk":"Bertram","y":"1961","s":B31b,
   "v":[{"n":"Hunt prototype","mk":"Bertram","y":"1960","d":"won the Miami–Nassau race"},
        {"n":"Sport Fisherman","mk":"Bertram","y":"1961–1983","d":"lower station and open wheelhouse"},
        {"n":"Flybridge Cruiser","mk":"Bertram","y":"","d":"rear bulkhead"},{"n":"Hardtop Cruiser","mk":"Bertram","y":"","d":""},{"n":"Express Cruiser","mk":"Bertram","y":"","d":"open"}],
   "dt":"layout · engines · restoration state; 1,860 built 1961–1983"},
  {"n":"Hatteras convertible","a":"Hatteras 41 · Knit Wits","d":"Willis Slane's 41 ft convertible sportfisherman, the first fibreglass boat over 40 ft, and the Hatteras sportfish line that followed.","mk":"Hatteras","y":"1959","s":HT,
   "v":[{"n":"Knit Wits (41 ft)","mk":"Hatteras","y":"1959","d":"first fibreglass boat over 40 ft"},{"n":"48 sportfish","mk":"Hatteras","y":"","d":""},{"n":"77 sportfish","mk":"Hatteras","y":"","d":""}],
   "dt":"length · enclosed or open bridge · engines"},
  {"n":"Merritt sportfisherman","a":"Merritt","d":"Custom sportfishermen built by Allen and Buddy Merritt in Pompano Beach since 1955.","mk":"Merritt","y":"1955","s":YM,
   "v":[{"n":"Merritt 42","mk":"Merritt","y":"","d":"e.g. Caliban"},{"n":"Tuna Teaser (37 ft)","mk":"Merritt","y":"","d":""},{"n":"72 ft Merritt","mk":"Merritt","y":"","d":""}],"dt":"custom build · length"},
  {"n":"Whiticar sportfisherman","a":"Whiticar","d":"Custom sportfishermen from Curt Whiticar, who built about 60 boats.","mk":"Whiticar","y":"1937","s":YM,
   "v":[{"n":"Shearwater (33 ft)","mk":"Whiticar","y":"1937","d":"built for himself; seventh hull"},{"n":"Gannet II","mk":"Whiticar","y":"","d":""}],"dt":"cold-moulded hull · cored fibreglass superstructure"}]},
{"n":"Jon boat","a":"johnboat · john boat","d":"Flat-bottomed open boat with bench seats and an outboard transom, for shallow calm water.",
 "t":["aluminium","fibreglass","wood","polyethylene","8–24 ft"],"s":WP+"Jon_boat"}]
brands=[
{"n":"Boston Whaler","c":"United States","f":"1958","seg":"fishing and leisure boats","d":"Maker of foam-filled 'unsinkable' outboard boats, founded by Richard Fisher; part of Brunswick.","lines":["Montauk","Outrage","Dauntless"],"eras":[],"sig":["Boston Whaler Montauk"],"sc":[],"rel":[],"s":BW},
{"n":"Grady-White","c":"United States","f":"1959","seg":"saltwater fishing boats","d":"Greenville, North Carolina builder of outboard fishing boats, owned by Eddie Smith since 1968.","lines":["Fisherman","Canyon","Freedom","Express","Coastal Explorer"],"eras":[],"sig":["Grady-White Fisherman"],"sc":[],"rel":[],"s":GW},
{"n":"Skeeter","c":"United States","f":"1948","seg":"bass and freshwater fishing boats","d":"Bass-boat pioneer founded by Holmes Thurmond; owned by Yamaha since 1996.","lines":["FX","ZX","iClass","WX","MX","SX"],"eras":[],"sig":["Skeeter bass boat"],"sc":[],"rel":[],"s":SK},
{"n":"Ranger Boats","c":"United States","f":"1968","seg":"bass and freshwater fishing boats","d":"Flippin, Arkansas bass-boat maker founded by Forrest L. Wood; part of Bass Pro Group since 2014.","lines":["Fisherman Series"],"eras":[],"sig":["Ranger bass boat"],"sc":[],"rel":["Stratos"],"s":RG},
{"n":"Hewes","c":"United States","f":"","seg":"flats boats","d":"Flats-skiff name from Bob Hewes of Miami; built by Maverick Boat Co. since 1989.","lines":["Redfisher"],"eras":[],"sig":["Hewes Redfisher"],"sc":[],"rel":[],"s":HW},
{"n":"Bertram","c":"United States","f":"1961","seg":"sportfishing yachts","d":"Miami builder founded by Dick Bertram on the Ray Hunt deep-V Bertram 31.","lines":[],"eras":[],"sig":["Bertram 31"],"sc":[],"rel":[],"s":B31},
{"n":"Hatteras","c":"United States","f":"1959","seg":"sportfishing and motor yachts","d":"North Carolina yacht builder founded by Willis Slane; owned by White River Marine Group since 2021.","lines":["Legacy GT"],"eras":[],"sig":["Hatteras convertible"],"sc":[],"rel":[],"s":HT},
{"n":"Rybovich","c":"United States","f":"","seg":"custom sportfishing boats","d":"Florida custom yard that shaped the purpose-built tournament sportfisherman.","lines":[],"eras":[],"sig":["Rybovich sportfisherman"],"sc":[],"rel":["Merritt"],"s":YM},
{"n":"Merritt","c":"United States","f":"1955","seg":"custom sportfishing boats","d":"Pompano Beach custom builder started by Allen and Buddy Merritt.","lines":[],"eras":[],"sig":["Merritt sportfisherman"],"sc":[],"rel":["Rybovich"],"s":YM},
{"n":"Whiticar","c":"United States","f":"","seg":"custom sportfishing boats","d":"Custom sportfisherman builder founded by Curt Whiticar.","lines":[],"eras":[],"sig":["Whiticar sportfisherman"],"sc":[],"rel":[],"s":YM},
{"n":"Lund","c":"United States","f":"1948","seg":"aluminium fishing boats","d":"New York Mills, Minnesota maker of aluminium fishing boats founded by G. Howard Lund.","lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":LU}]
notes=("All five planned kinds kept (k105–k109). Archetypes from retrieved pages: Montauk/Outrage (Wikipedia Boston Whaler), Grady-White Fisherman/Canyon (gradywhite.com), Skeeter and Ranger bass boats, Hewes Redfisher, Rybovich, Bertram 31, Hatteras convertible, Merritt, Whiticar (Soundings, Yachting, Hatteras site). "
 "Left out: Lund aluminium archetype (no retrieved page named a Lund model; lundboats.com blocked) - Lund kept as a brand only; consider a new 'Deep-V aluminium fishing boat' kind if sourced. Jon boat has no archetypes (maker-free pattern; no makers named in the retrieved page). "
 "Montauk introduction year and Bertram/Hatteras model years beyond those listed not confirmed, so left blank. Hewes 'Bonefisher' name and Bertram 'Moppie' only from search snippets, omitted. Viking, Tracker, Nitro, Triton etc. not added as archetypes (no retrieved model details). Stratos 285 Pro Elite kept in m from Wikipedia Bass boat page (Stratos not in register).")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/G1/shelves/06_03.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
