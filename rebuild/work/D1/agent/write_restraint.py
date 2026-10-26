import json, os, sys
B = '/home/user/Possession-Taxonomy/rebuild/work/D1/shelves/'
def K(n, d, s, m=None, t=None, a='', r=None, tg=None):
    k = {'n': n, 'a': a, 'd': d}
    if t: k['t'] = t
    if tg: k['tg'] = tg
    k['s'] = s
    k['m'] = m or []
    if r: k['r'] = r
    return k
WD = 'Western Digital'
J = {}
J['02_00'] = dict(kinds=[
 K('Internal SSD', 'Solid-state drive fitted inside a computer, as an M.2 card or a 2.5-inch drive.',
   'https://www.bestbuy.ca/en-ca/category/network-attached-storage-nas/29582',
   [["Samsung 9100 Pro","Samsung"],["Samsung 980 PRO","Samsung"],["Samsung 870 EVO","Samsung"],["WD_BLACK SN850P",WD],["WD Blue SN5000",WD],["WD Blue SATA SSD",WD],["Crucial P310","Crucial"],["Crucial BX500","Crucial"],["SanDisk Optimus GX 7100","SanDisk"]],
   t=['M.2 NVMe','M.2 SATA','2.5-inch SATA']),
 K('External SSD', 'Solid-state drive in its own case, connected by USB or Thunderbolt.',
   'https://www.bestbuy.ca/en-ca/category/network-attached-storage-nas/29582',
   [["Samsung T7","Samsung"],["Samsung T7 Shield","Samsung"],["Samsung T9","Samsung"],["SanDisk Extreme Portable SSD","SanDisk"],["SanDisk Extreme PRO Portable SSD","SanDisk"],["WD My Passport SSD",WD],["Lexar Portable SSD SL300","Lexar"],["PNY Pro Elite V2","PNY"]],
   t=['pocket','rugged','USB-C','Thunderbolt']),
 K('Internal HDD', 'Spinning-disk drive fitted inside a computer or NAS.',
   'https://www.bestbuy.ca/en-ca/category/network-attached-storage-nas/29582',
   [["Seagate Barracuda","Seagate"],["Seagate IronWolf","Seagate"],["Seagate IronWolf Pro","Seagate"],["Seagate SkyHawk AI","Seagate"],["WD Red Plus",WD],["WD Purple Pro",WD]],
   t=['3.5-inch desktop','2.5-inch laptop','NAS (CMR)','surveillance']),
 K('External HDD', 'Spinning-disk drive in its own case, connected from outside.',
   'https://www.bestbuy.ca/en-ca/category/network-attached-storage-nas/29582',
   [["WD My Passport",WD],["WD easystore",WD],["Seagate Expansion","Seagate"],["Seagate Expansion Desktop","Seagate"]],
   t=['portable (2.5-inch)','desktop (3.5-inch, mains-powered)']),
 K('Drive enclosure', 'Housing, sold empty, that turns a bare drive into an external drive.',
   'https://www.memoryexpress.com/Category/ExternalEnclosures',
   [["OWC Express 1M2","OWC"],["OWC Express 4M2","OWC"],["Vantec NexStar GX","Vantec"],["Vantec NexStar TX","Vantec"],["Sharge Disk","Sharge"]],
   t=['USB enclosure','dock','duplicator','M.2 NVMe','2.5-inch','3.5-inch']),
], notes='Restraint only: kept all five planned kinds; form factor and interface moved into types. Trimmed duplicate generations (Samsung T5 EVO, SanDisk Portable SSD, Vantec NexStar JX/SX) to keep the lists short. No new models or brands added (no research this pass).')

