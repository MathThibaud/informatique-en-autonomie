# Défis Advent of Code

<p class="sous-titre">Recherche textuelle</p>

## <span class="etiquette">Défi 1</span> Password Philosophy

*les mots de passe — découpage de chaînes et ou exclusif*

<p class="infos-activite">Jour 2</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/12-defi-aoc-2020-02){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-12-defi-aoc-2020-02.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/2 ](https://adventofcode.com/2020/day/2 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (lien ci-dessus) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

!!! encadre "Le défi en bref"

    **Le problème.** Une base de mots de passe est en partie abîmée : chaque ligne contient un mot de passe et la règle qu’il devait respecter. Il faut compter les mots de passe conformes à leur règle. Le fichier compte un millier de lignes, toutes différentes : il faut un programme qui découpe chaque ligne, puis applique la règle.

    **Ce qu’on réinvestit.** La **recherche dans un texte**, vue dans ce chapitre. Ici, le motif cherché est une simple lettre : on compte ses occurrences dans le mot de passe par une boucle de comptage, que l’on compare à la recherche naïve du cours (qui teste chaque position). L’approfondissement revient sur le **ou exclusif** du masque jetable, vu au chapitre 10, car c’est exactement l’opération logique dont la partie 2 a besoin.

    **La démarche de la fiche.**

    1.  Comprendre la règle et ses pièges, puis l’appliquer à la main sur cinq lignes.

    2.  Écrire une fonction qui découpe une ligne en ses quatre morceaux.

    3.  Écrire une fonction de validation, puis compter les lignes valides : c’est la partie 1.

    4.  Partie 2 : garder le découpage, écrire une seconde fonction de validation.

    5.  En approfondissement, étudier le ou exclusif par sa table de vérité.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| password | mot de passe | policy | règle, politique |
| corrupted | corrompu, abîmé | valid | valide, conforme |
| lowest / highest | plus petit / plus grand | number of times | nombre de fois |
| log in | se connecter | instance | occurrence (d’une lettre) |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Le héros part en vacances et doit descendre jusqu’à la côte en luge. Le loueur de luges ne parvient plus à se connecter : sa base de mots de passe est en partie abîmée. Il s’agit de repérer, dans cette base, les mots de passe qui respectent leur propre règle.

    **Les données.** Chaque ligne du fichier décrit un mot de passe enregistré, accompagné de la règle de sécurité qui était en vigueur quand il a été choisi. Une ligne a la forme `a-b l: motdepasse` : deux entiers $a \leq b$ séparés par un tiret, un espace, une lettre `l` suivie de deux-points, un espace, puis le mot de passe, écrit en lettres minuscules. Les entiers peuvent avoir plusieurs chiffres.

    **La règle.**

    - On compte combien de fois la lettre `l` apparaît dans le mot de passe.

    - Le mot de passe est valide si ce nombre est au moins $a$ et au plus $b$, bornes comprises. Autrement dit, le nombre d’occurrences de `l` doit appartenir à l’intervalle $[a, b]$.

    **La réponse attendue.** Le nombre de lignes dont le mot de passe respecte sa règle. Par exemple, `1-3 b: abbc` est valide (deux `b`) mais `2-3 x: xab` ne l’est pas (un seul `x`) : ces deux lignes seules donneraient la réponse 1.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-recherche-textuelle-aoc-1-1 }

**But.** Vérifier qu’on a compris la règle et repérer les pièges du format des lignes.

**À quoi ça sert ?** Chaque question annonce une difficulté du programme : les bornes comprises dans le test, le `:` collé à la lettre lors du découpage, et les nombres à plusieurs chiffres qui interdisent de lire la ligne à des positions fixes.

Après lecture de l’énoncé et du résumé, vérifier sa compréhension :

1.  Le mot de passe `kkk` respecte-t-il la règle `1-3 k` ? Et la règle `4-5 k` ?

2.  Après `"2-3 z: zaz".split()`, que contient le deuxième morceau ? Quel piège pour comparer la lettre ?

3.  Les nombres peuvent avoir deux chiffres (`10-12`). Pourquoi est-il alors dangereux de lire la ligne à des positions fixes ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-recherche-textuelle-aoc-1-2 }

