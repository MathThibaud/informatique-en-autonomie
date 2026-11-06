# Défis Advent of Code

<p class="sous-titre">Réseaux</p>

## <span class="etiquette">Défi</span> Lobby Layout

*le carrelage hexagonal — ensembles, coordonnées et automate*

<p class="infos-activite">Jour 24</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/09-defi-aoc-2020-24){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-09-defi-aoc-2020-24.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/24 ](https://adventofcode.com/2020/day/24 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (lien ci-dessus) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

!!! encadre "Le défi en bref"

    **Le problème.** Un sol est pavé de carreaux hexagonaux, blancs d’un côté et noirs de l’autre. Le fichier indique des centaines de carreaux à retourner, chacun désigné par un chemin à suivre depuis le centre. On veut compter les carreaux noirs, puis faire évoluer le motif pendant 100 jours. Le pavage est infini et les chemins sont longs : il faut un programme, et surtout une bonne façon de repérer une case hexagonale.

    **Ce qu’on réinvestit.** La notion de **voisins dans un graphe**, vue au chapitre 8 : chaque carreau du pavage a exactement six voisins. Un bon système de **coordonnées** transforme chaque direction en un déplacement à additionner, et un **ensemble** ne garde que les carreaux noirs d’un pavage infini. La partie 2 fait évoluer tous les carreaux en même temps, comme les sièges du défi *Seating System* (chapitre 4).

    **La démarche de la fiche.**

    1.  Comprendre comment se lisent les chemins et quand un carreau finit noir, puis suivre quelques chemins sur un dessin.

    2.  Découper une ligne en directions, puis choisir des coordonnées pour calculer la case d’arrivée.

    3.  Retourner les carreaux dans un ensemble de carreaux noirs : sa taille est la réponse de la partie 1.

    4.  Faire évoluer le pavage jour après jour en comptant les voisins noirs (partie 2).

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

    **Contexte.** Enfin arrivé à l’hôtel, vous trouvez le hall en travaux : il faut poser un carrelage hexagonal formant un motif précis. Chaque carreau est blanc d’un côté et noir de l’autre. Les ouvriers ont une liste des carreaux à retourner, mais ils ont besoin de vous pour savoir à quoi ressemblera le motif.

    **Les données.** Le sol est un pavage infini de carreaux hexagonaux, disposés en rangées horizontales : chaque carreau a six voisins, dans les directions `e` (est), `se` (sud-est), `sw` (sud-ouest), `w` (ouest), `nw` (nord-ouest) et `ne` (nord-est). Chaque ligne du fichier est un chemin : une suite de ces directions collées, sans séparateur, comme `seswnee`.

    **La règle.**

    - Au départ, tous les carreaux sont blancs.

    - Pour chaque ligne, on part toujours du même carreau de référence et l’on suit les directions une à une, de voisin en voisin.

    - Le carreau d’arrivée est retourné : blanc devient noir, noir devient blanc. Les carreaux traversés en chemin ne changent pas.

    - Plusieurs lignes peuvent désigner le même carreau par des chemins différents : il est alors retourné plusieurs fois.

    **La réponse attendue.** Le nombre de carreaux noirs une fois toutes les lignes traitées. Par exemple, avec les trois lignes `ee`, `w` et `ee`, le carreau désigné par `ee` est retourné deux fois et redevient blanc ; seul celui désigné par `w` est noir : la réponse serait 1.

### <span class="exo-num">Exercice 1</span> — Vérifier sa compréhension <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-reseaux-aoc-1-1 }

**But.** Comprendre comment se lisent les directions et ce que deviennent les carreaux désignés plusieurs fois.

**À quoi ça sert ?** La première question prépare le découpage des lignes ; la deuxième montre qu’il faut repérer les carreaux par une position, et non par le chemin qui y mène.

1.  Pourquoi `ne` ne peut-il pas être lu comme `n` puis `e` ?

2.  Deux lignes différentes peuvent-elles désigner le même carreau ? Un carreau désigné trois fois finit-il noir ou blanc ?

3.  Le carreau de référence peut-il être retourné ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-reseaux-aoc-1-2 }

**But.** Découper quelques chemins et les suivre sur un dessin de grille hexagonale.

**À quoi ça sert ?** On découvre que des chemins différents peuvent arriver au même carreau, et l’on obtient une réponse connue (`6`) pour tester le programme.

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

### <span class="exo-num">Exercice 3</span> — Découper une ligne <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-reseaux-aoc-1-3 }

