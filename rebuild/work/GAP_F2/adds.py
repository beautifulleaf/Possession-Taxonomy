W='https://en.wikipedia.org/wiki/'
# kind -> (ref_slug, ref_label, rows_m, rest_text, [ (name, year, desc, alias) ])
A={}
A['Rarely met named process']=('List_of_photographic_processes',"Wikipedia's List of photographic processes",250,"the rest are existing kinds, aliases, film stocks, negatives, papers and darkroom steps, which are not photographs; both windows of the list were read to its end at Ziatype",[
 ('Oil print','','Named in the list as the Oil Print Process; the list gives no date or description.',''),
 ('Pinatype','','Named in the list as the Pinatype process; the list gives no date or description.',''),
 ('Wash-off relief','','Named in the list; the list gives no date or description.',''),
 ('Stanhope','','Named in the list; the list gives no date or description.',''),
 ('Photolithography','','Named in the list; the list gives no date or description.','')])
# calligraphy
isl=lambda n,y,d,a='':(n,y,d,a)
A['Islamic calligraphy']=('Islamic_calligraphy',"Wikipedia's Islamic calligraphy article",10,"the article was read to character 100,000 of 184,335 and names ten styles, all now entries or versions; later sections are history and artists",[
 ('Kufic','late 7th century (disputed)','Angular, rigid script that later branched into floral, foliated, plaited, bordered and square (banna\'i) forms.',''),
 ('Naskh','7th century','Standard script for copying books and manuscripts, and the basis of modern Arabic print.',''),
 ('Thuluth','15th century (refined)','Script with long vertical strokes and broad spacing, refined by Ottoman calligraphers.','Sulus'),
 ('Reqāʿ','10th century','Handwriting style like thuluth but with short strokes and small flourishes.','Riqa'),
 ('Muhaqqaq','Mamluk era','Majestic thuluth variant, later limited mostly to short phrases such as the basmala.',''),
 ('Maghrebi script','','Script derived from Kufic letters, written with a pointed pen; sub-styles are mujawher and mabsut.',''),
 ('Sudani script','','Maghrebi sub-style developed in the West African Sahel.',''),
 ('Diwani','16th to early 17th century','Ornate Ottoman cursive for court documents; the djali variant is densely decorated.','Divani'),
 ("Nasta'liq",'','Persian cursive script with sloped lines and high-contrast hook-like letters; shikasteh is a 17th-century variant.','Nastaliq'),
 ('Sini script','','Chinese-influenced style written with a horsehair brush.','')])
A['Western calligraphy']=('Western_calligraphy',"Wikipedia's Western calligraphy article",26,"the page names 26 hands; Merovingian script, Humanist minuscule and Antiqua are named without description and are included as entries only where the page dates them",[
 ('Roman square capitals','','Formal Roman capital letters.',''),
 ('Rustic capitals','','Early Roman capital lettering, later used in manuscripts.',''),
 ('Roman cursive','','Informal, running Roman handwriting.',''),
 ('Uncial','c. 5th century','Rounded capital-style book hand that developed from Roman bookhands.',''),
 ('Half-uncial','c. 5th century','Hand related to uncial, developed from Roman bookhands at the same time.',''),
 ('Carolingian minuscule','late 8th century','Lowercase hand developed under Charlemagne and Alcuin; ancestor of modern book type.',''),
 ('Beneventan script','8th century','Regional book hand named in the page table; no description given.',''),
 ('Visigothic script','9th century','Regional book hand named in the page table; no description given.',''),
 ('Insular script','','Hand named in the article links; no description given.',''),
 ('Blackletter','12th century','Compressed, angular northern European hand used by Gutenberg for printing.','Gothic hand'),
 ('Rotunda','12th century onward','Rounder, heavier Gothic variant favoured in Italy and Spain.',''),
 ('Chancery hand','mid-15th century','Standardised hand for official and legal documents in late medieval England.',''),
 ('Italic','15th century','Lighter, slanted hand designed by Italian scribes.','Chancery cursive'),
 ('Roman bookhand','15th century','Italian revival of Roman and Carolingian models; became a printed standard.',''),
 ('Bastarda','mid-1600s','Speed hand, one of three approved for French legal documents.',''),
 ('Coulée','mid-1600s','Hand that French officials restricted for legal documents.',''),
 ('Round hand','mid-1600s','French legal hand (rhonde), later English roundhand.','Rhonde'),
 ('English script','18th century','Hand named in the page table; no description given.',''),
 ('Copperplate','','Hand named in the article navigation list; no description given.',''),
 ('Spencerian','','Hand named in the article navigation list; no description given.','')])
A['East Asian calligraphy']=('Shufa',"Wikipedia's Shufa article",10,"the article was read to character 100,000 of 133,959; large seal script is not covered and Oracle bone and bronze inscriptions are historical scripts, not display styles",[
 ('Small seal script','c. 220 BCE','Qin standardised form of seal script (xiaozhuan), unified under Li Si.','Xiaozhuan'),
 ('Clerical script','Han dynasty','More regular, angular style close to modern print; still used for decoration.','Lishu'),
 ('Regular script','mature by the 7th century','Newest major style, with the most standardised strokes.','Kaishu'),
 ('Semi-cursive script','Han origins','Partly abbreviated running style that most readers of regular script can follow.','Xingshu'),
 ('Cursive script','Han through Jin','Fast, highly abbreviated style that is hard for non-practitioners to read.','Caoshu'),
 ('Slender gold script','early 12th century','Imperial style of gold-coloured writing used by Emperor Huizong on paintings.','Shoujinshu')])
