import json,re,collections
rows=[l.rstrip('\n').split('\t') for l in open('moma_items.tsv')]
rows=[r for r in rows if r[0]=='vase']
# page assignment by order: 40 per page, order of tsv: p2,p3,p1,p4,p5 as fetched
pages=[2,3,1,4,5]; 
urlbase='https://www.moma.org/collection/works/?q=vase&classifications=3'
des=["Elsa Fischer-Treyden, Margret Hildebrand","Erich Walter Stadler","Hans Coper","Michael Cohen","Tapio Wirkkala","Harvey Littleton","Sergio Asti","Alfredo Barbini","Peter Pelzel","Gunnar Cyrén","Ward Bennett","Timo Sarpaneva","Jan Bontjes van Beek","Kaj Franck","Nils Landberg","Flavio Poli","Paolo Venini","Alvar Aalto, Karhula Glassworks, Finland","Alvar Aalto","Umberto Nason","Sven Palmqvist","Lucie Rie, Hans Coper","Lucie Rie","Kitaoji Rosanjin","Richard Süssmuth","Vallauris","Fulvio Bianconi","Carl-Harry Stålhane","Wilhelm Wagenfeld","Seguso S.R.L., Murano, Italy","Unidentified Designer","Blenko Glass Co., Inc., Milton, WV","Josef Hoffmann","Gertrud Natzler, Otto Natzler","Peter Schlumbohm","Viking Glass Co., New Martinsville, WV","Frank Graham Holmes","Frances Felten","Walter Dorwin Teague","Russel Wright","Marguerite Wildenhain","Charles S. Todd","Louis Comfort Tiffany, Tiffany Studios, New York, NY","Louis Comfort Tiffany","Daum Frères, Nancy, France","Koloman Moser","Hans Ofner","Jacques Sicard","E. Bakalowitz & Söhne, Vienna","Johann Lötz Witwe, Tiffany Glass & Decorating Co., New York, NY","Johann Loetz","Emile Gallé","Hector Guimard","Grueby Faience Company, Boston, MA","Hugo Leven","John D. Wareham","Tomáš Gabzdil Libertíny","Hella Jongerius","Jiří Pelcl","Ronan Bouroullec, Erwan Bouroullec","Konstantin Grcic","Vincent de Rijk Kom BV","Toots Zynsky","Shiro Kuramata","Philippe Starck","Paul Chaleff","Sydney Cash","Otto Natzler","Ursula Morley Price","Makoto Komatsu","Thomas Patti","Mary Rogers","Ettore Sottsass","Enzo Mari","Lino Sabattini"]
short={"Elsa Fischer-Treyden, Margret Hildebrand":"Fischer-Treyden and Hildebrand","Alvar Aalto, Karhula Glassworks, Finland":"Aalto","Seguso S.R.L., Murano, Italy":"Seguso","Blenko Glass Co., Inc., Milton, WV":"Blenko","Gertrud Natzler, Otto Natzler":"Gertrud and Otto Natzler","Viking Glass Co., New Martinsville, WV":"Viking Glass","Louis Comfort Tiffany, Tiffany Studios, New York, NY":"Tiffany","Louis Comfort Tiffany":"Tiffany","Daum Frères, Nancy, France":"Daum","Johann Lötz Witwe, Tiffany Glass & Decorating Co., New York, NY":"Lötz Witwe for Tiffany","Grueby Faience Company, Boston, MA":"Grueby","E. Bakalowitz & Söhne, Vienna":"Bakalowitz","Lucie Rie, Hans Coper":"Rie and Coper","Ronan Bouroullec, Erwan Bouroullec":"Bouroullec","Vincent de Rijk Kom BV":"de Rijk","Johann Loetz":"Loetz","Unidentified Designer":"unidentified designer","Vallauris":"Vallauris"}
ctry={"Hans Coper":"United Kingdom","Lucie Rie":"United Kingdom","Lucie Rie, Hans Coper":"United Kingdom","Tapio Wirkkala":"Finland","Timo Sarpaneva":"Finland","Kaj Franck":"Finland","Alvar Aalto":"Finland","Alvar Aalto, Karhula Glassworks, Finland":"Finland","Paolo Venini":"Italy","Fulvio Bianconi":"Italy","Umberto Nason":"Italy","Flavio Poli":"Italy","Sergio Asti":"Italy","Alfredo Barbini":"Italy","Seguso S.R.L., Murano, Italy":"Italy","Gunnar Cyrén":"Sweden","Nils Landberg":"Sweden","Sven Palmqvist":"Sweden","Carl-Harry Stålhane":"Sweden","Wilhelm Wagenfeld":"Germany","Richard Süssmuth":"Germany","Jan Bontjes van Beek":"Germany","Josef Hoffmann":"Austria","Koloman Moser":"Austria","Hans Ofner":"Austria","E. Bakalowitz & Söhne, Vienna":"Austria","Johann Lötz Witwe, Tiffany Glass & Decorating Co., New York, NY":"United States","Johann Loetz":"Czech Republic","Louis Comfort Tiffany":"United States","Louis Comfort Tiffany, Tiffany Studios, New York, NY":"United States","Daum Frères, Nancy, France":"France","Emile Gallé":"France","Hector Guimard":"France","Jacques Sicard":"France","Vallauris":"France","Kitaoji Rosanjin":"Japan","Gertrud Natzler, Otto Natzler":"United States","Walter Dorwin Teague":"United States","Russel Wright":"United States","Frank Graham Holmes":"United States","Frances Felten":"United States","Charles S. Todd":"United States","John D. Wareham":"United States","Grueby Faience Company, Boston, MA":"United States","Blenko Glass Co., Inc., Milton, WV":"United States","Viking Glass Co., New Martinsville, WV":"United States","Harvey Littleton":"United States","Ward Bennett":"United States","Hella Jongerius":"Netherlands","Toots Zynsky":"United States","Shiro Kuramata":"Japan","Philippe Starck":"France"}
skipwords=['Tschichold','Boontje']
def parse(t):
    t=t.replace('Image not available ','')
    t=re.sub(r' On view Gallery \d+$','',t)
    for d in sorted(des,key=len,reverse=True):
        if t.startswith(d+' '):
            rest=t[len(d)+1:]; break
    else: return None
    m=re.search(r'(Designed 1936 \(this example produced 1956\)|c\. ?\d{4}(?:-\d{2,4})?|c\.\d{4}(?:-\d{4})?|\d{4}(?:-\d{2,4})?|\d{4}–\d{4})$',rest)
    y=m.group(1) if m else ''
    title=rest[:m.start()].strip() if m else rest
    return d,title,y
groups=collections.OrderedDict()
skipped=[]
for i,r in enumerate(rows):
    pg=pages[i//40] if i//40<5 else 5
    p=parse(r[1])
    if not p: skipped.append(r[1]); continue
    d,title,y=p
    key=(d,title,y)
    groups.setdefault(key,{'n':0,'pg':pg,'ids':[]})
    groups[key]['n']+=1; groups[key]['ids'].append(r[2].split('/')[-1])
print('skipped',skipped)
json.dump([[list(k),v] for k,v in groups.items()],open('b4_groups.json','w'),ensure_ascii=False,indent=0)
print(len(groups))
