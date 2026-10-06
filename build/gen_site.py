"""Génère mkdocs.yml, la page d'accueil et les pages d'accueil des niveaux (à partir de nav.json)."""
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / 'docs'
NAV = json.loads((ROOT / 'build' / 'nav.json').read_text())
_LIV = ROOT / 'build' / 'livres.json'
LIVRES = json.loads(_LIV.read_text()) if _LIV.exists() else {}

LEVELS = [
    ('seconde', 'Seconde', 'SNT', 'Sciences numériques et technologie',
     'Python, Web, Internet, réseaux sociaux, photo numérique, données, localisation, objets connectés.',
     ':material-earth:'),
    ('premiere', 'Première', 'NSI', 'Numérique et sciences informatiques — spécialité',
     'Python, types construits, données en tables, tris, algorithmes, Web, architecture et OS.',
     ':material-language-python:'),
    ('terminale', 'Terminale', 'NSI', 'Numérique et sciences informatiques — spécialité',
     'Récursivité, POO, structures de données, arbres, graphes, SQL, réseaux, cryptographie.',
     ':material-graph-outline:'),
]


def level_nav(key, titre):
    n = NAV[key]
    items = [{'Accueil %s' % titre: '%s/index.md' % key}]
    for t, p in n['front']:
        items.append({t: p})
    for t, sub in n['chapters']:
        items.append({t: [p for _, p in sub[:1]] + [{lab: p} for lab, p in sub[1:]]})
    if n['pratique']:
        items.append({'Épreuve pratique': [n['pratique'][0][1]] +
                      [{t: p} for t, p in n['pratique'][1:]]})
    for t, p in n.get('annexes', []):
        items.append({t: p})
    if n['credits']:
        items.append({'Crédits iconographiques': '%s/credits.md' % key})
    return items


def level_index(key, titre, mat, long_, desc, icon):
    n = NAV[key]
    md = ['---', 'hide:', '  - toc', '---', '',
          '# %s %s' % (mat, titre), '', '<p class="sous-titre">%s</p>' % long_, '']
    if n['front']:
        md.append('<div class="liens-annee" markdown>\n')
        for t, p in n['front']:
            md.append('[%s](%s){ .md-button }' % (t, p.split('/', 1)[1]))
        md.append('\n</div>\n')
    liv = LIVRES.get(key)
    if liv and 'livre' in liv:
        b = liv['livre']
        md.append('!!! livre "Le manuel complet en PDF"\n')
        md.append('    Tout le cours, les exercices et les corrigés de l\'année, dans la version '
                  'distribuée en classe (version du %s).\n' % b['date'])
        md.append('    [:material-download: Télécharger le manuel (%s Mo)](%s){ .md-button .md-button--primary }'
                  % (str(b['mo']).replace('.', ','), b['url']))
        if '-a4' in liv:
            a = liv['-a4']
            md.append('    [:material-printer: Version A4 à imprimer (%s Mo)](%s){ .md-button }'
                      % (str(a['mo']).replace('.', ','), a['url']))
        md.append('')
    md.append('## Chapitres\n')
    md.append('<div class="grid cards chapitres" markdown>\n')
    for t, sub in n['chapters']:
        idx = sub[0][1].split('/', 1)[1]
        labels = ' · '.join(lab for lab, _ in sub[1:])
        md.append('-   [**%s**](%s)\n\n    <small>%s</small>\n' % (t, idx, labels))
    md.append('</div>\n')
    if n['pratique']:
        md.append("## Épreuve pratique\n")
        md.append("[Sujets d'entraînement (%d)](%s){ .md-button }\n" %
                  (len(n['pratique']) - 1, n['pratique'][0][1].split('/', 1)[1]))
    (DOCS / key / 'index.md').write_text('\n'.join(md) + '\n', encoding='utf-8')


def home():
    cards = []
    for key, titre, mat, long_, desc, icon in LEVELS:
        if key not in NAV:
            continue
        nb = len(NAV[key]['chapters'])
        cards.append('''<a class="carte-niveau niveau-%s" href="%s/">
  <span class="carte-mat">%s</span>
  <span class="carte-titre">%s</span>
  <span class="carte-long">%s</span>
  <span class="carte-desc">%s</span>
  <span class="carte-nb">%d chapitres →</span>
</a>''' % (key, key, mat, titre, long_, desc, nb))
    md = '''---
hide:
  - navigation
  - toc
---

<div class="hero" markdown>

<p class="hero-prompt"><span class="prompt">&gt;_</span> cours d'informatique au lycée</p>

# Informatique en autonomie

<p class="hero-sub">Cours, exercices corrigés, activités et TP — de la Seconde à la Terminale.</p>

</div>

<div class="niveaux">
%s
</div>

<div class="accueil-infos" markdown>

Chaque chapitre propose des **activités** de découverte, le **cours**, une feuille d'**exercices**
dont les **corrigés se déplient** sous chaque énoncé, et des **TP**. Les fichiers Python à compléter
sont téléchargeables depuis les TP.

Ces pages sont une version web du manuel distribué aux élèves ; elles sont mises à jour
régulièrement. En cas d'écart, **les fiches et le manuel distribués en classe font foi**.

[À propos et licence](a-propos.md){ .md-button }

</div>
''' % '\n'.join(cards)
    (DOCS / 'index.md').write_text(md, encoding='utf-8')


