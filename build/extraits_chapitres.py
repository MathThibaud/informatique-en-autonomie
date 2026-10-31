"""Découpe un livre d'édition en un PDF par chapitre : pages du chapitre (activités, cours,
exercices, TP, fiche de révision, défis) suivies de ses corrigés.

Les pages sont copiées telles quelles : chaque extrait garde les numéros de page du livre
(imprimés et affichés par le lecteur PDF grâce aux étiquettes de page), si bien que les
renvois « corrigé p. N » restent justes. Les chapitres sont repérés par les signets du livre :
« Cours et exercices » > chapitre, et « Corrigés » > même titre.
"""
import re

import pymupdf as fitz


def _norm(t):
    return re.sub(r'^\d+\.\s*', '', t).strip()


def _sections(toc, parent, nb_pages):
    """{titre: (première, dernière page)} des entrées de niveau 2 sous le signet parent."""
    out, dans = {}, False
    plats = [(lvl, t, p) for lvl, t, p, *_ in toc if lvl <= 2]
    for i, (lvl, t, p) in enumerate(plats):
        if lvl == 1:
            dans = t == parent
            continue
        if dans:
            fin = plats[i + 1][2] - 1 if i + 1 < len(plats) else nb_pages
            out[t] = (p, fin)
    return out


def extraire(livre, titres, sortie):
    """Écrit un PDF par titre de chapitre (titres = {titre du site: nom de fichier}).
    Renvoie {titre du site: (chemin, nb de pages)}."""
    src = fitz.open(livre)
    toc = src.get_toc(simple=False)
    chap = _sections(toc, 'Cours et exercices', len(src))
    corr = _sections(toc, 'Corrigés', len(src))
    res = {}
    for titre, nom in titres.items():
        t = next((k for k in chap if _norm(k) == _norm(titre)), None)
        if not t:
            continue
        plages = [chap[t]] + ([corr[t]] if t in corr else [])
        doc = fitz.open()
        labels, signets = [], []
        for a, b in plages:
            labels.append({'startpage': len(doc), 'prefix': '', 'style': 'D', 'firstpagenum': a})
            debut = len(doc)
            doc.insert_pdf(src, from_page=a - 1, to_page=b - 1)
            # signets du livre compris dans la plage, renumérotés dans l'extrait
            for lvl, st, p, *_ in toc:
                if a <= p <= b and lvl >= 2:
                    nom_sig = st if (a, b) == plages[0] or lvl > 2 else 'Corrigés — ' + st
                    signets.append([lvl - 1, nom_sig, debut + p - a + 1])
        doc.set_page_labels(labels)
        # liens internes du livre (« corrigé p. N », « ↑ énoncé », sommaire du chapitre) :
        # insert_pdf les perd ; on les recrée quand la cible est dans l'extrait
        vers = {}
        for a, b in plages:
            for p in range(a - 1, b):
                vers[p] = len(vers)
        for p_src, p_dst in vers.items():
            for lien in src[p_src].get_links():
                cible = lien.get('page', -1)
                if lien['kind'] in (fitz.LINK_GOTO, fitz.LINK_NAMED) and cible in vers:
                    doc[p_dst].insert_link({'kind': fitz.LINK_GOTO, 'from': lien['from'],
                                            'page': vers[cible], 'to': lien.get('to', fitz.Point(0, 0)),
                                            'zoom': 0})
        if signets:
            m = min(s[0] for s in signets)
            for s in signets:
                s[0] -= m - 1
            # un signet ne peut pas descendre de plus d'un niveau d'un coup
            prec = 0
            for s in signets:
                s[0] = min(s[0], prec + 1)
                prec = s[0]
            doc.set_toc(signets)
        doc.set_metadata({'title': '%s — %s' % (src.metadata.get('title') or 'Manuel', _norm(titre)),
                          'author': src.metadata.get('author', '')})
        chemin = sortie / nom
        doc.save(chemin, garbage=4, deflate=True)
        res[titre] = (chemin, len(doc))
    return res
