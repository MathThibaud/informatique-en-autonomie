# Défis Advent of Code

<p class="sous-titre">Diviser pour régner</p>

## <span class="etiquette">Défi 1</span> Report Repair

*la note de frais — parcours de listes et complexité*

<p class="infos-activite">Jour 1</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/05-defi-aoc-2020-01){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-05-defi-aoc-2020-01.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/1 ](https://adventofcode.com/2020/day/1 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/05-defi-aoc-2020-01>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

*Ce défi fait comparer plusieurs méthodes et leur coût, comme dans ce chapitre : double boucle, ensemble, et tri suivi d’un parcours par les deux bouts.*

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| expense report | note de frais | entry | ligne, valeur du fichier |
| accounting | comptabilité | sum to | avoir pour somme |
| fix up | corriger | multiply | multiplier |
| puzzle input | vos données (fichier personnel) | star | étoile (une par partie réussie) |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Avant de partir en vacances, vous devez régler un dernier problème : les elfes de la comptabilité ont une note de frais qui ne tombe pas juste et vous demandent de les aider à la corriger. Le fichier de données est cette note de frais : chaque ligne est une dépense, c’est-à-dire un entier positif.

    **Ce qu’il faut faire.**

    - Parmi toutes les dépenses, exactement **deux** lignes ont des valeurs dont la somme vaut **2020**. Autrement dit, il faut trouver la seule paire de lignes différentes qui « complètent » 2020.

    - La réponse à donner sur le site est le **produit** de ces deux valeurs.

### <span class="exo-num">Exercice 1</span> — Vérifier sa compréhension <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-diviser-pour-regner-aoc-1-1 }

1.  Si le fichier contient une seule fois la valeur `1010`, peut-elle former la paire avec elle-même ?

2.  L’ordre des lignes dans le fichier a-t-il une importance pour la réponse ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-diviser-pour-regner-aoc-1-2 }

On considère le fichier (inventé) suivant :

```console
1010
812
1500
1208
33
487
```

Trouver à la main la réponse attendue. Vérification : on doit obtenir `980896`. Pourquoi la ligne `1010` ne donne-t-elle pas de solution à elle seule ?

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire le fichier <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-diviser-pour-regner-aoc-1-3 }

Écrire les lignes qui lisent `input.txt` et construisent la liste `nombres` des entiers qu’il contient. Afficher sa longueur pour vérifier.

### <span class="exo-num">Exercice 4</span> — Une première solution <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-diviser-pour-regner-aoc-1-4 }

Écrire une fonction `paire_2020(nombres)` qui renvoie le produit des deux valeurs recherchées. Tester sur l’exemple de la fiche, puis sur vos données.

??? pouce "Coup de pouce"

    Deux boucles imbriquées sur les **indices** `i` et `j`, avec `j > i` pour ne jamais prendre deux fois la même ligne.

### <span class="exo-num">Exercice 5</span> — Combien d’opérations ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-diviser-pour-regner-aoc-1-5 }

Le fichier contient environ $200$ nombres. Combien de paires la fonction précédente examine-t-elle au pire ? Quelle est sa complexité en fonction de $n$ ?

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Les elfes sont ravis, mais il leur reste une ancienne note de frais à vérifier selon une autre règle. Même fichier : il faut cette fois trouver les **trois** lignes différentes dont les valeurs ont pour somme 2020, et donner le produit de ces trois valeurs.

### <span class="exo-num">Exercice 6</span> — La partie 2 <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-diviser-pour-regner-aoc-1-6 }

Adapter le programme pour répondre à la nouvelle question. Sur l’exemple de la fiche, on doit trouver `24106500`.

??? pouce "Coup de pouce"

    Une boucle de plus. Combien de triplets pour $n = 200$ ? C’est encore rapide.

## Approfondissement

