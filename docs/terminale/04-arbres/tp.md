# TP et projets

<p class="sous-titre">Arbres</p>

## <span class="etiquette">TP</span> Un arbre binaire de recherche, de A à Z

*construire, chercher, mesurer, indexer*

<p class="infos-activite">Durée : 3 h environ (deux séances) · Sur machine, seul ou par deux</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/04-tp-arbres){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-04-tp-arbres.zip){ .md-button }

!!! encadre "But du TP"

    Programmer une classe `ABR` complète (insertion, recherche, minimum et maximum, parcours infixe), puis **mesurer** ce que le cours affirme : un ABR rempli au hasard reste bas, un ABR rempli avec des valeurs triées devient un « peigne » aussi lent qu’une liste. On termine par une application : l’**index** des mots d’un texte, comme à la fin d’un livre. <span class="run" title="À programmer et tester sur machine">▶</span>  signale ce qui est à programmer et tester.

!!! consignes "Consignes"

    - Le fichier `tp_arbres_depart.py` est **à télécharger** (lien ci-dessus) : la classe `Noeud` et les fonctions `taille` et `hauteur` du cours, le squelette des classes et, en fin de fichier, des **tests**. Relancer le fichier après chaque partie : chaque ligne `[A FAIRE]` doit devenir `[OK]`.

    - **Convention** de hauteur du cours : on compte les nœuds (racine seule $\to$ hauteur $1$, arbre vide $\to$ $0$).

    - Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la [charte d’usage de l’IA](../charte.md).

## Construire un ABR

On enveloppe l’arbre dans une classe `ABR` : l’attribut privé `_racine` désigne le nœud racine (ou `None`), et `_taille` compte les valeurs. L’utilisateur ne manipule jamais les nœuds : il appelle `inserer`, `contient`, `infixe`… Les valeurs sont **sans doublon**.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — L’ordre d’insertion compte <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-arbres-tp-1-1 }

1.  Dessiner l’ABR obtenu en insérant, dans cet ordre, `15, 8, 20, 5, 12, 25, 10, 18, 2` dans un arbre vide. Donner sa taille et sa hauteur.

2.  Dessiner l’ABR obtenu en insérant les **mêmes** valeurs dans l’ordre croissant `2, 5, 8, 10, 12, 15, 18, 20, 25`. Taille ? Hauteur ? Pourquoi parle-t-on de « peigne » ?

3.  Proposer un ordre d’insertion de ces neuf valeurs qui donne un arbre de hauteur $4$ **différent** de celui de la question 1.

??? corrige "Corrigé"

    Tout le code ci-dessous a été exécuté : avec ces solutions, les six tests du fichier `tp_arbres_depart.py` affichent `[OK]`, et les mesures sont celles réellement obtenues.

    ![](../figures/8be18960b53b279a.svg){ .tikz loading=lazy }

    ![](../figures/515dc9264ce9e31c.svg){ .tikz loading=lazy }

    ![](../figures/e2a87f28bcf12593.svg){ .tikz loading=lazy }

    **1.** Arbre de gauche : taille $9$, hauteur $4$ (chemin `15--8--5--2` ou `15--8--12--10`).

    **2.** Arbre du milieu : chaque valeur est plus grande que toutes les précédentes, donc elle va toujours à droite. Taille $9$, hauteur **$9$** : chaque nœud n’a qu’un fils, l’arbre est une « dent de peigne », en fait une liste chaînée déguisée.

    **3.** Par exemple `12, 5, 20, 2, 8, 15, 25, 10, 18` (arbre de droite) : hauteur $4$. Un bon ordre commence par une valeur « médiane », puis les médianes de chaque moitié.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 2</span> — Insérer sans récursivité <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-arbres-tp-1-2 }

