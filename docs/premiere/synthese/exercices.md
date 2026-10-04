# Exercices

<p class="sous-titre">Problèmes de synthèse et exercices type bac</p>

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

        On donne une version testée de chaque fonction ; d’autres écritures correctes sont possibles. Le fichier complet, `corrige_synthese_premiere.py`, est en ligne : [`github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/premiere/synthese`](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/premiere/synthese).

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

    $12 + (-12)$ donne bien $0$ ($12 + 244 = 256$, et $256 \bmod 256 = 0$ : la retenue qui déborde est oubliée). Mais $100 + 50$ renvoie $-106$ et $127 + 1$ renvoie $-128$ : le vrai résultat ($150$, $128$) dépasse $127$, le plus grand entier codable. Son code a un bit de poids fort à $1$, qui est lu comme le signe d’un négatif. C’est un **dépassement de capacité** : la machine ne signale rien, c’est au programmeur d’y penser.

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

    `meilleur(notes)` renvoie `("Zoé", 15.0)`.

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
