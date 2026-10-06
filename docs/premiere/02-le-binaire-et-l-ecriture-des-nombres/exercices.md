# Exercices

<p class="sous-titre">Le binaire et l'écriture des nombres</p>

!!! consignes "Mode d’emploi"

    - Niveau : ★ échauffement, ★★ classique (niveau bac), ★★★ défi ; les *coups de pouce* et les *corrigés* se déplient sous chaque exercice.

    - \[ à la main \]  à traiter **à la main** (sur le cahier) ; \[ sur machine \]  à faire ou **vérifier en console** Python.

    - Rappels : `bin(n)`, `hex(n)`, `int("...", 2)`, `int("...", 16)`, littéraux `0b...` et `0x...`.

    - Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la [charte d’usage de l’IA](../charte.md).

### Bases et conversions

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — Compter les possibilités <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-1 }

\[ à la main \] 

1.  Combien de valeurs différentes peut-on coder sur `4` bits ? sur `8` bits ? sur `n` bits ?

2.  Quel est le plus grand entier positif codable sur un octet (8 bits) ?

??? corrige "Corrigé"

    !!! remarque "Remarque"

        Les conversions à la main sont détaillées ; on peut toujours les vérifier avec `bin`, `hex` et `int`.

    **1.** Sur `4` bits : $2^4 = 16$ valeurs ; sur `8` bits : $2^8 = 256$ ; sur `n` bits : $2^n$. **2.** Le plus grand entier sur un octet est $2^8 - 1 = 255$ (soit `11111111`).

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 2</span> — Du binaire vers le décimal <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-2 }

\[ à la main \]  Convertir en base 10 : $\texttt{1011}_2$ ; $\texttt{11001}_2$ ; $\texttt{10111001}_2$.

??? corrige "Corrigé"

    On additionne les poids des rangs à `1` :

    - $\texttt{1011}_2 = 8 + 2 + 1 = 11$ ;

    - $\texttt{11001}_2 = 16 + 8 + 1 = 25$ ;

    - $\texttt{10111001}_2 = 128 + 32 + 16 + 8 + 1 = 185$.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 3</span> — Du décimal vers le binaire <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-3 }

\[ à la main \]  Convertir en base 2 (méthode des divisions par 2) : $13$ ; $42$ ; $200$.

??? corrige "Corrigé"

    Divisions successives par 2, restes lus de bas en haut :

    - $13 = \texttt{1101}_2$ ($13,6,3,1 \to$ restes $1,0,1,1$) ;

    - $42 = \texttt{101010}_2$ ;

    - $200 = \texttt{11001000}_2$.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 4</span> — Vérifier à la machine <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-4 }

\[ sur machine \]  Vérifier les réponses des exercices 2 et 3 en console.

```text
>>> bin(200)
>>> int("11001", 2)
```

??? corrige "Corrigé"

    ```text
    >>> bin(200)
    '0b11001000'
    >>> int("11001", 2)
    25
    ```

### L’hexadécimal

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 5</span> — Binaire et hexadécimal <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-5 }

\[ à la main \]  En regroupant les bits par paquets de 4 : convertir $\texttt{11011010}_2$ en hexadécimal, et $\texttt{3F}_{16}$ en binaire.0

??? pouce "Coup de pouce"

    Un paquet de 4 bits code une valeur de $0$ à $15$, donc exactement un chiffre hexadécimal. Par quel côté commencer les paquets ? Dans l’autre sens, chaque chiffre hexadécimal redonne 4 bits.

??? corrige "Corrigé"

    On regroupe par 4 bits : $$\texttt{11011010}_2 = \underbrace{\texttt{1101}}_{\texttt{D}}\,\underbrace{\texttt{1010}}_{\texttt{A}} = \texttt{DA}_{16}, \qquad \texttt{3F}_{16} = \underbrace{\texttt{0011}}_{\texttt{3}}\,\underbrace{\texttt{1111}}_{\texttt{F}} = \texttt{00111111}_2.$$

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Décimal et hexadécimal <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-6 }

