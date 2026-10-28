import json,os,copy
O='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(O+'F2.json'))
B=json.load(open(O+'F2_brands.json'))
T=json.load(open(O+'F2_traditions.json'))
W='https://en.wikipedia.org/wiki/'
def find(dn,sn=None):
    dp=[x for x in d['depts'] if x['n']==dn][0]
    return dp if sn is None else [s for s in dp['s'] if s['n']==sn][0]
fig=find('Collectible figurines')
sh1=find('Collectible figurines','Porcelain & pottery figurines')
sh2=find('Collectible figurines','Crystal, metal & resin figurines')
old=[k for k in sh1['k'] if k['n']=='Porcelain and bone china figurine'][0]
arch={x['n']:x for x in old['x']}
# fold flat pieces
flat=old.get('m',[])
doul=arch['Royal Doulton HN figure']; lla=arch['Lladró figurine']
dn={v['n'] for v in doul['v']}
for n,mk in flat:
    if mk=='Royal Doulton' and n not in dn and not any(n.startswith(x.split(' (')[0]) for x in dn):
        doul['v'].append({"n":n,"mk":"Royal Doulton","y":"","d":""})
    elif mk=='Lladro':
        if n not in {v['n'] for v in lla['v']}: lla['v'].append({"n":n,"mk":"Lladro","y":"","d":""})
malin=[m for m in flat if m[1]=='Gustavsberg']
common_t=["limited edition","annual or club piece"]
cont=dict(n="Continental porcelain figure",a="European porcelain figure · hard-paste figure · Meissen-style figure",
 d="Figures from European porcelain manufactories such as Meissen, Nymphenburg and Herend, organised by house, then modeller or series.",
 t=["Hard-paste porcelain figurine","Soft-paste porcelain figurine","Biscuit (unglazed) porcelain figurine","Glazed pottery figurine"]+common_t,
 s=W+"Meissen_porcelain",
 x=[arch[n] for n in ['Meissen Kändler figures','Nymphenburg commedia dell\'arte figures','Capodimonte figure','Herend Hungarian figures']]+[
 {"n":"Bing & Grøndahl Thorvaldsen biscuit figures","a":"B&G biscuit figures","d":"Early biscuit porcelain figures from Bing & Grøndahl modelled on Bertel Thorvaldsen's neoclassical sculptures.","mk":"Bing & Grøndahl","y":"from 1853","s":W+"Bing_%26_Gr%C3%B8ndahl","v":[],"dt":"model after Thorvaldsen · biscuit finish · mark · size"},
 {"n":"Lomonosov peasant and minority figures","a":"Imperial Porcelain Factory figures","d":"Figures of peasants and ethnic types from the St Petersburg Imperial Porcelain Factory, later followed by Soviet propaganda figures.","mk":"Lomonosov Porcelain Factory","y":"1780s–1917","s":W+"Lomonosov_Porcelain_Factory","v":[{"n":"Fisherman, Lapplander and Ice Cream Seller","mk":"Lomonosov Porcelain Factory","y":"c. 1780–1800","d":"examples named on the page"},{"n":"Soviet propaganda figurines","mk":"Lomonosov Porcelain Factory","y":"after 1917","d":"plates and figurines of the Soviet elite"}],"dt":"period (Imperial vs Soviet) · factory mark · subject · restoration"}])
if malin: cont['m']=malin
eng=dict(n="English bone-china figure",a="English porcelain figure · Staffordshire china figure",
 d="Figures from English bone-china and porcelain potteries such as Royal Doulton, Beswick and Wade, organised by house, then series.",
 t=["Bone china figurine","Glazed pottery figurine","Earthenware figurine"]+common_t,
 s=W+"List_of_Royal_Doulton_figurines",
 x=[doul,arch['Beswick animal'],
 {"n":"Wade Whimsies","a":"Whimsies","d":"Small solid porcelain animal figures developed by Sir George Wade and launched at retail in 1954.","mk":"Wade Ceramics","y":"1954 onward","s":W+"Wade_Ceramics","v":[{"n":"Red Rose Tea figures","mk":"Wade Ceramics","y":"from 1967","d":"offered with Red Rose Tea"}],"dt":"series · animal · glaze · backstamp era"}])
