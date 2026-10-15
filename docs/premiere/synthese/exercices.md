# Exercices

<p class="sous-titre">Problèmes de synthèse</p>

!!! consignes "Mode d’emploi"

    - Chaque problème **croise** des notions de plusieurs chapitres : en programmation, on ne se demande jamais « est-ce un exercice sur les boucles ou sur le binaire ? ».

    - Sous chaque titre, la ligne Chapitres croisés indique ce qu’il faut avoir vu. Un problème peut être repris plus tard dans l’année, pour réviser.

    - Niveau : ★ échauffement, ★★ classique (niveau bac), ★★★ défi ; les *coups de pouce* et les *corrigés* se déplient sous chaque exercice.

    - <span class="run" title="À programmer et tester sur machine">▶</span> *À programmer et tester* en Python (console ou éditeur en ligne).

    - Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la [charte d’usage de l’IA](../charte.md).

### Après les chapitres 1 et 2 (Les bases de la programmation Python ; Le binaire et l’écriture des nombres)

!!! remarque "Remarque"

    Dans cette section, on travaille uniquement avec des **entiers** : pas de listes ni de chaînes de caractères. Les deux outils clés sont `n % 2` (le dernier bit de `n`) et `n // 2` (`n` privé de son dernier bit), comme dans la méthode des divisions successives.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 1</span> — Le binaire avec des entiers <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-S-1 }

Chapitres croisés : *Les bases de la programmation Python (boucle `while`, fonctions) ; Le binaire et l’écriture des nombres*

On veut faire écrire par Python l’écriture binaire d’un entier, **sans chaîne de caractères** : on la représente par un entier « qui ne contient que des 0 et des 1 ». Par exemple, l’écriture binaire de $13$ est représentée par l’entier `1101` (mille cent un).

1.  Écrire à la main l’écriture binaire de $13$ et de $185$ par la méthode des divisions successives. Dans quel ordre obtient-on les bits ?

2.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire une fonction `en_binaire(n)` qui renvoie cet entier pour un entier `n` positif ou nul (`en_binaire(13)` renvoie `1101` et `en_binaire(0)` renvoie `0`). On pourra utiliser une variable `puissance` qui vaut successivement $1$, $10$, $100$…

    ??? pouce "Coup de pouce"

        À chaque tour : on récupère le dernier bit `n % 2`, on le place à la bonne position en le multipliant par `puissance`, puis on passe au bit suivant (`n` devient `n // 2`, `puissance` est multipliée par $10$).

3.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire la fonction réciproque `en_decimal(b)` : `en_decimal(1101)` renvoie `13`. À l’aide d’une boucle, vérifier que `en_decimal(en_binaire(n))` redonne bien `n` pour tous les entiers `n` de $0$ à $300$.

4.  Justifier que la boucle de `en_binaire` se termine : quel **variant** peut-on proposer ?

5.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire une fonction `nb_bits(n)` qui renvoie le nombre de bits nécessaires pour écrire l’entier `n` $\geqslant 1$. Combien de bits faut-il pour $255$ ? pour $256$ ? Faire le lien avec le cours.

??? corrige "Corrigé"

    !!! remarque "Remarque"

        On donne une version de chaque fonction ; d’autres écritures correctes sont possibles. Le fichier complet, `corrige_synthese_premiere.py`, est en ligne : [`github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/premiere/synthese`](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/premiere/synthese).

    **1.** $13 = 2 \times 6 + 1$, $6 = 2 \times 3 + 0$, $3 = 2 \times 1 + 1$, $1 = 2 \times 0 + 1$ : en lisant les restes de bas en haut, $13 = \texttt{1101}_2$. De même, $185 = \texttt{10111001}_2$. Les bits sont obtenus **de droite à gauche** : le premier reste est le bit de poids faible.

    **2.**

    ```python
    def en_binaire(n):
        resultat = 0
        puissance = 1
        while n > 0:
            resultat = resultat + (n % 2) * puissance
            puissance = puissance * 10
            n = n // 2
        return resultat
    ```

    Pour `n = 0`, on n’entre pas dans la boucle et la fonction renvoie `0`.

    **3.** Même idée en sens inverse : on lit les chiffres de `b` de droite à gauche (`b % 10`) et on les multiplie par $1, 2, 4, 8\dots$

    ```python
    def en_decimal(b):
        total = 0
        puissance = 1
        while b > 0:
            total = total + (b % 10) * puissance
            puissance = puissance * 2
            b = b // 10
        return total

    for n in range(301):
        assert en_decimal(en_binaire(n)) == n
    ```

    **4.** **Variant** : `n`. C’est un entier positif ou nul qui diminue strictement à chaque tour (`n // 2 < n` dès que `n` $\geqslant 1$) ; il finit donc par valoir $0$, et la condition `n > 0` devient fausse.

    **5.**

    ```python
    def nb_bits(n):
        nb = 1
        while n >= 2:
            n = n // 2
            nb = nb + 1
        return nb
    ```

    `nb_bits(255)` vaut $8$ et `nb_bits(256)` vaut $9$ : sur $8$ bits, on code les entiers de $0$ à $2^8 - 1 = 255$, et $256 = 2^8$ en demande un de plus (`100000000`).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 2</span> — Le bit de parité <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-S-2 }

Chapitres croisés : *Les bases de la programmation Python (accumulateur, booléens) ; Le binaire et l’écriture des nombres*

Lors d’une transmission, un bit peut être modifié par une perturbation. Pour détecter l’erreur, l’émetteur ajoute à droite du message un **bit de parité**, choisi pour que le nombre total de bits à $1$ soit **pair**.

