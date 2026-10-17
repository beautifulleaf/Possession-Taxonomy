"""Build the stage-3 pilot browser (pages/pilot.html) from the data tables.
usage: build_pilot_page.py [CODE ...]   (default A1 D1)
Reads data/nodes.tsv, kinds.tsv, named_forms.tsv, lines.tsv and makers.tsv; embeds them as JSON and renders the
trees in the browser: category tabs, sub-family rail, kinds with definition and attesting pages, named forms by
maker, lines, and a maker ledger tab. The page is generated; edit this script, never the HTML."""
import html, json, sys
from collections import defaultdict
from common import ROOT, read_tsv

CODES = sys.argv[1:] or ["A1", "D1"]
OUT = ROOT / "pages" / "pilot.html"
NAMES = {"A1": "Clothing", "D1": "Computers & Components"}

def srcs(r):
    s = [x.strip() for x in (r.get("sources") or "").split("|") if x.strip()]
    f = [x.strip() for x in (r.get("fetch_status") or "").split("|")]
    return [[u, f[i] if i < len(f) else ""] for i, u in enumerate(s)]

def main():
    nodes = [n for n in read_tsv(ROOT / "data/nodes.tsv") if n["code"] in CODES]
    kinds = [k for k in read_tsv(ROOT / "data/kinds.tsv") if k["code"] in CODES]
    kind_ids = {k["kind_id"] for k in kinds}
    nfs = [n for n in read_tsv(ROOT / "data/named_forms.tsv") if n["kind_id"] in kind_ids]
    lines = [l for l in read_tsv(ROOT / "data/lines.tsv") if any(k in kind_ids for k in l["kinds"].split(";"))]
    makers = {m["maker_id"]: m for m in read_tsv(ROOT / "data/makers.tsv")}
    worklist = {}
    for c in CODES:
        p = ROOT / f"verify/out/HV_{c}_worklist.tsv"
        if p.exists():
            for w in read_tsv(p): worklist[w["kind_id"]] = w
    mk_kinds = defaultdict(set)
    for n in nfs:
        if n["maker_id"]: mk_kinds[n["maker_id"]].add(n["kind_id"])
    for l in lines:
        for k in l["kinds"].split(";"):
            if k in kind_ids: mk_kinds[l["maker_id"]].add(k)
    used = {m for m in mk_kinds}
    data = {
        "codes": [{"code": c, "name": NAMES.get(c, c)} for c in CODES],
        "nodes": [{"id": n["node_id"], "code": n["code"], "level": n["level"], "parent": n["parent_id"], "name": n["name"],
                   "sort": int(n["sort"] or 0)} for n in nodes],
        "kinds": [{"id": k["kind_id"], "code": k["code"], "sf": k["sub_family"], "leaf": k["leaf"], "name": k["name"],
                   "native": k["native_name"], "def": k["definition"], "notes": k["notes"], "src": srcs(k),
                   "dagger": (worklist.get(k["kind_id"], {}).get("dagger") == "yes"), "new": k["memo_ref"] == "HVMK"}
                  for k in sorted(kinds, key=lambda k: [int(x) if x.isdigit() else x for x in k["kind_id"].replace("A", "").replace("D", "").split(".")])],
        "nfs": [{"id": n["named_form_id"], "kind": n["kind_id"], "name": n["name"], "native": n["native_name"],
                 "bound": n["maker_bound"] == "yes", "maker": n["maker_id"], "line": n["line_id"], "region": n["region"],
                 "src": srcs(n)} for n in nfs],
        "lines": [{"id": l["line_id"], "maker": l["maker_id"], "name": l["name"], "kinds": [k for k in l["kinds"].split(";") if k],
                   "src": srcs(l)} for l in lines],
        "makers": {m: {"name": makers[m]["name"], "native": makers[m]["native_name"], "cls": makers[m]["maker_class"],
                       "country": makers[m]["country"], "src": srcs(makers[m]), "kinds": sorted(mk_kinds[m])}
                   for m in sorted(used) if m in makers},
        "ledger": len([m for m in makers.values()]),
    }
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    page = TEMPLATE.replace("__DATA__", blob)
    OUT.parent.mkdir(exist_ok=True)
    tmp = OUT.with_suffix(".tmp"); tmp.write_text(page, encoding="utf-8"); tmp.replace(OUT)
    print(OUT, round(OUT.stat().st_size / 1024), "KB;", len(kinds), "kinds,", len(nfs), "named forms,", len(lines), "lines,",
          len(data["makers"]), "makers linked")

