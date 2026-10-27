import json, os
def w(code, job, obj):
    p = f'/home/user/Possession-Taxonomy/rebuild/work/{code}/shelves/{job}.json'
    t = p + '.tmp'; json.dump(obj, open(t, 'w'), ensure_ascii=False, indent=1); os.replace(t, p)
def K(n,a,d,s,m=None,r=None,t=None):
    k={"n":n,"a":a,"d":d}
    if t: k["t"]=t
    k["s"]=s
    if m: k["m"]=[list(x) for x in m]
    if r: k["r"]=[list(x) for x in r]
    return k
E="Eschenbach Optik"; C="Carson Optical"; A="https://www.astroshop.eu/microscopy/magnifying-glasses/26"; L="https://www.labdepotinc.com/laboratory-glassware"; DWK="DWK Life Sciences"; LE="https://www.labdepotinc.com/c-91-laboratory-equipment"
w('E6','03_01',{"kinds":[
 K("Handheld magnifier","magnifying glass","Magnifying lens on a handle held in the hand.",A,
   [("Mobilux LED",E),("Mediplan Ergo",E),("varioPLUS",E),("BigEye",C),("TriView",C)],None,["plain","illuminated"]),
 K("Stand magnifier","","Magnifier on a desk, floor or neck-cord stand.",A,
   [("Maxi-plus",E),("Combi-plus",E),("Tech-Line stand magnifier","Schweizer"),("LumiLoupe",C)],[("DTX","Levenhuk")]),
 K("Loupe","pocket loupe · eye loupe · watchmaker's loupe · jeweller's loupe","Small strong magnifier held close to the eye, folding into a case or worn in the eye socket.",A,
   [("Pocket Loupe 10x Z00006","Carl Zeiss"),("Aplanatic-achromatic folding magnifier D40 AR","Carl Zeiss"),("easyPOCKET LED",E),("Watchmaker's Loupe","Bausch + Lomb"),("LumiLoupe Plus LO-10",C)],None,
   ["folding loupe","triplet jeweller's loupe","watchmaker's eye loupe","illuminated loupe"]),
 K("Head-worn magnifier","binocular loupe","Loupe or magnifier on a headband or clip; also called a binocular loupe.",A,
   [("maxDETAIL",E),("labo-clip",E),("Tech-Line BINO LED headband magnifier","Schweizer"),("Zeno Vizor H2","Levenhuk"),("Zeno Vizor HR4","Levenhuk")],[("Zeno Vizor","Levenhuk")],["headband","spectacle clip-on"])],
 "brands":[],"traditions":[],"notes":"Merged Folding loupe and Eye loupe into Loupe (folding, triplet, watchmaker's eye loupe and illuminated as types; kept the folding loupe's source). Head-worn magnifier cut from 10 to 5 (Levenhuk Zeno Vizor range kept, five near-identical H/HR models dropped). Electronic video magnifiers not here (H2)."})
