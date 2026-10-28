import json,os
P='out/B2'
d=json.load(open(P+'.json'));br=json.load(open(P+'_brands.json'));tr=json.load(open(P+'_traditions.json'))
def find(n):
    for dp in d['depts']:
        for s in dp['s']:
            for i,k in enumerate(s['k']):
                if k['n']==n: return dp,s,i,k
def rm(n):
    dp,s,i,k=find(n); s['k'].pop(i); return k
def addt(k,*ts):
    k.setdefault('t',[]); k['t']+= [t for t in ts if t not in k['t']]
def alias(k,*a):
    cur=[x for x in k.get('a','').split(' · ') if x]
    k['a']=' · '.join(cur+[x for x in a if x not in cur])
def addm(k,ms):
    k.setdefault('m',[]); k['m']+=ms
# B2-4
duv=find('Duvet')[3]; c=rm('Comforter')
alias(duv,'comforter (US)'); addt(duv,'sewn-through comforter (fill built in, no cover)')
duv['d']="A filled top cover with loose fill in stitched channels or boxes; a duvet takes a removable cover, a US comforter is sewn closed."
addm(duv,c['m'])
top=find('Mattress topper')[3]
for n,t in(('Featherbed','featherbed (feather or down)'),('Mattress pad','thin quilted mattress pad')):
    k=rm(n); alias(top,n.lower()); addt(top,t)
top['d']="A removable layer laid on a mattress to change its feel; thicker toppers and thin quilted pads are types."
k=rm('Sheer curtain'); cur=find('Curtain')[3]; alias(cur,'sheer curtain · voile · net curtain'); addt(cur,'sheer or voile')
k=rm('Panel blind'); v=find('Vertical blind')[3]; alias(v,'panel blind'); addt(v,'wide sliding panels (panel track)')
k=rm('Tie-up shade'); r=find('Roman blind')[3]; alias(r,'tie-up shade'); addt(r,'tie-up shade (hand-gathered, no cords)')
cc=rm('Cushion cover'); sc=find('Scatter cushion')[3]
alias(sc,'cushion cover'); addt(sc,'cover only (removable)','cushion with insert')
sc['d']="A loose stuffed decorative cushion for a sofa, chair or bed; the removable cover is sold alone or with the insert."
# B2-5
fc=find('Floor cushion')[3]
for n in('Meditation cushion','Meditation mat'):
    k=rm(n); addm(fc,k['m'])
alias(fc,'zafu · meditation cushion · meditation mat')
fc['t']=[t for t in fc['t'] if t!='zabuton']+['zabuton (flat mat)','zafu (round or crescent)','pouffe-style' ] if False else fc['t']
addt(fc,'zafu (round or crescent meditation cushion)','zabuton (flat padded mat)')
fc['d']="A large frameless cushion or mat made to sit on at floor level, including Zen meditation zafu and zabuton (see the Spiritual pursuits taxonomy)."
# B2-6
dp=find('Tablecloth')[0]
dp['note']="Tier for everyday table linen; variety for linen houses and table-linen traditions."
for n in('Tablecloth','Table runner','Cloth napkin','Fabric placemat','Tea towel'):
    k=find(n)[3]
    k['m']=[m for m in k.get('m',[]) if m[1]!='IKEA']
    if not k['m']: k.pop('m')