**But.** Appliquer la règle à la main sur cinq lignes.

**À quoi ça sert ?** On obtient un exemple dont on **connaît la réponse** (`3`) : le programme devra le retrouver avant d’être lancé sur les vraies données.

On considère le fichier (inventé) suivant :

```console
2-4 m: mmxmz
1-2 k: akkkb
3-5 t: tttxt
1-1 q: rst
2-6 e: eeabcf
```

Pour chaque ligne, dire si le mot de passe respecte la règle de la partie 1. Vérification : on doit compter `3` mots de passe valides.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Découper une ligne <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-recherche-textuelle-aoc-1-3 }

**But.** Écrire une fonction qui transforme une ligne de texte en ses quatre morceaux utiles : deux entiers, la lettre, le mot de passe.

**À quoi ça sert ?** Séparer la lecture de la règle de son application rend chaque fonction plus simple à tester. Ce découpage sert tel quel dans les deux parties : seule la validation changera.

Écrire une fonction `decouper(ligne)` qui renvoie le tuple `(a, b, lettre, mdp)` formé de deux entiers et de deux chaînes. Par exemple `decouper("2-4 m: mmxmz")` doit renvoyer `(2, 4, "m", "mmxmz")`. Tester avec `assert`.

??? pouce "Coup de pouce"

    `ligne.split()` coupe aux espaces et donne trois morceaux ; le premier se recoupe avec `split("-")`, le deuxième se débarrasse du `:` en ne gardant que son premier caractère.

!!! encadre "Méthode : compter les apparitions d’une lettre, et comparaisons enchaînées"

    Pour compter combien de fois une lettre apparaît dans une chaîne, on parcourt la chaîne caractère par caractère avec un **compteur** initialisé à 0. Python accepte aussi d’enchaîner les comparaisons, comme en mathématiques.

    ```python
    def compter(lettre, mot):
        """Renvoie le nombre d'apparitions de lettre dans mot."""
        nb = 0
        for c in mot:
            if c == lettre:
                nb += 1
        return nb

    print(compter("a", "banane"))   # 2
    print(compter("z", "banane"))   # 0 si absente
    n = 3
    print(1 <= n <= 5)              # True : equivaut a 1 <= n and n <= 5
    ```

    **Intérêt.** Un seul parcours de la chaîne : le coût est proportionnel à sa longueur.

    **À essayer.** Adapter `compter` pour compter un **morceau** de chaîne (`motif`) en testant chaque position `i` avec la tranche `mot[i:i + len(motif)]`. Combien d’apparitions de `"aa"` trouve-t-on dans `"aaaa"` ? Comparer avec la fonction `recherche_naive("aa", "aaaa")` du cours.

!!! encadre "Outil Python : strip (nettoyer une ligne lue)"

    Chaque ligne renvoyée par `readlines()` se termine par le caractère de fin de ligne `"\n"` (sauf parfois la dernière). `ligne.strip()` renvoie une copie de la ligne sans les espaces ni les fins de ligne placés au début et à la fin.

    ```python
    ligne = "1721\n"
    print(ligne.strip())                  # 1721
    print(len(ligne), len(ligne.strip())) # 5 4
    ```

    **Intérêt.** Comparer ou découper une ligne sans que la fin de ligne ne gêne : `"abc\n" == "abc"` vaut `False`.

### <span class="exo-num">Exercice 4</span> — Valider et compter <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-recherche-textuelle-aoc-1-4 }

**But.** Écrire la fonction qui dit si un mot de passe respecte sa règle, puis compter les lignes valides du fichier.

**À quoi ça sert ?** C’est le cœur de la partie 1 : la boucle de comptage de la lettre est une recherche dans un texte, et le nombre de lignes valides est la réponse à donner.

Écrire une fonction `valide1(a, b, lettre, mdp)` qui renvoie un booléen, puis le programme qui lit `input.txt` et compte les mots de passe valides. Tester sur l’exemple du défi, puis sur vos données.

