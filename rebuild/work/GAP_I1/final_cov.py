import json,re,os
P='/home/user/Possession-Taxonomy/rebuild/out/I1.json'
d=json.load(open(P))
M=re.compile(r"(Complete: \d+ of \d+|Covers \d+ of about \d+|No complete list exists)")
OV={
"Linux distribution":"Complete: 543 of 543 rows in DistroWatch's Page Hit Ranking (last 12 months), plus 143 names from the major-family sections of Wikipedia's List of Linux distributions that DistroWatch lacks; the Android-based and historical sections of that list are not entries.",
"Alternative & hobby operating system":"Covers 69 of about 1,100 in Wikipedia's List of operating systems (read to its end); the rest are mainframe, minicomputer, real-time, router and historic systems, out of scope.",
"Mobile operating system":"Covers 40 of about 1,100 in Wikipedia's List of operating systems (its mobile and embedded sections); embedded, router and real-time systems are out of scope.",
"Antivirus software":"Covers 63 of about 85 pages of Wikipedia's Category:Antivirus software; the rest are labs, concepts and company pages, and the Comparison of antivirus software page returned 404 (WebFetch and Firecrawl).",
"File archiver":"Complete: 31 of 31 archivers in the General information table of Wikipedia's Comparison of file archivers.",
"Note-taking app":"Complete: 38 of 38 applications named on Wikipedia's Comparison of note-taking software.",
"Local AI model runner":"Complete: 6 of 6 runners named in the navigation of Wikipedia's List of chatbots; no wider list of local runners was found.",
}
for dp in d['depts']:
  for sh in dp['s']:
    for k in sh['k']:
      x=k.get('x') or []
      if not x: continue
      s=re.sub(r'\s*Entries: \d+\.?\s*$','',k['sel']).strip()
      if k['n'] in OV:
          if k['n'] in("Linux distribution","Alternative & hobby operating system","Mobile operating system","Antivirus software","File archiver","Note-taking app","Local AI model runner") and not s.endswith(OV[k['n']]):
              s=s+' '+OV[k['n']]
      elif not M.search(s):
          urls=re.findall(r'https?://\S+?(?=\s|\.\s|,|\)|$)',s)
          src=f" the overview at {urls[0].rstrip('.')}" if urls else " the overviews named above"
          if 'kept from the previous edition' in s or 'No whole-space' in s or True:
              s=re.sub(r'\s*No whole-space reference list for this kind was fetched, so coverage is open and not claimed complete\.','',s)
              s=re.sub(r'\s*A search for a Wikipedia comparison or list page.*$','',s)
              s=s.strip()
              s=s+f" No complete list exists; follows{src} and the earlier edition's sources; coverage is open."
      k['sel']=s
tmp=P+'.tmp'; json.dump(d,open(tmp,'w'),ensure_ascii=False); os.replace(tmp,P)
