"""Build the stage-2 owner review page (pages/stage2_review.html) from
framework/structure/STAGE2_SUMMARY.md and STAGE2_OWNER_QUESTIONS.md.

The page is generated; edit the Markdown sources or this script, never the HTML.
Converts the Markdown subset those files use: headings, rules, paragraphs,
nested bullet and numbered lists, pipe tables, bold, italic, code and links.
"""
import html, re
from common import ROOT

SRC = ROOT / "framework" / "structure"
OUT = ROOT / "pages" / "stage2_review.html"

ID_RE = re.compile(r"(?<![\w-])((?:CV|K|[A-J])-\d+)(?![\w-])")


def slug(prefix, text):
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return f"{prefix}-{s[:60]}".rstrip("-")


def inline(text):
    codes = []
    def keep(m):
        codes.append(m.group(1))
        return f"\x00{len(codes) - 1}\x00"
    text = re.sub(r"`([^`]+)`", keep, text)
    t = html.escape(text, quote=False)
    def link(m):
        label, href = m.group(1), m.group(2)
        if href.endswith("STAGE2_OWNER_QUESTIONS.md"):
            return f'<a href="#questions" data-tab="questions">{label}</a>'
        if href.startswith("http"):
            return f'<a href="{html.escape(href)}">{label}</a>'
        return label
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)([^*]+?)\*(?![\w*])", r"<em>\1</em>", t)
    t = ID_RE.sub(r'<span class="qid">\1</span>', t)
    t = t.replace("★", '<span class="star" title="most consequential">★</span>')
    t = re.sub(r"\[(Rec: [^\]]+|yes|no|[^\]\[]{1,60})\]", lambda m: f'<span class="rec">[{m.group(1)}]</span>'
               if not m.group(1).startswith(("P:", "Probe")) else f'<span class="probe">[{m.group(1)}]</span>', t)
    return re.sub(r"\x00(\d+)\x00", lambda m: f"<code>{html.escape(codes[int(m.group(1))])}</code>", t)


def convert(md, prefix, toc):
    lines = md.splitlines()
    out, i, para = [], 0, []
    list_stack = []  # (indent, tag)

    def flush_para():
        if para:
            out.append(f"<p>{inline(' '.join(para))}</p>")
            para.clear()

    def close_lists(to_indent=-1):
        while list_stack and list_stack[-1][0] > to_indent:
            out.append(f"</li></{list_stack.pop()[1]}>")

    while i < len(lines):
        line = lines[i]
        s = line.strip()
        m_h = re.match(r"^(#{1,4})\s+(.*)", line)
        m_li = re.match(r"^(\s*)(?:([-*])|(\d+)\.)\s+(.*)", line)
        if not s:
            flush_para(); i += 1; continue
        if m_h:
            flush_para(); close_lists()
            level, text = len(m_h.group(1)), m_h.group(2).strip()
            hid = slug(prefix, text)
            if level in (2, 3):
                toc.append((level, hid, text))
            out.append(f'<h{level} id="{hid}">{inline(text)}</h{level}>')
            i += 1; continue
        if re.match(r"^-{3,}$", s):
            flush_para(); close_lists(); out.append("<hr>"); i += 1; continue
        if s.startswith("|"):
            flush_para(); close_lists()
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(lines[i].strip()); i += 1
            cells = [[c.strip() for c in r.strip("|").split("|")] for r in rows]
            body = [c for c in cells[1:] if not all(re.match(r"^:?-{2,}:?$", x) for x in c)]
            t = ['<div class="table-wrap"><table><thead><tr>']
            t += [f"<th>{inline(c)}</th>" for c in cells[0]]
            t.append("</tr></thead><tbody>")
            for r in body:
                t.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
            t.append("</tbody></table></div>")
            out.append("".join(t)); continue
        if m_li:
            flush_para()
            indent = len(m_li.group(1).replace("\t", "    "))
            tag = "ul" if m_li.group(2) else "ol"
            if list_stack and indent < list_stack[-1][0]:
                close_lists(indent)
            if list_stack and list_stack[-1][0] == indent:
                if list_stack[-1][1] != tag:
                    out.append(f"</li></{list_stack.pop()[1]}>")
                    out.append(f"<{tag}><li>")
                    list_stack.append((indent, tag))
                else:
                    out.append("</li><li>")
            else:
                start = f' start="{m_li.group(3)}"' if tag == "ol" and m_li.group(3) not in (None, "1") else ""
                out.append(f"<{tag}{start}><li>")
                list_stack.append((indent, tag))
            out.append(inline(m_li.group(4)))
            i += 1; continue
        if list_stack and line.startswith(" "):
            out.append(" " + inline(s)); i += 1; continue
        close_lists()
        para.append(s); i += 1
    flush_para(); close_lists()
    return "\n".join(out)


