# Informatique en autonomie — les cours

Cours de SNT (Seconde) et de NSI (Première, Terminale) de Mathieu Thibaud : activités, cours, exercices avec corrigés dépliables, TP.

**Site : https://maththibaud.github.io/informatique-en-autonomie/**

Le contenu de `docs/` est généré automatiquement à partir des sources LaTeX (manuel d'édition) par les scripts de `build/` ; il est mis à jour régulièrement. Les fiches et le manuel distribués en classe font foi.

Licence : [CC BY-NC-SA 4.0](LICENSE.md). La forme du site s'inspire du travail de [Gilles Lassus](https://glassus.github.io/).

## Régénérer (poste de l'auteur)

```sh
python3.11 -m venv .venv && .venv/bin/pip install -r requirements.txt
./build.sh            # git pull Overleaf, conversion, figures, mkdocs build
git add -A && git commit -m "Mise à jour" && git push   # publication automatique
```
