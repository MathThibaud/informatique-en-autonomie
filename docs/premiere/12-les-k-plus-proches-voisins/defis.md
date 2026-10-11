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

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

*Ce défi fait intervenir une distance entre deux cases, comme l’algorithme des $k$ plus proches voisins de ce chapitre : ici, deux cases « se touchent » quand le plus grand écart entre leurs coordonnées vaut au plus 1.*

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| rope | corde | knot | nœud |
| head / tail | tête / queue | touching | en contact, qui se touchent |
| adjacent | voisin (y compris en diagonale) | overlapping | superposés |
| step | pas | visit at least once | visiter au moins une fois |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Vous traversez un vieux pont de corde, et pour ne pas regarder en bas vous imaginez une corde qui se déplace sur une grille. La corde a deux bouts, la tête et la queue ; quand on tire la tête, la queue finit par suivre. Le fichier donne la suite des déplacements de la tête, et l’on s’intéresse au chemin suivi par la queue.

    **Ce qu’il faut faire.**

    - Tête et queue partent de la même case. Chaque ligne `D n` déplace la tête de `n` cases, **une à la fois**, vers le haut, le bas, la gauche ou la droite (`U`, `D`, `L`, `R`).

    - Après chaque pas de la tête, si la queue la touche encore (même case ou case voisine, diagonales comprises), elle ne bouge pas. Sinon, elle avance d’une case vers la tête : en ligne droite si elles sont sur la même ligne ou colonne, en diagonale sinon. Autrement dit, la queue rattrape la tête en restant collée à elle.

    - Réponse : le nombre de cases différentes visitées par la queue, départ compris.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-les-k-plus-proches-voisins-aoc-1-1 }

Après lecture du résumé (et de l’énoncé), vérifier sa compréhension sur ces cas particuliers :

1.  La tête est en $(2, 1)$ et la queue en $(0, 0)$ : où va la queue ?

2.  Pourquoi faut-il traiter `R 4` comme quatre déplacements d’une case ?

3.  La queue peut-elle se retrouver sur la même case que la tête ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-les-k-plus-proches-voisins-aoc-1-2 }

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

Écrire une fonction `suivre(xt, yt, xq, yq)` qui reçoit la position de la tête et celle de la queue, et renvoie la nouvelle position de la queue. Tester les trois situations : en contact, à deux cases en ligne droite, en diagonale « lointaine ».

??? pouce "Coup de pouce"

    La queue doit bouger seulement si `abs(xt - xq) > 1 or abs(yt - yq) > 1`. Dans ce cas, elle se rapproche de la tête d’**au plus une case** dans chaque direction.

??? pouce "Coup de pouce 2 (début de solution)"

    Écrire une petite fonction `signe(n)` qui renvoie `1`, `-1` ou `0`. Si la queue doit bouger : `xq += signe(xt - xq)` et `yq += signe(yt - yq)`. Ce seul calcul couvre la ligne droite **et** la diagonale.

!!! encadre "Rappel : les ensembles (set)"

    Les ensembles sont présentés dans l’encadré « Outil Python : les ensembles » du défi *High-Entropy Passphrases* (chapitre 7). L’essentiel : `set()` crée un ensemble vide, `e.add(x)` ajoute `x` (sans doublon), `len(e)` compte les éléments, et le test `x in e` est quasi instantané, quelle que soit la taille de `e`. Un ensemble peut contenir des p-uplets comme `(0, 0)`.

    *À essayer.* Que vaut `len({(0, 0), (0, 0), (2, 1)})` ?

### <span class="exo-num">Exercice 5</span> — Simuler <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-les-k-plus-proches-voisins-aoc-1-5 }

Simuler tous les mouvements **un pas à la fois** : à chaque pas, déplacer la tête d’une case, faire suivre la queue, et noter la case de la queue dans une liste sans doublon (ou un ensemble, voir l’encadré). Vérifier `7` sur l’exemple.

??? pouce "Coup de pouce"

    Pour `("U", 2)`, on fait deux tours de boucle, chacun déplaçant la tête d’une seule case. Décider du sens du repère (par exemple `y` augmente vers le haut) et s’y tenir.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Le pont tremble et la corde imaginaire s’allonge. Elle a maintenant **10 nœuds** : la tête, puis 9 nœuds qui suivent chacun celui qui le précède, avec exactement la même règle que la queue de la partie 1. Réponse : le nombre de cases différentes visitées par le **dernier** nœud.

### <span class="exo-num">Exercice 6</span> — Une corde plus longue <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-les-k-plus-proches-voisins-aoc-1-6 }

Généraliser : la corde est maintenant représentée par une **liste de positions** `noeuds`, `noeuds[0]` étant la tête. Répondre à la nouvelle question. Sur l’exemple du défi, la réponse de la partie 2 est `1` ; sur les mouvements `U 6`, `R 12`, `D 9`, `L 15`, on doit trouver `39` pour la partie 1 et `11` pour la partie 2.

??? pouce "Coup de pouce"

    Chaque nœud suit celui qui le précède, exactement avec la fonction `suivre` de la partie 1 : le nœud d’indice `i` joue le rôle de la queue, celui d’indice `i - 1` le rôle de la tête.

??? pouce "Coup de pouce 2 (début de solution)"

    À chaque pas : déplacer `noeuds[0]`, puis `for i in range(1, len(noeuds)):` `noeuds[i] = suivre(...)` en utilisant `noeuds[i - 1]`. La case à noter est celle du **dernier** nœud, `noeuds[-1]`. Avec une liste de 2 nœuds, on doit retrouver la partie 1.

## Approfondissement

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : un ensemble de cases visitées <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-les-k-plus-proches-voisins-aoc-1-7 }

1.  Réécrire la simulation de la partie 2 en rangeant les cases visitées dans un ensemble plutôt que dans une liste. Quel test devient inutile ?

    ??? pouce "Coup de pouce"

        `visitees = {(0, 0)}` puis `visitees.add(noeuds[-1])` à chaque pas.

2.  Si la queue visite environ $6\,000$ cases, combien de comparaisons le test `in` sur une liste coûte-t-il au total, à peu près ? Et avec un ensemble ?

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 8</span> — Approfondissement 2 : voir la corde <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-les-k-plus-proches-voisins-aoc-1-8 }

1.  Écrire une fonction qui affiche la corde sur une petite grille (le numéro de chaque nœud, des points ailleurs) et l’utiliser après chaque ligne de mouvements de l’exemple.

    ??? pouce "Coup de pouce"

        Parcourir les lignes de haut en bas (`y` décroissant) ; pour chaque case, chercher si un nœud s’y trouve.

2.  Pourquoi, dans la partie 2, un nœud peut-il se retrouver à deux cases en diagonale de son prédécesseur, ce qui n’arrive jamais avec deux nœuds ?

    ??? pouce "Coup de pouce"

        Dans la partie 1, la tête ne bouge jamais en diagonale. Dans la partie 2, le nœud 1 peut bouger en diagonale et entraîner le nœud 2 de façon nouvelle.
