# Exercices

<p class="sous-titre">La recherche dichotomique</p>

!!! consignes "Mode d’emploi"

    - Niveau : ★ échauffement, ★★ classique (niveau bac), ★★★ défi ; les *coups de pouce* et les *corrigés* se déplient sous chaque exercice.

    - <span class="run" title="À programmer et tester sur machine">▶</span> *À programmer et tester* en Python. Le symbole `>>>` figure une saisie dans la console.

    - **Rappel :** la recherche dichotomique ne s’applique qu’à un tableau **trié**. Le milieu se calcule avec `(deb + fin) // 2`.

    - Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la [charte d’usage de l’IA](../charte.md).

### Dérouler la recherche à la main

On utilise le tableau trié $$\texttt{t = [3, 8, 11, 16, 19, 24, 30, 33, 38, 47, 52]} \quad \text{(indices 0 à 10).}$$

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — Un élément présent <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-07-1 }

On cherche `x = 33` par dichotomie. Recopier et compléter un tableau donnant, à chaque tour : `deb`, `fin`, `mil`, la valeur `t[mil]` et la décision (à gauche / à droite / trouvé). Combien de tours ont été nécessaires ?

??? corrige "Corrigé"

    !!! remarque "Remarque"

        On donne **une** version simple ; d’autres écritures sont possibles. On note `t = [3, 8, 11, 16, 19, 24, 30, 33, 38, 47, 52]`.

    Recherche de `x = 33` :

    | tour | `deb` | `fin` | `mil` | `t[mil]` | décision                          |
    |:----:|:-----:|:-----:|:-----:|:--------:|:----------------------------------|
    |  1   |   0   |  10   |   5   |    24    | $33 > 24$ : à droite (`deb` = 6)  |
    |  2   |   6   |  10   |   8   |    38    | $33 < 38$ : à gauche (`fin` = 7)  |
    |  3   |   6   |   7   |   6   |    30    | $33 > 30$ : à droite (`deb` = 7)  |
    |  4   |   7   |   7   |   7   |    33    | $33 = 33$ : **trouvé** (indice 7) |

    Trouvé en **4 tours**.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 2</span> — Un élément absent <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-07-2 }

Même travail pour `x = 20`. Où et pourquoi la recherche s’arrête-t-elle ? Que renvoie l’algorithme ?

??? corrige "Corrigé"

    Recherche de `x = 20` :

    | tour | `deb` | `fin` | `mil` | `t[mil]` | décision                         |
    |:----:|:-----:|:-----:|:-----:|:--------:|:---------------------------------|
    |  1   |   0   |  10   |   5   |    24    | $20 < 24$ : à gauche (`fin` = 4) |
    |  2   |   0   |   4   |   2   |    11    | $20 > 11$ : à droite (`deb` = 3) |
    |  3   |   3   |   4   |   3   |    16    | $20 > 16$ : à droite (`deb` = 4) |
    |  4   |   4   |   4   |   4   |    19    | $20 > 19$ : à droite (`deb` = 5) |

    Maintenant `deb = 5 > fin = 4` : la zone de recherche est **vide**, la boucle s’arrête et l’algorithme renvoie `False`. `20` est absent (il aurait dû se trouver entre `19` et `24`).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 3</span> — Le rôle du tri <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-07-3 }

On applique *malgré tout* l’algorithme au tableau **non trié** `[9, 7, 5, 3, 1]` pour y chercher `x = 9`.

1.  Dérouler l’algorithme. Que renvoie-t-il ?

    ??? pouce "Coup de pouce"

        Au premier tour, comparer `9` à `t[mil]` : de quel côté l’algorithme poursuit-il sa recherche ? Est-ce de ce côté que se trouve `9` ?

2.  `9` est pourtant bien dans le tableau. Expliquer, avec cet exemple, pourquoi le tri est **indispensable**.

