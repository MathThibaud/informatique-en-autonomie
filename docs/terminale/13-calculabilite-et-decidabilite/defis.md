# Défis Advent of Code

<p class="sous-titre">Calculabilité et décidabilité</p>

## <span class="etiquette">Défi 1</span> Handheld Halting

*la console bloquée — interpréteur et problème de l’arrêt*

<p class="infos-activite">Jour 8</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/13-defi-aoc-2020-08){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-13-defi-aoc-2020-08.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/8 ](https://adventofcode.com/2020/day/8 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/13-defi-aoc-2020-08>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

*Ce défi illustre le problème de l’arrêt vu dans ce chapitre : on y détecte une boucle infinie, ce qui n’est possible ici que parce que la machine a un nombre fini d’états.*

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|                      |                        |             |              |
|:---------------------|:-----------------------|:------------|:-------------|
| boot code            | programme de démarrage | instruction | instruction  |
| operation / argument | opération / argument   | accumulator | accumulateur |
| jump                 | saut                   | offset      | décalage     |
| infinite loop        | boucle infinie         | terminate   | se terminer  |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** En plein vol, un enfant assis à côté du héros n’arrive plus à démarrer sa console de jeu portable : son programme de démarrage tourne en rond. Le fichier contient ce programme, écrit dans un langage très simple, avec une instruction par ligne. La machine ne possède qu’une seule mémoire, l’*accumulateur*, qui vaut 0 au départ.

    **Ce qu’il faut faire.**

    - Une instruction est formée d’une opération (`acc`, `jmp` ou `nop`) et d’un entier signé (`+4`, `-20`).

    - `acc n` ajoute `n` à l’accumulateur, puis passe à la ligne suivante.

    - `jmp n` est un saut de `n` lignes compté à partir de l’instruction courante : `jmp +1` va à la ligne suivante, `jmp -2` remonte de deux lignes.

    - `nop n` ne fait rien (l’argument est ignoré) et passe à la ligne suivante.

    - On commence à la première ligne. Le programme finit par boucler : dès qu’une instruction est sur le point d’être exécutée une deuxième fois, on s’arrête **avant** de l’exécuter. Il faut renvoyer la valeur de l’accumulateur à ce moment.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-13-calculabilite-et-decidabilite-aoc-1-1 }

Après lecture de l’énoncé et du résumé, vérifier sa compréhension :

1.  Que fait l’instruction `jmp +0` ? Et `nop -5` ?

2.  Si l’instruction qui revient est un `acc`, son ajout est-il compté une seconde fois ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-13-calculabilite-et-decidabilite-aoc-1-2 }

```console
acc +2
jmp +3
acc +10
jmp +3
nop -2
acc -4
jmp -4
acc +7
```

On considère le programme (inventé) suivant, dont les lignes sont numérotées à partir de 0.

Exécuter le programme à la main dans un tableau à trois colonnes : numéro de ligne, instruction, accumulateur après l’instruction. Vérification : on doit trouver `8`.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire le programme <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-13-calculabilite-et-decidabilite-aoc-1-3 }

Construire la liste `programme` de tuples `(operation, argument)`, l’argument étant un entier. Par exemple la ligne `jmp -4` donne `("jmp", -4)`.

??? pouce "Coup de pouce"

    `int("+3")` et `int("-4")` fonctionnent directement : pas besoin de traiter le signe à part.

!!! encadre "Outil Python : les ensembles (set)"

    Un **ensemble** est une collection **sans doublon** et **sans ordre** : on ne peut pas y accéder par un indice, on peut seulement ajouter, retirer, et demander si un élément y est. Python sait aussi calculer l’union, l’intersection et la différence de deux ensembles.

    ```python
    vus = set()              # ensemble vide (attention : {} est un dictionnaire vide)
    vus.add(5)               # ajout ; ajouter une valeur deja presente ne change rien
    vus.add(8)
    print(8 in vus)          # True : test d'appartenance
    print(len(vus))          # 2
    a = {1, 2, 3}            # ensemble ecrit directement
    b = set([2, 3, 4, 4])    # a partir d'une liste : {2, 3, 4}
    print(a | b)             # union : {1, 2, 3, 4}
    print(a & b)             # intersection : {2, 3}
    print(a - b)             # difference : {1}
    ```

    **Intérêt.** Avec une liste, `x in liste` compare `x` à chaque élément l’un après l’autre : jusqu’à $n$ comparaisons. Un ensemble range ses éléments selon une valeur calculée à partir d’eux (une *fonction de hachage*, comme les clés d’un dictionnaire) : Python va directement là où `x` devrait se trouver. Le test `x in ensemble` prend donc un temps qui ne dépend pas du nombre d’éléments (**temps constant**, en moyenne).

    **À essayer.** Que vaut `len(vus)` après `vus = {1, 2}` puis `vus.add(2)` ?