A['Carved seal']=('Seal_carving',"Wikipedia's Seal carving article",14,"the other rows are state seals and navigation-box items, which are not carved personal seals",[
 ('Hui (Wan) School seal','Ming and Qing','Anhui school of seal carving, also called the Wan School.','Wan School seal'),
 ('Hai School seal','late Qing and Republic','Shanghai school of seal carving.',''),
 ('Balin stone seal','Qing','Seal cut from Balin stone, used from the Qing dynasty.',''),
 ('Side-carved seal','','Seal art that focuses on the vertical sides of the seal.',''),
 ('Seal knob carving','','Seal art that focuses on the head, or knob, of the seal.','')])
# tapestry
A['Tapestry']=('Tapestry',"Wikipedia's Tapestry article",30,"the page was read to character 100,000 of 168,063; rugs (kilim, Navajo), institutions and restoration workshops are not tapestry kinds",[
 ('Beauvais tapestry','1664','French manufactory founded by Colbert as a private enterprise; specialised in furniture upholstery.',''),
 ('Brussels tapestry','c. 1500–1794','Main weaving centre from the early 16th century; city marks required from 1528.',''),
 ('Arras tapestry','15th century','Leading centre whose name became the word for tapestries; sacked in 1477.',''),
 ('Tournai tapestry','late 15th to early 16th century','Centre that rose after Arras was sacked in 1477.',''),
 ('Oudenarde verdure tapestry','from c. 1600','Landscape (verdure) tapestries from Oudenarde.',''),
 ('Delft Armada tapestry','1590s','Armada Tapestries (1591) and Dutch naval victory sets woven in Delft.',''),
 ('Mortlake tapestry','1619 to late 17th century','English royal works using Flemish weavers at first; best work in the 1620s and 1630s.',''),
 ('Barberini tapestry','1630 to late 17th century','Roman workshop founded by Cardinal Francesco Barberini.',''),
 ('Royal Tapestry Factory, Madrid','1720','Spanish factory founded after Spain lost its Flemish territories; Goya drew cartoons from 1775.',''),
 ('Pinton Felletin tapestry','20th century','Aubusson-area workshop that wove Graham Sutherland\'s Coventry Cathedral tapestry (1962).',''),
 ('Kesi','Ming dynasty and earlier','Chinese silk tapestry weave used for court clothing and later to copy paintings.','K\'o-ssu'),
 ('Pre-Columbian Peruvian tapestry','','Peruvian tradition of pieces meant to be seen from both sides.',''),
 ('Millefleur tapestry','c. 1400–1550','Background of small flowers on a green ground, common in unicorn and heraldic sets.',''),
 ('Heraldic tapestry','late medieval to Renaissance','Smaller piece with a coat of arms over a floral field.',''),
 ('Jacquard tapestry','late 19th century onward','Machine-woven figurative textile with optical colour blending.','')])
# ceramics
A['Art pottery']=('Art_pottery',"Wikipedia's Art pottery article",30,"all named companies and lines on the page are entries except studios already covered by other kinds",[
 ('Linthorpe Art Pottery','1879','Yorkshire works linked to the designer Christopher Dresser.',''),
 ('Mintons Art Pottery Studio','1870–71','Art studio of the Staffordshire firm Mintons; also made the Secessionist Ware range.',''),
 ('Doulton Lambeth stoneware','','Lambeth art stoneware, including pieces incised by Hannah Barlow (1874).',''),
 ('Maw & Co art pottery','','Maker known for encaustic tiles and "Art Pottery" lines from the 1880s.',''),
 ('Ruskin Pottery','1898–1935','English pottery known for high-fired reduction glaze effects.',''),
 ("Pilkington's Lancastrian Pottery",'','English pottery that made uranium glazes.',''),
 ('Royal Copenhagen art pottery','1883','Porcelain maker that moved to art-pottery-style designs after Aluminia bought it in 1883.',''),
 ('Rozenburg (Haagsche Plateelbakkerij)','taken over 1884','The Hague maker of Art Nouveau porcelain, including the Rozenburg teapot of 1900.',''),
 ('Zsolnay art pottery','','Budapest firm known for architectural ceramics and eosin glaze.',''),
 ('Tonwerke Kandern slip-painted earthenware','c. 1898','German slip-painted earthenware designed by Max Laeuger.',''),
 ('Service Rousseau','1867','Early Japonisme service designed by Félix Bracquemond at Creil-Montereau.',''),
 ('Théodore Deck faience','1856','Islamic-inspired French faience; Deck became art director of Sèvres in 1887.',''),
 ('Cowan Pottery','','One of the major Ohio art potteries.',''),
 ('Lonhuda Pottery','','One of the major Ohio art potteries.',''),
 ('J. B. Owens Pottery','','One of the major Ohio art potteries.',''),
 ('Roseville Pottery','','One of the major Ohio art potteries.',''),
 ('Weller Pottery','','One of the major Ohio art potteries.',''),
 ('Dedham Pottery','c. 1886–89','Massachusetts pottery known for Hugh C. Robertson\'s crackle glaze.',''),
 ('Marblehead Pottery','','Massachusetts art pottery.',''),
 ('Paul Revere Pottery','c. 1911','Massachusetts art pottery.',''),
 ('Van Briggle Pottery','1903','American art pottery of Artus Van Briggle.','')])
