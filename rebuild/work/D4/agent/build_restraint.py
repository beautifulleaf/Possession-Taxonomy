import json, os, sys
D = '/home/user/Possession-Taxonomy/rebuild/work/D4/shelves/'
AD = 'https://www.adorama.com/l/Photography/Lens-Filters'
S = {}
S['02_01'] = dict(kinds=[
 dict(n="Polarising filter", a="circular polariser · circular polarizer · CPL", d="Filter that cuts glare and reflections from water and glass and deepens blue skies.",
      t=["Screw-in circular polariser","Square or slot-system polariser","Magnetic polariser"], s="https://www.adorama.com/l/Photography/Lens-Filters/Polar-Pro~Polarizing-Filters"),
 dict(n="Neutral density filter", a="ND filter", d="Grey filter that cuts light evenly so you can use slower shutter speeds or wider apertures.",
      t=["Solid ND","Graduated ND","Variable ND","Screw-in","Square or slot system"], s=AD),
 dict(n="UV and clear protection filter", a="UV filter · haze filter · protector filter · clear filter", d="Clear or UV-blocking filter left on the lens to guard the front element.",
      t=["UV or haze filter","Clear protector","Screw-in","Magnetic"], s="https://www.adorama.com/l/Photography/Lens-Filters/Polar-Pro~Polarizing-Filters"),
 dict(n="Soft-effect filter", a="diffusion filter · mist filter · soft-focus filter", d="Filter that softens detail or adds glow around highlights.",
      t=["Mist","Diffusion","Soft focus","Star or cross-screen"], s=AD),
 dict(n="Close-up lens", a="close-up filter · dioptre", d="Simple magnifying element screwed onto a lens so it focuses closer.",
      t=["Single-element","Achromatic (two-element)"], m=[["Close-Up Lens 500D (77mm)","Canon"],["Close-Up lens +3","Hoya"]],
      s="https://gearfocus.com/products/canon-77mm-close-up-lens-500d-v0QmM")],
 notes="'Other lens filters' (k35) dissolved into the five specific kinds (its retailer source was an unrelated focal-reducer page, so not reused). Screw-in vs square/slot and solid/graduated/variable ND recorded as types. No models added: the brief's makers (B+W, Hoya, Kase, NiSi, Lee, PolarPro, Tiffen) have no models in the old data and this restraint shelf takes no new research.")
S['02_02'] = dict(kinds=[
 dict(n="Mount adapter", a="lens adapter", d="Ring with no optics that fits a lens of one mount to a body of another.",
      t=["Manual (no electronics)","Electronic smart adapter (AF and aperture control)"], m=[["Canon EF to Sony E T CINE Smart Adapter","Metabones"]], r=[["Smart Adapter","Metabones"]],
      s="https://www.lensrentals.com/buy/metabones-canon-ef-lens-to-sony-e-mount-t-cine-smart-adapter"),
 dict(n="Focal reducer", a="speed booster", d="Mount adapter with optics that shorten focal length and brighten the aperture while changing mounts.",
      m=[["Canon EF to Sony E Speed Booster T CINE Ultra","Metabones"],["EF-EOS M2 Speed Booster","Viltrox"]], r=[["Speed Booster","Metabones"]],
      s="https://www.photospecialist.ie/viltrox-ef-eos-m2-speed-booster-focal-reduc-12249630"),
 dict(n="Teleconverter", a="extender · tele-extender", d="Optical unit fitted between camera and lens that lengthens the focal length.",
      t=["1.4x","2x"], m=[["Extender EF","Canon"],["AF-S TC-14E II","Nikon"],["EC-20 (2x Zuiko Digital TeleConverter)","Olympus"],["Teleplus HD DGX 1.4x","Kenko"]], r=[["Teleplus HD DGX","Kenko"]],
      s="https://www.backscatter.com/Kenko-TELEPLUS-HD-DGX-1.4x-Teleconverter-Nikon"),
 dict(n="Extension tube", a="macro extension tube · bellows", d="Lensless spacer fitted between body and lens so the lens focuses closer.",
      t=["Extension tube","Bellows unit"], s="https://www.photospecialist.ie/viltrox-ef-eos-m2-speed-booster-focal-reduc-12249630")],
 notes="All four kinds kept; camera makers' own teleconverters listed first. Bellows recorded as a type of extension tube. No models added for Fotodiox or K&F: none in old data and no research on this restraint shelf.")
