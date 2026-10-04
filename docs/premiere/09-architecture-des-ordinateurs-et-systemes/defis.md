# Défis Advent of Code

<p class="sous-titre">Architecture des ordinateurs et systèmes d'exploitation</p>

## <span class="etiquette">Défi 1</span> Rucksack Reorganization

*ranger les sacs à dos — moitiés de chaîne, caractère commun, ord()*

<p class="infos-activite">Jour 3</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/09-defi-aoc-2022-03){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-09-defi-aoc-2022-03.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2022/day/3 ](https://adventofcode.com/2022/day/3 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (facultatif), le lien *get your puzzle input* donne **vos** données, à enregistrer sous `input.txt` à côté du programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/09-defi-aoc-2022-03>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|              |                 |             |                     |
|:-------------|:----------------|:------------|:--------------------|
| rucksack     | sac à dos       | compartment | compartiment, poche |
| item type    | type d’objet    | half        | moitié              |
| lowercase    | minuscule       | uppercase   | majuscule           |
| both         | les deux        | priority    | priorité            |
| to appear in | apparaître dans | to fail to  | ne pas réussir à    |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Un elfe a rempli les sacs à dos de l’expédition, mais n’a pas bien respecté la consigne. Chaque sac a deux poches de même taille, et chaque type d’objet aurait dû se trouver dans une seule des deux poches. Dans chaque sac, il y a exactement un type d’objet mal rangé, et il faut le retrouver.

    **Ce qu’il faut faire.**

    - Chaque ligne décrit un sac : une chaîne de lettres de longueur paire, où chaque lettre est un type d’objet (`a` et `A` sont des types différents).

    - La première moitié de la chaîne est le contenu de la première poche, la seconde moitié celui de la seconde.

    - Exactement une lettre apparaît dans les deux moitiés (elle peut y apparaître plusieurs fois) : c’est l’objet mal rangé.

    - Chaque lettre a une priorité : `a` à `z` valent 1 à 26, `A` à `Z` valent 27 à 52. La réponse est la somme des priorités des lettres communes, une par sac.

### <span class="exo-num">Exercice 1</span> — Vérifier sa compréhension <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-aoc-1-1 }

Questions pièges, à traiter sur le cahier :

1.  Si la lettre commune apparaît deux fois dans une moitié, combien de fois ajoute-t-on sa priorité ?

2.  Quelles sont les priorités de `m` et de `M` ?

3.  Pour une ligne de 10 caractères, quels sont les indices de la seconde moitié ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-aoc-1-2 }

On considère les sacs (inventés) suivants :

```console
abcDxyzD
Dqrsmnqo
tuDvwvke
PgHjPlmn
JgkFhFiw
bgceLbtd
```

Pour chaque sac, couper la ligne en deux, trouver le caractère commun et sa priorité. Vérification : on doit trouver `30`, `17`, `22`, `42`, `32`, `2`, soit un total de `145`.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Deux moitiés <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-aoc-1-3 }

Pour une chaîne `s` de longueur paire, que donnent `s[:len(s) // 2]` et `s[len(s) // 2:]` ? Tester avec `"abcDxyzD"`.

### <span class="exo-num">Exercice 4</span> — Le caractère commun <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-aoc-1-4 }

Écrire une fonction `commun(s1, s2)` qui renvoie un caractère présent à la fois dans `s1` et dans `s2`.

??? pouce "Coup de pouce"

    Parcourir les caractères de `s1` ; le test `c in s2` dit si `c` est aussi dans `s2`. Dès qu’on en trouve un, le renvoyer.

!!! encadre "Rappel : codes des caractères (ord, chr) ; outil : islower"

    On a vu au chapitre sur le binaire que chaque caractère a un code (ASCII) : `ord` donne le code d’un caractère, `chr` fait l’inverse ; les lettres de `a` à `z` ont des codes consécutifs, de même que celles de `A` à `Z`. Nouvel outil : la méthode `islower` dit si un caractère est une minuscule.

    ```python
    print(ord("a"), ord("A"))    # 97 65
    print("q".islower())         # True
    print("Q".islower())         # False
    ```

    Question : que vaut `ord("z") - ord("a")` ? Et `chr(ord("a") + 2)` ?

### <span class="exo-num">Exercice 5</span> — La priorité <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-aoc-1-5 }

La fonction `ord` donne le code d’un caractère : afficher `ord("a")`, `ord("b")`, `ord("A")`. Écrire une fonction `priorite(c)` qui renvoie la priorité d’un caractère, puis répondre à la partie 1 sur l’exemple et sur vos données.

