# Exercices

<p class="sous-titre">Architecture des ordinateurs et systèmes d'exploitation</p>

!!! consignes "Mode d’emploi"

    - Niveau : ★ échauffement, ★★ classique (niveau bac), ★★★ défi ; les *coups de pouce* et les *corrigés* se déplient sous chaque exercice.

    - <span class="run" title="À programmer et tester sur machine">▶</span> *À taper et tester* sur un simulateur en ligne (`peterhigginson.co.uk/lmc/`).

    - Rappel du **Little Man Computer** : mémoire de cases `00`–`99`, un accumulateur **ACC**, instructions `INP OUT LDA STA ADD SUB BRA BRZ BRP HLT DAT`.

    - Les commandes Linux sont à essayer dans un **terminal Linux en ligne**, comme JSLinux (`bellard.org/jslinux`), utilisé dans l’activité de découverte.

    - Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la [charte d’usage de l’IA](../charte.md).

Sauf mention contraire, les exercices de ligne de commande utilisent l’**arborescence de référence** suivante, et vous démarrez depuis `/home/eleve`.

```text
/
|-- home/
|   |-- eleve/               « ~  = repertoire de depart »
|       |-- Documents/
|       |   |-- cours_nsi.txt
|       |   |-- tp_os.txt
|       |-- Images/
|       |   |-- logo.png
|       |-- Projets/         « vide au depart »
|       |-- notes.txt
|-- etc/
    |-- hosts
```

### Architecture matérielle et modèle de von Neumann

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — Chaque chose à sa place <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-09-1 }

Associer chaque composant à son rôle.

|  |  |
|:---|:---|
| \(1\) unité de commande | \(a\) fait les calculs (additions, comparaisons…) |
| \(2\) UAL | \(b\) range programme et données dans des cases adressées |
| \(3\) mémoire | \(c\) lit, décode et ordonne l’exécution des instructions |
| \(4\) entrées-sorties | \(d\) font communiquer la machine avec le monde extérieur |

??? corrige "Corrigé"

    !!! remarque "Remarque"

        On donne **une** version simple ; d’autres écritures sont possibles (surtout pour les programmes LMC).

    (1)–(c), \; (2)–(a), \; (3)–(b), \; (4)–(d).

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 2</span> — Vrai ou faux <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-09-2 }

Pour chaque affirmation, répondre par vrai ou faux et **justifier** en une phrase.

1.  Le processeur (CPU) contient l’unité de commande et l’UAL.

2.  La mémoire vive (RAM) conserve les données même quand l’ordinateur est éteint.

3.  Dans le modèle de von Neumann, le programme est rangé dans la mémoire, comme les données.

4.  Un registre est plus grand mais plus lent que le disque dur.

??? corrige "Corrigé"

    **a) Vrai** : le processeur (CPU) réunit l’unité de commande, l’UAL et les registres. **b) Faux** : la RAM est *volatile*, elle s’efface à l’extinction ; c’est le **disque** qui conserve. **c) Vrai** : c’est l’idée centrale de von Neumann, programme et données dans la même mémoire. **d) Faux** : un registre est bien plus *petit* mais bien plus *rapide* que le disque.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 3</span> — Ordres de grandeur <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-09-3 }

Recopier chaque grandeur en la reliant à l’ordre de grandeur qui convient : \; *quelques nanomètres* \;/\; *quelques milliards* \;/\; *quelques gigahertz*.

1.  taille d’un transistor gravé aujourd’hui ;

2.  nombre de transistors dans un processeur moderne ;

3.  fréquence (nombre de cycles par seconde) d’un processeur.

??? corrige "Corrigé"

    a\) quelques **nanomètres** ; \; b) quelques **milliards** ; \; c) quelques **gigahertz**.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 4</span> — La loi de Moore <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-4 }

L’Intel 4004 (1971) comptait environ **2 300** transistors. La loi de Moore affirme que ce nombre **double tous les deux ans**.

1.  Combien de transistors, environ, la loi prévoit-elle après 10 ans (soit 5 doublements) ?