# B2-7
kf=find('Kotatsu futon')[3]
kf['d']="A quilted cover draped over a heated low table (kotatsu) to hold its warmth in; the table itself is Heated low table in Furniture & storage."
# B2-2
today='2026-10-28'
kind={"n":"Printed & embroidered furnishing textile","a":"furnishing cloth · decorative textile","d":"Patterned cloth by the metre or ready-made, printed, resist-dyed or embroidered, for hangings, upholstery, curtains and cushions.",
"t":["printed","resist-dyed (ikat)","embroidered","by the metre","ready-made hanging"],"s":"https://en.wikipedia.org/wiki/Ikat",
"x":[
{"n":"Suzani","a":"suzandozi","d":"Embroidered tribal textile of Central Asia and Iran, traditionally made by brides as part of a dowry.","mk":"","y":"examples from late 18th–early 19th c.","s":"https://en.wikipedia.org/wiki/Suzani_(textile)","v":[],"dt":"Tajikistan, Uzbekistan, Afghanistan origin · large blossom motifs · antique or new"},
{"n":"Ikat furnishing cloth","a":"ikat","d":"Cloth woven from yarns resist-dyed before weaving, so the pattern shows on both faces with a slightly blurred edge.","mk":"","y":"","s":"https://en.wikipedia.org/wiki/Ikat","v":[
 {"n":"Patola","mk":"","y":"","d":"silk double ikat of Patan and Khambat, Gujarat"},
 {"n":"Geringsing","mk":"","y":"","d":"double ikat of Tenganan, Bali"},
 {"n":"Pochampally","mk":"","y":"","d":"double ikat silk of Andhra Pradesh"},
 {"n":"Abrbandi","mk":"","y":"","d":"Uzbek ikat"}],"dt":"warp, weft or double ikat · silk or cotton"},
{"n":"Toile de Jouy","a":"toile","d":"Fabric printed with a single-colour pastoral scene, usually on white or off-white, named for Jouy-en-Josas near Paris.","mk":"","y":"late 18th c.","s":"https://en.wikipedia.org/wiki/Toile_de_Jouy","v":[],"dt":"red, blue or black on cream · cotton or linen · wallpaper and furnishing weights"},
{"n":"Josef Frank prints","a":"Svenskt Tenn textiles","d":"Large-scale botanical furnishing prints designed by Josef Frank for Svenskt Tenn, including designs made in New York 1941–1946.","mk":"Svenskt Tenn","y":"1930s–1940s","s":"https://en.wikipedia.org/wiki/Svenskt_Tenn","v":[],"dt":"printed linen or cotton · by the metre"}]}
dp=[x for x in d['depts'] if x['n']=='Cushions & covers'][0]
dp['s'].append({"n":"Furnishing fabrics","k":[kind]})
if not any(b['n']=='Svenskt Tenn' for b in br['b']):
    br['b'].append({"n":"Svenskt Tenn","c":"Sweden","f":"1924","seg":"Heritage manufactory","kf":"Josef Frank prints","d":"Stockholm interiors house founded by Estrid Ericson, known for Josef Frank furniture and textile designs.","lines":[],"eras":["Estrid Ericson, founder, 1924"],"sig":["Josef Frank prints"],"sc":[],"rel":[],"s":"https://en.wikipedia.org/wiki/Svenskt_Tenn"})
tr['t']+= [
{"n":"Suzani","g":"Textiles & rugs","r":"Central Asia and Iran","p":"surviving examples from late 18th c.","d":"Embroidered tribal textile made by brides as dowry; called suzandozi in Iran.","tech":"embroidery","mat":"","forms":["Printed & embroidered furnishing textile"],"ctr":["Tajikistan","Uzbekistan","Afghanistan"],"auth":"","s":"https://en.wikipedia.org/wiki/Suzani_(textile)"},
{"n":"Ikat","g":"Textiles & rugs","r":"Southeast Asia, South Asia, Central Asia, Japan, Americas","p":"","d":"Resist-dyeing of yarns before weaving so the pattern shows on both faces.","tech":"warp, weft or double ikat","mat":"silk, cotton","forms":["Printed & embroidered furnishing textile"],"ctr":["Patan and Khambat","Tenganan","Pochampally","Odisha"],"auth":"Both faces patterned, with slightly blurred design edges.","s":"https://en.wikipedia.org/wiki/Ikat"},
{"n":"Toile de Jouy","g":"Textiles & rugs","r":"France","p":"late 18th c.","d":"Fabric printing of single-colour pastoral scenes on pale ground, named for Jouy-en-Josas.","tech":"fabric printing","mat":"cotton, linen","forms":["Printed & embroidered furnishing textile"],"ctr":["Jouy-en-Josas"],"auth":"","s":"https://en.wikipedia.org/wiki/Toile_de_Jouy"}]
for n,o in((P+'.json',d),(P+'_brands.json',br),(P+'_traditions.json',tr)):
    json.dump(o,open(n+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(n+'.tmp',n)
