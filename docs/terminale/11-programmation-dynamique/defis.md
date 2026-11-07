# Défis Advent of Code

<p class="sous-titre">Programmation dynamique</p>

## <span class="etiquette">Défi 1</span> Adapter Array

*les adaptateurs — tri et programmation dynamique*

<p class="infos-activite">Jour 10</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/11-defi-aoc-2020-10){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-11-defi-aoc-2020-10.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/10 ](https://adventofcode.com/2020/day/10 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (lien ci-dessus) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - **Attention aux exemples.** L’énoncé en ligne a son propre exemple, avec d’autres réponses. Les valeurs de test de cette fiche portent sur **l’exemple inventé de la fiche** (exercice « À la main ») : l’enregistrer dans un fichier `exemple.txt` à côté du programme, et ouvrir `"exemple.txt"` au lieu de `"input.txt"` pour tester.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

!!! encadre "Le défi en bref"

    **Le problème.** On dispose d’une centaine d’adaptateurs électriques, chacun avec sa tension, qu’on peut brancher en chaîne entre une prise et un appareil. La partie 1 demande des statistiques sur la chaîne qui utilise tous les adaptateurs ; la partie 2 demande *combien* de chaînes différentes sont possibles. Ce nombre dépasse plusieurs milliers de milliards : impossible de les construire une à une, même avec un ordinateur.

    **Ce qu’on réinvestit.** La **programmation dynamique** vue dans ce chapitre. Le nombre de façons d’atteindre un adaptateur se déduit du nombre de façons d’atteindre les adaptateurs qui peuvent se brancher juste avant lui : en résolvant ces sous-problèmes du plus petit au plus grand, et en mémorisant leurs résultats, on compte un nombre astronomique de possibilités sans en énumérer aucune. On utilise aussi un tri et un dictionnaire pour compter.

    **La démarche de la fiche.**

    1.  Comprendre pourquoi la chaîne complète est la liste triée, puis calculer à la main la réponse de la partie 1 sur un petit exemple.

    2.  Lire et trier les valeurs, puis compter les écarts avec un dictionnaire : réponse de la partie 1.

    3.  Constater qu’énumérer toutes les chaînes est impossible, puis les compter par programmation dynamique : réponse de la partie 2.

    4.  En défi et en approfondissement, écrire une version récursive mémoïsée, puis une méthode par blocs.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| adapter | adaptateur | rated for | prévu pour (valeur nominale) |
| joltage | tension (unité inventée : le *jolt*) | outlet | prise de courant |
| built-in | intégré | lower than | inférieur à |
| distribution | répartition | difference | écart |
| arrangement | façon d’agencer, combinaison | distinct | différent |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** En plein vol vers vos vacances, votre appareil n’a plus de batterie. La prise sous le siège ne fournit pas la bonne tension, mais votre sac déborde d’adaptateurs que l’on peut brancher les uns derrière les autres, comme des rallonges. Il s’agit de vérifier qu’on peut tous les enchaîner, et de décrire les écarts de tension le long de la chaîne.

    **Les données.** Chaque ligne du fichier contient **un entier** : la tension de sortie d’un adaptateur (l’unité, le *jolt*, est inventée). Les lignes ne sont pas rangées, et dans les données toutes les valeurs sont différentes.

    **La règle.**

    - La prise vaut `0`. L’appareil possède son propre adaptateur intégré, qui vaut la plus grande valeur du sac plus `3`.

    - Un adaptateur de valeur $v$ accepte une source de valeur $v-1$, $v-2$ ou $v-3$ : chaque maillon de la chaîne doit être plus grand que le précédent, d’au plus 3.

    - Dans la partie 1, on utilise **tous** les adaptateurs pour former la chaîne prise $\to$ adaptateurs $\to$ appareil.

    - On calcule les écarts entre éléments consécutifs de cette chaîne, y compris l’écart entre la prise et le premier adaptateur, et celui entre le dernier adaptateur et l’appareil. On compte les écarts égaux à 1 et les écarts égaux à 3.

    **La réponse attendue.** Le produit (nombre d’écarts de 1) $\times$ (nombre d’écarts de 3). Par exemple, avec les adaptateurs 2, 3 et 6, la chaîne est 0, 2, 3, 6, 9 : les écarts sont 2, 1, 3, 3, soit un écart de 1 et deux écarts de 3, et la réponse serait $1 \times 2 = 2$.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-programmation-dynamique-aoc-1-1 }