??? corrige "Corrigé"

    **1.** Sur `[9, 7, 5, 3, 1]`, recherche de `x = 9` :

    | tour | `deb` | `fin` | `mil` | `t[mil]` | décision                       |
    |:----:|:-----:|:-----:|:-----:|:--------:|:-------------------------------|
    |  1   |   0   |   4   |   2   |    5     | $9 > 5$ : à droite (`deb` = 3) |
    |  2   |   3   |   4   |   3   |    3     | $9 > 3$ : à droite (`deb` = 4) |
    |  3   |   4   |   4   |   4   |    1     | $9 > 1$ : à droite (`deb` = 5) |

    `deb = 5 > fin = 4` : l’algorithme renvoie `False`.

    **2.** Or `9` est bel et bien présent (en tête !). L’algorithme le rate parce qu’il **suppose** que « à droite se trouvent les plus grands » : c’est faux ici, puisque le tableau n’est pas trié. Chaque décision « à gauche / à droite » n’a de sens que sur un tableau **trié**. Sans tri, la dichotomie donne un résultat *faux*.

### Écrire l’algorithme

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 4</span> — Compléter la recherche dichotomique <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-07-4 }

Compléter les six trous `.....` de cette fonction, puis la tester sur le tableau `t` donné plus haut (avant l’exercice 1) avec `x = 24` (présent) et `x = 10` (absent).

```text
def recherche_dichotomique(t, x):
    deb = 0
    fin = .....
    while ..... :               # tant que la zone n'est pas vide
        mil = .....
        if t[mil] == x:
            return True
        elif x > t[mil]:
            deb = .....         # on garde la moitie droite
        else:
            fin = .....         # on garde la moitie gauche
    return .....
```

??? corrige "Corrigé"

    Les six trous, dans l’ordre : `len(t) - 1`, `deb <= fin`, `(deb + fin) // 2`, `mil + 1`, `mil - 1`, `False`.

    ```python
    def recherche_dichotomique(t, x):
        deb = 0
        fin = len(t) - 1
        while deb <= fin:
            mil = (deb + fin) // 2
            if t[mil] == x:
                return True
            elif x > t[mil]:
                deb = mil + 1
            else:
                fin = mil - 1
        return False
    ```

    Avec `t = [3, 8, 11, 16, 19, 24, 30, 33, 38, 47, 52]`, l’appel avec `24` renvoie `True` et l’appel avec `10` renvoie `False`. À noter : `fin` est le **dernier indice** (`len(t) - 1`, pas `len(t)`) ; on écrit `mil + 1` et `mil - 1` car `mil` vient d’être testé.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 5</span> — La recherche dichotomique <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-5 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `recherche_dichotomique(t, x)` qui renvoie `True` si `x` est présent dans le tableau trié `t`, `False` sinon. Tester sur `t = [3, 8, 11, 16, 19, 24, 30, 33, 38, 47, 52]` avec `x = 38` (présent) puis `x = 25` (absent).

??? pouce "Coup de pouce"

    Deux indices `deb` et `fin` délimitent la zone où `x` peut encore se trouver. Que faire tant que cette zone n’est pas vide ? Que conclure quand elle l’est devenue ?

??? pouce "Coup de pouce 2 (début de solution)"

    `deb = 0`  
    `fin = len(t) - 1`  
    `while deb <= fin:`  
    `mil = (deb + fin) // 2`

??? corrige "Corrigé"

    ```python
    def recherche_dichotomique(t, x):
        deb = 0
        fin = len(t) - 1
        while deb <= fin:
            mil = (deb + fin) // 2
            if t[mil] == x:
                return True
            elif x > t[mil]:
                deb = mil + 1
            else:
                fin = mil - 1
        return False
    ```

    `recherche_dichotomique(t, 38)` renvoie `True` ; `recherche_dichotomique(t, 25)` renvoie `False`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Renvoyer la position <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-6 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `indice_dichotomique(t, x)` qui renvoie l’**indice** de `x` dans `t`, ou `-1` si `x` est absent.

