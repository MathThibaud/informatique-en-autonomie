# Exercices

<p class="sous-titre">Algorithmique : le parcours séquentiel</p>

!!! consignes "Mode d’emploi"

    - Niveau : ★ échauffement, ★★ classique (niveau bac), ★★★ défi ; les *coups de pouce* et les *corrigés* se déplient sous chaque exercice.

    - <span class="run" title="À programmer et tester sur machine">▶</span> *À programmer et tester* en Python. Le symbole `>>>` figure une saisie dans la console.

    - **Sauf mention contraire**, on n’utilise **pas** les fonctions toutes faites `sum`, `max`, `min` : le but est d’écrire le **parcours** soi-même.

    - **Réflexe coût** : pour chaque fonction, se demander *combien de fois* on parcourt le tableau.

    - Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la [charte d’usage de l’IA](../charte.md).

### Le patron du parcours

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — Lecture de trace <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-04-1 }

Sans machine, dire ce que renvoie `mystere([4, 1, 7, 2])`.

```python
def mystere(t):
    r = 0
    for x in t:
        if x > r:
            r = x
    return r
```

Que calcule cette fonction en général ? Renvoie-t-elle un résultat correct si tous les éléments sont négatifs ? Expliquer.

??? corrige "Corrigé"

    !!! remarque "Remarque"

        On donne **une** version simple ; d’autres écritures sont possibles.

    `mystere([4, 1, 7, 2])` renvoie `7`. La fonction calcule le **maximum** du tableau… mais **seulement s’il est positif** : le champion initial est `0`. Sur un tableau tout négatif, comme `[-3, -7]`, elle renvoie `0`, qui n’est **pas** un élément du tableau : résultat **faux**. Il fallait initialiser avec `t[0]`.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 2</span> — Reconnaître le patron <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-04-2 }

<span class="run" title="À programmer et tester sur machine">▶</span> En suivant le patron du cours (initialisation, mise à jour, renvoi), écrire :

1.  `produit(t)` : le produit de tous les éléments ;

2.  `concatener(mots)` : la chaîne obtenue en collant tous les mots d’un tableau de chaînes.

??? corrige "Corrigé"

    ```python
    def produit(t):
        p = 1                     # element neutre de la multiplication
        for x in t:
            p = p * x
        return p

    def concatener(mots):
        resultat = ""             # element neutre de la concatenation
        for mot in mots:
            resultat = resultat + mot
        return resultat
    ```

### Décliner : comptages, moyennes

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 3</span> — Compter dans un intervalle : code à trous <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-04-3 }

La fonction `nb_entre(t, a, b)` doit renvoyer le nombre d’éléments du tableau `t` compris entre `a` et `b` (bornes incluses). Recopier et compléter les pointillés en suivant le patron du parcours (initialisation, mise à jour, renvoi).

```python
def nb_entre(t, a, b):
    c = ......
    for x in ......:
        if ...... and ......:
            c = ......
    return ......
```

```text
>>> nb_entre([12, 5, 18, 9, 15], 10, 15)
2
```

??? corrige "Corrigé"

    ```python
    def nb_entre(t, a, b):
        c = 0                       # compteur : element neutre 0
        for x in t:
            if x >= a and x <= b:   # mise a jour conditionnelle
                c = c + 1
        return c
    ```

    `nb_entre([12, 5, 18, 9, 15], 10, 15)` renvoie bien `2` (les éléments `12` et `15`). Les deux conditions sont reliées par `and` : il faut *à la fois* `x >= a` et `x <= b`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 4</span> — Taux de réussite et moyenne pondérée <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-4 }

<span class="run" title="À programmer et tester sur machine">▶</span> Les notes d’un élève sont rangées dans un tableau `notes` **non vide** ; le tableau `coefs`, de même longueur, donne leurs coefficients (`coefs[i]` est le coefficient de `notes[i]`). Écrire :

1.  `taux_reussite(notes)` : le pourcentage de notes supérieures ou égales à `10` ;

2.  `moyenne_ponderee(notes, coefs)` : la somme des produits `notes[i] * coefs[i]`, divisée par la somme des coefficients.

```text
>>> taux_reussite([12, 8, 15, 9])
50.0
>>> moyenne_ponderee([12, 8, 15], [2, 1, 1])
11.75
```

??? pouce "Coup de pouce"

    Question 1 : un compteur, puis une division par le nombre de notes. Question 2 : deux accumulateurs mis à jour dans la *même* boucle ; il faut lire à la fois `notes[i]` et `coefs[i]`, donc parcourir par indice.

