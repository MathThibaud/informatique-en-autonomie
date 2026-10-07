# Défis Advent of Code

<p class="sous-titre">Programmation orientée objet et paradigmes</p>

## <span class="etiquette">Défi 1</span> Toboggan Trajectory

*la descente en luge — grille et modulo*

<p class="infos-activite">Jour 3</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/02-defi-aoc-2020-03){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-02-defi-aoc-2020-03.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/3 ](https://adventofcode.com/2020/day/3 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/02-defi-aoc-2020-03>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

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

    **Contexte.** Toujours en route vers l’aéroport, le héros dévale une pente boisée en luge, sans pouvoir vraiment la diriger. Il dispose d’une carte de la forêt vue de dessus : chaque ligne du fichier représente une rangée de la pente, chaque caractère une case, libre ou occupée par un arbre. Il veut savoir combien d’arbres il va percuter en suivant une trajectoire fixée.

    **Ce qu’il faut faire.**

    - Dans la carte, `.` désigne une case libre et `#` un arbre ; toutes les lignes ont la même longueur.

    - La forêt est bien plus large que la carte : le même motif se répète indéfiniment vers la **droite** (mais pas vers le bas). Autrement dit, après la dernière colonne, on retrouve la première.

    - On part de la case en haut à gauche (ligne 0, colonne 0). À chaque pas, on se déplace de 3 colonnes vers la droite et de 1 ligne vers le bas, et l’on s’arrête quand on dépasse la dernière ligne de la carte.

    - Il faut renvoyer le nombre d’arbres sur les cases atteintes à chaque pas.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-programmation-orientee-objet-et-paradigm-aoc-1-1 }

Après lecture de l’énoncé et du résumé, vérifier sa compréhension :

1.  Sur une carte de largeur 7, dans quelle colonne de la carte réelle arrive-t-on au 4<sup>e</sup> pas ?

2.  Sur une carte de 9 lignes, combien de cases visite-t-on en plus de la case de départ ?

3.  Pourquoi est-il maladroit de recopier la carte vers la droite avant de commencer ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-programmation-orientee-objet-et-paradigm-aoc-1-2 }

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

Construire la liste `carte` des lignes de `input.txt` (des chaînes, sans le retour à la ligne final). Afficher la hauteur et la largeur de la carte.

??? pouce "Coup de pouce"

    `f.read().split()` donne directement la liste des lignes sans les `\n`.

### <span class="exo-num">Exercice 4</span> — Compter les arbres <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-programmation-orientee-objet-et-paradigm-aoc-1-4 }

Écrire une fonction `compter_arbres(carte, dx, dy)` qui renvoie le nombre d’arbres rencontrés en se déplaçant de `dx` cases vers la droite et `dy` vers le bas à chaque pas. Tester sur l’exemple de la fiche, puis sur vos données.

??? pouce "Coup de pouce"

    Inutile de recopier la carte vers la droite : la colonne `x` d’une carte infinie correspond à la colonne `x % largeur` de la carte réelle.

??? pouce "Coup de pouce 2 (début de solution)"

    Une boucle `for y in range(0, len(carte), dy)` donne les lignes visitées ; la colonne `x` augmente de `dx` à chaque tour.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Le héros veut comparer plusieurs trajectoires avant de choisir la moins dangereuse.

    - Refaire le comptage pour cinq pentes : (1 à droite, 1 en bas), (3, 1), (5, 1), (7, 1) et (1 à droite, **2** en bas). Pour cette dernière, on saute donc une ligne sur deux.

    - Il faut renvoyer le **produit** des cinq nombres d’arbres obtenus.

### <span class="exo-num">Exercice 5</span> — Plusieurs pentes <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-programmation-orientee-objet-et-paradigm-aoc-1-5 }

Utiliser la fonction précédente pour toutes les pentes demandées et calculer la réponse. Sur l’exemple de la fiche, on doit trouver `72`.

??? pouce "Coup de pouce"

    Ranger les pentes dans une liste de tuples `(dx, dy)` et accumuler dans une variable initialisée à `1` (et non à `0`, puisqu’on multiplie).

