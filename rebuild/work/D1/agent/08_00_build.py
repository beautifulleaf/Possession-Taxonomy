import json, os
WK="https://en.wikipedia.org/wiki/"
def v(n,mk="",y="",d=""):
    o={"n":n,"mk":mk}
    if y:o["y"]=y
    if d:o["d"]=d
    return o
RP="Raspberry Pi"; AR="Arduino"; ES="Espressif"; AD="Adafruit"; RPW=WK+"Raspberry_Pi"
sbc={"n":"Single-board computer","a":"SBC","d":"Complete computer on one board that runs an operating system, even when a microcontroller sits beside it.",
 "t":["ARM","x86","RISC-V","AI / GPU accelerated","keyboard computer"],"s":"https://core-electronics.com.au/raspberry-pi-5-model-b-4gb.html.plain.md",
 "x":[
 {"n":"Raspberry Pi (Model B line)","a":"Raspberry Pi","d":"Credit-card-sized, low-cost ARM computer from the UK.","mk":RP,"y":"2012","s":RPW,
  "v":[v("Model B",RP,"2012"),v("Model A",RP,"2013"),v("Model B+",RP,"2014"),v("Model A+",RP,"2014"),v("Raspberry Pi 2",RP,"2015"),v("Raspberry Pi 3",RP,"2016"),v("Raspberry Pi 3 Model B+",RP,"2018"),
       v("Raspberry Pi 3 Model A+",RP,"2018"),v("Raspberry Pi 4",RP,"2019"),v("Raspberry Pi 5 Model B",RP,"2023")],"dt":"RAM size · case and cooler"},
 {"n":"Raspberry Pi Zero","a":"Pi Zero","d":"Smallest, cheapest Raspberry Pi board.","mk":RP,"y":"2015","s":RPW,
  "v":[v("Raspberry Pi Zero",RP,"2015"),v("Raspberry Pi Zero W",RP,"2017","adds wireless"),v("Raspberry Pi Zero 2 W",RP,"2021")],"dt":"with or without header"},
 {"n":"Raspberry Pi 400 / 500","a":"","d":"Raspberry Pi built into a keyboard as a complete desktop computer.","mk":RP,"y":"2020","s":RPW,
  "v":[v("Raspberry Pi 400",RP,"2020"),v("Raspberry Pi 500",RP,"2024"),v("Raspberry Pi 500+",RP,"2025")],"dt":"keyboard layout"},
 {"n":"Raspberry Pi Compute Module","a":"CM","d":"Raspberry Pi in module form for building into carrier boards and products.","mk":RP,"y":"2014","s":RPW,
  "v":[v("Compute Module 1",RP,"2014"),v("Compute Module 3",RP,"2017"),v("Compute Module 4",RP,"2020"),v("Raspberry Pi Compute Module 5",RP,"2024")],"dt":"RAM · eMMC · wireless"},
 {"n":"BeagleBoard / BeagleBone","a":"Beagle","d":"Texas Instruments-designed open-hardware boards from BeagleBoard.org.","mk":"BeagleBoard.org","y":"2008","s":WK+"BeagleBoard",
  "v":[v("BeagleBoard","BeagleBoard.org","2008"),v("BeagleBoard-xM","BeagleBoard.org","2010"),v("BeagleBone","BeagleBoard.org","2011"),v("BeagleBone Black","BeagleBoard.org","2013"),v("PocketBeagle","BeagleBoard.org","2017"),
       v("BeagleBone AI","BeagleBoard.org","2019"),v("BeagleBone AI-64","BeagleBoard.org","2022"),v("BeaglePlay","BeagleBoard.org","2023"),v("BeagleV-Ahead","BeagleBoard.org","2023","RISC-V")],"dt":"processor · I/O headers"},
 {"n":"Orange Pi","a":"","d":"Low-cost ARM single-board computers from Shenzhen Xunlong.","mk":"Orange Pi","y":"2014","s":WK+"Orange_Pi",
  "v":[v("Orange Pi 5 Ultra","Orange Pi"),v("Orange Pi Prime","Orange Pi"),v("Orange Pi R1","Orange Pi"),v("Orange Pi RV","Orange Pi","","RISC-V"),v("Orange Pi AIpro","Orange Pi")],"dt":"RAM · processor"},
 {"n":"NVIDIA Jetson Nano","a":"Jetson","d":"GPU-equipped developer board for AI and hobbyist robotics.","mk":"Nvidia","y":"2019","s":WK+"Nvidia_Jetson",
  "v":[v("Jetson Nano","Nvidia","2019","Maxwell GPU, 4 GB"),v("Jetson Orin Nano","Nvidia","2022","Ampere GPU; updated 2024")],"dt":"developer kit or module"},
 {"n":"LattePanda","a":"","d":"x86 single-board computer running Windows or Linux, with an Arduino Leonardo co-processor.","mk":"DFRobot","y":"","s":"https://community.element14.com/products/devtools/product-pages/w/documents/23032/lattepanda---single-board-computer",
  "v":[v("LattePanda V1.0","DFRobot","","Intel Z8350, 2 GB/32 GB or 4 GB/64 GB")],"dt":"RAM · eMMC · Windows licence"}],
 "m":[["FS-FP5V","Sapphire"]]}