```text
>>> indice_dichotomique([3, 8, 11, 16, 19], 16)
3
```

??? pouce "Coup de pouce"

    Partir de `recherche_dichotomique` : que faut-il renvoyer à la place de `True` quand `t[mil] == x` ? et à la place de `False` ?

??? corrige "Corrigé"

    On renvoie `mil` au lieu de `True`, et `-1` au lieu de `False`.

    ```python
    def indice_dichotomique(t, x):
        deb = 0
        fin = len(t) - 1
        while deb <= fin:
            mil = (deb + fin) // 2
            if t[mil] == x:
                return mil
            elif x > t[mil]:
                deb = mil + 1
            else:
                fin = mil - 1
        return -1
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Compter les tours <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-7 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `nb_tours(t, x)` qui effectue la recherche dichotomique de `x` et renvoie le **nombre de tours de boucle** exécutés.

??? pouce "Coup de pouce"

    Un compteur initialisé à `0`, augmenté de 1 au début de chaque tour ; attention, il y a deux sorties possibles (trouvé, absent) et il faut le renvoyer dans les deux.

1.  Combien de valeurs sont examinées pour chercher `7` dans `[0, 1, 1, 2, 3, 5, 8, 13, 21]` ?

2.  Donner un exemple (tableau + valeur cherchée) où l’on examine **exactement** 4 valeurs.

    ??? pouce "Coup de pouce"

        Avec combien d’éléments, au minimum, une recherche peut-elle durer 4 tours ? Chercher une valeur placée tout au bout, ou plus grande que toutes.

??? corrige "Corrigé"

    ```python
    def nb_tours(t, x):
        deb = 0
        fin = len(t) - 1
        n = 0
        while deb <= fin:
            n = n + 1
            mil = (deb + fin) // 2
            if t[mil] == x:
                return n
            elif x > t[mil]:
                deb = mil + 1
            else:
                fin = mil - 1
        return n
    ```

    **1.** Pour `7` dans `[0, 1, 1, 2, 3, 5, 8, 13, 21]` (9 éléments), on examine `3` (mil 4), `8` (mil 6), `5` (mil 5), puis la zone est vide : **3 tours**, et `7` est absent.  
    **2.** Par exemple, chercher `7` dans `[0, 1, 2, 3, 4, 5, 6, 7]` : on examine `3`, `5`, `6`, `7` — soit **4** valeurs. *(Tout tableau de 8 à 15 éléments dont l’élément cherché est au « fond » convient.)*

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 8</span> — La première occurrence <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-8 }

Dans un tableau trié qui contient des **doublons**, `indice_dichotomique` renvoie une occurrence de `x`, mais pas forcément la première : `indice_dichotomique([2, 4, 4, 4, 7, 9], 4)` renvoie `2`.

1.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire `premiere_occurrence(t, x)` qui renvoie l’indice de la **première** occurrence de `x` dans le tableau trié `t`, ou `-1` si `x` est absent, en gardant un coût **logarithmique**.

2.  Un camarade propose plutôt : trouver une occurrence par dichotomie, puis reculer case par case tant que la case de gauche vaut encore `x`. Pourquoi son coût n’est-il plus logarithmique dans le pire cas ? Donner un tableau qui le montre.

```text
>>> premiere_occurrence([2, 4, 4, 4, 7, 9], 4)
1
>>> premiere_occurrence([2, 4, 4, 4, 7, 9], 5)
-1
```

??? pouce "Coup de pouce"

    Quand on tombe sur `x` en `mil`, est-ce forcément la première occurrence ? De quel côté peut se cacher une occurrence plus à gauche ?

??? pouce "Coup de pouce 2 (début de solution)"

    Quand `t[mil] == x` : mémoriser `mil` dans une variable `resultat` (initialisée à `-1`), puis **continuer** la recherche à gauche avec `fin = mil - 1` au lieu de s’arrêter.

??? corrige "Corrigé"

    **1.** Quand on trouve `x`, on le **mémorise** comme candidat, puis on continue à chercher dans la moitié **gauche**, où peut se trouver une occurrence plus à gauche. La zone diminue toujours de moitié : le coût reste logarithmique.

    ```python
    def premiere_occurrence(t, x):
        deb = 0
        fin = len(t) - 1
        resultat = -1
        while deb <= fin:
            mil = (deb + fin) // 2
            if t[mil] == x:
                resultat = mil      # candidat : on cherche encore a gauche
                fin = mil - 1
            elif x > t[mil]:
                deb = mil + 1
            else:
                fin = mil - 1
        return resultat
    ```

    Sur `[2, 4, 4, 4, 7, 9]` avec `x = 4` : `mil = 2` (trouvé, `resultat = 2`, `fin = 1`), puis `mil = 0` (`2 < 4`, `deb = 1`), puis `mil = 1` (trouvé, `resultat = 1`, `fin = 0`) ; la zone est vide, on renvoie `1`.  
    **2.** Avec un tableau qui ne contient que des `x`, par exemple `[4] * 1000` : la dichotomie tombe sur le milieu (indice 499), puis il faut reculer case par case jusqu’à l’indice 0, soit environ $n/2$ pas. Le coût redevient **linéaire** dans le pire cas.

### Le coût logarithmique

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 9</span> — Combien d’étapes ? <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-07-9 }

Sans machine, donner le nombre *maximal* de comparaisons d’une recherche dichotomique pour un tableau trié de :

1.  $8$ éléments ; **2.** $16$ éléments ; **3.** $1\,000$ éléments (donner un ordre de grandeur).

??? pouce "Coup de pouce"

    Combien de fois faut-il diviser la taille par 2 pour arriver à 1 ?

??? corrige "Corrigé"

    On compte combien de fois diviser la taille par 2 pour atteindre 1, puis on ajoute la comparaison faite sur la dernière case restante.  
    **1.** Au pire, la zone de recherche passe par $8 \to 4 \to 2 \to 1$ : **3** divisions, puis une dernière comparaison sur la case restante, soit **4** comparaisons au maximum (c’est `nb_de_tour(8)`, car $2^3 = 8 \leq 8 < 2^4$).  
    **2.** $16 \to 8 \to 4 \to 2 \to 1$ : **4** divisions, plus la dernière comparaison, soit **5** comparaisons au maximum.  
    **3.** Pour $1\,000$ : $\log_2(1000) \approx 10$, donc **une dizaine** de comparaisons (à comparer aux 1000 d’un parcours !).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 10</span> — Le plus petit `k` tel que $2^k > n$ <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-10 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `nb_de_tour(n)` qui renvoie le plus petit entier `k` tel que `2**k > n` — c’est le nombre maximal de valeurs examinées par la dichotomie dans un tableau de taille `n`. *On utilisera une boucle qui double une puissance de 2 tant qu’elle ne dépasse pas `n`.*

```text
>>> nb_de_tour(100)
7
```

??? pouce "Coup de pouce"

    Garder deux variables : `k` et la puissance $2^k$ correspondante, que l’on double à chaque tour. Vérifier à la main avec `n = 1` puis `n = 2`.

??? corrige "Corrigé"

    On double une puissance de 2 tant qu’elle ne dépasse pas `n`, en comptant les doublements.

    ```python
    def nb_de_tour(n):
        k = 0
        puissance = 1          # vaut 2**k
        while puissance <= n:
            puissance = puissance * 2
            k = k + 1
        return k
    ```

    `nb_de_tour(100)` vaut `7` (car $2^6 = 64 \leq 100 < 128 = 2^7$).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 11</span> — Le pire cas, en vrai <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-11 }

<span class="run" title="À programmer et tester sur machine">▶</span> Le pire cas de la dichotomie est atteint quand l’élément est **absent**. En cherchant la valeur `1` dans un tableau ne contenant que des `0` (par exemple `[0] * n`), afficher le nombre de tours pour `n = 100`, `1000`, `10000`, `100000`, `1000000`. Que constate-t-on quand `n` est multiplié par 10 ? Comparer à la recherche séquentielle.

??? pouce "Coup de pouce"

    Réutiliser la fonction `nb_tours` de l’exercice « Compter les tours », appelée dans une boucle `for` sur la liste des tailles.

??? corrige "Corrigé"

    ```python
    for n in [100, 1000, 10000, 100000, 1000000]:
        t = [0] * n
        print(n, nb_tours(t, 1))   # 1 est absent : pire cas
    ```

    On obtient environ `7, 10, 14, 17, 20`. À chaque fois que `n` est **multiplié par 10**, le nombre de tours n’augmente que de **3 ou 4** : la croissance est **logarithmique**, extraordinairement lente. Une recherche séquentielle, elle, ferait jusqu’à `n` comparaisons (donc $\times 10$ à chaque fois).

### La terminaison

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 12</span> — Pourquoi ça s’arrête <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-07-12 }

La recherche dichotomique utilise une boucle `while` : il faut s’assurer qu’elle ne tourne pas indéfiniment.

1.  Montrer que la quantité `fin - deb` **diminue strictement** à chaque tour où l’on n’a pas trouvé `x` (examiner les deux cas : « à droite » et « à gauche »).

    ??? pouce "Coup de pouce"

        Dans le cas « à droite », `deb` devient `mil + 1`. Or `mil` est compris entre `deb` et `fin` : comparer la nouvelle valeur de `deb` à l’ancienne. Même raisonnement pour `fin`.

2.  En déduire que l’algorithme se termine toujours. Comment appelle-t-on une telle quantité ?

??? corrige "Corrigé"

    **1.** À chaque tour qui ne renvoie pas `True` :

    - cas « à droite » : `deb` devient `mil + 1` $>$ `deb` : la largeur `fin - deb` diminue ;

    - cas « à gauche » : `fin` devient `mil - 1` $<$ `fin` : la largeur `fin - deb` diminue aussi.

    Dans les deux cas, `fin - deb` **diminue strictement** (d’au moins 1).  
    **2.** Une quantité entière qui décroît strictement ne peut pas décroître indéfiniment : tôt ou tard `deb > fin`, la condition de la boucle devient fausse, l’algorithme se termine. Une telle quantité est un **variant de boucle**.

### Le jeu du nombre mystère

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 13</span> — Deviner en un minimum d’essais <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-07-13 }

On joue à deviner un nombre entre `1` et `100` : à chaque proposition, on répond *plus petit* ou *plus grand*.

1.  Quelle est la meilleure première proposition ? Pourquoi ?

2.  Combien d’essais suffisent, dans le pire des cas, en jouant de façon **optimale** ? Relier ce nombre à la dichotomie.

??? corrige "Corrigé"

    **1.** La meilleure première proposition est `50`, le **milieu** : quelle que soit la réponse, on élimine la moitié des possibilités (soit 1–49, soit 51–100).  
    **2.** En proposant toujours le milieu, le nombre de possibilités restantes, au pire, passe par $100 \to 50 \to 25 \to 12 \to 6 \to 3 \to 1$ : six essais pour réduire à un seul nombre possible, et un septième pour le proposer. **7 essais** suffisent donc dans le pire des cas. C’est exactement $\texttt{nb\_de\_tour(100)} = 7$ : le jeu *est* une recherche dichotomique.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 14</span> — L’ordinateur devine : la preuve <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-14 }

Au chapitre *Les bases de la programmation Python*, le défi « L’ordinateur devine » du TP « Le nombre mystère » vous a fait programmer un ordinateur qui devine un nombre en proposant toujours le **milieu**. On reprend ici ce programme, non pour le réécrire, mais pour l’**analyser** avec les outils du cours (la fonction `comparer` du TP est remplacée par des comparaisons directes).

```python
def essais_ordinateur(secret, maxi):
    """Simule la strategie du milieu ; renvoie le nombre d'essais.
    Precondition : 1 <= secret <= maxi."""
    mini = 1
    essais = 0
    trouve = False
    while not trouve:
        proposition = (mini + maxi) // 2
        essais = essais + 1
        if proposition < secret:
            mini = proposition + 1
        elif proposition > secret:
            maxi = proposition - 1
        else:
            trouve = True
    return essais