**But.** Transformer une ligne comme `seswnee` en liste de directions.

**À quoi ça sert ?** Les directions sont collées et n’ont pas toutes la même longueur : une fois la liste obtenue, suivre le chemin devient une simple boucle.

Écrire une fonction `directions(ligne)` qui renvoie la liste des directions d’une ligne. Tester sur `seswnee`.

??? pouce "Coup de pouce"

    Parcourir la chaîne avec un indice `i` dans une boucle `while` : si le caractère est `n` ou `s`, la direction occupe deux caractères, sinon un seul.

### <span class="exo-num">Exercice 4</span> — Des coordonnées <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-reseaux-aoc-1-4 }

**But.** Associer à chaque direction un déplacement, puis calculer la position du carreau désigné par une ligne.

**À quoi ça sert ?** C’est le point clé du défi : avec de bonnes coordonnées, deux chemins qui mènent au même carreau donnent la même position, et l’on peut alors repérer chaque carreau sans dessiner la grille.

**Avant de coder**, choisir un système de coordonnées (lire l’encadré) et écrire, pour chacune des six directions, le déplacement correspondant. Vérifier sur un dessin que `nw` puis `se`, ou `e`, `nw` puis `sw`, ramènent au point de départ. Écrire alors une fonction `position(ligne)` qui renvoie les coordonnées du carreau désigné.

??? pouce "Coup de pouce"

    Un dictionnaire `DEPLACEMENTS` qui associe à chaque direction un couple `(dx, dy)` rend la fonction très courte.

!!! encadre "Méthode : retourner un carreau avec un ensemble (set)"

    Les ensembles sont présentés dans l’encadré « Outil Python : les ensembles » du défi *Crab Combat* (chapitre 4) ; rappel : éléments non modifiables, donc une position `(q, r)` convient. On ne garde que les carreaux **noirs** : retourner un carreau, c’est l’ajouter à l’ensemble s’il n’y est pas, l’en retirer sinon.

    ```python
    def retourner(noirs, p):
        """Retourne le carreau p : blanc -> noir, noir -> blanc."""
        if p in noirs:
            noirs.remove(p)
        else:
            noirs.add(p)

    noirs = set()              # ensemble vide (attention : {} est un dict)
    noirs.add((3, 0))
    print((3, 0) in noirs)     # True
    retourner(noirs, (1, 1))   # (1, 1) absent : il est ajoute
    retourner(noirs, (3, 0))   # (3, 0) present : il est retire
    print(noirs)               # {(1, 1)}
    ```

    **Intérêt.** Le test `p in noirs` se fait en temps constant ; avec une liste, chaque test `p in liste` parcourrait toute la liste. Question : que contient `noirs` si l’on appelle trois fois `retourner(noirs, (0, 0))` à partir d’un ensemble vide ?

### <span class="exo-num">Exercice 5</span> — Retourner les carreaux <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-reseaux-aoc-1-5 }

**But.** Tenir à jour l’ensemble des carreaux noirs en traitant toutes les lignes.

**À quoi ça sert ?** C’est la réponse de la partie 1 (la taille de l’ensemble) ; cet ensemble est aussi l’état de départ de la partie 2.

Gérer l’ensemble `noirs` des coordonnées des carreaux noirs et répondre à la partie 1.

??? pouce "Coup de pouce"

    Retourner un carreau, c’est l’ajouter à l’ensemble s’il n’y est pas, l’en retirer sinon : c’est la fonction `retourner` de l’encadré.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    **Ce qui change.** Le motif n’est pas figé : il évolue de jour en jour selon une règle simple. On part du carrelage obtenu en partie 1.

    **La nouvelle règle.**

    - Chaque jour, on compte les voisins noirs de chaque carreau dans l’état de la veille, puis tous les carreaux changent **en même temps**.

    - Un carreau noir ayant $0$ ou plus de $2$ voisins noirs devient blanc.

    - Un carreau blanc ayant exactement $2$ voisins noirs devient noir.

    - Les autres carreaux ne changent pas.

    **La réponse attendue.** Le nombre de carreaux noirs après 100 jours. Par exemple, si seuls deux carreaux voisins étaient noirs, ils le resteraient (un voisin noir chacun) et les deux carreaux qui les touchent tous les deux deviendraient noirs : 4 carreaux noirs le lendemain.

