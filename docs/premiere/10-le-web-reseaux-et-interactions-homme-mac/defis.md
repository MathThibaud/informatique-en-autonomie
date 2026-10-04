# Défis Advent of Code

<p class="sous-titre">Le Web : réseaux et interactions homme-machine</p>

## <span class="etiquette">Défi 1</span> Tuning Trouble

*le signal radio — fenêtre glissante sur une chaîne*

<p class="infos-activite">Jour 6</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/10-defi-aoc-2022-06){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-10-defi-aoc-2022-06.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2022/day/6 ](https://adventofcode.com/2022/day/6 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/10-defi-aoc-2022-06>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| datastream | flux de données | buffer | tampon, mémoire de réception |
| marker | marqueur | start-of-packet | début de paquet |
| all different | tous différents | characters processed | caractères traités |
| received | reçu | start-of-message | début de message |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Un elfe vous confie un petit appareil de communication, qui doit d’abord se caler sur le signal radio des elfes. Le signal arrive comme une suite de lettres reçues l’une après l’autre ; le fichier contient tout ce flux sur une seule ligne. Le début d’un paquet de données est signalé par un groupe de lettres consécutives toutes différentes, qu’il faut repérer.

    **Ce qu’il faut faire.**

    - On lit les caractères de gauche à droite. On cherche le premier endroit où les **4 derniers caractères lus** sont tous différents : c’est le marqueur de début de paquet.

    - Réponse : le nombre de caractères lus depuis le début jusqu’au dernier caractère de ce marqueur, positions comptées à partir de 1. Autrement dit, si le marqueur occupe les caractères 3 à 6, la réponse est 6.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-aoc-1-1 }

Après lecture du résumé (et de l’énoncé), vérifier sa compréhension sur ces cas particuliers :

1.  Peut-on obtenir une réponse plus petite que 4 ?

2.  Pour `abcd...`, quelle est la réponse ? et pour `aaaabcd` ?

3.  Si la fenêtre `flux[i:i+4]` convient, faut-il répondre `i`, `i + 4` ou `i + 3` ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-aoc-1-2 }

Pour chacun des flux (inventés) suivants, trouver la réponse de la partie 1 :

```console
aabacbdeffgh
nsinsinsiabcdefghijklmnop
```

Vérification : on doit obtenir `7` pour le premier, `10` pour le second. Écrire les fenêtres de 4 caractères examinées l’une après l’autre pour le premier flux.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire le fichier <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-aoc-1-3 }

Le fichier ne contient qu’une ligne : on le lit d’un coup.

```python
fichier = open("input.txt", encoding="utf-8")
flux = fichier.read().strip()   # toute la ligne, sans le retour final
fichier.close()
```

Afficher la longueur de `flux` et ses 10 premiers caractères (`flux[0:10]`).

### <span class="exo-num">Exercice 4</span> — Des caractères tous différents ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-aoc-1-4 }

Écrire une fonction `tous_differents(morceau)` qui renvoie `True` si la chaîne `morceau` ne contient pas deux fois le même caractère. Tester avec `"acbd"` et `"abac"`.

??? pouce "Coup de pouce"

    Pour chaque indice `i`, regarder si `morceau[i]` apparaît dans la suite de la chaîne, `morceau[i+1:]`, avec l’opérateur `in`.

### <span class="exo-num">Exercice 5</span> — Faire glisser la fenêtre <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-aoc-1-5 }

Écrire une fonction `position_marqueur(flux)` qui renvoie la réponse de la partie 1. Vérifier les deux valeurs de l’exemple, puis lancer sur vos données.

??? pouce "Coup de pouce"

    La fenêtre qui se termine juste avant l’indice `fin` est la tranche `flux[fin-4:fin]`. Le premier `fin` possible est `4`.

??? pouce "Coup de pouce 2 (début de solution)"

    Une boucle `while` qui avance `fin` de 1 tant que la fenêtre `flux[fin-4:fin]` n’est pas formée de caractères tous différents. À la sortie, `fin` est exactement le nombre de caractères traités.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    L’appareil doit aussi repérer le début des messages, signalé par un marqueur plus long. Même question, mais avec **14** caractères consécutifs tous différents au lieu de 4. Réponse : le nombre de caractères lus jusqu’à la fin de ce premier groupe de 14.

### <span class="exo-num">Exercice 6</span> — Généraliser <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-aoc-1-6 }

Ajouter un paramètre : `position_marqueur(flux, taille)`. La partie 1 correspond à `taille = 4`. Répondre à la partie 2. Sur le second flux de l’exemple, on doit trouver `23`.

??? pouce "Coup de pouce"

    Remplacer chaque `4` écrit « en dur » par `taille`. Si la fonction était bien écrite, la partie 2 ne demande que de changer l’appel.

## Approfondissement

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

    *À essayer.* Que vaut `len(set("abac"))` ? Comparer avec `len("abac")`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : tous différents avec un ensemble <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-aoc-1-7 }