S['03_00'] = dict(kinds=[
 dict(n="Speedlight", a="flashgun · hot-shoe flash", d="Small battery flash that mounts on the camera hot shoe or a stand.",
      t=["Hot-shoe speedlight","Round-head flash","Mini flash"],
      m=[["Nikon SB-700 AF Speedlight","Nikon"],["Godox V1Pro","Godox"],["Godox V100","Godox"],["Godox TT685 II","Godox"],["Godox iT32","Godox"],["Godox Lux Master","Godox"],["Ricoh GF-2","Ricoh"],["Bolt VD-420","Bolt"]],
      r=[["V series round-head speedlights","Godox"],["Thinklite TT speedlights","Godox"],["iT and iM mini flashes","Godox"]],
      s="https://www.bhphotovideo.com/c/buy/On-Camera-Flashes/ci/647/cp/19539+989+1161+647"),
 dict(n="Studio flash", a="strobe · strobe head · monolight", d="Mains or battery flash for studio or location, sold as self-contained monolights or as a power pack with heads.",
      t=["Monolight","Battery location flash","Pack and head"],
      m=[["Profoto B10X Plus","Profoto"],["Profoto D30","Profoto"],["Profoto Pro-11","Profoto"],["Godox AD200Pro II","Godox"],["Godox AD600Pro II","Godox"],["Godox SK400II-V","Godox"],["Elinchrom ELB 500 TTL","Elinchrom"],["Westcott FJ400 II","Westcott"],["Broncolor Scoro S","broncolor"],["Hensel EH Pro Mini","Hensel"],["Flashpoint XPLOR 400PRO","Flashpoint"],["Godox AD400Pro II","Godox"]],
      r=[["B series OCF flash heads","Profoto"],["Witstro AD series (AD100Pro to AD800Pro)","Godox"],["ELB battery packs","Elinchrom"],["Scoro power packs","broncolor"]], s="")],
 notes="Godox SKU flood cut to one or two per line (speedlights 14->8 models, studio flash 39->12). Dropped older or duplicate generations (AD100Pro, AD200Pro, AD300Pro, AD600Pro, AD800Pro, TT350S, TT600, V1, IM20/IM30, iT30Pro), Impact, Neewer Q4, Speedotron, Photogenic and duplicate Profoto/Elinchrom/broncolor items; their lines remain as ranges. Ring light stays in Continuous lights as planned there (no ring-flash data to move). Studio flash had no old source, so s left empty.")
BH = "https://www.bhphotovideo.com/c/browse/more-light-modifiers/ci/57226/cp/19539+989+1161+57226"
AL = "https://www.adorama.com/l/Used/Photography/Lighting-and-Studio/Continuous-Lighting/LED-Lighting"
S['03_01'] = dict(kinds=[
 dict(n="LED panel", a="LED light panel", d="Flat panel of LEDs giving constant, broad light.", t=["Daylight","Bi-colour","RGB"],
      m=[["Litepanels Lykos","Litepanels"],["Litepanels Astra 6X","Litepanels"],["Ikan Onyx","Ikan"],["F&V K4000S","F&V Lighting"]], s=AL),
 dict(n="COB LED light", a="chip-on-board light · point-source LED", d="Single chip-on-board LED source, usually in a reflector or with a modifier mount.", t=["Daylight","Bi-colour","RGB"],
      m=[["amaran Ray 60c","Amaran"],["amaran Ray 120c","Amaran"],["amaran Ray 360c","Amaran"],["amaran Ray 660c","Amaran"],["Godox Litemons LA150R","Godox"],["Godox Litemons LA200D","Godox"],["Godox Litemons LA300R","Godox"]],
      r=[["Ray COB lights","Amaran"],["Litemons LED video lights","Godox"]], s="https://essentialphoto.co.uk/blogs/news/godox-for-the-film-and-tv-industry"),
 dict(n="LED tube light", a="light wand · light stick", d="Handheld or mountable LED tube or bar that gives constant light along its length.", s=AL),
 dict(n="Ring light", a="", d="Circular light made to surround the lens or face the subject.", m=[["Godox LR150 Air","Godox"]], s=AL),
 dict(n="Fresnel light", a="LED Fresnel", d="Constant light with a stepped Fresnel lens that focuses the beam from spot to flood.", t=["LED Fresnel","Tungsten Fresnel"],
      m=[["Godox F7-120","Godox"],["Godox F7-300R","Godox"],["Litepanels Sola 4+","Litepanels"],["Came-TV Boltzen","Came-TV"],["Dracast LED Fresnel","Dracast"],["Ikan Red Star","Ikan"]],
      r=[["Sola Fresnel lights","Litepanels"]], s="https://www.adorama.com/lists/fresnel-led-lights"),
 dict(n="Tungsten light", a="redhead · blonde · open-face light", d="Constant light with a tungsten-halogen lamp in an open-face housing.", t=["Redhead (about 800 W)","Blonde (about 2000 W)"],
      m=[["Arrilite 1000","ARRI"],["Tota-light","Lowel"]], s="https://www.adorama.com/clearance/l/Photography/Lighting-and-Studio/Continuous-Lighting/ARRI~Tungsten-Lighting")],
 notes="Dropped film-set-only models: Kino Flo Diva-Lite LED, Lupo Superpanel (LED panel); ARRI L10-C, ARRI L7-C, Mole-Richardson JuniorLED, Litepanels Studio X3, Litepanels SolaENG, Elation KL Fresnel (Fresnel). No Nanlite, Neewer or Elgato models added: none in old data and no research on this restraint shelf.")
