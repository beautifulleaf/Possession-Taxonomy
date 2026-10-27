import json, os
WK="https://en.wikipedia.org/wiki/"
def v(n,mk="",y="",d=""):
    o={"n":n,"mk":mk}
    if y:o["y"]=y
    if d:o["d"]=d
    return o
P="Prusa Research"; B="Bambu Lab"; CR="Creality"; MB="MakerBot"; FL="Formlabs"; VD="Voron Design"; E="Elegoo"; A="Anycubic"
pr={"n":"3D printer","a":"","d":"Machine that builds objects layer by layer, from melted filament (FDM) or light-cured resin.",
 "t":["FDM / FFF","resin (MSLA, LCD)","resin (laser SLA)","self-build kit","enclosed CoreXY","multi-material"],
 "s":"https://us.store.bambulab.com/collections/3d-printer",
 "x":[
 {"n":"RepRap","a":"","d":"Open-source self-replicating printer project from the University of Bath that started the home 3D-printing movement.","mk":"","y":"2005","s":WK+"RepRap",
  "v":[v("RepRap 1.0 Darwin","","2008","first generation"),v("Mendel","","2009","second generation"),v("Huxley","","2010","miniature Mendel"),v("Rostock","","2012","first successful delta design")],"dt":"open hardware · self-printed parts"},
 {"n":"MakerBot Replicator","a":"","d":"MakerBot's desktop FDM line that brought ready-built printers to homes and schools.","mk":MB,"y":"2012","s":WK+"MakerBot",
  "v":[v("Cupcake CNC",MB,"2009","predecessor kit"),v("Thing-O-Matic",MB,"2010","predecessor kit"),v("Replicator",MB,"2012"),v("Replicator 2",MB,"2012"),v("5th Generation Replicator",MB,"2014"),
       v("Replicator Mini",MB,"2014"),v("Replicator Z18",MB,"2014"),v("Replicator+",MB,"2016"),v("METHOD",MB,"2018")],"dt":"build volume · single or dual extrusion"},
 {"n":"Prusa i3","a":"Original Prusa","d":"Josef Průša's RepRap-derived open FDM printer, sold as kits and assembled by Prusa Research.","mk":P,"y":"2012","s":WK+"Prusa_i3",
  "v":[v("Prusa i3 (MK0)",P,"2012","original design"),v("MK1",P,"2015","1.75 mm filament"),v("MK2",P,"2016","mesh bed levelling"),v("MK2S",P,"2017"),v("MK3",P,"2017"),v("MK3S",P,"2019"),
       v("MK3S+",P,"2020"),v("MK4",P,"2023","load-cell levelling"),v("Original Prusa MK4S",P,"2024"),v("Original Prusa MINI",P,"","cantilever sibling"),v("Original Prusa XL",P,"","CoreXY, large format"),v("Prusa CORE One",P,"2024","enclosed CoreXY successor")],
  "dt":"kit or assembled · MMU multi-material add-on"},
 {"n":"Creality Ender 3","a":"Ender-3","d":"Low-cost open-frame FDM printer widely used as an entry machine.","mk":CR,"y":"2018","s":WK+"Creality",
  "v":[v("Creality CR-10",CR,"2016","larger forerunner"),v("Ender 3",CR,"2018"),v("Ender 3 Pro",CR,"2018"),v("Ender 3 V2",CR,"2020"),v("Ender 3 S1",CR,"2021"),v("Ender 3 V3",CR,"2024")],"dt":"kit · upgrades widely sold"},
 {"n":"Bambu Lab X1 / P1 / A1","a":"Bambu","d":"Fast, largely automatic consumer FDM printers with optional multi-colour feeding.","mk":B,"y":"2022","s":WK+"Bambu_Lab",
  "v":[v("X1",B,"2022","enclosed CoreXY flagship"),v("P1P",B,"2022"),v("P1S",B,"2023"),v("X1E",B,"2023"),v("A1 mini",B,"2023"),v("A1",B,"2023","bed-slinger"),v("H2D",B,"2025"),
       v("H2S",B,"2025"),v("P2S",B,"2025"),v("H2C",B,"2025"),v("X2D",B,"2026"),v("A2L",B,"2026")],"dt":"AMS multi-colour unit · enclosure"},
 {"n":"Voron","a":"","d":"Open-source high-speed CoreXY printers that owners build from sourced parts or kits.","mk":VD,"y":"2015","s":WK+"Voron_Design",
  "v":[v("Voron 1",VD,"c. 2015–2016","original design"),v("Voron 2.4",VD,"2020","four-corner Z"),v("Voron 2.4R2",VD,"2022"),v("Voron Trident",VD,"2021","fixed gantry, three Z motors"),v("Voron 0.1",VD,"2021","small 120 mm"),v("Voron 0.2",VD,"2023"),
       v("Voron Switchwire",VD),v("Voron Legacy",VD,"","recreation of Voron 1")],"dt":"build size · kit vendor"},
 {"n":"Elegoo Mars","a":"","d":"Low-cost LCD resin printer line from Elegoo.","mk":E,"y":"2017","s":"https://www.3dnatives.com/3d-materials/en/3d-printers/elegoo-mars/",
  "v":[v("Mars",E,"2017"),v("Mars 2",E),v("Mars 2 Pro",E),v("Mars 3 Pro",E),v("Mars 3 Ultra",E),v("Elegoo Mars 5 Ultra",E)],"dt":"LCD resolution · build volume"},
 {"n":"Anycubic Photon","a":"","d":"Anycubic's LCD resin printer line, priced near budget FDM machines.","mk":A,"y":"2018","s":"https://all3dp.com/1/anycubic-photon-mono-review-3d-printer-specs/?critical=1",
  "v":[v("Photon",A,"2018","first Anycubic resin printer"),v("Photon S",A),v("Photon Zero",A),v("Photon Mono",A,"","monochrome LCD"),v("Photon Mono X",A),v("Photon Mono SE",A)],"dt":"monochrome or RGB LCD · resolution"},
 {"n":"Formlabs Form","a":"","d":"Desktop stereolithography printers that brought laser resin printing to studios and prosumers.","mk":FL,"y":"2013","s":WK+"Formlabs",
  "v":[v("Form 1",FL,"2013","laser SLA"),v("Form 1+",FL,"2014"),v("Form 2",FL,"2015"),v("Form 3",FL,"2019","Low Force Stereolithography"),v("Form 4",FL,"2024","LCD light source")],"dt":"resin cartridges · build size"}],
 "m":[["Creality K1",CR],["Elegoo Saturn 4 Ultra 16K",E],["Elegoo Centauri Carbon",E],["Elegoo Neptune 4 Pro",E],["Elegoo Neptune 4",E],["Elegoo Neptune 4 Plus",E],["Elegoo Neptune 4 Max",E],
      ["Elegoo Neptune 3 Pro",E],["Elegoo Neptune 3 Plus",E],["Elegoo Neptune 3 Max",E],["Elegoo Jupiter",E],["Elegoo OrangeStorm Giga",E]]}