1.  Pour une fenêtre de taille $k$, combien de comparaisons de caractères `tous_differents` fait-elle au pire ? Calculer pour $k = 4$ et $k = 14$.

    ??? pouce "Coup de pouce"

        Le premier caractère est comparé aux $k - 1$ suivants, le deuxième aux $k - 2$ suivants, etc.

2.  Écrire `tous_differents_ens(morceau)` en une ligne, avec un ensemble, et vérifier qu’elle donne les mêmes réponses.

    ??? pouce "Coup de pouce"

        Les caractères sont tous différents si et seulement si l’ensemble des caractères a la même taille que la fenêtre.

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

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 8</span> — Approfondissement 2 : ne pas tout recompter <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-aoc-1-8 }

Quand la fenêtre glisse d’un cran, un seul caractère entre et un seul sort : les autres ne changent pas.

1.  À la main, sur `aabacbdeffgh` avec $k = 4$ : écrire, pour chaque glissement, le caractère qui entre et celui qui sort.

2.  Écrire `position_rapide(flux, taille)` qui tient à jour une liste de 26 compteurs (un par lettre) et le nombre de lettres différentes présentes dans la fenêtre. Vérifier qu’elle redonne les réponses des parties 1 et 2.

    ??? pouce "Coup de pouce"

        Quand un caractère entre, ajouter 1 à son compteur ; si ce compteur passe de 0 à 1, une lettre différente de plus est présente.

    ??? pouce "Coup de pouce 2 (début de solution)"

        Quand un caractère sort (celui d’indice `i - taille`), retirer 1 à son compteur ; s’il retombe à 0, une lettre différente de moins. On a trouvé le marqueur quand le nombre de lettres différentes vaut `taille`.

3.  Combien d’opérations pour un flux de $n$ caractères ? Cela dépend-il encore de $k$ ?

## <span class="etiquette">Défi 2</span> Mull It Over

*la mémoire corrompue — rechercher des motifs dans un texte*

<p class="infos-activite">Jour 3</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/10-defi-aoc-2024-03){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-10-defi-aoc-2024-03.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2024/day/3 ](https://adventofcode.com/2024/day/3 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/10-defi-aoc-2024-03>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|             |                 |         |            |
|:------------|:----------------|:--------|:-----------|
| corrupted   | corrompu, abîmé | memory  | mémoire    |
| instruction | instruction     | digit   | chiffre    |
| invalid     | invalide        | ignore  | ignorer    |
| enable      | activer         | disable | désactiver |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** L’ordinateur d’un magasin de location de luges est en panne : sa mémoire a été abîmée et ressemble à un long texte plein de caractères au hasard. Quelques instructions de multiplication ont survécu au milieu de ce désordre. Le fichier contient cette mémoire, parfois sur plusieurs lignes, et il faut retrouver ce que le programme calculait.

    **Ce qu’il faut faire.**

    - Une instruction valide s’écrit **exactement** `mul(X,Y)`, où `X` et `Y` sont des entiers de **1 à 3 chiffres**, sans espace ni autre caractère. Elle calcule `X * Y`.

    - Tout motif qui ressemble mais n’est pas exact (espace, crochet, 4 chiffres, nombre manquant…) est un débris : on l’ignore.

    - Réponse : la somme des produits de toutes les instructions valides.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-aoc-2-1 }

Après lecture du résumé (et de l’énoncé), vérifier sa compréhension sur ces cas particuliers :

1.  `mul(3,4)` écrit sur deux lignes du fichier (retour à la ligne au milieu) compte-t-il ?

2.  Le texte `mul(2,3)mul(4,5)` contient-il un ou deux motifs valides ?

3.  `mul(07,2)` est-il valide d’après le résumé ? Et `mul(,2)` ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-aoc-2-2 }

On considère la mémoire (inventée) suivante, sur une seule ligne :

```console
?mul(3,4)xx mul(10,2]don't()mul(5,5)!do()^mul(6,7)mul ( 1,1)mul(1234,2)
```

Entourer les instructions valides. Vérification : on doit obtenir `79`. Pourquoi `mul(10,2]` et `mul(1234,2)` ne comptent-ils pas ?

## Programmer la partie 1, sans outil spécial

### <span class="exo-num">Exercice 3</span> — Lire le fichier <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-aoc-2-3 }

Le fichier peut contenir plusieurs lignes ; on le lit d’un seul bloc, comme une longue chaîne :

```python
fichier = open("input.txt", encoding="utf-8")
texte = fichier.read()
fichier.close()
```

Afficher `len(texte)` et les 60 premiers caractères.

!!! encadre "Outil Python : reconnaître un chiffre (isdigit)"

    La méthode `isdigit` d’une chaîne renvoie `True` si la chaîne n’est pas vide et ne contient que des chiffres.

    ```python
    print("7".isdigit())       # True
    print("x".isdigit())       # False
    print("12".isdigit())      # True : tous les caracteres sont des chiffres
    print("1a".isdigit())      # False
    print("".isdigit())        # False : chaine vide
    ```

    **Intérêt.** Elle remplace un test du genre `c in "0123456789"`, plus long à écrire.

    *À essayer.* Que renvoie `"-3".isdigit()` ? Pourquoi ?

