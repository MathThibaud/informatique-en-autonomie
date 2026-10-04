# Défis Advent of Code

<p class="sous-titre">Structures linéaires : piles, files, listes chaînées</p>

## <span class="etiquette">Défi 1</span> Operation Order

*les devoirs de maths — piles et analyse d’expressions*

<p class="infos-activite">Jour 18</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/03-defi-aoc-2020-18){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-03-defi-aoc-2020-18.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/18 ](https://adventofcode.com/2020/day/18 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/03-defi-aoc-2020-18>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

*Ce défi réinvestit les piles vues dans ce chapitre : comme pour la vérification d’un parenthésage, une pile permet de traiter les parenthèses imbriquées.*

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| homework | devoirs à la maison | expression | expression (calcul) |
| addition / multiplication | addition / multiplication | parentheses | parenthèses |
| evaluate | calculer, évaluer | precedence | priorité (des opérations) |
| left-to-right | de gauche à droite | regardless of | quel que soit |
| resulting value | valeur obtenue | sum | somme |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** En 2020, les elfes vous ont laissé partir en vacances sous les tropiques. Pendant un vol, un enfant assis à côté de vous vous demande de l’aide pour ses devoirs de calcul... mais dans son école, les règles de priorité ne sont pas celles que vous connaissez. Chaque ligne du fichier est un calcul de son cahier.

    **Ce qu’il faut faire.**

    - Une expression contient des entiers positifs (d’un seul chiffre dans les données), les opérateurs `+` et `*`, et des parenthèses ; les symboles sont séparés par des espaces.

    - Les parenthèses gardent leur rôle : leur contenu se calcule d’abord, et elles peuvent être imbriquées.

    - En revanche, `*` n’est **pas** prioritaire sur `+` : en dehors des parenthèses, on effectue les opérations dans l’ordre où on les lit, de gauche à droite. Autrement dit, `2 + 3 * 4` se calcule comme `(2 + 3) * 4`.

    - Réponse : la somme des valeurs de toutes les lignes.

### <span class="exo-num">Exercice 1</span> — Vérifier sa compréhension <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-structures-lineaires-piles-files-listes-aoc-1-1 }

1.  Que valent `2 * 3 + 4` et `2 + 3 * 4` avec cette règle ?

2.  Que vaut `2 * (3 + 4) * 2` ? Et `((1 + 2))` ?

3.  La somme finale dépasse largement $10^{9}$ : est-ce un problème en Python ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-structures-lineaires-piles-files-listes-aoc-1-2 }

On considère le fichier (inventé) suivant :

```console
3 * (2 + 4) + 5
2 + 3 * 4 + (1 * 6)
(4 + 5 * (2 + 1)) * 2 + 3
```

Calculer chaque ligne avec la règle de l’énoncé, en écrivant les étapes comme sur le site. Vérification : les trois valeurs ont pour somme `106`. Quelle valeur Python donne-t-il pour la deuxième ligne avec `eval` ? Pourquoi ne peut-on donc pas utiliser `eval` directement ?

## Programmer la partie 1

!!! encadre "Outil Python : deux méthodes de chaînes (isdigit, replace)"

    Les chaînes de caractères possèdent des *méthodes* toutes faites. `c.isdigit()` renvoie `True` si tous les caractères de `c` sont des chiffres ; `s.replace(a, b)` renvoie une **nouvelle** chaîne où chaque occurrence de `a` est remplacée par `b` (la chaîne `s` n’est pas modifiée).

    ```python
    print("7".isdigit())       # True
    print("+".isdigit())       # False
    print("12".isdigit())      # True : tous les caracteres sont des chiffres
    s = "3 * (2 + 4)"
    t = s.replace(" ", "")     # on remplace chaque espace par "rien"
    print(t)                   # 3*(2+4)
    print(s)                   # s est inchange : 3 * (2 + 4)
    ```

    **Intérêt.** Ces méthodes évitent d’écrire soi-même une boucle de comparaison (`c in "0123456789"` fait le même travail que `c.isdigit()` pour un caractère). Question : recopier et exécuter ce code ; que renvoie `"2020".replace("0", "")` ? et `"".isdigit()` ?