??? pouce "Coup de pouce"

    Les minuscules ont des codes consécutifs, les majuscules aussi. Pour une minuscule, `ord(c) - ord("a")` vaut 0 pour `a`, 1 pour `b`… Que faut-il ajouter ? Le test `c.islower()` dit si `c` est une minuscule.

??? pouce "Coup de pouce 2 (début de solution)"

    Pour une minuscule : `ord(c) - ord("a") + 1`. Pour une majuscule, même idée avec `ord("A")`, en ajoutant de quoi commencer à la bonne valeur. Vérifier avec `a`, `z`, `A` et `Z`.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Les elfes voyagent en groupes de trois, et chaque groupe porte un badge, le seul type d’objet commun à leurs trois sacs. Les lignes forment donc des groupes de **trois lignes consécutives** ; dans chaque groupe, une seule lettre est présente dans les trois lignes. La réponse est la somme des priorités de ces lettres, une par groupe.

### <span class="exo-num">Exercice 6</span> — Par groupes de trois <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-aoc-1-6 }

La suite de l’énoncé regroupe les lignes trois par trois. Écrire une fonction `commun3(s1, s2, s3)`, puis répondre à la partie 2. Sur l’exemple de la fiche, on doit trouver `37`.

??? pouce "Coup de pouce"

    Lire d’abord toutes les lignes dans une liste `sacs`, puis parcourir les indices de 3 en 3 : `for i in range(0, len(sacs), 3):` ; le groupe est formé de `sacs[i]`, `sacs[i + 1]` et `sacs[i + 2]`.

??? pouce "Coup de pouce 2 (début de solution)"

    `commun3` : parcourir les caractères de `s1` et renvoyer le premier `c` tel que `c in s2 and c in s3`.

## Approfondissement

!!! encadre "Outil Python : les ensembles (set)"

    Un **ensemble** est une collection **sans doublon** et **sans ordre**. L’opérateur `&` donne l’**intersection** de deux ensembles : les éléments présents dans les deux.

    ```python
    e = set("abca")           # {'a', 'b', 'c'} : les doublons disparaissent
    f = set("cde")
    print(e & f)              # {'c'} : elements communs
    print("b" in e)           # True
    print(len(e))             # 3
    g = e & f
    print(g.pop())            # c : pop retire et renvoie un element
    ```

    **Intérêt.** Le test `x in ensemble` est quasi instantané, alors que `x in chaine` parcourt la chaîne. Question : que donne `set("abc") & set("xyz")` ?

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : avec des ensembles <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-aoc-1-7 }

1.  Sur le premier sac de l’exemple, écrire à la main `set("abcD")`, `set("xyzD")` et leur intersection.

2.  Réécrire `commun` et `commun3` avec l’opérateur `&`.

    ??? pouce "Coup de pouce"

        L’intersection ne contient qu’un élément ; pour le récupérer, on peut écrire `e.pop()`.

3.  Comparer le nombre de comparaisons de `commun` (deux boucles cachées : `for` et `in`) et de la version avec ensembles, pour des chaînes de longueur $k$.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Approfondissement 2 : la priorité sans `ord` <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-aoc-1-8 }

On peut aussi trouver la priorité en cherchant la lettre dans une chaîne `ALPHABET` qui contient les 26 minuscules puis les 26 majuscules, dans l’ordre.

1.  À quel indice de `ALPHABET` se trouve `a` ? `A` ? Quel lien avec la priorité ?

2.  Écrire `priorite_alphabet(c)` avec une boucle sur les indices de `ALPHABET`, et vérifier qu’elle donne les mêmes résultats que `priorite` pour les 52 lettres.

    ??? pouce "Coup de pouce"

        Parcourir `range(len(ALPHABET))` et renvoyer `i + 1` dès que `ALPHABET[i]` vaut `c`.

3.  Laquelle des deux fonctions fait le moins de calculs ?

## <span class="etiquette">Défi 2</span> Cathode-Ray Tube

*l’écran du communicateur — simuler un petit processeur*

<p class="infos-activite">Jour 10</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/09-defi-aoc-2022-10){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-09-defi-aoc-2022-10.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2022/day/10 ](https://adventofcode.com/2022/day/10 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/09-defi-aoc-2022-10>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

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

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-aoc-2-1 }

Après lecture du résumé (et de l’énoncé), vérifier sa compréhension sur ces cas particuliers :

1.  Pendant les deux cycles d’un `addx 3`, `X` a-t-il déjà augmenté ?