S['03_02'] = dict(kinds=[
 dict(n="Softbox", a="strip box · octabox · speed ring", d="Fabric box with a diffusing front that softens a light placed inside it; fixed to the light with a speed ring.",
      t=["Rectangular","Strip box","Octabox","Parabolic","Lantern","Speed ring"], m=[["Glow ParaSnap","Glow"]],
      s="https://www.adorama.com/l/Photography/Lighting-and-Studio/Light-Modifiers-and-Reflectors"),
 dict(n="Umbrella", a="photo umbrella", d="Umbrella that bounces or, when translucent, diffuses a light.", t=["Reflective","Shoot-through","Parabolic"],
      m=[["Profoto Deep Umbrella","Profoto"],["Profoto Shallow Umbrella","Profoto"]], s="https://www.adorama.com/l/Photography/Lighting-and-Studio/Light-Modifiers-and-Reflectors"),
 dict(n="Portable reflector", a="collapsible reflector · collapsible diffuser · portable diffuser", d="Collapsible disc or panel that bounces or diffuses light.", t=["5-in-1 disc","Single-surface disc","Framed panel"],
      m=[["Westcott Illuminator","Westcott"]], s="https://www.adorama.com/l/Photography/Lighting-and-Studio/Light-Modifiers-and-Reflectors"),
 dict(n="Beauty dish", a="", d="Shallow dish with a central deflector that gives crisp, wrapping light.", m=[["Profoto Softlight Reflector","Profoto"],["Godox BDR-S55 Pro","Godox"],["Godox BDR-S550","Godox"]],
      s="https://www.camerapro.com.au/lighting/shop-by-category/lighting-accessories.html?p=8"),
 dict(n="Reflector dish", a="standard reflector", d="Metal bowl that directs light from a flash head.", m=[["Profoto TeleZoom Reflector","Profoto"],["Profoto SpillKill Reflector","Profoto"],["Godox BeamLight Max90","Godox"]],
      s="https://www.adorama.com/l/Photography/Lighting-and-Studio/Profoto~Light-Modifiers-and-Reflectors"),
 dict(n="Grid", a="honeycomb · egg-crate", d="Honeycomb or egg-crate that narrows and straightens a beam.", t=["Honeycomb grid","Softbox fabric grid"],
      m=[["Profoto Softgrid","Profoto"],["DoPchoice SnapGrid","DoPchoice"]], s="https://www.adorama.com/l/Photography/Lighting-and-Studio/Profoto~Light-Modifiers-and-Reflectors"),
 dict(n="Snoot", a="", d="Tube that narrows a light to a small circle.", m=[["Elinchrom Snoot 26425","Elinchrom"],["Godox Witstro Snoot AD-S9","Godox"],["Flashpoint Snoot Kit","Flashpoint"]],
      s="https://www.masterfoto.lv/en/barndoors-snoots-grids/17925-godox-witstro-snoot-met-grid.html"),
 dict(n="Barn doors", a="barndoors", d="Hinged flaps fitted to a light to cut and shape the beam.", t=["2-leaf","4-leaf"], m=[["Profoto 4-Leaf Barndoors","Profoto"],["Godox BD-100 Barndoor","Godox"]],
      s="https://www.camerapro.com.au/lighting/shop-by-category/lighting-accessories.html?p=8"),
 dict(n="Colour gel", a="gel · lighting filter", d="Coloured or colour-correction sheet fitted over a light.", t=["Effect colour","Colour correction"],
      m=[["Godox VSA-11C Color Effect Set","Godox"],["Flashpoint V-11C Color Effect Filter Set","Flashpoint"]], s="https://www.adorama.com/l/Photography/Lighting-and-Studio/Light-Modifiers-and-Reflectors"),
 dict(n="Gobo", a="", d="Pattern or shape cut-out placed in a beam to project a shadow or pattern.", m=[["Dedolight DP-1 Gobo Holder","Dedolight"],["Godox VSA-GS4 Gobo Set","Godox"]],
      s="https://www.adorama.com/l/Photography/Lighting-and-Studio/Godox~Light-Modifiers-and-Reflectors"),
 dict(n="Flag, net or overhead frame", a="flag · cutter · net · butterfly · overhead", d="Framed fabric or net set in front of or over a light or scene to block, cut or soften it.",
      t=["Flag","Cutter","Single net","Double net","Overhead frame (butterfly)"], s=BH)],
 notes="Generic shape names listed as models (Lantern softbox, Octabox, Parabolic softbox, Strip box, Parabolic umbrella, 5-in-1 reflector) moved to types. Speed ring merged into Softbox; Overhead frame merged into Flag, net or overhead frame.")
