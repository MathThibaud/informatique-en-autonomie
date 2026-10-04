# Activités préparatoires

<p class="sous-titre">Les algorithmes de tri</p>

## <span class="etiquette">Activité 1</span> Trier sans tricher

*ranger 8 cartes en comptant les comparaisons*

<p class="infos-activite">Durée : 20 min · Par binômes, sans machine, réponses sur le cahier</p>

!!! consignes "Consignes"

    - Matériel : 8 cartes numérotées, posées **face cachée**.

    - L’un est le **trieur**, l’autre l’**arbitre**. L’arbitre mélange les cartes et les aligne face cachée sur la table, aux positions 0 à 7.

    - Le trieur **ne voit jamais** les valeurs. Il n’a droit qu’à deux actions :

      - **comparer** : il désigne deux cartes ; l’arbitre les regarde en cachette et dit laquelle est la plus petite. L’arbitre fait **un trait** à chaque comparaison ;

      - **déplacer** : il échange deux cartes, ou glisse une carte à un autre endroit de la ligne (gratuit, sans regarder).

    - Objectif : ranger les cartes de la plus petite (à gauche) à la plus grande (à droite), avec **le moins de comparaisons possible**. À la fin, on retourne les cartes pour vérifier.

    - *Variante :* 8 boîtes opaques de masses différentes et une balance à deux plateaux ; comparer, c’est peser deux boîtes l’une contre l’autre.

### <span class="exo-num">Exercice 1</span> — Chacun sa méthode <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-06-les-algorithmes-de-tri-act-1-1 }

1.  Premier tri. Nombre de comparaisons ? Le rangement est-il réussi ?

2.  Décrire en deux ou trois phrases la méthode utilisée.

3.  On échange les rôles et l’arbitre remélange. Le nouveau trieur essaie une **autre** méthode. Nombre de comparaisons ?

4.  Relever les résultats des autres binômes. Quel est le plus petit nombre de comparaisons de la classe ? Une même méthode donne-t-elle toujours le même nombre ?

??? corrige "Corrigé"

    **1–3.** Réponses variables : en général entre 15 et 30 comparaisons. On vérifie en retournant les cartes. Les méthodes inventées ressemblent presque toujours à l’une des deux méthodes de l’exercice 2 (chercher le plus petit, ou ranger au fur et à mesure) ; on peut aussi couper le paquet en deux, trier chaque moitié, puis les réunir : c’est une autre méthode, plus rapide, qu’on retrouvera plus tard.  
    **4.** Le minimum de la classe est souvent autour de 16 à 20. Une même méthode ne donne pas toujours le même nombre : avec la méthode « main de cartes », cela dépend de l’ordre de départ. *Remarque :* on ne peut pas garantir de trier 8 cartes en moins de 16 comparaisons, quelle que soit la méthode (il y a $8! = 40\,320$ ordres possibles, et chaque comparaison divise au mieux les possibilités par deux : $2^{15} < 40\,320 \leq 2^{16}$). Hors programme.

### <span class="exo-num">Exercice 2</span> — Deux méthodes à l’essai <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-06-les-algorithmes-de-tri-act-1-2 }

**Méthode 1 — « le plus petit d’abord ».** On garde une carte « championne » et on la compare tour à tour à toutes les autres (si l’autre est plus petite, elle devient la championne) : on obtient la plus petite des 8, qu’on place en position 0. On recommence avec les 7 cartes restantes, et ainsi de suite.

1.  Combien faut-il de comparaisons pour trouver la plus petite des 8 cartes ? la plus petite des 7 restantes ? Combien en tout ? Vérifier en appliquant la méthode.

2.  Ce total dépend-il de l’ordre dans lequel l’arbitre a posé les cartes ?

**Méthode 2 — « comme une main de cartes ».** On prend les cartes une par une, de gauche à droite. Chaque nouvelle carte est comparée à ses voisines de gauche, de la plus proche à la plus lointaine, et glissée à sa place parmi les cartes déjà rangées : on s’arrête dès qu’on rencontre une carte plus petite qu’elle (ou qu’on arrive au bout).

1.  L’arbitre pose les cartes **déjà dans l’ordre**. Nombre de comparaisons avec la méthode 2 ?

2.  L’arbitre pose les cartes **dans l’ordre inverse**. Nombre de comparaisons ?

3.  Les cartes sont *presque* rangées (seules deux voisines sont inversées). Quelle méthode choisir ? Pourquoi ?

??? corrige "Corrigé"

    **5.** 7 comparaisons pour la plus petite des 8 (la championne affronte les 7 autres), puis 6, 5, …, 1 : en tout $7 + 6 + 5 + 4 + 3 + 2 + 1 = 28$.  
    **6.** Non : on fait toujours les 28 comparaisons, que les cartes soient mélangées, rangées ou à l’envers.  
    **7.** Cartes déjà rangées : chaque nouvelle carte est comparée à sa voisine de gauche, plus petite, et ne bouge pas : $7$ comparaisons seulement.  
    **8.** Ordre inverse : chaque nouvelle carte doit remonter tout au début ; la 2<sup>e</sup> carte fait 1 comparaison, la 3<sup>e</sup> en fait 2, …, la 8<sup>e</sup> en fait 7 : $1 + 2 + \cdots + 7 = 28$.  
    **9.** La méthode 2 : sur des cartes presque rangées, elle ne fait que 7 ou 8 comparaisons, contre 28 pour la méthode 1, qui ne profite pas de l’ordre déjà présent.

### <span class="exo-num">Exercice 3</span> — Ce qu’on a découvert <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-06-les-algorithmes-de-tri-act-1-3 }

1.  Avec la méthode 1 et **16** cartes, combien faudrait-il de comparaisons ? Environ combien de fois plus qu’avec 8 cartes ?

2.  **Ce qu’on a découvert.** Recopier et compléter sur le cahier : « Trier, c’est réorganiser les éléments pour qu’ils soient …, en n’utilisant que deux opérations : … deux éléments et les …. Pour savoir si une méthode est rapide, on compte … »

??? corrige "Corrigé"

    **10.** $15 + 14 + \cdots + 1 = \frac{16 \times 15}{2} = 120$ comparaisons, environ **4 fois** plus que 28 : doubler le nombre de cartes quadruple (à peu près) le travail.  
    **11.** « Trier, c’est réorganiser les éléments pour qu’ils soient **dans l’ordre croissant**, en n’utilisant que deux opérations : **comparer** deux éléments et les **échanger** (ou les déplacer). Pour savoir si une méthode est rapide, on compte **les comparaisons**. »
