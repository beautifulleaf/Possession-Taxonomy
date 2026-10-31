import sys, json, time
sys.path.insert(0, 'tools')
import run
titles = [l.strip() for l in open(sys.argv[1]) if l.strip()]
n = int(sys.argv[2]) if len(sys.argv)>2 else 500
todo = list(titles); tries = 0
while todo and tries < 12:
    batch = todo[:10]
    r = json.loads(run.handle_client_tool('J8', '04_00', 'wiki', {'titles': batch}))
    pages = r.get('pages', [])
    if not pages or all(p.get('error') == 429 for p in pages):
        tries += 1; time.sleep(15 * tries); continue
    done = set()
    for p in pages:
        if p.get('error') == 429: continue
        done.add(p['title'])
        if p.get('exists'): print('##', p['title'], '|', p['url'], '\n', p.get('extract','')[:n].replace('\n',' '), flush=True)
        else: print('## MISSING', p, flush=True)
    # remove the batch items that got an answer (titles may be normalized: drop whole batch if any answered)
    todo = todo[10:] if done else todo
    time.sleep(3)
print('LEFT', todo)
