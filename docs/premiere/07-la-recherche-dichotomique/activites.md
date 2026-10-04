# Activités préparatoires

<p class="sous-titre">La recherche dichotomique</p>

## <span class="etiquette">Activité 1</span> Le nombre mystère

*trouver un nombre en un minimum de coups*

<p class="infos-activite">Durée : 20 min · Par binômes, sans machine, réponses sur le cahier</p>

!!! consignes "Consignes"

    - Une feuille de brouillon pour le maître du jeu.

    - Le **maître du jeu** choisit un nombre secret et l’écrit, caché, sur son brouillon. Le **joueur** fait des propositions ; à chaque proposition, le maître du jeu répond seulement **« plus grand »**, **« plus petit »** ou **« gagné »**.

    - On compte les **coups** : chaque proposition compte pour un coup, y compris la dernière.

### <span class="exo-num">Exercice 1</span> — Entre 1 et 100 <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-07-la-recherche-dichotomique-act-1-1 }

1.  Jouer quatre parties avec un secret entre 1 et 100, en échangeant les rôles à chaque partie. Noter sur le cahier, pour chaque partie, le nombre secret et le nombre de coups.

2.  Décrire en une ou deux phrases la stratégie du joueur qui a utilisé le moins de coups.

??? corrige "Corrigé"

    **1.** Réponses variables, typiquement entre 4 et 12 coups ; un joueur chanceux peut gagner en 1 coup. Ceux qui proposent 1, 2, 3… peuvent aller jusqu’à 100 coups.  
    **2.** La stratégie gagnante qui émerge presque toujours : « proposer le milieu, puis le milieu de ce qui reste ».

### <span class="exo-num">Exercice 2</span> — La meilleure stratégie <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-07-la-recherche-dichotomique-act-1-2 }

1.  Quelle est la meilleure **première** proposition ? Pourquoi ?

2.  Avec cette première proposition, combien de nombres possibles reste-t-il, au pire, après la réponse ?

3.  En continuant ainsi, écrire la suite du nombre de possibilités restantes, au pire : $100 \to 50 \to \ldots$ jusqu’à $1$. Combien de coups faut-il donc, au pire, pour être sûr de gagner ?

4.  **Le maître du jeu malin.** Nouvelle règle : le maître du jeu n’écrit plus son secret. Il répond à chaque fois de façon à faire durer la partie le plus longtemps possible, mais sans jamais contredire ses réponses précédentes. Jouer deux parties, le joueur appliquant la meilleure stratégie. Noter le nombre de coups de chaque partie. Le maître du jeu malin peut-il dépasser le nombre trouvé à la question 5 ?

??? corrige "Corrigé"

    **3.** **50** (le milieu) : quelle que soit la réponse, on élimine environ la moitié des nombres. Proposer 10, par exemple, ne laisse que 9 nombres si la réponse est « plus petit », mais 90 si elle est « plus grand » : au pire, c’est bien pire.  
    **4.** Au pire **50** nombres (de 51 à 100 ; il en reste 49 si c’est « plus petit »).  
    **5.** $100 \to 50 \to 25 \to 12 \to 6 \to 3 \to 1$ : six coups pour réduire à un seul nombre, et un septième pour le proposer. Au pire **7 coups**.  
    **6.** Le maître du jeu malin obtient en général 7 coups (parfois 6), jamais plus : la meilleure stratégie **garantit** 7 coups, quel que soit le secret. *Remarque : on raisonne sur le **pire cas**, comme on le fera pour le coût d’un algorithme.*

### <span class="exo-num">Exercice 3</span> — Entre 1 et 1000 <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-07-la-recherche-dichotomique-act-1-3 }

1.  **Avant de jouer**, prédire le nombre de coups nécessaires, au pire, avec la meilleure stratégie.

2.  Jouer contre le maître du jeu malin, avec un secret entre 1 et 1000. Combien de coups a-t-il fallu ? La prédiction était-elle juste ?

3.  Recopier et compléter sur le cahier le tableau suivant (sans jouer pour les deux dernières colonnes).

    | Nombres possibles | 100 | 200 | 1 000 | 2 000 | 1 000 000 |
    |:------------------|:---:|:---:|:-----:|:-----:|:---------:|
    | Coups au pire     |     |     |       |       |           |

    Quand on **double** le nombre de possibilités, combien de coups faut-il en plus ? Et quand on le multiplie par 1 000 ?

??? corrige "Corrigé"

    **7.** On est tenté de répondre 70 (« dix fois plus de nombres, dix fois plus de coups ») : c’est l’intuition « linéaire », et elle est fausse. La bonne prédiction est **10**.  
    **8.** On constate 10 coups au plus (9 ou 10 contre le maître du jeu malin).  
    **9.** Coups au pire : $100 \to 7$ ; $200 \to 8$ ; $1\,000 \to 10$ ; $2\,000 \to 11$ ; $1\,000\,000 \to 20$. Doubler le nombre de possibilités ajoute **un seul coup** ; le multiplier par $1\,000$ (environ $2^{10}$) n’en ajoute que **10**.

### <span class="exo-num">Exercice 4</span> — Ce qu’on a découvert <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-07-la-recherche-dichotomique-act-1-4 }

1.  **Ce qu’on a découvert.** Recopier et compléter sur le cahier : « La meilleure stratégie consiste à proposer le … des nombres encore possibles : chaque coup … le nombre de possibilités par … Avec $k$ coups, on peut départager jusqu’à $2^k$ nombres : comme $2^{10} = \ldots$, il suffit de … coups pour 1 000 nombres. »

2.  Cette stratégie marcherait-elle si le maître du jeu ne répondait que « gagné » ou « perdu » ? Qu’est-ce qui la rend possible ?

??? corrige "Corrigé"

    **10.** « La meilleure stratégie consiste à proposer le **milieu** des nombres encore possibles : chaque coup **divise** le nombre de possibilités par **deux**. Avec $k$ coups, on peut départager jusqu’à $2^k$ nombres : comme $2^{10} = \mathbf{1\,024}$, il suffit de **10** coups pour 1 000 nombres. » Ce nombre de coups, le nombre de fois qu’on peut diviser par 2 avant d’arriver à 1, s’appelle le **logarithme en base 2** : $\log_2(1\,000) \approx 10$.  
    **11.** Non : avec seulement « gagné / perdu », on n’apprend rien sur la position du secret et il faut essayer les nombres un par un (jusqu’à 1 000 coups). Ce qui rend la stratégie possible, c’est que les nombres sont **rangés dans l’ordre** : la réponse « plus grand / plus petit » permet d’éliminer d’un coup toute une moitié.
