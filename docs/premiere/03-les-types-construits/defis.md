# Défis Advent of Code

<p class="sous-titre">Les types construits</p>

## <span class="etiquette">Défi 1</span> Calorie Counting

*les provisions des elfes — sommes par groupes et maximum*

<p class="infos-activite">Jour 1</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/03-defi-aoc-2022-01){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-03-defi-aoc-2022-01.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2022/day/1 ](https://adventofcode.com/2022/day/1 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (facultatif), le lien *get your puzzle input* donne **vos** données, à enregistrer sous `input.txt` à côté du programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/03-defi-aoc-2022-01>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

*Ce défi réinvestit les tableaux vus dans ce chapitre : construction avec `append`, parcours, recherche du maximum.*

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| to carry | porter, transporter | item | objet, aliment |
| inventory | inventaire, liste des provisions | blank line | ligne vide |
| to separate | séparer | previous | précédent |
| the most | le plus | how many | combien |
| puzzle input | vos données (fichier personnel) | star | étoile (une par partie réussie) |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Une expédition d’elfes part à pied dans la jungle chercher des fruits magiques. Avant le départ, chaque elfe a noté la valeur énergétique (en calories) de chacun des aliments qu’il emporte. Le fichier rassemble toutes ces notes : chaque nombre est un aliment, et chaque bloc de nombres correspond aux provisions d’un même elfe.

    **Ce qu’il faut faire.**

    - Le fichier contient un entier par ligne. Une **ligne vide** marque le passage d’un elfe au suivant ; il n’y en a pas après le dernier elfe.

    - Le total d’un elfe est la somme des nombres de son bloc (un elfe peut n’avoir qu’un seul aliment).

    - On veut savoir quel elfe est le mieux approvisionné : la réponse est le **plus grand total**, c’est-à-dire la valeur de ce total, et non le numéro de l’elfe.

### <span class="exo-num">Exercice 1</span> — Vérifier sa compréhension <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-les-types-construits-aoc-1-1 }

Questions pièges, à traiter sur le cahier :

1.  Que doit faire le programme quand il lit une ligne vide ? Et quand il arrive à la fin du fichier ?

2.  Si deux elfes ont le même plus grand total, la réponse change-t-elle ?

3.  Un elfe n’a qu’un seul nombre : quel est son total ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-les-types-construits-aoc-1-2 }

On considère le fichier (inventé) suivant, à recopier aussi dans un fichier `exemple.txt`.

Combien d’elfes ce fichier décrit-il ? Calculer le total de chacun, puis la réponse attendue. Vérification : on doit obtenir `7200`.

```console
3000
1500

7200

2500
2500
1000

4100
900

6400
```

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire le fichier ligne par ligne <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-les-types-construits-aoc-1-3 }

Voici comment lire un fichier texte en Python :

```python
fichier = open("exemple.txt")
for ligne in fichier:
    ligne = ligne.strip()   # retire le retour a la ligne "\n" de la fin
    print(ligne, len(ligne))
fichier.close()
```

Exécuter ce programme. Que vaut `ligne` quand la ligne du fichier est vide ? Que faut-il faire pour obtenir le **nombre** `3000` et non la chaîne `"3000"` ?

??? pouce "Coup de pouce"

    Une ligne vide donne la chaîne vide `""`, de longueur 0. La fonction `int` transforme la chaîne `"3000"` en l’entier `3000`.

### <span class="exo-num">Exercice 4</span> — Le total de chaque elfe <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-les-types-construits-aoc-1-4 }

Écrire une fonction `totaux(nom_fichier)` qui renvoie la liste des totaux des elfes, dans l’ordre du fichier. Sur l’exemple : `[4500, 7200, 6000, 5000, 6400]`.

??? pouce "Coup de pouce"

    Garder une variable `total` qui commence à 0. Pour chaque ligne : si elle est vide, l’elfe est terminé (on range `total` dans la liste et on repart de 0) ; sinon on ajoute `int(ligne)` à `total`.

??? pouce "Coup de pouce 2 (début de solution)"

    `liste = []` et `total = 0` avant la boucle ; dans la boucle : `if ligne == "":` puis `liste.append(total)` et `total = 0`, `else:` `total += int(ligne)`. Attention : le dernier elfe n’est suivi d’aucune ligne vide, il faut donc ajouter `total` une dernière fois **après** la boucle.

