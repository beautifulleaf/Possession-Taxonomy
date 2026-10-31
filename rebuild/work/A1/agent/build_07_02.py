import json, os
W='https://en.wikipedia.org/wiki/'
AO=W+'%C3%81o_d%C3%A0i'; KB=W+'Kebaya'; BK=W+'Baju_kurung'; BT=W+'Barong_tagalog'; SR=W+'Sarong'
BS=W+'Baro%27t_saya'; PT=W+'Puletasi'; MU=W+'Muumuu'; MH=W+'Mother_Hubbard_dress'; RV=W+'Ram%C3%B3n_Valera'
LY=W+'Longyi'; AA=W+'Anne_Avantie'; PS=W+'Pacific_Sisters'; SP=W+'Sampot'; SN=W+'Sinh_(clothing)'
HB='https://www.heritagebarong.com/pages/about-heritage-barong'
def X(n,d,s,a='',mk='',y='',v=None,dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[{"n":a_[0],"mk":a_[1],"y":a_[2],"d":a_[3]} for a_ in (v or [])],"dt":dt}
kinds=[
{"n":"Ao dai","a":"áo dài · Vietnamese long dress","d":"Vietnamese long, side-split tunic worn over loose silk trousers, for women and men.","s":AO,
 "t":["women's","men's","áo dài mini (knee-length panels)","áo dài cách tân (short modern cut)","wedding","school uniform (white)"],
 "x":[X("Áo ngũ thân","Five-panel buttoned court gown, the predecessor of the áo dài.",AO,a="five-piece shirt",mk="",y="18th century",
        v=[("Court dress decree of Nguyễn Phúc Khoát","","1744","Trousers and buttoned gown ordered at the Nguyễn court in Phú Xuân")],dt="five panels · knee-to-ankle length · silk, brocade"),
      X("Áo dài Le Mur","Close-fitting two-piece buttoned women's design that defines the modern áo dài.",AO,a="Le Mur shirt",mk="Nguyễn Cát Tường",y="1930",
        v=[("Lê Phô styles","Lê Phô","1934","Several popular variations introduced from 1934")],dt="fitted bodice · high collar · side splits · silk"),
      X("Raglan-sleeve áo dài","Saigon cut with raglan sleeves and a diagonal seam, giving a closer fit at shoulders.",AO,mk="Trần Kim",y="1950s",
        v=[("Thiết Lập Tailors cut","Trần Kim","1950s",""),("Dũng Tailors cut","Dũng","1950s","")],dt="raglan sleeve · diagonal seam"),
      X("Boat-neck áo dài","Collarless version with a wide boat neckline.",AO,a="Madame Nhu áo dài",mk="",y="1958",dt="boat neck · fitted"),
      X("Áo dài hippy","Late-1960s youthful variant.",AO,y="1968"),
      X("Áo gấm","Men's thick brocade long tunic worn at Tết and ceremonies.",AO,a="brocade long shirt",dt="brocade · colours · turban (khăn đóng) pairing"),
      X("Áo tứ thân","Older four-panel northern garment counted in the broader áo dài family.",AO,a="four-piece shirt")]},
{"n":"Baju kurung & baju Melayu","a":"baju kurung · baju Melayu · baju kebarung","d":"Malay loose blouse-and-skirt outfit for women (baju kurung) and loose shirt with trousers and samping for men (baju Melayu).","s":BK,
 "t":["women's baju kurung","men's baju Melayu","samping (kain dagang) worn over","festive / Raya set","family matching set"],
 "x":[X("Teluk Belanga","Collarless Johor style with an embroidered neckline, now the standard baju kurung.",BK,mk="",y="reign of Sultan Abu Bakar of Johor",
        v=[("Teluk Belanga baju Melayu","","","Men's version, two pockets")],dt="no collar · mata lalat neck stitching · pockets"),
      X("Cekak Musang","Style with a standing collar fastened by buttons, two of them on the collar.",BK,
        v=[("Cekak Musang baju Melayu","","","Men's version, typically three pockets")],dt="stand collar · five buttons"),
      X("Baju Kurung Kedah","Short, hip-length top usually worn with plain batik, everyday wear in northern Malaysia.",BK,dt="hip length · Teluk Belanga neck"),
      X("Baju Kurung Riau-Pahang","Cekak Musang collar with seven or nine buttons, linked to the Riau and Pahang courts.",BK,a="Pahang"),
      X("Baju Puteri Perak","Perak version with trousers instead of a sarong, worn with samping.",BK,dt="trousers · samping · Cekak Musang collar"),
      X("Baju Kurung Moden","Modern baju kurung with embroidery, beads, sequins and a wide range of fabrics.",BK,dt="embellishment · bright colours · fabric"),
      X("Kebarung","Late-1990s blend of kebaya and baju kurung.",KB,y="late 1990s")]},
{"n":"Kebaya","a":"kebaya · nyonya kebaya · kebaya encim","d":"Front-opening fitted blouse fastened by buttons or brooches, worn over a sarong, kain or kemben in maritime Southeast Asia.","s":KB,
 "t":["kerongsang brooch fastening","semi-transparent (voile)","brocade","velvet","lace"],
 "m":[["Couture kebaya","Anne Avantie"]],
 "x":[X("Kebaya Kartini","Javanese aristocratic kebaya, non-transparent with a V-collar.",KB,dt="V-collar · opaque · worn with batik kain"),
      X("Kebaya Kutubaru","Kebaya with an extra panel forming a square collar, believed to come from Central Java.",KB,dt="stomacher panel · square collar"),
      X("Nyonya kebaya","Peranakan semi-transparent, heavily embroidered kebaya fastened with three linked kerongsang brooches.",KB,a="kebaya sulam · Peranakan kebaya",dt="voile · embroidery colours · kerongsang set"),
      X("Kebaya Encim","Kebaya of Chinese-Indonesian women in Javanese coastal cities, adopted by the Betawi.",KB),
      X("Balinese kebaya","Tight V-neck kebaya with a sash, worn for Hindu rituals.",KB,dt="lace or brocade · sash colour"),
      X("Sundanese kebaya","Tight brocade kebaya with a U-collar and extra-long lower panels.",KB),
      X("Keraton kebaya","Aristocratic Solo style, usually dark velvet with beads and sequins.",KB,a="Solo kebaya"),
      X("Kebaya Labuh","Loose knee-length Malay tunic associated with Melayu Lingga culture.",KB),
      X("Kebaya Bandung","Very short 1950s kebaya with a shawl collar.",KB,y="1950s"),
      X("Kebaya Saloma","Tight kebaya with a wide neck and low back, popularised by singer Saloma.",KB,mk="",y="mid-20th century"),
      X("Kebaya Kota Bharu","Kebaya with a front flap (lidah baju) fastened with snaps instead of brooches.",KB),
      X("Kebaya Madura","Tapered kebaya with a V-collar worn with neck and chest jewellery.",KB,a="rancongan"),
      X("Kebaya Kerancang","Betawi kebaya decorated with kerancang cut-work embroidery.",KB)]},
{"n":"Sarong & wrap cloth","a":"sarong · kain sarung · wrap skirt · kanga","d":"Length of cloth, open or sewn into a tube, wrapped round the waist or body.","s":SR,
 "t":["open length","sewn tube","checked","printed","handwoven silk","beach wrap"],
 "m":[["Kira",""],["Lambahoany",""]],
 "x":[X("Longyi","Burmese cloth tube about 2 m long, held at the waist by folding, not knotting.",LY,
        v=[("Paso","","","Men's, tied in front, stripes or checks"),("Htamein","","","Women's, single broad fold, black htet sint waistband"),("Acheik","","","Elaborate wave-pattern silk for weddings, Amarapura"),("Bangauk paso","","","Men's silk for special occasions")],dt="cotton, silk, mercerised · stripes, checks, regional pattern (Rakhine, Mon, Kachin, Inle, Zin Mè, Yaw, Dawei)"),
      X("Sinh","Handmade Lao and northern/north-eastern Thai tube skirt whose patterned hem shows the wearer's region.",SN,
        v=[("Lao sinh","","",""),("Isan sinh","","",""),("Lanna (Tai Yuan) sinh","","","")],dt="silk or handwoven cotton · hua sinh waistband · tin sinh hem"),
      X("Sampot","Cambodian lower garment, worn draped as a skirt or twisted through the legs.",SP,
        v=[("Sampot chong kben","","","Unisex wrap pulled between the legs and belted"),("Sampot samloy","","","Free-hanging tube or wrap skirt"),("Sampot hol","","","Ikat silk in uneven twill"),("Sampot charobab","","","Gold or silver brocaded silk for dancers and weddings"),("Sampot phamuong","","","Plain shimmering silk for ceremonies")],dt="silk · ikat, brocade, damask"),
      X("Lavalava","Samoan sarong-type wrap.",SR,a="lava-lava · 'ie lavalava"),
      X("Pāreu","Tahitian and Cook Islands wrap, known as pareo elsewhere.",SR,a="pareo · pareu"),
      X("Isulu","Fijian sarong-type wrap.",SR,a="sulu"),
      X("Tupenu","Tongan sarong-type wrap.",SR),
      X("Malong","Mindanao tube cloth used as skirt, turban, blanket and more.",SR),
      X("Kain pelikat","Malaysian checked sarong for men; kain batik and kain samping are the other main Malay types.",SR),
      X("Lungi","Coloured wrap of Bangladesh and southern and eastern India.",SR,a="kaili"),
      X("Kikoi","Swahili-coast men's wrap with simple designs, also used as a throw or beachwear.",SR,a="kikoy"),
      X("Kanga","Brightly coloured printed cotton wrap of the Swahili coast carrying a proverb.",SR),
      X("Chitenge","Printed wrap of Zambia and Malawi.",SR,a="chitenje · kitenge"),
      X("Capulana","Mozambican wrap cloth.",SR),
      X("Lamba","Malagasy wrap cloth.",SR)]},
{"n":"Barong Tagalog","a":"barong · baro","d":"Sheer, embroidered, long-sleeved Philippine formal shirt worn untucked over an undershirt.","s":BT,
 "t":["piña","piña seda","jusi","piña jusi","sinamay","pinukpok (abacá)","jusilyn","organza","pechera (chest) embroidery","sabog (all-over) embroidery","calado","sombrado","camisa de chino undershirt"],
 "m":[["Hand-embroidered custom barong","Heritage Barong"]],
 "x":[X("Classic barong","Sheer, untucked long-sleeved barong that replaced the barong mahaba from the 1840s.",BT,y="1840s",dt="nipis fabric · embroidered pechera · collar"),
      X("Barong mahaba","Early long barong, often striped, with ruff or high collars.",BT,a="long baro",y="1820s"),
      X("Baro cerrada","Closed-neck, usually opaque barong of the 1890s worn with white trousers.",BT,a="Americana cerrada",y="1890s"),
      X("Pinukpok barong","Longer, coat-like mid-19th-century barong; the name now covers formal opaque abacá barongs.",BT,y="mid-19th century"),
      X("Pierre Cardin barong","1970s fitted barong with a large point collar and flared sleeves.",BT,y="1970s"),
      X("Polo barong","Short-sleeved, least formal barong, often linen, ramie or cotton.",BT),
      X("Shirt-jack barong","Shirt-jacket cut with a wide hem band, worn untucked.",BT),
      X("Gusót-mayaman barong","Linen or linen-look everyday office barong that wrinkles easily.",BT,a="linen barong")]},
{"n":"Terno & Filipiniana","a":"Filipiniana · baro't saya · terno · traje de mestiza","d":"Philippine women's national dress: blouse-and-skirt baro't saya and its gown forms, the terno with butterfly sleeves.","s":BS,
 "t":["pañuelo (shoulder kerchief)","tapis overskirt","piña","embroidered","wedding","semi-formal"],
 "x":[X("Baro't saya","Blouse (baro) and long skirt (saya), with pañuelo kerchief and tapis overskirt.",BS,a="baro at saya",dt="camisa · saya · pañuelo · tapis"),
      X("Traje de mestiza","Aristocratic gown form of the baro't saya.",BS,a="María Clara gown",
        v=[("Bell-sleeve María Clara wedding gown","Ramón Valera","","Reimagined with stiffened bell sleeves as a wedding dress")]),
      X("Terno","Unified one-piece gown with butterfly sleeves, fastened at the back with a zip.",RV,mk="Ramón Valera",y="20th century",dt="butterfly sleeves · one piece · back zip"),
      X("Balintawak","Casual and cocktail-dress version of the terno.",BS),
      X("Kimona","Visayan variant: short-sleeved or poncho-like embroidered blouse with a patadyong skirt.",BS)]},
{"n":"Pacific island dress","a":"island dress · mission dress · Mother Hubbard","d":"Loose, yoked missionary-derived dresses and two-piece outfits worn across Polynesia, Melanesia and Micronesia.","s":MH,
 "t":["floral or aloha print","matching family or church set","tapa or woven flax waist overlay"],
 "x":[X("Holokū","Hawaiian fitted long gown with train, from the Mother Hubbard dress brought by missionaries.",MH,y="1820s"),
      X("Muʻumuʻu","Loose yokeless Hawaiian dress without a train, part of aloha wear.",MU,a="muumuu",y="19th century",dt="cotton · floral Polynesian prints · length"),
      X("Puletasi","Samoan, Tongan and Fijian two-piece of tunic top over a wrap skirt, worn to church and formal events.",PT,a="puletaha (Tonga)",y="late 19th century",dt="matching or plain skirt · print"),
      X("Robe mission","New Caledonian loose mission dress, also called robe popinée.",MH,a="robe popinée"),
      X("Meri blaus","Papua New Guinea women's blouse, formal local attire.",MH,a="meri blouse"),
      X("Wau","Marshall Islands mission dress named after Oahu.",MH),
      X("ʻAhu māmā rūʻau","Tahitian Mother Hubbard dress, 'grandmother's dress'.",MH,a="ʻahu tua")]}]
