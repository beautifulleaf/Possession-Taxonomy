import json, os
W = 'https://en.wikipedia.org/wiki/'
def V(n, mk='', y='', d=''):
    o = {'n': n}
    if mk: o['mk'] = mk
    if y: o['y'] = y
    if d: o['d'] = d
    return o
def X(n, d, mk, y, s, v=(), a='', dt=''):
    o = {'n': n, 'a': a, 'd': d, 'mk': mk, 'y': y, 's': s, 'v': list(v)}
    if dt: o['dt'] = dt
    return o

H, M, P, B, R = 'Hasselblad', 'Mamiya', 'Pentax', 'Bronica', 'Rollei'

mf_slr = {
 'n': 'Medium-format SLR camera', 'a': 'medium-format reflex · 120 SLR',
 'd': 'Single-lens reflex system camera for 120/220 roll film, usually with interchangeable lenses, finders and film backs.',
 't': ['6×4.5 cm (645)', '6×6 cm', '6×7 cm'], 's': W + 'Medium_format',
 'x': [
  X('Hasselblad V system', 'Modular 6×6 SLR with interchangeable lenses, finders and film magazines; the 500-series bodies are the reference.', H, '1957', W + 'Hasselblad',
    [V('1600F', H, '1948/49', 'first Hasselblad focal-plane body'), V('1000F', H, '1953'), V('500C', H, '1957', 'leaf-shutter lenses; 1957–1970'),
     V('500EL', H, '1964', 'motorised EL series'), V('500C/M', H, '1970', '1970–1994'), V('2000 FC', H, '1977', 'focal-plane shutter'),
     V('503CX', H, '1988'), V('205 TCC', H, '1991'), V('201 F', H, '1994'), V('501C', H, '1994'), V('503CW', H, '1996', '1996–2013'),
     V('501CM', H, '1997'), V('555ELD', H, '1998'), V('SWC', H, '1959', 'Super Wide-angle series, 1959–1979')],
    a='Hasselblad 500 series', dt='body series C, CM, CW, EL, F · chrome or black · finders and magazines'),
  X('Pentax 6×7 / 67', 'Medium-format SLR shaped like an enlarged 35 mm SLR, giving 56 × 70 mm frames on 120 and 220 film.', P, '1969', W + 'Pentax_6%C3%977',
    [V('Asahi Pentax 6×7', P, '1969', 'first generation; Honeywell Pentax 6×7 in the US'), V('6×7 MLU', P, '1976', 'mirror lock-up'),
     V('Pentax 67', P, '1990', 'renamed, minor updates'), V('Pentax 67 II', P, '1999', 'fourth generation')],
    a='Pentax 67', dt='prism or waist-level finder · wooden grip'),
  X('Mamiya RB67', 'Mechanical 6×7 studio SLR with bellows focusing and a rotating back for portrait or landscape frames.', M, '1970', W + 'Mamiya_RB67',
    [V('RB67 Professional', M, '1970'), V('RB67 Pro-S', M, '1974'), V('RB67 Pro-SD', M, '1990')],
    dt='backs 6×7, 6×6, 6×4.5 · 120/220'),
  X('Mamiya RZ67', 'Electronic successor to the RB67, with lens shutters cocked and fired from the body and a lighter plastic exterior.', M, '1982', W + 'Mamiya_RZ67',
    [V('RZ67 Professional', M, '1982'), V('RZ67 Professional II', M, '1993', 'half-step shutter speeds'), V('RZ67 Professional IID', M, '2004')]),
  X('Bronica SQ', 'Modular 6×6 SLR system with leaf-shutter lenses, the lower-cost rival to the Hasselblad V system.', B, '1980', W + 'Bronica',
    [V('SQ', B, '1980'), V('SQ-A', B, '1982'), V('SQ-Ai', B, '1990'), V('SQ-B', B, '1996')]),
  X('Bronica ETR', 'Modular 6×4.5 SLR system with leaf-shutter lenses and interchangeable backs.', B, '1976', W + 'Bronica',
    [V('ETR', B, '1976'), V('ETRS', B, '1978'), V('ETRSi', B, '1988')]),
  X('Pentax 645', 'Handheld 6×4.5 SLR with a built-in motor drive, taking 120, 220 and 70 mm film.', P, '1984', W + 'Pentax_645',
    [V('645', P, '1984'), V('645N', P, '1997', 'autofocus, matrix metering'), V('645NII', P, '2001', 'mirror lock-up')]),
  X('Mamiya 645', 'Modular 6×4.5 SLR system from Mamiya, later with an autofocus line.', M, '1975', W + 'Mamiya',
    [V('M645', M, '1975'), V('645AF', M, '1999', 'autofocus')]),
  X('Rolleiflex SL66', '6×6 SLR with bellows focusing and lenses that tilt up to 8 degrees for Scheimpflug control.', R, '1966', W + 'Rolleiflex_SL66',
    [V('SL66', R, '1966'), V('SL66E', R, '1982', 'TTL metering and flash'), V('SL66X', R, '1982', 'TTL flash only'), V('SL66SE', R, '1982', 'spot and centre-weighted meter; to 1992')]),
  X('Bronica S series', 'Early focal-plane 6×6 Bronica SLRs.', B, '1961', W + 'Bronica',
    [V('S', B, '1961'), V('S2', B, '1965'), V('EC', B, '1972')]),
  X('Bronica GS-1', 'Modular 6×7 SLR system from Bronica.', B, '1983', W + 'Bronica', [V('GS-1', B, '1983', 'made to 2002')]),
 ]}