??? pouce "Coup de pouce 2 (début de solution)"

    `def moyenne_ponderee(notes, coefs):`  
    `total = 0`  
    `total_coefs = 0`  
    `for i in range(len(notes)):`

??? corrige "Corrigé"

    ```python
    def taux_reussite(notes):
        c = 0
        for note in notes:
            if note >= 10:
                c = c + 1
        return 100 * c / len(notes)

    def moyenne_ponderee(notes, coefs):
        total = 0                   # somme des notes[i] * coefs[i]
        total_coefs = 0             # somme des coefficients
        for i in range(len(notes)):
            total = total + notes[i] * coefs[i]
            total_coefs = total_coefs + coefs[i]
        return total / total_coefs
    ```

    Pour `moyenne_ponderee`, on parcourt par **indice** : le même `i` donne la note et son coefficient. Les deux accumulateurs sont mis à jour dans la même boucle : un seul parcours. Sur l’exemple : $(12 \times 2 + 8 + 15) / (2 + 1 + 1) = 47 / 4 = 11{,}75$.

### Recherche séquentielle

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 5</span> — Un multiple dans le tableau <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-04-5 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `a_un_multiple(t, k)` qui renvoie `True` si au moins un élément de `t` est un multiple de `k`, `False` sinon. La fonction doit **s’arrêter** dès qu’un multiple est trouvé. Combien de tours de boucle effectue `a_un_multiple([7, 10, 3, 20], 5)` ? Et `a_un_multiple([7, 10, 3, 20], 6)` ?

??? pouce "Coup de pouce"

    `x` est un multiple de `k` quand `x % k == 0`. Où placer `return False` : dans la boucle ou après ?

??? corrige "Corrigé"

    ```python
    def a_un_multiple(t, k):
        for x in t:
            if x % k == 0:
                return True       # on s'arrete des qu'on trouve
        return False              # parcours fini sans succes
    ```

    `a_un_multiple([7, 10, 3, 20], 5)` fait **2** tours : `10` est trouvé au deuxième tour, et `return` arrête aussitôt la fonction. `a_un_multiple([7, 10, 3, 20], 6)` fait **4** tours : aucun multiple de 6, il faut tout parcourir avant de répondre `False`. C’est le pire cas.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Où est-il ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-6 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire :

1.  `premiere_voyelle(mot)` : l’indice de la **première** voyelle (`a`, `e`, `i`, `o`, `u`, `y`) de la chaîne `mot`, ou `-1` s’il n’y en a pas ;

2.  `dernier_indice(t, x)` : l’indice de la **dernière** occurrence de `x` dans le tableau `t`, ou `-1` si `x` est absent.

```text
>>> premiere_voyelle("schtroumpf")
5
>>> dernier_indice([4, 1, 4, 2], 4)
2
```

??? pouce "Coup de pouce"

    Première voyelle : parcourir par indice, tester `mot[i] in "aeiouy"` et s’arrêter dès qu’on trouve. Dernière occurrence : soit parcourir tout le tableau en mémorisant le dernier indice rencontré, soit parcourir les indices à l’envers.

