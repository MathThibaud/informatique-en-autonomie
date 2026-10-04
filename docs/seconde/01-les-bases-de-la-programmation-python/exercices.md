# Exercices

<p class="sous-titre">Les bases de la programmation Python</p>

!!! consignes "Mode d’emploi"

    - Niveau : ★ échauffement, ★★ classique (niveau bac), ★★★ défi ; les *coups de pouce* et les *corrigés* se déplient sous chaque exercice.

    - Sauf mention <span class="tag">sur papier</span> , les exercices se font **sur machine** (Spyder ou Basthon) : on écrit dans l’éditeur, on exécute, on vérifie dans la console.

    - <span class="run" title="À programmer et tester sur machine">▶</span> *signale les exercices où l’on écrit un vrai programme à tester.*

    - Avancez dans l’ordre : chaque section suit la progression du cours.

    - Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la charte d’usage de l’IA.

### Premiers pas : afficher

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — Bonjour <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-1 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Écrire un programme qui affiche : *Bonjour, je m’appelle …* (en y mettant son prénom).

??? corrige "Corrigé"

    !!! remarque "Remarque"

        Plusieurs écritures sont souvent possibles ; on en donne une simple. Les exercices marqués « sur papier » indiquent le résultat attendu. Rappel utile : `input` renvoie toujours du texte, on convertit avec `int(...)` pour calculer.

    ```python
    print("Bonjour, je m'appelle Marie")
    ```

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 2</span> — Le menu de la cantine <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-2 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Écrire un programme qui affiche le menu du jour **sur trois lignes** : l’entrée, le plat, puis le dessert (par exemple *Entrée : salade niçoise*).

??? corrige "Corrigé"

    Une instruction `print` par ligne à afficher.

    ```python
    print("Entree : salade nicoise")
    print("Plat : lasagnes")
    print("Dessert : tarte aux pommes")
    ```

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 3</span> — Texte ou calcul ? <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-3 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Écrire un programme qui affiche **exactement** les trois lignes ci-dessous. La deuxième doit être *calculée* par Python (interdit d’écrire `17` soi-même !).

```text
12 + 5
17
Bonjour Monaco
```

??? pouce "Coup de pouce"

    Pour la troisième ligne, collez deux morceaux de texte avec `+` (sans oublier l’espace entre les deux mots).

??? corrige "Corrigé"

    Entre guillemets, Python affiche le texte tel quel ; sans guillemets, il calcule. Le `+` entre deux textes les colle (attention à l’espace après *Bonjour*).

    ```python
    print("12 + 5")
    print(12 + 5)
    print("Bonjour " + "Monaco")
    ```

### Variables et types

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 4</span> — Deux variables <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-4 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Créer une variable `sport` contenant son sport préféré (du texte) et une variable `heures` contenant le nombre d’heures qu’on y consacre par semaine (un nombre), puis les afficher.

??? corrige "Corrigé"

    Le texte va entre guillemets, le nombre non.

    ```python
    sport = "natation"
    heures = 4
    print(sport)
    print(heures)
    ```

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 5</span> — Valeur finale <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-5 }

<span class="tag">sur papier</span>  Sans machine, donner la valeur finale de `a` *et* de `b`, puis vérifier.

```python
a = 5
b = a + 1
a = 10
```

??? corrige "Corrigé"

    *Sur papier.* `a` $= \mathbf{10}$ et `b` $= \mathbf{6}$. La valeur de `b` a été calculée *une fois pour toutes* quand `a` valait $5$ : modifier `a` ensuite ne change pas `b`.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 6</span> — Des noms parlants <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-6 }

<span class="tag">sur papier</span>  Ce programme calcule le prix de $3$ places de cinéma à $12$ €, mais ses noms de variables ne veulent rien dire :

```python
x = 12
y = 3
z = x * y
```

1.  Proposer des noms **parlants** (et valides) pour `x`, `y` et `z`.

2.  Un camarade propose `prix place`, `3places` et `total€`. Pourquoi Python les refuse-t-il ?

??? corrige "Corrigé"

    *Sur papier.*

    1.  Par exemple `prix_place`, `nb_places` et `total`.

    2.  `prix place` contient une espace ; `3places` commence par un chiffre ; `total€` contient un symbole (`€`) interdit dans un nom.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — La tirelire <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-7 }

<span class="run" title="À programmer et tester sur machine">▶</span>  La variable `tirelire` de Léa vaut $20$. Sa grand-mère **double** son contenu, puis Léa dépense $15$ € au cinéma, puis elle ajoute $8$ € d’argent de poche. En modifiant `tirelire` à chaque étape, afficher le contenu final (attendu : $33$).

??? pouce "Coup de pouce"

    Chaque étape s’écrit `tirelire = ...` en partant de l’ancienne valeur de `tirelire`.

