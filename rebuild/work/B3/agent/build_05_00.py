import json, os
U = dict(
    sf_story="https://www.surefire.com/surefire-story/",
    sf_wiki="https://en.wikipedia.org/wiki/SureFire",
    mag="https://en.wikipedia.org/wiki/Maglite",
    fl="https://en.wikipedia.org/wiki/Flashlight",
    tac="https://en.wikipedia.org/wiki/Tactical_light",
    dive="https://en.wikipedia.org/wiki/Dive_light",
    sl="https://en.wikipedia.org/wiki/Streamlight",
    fulton="https://en.wikipedia.org/wiki/Fulton_MX991/U_Flashlight",
    kel="https://en.wikipedia.org/wiki/Kel-Lite",
    d4="https://1lumen.com/review/emisar-d4v2/",
    zl="https://zeroair.org/2021/06/11/zebralight-sc700d-flashlight-review/",
    ok="https://zeroair.org/2017/10/27/okluma-dc1-brass-custom-flashlight-review/",
    mdc="https://www.thefirearmblog.com/blog/2013/04/02/malkoff-mdc-daily-carry-ha-aa-light/",
    s2="https://1lumen.com/review/convoy-s2/",
    baton="https://1lumen.com/review/olight-baton-4",
    pd35="https://1lumen.com/review/fenix-pd35-v3",
    edc27="https://1lumen.com/review/nitecore-edc27/",
    stinger="https://www.shootingillustrated.com/content/streamlight-introduces-stinger-classic-led",
    l19="https://1lumen.com/review/acebeam-l19/",
    sp40="https://1lumen.com/review/sofirn-sp40",
    aeon="https://zeroair.org/?p=49866",
    protac="https://www.officer.com/tactical/flashlights/product/12301061/streamlight-inc-dual-fuel-tactical-lights",
    warrior="https://1lumen.com/review/olight-warrior-3s/",
    tm="https://1lumen.com/review/nitecore-tm12k/",
    g2x="https://www.thegearbunker.com/surefire-g2x-tactical-flashlight-review/",
    seeker="https://1lumen.com/review/olight-seeker-4-pro",
    waypoint="https://www.officer.com/investigations/portable-lighting/product/12052114/streamlight-inc-waypoint-pistolgrip-spotlights",
)
def V(n, mk="", y="", d=""):
    o = {"n": n}
    if mk: o["mk"] = mk
    if y: o["y"] = y
    if d: o["d"] = d
    return o
def X(n, d, mk, y, s, v=(), dt="", a=""):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": U[s], "v": list(v), "dt": dt}

