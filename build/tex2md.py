"""Conversion d'un corps de chapitre LaTeX (livre d'édition) en Markdown MkDocs Material.

Principe : le LaTeX est pré-traité en Python (macros maison -> jetons « QQ…QQ »),
pandoc convertit le reste, puis les jetons sont remplacés par du Markdown
(admonitions, blocs de code, figures SVG, liens, corrigés dépliables).
"""
import hashlib
import os
import re
import subprocess

import pypandoc

from texparse import (find_env, find_group, find_opt, read_arg, read_opt,
                      skip_ws, strip_comments, sub_macro)

PANDOC = pypandoc.get_pandoc_path()

MDFMT = ('markdown+raw_tex-fenced_divs-bracketed_spans-native_divs-native_spans'
         '-header_attributes-link_attributes-inline_code_attributes'
         '-fenced_code_attributes-smart-simple_tables-multiline_tables'
         '-grid_tables-subscript-superscript-strikeout-example_lists'
         '-fancy_lists-startnum-implicit_figures-escaped_line_breaks'
         '-raw_attribute-auto_identifiers-citations-yaml_metadata_block')

LANGS = {'spython': 'python', 'spythonnn': 'python', 'blacknn': 'text', 'black': 'text',
         'terminal': 'console', 'SQL': 'sql', 'shtml5': 'html', 'shtml5texte': 'html',
         'scss': 'css', 'sjs': 'javascript', 'http': 'http', 'lmc': 'text', 'tree': 'text',
         'socaml': 'ocaml', 'sprolog': 'prolog'}

# environnements encadrés : nom -> (type d'admonition, titre, numéroté)
BOXES = {
    'defi': ('definition', 'Définition', True),
    'regle': ('regle', 'Règle', True),
    'propr': ('propriete', 'Propriété', True),
    'prop': ('propriete', 'Propriété', True),
    'thm': ('theoreme', 'Théorème', True),
    'remarque': ('remarque', 'Remarque', False),
    'rem': ('remarque', 'Remarque', False),
    'exemple': ('exemple', 'Exemple', False),
    'ex': ('exemple', 'Exemple(s)', False),
    'demonstration': ('demonstration', 'Démonstration', False),
    'demo': ('demonstration', 'Démonstration', False),
    'consignes': ('consignes', 'Consignes', False),
    'modeemploi': ('consignes', "Mode d'emploi", False),
    'encadre': ('encadre', None, False),          # titre = argument
    'activite': ('activite', 'Activité', False),  # titre = argument
    'etudedoc': ('etudedoc', 'Étude de document', False),
    'passerelle': ('passerelle', 'Passerelle avec Scratch', False),
    'navigateur': ('navigateur', 'Rendu dans le navigateur', False),
    'projet': ('projet', 'Projet', False),
    'encadremonaco': ('monaco', 'Et à Monaco ?', False),
    'flash': ('flash', 'Questions flash', False),
    'testetoi': ('testetoi', 'Se tester', False),
    'autopositionnement': ('autopos', 'Savoir-faire : je me positionne', False),
    'tcolorbox': ('encadre', None, False),
}
BOX_ARGS = {'encadre': 'm', 'activite': 'm', 'etudedoc': 'm', 'projet': 'm', 'flash': 'm',
            'navigateur': 'o', 'tcolorbox': 'o'}
THEOREMS = {'defi', 'regle', 'propr', 'prop', 'thm', 'remarque', 'rem', 'exemple', 'ex',
            'demonstration', 'demo'}

GRAPHIC_RE = re.compile(r'\\begin\{tikzpicture\}|\\tikz(?![a-zA-Z])|\\draw\b|\\fill\b|\\node\b|'
                        r'\\path\b|\\pgf|\\foreach\b|\\filldraw\b|\\shade\b|\\matrix\b')
COMPLEX_RE = re.compile(r'\\if|\\csname|\\expandafter|\\edef|\\the\\|\\numexpr|\\@')

IA_TITRES = {'rouge': "Sans IA : le but est l'automatisme lui-même",
             'orange': "IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre",
             'vert': "IA intégrée : l'exercice s'appuie sur une réponse d'IA"}

SIMPLE_DROP0 = ['medskip', 'smallskip', 'bigskip', 'noindent', 'centering', 'raggedright',
                'raggedleft', 'sloppy', 'fussy', 'clearpage', 'newpage', 'cleardoublepage',
                'cleartorecto', 'cleartoverso', 'pagebreak', 'nopagebreak', 'phantomsection', 'hfill', 'vfill',
                'strut', 'leavevmode', 'nobreak', 'allowbreak', 'footnotesize', 'scriptsize',
                'tiny', 'small', 'normalsize', 'large', 'Large', 'LARGE', 'huge', 'Huge',
                'normalfont', 'selectfont', 'finrubrique', 'separationactivites',
                'afficherCoupsDePouce', 'makeatletter', 'makeatother', 'enoncref_', 'hrule',
                'bandeaupagetitre', 'frenchspacing', 'unskip', 'break', 'protect', 'relax',
                'mainmatter', 'frontmatter', 'backmatter', 'tableofcontents', 'linebreak',
                'arraybackslash', 'displaystyle_', 'ttfamily', 'sffamily', 'rmfamily',
                'bfseries', 'itshape', 'mdseries', 'upshape', 'em_']
SIMPLE_DROP1 = ['vspace', 'hspace', 'needspace', 'setcounter_', 'addtocounter_', 'stepcounter',
                'refstepcounter', 'hypersetup', 'color', 'thispagestyle', 'pagestyle',
                'markright', 'enlargethispage', 'iadefaut_', 'pagecolor', 'label_', 'pageref',
                'qrcode', 'enoncref_', 'coursretour', 'rowcolor', 'cellcolor', 'columncolor',
                'arrayrulecolor', 'usetikzlibrary', 'newcounter', 'fontsize_', 'cline',
                'cmidrule', 'addvspace']
UNWRAP1 = ['mbox', 'fbox', 'textnormal', 'textrm', 'textsf', 'textup', 'textmd', 'underline',
           'uline', 'hbox', 'emph_', 'MakeUppercase', 'text_']


class Store:
    """Jetons partagés : valeurs Markdown associées à des marqueurs alphanumériques."""

    def __init__(self):
        self.n = 0
        self.vals = {}

    def put(self, val):
        self.n += 1
        self.vals[self.n] = val
        return self.n


MATH_RE = re.compile(r'(\$\$.*?\$\$|(?<!\\)\$.*?(?<!\\)\$|\\\[.*?\\\]|\\\(.*?\\\)|'
                     r'\\begin\{(equation|align|displaymath|gather|multline)\*?\}.*?\\end\{\2\*?\})', re.S)


def outside_math(s, fn):
    """Applique fn au texte en masquant les formules (remises en place ensuite)."""
    maths = []

    def keep(m):
        maths.append(m.group(0))
        return '{}QQMATH%dQQ' % (len(maths) - 1)
    s = fn(MATH_RE.sub(keep, s))
    return re.sub(r'(?:\{\})?QQMATH(\d+)QQ', lambda m: maths[int(m.group(1))], s)


