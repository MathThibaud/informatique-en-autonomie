# Défis Advent of Code

<p class="sous-titre">Processus et ordonnancement</p>

## <span class="etiquette">Défi 1</span> Seating System

*la salle d’attente — automate cellulaire et copie de grilles*

<p class="infos-activite">Jour 11</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/10-defi-aoc-2020-11){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-10-defi-aoc-2020-11.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/11 ](https://adventofcode.com/2020/day/11 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/10-defi-aoc-2020-11>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|                  |                 |               |                    |
|:-----------------|:----------------|:--------------|:-------------------|
| seat layout      | plan des sièges | floor         | sol (pas un siège) |
| empty / occupied | libre / occupé  | adjacent      | voisin, adjacent   |
| simultaneously   | en même temps   | round         | tour (de règles)   |
| become           | devenir         | stop changing | cesser de changer  |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Vous attendez un ferry dans une salle encore vide et vous voulez prévoir où les voyageurs vont s’asseoir, pour choisir la meilleure place. Leur comportement est très prévisible : on le simule comme un *automate cellulaire*. Le fichier est le plan de la salle : chaque caractère est une case du sol ou un siège.

    **Ce qu’il faut faire.**

    - `.` représente le sol, `L` un siège libre, `#` un siège occupé.

    - Les voisins d’une case sont les 8 cases qui l’entourent (même ligne, même colonne et diagonales), sans sortir du plan.

    - À chaque tour, **toutes** les cases changent en même temps, d’après l’état du tour précédent. Un siège libre dont aucun voisin n’est occupé devient occupé (on aime être tranquille). Un siège occupé qui a au moins 4 voisins occupés se libère (trop de monde). Dans les autres cas, rien ne change ; le sol ne change jamais.

    - On répète les tours jusqu’à ce que plus rien ne bouge. La réponse est le nombre de sièges occupés à ce moment-là.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-processus-et-ordonnancement-aoc-1-1 }

Questions de vérification, à traiter sur le cahier :

1.  Combien de voisins a une case du bord qui n’est pas un coin ?

2.  Un siège occupé qui a exactement 3 voisins occupés change-t-il d’état ? Et un siège libre qui en a 1 ?

3.  Pourquoi ne peut-on pas modifier la grille au fur et à mesure qu’on la parcourt ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-processus-et-ordonnancement-aoc-1-2 }

On considère la grille (inventée) suivante :

```console
L.LLL
LLLL.
L.L.L
LLLLL
..L.L
```

Dessiner la grille après un tour, puis après deux tours. Vérification : la grille ne change plus après le troisième tour, et l’on compte alors `11` sièges occupés.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire la grille <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-processus-et-ordonnancement-aoc-1-3 }

Écrire une fonction `lire_grille(nom_fichier)` qui renvoie une liste de listes de caractères (une liste par ligne). Afficher le nombre de lignes et de colonnes.

### <span class="exo-num">Exercice 4</span> — Compter les voisins occupés <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-processus-et-ordonnancement-aoc-1-4 }

Écrire une fonction `voisins_occupes(grille, i, j)` qui renvoie le nombre de sièges occupés autour de la case $(i, j)$. La tester sur une case du bord et sur une case du centre.

??? pouce "Coup de pouce"

    Deux boucles sur les décalages `di` et `dj` dans `[-1, 0, 1]`, sans oublier d’exclure le cas `(0, 0)` et de vérifier qu’on ne sort pas de la grille.

!!! encadre "Outil Python : compter des éléments (count)"

    `l.count(x)` renvoie le nombre d’éléments de la liste `l` égaux à `x` ; la même méthode existe pour les chaînes de caractères.

    ```python
    ligne = ["#", ".", "L", "#"]
    print(ligne.count("#"))     # 2 : nombre d'elements egaux a "#"
    print("#.L##".count("#"))   # 3 : fonctionne aussi sur une chaine
    grille = [["#", "L"], ["#", "#"]]
    print(sum([l.count("#") for l in grille]))   # 3 : somme des comptes de chaque ligne
    ```

    **Intérêt.** Une ligne au lieu d’une boucle et d’un compteur. Attention : `count` parcourt toute la liste, son coût est proportionnel à sa longueur.

    **À essayer.** Que renvoie `[1, 2, 1].count(3)` ?

