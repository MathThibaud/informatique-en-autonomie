# Défis Advent of Code

<p class="sous-titre">Réseaux</p>

## <span class="etiquette">Défi 1</span> Shuttle Search

*les navettes — modulo et efficacité*

<p class="infos-activite">Jour 13</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/11-defi-aoc-2020-13){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-11-defi-aoc-2020-13.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/13 ](https://adventofcode.com/2020/day/13 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/11-defi-aoc-2020-13>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|                |              |            |                      |
|:---------------|:-------------|:-----------|:---------------------|
| shuttle bus    | navette      | timestamp  | instant (en minutes) |
| depart         | partir       | earliest   | le plus tôt possible |
| out of service | hors service | ID         | identifiant (numéro) |
| offset         | décalage     | subsequent | suivant, consécutif  |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Arrivé au port, vous devez rejoindre l’aéroport en navette. Chaque navette fait une boucle de durée fixe et repasse donc régulièrement au port ; son numéro est justement la durée de sa boucle, en minutes. Le fichier contient vos notes : l’heure à laquelle vous serez prêt, et la liste des navettes de la compagnie.

    **Ce qu’il faut faire.**

    - Ligne 1 : l’instant $a$ (en minutes) à partir duquel vous pouvez partir. Ligne 2 : les numéros des navettes séparés par des virgules ; un `x` désigne une navette hors service, à ignorer.

    - Toutes les navettes sont parties ensemble à l’instant 0 : la navette numéro $b$ part donc aux instants $0$, $b$, $2b$, $3b$… autrement dit aux multiples de $b$.

    - Il faut trouver la navette qui part le plus tôt à partir de l’instant $a$ (un départ à l’instant $a$ lui-même convient). La réponse est son numéro multiplié par le nombre de minutes d’attente.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-reseaux-aoc-1-1 }

Questions de vérification, à traiter sur le cahier :

1.  Si $a$ est un multiple de $b$, combien de minutes attend-on la navette $b$ ?

2.  Avec $a = 30$, à quel instant part la navette 7, et combien attend-on ?

3.  Les `x` jouent-ils un rôle dans la partie 1 ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-reseaux-aoc-1-2 }

On considère le fichier (inventé) suivant :

```console
96
5,x,7,x,x,11
```

Pour chaque navette, calculer le premier départ à partir de l’instant 96 et l’attente correspondante. Vérification : la réponse est `14`.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire le fichier <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-reseaux-aoc-1-3 }

Écrire une fonction `lire_notes(nom_fichier)` qui renvoie l’instant d’arrivée et la liste des numéros des navettes en service (sans les `x`).

??? pouce "Coup de pouce"

    `ligne.split(",")` découpe la seconde ligne ; on ne garde que les morceaux différents de `"x"`.

### <span class="exo-num">Exercice 4</span> — L’attente, avec un modulo <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-reseaux-aoc-1-4 }

Écrire une fonction `attente(arrivee, numero)` qui renvoie le nombre de minutes à attendre la navette `numero`, **sans boucle**. En déduire la réponse. Tester sur l’exemple de la fiche, puis sur vos données.

??? pouce "Coup de pouce"

    `arrivee % numero` donne le temps écoulé depuis le dernier départ. Attention au cas où il vaut `0` : on part tout de suite.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    La compagnie propose un concours : trouver le moment où les navettes partent les unes après les autres, minute après minute, dans l’ordre de la liste.

    - La première ligne ne sert plus. Les positions dans la liste sont numérotées à partir de 0, `x` compris ; un `x` n’impose aucune condition.

    - Trouver le plus petit instant $t$ tel que la navette en position $i$ parte exactement à l’instant $t + i$, pour toutes les navettes en service.

### <span class="exo-num">Exercice 5</span> — Comprendre la condition <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-reseaux-aoc-1-5 }

Traduire la condition sur une navette de numéro $b$ placée en position $i$ par une égalité avec `%`. Sur l’exemple de la fiche, on doit trouver $t = 215$ : le vérifier pour chacune des trois navettes.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 6</span> — Défi : la partie 2 sur vos données <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-reseaux-aoc-1-6 }