edc = {"n": "EDC flashlight", "a": "everyday-carry torch · pocket torch · flashlight",
 "d": "Pocket-sized hand torch carried daily, usually on one rechargeable or primary cell, with a clip and several output modes.",
 "t": ["AA / AAA", "14500 / 16340 / 18350", "18650 / 21700", "built-in battery", "flat body", "tail clicky", "side e-switch", "titanium / copper / brass body"],
 "s": "https://zips.com/shop-by-brand/streamlight",
 "x": [
  X("Mini Maglite", "First personal-size Maglite: a slim aluminium torch on two AA cells, the mass-market pocket torch.", "Maglite", "1984", "mag",
    [V("Mini Maglite 2AA (incandescent)", "Maglite", "1984"), V("Mini Maglite LED 2AA", "Maglite", "2006"),
     V("Mini Maglite AA Pro / AA Pro+", "Maglite", "2012", "215 / 245 lumens"), V("Mini Maglite LED 2 AAA", "Maglite", "2012")],
    "battery 2AA / 2AAA · incandescent or LED · anodised colours"),
  X("Zebralight SC series", "Compact side-switch lights with a short body, neutral high-CRI emitters and a programmable e-switch interface.", "Zebralight", "", "zl",
    [V("SC700d", "Zebralight", "2021", "21700, Cree XHP70.2, 90+ CRI"), V("SC700fd", "Zebralight", "", "floodier SC700d"),
     V("SC600w III HI", "Zebralight"), V("SC600Fd Mk III", "Zebralight"), V("SC64c", "Zebralight")],
    "cell 18650 / 21700 · flood (f) or spot · neutral (w) or high-CRI (c/d)"),
  X("Emisar D4", "Short, powerful quad-emitter enthusiast light by Hank (Emisar); D4V2 runs the community Anduril firmware with aux LEDs.", "Emisar", "", "d4",
    [V("D4", "Emisar", "", "original; RampingIOS firmware"), V("D4V2", "Emisar", "2020", "Anduril firmware, aux LEDs, new knurling"), V("D4K", "Emisar")],
    "18650 / 21700 · emitter choice (SST-20, 219C, XPL-HI) · CCT and CRI · anodised or metal bodies"),
  X("Olight Baton", "Tiny side-switch light on a proprietary cell, charged magnetically or in a case; Olight's best-known EDC line.", "Olight", "", "baton",
    [V("Baton 4", "Olight", "2023", "16340, 1,300 lumens; Premium Edition with charging case"), V("Baton 3", "Olight"), V("Baton 3 Pro Max", "Olight"),
     V("Baton 4 Pro", "Olight"), V("Baton Turbo", "Olight"), V("Baton Ultra", "Olight"), V("S2 Baton", "Olight")],
    "cell 16340 / 18650 / 21700 · colours and limited editions · Premium charging case"),
  X("Fenix PD35", "18650 tactical-EDC light with rear forward clicky and side mode switch; the reference mid-size Fenix.", "Fenix", "2013", "pd35",
    [V("PD35", "Fenix", "2013", "Cree XM-L2, ~850 lumens"), V("PD35 Tactical Edition (PD35TAC)", "Fenix", "2015", "Cree XP-L, 1,000 lumens"),
     V("PD35 V2.0", "Fenix", "2018", "cosmetic update"), V("PD35 V3.0", "Fenix", "2021", "Luminus SFT40, 1,700 lumens")],
    "18650 or 2×CR123A · cool white · holster and clip"),
  X("Olight Seeker", "Larger 21700 outdoor/EDC light with a rotary dial for stepless output and magnetic holster charging.", "Olight", "", "seeker",
    [V("Seeker 4 Pro", "Olight", "2023", "4,600 lumens, rotary dial"), V("Seeker 3 Pro", "Olight", "", "predecessor with proximity sensor"),
     V("Seeker 4", "Olight"), V("Seeker 4 Mini", "Olight"), V("Seeker Ultra", "Olight")],
    "cool or neutral white · colours"),
  X("Nitecore EDC series", "Flat, slim built-in-battery EDC lights with an OLED status screen and very high burst output.", "Nitecore", "2023", "edc27",
    [V("EDC27", "Nitecore", "2023", "3,000 lumens, flat body, OLED"), V("EDC27 UHi", "Nitecore"), V("EDC29", "Nitecore"),
     V("EDC33", "Nitecore"), V("EDC35", "Nitecore"), V("EDC37", "Nitecore")],
    "built-in Li-ion · flat body · clip"),
  X("Convoy S2+", "Inexpensive 1×18650 tail-clicky light sold with many emitters; the standard host for modding.", "Convoy", "", "s2",
    [V("S2+ (SST20)", "Convoy"), V("S2+ Nichia 519A", "Convoy"), V("S2+ MAO", "Convoy", "", "micro-arc oxidation finish")],
    "emitter (SFT40, SST20, 519A, XPL-HI, LH351D…) · driver · anodised colours"),
  X("Okluma DC1", "Small-batch machined 18350 triple-optic custom light; flagship of the custom EDC scene.", "Okluma", "", "ok",
    [V("DC1 aluminium", "Okluma"), V("DC1 brass", "Okluma", "2017", "Nichia 219C, Carclo 10507 optic")],
    "aluminium, brass and other metals · optic spot or flood · programmable driver option"),
  X("Malkoff MDC", "'Malkoff Daily Carry': potted, American-made lights built around Malkoff's M61-family light engines.", "Malkoff Devices", "", "mdc",
    [V("MDC HA AA", "Malkoff Devices", "2013", "AA / 14500, hard-anodised, three modes")],
    "battery AA / CR123 / 18650 · hard anodised or colours"),
  X("Muyshondt Aeon", "Tiny luxury CR2 light with reverse clicky, made in aluminium, titanium and copper.", "Muyshondt", "", "aeon",
    [V("Aeon Mk III", "Muyshondt", "2021", "CR2, Nichia 219b"), V("Aeon (twisty, Mk I/II)", "Muyshondt")],
    "aluminium (black, indigo), titanium, copper"),
 ],
 "m": [["P7R", "Ledlenser"], ["P9R", "Ledlenser"], ["P5", "Ledlenser"], ["P4", "Ledlenser"], ["P3", "Ledlenser"], ["MT10", "Ledlenser"], ["MT14", "Ledlenser"], ["T7M", "Ledlenser"],
       ["E2L", "SureFire"], ["Stiletto", "SureFire"], ["Wedge", "Streamlight"], ["MacroStream", "Streamlight"], ["MicroStream", "Streamlight"],
       ["Arkfeld", "Olight"], ["Arkfeld Pro", "Olight"], ["Arkfeld Ultra", "Olight"], ["i3T 2 EOS", "Olight"], ["i5R", "Olight"], ["Prowess", "Olight"],
       ["LD15R", "Fenix"], ["E40R", "Fenix"], ["PD36R V2.0", "Fenix"], ["PD40R", "Fenix"], ["MT2A Pro", "Nitecore"],
       ["Mini MLR2", "Foursevens"], ["Archer 2A V3", "ThruNite"], ["SC31Pro", "Sofirn"], ["TS10 V2", "Wurkkos"], ["C3", "WUBEN"],
       ["Pokelit AA", "Acebeam"], ["Rider RX", "Acebeam"], ["XL100", "Maglite"], ["XL200", "Maglite"], ["HX5 Pure Beam", "Coast Products"], ["F30 Pro", "VARTA"], ["GatLight", "Lumencraft"]],
 "r": [["P series", "Ledlenser"], ["Arkfeld", "Olight"], ["XL series", "Maglite"]],
}

