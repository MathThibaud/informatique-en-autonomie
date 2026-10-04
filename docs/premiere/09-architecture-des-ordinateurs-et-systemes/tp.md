# TP et projets

<p class="sous-titre">Architecture des ordinateurs et systèmes d'exploitation</p>

## <span class="etiquette">TP</span> Sous le capot

*programmer un processeur-jouet, puis piloter un vrai Linux en ligne de commande*

<p class="infos-activite">Durée : 2 à 3 h (une séance par partie) · En binôme, sur machine</p>

!!! encadre "But du TP"

    Deux couches du « mille-feuille » du cours, à pratiquer sur machine. **Partie A** : écrire de vrais programmes pour le **Little Man Computer** (LMC), le processeur-modèle du cours, et les regarder s’exécuter instruction par instruction — calculs, tests, boucles. **Partie B** : dans un vrai Linux qui tourne dans le navigateur, construire une arborescence, manipuler des fichiers, puis mettre à l’épreuve les **droits d’accès** avec deux utilisateurs. Produits finaux : une collection de programmes LMC qui marchent, et un **tableau « qui peut faire quoi »** établi par l’expérience.

!!! consignes "Consignes"

    - Rien à installer. Gardez sous les yeux le jeu d’instructions LMC et le tableau des commandes du cours.

    - Partie A : `peterhigginson.co.uk/lmc/`. On tape le programme dans la zone de gauche, on clique sur **Submit** (ou **Assemble into RAM**), puis **Run** (ou **Step** pour avancer d’une instruction). Quand la machine attend une entrée, on tape le nombre dans la case **Input** puis **Entrée**. Les boutons `<<` et `>>` règlent la vitesse.

    - Partie B : `bellard.org/jslinux/`, ligne **x86 – Alpine Linux 3.12.0 – Console** (comme dans l’activité « Perdu dans le terminal »). Recharger la page remet tout à zéro : notez vos commandes au fur et à mesure.

    - <span class="run" title="À programmer et tester sur machine">▶</span> *À faire sur machine.* Pour chaque programme écrit, recopier le code final et les tests effectués (sur le cahier ou dans un fichier texte). Niveau : ★ échauffement, ★★ classique (niveau bac), ★★★ défi ; les *coups de pouce* et les *corrigés* se déplient sous chaque exercice.

    - Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la [charte d’usage de l’IA](../charte.md).

## Partie A — Programmer le Little Man Computer

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — Prise en main : la somme, vue de l’intérieur <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-tp-1-1 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Taper le programme du cours (avec des étiquettes, le simulateur choisit lui-même les adresses), l’assembler, puis l’exécuter **pas à pas** avec les entrées 5 puis 3.

```text
     INP
     STA a
     INP
     STA b
     LDA a
     ADD b
     OUT
     HLT
a    DAT
b    DAT
```

1.  Après l’assemblage, quels nombres apparaissent dans les cases 00 à 09 de la mémoire (RAM) ? Recopier-les.

2.  En comparant au programme, retrouver le **code** de chaque instruction : `INP` $\to$ …, `STA` $\to$ 3 …, `LDA` $\to$ …, `ADD` $\to$ …, `OUT` $\to$ …, `HLT` $\to$ … Que signifient les deux derniers chiffres ?

3.  Pendant l’exécution pas à pas, observer le **compteur de programme** : de combien avance-t-il à chaque instruction ? Quelle est sa valeur quand la machine s’arrête ?

4.  Quelle idée du modèle de von Neumann cette mémoire illustre-t-elle ?

