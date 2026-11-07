# Défis Advent of Code

<p class="sous-titre">Programmation orientée objet et paradigmes</p>

## <span class="etiquette">Défi 1</span> Toboggan Trajectory

*la descente en luge — grille et modulo*

<p class="infos-activite">Jour 3</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/02-defi-aoc-2020-03){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-02-defi-aoc-2020-03.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/3 ](https://adventofcode.com/2020/day/3 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (lien ci-dessus) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - **Attention aux exemples.** L’énoncé en ligne a son propre exemple, avec d’autres réponses. Les valeurs de test de cette fiche portent sur **l’exemple inventé de la fiche** (exercice « À la main ») : l’enregistrer dans un fichier `exemple.txt` à côté du programme, et ouvrir `"exemple.txt"` au lieu de `"input.txt"` pour tester.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

!!! encadre "Le défi en bref"

    **Le problème.** Une luge descend une pente boisée en ligne droite, et l’on veut savoir combien d’arbres elle va percuter. La carte de la forêt compte plusieurs centaines de lignes et, en théorie, elle se prolonge sans fin vers la droite : impossible de suivre la trajectoire à la main, et impossible de stocker une carte infinie. Le programme doit donc retrouver, pour chaque case atteinte, la case correspondante de la carte réelle.

    **Ce qu’on réinvestit.** L’**encapsulation** vue dans ce chapitre. Le calcul qui ramène une colonne quelconque dans la carte réelle (un modulo) sera caché dans une classe `Foret`, derrière une méthode `est_arbre(x, y)` (exercice « Cacher le modulo dans une classe »). L’utilisateur de la classe croit manipuler une forêt infinie, alors que l’objet ne stocke que le motif de la carte : c’est exactement le rôle d’une interface, qui sépare ce qu’on fait de la façon dont c’est fait.

    **La démarche de la fiche.**

    1.  Comprendre le déplacement et la répétition de la carte, puis suivre la luge à la main sur une petite carte.

    2.  Lire la carte dans une liste de chaînes.

    3.  Écrire une fonction qui compte les arbres pour une pente quelconque : elle donne la partie 1.

    4.  Cacher le calcul du modulo dans une classe `Foret` (encapsulation).

    5.  Partie 2 : appeler cette fonction pour cinq pentes et multiplier les résultats.

    6.  En approfondissement, dessiner le trajet sur la carte.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| toboggan | luge | slope | pente (déplacement) |
| tree | arbre | open square | case libre |
| grid | grille | repeats to the right | se répète vers la droite |
| right 3, down 1 | 3 à droite, 1 en bas | top-left corner | coin en haut à gauche |
| encounter | rencontrer | bottom | bas (de la carte) |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Toujours en route vers l’aéroport, le héros dévale une pente boisée en luge, sans pouvoir vraiment la diriger. Il dispose d’une carte de la forêt vue de dessus et veut savoir combien d’arbres il va percuter en suivant une trajectoire fixée.

    **Les données.** Le fichier est cette carte. Chaque ligne du fichier représente une rangée de la pente (la première ligne est en haut), et chaque caractère une case : `.` désigne une case libre et `#` un arbre. Toutes les lignes ont la même longueur.

    **La règle.**

    - La forêt est bien plus large que la carte : le même motif se répète indéfiniment vers la **droite** (mais pas vers le bas). Autrement dit, après la dernière colonne, on retrouve la première.

    - On part de la case en haut à gauche (ligne 0, colonne 0).

    - À chaque pas, on se déplace de 3 colonnes vers la droite et de 1 ligne vers le bas. Par exemple, sur une carte large de 5 cases, le 2e pas mène à la colonne 6 de la forêt, qui correspond à la colonne 1 de la carte.

    - On regarde la case atteinte à chaque pas ; la case de départ ne compte pas.

    - On s’arrête quand on dépasse la dernière ligne de la carte.

    **La réponse attendue.** Le nombre d’arbres sur les cases atteintes. Par exemple, si les cases atteintes contiennent, dans l’ordre, `.`, `#`, `#`, `.`, `#`, la réponse serait 3.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-programmation-orientee-objet-et-paradigm-aoc-1-1 }