### <span class="exo-num">Exercice 5</span> — Le plus grand total <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-les-types-construits-aoc-1-5 }

Écrire une fonction `maximum(liste)` qui renvoie le plus grand élément d’une liste non vide, **sans** utiliser `max`. Vérifier qu’elle donne le même résultat que `max`, puis répondre à la partie 1 sur vos données.

??? pouce "Coup de pouce"

    Partir du premier élément comme « meilleur provisoire », puis parcourir la liste : dès qu’un élément est plus grand, il devient le nouveau meilleur.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    On ne veut plus dépendre d’un seul elfe en cas de fringale : on s’intéresse maintenant aux trois elfes les mieux approvisionnés. Le fichier se découpe en elfes exactement comme avant ; la réponse est la **somme des trois plus grands totaux**.

!!! encadre "Outil Python : retirer un élément d’un tableau (remove)"

    La méthode `remove` retire d’un tableau la **première** occurrence d’une valeur. Elle modifie le tableau : pour garder l’original intact, on travaille sur une copie.

    ```python
    t = [40, 10, 50, 10]
    copie = list(t)          # une vraie copie (et non un alias)
    copie.remove(10)         # copie vaut [40, 50, 10] ; t n'a pas change
    print(t, copie)
    ```

    **Intérêt.** Après avoir trouvé le maximum, on peut le retirer et chercher le maximum de ce qui reste. Question : que se passe-t-il avec `copie.remove(99)` ?

### <span class="exo-num">Exercice 6</span> — La partie 2 <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-les-types-construits-aoc-1-6 }

Adapter le programme pour répondre à la nouvelle question : chercher le plus grand total, le retirer d’une copie du tableau, puis recommencer. Sur l’exemple de la fiche, on doit trouver `19600`.

??? pouce "Coup de pouce"

    Réutiliser la fonction `maximum`. Le deuxième plus grand total est le maximum du tableau privé du plus grand.

??? pouce "Coup de pouce 2 (début de solution)"

    `copie = list(liste)` et `somme = 0` ; puis trois fois (`for i in range(3):`) : `m = maximum(copie)`, `somme += m`, `copie.remove(m)`.

## Approfondissement

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : en un seul parcours <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-les-types-construits-aoc-1-7 }

La méthode de la partie 2 parcourt le tableau trois fois (et le copie). On peut faire mieux.

1.  On parcourt la liste des totaux de l’exemple, `[4500, 7200, 6000, 5000, 6400]`, en tenant à jour trois variables `premier`, `deuxieme`, `troisieme` (toutes à 0 au départ). Écrire sur le cahier leurs valeurs après chaque élément.

2.  Écrire une fonction `trois_plus_grands_sans_tri(liste)` qui fait ce travail en un **seul** parcours et renvoie la somme des trois variables.

    ??? pouce "Coup de pouce"

        Quand un total dépasse `premier`, l’ancien premier devient deuxième et l’ancien deuxième devient troisième. Traiter ensuite les cas « dépasse seulement `deuxieme` » et « dépasse seulement `troisieme` ».

    ??? pouce "Coup de pouce 2 (début de solution)"

        `if x > premier:` décaler dans cet ordre : `troisieme = deuxieme`, puis `deuxieme = premier`, puis `premier = x`. Ensuite `elif x > deuxieme:` … et `elif x > troisieme:` …

3.  Pourquoi l’ordre des trois affectations est-il important ?

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Approfondissement 2 : les $k$ plus grands <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-les-types-construits-aoc-1-8 }

On veut généraliser : la somme des $k$ plus grands totaux, pour un entier $k$ quelconque.

1.  Écrire une fonction `k_plus_grands(liste, k)` qui généralise la méthode de la partie 2. Vérifier qu’avec $k = 3$, on retrouve la réponse de la partie 2.

    ??? pouce "Coup de pouce"

        Remplacer le 3 de la boucle par le paramètre `k`.

2.  Que doit renvoyer `k_plus_grands(t, 1)` ? Et `k_plus_grands(t, len(t))` ? Vérifier.