??? corrige "Corrigé"

    Tous les programmes LMC ci-dessous ont été vérifiés avec un interpréteur LMC écrit en Python (mêmes codes d’instructions que le simulateur de Peter Higginson) sur de nombreuses entrées, et la multiplication a été exécutée sur le simulateur en ligne. Les sorties de terminal de la partie B ont été obtenues dans JSLinux (Alpine Linux 3.12.0, console x86).

    **1.** Un `if` : un calcul (souvent `SUB`) suivi d’un saut conditionnel `BRZ` ou `BRP`, et d’un `BRA` pour sauter par-dessus le bloc « sinon ». Une boucle `while` : une étiquette en haut, un test de sortie (`BRZ`/`BRP` vers `fin`) et un `BRA` qui remonte. **2.** La mémoire ne contient que des nombres : les instructions sont codées (`ADD 09` $\to$ `109`). Les mots sont pour les humains (l’assembleur), les nombres pour la machine (le langage machine). **3.** Tableau complété :

    | pour… | lire un fichier | modifier un fichier | créer/supprimer dans un répertoire |
    |:---|:---|:---|:---|
    | il faut le droit… | `r` | `w` | `w` (et `x`) |
    | sur… | le fichier (et `x` sur les répertoires traversés) | le fichier | le répertoire |
    | `root` est-il concerné ? | non | non | non |

    Seule exception observée : pour *exécuter* un fichier, même `root` a besoin qu’au moins un `x` soit présent (exercice 10).

    **1.** Cases 00 à 09 : `901  308  901  309  508  109  902  000  000  000`. **2.** `INP` $\to$ 901, `STA` $\to$ 3 …, `LDA` $\to$ 5 …, `ADD` $\to$ 1 …, `OUT` $\to$ 902, `HLT` $\to$ 000. Les deux derniers chiffres sont l’**adresse** de la case visée (`a` est en 08, `b` en 09). **3.** Le compteur de programme avance de **1** à chaque instruction (il est incrémenté au moment où l’instruction est *cherchée*) ; à l’arrêt, il vaut **08** : l’instruction `HLT` (case 07) a déjà été lue. **4.** Le programme est fait de **nombres rangés dans la même mémoire que les données** (les cases 08 et 09 contiennent les données, les cases 00 à 07 le programme) : c’est l’idée clé de von Neumann.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 2</span> — Le programme mystère <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-tp-1-2 }

Voici le contenu des cases 00 à 09 d’une mémoire, **sans** le programme assembleur : `901  309  901  109  309  109  902  000  000  000`.

On sait aussi que `SUB` a pour code 2 …, `BRA` 6 …, `BRZ` 7 … et `BRP` 8 ….

1.  « Désassembler » : réécrire ce programme en assembleur, une instruction par case.

2.  Dérouler à la main pour les entrées 5 puis 3. Que calcule ce programme ?

3.  <span class="run" title="À programmer et tester sur machine">▶</span>  Vérifier de deux façons : taper votre version assembleur dans le simulateur et contrôler qu’après l’assemblage la RAM contient exactement les nombres de l’énoncé ; puis l’exécuter avec 5 et 3.

??? corrige "Corrigé"

    ```text
    00  INP
    01  STA 09
    02  INP
    03  ADD 09
    04  STA 09
    05  ADD 09
    06  OUT
    07  HLT
    ```

    Déroulé pour 5 puis 3 : ACC $=5$, case 09 $=5$ ; ACC $=3$ ; ACC $=3+5=8$ ; case 09 $=8$ ; ACC $=8+8=16$ ; sortie **16**.

    Le programme calcule $2 \times (a + b)$.

    Assemblé, ce code redonne exactement les nombres de l’énoncé (les cases 08 et 09 restent à 000 avant l’exécution).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 3</span> — L’écart entre deux nombres <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-tp-1-3 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Écrire un programme qui lit deux nombres $a$ et $b$ et affiche leur **écart** (la différence du plus grand moins le plus petit) : 2 et 7 donnent 5 ; 7 et 2 donnent 5 aussi. Le tester sur ces deux cas, puis avec deux nombres égaux.

??? pouce "Coup de pouce"

    Calculer d’abord `b - a` : si le résultat est positif ou nul (`BRP`), c’est la réponse ; sinon, recalculer dans l’autre sens `a - b`.