<span class="run" title="À programmer et tester sur machine">▶</span> Compléter la méthode `inserer(x)` avec une boucle `while` : si l’arbre est vide, le nouveau nœud devient la racine ; sinon, on descend depuis la racine, à gauche si `x` est plus petit que la valeur du nœud courant, à droite s’il est plus grand, jusqu’à trouver une place libre (`None`) où l’on accroche `Noeud(x)`. La méthode renvoie `True` si `x` a été ajouté, `False` s’il était déjà présent (l’arbre est alors inchangé). Penser à mettre `_taille` à jour.

??? pouce "Coup de pouce"

    Garder une variable `n` sur le nœud courant. À chaque tour : si `x == n.valeur`, renvoyer `False` ; si `x < n.valeur` et que `n.gauche` est `None`, on accroche le nouveau nœud à gauche ; sinon on descend `n = n.gauche`. Même chose à droite. Un booléen `place`, qui passe à `True` quand le nœud est accroché, sert de condition à la boucle : `while not place`.

```text
>>> a = ABR()
>>> for v in [15, 8, 20, 5, 12, 25, 10, 18, 2]:
...     a.inserer(v)
>>> a.taille(), a.hauteur()
(9, 4)
>>> a.inserer(12)
False
```

Le test vérifie aussi que `_taille` est égal à `taille(a._racine)`. Quel est l’intérêt de tenir à jour l’attribut `_taille` plutôt que d’appeler la fonction récursive `taille` à chaque fois ?

??? corrige "Corrigé"

    ```python
    class ABR:
        def __init__(self):
            self._racine = None
            self._taille = 0

        def inserer(self, x):
            nouveau = Noeud(x)
            if self._racine is None:
                self._racine = nouveau
                self._taille = 1
                return True
            n = self._racine
            place = False                      # le nouveau noeud est-il accroche ?
            while not place:
                if x == n.valeur:              # deja present : on ne fait rien
                    return False
                if x < n.valeur:
                    if n.gauche is None:
                        n.gauche = nouveau
                        place = True
                    else:
                        n = n.gauche
                else:
                    if n.droite is None:
                        n.droite = nouveau
                        place = True
                    else:
                        n = n.droite
            self._taille = self._taille + 1
            return True
    ```

    L’attribut `_taille` répond **immédiatement**, alors que la fonction `taille` parcourt tout l’arbre ($n$ appels) à chaque fois. En contrepartie, il faut le tenir à jour dans chaque méthode qui modifie l’arbre : c’est un **invariant** que le test vérifie.

## Chercher

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 3</span> — Chercher en comptant ses pas <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-arbres-tp-1-3 }

1.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire la méthode `contient(x)`, **itérative**, qui renvoie le couple `(présent, visites)` : un booléen, et le nombre de nœuds visités pendant la recherche.

    ```text
    >>> a.contient(15), a.contient(10), a.contient(13)
    ((True, 1), (True, 4), (False, 3))
    ```

2.  Justifier, sur l’arbre de la question 1 de l’exercice 1, que `a.contient(13)` visite $3$ nœuds. Pourquoi le nombre de visites ne dépasse-t-il jamais la hauteur de l’arbre ?

??? corrige "Corrigé"

    **1.**

    ```python
        def contient(self, x):
            n = self._racine
            visites = 0
            while n is not None:
                visites = visites + 1
                if x == n.valeur:
                    return True, visites
                if x < n.valeur:
                    n = n.gauche
                else:
                    n = n.droite
            return False, visites
    ```

    **2.** Pour `13` : `15` (on va à gauche), `8` (à droite), `12` (à droite) : sous-arbre vide, absent, $3$ visites. Chaque visite descend d’un niveau, sur un unique chemin partant de la racine : on visite au plus autant de nœuds que le plus long chemin racine–feuille en contient, c’est-à-dire la hauteur.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 4</span> — Le plus petit et le plus grand <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-arbres-tp-1-4 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `minimum()` et `maximum()`, qui lèvent `ValueError("arbre vide")` sur un arbre vide. Où se trouve la plus petite valeur d’un ABR ? Est-ce forcément une feuille ?

