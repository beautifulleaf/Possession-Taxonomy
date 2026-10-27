import json, os
ACOG='https://en.wikipedia.org/wiki/Advanced_Combat_Optical_Gunsight'; CM='https://en.wikipedia.org/wiki/Aimpoint_CompM4'
EO='https://en.wikipedia.org/wiki/EOTech'; OT='https://www.optics-trade.eu/en/zeiss_victory_v8_2_8-20x56_vs_swarovski_z8i_2_3-18x56_p.html/'
GD='https://gundigest.com/gear-ammo/optics/long-live-leupolds-vx-3-family-of-variable-power-scopes'
PU='https://pulsarvision.com/journal/pulsar-riflescopes-in-a-nutshell'
def v(n,mk,y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
kinds=[
{"n":"Rifle scope","a":"telescopic sight · riflescope","d":"Telescopic sight made to mount on a firearm, air rifle or crossbow.",
 "t":["fixed power","variable power","LPVO (low-power variable, 1x bottom end)","first / second focal plane","illuminated reticle","prismatic"],
 "s":"https://www.eurooptic.com/Vortex-Viper-PST-2-10x32-EBR-4-MRAD-PST-2105.aspx",
 "x":[
  {"n":"Leupold VX-3","a":"Vari-X III","d":"Leupold's flagship family of variable-power hunting scopes, descended from the Vari-X III.","mk":"Leupold & Stevens","y":"1973","s":GD,
   "v":[v("Vari-X III","Leupold & Stevens","1973","original line"),v("VX-III","Leupold & Stevens","2004"),v("VX-3","Leupold & Stevens","2009"),v("VX-3i","Leupold & Stevens","2016"),v("VX-3HD","Leupold & Stevens","2021")],
   "dt":"magnification range · objective size · reticle"},
  {"n":"Trijicon ACOG","a":"Advanced Combat Optical Gunsight","d":"Fixed-power prismatic sight with tritium and fibre-optic reticle illumination, made for the M16 and M4.","mk":"Trijicon","y":"1987","s":ACOG,
   "v":[v("TA01","Trijicon","1987","4×32, first model"),v("TA31RCO","Trijicon","","4×32; M150 RCO in US Army service"),v("TA648","Trijicon","","6×48 machine-gun optic")],
   "dt":"magnification 1.25–6× · reticle · illumination (tritium, fibre, LED)"},
  {"n":"Swarovski Z8i","a":"","d":"Swarovski's top-line variable hunting scope with an eight-times zoom range.","mk":"Swarovski Optik","y":"","s":OT,
   "v":[v("Z8i 2.3-18x56 P","Swarovski Optik")],"dt":"magnification range · objective size · reticle"},
  {"n":"Zeiss Victory V8","a":"","d":"Zeiss's top-line variable hunting scope with an eight-times zoom range.","mk":"Zeiss","y":"","s":OT,
   "v":[v("Victory V8 2.8-20x56","Zeiss")],"dt":"magnification range · objective size · reticle"}],
 "m":[["Viper PST Gen II","Vortex Optics"]],"r":[["Viper","Vortex Optics"]]},
{"n":"Red-dot sight","a":"reflex sight · holographic sight","d":"Non-magnifying reflex or holographic sight that shows an aiming dot, made to mount on a weapon.",
 "t":["tube","open reflex","holographic","pistol-mounted"],"s":"https://www.frankonia.de/sitemap/alle-sortimente.html",
 "x":[
  {"n":"Aimpoint CompM","a":"M68 CCO","d":"Tubed battery-powered red-dot sight adopted by the US Army as the M68 Close Combat Optic.","mk":"Aimpoint","y":"","s":CM,
   "v":[v("CompM2","Aimpoint","","earlier M68 CCO"),v("CompM4","Aimpoint","2009","selected for the M68 CCO programme"),v("CompM4s","Aimpoint","","battery and power knob moved low")],
   "dt":"dot size · mount height · NVG settings"},
  {"n":"EOTech holographic weapon sight","a":"HWS · HoloSight","d":"Sight projecting a holographic reticle, introduced as the first holographic sight.","mk":"EOTech","y":"1996","s":EO,
   "v":[v("512","EOTech"),v("553","EOTech","","SU-231/PEQ"),v("EXPS3","EOTech","","SU-231A/PEQ")],
   "dt":"reticle ring and dot · battery type · night-vision compatibility"}]},
{"n":"Night-vision and thermal sight","a":"thermal riflescope · thermal weapon sight · digital night-vision scope","d":"Weapon sight that shows an image in darkness, by thermal imaging or digital low-light sensing.",
 "t":["thermal","digital night vision","image-intensifier","clip-on","laser rangefinder"],"s":PU,
 "x":[
  {"n":"Pulsar Thermion","a":"","d":"Thermal riflescope family styled like a conventional scope, with single-channel and thermal-plus-day models.","mk":"Pulsar","y":"","s":PU,
   "v":[v("Thermion 2 XP50 Pro","Pulsar"),v("Thermion 2 LRF XP50 Pro","Pulsar","","laser rangefinder"),v("Thermion Duo DXP50","Pulsar","","thermal and digital day channels"),v("Thermion Duo DXP55","Pulsar")],
   "dt":"sensor resolution · objective size · rangefinder"},
  {"n":"Pulsar Talion","a":"","d":"Fully thermal riflescope line.","mk":"Pulsar","y":"","s":PU,
   "v":[v("Talion XG35","Pulsar"),v("Talion XQ35 Pro","Pulsar","","replaced XQ38")],"dt":"sensor resolution · objective size"},
  {"n":"Pulsar Digex","a":"","d":"Digital day-and-night riflescope line for 24-hour use.","mk":"Pulsar","y":"","s":PU,
   "v":[v("Digex C50","Pulsar")],"dt":"sensor · illuminator"}]},
{"n":"Scope mount","a":"scope rings · scope bases","d":"Rings, bases or one-piece mount that fix a sight to a weapon.",
 "t":["rings","bases","one-piece cantilever","quick-detach","Picatinny","dovetail"],"s":"https://www.frankonia.de/sitemap/alle-sortimente.html"},
]
K='knowledge'
def b(n,c,f,seg,kf,d,s=K):
    x={"n":n,"c":c,"seg":seg,"kf":kf,"d":d,"s":s}
    if f: x["f"]=f
    return x
brands=[
b("Leupold & Stevens","United States","1907","Mainstream","rifle scopes","Oregon optics maker known for the VX scope lines."),
b("Trijicon","United States","1981","Professional & flagship","tritium sights","Michigan maker of the ACOG and tritium-illuminated sights."),
b("Aimpoint","Sweden","1974","Professional & flagship","red-dot sights","Swedish maker of red-dot sights including the CompM series."),
b("EOTech","United States","1995","Professional & flagship","holographic sights","Michigan maker of holographic weapon sights.",EO),
b("Swarovski Optik","Austria","1949","Premium","hunting optics","Austrian maker of premium scopes and binoculars."),
b("Zeiss","Germany","1846","Premium","optics","German optics maker with Victory and Conquest hunting scopes."),
b("Pulsar","","","Specialist","thermal optics","Maker of thermal and digital night-vision riflescopes."),
b("Vortex Optics","United States","","Mainstream","rifle scopes","Wisconsin optics brand with Viper, Razor and Strike Eagle lines."),
]
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":"Rifle scope gains archetypes Leupold VX-3 (Vari-X III to VX-3HD), Trijicon ACOG, Swarovski Z8i, Zeiss Victory V8; LPVO, focal plane etc. as types. Red-dot sight gains Aimpoint CompM and EOTech HWS. New kind Night-vision and thermal sight (Pulsar Thermion/Talion/Digex). Vortex Viper PST Gen II kept as a model. No ATN ThOR: its press page was behind a paywall redirect. Scope mount has types only."}
p='work/E4/shelves/04_00.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
