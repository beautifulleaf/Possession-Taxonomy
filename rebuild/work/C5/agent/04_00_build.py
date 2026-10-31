import json, os
W = 'https://en.wikipedia.org/wiki/'
OW = 'https://www.officeworks.com.au/shop/officeworks/c/office-supplies/calculators'
CU = 'https://www.casio.com/uk/scientific-calculators/product.FX-83GT-CW-PLUS-GY/'


def X(n, d, mk, y, s, v=(), a='', dt=''):
    o = {'n': n, 'a': a, 'd': d, 'mk': mk, 'y': y, 's': s, 'v': [dict(zip(('n', 'mk', 'y', 'd'), t)) for t in v]}
    if dt: o['dt'] = dt
    return o

C, TI, HP = 'Casio', 'Texas Instruments', 'HP'

sci = {'n': 'Scientific calculator', 'a': 'school calculator · engineering calculator',
 'd': 'Calculator with trigonometric, logarithmic and statistical functions.',
 't': ['natural (textbook) display', 'two-line display', 'solar with battery backup', 'RPN', 'programmable', 'exam-approved'],
 's': OW,
 'x': [
  X('Casio fx-82 / ClassWiz', 'Casio\'s school scientific line since 1982, now the ClassWiz range with textbook display; fx-83/85 are the UK versions and fx-991 the advanced model.', C, '1982', W + 'Casio_fx-82_series',
    [('fx-82', C, '1982', 'upgrade of the fx-80'), ('fx-82MS', C, '2001', ''), ('fx-82ES', C, '2004', ''), ('fx-82EX (ClassWiz)', C, '2015', ''), ('fx-82CW', C, '', 'current ClassWiz'),
     ('fx-83GT CW', C, '', 'UK, replaced by fx-83GT CW+'), ('fx-83GT CW+', C, '', 'UK, 290+ functions, AAA battery'), ('fx-85GT CW', C, '', 'UK, solar'), ('fx-85GT CW+', C, '', 'solar, up to 90% recycled materials'),
     ('fx-991CW', C, '', 'advanced model'), ('fx-991CW UK+', C, '', 'more than 540 functions')], dt='colours: black, blue, grey, pink (CW+)'),
  X('TI-30', 'Texas Instruments\' long-running school scientific calculator, first sold for about US$25.', TI, '1976', W + 'TI-30',
    [('TI-30', TI, '1976', 'LED original'), ('TI-30 Galaxy', TI, '', 'mid-1980s landscape'), ('TI-30Xa', TI, '1994', ''), ('TI-30X IIS', TI, '1998', ''),
     ('TI-30XS MultiView', TI, '2005', ''), ('TI-30X Pro MultiView / TI-36X Pro', TI, '2011', ''), ('TI-30X Pro MathPrint', TI, '2018', '')]),
  X('HP 35s', 'RPN and algebraic programmable scientific calculator made for the HP-35\'s 35th anniversary; allowed in US FE and PE exams.', HP, '2007', W + 'HP_35s',
    [('HP 33s', HP, '', 'predecessor'), ('HP 35s', HP, '2007', 'discontinued 2021')], dt='retro styling · two CR2032 cells'),
 ]}

gr = {'n': 'Graphing calculator', 'a': 'graphic calculator',
 'd': 'Programmable calculator that plots functions on a graphic display.',
 't': ['monochrome', 'colour screen', 'CAS (computer algebra)', 'Python programmable', 'exam mode'],
 's': OW,
 'x': [
  X('TI-84 Plus', 'Texas Instruments\' mainstream school graphing calculator, upgrade of the TI-83 Plus.', TI, '2004', W + 'TI-84_Plus_series',
    [('TI-84 Plus', TI, '2004', ''), ('TI-84 Plus Silver Edition', TI, '2004', 'discontinued 2015'), ('TI-84 Plus C Silver Edition', TI, '2013', ''), ('TI-84 Plus CE', TI, '', 'about 2015')]),
  X('TI-Nspire', 'TI\'s document-based graphing calculator, with CAS versions.', TI, '2007', W + 'TI-Nspire_series',
    [('TI-Nspire / Nspire CAS', TI, '2007', ''), ('TI-Nspire CX / CX CAS', TI, '2011', 'colour'), ('TI-Nspire CX II / CX II CAS', TI, '2019', ''), ('TI-Nspire CX II-T', TI, '', 'European version')]),
  X('Casio Prizm (fx-CG)', 'Casio\'s colour graphing calculators, the first full-colour graphing models.', C, '2011', W + 'Casio_Prizm',
    [('fx-CG10 / fx-CG20', C, '2011', 'sold as PRIZM in North America'), ('fx-CG50', C, '2017', 'MicroPython'), ('fx-CG100 ClassWiz CG', C, '2024', 'successor to fx-CG50')]),
  X('HP Prime', 'Colour touchscreen graphing calculator with a separate CAS home screen based on Xcas/Giac.', HP, '2013', W + 'HP_Prime',
    [('HP Prime G1', HP, '2013', ''), ('HP Prime G2', HP, '2018', '2AP18AA, about three times faster')]),
  X('NumWorks', 'French graphing calculator programmable in Python, with source-available software and open hardware design.', 'NumWorks', '2017', W + 'NumWorks',
    [('N0100', 'NumWorks', '2017', 'discontinued 2019'), ('N0110', 'NumWorks', '', ''), ('N0115', 'NumWorks', '', ''), ('N0120', 'NumWorks', '', '')]),
 ]}

