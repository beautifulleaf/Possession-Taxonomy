import json, os
W = 'https://en.wikipedia.org/wiki/'
def X(n, mk, y, s, d, v=(), a='', dt=''):
    x = {'n': n, 'a': a, 'd': d, 'mk': mk, 'y': y, 's': s if s.startswith('http') else W + s,
         'v': [dict(zip(('n', 'mk', 'y', 'd'), t)) for t in v]}
    if dt: x['dt'] = dt
    return x

cpu_x = [
 X('Intel 4004', 'Intel', '1971', 'Intel_4004', 'The first commercial single-chip microprocessor, a 4-bit CPU and the start of Intel\'s CPU line.',
   [('4004', 'Intel', '1971', '740–750 kHz, 2,300 transistors'), ('4040', 'Intel', '1974', 'successor')]),
 X('Intel 8086', 'Intel', '1978', 'Intel_8086', '16-bit chip that founded the x86 instruction set used by PCs ever since.',
   [('8086', 'Intel', '1978', '5 MHz; later 8086-1/-2/-4 speed grades'), ('8088', 'Intel', '1979', '8-bit external bus; used in the IBM PC at 4.77 MHz')]),
 X('Intel 80386', 'Intel', '1985', 'I386', 'First 32-bit x86 processor, implementing the full IA-32 architecture.', a='386 · i386',
   v=[('386DX', 'Intel', '1985', 'original; 33 MHz version 1989'), ('386SX', 'Intel', '1988', '16-bit data bus for lower-cost PCs'), ('386SL', 'Intel', '', 'low-power laptop version, 20 and 25 MHz')]),
 X('Pentium', 'Intel', '1993', 'Pentium', 'Intel\'s fifth-generation x86 brand, later its mid-range and entry line until 2023.',
   [('Pentium (P5)', 'Intel', '1993', ''), ('Pentium Pro', 'Intel', '1995', 'P6, out-of-order execution'), ('Pentium MMX', 'Intel', '1997', 'MMX instructions'),
    ('Pentium II', 'Intel', '1997', 'Klamath'), ('Pentium III', 'Intel', '1999', 'Katmai'), ('Pentium 4', 'Intel', '2000', 'NetBurst'),
    ('Pentium M', 'Intel', '2003', 'efficient mobile chip'), ('Pentium D', 'Intel', '2005', 'first multi-core Pentium'),
    ('Pentium Dual-Core', 'Intel', '2006–2009', ''), ('Pentium Gold / Silver', 'Intel', '2017', 'entry desktop / low-power; brand dropped 2023')]),
 X('Athlon', 'AMD', '1999', 'Athlon', 'AMD\'s K7 desktop processor, the first desktop CPU to reach 1 GHz; later AMD\'s budget brand.',
   [('Athlon (Slot A, K7)', 'AMD', '1999', ''), ('Thunderbird', 'AMD', '2000', 'Socket A, on-die L2 cache'), ('Athlon XP', 'AMD', '2001', 'Palomino to Barton cores'),
    ('Athlon II', 'AMD', '2009', ''), ('Athlon X4', 'AMD', '2013–2017', 'FM2+, later AM4; e.g. Athlon X4 860K, 880K'),
    ('Athlon (Zen)', 'AMD', '2018', 'Athlon 200GE, then 3000G (2019)'), ('Athlon Gold / Silver', 'AMD', '2022', 'Mendocino mobile and Chromebook parts, e.g. 7220U, 7120U')]),
 X('Athlon 64', 'AMD', '2003', 'Athlon_64', 'First 64-bit x86 processor aimed at ordinary consumers (AMD64, K8 core).',
   [('Athlon 64', 'AMD', '2003', 'Socket 754 and 939'), ('Athlon 64 FX', 'AMD', '2003', 'enthusiast, unlocked; FX-51 first'), ('Athlon 64 X2', 'AMD', '2005', 'AMD\'s first dual-core desktop CPU; AM2 version 2006')]),
 X('Core 2', 'Intel', '2006', 'Intel_Core_2', 'Intel\'s Core-microarchitecture family that replaced Pentium at the top and united laptop and desktop chips.', a='Core 2 Duo',
   v=[('Core 2 Duo', 'Intel', '2006', 'Conroe, 65 W'), ('Core 2 Extreme', 'Intel', '2006', 'enthusiast'), ('Core 2 Quad', 'Intel', '2007', 'Kentsfield; Yorkfield 45 nm in 2008')]),
 X('Intel Core i3 / i5 / i7 / i9', 'Intel', '2008', 'Intel_Core', 'Intel\'s mainstream desktop and laptop line in good–better–best tiers, sold by generation from 2008 to 2024.', a='Core i7 · Core i9',
   v=[('1st gen (Nehalem)', 'Intel', '2008–2010', 'Bloomfield, Lynnfield, Clarkdale; Core i7-920, i7-980X'), ('2nd gen Sandy Bridge', 'Intel', '2011', 'Core i7-2600K'),
      ('3rd gen Ivy Bridge', 'Intel', '2012', 'Core i7-3770K'), ('4th gen Haswell', 'Intel', '2013', 'Core i7-4790K'), ('5th gen Broadwell', 'Intel', '2015', ''),
      ('6th gen Skylake', 'Intel', '2015', 'Core i7-6700K'), ('7th gen Kaby Lake', 'Intel', '2017', 'Core i7-7700K; Core i9 tier added 2017'),
      ('8th gen Coffee Lake', 'Intel', '2017–2018', 'Core i7-8700K'), ('9th gen Coffee Lake Refresh', 'Intel', '2018–2019', 'Core i9-9900K'),
      ('10th gen Comet Lake', 'Intel', '2020', 'Core i9-10900K'), ('11th gen Rocket Lake', 'Intel', '2021', 'Core i9-11900K'),
      ('12th gen Alder Lake', 'Intel', '2021–2022', 'Core i9-12900K'), ('13th gen Raptor Lake', 'Intel', '2022–2023', 'Core i9-13900K'),
      ('14th gen Raptor Lake Refresh', 'Intel', '', 'Core i9-14900K; last "i" generation')],
   dt='tier i3 · i5 · i7 · i9 · suffix K unlocked, F no graphics, T low-power, H/U/HX laptop'),
 X('Intel Core Ultra', 'Intel', '2023', 'Intel_Core', 'Intel\'s successor branding to Core i, sold as Core Ultra 5/7/9 in numbered series.',
   [('Series 1 Meteor Lake', 'Intel', '2023–2024', 'laptops'), ('Series 2 Arrow Lake / Lunar Lake', 'Intel', '', 'desktop Core Ultra 9 285K, Ultra 7 265K'), ('Series 3 Panther Lake', 'Intel', '', '')]),
 X('AMD Ryzen', 'AMD', '2017', 'Ryzen', 'AMD\'s Zen-based desktop and laptop line in Ryzen 3/5/7/9 tiers that revived its competition with Intel.', a='Ryzen 7 · Ryzen 9',
   v=[('Ryzen 1000 (Zen)', 'AMD', '2017', 'AM4; Ryzen 7 1800X'), ('Ryzen 2000 (Zen+)', 'AMD', '2018', 'Ryzen 7 2700X'), ('Ryzen 3000 (Zen 2)', 'AMD', '2019', 'Ryzen 9 3950X'),
      ('Ryzen 5000 (Zen 3)', 'AMD', '2020', 'Ryzen 9 5950X; Ryzen 7 5800X3D with 3D V-Cache'), ('Ryzen 7000 (Zen 4)', 'AMD', '2022', 'AM5; Ryzen 9 7950X, Ryzen 7 7800X3D'),
      ('Ryzen 8000G (Zen 4 APU)', 'AMD', '2024', 'Ryzen 7 8700G'), ('Ryzen 9000 (Zen 5)', 'AMD', '2024', 'Ryzen 9 9950X; Ryzen 7 9800X3D, second-generation 3D V-Cache'),
      ('Ryzen 9 9950X3D2 Dual Edition', 'AMD', '2026', 'first dual 3D V-Cache CPU')],
   dt='tier 3 · 5 · 7 · 9 · suffix X, X3D (stacked cache, gaming), G (graphics), U/H/HX laptop · socket AM4, AM5'),
 X('Ryzen Threadripper', 'AMD', '2017', 'Ryzen', 'AMD\'s high-core-count desktop line for workstations and enthusiasts.', a='Threadripper',
   v=[('Threadripper 1000 (Whitehaven)', 'AMD', '2017', 'TR4, 8–16 cores; 1950X'), ('Threadripper 2000 (Colfax)', 'AMD', '2018', 'up to 32 cores; 2990WX'),
      ('Threadripper 3000 (Castle Peak)', 'AMD', '2019', 'sTRX4, up to 64 cores; 3970X, 3990X'), ('Threadripper PRO 5000 (Chagall)', 'AMD', '', 'Zen 3, sWRX8'),
      ('Threadripper 7000 / PRO 7000 (Storm Peak)', 'AMD', '2023', 'sTR5, PRO up to 96 cores; 7980X, PRO 7995WX'), ('Threadripper 9000', 'AMD', '', '9980X')]),
 X('Intel Xeon', 'Intel', '1998', 'Xeon', 'Intel\'s server and workstation brand with ECC memory, more cores and PCIe lanes; mostly trade equipment, owned by home-lab builders.',
   [('Pentium II Xeon', 'Intel', '1998', 'Drake'), ('Xeon E3 / E5 / E7', 'Intel', '', ''), ('Xeon Scalable', 'Intel', '2017', 'Bronze, Silver, Gold, Platinum'),
    ('Xeon W', 'Intel', '2017', 'workstation; w3–w9 tiers from 2023'), ('Xeon 6', 'Intel', '2024', 'renaming announced April 2024')]),
 X('Apple M-series', 'Apple', '2020', 'Apple_silicon', 'Apple\'s system-on-chip for Macs and iPads; built into the device, not sold as a separate part.', a='Apple silicon',
   v=[('M1 / Pro / Max / Ultra', 'Apple', '2020–2022', ''), ('M2 family', 'Apple', '2022–2023', ''), ('M3 family', 'Apple', '2023', 'M3 Ultra 2025'),
      ('M4 family', 'Apple', '2024', ''), ('M5 family', 'Apple', '2025–2026', '')]),
]