??? corrige "Corrigé"

    ```text
           INP
           STA a
           INP
           STA b
           SUB a
           BRP fin
           LDA a
           SUB b
    fin    OUT
           HLT
    a      DAT
    b      DAT
    ```

    Tests : (2, 7) $\to$ 5 ; (7, 2) $\to$ 5 ; (4, 4) $\to$ 0.

    Après `SUB a`, l’accumulateur contient $b - a$. S’il est positif ou nul, c’est l’écart et l’on saute directement à `OUT` ; sinon on recalcule $a - b$. C’est un `if … else` : `BRP` joue le rôle du test.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 4</span> — Le compte à rebours <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-tp-1-4 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Écrire un programme qui lit un nombre $n$ puis affiche $n$, $n-1$, …, $1$, $0$ et s’arrête. Le tester avec 3 (sorties : 3, 2, 1, 0), puis avec 0.

1.  Quelle instruction permet de **revenir en arrière** dans le programme ? Laquelle permet d’en **sortir** ?

2.  Il faut retirer 1 à chaque tour : où trouver ce 1 ? (Indice : `DAT` peut recevoir une valeur initiale, par exemple `un DAT 1`.)

3.  Que se passerait-il si l’on oubliait le test d’arrêt ? *Ne pas essayer longtemps : bouton **Stop**.*

??? pouce "Coup de pouce"

    Une boucle en LMC : une étiquette sur la première instruction du corps (`boucle OUT`), un test qui saute vers `fin` quand l’accumulateur vaut 0 (`BRZ fin`), et un saut inconditionnel `BRA boucle` en bas du corps.

??? corrige "Corrigé"

    ```text
           INP
    boucle OUT
           BRZ fin
           SUB un
           BRA boucle
    fin    HLT
    un     DAT 1
    ```

    Tests : 3 $\to$ 3, 2, 1, 0 ; 0 $\to$ 0.

    **1.** `BRA boucle` revient en arrière ; `BRZ fin` fait sortir quand ACC vaut 0. **2.** Dans une case initialisée par `un DAT 1`. **3.** Sans `BRZ`, la boucle ne s’arrête plus d’elle-même : le programme affiche des nombres négatifs indéfiniment (il faut l’arrêter).

    Autre solution correcte : ranger $n$ dans une case et faire `LDA`/`SUB`/`STA` à chaque tour (plus long mais correct).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 5</span> — La multiplication sans multiplier <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-tp-1-5 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Le LMC ne sait pas multiplier. Mais $a \times b$, c’est $a + a + \dots + a$ ($b$ fois).

1.  Écrire un programme qui lit $a$ puis $b$ et affiche $a \times b$, en ajoutant $a$ à un résultat `res` (initialisé à 0) et en décrémentant $b$ à chaque tour, jusqu’à ce que $b$ vaille 0. Le tester : $6 \times 7$, $5 \times 0$, $0 \times 5$.

2.  Le corps de la boucle compte 8 instructions. Combien d’instructions environ la machine exécute-t-elle pour $3 \times 200$ ? Et pour $200 \times 3$ ? Comment rendre le programme plus rapide dans le premier cas ?

??? pouce "Coup de pouce"

    Cases à prévoir : `a DAT`, `b DAT`, `res DAT 0`, `un DAT 1`. Le corps de boucle : charger `b` ; s’il vaut 0, aller à `fin` ; sinon `b` $\leftarrow$ `b` $-$ 1, puis `res` $\leftarrow$ `res` $+$ `a`.