??? corrige "Corrigé"

    On met à jour `tirelire` à partir de sa propre valeur, étape par étape.

    ```python
    tirelire = 20
    tirelire = tirelire * 2    # 40
    tirelire = tirelire - 15   # 25
    tirelire = tirelire + 8    # 33
    print(tirelire)
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Le type d’un résultat <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-8 }

<span class="tag">sur papier</span>  Sans machine, donner la valeur et le type (`int`, `float` ou `str`) du **résultat** de chaque expression, puis vérifier avec `type(...)` : `7 + 2` ; `7 / 7` ; `"7" + "2"` ; `3 * 1.0` ; `int("5") + 1` ; `str(4) + "0"`.

??? pouce "Coup de pouce"

    Pour chaque expression, demandez-vous si les valeurs sont des nombres ou du texte (entre guillemets). Relisez dans le cours ce que donne toujours la division `/`.

??? corrige "Corrigé"

    *Sur papier.*

    - `7 + 2` $\to$ `9` (`int`) ; `7 / 7` $\to$ `1.0` (`float` : la division `/` donne toujours un flottant) ;

    - `"7" + "2"` $\to$ `"72"` (`str` : on colle deux textes) ; `3 * 1.0` $\to$ `3.0` (`float`) ;

    - `int("5") + 1` $\to$ `6` (`int`) ; `str(4) + "0"` $\to$ `"40"` (`str`).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 9</span> — L’échange <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-9 }

<span class="run" title="À programmer et tester sur machine">▶</span>  On a `a = 1` et `b = 2`. Écrire les instructions qui **échangent** leurs valeurs (à la fin, `a` vaut $2$ et `b` vaut $1$).

??? pouce "Coup de pouce"

    Si l’on écrit directement `a = b`, l’ancienne valeur de `a` est perdue : rangez-la d’abord dans une troisième variable `temporaire`.

??? corrige "Corrigé"

    On garde l’une des valeurs de côté dans une variable `temporaire`, sinon on l’écrase.

    ```python
    a = 1
    b = 2
    temporaire = a
    a = b
    b = temporaire
    ```

### Calculs

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 10</span> — Somme et produit <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-10 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Ranger deux nombres dans `a` et `b`, puis afficher leur somme *et* leur produit.

??? corrige "Corrigé"

    ```python
    a = 6
    b = 4
    print(a + b)   # 10
    print(a * b)   # 24
    ```

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 11</span> — Le trajet <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-11 }

<span class="run" title="À programmer et tester sur machine">▶</span>  À partir de deux variables `vitesse` (en km/h) et `duree` (en heures), calculer et afficher la distance parcourue. Test : $90$ km/h pendant $2{,}5$ h donnent $225$ km.

??? corrige "Corrigé"

    Distance $=$ vitesse $\times$ durée. En Python, la virgule décimale s’écrit avec un point.

    ```python
    vitesse = 90
    duree = 2.5
    print(vitesse * duree)   # 225.0
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 12</span> — Priorités de calcul <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-12 }

<span class="tag">sur papier</span>  Python respecte les priorités opératoires des maths. Sans machine, donner la valeur *et* le type de chaque résultat, puis vérifier.

```python
2 + 3 * 4
(2 + 3) * 4
10 - 6 / 2
2 * 3 ** 2
20 // 3 % 2
```

??? pouce "Coup de pouce"

    Comme en maths : d’abord les parenthèses, puis `**`, puis `*`, `/`, `//`, `%` (de gauche à droite), enfin `+` et `-`. Pensez aussi au type : `/` donne toujours un `float`.

??? corrige "Corrigé"

    *Sur papier.*

    - `2 + 3 * 4` $= 14$ (`int`) : la multiplication passe avant ;

    - `(2 + 3) * 4` $= 20$ (`int`) : les parenthèses d’abord ;

    - `10 - 6 / 2` $= 7.0$ (`float`) : `6 / 2` vaut `3.0` ;

    - `2 * 3 ** 2` $= 18$ (`int`) : la puissance passe avant la multiplication ;

    - `20 // 3 % 2` $= 0$ (`int`) : même priorité, on calcule de gauche à droite, `20 // 3` $= 6$ puis `6 % 2` $= 0$.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 13</span> — La moyenne avec coefficients <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-13 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Un élève a $14$ en maths (coefficient $3$), $11$ en français (coefficient $2$) et $17$ en SNT (coefficient $1$). Ranger notes et coefficients dans des variables, puis calculer et afficher sa moyenne pondérée (attendu : $13{,}5$).

??? pouce "Coup de pouce"

    Moyenne pondérée = (somme des notes multipliées chacune par son coefficient) divisée par (somme des coefficients). Attention aux parenthèses.

??? corrige "Corrigé"

    On additionne les notes multipliées par leur coefficient, puis on divise par la *somme des coefficients* (et non par le nombre de notes).

    ```python
    maths, coef_maths = 14, 3
    francais, coef_francais = 11, 2
    snt, coef_snt = 17, 1
    total = maths * coef_maths + francais * coef_francais + snt * coef_snt
    moyenne = total / (coef_maths + coef_francais + coef_snt)
    print(moyenne)   # 13.5
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 14</span> — Le solde <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-14 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Un article coûte $80$ €. Le magasin fait une remise de $25\,\%$. Écrire un programme qui calcule et affiche le prix après remise.

??? pouce "Coup de pouce"

    Calculez d’abord le montant de la remise, puis retirez-le du prix de départ. Rappel : prendre $25\,\%$ d’un nombre, c’est le multiplier par $25/100$.

??? corrige "Corrigé"

    Une remise de $25\,\%$, c’est payer $75\,\%$ du prix.

    ```python
    prix = 80
    remise = prix * 25 / 100
    print(prix - remise)   # 60.0
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 15</span> — Quel jour serons-nous ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-15 }

