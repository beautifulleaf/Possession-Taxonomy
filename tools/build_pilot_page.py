"""Build the stage-3 pilot browser (pages/pilot.html) from the data tables.
usage: build_pilot_page.py [CODE ...]   (default A1 D1)
Reads data/nodes.tsv, kinds.tsv, named_forms.tsv, lines.tsv and makers.tsv; embeds them as JSON and renders the
trees in the browser: category tabs, sub-family rail, kinds with definition and attesting pages, named forms by
maker, lines, and a maker ledger tab. A1 opens "By scene" (R-71); its "Coverage" view shows brands per region and
country against the reference distribution (tools/coverage.py, R-80, R-94). The page is generated; edit this script,
never the HTML."""
import html, json, subprocess, sys
from collections import defaultdict
from common import ROOT, read_tsv
from regions import REGIONS, REGION_OF

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
    for r in read_tsv(ROOT / "data/maker_kinds.tsv"):  # garment-level and category-level ties (R-75, R-76)
        if r["kind_id"] in kind_ids or r["kind_id"] in CODES:
            mk_kinds[r["maker_id"]].add(r["kind_id"])
    brand_only = {m for m in makers if "manufacturer" in makers[m].get("supply_role", "")}
    used = {m for m in mk_kinds if m not in brand_only}
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
                       "country": makers[m]["country"], "src": srcs(makers[m])[:1], "kinds": sorted(mk_kinds[m])}
                   for m in sorted(used) if m in makers},
        "ledger": len([m for m in makers.values()]),
        "scenes": [{"id": x["scene_id"], "name": x["name"], "native": x["native_name"], "cluster": x["cluster"],
                    "parent": x["parent_id"], "desc": x["description"], "def": x["definition_source"]}
                   for x in read_tsv(ROOT / "data/scenes.tsv")],
        "tags": [{"maker": t["subject_id"], "scene": t["scene_id"], "strength": t["strength"], "src": srcs(t)}
                 for t in read_tsv(ROOT / "data/scene_tags.tsv") if t["subject_type"] == "maker"],
    }
    for t in data["tags"]:  # makers known only through a scene tag still need a ledger entry on the page
        m = t["maker"]
        if m not in data["makers"] and m in makers:
            data["makers"][m] = {"name": makers[m]["name"], "native": makers[m]["native_name"], "cls": makers[m]["maker_class"],
                                 "country": makers[m]["country"], "src": srcs(makers[m])[:1], "kinds": sorted(mk_kinds[m])}
    data["coverage"] = coverage()
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    OUT.parent.mkdir(exist_ok=True)
    dp = OUT.with_name("pilot-data.json"); tmpd = dp.with_suffix(".tmp"); tmpd.write_text(blob, encoding="utf-8"); tmpd.replace(dp)
    page = TEMPLATE  # the data ships beside the page as pilot-data.json (published with it), so the page itself stays small
    tmp = OUT.with_suffix(".tmp"); tmp.write_text(page, encoding="utf-8"); tmp.replace(OUT)
    print(OUT, round(OUT.stat().st_size / 1024), "KB page +", round(len(blob.encode()) / 1024), "KB data;", len(kinds), "kinds,", len(nfs), "named forms,", len(lines), "lines,",
          len(data["makers"]), "makers linked")

