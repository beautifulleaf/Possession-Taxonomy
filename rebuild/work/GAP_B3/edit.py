import json,os,re
P='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(P+'B3.json'))
LT='https://www.lightology.com/index.php?module=how_to&sub=italian-lighting-design-history'
def E(n,dd,mk,y,s,g,a='',v=None):
    return {"n":n,"a":a,"d":dd,"mk":mk,"y":y,"s":s,"v":v or [],"g":g}
new={
'Desk lamp':[
 E("548","Desk lamp by Gino Sarfatti for Arteluce, listed in the Lightology Italian lighting classics.","Arteluce","1951",LT,"1950s"),
 E("Samurai","Desk lamp by Shigeaki Asahara for Stilnovo, listed in the Lightology Italian lighting classics.","Stilnovo","1970",LT,"1970s")],
'Table lamp':[
 E("E63","Table lamp by Umberto Riva for Bieffeplast and FontanaArte, listed in the Lightology Italian lighting classics.","Bieffeplast","1963",LT,"1960s"),
 E("KD 27","Table lamp by Joe Colombo for Kartell, listed in the Lightology Italian lighting classics.","Kartell","1968",LT,"1960s"),
 E("602","Lamp by Cini Boeri for Arteluce with a pivoting PVC body on a lacquered metal base; Galerie kreo calls it a table light and notes it is out of production.","Arteluce","1968","https://www.galeriekreo.com/en/piece/cini-boeri/602","1960s",v=[{"n":"Boijmans record","mk":"Arteluce","y":"1968","d":"held by Museum Boijmans Van Beuningen (https://www.boijmans.nl/en/collection/artworks/108735/602)"}]),
 E("Flash","Table lamp by Joe Colombo for Oluce, model 2207; the Flash name also covers floor, wall and ceiling versions of the same system.","Oluce","1968","https://www.1stdibs.com/furniture/lighting/table-lamps/joe-colombo-table-lamp-2207-flash-italy-1968/id-f_14587711","1960s"),
 E("Tokio","Table lamp by Shigea Asahara for Stilnovo, listed in the Lightology Italian lighting classics.","Stilnovo","1980",LT,"1980s"),
 E("Ziggurat","Table lamp by Shigea Asahara for Stilnovo, listed in the Lightology Italian lighting classics.","Stilnovo","1980",LT,"1980s"),
 E("Nastro","Table lamp by Alberto Fraser for Stilnovo, listed in the Lightology Italian lighting classics.","Stilnovo","1985",LT,"1980s"),
 E("Aggregato","Adjustable table lamp by Enzo Mari with Giancarlo Fassina for Artemide, with a plexiglass shade; Lightology dates it 1976.","Artemide","1976","https://curiouz.com/products/aggregate-table-lamp-by-enzo-mari-and-giancarlo-fassina-for-artemide","1970s"),
 E("Anima","Lamp by Davide Groppi and Giorgio Rava that won the 2024 Compasso d'Oro; the ADI Design Museum lists it as a lighting device without giving a type.","Davide Groppi","","https://www.adidesignmuseum.org/en/collection/anima-lamp/","2020s"),
 E("Biga","Multifunctional lamp by Studio Marco Zito for Lym combining bedside table, light, connectivity and charging; 2024 Compasso d'Oro winner.","Lym","","https://www.adidesignmuseum.org/en/collection/biga-lamp/","2020s")],
'Floor lamp':[
 E("1047","Floor lamp by Vittoriano Viganò for Arteluce with an adjustable black aluminium shade on a brass stem and tripod base.","Arteluce","c. 1951","https://www.1stdibs.com/furniture/lighting/floor-lamps/vittoriano-vigano-arteluce-rare-floor-lamp-model-1047/id-f_13749432","1950s")],
'Wall light':[
 E("237","Wall light by Gino Sarfatti for Arteluce, listed in the Lightology Italian lighting classics.","Arteluce","1960",LT,"1960s"),
 E("265","Wall light by Paolo Rizzatto, listed in the Lightology Italian lighting classics; the page names no maker.","","1973",LT,"1970s")],
'Pendant light':[
 E("Hope","Pendant lamp by Francisco Gomez Paz and Paolo Rizzatto for Luceplan using thin plastic Fresnel lenses; Compasso d'Oro 2011.","Luceplan","2009","https://www.adidesignmuseum.org/en/collection/hope-suspension-lamp/","2000s",v=[{"n":"Lightology listing","mk":"Luceplan","y":"2009","d":"dated 2009 on the Lightology Italian lighting classics page"}])],
}
cnt=0
for dp in d['depts']:
  for sh in dp['s']:
    for k in sh['k']:
      if k['n'] in new:
        have={e['n'].lower() for e in k['x']}
        for e in new[k['n']]:
          if e['n'].lower() not in have:
            k['x'].append(e); cnt+=1
      # LIFX
      for e in k.get('x',[]):
        if e['n']=='LIFX':
          e['d']="Wi-Fi smart bulb brand that needs no bridge; Feit Electric bought the LIFX assets from Lifi Labs, Inc. in August 2022."
          e['own']="Feit Electric"; e['own_y']="2022"; e['g']=e.get('g') or "2010s"
          e['s']="https://homekitnews.com/?p=32930"
def order(k):
    gl=[]
    for e in k['x']:
        if e['g'] not in gl: gl.append(e['g'])
    return gl
