import json, re, copy, sys
ROOT = '/home/user/Possession-Taxonomy/rebuild/'
src = json.load(open(ROOT + 'out/E3.json'))
brands_reg = {b['n'] for b in json.load(open(ROOT + 'out/E3_brands.json'))['b']}
DEPTS = ["Keyboards & electronic instruments", "Drums & percussion", "Recording & live sound", "DJ equipment"]
WK = 'https://en.wikipedia.org/wiki/'
U = dict(
    SY=WK + 'List_of_synthesizers', KO=WK + 'List_of_Korg_products', DM=WK + 'Drum_machine', MPC=WK + 'Akai_MPC',
    JUP=WK + 'Roland_Jupiter', RO=WK + 'Roland_Corporation', MO=WK + 'Moog_Music', SQ=WK + 'Sequential_(company)',
    OB=WK + 'Oberheim_Electronics', HA=WK + 'Hammond_organ', RH=WK + 'Fender_Rhodes', WU=WK + 'Wurlitzer_electric_piano',
    BO=WK + 'B%C3%B6sendorfer', ST=WK + 'Steinway_%26_Sons', ED=WK + 'Electronic_drum', PE=WK + 'Pearl_Drums',
    PA=WK + 'Paiste', LU=WK + 'Ludwig_Drums', TA=WK + 'Tama_Drums', DW=WK + 'Drum_Workshop', ZI=WK + 'Zildjian',
    NE=WK + 'Georg_Neumann', SH=WK + 'Shure', SS=WK + 'Solid_State_Logic', NV=WK + 'Neve_Electronics',
    CDJ=WK + 'CDJ', DJM=WK + 'DJM', YA=WK + 'Yamaha_Corporation', FE=WK + 'Fender_Musical_Instruments_Corporation',
    SM=WK + 'List_of_synthesizer_manufacturers')

def norm(s): return re.sub(r'[^a-z0-9]', '', s.lower())
def yr(y):
    m = re.search(r'\d{4}', y or '')
    return int(m.group()) if m else 9999
def clean(mk): return re.sub(r'\s*\((audio|Pioneer DJ)\)', '', mk).strip() if mk not in ('AlphaTheta (Pioneer DJ)',) else mk

def E(n, mk, y, d, s, v=None, a='', dt=''):
    return dict(n=n, a=a, d=d, mk=mk, y=y, s=U.get(s, s), v=v or [], dt=dt)
def V(n, mk, y='', d=''): return dict(n=n, mk=mk, y=y, d=d)

NEW = {}   # kind -> list of entries
VADD = {}  # (kind, entry) -> list of versions
def add(kind, *entries): NEW.setdefault(kind, []).extend(entries)
def addv(kind, entry, *vs): VADD.setdefault((kind, entry), []).extend(vs)

# ---------------- KEYBOARDS: pianos, organs --------------------
add('Grand piano',
    E('Steinway Boston grands', 'Steinway & Sons', '', 'Steinway-designed grand piano line, sold as Boston: GP-156 PE, GP-163 PE, GP-178 PE, GP-193 PE and GP-215 PE.', 'ST'),
    E('Steinway Essex grands', 'Steinway & Sons', '', 'Steinway-designed entry grand line, sold as Essex: EGP-155 and EGP-173.', 'ST'),
    E('Bösendorfer Swarovski Crystal Grand', 'Bösendorfer', '2003', 'Limited Bösendorfer grand set with Swarovski crystal; three were made.', 'BO'),
    E('Bösendorfer Hans Hollein 225', 'Bösendorfer', '1990', 'Bösendorfer 225 in a design by Hans Hollein; two were made.', 'BO'))
add('Electric piano',
    E('Rhodes Mark 7', 'Rhodes', '2007', 'Later Rhodes electric piano in the line begun by Harold Rhodes.', 'RH'),
    E('Rhodes Mark 8', 'Rhodes', '2021', 'Rhodes electric piano issued in 2021, listed as the MK8.', 'RH'),
    E('Rhodes Xylette', 'Rhodes', '1945', 'Earliest instrument in the Rhodes article, from 1945.', 'RH'),
    E('Wurlitzer 120', 'Wurlitzer', '1956–1962', 'Wurlitzer reed electric piano in production 1956 to 1962.', 'WU'),
    E('Wurlitzer 140', 'Wurlitzer', '1962–1968', 'Wurlitzer reed electric piano in pre-A, A and B variants, 1962 to 1968.', 'WU',
      v=[V('140', 'Wurlitzer', '1962'), V('145 / 145B', 'Wurlitzer', '', 'phased out late 1965'), V('146 / 146B', 'Wurlitzer', '', 'solid-state classroom variant')]),
    E('Wurlitzer 300', 'Wurlitzer', '1973', 'European-only Wurlitzer electric piano of early 1973.', 'WU'),
    E('Wurlitzer 700', 'Wurlitzer', '', 'Wurlitzer electric piano listed with the 720; year not stated on the page.', 'WU', v=[V('720', 'Wurlitzer')]))
addv('Tonewheel organ', 'Hammond B-3', V('Hammond B-3 (infobox date)', 'Hammond', '1955', 'The article infobox gives 1955; the text gives 1954'))
add('Tonewheel organ',
    E('Hammond Model BC', 'Hammond', '1936', 'Two-manual tonewheel console from 1936.', 'HA'),
    E('Hammond Model D', 'Hammond', '1939', 'Hammond console of 1939 in the early A to D series.', 'HA'),
    E('Hammond RT', 'Hammond', '1949', 'Church console with pedals from 1949.', 'HA'),
    E('Hammond X-66', 'Hammond', '1967', 'Hammond model of 1967.', 'HA'),
    E('Hammond Concorde', 'Hammond', '1971', 'Hammond model of 1971.', 'HA'),
    E('Hammond Aurora 8000', 'Hammond', '1976', 'Hammond Aurora of 1976; the 8000M followed in 1977.', 'HA', v=[V('8000M Aurora', 'Hammond', '1977')]),
    E('Hammond X-5', 'Hammond', '1979', 'Nihon Hammond model of 1979.', 'HA'),
    E('Hammond XB-3', 'Hammond', '1990s', 'Clonewheel Hammond of the 1990s.', 'HA'),
    E('Hammond XK clonewheel line', 'Hammond', '2014', 'Hammond digital drawbar line: XK-1c 2014, XK-5 2016, SK-X 2019.', 'HA',
      v=[V('XK-1c', 'Hammond', '2014'), V('XK-5', 'Hammond', '2016'), V('SK-X', 'Hammond', '2019')]),
    E('Korg CX-3', 'Korg', '1980', 'Korg organ of 1980 in the Korg product list.', 'KO'))
