# Exercices

<p class="sous-titre">Complément : dessiner avec la tortue</p>

!!! consignes "Mode d’emploi"

    - Niveau : ★ échauffement, ★★ classique (niveau bac), ★★★ défi ; les *coups de pouce* et les *corrigés* se déplient sous chaque exercice.

    - <span class="run" title="À programmer et tester sur machine">▶</span> *À programmer et exécuter* sur machine. Commencez toujours par `import turtle as t` et terminez par `t.done()`.

    - **Partie 1** : des ordres en séquence, puis la boucle `for`. **Partie 2** : avec des fonctions.

    - **Réflexes** : une figure qui se répète $\rightarrow$ une boucle `for` ; un motif à réutiliser $\rightarrow$ une **fonction** (partie 2) ; un polygone à `n` côtés $\rightarrow$ on tourne de `360 / n`.

    - Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la [charte d’usage de l’IA](../charte.md).

### Partie 1 — Séquence d’instructions et boucle `for`

### Premiers tracés

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — Le carré <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-T-1 }

<span class="essentiel">• essentiel</span>

<span class="run" title="À programmer et tester sur machine">▶</span> Dessiner un carré de côté `100` (4 côtés, on tourne de `90` à chaque fois) : d’abord en écrivant les ordres **à la suite**, l’un sous l’autre (combien en faut-il ?), puis à l’aide d’une boucle `for`.0

??? pouce "Coup de pouce"

    Écrire d’abord les ordres pour *un seul* côté. Quel groupe d’ordres se répète, et combien de fois ? C’est lui qui va dans la boucle, décalé de 4 espaces.

![](../figures/f17d0487e5524a97.svg){ .tikz loading=lazy }

??? corrige "Corrigé"

    !!! remarque "Remarque"

        Plusieurs écritures sont possibles ; on en donne une simple. Chaque programme suppose `import turtle as t` au début et `t.done()` à la fin. On rappelle la règle d’or : un polygone régulier à `n` côtés se ferme en tournant de `360 / n` à chaque sommet.

    **En séquence** : 8 ordres (4 fois « avancer, tourner »).

    ```python
    import turtle as t
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.done()
    ```

    **Avec une boucle** : on répète 4 fois le couple « avancer, tourner ».

    ```python
    import turtle as t
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.done()
    ```

    <span class="erreurfreq">▷ Erreur fréquente.</span> ne pas décaler `t.left(90)` : il sort de la boucle, la tortue avance quatre fois tout droit (un seul trait de 400) et ne tourne qu’à la fin.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 2</span> — Le rectangle <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-T-2 }

<span class="run" title="À programmer et tester sur machine">▶</span> Dessiner un rectangle de `200` de large sur `100` de haut. *(Attention : les quatre côtés ne sont pas tous égaux, mais on tourne toujours de `90`.)*0

??? pouce "Coup de pouce"

    Les côtés vont par paires : un grand côté puis un petit. Quel groupe d’ordres se répète, et combien de fois ?

??? corrige "Corrigé"

    Deux longueurs et deux largeurs : on répète **deux fois** le couple « long côté / court côté ».

    ```python
    import turtle as t
    for i in range(2):
        t.forward(200)   # longueur
        t.left(90)
        t.forward(100)   # largeur
        t.left(90)
    t.done()
    ```

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 3</span> — L’escalier <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-T-3 }

<span class="essentiel">• essentiel</span>

<span class="run" title="À programmer et tester sur machine">▶</span> Dessiner un escalier de **5 marches** : une marche est un déplacement horizontal suivi d’un déplacement vertical. Utiliser une boucle qui répète 5 fois « avancer, tourner, avancer, tourner ».0

??? pouce "Coup de pouce"

    Après avoir monté une contremarche, la tortue regarde vers le haut : de quel côté doit-elle tourner pour repartir à l’horizontale ? Dessiner une marche sur papier en suivant la tortue.

![](../figures/7c64254262e820da.svg){ .tikz loading=lazy }

