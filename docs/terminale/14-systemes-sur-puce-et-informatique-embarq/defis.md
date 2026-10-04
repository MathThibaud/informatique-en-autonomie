# Défis Advent of Code

<p class="sous-titre">Systèmes sur puce et informatique embarquée</p>

## <span class="etiquette">Défi</span> Docking Data

*l’amarrage — masques et opérations bit à bit*

<p class="infos-activite">Jour 14</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/14-defi-aoc-2020-14){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-14-defi-aoc-2020-14.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/14 ](https://adventofcode.com/2020/day/14 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/14-defi-aoc-2020-14>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| bitmask | masque de bits | overwrite | écraser, remplacer |
| unchanged | inchangé | memory address | adresse mémoire |
| 36-bit unsigned | entier positif sur 36 bits | most significant bit | bit de poids fort |
| initialization | initialisation | sum | somme |
| floating | flottant (bit qui prend les deux valeurs) | decoder | décodeur |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** À l’approche du port, l’ordinateur du ferry doit initialiser sa mémoire, mais il ne comprend pas le système de masques de bits utilisé par le port. Vous allez émuler ce système. Le fichier est un petit programme : chaque ligne change le masque courant ou écrit une valeur en mémoire.

    **Ce qu’il faut faire.**

    - Une ligne `mask = ` est suivie de 36 caractères parmi `0`, `1`, `X` ; une ligne `mem[a] = v` écrit la valeur $v$ à l’adresse $a$. Adresses et valeurs sont des entiers positifs sur 36 bits.

    - Le masque s’écrit bit de poids fort à gauche ($2^{35}$) et reste en vigueur jusqu’au `mask` suivant.

    - Juste avant chaque écriture, on applique le masque à la valeur : un `0` ou un `1` du masque impose ce bit, un `X` laisse le bit de $v$ tel quel. Autrement dit, le masque ne retouche que certains bits.

    - Toutes les cases valent 0 au départ ; écrire à nouveau à la même adresse remplace l’ancienne valeur. La réponse est la somme de toutes les valeurs présentes en mémoire à la fin.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-14-systemes-sur-puce-et-informatique-embarq-aoc-1-1 }

Questions de vérification, à traiter sur le cahier :

1.  Si le masque ne contient que des `X`, quelle valeur est écrite ?

2.  Deux lignes `mem` écrivent à la même adresse : que contient la case à la fin ?

3.  Pourquoi ne peut-on pas représenter la mémoire par une liste de $2^{36}$ cases ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-14-systemes-sur-puce-et-informatique-embarq-aoc-1-2 }

On considère le programme (inventé) suivant :

```console
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX1X0X0
mem[3] = 6
mem[10] = 21
mem[3] = 13
```

Écrire 6, 21 et 13 en binaire sur 6 bits, appliquer le masque et donner la valeur écrite à chaque fois. Vérification : la réponse est `40`.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire une ligne <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-14-systemes-sur-puce-et-informatique-embarq-aoc-1-3 }

Écrire une fonction `analyser(ligne)` qui renvoie `("mask", chaine)` ou `("mem", adresse, valeur)` selon la ligne.

??? pouce "Coup de pouce"

    `ligne.split(" = ")` sépare la partie gauche de la valeur. Pour l’adresse, on peut découper `"mem[3]"` avec des tranches ou `replace`.

!!! encadre "Outil Python : opérations bit à bit et conversions binaires (&, |, int(s, 2), format)"

    Les opérateurs `&` (et) et `|` (ou) travaillent sur l’écriture binaire des entiers, bit par bit, tous les bits en même temps. `int(chaine, 2)` lit une chaîne binaire ; `format(n, "036b")` écrit `n` en binaire sur 36 chiffres, complété par des zéros à gauche.

    ```python
    a = int("1100", 2)             # 12 : chaine binaire -> entier
    b = int("1010", 2)             # 10
    print(a & b)                   # 8  (1000) : 1 la ou les deux bits valent 1
    print(a | b)                   # 14 (1110) : 1 la ou au moins un des bits vaut 1
    print(format(a & b, "04b"))    # 1000 : entier -> chaine binaire sur 4 chiffres
    print(format(5, "036b"))       # 36 caracteres, completes par des 0 a gauche
    print(bin(5))                  # 0b101 : autre ecriture, avec le prefixe 0b
    ```

    **Intérêt.** `x & m` met à 0 tous les bits de `x` là où `m` a un 0 ; `x | m` met à 1 tous les bits de `x` là où `m` a un 1. Une seule opération, très rapide, remplace une boucle sur les 36 bits.

    **À essayer.** Calculer à la main `13 & 6` et `13 | 6` (écrire 13 et 6 sur 4 bits), puis vérifier avec Python.