def toc_html(toc):
    items = []
    for level, hid, text in toc:
        label = re.sub(r"[*`]", "", text)
        items.append(f'<li class="l{level}"><a href="#{hid}">{html.escape(label)}</a></li>')
    return "<ol class=\"toc\">" + "".join(items) + "</ol>"


CSS = """
/* Layout: sticky tab bar; two-column reading view (contents rail + text), one column on phones. */
:root {
  --bg: #f3f5f6; --surface: #ffffff; --fg: #1d2529; --muted: #5b676e; --rule: #d5dcdf;
  --accent: #1c5d78; --accent-soft: #e2eef3; --mark: #8a6200; --mark-soft: #f6edd4; --probe: #7a3b6b;
  --display: "Bricolage Grotesque", "Segoe UI", system-ui, sans-serif;
  --body: "Literata", Georgia, "Times New Roman", serif;
  --mono: "JetBrains Mono", ui-monospace, Menlo, Consolas, monospace;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --bg: #12181b; --surface: #182024; --fg: #e3e9ec; --muted: #9aa8ae; --rule: #2c383d;
  --accent: #7fc3df; --accent-soft: #1d3440; --mark: #e2b955; --mark-soft: #3a3016; --probe: #d99acb; color-scheme: dark } }
:root[data-theme="dark"] {
  --bg: #12181b; --surface: #182024; --fg: #e3e9ec; --muted: #9aa8ae; --rule: #2c383d;
  --accent: #7fc3df; --accent-soft: #1d3440; --mark: #e2b955; --mark-soft: #3a3016; --probe: #d99acb; color-scheme: dark }
* { box-sizing: border-box }
body { background: var(--bg); color: var(--fg); font: 16px/1.6 var(--body); }
body::before { content: ""; position: fixed; inset: 0 0 auto; height: env(safe-area-inset-top, 0px); z-index: 10; background: var(--surface); }
.bar { position: sticky; top: env(safe-area-inset-top, 0px); z-index: 5; background: var(--surface); border-bottom: 1px solid var(--rule);
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }
.bar-inner { max-width: 1180px; margin: 0 auto; display: flex; flex-wrap: wrap; align-items: center; gap: 8px 20px; padding-block: 10px; }
.brand { font: 700 15px/1.2 var(--display); letter-spacing: .01em; }
.brand small { display: block; font: 500 12px/1.3 var(--mono); color: var(--muted); letter-spacing: .04em; text-transform: uppercase; }
.tabs { display: flex; gap: 4px; margin-left: auto; }
.tabs button { font: 600 14px/1 var(--display); padding: 9px 14px; border-radius: 6px; border: 1px solid var(--rule); background: transparent; color: var(--fg); cursor: pointer; }
.tabs button[aria-selected="true"] { background: var(--accent); border-color: var(--accent); color: var(--surface); }
.tabs button:focus-visible, .search:focus-visible, a:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.wrap { max-width: 1180px; margin: 0 auto; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); padding-block: 28px 64px;
  display: grid; grid-template-columns: 250px minmax(0, 1fr); gap: 40px; }
nav.rail { position: sticky; top: calc(env(safe-area-inset-top, 0px) + 72px); align-self: start; max-height: calc(100vh - 96px); overflow-y: auto; font: 13px/1.4 var(--display); }
.rail h2 { font: 600 11px/1 var(--mono); text-transform: uppercase; letter-spacing: .08em; color: var(--muted); margin: 0 0 10px; }
.toc { list-style: none; margin: 0; padding: 0; display: grid; gap: 2px; }
.toc a { color: var(--fg); text-decoration: none; display: block; padding: 3px 8px; border-radius: 4px; }
.toc a:hover { background: var(--accent-soft); }
.toc .l3 a { padding-left: 20px; color: var(--muted); font-size: 12.5px; }
main { min-width: 0; }
.status { display: flex; flex-wrap: wrap; gap: 10px 24px; padding: 14px 18px; margin: 0 0 28px; background: var(--surface); border: 1px solid var(--rule); border-radius: 8px; font: 14px/1.4 var(--display); }
.status div { display: grid; }
.status b { font: 700 22px/1.1 var(--display); font-variant-numeric: tabular-nums; }
.status span { color: var(--muted); font-size: 12.5px; }
.note { font: 14px/1.5 var(--display); color: var(--muted); margin: 0 0 24px; }
article { max-width: 78ch; }
article h1 { font: 700 clamp(26px, 4vw, 36px)/1.15 var(--display); text-wrap: balance; margin: 0 0 12px; letter-spacing: -.01em; }
article h2 { font: 700 23px/1.25 var(--display); text-wrap: balance; margin: 44px 0 12px; padding-top: 14px; border-top: 2px solid var(--fg); }
article h3 { font: 650 18px/1.3 var(--display); margin: 30px 0 8px; color: var(--accent); }
article h4 { font: 650 16px/1.3 var(--display); margin: 22px 0 6px; }
article p, article li { font-size: 15.5px; }
article ul, article ol { padding-left: 22px; margin: 8px 0 14px; }
article li { margin: 5px 0; }
article li::marker { color: var(--muted); }
article hr { border: 0; border-top: 1px solid var(--rule); margin: 32px 0; }
a { color: var(--accent); }
code { font: 13px/1.4 var(--mono); background: var(--accent-soft); padding: 1px 5px; border-radius: 3px; overflow-wrap: anywhere; }
.qid { font: 600 12.5px/1 var(--mono); color: var(--accent); background: var(--accent-soft); padding: 2px 6px; border-radius: 4px; white-space: nowrap; }
.star { color: var(--mark); }
.rec { font: 600 13px/1.4 var(--display); color: var(--mark); background: var(--mark-soft); padding: 0 4px; border-radius: 3px; }
.probe { font: 600 13px/1.4 var(--display); color: var(--probe); }
.table-wrap { overflow-x: auto; margin: 14px 0 20px; border: 1px solid var(--rule); border-radius: 6px; background: var(--surface); }
article .table-wrap { max-width: none; width: min(100%, 100%); }
table { border-collapse: collapse; font: 13px/1.4 var(--display); min-width: 100%; }
th, td { text-align: left; vertical-align: top; padding: 7px 10px; border-bottom: 1px solid var(--rule); }
th { font: 600 11px/1.3 var(--mono); text-transform: uppercase; letter-spacing: .05em; color: var(--muted); background: var(--bg); position: sticky; top: 0; }
tbody tr:last-child td { border-bottom: 0; }
td:first-child { font-family: var(--mono); font-weight: 600; white-space: nowrap; }
.wide article { max-width: none; }
.search-row { display: flex; flex-wrap: wrap; gap: 8px 14px; align-items: center; margin: 0 0 24px; }
.search { font: 15px/1.2 var(--display); padding: 10px 12px; border: 1px solid var(--rule); border-radius: 6px; background: var(--surface); color: var(--fg); width: min(100%, 420px); }
.count { font: 13px/1.3 var(--mono); color: var(--muted); }
li.miss { display: none; }
@media (max-width: 860px) {
  .wrap { grid-template-columns: minmax(0, 1fr); gap: 20px; }
  nav.rail { position: static; max-height: none; border: 1px solid var(--rule); border-radius: 8px; padding: 12px; background: var(--surface); }
  .tabs { margin-left: 0; }
}
@media (prefers-reduced-motion: no-preference) { html { scroll-behavior: smooth; } }
"""

