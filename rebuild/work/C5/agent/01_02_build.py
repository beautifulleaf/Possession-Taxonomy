import json, os
W = 'https://en.wikipedia.org/wiki/'
PA = 'https://www.penaddict.com/blog/'
UNI = 'Mitsubishi Pencil (Uni)'
MP = W + 'Mechanical_pencil'
PEN = W + 'Pencil'


def X(n, d, mk, y, s, v=(), a='', dt=''):
    o = {'n': n, 'a': a, 'd': d, 'mk': mk, 'y': y, 's': s, 'v': [dict(zip(('n', 'mk', 'y', 'd'), t)) for t in v]}
    if dt: o['dt'] = dt
    return o


wood = {'n': 'Wooden pencil', 'a': 'wood-cased pencil · lead pencil · graphite pencil',
 'd': 'Graphite core cased in wood, sharpened to use; graded from hard (H) to soft (B).',
 't': ['hexagonal', 'round', 'triangular', 'with eraser tip', 'grades 10H–12B (US No. 1–4)'],
 's': PEN,
 'x': [
  X('Koh-i-Noor 1500', 'Graded drawing pencil in 20 grades from the Koh-i-Noor brand, introduced in 1890.', 'Koh-i-Noor Hardtmuth', '1890', PEN,
    [('1500', 'Koh-i-Noor Hardtmuth', '', '10H–8B')]),
  X('Faber-Castell Castell 9000', 'Dark-green hexagonal graded pencil launched by Count Alexander von Faber-Castell.', 'Faber-Castell', '1905',
    'https://fabercastellusa.reamaze.io/kb/history-and-fun-facts/faber-castell-castell-9000-born-in-1905', [('Castell 9000', 'Faber-Castell', '1905', '')]),
  X('Blackwing 602', 'Soft-graphite pencil with a metal eraser clip, stamped "Half the Pressure, Twice the Speed"; used by Steinbeck and animators.', 'Eberhard Faber', '1934', W + 'Blackwing_602',
    [('Blackwing 602', 'Eberhard Faber', '1934', 'made until 1988'), ('Blackwing 602', 'Faber-Castell', '1988', 'after acquisition'),
     ('Blackwing 602', 'Sanford', '1994', 'discontinued 1998'), ('Palomino Blackwing', 'Blackwing', '2011', 'revival by California Cedar'), ('Blackwing Pearl', 'Blackwing', '', '')]),
  X('Dixon Ticonderoga', 'Yellow hexagonal US school pencil with green ferrule and pink eraser.', 'Dixon Ticonderoga', '', W + 'Dixon_Ticonderoga',
    [('Ticonderoga', 'Dixon Ticonderoga', '', 'American cedar'), ('The World\'s Best Pencil', 'Dixon Ticonderoga', '', '')]),
  X('Uni Hi-Uni', 'Japanese premium graded pencil in 22 grades, the rival the Mono 100 answered.', UNI, '', PEN,
    [('Hi-Uni', UNI, '', '10H–10B'), ('Uni 9850', UNI, '', '')]),
  X('Tombow Mono 100', 'Glossy black pencil with a white end stripe, designed by Takashi Kono.', 'Tombow', '1967', 'https://www.cwpencils.com/blog-archive/a-moment-in-pencil-history-tombow-mono-100',
    [('Mono 100', 'Tombow', '1967', ''), ('Mono-R', 'Tombow', '', ''), ('Mono-J', 'Tombow', '', ''), ('Mono Professional', 'Tombow', '', 'US market'), ('2558', 'Tombow', '', '')]),
  X('Staedtler Mars Lumograph', 'Drawing and drafting pencil in 24 grades.', 'Staedtler', '', PEN, [('Mars Lumograph', 'Staedtler', '', '10H–12B')]),
 ]}