A['Studio pottery']=('Japanese_pottery_and_porcelain',"Wikipedia's Japanese pottery and porcelain article (for the mingei strand)",1,"the Studio pottery article has no list of named forms; no complete list exists, so the kind also follows department overviews",[
 ('Mashiko ware','20th century (mingei era)','Folk pottery centre in Tochigi led by Shōji Hamada.',''),
 ('Mingei pottery','1920s–1930s onward','Japanese folk-craft movement founded by Yanagi Sōetsu.','')])
J=lambda n,r,y,d,a='':(n,y,r+' '+d if r else d,a)
A['Asian art ceramics']=('Japanese_pottery_and_porcelain',"Wikipedia's Japanese pottery and porcelain article (read to its end, 137,030 characters)",75,"the rest are ancient pottery (Jōmon, Yayoi, Haji), glazes, repair and gilding techniques, vessel forms and European factories, which are not Asian art wares; Korean wares beyond Goryeo and Joseon are not named by the page",[
 ('Shigaraki ware','Kamakura','Shiga ware among the Six Ancient Kilns, known for tanuki figures.',''),
 ('Tamba ware','Kamakura','Hyōgo ware among the Six Ancient Kilns, also called Tatekui ware.',''),
 ('Tokoname ware','Kamakura','Aichi ware among the Six Ancient Kilns.',''),
 ('Echizen ware','','Fukui ware among the Six Ancient Kilns.',''),
 ('Seto ware','Kamakura','Aichi ware among the Six Ancient Kilns; "seto-mono" became a general word for Japanese ceramics.',''),
 ('Shino ware','late 16th century','Mino ware with a prized milky glaze.',''),
 ('Oribe ware','late 16th century','Mino ware known for copper-green glaze.',''),
 ('Ki-Seto and Setoguro','late 16th century','Yellow and black glazed Mino wares made by Seto potters who fled civil wars.',''),
 ('Arita ware','early Edo','Main source of Japanese export porcelain, begun by Korean potters.',''),
 ('Nabeshima ware','1675','Elite porcelain of the Nabeshima clan\'s kiln, with textile-inspired designs.',''),
 ('Hirado ware','17th century onward','Fine blue painting on white porcelain.',''),
 ('Kyō ware','17th century onward','Kyoto ceramics shaped by Ninsei and Kenzan; Kiyomizu ware is a sub-category.','Kyōyaki'),
 ('Hagi ware','Azuchi-Momoyama onward','Low-fired, fragile Yamaguchi ware prized for tea.',''),
 ('Karatsu ware','16th century','Saga ware that is the most-produced pottery in western Japan.',''),
 ('Kutani ware','late 17th century','Ishikawa enamelled porcelain; Ko-Kutani is the old style.',''),
 ('Iga ware','Edo','Mie ware similar to Shigaraki and used in tea.',''),
 ('Asahi ware','Edo','Wood-ash-glazed stoneware tea bowls from Uji.',''),
 ('Takatori ware','Momoyama','Kiln listed among the Sengoku-period kilns.',''),
 ('Koishiwara ware','16th century','Fukuoka ware founded by a Korean potter, with coil-and-throw technique.',''),
 ('Onta ware','18th century style','Slipware made in a village without electricity.',''),
 ('Tobe ware','Edo','Ehime thick porcelain with cobalt blue painting.',''),
 ('Tsuboya ware','19th century example','Ryukyuan porcelain tableware with cobalt painting.',''),
 ('Banko ware','19th century','Mie teacups, teapots and flower vases.',''),
 ('Mikawachi ware','Edo','Porcelain with underglaze blue.',''),
 ('Tenmoku','12th–13th century','Chocolate-brown glaze from Song China, prized in the tea ceremony.',''),
 ('Chinese celadon','1st century','Chinese ware with a green glaze, listed with Yue, Xing and Longquan lines.',''),
 ('Ding ware','10th century','Chinese white-bodied ware named in the page\'s China list.',''),
 ('Qingbai','12th century','Chinese pale blue-white porcelain named in the page\'s China list.',''),
 ('Chinese blue and white porcelain','14th century onward','Jingdezhen porcelain painted in underglaze cobalt.',''),
 ('Blanc de Chine','14th century onward','Chinese white porcelain named in the page\'s China list.',''),
 ('Kraak porcelain','16th century','Chinese export porcelain named in the page\'s China list.',''),
 ('Swatow ware','16th century','Chinese export ware named in the page\'s China list.',''),
 ('Famille verte, jaune, noire and rose','17th century','Chinese porcelain enamel palettes named in the page\'s China list.',''),
 ('Canton porcelain','18th century','Chinese export porcelain named in the page\'s China list.',''),
 ('Joseon white porcelain','14th century','Korean porcelain named in the page\'s Korea list.','')])