mf_rf = {
 'n': 'Medium-format rangefinder camera', 'a': 'medium-format RF · 120 rangefinder',
 'd': 'Rangefinder-focused camera for 120/220 roll film, with fixed or interchangeable lenses and no mirror.',
 't': ['6×4.5 cm (645)', '6×6 cm', '6×7 cm', '6×9 cm', 'Folding or rigid body'], 's': W + 'Medium_format',
 'x': [
  X('Mamiya 7', 'Interchangeable-lens 6×7 rangefinder with leaf-shutter lenses and frame lines for the lens fitted.', M, '1995', W + 'Mamiya_7',
    [V('Mamiya 7', M, '1995'), V('Mamiya 7 II', M, '1999', 'improved finder, multiple exposure')], dt='black or champagne · optional 35 mm panoramic adapter'),
  X('Mamiya 6', '6×6 rangefinder with a collapsing lens mount and built-in dark slide for lens changes mid-roll.', M, '1989', W + 'Mamiya_6',
    [V('Mamiya 6', M, '1989'), V('Mamiya 6 MF', M, '1993', '6×4.5 and panorama adapters')]),
  X('Plaubel Makina', 'Folding medium-format press rangefinder with a leaf shutter and collapsible bellows.', 'Plaubel', '1912', W + 'Plaubel_Makina',
    [V('Makina (German)', 'Plaubel', '1912', 'Plaubel & Co., Frankfurt, to 1953; Anticomar lens'), V('Makina 67', 'Plaubel', '', 'Japanese redesign from 1978, Nikkor 80 mm f/2.8'),
     V('Makina 670', 'Plaubel', '', 'Nikkor 80 mm f/2.8; 120 and 220'), V('Makina 69W Proshift', 'Plaubel', '', 'rigid wide-angle, 47 mm Super-Angulon')]),
  X('Fujifilm GW690 family', 'Large fixed-lens 6×9 and 6×7 rangefinders from Fujifilm.', 'Fujifilm', '', W + 'Fujifilm',
    [V('GW690', 'Fujifilm'), V('GW670', 'Fujifilm')]),
  X('Bronica RF645', 'Interchangeable-lens 6×4.5 rangefinder from Bronica.', B, '2000', W + 'Bronica', [V('RF645', B, '2000', 'made to 2005')]),
  X('Mamiya Press', 'Modular medium-format press camera with rangefinder and interchangeable lenses and backs.', M, '1962', W + 'Mamiya',
    [V('Mamiya Press', M, '1962'), V('Super / Universal', M, '', 'later Press-series bodies')]),
 ],
 'm': [['GA645', 'Fujifilm'], ['GF670', 'Fujifilm']]}