L’énoncé prévient que la réponse dépasse $10^{14}$ : tester tous les instants un par un prendrait des années. Lire la section suivante, puis écrire une fonction `premier_instant(navettes)` qui suit cette méthode. Vérifier sur l’exemple de la fiche et sur ceux de l’énoncé avant vos données.

??? pouce "Coup de pouce"

    On traite les navettes une par une. Une fois une navette satisfaite, on ne regarde plus que des instants qui la satisfont encore.

??? pouce "Coup de pouce 2 (début de solution)"

    Deux variables suffisent : `t` (candidat actuel) et `pas`. Pour chaque navette, on ajoute `pas` à `t` tant que la condition n’est pas vérifiée, puis on met à jour `pas`.

## Pour y arriver : synchroniser des périodes <span class="horsprog">au-delà du programme</span>

!!! encadre "Recherche à pas croissant"

    On cherche $t$ tel que $t \,\%\, 5 = 0$, $(t+2) \,\%\, 7 = 0$ et $(t+5) \,\%\, 11 = 0$ (exemple de la fiche).

    **Idée.** Si $t$ convient pour la navette 5, alors $t + 5$, $t + 10$… conviennent aussi : la condition est *périodique*. Si $t$ convient pour 5 *et* 7, alors $t + 35$, $t + 70$… conviennent encore pour les deux, puisque 35 est un multiple de 5 et de 7.

    **Méthode.** On part de $t = 0$ avec un pas de 1. Pour chaque navette, on avance de *pas* en *pas* jusqu’à ce qu’elle soit satisfaite, puis on multiplie le pas par son numéro : le pas est toujours le produit des périodes déjà satisfaites.

    - navette 5 : $t = 0$ convient tout de suite ; le pas devient $5$ ;

    - navette 7 : on teste $0$, puis $5$ ; $5 + 2 = 7$ est divisible par 7 ; le pas devient $5 \times 7 = 35$ ;

    - navette 11 : on teste $5, 40, 75, 110, 145, 180, 215$ ; $215 + 5 = 220 = 11 \times 20$. Donc $t = 215$.

    Il a suffi de 7 essais au lieu de 215. Pour chaque navette, on fait au plus « numéro » essais : quelques centaines en tout, même si $t$ dépasse $10^{14}$.

    **Pourquoi ça marche.** Les numéros des navettes sont premiers entre eux (ici ce sont même des nombres premiers) : en avançant de pas en pas, on finit toujours par satisfaire la nouvelle navette en moins de « numéro » essais. Si les numéros avaient un diviseur commun, il faudrait prendre leur PPCM.

    **Pour aller plus loin.** En mathématiques, ce problème est résolu par le *théorème des restes chinois* : si $n_1, \dots, n_k$ sont premiers entre eux deux à deux, il existe une unique solution $t$ entre $0$ et $n_1 \times \dots \times n_k - 1$ à un système de conditions $t \,\%\, n_j = r_j$. La méthode ci-dessus est une façon simple de la calculer.

## Approfondissement

!!! encadre "Outil Python : puissance modulaire et inverse (pow(a, b, m))"

    `pow(a, b, m)` calcule $a^b \bmod m$ sans jamais former le très grand nombre $a^b$. Avec l’exposant $-1$, `pow(a, -1, m)` renvoie l’**inverse de $a$ modulo $m$**, c’est-à-dire l’entier $y$ entre $0$ et $m-1$ tel que $a \times y \bmod m = 1$ (Python 3.8 ou plus récent). Il n’existe que si $a$ et $m$ sont premiers entre eux.

    ```python
    print(pow(3, 4))               # 81 : comme 3 ** 4
    print(pow(3, 4, 7))            # 4 : 81 % 7, sans jamais former de tres grand nombre
    print(pow(6, -1, 7))           # 6 : inverse de 6 modulo 7 (6 * 6 = 36 = 5 * 7 + 1)
    print(6 * pow(6, -1, 7) % 7)   # 1
    ```

    **Intérêt.** L’inverse modulaire se calcule en un nombre d’étapes proportionnel au nombre de chiffres (algorithme d’Euclide étendu), même pour des nombres immenses ; le chercher en essayant $y = 1, 2, 3\dots$ prendrait jusqu’à $m$ essais.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : la formule des restes chinois <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-reseaux-aoc-1-7 }

