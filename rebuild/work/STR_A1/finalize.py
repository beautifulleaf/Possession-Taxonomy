import json,os,re
R='/home/user/Possession-Taxonomy/rebuild/'
old=json.load(open(R+'work/STR_A1/bak/A1.json'))
st=json.load(open(R+'work/STR_A1/stage.json'))
new=dict(old)
new['ax']="Which part of the body or occasion does the garment dress: a regional tradition, a trade, the skin layer, the head, the neck, hands or waist, formal wear, an outer layer, a dress or skirt, the legs, or the upper body?"
new['key']=[
"1. Is it dress or a named cloth belonging to a people or region (sari, kimono, kilt, kente, tartan)? → Traditional dress",
"2. Is it clothing made for a trade or a uniform (overalls, chore coat, chef's jacket)? → Workwear & uniform clothing",
"3. Is it worn against the skin, in bed or in the water (bra, socks, pyjamas, bikini)? → Underwear, nightwear & swim",
"4. Is it worn on the head (hat, cap, turban, headscarf)? → Hats & headwear",
"5. Is it worn on the neck, hands or waist (scarf, shawl, glove, belt)? → Scarves, gloves & belts",
"6. Is it a suit, a tailored jacket, a waistcoat, a tie or other dress-code formal piece? → Suits & formalwear",
"7. Is it an outer layer worn over other clothes (coat, jacket, tracksuit)? → Coats & jackets",
"8. Is it a dress? → Dresses",
"9. Is it a skirt, a one-piece with legs, a matching set or a costume? → Skirts, jumpsuits & sets",
"10. Does it cover the legs separately (jeans, trousers, shorts, leggings)? → Trousers, jeans & shorts",
"11. Otherwise it covers the upper body (shirt, jumper, hoodie, team shirt). → Tops",
"<i>Precedence: heritage workwear such as a chore coat is workwear (step 2) before a coat; a kilt or kimono is traditional dress (step 1) before a skirt or robe; a tie is formalwear (step 6) though worn at the neck; a hooded sweatshirt is a top (step 11), not a jacket.</i>"]
import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/STR_A1')
import patch_tt; print('patched',patch_tt.apply(st['depts']))
new['depts']=st['depts']
new['lead']=old['lead'].replace("organised by garment type (tops, bottoms, dresses, coats, suits, underwear, headwear, traditional dress, workwear)","organised by what part of the body or occasion the garment dresses (tops, legwear, dresses, skirts, coats, suits, underwear, headwear, neckwear and hands, traditional dress, workwear)")
tmp=R+'out/A1.json.tmp'
json.dump(new,open(tmp,'w'),ensure_ascii=False,separators=(',',':'))
os.replace(tmp,R+'out/A1.json')
# see target checks
names={}
for dp in new['depts']:
    for s in dp['s']:
        for k in s['k']: names[k['n']]=1
for c in('E2','H1'):
    d=json.load(open(R+f'reader/{c}.json'))
    names.update({('%s:'%c)+k['n']:1 for dp in d['depts'] for s in dp['s'] for k in s['k']})
for dp in new['depts']:
    for s in dp['s']:
        for k in s['k']:
            for sv in k.get('see',[]):
                key=sv[1] if sv[0]=='A1' else sv[0]+':'+sv[1]
                if key not in names: print('BAD SEE',k['n'],sv)
            if 't' in k: print('still t',k['n'])
            if not k.get('s'): print('NO S',k['n'])
# brands check for mk
print(os.path.getsize(R+'out/A1.json'))