??? corrige "Corrigé"

    ```text
           INP
           STA a
           INP
           STA b
    boucle LDA b
           BRZ fin
           SUB un
           STA b
           LDA res
           ADD a
           STA res
           BRA boucle
    fin    LDA res
           OUT
           HLT
    a      DAT
    b      DAT
    res    DAT 0
    un     DAT 1
    ```

    **1.** Tests : $6 \times 7 \to 42$ (vérifié aussi sur le simulateur en ligne) ; $5 \times 0 \to 0$ ; $0 \times 5 \to 0$.

    **2.** La machine exécute $8b + 9$ instructions : 4 pour les entrées, 8 par tour de boucle, 2 pour le dernier test, 3 pour finir. Pour $3 \times 200$ : **1 609** instructions ; pour $200 \times 3$ : **33** seulement. Pour aller plus vite, il faut boucler sur le **plus petit** des deux nombres : comparer $a$ et $b$ au début (`SUB` puis `BRP`) et les échanger si besoin.

    *Même résultat, coût très différent : c’est déjà une question d’algorithmique.*

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Le plus grand de trois <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-tp-1-6 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

L’exercice 8 (« Le plus grand des deux ») de la rubrique Exercices de ce chapitre donne un programme qui affiche le plus grand de *deux* nombres. Écrire un programme qui lit **trois** nombres et affiche le plus grand. Le tester avec au moins quatre jeux d’entrées bien choisis (le maximum en 1<sup>re</sup>, 2<sup>e</sup>, 3<sup>e</sup> position ; des nombres égaux).

??? pouce "Coup de pouce"

    Appliquer l’invariant du champion : ranger le premier nombre dans une case `max` ; pour chacun des deux autres, calculer `nombre - max` ; si c’est positif ou nul (`BRP`), ce nombre devient le nouveau `max`.

??? corrige "Corrigé"

    ```text
           INP
           STA a
           INP
           STA b
           INP
           STA c
           LDA a
           STA max
           LDA b
           SUB max
           BRP prendb
           BRA testc
    prendb LDA b
           STA max
    testc  LDA c
           SUB max
           BRP prendc
           BRA fin
    prendc LDA c
           STA max
    fin    LDA max
           OUT
           HLT
    a      DAT
    b      DAT
    c      DAT
    max    DAT
    ```

    Tests : (9, 4, 7) $\to$ 9 ; (4, 9, 7) $\to$ 9 ; (4, 7, 9) $\to$ 9 ; (7, 7, 2) $\to$ 7. Le programme a été vérifié par l’interpréteur sur les 125 triplets formés avec 0, 1, 4, 7, 9.

    C’est l’**invariant du champion** du chapitre *Algorithmique : le parcours séquentiel* : `max` contient le plus grand nombre vu jusque-là.

    Erreur fréquente : oublier `BRA testc` (ou `BRA fin`) ; la machine « tombe » alors dans le bloc suivant et prend toujours `b` (ou `c`).

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Division euclidienne <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-tp-1-7 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Écrire un programme qui lit $a$ puis $b$ (avec $b > 0$) et affiche le **quotient** puis le **reste** de la division euclidienne de $a$ par $b$, en retirant $b$ à $a$ autant de fois que possible. Tester : $17$ et $5$ (sorties 3 puis 2) ; $15$ et $5$ ; $4$ et $9$. Que se passe-t-il si $b = 0$ ? Quel est l’équivalent Python de ce programme (avec une boucle `while`) ?

??? corrige "Corrigé"

    ```text
           INP
           STA a
           INP
           STA b
    boucle LDA a
           SUB b
           BRP suite
           BRA fin
    suite  STA a
           LDA q
           ADD un
           STA q
           BRA boucle
    fin    LDA q
           OUT
           LDA a
           OUT
           HLT
    a      DAT
    b      DAT
    q      DAT 0
    un     DAT 1
    ```

    Tests : (17, 5) $\to$ 3 puis 2 ; (15, 5) $\to$ 3 puis 0 ; (4, 9) $\to$ 0 puis 4. Vérifié par l’interpréteur pour tous les $a$ de 0 à 59 et $b$ de 1 à 11.

    Si $b = 0$, `a - b` reste toujours positif : la boucle ne s’arrête jamais (`q` augmente sans fin). Un programme correct testerait $b$ dès le départ.

    Équivalent Python :

    ```python
    q = 0
    while a >= b:
        a = a - b
        q = q + 1
    print(q, a)
    ```

