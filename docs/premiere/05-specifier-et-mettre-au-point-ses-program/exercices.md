# Exercices

<p class="sous-titre">Spécifier et mettre au point ses programmes</p>

!!! consignes "Mode d’emploi"

    - Niveau : ★ échauffement, ★★ classique (niveau bac), ★★★ défi ; les *coups de pouce* et les *corrigés* se déplient sous chaque exercice.

    - <span class="run" title="À programmer et tester sur machine">▶</span> *À programmer et tester* en Python. `>>>` figure une saisie dans la console.

    - Réflexe de tout le chapitre : **une docstring, une précondition, des tests** pour chaque fonction.

    - Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la [charte d’usage de l’IA](../charte.md).

### Spécifier et documenter

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — Précondition ou postcondition ? <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-05-1 }

Pour chaque affirmation sur une fonction `racine_carree(x)`, dire s’il s’agit d’une **précondition** ou d’une **postcondition**.

1.  `x` doit être positif ou nul ;

2.  le résultat élevé au carré redonne `x` ;

3.  le résultat est positif ou nul.

??? corrige "Corrigé"

    \(a\) **précondition** (condition sur l’argument `x`) ; (b) **postcondition** (garantie sur le résultat) ; (c) **postcondition**.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 2</span> — Une docstring pour `division_euclidienne` <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-05-2 }

Donner une chaîne de documentation (rôle, précondition, postcondition) à la fonction `division_euclidienne` vue dans le cours.

??? corrige "Corrigé"

    ```python
    def division_euclidienne(a, b):
        """Renvoie (q, r), quotient et reste de la division de a par b.
        Precondition : a >= 0 et b > 0.
        Postcondition : a == q * b + r et 0 <= r < b."""
    ```

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 3</span> — Prototyper puis documenter <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-05-3 }

Écrire l’en-tête (`def`…) **et** la docstring d’une fonction `puissance(x, n)` qui calcule `x` à la puissance `n`, pour `n` entier positif ou nul. On n’écrit *pas* le corps.

??? corrige "Corrigé"

    ```python
    def puissance(x, n):
        """Renvoie x eleve a la puissance n.
        Precondition : n est un entier >= 0.
        Postcondition : renvoie x**n (et 1 si n == 0)."""
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 4</span> — Un meilleur nom <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-4 }

Cette fonction « marche », mais se lit mal.

```python
def f(t):
    s = 0
    for i in range(len(t)):
        s = s + t[i]
    return s
```

Lui donner : (a) un **nom** explicite, (b) une **docstring**, (c) un **invariant** de boucle, (d) trois **tests**.

??? pouce "Coup de pouce"

    Commencer par l’essayer sur `[1, 2, 3]` : que calcule-t-elle ? Pour l’invariant : que contient `s` au début du tour d’indice `i` ? Pour les tests, penser au tableau vide.

??? corrige "Corrigé"

    ```python
    def somme(t):
        """Renvoie la somme des elements du tableau t (0 si t est vide)."""
        s = 0
        for i in range(len(t)):
            # invariant : s == t[0] + t[1] + ... + t[i-1]
            s = s + t[i]
        return s

    assert somme([]) == 0
    assert somme([5]) == 5
    assert somme([1, 2, 3, 4]) == 10
    ```

### Programmation défensive

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 5</span> — Poser un garde-fou <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-05-5 }

Ajouter à la fonction `puissance(x, n)` une ligne `assert` qui garantit sa précondition, avec un message clair. Que se passe-t-il si on appelle `puissance(2, -3)` ?

??? corrige "Corrigé"

    ```python
    def puissance(x, n):
        assert n >= 0, "l'exposant doit etre positif ou nul"
        r = 1
        for i in range(n):
            r = r * x
        return r
    ```

    `puissance(2, -3)` déclenche `AssertionError: l’exposant doit être positif ou nul` : le programme s’interrompt immédiatement, à l’endroit du vrai problème.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — `assert` ou `None` ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-6 }

On écrit `premier_element(t)` qui renvoie le premier élément d’un tableau.

1.  Écrire une version **défensive avec `assert`** (précondition : `t` non vide).

2.  Écrire une version qui **renvoie `None`** sur un tableau vide.

3.  Pour chaque version, écrire le code qui **appelle** la fonction en respectant sa stratégie.

??? pouce "Coup de pouce"

    c\) Avec la version `assert`, l’appelant doit vérifier quelque chose *avant* l’appel ; avec la version `None`, il vérifie *après* l’appel, sur le résultat.

??? corrige "Corrigé"

    ```python
    def premier_element(t):        # version defensive
        assert len(t) > 0, "tableau vide"
        return t[0]

    def premier_element_ou_none(t):  # version sentinelle
        if len(t) == 0:
            return None
        return t[0]
    ```

    Appels respectant chaque stratégie :

    ```python
    if len(t) > 0:              # avec assert : on garantit la precondition
        print(premier_element(t))

    r = premier_element_ou_none(t)   # avec None : on teste le resultat
    if r is not None:
        print(r)
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Le piège de `-1` <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-7 }