A['Studio glass']=('Studio_glass',"Wikipedia's Studio glass article",22,"the article's institutions, schools and residencies are not objects and are left out",[
 ('Flameworked glass','','Torch-based, small-scale glass; lampworking.','Lampworked glass'),
 ('Fused glass','','Layers fused in a kiln at a lower temperature than casting.',''),
 ('Slumped glass','','Glass formed over or into a mould in a kiln.',''),
 ('Pâte de verre','','Cast glass technique listed as a studio technique.',''),
 ('Cold-worked glass','','Glass shaped without heat by cutting, sandblasting or gluing.',''),
 ('Sandblasted and etched glass','','Surface relief made by sandblasting or acid etching.',''),
 ('Murrine and cane glass','','Patterned glass tiles set into blown bubbles, and stretched coloured rods; zanfirico is woven cane.',''),
 ('Incalmo, reticello and latticino','','Glassblowing techniques developed on Murano.','')])
A['Art glass']=('Art_glass',"Wikipedia's Art glass article",15,"the page's techniques (cutting, engraving, frosting) are attributes of glass, not entries",[
 ('Peach Blow glass','1886–88','Blown glass with gold enamel from the New England Glass Company.',''),
 ('Edo kiriko','','Japanese cut glass.',''),
 ('Bohemian cut glass','19th century','Two-layered cut beakers from Bohemia.',''),
 ('Art cut crystal','1920–70','Limited-run designer cut crystal, such as Keith Murray for Steven & Williams.',''),
 ('Lalique moulded glass','','Moulded glass in Art Nouveau and Art Deco designs.',''),
 ('Orrefors art glass','','Swedish factory art glass.',''),
 ('Kosta art glass','','Swedish factory art glass.',''),
 ('Brilliant Period cut glass','to c. 1915','Deeply cut glass in High-Victorian style.','')])
A['Stained-glass panel']=('Stained_glass',"Wikipedia's Stained glass article",16,"the article was read to character 100,000 of 277,630; individual glaziers and windows are works and makers, not panel kinds",[
 ('Grisaille panel','15th century (example)','Black linear paint fired onto coloured glass.',''),
 ('Pot-metal glass panel','medieval','Panel of glass coloured through its body while molten.',''),
 ('Flashed glass panel','medieval onward','Thin coloured layer fused to clear glass, used especially for red.',''),
 ('Silver-stain panel','after c. 1300','Yellow-to-orange stain fired onto the glass surface; earliest dated window is 1313.',''),
 ('Cathedral glass panel','mid-1830s','Rolled sheet glass.','Rolled glass'),
 ('Crown glass roundel','','Spun hand-blown glass with a bull\'s-eye centre.',''),
 ('Opalescent glass panel','late 19th century','Streaky, mottled glass associated with Louis Comfort Tiffany.','')])
# textile
A['Art quilt']=('Quilt',"Wikipedia's Quilt article",18,"patchwork, appliqué, trapunto, sashiko and kantha are techniques, held in the neighbouring kinds or as attributes",[
 ('Baltimore album quilt','1840s','Quilt of detailed appliquéd blocks, often floral, on white or off-white grounds.',''),
 ('Amish quilt','','Traditionally solid-coloured quilts from Lancaster, Pennsylvania, and the Midwest.',''),
 ('Hawaiian quilt','','Wholecloth quilt with symmetrical appliqué, often red on white.',''),
 ('Crazy quilt','late 19th century','Irregular pieces of luxury fabric with decorative embroidery, made for display.',''),
 ('Durham quilt','Industrial Revolution onward','Densely quilted wholecloth quilt from north-east England.','North Country quilt'),
 ('Tivaevae','','Ceremonial quilts of the Cook Islands, given at weddings and christenings.',''),
 ('Boutis','since the 17th century','Stuffed wholecloth quilting from Provence.','Provençal quilting'),
 ('Story quilt','','Quilt with text and imagery that narrates stories, associated with Faith Ringgold.','')])
A['Embroidered picture']=('Sampler_(needlework)',"Wikipedia's Sampler (needlework) article",12,"all twelve sampler types named by the page are entries here or in Appliqué textile picture",[
 ('Spot sampler','200 BCE–300 CE','Scattered motifs; the earliest extant sampler is Nazca.',''),
 ('Coptic sampler','400–500 CE','Silk on linen with early Christian designs, found in burial grounds.',''),
 ('Dechado','1509 inventory','Spanish sampler; fifty are recorded in a 1509 inventory and all have since disappeared.',''),
 ('Dutch sampler','1608','Oldest known Dutch embroidery sampler.',''),
 ('Band sampler','mid-17th century onward','Narrow band of fabric fully covered in stitches.',''),
 ('Whitework sampler','before 1603','Reticella whitework in white linen thread.',''),
 ('Philadelphia sampler','1805','Silk on linen, worked by Catharine Ann Speel.',''),
 ('Barbados sampler','1771 and 1777','Band-style pieces following 17th-century patterns.',''),
 ('School sampler','late 17th–19th century','Schoolroom exercises with alphabets, verses and educational themes.',''),
 ('Map sampler','','Sampler with a map theme.',''),
 ('Mourning sampler','18th–19th century','Sampler mainly worked in cross stitch.','')])
