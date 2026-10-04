# TP et projets

<p class="sous-titre">Le binaire et l'écriture des nombres</p>

## <span class="etiquette">TP</span> Programmer l’arithmétique binaire

*des convertisseurs à l’additionneur et au multiplicateur*

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/02-tp-arithmetique-binaire){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-02-tp-arithmetique-binaire.zip){ .md-button }

!!! consignes "Mode d’emploi"

    - Objectif : **reprogrammer ce que vous savez faire à la main** (conversions, complément à deux), puis construire l’addition et la multiplication **à partir de simples portes logiques**, comme dans un processeur.

    - Tous les nombres binaires sont des **chaînes** de `"0"` et de `"1"`, écrites comme d’habitude (bit de poids fort à gauche) : `"1011"` représente $11$.

    - **Interdit** : `bin`, `int(…, 2)`, `format`… Ils ne servent qu’à *vérifier* vos résultats.

    - Les questions \[ à la main \]  se traitent sur le cahier ; les questions \[ sur machine \]  dans le fichier Python.

    - Partez du fichier `activite_arithmetique_binaire_depart.py` : chaque partie a sa fonction de tests (`tester_A()`, `tester_B()`…) à appeler dès que la partie est terminée.

    - Niveau : ★ échauffement ★★ classique ★★★ défi.

    - Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la [charte d’usage de l’IA](../charte.md).

!!! remarque "Remarque"

    **Boîte à outils sur les chaînes.** Avec `s = "1011"` :

    - `len(s)` vaut `4` ; `s[0]` vaut `"1"` (premier caractère) ; `s[len(s) - 1]` vaut `"1"` (dernier) ;

    - `"0" + s` vaut `"01011"` (concaténation) ; `"0" * 3` vaut `"000"` (répétition) ;

    - `s[1:]` vaut `"011"` (tout sauf le premier caractère) ;

    - `for c in s:` parcourt les caractères de gauche à droite ; `for i in range(len(s) - 1, -1, -1):` parcourt les *indices* de droite à gauche (utile pour les retenues) ;

    - `str(1)` vaut `"1"` et `int("1")` vaut `1`.

## Les convertisseurs

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — Du binaire vers le décimal <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-tp-1-1 }

\[ sur machine \]  Écrire `binaire_vers_decimal(s)`. Méthode de Horner : on lit les bits de gauche à droite ; à chaque bit `c`, on fait `n = 2 * n + int(c)`.

\[ à la main \]  Avant de coder, dérouler cette méthode à la main sur `"1011"` (valeurs successives de `n`).

```text
>>> binaire_vers_decimal("1011")
11
```

??? corrige "Corrigé"

    À la main sur `"1011"` : `n` vaut successivement $0 \to 1 \to 2 \to 5 \to 11$.

    ```python
    def binaire_vers_decimal(s):
        n = 0
        for c in s:
            n = 2 * n + int(c)
        return n
    ```

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 2</span> — Du décimal vers le binaire <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-tp-1-2 }

\[ sur machine \]  Écrire `decimal_vers_binaire(n)` par divisions successives par 2 : chaque reste `n % 2` est un bit, **ajouté à gauche** de la chaîne déjà construite. Attention au cas `n = 0`, qui doit renvoyer `"0"`.

```text
>>> decimal_vers_binaire(13)
'1101'
```

??? corrige "Corrigé"

    Le reste est ajouté **à gauche** : le premier reste obtenu est le bit des unités.

    ```python
    def decimal_vers_binaire(n):
        if n == 0:
            return "0"
        s = ""
        while n > 0:
            s = str(n % 2) + s
            n = n // 2
        return s
    ```

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 3</span> — Compléter à gauche <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-tp-1-3 }

\[ sur machine \]  Écrire `completer(s, nb_bits)` qui ajoute des `"0"` à gauche de `s` jusqu’à atteindre `nb_bits` caractères (et ne change rien si `s` est déjà assez long).

```text
>>> completer("101", 8)
'00000101'
```

??? corrige "Corrigé"

    ```python
    def completer(s, nb_bits):
        while len(s) < nb_bits:
            s = "0" + s
        return s
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 4</span> — Du binaire vers l’hexadécimal <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-tp-1-4 }

\[ sur machine \]  Écrire `binaire_vers_hexa(s)` : compléter `s` pour que sa longueur soit un multiple de 4, puis convertir chaque paquet de 4 bits (`s[i:i + 4]`) en un chiffre de `"0123456789ABCDEF"`.

```text
>>> binaire_vers_hexa("11111010")
'FA'
```

??? corrige "Corrigé"

    Chaque paquet de 4 bits est converti par `binaire_vers_decimal`, qui donne l’indice du chiffre dans `chiffres`.

    ```python
    def binaire_vers_hexa(s):
        chiffres = "0123456789ABCDEF"
        while len(s) % 4 != 0:
            s = "0" + s
        h = ""
        for i in range(0, len(s), 4):
            h = h + chiffres[binaire_vers_decimal(s[i:i + 4])]
        return h
    ```

## Le complément à deux

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 5</span> — Inverser les bits <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-tp-1-5 }

\[ sur machine \]  Écrire `inverser(s)` qui remplace chaque `"0"` par `"1"` et réciproquement.

??? corrige "Corrigé"

    ```python
    def inverser(s):
        r = ""
        for c in s:
            if c == "0":
                r = r + "1"
            else:
                r = r + "0"
        return r
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Ajouter 1 : la retenue qui se propage <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-tp-1-6 }

\[ à la main \]  Poser à la main `0111 + 1` puis `1111 + 1` sur 4 bits. Recopier et compléter la règle : « en partant de la droite, tant que le bit vaut `1`, on le remplace par … et la retenue … ; au premier `0` rencontré, on le remplace par … et la retenue … ».