??? pouce "Coup de pouce"

    Compter les occurrences de `lettre` dans `mdp` avec une boucle et un compteur (voir l’encadré « Méthode »). Python accepte les comparaisons enchaînées : `a <= n <= b`.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    **Ce qui change.** Le loueur s’aperçoit qu’il s’est trompé de règlement : les deux nombres n’ont pas le sens qu’on leur a donné. Le fichier et le format des lignes ne changent pas ; seule la façon de lire la règle change.

    **La nouvelle règle.**

    - Les deux nombres désignent maintenant deux **positions** dans le mot de passe, numérotées **à partir de 1** (il n’y a pas de position 0).

    - Le mot de passe est valide si la lettre se trouve à exactement une de ces deux positions : ni à aucune, ni aux deux.

    - Les occurrences de la lettre ailleurs dans le mot ne comptent plus.

    **La réponse attendue.** Le nombre de mots de passe valides selon cette nouvelle règle. Par exemple, `1-3 c: cbd` est valide (un `c` en position 1 seulement), mais `1-3 c: cbc` ne l’est pas (un `c` aux deux positions).

### <span class="exo-num">Exercice 5</span> — Une nouvelle règle <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-recherche-textuelle-aoc-1-5 }

**But.** Appliquer la règle de la partie 2 à la main, puis la programmer dans une seconde fonction de validation.

**À quoi ça sert ?** On réutilise `decouper` et la boucle qui compte les lignes valides ; seule la fonction de validation change. Les deux pièges sont la numérotation à partir de 1 et le « exactement une des deux positions ».

1.  Sans programme : la ligne `1-3 a: aba` est-elle valide selon la nouvelle règle ? Et `2-3 b: abc` ?

2.  Écrire `valide2(a, b, lettre, mdp)` et compter. Sur l’exemple du défi, on doit trouver `2` mots de passe valides.

??? pouce "Coup de pouce"

    Attention au décalage : la position `1` de l’énoncé correspond à l’indice `0` en Python.

??? pouce "Coup de pouce 2 (début de solution)"

    Calculer deux booléens `p` et `q` (la lettre est-elle à chacune des deux positions ?). « L’un ou l’autre mais pas les deux » s’écrit `p != q` : c’est le *ou exclusif*.

## Approfondissement

!!! encadre "Outil Python : les opérateurs bit à bit (&, |, ^)"

    Sur des entiers, ces opérateurs travaillent chiffre binaire par chiffre binaire : `&` (et), `|` (ou), `^` (ou exclusif). Sur des booléens, ils donnent le même résultat que `and`, `or` et le ou exclusif.

    ```python
    print(6 & 3)          # 110 et 011 -> 010, soit 2
    print(6 | 3)          # 110 ou 011 -> 111, soit 7
    print(6 ^ 3)          # 110 xor 011 -> 101, soit 5
    print(True ^ True)    # False
    print(5 ^ 5)          # 0 : x ^ x vaut toujours 0
    ```

    **Intérêt.** Un seul calcul traite tous les bits à la fois ; le ou exclusif est très utilisé en cryptographie (masque jetable de Vernam, chapitre 10) et pour coder des ensembles de petits entiers.

    **À essayer.** Calculer à la main `12 ^ 10`, puis vérifier avec Python.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 6</span> — Défi : une table de vérité <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-recherche-textuelle-aoc-1-6 }

**But.** Vérifier par un programme que trois écritures du ou exclusif sont équivalentes.

**À quoi ça sert ?** La partie 2 se résume à un ou exclusif entre deux booléens. Savoir l’écrire de plusieurs façons, et le vérifier sur tous les cas, prépare son usage en cryptographie (masque jetable, chapitre 10).

Dresser la table de vérité du ou exclusif. Vérifier que `p != q`, `p ^ q` et `(p or q) and not (p and q)` donnent le même résultat pour les quatre cas, en le faisant afficher par un programme.

??? pouce "Coup de pouce"

    Deux boucles `for p in (False, True)` imbriquées suffisent à parcourir les quatre cas.

## <span class="etiquette">Défi 2</span> Monster Messages

*les messages du satellite — grammaires et récursivité*