### <span class="exo-num">Exercice 4</span> — Un interpréteur <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-13-calculabilite-et-decidabilite-aoc-1-4 }

Écrire une fonction `executer(programme)` qui simule la machine : une variable `acc`, une variable `ip` (numéro de l’instruction courante), et une boucle qui exécute une instruction par tour. La fonction s’arrête dès qu’une instruction s’apprête à être exécutée pour la deuxième fois et renvoie `acc`. Tester sur l’exemple de la fiche, puis sur vos données.

??? pouce "Coup de pouce"

    Garder dans un ensemble `deja_vues` les numéros des instructions exécutées. La condition de la boucle `while` porte sur `ip`.

!!! encadre "Le problème de l’arrêt : rappel du cours"

    Peut-on écrire un programme `arret(P, x)` qui dirait, pour **tout** programme `P` et toute entrée `x`, si `P` finit par s’arrêter sur `x` ? Turing a démontré en 1936 que non : ce problème est *indécidable*. On le prouve par l’absurde, en construisant un programme qui fait le contraire de ce que `arret` prédit pour lui-même.

    Pourquoi la détection réussit-elle ici ? Parce que la machine de l’énigme a un état **fini** : l’état ne dépend que de `ip`, et l’accumulateur n’influence jamais la suite des instructions. Si une instruction revient, tout se répète à l’identique. Un programme quelconque peut, lui, utiliser une mémoire non bornée sans jamais repasser par le même état.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Il faut maintenant réparer la console pour que le programme aille jusqu’au bout.

    - Exactement une instruction est fautive : un `jmp` devrait être un `nop`, ou un `nop` un `jmp`. Les `acc` sont corrects.

    - Le programme réparé se termine, c’est-à-dire qu’il cherche à exécuter la ligne qui suit immédiatement la dernière. Il faut renvoyer la valeur de l’accumulateur à ce moment.

!!! encadre "Outil Python : copier une liste (copy)"

    Écrire `b = a` ne copie pas la liste : `a` et `b` désignent la **même** liste, et modifier l’une modifie « l’autre ». La méthode `copy` (ou la tranche `a[:]`) fabrique une nouvelle liste contenant les mêmes éléments.

    ```python
    a = [1, 2, 3]
    b = a              # meme liste, deux noms
    b[0] = 9
    print(a)           # [9, 2, 3] : a a change aussi !
    c = a.copy()       # vraie copie (comme a[:])
    c[0] = 0
    print(a, c)        # [9, 2, 3] [0, 2, 3]
    ```

    **Intérêt.** Chaque essai de la partie 2 part d’un programme intact. Une copie coûte un temps proportionnel à la longueur de la liste.

    **À essayer.** Avec `a = [[1], [2]]` et `c = a.copy()`, que devient `a` après `c[0].append(5)` ? Pourquoi n’est-ce pas un problème pour une liste de tuples ?

### <span class="exo-num">Exercice 5</span> — Réparer le programme <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-13-calculabilite-et-decidabilite-aoc-1-5 }

1.  Modifier `executer` pour qu’elle renvoie aussi un booléen indiquant si le programme s’est terminé normalement. Quelle condition sur `ip` signale une fin normale ?

2.  Essayer toutes les modifications autorisées par l’énoncé, une à une, jusqu’à trouver celle qui fait terminer le programme. Sur l’exemple de la fiche, on doit obtenir `5`.