??? corrige "Corrigé"

    Pour la **première** voyelle, on renvoie dès qu’on trouve. Pour la **dernière** occurrence, en parcourant de gauche à droite, on ne peut pas s’arrêter tôt : une autre occurrence peut encore venir. On retient donc le dernier indice vu, jusqu’au bout du tableau.

    ```python
    def premiere_voyelle(mot):
        for i in range(len(mot)):
            if mot[i] in "aeiouy":
                return i
        return -1

    def dernier_indice(t, x):
        resultat = -1
        for i in range(len(t)):
            if t[i] == x:
                resultat = i      # on ecrase : on garde le dernier
        return resultat
    ```

    *Autre méthode* pour `dernier_indice` : parcourir les indices **à l’envers**, du dernier au premier : la première occurrence rencontrée est alors la dernière du tableau, et on peut s’arrêter dès qu’on la trouve.

    ```python
    def dernier_indice(t, x):
        for i in range(len(t) - 1, -1, -1):
            if t[i] == x:
                return i
        return -1
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Recherche sous condition <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-7 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `premier_negatif(t)` qui renvoie le premier élément strictement négatif rencontré, ou `None` s’il n’y en a pas.

```text
>>> premier_negatif([4, 7, -2, 9, -5])
-2
```

??? pouce "Coup de pouce"

    Même structure que `a_un_multiple` : on renvoie l’élément dès que la condition est vraie. Que renvoyer si la boucle se termine sans succès ?

??? corrige "Corrigé"

    ```python
    def premier_negatif(t):
        for x in t:
            if x < 0:
                return x
        return None
    ```

### Minimum, maximum et champion

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 8</span> — Le plus petit <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-04-8 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `minimum(t)` (tableau non vide), **sans** `min`. Préciser l’**invariant** de votre boucle. Pourquoi serait-il faux d’initialiser le champion à `0` ? (Penser au tableau `[3, 8, 5]`.)

??? corrige "Corrigé"

    ```python
    def minimum(t):
        m = t[0]
        for x in t:
            if x < m:
                m = x
        return m
    ```

    **Invariant** : à chaque tour, `m` est le minimum des éléments déjà visités. Initialiser `m` à `0` serait faux : sur `[3, 8, 5]`, aucun élément n’est inférieur à `0`, et la fonction renverrait `0`, qui n’est même pas dans le tableau (c’est le défaut de l’exercice « Lecture de trace »). On initialise avec un élément *existant* : `t[0]`.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 9</span> — Le mot le plus long : lignes à remettre dans l’ordre <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-04-9 }

Les lignes de la fonction `mot_le_plus_long(mots)` (tableau de chaînes **non vide**) ont été mélangées et leur indentation a été perdue. Les recopier **dans le bon ordre** et **correctement indentées**, puis <span class="run" title="À programmer et tester sur machine">▶</span> tester sur `["chat", "girafe", "ours", "souris"]`. Pourquoi obtient-on `"girafe"` et non `"souris"`, qui a pourtant la même longueur ?

```text
return champion
champion = mot
def mot_le_plus_long(mots):
if len(mot) > len(champion):
champion = mots[0]
for mot in mots:
```

??? corrige "Corrigé"

    ```python
    def mot_le_plus_long(mots):
        champion = mots[0]
        for mot in mots:
            if len(mot) > len(champion):
                champion = mot
        return champion
    ```

    À noter : `champion = mots[0]` se place **avant** la boucle (initialisation du champion) ; `return champion` est au niveau de la boucle, **après** elle (sinon on renverrait dès le premier tour). Sur l’exemple, on obtient `"girafe"` : quand arrive `"souris"`, le test `len(mot) > len(champion)` compare `6 > 6`, qui est faux. La comparaison **stricte** garde donc le **premier** mot de longueur maximale.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 10</span> — La position du champion <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-10 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `indice_du_min(t)` qui renvoie l’indice du plus petit élément (le premier en cas d’égalité).

??? pouce "Coup de pouce"

    Retenir l’*indice* du champion, pas sa valeur : parcourir par indice et comparer `t[i]` à la valeur du champion. Faut-il `<` ou `<=` pour garder le premier en cas d’égalité ?

??? corrige "Corrigé"

    ```python
    def indice_du_min(t):
        i_min = 0
        for i in range(len(t)):
            if t[i] < t[i_min]:   # strict : on garde le PREMIER en cas d'egalite
                i_min = i
        return i_min
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 11</span> — Amplitude <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-11 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `amplitude(t)` qui renvoie la différence entre le plus grand et le plus petit élément d’un tableau non vide. Combien de parcours votre solution effectue-t-elle ?

??? pouce "Coup de pouce"

    Il faut deux « champions » : le plus grand et le plus petit. Peut-on les mettre à jour dans la même boucle ?

??? corrige "Corrigé"

    ```python
    def amplitude(t):
        plus_petit = t[0]
        plus_grand = t[0]
        for x in t:
            if x < plus_petit:
                plus_petit = x
            if x > plus_grand:
                plus_grand = x
        return plus_grand - plus_petit
    ```

    Cette solution fait **un seul** parcours (on cherche min et max en même temps). Deux parcours séparés donneraient le même résultat, en deux fois plus de tours.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 12</span> — Moyenne de fin de trimestre <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-12 }

<span class="run" title="À programmer et tester sur machine">▶</span> Les notes d’un élève sont dans un tableau. Écrire `moyenne_sans_pire(t)` qui calcule la moyenne **après avoir retiré la plus mauvaise note**. On supposera au moins deux notes.

```text
>>> moyenne_sans_pire([8, 12, 15, 5])
11.666666666666666
```