La section précédente cite le théorème des restes chinois. Il donne aussi une **formule** : pour le système $t \,\%\, n_m = r_m$ ($m = 1, \dots, k$), avec des $n_m$ premiers entre eux deux à deux, on pose $N = n_1 \times \dots \times n_k$, $N_m = N / n_m$ et $y_m$ l’inverse de $N_m$ modulo $n_m$. Alors $$t = \Big(\sum_{m} r_m \, N_m \, y_m\Big) \bmod N.$$

1.  Recopier et exécuter le code de l’encadré. Que se passe-t-il avec `pow(4, -1, 6)` ? Pourquoi ?

2.  Pour une navette de numéro $b$ en position $i$, quel reste $r$ doit avoir $t$ modulo $b$ ? Sur l’exemple de la fiche (`5,x,7,x,x,11`), calculer pour chaque navette $r_m$, $N_m$ et $y_m$, puis $t$. On doit retrouver `215`.

3.  Vérifier sur l’exemple que le terme associé à la navette 7 est un multiple de 5 et de 11, et qu’il a le bon reste modulo 7. En déduire pourquoi la formule fonctionne.

4.  Écrire une fonction `restes_chinois(navettes)` et la comparer à `premier_instant` : nombre d’opérations, lisibilité.

    ??? pouce "Coup de pouce"

        `(-i) % b` donne un reste compris entre 0 et `b - 1`, même quand `-i` est négatif.

    ??? pouce "Coup de pouce 2 (début de solution)"

        Une première boucle calcule le produit $N$ ; une seconde ajoute `r * (N // b) * pow(N // b, -1, b)` pour chaque navette ; on renvoie le total modulo $N$.

## <span class="etiquette">Défi 2</span> Lobby Layout

*le carrelage hexagonal — ensembles, coordonnées et automate*

<p class="infos-activite">Jour 24</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/11-defi-aoc-2020-24){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-11-defi-aoc-2020-24.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/24 ](https://adventofcode.com/2020/day/24 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/11-defi-aoc-2020-24>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| hexagonal tile | carreau hexagonal | hex grid | grille hexagonale |
| flip | retourner | white / black side | face blanche / noire |
| reference tile | carreau de référence | step | pas, déplacement |
| neighbor | voisin | delimiter | séparateur |
| east / west | est / ouest | northeast, southwest… | nord-est, sud-ouest… |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Enfin arrivé à l’hôtel, vous trouvez le hall en travaux : il faut poser un carrelage hexagonal formant un motif précis. Chaque carreau est blanc d’un côté et noir de l’autre. Le fichier est la liste des carreaux à retourner, chacun repéré par un chemin à suivre depuis le carreau central.

    **Ce qu’il faut faire.**

    - Le sol est un pavage infini de carreaux hexagonaux, tous blancs au départ, disposés en rangées horizontales : chaque carreau a six voisins, notés `e`, `se`, `sw`, `w`, `nw`, `ne`.

    - Chaque ligne est une suite de directions collées, sans séparateur, à suivre en partant toujours du même carreau de référence. Le carreau d’arrivée est retourné (blanc devient noir, noir devient blanc).

    - Réponse : le nombre de carreaux noirs une fois toutes les lignes traitées.

### <span class="exo-num">Exercice 1</span> — Vérifier sa compréhension <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-reseaux-aoc-2-1 }

1.  Pourquoi `ne` ne peut-il pas être lu comme `n` puis `e` ?

2.  Deux lignes différentes peuvent-elles désigner le même carreau ? Un carreau désigné trois fois finit-il noir ou blanc ?

3.  Le carreau de référence peut-il être retourné ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-reseaux-aoc-2-2 }

On considère le fichier (inventé) suivant :

```console
eee
nwwsw
seswnee
wwnw
enwsw
swsenw
nenenw
ewnwse
```

Découper chaque ligne en directions (par exemple `seswnee` donne `se`, `sw`, `ne`, `e`). Sur un dessin de grille hexagonale, repérer les carreaux désignés par `enwsw` et `ewnwse`. Vérification : à la fin, `6` carreaux sont noirs.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Découper une ligne <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-reseaux-aoc-2-3 }

Écrire une fonction `directions(ligne)` qui renvoie la liste des directions d’une ligne. Tester sur `seswnee`.

