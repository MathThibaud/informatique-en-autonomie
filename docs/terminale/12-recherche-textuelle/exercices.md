# Exercices

<p class="sous-titre">Recherche textuelle</p>

Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la [charte d’usage de l’IA](../charte.md).

*Rappel : les positions sont comptées à partir de $0$.* Niveau : ★ échauffement, ★★ classique (niveau bac), ★★★ défi ; les *coups de pouce* et les *corrigés* se déplient sous chaque exercice.

### La méthode naïve

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — Naïf, à la main <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-12-1 }

On cherche le motif `AA` dans le texte `CAAAB`.

1.  Dérouler la méthode naïve : à quelle(s) position(s) trouve-t-on le motif ?

2.  Cette méthode compare le motif de la gauche vers la droite et décale d’un cran à chaque échec. Quel est son coût dans le **pire des cas**, en fonction de $n$ (longueur du texte) et $m$ (longueur du motif) ?

??? corrige "Corrigé"

    1.  `C``AA``AB` et `CA``AA``B` : le motif `AA` est trouvé aux positions **1** et **2**.

    2.  Au pire, on compare presque tout le motif ($m$ comparaisons) à chacune des $\approx n$ positions : coût **$O(n\times m)$** (quadratique).

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 2</span> — Naïf, en Python <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-2 }

Recopier et compléter la fonction de recherche naïve :

```python
def recherche_naive(motif, texte):
    n, m = len(texte), len(motif)
    positions = []
    for i in range(...):                 # (a) toutes les positions de depart
        j = 0
        while j < m and texte[i + j] == motif[j]:
            j += 1
        if ... :                          # (b) tout le motif a correspondu ?
            positions.append(i)
    return positions
```

??? corrige "Corrigé"

    `(a)` `range(n - m + 1)` ; `(b)` `if j == m:`.

### Boyer-Moore

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 3</span> — Les deux idées, et un grand saut <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-12-3 }

1.  Rappeler les **deux idées** de l’algorithme de Boyer-Moore.

2.  On considère le motif `CGGCAG`. Donner, pour chaque lettre du motif, sa **dernière position** (table du prétraitement de Boyer-Moore).

3.  On compare (de droite à gauche) et la lettre du texte qui provoque l’échec est un `T`. Sachant que `T` n’apparaît pas dans `CGGCAG`, de combien de crans peut-on décaler le motif d’un seul coup ? Justifier.

    ??? pouce "Coup de pouce"

        Si `T` n’apparaît nulle part dans le motif, un alignement où le motif recouvre ce `T` peut-il donner une occurrence ?

??? corrige "Corrigé"

    1.  **(1)** comparer le motif **de droite à gauche** ; **(2)** **prétraiter** le motif pour **sauter de plusieurs crans** en cas d’échec (règle du mauvais caractère).

    2.  `CGGCAG` : `C`$\to 3$, `G`$\to 5$, `A`$\to 4$ (dernières positions ; `C0 G1 G2 C3 A4 G5`).

    3.  `T` n’apparaît pas dans le motif : aucun alignement où `T` tomberait *dans* le motif ne peut réussir. On saute donc de **6 crans** (toute la longueur du motif) d’un seul coup.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 4</span> — Dérouler Boyer-Moore <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-12-4 }

On cherche le motif `GCAGC` dans le texte `ACGTGCAGCTGCAGC` (règle du mauvais caractère). La table des dernières positions est `G`$\to 3$, `C`$\to 4$… *(la compléter au besoin).*

<table>
<thead>
<tr>
<th style="text-align: center;"><strong>position <span class="math inline"><em>i</em></span></strong></th>
<th style="text-align: center;"><strong>fenêtre du texte</strong></th>
<th style="text-align: center;"><strong>échec / trouvé</strong></th>
<th style="text-align: center;"><strong>décalage</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><span class="math inline"><em>i</em> = 0</span></td>
<td style="text-align: center;"><code>ACGTG</code></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">… (compléter jusqu’à la fin du texte) …</td>
</tr>
</tbody>
</table>

Donner la (les) position(s) d’occurrence.

??? pouce "Coup de pouce"

    À chaque échec, repérer la lettre `c` du texte qui fait échouer et l’indice $j$ du motif où cela se produit, puis appliquer la règle du mauvais caractère du cours (décalage d’au moins $1$).

??? corrige "Corrigé"

    Table (dernières positions) de `GCAGC` : `G`$\to 3$, `C`$\to 4$, `A`$\to 2$.

    | **position $i$** | **fenêtre** |      **échec / trouvé**       | **décalage** |
    |:----------------:|:-----------:|:-----------------------------:|:------------:|
    |      $i=0$       |   `ACGTG`   | échec en $j=4$ (`G` du texte) |     $1$      |
    |      $i=1$       |   `CGTGC`   |     échec en $j=2$ (`T`)      |     $3$      |
    |      $i=4$       |   `GCAGC`   |          **trouvé**           |     $1$      |
    |      $i=5$       |   `CAGCT`   |     échec en $j=4$ (`T`)      |     $5$      |
    |      $i=10$      |   `GCAGC`   |          **trouvé**           |      —       |

    Occurrences aux positions **4** et **10**.

### Boyer-Moore-Horspool

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 5</span> — Construire la table de décalage <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-12-5 }

Pour un motif de longueur $m$, la table de Horspool donne à la lettre en position $k$ (sauf la dernière) le décalage $m-1-k$ ; toute autre lettre reçoit $m$.

Construire la table de décalage de chacun de ces motifs (préciser le décalage par défaut) :

1.  `ANANAS`

2.  `GATTACA`

3.  `ABRACADABRA`

    ??? pouce "Coup de pouce"

        Parcourir les lettres de gauche à droite en ignorant la dernière : quand une lettre revient, sa nouvelle valeur remplace l’ancienne.

