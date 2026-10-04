# Exercices

<p class="sous-titre">Les bases de la programmation Python</p>

!!! consignes "Mode d’emploi"

    - Niveau : ★ échauffement, ★★ classique (niveau bac), ★★★ défi ; les *coups de pouce* et les *corrigés* se déplient sous chaque exercice.

    - <span class="run" title="À programmer et tester sur machine">▶</span> *À programmer et tester* en Python (console ou éditeur en ligne). Le symbole `>>>` figure une saisie dans la console.

    - **Réflexe** pour chaque fonction : **(1)** que reçoit-elle (paramètres, *préconditions*) et que **renvoie**-t-elle ? **(2)** l’ai-je **testée** sur des cas simples *et* des cas limites (0, égalité, mot vide…) ?

    - Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la [charte d’usage de l’IA](../charte.md).

!!! remarque "Remarque"

    La **tortue** (`turtle`) fait l’objet d’un **complément séparé**, après ce chapitre : elle n’est pas reprise ici.

### Variables, affectation, types

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — Lecture de trace <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-1 }

Sans machine, donner ce qu’affiche ce programme. Détailler l’évolution de chaque variable.

```python
x = 5
y = 3
x = x + y
y = x - y
x = x - y
print(x, y)
```

Que réalise, au final, ce programme sur `x` et `y` ?

??? corrige "Corrigé"

    !!! remarque "Remarque"

        Plusieurs écritures sont souvent possibles : on donne **une** version simple.

    On suit chaque affectation (on évalue la droite, on range à gauche) :

    | instruction | `x` | `y` |
    |:------------|:---:|:---:|
    | `x = 5`     |  5  |  —  |
    | `y = 3`     |  5  |  3  |
    | `x = x + y` |  8  |  3  |
    | `y = x - y` |  8  |  5  |
    | `x = x - y` |  3  |  5  |

    L’affichage est donc `3 5`. Ce programme **échange** les contenus de `x` et `y` *sans* variable temporaire, en n’utilisant que des additions et des soustractions.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 2</span> — Échanger deux variables <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-2 }

<span class="run" title="À programmer et tester sur machine">▶</span> Deux variables `a` et `b` contiennent respectivement `1` et `2`. Écrire les instructions qui **échangent** leurs contenus (en utilisant une **variable temporaire**), de sorte qu’à la fin `a` vaut `2` et `b` vaut `1`. Pourquoi une variable temporaire est-elle nécessaire ?

??? corrige "Corrigé"

    Avec une variable temporaire :

    ```python
    a = 1
    b = 2
    temp = a         # on met a l'abri la valeur de a
    a = b            # a recoit b
    b = temp         # b recoit l'ancienne valeur de a
    print(a, b)      # 2 1
    ```

    La variable temporaire est nécessaire : sans elle, `a = b` écraserait la valeur de `a`, qui serait perdue avant d’avoir pu être rangée dans `b`.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 3</span> — Convertisseur <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-3 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

1.  Écrire une fonction `celsius_en_fahrenheit(c)` qui convertit une température en degrés Celsius vers des degrés Fahrenheit (formule : $F = \frac{9}{5}\,C + 32$).

2.  Écrire une fonction `prix_ttc(ht)` qui renvoie le prix TTC d’un article à partir de son prix hors taxe, avec une TVA de 20 %.

```text
>>> celsius_en_fahrenheit(100)
212.0
>>> prix_ttc(50)
60.0
```

??? corrige "Corrigé"

    ```python
    def celsius_en_fahrenheit(c):
        return 9 / 5 * c + 32

    def prix_ttc(ht):
        return ht * 1.20

    assert celsius_en_fahrenheit(100) == 212.0
    assert celsius_en_fahrenheit(0) == 32.0
    assert prix_ttc(50) == 60.0
    ```

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 4</span> — Rectangle : périmètre et aire <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-4 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire deux fonctions `perimetre(largeur, hauteur)` et `aire(largeur, hauteur)` qui renvoient respectivement le périmètre et l’aire d’un rectangle.

```text
>>> perimetre(3, 4)
14
>>> aire(3, 4)
12
```

??? corrige "Corrigé"

    ```python
    def perimetre(largeur, hauteur):
        return 2 * (largeur + hauteur)

    def aire(largeur, hauteur):
        return largeur * hauteur

    assert perimetre(3, 4) == 14
    assert aire(3, 4) == 12
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 5</span> — Le bon usage de `//` et `%` <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-5 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire trois fonctions `unites(n)`, `dizaines(n)` et `centaines(n)` qui prennent un entier de trois chiffres au plus et renvoient respectivement son chiffre des unités, des dizaines et des centaines. On n’utilisera que les opérateurs `//` (quotient) et `%` (reste).0

??? pouce "Coup de pouce"

    Que donnent `347 % 10` et `347 // 10` ? Comment isoler ensuite le chiffre des dizaines à partir de `34` ?

```text
>>> unites(347)
7
>>> dizaines(347)
4
>>> centaines(347)
3
>>> dizaines(60)
6
```

??? corrige "Corrigé"

    `n % 10` isole le dernier chiffre ; `n // 10` « décale » le nombre d’un cran vers la droite.

    ```python
    def unites(n):
        return n % 10

    def dizaines(n):
        return (n // 10) % 10

    def centaines(n):
        return (n // 100) % 10

    assert unites(347) == 7 and dizaines(347) == 4 and centaines(347) == 3
    assert unites(60) == 0 and dizaines(60) == 6 and centaines(60) == 0
    assert unites(7) == 7 and dizaines(7) == 0 and centaines(7) == 0
    ```

### Les conditionnelles

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 6</span> — Pair ou impair <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-6 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire une fonction `est_pair(n)` qui renvoie `True` si l’entier `n` est pair, `False` sinon. Vérifier le résultat sur quelques valeurs, sans oublier le cas `n = 0`.