giftw=dict(n="Collectible giftware figurine",a="collectors' society figurine · limited-edition figurine",
 d="Mass-produced collectible figures sold through gift retail and collectors' clubs, such as Hummel, Lladró and Precious Moments.",
 t=["limited edition","annual or club piece","retired piece"],
 s=W+"Hummel_figurines",
 x=[arch['M.I. Hummel figurine'],lla,arch['Precious Moments figurine']])
idx=sh1['k'].index(old)
sh1['k'][idx:idx+1]=[cont,eng,giftw]
# crystal additions
cr=[k for k in sh2['k'] if k['n']=='Crystal and glass figurine'][0]
cr['x']+= [
 {"n":"Baccarat Zodiaque","a":"Baccarat zodiac animals","d":"Annual limited-edition crystal animals for the Chinese zodiac, from Baccarat, founded 1764.","mk":"Baccarat","y":"annual","s":"https://formfluent.com/products/baccarat-zodiaque-snake-2025","v":[{"n":"Zodiaque Snake 2025","mk":"Baccarat","y":"2024","d":"designed by animal sculptor Allison Hawkes; reference 2816600"}],"dt":"zodiac animal · year · clear or gilded · limited edition"},
 {"n":"Daum pâte de verre figure","a":"Daum glass-paste sculpture","d":"Cast glass-paste pieces from Daum of Nancy, which revived pâte de verre in 1906.","mk":"Daum","y":"from 1906","s":W+"Daum_(studio)","v":[],"dt":"artist collaboration · signature · edition number"},
 {"n":"Kosta Boda Snakes in Love","a":"Föralskade Ormar","d":"Art-glass snakes by Ulrica Hydman-Vallien, c. 1985, from Sweden's Kosta Boda.","mk":"Kosta Boda","y":"c. 1985","s":W+"Kosta_Boda","v":[],"dt":"signature · size · colour"}]
# miniature cottage kind
cot=dict(n="Miniature cottage and village building",a="collectible cottage · miniature village house",
 d="A small hand-finished model of a cottage or village building sold as a collectible, usually in numbered collections.",
 t=["limited edition","retired piece","collectors' guild piece","lighted piece (see Department 56, B4)"],
 s=W+"Lilliput_Lane",
 x=[{"n":"Lilliput Lane cottage","a":"Lilliput Lane","d":"Miniature British cottages founded by David Tate in 1982; production ended in 2016.","mk":"Lilliput Lane","y":"1982–2016","s":W+"Lilliput_Lane","v":[{"n":"Langholm factory","mk":"Lilliput Lane","y":"2009","d":"production moved to Langholm, Scotland"},{"n":"Closure under Enesco","mk":"Lilliput Lane","y":"2016","d":"end of Lilliput Lane production"}],"dt":"collection · retired date · box and deed · size"},
 {"n":"David Winter Cottages","a":"David Winter cottage","d":"Miniature village houses first made by David Winter with John Hine in 1979; production ceased in 2002 or 2003.","mk":"David Winter","y":"1979–2003","s":W+"David_Winter_(sculptor)","v":[{"n":"First cottage","mk":"David Winter","y":"1979","d":"made with John Hine"}],"dt":"collection · retired date · Collectors Guild piece · box and certificate"}])