### <span class="exo-num">Exercice 3</span> — Découper une ligne en symboles <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-structures-lineaires-piles-files-listes-aoc-1-3 }

Écrire une fonction `decouper(ligne)` qui renvoie la liste des *symboles* de la ligne : les nombres (convertis en `int`), `’+’`, `’*’`, `’(’` et `’)’`. Par exemple `decouper("3 * (2 + 4)")` doit renvoyer `[3, ’*’, ’(’, 2, ’+’, 4, ’)’]`.

??? pouce "Coup de pouce"

    Supprimer d’abord les espaces avec `replace`, puis parcourir la chaîne caractère par caractère en accumulant les chiffres consécutifs dans une chaîne `nombre` : un nombre est terminé dès qu’on rencontre autre chose qu’un chiffre.

### <span class="exo-num">Exercice 4</span> — Évaluer sans priorité <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-structures-lineaires-piles-files-listes-aoc-1-4 }

Écrire une fonction `evaluer(symboles)` qui renvoie la valeur de l’expression avec la règle de la partie 1. Tester sur les trois lignes de l’exemple, puis calculer la somme sur `input.txt`.

??? pouce "Coup de pouce"

    Deux méthodes possibles. **Avec une pile** : quand on rencontre `’(’`, on empile le résultat partiel et l’opérateur en attente, puis on repart de zéro ; quand on rencontre `’)’`, on dépile et on combine. **Récursivement** : une fonction lit l’expression de gauche à droite et s’appelle elle-même dès qu’elle rencontre une parenthèse ouvrante ; elle renvoie la valeur *et* l’indice où elle s’est arrêtée.

??? pouce "Coup de pouce 2 (début de solution)"

    Version récursive : `evaluer_depuis(symboles, i)` garde une variable `total` et un opérateur courant `op` (au départ `’+’` et `total = 0`). Pour chaque symbole : un nombre, ou une sous-expression obtenue par appel récursif après `’(’`, est combiné à `total` avec `op` ; `’+’` ou `’*’` met à jour `op` ; `’)’` ou la fin de la liste arrête la boucle et l’on renvoie `(total, i)`.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Vous avez mal compris : dans cette école, il existe bien une priorité, mais à l’envers de la vôtre. L’**addition est prioritaire** sur la multiplication. Les parenthèses passent toujours en premier ; à priorité égale, on calcule de gauche à droite. Ainsi `2 * 3 + 4` vaut maintenant $2 \times 7 = 14$. Réponse : la somme des valeurs des lignes.

### <span class="exo-num">Exercice 5</span> — Changer la priorité <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-structures-lineaires-piles-files-listes-aoc-1-5 }

Seule la priorité entre `+` et `*` change. Adapter le programme. Sur l’exemple de la fiche, on doit trouver les valeurs `33`, `50` et `135`, de somme `218`.

??? pouce "Coup de pouce"

    Avec la méthode récursive, il suffit de repérer qu’une expression devient un *produit de sommes* : une fonction calcule une somme (de nombres ou de parenthèses), une autre fait le produit de ces sommes.

??? pouce "Coup de pouce 2 (début de solution)"

    Algorithme de la gare de triage (Dijkstra) : une pile d’opérateurs et une pile de valeurs. On donne à chaque opérateur une priorité (un dictionnaire `{’+’: 2, ’*’: 1}`). Avant d’empiler un opérateur, on applique tous ceux du sommet de pile de priorité supérieure ou égale ; une `’)’` applique les opérateurs jusqu’à la `’(’` correspondante. Avec `{’+’: 1, ’*’: 1}`, le même code résout la partie 1.

## Approfondissement

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Approfondissement 1 : la descente récursive <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-structures-lineaires-piles-files-listes-aoc-1-6 }

En partie 2, une expression est un **produit de sommes** : `2 + 3 * 4 + (1 * 6)` se lit $(2 + 3) \times (4 + (1 \times 6))$. On peut décrire toutes les expressions par trois définitions qui s’appellent mutuellement :

- un *produit* est une somme, éventuellement suivie de `* somme`, `* somme`…

- une *somme* est un facteur, éventuellement suivi de `+ facteur`, `+ facteur`…

- un *facteur* est un nombre, ou bien un produit entre parenthèses.

