import json, os
W = 'https://en.wikipedia.org/wiki/'
def X(n, mk, y, s, d, v=(), a='', dt=''):
    x = {'n': n, 'a': a, 'd': d, 'mk': mk, 'y': y, 's': s if s.startswith('http') else W + s,
         'v': [dict(zip(('n', 'mk', 'y', 'd'), t)) for t in v]}
    if dt: x['dt'] = dt
    return x
LL = 'Lian Li'
case_x = [
 X('Fractal Design Define', 'Fractal Design', '2009', 'Fractal_Design', 'Quiet, sound-dampened Scandinavian-styled tower case line that made Fractal Design\'s name.',
   [('Define (first)', 'Fractal Design', '2009', ''), ('Define (new generation)', 'Fractal Design', '2016', '')], dt='brushed solid front · sound-dampening panels'),
 X('Fractal Design Meshify', 'Fractal Design', '2017', 'https://aphnetworks.com/reviews/fractal-design-meshify-c', 'Airflow-first case line with an angular mesh front, set beside the quiet Define.',
   [('Meshify C', 'Fractal Design', '2017', 'compact ATX mid-tower, tempered-glass side')]),
 X('NZXT H series', 'NZXT', '2017', 'NZXT', 'NZXT\'s clean, minimal steel-and-glass mid-tower line, a staple of first builds.',
   [('H700 / H400 / H200', 'NZXT', '2017', ''), ('H500', 'NZXT', '2018', ''), ('H510 (Elite)', 'NZXT', '2019', 'refresh')]),
 X('Lian Li O11 Dynamic', LL, '2018', 'https://gamersnexus.net/hwreviews/3285-lian-li-o11-dynamic-review-benchmark-der8auer-case-design',
   'Dual-chamber glass "fish-tank" case co-designed with overcloker der8auer, built for radiators and show builds.',
   [('PC-O11', LL, '', 'earlier model it grew from'), ('O11 Dynamic', LL, '2018', 'der8auer edition, no fans included'), ('O11 Air', LL, '', 'mesh-fronted airflow version'),
    ('O11 Dynamic Mini / Mini V2', LL, '', ''), ('O11 Dynamic EVO / EVO RGB / EVO XL', LL, '', 'reversible layout'), ('O11 Vision / Vision Compact', LL, '', 'pillarless glass'),
    ('O11 Air Mini', LL, '', '')], dt='glass front and side · dual chamber · ATX, mATX, E-ATX · black, white'),
 X('Corsair 4000D', 'Corsair', '2020', 'https://pcper.com/2020/10/corsair-4000d-airflow-tempered-glass-mid-tower-atx-case-review/', 'Corsair\'s widely recommended affordable ATX mid-tower in three front-panel variants.',
   [('4000D', 'Corsair', '2020', 'solid steel front'), ('4000D AIRFLOW', 'Corsair', '2020', 'ventilated front, two 120 mm fans'), ('4000X RGB', 'Corsair', '2020', 'glass front, three RGB fans')]),
 X('Dan A4-SFX', 'Dan Cases', '', 'https://techpowerup.com/review/dan-a4-sfx', 'Tiny aluminium Mini-ITX case that still takes a full-length graphics card; a small-form-factor icon.',
   [('A4-SFX V4.1', 'Dan Cases', '', 'smallest full-GPU ITX case TechPowerUp had reviewed')]),
 X('Cooler Master MasterBox NR200', 'Cooler Master', '2020', 'https://www.tweaktown.com/reviews/9611/cooler-master-masterbox-nr200-mini-itx-chassis/index.html',
   'Affordable ventilated Mini-ITX case of about 18 litres that brought small-form-factor building to the mainstream.',
   [('NR200', 'Cooler Master', '2020', 'steel mesh panels'), ('NR200P', 'Cooler Master', '', 'adds a tempered-glass side panel')]),
]
case_m = [['Lancool III', LL], ['Lancool 216', LL], ['Vector V100', LL], ['ROG Hyperion GR701', 'ASUS'], ['ROG Strix Helios II', 'ASUS'],
          ['TUF Gaming GT502', 'ASUS'], ['ProArt PA602', 'ASUS'], ['Prime AP201', 'ASUS']]