**But.** Vérifier sur trois questions courtes qu’on a compris comment se forme la chaîne complète.

**À quoi ça sert ?** Elles révèlent deux faits qui simplifient tout le programme : la chaîne est la liste triée, et il ne faut oublier ni la prise ni l’appareil.

Questions de vérification, à traiter sur le cahier :

1.  Pourquoi la chaîne de la partie 1 est-elle forcément rangée dans l’ordre croissant ?

2.  Que se passerait-il si deux adaptateurs voisins dans l’ordre croissant étaient séparés de 4 ?

3.  L’écart entre la prise et le premier adaptateur compte-t-il ? Et celui entre le dernier adaptateur et l’appareil ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-programmation-dynamique-aoc-1-2 }

**But.** Former la chaîne et calculer les écarts à la main sur dix adaptateurs.

**À quoi ça sert ?** On obtient un exemple dont on **connaît la réponse** (24), qui servira à tester chaque fonction. Cette même chaîne servira aussi en partie 2 et dans l’approfondissement.

On considère le fichier (inventé) suivant, écrit ici sur une seule ligne pour gagner de la place (dans le vrai fichier : une valeur par ligne) :

```console
9  1  13  4  8  2  14  7  3  12
```

Ranger les valeurs dans l’ordre croissant, ajouter la prise et l’appareil, puis écrire la liste des écarts successifs. Vérification : on doit obtenir `24` pour la partie 1.

## Programmer la partie 1

!!! encadre "Outil Python : strip (nettoyer une ligne lue)"

    Chaque ligne lue dans un fichier (avec `for ligne in fichier` ou `readlines()`) se termine par le caractère de fin de ligne `"\n"` (sauf parfois la dernière). `ligne.strip()` renvoie une copie de la ligne sans les espaces ni les fins de ligne placés au début et à la fin.

    ```python
    ligne = "1721\n"
    print(ligne.strip())                  # 1721
    print(len(ligne), len(ligne.strip())) # 5 4
    ```

    **Intérêt.** Comparer ou découper une ligne sans que la fin de ligne ne gêne : `"abc\n" == "abc"` vaut `False`.

!!! encadre "Méthode : trier une liste par insertion (rappel de Première)"

    On parcourt la liste de gauche à droite ; chaque élément est ramené vers la gauche, en décalant d’un cran les éléments plus grands, jusqu’à sa place dans la partie déjà triée.

    ```python
    def tri_insertion(t):
        """Trie la liste t sur place, par ordre croissant."""
        for i in range(1, len(t)):
            x = t[i]
            j = i
            while j > 0 and t[j - 1] > x:
                t[j] = t[j - 1]          # decaler vers la droite
                j -= 1
            t[j] = x

    t = [9, 1, 13, 4]
    tri_insertion(t)
    print(t)                         # [1, 4, 9, 13]
    ```

    **Intérêt.** Le coût est quadratique dans le pire cas, ce qui reste négligeable pour une centaine d’adaptateurs. Le maximum d’une liste triée est son dernier élément.

### <span class="exo-num">Exercice 3</span> — Lire et ranger <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-programmation-dynamique-aoc-1-3 }

**But.** Construire la chaîne complète sous forme de liste triée, prise et appareil compris.

**À quoi ça sert ?** Toutes les questions suivantes, partie 2 comprise, partent de cette liste : une erreur ici (prise ou appareil oubliés) fausserait toutes les réponses.