1.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire une fonction `nb_uns(n)` qui renvoie le nombre de bits égaux à $1$ dans l’écriture binaire de `n` (`nb_uns(13)` renvoie `3`).

2.  <span class="run" title="À programmer et tester sur machine">▶</span> En déduire une fonction `bit_parite(n)` qui renvoie `0` ou `1`.

3.  Ajouter un bit $b$ à droite de l’écriture binaire de $n$ revient à calculer $2n + b$. Justifier, puis écrire une fonction `emettre(n)` qui renvoie le nombre réellement envoyé. Que vaut `emettre(13)`, en décimal et en binaire ?

4.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire une fonction `verifier(m)` qui renvoie `True` si le nombre reçu `m` a un nombre pair de bits à $1$, et `False` sinon.

5.  Le message `11011` est envoyé. On reçoit `11111`, puis, lors d’un autre envoi, `11101`. Que répond `verifier` dans chaque cas ? Quelle est la limite de ce procédé ?

    ??? pouce "Coup de pouce"

        Compter les bits modifiés dans chacun des deux messages reçus. Un nombre pair de bits à $1$ peut-il le rester quand on change deux bits ?

??? corrige "Corrigé"

    **1.** et **2.**

    ```python
    def nb_uns(n):
        nb = 0
        while n > 0:
            nb = nb + n % 2      # le dernier bit vaut 0 ou 1
            n = n // 2
        return nb

    def bit_parite(n):
        return nb_uns(n) % 2
    ```

    **3.** Multiplier par $2$ décale tous les bits d’un cran vers la gauche (comme multiplier par $10$ en décimal) et place un $0$ à droite ; ajouter $b$ remplace ce $0$ par $b$.

    ```python
    def emettre(n):
        return 2 * n + bit_parite(n)
    ```

    $13 = \texttt{1101}$ a trois bits à $1$ : le bit de parité vaut $1$, et `emettre(13)` renvoie $27 = \texttt{11011}_2$.

    **4.**

    ```python
    def verifier(m):
        return nb_uns(m) % 2 == 0
    ```

    **5.** `11111` contient cinq $1$ (un bit modifié) : `verifier` renvoie `False`, l’erreur est **détectée**. `11101` contient quatre $1$ (deux bits modifiés) : `verifier` renvoie `True`, l’erreur **passe inaperçue**. Le bit de parité détecte un nombre *impair* de bits modifiés, jamais un nombre pair ; il ne dit pas non plus *quel* bit est faux.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 3</span> — Des entiers relatifs sur 8 bits <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-S-3 }

Chapitres croisés : *Le binaire et l’écriture des nombres (complément à deux) ; Les bases de la programmation Python*

Sur 8 bits, on code les entiers de $-128$ à $127$ en complément à deux. Le code d’un entier est un nombre de $0$ à $255$ (l’octet qu’on range en mémoire).

1.  Coder $-12$ sur 8 bits avec la méthode du cours (inverser les bits, ajouter $1$), puis donner la valeur décimale de l’octet obtenu.

2.  Pour $a$ compris entre $0$ et $255$, inverser les 8 bits de $a$ donne $255 - a$. Justifier. En déduire que le code de $-x$ (avec $0 < x \leqslant 128$) est $256 - x$. Vérifier sur $-12$.

3.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire une fonction `code_8bits(x)` qui renvoie le code de l’entier `x` (avec $-128 \leqslant x \leqslant 127$), et la fonction réciproque `valeur(v)` qui renvoie l’entier représenté par un octet `v`. Tester avec une boucle que `valeur(code_8bits(x))` redonne `x` pour tous les entiers de $-128$ à $127$.

4.  La machine additionne deux octets puis ne garde que 8 bits, c’est-à-dire le reste de la division par $256$. <span class="run" title="À programmer et tester sur machine">▶</span> Écrire une fonction `addition_8bits(a, b)` qui simule ce calcul pour deux entiers relatifs. Que renvoie-t-elle pour $12 + (-12)$ ? pour $100 + 50$ ? pour $127 + 1$ ? Expliquer ces deux derniers résultats.

    ??? pouce "Coup de pouce"

        On code `a` et `b`, on additionne les deux codes, on prend le reste modulo $256$ (on « oublie » la retenue qui déborde), puis on revient à un entier relatif avec `valeur`.

??? corrige "Corrigé"

    **1.** $12 = \texttt{00001100}$, on inverse : `11110011`, on ajoute $1$ : `11110100`, soit $128 + 64 + 32 + 16 + 4 = 244$.

    **2.** Pour chaque position, le bit inversé vaut $1 -$ le bit d’origine. La somme de $a$ et de son inversé a donc ses $8$ bits à $1$ : elle vaut $\texttt{11111111}_2 = 255$, d’où inversé $= 255 - a$. Le code de $-x$ est alors $(255 - x) + 1 = 256 - x$. Pour $-12$ : $256 - 12 = 244$.

    **3.**

    ```python
    def code_8bits(x):
        if x >= 0:
            return x
        return 256 + x

    def valeur(v):
        if v < 128:          # bit de poids fort a 0 : entier positif
            return v
        return v - 256

    for x in range(-128, 128):
        assert valeur(code_8bits(x)) == x
    ```

    **4.**

    ```python
    def addition_8bits(a, b):
        return valeur((code_8bits(a) + code_8bits(b)) % 256)
    ```

    $12 + (-12)$ donne bien $0$ ($12 + 244 = 256$, et `256 % 256` vaut $0$ : la retenue qui déborde est oubliée). Mais $100 + 50$ renvoie $-106$ et $127 + 1$ renvoie $-128$ : le vrai résultat ($150$, $128$) dépasse $127$, le plus grand entier codable. Son code a un bit de poids fort à $1$, qui est lu comme le signe d’un négatif. C’est un **dépassement de capacité** : la machine ne signale rien, c’est au programmeur d’y penser.

