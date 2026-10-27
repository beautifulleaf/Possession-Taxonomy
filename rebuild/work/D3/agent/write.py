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
P=lambda *x:[(i,"Polk Audio") for i in x]
w('D3','00_02',{"kinds":[
 K("Headphone & earbud spare parts","ear pads · ear cushions · ear tips · replacement charging case","Replacement part made for one headphone or earbud model, such as ear pads, ear tips or a charging case.","https://dekoniaudio.com/collections/earpads",[("Earpads for HD 600 series","Sennheiser")],[("Core Series","Comply Foam")],["ear pads","ear tips","replacement charging case"]),
 K("Headphone cable","detachable headphone cable","Cable made for one headphone model; standard-connector cables are in Computers.","https://straussandwagner.com/collections/sennheiser-compatible-cables",[("Geneva","Strauss & Wagner"),("Lucerne","Strauss & Wagner"),("Riga","Strauss & Wagner")]),
 K("Headphone stand","headphone hanger","Stand or hanger made to hold headphones when not worn, for one model or any.","https://www.sanus.com/en_AD/designed-for-sonos")],
 "brands":[],"traditions":[],"notes":"Merged Headphone ear pads, Earphone ear tips and Earbud charging case into one spare-parts kind (parts as types; kept the ear-pads source). Headphone cable cut from 8 Strauss & Wagner models to 3 (single-maker list). Stand unchanged."})
w('D3','01_01',{"kinds":[
 K("Home cinema speaker system","home-cinema speaker package","Package of speakers for a TV sold and compared as one system.","https://www.polkaudio.com/en-us/category/home-speakers/home-theater-systems",
   [("Klipsch Reference Theater Pack","Klipsch"),("Klipsch R-600F Home Theater System","Klipsch"),("Klipsch R-800F Home Theater System","Klipsch")]+P("Polk Audio Signature Elite 5.2 Home Theater System","Polk Audio Signature Elite 2.1 System"),
   [("Reference","Klipsch"),("Signature Elite Series","Polk Audio")]),
 K("Centre speaker","centre-channel speaker","Speaker made to carry the centre channel of a surround system, placed at the screen.","https://www.polkaudio.com/en-us/category/home-speakers/home-theater-systems",
   P("Polk Audio Reserve R350","Polk Audio Signature Elite ES35","Polk Audio Monitor XT30","Polk Audio T30"),
   [("Reserve Series","Polk Audio"),("Signature Elite Series","Polk Audio"),("Monitor XT Series","Polk Audio"),("T Series","Polk Audio")]),
 K("Surround speakers","","Speaker made for the side, rear or height channels of a surround system.","https://www.kbaudio.co.uk/collections/surround-channel-speakers",
   [("Klipsch RP-502S II","Klipsch"),("Klipsch RP-500SA II","Klipsch"),("Monitor Audio Bronze AMS 7G","Monitor Audio"),("Paradigm Surround 3","Paradigm"),("JBL Stage 240H","JBL"),("Mission LX-3D","Mission")]+P("Polk Audio Reserve R900","Polk Audio Signature Elite ES10","Polk Audio SR2 Wireless Surrounds"),
   [("Reference Premiere","Klipsch"),("Reserve Series","Polk Audio"),("Signature Elite Series","Polk Audio")],
   ["side","rear","height (Atmos-enabled)","wireless"]),
 K("In-wall and in-ceiling speakers","","Speakers without a cabinet, with a mounting flange, built into a wall or ceiling.","https://www.richersounds.com/hi-fi",P("Polk Audio 265-LS","Polk Audio 80 F/X-LS"),None,["in-wall","in-ceiling"]),
 K("On-wall speakers","","Slim speaker cabinets made to hang flat on a wall, often beside a TV; in-wall speakers have no cabinet.","https://www.polkaudio.com/en-us/category/built-in-speakers/in-wall/")],
 "brands":[],"traditions":[],"notes":"All five kinds kept. Surround speakers cut from 13 to 9 models (dropped Klipsch THX-5000-SUR, Paradigm Surround 1, Polk Monitor XT90, Polk Signature Elite ES90 as near-duplicates of kept lines; Monitor XT range dropped with them); positions as types. Home cinema system cut from 7 to 5 (dropped R-50M and R-605FA). In-wall vs in-ceiling as types. No new models."})
