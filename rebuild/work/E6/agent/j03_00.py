import json, os
def w(job, obj):
    p=f'/home/user/Possession-Taxonomy/rebuild/work/E6/shelves/{job}.json'; t=p+'.tmp'
    json.dump(obj,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
def X(n,d,mk,y,s,v=(),dt="",a=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),q)) for q in v],"dt":dt}
CZ="Carl Zeiss"; OL="Olympus"; NI="Nikon"; PL="Powell & Lealand"; DL="Dino-Lite"; CA="Carson Optical"
EV="Evident (formerly Olympus Scientific)"; EU="Euromex"; MO="Motic"; OM="Omegon"; OP="Optika"; BR="Bresser"; TT="ToupTek"; LV="Levenhuk"
ALW="https://alanwood.net/olympus/compound-microscopes.html"
comp={"n":"Compound light microscope","a":"biological microscope · upright microscope","d":"Microscope with an objective and an eyepiece in series, for thin specimens on a slide.",
 "t":["monocular","binocular","trinocular","finite (160 mm) optics","infinity-corrected optics","phase contrast","darkfield","student / teaching","antique brass"],
 "s":"https://www.microscope.com/education-center/buyers-guides/how-to-buy",
 "x":[
  X("Powell & Lealand No. 1","Large brass bar-limb research stand, the flagship of Victorian British microscopy, made almost unchanged for about 40 years.",PL,"1869","https://microscope-antiques.com/pandleal.html",
    [("tripod stand (forerunner)",PL,"1843","bar-limb tripod design that led to the No. 1"),("transitional No. 1",PL,"1861","ring-carried stage"),("No. 1 definitive",PL,"1869",""),("No. 1 with substage fine focus",PL,"1882",""),("No. 1 with draw-tube rack",PL,"1887","suggested by E.M. Nelson")],
    "brass · monocular or binocular · substage condenser"),
  X("Powell & Lealand No. 5 (Iron Microscope)","Simpler iron student stand from the same London workshop.",PL,"1848","https://microscope-antiques.com/pandleal.html",
    [("Iron Microscope / No. 5 Student Model",PL,"1848","")],"iron and brass"),
  X("Zeiss Standard","Modular post-war Zeiss laboratory stand, a favourite used microscope for amateurs; nosepieces, tubes and illuminators interchange.",CZ,"","https://www.microbehunter.com/microscopy-forum/viewtopic.php?p=76499",
    [("Standard WL",CZ,"","larger stand with removable nosepiece"),("Standard Junior",CZ,"","student stand, not fully modular")],"fixed or removable nosepiece · built-in or separate lamp house · 160 mm DIN objectives"),
  X("Olympus BH-2","Olympus's 1980s clinical and lab microscope with long-barrel (LB) objectives; it led the world market and is plentiful used.",OL,"1980",ALW,
    [("BHS",OL,"","interchangeable nosepiece"),("BHT",OL,"","interchangeable nosepiece"),("BHSU",OL,"","fixed nosepiece"),("BHTU",OL,"","fixed nosepiece"),("BH (predecessor, BHA/BHB/BHC)",OL,"1974","")],
    "160 mm tube · 45 mm parfocal · halogen lamp"),
  X("Olympus CH","Olympus student and teaching microscope, sold widely to schools and labs.",OL,"1976",ALW,
    [("CH",OL,"1976",""),("CH-2",OL,"1985","")],"160 mm tube · monocular or binocular"),
  X("Nikon Eclipse E200","Affordable Nikon lab microscope with CFI60 infinity optics, introduced in 2000; later replaced by the Eclipse Si.",NI,"2000","https://www.microscope.healthcare.nikon.com/about/news/nikon-eclipse-e200-microscope-offers-brightest-easiest-most-versatile-imaging-to-help-build-veterinary-practices",
    [("Eclipse E200",NI,"2000","CFI60 infinity optics, Siedentopf head")],"infinity optics · phase contrast and fluorescence options")],
 "m":[["B-Scope",EU],["BioBlue",EU],["Delphi-X",EU],["iScope IS.1153",EU],["BA410 Elite",MO],["MonoView",OM],["Nabla I Bino",OM],["Nabla II",OM],["Nabla III",OM],["MIPRO portable compound microscope","PZO Polskie Zakłady Optyczne"]],
 "r":[["Nabla",OM],["Panthera",MO],["iScope",EU]]}
