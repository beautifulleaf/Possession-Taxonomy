HC='https://en.wikipedia.org/wiki/List_of_home_computers'
# (name, maker, year) -- every row of the fetched list; siblings folded as versions where noted in FOLD
ROWS=[
('Honeywell 316 Kitchen Computer','Honeywell','1969'),
('Apple II','Apple','1977'),('Commodore PET','Commodore','1977'),('TRS-80','Tandy Corporation','1977'),
('Bally Astrocade','Bally','1977'),('COSMAC VIP','RCA','1977'),('Compucolor II','Compucolor','1977'),
('Sord M200 Smart Home Computer','Sord','1977'),('VideoBrain Family Computer','VideoBrain','1977'),
('Exidy Sorcerer','Exidy','1978'),('ABC 80','Luxor','1978'),('CyberVision 2001','','1978'),
('Atari 8-bit computers','Atari','1979'),('TI-99/4A','Texas Instruments','1979'),('Bally Brain','Bally','1979'),
('Imagination Machine','Bally','1979'),('Interact Home Computer','Interact','1979'),('Hector 1','Micronique','1979'),
('NEC PC-8000 series','NEC','1979'),('Sharp MZ series','Sharp','1979'),('Apple II clones','','1979'),
('Acorn Atom','Acorn Computers','1980'),('Commodore VIC-20','Commodore','1980'),('Sinclair ZX80 / ZX81','Sinclair Research','1980'),
('DAI Personal Computer','DAI','1980'),('Philips P2000','Philips','1980'),('IMKO-1','','1980'),('Video Genie family','EACA','1980'),
('TRS-80 Color Computer','Tandy Corporation','1980'),
('BBC Micro','Acorn Computers','1981'),('IBM Personal Computer','IBM','1981'),('NEC PC-8800','NEC','1981'),('NEC PC-6000 series','NEC','1981'),
('Galeb','','1981'),('Poly-1','','1981'),
('Sinclair ZX Spectrum','Sinclair Research','1982'),('ZX Spectrum','Sinclair Research','1982'),
('Commodore 64','Commodore','1982'),('Dragon 32 / 64','Dragon Data','1982'),('NEC PC-9800','NEC','1982'),
('Sharp X1','Sharp','1982'),('FM-7 series','Fujitsu','1982'),('Franklin ACE series','Franklin','1982'),('Grundy NewBrain','Grundy','1982'),
('Jupiter Ace','Jupiter Cantab','1982'),('Sord M5','Sord','1982'),('Thomson TO7','Thomson','1982'),('Timex Sinclair 1000 and 1500','Timex','1982'),
('Pravetz 8D','','1982'),('Aster CT-80','','1982'),('MAX Machine','Commodore','1982'),
('Acorn Electron','Acorn Computers','1983'),('Colour Genie','EACA','1983'),('Comx-35','Comx','1983'),('Aquarius','Mattel','1983'),
('Matra Alice','Matra','1983'),('Memotech MTX500 / MTX512 / RS128','Memotech','1983'),('MicroBee series','Microbee','1983'),
('Microprofessor III','Multitech','1983'),('NEC PC-100','NEC','1983'),('TRS-80 MC-10','Tandy Corporation','1983'),('Oric-1','Oric','1983'),
('G7480','','1983'),('SC-3000','Sega','1983'),('SPC-1000','Samsung','1983'),('SV-318','Spectravideo','1983'),('Timex Computer 2068','Timex','1983'),
('Coleco Adam','Coleco','1983'),('Rabbit RX83','','1983'),('Lynx','','1983'),('PC-100','','1983'),('Ivel Z3','Ivel','1983'),
('Macintosh','Apple','1984'),('Amstrad CPC','Amstrad','1984'),('IBM PCjr','IBM','1984'),('Sinclair QL','Sinclair Research','1984'),
('Apricot F1','Apricot','1984'),('Commodore 16 / 116 / Plus/4','Commodore','1984'),('Tatung Einstein','Tatung','1984'),
('Aamber Pegasus','','1984'),('AGAT-9','','1984'),('EXL 100','Exelvision','1984'),('Ivel Ultra','Ivel','1984'),('KC 85','','1984'),
('MO5','Thomson','1984'),('Mindset','Mindset Corporation','1984'),('Oric Atmos','Oric','1984'),('Orao','','1984'),
('Primo','','1984'),('Prologica CP-400','Prologica','1984'),('Timex Computer 2048','Timex','1984'),('West PC-800','','1984'),('Timex Sinclair 2048','Timex','1984'),
('Atari ST','Atari Corporation','1985'),('Commodore 128','Commodore','1985'),('Commodore Amiga','Commodore','1985'),('Amstrad PCW','Amstrad','1985'),
('BK-0010','','1985'),('CCE MC-1000','CCE','1985'),('Enterprise 64 / 128','Enterprise Computers','1985'),('Gradiente Expert','Gradiente','1985'),
('Lambda 8300','','1985'),('Pecom 32 / 64','Elektronska Industrija','1985'),('Philips :YES','Philips','1985'),('Pravetz series 8','','1985'),
('VTech Laser 200','VTech','1985'),('TK82C series','Microdigital','1985'),('Z1013','','1985'),('PMD 85','Tesla','1985'),('GEM 1000','','1985'),
('Amstrad PC1512','Amstrad','1986'),('Acorn Master','Acorn Computers','1986'),('Apple IIGS','Apple','1986'),('CEC-I Zhonghua teaching machine','','1986'),
('CoBra','','1986'),('Komputer 2086','Timex','1986'),('Oric Telestrat','Oric','1986'),('Tomy Tutor','Tomy','1986'),('TVC','Videoton','1986'),
('VG5000','Philips','1986'),('Alpha / Beta','','1986'),('AI Computer','','1986'),
('Acorn Archimedes','Acorn Computers','1987'),('Sharp X68000','Sharp','1987'),('Tandy 1000','Tandy Corporation','1987'),('Vector-06C','','1987'),
('KC 87','','1987'),('SPC-1500','Samsung','1987'),('Gama','','1987'),
('Euro PC','Amstrad','1988'),('FM Towns series','Fujitsu','1989'),('SAM Coupe','MGT','1989'),('Iskra-1030','','1989'),('MATO','','1989'),
('Atari TT / Falcon','Atari Corporation','1990'),('IBM PS/1','IBM','1990'),('Hobbit','','1990'),('Dubna 48K','','1991'),
('Acorn A7000','Acorn Computers','1995'),
]
FOLD_NOTE={'Sinclair ZX Spectrum','ZX Spectrum'}
def era(y):
    y=int(y)
    if y<=1979: return 'Pioneers (to 1979)'
    if y<=1982: return 'Early 1980s (1980–1982)'
    if y<=1985: return 'Mid 1980s (1983–1985)'
    return 'Late period (1986 onward)'
