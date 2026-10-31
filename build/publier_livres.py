"""Publie les PDF des livres d'édition comme pièces jointes de la release GitHub « livres ».

Les PDF ne vont pas dans le dépôt (≈ 70 Mo, l'historique gonflerait à chaque mise à jour) :
ils sont remplacés en place dans la release, à une adresse stable. Seuls les PDF modifiés
sont renvoyés. Écrit build/livres.json (date et taille), lu par gen_site.py.
Publie aussi un PDF par chapitre (extraits_chapitres.py), renvoyés quand le livre a changé.
"""
import datetime
import hashlib
import json
import subprocess
import tempfile
from pathlib import Path

from extraits_chapitres import extraire

ROOT = Path(__file__).resolve().parent.parent
OVERLEAF = Path.home() / 'Documents' / 'Overleaf'
REPO = 'MathThibaud/informatique-en-autonomie'
TAG = 'livres'
URL = 'https://github.com/%s/releases/download/%s/' % (REPO, TAG)
NIVEAUX = {'seconde': 'Seconde', 'premiere': 'Premiere', 'terminale': 'Terminale'}
FORMATS = {'livre_edition.pdf': ''}   # format A4 unique depuis le 11-10-2026 (plus de 19×26)
MOIS = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre',
        'octobre', 'novembre', 'décembre']


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def chapitres(niv, livre, h, date, etat):
    """Un PDF par chapitre ; tous renvoyés si le livre a changé depuis le dernier envoi."""
    nav = json.loads((ROOT / 'build' / 'nav.json').read_text())[niv]
    titres = {t: 'chapitre-%s-%s.pdf' % (niv, sub[0][1].split('/')[1]) for t, sub in nav['chapters']}
    cle = 'chapitres-' + niv
    with tempfile.TemporaryDirectory() as tmp:
        res = extraire(livre, titres, Path(tmp))
        manquants = set(titres) - set(res)
        if manquants:
            print('  ! chapitres introuvables dans les signets du livre :', ', '.join(sorted(manquants)))
        if etat.get(cle) != h:
            print('  envoi des %d chapitres de %s' % (len(res), niv))
            subprocess.run(['gh', 'release', 'upload', TAG, *[str(c) for c, _ in res.values()],
                            '-R', REPO, '--clobber'], check=True)
            etat[cle] = h
        return {t: {'url': URL + c.name, 'mo': round(c.stat().st_size / 1e6, 1), 'pages': n,
                    'date': date} for t, (c, n) in res.items()}


def main():
    etat_f = ROOT / '.cache' / 'livres_envoyes.json'
    etat = json.loads(etat_f.read_text()) if etat_f.exists() else {}
    if subprocess.run(['gh', 'release', 'view', TAG, '-R', REPO], capture_output=True).returncode:
        subprocess.run(['gh', 'release', 'create', TAG, '-R', REPO, '--title', 'Livres (PDF)',
                        '--notes', "Manuels d'édition en PDF (format A4). "
                        'Remplacés à chaque mise à jour du site.'], check=True)
    infos = {}
    for niv, dossier in NIVEAUX.items():
        for src, suffixe in FORMATS.items():
            p = OVERLEAF / dossier / 'livre_autonome' / src
            if not p.exists():
                continue
            nom = 'manuel-%s%s.pdf' % (niv, suffixe)
            h = sha(p)
            if etat.get(nom) != h:
                print('  envoi de %s (%.1f Mo)' % (nom, p.stat().st_size / 1e6))
                cible = ROOT / '.cache' / nom
                cible.write_bytes(p.read_bytes())
                subprocess.run(['gh', 'release', 'upload', TAG, str(cible), '-R', REPO, '--clobber'],
                               check=True)
                cible.unlink()
                etat[nom] = h
            d = datetime.date.fromtimestamp(p.stat().st_mtime)
            date = '%d %s %d' % (d.day, MOIS[d.month - 1], d.year)
            infos.setdefault(niv, {})[suffixe or 'livre'] = {
                'url': URL + nom, 'mo': round(p.stat().st_size / 1e6, 1), 'date': date}
            infos[niv]['chapitres'] = chapitres(niv, p, h, date, etat)
    etat_f.parent.mkdir(exist_ok=True)
    etat_f.write_text(json.dumps(etat, indent=1))
    (ROOT / 'build' / 'livres.json').write_text(json.dumps(infos, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