tlr_m = [['Yashica 44', 'Yashica'], ['Yashica 635', 'Yashica'], ['Ciro-flex', 'Ciro Cameras'], ['Argus 75', 'Argus'], ['Duaflex IV', 'Kodak'],
         ['Koniflex', 'Konica'], ['Gemflex', 'Showa Optica Works']]
tlr = {
 'n': 'Twin-lens reflex camera', 'a': 'TLR',
 'd': 'Film camera with two matched lenses, one for the waist-level viewing screen and one for taking the picture.',
 't': ['6×6 cm on 120', '4×4 cm on 127', 'Interchangeable-lens'], 's': 'https://kamerastore.com/en-us/products/rollei-rolleiflex-2-8f',
 'x': [
  X('Rolleiflex TLR', 'The 6×6 twin-lens reflex that set the pattern for mass-market TLRs from 1929.', R, '1929', W + 'Rolleiflex',
    [V('Original (K1)', R, '1929'), V('Standard', R, '1932'), V('Automat', R, '1937'), V('2.8E', R, '1956'), V('3.5F', R, '1958'),
     V('Tele Rolleiflex', R, '1959'), V('2.8F', R, '1960', 'Zeiss Planar or Schneider Xenotar 80 mm f/2.8; to 1981'), V('3.5T', R, '', 'from old data'),
     V('Wide Rolleiflex', R, '1961'), V('Baby Rolleiflex', R, '1931', '4×4 on 127; post-war 4×4 1957'), V('2.8GX', R, '1989'), V('2.8FX', R, '2002')],
    dt='Planar or Xenotar/Tessar or Xenar taking lens · with or without meter'),
  X('Rolleicord', 'Simpler, cheaper Rollei TLR for amateurs, made alongside the Rolleiflex.', R, '1933', W + 'Rolleicord',
    [V('Rolleicord I', R, '1933', 'Art Deco front'), V('Rolleicord III', R, '1950'), V('Rolleicord IV', R, '1953'), V('Rolleicord V', R, '1954'),
     V('Rolleicord Va', R, '1957'), V('Rolleicord Vb', R, '1962', 'last model, to 1977')]),
  X('Mamiya C series', 'Professional TLRs with truly interchangeable lens pairs and bellows focusing.', M, '1956', W + 'Mamiya',
    [V('Mamiyaflex C Professional', M, '1956'), V('C2', M, '1958'), V('C3', M, '1962'), V('C33', M, '1965'), V('C22', M, '1966'),
     V('C220', M, '1968'), V('C330', M, '1969'), V('C330f', M, '1975'), V('C220f', M, '1982'), V('C330s', M, '1983')]),
  X('Yashica-Mat', 'Affordable crank-advance 6×6 TLR on the Rolleiflex pattern.', 'Yashica', '1957', W + 'Yashica',
    [V('Yashicaflex', 'Yashica', '1953', 'earlier knob-wind line'), V('Yashica-Mat', 'Yashica', '1957'), V('Yashica-Mat 124', 'Yashica', '1968'),
     V('Yashica-Mat 124 G', 'Yashica', '1970')]),
  X('Voigtländer Superb', 'Early 6×6 TLR with parallax correction.', 'Voigtländer', '1933', W + 'Twin-lens_reflex_camera', [V('Superb', 'Voigtländer', '1933')]),
  X('Lubitel', 'Low-cost Soviet bakelite TLR for 120 film, based on the Voigtländer Brillant.', 'LOMO', '1950', W + 'Lubitel',
    [V('Lubitel', 'LOMO', '1950'), V('Lubitel-2', 'LOMO', '1955'), V('Lubitel-166', 'LOMO', '1977'), V('Lubitel-166 B', 'LOMO', '1980'),
     V('Lubitel-166 Universal', 'LOMO', '1984'), V('Lubitel-166+', 'Lomography', '2008', 'sold by the Lomographic Society')]),
 ],
 'm': tlr_m}

