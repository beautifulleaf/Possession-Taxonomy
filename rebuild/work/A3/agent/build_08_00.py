import json, os
W='https://en.wikipedia.org/wiki/'
CU=W+'Cuban_link_chain'; RO=W+'Rope_chain'; JP=W+'Jesus_piece_(jewelry)'; GR=W+'Grill_(jewelry)'
CL='https://culted.com/dookie-chain-defined-hip-hop-tyler-new-album-ll-cool-j/'
IF='https://www.ifandco.com/blogs/jewelry-news-and-insights/different-types-of-grillz-styles'
kinds=[
{"n":"Cuban link chain","a":"Cuban chain · Cuban links","d":"Heavy chain of interlocking uniform oval links derived from the curb chain, a hip-hop status piece.","t":["polished","diamond-set","handmade","machine-made","lobster clasp"],"s":CU,
 "x":[
  {"n":"Miami Cuban link","a":"Miami Cuban","d":"Tighter, denser Cuban chain with slightly rounder links; the best-known form, from Miami's Cuban and hip-hop scenes.","mk":"","y":"1970s–1980s","s":CU,"v":[],"dt":"width from slim to oversized · gold, silver, platinum · solid or diamond-set"},
  {"n":"Iced Cuban link","a":"Diamond Cuban","d":"Cuban link chain set with diamonds or other gemstones across the links.","mk":"","y":"","s":CU,"v":[],"dt":"stone coverage · gold colour · width"},
  {"n":"LA Cuban link","a":"","d":"Cuban chain with thicker links and sharper filing, a harder-edged Los Angeles style.","mk":"","y":"","s":CU,"v":[],"dt":"width · metal"}]},
{"n":"Rope chain","a":"Dookie chain · twist chain","d":"Chain of small links twisted together into a rope pattern, worn thick in Golden Age hip-hop.","t":["thin","medium","thick","polished","diamond-cut","sterling silver","gold"],"s":RO,
 "x":[
  {"n":"Dookie rope chain","a":"Dookie chain · dookie roll","d":"Very thick gold rope chain, the signature status piece of 1980s hip-hop worn by Run-DMC, LL Cool J and Slick Rick.","mk":"","y":"1980s","s":CL,
   "v":[{"n":"Dapper Dan × Gucci dookie roll","mk":"Gucci","y":"2018","d":"revival in Dapper Dan's Gucci collaboration"}],"dt":"thickness · gold carat · pendant worn on it"}]},
{"n":"Iced-out pendant","a":"Iced pendant · chain piece · medallion","d":"Large pendant heavily set with diamonds or gems, worn on a heavy chain as a hip-hop status piece.","t":["custom logo piece","religious figure","gold","platinum","diamond","coloured gemstones"],"s":JP,
 "x":[
  {"n":"Jesus piece","a":"","d":"Pendant of Jesus's face, usually with the crown of thorns, often set with gems; first worn in rap by Ghostface Killah.","mk":"","y":"1990s","s":JP,
   "v":[{"n":"Notorious B.I.G. pieces","mk":"Tito Caicedo","y":"1990s","d":"popularised the form; given to associates"},
        {"n":"Kanye West piece","mk":"Jacob & Co","y":"2004","d":"by Jacob Arabo; diamonds, aquamarine eyes, ruby tears"},
        {"n":"Kanye West × Takashi Murakami design","mk":"Takashi Murakami","y":"2007","d":"artist-designed version"}],"dt":"face size · stones (diamond, aquamarine, ruby) · gold colour · budget wood or base-metal versions"},
  {"n":"adidas Superstar pendant","a":"","d":"Gold Superstar shoe pendant given to Run-DMC after their song \"My Adidas\" and worn on their rope chains.","mk":"adidas","y":"1986","s":CL,"v":[],"dt":"14k gold"}]},
{"n":"Grillz","a":"Grills · fronts · golds · caps","d":"Removable metal cover worn over the teeth, often gold and set with stones.","t":["top 6","top 8","bottom 8","bottom 10","single cap","removable","permanent","10k–24k gold","silver","platinum","yellow, white or rose gold"],"s":GR,
 "x":[
  {"n":"Fronts","a":"Caps","d":"Multi-tooth gold caps adapted from single crowns by Eddie Plein in New York, the first grills.","mk":"","y":"1980s","s":GR,
   "v":[{"n":"Just-Ice's teeth","mk":"Eddie Plein","y":"1987","d":"on the Kool and Deadly album; first notable client"}],"dt":"number of teeth · gold carat"},
  {"n":"Solid gold grill","a":"Solid set","d":"Gold grill covering the whole visible face of each tooth, polished or matte.","mk":"","y":"","s":IF,"v":[{"n":"Satin-finish bottom 8","d":"matte finish"}],"dt":"teeth covered · finish · gold colour"},
  {"n":"Open-face grill","a":"Open-faced grill · window cut","d":"Grill whose metal frames each tooth and leaves the natural enamel showing.","mk":"","y":"","s":IF,"v":[{"n":"Open-face top 6","d":"14k yellow gold"},{"n":"Open-face white gold diamond","d":"diamond-set frame"}],"dt":"teeth covered · cut shape · stones"},
  {"n":"Iced grill","a":"Fully iced set · diamond grill","d":"Grill pavé-set with diamonds over some or all teeth.","mk":"","y":"2000s","s":IF,
   "v":[{"n":"Paul Wall grills","mk":"Johnny Dang & Co.","y":"2002","d":"partnership that made the Houston jeweller's name"},{"n":"Deep-cut upper 6","d":"deep-cut diamond setting"},{"n":"Princess-cut grill","d":"princess-cut diamonds"}],"dt":"teeth covered · stone cut · gold colour"},
  {"n":"Double-cap grill","a":"","d":"Lighter grill design with caps split across the tooth, plain or iced on one or both sides.","mk":"","y":"","s":IF,"v":[],"dt":"plain or iced · teeth covered"}]}]