# ---------------- SYNTHESIZERS --------------------
MON, POL = 'Monophonic synthesizer', 'Polyphonic synthesizer'
add(MON,
    E('Moog Satellite', 'Moog Music', '1974–1979', 'Moog monophonic synthesizer sold 1974 to 1979.', 'MO'),
    E('Moog Sonic Six', 'Moog Music', '1974–1979', 'Moog duophonic synthesizer sold 1974 to 1979.', 'MO'),
    E('Minitmoog', 'Moog Music', '1975–1976', 'Moog monophonic synthesizer sold 1975 to 1976.', 'MO'),
    E('Micromoog', 'Moog Music', '1975–1979', 'Moog monophonic synthesizer sold 1975 to 1979.', 'MO'),
    E('Multimoog', 'Moog Music', '1978–1981', 'Moog monophonic synthesizer sold 1978 to 1981.', 'MO'),
    E('Moog Prodigy', 'Moog Music', '1979–1984', 'Moog monophonic synthesizer sold 1979 to 1984.', 'MO'),
    E('Moog Rogue', 'Moog Music', '1981–1983', 'Moog monophonic synthesizer sold 1981 to 1983.', 'MO'),
    E('Moog Source', 'Moog Music', '1981–1984', 'Moog monophonic synthesizer sold 1981 to 1984.', 'MO'),
    E('Moog Little Phatty', 'Moog Music', '2006–2013', 'Moog analogue monosynth sold 2006 to 2013.', 'MO'),
    E('Moog Slim Phatty', 'Moog Music', '2010–2014', 'Moog analogue monosynth sold 2010 to 2014.', 'MO'),
    E('Moog Minitaur', 'Moog Music', '2012', 'Moog bass synthesizer module of 2012.', 'MO'),
    E('Moog Sub Phatty', 'Moog Music', '2013', 'Moog analogue monosynth of 2013.', 'MO'),
    E('Moog Sub 37', 'Moog Music', '2014', 'Moog analogue monosynth of 2014; the Subsequent 37 followed in 2017.', 'MO'),
    E('Moog Werkstatt-01', 'Moog Music', '2014', 'Moog kit synthesizer of 2014.', 'MO'),
    E('Moog Mother-32', 'Moog Music', '2015', 'Moog semi-modular synthesizer of 2015.', 'MO'),
    E('Moog DFAM', 'Moog Music', '2017', 'Moog drummer-from-another-mother semi-modular percussion synthesizer, kit 2017 and production from 2018.', 'MO'),
    E('Moog Subharmonicon', 'Moog Music', '2018', 'Moog semi-modular synthesizer, kit 2018 and production from 2020.', 'MO'),
    E('Moog Matriarch', 'Moog Music', '2019–2026', 'Moog semi-modular synthesizer sold 2019 to 2026.', 'MO'),
    E('Moog Mavis', 'Moog Music', '2022', 'Moog semi-modular kit synthesizer of 2022.', 'MO'),
    E('Moog Labyrinth', 'Moog Music', '2024', 'Moog synthesizer of 2024.', 'MO'),
    E('Sequential Pro-One', 'Sequential', '1981', 'Sequential Circuits monophonic synthesizer of 1981.', 'SQ'),
    E('Oberheim SEM', 'Oberheim', '1974', 'Oberheim Synthesizer Expander Module of 1974; a new version by Tom Oberheim followed in 2009.', 'OB', v=[V('SEM (new version)', 'Oberheim', '2009')]),
    E('Roland SH-1000', 'Roland', '1973', 'Roland monophonic synthesizer of 1973.', 'RO'),
    E('Roland SH-3', 'Roland', '1973', 'Roland monophonic synthesizer of 1973, with the SH-3A.', 'RO', v=[V('SH-3A', 'Roland', '1973')]),
    E('Roland SH-2000', 'Roland', '', 'Roland synthesizer named on Wikidata; year not stated.', 'RO'),
    E('Korg miniKORG 700', 'Korg', '1973', 'First Korg synthesizer, with the MAXI KORG 800DV following in 1974.', 'KO',
      v=[V('MAXI KORG 800DV', 'Korg', '1974'), V('miniKORG 700FS', 'Korg', '2021'), V('miniKORG 700Sm', 'Korg', '2025')]),
    E('Korg SB-100', 'Korg', '1975', 'Korg bass synthesizer of 1975.', 'KO'),
    E('Korg Mono/Poly', 'Korg', '1981', 'Korg four-oscillator monophonic synthesizer of 1981.', 'KO'),
    E('Korg Monotron', 'Korg', '2010', 'Korg pocket analogue synthesizer of 2010; the Monotribe followed in 2011.', 'KO', v=[V('Monotribe', 'Korg', '2011')]),
    E('Korg Minilogue', 'Korg', '2015', 'Korg analogue polyphonic keyboard of 2015 with the Monologue (2017) and Minilogue XD (2019).', 'KO',
      v=[V('Minilogue', 'Korg', '2015'), V('Monologue', 'Korg', '2017'), V('Minilogue XD', 'Korg', '2019')]),
    E('Korg Volca FM2', 'Korg', '2022', 'Korg Volca FM synthesizer of 2022.', 'KO'),
    E('Korg Phase 8', 'Korg', '2026', 'Korg acoustic synthesizer listed for 2026.', 'KO'),
    E('Buchla Model 100 Series', 'Buchla and Associates', '1963', 'First Buchla modular system, 1963; the Series 200 followed in 1970.', 'SY', v=[V('Buchla Series 200', 'Buchla and Associates', '1970')]))
