import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/GAP_E6')
from common import *
d=load(); W='https://en.wikipedia.org/wiki/'
def add(k,items):
    k.setdefault('x',[])
    have={e['n'].lower() for e in k['x']}
    for e in items:
        if e['n'].lower() not in have: k['x'].append(e)
k=find(d,'Monocular'); S=W+'Monocular'
M=[('Leica Monovid 8×20','Leica','Compact 8× monocular supplied with a close-up lens.'),
('Opticron 8×42 DBA','Opticron','Top-specification 8× monocular with very long eye relief.'),
('Opticron 10×42 BGA','Opticron','10× monocular in the BGA line.'),
('Opticron 8×32 LE','Opticron','Compact 8× monocular.'),
('Opticron 4×12G gallery scope','Opticron','Low-power gallery scope with a wide field of view.'),
('Opticron Trailfinder 8×25','Opticron','Compact 8× monocular with a quick-focus lever.'),
('Zeiss Mono 8×20','Carl Zeiss','Compact 8× monocular.'),
('Carl Zeiss Jena Turmon 8×21','Carl Zeiss Jena','Folding monocular.'),
('Bushnell Legend 10×42 Ultra HD','Bushnell','10× monocular with a quick-focus wheel.'),
('Asika 8×42','Asika','8× monocular with a top quick-focus wheel.'),
('Eschenbach 6×16','Eschenbach Optik','Compact monocular with a sliding focus button.'),
('Minox 8×25 Macroscope','Minox','Monocular focused by a knurled ring around the objective.'),
('Minox 8×16 series','Minox','Ultra-compact monocular series with a slider focus button.'),
('Carson Bandit 8×25','Carson Optical','Quick-focus monocular with a toggle focus.'),
('Vortex Solo','Vortex Optics','Monocular reviewed as an example of twist focus.'),
('Seago 8×42 compass monocular','Seago','Monocular with a built-in compass.'),
('Bresser 16×30 image-stabilised monocular','Bresser','Monocular with built-in image stabilisation.'),
('Red Army monocular 2.5×17.5','Soviet Union','Miniature Galilean-type monocular.')]
add(k,[ent(n,t,mk=mk,s=S,g='Maker lines') for n,mk,t in M])
k['sel']='Named monoculars in the Wikipedia article Monocular (the article lists 24; novelty items such as the Sony radio monocular, the Specwell microscope converter and the Luger MD are left out) with lines of the earlier pass.'
k=find(d,'Spotting scope'); S=W+'Spotting_scope'
add(k,[ent('Straight-through spotting scope','Eyepiece on the same axis as the scope body.',s=S,g='Eyepiece layouts'),ent('Angled spotting scope','Eyepiece at an angle to the body, usually 45 degrees.',s=S,g='Eyepiece layouts')])
k['x'].sort(key=lambda e:0 if e['g']=='Eyepiece layouts' else 1)
k['xg']='eyepiece layout, then maker lines'
k['sel']='Eyepiece layouts from the Wikipedia article Spotting scope (it lists no models), then maker lines of the earlier pass; no whole-space reference exists.'
k=find(d,'Stevenson screen'); S=W+'Stevenson_screen'
k['x']=[ent('Stevenson screen','Small thermometer screen with double-louvred walls and no floor, developed by Thomas Stevenson.',mk='Thomas Stevenson',y='1864',s=S,g='Designs',role='origin'),
 ent('Mawley modification','Stevenson-type screen with a double roof and slanted-board floor, adopted by the British Meteorological Office.',mk='Edward Mawley',y='1884',s=S,g='Designs'),
 ent('Cotton region shelter','US national-service screen variant with single louvres.',s=S,g='Designs')]
k['nl']='One entry is an instrument-shelter design named in the Wikipedia article Stevenson screen.'
k['sel']='Complete: 3 of 3 shelter designs named in the Wikipedia article Stevenson screen.'
k=find(d,'Barlow lens'); S=W+'Barlow_lens'
add(k,[ent('Barlow lens','Diverging lens unit that increases effective focal length; named after Peter Barlow, the standard 2× or 3× astronomical form.',mk='Peter Barlow',s=S,g='Designs'),
 ent('Adjustable Barlow','Barlow whose power is changed by adding an extension tube between it and the eyepiece.',s=S,g='Designs')])
for e in k['x']:
    if e.get('g')!='Designs': e['g']='Maker lines'
k['x'].sort(key=lambda e:0 if e['g']=='Designs' else 1)
k['xg']='design, then maker lines'
save(d)