mcu={"n":"Microcontroller board","a":"dev board · development board","d":"Board that runs one program on a microcontroller, programmed over USB.","t":["8-bit AVR","ARM Cortex-M","Wi-Fi / Bluetooth","RISC-V"],
 "s":"https://www.mouser.se/arduino-uno-rev-4-boards",
 "x":[
 {"n":"Arduino Uno","a":"Uno","d":"Arduino's standard-size board with headers for stacking shields.","mk":AR,"y":"2010","s":WK+"Arduino_Uno",
  "v":[v("Arduino UNO REV3",AR,"","ATmega328P"),v("Arduino Uno WiFi REV2",AR),v("Arduino UNO R4 Minima",AR,"2023","Renesas RA4M1"),v("Arduino UNO R4 WiFi",AR,"2023","adds ESP32-S3 and LED matrix"),v("Arduino Uno Q",AR,"2025","runs Linux")],"dt":"DIP or SMD chip · header type"},
 {"n":"Arduino Mega","a":"","d":"Large Arduino board with many more pins for bigger projects.","mk":AR,"y":"","s":WK+"Arduino_Uno","v":[v("Arduino Mega 2560 Rev3",AR,"","ATmega2560")],"dt":""},
 {"n":"Arduino Nano","a":"","d":"Breadboard-friendly small Arduino board.","mk":AR,"y":"","s":WK+"Arduino",
  "v":[v("Arduino Nano",AR,"","ATmega328P"),v("Arduino Nano 33 BLE Sense Rev2",AR),v("Arduino Nano ESP32",AR)],"dt":"with or without headers"},
 {"n":"ESP8266 boards","a":"NodeMCU · D1 mini","d":"Cheap Wi-Fi microcontroller boards built on Espressif's ESP8266 chip.","mk":ES,"y":"2014","s":WK+"ESP8266",
  "v":[v("ESP-01","Ai-Thinker","2014","module that popularised the chip"),v("NodeMCU DEVKIT","","","ESP-12 module, USB serial"),v("Wemos D1 mini","WeMos")],"dt":"flash size · module"},
 {"n":"ESP32 boards","a":"","d":"Low-cost Wi-Fi and Bluetooth microcontroller boards on Espressif's ESP32 family.","mk":ES,"y":"2016","s":WK+"ESP32",
  "v":[v("ESP32-DevKitC",ES),v("ESP32 DEVKIT V1","","","widely copied pinout"),v("ESP32-CAM","","","camera board"),v("Adafruit HUZZAH32",AD),v("ESP32-S3 boards",ES,"","dual-core LX7, USB OTG"),v("ESP32-C3 / C6 boards",ES,"","RISC-V")],"dt":"chip variant · antenna · flash"},
 {"n":"BBC micro:bit","a":"micro:bit","d":"Pocket-sized educational board with LED matrix and buttons, designed by the BBC for UK schools.","mk":"Micro:bit Educational Foundation","y":"2016","s":WK+"Micro_Bit",
  "v":[v("micro:bit v1","Micro:bit Educational Foundation","2016","nRF51822"),v("micro:bit v2","Micro:bit Educational Foundation","2020","nRF52833, microphone and speaker")],"dt":"board alone or go kit"},
 {"n":"Teensy","a":"","d":"Small, fast Arduino-compatible boards from PJRC.","mk":"PJRC","y":"","s":WK+"Teensy",
  "v":[v("Teensy 2.0","PJRC"),v("Teensy++ 2.0","PJRC"),v("Teensy 3.0","PJRC"),v("Teensy 3.1/3.2","PJRC"),v("Teensy 3.5","PJRC"),v("Teensy 3.6","PJRC"),v("Teensy LC","PJRC"),v("Teensy 4.0","PJRC")],"dt":"with or without pins"},
 {"n":"Raspberry Pi Pico","a":"Pico","d":"Raspberry Pi's own low-cost microcontroller board.","mk":RP,"y":"2021","s":RPW,
  "v":[v("Raspberry Pi Pico",RP,"2021","RP2040"),v("Raspberry Pi Pico H",RP,"","with headers"),v("Raspberry Pi Pico W",RP,"2022","wireless"),v("Raspberry Pi Pico WH",RP),v("Raspberry Pi Pico 2",RP,"2024")],"dt":"with or without headers"},
 {"n":"Adafruit Feather","a":"Feather","d":"Adafruit's family of Arduino-like boards sharing one form factor and pinout.","mk":AD,"y":"","s":WK+"Adafruit_Industries",
  "v":[v("Adafruit Feather M0 WiFi",AD),v("Adafruit Feather RP2040",AD),v("Adafruit Feather nRF52840 Sense",AD)],"dt":"microcontroller · radio"},
 {"n":"Adafruit Circuit Playground","a":"","d":"Round teaching board with built-in LEDs and sensors.","mk":AD,"y":"2016","s":WK+"Adafruit_Industries",
  "v":[v("Circuit Playground",AD,"2016","ATmega32u4"),v("Circuit Playground Express",AD,"2017","SAMD21")],"dt":""},
 {"n":"Seeed Studio XIAO","a":"XIAO","d":"Fingernail-sized development boards on many chip platforms.","mk":"Seeed Studio","y":"","s":"https://wiki.seeedstudio.com/xiao_topic_page",
  "v":[v("XIAO SAMD21","Seeed Studio"),v("XIAO RP2040","Seeed Studio"),v("XIAO nRF52840 (Sense)","Seeed Studio"),v("XIAO ESP32C3","Seeed Studio"),v("XIAO ESP32S3 (Sense)","Seeed Studio"),v("XIAO ESP32C6","Seeed Studio"),v("XIAO RP2350","Seeed Studio"),v("XIAO RA4M1","Seeed Studio")],"dt":"Sense versions add sensors"}],
 "m":[["Arduino Leonardo",AR],["Arduino Micro",AR],["Arduino Due",AR],["Arduino MKR WiFi 1010",AR],["FeatherS3[D]","Unexpected Maker"]]}