<p class="infos-activite">Jour 19</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/12-defi-aoc-2020-19){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-12-defi-aoc-2020-19.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/19 ](https://adventofcode.com/2020/day/19 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (lien ci-dessus) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

!!! encadre "Le défi en bref"

    **Le problème.** On reçoit quelques centaines de messages formés des lettres `a` et `b`, et une liste de règles numérotées qui décrivent ce qu’est un message correct. Les règles s’appuient les unes sur les autres et proposent des alternatives : un même message peut se découper de nombreuses façons. On veut compter les messages corrects ; à la main, explorer tous les découpages est impossible.

    **Ce qu’on réinvestit.** Ce défi prolonge la **recherche textuelle** de ce chapitre : on ne cherche plus un motif fixe dans un texte, mais on vérifie si des messages entiers respectent des règles. La **récursivité** est l’outil naturel, puisque chaque règle est définie à partir d’autres règles ; l’approfondissement 2 réinvestit la **mémoïsation** du chapitre 11 pour éviter de refaire les mêmes calculs.

    **La démarche de la fiche.**

    1.  Comprendre comment les règles s’emboîtent, puis trouver à la main les mots reconnus par de petites règles.

    2.  Lire le fichier : les règles dans un dictionnaire, les messages dans une liste.

    3.  Écrire une fonction récursive qui renvoie toutes les positions où une règle peut s’arrêter : elle décide si un message est valide (partie 1).

    4.  Vérifier que cette fonction résiste aux règles qui s’appellent elles-mêmes (partie 2).

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| rule / sub-rule | règle / sous-règle | to match | correspondre à, être reconnu par |
| pipe (\|) | barre verticale (« ou ») | corrupted | corrompu, abîmé |
| build upon | s’appuyer sur | completely | entièrement |
| loop | boucle | unmatched | non reconnu, en trop |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Arrivé dans une forêt, vous êtes contacté par les elfes : un satellite leur envoie des messages, mais la liaison est mauvaise et beaucoup arrivent abîmés. Pour faire le tri, ils disposent de règles qui décrivent exactement à quoi ressemble un message correct. Il faut leur dire combien de messages sont utilisables.

    **Les données.** Le fichier a deux parties séparées par une ligne vide. D’abord les règles, une par ligne, sous la forme `numéro: définition` (par exemple `2: 4 3 | 3 1`), pas forcément rangées dans l’ordre des numéros. Ensuite les messages reçus, un par ligne, formés uniquement des lettres `a` et `b`.

    **La règle.**

    - Une règle « lettre », écrite entre guillemets comme `"a"`, reconnaît exactement ce caractère.

    - Une règle composée est une suite de numéros : le texte doit se découper en morceaux consécutifs reconnus, dans l’ordre, par ces sous-règles.

    - Le symbole `|` sépare des alternatives : il suffit que l’une d’elles convienne. Les règles s’emboîtent ainsi comme des briques, de la lettre jusqu’à la règle `0`.

    - En partie 1, aucune règle ne fait appel à elle-même, directement ou par l’intermédiaire d’autres règles.

    - Un message est valide si la règle `0` le reconnaît **en entier**, sans caractère en trop.

    **La réponse attendue.** Le nombre de messages valides. Par exemple, avec les règles `0: 1 2 | 2 1`, `1: "a"` et `2: "b"`, la règle `0` reconnaît `ab` et `ba` seulement : parmi les messages `ab`, `ba`, `aba` et `bb`, la réponse serait 2 (`aba` a une lettre en trop).

### <span class="exo-num">Exercice 1</span> — Vérifier sa compréhension <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-recherche-textuelle-aoc-2-1 }

**But.** Repérer les pièges du découpage : choix d’alternative indépendants, alternatives à garder toutes, règles dans le désordre.

**À quoi ça sert ?** Chaque question correspond à une décision de programmation : la deuxième, en particulier, explique pourquoi la fonction de la partie 1 doit renvoyer **toutes** les positions possibles et pas une seule.

1.  Une même règle peut-elle apparaître deux fois dans une définition ? Le choix d’alternative est-il alors forcément le même ?

2.  Devant une règle à deux alternatives, peut-on garder la première qui reconnaît un début du texte et oublier l’autre ?

3.  Les règles sont-elles forcément rangées dans l’ordre des numéros ? Quelle structure de données évite de s’en soucier ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-recherche-textuelle-aoc-2-2 }