3.  Le tableau contient $n$ totaux. Combien de comparaisons fait environ `k_plus_grands` ? Est-ce raisonnable pour $k = 3$ ? pour $k = n$ ?

## <span class="etiquette">Défi 2</span> Binary Diagnostic

*le diagnostic du sous-marin — représentation binaire des entiers*

<p class="infos-activite">Jour 3</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/03-defi-aoc-2021-03){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-03-defi-aoc-2021-03.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2021/day/3 ](https://adventofcode.com/2021/day/3 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/03-defi-aoc-2021-03>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

*Ce défi réinvestit l’écriture binaire des entiers (chapitre précédent) avec les tableaux de ce chapitre.*

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| diagnostic report | rapport de diagnostic | binary number | nombre en binaire |
| bit | chiffre binaire (0 ou 1) | position | position, rang |
| most common | le plus fréquent | least common | le moins fréquent |
| rate | taux | power consumption | consommation électrique |
| rating | valeur, note | keep / discard | garder / écarter |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Le sous-marin fait des bruits inquiétants, et l’on demande son rapport de diagnostic. Ce rapport est une liste de nombres binaires, tous de même longueur, un par ligne. On ne lit pas ces nombres un par un : on les étudie colonne par colonne pour en déduire deux nombres qui mesurent la consommation électrique du sous-marin.

    **Ce qu’il faut faire.**

    - Le nombre $\gamma$ (*gamma*) se construit bit par bit : son bit en position $k$ est le bit **le plus fréquent** dans la colonne $k$ du rapport.

    - Le nombre $\varepsilon$ (*epsilon*) se construit de même avec le bit **le moins fréquent** de chaque colonne. Autrement dit, $\varepsilon$ s’écrit avec les bits contraires de ceux de $\gamma$.

    - Réponse : le produit des valeurs **en base 10** de $\gamma$ et $\varepsilon$.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-les-types-construits-aoc-2-1 }

Après lecture du résumé (et de l’énoncé), vérifier sa compréhension sur ces cas particuliers :

1.  Avec un nombre impair de lignes, une colonne peut-elle avoir autant de `0` que de `1` ?

2.  Pourquoi ne faut-il pas convertir `"00110"` en entier dès la lecture si l’on veut garder les colonnes ?

3.  Les nombres $\gamma$ et $\varepsilon$ ont-ils toujours des bits opposés ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-les-types-construits-aoc-2-2 }

On considère le fichier (inventé) suivant :

```console
10110
01100
11101
10011
00110
11100
10101
```

Pour chaque colonne, compter les `1` et les `0`. Écrire le *gamma rate* et l’*epsilon rate* en binaire, puis les convertir en base 10 à la main (poids $16, 8, 4, 2, 1$). Vérification : on doit obtenir $20$ et $11$, et la réponse `220`.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire le fichier <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-les-types-construits-aoc-2-3 }

Rappel pour lire un fichier ligne par ligne :

```python
fichier = open("input.txt", encoding="utf-8")
for ligne in fichier:
    ligne = ligne.strip()   # enlève le retour à la ligne final
fichier.close()
```

Construire la liste `nombres` des lignes, **gardées sous forme de chaînes** : on a besoin d’accéder à chaque bit.

??? pouce "Coup de pouce"

    Si l’on convertissait tout de suite en entier, la ligne `"00110"` deviendrait `110` et l’on perdrait les zéros de tête.

### <span class="exo-num">Exercice 4</span> — Compter une colonne <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-les-types-construits-aoc-2-4 }

Écrire une fonction `nb_uns(nombres, k)` qui renvoie le nombre de lignes dont le bit d’indice `k` vaut `"1"`. Sur l’exemple, `nb_uns(nombres, 0)` vaut `5`.

??? pouce "Coup de pouce"

    Un compteur et une boucle sur la liste ; le bit d’indice `k` de la chaîne `s` est `s[k]`. Attention : on compare à la **chaîne** `"1"`, pas à l’entier `1`.