JS = """
(function () {
  const tabs = document.querySelectorAll('.tabs button');
  const views = { summary: document.getElementById('view-summary'), questions: document.getElementById('view-questions') };
  function show(name, scroll) {
    if (!views[name]) name = 'summary';
    tabs.forEach(b => b.setAttribute('aria-selected', String(b.dataset.tab === name)));
    Object.entries(views).forEach(([k, v]) => { v.hidden = k !== name; });
    if (scroll) window.scrollTo(0, 0);
  }
  tabs.forEach(b => b.addEventListener('click', () => { show(b.dataset.tab, true); history.replaceState(null, '', '#' + b.dataset.tab); }));
  document.querySelectorAll('a[data-tab]').forEach(a => a.addEventListener('click', e => { e.preventDefault(); show(a.dataset.tab, true); history.replaceState(null, '', '#' + a.dataset.tab); }));
  const h = location.hash.slice(1);
  if (h === 'questions' || h.startsWith('q-')) show('questions'); else show('summary');
  if (h.startsWith('q-') || h.startsWith('s-')) { const t = document.getElementById(h); if (t) t.scrollIntoView(); }
  document.querySelectorAll('nav.rail a').forEach(a => a.addEventListener('click', () => {
    const id = a.getAttribute('href').slice(1); show(id.startsWith('q-') ? 'questions' : 'summary');
  }));
  const box = document.getElementById('q-search'), count = document.getElementById('q-count');
  const items = Array.from(document.querySelectorAll('#view-questions article li'));
  function filter() {
    const q = box.value.trim().toLowerCase(); let n = 0;
    items.forEach(li => { const hit = !q || li.textContent.toLowerCase().includes(q); li.classList.toggle('miss', !hit); if (hit && q) n++; });
    count.textContent = q ? n + ' matching items' : items.length + ' items';
  }
  box.addEventListener('input', filter); filter();
})();
"""