Écrire une fonction `chaine(nom_fichier)` qui renvoie la liste triée des valeurs, complétée par `0` au début et par la valeur de l’appareil à la fin.

??? pouce "Coup de pouce"

    Lire les lignes non vides et les convertir avec `int`, puis trier avec le tri par insertion de l’encadré. L’appareil vaut le maximum plus 3, c’est-à-dire le dernier élément de la liste triée plus 3.

!!! encadre "Méthode : compter avec un dictionnaire"

    Pour compter des apparitions, on associe à chaque valeur rencontrée son nombre d’apparitions. Avant d’augmenter un compteur, on teste si la clé existe déjà : sinon, on la crée avec la valeur 1.

    ```python
    compte = {"a": 2}
    for c in ["a", "z", "z"]:
        if c in compte:
            compte[c] += 1     # cle deja presente
        else:
            compte[c] = 1      # premiere apparition
    print(compte)              # {'a': 3, 'z': 2}
    print("y" in compte)       # False : la cle n'existe pas
    ```

    **Intérêt.** Le test `in` et l’accès `compte[c]` coûtent un temps constant en moyenne : on compte en un seul parcours.

    **À essayer.** Recopier et exécuter ce code. Que se passe-t-il si l’on écrit `compte["y"]` ? Écrire une fonction `valeur(d, cle)` qui renvoie `d[cle]` si la clé existe, et `0` sinon.

### <span class="exo-num">Exercice 4</span> — Compter les écarts <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-programmation-dynamique-aoc-1-4 }

**But.** Compter, avec un dictionnaire, combien de fois apparaît chaque écart entre deux valeurs voisines.

**À quoi ça sert ?** Le dictionnaire obtenu donne en un seul parcours le nombre d’écarts de 1 et de 3, donc la réponse de la partie 1.

Écrire une fonction `ecarts(valeurs)` qui renvoie un dictionnaire associant à chaque écart son nombre d’apparitions. En déduire la réponse ; tester sur l’exemple inventé de la fiche, puis sur vos données.

??? pouce "Coup de pouce"

    On compare chaque valeur à la suivante : boucle sur les indices `i` de `0` à `len(valeurs) - 2`.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    **Ce qui change.** Vous voulez maintenant savoir de combien de manières différentes on aurait pu brancher l’appareil, sans être obligé d’utiliser tout le sac.

    **La nouvelle règle.**

    - On compte les chaînes qui relient la prise à l’appareil en respectant toujours la règle des écarts de 1 à 3, avec n’importe quel sous-ensemble des adaptateurs.

    - Deux chaînes sont différentes si elles n’utilisent pas exactement les mêmes adaptateurs.

    - Le nombre obtenu est gigantesque : il faut le compter, pas construire les chaînes une à une.

    **La réponse attendue.** Le nombre total de chaînes possibles. Par exemple, avec les adaptateurs 1, 2 et 3 (appareil 6), l’adaptateur 3 est obligatoire, mais 1 et 2 sont facultatifs : il y a 4 chaînes.

### <span class="exo-num">Exercice 5</span> — Pourquoi pas tout énumérer ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-programmation-dynamique-aoc-1-5 }

**But.** Comprendre pourquoi construire toutes les chaînes une à une est hors de portée.

**À quoi ça sert ?** C’est ce constat qui justifie de changer de méthode : il faut *compter* les chaînes sans les fabriquer, ce que permet la programmation dynamique.

Sur l’exemple inventé de la fiche, on trouve `28` façons. Avec une centaine d’adaptateurs, l’énoncé annonce un nombre astronomique : expliquer pourquoi un programme qui construirait chaque façon une par une ne terminerait jamais.

### <span class="exo-num">Exercice 6</span> — Compter sans énumérer <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-programmation-dynamique-aoc-1-6 }

