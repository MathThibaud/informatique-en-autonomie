# Exercices

<p class="sous-titre">Les $k$k plus proches voisins</p>

!!! consignes "Mode d’emploi"

    - Niveau : ★ échauffement, ★★ classique (niveau bac), ★★★ défi ; les *coups de pouce* et les *corrigés* se déplient sous chaque exercice.

    - <span class="run" title="À programmer et tester sur machine">▶</span> *À programmer et tester* en Python. Rappel : pour *comparer* des distances, on peut garder la **somme des carrés** (sans racine).

    - Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la [charte d’usage de l’IA](../charte.md).

### Classification et distance

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — Le vocabulaire <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-12-1 }

Répondre par une phrase.

1.  Qu’est-ce qu’une classification **supervisée** ?

2.  Dans le $k$-NN, que représentent les **descripteurs** d’un individu ? son **étiquette** ?

3.  Résumer la méthode des $k$ plus proches voisins en une phrase.

??? corrige "Corrigé"

    !!! remarque "Remarque"

        On donne **une** version simple ; d’autres écritures sont possibles.

    **a)** Apprendre à prédire une étiquette à partir d’**exemples déjà étiquetés**. **b)** Les descripteurs sont les **mesures** (les coordonnées) de l’individu ; l’étiquette est sa **classe**. **c)** On calcule la distance de l’individu à tous les exemples, on garde les $k$ plus proches, on prend leur classe **majoritaire**.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 2</span> — Calculer des distances <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-12-2 }

1.  Distance euclidienne entre $A=(3 ; 4)$ et $B=(0 ; 0)$.

2.  Distance entre $A=(1 ; 2 ; 2)$ et $B=(4 ; 2 ; 6)$ (trois descripteurs).

3.  Entre $A=(4.7 ; 1.4)$ et $B=(4.5 ; 1.5)$, donner la distance **au carré**, puis la distance.

??? corrige "Corrigé"

    **a)** $\sqrt{3^2+4^2}=\sqrt{25}=\textbf{5}$. **b)** $\sqrt{3^2+0^2+4^2}=\sqrt{25}=\textbf{5}$. **c)** $d^2=0.2^2+0.1^2=0.04+0.01=\textbf{0.05}$ ; $d=\sqrt{0.05}\approx\textbf{0.22}$.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 3</span> — Qui gagne le vote ? <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-12-3 }

On a déjà calculé la distance au carré entre un fruit inconnu $x$ et six fruits étiquetés.

|  **fruit**  |   1   |   2   |   3   |   4   |   5   |   6   |
|:-----------:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| $d^2$ à $x$ |   2   |   9   |   1   |   5   |   3   |  12   |
|  étiquette  | pomme | poire | poire | pomme | pomme | poire |

1.  Ranger les six fruits du plus proche au plus lointain de $x$.

2.  Quelle étiquette prédit le $1$-NN ? le $3$-NN ? le $5$-NN ?

??? corrige "Corrigé"

    **a)** Fruit 3 ($d^2=1$, poire), 1 (2, pomme), 5 (3, pomme), 4 (5, pomme), 2 (9, poire), 6 (12, poire). **b)** $1$-NN : **poire**. $3$-NN : poire, pomme, pomme $\to$ **pomme**. $5$-NN : 3 pommes contre 2 poires $\to$ **pomme**. La prédiction peut changer avec $k$.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 4</span> — Dérouler le $k$-NN à la main (iris) <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-12-4 }

On dispose des exemples suivants (longueur ; largeur de pétale $\to$ espèce) :

| **long.** | **larg.** | **espèce** |
|:---------:|:---------:|:----------:|
|    1.4    |    0.2    |   setosa   |
|    1.5    |    0.2    |   setosa   |
|    4.5    |    1.5    | versicolor |
|    4.9    |    1.5    | versicolor |
|    5.5    |    2.1    | virginica  |
|    5.8    |    2.2    | virginica  |

On veut classer la fleur $x = (4.7 ; 1.4)$.

