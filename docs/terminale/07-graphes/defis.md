# Défis Advent of Code

<p class="sous-titre">Graphes</p>

## <span class="etiquette">Défi 1</span> Jurassic Jigsaw

*le puzzle d’images — grilles, rotations et symétries*

<p class="infos-activite">Jour 20</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/07-defi-aoc-2020-20){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-07-defi-aoc-2020-20.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/20 ](https://adventofcode.com/2020/day/20 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/07-defi-aoc-2020-20>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

*Ce défi réinvestit les graphes de ce chapitre : les tuiles en sont les sommets, et deux tuiles qui partagent un bord sont reliées par une arête. L’approfondissement assemble l’image par un parcours de ce graphe.*

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| tile | tuile, morceau d’image | reassemble | réassembler |
| rotated / flipped | tourné / retourné (en miroir) | border / edge | bord |
| line up | coïncider, s’aligner | outermost | le plus à l’extérieur |
| corner | coin | ID number | numéro d’identification |
| sea monster | monstre marin (motif à chercher) | roughness | rugosité (partie 2) |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Les messages du satellite contiennent en fait une photo, mais l’appareil l’a envoyée découpée en petits carrés (des « tuiles »), mélangés et, pire, tournés ou retournés au hasard. Il faut reconstituer ce puzzle. Chaque bloc du fichier est une tuile en noir et blanc, avec son numéro.

    **Ce qu’il faut faire.**

    - Un bloc est une ligne `Tile <numéro>:` suivie d’une grille carrée de $10 \times 10$ caractères `.` ou `#` ; les blocs sont séparés par une ligne vide.

    - Remises dans le bon sens, les tuiles forment une image carrée. Chaque tuile a pu être tournée d’un nombre quelconque de quarts de tour et/ou retournée en miroir.

    - Deux tuiles voisines dans l’image ont, une fois bien orientées, des bords identiques : c’est ce qui permet de les raccorder. Les bords extérieurs de l’image ne correspondent à aucune autre tuile (en pratique, deux tuiles non voisines n’ont jamais de bord commun).

    - Réponse : le produit des numéros des quatre tuiles placées aux coins de l’image.

### <span class="exo-num">Exercice 1</span> — Vérifier sa compréhension <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-graphes-aoc-1-1 }

1.  Deux bords qui se correspondent peuvent apparaître « à l’envers » l’un par rapport à l’autre : pourquoi ?

2.  Combien de bords sans correspondant a une tuile de coin ? une tuile du bord de l’image ? une tuile intérieure ?

3.  Faut-il reconstituer toute l’image pour la partie 1 ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-graphes-aoc-1-2 }

Voici deux tuiles inventées de taille $5\times 5$ :

```console
Tuile A
#.#..
#.#..
#...#
.#.##
#....
```

```console
Tuile B
.#...
##.##
###.#
....#
.#.##
```

1.  Écrire les quatre bords de chaque tuile sous forme de chaînes, en lisant toujours de gauche à droite (haut, bas) ou de haut en bas (gauche, droite).

2.  Montrer qu’un seul bord de A coïncide avec un bord de B, à condition de lire l’un des deux à l’envers. Vérification : il s’agit du bord droit de A et du bord gauche de B.

3.  Pour placer B à droite de A, B doit-il être tourné, retourné, ou laissé tel quel ?

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire les tuiles <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-graphes-aoc-1-3 }

Construire un dictionnaire `tuiles` qui associe à chaque numéro (un entier) la tuile sous forme de liste de chaînes. Vérifier le nombre de tuiles : est-ce un carré parfait ?

??? pouce "Coup de pouce"

    Les tuiles sont séparées par une ligne vide : `split("\n\n")`. La première ligne d’un bloc donne le numéro (enlever le texte et le `:`).

