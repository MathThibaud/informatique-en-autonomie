# Exercices

<p class="sous-titre">Structures linéaires : piles, files, listes chaînées</p>

!!! consignes "Mode d’emploi"

    -  Étoiles, <span class="essentiel">• essentiel</span>, coup de pouce, $\blacktriangleright$ et pastilles IA : voir le [mode d’emploi du chapitre 1](../01-recursivite/exercices.md#modeemploi).

    - **Réflexe** : on **utilise** une structure par son **interface** (`empiler`, `depiler`, `enfiler`, `defiler`, `est_vide`…) et l’on **admet** qu’une classe l’implémente. On écrit `p = Pile()` ou `f = File()` sans la reprogrammer.

    - **Convention** de ces exercices : pile dessinée **verticalement** (sommet en haut), file dessinée **horizontalement** avec la **tête à droite** (on enfile à gauche, on défile à droite).

### Piles

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — La bonne opération sur une pile <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-03-1 }

<span class="essentiel">• essentiel</span>

On dispose d’une pile `p`. Pour chaque phrase, écrire l’**appel de méthode** correspondant.

??? pouce "Coup de pouce"

    Relire l’interface d’une pile (cours, ou « Réflexe » du mode d’emploi) : quatre méthodes, une par phrase. Lesquelles modifient la pile, lesquelles la laissent intacte ?

1.  ajouter la valeur `7` au sommet de la pile `p` ;

2.  retirer et récupérer l’élément au sommet de `p` ;

3.  savoir si la pile `p` est vide ;

4.  consulter le sommet de `p` *sans* le retirer.

??? corrige "Corrigé"

    **1.** `p.empiler(7)` **2.** `p.depiler()` **3.** `p.est_vide()` **4.** `p.sommet()`

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 2</span> — Trace d’une pile <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-03-2 }

<span class="essentiel">• essentiel</span>

On part d’une pile `p` vide. Donner, pour chaque appel qui renvoie une valeur, la **valeur renvoyée**, puis représenter le **contenu final** de la pile (sommet en haut).

??? pouce "Coup de pouce"

    Tenir un tableau à trois colonnes : instruction, valeur renvoyée, contenu de la pile après l’instruction. Seuls `depiler` et `sommet` renvoient une valeur : lequel des deux ne retire rien ?

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

    <span class="erreurfreq">▷ Erreur fréquente.</span> Traiter `sommet()` comme `depiler()` : `sommet` renvoie l’élément du sommet *sans le retirer*. Sinon, le dernier `depiler()` renverrait `7` et il ne resterait que `4`.

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

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 3</span> — Parenthésage à la main <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-03-3 }

<span class="essentiel">• essentiel</span>

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

    <span class="erreurfreq">▷ Erreur fréquente.</span> Conclure « correcte » pour `([]` parce qu’aucune erreur n’est apparue pendant la lecture : il faut encore vérifier qu’à la fin la pile est **vide**.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 4</span> — Programmer le parenthésage <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-4 }

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

<span class="routine">▷ Avant de coder.</span> Écrire trois appels attendus sous forme d’`assert` : un cas **normal**, un cas **limite**, un cas **piège**.

??? corrige "Corrigé"

    **Démarche :** on reprend l’algorithme du cours : chaque ouvrante est empilée ; une fermante doit trouver au sommet l’ouvrante qui lui correspond (un dictionnaire donne cette correspondance) ; à la fin, la pile doit être vide. *Appels attendus, écrits avant de coder :*

    ```python
    assert parenthesage_correct("{[()]}")       # cas normal
    assert parenthesage_correct("")             # cas limite : chaine vide
    assert not parenthesage_correct("([)]")     # cas piege : bons nombres, mauvais ordre
    ```

    ```python
    def parenthesage_correct(expr):
        p = Pile()                             # INITIALISER
        correspond = {')': '(', ']': '[', '}': '{'}
        for c in expr:                         # PARCOURIR
            if c in "([{":                     # TESTER : ouvrante, en attente
                p.empiler(c)                   # METTRE A JOUR
            elif c in ")]}":                   # TESTER : fermante
                if p.est_vide():               # TESTER : rien a refermer
                    return False               # RENVOYER
                if p.depiler() != correspond[c]:   # TESTER : mauvais appariement
                    return False               # RENVOYER
        return p.est_vide()                    # RENVOYER : tout est-il referme ?
    ```

    Tests : `{[()]}` $\to$ `True` ; `(]` $\to$ `False` ; `([]` $\to$ `False` ; `())(` $\to$ `False`.

    <span class="erreurfreq">▷ Erreur fréquente.</span> Appeler `p.depiler()` sans tester d’abord `p.est_vide()` : sur `())(`, la deuxième fermante ferait dépiler une pile vide, ce qui provoque une erreur au lieu de renvoyer `False`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 5</span> — Renverser avec une pile <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-5 }

<span class="essentiel">• essentiel</span>

<span class="run" title="À programmer et tester sur machine">▶</span> En utilisant **uniquement** une pile (interface `empiler`/`depiler`/`est_vide`), écrire une fonction `renverser(tab)` qui renvoie une **nouvelle** liste contenant les éléments de `tab` dans l’ordre inverse.

??? pouce "Coup de pouce"

    Tout empiler, puis dépiler tant que la pile n’est pas vide, en ajoutant chaque élément dépilé à la nouvelle liste.

<span class="routine">▷ Avant de coder.</span> Écrire trois appels attendus sous forme d’`assert` : un cas **normal**, un cas **limite**, un cas **piège**.

```text
>>> renverser([1, 2, 3, 4])
[4, 3, 2, 1]
```