w('D3','01_02',{"kinds":[
 K("Soundbar","TV soundbar","Speaker made as a bar for a TV, with or without a separate subwoofer.","https://www.hifi-regler.de/",
   [("Sonos Arc Ultra","Sonos"),("Sonos Beam (Gen 2)","Sonos"),("Sonos Ray","Sonos"),("Sony BRAVIA 9 Soundbar","Sony"),("Bluesound Pulse Soundbar+","Bluesound")]+P("Polk Audio MagniFi Max AX SR","Polk Audio MagniFi Mini AX","Polk Audio Signa S4"),
   [("BRAVIA","Sony"),("MagniFi Series","Polk Audio"),("Signa Series","Polk Audio")]),
 K("Wi-Fi and multi-room speakers","wireless home speaker · smart speaker (Sonos type) · single-enclosure speaker","Mains-powered speaker that streams over Wi-Fi or Bluetooth, often grouping with others across rooms.","https://www.bestbuy.com/site/home-audio-systems/wireless-streaming-audio/pcmcat186600050004.c?id=pcmcat186600050004",
   [("Sonos Era 100","Sonos"),("Sonos Era 300","Sonos"),("Sonos Five","Sonos"),("Sonos One","Sonos")],None,["Wi-Fi multi-room","mains-powered Bluetooth"]),
 K("Portable Bluetooth speakers","portable speaker · wireless speaker","Battery-powered speaker made to carry around, usually Bluetooth and often waterproof.","https://www.bestbuy.com/site/portable-speakers-docks-radios/portable-speakers/pcmcat748301666245.c?id=pcmcat748301666245",
   [("Sonos Move 2","Sonos"),("Sonos Roam 2","Sonos")]),
 K("Party speakers","PartyBox · Megasound speaker","Large loud speaker for parties, often with lights, handles and microphone inputs.","https://www.bestbuy.com/site/shop/portable-bluetooth-speakers-for-party")],
 "brands":[],"traditions":[],"notes":"Dissolved 'Other single-box speakers' into Wi-Fi and multi-room speakers (mains-powered Bluetooth as a type; portable and party speakers already have their own kinds). Soundbar cut from 12 to 8 (dropped Polk MagniFi Max AX, Signa S2D, Signa S3 as overlapping Polk lines, and Sonos Beam Ultra which could not be confirmed). No new models: the old data has no Bose, Samsung, JBL, Ultimate Ears or Marshall models and none were added without research."})
w('D3','03_02',{"kinds":[
 K("AV receiver","home cinema receiver","Multichannel amplifier with surround decoding, video switching and a tuner in one box.","https://www.hifi-regler.de/",
   [("Denon AVR-X3900H","Denon"),("Denon AVC-X4800H","Denon"),("Marantz Cinema 30","Marantz"),("Marantz SR7015","Marantz"),("Yamaha RX-A4A Aventage","Yamaha"),("Yamaha RX-A6A","Yamaha"),("Onkyo TX-NR6050","Onkyo"),("Onkyo TX-RZ50","Onkyo"),("NAD T 778","NAD"),("NAD T 758 V3i","NAD")]),
 K("AV processor","surround processor","Multichannel surround preamplifier and decoder that feeds separate power amplifiers.","https://hificentre.com/collections/surround-processors",
   [("Trinnov Altitude 16","Trinnov"),("Trinnov Altitude 32","Trinnov"),("Anthem AVM 90","Anthem"),("Marantz AV 10","Marantz"),("Marantz AV 20","Marantz"),("Storm Audio ISP Core 16","Storm Audio"),("Storm Audio ISP Evo 32 AoIP","Storm Audio"),("miniDSP Tide 16","miniDSP")],
   [("Altitude","Trinnov")]),
 K("Multichannel power amplifier","","Power stage with three or more channels that drives home-cinema speakers from an AV processor.","https://shopaudioexperience.com/streamer/"),
 K("Video processor","","External unit that scales and tone-maps video between a source and a TV or projector.","https://www.audiovenue.uk/product-tag/dap/")],
 "brands":[],"traditions":[],"notes":"All four kinds kept. AV receiver cut from 11 to 10 (dropped Onkyo TX-NR7100). AV processor cut from 11 to 8 (dropped Trinnov Altitude CI and Storm Audio ISP Elite 16 Analog MK3 as custom-install variants, Marantz AV 30). Video processor kept kind-level with no models. No new models."})