\[ à la main \]  Convertir $255$ et $3000$ en hexadécimal ; convertir $\texttt{2A}_{16}$ et $\texttt{FF}_{16}$ en décimal.0

??? pouce "Coup de pouce"

    Même méthode qu’en binaire, avec la base 16 : divisions successives par $16$ dans un sens, somme des poids ($1$, $16$, $256$…) dans l’autre. Ne pas oublier que `A` vaut $10$ et `F` vaut $15$.

??? corrige "Corrigé"

    $255 = \texttt{FF}_{16}$ ; $3000 = \texttt{BB8}_{16}$ (car $3000 = 11{\cdot}256 + 11{\cdot}16 + 8$).  
    $\texttt{2A}_{16} = 2{\cdot}16 + 10 = 42$ ; $\texttt{FF}_{16} = 15{\cdot}16 + 15 = 255$.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Une couleur du Web <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-7 }

\[ sur machine \]  Sur le Web, une couleur s’écrit `#RRGGBB` en hexadécimal (rouge, vert, bleu, chacun sur un octet). Retrouver les trois composantes (en base 10) de la couleur `#FF8000`.

```text
>>> int("FF", 16)
>>> int("80", 16)
>>> int("00", 16)
```

À votre avis, quelle *couleur* obtient-on (rouge « à fond », un peu de vert, pas de bleu) ?0

??? pouce "Coup de pouce"

    Découper `FF8000` en trois paquets de deux chiffres hexadécimaux : un octet par composante. Que vaut chaque octet sur l’échelle de $0$ à $255$ ?

??? corrige "Corrigé"

    ```text
    >>> int("FF", 16)
    255
    >>> int("80", 16)
    128
    >>> int("00", 16)
    0
    ```

    Rouge à fond (`255`), vert à moitié (`128`), pas de bleu : on obtient un **orange**.

### Programmer les conversions

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Décimal vers binaire <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-8 }

\[ sur machine \]  Écrire une fonction `decimal_vers_binaire(n)` qui renvoie l’écriture binaire d’un entier `n` $\geqslant 0$ sous forme de **chaîne**, à l’aide d’une boucle `while`. Traiter le cas `n = 0`.0

??? pouce "Coup de pouce"

    Refaire à la main les divisions par 2 de $13$ : à chaque étape, quel reste note-t-on, et de quel côté de la chaîne déjà écrite faut-il le placer ?

0

??? pouce "Coup de pouce 2 (début de solution)"

    `resultat = ""`  
    `while n > 0:`  
    `resultat = str(n % 2) + resultat`  
    …

```text
>>> decimal_vers_binaire(13)
'1101'
```