??? pouce "Coup de pouce"

    Depuis la racine, descendre toujours du même côté tant que c’est possible.

??? corrige "Corrigé"

    ```python
        def minimum(self):
            if self._racine is None:
                raise ValueError("arbre vide")
            n = self._racine
            while n.gauche is not None:
                n = n.gauche
            return n.valeur

        def maximum(self):
            if self._racine is None:
                raise ValueError("arbre vide")
            n = self._racine
            while n.droite is not None:
                n = n.droite
            return n.valeur
    ```

    Le minimum est le nœud le plus à gauche : il n’a pas de fils gauche, mais **pas forcément** une feuille (il peut avoir un fils droit, comme `2` dans l’arbre en peigne).

## Le parcours infixe trie

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 5</span> — Infixe et tri par ABR <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-arbres-tp-1-5 }

1.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire la méthode `infixe()`, qui renvoie la **liste** des valeurs dans l’ordre du parcours infixe. On pourra définir, *à l’intérieur* de la méthode, une fonction récursive `parcours(n)` qui ajoute les valeurs du sous-arbre de racine `n` à une liste `res`.

    ??? pouce "Coup de pouce"

        `parcours(n)` : si `n` n’est pas `None`, parcourir le sous-arbre gauche, ajouter `n.valeur` à `res`, puis parcourir le sous-arbre droit. La méthode appelle `parcours(self._racine)` puis renvoie `res`.

2.  Sur l’arbre de l’exercice 1, que renvoie `infixe()` ? Expliquer, à l’aide de la définition d’un ABR, pourquoi le parcours infixe donne **toujours** les valeurs dans l’ordre croissant.

3.  <span class="run" title="À programmer et tester sur machine">▶</span> En déduire une fonction `tri_abr(tab)` de **trois lignes** (sans compter la ligne `def`) qui trie une liste. Que deviennent les doublons ?

    ```text
    >>> tri_abr([5, 3, 9, 3, 1, 7])
    [1, 3, 5, 7, 9]
    ```

4.  <span class="run" title="À programmer et tester sur machine">▶</span> Tester `tri_abr` sur $200$ listes aléatoires en comparant son résultat à `sorted(set(t))`.

??? corrige "Corrigé"

    **1. et 3.**

    ```python
        def infixe(self):
            res = []
            def parcours(n):
                if n is not None:
                    parcours(n.gauche)
                    res.append(n.valeur)
                    parcours(n.droite)
            parcours(self._racine)
            return res

    def tri_abr(tab):
        arbre = ABR()
        for x in tab:
            arbre.inserer(x)
        return arbre.infixe()
    ```

    *Autre méthode :* sans fonction intérieure, une fonction récursive qui **renvoie** la liste infixe d’un sous-arbre : celle de gauche, puis la racine, puis celle de droite, recollées par concaténation.

    ```python
    def infixe_noeud(n):
        if n is None:
            return []
        return infixe_noeud(n.gauche) + [n.valeur] + infixe_noeud(n.droite)

        def infixe(self):                      # dans la classe ABR
            return infixe_noeud(self._racine)
    ```

    **2.** `[2, 5, 8, 10, 12, 15, 18, 20, 25]`. En chaque nœud, le parcours infixe écrit d’abord tout le sous-arbre gauche (valeurs plus petites), puis le nœud, puis tout le sous-arbre droit (valeurs plus grandes) ; comme c’est vrai à tous les niveaux, la liste obtenue est croissante.

    **3.** Les doublons disparaissent, car `inserer` les refuse : `tri_abr` renvoie `sorted(set(tab))`.

    **4.** Les $200$ comparaisons avec `sorted(set(t))` sont toutes égales.

    ```python
    for essai in range(200):
        t = [random.randint(0, 50) for i in range(random.randint(0, 30))]
        assert tri_abr(t) == sorted(set(t))
    ```

## Mesurer la hauteur