BHS = "https://www.bhphotovideo.com/c/buy/Lightstands/ci/5799/cp/19539+989+1161+5799"
S['03_03'] = dict(kinds=[
 dict(n="Light stand", a="C-stand · roller stand", d="Adjustable stand that carries a light or modifier.", t=["Standard light stand","Compact (nano) stand","C-stand","Roller stand"],
      m=[["Manfrotto Alu Master 1004BAC","Manfrotto"],["Manfrotto Nano Light Stand 5001B","Manfrotto"],["Matthews Century C+","Matthews"],["Matthews MERF","Matthews"]], s=BHS),
 dict(n="Boom arm", a="boom stand", d="Counterweighted arm that carries a light overhead.", m=[["Impact Combo Boom Stand","Impact"],["RedWing Boom Arm","RedWing"]], s=BHS),
 dict(n="Backdrop stand", a="background support", d="Stands and crossbar, or a frame, that hold a studio backdrop.",
      m=[["Manfrotto Free Standing Background Support System","Manfrotto"],["Manfrotto Solo Background Support System","Manfrotto"],["Savage Port-A-Stand","Savage"],["Westcott X-Drop Frame Stand","Westcott"],["Phottix Saldo Backdrop Stand","Phottix"],["Photoflex BackDrop Support Kit","Photoflex"],["Flashpoint Background Support System","Flashpoint"]],
      s="https://www.adorama.com/lists/heavy-duty-backdrop-stands"),
 dict(n="Studio backdrop", a="photo backdrop · background", d="Large sheet of paper, cloth or vinyl hung or stretched behind a subject.", t=["Paper roll","Muslin","Vinyl","Collapsible"],
      s="https://www.dbackdrop.com/collections/muslin-backdrop")],
 notes="Generic 'C-stand' and 'Roller stand' moved from models to types. Backdrop stand definition no longer points to Soft Furnishings, since Studio backdrop now sits on this shelf. No Avenger or Godox/Neewer stand models added: none in old data.")
CP = "https://www.camerapro.com.au/accessories/shop-by-category/tripods-monopods/heads-and-plates.html?p=2"
S['04_00'] = dict(kinds=[
 dict(n="Tripod", a="", d="Three-legged camera support, chosen by height, leg sections, weight and load.", t=["Full-size tripod","Travel tripod","Tabletop tripod","Aluminium","Carbon fibre"],
      m=[["Gitzo Systematic Series 3 (GT3543XLS)","Gitzo"],["Gitzo Traveler Series 1 (GT1555T)","Gitzo"],["Really Right Stuff Versa Apex","Really Right Stuff"],["Peak Design Travel Tripod","Peak Design"],["Manfrotto Befree Advanced","Manfrotto"],["Manfrotto 290 Xtra","Manfrotto"],["Manfrotto Element Traveller","Manfrotto"],["Benro Tortoise","Benro"],["Benro Adventure","Benro"],["FLM CP30-L4","FLM"],["3Pod Orbit","3Pod"]],
      r=[["Befree travel tripods","Manfrotto"],["Tortoise columnless carbon tripods","Benro"],["VEO","Vanguard"]], s=""),
 dict(n="Tripod head", a="", d="Separate head that mounts on a tripod or monopod and holds the camera.", t=["Ball head","3-way (pan-and-tilt) head","Fluid head","Geared head","Gimbal head","Panoramic head"],
      m=[["Manfrotto 500X Fluid Head","Manfrotto"],["Benro GH5C","Benro"],["Leofoto G20 Geared Panoramic Head","Leofoto"],["Sirui PH-30","Sirui"],["Wimberley WH-200","Wimberley"],["ProMediaGear Katana","ProMediaGear"],["Sunwayfoto GH-02","Sunwayfoto"],["Slik SGH-300","Slik"]], s=CP),
 dict(n="Monopod", a="", d="Single-leg camera support.", m=[["Leofoto MPC-366CL","Leofoto"]], s="https://thecamerastore.com/collections/tripods-heads?page=1"),
 dict(n="Quick-release plate", a="quick-release system · L-bracket", d="Plate, L-bracket or collar that lets a camera or lens click on and off a support.", t=["Arca-type plate","Proprietary plate","L-bracket","Clamp"],
      m=[["Manfrotto 200PL-Pro","Manfrotto"],["PGYTECH Arca-Type Quick Release Clamp and Plate","PGYTECH"]], s=CP)],
 notes="Generic head names (3-way, ball, fluid, geared, gimbal head) and 'L-bracket' moved from models to types. Tripods trimmed 17->11 (dropped 3Pod Everest, 3Pod TREK, Benro Slim, Benro Tripster, Manfrotto Befree Live, Manfrotto ONE). Tripod had no old source, so s left empty.")