kinds = [
 {'n': 'PC case', 'a': 'computer case · chassis · tower · PCケース', 'd': 'Enclosure that holds a computer\'s motherboard, drives, cards and power supply.',
  't': ['full tower', 'ATX mid-tower', 'micro-ATX', 'Mini-ITX / small form factor', 'dual-chamber', 'open frame / test bench', 'HTPC'],
  's': 'https://lian-li.com/product-category/cases/', 'x': case_x, 'm': case_m,
  'r': [['O11', LL], ['Lancool', LL], ['Vector', LL], ['Define', 'Fractal Design'], ['Meshify', 'Fractal Design'], ['H series', 'NZXT'],
        ['ROG', 'ASUS'], ['TUF Gaming', 'ASUS'], ['ProArt', 'ASUS'], ['Prime', 'ASUS']]},
 {'n': 'PC power supply', 'a': 'PSU · power supply unit · 電源ユニット', 'd': 'Unit fitted in the case that turns mains power into the voltages the parts need.',
  't': ['ATX', 'SFX / SFX-L', 'modular / semi-modular / fixed cables', 'ATX 3.x with 12V-2x6 (PCIe 5) connector',
        '80 Plus Bronze', '80 Plus Gold', '80 Plus Platinum', '80 Plus Titanium'],
  's': 'https://www.overclockers.co.uk/pc-components/pc-power-supplies',
  'm': [['RPS0110 (CP-9020188) (RM850x)', 'Corsair'], ['RPS0178 (CP-9020263) (RM850e)', 'Corsair'], ['SRP-FGX851-A5A32SF (FOCUS GX-850 ATX 3)', 'Seasonic'],
        ['SF-1000F14MP', 'Super Flower'], ['E12-1000W', 'be quiet!'], ['SuperNOVA 850 GA', 'EVGA'], ['HALE90-850-M', 'NZXT'], ['MPE-8506-ACAG', 'Cooler Master'],
        ['MAG A850GL PCIE5', 'MSI'], ['TOUGHPOWER GF 850W', 'Thermaltake'], ['HGE850', 'FSP'], ['SST-SX1000-LPT', 'Silverstone'], ['ROG-THOR-1000P2-GAMING', 'ASUS'],
        ['FD-P-IA3G-850 (Ion 3 Gold 850W)', 'Fractal Design'], ['EDGE GOLD', LL], ['EA650G PRO', 'Antec']],
  'r': [['PRIME', 'Seasonic'], ['FOCUS', 'Seasonic'], ['RM', 'Corsair'], ['Dark Power', 'be quiet!'], ['Leadex', 'Super Flower'], ['SuperNOVA', 'EVGA']]},
 {'n': 'Internal PC cable', 'a': 'sleeved cable · extension cable · riser cable', 'd': 'Cable that connects parts inside a computer case, such as power extensions and PCIe risers.',
  't': ['sleeved power extension', 'custom-length sleeved PSU cable', 'PCIe riser', 'fan / RGB cable', 'SATA data'],
  's': 'https://lian-li.com/product-category/accessories/cables', 'm': [['Strimer Plus', LL], ['Strimer Wireless', LL], ['AVA riser cable', 'LINKUP']]},
]
K = 'knowledge'
def B(n, c, f, seg, kf, d, s=K, **kw):
    b = {'n': n, 'c': c, 'f': f, 'seg': seg, 'kf': kf, 'd': d, 's': s}; b.update(kw); return b
brands = [
 B('Lian Li', 'Taiwan', '1983', 'Premium', 'aluminium cases', 'Taiwanese case maker known for aluminium and glass cases.', W + 'Lian_Li', lines=['O11', 'Lancool', 'Strimer'], sig=['Lian Li O11 Dynamic']),
 B('Fractal Design', 'Sweden', '2007', 'Premium', 'Scandinavian cases', 'Swedish maker of minimalist cases, coolers and PSUs.', W + 'Fractal_Design', lines=['Define', 'Meshify'], sig=['Fractal Design Define']),
 B('NZXT', 'United States', '2004', 'Mainstream', 'minimal cases', 'Californian maker of cases, Kraken coolers and prebuilt PCs.', W + 'NZXT', lines=['H series', 'Kraken']),
 B('Cooler Master', 'Taiwan', '1992', 'Mainstream', 'cases, coolers', 'Taiwanese maker of cases, coolers and power supplies.', W + 'Cooler_Master', lines=['MasterBox', 'Hyper']),
 B('Dan Cases', 'Germany', '', 'Artisan & independent', 'SFF cases', 'Small independent designer of the A4-SFX small-form-factor case.', 'https://techpowerup.com/review/dan-a4-sfx', rel=['Lian Li']),
 B('Seasonic', 'Taiwan', '1975', 'Professional & flagship', 'power supplies', 'Taiwanese PSU maker, long an OEM for other brands.', W + 'Seasonic', lines=['PRIME', 'FOCUS', 'CORE']),
 B('Super Flower', 'Taiwan', '', 'Specialist', 'power supplies', 'Taiwanese PSU maker, also an OEM for other brands.', lines=['Leadex']),
 B('be quiet!', 'Germany', '2002', 'Premium', 'quiet PSUs, coolers', 'German brand of quiet power supplies, coolers and cases.', lines=['Dark Power', 'Pure Power', 'Dark Rock']),
]
out = {'kinds': kinds, 'brands': brands, 'traditions': [],
       'notes': 'PC case: 7 archetypes from retrieved pages (Define, Meshify, NZXT H, O11 Dynamic, Corsair 4000D, Dan A4-SFX, NR200); old O11 models moved into O11 versions; 8 other old models kept. Cooler Master HAF/Cosmos, Corsair Obsidian and Louqe Ghost not added: no retrieved page in time. PSU: 37 old SKUs trimmed to 16 market-covering models; efficiency (80 Plus) and form factor as types. Old MSI model "MAG A850GLS PCIE5" kept as "MAG A850GL PCIE5"? no — see build: kept spelling from old data.'}
p = '/home/user/Possession-Taxonomy/rebuild/work/D1/shelves/01_02.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('written')
