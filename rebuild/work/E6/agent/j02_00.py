import json, os
def w(job, obj):
    p=f'/home/user/Possession-Taxonomy/rebuild/work/E6/shelves/{job}.json'; t=p+'.tmp'
    json.dump(obj,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
def X(n,d,mk,y,s,v=(),dt="",a=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),q)) for q in v],"dt":dt}
LC="Leica Camera"; CZ="Carl Zeiss"; SO="Swarovski Optik"; NK="Nikon"; CN="Canon"; FJ="Fujinon"; ST="Steiner-Optik"
WB="https://en.wikipedia.org/wiki/Binoculars"; WT="https://en.wikipedia.org/wiki/Trinovid"; WS="https://en.wikipedia.org/wiki/Swarovski_Optik"
bino={"n":"Binoculars","a":"field glasses","d":"Pair of matched telescopes held in both hands, sized by magnification × objective diameter (e.g. 8×42).",
 "t":["Porro prism","roof prism (Schmidt–Pechan)","roof prism (Abbe–König)","image-stabilised","compact / pocket","marine 7×50 with compass","rangefinder"],
 "s":WB,
 "x":[
  X("Leica Trinovid","Leitz's 1958 roof-prism binocular with internal focusing and built-in dioptre, the template for the modern roof binocular.",LC,"1958",WT,
    [("Trinovid 7×42",LC,"1958","first model, Uppendahl prisms"),("Trinovid 8×20 C",LC,"","compact"),("Trinovid 8×42 BA",LC,"1993","Schmidt–Pechan, made to 2000"),("Trinovid BN",LC,"2001","successor to BA")],
    "Uppendahl then Schmidt–Pechan prisms (c. 1990) · B = spectacle eye relief"),
  X("Zeiss 7×50 B/GA T*","Rubber-armoured Porro marine binocular, the last of Zeiss's long 7×50 line and a collector favourite.",CZ,"","https://binocular.ch/zeiss-7x50-b-ga-t/",
    [("7×50 B/GA T*",CZ,"","individual focus; discontinued 2017")],"Porro I prisms · 7.4° field · 1,230 g"),
  X("Swarovski EL","Swarovski's open-bridge roof binocular with wrap-around grip; the reference alpha binocular since 1999.",SO,"1999",WS,
    [("EL",SO,"1999","first wrap-around grip"),("EL Swarovision",SO,"2009",""),("EL Range",SO,"",""),("NL Pure",SO,"2020","new flagship line")],"roof prism · open bridge"),
  X("Swarovski Habicht","Classic Austrian Porro binocular made since the company's founding.",SO,"1949",WS,[("Habicht 7×42",SO,"1949","")],"Porro · 7×42"),
  X("Zeiss Victory SF","Zeiss's flagship roof binocular, its first designed for birders, with a low focus wheel and field flattener.",CZ,"2014","https://www.allaboutbirds.org/news/?p=16187",
    [("Victory SF 8×42",CZ,"2014","780 g, 1.8-turn focus")],"8×42 · 780 g"),
  X("Leica Ultravid","Leica's premium roof binocular line added above the Trinovid.",LC,"2004",WT,[],""),
  X("Leica Noctivid","Leica's top roof binocular, answering the Swarovision EL and Victory SF.",LC,"2016",WT,[],""),
  X("Nikon E II","Nikon's classic wide-field central-hinge Porro binocular.",NK,"1999","https://www.binomania.it/en/nikon-8x30-eii-review/",
    [("Classic Porro 8×30 and 10×35",NK,"1978","original E"),("8×30 E II",NK,"1999","8.8° field, not waterproof"),("10×35 E II",NK,"","")],"Porro · 8×30, 10×35"),
  X("Canon IS binoculars","Porro binoculars with Canon's powered image stabilisation, steadying hand-held views at high power.",CN,"","https://scopeviews.co.uk/Canon12x36ISIII.htm",
    [("10×30 IS",CN,"",""),("Canon 10x30 IS II",CN,"",""),("12×36 IS III",CN,"","third-generation stabiliser"),("10×42 IS",CN,"","waterproof, for birders"),("18×50 IS",CN,"",""),("Canon 10x20 IS",CN,"","pocket")],"8×20 to 18×50 · battery powered"),
  X("Fujinon FMT-SX","Fujinon's 7×50 marine Porro binocular with individual focus, sold as Polaris; a rubber-armoured and a compass version.",FJ,"","https://company7.com/fujinon/binocs/0750fmtrsx.html",
    [("7×50 FMT-SX",FJ,"",""),("7×50 FMTR-SX Polaris",FJ,"","rubber armour, objective covers"),("7×50 FMTRC-SX",FJ,"","with compass")],"7×50 · 7.5° field · 23 mm eye relief · nitrogen-filled"),
  X("Steiner Military","German military binocular with individual focus eyepieces.",ST,"",WB,[("Military 8×30 R",ST,"","")],"")],
 "m":[["Conquest HD",CZ],["Zeiss Victory Pocket 10x25",CZ],["SLC",SO],["CL Companion",SO],["CL Pocket",SO],["AX Visio",SO],["Monarch HG",NK],["EDG",NK],["Travelite EX",NK],["Nikon Aculon T02 10x21",NK],
     ["Diamondback","Vortex Optics"],["Frontier ED X Compact","Hawke Sport Optics"],["Nature DX ED","Celestron"],["Aurora BGA VHD","Opticron"],["Derby Compact","Eschenbach Optik"],["SP","Pentax"],["YF II","Kowa"],["H2O","Bushnell"],["Steiner Bluhorizons 10x26",ST],["Fujifilm Fujinon TS 12x28","Fujifilm"]]}