??? corrige "Corrigé"

    1.  `ANANAS` ($m=6$) : `A`$\to 1$, `N`$\to 2$, défaut **6**. *(La dernière occurrence de `A` avant la fin est en position 4 $\to 1$ ; de `N` en position 3 $\to 2$.)*

    2.  `GATTACA` ($m=7$) : `G`$\to 6$, `A`$\to 2$, `T`$\to 3$, `C`$\to 1$, défaut **7**.

    3.  `ABRACADABRA` ($m=11$) : `A`$\to 3$, `B`$\to 2$, `R`$\to 1$, `C`$\to 6$, `D`$\to 4$, défaut **11**.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Dérouler Horspool <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-12-6 }

On cherche `ACGT` dans `GTACACGTAC`. Table : `A`$\to 3$, `C`$\to 2$, `G`$\to 1$, autres $\to 4$.

Recopier et compléter le tableau (**la lettre de fin** est celle du texte alignée avec la dernière case de la fenêtre) :

<table>
<thead>
<tr>
<th style="text-align: center;"><strong>position <span class="math inline"><em>i</em></span></strong></th>
<th style="text-align: center;"><strong>fenêtre</strong></th>
<th style="text-align: center;"><strong>lettre de fin</strong></th>
<th style="text-align: center;"><strong>décalage</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><span class="math inline"><em>i</em> = 0</span></td>
<td style="text-align: center;"><code>GTAC</code></td>
<td style="text-align: center;"><code>C</code></td>
<td style="text-align: center;">…</td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">…</td>
</tr>
</tbody>
</table>

Conclure : le motif est-il présent, et où ?

??? pouce "Coup de pouce"

    À chaque étape, la lettre de fin est celle du texte en position $i+3$ ; son décalage se lit dans la table.

??? corrige "Corrigé"

    | **position $i$** | **fenêtre** | **lettre de fin** | **décalage** |
    |:----------------:|:-----------:|:-----------------:|:------------:|
    |      $i=0$       |   `GTAC`    |        `C`        |     $2$      |
    |      $i=2$       |   `ACAC`    |        `C`        |     $2$      |
    |      $i=4$       |   `ACGT`    |   `T` (trouvé)    |      —       |

    Le motif `ACGT` est trouvé à la position **4**.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Horspool en Python <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-7 }

Recopier et compléter les deux fonctions :

??? pouce "Coup de pouce"

    Pour `(c)`, quelle méthode des dictionnaires renvoie une valeur par défaut quand la clé est absente ?

```python
def table_decalage(motif):
    m = len(motif)
    dec = {}
    for k in range(...):              # (a) toutes les lettres SAUF la derniere
        dec[motif[k]] = ...           # (b) le decalage
    return dec

def horspool(motif, texte):
    n, m = len(texte), len(motif)
    dec = table_decalage(motif)
    positions = []
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and texte[i + j] == motif[j]:
            j -= 1
        if j < 0:
            positions.append(i)
        c = texte[i + m - 1]
        i += ...                       # (c) le saut (m par defaut)
    return positions
```

??? corrige "Corrigé"

    `(a)` `range(m - 1)` ; `(b)` `dec[motif[k]] = m - 1 - k` ; `(c)` `i += dec.get(c, m)`.

### Coût

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Le miracle du sous-linéaire <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-8 }

1.  Combien coûte le **prétraitement** (construction de la table) en fonction de $m$ ?

2.  Expliquer pourquoi Horspool peut trouver un motif **sans lire tous les caractères** du texte.

    ??? pouce "Coup de pouce"

        Quand on saute de $m$ crans, quelles lettres du texte n’ont jamais été lues ?

3.  Vrai ou faux (justifier) : « plus le motif est long, plus la recherche est *lente* ».

4.  Boyer-Moore est-il *toujours* plus rapide que la méthode naïve ?

    ??? pouce "Coup de pouce"

        Penser au pire cas, par exemple chercher `AAA` dans `AAAAAAAA` : les sauts sont-ils grands ? combien de comparaisons par alignement ?

??? corrige "Corrigé"

    1.  Une seule passe sur le motif : **$O(m)$** (les lettres absentes du motif ne sont pas stockées dans la table).

    2.  À chaque échec, Horspool **saute** de plusieurs cases : les lettres survolées ne sont *jamais lues*. On peut donc conclure en bien moins de $n$ comparaisons.

    3.  **Faux** : c’est le contraire ! Plus le motif est long, plus les sauts possibles sont grands, donc plus la recherche est **rapide** (jusqu’à $\approx n/m$ comparaisons).

    4.  **Non** : au **pire cas**, Boyer-Moore reste en $O(n\times m)$, comme le naïf. C’est *en pratique*, sur des textes ordinaires, qu’il est spectaculairement plus rapide.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 9</span> — Exercice d’entraînement — Chercher un gène dans l’ADN <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-9 }

On modélise un brin d’ADN par une chaîne sur l’alphabet `{A, T, G, C}`, et on cherche le motif `GATTACA` par l’algorithme de Horspool.

1.  Construire la **table de décalage** de `GATTACA` (préciser le décalage par défaut).

2.  Dérouler Horspool sur le brin `GTAGATTACAGT` : donner la suite des positions $i$ testées, la lettre de fin de fenêtre, et le décalage à chaque étape. À quelle position trouve-t-on le motif ?

    ??? pouce "Coup de pouce"

        Le motif a $7$ lettres : la lettre de fin de la fenêtre $i$ est `brin[i + 6]`.

    ??? pouce "Coup de pouce 2 (début de solution)"

        Première étape : $i=0$, fenêtre `GTAGATT`, lettre de fin `T`, décalage $3$.