??? corrige "Corrigé"

    C’est la méthode des divisions par 2, avec accumulation des restes en tête de chaîne.

    ```python
    def decimal_vers_binaire(n):
        if n == 0:
            return "0"
        resultat = ""
        while n > 0:
            resultat = str(n % 2) + resultat   # on place le reste devant
            n = n // 2
        return resultat

    assert decimal_vers_binaire(13) == "1101"
    assert decimal_vers_binaire(200) == "11001000"
    assert decimal_vers_binaire(0) == "0"
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 9</span> — Binaire vers décimal <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-9 }

\[ sur machine \]  Écrire une fonction `binaire_vers_decimal(ch)` qui prend une chaîne de `0` et de `1` et renvoie l’entier correspondant, en parcourant la chaîne avec une boucle `for`.0

??? pouce "Coup de pouce"

    Lire les bits de gauche à droite en gardant un accumulateur `n`. Quand on ajoute un bit à droite d’un nombre binaire, sa valeur est multipliée par combien ?

0

??? pouce "Coup de pouce 2 (début de solution)"

    `n = 0`  
    `for c in ch:`  
    `n = n * 2 + int(c)` (puis renvoyer `n`)

```text
>>> binaire_vers_decimal("10111001")
185
```

??? corrige "Corrigé"

    Le schéma d’Horner : à chaque chiffre, on double l’accumulateur et on ajoute le bit.

    ```python
    def binaire_vers_decimal(ch):
        n = 0
        for c in ch:
            n = n * 2 + int(c)
        return n

    assert binaire_vers_decimal("1011") == 11
    assert binaire_vers_decimal("10111001") == 185
    ```

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 10</span> — Changer de base <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-10 }

\[ sur machine \]  Écrire une fonction `decimal_vers_base(n, b)` qui renvoie, sous forme de chaîne, l’écriture d’un entier `n` $\geqslant 0$ en base `b`, pour $2 \leqslant b \leqslant 16$. Les chiffres utilisés sont ceux de la chaîne `"0123456789ABCDEF"`.0

??? pouce "Coup de pouce"

    Généraliser `decimal_vers_binaire` : que devient la division par 2 ? Le reste est un nombre entre $0$ et $b - 1$ : comment obtenir le *caractère* correspondant à partir de la chaîne `"0123456789ABCDEF"` ?

0

??? pouce "Coup de pouce 2 (début de solution)"

    `chiffres = "0123456789ABCDEF"`  
    `resultat = ""`  
    `while n > 0:`  
    `resultat = chiffres[n % b] + resultat`  
    …

```text
>>> decimal_vers_base(255, 16)
'FF'
>>> decimal_vers_base(13, 2)
'1101'
>>> decimal_vers_base(100, 8)
'144'
```

Vérifier les résultats avec `hex`, `bin` et `int("144", 8)`.

??? corrige "Corrigé"

    Même algorithme que pour le binaire, en divisant par `b` au lieu de 2. Le reste `n % b`, compris entre $0$ et $b - 1$, sert d’indice dans la chaîne des chiffres.

    ```python
    def decimal_vers_base(n, b):
        chiffres = "0123456789ABCDEF"
        if n == 0:
            return "0"
        resultat = ""
        while n > 0:
            resultat = chiffres[n % b] + resultat
            n = n // b
        return resultat

    assert decimal_vers_base(255, 16) == "FF"
    assert decimal_vers_base(13, 2) == "1101"
    assert decimal_vers_base(100, 8) == "144"
    assert decimal_vers_base(0, 5) == "0"
    ```

    Vérification : `hex(255)` affiche `’0xff’`, `bin(13)` affiche `’0b1101’` et `int("144", 8)` vaut `100`. La boucle se termine car `n` décroît strictement (`n // b < n` dès que $b \geqslant 2$).

### Les entiers relatifs (complément à deux)

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 11</span> — Coder et décoder <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-11 }

\[ à la main \] 

1.  Donner la représentation de $-20$ sur `8` bits (complément à deux).

2.  On lit `11111011` (8 bits, complément à deux). Est-ce un nombre positif ou négatif ? Quelle est sa valeur ?0

    ??? pouce "Coup de pouce"

        Pour coder : écrire $20$ sur 8 bits, inverser, ajouter $1$. Pour décoder : le bit de poids fort donne le signe ; la même opération « inverser puis ajouter 1 » redonne la valeur absolue.

??? corrige "Corrigé"

    **1.** Coder $-20$ sur 8 bits : $20 = \texttt{00010100}$ ; on inverse : `11101011` ; on ajoute 1 : `11101100`. Donc $-20 = \texttt{11101100}$.

    **2.** `11111011` commence par `1` : c’est un **négatif**. Pour trouver sa valeur, on inverse (`00000100`) et on ajoute 1 (`00000101` $= 5$) : la valeur est donc $-5$.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 12</span> — Débordement <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-12 }

\[ à la main \]  \[ sur machine \] 

1.  Quelles sont les valeurs minimale et maximale d’un entier relatif codé sur `8` bits ? sur `16` bits ?

2.  En console, calculer `2 ** 64`. Pourquoi Python y arrive-t-il alors qu’un entier « sur 64 bits fixes » déborderait ?0

    ??? pouce "Coup de pouce"

        Sur 8 bits, le bit de poids fort indique le signe : quel est le plus grand nombre qui commence par `0` ? Et quel est le code du plus petit négatif ? Généraliser à 16 bits avec des puissances de 2.

    0

    ??? pouce "Coup de pouce 2 (début de solution)"

        Sur 8 bits, le plus grand positif est `01111111`, soit $2^7 - 1$. Écrire de même le plus petit négatif à l’aide d’une puissance de 2, puis remplacer $7$ par $15$.

