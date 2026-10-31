import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/D3/agent')
from lib import *
VT='https://vintagetechnics.co.uk/'; SC=WP+'Sony_CDP-101'; LN=WP+'Linn_Products'; QD=WP+'Quad_Electroacoustics'; NA=WP+'Naim_Audio'; RV=WP+'Revox'
kinds=[
K("CD player","compact disc player · CD transport · SACD player","Player for compact discs.",VT,
  ["CD only","SACD/CD","transport only","with DAC inputs","multi-disc changer"],
  [X("Sony CDP-101","Sony","1982",SC,"The first commercially released CD player, on sale in Japan from October 1982.",[("CDP-101","Sony","1982",""),("CDP-30","Sony","c. 1984","")]),
   X("Philips CD100","Philips","1983",SC,"Philips's first CD player, on sale in the US and Europe from March 1983."),
   X("Meridian MCD","Meridian","1985",WP+"Meridian_Audio","Described as the first audiophile CD player."),
   X("Marantz CD63","Marantz","",WP+"Marantz","Marantz's iconic CD player range, much modified by enthusiasts.",[("CD63","Marantz","",""),("CD63SE","Marantz","","")]),
   X("Quad CD players","Quad","1989",QD,"Quad's CD players made to match its amplifiers.",[("CD66","Quad","1989","to 1994"),("CD67","Quad","1993","to 1996"),("77CD","Quad","1996","to 1999"),("99CD","Quad","1999","")]),
   X("Naim CDS","Naim","1989",NA,"Naim's top CD player, announced 1989.",[("CDS","Naim","1989",""),("CDS2","Naim","1998",""),("CDS3","Naim","2002","")]),
   X("Linn Karik / Sondek CD12","Linn","1993",LN,"Linn's CD players, made until it switched to streaming in 2009.",[("Karik","Linn","1993","first Linn CD player"),("Sondek CD12","Linn","1997","discontinued 2005")]),
   X("Revox B225","Revox","",RV,"CD player heavily based on the Studer A725 and A727."),
  ],
  [("Cambridge Audio AX C35","Cambridge Audio"),("Denon DCD-3000NE","Denon"),("Denon DCD-900NE","Denon"),("Denon DCD-600NE","Denon"),("Marantz CD 70","Marantz"),("Marantz CD6007","Marantz"),("Technics SL-P1","Technics"),("Technics SL-P2","Technics"),("Technics SL-PG440","Technics")]),
K("Network streamer","music streamer · network player · music server","Hi-fi source that plays music from the network or streaming services into an audio system.","https://www.richersounds.com/hi-fi",
  ["streamer only","with DAC","with preamplifier","with storage (music server)"],
  [X("Linn DS","Linn","2007",LN,"Linn's network streamers; the Klimax DS (2007) launched its streaming strategy.",
     [("Klimax DS","Linn","2007","first"),("Akurate DS","Linn","",""),("Majik DS","Linn","",""),("Majik DS-I","Linn","2010","with amplifier"),("Sneaky DS","Linn","",""),("Selekt DSM","Linn","","")]),
   X("Squeezebox","Slim Devices","2001",WP+"Squeezebox_(network_music_player)","Network music players from Slim Devices, bought by Logitech in 2006; discontinued 2012.",
     [("SliMP3","Slim Devices","2001",""),("Squeezebox","Slim Devices","2003",""),("Squeezebox2","Slim Devices","2005",""),("Squeezebox Classic","Slim Devices","2005","SB3"),("Transporter","Slim Devices","2006","audiophile model"),("Squeezebox Duet","Slim Devices","2008",""),("Squeezebox Touch","Slim Devices","2010","")]),
   X("Naim Uniti","Naim","2009",NA,"Naim's range of one-box streaming players and amplifiers."),
   X("Meridian Sooloos","Meridian","2008",WP+"Meridian_Audio","Media server system Meridian gained by buying Sooloos in 2008."),
  ],
  [("Bluesound Node Icon","Bluesound"),("Bluesound Node N132","Bluesound"),("Bluesound Node Nano","Bluesound"),("Bluesound Vault 2i","Bluesound"),("Cambridge Audio CXN100 SE","Cambridge Audio"),("Cambridge Audio MXN10","Cambridge Audio"),("Denon DNP-2000NE","Denon"),("Eversolo DMP-A6","Eversolo"),("Eversolo DMP-A8","Eversolo"),("Rose RS151","Rose")]),
K("FM/DAB tuner","separate radio tuner · hi-fi tuner","Hi-fi separate that receives radio broadcasts for an amplifier, with no speaker of its own.",VT,
  ["FM","AM/FM","DAB / DAB+","with internet radio"],
  [X("Marantz Model 10B","Marantz","1964","https://www.psaudio.com/blogs/copper/the-saul-authority-the-story-of-hi-fi-pioneer-saul-marantz","Valve FM tuner designed with Richard Sequerra, a collector icon."),
   X("Quad FM3","Quad","1971",QD,"Quad FM tuner, made 1971–1982.",[("FM3","Quad","1971","to 1982"),("FM4","Quad","1982","to 1995")]),
   X("Accuphase T-100","Accuphase","1973",WP+"Accuphase","One of Kensonic (Accuphase)'s first products.",[("T-100","Accuphase","",""),("T-101","Accuphase","","upgraded")]),
   X("Revox B760","Revox","c. 1977",RV,"Revox synthesiser FM tuner."),
   X("Naim NAT 01","Naim","",NA,"Naim's top FM tuner, developed by Guy Lamotte."),
  ],
  [("NAD C 427","NAD"),("Technics ST-G90","Technics"),("Technics ST-Z1","Technics"),("Technics ST-8044","Technics"),("Technics ST-7300","Technics")]),
]
brands=[
 B("Sony","Japan","1946","Premium","consumer electronics","Tokyo electronics maker that co-developed the CD.","knowledge",["CDP-101"]),
 B("Philips","Netherlands","1891","Mainstream","consumer electronics","Eindhoven electronics maker that co-developed the CD.",WP+"Philips",["CD100"]),
 B("Meridian","United Kingdom","1977","Premium","digital audio","Huntingdon maker founded by Bob Stuart and Allen Boothroyd.",WP+"Meridian_Audio",["MCD","Sooloos"]),
 B("Marantz","United States","1953","Premium","amplifiers, CD players","Founded by Saul Marantz in New York.",WP+"Marantz",["Model 10B","CD63"]),
 B("Quad","United Kingdom","1936","Heritage manufactory","amplifiers, tuners","Founded by Peter Walker in London.",QD,["FM3","CD66"]),
 B("Naim","United Kingdom","1973","Premium","amplifiers, streamers","Salisbury maker founded by Julian Vereker.",NA,["CDS","NAT 01","Uniti"]),
 B("Linn","United Kingdom","1972","Premium","LP12, streaming","Glasgow hi-fi maker founded by Ivor Tiefenbrun.",LN,["Klimax DS","Sondek CD12"]),
 B("Revox","Switzerland","1951","Heritage manufactory","tape recorders","Willi Studer's consumer brand.",RV,["B225","B760"]),
 B("Accuphase","Japan","1972","Professional & flagship","amplifiers","Yokohama maker founded as Kensonic by Jiro Kasuga.",WP+"Accuphase",["T-100"]),
 B("Slim Devices","United States","","Specialist","Squeezebox","Maker of Squeezebox network players, bought by Logitech in 2006.",WP+"Squeezebox_(network_music_player)",["Squeezebox","Transporter"]),
 B("Cambridge Audio","United Kingdom","1968","Mainstream","affordable hi-fi","Founded as a division of Cambridge Consultants; now a London brand of Audio Partnership.",WP+"Cambridge_Audio",["CD1","CXN"]),
 B("Bluesound","Canada","","Mainstream","streamers","Lenbrook's wireless and streaming brand, sister to NAD.","knowledge",["Node"]),
]
notes=("All three kinds kept. CD player: 11 models cut to 9 (dropped Technics SL-P3, SL-P7) plus 8 archetypes; SACD and transport-only as types. Streamer: 12 cut to 10 (dropped Matrix Audio Mini-i Pro 4, SMSL DP5se). Tuner keeps 5 old models plus 5 archetypes. "
 "Left out (no retrieved page naming them): Philips CD104 / Marantz CD-63 lineage link, Meridian 207, Arcam Alpha CD, Cambridge CXC/CXN archetypes, Naim CDX/ND5, Bluesound Node, WiiM and Lumin archetypes, Sequerra Model 1 tuner.")
write('04_01',kinds,brands,notes)
