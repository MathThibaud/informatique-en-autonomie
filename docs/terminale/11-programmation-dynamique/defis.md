# Défis Advent of Code

<p class="sous-titre">Programmation dynamique</p>

## <span class="etiquette">Défi 1</span> Adapter Array

*les adaptateurs — tri et programmation dynamique*

<p class="infos-activite">Jour 10</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/11-defi-aoc-2020-10){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-11-defi-aoc-2020-10.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/10 ](https://adventofcode.com/2020/day/10 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/11-defi-aoc-2020-10>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

*Ce défi réinvestit la programmation dynamique vue dans ce chapitre : on compte un nombre astronomique de possibilités en réutilisant les résultats des sous-problèmes déjà résolus.*

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

    **Contexte.** En plein vol vers vos vacances, votre appareil n’a plus de batterie. La prise sous le siège ne fournit pas la bonne tension, mais votre sac déborde d’adaptateurs que l’on peut brancher les uns derrière les autres, comme des rallonges. Chaque ligne du fichier est la tension de sortie d’un de ces adaptateurs (l’unité, le *jolt*, est inventée).

    **Ce qu’il faut faire.**

    - La prise vaut `0`. L’appareil possède son propre adaptateur intégré, qui vaut la plus grande valeur du sac plus `3`. Dans les données, toutes les valeurs sont différentes.

    - Un adaptateur de valeur $v$ accepte une source de valeur $v-1$, $v-2$ ou $v-3$ : autrement dit, chaque maillon de la chaîne doit être plus grand que le précédent, d’au plus 3.

    - Dans la partie 1, on utilise **tous** les adaptateurs pour former la chaîne prise $\to$ adaptateurs $\to$ appareil. On compte les écarts égaux à 1 et les écarts égaux à 3 entre éléments consécutifs ; la réponse est (nombre d’écarts de 1) $\times$ (nombre d’écarts de 3).

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-programmation-dynamique-aoc-1-1 }

Questions de vérification, à traiter sur le cahier :

1.  Pourquoi la chaîne de la partie 1 est-elle forcément rangée dans l’ordre croissant ?

2.  Que se passerait-il si deux adaptateurs voisins dans l’ordre croissant étaient séparés de 4 ?

3.  L’écart entre la prise et le premier adaptateur compte-t-il ? Et celui entre le dernier adaptateur et l’appareil ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-programmation-dynamique-aoc-1-2 }

On considère le fichier (inventé) suivant, écrit ici sur une seule ligne pour gagner de la place (dans le vrai fichier : une valeur par ligne) :

```console
9  1  13  4  8  2  14  7  3  12
```

Ranger les valeurs dans l’ordre croissant, ajouter la prise et l’appareil, puis écrire la liste des écarts successifs. Vérification : on doit obtenir `24` pour la partie 1.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire et ranger <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-programmation-dynamique-aoc-1-3 }

Écrire une fonction `chaine(nom_fichier)` qui renvoie la liste triée des valeurs, complétée par `0` au début et par la valeur de l’appareil à la fin.

??? pouce "Coup de pouce"

    La méthode `sort()` ou la fonction `sorted` trient une liste. L’appareil vaut le maximum plus 3.

!!! encadre "Outil Python : la méthode get des dictionnaires (d.get(cle, defaut))"

    `d.get(cle, defaut)` renvoie la valeur associée à `cle` si la clé existe, et la valeur `defaut` sinon, sans provoquer d’erreur. Le dictionnaire n’est pas modifié.

    ```python
    compte = {"a": 2}
    print(compte.get("a", 0))   # 2 : la cle existe
    print(compte.get("z", 0))   # 0 : cle absente, on obtient la valeur par defaut
    compte["z"] = compte.get("z", 0) + 1   # compter sans tester si la cle existe
    print(compte)               # {'a': 2, 'z': 1}
    ```

    **Intérêt.** On évite d’écrire un test `if cle in d: … else: …` à chaque fois qu’on compte ou qu’on lit une valeur peut-être absente. Le coût reste celui d’un accès au dictionnaire : constant en moyenne.

    **À essayer.** Recopier et exécuter ce code. Que se passe-t-il si l’on écrit `compte["y"]` ? Et `compte.get("y")`, sans second argument ?

