import json, os
W = 'https://en.wikipedia.org/wiki/'
K = 'knowledge'
def X(n, d, mk, y, s, v=(), a="", dt=""):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": [dict(zip(("n", "mk", "y", "d"), t)) for t in v], "dt": dt}
HEN = 'https://www.henle.de/Profile/'; BAR = 'https://emag.baerenreiter.com/en/baerenreiter-urtext/'; WU = 'https://www.imslp.org/wiki/Wiener_Urtext_Edition'
PET = W + 'Edition_Peters'; SCH = 'https://imslp.org/wiki/G._Schirmer'; DOV = 'https://imslp.org/wiki/Dover_Publications'; KAL = W + 'Edwin_F._Kalmus'
EUL = W + 'Ernst_Eulenburg_(musical_editions)'; LSS = W + 'List_of_score_series_and_pocket-score_series'
TPA = 'https://syncopatedtimes.com/sydney-leff-and-the-art-of-sheet-music-illustration/'; ABR = 'https://www.imslp.org/wiki/Associated_Board'
HL = 'https://www.stretta-music.it/piano-solos-book-1-nr-810680.html'; NOV = 'https://imslp.org/wiki/Novello%27s_Octavo_Anthems'
VAM = 'https://collections.vam.ac.uk/item/O1410898/champagne-charlie-music-leybourne-george/'; SUZ = W + 'Suzuki_method'
SMP = 'https://www.sheetmusicplus.com/en/category/formats'; ILL = 'https://guides.library.illinois.edu/findingmusic/printedmusicformats'
kinds = [
 {"n": "Songbook", "a": "collection · album · instrumental edition", "d": "Bound volume of songs or instrumental pieces in notation for voice, piano or another instrument, from lead-sheet books to urtext editions.",
  "t": ["piano/vocal/guitar (PVG)", "lead-sheet book (fake book)", "easy arrangement", "urtext edition", "practical (edited) edition", "with fingering", "with audio", "paperbound", "clothbound", "spiral-bound"],
  "s": SMP,
  "x": [
   X("G. Henle Urtext", "Munich urtext editions giving the composer's text from the sources, almost all bound in characteristic blue card covers.", "G. Henle Verlag", "1948", HEN,
     [("Paperbound Urtext", "G. Henle Verlag", "", "blue cover"), ("Clothbound Urtext", "G. Henle Verlag", "", ""), ("Henle Library app", "G. Henle Verlag", "", "digital edition"),
      ("Horizons", "G. Henle Verlag", "2026", "orange-covered imprint")], a="Henle blue", dt="HN number · paper or cloth · fingering"),
   X("Bärenreiter Urtext", "Kassel urtext editions edited by scholars and performers, with a critical commentary and practical page turns.", "Bärenreiter", "", BAR,
     [], dt="BA number · critical commentary · extra parts"),
   X("Wiener Urtext Edition", "Vienna urtext series founded by Schott and Universal Edition, mostly standard repertoire from Bach to Brahms.", "Wiener Urtext Edition", "1972", WU,
     [], a="Vienna Urtext · UT", dt="UT number · fingering by named performer"),
   X("Edition Peters", "Leipzig's inexpensive collected-classics series in light green covers, pink for licensed newer works.", "Edition Peters", "1867", PET,
     [("Green cover", "Edition Peters", "1867", "older, out-of-copyright works"), ("Pink cover", "Edition Peters", "", "newer works acquired or licensed")], a="Peters green", dt="edition number · cover colour"),
   X("Breitkopf Volksausgabe", "Breitkopf & Härtel's inexpensive 'people's edition' of the classics, launched in competition with Edition Peters.", "Breitkopf & Härtel", "1867", PET,
     [], a="People's edition", dt="edition number"),
   X("Schirmer's Library of Musical Classics", "New York's yellow-covered American editions of the standard repertoire.", "G. Schirmer", "1892", SCH,
     [], a="Schirmer yellow", dt="volume number · editor"),
   X("Dover reprint", "Low-cost paperback reprints of public-domain scores, often photographed from Breitkopf & Härtel and Peters editions.", "Dover Publications", "1941", DOV,
     [], dt="source edition · paperback"),
   X("Kalmus Classic Series", "Inexpensive reprints of older public-domain editions under the Kalmus name.", "Edwin F. Kalmus", "1926", KAL,
     [("Kalmus Classic Series", "Alfred Music", "", "Alfred's imprint for the former Belwin-Mills Kalmus titles")], dt="reprint source"),
  ]},
 {"n": "Vocal score", "a": "piano-vocal score", "d": "Score with the vocal parts in full and the accompaniment reduced for piano.",
  "t": ["opera", "oratorio", "musical", "octavo size", "with tonic sol-fa", "language of text"], "s": ILL},
 {"n": "Piano reduction", "a": "", "d": "Edition of an ensemble or concerto work with the orchestra reduced for piano, usually with the solo part.",
  "t": ["with solo part", "two-piano version", "urtext"], "s": ILL},
 {"n": "Full score", "a": "conductor's score", "d": "Printed score showing every part of an ensemble work on the page at full size.",
  "t": ["conductor's score", "hire-library score", "reprint", "urtext / critical edition", "paperback", "clothbound"], "s": ILL,
  "x": [
   X("Dover full-score reprint", "Large-format paperback reprints of orchestral and choral full scores from older public-domain editions.", "Dover Publications", "", DOV, [], dt="works collected · source edition"),
  ]},
 {"n": "Miniature score", "a": "study score · pocket score · Studienpartitur", "d": "Full score reduced to pocket size for study.",
  "t": ["orchestral", "chamber", "opera", "urtext", "with introduction"], "s": ILL,
  "x": [
   X("Eulenburg miniature score", "Leipzig-born pocket-score series in bright yellow covers, over 1,200 orchestral, chamber and operatic titles.", "Edition Eulenburg", "1891", EUL,
     [("Payne's kleine Partitur-Ausgabe", "A. Payne's Musikverlag", "", "chamber-music pocket scores; bought by Eulenburg 1891"),
      ("Donajowski's Miniature Scores", "", "", "London orchestral pocket scores; bought by Eulenburg 1908"), ("Eulenburg London", "Edition Eulenburg", "1939", "Ernst Eulenburg Ltd; to Schott late 1950s")],
     a="Eulenburg yellow", dt="catalogue number · cover · introduction"),
   X("Hawkes Pocket Scores", "Boosey & Hawkes's study-score series, mostly 20th-century and contemporary music.", "Boosey & Hawkes", "", LSS, [], a="HPS", dt="HPS number"),
   X("Philharmonia Partituren", "Vienna pocket-score series founded by Alfred Kalmus.", "Wiener Philharmonischer Verlag", "1923", LSS, [], a="Philharmonia Pocket Scores", dt="number"),
   X("Bärenreiter-Taschenpartituren", "Bärenreiter's urtext study scores.", "Bärenreiter", "", LSS, [], dt="catalogue number"),
   X("Henle Studienpartituren", "Smaller-format urtext study scores from G. Henle.", "G. Henle Verlag", "", HEN, [], a="Henle study score", dt="HN number"),
   X("Dover Miniature Scores", "Reprints of public-domain works in miniature format.", "Dover Publications", "", LSS, [], dt="source edition"),
   X("Kalmus Miniature Scores", "Pocket scores first issued by Edwin F. Kalmus.", "Edwin F. Kalmus", "", LSS, [], dt="number"),
  ]},
 {"n": "Score and parts", "a": "", "d": "Score issued together with the separate parts for each performer.", "t": ["chamber", "with piano", "urtext"], "s": SMP},
 {"n": "Performance parts", "a": "set of parts · single part · instrumental part", "d": "Performers' parts of a work issued without the score, as a complete set or one part alone.",
  "t": ["complete set", "single part", "string set", "wind set", "extra string parts", "hire material"], "s": SMP},
 {"n": "Choral octavo", "a": "octavo", "d": "Single choral work printed in octavo format (about 10 × 6.5 inches) for choir use.",
  "t": ["SATB", "upper voices", "male voices", "with piano or organ", "a cappella", "tonic sol-fa"], "s": SMP,
  "x": [
   X("Novello octavo", "Novello's cheap octavo-size choral editions, which set the standard size for choral music.", "Novello", "1850s", NOV,
     [("Novello's Octavo Anthems", "Novello", "1875", "No. 700 by 1900, 1200 by 1940"), ("Tonic sol-fa issue", "Novello", "", "same series in sol-fa notation")], dt="series number · notation"),
  ]},
 {"n": "Method or tutor book", "a": "tutor · method · exam book", "d": "Graded instruction book for learning an instrument or voice, often in a numbered series with recordings.",
  "t": ["beginner", "graded level", "with audio", "theory workbook", "exam pieces", "scales and arpeggios", "teacher's edition"], "s": SUZ,
  "x": [
   X("Suzuki repertoire books", "Graded volumes of the Suzuki Talent Education 'mother-tongue' method, one numbered series per instrument with recordings.", "", "1945", SUZ,
     [("Violin", "", "", "10 volumes"), ("Viola", "", "", "9 volumes"), ("Cello", "", "", "10 volumes"), ("Piano", "", "", "7 volumes"), ("Flute", "", "", "14 volumes"),
      ("Guitar", "", "", "9 volumes"), ("Revised violin volumes", "", "2007", "new recordings of volumes 1–4")], a="Suzuki Violin School", dt="instrument · volume · edition · recording"),
   X("ABRSM exam publications", "Graded exam pieces, scales and editions published for the Associated Board's music examinations.", "ABRSM", "1918", ABR,
     [("Performing editions", "ABRSM", "1920s", "e.g. Tovey's editions of piano classics")], dt="instrument · grade · syllabus years"),
   X("Hal Leonard Student Piano Library", "Graded piano method with lesson, solo, practice-game and theory books at each level.", "Hal Leonard", "", HL,
     [("Piano Solos Book 1", "Hal Leonard", "", "HL00296003, 32 pages, accompaniments on CD or MIDI disk")], dt="book · level · audio"),
  ]},
 {"n": "Popular song sheet", "a": "sheet music · song sheet · songsheet", "d": "Single popular song for voice and piano sold unbound with an illustrated cover.",
  "t": ["chromolithographed cover", "offset-printed cover", "11 × 14 inches (pre-1917)", "6 × 9 inches (war size)", "9 × 12 inches (standard)", "artist-signed cover", "performer portrait cover"],
  "s": TPA,
  "x": [
   X("Victorian music-hall song sheet", "Victorian song sheet with a full-colour chromolithographed cover, often a portrait of the music-hall singer.", "", "1860s", VAM,
     [("Concanen cover", "Charles Sheard & Co.", "1866", "colour lithograph by Alfred Concanen")], dt="cover artist · publisher · condition"),
   X("Tin Pan Alley sheet", "American popular song sheet of the early 20th century, sold on a bold illustrated cover by artists such as Sydney Leff.", "", "", TPA,
     [("Large size", "", "", "11 × 14 inches before the First World War"), ("War size", "", "", "6 × 9 inches during paper shortages"), ("Standard size", "", "", "9 × 12 inches after 1918")],
     dt="size · cover artist · publisher · condition"),
  ]},
]
brands = [
 {"n": "G. Henle Verlag", "c": "Germany", "f": "1948", "seg": "Specialist", "kf": "urtext", "d": "Munich publisher founded by Günter Henle, known for blue-covered urtext editions.", "sig": ["G. Henle Urtext"], "lines": ["Henle Studienpartituren", "Horizons"], "s": HEN},
 {"n": "Bärenreiter", "c": "Germany", "f": "1923", "seg": "Specialist", "kf": "urtext, complete editions", "d": "Kassel music publisher of urtext editions and complete editions.", "sig": ["Bärenreiter Urtext"], "lines": ["Bärenreiter-Taschenpartituren"], "s": K},
 {"n": "Wiener Urtext Edition", "c": "Austria", "f": "1972", "seg": "Specialist", "kf": "urtext", "d": "Vienna urtext publisher founded jointly by Schott and Universal Edition.", "sig": ["Wiener Urtext Edition"], "s": WU},
 {"n": "Edition Peters", "c": "Germany", "f": "1800", "seg": "Heritage manufactory", "kf": "green-cover classics", "d": "Leipzig music publisher founded as the Bureau de Musique, known for its green-covered edition.", "sig": ["Edition Peters"], "rel": ["Breitkopf & Härtel"], "s": PET},
 {"n": "Breitkopf & Härtel", "c": "Germany", "f": "1719", "seg": "Heritage manufactory", "kf": "music publishing", "d": "Leipzig music publisher, among the oldest, with the Volksausgabe series.", "sig": ["Breitkopf Volksausgabe"], "rel": ["Edition Peters"], "s": K},
 {"n": "G. Schirmer", "c": "United States", "f": "1861", "seg": "Mainstream", "kf": "yellow-cover classics", "d": "New York music publisher founded by Gustav Schirmer, known for the Library of Musical Classics.", "sig": ["Schirmer's Library of Musical Classics"], "s": SCH},
 {"n": "Dover Publications", "c": "United States", "f": "1941", "seg": "Value", "kf": "reprints", "d": "American reprint publisher of public-domain scores, founded by Hayward Cirker.", "sig": ["Dover reprint", "Dover full-score reprint"], "lines": ["Dover Miniature Scores"], "s": DOV},
 {"n": "Edwin F. Kalmus", "c": "United States", "f": "1926", "seg": "Value", "kf": "reprints", "d": "New York-founded publisher of inexpensive public-domain reprints and orchestral material.", "sig": ["Kalmus Classic Series"], "lines": ["Kalmus Miniature Scores"], "rel": ["Alfred Music"], "s": KAL},
 {"n": "Alfred Music", "c": "United States", "f": "1922", "seg": "Mainstream", "kf": "educational music", "d": "American educational music publisher, owner of the Kalmus Classic Series imprint.", "s": K},
 {"n": "Edition Eulenburg", "c": "Germany", "f": "1874", "seg": "Specialist", "kf": "miniature scores", "d": "Pocket-score publisher founded by Ernst Eulenburg in Leipzig, known for yellow covers; part of Schott.", "sig": ["Eulenburg miniature score"], "s": EUL},
 {"n": "A. Payne's Musikverlag", "c": "Germany", "f": "", "seg": "Specialist", "kf": "miniature scores", "d": "Early publisher of chamber-music pocket scores, bought by Eulenburg.", "rel": ["Edition Eulenburg"], "s": EUL},
 {"n": "Boosey & Hawkes", "c": "United Kingdom", "f": "1930", "seg": "Mainstream", "kf": "20th-century music", "d": "London music publisher with the Hawkes Pocket Scores study-score series.", "sig": ["Hawkes Pocket Scores"], "s": K},
 {"n": "Wiener Philharmonischer Verlag", "c": "Austria", "f": "1923", "seg": "Specialist", "kf": "pocket scores", "d": "Vienna publisher of the Philharmonia pocket scores, founded by Alfred Kalmus.", "sig": ["Philharmonia Partituren"], "s": LSS},
 {"n": "Novello", "c": "United Kingdom", "f": "1811", "seg": "Heritage manufactory", "kf": "choral music", "d": "London music publisher that made the octavo the standard choral format.", "sig": ["Novello octavo"], "s": K},
 {"n": "ABRSM", "c": "United Kingdom", "f": "1889", "seg": "Institution & issuer", "kf": "music exams", "d": "Associated Board of the Royal Schools of Music, examining board publishing since 1918.", "sig": ["ABRSM exam publications"], "s": ABR},
 {"n": "Hal Leonard", "c": "United States", "f": "1947", "seg": "Mainstream", "kf": "printed music", "d": "Large American printed-music publisher and distributor.", "sig": ["Hal Leonard Student Piano Library"], "s": K},
 {"n": "Charles Sheard & Co.", "c": "United Kingdom", "f": "", "seg": "Heritage manufactory", "kf": "music-hall songs", "d": "London music-hall song publisher at 192 High Holborn.", "s": VAM},
]
notes = ("All eight old kinds kept; Set of parts and Single part merged into Performance parts (t: complete set, single part). New kinds: Method or tutor book, Popular song sheet. "
         "Publisher edition lines are archetypes: urtext and classics lines under Songbook (broadened to instrumental volumes, since no other kind takes them), pocket-score lines under Miniature score (old models became archetypes/versions), Novello under Choral octavo. "
         "Suzuki book publisher not named (not on fetched page). Breitkopf founding year, Bärenreiter, Boosey & Hawkes, Novello, Hal Leonard, Alfred from knowledge. No piece titles named.")
out = {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes}
p = 'work/F1/shelves/05_00.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('written')