### Après les chapitres 3 et 4 (Les types construits ; Algorithmique : le parcours séquentiel)

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 4</span> — Le bulletin de notes <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-S-4 }

Chapitres croisés : *Les types construits (dictionnaires, tableaux, p-uplets) ; Algorithmique : le parcours séquentiel*

Les notes d’une petite classe sont rangées dans un dictionnaire qui associe à chaque prénom le tableau de ses notes.

```python
notes = {"Léa": [12, 15, 9], "Noé": [8, 11, 14, 10], "Zoé": [17, 13]}
```

1.  Que valent `notes["Noé"]`, `len(notes)` et `notes["Léa"][2]` ? Écrire l’instruction qui ajoute la note $16$ à Zoé.

2.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire une fonction `moyenne(t)` qui renvoie la moyenne d’un tableau de nombres non vide, puis une fonction `moyennes(notes)` qui renvoie un **nouveau** dictionnaire associant à chaque prénom sa moyenne.

3.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire une fonction `meilleur(notes)` qui renvoie le p-uplet `(prénom, moyenne)` de l’élève qui a la meilleure moyenne.

    ??? pouce "Coup de pouce"

        C’est la recherche d’un maximum du cours : on garde le meilleur trouvé jusqu’ici (son prénom *et* sa moyenne) et on le remplace dès qu’on trouve mieux.

4.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire une fonction `nb_notes_sous(notes, seuil)` qui compte, tous élèves confondus, les notes strictement inférieures à `seuil`. Combien de fois la comparaison `note < seuil` est-elle exécutée pour une classe de $30$ élèves ayant chacun $8$ notes ?

??? corrige "Corrigé"

    **1.** `notes["Noé"]` vaut `[8, 11, 14, 10]`, `len(notes)` vaut $3$ (trois clés) et `notes["Léa"][2]` vaut $9$. Pour ajouter une note : `notes["Zoé"].append(16)`.

    **2.**

    ```python
    def moyenne(t):
        s = 0
        for x in t:
            s = s + x
        return s / len(t)

    def moyennes(notes):
        resultat = {}
        for nom in notes:
            resultat[nom] = moyenne(notes[nom])
        return resultat
    ```

    Avec le dictionnaire de l’énoncé : `{"Léa": 12.0, "Noé": 10.75, "Zoé": 15.0}`.

    **3.**

    ```python
    def meilleur(notes):
        meilleur_nom = None
        meilleure_moy = -1          # plus petite que toute moyenne possible
        for nom in notes:
            m = moyenne(notes[nom])
            if m > meilleure_moy:
                meilleur_nom = nom
                meilleure_moy = m
        return (meilleur_nom, meilleure_moy)
    ```

    `meilleur(notes)` renvoie `("Zoé", 15.0)`. Le champion part ici d’une moyenne fictive `-1` (une *sentinelle*), valable parce que toute moyenne est positive. *Autre méthode*, celle du cours : initialiser le champion avec un élément existant, par exemple le premier nom rencontré dans le dictionnaire.

    **4.**

    ```python
    def nb_notes_sous(notes, seuil):
        nb = 0
        for nom in notes:
            for note in notes[nom]:
                if note < seuil:
                    nb = nb + 1
        return nb
    ```

    `nb_notes_sous(notes, 10)` renvoie $2$ (le $9$ de Léa et le $8$ de Noé). Chaque note est comparée une fois : $30 \times 8 = 240$ comparaisons. Le coût est proportionnel au nombre total de notes.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 5</span> — Une image en noir et blanc <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-S-5 }

Chapitres croisés : *Les types construits (tableaux de tableaux) ; Algorithmique : le parcours séquentiel ; Le binaire et l’écriture des nombres*

Une image de $8 \times 8$ pixels en noir et blanc est représentée par un tableau de $8$ lignes, chaque ligne étant un tableau de $8$ entiers : `1` pour un pixel noir, `0` pour un pixel blanc.

```python
image = [[0, 0, 1, 1, 1, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 1, 0],
         [1, 0, 1, 0, 0, 1, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 1, 0, 0, 1, 0, 1],
         [1, 0, 0, 1, 1, 0, 0, 1],
         [0, 1, 0, 0, 0, 0, 1, 0],
         [0, 0, 1, 1, 1, 1, 0, 0]]
```

1.  Dessiner l’image sur un quadrillage de $8 \times 8$ cases. Que vaut `image[5][3]` ?

2.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire une fonction `nb_noirs(image)` qui compte les pixels noirs, à l’aide de deux boucles imbriquées.

3.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire, **par compréhension**, une fonction `negatif(image)` qui renvoie une **nouvelle** image où le noir et le blanc sont échangés, sans modifier `image`.

4.  Chaque ligne, lue de gauche à droite, est l’écriture binaire d’un entier de $0$ à $255$ : la ligne entière tient donc dans un seul **octet**. Quel entier représente la première ligne ? <span class="run" title="À programmer et tester sur machine">▶</span> Écrire une fonction `ligne_en_octet(ligne)`, puis une fonction `compresser(image)` qui renvoie le tableau des $8$ octets de l’image.

    ??? pouce "Coup de pouce"

        En lisant les bits de gauche à droite, on peut construire le nombre au fur et à mesure : à chaque nouveau bit, la valeur déjà obtenue est multipliée par $2$ (tous ses bits se décalent d’un cran vers la gauche), puis on ajoute le nouveau bit.

5.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire la fonction réciproque `decompresser(octets)`, qui reconstruit l’image à partir des $8$ octets, et vérifier que `decompresser(compresser(image)) == image`. Combien d’entiers faut-il stocker avant et après compression ?