brands=[
 {"n":"Jacob & Co","c":"United States","f":"1986","seg":"Luxury jewellery and watches","d":"New York jeweller founded by Jacob Arabo ('Jacob the Jeweler'), early maker of large diamond pieces for hip-hop artists.","lines":["Five Time Zone","Astronomia","Epic","Billionaire"],"sig":["Jesus piece"],"sc":["Hip-hop"],"rel":["Johnny Dang & Co."],"s":W+"Jacob_%26_Co"},
 {"n":"Johnny Dang & Co.","c":"United States","f":"1998","seg":"Hip-hop jewellery and grillz","d":"Houston jeweller of Johnny Dang, known for jewelled grills and his partnership with Paul Wall from 2002; first store opened 1998.","sig":["Iced grill"],"sc":["Hip-hop"],"rel":["Jacob & Co"],"s":W+"Johnny_Dang"},
 {"n":"adidas","c":"Germany","f":"1949","seg":"Sportswear","d":"German sportswear maker from Herzogenaurach.","sig":["adidas Superstar pendant"],"s":"knowledge"}]
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":"All four planned kinds are new (no old data). Not added: Ben Baller (IF & Co.), Avianne, Elliot Eliantte — no reliable retrieved register-level page (Ben Baller Wikipedia 404). Box clasp and specific Cuban widths unconfirmed, left out. Nameplate necklace (Big Daddy Kane, Slick Rick; source https://en.wikipedia.org/wiki/Nameplate_necklace) belongs with Initial and name pendant on the Pendants shelf, not duplicated here. Doorknocker earrings not sourced. Johnny Dang & Co. founding year given as his first store (TV Jewelry, 1998). Tennis chain left to Tennis necklace kind. No traditions apply."}
p='/home/user/Possession-Taxonomy/rebuild/work/A3/shelves/08_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