1.  À la main : découper la deuxième ligne de l’exemple en sommes, puis chaque somme en facteurs. Faire de même pour la troisième ligne. Où intervient la définition récursive du facteur ?

2.  Écrire trois fonctions `facteur(symboles, i)`, `somme(symboles, i)` et `produit(symboles, i)` qui lisent la liste à partir de l’indice `i` et renvoient le couple `(valeur, indice du premier symbole non lu)`. Vérifier qu’on retrouve `33`, `50` et `135`.

    ??? pouce "Coup de pouce"

        Chaque fonction suit sa définition : `somme` appelle `facteur`, puis, tant que le symbole courant est `’+’`, saute ce symbole et appelle à nouveau `facteur`. `produit` fait de même avec `somme` et `’*’`.

    ??? pouce "Coup de pouce 2 (début de solution)"

        `facteur` : si `symboles[i]` vaut `’(’`, appeler `produit(symboles, i + 1)`, qui renvoie `(v, j)` avec `symboles[j] == ’)’` ; renvoyer alors `(v, j + 1)`. Sinon renvoyer `(symboles[i], i + 1)`.

3.  Quelle est la complexité de cette méthode ? Comment l’adapter à la partie 1 (une seule priorité) ?

!!! encadre "Outil Python : tester le type d’une valeur (isinstance)"

    `isinstance(x, int)` renvoie `True` si `x` est un entier ; de même avec `str`, `list`… C’est utile quand une même liste contient des valeurs de types différents, par exemple des nombres et des opérateurs.

    ```python
    expression = [3, 4, "+", 2, "*"]
    print(isinstance(expression[0], int))   # True  : un nombre
    print(isinstance(expression[2], int))   # False : un operateur
    print(isinstance(expression[2], str))   # True
    ```

    Question : que renvoie `isinstance("7", int)` ? Pourquoi ?

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 2 : la notation postfixe <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-structures-lineaires-piles-files-listes-aoc-1-7 }

En **notation postfixe** (ou « polonaise inverse »), on écrit chaque opérateur *après* ses deux opérandes, et l’on n’a plus besoin de parenthèses : `(3 + 4) * 2` s’écrit `3 4 + 2 *`. Certaines calculatrices fonctionnent ainsi.

1.  Évaluer à la main `3 4 + 2 *` en utilisant une pile : on lit de gauche à droite ; un nombre est empilé ; un opérateur dépile deux valeurs et empile le résultat. Dessiner la pile après chaque symbole.

2.  Écrire `evaluer_postfixe(expression)` qui évalue une liste comme `[3, 4, ’+’, 2, ’*’]`.

    ??? pouce "Coup de pouce"

        Une seule pile (une liste avec `append` et `pop`) ; `isinstance(s, int)` distingue les nombres des opérateurs. Attention à l’ordre : le premier élément dépilé est l’opérande de **droite**.

3.  L’algorithme de la gare de triage peut, au lieu de calculer, **écrire** l’expression en notation postfixe : un nombre va directement dans la liste de sortie, un opérateur dépilé y est ajouté au lieu d’être appliqué. Écrire `postfixe(symboles, priorite)`. Écrire à la main la notation postfixe de la deuxième ligne de l’exemple pour chacune des deux parties : qu’est-ce qui change ?

    ??? pouce "Coup de pouce"

        Reprendre le code de la gare de triage : là où l’on appliquait un opérateur dépilé, on l’ajoute à la fin de la liste `sortie`.

    ??? pouce "Coup de pouce 2 (début de solution)"

        Partie 1 : `2 3 + 4 * 1 6 * +`. Il reste à trouver celle de la partie 2 et à vérifier que `evaluer_postfixe(postfixe(...))` redonne bien `50`.

4.  Combien de piles au total pour calculer une expression de cette façon ? Quelle est la complexité ?

## <span class="etiquette">Défi 2</span> Crab Cups

*les gobelets du crabe — listes chaînées*

