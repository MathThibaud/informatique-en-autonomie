# Défis Advent of Code

<p class="sous-titre">Arbres</p>

## <span class="etiquette">Défi 1</span> Binary Boarding

*les cartes d’embarquement — binaire et dichotomie*

<p class="infos-activite">Jour 5</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/05-defi-aoc-2020-05){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-05-defi-aoc-2020-05.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/5 ](https://adventofcode.com/2020/day/5 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/05-defi-aoc-2020-05>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

*Ce défi réinvestit les arbres binaires vus dans ce chapitre : un code de place décrit un chemin depuis la racine d’un arbre binaire complet, chaque lettre choisissant le fils gauche ou le fils droit.*

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| boarding pass | carte d’embarquement | seat | siège, place |
| row / column | rang / colonne | seat ID | numéro de siège |
| front / back | avant / arrière | lower / upper half | moitié basse / haute |
| binary space partitioning | partition binaire de l’espace | sanity check | vérification de bon sens |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Le héros est enfin dans l’avion… mais il a perdu sa carte d’embarquement. Il photographie celles des autres passagers pour retrouver sa place par élimination. Chaque ligne du fichier est le code de place imprimé sur une carte ; ce code désigne un rang et une colonne de l’avion, avec un système de découpages successifs en deux.

    **Ce qu’il faut faire.**

    - Un code compte 10 lettres. Les 7 premières (`F` ou `B`) donnent le rang, numéroté de 0 à 127 ; les 3 dernières (`L` ou `R`) donnent la colonne, de 0 à 7.

    - Pour décoder, on part de l’intervalle complet des rangs. `F` garde la moitié basse et `B` la moitié haute ; après la septième lettre il ne reste qu’un rang. On procède de même pour la colonne avec `L` (moitié basse) et `R` (moitié haute).

    - Chaque siège a un numéro : rang $\times 8$ + colonne.

    - Il faut renvoyer le plus grand numéro de siège présent dans le fichier.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-arbres-aoc-1-1 }

Après lecture de l’énoncé et du résumé, vérifier sa compréhension :

1.  Quel rang donne `FFFFFFF` ? Et `BBBBBBB` ?

2.  Quels sont le plus petit et le plus grand numéro de siège possibles ?

3.  Deux codes différents peuvent-ils donner le même numéro de siège ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-arbres-aoc-1-2 }

Décoder à la main le code `BFFBFBBLRL` en suivant la méthode de l’énoncé (diviser l’intervalle par deux à chaque lettre). On doit trouver le rang `75`, la colonne `2` et le numéro `602`.

Faire de même avec `FFBBFBFRLR`, puis comparer : écrire `75` et `2` en binaire. Que remarque-t-on ?

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Reconnaître le binaire <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-arbres-aoc-1-3 }

1.  Remplacer dans `BFFBFBBLRL` chaque `F` et chaque `L` par `0`, chaque `B` et chaque `R` par `1`. Que vaut le nombre binaire obtenu ? Le comparer au numéro de siège.

2.  Expliquer pourquoi « multiplier le rang par 8 puis ajouter la colonne » revient à recoller les deux écritures binaires.

??? pouce "Coup de pouce"

    Multiplier par $8 = 2^3$ décale l’écriture binaire de trois rangs vers la gauche, ce qui laisse exactement la place des 3 bits de la colonne.

!!! encadre "Outil Python : conversions binaires (int(..., 2), bin, format) et replace"

    Python sait lire et écrire des nombres en base 2. La méthode `replace` fabrique une nouvelle chaîne où un morceau est remplacé par un autre.

    ```python
    print(int("1011", 2))          # 11 : lit une chaine ecrite en base 2
    print(bin(11))                 # 0b1011 : ecriture binaire (une chaine)
    print(format(11, "08b"))       # 00001011 : sur 8 chiffres, sans 0b
    mot = "FBFB"
    print(mot.replace("F", "0"))   # 0B0B : nouvelle chaine
    print(mot)                     # FBFB : mot n'a pas change
    ```

    **Intérêt.** La conversion prend un temps proportionnel au nombre de chiffres, et `replace` évite d’écrire une boucle caractère par caractère.

    **À essayer.** Que vaut `int("1111111111", 2)` ? Quel lien avec le plus grand numéro de siège possible ?

### <span class="exo-num">Exercice 4</span> — Décoder et chercher le maximum <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-arbres-aoc-1-4 }

Écrire une fonction `numero_siege(code)` qui renvoie le numéro de siège, puis le programme qui donne la réponse sur `input.txt`. Vérifier `numero_siege("BFFBFBBLRL") == 602`. Sur la liste (inventée) `BFFBFBBLRL`, `FBBFFFBRRR`, `BBFBFFFLLR`, `FFBBFBFRLR`, `BFBBBFFLRR`, on doit trouver `833`.

