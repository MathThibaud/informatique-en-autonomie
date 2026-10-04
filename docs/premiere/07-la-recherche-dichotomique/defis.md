# Défis Advent of Code

<p class="sous-titre">La recherche dichotomique</p>

## <span class="etiquette">Défi 1</span> Squares With Three Sides

*des triangles possibles — inégalité triangulaire, lecture par colonnes*

<p class="infos-activite">Jour 3</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/07-defi-aoc-2016-03){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-07-defi-aoc-2016-03.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2016/day/3 ](https://adventofcode.com/2016/day/3 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (facultatif), le lien *get your puzzle input* donne **vos** données, à enregistrer sous `input.txt` à côté du programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/07-defi-aoc-2016-03>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|           |          |             |                              |
|:----------|:---------|:------------|:-----------------------------|
| side      | côté     | length      | longueur                     |
| triangle  | triangle | valid       | valide, possible             |
| sum       | somme    | larger than | plus grand que (strictement) |
| remaining | restant  | impossible  | impossible                   |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** En explorant les bureaux du lapin de Pâques, vous trouvez des documents couverts de triangles, chacun décrit par les longueurs de ses trois côtés. Mais certains de ces « triangles » sont impossibles à construire. Le fichier liste ces triplets de longueurs : il faut trier le possible de l’impossible.

    **Ce qu’il faut faire.**

    - Chaque ligne contient trois longueurs entières, alignées avec des espaces.

    - Trois longueurs forment un triangle possible si la somme de deux quelconques d’entre elles est **strictement** plus grande que la troisième. Autrement dit, aucun côté n’est trop long pour être « rejoint » par les deux autres.

    - La réponse est le nombre de lignes qui forment un triangle possible.

### <span class="exo-num">Exercice 1</span> — Vérifier sa compréhension <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-1-1 }

Questions pièges, à traiter sur le cahier :

1.  Les longueurs `3 4 7` forment-elles un triangle possible ? Et `5 5 5` ?

2.  L’ordre des trois nombres sur la ligne a-t-il de l’importance ?

3.  Pourquoi ne suffit-il pas de vérifier une seule des trois inégalités, prise au hasard ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-1-2 }

On considère le fichier (inventé) suivant :

```console
  4    5    6
  3   10    4
  8    2    5
  7    7    7
  1    9    9
 20    6   16
```

Pour chaque ligne, dire si c’est un triangle possible. Vérification : on doit en trouver `4`.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire le fichier <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-1-3 }

Écrire une fonction `lire(nom_fichier)` qui renvoie la liste des lignes, chaque ligne étant une liste de trois entiers (une *liste de listes*). Sur l’exemple, le premier élément est `[4, 5, 6]`.

??? pouce "Coup de pouce"

    Les espaces en début de ligne et les espaces multiples ne gênent pas `split()` sans argument.

### <span class="exo-num">Exercice 4</span> — Triangle ou pas <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-1-4 }

Écrire une fonction `est_triangle(a, b, c)` qui renvoie `True` si les trois longueurs forment un triangle possible. Faut-il vraiment tester trois inégalités ? Compter ensuite les triangles possibles de l’exemple et de vos données.

??? pouce "Coup de pouce"

    On peut écrire les trois conditions reliées par `and`. Ou bien : si l’on trie les trois longueurs, une seule condition suffit. Laquelle ?

??? pouce "Coup de pouce 2 (début de solution)"

    `x, y, z = sorted([a, b, c])` : alors `z` est le plus grand côté, et le triangle est possible quand `x + y > z`.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    En regardant mieux les documents, vous comprenez que les triangles ne sont pas écrits en lignes, mais **en colonnes**. On prend les lignes par paquets de trois lignes consécutives ; dans chaque paquet, chacune des trois colonnes donne un triangle. La réponse est le nombre de triangles possibles.

### <span class="exo-num">Exercice 5</span> — Lire par colonnes <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-1-5 }