3.  On donne la fonction ci-dessous, qui **compte** le nombre d’occurrences. Compléter les lignes `(a)` et `(b)`.

    ??? pouce "Coup de pouce"

        Comparer avec la fonction `horspool` du cours : quelle condition signalait une occurrence ?

    ```python
    def compte_occurrences(motif, texte):
        dec = table_decalage(motif)
        n, m = len(texte), len(motif)
        nb = 0
        i = 0
        while i <= n - m:
            j = m - 1
            while j >= 0 and texte[i + j] == motif[j]:
                j -= 1
            if ... :                       # (a) motif entierement retrouve ?
                nb = nb + 1
            i += dec.get(texte[i + m - 1], ...)   # (b) valeur par defaut ?
        return nb
    ```

4.  Un génome humain compte environ $3$ milliards de bases. En quoi le choix de Horspool plutôt que la méthode naïve est-il crucial ici ?

??? corrige "Corrigé"

    1.  `GATTACA` : `G`$\to 6$, `A`$\to 2$, `T`$\to 3$, `C`$\to 1$, défaut **7**.

    2.  Sur `GTAGATTACAGT` :

        | $i$ |  fenêtre  |  lettre de fin   |       décalage       |
        |:---:|:---------:|:----------------:|:--------------------:|
        | $0$ | `GTAGATT` |       `T`        |         $3$          |
        | $3$ | `GATTACA` | `A` (**trouvé**) |         $2$          |
        | $5$ | `TTACAGT` |       `T`        | $3$ (dépasse la fin) |

        Le motif est trouvé à la position **3**.

    3.  `(a)` `if j < 0:` ; `(b)` `m` (le décalage par défaut).

    4.  Sur $3$ milliards de bases, un coût quadratique $O(n\times m)$ serait **prohibitif**. Horspool, souvent **sous-linéaire** (il saute une grande partie du brin sans la lire), rend la recherche réalisable en un temps raisonnable.

### Vers le bac

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 10</span> — Type bac — Parcourir une chaîne de caractères *(d’après Centres étrangers 2023, jour 2)* <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-10 }

On rappelle quelques notions sur la manipulation des chaînes de caractères en Python. Une chaîne de caractères se comporte comme un tableau de caractères que l’on ne peut pas modifier. Par exemple :

```text
>>> une_chaine = 'Bonjour'
>>> une_chaine[3]
'j'
>>> une_chaine[3] = 'z'
TypeError: 'str' object does not support item assignment
```

On peut aussi utiliser l’opérateur de concaténation `+` :

```text
>>> une_chaine = 'a' + 'b'
>>> une_chaine
'ab'
>>> une_chaine = une_chaine + 'c'
>>> une_chaine
'abc'
```

On définit la fonction `bonjour` par le code suivant :

```python
def bonjour(nom):
    return 'Bonjour ' + nom + ' !'
```

1.  Donner le résultat de l’exécution de `bonjour(’Alan’)`.

2.  On exécute le programme suivant :

    ```python
    une_chaine = 'Bonjour'
    x = (une_chaine[2] == une_chaine[3])
    y = (une_chaine[4] == une_chaine[1])
    ```

    Donner le type et les valeurs des variables `x` et `y`.

3.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire une fonction `occurrences_lettre(une_chaine, une_lettre)` prenant en paramètres une chaîne `une_chaine` et une lettre `une_lettre` et renvoyant le nombre d’occurrences de `une_lettre` dans `une_chaine`.

??? corrige "Corrigé"

    1.  `bonjour(’Alan’)` renvoie la chaîne `’Bonjour Alan !’` (concaténation de trois chaînes).

    2.  `une_chaine[2]` vaut `’n’` et `une_chaine[3]` vaut `’j’` : `x` vaut `False`. `une_chaine[4]` et `une_chaine[1]` valent tous deux `’o’` : `y` vaut `True`. Les deux variables sont de type **booléen** (`bool`).

    3.  On parcourt la chaîne caractère par caractère (c’est la méthode naïve pour un motif d’une seule lettre) :

        ```python
        def occurrences_lettre(une_chaine, une_lettre):
            nb = 0
            for c in une_chaine:
                if c == une_lettre:
                    nb = nb + 1
            return nb
        ```

        Par exemple `occurrences_lettre(’Bonjour’, ’o’)` renvoie `2`.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 11</span> — Type bac — Le principe de Boyer-Moore *(d’après Asie 2025, jour 1)* <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-11 }

Dans ce sujet, on veut repérer un mot-clé (par exemple `"while"`) dans le texte d’un programme Python. On suppose disposer d’une fonction `recherche(mot, texte)` qui renvoie `True` si la chaîne de caractères `mot` est présente dans la chaîne de caractères `texte`, et `False` sinon.

1.  Expliquer succinctement le principe de l’algorithme de Boyer-Moore, qui permet d’implémenter cette fonction `recherche`.

??? corrige "Corrigé"

    1.  On aligne le `mot` sous le début du `texte`, puis on compare les caractères **de droite à gauche**, en partant de la **fin** du mot. Si tous les caractères coïncident, le mot est trouvé (`True`). Sinon, on regarde le caractère du texte qui a provoqué la différence (règle du « mauvais caractère ») : grâce à une table calculée à l’avance à partir du mot seul (prétraitement), on **décale le mot vers la droite** de façon à aligner ce caractère avec sa dernière occurrence dans le mot, ou **au-delà de ce caractère** s’il n’apparaît pas dans le mot. On recommence jusqu’à trouver le mot ou dépasser la fin du texte (`False`). Ces sauts permettent de ne pas lire tous les caractères du texte : l’algorithme est en pratique bien plus rapide que la méthode naïve, surtout pour des mots longs.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 12</span> — Type bac — Rechercher et remplacer dans un éditeur *(sujet maison, façon bac)* <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-12 }

Un éditeur de texte propose deux commandes : **Rechercher**, qui surligne toutes les occurrences d’un motif, et **Remplacer tout**, qui remplace chaque occurrence d’un motif par un autre texte. On étudie leur programmation avec la méthode naïve. On rappelle la fonction du cours :

```python
def recherche_naive(motif, texte):
    n, m = len(texte), len(motif)
    positions = []
    for i in range(n - m + 1):
        j = 0
        while j < m and texte[i + j] == motif[j]:
            j += 1
        if j == m:
            positions.append(i)
    return positions
```