!!! encadre "Outil Python : les ensembles (set)"

    Un **ensemble** est une collection **sans doublon** et **sans ordre** : on ne peut pas y accéder par un indice, on peut seulement ajouter, retirer, et demander si un élément y est.

    ```python
    vus = set()              # ensemble vide (attention : {} est un dictionnaire vide)
    vus.add(812)             # ajout ; ajouter une valeur deja presente ne change rien
    vus.add(1208)
    pairs = {2, 4, 6}        # ensemble ecrit directement
    print(812 in vus)        # True : test d'appartenance
    print(len(vus))          # 2
    vus.remove(812)          # retrait (erreur si l'element est absent)
    for x in pairs:          # parcours possible, mais dans un ordre quelconque
        print(x)
    ```

    **Intérêt.** Avec une liste, `x in liste` compare `x` à chaque élément l’un après l’autre : jusqu’à $n$ comparaisons. Un ensemble range ses éléments selon une valeur calculée à partir d’eux (une *fonction de hachage*, le même principe que les clés d’un dictionnaire) : Python va directement à l’endroit où `x` devrait se trouver. Le test `x in ensemble` prend donc un temps qui **ne dépend pas** du nombre d’éléments (on dit en **temps constant**, en moyenne). Sur un million d’éléments, la différence est énorme.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : une seule boucle grâce à un ensemble <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-diviser-pour-regner-aoc-1-7 }

1.  Recopier puis exécuter le code de l’encadré. Que se passe-t-il si l’on ajoute deux fois `1208` ?

2.  Écrire `paire_rapide(nombres)` qui résout la partie 1 avec une **seule** boucle et un ensemble `vus`. Quelle est sa complexité ?

    ??? pouce "Coup de pouce"

        Pour chaque nombre `x`, la seule valeur qui le complète est `2020 - x`. Il suffit de savoir si on l’a déjà rencontrée.

    ??? pouce "Coup de pouce 2 (début de solution)"

        On parcourt les nombres un par un ; **avant** d’ajouter `x` à l’ensemble `vus`, on regarde si `2020 - x` y est déjà. Tester avant d’ajouter évite d’utiliser deux fois la même ligne.

3.  En déduire une solution de la partie 2 en $O(n^2)$ au lieu de $O(n^3)$.

    ??? pouce "Coup de pouce"

        Généraliser la fonction avec un paramètre `cible` : pour chaque `x`, chercher une paire de somme `2020 - x` parmi les nombres **suivants**.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Approfondissement 2 : trier puis rapprocher deux indices <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-diviser-pour-regner-aoc-1-8 }

Une autre idée, sans ensemble, réinvestit le **tri** vu en Première. On trie la liste, puis on place un indice `g` au début et un indice `d` à la fin.

1.  Sur la liste triée `[33, 487, 812, 1010, 1208, 1500]`, on a `g = 0` et `d = 5` : la somme vaut $33 + 1500 = 1533$, trop petite. Faut-il avancer `g` ou reculer `d` ? Justifier, puis dérouler la méthode à la main jusqu’à trouver la paire.

2.  Écrire `paire_triee(nombres, cible)` qui applique cette méthode (on travaille sur une copie triée, par exemple `sorted(nombres)`) et renvoie le produit, ou `None` s’il n’y a pas de paire.

    ??? pouce "Coup de pouce"

        Tant que `g < d` : si la somme est trop petite, la seule façon de l’augmenter est d’avancer `g` ; si elle est trop grande, reculer `d`.

    ??? pouce "Coup de pouce 2 (début de solution)"

        Si `t[g] + t[d] < cible`, alors `t[g]` associé à n’importe quel élément situé avant `d` donne aussi une somme trop petite : `t[g]` ne peut faire partie d’aucune paire, on peut l’écarter.

3.  Quelle est la complexité totale (tri compris) ? Comparer avec les deux méthodes précédentes.

4.  Utiliser `paire_triee` pour résoudre la partie 2 en $O(n^2)$, sans ensemble.