add(POL,
    E('Moog Polymoog', 'Moog Music', '1975–1980', 'Moog polyphonic synthesizer sold 1975 to 1980.', 'MO'),
    E('Moog Memorymoog', 'Moog Music', '1982–1985', 'Moog polyphonic synthesizer sold 1982 to 1985.', 'MO'),
    E('Moog Opus 3', 'Moog Music', '1980–1983', 'Moog ensemble keyboard sold 1980 to 1983.', 'MO'),
    E('Moog Concertmate MG-1', 'Moog Music', '1981–1983', 'Moog polyphonic synthesizer sold 1981 to 1983.', 'MO'),
    E('Moog Taurus bass pedals', 'Moog Music', '1976–1983', 'Moog bass pedal synthesizer sold 1976 to 1983; the Taurus 3 followed in 2011.', 'MO'),
    E('Moog Sirin', 'Moog Music', '2019', 'Moog synthesizer of 2019.', 'MO'),
    E('Sequential Prophet 600', 'Sequential', '1982', 'Sequential Circuits six-voice synthesizer of 1982.', 'SQ'),
    E('Sequential Prophet T8', 'Sequential', '1983', 'Sequential Circuits weighted-key eight-voice synthesizer of 1983.', 'SQ'),
    E('Sequential Prophet VS', 'Sequential', '', 'Sequential Circuits vector synthesizer named in the Sequential article.', 'SQ'),
    E('Sequential Six-Trak', 'Sequential', '', 'Sequential Circuits multitimbral synthesizer named in the Sequential article.', 'SQ'),
    E('Sequential Split-8', 'Sequential', '', 'Sequential Circuits synthesizer named in the Sequential article.', 'SQ'),
    E('Sequential Prophet ’08', 'Sequential', '2008', 'Dave Smith Instruments analogue polyphonic synthesizer of 2008.', 'SQ', v=[V('Prophet Rev2', 'Dave Smith Instruments', '2017')]),
    E('Dave Smith Instruments Evolver', 'Sequential', '2002', 'Dave Smith Instruments hybrid synthesizer of 2002.', 'SQ'),
    E('Sequential Prophet-X', 'Sequential', '2018', 'Dave Smith Instruments sample-based synthesizer of 2018, rebranded as Sequential that August.', 'SQ'),
    E('Oberheim Two Voice', 'Oberheim', '1975', 'Oberheim two-voice SEM synthesizer of 1975; the Four Voice also dates from 1975.', 'OB', v=[V('Four Voice', 'Oberheim', '1975'), V('Two Voice Pro', 'Oberheim', '2014')]),
    E('Oberheim OB-1', 'Oberheim', '1977', 'Oberheim monosynth of 1977.', 'OB'),
    E('Oberheim OB-Xa', 'Oberheim', '1980', 'Oberheim eight-voice synthesizer, successor to the OB-X.', 'OB'),
    E('Oberheim OB-8', 'Oberheim', '1983', 'Oberheim polyphonic synthesizer of 1983.', 'OB'),
    E('Oberheim Matrix-1000', 'Oberheim', '1988', 'Oberheim rack synthesizer; the article gives 1988 and its text 1987.', 'OB'),
    E('Oberheim Matrix-6', 'Oberheim', '', 'Oberheim matrix-modulation synthesizer; year not stated.', 'OB'),
    E('Oberheim Matrix-12', 'Oberheim', '', 'Oberheim twelve-voice matrix synthesizer; year not stated.', 'OB'),
    E('Oberheim Xpander', 'Oberheim', '', 'Oberheim six-voice multitimbral synthesizer; year not stated.', 'OB'),
    E('Oberheim OB-Mx', 'Oberheim', '1994', 'Oberheim synthesizer of 1994.', 'OB'),
    E('Oberheim OB*12', 'Oberheim', '2000', 'Oberheim synthesizer of 2000 (the Wikidata item Oberheim OB12 lists Viscount as maker).', 'OB'),
    E('Oberheim OB-6', 'Oberheim', '2016', 'Dave Smith and Tom Oberheim analogue polysynth of 2016.', 'OB'),
    E('Oberheim OB-X8', 'Oberheim', '2022', 'Oberheim eight-voice synthesizer of 2022.', 'OB'),
    E('Oberheim TEO-5', 'Oberheim', '2024', 'Oberheim synthesizer of 2024.', 'OB'),
    E('Yamaha DX1', 'Yamaha', '1983', 'Flagship FM synthesizer of the DX range, 1983.', 'SY'),
    E('Yamaha DX21', 'Yamaha', '1985', 'Yamaha FM synthesizer of 1985.', 'SY'),
    E('Yamaha DX7II', 'Yamaha', '1987', 'Revised DX7 with improved voices, 1987.', 'SY'),
    E('Yamaha TX81Z', 'Yamaha', '1987', 'Yamaha four-operator FM rack module of 1987.', 'SY'),
    E('Yamaha DX11', 'Yamaha', '1988', 'Yamaha FM synthesizer of 1988.', 'SY'),
    E('Roland Jupiter-4', 'Roland', '1978', 'Roland analogue synthesizer of 1978.', 'JUP'),
    E('Roland Jupiter-6', 'Roland', '1983', 'Roland analogue synthesizer of 1983.', 'JUP'),
    E('Roland MKS-80 Super Jupiter', 'Roland', '1984', 'Rack version of the Jupiter-8 line, 1984.', 'JUP'),
    E('Roland JP-8000', 'Roland', '1996', 'Roland virtual-analogue synthesizer of 1996; the JP-8080 followed in 1998.', 'JUP', v=[V('JP-8080', 'Roland', '1998')]),
    E('Roland Jupiter-50', 'Roland', '2011', 'Roland digital synthesizer of 2011.', 'JUP'),
    E('Roland Jupiter-80', 'Roland', '2011', 'Roland digital synthesizer of 2011.', 'JUP'),
    E('Roland Jupiter-Xm', 'Roland', '2019', 'Compact Roland digital synthesizer of 2019.', 'JUP'),
    E('Roland Jupiter-X', 'Roland', '2020', 'Roland digital synthesizer of 2020.', 'JUP'),
    E('Roland JX-3P', 'Roland', '1983', 'Roland six-voice analogue synthesizer of 1983.', 'SY'),
    E('Roland JX-8P', 'Roland', '1985', 'Roland analogue synthesizer of 1985.', 'RO'),
    E('Roland JX-10', 'Roland', '1986', 'Roland analogue synthesizer of 1986.', 'RO'),
    E('Roland Alpha Juno', 'Roland', '1985', 'Roland analogue synthesizer of 1985 in the Juno family.', 'SY'),
    E('Roland JD-800', 'Roland', '1991', 'Roland digital synthesizer of 1991.', 'SY'),
    E('Roland JD-990', 'Roland', '1993', 'Roland digital synthesizer module of 1993.', 'RO'),
    E('Roland System 100', 'Roland', '1976', 'Roland modular analogue system of 1976.', 'RO'),
    E('Roland System 700', 'Roland', '1976', 'Roland large modular analogue system of 1976.', 'RO'),
    E('Korg Polysix', 'Korg', '1981', 'Korg six-voice analogue polyphonic synthesizer of 1981.', 'SY'),
    E('Korg Poly-61', 'Korg', '1982', 'Korg analogue polyphonic synthesizer of 1982.', 'KO'),
    E('Korg Poly-800', 'Korg', '1983', 'Korg low-cost polyphonic synthesizer of 1983.', 'KO'),
    E('Korg DW-6000 / DW-8000', 'Korg', '1985', 'Korg digital waveform synthesizers of 1985.', 'KO', v=[V('DW-6000', 'Korg', '1985'), V('DW-8000', 'Korg', '1985')]),
    E('Korg DS-8', 'Korg', '1987', 'Korg FM synthesizer of 1987.', 'KO'),
    E('Korg DSM-1', 'Korg', '1987', 'Korg rack synthesizer of 1987.', 'KO'),
    E('Korg Wavestation', 'Korg', '1990', 'Korg vector and wave-sequencing synthesizer of 1990, developed by former Sequential staff.', 'SY'),
    E('Korg Prophecy', 'Korg', '1995', 'Korg physical-modelling monophonic synthesizer of 1995.', 'KO'),
    E('Korg Z1', 'Korg', '1997', 'Korg physical-modelling synthesizer of 1997.', 'KO'),
    E('Korg NS5R', 'Korg', '1997', 'Korg synthesizer module of 1997.', 'KO'),
    E('Korg MS2000', 'Korg', '2000', 'Korg analogue-modelling synthesizer of 2000.', 'KO'),
    E('Korg microKORG', 'Korg', '2002', 'Compact Korg synthesizer and vocoder of 2002; the microKORG XL followed in 2009 and the microKORG 2 in 2024.', 'KO',
      v=[V('microKORG XL', 'Korg', '2009'), V('microKORG 2', 'Korg', '2024')]),
    E('Korg KingKORG', 'Korg', '2013', 'Korg analogue-modelling synthesizer of 2013; the KingKORG Neo followed in 2024.', 'KO', v=[V('KingKORG Neo', 'Korg', '2024')]),
    E('Korg prologue', 'Korg', '2018', 'Korg analogue polyphonic synthesizer of 2018.', 'KO'),
    E('Korg Wavestate', 'Korg', '2020', 'Korg wave-sequencing synthesizer of 2020, with the Wavestate mkII and SE in 2023.', 'KO', v=[V('Wavestate mkII', 'Korg', '2023'), V('Wavestate SE', 'Korg', '2023')]),
    E('Korg opsix', 'Korg', '2020', 'Korg altered-FM synthesizer of 2020; the opsix SE followed in 2023.', 'KO', v=[V('opsix SE', 'Korg', '2023')]),
    E('Korg Modwave', 'Korg', '2021', 'Korg wavetable synthesizer of 2021.', 'KO'),
    E('Korg Multi/poly module', 'Korg', '2025', 'Korg synthesizer module listed for 2025.', 'KO'),
    E('PPG Wave', 'Palm Products GmbH (PPG)', '1981', 'German wavetable synthesizer of 1981.', 'SY'),
    E('Kurzweil K250', 'Kurzweil', '1984', 'Kurzweil sampled-sound keyboard of 1984.', 'SY'),
    E('Synclavier', 'New England Digital (NED)', '1980', 'New England Digital digital synthesizer and workstation of 1980.', 'SY'),
    E('Elektron SidStation', 'Elektron', '1999', 'Elektron synthesizer built around the SID chip, 1999.', 'SY'),
    E('Elektron Analog Four', 'Elektron', '2012', 'Elektron four-voice analogue synthesizer of 2012.', 'SY'),
    E('Elektron Digitone', 'Elektron', '2018', 'Elektron eight-voice FM synthesizer of 2018.', 'SY'),
    E('Akai MPC-era Prophet 2000', 'Sequential', '', 'Sequential Prophet 2000 sampling keyboard named in the Sequential article.', 'SQ'))
add('Modular synthesizer and Eurorack module',
    E('Moog modular (reissue)', 'Moog Music', '2015', 'Moog modular system produced 1963 to 1980 and again from 2015.', 'MO'),
    E('Emerson Moog Modular', 'Moog Music', '2014', 'Moog modular recreation of 2014.', 'MO'),
    E('Moog Spectravox', 'Moog Music', '2019', 'Moog semi-modular spectral processor of 2019.', 'MO'))
add('Theremin', E('Moog Theremini', 'Moog Music', '', 'Moog theremin with pitch correction.', 'https://www.sweetwater.com/shop/by-category'))
add('Keytar', E('Korg RK-100S', 'Korg', '2014', 'Korg keytar of 2014; the RK-100S v2 followed in 2020.', 'KO', v=[V('RK-100S 2', 'Korg', '2020')]))
add('Portable keyboard',
    E('Korg i3', 'Korg', '1993', 'Korg arranger workstation of 1993; a Korg i3 was listed again in 2020.', 'KO'),
    E('Korg Pa5X', 'Korg', '2022', 'Korg arranger keyboard of 2022.', 'KO'),
    E('Korg EK-50 Limitless', 'Korg', '2020', 'Korg entertainer keyboard of 2020.', 'KO'))
add('Digital piano',
    E('Korg SV-1', 'Korg', '2009', 'Korg vintage-sound stage piano of 2009; the SV-2 followed in 2020.', 'KO', v=[V('SV-2', 'Korg', '2020')]),
    E('Korg Grandstage', 'Korg', '2017', 'Korg stage piano of 2017.', 'KO'),
    E('Korg LP-380-U', 'Korg', '2021', 'Korg home digital piano of 2021.', 'KO'),
    E('Korg Kronos', 'Korg', '2011', 'Korg workstation of 2011 with the Kronos X (2012), Kronos 2 Titanium (2020) and New Kronos (2025).', 'KO',
      v=[V('Kronos X', 'Korg', '2012'), V('Kronos 2 Titanium', 'Korg', '2020'), V('New Kronos', 'Korg', '2025')]))