mb_x = [
 X('ASUS ROG motherboards', 'ASUS', '', 'Asus_ROG', 'ASUS\'s Republic of Gamers enthusiast boards: Maximus for Intel, Crosshair for AMD, Strix below them.', a='Republic of Gamers',
   v=[('ROG Maximus', 'ASUS', '', 'Intel flagship; e.g. Maximus Z890 Hero, Apex, Extreme; Z790 Formula'),
      ('ROG Crosshair', 'ASUS', '', 'AMD flagship; e.g. Crosshair VIII Dark Hero, X670E Hero, X870E Hero, X870E Extreme'),
      ('ROG Strix', 'ASUS', '', 'gaming mainstream; e.g. Strix Z890-E, X870E-E, B850-F Gaming WiFi, X870-I (Mini-ITX)')],
   dt='chipset (Z/B/H Intel · X/B/A AMD) · ATX, micro-ATX, Mini-ITX · BTF rear-connector variants'),
 X('Gigabyte AORUS', 'Gigabyte', '', 'Gigabyte_Technology', 'Gigabyte\'s gaming sub-brand of motherboards, laddered Elite, Pro, Ultra, Master and Xtreme.',
   v=[('X570 AORUS Master / Xtreme', 'Gigabyte', '', 'AMD AM4'), ('Z590 Aorus Master / Extreme', 'Gigabyte', '', 'Intel'),
      ('Z690 Aorus Master / Extreme', 'Gigabyte', '', 'Intel; Extreme Waterforce with monoblock'), ('Z690I Aorus Ultra', 'Gigabyte', '', 'Mini-ITX')],
   dt='Elite · Pro · Ultra · Master · Xtreme'),
 X('ASRock Taichi', 'ASRock', '2016', 'https://www.funkykit.com/articles/the-asrock-taichi-journey-ten-years-of-innovation-and-stories/',
   'ASRock\'s flagship premium motherboard line, recognised by its cog-wheel styling.',
   [('X99 Taichi', 'ASRock', '2016', 'first Taichi'), ('X370 Taichi', 'ASRock', '2017', 'AMD AM4'), ('X399 Taichi', 'ASRock', '2017', 'Threadripper'),
    ('Z390 Taichi / Taichi Ultimate', 'ASRock', '2018', ''), ('X570 Taichi', 'ASRock', '2019', ''), ('TRX40 Taichi', 'ASRock', '2019', ''),
    ('X870E / Z890 Taichi Lite', 'ASRock', '', 'pared-down version')]),
 X('MSI MEG', 'MSI', '2018', 'https://techpowerup.com/review/msi-meg-z390-godlike', 'MSI\'s top enthusiast motherboard tier, above MPG, MAG and PRO.',
   [('MEG Z390 GODLIKE', 'MSI', '', 'flagship with RGB mirror, M.2 card and capture card')]),
]
mb_m = [['ProArt Z890-Creator WiFi', 'ASUS'], ['ProArt X870E-Creator WiFi', 'ASUS'], ['TUF Gaming Z890-Plus WiFi', 'ASUS'], ['TUF Gaming X870-Plus WiFi', 'ASUS'],
        ['TUF Gaming B850-Plus WiFi', 'ASUS'], ['Prime B860-Plus WiFi', 'ASUS'], ['Prime B850M-A WiFi', 'ASUS'], ['Prime H810M-A', 'ASUS'],
        ['B650 Aero G', 'Gigabyte'], ['Z690 Aero G DDR4', 'Gigabyte'], ['1ST-MITX-ALN10', '1ST-embedded']]