### <span class="exo-num">Exercice 4</span> — Compter les écarts <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-programmation-dynamique-aoc-1-4 }

Écrire une fonction `ecarts(valeurs)` qui renvoie un dictionnaire associant à chaque écart son nombre d’apparitions. En déduire la réponse ; tester sur l’exemple de la fiche, puis sur vos données.

??? pouce "Coup de pouce"

    On compare chaque valeur à la suivante : boucle sur les indices `i` de `0` à `len(valeurs) - 2`.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Vous voulez maintenant savoir de combien de manières différentes on aurait pu brancher l’appareil, sans être obligé d’utiliser tout le sac.

    - Compter les chaînes qui relient la prise à l’appareil en respectant toujours la règle des écarts de 1 à 3, avec n’importe quel sous-ensemble des adaptateurs.

    - Deux chaînes sont différentes si elles n’utilisent pas exactement les mêmes adaptateurs. Le nombre obtenu est gigantesque.

### <span class="exo-num">Exercice 5</span> — Pourquoi pas tout énumérer ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-programmation-dynamique-aoc-1-5 }

Sur l’exemple de la fiche, on trouve `28` façons. Avec une centaine d’adaptateurs, l’énoncé annonce un nombre astronomique : expliquer pourquoi un programme qui construirait chaque façon une par une ne terminerait jamais.

### <span class="exo-num">Exercice 6</span> — Compter sans énumérer <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-programmation-dynamique-aoc-1-6 }

On note $N(v)$ le nombre de façons d’aller de la prise jusqu’à l’adaptateur de valeur $v$. Exprimer $N(v)$ à l’aide des valeurs de $N$ pour les adaptateurs qui peuvent se brancher juste avant $v$. Écrire une fonction `nombre_facons(valeurs)` qui remplit un dictionnaire `N` en parcourant la liste triée. Vérifier : sur l’exemple, $N(4) = 7$ et $N(9) = 14$.

??? pouce "Coup de pouce"

    C’est de la programmation dynamique : on résout le problème pour chaque adaptateur, du plus petit au plus grand, en réutilisant les résultats déjà calculés.

??? pouce "Coup de pouce 2 (début de solution)"

    `N[0] = 1`, puis pour chaque valeur `v` : `N[v]` est la somme des `N[v - k]` pour `k` valant 1, 2 et 3, en comptant 0 si `v - k` n’est pas un adaptateur (méthode `get` des dictionnaires).

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Défi : la version récursive <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-programmation-dynamique-aoc-1-7 }

Écrire une version récursive de `nombre_facons` (le nombre de façons de finir la chaîne à partir de l’adaptateur d’indice `i`). La tester sur vos données : que se passe-t-il ? Corriger avec la mémoïsation.

??? pouce "Coup de pouce"

    Sans mémoire, les mêmes sous-problèmes sont recalculés un nombre exponentiel de fois. Un dictionnaire des résultats déjà connus règle le problème.

## Approfondissement

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Approfondissement 1 : découper en blocs <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-programmation-dynamique-aoc-1-8 }

Dans les données (et dans l’exemple de la fiche), les écarts entre adaptateurs consécutifs valent 1 ou 3, jamais 2. On peut en profiter pour compter autrement.

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

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/11-defi-aoc-2020-15>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