2.  La loi de Moore est-elle une loi de la physique ? Pourquoi finit-elle par ralentir ?

    ??? pouce "Coup de pouce"

        a\) Doubler 5 fois, c’est multiplier par $2 \times 2 \times 2 \times 2 \times 2$. b) Comparer la taille d’un transistor actuel à celle d’un atome.

??? corrige "Corrigé"

    **a)** 5 doublements multiplient par $2^5 = 32$ : environ $2\,300 \times 32 \approx \textbf{73\,600}$ transistors. **b)** Ce n’est **pas** une loi de la physique, mais une **observation** (une tendance) qui a longtemps guidé l’industrie. Elle ralentit car on approche de la **taille de l’atome** : un transistor de quelques atomes ne peut plus vraiment être réduit (effets physiques parasites, chaleur).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 5</span> — RAM ou disque ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-5 }

On enregistre un document puis on éteint brutalement l’ordinateur (coupure de courant).

1.  Le travail *enregistré* est-il perdu ? Où se trouve-t-il ?

2.  Le travail *non enregistré* est-il perdu ? Dans quelle mémoire se trouvait-il ?

3.  Expliquer, avec les mots « volatile » et « permanent », ce que fait le bouton « Enregistrer ».

    ??? pouce "Coup de pouce"

        Pour chaque mémoire (RAM, disque), se demander ce qu’elle devient quand le courant est coupé.

??? corrige "Corrigé"

    **a)** Le travail enregistré n’est **pas** perdu : il est sur le **disque** (mémoire permanente). **b)** Le travail non enregistré est **perdu** : il était en **RAM** (mémoire volatile). **c)** « Enregistrer », c’est **recopier** les données de la RAM (*volatile*) vers le disque (*permanent*).

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 6</span> — Capteur ou actionneur ? <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-09-6 }

Pour chaque élément, dire s’il s’agit d’un **capteur** (entrée : il *mesure*) ou d’un **actionneur** (sortie : il *agit*) : *a)* un thermomètre ; *b)* un moteur de volet roulant ; *c)* un micro ; *d)* une LED ; *e)* l’écran tactile (les deux ? préciser) ; *f)* un haut-parleur.

Puis décrire, pour un **arrosage automatique de plante**, la boucle *capter $\to$ décider $\to$ agir* en nommant le capteur et l’actionneur.

??? corrige "Corrigé"

    **a)** capteur (mesure la température) ; **b)** actionneur (agit : ouvre/ferme) ; **c)** capteur (mesure le son) ; **d)** actionneur (émet de la lumière) ; **e)** l’écran tactile est **les deux** : la dalle tactile est un *capteur* (mesure le doigt), l’affichage est un *actionneur* (sortie visuelle) ; **f)** actionneur (émet du son).

    **Arrosage automatique :** un **capteur** d’humidité du sol mesure l’humidité (*capter*) ; le programme la compare à un seuil (*décider*) ; si le sol est trop sec, il commande la **pompe** ou l’électrovanne (**actionneur**) pour arroser (*agir*).

### Le processeur au travail : langage machine (LMC)

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Dérouler pas à pas <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-09-7 }

On donne le programme LMC suivant.

```console
00   INP
01   STA 08
02   ADD 08
03   ADD 08
04   OUT
05   HLT
08       DAT
```

1.  Dérouler l’exécution pour l’entrée **4**, en remplissant un tableau à colonnes `Adresse`, `Instruction`, `ACC`, `case 08`.

2.  Quelle valeur est affichée par `OUT` ?

3.  En une phrase : que calcule ce programme à partir du nombre lu ?

    ??? pouce "Coup de pouce"

        Une ligne du tableau par instruction exécutée. `ADD 08` ajoute à ACC le contenu de la case 08, sans modifier cette case.

??? corrige "Corrigé"

    **a)** Déroulé pour l’entrée 4 :

    | **Adr.** | **Instr.** | **ACC** | `case 08` |
    |:--------:|:----------:|:-------:|:---------:|
    |    00    |    INP     |    4    |     –     |
    |    01    |   STA 08   |    4    |     4     |
    |    02    |   ADD 08   |    8    |     4     |
    |    03    |   ADD 08   |   12    |     4     |
    |    04    |    OUT     |   12    |     4     |

    **b)** La sortie est **12**. \; **c)** Le programme affiche le **triple** du nombre lu ($3\times 4 = 12$), obtenu par deux additions successives.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Le plus grand des deux <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-09-8 }