Une fonction `indice_de(v, t)` renvoie l’indice de `v` dans `t`, et `-1` si `v` est absente. Cette convention est courante (on la trouve dans des sujets de bac). Montrer, sur un exemple, le **piège** qu’elle tend au code appelant en Python, puis écrire ce code appelant correctement. Quelle autre convention évite ce piège ?

??? pouce "Coup de pouce"

    Que vaut `t[-1]` en Python ? Imaginer un appelant pressé qui écrit `t[indice_de(v, t)]` sans rien vérifier.

??? corrige "Corrigé"

    Sur `t = [10, 20, 30]`, si `v` est absente la fonction renvoie `-1`. Mais `t[-1]` vaut `30` : le code appelant qui ferait `t[indice_de(v, t)]` croirait avoir trouvé `v` alors qu’il lit le **dernier** élément. Le code appelant doit donc **tester** le résultat avant de s’en servir : `r = indice_de(v, t)` puis `if r != -1 :` `print(t[r])`. L’autre convention, `None`, évite le piège (ce n’est jamais un indice) ; les deux sont correctes, il faut suivre celle de l’énoncé.

### Tester ses programmes

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 8</span> — Tests pour `puissance` <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-05-8 }

Écrire un bon jeu de tests (au moins quatre `assert`) pour `puissance(x, n)`. On pensera au **cas limite** `n = 0`.

??? corrige "Corrigé"

    ```python
    assert puissance(2, 0) == 1     # cas limite n = 0
    assert puissance(2, 1) == 2
    assert puissance(2, 10) == 1024
    assert puissance(5, 3) == 125
    assert puissance(1, 100) == 1
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 9</span> — Trouver le contre-exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-9 }

On prétend que la fonction suivante teste l’appartenance de `v` au tableau `t`.

```python
def appartient(v, t):
    i = 0
    while i < len(t) - 1 and t[i] != v:
        i = i + 1
    return i < len(t)