### <span class="exo-num">Exercice 5</span> — Un tour, puis jusqu’à stabilité <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-processus-et-ordonnancement-aoc-1-5 }

Écrire une fonction `tour(grille)` qui renvoie la **nouvelle** grille sans modifier l’ancienne, puis répéter les tours tant que la grille change. Tester sur l’exemple de la fiche, puis sur vos données.

??? pouce "Coup de pouce"

    Attention : toutes les cases changent **en même temps**. Si l’on modifie la grille pendant qu’on la parcourt, les cases suivantes voient un mélange d’ancien et de nouvel état. Sur l’exemple, la première ligne deviendrait `#.#L#` au lieu de `#.###` après un tour.

??? pouce "Coup de pouce 2 (début de solution)"

    `copie = grille[:]` ne suffit pas : les lignes restent partagées. Construire une nouvelle liste de listes, par exemple par compréhension : `[ligne[:] for ligne in grille]`, ou remplir une grille neuve case par case. Deux listes de listes se comparent directement avec `==`.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    En observant mieux, on comprend que les voyageurs ne regardent pas seulement les places juste à côté : ils regardent aussi plus loin.

    - Dans chacune des 8 directions, on compte le **premier siège visible** (libre ou occupé) en sautant les cases de sol ; s’il n’y a que du sol jusqu’au bord, la direction ne compte pas.

    - Un siège occupé se libère s’il voit au moins 5 sièges occupés. La règle pour s’asseoir et la réponse demandée ne changent pas.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Ce que l’on voit <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-processus-et-ordonnancement-aoc-1-6 }

Écrire une fonction `visibles_occupes` (mêmes paramètres que `voisins_occupes`), puis adapter `tour` pour qu’elle reçoive en paramètres la fonction de comptage et le seuil. Sur l’exemple de la fiche, on doit trouver `9`.

??? pouce "Coup de pouce"

    Pour chacune des 8 directions `(di, dj)`, on avance pas à pas tant qu’on est dans la grille et sur du sol ; on s’arrête au premier siège rencontré.

??? pouce "Coup de pouce 2 (début de solution)"

    Une fonction est une valeur comme une autre en Python : `tour(grille, visibles_occupes, 5)` est un appel tout à fait valide, et dans `tour` on appelle simplement le paramètre reçu.

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

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Défi : précalculer <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-processus-et-ordonnancement-aoc-1-7 }

Les voisins visibles d’un siège ne dépendent pas de l’état des sièges, seulement de la position du sol. Les calculer une seule fois au début (dictionnaire case $\to$ liste de cases) et mesurer le gain de temps avec le module `time`.

??? pouce "Coup de pouce"

    Le sol ne change jamais : la recherche dans les 8 directions peut être faite une fois pour toutes.

## <span class="etiquette">Défi 2</span> Crab Combat

*la bataille contre le crabe — files et récursivité*