??? pouce "Coup de pouce 2 (début de solution)"

    Si la réponse de la partie 2 est fausse alors que la partie 1 est juste, tester la pente qui descend de plus d’une ligne : votre boucle saute-t-elle bien des lignes ?

## Approfondissement

!!! encadre "Outil Python : d’une chaîne à une liste et retour (list, join)"

    Une chaîne n’est pas modifiable : `ligne[2] = "X"` provoque une erreur. On la convertit en liste de caractères, que l’on peut modifier, puis on recolle les morceaux avec `join`, appelée sur le séparateur.

    ```python
    ligne = "..#.."
    cases = [c for c in ligne]        # ['.', '.', '#', '.', '.']
    cases[2] = "X"                    # une liste, elle, se modifie
    print("".join(cases))             # ..X..  (separateur vide)
    print("-".join(["a", "b", "c"]))  # a-b-c
    ```

    **Intérêt.** `join` assemble tous les morceaux en un seul passage, alors que des `+` successifs recopient la chaîne à chaque ajout (coût quadratique sur de longues chaînes).

    **À essayer.** Que se passe-t-il si l’on exécute directement `ligne[2] = "X"` ? Que renvoie `" ".join("abc")` ?

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 6</span> — Défi : visualiser le trajet <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-programmation-orientee-objet-et-paradigm-aoc-1-6 }

Écrire une fonction qui affiche la carte en remplaçant chaque case visitée par `O` (case libre) ou `X` (arbre). Les chaînes n’étant pas modifiables, comment s’y prendre ?

??? pouce "Coup de pouce"

    Convertir chaque ligne en liste avec `[c for c in ligne]`, la modifier, puis la recoller avec `"".join(...)`.

## <span class="etiquette">Défi 2</span> Rain Risk

*la navigation — programmation orientée objet*

<p class="infos-activite">Jour 12</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/02-defi-aoc-2020-12){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-02-defi-aoc-2020-12.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/12 ](https://adventofcode.com/2020/day/12 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/02-defi-aoc-2020-12>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

*Ce défi réinvestit la programmation orientée objet vue dans ce chapitre : une classe, ses attributs et ses méthodes modélisent le navire.*

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

    **Contexte.** Le ferry est pris dans une tempête et son ordinateur de navigation a produit une liste d’ordres très tortueuse. Vous aidez le capitaine à savoir où ces ordres mènent le bateau. Chaque ligne du fichier est un ordre : une lettre (l’action) suivie d’un entier (la quantité), par exemple `N4`.

    **Ce qu’il faut faire.**

    - `N`, `S`, `E`, `W` déplacent le navire de la quantité indiquée vers le nord, le sud, l’est ou l’ouest, **sans** changer la direction vers laquelle il pointe : il se décale comme un crabe.

    - `L` et `R` le font pivoter sur place vers la gauche ou la droite du nombre de degrés indiqué (toujours un multiple de 90 dans les données).

    - `F` le fait avancer de la quantité indiquée, droit devant lui.

    - Au départ, le navire est à l’origine et pointe vers l’est. La réponse est la distance de Manhattan entre l’arrivée et le départ, c’est-à-dire $|x| + |y|$ (comme dans une ville quadrillée, on ne coupe pas en diagonale).

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-programmation-orientee-objet-et-paradigm-aoc-2-1 }

Questions de vérification, à traiter sur le cahier :

1.  Le navire tourné vers l’est exécute `N4` : vers où est-il tourné ensuite ?

2.  En partant de l’est, quelle orientation obtient-on après `R270` ? Après `L180` ?

3.  Un navire termine à 3 unités à l’ouest et 5 au sud : quelle réponse ? Pourquoi des valeurs absolues ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-programmation-orientee-objet-et-paradigm-aoc-2-2 }

On considère les instructions (inventées) suivantes, une par ligne dans le fichier :

```console
N4  F6  L90  F3  R180  W2  F5
```

Suivre le navire sur un quadrillage (est vers la droite, nord vers le haut). Vérification : après `F3`, le navire est à 6 unités à l’est et 7 au nord ; la réponse finale est `6`.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — La classe `Navire` <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-programmation-orientee-objet-et-paradigm-aoc-2-3 }

