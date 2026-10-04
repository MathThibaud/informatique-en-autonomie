# Exercices

<p class="sous-titre">Structures linéaires : piles, files, listes chaînées</p>

!!! consignes "Mode d’emploi"

    - Niveau : ★ échauffement, ★★ classique (niveau bac), ★★★ défi ; les *coups de pouce* et les *corrigés* se déplient sous chaque exercice.

    - <span class="run" title="À programmer et tester sur machine">▶</span> *À programmer et tester* en Python (console ou éditeur en ligne).

    - **Réflexe** : on **utilise** une structure par son **interface** (`empiler`, `depiler`, `enfiler`, `defiler`, `est_vide`…) et l’on **admet** qu’une classe l’implémente. On écrit `p = Pile()` ou `f = File()` sans la reprogrammer.

    - **Convention** de cette feuille : pile dessinée **verticalement** (sommet en haut), file dessinée **horizontalement** avec la **tête à droite** (on enfile à gauche, on défile à droite).

    - Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la [charte d’usage de l’IA](../charte.md).

### Comprendre l’interface

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — LIFO ou FIFO ? <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-03-1 }

Pour chaque situation, indiquer si la structure adaptée est une **pile** (LIFO) ou une **file** (FIFO), et justifier en une courte phrase.

1.  la fonction « Annuler » (`Ctrl+Z`) d’un traitement de texte ;

2.  les documents en attente sur une imprimante partagée ;

3.  les appels de fonctions récursives gérés par la machine ;

4.  les caractères tapés au clavier en attente d’être traités ;

5.  le bouton « page précédente » d’un navigateur.

??? corrige "Corrigé"

    1.  **Pile** (LIFO) : « annuler » retire la *dernière* action effectuée.

    2.  **File** (FIFO) : les documents s’impriment dans l’*ordre d’arrivée*.

    3.  **Pile** (LIFO) : la dernière fonction appelée est la première dont on revient (pile d’appels).

    4.  **File** (FIFO) : les caractères sont traités dans l’ordre où ils ont été tapés.

    5.  **Pile** (LIFO) : « précédent » revient à la *dernière* page visitée.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 2</span> — La bonne opération <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-03-2 }

On dispose d’une pile `p` et d’une file `f`. Pour chaque phrase, écrire l’**appel de méthode** correspondant.

1.  ajouter la valeur `7` au sommet de la pile `p` ;

2.  retirer et récupérer l’élément de tête de la file `f` ;

3.  savoir si la pile `p` est vide ;

4.  ajouter la valeur `7` à la queue de la file `f` ;

5.  consulter le sommet de `p` *sans* le retirer.

??? corrige "Corrigé"

    **1.** `p.empiler(7)` **2.** `f.defiler()` **3.** `p.est_vide()` **4.** `f.enfiler(7)` **5.** `p.sommet()`

### Tracer une pile, tracer une file

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 3</span> — Trace d’une pile <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-03-3 }

On part d’une pile `p` vide. Donner, pour chaque appel qui renvoie une valeur, la **valeur renvoyée**, puis représenter le **contenu final** de la pile (sommet en haut).

```text
p.empiler(4)
p.empiler(7)
p.empiler(2)
p.depiler()
p.empiler(9)
p.sommet()
p.depiler()
```

??? corrige "Corrigé"

    Valeurs renvoyées : `p.depiler()` $\to$ `2` ; `p.sommet()` $\to$ `9` ; `p.depiler()` $\to$ `9`.

    Contenu final (sommet en haut) : `7` au sommet, `4` en dessous. Détail :

    | **Instruction** | **Renvoie** | **Pile écrite en ligne (sommet à droite)** |
    |:----------------|:-----------:|:-------------------------------------------|
    | `empiler(4)`    |      —      | $4$                                        |
    | `empiler(7)`    |      —      | $4\ ;\ 7$                                  |
    | `empiler(2)`    |      —      | $4\ ;\ 7\ ;\ 2$                            |
    | `depiler()`     |     `2`     | $4\ ;\ 7$                                  |
    | `empiler(9)`    |      —      | $4\ ;\ 7\ ;\ 9$                            |
    | `sommet()`      |     `9`     | $4\ ;\ 7\ ;\ 9$                            |
    | `depiler()`     |     `9`     | $4\ ;\ 7$                                  |

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 4</span> — Trace d’une file <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-03-4 }

On part d’une file `f` vide. Même travail (la **tête est à droite** : on défile à droite).

```text
f.enfiler(4)
f.enfiler(7)
f.enfiler(2)
f.defiler()
f.enfiler(9)
f.tete()
f.defiler()
```

??? corrige "Corrigé"

    Valeurs renvoyées : `f.defiler()` $\to$ `4` ; `f.tete()` $\to$ `7` ; `f.defiler()` $\to$ `7`.

    Contenu final (tête à droite) : $9\ ;\ 2$, soit `2` en tête. Détail :

    | **Instruction** | **Renvoie** | **File (tête à droite)** |
    |:----------------|:-----------:|:-------------------------|
    | `enfiler(4)`    |      —      | $4$                      |
    | `enfiler(7)`    |      —      | $7\ ;\ 4$                |
    | `enfiler(2)`    |      —      | $2\ ;\ 7\ ;\ 4$          |
    | `defiler()`     |     `4`     | $2\ ;\ 7$                |
    | `enfiler(9)`    |      —      | $9\ ;\ 2\ ;\ 7$          |
    | `tete()`        |     `7`     | $9\ ;\ 2\ ;\ 7$          |
    | `defiler()`     |     `7`     | $9\ ;\ 2$                |

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 5</span> — Même séquence, deux structures <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-03-5 }

On applique la *même* suite d’ajouts `1, 2, 3, 4` à une pile et à une file, puis on retire **tous** les éléments un par un.