```

Donner un jeu de tests, dont un `assert` qui **échoue** et prouve que la fonction est incorrecte. Où est l’erreur ?

??? pouce "Coup de pouce"

    Varier les situations : valeur en tête, en dernière position, absente. Dans chaque cas, que vaut `i` à la sortie de la boucle, et que renvoie alors `i < len(t)` ?

??? corrige "Corrigé"

    La condition `i < len(t) - 1` arrête la boucle **un cran trop tôt** : le **dernier** élément n’est jamais comparé, et `i` vaut au plus `len(t) - 1` à la sortie. Le `return i < len(t)` renvoie donc `True` pour **tout tableau non vide**, que `v` soit présent ou non. Sur `t = [2, 5, 9]` et `v = 9`, la boucle s’arrête à `i = 2` sans avoir comparé le `9` : la réponse `True` est juste, mais par hasard. Les tests « présent » passent tous ; seul un test « absent » révèle l’erreur :

    ```python
    assert appartient(9, [2, 5, 9]) == True   # passe (par hasard)
    assert appartient(2, [2, 5, 9]) == True   # passe
    assert appartient(4, []) == False         # passe
    assert appartient(4, [1, 2]) == False     # ECHOUE : renvoie True
    ```

    Correction : la condition doit être `i < len(t)`. La boucle s’arrête alors soit sur `v`, soit au bout du tableau ; `i < len(t)` dit lequel des deux.

    ```python
    def appartient(v, t):
        i = 0
        while i < len(t) and t[i] != v:
            i = i + 1
        return i < len(t)      # vrai seulement si on s'est arrete sur v
    ```

    *Autre méthode :* un `for` qui renvoie `True` dès qu’on trouve, et `False` seulement après le parcours complet.

    ```python
    def appartient(v, t):
        for x in t:
            if x == v:
                return True
        return False
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 10</span> — Deux erreurs pour le prix d’une <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-10 }

Même énoncé pour cette autre version.

```python
def appartient(v, t):
    for i in range(len(t)):
        if t[i] == v:
            trouvee = True
        else:
            trouvee = False
    return trouvee
```

Donner des tests montrant **deux** raisons distinctes pour lesquelles elle est fausse.

??? pouce "Coup de pouce"

    Que se passe-t-il si `t` est vide ? Et si l’élément cherché est présent, mais pas en dernière position ?

??? corrige "Corrigé"

    **Erreur 1 — tableau vide :** `trouvee` n’est jamais définie, l’appel lève `NameError` (ou `UnboundLocalError`). **Erreur 2 — seule la dernière case compte :** `trouvee` est réécrite à chaque tour, donc elle vaut le résultat de la comparaison sur le *dernier* élément seulement.

    ```python
    assert appartient(1, []) == False       # ECHOUE : NameError (trouvee non definie)
    assert appartient(1, [1, 2]) == True    # ECHOUE : renvoie False (dernier = 2)
    ```

    Correction : renvoyer `True` dès qu’on trouve, `False` après le parcours complet.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 11</span> — Un bon jeu de tests <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-11 }

Une fonction `est_pair(n)` renvoie un booléen. En s’appuyant sur la check-list du cours, lister les **cas** qu’un bon jeu de tests doit couvrir, puis écrire les `assert` correspondants.

??? pouce "Coup de pouce"

    Une fonction booléenne a deux réponses possibles : les tester toutes les deux. Penser aussi aux valeurs limites : $0$ et les nombres négatifs.

??? corrige "Corrigé"

    `est_pair` est booléenne : il faut un cas `True` et un cas `False`, le cas limite `0`, et des négatifs.

    ```python
    assert est_pair(4) == True
    assert est_pair(7) == False
    assert est_pair(0) == True     # cas limite
    assert est_pair(-2) == True    # negatif pair
    assert est_pair(-3) == False   # negatif impair
    ```

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 12</span> — Des tests qui démasquent <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-12 }

La fonction `est_trie(t)` doit renvoyer `True` si les éléments du tableau `t` sont rangés dans l’ordre croissant au sens large (`[2, 2, 5]` est trié), `False` sinon. Trois élèves en proposent chacun une version.

```python
def est_trie_1(t):
    for i in range(len(t) - 2):
        if t[i] > t[i + 1]:
            return False
    return True

def est_trie_2(t):
    for i in range(len(t) - 1):
        if t[i] >= t[i + 1]:
            return False
    return True

def est_trie_3(t):
    for i in range(len(t) - 1):
        if t[i] > t[i + 1]:
            return False
        else:
            return True
    return True
```

1.  Sans machine, trouver pour chaque version un tableau sur lequel elle répond faux.

2.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire un jeu de tests **le plus court possible** (des `assert` sur `est_trie`) qu’une version correcte passe, mais qui fait échouer **chacune** des trois versions. Combien d’`assert` suffisent ?