**But.** Écrire la relation qui relie $N(v)$ aux valeurs de $N$ des adaptateurs précédents, puis la programmer.

**À quoi ça sert ?** C’est le cœur de la partie 2 : en remplissant $N$ du plus petit au plus grand adaptateur, la valeur pour l’appareil est directement la réponse, obtenue en un seul parcours.

On note $N(v)$ le nombre de façons d’aller de la prise jusqu’à l’adaptateur de valeur $v$. Exprimer $N(v)$ à l’aide des valeurs de $N$ pour les adaptateurs qui peuvent se brancher juste avant $v$. Écrire une fonction `nombre_facons(valeurs)` qui reçoit la liste renvoyée par `chaine` (prise et appareil compris), remplit un dictionnaire `N` en parcourant cette liste à partir du **deuxième** élément (la prise est le cas de base : `N[0] = 1`), et renvoie la valeur de `N` pour l’appareil. Vérifier : sur l’exemple, $N(4) = 7$, $N(9) = 14$ et la fonction renvoie `28`.

??? pouce "Coup de pouce"

    C’est de la programmation dynamique : on résout le problème pour chaque adaptateur, du plus petit au plus grand, en réutilisant les résultats déjà calculés.

??? pouce "Coup de pouce 2 (début de solution)"

    Pour chaque valeur `v` après la prise : `N[v]` est la somme des `N[v - k]` pour `k` valant 1, 2 et 3, en comptant 0 si `v - k` n’est pas un adaptateur (tester d’abord `v - k in N`, comme dans l’encadré sur le comptage).

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Défi : la version récursive <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-programmation-dynamique-aoc-1-7 }

**But.** Reformuler le même calcul de façon récursive, constater qu’il est trop lent, puis le corriger.

**À quoi ça sert ?** On voit concrètement pourquoi la mémoïsation est indispensable : c’est elle qui transforme une récursion exponentielle en un calcul aussi rapide que la version itérative.

Écrire une fonction récursive `depuis(valeurs, i)` qui renvoie le nombre de façons d’aller de `valeurs[i]` jusqu’à l’appareil (cas de base : `i` est l’indice de l’appareil, une seule façon) ; `depuis(valeurs, 0)` doit redonner la réponse de la partie 2. La tester sur vos données : que se passe-t-il ? Corriger avec la mémoïsation (ajouter un paramètre `memo`, dictionnaire partagé par tous les appels).

??? pouce "Coup de pouce"

    Sans mémoire, les mêmes sous-problèmes sont recalculés un nombre exponentiel de fois. Un dictionnaire des résultats déjà connus règle le problème.

## Approfondissement

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Approfondissement 1 : découper en blocs <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-programmation-dynamique-aoc-1-8 }

**But.** Compter les chaînes autrement, en découpant la liste en blocs indépendants.

**À quoi ça sert ?** Cette méthode exploite une particularité des données (pas d’écart de 2). La comparer à la programmation dynamique montre ce qu’on gagne et ce qu’on perd en s’appuyant sur une propriété particulière plutôt que sur une méthode générale.

Dans les données (et dans l’exemple inventé de la fiche), les écarts entre adaptateurs consécutifs valent 1 ou 3, jamais 2. On peut en profiter pour compter autrement.

1.  Sur l’exemple, découper la chaîne $0, 1, 2, 3, 4, 7, 8, 9, 12, 13, 14, 17$ en **blocs** de valeurs consécutives (écarts de 1), séparés par les écarts de 3. Expliquer pourquoi la première et la dernière valeur de chaque bloc sont forcément utilisées.

2.  À la main, compter les façons de traverser un bloc de 1, 2, 3, 4 puis 5 valeurs, la première et la dernière étant obligatoires. Vérifier que le produit sur les blocs de l’exemple redonne `28`.