Le cours affirme qu’un ABR de $n$ valeurs « bien rempli » a une hauteur proche de $\log_2(n)$, mais qu’un ABR déséquilibré peut atteindre une hauteur $n$. Vérifions-le.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Au hasard ou dans l’ordre <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-arbres-tp-1-6 }

1.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire `hauteur_triee(n)`, qui renvoie la hauteur de l’ABR obtenu en insérant `0, 1, …, n-1` dans l’ordre, et `hauteur_aleatoire(n, essais=20)`, qui renvoie la hauteur **moyenne** sur `essais` ABR obtenus en insérant ces mêmes entiers dans un ordre aléatoire (`random.shuffle`).

    ??? pouce "Coup de pouce"

        Pour `hauteur_aleatoire` : à chaque essai, construire `valeurs = list(range(n))`, la mélanger, l’insérer dans un nouvel `ABR`, puis ajouter sa hauteur à un total.

2.  <span class="run" title="À programmer et tester sur machine">▶</span> Recopier et compléter sur le cahier le tableau suivant (la hauteur triée pour $n = 10\,000$ se déduit sans calcul).

    | $n$                        |  $10$   | $100$ | $1\,000$ | $10\,000$ |
    |:---------------------------|:-------:|:-----:|:--------:|:---------:|
    | $\log_2(n)$ (`math.log2`)  | $3{,}3$ |       |          |           |
    | hauteur moyenne, au hasard |         |       |          |           |
    | hauteur, valeurs triées    |         |       |          |           |

3.  Que vaut à peu près le rapport entre la hauteur moyenne au hasard et $\log_2(n)$ ? Comment évolue la hauteur au hasard quand $n$ est multiplié par $10$ ?

4.  <span class="run" title="À programmer et tester sur machine">▶</span> Tracer les deux courbes avec `matplotlib`, ainsi que $\log_2(n)$, pour $n$ parmi `10, 20, 50, 100, 200, 500, 1000, 2000` (valeurs triées) et jusqu’à `10000` (au hasard). Les échelles logarithmiques (`plt.xscale("log")` et `plt.yscale("log")`) rendent le graphique lisible.

5.  Le fichier de départ commence par `sys.setrecursionlimit(20000)`. Sans cette ligne, quel calcul échouerait, et pourquoi ? *(Penser à la forme de l’arbre et à la fonction `hauteur`.)*

??? corrige "Corrigé"

    **1.**

    ```python
    def hauteur_triee(n):
        arbre = ABR()
        for v in range(n):
            arbre.inserer(v)
        return arbre.hauteur()

    def hauteur_aleatoire(n, essais=20):
        total = 0
        for k in range(essais):
            valeurs = list(range(n))
            random.shuffle(valeurs)
            arbre = ABR()
            for v in valeurs:
                arbre.inserer(v)
            total = total + arbre.hauteur()
        return total / essais
    ```

    **2.** Mesures obtenues (`random.seed(2026)` exécuté une seule fois, puis `hauteur_aleatoire(n)` appelée pour $n = 10$, $100$, $1\,000$, $10\,000$ dans cet ordre ; sans graine, les moyennes au hasard varient d’une ou deux unités) :

    | $n$                        |   $10$   |  $100$   | $1\,000$ | $10\,000$ |
    |:---------------------------|:--------:|:--------:|:--------:|:---------:|
    | $\log_2(n)$                | $3{,}3$  | $6{,}6$  | $10{,}0$ | $13{,}3$  |
    | hauteur moyenne, au hasard | $5{,}45$ | $12{,}8$ | $22{,}3$ | $31{,}05$ |
    | hauteur, valeurs triées    |   $10$   |  $100$   | $1\,000$ | $10\,000$ |

    **3.** Au hasard, la hauteur vaut environ **2 à 2,3 fois** $\log_2(n)$ (un peu moins pour les petites valeurs de $n$) : elle n’augmente que de $7$ à $10$ environ quand $n$ est multiplié par $10$ (croissance logarithmique). Avec des valeurs triées, la hauteur vaut $n$ : elle est multipliée par $10$.

    **4.**

    ```python
    import matplotlib.pyplot as plt
    ns = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
    nt = [n for n in ns if n <= 2000]
    plt.plot(nt, [hauteur_triee(n) for n in nt], "o-", label="valeurs triees")
    plt.plot(ns, [hauteur_aleatoire(n) for n in ns], "o-", label="au hasard")
    plt.plot(ns, [math.log2(n) for n in ns], "--", label="log2(n)")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("n")
    plt.ylabel("hauteur")
    plt.legend()
    plt.show()
    ```

    \*(image manquante : 04ct1_tp_arbres_hauteurs)\*

    En échelles logarithmiques, la droite rouge (pente $1$) traduit une hauteur proportionnelle à $n$ ; la courbe verte reste parallèle à $\log_2(n)$, environ deux fois au-dessus.

    **5.** `hauteur` est récursive : sur un peigne de $1\,000$ nœuds ou plus, elle s’appelle elle-même $1\,000$ fois en cascade, ce qui dépasse la limite par défaut de Python (environ $1\,000$ appels imbriqués) : `RecursionError`. L’insertion, écrite avec une boucle, n’a pas ce problème.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Ce que cela coûte vraiment <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-arbres-tp-1-7 }