**But.** Vérifier qu’on sait suivre la luge, en particulier quand elle sort de la carte par la droite.

**À quoi ça sert ?** La première question fait découvrir le calcul de colonne (le modulo) qu’utilisera le programme ; la deuxième fixe le nombre de tours de la boucle ; la troisième explique pourquoi on ne recopie pas la carte.

Après lecture de l’énoncé et du résumé, vérifier sa compréhension :

1.  Sur une carte de largeur 7, dans quelle colonne de la carte réelle arrive-t-on au 4<sup>e</sup> pas ?

2.  Sur une carte de 9 lignes, combien de cases visite-t-on en plus de la case de départ ?

3.  Pourquoi est-il maladroit de recopier la carte vers la droite avant de commencer ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-programmation-orientee-objet-et-paradigm-aoc-1-2 }

**But.** Suivre la trajectoire à la main sur une carte de neuf lignes.

**À quoi ça sert ?** On obtient un exemple dont on **connaît la réponse** (`2`) pour tester la fonction de comptage ; dessiner la carte prolongée aide aussi à voir que la colonne réelle se calcule par un reste.

On considère la carte (inventée) suivante, large de $7$ cases :

```console
..#....
#...#..
.#...#.
...#..#
#.#....
..#.#..
.#...#.
#......
...##..
```

Recopier la carte sur le cahier, prolongée vers la droite, et marquer les cases visitées avec le déplacement de la partie 1. Vérification : on doit rencontrer `2` arbres.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire la carte <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-programmation-orientee-objet-et-paradigm-aoc-1-3 }

**But.** Ranger la carte dans une liste de chaînes `carte`, une chaîne par ligne.

**À quoi ça sert ?** Avec cette liste, la case de la ligne `y` et de la colonne `x` s’obtient directement par `carte[y][x]`. Afficher hauteur et largeur vérifie la lecture et donne la largeur, indispensable pour le modulo.

Construire la liste `carte` des lignes de `input.txt` (des chaînes, sans le retour à la ligne final). Afficher la hauteur et la largeur de la carte.

??? pouce "Coup de pouce"

    `f.read().split()` donne directement la liste des lignes sans les `\n`.

### <span class="exo-num">Exercice 4</span> — Compter les arbres <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-programmation-orientee-objet-et-paradigm-aoc-1-4 }

**But.** Écrire une fonction qui compte les arbres rencontrés pour une pente quelconque `(dx, dy)`.

**À quoi ça sert ?** Appelée avec la pente `(3, 1)`, elle donne la réponse de la partie 1. Avoir mis la pente en paramètres, plutôt que d’écrire 3 et 1 en dur, permettra de la réutiliser telle quelle dans la partie 2.

Écrire une fonction `compter_arbres(carte, dx, dy)` qui renvoie le nombre d’arbres rencontrés en se déplaçant de `dx` cases vers la droite et `dy` vers le bas à chaque pas. Tester sur l’exemple inventé de la fiche, puis sur vos données.

??? pouce "Coup de pouce"

    Inutile de recopier la carte vers la droite : la colonne `x` d’une carte infinie correspond à la colonne `x % largeur` de la carte réelle.

??? pouce "Coup de pouce 2 (début de solution)"

    Une boucle `for y in range(dy, len(carte), dy)` donne les lignes visitées (la case de départ, en ligne 0, n’est pas comptée) ; la colonne `x` augmente de `dx` à chaque tour.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 5</span> — Cacher le modulo dans une classe <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-programmation-orientee-objet-et-paradigm-aoc-1-5 }

**But.** Écrire une classe `Foret` qui donne l’illusion d’une forêt infinie.

**À quoi ça sert ?** C’est l’encapsulation du chapitre : l’utilisateur de la classe demande si une case est un arbre sans savoir que la carte est répétée par un modulo. Le comptage des arbres s’écrit alors sans aucun calcul de colonne.

Écrire une classe `Foret` dont le constructeur reçoit la liste `carte`, avec deux méthodes :