\[ sur machine \]  Écrire `incrementer(s)` qui ajoute 1 à `s` **sur le même nombre de bits** (la retenue qui sort à gauche est perdue). On parcourt les indices de droite à gauche avec un booléen `retenue`, qui vaut `True` au départ.

```text
>>> incrementer("0111")
'1000'
>>> incrementer("1111")
'0000'
```

*Gardez cette fonction précieusement : c’est exactement ce que fait un registre de la machine à billes Turing Tumble (atelier associé).*

??? corrige "Corrigé"

    $\texttt{0111} + 1 = \texttt{1000}$ et $\texttt{1111} + 1 = \texttt{(1)0000}$. Règle : tant que le bit vaut `1`, on le remplace par `0` et la retenue **continue** ; au premier `0`, on le remplace par `1` et la retenue **s’arrête** ; les bits suivants sont recopiés.

    ```python
    def incrementer(s):
        r = ""
        retenue = True
        for i in range(len(s) - 1, -1, -1):
            if retenue and s[i] == "1":
                r = "0" + r        # 1 + 1 = 10 : on pose 0, la retenue continue
            elif retenue and s[i] == "0":
                r = "1" + r        # 0 + 1 = 1 : la retenue s'arrete
                retenue = False
            else:
                r = s[i] + r       # plus de retenue : on recopie
        return r
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Coder un entier relatif <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-tp-1-7 }

\[ sur machine \]  Écrire `complement_a_deux(n, nb_bits)` :

- si $\texttt{n} \geqslant 0$ : écrire `n` en binaire et compléter à `nb_bits` ;

- sinon : écrire $|\texttt{n}|$ sur `nb_bits`, **inverser**, puis **ajouter 1** (réutiliser vos fonctions !).

```text
>>> complement_a_deux(-5, 8)
'11111011'
```

??? corrige "Corrigé"

    ```python
    def complement_a_deux(n, nb_bits):
        if n >= 0:
            return completer(decimal_vers_binaire(n), nb_bits)
        return incrementer(inverser(completer(decimal_vers_binaire(-n), nb_bits)))
    ```

    Remarque : pour $-128$ sur 8 bits, on obtient bien `10000000`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Décoder un entier relatif <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-tp-1-8 }

\[ sur machine \]  Écrire `decoder_c2(s)`. Si le bit de poids fort est `0`, c’est un entier positif ordinaire. Sinon, la valeur est celle de `s` lu comme un entier positif, **moins** $2^{n}$, où $n$ est le nombre de bits.

\[ à la main \]  Vérifier la règle à la main sur `"11111011"` : $251 - 256 = \dots$

```text
>>> decoder_c2("11111011")
-5
```

??? corrige "Corrigé"

    $\texttt{11111011}_2 = 251$ et $251 - 256 = -5$.

    ```python
    def decoder_c2(s):
        if s[0] == "0":
            return binaire_vers_decimal(s)
        return binaire_vers_decimal(s) - 2 ** len(s)
    ```

## Les portes logiques

Dans cette partie, un bit est une chaîne d’un caractère : `"0"` ou `"1"`.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 9</span> — Les trois portes de base <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-tp-1-9 }

\[ sur machine \]  Écrire `non(a)`, `et(a, b)` et `ou(a, b)` avec des `if`. Chacune renvoie `"0"` ou `"1"`.

??? corrige "Corrigé"

    ```python
    def non(a):
        if a == "0":
            return "1"
        return "0"

    def et(a, b):
        if a == "1" and b == "1":
            return "1"
        return "0"

    def ou(a, b):
        if a == "1" or b == "1":
            return "1"
        return "0"
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 10</span> — Construire le OU exclusif <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-tp-1-10 }

Le OU exclusif (*xor*) vaut `"1"` lorsque **exactement un** des deux bits vaut `"1"`.

1.  \[ à la main \]  Dresser sa table de vérité.

2.  \[ sur machine \]  Écrire `xor(a, b)` **sans aucun `if`**, en combinant seulement `non`, `et` et `ou`. Indice : « `a` et pas `b`, ou bien pas `a` et `b` ».

3.  \[ sur machine \]  Afficher sa table de vérité avec deux boucles imbriquées `for a in "01":` et `for b in "01":`.

??? corrige "Corrigé"

    **1.** Table : $(0,0) \mapsto 0$, $(0,1) \mapsto 1$, $(1,0) \mapsto 1$, $(1,1) \mapsto 0$.

    **2. et 3.**

    ```python
    def xor(a, b):
        return ou(et(a, non(b)), et(non(a), b))

    for a in "01":
        for b in "01":
            print(a, b, xor(a, b))
    ```

## Les additionneurs

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 11</span> — Le demi-additionneur <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-tp-1-11 }

\[ à la main \]  Poser les quatre additions d’un bit : $0+0$, $0+1$, $1+0$, $1+1$. Écrire chaque résultat **sur deux bits** (retenue, somme). Reconnaître ensuite la porte qui donne la retenue et celle qui donne la somme.

![](../figures/9208daa0d68e5202.svg){ .tikz loading=lazy }

\[ sur machine \]  Écrire `demi_additionneur(a, b)` qui renvoie la chaîne `retenue + somme`. C’est donc exactement $a + b$ écrit en binaire sur deux bits.

```text
>>> demi_additionneur("1", "1")
'10'
```