??? corrige "Corrigé"

    **1.** L’image est un visage souriant. `image[5][3]` (ligne $5$, colonne $3$, en comptant à partir de $0$) vaut $1$ : un pixel noir de la bouche.

    **2.**

    ```python
    def nb_noirs(image):
        nb = 0
        for ligne in image:
            for pixel in ligne:
                if pixel == 1:
                    nb = nb + 1
        return nb
    ```

    Pour l’image de l’énoncé : $26$ pixels noirs.

    **3.** `1 - pixel` échange $0$ et $1$ :

    ```python
    def negatif(image):
        return [[1 - pixel for pixel in ligne] for ligne in image]
    ```

    La compréhension construit de nouveaux tableaux : `image` n’est pas modifiée.

    **4.** La première ligne `00111100` représente $32 + 16 + 8 + 4 = 60$.

    ```python
    def ligne_en_octet(ligne):
        v = 0
        for bit in ligne:
            v = 2 * v + bit     # decalage a gauche, puis ajout du bit
        return v

    def compresser(image):
        return [ligne_en_octet(ligne) for ligne in image]
    ```

    `compresser(image)` renvoie `[60, 66, 165, 129, 165, 153, 66, 60]`.

    *Autre méthode :* sans compréhension, on part d’un tableau vide et on ajoute l’octet de chaque ligne.

    ```python
    def compresser(image):
        octets = []
        for ligne in image:
            octets.append(ligne_en_octet(ligne))
        return octets
    ```

    **5.** On retrouve les bits par divisions successives, du dernier (colonne $7$) au premier :

    ```python
    def octet_en_ligne(v):
        ligne = [0] * 8
        for i in range(7, -1, -1):
            ligne[i] = v % 2
            v = v // 2
        return ligne

    def decompresser(octets):
        return [octet_en_ligne(v) for v in octets]
    ```

    On stocke $8$ entiers au lieu de $64$ : chaque pixel n’occupe plus qu’un bit, au lieu d’un entier entier. C’est ainsi que les formats d’image en noir et blanc rangent les pixels.

### Après les chapitres 5 à 8 (Spécifier et mettre au point ses programmes ; Les algorithmes de tri ; La recherche dichotomique ; Les données en tables)

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Le classement d’un cross <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-S-6 }

Chapitres croisés : *Spécifier et mettre au point ses programmes ; Les algorithmes de tri ; La recherche dichotomique ; Les données en tables ; Algorithmique : le parcours séquentiel*

Les résultats d’un cross du lycée sont rangés dans une table : une liste de dictionnaires, un par coureur, avec son temps en secondes.

```python
coureurs = [{"nom": "Inès", "classe": "1G1", "temps": 754},
            {"nom": "Hugo", "classe": "1G2", "temps": 712},
            {"nom": "Léna", "classe": "1G1", "temps": 803},
            {"nom": "Tom", "classe": "1G3", "temps": 698},
            {"nom": "Maël", "classe": "1G2", "temps": 745},
            {"nom": "Sara", "classe": "1G3", "temps": 731}]
```

1.  On veut une fonction `plus_rapide(table)` qui renvoie le nom du coureur le plus rapide. Écrire sa **spécification** : prototype, docstring, précondition sur la table, postcondition sur le résultat.

2.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire cette fonction, en vérifiant la précondition par un `assert`. Écrire ensuite un **jeu de tests** d’au moins trois `assert`, dont une table d’un seul coureur et une table où le plus rapide est le dernier. Si tous les tests passent, la fonction est-elle forcément juste ?

3.  <span class="run" title="À programmer et tester sur machine">▶</span> Adapter le **tri par insertion** du cours pour écrire `trier_par_temps(table)`, qui trie la table **en place** par temps croissant. Donner l’ordre d’arrivée.

    ??? pouce "Coup de pouce"

        On déplace des fiches entières, mais on compare leurs temps : la condition du `while` devient `table[j]["temps"] > fiche["temps"]`.

4.  Au début du tour de boucle d’indice `i`, que peut-on affirmer des fiches d’indices $0$ à `i - 1` ? Comment s’appelle une telle propriété ?

5.  Après le tri, on construit **par compréhension** le tableau `temps` des temps, dans l’ordre. <span class="run" title="À programmer et tester sur machine">▶</span> Adapter la recherche dichotomique du cours en une fonction `position(t, x)` qui renvoie un indice de `x` dans le tableau trié `t`, ou `-1` si `x` est absent. Quelle est la place (1<sup>er</sup>, 2<sup>e</sup>…) du coureur qui a mis 745 secondes ? Combien de tours de boucle a-t-il fallu ? Même question pour 760 secondes.