<span class="run" title="À programmer et tester sur machine">▶</span> On insère les entiers de $0$ à $999$, une fois dans un ordre aléatoire (arbre `ar`), une fois dans l’ordre (arbre `at`). Pour chaque arbre, calculer le nombre **moyen** et le nombre **maximal** de nœuds visités par `contient(v)` quand `v` parcourt `range(1000)`. Comparer avec la recherche dans une liste non triée, puis avec la recherche dichotomique dans une liste triée (Première). Conclure : quand un ABR est-il intéressant ?

??? corrige "Corrigé"

    ```python
    random.seed(2026)
    valeurs = list(range(1000))
    random.shuffle(valeurs)
    ar = ABR()
    at = ABR()
    for v in valeurs:
        ar.inserer(v)
    for v in range(1000):
        at.inserer(v)
    for arbre in [ar, at]:
        visites = [arbre.contient(v)[1] for v in range(1000)]
        print(sum(visites) / 1000, max(visites))
    ```

    Arbre au hasard : **11,8** visites en moyenne, **22** au pire (sa hauteur). Arbre trié : **500,5** en moyenne, **1000** au pire — exactement comme une recherche séquentielle dans une liste non triée ($500{,}5$ et $1\,000$). La dichotomie dans une liste triée fait au plus $10$ comparaisons. Un ABR n’est intéressant que s’il reste **peu haut** ; il a alors l’avantage sur la liste triée d’accepter des insertions rapides (pas de décalage).

## Application : l’index d’un texte

À la fin d’un livre, l’**index** donne, pour chaque mot important, les pages où il apparaît, **par ordre alphabétique**. On le construit avec un ABR dont les clés sont des **mots** (les chaînes se comparent avec `<` dans l’ordre du dictionnaire) et dont chaque nœud (classe fournie `NoeudIndex`) porte aussi la liste `lignes` des numéros de lignes où le mot apparaît.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Construire et interroger l’index <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-arbres-tp-1-8 }

1.  <span class="run" title="À programmer et tester sur machine">▶</span> Compléter la méthode `ajouter(mot, ligne)` de la classe `Index` : on descend dans l’ABR comme pour `inserer` ; si le mot est absent, on crée son nœud (et l’on incrémente `_nb_mots`) ; on ajoute ensuite `ligne` à la liste du nœud, sauf si ce numéro y figure déjà (les lignes arrivent dans l’ordre : il suffit de regarder le dernier).

    ??? pouce "Coup de pouce"

        Écrire la boucle `while n.valeur != mot` : à chaque tour, si le fils où il faut descendre est `None`, on y crée d’abord un `NoeudIndex(mot)`, puis on descend. En sortie de boucle, `n` est le nœud du mot.