??? corrige "Corrigé"

    **Démarche :** une pile inverse l’ordre : on empile tous les éléments de `tab`, puis on dépile tant que la pile n’est pas vide, en ajoutant chaque élément dépilé à la nouvelle liste. *Appels attendus, écrits avant de coder :*

    ```python
    t = [4, 7, 2]
    assert renverser(t) == [2, 7, 4]       # cas normal
    assert renverser([]) == []             # cas limite : liste vide
    assert t == [4, 7, 2]                  # cas piege : tab n'est pas modifie
    ```

    ```python
    def renverser(tab):
        p = Pile()                         # INITIALISER
        for x in tab:                      # PARCOURIR : on empile tout
            p.empiler(x)                   # METTRE A JOUR
        resultat = []                      # INITIALISER
        while not p.est_vide():            # PARCOURIR : on depile tout
            resultat.append(p.depiler())   # METTRE A JOUR : ordre inverse
        return resultat                    # RENVOYER
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — La structure de pile (d’après Asie 2024, jour 1) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-6 }

<span class="duree">≈ 15 min</span>

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

    **Barème indicatif** (sur 2) : Q1 : 0,5 ; Q2 : 0,5 ; Q3 : 1

    **1.** On empile `3`, `2`, `10` (sommet `10`). Premier `depiler` $\to$ `10` ; second `depiler` $\to$ `2`. Donc `elt` vaut **2**. La pile `essai` ne contient plus que `3` (au sommet et au fond).

    **2.** Politique **LIFO** : le dernier empilé (`10`) sort en premier, puis l’avant-dernier (`2`). C’est donc `2` qui est la dernière valeur affectée à `elt` ; `3`, empilé en premier, reste au fond.

    **3.** **Démarche :** une boucle `while` qui tourne tant que la pile n’est pas vide ; chaque tour dépile un élément et l’affiche.

    ```python
    def vider(p):
        while not p.estVide():       # PARCOURIR : jusqu'a la pile vide
            print(p.depiler())
    ```

    Pour `3, 2, 10` empilés dans cet ordre, l’affichage est `10`, puis `2`, puis `3` (du sommet vers le fond).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — La taille d’une pile <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-7 }

<span class="essentiel">• essentiel</span>

La classe `Pile` du cours n’a **pas** de méthode `taille` : on ne dispose que de `est_vide`, `empiler`, `depiler` et `sommet`.

1.  Un élève propose la fonction suivante.

    ```python
    def taille(p):
        n = 0
        while not p.est_vide():
            p.depiler()
            n = n + 1
        return n
    ```

    On empile `4`, `7` puis `2` dans une pile vide `p`, puis on exécute deux fois de suite `print(taille(p))`. Qu’affiche le programme ? Expliquer, avec l’expression **effet de bord**, pourquoi cette fonction ne convient pas.

2.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire une fonction `taille(p)` qui renvoie le nombre d’éléments de la pile `p`, en n’utilisant **que** les méthodes de l’interface, et qui laisse `p` **dans son état d’origine** (mêmes éléments, même ordre).

    ??? pouce "Coup de pouce"

        Les éléments dépilés doivent être rangés quelque part pour être remis ensuite : dans une seconde pile, par exemple. Dans quel ordre en ressortent-ils ?

    <span class="routine">▷ Avant de coder.</span> Écrire trois appels attendus sous forme d’`assert` : un cas **normal**, un cas **limite**, un cas **piège**.

3.  Avec la pile `p` de la question 1, représenter `p` et la pile auxiliaire au moment où l’on a fini de compter, puis à la fin de l’appel.

??? corrige "Corrigé"

    **1.** Le programme affiche `3`, puis `0`. Pour compter, la fonction **dépile tout** : elle modifie la pile reçue en paramètre (**effet de bord**), qui est vide après le premier appel. Connaître la taille d’une pile ne doit pas la détruire.

    <span class="erreurfreq">▷ Erreur fréquente.</span> Répondre que le programme affiche deux fois `3` : la fonction a vidé la pile lors du premier appel, le second trouve une pile vide.

    **2.** On range chaque élément dépilé dans une pile auxiliaire, puis on le remet dans `p` : *Appels attendus, écrits avant de coder :*

    ```python
    p = Pile()
    for x in [4, 7, 2]:
        p.empiler(x)
    assert taille(p) == 3                       # cas normal
    assert taille(Pile()) == 0                  # cas limite : pile vide
    assert taille(p) == 3 and p.sommet() == 2   # cas piege : p n'a pas ete videe
    ```

    ```python
    def taille(p):
        aux = Pile()                     # INITIALISER
        n = 0                            # INITIALISER
        while not p.est_vide():          # PARCOURIR : on vide p dans aux
            aux.empiler(p.depiler())     # METTRE A JOUR
            n = n + 1                    # METTRE A JOUR : on compte
        while not aux.est_vide():        # PARCOURIR : on remet tout dans p
            p.empiler(aux.depiler())     # METTRE A JOUR
        return n                         # RENVOYER
    ```

    **3.** Fin du comptage : `p` est vide et `aux` contient, du fond vers le sommet, `2`, `7`, `4` (l’ordre est **inversé**). Fin de l’appel : `aux` est vide et `p` contient de nouveau `4`, `7`, `2` (`2` au sommet) : le second transvasement inverse une seconde fois l’ordre, ce qui le rétablit.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Copier une pile <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-8 }

On veut écrire une fonction `copier_pile(p)` qui renvoie une **nouvelle** pile contenant les mêmes éléments que `p`, **dans le même ordre** (même sommet), en n’utilisant que `est_vide`, `empiler`, `depiler` et `sommet`. À la fin, `p` doit avoir retrouvé son état d’origine.

1.  Pourquoi l’instruction `q = p` ne fabrique-t-elle pas une copie ? Que devient `p` si l’on exécute ensuite `q.depiler()` ?

2.  Un élève dépile `p` jusqu’à ce qu’elle soit vide en empilant chaque élément dans une nouvelle pile `q`. Pour la pile `p` contenant `4`, `7`, `2` (`2` au sommet), représenter `p` et `q` à la fin. Relever les **deux** défauts de cette méthode.

3.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire la fonction `copier_pile(p)`. La tester en vérifiant que `p` et sa copie se dépilent dans le même ordre, et que dépiler la copie ne modifie pas `p`.

    ??? pouce "Coup de pouce"

        Un seul transvasement renverse l’ordre ; deux transvasements le rétablissent. Pendant le second, chaque élément retiré de la pile auxiliaire peut être empilé **deux fois** : dans `p` et dans la copie.

    ??? pouce "Coup de pouce 2 (début de solution)"

        `def copier_pile(p):`  
        `aux = Pile()`  
        `while not p.est_vide():`  
        `aux.empiler(p.depiler())`  
        `q = Pile()`

    <span class="routine">▷ Avant de coder.</span> Écrire trois appels attendus sous forme d’`assert` : un cas **normal**, un cas **limite**, un cas **piège**.

??? corrige "Corrigé"

    **1.** `q = p` ne crée aucune pile : `q` et `p` sont **deux noms pour le même objet**. `q.depiler()` retire donc aussi le sommet `2` de `p`.

    **2.** À la fin, `p` est vide et `q` contient `2`, `7`, `4` (`4` au sommet). Deux défauts : l’ordre est **inversé** (le sommet de `q` est le fond de `p`) et `p` a été **détruite**.

    **3.** Deux transvasements ; pendant le second, chaque élément est empilé à la fois dans `p` (restauration) et dans la copie : *Appels attendus, écrits avant de coder :*

    ```python
    p = Pile()
    for x in [4, 7, 2]:
        p.empiler(x)
    q = copier_pile(p)
    assert q.depiler() == 2 and q.depiler() == 7   # cas normal : meme ordre
    assert copier_pile(Pile()).est_vide()          # cas limite : pile vide
    assert p.sommet() == 2                         # cas piege : p intacte
    ```

    ```python
    def copier_pile(p):
        aux = Pile()                     # INITIALISER
        while not p.est_vide():          # PARCOURIR : p renversee dans aux
            aux.empiler(p.depiler())     # METTRE A JOUR
        q = Pile()                       # INITIALISER
        while not aux.est_vide():        # PARCOURIR : retour a l'ordre d'origine
            x = aux.depiler()
            p.empiler(x)                 # METTRE A JOUR : on restaure p
            q.empiler(x)                 # METTRE A JOUR : on construit la copie
        return q                         # RENVOYER
    ```

    Test : avec `p` contenant `4`, `7`, `2`, `q = copier_pile(p)` puis `q.depiler()` renvoie `2`, et `p.sommet()` vaut toujours `2` : les deux piles sont bien indépendantes.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 9</span> — Défi — des balises bien imbriquées <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-9 }

<span class="duree">≈ 20 min</span>

Dans un document, les balises s’écrivent <code>&lt;b&gt;</code> (ouvrante) et <code>&lt;/b&gt;</code> (fermante), comme en HTML. Une liste de balises est **bien imbriquée** si chaque fermante correspond à la dernière ouvrante non encore fermée.

<span class="run" title="À programmer et tester sur machine">▶</span> On donne une liste de balises, par exemple <code>&#91;"&lt;b&gt;", "&lt;i&gt;", "&lt;/i&gt;", "&lt;/b&gt;"&#93;</code> (bien imbriquée) ou <code>&#91;"&lt;b&gt;", "&lt;i&gt;", "&lt;/b&gt;", "&lt;/i&gt;"&#93;</code> (mal imbriquée). Écrire `balises_ok(liste)` qui renvoie un booléen, en s’inspirant du parenthésage (une balise fermante <code>&lt;/x&gt;</code> doit correspondre à l’ouvrante <code>&lt;x&gt;</code> au sommet de la pile).

??? pouce "Coup de pouce"

    Une balise fermante commence par <code>"&lt;/"</code> : il suffit de comparer ses deux premiers caractères, `b[:2]`, à <code>"&lt;/"</code>. On empile les ouvrantes telles quelles ; pour une fermante `b`, l’ouvrante attendue au sommet s’obtient par concaténation : `"<" + b[2:]`. Il reste à reprendre l’algorithme du parenthésage.

??? pouce "Coup de pouce 2 (début de solution)"

    `def balises_ok(liste):`  
    `p = Pile()`  
    `for b in liste:`  
    <code>if b&#91;:2&#93; != "&lt;/":</code>  
    `p.empiler(b)`

<span class="routine">▷ Avant de coder.</span> Écrire trois appels attendus sous forme d’`assert` : un cas **normal**, un cas **limite**, un cas **piège**.

??? corrige "Corrigé"

    *Appels attendus, écrits avant de coder :*

    ```python
    assert balises_ok(["<b>", "<i>", "</i>", "</b>"])       # cas normal
    assert balises_ok([])                                    # cas limite : aucune balise
    assert not balises_ok(["<b>", "<i>", "</b>", "</i>"])   # cas piege : mauvais ordre
    ```

    ```python
    def balises_ok(liste):
        p = Pile()                             # INITIALISER
        for b in liste:                        # PARCOURIR
            if b[:2] != "</":                  # TESTER : ouvrante <x>
                p.empiler(b)                   # METTRE A JOUR
            else:                              # fermante </x>
                if p.est_vide():               # TESTER : rien a fermer
                    return False               # RENVOYER
                ouvrante = p.depiler()
                if ouvrante != "<" + b[2:]:    # TESTER : "</b>" attend "<b>"
                    return False               # RENVOYER
        return p.est_vide()                    # RENVOYER
    ```

    <code>&#91;"&lt;b&gt;", "&lt;i&gt;", "&lt;/i&gt;", "&lt;/b&gt;"&#93;</code> $\to$ `True` ; <code>&#91;"&lt;b&gt;", "&lt;i&gt;", "&lt;/b&gt;", "&lt;/i&gt;"&#93;</code> $\to$ `False` (à <code>&lt;/b&gt;</code>, on dépile <code>&lt;i&gt;</code> qui ne correspond pas).

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 10</span> — Défi — notation polonaise inverse <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-10 }

<span class="duree">≈ 20 min</span>

En **notation polonaise inverse** (NPI), on écrit les opérateurs *après* leurs opérandes : `"3 4 +"` vaut $7$, et `"5 1 2 + 4 * +"` vaut $17$. On évalue avec une pile : chaque **nombre** est empilé ; à chaque **opérateur**, on dépile les *deux* derniers nombres, on applique l’opération et on empile le résultat.

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `evaluer_npi(expr)` qui renvoie la valeur (un entier) de l’expression `expr`, une chaîne dont les éléments sont séparés par des espaces (on se limite à `+`, `-`, `*`). Les nombres lus sont des chaînes, à convertir avec `int` avant de les empiler.

??? pouce "Coup de pouce"

    `expr.split()` découpe la chaîne en une liste d’éléments. Lors d’un opérateur, le premier nombre dépilé est l’opérande de **droite** : attention à l’ordre pour `-`. À la fin, la pile ne contient plus qu’un nombre : le résultat.

??? pouce "Coup de pouce 2 (début de solution)"

    `def evaluer_npi(expr):`  
    `p = Pile()`  
    `for jeton in expr.split():`  
    `if jeton in "+-*":`  
    `b = p.depiler()`  
    `a = p.depiler()`

<span class="routine">▷ Avant de coder.</span> Écrire trois appels attendus sous forme d’`assert` : un cas **normal**, un cas **limite**, un cas **piège**.

??? corrige "Corrigé"

    *Appels attendus, écrits avant de coder :*

    ```python
    assert evaluer_npi("3 4 +") == 7      # cas normal
    assert evaluer_npi("42") == 42        # cas limite : un seul nombre, aucun operateur
    assert evaluer_npi("10 4 -") == 6     # cas piege : l'ordre des operandes (pas -6)
    ```

    ```python
    def evaluer_npi(expr):
        p = Pile()                       # INITIALISER
        for jeton in expr.split():       # PARCOURIR
            if jeton in "+-*":           # TESTER : un operateur
                b = p.depiler()          # 2e operande (depile en premier)
                a = p.depiler()          # 1er operande
                if jeton == "+":
                    p.empiler(a + b)     # METTRE A JOUR
                elif jeton == "-":
                    p.empiler(a - b)     # METTRE A JOUR : attention, a - b
                else:
                    p.empiler(a * b)     # METTRE A JOUR
            else:
                p.empiler(int(jeton))    # METTRE A JOUR : un nombre
        return p.depiler()               # RENVOYER : le nombre restant
    ```

    `"3 4 +"` $\to$ `7` ; `"5 1 2 + 4 * +"` $\to$ `17` (on empile `5`, puis `1+2=3`, puis `3*4=12`, puis `5+12=17`).

### Files

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 11</span> — La bonne opération sur une file <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-03-11 }

On dispose d’une file `f`. Pour chaque phrase, écrire l’**appel de méthode** correspondant.

??? pouce "Coup de pouce"

    Même travail qu’à l’exercice 1, avec l’interface d’une file : `enfiler`, `defiler`, `est_vide`, `tete`. Par quel bout entre-t-on dans une file, par quel bout en sort-on ?

1.  ajouter la valeur `7` à la queue de la file `f` ;

2.  retirer et récupérer l’élément de tête de la file `f` ;

3.  savoir si la file `f` est vide ;

4.  consulter la tête de `f` *sans* la retirer.

??? corrige "Corrigé"

    **1.** `f.enfiler(7)` **2.** `f.defiler()` **3.** `f.est_vide()` **4.** `f.tete()`

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 12</span> — Trace d’une file <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-03-12 }

<span class="essentiel">• essentiel</span>

On part d’une file `f` vide. Même travail (la **tête est à droite** : on défile à droite).

??? pouce "Coup de pouce"

    Même tableau qu’à l’exercice 2. On enfile à gauche et l’on défile à droite : l’élément qui sort est toujours le plus ancien encore présent.

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

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 13</span> — Ordonnancer des processus avec une file (d’après Amérique du Nord 2024, jour 1) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-13 }

<span class="essentiel">• essentiel</span> <span class="duree">≈ 30 min</span>

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

4.  On crée `o = Ordonnanceur()`, ainsi que `p1 = Processus("p1", 2)` et `p2 = Processus("p2", 1)`, que l’on ajoute dans cet ordre avec `o.ajoute_nouveau_processus`. On appelle ensuite `o.tourniquet()` **trois** fois. Donner les trois noms renvoyés et l’état final de la file.

??? corrige "Corrigé"

    **Barème indicatif** (sur 4) : Q1 : 0,75 ; Q2 : 1 ; Q3 : 1,5 ; Q4 : 0,75

    **1.** L’unique attribut est `contenu`, de type `list` (une liste Python). `enfile` ajoute en queue avec `append` (immédiat), tandis que `defile` retire la tête avec `pop(0)`, ce qui oblige à **décaler tous les éléments restants** : le coût est proportionnel au nombre d’éléments (cf. cours).

    **2.** Quand la file est vide, `self.contenu` vaut `[]` et `pop(0)` sur une liste vide lève une `IndexError`. On protège la méthode :

    ```python
    def defile(self):
        if self.contenu == []:
            return None
        return self.contenu.pop(0)
    ```

    **3.** **Démarche :** chaque ligne appelle une méthode de l’interface : on défile le processus élu, on l’exécute un cycle, puis on le réenfile (en fin de file) s’il n’est pas fini.

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

    **4.** On donne ici le contenu de l’attribut `contenu` (liste Python : la tête est l’indice `0`, donc **à gauche**, à l’inverse de la convention de dessin « tête à droite » de la feuille). File de départ : `[p1(2), p2(1)]`.

    - `tourniquet()` : on défile `p1`, il s’exécute (reste `1`), pas fini $\Rightarrow$ réenfilé. File : `[p2(1), p1(1)]`. Renvoie `"p1"`.

    - `tourniquet()` : on défile `p2`, il s’exécute (reste `0`), fini $\Rightarrow$ non réenfilé. File : `[p1(1)]`. Renvoie `"p2"`.

    - `tourniquet()` : on défile `p1`, il s’exécute (reste `0`), fini. File : `[]`. Renvoie `"p1"`.

    Noms renvoyés : `"p1"`, `"p2"`, `"p1"` ; la file finale est **vide**.

    <span class="erreurfreq">▷ Erreur fréquente.</span> Faire exécuter `p1` deux fois de suite : après son premier cycle, il est remis en **fin** de file, derrière `p2`, qui passe donc avant lui.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 14</span> — Une file de priorité de tâches (d’après Métropole 2025, jour 1) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-14 }

<span class="duree">≈ 30 min</span>

Pour ordonnancer des tâches, on stocke des tuples `(tache, priorite)` dans une `File` d’interface : `enfiler(e)` (ajoute `e` en fin de file), `defiler()` (retire et renvoie la tête), `examiner()` (renvoie la tête sans la retirer), `est_vide()`. La file est rangée de la plus **haute** priorité (en tête) à la plus basse.

On considère la file `f` suivante **(tête à droite)** :

<code>(&lt;t5&gt;, 1) ; (&lt;t4&gt;, 1) ; (&lt;t2&gt;, 3) ; (&lt;t1&gt;, 3) ; (&lt;t3&gt;, 4)</code>

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

4.  En repartant de la file `f` d’origine, représenter la file obtenue par <code>f = ajouter&#95;file&#95;prio(f, &lt;t6&gt;, 2)</code> puis <code>f = ajouter&#95;file&#95;prio(f, &lt;t7&gt;, 4)</code>.

5.  Donner le **coût d’exécution**, dans le pire des cas, de `ajouter_file_prio` en fonction du nombre `m` d’éléments de `f`.

6.  *(Pomodoro)* On admet une classe `Tache` munie de `avancer(minutes)` (fait progresser la tâche) et de `est_terminee()` (booléen). <span class="run" title="À programmer et tester sur machine">▶</span> Écrire une fonction `planning(f)` qui : tant que `f` n’est pas vide, défile le tuple de tête, **avance de 25** minutes sa tâche, ajoute cette **tâche** (l’objet `Tache`, pas le tuple) à une liste résultat, puis, si elle n’est pas terminée, la **ré-insère** avec sa priorité : `f = ajouter_file_prio(f,` `tache, priorite)` (la fonction renvoie une **nouvelle** file) ; la fonction renvoie la liste des tâches dans l’ordre où elles ont avancé.

??? corrige "Corrigé"

    **Barème indicatif** (sur 4) : Q1 : 0,5 ; Q2 : 0,5 ; Q3 : 1 ; Q4 : 0,5 ; Q5 : 0,5 ; Q6 : 1

    **1.** `defiler` retire la tête, ici <code>(&lt;t3&gt;, 4)</code> ; `f.defiler()[0]` vaut donc <code>&lt;t3&gt;</code> (la tâche). Après : <code>(&lt;t5&gt;, 1) ; (&lt;t4&gt;, 1) ; (&lt;t2&gt;, 3) ; (&lt;t1&gt;, 3)</code> (tête = <code>(&lt;t1&gt;, 3)</code>).

    <span class="erreurfreq">▷ Erreur fréquente.</span> Défiler <code>(&lt;t5&gt;, 1)</code>, l’élément écrit en premier : la tête est à **droite**, c’est <code>(&lt;t3&gt;, 4)</code> qui sort.

    **2.** `examiner` renvoie la tête *sans* la retirer, ici <code>(&lt;t3&gt;, 4)</code> ; `f.examiner()[1]` vaut donc `4` (la priorité). La file `f` est **inchangée**.

    **3.** **Démarche :** on défile vers `f_aux` les tâches plus prioritaires que `p`, on enfile `(t, p)`, puis on transvase le reste.

    ```python
    def ajouter_file_prio(f, t, p):
        f_aux = File()                     # INITIALISER
        while (not f.est_vide()) and f.examiner()[1] > p:   # PARCOURIR
            f_aux.enfiler(f.defiler())     # METTRE A JOUR : les plus prioritaires
        f_aux.enfiler((t, p))              # METTRE A JOUR : (t, p) a sa place
        while not f.est_vide():            # PARCOURIR : le reste
            f_aux.enfiler(f.defiler())     # METTRE A JOUR : on transvase
        return f_aux                       # RENVOYER
    ```

    *(Attention : avec la condition stricte `> p`, la boucle s’arrête dès qu’elle rencontre une tâche de *même* priorité ; `(t, p)` est donc placé *devant* les tâches de même priorité déjà présentes et passe en premier. Pour respecter l’ordre d’arrivée à priorité égale, il faudrait écrire `>= p`.)*

    **4.** En insérant `(t6, 2)` (entre les priorités 3 et 1) puis `(t7, 4)` : la tête `(t3, 4)` n’est pas *strictement* plus prioritaire, donc la boucle ne tourne pas et `t7` est enfilé en premier — il passe *devant* `t3`. On obtient (tête à droite) : `(t5, 1) ; (t4, 1) ; (t6, 2) ; (t2, 3) ; (t1, 3) ; (t3, 4) ; (t7, 4)`.

    **5.** Au pire, on défile puis ré-enfile les `m` éléments de `f` : le coût est **proportionnel à `m`** (linéaire).

    **6.** **Démarche :** tant que la file n’est pas vide : défiler, avancer la tâche, la noter, et la réinsérer à sa place (avec sa priorité) si elle n’est pas terminée.

    ```python
    def planning(f):
        resultat = []                      # INITIALISER
        while not f.est_vide():            # PARCOURIR
            tache, prio = f.defiler()
            tache.avancer(25)
            resultat.append(tache)         # METTRE A JOUR
            if not tache.est_terminee():   # TESTER
                f = ajouter_file_prio(f, tache, prio)  # METTRE A JOUR : reinseree
        return resultat                    # RENVOYER
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 15</span> — Une file écrite par un assistant d’IA <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> { #ex-03-15 }

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

« Les éléments entrent par la queue avec `append` et sortent par la tête avec `pop` : le premier entré est le premier sorti. »

1.  La réponse est-elle correcte ? Dérouler à la main la séquence `f = File()`, `f.enfiler(7)`, `f.enfiler(19)`, `f.enfiler(22)`, puis `f.tete()` et `f.defiler()` (dessiner la file horizontalement, tête à droite, comme dans tout le chapitre).

2.  Localiser et corriger l’erreur.

    ??? pouce "Coup de pouce"

        Sur une liste Python, quel élément `pop()` sans argument retire-t-il : le premier ou le dernier ?

3.  Quelle vérification simple, faite avant de faire confiance à la réponse, aurait suffi à détecter l’erreur ?

??? corrige "Corrigé"

    **1.** **Non.** Après les trois `enfiler`, `contenu` vaut `[7, 19, 22]` ; `f.tete()` renvoie bien `7`, mais `f.defiler()` renvoie `22`, le *dernier* entré, et laisse `[7, 19]`. Le premier entré, `7`, n’est pas le premier sorti : la structure se comporte comme une **pile**, et `tete` et `defiler` ne désignent même pas le même élément.

    **2.** L’erreur : `pop()` sans argument retire le **dernier** élément de la liste (la queue). Pour retirer la tête, placée au début :

    ```python
        def defiler(self):
            return self.contenu.pop(0)   # retire et renvoie le premier = tete
    ```

    La séquence donne alors `f.defiler()` $\to$ `7`, et il reste `[19, 22]`.

    **3.** Enfiler **deux ou trois valeurs distinctes** puis défiler une fois : on doit ressortir la *première* entrée. Vérifier aussi la cohérence interne de la classe : `tete()` et `defiler()` doivent parler du **même** élément.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 16</span> — Copier une file <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-16 }