Dans les questions 1 à 3 et 6, la variable `texte` contient la chaîne `’LE CHAT ET LE CHATON’`.

1.  Donner la longueur $n$ de `texte`, puis la valeur renvoyée par chacun des appels suivants :

    `recherche_naive(’CHAT’, texte)` et `recherche_naive(’LE’, texte)`

2.  Combien de positions de départ `i` la boucle `for` examine-t-elle lors de la recherche du motif `’CHAT’` ?

3.  Pour mesurer le coût, on compte les **comparaisons de caractères**, c’est-à-dire le nombre d’évaluations de `texte[i + j] == motif[j]`. Expliquer pourquoi, lors de la recherche de `’CHAT’`, toutes les positions de départ sauf deux ne coûtent qu’une seule comparaison. En déduire le nombre total de comparaisons.

4.  Donner un motif de longueur $4$ et un texte de longueur $12$, écrits avec les lettres `A` et `B`, pour lesquels la méthode naïve effectue le plus grand nombre possible de comparaisons. Combien en effectue-t-elle ? Exprimer ce nombre en fonction de $n$ et $m$.

    ??? pouce "Coup de pouce"

        Pour que chaque position de départ coûte $m$ comparaisons, le motif doit « presque » correspondre partout : quel texte et quel motif choisir avec seulement deux lettres ?

5.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire une fonction `est_occurrence(motif, texte, i)` qui renvoie `True` si `motif` apparaît dans `texte` à partir de la position `i`, et `False` sinon. On suppose que `i + len(motif) <= len(texte)`.

    ??? pouce "Coup de pouce 2 (début de solution)"

        `def est_occurrence(motif, texte, i):`  
        `for j in range(len(motif)):`  
        `if texte[i + j] != motif[j]:`

6.  <span class="run" title="À programmer et tester sur machine">▶</span> Pour la commande **Remplacer tout**, on parcourt le texte de gauche à droite en construisant une nouvelle chaîne. Recopier et compléter les lignes `(a)` à `(d)`, puis donner la valeur renvoyée par `remplacer_tout(’CHAT’, ’LOUP’, texte)`.

    ??? pouce "Coup de pouce"

        Deux cas : une occurrence commence en `i`, ou non. Dans chaque cas, que faut-il ajouter à `resultat`, et de combien faut-il avancer ?

    ```python
    def remplacer_tout(motif, nouveau, texte):
        n, m = len(texte), len(motif)
        resultat = ''
        i = 0
        while i < n:
            if i <= n - m and est_occurrence(motif, texte, i):
                resultat = ...           # (a)
                i = ...                  # (b)
            else:
                resultat = ...           # (c)
                i = ...                  # (d)
        return resultat
    ```

7.  L’appel `recherche_naive(’AA’, ’AAA’)` renvoie `[0, 1]`, alors que `remplacer_tout(’AA’, ’B’, ’AAA’)` renvoie `’BA’`. Expliquer cette différence, et pourquoi c’est bien le comportement attendu d’un éditeur.

8.  Un fichier contient un million de caractères et l’on cherche un motif de $10$ caractères. Donner l’ordre de grandeur du nombre de comparaisons de la méthode naïve dans le pire des cas. Citer un algorithme du cours plus efficace en pratique, et l’idée qui le rend plus rapide.

??? corrige "Corrigé"

    1.  $n = 20$ (les espaces comptent). `recherche_naive(’CHAT’, texte)` renvoie `[3, 14]` et `recherche_naive(’LE’, texte)` renvoie `[0, 11]`.

    2.  La boucle examine les positions $0$ à $n - m = 16$, soit $n - m + 1 = \textbf{17}$ positions.

    3.  La première comparaison porte sur `motif[0]`, c’est-à-dire `C`. Or le texte ne contient la lettre `C` qu’aux positions $3$ et $14$ : partout ailleurs, la première comparaison échoue et la boucle `while` s’arrête aussitôt (1 comparaison). Aux positions $3$ et $14$, les quatre lettres correspondent (4 comparaisons). Total : $15 \times 1 + 2 \times 4 = \textbf{23}$ comparaisons.

    4.  Par exemple le motif `’AAAB’` dans le texte `’AAAAAAAAAAAA’` (douze `A`) : à chacune des $12 - 4 + 1 = 9$ positions, les trois `A` correspondent et l’échec n’a lieu que sur la dernière lettre, soit $4$ comparaisons. Total : $9 \times 4 = \textbf{36}$ comparaisons, c’est-à-dire $(n - m + 1) \times m$ : le maximum possible, puisqu’on ne fait jamais plus de $m$ comparaisons par position. *(Le motif `’AAAA’` convient aussi.)*

    5.  On compare lettre à lettre, comme dans la méthode naïve :

        ```python
        def est_occurrence(motif, texte, i):
            for j in range(len(motif)):
                if texte[i + j] != motif[j]:
                    return False
            return True
        ```

    6.  `(a)` `resultat = resultat + nouveau` ; `(b)` `i = i + m` (on saute toute l’occurrence) ; `(c)` `resultat = resultat + texte[i]` ; `(d)` `i = i + 1`.

        `remplacer_tout(’CHAT’, ’LOUP’, texte)` renvoie `’LE LOUP ET LE LOUPON’` (le `CHAT` de `CHATON` est remplacé lui aussi).

    7.  `recherche_naive` teste *toutes* les positions, y compris celles qui chevauchent une occurrence déjà trouvée : `AA` est présent en $0$ et en $1$. `remplacer_tout`, après une occurrence, saute les $m$ caractères remplacés (ligne `(b)`) : l’occurrence en $0$ donne `B`, puis on reprend en position $2$, où il ne reste que `A`, recopié tel quel. C’est le comportement attendu : un même caractère du texte ne peut pas être remplacé deux fois.

    8.  Au pire $(n - m + 1) \times m \approx 10^6 \times 10 = 10^7$ comparaisons. L’algorithme de **Boyer-Moore** (ou sa version simplifiée, **Horspool**) est bien plus rapide en pratique : il compare le motif de droite à gauche et, grâce à une table calculée à l’avance à partir du motif, **saute** plusieurs positions d’un coup en cas d’échec, sans lire les caractères survolés.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 13</span> — Type bac — Un antivirus à la recherche de signatures *(sujet maison, façon bac)* <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-13 }