??? corrige "Corrigé"

    $0+0 = \texttt{00}$, $0+1 = \texttt{01}$, $1+0 = \texttt{01}$, $1+1 = \texttt{10}$. La retenue (bit de gauche) est la table du **ET** ; la somme (bit de droite) est celle du **OU exclusif**.

    ```python
    def demi_additionneur(a, b):
        return et(a, b) + xor(a, b)
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 12</span> — L’additionneur complet <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-tp-1-12 }

Pour additionner des nombres de plusieurs bits, chaque colonne reçoit **trois** bits : `a`, `b` et la retenue `r` venue de la colonne de droite. L’additionneur complet se construit avec **deux demi-additionneurs** et une porte OU :

![](../figures/1ce44473f554a47a.svg){ .tikz loading=lazy }

\[ sur machine \]  Écrire `additionneur_complet(a, b, r)` qui renvoie `retenue + somme` de $a+b+r$, en appelant deux fois `demi_additionneur`. Si `d1 = demi_additionneur(a, b)`, alors `d1[0]` est la retenue et `d1[1]` la somme.

```text
>>> additionneur_complet("1", "0", "1")
'10'
```

??? corrige "Corrigé"

    Les deux retenues intermédiaires ne peuvent pas valoir `1` en même temps. Un OU suffit donc pour obtenir la retenue sortante.

    ```python
    def additionneur_complet(a, b, r):
        d1 = demi_additionneur(a, b)
        d2 = demi_additionneur(d1[1], r)
        return ou(d1[0], d2[0]) + d2[1]
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 13</span> — L’additionneur $n$ bits <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-tp-1-13 }

En chaînant $n$ additionneurs complets (la retenue sortante de l’un entre dans le suivant, à gauche), on additionne deux nombres de $n$ bits. C’est l’**additionneur à propagation de retenue** des processeurs.

\[ sur machine \]  Écrire `additionner(s1, s2)` (deux chaînes de même longueur $n$). Le résultat fait $n+1$ bits : la dernière retenue est placée à gauche.

```text
>>> additionner("0101", "0110")     # 5 + 6
'01011'
```

\[ à la main \]  Combien d’appels à `additionneur_complet` faut-il pour additionner deux nombres de 64 bits ?

??? corrige "Corrigé"

    ```python
    def additionner(s1, s2):
        r = ""
        retenue = "0"
        for i in range(len(s1) - 1, -1, -1):
            res = additionneur_complet(s1[i], s2[i], retenue)
            r = res[1] + r
            retenue = res[0]
        return retenue + r
    ```

    Pour deux nombres de 64 bits : **64** appels, un par colonne.

## La soustraction

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 14</span> — Soustraire, c’est additionner l’opposé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-tp-1-14 }

En complément à deux, $a - b = a + (-b)$, et $-b$ s’obtient en inversant les bits de $b$ puis en ajoutant 1. Le processeur n’a donc **pas besoin d’un circuit de soustraction** !

\[ sur machine \]  Écrire `soustraire(s1, s2)` en une ligne, avec `additionner`, `inverser` et `incrementer`. On garde $n$ bits : la retenue finale est ignorée (`[1:]`).

```text
>>> soustraire("0010", "0111")      # 2 - 7
'1011'
>>> decoder_c2("1011")
-5
```

??? corrige "Corrigé"

    ```python
    def soustraire(s1, s2):
        return additionner(s1, incrementer(inverser(s2)))[1:]
    ```

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 15</span> — Détecter le dépassement <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-tp-1-15 }

Sur 4 bits, le complément à deux représente les entiers de $-8$ à $7$.

1.  \[ à la main \]  Calculer `0111 + 0001` sur 4 bits et décoder le résultat. Que s’est-il passé ?

2.  \[ à la main \]  Montrer que la somme de deux nombres de signes *contraires* ne peut jamais dépasser.

3.  \[ sur machine \]  En déduire `depassement(s1, s2)` qui renvoie `True` si `s1` et `s2` ont le même bit de signe et que leur somme (sur $n$ bits) a un bit de signe différent.

??? corrige "Corrigé"

    **1.** $\texttt{0111} + \texttt{0001} = \texttt{1000}$, qui se décode en $-8$ : on a obtenu $7 + 1 = -8$. Le vrai résultat, $8$, sort de la plage $[-8 \,;\, 7]$ et « déborde » sur le bit de signe.

    **2.** Si $x \geqslant 0$ et $y < 0$, alors $y \leqslant x + y < x$ : la somme est comprise entre deux nombres représentables, donc elle est représentable.

    **3.**

    ```python
    def depassement(s1, s2):
        somme = additionner(s1, s2)[1:]
        return s1[0] == s2[0] and somme[0] != s1[0]
    ```

## La multiplication

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 16</span> — Multiplier par 2, 4, 8… <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-tp-1-16 }

\[ à la main \]  Que devient l’écriture binaire d’un nombre quand on le multiplie par 2 ? par $2^k$ ? (Comparer avec la multiplication par 10 en décimal.)

\[ sur machine \]  Écrire `decaler(s, k)` qui renvoie `s` multiplié par $2^k$.

??? corrige "Corrigé"

    Multiplier par 2 revient à ajouter un `0` à droite, tous les bits montant d’un rang. Multiplier par $2^k$ revient à ajouter $k$ zéros, exactement comme $\times 10$ en décimal.

    ```python
    def decaler(s, k):
        return s + "0" * k
    ```

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 17</span> — Le multiplicateur <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-tp-1-17 }

\[ à la main \]  Poser la multiplication `1101 × 1011` comme à l’école primaire. Constater que chaque ligne intermédiaire est soit `0`, soit `1101` décalé : en binaire, **on n’a jamais besoin des tables de multiplication** !

\[ sur machine \]  Écrire `multiplier(s1, s2)` (entiers positifs) :