??? pouce "Coup de pouce"

    Faut-il vraiment retirer la note du tableau ? Une fois la pire note enlevée, que deviennent la somme des notes et leur nombre ?

??? corrige "Corrigé"

    On retire une fois la plus mauvaise note de la somme, et on divise par `len(t) - 1`. La somme et la pire note se calculent dans le même parcours.

    ```python
    def moyenne_sans_pire(t):
        pire = t[0]
        total = 0
        for x in t:
            total = total + x
            if x < pire:
                pire = x
        return (total - pire) / (len(t) - 1)
    ```

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 13</span> — Le deuxième plus grand <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-13 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `deuxieme_max(t)` qui renvoie le deuxième plus grand élément *distinct* d’un tableau (on suppose au moins deux valeurs distinctes), en **un seul** parcours.

```text
>>> deuxieme_max([3, 9, 9, 7, 2])
7
```

??? pouce "Coup de pouce"

    Garder deux champions : `premier` (le plus grand vu) et `second`. Quand un élément bat `premier`, que devient l’ancien `premier` ? Et que faire d’un élément égal à `premier` ?

??? pouce "Coup de pouce 2 (début de solution)"

    `premier = None`  
    `second = None`  
    `for x in t:`  
    puis distinguer deux cas : `x` bat `premier` ; `x` se place entre `second` et `premier`.

??? corrige "Corrigé"

    On tient à jour **deux** champions : le plus grand (`premier`) et le deuxième plus grand *distinct* (`second`), initialisés à `None` (« pas encore de champion »). Pour chaque élément `x`, deux cas utiles : `x` bat le record (l’ancien premier passe deuxième) ; ou `x` est strictement plus petit que `premier` et bat `second`. Un élément *égal* à `premier` ne change rien.

    ```python
    def deuxieme_max(t):
        premier = None       # plus grand vu
        second = None        # 2e plus grand DISTINCT
        for x in t:
            if premier == None or x > premier:     # nouveau record
                second = premier
                premier = x
            elif x < premier:                      # entre second et premier ?
                if second == None or x > second:
                    second = x
        return second
    ```

    On écrit ici `== None` ; le chapitre *Spécifier et mettre au point ses programmes* présentera l’écriture recommandée `is None`.

### Invariants de boucle

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 14</span> — Que contient la variable ? <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-04-14 }

On considère la fonction suivante :

```python
def f(t):
    c = 0
    for x in t:
        if x % 2 == 0:
            c = c + 1
    return c
```

1.  Énoncer l’**invariant** de la boucle : que contient `c` à chaque tour ?

2.  En déduire ce que calcule la fonction.

??? corrige "Corrigé"

    **1.** Invariant : à chaque tour, `c` contient le **nombre d’éléments pairs déjà visités**.  
    **2.** À la fin, tous les éléments ont été visités : la fonction renvoie le **nombre d’éléments pairs** du tableau.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 15</span> — Énoncer un invariant <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-04-15 }

On reprend la fonction `produit(t)` (initialisation `p = 1`, puis `p = p * x` à chaque tour).

1.  Énoncer l’**invariant** de la boucle (ce que contient `p` à chaque tour).

2.  Expliquer en une phrase pourquoi cet invariant **garantit** que le résultat final est correct.

??? pouce "Coup de pouce"

    S’inspirer de l’invariant du champion : « `p` contient … des éléments **déjà visités** ». Que sont les éléments déjà visités à la sortie de la boucle ?

??? corrige "Corrigé"

    **1.** Invariant : à chaque tour, `p` contient le **produit des éléments déjà visités** (et `p = 1`, produit vide, avant le premier tour).  
    **2.** Comme l’invariant est vrai à chaque tour, il l’est encore au dernier : quand tous les éléments ont été visités, `p` est le produit de *tout* le tableau — le résultat est donc correct.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 16</span> — Une preuve d’invariant en deux étapes <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-16 }