??? corrige "Corrigé"

    **1.** Sur 8 bits : de $-128$ à $+127$. Sur 16 bits : de $-32768$ à $+32767$.

    **2.** `2 ** 64` vaut `18446744073709551616` : Python le calcule car ses entiers sont de **taille arbitraire** (ils grandissent avec la mémoire). Sur « 64 bits fixes » (comme dans le matériel ou d’autres langages), cette valeur **dépasse** le plus grand entier codable : elle « déborde ».

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 13</span> — Le cas étrange de $-128$ <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-13 }

\[ à la main \] 

1.  Coder $-128$ sur `8` bits en complément à deux (on écrira d’abord $128$ en binaire sur 8 bits).

2.  Appliquer la méthode « inverser puis ajouter 1 » à l’écriture obtenue, comme pour calculer son opposé. Que constate-t-on ?

3.  Expliquer ce résultat à l’aide des valeurs extrêmes codables sur 8 bits.

4.  Sur 8 bits, combien d’entiers **strictement négatifs** peut-on coder ? Combien d’entiers **positifs ou nuls** ? Pourquoi les bornes ne sont-elles pas symétriques ?0

    ??? pouce "Coup de pouce"

        Pour la question 2, l’opposé de $-128$ serait $+128$ : ce nombre fait-il partie des valeurs codables sur 8 bits en complément à deux ?

    0

    ??? pouce "Coup de pouce 2 (début de solution)"

        $128 = \texttt{10000000}$ ; inversion : `01111111` ; ajout de $1$ : … Pour la question 4, ne pas oublier que $0$ occupe l’un des codes qui commencent par `0`.

??? corrige "Corrigé"

    **1.** $128 = \texttt{10000000}$ ; on inverse : `01111111` ; on ajoute 1 : `10000000`. Donc $-128$ se code `10000000`.

    **2.** On inverse `10000000` : `01111111` ; on ajoute 1 : `10000000`. On **retombe sur le même code** : l’« opposé » de $-128$ calculé ainsi est encore $-128$.

    **3.** L’opposé de $-128$ est $+128$, qui n’est **pas codable** sur 8 bits : le plus grand positif est $+127$ (`01111111`). Le calcul déborde et redonne $-128$.

    **4.** Les codes qui commencent par `1` sont les $2^7 = 128$ négatifs, de $-128$ à $-1$. Les codes qui commencent par `0` sont aussi au nombre de 128, mais l’un d’eux est $0$ : il ne reste que 127 positifs stricts, de $1$ à $127$. D’où l’asymétrie des bornes $-128$ et $+127$.

### Les nombres à virgule

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 14</span> — Fractions en binaire <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-14 }

\[ à la main \] 

1.  Convertir en binaire : $0{,}75$ et $6{,}25$.

2.  Convertir en base 10 : $\texttt{101,101}_2$.0

    ??? pouce "Coup de pouce"

        Traiter séparément la partie entière (méthode habituelle) et la partie après la virgule : la multiplier par 2, noter le chiffre avant la virgule, recommencer. Après la virgule, les poids sont $\frac{1}{2}$, $\frac{1}{4}$, $\frac{1}{8}$…

??? corrige "Corrigé"

    **1.** $0{,}75 = \texttt{0,11}_2$ (car $0{,}75 \times 2 = 1{,}5$ puis $0{,}5 \times 2 = 1{,}0$) ; $6{,}25 = \texttt{110,01}_2$ (car $6 = \texttt{110}$ et $0{,}25 = \texttt{0,01}$).

    **2.** $\texttt{101,101}_2 = 4 + 1 + \tfrac{1}{2} + \tfrac{1}{8} = 5{,}625$.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 15</span> — La trahison des flottants <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-15 }

\[ sur machine \]  En console, taper `0.1 + 0.2`, puis `0.1 + 0.2 == 0.3`. Expliquer en une phrase ce que l’on observe. Proposer une manière **correcte** de tester si deux flottants sont « égaux ».