??? pouce "Coup de pouce"

    `int("1011", 2)` convertit une chaîne écrite en binaire en entier. Pour remplacer les lettres, `replace` appelé quatre fois convient.

### <span class="exo-num">Exercice 5</span> — Le lien avec la dichotomie <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-arbres-aoc-1-5 }

Écrire une seconde version `numero_siege_dicho(code)` qui suit littéralement l’énoncé : deux bornes `bas` et `haut`, et chaque lettre garde une moitié. Vérifier qu’elle donne les mêmes résultats que la première. Combien de lettres faudrait-il pour un avion de $1024$ rangs ?

??? pouce "Coup de pouce"

    Le milieu est `(bas + haut) // 2` ; une lettre « basse » modifie `haut`, une lettre « haute » modifie `bas`.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Il reste à trouver la place du héros, puisque c’est la seule dont la carte manque.

    - L’avion est plein, sauf quelques sièges tout à l’avant et tout à l’arrière qui n’existent pas. Votre siège est absent de la liste, mais les numéros juste avant et juste après le vôtre y figurent.

    - Il faut renvoyer le numéro de votre siège.

### <span class="exo-num">Exercice 6</span> — La place libre <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-arbres-aoc-1-6 }

Trouver votre place en suivant les indications de la partie 2.

??? pouce "Coup de pouce"

    Trier la liste des numéros, puis la parcourir en comparant chaque numéro au suivant.

??? pouce "Coup de pouce 2 (début de solution)"

    Dans la liste triée, le trou se repère au premier indice `k` tel que `tries[k + 1] != tries[k] + 1` : la place cherchée est alors `tries[k] + 1`.

## Approfondissement

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Défi : sans tri <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-arbres-aoc-1-7 }

Trouver la place libre en temps linéaire sans trier ni utiliser d’ensemble, en comparant la somme des numéros présents à une somme connue.

??? pouce "Coup de pouce"

    La somme des entiers de $a$ à $b$ vaut $\frac{(a+b)(b-a+1)}{2}$.

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

    **À essayer.** Construire l’ensemble des numéros de la liste de la fiche, puis tester si `602` et `603` en font partie.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Approfondissement 1 : la place libre avec un ensemble <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-arbres-aoc-1-8 }

1.  Recopier et exécuter le code de l’encadré, puis répondre à la question « À essayer ».

2.  À la main : les numéros présents sont $\{12, 13, 14, 16, 17\}$. Parcourir les entiers de $12$ à $17$ et dire, pour chacun, s’il est dans l’ensemble. Quelle place est libre ?

3.  Écrire `place_libre_ensemble(numeros)` qui trouve la place libre sans trier, puis vérifier qu’elle donne le même résultat que l’exercice de la partie 2.

4.  Comparer les complexités des deux méthodes (tri, ensemble).

??? pouce "Coup de pouce"

    Les seules places candidates sont les entiers compris entre le plus petit et le plus grand numéro présents : `range(min(numeros), max(numeros))`.

??? pouce "Coup de pouce 2 (début de solution)"

    On parcourt ces entiers et l’on renvoie le premier qui n’est pas dans l’ensemble `presents = set(numeros)` : chaque test coûte un temps constant.

## <span class="etiquette">Défi 2</span> Custom Customs

*la douane — ensembles, union et intersection*

<p class="infos-activite">Jour 6</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/05-defi-aoc-2020-06){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-05-defi-aoc-2020-06.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/6 ](https://adventofcode.com/2020/day/6 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/05-defi-aoc-2020-06>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| customs | douane | declaration form | formulaire de déclaration |
| yes-or-no question | question fermée (oui/non) | group | groupe |
| anyone | au moins une personne | everyone | tout le monde |
| duplicate | doublon | sum of those counts | somme de ces nombres |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Pendant le vol, on distribue des formulaires de douane comportant 26 questions fermées, repérées par les lettres de `a` à `z`. Le héros aide les autres passagers, regroupés par groupes de voyage, à les remplir. Le fichier recense les réponses : chaque ligne correspond à une personne et contient les lettres des questions auxquelles elle a répondu « oui ».

    **Ce qu’il faut faire.**

    - Les groupes sont séparés par une **ligne vide** ; à l’intérieur d’un groupe, il y a une ligne par personne.

    - Une ligne contient, sans doublon, les lettres des questions où la personne a répondu oui. Une question absente de la ligne correspond donc à un non.

    - Pour chaque groupe, on compte les lettres différentes cochées par **au moins une** personne du groupe. Une même lettre cochée par plusieurs personnes ne compte qu’une fois.

    - Il faut renvoyer la somme de ces nombres sur tous les groupes.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-arbres-aoc-2-1 }

Après lecture de l’énoncé et du résumé, vérifier sa compréhension :

1.  Un groupe formé des deux lignes `ab` et `ba` compte pour combien ?

2.  L’ordre des lettres dans une ligne a-t-il une importance ? Et l’ordre des personnes dans un groupe ?