sh3={"n":"Miniature cottages & villages","k":[cot]}
fig['s'].append(sh3)
# monoprint -> type of monotype
pr=find('Prints','Monotypes & experimental prints')
mp=[k for k in pr['k'] if k['n']=='Monoprint'][0]
pr['k'].remove(mp)
mt=[k for k in pr['k'] if k['n']=='Monotype'][0]
mt['a']=(mt.get('a') or '')+(' · ' if mt.get('a') else '')+'monoprint'
mt['t']+= ["monoprint (plate with fixed lines or textures, varied each time)"]+[t for t in mp['t'] if t not in mt['t']]
mt['d']="A unique print pulled from ink or paint on a smooth plate; a monoprint uses a plate with fixed features."
# photo processes
ph=find('Photographs','Alternative & instant processes')
ph['k']+=[
 dict(n="Carbon print",a="carbon process · pigment print",d="A print whose image is pigmented gelatin rather than silver; light hardens the gelatin and warm water washes the rest away.",t=["single transfer","double transfer","carbro","Fresson","Autotype"],s=W+"Carbon_print",
 x=[{"n":"Swan carbon tissue print","a":"Autotype carbon print","d":"Carbon prints made from Joseph Swan's ready-made pigmented tissue, introduced in 1864 and marketed from 1866.","mk":"","y":"1864–","s":W+"Carbon_print","v":[],"dt":"tissue colour · transfer · mount"},
    {"n":"Carbro print","a":"carbon-bromide print","d":"A carbon print in which a silver bromide print, not light, hardens the gelatin; Autotype sold it in London 1920–1960.","mk":"","y":"1905 onward","s":W+"Carbon_print","v":[{"n":"Ozobrome process","mk":"","y":"1905","d":"Thomas Manly"}],"dt":"colour tri-carbro or single · size"},
    {"n":"Fresson print","a":"","d":"Pigment print process devised by Henri Théodore Fresson in 1899, sold in the USA 1927–1939.","mk":"","y":"1899","s":W+"Carbon_print","v":[],"dt":"grain · colour · size"}]),
 dict(n="Gum bichromate print",a="gum print · gum printing",d="A painterly print made from dichromate-sensitised gum and pigment, with no silver halides.",t=["monochrome","multi-layer colour","over platinum"],s=W+"Gum_bichromate",
 x=[{"n":"Pictorialist gum print","a":"","d":"Gum bichromate prints by Robert Demachy and Hugo Henneberg, who used the process for painterly images from photographic negatives.","mk":"","y":"1890s–1900s","s":W+"Gum_bichromate","v":[{"n":"Dichromate light-sensitivity discovered","mk":"","y":"1839","d":"Mungo Ponton"},{"n":"First colour images","mk":"","y":"1858","d":"John Pouncy"}],"dt":"pigment colour · layers · paper"}]),
 dict(n="Bromoil print",a="oil print",d="A print inked with oil paint on bleached bromide gelatin, allowing enlargement and hand control of the image.",t=["transfer bromoil","colour bromoil"],s=W+"Bromoil_process",
 x=[{"n":"Pictorialist bromoil","a":"","d":"Bromoil prints from 1907, when E. J. Wall described the process and C. Welborne Piper worked out its practice.","mk":"","y":"1907 onward","s":W+"Bromoil_process","v":[{"n":"A Crowd","mk":"","y":"1910","d":"Robert Demachy"}],"dt":"ink colour · paper · size"}]),
 dict(n="Woodburytype",a="Woodbury process print",d="A photomechanical print in pigmented gelatin pressed from a lead mould, with continuous tone and slight relief; patented 1864.",t=["book illustration","cabinet card","carte de visite"],s=W+"Woodburytype",
 x=[{"n":"Woodburytype cabinet card","a":"","d":"Portrait cabinet cards printed by Woodbury's process, including Annie Oakley's.","mk":"","y":"1864–1890s","s":W+"Woodburytype","v":[],"dt":"sitter · studio · relief edge · fading"}])]