On considère `nb_positifs(t)`, qui compte les éléments strictement positifs (initialisation `c = 0` ; à chaque tour, `c = c + 1` si `x > 0`). Soit la propriété $$P : \text{«~\texttt{c} contient le nombre d'éléments strictement positifs \textbf{déjà visités}~».}$$ En suivant la méthode du cours, **démontrer** que $P$ est un invariant :

1.  **Initialisation** : montrer que $P$ est vraie avant le premier tour.

2.  **Hérédité** : en supposant $P$ vraie avant un tour, montrer qu’elle l’est encore après (distinguer les cas `x > 0` et `x <= 0`).

3.  **Conclusion** : expliquer pourquoi la fonction renvoie bien le nombre d’éléments positifs du tableau entier.

??? pouce "Coup de pouce"

    Initialisation : avant le premier tour, combien d’éléments ont été visités, et combien de positifs parmi eux ? Hérédité : partir de « `c` = nombre de positifs déjà visités » et regarder l’effet du nouvel élément `x`.

??? pouce "Coup de pouce 2 (début de solution)"

    Hérédité, cas `x > 0` : le nombre de positifs déjà visités augmente de `1`, et l’instruction `c = c + 1` fait de même. Rédiger ensuite le cas `x <= 0`, puis la conclusion.

??? corrige "Corrigé"

    **1. Initialisation.** Avant le premier tour, aucun élément n’a été visité et `c = 0` : il y a bien `0` élément positif parmi les éléments visités (il n’y en a aucun). $P$ est vraie.

    **2. Hérédité.** Supposons $P$ vraie avant un tour : `c` est le nombre de positifs déjà vus. On visite `x`, deux cas :

    - `x > 0` : on fait `c = c + 1`. `x` étant positif, le nombre de positifs vus augmente de 1 : `c` est à jour.

    - `x <= 0` : `c` ne change pas. `x` n’étant pas positif, le nombre de positifs vus ne change pas non plus : `c` est à jour.

    Dans les deux cas, $P$ est encore vraie après le tour.

    **3. Conclusion.** $P$ est vraie au départ et se conserve : elle est donc vraie à chaque tour, en particulier à la fin, quand tous les éléments ont été visités. `c` contient alors le nombre d’éléments strictement positifs de *tout* le tableau. $\square$

### Le coût : linéaire ou quadratique ?

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 17</span> — Compter les tours <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-04-17 }

Pour chaque fonction, dire combien de tours de boucle sont effectués pour un tableau de `n` éléments, et si le coût est **linéaire** ou **quadratique**.

```python
# (a)                              # (b)
def f(t):                          def g(t):
    s = 0                              c = 0
    for x in t:                        for i in range(len(t)):
        s = s + x                          for j in range(len(t)):
    return s                                   if t[i] == t[j]:
                                                   c = c + 1
                                       return c
```

??? corrige "Corrigé"

    **(a)** `n` tours de boucle : coût **linéaire**. **(b)** deux boucles imbriquées sur `t` : $n \times n = n^2$ tours : coût **quadratique**.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 18</span> — Min et max en une seule passe <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-18 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `mini_maxi(t)` qui renvoie le p-uplet `(min, max)` en **un seul** parcours du tableau. Comparer au coût de deux parcours séparés.

??? pouce "Coup de pouce"

    Deux champions initialisés avec `t[0]`, et deux tests dans le même tour de boucle. Combien de tours font deux parcours séparés ?

??? corrige "Corrigé"

    ```python
    def mini_maxi(t):
        mini = t[0]
        maxi = t[0]
        for x in t:
            if x < mini:
                mini = x
            if x > maxi:
                maxi = x
        return mini, maxi
    ```

    Un seul parcours ($n$ tours) au lieu de deux ($2n$ tours) : deux fois moins de **tours de boucle**, mais autant de **comparaisons** (deux par tour, soit $2n$ dans les deux cas). Le coût reste **linéaire**.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 19</span> — Détecter un doublon <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-19 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `a_un_doublon(t)` qui renvoie `True` si (au moins) deux éléments de `t` sont égaux. Quel est le coût de votre solution (en nombre de comparaisons dans le pire cas) ? <span class="horsprog">au-delà du programme</span>

??? pouce "Coup de pouce"

    Comparer chaque élément à ceux qui sont *après* lui : deux boucles imbriquées sur les indices. Attention à ne jamais comparer un élément à lui-même.

??? corrige "Corrigé"

    ```python
    def a_un_doublon(t):
        for i in range(len(t)):
            for j in range(i + 1, len(t)):   # on ne compare chaque paire qu'une fois
                if t[i] == t[j]:
                    return True
        return False
    ```

    Dans le pire cas (aucun doublon), on examine toutes les paires, soit environ $\dfrac{n^2}{2}$ comparaisons : coût **quadratique**. <span class="horsprog">au-delà du programme</span>

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 20</span> — Deux tableaux <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-20 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `element_commun(t1, t2)` qui renvoie `True` si les deux tableaux ont (au moins) un élément en commun. Combien de fois, dans le pire cas, compare-t-on deux éléments si `t1` et `t2` ont chacun `n` éléments ? Quel est le coût ? <span class="horsprog">au-delà du programme</span>

