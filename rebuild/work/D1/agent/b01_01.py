import json, os
W = 'https://en.wikipedia.org/wiki/'
def X(n, mk, y, s, d, v=(), a='', dt=''):
    x = {'n': n, 'a': a, 'd': d, 'mk': mk, 'y': y, 's': s if s.startswith('http') else W + s,
         'v': [dict(zip(('n', 'mk', 'y', 'd'), t)) for t in v]}
    if dt: x['dt'] = dt
    return x
N, A = 'Nvidia', 'AMD'
gpu_x = [
 X('3dfx Voodoo', '3dfx', '1996', '3dfx_Interactive', 'The first consumer 3D accelerator card, whose Glide API defined late-1990s PC gaming; now a collector icon.',
   [('Voodoo Graphics', '3dfx', '1996', '3D-only, needs a separate 2D card'), ('Voodoo2', '3dfx', '1998', 'second texture unit; two boards linked by SLI'),
    ('Voodoo Banshee', '3dfx', '1998', 'single-chip 2D/3D'), ('Voodoo3', '3dfx', '1999', 'strong sales'), ('Voodoo4 4500 / Voodoo5 5500', '3dfx', '2000', 'last cards before Nvidia bought the assets')]),
 X('Nvidia GeForce', N, '1999', 'GeForce', 'Nvidia\'s consumer graphics line, from the "first GPU" to today\'s RTX ray-tracing cards.', a='GeForce GTX · GeForce RTX',
   v=[('GeForce 256', N, '1999', 'marketed as the first GPU'), ('GeForce 2 / 3 / 4', N, '2000–2002', 'GeForce 3 added programmable shaders'),
      ('GeForce FX', N, '2003', ''), ('GeForce 6 / 7', N, '2004–2005', 'SLI; 7 series last with AGP; 7900 GTX'),
      ('GeForce 8', N, '2006', '8800 GTX: first Direct3D 10 card, unified shaders; 8800 GT'), ('GeForce 200', N, '2008', 'GTX 260, GTX 280'),
      ('GeForce 400 / 500 (Fermi)', N, '2010', 'GTX 480, GTX 580'), ('GeForce 600 / 700 (Kepler)', N, '2012–2013', 'GTX 680, GTX 780, GTX Titan'),
      ('GeForce 900 (Maxwell)', N, '2014', ''), ('GeForce 10 (Pascal)', N, '2016', 'GTX 1080, GTX 1080 Ti'), ('GeForce 16', N, '2019', 'Turing without RT cores, budget'),
      ('GeForce RTX 20 (Turing)', N, '2018', 'first real-time ray tracing and DLSS; RTX 2080 Ti'), ('GeForce RTX 30 (Ampere)', N, '2020', 'RTX 3090, 3090 Ti'),
      ('GeForce RTX 40 (Ada Lovelace)', N, '2022', 'RTX 4090'), ('GeForce RTX 50 (Blackwell)', N, '2025', 'RTX 5090, 5080, 5070 Ti, 5070'),
      ('Titan', N, '2013', 'GTX Titan, Titan X, Titan Black, Titan Z, Titan RTX')],
   dt='tier xx50 · xx60 · xx70 · xx80 · xx90 · suffix Ti, Super · Founders Edition or partner board'),
 X('AMD Radeon', A, '2000', 'Radeon', 'ATI\'s, then AMD\'s, consumer graphics line, the main rival to GeForce.', a='ATI Radeon · Radeon RX',
   v=[('Radeon 7000–9000', 'ATI', '2000–2002', 'original ATI Radeon line'), ('Radeon X series', 'ATI', '2004–2005', 'X300 to X1000'),
      ('Radeon HD', 'ATI', '2007–2013', 'HD 2000 to HD 8000; AMD bought ATI in 2006'), ('Radeon R7 / R9 200 / 300', A, '2013–2015', 'GCN'),
      ('Radeon RX 400 / 500 (Polaris)', A, '2016–2017', ''), ('Radeon RX Vega', A, '2017', ''), ('Radeon RX 5000 (RDNA)', A, '2019', 'e.g. RX 5700 XT'),
      ('Radeon RX 6000 (RDNA 2)', A, '2020', ''), ('Radeon RX 7000 (RDNA 3)', A, '2022', ''), ('Radeon RX 9000 (RDNA 4)', A, '2025', '')]),
 X('Intel Arc', 'Intel', '2022', 'Intel_Arc', 'Intel\'s discrete graphics cards, its first serious entry into gaming GPUs.',
   [('Alchemist (A-series)', 'Intel', '2022', 'Arc A770, A750'), ('Battlemage (B-series)', 'Intel', '2024', 'Arc B580 (Dec 2024), B570 (Jan 2025)')]),
]
gpu_m = [['ROG Astral GeForce RTX 5090', 'ASUS'], ['ROG Strix GeForce RTX 5070 Ti', 'ASUS'], ['TUF Gaming GeForce RTX 5080', 'ASUS'], ['Prime GeForce RTX 5070', 'ASUS'],
         ['ROG Matrix GeForce RTX 4090 Platinum', 'ASUS'], ['Radeon RX 5700 XT Challenger', 'ASRock']]