!!! encadre "Outils Python : lire une chaîne à l’envers, assembler, comparer ([::-1], join, min)"

    `s[::-1]` est la tranche qui parcourt `s` avec un pas de $-1$ : c’est la chaîne à l’envers. `"".join(...)` colle bout à bout des chaînes (ici des caractères) en une seule. Enfin `min` et `<` comparent les chaînes dans l’ordre « alphabétique » des caractères (l’ordre de leurs codes : `#` vient avant `.`).

    ```python
    tuile = ["#.#", "..#", "##."]
    print(tuile[0][::-1])                         # "#.#" lu a l'envers : "#.#"
    print("..#"[::-1])                            # "#.."
    gauche = "".join(ligne[0] for ligne in tuile) # premier caractere de chaque ligne
    print(gauche)                                 # "#.#"
    print("-".join(["a", "b", "c"]))              # "a-b-c" : le separateur est au choix
    print(min("..#", "#.."))                      # "#.." car "#" < "."
    ```

    **Intérêt.** Avec `min(b, b[::-1])`, un bord et son inverse donnent **la même** chaîne : on peut alors les ranger sous une seule clé de dictionnaire. Question : écrire le bord droit de cette tuile avec `join`. Que vaut `min("##.", ".##")` ?

### <span class="exo-num">Exercice 4</span> — Les bords <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-graphes-aoc-1-4 }

Écrire une fonction `bords(tuile)` qui renvoie la liste des quatre bords. Puis compter, pour chaque bord de chaque tuile, combien d’*autres* tuiles possèdent ce bord, à l’endroit ou à l’envers.

??? pouce "Coup de pouce"

    `"".join(ligne[0] for ligne in tuile)` donne le bord gauche ; `chaine[::-1]` lit une chaîne à l’envers.

### <span class="exo-num">Exercice 5</span> — Les coins <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-graphes-aoc-1-5 }

Une tuile de coin a exactement deux bords qui ne correspondent à aucune autre tuile. Repérer les quatre coins et calculer la réponse.

??? pouce "Coup de pouce"

    Construire un dictionnaire qui associe à chaque bord, mis sous une forme *canonique* (le plus petit, dans l’ordre alphabétique, entre le bord et son inverse : `min(b, b[::-1])`), la liste des tuiles qui le possèdent. Un bord de tuile est « libre » si cette liste n’a qu’un élément.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site. Cette partie est **longue** : la découper en étapes et tester chacune.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Une fois l’image reconstituée, on y cherche des monstres marins.

    - Assembler l’image, retirer le bord (première et dernière lignes et colonnes) de chaque tuile, puis recoller les tuiles : chacune devient un carré $8 \times 8$.

    - Chercher un motif (le « monstre », dessiné sur le site) dans l’une des 8 orientations de l’image : chaque `#` du motif doit tomber sur un `#` de l’image, les autres cases sont quelconques.

    - Réponse : le nombre de `#` de l’image qui n’appartiennent à aucun monstre.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Assembler l’image <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-graphes-aoc-1-6 }

Écrire `rotation(tuile)` (quart de tour) et `symetrie(tuile)` (miroir), puis `orientations(tuile)` qui renvoie les huit positions possibles (lire l’encadré). Assembler ensuite toute l’image en suivant la stratégie de l’encadré.

??? pouce "Coup de pouce"

    Tester `rotation` sur la tuile A : quatre rotations successives doivent redonner A, et `orientations(A)` doit contenir 8 tuiles toutes différentes.

??? pouce "Coup de pouce 2 (début de solution)"

    Pour une liste de chaînes `t` de taille $n$, la ligne `j` de la tuile tournée d’un quart de tour dans le sens horaire est formée des caractères `t[n - 1 - i][j]` pour `i` de `0` à `n - 1`.

!!! encadre "Outils Python : all et les ensembles (set)"

    `all(...)` renvoie `True` si tous les tests qu’on lui donne sont vrais (et s’arrête au premier faux). Un **ensemble** est une collection sans doublon et sans ordre ; on y ajoute avec `add`, on réunit deux ensembles avec `|`, et le test `x in ensemble` est très rapide.

    ```python
    image = ["#.#", "###"]
    cases = [(0, 0), (1, 1)]
    print(all(image[i][j] == "#" for i, j in cases))   # True
    couvertes = set()                    # ensemble vide (attention : {} est un dict)
    couvertes.add((0, 0))
    couvertes |= {(0, 0), (1, 1)}        # reunion : (0, 0) n'est pas compte deux fois
    print(len(couvertes))                # 2
    print((1, 1) in couvertes)           # True
    ```

    **Intérêt.** Si deux monstres se chevauchaient, une case commune ne serait comptée qu’une fois dans l’ensemble. Question : que renvoie `all(image[i][j] == "#" for i, j in [(0, 0), (0, 1)])` ?

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Chercher le motif <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-graphes-aoc-1-7 }