On dispose d’une classe `File` d’interface `est_vide`, `enfiler`, `defiler` et `tete` (sans méthode `taille`). On veut une fonction `copier_file(f)` qui renvoie une **nouvelle** file contenant les mêmes éléments que `f`, dans le même ordre, et qui laisse `f` dans son état d’origine.

1.  On défile `f` jusqu’à ce qu’elle soit vide en enfilant chaque élément dans une nouvelle file `copie`. L’ordre est-il conservé ? Comparer avec la même méthode appliquée à une pile (exercice 8, question 2). Que manque-t-il encore ?

2.  Pour ne pas vider `f`, un élève propose de réenfiler dans `f` chaque élément juste après l’avoir défilé (et de l’enfiler aussi dans `copie`). Expliquer pourquoi sa boucle `while not f.est_vide():` ne s’arrête jamais.

3.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire la fonction `copier_file(f)`.

    ??? pouce "Coup de pouce"

        Une file auxiliaire garde les éléments retirés, le temps de les remettre dans `f` une fois la copie terminée. Contrairement à une pile, un transvasement de file à file conserve l’ordre.

    <span class="routine">▷ Avant de coder.</span> Écrire trois appels attendus sous forme d’`assert` : un cas **normal**, un cas **limite**, un cas **piège**.

