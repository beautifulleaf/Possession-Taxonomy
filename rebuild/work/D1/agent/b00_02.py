import json, os
W='https://en.wikipedia.org/wiki/'
def X(n,mk,y,s,d,v=(),a='',dt=''):
    x={'n':n,'a':a,'d':d,'mk':mk,'y':y,'s':(s if s.startswith('http') else W+s),'v':[dict(zip(('n','mk','y','d'),t)) for t in v]}
    if dt: x['dt']=dt
    return x
old={k['n']:k for k in json.load(open('work/D1/agent/00_02.old.json'))}
C='Commodore'; A='Apple'; AT='Atari'
home=[
 X('TRS-80','Tandy Corporation','1977','TRS-80','Tandy\'s Radio Shack computer line, one of the 1977 "Trinity" of ready-built micros.',
   [('TRS-80 Model I','Tandy Corporation','1977','keyboard unit with separate monitor'),('TRS-80 Model III','Tandy Corporation','1980','all-in-one successor'),('TRS-80 Color Computer','Tandy Corporation','1980',''),('TRS-80 Model 4','Tandy Corporation','1983','')]),
 X('Atari 8-bit computers','Atari','1979','Atari_8-bit_computers','Atari\'s 6502 home computers with custom graphics and sound chips.',
   [('Atari 400 / 800','Atari','1979',''),('Atari 1200XL','Atari','1983',''),('Atari 600XL / 800XL','Atari','1983',''),('Atari 65XE / 130XE','Atari','1985',''),('Atari XEGS','Atari','1987','console-style')]),
 X('Sinclair ZX80 / ZX81','Sinclair Research','1980','ZX_Spectrum','Tiny, cheap Sinclair predecessors of the ZX Spectrum.',
   [('ZX80','Sinclair Research','1980',''),('ZX81','Sinclair Research','1981','')]),
 X('Commodore VIC-20','Commodore','1980','VIC-20','Commodore\'s low-cost colour home computer, the first computer to sell a million units.',
   [('VIC-1001','Commodore','1980','Japan'),('VIC-20','Commodore','1981','worldwide; VC-20 in Germany')]),
 X('BBC Micro','Acorn Computers','1981','BBC_Micro','Acorn\'s computer for the BBC Computer Literacy Project, standard in British schools.',
   [('Model A','Acorn Computers','1981',''),('Model B','Acorn Computers','1981',''),('B+ / B+128','Acorn Computers','1985',''),('Master 128','Acorn Computers','1986',''),('Master Compact','Acorn Computers','','')]),
 X('ZX Spectrum','Sinclair Research','1982','ZX_Spectrum','Sinclair\'s rubber-keyed colour home computer, designed by Richard Altwasser and Rick Dickinson.',
   [('ZX Spectrum 16K / 48K','Sinclair Research','1982','rubber keys'),('ZX Spectrum+','Sinclair Research','1984',''),('ZX Spectrum 128','Sinclair Research','1985','Spain 1985, UK 1986'),('ZX Spectrum +2','Amstrad','1986','built-in cassette'),('ZX Spectrum +3','Amstrad','1987','built-in 3-inch disc drive'),('ZX Spectrum +2A / +2B / +3B','Amstrad','1988–1989','')]),
 X('Commodore 64','Commodore','1982','Commodore_64','Best-selling single computer model of all time, with SID sound and sprite graphics.',
   [('C64 "breadbin"','Commodore','1982','original brown case'),('SX-64','Commodore','1983','portable with built-in screen and 1541 drive'),('Commodore 128','Commodore','1985','C64-compatible successor'),('C64C','Commodore','1986','flat C128-style case'),('C64 Games System','Commodore','1990','console version')]),
 X('Acorn Electron','Acorn Computers','1983','BBC_Micro','Cheaper, simplified home version of the BBC Micro.',[('Acorn Electron','Acorn Computers','1983','')]),
 X('MSX','','1983','MSX','Japanese standard home-computer platform from Microsoft and ASCII, built by many makers.',
   [('MSX','','1983','Sony, Panasonic, Philips, Yamaha, Sharp, Canon, Toshiba, Spectravideo, Daewoo'),('MSX2','','1985',''),('MSX2+','','1988','Japan only'),('MSX turbo R','','1990','Japan only')]),
 X('Amstrad CPC','Amstrad','1984','Amstrad_CPC','Amstrad\'s Z80 home computer sold with its own monitor and a cassette or disc drive built in.',
   [('CPC 464','Amstrad','1984','built-in cassette'),('CPC 664','Amstrad','1985','3-inch disc'),('CPC 6128','Amstrad','1985','128 KB, 3-inch disc'),('464 Plus / 6128 Plus','Amstrad','1990',''),('GX4000','Amstrad','1990','console')]),
 X('Atari ST','Atari','1985','Atari_ST','Atari\'s 68000 GEM computer with built-in MIDI ports, favoured by musicians.',
   [('520ST','Atari','1985',''),('1040ST','Atari','1986','1040STF / STFM'),('520STE / 1040STE','Atari','1989',''),('Falcon030','Atari','1992','')]),
 X('Commodore Amiga (keyboard models)','Commodore','1987','Amiga','Commodore\'s multimedia 68000 computer in its wedge keyboard form.',
   [('Amiga 500','Commodore','1987',''),('Amiga 500+','Commodore','1991',''),('Amiga 600','Commodore','1992',''),('Amiga 1200','Commodore','1992','AGA chipset')]),
]
m_home=[["Commodore 16",C],["Commodore 116",C],["Commodore Plus/4",C]]
desk=[
 X('MITS Altair 8800','MITS','1975','Microcomputer','Front-panel kit microcomputer with lights and switches, the start of the hobby computer boom.',[('Altair 8800','MITS','1975','kit')]),
 X('Commodore PET','Commodore','1977','Commodore_PET','All-in-one metal-cased computer with built-in screen, designed under Chuck Peddle.',
   [('PET 2001','Commodore','1977','chiclet keyboard, built-in cassette'),('PET 2001-N','Commodore','1979',''),('PET 4000 series','Commodore','1980',''),('PET 8000 series','Commodore','','80-column'),('SuperPET SP9000','Commodore','1981','')]),
 X('Apple II','Apple','1977','Apple_II','Wozniak\'s colour computer with expansion slots, Apple\'s first mass-market success.',
   [('Apple II','Apple','1977',''),('Apple II Plus','Apple','1979',''),('Apple IIe','Apple','1983','sold until 1993'),('Apple IIc','Apple','1984','compact'),('Apple IIGS','Apple','1986','16-bit, colour graphics and sound'),('Apple IIc Plus','Apple','1988','')]),
 X('NEC PC-8800','NEC Corporation','1981','PC-8800_series','NEC\'s Japanese 8-bit personal computer series, a major games platform.',
   [('PC-8801','NEC Corporation','1981',''),('PC-8801mkII','NEC Corporation','1983',''),('PC-8801mkII SR','NEC Corporation','1985','improved graphics and sound'),('PC-8801 FA / MA','NEC Corporation','1987','FM sound')]),
 X('IBM Personal Computer','IBM','1981','IBM_Personal_Computer','IBM\'s 5150 and its successors, the origin of the PC-compatible standard.',
   [('IBM PC 5150','IBM','1981',''),('IBM PC XT 5160','IBM','1983','hard disk'),('IBM PCjr 4860','IBM','1983','home model'),('IBM Portable 5155','IBM','1984','luggable'),('IBM PC AT 5170','IBM','1984','80286')]),
 X('NEC PC-9800','NEC Corporation','1982','PC-9800_series','NEC\'s dominant Japanese PC line with native Japanese text, sold until 2003.',[('PC-9801','NEC Corporation','1982','')]),
 X('Compact Macintosh','Apple','1984','Compact_Macintosh','Apple\'s all-in-one Mac with built-in 9-inch screen, the first mass-market GUI computer.',
   [('Macintosh 128K','Apple','1984',''),('Macintosh 512K','Apple','',''),('Macintosh Plus','Apple','',''),('Macintosh SE','Apple','',''),('Macintosh SE/30','Apple','',''),('Macintosh Classic','Apple','',''),('Macintosh Classic II','Apple','',''),('Color Classic','Apple','','line ended 1995')]),
 X('Amiga big-box','Commodore','1985','Amiga','Separate-case Amiga models with expansion slots.',
   [('Amiga 1000','Commodore','1985','first Amiga'),('Amiga 2000','Commodore','1987','Zorro slots'),('Amiga 1500 / 2500','Commodore','',''),('Amiga 3000','Commodore','1990',''),('Amiga 4000','Commodore','1992','AGA')]),
 X('Amstrad PCW','Amstrad','1985','Amstrad_PCW','Low-cost word-processing computer sold with monitor and printer.',
   [('PCW 8256 / 8512','Amstrad','1985',''),('PCW 9512','Amstrad','1987',''),('PCW 9256','Amstrad','1991',''),('PcW16','Amstrad','1995','')]),
 X('Atari Mega ST and TT','Atari','1986','Atari_ST','Separate-keyboard professional models of the Atari ST family.',
   [('Mega ST','Atari','1986','Mega 1, ST2, ST4'),('TT030','Atari','1990','68030 workstation'),('Mega STE','Atari','1991','')]),
 X('Acorn Archimedes','Acorn Computers','1987','Acorn_Archimedes','First commercially available RISC microcomputer, built on Acorn\'s ARM.',
   [('A305 / A310 / A440','Acorn Computers','1987','ARM2'),('A3000','Acorn Computers','1989','keyboard case, for schools'),('A5000','Acorn Computers','1991','ARM3, RISC OS 3'),('A3010 / A3020 / A4000','Acorn Computers','1992','ARM250')]),
 X('NeXTcube','NeXT','1990','NeXTcube','NeXT\'s magnesium cube workstation, on which the World Wide Web was created at CERN.',
   [('NeXT Computer','NeXT','','original cube'),('NeXTcube','NeXT','1990',''),('NeXTcube Turbo','NeXT','','33 MHz')]),
]
lug=[
 X('Osborne 1','Osborne Computer Corporation','1981','Osborne_1','First commercially successful portable computer, designed by Lee Felsenstein.',
   [('Osborne 1','Osborne Computer Corporation','1981','5-inch screen, 52 columns'),('Osborne Executive','Osborne Computer Corporation','','80-column successor')]),
 X('Kaypro','Kaypro','1982','Kaypro','Metal-cased CP/M luggables.',
   [('Kaypro II','Kaypro','1982',''),('Kaypro 10','Kaypro','1983','10 MB hard disk'),('Kaypro 4','Kaypro','1984','double-sided drives')]),
 X('Compaq Portable','Compaq','1982','Compaq_Portable','Luggable that was one of the first IBM PC compatibles, and Compaq\'s first product.',
   [('Compaq Portable','Compaq','1982','announced 1982, shipped 1983'),('Portable Plus','Compaq','','hard disk'),('Portable 286','Compaq','1985',''),('Portable II','Compaq','1985','smaller, lighter'),('Portable III','Compaq','',''),('Portable 386','Compaq','','')]),
 X('TRS-80 Model 100','Tandy Corporation','1983','TRS-80_Model_100','Battery notebook with built-in software, designed by Kyocera, loved by journalists.',
   [('Kyotronic 85','Kyocera','1983','Japan'),('TRS-80 Model 100','Tandy Corporation','1983',''),('NEC PC-8201','NEC Corporation','','sibling'),('Olivetti M10','Olivetti','','sibling'),('Tandy 200','Tandy Corporation','1984',''),('Tandy 102','Tandy Corporation','1986','slimmer')]),
]
pocket=[
 X('Sharp PC-1211','Sharp Corporation','1980','Sharp_PC-1211','The first pocket computer, programmable in BASIC.',
   [('PC-1211','Sharp Corporation','1980',''),('TRS-80 Pocket Computer PC-1','Tandy Corporation','1980','rebadged')]),
 X('Sharp PC-1500','Sharp Corporation','1981','Sharp_PC-1500','Larger BASIC pocket computer with a graphic LCD and plotter accessory.',
   [('PC-1500','Sharp Corporation','1981',''),('TRS-80 PC-2','Tandy Corporation','','rebadged')],dt='CE-150 four-colour printer/plotter'),
]
m_pocket=[["PC-1401","Sharp Corporation"],["PC-E500S","Sharp Corporation"],["PC-G850","Sharp Corporation"]]
trainer=[
 X('Apple I','Apple','1976','Apple_I','Wozniak\'s hand-built single-board computer, Apple\'s first product; about 200 made.',[('Apple I','Apple','1976','board only; owners added case, keyboard, power')]),
 X('KIM-1','MOS Technology','1976','KIM-1','6502 single-board computer with hex keypad and LED display, popular with hobbyists.',[('KIM-1','MOS Technology','1976','')]),
 X('Heathkit ET-3400','Heathkit','1976','https://www.computinghistory.org.uk/det/44383/Heathkit-ET-3400-Trainer','Motorola 6800 microcomputer learning system sold as a kit or assembled.',
   [('ET-3400','Heathkit','1976','6800'),('ET-3400 (6808)','Heathkit','1981',''),('ET-3400 (6802)','Heathkit','1987','')]),
 X('Micro-Professor MPF-I','Multitech','1981','Micro-Professor_MPF-I','Z80 trainer board in a book-style case for learning machine code.',
   [('MPF-I','Multitech','1981',''),('MPF-IP','Multitech','1984',''),('MPF-I/88','Multitech','1985','')]),
]
recre=[
 X('THEC64','Retro Games Ltd.','2018','https://www.c64-wiki.com/wiki/Retro_Games_Ltd.','Licensed emulation-based re-creations of Commodore machines from Retro Games Ltd.',
   [('THEC64 Mini','Retro Games Ltd.','2018','half size'),('THEC64','Retro Games Ltd.','2019','full size, working keyboard'),('THEVIC20','Retro Games Ltd.','2020','')]),
 X('ZX Spectrum Next','SpecNext','2017','ZX_Spectrum_Next','FPGA-based enhanced ZX Spectrum, funded through Kickstarter.',
   [('Next (board)','SpecNext','2017',''),('Next Accelerated','SpecNext','2020','cased'),('Next Magenta Accelerated','SpecNext','2025','third Kickstarter')]),
 X('MEGA65','Museum of Electronic Games & Art','2021','https://c64-wiki.com/wiki/mega65','Open-source FPGA completion of the unreleased Commodore 65, with C64 mode.',[('MEGA65','Museum of Electronic Games & Art','2021','Artix-7 FPGA, built-in floppy drive')]),
]
m_recre=[["THEA1200","Retro Games Ltd."],["THE800XL","Retro Games Ltd."],["The Spectrum","Retro Games Ltd."]]
floppy=[
 X('Apple Disk II','Apple','1978','Disk_II','Wozniak\'s low-cost 5.25-inch drive for the Apple II.',[('Disk II','Apple','1978',''),('Disk IIc','Apple','',''),('DuoDisk','Apple','',''),('Apple 5.25 Drive','Apple','','')]),
 X('Commodore 1541','Commodore','1982','Commodore_1541','5.25-inch serial drive for the Commodore 64, 170 KB per disk.',
   [('VIC-1541','Commodore','1982','off-white'),('1541','Commodore','1983','beige'),('1541C','Commodore','1986','quieter'),('1541-II','Commodore','1988','external power supply'),('1571','Commodore','','double-sided, C128'),('1581','Commodore','','3.5-inch, 800 KB')]),
 X('Gotek with FlashFloppy','','','https://github.com/linvjw/flashfloppy','Low-cost USB-stick floppy emulator board fitted in place of a drive, usually flashed with free FlashFloppy firmware.',[('Gotek (FlashFloppy)','','','disk images on a USB stick')]),
]
def ok(lst,kind):
    allm={tuple(m) for m in old[kind]['m']} if kind in old else set()
    return lst