3.  Peut-on traiter le fichier ligne par ligne sans perdre l’information « fin de groupe » ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-arbres-aoc-2-2 }

```console
xyz
yz

m
m
m

pqr
qrs
rst

abcd

hk
kh
h
```

On considère le fichier (inventé) suivant.

1.  Combien contient-il de groupes, et combien de personnes dans chaque groupe ?

2.  Pour chaque groupe, écrire l’ensemble des lettres demandé par la partie 1 et son cardinal.

Vérification : la somme doit valoir `15`.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Découper en groupes <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-arbres-aoc-2-3 }

Lire tout le fichier en une chaîne et construire une liste de groupes, chaque groupe étant la liste des lignes de ses membres. Afficher le nombre de groupes.

??? pouce "Coup de pouce"

    Couper d’abord aux lignes vides (`"\n\n"`), puis couper chaque bloc avec `split()`.

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

    **À essayer.** Que renvoient `set("banane")` et `len(set("banane"))` ?

### <span class="exo-num">Exercice 4</span> — Réunir les réponses <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-arbres-aoc-2-4 }

Écrire une fonction `nb_oui_quelquun(groupe)` qui renvoie le nombre de lettres présentes chez au moins un membre, puis faire la somme sur tout le fichier. Tester sur l’exemple de la fiche, puis sur vos données.

??? pouce "Coup de pouce"

    `set("pqr")` donne l’ensemble `{"p", "q", "r"}`. Les doublons disparaissent d’eux-mêmes dans un ensemble.

??? pouce "Coup de pouce 2 (début de solution)"

    Partir d’un ensemble vide `set()` et lui ajouter les lettres de chaque membre avec l’opérateur `|` (union).

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Le héros a mal lu la consigne : ce qui compte n’est pas ce que quelqu’un a coché, mais ce que tout le groupe a coché.

    - Le découpage reste le même, mais pour chaque groupe on compte les lettres cochées par **toutes** les personnes du groupe.

    - Il faut renvoyer la somme de ces nombres sur tous les groupes.

### <span class="exo-num">Exercice 5</span> — Changer d’opération <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-arbres-aoc-2-5 }

1.  Quelle opération sur les ensembles correspond à la nouvelle question ?

2.  Écrire la fonction correspondante et faire la somme. Sur l’exemple de la fiche, on doit trouver `9`.

??? pouce "Coup de pouce"

    L’opérateur `&` donne l’intersection de deux ensembles.

??? pouce "Coup de pouce 2 (début de solution)"

    Attention au point de départ : partir de l’ensemble vide ne marche plus ici. Partir plutôt de l’ensemble des réponses du **premier** membre du groupe.

## Approfondissement

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 6</span> — Défi : sans ensembles <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-arbres-aoc-2-6 }

Résoudre les deux parties sans ensemble, avec un dictionnaire qui compte, pour chaque lettre, le nombre de membres du groupe qui l’ont cochée. Comment lit-on alors les deux réponses dans ce dictionnaire ?

??? pouce "Coup de pouce"

    Une lettre compte pour la partie 2 si son compteur est égal au nombre de membres du groupe.

!!! encadre "Outil Python : passer une liste comme arguments (*)"

    Placée devant une liste lors d’un appel de fonction, l’étoile la « dépaquette » : chaque élément devient un argument séparé. Or `set.union` et `set.intersection` acceptent un nombre quelconque d’ensembles.

    ```python
    nombres = [3, 1, 2]
    print(*nombres)                  # 3 1 2  (comme print(3, 1, 2))
    e = [{1, 2, 3}, {2, 3}, {3, 4}]
    print(set.union(*e))             # {1, 2, 3, 4}
    print(set.intersection(*e))      # {3}
    ```

    **Intérêt.** Écrire en une ligne une opération sur un nombre variable d’ensembles, sans boucle ni valeur de départ à choisir.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : chaque partie en une ligne <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-arbres-aoc-2-7 }

1.  À la main, pour le troisième groupe de l’exemple de la fiche (`pqr`, `qrs`, `rst`), que renvoie l’expression suivante ? Et avec `set.union` ?

    `set.intersection(*[set(p) for p in groupe])`

2.  Écrire `nb_oui_quelquun_court(groupe)` et `nb_oui_tous_court(groupe)`, une ligne chacune, et vérifier qu’on retrouve `15` et `9` sur l’exemple.

3.  Que se passe-t-il si un groupe est une liste vide ? Dans quel cas la lecture du fichier pourrait-elle en produire un ?

??? pouce "Coup de pouce"

    La compréhension `[set(p) for p in groupe]` fabrique la liste des ensembles des membres ; il reste à la dépaqueter.

??? pouce "Coup de pouce 2 (début de solution)"

    `len(set.union(*[set(p) for p in groupe]))`, puis la même chose avec `intersection`. Pour la question 3, essayer `set.union(*[])`.
