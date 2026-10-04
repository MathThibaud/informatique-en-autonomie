# Défis Advent of Code

<p class="sous-titre">Les $k$k plus proches voisins</p>

## <span class="etiquette">Défi 1</span> Hydrothermal Venture

*les cheminées sous-marines — segments sur une grille*

<p class="infos-activite">Jour 5</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/12-defi-aoc-2021-05){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-12-defi-aoc-2021-05.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2021/day/5 ](https://adventofcode.com/2021/day/5 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/12-defi-aoc-2021-05>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|          |                  |                       |                       |
|:---------|:-----------------|:----------------------|:----------------------|
| vent     | cheminée, source | line segment          | segment               |
| endpoint | extrémité        | horizontal / vertical | horizontal / vertical |
| overlap  | se superposer    | at least two          | au moins deux         |
| diagonal | diagonale        | 45 degrees            | 45 degrés             |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Au fond de l’océan, le sous-marin longe des champs de cheminées hydrothermales qui forment des lignes droites et dégagent des nuages dangereux. Le fichier décrit ces lignes de cheminées, une par ligne, par leurs deux extrémités. Il faut repérer les endroits où plusieurs lignes se croisent, pour les éviter.

    **Ce qu’il faut faire.**

    - Chaque ligne a la forme `x1,y1 -> x2,y2` : un segment sur une grille, extrémités **comprises** ; $x$ est la colonne, $y$ la ligne.

    - Pour la partie 1, on ne prend en compte que les segments **horizontaux** ($y_1 = y_2$) ou **verticaux** ($x_1 = x_2$) ; les autres sont ignorés.

    - Une case est dangereuse si au moins **deux** segments la couvrent.

    - Réponse : le nombre de cases dangereuses.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-les-k-k-plus-proches-voisins-aoc-1-1 }

Après lecture du résumé (et de l’énoncé), vérifier sa compréhension sur ces cas particuliers :

1.  Un segment peut-il être écrit « à l’envers », avec `x2 < x1` ? Qu’est-ce que cela change pour `range` ?

2.  Une case couverte par trois segments compte-t-elle pour 1 ou pour 2 ?

3.  Un segment réduit à un point (`3,3 -> 3,3`) est-il horizontal, vertical, les deux ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-les-k-k-plus-proches-voisins-aoc-1-2 }

On considère le fichier (inventé) suivant :

```console
0,1 -> 5,1
2,0 -> 2,4
4,4 -> 4,0
0,0 -> 4,4
5,5 -> 1,1
3,1 -> 6,1
```

Dessiner une grille de $7 \times 7$ cases ($x$ de gauche à droite, $y$ de haut en bas), puis écrire dans chaque case le nombre de segments de la partie 1 qui la couvrent. Vérification : on doit obtenir `4`.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire les segments <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-les-k-k-plus-proches-voisins-aoc-1-3 }

Rappel pour lire un fichier ligne par ligne :

```python
fichier = open("input.txt", encoding="utf-8")
for ligne in fichier:
    ligne = ligne.strip()   # enlève le retour à la ligne final
fichier.close()
```

Écrire une fonction `lire_segment(ligne)` qui renvoie le quadruplet d’entiers `(x1, y1, x2, y2)`. Construire la liste `segments`, puis chercher la plus grande coordonnée présente dans vos données.

??? pouce "Coup de pouce"

    `ligne.split(" -> ")` donne deux morceaux comme `"0,1"` ; chacun se découpe ensuite sur la virgule.

### <span class="exo-num">Exercice 4</span> — La grille <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-les-k-k-plus-proches-voisins-aoc-1-4 }

Créer une grille de zéros sous forme de **liste de listes** : `grille[y][x]` est le nombre de segments qui couvrent la case $(x, y)$. Choisir la taille d’après la question précédente.

??? pouce "Coup de pouce"

    Construire chaque ligne séparément dans une boucle (une nouvelle liste `[0] * taille` à chaque tour). Attention : `[[0] * taille] * taille` crée une seule ligne répétée, et modifier une case modifierait toute la colonne !

### <span class="exo-num">Exercice 5</span> — Tracer et compter <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-les-k-k-plus-proches-voisins-aoc-1-5 }