<p class="infos-activite">Jour 23</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/03-defi-aoc-2020-23){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-03-defi-aoc-2020-23.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/23 ](https://adventofcode.com/2020/day/23 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/03-defi-aoc-2020-23>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

*Ce défi réinvestit les listes chaînées de ce chapitre : un cercle de gobelets est une liste chaînée circulaire, et l’on verra qu’un simple tableau suffit à la représenter.*

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| cup | gobelet | label | étiquette, numéro |
| clockwise | dans le sens des aiguilles d’une montre | circle | cercle |
| current cup | gobelet courant | pick up | ramasser, retirer |
| destination cup | gobelet de destination | move | coup |
| wrap around | repartir de l’autre bout | immediately | juste (après) |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Le crabe vous défie maintenant à un jeu de bonneteau : il déplace des gobelets numérotés disposés en cercle, et vous devez prédire où ils seront à la fin. Le fichier est une simple suite de chiffres : les numéros des gobelets dans l’ordre du cercle.

    **Ce qu’il faut faire.**

    - Les données sont 9 chiffres (de 1 à 9, chacun une fois) : les étiquettes des gobelets dans le sens horaire. Le premier est le gobelet « courant ».

    - Un coup : retirer les 3 gobelets qui suivent le courant ; la destination est l’étiquette du courant moins 1, en sautant les étiquettes retirées et en repartant de la plus grande étiquette si l’on passe sous la plus petite ; replacer les 3 gobelets, dans le même ordre, juste après la destination ; le nouveau courant est le gobelet qui suit alors le courant. Autrement dit, le crabe déplace un paquet de trois gobelets vers le plus grand numéro inférieur disponible.

    - Jouer 100 coups. Réponse : les étiquettes lues dans le sens horaire à partir du gobelet 1 (sans lui), écrites en une seule chaîne.

### <span class="exo-num">Exercice 1</span> — Vérifier sa compréhension <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-structures-lineaires-piles-files-listes-aoc-2-1 }

1.  Avec 9 gobelets, le courant porte 2 et les gobelets retirés sont 1, 9 et 8 : quelle est la destination ?

2.  Le gobelet courant peut-il être la destination ? Un gobelet retiré ?

3.  Le nouveau courant se choisit-il avant ou après avoir replacé les trois gobelets ? Cela change-t-il quelque chose ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-structures-lineaires-piles-files-listes-aoc-2-2 }

On part de l’étiquetage (inventé) `527164839`. Jouer le premier coup à la main. Vérification : en lisant le cercle à partir du `5`, on obtient `5 6 4 2 7 1 8 3 9`. Quel est le nouveau gobelet courant ? Jouer encore deux coups.

## Programmer la partie 1

!!! encadre "Outil Python : chercher dans une liste (index, max)"

    `liste.index(x)` renvoie l’indice de la **première** occurrence de `x` (erreur si `x` est absent) ; `max(liste)` renvoie le plus grand élément.

    ```python
    g = [5, 6, 4, 2, 7, 1, 8, 3, 9]
    print(g.index(1))          # 5
    print(max(g))              # 9
    k = g.index(4)
    g = g[:k + 1] + [0] + g[k + 1:]    # insertion juste apres le 4
    print(g)                   # [5, 6, 4, 0, 2, 7, 1, 8, 3, 9]
    ```

    **Intérêt et limite.** Ces fonctions sont pratiques, mais elles parcourent la liste : `index` et `max` coûtent jusqu’à $n$ opérations. Question : que se passe-t-il avec `g.index(10)` ?

### <span class="exo-num">Exercice 3</span> — Une première simulation avec une liste <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-structures-lineaires-piles-files-listes-aoc-2-3 }

Écrire une fonction `jouer(gobelets, nb_coups)` qui simule le jeu sur une liste Python d’entiers, puis une fonction qui renvoie la réponse sous forme de chaîne. Sur l’exemple de la fiche, on doit obtenir `53269478` après 10 coups et `98357642` après 100 coups.

??? pouce "Coup de pouce"

    Le plus simple est de garder le gobelet courant toujours en tête de liste : après chaque coup, faire « tourner » la liste d’un cran (le premier élément passe à la fin). Les trois gobelets ramassés sont alors aux indices 1, 2 et 3.

### <span class="exo-num">Exercice 4</span> — Combien ça coûte ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-structures-lineaires-piles-files-listes-aoc-2-4 }