snd_x = [
 X('Sound Blaster', 'Creative', '1989', 'Sound_Blaster', 'Creative\'s sound-card line that became the de facto PC audio standard.',
   [('Sound Blaster 1.0', 'Creative', '1989', 'CT1320'), ('Sound Blaster Pro', 'Creative', '1991', ''), ('Sound Blaster 16', 'Creative', '1992', ''),
    ('Sound Blaster AWE32', 'Creative', '1994', 'wavetable'), ('Sound Blaster AWE64', 'Creative', '1996', ''), ('Sound Blaster Live!', 'Creative', '1998', ''),
    ('Sound Blaster Audigy', 'Creative', '2001', ''), ('Sound Blaster X-Fi', 'Creative', '2005', ''), ('Sound Blaster Z-Series', 'Creative', '2012', ''),
    ('Sound BlasterX AE-5', 'Creative', '2017', ''), ('Sound Blaster AE-7 / AE-9', 'Creative', '2019', '')]),
 X('Roland MT-32', 'Roland', '1987', 'Roland_MT-32', 'MIDI sound module that set the music standard for late-1980s PC games, sought by retro collectors.',
   [('MT-32', 'Roland', '1987', 'external module; early units need a SysEx delay'), ('LAPC-I', 'Roland', '1989', 'ISA card with MPU-401 interface'),
    ('CM-32L', 'Roland', '1989', 'no display; adds 33 sound effects used by many games')]),
]
cap_x = [
 X('Elgato Game Capture', 'Elgato', '2012', 'Elgato', 'Elgato\'s capture devices for recording and streaming console and PC gameplay.',
   [('Game Capture HD', 'Elgato', '2012', ''), ('Game Capture HD60', 'Elgato', '2014', ''), ('Game Capture HD60 X', 'Elgato', '', 'external USB'),
    ('Game Capture 4K Pro', 'Elgato', '', 'internal PCIe card'), ('Game Capture 4K X', 'Elgato', '2024', 'external'), ('Game Capture 4K S', 'Elgato', '', 'external'),
    ('Cam Link 4K', 'Elgato', '', 'turns a camera into a webcam')]),
]
kinds = [
 {'n': 'Graphics card', 'a': 'video card · GPU · グラフィックボード · ビデオカード',
  'd': 'Expansion card with a graphics processor that drives displays and renders games.',
  't': ['reference / Founders Edition', 'partner board (custom cooler)', 'low-profile', 'water-blocked', 'blower'],
  's': 'https://shop.tsukumo.co.jp/dir/20', 'x': gpu_x, 'm': gpu_m,
  'r': [['GeForce RTX', N], ['GeForce GTX', N], ['GeForce GT', N], ['Titan', N], ['Radeon RX', A], ['Arc', 'Intel'],
        ['ROG Astral', 'ASUS'], ['ROG Strix', 'ASUS'], ['ROG Matrix', 'ASUS'], ['TUF Gaming', 'ASUS'], ['Prime', 'ASUS'], ['Challenger', 'ASRock'],
        ['FTW', 'EVGA'], ['Kingpin', 'EVGA'], ['Classified', 'EVGA']]},
 {'n': 'External GPU enclosure', 'a': 'eGPU · eGPU box', 'd': 'Housing that holds a desktop graphics card outside the computer and connects it, usually by Thunderbolt.',
  's': 'https://www.razer.com/gaming-egpus/razer-core-x-v2', 'm': [['Core X', 'Razer'], ['Breakaway Box 750ex', 'Sonnet'], ['Breakaway Box 850', 'Sonnet']]},
 {'n': 'Sound card', 'a': 'audio card', 'd': 'Card or module that handles a computer\'s audio, from modern gaming cards to retro collector boards.',
  't': ['internal PCIe', 'USB', 'retro ISA', 'MIDI sound module'], 's': 'https://us.creative.com/aeseries/', 'x': snd_x, 'm': [['Sound Blaster AE-9', 'Creative']]},
 {'n': 'Video capture device', 'a': 'capture card · ビデオキャプチャー', 'd': 'Card or box that records or streams a video signal from a console, camera or second PC.',
  't': ['internal card', 'external USB', 'HDMI passthrough', '4K / high frame rate'], 's': 'https://www.elgato.com/us/en/p/game-capture-4k-pro', 'x': cap_x},
 {'n': 'Network card', 'a': 'network adapter card · NIC', 'd': 'Card fitted inside the computer that adds a wired or wireless network connection.',
  't': ['Ethernet (1, 2.5, 10 Gb)', 'Wi-Fi'], 's': 'https://www.intel.com/content/www/us/en/ark/products/series/189530/intel-ethernet-network-adapter-x710.html',
  'm': [['Ethernet Network Adapter X710', 'Intel']]},
 {'n': 'I/O expansion card', 'a': 'port card', 'd': 'Card fitted inside the computer that adds ports.',
  't': ['USB', 'Thunderbolt', 'SATA / M.2', 'serial / parallel'], 's': 'https://www.startech.com/en-us/cards-adapters/pexusb312a2c2v', 'm': [['GC-TITAN RIDGE', 'Gigabyte']]},
 {'n': 'TV tuner card', 'a': 'TV card', 'd': 'Card fitted inside the computer that receives broadcast television.',
  't': ['DVB-T/T2', 'DVB-S/S2', 'DVB-C', 'ATSC', 'multi-tuner'], 's': 'https://shop.tbsdtv.com/dvbt2-tv-tuner-pcie-c-12.html',
  'm': [['WinTV-quadHD', 'Hauppauge'], ['TBS6205', 'TBS'], ['TBS6209', 'TBS'], ['TBS6281SE', 'TBS'], ['TBS6522', 'TBS'], ['TBS6590', 'TBS']]},
]
K = 'knowledge'
def B(n, c, f, seg, kf, d, s=K, **kw):
    b = {'n': n, 'c': c, 'f': f, 'seg': seg, 'kf': kf, 'd': d, 's': s}; b.update(kw); return b