??? corrige "Corrigé"

    ```text
    >>> 0.1 + 0.2
    0.30000000000000004
    >>> 0.1 + 0.2 == 0.3
    False
    ```

    `0,1` et `0,2` n’ayant pas d’écriture binaire finie, ils sont stockés de façon **approchée** : la somme n’est pas exactement `0.3`. Pour comparer deux flottants, on teste si leur écart est minuscule :

    ```python
    abs((0.1 + 0.2) - 0.3) < 1e-9      # True
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 16</span> — Additionner dix fois un dixième <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-16 }

\[ sur machine \]  En console, calculer la somme de dix fois `0.1` :

```python
total = 0
for i in range(10):
    total = total + 0.1
print(total)
```

Quel résultat obtient-on ? Est-il exactement égal à `1.0` ? Relier cette observation au cours.0

??? pouce "Coup de pouce"

    Le nombre `0.1` a-t-il une écriture binaire finie ? Que se passe-t-il pour une petite erreur répétée dix fois ?

??? corrige "Corrigé"

    On obtient `0.9999999999999999`, et non `1.0`. Chaque `0.1` étant déjà approché, les petites erreurs s’**accumulent** à chaque addition. C’est la même cause qu’à l’exercice précédent : les flottants sont des approximations, jamais des valeurs exactes.

### Coder le texte : ASCII et Unicode

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 17</span> — Lire la table ASCII <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-17 }

\[ à la main \]  On donne les codes ASCII : `A`${=}65$, `Z`${=}90$, `a`${=}97$, `0`${=}48$.

1.  Quel est le code de `C` ? de `c` ? *(On rappelle : minuscule $=$ majuscule $+\,32$.)*

2.  Quel caractère a pour code $90 - 25 = 65$ ? Quel caractère a pour code $57$ ?

3.  Écrire le code du caractère `A` ($65$) en binaire sur 7 bits.

??? corrige "Corrigé"

    1.  `C` $= 65 + 2 = 67$ ; `c` $= 67 + 32 = 99$.

    2.  Le code $65$ est celui de `A` ; le code $57$ est celui de `9` (les chiffres vont de `0`${=}48$ à `9`${=}57$).

    3.  $65 = 64 + 1 = \texttt{1000001}_2$ (sur 7 bits).

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 18</span> — `ord` et `chr` <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-18 }

\[ sur machine \]  En console, prévoir *puis vérifier* :

```python
ord("H")
chr(105)
chr(ord("B") + 32)
ord("i") - ord("H")
```

??? corrige "Corrigé"

    ```text
    >>> ord("H")
    72
    >>> chr(105)
    'i'
    >>> chr(ord("B") + 32)
    'b'
    >>> ord("i") - ord("H")
    33
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 19</span> — Caractères et octets <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-19 }

\[ sur machine \]  Soit le mot `"élève"`.

1.  Combien a-t-il de **caractères** ? Vérifier avec `len("élève")`.

2.  Combien occupe-t-il d’**octets** en UTF-8 ? Vérifier avec `len("élève".encode("utf-8"))`.

3.  Expliquer l’écart entre les deux nombres.0

    ??? pouce "Coup de pouce"

        Quelles lettres du mot ne font pas partie de l’ASCII ? Combien d’octets UTF-8 utilise-t-il pour une lettre accentuée ?

??? corrige "Corrigé"

    1.  `"élève"` a **5 caractères** : `len("élève")` renvoie `5`.

    2.  Il occupe **7 octets** en UTF-8 : `len("élève".encode("utf-8"))` renvoie `7`.

    3.  Les lettres `é` et `è` ne sont pas dans l’ASCII : chacune prend **2 octets** en UTF-8. On a donc $3$ lettres ASCII ($1$ octet) $+\ 2$ lettres accentuées ($2$ octets) $= 3 + 4 = 7$ octets, pour seulement $5$ caractères.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 20</span> — D’où vient le charabia <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-20 }

\[ à la main \]  Une page Web affiche `cafÃ©` au lieu de `café`.