??? corrige "Corrigé"

    Chaque marche = un pas horizontal, un pas vertical. Après être monté, on se **remet** à l’horizontale (`right(90)`).

    ```python
    import turtle as t
    for i in range(5):
        t.forward(40)   # horizontal
        t.left(90)
        t.forward(40)   # vertical
        t.right(90)     # on repart a l'horizontale
    t.done()
    ```

    <span class="erreurfreq">▷ Erreur fréquente.</span> tourner deux fois à gauche : la tortue revient vers son point de départ et repasse cinq fois sur le même petit carré.

### Les polygones réguliers

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 4</span> — Triangle et hexagone <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-T-4 }

<span class="run" title="À programmer et tester sur machine">▶</span> Dessiner un **triangle équilatéral** (3 côtés), puis un **hexagone** (6 côtés). Dans chaque cas, de combien de degrés faut-il tourner à chaque sommet ?0

??? pouce "Coup de pouce"

    Pour le carré, la tortue tourne 4 fois de `90` : `360` degrés en tout pour revenir à son orientation de départ. Le même total vaut-il pour le triangle ? Attention : l’angle dont tourne la tortue n’est pas l’angle intérieur du triangle.

![](../figures/ca68971127b1d880.svg){ .tikz loading=lazy }

??? corrige "Corrigé"

    Pour refermer la figure, la tortue tourne de $360$ degrés en tout, partagés entre les sommets. Triangle : $360 / 3 = \mathbf{120}$ degrés. Hexagone : $360 / 6 = \mathbf{60}$ degrés.

    ```python
    import turtle as t
    for i in range(3):      # triangle equilateral
        t.forward(120)
        t.left(120)
    for i in range(6):      # hexagone
        t.forward(80)
        t.left(60)
    t.done()
    ```

    <span class="erreurfreq">▷ Erreur fréquente.</span> tourner de `60` pour le triangle : c’est l’angle *intérieur* ; la tortue, elle, tourne de l’angle extérieur, `120`. Avec `60`, on obtient la moitié d’un hexagone.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 5</span> — L’étoile à cinq branches <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-T-5 }

<span class="run" title="À programmer et tester sur machine">▶</span> Dessiner une étoile à 5 branches.0

??? pouce "Coup de pouce"

    Suivre du doigt le tracé de l’étoile : la tortue fait **deux** tours complets sur elle-même avant de revenir à son orientation de départ. Combien de degrés en tout, répartis sur combien de sommets ?

![](../figures/4e2bc1475cf04f4e.svg){ .tikz loading=lazy }

??? corrige "Corrigé"

    En traçant l’étoile, la tortue fait **deux** tours complets, soit $720$ degrés, répartis sur 5 pointes : $720 / 5 = \mathbf{144}$ degrés. En tournant ainsi, on « saute » un sommet sur deux, ce qui trace l’étoile.

    ```python
    import turtle as t
    for i in range(5):
        t.forward(200)
        t.left(144)
    t.done()
    ```

### Répéter en tournant

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Rosace de cercles <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-T-6 }

<span class="run" title="À programmer et tester sur machine">▶</span> La tortue sait tracer un cercle avec `t.circle(rayon)`. Dessiner une jolie « fleur » en répétant **18 cercles** de rayon `80`, en tournant un peu entre chaque. De combien faut-il tourner à chaque fois ?0

??? pouce "Coup de pouce"

    Même raisonnement que pour les polygones : après les 18 cercles, la tortue doit avoir fait exactement un tour complet sur elle-même.

![](../figures/1966ebc937319f6d.svg){ .tikz loading=lazy }