2.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire `lignes(mot)` (recherche itérative) et `afficher()` (parcours infixe), puis construire l’index du texte fourni avec `idx = indexer(TEXTE)`.

    ```text
    >>> idx.lignes("hauteur")
    [6, 9, 12]
    >>> idx.afficher()
    a : 9
    arbre : 1, 6, 8
    arbres : 11
    ...
    ```

3.  Combien de mots différents l’index contient-il ? Comparer la hauteur de l’index à $\log_2$ de ce nombre. Les mots d’un texte arrivent-ils « au hasard » ou « triés » ?

4.  Où les mots `à`, `élimine` et `équilibré` apparaissent-ils dans l’affichage ? Expliquer (`ord("é")` et `ord("z")` aideront). Proposer une façon d’obtenir un vrai ordre alphabétique.

??? corrige "Corrigé"

    **1. et 2.**

    ```python
        def ajouter(self, mot, ligne):
            if self._racine is None:
                self._racine = NoeudIndex(mot)
                self._nb_mots = 1
            n = self._racine
            while n.valeur != mot:
                if mot < n.valeur:
                    if n.gauche is None:
                        n.gauche = NoeudIndex(mot)
                        self._nb_mots = self._nb_mots + 1
                    n = n.gauche
                else:
                    if n.droite is None:
                        n.droite = NoeudIndex(mot)
                        self._nb_mots = self._nb_mots + 1
                    n = n.droite
            if n.lignes == [] or n.lignes[-1] != ligne:
                n.lignes.append(ligne)

        def lignes(self, mot):
            n = self._racine
            while n is not None:
                if mot == n.valeur:
                    return n.lignes
                if mot < n.valeur:
                    n = n.gauche
                else:
                    n = n.droite
            return []

        def afficher(self):
            def parcours(n):
                if n is not None:
                    parcours(n.gauche)
                    texte = str(n.lignes[0])
                    for i in range(1, len(n.lignes)):
                        texte = texte + ", " + str(n.lignes[i])
                    print(n.valeur, ":", texte)
                    parcours(n.droite)
            parcours(self._racine)
    ```

    **3.** L’index contient **77** mots différents ; sa hauteur est **15**, pour $\log_2(77) \approx 6{,}3$. Les mots d’un texte n’arrivent ni triés ni vraiment au hasard : l’arbre est plus haut que le minimum possible ($7$), mais très loin du peigne ($77$).

    **4.** Ils apparaissent **à la fin**, après `valeurs` : `à`, puis `égale`, `élimine`, `équilibré`, `équilibrés`. Python compare les chaînes caractère par caractère selon leur code : `ord("é")` vaut $233$ et `ord("à")` $224$, bien plus que `ord("z")` $= 122$. Pour un vrai ordre alphabétique, on peut ranger les nœuds selon une **clé sans accents** (fonction qui remplace `é`, `è`, `ê` par `e`, `à` par `a`, etc.) tout en affichant le mot d’origine.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 9</span> — Défi — toutes les valeurs d’un intervalle <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-arbres-tp-1-9 }

1.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire la méthode `entre(a, b)` de la classe `ABR`, qui renvoie le couple formé de la liste croissante des valeurs `v` telles que `a <= v <= b`, et du nombre de nœuds visités. Elle ne doit **pas** explorer les sous-arbres qui ne peuvent rien contenir d’utile : quand la valeur d’un nœud est inférieure ou égale à `a`, son sous-arbre gauche est inutile ; quand elle est supérieure ou égale à `b`, son sous-arbre droit l’est.

    ```text
    >>> a.entre(9, 19)
    ([10, 12, 15, 18], 6)
    ```

2.  <span class="run" title="À programmer et tester sur machine">▶</span> Sur les arbres `ar` et `at` de l’exercice 7, comparer le nombre de nœuds visités par `entre(500, 509)`.