1.  Sachant que `é` s’écrit sur deux octets en UTF-8, expliquer en une ou deux phrases comment un tel affichage se produit.0

    ??? pouce "Coup de pouce"

        Combien de caractères bizarres remplacent le `é` ? En Latin-1, combien d’octets occupe chaque caractère ? Le fichier a été écrit dans un encodage et lu dans un autre.

2.  \[ sur machine \]  Vérifier avec `"café".encode("utf-8").decode("latin-1")`.

??? corrige "Corrigé"

    1.  Le fichier a été **écrit en UTF-8** (où `é` $=$ deux octets `C3 A9`) mais **relu comme du Latin-1**, où chaque octet est un caractère : `C3` devient `Ã` et `A9` devient `©`, d’où `cafÃ©`. Le fichier n’indique pas lui-même son encodage.

    2.  `"café".encode("utf-8").decode("latin-1")` renvoie `’cafÃ©’`, ce qui reproduit exactement le charabia observé.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 21</span> — Programmer : coder un mot <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-21 }

\[ sur machine \]  Écrire une fonction `afficher_codes(mot)` qui affiche, ligne par ligne, chaque caractère de `mot` suivi de son code ASCII.

*Exemple :* `afficher_codes("Hi")` affiche `H 72` puis, à la ligne suivante, `i 105`.0

??? pouce "Coup de pouce"

    Parcourir les caractères du mot avec une boucle `for` et, à chaque tour, afficher le caractère et le résultat de `ord`.

??? corrige "Corrigé"

    On parcourt les caractères et on affiche chacun avec son code `ord`.

    ```python
    def afficher_codes(mot):
        for c in mot:
            print(c, ord(c))

    afficher_codes("Hi")   # affiche  H 72  puis  i 105
    ```

### Logique booléenne et portes logiques

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 22</span> — Évaluer des opérateurs booléens <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-22 }

\[ à la main \] 

1.  On prend $a = 1$ et $b = 0$. Donner la valeur de : non $a$ ; $a$ et $b$ ; $a$ ou $b$ ; $a$ xor $b$ ; non$(a$ ou $b)$.

2.  Même question avec $a = 1$ et $b = 1$.

3.  \[ sur machine \]  Vérifier en console, en écrivant `True` pour `1`, `False` pour `0` et `a != b` pour $a$ xor $b$ :

    ```text
    >>> not True
    >>> True and False
    >>> True or False
    >>> True != False
    >>> not (True or False)
    ```