tactical = {"n": "Tactical flashlight", "a": "tactical torch · combat light · weapon light",
 "d": "Rugged high-output torch with a momentary tail switch for use with a firearm or for self-defence; includes weapon-mounted lights.",
 "t": ["handheld", "weapon-mounted (pistol / long gun)", "dual-fuel CR123A / 18650", "two-stage tail switch", "strobe"],
 "s": U["tac"],
 "x": [
  X("SureFire 6P", "Compact 2×CR123A high-intensity torch with push-button tailcap; it created the premium tactical-light market.", "SureFire", "1988", "sf_story",
    [V("6C", "SureFire", "1988", "first compact 60-lumen light, 4.6 in"), V("6P", "SureFire", "1988", "adds push-button tailcap"),
     V("6Z", "SureFire", "1997", "first CombatGrip")], "incandescent or LED drop-in · black anodised"),
  X("SureFire WeaponLight", "Dedicated light mounted on a handgun or long gun, begun with SureFire's Model 310 for the Colt 1911.", "SureFire", "1985", "sf_story",
    [V("Model 310 / 610", "SureFire", "1985", "3 V / 6 V lights for the Colt 1911A1"), V("300 series", "SureFire", "", "the 'patriarch' WeaponLight with tape switch"),
     V("X300", "SureFire", "", "best-selling handgun light"), V("Scout Light (M600)", "SureFire", "", "long-gun light family")],
    "pistol rail or long-gun mount · tape or tail switch"),
  X("SureFire M6 Guardian", "Large xenon handheld whose 500-lumen output set a new standard for tactical lights.", "SureFire", "2000", "sf_story",
    [V("M6", "SureFire", "2000", "500 lumens")], "250 / 500-lumen lamp assemblies"),
  X("SureFire Z2 CombatLight", "Handheld light with CombatGrip ring, issued to the FBI and the Federal Air Marshal Service.", "SureFire", "", "sf_wiki", [], ""),
  X("SureFire G2X", "Light Nitrolon-bodied 2×CR123A tactical torch, the affordable SureFire.", "SureFire", "", "g2x",
    [V("G2X Tactical", "SureFire", "", "single 600-lumen mode"), V("G2X Pro", "SureFire", "", "15 / 600-lumen dual output")], "Nitrolon body colours"),
  X("Streamlight ProTac", "Streamlight's family of tactical tail-switch lights; X models are 'dual fuel' (2×CR123A or 18650).", "Streamlight", "", "protac",
    [V("ProTac HL-X", "Streamlight", "2017", "1,000 lumens, dual fuel"), V("ProTac 2L-X", "Streamlight", "2017", "500 lumens, dual fuel"),
     V("ProTac 2L-X USB", "Streamlight"), V("ProTac HL", "Streamlight"), V("ProTac 1L-X", "Streamlight"), V("ProTac 1L-1AA", "Streamlight"),
     V("ProTac 2AA-X", "Streamlight"), V("ProTac 2.0", "Streamlight"), V("ProTac 5-X", "Streamlight"), V("ProTac 90", "Streamlight"), V("ProTac 90X", "Streamlight")],
    "battery CR123A / 18650 / AA · black or coyote"),
  X("Olight Warrior", "Olight's tactical line with a two-stage tail switch, side switch and magnetic charging.", "Olight", "", "warrior",
    [V("Warrior 3S", "Olight", "2022", "21700, 2,300 lumens"), V("Warrior 3", "Olight", "", "predecessor"), V("Warrior M2R Pro", "Olight"),
     V("Warrior X 3", "Olight"), V("Warrior X 4", "Olight"), V("Warrior Ultra", "Olight"), V("Warrior Nano", "Olight"), V("Warrior Mini 2", "Olight")],
    "aluminium, titanium or copper · colours"),
 ],
 "m": [["TK16", "Fenix"], ["TK20R V2", "Fenix"], ["TK11 Pro", "Fenix"], ["TK15R", "Fenix"], ["TK21R", "Fenix"], ["TK28R", "Fenix"], ["PD36 TAC", "Fenix"], ["GL30R", "Fenix"],
       ["P20iX", "Nitecore"], ["P10i", "Nitecore"], ["MH12 Pro", "Nitecore"], ["MH25 Pro", "Nitecore"], ["PolyTac", "Streamlight"], ["TLR-8", "Streamlight"],
       ["Valkyrie PL-3R", "Olight"], ["Valkyrie PL-Mini 2", "Olight"], ["Odin", "Olight"], ["Mag-Tac", "Maglite"], ["TAC 2AA", "Acebeam"]],
 "r": [["TK series", "Fenix"], ["Valkyrie", "Olight"]],
}