brands=[
 {"n":"Anne Avantie","c":"Indonesia","f":"1989","seg":"designer kebaya couture","d":"Semarang-born designer called a pioneer of contemporary kebaya, starting from a rented house with two sewing machines.","lines":[],"eras":["Anne Avantie, 1989–present"],"sig":[],"sc":[],"rel":[],"s":AA},
 {"n":"Heritage Barong","c":"Philippines","f":"1950s","seg":"made-to-measure barong","d":"Lumban, Laguna maker of hand-embroidered barong tagalog, tracing back to Brigida Yasoña-Macalos in the early 1950s.","lines":["Hand-embroidered barong tagalog","Wedding barong"],"eras":[],"sig":["Classic barong"],"sc":[],"rel":[],"s":HB},
 {"n":"Ramón Valera","c":"Philippines","f":"","seg":"couture (designer)","d":"Filipino couturier (1912–1972), first fashion designer named National Artist of the Philippines, credited with the one-piece zip-back terno.","lines":[],"eras":["Ramón Valera, 20th century"],"sig":["Terno","Traje de mestiza"],"sc":[],"rel":[],"s":RV},
 {"n":"Pacific Sisters","c":"New Zealand","f":"1992","seg":"artist and fashion collective","d":"Pacific and Māori collective of artists, designers and performers known for fashion activism.","lines":[],"eras":["Founders Selina Forsyth, Niwhai Tupaea, Suzanne Tamaki, 1992"],"sig":[],"sc":[],"rel":[],"s":PS}]