??? corrige "Corrigé"

    ```python
    def est_pair(n):
        return n % 2 == 0

    assert est_pair(4) == True
    assert est_pair(7) == False
    assert est_pair(0) == True
    ```

    Remarquer qu’on *renvoie directement* le booléen `n % 2 == 0` : inutile d’écrire `if ...: return True else: return False`.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 7</span> — Le plus grand des deux <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-7 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire une fonction `maximum2(a, b)` qui renvoie le plus grand des deux nombres `a` et `b`, **sans** utiliser la fonction `max`. Ne pas oublier le cas d’égalité.

??? corrige "Corrigé"

    ```python
    def maximum2(a, b):
        if a > b:
            return a
        return b        # couvre aussi le cas a == b

    assert maximum2(3, 5) == 5
    assert maximum2(5, 3) == 5
    assert maximum2(4, 4) == 4
    ```

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 8</span> — Le signe d’un nombre <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-8 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `signe(x)` qui renvoie `1` si `x` est strictement positif, `-1` s’il est strictement négatif, et `0` s’il est nul. (On utilisera `if`, `elif`, `else`.)

??? corrige "Corrigé"

    ```python
    def signe(x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0

    assert signe(12) == 1
    assert signe(-3) == -1
    assert signe(0) == 0
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 9</span> — Mention au bac <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-9 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire une fonction `mention(note)` qui renvoie la mention correspondant à une note sur 20 : « Très bien » ($\geqslant 16$), « Bien » ($\geqslant 14$), « Assez bien » ($\geqslant 12$), « Admis » ($\geqslant 10$, sans mention), « Refusé » sinon.

1.  Pourquoi l’**ordre** des tests est-il important ? Que se passerait-il si on testait `note >= 10` en premier ?

2.  Que renvoie votre fonction pour `note = 25` (valeur impossible) ? On verra plus loin comment interdire proprement une telle valeur avec une *précondition*.0

    ??? pouce "Coup de pouce"

        Reprendre l’exemple du cours sur `elif` : Python exécute le *premier* bloc dont la condition est vraie. Tester à la main la note `18` avec votre ordre de tests.

??? corrige "Corrigé"

    ```python
    def mention(note):
        if note >= 16:
            return "Tres bien"
        elif note >= 14:
            return "Bien"
        elif note >= 12:
            return "Assez bien"
        elif note >= 10:
            return "Admis"
        else:
            return "Refuse"
    ```

    **1.** L’ordre va du plus exigeant au moins exigeant, car Python exécute le *premier* `elif` vrai. Si on testait `note >= 10` en premier, une note de `18` renverrait « Admis » : toutes les bonnes notes seraient mal classées.

    **2.** `mention(25)` renvoie « Tres bien » (car $25 \geqslant 16$) : la fonction accepte sans broncher une note impossible. C’est justement ce qu’une *précondition* permettra d’interdire (section *Les fonctions* du cours).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 10</span> — Année bissextile <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-10 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire une fonction `est_bissextile(annee)` qui renvoie un booléen, sachant qu’une année est bissextile si elle est divisible par 400, *ou* divisible par 4 sans l’être par 100.0

??? pouce "Coup de pouce"

    « Divisible par 4 » se traduit par `annee % 4 == 0`. Traduire ensuite la phrase mot à mot avec `or` et `and`, en plaçant des parenthèses.

```text
>>> est_bissextile(2000)
True
>>> est_bissextile(1900)
False
>>> est_bissextile(2024)
True
```

??? corrige "Corrigé"

    Un seul booléen suffit :

    ```python
    def est_bissextile(annee):
        return annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0)

    assert est_bissextile(2000) == True
    assert est_bissextile(1900) == False
    assert est_bissextile(2024) == True
    assert est_bissextile(2023) == False
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 11</span> — Le plus grand des trois <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-11 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `maximum3(a, b, c)` qui renvoie le plus grand de trois nombres, sans utiliser `max`.0

??? pouce "Coup de pouce"

    Retenir un « champion provisoire » `m`, égal à `a` au départ, puis le comparer successivement à `b` et à `c`.

??? corrige "Corrigé"

    On garde un « champion provisoire » que l’on met à jour :

    ```python
    def maximum3(a, b, c):
        m = a
        if b > m:
            m = b
        if c > m:
            m = c
        return m

    assert maximum3(3, 9, 5) == 9
    assert maximum3(3, 5, 9) == 9
    assert maximum3(4, 4, 4) == 4
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 12</span> — Quel type de triangle ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-12 }

<span class="run" title="À programmer et tester sur machine">▶</span> On donne les longueurs `a`, `b`, `c` des trois côtés d’un triangle (supposées valides, donc strictement positives). Écrire `type_triangle(a, b, c)` qui renvoie `"equilateral"` (trois côtés égaux), `"isocele"` (exactement deux côtés égaux) ou `"scalene"` (aucun côté égal).0

??? pouce "Coup de pouce"

    Dans quel ordre tester les cas ? Si l’on teste d’abord « trois côtés égaux », que reste-t-il à distinguer ensuite ?

```text
>>> type_triangle(3, 3, 3)
'equilateral'
>>> type_triangle(3, 4, 5)
'scalene'
```

??? corrige "Corrigé"

    On teste l’égalité des trois côtés, puis d’exactement deux (grâce à l’ordre : si les trois étaient égaux, on serait déjà sorti).

    ```python
    def type_triangle(a, b, c):
        assert a > 0 and b > 0 and c > 0
        if a == b and b == c:
            return "equilateral"
        elif a == b or b == c or a == c:
            return "isocele"
        else:
            return "scalene"

    assert type_triangle(3, 3, 3) == "equilateral"
    assert type_triangle(3, 3, 5) == "isocele"
    assert type_triangle(3, 4, 5) == "scalene"
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 13</span> — Réduction par paliers <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-13 }