**But.** Énumérer les mots reconnus par de petites règles et tester quelques messages.

**À quoi ça sert ?** On construit à la main ce que le programme fera automatiquement : remonter des lettres jusqu’à la règle `0`. Les mots trouvés servent ensuite de tests, et le cas `bbaa` montre le piège du message reconnu seulement en partie.

On considère les règles (inventées) suivantes :

```console
0: 1 2
1: 3 3 | 4
2: 4 3 | 3 1
3: "a"
4: "b"
```

1.  Écrire tous les mots reconnus par la règle `1`, puis par la règle `2`.

2.  En déduire tous les mots reconnus par la règle `0`. Vérification : il y en a `6`.

3.  Parmi `aaab`, `bba`, `baab`, `aba` et `bbaa`, lesquels sont acceptés ? Que se passe-t-il pour `bbaa` ?

## Programmer la partie 1

!!! encadre "Outil Python : strip (nettoyer une ligne lue)"

    Chaque ligne renvoyée par `readlines()` se termine par le caractère de fin de ligne `"\n"` (sauf parfois la dernière). `ligne.strip()` renvoie une copie de la ligne sans les espaces ni les fins de ligne placés au début et à la fin.

    ```python
    ligne = "1721\n"
    print(ligne.strip())                  # 1721
    print(len(ligne), len(ligne.strip())) # 5 4
    ```

    **Intérêt.** Comparer ou découper une ligne sans que la fin de ligne ne gêne : `"abc\n" == "abc"` vaut `False`.

### <span class="exo-num">Exercice 3</span> — Lire le fichier <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-recherche-textuelle-aoc-2-3 }

**But.** Ranger les règles dans un dictionnaire indexé par leur numéro, et les messages dans une liste.

**À quoi ça sert ?** Le dictionnaire donne en une instruction la définition de n’importe quelle règle, quel que soit l’ordre des lignes du fichier : la fonction récursive en aura besoin à chaque appel.

Lire `input.txt` et construire un dictionnaire `regles` : à chaque numéro (une chaîne, par exemple `’2’`), on associe soit la lettre (`’a’`), soit la liste des alternatives, chacune étant une liste de numéros (`[[’4’, ’3’], [’3’, ’1’]]`). Construire aussi la liste `messages`.

??? pouce "Coup de pouce"

    Le fichier se coupe en deux avec `strip()` puis `split("\n\n")`. Pour une règle, `split(": ")` sépare le numéro du reste, puis `split(" | ")` sépare les alternatives. Une règle « lettre » s’écrit `"a"` avec ses guillemets : la lettre est le caractère d’indice 1.

!!! encadre "Méthode : reconnaître une règle « lettre »"

    Dans le dictionnaire `regles`, une valeur est soit une chaîne (une lettre), soit une liste d’alternatives. Dans ce défi, les seules lettres sont `a` et `b` : une règle est une règle « lettre » exactement quand elle vaut `"a"` ou `"b"`. Comparer une liste à une chaîne avec `==` ne provoque pas d’erreur : le résultat est simplement `False`.

    ```python
    regles = {"3": "a", "2": [["4", "3"], ["3", "1"]]}
    print(regles["3"] == "a" or regles["3"] == "b")   # True : regle "lettre"
    print(regles["2"] == "a" or regles["2"] == "b")   # False : alternatives
    ```

    **Intérêt.** Cela évite de stocker une information supplémentaire (« type de règle ») : la valeur elle-même dit de quoi il s’agit. Question : que vaut `["a"] == "a"` ? Pourquoi ?

### <span class="exo-num">Exercice 4</span> — Reconnaître un message <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-recherche-textuelle-aoc-2-4 }

**But.** Écrire la fonction récursive `fins`, qui renvoie toutes les positions où peut s’arrêter un morceau reconnu par une règle.

**À quoi ça sert ?** C’est le cœur du défi : un message est valide quand l’une de ces positions est sa longueur, et compter les messages valides donne la réponse de la partie 1. Renvoyer toutes les fins possibles évite d’avoir à deviner la bonne alternative.