stereo={"n":"Stereo microscope","a":"dissecting microscope · stereomicroscope","d":"Low-power microscope with two optical paths giving an upright three-dimensional view of solid objects.",
 "t":["Greenough (two objectives)","common main objective (CMO)","fixed magnification","zoom","boom stand","trinocular"],
 "s":"https://www.astroshop.eu/microscopy/microscopes/stereo-microscope/23_11_20/s,green",
 "x":[
  X("Greenough stereo microscope","Two-objective stereomicroscope conceived by H.S. Greenough, put to Ernst Abbe in 1896; Zeiss built it as the first factory-made stereo microscope.",CZ,"1896","https://neurophysics.ucsd.edu/Manuals/Zeiss/DV_4_and_Stemi_2000_Stereo_Overview_Profile.pdf",
    [],"two converging optical paths · upright image"),
  X("Zeiss Stemi","Zeiss's Greenough-type stereomicroscope family for lab, workshop and hobby use.",CZ,"","https://neurophysics.ucsd.edu/Manuals/Zeiss/DV_4_and_Stemi_2000_Stereo_Overview_Profile.pdf",
    [("Stemi DR",CZ,"","fixed-magnification"),("Stemi DV4",CZ,"",""),("Stemi 2000",CZ,"","first stereo with a 35° viewing angle"),("Stemi 2000 C",CZ,"",""),("Stemi 2000 CS",CZ,"",""),("Stemi 355",CZ,"","from old data")],
    "fixed or zoom · object field up to 35 mm")],
 "m":[["SZ51",EV],["SZ61",EV],["SZX7",EV],["SZX10",EV],["SZX16",EV],["SMZ-143",MO],["SMZ-171",MO],["Nexius Zoom",EU],["StereoBlue",EU],["Advance ICD",BR],["Analyth STR",BR],["Science ETD 201",BR],["StereoView",OM],["SLX-3",OP],["SZR-180",OP],["HPS 6","Windaus"]]}
dig={"n":"Digital microscope","a":"USB microscope","d":"Microscope with its own sensor that shows the image on a screen or computer.",
 "t":["handheld USB","with built-in LCD","Wi-Fi","stand-mounted inspection"],
 "s":"https://www.astroshop.eu/microscopy/microscopes/digital-microscopes/23_11_40",
 "x":[X("Dino-Lite handheld USB microscope","Pen-sized handheld digital microscope with built-in LEDs that plugs into a computer; AnMo Electronics' Dino-Lite line.",DL,"","https://www.dinolite.us/about/",
    [("AM4113T",DL,"","from old data"),("AM4113ZT",DL,"","from old data, polarising"),("AF3113T",DL,"","from old data"),("AF4135ZTE",DL,"","from old data"),("AF7115MZT",DL,"","from old data")],"USB or Wi-Fi · fixed or adjustable polariser · LED ring")],
 "m":[["MacroZoom",EU],["OIV 345","Kern & Sohn"],["DTX 800 LCD",LV],["Digistar",OM],["DigitalView",OM],["EVO Cam II","Vision Engineering"],["Digital Microscope S1000","Vixen"]],
 "r":[["DTX",LV]]}
pocket={"n":"Pocket microscope","a":"handheld microscope","d":"Small handheld microscope carried in the pocket, often with its own light.",
 "t":["lighted","zoom","paper fold-up","smartphone clip"],
 "s":"https://www.carson.com/product-directory/microscopes",
 "x":[
  X("Foldscope","Fold-it-yourself paper microscope with a tiny ball lens, designed by Manu Prakash's Stanford team to cost under a dollar.","","2014","https://en.wikipedia.org/wiki/Foldscope",
    [("standard kit","","","140× lens; magnets attach it to a smartphone")],"paper body · ball lens"),
  X("Carson MicroBrite","Cheap LED-lighted pocket microscope sold widely for field and classroom use.",CA,"","https://www.activewild.com/carson-microbrite-pocket-microscope-review/",
    [("MicroBrite MM-24",CA,"","20–40×, removable base"),("MicroBrite Plus MM-300",CA,"","60–120×")],"zoom · LED")]}
