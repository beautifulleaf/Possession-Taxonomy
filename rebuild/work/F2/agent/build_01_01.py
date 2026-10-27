import json, os
CV='https://waltdisney.org/blog/courvoisier-galleries-selling-disney-magic'
SER='https://comics.ha.com/itm/memorabilia/disney/sleeping-beauty-cast-of-characters-limited-edition-sericel-walt-disney-1997-/a/322348-50350.s'
WB='https://comics.ha.com/itm/animation-art/production-cel/operation-rabbit-wile-e-coyote-and-bugs-bunny-production-cel-setup-with-painted-background-warner-brothers-1952-/a/7232-98305.s'
GH='https://www.mentalfloss.com/entertainment/movies/ghibli-anime-art-auction'
IC='https://icv2.com/articles/news/view/62848/don-hecks-tales-suspense-39-original-art-splash-page-sells-record-3-875-million'
MS='https://themarysue.com/?p=7947'
PY='https://www.americanillustrators.com/traveling-exhibitions/howard-pyle-his-students-and-the-golden-age-of-american-illustration'
RW='https://www.massmoments.org/moment-details/norman-rockwell-wins-medal-of-freedom/submoment/saturday-evening-post-publishes-first-norman-rockwell-cover.html'
kinds=[
 {"n":"Animation cel","a":"cel · production cel · celluloid","d":"An image hand-inked and painted on a clear acetate sheet for an animated film, or a screen-printed edition of one.",
  "t":["production cel","key set-up (cel on matching background)","master set-up","limited-edition cel","sericel","animation drawing","production background","story sketch"],
  "s":"https://www.1stdibs.com/buy/animated-cels/",
  "x":[
   {"n":"Courvoisier set-up","a":"Courvoisier cel","d":"A trimmed Disney production cel laid over a stencilled, airbrushed or wood-veneer background, sold through Courvoisier Galleries as fine art.","mk":"Courvoisier Galleries","y":"1938–1946","s":CV,
    "v":[{"n":"Snow White and the Seven Dwarfs set-ups","mk":"Walt Disney Productions","y":"1938","d":"first and most popular source; early prices about $5–35"},
         {"n":"Silly Symphony set-ups (Ferdinand the Bull, The Ugly Duckling)","mk":"Walt Disney Productions","y":"1939","d":""},
         {"n":"Pinocchio set-ups","mk":"Courvoisier Galleries","y":"1940","d":"prepared by Courvoisier after the film's release"}],
    "dt":"film · characters · background type (airbrush, stencil, wood veneer) · original label and mat · condition"},
   {"n":"Warner Bros. production cel set-up","a":"Looney Tunes cel","d":"A hand-inked, hand-painted cel from a Warner Bros. cartoon short, often shown on a painted background.","mk":"Warner Bros.","y":"1950s","s":WB,
    "v":[{"n":"Operation: Rabbit (Wile E. Coyote and Bugs Bunny)","mk":"Warner Bros.","y":"1952","d":"cel set-up with painted background; Heritage 2020"}],
    "dt":"short and year · characters · original or matching background · paint cracking · signatures"},
   {"n":"Studio Ghibli production cel","a":"Ghibli cel","d":"A hand-painted production cel from a Studio Ghibli feature, sold through specialist anime-art auctions.","mk":"Studio Ghibli","y":"1980s onward","s":GH,
    "v":[{"n":"My Neighbor Totoro (Mei and Satsuki; Catbus)","mk":"Studio Ghibli","y":"1988","d":"production cels; Heritage Art of Anime sale 2025"},
         {"n":"Spirited Away (Haku and Chihiro)","mk":"Studio Ghibli","y":"2001","d":"limited-edition cel"}],
    "dt":"film · characters · with douga or background · production or limited edition"},
   {"n":"Limited-edition sericel","a":"serigraph cel","d":"A screen-printed edition on acetate made from hand-painted studio originals, numbered and sealed rather than used in production.","mk":"Walt Disney Productions","y":"","s":SER,
    "v":[{"n":"Sleeping Beauty 'Cast of Characters'","mk":"Walt Disney Productions","y":"1997","d":"edition of 5,000; Disney seal and certificate"}],
    "dt":"edition size · seal · certificate · framing"}]},
 {"n":"Original comic art","a":"comic book art · original art · OA","d":"A hand-drawn page or cover made for publication in a comic book or strip, usually pencilled and inked on board.",
  "t":["interior page","splash page","cover","comic-strip daily","Sunday page","pencils only","pencils and inks","published or unpublished"],
  "s":IC,
  "x":[
   {"n":"Splash page","a":"","d":"A full-page opening or key panel page, the most prized interior page in original comic art.","mk":"","y":"","s":IC,
    "v":[{"n":"Tales of Suspense #39, page 1","mk":"Don Heck","y":"1963","d":"Iron Man's first appearance; $3.875 million, Heritage 2026"},
         {"n":"The Dark Knight Returns splash page","mk":"Frank Miller","y":"","d":"$448,125 in 2011"}],
    "dt":"publisher · issue and page · pencils/inks credits · board size · published state"},
   {"n":"Interior story page","a":"","d":"A standard story page of panels, valued by character, artist and action.","mk":"","y":"","s":IC,
    "v":[{"n":"Secret Wars #8, page 24","mk":"","y":"1984","d":"$3.36 million in 2022"},
         {"n":"Marvel Super Special #27, page 55","mk":"Al Williamson","y":"","d":"with Carlos Garzon, Tom Palmer and Ron Frenz; $275,000"}],
    "dt":"panel content · character appearance · artist credits"},
   {"n":"Cover art","a":"original cover","d":"The original drawing for a comic book cover.","mk":"","y":"","s":IC,
    "v":[{"n":"Secret Wars II #1 cover","mk":"John Byrne","y":"","d":"inked by Terry Austin; $250,000"},
         {"n":"Weird Fantasy #29 cover","mk":"","y":"","d":"former record of $380,000"}],
    "dt":"publisher · issue · pencils/inks · size · corrections and paste-ups"}]},
 {"n":"Illustration original","a":"illustration art · original illustration","d":"The original painting or drawing made to be reproduced in a book, magazine or advertisement.",
  "t":["magazine cover","story illustration","book illustration","advertising art","oil on canvas or board","watercolour and charcoal","gouache and ink"],
  "s":PY,
  "x":[
   {"n":"Golden Age illustration painting","a":"Brandywine School illustration","d":"A story illustration, often in oil, painted for books and magazines such as Harper's, Century and McClure's.","mk":"Howard Pyle","y":"c. 1880–1925","s":PY,
    "v":[{"n":"The Good Aged Doctor","mk":"Howard Pyle","y":"1899","d":"oil on board"},
         {"n":"La Salle Christening the Country 'Louisiana'","mk":"Howard Pyle","y":"1905","d":"oil on canvas; Harper's"},
         {"n":"The Five Little Pigs","mk":"Elizabeth Shippen Green","y":"1905","d":"watercolour and charcoal on board"},
         {"n":"Only Jules Verbeaux","mk":"Frank Schoonover","y":"1905","d":"oil on canvas"},
         {"n":"Young Tennis Player","mk":"Jessie Willcox Smith","y":"1929","d":"oil and mixed media on board"}],
    "dt":"publication and story · medium · size · tear sheet"},
   {"n":"Magazine cover painting","a":"","d":"The original painting for a magazine cover, painted to be reproduced on the newsstand.","mk":"","y":"20th century","s":RW,
    "v":[{"n":"Saturday Evening Post covers","mk":"Norman Rockwell","y":"1916–c. 1963","d":"323 covers, the first on 20 May 1916"}],
    "dt":"magazine and issue date · medium · tear sheet · provenance"}]}]