Sur l’exemple, écrire à la main les six triangles obtenus avec la nouvelle lecture : on doit trouver `2` triangles possibles.

??? pouce "Coup de pouce"

    On regroupe les lignes par paquets de trois ; dans chaque paquet, chaque colonne forme un triangle. Pour l’exemple, le premier triangle est `4, 3, 8`.

### <span class="exo-num">Exercice 6</span> — Programmer la partie 2 <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-1-6 }

Réutiliser `lire` et `est_triangle` pour répondre à la partie 2.

??? pouce "Coup de pouce"

    Parcourir les indices de ligne de 3 en 3 : `for i in range(0, len(lignes), 3):`. Les lignes du paquet sont `lignes[i]`, `lignes[i + 1]` et `lignes[i + 2]`.

??? pouce "Coup de pouce 2 (début de solution)"

    Dans le paquet, pour chaque colonne `j` de 0 à 2, le triangle est formé de `lignes[i][j]`, `lignes[i + 1][j]` et `lignes[i + 2][j]`.

## Approfondissement

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : une fonction de transformation <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-1-7 }

1.  Écrire une fonction `colonnes(lignes)` qui transforme la liste de listes en la liste des triangles lus selon la règle de la partie 2. Sur l’exemple, le résultat commence par `[[4, 3, 8], [5, 10, 2], …]`.

2.  Écrire une fonction `compter(triangles)` qui compte les triangles possibles d’une liste de triplets, puis traiter les deux parties avec elle.

3.  Pourquoi la longueur du fichier doit-elle être un multiple de 3 ? Que se passe-t-il sinon ?

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Approfondissement 2 : sans trier <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-1-8 }

Écrire `est_triangle_bis(a, b, c)` qui teste directement les trois inégalités, sans trier. Vérifier sur tout le fichier qu’elle donne les mêmes résultats que `est_triangle`. Laquelle fait le moins de calculs ?

??? pouce "Coup de pouce"

    Trois conditions reliées par `and`. Le tri de trois nombres demande lui aussi des comparaisons.

## <span class="etiquette">Défi 2</span> High-Entropy Passphrases

*les phrases de passe — doublons et anagrammes*

<p class="infos-activite">Jour 4</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/07-defi-aoc-2017-04){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-07-defi-aoc-2017-04.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2017/day/4 ](https://adventofcode.com/2017/day/4 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/07-defi-aoc-2017-04>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|            |                 |                     |                         |
|:-----------|:----------------|:--------------------|:------------------------|
| passphrase | phrase de passe | valid               | valide                  |
| duplicate  | en double       | separated by spaces | séparés par des espaces |
| word       | mot             | policy              | règle, politique        |
| anagram    | anagramme       | rearrange           | réarranger, permuter    |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Un nouveau système informatique protège ses comptes par des « phrases de passe » : plusieurs mots en minuscules séparés par des espaces. Pour qu’une phrase soit assez sûre, elle doit respecter une règle de construction. Le fichier contient une liste de phrases de passe, une par ligne, et l’on veut savoir combien sont acceptables.

    **Ce qu’il faut faire.**

    - Une phrase est valide si elle ne contient **jamais deux fois le même mot**, exactement le même (une ressemblance ne suffit pas à la rendre invalide).

    - Réponse : le nombre de lignes valides.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-2-1 }

Après lecture du résumé (et de l’énoncé), vérifier sa compréhension sur ces cas particuliers :

1.  Les mots `abc` et `abcd` sont-ils considérés comme un doublon ?

2.  Une ligne d’un seul mot est-elle valide ?

3.  (Pour plus tard.) Les mots `ab` et `aab` utilisent les mêmes lettres : sont-ils des anagrammes ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-2-2 }

On considère le fichier (inventé) suivant :

```console
le chat et le chien
un deux trois
ab ba abc
mer rame arme
sol los sol
```

Indiquer pour chaque ligne si elle est valide. Vérification : on doit obtenir `3`. Les mots `ab` et `ba` sont-ils des doublons au sens de la partie 1 ?

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire et découper <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-2-3 }