mech = {'n': 'Mechanical pencil', 'a': 'propelling pencil · シャープペンシル · drafting pencil',
 'd': 'Refillable holder that advances a thin lead (0.2–1.4 mm) by a mechanism.',
 't': ['click (ratchet)', 'twist (screw)', 'drafting (long lead sleeve)', 'retractable tip', 'auto-rotating lead', 'lead-protecting', '0.2–1.4 mm'],
 's': MP,
 'x': [
  X('Sampson Mordan propelling pencil', 'Early refillable propelling pencil patented in Britain.', 'Sampson Mordan', '1822', MP, [('Propelling pencil', 'Sampson Mordan', '1822', 'with John Isaac Hawkins')]),
  X('Eversharp', 'Early mass-produced propelling pencil that set the 1.18 mm lead standard.', '', '1913', MP, [('Eversharp', '', '1913', 'Charles R. Keeran patent')]),
  X('Pentel Sharp P200', 'Light plastic drafting pencil with brass clutch, design little changed since the 1970s.', 'Pentel', '1970s', 'https://yosekastationery.com/blogs/news/pentel-200-series',
    [('Sharp P200 series', 'Pentel', '', '0.3–0.9 mm')]),
  X('Pentel Graph 1000 for Pro', 'Drafting pencil with aluminium grip, rubber bumps and a step tip.', 'Pentel', '', PA + '2026/4/15/pentel-graph-1000-for-pro-drafting-pencil-review',
    [('Graph 1000 for Pro', 'Pentel', '', '0.5 mm'), ('60th Anniversary Edition', 'Pentel', '', 'blacked-out'), ('Creator\'s Style', 'Pentel', '', 'metallic blue'), ('GraphGear 1000', 'Pentel', '', 'metal body, retractable pipe')]),
  X('Pentel Smash', 'Lightweight drafting pencil with rubber-pad grip and notched grade dial.', 'Pentel', '', PA + '2021/3/3/pentel-q1005-smash-drafting-pencil-review',
    [('Smash Q1005', 'Pentel', '', ''), ('Katakana Smash', 'Pentel', '', 'special edition')]),
  X('Pentel Orenz', 'Pencil whose retractable guide pipe protects ultra-thin lead from breaking.', 'Pentel', '', PA + '2014/9/2/pentel-orenz-02-mm-mechanical-pencil-review',
    [('Orenz 0.2', 'Pentel', '', ''), ('Orenz Nero', 'Pentel', '', '')]),
  X('Rotring 600 / 800', 'Hexagonal knurled metal drafting pencils; the 800 adds a retractable tip.', 'Rotring', '', 'https://www.architecturelab.net/rotring-800-mechanical-pencil/',
    [('600', 'Rotring', '', 'metal body, fixed tip'), ('800', 'Rotring', '', 'brass body, retractable tip'), ('Tikky', 'Rotring', '', '')]),
  X('Uni Kuru Toga', 'Pencil whose clutch rotates the lead 9° each stroke to keep a sharp point.', UNI, '', MP,
    [('Kuru Toga', UNI, '', '9° per stroke'), ('Kuru Toga Advance', UNI, '', ''), ('Kuru Toga Dive', UNI, '', ''), ('Kuru Toga Metal', UNI, '', ''), ('Kuru Toga Roulette', UNI, '', ''), ('Kuru Toga Wood', UNI, '', '')]),
  X('Zebra DelGuard', 'Pencil with a lead-protection mechanism against breakage.', 'Zebra', '', MP, [('DelGuard', 'Zebra', '', '')]),
  X('Pilot S20', 'Wood-bodied drafting pencil with a grade window in the cap.', 'Pilot', '', 'https://www.penciltalk.org/?p=170', [('S20', 'Pilot', '', ''), ('S10', 'Pilot', '', 'related model')]),
  X('Staedtler 925 25', 'Metal drafting pencil.', 'Staedtler', '', MP, [('925 25 05', 'Staedtler', '', '0.5 mm')]),
  X('Lamy 2000 pencil', 'Makrolon and steel pencil of the 1966 Lamy 2000 design.', 'Lamy', '', W + 'Lamy_2000', [('2000 mechanical pencil', 'Lamy', '', '')]),
  X('Caran d\'Ache 844', 'Hexagonal aluminium pencil matching the 849 ballpoint; Swiss made.', 'Caran d\'Ache', '', 'https://shop.gentlemanstationer.com/products/caran-dache-844-7mm-mechanical-pencil',
    [('844', 'Caran d\'Ache', '', '0.7 mm')]),
 ],
 'm': [['Ballograf Epoca P', 'Ballograf'], ['E+M Move', 'E+M'], ['Kitera Double Chuck', 'Kitera'], ['Monteverde One Touch Tool Pencil', 'Monteverde'],
       ['Morning Glory Sketch 1000', 'Morning Glory'], ['Pilot Color Eno', 'Pilot']]}