pol={"n":"Polarising microscope","a":"polarizing microscope · petrographic microscope","d":"Microscope that lights the specimen with polarised light, for minerals, crystals and thin sections.",
 "t":["rotating stage","Bertrand lens","compensator slot","transmitted or reflected light"],
 "s":"https://www.astroshop.eu/microscopy/microscopes/upright-microscopes/polarising-microscopes/23_11_10_60/a,Mikroskope.Mechanik.Bauart=binocular",
 "m":[["BH-2 BHTP",OL],["CX31-P",OL],["CX43 POL",EV],["E200POL",NI],["50iPOL",NI],["BA310 POL",MO],["iScope POL",EU]]}
parts={"n":"Microscope optics & parts","a":"microscope objective · microscope eyepiece · ocular · microscope stage","d":"Objectives, eyepieces, condensers and stages bought apart from the stand to upgrade or repair a microscope.",
 "t":["objective (RMS or M25 thread; achromat, plan, apochromat)","eyepiece (23.2 or 30 mm barrel)","condenser","stage (manual or motorised)"],
 "s":"https://www.newport.com/p/MVC-40X",
 "m":[["EP10X23 WF10X eyepiece pair","AmScope (United Scope LLC)"],["WHB10X-H",EV],["N-WF10X",MO],["CFI CM 10x",NI],["Deluxe microscope eyepieces",OM],["SCAN IM","Märzhäuser Wetzlar"],["ProScan H101","Prior Scientific"]],
 "r":[["ACHROPLAN","Carl Zeiss Microscopy"],["A-Plan","Carl Zeiss Microscopy"],["EC Plan-Neofluar","Carl Zeiss Microscopy"],["HC PL APO","Leica Microsystems"],["UPLFLN",EV],["PLAPON",EV]]}
cam={"n":"Microscope camera","a":"eyepiece camera","d":"Camera made to fit a microscope's eyepiece tube or camera port.",
 "t":["eyepiece camera","C-mount camera","HDMI","Wi-Fi","USB"],
 "s":"https://www.astroshop.eu/microscopy/microscopy-accessories/cameras/23_60_50/pr,200-500",
 "x":[X("Dino-Eye eyepiece camera","Camera that drops into a microscope eyepiece tube in place of the eyepiece; AnMo's Dino-Eye series.",DL,"","https://www.dinolite.us/about/",[],"fits eyepiece tube · USB")],
 "m":[["MikroCam SP 5.0",BR],["MicroCam PRO HDMI",BR],["CMEX",EU],["HD-Lite",EU],["Moticam A1",MO],["Moticam S1",MO],["Moticam Pro S5 Lite",MO],["M500 BASE",LV],["M1000 PLUS",LV],["C-E2 eyepiece camera",OP],["C-P6 Pro",OP],["ToupCam E3ISPM",TT],["ToupCam XCAMLITE4K",TT],["CHD10","MAGUS"]],
 "r":[["MikroCam",BR],["Moticam",MO],["ToupCam",TT]]}
slide={"n":"Microscope slide","a":"slide · cover slip","d":"Glass slide that holds a specimen under a microscope, blank or with a prepared mount.",
 "t":["plain","frosted end","cavity (depression)","prepared slide set","antique mounted slide"],
 "s":"https://www.microscope.com/all-products/slides-and-accessories",
 "x":[X("Victorian mounted slide","Hand-made specimen slide from the professional mounting trade of the later 19th century, now collected.","","1850s–1900","https://www.quekett.org/starting/antique-microscopes-slides",
    [("Topping slide","Topping","",""),("Norman slide","Norman","",""),("Sinel & Hornell slide","Sinel & Hornell","",""),("Wheeler slide","Wheeler","",""),("retailer slides","Watson & Son","","also Beck and Baker")],"mount type · label · specimen")],
 "m":[["Plain Glass Microslides","Fisherbrand"],["Superfrost Plus Microscope Slides","Fisherbrand"],["Premium Frosted Microscope Slides","Fisherbrand"]]}
