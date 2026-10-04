# Exercices

<p class="sous-titre">Les algorithmes gloutons</p>

!!! consignes "Mode d’emploi"

    - Niveau : ★ échauffement, ★★ classique (niveau bac), ★★★ défi ; les *coups de pouce* et les *corrigés* se déplient sous chaque exercice.

    - <span class="run" title="À programmer et tester sur machine">▶</span> *À programmer et tester* en Python. Le symbole `>>>` figure une saisie dans la console.

    - Coupures en euros disponibles (on oublie les centimes) : \; 1, 2, 5, 10, 20, 50, 100, 200.

    - Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la [charte d’usage de l’IA](../charte.md).

### Problèmes d’optimisation et principe glouton

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — Qu’optimise-t-on ? <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-11-1 }

Pour chaque problème, dire ce qu’on cherche à **minimiser** ou à **maximiser**.

1.  rendre une somme avec des pièces ;

2.  remplir un sac à dos de capacité limitée ;

3.  choisir un trajet passant par plusieurs villes ;

4.  répartir des fichiers sur des CD sans dépasser leur capacité.

??? corrige "Corrigé"

    !!! remarque "Remarque"

        On donne **une** version simple ; d’autres écritures sont possibles.

    a\) **minimiser** le nombre de pièces ; b) **maximiser** la valeur emportée ; c) **minimiser** la distance totale ; d) **minimiser** le nombre de CD utilisés.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 2</span> — Vrai ou faux <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-11-2 }

Répondre et justifier en une phrase.

1.  Un algorithme glouton fait, à chaque étape, le meilleur choix local.

2.  Un algorithme glouton revient en arrière s’il s’aperçoit qu’il s’est trompé.

3.  Un algorithme glouton donne toujours la solution optimale.

4.  Un algorithme glouton est en général rapide.

??? corrige "Corrigé"

    **a) V**. \; **b) F** : un glouton ne revient *jamais* sur un choix. \; **c) F** : il n’est pas toujours optimal. \; **d) V** : il est en général très rapide (un seul choix par étape).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 3</span> — Les ingrédients <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-11-3 }

Pour le rendu de monnaie glouton, identifier : (a) les **candidats**, (b) le **critère de choix glouton**, (c) la **contrainte de faisabilité**.

??? pouce "Coup de pouce"

    Relire les trois ingrédients du cours et se demander, pour chacun, ce qu’il devient quand on rend une somme : qu’ajoute-t-on à la solution, comment le choisit-on, qu’est-ce qui interdit un choix ?

??? corrige "Corrigé"

    a\) **candidats** : les coupures disponibles ; b) **critère glouton** : la plus grande coupure qui ne dépasse pas la somme restante ; c) **faisabilité** : une coupure n’est utilisable que si elle est $\leq$ à la somme restant à rendre.

### Rendu de monnaie

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 4</span> — Dérouler à la main <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-11-4 }

Avec les coupures en euros, appliquer la stratégie gloutonne et donner la liste des coupures rendues, puis leur nombre :

1.  8 € b) 27 € c) 63 € d) 199 €

??? corrige "Corrigé"

    a\) $8 = 5+2+1$ : **3** pièces. \; b) $27 = 20+5+2$ : **3**. \; c) $63 = 50+10+2+1$ : **4**. \; d) $199 = 100+50+20+20+5+2+2$ : **7**.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 5</span> — <span class="run" title="À programmer et tester sur machine">▶</span>  La fonction `rendre` <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-5 }

On donne la fonction du cours :

```python
pieces = [200, 100, 50, 20, 10, 5, 2, 1]
def rendre(somme):
    rendu = []
    for p in pieces:
        while somme >= p:
            rendu.append(p)
            somme = somme - p
    return rendu
```

1.  Tester `rendre(48)` et `rendre(88)`, puis utiliser la fonction pour vérifier vos réponses de l’exercice précédent (8, 27, 63 et 199 €).

2.  Écrire une fonction `nb_pieces(somme)` qui renvoie le **nombre** de coupures rendues (sans construire la liste).

3.  <span class="horsprog">au-delà du programme</span> Réécrire la boucle `while` à l’aide d’une division : le nombre de coupures `p` vaut `somme // p`, et il reste `somme % p`.

    ??? pouce "Coup de pouce"

        Pour b), garder la structure de `rendre`, mais remplacer la liste `rendu` par un compteur qui part de 0.