add('Sampler',
    E('Korg DSS-1', 'Korg', '1986', 'Korg sampling synthesizer of 1986.', 'KO'),
    E('Ensoniq Mirage', 'Ensoniq', '1984', 'Ensoniq sampling keyboard of 1984.', 'SY'),
    E('E-mu Emulator II', 'E-mu Systems', '1984', 'E-mu sampling keyboard of 1984.', 'SY'),
    E('Casio FZ-1', 'Casio', '', 'Casio sampling keyboard named on Wikidata; year not stated.', 'https://www.wikidata.org/wiki/Special:Search?search=Casio+FZ-1'),
    E('Sequential Prophet 3000', 'Sequential', '1987', 'Sequential Circuits sampler of 1987.', 'SQ'),
    E('Sequential Studio 440', 'Sequential', '', 'Sequential Circuits sampling drum machine and sequencer named in the Sequential article.', 'SQ'))
addv('Sampler', 'Akai MPC', V('MPC60 MkII', 'Akai Professional', '', 'Used by DJ Shadow for the 1996 album Endtroducing'), V('MPC2000XL', 'Akai Professional', '', 'Used by Kanye West for a 2010 MTV Video Music Awards performance'))
add('Groovebox',
    E('Korg Volca series', 'Korg', '2013', 'Korg Volca range from 2013: Beats, Bass and Keys at launch; Drum in 2019; FM2 in 2022.', 'KO',
      v=[V('Volca Beats', 'Korg', '2013'), V('Volca Bass', 'Korg', '2013'), V('Volca Keys', 'Korg', '2013'), V('Volca Drum', 'Korg', '2019')]),
    E('Korg Kross', 'Korg', '2013', 'Korg workstation of 2013.', 'KO'))
add('Step sequencer',
    E('Sequential Model 800', 'Sequential', '1975', 'Sequential Circuits sequencer of 1975; the Model 700 Programmer followed in 1976.', 'SQ'),
    E('Roland MC-8 MicroComposer', 'Roland', '1977', 'Roland computer music sequencer of 1977.', 'RO'),
    E('Oberheim DSX', 'Oberheim', '1981', 'Oberheim digital sequencer of 1981.', 'OB'),
    E('Korg SQ-1', 'Korg', '2015', 'Korg step sequencer of 2015; the SQ-64 followed in 2021.', 'KO', v=[V('SQ-64', 'Korg', '2021')]))
# drum machines
DMK = 'Drum machine'
add(DMK,
    E('Rhythmicon', 'Léon Theremin', '1932', 'Early rhythm instrument by Léon Theremin, first in the Wikipedia drum machine list.', 'DM'),
    E('Chamberlin Rhythmate', 'Chamberlin', '1957', 'Tape-loop rhythm unit of 1957.', 'DM'),
    E('Wurlitzer Sideman', 'Wurlitzer', '1959', 'Wurlitzer rhythm unit of 1959.', 'DM'),
    E('Raymond Scott Rhythm Synthesizer', 'Raymond Scott', '1960', 'Rhythm synthesizer by Raymond Scott, 1960.', 'DM', v=[V('Bandito the Bongo Artist', 'Raymond Scott', '1963')]),
    E('Seeburg Select-A-Rhythm', 'Seeburg', '1964', 'Seeburg/Gulbransen rhythm unit of 1964, with the Rhythm Prince.', 'DM', v=[V('Rhythm Prince', 'Seeburg')]),
    E('Donca-Matic', 'Korg', '1963', 'Keio-Giken rhythm units that became Korg: DA-20 1963, DC-11 mid-1960s, DE-20 and DE-11 1966.', 'DM',
      v=[V('Donca-Matic DA-20', 'Korg', '1963'), V('Donca-Matic DC-11', 'Korg', 'mid-1960s'), V('Donca-Matic DE-20', 'Korg', '1966'), V('Donca-Matic DE-11', 'Korg', '1966')]),
    E('Korg Mini Pops', 'Korg', '1967', 'Keio-Giken (Korg) rhythm units from 1967: MP-2, MP-3 and MP-7.', 'DM', v=[V('MP-2', 'Korg', '1967'), V('MP-3', 'Korg'), V('MP-7', 'Korg')]),
    E('Ace Tone Rhythm Ace', 'Ace Tone', '1967', 'Ace Tone rhythm units: FR-1 1967, FR-3 and FR-15 (1975); Bentley sold a Rhythm Ace.', 'DM',
      v=[V('FR-1', 'Ace Tone', '1967'), V('FR-3', 'Ace Tone'), V('Rhythm Producer FR-15', 'Ace Tone', '1975'), V('Bentley Rhythm Ace', 'Bentley')]),
    E('Eko ComputeRhythm', 'Eko', '1972', 'Eko rhythm computer of 1972.', 'DM'),
    E('PAiA Programmable Drum Set', 'PAiA Electronics', '1975', 'PAiA kit drum machine of 1975.', 'DM'),
    E('Wendel', 'Roger Nichols', '1978', 'Digital drum machine by Roger Nichols, 1978.', 'DM'),
    E('Boss DR-55', 'Boss', '1979', 'Boss programmable rhythm unit of 1979.', 'DM'),
    E('Linn LinnDrum', 'Linn', '1982', 'Linn sampled drum machine of 1982.', 'DM'),
    E('Sequential Drumtraks', 'Sequential', '1984', 'Sequential Circuits drum machine of 1984.', 'SQ'),
    E('Cheetah SpecDrum', 'Cheetah Marketing', '1986', 'Add-on drum sampler for the ZX Spectrum, 1986.', 'DM'),
    E('E-mu Drumulator', 'E-mu Systems', '', 'E-mu sampled drum machine named in the Drum machine article; year not stated.', 'DM'),
    E('Yamaha RX11', 'Yamaha', '', 'Yamaha digital drum machine; year not stated.', 'DM'),
    E('Roland TR-33 / TR-55 / TR-77', 'Roland', '', 'Early Roland rhythm units named in the Roland article; years not stated.', 'RO',
      v=[V('TR-33', 'Roland'), V('TR-55', 'Roland'), V('TR-77 Rhythm 77', 'Roland')]),
    E('Akai Rhythm Wolf', 'Akai Professional', '', 'Akai analogue drum machine of the 2010s.', 'DM'),
    E('Arturia DrumBrute', 'Arturia', '', 'Arturia analogue drum machine named in the Drum machine article.', 'DM'),
    E('MFB Tanzbär', 'MFB', '', 'German analogue drum machine named in the Drum machine article.', 'DM'),
    E('Dave Smith Instruments Tempest', 'Dave Smith Instruments', '', 'Analogue drum machine named in the Drum machine article.', 'DM'),
    E('Roland TR-09', 'Roland', '', 'Boutique recreation of the TR-909 named in the Drum machine article.', 'DM'),
    E('Korg KR-55', 'Korg', '1979–1980', 'Korg Rhythm 55 drum machine.', 'KO'),
    E('Korg KPR-77', 'Korg', '1982', 'Korg analogue drum machine of 1982.', 'KO'),
    E('Korg MR-16', 'Korg', '1985', 'Korg drum machine of 1985.', 'KO'),
    E('Korg DDM-110', 'Korg', '1985', 'Korg digital drum machine of 1985.', 'KO'),
    E('Korg DDD-1', 'Korg', '1986', 'Korg sampling drum machine of 1986.', 'KO'),
    E('Korg DRM-1', 'Korg', '1988', 'Korg drum module of 1988.', 'KO'),
    E('Korg S3', 'Korg', '1991', 'Korg drum machine of 1991.', 'KO'),
    E('Korg KR mini', 'Korg', '2013', 'Korg Rhythm mini of 2013.', 'KO'),
    E('Korg drumlogue', 'Korg', '2022', 'Korg hybrid drum machine of 2022.', 'KO'))