1.  Dans quel ordre les valeurs sortent-elles de la **pile** ?

2.  Dans quel ordre sortent-elles de la **file** ?

3.  Quelle structure *inverse* l’ordre des éléments ? Quelle structure le *conserve* ?

??? corrige "Corrigé"

    **1.** De la pile : `4, 3, 2, 1` (le dernier entré sort en premier). **2.** De la file : `1, 2, 3, 4` (le premier entré sort en premier). **3.** La **pile** inverse l’ordre ; la **file** le conserve.

### L’exemple phare : le parenthésage

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Parenthésage à la main <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-03-6 }

On reprend l’algorithme du cours : on **empile** chaque symbole ouvrant, et à chaque symbole fermant on **dépile** en vérifiant la correspondance. Pour chacune des expressions suivantes, dérouler l’algorithme (contenu de la pile étape par étape) et conclure : **correcte** ou **incorrecte** (et pourquoi).

??? pouce "Coup de pouce"

    À la lecture d’un symbole fermant, deux situations font échouer : lesquelles ? Et que doit contenir la pile une fois toute l’expression lue ?

1.  `{[()]}`

2.  `(]`

3.  `([]`

4.  `())(`

??? corrige "Corrigé"

    1.  `{[()]}` : on empile `{`, `[`, `(` ; `)` dépile `(` (ok), `]` dépile `[` (ok), `}` dépile `{` (ok). Pile vide en fin $\Rightarrow$ **correcte**.

    2.  `(]` : on empile `(` ; `]` dépile `(`, or `]` attend `[` $\Rightarrow$ mauvais appariement $\Rightarrow$ **incorrecte**.

    3.  `([]` : on empile `(`, `[` ; `]` dépile `[` (ok). En fin, la pile n’est **pas vide** (il reste `(`) $\Rightarrow$ **incorrecte** (une ouvrante jamais refermée).

    4.  `())(` : on empile `(` ; `)` dépile `(` (ok, pile vide) ; `)` suivante : la pile est **vide** $\Rightarrow$ fermante sans ouvrante $\Rightarrow$ **incorrecte**.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Programmer le parenthésage <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-7 }

On admet disponible une classe `Pile` d’interface `empiler`, `depiler`, `est_vide`.

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire la fonction `parenthesage_correct(expr)` qui renvoie `True` si la chaîne `expr` est correctement parenthésée (avec `()`, `[]` et `{}`), `False` sinon. La tester sur les quatre exemples précédents.

??? pouce "Coup de pouce"

    Associer à chaque fermante son ouvrante, par exemple avec un dictionnaire. Il y a trois cas d’échec : une fermante alors que la pile est vide, une mauvaise correspondance, une pile non vide à la fin.

??? pouce "Coup de pouce 2 (début de solution)"

    `def parenthesage_correct(expr):`  
    `p = Pile()`  
    `for c in expr:`  
    `if c in "([{":`  
    `p.empiler(c)`

??? corrige "Corrigé"

    ```python
    def parenthesage_correct(expr):
        p = Pile()
        correspond = {')': '(', ']': '[', '}': '{'}
        for c in expr:
            if c in "([{":                     # ouvrante : en attente
                p.empiler(c)
            elif c in ")]}":                   # fermante : doit solder une ouvrante
                if p.est_vide():
                    return False
                if p.depiler() != correspond[c]:
                    return False
        return p.est_vide()                    # tout doit avoir ete referme
    ```

    Tests : `{[()]}` $\to$ `True` ; `(]` $\to$ `False` ; `([]` $\to$ `False` ; `())(` $\to$ `False`.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 8</span> — Défi — des balises bien imbriquées <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-8 }

Dans un document, les balises s’écrivent `<b>` (ouvrante) et `</b>` (fermante), comme en HTML. Une liste de balises est **bien imbriquée** si chaque fermante correspond à la dernière ouvrante non encore fermée.

<span class="run" title="À programmer et tester sur machine">▶</span> On donne une liste de balises, par exemple `["<b>", "<i>", "</i>", "</b>"]` (bien imbriquée) ou `["<b>", "<i>", "</b>", "</i>"]` (mal imbriquée). Écrire `balises_ok(liste)` qui renvoie un booléen, en s’inspirant du parenthésage (une balise fermante `</x>` doit correspondre à l’ouvrante `<x>` au sommet de la pile).

??? pouce "Coup de pouce"

    Une balise fermante commence par `"</"` (méthode `startswith`). On empile les ouvrantes telles quelles ; pour une fermante `b`, l’ouvrante attendue au sommet s’obtient par concaténation : `"<" + b[2:]`. Il reste à reprendre l’algorithme du parenthésage.

??? pouce "Coup de pouce 2 (début de solution)"

    `def balises_ok(liste):`  
    `p = Pile()`  
    `for b in liste:`  
    `if not b.startswith("</"):`  
    `p.empiler(b)`

??? corrige "Corrigé"

    ```python
    def balises_ok(liste):
        p = Pile()
        for b in liste:
            if not b.startswith("</"):         # ouvrante <x>
                p.empiler(b)
            else:                              # fermante </x>
                if p.est_vide():
                    return False
                ouvrante = p.depiler()
                if ouvrante != "<" + b[2:]:     # "</b>" -> b[2:]="b>" -> "<b>"
                    return False
        return p.est_vide()
    ```

    `["<b>", "<i>", "</i>", "</b>"]` $\to$ `True` ; `["<b>", "<i>", "</b>", "</i>"]` $\to$ `False` (à `</b>`, on dépile `<i>` qui ne correspond pas).

### Utiliser une pile, utiliser une file

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 9</span> — Renverser avec une pile <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-9 }

