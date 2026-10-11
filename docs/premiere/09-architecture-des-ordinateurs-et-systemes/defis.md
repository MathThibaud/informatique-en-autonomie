# Défis Advent of Code

<p class="sous-titre">Architecture des ordinateurs et systèmes d'exploitation</p>

## <span class="etiquette">Défi</span> Cathode-Ray Tube

*l’écran du communicateur — simuler un petit processeur*

<p class="infos-activite">Jour 10</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/09-defi-aoc-2022-10){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-09-defi-aoc-2022-10.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2022/day/10 ](https://adventofcode.com/2022/day/10 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (lien ci-dessus) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

*Ce défi réinvestit le fonctionnement d’un processeur vu dans ce chapitre : horloge, cycles et registre.*

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|                 |                     |             |                       |
|:----------------|:--------------------|:------------|:----------------------|
| clock circuit   | horloge (circuit)   | cycle       | cycle (top d’horloge) |
| register        | registre            | instruction | instruction           |
| take two cycles | durer deux cycles   | during      | pendant               |
| signal strength | intensité du signal | CRT         | écran cathodique      |
| pixel           | pixel               | sprite      | sprite, motif affiché |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** L’écran de votre appareil de communication est cassé, et pour le remplacer il faut comprendre le petit processeur qui le pilote. Ce processeur est cadencé par une horloge et possède un seul registre, `X`. Le fichier est le programme qu’il exécute, une instruction par ligne. On veut suivre la valeur de `X` au fil des cycles d’horloge.

    **Ce qu’il faut faire.**

    - `X` vaut **1** au départ ; les cycles sont numérotés à partir de 1.

    - `noop` dure 1 cycle et ne fait rien. `addx n` dure 2 cycles, et `X` augmente de `n` (entier, parfois négatif) seulement **à la fin** de ces deux cycles : pendant ces cycles, `X` garde son ancienne valeur.

    - L’intensité du signal pendant le cycle $c$ vaut $c \times$ (valeur de `X` **pendant** ce cycle).

    - Réponse : la somme des intensités pendant les cycles 20, 60, 100, 140, 180 et 220.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-aoc-1-1 }

Après lecture du résumé (et de l’énoncé), vérifier sa compréhension sur ces cas particuliers :

1.  Pendant les deux cycles d’un `addx 3`, `X` a-t-il déjà augmenté ?

2.  Si l’on calcule `X` *après* le cycle 20 au lieu de *pendant*, quelle erreur commet-on ?

3.  Combien de cycles dure un programme de 5 `noop` et 5 `addx` ?

!!! encadre "Lien avec le cours : l’architecture de von Neumann"

    Ce petit processeur ressemble à celui du chapitre sur l’architecture : une **horloge** cadence le travail, le programme est une suite d’instructions exécutées l’une après l’autre, et un **registre** (ici `X`) garde une valeur que les instructions modifient. Certaines instructions demandent plus de cycles que d’autres, comme dans un vrai processeur.

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-aoc-1-2 }

On considère le programme (inventé) suivant :

```console
noop
addx 4
addx -2
noop
addx 5
addx -1
```

Remplir un tableau à deux lignes : numéro du cycle (de 1 à 10) et valeur de `X` **pendant** ce cycle. Vérification : pendant le cycle 4, `X` vaut $5$ ; pendant le cycle 9, il vaut $8$ ; à la fin du programme, il vaut $7$. Que vaudrait l’intensité du signal pendant le cycle 6 ? (On doit trouver $18$.)

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire le programme <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-aoc-1-3 }

Rappel pour lire un fichier ligne par ligne :

```python
fichier = open("input.txt", encoding="utf-8")
for ligne in fichier:
    ligne = ligne.strip()   # enlève le retour à la ligne final
fichier.close()
```

Construire la liste `programme` des lignes. Pour chaque ligne, savoir distinguer `noop` de `addx` et récupérer l’entier (éventuellement négatif) qui suit `addx`.