holder = {'n': 'Lead holder', 'a': 'clutch pencil · leadholder',
 'd': 'Holder whose clutch grips a thick lead (2 mm or more) that drops when the button is pressed; sharpened in a lead pointer.',
 't': ['2 mm', '3.15 mm', '5.6 mm', 'cap sharpener', 'all-metal'],
 's': 'https://www.jetpens.com/Pencils/ct/1319',
 'x': [
  X('Staedtler Mars Technico 780', 'German 2 mm clutch holder with a lead sharpener in the end cap.', 'Staedtler', '', 'https://www.parkablogs.com/node/14313',
    [('Mars Technico 780', 'Staedtler', '', '2 mm, Mars Carbon leads')]),
  X('Koh-i-Noor 5900 / Versatil', 'All-metal 2 mm Czech holders with a four-blade cap sharpener.', 'Koh-i-Noor Hardtmuth', '', 'https://www.penciltalk.org/?p=1148',
    [('5900 Toison d\'Or', 'Koh-i-Noor Hardtmuth', '', ''), ('5201 Versatil', 'Koh-i-Noor Hardtmuth', '', 'yellow'), ('5216 Versatil', 'Koh-i-Noor Hardtmuth', '', '10 colours')]),
  X('Caran d\'Ache Fixpencil', 'Swiss clutch holder for thick leads.', 'Caran d\'Ache', '', MP, [('Fixpencil', 'Caran d\'Ache', '', ''), ('Fixpencil 22', 'Caran d\'Ache', '', '')]),
  X('Faber-Castell TK', 'Clutch lead holder for 2 mm leads.', 'Faber-Castell', '', MP, [('TK', 'Faber-Castell', '', '2.0 mm')]),
 ],
 'm': [['Alvin Tech-Matic', 'Alvin']]}

leads = {'n': 'Pencil leads', 'a': 'pencil lead refill · leads',
 'd': 'Tube of leads for mechanical pencils or lead holders, chosen by diameter and grade.',
 't': ['0.2 mm', '0.3 mm', '0.5 mm', '0.7 mm', '0.9 mm', '1.18 mm', '2 mm', '3.15 mm', '5.6 mm', 'polymer-bound', 'colour'],
 's': 'https://www.jetpens.com/Pencil-Leads/ct/99',
 'm': [['Pentel Ain lead', 'Pentel'], ['Pilot Neox high-purity graphite lead', 'Pilot'], ['Uni Smudge-Proof lead', UNI], ['Mars Carbon 2 mm lead', 'Staedtler'], ['Koh-i-Noor colour leads', 'Koh-i-Noor Hardtmuth']]}

