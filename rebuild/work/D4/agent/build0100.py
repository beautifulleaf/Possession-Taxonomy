import json, os
W='https://en.wikipedia.org/wiki/'
def X(n,mk,y,s,d,dt,v=(),a=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
slr = {"n":"Film SLR camera","a":"film single-lens reflex camera · 35 mm SLR",
 "d":"35 mm film body with a mirror and prism that shows the picture through the taking lens.",
 "t":["manual mechanical","electronic auto-exposure","autofocus"],
 "s":W+"Single-lens_reflex_camera",
 "x":[
  X("Kine Exakta","Ihagee","1936",W+"Kine_Exakta","First 35 mm SLR in regular production.","Exakta bayonet mount · round or rectangular magnifier",
    [("Version 1 (round magnifier)","Ihagee","1936","original"),("Version 2 (rectangular magnifier)","Ihagee","",""),("Exacta (North American)","Ihagee","","US-market spelling")]),
  X("Contax S","Zeiss Ikon","1949",W+"Single-lens_reflex_camera","One of the two original eye-level pentaprism SLRs to enter production in 1949.","eye-level pentaprism",a="VEB Contax S"),
  X("Asahiflex","Pentax","1952",W+"Asahiflex","Japan's first 35 mm SLR; the IIB added a quick-return mirror; led to the Asahi Pentax.","M37 screw mount (Asahiflex) · integrated pentaprism (Asahi Pentax)",
    [("Asahiflex I","Pentax","1952",""),("Asahiflex IA","Pentax","1953",""),("Asahiflex IIB","Pentax","1954","quick-return mirror"),("Asahiflex IIA","Pentax","1955",""),("Asahi Pentax","Pentax","1957","integrated eye-level pentaprism")]),
  X("Nikon F","Nikon","1959",W+"Nikon_F","Nikon's first SLR, combining many existing SLR features in one body; introduced the Nikon F mount.","Nikon F mount · interchangeable finders (Photomic metering heads)",
    [("Nikon F Photomic","Nikon","1962","meter head with independent cell"),("Nikon F Photomic T","Nikon","","TTL metering"),("Nikon F Photomic FTn","Nikon","1968","centre-weighted TTL metering")]),
  X("Nikon F2","Nikon","1971",W+"Nikon_F2","Last all-mechanical professional Nikon SLR, a photojournalist workhorse.","Nikon F mount · DP-series metering heads · titanium F2T",
    [("F2 Photomic (DP-1)","Nikon","1971",""),("F2S Photomic (DP-2)","Nikon","1973",""),("F2SB Photomic (DP-3)","Nikon","1976",""),("F2A Photomic (DP-11)","Nikon","1977","AI lenses"),("F2AS Photomic (DP-12)","Nikon","1977",""),("F2T","Nikon","1978","titanium"),("F2H","Nikon","1978","high speed")]),
  X("Nikon F3","Nikon","1980",W+"Nikon_F3","Giugiaro-styled professional SLR with aperture-priority automation; last manual-focus pro Nikon.","Nikon F mount · DE-2 or DE-3 high-eyepoint finder · titanium F3/T",
    [("F3HP","Nikon","","high-eyepoint DE-3 finder"),("F3/T","Nikon","1982","titanium, champagne then black"),("F3P","Nikon","1983","press version, weathersealed"),("F3AF","Nikon","1983","Nikon's first autofocus camera"),("F3 Limited","Nikon","1994","Japan-only")]),
  X("Nikon F4","Nikon","1988",W+"Nikon_F4","Nikon's first professional SLR with practical autofocus.","Nikon F mount · MB-20, MB-21 or MB-23 battery pack",
    [("F4","Nikon","1988","MB-20, 4 fps"),("F4S","Nikon","1988","MB-21, 5.7 fps"),("F4E","Nikon","1991","MB-23")]),
  X("Nikon F5","Nikon","1996",W+"Nikon_F5","Fifth professional film SLR in Nikon's F line, made until 2004.","Nikon F mount · 50th anniversary edition",
    [("F5 50th Anniversary","Nikon","","limited edition")]),
  X("Nikon F6","Nikon","2004",W+"Nikon_F6","Nikon's last film SLR and final F-series model, discontinued in 2020.","Nikon F mount"),
  X("Nikon FM","Nikon","1977",W+"Nikon_FM","Compact mechanical semi-professional SLR on a duralumin chassis; started the FM/FE family.","Nikon F mount",
    [("FM","Nikon","1977","mechanical"),("FE","Nikon","1978","electronic, aperture priority"),("FM2","Nikon","1982",""),("FE2","Nikon","1983","faster shutter, TTL flash"),("FA","Nikon","1983",""),("FM3A","Nikon","2001","limited production")],a="FM · FM2 · FE · FE2"),
  X("Nikkormat","Nikon","1965",W+"Nikkormat","Nikon's consumer line of F-mount SLRs, sold as Nikomat in Japan.","Nikon F mount · mechanical FT series or electronic EL series",
    [("FT","Nikon","1965","first with TTL metering"),("FS","Nikon","1965","unmetered"),("FTN","Nikon","1967",""),("EL","Nikon","1972","aperture-priority auto"),("FT2","Nikon","1975","hot shoe"),("ELW","Nikon","1976","winder"),("FT3","Nikon","1977","AI lenses"),("EL2","Nikon","1977","sold as Nikon")],a="Nikomat"),
  X("Canon F-1","Canon","1971",W+"Canon_F-1","Canon's first professional system SLR, built to rival the Nikon F and F2.","Canon FD mount · titanium foil shutter · motor-drive High Speed model",
    [("F-1","Canon","1971",""),("F-1 High Speed Motor Drive","Canon","1972","9 fps"),("F-1n","Canon","1976","13 refinements"),("New F-1","Canon","1981","successor")]),
  X("Canon AE-1","Canon","1976",W+"Canon_AE-1","First A-series SLR and the first SLR with a digital integrated circuit; a mass-market best-seller.","Canon FD mount",
    [("AE-1","Canon","1976",""),("AT-1","Canon","1977",""),("AV-1","Canon","1979",""),("AE-1 Program","Canon","1981","program mode; successor"),("AL-1","Canon","1982","")],a="AE-1 Program"),
  X("Canon A-1","Canon","1978",W+"Canon_A-1","First SLR with programmed auto-exposure and all four PASM modes.","Canon FD mount"),
  X("Canon EOS-1","Canon","1989",W+"Canon_EOS-1","Canon's first professional EOS autofocus film SLR.","Canon EF mount",
    [("EOS-1","Canon","1989",""),("EOS-1N","Canon","1994",""),("EOS-1N RS","Canon","1995",""),("EOS-1V","Canon","2000","")]),
  X("Olympus OM-1","Olympus","1972",W+"Olympus_OM-1","Maitani's compact, quiet manual SLR that shrank the 35 mm SLR; shown as the M-1.","Olympus OM mount",
    [("M-1","Olympus","1972","original name"),("OM-1","Olympus","1973",""),("OM-1MD","Olympus","1974","motor-drive ready"),("OM-1n","Olympus","1979","")],a="M-1"),
  X("Olympus OM-2","Olympus","1975",W+"Olympus_OM-2","OM-1 body with automatic exposure and direct TTL metering (ADM).","Olympus OM mount",
    [("OM-2","Olympus","1975",""),("OM-2N","Olympus","1979",""),("OM-2S Spot Program","Olympus","1984","spot metering, program mode"),("OM-4","Olympus","","successor")]),
  X("Pentax Spotmatic","Pentax","1964",W+"Pentax_Spotmatic","One of the first SLRs with through-the-lens metering.","M42 screw mount",
    [("Spotmatic","Pentax","1964",""),("Spotmatic SL","Pentax","1968",""),("Spotmatic SP II","Pentax","1971",""),("Electro-Spotmatic / ES","Pentax","1971","auto exposure"),("Spotmatic F","Pentax","1973",""),("ES II","Pentax","1973",""),("Spotmatic SP1000","Pentax","1974","")]),
  X("Pentax K1000","Pentax","1976",W+"Pentax_K1000","Simplest K-series SLR, fully mechanical; the classic student camera, over three million sold.","Pentax K mount · made in Japan, Hong Kong (1978) and China (1990)",
    [("K2","Pentax","1975","K-series sibling"),("KM","Pentax","1975","K1000 base"),("KX","Pentax","1975","")]),
  X("Pentax MX","Pentax","1976",W+"Pentax_MX","Compact fully mechanical manual SLR, Pentax's flagship until the LX.","Pentax K mount · twin of the ME"),
  X("Pentax LX","Pentax","1980",W+"Pentax_LX","Pentax's professional system SLR with weather and dust-sealed controls, made until 2001.","Pentax K mount · weather-sealed controls",
    [("LX Gold","Pentax","1981","300 made"),("LX Titanium","Pentax","1994","75th anniversary"),("LX 2000","Pentax","2000","limited")]),
  X("Minolta SR-T","Minolta","1966",W+"Minolta_SR-T","Minolta's SR-mount series with through-the-lens full-aperture metering.","Minolta SR mount",
    [("SR-T 101","Minolta","1966","")]),
  X("Minolta X-700","Minolta","1981",W+"Minolta_X-700","Top model of Minolta's last manual-focus series; European Camera of the Year 1982.","Minolta SR mount",
    [("X-500 / X-570","Minolta","",""),("X-300 / X-370","Minolta","1983","")]),
  X("Contax RTS","Contax","1975",W+"Contax_RTS","Porsche Design-styled professional SLR made by Yashica with Zeiss optics.","Zeiss optics · Porsche Design styling",
    [("RTS","Contax","1975",""),("RTS II","Contax","1982","TTL flash, titanium shutter"),("RTS III","Contax","1990","vacuum film plate")]),
 ],
 "m":[["Canonflex","Canon"],["Retina Reflex","Kodak"],["SR-2","Minolta"],["T","Miranda Camera"],["Auto 100","Topcon"],["Pentamatic","Yashica"]],
 "r":[["Exa","Ihagee"]]}
rf = {"n":"Film rangefinder camera","a":"35 mm rangefinder",
 "d":"35 mm film body focused with a coupled rangefinder in the viewfinder window.",
 "t":["interchangeable-lens","fixed-lens","screw mount (M39/LTM)","bayonet mount"],
 "s":"https://kamerastore.com/en-us/products/leica-m6",
 "x":[
  X("Leica screw-mount (Barnack)","Leica","1925",W+"Leica_Camera","Oskar Barnack's compact 35 mm camera that founded the format; rangefinder coupled from the Leica II.","M39 screw mount (LTM, from 1930)",
    [("Ur-Leica","Leica","1914","prototype"),("Leica I","Leica","1925",""),("Leica I Schraubgewinde","Leica","1930","interchangeable screw-mount lenses"),("Leica II","Leica","1932","coupled rangefinder"),("Leica III","Leica","1933","slow speeds to 1 s"),("Leica IIIa","Leica","","1/1000 s")],a="LTM · Barnack Leica"),
  X("Leica M","Leica","1954",W+"Leica_M_mount","Leica's bayonet rangefinder line with combined range- and viewfinder, the reference 35 mm rangefinder.","Leica M mount · finder magnification (e.g. 0.72×)",
    [("M3","Leica","1954","first M"),("M2","Leica","1957","0.72× finder for wide angles"),("M1","Leica","1959",""),("M4","Leica","1964","faster loading; later M4-2, M4-P"),("M5","Leica","1971","TTL metering"),("M6","Leica","1984","meter in classic body"),("M6 TTL","Leica","1998","TTL flash"),("M7","Leica","2002","aperture priority"),("MP","Leica","2003","manual with TTL metering"),("M-A","Leica","2014","manual only; M3-style re-release"),("M6 (reissue)","Leica","2022","")]),
  X("Zeiss Ikon Contax","Zeiss Ikon","1932",W+"Contax_I","Zeiss Ikon's rival to the Leica II, with bayonet mount, long-base rangefinder and metal shutter.","Contax bayonet mount · vertical metal focal-plane shutter",
    [("Contax I","Zeiss Ikon","1932",""),("Contax II","Zeiss Ikon","1936","rangefinder in viewfinder")],a="Contax I · Contax II"),
  X("Kodak Retina","Kodak","1934",W+"Kodak_Retina","Nagel-designed folding 35 mm cameras built in Stuttgart around the 135 cartridge.","folding body · convertible lenses (IIc, IIIc)",
    [("Retina II","Kodak","1936","rangefinder"),("Retina IIa","Kodak","1939",""),("Retina IIc","Kodak","1954","convertible lenses"),("Retina IIIc","Kodak","1954","with meter")]),
  X("Argus C3","Argus","1939",W+"Argus_C3","Low-priced American rangefinder, 'the Brick', sold over 2.2 million until 1966.","brick-shaped body",a="the Brick"),
  X("Nikon S / SP","Nikon","1948",W+"Nikon_SP","Nikon's rangefinder line from the Nikon I (1948) to the professional SP, the peak of the series.","Nikon S bayonet mount · S-36 motor drive (SP)",
    [("Nikon I","Nikon","1948","first"),("SP","Nikon","1957","professional; first motorised rangefinder"),("S3 (reproduction)","Nikon","2000",""),("SP Limited Edition","Nikon","2005","2,500 made")],a="Nikon rangefinder"),
  X("Canon 7","Canon","1961",W+"Canon_7","Canon's photojournalist rangefinder with selenium meter; last M39-compatible model.","M39 screw mount",
    [("7","Canon","1961","selenium meter"),("7s","Canon","1965","CdS meter, cold shoe"),("7sZ","Canon","1967","7s Type II")]),
  X("Contax G","Contax","1994",W+"Contax_G","Kyocera's autofocus interchangeable-lens rangefinders with Zeiss lenses.","Contax G mount (autofocus, breech-lock)",
    [("G1","Contax","1994",""),("G2","Contax","1996","")]),
  X("Voigtländer Bessa","Voigtländer","1999",W+"35_mm_Bessa","Cosina-made Voigtländer rangefinders that revived affordable screw- and M-mount bodies.","M39 screw (L, R) · Leica M (T, R2 onward) · Nikon S / Contax (R2S, R2C)",
    [("Bessa-L","Voigtländer","1999","M39"),("Bessa-R","Voigtländer","2000","M39"),("Bessa-T","Voigtländer","2001","Leica M"),("Bessa-R2","Voigtländer","2002",""),("Bessa-R2S / R2C","Voigtländer","2002","Nikon S / Contax mount"),("Bessa-R2A / R3A","Voigtländer","2004",""),("Bessa-R2M / R3M","Voigtländer","2007",""),("Bessa-R4A / R4M","Voigtländer","2007","")]),
  X("Konica Hexar RF","Konica","1999",W+"Konica_Hexar_RF","Motorised M-compatible rangefinder with Leica-like finder.","Konica KM mount (Leica M compatible)",
    [("Hexar RF Limited","Konica","2001","chrome, 2,001 made")]),
 ],
 "m":[["Ektra","Kodak"],["Witness","Ilford"],["Opema II","Meopta"]]}
cp = {"n":"35 mm compact film camera","a":"film point-and-shoot camera · viewfinder film camera · premium compact",
 "d":"Small fixed-lens 35 mm camera with autofocus or zone focus and automatic exposure, from everyday to premium models.",
 "t":["autofocus","zone or scale focus","fixed-focus","zoom lens","titanium premium"],
 "s":"https://kamerastore.com/en-pl/products/new-pentax-17-half-frame-35mm-compact-film-camera",
 "x":[
  X("Olympus XA","Olympus","1979",W+"Olympus_XA","Maitani's clamshell pocket cameras; the original is one of the smallest rangefinders made.","sliding clamshell cover · 35 mm f/2.8 (XA) · scale or fixed focus (XA1–XA4)",
    [("XA","Olympus","1979","rangefinder, aperture priority"),("XA2","Olympus","1980","scale focus"),("XA1","Olympus","1982","fixed focus"),("XA3","Olympus","1985","DX coding"),("XA4","Olympus","1985","28 mm macro")]),
  X("Contax T","Contax","1984",W+"Contax_T2","Kyocera's titanium premium compacts with Zeiss Sonnar lenses.","titanium body · 38 mm Sonnar (T, T2) · 35 mm (T3) · 28–56 mm Vario-Sonnar (T-VS)",
    [("Contax T","Contax","1984","manual-focus rangefinder"),("Contax T2","Contax","1991","autofocus, built-in flash"),("Contax T3","Contax","","35 mm lens"),("Contax T-VS","Contax","","zoom")],a="T2 · T3"),
  X("Olympus mju","Olympus","1991",W+"Olympus_Stylus","Olympus's pocket autofocus compact series, sold as Stylus in North America.","prime or zoom lens",
    [("mju (Stylus)","Olympus","1991",""),("mju II (Stylus Epic)","Olympus","1997",""),("mju II Zoom (Stylus Epic Zoom 80)","Olympus","1998","")],a="Stylus · µ"),
  X("Konica Big Mini","Konica","1990","https://www.analog.cafe/r/konica-big-mini-bm-201-camera-review-dhrf","Konica's small autofocus compact line of the 1990s.","35 mm f/3.5 lens (BM-201)",
    [("BM-201","Konica","1990",""),("BM-302","Konica","","next generation"),("Big Mini F","Konica","","")]),
  X("Yashica T4","Yashica","early 1990s",W+"Point-and-shoot_camera","Autofocus compact with a Zeiss Tessar lens.","Tessar lens"),
  X("Konica Hexar","Konica","1993",W+"Konica_Hexar","Autofocus 35 mm f/2 compact with rangefinder-style handling and a silent mode.","35 mm f/2 lens · black, silver, gold finishes",
    [("Hexar (black)","Konica","1993",""),("Hexar Classic","Konica","1993","silver, ~2,000 made"),("Hexar Gold","Konica","1993","500 made"),("Hexar Silver","Konica","1997","silent mode disabled")],a="Hexar AF"),
  X("Nikon 35Ti","Nikon","1993",W+"Nikon_35Ti","Titanium-clad premium compact with a 35 mm f/2.8 lens.","titanium body · analogue dials",
    [("35Ti","Nikon","1993","chrome"),("28Ti","Nikon","1994","28 mm, black")]),
 ]}
hf = {"n":"Half-frame camera","a":"half-frame 35 mm camera · 18×24 camera",
 "d":"35 mm camera that takes 18×24 mm frames, giving twice the shots per roll.",
 "t":["compact","SLR"],
 "s":W+"Half-frame_camera",
 "x":[
  X("Olympus Pen","Olympus","1959",W+"Olympus_Pen","Maitani's compact half-frame series, Japan's first half-frame camera.","fixed lens · manual, D (metered) or EE (auto) series",
    [("Pen","Olympus","1959",""),("Pen EE","Olympus","1961","auto exposure"),("Pen EE-S","Olympus","1962",""),("Pen D","Olympus","1962","fast lens, meter"),("Pen Wide","Olympus","1964",""),("Pen EE-2","Olympus","1968",""),("Pen EE-3","Olympus","1973",""),("Pen EF","Olympus","1981","last Pen")]),
  X("Olympus Pen F","Olympus","1963",W+"Olympus_Pen_F","Half-frame SLR system with rotary shutter, one of the smallest SLR systems.","Olympus Pen F mount · rotary focal-plane shutter",
    [("Pen F","Olympus","1963",""),("Pen FT","Olympus","1966","uncoupled meter"),("Pen FV","Olympus","1967","FT without meter")]),
  X("Canon Demi","Canon","1963","https://global.canon/en/c-museum/product/film44.html","Canon's pocket half-frame with selenium meter, built to answer the Olympus Pen.","28 mm f/2.8 SH lens · selenium meter"),
  X("Pentax 17","Pentax","2024","https://www.australianphotography.com/gear/ricoh-launches-pentax-17-half-frame-fixed-lens-film-camera","Ricoh's new half-frame zone-focus camera that relaunched Pentax film cameras.","25 mm f/3.5 lens · vertical frames · six zone distances"),
  X("Kodak Ektar H35","Kodak","",'https://kamerastore.com/en-int/products/kodak-ektar-h35-half-frame-35mm-film-camera',"Simple reusable fixed-focus half-frame with built-in flash.","fixed focus and shutter · black, brown, beige"),
 ]}
def B(n,c,f,seg,d,sig,s="knowledge",rel=()):
    b={"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":[],"eras":[],"sig":sig,"sc":[],"rel":list(rel),"s":s}
    return {k:v for k,v in b.items() if v not in ("",)}
brands=[
 B("Leica","Germany","1869","premium camera maker","Wetzlar maker of the Leica 35 mm camera and M rangefinders.",["Leica screw-mount (Barnack)","Leica M"],W+"Leica_Camera"),
 B("Nikon","Japan","1917","camera system maker","Japanese optics firm (Nippon Kogaku) behind the F-mount SLRs and S rangefinders.",["Nikon F","Nikon F2","Nikon F3","Nikon FM","Nikon S / SP"]),
 B("Canon","Japan","1937","camera system maker","Japanese camera maker of FD- and EF-mount SLRs and rangefinders.",["Canon F-1","Canon AE-1","Canon A-1","Canon EOS-1","Canon 7"]),
 B("Olympus","Japan","1919","camera maker","Japanese optics maker of the Pen, OM, XA and mju cameras.",["Olympus OM-1","Olympus Pen","Olympus XA","Olympus mju"]),
 B("Pentax","Japan","1919","camera maker","Asahi Optical's camera brand, later company name; now part of Ricoh Imaging.",["Asahiflex","Pentax Spotmatic","Pentax K1000","Pentax LX","Pentax 17"],rel=["Ricoh"]),
 B("Minolta","Japan","1928","camera maker","Japanese maker of SR-mount SLRs; merged into Konica Minolta in 2003.",["Minolta SR-T","Minolta X-700"],rel=["Konica"]),
 B("Konica","Japan","","camera maker","Japanese camera and film maker of the Hexar cameras; merged into Konica Minolta in 2003.",["Konica Hexar","Konica Hexar RF","Konica Big Mini"],rel=["Minolta"]),
 B("Contax","","1932","premium camera brand","Camera brand begun by Zeiss Ikon and later used by Yashica and Kyocera until 2005.",["Contax RTS","Contax G","Contax T"],W+"Contax_G",rel=["Zeiss Ikon","Yashica"]),
 B("Zeiss Ikon","Germany","1926","camera maker","Dresden camera maker formed by Carl Zeiss, maker of the original Contax.",["Zeiss Ikon Contax","Contax S"],rel=["Contax"]),
 B("Ihagee","Germany","1912","camera maker","Dresden maker of the Exakta, the first 35 mm SLR.",["Kine Exakta"],W+"Kine_Exakta"),
 B("Voigtländer","Austria","1756","optics and camera brand","Historic optics name, licensed to Cosina for cameras and lenses since 1999.",["Voigtländer Bessa"]),
 B("Kodak","United States","1888","film and camera maker","Rochester film and camera company; its Stuttgart works made the Retina.",["Kodak Retina"]),
 B("Argus","United States","","camera maker","Ann Arbor, Michigan camera maker of the Argus C3.",["Argus C3"],W+"Argus_C3"),
 B("Yashica","Japan","1949","camera maker","Japanese camera maker, acquired by Kyocera in 1983; made Contax bodies.",["Yashica T4"],rel=["Contax"]),
]
for b in brands:
    if b["s"]!="knowledge" and b["n"] in ("Ihagee","Contax"):
        pass
# drop founding years not on retrieved page for sourced non-knowledge entries
for b in brands:
    if b["n"]=="Ihagee": b.pop("f",None)   # Kine Exakta page gives no founding year
    if b["n"]=="Contax": b["c"]="Germany / Japan"
notes=("Moved out of this shelf (same category, other shelves): Bronica RF645, Mamiya 6/7/7II -> Medium-format rangefinder camera; Hasselblad XPan/XPan II -> Panoramic film camera; "
 "Holga 120N -> Toy camera. Pentax 17 and Olympus Pen F/FT/FV moved into the new Half-frame camera kind. Old range 'F (film SLR)' Nikon and 'M' Leica dissolved into archetypes. "
 "Not added for lack of a retrieved page this session: Leica IIIc/IIIf/IIIg dates, Nikon S2/S3/S4 dates, Minolta SR-T 102/303, Olympus OM-4 year, Contax T3/T-VS years, Ricoh GR1, Yashica T4 versions; Canonflex kept as flat model (no page found). "
 "Wikipedia API and Wikidata helpers returned HTTP 429; Parallel fetch had no credit; all pages retrieved with WebFetch.")
out={"kinds":[slr,rf,cp,hf],"brands":brands,"traditions":[],"notes":notes}
p='work/D4/shelves/01_00.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p); print('written', os.path.getsize(p))