??? pouce "Coup de pouce"

    `ligne.split()` donne `["addx", "-2"]` ; `int("-2")` vaut bien `-2`.

### <span class="exo-num">Exercice 4</span> — L’historique du registre <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-aoc-1-4 }

Écrire une fonction `valeurs_pendant(programme)` qui renvoie la liste des valeurs de `X` pendant chaque cycle : l’élément d’indice `0` correspond au cycle 1. Sur l’exemple, on doit obtenir `[1, 1, 1, 5, 5, 3, 3, 3, 8, 8]`.

??? pouce "Coup de pouce"

    Pour `noop`, ajouter une fois la valeur actuelle de `X` à la liste ; pour `addx`, l’ajouter **deux** fois, et seulement ensuite modifier `X`.

??? pouce "Coup de pouce 2 (début de solution)"

    `X = 1`, `valeurs = []` ; `for ligne in programme:` si c’est `noop`, `valeurs.append(X)` ; sinon deux `append(X)` puis `X += int(...)`.

### <span class="exo-num">Exercice 5</span> — L’intensité du signal <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-aoc-1-5 }

Avec cette liste, calculer la réponse de la partie 1. Attention au décalage entre numéro de cycle et indice dans la liste.

??? pouce "Coup de pouce"

    La valeur pendant le cycle `c` est `valeurs[c - 1]`. Les cycles demandés se suivent de 40 en 40 : `range(20, 221, 40)`.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    On découvre que `X` commande en fait la position d’un motif sur l’écran. L’écran fait 40 pixels de large sur 6 lignes et se dessine pendant les cycles, un pixel par cycle, de gauche à droite puis ligne par ligne (le cycle 1 dessine la colonne 0, le cycle 41 recommence au début de la ligne suivante). Le motif fait 3 pixels de large, centré sur la colonne `X`. Le pixel dessiné est allumé si sa colonne est l’une des trois du motif. Réponse : les 8 lettres majuscules lues à l’écran.

### <span class="exo-num">Exercice 6</span> — Dessiner l’écran <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-aoc-1-6 }

Lire attentivement comment l’écran est balayé (combien de pixels par ligne, combien de lignes) et à quelle condition un pixel est allumé. Construire l’image ligne par ligne sous forme de chaînes de caractères (par exemple `"#"` pour allumé et `"."` pour éteint), l’afficher, et lire les lettres majuscules qui apparaissent : c’est la réponse.

??? pouce "Coup de pouce"

    Réutiliser la liste de la partie 1 : pour le cycle numéro `c`, la colonne du pixel dessiné est `(c - 1) % 40`. Comparer cette colonne à la valeur de `X` pendant ce cycle.

??? pouce "Coup de pouce 2 (début de solution)"

    Le pixel est allumé si l’écart entre la colonne et `X` vaut au plus 1 : `abs(colonne - X) <= 1`. Ajouter le caractère à une chaîne `ligne_ecran` et l’afficher (puis la vider) tous les 40 cycles.

## Approfondissement

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : un vrai petit processeur <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-aoc-1-7 }

On ajoute un second registre `Y`, qui vaut 0 au départ, et deux instructions inventées : `addy n` (2 cycles, ajoute `n` à `Y` à la fin) et `copy` (1 cycle, copie `X` dans `Y`).

1.  À la main : écrire les valeurs de `(X, Y)` pendant chaque cycle du programme `addx 4`, `copy`, `addy 3`, `noop`.

2.  Écrire `historique(programme)` qui renvoie la liste des couples `(X, Y)` pendant chaque cycle, et comparer avec la question 1.

    ??? pouce "Coup de pouce"

        Une fonction `duree(nom)` qui renvoie le nombre de cycles d’une instruction (avec des `if`) permet d’écrire une seule boucle d’ajout pour toutes les instructions.

3.  Quelle structure de données serait pratique pour associer à chaque instruction sa durée ?
