# Défis Advent of Code

<p class="sous-titre">Les bases de la programmation Python</p>

## <span class="etiquette">Défi 1</span> Not Quite Lisp

*l’ascenseur du père Noël — compteur sur une chaîne*

<p class="infos-activite">Jour 1</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/01-defi-aoc-2015-01){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-01-defi-aoc-2015-01.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2015/day/1 ](https://adventofcode.com/2015/day/1 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Créer un compte sur le site est **facultatif** (connexion avec GitHub, Google…). Avec un compte, le lien *get your puzzle input* affiche **vos** données : tout sélectionner, copier, puis coller dans un fichier texte vide enregistré sous le nom `input.txt`, **dans le même dossier** que votre programme Python. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/01-defi-aoc-2015-01>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

*Ce défi réinvestit le parcours d’une chaîne caractère par caractère et le motif de l’accumulateur vus dans ce chapitre.*

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|                         |                        |              |                 |
|:------------------------|:-----------------------|:-------------|:----------------|
| floor                   | étage                  | ground floor | rez-de-chaussée |
| basement                | sous-sol               | parenthesis  | parenthèse      |
| up / down               | monter / descendre     | building     | immeuble        |
| one character at a time | un caractère à la fois | directions   | instructions    |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Le Père Noël doit livrer des cadeaux dans un immeuble immense, avec des sous-sols très profonds. Les instructions qu’on lui a données sont une longue suite de parenthèses : chacune lui dit de monter ou de descendre d’un étage. Le fichier contient cette suite ; il faut trouver où il arrive.

    **Ce qu’il faut faire.**

    - Le fichier ne contient qu’**une seule ligne**, formée des caractères `(` et `)`.

    - On part du rez-de-chaussée, l’étage 0, et on lit les caractères un par un : `(` fait monter d’un étage, `)` fait descendre d’un étage.

    - L’immeuble n’a ni dernier étage ni sous-sol le plus bas : l’étage peut devenir aussi grand ou aussi négatif qu’on veut. Un étage négatif est un sous-sol ($-1$ est le premier sous-sol).

    - La réponse est l’étage atteint après le dernier caractère.

### <span class="exo-num">Exercice 1</span> — Vérifier sa compréhension <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-les-bases-de-la-programmation-python-aoc-1-1 }

Questions pièges, à traiter sur le cahier :

1.  L’ordre des caractères change-t-il l’étage final ? Comparer `(())` et `))((`.

2.  Quel est l’étage final d’une chaîne qui contient autant de `(` que de `)` ?

3.  Peut-on trouver la réponse sans parcourir la chaîne caractère par caractère ?

### <span class="exo-num">Exercice 2</span> — À la main, sur de petits exemples <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-les-bases-de-la-programmation-python-aoc-1-2 }

Pour chacune des chaînes (inventées) suivantes, trouver l’étage d’arrivée :

```console
(()))(()        ((())())))(        ())((
```

Vérification : on doit obtenir `0`, `-1` et `1`.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire les données <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-les-bases-de-la-programmation-python-aoc-1-3 }

Le fichier ne contient qu’une ligne. Voici comment la lire en Python (ces trois lignes sont fournies, il suffit de les recopier) :

```python
fichier = open("input.txt")              # ouvre le fichier
instructions = fichier.readline().strip()  # lit la ligne, sans le retour a la ligne
fichier.close()                          # ferme le fichier
```

Recopier ces lignes, puis afficher la longueur de `instructions`, son premier et son dernier caractère.

### <span class="exo-num">Exercice 4</span> — L’étage d’arrivée <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-les-bases-de-la-programmation-python-aoc-1-4 }

Écrire une fonction `etage_final(instructions)` qui renvoie l’étage atteint à la fin. Tester sur les trois exemples, puis sur vos données.

??? pouce "Coup de pouce"

    Une variable `etage` qui commence à 0 ; parcourir la chaîne caractère par caractère avec `for c in instructions:` et augmenter ou diminuer `etage` selon `c`.

!!! encadre "Outil Python : compter dans une chaîne (count)"

    La méthode `count` d’une chaîne renvoie le nombre de fois qu’un morceau de texte y apparaît (sans chevauchement). Elle fait elle-même la boucle à notre place.

    ```python
    mot = "abracadabra"
    print(mot.count("a"))      # 5
    print(mot.count("abra"))   # 2 : on peut compter un morceau de plusieurs lettres
    print(mot.count("z"))      # 0
    ```

    **Intérêt.** Le code est plus court ; le travail reste le même (un parcours de toute la chaîne), mais il est fait par Python, plus vite qu’une boucle écrite à la main. Question : que vaut `"aaaa".count("aa")` ?

### <span class="exo-num">Exercice 5</span> — Une autre méthode <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-les-bases-de-la-programmation-python-aoc-1-5 }

À l’aide de la méthode `count`, écrire une deuxième version de `etage_final` en une seule ligne, et vérifier qu’elle donne les mêmes résultats.