??? corrige "Corrigé"

    **1.** Oui : la file est FIFO, le premier défilé est le premier enfilé dans `copie`, qui reçoit donc les éléments dans le même ordre. Avec une pile, la même méthode *inverse* l’ordre (exercice 8). Il manque la restauration : `f` a été vidée.

    **2.** Chaque tour de boucle défile un élément puis le réenfile : `f` garde toujours le même nombre d’éléments et n’est **jamais vide**. La condition `not f.est_vide()` reste vraie : boucle infinie (et `copie` grossit sans fin).

    **3.** Une file auxiliaire garde les éléments, puis on les remet dans `f` : *Appels attendus, écrits avant de coder :*

    ```python
    f = File()
    for x in [3, 8, 5]:
        f.enfiler(x)
    c = copier_file(f)
    assert c.defiler() == 3 and c.defiler() == 8   # cas normal : meme ordre
    assert copier_file(File()).est_vide()          # cas limite : file vide
    assert f.tete() == 3                           # cas piege : f n'a pas ete videe
    ```

    ```python
    def copier_file(f):
        aux = File()                     # INITIALISER
        copie = File()                   # INITIALISER
        while not f.est_vide():          # PARCOURIR
            x = f.defiler()
            copie.enfiler(x)             # METTRE A JOUR : la copie, dans l'ordre
            aux.enfiler(x)               # METTRE A JOUR : de quoi restaurer f
        while not aux.est_vide():        # PARCOURIR : f retrouve son etat
            f.enfiler(aux.defiler())     # METTRE A JOUR
        return copie                     # RENVOYER
    ```

    Le transvasement de `aux` vers `f` conserve l’ordre : `f` retrouve les mêmes éléments, avec la même tête.