A['Appliqué textile picture']=('Quilt',"Wikipedia's Quilt article (appliqué strand)",2,"appliqué is otherwise a technique; no complete list exists",[
 ('Broderie perse','','Appliqué of motifs cut from printed fabric and rearranged on a new ground.','')])
A['Paper cut']=('Papercutting',"Wikipedia's Papercutting article",14,"the page's Swedish Christmas papercutting is a seasonal decoration, not a picture",[
 ('Kirigami','','Japanese term for cut-paper work.',''),
 ('Vytynanky','','Ukrainian name for the Slavic layered paper cut.',''),
 ('Silhouette','1778 example','Outline or portrait cut from black paper; the page gives Goethe\'s 1778 silhouette.',''),
 ('Pabalat','','Filipino cut-paper wrapper for sweets.',''),
 ('Jewish papercut','','Eastern European and Israeli papercuts used for ketubot and mizrahs; revived in Israel in the 20th century.',''),
 ('Swiss papercutting','','Tradition especially associated with Pays-d\'Enhaut.','')])
A['Mosaic picture']=('Roman_mosaic',"Wikipedia's Roman mosaic article",10,"sites and named mosaics are works, not kinds",[
 ('Tessellated mosaic','from 3rd century BC','Mosaic built from tesserae, which replaced earlier pebble mosaics.','Opus tessellatum'),
 ('Pebble mosaic','5th–4th century BC','Earlier mosaic made from small pebbles.',''),
 ('Emblema','','Small separately made mosaic with a genre scene or still life, set in the centre of a larger panel.','Emblem'),
 ('Gold-ground wall mosaic','Late Antiquity','Style used in wall mosaics in grand churches.',''),
 ('Opus sectile panel','','Glass opus sectile panel named in the page references.','')])
# paintings
A['Persian and Indian miniature painting']=('Persian_miniature',"Wikipedia's Persian miniature article",30,"the article was read to character 100,000 of 154,447; individual manuscripts are works, not kinds. The Indian schools follow earlier fetched pages",[
 ('Ilkhanid miniature','13th–14th century','Illustrated manuscripts of the Ilkhanid court with Chinese and Christian influences.',''),
 ('Jalayirid miniature','c. 1330–1410','Lyrical, pastel, naturalistic style with Chinese-inspired landscapes.',''),
 ('Injuid and Muzaffarid Shiraz miniature','1331–c. 1390','Shiraz manuscript style of the Injuid and Muzaffarid periods.',''),
 ('Timurid Herat miniature','15th century','Herat school of classical restraint and elegance from the Timurid royal workshops.',''),
 ('Turkmen Tabriz miniature','late 15th century','Tabriz style, more expressive and imaginative than Herat.',''),
 ('Qajar illustrated manuscript','1853 example','Qajar-period manuscript illustration, as in the 1853 One Thousand and One Nights.','')])
A['Portrait miniature']=('Portrait_miniature',"Wikipedia's Portrait miniature article",34,"the page's schools named after individual miniaturists are makers, not kinds",[
 ('Vellum miniature','16th–17th century','Watercolour on stretched or thin vellum, an early support.',''),
 ('Playing-card miniature','16th century','Miniature painted on card backs, often with thin vellum mounted on them.',''),
 ('Oil-on-copper miniature','16th century','Method attributed to Italian or Dutch artists.',''),
 ('Ivory miniature','c. 1700','Watercolour on ivory, the standard 18th-century medium.',''),
 ('Mica-overlay miniature','1650s','Thin transparent mica sheets painted to disguise or dress the sitter.',''),
 ('Dressed miniature','late 18th century','Fabric, ribbon and lace attached to the image.',''),
 ('Locket and jewellery miniature','18th century','Miniature set into a locket, watch cover or other jewellery.',''),
 ('Snuff-box miniature','18th century','Miniature fitted into a snuff-box lid.',''),
 ('Mourning miniature','mid-18th century','Miniature set in rings, brooches or lockets to honour the deceased.',''),
 ('Betrothal miniature','1489 example','Miniature exchanged as a token of marriage alliance.','')])
A['Reverse glass painting']=('Reverse_glass_painting',"Wikipedia's Reverse glass painting article",18,"Kandinsky and the American painters are artist-led and sit with Visual Entertainment",[
 ('Byzantine icon on glass','Middle Ages','The most famous sacred form of the technique.',''),
 ('Venetian glass painting','Renaissance','Reverse glass painting that influenced Venetian Renaissance art.',''),
 ('Bavarian and Austrian folk glass painting','19th century','Widely popular folk art.','Hinterglasmalerei'),
 ('Bohemian and Moravian folk glass painting','19th century','Widely popular folk art.',''),
 ('Slovak folk glass painting','19th century','Widely popular folk art.',''),
 ('Romanian icon on glass','','Traditional Transylvanian style; the page marks the claim as needing a citation.',''),
 ('Japanese reverse glass painting','19th century','Spread from China in the Edo period.',''),
 ('Indian reverse glass painting','19th century','Popular in 19th-century India.',''),
 ('Clock-face painting','early to mid-19th century','Central European clock faces made with the technique.','')])