def coverage(code="A1"):
    """Per region and country: brands, actual share, expected share, ratio (tools/coverage.py writes the table)."""
    subprocess.run([sys.executable, str(ROOT / "tools/coverage.py"), code], capture_output=True, text=True)
    rows = read_tsv(ROOT / f"verify/out/coverage_{code}.tsv")
    unknown = sum(int(r["brands"] or 0) for r in rows if r["region"] == "unknown")
    cs = [r for r in rows if r["country"]]
    known = sum(int(r["brands"] or 0) for r in cs) or 1
    regs = []
    for reg in REGIONS:
        rr = [r for r in cs if REGION_OF.get(r["country"]) == reg]
        b = sum(int(r["brands"] or 0) for r in rr); e = sum(float(r["expected"] or 0) for r in rr)
        regs.append({"region": reg, "brands": b, "share": b / known, "expected": e, "ratio": (b / known) / e if e else None,
                     "countries": len([r for r in rr if int(r["brands"] or 0)])})
    ctr = [{"c": r["country"], "region": r["region"], "brands": int(r["brands"] or 0), "share": float(r["share"] or 0),
            "expected": float(r["expected"] or 0), "ratio": float(r["ratio"]) if r["ratio"] else None, "flag": r["flag"]}
           for r in cs]
    return {"code": code, "known": known, "unknown": unknown, "regions": regs, "countries": ctr}

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
.modes { display: flex; gap: 4px; margin: 0 0 16px; }
.modes button { font: 600 13px/1 var(--display); padding: 8px 12px; border-radius: 999px; border: 1px solid var(--rule); background: var(--surface); color: var(--fg); cursor: pointer; }
.modes button[aria-pressed="true"] { background: var(--fg); border-color: var(--fg); color: var(--surface); }
h2.cl { font: 700 24px/1.2 var(--display); text-wrap: balance; margin: 30px 0 4px; padding-top: 12px; border-top: 2px solid var(--fg); }
.scene { margin: 18px 0 8px; }
.scene h3 { font: 650 17px/1.3 var(--display); color: var(--accent); margin: 0 0 2px; display: flex; gap: 8px; flex-wrap: wrap; align-items: baseline; }
.scene p { margin: 0 0 8px; font: 14px/1.5 var(--body); max-width: 70ch; }
.brands { display: grid; grid-template-columns: repeat(auto-fill, minmax(230px, 1fr)); gap: 6px; }
details.brand { background: var(--surface); border: 1px solid var(--rule); border-radius: 6px; min-width: 0; }
details.brand > summary { cursor: pointer; padding: 7px 10px; display: flex; justify-content: space-between; gap: 8px; align-items: baseline; list-style: none; font: 600 14px/1.3 var(--display); }
details.brand > summary::-webkit-details-marker { display: none; }
details.brand.core { border-left: 3px solid var(--accent); }
.bbody { padding: 0 10px 10px; display: grid; gap: 8px; font: 13px/1.45 var(--display); }
.sub { color: var(--muted); font: 12px/1.3 var(--mono); }
.cov td.num, .cov th.num { text-align: right; font-variant-numeric: tabular-nums; font-family: var(--mono); font-size: 12.5px; }
.bars { position: relative; height: 18px; min-width: 140px; }
.bars span { position: absolute; left: 0; height: 8px; border-radius: 2px; }
.bars .act { top: 1px; background: var(--accent); }
.bars .exp { top: 10px; background: var(--muted); opacity: .55; }
.ratio { font: 600 12px/1 var(--mono); padding: 3px 6px; border-radius: 4px; font-variant-numeric: tabular-nums; }
.ratio.low { background: var(--mark-soft); color: var(--mark); }
.ratio.okr { background: var(--ok-soft); color: var(--ok); }
.ratio.mid { background: var(--accent-soft); color: var(--accent); }
.legend { display: flex; flex-wrap: wrap; gap: 14px; font: 12px/1.3 var(--display); color: var(--muted); margin: 0 0 12px; }
.legend i { display: inline-block; width: 18px; height: 8px; border-radius: 2px; margin-right: 6px; vertical-align: middle; }
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
<div class="wrap"><nav class="rail" aria-label="Sub-families" id="rail"></nav><main id="main"><p class="note">Loading the taxonomy data (about 8 MB)…</p></main></div>
<script>
fetch('pilot-data.json').then(r => { if (!r.ok) throw new Error(r.status); return r.json(); }).then(start).catch(e => {
  document.getElementById('main').textContent = 'The data file did not load (' + e.message + '). Reload the page to try again.';
});
function start(D) {
  const $ = (t, a = {}, ...kids) => { const e = document.createElement(t); for (const [k, v] of Object.entries(a)) { if (k === 'class') e.className = v; else if (k === 'text') e.textContent = v; else e.setAttribute(k, v); } kids.flat().forEach(c => c != null && e.append(c)); return e; };
  const nfByKind = {}, linesByKind = {};
  D.nfs.forEach(n => (nfByKind[n.kind] ||= []).push(n));
  D.lines.forEach(l => l.kinds.forEach(k => (linesByKind[k] ||= []).push(l)));
  const mname = id => (D.makers[id] && D.makers[id].name) || (id || '').replace(/^M-/, '');
  const host = u => { try { return new URL(u).hostname.replace(/^www\./, ''); } catch (e) { return u; } };
  const srcList = src => $('div', { class: 'srcs' }, src.map(([u, f]) => $('a', { class: 'src' + (f === 'partial' ? ' part' : ''), href: u, target: '_blank', rel: 'noopener' }, host(u), $('i', { text: f }))));
  let view = 'A1';
  let mode = {};  // per category: 'scene' or 'tree'
  const hasScenes = code => D.tags.length && D.scenes.some(x => (x.cluster || '') !== '') && code === 'A1';
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

  function renderScenes(code) {
    const main = document.getElementById('main'), rail = document.getElementById('rail');
    const kinds = new Map(D.kinds.filter(k => k.code === code).map(k => [k.id, k]));
    const piecesOf = m => D.nfs.filter(n => n.maker === m && kinds.has(n.kind));
    const tagsOf = m => D.tags.filter(t => t.maker === m);
    const sceneName = id => (D.scenes.find(x => x.id === id) || {}).name || id;
    const clusters = [...new Set(D.scenes.map(x => x.cluster).filter(Boolean))];
    const brandsIn = new Set(D.tags.map(t => t.maker));
    main.append($('div', { class: 'stats' }, [[clusters.length, 'scene clusters'], [D.scenes.length, 'scenes'], [brandsIn.size, 'brands placed in a scene'], [D.tags.length, 'scene tags']]
      .map(([n, l]) => $('div', {}, $('b', { text: n.toLocaleString('en') }), $('span', { text: l })))));
    main.append($('p', { class: 'note', text: 'Clothing by scene: each scene is defined on a fetched page; each brand is placed in it on a fetched page, as core (defining the scene) or adjacent (worn in it). A brand can sit in several scenes. Open a brand for its signature pieces and its other scenes. The garment tree is under "By garment".' }));
    const ol = $('ol');
    clusters.forEach(cl => {
      const sc = D.scenes.filter(x => x.cluster === cl);
      const cid = 'cl-' + cl.replace(/[^A-Za-z0-9]+/g, '-');
      ol.append($('li', {}, $('a', { href: '#' + cid }, cl, $('span', { text: sc.length }))));
      main.append($('h2', { class: 'cl', id: cid, text: cl }));
      sc.forEach(x => {
        const tags = D.tags.filter(t => t.scene === x.id).sort((a, b) => (a.strength !== 'core') - (b.strength !== 'core') || mname(a.maker).localeCompare(mname(b.maker)));
        const box = $('section', { class: 'scene', id: 's-' + x.id });
        box.append($('h3', {}, x.name + (x.native ? ' [' + x.native + ']' : ''), x.parent ? $('span', { class: 'sub', text: 'in ' + sceneName(x.parent) }) : null,
          $('span', { class: 'sub', text: tags.filter(t => t.strength === 'core').length + ' core · ' + tags.filter(t => t.strength !== 'core').length + ' adjacent' })));
        if (x.desc) box.append($('p', { text: x.desc }));
        if (x.def) box.append($('div', { class: 'srcs' }, $('a', { class: 'src', href: x.def, target: '_blank', rel: 'noopener' }, 'defined on ' + host(x.def))));
        const grid = $('div', { class: 'brands' });
        tags.forEach(t => {
          const pcs = piecesOf(t.maker), other = tagsOf(t.maker).filter(o => o.scene !== x.id);
          const body = $('div', { class: 'bbody' });
          body.append($('div', {}, $('div', { class: 'label', text: 'Placed in this scene by' }), srcList(t.src)));
          if (pcs.length) body.append($('div', {}, $('div', { class: 'label', text: 'Signature pieces' }), $('div', { class: 'nfs' }, pcs.map(n => $('a', { class: 'nf', href: (n.src[0] || [])[0] || '#', target: '_blank', rel: 'noopener' }, n.name, $('small', { text: (kinds.get(n.kind) || {}).name || n.kind }))))));
          if (other.length) body.append($('div', {}, $('div', { class: 'label', text: 'Also in' }), $('div', { class: 'nfs' }, other.map(o => $('a', { class: 'nf', href: '#s-' + o.scene }, sceneName(o.scene), $('small', { text: o.strength }))))));
          const d = $('details', { class: 'brand' + (t.strength === 'core' ? ' core' : '') }, $('summary', {}, $('span', { text: mname(t.maker) }), $('span', { class: 'sub', text: t.strength + (pcs.length ? ' · ' + pcs.length : '') })), body);
          d.dataset.text = (mname(t.maker) + ' ' + x.name + ' ' + cl + ' ' + pcs.map(n => n.name).join(' ')).toLowerCase();
          grid.append(d);
        });
        box.append(grid); box.dataset.text = (x.name + ' ' + cl + ' ' + (x.desc || '')).toLowerCase();
        main.append(box);
      });
    });
    rail.append($('h2', { text: 'Scene clusters' }), ol);
  }

  function renderCoverage() {
    const main = document.getElementById('main'), rail = document.getElementById('rail'), C = D.coverage;
    const pct = x => (100 * x).toFixed(x >= 0.1 ? 1 : 2) + ' %';
    const maxShare = Math.max(...C.regions.map(r => Math.max(r.share, r.expected)), ...C.countries.map(r => Math.max(r.share, r.expected)));
    const bars = (a, e) => $('div', { class: 'bars', role: 'img', 'aria-label': 'actual ' + pct(a) + ', expected ' + pct(e) },
      $('span', { class: 'act', style: 'width:' + (100 * a / maxShare).toFixed(1) + '%' }), $('span', { class: 'exp', style: 'width:' + (100 * e / maxShare).toFixed(1) + '%' }));
    const ratioChip = q => q == null ? $('span', { class: 'sub', text: 'no reference' }) : $('span', { class: 'ratio ' + (q < 0.5 ? 'low' : q < 1 ? 'mid' : 'okr'), text: q.toFixed(2) });
    const flagged = C.countries.filter(r => r.flag);
    main.append($('div', { class: 'stats' }, [[C.known + C.unknown, 'clothing brands'], [C.countries.filter(r => r.brands).length, 'countries with brands'], [C.unknown, 'without a country'], [flagged.length, 'countries below half their share']]
      .map(([n, l]) => $('div', {}, $('b', { text: n.toLocaleString('en') }), $('span', { text: l })))));
    main.append($('p', { class: 'note', text: 'Coverage of clothing brands against a reference distribution of the world\'s brands, built from fetched figures: apparel market size (GDP where no market figure was found), trademark filing activity by origin, and Wikipedia brand counts, combined as a geometric mean. A ratio of 1 means a country holds its expected share; a country expected to hold at least 0.5 % of brands is flagged below 0.5. Thin countries were raised with depth passes; no attested brand was removed to balance the count.' }));
    main.append($('div', { class: 'legend' }, $('span', {}, $('i', { style: 'background:var(--accent)' }), 'actual share'), $('span', {}, $('i', { style: 'background:var(--muted);opacity:.55' }), 'expected share')));
    main.append($('h2', { class: 'sf', id: 'cov-regions', text: 'By region' }));
    const rt = $('tbody');
    C.regions.forEach(r => rt.append($('tr', {}, $('td', { text: r.region }), $('td', { class: 'num', text: r.brands.toLocaleString('en') }), $('td', { class: 'num', text: r.countries }),
      $('td', { class: 'num', text: pct(r.share) }), $('td', { class: 'num', text: pct(r.expected) }), $('td', {}, ratioChip(r.ratio)), $('td', {}, bars(r.share, r.expected)))));
    main.append($('div', { class: 'tw' }, $('table', { class: 'mk cov' }, $('thead', {}, $('tr', {}, [['Region'], ['Brands', 'num'], ['Countries', 'num'], ['Actual', 'num'], ['Expected', 'num'], ['Ratio'], ['Shares']].map(([h, c]) => $('th', c ? { class: c, text: h } : { text: h })))), rt)));
    main.append($('h2', { class: 'sf', id: 'cov-countries', text: 'By country' }));
    const ct = $('tbody');
    const rows = C.countries.slice().sort((a, b) => b.expected - a.expected || b.brands - a.brands).map(r => {
      const tr = $('tr', {}, $('td', { text: r.c }), $('td', { text: r.region }), $('td', { class: 'num', text: r.brands.toLocaleString('en') }), $('td', { class: 'num', text: pct(r.share) }),
        $('td', { class: 'num', text: r.expected ? pct(r.expected) : '–' }), $('td', {}, ratioChip(r.ratio)), $('td', {}, bars(r.share, r.expected)));
      tr.dataset.text = (r.c + ' ' + r.region).toLowerCase(); return tr; });
    rows.forEach(r => ct.append(r));
    main.append($('div', { class: 'tw' }, $('table', { class: 'mk cov' }, $('thead', {}, $('tr', {}, [['Country'], ['Region'], ['Brands', 'num'], ['Actual', 'num'], ['Expected', 'num'], ['Ratio'], ['Shares']].map(([h, c]) => $('th', c ? { class: c, text: h } : { text: h })))), ct)));
    main._covRows = rows;
    const ol = $('ol', {}, $('li', {}, $('a', { href: '#cov-regions' }, 'By region', $('span', { text: C.regions.length }))), $('li', {}, $('a', { href: '#cov-countries' }, 'By country', $('span', { text: C.countries.length }))));
    rail.append($('h2', { text: 'Coverage' }), ol, $('p', { class: 'empty', text: 'Filter countries by code or region with the search box.' }));
  }

  function renderMakers() {
    const main = document.getElementById('main'), rail = document.getElementById('rail');
    const ids = Object.keys(D.makers).sort((a, b) => D.makers[a].name.localeCompare(D.makers[b].name));
    main.append($('div', { class: 'stats' }, [[D.ledger, 'makers in the ledger'], [ids.length, 'linked to a pilot kind']].map(([n, l]) => $('div', {}, $('b', { text: n.toLocaleString('en') }), $('span', { text: l })))));
    main.append($('p', { class: 'note', text: 'One maker ledger serves the whole domain. This list shows the makers tied to a pilot kind or category: through a named form, a line, a garment tie, or a category-level tie from a brand list (R-76). Producers known only from factory directories are in data/makers.tsv but not listed here.' }));
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
    if (main._covRows) main._covRows.forEach(r => r.classList.toggle('hidden-by-search', !!q && !r.dataset.text.includes(q)));
    main.querySelectorAll('section.scene').forEach(sec => {
      let any = false;
      sec.querySelectorAll('details.brand').forEach(d => { const hit = !q || d.dataset.text.includes(q) || sec.dataset.text.includes(q); d.classList.toggle('hidden-by-search', !hit); if (hit) any = true; });
      sec.classList.toggle('hidden-by-search', !!q && !any);
    });
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
    if (view === 'makers') renderMakers();
    else {
      if (hasScenes(view)) {
        const m = mode[view] || 'scene';
        const bar = $('div', { class: 'modes', role: 'group', 'aria-label': 'Navigate by' });
        [['scene', 'By scene'], ['tree', 'By garment'], ['coverage', 'Coverage']].forEach(([k, l]) => { const b = $('button', { type: 'button', 'aria-pressed': String(m === k), text: l }); b.addEventListener('click', () => { mode[view] = k; render(); }); bar.append(b); });
        document.getElementById('main').append(bar);
        if (m === 'scene') renderScenes(view); else if (m === 'coverage') renderCoverage(); else renderTree(view);
      } else renderTree(view);
    }
    applyFilter();
  }
  document.getElementById('q').addEventListener('input', applyFilter);
  if (!D.codes.some(c => c.code === view) && view !== 'makers') view = D.codes[0].code;
  render();
}
</script>
"""

if __name__ == "__main__":
    main()