On donne ce programme (les cases `11` et `12` sont nommées `a` et `b`).

```console
00   INP
01   STA a
02   INP
03   STA b
04   SUB a       « ACC <- b - a »
05   BRP 08      « si ACC >= 0, aller en 08 »
06   LDA a
07   BRA 09
08   LDA b
09   OUT
10   HLT
11   a  DAT
12   b  DAT
```

1.  Dérouler pour les entrées **7** puis **2**. Quelle est la sortie ?

2.  Dérouler pour les entrées **3** puis **8**. Quelle est la sortie ?

3.  Que calcule ce programme ? À quoi sert l’instruction `BRP` ?

    ??? pouce "Coup de pouce"

        Calculer ACC juste après `SUB a` : c’est son signe qui décide si l’on saute en 08 ou non.

??? corrige "Corrigé"

    **a)** Entrées 7 puis 2 : `a`$=7$, `b`$=2$ ; en 04 `SUB a` donne ACC $=2-7=-5<0$, donc `BRP` ne saute pas ; on charge `a` et on affiche **7**. **b)** Entrées 3 puis 8 : `a`$=3$, `b`$=8$ ; en 04 ACC $=8-3=5\geq 0$, donc `BRP` saute en 08, on charge `b` et on affiche **8**. **c)** Le programme affiche le **plus grand** des deux nombres. `BRP` réalise le **test** : selon le signe de $b-a$, on choisit d’afficher $a$ ou $b$.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 9</span> — <span class="run" title="À programmer et tester sur machine">▶</span>  À vous d’écrire <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-9 }

Écrire un programme LMC qui lit **trois** nombres et affiche leur **somme**. Le tester sur le simulateur avec les entrées 10, 20, 30 (on doit lire 60).

??? pouce "Coup de pouce"

    Il n’y a qu’un accumulateur : chaque nombre lu doit être rangé dans une case (réservée par `DAT`) avant d’en lire un autre.

??? corrige "Corrigé"

    Une solution (les cases 10 et 11 stockent les deux premiers nombres) :

    ```console
    00   INP
    01   STA 10
    02   INP
    03   STA 11
    04   INP
    05   ADD 10
    06   ADD 11
    07   OUT
    08   HLT
    10       DAT
    11       DAT
    ```

    Pour 10, 20, 30 : le troisième nombre (30) est dans ACC, on ajoute les cases 10 et 11 ($+10$ puis $+20$) : sortie $=60$.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 10</span> — <span class="run" title="À programmer et tester sur machine">▶</span>  Le plus petit <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-10 }

En s’inspirant du programme « le plus grand des deux », écrire un programme LMC qui lit deux nombres et affiche le **plus petit**. Le tester (entrées 7 et 2 $\to$ 2 ; entrées 3 et 8 $\to$ 3).

??? pouce "Coup de pouce"

    Dans « le plus grand des deux », repérer quelle case est chargée quand ACC $\geqslant 0$ et quelle case l’est sinon : que faut-il changer ?

??? pouce "Coup de pouce 2 (début de solution)"

    Le début ne change pas :  
    `00 INP`  
    `01 STA a`  
    `02 INP`  
    `03 STA b`  
    `04 SUB a` (ACC $\geqslant 0$ signifie $b \geqslant a$).

??? corrige "Corrigé"

    On garde la même structure, mais on échange les deux chargements :

    ```console
    00   INP
    01   STA a
    02   INP
    03   STA b
    04   SUB a       « ACC <- b - a »
    05   BRP 08      « si b >= a, le plus petit est a »
    06   LDA b       « sinon b < a : le plus petit est b »
    07   BRA 09
    08   LDA a
    09   OUT
    10   HLT
    11   a  DAT
    12   b  DAT
    ```

    Entrées 7 et 2 : $b-a=-5<0 \to$ on affiche `b`$=2$. Entrées 3 et 8 : $b-a=5\geq0 \to$ on affiche `a`$=3$.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 11</span> — <span class="run" title="À programmer et tester sur machine">▶</span>  Une boucle : la somme des entiers <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-11 }