thrower = {"n": "Thrower", "a": "long-range torch · search torch · flood monster",
 "d": "Torch built for maximum beam distance (\"throw\") with a deep reflector, large optic or laser source; flood monsters are its wide-beam opposite.",
 "t": ["deep reflector", "TIR optic", "LEP (laser-excited phosphor)", "flood monster (very high lumens)", "green or white emitter"],
 "s": U["fl"],
 "x": [
  X("Acebeam L19", "Compact 21700 hunting thrower using a 60 mm TIR optic for about 1,300 m of throw.", "Acebeam", "2021", "l19",
    [V("L19", "Acebeam", "2021", "OSRAM Boost HX, TIR"), V("L19 V2.0", "Acebeam")], "white or green emitter"),
  X("Nitecore Tiny Monster", "Nitecore's TM series of very high-output multi-emitter lights with OLED displays.", "Nitecore", "", "tm",
    [V("TM10K", "Nitecore", "", "10,000 lumens, six XHP35 HD"), V("TM12K", "Nitecore", "2022", "12,000 lumens, six XHP50.2"),
     V("TM20K", "Nitecore"), V("TM9K Pro", "Nitecore")], "built-in battery · flood-biased"),
 ],
 "m": [["C8+", "Convoy"], ["C8F", "Sofirn"], ["C8G", "Sofirn"], ["SP70", "Sofirn"], ["Q8 Pro", "Sofirn"], ["IF22A", "Sofirn"], ["IF25", "Sofirn"], ["SC31T", "Sofirn"], ["SF14", "Sofirn"], ["SP36", "Sofirn"],
       ["LR40R", "Fenix"], ["LR50R V2", "Fenix"], ["TK47UE", "Fenix"], ["TK35UE", "Fenix"], ["Javelot Pro 2", "Olight"], ["Javelot Turbo", "Olight"], ["Javelot Mini", "Olight"],
       ["Marauder 3", "Olight"], ["Marauder 2", "Olight"], ["Marauder Mini 2", "Olight"], ["SR90", "Olight"], ["X75", "Acebeam"], ["X50", "Acebeam"], ["X25", "Acebeam"], ["E75", "Acebeam"],
       ["MS03", "Imalent"], ["SR32", "Imalent"], ["TM12K", "Nitecore"]],
 "r": [["Javelot", "Olight"], ["Tiny Monster", "Nitecore"]],
}
thrower["m"] = [m for m in thrower["m"] if m[0] != "TM12K"]

