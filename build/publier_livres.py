"""Publie les PDF des livres d'édition comme pièces jointes de la release GitHub « livres ».

Les PDF ne vont pas dans le dépôt (≈ 70 Mo, l'historique gonflerait à chaque mise à jour) :
ils sont remplacés en place dans la release, à une adresse stable. Seuls les PDF modifiés
sont renvoyés. Écrit build/livres.json (date et taille), lu par gen_site.py.
"""
import datetime
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OVERLEAF = Path.home() / 'Documents' / 'Overleaf'
REPO = 'MathThibaud/informatique-en-autonomie'
TAG = 'livres'
URL = 'https://github.com/%s/releases/download/%s/' % (REPO, TAG)
NIVEAUX = {'seconde': 'Seconde', 'premiere': 'Premiere', 'terminale': 'Terminale'}
FORMATS = {'livre_edition.pdf': '', 'livre_edition_a4.pdf': '-a4'}
MOIS = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre',
        'octobre', 'novembre', 'décembre']


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    etat_f = ROOT / '.cache' / 'livres_envoyes.json'
    etat = json.loads(etat_f.read_text()) if etat_f.exists() else {}
    if subprocess.run(['gh', 'release', 'view', TAG, '-R', REPO], capture_output=True).returncode:
        subprocess.run(['gh', 'release', 'create', TAG, '-R', REPO, '--title', 'Livres (PDF)',
                        '--notes', "Manuels d'édition en PDF (format livre 19×26 et format A4). "
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
            infos.setdefault(niv, {})[suffixe or 'livre'] = {
                'url': URL + nom, 'mo': round(p.stat().st_size / 1e6, 1),
                'date': '%d %s %d' % (d.day, MOIS[d.month - 1], d.year)}
    etat_f.parent.mkdir(exist_ok=True)
    etat_f.write_text(json.dumps(etat, indent=1))
    (ROOT / 'build' / 'livres.json').write_text(json.dumps(infos, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