add={"n":"Maker add-on board","a":"HAT · shield · FeatherWing","d":"Board made to plug onto one maker-board family's header (HAT, shield, FeatherWing).","t":["display","motor driver","audio / DAC","networking / PoE","sensor","storage (M.2)","AI accelerator"],
 "s":"https://www.raspberrypi.com/products/",
 "x":[
 {"n":"Raspberry Pi HAT","a":"HAT · HAT+","d":"Add-on board for the Raspberry Pi GPIO header, identified to the Pi over the HAT ID bus.","mk":RP,"y":"","s":RPW,
  "v":[v("Sense HAT",RP),v("PoE+ HAT",RP),v("M.2 HAT+",RP),v("AI HAT+",RP),v("AI HAT+ 2",RP),v("Build HAT",RP),v("TV HAT",RP),v("DAC+",RP),v("DAC Pro",RP),v("DigiAMP+",RP),v("Codec Zero",RP)],"dt":"full-size or Zero-size"},
 {"n":"Arduino shield","a":"shield","d":"Add-on board that stacks onto an Arduino's headers, e.g. for motors, displays, Ethernet or GPS.","mk":AR,"y":"","s":WK+"Arduino","v":[],"dt":"made by Arduino and by SparkFun, Adafruit, Seeed"},
 {"n":"FeatherWing","a":"","d":"Adafruit expansion board for Feather boards: displays, NeoPixels, motor drivers.","mk":AD,"y":"","s":WK+"Adafruit_Industries","v":[],"dt":"stacking or side-by-side"}]}
kit={"n":"Electronics starter kit","a":"Arduino kit · component kit","d":"Boxed set of a board, components and project guide for learning electronics, or a component assortment.","t":["board + project book","component assortment"],
 "s":"https://craftingtable.com/best-arduino-kit",
 "m":[["Arduino Starter Kit",AR],["SparkFun Inventor's Kit for Arduino Uno v4.1","SparkFun Electronics"],["Super Starter Kit","Elegoo"],["Starter Kit","SunFounder"],["30 Days Lost in Space","CraftingTable"],["SparkFun 1/4W Resistor Kit (500)","SparkFun Electronics"]]}