# ---------------- DRUMS --------------------
DR = 'Acoustic drum kit'
add(DR,
    E('Ludwig Vistalite (Amber)', 'Ludwig', '', 'Ludwig acrylic kit family named in the Ludwig article beside Green Sparkle; years not stated.', 'LU'),
    E('Tama Star Drums', 'Tama', '1961', 'Brand under which Hoshino began making drums in 1961 (the Tama article); later Imperial Star and Royal Star.', 'TA',
      v=[V('Imperial Star', 'Tama'), V('Royal Star', 'Tama')]),
    E('Camco', 'Tama', '', 'High-end Camco drum line whose name, designs and patents Tama and Drum Workshop bought after the bankruptcy of Camco.', 'TA'),
    E('Slingerland (DW)', 'Drum Workshop', '2019', 'Slingerland drum company, acquired by DW from Gibson in November 2019.', 'DW'),
    E('Pearl Masters Maple Complete', 'Pearl', '', 'Pearl Masters family; Complete, Gum (2019) and Reserve are listed as current lines.', 'PE',
      v=[V('Masters Maple Complete (MCT)', 'Pearl'), V('Masters Maple Gum (MMG)', 'Pearl', '2019'), V('Masters Maple Reserve (MRV)', 'Pearl'), V('Masters Premium', 'Pearl'), V('Masters Premium Legend (MPL)', 'Pearl', '2011', 'Europe only'), V('Masters Custom', 'Pearl'), V('Masters (1993 series)', 'Pearl', '1993')]),
    E('Pearl Reference Pure', 'Pearl', '2011', 'Pearl Reference line launched in 2011 as Reference Pure.', 'PE', v=[V('Reference (RF)', 'Pearl')]),
    E('Pearl Decade Maple', 'Pearl', '', 'Pearl Decade Maple kit (DMP), listed as a current line.', 'PE'),
    E('Pearl Crystal Beat', 'Pearl', '1973', 'Pearl acrylic kit of 1973, reintroduced in 2014.', 'PE'),
    E('Pearl Session Studio Select', 'Pearl', '2018', 'Pearl kit shown at Winter NAMM 2018; it replaced the Session Studio Classic (2012).', 'PE', v=[V('Session Studio Classic (SSC)', 'Pearl', '2012')]),
    E('Pearl Midtown', 'Pearl', '', 'Pearl compact kit (MDT), listed as a current line.', 'PE'),
    E('Pearl Roadshow', 'Pearl', '', 'Pearl beginner kit (RS), listed as a current line.', 'PE'),
    E('Pearl Session (1991 series)', 'Pearl', '1991–2006', 'Pearl Session series, introduced in 1991 and discontinued in 2006.', 'PE'),
    E('Pearl World Series', 'Pearl', '1986', 'Pearl World Series (WLX/WX), discontinued by 1990 when it was renamed Session.', 'PE'),
    E('Pearl Custom Z', 'Pearl', '1989–1994', 'Pearl Custom Z (CZX), 1989 to 1994.', 'PE'),
    E('Pearl CenterStage', 'Pearl', '', 'Pearl CenterStage kit, listed as a current line.', 'PE'))
add('Snare drum',
    E('Ludwig Challenger', 'Ludwig', '1970s', 'Ludwig snare drum line of the 1970s.', 'LU'),
    E('Pearl StaveCraft', 'Pearl', '', 'Pearl stave-shell snare line, listed as current.', 'PE'),
    E('Pearl UltraCast', 'Pearl', '', 'Pearl cast-shell snare line, listed as current.', 'PE'),
    E('Pearl Symphonic', 'Pearl', '', 'Pearl concert snare line, listed as current.', 'PE'),
    E('Pearl Firecracker', 'Pearl', '', 'Pearl small-diameter effects snare line, listed as current.', 'PE'),
    E('Pearl Reference snare', 'Pearl', '', 'Pearl Reference-series snare line, listed as current.', 'PE'),
    E('Pearl Masterworks snare', 'Pearl', '', 'Pearl Masterworks-series snare line, listed as current.', 'PE'),
    E('Slingerland Radio King (DW)', 'Drum Workshop', '2019', 'Radio King snare name used in the 2019 Slingerland revival by DW.', 'DW'))
add('Electronic drum kit',
    E('Pollard Syndrum', 'Pollard Industries', '1976', 'Early electronic drum, 1976, in the Electronic drum article.', 'ED'),
    E('Alesis PerformancePad', 'Alesis', '', 'Alesis electronic drum pad named in the Electronic drum article.', 'ED'),
    E('Yamaha DTXpress IV', 'Yamaha', '', 'Yamaha DTX kit named in the Electronic drum article.', 'ED'))
addv('Electronic drum kit', 'Roland V-Drums', V('TD-12', 'Roland'), V('TD-12S (V-Stage)', 'Roland'), V('TD-27KV2', 'Roland'), V('TD-30', 'Roland', '2010s'))
addv('Electronic drum kit', 'Simmons SDS-V', V('SDSV', 'Simmons', '1981'))
addv('Cymbal', 'Paiste Formula 602', V('Flat Ride (Space Sound)', 'Paiste', '1960s'))
add('Cymbal',
    E('Paiste Stambul 65', 'Paiste', '1965', 'Paiste series of 1965.', 'PA'),
    E('Paiste Rude', 'Paiste', '1980', 'Paiste unlathed series of 1980.', 'PA'),
    E('Paiste Sound Creation', 'Paiste', '1977', 'Paiste series, with a Short Crash from late 1977.', 'PA'),
    E('Paiste Giant Beat', 'Paiste', '', 'Paiste series named in the Paiste article; year not stated.', 'PA'),
    E('Paiste 3000', 'Paiste', '1989', 'Paiste series, discontinued in 1989.', 'PA'),
    E('Paiste Innovations', 'Paiste', '2001', 'Paiste series of 2001.', 'PA'),
    E('Paiste Alpha', 'Paiste', '', 'Paiste series named in the Paiste article with an Alpha China; year not stated.', 'PA'),
    E('Paiste Colorsound', 'Paiste', '1984', 'Paiste coloured cymbals of 1984.', 'PA'))
# ---------------- RECORDING --------------------
LDC, SDC, DYN = 'Large-diaphragm condenser microphone', 'Small-diaphragm condenser microphone', 'Dynamic microphone'
add(LDC,
    E('Neumann M 49', 'Neumann', '', 'Neumann postwar tube condenser; year not stated.', 'NE'),
    E('Neumann M 50', 'Neumann', '', 'Neumann postwar omnidirectional condenser; year not stated.', 'NE'),
    E('Neumann SM 2', 'Neumann', '1957', 'Neumann stereo condenser of 1957.', 'NE'),
    E('Neumann U 64', 'Neumann', '1964', 'Neumann condenser of 1964.', 'NE'),
    E('Neumann U 77', 'Neumann', '1965', 'Neumann condenser of 1965.', 'NE'),
    E('Neumann U 89', 'Neumann', '1966', 'Neumann multipattern condenser of 1966.', 'NE'),
    E('Neumann USM 69', 'Neumann', '1966', 'Neumann stereo condenser of 1966.', 'NE'),
    E('Neumann TLM 170', 'Neumann', '1983', 'Neumann transformerless condenser of 1983.', 'NE'),
    E('Neumann TLM 193', 'Neumann', '', 'Neumann TLM condenser named in the Neumann article.', 'NE'),
    E('Neumann M 147 / M 149 / M 150 Tube', 'Neumann', '1995', 'Neumann tube condensers of 1995.', 'NE', v=[V('M 147 Tube', 'Neumann', '1995'), V('M 149 Tube', 'Neumann', '1995'), V('M 150 Tube', 'Neumann', '1995')]),
    E('Shure KSM32', 'Shure', '1999', 'Shure side-address condenser of 1999.', 'SH'),
    E('Shure KSM44', 'Shure', '2001', 'Shure multipattern condenser of 2001.', 'SH'),
    E('Shure KSM11', 'Shure', '2023', 'Shure handheld condenser of 2023.', 'SH'),
    E('Shure Model 40D', 'Shure', '1933', 'Shure condenser microphone of 1933.', 'SH'))