3.  Écrire `facons_bloc(m)` puis `nombre_facons_blocs(valeurs)`.

    ??? pouce "Coup de pouce"

        Un écart de 3 ne laisse aucun choix : les deux adaptateurs qui l’encadrent sont obligatoires. Les choix se font à l’intérieur de chaque bloc, indépendamment des autres blocs : on multiplie.

    ??? pouce "Coup de pouce 2 (début de solution)"

        Parcourir la liste triée en tenant à jour la taille du bloc en cours ; à chaque écart de 3, multiplier le résultat par `facons_bloc(taille)` et repartir à 1. `facons_bloc(m)` peut réutiliser `nombre_facons` sur la liste `[i for i in range(m)]`.

4.  Pourquoi cette méthode tombe-t-elle en défaut s’il existe un écart de 2 ? Laquelle des deux méthodes est la plus générale ?

## <span class="etiquette">Défi 2</span> Rambunctious Recitation

*le jeu de mémoire — dictionnaires et complexité*

<p class="infos-activite">Jour 15</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/11-defi-aoc-2020-15){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-11-defi-aoc-2020-15.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/15 ](https://adventofcode.com/2020/day/15 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (lien ci-dessus) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - **Attention aux exemples.** L’énoncé en ligne a son propre exemple, avec d’autres réponses. Les valeurs de test de cette fiche portent sur **l’exemple inventé de la fiche** (exercice « À la main ») : l’enregistrer dans un fichier `exemple.txt` à côté du programme, et ouvrir `"exemple.txt"` au lieu de `"input.txt"` pour tester.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

!!! encadre "Le défi en bref"

    **Le problème.** Des elfes jouent à un jeu de mémoire : à chaque tour, le nombre annoncé dépend de la dernière fois où le nombre précédent avait été dit. Il faut trouver le nombre annoncé au tour 2020, puis au tour $30\,000\,000$. La règle est simple, mais le jeu ne suit aucun motif prévisible : il faut le simuler tour par tour, et le faire assez vite pour que 30 millions de tours tiennent en quelques secondes.

    **Ce qu’on réinvestit.** Ce défi prolonge ce chapitre : comme pour la **mémoïsation**, on gagne énormément de temps en conservant dans un dictionnaire des informations déjà calculées (ici, le dernier tour où chaque nombre a été dit) au lieu de les rechercher à nouveau dans toute la liste. On réinvestit aussi l’analyse de **complexité** et sa vérification par des mesures de temps.

    **La démarche de la fiche.**

    1.  Vérifier sa compréhension de la règle, puis dérouler les dix premiers tours à la main.

    2.  Écrire une première version qui garde tous les nombres dans une liste et y cherche le précédent : réponse de la partie 1.

    3.  Estimer et mesurer le coût de cette version, pour constater qu’elle est trop lente pour la partie 2.

    4.  Remplacer la recherche par un dictionnaire, ce qui rend chaque tour de coût constant : réponse de la partie 2.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| memory game | jeu de mémoire | take turns | parler à tour de rôle |
| starting numbers | nombres de départ | spoken | prononcé, dit |
| most recently | le plus récemment | turn | tour |
| apart | d’écart, séparés de | age | âge (ici : un écart de tours) |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** En attendant votre avion, vous appelez les elfes du pôle Nord : ils jouent à un jeu de mémoire où chacun, à son tour, annonce un nombre qui dépend de ce qui a déjà été dit. Vous voulez prévoir ce qui sera annoncé bien plus tard dans la partie.

    **Les données.** Le fichier contient **une seule ligne** : les nombres de départ, séparés par des virgules. Ils sont tous différents.

    **La règle.**

    - Les tours sont numérotés à partir de 1. Les premiers tours servent à annoncer les nombres de départ, dans l’ordre.

    - Ensuite, à chaque tour, on regarde le nombre annoncé au tour précédent.

    - S’il était annoncé pour la première fois, on annonce `0`.

    - Sinon, on annonce l’écart entre le tour où il vient d’être annoncé et le tour où il l’avait été la fois d’avant : autrement dit, « il y a combien de tours qu’on l’avait déjà dit ? ». Seule compte l’avant-dernière fois, pas les plus anciennes.

    **La réponse attendue.** Le nombre annoncé au tour 2020. Par exemple, avec les nombres de départ 1 et 3, la partie se poursuit par 0 (3 est nouveau), 0 (0 est nouveau), 1 (0 a été dit aux tours 4 et 3), puis 4 (1 a été dit aux tours 5 et 1).

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-programmation-dynamique-aoc-2-1 }