J['02_01'] = dict(kinds=[
 K('USB flash drive', 'Small flash storage device that plugs into a USB port.',
   'https://www.bhphotovideo.com/c/buy/USB-Flash-Drives/ci/5699',
   [["SanDisk Cruzer Glide","SanDisk"],["SanDisk Ultra Flair","SanDisk"],["SanDisk Ultra Dual Drive Luxe","SanDisk"],["SanDisk Extreme PRO Dual Drive","SanDisk"],["Samsung BAR Plus","Samsung"],["Kingston DataTraveler Exodia M","Kingston"],["Kingston DataTraveler microDuo 3C","Kingston"],["Lexar JumpDrive Dual Drive D400","Lexar"],["PNY Turbo Attache 3","PNY"]],
   t=['USB-A','USB-C','dual-connector']),
 K('Memory card', 'Removable flash card for cameras, phones, handhelds and card slots. A card made only for one games console is in Video Games.',
   'https://www.pbtech.co.nz/category/peripherals/usb-memory-cards/microsd-cards/brand-Canon',
   [["SanDisk Extreme PRO microSD","SanDisk"],["SanDisk Extreme microSDXC UHS-I","SanDisk"],["SanDisk Ultra microSD","SanDisk"],["SanDisk microSD Express","SanDisk"],["Kingston Canvas Select Plus microSDXC","Kingston"],["Sony SF-G TOUGH SDXC UHS-II","Sony"],["WD Purple microSDXC",WD]],
   t=['SD/SDHC/SDXC','microSD','CFexpress Type A','CFexpress Type B','CompactFlash','XQD','Memory Stick'], a='SD card · microSD card · TF card'),
 K('Memory-card reader', 'Device that reads memory cards and connects to a computer.',
   'https://www.bhphotovideo.com/c/buy/Card-Readers/ci/7862',
   [["SanDisk QuickFlow SD Card Reader","SanDisk"],["SanDisk QuickFlow microSD Card Reader","SanDisk"],["SanDisk PRO-DOCK 4","SanDisk"]]),
 K('NAS', 'Network-attached storage device that holds drives and serves files over a network. A recorder sold only to run security cameras is in Home Safety & Security.',
   'https://www.newegg.com/Network-Attached-Storage-NAS/Category/ID-241',
   [["Synology DiskStation DS925+","Synology"],["Synology DiskStation DS923+","Synology"],["Synology DiskStation DS1522+","Synology"],["QNAP TS-233","QNAP"],["QNAP TS-264","QNAP"],["QNAP TS-433","QNAP"],["ASUSTOR Nimbustor 4 Gen2 AS5404T","ASUSTOR"],["ASUSTOR FLASHSTOR 12 Pro FS6712X","ASUSTOR"],["UGREEN NASync DXP4800 Pro","Ugreen"],["Ubiquiti UNAS 2","Ubiquiti (UniFi)"],["Buffalo LinkStation 220","Buffalo"]],
   t=['1–2 bay','4 bay','5+ bay','all-flash (M.2)'], a='network-attached storage'),
 K('Optical drive', 'Drive that reads or writes discs, fitted in a drive bay or in its own case.',
   'https://pcpartpicker.com/products/optical-drive/',
   [["ASUS SDRW-08D2S-U Lite","ASUS"],["LG GP60NB50","LG"]], t=['internal','external','DVD','Blu-ray']),
], notes='Merged microSD card, SD card and Other memory cards into Memory card (formats as types). NAS trimmed from 23 models to 11 across Synology, QNAP, ASUSTOR, Ugreen, Ubiquiti and Buffalo; dropped rack-mount and business units (RackStation RS2423+, DS3622xs+, DS1621xs+, TeraStation 5820) under the scope rule, and older generations (DS916+, DS1019+, DS1817, DS1819+, DS1621+, DS220+). USB flash drive trimmed to 9. No new models added.')