3.  <span class="run" title="À programmer et tester sur machine">▶</span> *(Application.)* Écrire, dans la classe `Index`, une méthode `commencant_par(prefixe)` qui renvoie les mots de l’index commençant par `prefixe`, dans l’ordre, en élaguant de la même façon : c’est le principe de l’**autocomplétion**. Par exemple, `commencant_par("arb")` renvoie `[’arbre’, ’arbres’]`.

??? corrige "Corrigé"

    ```python
        def entre(self, a, b):
            res = []
            def parcours(n):                     # renvoie le nombre de noeuds visites
                if n is None:
                    return 0
                visites = 1
                if a < n.valeur:                 # a gauche, il peut y avoir des valeurs >= a
                    visites = visites + parcours(n.gauche)
                if a <= n.valeur <= b:
                    res.append(n.valeur)
                if n.valeur < b:                 # a droite, il peut y avoir des valeurs <= b
                    visites = visites + parcours(n.droite)
                return visites
            nb = parcours(self._racine)
            return res, nb
    ```

    **1.** Sur l’arbre de l’exercice 1 : `([10, 12, 15, 18], 6)` — les nœuds `5`, `2` et `25` ne sont jamais visités.

    **2.** `entre(500, 509)` visite **24** nœuds dans `ar`, contre **510** dans `at` (il faut descendre le peigne jusqu’à `509`).

    **3.** Un mot commence par `prefixe` s’il est compris entre `prefixe` et les mots qui le prolongent ; on élague donc de la même façon :

    ```python
        def commencant_par(self, prefixe):
            res = []
            def parcours(n):
                if n is None:
                    return
                if prefixe < n.valeur:
                    parcours(n.gauche)
                commence = n.valeur[:len(prefixe)] == prefixe   # memes premieres lettres ?
                if commence:
                    res.append(n.valeur)
                if n.valeur < prefixe or commence:
                    parcours(n.droite)
            parcours(self._racine)
            return res
    ```

    `commencant_par("arb")` renvoie `[’arbre’, ’arbres’]` ; `commencant_par("rech")` renvoie `[’recherche’]`.

## Bilan à rédiger

### <span class="exo-num">Exercice 10</span> — Ce que j’ai mesuré <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-arbres-tp-1-10 }

Rédiger, en une dizaine de lignes, un bilan qui répond aux questions suivantes.

1.  De quoi dépend le coût d’une recherche dans un ABR ? Citer vos mesures pour $n = 1\,000$ (hauteur, nombre moyen de visites) dans les deux cas.

2.  Dans quelles situations réelles risque-t-on d’insérer des valeurs déjà triées ? Comment une base de données pourrait-elle s’en protéger ? *(Penser à la hauteur de l’arbre : quelle forme faudrait-il lui garantir, quel que soit l’ordre des insertions ?)*

3.  Quelles propriétés de l’ABR l’index a-t-il utilisées ? Citer deux méthodes du TP et la propriété dont chacune dépend.

??? corrige "Corrigé"

    Éléments attendus :

    - Le coût d’une recherche est au plus la **hauteur** ; il dépend donc de la **forme** de l’arbre, c’est-à-dire de l’ordre d’insertion. Pour $n = 1\,000$ : hauteur $\approx 22$ et $\approx 12$ visites en moyenne au hasard ; hauteur $1\,000$ et $500$ visites en moyenne avec des valeurs triées.

    - Valeurs triées en pratique : numéros de dossiers ou d’élèves attribués dans l’ordre, dates d’inscription, identifiants croissants d’une base. Les bases de données utilisent des arbres **équilibrés** (B-arbres) qui se réorganisent pour garder une hauteur petite.

    - L’index utilise l’**ordre** de l’ABR : la recherche (`lignes`, `ajouter`) descend d’un seul côté à chaque nœud ; l’affichage (`afficher`) repose sur le fait que le parcours infixe donne les clés triées ; `commencant_par` élague grâce à l’ordre.