??? pouce "Coup de pouce"

    Chaque essai doit partir du programme **d’origine** : si l’on modifie la liste sans la recopier, les modifications s’accumulent d’un essai à l’autre.

??? pouce "Coup de pouce 2 (début de solution)"

    `copie = programme.copy()`, puis on remplace un seul tuple de `copie`. Inutile d’essayer les lignes `acc`.

## Approfondissement

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 6</span> — Défi : combien d’exécutions ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-13-calculabilite-et-decidabilite-aoc-1-6 }

Pour un programme de $n$ instructions, combien d’instructions la méthode précédente exécute-t-elle au pire ? Proposer et tester une idée pour réduire le nombre d’essais.

??? pouce "Coup de pouce"

    Modifier une instruction jamais atteinte par l’exécution de la partie 1 ne change rien.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : une réparation en temps linéaire <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-13-calculabilite-et-decidabilite-aoc-1-7 }

On note $n$ le nombre de lignes et $\mathrm{succ}(k)$ la ligne exécutée juste après la ligne $k$ ; la valeur $n$ représente la fin du programme.

1.  Sur l’exemple de la fiche, donner $\mathrm{succ}(k)$ pour $k$ de $0$ à $7$.

2.  Quelles lignes mènent, sans modification, jusqu’à la fin $8$ ? On les trouve en **remontant** les flèches depuis $8$.

3.  Parmi les lignes atteintes lors de l’exécution de la partie 1, laquelle, une fois échangée (`jmp` et `nop`), envoie vers une ligne trouvée à la question 2 ?

4.  Écrire `reparer_lineaire(programme)` qui applique cette méthode et renvoie l’accumulateur du programme réparé. Quelle est sa complexité ?

??? pouce "Coup de pouce"

    Construire le graphe inverse : un dictionnaire qui associe à chaque ligne $s$ la liste des lignes $k$ telles que $\mathrm{succ}(k) = s$. Un parcours (avec une pile) depuis $n$ donne l’ensemble `vers_fin`.

??? pouce "Coup de pouce 2 (début de solution)"

    Une seule exécution réparée suffit à la fin. Pourquoi est-on sûr qu’elle se termine ? Si la ligne $k$ modifiée était sur le chemin de la nouvelle ligne vers la fin, $k$ serait dans `vers_fin`, et le programme d’origine se terminerait.

## <span class="etiquette">Défi 2</span> Conway Cubes

*les cubes de Conway — ensembles et simulation en 3D puis 4D*

<p class="infos-activite">Jour 17</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/13-defi-aoc-2020-17){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-13-defi-aoc-2020-17.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/17 ](https://adventofcode.com/2020/day/17 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/13-defi-aoc-2020-17>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

*Ce défi est une variante en trois dimensions du jeu de la vie de Conway, dont la version plane est un exemple célèbre de système Turing-complet, notion vue dans ce chapitre.*

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|          |                             |                   |                 |
|:---------|:----------------------------|:------------------|:----------------|
| cube     | cube (une case de l’espace) | active / inactive | actif / inactif |
| neighbor | voisin                      | coordinate        | coordonnée      |
| cycle    | cycle, étape                | simultaneously    | en même temps   |
| slice    | tranche, coupe              | boot up           | démarrer        |
| infinite | infini                      | dimension         | dimension       |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Les elfes vous demandent de l’aide pour une source d’énergie expérimentale : une grille infinie de cubes, chacun actif ou inactif, qui évolue par cycles selon l’état de ses voisins. C’est une version en trois dimensions du célèbre *jeu de la vie* de Conway. Le fichier donne l’état d’une petite zone plate au départ.

    **Ce qu’il faut faire.**

    - Le fichier est une grille de `#` (actif) et de `.` (inactif). C’est la tranche $z = 0$ de l’espace : le caractère de la ligne $y$, colonne $x$, donne l’état du cube $(x, y, 0)$. Tous les autres cubes de l’espace sont inactifs.

    - Les voisins d’un cube sont les 26 cubes dont chaque coordonnée diffère d’au plus 1 de la sienne : les cubes qui le touchent par une face, une arête ou un coin.

    - À chaque cycle, tous les cubes changent en même temps. Un cube actif reste actif s’il a exactement 2 ou 3 voisins actifs, sinon il s’éteint. Un cube inactif s’allume s’il a exactement 3 voisins actifs.

    - La réponse est le nombre de cubes actifs après 6 cycles.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-13-calculabilite-et-decidabilite-aoc-2-1 }