<span class="run" title="À programmer et tester sur machine">▶</span> En utilisant **uniquement** une pile (interface `empiler`/`depiler`/`est_vide`), écrire une fonction `renverser(tab)` qui renvoie une **nouvelle** liste contenant les éléments de `tab` dans l’ordre inverse.

??? pouce "Coup de pouce"

    Tout empiler, puis dépiler tant que la pile n’est pas vide, en ajoutant chaque élément dépilé à la nouvelle liste.

```text
>>> renverser([1, 2, 3, 4])
[4, 3, 2, 1]
```

??? corrige "Corrigé"

    ```python
    def renverser(tab):
        p = Pile()
        for x in tab:            # on empile tout
            p.empiler(x)
        resultat = []
        while not p.est_vide():  # on depile tout : ordre inverse
            resultat.append(p.depiler())
        return resultat
    ```

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 10</span> — Défi — notation polonaise inverse <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-10 }

En **notation polonaise inverse** (NPI), on écrit les opérateurs *après* leurs opérandes : `"3 4 +"` vaut $7$, et `"5 1 2 + 4 * +"` vaut $17$. On évalue avec une pile : chaque **nombre** est empilé ; à chaque **opérateur**, on dépile les *deux* derniers nombres, on applique l’opération et on empile le résultat.

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `evaluer_npi(expr)` où `expr` est une chaîne dont les éléments sont séparés par des espaces (on se limite à `+`, `-`, `*`).

??? pouce "Coup de pouce"

    `expr.split()` découpe la chaîne en une liste d’éléments. Lors d’un opérateur, le premier nombre dépilé est l’opérande de **droite** : attention à l’ordre pour `-`. À la fin, la pile ne contient plus qu’un nombre : le résultat.

??? pouce "Coup de pouce 2 (début de solution)"

    `def evaluer_npi(expr):`  
    `p = Pile()`  
    `for jeton in expr.split():`  
    `if jeton in "+-*":`  
    `b = p.depiler()`  
    `a = p.depiler()`

??? corrige "Corrigé"

    ```python
    def evaluer_npi(expr):
        p = Pile()
        for jeton in expr.split():
            if jeton in "+-*":
                b = p.depiler()          # 2e operande (depile en premier)
                a = p.depiler()          # 1er operande
                if jeton == "+":
                    p.empiler(a + b)
                elif jeton == "-":
                    p.empiler(a - b)     # attention a l'ordre : a - b
                else:
                    p.empiler(a * b)
            else:
                p.empiler(int(jeton))
        return p.depiler()
    ```

    `"3 4 +"` $\to$ `7` ; `"5 1 2 + 4 * +"` $\to$ `17` (on empile `5`, puis `1+2=3`, puis `3*4=12`, puis `5+12=17`).

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 11</span> — Défi — une file avec deux piles <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-11 }

On ne dispose que de **piles**. On veut fabriquer une file en utilisant **deux piles** `entree` et `sortie` : `enfiler` empile dans `entree` ; `defiler` dépile dans `sortie` — et si `sortie` est vide, on y transvase d’abord *tout* le contenu de `entree`.

1.  Sur un exemple (enfiler `1, 2, 3` puis défiler deux fois), expliquer pourquoi on récupère bien `1` puis `2` (comportement FIFO).

2.  Pourquoi le transvasement d’une pile dans l’autre *remet-il* les éléments dans le bon ordre ?

    ??? pouce "Coup de pouce"

        Dessiner les deux piles verticalement après chaque opération. Que devient l’ordre des éléments quand on vide une pile dans une autre ?

    ??? pouce "Coup de pouce 2 (début de solution)"

        Après les trois enfilages, `entree` contient `1`, `2`, `3` (`3` au sommet) et `sortie` est vide. Le premier `defiler` transvase donc tout : `sortie` contient alors `3`, `2`, `1`, avec `1` au sommet…

??? corrige "Corrigé"

    **1.** `enfiler(1)`, `enfiler(2)`, `enfiler(3)` $\Rightarrow$ `entree` contient `1, 2, 3` (sommet `3`), `sortie` vide. Premier `defiler` : `sortie` étant vide, on transvase `entree` dans `sortie` (on dépile `3, 2, 1` et on les empile) $\Rightarrow$ `sortie` contient `3, 2, 1` avec `1` au sommet ; on dépile $\Rightarrow$ **1**. Second `defiler` : `sortie` n’est pas vide, on dépile $\Rightarrow$ **2**. On obtient bien `1` puis `2` : comportement **FIFO**.

    **2.** Une pile *inverse* l’ordre. En transvasant `entree` dans `sortie`, on inverse une fois : l’élément le plus *ancien* (entré en premier) se retrouve au *sommet* de `sortie`, donc prêt à sortir en premier. C’est cette double inversion (empilement puis transvasement) qui rétablit l’ordre d’arrivée.

### Listes chaînées

!!! encadre "Rappel — la classe Cellule"

    Une liste chaînée est faite de **cellules** (maillons). On les représente par la classe suivante ; une liste est soit `None` (liste vide), soit une `Cellule` dont l’attribut `suivante` contient le reste de la liste (définition **récursive**).

    ```python
    class Cellule:
        def __init__(self, v, s):
            self.valeur = v       # l'element
            self.suivante = s     # la cellule suivante, ou None a la fin

    # la liste 1, 2, 3 :
    lst = Cellule(1, Cellule(2, Cellule(3, None)))
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 12</span> — Longueur d’une liste (avec une boucle) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-12 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `longueur(lst)` qui renvoie le nombre de cellules de la liste chaînée `lst`, à l’aide d’une boucle `while` qui parcourt les cellules en suivant les liens. *(La liste vide a pour longueur `0`.)*

??? pouce "Coup de pouce"

    Quelle variable sert de « curseur » sur les cellules, et comment avance-t-elle d’une cellule à la suivante ? Quand faut-il s’arrêter ?

??? corrige "Corrigé"

    ```python
    def longueur(lst):
        n = 0
        c = lst
        while c is not None:
            n = n + 1
            c = c.suivante        # on avance d'une cellule
        return n
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 13</span> — Nombre d’occurrences <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-13 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `occurrences(x, lst)` qui renvoie le nombre de fois que la valeur `x` apparaît dans la liste chaînée `lst`. L’écrire au choix récursivement ou avec une boucle.