rangle = {"n": "Right-angle flashlight", "a": "angle-head flashlight · L-shaped torch",
 "d": "Torch whose head shines at 90° to the body, so it can be clipped to a belt or strap or worn as a headlamp.",
 "t": ["military D-cell", "18650 with headband", "magnetic tail"],
 "s": U["fulton"],
 "x": [
  X("MX-991/U angle-head flashlight", "US military L-shaped D-cell torch with spare filter lenses in the tailcap, descended from the TL-122.", "Fulton Industries", "1960s", "fulton",
    [V("TL-122 series", "", "c. 1939–1944", "Eveready-based WWII angle-head; A to D variants"), V("MX-99/U", "", "1960", "first made by GT Price"),
     V("MX-991/U", "Fulton Industries", "", "current issue, two D cells, five lenses")],
    "olive drab plastic · red, blue, white and diffuser lenses · incandescent or LED", a="Fulton MX991/U · 'Moonbeam'"),
  X("Sofirn SP40", "Budget 18650 right-angle e-switch light sold with headband and clip.", "Sofirn", "", "sp40",
    [V("SP40", "Sofirn", "", "Cree XP-L HD, 1,200 lumens")], "3000 / 4000 / 5300 K"),
 ],
 "m": [["Sidewinder", "Streamlight"], ["Arkflex", "Olight"]],
}

duty = {"n": "Duty & heavy-duty torch", "a": "police torch · D-cell torch · rechargeable duty light",
 "d": "Long, robust torch for police, fire and security work, from aluminium D-cell lights to rechargeable lights in charging holders.",
 "t": ["D / C cell", "rechargeable in charger holder", "baton-length", "intrinsically safe"],
 "s": U["mag"],
 "x": [
  X("Kel-Lite", "Heavy 6061 aluminium police torch that doubled as a baton; the first of the modern duty lights.", "Kel-Lite", "1968", "kel",
    [V("Large Head (KL)", "Kel-Lite", "1968", "D cell"), V("Small Head (SKL)", "Kel-Lite", "", "D cell"), V("C-cell (CPL)", "Kel-Lite"),
     V("Baton Light", "Kel-Lite", "", "18–26 in, fits a baton ring")], "length by cell count · black anodised"),
  X("Maglite D-cell", "Machined aluminium torch with focusable beam on C or D cells; the archetypal police and household torch.", "Maglite", "1979", "mag",
    [V("C and D cell Maglite", "Maglite", "1979"), V("MagCharger", "Maglite", "1982", "rechargeable halogen; LED version 2013"),
     V("2D LED Pro", "Maglite", "2012"), V("ML100 / ML125", "Maglite", "2011", "LED; ML125 rechargeable"), V("ML300L", "Maglite"), V("ML150LR", "Maglite"), V("ML25IT", "Maglite")],
    "2 to 6 cells · incandescent or LED · colours"),
  X("Streamlight Stinger", "Compact rechargeable duty torch that drops into a charger holder; a police-car standard.", "Streamlight", "", "stinger",
    [V("Stinger (xenon)", "Streamlight", "", "original"), V("Stinger Classic LED", "Streamlight", "2013", "same size, LED, fits Stinger chargers"),
     V("UltraStinger", "Streamlight"), V("Poly Stinger", "Streamlight"), V("Stinger 2020", "Streamlight")], "charger holder (12 V / AC)"),
 ],
 "m": [["SL-20L", "Streamlight"], ["Strion", "Streamlight"], ["Survivor", "Streamlight"], ["Vantage", "Streamlight"], ["Dualie", "Streamlight"], ["4AA LED", "Streamlight"],
       ["Pelican 7000", "Pelican Products"], ["Pelican 7060", "Pelican Products"], ["Solitaire", "Maglite"]],
 "r": [["ML series", "Maglite"], ["Stinger", "Streamlight"]],
}
duty["m"] = [m for m in duty["m"] if m[0] != "Solitaire"]