3.  Les tests `[]`, `[5]`, `[1, 2, 3]` et `[3, 1, 2]` auraient-ils détecté une de ces erreurs ? Qu’en conclure sur le choix des tests ?

??? pouce "Coup de pouce"

    Écrire d’abord une version correcte, puis comparer chaque version avec elle, ligne à ligne. Quel tableau oblige le programme à passer par la ligne qui diffère ?

??? pouce "Coup de pouce 2 (début de solution)"

    Version 1 : sur un tableau de 3 éléments, quelles paires d’indices sont réellement comparées ? Version 2 : que répond-elle sur deux éléments égaux ? Version 3 : combien de paires examine-t-elle avant de répondre ?

??? corrige "Corrigé"

    **a)** Version 1 : `range(len(t) - 2)` oublie la **dernière paire** ; sur `[1, 3, 2]` elle répond `True`. Version 2 : `>=` rejette deux éléments **égaux** ; sur `[2, 2]` elle répond `False`. Version 3 : le `else: return True` conclut dès la **première paire** bien rangée ; sur `[1, 2, 0]` elle répond `True`.

    **b)** **Deux** `assert` suffisent :

    ```python
    assert est_trie([2, 2]) == True       # fait echouer la version 2
    assert est_trie([1, 2, 0]) == False   # fait echouer les versions 1 et 3
    ```

    Une version correcte (`range(len(t) - 1)` et `>`, `return True` seulement après la boucle) passe les deux.

    **c)** Non : sur `[]`, `[5]`, `[1, 2, 3]` et `[3, 1, 2]`, les trois versions répondent exactement comme une version correcte. Un jeu de tests « au hasard » peut donc passer entièrement sur un programme faux : il faut **viser** les cas où une erreur plausible se manifeste (égalités, désordre en **fin** de tableau, désordre après un début bien rangé).

### Corriger les erreurs (déboguer)

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 13</span> — La chasse au bug <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-13 }

La fonction doit renvoyer le plus petit élément d’un tableau non vide.

```python
def minimum(t):
    m = 0
    for x in t:
        if x < m:
            m = x
    return m
```

1.  Trouver un tableau sur lequel elle renvoie un résultat **faux**.

2.  Expliquer l’erreur (dérouler l’exécution), puis **corriger** la fonction.

3.  Ajouter une docstring, une précondition défensive et des tests.

??? pouce "Coup de pouce"

    Essayer un tableau dont tous les éléments sont strictement positifs. Avec quelle valeur faut-il initialiser le « meilleur jusqu’ici » ?

??? corrige "Corrigé"

    \(a\) Sur `[3, 8, 5]` elle renvoie `0` : faux. (b) Le champion `m` est initialisé à `0` (une *valeur*, pas un élément) : aucun élément positif n’est jamais plus petit que 0, donc `m` reste 0. Il faut initialiser `m` au **premier élément**. (c) Version corrigée :

    ```python
    def minimum(t):
        """Renvoie le plus petit element de t. Precondition : t non vide."""
        assert len(t) > 0, "tableau vide"
        m = t[0]
        for x in t:
            if x < m:
                m = x
        return m

    assert minimum([3, 8, 5]) == 3
    assert minimum([-1, -4, -2]) == -4
    assert minimum([7]) == 7
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 14</span> — Débogage guidé par l’affichage <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-14 }

La fonction doit renvoyer le nombre d’éléments **strictement positifs** d’un tableau.

```python
def nb_positifs(t):
    nb = 0
    for x in t:
        if x > 0:
            nb = 1
    return nb