Un antivirus repère un logiciel malveillant connu en cherchant sa **signature** — une courte suite d’octets qui le caractérise — dans le contenu des fichiers. Pour simplifier, le contenu d’un fichier et les signatures sont représentés par des chaînes de caractères écrites avec les chiffres hexadécimaux `0` à `9` et `A` à `F`, et l’on ne se préoccupe pas du découpage en octets.

L’antivirus utilise l’algorithme de **Boyer-Moore-Horspool**. On dispose des fonctions `table_decalage(motif)` et `horspool(motif, texte)` du cours ; `horspool` renvoie la liste des positions des occurrences de `motif` dans `texte`.

1.  Rappeler comment est construite la table de décalage d’un motif de longueur $m$. Construire la table de décalage de la signature `’4D5A90’` (préciser le décalage par défaut).

2.  Construire la table de décalage de la signature `’E8FFFF’`. La lettre `F` est la dernière lettre du motif : pourquoi figure-t-elle pourtant dans la table, et avec quel décalage ?

    ??? pouce "Coup de pouce"

        Seule la *dernière position* du motif est ignorée : la lettre `F` apparaît-elle aussi ailleurs dans `E8FFFF` ?

3.  Le contenu d’un fichier, de $22$ caractères, est :

    `contenu = ’00E84D5A0090FF4D5A90C3’`

    Dérouler `horspool(’4D5A90’, contenu)` en recopiant et complétant le tableau ci-dessous. Quelle valeur la fonction renvoie-t-elle ?

    <table>
    <thead>
    <tr>
    <th style="text-align: center;"><strong>position <span class="math inline"><em>i</em></span></strong></th>
    <th style="text-align: center;"><strong>fenêtre</strong></th>
    <th style="text-align: center;"><strong>lettre de fin</strong></th>
    <th style="text-align: center;"><strong>décalage</strong></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: center;"><span class="math inline"><em>i</em> = 0</span></td>
    <td style="text-align: center;"><code>00E84D</code></td>
    <td style="text-align: center;">…</td>
    <td style="text-align: center;">…</td>
    </tr>
    <tr>
    <td colspan="4" style="text-align: left;">…</td>
    </tr>
    </tbody>
    </table>

4.  Combien d’alignements Horspool a-t-il testés ? Combien la méthode naïve en aurait-elle testés ? Combien de comparaisons de caractères Horspool a-t-il effectuées au total ?

5.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire une fonction `est_infecte(contenu, signatures)` qui prend en paramètres le contenu d’un fichier et une liste de signatures, et renvoie `True` si au moins une des signatures apparaît dans le contenu, `False` sinon. On utilisera la fonction `horspool`.

    ??? pouce "Coup de pouce"

        Parcourir la liste des signatures : que renvoie `horspool` quand la signature est absente ? Peut-on conclure dès la première trouvée ?

6.  L’antivirus analyse $100\,000$ fichiers avec la même liste de $1\,000$ signatures. Combien de fois la table de décalage de chaque signature est-elle construite avec la fonction `est_infecte` ? Proposer, sans écrire tout le code, une organisation qui évite ce travail inutile.

7.  L’éditeur de l’antivirus affirme : « plus nos signatures sont longues, plus l’analyse est rapide ». Cette affirmation est-elle plausible ? Justifier.

??? corrige "Corrigé"

    1.  On parcourt les lettres du motif **sauf la dernière** : la lettre en position $k$ reçoit le décalage $m - 1 - k$ (si une lettre apparaît plusieurs fois, c’est sa dernière position qui l’emporte) ; toute autre lettre reçoit le décalage par défaut $m$.

        `’4D5A90’` ($m = 6$) : `4`$\to 5$, `D`$\to 4$, `5`$\to 3$, `A`$\to 2$, `9`$\to 1$, défaut **6**.

    2.  `’E8FFFF’` ($m = 6$) : `E`$\to 5$, `8`$\to 4$, `F`$\to 1$, défaut **6**. On n’exclut que la *dernière case* du motif, pas la lettre `F` elle-même : `F` apparaît aussi aux positions $2$, $3$ et $4$, et c’est la position $4$ (la plus à droite hors dernière case) qui donne le décalage $6 - 1 - 4 = 1$.

    3.  Déroulé de Horspool :

        | **position $i$** | **fenêtre** |   **lettre de fin**    |     **décalage**     |
        |:----------------:|:-----------:|:----------------------:|:--------------------:|
        |      $i=0$       |  `00E84D`   |          `D`           |         $4$          |
        |      $i=4$       |  `4D5A00`   | `0` (échec en $j = 4$) |         $6$          |
        |      $i=10$      |  `90FF4D`   |          `D`           |         $4$          |
        |      $i=14$      |  `4D5A90`   |    `0` (**trouvé**)    | $6$ (dépasse la fin) |

        La fonction renvoie `[14]`.

    4.  Horspool a testé **4** alignements, contre $22 - 6 + 1 = \textbf{17}$ pour la méthode naïve. Comparaisons : $1$ (en $i=0$) $+ 2$ (en $i=4$ : `0` correspond, puis `0` $\neq$ `9`) $+ 1$ (en $i=10$) $+ 6$ (en $i=14$) $= \textbf{10}$ comparaisons. *(La méthode naïve en effectue $26$.)*

    5.  On essaie les signatures une à une :

        ```python
        def est_infecte(contenu, signatures):
            for s in signatures:
                if len(horspool(s, contenu)) > 0:
                    return True
            return False
        ```

        Par exemple, avec le contenu de la question 3 :

        `est_infecte(contenu, [’E8FFFF’, ’4D5A90’])` renvoie `True` ;

        `est_infecte(contenu, [’E8FFFF’])` renvoie `False`.

    6.  Chaque appel à `horspool` reconstruit la table : la table d’une signature est donc construite jusqu’à **$100\,000$ fois** (une fois par fichier analysé), alors qu’elle ne dépend que de la signature. Il suffit de construire **une seule fois**, avant l’analyse, un dictionnaire qui associe à chaque signature sa table de décalage ($1\,000$ constructions en tout), puis d’utiliser une version de `horspool` qui reçoit la table en paramètre au lieu de la recalculer. On dépense un peu de mémoire pour gagner du temps.

    7.  **Oui**, c’est plausible : la table d’une signature longue autorise des décalages plus grands (jusqu’à $m$ quand la lettre de fin de fenêtre est absente du motif). En pratique, Horspool teste de l’ordre de $n / m$ alignements : plus $m$ est grand, moins il y a d’alignements, et la recherche est plus rapide (au pire des cas, le coût reste toutefois en $O(n \times m)$).

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 14</span> — Type bac — Repérer des amorces dans un brin d’ADN *(sujet maison, façon bac)* <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-14 }