fin = {'n': 'Financial calculator', 'a': 'business calculator',
 'd': 'Calculator with time-value-of-money and other finance functions.',
 't': ['RPN', 'algebraic', 'exam-approved'],
 's': OW,
 'x': [
  X('HP 12C', 'Gold-faced RPN financial calculator in continuous production since 1981.', HP, '1981', W + 'HP-12C',
    [('HP-12C', HP, '1981', 'original'), ('HP 12c Platinum', HP, '2003', 'adds algebraic entry, silver face'), ('HP 12c Prestige', HP, '2008', ''), ('30th Anniversary Edition', HP, '2011', 'NW258AA, 40,000 made')]),
  X('TI BA II Plus', 'Texas Instruments\' main financial calculator.', TI, '1991', W + 'Texas_Instruments_Business_Analyst',
    [('BA II Plus', TI, '1991', ''), ('BA II Plus (2014 revision)', TI, '2014', 'larger display digits'), ('BA II Plus Professional', TI, '2004', 'adds NFV and MIRR'), ('BA-35', TI, '1985', 'simpler student model')]),
 ]}

basic = {'n': 'Basic calculator', 'a': 'desk calculator · pocket calculator · printing calculator · adding machine',
 'd': 'Calculator for the four operations and percentages, from pocket and desk models to printing calculators with a paper roll.',
 't': ['pocket', 'desktop', 'solar', 'printing calculator', 'ink roller (spare part)', 'tax and currency keys'],
 's': OW,
 'm': [['Casio HR-100RC', 'Casio']]}


def B(n, c, f, seg, kf, d, s, lines=(), sig=()):
    return {'n': n, 'c': c, 'f': f, 'seg': seg, 'kf': kf, 'd': d, 'lines': list(lines), 'eras': [], 'sig': list(sig), 'sc': [], 'rel': [], 's': s}

brands = [
 B(C, 'Japan', '1946', 'Mainstream', 'calculators, watches', 'Tokyo electronics maker of school scientific and graphing calculators.', 'knowledge', ['ClassWiz', 'Prizm'], ['Casio fx-82 / ClassWiz', 'Casio Prizm (fx-CG)']),
 B(TI, 'United States', '1930', 'Mainstream', 'school calculators', 'Dallas semiconductor company and major maker of school calculators.', 'knowledge', ['TI-30', 'TI-84 Plus', 'TI-Nspire', 'BA II Plus'], ['TI-84 Plus', 'TI-30', 'TI BA II Plus', 'TI-Nspire']),
 B(HP, 'United States', '1939', 'Premium', 'RPN calculators', 'Hewlett-Packard, Palo Alto maker of RPN scientific and financial calculators.', 'knowledge', ['12C', '35s', 'Prime'], ['HP 12C', 'HP 35s', 'HP Prime']),
 B('NumWorks', 'France', '2016', 'Specialist', 'Python graphing calculators', 'French company founded by Romain Goyet making Python-programmable graphing calculators.', W + 'NumWorks', ['N0110', 'N0120'], ['NumWorks']),
]

notes = ('All four planned kinds kept. Old Printing calculator and Calculator ink roller merged into Basic calculator as types; HR-100RC kept as a model. '
 'Old Casio models fx-83GT CW, fx-85GT CW, fx-991CW and fx-CG50/fx-CG100 and TI BA II PLUS became versions of archetypes. '
 'No independent test winners for basic calculators added (no retrieved test page). Casio, TI and HP brand facts from knowledge; HP calculators\' current licensing not stated. Casio education site 403.')
out = {'kinds': [sci, gr, fin, basic], 'brands': brands, 'traditions': [], 'notes': notes}
p = 'work/C5/shelves/04_00.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