1.  Calculer la distance **au carré** de $x$ à chacun des 6 exemples.

2.  Quelle espèce prédit le $1$-NN (le plus proche voisin) ?

3.  Quelle espèce prédit le $3$-NN (vote des 3 plus proches) ?

    ??? pouce "Coup de pouce"

        Pour chaque exemple : carré de l’écart des longueurs, plus carré de l’écart des largeurs. Ranger ensuite les six résultats dans l’ordre croissant avant de voter.

??? corrige "Corrigé"

    **a)** Distances au carré de $x=(4.7;1.4)$ :

    | **exemple** | **espèce** | **$d^2$** |
    |:-----------:|:----------:|:---------:|
    |  (1.4;0.2)  |   setosa   |   12.33   |
    |  (1.5;0.2)  |   setosa   |   11.68   |
    |  (4.5;1.5)  | versicolor | **0.05**  |
    |  (4.9;1.5)  | versicolor | **0.05**  |
    |  (5.5;2.1)  | virginica  | **1.13**  |
    |  (5.8;2.2)  | virginica  |   1.85    |

    **b)** $1$-NN : le plus proche est une *versicolor* $\to$ **versicolor**. **c)** $3$-NN : deux versicolor (0.05 ; 0.05) et une virginica (1.13) $\to$ **versicolor**.

### Programmer le $k$-NN

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 5</span> — <span class="run" title="À programmer et tester sur machine">▶</span>  Les briques de base <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-5 }

Écrire (ou compléter) les fonctions Python :

1.  `distance2(a, b)` : la somme des carrés des écarts entre deux listes de même longueur, c’est-à-dire la distance **au carré** $d^2$ du cours (sans racine : pour comparer des distances, elle suffit) ;

2.  `vote(etiquettes)` : l’étiquette la plus fréquente d’une liste (avec un dictionnaire d’occurrences).

    ??? pouce "Coup de pouce"

        `distance2` : un accumulateur et une boucle sur les indices. `vote` : compter d’abord chaque étiquette dans un dictionnaire, puis chercher l’étiquette de compte maximal (invariant du champion).

??? corrige "Corrigé"

    ```python
    def distance2(a, b):
        s = 0
        for i in range(len(a)):
            s = s + (a[i] - b[i]) ** 2
        return s            # distance au carre (racine inutile pour comparer)

    def vote(etiquettes):
        compte = {}
        for e in etiquettes:
            compte[e] = compte.get(e, 0) + 1
        meilleure = None
        for e in compte:
            if meilleure is None or compte[e] > compte[meilleure]:
                meilleure = e
        return meilleure
    ```

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 6</span> — <span class="run" title="À programmer et tester sur machine">▶</span>  Le plus proche voisin, à trous <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-12-6 }

La fonction suivante renvoie l’étiquette de l’exemple le plus proche de `x` (c’est le $1$-NN). Elle utilise la fonction `distance2` de l’exercice précédent.

```python
def plus_proche(exemples, x):
    dists = []
    for descripteurs, etiquette in exemples:
        dists.append((.................... , etiquette))
    dists.sort(key=lambda couple: ..........)
    return dists[.....][1]
```

1.  Compléter les trois trous.

2.  Que contient la liste `dists` après le tri ? Que désigne `dists[0][1]` ?

3.  Tester avec les six iris de l’exercice 4 et `x = [4.7, 1.4]` : on doit obtenir `’versicolor’`.

??? corrige "Corrigé"

    **a)**

    ```python
    def plus_proche(exemples, x):
        dists = []
        for descripteurs, etiquette in exemples:
            dists.append((distance2(x, descripteurs), etiquette))
        dists.sort(key=lambda couple: couple[0])
        return dists[0][1]
    ```

    **b)** Après le tri, `dists` contient les couples `(distance au carré, etiquette)` rangés par distance **croissante**. `dists[0]` est le couple le plus proche ; `dists[0][1]` est donc l’étiquette du plus proche voisin. **c)** `plus_proche(iris, [4.7, 1.4])` renvoie `’versicolor’` (distance au carré $0.05$).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — <span class="run" title="À programmer et tester sur machine">▶</span>  Classer <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-7 }