Questions de vérification, à traiter sur le cahier :

1.  Le cube $(0, 0, 0)$ est-il voisin de $(1, 1, -1)$ ? De $(2, 0, 0)$ ?

2.  Un cube actif qui a 4 voisins actifs reste-t-il actif ? Un cube inactif qui en a 2 devient-il actif ?

3.  Un cube situé en dehors de la grille de départ peut-il devenir actif ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-13-calculabilite-et-decidabilite-aoc-2-2 }

On considère l’état initial (inventé) suivant, dans le plan $z = 0$ :

```console
#.#
.##
#..
```

Combien de cubes actifs au départ ? Compter les voisins actifs du cube central $(1, 1, 0)$ et dire s’il reste actif. Vérification : après un cycle, il y a `12` cubes actifs ; après six cycles, `138`.

## Programmer la partie 1

!!! encadre "Outil Python : les ensembles de tuples (set)"

    Un **ensemble** est une collection **sans doublon** et **sans ordre** : pas d’indice, on peut seulement ajouter, retirer et tester l’appartenance. Ses éléments doivent être non modifiables : des nombres, des chaînes ou des **tuples**, mais pas des listes.

    ```python
    actifs = set()                # ensemble vide (attention : {} est un dictionnaire)
    actifs.add((0, 1, 0))
    actifs.add((2, 0, 0))
    actifs.add((0, 1, 0))         # deja present : rien ne change
    print(len(actifs))            # 2
    print((2, 0, 0) in actifs)    # True
    print((5, 5, 5) in actifs)    # False : un cube absent est inactif
    ligne = {(x, 0, 0) for x in range(3)}   # ensemble en comprehension
    print(actifs & ligne)         # {(2, 0, 0)} : cubes communs aux deux ensembles
    ```

    **Intérêt.** On ne stocke que les cubes actifs, où qu’ils soient dans l’espace infini, et le test `cube in actifs` prend un temps constant (en moyenne), comme pour les clés d’un dictionnaire.

    **À essayer.** Essayer `actifs.add([1, 2, 3])` : que se passe-t-il ? Pourquoi utilise-t-on des tuples ?

### <span class="exo-num">Exercice 3</span> — Un ensemble de tuples <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-13-calculabilite-et-decidabilite-aoc-2-3 }

L’espace est infini : pas de liste de listes. Écrire une fonction `lire_actifs(nom_fichier)` qui renvoie l’**ensemble** des coordonnées `(x, y, 0)` des cubes actifs. Vérifier qu’on obtient 5 éléments sur l’exemple.

??? pouce "Coup de pouce"

    Un `set` de tuples : l’appartenance `(x, y, z) in actifs` se teste en temps quasi constant, et un cube inactif n’est tout simplement pas dans l’ensemble.

!!! encadre "Outil Python : itertools.product"

    `product(valeurs, repeat=d)` énumère tous les tuples de longueur `d` dont chaque élément est pris dans `valeurs` : c’est l’équivalent de `d` boucles imbriquées.

    ```python
    from itertools import product

    for d in product((-1, 0, 1), repeat=2):    # tous les couples de -1, 0, 1
        print(d)                               # (-1, -1), (-1, 0), ..., (1, 1)
    print(len([t for t in product("ab", repeat=3)]))  # 8 : 2 ** 3 triplets
    ```

    **Intérêt.** Le nombre de boucles devient un **paramètre** : le même code sert en dimension 3, 4 ou plus.

    **À essayer.** Combien de tuples produit `product((-1, 0, 1), repeat=4)` ? Lequel faut-il retirer pour obtenir les décalages vers les voisins ?

### <span class="exo-num">Exercice 4</span> — Les voisins <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-13-calculabilite-et-decidabilite-aoc-2-4 }