<span class="run" title="À programmer et tester sur machine">▶</span>  On numérote les jours de la semaine : lundi $= 0$, mardi $= 1$, …, dimanche $= 6$. Aujourd’hui, c’est mercredi (jour $2$). Écrire un programme qui calcule et affiche :

1.  le nombre de semaines complètes contenues dans $100$ jours ;

2.  le numéro du jour de la semaine qu’il sera dans $100$ jours.

??? pouce "Coup de pouce"

    Les jours reviennent tous les $7$ jours : `//` donne le nombre de semaines complètes, `%` le nombre de jours qui restent. N’oubliez pas qu’on part du jour $2$.

??? corrige "Corrigé"

    `//` compte les semaines complètes ; `%` donne le reste, ce qui « fait le tour » de la semaine.

    ```python
    aujourd_hui = 2                     # mercredi
    print(100 // 7)                     # 14 semaines completes
    print((aujourd_hui + 100) % 7)      # 4, c'est-a-dire vendredi
    ```

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 16</span> — Le rendu de monnaie <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-16 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Écrire un programme qui, à partir d’une somme en euros entiers (variable `montant`), affiche comment la payer avec le **moins de coupures possible** en billets de $10$, pièces de $2$ et pièces de $1$. Par exemple pour $27$ € : $2$ billets de $10$, $3$ pièces de $2$, $1$ pièce de $1$ ($20 + 6 + 1 = 27$).

??? pouce "Coup de pouce"

    Commencez par la plus grosse coupure : `//` donne combien on en utilise, `%` donne ce qui reste à payer avec les coupures plus petites.

??? pouce "Coup de pouce 2 (début de solution)"

    `billets10 = montant // 10`  
    `reste = montant % 10`  
    puis la même chose avec les pièces de $2$, en partant de `reste`.

??? corrige "Corrigé"

    On traite les coupures de la plus grande à la plus petite : `//` donne le nombre, `%` garde le reste à traiter ensuite.

    ```python
    montant = 27
    billets10 = montant // 10     # 2
    reste = montant % 10          # 7
    pieces2 = reste // 2          # 3
    pieces1 = reste % 2           # 1
    print(billets10, "billet(s) de 10")
    print(pieces2, "piece(s) de 2")
    print(pieces1, "piece(s) de 1")
    ```

    *Vérification : $2 \times 10 + 3 \times 2 + 1 \times 1 = 27$.*

### Chaînes de caractères et dialogue

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 17</span> — Nom de code <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-17 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Demander à l’utilisateur son prénom, puis sa ville, et afficher à l’aide d’une f-string : « Agent *prénom*, votre mission vous attend à *ville*. »

??? corrige "Corrigé"

    ```python
    prenom = input("Ton prenom ? ")
    ville = input("Ta ville ? ")
    print(f"Agent {prenom}, votre mission vous attend a {ville}.")
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 18</span> — Le temps d’écran <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-18 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Demander à l’utilisateur combien d’heures par jour il passe devant un écran, puis afficher combien d’heures cela représente sur une année ($365$ jours), et combien de **jours entiers** cela fait. (Attention : `input` renvoie du texte, il faut le convertir avec `int` !)

??? pouce "Coup de pouce"

    Sur une année : multipliez par $365$. Pour les jours entiers, une journée dure $24$ heures : quel opérateur donne le quotient entier ?

??? corrige "Corrigé"

    Sans le `int(...)`, le calcul planterait (on multiplierait du texte). Pour $3$ h par jour : $1095$ h, soit $45$ jours entiers.

    ```python
    par_jour = int(input("Heures d'ecran par jour ? "))
    par_an = par_jour * 365
    print(f"{par_an} heures par an")
    print(f"soit {par_an // 24} jours entiers")
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 19</span> — L’aire au clavier <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-19 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Demander la longueur puis la largeur d’un rectangle (des nombres **à virgule**, à taper avec un point : convertir avec `float`), puis afficher en une seule f-string : « Un rectangle de *L* sur *l* a une aire de *A*. »

??? pouce "Coup de pouce"

    Convertissez chaque `input` avec `float(...)` *avant* de calculer ; dans une f-string, chaque valeur s’écrit entre accolades `{...}`.

??? corrige "Corrigé"

    `float` convertit le texte saisi en nombre à virgule (`int` planterait sur `2.5`).

    ```python
    longueur = float(input("Longueur : "))
    largeur = float(input("Largeur : "))
    print(f"Un rectangle de {longueur} sur {largeur} a une aire de {longueur * largeur}.")
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 20</span> — L’écho <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-20 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Demander un mot puis un nombre entier `n` à l’utilisateur, et afficher le mot répété `n` fois collé (par exemple `"go"` et $3$ donnent `gogogo`).

??? pouce "Coup de pouce"

    Avec les chaînes, `*` répète : `"ha" * 2` donne `"haha"`. Le nombre saisi doit d’abord être converti avec `int`.

??? corrige "Corrigé"

    Avec les chaînes, `*` répète.

    ```python
    mot = input("Un mot : ")
    n = int(input("Combien de fois ? "))
    print(mot * n)
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 21</span> — Le ticket de caisse <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-21 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Demander le nom d’un article, son prix unitaire (nombre à virgule) et la quantité achetée (entier), puis afficher un ticket encadré par des lignes de tirets, par exemple :