??? corrige "Corrigé"

    **1.** et **2.**

    ```python
    def plus_rapide(table):
        """Renvoie le nom du coureur au plus petit temps.
        Precondition : table est une liste NON VIDE de fiches
        {"nom", "classe", "temps"}, les temps etant des entiers positifs.
        Postcondition : le temps de la fiche renvoyee est inferieur
        ou egal a celui de toutes les autres."""
        assert len(table) > 0, "table vide"
        meilleur = table[0]
        for fiche in table:
            if fiche["temps"] < meilleur["temps"]:
                meilleur = fiche
        return meilleur["nom"]

    assert plus_rapide(coureurs) == "Tom"
    assert plus_rapide([{"nom": "Ana", "classe": "1G1", "temps": 900}]) \
           == "Ana"
    assert plus_rapide([{"nom": "A", "classe": "1G1", "temps": 900},
                        {"nom": "B", "classe": "1G1", "temps": 600}]) == "B"
    ```

    Non : des tests réussis montrent seulement que la fonction est juste **sur ces exemples**. Un cas non testé (deux coureurs ex æquo, par exemple) peut encore poser problème. Les tests peuvent montrer la présence d’erreurs, jamais leur absence.

    **3.** On reprend le tri par insertion du cours ; on déplace des fiches entières, mais on compare leurs temps.

    ```python
    def trier_par_temps(table):
        for i in range(1, len(table)):
            fiche = table[i]
            j = i - 1
            while j >= 0 and table[j]["temps"] > fiche["temps"]:
                table[j + 1] = table[j]
                j = j - 1
            table[j + 1] = fiche
    ```

    Ordre d’arrivée : Tom ($698$), Hugo ($712$), Sara ($731$), Maël ($745$), Inès ($754$), Léna ($803$).

    **4.** Au début du tour d’indice `i`, les fiches d’indices $0$ à `i - 1` sont **rangées par temps croissant** : ce sont les `i` premières fiches de départ, remises dans l’ordre. C’est un **invariant de boucle** ; à la sortie (`i` vaut `len(table)`), il dit que toute la table est triée.

    **5.** `temps = [fiche["temps"] for fiche in coureurs]` vaut `[698, 712, 731, 745, 754, 803]`.

    ```python
    def position(t, x):
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

    Pour $745$ : `mil = 2` ($731 < 745$, `deb = 3`), puis `mil = 4` ($754 > 745$, `fin = 3`), puis `mil = 3` : trouvé, en **3 tours**. L’indice $3$ correspond à la **4<sup>e</sup> place**. Pour $760$ : `mil = 2`, puis `4`, puis `5` ($803 > 760$, `fin = 4`) ; la zone est vide après **3 tours** et la fonction renvoie `-1` : aucun coureur n’a ce temps.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Les doublons d’une liste d’inscriptions <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-S-7 }

Chapitres croisés : *Spécifier et mettre au point ses programmes (tests, débogage) ; Les algorithmes de tri (coût) ; Algorithmique : le parcours séquentiel ; Les types construits*

Les élèves s’inscrivent à un atelier avec leur identifiant. Certains se sont inscrits plusieurs fois.

```python
inscrits = ["lea.m", "tom.b", "ines.k", "hugo.p",
            "tom.b", "sara.d", "tom.b", "ines.k"]
```

1.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire une fonction `a_un_doublon(t)` qui renvoie `True` si deux cases du tableau `t` contiennent la même valeur, en comparant chaque case à toutes les suivantes. Combien de comparaisons fait-elle, au pire, pour un tableau de $1000$ identifiants ?

2.  Dans un tableau **trié**, deux valeurs égales sont forcément voisines. Un élève propose :

    ```python
    def a_un_doublon_trie(t):
        """t est trie ; renvoie True si deux cases sont egales."""
        for i in range(len(t)):
            if t[i] == t[i + 1]:
                return True
        return False
    ```

    Que se passe-t-il pour `a_un_doublon_trie(["a", "b", "c"])` ? Et pour `["a", "a", "c"]` ? Pourquoi ce second test ne suffisait-il pas à repérer l’erreur ? Corriger la fonction.

    ??? pouce "Coup de pouce"

        Pour le dernier indice `i`, que vaut `i + 1` ? Quel est le dernier indice valide d’un tableau ?

3.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire un jeu de tests de la fonction corrigée qui couvre les cas limites : tableau vide, un seul élément, doublon au début, doublon à la fin, aucun doublon.

4.  On trie d’abord une copie avec `sorted`, puis on appelle `a_un_doublon_trie`. Sachant que `sorted` fait de l’ordre de $n \log_2 n$ comparaisons, comparer le coût des deux méthodes pour $n = 1000$ (on prendra $\log_2 1000 \approx 10$).

5.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire une fonction `doublons(t)` qui, pour un tableau `t` trié, renvoie la liste des valeurs présentes au moins deux fois, chacune **une seule fois**. Que renvoie `doublons(sorted(inscrits))` ?

    ??? pouce "Coup de pouce"

        Parcourir les indices à partir de 1 et comparer `t[i]` à `t[i - 1]`. Avant d’ajouter une valeur, vérifier qu’elle n’est pas déjà la dernière de la liste résultat.

??? corrige "Corrigé"

    **1.**

    ```python
    def a_un_doublon(t):
        for i in range(len(t)):
            for j in range(i + 1, len(t)):
                if t[i] == t[j]:
                    return True
        return False
    ```

    Au pire (aucun doublon), la case $0$ est comparée aux $999$ suivantes, la case $1$ aux $998$ suivantes… soit $999 + 998 + \dots + 1 = \frac{1000 \times 999}{2} = 499\,500$ comparaisons.

    **2.** Pour `["a", "b", "c"]`, au dernier tour `i` vaut $2$ et `t[i + 1]` est `t[3]`, qui n’existe pas : `IndexError: list index out of range`. Pour `["a", "a", "c"]`, la fonction renvoie `True` dès `i = 0` et n’atteint jamais le dernier indice : le test passe alors que la fonction est fausse. Il faut s’arrêter à l’avant-dernière case :

    ```python
    def a_un_doublon_trie(t):
        for i in range(len(t) - 1):
            if t[i] == t[i + 1]:
                return True
        return False
    ```

    **3.**

    ```python
    assert not a_un_doublon_trie([])             # vide : range(-1) est vide
    assert not a_un_doublon_trie(["a"])          # un seul element
    assert a_un_doublon_trie(["a", "a", "b"])    # doublon au debut
    assert a_un_doublon_trie(["a", "b", "b"])    # doublon a la fin
    assert not a_un_doublon_trie(["a", "b", "c"])
    ```

    Le test « doublon à la fin » et le test « aucun doublon » auraient tous deux révélé l’erreur de la question 2.

    **4.** `a_un_doublon_trie(sorted(t))` fait environ $1000 \times 10 = 10\,000$ comparaisons pour le tri, puis au plus $999$ : environ $11\,000$ en tout, contre $499\,500$, soit environ $45$ fois moins.

    **5.**

    ```python
    def doublons(t):
        resultat = []
        for i in range(1, len(t)):
            nouveau = len(resultat) == 0 or resultat[-1] != t[i]
            if t[i] == t[i - 1] and nouveau:
                resultat.append(t[i])
        return resultat
    ```

    Le tableau trié est `["hugo.p", "ines.k", "ines.k", "lea.m", "sara.d", "tom.b", "tom.b", "tom.b"]` ; `doublons` renvoie `["ines.k", "tom.b"]`. Grâce au second test, `"tom.b"`, inscrit trois fois, n’apparaît qu’une fois.

### Après les chapitres 9 à 12 (Architecture des ordinateurs et systèmes d’exploitation ; Le Web : réseaux et interactions homme-machine ; Les algorithmes gloutons ; Les $k$ plus proches voisins)

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Les droits d’un fichier, en binaire <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-S-8 }

Chapitres croisés : *Architecture des ordinateurs et systèmes d’exploitation (droits) ; Le binaire et l’écriture des nombres ; Les types construits (chaînes)*

La commande `ls -l` affiche les droits d’un fichier sur 10 caractères, par exemple `-rwxr-x---` : le type, puis trois groupes de trois droits. On utilise l’écriture des droits en chiffres vue dans le cours *Architecture des ordinateurs et systèmes d’exploitation* (règle « Les droits en chiffres » : `r`$\,=4$, `w`$\,=2$, `x`$\,=1$, un chiffre par catégorie) : `-rwxr-x---` s’écrit `750`.

1.  Pour un fichier affiché `-rw-r-----` : qui peut le lire ? le modifier ? Écrire ses droits en trois chiffres.

2.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire une fonction `triplet_en_chiffre(triplet)` qui reçoit une chaîne de trois caractères comme `"r-x"` et renvoie le chiffre correspondant.

    ??? pouce "Coup de pouce"

        Comme pour lire un nombre binaire de gauche à droite : on part de `v = 0` et, pour chaque caractère, `v` devient `2 * v` plus le bit ($0$ pour `-`, $1$ sinon).

3.  <span class="run" title="À programmer et tester sur machine">▶</span> En déduire une fonction `code_droits(ligne)` qui reçoit les 10 caractères affichés par `ls -l` et renvoie la chaîne des trois chiffres (`code_droits("-rwxr-x---")` renvoie `"750"`). Que renvoie-t-elle pour `drwxr-xr-x` ?

4.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire la fonction réciproque `droits(code)` : `droits("754")` renvoie `"rwxr-xr--"`. Vérifier, avec trois boucles imbriquées, que `code_droits("-" + droits(code))` redonne `code` pour les $512$ codes possibles.

    ??? pouce "Coup de pouce"

        Pour un chiffre `d` : le bit de poids $4$ est `d // 4`, celui de poids $2$ est `(d // 2) % 2`, celui de poids $1$ est `d % 2`.