??? corrige "Corrigé"

    **a)** `rendre(48)` $=$ `[20, 20, 5, 2, 1]` (5 coupures) ; `rendre(88)` $=$ `[50, 20, 10, 5, 2, 1]` (6 coupures). **b)**

    ```python
    def nb_pieces(somme):
        n = 0
        for p in pieces:
            while somme >= p:
                n = n + 1
                somme = somme - p
        return n
    ```

    **c)** <span class="horsprog">au-delà du programme</span> Avec une division :

    ```python
    def rendre(somme):
        rendu = []
        for p in pieces:
            rendu = rendu + [p] * (somme // p)   # autant de p que possible
            somme = somme % p                    # ce qui reste apres ces p
        return rendu
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Un système qui piège le glouton <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-11-6 }

Dans un pays imaginaire, les pièces valent **1, 6 et 10**. On rend la somme **12**.

1.  Quelle solution donne l’algorithme glouton (plus grande pièce d’abord) ? Combien de pièces ?

2.  Existe-t-il une meilleure solution ? Laquelle ?

3.  Que peut-on conclure sur l’optimalité du glouton pour ce système ?

    ??? pouce "Coup de pouce"

        Pour b), chercher une solution qui n’utilise pas la pièce de 10.

??? corrige "Corrigé"

    **a)** Glouton : $10$, puis $1$, puis $1$ $\to$ `[10, 1, 1]`, soit **3 pièces**. **b)** Oui : $6 + 6$, soit **2 pièces**. **c)** Le glouton **n’est pas optimal** pour le système {1, 6, 10} : ce système n’est **pas canonique**.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Quand le glouton échoue carrément <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-7 }

Les pièces valent **2 et 3**. On veut rendre **4**.

1.  Dérouler l’algorithme glouton. Que se passe-t-il ?

2.  Une solution existe-t-elle pourtant ? Laquelle ?

3.  Expliquer la différence entre « le glouton n’est pas optimal » et « le glouton échoue ».

    ??? pouce "Coup de pouce"

        Suivre la somme restante après chaque pièce prise : que vaut-elle quand plus aucune pièce ne convient ?

??? corrige "Corrigé"

    **a)** Glouton : il prend $3$… il reste $1$, qu’aucune pièce (2 ou 3) ne permet de rendre : le glouton **échoue** (aucune solution trouvée). **b)** Pourtant $2 + 2 = 4$ : une solution existait. **c)** « Pas optimal » : le glouton trouve *une* solution, mais pas la meilleure (cas {1,6,10}). « Échoue » : le glouton ne trouve *aucune* solution, alors qu’il en existe une (cas {2,3}).

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 8</span> — Le rendu de monnaie en désordre <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-11-8 }

Les lignes de la fonction `rendre_general(systeme, somme)`, qui applique le rendu glouton pour un système de pièces quelconque (rangé de la plus grande à la plus petite), ont été mélangées et ont perdu leur indentation.

```text
return rendu
somme = somme - p
def rendre_general(systeme, somme):
while somme >= p:
rendu = []
rendu.append(p)
for p in systeme:
```

1.  Remettre les lignes dans l’ordre et les indenter correctement.

2.  Que renvoie `rendre_general([4, 3, 1], 6)` ? Est-ce le moins de pièces possible ?

??? corrige "Corrigé"

    **a)**

    ```python
    def rendre_general(systeme, somme):
        rendu = []
        for p in systeme:
            while somme >= p:
                rendu.append(p)
                somme = somme - p
        return rendu
    ```

    **b)** `[4, 1, 1]` : 3 pièces. Ce n’est **pas** le minimum, car $3 + 3 = 6$ n’utilise que 2 pièces : le système {4, 3, 1} n’est pas canonique.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 9</span> — <span class="run" title="À programmer et tester sur machine">▶</span>  Tester si un système est canonique <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-9 }

Un système est **canonique** si le glouton y est toujours optimal. On ne teste ici que les sommes de 1 à 30.

1.  Écrire `rendre_sys(systeme, somme)` qui applique le glouton pour un système de pièces quelconque (trié à l’envers) et renvoie le nombre de pièces (ou `None` si le glouton n’aboutit pas).

2.  On suppose disponible une fonction `optimal(systeme, somme)` qui renvoie le *vrai* nombre minimal de pièces. Écrire un test qui compare, pour toutes les sommes de 1 à 30, `rendre_sys` et `optimal`, et affiche la première somme où le glouton se trompe.

    ??? pouce "Coup de pouce"

        a\) Partir de `rendre_general` : compter les pièces au lieu de les ranger dans une liste ; à la fin, si la somme restante n’est pas nulle, le glouton n’a pas abouti. b) Une boucle sur les sommes de 1 à 30, et une comparaison à chaque tour.

    ??? pouce "Coup de pouce 2 (début de solution)"

        `def rendre_sys(systeme, somme):`  
        `n = 0`  
        `for p in systeme:`  
        …

??? corrige "Corrigé"

    ```python
    def rendre_sys(systeme, somme):
        n = 0
        for p in sorted(systeme, reverse=True):
            while somme >= p:
                n = n + 1
                somme = somme - p
        if somme == 0:
            return n
        return None            # le glouton n'aboutit pas

    def tester(systeme):
        for s in range(1, 31):
            if rendre_sys(systeme, s) != optimal(systeme, s):
                print("premier ecart pour la somme", s)
                return
        print("canonique jusqu'a 30")
    ```

    (Pour {1,6,10}, le premier écart apparaît pour la somme **12**.)

### Le sac à dos

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 10</span> — Remplir le sac <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-11-10 }

Sac de capacité **4 kg**. Objets : A (valeur 30, 2 kg), B (valeur 20, 2 kg), C (valeur 24, 3 kg).

1.  Calculer le rapport **valeur / poids** de chaque objet et les classer du meilleur au moins bon.

2.  Appliquer le glouton (meilleur rapport d’abord, tant que ça rentre). Quels objets emporte-t-on, pour quel poids et quelle valeur ?

3.  En essayant toutes les combinaisons qui tiennent dans 4 kg, vérifier qu’on ne fait pas mieux. Le glouton était-il optimal ici ?

    ??? pouce "Coup de pouce"

        Pour c), lister toutes les combinaisons possibles (un objet seul, deux objets…) et éliminer celles qui dépassent 4 kg.

??? corrige "Corrigé"

    **a)** Rapports valeur/poids : A $=30/2=\textbf{15}$, B $=20/2=\textbf{10}$, C $=24/3=\textbf{8}$. Classement : A, B, C. **b)** Glouton : A (2 kg, reste 2 kg, valeur 30), B (2 kg, reste 0, valeur 50), C (3 kg) ne rentre pas $\to$ on emporte **A $+$ B**, poids 4 kg, **valeur 50**. **c)** Les combinaisons qui tiennent dans 4 kg : {A}=30, {B}=20, {C}=24, {A,B}=50. La meilleure est A$+$B $=50$ : le glouton était **optimal** ici.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 11</span> — Un sac à dos où le glouton se trompe <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-11 }

Sac de capacité **5 kg**. Objets : A (valeur 60, 1 kg), B (valeur 100, 2 kg), C (valeur 120, 3 kg).

1.  Appliquer le glouton par rapport valeur/poids. Quelle valeur obtient-on ?

2.  Quelle est la meilleure combinaison possible ? De combien le glouton se trompe-t-il ?

    ??? pouce "Coup de pouce"

        Après avoir pris les objets de meilleur rapport, regarder la place qui reste : l’objet suivant y tient-il ? Pour b), comparer toutes les combinaisons qui tiennent dans 5 kg.

??? corrige "Corrigé"

    **a)** Rapports : A $=60$, B $=50$, C $=40$. Glouton : A (1 kg, reste 4, valeur 60), B (2 kg, reste 2, valeur 160), C (3 kg) ne rentre pas $\to$ **valeur 160**. **b)** La meilleure combinaison est **B $+$ C** (2$+$<!-- -->3 $=$ 5 kg, valeur **220**). Le glouton se trompe de **60**.

### Le plus proche voisin (voyageur)

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 12</span> — Toujours vers le plus proche <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-11-12 }

Quatre villes, distances (en km) :

|     |  A  |  B  |  C  |  D  |
|:---:|:---:|:---:|:---:|:---:|
|  A  |  —  | 10  | 15  | 20  |
|  B  | 10  |  —  | 35  | 25  |
|  C  | 15  | 35  |  —  | 30  |
|  D  | 20  | 25  | 30  |  —  |

On part de **A**, on visite toutes les villes et on revient à A, en allant à chaque fois vers la ville **non visitée la plus proche**.

1.  Dérouler l’algorithme glouton : donner l’itinéraire et la distance totale.

2.  L’itinéraire A–C–B–D–A mesure-t-il plus ou moins que celui du glouton ? Que peut-on dire de la qualité de la solution gloutonne *ici* (et est-ce garanti en général) ?

    ??? pouce "Coup de pouce"

        À chaque étape, ne lire que la ligne de la ville où l’on se trouve, en barrant les villes déjà visitées. Ne pas oublier le retour à A.

??? corrige "Corrigé"

    **a)** Départ A. Plus proche : B (10). Depuis B, non visitées C (35) et D (25) $\to$ D (25). Depuis D, reste C (30) $\to$ C. Retour C$\to$A (15). Itinéraire **A–B–D–C–A**, distance $10+25+30+15 = \textbf{80}$ km. **b)** A–C–B–D–A $= 15+35+25+20 = 95$ km, donc **plus long**. Ici la solution gloutonne (80 km) est en fait la **meilleure** — mais ce n’**est pas garanti** : sur de nombreuses villes, le glouton « plus proche voisin » est rarement optimal (cf. cours).

### Mini-problème de synthèse

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 13</span> — Le distributeur de billets <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-13 }

Un distributeur ne contient que des billets de **50, 20 et 10** euros. On retire une somme (multiple de 10).

1.  Appliquer le glouton pour 90 €, puis pour 80 €. Combien de billets à chaque fois ?

2.  Ce système {10, 20, 50} est-il canonique pour les multiples de 10 jusqu’à 100 ? (tester à la main ou en réutilisant `rendre_sys`).

3.  Le distributeur n’a plus de billets de 20. Pour 80 €, le glouton avec {10, 50} donne-t-il encore la solution en le moins de billets ?

    ??? pouce "Coup de pouce"

        Pour b), comparer, pour chaque somme 10, 20, …, 100, le nombre de billets du glouton à la meilleure solution trouvée à la main.

    ??? pouce "Coup de pouce 2 (début de solution)"

        a\) Pour 90 €, le glouton prend 50, puis 20 et encore 20 : 3 billets. c) Le glouton commence par 50 : que reste-t-il à rendre, et avec quels billets ?

??? corrige "Corrigé"

    **a)** Pour 90 : $50+20+20$ $\to$ **3 billets**. Pour 80 : $50+20+10$ $\to$ **3 billets**. **b)** Le système {10, 20, 50} est **canonique** pour les multiples de 10 jusqu’à 100 (le glouton donne le minimum pour chacun : c’est l’équivalent, à un facteur 10 près, du système {1, 2, 5}). **c)** Avec {10, 50} pour 80 : $50+10+10+10$ $\to$ **4 billets**. C’est bien le minimum *pour ce système réduit* (le glouton reste optimal sur {10, 50}) ; simplement, faute de billet de 20, il faut un billet de plus qu’avant.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 14</span> — Le rendu de monnaie selon un assistant d’IA <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> { #ex-11-14 }

Un élève demande à un assistant d’IA : « Écris une fonction Python qui rend une somme avec le moins de pièces possible. » Voici la réponse obtenue.

```python
def rendre(somme, pieces):
    """pieces : liste des coupures, triee par ordre decroissant"""
    rendu = []
    for p in pieces:
        while somme >= p:
            rendu.append(p)
            somme = somme - p
    return rendu