A['Aboriginal Australian painting']=('Contemporary_Indigenous_Australian_art',"Wikipedia's Contemporary Indigenous Australian art article",33,"the article was read to character 100,000 of 143,971; art centres and peak bodies are institutions, not kinds",[
 ('Papunya Tula painting','1971','Widely traced origin of contemporary acrylic painting; local men formed their own company.',''),
 ('Utopia painting','late 1980s to early 1990s','Style of the Utopia region, led by Emily Kngwarreye.',''),
 ('Balgo painting','1980s','Painting that spread from Papunya to Balgo, Western Australia.',''),
 ('Yuendumu painting','1980s','Painting from Yuendumu, Northern Territory, where Warlukurlangu Artists formed.',''),
 ('Ernabella acrylic design and batik','late 1950s','Acrylic poster designs that led to batik, from Australia\'s oldest Indigenous art centre.',''),
 ('Torres Strait printmaking','1990s','Linocut and etching from the Torres Strait Islands and north Queensland.',''),
 ('Pokerwork carving','','Significant carving medium in central Australian communities.','')])
A['Naive painting']=('Na%C3%AFve_art',"Wikipedia's Naïve art article",8,"museums named by the page are institutions, not kinds",[
 ('Saint Soleil painting','1970–1999','Haitian school named in the article navigation box.',''),
 ('Safed circle painting','late 19th to early 20th century','Naïve painting of Safed with Moshe Mizrahi Shah; Yitzhak Frenkel was influenced.','')])
A['Outsider art']=('Outsider_art',"Wikipedia's Outsider art article",9,"collections, fairs and journals named by the page are institutions, not kinds",[
 ('Visionary art','1945–1959','Works with spiritual or religious subject matter; also an umbrella term.',''),
 ('Neuve invention','','Dubuffet\'s term for marginal artists with some mainstream contact.','Art singulier'),
 ('Visionary environment','','Building or sculpture park made by an outsider artist.','')])
A['Korean folk painting']=('Minhwa',"Wikipedia's Minhwa article",19,"Gammo yeojaedo is named with no description and is omitted",[
 ('Morando','','Peony painting linked to ceremonies, marriage and royal events.',''),
 ('Yunhwa-do','','Lotus painting, often with fish, birds and insects.',''),
 ('Ssanghak pandodo','','Two cranes and peaches, a paradise tied to Korean Taoism.',''),
 ('Chochungdo','','Painting of flowers and insects.',''),
 ('Eohaedo','','Fish painting symbolising fertility, often placed in a bride\'s room.',''),
 ('Sipjangsaengdo','','Painting of the ten symbols of longevity.',''),
 ('Sogwado','','Vegetables and fruits symbolising continuation of the family line.',''),
 ('Yonghodo','','Painting of tigers and dragons to protect from misfortune.',''),
 ('Ilwolbusangdo','from 1392','Sun and moon over trees, made by royal court artists.','')])
A['Painted folding screen']=('Folding_screen',"Wikipedia's Folding screen article",18,"the rest are generic terms (Pingfeng, Byōbu), a kind elsewhere (Chaekgeori), single works (Torige ritsujo, Azuchi Screens) or architecture (Bình phong)",[
 ('Huaping','Tang dynasty','Chinese painted folding screen, on paper or silk.',''),
 ('Shuping','Tang dynasty','Chinese calligraphy folding screen.',''),
 ('Irworobongdo screen','Joseon dynasty','Korean screen placed behind thrones in royal throne rooms.',''),
 ('Chimbyeong','Joseon dynasty','Korean bedside screen.',''),
 ('Baeknapbyeong','Joseon dynasty','Korean screen decorated with drawings or writings.',''),
 ('Jangsaengdobyeong','Joseon dynasty','Korean screen depicting the ten symbols of longevity.',''),
 ('Sinseondobyeong','Joseon dynasty','Korean screen depicting gods under Taoist influence.',''),
 ('Sobyeong','Joseon dynasty','Plain white Korean screen used for mourning or ancestral rites.',''),
 ('Tiger and dragon screens','Azuchi-Momoyama','Japanese pair popular among feudal lords; example by Kanō Sanraku, 17th century.','')])
A['Retablo and ex-voto painting']=('Votive_paintings_of_Mexico',"Wikipedia's Votive paintings of Mexico article",3,"Milagro and New Mexico retablos are named without detail, and Santos and Ayacucho are not in the article",[
 ('Lámina retablo','','Mexican votive painting on a metal plate; lámina, retablo and ex-voto are used interchangeably.','')])