??? pouce "Coup de pouce"

    Commencez par les trois `input` (avec les bonnes conversions), calculez le total, puis enchaînez les `print`. Une ligne de tirets peut s’écrire `"-" * 20`.

```text
--------------------
3 x croissant
Prix unitaire : 1.5
TOTAL : 4.5 euros
--------------------
```

??? corrige "Corrigé"

    On convertit chaque saisie dans le bon type, on calcule le total, puis on affiche les tirets « à la main » avant et après.

    ```python
    article = input("Article : ")
    prix = float(input("Prix unitaire : "))
    quantite = int(input("Quantite : "))
    print("--------------------")
    print(f"{quantite} x {article}")
    print(f"Prix unitaire : {prix}")
    print(f"TOTAL : {prix * quantite} euros")
    print("--------------------")
    ```

### Les fonctions

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 22</span> — Le volume du cube <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-22 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Écrire une fonction `volume_cube(c)` qui renvoie le volume d’un cube d’arête `c`. Tester avec `volume_cube(3)` (attendu : $27$).

??? corrige "Corrigé"

    ```python
    def volume_cube(c):
        return c ** 3

    print(volume_cube(3))   # 27
    ```

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 23</span> — L’aire du triangle <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-23 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Écrire une fonction `aire_triangle(base, hauteur)` qui renvoie l’aire d’un triangle (rappel : $\dfrac{\text{base} \times \text{hauteur}}{2}$).

??? corrige "Corrigé"

    ```python
    def aire_triangle(base, hauteur):
        return base * hauteur / 2

    print(aire_triangle(6, 4))   # 12.0
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 24</span> — Une note sur 20 <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-24 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Un contrôle est noté sur un total qui n’est pas toujours $20$. Écrire une fonction `note_sur_20(points, total)` qui renvoie la note ramenée sur $20$. Vérifier que `note_sur_20(12, 15)` vaut $16$.

??? pouce "Coup de pouce"

    Règle de trois : $12$ points sur $15$, combien cela fait-il sur $20$ ? Écrivez le calcul avec les nombres, puis remplacez-les par `points` et `total`.

??? corrige "Corrigé"

    C’est une proportionnalité : $\dfrac{\text{points}}{\text{total}} \times 20$.

    ```python
    def note_sur_20(points, total):
        return points * 20 / total

    print(note_sur_20(12, 15))   # 16.0
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 25</span> — Retrouver le prix HT <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-25 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Sur un ticket, on lit le prix TTC (TVA de $20\,\%$ comprise). Écrire une fonction `prix_ht(prix_ttc)` qui renvoie le prix hors taxes. Vérifier que `prix_ht(60)` vaut $50$. (Attention : retirer $20\,\%$ au prix TTC ne donne *pas* le bon résultat !)

??? pouce "Coup de pouce"

    Ajouter $20\,\%$ de TVA revient à multiplier le prix HT par $1{,}2$. Pour revenir en arrière, quelle opération faut-il faire ?

??? corrige "Corrigé"

    Le prix TTC vaut $1{,}2$ fois le prix HT, donc on **divise** par $1{,}2$. (Retirer $20\,\%$ de $60$ donnerait $48$, et $48 \times 1{,}2 = 57{,}6 \neq 60$.)

    ```python
    def prix_ht(prix_ttc):
        return prix_ttc / 1.2

    print(prix_ht(60))   # 50.0
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 26</span> — Le poids d’une photo <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-26 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Une photo numérique non compressée utilise $3$ octets par pixel (un pour le rouge, un pour le vert, un pour le bleu). Écrire une fonction `poids_photo(largeur, hauteur)` qui renvoie le poids de l’image en octets, puis calculer celui d’une photo de $4000 \times 3000$ pixels. Combien de mégaoctets cela fait-il ($1$ Mo $= 1\,000\,000$ octets) ?

??? pouce "Coup de pouce"

    Nombre de pixels $=$ largeur $\times$ hauteur, et chaque pixel occupe $3$ octets. Pour obtenir des mégaoctets, divisez par $1\,000\,000$.

??? corrige "Corrigé"

    Nombre de pixels $\times 3$ octets.

    ```python
    def poids_photo(largeur, hauteur):
        return largeur * hauteur * 3

    print(poids_photo(4000, 3000))   # 36000000
    ```

    Soit $36$ Mo : c’est pour cela que les appareils *compressent* les photos (JPEG).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 27</span> — Tout en secondes <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-27 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Écrire une fonction `en_secondes(h, m, s)` qui prend une durée en heures, minutes et secondes et renvoie cette durée convertie en secondes. Tester avec `en_secondes(1, 30, 15)` (on doit obtenir $5415$).

??? pouce "Coup de pouce"

    Une heure contient $3600$ secondes et une minute $60$ secondes : convertissez chaque morceau, puis additionnez.

??? corrige "Corrigé"

    Une heure vaut $3600$ s et une minute $60$ s.

    ```python
    def en_secondes(h, m, s):
        return h * 3600 + m * 60 + s

    print(en_secondes(1, 30, 15))   # 5415
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 28</span> — Deviner l’affichage (fonctions) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-28 }

<span class="tag">sur papier</span>  Sans machine, écrire ce qu’affiche ce programme, puis vérifier sur machine.

```python
def f(x):
    return 2 * x + 1

def g(x):
    return x * x

print(f(3))
print(g(f(1)))
print(f(g(2)) + 1)
```