print('added',cnt)
# coverage lines
DES=("Complete lists were read for every reference that could be fetched: MoMA Design classification search \"lamp\" (191 of 191 results), the Vitra Design Museum online collection (28 of 28 lamp results), the V&A lamp records from 1900 (all six pages of the museum's search read; about 80 lamp records of 97 usable, the rest untitled, stage-design, poster or non-lamp), and the Lightology Italian lighting classics (41 of 41 lamps; type taken from the page where stated, from other fetched pages otherwise). "
 "Covers these four references in full and the Compasso d'Oro lighting winners found on fetched ADI Design Museum, Casa di Luce, Luceplan and fuorisalone pages, of about 300 museum and award lamps in all; the full ADI winners list is not served in a fetchable form, and MoMA's Product design and Furniture classifications and the Design Museum London's own catalogue could not be fetched.")
for dp in d['depts']:
  for sh in dp['s']:
    for k in sh['k']:
      if not k.get('x'): continue
      n=k['n']; s=k['sel']
      if s.startswith('Follows design collections'):
          i=s.index(' Covers 191')
          k['sel']=s[:i].rstrip()+' '+DES
          # fix wording duplication
          k['sel']=k['sel'].replace('Complete lists were read for every reference that could be fetched:','Reference readings:')
      elif n in('Lava lamp','Plasma lamp','Light panel'):
          k['sel']=s.replace(' No whole-space reference exists; lines not on those pages are not covered.','')+' No complete list exists; follows the overviews named here.'
      elif 'Commodity kind: keeps only the lines' in s:
          k['sel']=s+' Torch makers beyond these (for example Nitecore TINI, Fenix, Streamlight Stylus, Sofirn) are commodity lines with no fetched defining page and stay out of scope. No complete list exists; follows the Wikipedia overviews.'
      elif s.startswith('Historic and heritage lantern'):
          k['sel']=s.replace(' Covers the types on those pages; no whole-space reference exists.','')+' No complete list exists; follows the Wikipedia overviews named here.'
      elif s.startswith('Commodity kind: keeps only origin products'):
          k['sel']=s.replace(' Covers the first 100,000 characters of each lamp page; LIFX is listed from a 9to5mac article because the Wikipedia page returned 404.',' LIFX is listed from a HomeKit News report of its August 2022 sale to Feit Electric.')+' No complete list exists; follows the Wikipedia lamp overviews named here.'
for dp in d['depts']:
  for sh in dp['s']:
    for k in sh['k']:
      if k.get('x'):
        k['x'].sort(key=lambda e:(order_key(e) if False else 0))
# sort x by group then year then name
def gk(g):
    m=re.match(r'(\d{4})s',g); return (0,int(m.group(1))) if m else (1,0)
def yk(y):
    m=re.search(r'\d{4}',y or ''); return int(m.group()) if m else 9999
for dp in d['depts']:
  for sh in dp['s']:
    for k in sh['k']:
      if k.get('x'):
        k['x'].sort(key=lambda e:(gk(e['g']),yk(e['y']),e['n'].lower()))
os.makedirs(P+'.tmp',exist_ok=True) if False else None
json.dump(d,open(P+'B3.json.tmp','w'),ensure_ascii=False,indent=1)
os.replace(P+'B3.json.tmp',P+'B3.json')
# brands
bp=P+'B3_brands.json'; B=json.load(open(bp))
bl={b['n']:b for b in B['b']}
def add(n,c,seg,dd,s,f=''):
    if n not in bl:
        x={"n":n,"c":c,"seg":seg,"d":dd,"lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":s,"kf":"design lighting"}
        if f: x['f']=f
        B['b'].append(x)
add("Luceplan","Italy","Premium","Italian design-lighting maker of Hope, designed by Francisco Gomez Paz and Paolo Rizzatto.","https://www.adidesignmuseum.org/en/collection/hope-suspension-lamp/")
add("Davide Groppi","Italy","Premium","Italian design-lighting maker of the Anima lamp, a 2024 Compasso d'Oro winner.","https://www.adidesignmuseum.org/en/collection/anima-lamp/")
add("Lym","Italy","Premium","Italian lighting company that produces the Biga lamp, a 2024 Compasso d'Oro winner.","https://www.adidesignmuseum.org/en/collection/biga-lamp/")
add("Bieffeplast","Italy","Premium","Italian producer of the E63 table lamp by Umberto Riva, with FontanaArte, per Lightology.",LT)
add("FontanaArte","Italy","Premium","Italian lighting maker of the Bilia and E63 lamps, per Lightology.",LT)
for b in B['b']:
    if b['n'] in('Flos','Louis Poulsen') and 'Design Holding' not in b['d']:
        b['d']=b['d'].rstrip('.')+'; owned by Design Holding, jointly controlled by Investindustrial and The Carlyle Group (formed November 2018).'
        b['s']=b.get('s') or 'https://edisonreport.com/?p=18742'
    if b['n']=='Artemide':
        b['d']="Milan design-lighting maker founded in 1960 by Ernesto Gismondi and Sergio Mazza; privately held."
        b['s']='https://en.wikipedia.org/wiki/Artemide'
    if b['n']=='Louis Poulsen': b['f']='1874'
    if b['n']=='LIFX':
        b['d']="Wi-Fi smart bulb brand; Feit Electric bought the LIFX assets from Lifi Labs, Inc. in August 2022."
        b['s']='https://homekitnews.com/?p=32930'
json.dump(B,open(bp+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(bp+'.tmp',bp)