??? corrige "Corrigé"

    18 cercles répartis sur un tour complet : on tourne de $360 / 18 = \mathbf{20}$ degrés entre chaque.

    ```python
    import turtle as t
    for k in range(18):
        t.circle(80)
        t.left(20)
    t.done()
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — La spirale carrée <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-T-7 }

<span class="run" title="À programmer et tester sur machine">▶</span> Dessiner une spirale : on tourne toujours de `90` degrés, mais la longueur du côté **augmente** à chaque tour (par exemple `10, 20, 30, …`). Faire une vingtaine de segments.0

??? pouce "Coup de pouce"

    La longueur doit changer à chaque tour : utiliser la variable de boucle `i` dans le calcul de la longueur (que vaut `10 * i` pour `i` allant de `1` à `20` ?).

![](../figures/2312be89348863bb.svg){ .tikz loading=lazy }

??? corrige "Corrigé"

    On garde l’angle à `90` degrés, mais on **augmente** la longueur du côté à chaque tour.

    ```python
    import turtle as t
    cote = 10
    for i in range(20):
        t.forward(cote)
        t.left(90)
        cote = cote + 10    # le cote grandit
    t.done()
    ```

    <span class="erreurfreq">▷ Erreur fréquente.</span> écrire `cote = 10` *dans* la boucle : la longueur est remise à `10` à chaque tour, et la tortue repasse sur un petit carré.

    *Autre méthode :* au tour numéro `i`, le côté mesure `10 * i` ; on peut donc faire varier `i` de `1` à `20` sans variable `cote` : `for i in range(1, 21):` puis `t.forward(10 * i)` et `t.left(90)`.

### Défis

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 8</span> — La maison <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-T-8 }

<span class="duree">≈ 15 min</span>

<span class="run" title="À programmer et tester sur machine">▶</span> Dessiner une maison : un **carré** pour la façade, surmonté d’un **triangle** pour le toit. *(Il faudra bien positionner la tortue et gérer les angles du toit.)*0

??? pouce "Coup de pouce"

    Tracer d’abord le carré, puis se demander où se trouve la tortue et dans quelle direction elle regarde. Le toit est un triangle équilatéral posé sur le côté du haut : de combien tourner à chaque sommet ?

0

??? pouce "Coup de pouce 2 (début de solution)"

    `for i in range(4):` …(la façade)  
    `t.left(90)`  
    `t.forward(100)` \# la tortue est en haut à gauche  
    `t.right(30)` …

![](../figures/d5cbfcf069e1fbc0.svg){ .tikz loading=lazy }

??? corrige "Corrigé"

    On trace d’abord la façade (un carré). La tortue revient alors en bas à gauche ; on monte au coin haut-gauche, puis on pose un toit triangulaire (triangle équilatéral, angles de `120` degrés).

    ```python
    import turtle as t
    # La facade (carre de cote 100)
    for i in range(4):
        t.forward(100)
        t.left(90)
    # On monte au coin haut-gauche pour poser le toit
    t.left(90)
    t.forward(100)
    t.right(30)          # on vise le sommet du toit
    # Le toit (triangle equilateral)
    for i in range(3):
        t.forward(100)
        t.right(120)
    t.done()
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 9</span> — Un triangle selon un assistant d’IA <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> { #ex-T-9 }

Un élève demande à un assistant d’IA : « Écris un programme Python avec la tortue qui dessine un triangle équilatéral de côté 100. » Voici la réponse obtenue.

```python
import turtle as t
for i in range(3):
    t.forward(100)
    t.left(60)
t.done()
```

« La boucle répète trois fois : avancer de 100, puis tourner à gauche de 60 degrés, puisque les angles d’un triangle équilatéral mesurent 60 degrés. Après les trois tours, la tortue est revenue à son point de départ et le triangle est fermé. »

1.  La réponse est-elle correcte ? Calculer de combien de degrés la tortue a tourné en tout à la fin du programme, puis <span class="run" title="À programmer et tester sur machine">▶</span> exécuter le programme.

2.  Localiser et corriger l’erreur.

3.  Quelle vérification simple, faite avant de faire confiance à la réponse, aurait suffi à détecter l’erreur ?0

    ??? pouce "Coup de pouce"

        Pour refermer une figure, de combien de degrés la tortue doit-elle avoir tourné en tout ? Comparer avec `3 * 60`.

??? corrige "Corrigé"

    **1.** Non. En trois tours, la tortue tourne de $3 \times 60 = 180^\circ$ seulement, alors que, pour fermer un polygone, elle doit avoir tourné de $360^\circ$ en tout. À l’exécution, on obtient trois côtés d’un hexagone (une figure ouverte) : la tortue finit à environ $(100\,;\,173)$ du point de départ, cap à $180^\circ$, et rien n’est fermé. **2.** L’erreur est l’angle `left(60)`. L’angle *intérieur* du triangle vaut bien $60^\circ$, mais la tortue tourne de l’angle **extérieur**, $360 / 3 = 120^\circ$ (règle du cours : `360 / n` à chaque sommet).

    ```python
    import turtle as t
    for i in range(3):
        t.forward(100)
        t.left(120)
    t.done()
    ```

    **3.** Faire le calcul « nombre de côtés $\times$ angle $= 360$ » avant de lancer : $3 \times 60 \neq 360$. Ou, plus simplement, exécuter le programme et regarder le dessin : ici, l’erreur se voit à l’écran en une seconde.

### Partie 2 — Avec des fonctions

### Factoriser : les fonctions

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 10</span> — Un polygone au choix <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-T-10 }