??? pouce "Coup de pouce"

    Calculez de l’intérieur vers l’extérieur : pour `g(f(1))`, calculez d’abord `f(1)`, puis donnez ce résultat à `g`.

??? corrige "Corrigé"

    On calcule de l’intérieur vers l’extérieur.

    - `f(3)` $= 2 \times 3 + 1 = 7$ : affiche `7` ;

    - `f(1)` $= 3$, puis `g(3)` $= 9$ : affiche `9` ;

    - `g(2)` $= 4$, puis `f(4)` $= 9$, et $9 + 1 = 10$ : affiche `10`.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 29</span> — Le coût d’un trajet <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-29 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Une voiture consomme `conso` litres d’essence aux $100$ km.

1.  Écrire une fonction `litres(distance, conso)` qui renvoie le nombre de litres consommés pour parcourir `distance` kilomètres.

2.  Écrire une fonction `cout_trajet(distance, conso, prix_litre)` qui renvoie le coût du trajet en euros **en appelant** `litres`.

3.  Combien coûte un trajet de $800$ km avec une voiture qui consomme $6$ L aux $100$ km, si l’essence coûte $2$ € le litre ?

??? pouce "Coup de pouce"

    Pour $100$ km, la voiture consomme `conso` litres : pour $1$ km, elle consomme donc `conso / 100` litres.

??? pouce "Coup de pouce 2 (début de solution)"

    `def cout_trajet(distance, conso, prix_litre):`  
    `nb_litres = litres(distance, conso)`  
    puis on multiplie par le prix d’un litre.

??? corrige "Corrigé"

    `cout_trajet` réutilise `litres` au lieu de réécrire le calcul.

    ```python
    def litres(distance, conso):
        return distance * conso / 100

    def cout_trajet(distance, conso, prix_litre):
        return litres(distance, conso) * prix_litre

    print(cout_trajet(800, 6, 2))   # 96.0
    ```

    Le trajet consomme $48$ L et coûte $96$ €.

### Les conditions

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 30</span> — Le code secret <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-30 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Écrire une fonction `verifier(code)` qui renvoie `"Acces autorise"` si le code reçu vaut $2468$, et `"Acces refuse"` sinon.

??? corrige "Corrigé"

    Attention : on compare avec `==` (le `=` simple sert à ranger une valeur).

    ```python
    def verifier(code):
        if code == 2468:
            return "Acces autorise"
        else:
            return "Acces refuse"
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 31</span> — Pair ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-31 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Écrire une fonction `est_pair(n)` qui renvoie `True` si `n` est pair et `False` sinon.

??? pouce "Coup de pouce"

    La comparaison `n % 2 == 0` vaut déjà `True` ou `False` : on peut la renvoyer directement.

??? corrige "Corrigé"

    La comparaison `n % 2 == 0` est déjà un booléen : on le renvoie directement.

    ```python
    def est_pair(n):
        return n % 2 == 0
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 32</span> — Le signe <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-32 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Écrire une fonction `signe(x)` qui renvoie `"negatif"`, `"nul"` ou `"positif"` selon le nombre reçu (utiliser `elif`).

??? pouce "Coup de pouce"

    Trois cas, donc : `if` pour le premier, `elif` pour le deuxième, `else` pour le dernier.

??? corrige "Corrigé"

    Trois cas, donc `if` / `elif` / `else`.

    ```python
    def signe(x):
        if x < 0:
            return "negatif"
        elif x == 0:
            return "nul"
        else:
            return "positif"
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 33</span> — Divisible ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-33 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Écrire un programme qui demande deux entiers `a` et `b`, puis affiche « *a* est divisible par *b* » ou « *a* n’est pas divisible par *b* » (avec les vraies valeurs, à l’aide d’une f-string).

??? pouce "Coup de pouce"

    `a` est divisible par `b` lorsque le reste de la division, `a % b`, vaut $0$.

??? corrige "Corrigé"

    `a` est divisible par `b` quand le reste de la division, `a % b`, est nul.

    ```python
    a = int(input("a = "))
    b = int(input("b = "))
    if a % b == 0:
        print(f"{a} est divisible par {b}")
    else:
        print(f"{a} n'est pas divisible par {b}")
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 34</span> — Valeur absolue maison <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-34 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Écrire une fonction `valeur_absolue(x)` qui renvoie la valeur absolue de `x` **sans** utiliser la fonction `abs` de Python (se servir d’un `if`).

??? pouce "Coup de pouce"

    Quels sont les deux cas possibles selon le signe de `x` ? Que vaut la valeur absolue dans chacun d’eux ?