En biologie moléculaire, une **amorce** est une courte séquence d’ADN qui ne peut se fixer sur un brin qu’à l’endroit où elle apparaît telle quelle. Avant une expérience, un laboratoire vérifie par programme où ses amorces apparaissent dans un brin. Un brin et une amorce sont représentés par des chaînes de caractères sur l’alphabet `{A, C, G, T}`. Dans tout l’exercice, `brin = ’CATGGATGCATGCC’` ($14$ caractères) et l’on cherche l’amorce `’TGCATG’`.

**Partie A — Boyer-Moore (règle du mauvais caractère)**

On donne les fonctions suivantes :

```python
def table_dernier(motif):
    last = {}
    for k in range(len(motif)):
        last[motif[k]] = k
    return last

def boyer_moore(motif, texte):
    n, m = len(texte), len(motif)
    last = table_dernier(motif)
    positions = []
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and texte[i + j] == motif[j]:
            j -= 1
        if j < 0:
            positions.append(i)
            i += 1
        else:
            c = texte[i + j]
            i += max(1, j - last.get(c, -1))
    return positions
```

1.  Donner le dictionnaire renvoyé par `table_dernier(’TGCATG’)`.

2.  Dérouler `boyer_moore(’TGCATG’, brin)` : pour chaque position $i$ testée, donner la fenêtre du brin, l’indice $j$ et le caractère `c` qui provoquent l’échec (ou « trouvé »), et le décalage appliqué. Quelle valeur la fonction renvoie-t-elle ?

    ??? pouce "Coup de pouce"

        Commencer à $i=0$ : comparer `brin[5]` et `motif[5]`, puis reculer tant que les lettres coïncident ; le décalage vient de la ligne `i += max(1, ...)`.

3.  Lors de ce déroulé, la quantité `j - last.get(c, -1)` a été négative. À quelle position $i$ ? Que se passerait-il si l’on remplaçait `max(1, j - last.get(c, -1))` par `j - last.get(c, -1)` ?

    ??? pouce "Coup de pouce"

        Chercher l’étape où la dernière occurrence de `c` dans le motif est *à droite* de l’indice $j$.

**Partie B — Boyer-Moore-Horspool**

1.  Construire la table de décalage de Horspool de l’amorce `’TGCATG’` (préciser le décalage par défaut).

2.  Dérouler l’algorithme de Horspool sur le même brin (position $i$, fenêtre, lettre de fin de fenêtre, décalage). Comparer le nombre d’alignements testés par les deux algorithmes sur cet exemple.

**Partie C — Programmer**

1.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire une fonction `cherche_amorces(amorces, brin)` qui prend une liste d’amorces et un brin, et renvoie un **dictionnaire** associant à chaque amorce la liste de ses positions dans le brin (on utilisera la fonction `horspool` du cours). Par exemple, `cherche_amorces([’TGCATG’, ’GGA’, ’AAAA’], brin)` renvoie `{’TGCATG’: [6], ’GGA’: [3], ’AAAA’: []}`.

    ??? pouce "Coup de pouce 2 (début de solution)"

        `def cherche_amorces(amorces, brin):`  
        `resultat = {}`  
        `for amorce in amorces:`

2.  <span class="run" title="À programmer et tester sur machine">▶</span> En utilisant `cherche_amorces`, écrire une fonction `amorces_absentes(amorces, brin)` qui renvoie la liste des amorces qui n’apparaissent pas dans le brin.

3.  Un génome humain compte environ $3$ milliards de bases et une amorce environ $20$ bases. Donner l’ordre de grandeur du nombre d’alignements testés par la méthode naïve, puis par Horspool dans un cas favorable où chaque saut vaut la longueur de l’amorce.