5.  Pourquoi y a-t-il exactement $512$ réglages différents des droits d’un fichier ? Pourquoi chaque chiffre ne dépasse-t-il jamais $7$ ?

??? corrige "Corrigé"

    **1.** `-rw-r-----` : le propriétaire peut le lire et le modifier, les membres du groupe peuvent seulement le lire, les autres n’ont aucun droit. Code : `110 100 000`, soit **640**.

    **2.** et **3.**

    ```python
    def triplet_en_chiffre(triplet):
        v = 0
        for c in triplet:
            bit = 0
            if c != "-":
                bit = 1
            v = 2 * v + bit
        return v

    def code_droits(ligne):
        proprietaire = triplet_en_chiffre(ligne[1:4])
        groupe = triplet_en_chiffre(ligne[4:7])
        autres = triplet_en_chiffre(ligne[7:10])
        return str(proprietaire) + str(groupe) + str(autres)
    ```

    `code_droits("drwxr-xr-x")` renvoie `"755"` (le premier caractère, `d` pour un dossier, est ignoré).

    **4.**

    ```python
    def chiffre_en_triplet(d):
        triplet = ""
        if d // 4 == 1:
            triplet = triplet + "r"
        else:
            triplet = triplet + "-"
        if (d // 2) % 2 == 1:
            triplet = triplet + "w"
        else:
            triplet = triplet + "-"
        if d % 2 == 1:
            triplet = triplet + "x"
        else:
            triplet = triplet + "-"
        return triplet

    def droits(code):
        resultat = ""
        for c in code:
            resultat = resultat + chiffre_en_triplet(int(c))
        return resultat

    for a in range(8):
        for b in range(8):
            for c in range(8):
                code = str(a) + str(b) + str(c)
                assert code_droits("-" + droits(code)) == code
    ```

    **5.** Il y a $9$ droits, chacun présent ou absent : $2^9 = 512$ réglages. Un chiffre code $3$ bits, et le plus grand nombre de $3$ bits est $\texttt{111}_2 = 7$. Écrire un nombre avec des chiffres de $0$ à $7$, c’est l’écrire en base $8$ (l’**octal**), qui regroupe les bits par paquets de $3$ comme l’hexadécimal les regroupe par $4$.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 9</span> — Un conseil de film <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-S-9 }

Chapitres croisés : *Le Web : réseaux et interactions homme-machine (formulaire, URL, cookies) ; Les données en tables ; Les $k$ plus proches voisins*