<span class="run" title="À programmer et tester sur machine">▶</span> Un magasin applique une réduction selon le montant : `0 %` en dessous de 100 €, `5 %` de 100 à moins de 300 €, `10 %` à partir de 300 €. Écrire `prix_reduit(montant)` qui renvoie le montant après réduction.0

??? pouce "Coup de pouce"

    Choisir d’abord le taux (`0`, `5` ou `10`) avec `if`/`elif`/`else`, puis faire le calcul une seule fois à la fin. Attention aux bornes : `300` relève de quel palier ?

```text
>>> prix_reduit(50)
50.0
>>> prix_reduit(200)
190.0
>>> prix_reduit(300)
270.0
```

??? corrige "Corrigé"

    ```python
    def prix_reduit(montant):
        if montant < 100:
            taux = 0
        elif montant < 300:
            taux = 5
        else:
            taux = 10
        return montant * (1 - taux / 100)

    assert prix_reduit(50) == 50.0
    assert prix_reduit(200) == 190.0
    assert prix_reduit(300) == 270.0
    ```

### Les boucles bornées (`for`)

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 14</span> — Remettre l’accumulateur dans l’ordre <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-14 }

Les lignes de la fonction `somme_entre(a, b)`, qui renvoie $a + (a+1) + \dots + b$, ont été mélangées et ont perdu leur indentation.

```text
total = total + i
return total
def somme_entre(a, b):
total = 0
for i in range(a, b + 1):
```

1.  Recopier les lignes dans le bon ordre, **avec la bonne indentation**.

2.  <span class="run" title="À programmer et tester sur machine">▶</span> Vérifier que `somme_entre(3, 6)` renvoie `18`.

3.  Que renverrait la fonction si la ligne `total = 0` était placée *à l’intérieur* de la boucle ?

??? corrige "Corrigé"

    **1.** On initialise l’accumulateur *avant* la boucle, on le met à jour *dans* la boucle (un cran d’indentation de plus), on le renvoie *après* la boucle :

    ```python
    def somme_entre(a, b):
        total = 0
        for i in range(a, b + 1):
            total = total + i
        return total

    assert somme_entre(3, 6) == 18    # 3 + 4 + 5 + 6
    ```

    **2.** `somme_entre(3, 6)` renvoie bien `18`.

    **3.** L’accumulateur serait remis à `0` à chaque tour : à la fin, `total` ne contiendrait que la dernière valeur ajoutée, `b`. Ici, la fonction renverrait `6` au lieu de `18`.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 15</span> — Sommes <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-15 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

1.  Écrire `somme(n)` qui renvoie $1 + 2 + \dots + n$ à l’aide d’un accumulateur. Vérifier que `somme(100)` vaut `5050`.

2.  Écrire `somme_carres(n)` qui renvoie $1^2 + 2^2 + \dots + n^2$.

??? corrige "Corrigé"

    ```python
    def somme(n):
        total = 0
        for i in range(1, n + 1):
            total = total + i
        return total

    def somme_carres(n):
        total = 0
        for i in range(1, n + 1):
            total = total + i * i
        return total

    assert somme(100) == 5050
    assert somme_carres(3) == 14      # 1 + 4 + 9
    ```

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 16</span> — Table de multiplication <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-16 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `table(n)` qui **affiche**, une par ligne, les dix lignes de la table de multiplication de `n`, sous la forme `n x i = ...`. *Rappel :* `print(a, "x", b)` affiche les valeurs séparées par des espaces.

```text
>>> table(7)
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
...
7 x 10 = 70
```

??? corrige "Corrigé"

    La fonction **affiche** et ne renvoie rien : on ne peut donc pas la tester avec `assert`, on vérifie l’affichage à l’écran.

    ```python
    def table(n):
        for i in range(1, 11):
            print(n, "x", i, "=", n * i)

    table(7)    # affiche 7 x 1 = 7, puis 7 x 2 = 14, ... jusqu'a 7 x 10 = 70
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 17</span> — Construire une chaîne <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-17 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `ligne_etoiles(n)` qui renvoie une chaîne formée de `n` étoiles, en partant d’une chaîne **vide** `""` que l’on complète à chaque tour (`chaine = chaine + "*"`). C’est le même motif d’accumulateur que ci-dessus, appliqué à du texte.0

??? pouce "Coup de pouce"

    Combien de tours de boucle faut-il ? Quelle valeur la chaîne doit-elle avoir avant le premier tour ?

```text
>>> ligne_etoiles(5)
'*****'
```

??? corrige "Corrigé"

    On part d’une chaîne vide et on ajoute une étoile à chaque tour (accumulateur de texte, exactement comme l’accumulateur numérique ci-dessus).

    ```python
    def ligne_etoiles(n):
        chaine = ""
        for i in range(n):
            chaine = chaine + "*"
        return chaine

    assert ligne_etoiles(5) == "*****"
    assert ligne_etoiles(0) == ""
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 18</span> — Factorielle <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-18 }

<span class="run" title="À programmer et tester sur machine">▶</span> Une course réunit `n` coureurs. Combien d’ordres d’arrivée sont possibles ? Le vainqueur peut être l’un des `n` coureurs, le deuxième l’un des `n - 1` restants, et ainsi de suite : il y a $n \times (n-1) \times \dots \times 2 \times 1$ ordres possibles. Ce produit $1 \times 2 \times \dots \times n$ s’appelle la **factorielle** de `n`, avec la convention $0! = 1$ (sans coureur, un seul classement : le classement vide). Écrire `factorielle(n)` avec un accumulateur. Tester `factorielle(0)` et `factorielle(5)`.0

??? pouce "Coup de pouce"

    C’est le motif de la somme du cours, avec une multiplication. Mais si l’accumulateur part de `0`, que vaut le produit à la fin ? Par quelle valeur faut-il l’initialiser ?

