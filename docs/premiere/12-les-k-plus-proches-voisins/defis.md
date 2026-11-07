# Défis Advent of Code

<p class="sous-titre">Les k plus proches voisins</p>

## <span class="etiquette">Défi</span> Rope Bridge

*le pont de corde — simulation et généralisation*

<p class="infos-activite">Jour 9</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/12-defi-aoc-2022-09){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-12-defi-aoc-2022-09.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2022/day/9 ](https://adventofcode.com/2022/day/9 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (lien ci-dessus) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - **Attention aux exemples.** L’énoncé en ligne a son propre exemple, avec d’autres réponses. Les valeurs de test de cette fiche portent sur **l’exemple inventé de la fiche** (exercice « À la main ») : l’enregistrer dans un fichier `exemple.txt` à côté du programme, et ouvrir `"exemple.txt"` au lieu de `"input.txt"` pour tester.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

!!! encadre "Le défi en bref"

    **Le problème.** On simule une corde sur une grille : on tire sa tête selon deux mille mouvements, et sa queue suit en restant collée à elle. Il faut compter les cases différentes par lesquelles passe la queue. Comme chaque mouvement se décompose en plusieurs pas et que la queue doit être recalculée après chacun, seul un programme peut suivre la corde jusqu’au bout.

    **Ce qu’on réinvestit.** Une **distance entre deux cases**, comme dans l’algorithme des $k$ plus proches voisins de ce chapitre : ici, deux cases « se touchent » quand le plus grand écart entre leurs coordonnées vaut au plus 1, et c’est ce calcul qui décide si la queue doit bouger. On utilise aussi des p-uplets pour les positions, des fonctions, et en partie 2 une liste de positions.

    **La démarche de la fiche.**

    1.  Comprendre la règle avec des questions courtes, puis simuler à la main quelques mouvements dont on connaît la réponse.

    2.  Lire les mouvements du fichier.

    3.  Écrire une fonction qui fait suivre la queue, puis simuler tous les pas en notant les cases visitées : réponse de la partie 1.

    4.  Pour la partie 2, représenter une corde de dix nœuds par une liste et réutiliser la même fonction pour chaque nœud.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| rope | corde | knot | nœud |
| head / tail | tête / queue | touching | en contact, qui se touchent |
| adjacent | voisin (y compris en diagonale) | overlapping | superposés |
| step | pas | visit at least once | visiter au moins une fois |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Vous traversez un vieux pont de corde, et pour ne pas regarder en bas vous imaginez une corde qui se déplace sur une grille. La corde a deux bouts, la tête et la queue, qui restent toujours proches l’un de l’autre : quand on tire la tête, la queue finit par suivre. On s’intéresse au chemin suivi par la queue.

    **Les données.** Chaque ligne du fichier est un mouvement de la tête, de la forme `D n` : une lettre qui donne la direction (`U` vers le haut, `D` vers le bas, `L` vers la gauche, `R` vers la droite), un espace, puis le nombre `n` de cases à parcourir. Par exemple, `R 4` fait avancer la tête de quatre cases vers la droite.

    **La règle.**

    - Tête et queue partent de la même case.

    - Chaque mouvement `D n` se fait **une case à la fois**, en `n` pas.

    - Après chaque pas de la tête, si la queue la touche encore (même case ou case voisine, diagonales comprises), elle ne bouge pas.

    - Sinon, la queue avance d’une case vers la tête : en ligne droite si elles sont sur la même ligne ou la même colonne, en diagonale sinon. Autrement dit, la queue rattrape la tête en restant collée à elle.

    **La réponse attendue.** Le nombre de cases différentes visitées par la queue, départ compris. Par exemple, avec le seul mouvement `R 3`, la tête arrive trois cases à droite ; la queue reste sur place au premier pas, puis avance d’une case à chacun des deux pas suivants : elle a visité 3 cases, la réponse serait 3.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-les-k-plus-proches-voisins-aoc-1-1 }

**But.** Vérifier sur des cas particuliers qu’on a bien compris quand et comment la queue se déplace.

**À quoi ça sert ?** La première question est le cas le plus délicat (le déplacement en diagonale) ; la deuxième évite l’erreur qui consiste à déplacer la tête de plusieurs cases d’un coup.

Après lecture du résumé (et de l’énoncé), vérifier sa compréhension sur ces cas particuliers :

1.  La tête est en $(2, 1)$ et la queue en $(0, 0)$ : où va la queue ?

2.  Pourquoi faut-il traiter `R 4` comme quatre déplacements d’une case ?

3.  La queue peut-elle se retrouver sur la même case que la tête ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-les-k-plus-proches-voisins-aoc-1-2 }