TEMPLATE = r"""<title>Possession Taxonomy Pilot</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,600;12..96,700&family=JetBrains+Mono:wght@500;600&family=Literata:opsz,wght@7..72,400;7..72,600&display=swap">
<style>
/* Layout: sticky bar with category tabs and search; sub-family rail + kind list; one column on phones. Same tokens as the stage-2 review page. */
:root {
  --bg: #f3f5f6; --surface: #ffffff; --fg: #1d2529; --muted: #5b676e; --rule: #d5dcdf;
  --accent: #1c5d78; --accent-soft: #e2eef3; --mark: #8a6200; --mark-soft: #f6edd4; --ok: #2f6b3f; --ok-soft: #e3f0e6;
  --display: "Bricolage Grotesque", "Segoe UI", system-ui, sans-serif;
  --body: "Literata", Georgia, "Times New Roman", serif;
  --mono: "JetBrains Mono", ui-monospace, Menlo, Consolas, monospace;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --bg: #12181b; --surface: #182024; --fg: #e3e9ec; --muted: #9aa8ae; --rule: #2c383d;
  --accent: #7fc3df; --accent-soft: #1d3440; --mark: #e2b955; --mark-soft: #3a3016; --ok: #8fd19e; --ok-soft: #1c3424; color-scheme: dark } }
:root[data-theme="dark"] {
  --bg: #12181b; --surface: #182024; --fg: #e3e9ec; --muted: #9aa8ae; --rule: #2c383d;
  --accent: #7fc3df; --accent-soft: #1d3440; --mark: #e2b955; --mark-soft: #3a3016; --ok: #8fd19e; --ok-soft: #1c3424; color-scheme: dark }
* { box-sizing: border-box }
body { background: var(--bg); color: var(--fg); font: 15px/1.55 var(--body); }
body::before { content: ""; position: fixed; inset: 0 0 auto; height: env(safe-area-inset-top, 0px); z-index: 10; background: var(--surface); }
.bar { position: sticky; top: env(safe-area-inset-top, 0px); z-index: 5; background: var(--surface); border-bottom: 1px solid var(--rule);
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }
.bar-inner { max-width: 1180px; margin: 0 auto; display: flex; flex-wrap: wrap; align-items: center; gap: 8px 18px; padding-block: 10px; }
.brand { font: 700 15px/1.2 var(--display); }
.brand small { display: block; font: 500 12px/1.3 var(--mono); color: var(--muted); letter-spacing: .04em; text-transform: uppercase; }
.tabs { display: flex; flex-wrap: wrap; gap: 4px; }
.tabs button { font: 600 14px/1 var(--display); padding: 9px 14px; border-radius: 6px; border: 1px solid var(--rule); background: transparent; color: var(--fg); cursor: pointer; }
.tabs button[aria-selected="true"] { background: var(--accent); border-color: var(--accent); color: var(--surface); }
.search { margin-left: auto; font: 15px/1.2 var(--display); padding: 9px 12px; border: 1px solid var(--rule); border-radius: 6px; background: var(--bg); color: var(--fg); width: min(100%, 300px); }
button:focus-visible, .search:focus-visible, a:focus-visible, summary:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.wrap { max-width: 1180px; margin: 0 auto; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); padding-block: 24px 64px;
  display: grid; grid-template-columns: 240px minmax(0, 1fr); gap: 36px; }
nav.rail { position: sticky; top: calc(env(safe-area-inset-top, 0px) + 70px); align-self: start; max-height: calc(100vh - 96px); overflow-y: auto; font: 13px/1.4 var(--display); }
.rail h2 { font: 600 11px/1 var(--mono); text-transform: uppercase; letter-spacing: .08em; color: var(--muted); margin: 0 0 10px; }
.rail ol { list-style: none; margin: 0; padding: 0; display: grid; gap: 2px; }
.rail a { color: var(--fg); text-decoration: none; display: flex; justify-content: space-between; gap: 8px; padding: 4px 8px; border-radius: 4px; }
.rail a:hover { background: var(--accent-soft); }
.rail a span { color: var(--muted); font: 12px/1.4 var(--mono); font-variant-numeric: tabular-nums; }
main { min-width: 0; }
.stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 10px; margin: 0 0 22px; }
.stats div { background: var(--surface); border: 1px solid var(--rule); border-radius: 8px; padding: 10px 14px; display: grid; }
.stats b { font: 700 24px/1.1 var(--display); font-variant-numeric: tabular-nums; }
.stats span { color: var(--muted); font: 13px/1.3 var(--display); }
.note { font: 14px/1.5 var(--display); color: var(--muted); margin: 0 0 18px; max-width: 75ch; }
h2.sf { font: 700 22px/1.25 var(--display); text-wrap: balance; margin: 34px 0 6px; padding-top: 12px; border-top: 2px solid var(--fg); display: flex; gap: 10px; align-items: baseline; flex-wrap: wrap; }
h3.leaf { font: 650 16px/1.3 var(--display); color: var(--accent); margin: 22px 0 8px; display: flex; gap: 8px; align-items: baseline; flex-wrap: wrap; }
.id { font: 600 12px/1 var(--mono); color: var(--muted); }
.axis { font: 13px/1.45 var(--display); color: var(--muted); margin: 0 0 8px; }
details.kind { background: var(--surface); border: 1px solid var(--rule); border-radius: 6px; margin: 6px 0; }
details.kind > summary { cursor: pointer; padding: 9px 12px; display: grid; grid-template-columns: 14px minmax(0, 1fr) auto auto; gap: 4px 10px; align-items: baseline; list-style: none; }
@media (max-width: 560px) { details.kind > summary { grid-template-columns: 14px minmax(0, 1fr) auto; } details.kind > summary .count { grid-column: 2 / -1; } }
details.kind > summary::-webkit-details-marker { display: none; }
details.kind > summary::before { content: "▸"; color: var(--muted); font-size: 12px; }
details.kind[open] > summary::before { content: "▾"; }
.kname { font: 600 15px/1.35 var(--display); }
.kname .id { margin-left: 8px; }
.count { font: 12px/1.3 var(--mono); color: var(--muted); white-space: nowrap; font-variant-numeric: tabular-nums; }
.chip { font: 600 11px/1 var(--mono); padding: 3px 6px; border-radius: 4px; margin-left: 6px; letter-spacing: .03em; }
.chip.new { background: var(--accent-soft); color: var(--accent); }
.chip.dag { background: var(--mark-soft); color: var(--mark); }
.kbody { padding: 0 14px 14px 30px; display: grid; gap: 10px; min-width: 0; }
.kbody p { margin: 0; }
.label { font: 600 11px/1.2 var(--mono); text-transform: uppercase; letter-spacing: .07em; color: var(--muted); margin-bottom: 4px; }
.srcs { display: flex; flex-wrap: wrap; gap: 6px; }
.src { font: 12.5px/1.3 var(--mono); color: var(--accent); text-decoration: none; background: var(--accent-soft); padding: 3px 7px; border-radius: 4px; overflow-wrap: anywhere; }
.src i { font-style: normal; color: var(--muted); margin-left: 6px; }
.src.part { background: var(--mark-soft); color: var(--mark); }
.nfs { display: flex; flex-wrap: wrap; gap: 5px; }
.nf { font: 13px/1.3 var(--display); border: 1px solid var(--rule); border-radius: 4px; padding: 3px 7px; color: var(--fg); text-decoration: none; background: var(--bg); }
.nf small { color: var(--muted); margin-left: 4px; }
.nf.free { border-color: var(--ok); }
.empty { color: var(--muted); font: 13px/1.4 var(--display); }
.hidden-by-search { display: none; }
mark { background: var(--mark-soft); color: inherit; padding: 0 1px; }
table.mk { border-collapse: collapse; width: 100%; font: 13px/1.4 var(--display); }
.tw { overflow-x: auto; border: 1px solid var(--rule); border-radius: 6px; background: var(--surface); }
.mk th, .mk td { text-align: left; vertical-align: top; padding: 6px 10px; border-bottom: 1px solid var(--rule); }
.mk th { font: 600 11px/1.3 var(--mono); text-transform: uppercase; letter-spacing: .05em; color: var(--muted); background: var(--bg); position: sticky; top: 0; }
.mk td:first-child { font-weight: 600; }
.more { font: 600 13px/1 var(--display); margin-top: 12px; padding: 9px 14px; border-radius: 6px; border: 1px solid var(--rule); background: var(--surface); color: var(--fg); cursor: pointer; }
@media (max-width: 860px) {
  .wrap { grid-template-columns: minmax(0, 1fr); gap: 16px; }
  nav.rail { position: static; max-height: 220px; border: 1px solid var(--rule); border-radius: 8px; padding: 12px; background: var(--surface); }
  .search { margin-left: 0; width: 100%; }
}
@media (prefers-reduced-motion: no-preference) { html { scroll-behavior: smooth; } }
</style>
<header class="bar"><div class="bar-inner">
<div class="brand">Possession Taxonomy<small>Stage 3 pilot · harvested data</small></div>
<div class="tabs" role="tablist" id="tabs"></div>
<input class="search" id="q" type="search" placeholder="Filter kinds, models, makers" aria-label="Filter kinds, models and makers">
</div></header>
<div class="wrap"><nav class="rail" aria-label="Sub-families" id="rail"></nav><main id="main"></main></div>
<script id="data" type="application/json">__DATA__</script>
<script>
(function () {
  const D = JSON.parse(document.getElementById('data').textContent);
  const $ = (t, a = {}, ...kids) => { const e = document.createElement(t); for (const [k, v] of Object.entries(a)) { if (k === 'class') e.className = v; else if (k === 'text') e.textContent = v; else e.setAttribute(k, v); } kids.flat().forEach(c => c != null && e.append(c)); return e; };
  const nfByKind = {}, linesByKind = {};
  D.nfs.forEach(n => (nfByKind[n.kind] ||= []).push(n));
  D.lines.forEach(l => l.kinds.forEach(k => (linesByKind[k] ||= []).push(l)));
  const mname = id => (D.makers[id] && D.makers[id].name) || (id || '').replace(/^M-/, '');
  const host = u => { try { return new URL(u).hostname.replace(/^www\./, ''); } catch (e) { return u; } };
  const srcList = src => $('div', { class: 'srcs' }, src.map(([u, f]) => $('a', { class: 'src' + (f === 'partial' ? ' part' : ''), href: u, target: '_blank', rel: 'noopener' }, host(u), $('i', { text: f }))));
  let view = 'A1';
  const tabs = document.getElementById('tabs');
  [...D.codes.map(c => [c.code, c.code + ' ' + c.name]), ['makers', 'Makers']].forEach(([k, label]) => {
    const b = $('button', { type: 'button', role: 'tab', 'data-v': k, text: label });
    b.addEventListener('click', () => { view = k; render(); try { localStorage.setItem('pilot-view', k); } catch (e) {} });
    tabs.append(b);
  });
  try { const v = localStorage.getItem('pilot-view'); if (v) view = v; } catch (e) {}
  if (location.hash && /^#(A1|D1|makers)$/.test(location.hash)) view = location.hash.slice(1);

  function kindCard(k) {
    const nf = nfByKind[k.id] || [], ln = linesByKind[k.id] || [];
    const sum = $('summary', {}, $('span', { class: 'kname' }, k.name + (k.native ? ' [' + k.native + ']' : ''), $('span', { class: 'id', text: k.id })),
      $('span', {}, k.new ? $('span', { class: 'chip new', title: 'Added by the pilot decision pass (R-70)', text: 'new' }) : null,
        k.dagger ? $('span', { class: 'chip dag', title: 'Marked † in the memo: now attested by the harvest', text: '† attested' }) : null),
      $('span', { class: 'count', text: nf.length + ' forms · ' + ln.length + ' lines' }));
    const body = $('div', { class: 'kbody' });
    if (k.def) body.append($('p', { text: k.def }));
    if (k.notes) body.append($('p', { class: 'empty', text: k.notes }));
    body.append($('div', {}, $('div', { class: 'label', text: 'Attested on' }), srcList(k.src)));
    if (ln.length) body.append($('div', {}, $('div', { class: 'label', text: 'Lines (maker series spanning models)' }),
      $('div', { class: 'nfs' }, ln.map(l => $('a', { class: 'nf', href: (l.src[0] || [])[0] || '#', target: '_blank', rel: 'noopener' }, l.name, $('small', { text: mname(l.maker) }))))));
    const byMaker = {};
    nf.forEach(n => (byMaker[n.bound ? mname(n.maker) : ''] ||= []).push(n));
    const keys = Object.keys(byMaker).sort((a, b) => (a === '') - (b === '') || a.localeCompare(b));
    const nfBox = $('div', {}, $('div', { class: 'label', text: 'Named forms' + (nf.length ? '' : ': none yet') }));
    const wrapNf = $('div', { class: 'nfs' });
    keys.forEach(m => byMaker[m].forEach(n => wrapNf.append($('a', { class: 'nf' + (n.bound ? '' : ' free'), href: (n.src[0] || [])[0] || '#', target: '_blank', rel: 'noopener', title: n.bound ? 'maker-bound' : 'design many makers make' },
      n.name + (n.native ? ' [' + n.native + ']' : ''), $('small', { text: n.bound ? m : 'any maker' })))));
    if (nf.length) nfBox.append(wrapNf);
    body.append(nfBox);
    const d = $('details', { class: 'kind', id: 'k-' + k.id }, sum, body);
    d.dataset.text = [k.id, k.name, k.native, k.def, ...nf.map(n => n.name + ' ' + mname(n.maker)), ...ln.map(l => l.name + ' ' + mname(l.maker))].join(' ').toLowerCase();
    return d;
  }

  function renderTree(code) {
    const main = document.getElementById('main'), rail = document.getElementById('rail');
    const nodes = D.nodes.filter(n => n.code === code).sort((a, b) => a.sort - b.sort);
    const kinds = D.kinds.filter(k => k.code === code);
    const kset = new Set(kinds.map(k => k.id));
    const nfs = D.nfs.filter(n => kset.has(n.kind)), lines = D.lines.filter(l => l.kinds.some(k => kset.has(k)));
    const mk = new Set([...nfs.map(n => n.maker), ...lines.map(l => l.maker)].filter(Boolean));
    const cname = D.codes.find(c => c.code === code).name;
    main.append($('div', { class: 'stats' },
      [[kinds.length, 'kinds attested'], [nfs.length, 'named forms'], [lines.length, 'lines'], [mk.size, 'makers linked'], [kinds.filter(k => k.new).length, 'kinds added in the pilot']]
        .map(([n, l]) => $('div', {}, $('b', { text: n.toLocaleString('en') }), $('span', { text: l })))));
    main.append($('p', { class: 'note', text: code + ' ' + cname + ': every kind below is attested on a fetched page (blue source: full fetch, amber: partial). Open a kind for its definition, sources, maker lines and named forms; a named form with a green border is a design many makers make, the others are one maker\'s models. Counts are the pilot\'s first layer: depth passes come next.' }));
    const ol = $('ol');
    nodes.filter(n => n.level === 'sub_family').forEach(sf => {
      const ks = kinds.filter(k => k.sf === sf.id);
      ol.append($('li', {}, $('a', { href: '#n-' + sf.id }, sf.id.split('.').slice(1).join('.') + ' ' + sf.name.replace(/\s*\(.*\)$/, ''), $('span', { text: ks.length }))));
      main.append($('h2', { class: 'sf', id: 'n-' + sf.id }, sf.name, $('span', { class: 'id', text: sf.id })));
      const leaves = nodes.filter(n => n.level === 'leaf' && n.parent === sf.id);
      ks.filter(k => !k.leaf).forEach(k => main.append(kindCard(k)));
      leaves.forEach(lf => {
        const lk = ks.filter(k => k.leaf === lf.id);
        if (!lk.length) return;
        main.append($('h3', { class: 'leaf' }, lf.name, $('span', { class: 'id', text: lf.id })));
        lk.forEach(k => main.append(kindCard(k)));
      });
    });
    rail.append($('h2', { text: code + ' sub-families' }), ol);
  }

  function renderMakers() {
    const main = document.getElementById('main'), rail = document.getElementById('rail');
    const ids = Object.keys(D.makers).sort((a, b) => D.makers[a].name.localeCompare(D.makers[b].name));
    main.append($('div', { class: 'stats' }, [[D.ledger, 'makers in the ledger'], [ids.length, 'linked to a pilot kind']].map(([n, l]) => $('div', {}, $('b', { text: n.toLocaleString('en') }), $('span', { text: l })))));
    main.append($('p', { class: 'note', text: 'One maker ledger serves the whole domain. This list shows the makers tied to a pilot kind through a named form or a line; makers recorded only from brand lists are in data/makers.tsv.' }));
    const tb = $('tbody');
    const rows = ids.map(id => { const m = D.makers[id];
      const kn = m.kinds.map(k => (D.kinds.find(x => x.id === k) || {}).name || k);
      const tr = $('tr', {}, $('td', {}, m.name + (m.native ? ' [' + m.native + ']' : '')), $('td', { text: m.cls }), $('td', { text: m.country }),
        $('td', { text: kn.join(', ') }), $('td', {}, srcList(m.src.slice(0, 2))));
      tr.dataset.text = (m.name + ' ' + m.cls + ' ' + m.country + ' ' + kn.join(' ')).toLowerCase(); return tr; });
    let shown = 0;
    const more = $('button', { class: 'more', type: 'button' });
    const page = () => { rows.slice(shown, shown + 200).forEach(r => tb.append(r)); shown = Math.min(rows.length, shown + 200); more.textContent = 'Show more (' + (rows.length - shown) + ' left)'; more.hidden = shown >= rows.length; };
    more.addEventListener('click', page);
    main.append($('div', { class: 'tw' }, $('table', { class: 'mk' }, $('thead', {}, $('tr', {}, ['Maker', 'Class', 'Country', 'Pilot kinds', 'Source'].map(h => $('th', { text: h })))), tb)), more);
    page();
    main._allRows = rows; main._tbody = tb; main._more = more;
    rail.append($('h2', { text: 'Maker ledger' }), $('p', { class: 'empty', text: 'Filter by name, class, country or kind with the search box.' }));
  }

  function applyFilter() {
    const q = document.getElementById('q').value.trim().toLowerCase();
    const main = document.getElementById('main');
    if (view === 'makers') {
      if (q) { main._tbody.replaceChildren(...main._allRows.filter(r => r.dataset.text.includes(q))); main._more.hidden = true; }
      else { main._tbody.replaceChildren(...main._allRows.slice(0, 200)); main._more.hidden = main._allRows.length <= 200; }
      return;
    }
    main.querySelectorAll('details.kind').forEach(d => { const hit = !q || d.dataset.text.includes(q); d.classList.toggle('hidden-by-search', !hit); d.open = !!q && hit; });
    main.querySelectorAll('h3.leaf, h2.sf').forEach(h => {
      let n = h.nextElementSibling, any = false;
      while (n && !(n.matches('h2.sf') || (h.matches('h3.leaf') && n.matches('h3.leaf')))) { if (n.matches('details.kind') && !n.classList.contains('hidden-by-search')) any = true; n = n.nextElementSibling; }
      h.classList.toggle('hidden-by-search', !!q && !any);
    });
  }

  function render() {
    tabs.querySelectorAll('button').forEach(b => b.setAttribute('aria-selected', String(b.dataset.v === view)));
    document.getElementById('main').replaceChildren(); document.getElementById('rail').replaceChildren();
    if (view === 'makers') renderMakers(); else renderTree(view);
    applyFilter();
  }
  document.getElementById('q').addEventListener('input', applyFilter);
  if (!D.codes.some(c => c.code === view) && view !== 'makers') view = D.codes[0].code;
  render();
})();
</script>
"""

if __name__ == "__main__":
    main()
