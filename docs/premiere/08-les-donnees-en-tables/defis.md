# Défis Advent of Code

<p class="sous-titre">Les données en tables</p>

## <span class="etiquette">Défi</span> Cube Conundrum

*les cubes de couleur — découpage imbriqué de chaînes*

<p class="infos-activite">Jour 2</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/08-defi-aoc-2023-02){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-08-defi-aoc-2023-02.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2023/day/2 ](https://adventofcode.com/2023/day/2 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (lien ci-dessus) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

*Ce défi réinvestit la lecture d’un fichier et le découpage de lignes en champs avec `split`, vus dans les défis précédents, avec ici plusieurs niveaux de séparateurs.*

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|          |                           |           |                   |
|:---------|:--------------------------|:----------|:------------------|
| cube     | cube                      | bag       | sac               |
| game     | partie                    | reveal    | montrer, révéler  |
| handful  | poignée                   | semicolon | point-virgule     |
| possible | possible                  | fewest    | le moins possible |
| power    | puissance (ici : produit) | set       | ensemble, lot     |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Sur une île, un elfe vous propose un jeu. Il a mis dans un sac des cubes rouges, verts et bleus, sans dire combien. À chaque partie, il sort plusieurs poignées de cubes, les montre, puis les remet dans le sac. Chaque ligne du fichier raconte une partie : son numéro, puis ce qu’on a vu à chaque poignée.

    **Ce qu’il faut faire.**

    - Format : `Game n:` puis les tirages séparés par `;`. Un tirage est une liste séparée par `,` de morceaux comme `3 blue` (couleurs `red`, `green`, `blue`).

    - L’énoncé indique un contenu possible du sac (un nombre de cubes de chaque couleur). Une partie est **possible** avec ce sac si aucun tirage ne montre plus de cubes d’une couleur que le sac n’en contient. Les cubes étant remis entre deux tirages, on compare chaque tirage séparément.

    - Réponse : la somme des numéros des parties possibles.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-aoc-1-1 }

Après lecture du résumé (et de l’énoncé), vérifier sa compréhension sur ces cas particuliers :

1.  Une couleur peut-elle être absente d’un tirage ? Qu’est-ce que cela change ?

2.  Si une partie montre 7 rouges dans un tirage puis 7 rouges dans un autre, faut-il additionner ?

3.  Un tirage avec exactement autant de cubes que le sac en contient est-il permis ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-aoc-1-2 }

On considère le fichier (inventé) suivant, avec le contenu du sac indiqué dans l’énoncé :

```console
Game 1: 4 red, 2 green; 1 blue, 13 red
Game 2: 3 blue; 5 green, 2 red; 1 red, 1 green, 2 blue
Game 3: 14 green, 3 red; 10 blue
Game 4: 6 blue, 6 red, 6 green
```

Quelles parties sont possibles ? Vérification : on doit obtenir `6`.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Découper une ligne, étage par étage <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-aoc-1-3 }

Rappel pour lire un fichier ligne par ligne :

```python
fichier = open("input.txt", encoding="utf-8")
for ligne in fichier:
    ligne = ligne.strip()   # enlève le retour à la ligne final
fichier.close()
```

Sur la ligne `"Game 2: 3 blue; 5 green, 2 red"`, obtenir successivement : le numéro `2` (un entier) ; la liste des tirages `["3 blue", "5 green, 2 red"]` ; pour chaque tirage, la liste de ses morceaux ; pour chaque morceau, le nombre (entier) et la couleur.

??? pouce "Coup de pouce"

    Quatre `split` emboîtés : sur `": "`, puis sur `"; "`, puis sur `", "`, enfin sur l’espace. Afficher le résultat de chaque étape avant de passer à la suivante.

??? pouce "Coup de pouce 2 (début de solution)"

    `entete, tirages = ligne.split(": ")` ; le numéro est `int(entete.split()[1])`. Puis `for tirage in tirages.split("; "):` et, dedans, `for morceau in tirage.split(", "):` avec `nombre, couleur = morceau.split()`.

### <span class="exo-num">Exercice 4</span> — Une partie est-elle possible ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-aoc-1-4 }

Écrire une fonction `est_possible(tirages)` qui reçoit la partie droite de la ligne (après les deux-points) et renvoie `True` si aucun morceau ne dépasse le contenu du sac. Puis calculer la réponse : `6` sur l’exemple.

??? pouce "Coup de pouce"

    Une fonction `maximum_autorise(couleur)` qui renvoie la limite correspondant à la couleur (trois `if`) rend le test très court : il suffit qu’un seul morceau dépasse pour que la partie soit impossible.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    L’elfe se demande maintenant combien de cubes il fallait au minimum. Pour chaque partie, le plus petit sac qui la rend possible contient, pour chaque couleur, le plus grand nombre vu dans un tirage de cette partie. La « puissance » d’une partie est le produit de ces trois nombres. Réponse : la somme des puissances de toutes les parties.

### <span class="exo-num">Exercice 5</span> — Le minimum nécessaire <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-aoc-1-5 }

Pour chaque partie, calculer le plus grand nombre de cubes rouges vus dans un même tirage, de même pour les verts et les bleus, puis répondre à la nouvelle question. Sur l’exemple du défi, on doit trouver `692`.

??? pouce "Coup de pouce"

    Trois variables `rouge`, `vert`, `bleu` initialisées à 0 au début de chaque partie, et mises à jour avec un `if` à chaque morceau. C’est un calcul de maximum (patron du champion), comme dans le chapitre sur les parcours de tableaux.

??? pouce "Coup de pouce 2 (début de solution)"

    Sur l’exemple, les maxima de `Game 4` sont `6, 6, 6`, ce qui donne `216`. Ajouter le produit des trois maxima à un total.

## Approfondissement

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Approfondissement 1 : une seule fonction <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-aoc-1-6 }

1.  Écrire une fonction `maxima(tirages)` qui renvoie le triplet `(rouge, vert, bleu)` des maxima d’une partie (si ce n’est déjà fait en partie 2), puis réécrire la partie 1 en n’utilisant que cette fonction.

    ??? pouce "Coup de pouce"

        Une partie est possible si et seulement si chacun de ses trois maxima est inférieur ou égal au contenu du sac.

2.  À la main : donner les maxima de `Game 3` de l’exemple. Pourquoi la partie est-elle impossible ?

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 2 : un dictionnaire de couleurs <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-aoc-1-7 }

Remplacer les trois variables `rouge`, `vert`, `bleu` par un dictionnaire `plus_grand` dont les clés sont les noms des couleurs. Quel avantage si l’on ajoutait une quatrième couleur ?

??? pouce "Coup de pouce"

    Initialiser `plus_grand = {"red": 0, "green": 0, "blue": 0}` ; la couleur lue dans le morceau sert directement de clé, plus besoin de `if`.