??? corrige "Corrigé"

    **Partie A**

    1.  `TGCATG` = `T0 G1 C2 A3 T4 G5` : `table_dernier` renvoie `{’T’: 4, ’G’: 5, ’C’: 2, ’A’: 3}`.

    2.  Déroulé (le brin est `C0 A1 T2 G3 G4 A5 T6 G7 C8 A9 T10 G11 C12 C13`) :

        | **position $i$** | **fenêtre** |   **échec / trouvé**    |     **décalage**     |
        |:----------------:|:-----------:|:-----------------------:|:--------------------:|
        |      $i=0$       |  `CATGGA`   | échec en $j=5$, `c = A` |  $\max(1, 5-3) = 2$  |
        |      $i=2$       |  `TGGATG`   | échec en $j=2$, `c = G` |  $\max(1, 2-5) = 1$  |
        |      $i=3$       |  `GGATGC`   | échec en $j=5$, `c = C` |  $\max(1, 5-2) = 3$  |
        |      $i=6$       |  `TGCATG`   |       **trouvé**        |         $1$          |
        |      $i=7$       |  `GCATGC`   | échec en $j=5$, `c = C` | $3$ (dépasse la fin) |

        La fonction renvoie `[6]` (5 alignements testés).

    3.  En $i = 2$ : le caractère fautif `G` a sa dernière position ($5$) **à droite** de l’échec ($j = 2$), donc `j - last[’G’]` $= -3$. Sans le `max(1, ...)`, on ajouterait $-3$ à $i$ : le motif **reculerait** en $i = -1$. Sur cet exemple, $i$ prend ensuite les valeurs $-2$, $-3$, $-2$, $-3$… (en Python, un indice négatif lit le texte depuis la fin) : le programme **boucle sans fin**. Le `max` garantit qu’on avance toujours d’au moins un cran, donc que l’algorithme termine.

    **Partie B**

    1.  Lettres sauf la dernière (`T0 G1 C2 A3 T4`) : `T`$\to 1$, `G`$\to 4$, `C`$\to 3$, `A`$\to 2$, défaut **6**.

    2.  Déroulé de Horspool :

        | **position $i$** | **fenêtre** |  **lettre de fin**   |     **décalage**     |
        |:----------------:|:-----------:|:--------------------:|:--------------------:|
        |      $i=0$       |  `CATGGA`   |         `A`          |         $2$          |
        |      $i=2$       |  `TGGATG`   | `G` (échec en $j=2$) |         $4$          |
        |      $i=6$       |  `TGCATG`   |   `G` (**trouvé**)   | $4$ (dépasse la fin) |

        Horspool trouve l’amorce en position $6$ avec **3** alignements, contre **5** pour Boyer-Moore (règle du mauvais caractère seule). En $i = 2$, Boyer-Moore ne peut avancer que d’un cran (question 3), alors que Horspool, qui regarde toujours la lettre de fin de fenêtre, saute de $4$. Ce n’est pas une règle générale : les deux algorithmes sont aussi rapides en pratique.

    **Partie C**

    1.  On range la liste des positions de chaque amorce dans le dictionnaire :

        ```python
        def cherche_amorces(amorces, brin):
            resultat = {}
            for a in amorces:
                resultat[a] = horspool(a, brin)
            return resultat
        ```

    2.  On réutilise le dictionnaire renvoyé par `cherche_amorces`, et on construit par compréhension la liste des amorces qui n’ont aucune occurrence :

        ```python
        def amorces_absentes(amorces, brin):
            occurrences = cherche_amorces(amorces, brin)
            return [a for a in amorces if len(occurrences[a]) == 0]
        ```

        `amorces_absentes([’TGCATG’, ’GGA’, ’AAAA’], brin)` renvoie `[’AAAA’]`.

        *Autre méthode :* une boucle qui ajoute à la liste chaque amorce absente.

        ```python
        def amorces_absentes(amorces, brin):
            absentes = []
            occurrences = cherche_amorces(amorces, brin)
            for a in amorces:
                if len(occurrences[a]) == 0:
                    absentes.append(a)
            return absentes
        ```

    3.  Méthode naïve : $n - m + 1 \approx 3 \times 10^9$ alignements (3 milliards). Horspool, si chaque saut vaut $m = 20$ : environ $n / m = 3 \times 10^9 / 20 = 1{,}5 \times 10^8$ alignements (150 millions), soit vingt fois moins.

### Critiquer une réponse d’IA

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 15</span> — Une table de décalage construite par un assistant d’IA <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> { #ex-12-15 }

Un élève demande à un assistant d’IA : « Écris en Python la fonction `table_decalage(motif)` de l’algorithme de Horspool, puis la fonction `horspool(motif, texte)` qui renvoie la position de la première occurrence (ou `-1`). » Voici la réponse obtenue :

```python
def table_decalage(motif):
    m = len(motif)
    dec = {}
    for k in range(m):               # chaque lettre du motif
        dec[motif[k]] = m - 1 - k    # distance a la fin du motif
    return dec

def horspool(motif, texte):
    n, m = len(texte), len(motif)
    dec = table_decalage(motif)
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and texte[i + j] == motif[j]:
            j -= 1                   # comparaison droite -> gauche
        if j < 0:
            return i                 # motif trouve en i
        i += dec.get(texte[i + m - 1], m)   # saut selon la derniere case
    return -1
```

*« La table donne, pour chaque lettre du motif, sa distance à la fin ; une lettre absente vaut `m`. La recherche compare de droite à gauche et saute selon la lettre alignée avec la fin de la fenêtre. »*

1.  La réponse est-elle correcte ? Construire la table pour `ANANAS`, puis dérouler `horspool("ANANAS", "ANANES ANANAS")` : noter $i$, la lettre de fin de fenêtre et le décalage à chaque étape.

2.  Localiser et corriger l’erreur.

    ??? pouce "Coup de pouce"

        Comparer la boucle de `table_decalage` avec celle du cours : quelles lettres sont parcourues ? Quelle valeur reçoit alors la dernière lettre ?

3.  Quelle vérification simple, faite avant de faire confiance à la réponse, aurait suffi à détecter l’erreur ?

??? corrige "Corrigé"

    1.  **Non.** La table obtenue est `{’A’: 1, ’N’: 2, ’S’: 0}` : la dernière lettre `S` reçoit le décalage $0$. Déroulé : $i = 0$, fenêtre `ANANES`, comparaison de droite à gauche : `S = S`, puis `E `$\neq$` A` ; la lettre de fin de fenêtre est `S`, décalage `dec[’S’] = 0`, donc $i$ reste à $0$… et la même fenêtre est examinée indéfiniment : le programme **boucle sans fin** (sortie réelle : aucune, il faut l’interrompre).

    2.  L’erreur : la **dernière lettre** du motif ne doit *pas* figurer dans la table (cours : « *on parcourt ses lettres sauf la dernière* »), sinon son décalage vaut $0$. Ligne corrigée :

        ```python
            for k in range(m - 1):           # on ignore la DERNIERE lettre
        ```

        La table devient `{’A’: 1, ’N’: 2}` (`S` absent, donc décalage $6$). Déroulé corrigé : $i = 0$ (fin de fenêtre `S` $\to$ saut $6$), $i = 6$ (fenêtre « espace + `ANANA` », fin `A` $\to$ saut $1$), $i = 7$ : `ANANAS` trouvé. La fonction renvoie `7`.

    3.  Regarder la table produite : un décalage de **$0$** est **toujours** une erreur (on n’avancerait jamais). Plus généralement, vérifier qu’un algorithme de recherche termine sur un texte où le motif est *absent* ou précédé d’une fausse piste.

### S’entraîner à l’oral

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 16</span> — Expliquer en deux minutes <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-12-16 }