fi={"n":"3D-printer filament","a":"","d":"Spooled plastic filament fed into FDM 3D printers.","t":["PLA","PETG","ABS","ASA","TPU","nylon (PA)","polycarbonate","carbon- or glass-fibre filled","silk / matte / high-speed PLA"],
 "s":"https://shop.polymaker.com/fr/collections/filament-pla?page=1",
 "m":[["PolyLite PLA","Polymaker"],["PolyMax PLA","Polymaker"],["Polymaker PLA Pro","Polymaker"],["Polymaker HT-PLA","Polymaker"],["Panchroma Basic PLA","Polymaker"],["Panchroma Matte PLA","Polymaker"],["Panchroma Silk PLA","Polymaker"],["Panchroma Neon PLA","Polymaker"],["Sunlu High Speed PLA","Sunlu"],["Soleyin Ultra PLA","Creality"]]}
re={"n":"3D-printing resin","a":"photopolymer resin","d":"Light-cured liquid photopolymer for MSLA, DLP and SLA resin printers.","t":["standard","ABS-like","water-washable","plant-based","tough / rigid"],
 "s":"https://clevercreations.org/best-3d-printer-resin-brand-3d-printing-resins/",
 "m":[["Siraya Tech Fast ABS-Like Resin","Siraya Tech"],["Siraya Tech Blu","Siraya Tech"],["ABS-Like Resin",E],["Water Washable Resin",E],["Plant-Based Rapid Resin",A],["Onyx Rigid Pro 410","Phrozen"],["NOVA3D Printer Resin","NOVA3D"]]}