!!! encadre "Outil Python : méthodes de chaînes (replace, count, find)"

    `s.replace(a, b)` renvoie une copie de `s` où chaque `a` est remplacé par `b` ; `s.count(a)` compte les occurrences de `a` ; `s.find(a)` donne l’indice de la première occurrence, ou $-1$ s’il n’y en a pas.

    ```python
    m = "X1X0"
    print(m.replace("X", "0"))     # 0100 : renvoie une NOUVELLE chaine
    print(m.count("X"))            # 2 : nombre d'occurrences
    print(m.find("X"))             # 0 : indice de la premiere occurrence
    print(m.find("Z"))             # -1 : absent
    ```

    **Intérêt.** Ces méthodes évitent d’écrire une boucle sur les caractères ; leur coût reste proportionnel à la longueur de la chaîne.

    **À essayer.** Après `m.replace("X", "0")`, que vaut `m` ? Pourquoi ?

### <span class="exo-num">Exercice 4</span> — Appliquer le masque avec deux opérations bit à bit <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-14-systemes-sur-puce-et-informatique-embarq-aoc-1-4 }

Écrire une fonction `appliquer(masque, valeur)`. On construira deux entiers à partir du masque : l’un pour forcer des bits à `1`, l’autre pour forcer des bits à `0`. Vérifier : `appliquer(m, 6)` vaut `18` avec le masque de l’exemple.

??? pouce "Coup de pouce"

    En Python, `a | b` (ou bit à bit) et `a & b` (et bit à bit) agissent sur chaque bit ; `int("101", 2)` convertit une chaîne binaire en entier.

??? pouce "Coup de pouce 2 (début de solution)"

    Remplacer les `X` du masque par des `0` donne un entier `ou_masque` à combiner avec `|` ; les remplacer par des `1` donne un entier `et_masque` à combiner avec `&`.

### <span class="exo-num">Exercice 5</span> — La mémoire <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-14-systemes-sur-puce-et-informatique-embarq-aoc-1-5 }

La mémoire a $2^{36}$ cases : une liste est impossible. Utiliser un dictionnaire `memoire` (adresse $\to$ valeur), exécuter le programme et afficher la somme des valeurs. Tester sur l’exemple de la fiche, puis sur vos données.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Le programme ne fonctionne toujours pas : la version du système utilisée par le port est en fait un « décodeur d’adresses ».

    - Le masque agit maintenant sur l’**adresse**, et la valeur est écrite telle quelle : un `0` laisse le bit de l’adresse inchangé, un `1` le force à 1, un `X` est *flottant* et prend les deux valeurs.

    - Avec $k$ bits flottants, la valeur est donc écrite dans $2^k$ adresses. La réponse demandée est la même.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Un masque sur les adresses <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-14-systemes-sur-puce-et-informatique-embarq-aoc-1-6 }

Écrire une fonction `adresses(masque, adresse)` qui renvoie la liste de toutes ces adresses.

Pour tester, on utilise un autre programme inventé :

```console
mask = 000000000000000000000000000000X10X0X
mem[5] = 4
mask = 0000000000000000000000000000000X0000
mem[1] = 10
```

Vérification : `mem[5] = 4` écrit dans 8 adresses, de `16` à `53` ; la réponse finale est `48` (une adresse est écrite deux fois).

??? pouce "Coup de pouce"

    Travailler sur des chaînes de 36 caractères : `format(adresse, "036b")` donne l’écriture binaire complétée par des zéros. On construit d’abord la chaîne résultat avec ses `X`.

??? pouce "Coup de pouce 2 (début de solution)"

    Pour remplacer les $k$ bits `X` : énumérer les entiers de $0$ à $2^k - 1$ et utiliser leurs $k$ bits ; ou bien écrire une fonction récursive qui remplace le premier `X` par `0`, puis par `1`.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Défi : combien de `X` au maximum ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-14-systemes-sur-puce-et-informatique-embarq-aoc-1-7 }

Afficher le plus grand nombre de `X` parmi les masques de vos données, et le nombre total d’adresses écrites. Pourquoi le dictionnaire reste-t-il de taille raisonnable alors que la mémoire a $2^{36}$ cases ?

## Approfondissement

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Approfondissement 1 : énumérer les adresses par récursivité <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-14-systemes-sur-puce-et-informatique-embarq-aoc-1-8 }

1.  À la main, pour le modèle `X1X` : remplacer le premier `X` par `0`, puis par `1`, et recommencer sur chacune des deux chaînes obtenues. Dessiner l’arbre de ces remplacements et lister les chaînes finales dans l’ordre.

2.  Écrire une fonction récursive `remplacer_x(modele)` qui renvoie la liste de toutes les chaînes obtenues en remplaçant les `X` par des `0` et des `1`. Quel est le cas de base ?

    ??? pouce "Coup de pouce"

        Cas de base : le modèle ne contient aucun `X` (`find` renvoie $-1$) ; la liste ne contient alors que le modèle lui-même.

    ??? pouce "Coup de pouce 2 (début de solution)"

        Sinon, avec `i = modele.find("X")`, construire par tranches `modele[:i] + "0" + modele[i + 1:]` et la même chaîne avec `"1"`, puis concaténer les deux listes renvoyées par les appels récursifs.

3.  Utiliser `remplacer_x` pour réécrire `adresses` ; vérifier les 8 adresses de l’exemple de la partie 2 et la réponse `48`.

4.  Combien d’appels récursifs pour un modèle contenant $k$ fois `X` ? Comparer avec la version qui énumère les entiers de $0$ à $2^k - 1$.
