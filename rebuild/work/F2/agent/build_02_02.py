import json, os
W='https://en.wikipedia.org/wiki/'
GL=W+'Glossary_of_ukiyo-e'; TK=W+'The_Fifty-three_Stations_of_the_T%C5%8Dkaid%C5%8D'; SO=W+'S%C5%8Dsaku-hanga'
SH=W+'Sharaku'; ED=W+'One_Hundred_Famous_Views_of_Edo'
FJ='https://www.arc.ritsumei.ac.jp/artwiki/index.php/Fugaku_sanjûrokkei'
GW='https://www.britishmuseum.org/collection/object/A_2008-3008-1'
UT='https://www.britishmuseum.org/collection/object/A_1945-1101-0-19'
CL='https://www.clarkart.edu/microsites/competing-currents-20th-century-japanese-prints/print-making-movements/shin-hanga'
JT='https://japantimes.co.jp/culture/2022/06/17/arts/shin-hanga-ukiyo-e'
HO='https://honolulumuseum.org/beyond-onchi-creative-prints-by-munakata-shiko-ydsl'
SU='https://projects.mcah.columbia.edu/jaanus/node/900'
kinds=[
 {"n":"Ukiyo-e print","a":"nishiki-e · Japanese woodblock print","d":"An Edo-period colour woodblock print designed by an artist, cut by a carver and printed by a printer for a commercial publisher.",
  "t":["ōban","chūban","hosoban","aiban","ōban yoko-e (horizontal)","triptych","bijin-ga (beautiful women)","yakusha-e (actor prints)","landscape and famous places (meisho)","aizuri (blue print)","mica ground","bokashi gradation","karazuri embossing","early impression","late impression","re-carved reproduction"],
  "s":GL,
  "x":[
   {"n":"Hokusai Thirty-six Views of Mount Fuji","a":"Fugaku sanjūrokkei","d":"Hokusai's landscape series of Mount Fuji, begun as blue prints in Prussian blue and extended to 46 sheets.","mk":"Katsushika Hokusai","y":"1831–1833","s":FJ,
    "v":[{"n":"First five prints, all-blue impressions","mk":"Katsushika Hokusai","y":"1831","d":"early impressions printed entirely in blue"},
         {"n":"Under the Wave off Kanagawa ('The Great Wave')","mk":"Katsushika Hokusai","y":"c. late 1831","d":"signed Hokusai aratame Iitsu hitsu; ōban yoko-e; British Museum holds three impressions"},
         {"n":"Fuji in Clear Weather","mk":"Katsushika Hokusai","y":"c. late 1831","d":""},
         {"n":"Supplementary ten prints","mk":"Katsushika Hokusai","y":"c. early 1833","d":"signed Zen Hokusai Iitsu hitsu"}],
    "dt":"early or late impression · fading · signature form · kiwame censor seal · Eijudō publisher seal · margins"},
   {"n":"Hiroshige Fifty-three Stations of the Tōkaidō (Hōeidō)","a":"Hōeidō Tōkaidō","d":"Hiroshige's best-known and best-selling series of the post stations between Edo and Kyoto.","mk":"Utagawa Hiroshige","y":"1833–1834","s":TK,
    "v":[{"n":"First print, joint issue","mk":"Hōeidō","y":"1833","d":"published with Senkakudō; later prints by Hōeidō alone"},
         {"n":"Shōno (sudden rain)","mk":"Utagawa Hiroshige","y":"1833–34","d":"among the most famous of the series"},
         {"n":"Kanbara (village in snow)","mk":"Utagawa Hiroshige","y":"1833–34","d":""},
         {"n":"Nihonbashi, second edition","mk":"Hōeidō","y":"","d":"later edition with changes"}],
    "dt":"55 sheets (53 stations plus start and end) · edition · colour and bokashi · condition"},
   {"n":"Hiroshige One Hundred Famous Views of Edo","a":"Meisho Edo hyakkei","d":"Hiroshige's late series of 119 vertical views of Edo, completed by Hiroshige II.","mk":"Utagawa Hiroshige","y":"1856–1859","s":ED,
    "v":[{"n":"No. 30 Plum Park in Kameido","mk":"Utagawa Hiroshige","y":"","d":"copied by Van Gogh"},
         {"n":"No. 58 Sudden Shower over Shin-Ōhashi Bridge and Atake","mk":"Utagawa Hiroshige","y":"","d":"copied by Van Gogh"}],
    "dt":"date seal · publisher (Sakanaya Eikichi) · early or late impression"},
   {"n":"Utamaro bijin-ga half-length portrait","a":"bijin ōkubi-e","d":"A close-up picture of a beautiful woman, the genre Utamaro made his own.","mk":"Kitagawa Utamaro","y":"1790s–1800s","s":UT,
    "v":[{"n":"Fujin sōgaku jittai (Ten Types in the Physiognomic Study of Women)","mk":"Kitagawa Utamaro","y":"1802–1803","d":"Kyōwa-era set; British Museum"}],
    "dt":"series · format · mica ground · publisher · condition"},
   {"n":"Sharaku actor portrait","a":"Sharaku yakusha-e","d":"A kabuki actor print by the mysterious Sharaku, active for about ten months in 1794–95.","mk":"Sharaku","y":"1794–1795","s":SH,
    "v":[{"n":"First-period ōkubi-e on black mica","mk":"Sharaku","y":"1794","d":"28 ōban; signed Tōshūsai Sharaku"},
         {"n":"Ōtani Oniji III as Yakko Edobei","mk":"Sharaku","y":"1794","d":"first period"},
         {"n":"Arashi Ryūzō I as Ishibe Kinkichi","mk":"Sharaku","y":"1794","d":"€389,000 at Piasa, Paris, 2009"},
         {"n":"Later-period hosoban and aiban","mk":"Sharaku","y":"1794–1795","d":"signed Sharaku"}],
    "dt":"period · format · mica ground · actor and role"},
   {"n":"Re-carved ukiyo-e reproduction","a":"fukkoku · Watanabe reprint","d":"A 20th-century reproduction of a classic ukiyo-e design, re-carved and printed by hand.","mk":"Watanabe Shōzaburō","y":"20th century","s":JT,
    "v":[{"n":"Reproductions of Hiroshige and Utamaro","mk":"Watanabe Shōzaburō","y":"","d":""}],
    "dt":"publisher seal · paper · date of printing"}]},
 {"n":"Shin-hanga print","a":"new prints","d":"A 20th-century Japanese woodblock print made in the ukiyo-e way by artist, carver and printer under a publisher.",
  "t":["landscape","bijin-ga","kachō-e (birds and flowers)","pre-war or post-war printing","publisher seal"],
  "s":CL,
  "x":[
   {"n":"Watanabe shin-hanga","a":"","d":"A shin-hanga print issued by Watanabe Shōzaburō, the movement's leading publisher, with offices in Japan and London.","mk":"Watanabe Shōzaburō","y":"1910s onward","s":CL,
    "v":[{"n":"Zōjōji Temple, Shiba","mk":"Kawase Hasui","y":"1925","d":"Clark Art Institute"},
         {"n":"Prints with Ito Shinsui","mk":"Ito Shinsui","y":"","d":"Watanabe collaborator"},
         {"n":"Lyrical landscapes","mk":"Tsuchiya Koitsu","y":"","d":""}],
    "dt":"seal (early or later printing) · edition · condition"},
   {"n":"Yoshida street and landscape print","a":"","d":"A shin-hanga print by Yoshida Hiroshi, including dusk-shrouded street scenes.","mk":"Yoshida Hiroshi","y":"20th century","s":CL,
    "dt":"title · jizuri seal · lifetime or posthumous printing"}]},
 {"n":"Sōsaku-hanga print","a":"creative print","d":"A 20th-century Japanese print drawn, carved and printed by the artist as personal expression.",
  "t":["woodblock","abstract","figurative","self-printed (jizuri)","edition size"],
  "s":SO,
  "x":[
   {"n":"Self-carved creative print","a":"jiga · jikoku · jizuri","d":"A print that the artist drew, carved and printed alone, the founding ideal of the movement.","mk":"Kanae Yamamoto","y":"1904 onward","s":SO,
    "v":[{"n":"Fisherman (Gyofu)","mk":"Kanae Yamamoto","y":"1904","d":"published in the magazine Myōjō"},
         {"n":"Portrait of Hagiwara Sakutarō","mk":"Kōshirō Onchi","y":"1943","d":""},
         {"n":"Tokyo Shinsai Ato Fukei","mk":"Un'ichi Hiratsuka","y":"","d":"published by Hanga no Ie"}],
    "dt":"artist · edition · signature and seal · paper"},
   {"n":"Munakata woodblock","a":"","d":"Munakata's woodcuts, carved without preparatory sketches, often on Buddhist themes.","mk":"Shikō Munakata","y":"mid-20th century","s":HO,
    "v":[{"n":"Two Bodhisattvas and Ten Great Disciples of Sakyamuni","mk":"Shikō Munakata","y":"","d":""},
         {"n":"Self-portrait","mk":"Shikō Munakata","y":"1960","d":"ink on paper; Honolulu Museum of Art"}],
    "dt":"title · hand colouring · signature · edition"}]},
 {"n":"Surimono","a":"","d":"A privately commissioned Japanese woodblock print, often a New Year greeting with a poem, made to the highest standard.",
  "t":["shikishiban (square)","yokonagaban (large, folded)","kyōka surimono","haiku surimono","saitan (New Year) surimono","embossing","metal pigments"],
  "s":SU,
  "x":[
   {"n":"Kyōka surimono","a":"","d":"A surimono commissioned by a poetry circle to carry its comic 31-syllable kyōka verses.","mk":"","y":"1785–1830s","s":SU,
    "v":[{"n":"Surimono","mk":"Katsushika Hokusai","y":"","d":"among the finest"},
         {"n":"Surimono","mk":"Totoya Hokkei","y":"","d":"Hokusai pupil"},
         {"n":"Surimono","mk":"Kubo Shunman","y":"","d":""},
         {"n":"Surimono","mk":"Yashima Gakutei","y":"","d":""}],
    "dt":"format · poems and poets · embossing and metallic pigments · condition"},
   {"n":"Saitan surimono","a":"New Year surimono","d":"A privately commissioned New Year greeting print, popular after 1790.","mk":"","y":"after 1790","s":SU,
    "dt":"format · year sign · poems"}]}]