def main():
    summary_md = (SRC / "STAGE2_SUMMARY.md").read_text(encoding="utf-8")
    questions_md = (SRC / "STAGE2_OWNER_QUESTIONS.md").read_text(encoding="utf-8")
    toc_s, toc_q = [], []
    s_html = convert(summary_md, "s", toc_s)
    q_html = convert(questions_md, "q", toc_q)
    k = len(re.findall(r"^- \*\*K-\d+", questions_md, re.M))
    cv = len(set(re.findall(r"\*\*CV-(\d+)\*\*", summary_md)))
    per = len(re.findall(r"^- \*\*[A-J]-\d+\*\*", questions_md, re.M))
    status = (f'<div class="status"><div><b>53</b><span>categories with a structure memo</span></div>'
              f'<div><b>{cv}</b><span>shared-rule questions (CV)</span></div>'
              f'<div><b>{k}</b><span>framework questions (K)</span></div>'
              f'<div><b>{per}</b><span>per-category questions</span></div>'
              f'<div><b>0</b><span>approved so far</span></div></div>')
    page = f"""<title>Possession Taxonomy Stage 2</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,600;12..96,700&family=JetBrains+Mono:wght@500;600&family=Literata:opsz,wght@7..72,400;7..72,600&display=swap">
<style>{CSS}</style>
<header class="bar"><div class="bar-inner">
<div class="brand">Possession Taxonomy<small>Stage 2 · owner review · 2026-10-17</small></div>
<div class="tabs" role="tablist">
<button type="button" id="tab-summary" role="tab" data-tab="summary" aria-selected="true">Summary</button>
<button type="button" id="tab-questions" role="tab" data-tab="questions" aria-selected="false">All questions</button>
</div></div></header>
<section id="view-summary">
<div class="wrap"><nav class="rail" aria-label="Summary contents"><h2>Summary</h2>{toc_html(toc_s)}</nav>
<main>{status}<p class="note">Research proposals for review. Nothing here is approved, and no stage-2 change has been tested by blind placement yet. † in the memos marks a claim that still needs a fetched source.</p>
<article>{s_html}</article></main></div></section>
<section id="view-questions" hidden>
<div class="wrap"><nav class="rail" aria-label="Question lists"><h2>All questions</h2>{toc_html(toc_q)}</nav>
<main><div class="search-row"><input class="search" id="q-search" type="search" placeholder="Filter questions: an ID, object or word" aria-label="Filter questions"><span class="count" id="q-count"></span></div>
<article>{q_html}</article></main></div></section>
<script>{JS}</script>
"""
    OUT.parent.mkdir(exist_ok=True)
    tmp = OUT.with_suffix(".tmp")
    tmp.write_text(page, encoding="utf-8")
    tmp.replace(OUT)
    print(OUT, round(OUT.stat().st_size / 1024), "KB;", f"CV {cv}, K {k}, per-category {per}")


if __name__ == "__main__":
    main()