Écrire une fonction `tracer(grille, x1, y1, x2, y2)` qui ajoute 1 à chaque case d’un segment horizontal ou vertical, puis compter les cases qui valent au moins 2. Vérifier `4` sur l’exemple.

??? pouce "Coup de pouce"

    Pour un segment vertical (`x1 == x2`), faire varier `y` du plus petit au plus grand de `y1` et `y2` : `range(min(y1, y2), max(y1, y2) + 1)`. Même chose pour un segment horizontal.

??? pouce "Coup de pouce 2 (début de solution)"

    Pour ignorer les autres segments dans la partie 1 : ne tracer que si `x1 == x2 or y1 == y2`. Pour le comptage, deux boucles imbriquées sur la grille et un compteur.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Les lignes en biais existent aussi et sont tout aussi dangereuses. On prend désormais aussi en compte les segments en **diagonale**, qui sont toujours à exactement 45° (à chaque pas, $x$ et $y$ changent de 1). Même question : nombre de cases couvertes par au moins deux segments.

### <span class="exo-num">Exercice 6</span> — Les diagonales <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-les-k-k-plus-proches-voisins-aoc-1-6 }

Prendre aussi en compte les segments décrits dans la partie 2. Sur l’exemple de la fiche, on doit trouver `8`.

??? pouce "Coup de pouce"

    Sur une diagonale à 45°, à chaque pas, `x` change de 1 **et** `y` change de 1 (en plus ou en moins). Calculer d’abord le sens de chaque déplacement : `+1`, `-1` ou `0`.

??? pouce "Coup de pouce 2 (début de solution)"

    Avec `dx` et `dy` valant `1`, `-1` ou `0`, et `n = max(abs(x2 - x1), abs(y2 - y1))`, les cases du segment sont `(x1 + i * dx, y1 + i * dy)` pour `i` de `0` à `n`. Cette méthode marche aussi pour les segments horizontaux et verticaux.

## Approfondissement

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : un seul tracé pour tous les segments <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-les-k-k-plus-proches-voisins-aoc-1-7 }

La fonction de la partie 2 (avec `dx`, `dy` et $n$ pas) trace aussi les segments horizontaux et verticaux.

1.  À la main, pour le segment `4,4 -> 4,0` : que valent `dx`, `dy` et $n$ ? Écrire les cases obtenues pour $i = 0, 1, \dots, n$.

2.  Réécrire la partie 1 en utilisant uniquement `tracer_tout`, en filtrant les segments avant de les tracer. Vérifier `4` sur l’exemple.

    ??? pouce "Coup de pouce"

        Tracer un segment seulement si `x1 == x2 or y1 == y2`.

3.  Quel est l’avantage d’une seule fonction de tracé plutôt que trois cas séparés ?

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Approfondissement 2 : afficher la carte, puis s’en passer <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-les-k-k-plus-proches-voisins-aoc-1-8 }

1.  Écrire une fonction qui affiche la grille comme dans l’énoncé (un point pour 0, sinon le nombre), et l’utiliser sur l’exemple pour contrôler votre tracé.

    ??? pouce "Coup de pouce"

        Construire chaque ligne affichée comme une chaîne avec `+=`, puis `print`.

2.  Refaire le comptage de la partie 2 sans grille, avec un dictionnaire dont les clés sont les cases `(x, y)` et les valeurs le nombre de segments. Quel est l’avantage si les coordonnées sont très grandes ?

    ??? pouce "Coup de pouce"

        Seules les cases réellement couvertes deviennent des clés.

## <span class="etiquette">Défi 2</span> Rope Bridge

*le pont de corde — simulation et généralisation*