- `hauteur(self)` : renvoie le nombre de lignes de la forêt ;

- `est_arbre(self, x, y)` : renvoie `True` si la case de la colonne `x` et de la ligne `y` de la forêt infinie est un arbre, `False` sinon.

Écrire ensuite `compter_arbres_foret(foret, dx, dy)`, qui fait le même travail que `compter_arbres` à partir d’un objet `Foret`, **sans** utiliser `%` ni `len(carte[0])`. Vérifier qu’elle donne les mêmes résultats.

??? pouce "Coup de pouce"

    Le constructeur range la carte et sa largeur dans des attributs ; le modulo n’apparaît plus que dans `est_arbre`.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    **Ce qui change.** Le héros veut comparer plusieurs trajectoires avant de choisir la moins dangereuse. La carte et la façon de compter les arbres ne changent pas ; seule la pente (le déplacement à chaque pas) varie.

    **La nouvelle règle.**

    - Refaire le comptage pour cinq pentes : (1 à droite, 1 en bas), (3, 1), (5, 1), (7, 1) et (1 à droite, **2** en bas).

    - Pour la dernière pente, on descend de deux lignes à chaque pas : on saute donc une ligne sur deux.

    **La réponse attendue.** Le **produit** des cinq nombres d’arbres obtenus. Par exemple, si les cinq pentes rencontraient 2, 3, 1, 4 et 2 arbres, la réponse serait 48.

### <span class="exo-num">Exercice 6</span> — Plusieurs pentes <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-programmation-orientee-objet-et-paradigm-aoc-1-6 }

**But.** Appeler la fonction de comptage pour les cinq pentes et multiplier les résultats.

**À quoi ça sert ?** C’est la réponse de la partie 2. On mesure l’intérêt d’une fonction bien paramétrée : la partie 2 ne demande que quelques lignes de plus.

Utiliser la fonction précédente pour toutes les pentes demandées et calculer la réponse. Sur l’exemple inventé de la fiche, on doit trouver `72`.

??? pouce "Coup de pouce"

    Ranger les pentes dans une liste de tuples `(dx, dy)` et accumuler dans une variable initialisée à `1` (et non à `0`, puisqu’on multiplie).

??? pouce "Coup de pouce 2 (début de solution)"

    Si la réponse de la partie 2 est fausse alors que la partie 1 est juste, tester la pente qui descend de plus d’une ligne : votre boucle saute-t-elle bien des lignes ?

## Approfondissement

!!! encadre "Méthode : d’une chaîne à une liste et retour"

    Une chaîne n’est pas modifiable : `ligne[2] = "X"` provoque une erreur. On la convertit en liste de caractères par une compréhension de liste, puis, une fois la liste modifiée, on reconstruit une chaîne avec une boucle d’accumulation, en partant de la chaîne vide.

    ```python
    ligne = "..#.."
    cases = [c for c in ligne]        # ['.', '.', '#', '.', '.']
    cases[2] = "X"                    # une liste, elle, se modifie
    texte = ""
    for c in cases:
        texte = texte + c             # on ajoute les caracteres un a un
    print(texte)                      # ..X..
    ```

    **Intérêt.** La liste sert de brouillon modifiable ; la chaîne n’est reconstruite qu’une fois, à la fin.

    **À essayer.** Que se passe-t-il si l’on exécute directement `ligne[2] = "X"` ? Écrire une fonction `recoller(morceaux, sep)` qui renvoie les chaînes de la liste `morceaux` mises bout à bout, séparées par `sep` : `recoller(["a", "b", "c"], "-")` doit renvoyer `"a-b-c"` (pas de séparateur à la fin).

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Défi : visualiser le trajet <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-programmation-orientee-objet-et-paradigm-aoc-1-7 }

**But.** Afficher la carte avec le trajet de la luge, en marquant les cases visitées.

**À quoi ça sert ?** Voir le trajet permet de repérer d’un coup d’œil une erreur de déplacement (une ligne sautée, un modulo oublié). C’est aussi l’occasion de contourner le fait qu’une chaîne n’est pas modifiable.