**But.** Vérifier sur trois questions courtes qu’on a compris la règle, en particulier les cas particuliers.

**À quoi ça sert ?** Ces cas (nombre nouveau, nombre répété deux fois de suite) sont ceux où un programme se trompe le plus souvent ; la dernière question servira à justifier l’optimisation du défi final.

Questions de vérification, à traiter sur le cahier :

1.  Que dit-on juste après le dernier nombre de départ (les nombres de départ étant tous différents) ?

2.  Si le même nombre est dit à deux tours consécutifs, que dit-on au tour suivant ?

3.  Le nombre dit au tour $k$ peut-il dépasser $k$ (une fois les nombres de départ passés) ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-programmation-dynamique-aoc-2-2 }

**But.** Dérouler à la main les dix premiers tours du jeu.

**À quoi ça sert ?** On obtient un exemple dont on **connaît le début** : le programme devra retrouver exactement ces dix nombres avant d’être lancé sur 2020 tours.

Avec les nombres de départ (inventés) `2,0,1`, écrire les dix premiers nombres dits, en numérotant les tours à partir de 1. Vérification : les cinq premiers sont `2, 0, 1, 0, 2` et le dixième vaut `2`.

## Programmer la partie 1

Le fichier ne contient qu’une ligne : on la lit avec `read()`, on la nettoie avec `strip`, puis on la découpe avec `split(",")` avant de convertir chaque morceau avec `int`.

!!! encadre "Outil Python : strip (nettoyer une ligne lue)"

    Chaque ligne lue dans un fichier (avec `for ligne in fichier` ou `readlines()`) se termine par le caractère de fin de ligne `"\n"` (sauf parfois la dernière). `ligne.strip()` renvoie une copie de la ligne sans les espaces ni les fins de ligne placés au début et à la fin.

    ```python
    ligne = "1721\n"
    print(ligne.strip())                  # 1721
    print(len(ligne), len(ligne.strip())) # 5 4
    ```

    **Intérêt.** Comparer ou découper une ligne sans que la fin de ligne ne gêne : `"abc\n" == "abc"` vaut `False`.

### <span class="exo-num">Exercice 3</span> — Une première version avec une liste <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-programmation-dynamique-aoc-2-3 }

**But.** Simuler le jeu en gardant la liste de tous les nombres dits et en y cherchant la fois précédente.

**À quoi ça sert ?** C’est la traduction la plus directe de la règle : elle donne la réponse de la partie 1 et servira de référence pour vérifier la version rapide.

Écrire une fonction `jeu_liste(depart, n)` qui construit la liste de tous les nombres dits et renvoie le `n`-ième. Pour savoir quand le dernier nombre a été dit auparavant, on cherche dans la liste. Tester sur l’exemple inventé de la fiche : avec `n = 2020`, on doit trouver `779`.

??? pouce "Coup de pouce"

    Parcourir la liste à l’envers à partir de l’avant-dernier élément pour trouver l’occurrence précédente du dernier nombre.