divel = {"n": "Dive light", "a": "diving torch · underwater light",
 "d": "Watertight light carried by an underwater diver, as a primary, backup, canister or video light.",
 "t": ["primary", "backup", "canister (cable to battery pack)", "head-mounted", "video light"],
 "s": U["dive"]}

key = {"n": "Keychain light", "a": "", "d": "Very small light made to hang from a key ring.",
 "t": ["button cell", "AAA / 10440", "built-in rechargeable"],
 "s": "https://www.knifecountryusa.com/shop/manufacturer/2928/olight.html",
 "x": [X("Maglite Solitaire", "Single-AAA key-chain torch, originally sold as the Marquis.", "Maglite", "1988", "mag",
         [V("Solitaire (incandescent)", "Maglite", "1988")], "AAA · colours")],
 "m": [["TIKI", "Nitecore"], ["Tiki GITD", "Nitecore"], ["TINI 2", "Nitecore"], ["Tini 3", "Nitecore"], ["TIP SE", "Nitecore"], ["TUP", "Nitecore"], ["TUP2", "Nitecore"], ["T4K", "Nitecore"], ["Tube", "Nitecore"],
       ["i3E", "Olight"], ["iMini", "Olight"], ["iMini 2", "Olight"], ["i1R2 EOS", "Olight"], ["I1R 2 Pro EOS", "Olight"], ["i16", "Olight"], ["iTHX", "Olight"], ["i5T EOS Mini", "Olight"],
       ["Aurora A3", "RovyVon"], ["Aurora A4", "RovyVon"], ["Aurora A8", "RovyVon"], ["Aurora A9", "RovyVon"], ["S3", "RovyVon"],
       ["Maus Titanium", "Muyshondt"], ["Teeny DX3E", "Eagtac"], ["E03R V2", "Fenix"], ["E04R", "Fenix"], ["EDC01", "Lumintop"], ["Frog", "Lumintop"], ["Tool AA 3.0", "Lumintop"],
       ["Peanut Beast", "Maratac"], ["X3S Copper", "MecArmy"], ["Mycro", "NEBO"], ["Radiant MicroLight", "Nite Ize"], ["Beta-QRV2 Magnetic", "Prometheus Lights"],
       ["73301 Pocket Mate", "Streamlight"], ["Nano Light", "Streamlight"]]}

pen = {"n": "Penlight", "a": "pen light · medical penlight", "d": "Slim pen-shaped hand light for close work or inspection.",
 "t": ["medical (pupil) penlight", "inspection penlight", "AAA / AAAA / rechargeable"],
 "s": "https://zips.com/shop-by-brand/streamlight",
 "m": [["Stylus Pro", "Streamlight"], ["Stylus Pro USB", "Streamlight"], ["Stylus Reach", "Streamlight"], ["Stylus LED Pen Light", "Streamlight"],
       ["O'Pen 3", "Olight"], ["O-Pen", "Olight"], ["G20 Inspection Beam", "Coast Products"], ["Nurse Penlight", "Opoway"]],
 "r": [["Stylus", "Streamlight"]]}

