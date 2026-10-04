# Défis Advent of Code

<p class="sous-titre">Les algorithmes de tri</p>

## <span class="etiquette">Défi 1</span> I Was Told There Would Be No Math

*emballer les cadeaux — découper une chaîne, trier trois nombres*

<p class="infos-activite">Jour 2</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/06-defi-aoc-2015-02){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-06-defi-aoc-2015-02.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2015/day/2 ](https://adventofcode.com/2015/day/2 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (facultatif), le lien *get your puzzle input* donne **vos** données, à enregistrer sous `input.txt` à côté du programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/06-defi-aoc-2015-02>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

*Ce défi réinvestit le tri vu dans ce chapitre : trier trois nombres simplifie tous les calculs.*

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| wrapping paper | papier cadeau | present, gift | cadeau |
| length, width, height | longueur, largeur, hauteur | box | boîte |
| surface area | aire totale (de la surface) | side | face |
| smallest | le plus petit | slack | supplément, marge |
| square feet | pieds carrés (unité d’aire) | to order | commander |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Les elfes vont manquer de papier cadeau et doivent en commander. Tous les cadeaux sont des boîtes en forme de pavé droit, et les elfes connaissent les trois dimensions de chacune. Pour commander juste ce qu’il faut, ils ont besoin de la surface totale de papier.

    **Ce qu’il faut faire.**

    - Chaque ligne décrit une boîte : trois entiers séparés par la lettre `x`, la longueur $L$, la largeur $l$ et la hauteur $h$.

    - Pour une boîte, il faut de quoi recouvrir ses six faces, soit l’aire totale $2Ll + 2lh + 2hL$, plus un peu de marge : l’aire de sa **plus petite face**.

    - La réponse est la somme de ces quantités sur toutes les boîtes.

### <span class="exo-num">Exercice 1</span> — Vérifier sa compréhension <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-les-algorithmes-de-tri-aoc-1-1 }

Questions pièges, à traiter sur le cahier :

1.  Combien de papier faut-il pour un cube `2x2x2` ?

2.  L’ordre des trois nombres sur la ligne change-t-il la quantité de papier ?

3.  Si deux faces ont la même aire, la plus petite, ajoute-t-on deux fois cette aire ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-les-algorithmes-de-tri-aoc-1-2 }

Calculer le papier nécessaire pour les boîtes (inventées) `3x5x2`, `4x4x1` et `10x2x7`. Vérification : on doit trouver `68`, `52` et `222`, soit un total de `342`.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire les dimensions <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-les-algorithmes-de-tri-aoc-1-3 }

Que renvoie `"3x5x2".split("x")` ? Écrire une fonction `dimensions(ligne)` qui renvoie la **liste triée** des trois entiers. Exemple : `dimensions("3x5x2")` renvoie `[2, 3, 5]`.

??? pouce "Coup de pouce"

    Après le `split`, convertir chacun des trois morceaux avec `int`, les mettre dans une liste, puis trier avec `sorted(...)` ou la méthode `.sort()`.

### <span class="exo-num">Exercice 4</span> — Le papier d’une boîte <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-les-algorithmes-de-tri-aoc-1-4 }

Écrire une fonction `papier(ligne)` qui renvoie le papier nécessaire pour un cadeau. Pourquoi est-il pratique d’avoir trié les dimensions ? Tester sur les trois boîtes de l’exemple.

??? pouce "Coup de pouce"

    Une fois triées en `a <= b <= c`, la plus petite face est celle de dimensions `a` et `b`.

??? pouce "Coup de pouce 2 (début de solution)"

    `a, b, c = dimensions(ligne)` ; l’aire totale est `2 * (a * b + b * c + a * c)`, et il reste à ajouter le supplément demandé.

### <span class="exo-num">Exercice 5</span> — Le total <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-les-algorithmes-de-tri-aoc-1-5 }

Lire `input.txt` et additionner le papier de tous les cadeaux.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Les elfes doivent aussi commander du ruban. Pour une boîte, il faut de quoi en faire le tour par le côté le plus court, c’est-à-dire le **plus petit périmètre** parmi ceux des faces, plus de quoi faire le nœud, une longueur égale au **volume** de la boîte. La réponse est la somme sur toutes les boîtes.

### <span class="exo-num">Exercice 6</span> — Le ruban <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-les-algorithmes-de-tri-aoc-1-6 }

Écrire une fonction `ruban(ligne)`. Sur les boîtes de l’exemple, on doit trouver `40`, `26` et `158`, soit un total de `224`.

??? pouce "Coup de pouce"

    Le plus petit périmètre parmi ceux des trois faces : là encore, les dimensions triées le donnent immédiatement.

