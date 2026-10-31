import json,copy,re,sys
sys.path.insert(0,'.')
import adds
from adds import A,_mv
from data import *
_mv('Boss TW-1 T Wah','Tremolo and vibe pedal','Wah pedal')
old=json.load(open('../../out/E3.json'))
names={'Guitars & basses','Guitar & bass parts','Amps & effects'}
depts=[copy.deepcopy(d) for d in old['depts'] if d['n'] in names]
def norm(s): return re.sub(r'[^a-z0-9]+',' ',s.lower()).strip()
def ystart(y):
    m=re.search(r'\d{4}',y or ''); return int(m.group()) if m else 9999
removed=[];unk=set();stats={}
SEL={
'Solid-body electric guitar':('One entry is a solid-body electric guitar model or series sold under its own name; signature, reissue and import versions sit under it.',
 "Wikipedia's lists of Gibson and Fender products (solid-body rows), the model sections of the Ibanez, ESP, Jackson, Epiphone, Gretsch, Rickenbacker and Martin articles, Yamaha's Pacifica history and Premier Guitar's SG2000 article; a few rows from a Wikidata query of guitar models (109 rows). Sections are maker country, then maker."),
'Semi-hollow electric guitar':('One entry is a semi-hollow or thinline electric model sold under its own name.',"The same Wikipedia lists and maker pages, rows for semi-hollow and thinline models."),
'Hollow-body electric guitar':('One entry is a hollow-body electric archtop or thinline model sold under its own name.',"The same Wikipedia lists and maker pages, rows for fully hollow models."),
'Steel-string acoustic guitar':('One entry is a steel-string acoustic model sold under its own name; reissues and signature models are versions.',"Gibson, Fender, Epiphone and Martin Wikipedia pages, acoustic rows, plus Yamaha FG from Wikidata."),
'Classical guitar':('One entry is a classical guitar pattern or model named after its maker.',"Maker pages and Wikidata; this kind has no whole-space list."),
'Archtop acoustic guitar':('One entry is an acoustic archtop model.',"Gibson and Martin Wikipedia pages."),
'Resonator guitar':('One entry is a resonator guitar model.',"Existing sourced entries; no whole-space list was fetched."),
'Lap steel guitar':('One entry is a lap steel model.',"Fender and Rickenbacker Wikipedia pages."),
'Pedal steel guitar':('One entry is a pedal steel make or model.',"Existing entries plus the Fender list row."),
'Electric bass guitar':('One entry is a bass guitar model or series sold under its own name.',"Gibson, Fender, Ibanez, Epiphone, Rickenbacker, ESP and Jackson Wikipedia pages (bass rows), plus Yamaha and Tōkai rows from Wikidata."),
'Acoustic bass guitar':('One entry is an acoustic bass model.',"Martin Wikipedia page; other makers' models were not on a fetched page and are removed."),
'Guitar pickup':('One entry is a pickup model line, with revisions and pickup sets as versions.',"The Seymour Duncan and DiMarzio Wikipedia articles, which name the model lines; the PAF, P-90 and Filter'Tron origin entries stay from the structure pass."),
'Guitar strings':('A commodity kind: only the origin entry is kept.',"Wikipedia's String (music), which dates the first nylon guitar strings; other string ranges are brands of a commodity and are not listed."),
'Bass strings':('A commodity kind: no named entries.',"No fetched page names a first bass string, so the kind has no entries."),
'Bridge and tremolo':('One entry is a bridge or vibrato system.',"Existing entries from the structure pass; no whole-space list was fetched."),
'Tuning machines':('One entry is a tuning-machine pattern.',"Existing entries."),
'Combo amp':('One entry is an amplifier model line sold under its own name; era and reissue versions sit under it.',"Wikipedia's Fender amplifier, Marshall Amplification, Vox and Mesa Boogie articles plus the earlier sourced entries."),
'Amp head':('One entry is a head or piggyback amp model line.',"Wikipedia's Marshall Amplification, Vox, Mesa Boogie and Fender amplifier articles."),
'Speaker cabinet':('One entry is a cabinet model line.',"Wikipedia's Marshall Amplification article."),
'Guitar speaker':('One entry is a guitar loudspeaker model.',"Existing entries."),
'Amp modeller':('One entry is a modelling line.',"Existing entries; the models of other makers had no fetched page and are removed."),
}
EFXK={'Boost pedal','Overdrive pedal','Distortion pedal','Fuzz pedal','Tremolo and vibe pedal','Phaser pedal','Flanger pedal','Chorus pedal','Delay pedal','Reverb pedal','Wah pedal','Octave pedal','Pitch-shifter pedal','Compressor pedal','Noise gate','EQ pedal','Multi-effects processor','Looper','Volume pedal'}
for dp in depts:
  for sh in dp['s']:
    for k in sh['k']:
      kn=k['n']
      if k.pop('m',None):
          removed.append((kn,))
      if kn in('Guitar strings','Bass strings'):
          k['x']=[]; k.pop('r',None)
      ex=k.setdefault('x',[]) if (kn in A or k.get('x')) else k.get('x',[])
      seen=set()
      for e in ex:
          for nm in [e['n']]+(e.get('a') or '').split(' · ')+[v['n'] for v in e.get('v',[])]:
              seen.add(norm(nm))
              if e.get('mk'): seen.add(norm(nm.replace(e['mk'],'')))
      added=0
      for n,mk,y,d,s,kw in A.get(kn,[]):
          keys={norm(n),norm(n.replace(mk,''))}
          if keys & seen: continue
          seen|=keys
          ent={'n':n,'d':d,'mk':mk,'y':y,'s':s}
          if kw.get('v'): ent['v']=kw['v']
          if kw.get('role'): ent['role']=kw['role']
          ex.append(ent); added+=1
      if ex or 'x' in k:
          k['x']=ex
      for e in ex:
          c=CTY.get(e.get('mk',''))
          if not c: unk.add(e.get('mk'))
          e['g']=(c or 'Country not stated')+' · '+(e.get('mk') or 'Maker not stated')
      ex.sort(key=lambda e:(e['g'],ystart(e.get('y')),e['n']))
      if not ex: k.pop('x',None)
      stats[kn]=(len(ex),added)
      if kn in SEL: k['nl'],k['sel']=SEL[kn]
      elif kn in EFXK:
          k['nl']='One entry is a pedal or effects unit sold under its own name; later versions and reissues sit under it.'
          k['sel']="Wikipedia's Effects unit and Boss Corporation articles (read in full) plus the earlier sourced entries; pedals of other makers had no fetched page and are removed."
      elif not ex:
          k['sel']='No named entries: a commodity or parts kind with no fetched canon.'
      if ex: k['xg']='by maker country, then maker, then year'
      if ex and 'sel' not in k:
          k['nl']='One entry is a named model line.'; k['sel']='Existing entries.'
      if ex: k['sel']+=f" Shows {len(ex)} entries."
print(stats); print('unknown cty',unk)
json.dump({'replaces':sorted(names),'depts':depts,'brands':[],'brand_updates':{},'renames':{},'moves':[]},open('../../out/E3_parts/GUITAR.json','w'),ensure_ascii=False,indent=1)