!!! encadre "Outil Python : mesurer une durée (module time)"

    La fonction `time.perf_counter()` renvoie un instant en secondes (avec beaucoup de décimales). La différence entre deux appels donne la durée écoulée entre les deux.

    ```python
    import time

    debut = time.perf_counter()     # instant de depart (en secondes)
    total = 0
    for i in range(1000000):
        total += i
    duree = time.perf_counter() - debut
    print(f"{duree:.3f} s")         # duree ecoulee, arrondie a 3 decimales
    ```

    **Intérêt.** Vérifier *expérimentalement* une complexité : si doubler la taille des données double le temps, le programme est linéaire ; s’il le multiplie par 4, il est quadratique. Les durées varient d’une machine à l’autre : seuls les rapports comptent.

    **À essayer.** Recopier et exécuter ce code, puis remplacer `1000000` par `2000000`. Comment évolue la durée ?

### <span class="exo-num">Exercice 4</span> — Combien d’opérations ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-programmation-dynamique-aoc-2-4 }

**But.** Évaluer le coût de la première version, par le calcul puis par des mesures.

**À quoi ça sert ?** On découvre que la recherche dans la liste rend la méthode quadratique : c’est ce qui la rend inutilisable pour la partie 2, et qui indique quoi améliorer.

Au tour numéro $k$, combien de cases la recherche peut-elle examiner au pire ? En déduire la complexité de `jeu_liste` en fonction de $n$. Mesurer le temps pour $n = 2020$, puis $n = 20\,000$ et $n = 40\,000$ avec le module `time` : le résultat est-il cohérent ?

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    **Ce qui change.** Les elfes sont infatigables : ils continuent la partie beaucoup plus longtemps.

    **La nouvelle règle.**

    - Même jeu, mêmes nombres de départ, même règle.

    - Seul le nombre de tours change : il faut aller jusqu’au tour $30\,000\,000$, soit près de quinze mille fois plus loin qu’en partie 1.

    **La réponse attendue.** Le nombre annoncé au tour $30\,000\,000$. La difficulté n’est pas la règle, mais le temps de calcul.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 5</span> — 30 millions de tours <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-programmation-dynamique-aoc-2-5 }

**But.** Remplacer la recherche dans la liste par un dictionnaire qui mémorise le dernier tour de chaque nombre.

**À quoi ça sert ?** Chaque tour coûte alors un temps constant : la simulation devient linéaire et 30 millions de tours prennent quelques secondes. C’est la réponse de la partie 2.

Combien de temps prendrait `jeu_liste` pour 30 millions de tours, d’après vos mesures ? Écrire une fonction `jeu_dict(depart, n)` qui ne garde **pas** la liste des nombres, mais un dictionnaire `dernier_tour` associant à chaque nombre déjà dit le dernier tour où il a été dit. Vérifier qu’elle donne `779` pour 2020 tours sur l’exemple, puis `5068275` pour 30 millions de tours (patience : quelques secondes).

??? pouce "Coup de pouce"

    Accéder à un dictionnaire ou y écrire coûte un temps à peu près constant, quelle que soit sa taille : chaque tour devient de coût constant, donc l’ensemble est linéaire en $n$.

??? pouce "Coup de pouce 2 (début de solution)"

    Garder le dernier nombre dit dans une variable à part, et ne le ranger dans le dictionnaire qu’**après** avoir calculé le suivant : sinon on écrase l’information dont on a besoin.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 6</span> — Défi : encore plus vite <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-programmation-dynamique-aoc-2-6 }

**But.** Remplacer le dictionnaire par une liste indexée par le nombre lui-même, et comparer.

**À quoi ça sert ?** On gagne encore du temps en échange de mémoire : c’est un compromis classique entre temps de calcul et place occupée.

Hormis les nombres de départ (petits), les nombres dits sont toujours inférieurs au nombre de tours. Remplacer le dictionnaire par une liste de taille fixe `[0] * n` (une liste de `n` zéros) indexée par le nombre lui-même. Comparer les temps : pourquoi est-ce plus rapide, et qu’est-ce que cela coûte en mémoire ?

??? pouce "Coup de pouce"

    Un tour non encore joué peut être codé par `0`, puisque les tours sont numérotés à partir de 1.