```

Elle renvoie `1` pour `[3, 8, -2, 5]` alors qu’on attend `3`. En imaginant un `print(nb)` dans la boucle, expliquer ce qu’on observerait, identifier l’erreur et la corriger.

??? pouce "Coup de pouce"

    Écrire la suite des valeurs que `print(nb)` afficherait sur `[3, 8, -2, 5]`. À chaque élément positif, de combien `nb` devrait-il évoluer ?

??? corrige "Corrigé"

    Un `print(nb)` dans la boucle afficherait `1, 1, 1` : `nb` est **remis à 1** à chaque élément positif au lieu d’être **incrémenté**. Il faut `nb = nb + 1`.

    ```python
    def nb_positifs(t):
        nb = 0
        for x in t:
            if x > 0:
                nb = nb + 1
        return nb

    assert nb_positifs([3, 8, -2, 5]) == 3
    assert nb_positifs([]) == 0
    assert nb_positifs([-1, -2]) == 0
    ```

### Invariant de boucle

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 15</span> — Énoncer un invariant <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-05-15 }

Donner un invariant de boucle pour cette fonction, puis prouver qu’à la sortie il donne le résultat attendu.

```python
def puissance(x, n):
    r = 1
    for i in range(n):
        r = r * x
    return r
```

??? pouce "Coup de pouce"

    Que vaut `r` au début du tour d’indice `i` ? Le vérifier pour `i = 0, 1, 2`, puis se demander combien de tours ont été faits à la sortie.

??? corrige "Corrigé"

    Invariant, juste avant le tour d’indice `i` : `r == x ** i` (r est `x` multiplié par lui-même `i` fois). Vrai au départ (`i = 0`, `r = 1 = x**0`). Préservé : si `r == x**i`, alors après `r = r * x` et le passage à `i+1` on a `r == x**(i+1)`. À la sortie, `i` a atteint `n`, donc `r == x**n` : le résultat attendu.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 16</span> — Invariant et `assert` <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-16 }

On somme les éléments d’un tableau.

```python
def somme(t):
    s = 0
    for i in range(len(t)):
        s = s + t[i]
    return s
```

\(a\) Énoncer l’invariant reliant `s` et `i`. (b) L’écrire sous forme d’un `assert` placé au bon endroit dans la boucle. (c) En quoi cela aide-t-il à la mise au point ?

??? pouce "Coup de pouce"

    Au début du tour d’indice `i`, `s` contient la somme de quels éléments ? Peut-on désigner ces éléments par une tranche de `t` ?

??? pouce "Coup de pouce 2 (début de solution)"

    La somme des éléments d’indices `0` à `i - 1` s’écrit `sum(t[0:i])` (ici `sum` sert seulement à *vérifier*). L’`assert` doit être exécuté à chaque tour, *avant* la mise à jour de `s`.

??? corrige "Corrigé"

    ```python
    def somme(t):
        s = 0
        for i in range(len(t)):
            assert s == sum(t[0:i])   # invariant : s = somme des i premiers
            s = s + t[i]
        return s
    ```

    \(c\) Pendant la mise au point, Python **vérifie l’invariant à chaque tour** : si une erreur casse la logique de l’accumulation, l’`AssertionError` se déclenche *tout de suite*, au tour fautif, au lieu de laisser un résultat faux apparaître à la fin.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 17</span> — Une division qui se trompe parfois <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-17 }

Cette fonction doit renvoyer le couple `(q, r)` du quotient et du reste de la division euclidienne de `a` par `b`, pour `a` entier positif ou nul et `b` entier strictement positif.

```python
def division(a, b):
    q = 0
    r = a
    while r > b:
        r = r - b
        q = q + 1
    return q, r