def a_propos():
    md = '''# À propos

## L'auteur

Ces cours sont rédigés par **Mathieu Thibaud**, professeur d'informatique (SNT et NSI).
Ils sont écrits en LaTeX ; ce site en est une conversion automatique, accompagnée des
corrigés et des figures d'origine.

## Licence

![Licence Creative Commons BY-NC-SA](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-nc-sa.svg){ width="120" }

Sauf mention contraire, l'ensemble des contenus de ce site est mis à disposition selon les termes de la
licence [Creative Commons Attribution – Pas d'utilisation commerciale – Partage dans les mêmes conditions 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.fr).

Vous pouvez réutiliser, adapter et partager ces contenus **en citant l'auteur**, **sans usage commercial**,
et en diffusant vos adaptations **sous la même licence**.

Les images reproduites (photographies, portraits, documents historiques) restent soumises à leur propre
licence, indiquée dans les pages « Crédits iconographiques » de chaque niveau.

## Remerciements

La forme de ce site s'inspire du travail de **Gilles Lassus**, dont les cours de NSI en ligne
([glassus.github.io](https://glassus.github.io/)) sont une référence pour de nombreux enseignants.

Merci également à **David Roche** : son site [pixees.fr/informatiquelycee](https://pixees.fr/informatiquelycee/),
qu'il partage librement, m'a beaucoup aidé dans la préparation de mes cours de SNT et de NSI.

## Mises à jour

Le site est mis à jour régulièrement. Les fiches individuelles et le manuel distribués
en classe restent la version de référence.

## Signaler une erreur

Une coquille, une erreur dans un corrigé ? Signalez-la à votre professeur ou ouvrez une *issue* sur le
dépôt du site.
'''
    (DOCS / 'a-propos.md').write_text(md, encoding='utf-8')


def mkdocs_yml():
    nav = [{'Accueil': 'index.md'}]
    for key, titre, *_ in LEVELS:
        if key in NAV:
            nav.append({titre: level_nav(key, titre)})
    nav.append({'À propos': 'a-propos.md'})
    cfg = {
        'site_name': 'Informatique en autonomie',
        'site_description': "Cours d'informatique au lycée (SNT, NSI) — cours, exercices corrigés, TP",
        'site_author': 'Mathieu Thibaud',
        'site_url': 'https://maththibaud.github.io/informatique-en-autonomie/',
        'repo_url': 'https://github.com/MathThibaud/informatique-en-autonomie',
        'repo_name': 'informatique-en-autonomie',
        'edit_uri': '',
        'copyright': ('© 2026 Mathieu Thibaud — <a href="https://creativecommons.org/licenses/'
                      'by-nc-sa/4.0/deed.fr">CC BY-NC-SA 4.0</a>'),
        'theme': {
            'name': 'material',
            'language': 'fr',
            'custom_dir': 'overrides',
            'font': False,
            'logo': 'assets/favicon.svg',
            'favicon': 'assets/favicon-32.png',
            'palette': [
                {'media': '(prefers-color-scheme: dark)', 'scheme': 'slate', 'primary': 'custom',
                 'accent': 'custom', 'toggle': {'icon': 'material/weather-sunny',
                                                'name': 'Passer en mode clair'}},
                {'media': '(prefers-color-scheme: light)', 'scheme': 'default', 'primary': 'custom',
                 'accent': 'custom', 'toggle': {'icon': 'material/weather-night',
                                                'name': 'Passer en mode sombre'}},
            ],
            'features': ['navigation.tabs', 'navigation.tabs.sticky', 'navigation.indexes',
                         'navigation.top', 'navigation.footer', 'navigation.tracking',
                         'navigation.instant', 'navigation.instant.progress',
                         'toc.follow', 'search.highlight', 'search.suggest',
                         'content.code.copy'],
        },
        'extra_css': ['stylesheets/v3.css'],
        'extra_javascript': ['javascripts/mathjax.js',
                             'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js'],
        'markdown_extensions': [
            'abbr', 'attr_list', 'md_in_html', 'tables', 'def_list', 'footnotes', 'admonition',
            {'toc': {'permalink': '#', 'toc_depth': 3}},
            'pymdownx.details',
            {'pymdownx.superfences': {}},
            {'pymdownx.highlight': {'anchor_linenums': False, 'use_pygments': True}},
            'pymdownx.inlinehilite',
            {'pymdownx.arithmatex': {'generic': True, 'inline_syntax': ['dollar'], 'block_syntax': ['dollar']}},
            {'pymdownx.emoji': {'emoji_index': '!!python/name:material.extensions.emoji.twemoji',
                                'emoji_generator': '!!python/name:material.extensions.emoji.to_svg'}},
            {'pymdownx.tasklist': {'custom_checkbox': True}},
            'pymdownx.caret', 'pymdownx.tilde',
        ],
        'plugins': [{'search': {'lang': 'fr'}}],
        'validation': {'omitted_files': 'warn', 'absolute_links': 'warn',
                       'unrecognized_links': 'warn', 'anchors': 'warn'},
        'extra': {'generator': False},
        'nav': nav,
    }
    txt = yaml.safe_dump(cfg, allow_unicode=True, sort_keys=False, width=200)
    txt = txt.replace("'!!python/name:material.extensions.emoji.twemoji'",
                      '!!python/name:material.extensions.emoji.twemoji')
    txt = txt.replace("'!!python/name:material.extensions.emoji.to_svg'",
                      '!!python/name:material.extensions.emoji.to_svg')
    (ROOT / 'mkdocs.yml').write_text(txt, encoding='utf-8')


if __name__ == '__main__':
    home()
    a_propos()
    for lv in LEVELS:
        if lv[0] in NAV:
            level_index(*lv)
    mkdocs_yml()