ram_x = [
 X('Corsair Vengeance', 'Corsair', '', 'Corsair_Gaming', 'Corsair\'s mainstream enthusiast memory line, with and without RGB lighting, for desktops and laptops.',
   [('VENGEANCE Pro', 'Corsair', '', ''), ('VENGEANCE RGB PRO / RGB PRO SL', 'Corsair', '', 'RGB light bar; SL low-profile'), ('VENGEANCE RGB', 'Corsair', '', 'DDR5'),
    ('VENGEANCE DDR5 SODIMM', 'Corsair', '', 'laptop')]),
 X('Corsair Dominator', 'Corsair', '', 'Corsair_Gaming', 'Corsair\'s premium overclocking memory with heavy heat spreaders.',
   [('Dominator Platinum', 'Corsair', '', 'built for overclocking'), ('DOMINATOR TITANIUM RGB', 'Corsair', '', 'DDR5')]),
 X('G.Skill Trident Z', 'G.Skill', '', 'G.Skill', 'G.Skill\'s flagship enthusiast memory line, a common pick for overclocked builds.', a='TridentZ',
   v=[('Trident Z', 'G.Skill', '', 'DDR4'), ('Trident Z5 NEO RGB', 'G.Skill', '', 'DDR5, for AMD')]),
 X('Kingston FURY', 'Kingston', '2014', 'Kingston_Technology', 'Kingston\'s enthusiast memory, first under HyperX and from 2021 under its own FURY name.',
   [('HyperX FURY', 'Kingston', '2014', ''), ('Kingston FURY', 'Kingston', '2021', 'rebrand after HyperX peripherals were sold to HP')]),
 X('Kingston ValueRAM', 'Kingston', '1997', 'Kingston_Technology', 'Kingston\'s plain low-cost memory modules, built to standard specifications.'),
]