??? pouce "Coup de pouce 2 (début de solution)"

    Avec `a <= b <= c`, le plus petit périmètre de face est `2 * (a + b)` ; le volume est `a * b * c`.

## Approfondissement

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : une seule lecture du fichier <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-les-algorithmes-de-tri-aoc-1-7 }

Écrire une fonction `commande(nom_fichier)` qui renvoie les deux totaux (papier et ruban) en une seule lecture du fichier, et vérifier avec des `assert` les valeurs de l’exemple.

??? pouce "Coup de pouce"

    Deux accumulateurs dans la même boucle ; une fonction peut renvoyer un couple : `return total_papier, total_ruban`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Approfondissement 2 : sans trier <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-les-algorithmes-de-tri-aoc-1-8 }

On peut aussi se passer du tri, avec les fonctions `min` et `max` qui acceptent plusieurs nombres : `min(15, 10, 6)` vaut `6`.

1.  Pour la boîte `3x5x2`, calculer les aires des trois faces différentes et leur minimum.

2.  Écrire `papier_sans_tri(ligne)` qui utilise `min` sur les trois aires.

3.  Pour le ruban, il faut les deux plus petites dimensions. Montrer que leur somme vaut $L + l + h - \max(L, l, h)$, puis écrire `ruban_sans_tri(ligne)`.

    ??? pouce "Coup de pouce"

        Les deux plus petites dimensions, ce sont toutes les dimensions sauf la plus grande.

4.  Vérifier que les deux versions donnent les mêmes résultats sur tout le fichier. Laquelle préférez-vous, et pourquoi ?

## <span class="etiquette">Défi 2</span> Historian Hysteria

*deux listes à réconcilier — trier, distances, compter*

<p class="infos-activite">Jour 1</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/06-defi-aoc-2024-01){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-06-defi-aoc-2024-01.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2024/day/1 ](https://adventofcode.com/2024/day/1 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (facultatif), le lien *get your puzzle input* donne **vos** données, à enregistrer sous `input.txt` à côté du programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/06-defi-aoc-2024-01>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

*Ce défi réinvestit le tri d’un tableau vu dans ce chapitre.*

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| list | liste | side by side | côte à côte |
| left / right | gauche / droite | to pair up | associer par paires |
| smallest | le plus petit | second-smallest | le deuxième plus petit |
| how far apart | à quelle distance (l’écart) | to add up | additionner |
| to reconcile | mettre en accord | location ID | identifiant de lieu |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Les historiens du pôle Nord cherchent leur chef, introuvable. Dans son bureau, ils ont dressé deux listes de lieux à visiter, chaque lieu étant désigné par un numéro. Mais les deux listes ne concordent pas, et il faut mesurer à quel point elles diffèrent. Le fichier présente les deux listes côte à côte.

    **Ce qu’il faut faire.**

    - Chaque ligne contient deux entiers séparés par plusieurs espaces : le premier appartient à la liste de gauche, le second à la liste de droite.

    - On ne compare pas les nombres d’une même ligne : on trie chaque liste, puis on associe le plus petit nombre de gauche au plus petit de droite, le deuxième au deuxième, etc.

    - L’écart d’une paire est la distance entre ses deux nombres, c’est-à-dire la valeur absolue de leur différence.

    - La réponse est la somme des écarts de toutes les paires.

### <span class="exo-num">Exercice 1</span> — Vérifier sa compréhension <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-les-algorithmes-de-tri-aoc-2-1 }

Questions pièges, à traiter sur le cahier :

1.  Si les deux listes contiennent exactement les mêmes nombres, dans un autre ordre, quelle est la réponse ?

2.  L’écart entre 3 et 7 est-il le même que l’écart entre 7 et 3 ?

3.  Pourquoi les deux listes ont-elles forcément la même longueur ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-les-algorithmes-de-tri-aoc-2-2 }

On considère le fichier (inventé) suivant :

```console
5   2
2   5
7   4
1   2
2   8
6   2
```

Écrire les deux listes triées l’une sous l’autre, puis les écarts. Vérification : on doit obtenir `4`.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire les deux colonnes <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-les-algorithmes-de-tri-aoc-2-3 }

Écrire une fonction `lire(nom_fichier)` qui renvoie les deux listes `gauche` et `droite`. Sur l’exemple : `[5, 2, 7, 1, 2, 6]` et `[2, 5, 4, 2, 8, 2]`.

??? pouce "Coup de pouce"

    Même schéma que d’habitude (`open`, boucle sur les lignes). `"5 2".split()` renvoie `["5", "2"]` : les espaces multiples ne gênent pas.