!!! encadre "Outil Python : conversions binaires (int(s, 2), bin)"

    Python sait convertir directement entre l’écriture binaire et un entier. `int(s, 2)` lit la chaîne `s` comme un nombre écrit en base 2 ; `bin(n)` donne l’écriture binaire de `n`, précédée de `0b`.

    ```python
    print(int("10100", 2))     # 20 : la chaine est lue en base 2
    print(int("00110", 2))     # 6 : les zeros de tete ne genent pas
    print(bin(20))             # 0b10100 : ecriture binaire, prefixe 0b
    print(bin(20)[2:])         # 10100 : sans le prefixe
    ```

    **Intérêt.** Ces fonctions servent à **vérifier** votre propre conversion. Écrire la conversion soi-même (méthode du cours) reste l’objectif de l’exercice.

    *À essayer.* Que renvoient `int("11111", 2)` et `bin(11)` ?

### <span class="exo-num">Exercice 5</span> — Gamma, epsilon et conversion <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-les-types-construits-aoc-2-5 }

Construire les chaînes `gamma` et `epsilon` colonne par colonne, puis calculer la réponse. Pour convertir, écrire d’abord votre propre fonction `binaire_vers_entier(s)` ; vérifier ensuite avec la fonction toute faite `int(s, 2)`.

??? pouce "Coup de pouce"

    Le bit le plus fréquent est `"1"` si le nombre de uns dépasse la moitié du nombre de lignes. Pour la conversion, on peut ajouter les puissances de 2 comme dans le cours, ou utiliser cette astuce plus courte : partir de `n = 0` puis, pour chaque bit de gauche à droite, `n = 2 * n + int(bit)`.

??? pouce "Coup de pouce 2 (début de solution)"

    `gamma = ""` puis, pour `k` de `0` à `len(nombres[0]) - 1` : comparer `nb_uns(nombres, k)` à `len(nombres) - nb_uns(nombres, k)` et ajouter `"1"` ou `"0"` à `gamma` (l’inverse pour `epsilon`).

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    On vérifie ensuite le système de survie, à partir de deux valeurs obtenues par élimination. On examine les colonnes de gauche à droite ; à chaque colonne, on ne garde que les nombres dont le bit vaut le bit le plus fréquent (première valeur) ou le moins fréquent (seconde valeur), **calculé sur les nombres restants**. On s’arrête quand il n’en reste qu’un. En cas d’égalité, on garde `1` pour la première valeur et `0` pour la seconde. Réponse : le produit des deux valeurs en base 10.

### <span class="exo-num">Exercice 6</span> — Filtrer la liste <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-les-types-construits-aoc-2-6 }

Écrire une fonction `filtrer(nombres, k, bit)` qui renvoie la nouvelle liste des seuls nombres dont le bit d’indice `k` vaut `bit`. Puis écrire une fonction qui applique le procédé de la partie 2 colonne après colonne jusqu’à ce qu’il ne reste qu’un nombre. Lire très attentivement la règle en cas d’**égalité** : elle n’est pas la même pour les deux valeurs. Sur l’exemple de la fiche, on doit trouver `22` et `6`, donc la réponse `132`.

??? pouce "Coup de pouce"

    Le bit majoritaire se recalcule à chaque étape sur la liste **restante**, pas sur la liste de départ.

??? pouce "Coup de pouce 2 (début de solution)"

    Une boucle `while len(liste) > 1:` avec un indice `k` qui augmente de 1 à chaque tour ; à chaque tour, compter les uns de la colonne `k` dans `liste`, choisir le bit à garder, puis `liste = filtrer(liste, k, bit_garde)`.

## Approfondissement

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : sans chaînes <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-les-types-construits-aoc-2-7 }

1.  À la main : avec 5 bits, quel est le bit de poids $2^2$ de $22 = \texttt{10110}_2$ ? Calculer $(22 \mathbin{//} 4) \bmod 2$ et comparer.

2.  Refaire la partie 1 en convertissant chaque ligne en entier dès la lecture, et en obtenant le bit de poids $2^p$ par des calculs.

    ??? pouce "Coup de pouce"

        Le bit de poids $2^p$ de `n` est `(n // 2**p) % 2`. Pour `gamma`, ajouter $2^p$ quand ce bit est majoritaire.

3.  Comment obtenir `epsilon` à partir de `gamma` par une seule soustraction ?

    ??? pouce "Coup de pouce 2 (début de solution)"

        Avec $m$ bits, `gamma + epsilon` s’écrit avec $m$ chiffres `1`, c’est-à-dire $2^m - 1$.