Écrire une fonction qui affiche la carte en remplaçant chaque case visitée par `O` (case libre) ou `X` (arbre). Les chaînes n’étant pas modifiables, comment s’y prendre ?

??? pouce "Coup de pouce"

    Convertir chaque ligne en liste avec `[c for c in ligne]`, la modifier, puis reconstruire la chaîne avec une boucle d’accumulation (voir l’encadré « Méthode »).

## <span class="etiquette">Défi 2</span> Rain Risk

*la navigation — programmation orientée objet*

<p class="infos-activite">Jour 12</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/02-defi-aoc-2020-12){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-02-defi-aoc-2020-12.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/12 ](https://adventofcode.com/2020/day/12 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (lien ci-dessus) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - **Attention aux exemples.** L’énoncé en ligne a son propre exemple, avec d’autres réponses. Les valeurs de test de cette fiche portent sur **l’exemple inventé de la fiche** (exercice « À la main ») : l’enregistrer dans un fichier `exemple.txt` à côté du programme, et ouvrir `"exemple.txt"` au lieu de `"input.txt"` pour tester.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

!!! encadre "Le défi en bref"

    **Le problème.** Un navire reçoit plus de sept cents ordres de navigation : se décaler, pivoter, avancer. Il faut savoir où il se trouve à la fin, mesuré par sa distance au point de départ. Chaque ordre est simple, mais leur enchaînement est impossible à suivre de tête ; la partie 2 change en plus le sens de la plupart des ordres.

    **Ce qu’on réinvestit.** La **programmation orientée objet** vue dans ce chapitre. Le navire a un *état* (sa position, son orientation) que chaque ordre modifie : une classe regroupe cet état dans des attributs, et les actions possibles dans des méthodes (tourner, exécuter un ordre, calculer la distance). Le programme principal se réduit alors à « créer un navire, lui donner les ordres un par un ».

    **La démarche de la fiche.**

    1.  Vérifier sa compréhension des ordres, puis suivre le navire à la main sur un quadrillage.

    2.  Écrire la classe `Navire`, puis une méthode pour pivoter par quarts de tour.

    3.  Écrire la méthode qui exécute un ordre et l’appliquer à tout le fichier : réponse de la partie 1.

    4.  Pour la partie 2, ajouter un point de repère qui reprend le rôle de l’orientation, puis réorganiser le code par héritage.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| ship | navire | facing | orienté vers |
| north / south | nord / sud | east / west | est / ouest |
| turn left / right | tourner à gauche / droite | degrees | degrés |
| forward | en avant | Manhattan distance | distance de Manhattan |
| waypoint | point de repère (partie 2) | relative to | par rapport à |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Le ferry est pris dans une tempête et son ordinateur de navigation a produit une liste d’ordres très tortueuse. Vous aidez le capitaine à savoir où ces ordres mènent le bateau, pour estimer l’écart avec la route prévue.

    **Les données.** Chaque ligne du fichier est un ordre : **une lettre** (l’action) immédiatement suivie d’**un entier** (la quantité), par exemple `N4` ou `R90`. Les ordres s’exécutent dans l’ordre des lignes.

    **La règle.**

    - Au départ, le navire est à l’origine et pointe vers l’est.

    - `N`, `S`, `E`, `W` déplacent le navire de la quantité indiquée vers le nord, le sud, l’est ou l’ouest, **sans** changer la direction vers laquelle il pointe : il se décale comme un crabe.

    - `L` et `R` le font pivoter sur place vers la gauche ou la droite du nombre de degrés indiqué (toujours un multiple de 90 dans les données). Il ne se déplace pas.

    - `F` le fait avancer de la quantité indiquée, droit devant lui, dans la direction vers laquelle il pointe.

    **La réponse attendue.** La distance de Manhattan entre l’arrivée et le départ, c’est-à-dire $|x| + |y|$ (comme dans une ville quadrillée, on ne coupe pas en diagonale). Par exemple, avec les ordres `F2`, `R90`, `F3`, le navire avance de 2 vers l’est, pivote vers le sud, avance de 3 : il finit en $(2, -3)$ et la réponse serait $2 + 3 = 5$.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-programmation-orientee-objet-et-paradigm-aoc-2-1 }