*Ce défi prolonge ce chapitre : comme pour la mémoïsation, on gagne énormément de temps en conservant dans un dictionnaire des informations déjà calculées au lieu de les rechercher à nouveau.*

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| memory game | jeu de mémoire | take turns | parler à tour de rôle |
| starting numbers | nombres de départ | spoken | prononcé, dit |
| most recently | le plus récemment | turn | tour |
| apart | d’écart, séparés de | age | âge (ici : un écart de tours) |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** En attendant votre avion, vous appelez les elfes du pôle Nord : ils jouent à un jeu de mémoire où chacun, à son tour, annonce un nombre qui dépend de ce qui a déjà été dit. Le fichier contient seulement les nombres par lesquels la partie commence.

    **Ce qu’il faut faire.**

    - Le fichier est une ligne de nombres de départ séparés par des virgules.

    - Les tours sont numérotés à partir de 1. Les premiers tours servent à annoncer les nombres de départ, dans l’ordre.

    - Ensuite, à chaque tour, on regarde le nombre annoncé au tour précédent. S’il était annoncé pour la première fois, on annonce `0`. Sinon, on annonce l’écart entre le tour où il vient d’être annoncé et le tour où il l’avait été la fois d’avant : autrement dit, « il y a combien de tours qu’on l’avait déjà dit ? ».

    - La réponse est le nombre annoncé au tour 2020.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-programmation-dynamique-aoc-2-1 }

Questions de vérification, à traiter sur le cahier :

1.  Que dit-on juste après le dernier nombre de départ (les nombres de départ étant tous différents) ?

2.  Si le même nombre est dit à deux tours consécutifs, que dit-on au tour suivant ?

3.  Le nombre dit au tour $k$ peut-il dépasser $k$ (une fois les nombres de départ passés) ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-programmation-dynamique-aoc-2-2 }

Avec les nombres de départ (inventés) `2,0,1`, écrire les dix premiers nombres dits, en numérotant les tours à partir de 1. Vérification : les cinq premiers sont `2, 0, 1, 0, 2` et le dixième vaut `2`.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Une première version avec une liste <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-programmation-dynamique-aoc-2-3 }

Écrire une fonction `jeu_liste(depart, n)` qui construit la liste de tous les nombres dits et renvoie le `n`-ième. Pour savoir quand le dernier nombre a été dit auparavant, on cherche dans la liste. Tester sur l’exemple de la fiche : avec `n = 2020`, on doit trouver `779`.

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

Au tour numéro $k$, combien de cases la recherche peut-elle examiner au pire ? En déduire la complexité de `jeu_liste` en fonction de $n$. Mesurer le temps pour $n = 2020$, puis $n = 20\,000$ et $n = 40\,000$ avec le module `time` : le résultat est-il cohérent ?

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Les elfes sont infatigables : ils continuent la partie beaucoup plus longtemps.

    - Même jeu, mêmes nombres de départ. La réponse est le nombre annoncé au tour $30\,000\,000$.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 5</span> — 30 millions de tours <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-programmation-dynamique-aoc-2-5 }

Combien de temps prendrait `jeu_liste` pour 30 millions de tours, d’après vos mesures ? Écrire une fonction `jeu_dict(depart, n)` qui ne garde **pas** la liste des nombres, mais un dictionnaire `dernier_tour` associant à chaque nombre déjà dit le dernier tour où il a été dit. Vérifier qu’elle donne `779` pour 2020 tours sur l’exemple, puis `5068275` pour 30 millions de tours (patience : quelques secondes).

??? pouce "Coup de pouce"

    Accéder à un dictionnaire ou y écrire coûte un temps à peu près constant, quelle que soit sa taille : chaque tour devient de coût constant, donc l’ensemble est linéaire en $n$.

??? pouce "Coup de pouce 2 (début de solution)"

    Garder le dernier nombre dit dans une variable à part, et ne le ranger dans le dictionnaire qu’**après** avoir calculé le suivant : sinon on écrase l’information dont on a besoin.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 6</span> — Défi : encore plus vite <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-programmation-dynamique-aoc-2-6 }

Hormis les nombres de départ (petits), les nombres dits sont toujours inférieurs au nombre de tours. Remplacer le dictionnaire par une liste de taille fixe `[0] * n` (une liste de `n` zéros) indexée par le nombre lui-même. Comparer les temps : pourquoi est-ce plus rapide, et qu’est-ce que cela coûte en mémoire ?

??? pouce "Coup de pouce"

    Un tour non encore joué peut être codé par `0`, puisque les tours sont numérotés à partir de 1.
