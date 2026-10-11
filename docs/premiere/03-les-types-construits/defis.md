# Défis Advent of Code

<p class="sous-titre">Les types construits</p>

## <span class="etiquette">Défi</span> Binary Diagnostic

*le diagnostic du sous-marin — représentation binaire des entiers*

<p class="infos-activite">Jour 3</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/03-defi-aoc-2021-03){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-03-defi-aoc-2021-03.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2021/day/3 ](https://adventofcode.com/2021/day/3 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (lien ci-dessus) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

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

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-les-types-construits-aoc-1-1 }

Après lecture du résumé (et de l’énoncé), vérifier sa compréhension sur ces cas particuliers :

1.  Avec un nombre impair de lignes, une colonne peut-elle avoir autant de `0` que de `1` ?

2.  Pourquoi ne faut-il pas convertir `"00110"` en entier dès la lecture si l’on veut garder les colonnes ?

3.  Les nombres $\gamma$ et $\varepsilon$ ont-ils toujours des bits opposés ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-les-types-construits-aoc-1-2 }

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

### <span class="exo-num">Exercice 3</span> — Lire le fichier <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-les-types-construits-aoc-1-3 }

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

### <span class="exo-num">Exercice 4</span> — Compter une colonne <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-les-types-construits-aoc-1-4 }

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

### <span class="exo-num">Exercice 5</span> — Gamma, epsilon et conversion <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-les-types-construits-aoc-1-5 }

Construire les chaînes `gamma` et `epsilon` colonne par colonne, puis calculer la réponse. Pour convertir, écrire d’abord votre propre fonction `binaire_vers_entier(s)` ; vérifier ensuite avec la fonction toute faite `int(s, 2)`.

??? pouce "Coup de pouce"

    Le bit le plus fréquent est `"1"` si le nombre de uns dépasse la moitié du nombre de lignes. Pour la conversion, on peut ajouter les puissances de 2 comme dans le cours, ou utiliser cette astuce plus courte : partir de `n = 0` puis, pour chaque bit de gauche à droite, `n = 2 * n + int(bit)`.

??? pouce "Coup de pouce 2 (début de solution)"

    `gamma = ""` puis, pour `k` de `0` à `len(nombres[0]) - 1` : comparer `nb_uns(nombres, k)` à `len(nombres) - nb_uns(nombres, k)` et ajouter `"1"` ou `"0"` à `gamma` (l’inverse pour `epsilon`).

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    On vérifie ensuite le système de survie, à partir de deux valeurs obtenues par élimination. On examine les colonnes de gauche à droite ; à chaque colonne, on ne garde que les nombres dont le bit vaut le bit le plus fréquent (première valeur) ou le moins fréquent (seconde valeur), **calculé sur les nombres restants**. On s’arrête quand il n’en reste qu’un. En cas d’égalité, on garde `1` pour la première valeur et `0` pour la seconde. Réponse : le produit des deux valeurs en base 10.

### <span class="exo-num">Exercice 6</span> — Filtrer la liste <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-les-types-construits-aoc-1-6 }

Écrire une fonction `filtrer(nombres, k, bit)` qui renvoie la nouvelle liste des seuls nombres dont le bit d’indice `k` vaut `bit`. Puis écrire une fonction qui applique le procédé de la partie 2 colonne après colonne jusqu’à ce qu’il ne reste qu’un nombre. Lire très attentivement la règle en cas d’**égalité** : elle n’est pas la même pour les deux valeurs. Sur l’exemple du défi, on doit trouver `22` et `6`, donc la réponse `132`.

??? pouce "Coup de pouce"

    Le bit majoritaire se recalcule à chaque étape sur la liste **restante**, pas sur la liste de départ.

??? pouce "Coup de pouce 2 (début de solution)"

    Une boucle `while len(liste) > 1:` avec un indice `k` qui augmente de 1 à chaque tour ; à chaque tour, compter les uns de la colonne `k` dans `liste`, choisir le bit à garder, puis `liste = filtrer(liste, k, bit_garde)`.

## Approfondissement

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : sans chaînes <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-les-types-construits-aoc-1-7 }

1.  À la main : avec 5 bits, quel est le bit de poids $2^2$ de $22 = \texttt{10110}_2$ ? Calculer $(22 \mathbin{//} 4) \bmod 2$ et comparer.

2.  Refaire la partie 1 en convertissant chaque ligne en entier dès la lecture, et en obtenant le bit de poids $2^p$ par des calculs.

    ??? pouce "Coup de pouce"

        Le bit de poids $2^p$ de `n` est `(n // 2**p) % 2`. Pour `gamma`, ajouter $2^p$ quand ce bit est majoritaire.

3.  Comment obtenir `epsilon` à partir de `gamma` par une seule soustraction ?

    ??? pouce "Coup de pouce 2 (début de solution)"

        Avec $m$ bits, `gamma + epsilon` s’écrit avec $m$ chiffres `1`, c’est-à-dire $2^m - 1$.