Écrire une fonction récursive `fins(regles, num, message, i)` qui renvoie la **liste des positions** où peut se terminer un morceau du message commençant à l’indice `i` et reconnu par la règle `num` (lire l’encadré). Un message est accepté si `len(message)` figure dans `fins(regles, ’0’, message, 0)`. Tester sur l’exemple, puis compter les messages acceptés.

??? pouce "Coup de pouce"

    Cas de base : une règle « lettre » renvoie `[i + 1]` si `message[i]` est cette lettre (et `i` dans les bornes), et `[]` sinon.

??? pouce "Coup de pouce 2 (début de solution)"

    Pour une alternative `[’4’, ’3’]` : partir de `positions = [i]` ; pour chaque sous-règle, remplacer `positions` par la liste de toutes les fins obtenues depuis chacune des positions. Les résultats des différentes alternatives sont mis bout à bout.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    **Ce qui change.** Les elfes s’aperçoivent que deux de leurs règles étaient fausses et vous envoient les bonnes : `8: 42 | 42 8` et `11: 42 31 | 42 11 31`. Ces deux règles remplacent les anciennes règles `8` et `11` ; toutes les autres sont inchangées.

    **La nouvelle règle.**

    - Ces règles font appel à elles-mêmes : le nombre de mots qu’elles reconnaissent devient infini.

    - La règle `8` reconnaît une ou plusieurs répétitions de la règle `42`.

    - La règle `11` reconnaît $k$ fois la règle `42` suivie de $k$ fois la règle `31`, avec le même $k \geq 1$ des deux côtés. Par exemple, si `42` reconnaissait `a` et `31` reconnaissait `b`, la règle `11` reconnaîtrait `ab`, `aabb`, `aaabbb`… mais pas `aab`.

    - Un message est toujours valide si la règle `0` le reconnaît en entier.

    **La réponse attendue.** Le nouveau nombre de messages valides.

### <span class="exo-num">Exercice 5</span> — Des règles récursives <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-recherche-textuelle-aoc-2-5 }

**But.** Remplacer les deux règles et vérifier que la fonction `fins` donne encore la bonne réponse.

**À quoi ça sert ?** Une fonction récursive bien écrite n’a pas besoin de savoir à l’avance combien de fois une règle se répète : comprendre pourquoi elle s’arrête toujours, c’est s’assurer que la réponse de la partie 2 est juste.

Deux règles sont remplacées par des règles qui **s’appellent elles-mêmes**. Modifier le dictionnaire comme indiqué et relancer le comptage. Votre fonction `fins` fonctionne-t-elle encore ? Pourquoi ne boucle-t-elle pas indéfiniment ?

??? pouce "Coup de pouce"

    Observer où apparaît le numéro de la règle dans sa propre définition : jamais en première position. Avant chaque appel récursif, au moins une lettre a donc été consommée.

Exemple de test (inventé ; en partie 2, on remplace les règles `8` et `11` comme dans le résumé) :

```console
0: 8 11
8: 42
11: 42 31
42: 1 1 | 2 1
31: 1 2 | 2 2
1: "a"
2: "b"

aabaab
aaaaab
aaaabaabbb
aaabab
baaaaaab
abaaab
babaabab
```

Avec les règles d’origine, on doit compter `2` messages ; avec les règles modifiées, `4`.

## Pour y arriver : grammaires et récursivité <span class="horsprog">au-delà du programme</span>