Rappel pour lire un fichier ligne par ligne :

```python
fichier = open("input.txt", encoding="utf-8")
for ligne in fichier:
    ligne = ligne.strip()   # enlève le retour à la ligne final
fichier.close()
```

Pour chaque ligne, construire la liste de ses mots et l’afficher.

??? pouce "Coup de pouce"

    `ligne.split()` (sans argument) découpe la chaîne sur les espaces et renvoie une liste de chaînes.

### <span class="exo-num">Exercice 4</span> — Tous distincts ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-2-4 }

Écrire une fonction `tous_distincts(mots)` qui renvoie `True` si la liste `mots` ne contient aucun doublon. Tester sur les lignes de l’exemple, puis compter les lignes valides de vos données.

??? pouce "Coup de pouce"

    Deux boucles imbriquées sur les indices `i` et `j > i` : dès que `mots[i] == mots[j]`, la liste contient un doublon.

??? pouce "Coup de pouce 2 (début de solution)"

    `for i in range(len(mots)):` puis `for j in range(i + 1, len(mots)):` ; renvoyer `False` dès que `mots[i] == mots[j]`, et `True` après les deux boucles.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Le service de sécurité durcit la règle : un mot ne doit pas pouvoir s’obtenir en mélangeant les lettres d’un autre mot de la même ligne. Une phrase est valide si aucun mot n’est une **anagramme** d’un autre (mêmes lettres, en même nombre, dans un ordre éventuellement différent). Deux mots identiques sont aussi anagrammes. Réponse : le nombre de lignes valides.

!!! encadre "Outil Python : recoller une liste de caractères (join)"

    `sorted` appliqué à une chaîne renvoie la **liste** de ses caractères triés. Pour obtenir de nouveau une chaîne, on utilise `join` : la chaîne placée avant le point sert de séparateur.

    ```python
    lettres = sorted("rame")        # sorted sur une chaine renvoie une LISTE
    print(lettres)                  # ['a', 'e', 'm', 'r']
    print("".join(lettres))         # aemr : recolle sans separateur
    print("-".join(lettres))        # a-e-m-r : le separateur est la chaine de gauche
    ```

    **Intérêt.** Une chaîne se compare directement à une autre avec `==` ; une liste comparée à une chaîne donne toujours `False`. Recoller la liste évite ce piège.

    *À essayer.* Que renvoie `", ".join(["un", "deux"])` ? Et `sorted("rame") == "aemr"` ?

### <span class="exo-num">Exercice 5</span> — Reconnaître deux anagrammes <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-2-5 }

Écrire une fonction `signature(mot)` qui renvoie la chaîne formée des lettres du mot rangées dans l’ordre alphabétique. Par exemple, `signature("rame")` doit valoir `"aemr"`. Expliquer pourquoi deux mots sont anagrammes l’un de l’autre si et seulement s’ils ont la même signature.

??? pouce "Coup de pouce"

    `sorted("rame")` renvoie la **liste** `[’a’, ’e’, ’m’, ’r’]`. Pour recoller une liste de caractères en une chaîne : `"".join(liste)`.

### <span class="exo-num">Exercice 6</span> — La partie 2 <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-2-6 }

En réutilisant `signature` et `tous_distincts`, répondre à la nouvelle question. Sur l’exemple de la fiche, on doit trouver `1`.

??? pouce "Coup de pouce"

    Pour une ligne, construire la liste des signatures de ses mots (boucle et `append`), puis appliquer la fonction de la partie 1 à cette nouvelle liste.

## Approfondissement

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : trier pour rapprocher les doublons <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-2-7 }

Une autre idée pour `tous_distincts` réutilise le **tri**.

1.  À la main : trier les mots de la ligne `le chat et le chien`. Où se trouvent les deux `le` dans la liste triée ?