<p class="infos-activite">Jour 22</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/10-defi-aoc-2020-22){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-10-defi-aoc-2020-22.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/22 ](https://adventofcode.com/2020/day/22 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/10-defi-aoc-2020-22>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| deck | paquet de cartes | round | manche, tour |
| draw | tirer, piocher | top / bottom | dessus / dessous (du paquet) |
| higher-valued | de plus grande valeur | winner | gagnant |
| score | score | sub-game | sous-partie (partie 2) |
| recursive | récursif | infinite game | partie sans fin |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Sur le radeau, l’ennui guette ; heureusement, un petit crabe est monté à bord et accepte de jouer aux cartes avec vous, à un jeu proche de la bataille. Le fichier donne la main de départ de chaque joueur.

    **Ce qu’il faut faire.**

    - Le fichier contient deux blocs (joueur 1, puis joueur 2) : une carte par ligne, la carte du dessus en premier. Toutes les valeurs sont différentes.

    - À chaque manche, chaque joueur retire sa carte du dessus ; la plus forte gagne. Le gagnant place les deux cartes sous son paquet : la sienne d’abord, puis celle de l’adversaire.

    - La partie s’arrête quand un joueur a toutes les cartes.

    - Score du gagnant : la carte du dessous est multipliée par $1$, celle juste au-dessus par $2$, etc., jusqu’à la carte du dessus multipliée par le nombre de cartes ; on additionne. Autrement dit, plus une carte est haut dans le paquet, plus elle compte. Réponse : ce score.

### <span class="exo-num">Exercice 1</span> — Vérifier sa compréhension <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-processus-et-ordonnancement-aoc-2-1 }

1.  Une manche peut-elle se terminer par une égalité ?

2.  Le gagnant a 10 cartes, la carte du dessus vaut 4 : que rapporte-t-elle au score ?

3.  Le nombre total de cartes change-t-il au cours de la partie ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-processus-et-ordonnancement-aoc-2-2 }

On considère les paquets (inventés) suivants, le dessus étant écrit en premier :

```console
Joueur 1 : 6 2 8 1
Joueur 2 : 4 7 3 5
```

Jouer les trois premières manches à la main en écrivant les deux paquets après chaque manche. Combien de cartes chaque joueur a-t-il alors ? Vérification : la partie complète dure `18` manches et le score du gagnant vaut `198`.

## Programmer la partie 1

!!! encadre "Outil Python : la file toute faite (collections.deque)"

    Le module `collections` fournit `deque` (prononcer « dèque »), une file à deux bouts : on peut ajouter et retirer aussi bien au début qu’à la fin, en temps constant.

    ```python
    from collections import deque
    d = deque([6, 2, 8, 1])    # dessus du paquet a gauche
    x = d.popleft()            # retire et renvoie 6
    d.append(4)                # ajoute a la fin : deque([2, 8, 1, 4])
    d.extend([7, 3])           # ajoute plusieurs elements a la fin
    print(len(d), d[0])        # 6 2 : longueur, premier element
    print(list(d)[:2])         # [2, 8] : copie en liste pour faire une tranche
    if d:                      # une deque vide vaut False
        print("non vide")
    ```

    **Intérêt.** Avec une liste Python, `liste.pop(0)` décale tous les autres éléments d’une case : $O(n)$ opérations. `popleft` est en $O(1)$ : sur une partie de plusieurs milliers de manches, la différence se voit. C’est l’implémentation « professionnelle » de la file du cours. Question : que contient `d` à la fin du code ? Que se passe-t-il si l’on appelle `popleft` sur une `deque` vide ?

### <span class="exo-num">Exercice 3</span> — Une file pour chaque joueur <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-processus-et-ordonnancement-aoc-2-3 }

Lire le fichier et ranger les cartes de chaque joueur dans une **file** : on retire au début (dessus du paquet), on ajoute à la fin (dessous). Utiliser `collections.deque`, ou une classe `File` du cours.

??? pouce "Coup de pouce"

    Avec `from collections import deque`, `d = deque([6, 2, 8, 1])`, `d.popleft()` renvoie `6` et `d.append(x)` ajoute à la fin, en temps constant. Avec une liste, `pop(0)` est en $O(n)$.

!!! encadre "Outil Python : parcourir avec l’indice (enumerate)"

    `enumerate(suite)` fournit à chaque tour le couple `(indice, élément)`.

    ```python
    for i, carte in enumerate([8, 6, 7]):
        print(i, carte)        # 0 8, puis 1 6, puis 2 7
    ```

    **Intérêt.** On évite `for i in range(len(paquet))` suivi de `paquet[i]`, qui est moins lisible (et lent sur une `deque`, où l’accès par indice au milieu n’est pas en temps constant). Question : écrire avec `enumerate` une boucle qui affiche `carte * (3 - i)` pour la liste `[8, 6, 7]`.