??? pouce "Coup de pouce"

    Avec une boucle : même parcours que pour la longueur, mais le compteur n’augmente que sous condition. En récursif : condition d’arrêt `lst is None`, puis l’appel porte sur `lst.suivante`.

??? corrige "Corrigé"

    ```python
    def occurrences(x, lst):
        n = 0
        c = lst
        while c is not None:
            if c.valeur == x:
                n = n + 1
            c = c.suivante
        return n
    ```

    *Autre méthode :* récursivement, la liste vide contient `0` fois `x` ; sinon, on compte la première cellule (`1` ou `0`) et on ajoute les occurrences dans le reste.

    ```python
    def occurrences(x, lst):
        if lst is None:
            return 0
        if lst.valeur == x:
            return 1 + occurrences(x, lst.suivante)
        return occurrences(x, lst.suivante)
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 14</span> — Le n-ième élément <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-14 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `nieme(n, lst)` qui renvoie la valeur de la cellule d’indice `n` (le premier élément a l’indice `0`). Si `n` dépasse la liste, la fonction lèvera `IndexError("indice invalide")`.

??? pouce "Coup de pouce"

    Combien de fois faut-il suivre le lien `suivante` pour atteindre l’indice `n` ? Que vaut le curseur si la liste est trop courte ? L’erreur se lève avec `raise`.

??? corrige "Corrigé"

    ```python
    def nieme(n, lst):
        if lst is None:
            raise IndexError("indice invalide")
        if n == 0:
            return lst.valeur
        return nieme(n - 1, lst.suivante)
    ```

    *Autre méthode :* avec une boucle, on suit `n` fois le lien `suivante` ; si l’on tombe sur `None` en chemin, la liste est trop courte.

    ```python
    def nieme(n, lst):
        c = lst
        for i in range(n):
            if c is None:
                raise IndexError("indice invalide")
            c = c.suivante
        if c is None:
            raise IndexError("indice invalide")
        return c.valeur
    ```

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 15</span> — Défi — insertion dans une liste triée <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-15 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `inserer(x, lst)` qui prend un entier `x` et une liste chaînée `lst` **triée par ordre croissant**, et renvoie une **nouvelle** liste triée où `x` a été inséré à sa place. Ainsi, insérer `3` dans `1, 2, 5, 8` donne `1, 2, 3, 5, 8`.

??? pouce "Coup de pouce"

    Une fonction récursive convient bien. Deux cas immédiats : la liste est vide, ou `x` est inférieur ou égal à la première valeur ; on crée alors une cellule en tête. Sinon, on garde la première valeur, suivie de l’insertion de `x` dans le reste.

??? pouce "Coup de pouce 2 (début de solution)"

    `def inserer(x, lst):`  
    `if lst is None or x <= lst.valeur:`  
    `return Cellule(x, lst)`

??? corrige "Corrigé"

    ```python
    def inserer(x, lst):
        if lst is None or x <= lst.valeur:
            return Cellule(x, lst)                 # x se place ici, devant le reste
        return Cellule(lst.valeur, inserer(x, lst.suivante))
    ```

    Insérer `3` dans `1, 2, 5, 8` : `3 > 1` et `3 > 2`, puis `3 <= 5` $\Rightarrow$ on obtient `1, 2, 3, 5, 8`.

### Vers le bac

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 16</span> — La structure de pile (d’après Asie 2024, jour 1) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-16 }

On dispose d’une classe `Pile` dont les objets représentent une pile, munie des méthodes :

- `estVide()` : renvoie `True` si la pile est vide ;

- `empiler(e)` : ajoute l’élément `e` au sommet de la pile ;

- `depiler()` : renvoie la valeur du sommet et l’enlève de la pile.

1.  On exécute les instructions suivantes :

    ```text
    essai = Pile()
    essai.empiler(3)
    essai.empiler(2)
    essai.empiler(10)
    elt = essai.depiler()
    elt = essai.depiler()
    ```

    Donner la valeur finale de `elt`, puis représenter l’état de la pile `essai`.

2.  Expliquer, avec le mot **LIFO**, pourquoi c’est cette valeur qui est obtenue.

3.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire une fonction `vider(p)` qui dépile et affiche un à un **tous** les éléments d’une pile `p` jusqu’à ce qu’elle soit vide. Dans quel ordre les éléments empilés `3, 2, 10` sont-ils affichés ?

    ??? pouce "Coup de pouce"

        Une boucle `while` qui tourne tant que la pile n’est pas vide ; dans le corps, un seul `depiler`.

??? corrige "Corrigé"

    **1.** On empile `3`, `2`, `10` (sommet `10`). Premier `depiler` $\to$ `10` ; second `depiler` $\to$ `2`. Donc `elt` vaut **2**. La pile `essai` ne contient plus que `3` (au sommet et au fond).

    **2.** Politique **LIFO** : le dernier empilé (`10`) sort en premier, puis l’avant-dernier (`2`). C’est donc `2` qui est la dernière valeur affectée à `elt` ; `3`, empilé en premier, reste au fond.

    **3.**

    ```python
    def vider(p):
        while not p.estVide():
            print(p.depiler())
    ```

    Pour `3, 2, 10` empilés dans cet ordre, l’affichage est `10`, puis `2`, puis `3` (du sommet vers le fond).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 17</span> — Une file de priorité de tâches (d’après Métropole 2025, jour 1) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-17 }

Pour ordonnancer des tâches, on stocke des tuples `(tache, priorite)` dans une `File` d’interface : `enfiler(e)` (ajoute `e` en fin de file), `defiler()` (retire et renvoie la tête), `examiner()` (renvoie la tête sans la retirer), `est_vide()`. La file est rangée de la plus **haute** priorité (en tête) à la plus basse.

On considère la file `f` suivante **(tête à droite)** :

`(<t5>, 1) ; (<t4>, 1) ; (<t2>, 3) ; (<t1>, 3) ; (<t3>, 4)`

1.  Donner la valeur de `f.defiler()[0]`, puis représenter le contenu de `f` après cette instruction.

2.  En repartant de la file `f` d’origine, donner la valeur de `f.examiner()[1]`, et l’état de `f` après.

3.  On veut insérer un tuple `(t, p)` à sa place. Le principe : tant que la tête de `f` est *plus prioritaire* que `p`, on la défile vers une file auxiliaire `f_aux` ; on y enfile ensuite `(t, p)` ; on transvase le reste de `f` dans `f_aux` ; enfin on renvoie `f_aux`. <span class="run" title="À programmer et tester sur machine">▶</span> Recopier et compléter :

    ??? pouce "Coup de pouce"

        Dans les deux boucles, l’élément à enfiler dans `f_aux` est celui que l’on vient de retirer de `f` : par quel appel l’obtient-on ? Entre les deux boucles, on enfile le nouveau tuple.

    ```python
    def ajouter_file_prio(f, t, p):
        f_aux = File()
        while (not f.est_vide()) and f.examiner()[1] > p:
            f_aux.enfiler(...)
        f_aux.enfiler(...)
        while not f.est_vide():
            f_aux.enfiler(...)
        return f_aux
    ```

4.  Représenter l’état de la file `f` (d’origine) après y avoir ajouté, avec `ajouter_file_prio`, la tâche `(t6, 2)` puis la tâche `(t7, 4)`.

5.  Donner le **coût d’exécution**, dans le pire des cas, de `ajouter_file_prio` en fonction du nombre `m` d’éléments de `f`.

6.  *(Pomodoro)* On admet une classe `Tache` munie de `avancer(minutes)` (fait progresser la tâche) et de `est_terminee()` (booléen). <span class="run" title="À programmer et tester sur machine">▶</span> Écrire une fonction `planning(f)` qui : tant que `f` n’est pas vide, défile la tâche de tête, l’**avance de 25** minutes, l’ajoute à une liste résultat, puis, si elle n’est pas terminée, la **ré-insère** dans `f` (avec sa priorité, via `ajouter_file_prio`) ; la fonction renvoie la liste des tâches dans l’ordre où elles ont avancé.

??? corrige "Corrigé"

    **1.** `defiler` retire la tête, ici `(<t3>, 4)` ; `f.defiler()[0]` vaut donc `<t3>` (la tâche). Après : `(<t5>, 1) ; (<t4>, 1) ; (<t2>, 3) ; (<t1>, 3)` (tête = `(<t1>, 3)`).

    **2.** `examiner` renvoie la tête *sans* la retirer, ici `(<t3>, 4)` ; `f.examiner()[1]` vaut donc `4` (la priorité). La file `f` est **inchangée**.

    **3.**

    ```python
    def ajouter_file_prio(f, t, p):
        f_aux = File()
        while (not f.est_vide()) and f.examiner()[1] > p:
            f_aux.enfiler(f.defiler())     # les plus prioritaires passent devant
        f_aux.enfiler((t, p))              # on insere (t, p) a sa place
        while not f.est_vide():
            f_aux.enfiler(f.defiler())     # on transvase le reste
        return f_aux
    ```

    *(Attention : avec la condition stricte `> p`, la boucle s’arrête dès qu’elle rencontre une tâche de *même* priorité ; `(t, p)` est donc placé *devant* les tâches de même priorité déjà présentes et passe en premier. Pour respecter l’ordre d’arrivée à priorité égale, il faudrait écrire `>= p`.)*

    **4.** En insérant `(t6, 2)` (entre les priorités 3 et 1) puis `(t7, 4)` : la tête `(t3, 4)` n’est pas *strictement* plus prioritaire, donc la boucle ne tourne pas et `t7` est enfilé en premier — il passe *devant* `t3`. On obtient (tête à droite) : `(t5, 1) ; (t4, 1) ; (t6, 2) ; (t2, 3) ; (t1, 3) ; (t3, 4) ; (t7, 4)`.

    **5.** Au pire, on défile puis ré-enfile les `m` éléments de `f` : le coût est **proportionnel à `m`** (linéaire).

    **6.**

    ```python
    def planning(f):
        resultat = []
        while not f.est_vide():
            tache, prio = f.defiler()
            tache.avancer(25)
            resultat.append(tache)
            if not tache.est_terminee():
                f = ajouter_file_prio(f, tache, prio)  # reinseree a sa place
        return resultat
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 18</span> — Le collier de bonbons : maillons chaînés (d’après Amérique du Nord 2025, jour 2) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-18 }