sharp = {'n': 'Pencil sharpener', 'a': 'sharpener · lead pointer',
 'd': 'Device that sharpens a wooden pencil, manual or electric; lead pointers sharpen lead-holder leads.',
 't': ['hand-held', 'two-step long point', 'rotary (crank)', 'electric', 'lead pointer', 'brass wedge'],
 's': 'https://www.jetpens.com/Pencil-Sharpeners/ct/1255',
 'x': [
  X('KUM Automatic Long Point', 'Two-hole hand sharpener: one blade cuts the wood, the second points the core.', 'KUM', '', 'https://www.parkablogs.com/content/review-kum-automatic-long-point-pencil-sharpener',
    [('2-blade', 'KUM', '', ''), ('4-blade', 'KUM', '', 'adds 2 and 3.15 mm lead pointers'), ('Automatic Brake Long Point', 'KUM', '', ''), ('Meisterwerk', 'KUM', '', '')]),
  X('Carl Angel-5', 'Japanese desk crank sharpener, the reviewers\' benchmark for graphite points.', 'Carl', '', 'https://bleistift.blog/tag/dahle-133/', [('Angel-5', 'Carl', '', '')]),
  X('Dahle 133', 'Rotary crank sharpener with protected grippers, good for coloured and oversize pencils.', 'Dahle', '', 'https://bleistift.blog/tag/dahle-133/', [('133', 'Dahle', '', 'adjustable point')]),
 ],
 'm': [['Blackwing One-Step Long Point', 'Blackwing'], ['Blackwing Two-Step Long Point', 'Blackwing'], ['Dux Brass Sharpener', 'Dux'], ['Kita-Boshi 634', 'Kita-Boshi'],
       ['Kutsuwa Stad T\'Gaal', 'Kutsuwa'], ['Sonic Ratchetta Capsule', 'Sonic'], ['Deli 0635', 'Deli'], ['Staedtler Mars Technico lead pointer', 'Staedtler']]}


def B(n, c, f, seg, kf, d, s, lines=(), sig=()):
    return {'n': n, 'c': c, 'f': f, 'seg': seg, 'kf': kf, 'd': d, 'lines': list(lines), 'eras': [], 'sig': list(sig), 'sc': [], 'rel': [], 's': s}