- le résultat tient sur $n =$ `len(s1) + len(s2)` bits : partir de `"0" * n` ;

- parcourir les bits de `s2` de droite à gauche (rang `k` = 0, 1, 2…) ;

- si le bit vaut `"1"`, ajouter au résultat `decaler(s1, k)` complété à $n$ bits (garder $n$ bits avec `[1:]`).

```text
>>> multiplier("1101", "1011")      # 13 * 11
'10001111'
```

??? corrige "Corrigé"

    Lignes intermédiaires de `1101 × 1011` : `1101`, `11010`, `000000`, `1101000`. Leur somme vaut `10001111`, soit $13 \times 11 = 143$.

    ```python
    def multiplier(s1, s2):
        n = len(s1) + len(s2)
        resultat = "0" * n
        k = 0
        for i in range(len(s2) - 1, -1, -1):
            if s2[i] == "1":
                partiel = completer(decaler(s1, k), n)
                resultat = additionner(resultat, partiel)[1:]
            k = k + 1
        return resultat
    ```

    Le produit de deux nombres de $p$ et $q$ bits est strictement inférieur à $2^{p+q}$ : il tient toujours sur $p+q$ bits, et la retenue retirée par `[1:]` vaut toujours `0`.

## Comme la machine à billes

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 18</span> — Additionner avec des billes <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-tp-1-18 }

Dans la machine Turing Tumble, un registre de bits reçoit des billes : **chaque bille ajoute 1**.

1.  \[ sur machine \]  Écrire `ajouter_billes(registre, nb_billes)` qui appelle `incrementer` autant de fois qu’il y a de billes. Vérifier que `ajouter_billes("0101", 6)` donne `"1011"`.

2.  Pour calculer $A + B$ sur 32 bits, combien d’appels à `incrementer` faut-il dans le pire cas ? Et combien d’appels à `additionneur_complet` avec `additionner` ? Conclure : pourquoi les processeurs n’additionnent-ils pas « bille par bille » ?

??? corrige "Corrigé"

    **1.**

    ```python
    def ajouter_billes(registre, nb_billes):
        for i in range(nb_billes):
            registre = incrementer(registre)
        return registre
    ```

    **2.** Sur 32 bits, $B$ peut valoir jusqu’à $2^{32} - 1 \approx 4{,}3$ milliards : autant d’appels à `incrementer`. `additionner` n’utilise que **32** additionneurs complets, quel que soit $B$. Le coût bille par bille est proportionnel à la *valeur* de $B$, alors que celui de l’additionneur est proportionnel à son *nombre de bits*.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 19</span> — Le convertisseur d’un assistant d’IA <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-tp-1-19 }

Un élève demande à un assistant d’IA une fonction de conversion. Voici la réponse :

« Voici la fonction, testée sur plusieurs valeurs :

```python
def decimal_vers_binaire(n):
    if n == 0:
        return "0"
    s = ""
    while n > 0:
        s = s + str(n % 2)
        n = n // 2
    return s

assert decimal_vers_binaire(0) == "0"
assert decimal_vers_binaire(5) == "101"
assert decimal_vers_binaire(7) == "111"
assert decimal_vers_binaire(9) == "1001"
```

Les quatre tests passent, la fonction est donc correcte. »

1.  \[ sur machine \]  Les tests passent-ils vraiment ? Essayer `decimal_vers_binaire(6)`. La fonction est-elle correcte ?

2.  Localiser et corriger l’erreur.

3.  Qu’ont en commun `"101"`, `"111"` et `"1001"` ? Pourquoi ces tests étaient-ils incapables de détecter l’erreur ? Proposer un test qui l’aurait détectée. Que penser de la phrase « les tests passent, la fonction est donc correcte » ?

??? corrige "Corrigé"

    **1.** Les quatre tests passent bien, mais `decimal_vers_binaire(6)` renvoie `"011"` au lieu de `"110"`. La fonction est fausse.

    **2.** Les bits sont ajoutés *à droite* alors que le premier reste est le bit des unités. Il faut écrire `s = str(n % 2) + s`.

    **3.** `"101"`, `"111"` et `"1001"` (et `"0"`) sont des **palindromes** : écrits à l’envers, ils ne changent pas. Des tests qui ne portent que sur des palindromes ne peuvent pas détecter une chaîne retournée. N’importe quel nombre non palindrome, par exemple 6, 13 ou 2, l’aurait révélé. Le succès d’un jeu de tests ne garantit pas la correction d’un programme : il faut *choisir* des tests capables de faire échouer les erreurs plausibles.

## <span class="etiquette">Atelier</span> Turing Tumble : calculer avec des billes

!!! consignes "Mode d’emploi"

    - **Turing Tumble** est un ordinateur *mécanique* : des billes tombent sur des pièces qui les aiguillent. Pas d’électricité, mais les mêmes idées que dans un processeur.

    - Un groupe manipule le **plateau** ; les autres utilisent le **simulateur en ligne**, puis on tourne. Simulateur : `jessecrossen.github.io/ttsim`.

    - Les numéros de puzzles renvoient au livret du jeu. Les dessins reproduisent le plateau : **picots** (petits points) et **emplacements** en quinconce (où l’on clipse les pièces). Les pièces sont dessinées d’après le simulateur.

    - Les questions \[ à la main \]  se traitent sur le cahier (réponses, tables, schémas de montages).

    - Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la [charte d’usage de l’IA](../charte.md).

## Le matériel en deux minutes

![](../figures/250263a7db3512b8.svg){ .tikz loading=lazy }