## <span class="etiquette">Défi 2</span> Encoding Error

*la faille du chiffrement — fenêtre glissante et complexité*

<p class="infos-activite">Jour 9</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/05-defi-aoc-2020-09){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-05-defi-aoc-2020-09.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/9 ](https://adventofcode.com/2020/day/9 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/05-defi-aoc-2020-09>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|                |                           |                 |                   |
|:---------------|:--------------------------|:----------------|:------------------|
| preamble       | préambule                 | previous        | précédent         |
| sum of any two | somme de deux quelconques | different       | différent         |
| weakness       | faiblesse, faille         | valid / invalid | valide / invalide |
| contiguous set | suite contiguë            | at least two    | au moins deux     |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Le héros branche son ordinateur sur une prise de données de l’avion. Il en sort une longue suite de nombres (le fichier, un entier par ligne), chiffrée avec un vieux procédé qui a une faille. Dans ce procédé, chaque nombre doit pouvoir s’obtenir à partir des nombres reçus juste avant lui : un nombre qui ne le peut pas trahit l’erreur.

    **Ce qu’il faut faire.**

    - Les 25 premiers nombres forment le *préambule* (le petit exemple de l’énoncé en utilise 5). Ils ne sont pas testés.

    - Chaque nombre suivant doit être la somme de deux nombres de **valeurs différentes** pris parmi les 25 qui le précèdent immédiatement. Autrement dit, on regarde une fenêtre de 25 nombres qui glisse d’un cran à chaque nouveau nombre.

    - Il faut renvoyer le premier nombre qui ne respecte pas la règle.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-diviser-pour-regner-aoc-2-1 }

Après lecture de l’énoncé et du résumé, vérifier sa compréhension :

1.  La fenêtre contient `3 7 10 7 2`. Le nombre suivant `14` est-il valide ?

2.  Avec un préambule de longueur $p$, quels indices forment la fenêtre du nombre d’indice $i$ ?

3.  La paire peut-elle utiliser un nombre sorti de la fenêtre ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-diviser-pour-regner-aoc-2-2 }

On considère la liste (inventée) suivante, avec un préambule de longueur $5$ :

```console
6  3  7  11  1  13  24  8  25  33  37  62  70  58  22
```

Vérifier à la main les nombres situés après le préambule, en écrivant à chaque fois la fenêtre des 5 nombres précédents et une paire qui convient. Vérification : le premier nombre invalide est `22`.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Somme de deux <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-diviser-pour-regner-aoc-2-3 }

Écrire une fonction `somme_de_deux(fenetre, cible)` qui renvoie `True` si deux éléments de la liste `fenetre` ont pour somme `cible`, en respectant la règle des valeurs différentes. L’essayer avec des `assert` sur des cas simples.

??? pouce "Coup de pouce"

    Deux boucles sur les indices, avec `j > i`, comme pour le jour 1, et un test sur les valeurs des deux éléments.

### <span class="exo-num">Exercice 4</span> — La fenêtre glissante <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-diviser-pour-regner-aoc-2-4 }

Écrire une fonction `premier_invalide(nombres, p)` où `p` est la longueur du préambule. Tester avec `p = 5` sur l’exemple de la fiche, puis avec la bonne longueur sur vos données.

??? pouce "Coup de pouce"

    Pour le nombre d’indice `i`, la fenêtre est la tranche `nombres[i - p:i]`. Faire un petit dessin pour vérifier les bornes.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Pour exploiter la faille, il faut se servir du nombre fautif trouvé en partie 1.

    - Trouver une suite d’**au moins deux** nombres consécutifs du fichier dont la somme vaut ce nombre.

    - Il faut renvoyer la somme du plus petit et du plus grand nombre de cette suite (ce ne sont pas forcément le premier et le dernier).

### <span class="exo-num">Exercice 5</span> — Une première solution <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-diviser-pour-regner-aoc-2-5 }