def B(n,c,seg,kf,d,s,sig): return {"n":n,"c":c,"f":"","seg":seg,"kf":kf,"d":d,"s":s,"sig":sig}
brands=[
 B("Courvoisier Galleries","United States","Specialist","Disney cel set-ups","San Francisco gallery of Guthrie Courvoisier, sole seller of Disney original art from 1938.",CV,["Courvoisier set-up"]),
 B("Walt Disney Productions","United States","Professional & flagship","animation","American animation studio whose production art and sericels are the core of cel collecting.","knowledge",["Courvoisier set-up","Limited-edition sericel"]),
 B("Warner Bros.","United States","Professional & flagship","Looney Tunes","American film studio whose cartoon shorts yield collectable production cels.","knowledge",["Warner Bros. production cel set-up"]),
 B("Studio Ghibli","Japan","Professional & flagship","anime features","Japanese animation studio whose production cels sell through anime-art auctions.","knowledge",["Studio Ghibli production cel"]),
 B("Howard Pyle","United States","Artisan & independent","illustration","American illustrator and teacher, called the Father of American Illustration, founder of the Brandywine School.",PY,["Golden Age illustration painting"]),
 B("Norman Rockwell","United States","Artisan & independent","magazine covers","American illustrator who painted 323 Saturday Evening Post covers.",RW,["Magazine cover painting"]),
 B("Heritage Auctions","United States","Specialist","comic and animation art","Dallas auction house, a main market reference for comic and animation art.",IC,[]),
]
for b in brands:
    if b["n"]=="Courvoisier Galleries": b["f"]=""
out={"kinds":kinds,"brands":brands,"traditions":[],
 "notes":"Animation cel kept; Original comic art and Illustration original added. No title lists: comic versions are record sales that define the market. Chuck Jones not credited on any retrieved page, so the Warner archetype is credited to the studio. ComicLink not fetched. Ghibli limited-edition cel listed as a version for contrast with production cels. Version mk for Weird Fantasy #29 and Secret Wars #8 left blank (artist not named on the fetched page)."}
p='work/F2/shelves/01_01.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