!!! encadre "Grammaire, expression régulière et positions de fin"

    **Grammaire.** Les règles de l’énoncé forment une *grammaire* : chaque règle décrit un ensemble de mots à partir d’autres règles, comme « une phrase est un groupe nominal suivi d’un verbe ». On dit qu’un mot est *reconnu* s’il peut être obtenu en partant de la règle `0`.

    **Pourquoi pas une expression régulière ?** En partie 1, on peut remplacer chaque numéro par sa définition jusqu’à n’avoir que des lettres et obtenir une expression régulière : sur l’exemple du défi, la règle `0` devient `(aa|b)(ba|a(aa|b))`. Mais si une règle contient son propre numéro, ce remplacement ne s’arrête jamais. Pire : une règle du type « `X` suivi de `Y` autant de fois que de `X` » (même nombre des deux côtés) ne peut *pas du tout* s’écrire comme une expression régulière, car celles-ci ne savent pas compter.

    **L’idée de la fonction `fins`.** Plutôt que de deviner *où* s’arrête la partie reconnue par une règle, on renvoie *toutes* les possibilités. Sur l’exemple du défi, avec le mot `bbaa` : la règle `1` depuis l’indice `0` renvoie `[1]` (la lettre `b`) ; la règle `2` depuis l’indice `1` renvoie `[3]` (le morceau `ba`). Donc `fins(regles, ’0’, "bbaa", 0)` vaut `[3]` : le mot n’est pas reconnu en entier car $3 \neq 4$. Quand une règle a plusieurs alternatives, la liste peut contenir plusieurs positions ; une liste vide signifie « échec ».

## Approfondissement

!!! encadre "Outil Python : les ensembles (set)"

    Un **ensemble** est une collection sans doublon et sans ordre. On l’écrit entre accolades (`set()` pour l’ensemble vide), on peut le construire par compréhension comme une liste, et lui ajouter un élément avec `add`. La **réunion** `a | b` et l’**intersection** `a & b` construisent un nouvel ensemble (voir aussi l’encadré du défi *Crab Combat*, chapitre 4).

    ```python
    debuts = {"a", "b"}
    fins = {"a", "ab"}
    mots = {d + f for d in debuts for f in fins}   # tous les "collages"
    print(mots)                     # {'aa', 'aab', 'ba', 'bab'} (ordre quelconque)
    print("ba" in mots)             # True : test d'appartenance tres rapide
    mots = mots | {"bb", "aa"}     # reunion : "aa" deja present, pas de doublon
    print(len(mots))                # 5
    print(mots & {"bb", "ab"})      # {'bb'} : intersection
    ```

    **Intérêt.** Le test `x in ensemble` prend un temps qui ne dépend pas de la taille de l’ensemble (contrairement à une liste, qu’il faut parcourir), et les doublons disparaissent d’eux-mêmes. Question : combien d’éléments a `{d + f for d in "ab" for f in "ab"}` ?

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Approfondissement 1 : une méthode par blocs, propre aux données <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-recherche-textuelle-aoc-2-6 }

**But.** Résoudre la partie 2 autrement, en exploitant une particularité des vraies données.

**À quoi ça sert ?** Observer les données avant de programmer peut ramener un problème difficile (une grammaire récursive) à un simple découpage en blocs de même longueur ; on compare ensuite cette méthode, rapide mais spécialisée, à la méthode générale.

Dans les vraies données, la règle `0` est `8 11`, et les règles `42` et `31` ne contiennent pas de cycle : chacune reconnaît un ensemble **fini** de mots, et ces mots ont tous la même longueur.

1.  À la main, sur l’exemple de test de la partie 2 : écrire l’ensemble des mots reconnus par `42` et par `31`. Découper `aaaabaabbb` et `baaaaaab` en blocs de deux lettres et dire, pour chaque bloc, à quelle règle il appartient.

2.  Avec la règle `0: 8 11` modifiée, montrer qu’un message est valide si et seulement s’il s’écrit « $p$ blocs de `42` suivis de $q$ blocs de `31` » avec $p > q \geq 1$. Et en partie 1 ?

3.  Écrire une fonction récursive `mots(regles, num)` qui renvoie l’ensemble des mots reconnus par une règle sans cycle.

    ??? pouce "Coup de pouce"

        Pour une alternative, partir de l’ensemble `{""}` (le mot vide) et, pour chaque sous-règle, coller à chaque début chacun des mots de la sous-règle.

    ??? pouce "Coup de pouce 2 (début de solution)"

        `possibles = {debut + fin for debut in possibles for fin in mots(regles, sous_regle)}` ; les mots obtenus pour les différentes alternatives sont réunis dans l’ensemble résultat : `resultat = resultat | possibles`.