addv(LDC, 'Neumann U 87', V('U 87', 'Neumann', '1966'))
add(SDC,
    E('Neumann KM 53 / KM 54 / KM 56', 'Neumann', '1953–1956', 'Neumann small-diaphragm condensers of 1953 to 1956.', 'NE', v=[V('KM 53', 'Neumann'), V('KM 54', 'Neumann'), V('KM 56', 'Neumann')]),
    E('Neumann KM 64', 'Neumann', '1964', 'Neumann small-diaphragm condenser of 1964.', 'NE'),
    E('Neumann KMR 81 / KMR 82', 'Neumann', '1966', 'Neumann shotgun condensers of 1966.', 'NE', v=[V('KMR 81', 'Neumann', '1966'), V('KMR 82', 'Neumann', '1966')]),
    E('Neumann KM D', 'Neumann', '2006', 'Neumann digital small-diaphragm series of 2006.', 'NE'),
    E('Shure KSM9', 'Shure', '2007', 'Shure handheld condenser of 2007.', 'SH'),
    E('Shure KSM8 Dualdyne', 'Shure', '2017', 'Shure dual-diaphragm vocal microphone of 2017.', 'SH'))
add(DYN,
    E('Shure SM5', 'Shure', '1966', 'Shure broadcast dynamic of 1966, predecessor of the SM7.', 'SH'),
    E('Shure Beta 52 / Beta 56', 'Shure', '1989', 'Shure Beta series launched in 1989 with kick drum and snare microphones.', 'SH', v=[V('Beta 52', 'Shure', '1989'), V('Beta 52A', 'Shure'), V('Beta 56', 'Shure', '1989')]),
    E('Shure Beta 87', 'Shure', '1994', 'Shure Beta 87 vocal condenser of 1994.', 'SH'),
    E('Shure Beta 98', 'Shure', '2002', 'Shure Beta 98H/C clip-on instrument microphone of 2002.', 'SH'),
    E('Shure SM86', 'Shure', '2003', 'Shure SM86 of 2003.', 'SH'),
    E('Shure Beta 27', 'Shure', '2010', 'Shure Beta 27 of 2010.', 'SH'),
    E('Shure Beta 181', 'Shure', '2012', 'Shure Beta 181 of 2012.', 'SH'),
    E('Shure MV7', 'Shure', '2020', 'Shure podcast microphone of 2020.', 'SH'),
    E('Shure VP88', 'Shure', '1991', 'Shure stereo mid-side microphone of 1991.', 'SH'),
    E('Shure Model 33N', 'Shure', '1932', 'Shure two-button carbon microphone of 1932.', 'SH'))
add('Wireless microphone system',
    E('Shure L Series', 'Shure', '1990', 'Shure wireless of 1990.', 'SH'),
    E('Shure ULX', 'Shure', '2002', 'Shure wireless line of 2002.', 'SH', v=[V('ULX-D', 'Shure', '2012')]),
    E('Shure SLX', 'Shure', '2005', 'Shure wireless line of 2005.', 'SH', v=[V('SLX-D', 'Shure', '2020'), V('SLX-D+', 'Shure', '2026')]),
    E('Shure UHF-R', 'Shure', '2006', 'Shure wireless of 2006.', 'SH'),
    E('Shure Axient', 'Shure', '2012', 'Shure Axient shipped in 2012; Axient Digital followed in 2017.', 'SH', v=[V('Axient Digital', 'Shure', '2017')]),
    E('Shure BLX', 'Shure', '2013', 'Shure entry wireless of 2013.', 'SH'),
    E('Shure GLX-D', 'Shure', '2013', 'Shure digital wireless of 2013; GLX-D+ followed in 2023.', 'SH', v=[V('GLX-D+', 'Shure', '2023')]),
    E('Shure QLX-D', 'Shure', '2014', 'Shure digital wireless of 2014.', 'SH', v=[V('QLXD24/SM58', 'Shure')]),
    E('Shure PGX-D', 'Shure', '2011', 'Shure wireless of 2011.', 'SH'))
add('In-ear monitor system',
    E('Shure PSM', 'Shure', '1997', 'Shure personal monitor line: PSM 600 1997, PSM 400 and 700 2000, PSM 900 2010.', 'SH',
      v=[V('PSM 600', 'Shure', '1997'), V('PSM 400', 'Shure', '2000'), V('PSM 700', 'Shure', '2000'), V('PSM 900', 'Shure', '2010'), V('PSM300', 'Shure')]))
add('Outboard processor',
    E('Neve 1081', 'Neve', '1973', 'Neve microphone preamplifier and equaliser of 1973.', 'NV'),
    E('Neve 2254', 'Neve', '1968', 'Neve compressor and limiter of 1968.', 'NV'),
    E('Neve 33609', 'Neve', '2009', 'Neve compressor, redesigned by AMS Neve as the 33609JD around 2009.', 'NV'),
    E('SSL G Series Compressor', 'Solid State Logic', '2005', 'SSL bus compressor of 2005.', 'SS'),
    E('SSL XLogic Logic Channel', 'Solid State Logic', '2003', 'SSL channel strip of 2003.', 'SS'))
CON = 'Mixing console'
add(CON,
    E('Neve 8008', 'Neve', '1970', 'Neve console, first for AIR Studios, 1970.', 'NV'),
    E('Neve 8048', 'Neve', '1973', 'Neve console of 1973.', 'NV'),
    E('Neve 8058', 'Neve', '1977', 'Neve console of 1977.', 'NV'),
    E('Neve 8068', 'Neve', '1977', 'Neve console of 1977.', 'NV'),
    E('Neve 8108', 'Neve', '1979', 'Neve console of 1979.', 'NV'),
    E('Neve 8028', 'Neve', '', 'Neve console named in the Neve article; year not stated.', 'NV'),
    E('Neve 8078', 'Neve', '', 'Neve console named in the Neve article; year not stated.', 'NV'),
    E('SSL B Series', 'Solid State Logic', '1976', 'SSL console of 1976.', 'SS'),
    E('SSL 4000', 'Solid State Logic', '1979', 'SSL console: E Series 1979, G Series 1987.', 'SS', v=[V('4000 E Series', 'Solid State Logic', '1979'), V('4000 G Series', 'Solid State Logic', '1987')]),
    E('SSL AWS 900', 'Solid State Logic', '2004', 'SSL analogue workstation system of late 2004; the AWS 900+ followed in 2006.', 'SS', v=[V('AWS 900+', 'Solid State Logic', '2006')]),
    E('SSL Duality', 'Solid State Logic', '2006', 'SSL console of late 2006.', 'SS'))
# ---------------- DJ --------------------
addv('DJ media player', 'Pioneer CDJ',
     V('CDJ-300', 'Pioneer', '1994'), V('CDJ-500S (CDJ-700S in the US)', 'Pioneer', '1997'), V('CDJ-800', 'Pioneer', '2002'), V('CDJ-200', 'Pioneer', '2004'),
     V('CDJ-800 MK2', 'Pioneer', '2006'), V('CDJ-400', 'Pioneer', '2007'), V('CDJ-850', 'Pioneer', '2010'), V('CDJ-350', 'Pioneer', '2010'),
     V('CDJ-900 NXS', 'Pioneer', '2013'), V('CDJ-1000 MK1', 'Pioneer', '2001'), V('CDJ-1000 MK2', 'Pioneer', '2003'), V('CDJ-3000X', 'AlphaTheta (Pioneer DJ)', '2025'), V('CDJ-1500X', 'AlphaTheta (Pioneer DJ)', '2026'),
     V('XDJ-1000 MK2', 'Pioneer'))
addv('DJ media player', 'Pioneer DJM',
     *[V(n, 'Pioneer') for n in ['DJM-300', 'DJM-350', 'DJM-400', 'DJM-450', 'DJM-600', 'DJM-700', 'DJM-750', 'DJM-707', 'DJM-850', 'DJM-900 Nexus', 'DJM-900 Nexus 2', 'DJM-V10', 'DJM-909', 'DJM-1000', 'DJM-2000', 'DJM-250', 'DJM-900SRT']])
add('DJ media player',
    E('Pioneer DMP-555', 'AlphaTheta (Pioneer DJ)', '2002', 'Pioneer media player listed in the CDJ article, April 2002.', 'CDJ'))
add('DJ controller', E('Korg Kaoss DJ', 'Korg', '2015', 'Korg DJ controller of 2015.', 'KO'))