Le site `https://www.cine.mc` demande au visiteur de noter de $0$ à $10$ son goût pour l’action, l’humour et l’émotion, puis lui conseille des films.

```html
<form action="/conseil" method="get">
    <input type="number" name="action">
    <input type="number" name="humour">
    <input type="number" name="emotion">
    <button type="submit">Me conseiller</button>
</form>
```

1.  Un visiteur saisit $8$, $2$ et $6$. Écrire l’URL demandée au serveur.

2.  <span class="run" title="À programmer et tester sur machine">▶</span> Le serveur doit retrouver les réponses dans l’URL. La méthode `split` découpe une chaîne selon un séparateur : `"a=1&b=2".split("&")` renvoie `["a=1", "b=2"]`. Écrire une fonction `lire_reponses(url)` qui renvoie le dictionnaire `{"action": 8, "humour": 2, "emotion": 6}` (avec des entiers).

    ??? pouce "Coup de pouce"

        Trois découpages successifs : selon `"?"` (on garde la partie de droite), selon `"&"`, puis chaque paire selon `"="`.

3.  Le site connaît ces films, notés selon les mêmes critères :

    ```python
    films = [
        {"titre": "Les Pirates du lagon", "genre": "aventure",
         "action": 9, "humour": 4, "emotion": 3},
        {"titre": "Mission Mistral", "genre": "aventure",
         "action": 8, "humour": 1, "emotion": 5},
        {"titre": "Le Dîner raté", "genre": "comédie",
         "action": 1, "humour": 9, "emotion": 3},
        {"titre": "Coloc en folie", "genre": "comédie",
         "action": 3, "humour": 8, "emotion": 2},
        {"titre": "La Lettre", "genre": "drame",
         "action": 1, "humour": 2, "emotion": 9},
        {"titre": "Après l'orage", "genre": "drame",
         "action": 4, "humour": 1, "emotion": 8},
        {"titre": "Course contre la nuit", "genre": "aventure",
         "action": 9, "humour": 2, "emotion": 7}]
    ```

    Calculer à la main la distance au carré entre le profil $(8 ; 2 ; 6)$ et les films *Mission Mistral* et *Après l’orage*.

4.  <span class="run" title="À programmer et tester sur machine">▶</span> En reprenant les fonctions du cours, écrire `conseils(films, profil, k)`, qui renvoie les titres des `k` films les plus proches du profil, et `genre_conseille(films, profil, k)`, qui renvoie le genre majoritaire parmi eux. Que conseille-t-on au visiteur pour $k = 3$ ?

5.  Un second visiteur a le profil $(3 ; 4 ; 7)$. Quel genre lui conseille-t-on pour $k = 3$ ? Avec $k = 4$, que se passe-t-il lors du vote, et que renvoie la fonction `vote` du cours ?

6.  Pour ne pas redemander les notes, le serveur répond avec l’en-tête `Set-Cookie: profil=8-2-6; Max-Age=2592000`. Où ce profil est-il mémorisé ? Que contient la requête quand le visiteur revient sur le site, deux semaines plus tard ? Est-ce grave si le visiteur modifie ce cookie ?

??? corrige "Corrigé"

    **1.** `https://www.cine.mc/conseil?action=8&humour=2&emotion=6` : avec `get`, les paires `name=valeur` suivent un `?` et sont séparées par `&`.

    **2.**

    ```python
    def lire_reponses(url):
        reponses = {}
        for paire in url.split("?")[1].split("&"):
            morceaux = paire.split("=")
            reponses[morceaux[0]] = int(morceaux[1])
        return reponses
    ```

    **3.** *Mission Mistral* : $(8 - 8)^2 + (1 - 2)^2 + (5 - 6)^2 = 0 + 1 + 1 = 2$. *Après l’orage* : $(4 - 8)^2 + (1 - 2)^2 + (8 - 6)^2 = 16 + 1 + 4 = 21$.

    **4.** On adapte `distance`, `k_plus_proches` et `vote` du cours (distance au carré, puisqu’on ne fait que comparer) :

    ```python
    def distance2(film, profil):
        somme = 0
        for critere in ["action", "humour", "emotion"]:
            somme = somme + (film[critere] - profil[critere]) ** 2
        return somme

    def k_plus_proches(films, profil, k):
        dists = []
        for film in films:
            dists.append((distance2(film, profil), film))
        dists.sort(key=lambda couple: couple[0])
        return [film for (d, film) in dists[:k]]

    def conseils(films, profil, k):
        return [film["titre"] for film in k_plus_proches(films, profil, k)]

    def genre_conseille(films, profil, k):
        voisins = k_plus_proches(films, profil, k)
        return vote([film["genre"] for film in voisins])
    ```

    Distances au carré : *Mission Mistral* 2, *Course contre la nuit* 2, *Les Pirates du lagon* 14, *Après l’orage* 21, *La Lettre* 58, *Coloc en folie* 77, *Le Dîner raté* 107. Pour $k = 3$ : *Mission Mistral*, *Course contre la nuit*, *Les Pirates du lagon*, trois films d’**aventure**.

    **5.** Distances au carré pour $(3 ; 4 ; 7)$ : *Après l’orage* 11, *La Lettre* 12, *Mission Mistral* 38, *Course contre la nuit* 40, puis les autres. Pour $k = 3$ : deux drames et une aventure, on conseille un **drame**. Pour $k = 4$ : deux drames et deux aventures, c’est une **égalité**. La fonction `vote` du cours ne remplace la classe retenue que par une classe *strictement* plus fréquente : elle garde la première rencontrée, ici `"drame"`, celle du plus proche voisin. Ce choix n’a rien d’évident : il vaut mieux choisir $k$ pour limiter les égalités, ou les départager explicitement.

    **6.** Le profil est mémorisé **dans le client** (le navigateur). Deux semaines plus tard, le cookie est toujours là ($2\,592\,000$ secondes font $30$ jours) : la requête contient l’en-tête `Cookie: profil=8-2-6`, que le navigateur ajoute de lui-même. Si le visiteur modifie ce cookie, il ne change que ses propres conseils : ce n’est pas grave. Le serveur doit seulement vérifier que les valeurs reçues sont bien des nombres de $0$ à $10$ avant de s’en servir, comme pour toute donnée venue du client.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 10</span> — La soirée cinéma <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-S-10 }