<span class="essentiel">• essentiel</span>

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire une fonction `polygone(n, cote)` qui dessine un polygone régulier à `n` côtés de longueur `cote`. L’utiliser pour dessiner un triangle, un carré et un octogone.0

??? pouce "Coup de pouce"

    Reprendre le carré et le triangle : qu’est-ce qui change d’une figure à l’autre ? Ce sont ces deux nombres qui deviennent les paramètres `n` et `cote`.

??? corrige "Corrigé"

    On remplace l’angle par `360 / n` : la même fonction dessine tous les polygones réguliers.

    ```python
    import turtle as t
    def polygone(n, cote):
        for i in range(n):
            t.forward(cote)
            t.left(360 / n)

    polygone(3, 100)   # triangle
    polygone(4, 100)   # carre
    polygone(8, 60)    # octogone
    t.done()
    ```

    <span class="erreurfreq">▷ Erreur fréquente.</span> laisser `t.left(90)`, recopié du carré : seul l’appel `polygone(4, ...)` se referme. L’angle doit dépendre du paramètre : `360 / n`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 11</span> — Rosace de carrés <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-T-11 }

<span class="run" title="À programmer et tester sur machine">▶</span> En réutilisant une fonction `carre(cote)`, dessiner une rosace formée de **12 carrés**, chacun pivoté de `30` degrés par rapport au précédent. *(Pourquoi 30 ? Parce que $12 \times 30 = 360$.)*0

??? pouce "Coup de pouce"

    Écrire d’abord `carre(cote)` et vérifier qu’elle ramène la tortue à son point et à son orientation de départ. La rosace n’est alors qu’une boucle : un carré, puis on tourne.

![](../figures/a17662bb0118a30a.svg){ .tikz loading=lazy }

??? corrige "Corrigé"

    On écrit une fonction `carre`, puis on la répète 12 fois en pivotant de `30` degrés ($12 \times 30 = 360$).

    ```python
    import turtle as t
    def carre(cote):
        for i in range(4):
            t.forward(cote)
            t.left(90)

    for k in range(12):
        carre(100)
        t.left(30)
    t.done()
    ```

### Couleurs et déplacements

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 12</span> — Trois carrés colorés <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-T-12 }

<span class="essentiel">• essentiel</span>

<span class="run" title="À programmer et tester sur machine">▶</span> Dessiner **trois carrés** côte à côte, remplis de trois couleurs différentes (par exemple rouge, vert, bleu), en écrivant une fonction `carre_plein(cote, couleur)` que l’on appelle trois fois.0

??? pouce "Coup de pouce"

    Relire le tableau des commandes du cours : comment passer d’un carré au suivant **sans tracer de trait** ? Comment **remplir** une figure (voir l’exemple coloré du cours) ?