La rampe est une barre inclinée terminée par un crochet : la bille roule jusqu’au crochet, la rampe bascule et lâche la bille de ce côté, puis le **contrepoids** (le rond) la remet en place. Le bit, lui, n’a pas de contrepoids : il **reste** dans sa nouvelle position.

| **Pièce** | **Rôle** | **Équivalent électronique** |
|:---|:---|:---|
| Rampe (verte) | envoie la bille toujours du même côté | un fil |
| Croisement (orange) | deux chemins qui se croisent sans se mélanger | deux fils qui se croisent |
| **Bit** (bleu) | pointe à gauche ou à droite ; **change de sens** à chaque bille | un transistor / une bascule mémoire |
| Intercepteur (noir) | arrête la bille : la machine s’arrête | fin du programme |
| Bit à engrenage + engrenages | comme un bit, mais fait basculer les bits reliés | des bits « câblés » ensemble |
| Leviers du bas | une bille qui arrive à gauche lâche une bille bleue, à droite une bille rouge | l’horloge : une instruction après l’autre |

## Le bit : une mémoire d’un chiffre binaire

!!! definition "Définition 5 — Convention du jeu"

    Un bit qui pointe **à droite** vaut `1` ; un bit qui pointe **à gauche** vaut `0`. Quand une bille le traverse, elle tombe du côté **opposé** à la flèche, puis le bit **bascule**.

![](../figures/b82f39e5df3c57d2.svg){ .tikz loading=lazy }

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — Table du bit <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-tp-2-1 }

\[ à la main \]  Recopier et compléter sur le cahier le tableau suivant.

| **Valeur avant** | **Côté où tombe la bille** | **Valeur après** |
|:----------------:|:--------------------------:|:----------------:|
|       `0`        |             …              |        …         |
|       `1`        |             …              |        …         |

Quelle opération le bit réalise-t-il sur sa propre valeur ? Quelle porte logique du TP d’arithmétique binaire lui correspond ?

??? corrige "Corrigé"

    !!! remarque "Remarque"

        Conventions (celles du guide officiel de Turing Tumble) : un bit vaut 1 quand il pointe à droite, et le bit du haut d’un registre est celui des unités. Les montages des portes ET/OU, de l’inverseur et de « inverser puis $+1$ » ont été conçus pour l’atelier et **testés dans le simulateur** (tous les cas des portes ; `0101` $\to$ `1010` ; `1011` $\to$ `1100`).

    Valeur `0` : la bille tombe à **droite**, le bit passe à `1`. Valeur `1` : la bille tombe à **gauche**, le bit passe à `0`. Le bit **inverse** sa valeur à chaque passage : c’est la porte **NON** appliquée à sa propre mémoire.

## Des portes logiques avec des billes

Un bit peut servir d’**entrée** : on le règle à la main avant de lancer la bille (`1` = vrai, `0` = faux). La bille teste les bits l’un après l’autre et finit dans l’intercepteur **T** (vrai, *true*) ou **F** (faux, *false*). Voici deux montages, testés dans le simulateur, qui ne diffèrent que par l’orientation de quelques rampes.

![](../figures/8dcacc5c44439b1f.svg){ .tikz loading=lazy }

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 2</span> — Deux portes à reconnaître <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-tp-2-2 }

1.  \[ à la main \]  Pour chaque montage, suivre la bille dans les quatre cas ($A, B \in \{0, 1\}$) et dresser la table de vérité (colonnes A, B, intercepteur atteint). Quelle porte logique chaque montage réalise-t-il ?

2.  Dans le montage 1, que se passe-t-il quand A vaut `0` : le bit B est-il seulement « lu » ? Faire le lien avec l’évaluation paresseuse de `and` en Python (`a and b` n’évalue pas `b` quand `a` est faux).

3.  Après le passage de la bille, les bits traversés ont basculé. Que faut-il faire avant de tester le cas suivant ?

4.  \[ plateau ou simulateur \]  Le puzzle **18** (« Entanglement ») demande justement une porte ET : le monter et vérifier.

??? corrige "Corrigé"

    **1.** Montage 1 : seul le cas $A = B = 1$ mène à T (A à `1` : la bille part à gauche, la rampe la ramène sur B ; B à `1` : à gauche, vers T). Dans les trois autres cas, elle finit dans F : c’est la porte **ET**. Montage 2 : seul $A = B = 0$ mène à F. Si A vaut `1`, la bille part directement vers T ; sinon elle est envoyée sur B. C’est la porte **OU**.

    **2.** Si A vaut `0`, la bille part à droite et n’atteint jamais B : B n’est ni lu ni basculé. Le résultat est déjà connu (faux), exactement comme `a and b` en Python, qui n’évalue pas `b` quand `a` est faux. Le montage 2 fait de même pour `a or b` quand `a` est vrai.

    **3.** Remettre les bits traversés dans leur position de départ (ou dans la position du cas suivant) : l’entrée est « consommée » par le passage de la bille.

    **4.** Montage du puzzle 18 (sur le plateau ou le simulateur) : la bille n’atteint l’intercepteur « vrai » que si les deux bits d’entrée valent `1` (même logique que le montage 1).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 3</span> — NON, puis OU exclusif <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-tp-2-3 }

1.  \[ à la main \]  Avec **un seul** bit A, deux rampes et les deux intercepteurs, dessiner sur le cahier un montage qui réalise la porte NON (T si A vaut `0`, F sinon).

2.  *Défi* (★★★) : le OU exclusif doit envoyer vers T quand *exactement un* des deux bits vaut `1`. Pourquoi ne suffit-il pas de modifier les rampes du montage 1 ? Proposer une solution avec **deux** bits B et B’ réglés à la même valeur. Quelle pièce du jeu permettrait de les relier pour qu’on n’ait qu’une seule entrée B à régler ?