On représente les exemples par une liste de couples `(descripteurs, etiquette)`. Écrire :

1.  `k_plus_proches(exemples, x, k)` : la liste des étiquettes des $k$ exemples les plus proches de `x` (trier selon `distance2`) ;

2.  `classer(exemples, x, k)` qui renvoie l’étiquette prédite pour `x`.

Tester sur la table des iris de l’exercice 4 avec `x = [4.7, 1.4]` et $k=3$.

??? pouce "Coup de pouce"

    Ranger dans une liste des couples `(distance2(x, descripteurs), etiquette)`, puis trier cette liste en disant à `sort` sur quoi comparer : avec `key=lambda couple: couple[0]`, on trie selon le premier élément de chaque couple, la distance.

??? pouce "Coup de pouce 2 (début de solution)"

    `def k_plus_proches(exemples, x, k):`  
    `dists = []`  
    `for descripteurs, etiquette in exemples:`  
    …

??? corrige "Corrigé"

    ```python
    def k_plus_proches(exemples, x, k):
        dists = []
        for descripteurs, classe in exemples:
            dists.append((distance2(x, descripteurs), classe))
        dists.sort(key=lambda couple: couple[0])
        return [classe for (d, classe) in dists[:k]]

    def classer(exemples, x, k):
        return vote(k_plus_proches(exemples, x, k))
    ```

    Sur les iris avec `x=[4.7,1.4]` et $k=3$ : `’versicolor’`.

    *Autre méthode :* la liste `dists` se construit aussi par compréhension, en une ligne : `dists = [(distance2(x, d), classe) for (d, classe) in exemples]`.

### Choisir $k$, comprendre les limites

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — L’effet de $k$ <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-12-8 }

1.  Pourquoi $k=1$ est-il très sensible à un exemple **aberrant** (mal étiqueté) ?

2.  Que prédit le $k$-NN si l’on prend $k$ égal au **nombre total** d’exemples ? Le résultat dépend-il encore de $x$ ?

3.  Pour un problème à **deux** classes, pourquoi préfère-t-on un $k$ **impair** ?

    ??? pouce "Coup de pouce"

        Pour b), imaginer que tous les exemples votent : la position de `x` change-t-elle encore le résultat ? Pour c), essayer un vote à 4 voisins entre deux classes.

??? corrige "Corrigé"

    **a)** Avec $k=1$, la prédiction **copie** le seul voisin le plus proche : si c’est un exemple mal étiqueté, la réponse est fausse. **b)** Si $k=$ nombre total d’exemples, tous votent : on renvoie **toujours** la classe globalement majoritaire, *sans plus dépendre* de $x$. **c)** Un $k$ **impair** évite les **égalités** de vote entre les deux classes.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 9</span> — <span class="run" title="À programmer et tester sur machine">▶</span>  Départager une égalité <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-9 }

Le vote peut aboutir à une **égalité**. Une règle courante : en cas d’égalité, on **retire le voisin le plus lointain** et on revote, jusqu’à ce qu’une seule classe arrive en tête.

1.  Avec les six iris de l’exercice 4 et $x = (4.7 ; 1.4)$, pour quelles valeurs de $k$ le vote est-il à égalité ?

2.  Écrire `vote_departage(voisins)`, où `voisins` est la liste des étiquettes des voisins, rangées du plus proche au plus lointain, qui applique cette règle.

3.  Tester : `vote_departage(["A", "B", "B", "A", "C"])` doit renvoyer `"B"`. Expliquer pourquoi ce n’est pas l’étiquette du voisin le plus proche.

??? pouce "Coup de pouce"

    Écrire d’abord une fonction qui compte les voix dans un dictionnaire. Ensuite, tant que plusieurs classes ont le nombre maximal de voix, recommencer sur la liste privée de son dernier élément.