# map existing entry names -> row names (existing entries supply d, v, s)
MAP={'TRS-80':'TRS-80','Atari 8-bit computers':'Atari 8-bit computers','Sinclair ZX80 / ZX81':'Sinclair ZX80 / ZX81','Commodore VIP':None,
 'Commodore VIC-20':'Commodore VIC-20','BBC Micro':'BBC Micro','ZX Spectrum':'ZX Spectrum','Commodore 64':'Commodore 64','Acorn Electron':'Acorn Electron',
 'Amstrad CPC':'Amstrad CPC','Atari ST':'Atari ST','TI-99/4A':'TI-99/4A','Sinclair QL':'Sinclair QL','Dragon 32 / 64':'Dragon 32 / 64','Commodore Amiga':'Commodore Amiga',
 'Commodore 128':'Commodore 128','Acorn Atom':'Acorn Atom','Commodore PET':'Commodore PET','Apple II':'Apple II','NEC PC-8800':'NEC PC-8800',
 'IBM Personal Computer':'IBM Personal Computer','NEC PC-9800':'NEC PC-9800','Compact Macintosh':'Macintosh','Amstrad PCW':'Amstrad PCW',
 'Acorn Archimedes':'Acorn Archimedes','Sharp X68000':'Sharp X68000','IBM PCjr':'IBM PCjr','Tandy 1000':'Tandy 1000','Amstrad PC1512':'Amstrad PC1512'}
