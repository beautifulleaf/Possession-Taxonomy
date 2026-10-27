import json, os
def w(code, job, obj):
    p = f'/home/user/Possession-Taxonomy/rebuild/work/{code}/shelves/{job}.json'
    t = p + '.tmp'; json.dump(obj, open(t, 'w'), ensure_ascii=False, indent=1); os.replace(t, p)
def X(n,d,mk,y,s,v=(),dt="",a=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[{"n":a1,"mk":b,"y":c,"d":e} for a1,b,c,e in v],"dt":dt}
MW="https://en.wikipedia.org/wiki/Marker_(ski_bindings)"
K="knowledge"
kinds=[
 {"n":"Alpine ski","a":"downhill ski","d":"Ski made for downhill skiing with a fixed-heel binding; use class, width and turning radius vary.",
  "t":["piste / carving","race (slalom, giant slalom)","all-mountain","freeride","powder","park / twin-tip","women's","junior"],
  "s":"https://www.buckmans.com/products/1000/ski",
  "x":[
   X("Mantra","Völkl's long-running all-mountain charger with Titanal metal, narrowed over its generations.","Völkl","2006","https://skicanadamag.com/volkl-mantra-m5/",
     [("Mantra (M3)","Völkl","",""),("M5 Mantra","Völkl","2018","Titanal Frame; 96 mm waist, from 100 mm"),("M7 Mantra","Völkl","",""),("Mantra 88","Völkl","","")],"waist 96–100 mm · lengths"),
   X("Enforcer","Nordica's twin-titanal freeride ski, called the godfather of modern freeride skis.","Nordica","","https://www.skiessentials.com/2024-ski-test/skis/2024-nordica-enforcer-100",
     [("Enforcer 100","Nordica","2024","132.5/100/120.5 mm, dual titanal")],"waist widths · lengths 165–191 cm"),
   X("QST","Salomon's freeride ski line, now in its third generation.","Salomon","2016","https://steep.jp/en/gear-item/54702",
     [("QST 92","Salomon","",""),("QST 94","Salomon","",""),("QST 98","Salomon","",""),("QST 100","Salomon","",""),("QST 106","Salomon","2022","third generation, 139-106-126 mm"),
      ("QST Blank","Salomon","",""),("QST Stella 106","Salomon","","women's"),("S/LAB QST X","Salomon","","")],"waist 92–112 mm · women's (Stella)"),
   X("Bent Chetler","Fat twin-tip powder ski, the first pro model of Chris Benchetler.","Atomic","2008",
     "https://www.freeskier.com/chris-benchetler-celebrates-10-years-of-the-bent-chetler-with-one-hell-of-an-edit",
     [("Bent Chetler 120","Atomic","2018","HRZN Tech tip and tail"),("Bent Chetler 100","Atomic","2018","100 mm waist")],"waist widths"),
   X("Brahma","Blizzard's powerful two-titanal all-mountain ski for firm snow.","Blizzard","","https://www.skiessentials.com/2024-ski-test/skis/2024-blizzard-brahma-88",
     [("Brahma 88","Blizzard","2024","TrueBlend core, 128/88/110 mm")],"lengths 165–189 cm"),
   X("Mindbender","K2's all-mountain series with Titanal Y-Beam (Ti) models.","K2","","https://www.skiessentials.com/2025-ski-test/skis/2025-k2-mindbender-99ti",
     [("Mindbender 99Ti","K2","2025","134/99/120 mm, All Terrain Rocker")],"waist widths · Ti or C laminate"),
   X("Supershape","HEAD's performance piste-carving line.","Head","","https://www.head.com/en_DK/shop-ski/skis/performance",
     [("Supershape e-Original","Head","",""),("Supershape e-Speed","Head","",""),("Supershape e-Magnum","Head","",""),("Supershape e-Rally","Head","",""),("Supershape e-Titan","Head","","")],"turn shape · width"),
   X("Redster","Atomic's race-derived carving line.","Atomic","","https://www.skiessentials.com/2025-ski-test/skis/2025-atomic-redster-g9",
     [("Redster G9","Atomic","2025","GS carver, 68 mm waist, Revoshock S"),("Redster Q9.8","Atomic","",""),("Redster Q4","Atomic","","")],"G (giant slalom), Q (versatile)"),
   X("Hero Elite","Rossignol's recreational race carvers with Line Control Technology.","Rossignol","","https://www.skiessentials.com/2023-ski-test/skis/2023-rossignol-hero-elite-lt-ti",
     [("Hero Elite LT Ti","Rossignol","2023","long turn, 17 m at 177 cm"),("Hero Elite MT Ti","Rossignol","","multi-turn")],"turn radius"),
  ],
  "m":[["Arcade 84 W","Rossignol"],["Addikt Pro 76","Salomon"],["Stance 80","Salomon"],["Stance Pro 90","Salomon"],["départ. 01","Salomon"],["Blaze 94","Völkl"],["Peregrine 80","Völkl"]],
  "r":[["Stance","Salomon"]]},
 {"n":"Ski boot","a":"alpine ski boot","d":"Rigid plastic-shell boot made to drive an alpine or touring ski through the binding; stiffness is rated on the maker's scale.",
  "t":["flex index","last width LV / MV / HV","race","all-mountain","hike mode (hybrid)","GripWalk or ISO 5355 sole","BOA closure"],
  "s":"https://www.buckmans.com/products/1000/ski",
  "x":[
   X("Mach1","Tecnica's performance boot family in three last widths, with T-Drive carbon spine.","Tecnica","","https://outdoorgearlab.com/reviews/snow-sports/ski-boots/tecnica-mach1-mv-130",
     [("Mach1 MV 130","Tecnica","","Editors' Choice, 100 mm last"),("Mach1 LV","Tecnica","","98 mm last"),("Mach1 HV","Tecnica","","103 mm last")],"flex · last width")],
  "m":[["Hawx Prime 110 BOA","Atomic"],["Hawx Prime 90","Atomic"],["Redster JR 60 RS","Atomic"],["Raptor 65","Head"],["S/Pro Alpha","Salomon"],["S/Pro Supra","Salomon"],
       ["Shift Alpha BOA","Salomon"],["Cochise 130","Tecnica"],["Speedmachine 3 130 S","Nordica"],["Alltrack 90 HV","Rossignol"]],
  "r":[["Hawx Prime","Atomic"],["S/Pro","Salomon"]]},
 {"n":"Ski binding","a":"","d":"Binding that fixes a boot to a ski and releases it in a fall.",
  "t":["alpine (step-in)","hybrid (alpine/touring heel or frame)","touring pin (tech)","DIN range","brake width","GripWalk / Multinorm compatibility"],
  "s":"https://www.salomon.com/en-us/c/sports/alpine-skiing/bindings",
  "x":[
   X("Nevada","Look's toe binding that let the boot release at the toe; the Nevada II toe and Grand Prix heel followed.","Look","1950",MW,
     [("Nevada II toe","Look","1962",""),("Grand Prix heel","Look","1962","")],""),
   X("Rotamat","Marker heel with instep release, later with a turntable under the instep.","Marker","1965",MW,
     [("Rotamat","Marker","1965",""),("M4-15 Rotamat S","Marker","1979","turntable heel")],""),
   X("Duke and Jester","Marker freeski binding system of 2007; the Griffon followed.","Marker","2007",MW,
     [("Duke","Marker","2007",""),("Jester","Marker","2007",""),("Griffon","Marker","2008","")],"DIN · brake width"),
  ],
  "m":[["Icon RS 16","Atomic"],["Shift 13 MN","Atomic"],["Strive 14 GW","Atomic"],["Freeflex 14 GW","Head"],["Lowride 12 TCX GW","Marker"],["MTN Pure","Salomon"],
       ["MTN Summit 12","Salomon"],["S/LAB Shift 2 13 Multinorm","Salomon"],["Strive 12 Gripwalk","Salomon"]],
  "r":[["MTN Summit","Salomon"],["Shift","Salomon"],["Strive","Salomon"]]},
 {"n":"Ski pole","a":"","d":"Pole with a grip, strap and basket used in alpine and touring skiing.","t":["aluminium","carbon","adjustable","race (bent GS)","powder basket"],
  "s":"https://www.salomon.com/en-us/shop/sports/alpine-skiing.html"},
 {"n":"Ski helmet","a":"snow helmet","d":"Helmet made for skiing and snowboarding.","t":["hard shell","in-mould","MIPS or rotational system","with visor","audio-ready"],"s":"https://www.rei.com/c/ski-helmets",
  "m":[["Logan","Anon"],["Revent GT AMID","Atomic"],["Watts","Bern"],["Jackson","Giro"],["Ledge","Giro"],["Code","Smith"],["Level","Smith"],["Method","Smith"],["Nexus","Smith"],["Vantage","Smith"]]},
 {"n":"Ski goggles","a":"snow goggles","d":"Goggles made for skiing and snowboarding against glare, wind and snow.","t":["cylindrical or spherical lens","magnetic interchangeable lens","photochromic","over-the-glasses (OTG)"],
  "s":"https://www.rei.com/c/ski-goggles",
  "m":[["Revent Q HD","Atomic"],["Flight Deck","Oakley"],["Sentry Pro","Salomon"],["I/O MAG","Smith"],["Moment","Smith"],["Reason OTG","Smith"],["Skyline","Smith"],["Squad","Smith"]]},
 {"n":"Ski bag","a":"","d":"Bag that carries one pair of skis. A bag for several pieces is in Bags & Accessories.","t":["padded","unpadded","wheeled","adjustable length"],
  "s":"https://www.salomon.com/en-us/c/sports/alpine-skiing/sports-and-equipment-bags",
  "m":[["Extend 1 Pair Padded 165+20","Salomon"],["Original 1 Pair 160-210","Salomon"]]},
]
brands=[
 {"n":"Völkl","c":"Germany","seg":"Premium","kf":"skis","d":"German ski maker from Straubing.","sig":["Mantra"],"s":K},
 {"n":"Nordica","c":"Italy","seg":"Premium","kf":"skis, ski boots","d":"Italian ski boot and ski maker.","sig":["Enforcer"],"s":K},
 {"n":"Salomon","c":"France","seg":"Mainstream","kf":"skis, boots, bindings","d":"French winter-sports and outdoor brand from Annecy.","sig":["QST"],"s":K},
 {"n":"Atomic","c":"Austria","seg":"Professional & flagship","kf":"skis, boots","d":"Austrian ski maker.","sig":["Redster","Bent Chetler"],"s":K},
 {"n":"Blizzard","c":"Austria","seg":"Premium","kf":"skis","d":"Austrian ski maker.","sig":["Brahma"],"s":K},
 {"n":"K2","c":"United States","seg":"Mainstream","kf":"skis","d":"American ski brand.","sig":["Mindbender"],"s":K},
 {"n":"Head","c":"Austria","seg":"Mainstream","kf":"skis, rackets","d":"Sports-equipment maker founded by Howard Head.","sig":["Supershape"],"s":K},
 {"n":"Rossignol","c":"France","seg":"Professional & flagship","kf":"skis","d":"French ski maker.","sig":["Hero Elite"],"s":K},
 {"n":"Tecnica","c":"Italy","seg":"Premium","kf":"ski boots","d":"Italian ski-boot maker.","sig":["Mach1"],"s":K},
 {"n":"Marker","c":"Germany","f":"1952","seg":"Specialist","kf":"ski bindings","d":"Binding maker founded by Hannes Marker in Straubing; pioneer of releasable bindings.","sig":["Rotamat","Duke and Jester"],"s":MW},
 {"n":"Look","c":"France","seg":"Specialist","kf":"ski bindings","d":"French ski-binding maker whose Nevada introduced toe release.","sig":["Nevada"],"s":MW},
]
notes=("All 7 old kinds kept. Alpine ski: 16 flat models turned into 9 line archetypes (Mantra, Enforcer, QST, Bent Chetler, Brahma, Mindbender, Supershape, Redster, Hero Elite) + 7 models; "
 "dropped Stance Pro 82/86 (covered by Stance range). Ski boot: dropped S/Pro Alpha C BOA, S/Pro Delta BOA, S/Pro Supra Dual BOA, S/Pro Supra S BOA, T4 (S/Pro range covers them); added Mach1 archetype and test-page models. "
 "Binding: dropped Evo 9 GW CA, MTN Summit 9, N Strive 16 MN, S/LAB Shift 2 10, Strive 10/14 Gripwalk (ranges cover). Helmet: dropped Rodeo. "
 "Not done: Lange, Atomic Hawx and Look Pivot archetypes, Experience/Kore/Racetiger/Bonafide/Elan/Fischer lines, helmet/goggle test winners - Blister pages 403 (also via Firecrawl) and no other retrieved page.")
w('E2','11_00',{"kinds":kinds,"brands":brands,"traditions":[],"notes":notes})