On donne ce programme utilisant des **étiquettes** (le simulateur les accepte).

```console
       INP
       STA n
       LDA zero
       STA somme
       LDA n
       STA i
boucle LDA i
       BRZ fin       « si i = 0, on sort »
       LDA somme
       ADD i
       STA somme     « somme <- somme + i »
       LDA i
       SUB un
       STA i         « i <- i - 1 »
       BRA boucle
fin    LDA somme
       OUT
       HLT
zero   DAT 0
un     DAT 1
n      DAT
i      DAT
somme  DAT
```

1.  Dérouler pour l’entrée **3** en suivant `i` et `somme` à chaque passage de `boucle`. Quelle est la sortie ?

2.  Que calcule ce programme en fonction de l’entrée $n$ ?

3.  Quel rôle jouent `BRZ` et `BRA` pour réaliser la boucle ?

    ??? pouce "Coup de pouce"

        Faire un tableau à deux colonnes `i` et `somme`, avec une ligne à chaque passage par l’étiquette `boucle`.

    ??? pouce "Coup de pouce 2 (début de solution)"

        Au premier passage par `boucle` : `i` vaut 3 et `somme` vaut 0. Après le corps de la boucle, `somme` vaut 3 et `i` vaut 2, puis `BRA` renvoie à `boucle`.

??? corrige "Corrigé"

    **a)** Déroulé pour $n=3$, à chaque passage sur `boucle` :

    | **passage** | `i` (avant) |   `somme` (après)    |
    |:-----------:|:-----------:|:--------------------:|
    |      1      |      3      |       0+3 = 3        |
    |      2      |      2      |       3+2 = 5        |
    |      3      |      1      |       5+1 = 6        |
    |      4      |      0      | (`BRZ` $\to$ sortie) |

    La sortie est **6**. **b)** Le programme calcule $1+2+\dots+n$ (la somme des entiers de 1 à $n$). **c)** `BRZ` *teste* la condition d’arrêt (sortir quand `i`$=0$) ; `BRA` *retourne* sans condition au début de la boucle. Ensemble, ils réalisent la répétition.

### Le système d’exploitation

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 12</span> — À quoi sert l’OS ? <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-09-12 }

Pour chacune des situations, indiquer **quelle grande fonction** du système d’exploitation est en jeu (gérer le processeur / la mémoire / les fichiers / les périphériques / les utilisateurs).

1.  deux applications semblent s’exécuter « en même temps » ;

2.  on branche une imprimante et elle fonctionne sans rien réinstaller ;

3.  un fichier de Léa n’est pas accessible au compte de Tom ;

4.  chaque programme dispose de sa part de RAM sans écraser les autres ;

5.  on retrouve ses documents rangés en dossiers.

??? corrige "Corrigé"

    a\) gérer le **processeur** ; b) gérer les **périphériques** ; c) gérer les **utilisateurs** (droits) ; d) gérer la **mémoire** ; e) gérer les **fichiers**.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 13</span> — Familles de systèmes <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-09-13 }

Répondre brièvement.

1.  Citer trois grandes familles de systèmes d’exploitation.

2.  Sur quel noyau le système Android des smartphones est-il bâti ?

3.  « Un logiciel libre est forcément gratuit. » Vrai ou faux ? Expliquer.

??? corrige "Corrigé"

    a\) **Windows**, **macOS**, **Linux** (UNIX). \; b) Android est bâti sur un **noyau Linux**. \; c) **Faux** : « libre » désigne la liberté d’étudier, modifier et partager le code ; ce n’est pas synonyme de gratuit (confusion avec l’anglais *free*).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 14</span> — L’abstraction <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-14 }

Quand une application veut « ouvrir un fichier », elle ne s’adresse pas directement au disque dur : elle passe par le système d’exploitation. En reliant cela au **mille-feuille de couches** du cours, expliquer en quelques lignes l’intérêt de cette *abstraction* (penser à ce qui se passerait si chaque application devait connaître le modèle exact du disque).

??? pouce "Coup de pouce"

    Imaginer qu’on remplace le disque dur par un modèle d’une autre marque : qui faut-il modifier, chaque application ou seulement l’OS ?