```

1.  Écrire sa docstring : rôle, précondition, postcondition (deux relations entre `a`, `b`, `q` et `r`).

2.  `division(17, 5)` renvoie `(3, 2)`, ce qui est juste. Trouver un appel pour lequel le résultat est faux.

3.  <span class="run" title="À programmer et tester sur machine">▶</span> Ajouter un `assert` de l’invariant `a == q * b + r` au début du corps de la boucle, et un `assert` de la postcondition juste avant le `return`. Lequel échoue sur votre appel ? Qu’en déduire : l’erreur est-elle dans le corps de la boucle ou dans sa condition ?

4.  Corriger la fonction et ajouter l’`assert` de la précondition. Que se passerait-il, sans lui, pour `division(5, 0)` ?

??? pouce "Coup de pouce"

    Penser aux cas limites : que se passe-t-il au moment où `r` devient exactement égal à `b` ?

??? pouce "Coup de pouce 2 (début de solution)"

    Postcondition : `a == q * b + r` et `0 <= r < b`. Sur l’appel trouvé, l’invariant reste vrai à chaque tour : ce n’est donc pas le corps de la boucle qui est en cause.

??? corrige "Corrigé"

    **a)**

    ```python
    def division(a, b):
        """Renvoie (q, r), quotient et reste de la division euclidienne de a par b.
        Precondition : a et b entiers, a >= 0 et b > 0.
        Postcondition : a == q * b + r et 0 <= r < b."""
    ```

    **b)** `division(6, 3)` renvoie `(1, 3)` au lieu de `(2, 0)` (de même `division(7, 7)` renvoie `(0, 7)`) : l’erreur apparaît dès que `r` atteint exactement la valeur `b`.

    **c)** L’`assert` de l’invariant ne se déclenche jamais : le corps de la boucle conserve bien `a == q * b + r`. C’est l’`assert` de la postcondition qui échoue (`r` vaut `b`, donc `r < b` est faux). L’erreur est donc dans la **condition** de la boucle, qui s’arrête un tour trop tôt : il faut `r >= b`.

    **d)**

    ```python
    def division(a, b):
        assert b > 0, "le diviseur doit etre strictement positif"
        q = 0
        r = a
        while r >= b:
            assert a == q * b + r      # invariant (mise au point)
            r = r - b
            q = q + 1
        assert 0 <= r < b              # postcondition
        return q, r

    assert division(17, 5) == (3, 2)
    assert division(6, 3) == (2, 0)
    assert division(7, 7) == (1, 0)
    assert division(2, 5) == (0, 2)
    assert division(0, 4) == (0, 0)
    ```

    Sans l’`assert` de précondition, `division(5, 0)` ne se termine jamais : `r` reste égal à `5`, la condition `r >= 0` reste vraie, la boucle est **infinie**. L’`assert` transforme ce blocage silencieux en une erreur immédiate et explicite.

### Diversité des langages et bibliothèques

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 18</span> — Compilé ou interprété ? <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-05-18 }

Pour chacune des affirmations, indiquer si elle décrit plutôt un langage **compilé** ou **interprété**, et justifier en une phrase.

1.  « Le même fichier de code tourne sur ma machine et sur celle de mon voisin, sans rien retraduire. »

2.  « On obtient un fichier exécutable rapide, mais il faut tout retraduire à chaque modification. »

3.  « Une erreur de langage se manifeste seulement quand le programme atteint la ligne fautive. »

4.  « Les erreurs de langage sont signalées avant même de lancer le programme. »

??? corrige "Corrigé"

    a\) Interprété : le même fichier tourne partout où l’interpréteur est installé, sans retraduction. b) Compilé : on produit un exécutable rapide, mais il faut recompiler à chaque modification. c) Interprété : la traduction se fait à la volée, donc l’erreur n’apparaît qu’en atteignant la ligne. d) Compilé : la traduction complète a lieu avant l’exécution, ce qui permet de signaler les erreurs en amont.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 19</span> — Statique ou dynamique ? <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-05-19 }

1.  Pour chacune de ces trois lignes, dire si le typage est **statique** ou **dynamique**, et si le type est **écrit** ou **deviné** (inféré) : (C) `int n = 5;` (Python) `n = 5` (OCaml) `let n = 5`

2.  On considère la fonction Python suivante.

    ```python
    def prix_ttc(prix, code):
        if code == "normal":
            return prix * 1.2
        return "prix reduit : " + prix * 1.055
    ```

    Les appels `prix_ttc(10, "normal")` et `prix_ttc(50, "normal")` fonctionnent. Peut-on en conclure que la fonction est correcte ? Quel appel révèle l’erreur, et quel message Python affiche-t-il ? Un langage à typage statique aurait-il laissé passer cette erreur ?

??? pouce "Coup de pouce"

    a\) Le type est-il écrit dans la ligne ? Est-il vérifié avant ou pendant l’exécution ? b) Quelle ligne de la fonction n’est exécutée par aucun des deux appels ?

??? corrige "Corrigé"

    a\) (C) statique, type **écrit** (`int`) ; (Python) dynamique, rien à écrire ni à deviner avant l’exécution ; (OCaml) statique, type **deviné** (inféré) : OCaml déduit que `n` est un entier.

    b\) Non : les deux appels passent par la *même* branche (`code == "normal"`) ; la dernière ligne n’est jamais exécutée. L’appel `prix_ttc(10, "reduit")` l’atteint et déclenche `TypeError: can only concatenate str (not "float") to str` : on ne peut pas coller un texte et un nombre. Correction : `return "prix reduit : " + str(prix * 1.055)` (ou renvoyer simplement le nombre `prix * 1.055`). Un langage à typage **statique** aurait refusé ce programme *avant* l’exécution. Leçon : le jeu de tests doit passer par **toutes** les branches.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 20</span> — Le bon outil <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-05-20 }

Associer chaque besoin au langage le plus naturel (une seule réponse par ligne) : **Python**, **C**, **JavaScript**, **SQL**.

1.  Rendre une page web interactive dans le navigateur.

2.  Interroger une base de données pour retrouver des élèves.

3.  Programmer un tout petit objet embarqué où chaque microseconde compte.

4.  Analyser rapidement un jeu de données pour un projet de science.

??? corrige "Corrigé"

    a\) JavaScript. b) SQL. c) C. d) Python.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 21</span> — Vrai ou faux, et pourquoi <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-05-21 }

Dire si chaque affirmation est vraie ou fausse, en corrigeant les fausses.

1.  « Il existe un langage meilleur que tous les autres. »

2.  « Un algorithme dépend du langage dans lequel on l’écrit. »

3.  « Python peut se programmer dans plusieurs paradigmes. »

4.  « Un langage compilé est en général plus lent à l’exécution qu’un langage interprété. »

??? pouce "Coup de pouce"

    Pour chaque affirmation, chercher un exemple ou un contre-exemple dans la partie « Diversité et unité des langages » du cours.

??? corrige "Corrigé"

    a\) Faux : aucun langage n’est le meilleur ; chacun est un compromis adapté à certaines tâches. b) Faux : un *algorithme* est indépendant du langage ; seul le *programme* qui le traduit en dépend. c) Vrai : Python est multi-paradigme (impératif, fonctionnel, objet). d) Faux : c’est l’inverse en général ; un langage compilé est traduit une fois pour toutes et s’exécute typiquement *plus vite* qu’un langage interprété.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 22</span> — Langage de programmation ou pas ? <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-05-22 }

Pour chacun, dire si c’est un **langage de programmation** : Python, HTML, SQL, C, JavaScript. Justifier en une phrase.

??? corrige "Corrigé"

    **Python, C, JavaScript** : oui, on y écrit des algorithmes (variables, boucles, conditions). **HTML** : non, il *décrit* une page ; c’est un langage formalisé, mais pas un langage de programmation. **SQL** : c’est un langage de *requêtes*, qui *interroge* une base de données en décrivant le résultat voulu ; ce n’est pas un langage de programmation *généraliste*.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 23</span> — Lire un programme dans un langage inconnu <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-05-23 }

Voici une fonction dans un langage que vous ne connaissez pas.

```text
fonction double(x)
    retourne x * 2
