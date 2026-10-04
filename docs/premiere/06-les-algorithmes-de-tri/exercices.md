# Exercices

<p class="sous-titre">Les algorithmes de tri</p>

!!! consignes "Mode d’emploi"

    - Niveau : ★ échauffement, ★★ classique (niveau bac), ★★★ défi ; les *coups de pouce* et les *corrigés* se déplient sous chaque exercice.

    - <span class="run" title="À programmer et tester sur machine">▶</span> *À programmer et tester* en Python. Le symbole `>>>` figure une saisie dans la console.

    - **Sauf mention contraire**, on n’utilise **pas** `sort`, `sorted`, `min` ni `max` : le but est d’écrire le **tri** soi-même. On trie **en place** (le tableau donné est modifié).

    - **Réflexe coût** : pour chaque tri, se demander combien de *comparaisons* il effectue.

    - Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la [charte d’usage de l’IA](../charte.md).

### Comprendre : dérouler un tri à la main

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — Trace du tri par sélection <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-06-1 }

Sans machine, on trie `[7, 2, 5, 3, 8, 1]` par **sélection**. Recopier et compléter le tableau : à chaque étape, indiquer le minimum sélectionné dans la partie non triée, puis l’état du tableau après échange.

??? corrige "Corrigé"

    !!! remarque "Remarque"

        On donne **une** version simple ; d’autres écritures sont possibles. Tous les tris se font **en place**.

    Tableau montré **au début de chaque étape** : zone grisée déjà triée, et en orange le minimum de la zone restante, amené à sa place par un échange.

    <table>
    <thead>
    <tr>
    <th style="text-align: right;"><strong>étape</strong></th>
    <th colspan="6" style="text-align: left;"><strong>tableau</strong></th>
    <th style="text-align: left;"><strong>action</strong></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: right;"><code>i</code>=0</td>
    <td style="text-align: center;"><code>7</code></td>
    <td style="text-align: center;"><code>2</code></td>
    <td style="text-align: center;"><code>5</code></td>
    <td style="text-align: center;"><code>3</code></td>
    <td style="text-align: center;"><code>8</code></td>
    <td style="text-align: center;"><code>1</code></td>
    <td style="text-align: left;">min <span class="math inline"> = 1</span> (case 5) <span class="math inline">→</span> échange avec la case 0</td>
    </tr>
    <tr>
    <td style="text-align: right;"><code>i</code>=1</td>
    <td style="text-align: center;"><code>1</code></td>
    <td style="text-align: center;"><code>2</code></td>
    <td style="text-align: center;"><code>5</code></td>
    <td style="text-align: center;"><code>3</code></td>
    <td style="text-align: center;"><code>8</code></td>
    <td style="text-align: center;"><code>7</code></td>
    <td style="text-align: left;">min <span class="math inline"> = 2</span> : déjà en place</td>
    </tr>
    <tr>
    <td style="text-align: right;"><code>i</code>=2</td>
    <td style="text-align: center;"><code>1</code></td>
    <td style="text-align: center;"><code>2</code></td>
    <td style="text-align: center;"><code>5</code></td>
    <td style="text-align: center;"><code>3</code></td>
    <td style="text-align: center;"><code>8</code></td>
    <td style="text-align: center;"><code>7</code></td>
    <td style="text-align: left;">min <span class="math inline"> = 3</span> (case 3) <span class="math inline">→</span> échange avec la case 2</td>
    </tr>
    <tr>
    <td style="text-align: right;"><code>i</code>=3</td>
    <td style="text-align: center;"><code>1</code></td>
    <td style="text-align: center;"><code>2</code></td>
    <td style="text-align: center;"><code>3</code></td>
    <td style="text-align: center;"><code>5</code></td>
    <td style="text-align: center;"><code>8</code></td>
    <td style="text-align: center;"><code>7</code></td>
    <td style="text-align: left;">min <span class="math inline"> = 5</span> : déjà en place</td>
    </tr>
    <tr>
    <td style="text-align: right;"><code>i</code>=4</td>
    <td style="text-align: center;"><code>1</code></td>
    <td style="text-align: center;"><code>2</code></td>
    <td style="text-align: center;"><code>3</code></td>
    <td style="text-align: center;"><code>5</code></td>
    <td style="text-align: center;"><code>8</code></td>
    <td style="text-align: center;"><code>7</code></td>
    <td style="text-align: left;">min <span class="math inline"> = 7</span> (case 5) <span class="math inline">→</span> échange avec la case 4</td>
    </tr>
    <tr>
    <td style="text-align: right;">arrivée</td>
    <td style="text-align: center;"><code>1</code></td>
    <td style="text-align: center;"><code>2</code></td>
    <td style="text-align: center;"><code>3</code></td>
    <td style="text-align: center;"><code>5</code></td>
    <td style="text-align: center;"><code>7</code></td>
    <td style="text-align: center;"><code>8</code></td>
    <td style="text-align: left;">tableau trié</td>
    </tr>
    </tbody>
    </table>

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 2</span> — Trace du tri par insertion <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-06-2 }