??? pouce "Coup de pouce"

    L’étage final, c’est le nombre de montées moins le nombre de descentes.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    On s’intéresse maintenant au trajet lui-même, et non plus à l’arrivée. La réponse est la **position** du premier caractère qui amène le Père Noël à l’étage $-1$, c’est-à-dire son premier passage au sous-sol. Attention : les positions sont numérotées **à partir de 1** (le premier caractère est en position 1).

### <span class="exo-num">Exercice 6</span> — Le premier passage <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-les-bases-de-la-programmation-python-aoc-1-6 }

Écrire une fonction `premier_passage(instructions)` qui répond à la question. Attention : l’énoncé numérote les positions à partir de 1, Python à partir de 0. Sur les exemples de la fiche, on doit trouver `5`, `9` et `3`.

??? pouce "Coup de pouce"

    Cette fois, il faut connaître la **position** du caractère : parcourir les indices avec `for i in range(len(instructions)):`. La méthode `count` ne suffit plus : pourquoi ?

??? pouce "Coup de pouce 2 (début de solution)"

    Mettre à jour `etage` à chaque caractère et, juste après, tester `if etage < 0:` ; dans ce cas, renvoyer immédiatement la position avec `return`, en tenant compte de la numérotation de l’énoncé (`i` ou `i + 1` ?). Le `return` arrête la boucle.

## Approfondissement

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : tester et explorer le trajet <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-les-bases-de-la-programmation-python-aoc-1-7 }

1.  Que doit renvoyer `premier_passage` si l’on ne descend jamais sous le rez-de-chaussée (par exemple pour `"(()"`) ? Modifier la fonction pour qu’elle renvoie la valeur spéciale `None` (« rien ») dans ce cas, et écrire quelques `assert` qui testent les deux fonctions sur les exemples de la fiche.

2.  Écrire une fonction `etage_max(instructions)` qui renvoie l’étage le plus haut atteint pendant le trajet. Sur `((())())))(`, on doit trouver `3`.

    ??? pouce "Coup de pouce"

        Même boucle que `etage_final`, avec une seconde variable `record` qui retient le plus haut étage vu jusqu’ici.

3.  Écrire une fonction `nb_descentes_sous_sol(instructions)` qui compte combien de fois le Père Noël passe du rez-de-chaussée au premier sous-sol. Sur `())())`, écrire les étages successifs à la main et vérifier qu’on trouve `2`.

    ??? pouce "Coup de pouce 2 (début de solution)"

        Un compteur qu’on augmente quand, juste après une descente, l’étage vaut $-1$ : on venait alors forcément de l’étage 0.

## <span class="etiquette">Défi 2</span> The Tyranny of the Rocket Equation

*le carburant de la fusée — division entière, fonctions, boucle while*

<p class="infos-activite">Jour 1</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/01-defi-aoc-2019-01){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-01-defi-aoc-2019-01.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2019/day/1 ](https://adventofcode.com/2019/day/1 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Créer un compte sur le site est **facultatif** (connexion avec GitHub, Google…). Avec un compte, le lien *get your puzzle input* affiche **vos** données : tout sélectionner, copier, puis coller dans un fichier texte vide enregistré sous le nom `input.txt`, **dans le même dossier** que votre programme Python. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/01-defi-aoc-2019-01>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

*Ce défi réinvestit les fonctions, la division entière et la boucle `while` (avec son variant) vus dans ce chapitre.*

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| fuel | carburant | mass | masse |
| module | module (élément de la fusée) | required | nécessaire |
| to divide by | diviser par | to round down | arrondir à l’unité inférieure |
| to subtract | soustraire | to add together | additionner |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Le Père Noël est bloqué au bord du système solaire, et les elfes préparent une fusée pour aller le chercher. La fusée est faite de modules, et chaque module a besoin de carburant pour décoller, en quantité qui dépend de sa masse. Le fichier liste les masses des modules ; il faut calculer le carburant à embarquer.

    **Ce qu’il faut faire.**

    - Le fichier contient une masse (un entier positif) par ligne, une ligne par module.

    - Le carburant d’un module s’obtient ainsi : diviser la masse par 3, **arrondir à l’entier inférieur**, puis retirer 2. Autrement dit, c’est le quotient de la division entière par 3, moins 2.

    - La réponse est la somme des carburants de tous les modules.

### <span class="exo-num">Exercice 1</span> — Vérifier sa compréhension <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-les-bases-de-la-programmation-python-aoc-2-1 }

Questions pièges, à traiter sur le cahier :

1.  Quel carburant pour une masse de 9 ? de 10 ? de 11 ? Pourquoi trouve-t-on le même résultat ?

2.  Pour une masse de 2000, quelle différence entre arrondir à l’entier inférieur et arrondir à l’entier le plus proche ?

3.  Que donne la formule pour une masse de 6 ou de 7 ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-les-bases-de-la-programmation-python-aoc-2-2 }