**But.** Vérifier sur trois questions courtes qu’on distingue bien se décaler, pivoter et avancer.

**À quoi ça sert ?** La confusion entre `N` (se décaler vers le nord) et « avancer en pointant vers le nord » est l’erreur la plus fréquente ; le sens des rotations en est une autre.

Questions de vérification, à traiter sur le cahier :

1.  Le navire tourné vers l’est exécute `N4` : vers où est-il tourné ensuite ?

2.  En partant de l’est, quelle orientation obtient-on après `R270` ? Après `L180` ?

3.  Un navire termine à 3 unités à l’ouest et 5 au sud : quelle réponse ? Pourquoi des valeurs absolues ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-programmation-orientee-objet-et-paradigm-aoc-2-2 }

**But.** Suivre le navire ordre par ordre sur un quadrillage.

**À quoi ça sert ?** On obtient un exemple dont on **connaît la réponse** (6) et une position intermédiaire : si le programme se trompe, on pourra afficher la position après chaque ordre et repérer le premier écart.

On considère les instructions (inventées) suivantes, une par ligne dans le fichier :

```console
N4  F6  L90  F3  R180  W2  F5
```

Suivre le navire sur un quadrillage (est vers la droite, nord vers le haut). Vérification : après `F3`, le navire est à 6 unités à l’est et 7 au nord ; la réponse finale est `6`.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — La classe `Navire` <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-programmation-orientee-objet-et-paradigm-aoc-2-3 }

**But.** Écrire la classe qui représente le navire : sa position, son orientation et le calcul de la distance.

**À quoi ça sert ?** Toute la suite manipule cet objet. Représenter l’orientation par un vecteur `(dx, dy)` plutôt que par une lettre rend l’ordre `F` immédiat : on ajoute $k$ fois ce vecteur à la position.

Écrire une classe `Navire` dont le constructeur initialise la position `x`, `y` (est et nord) et l’orientation sous forme d’un vecteur `dx`, `dy` (vers l’est : `(1, 0)`). Ajouter une méthode `distance(self)` qui renvoie la distance de Manhattan à l’origine.

### <span class="exo-num">Exercice 4</span> — Tourner par quarts de tour <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-programmation-orientee-objet-et-paradigm-aoc-2-4 }

**But.** Faire pivoter le vecteur d’orientation par quarts de tour, dans les deux sens.

**À quoi ça sert ?** C’est la partie délicate des ordres `L` et `R`. Une seule formule (le quart de tour à gauche) suffit pour tous les angles ; elle resservira telle quelle pour faire tourner le waypoint en partie 2.

Écrire une méthode `tourner_gauche(self)` qui fait tourner l’orientation d’un quart de tour vers la gauche. Vérifier sur papier : est $\to$ nord $\to$ ouest $\to$ sud $\to$ est. En déduire `tourner(self, sens, angle)`, où `sens` vaut `"L"` (gauche) ou `"R"` (droite) et `angle` vaut 90, 180 ou 270.

??? pouce "Coup de pouce"

    Écrire les quatre vecteurs `(1, 0)`, `(0, 1)`, `(-1, 0)`, `(0, -1)` dans l’ordre et chercher comment on passe de l’un au suivant : les coordonnées s’échangent, et l’une change de signe.

??? pouce "Coup de pouce 2 (début de solution)"

    Un quart de tour à gauche transforme `(dx, dy)` en `(-dy, dx)`. Tourner à droite de 90° revient à tourner à gauche de 270°, et `angle // 90` donne le nombre de quarts de tour.

### <span class="exo-num">Exercice 5</span> — Exécuter le fichier <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-programmation-orientee-objet-et-paradigm-aoc-2-5 }

**But.** Traduire une ligne du fichier en action sur le navire, puis exécuter tout le fichier.

**À quoi ça sert ?** Cette méthode réunit les briques précédentes et donne la réponse de la partie 1. Le programme principal se réduit à une boucle sur les lignes.