fold = {
 'n': 'Box or folding camera', 'a': 'box camera · folding camera · folder',
 'd': 'Simple box-shaped camera, or one with a folding bellows body, mostly for roll film.',
 't': ['Box camera', 'Folding roll-film camera', 'Folding 35 mm camera', 'With coupled rangefinder'],
 's': 'https://kamerastore.com/en-us/products/zeiss-ikon-nettar-518-16',
 'x': [
  X('Kodak Brownie', 'Cheap cardboard and later metal or plastic box cameras that brought roll-film photography to everyone.', 'Kodak', '1900', W + 'Brownie_(camera)',
    [V('Brownie', 'Kodak', '1900', 'original cardboard box'), V('Brownie No. 2', 'Kodak', '1901', 'to 1935'), V('Six-20 Flash Brownie', 'Kodak', '1940'),
     V('Brownie Hawkeye Flash Model', 'Kodak', '1950', 'to 1961')]),
  X('Zeiss Ikon Ikonta', 'Self-erecting folding roll-film cameras in several frame sizes; the Super Ikonta adds a coupled rangefinder.', 'Zeiss Ikon', '1929',
    'https://phsne.org/the-ikonta-521-16its-predecessor-and-successors/',
    [V('Ikonta 520', 'Zeiss Ikon', '1929', 'variants A–D by frame size'), V('Ikonta 520/16', 'Zeiss Ikon', '1938', '6×6'),
     V('Ikonta 521/16', 'Zeiss Ikon', '1948', '6×6 on 120; to 1953'), V('Super Ikonta', 'Zeiss Ikon', '', 'coupled rangefinder')]),
  X('Zeiss Ikon Nettar', 'Simpler, cheaper Zeiss Ikon folding camera for 120 film.', 'Zeiss Ikon', '1949', 'https://kamerastore.com/en-us/products/zeiss-ikon-nettar-518-16',
    [V('Nettar 518/16', 'Zeiss Ikon', '1949', 'from old data')]),
  X('Zeiss Ikon Box-Tengor', 'Zeiss Ikon roll-film box camera derived from an earlier Goerz design.', 'Zeiss Ikon', 'c. 1932', W + 'Zeiss_Ikon',
    [V('Box Tengor Model 54', 'Zeiss Ikon', 'c. 1932')]),
  X('Kodak Retina (folding)', 'Compact folding 35 mm cameras from Kodak AG in Stuttgart, later with coupled rangefinders.', 'Kodak', '1934', W + 'Kodak_Retina',
    [V('Retina (Nr. 117)', 'Kodak', '1934', 'original'), V('Retina II', 'Kodak', '1936', 'coupled rangefinder'), V('Retina IIa', 'Kodak', '1939'),
     V('Retina IIIc', 'Kodak', '1954'), V('Retina IIIC', 'Kodak', '1957')]),
  X('Voigtländer Bessa', 'Voigtländer folding roll-film camera line, revived as the 6×6/6×7 Bessa III.', 'Voigtländer', '', W + 'Voigtl%C3%A4nder',
    [V('Bessa III', 'Voigtländer', '', 'Cosina-made, 6×6 or 6×7 on 120/220')]),
 ],
 'm': [['Panda', 'Ansco'], ['Midget model 22', 'Ensign'], ['Pocket Kodak', 'Kodak'], ['Model 203', 'Seagull Camera']]}