## Partie B — Piloter Linux en ligne de commande

Dans JSLinux, vous êtes connecté en tant qu’administrateur : l’invite se termine par `#` (et non par `$`). Rappels pratiques : la touche **Tab** complète les noms ; la flèche **haut** rappelle les commandes précédentes ; `history` les liste toutes. La commande `man` n’est pas installée ici : `ls --help` affiche l’aide d’une commande.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 8</span> — Où suis-je, qui suis-je ? <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-tp-1-8 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

1.  Taper `whoami`, `pwd`, puis `ls -l`. Qui êtes-vous ? Où êtes-vous ? Quel est le chemin absolu de votre répertoire personnel ?

2.  Pour `readme.txt`, écrire les droits du propriétaire, du groupe et des autres. Qui en est le propriétaire ?

??? corrige "Corrigé"

    **1.** `whoami` affiche `root` ; `pwd` affiche `/root` (c’est le répertoire personnel de l’administrateur). **2.** `ls -l` montre `-rw-r--r--  1 root root  151 … readme.txt` : fichier ordinaire, propriétaire `root` en lecture-écriture, groupe et autres en lecture seule.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 9</span> — Construire l’arborescence du club <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-tp-1-9 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

On veut obtenir, dans le répertoire personnel, l’arborescence suivante :

```text
club
|-- archives
|-- docs
|   |-- annonce.txt
|-- projets
    |-- jeu
    |-- site
```

1.  Écrire, **avant** de les taper, les commandes qui créent les répertoires (depuis le répertoire personnel, en entrant dans `club`).

2.  Pour créer un fichier qui contient du texte, on peut **rediriger** l’affichage d’`echo` vers un fichier : `echo ’Reunion jeudi 13h’ > docs/annonce.txt`. Le faire, puis afficher le contenu du fichier.

3.  Vérifier le résultat avec la commande `tree` (qui dessine l’arbre), puis avec `ls -R`.