??? pouce "Coup de pouce 2 (début de solution)"

    `def vote_departage(voisins):`  
    `n = len(voisins)`  
    `while n > 0:`  
    `compte = compter(voisins[:n])`  
    …

??? corrige "Corrigé"

    **a)** Voisins rangés : versicolor, versicolor, virginica, virginica, setosa, setosa. Égalité pour $k = 4$ (2 contre 2), $k = 5$ (2, 2 et 1) et $k = 6$ (2, 2 et 2). **b)**

    ```python
    def compter(voisins):
        compte = {}
        for c in voisins:
            compte[c] = compte.get(c, 0) + 1
        return compte

    def vote_departage(voisins):
        n = len(voisins)
        while n > 0:
            compte = compter(voisins[:n])
            maxi = 0
            for c in compte:
                if compte[c] > maxi:
                    maxi = compte[c]
            gagnants = [c for c in compte if compte[c] == maxi]
            if len(gagnants) == 1:
                return gagnants[0]
            n = n - 1          # egalite : on retire le voisin le plus lointain
    ```

    La boucle s’arrête : avec un seul voisin, il ne peut pas y avoir d’égalité. **c)** Avec 5 voisins : A 2, B 2, C 1 (égalité) ; avec 4 : A 2, B 2 (égalité) ; avec 3 : A 1, B 2 $\to$ `"B"`. Le plus proche voisin est un A, mais une fois les voisins lointains retirés, B reste majoritaire : la règle départage par le **vote**, pas par le premier voisin. Sur les iris, avec $k = 4$, 5 ou 6, on obtient `’versicolor’`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 10</span> — Le piège de l’échelle <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-10 }

On classe des personnes par leur **âge** (de 0 à 100) et leur **revenu mensuel** (de 0 à 5000). On utilise la distance euclidienne brute.

1.  Entre deux personnes, quel descripteur **domine** la distance ? Pourquoi ?

2.  Que faut-il faire avant d’appliquer le $k$-NN pour que les deux descripteurs comptent *équitablement* ?

    ??? pouce "Coup de pouce"

        Comparer un écart typique de 10 ans et un écart typique de 200 € : que valent leurs carrés ?

??? corrige "Corrigé"

    **a)** Le **revenu** domine : un écart de 200 € pèse $200^2=40\,000$, alors qu’un écart de 10 ans ne pèse que $10^2=100$. L’âge devient négligeable. **b)** Il faut **normaliser** : ramener chaque descripteur à la même échelle (par exemple entre 0 et 1) pour qu’ils comptent équitablement.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 11</span> — Le coût <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-12-11 }

Une base contient $10\,000$ exemples, chacun décrit par $196$ pixels.

1.  Pour classer **une** image, à combien d’exemples doit-on calculer la distance ?

2.  Pourquoi dit-on que le $k$-NN est un algorithme « paresseux » ? Quel est le coût par prédiction (linéaire, quadratique…) en le nombre d’exemples ?

??? corrige "Corrigé"

    **a)** À **10 000** exemples (tous). **b)** « Paresseux » car il ne construit **aucun modèle** au préalable : il garde tout et compare à la demande. Coût **linéaire** en le nombre d’exemples, à chaque prédiction.

### Applications

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 12</span> — Recommander un poste (football) <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-12-12 }

On décrit des joueurs par leur **taille** (cm) et leur **poids** (kg), avec leur **poste** :

| **taille** | **poids** | **poste** |
|:----------:|:---------:|:---------:|
|    180     |    75     |  milieu   |
|    178     |    72     |  milieu   |
|    192     |    88     | défenseur |
|    195     |    90     | défenseur |
|    170     |    65     | attaquant |
|    173     |    68     | attaquant |

Un nouveau joueur mesure $176$ cm pour $70$ kg.

1.  Calculer la distance au carré aux 6 joueurs.

2.  Quel poste recommande le $1$-NN ? le $3$-NN ?

