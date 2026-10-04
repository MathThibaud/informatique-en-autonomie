# Activités préparatoires

<p class="sous-titre">Le Web : réseaux et interactions homme-machine</p>

## <span class="etiquette">Activité 1</span> Le réseau qui perd des papiers

*un jeu de rôle pour ne perdre aucun message*

<p class="infos-activite">Durée : 30 min · Par groupes de trois, sans machine</p>

!!! consignes "Consignes"

    - Matériel : une vingtaine de petits papiers, un crayon chacun ; les réponses se notent sur le cahier.

    - Trois rôles. L’**émetteur** doit transmettre le mot **`BALLON`**, **une lettre par papier**. Le **récepteur**, assis dos à l’émetteur, écrit les lettres reçues dans l’ordre d’arrivée. Le **réseau** porte les papiers de l’un à l’autre, sans parler.

    - Le réseau suit en secret sa **feuille de route** (encadré en fin d’énoncé, que **seul** le joueur « réseau » consulte) : elle lui dit quels papiers **perdre** (il les garde dans sa poche). Sur Internet aussi, des paquets se perdent (câble saturé, routeur en panne).

    - Interdit de parler ou de se retourner : on ne communique **que par papiers**. On change de rôles à chaque manche.

### <span class="exo-num">Exercice 1</span> — Manche 1 : on envoie, c’est tout <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-act-1-1 }

L’émetteur envoie les six lettres, une par une, sans attendre.

1.  Quel mot le récepteur a-t-il écrit ?

2.  Le récepteur peut-il savoir qu’il lui manque une lettre ? L’émetteur, lui, sait-il que sa lettre n’est pas arrivée ?

3.  Proposer une règle (une seule phrase) pour que l’émetteur **sache** si chaque papier est bien arrivé.

??? corrige "Corrigé"

    **1.** `BALON` (le premier `L` est perdu).  
    **2.** Non : `BALON` ressemble à un mot plausible, rien ne signale le trou. L’émetteur non plus ne sait rien : il n’a aucun retour.  
    **3.** « Le récepteur renvoie un papier pour dire qu’il a bien reçu » (ou : « on attend la réponse avant d’envoyer la suite »). C’est exactement la règle de la manche 2.

### <span class="exo-num">Exercice 2</span> — Manche 2 : on répond « reçu » <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-act-1-2 }

Nouvelle règle : à chaque lettre reçue, le récepteur renvoie un papier « **reçu** ». L’émetteur n’envoie la lettre suivante qu’après avoir reçu ce papier. S’il n’a rien reçu au bout de **10 secondes** (compter dans sa tête), il **renvoie** la même lettre.

1.  Quel mot le récepteur a-t-il écrit ?

2.  Que s’est-il passé ? (Ouvrir la feuille de route du réseau seulement maintenant.)

3.  Le récepteur a-t-il pu deviner, au moment où il l’a reçu, que l’un des papiers était un **renvoi** et non une nouvelle lettre ? Pourquoi le mot `BALLON` rend-il la chose impossible ?

4.  Une lettre perdue est désormais renvoyée. Mais quel nouveau problème le papier « reçu » a-t-il fait apparaître ?

??? corrige "Corrigé"

    **4.** `BALLLON` (trois `L`).  
    **5.** Le premier `L` est bien arrivé, mais son papier « reçu » a été perdu. Faute de réponse au bout de 10 secondes, l’émetteur a **renvoyé** ce `L`, que le récepteur a recopié une deuxième fois ; puis l’émetteur a envoyé le vrai deuxième `L`.  
    **6.** Non : un papier `L` ressemble à un autre papier `L`. Comme `BALLON` contient *vraiment* deux `L` de suite, recevoir deux `L` d’affilée n’a rien d’anormal : impossible de savoir, au moment de la réception, si c’est un renvoi ou la lettre suivante.  
    **7.** Les lettres perdues sont réparées, mais un papier « reçu » perdu provoque un **doublon** : le récepteur reçoit deux fois la même donnée sans pouvoir la reconnaître.

### <span class="exo-num">Exercice 3</span> — Manche 3 : on numérote, mais avec un seul chiffre <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-act-1-3 }

Pour reconnaître un renvoi, on écrit un **numéro** sur chaque papier. Premier réflexe : 1, 2, 3, 4… Mais sur un vrai réseau, chaque chiffre écrit sur un paquet prend de la place. On essaie donc avec **un seul chiffre**, `0` ou `1`.

