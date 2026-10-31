import json, os, glob, re, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
meta = json.load(open('meta.json'))
t = open('template_v1.html').read().split('\n')
hi = t.index('<header>')
head = '\n'.join(t[:hi])
extra = """
#views { display: flex; flex-wrap: wrap; gap: 4px; }
#views button { font: 600 13px/1 var(--body); padding: 7px 12px; border-radius: 999px; border: 1px solid var(--rule); background: var(--paper); color: var(--ink); cursor: pointer; }
#views button[aria-pressed="true"] { background: var(--ink); border-color: var(--ink); color: var(--paper); }
article.item.wide { grid-column: 1 / -1; }
.archs { align-items: start; display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 8px; margin-top: 8px; }
.arch { align-content: start; border: 1px solid var(--rule); border-left: 3px solid var(--accent); border-radius: 5px; padding: 8px 10px; display: grid; gap: 4px; background: var(--bg); }
.arch .ah { display: flex; flex-wrap: wrap; gap: 4px 8px; align-items: baseline; }
.arch .ah b { font-weight: 600; font-size: 15px; }
.arch .ah i { font-style: normal; color: var(--muted); font-size: 13px; }
.vers { align-items: flex-start; display: flex; flex-wrap: wrap; gap: 4px; }
.chip.ver { background: var(--soft); }
.mk.link { text-decoration: underline; text-decoration-style: dotted; cursor: pointer; }
.tags { display: flex; flex-wrap: wrap; gap: 4px; margin: 0; }
.tag { font: 500 11px/1.4 var(--mono); border: 1px solid var(--rule); border-radius: 999px; padding: 1px 8px; color: var(--muted); background: transparent; }
button.tag { cursor: pointer; }
.mode { font: 500 12px/1 var(--mono); letter-spacing: 0; text-transform: none; color: var(--muted); border: 1px solid var(--rule); border-radius: 999px; padding: 3px 8px; margin-left: 10px; vertical-align: middle; }
.brows { display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 4px 12px; align-items: start; }
.brow > summary { cursor: pointer; padding: 5px 2px; border-bottom: 1px solid var(--rule); list-style: none; display: flex; gap: 8px; align-items: baseline; }
.brow > summary::-webkit-details-marker { display: none; }
.brow > summary b { font-weight: 600; }
.brow > summary i { font-style: normal; color: var(--muted); font-size: 13px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.brow[open] { grid-column: 1 / -1; }
.brow[open] > article.item { margin: 6px 0 10px; }
section.scene.sub { margin-left: 14px; padding-left: 12px; border-left: 2px solid var(--rule); }
section.scene h5 { font: 700 17px/1.1 var(--sign); letter-spacing: .02em; text-transform: uppercase; margin: 6px 0 0; display: flex; gap: 10px; align-items: baseline; flex-wrap: wrap; }
section.scene h5 span { font: 500 12px/1 var(--mono); color: var(--muted); text-transform: none; letter-spacing: 0; }
.cc { font: 500 12px/1 var(--mono); color: var(--muted); letter-spacing: 0; text-transform: none; margin-right: 8px; vertical-align: middle; }
h4.shelf-name .cc, h3.dept-name .cc { font-size: 12px; }
.kc { font: 500 10.5px/1 var(--mono); color: var(--muted); margin-left: 8px; font-weight: 400; }
p.test { margin: 4px 0 0; font-style: italic; color: var(--ink); max-width: 80ch; font-size: 15px; }
p.axis { margin: 2px 0 0; color: var(--muted); font-size: 14px; max-width: 80ch; }
p.axis b, p.test b { font-weight: 600; font-style: normal; }
p.defn { margin: -4px 0 0; font-size: 14.5px; max-width: 80ch; }
p.stats { display: flex; flex-wrap: wrap; gap: 4px 16px; font-size: 13.5px; }
p.stats b { color: var(--ink); font-variant-numeric: tabular-nums; }
details.key { margin-top: 8px; max-width: 80ch; font-size: 14.5px; }
details.key summary { cursor: pointer; color: var(--accent); font-weight: 600; }
details.key p { margin: 6px 0; }
details.key p.prec { color: var(--muted); }
.tt { display: grid; gap: 2px; }
.tt b { font-weight: 600; color: var(--ink); }
button.seel { font: inherit; color: var(--accent); background: none; border: 0; padding: 0; cursor: pointer; text-decoration: underline; text-decoration-style: dotted; }
button.seel i { font-style: normal; color: var(--muted); }
ol.keylist { display: grid; gap: 6px; padding-left: 22px; max-width: 90ch; }
section.guide p { max-width: 80ch; margin: 0; }
.role { font: 600 10.5px/1.4 var(--mono); text-transform: uppercase; letter-spacing: .05em; border-radius: 999px; padding: 1px 7px; background: var(--flag); color: var(--flag-ink); }
.arch.r-landmark, .arch.r-origin { border-left-color: var(--flag); }
.nl { display: grid; gap: 2px; font-size: 13.5px; color: var(--muted); border-left: 2px solid var(--rule); padding-left: 8px; }
.nl p { margin: 0; } .nl b { color: var(--ink); font-weight: 600; }
h6.xg { font: 700 14px/1.2 var(--sign); letter-spacing: .03em; text-transform: uppercase; margin: 12px 0 0; border-bottom: 1px solid var(--rule); padding-bottom: 2px; }
h6.xg span { font: 500 11px/1 var(--mono); color: var(--muted); text-transform: none; }
"""
head = head.replace('</style>', extra + '</style>', 1) if head.count('</style>') == 1 else head[::-1].replace('>elyts/<', ('>elyts/<' + extra[::-1]), 1)[::-1]
header = """<header>
  <div class="top gut"><h1>Possession Taxonomy</h1>
  <nav id="views" aria-label="Views"></nav>
  <input id="q" type="search" placeholder="Search every category" aria-label="Search every category, kind and archetype"></div>
  <div class="navrows gut"><nav class="doms" id="doms" aria-label="Domains"></nav><nav class="cats" id="cats" aria-label="Categories"></nav></div>
</header>
<div class="wrap gut"><nav class="side" id="side" aria-label="Sections"></nav><main id="main"><p class="none">Loading…</p></main></div>"""
sys.path.insert(0, 'tools'); import registers  # noqa: E402
REG = registers.split()
cats = []; index = []
for c in meta['cats']:
    p = 'reader/%s.json' % c['c']
    if not os.path.exists(p): continue
    d = json.load(open(p)); n = 0
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']:
                n += 1; index.append([c['c'], k['n'], k.get('a', ''), ''])
                for x in k.get('x', []) or []:
                    index.append([c['c'], x['n'], x.get('a', '') or '', k['n']])
                for m in k.get('m', []) or []:  # models (incl. versions the structure pass demoted) are findable too
                    index.append([c['c'], m[0], m[1] if len(m) > 1 else '', k['n']])
    r = REG.get(c['c'], {})
    cats.append(dict(c, k=n, nb=r.get('brands', 0), nt=r.get('traditions', 0), ns=r.get('species', 0)))
FW = '../framework/key_v0_8.json'
S = {'domains': meta['domains'], 'cats': cats, 'index': index, 'fw': json.load(open(FW)) if os.path.exists(FW) else {}}
app = open('app.js').read()
html = head + '\n' + header + '\n<script>\nconst S = ' + json.dumps(S, ensure_ascii=False, separators=(',', ':')) + ';\n' + app + '</script>\n'
open('index.html', 'w').write(html)
print('cats', len(cats), 'index', len(index), 'bytes', len(html))