kinds=[
 {'n':'Home computer (keyboard computer)','a':'keyboard computer · 8-bit micro','d':'Computer built into its keyboard case, the typical home computer of the late 1970s and 1980s.','s':old['Keyboard computer']['s'],'x':home,'m':m_home},
 {'n':'Vintage desktop computer','a':'vintage micro · early PC','d':'Historic microcomputer or PC with a separate system unit or built-in screen rather than a keyboard case.','t':['all-in-one with built-in screen','separate system unit','kit'],'s':W+'Microcomputer','x':desk},
 {'n':'Luggable & vintage portable','a':'luggable · transportable','d':'Early portable computer, from suitcase-sized luggables to battery notebooks of the 1980s.','t':['luggable (mains)','battery notebook'],'s':W+'Portable_computer','x':lug},
 {'n':'Pocket computer','a':'','d':'Programmable pocket-sized computer of a historic type.','s':old['Pocket computer']['s'],'x':pocket,'m':m_pocket},
 {'n':'Trainer & single-board kit (vintage)','a':'trainer kit · single-board computer','d':'Historic bare-board computer or kit sold to teach or explore computing.','s':old['Trainer kit']['s'],'x':trainer},
 {'n':'Retro computer re-creation','a':'replica · FPGA re-creation','d':'Modern licensed or FPGA-based re-creation of a classic computer.','t':['emulation-based','FPGA-based','mini','full-size'],'s':'https://www.c64-wiki.com/wiki/Retro_Games_Ltd.','x':recre,'m':m_recre},
 {'n':'Floppy disk drive','a':'','d':'Drive that reads or writes floppy disks, internal or in its own case, or a solid-state floppy emulator.','t':['8-inch','5.25-inch','3.5-inch','3-inch','USB floppy drive','floppy emulator'],'s':old['Floppy disk drive']['s'],'x':floppy},
]
K='knowledge'
brands=[
 dict(n='Apple',c='United States',f='1976',seg='Premium',kf='Mac computers',d='Californian maker of the Apple I and II, the Macintosh, iPhone and iPad.',lines=['Apple II','Macintosh'],sig=['Apple I','Apple II','Compact Macintosh'],s=K),
 dict(n='Commodore',c='Canada',f='1954',seg='Mainstream',kf='8-bit home computers',d='Maker of the PET, VIC-20, Commodore 64 and Amiga; bankrupt in 1994.',lines=['PET','VIC-20','C64','Amiga'],sig=['Commodore 64','Commodore Amiga (keyboard models)','Commodore PET'],s=K),
 dict(n='Sinclair Research',c='United Kingdom',f='',seg='Value',kf='low-cost home computers',d='Clive Sinclair\'s company behind the ZX80, ZX81 and ZX Spectrum; computer business sold to Amstrad in 1986.',lines=['ZX80','ZX81','ZX Spectrum'],sig=['ZX Spectrum'],rel=['Amstrad'],s=W+'ZX_Spectrum'),
 dict(n='Acorn Computers',c='United Kingdom',f='1978',seg='Mainstream',kf='BBC Micro and ARM',d='Cambridge maker of the BBC Micro and Archimedes, origin of the ARM processor.',lines=['BBC Micro','Electron','Archimedes'],sig=['BBC Micro','Acorn Archimedes'],s=K),
 dict(n='Atari',c='United States',f='1972',seg='Mainstream',kf='games and home computers',d='American games company whose 8-bit and ST computers were sold by Atari, Inc. and later Atari Corporation.',lines=['400/800','XL/XE','ST','TT','Falcon'],sig=['Atari 8-bit computers','Atari ST'],s=K),
 dict(n='Amstrad',c='United Kingdom',f='1968',seg='Value',kf='affordable home computers',d='Alan Sugar\'s British electronics company, maker of the CPC and PCW and later Spectrum models.',lines=['CPC','PCW','ZX Spectrum +2/+3'],sig=['Amstrad CPC','Amstrad PCW'],rel=['Sinclair Research'],s=K),
 dict(n='Tandy Corporation',c='United States',f='1919',seg='Own-label & retailer',kf='Radio Shack computers',d='Owner of the Radio Shack chain, which sold the TRS-80 computers.',lines=['TRS-80','Tandy 1000'],sig=['TRS-80','TRS-80 Model 100'],s=K),
 dict(n='IBM',c='United States',f='1911',seg='Professional & flagship',kf='business computing',d='American computing company that created the IBM PC.',lines=['PC','XT','AT','PS/2'],sig=['IBM Personal Computer'],s=K),
 dict(n='NEC Corporation',c='Japan',f='1899',seg='Mainstream',kf='Japanese PCs',d='Japanese electronics group whose PC-8800 and PC-9800 lines led the Japanese PC market.',lines=['PC-8800','PC-9800'],sig=['NEC PC-9800','NEC PC-8800'],s=K),
 dict(n='NeXT',c='United States',f='1985',seg='Premium',kf='workstations',d='Steve Jobs\'s workstation company, bought by Apple in 1997.',lines=['NeXT Computer','NeXTcube','NeXTstation'],sig=['NeXTcube'],rel=['Apple'],s=K),
 dict(n='Compaq',c='United States',f='1982',seg='Mainstream',kf='IBM-compatible PCs',d='American PC maker whose first product was the Compaq Portable; bought by HP in 2002.',lines=['Portable','Deskpro','LTE'],sig=['Compaq Portable'],s=K),
 dict(n='Osborne Computer Corporation',c='United States',f='',seg='Specialist',kf='portable computers',d='Maker of the Osborne 1, the first commercially successful portable computer.',lines=['Osborne 1','Executive'],sig=['Osborne 1'],s=W+'Osborne_1'),
 dict(n='Kaypro',c='United States',f='1982',seg='Specialist',kf='CP/M luggables',d='Solana Beach maker of metal-cased CP/M portables, spun out of Non-Linear Systems.',lines=['Kaypro II','Kaypro 4','Kaypro 10'],sig=['Kaypro'],s=W+'Kaypro'),
 dict(n='Sharp Corporation',c='Japan',f='1912',seg='Mainstream',kf='pocket computers',d='Japanese electronics maker of the first pocket computer.',lines=['PC-1211','PC-1500','PC-G850'],sig=['Sharp PC-1211','Sharp PC-1500'],s=K),
 dict(n='MOS Technology',c='United States',f='1969',seg='Specialist',kf='6502 chips',d='Chipmaker of the 6502 and the KIM-1 board, bought by Commodore in 1976.',lines=['KIM-1'],sig=['KIM-1'],rel=['Commodore'],s=K),
 dict(n='Heathkit',c='United States',f='1926',seg='Specialist',kf='electronics kits',d='American maker of electronics kits, including microcomputer trainers.',lines=['ET-3400'],sig=['Heathkit ET-3400'],s=K),
 dict(n='Multitech',c='Taiwan',f='1976',seg='Specialist',kf='trainer boards',d='Taiwanese maker of the Micro-Professor trainers, later renamed Acer.',lines=['Micro-Professor'],sig=['Micro-Professor MPF-I'],s=W+'Micro-Professor_MPF-I'),
 dict(n='Retro Games Ltd.',c='United Kingdom',f='2015',seg='Specialist',kf='licensed retro re-creations',d='Luton company making THEC64 and other licensed re-creations of classic computers.',lines=['THEC64','THEVIC20','THEA1200'],sig=['THEC64'],s='https://www.c64-wiki.com/wiki/Retro_Games_Ltd.'),
 dict(n='SpecNext',c='United Kingdom',f='',seg='Artisan & independent',kf='FPGA Spectrum',d='Developer of the ZX Spectrum Next.',lines=['ZX Spectrum Next'],sig=['ZX Spectrum Next'],s=W+'ZX_Spectrum_Next'),
 dict(n='Museum of Electronic Games & Art',c='Germany',f='',seg='Artisan & independent',kf='MEGA65',d='Non-profit association (MEGA e.V.) whose members develop the MEGA65.',lines=['MEGA65'],sig=['MEGA65'],s='https://c64-wiki.com/wiki/mega65'),
 dict(n='MITS',c='United States',f='',seg='Specialist',kf='Altair 8800',d='Maker of the Altair 8800 microcomputer kit.',lines=['Altair 8800'],sig=['MITS Altair 8800'],s=W+'Microcomputer'),
]
out={'kinds':kinds,'brands':brands,'traditions':[],'notes':'Collector view: 40 archetypes, each from a retrieved page (mostly Wikipedia; c64-wiki for Retro Games Ltd and MEGA65; Computing History for the ET-3400; FlashFloppy repository for Gotek), with generations as versions. Old keyboard-computer models became versions (Atari ST, Amiga, C64, VIC-20); C16, C116 and Plus/4 stay in m (no page retrieved). Amiga 1000/1500/2000/2500/3000/4000 and Atari Mega ST/Mega STE/TT030 taken over from the old low-profile desktop list (shelf 00_01) into Vintage desktop computer. Amiga and Atari ST are split into keyboard and separate-case archetypes because the kinds split on form. Apple I placed with trainers and single-board kits (it was sold as a bare board). Maker "Atari Corporation" normalised to "Atari" (the 8-bit machines came from Atari, Inc.). Compact Macintosh versions have no years except the 128K (the page gave years only in an image); NeXTstation, Gotek hardware makers and TRS-80 PC-2 year were not on retrieved pages so are left out. THEA500 Mini and later Retro Games models not on the retrieved page; old-data THEA1200, THE800XL and The Spectrum kept in m.'}
p='work/D1/shelves/00_02.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
