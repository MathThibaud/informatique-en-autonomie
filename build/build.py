"""Construit docs/ (Markdown MkDocs) à partir des livres d'édition Overleaf des 3 niveaux.

Usage : .venv/bin/python build/build.py [terminale premiere seconde] [--no-figures]
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from collections import OrderedDict
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
from texparse import find_group, read_arg, read_opt, strip_comments  # noqa: E402
from tex2md import Converter  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / 'docs'
CACHE = ROOT / '.cache'
OVERLEAF = Path.home() / 'Documents' / 'Overleaf'

LEVELS = OrderedDict([
    ('seconde', dict(dir='Seconde', titre='Seconde', matiere='SNT',
                     long='Sciences numériques et technologie')),
    ('premiere', dict(dir='Premiere', titre='Première', matiere='NSI',
                      long='Numérique et sciences informatiques')),
    ('terminale', dict(dir='Terminale', titre='Terminale', matiere='NSI',
                       long='Numérique et sciences informatiques')),
])

RUB = OrderedDict([('act', ('activites', 'Activités préparatoires')),
                   ('cours', ('cours', 'Cours')),
                   ('ex', ('exercices', 'Exercices')),
                   ('tp', ('tp', 'TP et projets')),
                   ('aoc', ('defis', 'Défis Advent of Code'))])
CRUB = {'c-act': 'act', 'c-ex': 'ex', 'c-tp': 'tp', 'c-aoc': 'aoc'}


def slugify(t):
    t = unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode()
    t = re.sub(r'[^a-zA-Z0-9]+', '-', t).strip('-').lower()
    return t[:40].strip('-')


def clean_title(t):
    t = re.sub(r'\\textsuperscript\{([^}]*)\}', r'\1', t)
    t = t.replace('---', '—').replace('--', '–').replace('\\,', ' ').replace('~', ' ')
    t = re.sub(r"\\'\{?e\}?", 'é', t)
    t = re.sub(r'\\[a-zA-Z]+\*?', '', t)
    return re.sub(r'[{}]', '', t).strip()


# ------------------------------------------------------------------ structure
class Chapter:
    def __init__(self, title, num, slug):
        self.title = title
        self.num = num
        self.slug = slug
        self.rub = OrderedDict()
        self.corr = OrderedDict()
        self.ouverture = None


def parse_book(path):
    tex = Path(path).read_text(encoding='utf-8')
    body = tex.split('\\begin{document}', 1)[1].split('\\end{document}')[0]
    body = '\n'.join(l for l in body.split('\n') if not l.lstrip().startswith('%'))
    book = dict(front=[], chapters=[], pratique_intro=[], pratique=[], credits=[], annexes=[])
    part = 0
    chap = None
    target = None
    numch = 0
    by_title = {}
    lines = body.split('\n')
    for line in lines:
        st = line.strip()
        if not st or st in ('\\clearpage', '\\mainmatter', '\\frontmatter', '\\tableofcontents',
                            '\\bandeaupagetitre', '\\cleartorecto') or st.startswith('\\lignesommaire'):
            continue
        if st.startswith('\\begin{titlepage}'):
            target = None
            part = -1
            continue
        if part == -1:
            if st.startswith('\\end{titlepage}'):
                part = 0
            continue
        if st.startswith('\\renewcommand{\\contentsname}'):
            continue
        m = re.match(r'\\partpage\{([^}]*)\}\{([^}]*)\}', st)
        if m:
            t = m.group(2)
            part = 3 if 'Corrig' in t else 2 if 'pratique' in t.lower() else 1
            target = None
            continue
        m = re.search(r'\\chapter(\*?)\{', st)
        if m:
            arg, _ = find_group(st, m.end() - 1)
            toc = re.search(r'\\addcontentsline\{toc\}\{chapter\}\{', st)
            title = clean_title(find_group(st, toc.end() - 1)[0] if toc else arg)
            star = m.group(1) == '*'
            if part <= 0:
                page = dict(title=title, items=[], slug=slugify(title))
                book['front'].append(page)
                target = page['items']
            elif part == 1:
                if 'synth' in title.lower():
                    chap = Chapter(title, None, 'synthese')
                    book['synthese'] = chap
                    chap.rub['ex'] = []
                    target = chap.rub['ex']
                else:
                    if not star:
                        numch += 1
                        num = numch
                        slug = '%02d-%s' % (num, slugify(title))
                    else:
                        num = None
                        slug = slugify(title.replace('Complément', ''))
                    chap = Chapter(title, num, slug)
                    book['chapters'].append(chap)
                    by_title[title] = chap
                    target = None
            elif part == 2:
                mm = re.match(r'Sujet (\d+)', title)
                if mm:
                    page = dict(title=title, num=int(mm.group(1)), items=[], corr=[])
                    book['pratique'].append(page)
                    target = page['items']
                else:
                    target = book['pratique_intro']
            elif part == 3:
                mm = re.match(r'Corrigé du sujet (\d+)', title)
                if mm:
                    p = [x for x in book['pratique'] if x['num'] == int(mm.group(1))][0]
                    target = p['corr']
                elif 'Crédits' in title:
                    target = book['credits']
                elif 'synth' in title.lower():
                    chap = book['synthese']
                    chap.corr['ex'] = []
                    target = chap.corr['ex']
                elif title in by_title:
                    chap = by_title[title]
                    target = None
                else:
                    page = dict(title=title, items=[], slug=slugify(title))
                    book['annexes'].append(page)
                    target = page['items']
            rest = st[st.index('}', m.end()) + 1:] if False else ''
            continue
        m = re.match(r'\\pagetitrechapitre\{([^}]*)\}', st)
        if m:
            if chap is not None:
                chap.ouverture = m.group(1)
            continue
        m = re.search(r'\\rubrique\*?\[([^\]]*)\]\{([^}]*)\}', st)
        if m:
            typ = m.group(1)
            if part == 3:
                key = CRUB.get(typ, typ)
                target = chap.corr.setdefault(key, [])
            else:
                target = chap.rub.setdefault(typ, [])
            continue
        if st.startswith('\\renewcommand{\\theHchapter}') or st.startswith('\\markboth') \
                or re.match(r'^\\(phantomsection|addcontentsline)', st) and 'Frise' not in st:
            continue
        m = re.match(r'\\input\{chapitres_edition/([^}]*)\}', st)
        if m:
            if target is not None:
                target.append(('input', m.group(1)))
            continue
        if re.match(r'^\\phantomsection\\addcontentsline\{toc\}\{chapter\}\{([^}]*)\}', st):
            title = re.search(r'\{chapter\}\{([^}]*)\}', st).group(1)
            page = dict(title=title, items=[], slug=slugify(title))
            book['front'].append(page)
            target = page['items']
            continue
        if target is not None:
            target.append(('raw', line))
    return book


def merge_items(items):
    out = []
    for kind, v in items:
        if kind == 'raw' and out and out[-1][0] == 'raw':
            out[-1] = ('raw', out[-1][1] + '\n' + v)
        else:
            out.append((kind, v))
    return out


# ------------------------------------------------------------------- pages
class Site:
    def __init__(self, level, figures=True):
        self.level = level
        self.cfg = LEVELS[level]
        self.src = OVERLEAF / self.cfg['dir'] / 'livre_autonome'
        self.out = DOCS / level
        self.conv = Converter(level, str(self.src), str(self.out))
        self.pages = OrderedDict()       # chemin docs/ -> md
        self.nav = []
        self.figures = figures

    def read(self, name):
        return (self.src / 'chapitres_edition' / (name + '.tex')).read_text(encoding='utf-8')

    def conv_items(self, items, page, ctx, mode='page'):
        mds = []
        for kind, v in merge_items(items):
            tex = self.read(v) if kind == 'input' else v
            ctx['mode'] = mode
            ctx.setdefault('seq', {})['iadef'] = ''
            try:
                mds.append(self.conv.convert(tex, page, ctx))
            except Exception as e:  # on signale sans bloquer tout le site
                print('  !! %s (%s) : %s' % (v if kind == 'input' else 'raw', page, e))
                mds.append('\n!!! danger "Conversion impossible"\n    Ce passage n\'a pas pu être converti.\n')
        return '\n\n'.join(mds)

    def corr_chunks(self, items, page, ctx):
        """Convertit des corrigés et les découpe par exercice / activité."""
        if not items:
            return {}
        cctx = dict(counters={}, slug=ctx.get('slug'))
        md = self.conv_items(items, page, cctx, mode='corrige')
        chunks = OrderedDict()
        act = 0
        key = 'A0'
        for line in md.split('\n'):
            s = line.strip()
            m = re.fullmatch(r'QQCA(\d+)QQ', s)
            if m:
                act = int(m.group(1))
                key = 'A%d' % act
                continue
            m = re.fullmatch(r'QQCS(.+?)QQ', s)
            if m:
                key = m.group(1)
                continue
            m = re.fullmatch(r'QQCE(.+?)QQ', s)
            if m:
                key = 'A%d' % act
                continue
            chunks.setdefault(key, []).append(line)
        res = OrderedDict()
        for k, v in chunks.items():
            txt = '\n'.join(v).strip('\n')
            if txt.strip():
                res[k] = txt
        return res

    @staticmethod
    def collapsible(ind, kind, title, content, opened=False):
        lines = [ind + ('???+' if opened else '???') + ' %s "%s"' % (kind, title), '']
        for l in content.split('\n'):
            lines.append((ind + '    ' + l) if l.strip() else '')
        return '\n'.join(lines)

    def inject(self, md, chunks):
        chunks = OrderedDict(chunks)
        ex_keys = [k for k in chunks if not k.startswith('A')]
        # texte d'introduction d'un corrigé : rattaché au premier exercice de l'activité
        for k in [k for k in chunks if k.startswith('A')]:
            n = k[1:]
            cands = [e for e in ex_keys if e.startswith(n + '.')]
            if n == '0':
                cands += [e for e in ex_keys if '.' not in e]
            if cands:
                chunks[cands[0]] = chunks[k] + '\n\n' + chunks[cands[0]]
                del chunks[k]
        used = set()

        def slot(m):
            ind, key = m.group(1), m.group(2)
            c = chunks.get(key)
            if not c:
                return ''
            used.add(key)
            title = 'Corrigé' if not key.startswith('A') or key == 'A0' else "Corrigé de l'activité"
            return '\n' + self.collapsible(ind, 'corrige', title, c) + '\n'
        md = re.sub(r'^([ \t]*)QQSLOT(.+?)QQ[ \t]*$', slot, md, flags=re.M)
        rest = [(k, v) for k, v in chunks.items() if k not in used]
        if rest:
            extra = [self.collapsible('', 'corrige', 'Corrigé', v) for k, v in rest]
            md += '\n\n## Corrigé\n\n' + '\n\n'.join(extra) + '\n'
        return md

    def add(self, path, md):
        self.pages[path] = md

    def build(self):
        print('== %s' % self.level)
        book = parse_book(self.src / 'livre_edition.tex')
        self.book = book
        L = self.level
        nav = []
        # pages d'ouverture (et annexes : lexique...)
        for p in book['front'] + book['annexes']:
            slug = 'charte' if 'charte' in p['title'].lower() else p['slug']
            path = '%s/%s.md' % (L, slug)
            ctx = dict(counters={}, slug=slug)
            if slug == 'charte':
                self.conv.anchors['charte'] = path
            md = '# %s\n\n' % p['title'] + self.conv_items(p['items'], path, ctx)
            self.add(path, md)
            nav.append((p['title'], path))
        self.front_nav = nav[:len(book['front'])]
        self.annex_nav = nav[len(book['front']):]
        # chapitres
        self.chap_nav = []
        for ch in book['chapters'] + ([book['synthese']] if 'synthese' in book else []):
            self.build_chapter(ch)
        # épreuve pratique
        self.prat_nav = []
        if book['pratique']:
            path = '%s/pratique/index.md' % L
            ctx = dict(counters={}, slug='pratique')
            md = "# Épreuve pratique : sujets d'entraînement\n\n" + \
                self.conv_items(book['pratique_intro'], path, ctx)
            md += '\n\n' + '\n'.join('- [%s](%s.md)' % (p['title'], 'sujet-%d' % p['num'])
                                     for p in book['pratique'])
            md = md.replace("Les corrigés sont regroupés en fin de livre.",
                            "Le corrigé se déplie sous chaque exercice.")
            self.add(path, md)
            self.prat_nav.append(('Présentation', path))
            for p in book['pratique']:
                path = '%s/pratique/sujet-%d.md' % (L, p['num'])
                ctx = dict(counters={}, slug='p%d' % p['num'])
                md = '# %s\n\n' % p['title'] + self.conv_items(p['items'], path, ctx)
                chunks = self.corr_chunks(p['corr'], path, ctx)
                md = self.inject(md, chunks)
                self.add(path, md)
                self.prat_nav.append((p['title'].split('—')[0].strip(), path))
        # crédits
        if book['credits']:
            path = '%s/credits.md' % L
            md = '# Crédits iconographiques\n\n' + self.conv_items(book['credits'], path, dict(counters={}))
            self.add(path, md)

    def build_chapter(self, ch):
        L = self.level
        base = '%s/%s' % (L, ch.slug)
        ctx = dict(counters={}, slug=ch.slug)
        sub = []
        titre = ('%d. ' % ch.num if ch.num else '') + ch.title
        print('  ' + titre)
        for typ, items in ch.rub.items():
            if typ not in RUB:
                continue
            fname, label = RUB[typ]
            path = '%s/%s.md' % (base, fname)
            pctx = dict(counters=ctx['counters'], slug='%s-%s' % (ch.slug, typ))
            self.conv.anchors.setdefault('rub-%s-%s' % (ch.slug, typ), path)
            md = '# %s\n\n<p class="sous-titre">%s</p>\n\n' % (label, ch.title)
            md += self.conv_items(items, path, pctx)
            chunks = self.corr_chunks(ch.corr.get(typ, []), path, pctx)
            md = self.inject(md, chunks)
            self.add(path, md)
            sub.append((label, path))
            if ch.num:
                self.conv.anchors.setdefault('rub-%02d-%s' % (ch.num, typ), path)
                self.conv.anchors.setdefault('crub-%02d-%s' % (ch.num, typ), path)
        # page d'accueil du chapitre
        path = '%s/index.md' % base
        md = '# %s\n\n' % ch.title
        if ch.ouverture:
            img = self.find_img(ch.ouverture)
            if img:
                name = self.conv.image_name(img)
                md += '![](../img/%s){ .ouverture }\n\n' % name
        md += '<div class="grid cards rubriques" markdown>\n\n'
        icons = {'act': ':material-lightbulb-on-outline:', 'cours': ':material-book-open-variant:',
                 'ex': ':material-pencil-outline:', 'tp': ':material-laptop:',
                 'aoc': ':material-star-shooting-outline:'}
        for (label, p), typ in zip(sub, [t for t in ch.rub if t in RUB]):
            md += '-   [%s %s](%s)\n' % (icons[typ], label, os.path.basename(p))
        md += '\n</div>\n'
        self.add(path, md)
        self.chap_nav.append((titre, [('Présentation', path)] + sub))
        if ch.num:
            self.conv.anchors.setdefault('chap-%02d' % ch.num, path)

    def find_img(self, name):
        for ext in ('', '.pdf', '.png', '.jpg', '.jpeg'):
            p = self.src / 'img' / (name + ext)
            if p.is_file():
                return str(p)
        return None

    # -------------------------------------------------------------- écriture
    def resolve_links(self):
        A = self.conv.anchors

        def lk(page):
            def fn(m):
                a = m.group(1)
                target = A.get(a)
                if target is None and a.startswith('corr-'):
                    a = 'ex-' + a[5:]
                    target = A.get(a)
                if target is None:
                    mm = re.match(r'c?rub-(\d+)-(\w+)', a)
                    if mm:
                        target = A.get('rub-%s-%s' % mm.groups())
                if target is None:
                    self.conv.unknown['lien:' + a] = self.conv.unknown.get('lien:' + a, 0) + 1
                    return '#'
                rel = os.path.relpath(target, os.path.dirname(page))
                if target == page:
                    rel = ''
                is_page = a.startswith(('rub-', 'crub-', 'chap-', 'charte'))
                return rel + ('' if is_page else '#' + a)
            return fn
        def plain(m):
            a = m.group(2)
            if a in A or a.replace('corr-', 'ex-', 1) in A or re.match(r'c?rub-(\d+)-(\w+)', a):
                return m.group(0)
            return m.group(1)
        for page, md in self.pages.items():
            md = re.sub(r'\[([^\]]*)\]\(QQLK(.+?)QQ\)', plain, md)
            self.pages[page] = re.sub(r'QQLK(.+?)QQ', lk(page), md)

    def write(self):
        if self.out.exists():
            for p in self.out.glob('**/*.md'):
                p.unlink()
            for p in self.out.glob('**/* [0-9].*'):   # copies de synchronisation iCloud
                p.unlink()
        for page, md in self.pages.items():
            md = self.finalize(md, page)
            p = DOCS / page
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(md, encoding='utf-8')

    def finalize(self, md, page):
        # macros LaTeX résiduelles hors code et maths : signalées puis retirées
        out = []
        fence = False
        for line in md.split('\n'):
            if line.strip().startswith('```'):
                fence = not fence
                out.append(line)
                continue
            if not fence:
                parts = re.split(r'(\$\$.*?\$\$|\$[^$]*\$|`[^`]*`)', line)
                for k in range(0, len(parts), 2):
                    for mm in re.finditer(r'\\([a-zA-Z]+)', parts[k]):
                        name = mm.group(1)
                        self.conv.unknown[name] = self.conv.unknown.get(name, 0) + 1
                line = ''.join(parts)
                if 'QQ' in line:
                    self.conv.unknown['QQ'] = self.conv.unknown.get('QQ', 0) + 1
            out.append(line)
        md = '\n'.join(out)
        # emplacements de corrigé restés vides (pages sans corrigé)
        md = re.sub(r'^[ \t]*QQSLOT.+?QQ[ \t]*$', '', md, flags=re.M)
        # garde-fou : aucun marqueur interne ne doit atteindre une page publiée
        reste = re.search(r'QQ(?:SLOT|I\d|B\d|W\d|AB|AE|H\d|HE|LK|CS|CE|CA\d|FIG|LST|TIKZ|MATH|PCT|IMG|NOTITLE)\S*', md)
        if reste:
            raise SystemExit('Marqueur interne non résolu dans %s : %s' % (page, reste.group(0)))
        md = re.sub(r'\n{3,}', '\n\n', md)
        return md.strip() + '\n'

    # --------------------------------------------------------- figures/images
    def compile_figures(self):
        figdir = self.out / 'figures'
        figdir.mkdir(parents=True, exist_ok=True)
        for f in figdir.glob('*.svg'):
            if f.stem not in self.conv.figures or 'figure indisponible' in f.read_text(errors='ignore')[:400]:
                f.unlink()
        todo = {h: v for h, v in self.conv.figures.items() if not (figdir / (h + '.svg')).exists()}
        cache = CACHE / self.level
        cache.mkdir(parents=True, exist_ok=True)
        for h in list(todo):
            c = cache / (h + '.svg')
            if c.exists():
                shutil.copy(c, figdir / (h + '.svg'))
                del todo[h]
        print('  figures : %d au total, %d à compiler' % (len(self.conv.figures), len(todo)))
        if not todo:
            return
        tex = (self.src / 'livre_edition.tex').read_text(encoding='utf-8')
        preamble = tex.split('\\begin{document}')[0]
        preamble += '\n\\usepackage[active,tightpage]{preview}\\setlength\\PreviewBorder{3pt}\n'
        groups = OrderedDict()
        for h, (defs, code) in todo.items():
            groups.setdefault(defs, []).append((h, code))
        env = dict(os.environ, TEXINPUTS='%s//:%s:' % (self.src / 'style', self.src))
        for gi, (defs, figs) in enumerate(groups.items()):
            for start in range(0, len(figs), 40):
                part = figs[start:start + 40]
                ok = self._compile(preamble, defs, part, env, cache, figdir)
                if not ok:
                    for f in part:
                        if not self._compile(preamble, defs, [f], env, cache, figdir):
                            print('  !! figure %s non compilable' % f[0])
                            (figdir / (f[0] + '.svg')).write_text(
                                '<svg xmlns="http://www.w3.org/2000/svg" width="200" height="30">'
                                '<text x="4" y="20" font-size="12">figure indisponible</text></svg>')

    def _compile(self, preamble, defs, figs, env, cache, figdir):
        with tempfile.TemporaryDirectory() as td:
            doc = preamble + '\\begin{document}\n\\makeatletter\n' + defs + '\n\\makeatother\n'
            for h, code in figs:
                doc += '\\begin{preview}\\color{black}%s\\end{preview}\n' % code
            doc += '\\end{document}\n'
            (Path(td) / 'f.tex').write_text(doc, encoding='utf-8')
            subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'f.tex'],
                           cwd=td, env=env, capture_output=True)
            pdf = Path(td) / 'f.pdf'
            if not pdf.exists():
                return False
            info = subprocess.run(['pdfinfo', str(pdf)], capture_output=True, text=True).stdout
            pages = int(re.search(r'Pages:\s+(\d+)', info).group(1))
            if pages != len(figs):
                return False
            for k, (h, code) in enumerate(figs, 1):
                out = cache / (h + '.svg')
                subprocess.run(['pdftocairo', '-svg', '-f', str(k), '-l', str(k), str(pdf), str(out)],
                               capture_output=True)
                shutil.copy(out, figdir / (h + '.svg'))
        return True

    def copy_images(self):
        imgdir = self.out / 'img'
        imgdir.mkdir(parents=True, exist_ok=True)
        for src, name in self.conv.images.items():
            if not name:
                continue
            dst = imgdir / name
            if dst.exists() and dst.stat().st_mtime >= os.stat(src).st_mtime:
                continue
            if src.lower().endswith('.pdf'):
                subprocess.run(['pdftocairo', '-svg', '-f', '1', '-l', '1', src, str(dst)])
            else:
                shutil.copy(src, dst)
                if os.path.getsize(dst) > 350_000:
                    subprocess.run(['sips', '-Z', '1600', str(dst)], capture_output=True)
                    if dst.suffix == '.jpg':
                        subprocess.run(['sips', '-s', 'formatOptions', '75', str(dst)],
                                       capture_output=True)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    levels = args or list(LEVELS)
    navs = {}
    for L in levels:
        site = Site(L)
        site.build()
        site.resolve_links()
        site.write()
        if '--no-figures' not in sys.argv:
            site.compile_figures()
        site.copy_images()
        unk = sorted(site.conv.unknown.items(), key=lambda x: -x[1])
        print('  inconnus :', unk[:60])
        navs[L] = dict(front=site.front_nav, annexes=site.annex_nav, chapters=site.chap_nav, pratique=site.prat_nav,
                       credits=bool(site.book['credits']),
                       synthese='synthese' in site.book)
    nf = ROOT / 'build' / 'nav.json'
    old = json.loads(nf.read_text()) if nf.exists() else {}
    old.update(navs)
    nf.write_text(json.dumps(old, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