SR = "https://www.adorama.com/l/Video/Video-Stabilizers-and-Supports/Supports-and-Rigs"
S['04_01'] = dict(kinds=[
 dict(n="Handheld gimbal", a="handheld gimbal stabiliser", d="Motorised handheld stabiliser that keeps a camera level while moving.", m=[["DJI RS 2","DJI"],["DJI RS 4 Mini","DJI"],["Zhiyun WEEBILL 5","Zhiyun"]],
      s="https://www.adorama.com/l/Video/Video-Stabilizers-and-Supports"),
 dict(n="Camera cage", a="", d="Frame that fits around a camera body and gives it mounting points.", s="https://adorama.com/lists/camera-shoulder-rigs"),
 dict(n="Camera rig", a="shoulder rig", d="Shoulder or frame system that carries a camera with accessories.", t=["Shoulder rig","Chest or pocket rig"],
      m=[["SmallRig HawkLock Shoulder Rig Pro SR007","SmallRig"],["Tilta Tiltaing Lightweight Shoulder Rig","Tilta"],["edelkrone PocketRIG v2","edelkrone"],["Zacuto Recoil Rig","Zacuto"]], s=SR),
 dict(n="Camera clamp", a="camera mount · magic arm · super clamp", d="Clamp or arm that fixes a camera to a pole, rail, window or vehicle.", m=[["Manfrotto Super Clamp","Manfrotto"],["Manfrotto Magic Arm","Manfrotto"],["Manfrotto Variable Friction Arm 244","Manfrotto"]],
      s="https://www.adorama.com/l/Photography/Lighting-and-Studio/Light-Stands-and-Mounting/Grips-comma-Clamps-and-Arms/Manfrotto~Arms"),
 dict(n="Camera slider", a="", d="Short rail with a carriage that slides a camera in a straight line.", t=["Manual","Motorised"],
      m=[["MoveOver8B","Benro"],["P1 Carbon Slider","Konova"],["Magic Carpet","Syrp"],["ALX S4","Libec"],["Hot Dog Carbon Fiber Slider","YC Onion"]], s="https://www.bhphotovideo.com/c/buy/camera-sliders-accessories/ci/21012/pn/3"),
 dict(n="Camera dolly", a="", d="Wheeled platform or track dolly that moves a camera smoothly during a shot.", m=[["DollyONE v2","edelkrone"],["SYL-960","Glide Gear"],["Swift Camera Track Dolly","Proaim"]],
      s="https://www.bhphotovideo.com/c/buy/Track-Cine-Dollies-Accessories/ci/3931/N/3907816545"),
 dict(n="Camera crane", a="jib", d="Counterweighted arm on a stand that raises, lowers and swings a camera.", m=[["JibONE v3","edelkrone"],["JB40","Libec"],["Comet","Proaim"]],
      s="https://www.bhphotovideo.com/c/buy/Cranes-Jibs/ci/3917/N/3907816541/pn/3"),
 dict(n="Body-worn camera support", a="Easyrig · Steadicam", d="Vest with a spring arm or overhead strut that moves a camera's weight onto the operator's body.", s=SR)],
 notes="Generic 'Shoulder rig' moved from models to types. Body-worn support kept kind-level with no models as the brief says. All other old models are consumer or prosumer and within limits, so kept.")
DC = "https://www.adorama.com/l/Photography/Film-and-Darkroom-Equipment/Darkroom-Chemicals"
S['05_01'] = dict(kinds=[
 dict(n="Developing tank", a="daylight developing tank", d="Light-tight tank in which film is processed after loading.", t=["Plastic","Stainless steel","Rotary drum"],
      m=[["Paterson Super System 4","Paterson"],["Jobo Expert Drum","Jobo"],["Arista Premium Double Reel Tank","Arista"],["Arista Classic Double Reel Tank","Arista"]],
      r=[["Super System 4 tanks and reels","Paterson"],["1500 Series","Jobo"],["2500 Series","Jobo"]], s="https://crkphotoimaging.com.au/printing-film/darkroom/_price_range_search/200_0/_brands/paterson"),
 dict(n="Developing reel", a="spiral", d="Spiral reel that holds film inside a developing tank.", t=["Plastic auto-load","Stainless steel"],
      m=[["Paterson Auto Load Adjustable Reel","Paterson"],["Jobo Duo Set Adjustable Reel","Jobo"],["Hewes Pro Stainless Steel Reel","Hewes"],["AGO Processor Reel","AGO"],["ARS-IMAGO LAB-BOX Reel","ARS-IMAGO"]],
      r=[["Super System 4 tanks and reels","Paterson"],["1500 Series","Jobo"],["2500 Series","Jobo"]], s="https://www.freestylephoto.com/category/287-Darkroom/Darkroom-Accessories/Tanks-and-Reels?max=96"),
 dict(n="Changing bag", a="", d="Light-proof bag for loading film into a tank in daylight.", m=[["Paterson Changing Bag PTP125","Paterson"]], s="https://www.adorama.com/paptp125.html"),
 dict(n="Film developer", a="", d="Developer for black-and-white film, sold as liquid concentrate or powder.", t=["Liquid concentrate","Powder"],
      m=[["Ilford ID-11","Ilford"],["Ilford Ilfotec DD-X","Ilford"],["Ilford Ilfosol 3","Ilford"],["Ilford Perceptol","Ilford"],["Ilford Phenisol","Ilford"]], s=DC),
 dict(n="Stop bath and fixer", a="stop bath · fixer · hypo · photographic chemistry", d="Process chemistry after the developer: stop bath, fixer and related baths, plus colour process kits.",
      t=["Stop bath","Fixer","Hypo clear","Wetting agent","C-41 colour kit","E-6 slide kit"],
      m=[["Ilford Ilfostop","Ilford"],["Ilford Rapid Fixer","Ilford"],["Ilford Hypam","Ilford"],["Arista Premium Odorless Stop Bath","Arista"],["Arista Premium Odorless Rapid Fixer","Arista"],["Ilford Simplicity","Ilford"]],
      r=[["Ilford film and paper chemistry","Ilford"]], s=DC),
 dict(n="Darkroom thermometer", a="", d="Thermometer for checking chemistry temperature in film and print processing.", m=[["PTP381 Color Thermometer","Paterson"]],
      s="https://www.glazerscamera.com/collections/film-darkroom/products/patterson-thermometer-30cm"),
 dict(n="Darkroom graduate", a="measuring cylinder", d="Measuring cylinder or jug for mixing photographic chemistry.", m=[["Plastic Graduate","Paterson"]],
      s="https://www.glazerscamera.com/collections/film-darkroom/products/graduate-5-oz-150-ml"),
 dict(n="Film dryer", a="film drying cabinet", d="Cabinet or heated unit that dries developed film hanging in strips.", m=[["Mistral 3","Jobo"]],
      s="https://cinestillfilm.com/products/jobo-mistral-3-kit-roll-film-drying-cabinet-with-dryer")],
 notes="Stop bath, Fixer and the 'Other photographic chemistry' catch-all merged into Stop bath and fixer with types. No models dropped. No Kodak or CineStill chemistry added: none in old data and no research on this restraint shelf.")