w('D3','07_00',{"kinds":[
 K("Television","TV","Screen sold with television reception or as a television, of any display technology.","https://web.abenson.com/television/tv/product-brand/lg-samsung-sony-tcl/tv-resolution/qled.html",
   [("LG OLED C6","LG"),("LG OLED G6","LG"),("LG QNED86","LG"),("LG Mini RGB MRGB86","LG"),("Samsung OLED S95F","Samsung"),("Samsung OLED S90F","Samsung"),("Samsung Neo 4K QN80H","Samsung"),("Samsung The Frame","Samsung"),("Sony BRAVIA 8 II","Sony"),("Sony BRAVIA 9 II","Sony"),("Sony BRAVIA 7 II","Sony"),("TCL QLED T6D","TCL")],
   [("BRAVIA","Sony")],["OLED","QD-OLED","Mini-LED","QLED","LED-LCD","RGB Mini-LED","32–43 in","50–65 in","75 in and up"]),
 K("Projector","digital projector","Projector that throws a picture from a video or computer signal onto a screen or wall from a distance.","https://www.benq.com/en-us/projector/tv-projector.html",
   [("Epson Home Cinema LS11000","Epson"),("Epson Home Cinema LS7500","Epson"),("Epson Home Cinema LS5000","Epson"),("BenQ AK800ST","BenQ"),("XGIMI Titan","XGIMI"),("Hisense C3 Ultra","Hisense"),("Hisense C3","Hisense"),("Valerion VisionMaster Max","Valerion"),("Formovie Xming Episode One","Formovie")]),
 K("Ultra-short-throw projector","","Projector made to sit at the wall just below the image it throws.","https://www.benq.com/en-us/projector/tv-projector.html",
   [("Hisense L9Q","Hisense"),("Hisense PX4 Pro","Hisense"),("Epson EH-LS800","Epson"),("BenQ V5010i","BenQ"),("LG CineBeam HU915QE","LG"),("XGIMI MIRA","XGIMI"),("AWOL Vision LTV-3500 Pro","AWOL Vision"),("AWOL Vision Aetherion Pro","AWOL Vision"),("Formovie THEATER","Formovie")]),
 K("Projector screen","projection screen","Screen made for a projector to throw its image onto.","https://www.lowes.com/pd/Kodak-100-inch-Projector-Screen-Fixed-Frame-with-Velvet-Frame-and-Wall-Mount-Kit/9112129")],
 "brands":[],"traditions":[],"notes":"Television cut from 25 to 12 models (dropped 2006-era Panasonic TH-42PX75U and Sony KDL-46S2000, previous-year Samsung S85F/S85H/S95H/Q8F, LG QNED70/80, Sony BRAVIA 2 II/9/A95L, TCL P71L/P7L); display technology and size as types. Projector cut from 12 to 9 (dropped Epson LS6000, Hisense C3 Pro, Hisense M2 Pro). UST cut from 15 to 9 (dropped Christie Captiva DWU500S as institutional, older BenQ V5000i/V7050i, Hisense L9Q Pro/PX3-Pro, Formovie Cinema Edge). No Panasonic, Philips, Sony, JVC or Optoma projector models added (none in old data)."})
w('D3','09_00',{"kinds":[
 K("Smart speaker","","Speaker whose designed function is a voice assistant.","https://en.wikipedia.org/wiki/Smart_speaker",
   [("Echo Dot","Amazon"),("Echo Dot Max","Amazon"),("Echo Studio","Amazon"),("HomePod","Apple"),("HomePod mini","Apple"),("Google Home","Google"),("Google Home Mini","Google"),("Google Home Max","Google"),("Invoke","Harman Kardon")],[("Echo","Amazon")]),
 K("Smart display","","Voice-assistant device with a screen.","https://store.google.com/category/nest_hubs_displays?hl=en-US",
   [("Echo Show 5","Amazon"),("Echo Show 8","Amazon"),("Echo Show 15","Amazon"),("Echo Show 21","Amazon"),("Nest Hub (2nd gen)","Google"),("Nest Hub Max","Google")],[("Echo","Amazon"),("Nest Hub","Google")]),
 K("Smart-home hub","","Device that links and controls smart-home devices.","https://us.aqara.com/collections/smart-home-hub",
   [("Hub M3","Aqara"),("Hub M200","Aqara"),("Hub M100","Aqara")],[("Hub","Aqara")])],
 "brands":[],"traditions":[],"notes":"All three kinds kept. Smart-home hub cut from 5 Aqara models to 3 (dropped Hub E1 and Hub M1S Gen 2); other hub makers left unnamed (no models in old data). Speakers and displays unchanged."})
w('D3','10_00',{"kinds":[
 K("TV and speaker stands and mounts","speaker stand · wall mount · bracket","Stand, bracket, arm or wall mount made to hold a TV or speaker.","https://www.sanus.com/es_CU/products/speaker-stands",None,None,["speaker stand","TV wall mount","TV floor stand","table stand","speaker wall bracket"]),
 K("TV antenna","aerial","Aerial made to receive broadcast television for a TV or receiver.","https://store.antennasdirect.com/HD-TV-antennas.html",
   [("ClearStream 4MAX","Antennas Direct"),("ClearStream 2MAX","Antennas Direct"),("ClearStream ECLIPSE","Antennas Direct"),("ClearStream FLEX","Antennas Direct"),("DB8-e","Antennas Direct"),("Mohu Leaf","Antennas Direct"),("Mohu Leaf Supreme Pro","Antennas Direct"),("Mohu Gateway","Antennas Direct")],
   [("ClearStream","Antennas Direct"),("Mohu","Antennas Direct")],["indoor","outdoor","attic"]),
 K("Remote control","universal remote","Remote made for one TV or audio system; a universal remote is listed here too.","https://www.lg.com/hu/tv-es-hangprojektor/tv-kiegeszitok/mr25ga",
   [("AI Magic Remote","LG"),("SolarCell Remote","Samsung")])],
 "brands":[],"traditions":[],"notes":"Merged Speaker stand and TV or speaker mount into one kind with mount types. TV antenna cut from 15 to 8 (dropped ClearStream 1MAX, MAX-V, MAX-XR, ELEMENT, Goliath, Mohu Gateway Plus, Mohu Leaf 50); indoor/outdoor as types. No universal-remote models added (none in old data)."})