??? pouce "Coup de pouce"

    Parcourir la chaîne avec un indice `i` dans une boucle `while` : si le caractère est `n` ou `s`, la direction occupe deux caractères, sinon un seul.

### <span class="exo-num">Exercice 4</span> — Des coordonnées <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-reseaux-aoc-2-4 }

**Avant de coder**, choisir un système de coordonnées (lire l’encadré) et écrire, pour chacune des six directions, le déplacement correspondant. Vérifier sur un dessin que `nw` puis `se`, ou `e`, `nw` puis `sw`, ramènent au point de départ. Écrire alors une fonction `position(ligne)` qui renvoie les coordonnées du carreau désigné.

??? pouce "Coup de pouce"

    Un dictionnaire `DEPLACEMENTS` qui associe à chaque direction un couple `(dx, dy)` rend la fonction très courte.

!!! encadre "Outil Python : les ensembles (set) et la différence symétrique ^"

    Un **ensemble** est une collection sans doublon et sans ordre, où le test `x in ensemble` est très rapide. Ses éléments doivent être non modifiables : nombres, chaînes, **tuples** (une position `(q, r)` convient). L’opérateur `a ^ b` (différence symétrique) donne les éléments qui sont dans `a` ou dans `b`, mais pas dans les deux.

    ```python
    noirs = set()              # ensemble vide (attention : {} est un dict)
    noirs.add((3, 0))
    print((3, 0) in noirs)     # True
    noirs ^= {(1, 1)}          # (1, 1) absent : il est ajoute
    noirs ^= {(3, 0)}          # (3, 0) present : il est retire
    print(noirs)               # {(1, 1)}
    print({1, 2, 3} ^ {3, 4})  # {1, 2, 4}
    ```

    **Intérêt.** `noirs ^= {p}` « retourne » le carreau `p` en une instruction, sans `if`. Avec une liste, chaque test `p in liste` parcourrait toute la liste. Question : que contient `noirs` si l’on exécute trois fois `noirs ^= {(0, 0)}` à partir d’un ensemble vide ?

### <span class="exo-num">Exercice 5</span> — Retourner les carreaux <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-reseaux-aoc-2-5 }

Gérer l’ensemble `noirs` des coordonnées des carreaux noirs et répondre à la partie 1.

??? pouce "Coup de pouce"

    Retourner un carreau, c’est l’ajouter à l’ensemble s’il n’y est pas, l’en retirer sinon. L’opérateur `^=` (différence symétrique) le fait en une instruction : `noirs ^= {p}`.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Le motif n’est pas figé : il évolue de jour en jour selon une règle simple. Partir du carrelage obtenu. Chaque jour, tous les carreaux changent **en même temps** : un carreau noir ayant $0$ ou plus de $2$ voisins noirs devient blanc ; un carreau blanc ayant exactement $2$ voisins noirs devient noir ; les autres ne changent pas. Réponse : le nombre de carreaux noirs après 100 jours.

!!! encadre "Outil Python : compter avec un dictionnaire (get)"

    `d.get(cle, defaut)` renvoie `d[cle]` si la clé existe, et `defaut` sinon (sans erreur et sans créer la clé). C’est idéal pour compter.

    ```python
    compte = {}
    for case in [(0, 1), (2, 0), (0, 1)]:
        compte[case] = compte.get(case, 0) + 1
    print(compte)              # {(0, 1): 2, (2, 0): 1}
    print(compte.get((5, 5), 0))   # 0 : cle absente
    ```

    **Intérêt.** On évite le test `if case in compte: ... else: ...`. Question : que se passerait-il avec `compte[case] = compte[case] + 1` ?

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Un automate cellulaire <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-reseaux-aoc-2-6 }

Écrire une fonction `jour_suivant(noirs)` qui renvoie le nouvel ensemble des carreaux noirs. Sur l’exemple de la fiche, on doit trouver `9` carreaux noirs après un jour, `10` après deux jours et `53` après dix jours.

??? pouce "Coup de pouce"

    La grille est infinie : on ne la stocke pas. Seuls les carreaux noirs et leurs voisins peuvent changer ; ce sont donc les seuls à examiner.