```

1.  Comparer avec `recherche_dichotomique` du cours : quel rôle jouent `mini`, `maxi` et `proposition` ? Dans quel « tableau trié » l’ordinateur cherche-t-il ?

2.  **Terminaison.** Montrer que `maxi - mini` diminue strictement à chaque essai raté. En utilisant la précondition (le secret reste toujours entre `mini` et `maxi`), en déduire que la boucle s’arrête. Comment appelle-t-on la quantité `maxi - mini` ?

3.  <span class="run" title="À programmer et tester sur machine">▶</span> Appeler `essais_ordinateur(150, 100)`, qui **ne respecte pas** la précondition (interrompre le programme au besoin). Expliquer ce qui se passe en suivant les valeurs de `mini` et `maxi`. Quelle condition de boucle, utilisée dans le cours, aurait évité ce problème ?

4.  **Coût.** Sans exécuter le programme, donner le nombre d’essais dans le pire des cas pour `maxi` égal à $100$, $1000$ et un million, en justifiant avec le raisonnement du cours. Combien d’essais faudrait-il, dans le pire des cas, à un ordinateur « naïf » qui propose $1$, puis $2$, puis $3$…?

??? pouce "Coup de pouce"

    Question 2 : examiner séparément les cas « trop petit » et « trop grand », comme pour `fin - deb` dans le cours. Question 3 : afficher `mini` et `maxi` à chaque tour avec un `print` ; que vaut `proposition` quand `mini` dépasse `maxi` ?

??? pouce "Coup de pouce 2 (début de solution)"

    Question 4 : le nombre de candidats est au moins divisé par deux à chaque essai raté ; chercher la plus petite puissance de 2 qui dépasse `maxi` (ou utiliser `nb_de_tour`).

??? corrige "Corrigé"

    **1.** C’est une recherche dichotomique : `mini` et `maxi` jouent le rôle de `deb` et `fin` (les bornes de la zone de recherche), `proposition` celui de `mil`. Le « tableau trié » est la suite des entiers `1, 2, …, maxi`, rangés dans l’ordre croissant : la valeur à la position `i` est `i` elle-même, il n’est donc pas besoin de la stocker.

    **2.** À chaque essai raté :

    - cas « trop petit » : `mini` devient `proposition + 1`, et `proposition` $\geqslant$ `mini`, donc `mini` augmente d’au moins 1 ;

    - cas « trop grand » : `maxi` devient `proposition - 1`, et `proposition` $\leqslant$ `maxi`, donc `maxi` diminue d’au moins 1.

    Dans les deux cas, l’entier `maxi - mini` **diminue strictement**. Grâce à la précondition, le secret reste toujours entre `mini` et `maxi` (on n’écarte que des nombres trop petits ou trop grands) : la zone ne peut donc jamais devenir vide. Comme `maxi - mini` ne peut pas décroître indéfiniment en restant $\geqslant 0$, on atteint au plus tard `mini == maxi` : la proposition est alors le secret lui-même, `trouve` devient `True` et la boucle s’arrête. La quantité `maxi - mini` est un **variant de boucle**.

    **3.** Le programme **ne s’arrête jamais**. Les propositions sont 50, 75, 88, 94, 97, 99, 100, toutes « trop petites » ; on arrive à `mini = 101` et `maxi = 100`. La zone est vide, mais la boucle continue car `trouve` reste `False` : `proposition` vaut `(101 + 100) // 2 = 100`, encore trop petite, `mini` reprend la valeur `101`… et rien ne change plus. Le variant ne décroît plus : la preuve de la question 2 utilisait la précondition, qui n’est pas respectée. La condition `while mini <= maxi` (le `while deb <= fin` du cours) arrête la boucle dès que la zone est vide, même si l’appel est incorrect ; on pourrait aussi vérifier la précondition par un `assert` en début de fonction.

    **4.** Après chaque essai raté, le nombre de candidats restants est au moins divisé par deux. Dans le pire des cas, le nombre d’essais est donc le plus petit $k$ tel que $2^k > \texttt{maxi}$, c’est-à-dire `nb_de_tour(maxi)` : **7** essais pour $100$ ($2^6 = 64 \leqslant 100 < 128 = 2^7$), **10** pour $1000$ ($2^{10} = 1024$) et **20** pour un million ($2^{20} = 1\,048\,576$). L’ordinateur naïf, lui, peut avoir besoin de `maxi` essais : $100$, $1000$, un million. Coût **logarithmique** contre coût **linéaire**, comme dans le cours.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 15</span> — La racine carrée entière <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-15 }