brands = [
 B('Koh-i-Noor Hardtmuth', 'Czech Republic', '1790', 'Heritage manufactory', 'pencils, lead holders', 'České Budějovice pencil maker of the 1500 and Versatil.', 'knowledge', ['1500', 'Versatil', 'Toison d\'Or'], ['Koh-i-Noor 1500', 'Koh-i-Noor 5900 / Versatil']),
 B('Faber-Castell', 'Germany', '1761', 'Mainstream', 'pencils', 'Stein pencil maker founded by Kaspar Faber.', 'knowledge', ['Castell 9000', 'TK', 'Textliner'], ['Faber-Castell Castell 9000']),
 B('Eberhard Faber', 'United States', '', 'Heritage manufactory', 'pencils', 'New York pencil maker of the original Blackwing 602, bought by Faber-Castell in 1988.', W + 'Blackwing_602', ['Blackwing 602'], ['Blackwing 602']),
 B('Blackwing', 'United States', '2011', 'Premium', 'pencils', 'Revived Blackwing brand of California Cedar\'s Palomino division.', W + 'Blackwing_602', ['Blackwing 602', 'Pearl'], ['Blackwing 602']),
 B('Dixon Ticonderoga', 'United States', '', 'Mainstream', 'school pencils', 'Maker of the Ticonderoga, owned by F.I.L.A. since 2005.', W + 'Dixon_Ticonderoga', ['Ticonderoga'], ['Dixon Ticonderoga']),
 B(UNI, 'Japan', '1887', 'Mainstream', 'pencils, Kuru Toga', 'Tokyo pen and pencil maker selling as Uni.', 'knowledge', ['Hi-Uni', 'Kuru Toga', '9800/9850'], ['Uni Hi-Uni', 'Uni Kuru Toga']),
 B('Tombow', 'Japan', '1913', 'Mainstream', 'pencils', 'Tokyo stationery maker of the Mono pencils.', 'knowledge', ['Mono 100', 'Mono'], ['Tombow Mono 100']),
 B('Staedtler', 'Germany', '1835', 'Mainstream', 'pencils, drafting', 'Nuremberg writing and drawing instrument maker.', 'knowledge', ['Mars Lumograph', 'Mars Technico', '925'], ['Staedtler Mars Lumograph', 'Staedtler Mars Technico 780']),
 B('Pentel', 'Japan', '1946', 'Mainstream', 'mechanical pencils', 'Tokyo maker that introduced 0.5 and 0.7 mm polymer leads in 1962.', W + 'Pentel', ['Sharp', 'Graph 1000', 'Orenz', 'Smash', 'Ain'], ['Pentel Sharp P200', 'Pentel Graph 1000 for Pro']),
 B('Rotring', 'Germany', '1928', 'Mainstream', 'drafting instruments', 'Hamburg drafting-instrument maker.', 'knowledge', ['600', '800', 'Tikky'], ['Rotring 600 / 800']),
 B('Zebra', 'Japan', '1897', 'Mainstream', 'pens and pencils', 'Tokyo pen maker.', 'knowledge', ['DelGuard'], ['Zebra DelGuard']),
 B('Pilot', 'Japan', '1918', 'Mainstream', 'pens and pencils', 'Japan\'s largest pen maker.', 'knowledge', ['S20', 'Neox'], ['Pilot S20']),
 B('Lamy', 'Germany', '1930', 'Premium', 'design pens', 'Heidelberg design-led pen maker.', W + 'Lamy_2000', ['2000'], ['Lamy 2000 pencil']),
 B('Caran d\'Ache', 'Switzerland', '1915', 'Premium', 'pencils, 849', 'Geneva maker of pencils, the 849 and Fixpencil.', 'knowledge', ['844', '849', 'Fixpencil'], ['Caran d\'Ache 844', 'Caran d\'Ache Fixpencil']),
 B('Sampson Mordan', 'United Kingdom', '', 'Heritage manufactory', 'propelling pencils', 'London silversmith who patented an early propelling pencil in 1822.', MP, ['propelling pencils'], ['Sampson Mordan propelling pencil']),
 B('KUM', 'Germany', '', 'Specialist', 'sharpeners', 'German sharpener maker known for the Long Point.', 'https://www.parkablogs.com/content/review-kum-automatic-long-point-pencil-sharpener', ['Long Point', 'Meisterwerk'], ['KUM Automatic Long Point']),
 B('Carl', 'Japan', '', 'Specialist', 'sharpeners, punches', 'Japanese office-tool maker of the Angel-5 sharpener.', 'https://bleistift.blog/tag/dahle-133/', ['Angel-5'], ['Carl Angel-5']),
 B('Dahle', 'Germany', '', 'Mainstream', 'sharpeners, trimmers', 'German maker of rotary sharpeners and paper trimmers.', 'https://bleistift.blog/tag/dahle-133/', ['133'], ['Dahle 133']),
]

notes = ('All five planned kinds kept. Old JetPens model lists restructured into archetypes (Blackwing 602 with its owners, Mono 100, Hi-Uni, Kuru Toga family, Orenz, Rotring Tikky into Rotring 600/800, Staedtler Mars Technico 780). '
 'Old range Tombow MONO folded into Mono 100 archetype; Pentel Ain range kept as a lead model. Not added: Staedtler Noris, Caran d\'Ache Swiss Wood, Platinum Pro-Use, Rotring and Hi-Uni launch years, Blackwing slogan source beyond Wikipedia (no retrieved page for the others); '
 'Pentel P203/205/207/209 named only by series. Brand facts for Koh-i-Noor, Faber-Castell, Uni, Tombow, Staedtler, Rotring, Zebra, Pilot, Caran d\'Ache from knowledge; KUM, Carl, Dahle founding years left blank. architecturelab.net blocked WebFetch and was retrieved via firecrawl.')
out = {'kinds': [wood, mech, holder, leads, sharp], 'brands': brands, 'traditions': [], 'notes': notes}
p = 'work/C5/shelves/01_02.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('archetypes', sum(len(k.get('x', [])) for k in out['kinds']))
