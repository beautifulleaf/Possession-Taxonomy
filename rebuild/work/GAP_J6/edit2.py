import json,re,os
Q='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(Q+'work/GAP_J6/J6.tmp')); br=json.load(open(Q+'work/GAP_J6/J6_brands.tmp'))
K={k['n']:k for D in d['depts'] for S in D['s'] for k in S['k']}
for e in K['Everyday ground & filter coffee']['x']:
  if not e.get('g'): e['g']='National champion: United States'
for e in K['Single-origin coffee']['x']: e['g']=e.get('g') or e['n'].split(' ')[0]
def strip(s):
  s=re.sub(r'\s*(Complete: [^.]*\.?|Covers \d+ of about[^.]*\.?|No complete (list|reference)[^.]*\.?|No whole-space reference[^.]*\.?|Kept from the earlier edition[^.]*\.?)\s*$','',s.strip())
  return s
NC='No complete list exists; follows '
cov={
'Single-origin coffee':'Origins named by fetched pages (Kenya, Jamaica, Kona, Colombia, Tarrazú, Antigua, Mocha); '+NC.lower()+'the country and cooperative pages cited. No complete list exists; follows those overviews.',
'Special-process coffee':'No complete list exists; follows the process pages cited (monsooning, civet and elephant-passage coffee).',
'Espresso blends':'No complete list exists; follows the Lavazza and illy brand pages.',
'Decaffeinated coffee':'No complete list exists; follows the JDE Peet\'s, Lavazza and illy pages and the decaffeination processes cited.',
'Traditional regional coffee':'No complete list exists; follows the regional pages cited for each preparation.',
'Coffee capsules & pods':'No complete list exists; follows the capsule systems named on the Nestlé, Keurig Dr Pepper, JDE Peet\'s and Lavazza pages.',
'Instant coffee':'No complete list exists; follows the Nescafé, Nestlé and JDE Peet\'s pages plus the Korea Times and Wikipedia pages for Maxim and G7.',
'Darjeeling tea':'Covers {n} gardens named in the Wikipedia article on Darjeeling tea, read to its end; the article gives no full garden register and no Tea Board register was found, so gardens it omits are not entries.',
'Assam & Indian black tea':'No complete list exists; follows the Wikipedia articles on Assam and Nilgiri tea (the Wikipedia page on tea in India returned 404 and RateTea shows only 10 of its 771 Indian teas).',
'Ceylon tea':'No complete list exists; follows the Wikipedia articles on Ceylon tea and tea production in Sri Lanka, which name {n} regions and estates; no register of Sri Lankan estates was found.',
'Kenyan, African & Black Sea tea':'No complete list exists; follows the Wikipedia article on tea production in Kenya and the Rize and Ilam pages cited.',
'Sencha & steamed green tea':'Covers {n} types, cultivars and regions from the Wikipedia articles on sencha and Japanese tea; no complete list of named Japanese teas was found (the Japanese teas list page returned 404).',
'Gyokuro & kabusecha':'Covers {n} entries from the Wikipedia article on gyokuro, read in full; no complete list of Japanese shaded teas exists.',
'Matcha':'Covers {n} entries from the Wikipedia article on matcha (first 100,000 characters read); no complete list of matcha brands or regions exists.',
'Chinese green tea':'Complete: 11 of 11 green teas on the Wikipedia list of Chinese teas; the other entries are further teas kept from the earlier edition.',
'Korean green tea':'No complete list exists; follows the Korean tea pages cited.',
'Yellow tea':'Complete: 2 of 2 yellow teas on the Wikipedia list of Chinese teas; the other two entries are kept from the earlier edition.',
'Wuyi rock oolong':'Complete: 9 of 9 Wuyi oolongs among the 16 oolongs on the Wikipedia list of Chinese teas; the list does not state provinces, so the other oolongs of unstated origin are in the next kind.',
'Tieguanyin & Anxi oolong':'Complete: 16 of 16 oolongs on the Wikipedia list of Chinese teas across this kind and Wuyi rock oolong (Pouchong is under Taiwanese oolong).',
'Taiwanese oolong':'Covers {n} teas, cultivars and mountains from the Wikipedia article on Taiwanese tea (first 100,000 of about 111,000 characters read); no complete list of Taiwanese teas was found.',
'White tea':'Complete: 3 of 3 white teas on the Wikipedia list of Chinese teas; Gong Mei is kept from the earlier edition.',
'Raw pu-erh (sheng)':'No complete list exists; the Wikipedia list of Chinese teas has the single entry Pu\'er, and recipes and factories follow the Pu\'er tea page.',
'Dark tea (hei cha)':'No complete list exists; the Wikipedia list of Chinese teas adds only Fu Cha, which is Fu brick tea.',
'Earl Grey & bergamot tea':'No complete list exists; follows the Earl Grey pages cited and the RateTea style list.',
'Jasmine & scented tea':'No complete list exists; follows the jasmine and scented tea pages cited and the RateTea style list.',
'Flavoured tea':'No complete list exists; follows the maker pages cited and the RateTea style list.',
'Herbal blend':'No complete list exists; follows the Celestial Seasonings and Yogi Tea pages and the Wikipedia list of tea companies.',
'Yerba mate':'No complete list exists; follows the mate pages cited.',
'Rooibos':'No complete list exists; follows the rooibos pages cited.',
'Kava':'No complete list exists; follows the kava pages cited.',
'Drinking chocolate':'No complete list exists; follows the tradition pages cited and the Wikipedia pages on Cadbury and Ghirardelli.',
'Instant hot chocolate mix':'No complete list exists; follows The Nibble hot chocolate overview and the Nesquik page.',
'Cocoa powder':'No complete list exists; follows the cocoa processing page cited.',
'Malted chocolate drink powder':'No complete list exists; follows the Ovaltine, Milo and Horlicks pages cited.',
}
for kn,c in cov.items():
  k=K[kn]; n=len(k['x'])
  base=strip(k.get('sel',''))
  if kn=='Single-origin coffee': base=''
  base=re.sub(r'; the Wikipedia pages on Japanese tea and the tea company list name[^.]*\.?','',base)
  base=base.replace('Kept from the earlier edition with fetched sources','Entries kept from the earlier edition, each with a fetched source').replace('Kept from the earlier edition','Entries kept from the earlier edition')
  if kn=='Single-origin coffee': base='Origins kept from the earlier edition, each backed by a fetched page; origin names as sold (Yirgacheffe, Sumatra, Gayo and others) are descriptions in the text, not separate entries.'; c='No complete list exists; follows the origin pages cited.'
  k['sel']=(base.rstrip('. ')+'. ' if base else '')+c.format(n=n)