FS = "https://www.freestylephoto.com/category/18-Darkroom/Enlargers-and-Accessories?page=6"
CRK = "https://crkphotoimaging.com.au/printing-film/darkroom/_price_range_search/200_0/_brands/paterson"
S['05_02'] = dict(kinds=[
 dict(n="Enlarger", a="photographic enlarger", d="Darkroom projector that exposes a negative onto paper.", t=["Condenser","Diffusion","Colour (dichroic) head","35 mm","Medium format","Large format"],
      m=[["Beseler 23CIII-XL","Beseler"],["Beseler 45MXT","Beseler"],["Beseler 67XL","Beseler"],["Beseler Printmaker 67 VC","Beseler"]], r=[["Printmaker enlargers","Beseler"]],
      s="https://www.adorama.com/l/Photography/Film-and-Darkroom-Equipment/Enlargers-and-Accessories/Beseler~Enlargers"),
 dict(n="Enlarging lens", a="", d="Lens made to project a negative sharply in an enlarger.", m=[["Schneider Componon-S","Schneider Kreuznach"]], s="https://www.adorama.com/sr5028cns.html"),
 dict(n="Negative carrier", a="", d="Frame that holds a negative flat in an enlarger, made per enlarger and format.", t=["Glassless","Glass"], s=FS),
 dict(n="Enlarging easel", a="", d="Frame that holds paper flat under an enlarger and sets the borders.", t=["Bladed easel","Multi-size (4-in-1) easel","Quick (speed) easel"],
      m=[["Arista 4-in-1 Enlarging Easel","Arista"]], s="https://www.freestylephoto.com/darkroom-supply-list"),
 dict(n="Focus finder", a="grain focuser", d="Magnifier used to focus the projected grain under an enlarger.", m=[["Paterson Major Focus Finder","Paterson"],["LegacyPro 10x Grain Focuser","LegacyPro"]], s=CRK),
 dict(n="Darkroom timer", a="enlarger timer", d="Timer that switches the enlarger or times process steps.", t=["Enlarger timer","Process timer"],
      m=[["GraLab 300","GraLab"],["GraLab 451R","GraLab"],["Paterson Digital Timer","Paterson"],["Kaiser Digital Darkroom Exposure Timer","Kaiser"],["Beseler Digital Darkroom Timer 8197","Beseler"],["CatLABS Universal Digital Darkroom Enlarger Timer","CatLABS"],["CatLABS Tank Top Timer","CatLABS"],["Time-O-Lite GR-90","Time-O-Lite"],["Time-O-Lite M-72R","Time-O-Lite"]],
      s="https://www.freestylephoto.com/category/244-Darkroom/Enlargers-and-Accessories/Timers"),
 dict(n="Enlarger filter", a="multigrade filter · variable-contrast filter", d="Contrast or colour filter used in or under the enlarger.", t=["Multigrade (variable-contrast)","Colour printing"],
      m=[["Ilford Multigrade Filter Set","Ilford"]], s=FS),
 dict(n="Contact printing frame", a="proof printer", d="Glass-topped frame that holds negatives against paper for contact sheets.", s=CRK),
 dict(n="Photographic paper", a="printing paper · enlarging paper", d="Light-sensitive paper for prints.", t=["Fibre-based","Resin-coated","Variable contrast","Graded","Colour (RA-4)","Inkjet photo paper"],
      m=[["Ilford Multigrade V RC Deluxe","Ilford"],["Ilford Multigrade FB Classic","Ilford"],["Ilford Multigrade RC Warmtone","Ilford"],["Ilford Multigrade Art 300","Ilford"],["Foma Fomaspeed Variant III","Foma"],["Arista EDU Ultra VC","Arista"],["Fujicolor Crystal Archive Type II","Fujifilm"]],
      r=[["Multigrade papers","Ilford"]], s="https://www.adorama.com/l/photography/film-and-darkroom-equipment/enlarging-paper"),
 dict(n="Paper developer", a="print developer", d="Developer for black-and-white printing paper.", m=[["Ilford Multigrade Paper Developer","Ilford"],["Ilford Bromophen","Ilford"],["Arista Premium Liquid Paper Developer","Arista"]], s=DC),
 dict(n="Developing tray", a="print tray", d="Shallow tray for print chemistry.", m=[["Cesco Dimpled Bottom Developing Tray","Cesco"]], s="https://www.freestylephoto.com/category/292-Darkroom/Darkroom-Accessories/Trays"),
 dict(n="Print tongs", a="", d="Tongs for moving prints between trays without touching the chemistry.", m=[["Print Tongs PTP341","Paterson"]], s="https://parallaxphotographic.coop/?p=6034"),
 dict(n="Safelight", a="", d="Darkroom lamp whose colour does not fog paper.", t=["LED","Filtered bulb"],
      m=[["Paterson Red Dome Safelight","Paterson"],["ARS-IMAGO LED Darkroom Safelight","ARS-IMAGO"],["LegacyPro Safelight 5.5x6.5","LegacyPro"],["Arista Darkroom Safelight","Arista"]],
      s="https://www.freestylephoto.com/category/194-Darkroom/Darkroom-Equipment/Safelights"),
 dict(n="Print washer", a="archival washer", d="Tank or archival washer that removes fixer from prints with running water.", s="https://www.bhphotovideo.com/c/browse/Developing-Processing/ci/568/N/4077265344"),
 dict(n="Print dryer", a="drying rack", d="Rack, screen or heated unit for drying prints.", m=[["Paterson Rapid Print Drying Rack","Paterson"]], s=CRK)],
 notes="Generic 'Bladed easel' and 'Quick easel' moved from models to types. Enlarger models trimmed 6->4 (dropped Beseler Cadet II and Printmaker 35) to cut single-maker skew; no Durst or Kaiser enlargers added because none are in the old data and this restraint shelf takes no research. Paper types fibre, resin-coated, colour and inkjet recorded.")
