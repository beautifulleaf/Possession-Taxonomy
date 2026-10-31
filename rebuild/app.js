const $ = (t, a = {}, ...kids) => { const e = document.createElement(t); for (const [k, v] of Object.entries(a)) { if (k === 'class') e.className = v; else if (k === 'text') e.textContent = v; else e.setAttribute(k, v); } kids.flat().forEach(c => c != null && e.append(c)); return e; };
const catName = c => (S.cats.find(x => x.c === c) || {}).n || c;
const cache = {}; let cur = null, data = null, view = 'cat';
const domsEl = document.getElementById('doms'), catsEl = document.getElementById('cats'), side = document.getElementById('side'), main = document.getElementById('main'), q = document.getElementById('q'), viewsEl = document.getElementById('views');
const MODE = { variety: 'Variety', tier: 'Tier', mixed: 'Mixed' };
let BR = null, TR = null;
async function getJSON(p) { if (!cache[p]) { const r = await fetch(p); if (!r.ok) throw new Error(r.status); cache[p] = await r.json(); } return cache[p]; }
async function brands() { if (!BR) { try { const j = await getJSON('reader/_brand_index.json'); BR = new Map(); j.b.forEach(b => [b[0], b[4]].filter(Boolean).forEach(n => { const k = n.toLowerCase(); if (!BR.has(k)) BR.set(k, []); BR.get(k).push(b); })); } catch (e) { BR = new Map(); } } return BR; }
const brandRow = (name, c) => { const rows = BR && BR.get(name.toLowerCase()); if (!rows) return null; return rows.find(b => b[3].includes(c)) || rows[0]; };
let tab = 'kinds', focusName = null;
function openBrand(name) { const b = brandRow(name, cur); if (!b) return; const cs = b[3]; open(cs.includes(cur) ? cur : cs[0], true, null, 'brands', b[0]); }
function setView(v) { view = v; viewsEl.querySelectorAll('button').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.v === v))); }
function showDom(d) { domsEl.querySelectorAll('.dom').forEach(b => b.setAttribute('aria-current', String(view === 'cat' && b.dataset.d === d)));
  catsEl.hidden = view !== 'cat';
  catsEl.replaceChildren(...S.cats.filter(c => c.d === d).map(c => { const b = $('button', { class: 'cat', type: 'button', 'data-c': c.c, 'aria-current': String(c.c === cur) }, c.n, $('small', { text: c.k + ' kinds' }));
    b.addEventListener('click', () => { q.value = ''; open(c.c, true); }); return b; })); }
S.domains.forEach(d => { const b = $('button', { class: 'dom', type: 'button', 'data-d': d.d, text: d.n });
  b.addEventListener('click', () => { q.value = ''; open(S.cats.find(c => c.d === d.d).c, true); }); domsEl.append(b); });
[['cat', 'Categories'], ['brands', 'Brands A–Z'], ['baby', 'Baby & child']].forEach(([v, l]) => { const b = $('button', { type: 'button', 'data-v': v, 'aria-pressed': 'false', text: l });
  b.addEventListener('click', () => { q.value = ''; if (v === 'cat') open(cur || S.cats[0].c, true); else if (v === 'brands') openBrandIndex(); else openBaby(); }); viewsEl.append(b); });
new ResizeObserver(() => document.documentElement.style.setProperty('--hh', document.querySelector('header').offsetHeight + 'px')).observe(document.querySelector('header'));
const hl = (text, term) => { if (!term || !text) return text; const i = text.toLowerCase().indexOf(term); if (i < 0) return text; return [text.slice(0, i), $('mark', { text: text.slice(i, i + term.length) }), text.slice(i + term.length)]; };
const slug = (...p) => p.join('-');
const meta = (...p) => p.filter(Boolean).join(' · ');
function makerEl(name) { if (!name) return null; const s = $('span', { class: 'mk' }, name);
  brands().then(m => { if (m.has(name.toLowerCase())) { s.classList.add('link'); s.setAttribute('role', 'link'); s.tabIndex = 0; const go = () => openBrand(name); s.addEventListener('click', go); s.addEventListener('keydown', e => { if (e.key === 'Enter') go(); }); } }); return s; }