```

« Cette fonction est gloutonne : à chaque étape, elle prend la plus grande pièce possible. Elle renvoie toujours le nombre minimal de pièces, quel que soit le système de pièces fourni, puisqu’elle utilise à chaque fois la coupure la plus grande. »

1.  La réponse est-elle correcte ? Vérifier à la main avec le système {4, 3, 1} et la somme 6.

2.  Localiser l’erreur (dans le code ou dans l’explication) et la corriger.

3.  Quelle vérification simple, faite avant de faire confiance à la réponse, aurait suffi à détecter l’erreur ?

    ??? pouce "Coup de pouce"

        Comparer le code à celui du cours. S’il est identique, l’erreur est dans une phrase de l’explication : laquelle est contredite par l’exercice « Un système qui piège le glouton » ?

??? corrige "Corrigé"

    **a)** Non. Avec `pieces = [4, 3, 1]` et `somme = 6`, la fonction renvoie `[4, 1, 1]` (3 pièces), alors que `[3, 3]` rend 6 avec **2 pièces**. **b)** Le *code* est un glouton correct (il rend bien la somme) ; l’erreur est dans l’*explication* : « quel que soit le système de pièces ». Le glouton n’est optimal que pour les systèmes **canoniques** (comme les euros). Correction : « elle donne le nombre minimal de pièces *pour un système canonique* ; pour un autre système, la solution est correcte mais pas forcément optimale ». **c)** Tester la fonction sur un petit système **non canonique**, comme celui du cours ({1, 6, 10} pour 12 : le glouton donne 3 pièces, $6 + 6$ en donne 2). Une affirmation en « toujours » se réfute avec un seul contre-exemple.