brands = [
 B('Nvidia', 'United States', '1993', 'Professional & flagship', 'GeForce GPUs', 'Graphics-chip maker behind GeForce and the RTX cards.', lines=['GeForce', 'Titan'], sig=['Nvidia GeForce']),
 B('3dfx', 'United States', '1994', 'Specialist', 'Voodoo cards', 'Pioneer of consumer 3D accelerators; assets sold to Nvidia in 2000.', W + '3dfx_Interactive', sig=['3dfx Voodoo']),
 B('ATI', 'Canada', '1985', 'Mainstream', 'Radeon', 'Canadian graphics maker that created Radeon; bought by AMD in 2006.', rel=['AMD']),
 B('EVGA', 'United States', '1999', 'Premium', 'GeForce cards', 'Nvidia board partner known for FTW, Classified and Kingpin cards; left graphics cards in 2022.', W + 'EVGA_Corporation', lines=['FTW', 'Classified', 'Kingpin']),
 B('Sapphire', 'Hong Kong', '2001', 'Mainstream', 'Radeon cards', 'Largest maker of AMD Radeon-based graphics cards.', W + 'Sapphire_Technology'),
 B('Creative', 'Singapore', '1981', 'Mainstream', 'Sound Blaster', 'Singaporean audio company behind the Sound Blaster cards.', lines=['Sound Blaster'], sig=['Sound Blaster']),
 B('Roland', 'Japan', '1972', 'Professional & flagship', 'synthesizers', 'Japanese electronic-instrument maker of the MT-32 sound module.', sig=['Roland MT-32']),
 B('Elgato', 'Germany', '2010', 'Specialist', 'capture & streaming', 'Streaming-gear brand owned by Corsair since 2018.', W + 'Elgato', rel=['Corsair']),
 B('Razer', 'United States', '2005', 'Premium', 'gaming peripherals', 'Gaming hardware brand that popularised the eGPU box with the Core.'),
 B('Hauppauge', 'United States', '1994', 'Specialist', 'TV tuners', 'Long-established maker of PC TV-tuner cards.'),
]
out = {'kinds': kinds, 'brands': brands, 'traditions': [],
       'notes': 'Graphics card: 382 SKUs cut; workstation/datacentre lines (Quadro, RTX professional, FirePro, Radeon Pro, Radeon AI Pro) dropped as trade equipment (all 78 old AMD models were of this kind). Four consumer archetypes (3dfx Voodoo, GeForce, Radeon, Arc) with generations and key cards; board-partner lines kept as ranges and 6 ASUS/ASRock models. Sapphire Nitro+/Pulse not attested by the fetched page, so not listed. Video capture: internal and external merged. Brand facts for Nvidia, ATI, Creative, Roland, Razer, Hauppauge from knowledge.'}
p = '/home/user/Possession-Taxonomy/rebuild/work/D1/shelves/01_01.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('written')