# updated partial ones
k=K['Everyday ground & filter coffee']; k['sel']=strip(k['sel'])+f" Covers {len(k['x'])} brands of about 80 coffee companies on that list; the rest are roasters and chains without a packaged national brand, and no complete ranked list of packaged coffee brands exists. Brazil (3 Corações, Pilão) added from a fetched market article."
k=K['Breakfast & everyday black tea']; k['sel']=strip(k['sel'])+f" Covers {len(k['x'])} entries; of about 120 companies on that list the rest are blenders, retailers and speciality houses without a fetched ownership page. English Breakfast and the other blend styles are kept from the earlier edition."
# dedupe stray repeated periods
for kk in K.values():
  if 'sel' in kk: kk['sel']=re.sub(r'\.\s*\.','.',kk['sel']).replace('  ',' ')
# missing coverage check
for kn,kk in K.items():
  if kk.get('x') and not re.search(r'(Complete: |Covers \d+ |No complete list exists)',kk.get('sel','')): print('MISSING',kn)
# kinds >12 w/o g
for kn,kk in K.items():
  if len(kk.get('x',[]))>12 and any(not e.get('g') for e in kk['x']): print('NOG',kn,[e['n'] for e in kk['x'] if not e.get('g')])
json.dump(d,open(Q+'work/GAP_J6/J6.final','w'),ensure_ascii=False,indent=1)
json.dump(br,open(Q+'work/GAP_J6/J6_brands.final','w'),ensure_ascii=False,indent=1)
