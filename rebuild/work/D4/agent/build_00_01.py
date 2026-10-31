import json, os
W='https://en.wikipedia.org/wiki/'
def V(n,mk,y='',d=''):
    v={"n":n,"mk":mk}
    if y: v["y"]=y
    if d: v["d"]=d
    return v
premium={"n":"Premium fixed-lens camera","a":"premium compact · large-sensor compact · enthusiast compact",
 "d":"Compact digital camera with a fixed, high-quality lens and a large sensor (1-inch to full frame), aimed at enthusiasts.",
 "t":["fixed prime lens","fixed zoom lens","monochrome sensor"],
 "s":W+"Point-and-shoot_camera",
 "x":[
 {"n":"Fujifilm X100","a":"X100 series · FinePix X100","d":"Rangefinder-styled APS-C compact with a fixed 23 mm lens and hybrid optical/electronic viewfinder.","mk":"Fujifilm","y":"2010","s":W+"Fujifilm_X100",
  "v":[V("FinePix X100","Fujifilm","2010","shown 2010, sold 2011; 12 MP APS-C"),V("X100S","Fujifilm","2013","16 MP"),V("X100T","Fujifilm","2014","16 MP"),V("X100F","Fujifilm","2017","24 MP"),V("X100V","Fujifilm","2020","26 MP"),V("X100VI","Fujifilm","2024","40 MP")],
  "dt":"generation · body colour (silver, black)"},
 {"n":"Ricoh GR","a":"GR Digital · GR series","d":"Pocketable street-photography compact with a fixed wide-angle prime lens; APS-C sensor since 2013.","mk":"Ricoh","y":"2005","s":W+"Ricoh_GR_digital_cameras",
  "v":[V("GR Digital","Ricoh","2005","1/1.8-inch CCD, 8 MP"),V("GR Digital II","Ricoh","2007"),V("GR Digital III","Ricoh","2009"),V("GR Digital IV","Ricoh","2011"),V("GR","Ricoh","2013","first APS-C GR, 16.2 MP"),V("GR II","Ricoh","2015"),V("GR III","Ricoh","2018","24 MP APS-C"),V("GR IIIx","Ricoh","2021","longer-lens variant"),V("GR III HDF","Ricoh","2024","highlight diffusion filter"),V("GR IIIx HDF","Ricoh","2024","highlight diffusion filter"),V("GR IV","Ricoh","2025","25.74 MP APS-C"),V("GR IV HDF","Ricoh","","highlight diffusion filter"),V("GR IV Monochrome","Ricoh","","monochrome sensor")],
  "dt":"generation · standard or x (longer lens) · HDF filter · monochrome"},
 {"n":"Leica Q","a":"Q (Typ 116) · Q series","d":"Full-frame compact with a fixed fast Summilux prime lens and electronic viewfinder.","mk":"Leica","y":"2015","s":W+"Leica_Q",
  "v":[V("Q (Typ 116)","Leica","2015","24 MP, 28 mm f/1.7"),V("Q-P","Leica","2018"),V("Q2","Leica","2019"),V("Q3","Leica","2023","60 MP, 28 mm f/1.7 Summilux"),V("Q3 43","Leica","2024","43 mm APO Summicron")],
  "dt":"generation · focal length (28 mm, 43 mm) · finish"},
 {"n":"Sony RX1","a":"Cyber-shot DSC-RX1","d":"Full-frame compact with a fixed 35 mm f/2 Zeiss Sonnar lens.","mk":"Sony","y":"2012","s":W+"Sony_Cyber-shot_DSC-RX1",
  "v":[V("DSC-RX1","Sony","2012","24.3 MP full frame"),V("DSC-RX1R","Sony","2013","no anti-aliasing filter"),V("DSC-RX1R II","Sony","2015","42 MP")],
  "dt":"generation · anti-aliasing filter"},
 {"n":"Sony RX100","a":"Cyber-shot DSC-RX100","d":"Pocket compact with a 1-inch sensor and fixed zoom lens.","mk":"Sony","y":"2012","s":W+"Sony_Cyber-shot_DSC-RX100",
  "v":[V("RX100","Sony","2012","28–100 mm equiv. f/1.8–4.9"),V("RX100 II","Sony","2013"),V("RX100 III","Sony","2014","24–70 mm equiv. f/1.8–2.8"),V("RX100 IV","Sony","2015"),V("RX100 V","Sony","2016"),V("RX100 VA","Sony","","updated V"),V("RX100 VI","Sony","2018","24–200 mm equiv."),V("RX100 VII","Sony","2019"),V("Stellar","Hasselblad","2013","RX100-based"),V("Stellar II","Hasselblad","2014","RX100 II-based")],
  "dt":"generation · lens range"},
 {"n":"Canon PowerShot G","a":"PowerShot G series","d":"Canon's enthusiast compact line with manual controls; larger 1-inch and 1.5-inch sensors from 2012.","mk":"Canon","y":"2000","s":W+"Canon_PowerShot_G",
  "v":[V("G1","Canon","2000"),V("G9","Canon","2007"),V("G12","Canon","2010"),V("G1 X","Canon","2012","1.5-inch sensor"),V("G16","Canon","2013"),V("G7 X","Canon","2014","1-inch sensor"),V("G5 X","Canon","2015"),V("G9 X","Canon","2015"),V("G1 X Mark III","Canon","2017","APS-C"),V("G5 X Mark II","Canon","2019"),V("G7 X Mark III","Canon","2019")],
  "dt":"generation · sensor size (1/1.8-inch to APS-C)"},
 {"n":"Panasonic Lumix LX","a":"LX series · LX100","d":"Panasonic's enthusiast compact line with Leica-branded fast zoom lenses; Four Thirds sensor in the LX100.","mk":"Panasonic","y":"","s":W+"Panasonic_Lumix_DMC-LX100",
  "v":[V("Lumix LX7","Panasonic"),V("Lumix LX100","Panasonic","2014","Four Thirds, 13 MP"),V("Lumix LX100 II","Panasonic","2018","17 MP")],
  "dt":"generation · sensor size"}
 ]}