giant={"n":"Giant binoculars","a":"astronomy binoculars · big binoculars","d":"Binoculars of 70 to 150 mm aperture, used on a tripod or fork mount.",
 "t":["straight-through","45° or 90° angled eyepieces","interchangeable eyepieces"],
 "s":"https://www.astroshop.eu/binoculars/20/a,Fernglaeser.Allgemein.Serie=Habicht/a,Fernglaeser.Leistung.Bauart=Porro+prisms",
 "x":[X("Fujinon 25×150 MT-SX","Huge Porro binocular for astronomy and ship use, needing a dedicated mount.",FJ,"","https://www.cliftoncameras.co.uk/fujinon-25x150-mt-sx-binoculars",
    [("25×150 MT-SX",FJ,"","2.7° field")],"150 mm objectives · mount sold separately")],
 "m":[["SkyMaster","Celestron"],["SkyMaster Pro ED","Celestron"],["LB ED-SX",FJ],["High Lander","Kowa"],["BT126 SS-A","Vixen"],["Spezial Astro","Bresser"],["Nightstar","Omegon"],["Brightsky","Omegon"],["Argus","Omegon"]]}
mono={"n":"Monocular","a":"","d":"Single-tube handheld viewing instrument, not a telescope on a mount.",
 "t":["pocket","close-focus","waterproof roof prism"],
 "s":"https://www.astroshop.eu/binoculars/20/a,Fernglaeser.Allgemein.Serie=Inception/a,Fernglaeser.Anwendungsgebiete=Theatre",
 "m":[["Mono 6x18 T*",CZ],["Monovid",LC],["Endurance ED Mono","Hawke Sport Optics"],["Oregon 4 PC Oasis monocular","Opticron"],["Artes Monocular HR","Vixen"],["Multi Monocular H","Vixen"],["Cygnus","Viking"],["Mono","Omegon"]]}