view = {
 'n': 'View camera', 'a': 'large-format camera · technical camera',
 'd': 'Large-format camera with bellows, ground-glass focusing and lens movements, for sheet film.',
 't': ['Monorail', 'Field (flatbed)', 'Press camera', '4×5 in', '5×7 in', '8×10 in'],
 's': 'https://kamerastore.com/en-gb/products/chamonix-45h-1-large-format',
 'x': [
  X('Linhof Technika', 'All-metal folding field camera with lens movements and a coupled rangefinder, still in production.', 'Linhof', '1934', W + 'Linhof',
    [V('Technika', 'Linhof', '1934', 'first all-metal folding field camera'), V('Master Technika Classic', 'Linhof'), V('Master Technika 2000', 'Linhof'),
     V('Master Technika 3000', 'Linhof')]),
  X('Sinar monorail system', 'Modular studio monorail view camera system from Zürich.', 'Sinar', '1947', W + 'Sinar_AG',
    [V('Norma', 'Sinar', '1947', 'to 1969'), V('Sinar P', 'Sinar', '1970'), V('Sinar F', 'Sinar', '', 'lightweight field series'),
     V('Sinar X', 'Sinar', '', 'lower-cost alternative to P2'), V('P2 / F2', 'Sinar', '1980s')]),
  X('Graflex Speed Graphic', 'American press camera with focal-plane and lens shutters, the standard news camera for decades.', 'Graflex', '1912', W + 'Speed_Graphic',
    [V('Anniversary Speed Graphic', 'Graflex', '1940'), V('Pacemaker Speed Graphic', 'Graflex', '1947', 'to 1970'),
     V('Pacemaker Crown Graphic', 'Graflex', '1947', 'no focal-plane shutter; to 1973')], dt='3¼×4¼ or 4×5 in'),
  X('Linhof Technikardan', 'Linhof folding monorail camera for field and studio.', 'Linhof', '', W + 'Linhof',
    [V('Technikardan 45', 'Linhof'), V('Technikardan 45S', 'Linhof'), V('Technikardan 23', 'Linhof'), V('Technikardan 23S', 'Linhof')]),
  X('Chamonix field camera', 'Modern wood-and-metal 4×5 folding field camera.', 'Chamonix', '', 'https://kamerastore.com/en-gb/products/chamonix-45h-1-large-format',
    [V('45H-1', 'Chamonix', '', 'teak or cherry')]),
  X('Intrepid', 'Lightweight, low-cost field camera hand-assembled in Brighton.', 'Intrepid', '', 'https://intrepidcamera.co.uk/',
    [V('Intrepid 4x5', 'Intrepid'), V('Intrepid 5x7', 'Intrepid'), V('Intrepid 8x10', 'Intrepid'), V('Black Edition', 'Intrepid'), V('Hardwood Edition', 'Intrepid')]),
 ],
 'm': [['Taro-Tenax 9x12', 'Goerz']]}

pano = {
 'n': 'Panoramic film camera', 'a': 'panoramic camera',
 'd': 'Film camera that exposes a wide panoramic frame, by a swinging lens, a rotating body or a wide fixed lens.',
 't': ['Swing-lens', 'Full-rotation', 'Fixed-lens (flatback)'], 's': 'https://www.keh.com/shop/cameras/film-cameras/35mm.html',
 'x': [
  X('Hasselblad XPan', 'Interchangeable-lens 35 mm rangefinder that switches between standard and panoramic frames.', H, '1998', W + 'Hasselblad_XPan',
    [V('XPan', H, '1998', 'rebadged Fujifilm TX-1'), V('XPan II', H, '2003', 'rebadged Fujifilm TX-2')]),
  X('Widelux', 'Fully mechanical swing-lens panoramic camera.', 'Panon Camera Shoko', '1958', W + 'Widelux',
    [V('F6', 'Panon Camera Shoko', 'c. 1970'), V('F7', 'Panon Camera Shoko', '1979'), V('F8', 'Panon Camera Shoko', '1988'),
     V('1500', 'Panon Camera Shoko', '1988', '50×122 mm on 120')]),
  X('Horizon', 'Russian swing-lens 35 mm panoramic camera covering 120 degrees on 24×58 mm frames.', 'KMZ', '1966', W + 'Horizon_(camera)',
    [V('FT-2', 'KMZ', '1958', 'predecessor'), V('Horizont', 'KMZ', '1966'), V('Horizon 202', 'KMZ', '1989', 'plastic body'),
     V('Horizon S3Pro', 'KMZ', '2003'), V('Horizon Perfekt', 'KMZ', '2005', 'sold with Lomography')]),
  X('Noblex', 'German motor-driven swing-lens panoramic camera made for several film formats.', 'Kamera-Werkstätten', '', W + 'Noblex_camera', []),
  X('Fuji G617', 'Fixed-lens 6×17 cm panoramic camera for 120 film.', 'Fujifilm', '', W + 'Panoramic_photography',
    [V('G617', 'Fujifilm'), V('GX617', 'Fujifilm', '', 'interchangeable lenses')]),
  X('Seitz Roundshot', 'Full-rotation panoramic camera capable of 360-degree exposures.', 'Seitz', '1988', W + 'Panoramic_photography', []),
  X('Lomography Spinner 360°', 'Hand-spun full-rotation 35 mm panoramic camera.', 'Lomography', '2010', W + 'Panoramic_photography', []),
 ],
 'm': [['Technorama 617', 'Linhof'], ['612PC', 'Linhof'], ['SW612', 'Horseman'], ['Art Panorama 617', 'Tomiyama']]}