<p class="infos-activite">Jour 9</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/12-defi-aoc-2022-09){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-12-defi-aoc-2022-09.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2022/day/9 ](https://adventofcode.com/2022/day/9 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/12-defi-aoc-2022-09>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

*Ce défi fait intervenir une distance entre deux cases, comme l’algorithme des $k$ plus proches voisins de ce chapitre : ici, deux cases « se touchent » quand le plus grand écart entre leurs coordonnées vaut au plus 1.*

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| rope | corde | knot | nœud |
| head / tail | tête / queue | touching | en contact, qui se touchent |
| adjacent | voisin (y compris en diagonale) | overlapping | superposés |
| step | pas | visit at least once | visiter au moins une fois |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Vous traversez un vieux pont de corde, et pour ne pas regarder en bas vous imaginez une corde qui se déplace sur une grille. La corde a deux bouts, la tête et la queue ; quand on tire la tête, la queue finit par suivre. Le fichier donne la suite des déplacements de la tête, et l’on s’intéresse au chemin suivi par la queue.

    **Ce qu’il faut faire.**

    - Tête et queue partent de la même case. Chaque ligne `D n` déplace la tête de `n` cases, **une à la fois**, vers le haut, le bas, la gauche ou la droite (`U`, `D`, `L`, `R`).

    - Après chaque pas de la tête, si la queue la touche encore (même case ou case voisine, diagonales comprises), elle ne bouge pas. Sinon, elle avance d’une case vers la tête : en ligne droite si elles sont sur la même ligne ou colonne, en diagonale sinon. Autrement dit, la queue rattrape la tête en restant collée à elle.

    - Réponse : le nombre de cases différentes visitées par la queue, départ compris.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-les-k-k-plus-proches-voisins-aoc-2-1 }

Après lecture du résumé (et de l’énoncé), vérifier sa compréhension sur ces cas particuliers :

1.  La tête est en $(2, 1)$ et la queue en $(0, 0)$ : où va la queue ?

2.  Pourquoi faut-il traiter `R 4` comme quatre déplacements d’une case ?

3.  La queue peut-elle se retrouver sur la même case que la tête ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-les-k-k-plus-proches-voisins-aoc-2-2 }

Sur une feuille quadrillée, simuler pas à pas les mouvements (inventés) suivants, la tête et la queue partant de la même case :

```console
R 3
U 2
L 4
D 1
R 2
```

Marquer chaque case par laquelle passe la queue. Vérification : on doit trouver `7` cases.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire les mouvements <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-les-k-k-plus-proches-voisins-aoc-2-3 }

Rappel pour lire un fichier ligne par ligne :

```python
fichier = open("input.txt", encoding="utf-8")
for ligne in fichier:
    ligne = ligne.strip()   # enlève le retour à la ligne final
fichier.close()
```

Construire la liste des mouvements sous forme de couples `(direction, nombre_de_pas)`, par exemple `("R", 3)`.

??? pouce "Coup de pouce"

    `d, n = ligne.split()` puis `int(n)`.

### <span class="exo-num">Exercice 4</span> — Faire suivre un nœud <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-les-k-k-plus-proches-voisins-aoc-2-4 }

Écrire une fonction `suivre(xt, yt, xq, yq)` qui reçoit la position de la tête et celle de la queue, et renvoie la nouvelle position de la queue. Tester les trois situations : en contact, à deux cases en ligne droite, en diagonale « lointaine ».

??? pouce "Coup de pouce"

    La queue doit bouger seulement si `abs(xt - xq) > 1 or abs(yt - yq) > 1`. Dans ce cas, elle se rapproche de la tête d’**au plus une case** dans chaque direction.

??? pouce "Coup de pouce 2 (début de solution)"

    Écrire une petite fonction `signe(n)` qui renvoie `1`, `-1` ou `0`. Si la queue doit bouger : `xq += signe(xt - xq)` et `yq += signe(yt - yq)`. Ce seul calcul couvre la ligne droite **et** la diagonale.

!!! encadre "Outil Python : les ensembles (set)"

    Un **ensemble** (`set`) est une collection **sans doublon** et **sans ordre** : pas d’indice, on peut seulement ajouter un élément, en retirer un, et demander s’il est présent.

    ```python
    vus = set()                 # ensemble vide (attention : {} est un dictionnaire vide)
    vus.add((0, 0))             # on peut y ranger des tuples
    vus.add((1, 0))
    vus.add((0, 0))             # deja present : rien ne change
    print(len(vus))             # 2
    print((1, 0) in vus)        # True : test d'appartenance
    a = {1, 2, 3}
    b = {2, 3, 4}
    print(a | b)                # reunion : {1, 2, 3, 4}
    print(a & b)                # intersection : {2, 3}
    ```

    **Intérêt.** Avec une liste, `x in liste` compare `x` aux éléments un par un : jusqu’à $n$ comparaisons. Un ensemble range chaque élément à un endroit calculé à partir de sa valeur (comme les clés d’un dictionnaire) : Python va directement voir à cet endroit. Le test `x in ensemble` prend un temps qui ne dépend pas du nombre d’éléments.

    *À essayer.* Recopier et exécuter ce code. Que vaut `len({(0, 0), (0, 0), (2, 1)})` ?