J['03_00'] = dict(kinds=[
 K('Monitor', 'Display sold for use with a computer.', 'https://pcpartpicker.com/products/monitor/',
   [["ROG Swift OLED PG27UCDM","ASUS"],["ROG Strix OLED XG27AQDMG Gen 2","ASUS"],["TUF Gaming VG27AQ5F","ASUS"],["Dell Alienware AW2725DF","Alienware"],["Dell UltraSharp 38 Curved USB-C Hub Monitor U3824DW","Dell"],["Dell Pro P27 P2726H","Dell"],["LG UltraGear 45GS95QE-B","LG"],["Samsung Odyssey G55C","Samsung"],["MSI MPG 271QRX QD-OLED","MSI"],["BenQ ZOWIE XL2586X+","BenQ"],["Lenovo Legion R27qc-30","Lenovo"],["HP E24m G4","HP"],["ViewSonic OMNI VX2728J","ViewSonic"]],
   t=['gaming','office','creator','ultrawide','portable','OLED','IPS','VA'], r=[["ROG Swift"] if False else ["ROG Strix","ASUS"],["TUF Gaming","ASUS"]]),
 K('Monitor arm or stand', 'Arm, bracket or stand made to hold one screen.',
   'https://www.markertek.com/product/ergo-45-695-292/ergotron-45-695-292-lx-pro-arm-single-monitor-desk-mount-with-12-inch-pole-2-piece-clamp-black',
   [["Ergotron LX Pro Arm","Ergotron"]], t=['desk-clamp arm','freestanding stand','wall mount']),
 K('Laptop stand', 'Stand or riser without fans made to hold one laptop at a height or angle.',
   'https://www.quill.com/laptop-cooling-pads/cbk/108343.html?page=2', [["WorkEZ Best Aluminum Laptop Stand","Uncaged Ergonomics"]]),
 K('Laptop cooler', 'Pad or stand with fans that cools a laptop.', 'https://www.dell.com/en-us/shopping/laptop-cooling-pads',
   [["Cooler Master NotePal X-Slim","Cooler Master"],["Targus Chill Mat","Targus"],["Kensington SmartFit Easy Riser","Kensington"],["Enhance Cryogen","Enhance"]]),
 K('Laptop sleeve or case', 'Sleeve or case made to hold or protect one laptop.',
   'https://www.thule.com/en-us/laptop-bags-sleeves/laptop-sleeves-and-cases/thule-gauntlet-macbook-pro-sleeve-14-_-3204903', [["Thule Gauntlet","Thule"]], t=['sleeve','hard-shell case']),
], notes='Monitor cut from 74 SKUs (46 of them ASUS: retail-harvest skew) to 13 across ASUS, Alienware, Dell, LG, Samsung, MSI, BenQ, Lenovo, HP and ViewSonic, keeping all old-data names; panel and use moved into types. Not checked against RTINGS/TFTCentral winners this pass (no research). Kept old ranges ROG Strix and TUF Gaming; dropped the bare ROG range as a duplicate. Laptop cooler trimmed to 4 brands (dropped Enhance Voltaic 2, Purely C50).')
# fix ranges literal
J['03_00']['kinds'][0]['r'] = [["ROG Strix","ASUS"],["TUF Gaming","ASUS"]]

J['03_02'] = dict(kinds=[
 K('Webcam', 'Camera made for use with a computer.', 'https://pcpartpicker.com/products/webcam/',
   [["Logitech C920S Pro","Logitech"],["Logitech C922 Pro Stream","Logitech"],["Logitech Brio 4K","Logitech"],["Logitech MX Brio","Logitech"],["Logitech Brio 300","Logitech"],["Logitech C270","Logitech"],["Elgato Facecam","Elgato"],["Elgato Facecam 4K","Elgato"],["Anker PowerConf C200","Anker"],["Creative Live! Cam Sync 4K","Creative Technology"]],
   t=['1080p','4K','streaming']),
 K('Microphone', 'Microphone made for speech, calls or streaming at a computer.', 'https://www.elgato.com/ww/es/p/wave-3',
   [["Shure MV7+","Shure"],["Shure MV7","Shure"],["Blue Yeti","Logitech"],["Elgato Wave:3","Elgato"],["Elgato Wave DX","Elgato"],["Elgato Wave Neo","Elgato"]],
   t=['USB','XLR','USB/XLR hybrid','desk','boom-arm'], a='speech microphone · streaming microphone'),
], notes='Webcam trimmed from 17 to 10 (dropped near-duplicate Logitech Brio 90/100/105/500, StreamCam, Elgato Facecam Neo, Creative 1080p V2). Microphone kept as is with USB/XLR types. Rode and Audio-Technica named in the brief not added: no model for them in the old data and no research this pass.')