fin
```

Repérer : (a) la **construction élémentaire** commune avec Python (appel, valeur de retour) ; (b) ce qui **diffère** de la syntaxe Python. Réécrire cette fonction en Python.

??? pouce "Coup de pouce"

    Repérer le mot qui joue le rôle de `def`, celui qui joue le rôle de `return`, et la façon dont la fin du bloc est marquée.

??? corrige "Corrigé"

    \(a\) Commun : une **fonction** nommée avec un paramètre et une **valeur de retour** (`retourne`). (b) Diffère : mot-clé `fonction` au lieu de `def`, `fin` pour fermer le bloc (pas d’indentation obligatoire), pas de « `:` ». En Python :

    ```python
    def double(x):
        return x * 2
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 24</span> — Lire une documentation <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-05-24 }

La documentation du module `random` indique : `randint(a, b)` *« renvoie un entier aléatoire N tel que a $\leqslant$ N $\leqslant$ b »*.

1.  Quelle est la **précondition** implicite sur `a` et `b` ?

2.  Écrire un appel qui simule le lancer d’un dé à six faces.

3.  A-t-on besoin de connaître le *code* de `randint` pour l’utiliser ?

??? pouce "Coup de pouce"

    a\) Que deviendrait la phrase de la documentation si `a` était plus grand que `b` ? b) Quelles sont les valeurs possibles d’un dé ?