Calculer le carburant nécessaire pour des modules (inventés) de masses `30`, `90` et `2000`, puis le total. Vérification : on doit obtenir `8`, `28`, `664`, soit un total de `700`.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Division entière <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-les-bases-de-la-programmation-python-aoc-2-3 }

En Python, comparer `2000 / 3`, `2000 // 3` et `int(2000 / 3)`. Lequel correspond à « diviser puis arrondir à l’unité inférieure » pour un nombre positif ?

### <span class="exo-num">Exercice 4</span> — Une fonction pour un module <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-les-bases-de-la-programmation-python-aoc-2-4 }

Écrire une fonction `carburant(masse)` qui renvoie le carburant d’un module. La tester avec des `assert` sur les trois masses de l’exemple, par exemple `assert carburant(30) == 8`.

??? pouce "Coup de pouce"

    Une seule ligne suffit dans la fonction : `return` suivi du calcul, avec l’opérateur `//`.

### <span class="exo-num">Exercice 5</span> — Le total <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-les-bases-de-la-programmation-python-aoc-2-5 }

Voici comment lire un fichier texte ligne par ligne (ces lignes sont fournies) :

```python
fichier = open("input.txt")      # ouvre le fichier
for ligne in fichier:            # une ligne a chaque tour de boucle
    ligne = ligne.strip()        # retire le retour a la ligne final
    masse = int(ligne)           # la chaine "1969" devient l'entier 1969
    print(masse)
fichier.close()                  # ferme le fichier
```

Recopier ce programme et l’exécuter sur un fichier contenant l’exemple de la fiche. Le modifier ensuite pour calculer la somme des carburants de tous les modules, avec le motif de l’accumulateur.

??? pouce "Coup de pouce"

    Une variable `total` qui vaut 0 avant la boucle ; à chaque tour, on lui ajoute `carburant(masse)`. On affiche `total` après la boucle.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    On avait oublié un détail : le carburant lui-même pèse, et il faut donc du carburant pour le transporter ! Pour chaque module, on calcule le carburant de ce carburant avec la même formule, puis le carburant de ce nouveau carburant, et ainsi de suite, en s’arrêtant dès qu’on obtient une valeur nulle ou négative (elle compte pour 0). Le carburant d’un module est la somme de toutes ces quantités ; ce calcul se fait **module par module**, et la réponse est la somme sur tous les modules.

### <span class="exo-num">Exercice 6</span> — Du carburant pour le carburant <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-les-bases-de-la-programmation-python-aoc-2-6 }

Écrire une fonction `carburant_total(masse)` qui applique la nouvelle règle à un module. Avec les masses de l’exemple, on doit trouver `8`, `35` et `980`, soit un total de `1023`. Détailler à la main le cas de la masse `90` avant de programmer.

??? pouce "Coup de pouce"

    On ne sait pas à l’avance combien de fois il faut recalculer : c’est le cas typique d’une boucle `while`. Que faut-il faire d’une quantité nulle ou négative ?

??? pouce "Coup de pouce 2 (début de solution)"

    `total = 0` et `ajout = carburant(masse)` ; `while ajout > 0:` on ajoute `ajout` à `total`, puis on remplace `ajout` par `carburant(ajout)`. Bien réutiliser la fonction de la partie 1.

### <span class="exo-num">Exercice 7</span> — Vérifier la boucle <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-les-bases-de-la-programmation-python-aoc-2-7 }

Pour la masse `90`, écrire le tableau des valeurs successives de `ajout` et `total` à chaque tour de boucle. Combien de tours fait la boucle ? Pourquoi est-on sûr qu’elle s’arrête ?

## Approfondissement

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 8</span> — Approfondissement 1 (pour aller plus loin, notion de Terminale) : une fonction qui s’appelle elle-même <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-les-bases-de-la-programmation-python-aoc-2-8 }

Une fonction peut s’appeler elle-même : on parle de fonction *récursive*. C’est une notion de Terminale, proposée ici pour les curieux.

1.  Expliquer pourquoi, pour une masse $m$ : carburant total de $m$ = carburant de $m$ + carburant total *de ce carburant*, tant que le carburant de $m$ est strictement positif.

2.  Écrire une version de `carburant_total` sans boucle, qui s’appelle elle-même sur la quantité de carburant qu’elle vient de calculer.

    ??? pouce "Coup de pouce"

        Si le carburant d’une masse est nul ou négatif, la réponse est 0 et on s’arrête : c’est le *cas de base*. Sinon, la réponse est ce carburant, plus le carburant total de ce carburant.

    ??? pouce "Coup de pouce 2 (début de solution)"

        `c = carburant(masse)` ; `if c <= 0:` `return 0` ; sinon `return c + carburant_total_rec(c)`.

3.  Écrire la suite des appels pour la masse 90 et vérifier qu’on retrouve `35`. Pourquoi est-on sûr que les appels s’arrêtent ?