??? corrige "Corrigé"

    **1.** Un seul bit A : s’il vaut `0`, la bille tombe à droite, donc une rampe vers la droite mène à T ; s’il vaut `1`, elle tombe à gauche, et une rampe vers la gauche mène à F.

    **2.** Dans les deux branches issues de A, il faut connaître B. Or, dans le montage 1, la branche « A $=$ `0` » ne passe pas par B. On ne peut pas non plus faire converger les deux branches sur le même bit B : après B, on ne saurait plus d’où venait la bille. Solution : A $=$ `1` mène à un bit B (B $=$ `1` $\to$ F, B $=$ `0` $\to$ T) ; A $=$ `0` mène à un second bit B’ (B’ $=$ `1` $\to$ T, B’ $=$ `0` $\to$ F). Pour n’avoir qu’une entrée, on relie B et B’ par des **bits à engrenage** : ils basculent ensemble et ont toujours la même valeur.

## Le registre : un compteur binaire

Voici le montage du puzzle **21** (« Quantum Number ») : quatre bits **empilés en colonne** forment le registre A, entourés de rampes. Le bit du **haut** vaut 1, le suivant 2, puis 4, puis 8. La valeur du registre est la somme des poids des bits qui pointent à droite.

![](../figures/b0bc3a0318dbed58.svg){ .tikz loading=lazy }

!!! propriete "Propriété 3 — Un registre compte en binaire"

    Sur un bit qui vaut `1`, la bille le remet à `0` et **continue** vers le bit suivant : c’est la **retenue**. Sur un bit qui vaut `0`, la bille le met à `1` et **sort** : la retenue s’arrête. Chaque bille ajoute donc **1** au registre : c’est exactement la fonction `incrementer` du TP d’arithmétique binaire.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 4</span> — Lire un registre <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-tp-2-4 }

\[ à la main \]  Donner la valeur de chaque registre (le bit du haut vaut 1).

![](../figures/b99d03c50ae79f65.svg){ .tikz loading=lazy }

??? corrige "Corrigé"

    **a.** $1 + 4 = 5$ (`0101`) ; **b.** $2 + 4 + 8 = 14$ (`1110`) ; **c.** $15$ (`1111`).

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 5</span> — Pair ou impair ? La moitié ? <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-tp-2-5 }

\[ à la main \]  Sans calculer la valeur du registre :

1.  Comment savoir, d’un seul coup d’œil, si le nombre stocké est pair ?

2.  On cache le bit du haut et on lit les trois autres bits comme un nombre de 3 bits (le bit 2 devient le bit des unités, etc.). Que trouve-t-on pour les registres a., b. et c. ci-dessus ? Quelle opération vient-on de faire ?

??? corrige "Corrigé"

    **1.** Le nombre est pair si et seulement si le bit du haut (celui des unités) pointe à gauche. **2.** a. `0101` (5) $\to$ `010` $=$ 2 ; b. `1110` (14) $\to$ `111` $=$ 7 ; c. `1111` (15) $\to$ `111` $=$ 7. On a fait la **division entière par 2** (`n // 2`) ; le bit caché est le reste (`n % 2`). C’est le décalage vers la droite, l’inverse de `decaler`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Faire tourner la machine dans sa tête <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-tp-2-6 }

1.  \[ à la main \]  Le registre vaut `0101` (5). On lâche 6 billes. Écrire la valeur du registre après chaque bille et, pour chaque bille, le nombre de bits qu’elle traverse.

2.  \[ plateau ou simulateur \]  Monter le puzzle 21 et vérifier. Astuce du livret : bloquer le levier gauche avec le doigt pour arrêter la machine, puis comparer le registre et le nombre de billes tombées.

3.  On part de `0000` et on lâche 16 billes. Quelles billes traversent les **quatre** bits ? Que vaut le registre juste après chacune d’elles ?

??? corrige "Corrigé"

    **1.**

    |     bille      |   1    |   2    |   3    |   4    |   5    |   6    |
    |:--------------:|:------:|:------:|:------:|:------:|:------:|:------:|
    | registre après | `0110` | `0111` | `1000` | `1001` | `1010` | `1011` |
    | bits traversés |   2    |   1    |   4    |   1    |   2    |   1    |

    On trouve bien $5 + 6 = 11$. Une bille traverse tous les bits à `1` de droite, plus le premier `0`.

    **2.** Sur le plateau (puzzle 21), après 6 billes le registre affiche `1011` : on retrouve le tableau ci-dessus. En bloquant le levier, le nombre de billes tombées est égal à la valeur du registre (départ à `0000`).

    **3.** La 8<sup>e</sup> bille ($\texttt{0111} \to \texttt{1000}$) et la 16<sup>e</sup> ($\texttt{1111} \to \texttt{0000}$). Pour la 16<sup>e</sup>, la bille ressort sous le bit de poids 8 : c’est la retenue qui sort du registre, elle est perdue.

## Additionner, soustraire

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — L’addition « bille par bille » <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-tp-2-7 }

1.  \[ plateau ou simulateur \]  Régler le registre sur $A = 5$, puis lâcher $B = 6$ billes. Lire le résultat.

2.  Avec un registre assez grand (8 bits), combien de billes faut-il pour calculer $5 + 200$ ? Et $200 + 5$ ? Quelle version est la plus rapide ?

3.  **Pour aller plus loin** (puzzle **37**) : la machine additionne deux *registres* (un de 3 bits valant 5 et un de 4 bits valant 6) et range la somme 11 dans le second. Observer comment les bits à engrenage « lisent » le premier registre.