def keyval(opts, key):
    """Valeur d'une clé dans une liste d'options « a=b, title={...} » (accolades gérées)."""
    m = re.search(r'(?:^|,)\s*' + key + r'\s*=\s*', opts)
    if not m:
        return None
    i = m.end()
    depth = 0
    j = i
    while j < len(opts):
        c = opts[j]
        if c == '\\':
            j += 2
            continue
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
        elif c == ',' and depth == 0:
            break
        j += 1
    v = opts[i:j].strip()
    if v.startswith('{') and v.endswith('}'):
        v = v[1:-1]
    return v


def sha(*parts):
    h = hashlib.sha1()
    for p in parts:
        h.update(p.encode('utf-8'))
        h.update(b'\0')
    return h.hexdigest()[:16]


class Converter:
    """Convertit les fichiers d'UN niveau ; garde les figures à compiler et les ancres."""

    def __init__(self, level, srcdir, outdir):
        self.level = level              # 'terminale'...
        self.srcdir = srcdir            # .../livre_autonome
        self.outdir = outdir            # docs/<level>
        self.st = Store()
        self.figures = {}               # hash -> (localdefs, code)
        self.images = {}                # source -> nom publié
        self.anchors = {}               # ancre -> page (chemin relatif à docs/)
        self.unknown = {}               # macro inconnue -> nombre
        self.counters = {}
        self.page = None                # chemin de la page en cours (relatif à docs/)
        self.links = []

    # ------------------------------------------------------------------ jetons
    def inline(self, md):
        return '{}QQI%dQQ' % self.st.put(md)

    def block(self, md):
        return '\n\nQQB%dQQ\n\n' % self.st.put(md)

    def wrap(self, fn, inner):
        n = self.st.put(fn)
        return '{}QQW%daQQ%sQQW%dzQQ' % (n, inner, n)

    def adm_begin(self, kind, title, collapsible=False, opened=False):
        n = self.st.put((kind, collapsible, opened))
        return '\n\nQQAB%dQQ %s QQABEQQ\n\n' % (n, title if title else 'QQNOTITLEQQ')

    def adm_end(self):
        return '\n\nQQAEQQ\n\n'

    def link(self, anchor, text_latex):
        def fn(inner, anchor=anchor):
            return '[%s](QQLK%sQQ)' % (inner.strip() or '→', anchor)
        return self.wrap(fn, text_latex)

    def anchor(self, a):
        self.anchors.setdefault(a, self.page)
        return self.inline('<span id="%s" class="ancre"></span>' % a)

    # --------------------------------------------------------- pré-traitement
    def protect_verbatim(self, s, store):
        """lstlisting / verb / lstinline -> jetons (avant retrait des commentaires)."""
        s = re.sub(r'\\(url|href)\{([^{}]*)\}',
                   lambda m: '\\%s{%s}' % (m.group(1), m.group(2).replace('%', 'QQPCTQQ')), s)
        def lst(m):
            opts = m.group(1) or ''
            code = m.group(2)
            if code.startswith('\n'):
                code = code[1:]
            code = code.rstrip(' \t')
            if code.endswith('\n'):
                code = code[:-1]
            style = re.search(r'style=([A-Za-z0-9]+)', opts)
            lang = LANGS.get(style.group(1), 'text') if style else 'text'
            if re.search(r'language=\{?\[?[^,\]]*\]?Python', opts):
                lang = 'python'
            k = len(store)
            store.append(('lst', lang, code, m.group(0)))
            return '\n\nQQLST%dQQ\n\n' % k
        s = re.sub(r'\\begin\{lstlisting\}(\[[^\]]*\])?(.*?)\\end\{lstlisting\}', lst, s,
                   flags=re.S)

        def verb(m):
            k = len(store)
            store.append(('verb', None, m.group(2), m.group(0)))
            return 'QQLST%dQQ' % k
        s = re.sub(r'\\(?:verb|lstinline)\*?(?:\[[^\]]*\])?([^a-zA-Z\s{])(.*?)\1', verb, s)

        def lstin(m):
            k = len(store)
            store.append(('verb', None, m.group(1), m.group(0)))
            return 'QQLST%dQQ' % k
        s = re.sub(r'\\lstinline(?:\[[^\]]*\])?\{([^}]*)\}', lstin, s)
        return s

    def restore_raw(self, s, store):
        return re.sub(r'QQLST(\d+)QQ', lambda m: store[int(m.group(1))][3], s)

    DEF_CMDS = ('newcommand', 'renewcommand', 'providecommand', 'ProvideDocumentCommand',
                'NewDocumentCommand', 'RenewDocumentCommand', 'DeclareDocumentCommand',
                'newenvironment', 'renewenvironment', 'newtcolorbox', 'tikzset', 'pgfkeys',
                'pgfdeclarelindenmayersystem', 'definecolor', 'colorlet', 'lstdefinestyle',
                'usetikzlibrary', 'newcounter', 'tikzstyle', 'pgfdeclarelayer', 'pgfsetlayers',
                'newsavebox', 'newlength', 'newif', 'def', 'gdef', 'let', 'pgfmathsetmacro',
                'tcbset', 'newtheorem', 'pgfplotsset', 'DeclareMathOperator',
                'newcolumntype', 'pgfdeclarepatternformonly', 'pgfdeclareshape', 'setlength',
                'renewcommand*', 'newcommand*')

    def extract_defs(self, s):
        """Retire les définitions locales ; renvoie (texte, defs_brutes, macros)."""
        defs = []
        macros = {}   # nom -> (nargs, default_opt, body, raw)
        envs = {}
        out = []
        pos = 0
        pat = re.compile(r'\\(newcommand|renewcommand|providecommand|ProvideDocumentCommand|'
                         r'NewDocumentCommand|RenewDocumentCommand|DeclareDocumentCommand|'
                         r'newenvironment|renewenvironment|newtcolorbox|tikzset|pgfkeys|'
                         r'pgfdeclarelindenmayersystem|definecolor|colorlet|lstdefinestyle|'
                         r'usetikzlibrary|newcounter|tikzstyle|pgfdeclarelayer|pgfsetlayers|'
                         r'newsavebox|newlength|newif|def|gdef|let|tcbset|newtheorem|pgfplotsset|'
                         r'DeclareMathOperator|newcolumntype|setlength|pgfmathsetmacro|'
                         r'pgfmathtruncatemacro|settowidth)(?![a-zA-Z@])(\*?)')
        while True:
            m = pat.search(s, pos)
            if not m:
                break
            cmd = m.group(1)
            i = m.end()
            try:
                if cmd in ('newcommand', 'renewcommand', 'providecommand'):
                    name, i = read_arg(s, i)
                    n, i = read_opt(s, i)
                    dflt, i = read_opt(s, i)
                    body, i = read_arg(s, i)
                    name = name.strip().lstrip('\\')
                    macros[name] = (int(n) if n else 0, dflt, body)
                elif cmd in ('ProvideDocumentCommand', 'NewDocumentCommand',
                             'RenewDocumentCommand', 'DeclareDocumentCommand'):
                    name, i = read_arg(s, i)
                    spec, i = read_arg(s, i)
                    body, i = read_arg(s, i)
                    name = name.strip().lstrip('\\')
                    nm = spec.count('m') + spec.count('o') + spec.count('O')
                    dflt = None
                    if spec.strip().startswith(('o', 'O')):
                        dflt = re.search(r'O\{([^}]*)\}', spec)
                        dflt = dflt.group(1) if dflt else ''
                    macros[name] = (nm, dflt, body)
                elif cmd in ('newenvironment', 'renewenvironment'):
                    name, i = read_arg(s, i)
                    n, i = read_opt(s, i)
                    dflt, i = read_opt(s, i)
                    b, i = read_arg(s, i)
                    e, i = read_arg(s, i)
                    envs[name.strip()] = (int(n) if n else 0, dflt, b, e)
                elif cmd == 'newtcolorbox':
                    name, i = read_arg(s, i)
                    n, i = read_opt(s, i)
                    dflt, i = read_opt(s, i)
                    b, i = read_arg(s, i)
                elif cmd in ('def', 'gdef'):
                    mm = re.match(r'\s*\\([a-zA-Z@]+)((?:#\d)*)', s[i:])
                    i += mm.end()
                    body, i = read_arg(s, i)
                    if not mm.group(2):
                        macros[mm.group(1)] = (0, None, body)
                    else:
                        macros[mm.group(1)] = (mm.group(2).count('#'), None, body)
                elif cmd == 'let':
                    mm = re.match(r'\s*\\[a-zA-Z@]+\s*=?\s*\\[a-zA-Z@]+', s[i:])
                    i += mm.end() if mm else 0
                elif cmd in ('definecolor',):
                    for _ in range(3):
                        _, i = read_arg(s, i)
                elif cmd in ('colorlet', 'lstdefinestyle', 'newtheorem', 'setlength',
                             'DeclareMathOperator', 'pgfmathsetmacro', 'pgfmathtruncatemacro',
                             'settowidth'):
                    _, i = read_arg(s, i)
                    _, i = read_opt(s, i)
                    _, i = read_arg(s, i)
                    if cmd == 'newtheorem':
                        _, i = read_opt(s, i)
                elif cmd == 'newcolumntype':
                    _, i = read_arg(s, i)
                    _, i = read_opt(s, i)
                    _, i = read_arg(s, i)
                elif cmd == 'pgfdeclarelindenmayersystem':
                    _, i = read_arg(s, i)
                    _, i = read_arg(s, i)
                else:
                    _, i = read_arg(s, i)
            except Exception:
                pos = m.end()
                continue
            raw = s[m.start():i]
            # \setlength et \pgfmathsetmacro dans le texte : utiles aux figures seulement
            defs.append(raw)
            out.append(s[pos:m.start()])
            pos = i
        out.append(s[pos:])
        return ''.join(out), '\n'.join(defs), macros, envs

    def classify(self, macros, envs):
        graphic = set()
        for name, (n, d, body) in macros.items():
            if GRAPHIC_RE.search(body) or COMPLEX_RE.search(body):
                graphic.add(name)
        changed = True
        while changed:
            changed = False
            for name, (n, d, body) in macros.items():
                if name in graphic:
                    continue
                for g in graphic:
                    if re.search(r'\\' + re.escape(g) + r'(?![a-zA-Z@])', body):
                        graphic.add(name)
                        changed = True
                        break
        return graphic

    # ----------------------------------------------------------------- figures
    def fig(self, code, localdefs, inline=False):
        h = sha(self.level, localdefs, code)
        self.figures[h] = (localdefs, code)
        return self.inline('QQFIG:%s:%s' % (h, 'i' if inline else 'b'))

    def extract_figures(self, s, localdefs, graphic, store):
        # 1. environnements tikzpicture (mis de côté dans convert)
        s = re.sub(r'QQTIKZ(\d+)QQ', lambda m: self.fig(self.restore_raw(self._tikz[int(m.group(1))], store),
                                                         localdefs), s)
        # 2. \tikz en ligne
        out = []
        pos = 0
        for m in re.finditer(r'\\tikz(?![a-zA-Z])', s):
            if m.start() < pos:
                continue
            i = m.end()
            o, i = read_opt(s, i)
            j = skip_ws(s, i)
            if j < len(s) and s[j] == '{':
                _, i = find_group(s, j)
            else:
                depth = 0
                k = j
                while k < len(s):
                    if s[k] == '{':
                        depth += 1
                    elif s[k] == '}':
                        depth -= 1
                    elif s[k] == ';' and depth == 0:
                        break
                    k += 1
                i = k + 1
            out.append(s[pos:m.start()])
            out.append(self.fig(self.restore_raw(s[m.start():i], store), localdefs, inline=True))
            pos = i
        out.append(s[pos:])
        s = ''.join(out)
        # 3. macros locales graphiques ou trop complexes
        for name in sorted(graphic, key=len, reverse=True):
            n, d, body = self.local_macros[name]
            nopt = 1 if d is not None else 0
            nargs = n - nopt

            def fn(opts, args, star, name=name):
                raw = '\\' + name + ''.join('[%s]' % o for o in opts if o is not None) + \
                      ''.join('{%s}' % a for a in args)
                return self.fig(self.restore_raw(raw, store), localdefs, inline=True)
            s = sub_macro(s, name, nargs, nopt, fn)
        return s

    def image(self, opts, path):
        path = path.strip()
        src = None
        for ext in ('', '.pdf', '.png', '.jpg', '.jpeg', '.svg', '.PNG', '.JPG'):
            p = os.path.join(self.srcdir, path + ext)
            if os.path.isfile(p):
                src = p
                break
        if not src:
            return '*(image manquante : %s)*' % path
        self.images[src] = None
        style = ''
        o = opts or ''
        m = re.search(r'width\s*=\s*([\d.]*)\s*\\(?:linewidth|textwidth|columnwidth)', o)
        if m:
            style = 'width:%d%%' % round(float(m.group(1) or 1) * 100)
        else:
            m = re.search(r'(width|height)\s*=\s*([\d.]+)\s*(cm|mm|pt)', o)
            if m:
                v = float(m.group(2)) * {'cm': 38, 'mm': 3.8, 'pt': 1.33}[m.group(3)]
                style = '%s:%dpx' % ('width' if m.group(1) == 'width' else 'height', round(v * 1.15))
        return self.inline('QQIMG:%s:%s' % (src, style))

    # ------------------------------------------------------------- conversion
    def convert(self, tex, page, ctx):
        """tex : corps LaTeX ; page : chemin docs/ ; ctx : dict d'état de page.
        Renvoie le Markdown (avec jetons de liens QQLK…QQ non résolus)."""
        self.page = page
        store = []
        s = tex
        s = self.protect_verbatim(s, store)
        s = strip_comments(s)
        s = s.strip()
        # groupe englobant {% ... }
        if s.startswith('{') and s.endswith('}'):
            try:
                inner, end = find_group(s, 0)
                if end == len(s):
                    s = inner
            except ValueError:
                pass
        # tikzpicture mis de côté AVANT l'extraction des définitions (\pgfmath… internes)
        tikz = []
        out = []
        pos = 0
        while True:
            r = find_env(s, 'tikzpicture', pos)
            if not r:
                break
            a, _, _, b = r
            out.append(s[pos:a])
            out.append('QQTIKZ%dQQ' % len(tikz))
            tikz.append(s[a:b])
            pos = b
        out.append(s[pos:])
        s = ''.join(out)

        def untikz(t):
            return re.sub(r'QQTIKZ(\d+)QQ', lambda m: tikz[int(m.group(1))], t)
        s, localdefs, macros, envs = self.extract_defs(s)
        localdefs = self.restore_raw(untikz(localdefs), store)
        macros = {k: (n, d, untikz(b)) for k, (n, d, b) in macros.items()}
        envs = {k: (n, d, untikz(b), untikz(e)) for k, (n, d, b, e) in envs.items()}
        self._tikz = tikz
        # les macros du style traitées ici ne doivent pas être redéfinies localement
        for k in list(macros):
            if k in HANDLED:
                del macros[k]
        self.local_macros = macros
        graphic = self.classify(macros, envs)
        s = self.extract_figures(s, localdefs, graphic, store)
        # environnements locaux (newenvironment) simples : remplacés par leur définition
        for name, (n, d, b, e) in envs.items():
            if name in BOXES or name in ('flash', 'testetoi', 'autopositionnement', 'resultat'):
                continue
            s = re.sub(r'\\begin\{%s\}' % re.escape(name), lambda m, b=b: b, s)
            s = re.sub(r'\\end\{%s\}' % re.escape(name), lambda m, e=e: e, s)
        # macros locales textuelles : expansion
        for _ in range(4):
            before = s
            for name, (n, d, body) in macros.items():
                if name in graphic:
                    continue
                nopt = 1 if d is not None else 0

                def fn(opts, args, star, body=body, d=d, name=name):
                    vals = []
                    if d is not None:
                        vals.append(opts[0] if opts and opts[0] is not None else d)
                    vals += args
                    r = body
                    for k, v in enumerate(vals, 1):
                        r = r.replace('#%d' % k, v)
                    return r + (' ' if not vals and name.isalpha() else '')
                s = sub_macro(s, name, n - nopt, nopt, fn)
            if s == before:
                break
        s = self.preprocess(s, ctx, store)
        md = self.pandoc(s)
        md = self.postprocess(md, store, ctx)
        return md

    def preprocess(self, s, ctx, store):
        I = self.inline
        s = re.sub(r'\$\s*((?:\\bigstar\s*)+)\$', lambda m: '★' * m.group(1).count('bigstar'), s)
        # --- textes du style maison
        s = sub_macro(s, 'ialegendecourte', 0, 0, lambda o, a, st:
                      "Usage de l'IA, indiqué sur chaque exercice : \\iabadge{rouge} aucune ; "
                      "\\iabadge{orange} en appui (déboguer, reformuler, vérifier ; la réponse "
                      "finale est écrite et comprise par vous) ; \\iabadge{vert} l'exercice "
                      "s'appuie sur une réponse d'IA. Voir la \\renvoicharte.")
        s = sub_macro(s, 'ialegende', 0, 0, lambda o, a, st:
                      "\\ialegendecourte")
        s = sub_macro(s, 'ialegendecourte', 0, 0, lambda o, a, st:
                      "Usage de l'IA : \\iabadge{rouge} aucune ; \\iabadge{orange} en appui ; "
                      "\\iabadge{vert} intégrée. Voir la \\renvoicharte.")
        s = sub_macro(s, 'iaconsigne', 0, 0, lambda o, a, st:
                      "\\iabadge{rouge} Travail \\textbf{sans IA} : ni assistant, ni complétion de "
                      "code ; vous devez pouvoir expliquer chaque réponse.")
        s = sub_macro(s, 'renvoicharte', 0, 0, lambda o, a, st:
                      self.link('charte', "charte d'usage de l'IA"))
        s = sub_macro(s, 'legendeniveaux', 0, 0, lambda o, a, st:
                      "Niveau : ★ échauffement, ★★ classique (niveau "
                      "bac), ★★★ défi ; les \\emph{coups de pouce} et "
                      "les \\emph{corrigés} se déplient sous chaque exercice.")
        s = sub_macro(s, 'iabadge', 1, 0, lambda o, a, st: I(self.badge(a[0].strip())))
        s = sub_macro(s, 'horsprog', 0, 0, lambda o, a, st:
                      I('<span class="horsprog">au-delà du programme</span>'))
        s = sub_macro(s, 'papier', 0, 0, lambda o, a, st:
                      I('<span class="tag">sur papier</span> '))
        s = sub_macro(s, 'machine', 0, 0, lambda o, a, st:
                      I('<span class="tag">sur machine</span> '))
        s = sub_macro(s, 'run', 0, 0, lambda o, a, st:
                      I('<span class="run" title="À programmer et tester sur machine">▶</span> '))
        s = sub_macro(s, 'sol', 0, 0, lambda o, a, st: '')
        s = sub_macro(s, 'pts', 1, 0, lambda o, a, st: ' (%s)' % a[0])
        s = sub_macro(s, 'labelP', 1, 0, lambda o, a, st: '\\textbf{%s}' % a[0])
        s = sub_macro(s, 'bloc', 1, 0, lambda o, a, st: '\n\n\\paragraph{%s}\n\n' % a[0]) \
            if 'bloc' not in self.local_macros else s
        s = sub_macro(s, 'afaire', 1, 0, lambda o, a, st:
                      '\n\n' + I('<span class="afaire">▶ Exercices d\'application :</span>') +
                      ' ' + a[0] + '\n\n')
        s = sub_macro(s, 'qrcode', 1, 1, lambda o, a, st: '')
        s = sub_macro(s, 'fichierseleves', 2, 0, lambda o, a, st: self.fichiers(a[0], a[1]))
        s = sub_macro(s, 'autoposcases', 0, 0, lambda o, a, st: '')
        s = sub_macro(s, 'checkmark', 0, 0, lambda o, a, st: '✓')
        s = sub_macro(s, 'euro', 0, 0, lambda o, a, st: '€')
        s = sub_macro(s, 'guillemotleft', 0, 0, lambda o, a, st: '«')
        s = sub_macro(s, 'guillemotright', 0, 0, lambda o, a, st: '»')
        s = sub_macro(s, 'og', 0, 0, lambda o, a, st: '« ')
        s = sub_macro(s, 'fg', 0, 0, lambda o, a, st: ' »')
        s = sub_macro(s, 'textvisiblespace', 0, 0, lambda o, a, st: '␣')
        s = sub_macro(s, 'textperiodcentered', 0, 0, lambda o, a, st: '·')
        s = sub_macro(s, 'textdegree', 0, 0, lambda o, a, st: '°')
        s = sub_macro(s, 'enspace', 0, 0, lambda o, a, st: ' ')
        s = sub_macro(s, 'textcircled', 1, 0, lambda o, a, st: '(%s)' % a[0])
        # babel-french
        s = sub_macro(s, 'degres', 0, 0, lambda o, a, st: '°')
        for nm, sup in (('ieme', 'e'), ('iemes', 'es'), ('ier', 'er'), ('iere', 're'), ('ieres', 'res'),
                        ('eme', 'e'), ('er', 'er'), ('re', 're')):
            s = sub_macro(s, nm, 0, 0, lambda o, a, st, sup=sup: I('<sup>%s</sup>' % sup))
        s = sub_macro(s, 'no', 0, 0, lambda o, a, st: 'n°')
        # formules en ligne écrites sur plusieurs lignes : une seule ligne
        s = re.sub(r'(?<![\\$])\$(?!\$)((?:[^$\\]|\\.)+?)\$', lambda m: '$' + re.sub(r'\s*\n\s*', ' ', m.group(1)) + '$', s)
        # --- lexique (SNT)
        s = sub_macro(s, 'lexmarque', 1, 0, lambda o, a, st: self.anchor('lex-' + a[0].strip()))
        s = re.sub(r'p\.\\,\s*(?=\\lexref)', '', s)
        s = sub_macro(s, 'lexref', 1, 0, lambda o, a, st: self.link('lex-' + a[0].strip(), 'voir le cours'))
        s = sub_macro(s, 'lexlettre', 1, 0, lambda o, a, st: '\n\n\\subsection*{%s}\n\n' % a[0])
        s = sub_macro(s, 'lexentree', 3, 0, lambda o, a, st:
                      '\n\n\\textbf{%s} --- %s \\emph{(%s)}\n\n' % (a[0], a[1], a[2]))
        # --- liens et ancres
        s = sub_macro(s, 'exref', 2, 0, lambda o, a, st:
                      self.link('ex-%s-%s' % (a[0].strip(), a[1].strip()), a[1]))
        s = sub_macro(s, 'hyperlink', 2, 0, lambda o, a, st: self.link(a[0].strip(), a[1]))
        s = sub_macro(s, 'hyperref', 1, 1, lambda o, a, st:
                      self.link(o[0].strip(), a[0]) if o[0] else a[0])
        s = sub_macro(s, 'titrecours', 2, 0, lambda o, a, st: a[1])
        s = sub_macro(s, 'corrref', 2, 0, lambda o, a, st: '')
        s = sub_macro(s, 'enoncref', 2, 0, lambda o, a, st: '')
        s = sub_macro(s, 'hypertarget', 2, 0, lambda o, a, st: self.anchor(a[0].strip()) + a[1])
        s = sub_macro(s, 'label', 1, 0, lambda o, a, st: self.anchor(a[0].strip()))
        s = sub_macro(s, 'ref', 1, 0, lambda o, a, st: '')
        s = sub_macro(s, 'includegraphics', 1, 1, lambda o, a, st: self.image(o[0], a[0]))
        s = sub_macro(s, 'creditimage', 5, 0, lambda o, a, st:
                      '\n\n' + I('<span class="credit">') + '\\emph{%s} --- %s, %s, \\url{%s}' %
                      (a[1], a[2], a[3], a[4]) + I('</span>') + '\n\n')
        # --- coups de pouce (dépliables)
        s = sub_macro(s, 'coupdepouce', 1, 1, lambda o, a, st:
                      self.adm_begin('pouce', 'Coup de pouce' if (o[0] or '1').strip() == '1'
                                     else 'Coup de pouce 2 (début de solution)', True) +
                      a[0] + self.adm_end())
        s = sub_macro(s, 'testq', 2, 0, lambda o, a, st:
                      '\\item ' + a[0] + self.adm_begin('reponse', 'Réponse', True) + a[1] +
                      self.adm_end())
        # --- \correction dans un exemple : dépliable jusqu'à la fin de l'encadré
        s = self.corrections(s)
        # --- encadrés
        s = self.boxes(s, ctx)
        out = []
        pos = 0
        for m in re.finditer(r'\\begin\{resultat\}', s):
            spec, i = read_arg(s, m.end())
            out.append(s[pos:m.start()] + '\\begin{center}\\begin{tabular}{%s}\\hline' % spec)
            pos = i
        out.append(s[pos:])
        s = ''.join(out)
        s = s.replace('\\end{resultat}', '\\hline\\end{tabular}\\end{center}')
        s = re.sub(r'\\(begin|end)\{(minipage|multicols|adjustwidth|samepage|figure|wrapfigure)\}'
                   r'(\[[^\]]*\])*(\{[^}]*\})*(\{[^}]*\})?', '\n', s)
        s = re.sub(r'\\begin\{(center|flushleft|flushright)\}', '\n\n', s)
        s = re.sub(r'\\end\{(center|flushleft|flushright)\}', '\n\n', s)
        # --- tableaux
        s = self.tables(s)
        # --- listes : options enumitem, étiquettes personnalisées
        s = self.lists(s)
        # --- exercices, activités, titres (balayage séquentiel avec état)
        s = self.sequential(s, ctx)
        # --- divers
        s = sub_macro(s, 'renewcommand', 2, 0, lambda o, a, st: '')
        s = sub_macro(s, 'scalebox', 2, 0, lambda o, a, st: a[1])
        s = sub_macro(s, 'resizebox', 3, 0, lambda o, a, st: a[2])
        s = sub_macro(s, 'up', 1, 0, lambda o, a, st: self.wrap(lambda x: '<sup>%s</sup>' % x, a[0]))
        s = re.sub(r'\\\\\s*\[[^\]]*\]', r'\\\\ ', s)
        s = outside_math(s, self.text_only)
        return s

    def text_only(self, s):
        """Nettoyages réservés au texte (jamais dans les formules)."""
        s = re.sub(r'\\q?quad(?![a-zA-Z@])', ' ', s)
        s = re.sub(r'\\string(?![a-zA-Z@])', '', s)
        for name in SIMPLE_DROP0:
            if name.endswith('_'):
                continue
            s = sub_macro(s, name, 0, 0, lambda o, a, st: '')
        for name in SIMPLE_DROP1:
            if name.endswith('_'):
                name = name[:-1]
            s = sub_macro(s, name, 1, 1, lambda o, a, st: '')
        s = sub_macro(s, 'setcounter', 2, 0, lambda o, a, st: '')
        s = sub_macro(s, 'addtocounter', 2, 0, lambda o, a, st: '')
        s = sub_macro(s, 'setlength', 2, 0, lambda o, a, st: '')
        s = sub_macro(s, 'addcontentsline', 3, 0, lambda o, a, st: '')
        s = sub_macro(s, 'markboth', 2, 0, lambda o, a, st: '')
        s = sub_macro(s, 'fontsize', 2, 0, lambda o, a, st: '')
        s = sub_macro(s, 'rule', 2, 1, lambda o, a, st: '')
        s = sub_macro(s, 'penalty', 0, 0, lambda o, a, st: '')
        s = re.sub(r'(?<=\d)\s*\\relax', '', s)
        s = sub_macro(s, 'textcolor', 2, 0, lambda o, a, st: a[1])
        s = sub_macro(s, 'colorbox', 2, 0, lambda o, a, st: a[1])
        s = sub_macro(s, 'fcolorbox', 3, 0, lambda o, a, st: a[2])
        s = sub_macro(s, 'makebox', 1, 2, lambda o, a, st: a[0])
        s = sub_macro(s, 'raisebox', 2, 2, lambda o, a, st: a[1])
        s = sub_macro(s, 'parbox', 2, 3, lambda o, a, st: a[1])
        s = sub_macro(s, 'multirow', 3, 0, lambda o, a, st: a[2])
        s = sub_macro(s, 'phantom', 1, 0, lambda o, a, st: '')
        s = sub_macro(s, 'hphantom', 1, 0, lambda o, a, st: '')
        s = sub_macro(s, 'vphantom', 1, 0, lambda o, a, st: '')
        s = sub_macro(s, 'url', 1, 0, lambda o, a, st:
                      '\\href{%s}{%s}' % (a[0], a[0].replace('_', '\\_').replace('#', '\\#').replace('%', '\\%')))
        for name in UNWRAP1:
            if name.endswith('_'):
                continue
            s = sub_macro(s, name, 1, 0, lambda o, a, st: '{%s}' % a[0])
        s = re.sub(r'\\\\\[[^\]]*\]', r'\\\\', s)
        s = re.sub(r'\\hangindent\s*=?\s*[\d.]+\w+', '', s)
        s = re.sub(r'\\(parskip|parindent|baselineskip|tabcolsep|arraystretch|fboxsep|fboxrule)'
                   r'\s*=?\s*[\d.]*\s*(\w+)?', '', s)
        return s

    def badge(self, c):
        if c not in IA_TITRES:
            return ''
        return '<span class="ia ia-%s" title="%s"></span>' % (c, IA_TITRES[c])

    def fichiers(self, dossier, zipurl):
        return (self.adm_begin('fichiers', 'Fichiers à télécharger') +
                self.inline('[:material-folder-open: dossier en ligne](%s){ .md-button } '
                            '[:material-zip-box: archive .zip](%s){ .md-button }' % (dossier, zipurl)) +
                self.adm_end())

    def corrections(self, s):
        pos = 0
        while True:
            m = re.compile(r'\\correction(?![a-zA-Z])').search(s, pos)
            if not m:
                return s
            # environnement englobant
            stack = []
            for mm in re.finditer(r'\\(begin|end)\{([a-zA-Z*]+)\}', s[:m.start()]):
                if mm.group(1) == 'begin':
                    stack.append((mm.group(2), mm.start()))
                elif stack and stack[-1][0] == mm.group(2):
                    stack.pop()
            boxes = [e for e in stack if e[0] in BOXES]
            begin_tok = self.adm_begin('corrige', 'Correction', True)
            end_tok = self.adm_end()
            if boxes:
                name, start = boxes[-1]
                r = find_env(s, name, start)
                endpos = r[2]
            else:
                nxt = re.compile(r'\\(section|subsection|subsubsection|exercice|exo|edsection|'
                                 r'enteteactivite|begin\{(?:' + '|'.join(BOXES) + r')\})').search(s, m.end())
                endpos = nxt.start() if nxt else len(s)
            s = s[:m.start()] + begin_tok + s[m.end():endpos] + end_tok + s[endpos:]
            pos = m.start() + len(begin_tok)

    def boxes(self, s, ctx):
        counters = ctx.setdefault('counters', {})

        def begin(name):
            def fn(m):
                kind, label, numbered = BOXES[name]
                i = m.end()
                title_arg = None
                spec = BOX_ARGS.get(name, 'o' if name in THEOREMS else '')
                if spec == 'm':
                    title_arg, i = read_arg(s_[0], i)
                elif spec == 'o':
                    title_arg, i = read_opt(s_[0], i)
                if name == 'tcolorbox':
                    title_arg = keyval(title_arg or '', 'title')
                    label = None
                if name in ('defi', 'regle', 'propr', 'prop', 'thm'):
                    key = 'propr' if name == 'prop' else name
                    counters[key] = counters.get(key, 0) + 1
                    title = '%s %d' % (label, counters[key])
                    if title_arg:
                        title += ' — ' + title_arg
                elif name == 'projet':
                    title = 'Projet — ' + (title_arg or '')
                elif name == 'flash':
                    title = 'Questions flash — rappel : ' + (title_arg or '')
                elif title_arg:
                    title = title_arg if label is None or name in ('encadre', 'activite', 'etudedoc') \
                        else '%s — %s' % (label, title_arg)
                    if name == 'activite':
                        title = 'Activité — ' + title_arg
                else:
                    title = label or ''
                extra = ''
                if name == 'testetoi':
                    extra = '\\begin{enumerate}'
                if name == 'autopositionnement':
                    extra = '\\begin{itemize}'
                return ('QQBOXSTART', i, self.adm_begin(kind, title) + extra)
            return fn
        s_ = [s]
        for name in BOXES:
            pat = re.compile(r'\\begin\{%s\}' % re.escape(name))
            out = []
            pos = 0
            cur = s_[0]
            while True:
                m = pat.search(cur, pos)
                if not m:
                    break
                s_[0] = cur
                _, i, rep = begin(name)(m)
                out.append(cur[pos:m.start()])
                out.append(rep)
                pos = i
            out.append(cur[pos:])
            cur = ''.join(out)
            extra = ''
            if name == 'testetoi':
                extra = '\\end{enumerate}'
            if name == 'autopositionnement':
                extra = '\\end{itemize}'
            cur = cur.replace('\\end{%s}' % name, extra + self.adm_end())
            s_[0] = cur
        return s_[0]

    def tables(self, s):
        def clean_spec(spec):
            spec = re.sub(r'[@!<>]\{(?:[^{}]|\{[^{}]*\})*\}', '', spec)
            spec = re.sub(r'\*\{(\d+)\}\{([^{}]*)\}', lambda m: m.group(2) * int(m.group(1)), spec)
            spec = re.sub(r'[pmb]\{[^{}]*\}', 'l', spec)
            spec = re.sub(r'[A-Z]\{[^{}]*\}', 'l', spec)
            spec = re.sub(r'[A-Z]', 'l', spec)
            spec = spec.replace('|', '')
            return spec

        def tabx(opts, args, star):
            return '\\begin{tabular}{%s}' % clean_spec(args[1])
        out = []
        pos = 0
        for m in re.finditer(r'\\begin\{(tabularx|tabular\*?|longtable|array)\}', s):
            if m.start() < pos:
                continue
            i = m.end()
            _, i = read_opt(s, i)
            if m.group(1) in ('tabularx', 'tabular*'):
                _, i = read_arg(s, i)
            spec, i = read_arg(s, i)
            env = 'array' if m.group(1) == 'array' else 'tabular'
            out.append(s[pos:m.start()])
            out.append('\\begin{%s}{%s}' % (env, clean_spec(spec) if env == 'tabular' else spec))
            pos = i
        out.append(s[pos:])
        s = ''.join(out)
        s = re.sub(r'\\end\{(tabularx|tabular\*|longtable)\}', r'\\end{tabular}', s)

        def multicol(opts, args, star):
            return '\\multicolumn{%s}{%s}{%s}' % (args[0], 'l', args[2])
        s = sub_macro(s, 'multicolumn', 3, 0, multicol)
        return s

    def lists(self, s):
        s = re.sub(r'\\begin\{(enumerate|itemize|description)\}\s*\[[^\]]*(?:\{[^}]*\}[^\]]*)*\]',
                   r'\\begin{\1}', s)
        # \item[étiquette] dans enumerate -> liste à puces avec l'étiquette en gras
        out = []
        pos = 0
        while True:
            r = find_env(s, 'enumerate', pos)
            if not r:
                break
            a, b, c, d = r
            body = s[b:c]
            if re.search(r'\\item\s*\[', body):
                body = re.sub(r'\\item\s*\[((?:[^\[\]]|\{[^{}]*\})*)\]',
                              lambda mm: '\\item \\textbf{%s}~' % re.sub(r'\\textbf\{(.*)\}', r'\1', mm.group(1).strip()), body)
                body = re.sub(r'\\item(?!\s*\\textbf)', r'\\item ', body)
                out.append(s[pos:a] + '\\begin{itemize}' + body + '\\end{itemize}')
            else:
                out.append(s[pos:d])
            pos = d
        out.append(s[pos:])
        return ''.join(out)

    def sequential(self, s, ctx):
        s = re.sub(r'(\\ancre\{corr-[^}]*\})\s*\\textbf\{Exercice(?:[^{}]|\{[^{}]*\})*\}', r'\1', s)
        """Exercices (numérotation, étoiles, ancre, badge IA, emplacement du corrigé),
        activités (\\enteteactivite), intertitres."""
        names = ['iadefaut', 'ia', 'ancre', 'stars', 'exo', 'exercice', 'enteteactivite',
                 'section', 'subsection', 'subsubsection', 'edsection', 'edsubsection',
                 'paragraph', 'chapter', 'rubrique']
        pat = re.compile(r'\\(' + '|'.join(names) + r')(?![a-zA-Z@])(\*?)')
        st = ctx.setdefault('seq', {})
        st.setdefault('iadef', '')
        st['ianext'] = ''
        st['anchor'] = None
        st['stars'] = ''
        st.setdefault('act', 0)
        st.setdefault('ex', 0)
        st['open'] = None
        mode = ctx.get('mode')          # 'page' ou 'corrige'
        out = []
        pos = 0
        level = ctx.get('base_level', 2)

        def flush():
            if st['open'] is not None:
                key = st['open']
                st['open'] = None
                if mode == 'corrige':
                    return '\n\nQQCE%sQQ\n\n' % key
                return '\n\nQQSLOT%sQQ\n\n' % key
            return ''

        while True:
            m = pat.search(s, pos)
            if not m:
                break
            name = m.group(1)
            i = m.end()
            rep = ''
            if name == 'iadefaut':
                a, i = read_arg(s, i)
                st['iadef'] = a.strip()
            elif name == 'ia':
                a, i = read_arg(s, i)
                st['ianext'] = a.strip()
            elif name == 'ancre':
                a, i = read_arg(s, i)
                a = a.strip()
                if re.match(r'(ex|corr)-', a):
                    rep = flush()
                    st['anchor'] = a
                    if mode == 'corrige':
                        # le corrigé commence dès l'ancre (certains n'ont pas de \exercice)
                        key = a.split('-', 1)[1]
                        rep += '\n\nQQCS%sQQ\n\n' % key
                        st['open'] = key
                        st['anchor_open'] = True
                else:
                    rep = self.anchor(a)
            elif name == 'stars':
                a, i = read_arg(s, i)
                st['stars'] = a
            elif name in ('exo', 'exercice'):
                if name == 'exo':
                    stars, i = read_arg(s, i)
                    if stars.strip():
                        st['stars'] = stars
                title, i = read_arg(s, i)
                if mode == 'corrige' and st.get('anchor_open'):
                    st['anchor_open'] = False
                    st['anchor'] = None
                    st['ex'] += 1
                    out.append(s[pos:m.start()])
                    pos = i
                    continue
                rep = flush()
                st['ex'] += 1
                n = st['ex']
                anchor = st['anchor']
                key = anchor.split('-', 1)[1] if anchor else '%d.%d' % (st['act'], n)
                stars = st['stars'].count('bigstar') + st['stars'].count('★')
                ia = st['ianext'] or st['iadef']
                st['ianext'] = ''
                st['stars'] = ''
                st['anchor'] = None
                if mode == 'corrige':
                    rep += '\n\nQQCS%sQQ\n\n' % key
                    st['open'] = key
                else:
                    hid = anchor or 'ex-%s-%d-%d' % (ctx.get('slug', 'x'), st['act'], n)
                    if anchor:
                        self.anchors.setdefault(anchor, self.page)
                    tok = self.st.put(('exo', n, stars, ia, hid))
                    rep += '\n\nQQH%dQQ %s QQHEQQ\n\n' % (tok, title)
                    st['open'] = key
            elif name == 'enteteactivite':
                args = []
                for _ in range(4):
                    a, i = read_arg(s, i)
                    args.append(a)
                rep = flush()
                if mode != 'corrige' and st['act'] > 0:
                    rep += '\n\nQQSLOTA%dQQ\n\n' % st['act']
                st['act'] += 1
                st['ex'] = 0
                if mode == 'corrige':
                    rep += '\n\nQQCA%dQQ\n\n' % st['act']
                else:
                    tok = self.st.put(('act', args[0]))
                    rep += '\n\nQQH%dQQ %s QQHEQQ\n\n' % (tok, args[1])
                    if args[2].strip():
                        rep += '\\emph{%s}\n\n' % args[2]
                    if args[3].strip():
                        rep += self.inline('<p class="infos-activite">') + args[3] + \
                            self.inline('</p>') + '\n\n'
            elif name in ('section', 'subsection', 'subsubsection', 'paragraph', 'edsection',
                          'edsubsection', 'chapter', 'rubrique'):
                o = None
                if name == 'rubrique':
                    o, i = read_opt(s, i)
                    a, i = read_arg(s, i)
                    _, i = read_arg(s, i)
                elif name == 'edsection':
                    _, i = read_arg(s, i)
                    o, i = read_opt(s, i)
                    a, i = read_arg(s, i)
                else:
                    o, i = read_opt(s, i)
                    a, i = read_arg(s, i)
                rep = flush()
                lv = {'chapter': 1, 'section': 2, 'edsection': 2, 'rubrique': 2,
                      'subsection': 3, 'edsubsection': 3, 'subsubsection': 4,
                      'paragraph': 5}[name] + (level - 2)
                lv = max(2, min(lv, 5))
                if mode == 'corrige':
                    rep += '\n\n'   # les intertitres des corrigés ne sont pas repris
                else:
                    tok = self.st.put(('h', lv))
                    rep += '\n\nQQH%dQQ %s QQHEQQ\n\n' % (tok, a)
            out.append(s[pos:m.start()])
            out.append(rep)
            pos = i
        out.append(s[pos:])
        out.append(flush())
        if mode != 'corrige':
            out.append('\n\nQQSLOTA%dQQ\n\n' % st['act'])
        st['anchor_open'] = False
        return ''.join(out)

    # ------------------------------------------------------------------ pandoc
    def pandoc(self, s):
        prelude = ('\\newcommand{\\N}{\\mathbb{N}}\\newcommand{\\Z}{\\mathbb{Z}}'
                   '\\newcommand{\\R}{\\mathbb{R}}\\newcommand{\\Q}{\\mathbb{Q}}\n')
        r = subprocess.run([PANDOC, '-f', 'latex+raw_tex', '-t', MDFMT, '--wrap=none',
                            '--shift-heading-level-by=1'],
                           input=prelude + s, capture_output=True, text=True)
        if r.returncode != 0:
            raise RuntimeError('pandoc : ' + r.stderr[:2000])
        return r.stdout

    # ------------------------------------------------------------ post-pandoc
    def postprocess(self, md, store, ctx):
        V = self.st.vals
        # pandoc échappe parfois les marqueurs ; on normalise
        md = md.replace('\\QQ', 'QQ').replace('QQPCTQQ', '%')
        # 1. enveloppes (de l'intérieur vers l'extérieur)
        wpat = re.compile(r'QQW(\d+)aQQ((?:(?!QQW\d+aQQ).)*?)QQW\1zQQ', re.S)
        for _ in range(20):
            new = wpat.sub(lambda m: V[int(m.group(1))](m.group(2)), md)
            if new == md:
                break
            md = new
        # 2. titres
        def head(m):
            ind, n, title = m.group(1), int(m.group(2)), m.group(3).strip()
            v = V[n]
            if v[0] == 'h':
                return '%s%s %s' % (ind, '#' * v[1], title)
            if v[0] == 'act':
                lab = re.sub(r'\\[a-z]+|[{}]', '', v[1]).strip()
                return '%s## <span class="etiquette">%s</span> %s' % (ind, lab, title)
            _, num, stars, ia, hid = v
            st = '<span class="stars" title="Niveau %d sur 3">%s</span> ' % (stars, '★' * stars) \
                if stars else ''
            badge = ' ' + self.badge(ia) if ia else ''
            sep = ' — ' if title else ''
            return '%s### %s<span class="exo-num">Exercice %d</span>%s%s%s { #%s }' % (
                ind, st, num, sep, title, badge, hid)
        md = re.sub(r'^([ \t]*)QQH(\d+)QQ(.*?)QQHEQQ[ \t]*$', head, md, flags=re.M)
        # 3. jetons en ligne
        for _ in range(4):
            md = re.sub(r'QQI(\d+)QQ', lambda m: self.render_inline(V[int(m.group(1))]), md)
        # 4. code
        def code_block(m):
            ind, pre, k, post = m.group(1), m.group(2) or '', int(m.group(3)), m.group(4)
            kind, lang, code, raw = store[k]
            if kind == 'verb':
                tick = '``' if '`' in code else '`'
                return '%s%s%s%s%s%s%s' % (ind, pre, tick, code, tick, post, '')
            lines = code.split('\n')
            fence = '```'
            body = '\n'.join((ind + '    ' * bool(pre) + l) if l.strip() else '' for l in lines)
            open_ = ind + ('    ' * bool(pre)) + fence + lang
            close = ind + ('    ' * bool(pre)) + fence
            head_ = (ind + pre.rstrip() + '\n\n') if pre else ''
            return '%s%s\n%s\n%s%s' % (head_, open_, body, close,
                                        ('\n\n' + ind + post.strip()) if post.strip() else '')
        md = re.sub(r'^([ \t]*)((?:[-*+]|\d+\.)[ \t]+)?QQLST(\d+)QQ(.*)$', code_block, md,
                    flags=re.M)

        def verb_inline(m):
            kind, lang, code, raw = store[int(m.group(1))]
            if kind == 'verb':
                tick = '``' if '`' in code else '`'
                return tick + code + tick
            return '`' + code.replace('\n', ' ') + '`'
        md = re.sub(r'QQLST(\d+)QQ', verb_inline, md)
        # 5. admonitions (indentation)
        md = self.admonitions(md)
        return md

    def render_inline(self, v):
        if isinstance(v, str) and v.startswith('QQFIG:'):
            _, h, kind = v.split(':')
            rel = os.path.relpath('%s/figures/%s.svg' % (self.level, h), os.path.dirname(self.page))
            cls = 'tikz' if kind == 'b' else 'tikz tikz-inline'
            return '![](%s){ .%s loading=lazy }' % (rel, cls.replace(' ', ' .'))
        if isinstance(v, str) and v.startswith('QQIMG:'):
            _, src, style = v.split(':', 2)
            name = self.image_name(src)
            rel = os.path.relpath('%s/img/%s' % (self.level, name), os.path.dirname(self.page))
            st = (' style="%s"' % style) if style else ''
            return '![](%s){ .photo loading=lazy%s }' % (rel, st)
        return v

    def image_name(self, src):
        base, ext = os.path.splitext(os.path.basename(src))
        ext = ext.lower()
        if ext == '.pdf':
            ext = '.svg'
        if ext == '.jpeg':
            ext = '.jpg'
        name = base + ext
        self.images[src] = name
        return name

    def admonitions(self, md):
        V = self.st.vals
        out = []
        depth = []      # indentation supplémentaire cumulée
        begin = re.compile(r'^([ \t]*)((?:[-*+]|\d+\.)[ \t]+)?QQAB(\d+)QQ(.*?)QQABEQQ[ \t]*$')
        end = re.compile(r'^[ \t]*((?:[-*+]|\d+\.)[ \t]+)?QQAEQQ[ \t]*$')
        for line in md.split('\n'):
            extra = ' ' * (4 * len(depth))
            mb = begin.match(line)
            if mb:
                ind, marker, n, title = mb.group(1), mb.group(2), int(mb.group(3)), mb.group(4).strip()
                kind, coll, opened = V[n]
                if title == 'QQNOTITLEQQ':
                    title = ''
                title = self.plain_title(title)
                prefix = '???' + ('+' if opened else '') if coll else '!!!'
                if marker:
                    out.append(extra + ind + marker.rstrip() + ' <span></span>')
                    ind = ind + ' ' * 4
                    out.append('')
                out.append('%s%s%s %s "%s"' % (extra, ind, prefix, kind, title.replace('"', '&quot;')))
                depth.append(n)
                continue
            if end.match(line):
                if depth:
                    depth.pop()
                continue
            out.append((extra + line) if line.strip() else '')
        return '\n'.join(out)

    @staticmethod
    def plain_title(t):
        t = re.sub(r'\*\*(.*?)\*\*', r'\1', t)
        t = re.sub(r'(?<!\w)\*(.*?)\*(?!\w)', r'\1', t)
        t = re.sub(r'`([^`]*)`', r'\1', t)
        t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t)
        t = re.sub(r'<[^>]+>', '', t)
        t = t.replace('\\', '')
        return t.strip()


HANDLED = {'ancre', 'exref', 'coursretour', 'corrref', 'enoncref', 'titrecours', 'creditimage',
           'exercice', 'exo', 'stars', 'run', 'sol', 'papier', 'machine', 'iabadge', 'ia',
           'iadefaut', 'coupdepouce', 'afaire', 'horsprog', 'labelP', 'pts', 'correction',
           'fichierseleves', 'enteteactivite', 'edsection', 'edsubsection', 'qrcode',
           'legendeniveaux', 'ialegendecourte', 'ialegende', 'renvoicharte', 'testq',
           'autoposcases', 'afficherCoupsDePouce', 'arraystretch', 'aocurl_'}