??? pouce "Coup de pouce"

    Pour chaque élément de `t1`, chercher s’il est dans `t2` : une recherche séquentielle à l’intérieur d’une autre boucle. Le pire cas : aucun élément commun.

??? pouce "Coup de pouce 2 (début de solution)"

    `for x in t1:`  
    `for y in t2:`  
    `if x == y:`

??? corrige "Corrigé"

    ```python
    def element_commun(t1, t2):
        for x in t1:
            for y in t2:
                if x == y:
                    return True
        return False
    ```

    Dans le pire cas (aucun élément commun), on compare chaque élément de `t1` à chaque élément de `t2`, soit $n \times n = n^2$ comparaisons : coût **quadratique**. <span class="horsprog">au-delà du programme</span>

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 21</span> — Moyenne, variance — et le piège du coût <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-21 }

C’est **l’exercice central** du chapitre. La variance mesure la dispersion : $V = \dfrac{1}{n}\displaystyle\sum_i (x_i - m)^2$, où $m$ est la moyenne.

1.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire `moyenne(t)` (un parcours).

2.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire `variance_naive(t)` en **appelant `moyenne(t)` à l’intérieur** de la boucle. La fonction est-elle correcte ?

3.  **Combien de fois** au total `variance_naive` additionne-t-elle des nombres pour un tableau de `n` éléments ? En déduire son coût.

4.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire `variance(t)` qui calcule la moyenne **une seule fois**, avant la boucle. Quel est son coût ?

5.  Vérifier que les deux versions donnent le **même** résultat sur `[2, 4, 4, 4, 5, 5, 7, 9]` (la variance vaut `4.0`). Laquelle utiliseriez-vous sur un million de valeurs, et pourquoi ?

??? pouce "Coup de pouce"

    Question 3 : `moyenne(t)` fait `n` additions, et `variance_naive` l’appelle à chaque tour de sa boucle. Combien de tours fait cette boucle ?

??? pouce "Coup de pouce 2 (début de solution)"

    `def variance(t):`  
    `m = moyenne(t)`  
    `s = 0`  
    `for x in t:`

??? corrige "Corrigé"

    **1, 2, 4.** Les trois fonctions :

    ```python
    def moyenne(t):              # 1.
        s = 0
        for x in t:
            s = s + x
        return s / len(t)

    def variance_naive(t):        # 2.
        n = len(t)
        s = 0
        for x in t:
            s = s + (x - moyenne(t)) ** 2     # moyenne(t) recalculee a chaque tour
        return s / n

    def variance(t):              # 4.
        n = len(t)
        m = moyenne(t)            # calculee UNE seule fois
        s = 0
        for x in t:
            s = s + (x - m) ** 2
        return s / n
    ```

    **2.** `variance_naive` est **correcte** : elle calcule bien la variance. **3.** À chacun des `n` tours, `moyenne(t)` effectue `n` additions : total $\approx n \times n = n^2$ additions. Coût **quadratique**. **4.** `variance` fait un parcours pour la moyenne puis un pour la somme : $\approx 2n$ opérations, coût **linéaire**. **5.** Les deux renvoient `4.0` sur l’exemple. Sur un million de valeurs, on utilise `variance` : la version naïve demanderait $\approx 10^{12}$ opérations (des heures), la version efficace $\approx 2\times 10^6$ (immédiat).

### Synthèse : petits problèmes

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 22</span> — Relevé météo <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-22 }

<span class="run" title="À programmer et tester sur machine">▶</span> Un tableau `temperatures` donne la température de chaque jour du mois.

1.  `jour_le_plus_chaud(temperatures)` : l’**indice** (le numéro du jour, à partir de 0) du maximum.

2.  `nb_jours_gel(temperatures)` : le nombre de jours où la température a été strictement négative.

3.  `plus_longue_serie_chaude(temperatures, seuil)` : la longueur de la plus longue série *consécutive* de jours au-dessus de `seuil`. <span class="horsprog">au-delà du programme</span>

??? pouce "Coup de pouce"

    1 : c’est la position du champion. 2 : un compteur. 3 : deux variables, la longueur de la série *en cours* et la meilleure longueur vue ; que devient la série en cours un jour plus froid ?