??? corrige "Corrigé"

    Le système d’exploitation offre des actions **simples et universelles** (« ouvrir un fichier ») et **cache** le fonctionnement réel du disque. Si chaque application devait connaître le modèle exact du matériel, il faudrait la **réécrire** pour chaque disque, chaque imprimante… : ingérable. Grâce à cette couche d’abstraction, les applications restent simples et **portables** : c’est tout l’intérêt du mille-feuille, où chaque couche ne parle qu’à celle juste en dessous.

### Ligne de commande Linux

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 15</span> — Se repérer <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-09-15 }

En utilisant l’arborescence de référence :

1.  Quelle commande affiche le répertoire courant ?

2.  Donner le **chemin absolu** du fichier `logo.png`.

3.  Vous êtes dans `/home/eleve/Documents`. Donner le chemin **relatif** pour atteindre `logo.png`.

??? corrige "Corrigé"

    a\) `pwd`. \; b) `/home/eleve/Images/logo.png`. \; c) `../Images/logo.png`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 16</span> — Naviguer <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-09-16 }

Vous démarrez dans `/home/eleve`. Écrire la commande demandée (chemin relatif sauf mention contraire).

1.  se déplacer dans `Documents` ;

2.  depuis `Documents`, revenir dans `/home/eleve` *sans taper le chemin complet* ;

3.  aller directement dans `/etc` en **chemin absolu** ;

4.  lister le contenu de `Images` *sans s’y déplacer*.

    ??? pouce "Coup de pouce"

        Revoir les raccourcis `.` et `..`, et la différence entre un chemin qui commence par `/` et un chemin qui n’en commence pas.

??? corrige "Corrigé"

    a\) `cd Documents` \; b) `cd ..` \; c) `cd /etc` \; d) `ls Images`

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 17</span> — Créer, copier, déplacer <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-17 }

Depuis `/home/eleve`, écrire les commandes pour :

1.  créer un répertoire `Rendus` dans `Projets` ;

2.  créer un fichier vide `brouillon.txt` dans `Projets/Rendus` ;

3.  afficher le contenu de `Documents/cours_nsi.txt` ;

4.  copier `tp_os.txt` de `Documents` vers `Projets/Rendus`, puis renommer la copie en `tp_final.txt` ;

5.  déplacer `notes.txt` de `/home/eleve` vers `Documents`.

    ??? pouce "Coup de pouce"

        On reste dans `/home/eleve` : chaque commande peut viser un fichier plus bas dans l’arbre avec un chemin relatif comme `Projets/Rendus`. Revoir le tableau des commandes du cours.