??? corrige "Corrigé"

    \(a\) Précondition implicite : `a <= b`. (b) `random.randint(1, 6)`. (c) Non : la documentation (la spécification) suffit pour l’utiliser correctement, sans lire son code — c’est tout l’intérêt d’une bibliothèque.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 25</span> — Une fonction spécifiée par un assistant d’IA <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> { #ex-05-25 }

Un élève demande à un assistant d’IA : « Écris une fonction `nb_chiffres(n)` qui renvoie le nombre de chiffres d’un entier positif, avec sa docstring et un jeu de tests. » Voici la réponse obtenue.

```python
def nb_chiffres(n):
    """Renvoie le nombre de chiffres de l'entier n.
    Precondition : n >= 0. Par convention nb_chiffres(0) vaut 1."""
    compteur = 0
    while n > 0:
        n = n // 10
        compteur = compteur + 1
    return compteur

assert nb_chiffres(2024) == 4
assert nb_chiffres(7) == 1
assert nb_chiffres(0) == 1
```

« À chaque tour, on retire le dernier chiffre par division entière et on compte ; la boucle s’arrête quand il ne reste plus rien. Les trois tests couvrent un cas général, un cas à un chiffre et le cas limite `0` : ils passent tous. »

1.  La réponse est-elle correcte ? Exécuter le fichier tel quel (ou faire la trace de `nb_chiffres(0)`).

2.  Localiser et corriger l’erreur, sans changer la spécification.

3.  Quelle vérification simple, faite avant de faire confiance à la réponse, aurait suffi à détecter l’erreur ?

??? pouce "Coup de pouce"

    Dérouler à la main `nb_chiffres(0)` : combien de tours fait la boucle `while n > 0` ? Que vaut alors `compteur` ?

??? corrige "Corrigé"

    \(a\) Non. Pour `n = 0`, la condition `n > 0` est fausse dès le départ : la boucle n’est jamais exécutée et la fonction renvoie `0`. Les deux premiers tests passent (`4` et `1`), le troisième échoue :

    ```text
    Traceback (most recent call last):
      File "nb_chiffres.py", line 12, in <module>
        assert nb_chiffres(0) == 1
    AssertionError
    ```

    \(b\) La fonction ne respecte pas sa propre spécification sur le cas limite `0`. On compte un chiffre d’office et on boucle tant qu’il en reste au moins un autre (`n >= 10`) :

    ```python
    def nb_chiffres(n):
        """Renvoie le nombre de chiffres de l'entier n.
        Precondition : n >= 0. Par convention nb_chiffres(0) vaut 1."""
        compteur = 1
        while n >= 10:
            n = n // 10
            compteur = compteur + 1
        return compteur
    ```

    Les trois `assert` passent. (c) Exécuter le jeu de tests fourni au lieu de croire la phrase « ils passent tous » : l’assistant a écrit le bon test (le cas limite) sans le lancer. Un test qu’on n’exécute pas ne vérifie rien.
