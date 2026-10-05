"""Génère docs/stylesheets/v3.css : thème Material aux couleurs des sites v3/v4."""
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
ICONS = ROOT / '.venv/lib/python3.11/site-packages/material/templates/.icons/material'

# type d'admonition -> (variable de couleur, icône)
ADM = {
    'definition': ('--c-blue', 'book-open-variant'),
    'regle': ('--c-green', 'gavel'),
    'propriete': ('--c-purple', 'check-decagram'),
    'theoreme': ('--c-purple', 'math-integral'),
    'remarque': ('--c-yellow', 'information-outline'),
    'exemple': ('--c-teal', 'flask-outline'),
    'demonstration': ('--c-dim', 'function-variant'),
    'consignes': ('--c-purple', 'clipboard-list-outline'),
    'encadre': ('--c-dim', 'card-text-outline'),
    'activite': ('--c-green', 'puzzle-outline'),
    'etudedoc': ('--c-blue', 'file-document-outline'),
    'passerelle': ('--c-orange', 'puzzle-outline'),
    'navigateur': ('--c-dim', 'monitor'),
    'projet': ('--c-orange', 'rocket-launch-outline'),
    'monaco': ('--c-red', 'flag-variant'),
    'flash': ('--c-yellow', 'lightning-bolt'),
    'testetoi': ('--c-purple', 'help-circle-outline'),
    'autopos': ('--c-blue', 'checkbox-marked-outline'),
    'corrige': ('--c-green', 'check-circle-outline'),
    'reponse': ('--c-green', 'eye-check-outline'),
    'pouce': ('--c-yellow', 'lightbulb-on-outline'),
    'fichiers': ('--c-blue', 'file-download-outline'),
    'livre': ('--c-green', 'book-open-variant'),
}


def icon(name):
    svg = (ICONS / (name + '.svg')).read_text().strip()
    return "url('data:image/svg+xml;charset=utf-8,%s')" % quote(svg)