CB = "https://www.adorama.com/l/Photography/Photography-Bags-and-Cases/Camera-Bags-and-Cases"
S['06_00'] = dict(kinds=[
 dict(n="Camera bag", a="camera case · shoulder bag · sling bag · waist pack", d="Padded bag or case made to carry a camera and lenses.",
      t=["Shoulder bag","Messenger","Sling","Waist pack","Hard case","Insert"],
      m=[["Domke F-5XB","Domke"],["Lowepro Adventura TLZ","Lowepro"]],
      r=[["Retrospective","Think Tank"],["DarkLight","Think Tank"],["DNA","Tenba"],["Roadie","Tenba"],["VEO","Vanguard"]], s=CB),
 dict(n="Camera backpack", a="", d="Backpack with padded dividers for a camera body and lenses.", m=[["Think Tank Airport Accelerator","Think Tank"],["Shimoda Action X","Shimoda"]], s=CB),
 dict(n="Rolling camera case", a="roller bag", d="Wheeled case with a pull handle for a large camera kit.", s=CB),
 dict(n="Camera strap", a="camera sling strap · harness", d="Strap, sling or harness that carries a camera on the body.", t=["Neck strap","Shoulder or sling strap","Wrist strap","Harness"],
      m=[["Op/Tech Super Classic Strap","Op/Tech USA"],["PGYTECH Camera Shoulder Strap Air","PGYTECH"],["Cotton Carrier Skout G2 Sling Harness","Cotton Carrier"],["Fab F8 Rope Camera Strap","Fab"],["Nikon AC-DN25","Nikon"]],
      s="https://thecamerastore.com/collections/camera-straps")],
 notes="'Other camera bags and cases', Camera shoulder bag, Camera sling bag and Camera waist pack merged into Camera bag with types. No Peak Design, Billingham or Wandrd models added: none in old data and no research on this restraint shelf.")