opera={"n":"Opera glasses","a":"theatre glasses","d":"Small low-power Galilean binoculars for the theatre and opera.",
 "t":["Galilean","with lorgnette handle","folding","mother-of-pearl (antique)"],
 "s":"https://levenhuk.com/reviews/opera_binoculars_buying_guide/",
 "x":[X("Lemaire opera glasses","Nineteenth-century Paris opera glasses, often in mother-of-pearl and gilt, with joint focusing of both barrels.","Lemaire","1847","https://fallriverhistorical.org/TinyTuesdays/?p=76",[],"mother-of-pearl, gilt metal · marked 'Lemaire, Paris'")],
 "m":[["OperaView","Carson Optical"],["Glamour","Eschenbach Optik"],["Pliant","Kenko Optics"],["Broadway 325F","Levenhuk"],["Compact Opera","Vixen"]]}
brands=[
 {"n":LC,"c":"Germany","seg":"Premium","kf":"cameras, sport optics","d":"Wetzlar optics maker, formerly Leitz (Leica since 1986), maker of Trinovid, Ultravid and Noctivid binoculars.","sig":["Leica Trinovid","Leica Ultravid","Leica Noctivid"],"s":WT},
 {"n":CZ,"c":"Germany","f":"1846","seg":"Premium","kf":"optics","d":"German optics maker whose Porro binoculars of 1894 set the modern pattern; makes Victory and Conquest binoculars.","sig":["Zeiss Victory SF","Zeiss 7×50 B/GA T*"],"s":"knowledge"},
 {"n":SO,"c":"Austria","f":"1949","seg":"Premium","kf":"binoculars, scopes","d":"Absam, Tyrol maker of premium binoculars, spotting scopes and riflescopes, founded by Wilhelm Swarovski.","sig":["Swarovski EL","Swarovski Habicht"],"s":WS},
 {"n":NK,"c":"Japan","f":"1917","seg":"Mainstream","kf":"cameras, optics","d":"Japanese camera and optics maker with binoculars from entry level to the EDG.","sig":["Nikon E II"],"s":"knowledge"},
 {"n":CN,"c":"Japan","f":"1937","seg":"Mainstream","kf":"cameras, IS binoculars","d":"Japanese camera maker known in binoculars for image stabilisation.","sig":["Canon IS binoculars"],"s":"knowledge"},
 {"n":FJ,"c":"Japan","seg":"Specialist","kf":"marine binoculars","d":"Fujifilm's optics brand, known for marine 7×50s and giant binoculars.","sig":["Fujinon FMT-SX","Fujinon 25×150 MT-SX"],"s":"knowledge"},
 {"n":ST,"c":"Germany","seg":"Specialist","kf":"military, marine binoculars","d":"German maker of military, marine and hunting binoculars.","sig":["Steiner Military"],"s":"knowledge"},
 {"n":"Lemaire","c":"France","f":"1847","seg":"Heritage manufactory","kf":"opera glasses","d":"Paris maker of opera glasses, founded by Jacques Lemaire, a major producer in the later nineteenth century.","sig":["Lemaire opera glasses"],"s":"https://fallriverhistorical.org/TinyTuesdays/?p=76"}]
w('02_00',{"kinds":[bino,giant,mono,opera],"brands":brands,"traditions":[],
 "notes":"Binoculars: 35 flat models -> 11 archetypes + 20 m. Dropped as minor/duplicative: Bresser Hunter Porro, Celestron Cometron and UpClose G2, Nikon Action, Bushnell PowerView, Olympus WP II, Omegon Blackstar and Hunter, Pentax UD 10x21, RSPB Skylark, Swarovski CL Curio. Ultravid/Noctivid years follow Wikipedia (2004/2016); binocular.ch gives 2003/2017. Not built (no fetched page): Vortex Viper/Razor, Nikon Monarch archetype (Monarch HG in m), Leica Monovid/Zeiss Mono archetypes, Chevalier opera glasses, Oberwerk. Giant binoculars: Fujinon 25x150 archetype; Celestron SkyMaster stays in m (retailer page empty). Opera glasses: maker-less 'Lorgnette' model became a type. No traditions (opera-glass making is covered by the Lemaire brand entry)."})
