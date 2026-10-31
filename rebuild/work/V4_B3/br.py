import json,os
p='/home/user/Possession-Taxonomy/rebuild/out/B3_brands.json'
b=json.load(open(p)); have={x['n'].lower() for x in b['b']}
def B(n,c,f,seg,dd,s,sig=[]): return {'n':n,'c':c,'f':f,'seg':seg,'d':dd,'lines':[],'eras':[],'sig':sig,'sc':[],'rel':[],'s':s,'kf':''}
new=[B('Signify','Netherlands','2016','Global group','Dutch lighting company spun off from Philips in 2016, named Philips Lighting N.V. until 2018; owns Philips Hue, WiZ and Color Kinetics.','https://en.wikipedia.org/wiki/Signify_N.V.',['Philips Hue']),
 B('ams OSRAM','Germany','1919','Global group','Osram was formed in 1919 from the lighting businesses of Auergesellschaft, Siemens & Halske and AEG; ams took it over in July 2020.','https://en.wikipedia.org/wiki/Osram'),
 B('GE Lighting','United States','1911','Global group','Lighting business sold by General Electric to Savant Systems on 1 July 2020.','https://en.wikipedia.org/wiki/GE_Lighting'),
 B('Savant Systems','United States','','Independent','Home automation company based in Hyannis, Massachusetts, which bought GE Lighting in 2020.','https://en.wikipedia.org/wiki/GE_Lighting'),
 B('Newell Brands','United States','','Global group','Owner of the Coleman brand since its acquisition of Jarden in December 2015.','https://en.wikipedia.org/wiki/Coleman_Company'),
 B('Nanoleaf','Canada','2012','Independent','Smart-lighting company founded in 2012 by Gimmy Chu, Christian Yan and Tom Rodinger; privately held.','https://en.wikipedia.org/wiki/Nanoleaf',['Nanoleaf Light Panels','Nanoleaf Essentials']),
 B('Toshiba','','','Global group','Released the first commercial white LED lamp for homes in 2007.','https://en.wikipedia.org/wiki/LED_lamp')]
for n in new:
    if n['n'].lower() not in have: b['b'].append(n)
json.dump(b,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