J['05_00'] = dict(kinds=[
 K('Printer', 'Machine that prints from a computer.', 'https://www.bhphotovideo.com/c/buy/Laser-Printers/ci/9997/pn/14',
   [["Brother HL-L2405W","Brother"],["Brother HL-L2460DW","Brother"],["Brother HL-L3295CDW","Brother"],["Canon PIXMA TS3725","Canon"],["HP Color LaserJet Pro 4201dn","HP"]],
   t=['inkjet','laser','ink-tank','photo','A3+ wide-format']),
 K('Multifunction printer', 'Machine that prints and scans (and copies) for use with a computer.', 'https://Quill.com/best-printer-buying-guide/cbx/167.html',
   [["Brother MFC-L2900DW","Brother"],["Brother MFC-L3780CDW","Brother"],["Brother MFC-J1010DW","Brother"],["Canon PIXMA TR8620a","Canon"],["Canon PIXMA TS3720","Canon"],["Canon imageCLASS D1650","Canon"],["Epson EcoTank ET-2903","Epson"],["Epson WorkForce WF-2960","Epson"],["HP Envy 6155e" if False else "HP Envy 6455e","HP"],["HP Color LaserJet Pro 3301FDW","HP"],["HP LaserJet Pro MFP 4101fdw","HP"]],
   t=['inkjet','laser','ink-tank'], a='all-in-one printer'),
 K('Scanner', 'Machine that scans documents or images into a computer.', 'https://www.walmart.com/browse/electronics/scanners/3944_3951_37807_4439',
   [["Fujitsu ScanSnap iX1500","Fujitsu"],["Epson FastFoto FF-680W","Epson"],["Epson WorkForce ES-400 II","Epson"],["Epson WorkForce ES-50","Epson"],["Epson WorkForce ES-590W","Epson"]],
   t=['flatbed','document','portable','film/photo']),
 K('Ink & toner cartridge', 'Ink or toner supply made for one printer type.', 'https://www.jbhifi.co.nz/products/hp-62-black-original-ink-cartridge',
   [["HP 62","HP"],["Canon PG-245","Canon"],["Epson EcoTank T502 ink bottle","Epson"],["Brother TN-760","Brother"]],
   t=['ink cartridge','ink bottle','toner cartridge','drum']),
], notes='Wide-format printer merged into Printer as type A3+ wide-format; its HP DesignJet/PageWide XL lines dropped as trade/office equipment (scope rule). Printer trimmed to 5 (dropped office-class Brother HL-L5000D/L5210DW/L6210DW/L6415DW/L9410CDN). Multifunction printer cut from 28 to 11 across Brother, Canon, Epson and HP. Scanner dropped Fujitsu fi-7160 (office production scanner) and the older ScanSnap iX500. Ink cartridge and Toner cartridge merged; Brother toner list reduced to one example. Not checked against test winners (no research).')
J['05_00']['kinds'][1]['m'][8] = ["HP Envy 6455e","HP"]

J['06_00'] = dict(kinds=[
 K('Wi-Fi router', 'Network device that routes traffic and provides wireless access.', 'https://www.tp-link.com/us/home-networking/all-router/',
   [["Archer BE550","TP-Link"],["Archer BE800","TP-Link"],["TL-WR841N","TP-Link"],["TP-Link Roam 7","TP-Link"],["ASUS RT-BE58U","ASUS"],["ASUS ZenWiFi BQ16","ASUS"],["ROG Rapture GT-BE98 Pro","ASUS"],["Nighthawk RS700S","Netgear"],["Nighthawk RS300","Netgear"],["FRITZ!Box 7590 AX","AVM"],["FRITZ!Box 6690 Cable","AVM"]],
   t=['single router','mesh system','travel router','gaming router'], a='wireless router', r=[["Nighthawk","Netgear"],["ROG","ASUS"]]),
 K('Modem', "Device that connects a home network to a provider's cable, DSL, fibre or cellular line; one with a built-in router is this kind.", 'https://www.surfboard.com/products/cable-modems',
   [["SURFboard SB8200","Arris International"],["SURFboard S33","Arris International"],["SURFboard S34","Arris International"]], t=['cable','DSL','fibre ONT','4G/5G']),
 K('Access point', 'Network device that adds wireless access to a wired network.', 'https://www.tp-link.com/us/home-networking/access-point/',
   [["UniFi U7 Pro","Ubiquiti (UniFi)"],["UniFi U6 Pro","Ubiquiti (UniFi)"],["UniFi U6 Long-Range","Ubiquiti (UniFi)"],["TL-WA1201","TP-Link"],["TL-WA3001","TP-Link"]], t=['ceiling','wall','outdoor']),
 K('Range extender', "Network device that receives a wireless signal and rebroadcasts it to widen coverage, including add-on mesh nodes.", 'https://www.tp-link.com/us/home-networking/range-extender/',
   [["RE700X","TP-Link"],["RE505X","TP-Link"],["RE220","TP-Link"],["RE815XE","TP-Link"],["FRITZ!Repeater 1200 AX","AVM"],["FRITZ!Repeater 6000","AVM"]], t=['plug-in','desktop','mesh node']),
 K('Network switch', 'Network device that connects wired devices on a local network.', 'https://www.tp-link.com/us/business-networking/soho-switch-unmanaged/',
   [["TL-SG105","TP-Link"],["TL-SG108-M2","TP-Link"],["TL-SG116P","TP-Link"],["TL-SX1008","TP-Link"]], t=['unmanaged','managed','PoE','multi-gig']),
 K('Powerline adapter', "Adapter that carries a network connection over a building's mains wiring, sold in pairs or kits.", 'https://www.tp-link.com/us/home-networking/powerline/',
   [["TL-PA7017P","TP-Link"],["TL-PA9020P","TP-Link"],["TL-WPA7617","TP-Link"],["TL-WPA8631P","TP-Link"]], t=['wired only','with Wi-Fi','pass-through socket']),
 K('PoE injector', 'Device that adds power to an Ethernet cable to feed a powered network device.', 'https://www.raspberrypi.com/products/', [["PoE+ Injector","Raspberry Pi"]]),
 K('Ethernet cable', 'Network cable with standard patch connectors.', 'https://cablematters.com/pc-732-160-cable-matters-snagless-cat6-ethernet-cable-cat6-cable-cat-6-cable-availble-25ft-150ft-in-length.aspx',
   [["ROG Cat7 Cable","ASUS"]], t=['Cat5e','Cat6','Cat6a','Cat7','Cat8','flat'], a='LAN cable · network cable', r=[["ROG","ASUS"]]),
], notes='Wi-Fi router cut from 39 (mostly ASUS ROG and Netgear Nighthawk flagship SKUs) to 11 across TP-Link, ASUS, Netgear and AVM; mesh and travel routers as types. Eero, Google Nest Wifi, Linksys and Ubiquiti routers named in the brief not added: no models in the old data, no research this pass. Range extender trimmed 13 to 6; powerline 10 to 4; access point 8 to 5 (dropped enterprise U6 Enterprise, U7 Pro Max, older TL-WA901N).')