3.  Ici taille et poids ont des ordres de grandeur *proches* : faut-il normaliser ? (Contraster avec l’exercice « âge / revenu ».)

    ??? pouce "Coup de pouce"

        Même méthode que pour les iris : un tableau des six distances au carré, rangées dans l’ordre croissant.

??? corrige "Corrigé"

    **a)** Distances au carré de $(176;70)$ :

    | **joueur** | **poste** | **$d^2$** |
    |:----------:|:---------:|:---------:|
    |  (180;75)  |  milieu   |    41     |
    |  (178;72)  |  milieu   |   **8**   |
    |  (192;88)  | défenseur |    580    |
    |  (195;90)  | défenseur |    761    |
    |  (170;65)  | attaquant |    61     |
    |  (173;68)  | attaquant |  **13**   |

    **b)** $1$-NN : le plus proche (8) est un **milieu**. $3$-NN : les trois plus proches sont 8 (milieu), 13 (attaquant), 41 (milieu) $\to$ 2 milieux contre 1 $\to$ **milieu**. **c)** Ici taille ($\sim$<!-- -->170–195) et poids ($\sim$<!-- -->65–90) sont du **même ordre** : la normalisation n’est pas indispensable. Au contraire, âge (0–100) et revenu (0–5000) diffèrent d’un facteur $\sim$<!-- -->50, d’où l’obligation de normaliser dans l’exercice précédent.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 13</span> — Reconnaître une image $3\times3$ (sans machine) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-13 }

Une image $3\times3$ est une liste de 9 pixels (0 blanc, 1 encre), lus ligne par ligne. On a deux **modèles** étiquetés : $$T=\begin{smallmatrix}1&1&1\\0&1&0\\0&1&0\end{smallmatrix}\quad(\text{« T »})
\qquad\qquad
L=\begin{smallmatrix}1&0&0\\1&0&0\\1&1&1\end{smallmatrix}\quad(\text{« L »})$$ On reçoit l’image inconnue \; $N=\begin{smallmatrix}1&1&1\\0&1&0\\0&1&1\end{smallmatrix}$.

1.  Écrire $T$, $L$ et $N$ comme des listes de 9 nombres.

2.  Avec des pixels 0/1, la distance au carré compte le **nombre de pixels différents**. Calculer $d(N,T)$ et $d(N,L)$.

3.  Que prédit le $1$-NN ? Cela vous semble-t-il correct visuellement ?

    ??? pouce "Coup de pouce"

        Comparer les deux listes case par case et compter les cases où elles diffèrent.

??? corrige "Corrigé"

    **a)** $T=[1,1,1,0,1,0,0,1,0]$, $L=[1,0,0,1,0,0,1,1,1]$, $N=[1,1,1,0,1,0,0,1,1]$. **b)** $N$ et $T$ ne diffèrent que sur le **dernier** pixel $\to d^2(N,T)=\textbf{1}$. $N$ et $L$ diffèrent sur **5** pixels $\to d^2(N,L)=\textbf{5}$. **c)** Le $1$-NN prédit **T** (le plus proche). C’est cohérent : $N$ est un « T » avec un pixel d’encre en plus.

### Mini-problème de synthèse

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 14</span> — Évaluer la qualité <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-14 }

On dispose d’exemples **d’entraînement** (étiquetés) et d’exemples **de test** (étiquetés eux aussi, mais on *cache* l’étiquette pour évaluer).

1.  <span class="run" title="À programmer et tester sur machine">▶</span>  Écrire `taux_reussite(train, test, k)` qui renvoie la proportion d’exemples de `test` correctement classés par le $k$-NN entraîné sur `train`.

2.  Pourquoi mesure-t-on la qualité sur des exemples **de test** et non sur ceux d’entraînement ?