??? corrige "Corrigé"

    **1.** `1011`, soit 11. **2.** $5 + 200$ : 200 billes ; $200 + 5$ : 5 billes. Mieux vaut mettre le grand nombre dans le registre, car le coût est proportionnel au nombre de billes, donc à la *valeur* ajoutée. Un additionneur électronique, lui, coûte autant d’étapes que de bits (TP d’arithmétique binaire, exercice *Additionner avec des billes*). **3.** Observation : chaque bit à engrenage du premier registre, quand il vaut `1`, aiguille vers le second registre autant de billes que son poids ; le second registre, qui est un compteur, fait le reste : $5 + 6 = 11 = \texttt{1011}$.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Le décompteur <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-tp-2-8 }

En retournant les rampes de l’autre côté du registre, il **décompte** : chaque bille retire 1 (puzzle **22**, « Depletion »).

![](../figures/72edbbd3f32c3795.svg){ .tikz loading=lazy }

1.  \[ à la main \]  Comparer avec le compteur : pourquoi suffit-il de changer les rampes de côté pour passer de « $+1$ » à « $-1$ » ? (Penser à la règle de l’emprunt quand on pose $\texttt{1000} - 1$.)

2.  \[ plateau ou simulateur \]  Puzzles **23** et **24** : laisser passer exactement 4, puis 9 billes, et intercepter la suivante. Quelle valeur de départ faut-il donner au registre ?

3.  \[ à la main \]  Le registre vaut `0000` et on retire encore 1. Que vaut-il ? Lu en **complément à deux** sur 4 bits, que représente ce résultat ? Conclure : le complément à deux n’est pas une convention arbitraire, c’est ce que fait naturellement un compteur qui passe sous zéro.

??? corrige "Corrigé"

    **1.** $\texttt{1000} - 1$ : les `0` de droite deviennent `1` (l’emprunt se propage) jusqu’au premier `1`, qui devient `0`. C’est la règle de l’incrément, `0` et `1` échangés. Chaque bit traversé bascule toujours de la même façon ; seul change le bit sur lequel la bille doit *continuer* : ceux à `0`, d’où elle tombe à droite. Les rampes de retenue passent donc à droite et le couloir de sortie à gauche. **2.** Départ à 4 pour le puzzle 23, à 9 pour le puzzle 24 : la bille suivante trouve le registre à 0 et est dirigée vers l’intercepteur. **3.** $\texttt{0000} - 1 = \texttt{1111}$, qui vaut $-1$ en complément à deux sur 4 bits. Le complément à deux est simplement ce qu’on obtient en continuant de compter à rebours sous zéro, modulo $2^4$.

## L’opposé d’un nombre : inverser, puis ajouter 1

En complément à deux, $-A$ s’obtient en **inversant** tous les bits de $A$, puis en **ajoutant 1**. La machine sait faire les deux, avec le *même* registre : il suffit de changer l’orientation des quatre rampes situées juste à droite des bits. Ces montages ont été testés dans le simulateur.

![](../figures/1d6fb8aca40b43a5.svg){ .tikz loading=lazy }

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 9</span> — Calculer $-4$ avec deux billes <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-tp-2-9 }

1.  \[ à la main \]  Phase 1 : dans le montage « inverser », les deux côtés de chaque bit mènent au bit du dessous. Combien de fois chaque bit est-il traversé ? Pourquoi obtient-on bien l’inverse de A ?

2.  Phase 2 : quel montage déjà vu reconnaît-on ? Pourquoi a-t-on placé des intercepteurs en bas ?

3.  \[ à la main \]  Décoder le résultat `1100` en complément à deux sur 4 bits. A-t-on bien obtenu $-4$ ?

4.  Entre les deux phases, les *données* (les bits) n’ont pas bougé : seules les rampes ont changé. À quoi correspondent les rampes dans un ordinateur : aux données ou au programme ?

??? corrige "Corrigé"

    **1.** Chaque bit est traversé **exactement une fois** : qu’il envoie la bille à gauche ou à droite, une rampe la ramène sur le bit du dessous. Chaque bit bascule donc une fois, ce qui donne l’inverse. **2.** C’est le compteur du puzzle 21 (une bille ajoute 1). Sans intercepteurs, la bille atteindrait le levier et lâcherait une nouvelle bille, qui recommencerait (inverser encore, ou ajouter encore 1). **3.** $\texttt{1100}_2 = 12$ et $12 - 16 = -4$ : c’est bien $-4$. **4.** Les rampes jouent le rôle du **programme** (les instructions), les bits celui des **données**. On a reprogrammé la machine sans toucher aux données.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 10</span> — Des cas surprenants <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-tp-2-10 }

1.  \[ plateau ou simulateur \]  Calculer $-5$ (A $=$ `0101`). Vérifier avec `complement_a_deux(-5, 4)` du TP d’arithmétique binaire.

2.  \[ à la main \]  Que donne la machine pour A $=$ `0000` ? Dans quel intercepteur finit la bille de la phase 2 ? Pourquoi le résultat reste-t-il juste ?

3.  \[ à la main \]  Et pour A $=$ `1000`, c’est-à-dire $-8$ ? Expliquer le résultat étonnant en revenant à la plage des entiers représentables sur 4 bits.

!!! remarque "Remarque"

    Le puzzle **27** (« Reflection ») demande d’inverser neuf bits quelle que soit leur position de départ, et les puzzles **28** à **30** introduisent la **bascule** (*latch*) : un bit à engrenage qui, une fois basculé, le reste, quelles que soient les billes suivantes. C’est une **mémoire** qui retient un événement, comme l’indicateur de dépassement du puzzle 30. Dans un processeur, les mémoires sont fabriquées de la même façon, à partir de portes logiques rebouclées sur elles-mêmes.