# multiple
sc=find('Sculpture','Cast & modelled sculpture')
sc['k'].append(dict(n="Multiple",a="art multiple · editioned object",d="An artwork made in many typically identical copies, none the original; the term was introduced by Daniel Spoerri in 1959.",t=["signed","stamped","boxed","numbered edition"],s="https://beuys-multiples.pinakothek.de/en/what-are-multiples",
 x=[{"n":"Edition MAT multiple","a":"Multiplication d'Art Transformable","d":"Small editioned sculptures sold at low prices, launched by Daniel Spoerri's Edition MAT in 1959.","mk":"","y":"1959","s":"https://beuys-multiples.pinakothek.de/en/what-are-multiples","v":[],"dt":"artist · edition size · signature"},
 {"n":"Fluxus Flux-Kit","a":"Flux Box","d":"Boxed Fluxus multiples sold by George Maciunas from his Fluxshop in New York, opened 1963.","mk":"","y":"1963","s":"https://beuys-multiples.pinakothek.de/en/what-are-multiples","v":[],"dt":"box · contents · edition"},
 {"n":"Beuys multiple","a":"","d":"Larger sculptural multiples by Joseph Beuys from 1965, combining found materials with hand-formed elements, often signed or stamped.","mk":"","y":"1965–1986","s":"https://beuys-multiples.pinakothek.de/en/what-are-multiples","v":[],"dt":"signature or stamp · edition size · materials"}]))
# brands
have={b['n'].lower() for b in B['b']}
def add(n,c,f,seg,kf,dd,s):
    if n.lower() not in have:
        B['b'].append({"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":dd,"s":s}); have.add(n.lower())
add("Bing & Grøndahl","Denmark","1853","Heritage manufactory","porcelain","Copenhagen porcelain maker, founded 1853, known for biscuit figures and Christmas plates.",W+"Bing_%26_Gr%C3%B8ndahl")
add("Lomonosov Porcelain Factory","Russia","1744","Heritage manufactory","Russian porcelain","St Petersburg Imperial Porcelain Factory, founded 1744 by Dmitry Vinogradov.",W+"Lomonosov_Porcelain_Factory")
add("Wade Ceramics","United Kingdom","1867","Heritage manufactory","Whimsies","Burslem pottery founded 1867, known for small animal figures.",W+"Wade_Ceramics")
add("Lilliput Lane","United Kingdom","1982","Specialist","miniature cottages","Miniature cottage maker founded by David Tate in 1982; production ended in 2016.",W+"Lilliput_Lane")
add("David Winter","United Kingdom","1979","Specialist","miniature cottages","Sculptor of the David Winter Cottages, first made in 1979 with John Hine.",W+"David_Winter_(sculptor)")
add("Kosta Boda","Sweden","1742","Heritage manufactory","art glass","Swedish glassworks founded in 1742 as Kosta Glasbruk.",W+"Kosta_Boda")
# tradition
if 'Nihonga' not in {t['n'] for t in T['t']}:
    T['t'].append({"n":"Nihonga","g":"Painting","r":"Japan","p":"Meiji era (1868) onward","d":"Japanese-style painting in mineral pigments and nikawa glue on washi or silk, named to distinguish it from yōga.","tech":"brush painting with layered mineral pigments, gold or silver leaf","mat":"washi, silk, mineral pigments, nikawa glue, gofun","forms":["Nihonga"],"ctr":["Tokyo Fine Arts School","Hashimoto Gahō","Yokoyama Taikan","Shimomura Kanzan"],"auth":"Pigment layering and ground; modern copies are common.","s":W+"Nihonga"})
json.dump(d,open('/home/user/Possession-Taxonomy/rebuild/work/FIX_F2/F2.tmp','w'),ensure_ascii=False,indent=1)
json.dump(B,open('/home/user/Possession-Taxonomy/rebuild/work/FIX_F2/F2b.tmp','w'),ensure_ascii=False,indent=1)
json.dump(T,open('/home/user/Possession-Taxonomy/rebuild/work/FIX_F2/F2t.tmp','w'),ensure_ascii=False,indent=1)