2.  Si l’on calcule `X` *après* le cycle 20 au lieu de *pendant*, quelle erreur commet-on ?

3.  Combien de cycles dure un programme de 5 `noop` et 5 `addx` ?

!!! encadre "Lien avec le cours : l’architecture de von Neumann"

    Ce petit processeur ressemble à celui du chapitre sur l’architecture : une **horloge** cadence le travail, le programme est une suite d’instructions exécutées l’une après l’autre, et un **registre** (ici `X`) garde une valeur que les instructions modifient. Certaines instructions demandent plus de cycles que d’autres, comme dans un vrai processeur.

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-aoc-2-2 }

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

### <span class="exo-num">Exercice 3</span> — Lire le programme <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-aoc-2-3 }

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

### <span class="exo-num">Exercice 4</span> — L’historique du registre <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-aoc-2-4 }

Écrire une fonction `valeurs_pendant(programme)` qui renvoie la liste des valeurs de `X` pendant chaque cycle : l’élément d’indice `0` correspond au cycle 1. Sur l’exemple, on doit obtenir `[1, 1, 1, 5, 5, 3, 3, 3, 8, 8]`.

??? pouce "Coup de pouce"

    Pour `noop`, ajouter une fois la valeur actuelle de `X` à la liste ; pour `addx`, l’ajouter **deux** fois, et seulement ensuite modifier `X`.

??? pouce "Coup de pouce 2 (début de solution)"

    `X = 1`, `valeurs = []` ; `for ligne in programme:` si c’est `noop`, `valeurs.append(X)` ; sinon deux `append(X)` puis `X += int(...)`.

### <span class="exo-num">Exercice 5</span> — L’intensité du signal <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-aoc-2-5 }

Avec cette liste, calculer la réponse de la partie 1. Attention au décalage entre numéro de cycle et indice dans la liste.

??? pouce "Coup de pouce"

    La valeur pendant le cycle `c` est `valeurs[c - 1]`. Les cycles demandés se suivent de 40 en 40 : `range(20, 221, 40)`.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    On découvre que `X` commande en fait la position d’un motif sur l’écran. L’écran fait 40 pixels de large sur 6 lignes et se dessine pendant les cycles, un pixel par cycle, de gauche à droite puis ligne par ligne (le cycle 1 dessine la colonne 0, le cycle 41 recommence au début de la ligne suivante). Le motif fait 3 pixels de large, centré sur la colonne `X`. Le pixel dessiné est allumé si sa colonne est l’une des trois du motif. Réponse : les 8 lettres majuscules lues à l’écran.

### <span class="exo-num">Exercice 6</span> — Dessiner l’écran <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-aoc-2-6 }

Lire attentivement comment l’écran est balayé (combien de pixels par ligne, combien de lignes) et à quelle condition un pixel est allumé. Construire l’image ligne par ligne sous forme de chaînes de caractères (par exemple `"#"` pour allumé et `"."` pour éteint), l’afficher, et lire les lettres majuscules qui apparaissent : c’est la réponse.

??? pouce "Coup de pouce"

    Réutiliser la liste de la partie 1 : pour le cycle numéro `c`, la colonne du pixel dessiné est `(c - 1) % 40`. Comparer cette colonne à la valeur de `X` pendant ce cycle.

??? pouce "Coup de pouce 2 (début de solution)"

    Le pixel est allumé si l’écart entre la colonne et `X` vaut au plus 1 : `abs(colonne - X) <= 1`. Ajouter le caractère à une chaîne `ligne_ecran` et l’afficher (puis la vider) tous les 40 cycles.

## Approfondissement

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : un vrai petit processeur <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-aoc-2-7 }

On ajoute un second registre `Y`, qui vaut 0 au départ, et deux instructions inventées : `addy n` (2 cycles, ajoute `n` à `Y` à la fin) et `copy` (1 cycle, copie `X` dans `Y`).

1.  À la main : écrire les valeurs de `(X, Y)` pendant chaque cycle du programme `addx 4`, `copy`, `addy 3`, `noop`.

2.  Écrire `historique(programme)` qui renvoie la liste des couples `(X, Y)` pendant chaque cycle, et comparer avec la question 1.

    ??? pouce "Coup de pouce"

        Une fonction `duree(nom)` qui renvoie le nombre de cycles d’une instruction (avec des `if`) permet d’écrire une seule boucle d’ajout pour toutes les instructions.

3.  Quelle structure de données serait pratique pour associer à chaque instruction sa durée ?
