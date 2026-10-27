import json, os
W = 'https://en.wikipedia.org/wiki/'
def X(n, mk, y, s, d, v=(), a='', dt=''):
    x = {'n': n, 'a': a, 'd': d, 'mk': mk, 'y': y, 's': s if s.startswith('http') else W + s,
         'v': [dict(zip(('n', 'mk', 'y', 'd'), t)) for t in v]}
    if dt: x['dt'] = dt
    return x
NO = 'Noctua'
air_x = [
 X('Noctua NH-D15', NO, '2014', 'https://www.tweaktown.com/reviews/6313/noctua-nh-d15-cpu-cooler-review/index.html',
   'Dual-tower, twin-fan air cooler that long set the benchmark for air cooling, in Noctua\'s brown and beige.',
   [('NH-D14', NO, '', 'predecessor'), ('NH-D15', NO, '2014', 'two NF-A15 fans'), ('NH-D15S', NO, '', 'single-fan, offset for RAM clearance'), ('NH-D15 G2', NO, '', 'second generation')],
   dt='brown/beige or black (chromax) · single or dual fan'),
 X('Cooler Master Hyper 212', 'Cooler Master', '', 'Cooler_Master', 'Budget single-tower air cooler, for years the standard first upgrade over a stock cooler.',
   [('Hyper 212 Evo', 'Cooler Master', '', 'popular budget upgrade')]),
 X('Thermalright Peerless Assassin 120 SE', 'Thermalright', '2022', 'https://tomshardware.com/reviews/thermalright-peerless-assassin-120-se',
   'Inexpensive dual-tower air cooler whose performance rivals far dearer coolers.', a='PA120 SE',
   v=[('Peerless Assassin 120 SE', 'Thermalright', '2022', 'under $40 at review')]),
]
aio_x = [
 X('Arctic Liquid Freezer', 'Arctic', '', 'https://gamersnexus.net/coolers/new-best-arctic-liquid-freezer-iii-360-280-cpu-cooler-review-benchmarks',
   'Thick-radiator AIO line with a small VRM fan in the pump, a frequent test winner.',
   [('Liquid Freezer II', 'Arctic', '', 'long a top-tested liquid cooler'), ('Liquid Freezer III', 'Arctic', '2023', '280 and 360 mm; Intel contact frame included')]),
 X('NZXT Kraken', 'NZXT', '2013', 'NZXT', 'NZXT\'s AIO line, known for its styled pump head.',
   [('Kraken (first)', 'NZXT', '2013', '140 and 280 mm')]),
]
loop_x = [
 X('EK custom loop parts', 'EKWB', '2003', 'EKWB', 'Slovenian range of water blocks, radiators and kits that defines much of the custom-loop hobby.', a='EK-Quantum · EK-Supremacy',
   v=[('EK-Supremacy', 'EKWB', '', 'CPU and GPU blocks'), ('EK-Quantum', 'EKWB', '', 'blocks, monoblocks, Quantum Surface radiators')]),
]
tim_x = [
 X('Honeywell PTM7950', 'Honeywell', '', 'https://evezone.evetech.co.za/gear-review/phase-change-thermal-paste-honeywell-ptm7950-vs-paste',
   'Phase-change pad that is solid at room temperature and melts at about 45 °C, prized because it does not pump out.',
   [('PTM7950', 'Honeywell', '', 'performs about level with Kryonaut and NT-H2')]),
]
kinds = [
 {'n': 'CPU air cooler', 'a': 'tower cooler · heatsink', 'd': 'Heatsink with heat pipes and a fan that cools a processor by air.',
  't': ['single tower', 'dual tower', 'low-profile / top-down', 'passive (fanless)'], 's': 'https://www.noctua.at/en/products/browse/coolers', 'x': air_x,
  'm': [['NH-U12S', NO], ['NH-U12A', NO], ['NH-U14S', NO], ['NH-D12L', NO], ['NH-C14S', NO], ['NH-L12S', NO], ['NH-L9i', NO], ['NH-L9a', NO], ['NH-L9x65', NO], ['NH-P1', NO]]},
 {'n': 'AIO liquid cooler', 'a': 'all-in-one liquid cooler · closed-loop cooler', 'd': 'Sealed pump, radiator and block unit that cools a processor or graphics chip by liquid.',
  't': ['120 mm', '240 mm', '280 mm', '360 mm', '420 mm', 'with LCD pump head'], 's': 'https://www.corsair.com/us/en/c/cpu-coolers', 'x': aio_x,
  'm': [['iCUE LINK TITAN', 'Corsair'], ['iCUE H150i ELITE CAPELLIX', 'Corsair'], ['iCUE H100i RGB PRO XT', 'Corsair'], ['Galahad II Trinity', 'Lian Li'],
        ['HydroShift LCD AIO', 'Lian Li'], ['MAELSTROM 240T', 'Deepcool'], ['CAPTAIN 360X', 'Deepcool'], ['NL-LC1', NO], ['XPG Levante II 360', 'XPG'], ['Hanbo Chroma', 'Razer']],
  'r': [['Liquid Freezer', 'Arctic'], ['H-Series', 'Corsair'], ['Galahad II', 'Lian Li'], ['MAELSTROM', 'Deepcool'], ['CAPTAIN', 'Deepcool'], ['Kraken', 'NZXT']]},
 {'n': 'Custom liquid-cooling parts', 'a': 'custom-loop parts · water-cooling parts', 'd': 'Separate parts (blocks, pumps, radiators, fittings, tubing) for building an open liquid-cooling loop.',
  't': ['CPU block', 'GPU block', 'monoblock', 'pump & reservoir', 'radiator', 'fittings & tubing (soft, hard)', 'coolant'],
  's': 'https://www.titanrig.com/water-cooling/aio-coolers.html', 'x': loop_x},
 {'n': 'Case fan', 'a': 'PC fan', 'd': 'Fan fitted to a computer case or radiator to move air.',
  't': ['120 mm', '140 mm', 'static pressure (radiator)', 'airflow', 'RGB', 'daisy-chain / interlocking'], 's': 'https://lian-li.com/product-category/cooling/fans/',
  'm': [['NF-A12x25', NO], ['NF-A14x25 G2', NO], ['NF-A14', NO], ['NF-A12x15', NO], ['NF-S12A', NO], ['NF-P12 redux', NO], ['UNI FAN SL-INF', 'Lian Li'], ['UNI FAN TL', 'Lian Li'], ['UNI FAN CL', 'Lian Li'], ['UNI FAN SL', 'Lian Li']],
  'r': [['UNI FAN', 'Lian Li'], ['NF-A', NO], ['redux', NO]]},
 {'n': 'Thermal paste & pads', 'a': 'thermal interface material · TIM · グリス · 熱伝導シート', 'd': 'Material that fills the gap between a chip and its cooler to carry heat across.',
  't': ['paste', 'pad', 'liquid metal', 'phase-change pad'], 's': 'https://www.arctic.de/us/MX-6/ACTCP00079A', 'x': tim_x,
  'm': [['MX-4', 'Arctic'], ['MX-6', 'Arctic'], ['NT-H2', NO], ['TP-3', 'Arctic'], ['TP-4', 'Arctic']]},
 {'n': 'M.2 heatsink', 'a': 'SSD heatsink', 'd': 'Heat spreader fitted to an M.2 drive.', 's': 'https://bequiet.com/en/accessories/2251', 'm': [['MC1', 'be quiet!'], ['MC1 Pro', 'be quiet!']]},
 {'n': 'Fan controller', 'a': 'fan hub · RGB controller · ファンコントローラー', 'd': 'Unit or hub that sets the speed and lighting of case fans.',
  't': ['fan hub', 'RGB / ARGB hub', 'bay-mounted controller with knobs', 'software-controlled'], 's': 'https://shop.tsukumo.co.jp/dir/20'},
]
K = 'knowledge'
def B(n, c, f, seg, kf, d, s=K, **kw):
    b = {'n': n, 'c': c, 'f': f, 'seg': seg, 'kf': kf, 'd': d, 's': s}; b.update(kw); return b