kinds = [
 {'n': 'Processor', 'a': 'CPU · central processing unit', 'd': 'Central processing chip of a computer, bought by builders and upgraders for a socket on the motherboard.',
  't': ['desktop (socketed)', 'laptop (soldered)', 'with integrated graphics (APU)', 'unlocked / overclockable', 'workstation / HEDT', 'server'],
  's': 'https://shop.tsukumo.co.jp/dir/20', 'x': cpu_x,
  'r': [['Core Ultra 5', 'Intel'], ['Core Ultra 7', 'Intel'], ['Core Ultra 9', 'Intel'], ['Core i3', 'Intel'], ['Core i5', 'Intel'], ['Core i7', 'Intel'], ['Core i9', 'Intel'],
        ['Celeron', 'Intel'], ['Pentium', 'Intel'], ['Xeon', 'Intel'], ['Ryzen 3', 'AMD'], ['Ryzen 5', 'AMD'], ['Ryzen 7', 'AMD'], ['Ryzen 9', 'AMD'], ['Ryzen Threadripper', 'AMD'], ['Athlon', 'AMD']]},
 {'n': 'Motherboard', 'a': 'mainboard · mobo · マザーボード', 'd': 'Main circuit board of a computer, into which the processor, memory and cards fit.',
  't': ['ATX', 'micro-ATX', 'Mini-ITX', 'E-ATX', 'Intel socket (LGA)', 'AMD socket (AM4, AM5, sTR5)', 'with CPU fitted (embedded board)', 'rear-connector (BTF)'],
  's': 'https://kakaku.com/pc/motherboard/', 'x': mb_x, 'm': mb_m,
  'r': [['ROG Maximus', 'ASUS'], ['ROG Crosshair', 'ASUS'], ['ROG Strix', 'ASUS'], ['TUF Gaming', 'ASUS'], ['ProArt', 'ASUS'], ['Prime', 'ASUS'],
        ['AORUS', 'Gigabyte'], ['Aero G', 'Gigabyte'], ['Gaming X', 'Gigabyte'], ['Vision G', 'Gigabyte'], ['Taichi', 'ASRock'], ['MEG', 'MSI']]},
 {'n': 'Memory (RAM)', 'a': 'RAM · memory module · DIMM · SODIMM', 'd': 'Plug-in module of working memory for a desktop or laptop.',
  't': ['desktop DIMM', 'laptop SODIMM', 'DDR3', 'DDR4', 'DDR5', 'CUDIMM / CSODIMM (clocked)', 'RGB lighting', 'kit of 2 or 4'],
  's': 'https://shop.tsukumo.co.jp/dir/20', 'x': ram_x,
  'r': [['VENGEANCE', 'Corsair'], ['DOMINATOR', 'Corsair'], ['Trident Z', 'G.Skill'], ['FURY', 'Kingston'], ['ValueRAM', 'Kingston']]},
]