Quelle est la complexité d’un coup avec cette méthode, en fonction du nombre $n$ de gobelets ? Lire la partie 2 (une fois débloquée) : combien d’opérations élémentaires faudrait-il environ ?

??? pouce "Coup de pouce"

    Chercher le gobelet de destination (`index`), retirer et insérer des éléments dans une liste Python : chacune de ces opérations est en $O(n)$.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Le crabe sort beaucoup plus de gobelets et joue beaucoup plus longtemps. Après vos 9 chiffres, le cercle est complété par les étiquettes $10, 11, \dots$ jusqu’à $1\,000\,000$, dans l’ordre. Jouer $10\,000\,000$ coups avec les mêmes règles. Réponse : le produit des deux étiquettes qui suivent le gobelet 1.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 5</span> — Une liste chaînée dans un tableau <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-structures-lineaires-piles-files-listes-aoc-2-5 }

Réécrire la simulation avec un **tableau des successeurs** (lire l’encadré), vérifier qu’elle redonne les résultats de la partie 1, puis répondre à la partie 2. Sur l’exemple de la fiche, on doit trouver `28997820592`. Le calcul peut prendre une dizaine de secondes.

??? pouce "Coup de pouce"

    Un coup ne modifie que **trois** cases du tableau `suivant`. Les écrire sur un dessin avant de coder : le successeur du courant, celui du dernier gobelet ramassé, celui de la destination.

??? pouce "Coup de pouce 2 (début de solution)"

    Avec `a = suivant[courant]`, `b = suivant[a]`, `c = suivant[b]` : le courant doit maintenant pointer vers `suivant[c]` ; `c` doit pointer vers l’ancien successeur de la destination ; la destination doit pointer vers `a`. Attention à l’ordre des affectations.

!!! encadre "Le tableau des successeurs"

    Une **liste chaînée** n’a pas besoin d’objets `Maillon` : comme les étiquettes sont les entiers de $1$ à $n$, on peut ranger dans une liste `suivant` de taille $n + 1$ l’étiquette qui suit chaque gobelet dans le cercle : `suivant[x]` est le gobelet juste après `x` (la case `0` ne sert pas). Pour le cercle `3 1 2` : `suivant[3] = 1`, `suivant[1] = 2` et `suivant[2] = 3` (le dernier pointe vers le premier : la liste est *circulaire*).

    **Avantages.** Trouver le gobelet d’étiquette `x` ne demande aucune recherche : c’est la case `x`. Retirer ou insérer un morceau de la chaîne revient à modifier quelques cases, sans décaler les autres éléments. Un coup se fait donc en temps constant, $O(1)$, quel que soit $n$.

    **Pour lire le cercle** à partir du gobelet `1`, on suit les flèches : `x = suivant[1]`, puis `x = suivant[x]`, jusqu’à revenir à `1`.

!!! encadre "Outils Python : mesurer un temps (time.perf_counter) et tableaux compacts (array)"

    `perf_counter()` renvoie un temps en secondes, très précis ; la différence entre deux appels donne une durée. Le module `array` fournit des tableaux d’entiers d’un seul type, plus compacts en mémoire qu’une liste.

    ```python
    from time import perf_counter
    from array import array
    debut = perf_counter()
    total = 0
    for k in range(1_000_000):
        total += k
    print(f"{perf_counter() - debut:.3f} s")   # duree de la boucle
    t = array("i", [0] * 10)    # 10 entiers de type "i" (int en C)
    t[3] = 42                   # s'utilise comme une liste
    print(t[3], len(t))         # 42 10
    ```

    Question : mesurer la durée de la boucle ci-dessus avec $10^6$ puis $10^7$ tours. Le temps est-il proportionnel au nombre de tours ?

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 6</span> — Défi : aller plus vite <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-structures-lineaires-piles-files-listes-aoc-2-6 }

Mesurer le temps de calcul avec `perf_counter`. Peut-on le réduire en évitant de recalculer des valeurs dans la boucle, ou avec le module `array` ?

??? pouce "Coup de pouce"

    Dans une boucle de dix millions de tours, chaque accès à une variable globale ou chaque appel de fonction compte : placer toute la boucle dans une fonction et utiliser des variables locales.