Même tableau `[7, 2, 5, 3, 8, 1]`, trié cette fois par **insertion**. Donner l’état du tableau **après chaque insertion** (5 étapes), en soulignant la partie déjà triée.

??? corrige "Corrigé"

    Tableau montré **après chaque insertion** : l’élément orange est celui qu’on vient d’insérer dans la partie gauche triée.

    <table>
    <thead>
    <tr>
    <th style="text-align: right;"></th>
    <th colspan="6" style="text-align: left;"><strong>tableau après insertion</strong></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: right;">départ</td>
    <td style="text-align: center;"><code>7</code></td>
    <td style="text-align: center;"><code>2</code></td>
    <td style="text-align: center;"><code>5</code></td>
    <td style="text-align: center;"><code>3</code></td>
    <td style="text-align: center;"><code>8</code></td>
    <td style="text-align: center;"><code>1</code></td>
    </tr>
    <tr>
    <td style="text-align: right;">insérer 2</td>
    <td style="text-align: center;"><code>2</code></td>
    <td style="text-align: center;"><code>7</code></td>
    <td style="text-align: center;"><code>5</code></td>
    <td style="text-align: center;"><code>3</code></td>
    <td style="text-align: center;"><code>8</code></td>
    <td style="text-align: center;"><code>1</code></td>
    </tr>
    <tr>
    <td style="text-align: right;">insérer 5</td>
    <td style="text-align: center;"><code>2</code></td>
    <td style="text-align: center;"><code>5</code></td>
    <td style="text-align: center;"><code>7</code></td>
    <td style="text-align: center;"><code>3</code></td>
    <td style="text-align: center;"><code>8</code></td>
    <td style="text-align: center;"><code>1</code></td>
    </tr>
    <tr>
    <td style="text-align: right;">insérer 3</td>
    <td style="text-align: center;"><code>2</code></td>
    <td style="text-align: center;"><code>3</code></td>
    <td style="text-align: center;"><code>5</code></td>
    <td style="text-align: center;"><code>7</code></td>
    <td style="text-align: center;"><code>8</code></td>
    <td style="text-align: center;"><code>1</code></td>
    </tr>
    <tr>
    <td style="text-align: right;">insérer 8</td>
    <td style="text-align: center;"><code>2</code></td>
    <td style="text-align: center;"><code>3</code></td>
    <td style="text-align: center;"><code>5</code></td>
    <td style="text-align: center;"><code>7</code></td>
    <td style="text-align: center;"><code>8</code></td>
    <td style="text-align: center;"><code>1</code></td>
    </tr>
    <tr>
    <td style="text-align: right;">insérer 1</td>
    <td style="text-align: center;"><code>1</code></td>
    <td style="text-align: center;"><code>2</code></td>
    <td style="text-align: center;"><code>3</code></td>
    <td style="text-align: center;"><code>5</code></td>
    <td style="text-align: center;"><code>7</code></td>
    <td style="text-align: center;"><code>8</code></td>
    </tr>
    </tbody>
    </table>

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 3</span> — Qui a fait quoi ? <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-06-3 }

On a photographié un tableau *en cours* de tri, juste après une étape : $$\texttt{[1, 2, 3, 8, 5, 9, 4, 7]}$$ On sait que le tri est soit une sélection, soit une insertion, et qu’on trie de gauche à droite. En observant la partie `[1, 2, 3]`, peut-on être sûr de laquelle il s’agit ? Justifier.

??? pouce "Coup de pouce"

    Dans chacun des deux tris, la partie triée de gauche contient-elle forcément les plus petits éléments du tableau ? Le tableau de départ est-il connu ?

??? corrige "Corrigé"

    On **ne peut pas** être certain. La partie gauche `[1, 2, 3]` est triée dans les deux cas. Mais l’indice décisif est ceci : en tri par **sélection**, la partie triée de gauche contient *à coup sûr les plus petits éléments du tableau, à leur place définitive*. Ici `[1, 2, 3]` sont bien les trois plus petits : c’est **compatible** avec une sélection (3 étapes faites). Mais c’est *aussi* compatible avec une insertion, si le tableau initial commençait déjà par de petites valeurs. Sans connaître le tableau de départ, on ne peut donc pas trancher. *(En revanche, si la partie gauche triée contenait une valeur qu’on sait **ne pas** être parmi les plus petites, ce serait forcément une insertion.)*

### Le tri par sélection

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 4</span> — L’ingrédient : trouver le minimum <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-06-4 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `indice_min(t, debut)` qui renvoie l’indice du plus petit élément de la portion `t[debut:]` (des indices `debut` jusqu’à la fin). Cette fonction est le cœur du tri par sélection.

