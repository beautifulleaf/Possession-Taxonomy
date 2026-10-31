import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(P+'F3.json'))
k=[k for dp in d['depts'] for sh in dp['s'] for k in sh.get('k',[]) if k['n']=='Base card'][0]
U="https://www.baseball-almanac.com/baseball_cards/baseball_card_sets.php?m=Topps"
upd={"2004 Topps":"Topps flagship baseball set of 2004, issued as Series 1 and Series 2 of 366 cards each in the Baseball Almanac listing.",
"2009 Topps":"Topps flagship baseball set of 2009, issued as Series 1 and Series 2 of 330 cards each in the Baseball Almanac listing.",
"2010 Topps":"Topps flagship baseball set of 2010, with a Series 1 of 330 cards in the Baseball Almanac listing.",
"2018 Topps":"Topps flagship baseball set of 2018, with a Series One of 350 cards in the Baseball Almanac listing."}
for e in k['x']:
    if e['n'] in upd: e['d']=upd[e['n']]
if not any(e['n']=='2025 Topps' for e in k['x']):
    k['x'].append({"n":"2025 Topps","a":"","d":"Topps flagship baseball set of 2025, 700 cards in the Baseball Almanac listing.","mk":"Topps","y":"2025","s":U,"v":[],"g":"2000 onward"})
k['sel']=k['sel'].rstrip()+" Card counts for 2004, 2009, 2010, 2018 and 2025 added from Baseball Almanac's Topps set list; Almanac gives no flagship count for 1993, 1994, 1997 to 1999, 2001 to 2003, 2005 to 2008, 2011 to 2017 and 2019 to 2024, so those entries carry none."
json.dump(d,open(P+'F3.json.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'F3.json.tmp',P+'F3.json')