def B(n,c,seg,kf,d,s,sig): return {"n":n,"c":"Japan","f":"","seg":seg,"kf":kf,"d":d,"s":s,"sig":sig}
A="Artisan & independent"
brands=[
 B("Katsushika Hokusai","",A,"landscape prints, surimono","Edo ukiyo-e designer of the Thirty-six Views of Mount Fuji.",FJ,["Hokusai Thirty-six Views of Mount Fuji"]),
 B("Utagawa Hiroshige","",A,"landscape prints","Edo ukiyo-e designer of the Tōkaidō and Edo view series.",TK,["Hiroshige Fifty-three Stations of the Tōkaidō (Hōeidō)","Hiroshige One Hundred Famous Views of Edo"]),
 B("Kitagawa Utamaro","",A,"bijin-ga","Ukiyo-e designer known for pictures of beautiful women.",UT,["Utamaro bijin-ga half-length portrait"]),
 B("Sharaku","",A,"actor prints","Ukiyo-e designer of kabuki actor portraits, active 1794–95.",SH,["Sharaku actor portrait"]),
 B("Watanabe Shōzaburō","","Specialist","shin-hanga publishing","Tokyo print publisher (1885–1962) who led the shin-hanga movement and issued ukiyo-e reproductions.",JT,["Watanabe shin-hanga","Re-carved ukiyo-e reproduction"]),
 B("Yoshida Hiroshi","",A,"shin-hanga landscapes","Japanese printmaker of landscapes and street scenes.",CL,["Yoshida street and landscape print"]),
 B("Kanae Yamamoto","",A,"creative prints","Japanese printmaker whose Fisherman (1904) is taken as the start of sōsaku-hanga.",SO,["Self-carved creative print"]),
 B("Shikō Munakata","",A,"woodcuts","Sōsaku-hanga printmaker (1903–1975) of Buddhist-themed woodcuts.",HO,["Munakata woodblock"]),
 B("Nishimuraya Yohachi","","Specialist","ukiyo-e publishing","Edo publisher (Eijudō) of Hokusai's Thirty-six Views of Mount Fuji.",FJ,[]),
 B("Hōeidō","","Specialist","ukiyo-e publishing","Edo publisher of Hiroshige's Fifty-three Stations of the Tōkaidō.",TK,[]),
]
for b in brands: b["c"]="Japan"
trads=[{"n":"Ukiyo-e","g":"Paper & print","r":"Japan (Edo, now Tokyo)","p":"Edo period, 17th–19th century",
 "d":"Commercial colour woodblock prints of actors, beauties and famous places, produced by a publisher with designer, carver and printer.",
 "tech":"multi-block colour woodblock printing (nishiki-e) with bokashi gradation, embossing and mica",
 "mat":"wood blocks, paper, pigments including Prussian blue",
 "forms":["Ukiyo-e print","Surimono","Shin-hanga print"],
 "ctr":["Eijudō (Nishimuraya Yohachi)","Hōeidō","Katsushika Hokusai","Utagawa Hiroshige","Kitagawa Utamaro","Sharaku"],
 "auth":"censor seals (kiwame and others, 1790–1876) and publisher seals date a print; early impressions have crisp lines and intended colours, late ones worn blocks and changed colours; 20th-century re-carved reproductions exist","s":GL}]
out={"kinds":kinds,"brands":brands,"traditions":trads,
 "notes":"Four new kinds, all sourced. Utamaro version is the Kyōwa-era (1802–03) physiognomy set from the fetched BM record; the Tsutaya 1792–93 set was not fetched. Hiroshi Yoshida not tied to Watanabe on any fetched page, so given his own archetype. Ito Shinsui's bijin-ga works not named on a fetched page. Individual dates for 100 Views plates 30 and 58 left blank (not stated on the fetched page). Firecrawl credits reported low."}
p='work/F2/shelves/02_02.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
