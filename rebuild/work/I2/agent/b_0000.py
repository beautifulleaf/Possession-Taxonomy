import sys; sys.path.insert(0,'work/I2/agent')
from put import put
W='https://en.wikipedia.org/wiki/'
def A(n,mk,y,s,d,v=(),a='',dt=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":W+s,"v":[dict(n=i[0],mk=i[1],y=i[2],d=i[3]) for i in v]}
    if dt: x["dt"]=dt
    return x
sans=[
A("Helvetica","Haas Type Foundry","1957","Helvetica","Neo-grotesque by Max Miedinger, first issued as Neue Haas Grotesk; the reference Swiss sans.",[
 ("Neue Haas Grotesk (original)","Haas Type Foundry","1957","Name until the 1959-61 renaming for Linotype"),
 ("Neue Helvetica / Helvetica Neue","Linotype","1983","Redesign by Stempel; nine weights, four widths"),
 ("Neue Haas Grotesk digital","Commercial Type","2010","Christian Schwartz; Text and Display optical sizes"),
 ("Helvetica Now","Monotype","2019","Micro, Text, Display sizes; variable font 2021")],"","weights hairline to extra black · widths compressed to extended · optical sizes Micro/Text/Display · variable weight, width, optical size"),
A("Akzidenz-Grotesk","Berthold","1898","Akzidenz-Grotesk","Berlin grotesque that Helvetica was modelled on; the Swiss post-war favourite.",[
 ("Akzidenz-Grotesk Old Face","Berthold","1984","Günter Gerhard Lange; keeps metal-type irregularities"),
 ("Akzidenz-Grotesk Next","Berthold","2006","Bernd Möllenstädt and Dieter Hofrichter; evened weights and x-heights")]),
A("Univers","Deberny & Peignot","1957","Univers","Adrian Frutiger's neo-grotesque, launched with a full weight-and-width system.",[
 ("Linotype Univers","Linotype","1997","Frutiger's revision, 63 fonts, three-digit numbering"),
 ("Univers Next","Linotype","2010","True small caps added")],"","21 original weight/width cuts · numbering system encodes weight, width, posture"),
A("Frutiger","Adrian Frutiger","1976","Frutiger_(typeface)","Humanist sans from Roissy airport signage, made for legibility at distance.",[
 ("Frutiger Next","Linotype","2000","Six weights with true italics"),
 ("Neue Frutiger","Linotype","2009","Frutiger with Akira Kobayashi; ten weights"),
 ("Neue Frutiger World","Monotype","2018","Over 150 languages across many scripts"),
 ("Frutiger Serif","Linotype","2008","Re-envisioned Méridien")]),
A("Futura","Bauersche Gießerei","1927","Futura_(typeface)","Paul Renner's geometric sans, 'the typeface of our time'.",[
 ("Architype Renner","The Foundry","1993","Keeps Renner's experimental alternates"),
 ("Futura ND","Neufville Digital","1999","Marie-Thérèse Koreman redesign"),
 ("Futura PT","ParaType","1995","Expanded to seven weights with Cyrillic"),
 ("Futura Next","Bauersche Gießerei","2016","Koreman; 20 fonts, 6 weights, 2 widths"),
 ("Futura Now","Monotype","2020","Redigitised from Renner's design, 102 added styles"),
 ("Formera","Bastien Sozoo","2011","Free, SIL OFL, based on 1927 metal type")]),
A("Gill Sans","Monotype","1928","Gill_Sans","Eric Gill's humanist sans for Monotype, drawing on Johnston's Underground lettering.",[
 ("Gill Kayo","Monotype","1936","Extremely bold, often sold as Ultra Bold"),
 ("Gill Sans Heavy","Monotype","1993","Issued with a book weight"),
 ("Gill Sans Nova","Monotype","2015","George Ryan; alternates and an ultra-light weight"),
 ("Gill Sans Infant","Monotype","","Single-storey a and g"),
 ("Gill Sans MT","Monotype","","Monotype's standard desktop release")]),
A("Gotham","Hoefler & Co.","2002","Gotham_(typeface)","Geometric sans from New York signage lettering by Tobias Frere-Jones with Jesse Ragan.",[
 ("Gotham Rounded","Hoefler & Co.","2007","Commissioned by Print magazine"),
 ("Gotham Narrow and Extra Narrow","Hoefler & Co.","2009","Added widths")],"","eight weights, four widths"),
A("Roboto","Google","2012","Roboto","Android's in-house UI sans by Christian Robertson, with serif, slab and mono relatives.",[
 ("Roboto Slab","Google","2013","Christian Robertson; variable weight 100-900"),
 ("Roboto Mono","Google","2015","Monospace relative"),
 ("Roboto Serif","Google","2022","Greg Gazdowicz of Commercial Type; four axes"),
 ("Roboto Flex","Google","","Variable font with 12 axes")]),
A("Inter","Rasmus Andersson","2017","Inter_(typeface)","Open-source neo-grotesque for screen UI text, built at Figma.",[
 ("Inter 4.1","Rasmus Andersson","2024","Latest release listed on Wikipedia; weight and optical-size axes")],"","variable weight Thin-Black · optical size axis · SIL OFL"),
]
serif=[
A("Garamond","Claude Garamond","16th century","Garamond","Old-style roman named for Claude Garamont; many 'Garamonds' actually follow Jean Jannon.",[
 ("Monotype Garamond","Monotype","1922","Revives Jean Jannon's work"),
 ("Stempel Garamond","Stempel","1925","Based on Garamond's roman and Granjon's italics"),
 ("Sabon","Jan Tschichold","1967","Designed 1964; for Linotype, Monotype and Stempel"),
 ("Adobe Garamond","Adobe","1989","Robert Slimbach; modernised interpretation"),
 ("Garamond Premier","Adobe","2005","Robert Slimbach; optical sizes, Greek and Cyrillic"),
 ("EB Garamond","Georg Duffner","2011","Open-source; later continued by Octavio Pardo")],"","optical sizes · italics from Granjon · small caps and swash")
,
A("Caslon","William Caslon I","1725","Caslon","William Caslon's London old-style, revived repeatedly since the 1840s.",[
 ("Adobe Caslon","Adobe","1990","Carol Twombly"),
 ("Big Caslon","Carter & Cone","1994","Matthew Carter; display sizes"),
 ("ITC Founder's Caslon","ITC","1998","Digitised by Justin Howes"),
 ("King's Caslon","Dalton Maag","2007",""),
 ("Williams Caslon Text","Font Bureau","2010","William Berkson")]),
A("Baskerville","John Baskerville","1757","Baskerville","Transitional serif by John Baskerville, punches cut by John Handy.",[
 ("Monotype Baskerville","Monotype","1923","Hot-metal version; installed with macOS"),
 ("Mrs Eaves","Emigre","1996","Zuzana Licko; low x-height, many ligatures"),
 ("Berthold Baskerville","Berthold","","Günter Gerhard Lange with Dieter Hofrichter, around 1980"),
 ("Libre Baskerville","Impallari Type","","Pablo Impallari; open-source web revival")]),
A("Bodoni","Giambattista Bodoni","1790","Bodoni","Didone with strong thick-thin contrast, revived many times from 1909.",[
 ("ATF Bodoni","American Type Founders","1909","Morris Fuller Benton"),
 ("Bauer Bodoni","Bauer Type Foundry","1926","Heinrich Jost; extreme contrast"),
 ("Poster Bodoni","Ludlow","1929","Chauncey H. Griffith; poster variant"),
 ("ITC Bodoni","ITC","","Sumner Stone; sizes 6, 12 and 72 pt")],"","optical sizes matter: hairlines dazzle at text size"),
A("Times New Roman","Monotype","1931","Times_New_Roman","Newspaper serif directed by Stanley Morison with Victor Lardent for The Times.",[
 ("Times Europa","The Times","1972","Walter Tracy; sturdier for fast presses"),
 ("Liberation Serif","Red Hat","2007","Steve Matteson; metric-compatible, open"),
 ("Tinos","Google","","Derivative of Liberation Serif")]),
]
slab=[
A("Rockwell","Monotype","1934","Rockwell_(typeface)","Geometric monoline slab serif supervised by Frank Hinman Pierpont, based on Litho Antique."),
A("Clarendon","Thorowgood & Co.","1845","Clarendon_(typeface)","Robert Besley's bold-companion slab, the origin of the Clarendon style.",[
 ("Eidenbenz Clarendon","Haas","1953","Hermann Eidenbenz"),
 ("New Clarendon","Monotype","1960","Redesign"),
 ("Belizio","Font Bureau","1998","David Berlow"),
 ("Sentinel","Hoefler & Co.","2009","")]),
]
kinds=[
 {"n":"Sans-serif typeface","a":"typeface · font family · grotesque · gothic","d":"A letterform family without serifs, kept as font files under a licence.","t":["Grotesque","Neo-grotesque","Geometric","Humanist"],"s":"https://myfonts.com/collections/miedinger-font-canada-type","x":sans,
  "m":[["Prompt","Cadson Demak"],["Miedinger","Canada Type"],["Lato","Google"],["Montserrat","Google"],["Open Sans","Google"],["Oswald","Google"],["Proxima Nova","Mark Simonson Studio"]]},
 {"n":"Serif typeface","a":"roman text face","d":"A family with serifs, used for book and text setting.","t":["Old-style","Transitional","Didone"],"s":W+"Garamond","x":serif,
  "m":[["FF Atma Serif","FontFont"],["Bell",""]]},
 {"n":"Slab-serif typeface","a":"Egyptian · mechanistic","d":"A family with heavy rectangular serifs and little stroke contrast.","t":["Clarendon","Geometric slab"],"s":W+"Rockwell_(typeface)","x":slab},
 {"n":"Script and handwriting typeface","a":"calligraphic · brush","d":"A family imitating pen, brush or hand lettering with joined or flowing forms.","t":["Calligraphic","Brush","Casual handwriting"],"s":W+"Zapfino","x":[
  A("Zapfino","Linotype","1998","Zapfino","Hermann Zapf's calligraphic script built on ligatures and variant forms.",[
   ("Zapfino Extra","Linotype","2003","With Akira Kobayashi; OpenType and AAT"),
   ("Zapfino Extra W1G","Linotype","2010","Adds Greek and Cyrillic"),
   ("Zapfino Arabic","Monotype","2014","Nadine Chahine; Naskh and Nastaaliq styles")])]},
 {"n":"Display and decorative typeface","a":"headline face · poster type","d":"A family made for large sizes and impact rather than continuous reading.","t":["Poster","Stencil","Decorative","Inline and shadow"],"s":W+"List_of_display_typefaces"},
 {"n":"Monospaced and coding typeface","a":"fixed-width · programming font","d":"A family where every glyph has the same advance width, for typewriting and code.","t":["Typewriter slab","Programming with ligatures","Terminal bitmap-style"],"s":W+"List_of_monospaced_typefaces","x":[
  A("Courier","IBM","1955","Courier_(typeface)","Howard Kettler's monospaced slab for IBM typewriters, the screenplay standard.",[
   ("Courier New","Monotype","","Windows system version"),
   ("Courier Prime","Quote-Unquote Apps","2013","Alan Dague-Greene; SIL OFL"),
   ("Courier 10 Pitch BT","Bitstream","","Common Linux default Courier")])],
  "m":[["Source Code Pro","Paul D. Hunt"],["Consolas","Lucas de Groot"],["Menlo","Jim Lyles"],["Fira Code","Nikita Prokopov"],["Inconsolata","Raph Levien"],["Iosevka","Belleve Invis"]]},
 {"n":"Blackletter typeface","a":"Gothic type · Fraktur · Textura","d":"A family based on dense, angular medieval German and Gothic hands.","t":["Textura","Rotunda","Schwabacher","Fraktur"],"s":W+"Fraktur","x":[
  A("Fraktur","","16th century","Fraktur","German blackletter that replaced Schwabacher in print.",[
   ("Fette Fraktur","Bauer","1850","Bold Fraktur"),
   ("Walbaum-Fraktur","","1800","Fraktur in the Walbaum manner"),
   ("Humboldtfraktur","Hiero Rhode","1938","")])]},
 {"n":"Non-Latin script typeface","a":"CJK font · Arabic font · Indic font","d":"A family for a writing system other than Latin, or covering many scripts at once.","t":["CJK (Chinese, Japanese, Korean)","Arabic and Nastaliq","Indic scripts","Greek and Cyrillic","Pan-script"],"s":W+"List_of_CJK_fonts","x":[
  A("Noto","Google","2013","Noto_fonts","Google's open pan-script family aiming for no tofu; 162 of 168 Unicode 16.0 scripts.",[
   ("Noto Sans / Noto Serif","Google","2013","Latin, Greek and Cyrillic base, from Droid and Open Sans"),
   ("Noto CJK (Source Han)","Google","","Developed with Adobe; SC, TC, JP, KR, HK variants"),
   ("Noto Color Emoji","Google","","OpenType CBDT colour format")],"","SIL OFL since 2015 · variable weight Thin-Black · OTC bundles")],
  "r":[["Noto","Google"]],
  "m":[["Hiragino Mincho","SCREEN Graphic Solutions"],["Kozuka Mincho","Adobe"],["RyuMin","Morisawa"],["YuMincho","Jiyu-Kobo"],["Nanum Myeongjo","Naver"]]},
 {"n":"Icon and symbol font","a":"dingbats · glyph font","d":"A font whose glyphs are symbols, ornaments or icons rather than letters.","t":["Dingbats","Web icon font","Colour emoji font"],"s":W+"Zapf_Dingbats","x":[
  A("Zapf Dingbats","Hermann Zapf","1978","Zapf_Dingbats","ITC symbol and ornament font; a subset of 360 from over 1,200 sketches, basis of the Unicode Dingbats block.",[
   ("ITC Zapf Dingbats Std","Adobe","","OpenType with 204 glyphs"),
   ("Zapf Essentials","ITC","","Later update with 372 glyphs")])]},
]
def B(n,c,f,seg,kf,d,s='knowledge'): return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s}
brands=[
 B("Monotype","United States","","Professional & flagship","type library","Largest commercial type library; owns Linotype, Hoefler & Co. and the Helvetica rights."),
 B("Linotype","Germany","","Professional & flagship","type library","Typesetting company whose library (Helvetica, Frutiger, Univers) is now owned by Monotype."),
 B("Adobe","United States","1982","Professional & flagship","Adobe Originals","Software maker with an in-house type programme (Garamond, Caslon)."),
 B("Hoefler & Co.","United States","1989","Premium","Gotham, Whitney","New York foundry founded by Jonathan Hoefler; acquired by Monotype in 2021.","https://en.wikipedia.org/wiki/Hoefler_&_Co."),
 B("Commercial Type","United States","2007","Premium","editorial type","Foundry of Christian Schwartz and Paul Barnes."),
 B("Klim","New Zealand","","Artisan & independent","independent foundry","Independent foundry led by Kris Sowersby."),
 B("Dalton Maag","United Kingdom","1991","Premium","brand typefaces","London studio making corporate and retail families."),
 B("Grilli Type","Switzerland","","Artisan & independent","contemporary sans","Independent Swiss foundry."),
 B("Colophon","United Kingdom","","Artisan & independent","independent foundry","Independent London foundry."),
 B("Emigre","United States","1984","Artisan & independent","digital-era experiments","Foundry of Zuzana Licko and Rudy VanderLans (Mrs Eaves)."),
 B("Font Bureau","United States","1989","Premium","magazine type","Foundry known for editorial and newspaper families."),
 B("House Industries","United States","1993","Specialist","retro lettering","Design studio and foundry known for vintage-inspired lettering."),
 B("Canada Type","Canada","","Specialist","revivals","Foundry of Patrick Griffin, known for revivals."),
 B("Cadson Demak","Thailand","","Specialist","Thai type","Thai foundry."),
 B("Google Fonts","United States","2010","Mainstream","open fonts","Free open-source font library (Roboto, Noto, Inter)."),
 B("Mark Simonson Studio","United States","","Artisan & independent","Proxima Nova","One-designer studio of Mark Simonson."),
 B("Typotheque","Netherlands","1999","Artisan & independent","multi-script type","Independent foundry with strong non-Latin coverage."),
 B("Morisawa","Japan","1924","Professional & flagship","Japanese type","Japanese type foundry and font maker."),
]
put('I2','00_00',{"kinds":kinds,"brands":brands,"traditions":[],"notes":"Single 'Digital font' kind split into nine classification kinds; old models Prompt, Miedinger, Lato, Montserrat, Open Sans, Oswald, Proxima Nova kept as sans m; FF Atma Serif and Bell as serif m; Noto kept in r and as archetype. Licence scope and variable are types in none of the kinds (not kinds). Brand facts marked unknown left blank; Google Fonts, Klim etc. from knowledge. No Gill Facia, Font Awesome or Material Symbols (not retrieved)."})