search = {"n": "Hand searchlight", "a": "pistol-grip spotlight · hand spotlight",
 "d": "Large-head or pistol-grip hand spotlight, a different shape from the cylindrical torch.",
 "t": ["pistol grip", "lantern-style", "12 V cord", "rechargeable"],
 "s": "https://fleetmaintenance.com/in-the-bay/shop-equipment/product/10741820/streamlight-inc-waypoint-rechargeable-spotlight",
 "x": [X("Streamlight Waypoint", "Pistol-grip LED spotlight with trigger switch, stand and 12 V cord.", "Streamlight", "", "waypoint",
         [V("Waypoint (alkaline)", "Streamlight", "2015", "4×C, 550 lumens, trigger switch"), V("Waypoint Rechargeable", "Streamlight", "2015", "Li-ion, 1,000 lumens, floats"),
          V("Waypoint 400", "Streamlight")], "yellow or black")],
 "m": [["LiteBox 1Million", "Streamlight"]]}

kinds = [edc, tactical, thrower, rangle, duty, divel, key, pen, search]

def B(n, c="", f="", seg="", d="", lines=(), sig=(), rel=(), s="knowledge"):
    o = {"n": n, "c": c, "f": f, "seg": seg, "d": d, "lines": list(lines), "eras": [], "sig": list(sig), "sc": [], "rel": list(rel), "s": s}
    return o
brands = [
 B("SureFire", "United States", "1979", "premium tactical lights", "Fountain Valley, California maker founded as Laser Products Corporation; renamed SureFire, LLC in 2000.",
   ["6P", "G2X", "E2", "M6", "Z2", "WeaponLight"], ["SureFire 6P", "SureFire WeaponLight", "SureFire M6 Guardian"], ["Streamlight", "Malkoff Devices"], U["sf_wiki"]),
 B("Maglite", "United States", "", "mass-market and duty torches", "Torch brand of Mag Instrument, Inc. (Ontario, California), founded by Anthony Maglica; the Maglite appeared in 1979.",
   ["D/C-cell", "Mini Maglite", "ML series", "XL series", "Solitaire"], ["Maglite D-cell", "Mini Maglite", "Maglite Solitaire"], ["Kel-Lite", "Streamlight"], U["mag"]),
 B("Streamlight", "United States", "1973", "duty and professional lights", "Eagleville, Pennsylvania maker of duty, tactical and weapon lights; absorbed Kel-Lite in 1983.",
   ["Stinger", "ProTac", "TLR", "Waypoint", "Stylus"], ["Streamlight Stinger", "Streamlight ProTac", "Streamlight Waypoint"], ["Kel-Lite", "SureFire"], U["sl"]),
 B("Kel-Lite", "United States", "1968", "historic police torches", "Californian maker founded by Donald Keller and Frank Patti; its aluminium baton-torch set the duty-light pattern; merged into Streamlight 1983.",
   [], ["Kel-Lite"], ["Streamlight", "Maglite"], U["kel"]),
 B("Fulton Industries", "United States", "", "military issue", "Current producer of the US Army and Marines' MX-991/U angle-head flashlight.", [], ["MX-991/U angle-head flashlight"], [], U["fulton"]),
 B("Fenix", "China", "", "outdoor and tactical lights", "Chinese flashlight maker with PD, TK, LR and E series.", ["PD", "TK", "LR", "E", "LD"], ["Fenix PD35"], ["Olight", "Nitecore"]),
 B("Olight", "China", "", "rechargeable EDC and tactical lights", "Chinese maker known for magnetic-charging lights.", ["Baton", "Seeker", "Warrior", "Javelot", "Marauder", "Arkfeld", "Valkyrie"],
   ["Olight Baton", "Olight Seeker", "Olight Warrior"], ["Fenix", "Nitecore"]),
 B("Nitecore", "China", "", "EDC, keychain and high-output lights", "Chinese maker of the EDC, TIKI/TINI keychain and Tiny Monster lines.", ["EDC", "P", "MH", "TM", "TIKI", "TINI", "TUP"],
   ["Nitecore EDC series", "Nitecore Tiny Monster"], ["Fenix", "Olight"]),
 B("Ledlenser", "Germany", "1993", "mainstream torches and headlamps", "Solingen maker founded by Harald and Rainer Opolka as Zweibrüder; known for the focusable P series.", ["P", "MT", "T"], [], []),
 B("Zebralight", "", "", "enthusiast EDC and headlamps", "Maker of compact side-switch SC lights and H headlamps with neutral and high-CRI emitters.", ["SC", "H"], ["Zebralight SC series"], [], U["zl"]),
 B("Emisar", "", "", "enthusiast lights", "Hank Wang's brand sold through Intl-Outdoor (with Noctigon); D4V2 uses the community Anduril firmware.", ["D4"], ["Emisar D4"], ["Convoy"], U["d4"]),
 B("Malkoff Devices", "United States", "", "duty and EDC lights", "Small American business run by Gene and Cathy Malkoff; makes MDC lights and M61 light engines used in other makers' torches.", ["MDC", "M61"], ["Malkoff MDC"], ["SureFire"], U["mdc"]),
 B("Okluma", "", "", "custom EDC lights", "Small-batch custom maker of machined 18350 lights.", ["DC1"], ["Okluma DC1"], [], U["ok"]),
 B("Convoy", "", "", "budget enthusiast lights", "Budget brand whose S2+ is the standard modding host.", ["S2+", "C8+"], ["Convoy S2+"], ["Emisar"], U["s2"]),
 B("Sofirn", "", "", "budget enthusiast lights", "Budget maker of throwers, EDC and right-angle lights.", ["SP", "SC", "C8", "IF"], ["Sofirn SP40"], ["Convoy"], U["sp40"]),
 B("Acebeam", "", "", "high-output and long-range lights", "Maker of throwers and high-output lights such as the L19 and X series.", ["L", "X", "E", "Pokelit"], ["Acebeam L19"], [], U["l19"]),
 B("Muyshondt", "", "", "luxury EDC lights", "Maker of small luxury lights in aluminium, titanium and copper.", ["Aeon", "Maus"], ["Muyshondt Aeon"], [], U["aeon"]),
]