brands=[
 {"n":CZ,"c":"Germany","f":"1846","seg":"Premium","kf":"optics","d":"Jena optics maker whose microscopes include the Standard stands and Stemi stereomicroscopes.","sig":["Zeiss Standard","Zeiss Stemi","Greenough stereo microscope"],"s":"knowledge"},
 {"n":OL,"c":"Japan","f":"1919","seg":"Premium","kf":"microscopes, cameras","d":"Japanese optics maker; its scientific division became Evident in 2022.","sig":["Olympus BH-2","Olympus CH"],"rel":[EV],"s":"knowledge"},
 {"n":NI,"c":"Japan","f":"1917","seg":"Mainstream","kf":"cameras, microscopes","d":"Japanese optics maker (formerly Nippon Kogaku) whose microscopes run from student to research stands.","sig":["Nikon Eclipse E200"],"s":"knowledge"},
 {"n":PL,"c":"United Kingdom","f":"1841","seg":"Heritage manufactory","kf":"brass microscopes","d":"London microscope makers (Hugh Powell and Peter Lealand), the leading Victorian British makers; ceased trading 1901.","sig":["Powell & Lealand No. 1"],"s":"https://microscope-antiques.com/pandleal.html"},
 {"n":DL,"c":"Taiwan","seg":"Specialist","kf":"USB microscopes","d":"Handheld USB digital microscopes and Dino-Eye eyepiece cameras, a trademark of AnMo Electronics.","sig":["Dino-Lite handheld USB microscope","Dino-Eye eyepiece camera"],"s":"https://www.dinolite.us/about/"},
 {"n":CA,"c":"United States","seg":"Value","kf":"magnifiers, pocket optics","d":"American maker of low-priced pocket microscopes, magnifiers and binoculars.","sig":["Carson MicroBrite"],"s":"knowledge"},
 {"n":"AmScope (United Scope LLC)","c":"United States","f":"1996","seg":"Value","kf":"microscopes","d":"Irvine, California seller of low-priced microscopes, cameras and parts; a division of United Scope LLC.","s":"https://eu.amscope.com/pages/about-us"}]
w('03_00',{"kinds":[comp,stereo,dig,pocket,pol,parts,cam,slide],"brands":brands,"traditions":[],
 "notes":"Compound: 6 archetypes (P&L No.1 and No.5, Zeiss Standard, Olympus BH-2 and CH, Nikon Eclipse E200); old models kept in m. Not built (no fetched page): Leitz, Nikon Labophot, Swift, Ross/Watson as separate archetypes, Zeiss Standard 14/16/18 numbering. Stereo: Greenough and Zeiss Stemi archetypes; m cut 19->16 (dropped NexiusZoom duplicate, Motic SMZ-160, Carl Zeiss Stemi 355 moved to the Stemi archetype); Leica S9, Nikon SMZ not added (no page). Digital: Dino-Lite archetype holds the 5 old Dino-Lite models; Levenhuk/Motic/ToupCam ranges trimmed (ToupCam HCAM moved out as a camera family); Andonstar not added. Pocket: Foldscope (maker left blank: designer Prakash lab, no maker page fetched) and Carson MicroBrite. Polarising: kept 7 old models, no archetype (no polarising-specific page fetched); LV100POL dropped as industrial. Optics & parts: merged objective, eyepiece and stage (k40-k42); objective ranges cut 13->6 and eyepieces to 5; Olympus WHSZ stereo eyepieces dropped. Camera: 33 models cut to 14 plus Dino-Eye archetype. Slides: Victorian mounted slide archetype from Quekett; Fisherbrand cut to 3; depression slide became type 'cavity'. No traditions."})