# --- m -> conversion rules ---
# (kind, mname) -> ('v', entry, [name]) | ('drop', why) ; default entry
MR = {}
def vr(kind, parent, names, mk, y=''):
    for n in names: MR[(kind, n)] = ('v', parent, mk, y)
vr('Grand piano', 'Bösendorfer VC grands', ['280 VC', '230 VC', '214 VC', '185 VC', '170 VC', '225'], 'Bösendorfer')
vr('Grand piano', 'Fazioli F-series grands', ['F228', 'F212', 'F198', 'F183', 'F156'], 'Fazioli')
vr('Grand piano', 'C. Bechstein Concert grands', ['D 282', 'C 234', 'B 212', 'A 192', 'L 167', 'Model B-208 (interwar)', 'Academy A 228–A 160'], 'C. Bechstein')
MR[('Grand piano', 'Bösendorfer VC grands')] = ('e', 'Bösendorfer VC grands')
MR[('Grand piano', 'Fazioli smaller grands')] = ('e', 'Fazioli F-series grands')
MR[('Grand piano', 'C. Bechstein Concert grands')] = ('e', 'C. Bechstein Concert grands')
vr('Tonewheel organ', 'Hammond clonewheel line (XB/XK/SK)', ['Hammond XB-2 / XB-3 / XB-5', 'Hammond XK-3', 'Hammond XK-5', 'Hammond XK-1c', 'Hammond SK1', 'Hammond SK-X'], 'Hammond')
vr('Tonewheel organ', 'Nord Electro', ['Nord Electro 2', 'Nord Electro 3', 'Nord Electro 4', 'Nord Electro 5', 'Nord Electro 6'], 'Clavia')
MR[('Tonewheel organ', 'Nord Electro')] = ('e', 'Nord Electro')
vr('Electronic organ', 'Lowrey home organ', ['Model S Spinet (Berkshire)', 'Holiday Deluxe LSL', 'DSO-1 Heritage Deluxe', 'Kalamazoo K-101 / Gibson G-101', 'Genie', 'C500 Celebration', 'MicroGenie Pro V600', 'NT series (Holiday, Heritage, MX-2)'], 'Lowrey')
vr(DMK, 'Elektron Machinedrum', ['Machinedrum SPS-1'], 'Elektron')
MR[(DMK, 'Elektron Machinedrum lineage')] = ('e', 'Elektron Machinedrum')
vr(DMK, 'Elektron Analog Rytm', ['Analog Rytm MKII'], 'Elektron')
MR[(DMK, 'Analog Rytm')] = ('e', 'Elektron Analog Rytm')
MR[(DMK, 'Korg Volca rhythm units')] = ('drop', 'duplicate of Volca series in Groovebox')
MR[(DMK, 'Volca Beats')] = ('drop', 'now a version of Korg Volca series (Groovebox)')
MR[(DMK, 'Volca Drum')] = ('drop', 'now a version of Korg Volca series (Groovebox)')
MR[(DMK, 'Polyend Drums')] = ('e', 'Polyend Drums')
MR[('Frame drum', 'Hex-key mechanical tuning')] = ('drop', 'a tuning feature, not an instrument; attribute only')
MR[('Cymbal', 'China: Hubei C series china 8 in')] = ('drop', 'single size of a trade line; out of scope')
MR[('Cymbal', 'Zildjian traditional splash')] = ('drop', 'generic type, not a named line')
MR[('Cymbal', 'Paiste bell and cup chime')] = ('drop', 'generic type, not a named line')
for n, p in [('Effects and stack: 2002 Mega Bell', 'Paiste 2002'), ('Effects and stack: 2002 Cup Chime', 'Paiste 2002'), ('Effects and stack: 2002 Accent Cymbal', 'Paiste 2002'),
             ('Effects and stack: Signature Mega Cup Chime', 'Paiste Signature'), ('Effects and stack: Formula 602 Classic Heavy Bell 13 in', 'Paiste Formula 602')]:
    MR[('Cymbal', n)] = ('v', p, 'Paiste', '')
MR[('Xylophone', 'Concert xylophone, 3.5 octave')] = ('e', 'Marimba One concert xylophone')
MR[('Xylophone', 'Concert xylophone, 4.0 octave')] = ('v', 'Marimba One concert xylophone', 'Marimba One', '')
for n in ['Yamaha 6200 series timpani', 'Yamaha 7200 series timpani']: MR[('Timpani', n)] = ('v', 'Yamaha 4200 series timpani', 'Yamaha', '')
MR[('Timpani', 'Yamaha 4200 series timpani')] = ('e', 'Yamaha pedal timpani')
MR[('Timpani', 'Yamaha 6200 series timpani')] = ('v', 'Yamaha pedal timpani', 'Yamaha', '')
MR[('Timpani', 'Yamaha 7200 series timpani')] = ('v', 'Yamaha pedal timpani', 'Yamaha', '')
MR[('DJ controller', 'Pioneer DDJ')] = ('drop', 'range heading, kept as range DDJ')
MR[('Sampler', 'Roland P-6')] = ('e', 'Roland P-6')
RENAMES = {}
NAMEFIX = {'Zoom (audio)': 'Zoom', 'JBL (audio)': 'JBL', 'AlphaTheta (Pioneer DJ)': 'Pioneer DJ'}

def ename(name, mk):
    mk2 = NAMEFIX.get(mk, mk)
    if not mk2 or norm(name).startswith(norm(mk2)) or norm(mk2) in norm(name): return name
    return f'{mk2} {name}'

stats = {}
report_rows = []
used_brands = set()
OWN = {  # maker: (own, tier, cty, own_y) only where a fetched page states it
    'Steinway & Sons': ('Paulson & Co.', 'Independent', 'United States', '2013'),
    'Bösendorfer': ('Yamaha Corporation', 'Global group', 'Austria', '2008'),
    'Moog Music': ('inMusic', 'Independent', 'United States', '2023'),
    'Ludwig': ('Conn-Selmer', 'Independent', 'United States', '1981'),
    'Drum Workshop': ('Roland Corporation', 'Independent', 'United States', '2022'),
    'Paiste': ('Paiste AG', 'Independent', 'Switzerland', ''),
    'Roland': ('Roland Corporation', 'Global group', 'Japan', ''),
    'Yamaha': ('Yamaha Corporation', 'Global group', 'Japan', ''),
    'Shure': ('Shure', 'Independent', 'United States', ''),
    'Sabian': ('Sabian', 'Independent', 'Canada', ''),
}
SECT_UNKNOWN = 'Other and historical makers'

def finish_entry(e, extra_src=None):
    mk = e.get('mk', '')
    e['mk'] = mk
    if mk in OWN:
        o = OWN[mk]
        e['own'], e['tier'], e['cty'] = o[0], o[1], o[2]
        if o[3]: e['own_y'] = o[3]
    used_brands.add(mk)
    e['g'] = NAMEFIX.get(mk, mk) if mk else SECT_UNKNOWN
    for v in e.get('v', []): used_brands.add(v.get('mk', ''))
    return e