??? corrige "Corrigé"

    **1.** `0101` $\to$ `1010` $\to$ `1011`, et `complement_a_deux(-5, 4)` renvoie bien `"1011"`. **2.** `0000` $\to$ `1111`, puis la bille de la phase 2 traverse les quatre bits (tous à `1`), les remet à `0` et finit dans l’intercepteur de **gauche**, celui de la retenue qui sort. Résultat `0000` : $-0 = 0$, la retenue perdue ne gêne pas (calcul modulo 16). **3.** `1000` $\to$ `0111` $\to$ `1000` : la machine affirme que $-(-8) = -8$ ! Sur 4 bits, la plage est $[-8 \,;\, 7]$ : $+8$ n’est pas représentable, c’est un **dépassement**. La fonction `complement_a_deux` a le même comportement.

## Le dépassement

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 11</span> — Quand le registre déborde <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-tp-2-11 }

1.  \[ à la main \]  Un registre de 4 bits vaut `1111`. On lâche une bille. Que vaut-il ensuite ? Où est passée la retenue ?

2.  \[ plateau ou simulateur \]  Puzzle **30** (« Overflow ») : un registre de 3 bits compte les billes ; un bit à engrenage `OV` doit basculer, et *rester* basculé, dès qu’on dépasse 7. À quoi sert ce bit ? Faire le lien avec la fonction `depassement` du TP d’arithmétique binaire.

??? corrige "Corrigé"

    **1.** `0000` : la retenue est sortie du registre et s’est perdue. La machine calcule *modulo 16*. **2.** Le bit `OV` est un **indicateur de dépassement**, comme le drapeau *overflow* d’un processeur. Il garde la trace du fait que le résultat affiché est faux, rôle que joue `depassement` dans le TP d’arithmétique binaire.

## Multiplier

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 12</span> — Compter de 2 en 2 <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-tp-2-12 }

1.  \[ à la main \]  Si les billes entraient dans le registre directement par le bit de poids 2 (et non par le bit du haut), de combien chaque bille augmenterait-elle le registre ? Et par le bit de poids 4 ?

2.  \[ plateau ou simulateur \]  *Défi* : modifier le compteur du puzzle 21 pour qu’il compte de 2 en 2. Que vaut le registre après $B$ billes ? Faire le lien avec `decaler` : multiplier par 2, c’est décaler d’un rang.

??? corrige "Corrigé"

    **1.** $+2$ par le bit de poids 2, $+4$ par le bit de poids 4 (on saute le ou les premiers rangs). **2.** Après $B$ billes, le registre vaut $A + 2B$ (modulo 16). Entrer un rang plus bas revient à multiplier la contribution de chaque bille par 2, comme `decaler(s, 1)`.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 13</span> — Le multiplicateur mécanique <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-tp-2-13 }

1.  \[ plateau ou simulateur \]  Puzzle **48** : multiplier un registre par 3. Proposer une idée à partir de ce qui précède (un registre qui décompte $A$ fois, et pour chaque décompte …).

2.  \[ plateau ou simulateur \]  Puzzle **56** : multiplier deux nombres de 2 bits. Le livret les additionne à un registre de 3 bits *modulo 8* : pourquoi ce modulo ? Combien de bits faudrait-il pour ne jamais perdre d’information ? (Voir l’exercice *Le multiplicateur* du TP d’arithmétique binaire.)

3.  Le plateau ne mesure que quelques dizaines de cases et la boîte contient un nombre limité de pièces. Pourquoi, malgré tout, dit-on que Turing Tumble est « Turing-complet » ?

??? corrige "Corrigé"

    **1.** Idée attendue : un registre $A$ décompte ; à chaque décompte, on ajoute 3 au registre résultat. On peut par exemple envoyer une bille par le bit des unités et une autre par le bit de poids 2 ($1 + 2 = 3$). On répète jusqu’à ce que $A$ vaille 0 : c’est la multiplication vue comme une addition répétée. **2.** $3 \times 3 = 9 = \texttt{1001}$ demande 4 bits. Avec un registre de 3 bits, la retenue de poids 8 est perdue : on obtient le résultat modulo 8. Un produit de deux nombres de 2 bits tient toujours sur $2 + 2 = 4$ bits. **3.** « Turing-complet » signifie qu’avec un plateau et des pièces *illimités*, la machine pourrait effectuer n’importe quel calcul qu’effectue un ordinateur (cela a été démontré en y simulant des machines de Turing). Un vrai ordinateur est d’ailleurs lui aussi limité par sa mémoire.

## Bilan

| **Turing Tumble** | **Processeur** | **TP arithmétique (Python)** |
|:---|:---|:---|
| un bit bleu | un bit de mémoire (bascule) | un caractère `"0"`/`"1"` |
| un registre de bits | un registre du processeur | une chaîne `"0101"` |
| une bille qui traverse le registre | un incrément (`+1`) | `incrementer(s)` |
| la bille qui continue | la retenue | le booléen `retenue` |
| rampes retournées (décompteur) | un décrément (`-1`) | `soustraire(s, "0001")` |
| `1111` + 1 bille $\to$ `0000` | le dépassement (*overflow*) | `depassement(s1, s2)` |
| entrer par le bit de poids 2 | le décalage (× 2) | `decaler(s, 1)` |
| bits A, B testés, intercepteurs T/F | une porte logique | `et(a, b)`, `ou(a, b)` |
| montage « inverser » | NON sur chaque bit | `inverser(s)` |
| inverser, puis 1 bille | l’opposé $-A$ | `complement_a_deux(-n, 4)` |