compact={"n":"Compact camera","a":"compact fixed-lens camera · point-and-shoot",
 "d":"Small digital stills camera with a non-removable lens and mostly automatic operation, built for pocket or carry use.",
 "t":["point-and-shoot","travel zoom","rugged/waterproof","vlogging compact"],
 "m":[["Lumix TZ70","Panasonic"],["Lumix TZ95D","Panasonic"]],
 "s":"https://www.bhphotovideo.com/c/product/1664769-REG/ricoh_15286_gr_iiix_digital_camera.html"}
bridge={"n":"Bridge camera","a":"superzoom camera",
 "d":"Digital stills camera with a fixed long-range zoom lens in a larger, SLR-like body with manual controls.",
 "t":["1-inch sensor","small-sensor superzoom"],
 "s":"https://www.cameraworld.co.uk/panasonic-lumix-fz1000-ii-digital-bridge-camera-100111.html",
 "x":[
 {"n":"Sony RX10","a":"Cyber-shot DSC-RX10","d":"Bridge camera with a 1-inch sensor and a Zeiss zoom lens.","mk":"Sony","y":"2013","s":W+"Sony_Cyber-shot_DSC-RX10",
  "v":[V("DSC-RX10","Sony","2013","24–200 mm equiv. constant f/2.8"),V("DSC-RX10 II","Sony"),V("DSC-RX10 III","Sony"),V("Cyber-shot DSC-RX10 IV","Sony")],"dt":"generation · zoom range"},
 {"n":"Panasonic Lumix FZ","a":"FZ series · FZ1000","d":"Panasonic's bridge line with Leica-branded zooms; 1-inch sensor in the FZ1000 and FZ2500.","mk":"Panasonic","y":"","s":W+"Panasonic_Lumix_DMC-FZ1000",
  "v":[V("Lumix FZ1000","Panasonic","2014","1-inch, 25–400 mm equiv."),V("Lumix FZ2500","Panasonic","2016"),V("Lumix FZ1000 II","Panasonic","2019")],"dt":"model · sensor size · zoom range"},
 {"n":"Nikon Coolpix P superzoom","a":"Coolpix P900 · P1000","d":"Nikon's small-sensor superzooms with extreme telephoto reach, up to 3000 mm equivalent.","mk":"Nikon","y":"","s":W+"Nikon_Coolpix_P1000",
  "v":[V("Coolpix P900","Nikon"),V("Coolpix P1000","Nikon","2018","125× zoom, 24–3000 mm equiv."),V("Coolpix P1100","Nikon","2025","replaces P1000")],"dt":"model · zoom range"}
 ]}
K=lambda n,c,f,seg,d: {"n":n,"c":c,"f":f,"seg":seg,"d":d,"s":"knowledge"}
brands=[K("Fujifilm","Japan","1934","camera and imaging maker","Japanese imaging company making X-series and GFX cameras and instax instant cameras."),
 K("Ricoh","Japan","1936","camera and office equipment maker","Japanese maker of the GR compacts and, through Ricoh Imaging, Pentax cameras."),
 K("Leica","Germany","","luxury camera maker","German maker of M rangefinders, Q and SL cameras and lenses."),
 K("Sony","Japan","1946","electronics maker","Japanese electronics group making Alpha and Cyber-shot cameras."),
 K("Canon","Japan","1937","camera and imaging maker","Japanese maker of EOS and PowerShot cameras and lenses."),
 K("Panasonic","Japan","1918","electronics maker","Japanese electronics group making Lumix cameras."),
 K("Nikon","Japan","1917","camera and optics maker","Japanese optics company making Z, DSLR and Coolpix cameras."),
 K("Hasselblad","Sweden","1941","premium camera maker","Swedish maker of medium-format cameras.")]
for b,sig in zip(brands,[["Fujifilm X100"],["Ricoh GR"],["Leica Q"],["Sony RX100","Sony RX1","Sony RX10"],["Canon PowerShot G"],["Panasonic Lumix LX","Panasonic Lumix FZ"],["Nikon Coolpix P superzoom"],[]]):
    if sig: b["sig"]=sig
notes=("Kept all planned kinds (Compact camera k3, Bridge camera k4); added Premium fixed-lens camera. Ricoh GR models and Lumix LX7 moved from Compact camera into archetypes; old range 'GR' replaced by the archetype. "
 "Left out (not confirmed on retrieved pages): Leica Q2 Monochrom, Sony RX1R III, Panasonic LX1-LX15, small-sensor FZ models, RX10 II-IV years, and any travel-zoom/rugged/vlogging models — those stay as types of Compact camera. "
 "Parallel web_fetch returned 402 (no credit); WebFetch used. Brand facts from knowledge; Leica founding year omitted (lineage ambiguous).")
out={"kinds":[premium,compact,bridge],"brands":brands,"traditions":[],"notes":notes}
p='work/D4/shelves/00_01.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