notes = ("k24 'Flashlight' (230 models) split by form into EDC, tactical, thrower, right-angle and duty kinds; Dive light added as a kind (no models: none attested). "
 "Dropped: 'Angle-head flashlight' (generic, no maker; now the Right-angle kind), Shadowhawk '10000 High Lumens' and GearLight S1000 (listing noise), "
 "Klein Tools rechargeable flashlight with work light and Fenix WT26RM, RC20, UC30, UC35, C7 Pro, C7 V2, E06R Pro RG, E08R UE, GL30R kept only where placed; "
 "Streamlight Bear Trap, Flipmate, Jr. F-Stop, Syclone, Speedlocker, Enduro (work/clip/headlamp forms belong to Work light / Headlamps shelves) and Olight Array, ArkPro, Baldr Mini/Pro R/S, Beagle, Drever, "
 "Mettle, Nightclaw, Rubato 4, Sigurd, Splint, Marauder Mini, Baton 4 Pro moved into versions; ThruNite Archer 2A Pro, Fenix TK20R, PD35 v3.0/PD35TAC folded into archetype versions. "
 "Weapon lights are a type of Tactical flashlight (SureFire WeaponLight archetype); E4 may cross-link. Mini Maglite placed under EDC (pocket 2AA), Solitaire under Keychain. "
 "Not done: archetypes for Ledlenser P7 (retailer page had no content), Convoy C8, Fenix TK, Streamlight SL-20, Olight Perun, LEP lights (no page retrieved). "
 "Brand founding years left blank where no retrieved page or reliable knowledge.")

out = {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes}
p = "/home/user/Possession-Taxonomy/rebuild/work/B3/shelves/05_00.json"
os.makedirs(os.path.dirname(p), exist_ok=True)
json.dump(out, open(p + ".tmp", "w"), ensure_ascii=False, indent=1)
os.replace(p + ".tmp", p)
print("written", sum(len(k.get("x", [])) for k in kinds), "archetypes")