up={"n":"3D-printer upgrade parts","a":"hotend · nozzle · extruder","d":"Replacement or upgrade parts for a 3D printer: hotends, nozzles, extruders and build plates.","t":["hotend","nozzle","extruder","build plate"],
 "s":"https://www.tinymachines3d.com/products/e3d-revo-six-hotend-rapid-change",
 "x":[{"n":"E3D V6","a":"","d":"Groove-mount all-metal hotend from E3D.","mk":"E3D","y":"","s":"https://www.tinymachines3d.com/products/e3d-revo-six-hotend-rapid-change",
       "v":[v("Revo Six","E3D","","drop-in V6 replacement with tool-free Revo nozzles; 12 V or 24 V")],"dt":"voltage · nozzle size"}]}
K="knowledge"
brands=[
 {"n":P,"c":"Czech Republic","seg":"Premium","kf":"Original Prusa","d":"Prague company of Josef Průša making the Original Prusa i3 line and its successors.","lines":["Original Prusa","CORE One"],"sig":["Prusa i3"],"s":WK+"Prusa_i3"},
 {"n":MB,"c":"USA","f":"2009","seg":"Mainstream","kf":"Replicator","d":"New York desktop-printer pioneer, bought by Stratasys in 2013 and merged with Ultimaker in 2022.","sig":["MakerBot Replicator"],"s":WK+"MakerBot"},
 {"n":B,"c":"China","f":"2020","seg":"Premium","kf":"fast FDM","d":"Shenzhen maker of fast, multi-colour consumer FDM printers.","lines":["X1","P1","A1","H2"],"sig":["Bambu Lab X1 / P1 / A1"],"s":WK+"Bambu_Lab"},
 {"n":CR,"c":"China","f":"2014","seg":"Value","kf":"Ender 3","d":"Shenzhen maker of low-cost FDM printers including the Ender and CR series.","lines":["Ender","CR","K1"],"sig":["Creality Ender 3"],"s":WK+"Creality"},
 {"n":FL,"c":"USA","f":"2011","seg":"Professional & flagship","kf":"desktop SLA","d":"Somerville, Massachusetts maker of Form resin printers.","sig":["Formlabs Form"],"s":WK+"Formlabs"},
 {"n":VD,"f":"2015","seg":"Artisan & independent","kf":"open-source CoreXY","d":"Open-hardware project founded by Maksim Zolin that publishes the Voron printer designs.","sig":["Voron"],"s":WK+"Voron_Design"},
 {"n":E,"c":"China","seg":"Value","kf":"resin printers","d":"Shenzhen maker of low-cost resin and FDM printers and resins.","lines":["Mars","Saturn","Neptune"],"sig":["Elegoo Mars"],"s":K},
 {"n":A,"c":"China","seg":"Value","kf":"resin printers","d":"Chinese maker of Photon resin printers, Kobra FDM printers and resins.","lines":["Photon"],"sig":["Anycubic Photon"],"s":"https://all3dp.com/1/anycubic-photon-mono-review-3d-printer-specs/?critical=1"},
 {"n":"E3D","c":"United Kingdom","seg":"Specialist","kf":"hotends","d":"British maker of 3D-printer hotends and nozzles.","sig":["E3D V6"],"s":K},
 {"n":"Polymaker","c":"China","seg":"Mainstream","kf":"filament","d":"Filament maker selling PolyLite, PolyMax and Panchroma lines.","lines":["PolyLite","PolyMax","Panchroma"],"s":K}]
notes="Both old kinds kept (k76, k77); two planned new kinds added (resin, upgrade parts). Old flat printer models folded into Bambu Lab, Prusa i3 and Elegoo Mars archetype versions; Elegoo Neptune/Saturn/others stay in m. Not added for lack of a retrieved page: Prusament, eSun and Bambu filament, Bondtech extruders, Micro Swiss, E3D V6 year, Elegoo Saturn line as archetype, Anycubic Mono years."
out={"kinds":[pr,fi,re,up],"brands":brands,"traditions":[],"notes":notes}
p="work/D1/shelves/05_01.json"; json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