<span class="run" title="À programmer et tester sur machine">▶</span> La dichotomie ne sert pas qu’à chercher dans un tableau : elle permet de chercher un **nombre** dans un intervalle. Écrire `racine_entiere(n)` qui renvoie le plus grand entier `r` tel que `r * r <= n` (`n` entier positif), par dichotomie sur les entiers de `0` à `n`, sans utiliser `**` ni le module `math`.

```text
>>> racine_entiere(50)
7
>>> racine_entiere(49)
7
```

Combien de tours de boucle environ pour `n = 1000000` ? Comparer avec l’essai de tous les entiers `0, 1, 2`… un par un.

??? pouce "Coup de pouce"

    Si `mil * mil <= n`, `mil` convient, mais la réponse est peut-être plus grande : de quel côté continuer ? Et si `mil * mil > n` ?

??? pouce "Coup de pouce 2 (début de solution)"

    Même schéma que « La première occurrence » : `deb = 0`, `fin = n`, `r = 0` ; dans la boucle, quand `mil * mil <= n`, on mémorise `r = mil` puis `deb = mil + 1`.

??? corrige "Corrigé"

    On cherche, dans l’intervalle des entiers de `0` à `n`, le plus grand `r` tel que `r * r <= n`. Même schéma que pour la première occurrence : on mémorise le meilleur candidat et on continue à chercher du côté où il pourrait y en avoir un meilleur.

    ```python
    def racine_entiere(n):
        deb = 0
        fin = n
        r = 0
        while deb <= fin:
            mil = (deb + fin) // 2
            if mil * mil <= n:
                r = mil             # mil convient ; peut-etre plus grand ?
                deb = mil + 1
            else:
                fin = mil - 1       # mil est trop grand
        return r
    ```

    `racine_entiere(50)` et `racine_entiere(49)` renvoient `7`.

    *Autre méthode :* une recherche séquentielle, qui essaie `1, 2, 3`… tant que le carré suivant ne dépasse pas `n` :

    ```python
    def racine_entiere(n):
        r = 0
        while (r + 1) * (r + 1) <= n:
            r = r + 1
        return r
    ```

    Plus simple, mais bien plus lente : pour `n = 1000000`, l’intervalle contient environ $10^6$ entiers ; la dichotomie le réduit en environ **20** tours ($2^{20} \approx 10^6$), contre $1\,000$ essais en testant `0, 1, 2`… un par un jusqu’à `1000`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 16</span> — Le mot dans le dictionnaire <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-16 }