??? corrige "Corrigé"

    ```console
    |mkdir| Projets/Rendus
    |touch| Projets/Rendus/brouillon.txt
    |cat| Documents/cours_nsi.txt
    |cp| Documents/tp_os.txt Projets/Rendus/
    |mv| Projets/Rendus/tp_os.txt Projets/Rendus/tp_final.txt
    |mv| notes.txt Documents/
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 18</span> — Corriger les erreurs <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-18 }

Chaque commande contient une erreur. L’identifier et proposer la correction.

1.  `cd /home/eleve/Documents/cours_nsi.txt` (on veut aller *dans* `Documents`) ;

2.  `rm -r notes.txt` (on veut supprimer ce simple fichier) ;

3.  vous êtes dans `/home/eleve/Images` et tapez `cat cours_nsi.txt` (le fichier est dans `Documents`).

    ??? pouce "Coup de pouce"

        Pour chaque commande, se demander : le dernier mot désigne-t-il un fichier ou un répertoire ? Et depuis quel répertoire la commande est-elle lancée ?

??? corrige "Corrigé"

    **a)** `cd` attend un **répertoire**, pas un fichier : `cd /home/eleve/Documents`. **b)** `-r` sert aux *répertoires* ; pour un simple fichier : `rm notes.txt`. **c)** Le fichier est dans `Documents`, pas dans le répertoire courant : `cat ../Documents/cours_nsi.txt`.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 19</span> — Reconstituer une séquence <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-19 }

Remettre ces commandes dans le bon ordre pour : créer un dossier `TP`, y créer un fichier `index.txt`, puis afficher son contenu.

`A. cat TP/index.txt` `B. mkdir TP` `C. touch TP/index.txt`

??? corrige "Corrigé"

    Ordre : **B** $\to$ **C** $\to$ **A** (créer le dossier, y créer le fichier, puis l’afficher).

### Droits et permissions

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 20</span> — Lire les droits <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-09-20 }

La commande `ls -l` affiche :

```console
-rwxr-xr--  1 eleve  nsi   240  8 sep 10:02 script.sh
drwxr-x---  2 eleve  nsi  4096  8 sep 10:05 secret
```

1.  Pour `script.sh` : s’agit-il d’un fichier ou d’un répertoire ? Quels droits a le **propriétaire** ? le **groupe** ? les **autres** ?

2.  Un membre du groupe `nsi` peut-il *exécuter* `script.sh` ? Le *modifier* ?

3.  Que signifie le `d` au début de la ligne de `secret` ? Les « autres » peuvent-ils entrer dans ce répertoire ?

    ??? pouce "Coup de pouce"

        Découper la chaîne : un caractère pour le type, puis trois blocs de trois caractères, dans l’ordre propriétaire, groupe, autres.

??? corrige "Corrigé"

    **a)** `script.sh` est un **fichier** (premier caractère `-`). Propriétaire : `rwx` (lecture, écriture, exécution) ; groupe : `r-x` (lecture, exécution, *pas* d’écriture) ; autres : `r--` (lecture seule). **b)** Un membre du groupe `nsi` **peut l’exécuter** (`x` présent) mais **ne peut pas le modifier** (pas de `w`). **c)** Le `d` indique un **répertoire**. Les « autres » ont `---` : ils **ne peuvent pas** y entrer (pas de droit `x`).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 21</span> — Modifier les droits <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-21 }

Écrire la commande `chmod` correspondante.

1.  retirer aux « autres » le droit de lecture sur `cours_nsi.txt` ;

2.  ajouter au « groupe » le droit d’écriture sur `cours_nsi.txt` ;

3.  rendre `script.sh` exécutable par son propriétaire ;

4.  donner à tout le monde le droit de lecture sur `logo.png`.

    ??? pouce "Coup de pouce"

        Une commande `chmod` se lit : *pour qui* (`u`, `g`, `o` ou `a`), *ajouter ou retirer* (`+` ou `-`), *quel droit* (`r`, `w`, `x`), puis le fichier.

??? corrige "Corrigé"

    a\) `chmod o-r cours_nsi.txt` \; b) `chmod g+w cours_nsi.txt` \; c) `chmod u+x script.sh` \; d) `chmod a+r logo.png`

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 22</span> — Le compte `root` <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-22 }

1.  Qui est l’utilisateur `root` et que peut-il faire de plus que les autres ?

2.  Pourquoi est-il déconseillé de travailler en permanence en tant que `root` ?

3.  En quoi les droits d’accès participent-ils à la **sécurité** d’une machine partagée ?

    ??? pouce "Coup de pouce"

        Imaginer la même faute de frappe dans une commande `rm -r`, tapée par un utilisateur ordinaire puis par `root` : quels fichiers peuvent être effacés dans chaque cas ?

??? corrige "Corrigé"

    **a)** `root` est l’**administrateur** (super-utilisateur) : il a **tous** les droits sur tous les fichiers et peut modifier les droits et les comptes. **b)** Une fausse manipulation ou un logiciel malveillant lancé en `root` peut **tout détruire**, sans garde-fou ; en compte normal, les droits **limitent** les dégâts. **c)** Les droits empêchent un utilisateur de lire ou modifier les fichiers des autres, et restreignent ce qu’un programme peut faire : ils assurent **confidentialité** et **protection** sur une machine partagée.

### Mini-problème de synthèse

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 23</span> — Du transistor au fichier <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-23 }

Léo, sur son environnement Linux, écrit un petit programme, l’enregistre, puis le rend exécutable.

1.  Léo tape le code dans un éditeur : dans quelle mémoire se trouve son texte tant qu’il n’a pas enregistré ? Que risque une coupure de courant ?

2.  Il enregistre dans `/home/leo/Projets/jeu.py`. Donner la commande qui, depuis `/home/leo`, affiche le contenu de ce fichier avec un **chemin relatif**.

3.  Il rend le fichier exécutable par lui seul. Écrire la commande `chmod`.

4.  Quand il lance son programme Python, celui-ci n’est pas exécuté tel quel par le processeur. Expliquer, avec les mots *traduction*, *langage machine* et *cycle chercher-décoder-exécuter*, ce qui se passe « en dessous ».

??? pouce "Coup de pouce"

    Chaque question reprend une partie du cours : a) les mémoires, b) les chemins relatifs, c) `chmod`, d) le cycle du processeur.

??? pouce "Coup de pouce 2 (début de solution)"

    a\) Avant l’enregistrement, le texte n’existe qu’en mémoire vive. b) Le chemin relatif part de `/home/leo` : il ne commence donc pas par `/`. d) Python est d’abord traduit ; le processeur répète ensuite son cycle sur des instructions…

??? corrige "Corrigé"

    **a)** Tant qu’il n’a pas enregistré, le texte est en **RAM** (mémoire volatile) : une coupure de courant le **perd**. **b)** `cat Projets/jeu.py` (chemin relatif depuis `/home/leo`). **c)** `chmod u+x Projets/jeu.py` (pour n’autoriser que lui, on peut aussi tout réinitialiser avec `chmod 700 Projets/jeu.py` <span class="horsprog">au-delà du programme</span>). **d)** Le processeur ne comprend que le **langage machine**. Le code Python est donc d’abord **traduit** par l’interpréteur Python (en simplifiant : il le traduit en un code intermédiaire, qu’il exécute ensuite instruction par instruction) ; tout en bas, ce sont des instructions en langage machine que le processeur exécute une à une, en répétant le **cycle chercher-décoder-exécuter**. Le programme « lisible » du haut du mille-feuille finit toujours en instructions élémentaires tout en bas.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 24</span> — Le modèle de von Neumann selon un assistant d’IA <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> { #ex-09-24 }

Un élève demande à un assistant d’IA : « Explique-moi le modèle de von Neumann. » Voici la réponse obtenue.

« Le modèle de von Neumann, proposé en 1945, décrit l’organisation de presque tous les ordinateurs actuels. Il comporte quatre unités : l’unité de commande, qui lit et décode les instructions ; l’unité arithmétique et logique (UAL), qui effectue les calculs ; la mémoire, faite de cases numérotées par une adresse ; et les dispositifs d’entrée-sortie, qui font le lien avec l’extérieur (clavier, écran, disque). L’unité de commande et l’UAL, avec quelques registres très rapides, forment le processeur, relié aux autres organes par des bus. Le processeur répète sans cesse le cycle chercher-décoder-exécuter. Le point essentiel du modèle est que les instructions du programme sont rangées dans une mémoire séparée de celle des données, ce qui évite que le processeur confonde une instruction et une donnée. »

1.  La réponse est-elle correcte ? Confronter chaque phrase au cours.

2.  Localiser et corriger l’erreur.

3.  Quelle vérification simple, faite avant de faire confiance à la réponse, aurait suffi à détecter l’erreur ?

    ??? pouce "Coup de pouce"

        Relire l’idée clé du modèle dans le cours : où sont rangés les instructions du programme et les données ?

??? corrige "Corrigé"

    **a)** Non. Les quatre unités, le processeur, les registres, les bus et le cycle chercher-décoder-exécuter sont conformes au cours ; la dernière phrase le contredit frontalement. Le cours dit : « dans le modèle de von Neumann, le **programme est rangé dans la même mémoire que les données**, sous forme de nombres ». **b)** L’erreur est « une mémoire séparée de celle des données ». Correction : instructions et données partagent **la même mémoire**, dans des cases adressées de la même façon ; c’est même l’idée centrale du modèle (« le programme est une donnée »), celle qui rend la machine **universelle** : changer de programme, c’est changer des nombres en mémoire. On le voit dans le LMC, où une instruction et une donnée occupent le même genre de case. **c)** Relire la définition du cours (ou le schéma des quatre unités, où une seule boîte « MÉMOIRE » contient « programme + données »). Quand une réponse présente un « point essentiel », c’est celui-là qu’il faut vérifier en premier.