**But.** Simuler pas à pas cinq mouvements sur papier quadrillé et compter les cases visitées par la queue.

**À quoi ça sert ?** On obtient un exemple dont on **connaît la réponse** (7), qui permettra de tester la simulation. Le faire à la main montre aussi l’ordre des opérations : d’abord la tête, ensuite la queue.

Sur une feuille quadrillée, simuler pas à pas les mouvements (inventés) suivants, la tête et la queue partant de la même case :

```console
R 3
U 2
L 4
D 1
R 2
```

Marquer chaque case par laquelle passe la queue. Vérification : on doit trouver `7` cases.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire les mouvements <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-les-k-plus-proches-voisins-aoc-1-3 }

**But.** Transformer chaque ligne du fichier en un couple `(direction, nombre_de_pas)`.

**À quoi ça sert ?** La simulation parcourra cette liste de couples ; le nombre de pas doit être un entier pour pouvoir servir dans une boucle.

!!! encadre "Outil Python : strip (nettoyer une ligne lue)"

    Chaque ligne lue dans un fichier (avec `for ligne in fichier` ou `readlines()`) se termine par le caractère de fin de ligne `"\n"` (sauf parfois la dernière). `ligne.strip()` renvoie une copie de la ligne sans les espaces ni les fins de ligne placés au début et à la fin.

    ```python
    ligne = "1721\n"
    print(ligne.strip())                  # 1721
    print(len(ligne), len(ligne.strip())) # 5 4
    ```

    **Intérêt.** Comparer ou découper une ligne sans que la fin de ligne ne gêne : `"abc\n" == "abc"` vaut `False`.

Rappel pour lire un fichier ligne par ligne :

```python
fichier = open("input.txt", encoding="utf-8")
for ligne in fichier:
    ligne = ligne.strip()   # enlève le retour à la ligne final
fichier.close()
```

Construire la liste des mouvements sous forme de couples `(direction, nombre_de_pas)`, par exemple `("R", 3)`.

??? pouce "Coup de pouce"

    `d, n = ligne.split()` puis `int(n)`.

### <span class="exo-num">Exercice 4</span> — Faire suivre un nœud <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-les-k-plus-proches-voisins-aoc-1-4 }

**But.** Écrire la fonction `suivre`, qui calcule la nouvelle position de la queue à partir de celle de la tête.

**À quoi ça sert ?** C’est le cœur du défi : la règle de la queue est entièrement dans cette fonction. Elle resservira telle quelle dans la partie 2, où chaque nœud suit celui qui le précède.

Écrire une fonction `suivre(xt, yt, xq, yq)` qui reçoit la position de la tête et celle de la queue, et renvoie la nouvelle position de la queue. Tester les trois situations : en contact, à deux cases en ligne droite, en diagonale « lointaine ».

??? pouce "Coup de pouce"

    La queue doit bouger seulement si `abs(xt - xq) > 1 or abs(yt - yq) > 1`. Dans ce cas, elle se rapproche de la tête d’**au plus une case** dans chaque direction.

??? pouce "Coup de pouce 2 (début de solution)"

    Écrire une petite fonction `signe(n)` qui renvoie `1`, `-1` ou `0`. Si la queue doit bouger : `xq += signe(xt - xq)` et `yq += signe(yt - yq)`. Ce seul calcul couvre la ligne droite **et** la diagonale.

!!! encadre "Rappel : les ensembles (set)"

    Les ensembles sont présentés dans l’encadré « Outil Python : les ensembles » du défi *High-Entropy Passphrases* (chapitre 7). L’essentiel : `set()` crée un ensemble vide, `e.add(x)` ajoute `x` (sans doublon), `len(e)` compte les éléments, et le test `x in e` est quasi instantané, quelle que soit la taille de `e`. Un ensemble peut contenir des p-uplets comme `(0, 0)`.

    *À essayer.* Que vaut `len({(0, 0), (0, 0), (2, 1)})` ?

### <span class="exo-num">Exercice 5</span> — Simuler <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-les-k-plus-proches-voisins-aoc-1-5 }

**But.** Enchaîner tous les pas de la tête, faire suivre la queue après chacun, et noter les cases visitées par la queue.

**À quoi ça sert ?** Le nombre de cases notées est la réponse de la partie 1. La boucle écrite ici sera la base de la simulation de la partie 2.

Simuler tous les mouvements **un pas à la fois** : à chaque pas, déplacer la tête d’une case, faire suivre la queue, et noter la case de la queue dans une liste sans doublon (ou un ensemble, voir l’encadré). Vérifier `7` sur l’exemple.