Un « collier » de bonbons est une liste chaînée **circulaire** et **doublement** chaînée : chaque bonbon est un maillon possédant trois informations — une `valeur`, un `pred` (le bonbon précédent) et un `succ` (le suivant), tous deux des objets `Bonbon`.

```python
class Bonbon:
    def __init__(self, valeur):
        self.pred = None
        self.valeur = valeur
        self.succ = None
```

On construit un collier de trois bonbons de valeurs `0`, `1`, `2` :

```python
zero = Bonbon(0)
un = Bonbon(1)
deux = Bonbon(2)
zero.succ = un ;   un.succ = deux ;   deux.succ = zero
zero.pred = deux ; un.pred = zero ;   deux.pred = un
```

1.  Donner le terme informatique correspondant à `pred`, `valeur` et `succ`.

2.  Déterminer les valeurs de `a` et `b` après :

    ```text
    a = zero.succ.valeur
    b = un.succ.succ.pred.valeur
    ```

3.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire `creer_collier(n)` qui crée un collier de `n` bonbons de valeurs `0, 1, …, n-1`, correctement chaîné dans les deux sens **et refermé** (le dernier a pour successeur le premier), puis renvoie le premier bonbon (valeur `0`). On suppose `n` $\geqslant 1$.

    ??? pouce "Coup de pouce"

        Créer le premier bonbon, puis, dans une boucle, chaque nouveau bonbon en le reliant au précédent dans les deux sens (une variable retient le précédent). Après la boucle, refermer le collier entre le dernier et le premier.