Écrire une fonction `voisins(cube)` qui renvoie la liste des 26 voisins d’un cube. La tester sur `(0, 0, 0)`.

??? pouce "Coup de pouce"

    Trois boucles imbriquées sur les décalages dans `[-1, 0, 1]`, en excluant le décalage nul.

### <span class="exo-num">Exercice 5</span> — Un cycle <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-13-calculabilite-et-decidabilite-aoc-2-5 }

Écrire une fonction `cycle(actifs)` qui renvoie le **nouvel** ensemble des cubes actifs. Quels cubes faut-il examiner ? Pas seulement les cubes actifs : la zone active grandit à chaque cycle. Simuler six cycles sur l’exemple de la fiche, puis sur vos données.

??? pouce "Coup de pouce"

    Seul un cube voisin d’au moins un cube actif peut être actif après le cycle. Les cubes à examiner sont donc les cubes actifs et leurs voisins.

??? pouce "Coup de pouce 2 (début de solution)"

    Plus efficace : parcourir les cubes actifs et, pour chacun de leurs voisins, ajouter 1 dans un dictionnaire `compte`. On applique ensuite les règles à chaque clé de `compte` ; un cube actif absent de `compte` n’a aucun voisin actif.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Mauvaise surprise : la source d’énergie fonctionne en réalité dans un espace à quatre dimensions.

    - Même simulation avec des points $(x, y, z, w)$ : l’état initial est dans le plan $z = w = 0$, et les voisins sont définis de la même façon (chaque coordonnée diffère d’au plus 1).

    - La réponse est le nombre de cubes actifs après 6 cycles.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Une dimension de plus <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-13-calculabilite-et-decidabilite-aoc-2-6 }

Combien de voisins un point a-t-il en dimension 4 ? Si votre code est bien écrit, peu de choses changent : adapter `lire_actifs` et `voisins`. Sur l’exemple de la fiche, on doit trouver `36` cubes actifs après un cycle et `680` après six cycles.

??? pouce "Coup de pouce"

    En dimension $d$, un point a $3^d - 1$ voisins.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Défi : un code pour toutes les dimensions <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-13-calculabilite-et-decidabilite-aoc-2-7 }

Écrire `voisins(point)` pour un tuple de longueur quelconque, sans écrire une boucle par dimension, et une fonction `simuler(grille, dimension, nb_cycles)` qui sert aux deux parties. Que donne la dimension 2 ? Et la dimension 5 sur l’exemple (mesurer le temps) ?

??? pouce "Coup de pouce"

    Utiliser `itertools.product` (voir l’encadré), ou la fonction récursive de l’approfondissement 1.

## Approfondissement

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Approfondissement 1 : les décalages sans `itertools` <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-13-calculabilite-et-decidabilite-aoc-2-8 }

On veut construire soi-même la liste des décalages, par récursivité.

1.  Lister à la main les tuples de longueur 1 formés de $-1$, $0$, $1$, puis ceux de longueur 2, obtenus en plaçant $-1$, $0$ ou $1$ devant chacun des précédents. Combien y en a-t-il en longueur $d$ ?

2.  Écrire une fonction récursive `decalages_rec(dimension)` qui renvoie les $3^d$ tuples, le tuple nul compris. Le cas de base est la dimension 0, qui renvoie `[()]` (une liste contenant le tuple vide).

    ??? pouce "Coup de pouce"

        `(-1,)` est un tuple à un seul élément (la virgule est obligatoire), et `(-1,) + (0, 1)` vaut `(-1, 0, 1)`.

    ??? pouce "Coup de pouce 2 (début de solution)"

        Pour chaque `debut` dans `(-1, 0, 1)` et chaque `fin` de `decalages_rec(dimension - 1)`, ajouter `(debut,) + fin` au résultat.

3.  Vérifier qu’une fois le tuple nul retiré, on obtient les mêmes décalages qu’avec `product` en dimension 3 et 4, puis l’utiliser dans `simuler`.

4.  Combien d’appels récursifs fait `decalages_rec(d)` ? Combien de voisins un point a-t-il en dimension 5 ?