bb={"n":"Breadboard & prototyping board","a":"protoboard · perfboard · stripboard","d":"Board for building trial circuits: solderless breadboards with spring clips, or soldered perfboard and stripboard.","t":["solderless breadboard","perfboard","stripboard","jumper wires"],"s":WK+"Breadboard"}
K="knowledge"
brands=[
 {"n":RP,"c":"United Kingdom","f":"2008","seg":"Mainstream","kf":"single-board computers","d":"UK foundation and company behind the Raspberry Pi computers and Pico boards.","lines":["Raspberry Pi","Zero","Compute Module","Pico"],"sig":["Raspberry Pi (Model B line)","Raspberry Pi Pico"],"s":RPW},
 {"n":AR,"c":"Italy","f":"2005","seg":"Mainstream","kf":"microcontroller boards","d":"Italian open-source hardware company, begun at Interaction Design Institute Ivrea, now owned by Qualcomm.","lines":["Uno","Nano","Mega","MKR"],"sig":["Arduino Uno"],"s":WK+"Arduino"},
 {"n":ES,"c":"China","seg":"Value","kf":"Wi-Fi microcontrollers","d":"Shanghai chip maker of the ESP8266 and ESP32.","sig":["ESP8266 boards","ESP32 boards"],"s":WK+"ESP32"},
 {"n":AD,"c":"USA","f":"2005","seg":"Specialist","kf":"maker boards","d":"Brooklyn maker-electronics company founded by Limor Fried.","lines":["Feather","Circuit Playground"],"sig":["Adafruit Feather","FeatherWing"],"s":WK+"Adafruit_Industries"},
 {"n":"PJRC","c":"USA","seg":"Artisan & independent","kf":"Teensy","d":"Small company making the Teensy boards.","sig":["Teensy"],"s":K},
 {"n":"Micro:bit Educational Foundation","c":"United Kingdom","f":"2016","seg":"Institution & issuer","kf":"micro:bit","d":"Not-for-profit that took over the BBC micro:bit in 2016.","sig":["BBC micro:bit"],"s":WK+"Micro_Bit"},
 {"n":"BeagleBoard.org","c":"USA","seg":"Specialist","kf":"open-hardware SBCs","d":"Organisation behind the TI-designed BeagleBoard and BeagleBone boards.","sig":["BeagleBoard / BeagleBone"],"s":WK+"BeagleBoard"},
 {"n":"Orange Pi","c":"China","seg":"Value","kf":"low-cost SBCs","d":"Single-board computer brand of Shenzhen Xunlong Software.","sig":["Orange Pi"],"s":WK+"Orange_Pi"},
 {"n":"Nvidia","c":"USA","f":"1993","seg":"Professional & flagship","kf":"GPUs","d":"US graphics-chip company whose Jetson boards target AI and robotics.","sig":["NVIDIA Jetson Nano"],"s":K},
 {"n":"DFRobot","c":"China","seg":"Value","kf":"LattePanda","d":"Chinese maker-electronics company behind the LattePanda boards.","sig":["LattePanda"],"s":K},
 {"n":"Seeed Studio","c":"China","seg":"Value","kf":"XIAO boards","d":"Shenzhen maker-hardware company known for XIAO and Grove products.","sig":["Seeed Studio XIAO"],"s":K},
 {"n":"SparkFun Electronics","c":"USA","seg":"Specialist","kf":"kits and breakouts","d":"US maker-electronics retailer and designer of kits and breakout boards.","s":K}]
notes="All four old kinds kept (k10, k101, k102, k103; component kit renamed Electronics starter kit and widened to learning kits); new kind Breadboard & prototyping board added. Old flat models folded into Raspberry Pi, Arduino, Pico, Feather and HAT archetype versions; old range 'Pico 1' dropped as a duplicate of Raspberry Pi Pico. Not added for lack of a retrieved page: Radxa/Rock Pi, M5Stack, SparkFun RedBoard, Teensy 4.1, Seeed XIAO and Teensy years, Orange Pi model years."
out={"kinds":[sbc,mcu,add,kit,bb],"brands":brands,"traditions":[],"notes":notes}
p="work/D1/shelves/08_00.json"; json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