4.  Écrire les **deux instructions** qui « mangent » le bonbon `deux`, c’est-à-dire le **retirent** du collier en reliant directement son prédécesseur et son successeur.

5.  Quelle égalité caractérise un collier réduit à **un seul** bonbon `b` ?

    ??? pouce "Coup de pouce"

        Que valent alors `b.succ` et `b.pred` ?

6.  *(défi)* <span class="run" title="À programmer et tester sur machine">▶</span> Écrire `dernier_chaine(n)` qui construit le collier de `n` bonbons (avec `creer_collier`), puis les « mange » de proche en proche — à chaque étape, le bonbon courant **mange son successeur** (on le retire du collier), puis on passe au bonbon suivant — jusqu’à ce qu’il n’en reste qu’**un**, dont on renvoie la `valeur`.

    ??? pouce "Coup de pouce"

        Une boucle qui tourne tant que le collier n’est pas réduit à un bonbon (question 5) ; à chaque tour : retirer le successeur du bonbon courant (question 4), puis avancer.

??? corrige "Corrigé"

    **1.** `pred` est le **prédécesseur**, `valeur` la **valeur** (le contenu) et `succ` le **successeur** du maillon. `pred` et `succ` sont eux-mêmes des maillons : la structure est une **liste doublement chaînée** (et ici circulaire).

    **2.** `a = zero.succ.valeur` : `zero.succ` est `un`, donc `a = 1`.  
    `b = un.succ.succ.pred.valeur` : `un.succ` $=$ `deux`, `deux.succ` $=$ `zero`, `zero.pred` $=$ `deux`, donc `b = 2`.

    **3.**

    ```python
    def creer_collier(n):
        premier = Bonbon(0)
        precedent = premier
        for i in range(1, n):
            courant = Bonbon(i)
            precedent.succ = courant       # chainage avant
            courant.pred = precedent       # chainage arriere
            precedent = courant
        precedent.succ = premier           # on referme le collier
        premier.pred = precedent
        return premier
    ```

    *(Pour `n = 1`, la boucle ne s’exécute pas : `premier.succ` et `premier.pred` pointent sur `premier` lui-même.)*

    **4.** On relie le prédécesseur et le successeur de `deux` :

    ```text
    deux.pred.succ = deux.succ
    deux.succ.pred = deux.pred
    ```

    **5.** Un collier réduit à un seul bonbon `b` vérifie `b.succ == b` **et** `b.pred == b` (il est son propre successeur et prédécesseur).

    **6.**

    ```python
    def dernier_chaine(n):
        b = creer_collier(n)
        while b.succ != b:              # tant qu'il reste plus d'un bonbon
            mange = b.succ             # b mange son successeur
            b.succ = mange.succ        # on retire "mange" du collier
            mange.succ.pred = b
            b = b.succ                 # on passe au bonbon suivant
        return b.valeur
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 19</span> — Piles et files pour parcourir un graphe (d’après Polynésie 2024, jour 2) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-19 }

Un graphe est donné par un dictionnaire d’adjacence (les clés sont les sommets, la valeur est la liste des voisins) :

```python
graphe = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D'],
          'D': ['B', 'C']}
```

On admet une **file** d’interface `enfiler(f, e)` / `defiler(f)` / `est_vide(f)`. Le parcours suivant explore le graphe à partir d’un sommet :

```python
def parcours(graphe, depart):
    f = File()
    enfiler(f, depart)
    visite = [depart]
    while not est_vide(f):
        s = defiler(f)
        for v in graphe[s]:
            if v not in visite:
                visite.append(v)
                enfiler(f, v)
    return visite