### Piles et files ensemble

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 17</span> — LIFO ou FIFO ? <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-03-17 }

<span class="essentiel">• essentiel</span>

Pour chaque situation, indiquer si la structure adaptée est une **pile** (LIFO) ou une **file** (FIFO), et justifier en une courte phrase.

??? pouce "Coup de pouce"

    Pour chaque situation, se demander quel élément doit être traité en premier : le plus récent (pile) ou le plus ancien (file) ?

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

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 18</span> — Même séquence, deux structures <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-03-18 }

On applique la *même* suite d’ajouts `1, 2, 3, 4` à une pile et à une file, puis on retire **tous** les éléments un par un.

??? pouce "Coup de pouce"

    Dessiner les deux structures après les quatre ajouts (pile verticale, sommet en haut ; file horizontale, tête à droite), puis retirer les éléments un par un en notant chaque valeur qui sort.

1.  Dans quel ordre les valeurs sortent-elles de la **pile** ?

2.  Dans quel ordre sortent-elles de la **file** ?

3.  Quelle structure *inverse* l’ordre des éléments ? Quelle structure le *conserve* ?

??? corrige "Corrigé"

    **1.** De la pile : `4, 3, 2, 1` (le dernier entré sort en premier). **2.** De la file : `1, 2, 3, 4` (le premier entré sort en premier). **3.** La **pile** inverse l’ordre ; la **file** le conserve.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 19</span> — Piles et files pour parcourir un graphe (d’après Polynésie 2024, jour 2) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-19 }

<span class="duree">≈ 20 min</span>

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

3.  <span class="run" title="À programmer et tester sur machine">▶</span> Traduire en une fonction Python `parcours2(graphe, depart)` l’algorithme suivant, en utilisant la classe `Pile` du cours (`empiler`, `depiler`, `est_vide`) :

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

    **Barème indicatif** (sur 3) : Q1 : 0,5 ; Q2 : 0,75 ; Q3 : 1,25 ; Q4 : 0,5

    **1.** **LIFO** = *Last In, First Out* (dernier entré, premier sorti) : c’est la **pile**. **FIFO** = *First In, First Out* (premier entré, premier sorti) : c’est la **file**.

    **2.** On défile `A` et on ajoute `B`, `C` ; on défile `B` et on ajoute `D` ; on défile `C` puis `D` (voisins déjà vus). Ordre d’entrée dans `visite` : `A, B, C, D`.

    **3.** **Démarche :** on traduit l’algorithme ligne à ligne ; c’est la fonction `parcours` où la file est remplacée par une pile, et où un sommet n’est marqué visité qu’au dépilement.

    ```python
    def parcours2(graphe, depart):
        p = Pile()                   # INITIALISER
        p.empiler(depart)            # INITIALISER
        visite = []                  # INITIALISER
        while not p.est_vide():      # PARCOURIR
            x = p.depiler()
            if x not in visite:      # TESTER
                visite.append(x)     # METTRE A JOUR
                for v in graphe[x]:  # PARCOURIR : les voisins
                    p.empiler(v)     # METTRE A JOUR
        return visite                # RENVOYER
    ```

    **4.** Un résultat possible : `[’A’, ’C’, ’D’, ’B’]` (l’ordre dépend de l’ordre d’empilement des voisins). Avec la pile, on repart toujours du dernier sommet ajouté : l’ordre de visite diffère de celui de la question 2.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 20</span> — Défi — une file avec deux piles <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-20 }

<span class="duree">≈ 15 min</span>

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

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 21</span> — Longueur d’une liste (avec une boucle) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-21 }

<span class="essentiel">• essentiel</span>

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `longueur(lst)` qui renvoie le nombre de cellules de la liste chaînée `lst`, à l’aide d’une boucle `while` qui parcourt les cellules en suivant les liens. *(La liste vide a pour longueur `0`.)*

??? pouce "Coup de pouce"

    Quelle variable sert de « curseur » sur les cellules, et comment avance-t-elle d’une cellule à la suivante ? Quand faut-il s’arrêter ?

<span class="routine">▷ Avant de coder.</span> Écrire trois appels attendus sous forme d’`assert` : un cas **normal**, un cas **limite**, un cas **piège**.

??? corrige "Corrigé"

    **Démarche :** une variable `c` sert de curseur : elle part de la première cellule et avance en suivant le lien `suivante` ; on compte une cellule à chaque tour, et l’on s’arrête quand le curseur vaut `None`. *Appels attendus, écrits avant de coder :*

    ```python
    lst = Cellule(1, Cellule(2, Cellule(3, None)))
    assert longueur(lst) == 3                  # cas normal
    assert longueur(None) == 0                 # cas limite : liste vide
    assert longueur(Cellule(5, None)) == 1     # cas piege : la derniere cellule compte
    ```

    ```python
    def longueur(lst):
        n = 0                     # INITIALISER
        c = lst                   # INITIALISER : le curseur
        while c is not None:      # PARCOURIR
            n = n + 1             # METTRE A JOUR
            c = c.suivante        # METTRE A JOUR : on avance d'une cellule
        return n                  # RENVOYER
    ```

    <span class="erreurfreq">▷ Erreur fréquente.</span> Écrire `while c.suivante is not None` : la dernière cellule n’est pas comptée, et la liste vide provoque une erreur (`None` n’a pas d’attribut `suivante`).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 22</span> — Nombre d’occurrences <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-22 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `occurrences(x, lst)` qui renvoie le nombre de fois que la valeur `x` apparaît dans la liste chaînée `lst`. L’écrire au choix récursivement ou avec une boucle.