### <span class="exo-num">Exercice 4</span> — Lire un nombre <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-aoc-2-4 }

Écrire une fonction `lire_nombre(texte, i)` qui lit les chiffres consécutifs à partir de l’indice `i` et renvoie le couple `(chaine_de_chiffres, indice_suivant)`. Par exemple `lire_nombre("ab12,7", 2)` renvoie `("12", 4)` et `lire_nombre("ab12,7", 0)` renvoie `("", 0)`.

??? pouce "Coup de pouce"

    Une boucle `while` qui avance `i` tant que `i < len(texte)` **et** que `texte[i]` est un chiffre (méthode `isdigit()`). L’ordre des deux conditions compte !

### <span class="exo-num">Exercice 5</span> — Reconnaître une instruction <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-aoc-2-5 }

Écrire une fonction `produit_en(texte, i)` qui renvoie le produit des deux nombres si une instruction valide commence à l’indice `i`, et `0` sinon. Puis parcourir tous les indices du texte et faire la somme. Vérifier `79` sur l’exemple.

??? pouce "Coup de pouce"

    Vérifier dans l’ordre : `texte[i:i+4] == "mul("` ; puis un premier nombre de 1 à 3 chiffres ; puis une virgule ; puis un second nombre de 1 à 3 chiffres ; puis une parenthèse fermante. Au premier échec, renvoyer `0`.

??? pouce "Coup de pouce 2 (début de solution)"

    `a, j = lire_nombre(texte, i + 4)` ; tester `1 <= len(a) <= 3` puis `texte[j] == ","` ; ensuite `b, k = lire_nombre(texte, j + 1)`, tester sa longueur et `texte[k] == ")"`. Attention à ne pas dépasser la fin du texte : une tranche `texte[j:j+1]` ne provoque jamais d’erreur.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    En regardant mieux, la mémoire contient aussi des interrupteurs. L’instruction `do()` active les `mul` qui suivent, `don’t()` les désactive ; seule la plus récente des deux compte, et au début du texte les `mul` sont actifs. Réponse : la somme des produits des seuls `mul` valides et actifs.

### <span class="exo-num">Exercice 6</span> — Un interrupteur <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-aoc-2-6 }

Ajouter une variable booléenne `actif`. Pendant le parcours des indices, mettre à jour `actif` lorsque l’on rencontre les instructions décrites dans la partie 2, et n’ajouter un produit que si `actif` vaut `True`. Sur l’exemple, on doit trouver `54`.

??? pouce "Coup de pouce"

    Relire l’énoncé : quelle est la valeur de `actif` au tout début ? Tester `texte[i:i+4] == "do()"` et `texte[i:i+7] == "don’t()"`.

## Approfondissement

!!! encadre "Outil Python : les expressions régulières (re) au-delà du programme"

    Une **expression régulière** (*regex*) décrit un *motif* de texte. Le module `re` de Python sait trouver toutes les portions d’un texte qui respectent un motif. Quelques briques : `\d` = un chiffre ; `\d{1,3}` = de 1 à 3 chiffres ; `\(` = une vraie parenthèse ; des parenthèses *sans* barre délimitent un morceau à récupérer ; `A|B` = le motif `A` ou le motif `B`.

    ```python
    import re
    print(re.findall(r"a(\d)", "a1 b2 a3"))      # ['1', '3'] : les morceaux recuperes
    for m in re.finditer(r"a(\d)|stop", "a1 stop a3"):
        print(m.group(), m.group(1))             # a1 1, puis stop None, puis a3 3
    ```

    Le `r` devant la chaîne évite que Python interprète lui-même les barres obliques inverses. `findall` renvoie les morceaux récupérés ; `finditer` parcourt les correspondances dans l’ordre du texte : `m.group()` est le texte trouvé en entier, `m.group(1)` le premier morceau récupéré.

    **Intérêt.** Un motif d’une ligne remplace une fonction de reconnaissance de quinze lignes, et le module est optimisé.

    *À essayer.* Que renvoie `re.findall(r"\d{2}", "1 22 333")` ?

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : la partie 1 en trois lignes <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-aoc-2-7 }

Écrire un motif qui reconnaît exactement les instructions valides de la partie 1, en récupérant les deux nombres. Avec `re.findall`, refaire la partie 1 et comparer avec votre première version.

??? pouce "Coup de pouce"

    `re.findall` renvoie une liste de couples de chaînes lorsque le motif contient deux morceaux entre parenthèses. Le motif commence par `mul\(`.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 8</span> — Approfondissement 2 : la partie 2 avec `finditer` <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-aoc-2-8 }

1.  Écrire un motif qui reconnaît une instruction `mul` valide **ou** `do()` **ou** `don’t()`.

2.  Avec `re.finditer`, parcourir les correspondances dans l’ordre et appliquer l’interrupteur de la partie 2. Vérifier `54` sur l’exemple.

    ??? pouce "Coup de pouce"

        Tester `m.group()` : s’il vaut `"do()"` ou `"don’t()"`, mettre à jour `actif` ; sinon, c’est un `mul` et ses nombres sont `m.group(1)` et `m.group(2)`.
