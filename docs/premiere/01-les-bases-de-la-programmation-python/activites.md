# Activités préparatoires

<p class="sous-titre">Les bases de la programmation Python</p>

## <span class="etiquette">Activité 1</span> L’ordinateur humain

*exécuter un programme à la main, avant de savoir programmer*

<p class="infos-activite">Durée : 20 min · Sans ordinateur, crayon et gomme en main, par deux</p>

!!! consignes "Consignes"

    - Les réponses s’écrivent sur le cahier.

    - Vous êtes l’ordinateur. Vous lisez le programme **une ligne à la fois, de haut en bas**, et vous faites exactement ce qui est écrit, sans rien deviner.

    - Chaque nom (`a`, `b`, `total`…) désigne une **boîte**, que l’on dessine sur le cahier. Une boîte ne contient qu’**une seule valeur à la fois** : pour en écrire une nouvelle, on gomme l’ancienne.

    - `print(...)` signifie : « écrire à l’écran ce qu’il y a entre les parenthèses ». Ici, l’écran, c’est la ligne « Affichage obtenu : …» que vous écrivez sur le cahier.

### <span class="exo-num">Exercice 1</span> — Des boîtes et une flèche <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-les-bases-de-la-programmation-python-act-1-1 }

Programme 1 :

```python
a = 7
b = a + 3
a = 2
print(a, b)
```

1.  Dessiner sur le cahier deux boîtes `a` et `b`, puis exécuter le programme ligne par ligne en les remplissant (gommer quand une valeur change).

2.  Quel est l’affichage obtenu ?

3.  À la ligne 3, la boîte `a` change. La boîte `b` a-t-elle changé elle aussi ? Pourquoi ?

Programme 2 :

```python
n = 5
n = n + 1
print(n)
```

1.  En mathématiques, l’égalité $n = n + 1$ est impossible. Pourtant l’ordinateur l’exécute sans erreur. Qu’affiche-t-il ?

2.  Pour exécuter la ligne 2, par quel côté du signe `=` avez-vous commencé : la gauche ou la droite ? Décrire en une phrase ce que fait une ligne de la forme `nom = calcul`.

??? corrige "Corrigé"

    **1.** `a` : $7$, puis $2$ (le $7$ est gommé) ; `b` : $10$.

    **2.** Affichage : `2 10`.

    **3.** Non : à la ligne 2, on a calculé `a + 3` avec la valeur *de ce moment-là* ($7$) et rangé le **résultat** $10$ dans `b`. La boîte `b` contient un nombre, pas la formule « `a + 3` » : modifier `a` ensuite ne change pas `b`.

    **4.** Affichage : `6`.

    **5.** On commence par la **droite** : on calcule `n + 1` avec le contenu actuel de `n` ($5 + 1 = 6$), puis on range le résultat dans la boîte de **gauche**, `n`. Le signe `=` ne veut pas dire « est égal à » mais « **reçoit** ».

### <span class="exo-num">Exercice 2</span> — Échanger deux boîtes <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-les-bases-de-la-programmation-python-act-1-2 }

Programme 3 (il est censé échanger les contenus de `a` et de `b`) :

```python
a = 1
b = 2
a = b
b = a
print(a, b)
```

1.  Exécuter le programme en dessinant les boîtes `a` et `b` sur le cahier. Quel est l’affichage obtenu ? L’échange a-t-il réussi ?

2.  Où la valeur `1` est-elle passée ? Proposer une correction du programme, en vous autorisant une troisième boîte `c`.

??? corrige "Corrigé"

    **6.** `a` : $1$ puis $2$ ; `b` : $2$ puis $2$. Affichage : `2 2`. L’échange a échoué.

    **7.** La valeur `1` a été **gommée** par `a = b` : elle est perdue avant d’avoir pu être rangée dans `b`. Correction avec une troisième boîte :

    ```python
    a = 1
    b = 2
    c = a      # on met la valeur de a a l'abri
    a = b
    b = c
    print(a, b)   # 2 1
    ```

    Image à donner : pour échanger le contenu de deux verres, il faut un troisième verre vide.

### <span class="exo-num">Exercice 3</span> — Répéter sans réécrire <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-les-bases-de-la-programmation-python-act-1-3 }

Nouvelle règle : la ligne `for i in range(1, 5):` signifie « pour `i` valant successivement `1`, `2`, `3`, puis `4`, exécuter les lignes **décalées** juste en dessous ». Chaque passage s’appelle un **tour**.

Programme 4 :

```python
total = 0
for i in range(1, 5):
    total = total + i
print(total)
```

1.  Recopier et compléter sur le cahier le tableau suivant : valeurs des boîtes à la fin de chaque tour. Donner ensuite l’affichage obtenu.

    |         | avant la boucle | tour 1 | tour 2 | tour 3 | tour 4 |
    |:-------:|:---------------:|:------:|:------:|:------:|:------:|
    |   `i`   |        —        |        |        |        |        |
    | `total` |       `0`       |        |        |        |        |

2.  Combien de fois la ligne `print(total)` a-t-elle été exécutée ? Et la ligne `total = total + i` ?

3.  On décale la dernière ligne vers la droite, au même niveau que `total = total + i`. Que devient l’affichage ?

4.  Quelle unique modification faut-il apporter au programme 4 pour calculer $1 + 2 + \dots + 100$ ?

??? corrige "Corrigé"

    **8.**

    |         | avant la boucle | tour 1 | tour 2 | tour 3 | tour 4 |
    |:-------:|:---------------:|:------:|:------:|:------:|:------:|
    |   `i`   |        —        |   1    |   2    |   3    |   4    |
    | `total` |        0        |   1    |   3    |   6    |   10   |

    Affichage : `10`.

    **9.** `print(total)` : une seule fois (elle n’est pas décalée, elle est exécutée après la boucle). `total = total + i` : quatre fois, une par tour.

    **10.** La ligne fait alors partie de la boucle : elle est exécutée à chaque tour. Affichage : `1`, `3`, `6`, `10` (un nombre par ligne). Le décalage (l’**indentation**) change le sens du programme.

    **11.** Remplacer `range(1, 5)` par `range(1, 101)` : la borne de droite n’est pas atteinte. Le programme affiche alors `5050`.

### <span class="exo-num">Exercice 4</span> — Ce qu’on a découvert <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-les-bases-de-la-programmation-python-act-1-4 }

1.  Recopier et compléter sur le cahier avec vos mots.

    - Un nom comme `total` désigne …

    - Pour exécuter `nom = calcul`, l’ordinateur …

    - Les lignes décalées sous un `for` …

??? corrige "Corrigé"

    **12.** Réponse possible :

    - un nom comme `total` désigne une boîte de la mémoire qui contient une valeur : c’est une **variable** ;

    - pour exécuter `nom = calcul`, l’ordinateur calcule d’abord la partie droite avec les valeurs actuelles, puis range le résultat dans la boîte de gauche, en effaçant l’ancienne valeur : c’est l’**affectation** ;

    - les lignes décalées sous un `for` sont répétées, une fois par valeur de `i` : c’est une **boucle**.