??? corrige "Corrigé"

    L’accumulateur d’un *produit* s’initialise à `1`. La boucle `range(2, n+1)` ne fait aucun tour si `n` vaut `0` ou `1`, ce qui donne bien `1`.

    ```python
    def factorielle(n):
        produit = 1
        for i in range(2, n + 1):
            produit = produit * i
        return produit

    assert factorielle(0) == 1
    assert factorielle(1) == 1
    assert factorielle(5) == 120
    ```

    Avec 5 coureurs, il y a donc `120` ordres d’arrivée possibles ; avec 10 coureurs, déjà `factorielle(10)` $=$ `3628800`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 19</span> — Compter les voyelles <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-19 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `compter_voyelles(mot)` qui renvoie le nombre de voyelles d’une chaîne (on comptera aussi le `y`). *Rappel :* on parcourt une chaîne caractère par caractère avec `for lettre in mot:` et on teste `if lettre in "aeiouy":`.0

??? pouce "Coup de pouce"

    C’est un **compteur** : une variable qui part de `0` et augmente de `1` chaque fois que la condition est vraie.

```text
>>> compter_voyelles("bonjour")
3
```

??? corrige "Corrigé"

    ```python
    def compter_voyelles(mot):
        n = 0
        for lettre in mot:
            if lettre in "aeiouyAEIOUY":
                n = n + 1
        return n

    assert compter_voyelles("bonjour") == 3
    assert compter_voyelles("") == 0
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 20</span> — Diviseurs et nombres parfaits <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-20 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

1.  Écrire `somme_diviseurs(n)` qui renvoie la somme de tous les diviseurs de `n` (y compris `1` et `n`).

2.  Un entier est **parfait** si la somme de ses diviseurs vaut `2*n`. Écrire `est_parfait(n)`.

3.  Afficher tous les nombres parfaits strictement inférieurs à `100`.0

    ??? pouce "Coup de pouce"

        Un diviseur `d` de `n` vérifie `n % d == 0`. Quelles valeurs de `d` faut-il essayer ? Pour la question 3, réutiliser `est_parfait` dans une boucle.

```text
>>> somme_diviseurs(6)
12
>>> est_parfait(28)
True
```

??? corrige "Corrigé"

    ```python
    def somme_diviseurs(n):
        total = 0
        for d in range(1, n + 1):
            if n % d == 0:
                total = total + d
        return total

    def est_parfait(n):
        return somme_diviseurs(n) == 2 * n

    for k in range(1, 100):
        if est_parfait(k):
            print(k)          # affiche 6 puis 28

    assert somme_diviseurs(6) == 12
    assert est_parfait(28) == True
    assert est_parfait(12) == False
    ```

    Les nombres parfaits inférieurs à 100 sont `6` et `28`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 21</span> — Compter les occurrences d’une lettre <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-21 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `occurrences(caractere, mot)` qui renvoie le nombre de fois que `caractere` apparaît dans `mot`.0

??? pouce "Coup de pouce"

    Même schéma que « Compter les voyelles » : seule la condition testée sur chaque lettre change.

```text
>>> occurrences("a", "banana")
3
```

??? corrige "Corrigé"

    ```python
    def occurrences(caractere, mot):
        n = 0
        for lettre in mot:
            if lettre == caractere:
                n = n + 1
        return n

    assert occurrences("a", "banana") == 3
    assert occurrences("z", "banana") == 0
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 22</span> — Puissance sans `**` <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-22 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `puissance(a, n)` qui renvoie $a^n$ à l’aide d’une boucle (accumulateur de produit), **sans** utiliser l’opérateur `**`. On rappelle que $a^0 = 1$.0

??? pouce "Coup de pouce"

    $a^n = a \times a \times \dots \times a$ ($n$ facteurs) : combien de tours de boucle, et quelle valeur initiale pour l’accumulateur ?

```text
>>> puissance(2, 10)
1024
>>> puissance(5, 0)
1
```

??? corrige "Corrigé"

    L’accumulateur d’un produit s’initialise à `1`. La boucle fait `n` tours ; si `n` vaut `0`, elle n’en fait aucun et renvoie `1`.

    ```python
    def puissance(a, n):
        resultat = 1
        for i in range(n):
            resultat = resultat * a
        return resultat

    assert puissance(2, 10) == 1024
    assert puissance(5, 0) == 1
    assert puissance(3, 3) == 27
    ```

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 23</span> — FizzBuzz <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-23 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `fizzbuzz(n)` qui **affiche**, un par ligne, les entiers de `1` à `n`, en affichant à la place `Fizz` pour chaque multiple de 3, `Buzz` pour chaque multiple de 5, et `FizzBuzz` pour chaque multiple de 3 *et* de 5.0

??? pouce "Coup de pouce"

    Dans quel **ordre** tester les cas ? Pour `15`, lequel des tests `i % 3 == 0` et `i % 5 == 0` serait capté en premier ?

0

??? pouce "Coup de pouce 2 (début de solution)"

    `for i in range(1, n + 1):`  
    `if i % 3 == 0 and i % 5 == 0:`  
    `print("FizzBuzz")`  
    `elif ...`

```text
>>> fizzbuzz(5)
1
2
Fizz
4
Buzz
```