!!! encadre "Méthode : compter avec un dictionnaire"

    Pour compter les apparitions de chaque valeur, on associe à chaque valeur rencontrée son nombre d’apparitions. À la première rencontre, la clé n’existe pas encore : on la crée avec la valeur `1`.

    ```python
    compte = {}
    for case in [(0, 1), (2, 0), (0, 1)]:
        if case in compte:
            compte[case] += 1
        else:
            compte[case] = 1
    print(compte)              # {(0, 1): 2, (2, 0): 1}
    print((5, 5) in compte)    # False : case jamais rencontree
    ```

    **Intérêt.** Une seule lecture de la liste suffit, et le test `case in compte` se fait en temps constant. Question : que se passerait-il sans le test, avec seulement `compte[case] = compte[case] + 1` ?

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Un automate cellulaire <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-reseaux-aoc-1-6 }

**But.** Calculer l’ensemble des carreaux noirs du lendemain, puis répéter cent fois.

**À quoi ça sert ?** C’est la réponse de la partie 2. Comme le pavage est infini, toute la difficulté est de n’examiner que les carreaux susceptibles de changer, et de compter leurs voisins noirs efficacement.

Écrire une fonction `jour_suivant(noirs)` qui renvoie le nouvel ensemble des carreaux noirs. Sur l’exemple du défi, on doit trouver `9` carreaux noirs après un jour, `10` après deux jours et `53` après dix jours.

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

!!! encadre "Méthode : additionner deux positions coordonnée par coordonnée"

    Une position à 2 ou à 3 coordonnées se range dans un tuple. Pour lui ajouter un déplacement, on parcourt les indices des coordonnées avec une **compréhension de liste**, puis on reconvertit le résultat en tuple pour pouvoir le ranger dans un ensemble.

    ```python
    pos = (1, -2, 1)
    pas = (0, 1, -1)
    somme = [pos[k] + pas[k] for k in range(len(pos))]
    print(somme)                          # [1, -1, 0]
    nouvelle = tuple(somme)               # (1, -1, 0) : rangeable dans un ensemble
    ```

    **Intérêt.** Grâce à `len(pos)`, le même code additionne des positions à 2 ou à 3 coordonnées. Question : que se passe-t-il si `pos` vaut `(1, 2, 3)` et `pas` vaut `(10, 20)` ?

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : d’autres systèmes de coordonnées <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-reseaux-aoc-1-7 }

**But.** Résoudre le défi avec d’autres repérages des cases hexagonales, et les comparer.

**À quoi ça sert ?** Le choix d’une représentation conditionne la simplicité du code : on voit qu’une même fonction peut servir pour plusieurs systèmes, et que les coordonnées cubiques donnent en plus une formule de distance.

1.  **Coordonnées cubiques.** On repère une case par $(x, y, z)$ avec $x + y + z = 0$ ; on choisit `e` $= (1, -1, 0)$ et `ne` $= (1, 0, -1)$. Trouver les quatre autres déplacements, sachant que `w` est l’opposé de `e` et que faire `e` puis `nw` revient à faire `ne`. Calculer à la main la position de `seswnee`.

2.  Écrire une fonction `position_systeme(ligne, deplacements)` qui fonctionne avec n’importe quel dictionnaire de déplacements (2 ou 3 coordonnées). Vérifier qu’on trouve encore `6` carreaux noirs sur l’exemple du défi.

    ??? pouce "Coup de pouce"

        Partir de la liste `[0] * len(deplacements["e"])` et, à chaque pas, additionner coordonnée par coordonnée (voir l’encadré). Renvoyer un tuple, pour pouvoir le ranger dans un ensemble.

3.  **Coordonnées doublées.** Avec `e` $= (2, 0)$ et `ne` $= (1, -1)$, trouver les autres déplacements. Montrer que $x + y$ est toujours pair. Retrouver le résultat de la partie 1.

4.  **Distance.** En coordonnées cubiques, on admet que le nombre minimal de pas pour aller du centre à la case $(x, y, z)$ est $\max(|x|, |y|, |z|)$. Vérifier sur `eee` et `seswnee`. Quel est, sur l’exemple, le carreau noir le plus éloigné du centre ?

    ??? pouce "Coup de pouce"

        Un pas modifie deux coordonnées d’une unité chacune, en sens contraires : il ne peut faire baisser $\max(|x|, |y|, |z|)$ que d’au plus 1.

5.  Comparer les trois systèmes : nombre de coordonnées, facilité de vérification, calcul des voisins pour la partie 2.
