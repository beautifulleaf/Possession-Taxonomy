import json, os
W="https://en.wikipedia.org/wiki/"
WB=W+"Farrow_%26_Ball"
kinds=[
{"n":"Wall and ceiling paint","a":"emulsion · interior wall paint","d":"Interior paint for walls and ceilings, usually water-based emulsion.",
 "t":["matt","flat or dead flat","silk","soft sheen","eggshell","washable or scrubbable","contract or trade matt"],
 "m":[["Modern Emulsion","Farrow & Ball"],["Intelligent Matt Emulsion","Little Greene"],["Dynasty","Behr"],["Ultra","Behr"],["Marquee","Behr"],["Reserve","Valspar"],["Signature","Valspar"],["Aura","Benjamin Moore"],["Regal","Benjamin Moore"],["ben","Benjamin Moore"],["HGTV Home Infinity","Sherwin-Williams"],["Easycare Washable & Tough Matt","Dulux"],["Easyclean Matt","Crown"],["Clark+Kensington","Clark+Kensington"]],
 "s":"https://www.toolstation.com/painting-decorating/c8"},
{"n":"Woodwork and metal paint","a":"trim paint · gloss · satinwood · eggshell","d":"Hard-wearing paint for doors, trim, skirting and metalwork.",
 "t":["gloss","satin or satinwood","eggshell","water-based","solvent-based","direct-to-metal"],
 "m":[["Trade Liquid Gloss","Wickes"]],
 "s":"https://www.wickes.co.uk/Products/Painting+Decorating/Interior-Paint/Interior-Wood-Paint/c/1001117/f/1-l-interior-wood-paint"},
{"n":"Primer and undercoat","a":"primer · undercoat · sealer","d":"Preparatory coat under the top coat to seal, block stains or give adhesion.",
 "t":["primer","undercoat","primer-undercoat","stain-blocking sealer","bonding primer","metal primer"],
 "m":[["B-I-N Primer Sealer","Zinsser"],["Bulls Eye 123 Primer Sealer","Zinsser"],["Cover Stain","Zinsser"],["Gardz Clear Primer","Zinsser"],["Peel Stop","Zinsser"]],
 "s":"https://www.wickes.co.uk/Products/Decorating+Interiors/Paint/Undercoats+Primers/c/1001122"},
{"n":"Masonry paint","a":"exterior wall paint","d":"Exterior paint for brick, render and masonry walls.",
 "t":["smooth","textured","water-based","solvent-based"],
 "m":[["Weathershield Smooth Masonry","Dulux"],["Microseal Smooth Masonry","Sandtex"],["Granocryl Smooth Masonry","Leyland"]],
 "s":"https://www.toolstation.com/painting-decorating/c8"},
{"n":"Furniture paint","a":"chalk paint · cabinet paint","d":"Paint made for furniture and cabinets, often ultra-matt and low-preparation.",
 "t":["chalk-style","mineral","cabinet enamel","eggshell"],
 "x":[{"n":"Chalk Paint","a":"chalk paint","d":"Water-based decorative paint with an ultra-matt finish that sticks to most surfaces with little preparation; usually waxed or lacquered.",
       "mk":"Annie Sloan Interiors","y":"1990","s":W+"Chalk_paint",
       "v":[{"n":"Chalk Paint (registered trademark)","mk":"Annie Sloan Interiors","y":"1990","d":"the original, developed by Annie Sloan"}],
       "dt":"finish ultra-matt · sealed with wax or lacquer · distressed or colour-washed"}],
 "s":"https://www.toolstation.com/painting-decorating/c8"},
{"n":"Spray paint","a":"aerosol paint · rattle can","d":"Paint in a pressurised aerosol can, for general touch-up, craft or graffiti use.",
 "t":["general-purpose","graffiti and artist (high or low pressure)","water-based","primer","metallic and chrome effect","textured and stone effect","automotive"],
 "m":[["MTN 94","Montana Colors"],["Hardcore","Montana Colors"],["Water Based 400","Montana Colors"],["Nitro 2G","Montana Colors"],["Montana BLACK","Montana Cans"],["Montana GOLD","Montana Cans"],["Montana BLUE","Montana Cans"]],
 "s":"https://www.toolstation.com/painting-decorating/c8"},
{"n":"Specialist paint","a":"floor paint · radiator paint · tile paint","d":"Paint formulated for a demanding surface: floors, radiators, glazed tiles or damp rooms.",
 "t":["floor and garage floor","radiator (heat-resistant)","tile","anti-mould","kitchen and bathroom"],
 "m":[["Garage Floor","Johnstone's"]],
 "s":"https://www.toolstation.com/painting-decorating/c8"},
]
brands=[
{"n":"Farrow & Ball","c":"United Kingdom","f":"1946","seg":"premium heritage paint and wallpaper","d":"Paint and wallpaper maker founded in Wimborne, Dorset, by chemists John Farrow and Richard Ball; owned by Hempel since 2021.","lines":["paint","block- and trough-printed wallpaper"],"sig":["Modern Emulsion"],"rel":["Little Greene","Crown Paints"],"s":WB},
{"n":"Little Greene","c":"United Kingdom","f":"","seg":"premium heritage paint and wallpaper","d":"Manchester paint and wallpaper maker run by founder David Mottershead's family, with a factory in Wales and a National Trust collaboration.","lines":["paint","wallpaper","National Trust collection"],"sig":["Intelligent Matt Emulsion"],"rel":["Farrow & Ball"],"s":W+"Little_Greene"},
{"n":"Dulux","c":"United Kingdom","f":"1931","seg":"mass-market decorative paint","d":"Paint brand launched by ICI in 1931, now made by AkzoNobel, known for its Old English Sheepdog advertising since 1961.","lines":["Weathershield","Easycare"],"sig":["Weathershield Smooth Masonry"],"rel":["Crown Paints"],"s":W+"Dulux"},
{"n":"Crown Paints","c":"United Kingdom","f":"1850s","seg":"mass-market decorative paint","d":"Darwen, Lancashire paint maker traceable to the late 1850s, formerly Walpamur and Crown Berger; owned by Hempel since 2011.","rel":["Dulux","Farrow & Ball"],"s":W+"Crown_Paints"},
{"n":"Benjamin Moore","c":"United States","f":"1883","seg":"premium decorative paint","d":"Paint maker founded in New York in 1883, based in Montvale, New Jersey, owned by Berkshire Hathaway since 2000.","lines":["Aura","Regal","ben","Fresh Start","Woodluxe"],"sig":["Aura"],"rel":["Sherwin-Williams","Behr"],"s":W+"Benjamin_Moore_%26_Co."},
{"n":"Sherwin-Williams","c":"United States","f":"1866","seg":"paint group","d":"Cleveland paint group founded by Henry Sherwin and Edward Williams, owning Valspar, Krylon, Dutch Boy, Minwax, Cabot, Purdy and Ronseal.","lines":["HGTV Home","Krylon","Dutch Boy","Minwax","Ronseal"],"rel":["Valspar","Benjamin Moore"],"s":W+"Sherwin-Williams"},
{"n":"Valspar","c":"United States","f":"1806","seg":"mass-market decorative paint","d":"Paint company begun as a Boston paint dealership in 1806, based in Minneapolis and owned by Sherwin-Williams since 2017.","lines":["Reserve","Signature"],"rel":["Sherwin-Williams"],"s":W+"Valspar"},
{"n":"Behr","c":"United States","f":"1947","seg":"mass-market decorative paint","d":"Santa Ana paint maker founded by Otho Behr Jr., owned by Masco since 1999 and sold only through The Home Depot.","lines":["Dynasty","Ultra","Marquee","Premium Plus"],"sig":["Dynasty"],"rel":["Valspar","Benjamin Moore"],"s":W+"Behr_Paint"},
{"n":"Rust-Oleum","c":"United States","f":"1921","seg":"protective and specialist coatings","d":"Rust-preventive paint maker founded in Evanston, Illinois, by Robert Fergusson; owned by RPM International since 1994, with Zinsser among its brands.","lines":["Painter's Touch","Zinsser"],"rel":["Zinsser"],"s":W+"Rust-Oleum"},
{"n":"Montana Colors","c":"Spain","f":"1994","seg":"graffiti and artist spray paint","d":"Barcelona spray-paint maker (MTN) founded by Jordi Rubio, making paint mainly for graffiti.","lines":["MTN 94","Hardcore","Water Based 400","Nitro 2G","Mega"],"rel":["Montana Cans"],"s":W+"Montana_Colors"},
{"n":"Montana Cans","c":"Germany","f":"1995","seg":"graffiti and artist spray paint","d":"German graffiti spray-paint brand that began in 1995 after a naming split with Montana Colors.","lines":["Montana BLACK","Montana GOLD","Montana BLUE"],"rel":["Montana Colors"],"s":"https://www.montana-cans.com/"},
{"n":"Annie Sloan Interiors","c":"United Kingdom","f":"1990","seg":"furniture paint","d":"Company of British artist Annie Sloan, inventor of Chalk Paint in 1990, which owns the Chalk Paint trademark.","sig":["Chalk Paint"],"s":W+"Annie_Sloan"},
]
notes=("Merged Floor, Radiator and Tile paint (k157,k160,k161) into Specialist paint with types. Wall paint models are independent test results: "
"Which? Best Buy washable paint (Farrow & Ball Modern Emulsion 2022, Little Greene Intelligent Matt 2022, via brewers.co.uk), Consumer Reports 2026 (Behr Dynasty top, Valspar Reserve 2nd, Behr Ultra Best Buy, via hunker.com) "
"and CR 2013 (Clark+Kensington top), plus market brands from the Which? test field (Dulux, Crown). Masonry models from Expert Reviews. "
"Not added: Stiftung Warentest and CHOICE winners (not retrieved); Which? masonry test (paywalled); Zinsser brand entry (maker page 403); Farrow & Ball Limewash left to the heritage shelf; Krylon has no own page (redirects to Sherwin-Williams).")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p="work/C8/shelves/05_00.json"; t=p+".tmp"
json.dump(out,open(t,"w"),ensure_ascii=False,indent=1); os.replace(t,p)