Règles : les lettres sont marquées tour à tour `0`, `1`, `0`, `1`… ; un renvoi garde **le même** chiffre. Le récepteur note à chaque fois le chiffre qu’il **attend** (au début : `0`). S’il reçoit un papier portant le chiffre qu’il vient **déjà** de recevoir, il ne recopie pas la lettre, mais renvoie quand même « reçu ».

1.  Recopier sur le cahier et compléter le tableau des papiers envoyés par l’émetteur pendant la manche (une case par envoi, renvois compris) :

    | lettre  | `B` |     |     |     |     |     |     |     |     |
    |:--------|:----|:----|:----|:----|:----|:----|:----|:----|:----|
    | chiffre | `0` |     |     |     |     |     |     |     |     |

2.  Quel mot le récepteur a-t-il écrit ? Est-il correct ?

3.  Pourquoi le récepteur doit-il renvoyer « reçu » même pour un papier qu’il jette ? (Penser à ce que ferait l’émetteur sinon.)

4.  Pourquoi un seul chiffre suffit-il ? (Combien de papiers différents l’émetteur peut-il avoir « en route » à un instant donné ?)

??? corrige "Corrigé"

    **8.** Avec la feuille de route (2<sup>e</sup> papier de lettre perdu, 4<sup>e</sup> « reçu » perdu), l’émetteur fait **8 envois** :

    | lettre        | `B`  |   `A`   | `A`  | `L`  |   `L`    |      `L`       | `O`  | `N`  |
    |:--------------|:----:|:-------:|:----:|:----:|:--------:|:--------------:|:----:|:----:|
    | chiffre       | `0`  |   `1`   | `1`  | `0`  |   `1`    |      `1`       | `0`  | `1`  |
    | ce qui arrive | reçu | *perdu* | reçu | reçu | reçu (1) | *doublon jeté* | reçu | reçu |

    (1) la lettre arrive, mais c’est son « reçu » qui est perdu.

    Le 3<sup>e</sup> envoi est le renvoi du `A` perdu ; le 6<sup>e</sup> est le renvoi du second `L` (son « reçu » s’est perdu) : le récepteur attendait `0`, il reçoit `1`, déjà traité, donc il le jette.  
    **9.** `BALLON` : correct.  
    **10.** Si le récepteur jetait le doublon sans répondre, l’émetteur, toujours sans « reçu », renverrait encore et encore le même papier : la transmission serait bloquée. Le « reçu » du doublon remplace celui qui s’est perdu.  
    **11.** L’émetteur attend le « reçu » avant d’envoyer la suite : il n’y a jamais qu’**une** lettre en route. Le récepteur doit seulement distinguer « la même que la précédente » de « la suivante » : deux cas, donc un seul chiffre `0`/`1` (un **bit**) suffit.

### <span class="exo-num">Exercice 4</span> — Mettre des mots <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-act-1-4 }

1.  Recopier sur le cahier en complétant les trous **(a)** à **(d)** : « Pour être sûr qu’un paquet est arrivé, le récepteur renvoie un … **(a)**. Sans réponse au bout d’un certain … **(b)**, l’émetteur … **(c)** le même paquet. Pour ne pas confondre un renvoi avec un nouveau paquet, on marque chaque paquet d’un … **(d)** qui vaut alternativement `0` et `1`. »

2.  Comment appelle-t-on un ensemble de règles que tous les participants doivent respecter pour communiquer ?

!!! encadre "Feuille de route du réseau — réservée au joueur « réseau »"

    - **Manche 1** : perdre le **3<sup>e</sup>** papier confié (la première lettre `L`).

    - **Manche 2** : transmettre toutes les lettres, mais perdre le **3<sup>e</sup>** papier « reçu » (celui de la première lettre `L`).

    - **Manche 3** : perdre le **2<sup>e</sup>** papier de lettre (le premier `A`) et le **4<sup>e</sup>** papier « reçu » transporté.

??? corrige "Corrigé"

    **12.** « …le récepteur renvoie un **accusé de réception**. Sans réponse au bout d’un certain **délai**, l’émetteur **renvoie** le même paquet. Pour ne pas confondre un renvoi avec un nouveau paquet, on marque chaque paquet d’un **bit** qui vaut alternativement `0` et `1`. »  
    **13.** Un **protocole**.