brands = [
 B(NO, 'Austria', '2005', 'Professional & flagship', 'quiet coolers, fans', 'Austrian maker of air coolers and fans in its brown-and-beige colours.', W + 'Noctua_(company)', sig=['Noctua NH-D15']),
 B('Arctic', 'Germany', '', 'Value', 'value coolers, paste', 'German maker of coolers, fans and thermal paste.', W + 'Arctic_(company)', lines=['Liquid Freezer', 'MX']),
 B('Thermalright', 'Taiwan', '', 'Value', 'budget air coolers', 'Taiwanese cooler maker known for cheap, strong dual-tower coolers.'),
 B('EKWB', 'Slovenia', '2003', 'Specialist', 'custom water cooling', 'Slovenian maker of custom water-cooling blocks and radiators.', W + 'EKWB', lines=['EK-Quantum', 'EK-Supremacy']),
 B('Honeywell', 'United States', '', 'Specialist', 'industrial materials', 'Industrial group whose PTM7950 pad became an enthusiast favourite.'),
 B('Deepcool', 'China', '', 'Value', 'coolers, cases', 'Chinese maker of coolers and cases.'),
]
out = {'kinds': kinds, 'brands': brands, 'traditions': [],
       'notes': 'Thermal paste and thermal pad merged into "Thermal paste & pads" (types paste, pad, liquid metal, phase-change). AIO: 57 old SKUs cut to 10 models + 2 archetypes (Liquid Freezer, Kraken). Air cooler archetypes NH-D15, Hyper 212, Peerless Assassin; be quiet! Dark Rock, Scythe Fuma, Corsair Hydro X, Alphacool, Watercool Heatkiller, Arctic P12, Phanteks T30, Thermal Grizzly Kryonaut not added as archetypes (no page retrieved naming their versions). Fan controller and custom-loop parts kept with no old models.'}
p = '/home/user/Possession-Taxonomy/rebuild/work/D1/shelves/01_03.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('written')