??? corrige "Corrigé"

    On fabrique une fonction « carré plein » (couleur $+$ `begin_fill`/`end_fill`), et on déplace la tortue *sans tracer* entre deux carrés grâce à `penup`/`goto`/`pendown`.

    ```python
    import turtle as t
    def carre_plein(cote, couleur):
        t.color(couleur)
        t.begin_fill()
        for i in range(4):
            t.forward(cote)
            t.left(90)
        t.end_fill()

    t.penup()
    t.goto(-150, 0)
    t.pendown()
    carre_plein(80, "red")
    t.penup()
    t.goto(-50, 0)
    t.pendown()
    carre_plein(80, "green")
    t.penup()
    t.goto(50, 0)
    t.pendown()
    carre_plein(80, "blue")
    t.done()
    ```

    <span class="erreurfreq">▷ Erreur fréquente.</span> oublier `t.penup()` avant `t.goto(...)` : la tortue trace un trait entre deux carrés.

### Défis

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 13</span> — Le damier <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-T-13 }

<span class="duree">≈ 30 min</span>

<span class="run" title="À programmer et tester sur machine">▶</span> À l’aide de **deux boucles imbriquées**, dessiner une grille de **$3 \times 3$ carrés** (9 cases). Pour un vrai défi, remplir une case sur deux en noir, comme un damier.0

??? pouce "Coup de pouce"

    Une boucle pour les lignes, une boucle pour les colonnes : la case de la ligne `ligne` et de la colonne `colonne` commence au point `(colonne * cote, ligne * cote)`. Pour le damier : à quelle condition sur `ligne + colonne` une case est-elle noire ?

0

??? pouce "Coup de pouce 2 (début de solution)"

    `for ligne in range(3):`  
    `for colonne in range(3):`  
    `t.penup()`  
    `t.goto(colonne * cote, ligne * cote)`  
    …

![](../figures/56aae1e62d947b13.svg){ .tikz loading=lazy }

??? corrige "Corrigé"

    Deux boucles imbriquées balayent lignes et colonnes, et on se place sur chaque case avec `goto`. Chaque case est un carré ; on ne **remplit** qu’une case sur deux, selon la parité de `ligne + colonne`.

    ```python
    import turtle as t
    def carre(cote):
        for i in range(4):
            t.forward(cote)
            t.left(90)

    cote = 40
    t.color("black")
    for ligne in range(3):
        for colonne in range(3):
            t.penup()
            t.goto(colonne * cote, ligne * cote)
            t.pendown()
            if (ligne + colonne) % 2 == 0:   # case noire : carre rempli
                t.begin_fill()
                carre(cote)
                t.end_fill()
            else:                            # case blanche : contour seul
                carre(cote)
    t.done()
    ```

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 14</span> — La cible <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-T-14 }

<span class="duree">≈ 20 min</span>

<span class="run" title="À programmer et tester sur machine">▶</span> On veut dessiner une cible de tir à l’arc : **cinq disques** de même centre `(0, 0)`, de rayons `100`, `80`, `60`, `40` et `20`, remplis alternativement en rouge et en blanc. *(On précise que* `t.circle(r)` *trace un cercle de rayon* `r` *dont le centre se trouve à* `r` *pas sur la **gauche** de la tortue.)*

1.  La tortue est tournée vers la droite, comme au départ. En quel point doit-elle se trouver pour que `t.circle(100)` trace un cercle de centre `(0, 0)` ? Et pour `t.circle(r)` ?

2.  Écrire une fonction `disque(r, couleur)` qui trace un disque de rayon `r`, de centre `(0, 0)`, rempli de la couleur `couleur`.

3.  À l’aide d’une boucle `for` et de `disque`, dessiner la cible. Pourquoi faut-il commencer par le **plus grand** disque ?0

    ??? pouce "Coup de pouce"

        Le rayon du disque numéro `i` (pour `i` allant de `0` à `4`) vaut `100 - 20 * i`. La couleur dépend de la parité de `i`, comme les cases du damier.

![](../figures/09bac102de73d012.svg){ .tikz loading=lazy }