K = 'knowledge'
def B(n, c, f, seg, kf, d, s=K, **kw):
    b = {'n': n, 'c': c, 'f': f, 'seg': seg, 'kf': kf, 'd': d, 's': s}; b.update(kw); return b
brands = [
 B('Intel', 'United States', '1968', 'Professional & flagship', 'x86 processors', 'Chipmaker behind the 4004, the x86 line and the Core processors.', K,
   lines=['Core', 'Core Ultra', 'Pentium', 'Celeron', 'Xeon'], sig=['Intel 8086', 'Intel Core i3 / i5 / i7 / i9']),
 B('AMD', 'United States', '1969', 'Professional & flagship', 'Ryzen processors', 'Chipmaker of Athlon and Ryzen x86 processors and Radeon graphics.', K,
   lines=['Ryzen', 'Ryzen Threadripper', 'Athlon'], sig=['Athlon 64', 'AMD Ryzen']),
 B('Apple', 'United States', '1976', 'Premium', 'Macs, Apple silicon', 'Computer and phone maker that designs its own M-series chips.', K),
 B('ASUS', 'Taiwan', '1989', 'Mainstream', 'motherboards, ROG', 'Taiwanese maker of motherboards, graphics cards and laptops.', K,
   lines=['ROG', 'TUF Gaming', 'ProArt', 'Prime'], sig=['ASUS ROG motherboards']),
 B('Gigabyte', 'Taiwan', '1986', 'Mainstream', 'motherboards, AORUS', 'Taiwanese maker of motherboards and graphics cards.', W + 'Gigabyte_Technology', lines=['AORUS', 'Aero', 'Gaming']),
 B('ASRock', 'Taiwan', '2002', 'Mainstream', 'motherboards', 'Taiwanese motherboard maker, part of the Pegatron group.', W + 'ASRock', lines=['Taichi'], rel=['ASUS']),
 B('MSI', 'Taiwan', '1986', 'Mainstream', 'motherboards, gaming', 'Taiwanese maker that built its name on motherboards.', W + 'Micro-Star_International', lines=['MEG', 'MPG', 'MAG', 'PRO']),
 B('Corsair', 'United States', '1994', 'Premium', 'memory, PC parts', 'American maker of memory and PC components, founded as Corsair Microsystems.', W + 'Corsair_Gaming', lines=['Vengeance', 'Dominator']),
 B('G.Skill', 'Taiwan', '1989', 'Specialist', 'enthusiast memory', 'Taiwanese memory maker known for high-speed kits.', W + 'G.Skill', lines=['Trident Z']),
 B('Kingston', 'United States', '1987', 'Mainstream', 'memory', 'Large independent memory-module maker.', W + 'Kingston_Technology', lines=['FURY', 'ValueRAM']),
 B('Crucial', 'United States', '', 'Mainstream', 'memory, SSDs', 'Micron\'s consumer memory and SSD brand, discontinued in February 2026.', W + 'Crucial_(brand)'),
]
out = {'kinds': kinds, 'brands': brands, 'traditions': [],
       'notes': 'Processor: 2,857 SKUs cut to 13 archetypes (historic icons 4004/8086/386/Pentium/Athlon/Athlon 64/Core 2, Core i, Core Ultra, Ryzen incl. X3D, Threadripper, Xeon and Apple M stubs) with generations and key SKUs from the old list; Celeron left as range only. Motherboard: "Motherboard with CPU" merged as type; 103 SKUs cut to 4 line archetypes + 11 models. MSI MPG/MAG and ASUS TUF/ProArt left as ranges (no retrieved page). Memory: desktop and laptop RAM merged. Crucial in brand register only (brand discontinued 2026); no Crucial model was in the old data.'}
p = '/home/user/Possession-Taxonomy/rebuild/work/D1/shelves/01_00.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('written')