```text
>>> indice_min([9, 4, 7, 2, 8], 1)
3
```

??? corrige "Corrigé"

    ```python
    def indice_min(t, debut):
        i_min = debut
        for j in range(debut + 1, len(t)):
            if t[j] < t[i_min]:
                i_min = j
        return i_min
    ```

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 5</span> — Remettre le tri par sélection dans l’ordre <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-06-5 }

Voici les lignes de la fonction `tri_selection` du cours (recherche du minimum écrite en entier), **mélangées** et **sans indentation**. Les remettre dans le bon ordre et les indenter correctement, puis vérifier sur machine que `[5, 3, 8, 1]` devient `[1, 3, 5, 8]`.

```text
t[i_min] = temp
for j in range(i + 1, n):
i_min = j
def tri_selection(t):
temp = t[i]
for i in range(n):
if t[j] < t[i_min]:
n = len(t)
t[i] = t[i_min]
i_min = i
```

??? corrige "Corrigé"

    On retrouve les deux temps du cours : chercher le minimum de `t[i:]`, puis l’échanger avec `t[i]`.

    ```python
    def tri_selection(t):
        n = len(t)
        for i in range(n):
            i_min = i
            for j in range(i + 1, n):
                if t[j] < t[i_min]:
                    i_min = j
            temp = t[i]
            t[i] = t[i_min]
            t[i_min] = temp
    ```

    À noter : `i_min = i` se place *avant* la boucle sur `j` (dans la boucle sur `i`) ; les trois lignes de l’échange sont *après* la boucle sur `j`, au même niveau que `i_min = i`. Avec `[5, 3, 8, 1]`, on obtient bien `[1, 3, 5, 8]`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Le tri par sélection <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-6 }

<span class="run" title="À programmer et tester sur machine">▶</span> En utilisant l’idée précédente, écrire `tri_selection(t)` qui trie le tableau `t` **en place** dans l’ordre croissant. Tester sur plusieurs exemples, dont un tableau vide et un tableau déjà trié.

??? pouce "Coup de pouce"

    À l’étape `i`, où faut-il chercher le minimum ? La fonction `indice_min` répond exactement à cette question ; il reste à échanger deux cases (variable temporaire).

??? pouce "Coup de pouce 2 (début de solution)"

    `def tri_selection(t):`  
    `for i in range(len(t)):`  
    `i_min = indice_min(t, i)`  
    `...` (échange de `t[i]` et `t[i_min]`)

??? corrige "Corrigé"

    ```python
    def tri_selection(t):
        n = len(t)
        for i in range(n):
            i_min = indice_min(t, i)   # reutilise l'exercice precedent
            temp = t[i]                # echange via variable temporaire
            t[i] = t[i_min]
            t[i_min] = temp
    ```

    Sur un tableau vide (`n = 0`), la boucle ne s’exécute pas : rien à trier, c’est correct. Sur un tableau déjà trié, chaque `indice_min` renvoie `i` : les échanges sont neutres, le tableau reste trié.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Dans l’autre sens <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-7 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `tri_selection_decroissant(t)` qui trie `t` du plus grand au plus petit. *Un seul caractère change par rapport au tri croissant : lequel ?*

??? pouce "Coup de pouce"

    Pour ranger du plus grand au plus petit, quel élément de la partie non triée faut-il amener en position `i` à chaque étape ?

??? corrige "Corrigé"

    On cherche le **maximum** au lieu du minimum : le seul changement est le sens de la comparaison (`>` au lieu de `<`).

    ```python
    def tri_selection_decroissant(t):
        n = len(t)
        for i in range(n):
            i_max = i
            for j in range(i + 1, n):
                if t[j] > t[i_max]:    # seul changement : > au lieu de <
                    i_max = j
            temp = t[i]
            t[i] = t[i_max]
            t[i_max] = temp
    ```

### Le tri par insertion

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 8</span> — Compléter le tri par insertion <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-06-8 }

Compléter les cinq trous `.....` de cette fonction de tri par insertion, puis la tester sur `[4, 2, 5, 1]`.

```text
def tri_insertion(t):
    n = len(t)
    for i in range(1, .....):
        x = t[i]                # l'element a inserer
        j = .....
        while j >= 0 and ..... :
            t[j + 1] = .....    # decaler vers la droite
            j = j - 1
        t[.....] = x            # poser x dans le trou
```