Retirer les bords de chaque tuile, recoller l’image, puis chercher le motif dans chacune de ses huit orientations. Calculer la réponse demandée.

??? pouce "Coup de pouce"

    Stocker le motif comme une liste de décalages `(ligne, colonne)` des cases `#` ; le motif est présent à la position `(i, j)` si (avec `all`) toutes les cases `(i + dl, j + dc)` de l’image sont des `#`. Une seule orientation de l’image contient des motifs.

## Pour y arriver : orientations et assemblage

!!! encadre "Les huit orientations d’une grille carrée"

    Un carré peut être tourné de $0$, $1$, $2$ ou $3$ quarts de tour : cela fait 4 positions. On peut aussi le retourner (miroir gauche-droite) avant de le tourner : 4 positions de plus. Toute autre transformation (miroir haut-bas, miroir selon une diagonale) redonne l’une de ces 8 positions : par exemple, le miroir haut-bas est un miroir gauche-droite suivi d’un demi-tour. Il suffit donc de deux fonctions, `rotation` et `symetrie`, pour toutes les obtenir.

!!! encadre "Stratégie d’assemblage pas à pas"

    1.  Prendre un coin trouvé en partie 1 et chercher l’orientation où ses deux bords libres sont en haut et à gauche : il sera la case $(0, 0)$.

    2.  Remplir la première ligne de gauche à droite : pour la case suivante, chercher parmi les tuiles non placées celle qui, dans l’une de ses 8 orientations, a un bord gauche égal au bord droit de la tuile précédente.

    3.  Pour les lignes suivantes, chaque tuile doit avoir son bord haut égal au bord bas de la tuile du dessus.

    4.  Grâce à la partie 1, on sait que chaque bord intérieur n’est partagé que par deux tuiles : à chaque étape, il y a donc une seule tuile possible.

## Approfondissement

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Approfondissement 1 : assembler par un parcours <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-graphes-aoc-1-8 }

La stratégie de la fiche part d’un coin et remplit l’image ligne par ligne. On peut aussi partir de **n’importe quelle** tuile, laissée telle quelle à la position $(0, 0)$, et propager : pour chaque tuile placée, on cherche ses voisines par ses quatre bords, on les oriente et on les place à côté. Les positions peuvent devenir négatives ; on « recadre » à la fin.

1.  À la main, avec les tuiles A et B de la fiche : A est placée telle quelle en $(0, 0)$. À quelle position va B, et dans quelle orientation ? Quelle serait la position de B si l’on avait placé B en premier ?

2.  Écrire `assembler_parcours(tuiles)` qui utilise une **pile** des tuiles placées mais pas encore traitées, et un dictionnaire `place` qui associe à chaque position `(ligne, colonne)` la tuile orientée. Vérifier qu’on obtient la même réponse à la partie 2.

    ??? pouce "Coup de pouce"

        Pour le côté droit d’une tuile `t` placée en `(l, c)` : la voisine (si elle existe et n’est pas encore placée) va en `(l, c + 1)`, dans l’orientation dont le bord **gauche** est égal au bord droit de `t`. Idem pour les trois autres côtés.

    ??? pouce "Coup de pouce 2 (début de solution)"

        Une liste `COTES` de quadruplets `(dl, dc, mon_bord, son_bord)`, par exemple `(0, 1, droite, gauche)`, évite d’écrire quatre fois le même code (les fonctions sont des valeurs comme les autres). Recadrage : soustraire à toutes les positions le plus petit numéro de ligne et le plus petit numéro de colonne.

3.  Cette méthode suppose qu’aucun bord n’est un palindrome (une chaîne égale à son inverse). Pourquoi ? La méthode de la fiche a-t-elle le même défaut ?

4.  Comparer les deux méthodes : nombre de tuiles examinées, longueur du code. Quel parcours de graphe reconnaît-on ?

## <span class="etiquette">Défi 2</span> Allergen Assessment

*les allergènes — ensembles, intersections et élimination*