!!! encadre "Outil Python : strip (nettoyer une ligne lue)"

    Chaque ligne lue dans un fichier (avec `for ligne in fichier` ou `readlines()`) se termine par le caractère de fin de ligne `"\n"` (sauf parfois la dernière). `ligne.strip()` renvoie une copie de la ligne sans les espaces ni les fins de ligne placés au début et à la fin.

    ```python
    ligne = "1721\n"
    print(ligne.strip())                  # 1721
    print(len(ligne), len(ligne.strip())) # 5 4
    ```

    **Intérêt.** Comparer ou découper une ligne sans que la fin de ligne ne gêne : `"abc\n" == "abc"` vaut `False`.

Écrire une méthode `executer(self, instruction)` qui reçoit une chaîne comme `"F6"` et met à jour le navire. Lire le fichier, exécuter toutes les instructions et afficher la distance. Tester sur l’exemple inventé de la fiche, puis sur vos données.

??? pouce "Coup de pouce"

    Lire les lignes avec `readlines()` et les nettoyer avec `strip` ; `instruction[0]` donne la lettre, `int(instruction[1:])` la valeur.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    **Ce qui change.** En relisant le manuel, on découvre que la plupart des ordres ne concernent pas le navire lui-même, mais un point de repère (*waypoint*) qu’il poursuit.

    **La nouvelle règle.**

    - Le waypoint est repéré **par rapport au navire** ; au départ, il est à 10 unités à l’est et 1 au nord du navire.

    - `N`, `S`, `E`, `W` déplacent le waypoint (pas le navire).

    - `L`, `R` font tourner le waypoint autour du navire, du nombre de degrés indiqué.

    - `F` $k$ déplace le navire $k$ fois du vecteur navire $\to$ waypoint ; le waypoint suit le navire et garde sa position relative.

    **La réponse attendue.** La même qu’en partie 1 : la distance de Manhattan entre l’arrivée du navire et son départ. Avec les ordres `F2`, `R90`, `F3`, le navire va en $(20, 2)$, le waypoint pivote en $(1, -10)$, puis le navire finit en $(23, -28)$ : la réponse serait 51.

### <span class="exo-num">Exercice 6</span> — Le waypoint <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-programmation-orientee-objet-et-paradigm-aoc-2-6 }

**But.** Adapter le navire pour qu’il suive un waypoint, et exécuter les ordres avec leur nouveau sens.

**À quoi ça sert ?** Le waypoint joue exactement le rôle du vecteur d’orientation de la partie 1 : en le voyant, on réutilise la rotation déjà écrite et l’on obtient la réponse de la partie 2 avec peu de code nouveau.

Écrire une classe `NavireRepere` (ou ajouter les attributs `wx`, `wy`) et une méthode `executer2`. Sur l’exemple inventé de la fiche, on doit trouver `70`.

??? pouce "Coup de pouce"

    Le waypoint est repéré **par rapport au navire** : il joue exactement le rôle du vecteur d’orientation de la partie 1, mais avec une longueur quelconque. La méthode de rotation se réutilise telle quelle.

??? pouce "Coup de pouce 2 (début de solution)"

    Sur l’exemple, après `N4` et `F6` le navire est à 60 est, 30 nord ; après `L90` le waypoint est à `(-5, 10)` par rapport au navire.

!!! encadre "Outil Python : l’héritage (class Fille(Mere) et super())"

    Une classe peut **hériter** d’une autre : elle reçoit automatiquement tous ses attributs et méthodes, et l’on n’écrit que ce qui change. Une méthode réécrite dans la classe fille *remplace* celle de la classe mère ; `super()` permet d’appeler la version de la classe mère.

    ```python
    class Animal:
        def __init__(self, nom):
            self.nom = nom

        def presenter(self):
            return f"Je suis {self.nom}"

        def cri(self):
            return "..."

    class Chat(Animal):               # Chat herite de Animal
        def __init__(self, nom):
            super().__init__(nom)     # appelle le constructeur de Animal
            self.vies = 9

        def cri(self):                # redefinition de la methode
            return "Miaou"

    c = Chat("Tom")
    print(c.presenter())   # Je suis Tom : methode heritee, non reecrite
    print(c.cri())         # Miaou : methode redefinie
    print(c.vies)          # 9
    ```

    **Intérêt.** Ne pas recopier le code commun à deux classes proches : une correction faite dans la classe mère profite aux deux.

    **À essayer.** Supprimer la ligne `super().__init__(nom)`, puis exécuter `c.presenter()`. Que se passe-t-il, et pourquoi ?

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Défi : héritage <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-programmation-orientee-objet-et-paradigm-aoc-2-7 }

