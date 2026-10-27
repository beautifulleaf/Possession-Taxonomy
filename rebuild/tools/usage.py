"""Audit paid-connector use across worker transcripts: python3 tools/usage.py <tasks-dir>
Counts WebFetch/WebSearch vs Firecrawl/Parallel calls and how many paid scrapes were retries of a URL first tried with WebFetch."""
import json, glob, sys, collections, os
tot = collections.Counter(); retry = first = 0; heavy = []
for f in glob.glob(os.path.join(sys.argv[1], '*.output')):
    c = collections.Counter(); wf = set(); paid = []
    for line in open(f, errors='ignore'):
        try: m = json.loads(line).get('message') or {}
        except Exception: continue
        for b in m.get('content') if isinstance(m.get('content'), list) else []:
            if b.get('type') != 'tool_use': continue
            n, i = b['name'], b.get('input') or {}; c[n] += 1
            if n == 'WebFetch': wf.add(i.get('url'))
            if n == 'mcp__Firecrawl__firecrawl_scrape': paid.append(i.get('url'))
            if n == 'mcp__Parallel_Auth__web_fetch': paid += i.get('urls') or []
    r = sum(1 for u in paid if u in wf); retry += r; first += len(paid) - r
    if len(paid) - r >= 5: heavy.append((os.path.basename(f)[:8], len(paid) - r))
    tot.update(c)
keys = ['WebFetch', 'WebSearch', 'mcp__Firecrawl__firecrawl_scrape', 'mcp__Firecrawl__firecrawl_search', 'mcp__Parallel_Auth__web_fetch', 'mcp__Parallel_Auth__web_search']
print({k.split('__')[-1]: tot[k] for k in keys})
print(f'paid fetches: {retry} retries after WebFetch, {first} first-choice; workers with >=5 first-choice paid fetches: {heavy}')