def Bd(n, c, f, seg, d, s, sig=(), lines=(), rel=()):
    o = {'n': n, 'c': c, 'f': f, 'seg': seg, 'd': d, 's': s}
    if sig: o['sig'] = list(sig)
    if lines: o['lines'] = list(lines)
    if rel: o['rel'] = list(rel)
    return o
K = 'knowledge'
brands = [
 Bd(H, 'Sweden', '1941', 'Medium-format cameras', 'Gothenburg maker of medium-format cameras, famed for the V system and its use on the Apollo missions.', W + 'Hasselblad',
    ['Hasselblad V system', 'Hasselblad XPan'], ['V system (500 series)', 'XPan'], ['Fujifilm']),
 Bd(M, 'Japan', '1940', 'Medium-format cameras', 'Japanese maker of professional medium-format SLRs, TLRs and rangefinders.', W + 'Mamiya',
    ['Mamiya RB67', 'Mamiya RZ67', 'Mamiya 7', 'Mamiya C series'], ['RB67', 'RZ67', '645', 'C series', '6', '7', 'Press']),
 Bd(P, 'Japan', '1919', 'Cameras', 'Japanese camera maker (Asahi Optical) whose medium-format line comprised the 6×7/67 and 645.', K, ['Pentax 6×7 / 67', 'Pentax 645']),
 Bd(B, 'Japan', '', 'Medium-format cameras', 'Tokyo maker of modular medium-format SLR systems, later owned by Tamron.', W + 'Bronica',
    ['Bronica SQ', 'Bronica ETR', 'Bronica RF645'], ['S', 'ETR', 'SQ', 'GS-1', 'RF645'], [H]),
 Bd(R, 'Germany', '1920', 'Cameras', 'Braunschweig maker (Franke & Heidecke) of the Rolleiflex and Rolleicord TLRs.', W + 'Rolleiflex',
    ['Rolleiflex TLR', 'Rolleicord', 'Rolleiflex SL66'], ['Rolleiflex', 'Rolleicord', 'SL66']),
 Bd('Fujifilm', 'Japan', '1934', 'Imaging and film', 'Japanese film and camera maker; its professional film cameras include the GW690 family and G617.', W + 'Fujifilm',
    ['Fujifilm GW690 family', 'Fuji G617'], rel=[H]),
 Bd('Plaubel', 'Germany', '', 'Cameras', 'Frankfurt camera maker of the Makina folding press cameras; the name later passed to Japanese owners.', W + 'Plaubel_Makina', ['Plaubel Makina']),
 Bd('Yashica', 'Japan', '1949', 'Cameras', 'Japanese camera maker known for affordable TLRs such as the Yashica-Mat.', W + 'Yashica', ['Yashica-Mat']),
 Bd('LOMO', 'Russia', '1914', 'Cameras and optics', 'St Petersburg optical works that made the Lubitel TLRs.', K, ['Lubitel'], rel=['Lomography']),
 Bd('Lomography', 'Austria', '1992', 'Analogue cameras', 'Vienna-based analogue photography company selling revived and new film cameras.', K,
    ['Lomography Spinner 360°'], rel=['LOMO', 'KMZ']),
 Bd('Zeiss Ikon', 'Germany', '1926', 'Cameras', 'Dresden camera maker formed by merger in 1926; makers of the Ikonta, Nettar and Box-Tengor.', W + 'Zeiss_Ikon',
    ['Zeiss Ikon Ikonta', 'Zeiss Ikon Nettar', 'Zeiss Ikon Box-Tengor']),
 Bd('Voigtländer', 'Austria', '1756', 'Cameras and optics', 'Optical firm founded in Vienna, maker of the Bessa folders and Superb TLR.', W + 'Voigtl%C3%A4nder',
    ['Voigtländer Bessa', 'Voigtländer Superb']),
 Bd('Kodak', 'United States', '1888', 'Film and cameras', 'Rochester film and camera company behind the Brownie and, through Kodak AG, the Retina.', K,
    ['Kodak Brownie', 'Kodak Retina (folding)']),
 Bd('Linhof', 'Germany', '1887', 'Large-format cameras', 'Munich maker of technical and view cameras, founded by Valentin Linhof.', W + 'Linhof',
    ['Linhof Technika', 'Linhof Technikardan']),
 Bd('Sinar', 'Switzerland', '1948', 'Large-format cameras', 'Zürich maker of modular monorail view cameras, founded by Carl Hans.', W + 'Sinar_AG', ['Sinar monorail system']),
 Bd('Graflex', 'United States', '', 'Press cameras', 'Rochester maker of the Speed Graphic and Crown Graphic press cameras, dissolved in 1973.', W + 'Speed_Graphic', ['Graflex Speed Graphic']),
 Bd('Chamonix', 'China', '', 'Large-format cameras', 'Maker of wood-and-metal large-format field cameras.', K, ['Chamonix field camera']),
 Bd('Intrepid', 'United Kingdom', '', 'Large-format cameras', 'Brighton maker of lightweight, low-cost large-format field cameras.', 'https://intrepidcamera.co.uk/', ['Intrepid']),
 Bd('Panon Camera Shoko', 'Japan', '', 'Panoramic cameras', 'Japanese maker of the Widelux swing-lens panoramic cameras.', W + 'Widelux', ['Widelux']),
 Bd('KMZ', 'Russia', '1942', 'Cameras and optics', 'Krasnogorsk mechanical works, maker of the Horizon swing-lens panoramic cameras.', W + 'Horizon_(camera)', ['Horizon'], rel=['Lomography']),
 Bd('Kamera-Werkstätten', 'Germany', '', 'Panoramic cameras', 'German maker of the Noblex motor-driven panoramic cameras.', W + 'Noblex_camera', ['Noblex']),
 Bd('Seitz', 'Switzerland', '', 'Panoramic cameras', 'Swiss maker of the Roundshot rotating panoramic cameras.', K, ['Seitz Roundshot']),
]
notes = ("All six planned kinds kept; old models folded into archetype versions (Rolleiflex, Rolleicord, Mamiya C, Lubitel, Nettar, Bessa III, Technika, Sinar F, Chamonix 45H-1). "
 "Old flat models Superb, Retina, Box-Tengor and old ranges Brownie, Nettar, Rolleiflex, Mamiya C, Chamonix H/F, Technika, Sinar F became archetypes or versions. Models handed over from shelf 01_00 are included: Bronica RF645 and Mamiya 6 / 7 / 7 II (rangefinder archetypes), Hasselblad XPan / XPan II (panoramic archetype). "
 "Planned rangefinder models 'from k17' were not supplied in the brief, so only Fujifilm GA645 and GF670 (named on the Fujifilm page) sit in m. "
 "Not added for lack of a retrieved page with details: Fuji GSW690 and G690 versions, Hasselblad SWC as its own archetype (kept as a V-system version), Kodak Cirkut (maker not on page), Deardorff, Toyo, Wista, Ebony, Shen Hao, Agfa Isolette, Mamiya Six, Minolta Autocord. "
 "Some years omitted where pages gave none (Makina 67/670, Sinar F/X, Technikardan). Brand facts from knowledge: Pentax, LOMO, Lomography, Kodak, Chamonix country, Seitz; founding years for Hasselblad, Mamiya, Rollei, Fujifilm, Yashica, KMZ also from knowledge. No traditions: industrial products.")
out = {'kinds': [mf_slr, mf_rf, tlr, fold, view, pano], 'brands': brands, 'traditions': [], 'notes': notes}
p = 'work/D4/shelves/01_01.json'; tmp = p + '.tmp'
json.dump(out, open(tmp, 'w'), ensure_ascii=False, indent=1); os.replace(tmp, p)
print('written', os.path.getsize(p))