??? corrige "Corrigé"

    Le piège : il faut tester le cas « multiple de 3 **et** de 5 » (c’est-à-dire multiple de 15) **en premier**, sinon il serait capté par `% 3` et ne donnerait jamais « FizzBuzz ».

    ```python
    def fizzbuzz(n):
        for i in range(1, n + 1):
            if i % 15 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)

    fizzbuzz(15)    # la derniere ligne affichee doit etre FizzBuzz
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 24</span> — Un triangle d’étoiles <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-24 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `triangle(n)` qui **affiche** un triangle de `n` lignes : la ligne numéro `i` contient `i` étoiles.0

??? pouce "Coup de pouce"

    Une ligne affichée par tour de boucle : quelles valeurs `i` doit-il prendre ? Pour construire la ligne, réutiliser `ligne_etoiles` de l’exercice « Construire une chaîne », ou tester `"*" * 3` dans la console.

```text
>>> triangle(3)
*
**
***
```

??? corrige "Corrigé"

    `"*" * i` construit une chaîne de `i` étoiles ; on affiche une ligne par tour de boucle.

    ```python
    def triangle(n):
        for i in range(1, n + 1):
            print("*" * i)

    triangle(3)    # affiche *, puis **, puis ***
    ```

    Variante sans `"*" * i`, en réutilisant `ligne_etoiles` : `print(ligne_etoiles(i))` à chaque tour.

### Les boucles non bornées (`while`)

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 25</span> — Compte à rebours <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-25 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `compte_a_rebours(n)` qui affiche `n`, `n-1`, …, `1` à l’aide d’une boucle `while`. **Justifier** que cette boucle se termine en exhibant un **variant**.

??? corrige "Corrigé"

    ```python
    def compte_a_rebours(n):
        while n > 0:
            print(n)
            n = n - 1
    ```

    **Terminaison.** La variable `n` est un **variant** : elle est positive tant qu’on entre dans la boucle (`n > 0`) et diminue de `1` à chaque tour. Une suite d’entiers positifs qui décroît strictement atteint forcément `0`, ce qui rend la condition fausse : la boucle se termine.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 26</span> — Décortiquer un entier <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-26 }

<span class="run" title="À programmer et tester sur machine">▶</span> À l’aide de `n % 10` (dernier chiffre) et `n // 10` (on retire le dernier chiffre) :

1.  écrire `nombre_de_chiffres(n)` qui renvoie combien de chiffres possède `n` ;

2.  écrire `somme_chiffres(n)` qui renvoie la somme des chiffres de `n`.0

    ??? pouce "Coup de pouce"

        Tant que `n` n’est pas nul, on traite le dernier chiffre puis on le retire. Attention au cas `n = 0` : combien de chiffres possède-t-il ?

```text
>>> nombre_de_chiffres(347)
3
>>> somme_chiffres(347)
14
```

??? corrige "Corrigé"

    ```python
    def nombre_de_chiffres(n):
        if n == 0:
            return 1
        compteur = 0
        while n > 0:
            n = n // 10
            compteur = compteur + 1
        return compteur

    def somme_chiffres(n):
        total = 0
        while n > 0:
            total = total + n % 10
            n = n // 10
        return total

    assert nombre_de_chiffres(347) == 3
    assert nombre_de_chiffres(0) == 1
    assert somme_chiffres(347) == 14
    ```

    Dans les deux fonctions, `n` est un **variant** : c’est un entier positif, et l’affectation `n = n // 10` le fait décroître strictement à chaque tour (car `n` $\geqslant 1$ dans la boucle), jusqu’à `0`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 27</span> — Racine entière <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-27 }

<span class="run" title="À programmer et tester sur machine">▶</span> Avec `n` dalles carrées, on veut carreler la plus grande terrasse **carrée** possible : `k` dalles de côté, donc $k \times k$ dalles, sans dépasser les `n` dalles disponibles. Ce plus grand entier `k` tel que $k \times k \leqslant n$ s’appelle la **racine entière** de `n` (avec `n` $\geqslant 0$). Écrire `racine_entiere(n)` avec une boucle `while`, **sans** utiliser `**` ni de racine carrée toute faite. Justifier la terminaison.0

??? pouce "Coup de pouce"

    Partir de `k = 0` et augmenter `k` tant que le *suivant*, `k + 1`, convient encore. Pour la terminaison, chercher une quantité entière positive qui diminue.

```text
>>> racine_entiere(15)
3
>>> racine_entiere(16)
4
```

??? corrige "Corrigé"

    ```python
    def racine_entiere(n):
        k = 0
        while (k + 1) * (k + 1) <= n:
            k = k + 1
        return k

    assert racine_entiere(15) == 3
    assert racine_entiere(16) == 4
    assert racine_entiere(0) == 0
    ```

    Avec 15 dalles, la plus grande terrasse carrée fait $3 \times 3$ (9 dalles) ; avec 16 dalles, $4 \times 4$. **Terminaison.** La quantité `n - k*k` décroît strictement (`k` augmente de `1` à chaque tour) et reste positive tant qu’on boucle : la boucle s’arrête donc.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 28</span> — Dépasser un seuil <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-28 }

<span class="run" title="À programmer et tester sur machine">▶</span> Léa remplit une tirelire : le jour 1 elle y met 1 €, le jour 2 elle y met 2 €, le jour 3 elle y met 3 €, et ainsi de suite. Au bout de `n` jours, la tirelire contient donc $1 + 2 + \dots + n$ euros. Écrire `seuil(s)` qui renvoie le premier jour `n` où la tirelire contient **strictement plus** de `s` euros. **Justifier** la terminaison. Tester : `seuil(1000)` doit renvoyer `45`.0

??? pouce "Coup de pouce"

    Deux variables évoluent ensemble : l’entier `n` et le total `1 + 2 + ... + n`. Quelle condition écrire dans le `while` pour continuer *tant que* le seuil n’est pas dépassé ?

??? corrige "Corrigé"

    ```python
    def seuil(s):
        n = 0
        total = 0
        while total <= s:
            n = n + 1
            total = total + n
        return n

    assert seuil(1000) == 45      # 1+...+44 = 990, 1+...+45 = 1035
    ```

    Le total `total` est le contenu de la tirelire et `n` le numéro du jour : Léa dépasse 1000 € le 45<sup>e</sup> jour. **Terminaison.** La quantité `s - total` décroît strictement à chaque tour (on ajoute au moins `1` à `total`) : elle finit par devenir négative, ce qui arrête la boucle.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 29</span> — PGCD (algorithme d’Euclide) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-29 }

<span class="run" title="À programmer et tester sur machine">▶</span> Pour calculer le PGCD de deux entiers strictement positifs, on remplace répétitivement le plus grand par sa différence avec le plus petit, jusqu’à ce que les deux soient égaux : cette valeur commune est le PGCD.