??? corrige "Corrigé"

    ```console
    |cd|
    |mkdir club|
    |cd club|
    |mkdir archives docs projets|
    |mkdir projets/jeu projets/site|
    |echo 'Reunion jeudi 13h' > docs/annonce.txt|
    |cat docs/annonce.txt|
    Reunion jeudi 13h
    |tree|
    ```

    ```text
    .
    |-- archives
    |-- docs
    |   `-- annonce.txt
    `-- projets
        |-- jeu
        `-- site

    5 directories, 1 file
    ```

    (`tree` dessine l’arbre avec des traits continus ; `ls -R` liste le contenu de chaque répertoire, l’un après l’autre.)

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 10</span> — Un script et le droit `x` <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-tp-1-10 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

1.  Dans `club`, créer un petit programme : `echo ’echo Bonjour le club’ > bonjour.sh`. Afficher ses droits avec `ls -l`.

2.  Le lancer avec `./bonjour.sh`. Quel message obtient-on ? Pourquoi ?

3.  Le lancer avec `sh bonjour.sh`. Cette fois ça marche : quel programme est réellement exécuté, et de quel droit sur `bonjour.sh` a-t-il besoin ?

4.  Rendre le fichier exécutable par son propriétaire, vérifier avec `ls -l` (qu’est-ce qui a changé ?), et relancer `./bonjour.sh`.

??? corrige "Corrigé"

    ```console
    |echo 'echo Bonjour le club' > bonjour.sh|
    |ls -l bonjour.sh|
    -rw-r--r--    1 root     root            21 ...  bonjour.sh
    |./bonjour.sh|
    sh: ./bonjour.sh: Permission denied
    |sh bonjour.sh|
    Bonjour le club
    |chmod u+x bonjour.sh|
    |ls -l bonjour.sh|
    -rwxr--r--    1 root     root            21 ...  bonjour.sh
    |./bonjour.sh|
    Bonjour le club
    ```

    **2.** Le fichier n’a le droit `x` pour personne : le système refuse de l’exécuter, *même pour `root`*. **3.** Avec `sh bonjour.sh`, c’est le programme `sh` (l’interpréteur de commandes) qui est exécuté ; il se contente de **lire** `bonjour.sh`, ce qui ne demande que le droit `r`. **4.** Un `x` est apparu chez le propriétaire.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 11</span> — Copier, déplacer, renommer, supprimer <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-tp-1-11 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Depuis `club`, **prévoir** sur le cahier l’arbre obtenu après la suite d’actions ci-dessous, **puis** écrire et exécuter les commandes, et comparer avec `tree`.

1.  copier `annonce.txt` dans `archives` ;

2.  renommer cette copie en `annonce_sept.txt` ;

3.  déplacer `bonjour.sh` dans `projets/jeu`, puis le lancer depuis `club` sans changer de répertoire ;

4.  supprimer le répertoire `projets/site` et tout son contenu. Pourquoi faut-il être particulièrement prudent avec cette commande ?

??? corrige "Corrigé"

    ```console
    |cp docs/annonce.txt archives/|
    |mv archives/annonce.txt archives/annonce_sept.txt|
    |mv bonjour.sh projets/jeu/|
    |./projets/jeu/bonjour.sh|
    Bonjour le club
    |rm -r projets/site|
    |tree|
    ```

    ```text
    .
    |-- archives
    |   `-- annonce_sept.txt
    |-- docs
    |   `-- annonce.txt
    `-- projets
        `-- jeu
            `-- bonjour.sh

    4 directories, 3 files
    ```

    `rm -r` supprime **définitivement** un répertoire et tout ce qu’il contient, sans corbeille ni confirmation : une faute de frappe sur le nom peut effacer tout un travail.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 12</span> — L’administrateur n’a pas de limites <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-tp-1-12 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Créer `secret.txt` contenant une ligne de texte, puis lui retirer **tous** les droits : `chmod 000 secret.txt`. Vérifier avec `ls -l`, puis essayer `cat secret.txt`. Que constate-t-on ? Expliquer, et en déduire pourquoi le cours conseille de ne pas travailler en permanence avec le compte `root`.

??? corrige "Corrigé"

    ```console
    |echo 'code: 1234' > secret.txt|
    |chmod 000 secret.txt|
    |ls -l secret.txt|
    ----------    1 root     root            11 ...  secret.txt
    |cat secret.txt|
    code: 1234
    ```

    Personne n’a de droit sur le fichier… et pourtant `root` le lit : l’administrateur **ignore les droits de lecture et d’écriture** (seule l’exécution exige au moins un `x`, comme on l’a vu). Une erreur ou un programme malveillant lancé en `root` n’est donc arrêté par **aucune** protection : d’où le conseil de n’utiliser ce compte qu’en cas de besoin.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 13</span> — Mini-scénario : le dossier partagé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-tp-1-13 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Pour voir les droits à l’œuvre, il faut un **deuxième utilisateur**. En tant que `root`, taper :

```console
|adduser -D lea|
|mkdir /tmp/partage|
|cd /tmp/partage|
|echo 'Sortie au musee le 12' > annonce.txt|
|echo 'Lea 15, Tom 12' > notes.txt|
|chmod o-r notes.txt|
|ls -l|
```

(`adduser -D lea` crée un compte `lea` sans mot de passe, possible seulement pour l’administrateur.)

**1. Prévoir, puis vérifier.** Recopier le tableau et le compléter *avant* de passer sur le compte de Léa avec `su lea` (l’invite se termine alors par `$`). Puis taper chaque commande et noter le résultat réel. On revient au compte `root` avec `exit`.

| commande tapée par `lea`, dans `/tmp/partage` | prévision | résultat |
|:---|:--:|:--:|
| `cat annonce.txt` |  |  |
| `cat notes.txt` |  |  |
| `echo ’Lea vient’ >> annonce.txt` *(ajoute une ligne)* |  |  |
| `touch essai.txt` |  |  |
| `cat /root/club/docs/annonce.txt` |  |  |
| `cd ; touch essai.txt` *(dans son répertoire personnel)* |  |  |