SKIP_ROWS={'Sinclair ZX Spectrum'}  # duplicate spelling of ZX Spectrum
EXTRA_EXISTING=['MSX']  # kept: standard listed as 'Various models (1983)'
# keyboard switches
KD='https://en.wikipedia.org/wiki/Keyboard_technology'
KS_NEW=[ # (name, maker, year, desc, group, versions)
('Rubber-dome membrane','','','Full-travel keyboard design in which a rubber dome over a membrane acts as the return spring; the most common kind.','Dome and membrane',[]),
('Scissor switch','','','Low-profile rubber-dome variant with interlocking plastic pieces, mostly used in laptops.','Dome and membrane',[]),
('Flat-panel membrane','','','Sealed, leak-resistant keys used on early computers such as the ZX80, ZX81 and Atari 400.','Dome and membrane',[]),
('Reed switch','Bell Telephone Laboratories','1936','Magnetically operated metal leaf contacts sealed in a glass capsule.','Magnetic and optical',[]),
('Hall-effect switch','','','Magnet movement is read by solid-state sensors; allows adjustable actuation and rapid trigger.','Magnetic and optical',[]),
('Optical switch','','','Light beams blocked or altered by the key; resistant to dust and moisture.','Magnetic and optical',[]),
('Capacitive foam-and-foil','','','Pressing a key changes capacitance between pads on the board, so no debouncing is needed.','Capacitive',[]),
]
KS_GROUP={'Cherry MX':'Metal-contact mechanical','Alps SKCL/SKCM':'Metal-contact mechanical','Gateron KS-3':'Metal-contact mechanical','Kailh BOX':'Metal-contact mechanical',
 'Holy Panda':'Metal-contact mechanical','Zealio':'Metal-contact mechanical','NovelKeys Cream':'Metal-contact mechanical','IBM buckling spring':'Buckling spring',
 'Topre capacitive':'Capacitive','Wooting Lekker':'Magnetic and optical'}
KS_MAKER_ENTRIES=[ # from former loose models: maker families
('Kailh speed switches','Kailh','Speed Silver, Speed Copper and Speed Bronze short-travel switches.','Metal-contact mechanical',['Kailh Speed Silver','Kailh Speed Copper','Kailh Speed Bronze']),
('Logitech Romer-G and GL','Logitech','Logitech’s own gaming switches.','Metal-contact mechanical',['Logitech GL Linear','Logitech GL Tactile','Logitech GL Clicky','Logitech Romer-G Linear','Logitech Romer-G Tactile']),
('Razer switches','Razer','Razer’s own mechanical and optical switches.','Metal-contact mechanical',['Razer Optical Red','Razer Optical Purple','Razer Yellow','Razer Orange','Razer Green']),
('Outemu switches','Outemu','Cherry-style switches used in budget keyboards.','Metal-contact mechanical',['Outemu Red','Outemu Brown','Outemu Blue']),
('Drop Halo','Drop','Halo Clear and Halo True tactile switches.','Metal-contact mechanical',['Drop Halo Clear','Drop Halo True']),
('Roccat Titan','Roccat','Titan Linear and Titan Tactile optical switches.','Magnetic and optical',['Roccat Titan Linear','Roccat Titan Tactile']),
]
LAPTOP_G={'DynaBook':'Toshiba and Dynabook','Toshiba Libretto':'Toshiba and Dynabook','Panasonic Toughbook':'Panasonic','PowerBook':'Apple','iBook':'Apple','MacBook Pro':'Apple','MacBook Air':'Apple',
 'ThinkPad T series':'IBM and Lenovo','ThinkPad X series':'IBM and Lenovo','ThinkPad X1 Carbon':'IBM and Lenovo','Dell XPS':'Dell','HP EliteBook':'HP','HP Spectre':'HP','Razer Blade':'Razer','ASUS ROG Zephyrus':'ASUS','Microsoft Surface Laptop':'Microsoft','Framework Laptop':'Framework'}