```

1.  Indiquer la signification des acronymes **LIFO** et **FIFO**, et préciser lequel désigne une file.

2.  Dérouler `parcours(graphe, ’A’)` : donner l’ordre dans lequel les sommets entrent dans `visite`.

3.  <span class="run" title="À programmer et tester sur machine">▶</span> Traduire en une fonction Python `parcours2(graphe, depart)` l’algorithme suivant :

    ??? pouce "Coup de pouce"

        S’inspirer de la fonction `parcours` donnée : remplacer la file par une pile, puis traduire l’algorithme ligne à ligne (une ligne d’algorithme, une instruction Python).

    ```text
    créer une pile p ; empiler depart dans p
    créer une liste visite vide
    tant que p n'est pas vide :
        x = dépiler p
        si x n'est pas dans visite :
            ajouter x à visite
            pour chaque voisin v de x : empiler v dans p
    renvoyer visite
    ```

4.  Donner un **résultat possible** de l’appel `parcours2(graphe, ’A’)`.

*On reconnaît les deux parcours nommés dans le cours : avec une file, le parcours **en largeur** ; avec une pile, le parcours **en profondeur**. Ils seront étudiés en détail aux chapitres Arbres et Graphes.*

??? corrige "Corrigé"

    **1.** **LIFO** = *Last In, First Out* (dernier entré, premier sorti) : c’est la **pile**. **FIFO** = *First In, First Out* (premier entré, premier sorti) : c’est la **file**.

    **2.** On défile `A` et on ajoute `B`, `C` ; on défile `B` et on ajoute `D` ; on défile `C` puis `D` (voisins déjà vus). Ordre d’entrée dans `visite` : `A, B, C, D`.

    **3.**

    ```python
    def parcours2(graphe, depart):
        p = Pile()
        p.empiler(depart)
        visite = []
        while not p.est_vide():
            x = p.depiler()
            if x not in visite:
                visite.append(x)
                for v in graphe[x]:
                    p.empiler(v)
        return visite
    ```

    **4.** Un résultat possible : `[’A’, ’C’, ’D’, ’B’]` (l’ordre dépend de l’ordre d’empilement des voisins). Avec la pile, on repart toujours du dernier sommet ajouté : l’ordre de visite diffère de celui de la question 2.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 20</span> — Ordonnancer des processus avec une file (d’après Amérique du Nord 2024, jour 1) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-20 }

Un système d’exploitation partage le processeur entre plusieurs **processus** à l’aide d’une `File`, selon la méthode du *tourniquet* : à chaque cycle, on défile un processus, on l’exécute pendant un cycle, et s’il n’est pas terminé on le remet en fin de file. On dispose des deux classes suivantes.

```python
class File:
    def __init__(self):
        self.contenu = []
    def enfile(self, element):
        self.contenu.append(element)     # ajout en queue
    def defile(self):
        return self.contenu.pop(0)       # retire et renvoie la tete
    def est_vide(self):
        return self.contenu == []

class Processus:
    def __init__(self, nom, duree):
        self.nom = nom
        self.reste = duree               # nombre de cycles restants
    def execute(self):
        self.reste = self.reste - 1      # consomme un cycle
    def est_fini(self):
        return self.reste == 0
```

1.  Donner l’unique attribut de la classe `File` et son type. Rappeler pourquoi `defile` (qui utilise `pop(0)`) est plus coûteux que `enfile`.

2.  Le code `f = File()` puis `print(f.defile())` provoque une erreur. Expliquer laquelle et pourquoi, puis réécrire la méthode `defile` pour qu’elle renvoie `None` lorsque la file est vide.

3.  <span class="run" title="À programmer et tester sur machine">▶</span> Recopier et compléter la classe `Ordonnanceur` ci-dessous (l’attribut `temps` est le cycle courant).

    ??? pouce "Coup de pouce"

        Chaque ligne à compléter appelle une méthode de `self.file` ou de `proc` : relire les méthodes des deux classes données et choisir la bonne.

    ```python
    class Ordonnanceur:
        def __init__(self):
            self.temps = 0
            self.file = File()

        def ajoute_nouveau_processus(self, proc):
            ...                              # (question 3)

        def tourniquet(self):
            self.temps = self.temps + 1
            if not self.file.est_vide():
                proc = ...                   # (a) le processus elu
                ...                          # (b) l'executer un cycle
                if not proc.est_fini():
                    ...                      # (c) le remettre dans la file
                return proc.nom
            else:
                return None
    ```

4.  On crée `o = Ordonnanceur()`, puis on enfile deux processus `p1` (durée `2`) et `p2` (durée `1`), dans cet ordre. On appelle ensuite `o.tourniquet()` **trois** fois. Donner les trois noms renvoyés et l’état final de la file.

??? corrige "Corrigé"

    **1.** L’unique attribut est `contenu`, de type `list` (une liste Python). `enfile` ajoute en queue avec `append` (immédiat), tandis que `defile` retire la tête avec `pop(0)`, ce qui oblige à **décaler tous les éléments restants** : le coût est proportionnel au nombre d’éléments (cf. cours).

    **2.** Quand la file est vide, `self.contenu` vaut `[]` et `pop(0)` sur une liste vide lève une `IndexError`. On protège la méthode :

    ```python
    def defile(self):
        if self.contenu == []:
            return None
        return self.contenu.pop(0)
    ```

    **3.**

    ```python
    def ajoute_nouveau_processus(self, proc):
        self.file.enfile(proc)

    def tourniquet(self):
        self.temps = self.temps + 1
        if not self.file.est_vide():
            proc = self.file.defile()      # (a) le processus elu
            proc.execute()                 # (b) un cycle consomme
            if not proc.est_fini():
                self.file.enfile(proc)     # (c) remis en fin de file
            return proc.nom
        else:
            return None
    ```

    **4.** File de départ (tête à gauche pour `pop(0)`) : `[p1(2), p2(1)]`.

    - `tourniquet()` : on défile `p1`, il s’exécute (reste `1`), pas fini $\Rightarrow$ réenfilé. File : `[p2(1), p1(1)]`. Renvoie `"p1"`.

    - `tourniquet()` : on défile `p2`, il s’exécute (reste `0`), fini $\Rightarrow$ non réenfilé. File : `[p1(1)]`. Renvoie `"p2"`.

    - `tourniquet()` : on défile `p1`, il s’exécute (reste `0`), fini. File : `[]`. Renvoie `"p1"`.

    Noms renvoyés : `"p1"`, `"p2"`, `"p1"` ; la file finale est **vide**.

### Critiquer une réponse d’IA

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 21</span> — Une file écrite par un assistant d’IA <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> { #ex-03-21 }

Un élève demande à un assistant d’IA : « Écris une classe Python `File` (structure FIFO) avec les méthodes `est_vide`, `enfiler`, `defiler` et `tete`, à partir d’une liste Python. » Voici la réponse obtenue :

```python
class File:
    def __init__(self):
        self.contenu = []            # la tete est au debut de la liste

    def est_vide(self):
        return self.contenu == []

    def enfiler(self, x):
        self.contenu.append(x)       # on ajoute en queue

    def defiler(self):
        return self.contenu.pop()    # on retire l'element de tete

    def tete(self):
        return self.contenu[0]