2.  Expliquer pourquoi, dans une liste triée, il suffit de comparer chaque élément à son **voisin** pour savoir s’il y a un doublon.

3.  Écrire `tous_distincts_tri(mots)` avec une seule boucle et vérifier qu’elle donne la même réponse que la partie 1.

    ??? pouce "Coup de pouce"

        Travailler sur une copie triée `t = sorted(mots)` pour ne pas modifier la liste de départ.

    ??? pouce "Coup de pouce 2 (début de solution)"

        Comparer `t[i]` et `t[i + 1]` pour `i` de `0` à `len(t) - 2` ; attention à ne pas sortir de la liste.

4.  Pour une ligne de $k$ mots, comparer le nombre de comparaisons de la double boucle et de cette méthode (le tri de Python coûte environ $k \log_2 k$ comparaisons).

!!! encadre "Outil Python : codes des caractères (ord, chr)"

    Chaque caractère a un numéro (son code). `ord` donne le code d’un caractère, `chr` fait l’inverse. Les lettres minuscules ont des codes consécutifs.

    ```python
    print(ord("a"))              # 97 : code du caractere
    print(ord("c") - ord("a"))   # 2 : rang de "c" dans l'alphabet (a -> 0)
    print(chr(98))               # b : operation inverse
    compteurs = [0] * 26
    compteurs[ord("c") - ord("a")] += 1    # on compte un "c"
    ```

    **Intérêt.** `ord(c) - ord("a")` transforme une lettre en un indice de $0$ à $25$ : on peut alors compter les lettres dans une simple liste de 26 entiers.

    *À essayer.* Que vaut `ord("z") - ord("a")` ? Et `chr(ord("a") + 3)` ?

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Approfondissement 2 : une signature sans tri <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-2-8 }

1.  À la main : donner les effectifs des lettres `a`, `e`, `m`, `r` dans `rame` et dans `arme`. Que constate-t-on ?

2.  Écrire `signature26(mot)` qui renvoie la liste des 26 effectifs (nombre de `a`, de `b`…) du mot, puis refaire la partie 2 avec cette signature. Obtient-on la même réponse ?

    ??? pouce "Coup de pouce"

        Partir de `[0] * 26` et ajouter 1 à la case d’indice `ord(lettre) - ord("a")` pour chaque lettre.

    ??? pouce "Coup de pouce 2 (début de solution)"

        Deux listes se comparent directement avec `==` : la fonction `tous_distincts` marche telle quelle sur une liste de signatures-listes.

!!! encadre "Outil Python : les ensembles (set)"

    Un **ensemble** (`set`) est une collection **sans doublon** et **sans ordre** : pas d’indice, on peut seulement ajouter un élément, en retirer un, et demander s’il est présent.

    ```python
    vus = set()                 # ensemble vide (attention : {} est un dictionnaire vide)
    vus.add("a")                # ajout
    vus.add("b")
    vus.add("a")                # deja present : rien ne change
    print(len(vus))             # 2
    print("a" in vus)           # True : test d'appartenance
    print(set("nsin"))          # les caracteres distincts, dans un ordre quelconque
    print(len(set("nsin")))     # 3
    ```

    **Intérêt.** Avec une liste, `x in liste` compare `x` aux éléments un par un : jusqu’à $n$ comparaisons. Un ensemble range chaque élément à un endroit calculé à partir de sa valeur (comme les clés d’un dictionnaire) : Python va directement voir à cet endroit. Le test `x in ensemble` prend un temps qui ne dépend pas du nombre d’éléments.

    *À essayer.* Que vaut `len(set(["le", "chat", "le"]))` ?

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 9</span> — Approfondissement 3 : tous distincts en une ligne <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-2-9 }

Un ensemble ne garde qu’un exemplaire de chaque élément. En déduire une version de `tous_distincts(mots)` en une seule ligne, et la tester sur l’exemple.

??? pouce "Coup de pouce"

    Comparer la longueur de la liste et celle de l’ensemble de ses éléments.