1.  Écrire `pgcd(a, b)` avec une boucle `while a != b`.

2.  **Justifier la terminaison** : trouver une quantité qui décroît strictement à chaque tour et reste positive.0

    ??? pouce "Coup de pouce"

        Faire d’abord à la main `pgcd(12, 18)` : noter les valeurs de `a` et `b` à chaque tour. À chaque tour, lequel des deux modifie-t-on ?

    0

    ??? pouce "Coup de pouce 2 (début de solution)"

        `while a != b:`  
        `if a > b:`  
        `a = a - b`  
        `else:` …

```text
>>> pgcd(12, 18)
6
```

??? corrige "Corrigé"

    ```python
    def pgcd(a, b):
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        return a

    assert pgcd(12, 18) == 6
    assert pgcd(7, 7) == 7
    assert pgcd(1071, 462) == 21
    ```

    **Terminaison.** La quantité `a + b` est un variant : à chaque tour on retranche à l’un des deux une valeur strictement positive, donc `a + b` décroît strictement tout en restant $\geqslant 2$. La boucle ne peut donc pas tourner indéfiniment.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 30</span> — Racine numérique <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-30 }

<span class="run" title="À programmer et tester sur machine">▶</span> La **racine numérique** d’un entier s’obtient en additionnant ses chiffres, puis en recommençant sur le résultat, jusqu’à n’obtenir qu’un seul chiffre. Par exemple : $347 \rightarrow 3+4+7 = 14 \rightarrow 1+4 = 5$. Écrire `racine_numerique(n)` à l’aide d’une boucle `while`. Justifier la terminaison.0

??? pouce "Coup de pouce"

    Une fonction déjà écrite dans l’exercice « Décortiquer un entier » fait l’essentiel du travail. Comment reconnaître qu’un entier n’a plus qu’un seul chiffre ?

0

??? pouce "Coup de pouce 2 (début de solution)"

    `def racine_numerique(n):`  
    `while n >= 10:`  
    …

```text
>>> racine_numerique(347)
5
>>> racine_numerique(12345)
6
```

??? corrige "Corrigé"

    Tant que `n` a plus d’un chiffre, on le remplace par la somme de ses chiffres.

    ```python
    def somme_chiffres(n):        # deja ecrite plus haut
        total = 0
        while n > 0:
            total = total + n % 10
            n = n // 10
        return total

    def racine_numerique(n):
        while n >= 10:
            n = somme_chiffres(n)
        return n

    assert racine_numerique(347) == 5
    assert racine_numerique(9) == 9
    assert racine_numerique(12345) == 6
    ```

    **Terminaison.** Dès que `n` a au moins deux chiffres, la somme de ses chiffres est *strictement plus petite* que `n` : la valeur de `n` décroît strictement à chaque tour tout en restant positive, jusqu’à passer sous `10`.

### Fonctions : spécifier et tester

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 31</span> — Nombres premiers <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-31 }

<span class="run" title="À programmer et tester sur machine">▶</span> Un entier `n` est premier s’il vaut au moins 2 et n’admet aucun diviseur autre que 1 et lui-même.

1.  Écrire `est_premier(n)`.

2.  Rédiger un **jeu de tests** (`assert`) couvrant : un premier, un non-premier, et les cas limites `0`, `1`, `2`.0

    ??? pouce "Coup de pouce"

        Traiter d’abord les entiers inférieurs à `2`. Ensuite, chercher un diviseur entre `2` et `n - 1` : dès qu’on en trouve un, la réponse est connue.

??? corrige "Corrigé"

    ```python
    def est_premier(n):
        if n < 2:
            return False
        for d in range(2, n):
            if n % d == 0:
                return False
        return True

    assert est_premier(2) == True      # cas limite
    assert est_premier(7) == True
    assert est_premier(97) == True
    assert est_premier(0) == False     # cas limite
    assert est_premier(1) == False     # cas limite
    assert est_premier(9) == False
    ```

    Dès qu’un diviseur est trouvé, `return False` sort immédiatement de la fonction : inutile de continuer.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 32</span> — Palindrome <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-32 }

<span class="run" title="À programmer et tester sur machine">▶</span> Un palindrome est un mot qui se lit de la même façon dans les deux sens (« radar », « kayak »). Écrire une fonction booléenne `est_palindrome(mot)` qui le détecte. Prévoir les cas limites (mot vide, une seule lettre). *(On rappelle que* `len(mot)` *est le nombre de caractères de* `mot` *et que* `mot[i]` *est le caractère de position* `i`*, la première position étant* `0`*.)*0

??? pouce "Coup de pouce"

    Comparer le premier et le dernier caractère, puis se rapprocher du centre avec deux indices `i` et `j`. Quand faut-il s’arrêter ?

```text
>>> est_palindrome("radar")
True
>>> est_palindrome("bonjour")
False
```

??? corrige "Corrigé"

    On compare les caractères par paires, en partant des deux bords et en se rapprochant du centre avec deux indices `i` et `j`. La quantité `j - i` est un variant : elle diminue de 2 à chaque tour.

    ```python
    def est_palindrome(mot):
        i = 0
        j = len(mot) - 1
        while i < j:
            if mot[i] != mot[j]:
                return False
            i = i + 1
            j = j - 1
        return True

    assert est_palindrome("radar") == True
    assert est_palindrome("bonjour") == False
    assert est_palindrome("") == True      # cas limites
    assert est_palindrome("a") == True
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 33</span> — Jouer avec les bords d’un mot <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-33 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

1.  Écrire `meme_bord(mot)` qui renvoie `True` si le mot commence et se termine par la même lettre. *(On rappelle que* `mot[0]` *est la première lettre et* `mot[-1]` *la dernière.)*

2.  Écrire `memes_bords(mot1, mot2)` qui renvoie `True` si les deux mots commencent par la même lettre **et** finissent par la même lettre.0

    ??? pouce "Coup de pouce"

        Aucune boucle n’est nécessaire : une seule comparaison (ou deux, reliées par `and`) suffit. Que se passe-t-il avec le mot vide ?

```text
>>> meme_bord("radar")
True
>>> memes_bords("chat", "chocolat")
True
```

??? corrige "Corrigé"

    ```python
    def meme_bord(mot):
        if mot == "":
            return True          # cas limite : mot vide
        return mot[0] == mot[-1]

    def memes_bords(mot1, mot2):
        return mot1[0] == mot2[0] and mot1[-1] == mot2[-1]

    assert meme_bord("radar") == True
    assert meme_bord("bonjour") == False
    assert memes_bords("chat", "chocolat") == True
    assert memes_bords("chat", "chien") == False
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 34</span> — Le bug qui passe les tests <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-34 }