??? corrige "Corrigé"

    Les cinq trous, dans l’ordre : `n`, `i - 1`, `t[j] > x`, `t[j]`, `j + 1`.

    ```python
    def tri_insertion(t):
        n = len(t)
        for i in range(1, n):
            x = t[i]
            j = i - 1
            while j >= 0 and t[j] > x:
                t[j + 1] = t[j]
                j = j - 1
            t[j + 1] = x
    ```

    Sur `[4, 2, 5, 1]`, on obtient `[1, 2, 4, 5]`. On pose `x` en `t[j + 1]` car la boucle s’est arrêtée sur une case `j` qui *ne doit pas* bouger (ou sur `j = -1`).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 9</span> — Le tri par insertion <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-9 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `tri_insertion(t)` qui trie `t` **en place** par insertion. Vérifier sur `[5, 3, 8, 1, 9, 2]` qu’on obtient `[1, 2, 3, 5, 8, 9]`.

??? pouce "Coup de pouce"

    Mettre de côté l’élément à insérer dans une variable `x`, faire reculer un indice `j` tant qu’on rencontre plus grand que `x`, sans oublier de poser `x` à la fin.

??? pouce "Coup de pouce 2 (début de solution)"

    `def tri_insertion(t):`  
    `for i in range(1, len(t)):`  
    `x = t[i]`  
    `j = i - 1`