??? pouce "Coup de pouce 2 (début de solution)"

    `morceaux = ligne.split()` puis `gauche.append(int(morceaux[0]))` et de même pour `droite`. Une fonction peut renvoyer deux valeurs : `return gauche, droite`, récupérées par `g, d = lire("exemple.txt")`.

!!! encadre "Outil Python : la valeur absolue (abs)"

    La fonction `abs` renvoie la valeur absolue d’un nombre : le nombre sans son signe. Pour deux nombres `x` et `y`, `abs(x - y)` est la distance entre eux, quel que soit le plus grand.

    ```python
    print(abs(-4))       # 4
    print(abs(4))        # 4
    print(abs(3 - 7))    # 4
    print(abs(7 - 3))    # 4 : meme distance
    ```

    **Intérêt.** Inutile d’écrire un `if` pour savoir quel nombre est le plus grand. Question : que vaut `abs(0)` ? `abs(-2.5)` ?

### <span class="exo-num">Exercice 4</span> — La distance totale <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-les-algorithmes-de-tri-aoc-2-4 }

Écrire une fonction `distance_totale(gauche, droite)` qui renvoie la réponse de la partie 1. Tester sur l’exemple, puis sur vos données.

??? pouce "Coup de pouce"

    Trier les deux listes (`sorted`), puis parcourir les indices : l’écart entre deux nombres `x` et `y` est `abs(x - y)`.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Les historiens remarquent que beaucoup de numéros se retrouvent dans les deux listes : on mesure maintenant leur ressemblance autrement. Pour chaque nombre de la liste de gauche, on compte combien de fois il apparaît dans la liste de droite, et on multiplie le nombre par ce compte. La réponse est la somme de ces produits ; un nombre présent deux fois à gauche est compté deux fois.

!!! encadre "Outil Python : compter dans une liste (count)"

    La méthode `count` d’une liste renvoie le nombre de fois qu’une valeur y apparaît. Elle parcourt toute la liste à notre place.

    ```python
    t = [2, 5, 4, 2, 8, 2]
    print(t.count(2))    # 3
    print(t.count(7))    # 0 : valeur absente
    ```

    **Intérêt.** Le code est plus court, mais attention : chaque appel parcourt toute la liste, ce qui coûte cher s’il est répété. Question : combien de comparaisons fait `t.count(2)` ?

### <span class="exo-num">Exercice 5</span> — Compter les apparitions <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-les-algorithmes-de-tri-aoc-2-5 }

1.  Écrire une fonction `nb_apparitions(x, liste)` qui compte, avec une boucle, combien de fois `x` apparaît dans `liste`. Comparer avec la méthode `liste.count(x)`.

2.  Utiliser cette fonction pour répondre à la partie 2. Sur l’exemple de la fiche, on doit trouver `17`.

??? pouce "Coup de pouce"

    Relire précisément ce que l’énoncé multiplie : quel nombre, et par quoi ? Faut-il trier pour cette partie ?

??? pouce "Coup de pouce 2 (début de solution)"

    Pour chaque `x` de la liste de gauche, on ajoute au total `x * nb_apparitions(x, droite)`.

## Approfondissement

!!! encadre "Outil Python : la méthode get des dictionnaires"

    Pour un dictionnaire `d`, `d.get(cle, defaut)` renvoie la valeur associée à `cle` si elle existe, et `defaut` sinon, sans provoquer d’erreur.

    ```python
    compte = {2: 3, 5: 1}
    print(compte.get(2, 0))      # 3
    print(compte.get(7, 0))      # 0 : la cle 7 est absente
    ```

    Question : que se passe-t-il avec `compte[7]` ?

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 6</span> — Approfondissement 1 : compter une fois pour toutes <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-les-algorithmes-de-tri-aoc-2-6 }

1.  Avec 1000 nombres par liste, combien de comparaisons fait la solution de la partie 2 qui utilise `nb_apparitions` ?

2.  Sur l’exemple, écrire à la main le dictionnaire `compte` qui associe à chaque nombre de la liste de droite son nombre d’apparitions.

3.  Écrire une fonction `similarite_dico(gauche, droite)` qui construit ce dictionnaire en un parcours de la liste de droite, puis répond en un seul parcours de la liste de gauche. Quelle est sa complexité ?

    ??? pouce "Coup de pouce"

        Pour chaque `y` de la liste de droite : si `y` est déjà une clé, augmenter sa valeur de 1 ; sinon, créer la clé avec la valeur 1.

    ??? pouce "Coup de pouce 2 (début de solution)"

        Ensuite, pour chaque `x` de gauche, ajouter `x * compte.get(x, 0)` au total : `get` renvoie 0 pour un nombre absent de la liste de droite.