out_depts = []
for dep in src['depts']:
    if dep['n'] not in DEPTS: continue
    d2 = {k: v for k, v in dep.items() if k != 's'}
    d2['s'] = []
    allnames = {}
    for sh in dep['s']:
        for k in sh['k']:
            for e in k.get('x', []):
                allnames[norm(e['n'])] = 1
                for v in e.get('v', []): allnames[norm(v['n'])] = 1
    for sh in dep['s']:
        sh2 = {k: v for k, v in sh.items() if k != 'k'}
        sh2['k'] = []
        kinds = list(sh['k'])
        if dep['n'] == 'Recording & live sound' and sh['n'].startswith('Interfaces'):
            kinds.insert(2, dict(n=CON, a='studio console', d='Large mixing desk of a recording studio or broadcast room, built from channel strips and a master section.',
                                 s=U['SS'], tt=[['Signal path', ['Inline', 'Split']], ['Format', ['Analogue', 'Digital', 'Hybrid with workstation control']], ['Channel count', ['Small format', 'Large format']]]))
        for k in kinds:
            k2 = {a: b for a, b in k.items() if a not in ('m',)}
            xs = [copy.deepcopy(e) for e in k.get('x', [])]
            kn = k['n']
            by = {e['n']: e for e in xs}
            n_conv = n_ver = n_drop = 0
            # m conversion
            created = {}
            for mn, mk in k.get('m', []):
                rule = MR.get((kn, mn))
                if rule and rule[0] == 'drop':
                    n_drop += 1; report_rows.append((kn, mn, 'removed: ' + rule[1])); continue
                if rule and rule[0] == 'v':
                    pname = rule[1]
                    tgt = by.get(pname) or created.get(pname)
                    if tgt is None:
                        tgt = E(pname, rule[2], '', f'{pname}, a model line previously held as loose models.', k.get('s', ''))
                        created[pname] = tgt
                    tgt['v'].append(V(mn, mk or rule[2], rule[3], '')); n_ver += 1
                    report_rows.append((kn, mn, 'version of ' + pname)); continue
                nm = rule[1] if rule else ename(mn, mk)
                if norm(nm) in allnames or nm in created:
                    if nm in created: continue
                    report_rows.append((kn, mn, 'already an entry')); continue
                en = E(nm, mk, '', f'Current {kn.lower()} model from {NAMEFIX.get(mk, mk)}, listed on a retailer catalogue page.' if mk else f'{nm}, a maker or tradition named in the earlier list.', k.get('s', ''))
                created[nm] = en; n_conv += 1
                report_rows.append((kn, mn, 'entry ' + nm))
            for en in created.values():
                allnames[norm(en['n'])] = 1
                xs.append(en); by[en['n']] = en
            # new from references
            n_new = 0
            for en in NEW.get(kn, []):
                if norm(en['n']) in allnames: continue
                allnames[norm(en['n'])] = 1
                for v in en.get('v', []): allnames.setdefault(norm(v['n']), 1)
                xs.append(copy.deepcopy(en)); n_new += 1
            for (vk, vent), vs in VADD.items():
                if vk != kn: continue
                tgt = next((e for e in xs if e['n'] == vent), None)
                if tgt is None: continue
                have = {norm(v['n']) for v in tgt['v']}
                for v in vs:
                    if norm(v['n']) not in have:
                        tgt['v'].append(copy.deepcopy(v)); have.add(norm(v['n']))
            # dedupe versions by name inside entry
            for e in xs:
                seen = set(); vv = []
                for v in e.get('v', []):
                    key = norm(v['n']) + norm(v.get('y', ''))
                    if key in seen: continue
                    seen.add(key); vv.append(v)
                e['v'] = vv
                finish_entry(e)
            # order
            secs = sorted({e['g'] for e in xs}, key=lambda s: (s == SECT_UNKNOWN, s.lower()))
            xs.sort(key=lambda e: (secs.index(e['g']), yr(e['y']), e['n'].lower()))
            if xs:
                k2['x'] = xs
                refs = []
                if kn in NEW: refs = sorted({e['s'] for e in NEW[kn] if e['s'].startswith('http') and 'wikipedia' in e['s']})
                k2['nl'] = f'One entry is a named {kn.lower()} model or model line from one maker; revisions, reissues and sizes are versions.'
                refnames = [r.split('/')[-1].replace('_', ' ') for r in refs]
                cov = ''
                if kn in (MON, POL):
                    cov = f' Complete: 42 of 43 rows in Wikipedia "List of synthesizers" (ReBirth is software and belongs to I1); the Korg, Roland Jupiter, Moog, Sequential and Oberheim pages add the makers\' own lines.'
                elif kn == DMK:
                    cov = ' Complete: every hardware drum machine named in Wikipedia "Drum machine" (about 45); Korg rows come from the first 100,000 and last 39,084 characters of "List of Korg products" as condensed by the page summariser, so some Korg drum machines may be missing.'
                elif kn in ('Digital piano', 'Portable keyboard', 'Keytar', 'Sampler', 'Groovebox', 'Step sequencer', 'Tonewheel organ', 'Electric piano', 'Grand piano'):
                    cov = f' Covers {len(xs)} entries; the maker pages cited list only part of each canon and Wikipedia has no complete list of this kind.'
                elif dep['n'] == 'Recording & live sound':
                    cov = f' Covers {len(xs)} entries; the Neumann, Shure, Neve and SSL pages cite only part of each catalogue, and no AKG, Sennheiser, Electro-Voice or Universal Audio page was read.'
                elif dep['n'] == 'DJ equipment':
                    cov = f' Covers {len(xs)} entries; CDJ model years are complete in Wikipedia "CDJ" (31 models); the DJM page gives names without years.'
                elif dep['n'] == 'Drums & percussion':
                    cov = f' Covers {len(xs)} entries; the Pearl, Paiste, Ludwig, Tama and Drum Workshop pages name few lines and no Sabian, Zildjian, Gretsch, Sonor, Yamaha or Tama line page gave a list.'
                else:
                    cov = f' Covers {len(xs)} entries; no complete reference list exists for this kind.'
                k2['sel'] = ('Follows the existing hobby reference pages for each entry, with additions from ' + (', '.join(refnames) if refnames else 'no new page') + '; loose models were turned into entries or versions.' + cov)
                k2['xg'] = 'Sections are makers; within each, by year then name.'
            stats[kn] = (len(k.get('x', [])), len(xs), len(k.get('m', [])), n_conv, n_ver, n_drop, n_new)
            # ranges: drop those now covered
            if 'r' in k2:
                if kn in ('Grand piano', 'Upright piano', 'Pipe organ', 'Electronic organ', 'Conga', 'Bongos'):
                    k2.pop('r')
            sh2['k'].append(k2)
        d2['s'].append(sh2)
    out_depts.append(d2)

# department-level market summary
for d2 in out_depts:
    if d2['n'] == DEPTS[0]:
        d2['msum'] = 'Figures from the cited pages are company revenue and deal values, not market shares; no page read gave a share of the instrument market.'
        d2['ms'] = [
            {"mkt": "Musical instruments and audio, company revenue", "who": "Yamaha Corporation", "share": "¥462.08 billion", "yr": 2025, "s": U['YA'], "note": "revenue of the whole company as the page states, not a market share"},
            {"mkt": "Electronic instruments, company revenue", "who": "Roland Corporation", "share": "¥102.4 billion", "yr": 2023, "s": U['RO'], "note": "revenue of the whole company (about $668 million), not a market share"},
            {"mkt": "Concert and home pianos, ownership deal", "who": "Paulson & Co.", "share": "$512 million", "yr": 2013, "s": U['ST'], "note": "offer for Steinway Musical Instruments that beat a $438 million offer from Kohlberg & Company"},
        ]
    if d2['n'] == DEPTS[1]:
        d2['msum'] = 'No page read gave a drum or cymbal market share; ownership of the main kit and cymbal makers is shown on the entries.'
        d2['ms'] = []
    if d2['n'] == DEPTS[2]:
        d2['msum'] = 'The Shure page states no revenue; Shure is privately held. No page read gave a share of the microphone or console market.'
        d2['ms'] = []
    if d2['n'] == DEPTS[3]:
        d2['msum'] = 'No page read gave a DJ equipment market share.'
        d2['ms'] = []

brands = []
for mk in sorted(m for m in used_brands if m and m not in brands_reg):
    brands.append({"n": mk, "c": "", "f": "", "seg": "Specialist", "d": f"Maker named in the {mk} entries of the instrument canons.", "lines": [], "eras": [], "sig": [], "sc": [], "rel": [], "s": U['SM'], "kf": ""})
upd = {}
for mk, o in OWN.items():
    if mk in brands_reg: upd[mk] = {"own": o[0], "tier": o[1], "c": o[2]}
part = {"replaces": DEPTS, "depts": out_depts, "brands": brands, "brand_updates": upd, "renames": RENAMES, "moves": []}
json.dump(part, open(ROOT + 'out/E3_parts/KEYS.json', 'w'), ensure_ascii=False, indent=1)
json.dump({'stats': stats, 'rows': report_rows}, open(ROOT + 'work/V4_E3_KEYS/stats.json', 'w'), ensure_ascii=False, indent=1)
print(len(json.dumps(part)), 'bytes')
tot0 = sum(s[0] for s in stats.values()); tot1 = sum(s[1] for s in stats.values())
print('entries', tot0, '->', tot1, 'm items', sum(s[2] for s in stats.values()), 'conv', sum(s[3] for s in stats.values()), 'ver', sum(s[4] for s in stats.values()), 'drop', sum(s[5] for s in stats.values()), 'new', sum(s[6] for s in stats.values()))