??? corrige "Corrigé"

    **1.** Tournée vers la droite, la tortue a sa gauche vers le haut : le centre du cercle est `r` pas **au-dessus** d’elle. Pour un centre en `(0, 0)`, elle doit partir de `(0, -100)` pour `t.circle(100)`, et de `(0, -r)` pour `t.circle(r)`.

    **2. et 3.** Un cercle complet ramène la tortue à son point et à son orientation de départ : elle reste tournée vers la droite pour le disque suivant. On trace du plus grand au plus petit, car chaque disque rempli **recouvre** ce qui était dessiné dessous : en commençant par le plus petit, le disque de rayon `100`, tracé en dernier, cacherait tous les autres.

    ```python
    import turtle as t
    def disque(r, couleur):
        """Trace un disque de rayon r, de centre (0, 0), rempli de couleur."""
        t.penup()
        t.goto(0, -r)
        t.pendown()
        t.color(couleur)
        t.begin_fill()
        t.circle(r)
        t.end_fill()

    for i in range(5):
        if i % 2 == 0:
            disque(100 - 20 * i, "red")
        else:
            disque(100 - 20 * i, "white")
    t.done()
    ```

### Entraînement

*Exercices courts pour s’entraîner aux gestes de base, chacun avec plusieurs données. Ils font tous partie du parcours essentiel.*

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 15</span> — Prédire la figure <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-T-15 }

<span class="essentiel">• essentiel</span>

Pour chaque programme (la tortue part de `(0, 0)`, tournée vers la droite), dessiner **à main levée, sans machine**, la figure obtenue, en indiquant le point de départ. <span class="run" title="À programmer et tester sur machine">▶</span> Exécuter ensuite pour vérifier.0

??? pouce "Coup de pouce"

    Suivre la tortue avec un crayon : à chaque `forward`, tracer le segment ; à chaque `left` ou `right`, faire pivoter le crayon. Compter de combien de degrés elle a tourné en tout.

a\)

```python
for i in range(5):
    t.forward(80)
    t.left(72)
```

b\)

```python
for i in range(4):
    t.forward(100)
    t.right(90)
```

c\)

```python
for i in range(2):
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)
```

d\)

```python
for i in range(3):
    t.forward(100)
    t.left(90)
```

??? corrige "Corrigé"

    a) Un **pentagone** régulier de côté 80, au-dessus du point de départ : $5 \times 72 = 360$, la figure se referme. b) Un **carré** de côté 100, tracé *sous* le point de départ : avec `right`, la tortue tourne dans le sens des aiguilles d’une montre. c) Un **rectangle** de 100 sur 50 (deux paires « grand côté, petit côté »). d) Une figure **ouverte** : trois côtés d’un carré ; la tortue n’a tourné que de $3 \times 90 = 270$ degrés, le côté gauche manque.

    <span class="erreurfreq">▷ Erreur fréquente.</span> confondre `left` et `right` : la figure b) est la même que le carré de l’exercice 1, mais retournée vers le bas.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 16</span> — Trouver l’angle <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-T-16 }

<span class="essentiel">• essentiel</span>

<span class="run" title="À programmer et tester sur machine">▶</span> Pour chacun des polygones réguliers suivants, donner l’angle dont la tortue doit tourner à chaque sommet, puis écrire la boucle qui le dessine avec des côtés de `60` : a) un pentagone (5 côtés) ; b) un octogone (8 côtés) ; c) un ennéagone (9 côtés) ; d) un décagone (10 côtés).0

??? pouce "Coup de pouce"

    Après le dernier côté, la tortue doit avoir fait exactement un tour complet sur elle-même : combien de degrés, à partager entre combien de sommets ?

??? corrige "Corrigé"

    L’angle vaut `360 / n` : a) $360 / 5 = 72$ ; b) $360 / 8 = 45$ ; c) $360 / 9 = 40$ ; d) $360 / 10 = 36$. Par exemple, pour le pentagone :

    ```python
    for i in range(5):
        t.forward(60)
        t.left(72)
    ```

    Pour les autres, on remplace `5` et `72` par `8` et `45`, `9` et `40`, `10` et `36`.