### <span class="exo-num">Exercice 5</span> — Simuler <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-les-k-k-plus-proches-voisins-aoc-2-5 }

Simuler tous les mouvements **un pas à la fois** : à chaque pas, déplacer la tête d’une case, faire suivre la queue, et noter la case de la queue dans une liste sans doublon (ou un ensemble, voir l’encadré). Vérifier `7` sur l’exemple.

??? pouce "Coup de pouce"

    Pour `("U", 2)`, on fait deux tours de boucle, chacun déplaçant la tête d’une seule case. Décider du sens du repère (par exemple `y` augmente vers le haut) et s’y tenir.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Le pont tremble et la corde imaginaire s’allonge. Elle a maintenant **10 nœuds** : la tête, puis 9 nœuds qui suivent chacun celui qui le précède, avec exactement la même règle que la queue de la partie 1. Réponse : le nombre de cases différentes visitées par le **dernier** nœud.

### <span class="exo-num">Exercice 6</span> — Une corde plus longue <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-les-k-k-plus-proches-voisins-aoc-2-6 }

Généraliser : la corde est maintenant représentée par une **liste de positions** `noeuds`, `noeuds[0]` étant la tête. Répondre à la nouvelle question. Sur l’exemple de la fiche, la réponse de la partie 2 est `1` ; sur les mouvements `U 6`, `R 12`, `D 9`, `L 15`, on doit trouver `39` pour la partie 1 et `11` pour la partie 2.

??? pouce "Coup de pouce"

    Chaque nœud suit celui qui le précède, exactement avec la fonction `suivre` de la partie 1 : le nœud d’indice `i` joue le rôle de la queue, celui d’indice `i - 1` le rôle de la tête.

??? pouce "Coup de pouce 2 (début de solution)"

    À chaque pas : déplacer `noeuds[0]`, puis `for i in range(1, len(noeuds)):` `noeuds[i] = suivre(...)` en utilisant `noeuds[i - 1]`. La case à noter est celle du **dernier** nœud, `noeuds[-1]`. Avec une liste de 2 nœuds, on doit retrouver la partie 1.

## Approfondissement

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : un ensemble de cases visitées <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-les-k-k-plus-proches-voisins-aoc-2-7 }

1.  Réécrire la simulation de la partie 2 en rangeant les cases visitées dans un ensemble plutôt que dans une liste. Quel test devient inutile ?

    ??? pouce "Coup de pouce"

        `visitees = {(0, 0)}` puis `visitees.add(noeuds[-1])` à chaque pas.

2.  Si la queue visite environ $6\,000$ cases, combien de comparaisons le test `in` sur une liste coûte-t-il au total, à peu près ? Et avec un ensemble ?

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 8</span> — Approfondissement 2 : voir la corde <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-les-k-k-plus-proches-voisins-aoc-2-8 }

1.  Écrire une fonction qui affiche la corde sur une petite grille (le numéro de chaque nœud, des points ailleurs) et l’utiliser après chaque ligne de mouvements de l’exemple.

    ??? pouce "Coup de pouce"

        Parcourir les lignes de haut en bas (`y` décroissant) ; pour chaque case, chercher si un nœud s’y trouve.

2.  Pourquoi, dans la partie 2, un nœud peut-il se retrouver à deux cases en diagonale de son prédécesseur, ce qui n’arrive jamais avec deux nœuds ?

    ??? pouce "Coup de pouce"

        Dans la partie 1, la tête ne bouge jamais en diagonale. Dans la partie 2, le nœud 1 peut bouger en diagonale et entraîner le nœud 2 de façon nouvelle.