??? pouce "Coup de pouce"

    Avec une boucle : même parcours que pour la longueur, mais le compteur n’augmente que sous condition. En récursif : condition d’arrêt `lst is None`, puis l’appel porte sur `lst.suivante`.

<span class="routine">▷ Avant de coder.</span> Écrire trois appels attendus sous forme d’`assert` : un cas **normal**, un cas **limite**, un cas **piège**.

??? corrige "Corrigé"

    **Démarche :** même parcours que pour la longueur, mais le compteur n’augmente que si la valeur de la cellule est `x`. *Appels attendus, écrits avant de coder :*

    ```python
    lst = Cellule(2, Cellule(5, Cellule(2, None)))
    assert occurrences(5, lst) == 1      # cas normal
    assert occurrences(2, None) == 0     # cas limite : liste vide
    assert occurrences(2, lst) == 2      # cas piege : en tete et en derniere cellule
    ```

    ```python
    def occurrences(x, lst):
        n = 0                     # INITIALISER
        c = lst                   # INITIALISER
        while c is not None:      # PARCOURIR
            if c.valeur == x:     # TESTER
                n = n + 1         # METTRE A JOUR
            c = c.suivante        # METTRE A JOUR : on avance
        return n                  # RENVOYER
    ```

    *Autre méthode :* récursivement, la liste vide contient `0` fois `x` ; sinon, on compte la première cellule (`1` ou `0`) et on ajoute les occurrences dans le reste.

    ```python
    def occurrences(x, lst):
        if lst is None:                              # CAS DE BASE : liste vide
            return 0
        if lst.valeur == x:                          # TESTER
            return 1 + occurrences(x, lst.suivante)  # APPEL RECURSIF, COMBINER
        return occurrences(x, lst.suivante)          # APPEL RECURSIF
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 23</span> — Le n-ième élément <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-23 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `nieme(n, lst)` qui renvoie la valeur de la cellule d’indice `n` (le premier élément a l’indice `0`). Si `n` est supérieur ou égal à la longueur de la liste, la fonction doit lever `IndexError("indice invalide")`.

??? pouce "Coup de pouce"

    Combien de fois faut-il suivre le lien `suivante` pour atteindre l’indice `n` ? Que vaut le curseur si la liste est trop courte ? L’erreur se lève avec `raise IndexError("indice invalide")` (voir le cours du chapitre *Programmation orientée objet*, « Signaler une erreur »).

<span class="routine">▷ Avant de coder.</span> Écrire trois appels attendus sous forme d’`assert` : un cas **normal**, un cas **limite**, un cas **piège**.

??? corrige "Corrigé"

    **Démarche :** en récursif, deux conditions d’arrêt : la liste est vide (l’indice est trop grand : on lève `IndexError`) ou `n == 0` (on renvoie la valeur de la première cellule). Sinon, l’élément d’indice `n` de la liste est l’élément d’indice `n - 1` du reste. *Appels attendus, écrits avant de coder :*

    ```python
    lst = Cellule(4, Cellule(7, Cellule(2, None)))
    assert nieme(1, lst) == 7      # cas normal
    assert nieme(0, lst) == 4      # cas limite : l'indice 0, la tete
    assert nieme(2, lst) == 2      # cas piege : le dernier indice est longueur - 1
    ```

    ```python
    def nieme(n, lst):
        if lst is None:                         # CAS DE BASE : liste trop courte
            raise IndexError("indice invalide")
        if n == 0:                              # CAS DE BASE : on y est
            return lst.valeur                   # RENVOYER
        return nieme(n - 1, lst.suivante)       # APPEL RECURSIF
    ```

    *Autre méthode :* avec une boucle, on suit `n` fois le lien `suivante` ; si l’on tombe sur `None` en chemin, la liste est trop courte.

    ```python
    def nieme(n, lst):
        c = lst                                 # INITIALISER
        for i in range(n):                      # PARCOURIR : n liens a suivre
            if c is None:                       # TESTER : liste trop courte
                raise IndexError("indice invalide")
            c = c.suivante                      # METTRE A JOUR
        if c is None:                           # TESTER
            raise IndexError("indice invalide")
        return c.valeur                         # RENVOYER
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 24</span> — Le collier de bonbons : maillons chaînés (d’après Amérique du Nord 2025, jour 2) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-24 }

<span class="duree">≈ 45 min</span>

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

1.  Donner le terme correspondant à `pred`, `valeur` et `succ` dans le vocabulaire de la programmation orientée objet.

2.  Déterminer les valeurs de `a` et `b` après :

    ```text
    a = zero.succ.valeur
    b = un.succ.succ.pred.valeur
    ```

3.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire `creer_collier(n)` qui crée un collier de `n` bonbons de valeurs `0, 1, …, n-1`, correctement chaîné dans les deux sens **et refermé** (le dernier a pour successeur le premier), puis renvoie le premier bonbon (valeur `0`). On suppose `n` $\geqslant 1$.

    ??? pouce "Coup de pouce"

        Q3 : créer le premier bonbon, puis, dans une boucle, chaque nouveau bonbon en le reliant au précédent dans les deux sens (une variable retient le précédent). Après la boucle, refermer le collier entre le dernier et le premier.

    <span class="routine">▷ Avant de coder.</span> Écrire trois appels attendus sous forme d’`assert` : un cas **normal**, un cas **limite**, un cas **piège**.

4.  Écrire les **deux instructions** qui « mangent » le bonbon `deux`, c’est-à-dire le **retirent** du collier en reliant directement son prédécesseur et son successeur.

5.  Quelle égalité caractérise un collier réduit à **un seul** bonbon `b` ?

    ??? pouce "Coup de pouce"

        Q5 : que valent alors `b.succ` et `b.pred` ?

6.  *(défi* ★★★*)* <span class="run" title="À programmer et tester sur machine">▶</span> Écrire `dernier_chaine(n)` qui construit le collier de `n` bonbons (avec `creer_collier`), puis les « mange » de proche en proche en partant du bonbon de valeur `0` (celui que renvoie `creer_collier`) — à chaque étape, le bonbon courant **mange son successeur** (on le retire du collier), puis on passe au bonbon suivant — jusqu’à ce qu’il n’en reste qu’**un**, dont on renvoie la `valeur`.

    ??? pouce "Coup de pouce"

        Q6 : une boucle qui tourne tant que le collier n’est pas réduit à un bonbon (question 5) ; à chaque tour : retirer le successeur du bonbon courant (question 4), puis avancer.