BASE = r'''
/* Thème « Informatique en autonomie » : palette des sites v3/v4 (GitHub sombre, accent vert). */
:root {
  --c-green: #39d353; --c-blue: #58a6ff; --c-purple: #bc8cff; --c-yellow: #e3b341;
  --c-red: #f85149; --c-orange: #f0883e; --c-teal: #39c5cf; --c-dim: #8b949e;
  --font-mono: 'JetBrains Mono', 'Fira Code', 'Courier New', 'Lucida Console', monospace;
  --font-ui: 'Segoe UI', system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif;
  --md-text-font-family: var(--font-ui);
  --md-code-font-family: var(--font-mono);
}
[data-md-color-scheme="slate"] {
  --bg: #0d1117; --bg-card: #161b22; --border: #30363d; --text: #c9d1d9; --text-dim: #8b949e;
  --md-hue: 215;
  --md-default-bg-color: #0d1117;
  --md-default-fg-color: #c9d1d9;
  --md-default-fg-color--light: #8b949e;
  --md-default-fg-color--lighter: #6e7681;
  --md-default-fg-color--lightest: #30363d;
  --md-primary-fg-color: #161b22;
  --md-primary-fg-color--light: #161b22;
  --md-primary-fg-color--dark: #0d1117;
  --md-primary-bg-color: #c9d1d9;
  --md-primary-bg-color--light: #8b949e;
  --md-accent-fg-color: #39d353;
  --md-typeset-color: #c9d1d9;
  --md-typeset-a-color: #58a6ff;
  --md-code-bg-color: #161b22;
  --md-code-fg-color: #e6edf3;
  --md-footer-bg-color: #161b22;
  --md-footer-bg-color--dark: #0d1117;
  --md-admonition-bg-color: #161b22;
  --c-titre: #39d353;
  --fond-image: linear-gradient(rgba(13,17,23,.88), rgba(13,17,23,.88)), url('../assets/bg-code.webp');
}
[data-md-color-scheme="default"] {
  --bg: #ffffff; --bg-card: #f6f8fa; --border: #d0d7de; --text: #1f2328; --text-dim: #57606a;
  --c-green: #0a5c27; --c-blue: #0860c1; --c-purple: #8250df; --c-yellow: #735900;
  --c-red: #cf222e; --c-orange: #9a4b00; --c-teal: #0a6b73; --c-dim: #57606a;
  --md-default-bg-color: #ffffff;
  --md-default-fg-color: #1f2328;
  --md-default-fg-color--light: #57606a;
  --md-primary-fg-color: #f6f8fa;
  --md-primary-fg-color--light: #f6f8fa;
  --md-primary-fg-color--dark: #eaeef2;
  --md-primary-bg-color: #1f2328;
  --md-primary-bg-color--light: #57606a;
  --md-accent-fg-color: #0a5c27;
  --md-typeset-color: #1f2328;
  --md-typeset-a-color: #0860c1;
  --md-code-bg-color: #161b22;
  --md-code-fg-color: #e6edf3;
  --md-footer-bg-color: #f6f8fa;
  --md-footer-fg-color: #1f2328;
  --md-footer-fg-color--light: #57606a;
  --md-footer-fg-color--lighter: #6e7781;
  --md-footer-bg-color--dark: #eaeef2;
  --c-titre: #0a5c27;
  --fond-image: linear-gradient(rgba(255,255,255,.93), rgba(255,255,255,.93)), url('../assets/bg-code.webp');
}

body { background: var(--fond-image) center / cover fixed, var(--md-default-bg-color); }
.md-main, .md-container { background: transparent; }

/* --- En-tête façon barre de navigation v3 --- */
.md-header { border-bottom: 1px solid var(--border); box-shadow: none; }
.md-header__topic:first-child, .md-header__title { font-family: var(--font-mono); font-weight: 700; }
.md-header__topic:first-child .md-ellipsis { color: var(--c-titre); }
.md-tabs { background: var(--bg-card); border-bottom: 1px solid var(--border); }
.md-tabs__link { font-family: var(--font-mono); font-size: .72rem; color: var(--text-dim); opacity: 1;
  padding: .15rem .6rem; border-radius: 6px; margin-top: .5rem; }
.md-tabs__item { padding: 0 .3rem; }
.md-tabs__link:hover { color: var(--c-green); background: color-mix(in srgb, var(--c-green) 10%, transparent); }
.md-tabs__item--active .md-tabs__link { color: var(--bg); background: var(--c-green); font-weight: 700; }
.md-search__form { background: var(--bg); border: 1px solid var(--border); border-radius: 6px; }
.md-footer { border-top: 1px solid var(--border); }
.md-footer-meta { background: var(--bg-card); }

/* --- Navigation latérale --- */
.md-nav__link--active, .md-nav__item .md-nav__link--active { color: var(--c-green); font-weight: 600; }
.md-nav__link:hover { color: var(--c-green) !important; }
.md-nav__title { font-family: var(--font-mono); }

/* --- Contenu --- */
.md-content__inner { background: color-mix(in srgb, var(--bg) 80%, transparent);
  border: 1px solid var(--border); border-radius: 8px; padding: 1rem 1.6rem 2rem; margin-top: 1rem; }
.md-typeset h1 { font-family: var(--font-mono); color: var(--c-titre); font-weight: 700; margin-bottom: .3em; }
.md-typeset h2 { color: var(--c-purple); font-weight: 700; border-bottom: 1px solid var(--border);
  padding-bottom: .2em; }
.md-typeset h3 { color: var(--c-blue); font-weight: 700; }
.md-typeset h4 { color: var(--text); font-weight: 700; }
.md-typeset .sous-titre { font-family: var(--font-mono); color: var(--text-dim); margin-top: -.6em; }
.md-typeset a { text-decoration: underline; text-underline-offset: 2px; }
.md-typeset .md-button, .md-typeset .headerlink, .md-typeset .grid.cards a, .md-typeset a.carte-niveau
  { text-decoration: none; }
.md-typeset .md-button { font-family: var(--font-mono); font-size: .75rem; border-radius: 6px;
  border: 1px solid var(--border); color: var(--text); padding: .4em 1em; margin: .2em .3em .2em 0; }
.md-typeset .md-button:hover { border-color: var(--c-green); color: var(--c-green); background: transparent; }
.md-typeset code { border-radius: 4px; }
.md-typeset :not(pre) > code { background: color-mix(in srgb, var(--c-blue) 12%, transparent);
  color: var(--text); }
.md-typeset pre > code { border: 1px solid #30363d; border-radius: 6px; }
.md-typeset table:not([class]) { font-size: .72rem; }
.md-typeset table:not([class]) th { background: var(--bg-card); }

/* --- Exercices --- */
.md-typeset h3 .exo-num { font-family: var(--font-mono); color: var(--bg); background: var(--c-blue);
  border-radius: 4px; padding: .05em .45em; font-size: .85em; }
.md-typeset .stars { color: var(--c-yellow); letter-spacing: .05em; font-size: .9em; }
.md-typeset h2 .etiquette { font-family: var(--font-mono); font-size: .7em; color: var(--bg);
  background: var(--c-purple); border-radius: 4px; padding: .1em .5em; vertical-align: .15em; }
.md-typeset .infos-activite { font-family: var(--font-mono); font-size: .75rem; color: var(--text-dim); }
.md-typeset .run { color: var(--c-green); }
.md-typeset .tag { font-family: var(--font-mono); font-size: .7em; color: var(--c-purple);
  border: 1px solid currentColor; border-radius: 4px; padding: 0 .35em; }
.md-typeset .horsprog { font-family: var(--font-mono); font-size: .7em; color: var(--c-orange);
  border: 1px solid currentColor; border-radius: 4px; padding: 0 .35em; }
.md-typeset .afaire { color: var(--c-green); font-weight: 700; }
.md-typeset .credit { font-size: .8em; color: var(--text-dim); }

/* Feu tricolore « usage de l'IA » */
.md-typeset .ia { display: inline-block; vertical-align: middle; font-family: var(--font-mono);
  font-size: .6rem; font-weight: 700; line-height: 1; border-radius: 99px; padding: .25em .6em;
  border: 1px solid currentColor; cursor: help; }
.md-typeset .ia::before { content: "IA"; }
.md-typeset .ia-rouge { color: var(--c-red); }
.md-typeset .ia-rouge::before { content: "✕ sans IA"; }
.md-typeset .ia-orange { color: var(--c-yellow); }
.md-typeset .ia-orange::before { content: "◐ IA en appui"; }
.md-typeset .ia-vert { color: var(--c-green); }
.md-typeset .ia-vert::before { content: "● IA intégrée"; }

.md-typeset .md-button--primary { background: var(--c-green); border-color: var(--c-green);
  color: var(--bg); font-weight: 700; }
.md-typeset .md-button--primary:hover { background: transparent; color: var(--c-green); }

/* --- Figures --- */
.md-typeset img.tikz { display: block; margin: .8em auto; max-width: 100%; height: auto;
  background: #fff; border-radius: 6px; padding: .35rem; }
.md-typeset img.tikz-inline { display: inline-block; margin: 0 .15em; vertical-align: middle; padding: .1rem; }
.md-typeset img.photo { display: block; margin: .8em auto; max-width: 100%; height: auto; border-radius: 6px; }
.md-typeset td img.tikz, .md-typeset td img.photo { margin: .2em auto; }
.md-typeset img.ouverture { display: block; margin: 0 auto 1.5em; max-height: 280px; border-radius: 8px; }

/* --- Cartes --- */
.md-typeset .grid.cards > ul > li, .md-typeset .grid > .card { background: var(--bg-card);
  border: 1px solid var(--border); border-radius: 6px; }
.md-typeset .grid.cards > ul > li:hover { border-color: var(--c-blue);
  box-shadow: none; transform: translateY(-2px); transition: all .15s; }
.md-typeset .rubriques a { font-weight: 600; }
.liens-annee { margin: 1em 0; }

/* --- Accueil --- */
.md-typeset .hero { text-align: center; padding: 1.5rem 0 1rem; }
.md-typeset .hero h1 { font-family: var(--font-mono); font-size: 2.3rem; color: var(--c-titre); margin: .2em 0; }
.md-typeset .hero-prompt { font-family: var(--font-mono); color: var(--text-dim); margin: 0; }
.md-typeset .prompt { color: var(--c-green); }
.md-typeset .hero-sub { color: var(--text-dim); font-size: 1.05rem; }
.niveaux { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin: 1.5rem 0; }
.md-typeset a.carte-niveau { display: flex; flex-direction: column; gap: .35rem; padding: 1.3rem;
  border: 1px solid var(--border); border-radius: 8px; background: var(--bg-card); color: var(--text);
  transition: all .15s; }
.md-typeset a.carte-niveau:hover { border-color: var(--c-green); transform: translateY(-3px);
  background: color-mix(in srgb, var(--c-green) 6%, var(--bg-card)); }
.carte-mat { font-family: var(--font-mono); color: var(--c-yellow); font-size: .8rem; font-weight: 700; }
.carte-titre { font-family: var(--font-mono); font-size: 1.5rem; font-weight: 700; color: var(--c-green); }
.carte-long { font-size: .8rem; color: var(--text); font-weight: 600; }
.carte-desc { font-size: .75rem; color: var(--text-dim); line-height: 1.45; }
.carte-nb { font-family: var(--font-mono); font-size: .75rem; color: var(--c-blue); margin-top: auto; padding-top: .4rem; }
.accueil-infos { text-align: center; color: var(--text-dim); max-width: 40rem; margin: 1rem auto; }

/* --- Admonitions --- */
.md-typeset .admonition, .md-typeset details { border-width: 0 0 0 4px; border-radius: 6px;
  background: var(--bg-card); box-shadow: none; font-size: .78rem; }
.md-typeset .admonition-title, .md-typeset summary { font-weight: 700; }
.md-typeset details.corrige, .md-typeset details.pouce, .md-typeset details.reponse { margin-top: .6em; }
'''


def main():
    css = [BASE]
    for kind, (var, ic) in ADM.items():
        css.append(':root { --md-admonition-icon--%s: %s; }' % (kind, icon(ic)))
        css.append('.md-typeset .admonition.%s, .md-typeset details.%s { border-color: var(%s); }'
                   % (kind, kind, var))
        css.append('.md-typeset .%s > .admonition-title, .md-typeset .%s > summary '
                   '{ background-color: color-mix(in srgb, var(%s) 12%%, transparent); }' % (kind, kind, var))
        css.append('.md-typeset .%s > .admonition-title::before, .md-typeset .%s > summary::before '
                   '{ background-color: var(%s); -webkit-mask-image: var(--md-admonition-icon--%s); '
                   'mask-image: var(--md-admonition-icon--%s); }' % (kind, kind, var, kind, kind))
        css.append('.md-typeset .%s > summary::after { color: var(%s); }' % (kind, var))
    (ROOT / 'docs/stylesheets/v3.css').write_text('\n'.join(css) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
