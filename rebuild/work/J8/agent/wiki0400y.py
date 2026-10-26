import sys, json, time, re
sys.path.insert(0, 'tools')
import run
titles = [l.strip() for l in open(sys.argv[1]) if l.strip()]
n = int(sys.argv[2]); kw = sys.argv[3].split('|') if len(sys.argv)>3 else []
todo = list(titles); tries = 0
while todo and tries < 12:
    batch = todo[:8]
    r = json.loads(run.handle_client_tool('J8', '04_00', 'wiki', {'titles': batch}))
    pages = r.get('pages', [])
    if not pages or all(p.get('error') == 429 for p in pages):
        tries += 1; time.sleep(15 * tries); continue
    for p in pages:
        if not p.get('exists'): print('## MISSING', p); continue
        sents = re.split(r'(?<=[.!?])\s+', p.get('extract','').replace('\n',' '))
        keep = [s for s in sents if re.search(r'\b1[6-9]\d\d\b|\b20[0-2]\d\b', s) or any(k.lower() in s.lower() for k in kw)]
        print('##', p['title'], '|', p['url'], '\n', ' '.join(keep)[:n], flush=True)
    todo = todo[8:]; time.sleep(3)
print('LEFT', todo)