G='Textiles & rugs'
trads=[
 {"n":"Lumban embroidery","g":G,"r":"Lumban, Laguna, Philippines","p":"20th century–present","d":"Hand embroidery of barong tagalog and linens in the town called the embroidery capital of the Philippines.","tech":"Hand embroidery on sheer cloth","mat":"Piña, jusi and other sheer fabrics","forms":["Barong Tagalog"],"ctr":["Lumban"],"auth":"Hand-stitched rather than machine embroidery","s":HB},
 {"n":"Acheik silk weaving","g":G,"r":"Amarapura, Myanmar","p":"19th century–present","d":"Weaving of elaborate wave-patterned silk for wedding longyi.","tech":"Silk weaving of wave or houndstooth acheik patterns","mat":"Silk","forms":["Sarong & wrap cloth"],"ctr":["Amarapura"],"auth":"Silk acheik wave pattern","s":LY},
 {"n":"Khmer silk weaving","g":G,"r":"Cambodia","p":"Funan era–present","d":"Cambodian silk weaving for sampot: ikat hol, brocaded charobab, damask rbauk.","tech":"Resist-dyed ikat in uneven twill; supplementary metallic-thread brocade","mat":"Silk, gold and silver thread","forms":["Sarong & wrap cloth"],"ctr":[],"auth":"Hol: one face brighter than the other from the uneven twill","s":SP},
 {"n":"Lao and Tai sinh weaving","g":G,"r":"Laos; northern and north-eastern Thailand","p":"traditional","d":"Hand weaving of tube skirts whose hem designs mark the region of origin.","tech":"Handloom weaving with patterned hem (tin sinh)","mat":"Silk, handwoven cotton","forms":["Sarong & wrap cloth"],"ctr":[],"auth":"Handwoven; regional hem pattern","s":SN},
 {"n":"Peranakan nyonya kebaya embroidery","g":G,"r":"Malaysia, Singapore, Indonesia","p":"traditional–present","d":"Semi-transparent kebaya embroidered heavily and fastened with linked kerongsang brooches.","tech":"Embroidery (sulam) on voile","mat":"Voile, embroidery thread, kerongsang brooches","forms":["Kebaya"],"ctr":[],"auth":"Dense embroidery; three linked kerongsang","s":KB}]
notes=("Old sarong models Kikoi, Kitenge (as Chitenge), Lamba, Lungi, Pareu (as Pāreu), Sulu (as Isulu) became archetypes; Kira and Lambahoany kept in m (no page retrieved). "
 "Old kind source (simplybeach shop page) replaced by Wikipedia Sarong. Lungi and East African wraps kept here because the old kind was merged here; the South Asian and African shelves may cross-link. "
 "Not added: Vinta Gallery (site 404/403), Kultura (only search snippets), Pacific Sisters has no archetype link (collective stub only), Hue/Saigon ateliers and Raya labels (no pages retrieved), "
 "kebaya UNESCO 2024 listing noted only via Kebaya article; terno butterfly-sleeve history pages were blocked so Terno rests on the Ramón Valera page; aloha-print sets left to the Aloha shirt kind.")
out={"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/A1/shelves/07_02.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
print(len(kinds), sum(len(k['x']) for k in kinds), len(brands), len(trads))