4.  Écrire `valide_par_blocs(message, m42, m31)` et retrouver le résultat de la partie 2. Pourquoi faut-il que les deux ensembles n’aient aucun mot commun ? Le vérifier sur vos données (que doit valoir `m42 & m31` ?).

    ??? pouce "Coup de pouce"

        Compter le nombre `p` de blocs de tête qui sont dans `m42` ; tous les blocs restants doivent être dans `m31` (un booléen drapeau, comme dans le défi *Handy Haversacks*).

5.  Comparer avec la fonction `fins` : vitesse, et généralité (que se passe-t-il si l’on change la règle `0` ?).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 2 : mémoïser la fonction `fins` <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-recherche-textuelle-aoc-2-7 }

**But.** Éviter de recalculer plusieurs fois `fins` pour une même règle et une même position.

**À quoi ça sert ?** C’est la mémoïsation du chapitre 11 appliquée à un nouveau problème : elle borne le nombre de calculs différents et rend la méthode générale sûre même sur des messages longs.

Pour un message donné, la fonction `fins` peut être appelée plusieurs fois avec la même règle et la même position `i`.

1.  Sur l’exemple de test de la partie 2, avec les règles modifiées, expliquer pourquoi le calcul de `fins(regles, ’8’, message, 0)` appelle deux fois `fins(regles, ’42’, message, 0)`. Que se passe-t-il ensuite à la position 2, à la position 4…?

2.  Écrire `fins_memo(regles, num, message, i, memo)` qui range chaque résultat dans le dictionnaire `memo`, de clé `(num, i)`, et le réutilise s’il est déjà calculé. Vérifier qu’on obtient les mêmes réponses.

    ??? pouce "Coup de pouce"

        Le dictionnaire doit être **vide au début de chaque message** : un même couple `(num, i)` ne donne pas le même résultat pour deux messages différents.

3.  Combien de couples `(num, i)` différents au plus pour un message de longueur $n$ et $R$ règles ? Que peut-on en dire sur la complexité ?

!!! encadre "Un peu d’histoire : Chomsky, Backus, Naur et les grammaires"

    **Un linguiste.** En 1956, le linguiste américain **Noam Chomsky** (né en 1928) publie *Three Models for the Description of Language*. Il y compare plusieurs façons de décrire une langue par des règles, du plus simple au plus puissant. Il montre que les modèles les plus simples, qui lisent une phrase de gauche à droite sans rien retenir d’autre qu’un « état » parmi un nombre fini, ne suffisent pas pour l’anglais : les constructions emboîtées comme « *if* … *then* … », qui peuvent contenir d’autres « *if* … *then* … », demandent de **compter**. C’est exactement la règle `11` de la partie 2 ($k$ fois `42` puis $k$ fois `31`), qu’aucune expression régulière ne sait décrire.

    **Deux informaticiens.** En 1959, à la première conférence internationale sur le traitement de l’information (Unesco, Paris), **John Backus**, déjà l’inventeur du langage Fortran chez IBM, présente une notation pour décrire la syntaxe du nouveau langage ALGOL : chaque construction est définie par des règles qui peuvent se citer elles-mêmes, avec des alternatives séparées par une barre. Le Danois **Peter Naur** l’améliore et l’utilise pour rédiger le rapport ALGOL 60 (1960). En 1964, Donald Knuth propose d’appeler cette notation **BNF** (*Backus–Naur Form*). Les règles de l’énoncé, avec leurs `|` et leurs appels récursifs, en sont une version miniature.

    **Et aujourd’hui.** La syntaxe de presque tous les langages de programmation est décrite par une grammaire de ce type ; celle de Python figure dans sa documentation officielle, et c’est à partir d’elle que l’interpréteur vérifie vos programmes avant de les exécuter (le message `SyntaxError` vient de là). Backus a reçu le prix Turing en 1977, Naur en 2005.

    *Sources :* N. Chomsky, « Three Models for the Description of Language », *IRE Transactions on Information Theory*, 2 (1956), p. 113–124 ; P. Naur (éd.), « Report on the Algorithmic Language ALGOL 60 », *Communications of the ACM*, 3 (1960) ; D. Knuth, « Backus Normal Form vs. Backus Naur Form », *Communications of the ACM*, 7 (1964) ; site de l’ACM (lauréats du prix Turing).