<p class="infos-activite">Jour 21</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/07-defi-aoc-2020-21){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-07-defi-aoc-2020-21.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/21 ](https://adventofcode.com/2020/day/21 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/07-defi-aoc-2020-21>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

*Ce défi peut se lire avec les graphes de ce chapitre : relier chaque allergène aux ingrédients qui peuvent le contenir donne un graphe, et l’élimination retire des arêtes jusqu’à ce qu’il n’en reste qu’une par allergène.*

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|                 |                    |                |                        |
|:----------------|:-------------------|:---------------|:-----------------------|
| ingredient      | ingrédient         | allergen       | allergène              |
| food            | aliment            | contains       | contient               |
| listed / marked | indiqué, mentionné | safe           | sans danger            |
| exactly one     | exactement un      | zero or one    | zéro ou un             |
| dangerous       | dangereux          | alphabetically | par ordre alphabétique |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Pour rejoindre votre île, vous construisez un radeau et devez emporter des provisions. Problème : les étiquettes des aliments sont écrites dans une langue inconnue, seuls certains allergènes sont indiqués dans une langue que vous comprenez. Chaque ligne du fichier décrit un aliment : sa liste d’ingrédients (illisibles) et quelques-uns des allergènes qu’il contient.

    **Ce qu’il faut faire.**

    - Une ligne contient des ingrédients séparés par des espaces, puis `(contains` suivi d’allergènes séparés par des virgules, et `)`.

    - Chaque allergène se trouve dans exactement un ingrédient ; un ingrédient contient zéro ou un allergène.

    - Si un allergène est indiqué sur une ligne, l’ingrédient qui le contient figure sur cette ligne. Mais un allergène peut être présent dans un aliment sans y être indiqué : l’absence de mention ne prouve rien.

    - Trouver les ingrédients qui ne peuvent contenir aucun allergène. Réponse : le nombre total de leurs apparitions (un ingrédient présent sur trois lignes compte trois fois).

### <span class="exo-num">Exercice 1</span> — Vérifier sa compréhension <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-graphes-aoc-2-1 }

1.  Un allergène est indiqué sur deux lignes : où peut se trouver l’ingrédient qui le contient ?

2.  Un ingrédient absent d’une ligne qui indique `milk` peut-il contenir `milk` ?

3.  Un ingrédient présent sur une ligne qui n’indique pas `milk` peut-il contenir `milk` ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-graphes-aoc-2-2 }

On considère le fichier (inventé) suivant :

```console
brak zuli monto pirf (contains gluten, milk)
zuli kesa tolu (contains gluten)
monto tolu brak vemi (contains eggs)
tolu pirf zuli (contains gluten, eggs)
kesa zuli brak (contains milk)
```

1.  Pour l’allergène `gluten`, quels ingrédients figurent sur *toutes* les lignes qui le mentionnent ? Faire de même pour `eggs` et `milk`.

2.  En déduire les ingrédients qui ne peuvent contenir aucun allergène, et la réponse de la partie 1. Vérification : on doit trouver `7`.

3.  L’ingrédient `monto` figure sur une ligne qui mentionne `milk`. Pourquoi est-il pourtant sans danger ?

## Programmer la partie 1

!!! encadre "Outil Python : les ensembles (set) et leurs opérations"

    Un **ensemble** est une collection **sans doublon** et **sans ordre** (pas d’indice). Python fournit les opérations des mathématiques : intersection `&` (éléments communs), réunion `|` (éléments de l’un ou de l’autre), différence `-` (éléments du premier qui ne sont pas dans le second).

    ```python
    a = set("brak zuli monto".split())   # {'brak', 'zuli', 'monto'}
    b = {"zuli", "kesa", "brak"}
    print(a & b)          # {'brak', 'zuli'}   intersection
    print(a | b)          # 4 elements          reunion
    print(a - b)          # {'monto'}           difference
    print("kesa" in b)    # True : test tres rapide
    b.add("tolu")         # ajout (sans effet si deja present)
    b.discard("kesa")     # retrait (sans erreur si absent)
    x = b.pop()           # retire et renvoie un element quelconque
    vide = set()          # attention : {} est un dictionnaire vide
    ```

    **Intérêt.** Ces opérations s’écrivent en une ligne et sont rapides : tester si un élément appartient à un ensemble prend un temps qui ne dépend pas de sa taille, contrairement à une liste. Question : recopier ce code ; que vaut `b - a` après les deux premières lignes ? Et `len(a & set())` ?