??? corrige "Corrigé"

    **1.** Avec $a = 1$ et $b = 0$ : non $a = 0$ ; $a$ et $b = 0$ ; $a$ ou $b = 1$ ; $a$ xor $b = 1$ (les deux bits sont différents) ; non$(a$ ou $b) =$ non $1 = 0$.

    **2.** Avec $a = 1$ et $b = 1$ : non $a = 0$ ; $a$ et $b = 1$ ; $a$ ou $b = 1$ ; $a$ xor $b = 0$ (les deux bits sont égaux : c’est la ligne où ou et xor diffèrent) ; non$(a$ ou $b) = 0$.

    **3.**

    ```text
    >>> not True
    False
    >>> True and False
    False
    >>> True or False
    True
    >>> True != False
    True
    >>> not (True or False)
    False
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 23</span> — Dresser la table d’une expression <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-23 }

\[ à la main \] 

1.  Dresser la table de vérité de non$(a$ et $b)$, puis celle de (non $a)$ ou (non $b)$. Que constate-t-on ? Comment dit-on de ces deux expressions ?

2.  Dresser la table de vérité de $(a$ et $b)$ ou $c$. Combien de lignes faut-il ? Pour combien d’entre elles l’expression vaut-elle `1` ?0

    ??? pouce "Coup de pouce"

        Une ligne par combinaison des entrées : avec $n$ variables, $2^n$ lignes, énumérées en comptant en binaire (`000`, `001`, `010`…). Ajouter une colonne par étape du calcul, en commençant par les parenthèses.

??? corrige "Corrigé"

    **1.** Une ligne par combinaison de $a$ et $b$ (4 lignes), une colonne par étape : $$\begin{array}{|c|c||c|c||c|c|c|}
    \hline
    a & b & a \text{ et } b & \text{non}(a \text{ et } b) & \text{non } a & \text{non } b & (\text{non } a) \text{ ou } (\text{non } b) \\
    \hline
    \texttt{0} & \texttt{0} & \texttt{0} & \texttt{1} & \texttt{1} & \texttt{1} & \texttt{1} \\
    \texttt{0} & \texttt{1} & \texttt{0} & \texttt{1} & \texttt{1} & \texttt{0} & \texttt{1} \\
    \texttt{1} & \texttt{0} & \texttt{0} & \texttt{1} & \texttt{0} & \texttt{1} & \texttt{1} \\
    \texttt{1} & \texttt{1} & \texttt{1} & \texttt{0} & \texttt{0} & \texttt{0} & \texttt{0} \\
    \hline
    \end{array}$$ Les colonnes de non$(a$ et $b)$ et de (non $a)$ ou (non $b)$ sont identiques (`1`, `1`, `1`, `0`) : les deux expressions ont la même table de vérité, elles sont **équivalentes**. « Il est faux que $a$ et $b$ soient tous deux vrais » revient à dire « l’un des deux au moins est faux ».

    **2.** Trois variables : $2^3 = 8$ lignes. $$\begin{array}{|c|c|c||c||c|}
    \hline
    a & b & c & a \text{ et } b & (a \text{ et } b) \text{ ou } c \\
    \hline
    \texttt{0} & \texttt{0} & \texttt{0} & \texttt{0} & \texttt{0} \\
    \texttt{0} & \texttt{0} & \texttt{1} & \texttt{0} & \texttt{1} \\
    \texttt{0} & \texttt{1} & \texttt{0} & \texttt{0} & \texttt{0} \\
    \texttt{0} & \texttt{1} & \texttt{1} & \texttt{0} & \texttt{1} \\
    \texttt{1} & \texttt{0} & \texttt{0} & \texttt{0} & \texttt{0} \\
    \texttt{1} & \texttt{0} & \texttt{1} & \texttt{0} & \texttt{1} \\
    \texttt{1} & \texttt{1} & \texttt{0} & \texttt{1} & \texttt{1} \\
    \texttt{1} & \texttt{1} & \texttt{1} & \texttt{1} & \texttt{1} \\
    \hline
    \end{array}$$ L’expression vaut `1` pour **5** lignes sur 8 : les quatre où $c = 1$, plus la ligne $a = b = 1$, $c = 0$.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 24</span> — Le demi-additionneur <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-24 }

\[ à la main \] 

1.  Recopier et compléter la table de l’addition de deux bits $a$ et $b$, en écrivant le résultat sur deux bits : la retenue $r$ (à gauche) et la somme $s$ (à droite).

    | $a$ | $b$ | retenue $r$ | somme $s$ |
    |:---:|:---:|:-----------:|:---------:|
    | `0` | `0` |             |           |
    | `0` | `1` |             |           |
    | `1` | `0` |             |           |
    | `1` | `1` |             |           |

2.  Quelle porte logique donne la colonne $r$ ? Laquelle donne la colonne $s$ ? Dessiner le circuit du demi-additionneur.

3.  Dans un circuit qui additionne deux nombres de 4 bits, seule la colonne de droite peut être confiée à un demi-additionneur. Pourquoi ? Le constater en posant $\texttt{0110} + \texttt{0011}$ : quelle colonne doit additionner trois bits ? Que manque-t-il au demi-additionneur ?0

    ??? pouce "Coup de pouce"

        Dans la colonne de droite, on n’ajoute que deux bits. Dans la colonne suivante, combien de bits faut-il ajouter ? D’où vient le bit supplémentaire ?

??? corrige "Corrigé"

    **1.** $0 + 0 = \texttt{00}_2$, $0 + 1 = 1 + 0 = \texttt{01}_2$, $1 + 1 = \texttt{10}_2$ : $$\begin{array}{|c|c||c|c|}
    \hline
    a & b & r & s \\
    \hline
    \texttt{0} & \texttt{0} & \texttt{0} & \texttt{0} \\
    \texttt{0} & \texttt{1} & \texttt{0} & \texttt{1} \\
    \texttt{1} & \texttt{0} & \texttt{0} & \texttt{1} \\
    \texttt{1} & \texttt{1} & \texttt{1} & \texttt{0} \\
    \hline
    \end{array}$$

    **2.** La colonne $r$ (`0`, `0`, `0`, `1`) est la table du **et** : $r = a$ et $b$. La colonne $s$ (`0`, `1`, `1`, `0`) est la table du **xor** : $s = a$ xor $b$. Le circuit relie les deux entrées $a$ et $b$ à la fois à une porte xor (sortie : la somme) et à une porte et (sortie : la retenue), comme sur le schéma du cours.

    **3.** La colonne de droite ne reçoit jamais de retenue : on n’y ajoute que **deux** bits, un demi-additionneur suffit. Toute autre colonne peut recevoir la retenue de sa voisine de droite. Dans $\texttt{0110} + \texttt{0011}$, la deuxième colonne ($1 + 1 = \texttt{10}_2$) produit une retenue : la troisième colonne doit additionner **trois** bits ($1$, $0$ et la retenue $1$). Il manque donc au demi-additionneur une entrée pour la **retenue venue de la droite** ; c’est le rôle de l’additionneur complet, construit avec deux demi-additionneurs (voir le TP « Programmer l’arithmétique binaire »). Résultat : $\texttt{0110} + \texttt{0011} = \texttt{1001}$, soit $6 + 3 = 9$.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 25</span> — Le complément à deux selon un assistant d’IA <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> { #ex-02-25 }

Un élève demande à un assistant d’IA : « Comment écrit-on $-5$ sur 8 bits en complément à deux ? » Voici la réponse obtenue.

« On écrit d’abord $5$ sur 8 bits : `00000101`. Le complément à deux consiste à inverser tous les bits, ce qui donne `11111010`. Le bit de poids fort vaut `1`, ce qui confirme que le nombre est négatif. Donc $-5$ s’écrit `11111010` sur 8 bits. Avec cette convention, on représente sur 8 bits les entiers de $-128$ à $+127$. »

1.  \[ à la main \]  La réponse est-elle correcte ? Vérifier en posant l’addition $5 + (-5)$ sur 8 bits avec l’écriture proposée : que doit-on trouver ?

2.  Localiser et corriger l’erreur.

3.  \[ sur machine \]  Quelle vérification simple, faite avant de faire confiance à la réponse, aurait suffi à détecter l’erreur ?0

    ??? pouce "Coup de pouce"

        Un nombre plus son opposé doit donner $0$ : poser l’addition sur 8 bits en ignorant la retenue qui sort. En Python, `bin(256 - 5)` donne l’écriture sur 8 bits de $-5$.

??? corrige "Corrigé"

    **1.** Non. Posons $5 + (-5)$ avec l’écriture proposée : $\texttt{00000101} + \texttt{11111010} = \texttt{11111111}$, et non `00000000` : ce n’est pas l’opposé de $5$. D’ailleurs `11111010` est l’écriture de $-6$ (l’addition avec `00000110` donne bien `1 00000000`, où la retenue déborde des 8 bits). **2.** L’erreur est dans l’étape « inverser tous les bits » : le complément à deux, c’est inverser **puis ajouter 1** ; l’assistant a oublié le $+1$. $5 = \texttt{00000101}$ $\to$ inversion `11111010` $\to$ $+1$ : **`11111011`**. Vérification : $\texttt{00000101} + \texttt{11111011} = \texttt{1\,00000000}$, il reste $0$ sur 8 bits. Le reste de la réponse (signe lu sur le bit de poids fort, bornes $-128$ à $+127$) est juste. **3.** Additionner le nombre et son opposé supposé : on doit trouver $0$ sur 8 bits. Sur machine, `bin(256 - 5)` affiche `’0b11111011’`, ce qui contredit `11111010`.