??? pouce "Coup de pouce"

    Pour `("U", 2)`, on fait deux tours de boucle, chacun déplaçant la tête d’une seule case. Décider du sens du repère (par exemple `y` augmente vers le haut) et s’y tenir.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    **Ce qui change.** Le pont tremble et la corde imaginaire s’allonge : elle n’a plus deux bouts seulement, mais **10 nœuds** alignés les uns derrière les autres.

    **La nouvelle règle.**

    - Le premier nœud est la tête ; il se déplace comme dans la partie 1, selon les mouvements du fichier, une case à la fois.

    - Chacun des 9 autres nœuds suit le nœud qui le précède, avec exactement la même règle que la queue de la partie 1.

    - Tous les nœuds partent de la même case.

    **La réponse attendue.** Le nombre de cases différentes visitées par le **dernier** nœud, départ compris. Par exemple, avec le seul mouvement `R 3`, le mouvement s’amortit le long de la corde avant d’arriver au bout : le dernier nœud ne bouge pas, et la réponse serait 1.

### <span class="exo-num">Exercice 6</span> — Une corde plus longue <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-les-k-plus-proches-voisins-aoc-1-6 }

**But.** Représenter la corde par une liste de positions et faire suivre chaque nœud par le suivant.

**À quoi ça sert ?** On ne réécrit pas la règle : la fonction `suivre` de la partie 1 s’applique à chaque paire de nœuds voisins. Avec une liste de 2 nœuds, on doit d’ailleurs retrouver la réponse de la partie 1, ce qui fournit un test gratuit.

Généraliser : la corde est maintenant représentée par une **liste de positions** `noeuds`, `noeuds[0]` étant la tête. Répondre à la nouvelle question. Sur l’exemple inventé de la fiche, la réponse de la partie 2 est `1` ; sur les mouvements `U 6`, `R 12`, `D 9`, `L 15`, on doit trouver `39` pour la partie 1 et `11` pour la partie 2.

??? pouce "Coup de pouce"

    Chaque nœud suit celui qui le précède, exactement avec la fonction `suivre` de la partie 1 : le nœud d’indice `i` joue le rôle de la queue, celui d’indice `i - 1` le rôle de la tête.

??? pouce "Coup de pouce 2 (début de solution)"

    À chaque pas : déplacer `noeuds[0]`, puis `for i in range(1, len(noeuds)):` `noeuds[i] = suivre(...)` en utilisant `noeuds[i - 1]`. La case à noter est celle du **dernier** nœud, `noeuds[-1]`. Avec une liste de 2 nœuds, on doit retrouver la partie 1.

## Approfondissement

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : un ensemble de cases visitées <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-les-k-plus-proches-voisins-aoc-1-7 }

**But.** Ranger les cases visitées dans un ensemble plutôt que dans une liste, et estimer le gain de temps.

**À quoi ça sert ?** Avec des milliers de cases visitées, le test d’appartenance sur une liste devient coûteux : on mesure concrètement l’intérêt de choisir la bonne structure de données.

1.  Réécrire la simulation de la partie 2 en rangeant les cases visitées dans un ensemble plutôt que dans une liste. Quel test devient inutile ?

    ??? pouce "Coup de pouce"

        `visitees = {(0, 0)}` puis `visitees.add(noeuds[-1])` à chaque pas.

2.  Si la queue visite environ $6\,000$ cases, combien de comparaisons le test `in` sur une liste coûte-t-il au total, à peu près ? Et avec un ensemble ?

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 8</span> — Approfondissement 2 : voir la corde <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-les-k-plus-proches-voisins-aoc-1-8 }

**But.** Afficher la corde sur une petite grille après chaque mouvement, puis expliquer un comportement propre à la partie 2.

**À quoi ça sert ?** Visualiser une simulation est un excellent moyen de vérifier qu’elle se comporte comme prévu ; on comprend aussi pourquoi une corde longue présente des situations qui n’existent pas avec deux nœuds.

1.  Écrire une fonction qui affiche la corde sur une petite grille (le numéro de chaque nœud, des points ailleurs) et l’utiliser après chaque ligne de mouvements de l’exemple.

    ??? pouce "Coup de pouce"

        Parcourir les lignes de haut en bas (`y` décroissant) ; pour chaque case, chercher si un nœud s’y trouve.

2.  Pourquoi, dans la partie 2, un nœud peut-il se retrouver à deux cases en diagonale de son prédécesseur, ce qui n’arrive jamais avec deux nœuds ?

    ??? pouce "Coup de pouce"

        Dans la partie 1, la tête ne bouge jamais en diagonale. Dans la partie 2, le nœud 1 peut bouger en diagonale et entraîner le nœud 2 de façon nouvelle.