On propose la fonction suivante, censée additionner deux nombres :

```python
def addition(a, b):
    return a * b
```

1.  Vérifier que le jeu de tests `assert addition(2, 2) == 4` et `assert addition(0, 0) == 0` **passe** pourtant sans erreur. Expliquer pourquoi.

2.  Proposer un test `assert` qui **démasque** le bug.0

    ??? pouce "Coup de pouce"

        Comparer `2 + 2` et `2 * 2`, puis `0 + 0` et `0 * 0`. Chercher deux nombres pour lesquels somme et produit diffèrent.

3.  Que peut-on en conclure sur la phrase du programme : « *le succès d’un jeu de tests ne garantit pas la correction d’un programme* » ?

??? corrige "Corrigé"

    **1.** La fonction renvoie `a * b` au lieu de `a + b`. Or les deux tests choisis tombent sur des cas où produit et somme coïncident : $2 \times 2 = 2 + 2 = 4$ et $0 \times 0 = 0 + 0 = 0$. Les `assert` passent donc, alors que la fonction est fausse.

    **2.** Un test qui les sépare démasque le bug, par exemple :

    ```python
    assert addition(1, 3) == 4    # echoue : 1 * 3 = 3, pas 4
    ```

    **3.** Réussir un jeu de tests prouve seulement que la fonction est correcte **sur les cas testés**, jamais qu’elle l’est *en général*. Un jeu de tests mal choisi peut laisser passer un programme faux : c’est exactement le sens de la phrase du programme. D’où l’importance de tester des cas **variés** (normaux, limites, particuliers).

### Exercices de synthèse

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 35</span> — Les horaires du bus <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-35 }

Sur une ligne de bus de Monaco, le premier bus part à **6 h 30**, puis il en part un toutes les **12 minutes** ; aucun bus ne part après **21 h 00**. Pour calculer facilement, on compte les heures en **minutes écoulées depuis minuit** : 6 h 30 correspond à $6 \times 60 + 30 = 390$.

1.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire `en_minutes(h, m)` qui renvoie le nombre de minutes écoulées depuis minuit à l’heure `h` h `m`.

2.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire `prochain_bus(t)` qui renvoie l’horaire (en minutes) du premier bus partant à l’instant `t` ou après, et `-1` s’il n’y a plus de bus ce jour-là. On utilisera une boucle `while`.0

    ??? pouce "Coup de pouce"

        Partir de l’horaire du premier bus et passer au bus suivant tant qu’il part trop tôt. Une fois sorti de la boucle, ce bus part-il encore avant 21 h 00 ?

    0

    ??? pouce "Coup de pouce 2 (début de solution)"

        `def prochain_bus(t):`  
        `depart = 390`  
        `while depart < t:`  
        `depart = depart + 12`  
        …

3.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire `attente(h, m)` qui renvoie le nombre de minutes à attendre le prochain bus quand on arrive à l’arrêt à `h` h `m`, et `-1` s’il n’y a plus de bus.

4.  Quel est l’horaire du **dernier** bus de la journée ? L’écrire en heures et minutes à l’aide de `//` et `%`.

```text
>>> en_minutes(6, 30)
390
>>> prochain_bus(400)
402
>>> attente(8, 0)
6
>>> attente(22, 15)
-1
```

??? corrige "Corrigé"

    On part du premier bus (390) et on passe au suivant (`+ 12`) tant qu’il part avant l’instant `t`. En sortie de boucle, il reste à vérifier que ce bus part encore avant 21 h 00, soit $21 \times 60 = 1260$.

    ```python
    def en_minutes(h, m):
        return h * 60 + m

    def prochain_bus(t):
        depart = 390                  # 6 h 30
        while depart < t:
            depart = depart + 12      # bus suivant
        if depart > 1260:             # apres 21 h 00 : plus de bus
            return -1
        return depart

    def attente(h, m):
        t = en_minutes(h, m)
        depart = prochain_bus(t)
        if depart == -1:
            return -1
        return depart - t

    assert en_minutes(6, 30) == 390
    assert prochain_bus(400) == 402
    assert prochain_bus(0) == 390       # avant le premier bus
    assert prochain_bus(402) == 402     # un bus part pile a cet instant
    assert attente(8, 0) == 6
    assert attente(22, 15) == -1
    ```

    **4.** Les départs ont lieu à $390 + 12k$. Comme $1260 - 390 = 870 = 72 \times 12 + 6$, le dernier départ est $390 + 72 \times 12 = 1254$ minutes, et `1254 // 60` vaut `20`, `1254 % 60` vaut `54` : le dernier bus part à **20 h 54**. (On peut le vérifier : `prochain_bus(1249)` renvoie `1254` et `prochain_bus(1255)` renvoie `-1`.)

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 36</span> — Un mot de passe robuste <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-36 }

Un site exige des mots de passe **robustes** : au moins **8 caractères**, au moins une **majuscule**, au moins un **chiffre** et au moins un **caractère spécial** parmi `!?@#$%&*`. *(On rappelle que* `len(mdp)` *est le nombre de caractères de* `mdp`*.)*

1.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire `compter_chiffres(mdp)` qui renvoie le nombre de chiffres que contient la chaîne `mdp`.