??? corrige "Corrigé"

    Si le nombre est négatif, on renvoie son opposé.

    ```python
    def valeur_absolue(x):
        if x < 0:
            return -x
        else:
            return x
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 35</span> — L’icône de batterie <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-35 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Un téléphone affiche une icône selon le niveau de batterie (en %). Écrire une fonction `icone(niveau)` qui renvoie `"critique"` si le niveau est inférieur à $10$, `"faible"` s’il est inférieur à $30$, `"moyenne"` s’il est inférieur à $70$, et `"pleine"` sinon. Tester avec $5$, $50$ et $100$.

??? pouce "Coup de pouce"

    Testez les seuils dans l’ordre croissant avec `if` / `elif` : dès qu’une condition est vraie, les suivantes ne sont plus regardées.

??? corrige "Corrigé"

    On teste les seuils du plus bas au plus haut : le premier qui est vrai l’emporte.

    ```python
    def icone(niveau):
        if niveau < 10:
            return "critique"
        elif niveau < 30:
            return "faible"
        elif niveau < 70:
            return "moyenne"
        else:
            return "pleine"

    print(icone(5), icone(50), icone(100))   # critique moyenne pleine
    ```

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 36</span> — Le maximum de trois <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-36 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Écrire une fonction `max3(a, b, c)` qui renvoie le plus grand des trois nombres.

??? pouce "Coup de pouce"

    Gardez le plus grand nombre « vu jusqu’ici » dans une variable `grand`, puis comparez-la aux autres nombres un par un.

??? pouce "Coup de pouce 2 (début de solution)"

    `grand = a`  
    `if b > grand:`  
    `grand = b`  
    puis la même chose avec `c`, et enfin `return grand`.

??? corrige "Corrigé"

    On garde le plus grand vu jusqu’ici dans une variable `m`.

    ```python
    def max3(a, b, c):
        m = a
        if b > m:
            m = b
        if c > m:
            m = c
        return m
    ```

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 37</span> — Année bissextile <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-37 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Écrire une fonction `bissextile(annee)` qui renvoie `True` si l’année est bissextile. Règle : une année est bissextile si elle est divisible par $4$, *sauf* les années de siècle (divisibles par $100$) qui doivent en plus être divisibles par $400$. Tester avec $2024$ (oui), $1900$ (non) et $2000$ (oui).

??? pouce "Coup de pouce"

    « Divisible par $4$ » s’écrit `annee % 4 == 0`. Traitez les cas du plus particulier au plus général : d’abord $400$, puis $100$, puis $4$.

??? pouce "Coup de pouce 2 (début de solution)"

    `if annee % 400 == 0:`  
    `return True`  
    `elif annee % 100 == 0:`  
    `return False`

??? corrige "Corrigé"

    On traduit la règle : divisible par $4$ **et** pas par $100$, **ou** divisible par $400$.

    ```python
    def bissextile(annee):
        return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

    print(bissextile(2024))   # True
    print(bissextile(1900))   # False
    print(bissextile(2000))   # True
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 38</span> — Un triangle est-il possible ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-38 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Écrire une fonction `triangle(a, b, c)` qui renvoie `True` si trois longueurs peuvent former un triangle. Règle : chaque côté doit être plus petit que la somme des deux autres.

??? pouce "Coup de pouce"

    Il y a trois inégalités à vérifier (une par côté) ; elles doivent être vraies *toutes les trois* : pensez à `and`.

??? corrige "Corrigé"

    Chaque côté doit être plus petit que la somme des deux autres (les trois conditions reliées par `and`).

    ```python
    def triangle(a, b, c):
        return a < b + c and b < a + c and c < a + b
    ```

### Les boucles

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 39</span> — De 1 à 10 <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-39 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Écrire un programme qui affiche tous les entiers de $1$ à $10$ (boucle `for`).

??? corrige "Corrigé"

    `range(1, 11)` va de $1$ inclus à $11$ exclu.

    ```python
    for i in range(1, 11):
        print(i)
    ```

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 40</span> — Trace de boucle <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-40 }

<span class="tag">sur papier</span>  Sans machine, écrire ce qu’affiche ce programme, puis vérifier.

```python
for i in range(4):
    print(i * i)
```

??? corrige "Corrigé"

    *Sur papier.* `i` prend les valeurs $0, 1, 2, 3$ ; on affiche $i \times i$ :

    ```text
    0
    1
    4
    9
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 41</span> — La pyramide de boulets <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-41 }

<span class="run" title="À programmer et tester sur machine">▶</span>  On empile des boulets en pyramide à base carrée : $1$ au sommet, $4$ ($2 \times 2$) à l’étage du dessous, puis $9$, $16$… Écrire une fonction `pyramide(n)` qui renvoie le nombre total de boulets d’une pyramide de `n` étages. Vérifier que `pyramide(10)` vaut $385$.

??? pouce "Coup de pouce"

    À l’étage numéro `i`, il y a `i * i` boulets. Additionnez-les dans une variable `total` qui commence à $0$, en parcourant `range(1, n + 1)`.

??? corrige "Corrigé"

    On accumule dans `total` le carré de chaque numéro d’étage.

    ```python
    def pyramide(n):
        total = 0
        for etage in range(1, n + 1):
            total = total + etage * etage
        return total

    print(pyramide(10))   # 385
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 42</span> — Les puissances de 2 <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-42 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Écrire une fonction `puissances_de_2(n)` qui affiche $2^0, 2^1, 2^2, \ldots, 2^n$, une valeur par ligne. Que vaut $2^{10}$ ? (Ce nombre est partout en informatique !)

??? pouce "Coup de pouce"

    La boucle `for i in range(n + 1)` parcourt $0, 1, \ldots, n$ ; à chaque tour, on affiche `2 ** i`.