Un dictionnaire est un tableau trié de mots (l’ordre alphabétique). En Python, `"chat" < "chien"` compare deux chaînes dans l’ordre du dictionnaire.

1.  <span class="run" title="À programmer et tester sur machine">▶</span> Adapter `recherche_dichotomique` en `est_dans_dico(dico, mot)` qui cherche un **mot** dans un tableau de mots trié.

    ??? pouce "Coup de pouce"

        Les opérateurs `<`, `>` et `==` comparent aussi des chaînes : que reste-t-il à changer dans le code ?

2.  Sur un dictionnaire de $100\,000$ mots, combien de comparaisons faut-il au maximum pour savoir si un mot y figure ?

    ??? pouce "Coup de pouce"

        Chercher la plus petite puissance de 2 qui dépasse $100\,000$ (ou utiliser `nb_de_tour`).

??? corrige "Corrigé"

    **1.** L’algorithme est *identique* : les comparaisons `<`, `==` fonctionnent déjà sur les chaînes (ordre alphabétique).

    ```python
    def est_dans_dico(dico, mot):
        deb = 0
        fin = len(dico) - 1
        while deb <= fin:
            mil = (deb + fin) // 2
            if dico[mil] == mot:
                return True
            elif mot > dico[mil]:
                deb = mil + 1
            else:
                fin = mil - 1
        return False
    ```

    **2.** $\log_2(100\,000) \approx 16{,}6$, donc au plus **17** comparaisons pour un dictionnaire de cent mille mots. La puissance de la dichotomie !

    *Autre méthode :* une recherche séquentielle, par exemple `return mot in dico`. Elle marche même sur un dictionnaire non trié, mais elle examine les mots un par un : jusqu’à **100 000** comparaisons au lieu de 17.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 17</span> — La dichotomie selon un assistant d’IA <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> { #ex-07-17 }

Un élève demande à un assistant d’IA : « Écris une fonction Python rapide qui dit si une valeur est dans un tableau. » Voici la réponse obtenue.

```python
def contient(t, x):
    deb = 0
    fin = len(t) - 1
    while deb <= fin:
        mil = (deb + fin) // 2
        if t[mil] == x:
            return True
        elif x > t[mil]:
            deb = mil + 1
        else:
            fin = mil - 1
    return False
```

« C’est une recherche dichotomique : à chaque tour, la zone de recherche est divisée par deux, d’où un coût logarithmique. Elle fonctionne sur n’importe quel tableau, trié ou non, puisqu’on compare `x` à l’élément du milieu jusqu’à le trouver. »

1.  La réponse est-elle correcte ? Dérouler `contient([3, 9, 1, 7], 1)` à la main (valeurs de `deb`, `fin` et `mil` à chaque tour).

    ??? pouce "Coup de pouce"

        Noter à chaque tour `deb`, `fin`, `mil` et `t[mil]`. La case qui contient `1` est-elle examinée à un moment ?

2.  Localiser l’erreur (dans le code ou dans l’explication) et la corriger.

3.  Quelle vérification simple, faite avant de faire confiance à la réponse, aurait suffi à détecter l’erreur ?

??? corrige "Corrigé"

    **1.** Non. Trace de `contient([3, 9, 1, 7], 1)` :

    - `deb = 0`, `fin = 3`, `mil = 1`, `t[1] = 9` ; `1 > 9` est faux $\to$ `fin = 0` ;

    - `deb = 0`, `fin = 0`, `mil = 0`, `t[0] = 3` ; `1 > 3` est faux $\to$ `fin = -1` ;

    - `deb > fin` : la boucle s’arrête et la fonction renvoie **`False`**, alors que `1` est bien dans le tableau (case 2).

    **2.** Le code est celui du cours et il est juste ; l’erreur est dans l’explication : « trié ou non ». La dichotomie **ne s’applique qu’à un tableau trié** : c’est parce que le tableau est trié qu’on peut éliminer une moitié entière sans la regarder. Correction : préciser la précondition (`t` trié, à écrire dans la docstring) ; si le tableau ne l’est pas, utiliser une recherche séquentielle, ou le trier d’abord. Sur `[1, 3, 7, 9]`, la même fonction renvoie bien `True`. **3.** Tester la fonction sur un petit tableau **non trié** contenant la valeur cherchée : un seul appel révèle le problème. Plus généralement, une affirmation du type « fonctionne dans tous les cas » appelle un contre-exemple.