??? pouce "Coup de pouce 2 (début de solution)"

    Construire un dictionnaire `nb_voisins_noirs` : pour chaque carreau noir, ajouter 1 à chacun de ses six voisins. Le nouvel ensemble se construit ensuite à partir de ce dictionnaire et de l’ancien ensemble ; attention aux carreaux noirs qui n’ont aucun voisin noir (ils n’apparaissent pas dans le dictionnaire).

## Pour y arriver : repérer des cases hexagonales

!!! encadre "Trois systèmes de coordonnées possibles"

    Dans une grille hexagonale dont les lignes sont horizontales (comme ici), chaque case a deux voisins sur sa ligne et quatre sur les lignes voisines. Plusieurs repérages sont possibles :

    - **Coordonnées « doublées ».** On numérote les lignes $y$ ; sur une ligne, les colonnes $x$ avancent de 2 en 2, et les lignes voisines sont décalées d’un cran. Une case a donc des coordonnées $(x, y)$ avec $x + y$ pair.

    - **Coordonnées axiales.** Deux axes obliques à $60^\circ$ : chaque déplacement modifie une ou deux coordonnées de $\pm 1$.

    - **Coordonnées cubiques.** Trois coordonnées $(q, r, s)$ liées par $q + r + s = 0$ : chaque déplacement augmente l’une de 1 et en diminue une autre de 1. C’est symétrique et facile à vérifier, au prix d’une coordonnée en trop.

    Dans tous les cas, deux chemins qui mènent à la même case doivent donner exactement les mêmes coordonnées : c’est ce qui permet d’utiliser un ensemble.

## Approfondissement

!!! encadre "Outil Python : parcourir deux listes en parallèle (zip)"

    `zip(a, b)` fournit les couples `(a[0], b[0])`, `(a[1], b[1])`… jusqu’à la fin de la plus courte.

    ```python
    pos = (1, -2, 1)
    pas = (0, 1, -1)
    nouvelle = tuple(p + d for p, d in zip(pos, pas))
    print(nouvelle)                       # (1, -1, 0)
    print(list(zip("abc", [1, 2, 3])))    # [('a', 1), ('b', 2), ('c', 3)]
    ```

    **Intérêt.** Le même code additionne des positions à 2 ou à 3 coordonnées. Question : que donne `list(zip([1, 2, 3], [10, 20]))` ?

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : d’autres systèmes de coordonnées <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-reseaux-aoc-2-7 }

1.  **Coordonnées cubiques.** On repère une case par $(x, y, z)$ avec $x + y + z = 0$ ; on choisit `e` $= (1, -1, 0)$ et `ne` $= (1, 0, -1)$. Trouver les quatre autres déplacements, sachant que `w` est l’opposé de `e` et que faire `e` puis `nw` revient à faire `ne`. Calculer à la main la position de `seswnee`.

2.  Écrire une fonction `position_systeme(ligne, deplacements)` qui fonctionne avec n’importe quel dictionnaire de déplacements (2 ou 3 coordonnées). Vérifier qu’on trouve encore `6` carreaux noirs sur l’exemple de la fiche.

    ??? pouce "Coup de pouce"

        Partir de la liste `[0] * len(deplacements["e"])` et, à chaque pas, additionner coordonnée par coordonnée avec `zip`. Renvoyer un tuple, pour pouvoir le ranger dans un ensemble.

3.  **Coordonnées doublées.** Avec `e` $= (2, 0)$ et `ne` $= (1, -1)$, trouver les autres déplacements. Montrer que $x + y$ est toujours pair. Retrouver le résultat de la partie 1.

4.  **Distance.** En coordonnées cubiques, on admet que le nombre minimal de pas pour aller du centre à la case $(x, y, z)$ est $\max(|x|, |y|, |z|)$. Vérifier sur `eee` et `seswnee`. Quel est, sur l’exemple, le carreau noir le plus éloigné du centre ?

    ??? pouce "Coup de pouce"

        Un pas modifie deux coordonnées d’une unité chacune, en sens contraires : il ne peut faire baisser $\max(|x|, |y|, |z|)$ que d’au plus 1.

5.  Comparer les trois systèmes : nombre de coordonnées, facilité de vérification, calcul des voisins pour la partie 2.