A['Indian folk painting']=('Madhubani_art',"Wikipedia's Madhubani art article",5,"Warli, Gond, Kalamkari, Phad and other folk styles are not on this page",[])
A['Ukiyo-e print']=('Glossary_of_ukiyo-e',"Wikipedia's Glossary of ukiyo-e",32,"print sizes (ōban, chūban and others) and orientation terms are attributes, not entries; surimono has its own kind",[
 ('Nishiki-e','','Multi-colour woodblock printing.',''),
 ('Benizuri-e','','Early prints in pink and green.',''),
 ('Beni-e and tan-e','','Early prints printed mainly in pink or red.',''),
 ('Urushi-e','','Prints that imitate the thick, dark look of black lacquer.',''),
 ('Aizuri-e','','Prints made with blue ink.',''),
 ('Sumizuri-e','','Monochrome prints in black ink only.',''),
 ('Ishizuri-e','','Prints imitating stone rubbings, with pale images on a dark ground.',''),
 ('Kirazuri','','Prints with mica powder for a sparkling effect.',''),
 ('Hashira-e','','Very narrow, tall pillar prints.',''),
 ('Uchiwa-e','','Prints made on paddle-shaped hand fans.',''),
 ('Kakemono-e','','Tall prints made as an ōban diptych stacked vertically.',''),
 ('Bijin-ga','','Prints of beautiful women.',''),
 ('Yakusha-e','','Prints of kabuki actors.',''),
 ('Musha-e','','Prints of warriors.',''),
 ('Kachō-ga','','Prints of flowers and birds.',''),
 ('Shunga','','Erotically themed prints.',''),
 ('Kuchi-e','','Frontispiece illustrations for books and magazines.',''),
 ('Komochi-e','','Prints with moveable parts.',''),
 ('Megane-e','','Prints viewed through a convex lens to give a three-dimensional effect.',''),
 ('Omocha-e','','Picture books and toys made for children.','')])
A['Vintage poster']=('Poster',"Wikipedia's Poster article",35,"poster sessions, wanted posters and affirmation posters are not collectable posters",[
 ('Chérette poster','from 1866','Chéret\'s lively, provocative female figures in bright colours with striking typography.',''),
 ('Maîtres de l\'Affiche','1895–1900','Chéret\'s French series of poster reproductions, now seen as an important publication.',''),
 ('Art Nouveau poster','','Stylised figures, especially of women, as by Grasset and Mucha.',''),
 ('Sachplakat','years before WWI','Simple German object-poster style later applied to the war effort.','Object poster'),
 ('Railway pictorial poster','from 1850s','Commissioned by railway companies, such as the Great Northern Railway\'s Jolly Fisherman of 1908.',''),
 ('Circus poster','from 1850s','Early mass-produced woodcuts, later chromolithographs.',''),
 ('Beach Town poster','1920s–1930s','Art Deco travel posters of American beach resorts.',''),
 ('Recruiting poster','WWI and WWII','"Lord Kitchener Wants You" in the UK and "Uncle Sam wants you" in the US.',''),
 ('Wartime propaganda poster','WWI and WWII','Persuasion posters from Germany, the USSR, the US and France.',''),
 ('May 1968 student poster','1968','French student posters, among the most acclaimed of the century.',''),
 ('Film poster','','Colourful poster whose rarest examples reach high prices; Metropolis (1927) sold for US$690,000 in 2005.',''),
 ('Pin-up poster','1920s onward','Images of attractive women, popular with soldiers in WWII.',''),
 ('Psychedelic gig poster','1960s','Hippie-era concert posters for venues such as the Fillmore and Avalon.',''),
 ('Blacklight poster','','Poster designed to fluoresce under ultraviolet light.','')])
A['Exhibition and art poster']=('Poster',"Wikipedia's Poster article",35,"see Vintage poster for the other poster entries",[
 ('Commemorative sporting poster','1948 example','Olympic and World Cup posters; Paris 2024 medallists received one.',''),
 ('Concert poster','','Custom-designed poster that often becomes a collector\'s item.','')])
# sculpture
A['Bronze sculpture']=('Sculpture',"Wikipedia's Sculpture article",60,"the article was read to character 300,000 of 407,686; the rest is history and regional surveys",[
 ('Cabinet bronze','','Small bronze for collectors\' cabinets.',''),
 ('Plaquette','','Small cast relief plaque in metal.',''),
 ('Portrait medal','','Small cast portrait medal, invented by Pisanello.',''),
 ('Aquamanile','','Animal-shaped metal water vessel, often brass.',''),
 ('Brass sculpture','','Used for the Liège font and many aquamaniles.','')])
A['Stone carving']=('Sculpture',"Wikipedia's Sculpture article",60,"the rest are monuments and architecture",[
 ('Nottingham alabaster relief','','Altar reliefs exported across Europe.',''),
 ('Porphyry carving','','Hard stone used for the Four Tetrarchs.',''),
 ('Soapstone carving','','Zimbabwe Birds and modern Zimbabwean carving.',''),
 ('Sandstone carving','','Mathura sculptures and Meroitic reliefs.','')])
A['Terracotta sculpture']=('Sculpture',"Wikipedia's Sculpture article",60,"funerary forms (Terracotta Army, shabti) are tomb goods",[
 ('Sancai tomb figure','Tang','Three-colour glazed pottery figure for Tang tombs.',''),
 ('Dogū','Jōmon','Stylised Japanese pottery figure.',''),
 ('Haniwa','Kofun','Japanese terracotta funerary figures placed outside tombs.','')])
A['Ivory and bone carving']=('Sculpture',"Wikipedia's Sculpture article",60,"the rest are monuments",[
 ('Netsuke','','Small carved toggle for Japanese garments.','')])
A['Jade carving']=('Sculpture',"Wikipedia's Sculpture article",60,"the rest are monuments",[
 ('Mughal jade dagger hilt','','Carved jade hilt of the Mughal period.','')])