S['06_01'] = dict(kinds=[
 dict(n="Camera battery and charger", a="camera battery · battery charger", d="Rechargeable battery made for a camera, and the charger that charges it.", t=["Maker's own battery","Third-party battery","Single charger","Dual charger","USB charger"],
      s="https://www.adorama.com/l/Photography/Camera-Accessories/Camera-Batteries"),
 dict(n="Battery grip", a="vertical grip", d="Grip that adds a second battery and vertical controls to a camera body.", m=[["Canon BG-E20","Canon"],["Sony VG-C4EM","Sony"]], s="https://www.adorama.com/lists/camera-with-battery-grip"),
 dict(n="Remote shutter release", a="cable release · remote control", d="Cable, infrared or wireless release that fires a camera without touching it.", t=["Mechanical cable release","Electronic cable release","Wireless or infrared remote","Intervalometer"],
      m=[["Nikon MC-36A","Nikon"],["Nikon MC-DC3","Nikon"],["Sony RMT-DSLR2","Sony"],["Leica RC-SCL6","Leica"],["Kaiser Shutter Release Cord","Kaiser"],["Flashpoint Wave Commander II","Flashpoint"]],
      s="https://www.adorama.com/l/Photography/Camera-Accessories/Remote-Controls"),
 dict(n="Light meter", a="exposure meter · flash meter", d="Handheld meter that measures light to set exposure.", t=["Selenium cell","CdS","Spot meter","Flash meter","Incident and reflected"],
      m=[["Sekonic L-308X","Sekonic"],["Sekonic L-858D-U Speedmaster","Sekonic"],["Sekonic LiteMaster Pro L-478D","Sekonic"],["Sekonic L-398A Studio Deluxe III","Sekonic"],["Gossen Digiflash","Gossen"],["Gossen Mavo-Spot 2 USB","Gossen"],["Kenko KFM-1100","Kenko"]],
      r=[["LiteMaster Pro light meters","Sekonic"]], s="https://www.adorama.com/l/Photography/Camera-Accessories/Light-Meters"),
 dict(n="Viewfinder or eyepiece", a="external viewfinder · LCD loupe", d="Add-on viewfinder, eyepiece or screen magnifier fitted to a camera.", t=["Optical external finder","Electronic viewfinder","LCD loupe","Eyecup or magnifier"],
      m=[["Leica Visoflex 2","Leica"],["Ricoh GV-2","Ricoh"],["Ricoh GV-3","Ricoh"],["Sigma LVF-11","Sigma"],["TTArtisan 35mm External Optical Viewfinder","TTArtisan"],["Zacuto Z-Finder","Zacuto"],["Hoodman Live View Kit","Hoodman"],["Kinotehnik LCD Viewfinder","Kinotehnik"]],
      s="https://www.adorama.com/lists/external-viewfinders"),
 dict(n="Focusing screen", a="ground glass", d="Interchangeable ground-glass screen fitted in a camera's viewfinder.", t=["Plain matte","Split-image","Grid"], m=[["Type E","Nikon"],["ML-60","Pentax"]],
      s="https://www.bhphotovideo.com/c/buy/Focusing-Screens/ci/290")],
 notes="Camera battery and Battery charger merged. Light meters trimmed to Sekonic, Gossen and Kenko (dropped AstrHori AH-M1 and TTArtisan Light Meter II); classic meter types recorded as types. No Reveni model added: none in old data.")
S['06_02'] = dict(kinds=[
 dict(n="Lens hood and cap", a="lens hood · lens shade · lens cap", d="Shade that fits the front of a lens, and caps that cover its front or rear.", t=["Petal hood","Round hood","Front cap","Rear cap","Body cap"],
      s="https://thecamerastore.com/collections/lens-accessories/category_lens-hoods"),
 dict(n="Camera cleaning kit", a="sensor cleaning kit", d="Kit of swabs, blowers, brushes or fluid for cleaning a lens or sensor.", t=["Lens cleaning","Sensor swabs","Blower"],
      m=[["Visible Dust EZ Sensor Cleaning Kit","Visible Dust"],["Photographic Solutions Swab Ultra","Photographic Solutions"],["Pentax O-ICK1 Image Sensor Cleaning Kit","Pentax"]], s="https://www.adorama.com/lists/camera-sensor-cleaning-kits"),
 dict(n="Screen protector", a="camera screen protector", d="Film or glass sheet cut to protect one camera's rear screen.", t=["Tempered glass","Film"], m=[["SR5803","SmallRig"]], s="https://www.adorama.com/SR5803.html"),
 dict(n="Underwater housing", a="dive housing", d="Waterproof case made for a camera so it can be used underwater.", t=["Hard housing","Soft waterproof bag"],
      m=[["Ikelite 200DL","Ikelite"],["Ikelite 200DLM","Ikelite"],["OM SYSTEM PT-059","OM System"],["Sony MPK-HSR1","Sony"],["Ricoh TW-2","Ricoh"],["DiCAPac Waterproof Case","DiCAPac"]],
      r=[["200DL underwater housings","Ikelite"]], s="https://www.adorama.com/l/Photography/Underwater-Photography/Underwater-Camera-Housings"),
 dict(n="Camera dry cabinet", a="dry box", d="Humidity-controlled cabinet for storing cameras and lenses against fungus.", m=[["HC70","Sirui"]], s="https://store.sirui.com/products/hc-series")],
 notes="Lens hood and Lens cap merged. Underwater housings kept (6 models within limits); no Nauticam, Sea & Sea or Aquatech models added because none are in the old data and this restraint shelf takes no research.")
for j in sys.argv[1:]:
    o = dict(kinds=S[j]['kinds'], brands=[], traditions=[], notes=S[j]['notes'])
    p = D + j + '.json'; tmp = p + '.tmp'
    if os.path.exists(p): print('exists, skip', j); continue
    json.dump(o, open(tmp, 'w'), ensure_ascii=False, indent=1); os.replace(tmp, p); print('wrote', j)