function arch(x) {
  const box = $('div', { class: 'arch' }, $('div', { class: 'ah' }, $('b', { text: x.n }), x.mk || x.y ? $('i', {}, x.mk ? makerEl(x.mk) : null, x.mk && x.y ? ' · ' : '', x.y || '') : null));
  if (x.a) box.append($('p', { class: 'also', text: 'Also called ' + x.a }));
  if (x.d) box.append($('p', { class: 'desc', text: x.d }));
  if (x.v && x.v.length) box.append($('div', { class: 'vers' }, x.v.map(v => $('span', { class: 'chip ver', title: v.d || '' }, v.n, v.mk || v.y ? $('i', { text: meta(v.mk, v.y) }) : null))));
  if (x.dt) box.append($('p', { class: 'also', text: 'Details: ' + x.dt }));
  if (x.ex) box.append($('p', { class: 'also', text: 'Example: ' + x.ex }));
  if (x.s) box.append($('p', { class: 'src' }, $('a', { href: x.s, target: '_blank', rel: 'noopener', text: 'source' })));
  return box;
}
function item(k, term) {
  const a = $('article', { class: 'item' + (k.x && k.x.length ? ' wide' : '') }, $('h5', {}, hl(k.n, term)));
  if (k.a) a.append($('p', { class: 'also' }, 'Also called ', hl(k.a, term)));
  if (k.d) a.append($('p', { class: 'desc', text: k.d }));
  if (k.t && k.t.length) a.append($('p', { class: 'also' }, 'Types: ', hl(k.t.join(' · '), term)));
  if (k.tg && k.tg.length) a.append($('p', { class: 'tags' }, k.tg.map(t => $('span', { class: 'tag', text: t }))));
  if (k.x && k.x.length) { const det = $('details', { class: 'models', open: '' }, $('summary', { text: k.x.length + (k.x.length === 1 ? ' archetype' : ' archetypes') }));
    det.append($('div', { class: 'archs' }, k.x.map(arch))); a.append(det); }
  const m = k.m || [], r = k.r || [];
  if (m.length || r.length) {
    const lab = [m.length ? m.length + (m.length === 1 ? ' model' : ' models') : '', r.length ? r.length + (r.length === 1 ? ' range' : ' ranges') : ''].filter(Boolean).join(' · ');
    const det = $('details', { class: 'models' }, $('summary', { text: (k.x && k.x.length ? 'Other ' : '') + lab }));
    det.addEventListener('toggle', () => { if (!det.open || det.dataset.f) return; det.dataset.f = 1; const ch = $('div', { class: 'chips' });
      r.forEach(([n, mk]) => ch.append($('span', { class: 'chip range', title: "a maker's range covering several models" }, n, mk ? $('i', {}, makerEl(mk)) : null)));
      m.forEach(([n, mk]) => ch.append($('span', { class: 'chip' }, n, mk ? $('i', {}, makerEl(mk)) : null))); det.append(ch); });
    a.append(det);
  }
  if (k.s) a.append($('p', { class: 'src' }, $('a', { href: k.s, target: '_blank', rel: 'noopener', text: 'source' })));
  return a;
}
function best(list) { return $('div', { class: 'best' }, $('h4', { text: 'What makes a good one' }), $('ol', {}, list.map(b => $('li', {}, $('b', { text: b.m }), b.v ? [': ', $('span', { class: 'v', text: b.v })] : null, b.w ? '. ' + b.w : '')))); }
async function open(c, top, target, t, focus) {
  if (c !== cur || t) tab = t || 'kinds'; focusName = focus || null;
  setView('cat'); cur = c; showDom(c[0]);
  try { localStorage.setItem('reader-cat', c); } catch (e) {}
  main.replaceChildren($('p', { class: 'none', text: 'Loading ' + catName(c) + '…' })); side.replaceChildren();
  try { data = await getJSON('reader/' + c + '.json'); } catch (e) { main.replaceChildren($('p', { class: 'none', text: 'This category did not load (' + e.message + '). Choose it again to retry.' })); return; }
  if (cur !== c || view !== 'cat') return;
  render(); if (top) window.scrollTo({ top: 0 });
  if (target) document.getElementById(target)?.scrollIntoView();
}
let mode = 'scene';
function tabBar() {
  const ci = S.cats.find(x => x.c === cur) || {};
  const tabs = [['kinds', 'Kinds', ci.k], ['brands', 'Brands', ci.nb], ['traditions', 'Traditions', ci.nt], ['species', 'Rare species', ci.ns]].filter(([k, , n]) => k === 'kinds' || n);
  if (tabs.length < 2) return null;
  const bar = $('div', { class: 'modes', role: 'group', 'aria-label': 'Show' });
  tabs.forEach(([k, l, n]) => { const b = $('button', { type: 'button', 'aria-pressed': String(tab === k) }, l, $('span', { class: 'n', text: ' ' + (n || 0) })); b.addEventListener('click', () => { tab = k; focusName = null; render(); window.scrollTo({ top: 0 }); }); bar.append(b); });
  return bar;
}
function render() {
  if (tab !== 'kinds') return renderRegister();
  const hasScenes = !!(data.scenes && data.scenes.length);
  if (!hasScenes) return renderTree();
  const bar = $('div', { class: 'modes', role: 'group', 'aria-label': 'Browse by' });
  [['scene', 'By scene'], ['tree', 'By garment']].forEach(([k, l]) => { const b = $('button', { type: 'button', 'aria-pressed': String(mode === k), text: l }); b.addEventListener('click', () => { mode = k; render(); window.scrollTo({ top: 0 }); }); bar.append(b); });
  if (mode === 'tree') renderTree(); else renderScenes();
  main.insertBefore(bar, main.children[1] || null);
  const tb = tabBar(); if (tb) main.insertBefore(tb, main.children[1] || null);
}
function sceneBox(x, id, depth) {
  const core = x.b.filter(b => b[1]).length;
  const box = $('section', { class: 'scene' + (depth ? ' sub' : ''), id }, $(depth ? 'h5' : 'h4', {}, x.n, $('span', { text: core + ' defining' + (x.b.length - core ? ' · ' + (x.b.length - core) + ' also worn' : '') })));
  if (x.d) box.append($('p', { text: x.d }));
  if (x.g && x.g.length) box.append($('p', { class: 'also' }, 'Defining garments: ', x.g.join(' · ')));
  const br = $('div', { class: 'brands' });
  x.b.forEach(([nm, c, pcs]) => br.append($('details', { class: 'brand' + (c ? ' core' : '') }, $('summary', {}, nm, $('i', { text: c ? 'defines it' : 'also worn' })), $('div', {}, pcs && pcs.length ? 'Signature pieces: ' + pcs.join(', ') + '. ' : '', $('span', {}, 'Brand page: ', makerEl(nm))))));
  box.append(br);
  (x.c || []).forEach((y, k) => box.append(sceneBox(y, id + '-' + k, depth + 1)));
  return box;
}
function renderScenes() {
  const ol = $('ol');
  data.scenes.forEach((c, i) => { const li = $('li', { class: 'd' }, $('a', { href: '#' + slug('c', i) }, c.n, $('span', { text: c.s.length })));
    li.append($('ol', {}, c.s.map((x, j) => $('li', {}, $('a', { href: '#' + slug('x', i, j) }, x.n, $('span', { text: (x.c || []).length ? (x.c.length + 1) + ' styles' : '' })))))); ol.append(li); });
  side.replaceChildren($('h2', { text: catName(cur) + ' by scene' }), ol);
  const n = data.scenes.reduce((a, c) => a + c.s.reduce((b, x) => b + 1 + (x.c || []).length, 0), 0);
  main.replaceChildren($('div', { class: 'cat-head' }, $('h2', { text: catName(cur) }), $('p', { text: n + ' scenes and styles in ' + data.scenes.length + ' groups. Each lists its defining garments and the brands that define it; sub-styles sit under their parent. Brand names open the brand register.' })));
  data.scenes.forEach((c, i) => { const sec = $('section', { class: 'dept', id: slug('c', i) }, $('h3', { class: 'dept-name', text: c.n }));
    c.s.forEach((x, j) => sec.append(sceneBox(x, slug('x', i, j), 0))); main.append(sec); });
  spy();
}
function renderTree() {
  const total = data.depts.reduce((a, d) => a + d.s.reduce((b, s) => b + s.k.length, 0), 0);
  const ol = $('ol');
  data.depts.forEach((d, i) => { const n = d.s.reduce((a, s) => a + s.k.length, 0);
    const li = $('li', { class: 'd' }, $('a', { href: '#' + slug('d', i) }, d.n, $('span', { text: n })));
    if (d.s.length > 1) li.append($('ol', {}, d.s.map((s, j) => $('li', {}, $('a', { href: '#' + slug('s', i, j) }, s.n, $('span', { text: s.k.length }))))));
    ol.append(li); });
  side.replaceChildren($('h2', { text: catName(cur) }), ol);
  main.replaceChildren();
  main.append($('div', { class: 'cat-head' }, $('h2', { text: catName(cur) }), $('p', { text: (data.lead ? data.lead + ' ' : '') + total + ' kinds in ' + data.depts.length + (data.depts.length === 1 ? ' department.' : ' departments.') })));
  const tb = tabBar(); if (tb) main.append(tb);
  if ((data.b || []).length) main.append(best(data.b));
  data.depts.forEach((d, i) => {
    const sec = $('section', { class: 'dept', id: slug('d', i) }, $('h3', { class: 'dept-name' }, d.n, d.mode ? $('span', { class: 'mode', text: MODE[d.mode] || d.mode }) : null));
    if (d.note) sec.append($('p', { class: 'note', text: d.note }));
    if ((d.b || []).length) sec.append(best(d.b));
    d.s.forEach((s, j) => sec.append($('section', { class: 'shelf', id: slug('s', i, j) }, (d.s.length > 1 || s.n !== d.n) ? $('h4', { class: 'shelf-name' }, s.n, $('span', { text: s.k.length + (s.k.length === 1 ? ' kind' : ' kinds') })) : null, $('div', { class: 'items' }, s.k.map(k => item(k))))));
    main.append(sec);
  });
  spy();
}
const SEG_ORDER = ["Luxury house", "Designer", "Contemporary & premium", "Heritage & workwear", "Japanese & denim", "Streetwear", "Outdoor & technical", "Athletic & sportswear", "High street", "Value & basics", "Bespoke & artisan", "Traditional & national dress", "Subculture & alternative", "Haute maison", "Independent maker", "Premium", "Mainstream", "Value", "Traditional & regional", "Professional & flagship", "Heritage manufactory", "Artisan & independent", "Specialist", "Own-label & retailer", "Institution & issuer"];
async function renderRegister() {
  const c = cur, t = tab, file = 'reader/' + t + '/' + c + '.json';
  side.replaceChildren(); main.replaceChildren($('p', { class: 'none', text: 'Loading…' }));
  let j; try { j = await getJSON(file); } catch (e) { main.replaceChildren($('p', { class: 'none', text: 'This list did not load (' + e.message + '). Choose the tab again to retry.' })); return; }
  if (cur !== c || tab !== t || view !== 'cat') return;
  const list = j.b || j.t || j.i || [];
  const groupOf = t === 'brands' ? (e => e.stub ? 'Listed only (no details yet)' : (e.seg || 'Other')) : (e => e.g || 'Other');
  const groups0 = new Map(); list.forEach(e => { const g = groupOf(e); if (!groups0.has(g)) groups0.set(g, []); groups0.get(g).push(e); });
  const rank = g => { const i = SEG_ORDER.indexOf(g); return i < 0 ? 999 : i; };
  const groups = new Map([...groups0.entries()].sort((a, b) => t === 'brands' ? rank(a[0]) - rank(b[0]) || a[0].localeCompare(b[0]) : b[1].length - a[1].length || a[0].localeCompare(b[0])));
  const ol = $('ol'); [...groups.keys()].forEach((g, i) => ol.append($('li', {}, $('a', { href: '#' + slug('g', i) }, g, $('span', { text: groups.get(g).length })))));
  const title = { brands: 'Brands', traditions: 'Traditions', species: 'Rare species' }[t];
  side.replaceChildren($('h2', { text: catName(c) + ': ' + title }), ol);
  const blurb = { brands: ' brands, makers and houses in this category, grouped by segment. A brand that also appears elsewhere lists those categories.', traditions: ' craft and faith traditions behind objects in this category: origin, technique, materials, signature forms, centres and how to tell the real thing.', species: ' rarer species collected as specimens. The tree keeps the popular collector species; these are listed by class.' }[t];
  main.replaceChildren($('div', { class: 'cat-head' }, $('h2', { text: catName(c) }), $('p', { text: list.length + blurb })));
  const tb = tabBar(); if (tb) main.append(tb);
  const card = t === 'brands' ? brandCard : t === 'traditions' ? tradCard : speciesCard;
  // long lists (Clothing has ~1,750 brands): compact rows that build the full card when opened, sections added in batches
  const compact = list.length > 120;
  const bid = n => 'b-' + n.toLowerCase().replace(/[^a-z0-9]+/g, '-');
  const row = e => { const d = $('details', { class: 'brow', id: t === 'brands' ? bid(e.n) : null }, $('summary', {}, $('b', { text: e.n }), e.kf || e.g ? $('i', { text: e.kf || '' }) : null));
    d.addEventListener('toggle', () => { if (d.open && !d.dataset.f) { d.dataset.f = 1; const c = card(e); c.removeAttribute('id'); d.append(c); } }); return d; };
  const keys = [...groups.keys()];
  const fid = focusName ? bid(focusName) : null; focusName = null;
  const doFocus = () => { const el = fid && document.getElementById(fid); if (!el) return false; if (el.tagName === 'DETAILS') el.open = true; el.scrollIntoView({ block: 'center' }); el.style.outline = '2px solid var(--flag)'; return true; };
  let i = 0, focused = false;
  const step = () => { if (cur !== c || tab !== t || view !== 'cat') return;
    const end = Math.min(keys.length, i + (compact ? 2 : keys.length));
    for (; i < end; i++) { const g = keys[i]; const sec = $('section', { class: 'dept', id: slug('g', i) }, $('h3', { class: 'dept-name' }, g, $('span', { class: 'mode', text: String(groups.get(g).length) })));
      const items = groups.get(g).sort((a, b) => a.n.localeCompare(b.n));
      sec.append(compact ? $('div', { class: 'brows' }, items.map(row)) : $('div', { class: 'items' }, items.map(card))); main.append(sec); }
    if (!focused) focused = doFocus();
    if (i < keys.length) setTimeout(step, 0); else spy(); };
  step();
}
async function openBrandIndex() {
  setView('brands'); showDom(''); side.replaceChildren(); main.replaceChildren($('p', { class: 'none', text: 'Loading brands…' }));
  const m = await brands(); if (view !== 'brands') return;
  if (!m.size) { main.replaceChildren($('p', { class: 'none', text: 'The brand index did not load. Choose Brands A–Z again to retry.' })); return; }
  const all = [...new Set([...m.values()].flat())].sort((a, b) => a[0].localeCompare(b[0]));
  const letter = n => { const ch = n.normalize('NFD').replace(/[^A-Za-z0-9]/g, '').charAt(0).toUpperCase(); return /[A-Z]/.test(ch) ? ch : '#'; };
  const groups = new Map(); all.forEach(b => { const l = letter(b[0]); if (!groups.has(l)) groups.set(l, []); groups.get(l).push(b); });
  const keys = [...groups.keys()].sort((a, b) => (a === '#') - (b === '#') || a.localeCompare(b));
  const ol = $('ol'); keys.forEach((l, i) => ol.append($('li', {}, $('a', { href: '#' + slug('l', i) }, l, $('span', { text: groups.get(l).length })))));
  side.replaceChildren($('h2', { text: 'Brands A–Z' }), ol);
  main.replaceChildren($('div', { class: 'cat-head' }, $('h2', { text: 'Brands A–Z' }), $('p', { text: all.length + ' brands, makers and houses across every category. Each brand is described inside its categories (the Brands tab); choose a category to open the full entry there.' })));
  keys.forEach((l, i) => { const sec = $('section', { class: 'dept', id: slug('l', i) }, $('h3', { class: 'dept-name', text: l }));
    sec.append($('div', { class: 'hits' }, groups.get(l).map(([n, seg, kf, cs]) => $('div', { class: 'hit' }, $('span', {}, n, kf ? $('span', { class: 'also', text: ' · ' + kf }) : null), $('p', { class: 'tags' }, cs.map(c => { const t = $('button', { class: 'tag link', type: 'button', text: catName(c) }); t.addEventListener('click', () => open(c, true, null, 'brands', n)); return t; })))))); main.append(sec); });
  spy();
}
function brandCard(b) {
  const a = $('article', { class: 'item', id: 'b-' + b.n.toLowerCase().replace(/[^a-z0-9]+/g, '-') }, $('h5', { text: b.n }), $('p', { class: 'also', text: meta(b.c, b.f, b.seg) }));
  if (b.d) a.append($('p', { class: 'desc', text: b.d }));
  const row = (l, v) => v && v.length ? a.append($('p', { class: 'also' }, l + ': ', v.join(' · '))) : null;
  if (b.kf) a.append($('p', { class: 'also', text: 'Known for: ' + b.kf }));
  row('Lines', b.lines); row('Eras', b.eras); row('Signature', b.sig); row('Scenes', b.sc); row('Related', b.rel);
  if (b.cats && b.cats.length) a.append($('p', { class: 'tags' }, b.cats.map(c => { const t = $('button', { class: 'tag link', type: 'button', text: catName(c) }); t.addEventListener('click', () => open(c, true, null, 'brands', b.n)); return t; })));
  if (b.s) a.append($('p', { class: 'src' }, $('a', { href: b.s, target: '_blank', rel: 'noopener', text: 'source' })));
  return a;
}
function tradCard(t) {
  const a = $('article', { class: 'item' }, $('h5', { text: t.n }), $('p', { class: 'also', text: meta(t.r, t.p) }));
  if (t.d) a.append($('p', { class: 'desc', text: t.d }));
  [['Technique', t.tech], ['Materials', t.mat], ['Signature forms', t.forms], ['Centres and masters', t.ctr], ['Authenticity', t.auth]].forEach(([l, v]) => { if (v && v.length) a.append($('p', { class: 'also' }, l + ': ', Array.isArray(v) ? v.join(' · ') : v)); });
  if (t.cats && t.cats.length > 1) a.append($('p', { class: 'tags' }, t.cats.map(c => { const b = $('button', { class: 'tag link', type: 'button', text: catName(c) }); b.addEventListener('click', () => open(c, true, null, 'traditions')); return b; })));
  if (t.s) a.append($('p', { class: 'src' }, $('a', { href: t.s, target: '_blank', rel: 'noopener', text: 'source' })));
  return a;
}
function speciesCard(e) {
  const a = $('article', { class: 'item' }, $('h5', { text: e.n }));
  if (e.a) a.append($('p', { class: 'also', text: e.a }));
  if (e.d) a.append($('p', { class: 'desc', text: e.d }));
  if (e.m && e.m.length) a.append($('p', { class: 'also' }, 'Examples: ', e.m.join(' · ')));
  if (e.s) a.append($('p', { class: 'src' }, $('a', { href: e.s, target: '_blank', rel: 'noopener', text: 'source' })));
  return a;
}
async function openBaby() {
  setView('baby'); showDom(''); side.replaceChildren(); main.replaceChildren($('p', { class: 'none', text: 'Loading…' }));
  let j; try { j = await getJSON('reader/_baby.json'); } catch (e) { main.replaceChildren($('p', { class: 'none', text: 'This view has not been published yet.' })); return; }
  if (view !== 'baby') return;
  const groups = new Map(); j.i.forEach(([c, n, d]) => { if (!groups.has(c)) groups.set(c, []); groups.get(c).push([n, d]); });
  const ol = $('ol'); [...groups.keys()].forEach((c, i) => ol.append($('li', {}, $('a', { href: '#' + slug('y', i) }, catName(c), $('span', { text: groups.get(c).length })))));
  side.replaceChildren($('h2', { text: 'Baby & child' }), ol);
  main.replaceChildren($('div', { class: 'cat-head' }, $('h2', { text: 'Baby & child' }), $('p', { text: j.i.length + ' kinds for babies and children, gathered from every category. Each stays in its own category; choose one to open it there.' })));
  [...groups.keys()].forEach((c, i) => { const sec = $('section', { class: 'dept', id: slug('y', i) }, $('h3', { class: 'dept-name', text: catName(c) }));
    sec.append($('div', { class: 'hits' }, groups.get(c).map(([n, d]) => { const b = $('button', { class: 'hit', type: 'button' }, $('span', { text: n }), $('i', { text: d || '' })); b.addEventListener('click', () => jump(c, n)); return b; }))); main.append(sec); });
  spy();
}
async function jump(c, n) { q.value = ''; await open(c, true, null, 'kinds'); const el = [...main.querySelectorAll('article.item h5')].find(h => h.textContent === n); if (el) { el.closest('article').scrollIntoView({ block: 'center' }); el.closest('article').style.outline = '2px solid var(--flag)'; } }
function search() {
  const term = q.value.trim().toLowerCase();
  if (!term) { if (view === 'cat' && data) render(); else if (view === 'brands') openBrandIndex(); return; }
  const hits = S.index.filter(([c, n, a]) => (n + ' ' + a).toLowerCase().includes(term)).slice(0, 200);
  main.replaceChildren($('div', { class: 'cat-head' }, $('h2', { text: 'Search' }), $('p', { text: hits.length ? (hits.length === 200 ? 'The first 200 results' : hits.length + (hits.length === 1 ? ' result' : ' results')) + ' for "' + q.value.trim() + '". Choose one to open it in its category.' : 'Nothing is named "' + q.value.trim() + '". Try another word for it, or browse a category above.' })));
  main.append($('div', { class: 'hits' }, hits.map(([c, n, a, p]) => { const b = $('button', { class: 'hit', type: 'button' }, $('span', {}, hl(n, term), p ? $('span', { class: 'also' }, ' · ', p) : null, a ? $('span', { class: 'also' }, ' · ', hl(a, term)) : null), $('i', { text: catName(c) }));
    b.addEventListener('click', () => jump(c, p || n)); return b; })));
}
let spyObs;
function spy() {
  spyObs?.disconnect(); const links = new Map([...side.querySelectorAll('a')].map(a => [a.getAttribute('href').slice(1), a]));
  spyObs = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { side.querySelectorAll('a.on').forEach(x => x.classList.remove('on')); links.get(e.target.id)?.classList.add('on'); } }), { rootMargin: '-160px 0px -65% 0px' });
  main.querySelectorAll('section.shelf, section.dept, section.scene').forEach(s => spyObs.observe(s));
}
side.addEventListener('click', e => { const a = e.target.closest('a[href^="#"]'); if (!a) return; e.preventDefault(); document.getElementById(a.getAttribute('href').slice(1))?.scrollIntoView(); });
q.addEventListener('input', search);
let start = 'A1'; try { start = localStorage.getItem('reader-cat') || start; } catch (e) {}
const h = location.hash.slice(1); if (S.cats.some(c => c.c === h)) start = h;
if (!S.cats.some(c => c.c === start)) start = S.cats[0].c;
open(start);