2.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire `est_robuste(mdp)` qui renvoie `True` si le mot de passe respecte les quatre règles, `False` sinon.0

    ??? pouce "Coup de pouce"

        Pour la question 1, reprendre l’exercice « Compter les voyelles » : seule la chaîne de référence change (`"0123456789"` au lieu de `"aeiouy"`). Compter de même les majuscules et les caractères spéciaux.

    0

    ??? pouce "Coup de pouce 2 (début de solution)"

        `def est_robuste(mdp):`  
        `majuscules = 0`  
        `speciaux = 0`  
        `for c in mdp:`  
        `if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":`  
        …

3.  Rédiger un **jeu de tests** (`assert`) contenant un mot de passe robuste et, pour **chacune** des quatre règles, un mot de passe qui enfreint **cette seule** règle et respecte les trois autres.

```text
>>> compter_chiffres("Monaco98")
2
>>> est_robuste("Monaco98!")
True
>>> est_robuste("monaco98!")
False
```

??? corrige "Corrigé"

    Même motif que « Compter les voyelles » : un compteur par catégorie de caractères, puis les quatre règles reliées par `and`.

    ```python
    def compter_chiffres(mdp):
        n = 0
        for c in mdp:
            if c in "0123456789":
                n = n + 1
        return n

    def est_robuste(mdp):
        majuscules = 0
        speciaux = 0
        for c in mdp:
            if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                majuscules = majuscules + 1
            if c in "!?@#$%&*":
                speciaux = speciaux + 1
        return (len(mdp) >= 8 and majuscules >= 1
                and compter_chiffres(mdp) >= 1 and speciaux >= 1)

    assert compter_chiffres("Monaco98") == 2
    assert compter_chiffres("") == 0
    assert est_robuste("Monaco98!") == True
    assert est_robuste("Mon98!") == False       # trop court
    assert est_robuste("monaco98!") == False    # pas de majuscule
    assert est_robuste("Monacooo!") == False    # pas de chiffre
    assert est_robuste("Monaco98") == False     # pas de caractere special
    ```

    Chaque mot de passe refusé n’enfreint qu’**une seule** règle : si un test échoue, on sait immédiatement quelle condition est mal écrite.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 37</span> — Nombres premiers jumeaux <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-37 }

Deux nombres premiers sont **jumeaux** si leur différence vaut `2` (par exemple `3` et `5`, ou `11` et `13`).

<span class="run" title="À programmer et tester sur machine">▶</span> En réutilisant `est_premier`, écrire `premiers_jumeaux(n)` qui **affiche**, un couple par ligne, tous les couples `p` et `p+2` de premiers jumeaux tels que les deux nombres soient strictement inférieurs à `n`.0

??? pouce "Coup de pouce"

    Parcourir les candidats `p` un par un et tester *deux* conditions avec `and`. Quelle condition garantit que `p + 2` reste strictement inférieur à `n` ?

0

??? pouce "Coup de pouce 2 (début de solution)"

    `for p in range(2, n):`  
    `if p + 2 < n and est_premier(p) and` …

```text
>>> premiers_jumeaux(20)
3 et 5
5 et 7
11 et 13
17 et 19
```

??? corrige "Corrigé"

    On réutilise `est_premier`. La condition `p + 2 < n` garantit que les *deux* nombres du couple sont strictement inférieurs à `n`.

    ```python
    def premiers_jumeaux(n):
        for p in range(2, n):
            if p + 2 < n and est_premier(p) and est_premier(p + 2):
                print(p, "et", p + 2)

    premiers_jumeaux(20)    # affiche 3 et 5, 5 et 7, 11 et 13, 17 et 19
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 38</span> — Une somme selon un assistant d’IA <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> { #ex-01-38 }

Un élève demande à un assistant d’IA : « Écris une fonction Python qui renvoie la somme des entiers impairs de `1` à `n`. » Voici la réponse obtenue.

```python
def somme_impairs(n):
    somme = 0
    for i in range(1, n, 2):
        somme = somme + i
    return somme
```

« `range(1, n, 2)` produit `1, 3, 5,` … jusqu’à `n` ; on ajoute chaque valeur à `somme`, qui est renvoyée à la fin. Par exemple, `somme_impairs(5)` renvoie `1 + 3 + 5`, soit `9`. »

1.  La réponse est-elle correcte ? Faire la trace de `somme_impairs(5)` (valeurs successives de `i` et de `somme`), puis <span class="run" title="À programmer et tester sur machine">▶</span> vérifier dans la console.

2.  Localiser et corriger l’erreur.

3.  Quelle vérification simple, faite avant de faire confiance à la réponse, aurait suffi à détecter l’erreur ?0

    ??? pouce "Coup de pouce"

        Relire la définition de `range(a, b, pas)` dans le cours : la borne `b` est-elle atteinte ?

??? corrige "Corrigé"

    **1.** Non. Trace de `somme_impairs(5)` : `range(1, 5, 2)` donne `1` puis `3`, et s’arrête **avant** `5` (la borne est exclue). `somme` vaut `0`, puis `1`, puis `4` : la fonction renvoie **`4`**, et non `9` comme l’annonce pourtant l’assistant.

    ```text
    >>> somme_impairs(5)
    4
    ```

    **2.** L’erreur est la borne du `range` : `range(1, n, 2)` exclut `n`. Il faut `range(1, n + 1, 2)` :

    ```python
    def somme_impairs(n):
        somme = 0
        for i in range(1, n + 1, 2):
            somme = somme + i
        return somme

    print(somme_impairs(5))    # 9
    print(somme_impairs(6))    # 9  (1 + 3 + 5)
    ```

    **3.** Exécuter l’exemple que l’assistant donne lui-même : il annonce `9` pour `somme_impairs(5)`, la console affiche `4`. La réponse se contredit ; un seul appel suffisait. Le cas où `n` est lui-même impair est justement le cas limite à tester.