Écrire une fonction qui cherche la suite demandée en essayant toutes les positions de début et de fin. Sur l’exemple de la fiche, on doit trouver `12`.

??? pouce "Coup de pouce"

    Une suite contiguë, c’est une tranche `nombres[debut:fin]`. Attention : la suite réduite au seul nombre invalide ne compte pas.

### <span class="exo-num">Exercice 6</span> — Deux indices <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-diviser-pour-regner-aoc-2-6 }

Les nombres de vos données sont tous positifs. Expliquer pourquoi on peut alors trouver la suite avec seulement deux indices `debut` et `fin` qui ne font qu’avancer, en tenant à jour la somme de la tranche. Programmer cette méthode et comparer sa complexité à celle de l’exercice précédent.

??? pouce "Coup de pouce"

    Si la somme courante est trop petite, on ajoute le nombre suivant (`fin` avance) ; si elle est trop grande, on retire le premier (`debut` avance).

??? pouce "Coup de pouce 2 (début de solution)"

    Chaque indice avance au plus $n$ fois : la méthode est linéaire. La boucle `while` s’arrête quand la somme est atteinte avec au moins deux nombres.

## Approfondissement

!!! encadre "Outil Python : mesurer une durée (time) et tirer au hasard (random)"

    Le module `time` fournit un chronomètre précis ; le module `random` tire des nombres au hasard, utile pour fabriquer de grosses données de test.

    ```python
    import random
    import time

    x = random.randint(1, 6)         # entier au hasard entre 1 et 6 (bornes comprises)
    liste = [random.randint(1, 1000) for _ in range(5)]
    depart = time.perf_counter()     # top depart (en secondes)
    total = sum(range(10**6))
    duree = time.perf_counter() - depart
    print(f"{duree:.4f} s")          # 4 chiffres apres la virgule
    ```

    **Intérêt.** Vérifier expérimentalement une complexité : si l’on double $n$, une méthode linéaire prend environ deux fois plus de temps, une méthode quadratique environ quatre fois plus. Une mesure isolée varie : la répéter.

    **À essayer.** Mesurer `sum(range(10**6))` puis `sum(range(2 * 10**6))` : le rapport des durées est-il proche de 2 ?

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Défi : mesurer <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-diviser-pour-regner-aoc-2-7 }

Mesurer avec le module `time` la durée des deux méthodes de la partie 2 sur vos données, puis sur une liste aléatoire de $10\,000$ nombres. Les mesures sont-elles cohérentes avec les complexités annoncées ?

??? pouce "Coup de pouce"

    `time.perf_counter()` avant et après l’appel ; la différence donne la durée en secondes.

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

    **À essayer.** Avec `fenetre = [3, 7, 10, 7, 2]`, que vaut `set(fenetre)` ? Combien d’éléments ?

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Approfondissement 1 : la partie 1 avec un ensemble <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-diviser-pour-regner-aoc-2-8 }

1.  À la main : avec la fenêtre `3 7 10 7 2` et la cible `13`, calculer pour chaque `x` la valeur `13 - x` et dire si elle est dans la fenêtre. Recommencer avec la cible `14` : pourquoi le complément `7` de `7` ne convient-il pas ?

2.  Écrire `somme_de_deux_ensemble(fenetre, cible)` avec une seule boucle et un ensemble, puis l’utiliser pour retrouver `22` sur l’exemple de la fiche.

3.  Pour $p = 25$, combien de tests environ fait chaque version pour un nombre ? En déduire les complexités totales.

??? pouce "Coup de pouce"

    Pour chaque `x` de la fenêtre, la seule valeur qui le complète est `cible - x`.

??? pouce "Coup de pouce 2 (début de solution)"

    Construire `valeurs = set(fenetre)`, puis tester `cible - x in valeurs` sans oublier la règle des valeurs différentes : `cible - x != x`.