??? corrige "Corrigé"

    **Barème indicatif** (sur 6) : Q1 : 0,5 ; Q2 : 0,75 ; Q3 : 1,5 ; Q4 : 0,75 ; Q5 : 0,5 ; Q6 : 2

    **1.** Ce sont des **attributs** de la classe `Bonbon`. `pred` est le **prédécesseur**, `valeur` la **valeur** (le contenu) et `succ` le **successeur** du maillon. `pred` et `succ` sont eux-mêmes des maillons : la structure est une **liste doublement chaînée** (et ici circulaire).

    **2.** `a = zero.succ.valeur` : `zero.succ` est `un`, donc `a = 1`.  
    `b = un.succ.succ.pred.valeur` : `un.succ` $=$ `deux`, `deux.succ` $=$ `zero`, `zero.pred` $=$ `deux`, donc `b = 2`.

    **3.** **Démarche :** une variable `precedent` retient le dernier bonbon créé ; chaque nouveau bonbon lui est relié dans les deux sens ; après la boucle, on referme le collier entre le dernier et le premier. *Appels attendus, écrits avant de coder :*

    ```python
    b = creer_collier(3)
    u = creer_collier(1)
    assert b.succ.valeur == 1 and b.succ.succ.succ == b   # cas normal : referme
    assert u.succ == u and u.pred == u                    # cas limite : un seul bonbon
    assert b.pred.valeur == 2                             # cas piege : chainage arriere
    ```

    ```python
    def creer_collier(n):
        premier = Bonbon(0)                # INITIALISER
        precedent = premier                # INITIALISER
        for i in range(1, n):              # PARCOURIR
            courant = Bonbon(i)
            precedent.succ = courant       # METTRE A JOUR : chainage avant
            courant.pred = precedent       # METTRE A JOUR : chainage arriere
            precedent = courant            # METTRE A JOUR
        precedent.succ = premier           # on referme le collier
        premier.pred = precedent
        return premier                     # RENVOYER
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
        b = creer_collier(n)           # INITIALISER
        while b.succ != b:             # PARCOURIR : plus d'un bonbon
            mange = b.succ             # b mange son successeur
            b.succ = mange.succ        # METTRE A JOUR : "mange" retire
            mange.succ.pred = b        # METTRE A JOUR
            b = b.succ                 # METTRE A JOUR : bonbon suivant
        return b.valeur                # RENVOYER
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 25</span> — Copier une liste chaînée <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-25 }

1.  On exécute le programme suivant. Que vaut `lst.valeur` à la fin ? Pourquoi ?

    ```text
    lst = Cellule(1, Cellule(2, Cellule(3, None)))
    autre = lst
    autre.valeur = 10
    ```

2.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire une fonction **récursive** `copier_liste(lst)` qui renvoie une **nouvelle** liste chaînée, faite de **nouvelles** cellules, contenant les mêmes valeurs que `lst` dans le même ordre.

    ??? pouce "Coup de pouce"

        Condition d’arrêt : la liste vide. Sinon, la copie commence par une nouvelle cellule : quelle valeur contient-elle, et que doit valoir sa cellule suivante ?

    <span class="routine">▷ Avant de coder.</span> Écrire trois appels attendus sous forme d’`assert` : un cas **normal**, un cas **limite**, un cas **piège**.

3.  Vérifier qu’après `c = copier_liste(lst)`, l’instruction `c.valeur = 10` ne modifie pas `lst`.

??? corrige "Corrigé"

    **1.** `lst.valeur` vaut `10`. L’instruction `autre = lst` ne crée aucune cellule : `autre` et `lst` désignent la **même** première cellule, donc la modifier par l’un des noms la modifie pour l’autre.

    **2.** **Démarche :** condition d’arrêt : la liste vide, dont la copie est vide ; sinon, une **nouvelle** cellule de même valeur, suivie de la copie du reste. *Appels attendus, écrits avant de coder :*

    ```python
    lst = Cellule(1, Cellule(2, None))
    c = copier_liste(lst)
    assert c.valeur == 1 and c.suivante.valeur == 2   # cas normal
    assert copier_liste(None) is None                 # cas limite : liste vide
    assert c.suivante is not lst.suivante             # cas piege : le reste aussi est neuf
    ```

    ```python
    def copier_liste(lst):
        if lst is None:                       # CAS DE BASE : liste vide
            return None
        reste = copier_liste(lst.suivante)    # APPEL RECURSIF : copie du reste
        return Cellule(lst.valeur, reste)     # COMBINER : une cellule neuve devant
    ```

    Chaque appel crée une **nouvelle** cellule (`Cellule(…)`) avec la même valeur, suivie de la copie du reste.

    <span class="erreurfreq">▷ Erreur fréquente.</span> Renvoyer `Cellule(lst.valeur, lst.suivante)` : seule la première cellule est neuve, le reste est partagé avec `lst`. Il faut copier aussi le reste, par l’appel récursif.

    **3.** `c` est une nouvelle cellule : `c.valeur = 10` ne change qu’elle : les cellules de `lst` ne sont pas touchées.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 26</span> — Défi — insertion dans une liste triée <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-26 }

<span class="duree">≈ 20 min</span>

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `inserer(x, lst)` qui prend un entier `x` et une liste chaînée `lst` **triée par ordre croissant**, et renvoie une **nouvelle** liste triée où `x` a été inséré à sa place. Ainsi, insérer `3` dans `1, 2, 5, 8` donne `1, 2, 3, 5, 8`.

??? pouce "Coup de pouce"

    Une fonction récursive convient bien. Deux cas immédiats : la liste est vide, ou `x` est inférieur ou égal à la première valeur ; on crée alors une cellule en tête. Sinon, on garde la première valeur, suivie de l’insertion de `x` dans le reste.

??? pouce "Coup de pouce 2 (début de solution)"

    `def inserer(x, lst):`  
    `if lst is None or x <= lst.valeur:`  
    `return Cellule(x, lst)`

<span class="routine">▷ Avant de coder.</span> Écrire trois appels attendus sous forme d’`assert` : un cas **normal**, un cas **limite**, un cas **piège**.

??? corrige "Corrigé"

    *Appels attendus, écrits avant de coder :*

    ```python
    lst = Cellule(1, Cellule(2, Cellule(5, None)))
    assert nieme(2, inserer(3, lst)) == 3     # cas normal : au milieu
    assert inserer(3, None).valeur == 3       # cas limite : liste vide
    assert nieme(3, inserer(9, lst)) == 9     # cas piege : tout a la fin
    ```

    ```python
    def inserer(x, lst):
        if lst is None or x <= lst.valeur:    # CAS DE BASE : x se place ici
            return Cellule(x, lst)            # devant le reste
        reste = inserer(x, lst.suivante)      # APPEL RECURSIF
        return Cellule(lst.valeur, reste)     # COMBINER : la premiere valeur devant
    ```

    Insérer `3` dans `1, 2, 5, 8` : `3 > 1` et `3 > 2`, puis `3 <= 5` $\Rightarrow$ on obtient `1, 2, 3, 5, 8`.

### S’entraîner à l’oral

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 27</span> — Expliquer en deux minutes <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-03-27 }

Au Grand Oral comme devant l’examinateur de l’épreuve pratique, il faut savoir **expliquer** une notion clairement, sans lire ses notes. Choisir l’un des sujets suivants (ou le tirer au sort) :

1.  Expliquer à un camarade de Première la différence entre une **pile** et une **file**, avec pour chacune un exemple de la vie courante et un usage en informatique.

2.  Expliquer la différence entre **interface** et **implémentation** : pourquoi peut-on utiliser une pile sans savoir comment elle est programmée ?

3.  Expliquer pourquoi ajouter un élément en tête d’une **liste chaînée** est rapide, alors qu’accéder à son millième élément est lent.

**Préparation (5 min, seul).** Noter au brouillon **trois idées** et **un exemple**, rien de plus : comme au Grand Oral, ces notes servent d’aide-mémoire. **Exposé (2 min, chronométré).** Debout, face à un camarade, **sans lire ses notes** et sans rien écrire : tout passe par la parole. **Retour (2 min).** Le camarade pose une question de relance (on peut alors s’aider d’un schéma), remplit la grille ci-dessous et donne un conseil ; puis on échange les rôles. Cette grille reprend les critères d’évaluation du Grand Oral.

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

    - Piège : se tromper de bout. La pile se dessine verticalement, sommet en haut ; la file se dessine horizontalement, mais le côté de la tête n’est pas fixé : suivre celui de l’énoncé.

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

### Interface d’une liste, liste ou dictionnaire

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 28</span> — L’interface d’une liste <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-28 }

On dispose de l’interface du cours : `liste_vide()`, `est_vide(L)`, `ajouter_tete(x, L)`, `tete(L)` et `queue(L)`.

1.  On pose `L = ajouter_tete(3, ajouter_tete(8, ajouter_tete(1, liste_vide())))`. Écrire les éléments de `L` dans l’ordre, puis donner `tete(L)`, `tete(queue(L))` et `est_vide(queue(queue(queue(L))))`.

2.  <span class="run" title="À programmer et tester sur machine">▶</span> En n’utilisant **que** l’interface, écrire une fonction récursive `appartient(x, L)` qui renvoie `True` si `x` est un élément de `L`, `False` sinon.

    ??? pouce "Coup de pouce"

        Condition d’arrêt : la liste vide ne contient rien. Sinon, soit la tête est `x`, soit il faut chercher dans la queue.

    <span class="routine">▷ Avant de coder.</span> Écrire trois appels attendus sous forme d’`assert` : un cas **normal**, un cas **limite**, un cas **piège**.

3.  <span class="run" title="À programmer et tester sur machine">▶</span> Toujours avec la seule interface, écrire `renverser(L)` qui renvoie une **nouvelle** liste contenant les éléments de `L` dans l’ordre inverse.

    ??? pouce "Coup de pouce"

        Partir d’une liste vide `r` et, en parcourant `L` du début à la fin, ajouter chaque élément en tête de `r` : le premier élément lu finit en dernier.

4.  <span class="run" title="À programmer et tester sur machine">▶</span> Implémenter les cinq opérations de l’interface avec la classe `Cellule` du rappel, puis tester les questions 1 à 3.

5.  Après `M = ajouter_tete(9, L)`, la liste `L` a-t-elle changé ? Comparer avec `p.empiler(9)` sur une pile `p`.

??? corrige "Corrigé"

    **1.** On lit de l’intérieur vers l’extérieur : `1`, puis `8` devant, puis `3` devant. `L` est la liste `3, 8, 1`. `tete(L)` $\to$ `3` ; `tete(queue(L))` $\to$ `8` ; après trois `queue`, il ne reste rien : `est_vide(…)` $\to$ `True`.

    **2.** *Appels attendus, écrits avant de coder :*

    ```python
    L = ajouter_tete(3, ajouter_tete(8, ajouter_tete(1, liste_vide())))
    assert appartient(8, L)                  # cas normal
    assert not appartient(8, liste_vide())   # cas limite : liste vide
    assert appartient(1, L)                  # cas piege : la derniere valeur
    ```

    ```python
    def appartient(x, L):
        """Renvoie True si x est un element de la liste L."""
        if est_vide(L):                  # CAS DE BASE : liste vide
            return False
        if tete(L) == x:                 # CAS DE BASE : x trouve en tete
            return True
        return appartient(x, queue(L))   # APPEL RECURSIF : dans la queue
    ```

    `appartient(8, L)` $\to$ `True` ; `appartient(5, L)` $\to$ `False`. Variant : la longueur de `L`, qui diminue de 1 à chaque appel.

    **3.**

    ```python
    def renverser(L):
        """Renvoie une nouvelle liste : les elements de L dans l'ordre inverse."""
        r = liste_vide()                   # INITIALISER
        while not est_vide(L):             # PARCOURIR
            r = ajouter_tete(tete(L), r)   # METTRE A JOUR : passe devant r
            L = queue(L)                   # METTRE A JOUR : on avance
        return r                           # RENVOYER
    ```

    Sur `3, 8, 1`, `r` vaut successivement `3`, puis `8, 3`, puis `1, 8, 3`. La variable locale `L` avance dans la liste, mais la liste reçue n’est pas modifiée.

    **4.**

    ```python
    def liste_vide():
        return None

    def est_vide(L):
        return L is None

    def ajouter_tete(x, L):
        return Cellule(x, L)

    def tete(L):
        return L.valeur

    def queue(L):
        return L.suivante
    ```

    Les fonctions des questions 2 et 3 marchent sans changement avec cette implémentation : elles n’utilisent que l’interface.

    **5.** Non : `ajouter_tete` **renvoie** une nouvelle liste `9, 3, 8, 1`, dont la suite est `L` ; `L` vaut toujours `3, 8, 1`. Au contraire, `p.empiler(9)` ne renvoie rien et **modifie** la pile `p`. Les deux structures ne se distinguent pas par leur contenu, mais par leur **jeu de méthodes**.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 29</span> — Liste ou dictionnaire ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-29 }

Le portique d’un lycée doit vérifier, à chaque passage, que le numéro de badge présenté est autorisé. Il y a $n$ badges autorisés.

1.  On range les numéros autorisés dans une liste `autorises`. Combien de comparaisons fait, au pire, le test `b in autorises` ? Quand ce pire cas se produit-il ?

2.  On range plutôt les badges dans un dictionnaire `badges` dont les **clés** sont les numéros (et les valeurs, le nom de l’élève). Que dire du coût du test `b in badges` ?

3.  <span class="run" title="À programmer et tester sur machine">▶</span> Recopier et compléter la fonction suivante, qui mesure le temps d’un test pour un badge absent (le pire cas), puis l’appeler pour $n = 10\,000$, $100\,000$ et $1\,000\,000$. Que constate-t-on quand $n$ est multiplié par 10 ?

    ```python
    import time

    def mesurer(n):
        """Renvoie le couple (temps liste, temps dictionnaire), en secondes."""
        autorises = [b for b in range(n)]
        badges = {b: "inconnu" for b in range(n)}
        debut = time.perf_counter()
        trouve = -1 in autorises
        t_liste = time.perf_counter() - debut
        ...                              # a completer pour le dictionnaire
        return (t_liste, t_dico)
    ```

4.  Le surveillant veut aussi savoir si une élève nommée `"Lina"` a un badge. Le test `"Lina" in badges.values()` est-il aussi rapide que `b in badges` ? Pourquoi ?

5.  Le portique doit en plus afficher, à la fin de la journée, les passages **dans l’ordre** où ils ont eu lieu. Quelle structure choisir pour mémoriser les passages ? Et pour les badges autorisés ?

??? corrige "Corrigé"

    **1.** `b in autorises` compare `b` aux éléments un par un : au pire $n$ comparaisons, quand `b` est absent (ou est le dernier élément). Coût linéaire, en O($n$).

    **2.** Python ne parcourt pas les clés : il calcule, à partir de `b`, l’endroit où cette clé serait rangée. Le coût est à peu près constant, en O(1), quel que soit $n$.

    **3.**

    ```python
        debut = time.perf_counter()
        trouve = -1 in badges
        t_dico = time.perf_counter() - debut
    ```

    Ordres de grandeur obtenus (ils dépendent de la machine) :

    |      $n$      |     **liste**      |       **dictionnaire**        |
    |:-------------:|:------------------:|:-----------------------------:|
    |   $10\,000$   | environ $0{,}1$ ms |   moins d’une microseconde    |
    |  $100\,000$   |   environ $1$ ms   |   moins d’une microseconde    |
    | $1\,000\,000$ |  environ $10$ ms   | de l’ordre d’une microseconde |

    Quand $n$ est multiplié par 10, le temps de la liste est multiplié par 10 environ (coût linéaire) ; celui du dictionnaire ne change presque pas (les petites variations sont dues à la mesure elle-même).

    **4.** Non. Ce sont les **clés** qui se trouvent en temps constant. `badges.values()` est parcouru valeur par valeur : O($n$), comme une liste. Si l’on cherche souvent par nom, il faut un second dictionnaire dont les clés sont les noms.

    **5.** Pour les passages, une **liste** (ou une **file**) : on ajoute chaque passage à la fin, et l’ordre est conservé. Pour les badges autorisés, le **dictionnaire**, puisque l’opération la plus fréquente est « ce badge est-il autorisé ? ». Un même programme peut utiliser les deux structures, chacune pour ce qu’elle fait bien.