### <span class="exo-num">Exercice 3</span> — Lire le fichier <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-graphes-aoc-2-3 }

Construire la liste `aliments` : chaque aliment est un couple `(ingredients, allergenes)` de deux ensembles de chaînes.

??? pouce "Coup de pouce"

    `ligne.split(" (contains ")` sépare les deux parties ; il reste à enlever la parenthèse finale avec `rstrip(")")` puis à couper selon `", "`.

### <span class="exo-num">Exercice 4</span> — Les candidats <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-graphes-aoc-2-4 }

Écrire une fonction `candidats(aliments)` qui renvoie un dictionnaire associant à chaque allergène l’ensemble des ingrédients qui peuvent le contenir. Tester sur l’exemple.

??? pouce "Coup de pouce"

    L’ingrédient qui contient un allergène est présent sur chaque ligne où cet allergène est indiqué : il est donc dans l’**intersection** (opérateur `&`) des ensembles d’ingrédients de ces lignes.

### <span class="exo-num">Exercice 5</span> — Compter <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-graphes-aoc-2-5 }

Calculer l’ensemble des ingrédients « suspects » (réunion des candidats), puis compter les apparitions des autres ingrédients dans le fichier.

??? pouce "Coup de pouce"

    Réunion de plusieurs ensembles : partir de `set()` et lui réunir chaque ensemble de candidats avec `|`. Pour compter, la différence `ingredients - suspects` donne, sur chaque ligne, les ingrédients sans danger ; attention, on compte chaque apparition sur chaque ligne.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Il reste à identifier les ingrédients dangereux pour pouvoir les éviter. Déterminer, pour chaque allergène, l’ingrédient qui le contient (la solution est unique). Réponse : la liste de ces ingrédients, rangés dans l’ordre alphabétique de leur **allergène** (et non de leur nom), séparés par des virgules sans espace.

!!! encadre "Outil Python : assembler des chaînes (join)"

    `separateur.join(liste)` colle les chaînes de la liste en intercalant le séparateur.

    ```python
    mots = ["tolu", "zuli", "brak"]
    print(",".join(mots))           # tolu,zuli,brak
    print(" - ".join(mots))         # tolu - zuli - brak
    print(",".join(sorted(mots)))   # brak,tolu,zuli  (ordre alphabetique)
    ```

    **Intérêt.** C’est plus simple (et plus rapide) qu’une boucle qui ajoute les mots un par un, et l’on n’a pas de virgule en trop à la fin. Question : que donne `"".join(["a", "b"])` ?

### <span class="exo-num">Exercice 6</span> — Attribuer chaque allergène <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-graphes-aoc-2-6 }

Déterminer quel ingrédient contient chaque allergène, puis construire la chaîne demandée. Sur l’exemple de la fiche, on doit obtenir `tolu,zuli,brak`.

??? pouce "Coup de pouce"

    C’est le même raisonnement qu’un sudoku : un allergène qui n’a plus qu’un seul candidat est résolu, et cet ingrédient peut être retiré des candidats de tous les autres allergènes.

??? pouce "Coup de pouce 2 (début de solution)"

    Tant que le dictionnaire des candidats n’est pas vide : chercher un allergène dont l’ensemble a une seule valeur, le retirer du dictionnaire (`pop`) en notant l’ingrédient dans un dictionnaire `attribution`, puis faire `discard(ingredient)` sur tous les autres ensembles. Penser à trier par **allergène** pour la réponse.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Défi : et si ça bloquait ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-graphes-aoc-2-7 }

Inventer un petit fichier pour lequel la méthode d’élimination ne suffit pas : à un moment, aucun allergène n’a un seul candidat. Que faudrait-il faire alors ?

??? pouce "Coup de pouce"

    Essayer avec deux allergènes indiqués toujours ensemble, sur les mêmes lignes : le problème a-t-il encore une seule solution ? Dans les cas où la solution est unique mais où l’élimination bloque, on peut tester les possibilités une à une (retour sur trace).