Chapitres croisés : *Les algorithmes gloutons ; Les algorithmes de tri ; Le binaire et l’écriture des nombres ; Les types construits*

Une soirée dure au plus $240$ minutes. Chaque film est un p-uplet `(titre, durée en minutes, points d’envie)`, et l’on veut le plus de points possible sans dépasser $240$ minutes.

```python
soiree = [("Les Pirates du lagon", 60, 6), ("Le Dîner raté", 120, 9),
          ("La Lettre", 70, 5), ("Coloc en folie", 85, 6),
          ("Mission Mistral", 90, 8)]
```

1.  **Glouton n<sup>o</sup> 1** : on range les films par points décroissants, puis on prend chaque film qui tient encore dans la soirée. Dérouler à la main : quels films, combien de points ?

2.  **Glouton n<sup>o</sup> 2** : même méthode, mais en rangeant les films par **points par minute** décroissants. Dérouler à la main.

3.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire `soiree_gloutonne(duree_max, ordre)`, qui reçoit les films déjà rangés dans l’ordre du critère et renvoie la liste des titres choisis. Vérifier les deux réponses précédentes.

    ??? pouce "Coup de pouce"

        Comme au TP des algorithmes gloutons, écrire une fonction `points(f)` qui renvoie `f[2]`, le nombre de points du film `f` ; l’ordre se construit alors avec `sorted(soiree, key=points, reverse=True)`. Pour le second critère, une fonction `points_par_minute(f)` renvoie `f[2] / f[1]`.

4.  <span class="run" title="À programmer et tester sur machine">▶</span> Une soirée est un choix de films : chaque film est pris ou non, c’est un bit. Les $2^5 = 32$ soirées possibles correspondent donc aux entiers de $0$ à $31$ écrits en binaire. Écrire `meilleure_soiree(films, duree_max)` qui les essaie toutes et renvoie la meilleure. Les deux gloutons étaient-ils optimaux ?

    ??? pouce "Coup de pouce"

        Pour l’entier `code`, le film d’indice `i` est pris si le bit de poids $2^i$ vaut 1, c’est-à-dire si `(code // 2 ** i) % 2 == 1`.

5.  Avec $40$ films, combien de soirées la force brute devrait-elle essayer ? Pourquoi utilise-t-on quand même des algorithmes gloutons ?

??? corrige "Corrigé"

    **1.** Par points décroissants : *Le Dîner raté* (9 points, 120 min) est pris, il reste 120 min ; *Mission Mistral* (8 points, 90 min) est pris, il reste 30 min ; plus aucun film ne tient. Soirée de 210 min, **17 points**.

    **2.** Points par minute : *Les Pirates du lagon* $0{,}100$ ; *Mission Mistral* $0{,}089$ ; *Le Dîner raté* $0{,}075$ ; *La Lettre* $0{,}071$ ; *Coloc en folie* $0{,}071$ (un peu moins : $6/85 < 5/70$). On prend *Les Pirates du lagon* (reste 180 min), puis *Mission Mistral* (reste 90 min) ; *Le Dîner raté* ne tient pas ; on prend *La Lettre* (reste 20 min). Soirée de 220 min, **19 points**.

    **3.**

    ```python
    def soiree_gloutonne(duree_max, ordre):
        choisis = []
        reste = duree_max
        for (titre, duree, pts) in ordre:
            if duree <= reste:
                choisis.append(titre)
                reste = reste - duree
        return choisis

    def points(f):
        return f[2]

    def points_par_minute(f):
        return f[2] / f[1]

    par_points = sorted(soiree, key=points, reverse=True)
    soiree_gloutonne(240, par_points)
    # Le Diner rate, puis Mission Mistral
    par_minute = sorted(soiree, key=points_par_minute, reverse=True)
    soiree_gloutonne(240, par_minute)
    # ['Les Pirates du lagon', 'Mission Mistral', 'La Lettre']
    ```

    **4.**

    ```python
    def meilleure_soiree(films, duree_max):
        n = len(films)
        meilleur_choix = []
        meilleurs_points = 0
        for code in range(2 ** n):
            choix = []
            duree_totale = 0
            total_points = 0
            for i in range(n):
                if (code // 2 ** i) % 2 == 1:      # bit numero i du code
                    titre, duree, pts = films[i]
                    choix.append(titre)
                    duree_totale = duree_totale + duree
                    total_points = total_points + pts
            if duree_totale <= duree_max and total_points > meilleurs_points:
                meilleur_choix = choix
                meilleurs_points = total_points
        return meilleur_choix, meilleurs_points
    ```

    La meilleure soirée est *Les Pirates du lagon*, *Coloc en folie* et *Mission Mistral* : 235 min et **20 points**. Aucun des deux gloutons n’était optimal (17 et 19 points), même si le second en était proche.

    **5.** Avec $40$ films, il faudrait essayer $2^{40} = 1\,099\,511\,627\,776$ soirées, plus de mille milliards : chaque film de plus double le travail. Un glouton ne parcourt les films qu’une fois, après un tri : il répond instantanément, avec une solution souvent bonne mais sans garantie d’être la meilleure.
