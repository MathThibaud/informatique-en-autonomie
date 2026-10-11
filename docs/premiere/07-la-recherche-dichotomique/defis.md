# Défis Advent of Code

<p class="sous-titre">La recherche dichotomique</p>

## <span class="etiquette">Défi</span> High-Entropy Passphrases

*les phrases de passe — doublons et anagrammes*

<p class="infos-activite">Jour 4</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/07-defi-aoc-2017-04){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-07-defi-aoc-2017-04.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2017/day/4 ](https://adventofcode.com/2017/day/4 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (lien ci-dessus) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

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

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-1-1 }

Après lecture du résumé (et de l’énoncé), vérifier sa compréhension sur ces cas particuliers :

1.  Les mots `abc` et `abcd` sont-ils considérés comme un doublon ?

2.  Une ligne d’un seul mot est-elle valide ?

3.  (Pour plus tard.) Les mots `ab` et `aab` utilisent les mêmes lettres : sont-ils des anagrammes ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-1-2 }

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

### <span class="exo-num">Exercice 3</span> — Lire et découper <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-1-3 }

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

### <span class="exo-num">Exercice 4</span> — Tous distincts ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-1-4 }

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

### <span class="exo-num">Exercice 5</span> — Reconnaître deux anagrammes <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-1-5 }

Écrire une fonction `signature(mot)` qui renvoie la chaîne formée des lettres du mot rangées dans l’ordre alphabétique. Par exemple, `signature("rame")` doit valoir `"aemr"`. Expliquer pourquoi deux mots sont anagrammes l’un de l’autre si et seulement s’ils ont la même signature.

??? pouce "Coup de pouce"

    `sorted("rame")` renvoie la **liste** `[’a’, ’e’, ’m’, ’r’]`. Pour recoller une liste de caractères en une chaîne : `"".join(liste)`.

### <span class="exo-num">Exercice 6</span> — La partie 2 <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-1-6 }

En réutilisant `signature` et `tous_distincts`, répondre à la nouvelle question. Sur l’exemple du défi, on doit trouver `1`.

??? pouce "Coup de pouce"

    Pour une ligne, construire la liste des signatures de ses mots (boucle et `append`), puis appliquer la fonction de la partie 1 à cette nouvelle liste.

## Approfondissement

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : trier pour rapprocher les doublons <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-1-7 }

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

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Approfondissement 2 : une signature sans tri <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-1-8 }

1.  À la main : donner les effectifs des lettres `a`, `e`, `m`, `r` dans `rame` et dans `arme`. Que constate-t-on ?

2.  Écrire `signature26(mot)` qui renvoie la liste des 26 effectifs (nombre de `a`, de `b`…) du mot, puis refaire la partie 2 avec cette signature. Obtient-on la même réponse ?

    ??? pouce "Coup de pouce"

        Partir de `[0] * 26` et ajouter 1 à la case d’indice `ord(lettre) - ord("a")` pour chaque lettre.

    ??? pouce "Coup de pouce 2 (début de solution)"

        Deux listes se comparent directement avec `==` : la fonction `tous_distincts` marche telle quelle sur une liste de signatures-listes.

!!! encadre "Outil Python : les ensembles (set)"

    Un **ensemble** (`set`) est une collection **sans doublon** et **sans ordre** : pas d’indice, on peut seulement ajouter un élément, en retirer un, et demander s’il est présent. On peut y ranger des nombres, des chaînes ou des p-uplets comme `(0, 0)`. Cet encadré sert aussi pour les défis des chapitres suivants.

    ```python
    vus = set()                 # ensemble vide (attention : {} est un dictionnaire vide)
    vus.add("a")                # ajout
    vus.add("b")
    vus.add("a")                # deja present : rien ne change
    print(len(vus))             # 2
    print("a" in vus)           # True : test d'appartenance
    print(len(set("nsin")))     # 3 : les caracteres distincts de "nsin"
    a = {1, 2, 3}               # ensemble ecrit directement
    b = {2, 3, 4}
    print(a | b)                # reunion : {1, 2, 3, 4}
    print(a & b)                # intersection (elements communs) : {2, 3}
    print({7}.pop())            # 7 : pop retire et renvoie un element
    ```

    **Intérêt.** Avec une liste, `x in liste` compare `x` aux éléments un par un : jusqu’à $n$ comparaisons. Un ensemble range chaque élément à un endroit calculé à partir de sa valeur (comme les clés d’un dictionnaire) : Python va directement voir à cet endroit. Le test `x in ensemble` prend un temps qui ne dépend pas du nombre d’éléments.

    *À essayer.* Que vaut `len(set(["le", "chat", "le"]))` ?

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 9</span> — Approfondissement 3 : tous distincts en une ligne <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-1-9 }

Un ensemble ne garde qu’un exemplaire de chaque élément. En déduire une version de `tous_distincts(mots)` en une seule ligne, et la tester sur l’exemple.

??? pouce "Coup de pouce"

    Comparer la longueur de la liste et celle de l’ensemble de ses éléments.
