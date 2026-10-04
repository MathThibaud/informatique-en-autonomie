# Activités préparatoires

<p class="sous-titre">Algorithmique : le parcours séquentiel</p>

## <span class="etiquette">Activité 1</span> La carte la plus haute

*trouver un maximum en ne retenant qu’une seule carte*

<p class="infos-activite">Durée : 20 min · Sans ordinateur, par deux</p>

!!! consignes "Consignes"

    - Matériel : un paquet de cartes (ou des petits papiers numérotés). Les réponses aux questions s’écrivent sur le cahier.

    - Le **meneur** mélange une dizaine de cartes, les pose en pile face cachée, puis les retourne **une par une**. Une carte retournée est aussitôt défaussée : on ne peut plus la revoir.

    - Le **chercheur** n’a le droit de garder **qu’une seule carte en main**, et ne prend aucune note. Quand la pile est vide, il doit annoncer la carte la plus haute du paquet.

    - Valeurs : as $= 1$, valet $= 11$, dame $= 12$, roi $= 13$. On échange les rôles à chaque partie.

![](../figures/d93a059a539157fd.svg){ .tikz loading=lazy }

### <span class="exo-num">Exercice 1</span> — Jouer <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-04-algorithmique-le-parcours-sequentiel-act-1-1 }

1.  Jouer deux parties de 10 cartes (une fois chercheur, une fois meneur). Le chercheur a-t-il trouvé la bonne carte à chaque fois ?

2.  Que fait le chercheur avec la **toute première** carte retournée ? Pourquoi ?

3.  Écrire la règle du chercheur sous la forme : « à chaque nouvelle carte, si … alors … ; sinon … ».

4.  Le meneur a vu passer 9 cartes sur 10 ; le chercheur tient un roi. Peut-il annoncer « c’est le roi » sans regarder la dernière carte ? Et s’il tient un 10 ? Peut-on, en général, s’arrêter avant la fin de la pile ?

??? corrige "Corrigé"

    **1.** Oui, si la règle est bien appliquée : le chercheur trouve toujours la plus haute carte.

    **2.** Il la **garde** : il n’a encore rien en main, et c’est pour l’instant la plus haute carte vue.

    **3.** « À chaque nouvelle carte, si elle est plus haute que celle que je tiens, alors je la prends et je jette l’ancienne ; sinon je la jette. »

    **4.** Avec un roi, oui : $13$ est la plus haute valeur possible, rien ne peut le battre (c’est une information *en plus* sur le paquet). Avec un 10, non : la dernière carte peut être un valet, une dame ou un roi. En général, **on ne peut pas s’arrêter avant la fin** : pour être sûr d’avoir le maximum, il faut avoir tout regardé.

### <span class="exo-num">Exercice 2</span> — Compter le travail <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-04-algorithmique-le-parcours-sequentiel-act-1-2 }

Une **comparaison**, c’est regarder la carte retournée et la carte en main pour décider laquelle garder.

1.  Combien de comparaisons le chercheur a-t-il faites pour 10 cartes ? Combien en ferait-il pour 52 cartes ? Pour $n$ cartes ?

2.  Le meneur cherche à faire **changer** de carte le chercheur le plus souvent possible. Dans quel ordre doit-il ranger la pile ? Et pour qu’il ne change **jamais** de carte ? Le nombre de comparaisons change-t-il ?

3.  Un camarade propose une astuce : « au départ, je fais comme si je tenais une carte de valeur $0$ ». On rejoue avec des petits papiers portant des **températures** : $-3$, $-8$, $-1$, $-5$, $-6$. Qu’annonce le camarade ? A-t-il raison ? Quelle est la bonne façon de commencer ?

4.  Nouvelle mission : annoncer **combien** de cartes rouges contient la pile, toujours sans rien noter. Que faut-il retenir pendant la partie, et comment le faire évoluer à chaque carte ?

??? corrige "Corrigé"

    **5.** La première carte est prise sans comparaison, puis une comparaison par carte suivante : $9$ comparaisons pour 10 cartes, $51$ pour 52 cartes, $n - 1$ pour $n$ cartes. *(Dans le cours, `for x in t` compare aussi `t[0]` avec lui-même : $n$ comparaisons, ce qui ne change rien à l’ordre de grandeur.)*

    **6.** Pile rangée dans l’ordre **croissant** : le chercheur change de carte à chaque fois ($9$ changements). Plus haute carte en premier (par exemple ordre décroissant) : il ne change jamais. Dans les deux cas, il fait **toujours $9$ comparaisons** : le nombre de comparaisons ne dépend pas de l’ordre des cartes, seulement de leur nombre.

    **7.** Le camarade annonce $0$ : aucune température ne bat sa carte imaginaire. C’est faux ($0$ n’est même pas dans la pile ; la réponse est $-1$). La bonne façon de commencer est de **garder la première vraie carte**, comme à la question 2.

    **8.** On retient un **nombre**, qui vaut $0$ au départ, et on lui ajoute $1$ à chaque carte rouge. Ici, partir de $0$ est correct : avant d’avoir vu une carte, on a bien compté zéro carte rouge.

### <span class="exo-num">Exercice 3</span> — Ce qu’on a découvert <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-04-algorithmique-le-parcours-sequentiel-act-1-3 }

1.  Recopier et compléter sur le cahier, avec vos mots.

    - On examine les cartes …

    - À tout moment de la partie, la carte en main est …

    - Pour $n$ cartes, il faut … comparaisons : si le paquet double, le travail …

    - Pour trouver la plus haute carte ou pour compter les rouges, on fait la même chose : …

??? corrige "Corrigé"

    **9.**

    - On examine les cartes **une par une, de la première à la dernière, sans en sauter**.

    - À tout moment, la carte en main est **la plus haute des cartes déjà vues** (le « meilleur jusqu’ici »).

    - Pour $n$ cartes, il faut $n - 1$ comparaisons : si le paquet double, le travail **double** aussi (il est proportionnel au nombre de cartes).

    - Même schéma : on **prépare** une information au départ (la première carte, ou le compteur à $0$), on la **met à jour** à chaque carte, on l’**annonce** à la fin.