**2. Changer les règles.** Revenu en `root`, écrire les commandes `chmod` qui : (a) retirent aux « autres » le droit de lire et de traverser `/root/club` ; (b) permettent aux « autres » de modifier `annonce.txt` ; (c) permettent au groupe et aux autres de lire `notes.txt`. Repasser sur le compte de Léa et refaire les cinq premières lignes du tableau.

**3. L’énigme.** Léa peut maintenant *modifier* `annonce.txt`. Peut-elle le *supprimer* avec `rm` ? Essayer. En regardant les droits du répertoire `/tmp/partage` (`ls -ld /tmp/partage`), proposer une explication.

??? pouce "Coup de pouce"

    Pour un répertoire, `r` permet d’en lister le contenu, `x` d’y entrer ou de le traverser, et `w` d’y créer ou d’y supprimer des fichiers.

??? corrige "Corrigé"

    **1.** Résultats obtenus (`notes.txt` est en `-rw-r-----`, `annonce.txt` en `-rw-r--r--`, `/tmp/partage` en `drwxr-xr-x`, tous à `root`) :

    | commande (`lea`) | résultat |
    |:---|:---|
    | `cat annonce.txt` | `Sortie au musee le 12` : les autres ont `r` |
    | `cat notes.txt` | `cat: can’t open ’notes.txt’: Permission denied` |
    | `echo ’Lea vient’ >> annonce.txt` | `ash: can’t create annonce.txt: Permission denied` (pas de `w`) |
    | `touch essai.txt` | `touch: essai.txt: Permission denied` (pas de `w` sur le répertoire) |
    | `cat /root/club/docs/annonce.txt` | `Reunion jeudi 13h` : `r` sur le fichier, `x` sur les répertoires |
    | `cd ; touch essai.txt` | réussit : `/home/lea` appartient à `lea` |

    **2.**

    ```console
    |chmod o-rx /root/club|
    |chmod o+w /tmp/partage/annonce.txt|
    |chmod go+r /tmp/partage/notes.txt|
    ```

    Pour `lea` ensuite : `annonce.txt` est toujours lisible, et maintenant **modifiable** (la ligne `Lea vient` s’ajoute) ; `notes.txt` devient lisible (`Lea 15, Tom 12`) ; `touch essai.txt` est toujours refusé ; `cat /root/club/docs/annonce.txt` est désormais refusé (`Permission denied`) : sans le droit `x` sur `club`, on ne peut plus *traverser* ce répertoire, même si le fichier lui-même est lisible.

    **3.** `rm /tmp/partage/annonce.txt` donne `rm: can’t remove ’/tmp/partage/annonce.txt’: Permission denied`. Supprimer un fichier, c’est **modifier le répertoire** qui le contient (retirer son nom de la liste) : il faut le droit `w` sur `/tmp/partage`, qui est en `drwxr-xr-x`. Le droit `w` sur le fichier permet d’en changer le *contenu*, pas de le faire disparaître.

## Bilan

### <span class="exo-num">Exercice 14</span> — Ce que j’ai appris <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-tp-1-14 }

1.  Dans le LMC, comment réalise-t-on un `if` ? une boucle `while` ? Citer les instructions utilisées.

2.  Pourquoi le simulateur affiche-t-il des nombres dans la mémoire, et pas des mots comme `ADD` ?

3.  Recopier sur le cahier et compléter le tableau « qui peut faire quoi » à partir de vos expériences :

    | pour… | lire un fichier | modifier un fichier | créer/supprimer dans un répertoire |
    |:---|:--:|:--:|:--:|
    | il faut le droit… |  |  |  |
    | sur… |  |  |  |
    | `root` est-il concerné ? |  |  |  |
