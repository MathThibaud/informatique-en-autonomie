"""Outils d'analyse LaTeX : groupes équilibrés, arguments, remplacement de macros."""
import re


def skip_ws(s, i):
    n = len(s)
    while i < n and s[i] in ' \t\n':
        # une ligne vide termine la recherche d'argument
        if s[i] == '\n' and s[i + 1:i + 2] == '\n':
            return i
        i += 1
    return i


def find_group(s, i):
    """s[i] == '{' ; renvoie (contenu, indice après '}')."""
    depth = 0
    j = i
    n = len(s)
    while j < n:
        c = s[j]
        if c == '\\':
            j += 2
            continue
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
        j += 1
    raise ValueError('groupe non fermé : ' + s[i:i + 80])


def find_opt(s, i):
    """s[i] == '[' ; renvoie (contenu, indice après ']')."""
    depth = 0
    j = i + 1
    n = len(s)
    while j < n:
        c = s[j]
        if c == '\\':
            j += 2
            continue
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
        elif c == ']' and depth == 0:
            return s[i + 1:j], j + 1
        j += 1
    raise ValueError('option non fermée : ' + s[i:i + 80])


def read_arg(s, i):
    """Lit un argument obligatoire (groupe, macro seule ou caractère)."""
    j = skip_ws(s, i)
    if j >= len(s):
        return '', j
    if s[j] == '{':
        return find_group(s, j)
    if s[j] == '\\':
        m = re.match(r'\\([a-zA-Z@]+|.)', s[j:])
        return m.group(0), j + m.end()
    return s[j], j + 1


def read_opt(s, i):
    j = skip_ws(s, i)
    if j < len(s) and s[j] == '[':
        return find_opt(s, j)
    return None, i


def sub_macro(s, name, nargs=0, nopt=0, fn=None, opt_after=0):
    """Remplace chaque \\name[opt]...{arg}... par fn(opts, args, star).

    nopt options avant les arguments ; opt_after options facultatives après."""
    pat = re.compile(r'\\' + re.escape(name) + r'(?![a-zA-Z@])')
    out = []
    pos = 0
    while True:
        m = pat.search(s, pos)
        if not m:
            break
        i = m.end()
        star = False
        if s.startswith('*', i):
            star = True
            i += 1
        opts = []
        args = []
        try:
            for _ in range(nopt):
                o, i = read_opt(s, i)
                opts.append(o)
            for _ in range(nargs):
                a, i = read_arg(s, i)
                args.append(a)
            for _ in range(opt_after):
                o, i = read_opt(s, i)
                opts.append(o)
        except ValueError:
            # argument coupé (formule au milieu, etc.) : on laisse tel quel
            out.append(s[pos:m.end()])
            pos = m.end()
            continue
        if nargs == 0 and nopt == 0 and not star:
            # TeX mange l'espace après un mot de contrôle
            pass
        out.append(s[pos:m.start()])
        out.append(fn(opts, args, star))
        pos = i
    out.append(s[pos:])
    return ''.join(out)


def find_env(s, name, start=0):
    """Trouve \\begin{name}...\\end{name} (imbrication gérée).
    Renvoie (debut, fin_begin, debut_end, fin) ou None."""
    b = re.compile(r'\\begin\{' + re.escape(name) + r'\}')
    e = re.compile(r'\\end\{' + re.escape(name) + r'\}')
    m = b.search(s, start)
    if not m:
        return None
    depth = 1
    pos = m.end()
    while depth:
        mb = b.search(s, pos)
        me = e.search(s, pos)
        if not me:
            raise ValueError('environnement non fermé : ' + name)
        if mb and mb.start() < me.start():
            depth += 1
            pos = mb.end()
        else:
            depth -= 1
            pos = me.end()
            if depth == 0:
                return m.start(), m.end(), me.start(), me.end()


def strip_comments(s):
    out = []
    for line in s.split('\n'):
        i = 0
        cut = None
        while i < len(line):
            c = line[i]
            if c == '\\':
                i += 2
                continue
            if c == '%':
                cut = i
                break
            i += 1
        if cut is None:
            out.append(line)
        else:
            stripped = line[:cut]
            # ligne entièrement commentée : on la supprime (sinon paragraphe parasite)
            if stripped.strip() == '':
                out.append(None)
            else:
                out.append(stripped)
    # une ligne de commentaire ne doit pas créer de paragraphe vide
    res = [l for l in out if l is not None]
    return '\n'.join(res)