??? corrige "Corrigé"

    `range(n + 1)` va de $0$ à $n$ inclus. On trouve $2^{10} = 1024$.

    ```python
    def puissances_de_2(n):
        for i in range(n + 1):
            print(2 ** i)

    puissances_de_2(10)   # 1, 2, 4, ..., 1024
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 43</span> — Les écouteurs <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-43 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Léa part de $0$ € et économise $15$ € par semaine. Avec une boucle `while`, calculer et afficher au bout de combien de semaines elle aura **au moins** $200$ € pour s’offrir des écouteurs.

??? pouce "Coup de pouce"

    Deux variables : `economies` et `semaines`. Tant que les économies sont *inférieures* à $200$, on ajoute $15$ et on compte une semaine de plus.

??? corrige "Corrigé"

    On ne sait pas à l’avance combien de semaines il faudra : c’est un `while`.

    ```python
    economies = 0
    semaines = 0
    while economies < 200:
        economies = economies + 15
        semaines = semaines + 1
    print(semaines)   # 14 (210 euros)
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 44</span> — Les multiples de 7 <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-44 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Écrire un programme qui **compte** (sans les afficher) combien il y a de multiples de $7$ entre $1$ et $1000$, puis affiche ce nombre.

??? pouce "Coup de pouce"

    Un compteur commence à $0$ ; on parcourt les nombres de $1$ à $1000$ et on ajoute $1$ au compteur lorsque le nombre est multiple de $7$ (avec `%`).

??? corrige "Corrigé"

    Un compteur qu’on augmente à chaque multiple rencontré (le test `%` dans la boucle).

    ```python
    compteur = 0
    for n in range(1, 1001):
        if n % 7 == 0:
            compteur = compteur + 1
    print(compteur)   # 142
    ```

    Autre méthode : `len(range(7, 1001, 7))`, ou tout simplement `1000 // 7`.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 45</span> — Le livret d’épargne <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-45 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Un capital placé à $3\,\%$ par an est multiplié par $1{,}03$ chaque année. Écrire une fonction `capital(depart, n)` qui renvoie le capital au bout de `n` années, à l’aide d’une boucle `for` (sans utiliser `**`). Vérifier que `capital(1000, 10)` vaut environ $1343{,}92$.

??? pouce "Coup de pouce"

    Une variable `c` part de `depart` ; chaque année (un tour de boucle), elle est multipliée par $1{,}03$.

??? pouce "Coup de pouce 2 (début de solution)"

    `def capital(depart, n):`  
    `c = depart`  
    `for annee in range(n):`

??? corrige "Corrigé"

    On multiplie le capital par $1{,}03$ autant de fois qu’il y a d’années.

    ```python
    def capital(depart, n):
        c = depart
        for annee in range(n):
            c = c * 1.03
        return c

    print(capital(1000, 10))   # 1343.916...
    ```

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 46</span> — Combien de chiffres ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-46 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Écrire une fonction `nb_chiffres(n)` qui renvoie le nombre de chiffres d’un entier positif. Par exemple `nb_chiffres(2048)` vaut $4$.

??? pouce "Coup de pouce"

    Diviser par $10$ avec `//` enlève le dernier chiffre (`2048 // 10` vaut `204`). Comptez combien de fois on peut le faire, dans une boucle `while`, avant d’arriver à $0$.

??? pouce "Coup de pouce 2 (début de solution)"

    `compteur = 0`  
    `while n > 0:`  
    `n = n // 10`  
    (il reste à augmenter le compteur et à le renvoyer.)

??? corrige "Corrigé"

    Chaque division entière par $10$ retire le dernier chiffre ; on compte les étapes.

    ```python
    def nb_chiffres(n):
        compteur = 0
        while n > 0:
            n = n // 10
            compteur = compteur + 1
        return compteur

    print(nb_chiffres(2048))   # 4
    ```

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 47</span> — Nombre premier <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-47 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Écrire une fonction `est_premier(n)` qui renvoie `True` si `n` est un nombre premier (divisible seulement par $1$ et par lui-même), et `False` sinon.

??? pouce "Coup de pouce"

    `n` est premier s’il vaut au moins $2$ et si *aucun* nombre `d` compris entre $2$ et `n - 1` ne le divise. Dès qu’on trouve un diviseur, on peut répondre.

??? pouce "Coup de pouce 2 (début de solution)"

    `if n < 2:`  
    `return False`  
    `for d in range(2, n):`  
    `if n % d == 0:`

??? corrige "Corrigé"

    On cherche un diviseur entre $2$ et $n - 1$ ; s’il en existe un, `n` n’est pas premier.

    ```python
    def est_premier(n):
        if n < 2:
            return False
        for d in range(2, n):
            if n % d == 0:
                return False
        return True
    ```

### Petits défis de synthèse

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 48</span> — Fizz <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-48 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Afficher les entiers de $1$ à $30$, mais remplacer par le mot « Fizz » ceux qui sont des multiples de $3$.

??? pouce "Coup de pouce"

    Une boucle `for` de $1$ à $30$ ; à chaque tour, un `if` teste si le nombre est multiple de $3$ (avec `%`) ; sinon (`else`), on affiche le nombre.

??? corrige "Corrigé"

    ```python
    for i in range(1, 31):
        if i % 3 == 0:
            print("Fizz")
        else:
            print(i)
    ```

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 49</span> — L’ordinateur devine <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-49 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Cette fois, c’est **l’utilisateur** qui pense à un nombre entre $1$ et $100$, et l’ordinateur qui cherche. Il propose toujours le milieu de l’intervalle encore possible (variables `bas` et `haut`) ; l’utilisateur répond `+` (c’est plus grand), `-` (c’est plus petit) ou `=` (trouvé), et il resserre l’intervalle. Afficher à la fin le nombre d’essais. Combien lui en faut-il au maximum ?