??? corrige "Corrigé"

    ```python
    def tri_insertion(t):
        n = len(t)
        for i in range(1, n):
            x = t[i]
            j = i - 1
            while j >= 0 and t[j] > x:
                t[j + 1] = t[j]
                j = j - 1
            t[j + 1] = x
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 10</span> — Compter les décalages <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-10 }

Modifier `tri_insertion` en `tri_insertion_compte(t)` qui renvoie le **nombre total de décalages** effectués (les affectations `t[j+1] = t[j]`).

??? pouce "Coup de pouce"

    Un compteur initialisé à `0` avant les boucles ; où se trouve, dans le code, l’instruction qui réalise un décalage ?

1.  Combien de décalages sur `[1, 2, 3, 4, 5]` (déjà trié) ?

2.  Combien sur `[5, 4, 3, 2, 1]` (trié à l’envers) ? Que remarque-t-on ?

??? corrige "Corrigé"

    On ajoute un compteur incrémenté à chaque décalage.

    ```python
    def tri_insertion_compte(t):
        n = len(t)
        nb = 0
        for i in range(1, n):
            x = t[i]
            j = i - 1
            while j >= 0 and t[j] > x:
                t[j + 1] = t[j]
                nb = nb + 1
                j = j - 1
            t[j + 1] = x
        return nb
    ```

    **1.** Sur `[1, 2, 3, 4, 5]` : **0** décalage — la condition `t[j] > x` est fausse d’emblée à chaque étape. C’est le *meilleur cas*, coût linéaire.  
    **2.** Sur `[5, 4, 3, 2, 1]` : **10** décalages, soit $\frac{n(n-1)}{2}$ pour $n=5$. Chaque nouvel élément doit remonter tout au début : c’est le *pire cas*, coût quadratique.

### Exercice guidé : le tri à bulles

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 11</span> — Construire le tri à bulles <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-11 }

Le **tri à bulles** compare les éléments *voisins* et les échange s’ils sont dans le désordre. À force de passages, les grandes valeurs « remontent » comme des bulles vers la fin du tableau.

1.  <span class="run" title="À programmer et tester sur machine">▶</span> **Un passage.** Écrire `un_passage(t)` qui parcourt `t` de gauche à droite et, pour chaque couple de voisins `t[j]` et `t[j+1]`, les échange si `t[j] > t[j+1]`. Appliquer `un_passage` à `[5, 3, 8, 1, 9, 2]` : quel élément se retrouve à coup sûr en dernière position ?

    ??? pouce "Coup de pouce"

        Dernier couple de voisins : `t[len(t) - 2]` et `t[len(t) - 1]`. Jusqu’où doit donc aller `j` ?

2.  **Pourquoi « à sa place » ?** Expliquer en une phrase pourquoi, après un passage complet, le **plus grand** élément est forcément tout à droite.

    ??? pouce "Coup de pouce"

        Suivre le plus grand élément dès que le parcours l’atteint : que lui arrive-t-il à chacune des comparaisons suivantes ?

3.  <span class="run" title="À programmer et tester sur machine">▶</span> **Le tri complet.** En répétant les passages, écrire `tri_bulle(t)`. Combien de passages suffisent pour un tableau de `n` éléments ? *(Remarque : le $i$-ème passage n’a plus besoin d’aller jusqu’au bout, puisque la fin est déjà triée.)*

    ??? pouce "Coup de pouce 2 (début de solution)"

        `def tri_bulle(t):`  
        `n = len(t)`  
        `for i in range(n - 1):`  
        `for j in range(n - 1 - i):`

4.  <span class="run" title="À programmer et tester sur machine">▶</span> **Le drapeau malin.** <span class="horsprog">au-delà du programme</span> Si un passage n’effectue **aucun** échange, c’est que le tableau est déjà trié : inutile de continuer. Écrire `tri_bulle_optimise(t)` qui s’arrête dans ce cas, à l’aide d’une variable booléenne `echange`. Sur un tableau déjà trié, combien de passages fait-elle ?

    ??? pouce "Coup de pouce"

        À quel moment remettre `echange` à `False` ? À quel moment la passer à `True` ? Où la tester ?

??? corrige "Corrigé"

    **1.** Un passage compare chaque couple de voisins et les remet en ordre :

    ```python
    def un_passage(t):
        for j in range(len(t) - 1):
            if t[j] > t[j + 1]:
                temp = t[j]                 # echange via variable temporaire
                t[j] = t[j + 1]
                t[j + 1] = temp
    ```

    Sur `[5, 3, 8, 1, 9, 2]`, un passage donne `[3, 5, 1, 8, 2, 9]` : le **9** (le plus grand) se retrouve en dernière position.

    **2.** Le plus grand élément, dès qu’il est atteint par le parcours, est plus grand que son voisin de droite : il est donc échangé, et « poussé » d’un cran vers la droite à *chaque* comparaison suivante. Il glisse ainsi jusqu’au bout : après un passage complet, il est forcément tout à droite.

    **3.** Puisque chaque passage place au moins un élément (le plus grand restant) à sa position définitive à droite, $n-1$ passages suffisent. Le $i$-ème passage peut s’arrêter plus tôt (la fin est déjà triée) :

    ```python
    def tri_bulle(t):
        n = len(t)
        for i in range(n - 1):
            for j in range(n - 1 - i):   # la fin, deja triee, est ignoree
                if t[j] > t[j + 1]:
                    temp = t[j]
                    t[j] = t[j + 1]
                    t[j + 1] = temp
    ```

    **4.** <span class="horsprog">au-delà du programme</span> Avec un drapeau `echange` :

    ```python
    def tri_bulle_optimise(t):
        n = len(t)
        for i in range(n - 1):
            echange = False
            for j in range(n - 1 - i):
                if t[j] > t[j + 1]:
                    temp = t[j]
                    t[j] = t[j + 1]
                    t[j + 1] = temp
                    echange = True
            if not echange:      # aucun echange : c'est deja trie
                return
    ```

    Sur un tableau déjà trié, le **premier** passage ne fait aucun échange : la fonction s’arrête après **un seul** passage (coût linéaire).

### Le coût d’un tri

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 12</span> — Linéaire ou quadratique ? <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-06-12 }

Pour chacune des affirmations, répondre par vrai ou faux et justifier.

1.  Le tri par sélection fait le même nombre de comparaisons, que le tableau soit trié ou non.

2.  Le tri par insertion est plus rapide sur un tableau déjà trié.

3.  Doubler la taille d’un tableau multiplie par 2 le temps d’un tri quadratique.

??? corrige "Corrigé"

    **1. Vrai.** Le tri par sélection compare toujours $\frac{n(n-1)}{2}$ paires, que le tableau soit trié ou non : il ne « profite » jamais d’un tableau déjà ordonné.  
    **2. Vrai.** Sur un tableau déjà trié, la boucle `while` de l’insertion ne décale rien : coût linéaire, bien meilleur.  
    **3. Faux.** Un coût quadratique varie comme $n^2$ : doubler $n$ multiplie le temps par $\mathbf{4}$, pas par 2.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 13</span> — Compter les comparaisons de la sélection <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-13 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `nb_comparaisons_selection(t)` qui trie `t` par sélection **et** renvoie le nombre de comparaisons `t[j] < t[i_min]` effectuées.

1.  Combien vaut ce nombre pour un tableau de 5 éléments ? de 10 ?

2.  Vérifier expérimentalement la formule $\dfrac{n(n-1)}{2}$ vue en cours.

    ??? pouce "Coup de pouce"

        Repartir du tri par sélection du cours, où la recherche du minimum est écrite en entier : la comparaison à compter y apparaît une seule fois. Un compteur augmenté de 1 à chaque fois qu’elle est évaluée suffit.

??? corrige "Corrigé"

    ```python
    def nb_comparaisons_selection(t):
        n = len(t)
        c = 0
        for i in range(n):
            i_min = i
            for j in range(i + 1, n):
                c = c + 1              # une comparaison t[j] < t[i_min]
                if t[j] < t[i_min]:
                    i_min = j
            temp = t[i]
            t[i] = t[i_min]
            t[i_min] = temp
        return c
    ```

    **1.** Pour $n = 5$ : $\frac{5 \times 4}{2} = 10$ comparaisons. Pour $n = 10$ : $\frac{10 \times 9}{2} = 45$.  
    **2.** Quel que soit le contenu du tableau, on obtient toujours $\frac{n(n-1)}{2}$ : le nombre de comparaisons ne dépend que de la **taille**, ce qui confirme le coût quadratique.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 14</span> — Vérifier qu’un tableau est trié <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-14 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `est_trie(t)` qui renvoie `True` si `t` est trié dans l’ordre croissant, `False` sinon (s’arrêter dès qu’on trouve une « descente »). Quel est son coût ? À quoi peut servir cette fonction pour *tester* vos tris ?

??? pouce "Coup de pouce"

    Comparer chaque élément à son voisin de droite : quel est le dernier indice `i` pour lequel `t[i + 1]` existe ?

??? corrige "Corrigé"

    ```python
    def est_trie(t):
        for i in range(len(t) - 1):
            if t[i] > t[i + 1]:   # une descente : pas trie
                return False
        return True
    ```

    Coût **linéaire** (un seul parcours), avec arrêt anticipé dès la première descente. Elle sert de **test** : après avoir appliqué un tri, on peut vérifier que `est_trie(t)` vaut `True` et que `t` contient bien les mêmes éléments qu’au départ.

### Synthèse : vers le bac et au-delà

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 15</span> — Classement d’une compétition <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-15 }

Chaque concurrent est décrit par un p-uplet `(nom, temps)` et le tableau `resultats` les contient dans le désordre.

1.  <span class="run" title="À programmer et tester sur machine">▶</span> Adapter le tri par sélection en `classer(resultats)` qui trie le tableau par **temps croissant** (le plus rapide en premier). *On compare désormais les temps `resultats[j][1]`.*

    ??? pouce "Coup de pouce"

        Recopier le tri par sélection du cours : seule la ligne de comparaison change, l’échange déplace des p-uplets entiers.

2.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire `podium(resultats)` qui renvoie les **trois** premiers noms.

    ??? pouce "Coup de pouce"

        Une fois le tableau classé, où sont les trois plus rapides ? Dans un p-uplet `(nom, temps)`, à quel indice est le nom ?

```text
>>> classer([("Ana", 53), ("Bob", 47), ("Cid", 61)])
[('Bob', 47), ('Ana', 53), ('Cid', 61)]
```

??? corrige "Corrigé"

    **1.** On reprend le tri par sélection en comparant les **temps**, c’est-à-dire le second élément `resultats[j][1]` de chaque p-uplet :

    ```python
    def classer(resultats):
        n = len(resultats)
        for i in range(n):
            i_min = i
            for j in range(i + 1, n):
                if resultats[j][1] < resultats[i_min][1]:
                    i_min = j
            temp = resultats[i]
            resultats[i] = resultats[i_min]
            resultats[i_min] = temp
        return resultats
    ```

    **2.** Une fois le tableau classé, les trois plus rapides occupent les cases 0, 1 et 2 ; on garde le **nom** (indice 0) de chacun, en construisant la liste par compréhension :

    ```python
    def podium(resultats):
        classer(resultats)
        return [resultats[i][0] for i in range(3)]
    ```

    *Autre méthode :* écrire directement les trois noms, `return [resultats[0][0], resultats[1][0], resultats[2][0]]`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 16</span> — La médiane <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-16 }

<span class="run" title="À programmer et tester sur machine">▶</span> La **médiane** d’une série de nombres est la valeur du milieu quand on les range dans l’ordre. Écrire `mediane(t)` qui trie une **copie** de `t` (pour ne pas modifier l’original — utiliser `list(t)`) puis renvoie l’élément central (on suppose `len(t)` **impair**). En quoi trier rend-il ce calcul facile ?

??? pouce "Coup de pouce"

    Dans un tableau trié de taille impaire, à quel indice se trouve l’élément central ? Essayer avec 3, puis 5 éléments, et relier cet indice à `len(t)`.

??? corrige "Corrigé"

    On trie une **copie** (pour ne pas modifier l’original) et on lit l’élément central.

    ```python
    def mediane(t):
        copie = list(t)          # copie : l'original n'est pas modifie
        tri_selection(copie)
        return copie[len(copie) // 2]
    ```

    *Autre méthode :* la fonction `sorted` (vue avec les tableaux) renvoie directement une copie triée, sans toucher à `t` : `copie = sorted(t)` remplace les deux premières lignes.

    Une fois le tableau trié, la médiane est *simplement* l’élément du milieu : le tri a fait tout le travail. (Sans tri, il faudrait un algorithme bien plus subtil.)

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 17</span> — Chasse aux doublons <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-17 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `a_un_doublon(t)` qui renvoie `True` si deux éléments de `t` sont égaux. **Stratégie maligne** : trier une copie du tableau, puis se contenter d’un **seul** parcours pour comparer chaque élément à son *voisin*. Une fois le tri fait, quel est le coût du reste de l’algorithme ?

??? pouce "Coup de pouce"

    Après le tri, où se trouvent deux valeurs égales l’une par rapport à l’autre ? Il suffit alors de comparer chaque case à la suivante.

??? pouce "Coup de pouce 2 (début de solution)"

    `copie = list(t)`  
    `tri_selection(copie)`  
    `for i in range(len(copie) - 1):`  
    `...`

??? corrige "Corrigé"

    Après tri, deux valeurs égales sont forcément **voisines** : un seul parcours suffit à les repérer.

    ```python
    def a_un_doublon(t):
        copie = list(t)
        tri_selection(copie)          # cout quadratique
        for i in range(len(copie) - 1):
            if copie[i] == copie[i + 1]:
                return True
        return False                  # aucun voisin egal
    ```

    Une fois le tri effectué, le parcours de comparaison des voisins est **linéaire**. Le coût total est donc dominé par le tri : quadratique.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 18</span> — Presque trié <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-18 }

On dit qu’un tableau est *presque trié* si chaque élément est à au plus une case de sa position finale. On donne à trier un tel tableau : `[2, 1, 4, 3, 6, 5]`.

1.  Combien de *décalages* le tri par insertion effectue-t-il ? Le comparer au tri par sélection.

    ??? pouce "Coup de pouce"

        Dérouler l’insertion à la main : de combien de cases chaque élément inséré recule-t-il ? On peut aussi vérifier avec `tri_insertion_compte`.

    ??? pouce "Coup de pouce 2 (début de solution)"

        Insérer `1` : un décalage (le `2`) ; insérer `4` : aucun ; insérer `3` : … Pour la sélection, le nombre de comparaisons ne dépend que de $n$ : formule $\frac{n(n-1)}{2}$.

2.  En déduire lequel des deux tris on préférerait pour des données *déjà presque en ordre* (par exemple une liste triée dans laquelle on vient d’ajouter quelques éléments). <span class="horsprog">au-delà du programme</span>

??? corrige "Corrigé"

    **1.** Sur `[2, 1, 4, 3, 6, 5]`, le tri par **insertion** ne fait que **3** décalages (chaque petit élément recule d’une seule case) : le travail est proportionnel au **désordre**. Le tri par **sélection**, lui, refait ses $\frac{n(n-1)}{2} = 15$ comparaisons, sans profiter du bon ordre initial.  
    **2.** <span class="horsprog">au-delà du programme</span> On préfère nettement le tri par **insertion** pour des données presque en ordre : son coût s’approche du linéaire. C’est pour cela qu’il est utilisé comme brique dans des tris performants (comme Timsort) sur les portions déjà quasi triées.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 19</span> — Les k plus petits <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-19 }

<span class="run" title="À programmer et tester sur machine">▶</span> Pour afficher les $k$ meilleurs temps d’une course de $n$ coureurs, inutile de tout trier.

```text
>>> k_plus_petits([53, 47, 61, 50, 49, 58], 3)
[47, 49, 50]
```

1.  Écrire `k_plus_petits(t, k)` qui renvoie un tableau contenant, dans l’ordre croissant, les `k` plus petits éléments de `t` (on suppose `k <= len(t)`). On s’interdit de trier le tableau en entier : on n’effectue que les `k` premières étapes d’un tri par sélection, sur une copie de `t`.

2.  Combien de comparaisons sont effectuées pour $k = 3$ et $n = 100$ ? Comparer avec les $\frac{n(n-1)}{2}$ d’un tri complet.

??? pouce "Coup de pouce"

    Quelle propriété du tri par sélection garantit qu’après `k` étapes, les `k` premières cases contiennent déjà les `k` plus petits éléments, à leur place définitive ?

??? pouce "Coup de pouce 2 (début de solution)"

    `copie = list(t)`  
    `for i in range(k):`  
    `i_min = indice_min(copie, i)`  
    `...` (échange) puis renvoyer `copie[0:k]`.

??? corrige "Corrigé"

    **1.** D’après l’invariant du tri par sélection, après `k` étapes les `k` premières cases contiennent les `k` plus petits éléments, triés et à leur place définitive : on peut s’arrêter là.

    ```python
    def k_plus_petits(t, k):
        copie = list(t)                 # on ne modifie pas t
        for i in range(k):              # k etapes seulement
            i_min = indice_min(copie, i)
            temp = copie[i]
            copie[i] = copie[i_min]
            copie[i_min] = temp
        return copie[0:k]
    ```

    **2.** Les trois étapes font $99 + 98 + 97 = 294$ comparaisons, contre $\frac{100 \times 99}{2} = 4\,950$ pour un tri complet : environ 17 fois moins. Le coût est de l’ordre de $k \times n$ : **linéaire** en $n$ quand $k$ est fixé.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 20</span> — Trier des mots par longueur <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-20 }

On veut ranger des mots du plus court au plus long, **sans** changer l’ordre de départ des mots de même longueur.

```text
>>> mots = ["pomme", "kiwi", "figue", "noix", "ananas"]
>>> tri_longueur(mots)
>>> mots
['kiwi', 'noix', 'pomme', 'figue', 'ananas']
```

1.  <span class="run" title="À programmer et tester sur machine">▶</span> Adapter le tri par insertion en `tri_longueur(mots)`, qui compare les **longueurs** des mots. Vérifier qu’on obtient bien la sortie ci-dessus.

2.  Dans la condition du `while`, que se passerait-il si l’on remplaçait `>` par `>=` ? Le vérifier sur l’exemple et expliquer.

3.  **Sans machine** : le tri par sélection respecte-t-il, lui aussi, l’ordre de départ des mots de même longueur ? Chercher un exemple de trois mots qui tranche la question.

??? pouce "Coup de pouce"

    Question 1 : seule la comparaison change, on compare `len(mots[j])` et `len(x)`. Question 2 : dérouler l’insertion de `"noix"` derrière `"kiwi"`. Question 3 : un échange peut faire « sauter » un mot par-dessus un autre de même longueur.

??? pouce "Coup de pouce 2 (début de solution)"

    Question 3 : essayer la sélection sur `["abc", "xyz", "a"]`, étape par étape.

??? corrige "Corrigé"

    **1.** Seule la comparaison change : on compare les longueurs.

    ```python
    def tri_longueur(mots):
        for i in range(1, len(mots)):
            x = mots[i]
            j = i - 1
            while j >= 0 and len(mots[j]) > len(x):
                mots[j + 1] = mots[j]
                j = j - 1
            mots[j + 1] = x
    ```

    **2.** Avec `>=`, un mot recule aussi derrière les mots de **même** longueur : `"noix"` passe devant `"kiwi"`, `"figue"` devant `"pomme"`. On obtient `[’noix’, ’kiwi’, ’figue’, ’pomme’, ’ananas’]` : trié par longueur, mais l’ordre de départ des ex æquo est inversé. Avec `>` strict, on s’arrête dès qu’on rencontre un mot de même longueur : l’ordre de départ est conservé (on dit que le tri est *stable*).  
    **3.** Non. Sur `["abc", "xyz", "a"]` : à l’étape 0, le plus court est `"a"`, échangé avec `"abc"` $\to$ `["a", "xyz", "abc"]`, et plus rien ne bouge ensuite. `"abc"` et `"xyz"` ont la même longueur, mais leur ordre de départ est inversé : l’échange a fait « sauter » `"abc"` par-dessus `"xyz"`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 21</span> — Un tri selon un assistant d’IA <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> { #ex-06-21 }

Un élève demande à un assistant d’IA : « Écris le tri par sélection en Python, en place. » Voici la réponse obtenue.

```python
def tri_selection(t):
    n = len(t)
    for i in range(n):
        i_min = i
        for j in range(i + 1, n):
            if t[j] < t[i_min]:
                i_min = j
        t[i] = t[i_min]       # on place le minimum en position i
```

« À chaque étape `i`, la boucle interne trouve l’indice du minimum de la partie non triée, puis ce minimum est placé en position `i`. Après `n` étapes, le tableau est trié. Le coût est quadratique. »

1.  La réponse est-elle correcte ? Dérouler `tri_selection(t)` à la main sur `t = [5, 2, 4, 1]`, en écrivant le tableau après chaque étape `i`.

2.  Localiser et corriger l’erreur.

3.  Quelle vérification simple, faite avant de faire confiance à la réponse, aurait suffi à détecter l’erreur ?

    ??? pouce "Coup de pouce"

        Après chaque étape `i`, vérifier que toutes les valeurs de départ sont encore présentes dans le tableau.

??? corrige "Corrigé"

    **1.** Non. Sur `[5, 2, 4, 1]` : étape `i = 0`, minimum `1` (case 3), on écrit `t[0] = 1` $\to$ `[1, 2, 4, 1]` : le `5` a **disparu**, écrasé. Étape `i = 1` : minimum `1` (case 3) $\to$ `[1, 1, 4, 1]`. Étape `i = 2` : $\to$ `[1, 1, 1, 1]`. Étape `i = 3` : inchangé. Résultat **`[1, 1, 1, 1]`** : le tableau n’est pas trié, il a perdu ses éléments. **2.** L’erreur est la ligne `t[i] = t[i_min]` : on *recopie* le minimum au lieu de l’**échanger** avec `t[i]`, et la valeur qui était en `t[i]` est perdue. Correction (échange via une variable temporaire, comme dans le cours) :

    ```python
            temp = t[i]
            t[i] = t[i_min]
            t[i_min] = temp
    ```

    Avec cette correction, `[5, 2, 4, 1]` devient `[1, 2, 4, 5]`. **3.** Exécuter la fonction sur un petit tableau et **afficher le résultat** : `[1, 1, 1, 1]` saute aux yeux. Un tri ne doit jamais changer le *contenu* du tableau, seulement l’ordre : vérifier que toutes les valeurs sont encore là est le premier test à faire.