Au Grand Oral comme devant l’examinateur de l’épreuve pratique, il faut savoir **expliquer** une notion clairement, sans notes. Choisir l’un des sujets suivants (ou le tirer au sort) :

1.  Expliquer à un camarade de Première la recherche **naïve** d’un motif dans un texte et son coût.

2.  Expliquer l’idée de **Boyer-Moore-Horspool** : pourquoi comparer en partant de la fin du motif permet de sauter des positions.

3.  Expliquer pourquoi Boyer-Moore-Horspool est d’autant plus rapide que le motif est long, et dans quel cas il ne gagne rien.

**Préparation (5 min, seul).** Noter au brouillon **trois idées** et **un exemple**, rien de plus, puis retourner la feuille. **Exposé (2 min, chronométré).** Debout, face à un camarade, **sans lire de notes** : tout passe par la parole. **Retour (2 min).** Le camarade pose une question de relance (on peut alors s’aider d’un schéma), remplit la grille ci-dessous et donne un conseil ; puis on échange les rôles. Cette grille reprend les critères d’évaluation du Grand Oral.

??? pouce "Coup de pouce"

    Structurer chaque explication en trois temps : une **définition** en une phrase, un **exemple** petit et concret déroulé à voix haute, puis le **piège** (l’erreur que l’auditeur risque de faire). Finir par une phrase qui répond à la question posée. Prévoir un motif court (quatre lettres) et un texte d’une ligne, que l’on fait « glisser » à voix haute. Sujet 2 : quel caractère du texte regarde-t-on pour décider du saut ?

<table>
<thead>
<tr>
<th style="text-align: left;"><strong>Grille entre camarades</strong></th>
<th style="text-align: center;"><strong>Oui</strong></th>
<th style="text-align: center;"><strong>En partie</strong></th>
<th style="text-align: center;"><strong>Pas encore</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>Clair</strong> — audible, posé ; chaque mot technique est expliqué</td>
<td style="text-align: center;"><span class="math inline">▫</span></td>
<td style="text-align: center;"><span class="math inline">▫</span></td>
<td style="text-align: center;"><span class="math inline">▫</span></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Juste</strong> — c’est exact, et l’exemple montre vraiment l’idée</td>
<td style="text-align: center;"><span class="math inline">▫</span></td>
<td style="text-align: center;"><span class="math inline">▫</span></td>
<td style="text-align: center;"><span class="math inline">▫</span></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Construit</strong> — un fil conducteur, tenu en deux minutes, sans lire</td>
<td style="text-align: center;"><span class="math inline">▫</span></td>
<td style="text-align: center;"><span class="math inline">▫</span></td>
<td style="text-align: center;"><span class="math inline">▫</span></td>
</tr>
<tr>
<td colspan="4" style="text-align: left;"><strong>Un conseil</strong> pour la prochaine fois :</td>
</tr>
</tbody>
</table>

??? corrige "Corrigé"

    Pas de texte à apprendre par cœur : voici les **éléments attendus** pour chaque sujet. L’ordre, les mots et l’exemple peuvent être différents ; l’explication est réussie si ces idées y sont, justes et reliées entre elles.

    **Sujet 1.**

    - On place le motif (de longueur $m$) à chaque position du texte (de longueur $n$) et on compare caractère par caractère : une **fenêtre glissante** qui avance d’un cran.

    - Exemple : chercher `NSI` dans `LES NSI` : positions $0, 1, 2, 3$ échouent dès la première lettre, la position $4$ réussit.

    - Coût dans le pire cas : de l’ordre de $n \times m$ comparaisons (texte `AAAA…A`, motif `AAB`).

    - Piège : les bornes ; la dernière position possible est $n - m$.

    **Sujet 2.**

    - On compare le motif au texte en partant de la **fin** du motif.

    - Une **table de décalage** est préparée à l’avance : pour chaque caractère du motif (sauf le dernier), la distance entre sa dernière apparition et la fin du motif ; pour un caractère absent, la longueur du motif.

    - En cas d’échec, on décale selon le caractère du texte aligné avec la fin du motif ; s’il n’apparaît pas dans le motif, on saute de $m$ positions d’un coup.

    - Exemple : motif `CHAT` : décalages `C` $\to 3$, `H` $\to 2$, `A` $\to 1$, tout autre caractère $\to 4$.

    **Sujet 3.**

    - Chaque saut de $m$ positions évite de lire des caractères du texte : on en lit souvent bien moins que $n$ (coût **sous-linéaire**, de l’ordre de $n/m$ dans le meilleur cas).

    - Exemple : un motif de dix lettres rares dans un texte en français avance le plus souvent de dix positions à la fois.

    - Pire cas : petit alphabet et nombreuses répétitions (ADN, `AAAA…`) ; les décalages valent $1$, et l’on retrouve le coût de la méthode naïve.

    - On paie un peu de mémoire (la table) pour gagner beaucoup de temps ; usages : « Rechercher » d’un éditeur, antivirus, bio-informatique.