### <span class="exo-num">Exercice 4</span> — Jouer et compter <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-processus-et-ordonnancement-aoc-2-4 }

Écrire une fonction `combat(p1, p2)` qui joue la partie et renvoie le paquet du gagnant, puis une fonction `score(paquet)`. Tester sur l’exemple, puis sur vos données.

??? pouce "Coup de pouce"

    La boucle tourne `while p1 and p2` : une file vide vaut `False`. Pour le score, la carte du dessous est multipliée par 1 : avec `enumerate`, la carte d’indice `i` est multipliée par `len(paquet) - i`.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Le crabe a perdu et propose une revanche à une version « récursive » du jeu.

    - Avant chaque manche : si la même configuration des deux paquets est déjà apparue **dans cette partie**, le joueur 1 gagne aussitôt la partie.

    - Sinon, chacun tire sa carte. Si chaque joueur a encore au moins autant de cartes que la valeur qu’il vient de tirer, le gagnant de la manche est celui d’une sous-partie jouée avec des copies de ses $n$ cartes suivantes ($n$ = valeur tirée). Sinon, la plus forte carte gagne. Le gagnant range les cartes comme avant.

    - Réponse : le score du gagnant de la partie principale.

!!! encadre "Outil Python : un ensemble de tuples pour mémoriser des états"

    Un **ensemble** (`set`) est une collection sans doublon, dans laquelle le test `x in ensemble` est très rapide. On ne peut y ranger que des valeurs **non modifiables** (nombres, chaînes, tuples) : ni liste, ni `deque`. Pour mémoriser l’état des deux paquets, on le convertit en un couple de tuples.

    ```python
    from collections import deque
    p1, p2 = deque([6, 2]), deque([4, 7])
    deja_vus = set()                          # ensemble vide
    etat = (tuple(p1), tuple(p2))             # ((6, 2), (4, 7))
    print(etat in deja_vus)                   # False
    deja_vus.add(etat)
    print(((6, 2), (4, 7)) in deja_vus)       # True
    ```

    **Intérêt.** Avec une liste des états déjà vus, chaque test parcourrait toute la liste ; avec un ensemble, il prend un temps constant (en moyenne). Question : que se passe-t-il si l’on essaie `deja_vus.add(p1)` ?

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 5</span> — Le combat récursif <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-processus-et-ordonnancement-aoc-2-5 }

Écrire une fonction récursive `combat_recursif(p1, p2)` qui renvoie le numéro du gagnant et son paquet. Sur l’exemple de la fiche, le joueur 1 gagne avec un score de `151`. Bien relire la règle qui empêche une partie de durer indéfiniment : elle s’applique à **chaque** partie et sous-partie séparément.

??? pouce "Coup de pouce"

    La mémoire des situations déjà vues est un **ensemble** créé au début de chaque appel de la fonction (donc propre à chaque sous-partie). Une `deque` n’est pas utilisable comme élément d’un ensemble : y ranger le couple `(tuple(p1), tuple(p2))`.

??? pouce "Coup de pouce 2 (début de solution)"

    Pour une sous-partie, on construit de **nouveaux** paquets (copies) : `deque(list(p1)[:n])` prend les `n` cartes du dessus sans modifier `p1`. La fonction renvoie un couple `(gagnant, paquet)` ; dans la sous-partie, seul le gagnant compte pour décider de la manche en cours.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 6</span> — Défi : mesurer <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-processus-et-ordonnancement-aoc-2-6 }

Compter le nombre total d’appels de `combat_recursif` et la profondeur maximale de récursion atteinte sur vos données. Pourquoi la profondeur reste-t-elle faible ?

??? pouce "Coup de pouce"

    À chaque appel récursif, le nombre total de cartes en jeu diminue strictement.