3.  On teste $k = 1, 3, 5, 7$ et on garde le meilleur taux. Comment s’appelle cette démarche de **choix** de $k$ ?

    ??? pouce "Coup de pouce"

        Pour a), parcourir les couples de `test`, prédire l’étiquette de chacun avec `classer(train, …, k)`, compter les bonnes réponses, puis diviser par le nombre d’exemples de test.

    ??? pouce "Coup de pouce 2 (début de solution)"

        `def taux_reussite(train, test, k):`  
        `bons = 0`  
        `for descripteurs, etiquette in test:`  
        …

??? corrige "Corrigé"

    **a)**

    ```python
    def taux_reussite(train, test, k):
        bons = 0
        for descripteurs, vraie in test:
            if classer(train, descripteurs, k) == vraie:
                bons += 1
        return bons / len(test)
    ```

    **b)** Sur les exemples d’entraînement, l’évaluation est **trompeuse** (avec $k=1$, chaque exemple est son propre voisin $\to$ 100 %). Seul un jeu de **test** (jamais vu) mesure la capacité à **généraliser**. **c)** Tester plusieurs $k$ et garder le meilleur, c’est le **réglage** (ou *choix*) de $k$.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 15</span> — Un $k$-NN selon un assistant d’IA <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> { #ex-12-15 }

Un élève demande à un assistant d’IA : « Écris en Python une fonction `classer(exemples, x, k)` des $k$ plus proches voisins, où `exemples` est une liste de couples `(descripteurs, classe)`. » Voici la réponse obtenue (`distance` est la fonction du cours).

```python
def classer(exemples, x, k):
    dists = []
    for descripteurs, classe in exemples:
        dists.append((classe, distance(x, descripteurs)))
    dists.sort()                  # du plus proche au plus lointain
    compte = {}
    for classe, d in dists[:k]:   # les k voisins
        compte[classe] = compte.get(classe, 0) + 1
    meilleure = None
    for c in compte:
        if meilleure is None or compte[c] > compte[meilleure]:
            meilleure = c
    return meilleure
```

« On calcule la distance de `x` à chaque exemple, on trie, on garde les $k$ premiers et on renvoie leur classe majoritaire. »

1.  La réponse est-elle correcte ? <span class="run" title="À programmer et tester sur machine">▶</span>  Vérifier sur les six iris du cours avec $x = (4.7\,;\,1.4)$ et $k = 3$ (le cours donne *versicolor*).

2.  Localiser et corriger l’erreur.

3.  Quelle vérification simple, faite avant de faire confiance à la réponse, aurait suffi à détecter l’erreur ?

    ??? pouce "Coup de pouce"

        Dérouler le code sur les iris en écrivant le contenu de `dists` avant et après le tri.

??? corrige "Corrigé"

    **a)** Non. Sur les six iris du cours, `classer(iris, [4.7, 1.4], 3)` renvoie **`’setosa’`** (et de même avec $k = 1$), alors que les exemples les plus proches de $x$ sont des *versicolor* ($d^2 = 0.05$). **b)** L’erreur est l’ordre dans les couples : `(classe, distance)`. Le tri `dists.sort()` d’une liste de couples se fait sur le **premier** élément, donc ici par ordre **alphabétique des classes** (*setosa* avant *versicolor*), et non par distance croissante : les « $k$ premiers » sont les $k$ premiers dans l’alphabet. On met la distance en premier (ou on trie avec une clé, comme dans le cours) :

    ```python
    def classer(exemples, x, k):
        dists = []
        for descripteurs, classe in exemples:
            dists.append((distance(x, descripteurs), classe))
        dists.sort()                  # tri par distance croissante
        compte = {}
        for d, classe in dists[:k]:
            compte[classe] = compte.get(classe, 0) + 1
        meilleure = None
        for c in compte:
            if meilleure is None or compte[c] > compte[meilleure]:
                meilleure = c
        return meilleure
    ```

    Avec cette correction, l’appel renvoie `’versicolor’`. **c)** Afficher `dists` après le tri (les distances ne sont pas dans l’ordre croissant, cela saute aux yeux), ou tester sur l’exemple du cours dont on connaît la réponse.