A['African mask']=('Traditional_African_masks',"Wikipedia's Traditional African masks article",30,"the Makurian dancing mask, Makonde ndimu ornaments and unspecified photographed examples are omitted",[
 ('Sowei mask','','Helmet mask of the Mende and Vai (Sande society) in Sierra Leone, worn by women in initiation.','Sande helmet mask'),
 ('Plank mask','','Bwa, Bobo and Mossi mask of Burkina Faso, linked to water spirits.','Nwantantay'),
 ('Kifwebe mask','','Songye mask with striped patterns mixing animal traits.',''),
 ('Chiwara headdress','','Bambara antelope headdress of Mali.',''),
 ('Dogon mask','','Dogon masks of Mali; Griaule recorded at least 78 types.',''),
 ('Senufo mask','','Senufo mask of the Ivory Coast, including Poro society masks.',''),
 ('Bwa hawk mask','','Bwa and Buna mask whose beak shape identifies the group.',''),
 ('Kuba mask','','Mwaash ambooy and mgady amwaash of the Kuba Kingdom.',''),
 ('Mwana pwo','','Chokwe female ancestor mask; the male variant is cihongo.',''),
 ('Ngil mask','','Fang kaolin-coloured mask used in night masquerades.',''),
 ('Idia mask','','Benin mask commissioned by King Esigie in memory of his mother.',''),
 ('Ndeemba mask','','Yaka skull-shaped ancestor mask.',''),
 ('Grebo mask','','Grebo mask of the Ivory Coast.',''),
 ('Passport mask','','Personal protective miniature mask of West Africa.','Miniature mask')])
A['Pre-Columbian figure']=('Pre-Columbian_art',"Wikipedia's Pre-Columbian art article",27,"cultures with no sculpture described on the page (Colima, Nayarit and Jalisco, Chancay, Valdivia, Tolita, Taíno, Tairona, Quimbaya) are added only as names; the page was read to character 100,000 of 104,572",[
 ('Olmec jade figure','c. 1200–400 BCE','Jade figurines and colossal heads from the Gulf Coast.',''),
 ('Maya relief','Classic, c. 200–900 CE','Relief and stelae of Copán, Palenque and Bonampak.',''),
 ('Aztec stone carving','c. 900–1580 CE','Life-sized ceramics and carved stone sculpture.',''),
 ('Zapotec mosaic mask','','Mosaic jade mask of a bat god found in a tomb.',''),
 ('Mixtec gold and turquoise pectoral','post-classic','Mixtec-Puebla work in codices, murals and metal.',''),
 ('Toltec column','10th–12th century','Colossal block-like columns and sculpture from Tula.',''),
 ('Chavín stela','c. 1000–300 BCE','Carved stelae and obelisks with jaguar motifs.',''),
 ('Nazca polychrome ceramic','c. 200 CE to mid-8th century','Polychrome ceramics with increasingly abstract figures.',''),
 ('Wari ceramic','late 1st millennium','Large ceramics showing the Staff God.',''),
 ('Chimú metalwork','early 2nd millennium','Gold and silver portrait and decorative works.',''),
 ('Lambayeque funerary mask','','Funerary mask and ceremonial tumi knife.',''),
 ('Western Mexico figure (Nayarit and Jalisco)','','Named in the page navigation list; the page gives no description.','')])
A['Staffordshire figure']=('Staffordshire_figure',"Wikipedia's Staffordshire figure article",28,"the article names potters and subject categories; only the figure types are entries",[
 ('Pratt ware figure','c. 1780–1840','Colours applied to the biscuit body, then covered with clear lead glaze.',''),
 ('Whieldon-type figure','1750s','Imitation of Thomas Whieldon\'s tortoiseshell ware.',''),
 ('Arbour group','c. 1750','Two lovers seated before a bocage of foliage.',''),
 ('Pew group','c. 1745','Figures on a high-backed bench in a home or inn.',''),
 ('Bocage group','c. 1800–1860s','Figures set against a foliage backdrop.',''),
 ('Demosthenes figure','c. 1785','Enoch Wood model of the Greek orator.',''),
 ('Medici lion','c. 1780; c. 1820','Lion figure in coloured glazes or painted enamels over lead glaze.',''),
 ('Tithe pig group','1825–1830','Satirical clergy figure in pearlware.',''),
 ('Vicar and Moses','18th–19th century','Clergy satire derived from Hogarth\'s print The Sleeping Congregation (1736).',''),
 ('Staffordshire spill vase','c. 1855–1860','Vase-form figure such as the Mazeppa piece.',''),
 ('Equestrian figure','','Horse-and-rider figure, often about ten inches tall.',''),
 ('Dandy and Dandizette','1825–1830','Genteel couple genre figures.','')])
A['Collectible giftware figurine']=('Lladr%C3%B3',"Wikipedia's Lladró and Hummel figurines articles",16,"Privilege, Collectors' Society and museum items are programmes, not figurines",[
 ('Merry Wanderer','','Hummel figure; a life-size reproduction stands at the Goebel entrance in Rödental.',''),
 ('Little Pals','1985','First annual sculpture of the Lladró Collectors\' Society.',''),
 ('Guitar Girl','','Classic Lladró figurine shown in the article.',''),
 ('Fisherboy 4809','','Lladró figurine, reference 4809, shown in the article.','')])