Écrire une classe `Navire` dont le constructeur initialise la position `x`, `y` (est et nord) et l’orientation sous forme d’un vecteur `dx`, `dy` (vers l’est : `(1, 0)`). Ajouter une méthode `distance(self)` qui renvoie la distance de Manhattan à l’origine.

### <span class="exo-num">Exercice 4</span> — Tourner par quarts de tour <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-programmation-orientee-objet-et-paradigm-aoc-2-4 }

Écrire une méthode `tourner_gauche(self)` qui fait tourner l’orientation d’un quart de tour vers la gauche. Vérifier sur papier : est $\to$ nord $\to$ ouest $\to$ sud $\to$ est. En déduire `tourner(self, sens, angle)` pour les angles 90, 180 et 270.

??? pouce "Coup de pouce"

    Écrire les quatre vecteurs `(1, 0)`, `(0, 1)`, `(-1, 0)`, `(0, -1)` dans l’ordre et chercher comment on passe de l’un au suivant : les coordonnées s’échangent, et l’une change de signe.

??? pouce "Coup de pouce 2 (début de solution)"

    Un quart de tour à gauche transforme `(dx, dy)` en `(-dy, dx)`. Tourner à droite de 90° revient à tourner à gauche de 270°, et `angle // 90` donne le nombre de quarts de tour.

### <span class="exo-num">Exercice 5</span> — Exécuter le fichier <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-programmation-orientee-objet-et-paradigm-aoc-2-5 }

Écrire une méthode `executer(self, instruction)` qui reçoit une chaîne comme `"F6"` et met à jour le navire. Lire le fichier, exécuter toutes les instructions et afficher la distance. Tester sur l’exemple de la fiche, puis sur vos données.

??? pouce "Coup de pouce"

    `instruction[0]` donne la lettre, `int(instruction[1:])` la valeur.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    En relisant le manuel, on découvre que la plupart des ordres ne concernent pas le navire lui-même, mais un point de repère (*waypoint*) qu’il poursuit.

    - Le waypoint est repéré **par rapport au navire** ; au départ, il est à 10 unités à l’est et 1 au nord du navire.

    - `N`, `S`, `E`, `W` déplacent le waypoint ; `L`, `R` le font tourner autour du navire ; `F` $k$ déplace le navire $k$ fois du vecteur navire $\to$ waypoint (le waypoint suit le navire et garde sa position relative). La réponse demandée est la même.

### <span class="exo-num">Exercice 6</span> — Le waypoint <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-programmation-orientee-objet-et-paradigm-aoc-2-6 }

Écrire une classe `NavireRepere` (ou ajouter les attributs `wx`, `wy`) et une méthode `executer2`. Sur l’exemple de la fiche, on doit trouver `70`.

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

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Approfondissement 1 : naviguer avec des nombres complexes <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-programmation-orientee-objet-et-paradigm-aoc-2-8 }

1.  Recopier et exécuter le code de l’encadré. Calculer à la main $1 \times i$, puis $i \times i$, $(-1) \times i$ et $(-i) \times i$ : quelles orientations successives retrouve-t-on ? Par quel nombre faut-il multiplier pour un quart de tour vers la droite ?

2.  Sur l’exemple de la fiche, la position et la direction sont des complexes ; au départ `position = 0` et `direction = 1`. Que valent-elles après `N4`, `F6`, `L90` puis `F3` ?

3.  Écrire une fonction `trajet_complexe(instructions, partie)` qui traite les deux parties ; vérifier qu’on obtient `6` et `70` sur l’exemple.

    ??? pouce "Coup de pouce"

        Un dictionnaire associe à chaque lettre `N`, `S`, `E`, `W` son vecteur unitaire : `1j`, `-1j`, `1`, `-1`.

    ??? pouce "Coup de pouce 2 (début de solution)"

        `L` $k$ : multiplier la direction par `1j ** (k // 90)` ; `R` : par `(-1j) ** (k // 90)`. En partie 2, la variable `direction` joue le rôle du waypoint (au départ `10 + 1j`) : `N`, `S`, `E`, `W` la modifient au lieu de modifier la position.

4.  Pourquoi `abs(position)` ne donne-t-il pas la réponse ? Comparer cette version avec la classe `Navire` : longueur, lisibilité, facilité à corriger.