w('E6','06_00',{"kinds":[
 K("Beaker","","Wide cylindrical open vessel with a spout, for holding, mixing and heating liquids.",L,[("Griffin Low Form Beakers","Pyrex")]),
 K("Laboratory flask","Erlenmeyer flask · conical flask · volumetric flask","Glass flask with a narrow neck for mixing, heating or making up an exact volume.",L,
   [("KIMAX Graduated Narrow Mouth Erlenmeyer Flasks",DWK),("KIMAX Class A Volumetric Flasks",DWK)],None,["Erlenmeyer (conical)","volumetric","Florence"]),
 K("Test tube","","Small tube closed at one end, for holding or heating a small sample.",L),
 K("Graduated cylinder","measuring cylinder","Tall cylinder with a volume scale, for measuring liquid volume.",L,
   [("BLAUBRAND","BRAND"),("Silberbrand ETERNA","BRAND"),("DURAN Measuring Cylinder with Hexagonal Base",DWK),("Hirschmann Class A Measuring Cylinders","Hirschmann"),("Nalgene PMP Graduated Cylinders","Thermo Scientific")],None,["glass","plastic"]),
 K("Pipette","micropipette · burette","Tube for drawing up and delivering a measured amount of liquid, including the tapped burette.",L,
   [("Research plus","Eppendorf"),("Reference 2","Eppendorf"),("PIPETMAN Classic","Gilson"),("PIPETMAN L","Gilson"),("PYREX Accu-Red Burets","Corning"),("Educational-Grade Burets 17021H",DWK),("Eisco Class A Burette","Eisco")],None,["glass pipette","micropipette","burette"]),
 K("Distillation glassware","round-bottom flask · condenser","Round-bottom flasks, condensers and joints for distilling or refluxing liquids.","https://chemglass.com/flasks?orderby=11&pagenumber=2&pagesize=36",
   [("KIMAX Round Bottom Boiling Flasks",DWK),("Borosilicate Glass Round Bottom Boiling Flasks","United Scientific Supplies"),("SYNTHWARE Round Bottom Flasks","Kemtech America")],None,
   ["round-bottom flask","Liebig condenser","Allihn condenser","Graham condenser","Dimroth condenser","Friedrichs condenser","West condenser","Davies condenser","still head"]),
 K("Petri dish","","Shallow lidded dish for culturing cells or microbes.",L,[("Falcon Bacteriological Petri Dishes","Corning"),("Sterilin Petri Dishes","Thermo Scientific")]),
 K("Dissection set","","Set of instruments for dissecting specimens.","https://www.wiltronics.com.au/product/92418/dissecting-set-10-piece/",[("Deluxe Dissection Kit","Dr Instruments"),("Economy Dissecting Set","Ward's Science")])],
 "brands":[],"traditions":[],"notes":"Merged Erlenmeyer and Volumetric flask into Laboratory flask (types). Merged Burette into Pipette (11 Eppendorf/Gilson + 9 burette models cut to 7). Merged Round-bottom flask and Laboratory condenser into Distillation glassware: the condenser 'models' were maker-less generic designs, now types (Condensyn and Hartzler dropped as obscure); round-bottom flasks cut to 3 (dropped Ace Glass and microscale SYNTHWARE). Graduated cylinder cut from 7 to 5 (dropped BLAUBRAND ETERNA, Fisherbrand)."})
w('E6','06_01',{"kinds":[
 K("Laboratory balance","milligram balance · precision scale","Balance made to weigh small samples precisely.",LE,
   [("Pioneer PX","Ohaus"),("ME-TE","Mettler-Toledo"),("Accuris Compact balances","Accuris Instruments")],None,["analytical","precision","compact"]),
 K("Laboratory thermometer","","Thermometer made to read the temperature of a sample, liquid-in-glass or digital probe.","https://brannan.co.uk/about-brannan/",
   [("Checktemp 1","Hanna Instruments"),("H-B DURAC","SP Bel-Art"),("Digi-Sense Advanced Precalibrated Thermocouple Thermometer","Digi-Sense")],None,["liquid-in-glass","digital probe"]),
 K("Magnetic stirrer","laboratory stirrer · stir plate","Device that mixes a liquid with a stirring bar or paddle, often with a heating plate; home brewers use one for yeast starters.","https://www.spectaris.de/en/company/analytical-biological-and-laboratory-techniques/labortechnik",
   [("RCT basic","IKA"),("Hei-PLATE","Heidolph"),("Cimarec+","Thermo Scientific"),("Isotemp hotplate stirrer","Fisherbrand")],None,["magnetic stirrer","hotplate stirrer","overhead stirrer"]),
 K("Mini centrifuge","centrifuge · microcentrifuge","Small benchtop machine that spins sample tubes to separate their parts.",LE,
   [("5452 Minispin","Eppendorf"),("5453 Minispin Plus","Eppendorf"),("accuSpin Micro 17","Fisher Scientific")]),
 K("Incubator","laboratory incubator","Chamber that holds samples at a set warm temperature.",LE,
   [("Digital Mini Incubator","Fisherbrand"),("Digital Mini Incubator","Gilson"),("Mini Series Classic Vertical Incubator","Genlab")]),
 K("Laminar-flow hood","laminar-flow cabinet · clean bench · flow hood","Cabinet that blows HEPA-filtered air over the work surface to keep samples free of contamination; mushroom growers use small ones.",LE,
   [("Airstream Horizontal Laminar Flow Cabinet LHG","Esco Lifesciences"),("Purifier Horizontal Clean Bench","Labconco")],None,["horizontal flow","vertical flow"])],
 "brands":[],"traditions":[],"notes":"Research-grade SKUs dropped: balance 10 to 3 (Cubis II, Entris II, Explorer, labForce, Accuris Precision); stirrer 9 to 4; centrifuge renamed Mini centrifuge and cut from 50 floor/benchtop research models (Beckman Allegra/Avanti, Sorvall, Megafuge, Hettich, Hermle, Cytospin, larger Eppendorfs) to 3 small units; incubator dropped BINDER and Heratherm lines (9 to 3); laminar-flow hood 6 to 2. No hobby-specific models added (none in old data)."})