??? pouce "Coup de pouce 2 (début de solution)"

    `courante = 0`  
    `record = 0`  
    `for temp in temperatures:`  
    `if temp > seuil:`

??? corrige "Corrigé"

    ```python
    def jour_le_plus_chaud(temperatures):
        i_max = 0
        for i in range(len(temperatures)):
            if temperatures[i] > temperatures[i_max]:
                i_max = i
        return i_max

    def nb_jours_gel(temperatures):
        c = 0
        for temp in temperatures:
            if temp < 0:
                c = c + 1
        return c

    def plus_longue_serie_chaude(temperatures, seuil):   # au-dela du programme
        record = 0
        courante = 0
        for temp in temperatures:
            if temp > seuil:
                courante = courante + 1
                if courante > record:
                    record = courante
            else:
                courante = 0
        return record
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 23</span> — Vers le bac — contrôle de saisie <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-23 }

<span class="run" title="À programmer et tester sur machine">▶</span> Un tableau `notes` est censé ne contenir que des entiers entre `0` et `20`.

1.  `toutes_valides(notes)` : `True` si toutes les notes sont dans `[0 ; 20]`, `False` dès qu’une note sort de l’intervalle (s’arrêter tôt).

2.  `indices_invalides(notes)` : le tableau des indices des notes hors intervalle.

??? pouce "Coup de pouce"

    1 : renvoyer `False` dès qu’une note sort de l’intervalle, et `True` seulement après la boucle. 2 : partir d’un tableau vide et y ajouter des *indices*, donc parcourir par indice.

??? corrige "Corrigé"

    ```python
    def toutes_valides(notes):
        for note in notes:
            if note < 0 or note > 20:
                return False      # une seule note hors bornes suffit : on s'arrete
        return True

    def indices_invalides(notes):
        return [i for i in range(len(notes)) if notes[i] < 0 or notes[i] > 20]
    ```

    Pour `indices_invalides`, on parcourt par **indice** (c’est l’indice qu’on garde, pas la note). *Autre méthode :* la boucle avec `append` que la compréhension condense.

    ```python
    def indices_invalides(notes):
        resultat = []
        for i in range(len(notes)):
            if notes[i] < 0 or notes[i] > 20:
                resultat.append(i)
        return resultat
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 24</span> — Une recherche selon un assistant d’IA <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> { #ex-04-24 }

Un élève demande à un assistant d’IA : « Écris une fonction Python qui dit si une valeur `x` est présente dans un tableau `t`. » Voici la réponse obtenue.

```python
def est_present(t, x):
    """Renvoie True si x est dans t, False sinon."""
    for element in t:
        if element == x:
            return True
        else:
            return False
```

« La boucle parcourt le tableau : dès qu’un élément est égal à `x`, la fonction renvoie `True`, sinon elle renvoie `False`. Le coût est linéaire dans le pire des cas. »

1.  La réponse est-elle correcte ? Faire la trace de `est_present([3, 8, 5], 5)`.

2.  Localiser et corriger l’erreur.

3.  Quelle vérification simple, faite avant de faire confiance à la réponse, aurait suffi à détecter l’erreur ?

??? pouce "Coup de pouce"

    Faire la trace pas à pas : au premier tour, `element` vaut `3`. Lequel des deux `return` est exécuté ? La boucle continue-t-elle ?

??? corrige "Corrigé"

    **1.** Non. Trace de `est_present([3, 8, 5], 5)` : premier tour, `element = 3` ; `3 == 5` est faux, on passe dans le `else` et la fonction renvoie **`False`** — alors que `5` est bien dans le tableau. La fonction ne regarde en fait que le *premier* élément (elle ne répond `True` que pour `x = 3`). **2.** L’erreur est le `else: return False` *dans* la boucle : on conclut à l’absence avant d’avoir tout regardé. Le `return False` doit être **après** la boucle :

    ```python
    def est_present(t, x):
        for element in t:
            if element == x:
                return True
        return False          # parcours fini sans succes : absent
    ```

    Avec cette correction, `est_present([3, 8, 5], 5)` renvoie `True` et `est_present([3, 8, 5], 7)` renvoie `False`. **3.** Tester la fonction sur un exemple où `x` n’est *pas* en première position : un seul appel suffisait. Un `return False` placé dans un `for` est presque toujours suspect.