```

*« Les éléments entrent par la queue avec `append` et sortent par la tête avec `pop` : le premier entré est le premier sorti. »*

1.  La réponse est-elle correcte ? Dérouler à la main la séquence `f = File()`, `f.enfiler(7)`, `f.enfiler(19)`, `f.enfiler(22)`, puis `f.tete()` et `f.defiler()` (dessiner la file horizontalement, tête à droite, comme dans cette feuille).

2.  Localiser et corriger l’erreur.

    ??? pouce "Coup de pouce"

        Sur une liste Python, quel élément `pop()` sans argument retire-t-il : le premier ou le dernier ?

3.  Quelle vérification simple, faite avant de faire confiance à la réponse, aurait suffi à détecter l’erreur ?

??? corrige "Corrigé"

    **1.** **Non.** Après les trois `enfiler`, `contenu` vaut `[7, 19, 22]` ; `f.tete()` renvoie bien `7`, mais `f.defiler()` renvoie `22` (sortie réelle), le *dernier* entré, et laisse `[7, 19]`. Le premier entré, `7`, n’est pas le premier sorti : la structure se comporte comme une **pile**, et `tete` et `defiler` ne désignent même pas le même élément.

    **2.** L’erreur : `pop()` sans argument retire le **dernier** élément de la liste (la queue). Pour retirer la tête, placée au début :

    ```python
        def defiler(self):
            return self.contenu.pop(0)   # retire et renvoie le premier = tete
    ```

    La séquence donne alors `f.defiler()` $\to$ `7`, et il reste `[19, 22]`.

    **3.** Enfiler **deux ou trois valeurs distinctes** puis défiler une fois : on doit ressortir la *première* entrée. Vérifier aussi la cohérence interne de la classe : `tete()` et `defiler()` doivent parler du **même** élément.

### S’entraîner à l’oral

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 22</span> — Expliquer en deux minutes <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-03-22 }

Au Grand Oral comme devant l’examinateur de l’épreuve pratique, il faut savoir **expliquer** une notion clairement, sans notes. Choisir l’un des sujets suivants (ou le tirer au sort) :

1.  Expliquer à un camarade de Première la différence entre une **pile** et une **file**, avec pour chacune un exemple de la vie courante et un usage en informatique.

2.  Expliquer la différence entre **interface** et **implémentation** : pourquoi peut-on utiliser une pile sans savoir comment elle est programmée ?

3.  Expliquer pourquoi ajouter un élément en tête d’une **liste chaînée** est rapide, alors qu’accéder à son millième élément est lent.

**Préparation (5 min, seul).** Noter au brouillon **trois idées** et **un exemple**, rien de plus, puis retourner la feuille. **Exposé (2 min, chronométré).** Debout, face à un camarade, **sans lire de notes** : tout passe par la parole. **Retour (2 min).** Le camarade pose une question de relance (on peut alors s’aider d’un schéma), remplit la grille ci-dessous et donne un conseil ; puis on échange les rôles. Cette grille reprend les critères d’évaluation du Grand Oral.

??? pouce "Coup de pouce"

    Structurer chaque explication en trois temps : une **définition** en une phrase, un **exemple** petit et concret déroulé à voix haute, puis le **piège** (l’erreur que l’auditeur risque de faire). Finir par une phrase qui répond à la question posée. Pour le sujet 1 : faire entrer trois valeurs dans l’ordre $1, 2, 3$, puis dire laquelle sort en premier dans chaque structure. Pour le sujet 3 : que connaît-on, au départ, d’une liste chaînée ?

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

    - **Pile** : dernier entré, premier sorti (LIFO) ; opérations empiler, dépiler, sommet ; une pile d’assiettes ; usages : le bouton « Annuler », la pile d’exécution, le retour arrière du navigateur.

    - **File** : premier entré, premier sorti (FIFO) ; opérations enfiler, défiler ; une file d’attente ; usages : la file d’impression, l’ordonnancement des processus, le parcours en largeur.

    - Exemple : on fait entrer $1, 2, 3$ ; la pile rend $3$ d’abord, la file rend $1$.

    - Piège : la représentation dessinée (pile verticale, sommet en haut ; file horizontale) n’est qu’une convention : suivre celle de l’énoncé.

    **Sujet 2.**

    - Le **type abstrait** (l’interface) dit *quelles* opérations existent et ce qu’elles font (`empiler`, `depiler`, `est_vide`), pas *comment*.

    - L’**implémentation** est un choix concret : une liste Python, une liste chaînée…

    - Exemple : un programme qui évalue une expression avec une pile fonctionne sans changement quelle que soit l’implémentation de la classe `Pile`.

    - Intérêt : on peut changer d’implémentation (pour gagner en efficacité) sans toucher au code qui l’utilise ; seul le coût des opérations change.

    **Sujet 3.**

    - Une liste chaînée est une suite de **maillons** : chacun contient une valeur et un lien vers le maillon suivant ; on ne connaît directement que la **tête**.

    - Ajout en tête : on crée un maillon qui pointe vers l’ancienne tête ; quelques opérations, quelle que soit la longueur (coût constant).

    - Accès au $k$-ième élément : il faut suivre $k$ liens depuis la tête ; le coût est proportionnel à $k$.

    - Comparaison avec un tableau : accès direct par l’indice, mais insertion au début coûteuse (il faut décaler tous les éléments).