**But.** Écrire la classe de la partie 2 comme une classe fille de `Navire`.

**À quoi ça sert ?** L’héritage évite de recopier ce qui est commun aux deux navires (position, distance, rotation) : on n’écrit que ce qui change, et une correction faite une fois profite aux deux classes.

Écrire `NavireRepere` comme une classe fille de `Navire` qui ne redéfinit que ce qui change. Quelles méthodes peut-on hériter sans les réécrire ?

??? pouce "Coup de pouce"

    `class NavireRepere(Navire):` puis `super().__init__()` dans le constructeur.

## Approfondissement

!!! encadre "Outil Python : les nombres complexes (complex, 1j)"

    Python sait calculer avec les nombres complexes : `3 + 2j` a pour partie réelle 3 et pour partie imaginaire 2 (Python écrit `j` ce que l’on note $i$ en mathématiques, avec $i^2 = -1$). On peut voir un complexe comme un point ou un vecteur du plan : partie réelle = abscisse (est), partie imaginaire = ordonnée (nord).

    ```python
    z = 3 + 2j              # partie reelle 3, partie imaginaire 2
    print(z.real, z.imag)   # 3.0 2.0
    print(z + (1 - 1j))     # (4+1j) : on additionne coordonnee par coordonnee
    print(1j * 1j)          # (-1+0j) : j * j = -1
    print(z * 1j)           # (-2+3j)
    print(abs(z))           # 3.605... : longueur du vecteur (pas Manhattan !)
    ```

    **Intérêt.** Multiplier par `1j` fait tourner un vecteur d’un quart de tour vers la gauche : $(x + yi) \times i = -y + xi$, c’est exactement la formule $(d_x, d_y) \mapsto (-d_y, d_x)$. Position et direction deviennent chacune un seul nombre.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Approfondissement : naviguer avec des nombres complexes <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-programmation-orientee-objet-et-paradigm-aoc-2-8 }

**But.** Refaire les deux parties en représentant position et direction par des nombres complexes.

**À quoi ça sert ?** Une représentation bien choisie simplifie le code : une rotation devient une multiplication. Comparer avec la version objet montre qu’il n’y a pas une seule bonne modélisation.

1.  Recopier et exécuter le code de l’encadré. Calculer à la main $1 \times i$, puis $i \times i$, $(-1) \times i$ et $(-i) \times i$ : quelles orientations successives retrouve-t-on ? Par quel nombre faut-il multiplier pour un quart de tour vers la droite ?

2.  Sur l’exemple inventé de la fiche, la position et la direction sont des complexes ; au départ `position = 0` et `direction = 1`. Que valent-elles après `N4`, `F6`, `L90` puis `F3` ?

3.  Écrire une fonction `trajet_complexe(instructions, partie)` qui traite les deux parties ; vérifier qu’on obtient `6` et `70` sur l’exemple.

    ??? pouce "Coup de pouce"

        Un dictionnaire associe à chaque lettre `N`, `S`, `E`, `W` son vecteur unitaire : `1j`, `-1j`, `1`, `-1`.

    ??? pouce "Coup de pouce 2 (début de solution)"

        `L` $k$ : multiplier la direction par `1j ** (k // 90)` ; `R` : par `(-1j) ** (k // 90)`. En partie 2, la variable `direction` joue le rôle du waypoint (au départ `10 + 1j`) : `N`, `S`, `E`, `W` la modifient au lieu de modifier la position.

4.  Pourquoi `abs(position)` ne donne-t-il pas la réponse ? Comparer cette version avec la classe `Navire` : longueur, lisibilité, facilité à corriger.