J['07_00'] = dict(kinds=[
 K('USB cable', 'Cable with USB connectors at both ends.', 'https://www.anker.com/collections/usb-c-to-usb-c-cable',
   [["Anker 515 USB-C to USB-C Cable","Anker"],["Anker 643 USB-C to USB-C Cable","Anker"],["Anker Prime USB-C to USB-C Cable","Anker"]], t=['USB-C','USB-A','Lightning','Thunderbolt']),
 K('Display cable', 'Cable that carries video from a computer to a screen.', 'https://ldlc.com/en/product/PB00488989.html', [],
   t=['HDMI','DisplayPort','Mini DisplayPort','USB-C/Thunderbolt video'], a='HDMI cable · DisplayPort cable'),
 K('USB hub & adapter', 'Device that turns one USB port into several, or converts one connector to another.', 'https://www.anker.com/collections/multi-port-usb-hub',
   [["Anker 341 USB-C Hub (7-in-1)","Anker"],["Satechi Type-C Multi-Port Adapter V2","Satechi"]], t=['USB hub','USB-C multiport adapter','dongle/adapter'], a='USB-C hub · dongle'),
 K('Docking station', 'Base that carries power delivery and several outputs for a laptop, which an adapter or hub does not.', 'https://docking-stations.info/compare/caldigit-ts4-vs-kensington-sd5700t/',
   [["CalDigit TS4","CalDigit"],["Kensington SD5700T","Kensington"]], t=['Thunderbolt','USB-C']),
 K('KVM switch', 'Switch that shares one keyboard, display and mouse between several computers.', 'https://store.bsl-it.com/peripherals/kvm-switches.html?p=10',
   [["Belkin F1DN202KVM-UNN4","Belkin"],["StarTech P2ADD121D","StarTech"],["ATEN CS1798","ATEN"],["Lindy 4 Port HDMI KVM Switch 32810","Lindy"]], t=['2-port','4-port','HDMI','DisplayPort']),
], notes='HDMI cable and DisplayPort cable merged into Display cable (no models in old data). Other adapters merged into USB hub & adapter. USB cable: dropped Nintendo console charging cables (they follow their console in Video Games). KVM switch cut from 10 to 4, dropping rack/enterprise units (ATEN CS17916, CS18208, CS19208) and older VGA/DVI StarTech units.')