??? pouce "Coup de pouce"

    Le nombre proposé est `(bas + haut) // 2`. Si l’utilisateur répond `+`, le nombre cherché est au-dessus de la proposition : que devient alors `bas` ?

??? pouce "Coup de pouce 2 (début de solution)"

    `bas = 1`  
    `haut = 100`  
    `essais = 0`  
    `reponse = ""`  
    `while reponse != "=":`

??? corrige "Corrigé"

    À chaque réponse, l’intervalle est coupé en deux : c’est la *recherche par dichotomie*.

    ```python
    bas = 1
    haut = 100
    essais = 0
    reponse = ""
    while reponse != "=":
        proposition = (bas + haut) // 2
        essais = essais + 1
        reponse = input(f"Je propose {proposition} (+, - ou =) : ")
        if reponse == "+":
            bas = proposition + 1
        elif reponse == "-":
            haut = proposition - 1
    print(f"Trouve en {essais} essais !")
    ```

    Au maximum $7$ essais : chaque essai divise l’intervalle par deux, et $2^7 = 128 \geq 100$.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 50</span> — Moyenne d’une série de notes <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-50 }

<span class="run" title="À programmer et tester sur machine">▶</span>  L’utilisateur saisit des notes une par une ; il tape $-1$ pour terminer. Afficher alors la moyenne des notes saisies.

??? pouce "Coup de pouce"

    Boucle `while` : on ne sait pas combien de notes il y aura. Gardez la `somme` et le `nombre` de notes ; la valeur $-1$ ne doit pas être comptée.

??? pouce "Coup de pouce 2 (début de solution)"

    `somme = 0`  
    `nombre = 0`  
    `note = float(input("Note : "))`  
    `while note != -1:`

??? corrige "Corrigé"

    On lit une première note, puis on continue **tant que** ce n’est pas $-1$.

    ```python
    somme = 0
    nombre = 0
    note = int(input("Note (-1 pour finir) : "))
    while note != -1:
        somme = somme + note
        nombre = nombre + 1
        note = int(input("Note (-1 pour finir) : "))
    if nombre > 0:
        print("Moyenne :", somme / nombre)
    else:
        print("Aucune note saisie.")
    ```

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 51</span> — Le PGCD <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-51 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Écrire une fonction `pgcd(a, b)` qui renvoie le plus grand diviseur commun de deux entiers, par la méthode des soustractions successives : tant que les deux nombres sont différents, on remplace le plus grand par sa différence avec le plus petit. Tester avec `pgcd(24, 36)` (attendu : $12$).

??? pouce "Coup de pouce"

    Boucle `while a != b` ; à chaque tour, un `if` décide lequel des deux nombres est le plus grand.

??? pouce "Coup de pouce 2 (début de solution)"

    `while a != b:`  
    `if a > b:`  
    `a = a - b`

??? corrige "Corrigé"

    Tant que les deux nombres diffèrent, on remplace le plus grand par sa différence avec le plus petit.

    ```python
    def pgcd(a, b):
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        return a

    print(pgcd(24, 36))   # 12
    ```

### Critiquer une réponse d’IA

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 52</span> — Une puissance calculée par un assistant <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> { #ex-01-52 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Un élève a demandé à un assistant d’IA : « Écris une fonction `puissance(x, n)` qui renvoie `x` multiplié `n` fois par lui-même, avec une boucle `for` et sans utiliser l’opérateur `**`. » Voici la réponse obtenue :

```python
def puissance(x, n):
    resultat = 1
    for i in range(n + 1):
        resultat = resultat * x
    return resultat

print(puissance(2, 3))   # affiche 8
```

1.  La réponse est-elle correcte ? Recopier la fonction, l’exécuter et comparer ce qui s’affiche avec le commentaire de l’assistant. Tester aussi `puissance(5, 2)` et `puissance(3, 0)`.

2.  Localiser l’erreur et corriger la fonction (une seule ligne à modifier).

    ??? pouce "Coup de pouce"

        Comptez combien de tours fait `range(n + 1)` quand `n` vaut $3$. Combien de fois faut-il multiplier par `x` ?

3.  Quelle vérification simple, faite *avant* de faire confiance à cette réponse, aurait suffi à détecter l’erreur ?

??? corrige "Corrigé"

    **1.** Non. L’exécution affiche `16` et non `8` comme l’annonce le commentaire ; de même `puissance(5, 2)` donne `125` au lieu de `25`, et `puissance(3, 0)` donne `3` au lieu de `1`.  
    **2.** L’erreur est dans `range(n + 1)` : cette suite contient $n + 1$ nombres ($0, 1, \ldots, n$), donc la boucle multiplie **une fois de trop**. Il faut écrire `range(n)` (rappel du cours : `range(5)` fabrique cinq nombres, de $0$ à $4$).

    ```python
    def puissance(x, n):
        resultat = 1
        for i in range(n):
            resultat = resultat * x
        return resultat

    print(puissance(2, 3))   # affiche bien 8
    ```

    **3.** Exécuter la fonction sur **un petit exemple dont on connaît le résultat** ($2 \times 2 \times 2 = 8$) : le commentaire `# affiche 8` n’est qu’une affirmation de l’assistant ; seule la console fait foi.
