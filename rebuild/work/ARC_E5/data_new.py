LH="https://en.wikipedia.org/wiki/List_of_home_video_game_consoles"
LD="https://en.wikipedia.org/wiki/List_of_dedicated_consoles"
LR="https://en.wikipedia.org/wiki/List_of_retro_style_video_game_consoles"
LHH="https://en.wikipedia.org/wiki/List_of_handheld_game_consoles"
MC="https://en.wikipedia.org/wiki/Microconsole"
LL="https://liliputing.com/compare-handheld-gaming-pc-specs-anbernic-ayn-aya-gpd-onexplayer-and-valve/"
RH="https://retrohandheldhq.com/posts/best-handheld-emulators/"
GW="https://en.wikipedia.org/wiki/Game_%26_Watch"
GEN={2:"Second generation (1976–1992)",3:"Third generation (1983–2003)",4:"Fourth generation (1987–2004)",5:"Fifth generation (1993–2006)",6:"Sixth generation (1998–2013)",7:"Seventh generation (2005–2017)",8:"Eighth generation (2012–present)",9:"Ninth generation (2020–present)"}
def gen(y):
    y=int(y)
    for lim,g in((1982,2),(1986,3),(1992,4),(1997,5),(2004,6),(2011,7),(2019,8)):
        if y<=lim: return g
    return 9
# home consoles new: name, maker, year, gen-override, aliases, desc
HOME_NEW=[
("RCA Studio II","RCA","1977",None,"","Early cartridge console from RCA, listed beside the Channel F and Atari 2600."),
("Champion 2711","Unisonic","1978",None,"","Unisonic's cartridge console of the late 1970s."),
("Interton VC 4000","Interton","",2,"","German cartridge console of the second generation."),
("1292 Advanced Programmable Video System","Audiosonic","",2,"","Cartridge console sold under the Audiosonic name."),
("APF Imagination Machine","APF","1979",None,"","APF's computer-and-console system that extends its console line."),
("Bandai Super Vision 8000","Bandai","",2,"","Bandai's cartridge console of the second generation."),
("VTech CreatiVision","VTech","1981",None,"","VTech's first cartridge console, with a keyboard add-on."),
("Compact Vision TV Boy","Gakken","1983",None,"","Gakken's Japanese cartridge console."),
("Videopac+ G7400","Philips","1983",None,"Odyssey³ Command Center (planned US name)","Philips's upgraded Odyssey 2 line with improved graphics."),
("My Vision","Nichibutsu","",3,"","Nichibutsu's Japanese cartridge console."),
("Pyuuta Jr.","Tomy","1983",None,"","Tomy's Japanese home computer-console."),
("PV-1000","Casio","1983",None,"","Casio's Japanese cartridge console."),
("Super Cassette Vision","Epoch","1984",None,"","Epoch's successor to the Cassette Vision."),
("Bridge Companion","Heber","1985",None,"","Chess-playing unit with a cartridge game system from BBC and Heber."),
("Video Art","LJN","",3,"","LJN's cartridge console."),
("Zemmix","Daewoo","",3,"","Daewoo's Korean MSX-based game system."),
("Videosmarts","Connor Electronics","1986",None,"","Educational cartridge console sold by Connor Electronics and VTech."),
("Video Challenger","Tomy","",4,"","Tomy's laserdisc-style video game system."),
("Action Max","Worlds of Wonder","",4,"","Worlds of Wonder's video-tape-based light-gun game system."),
("View-Master Interactive Vision","View-Master Ideal Group","1988",None,"","Tape-based interactive video system from View-Master Ideal Group."),
("Terebikko","Bandai","",4,"","Bandai's telephone-style interactive video toy console."),
("VTech Socrates","VTech","",4,"","VTech's educational console."),
("Video Driver","Sega","1988",None,"Family Driver","Sega's driving-game system for children."),
("SuperGrafx","NEC","1989",None,"PC Engine2","Higher-spec follow-up to the PC Engine."),
("Commodore 64 Games System","Commodore","1990",None,"","Cartridge console built on Commodore 64 hardware."),
("CDTV","Commodore","1991",None,"","Commodore's CD-based multimedia console."),
("Picno","Konami","1992",None,"","Konami's Japanese educational game console."),
("Video Information System","Memorex","1992",None,"","Memorex and Tandy's CD-based home system."),
("FM Towns Marty","Fujitsu","1993",None,"","Fujitsu's console version of the FM Towns computer."),
("CPS Changer","Capcom","1994",None,"","Capcom's home unit that plays CP System arcade boards."),
("Neo Geo CD","SNK","1994",None,"","CD-based version of the Neo Geo home system."),
("Playdia","Bandai","1994",None,"","Bandai's CD-based interactive video console."),
("Super A'Can","Funtech","1995",None,"","Taiwanese 16-bit cartridge console."),
("Nuon","VM Labs","2000",None,"","DVD-player console platform from VM Labs."),
("DVD Kids","3-Plus","2002",None,"","Icelandic DVD-based children's game system."),
("Xavix PORT","SSD Company Limited","2004",None,"","Japanese sports-game console family from SSD Company."),
("Advanced Pico Beena","Sega","2005",None,"","Sega's educational children's console, successor to the Pico."),
("Game Wave Family Entertainment System","ZAPiT Games","2005",None,"","DVD-based family game console from ZAPiT Games."),
("V.Smile Baby Infant Development System","VTech","2006",None,"","VTech's infant-oriented version of the V.Smile line."),
("V.Flash","VTech","2006",None,"","VTech's disc-based educational console."),
("HyperScan","Mattel","2006",None,"","Mattel's card-driven console tied to trading cards."),
("Sport Vii","JungleTac","2007",None,"","Motion-controlled sports game system from JungleTac."),
("Zeebo","TecToy","2009",None,"","Brazilian console for downloadable games."),
("CT510","eedoo","2012",None,"","Chinese motion-game console listed for 2012."),
("Nex Playground","Nex Team Inc.","2023",None,"","Camera-based family console from Nex Team."),
]
# Plug-and-play etc handled in build script