J['07_01'] = dict(kinds=[
 K('Multi-device charger', 'Charger for many devices (USB, GaN or Qi); a charger made for one device follows it.', 'https://homescreen.pl/en/115244-ugreen-x513-30w-gan-usb-c-wall-charger-1m-usb-c-cable-white.html',
   [["Ugreen X513 GaN","Ugreen"]], t=['GaN multi-port','desktop charging station','wireless (Qi)'], a='generic charger'),
 K('Laptop charger & battery', 'Spare-part power adapter or replacement battery made for one laptop.', 'https://ldlc.com/en/product/PB00495610.html',
   [["Dell 65W Power Adapter NK6FN","Dell"]], t=['AC adapter','replacement battery'], a='laptop AC adapter · laptop battery'),
 K('UPS', 'Uninterruptible power supply that keeps equipment running through a mains failure. A portable power station is in Climate, Water & Energy.', 'https://www.cyberpowersystems.com/product/ups/pfc-sinewave/cp1500pfclcd/',
   [["Back-UPS Pro BX1500M","APC (Schneider Electric)"],["CP1500PFCLCD","CyberPower Systems"],["Eaton 5S UPS","Eaton"]], t=['standby','line-interactive','pure sine wave'], a='uninterruptible power supply'),
], notes='Laptop charger and Laptop battery merged into one spare-parts kind. Nothing dropped.')

J['08_01'] = dict(kinds=[
 K('Resistor', 'Passive component that resists current, fixed or variable.', 'https://www.mouser.com/c/passive-components/resistors/', [], t=['fixed','potentiometer/trimmer','thermistor (NTC/PTC)','varistor'], a='potentiometer · thermistor · varistor'),
 K('Capacitor', 'Passive component that stores charge.', 'https://www.mouser.com/electronic-components/', [], t=['ceramic','electrolytic','film','tantalum','supercapacitor']),
 K('Inductor & transformer', 'Passive component that stores energy in a magnetic field or transfers it between coils.', 'https://www.mouser.com/electronic-components/', [], t=['inductor','choke','transformer']),
 K('Crystal or oscillator', 'Loose frequency-control component (quartz crystal, resonator or oscillator).', 'https://www.mouser.com/electronic-components/', [], t=['quartz crystal','ceramic resonator','oscillator']),
 K('Transistor', 'Loose semiconductor used as a switch or amplifier.', 'https://www.mouser.com/electronic-components/', [["IRF540N",""]], t=['BJT','MOSFET'], a='MOSFET'),
 K('Diode', 'Loose semiconductor that lets current pass one way.', 'https://www.mouser.com/electronic-components/', [], t=['rectifier','Zener','Schottky']),
 K('LED', 'Loose light-emitting diode for circuits. A lamp or bulb is in Lighting.', 'https://www.mouser.com/electronic-components/', [], t=['through-hole','SMD','addressable (WS2812)']),
 K('Microcontroller chip', 'Loose integrated circuit that holds a processor, memory and ports.', 'https://www.mouser.com/electronic-components/', [["ATmega328P","Microchip"]]),
 K('Sensor', 'Loose component or breakout module that senses a physical quantity.', 'https://www.mouser.com/electronic-components/', [["BME280","Bosch"],["Adafruit BME280 breakout","Adafruit"],["Arduino Modulino Thermo","Arduino"]], t=['bare chip','breakout module']),
 K('Relay', 'Loose switch operated by an electromagnet.', 'https://www.mouser.com/electronic-components/', [], t=['electromechanical','solid-state','relay module']),
 K('Component connector', 'Loose connector for circuit boards and wiring.', 'https://www.mouser.com/electronic-components/', [], t=['pin headers','JST','Dupont','terminal blocks']),
 K('Blank RFID tag or card', 'Unissued RFID tag or card. An issued card is in Documents & Personal Records.', 'https://makerselectronics.com/product/nfc-card-13-56mhz-ntag215-chip-white/', [["NTAG215","NXP"]], t=['card','sticker','key fob']),
], notes='Potentiometer, Thermistor and Varistor merged into Resistor as types; Transformer merged with Inductor; MOSFET became Transistor. Kind level kept, with only the few old example parts.')

only = sys.argv[1:] or list(J)
for job in only:
    p = B + job + '.json'; tmp = p + '.tmp'
    json.dump(J[job], open(tmp, 'w'), ensure_ascii=False, indent=1); os.replace(tmp, p); print('wrote', p)
