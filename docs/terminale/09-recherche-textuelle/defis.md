# Défis Advent of Code

<p class="sous-titre">Recherche textuelle</p>

## <span class="etiquette">Défi</span> Monster Messages

*les messages du satellite — grammaires et récursivité*

<p class="infos-activite">Jour 19</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/09-defi-aoc-2020-19){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-09-defi-aoc-2020-19.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/19 ](https://adventofcode.com/2020/day/19 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/09-defi-aoc-2020-19>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

*Ce défi prolonge la recherche textuelle de ce chapitre : on ne cherche plus un motif fixe dans un texte, mais on vérifie si des messages entiers respectent des règles. L’approfondissement 2 réinvestit la mémoïsation du chapitre 8.*

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| rule / sub-rule | règle / sous-règle | to match | correspondre à, être reconnu par |
| pipe (\|) | barre verticale (« ou ») | corrupted | corrompu, abîmé |
| build upon | s’appuyer sur | completely | entièrement |
| loop | boucle | unmatched | non reconnu, en trop |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Arrivé dans une forêt, vous êtes contacté par les elfes : un satellite leur envoie des messages, mais la liaison est mauvaise et beaucoup arrivent abîmés. Pour trier, ils disposent de règles qui décrivent exactement à quoi ressemble un message correct. Le fichier contient ces règles, puis les messages reçus.

    **Ce qu’il faut faire.**

    - Les règles sont numérotées (`numéro: définition`, une par ligne) ; une ligne vide les sépare des messages, formés des lettres `a` et `b`.

    - Une règle « lettre » (`"a"`) reconnaît exactement ce caractère.

    - Une règle composée est une suite de numéros : le texte doit se découper en morceaux consécutifs reconnus, dans l’ordre, par ces sous-règles. Le symbole `|` sépare des alternatives : il suffit que l’une d’elles convienne. Autrement dit, les règles s’emboîtent comme des briques, de la lettre jusqu’à la règle `0`.

    - En partie 1, aucune règle ne fait appel à elle-même, directement ou par l’intermédiaire d’autres règles.

    - Un message est valide si la règle `0` le reconnaît **en entier**, sans caractère en trop. Réponse : le nombre de messages valides.

### <span class="exo-num">Exercice 1</span> — Vérifier sa compréhension <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-recherche-textuelle-aoc-1-1 }

1.  Une même règle peut-elle apparaître deux fois dans une définition ? Le choix d’alternative est-il alors forcément le même ?

2.  Devant une règle à deux alternatives, peut-on garder la première qui reconnaît un début du texte et oublier l’autre ?

3.  Les règles sont-elles forcément rangées dans l’ordre des numéros ? Quelle structure de données évite de s’en soucier ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-recherche-textuelle-aoc-1-2 }

On considère les règles (inventées) suivantes :

```console
0: 1 2
1: 3 3 | 4
2: 4 3 | 3 1
3: "a"
4: "b"
```

1.  Écrire tous les mots reconnus par la règle `1`, puis par la règle `2`.

2.  En déduire tous les mots reconnus par la règle `0`. Vérification : il y en a `6`.

3.  Parmi `aaab`, `bba`, `baab`, `aba` et `bbaa`, lesquels sont acceptés ? Que se passe-t-il pour `bbaa` ?

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire le fichier <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-recherche-textuelle-aoc-1-3 }

Lire `input.txt` et construire un dictionnaire `regles` : à chaque numéro (une chaîne, par exemple `’2’`), on associe soit la lettre (`’a’`), soit la liste des alternatives, chacune étant une liste de numéros (`[[’4’, ’3’], [’3’, ’1’]]`). Construire aussi la liste `messages`.

??? pouce "Coup de pouce"

    Le fichier se coupe en deux avec `split("\n\n")`. Pour une règle, `split(": ")` sépare le numéro du reste, puis `split(" | ")` sépare les alternatives.

!!! encadre "Outil Python : tester le type d’une valeur (isinstance)"

    Dans le dictionnaire `regles`, une valeur est soit une chaîne (une lettre), soit une liste d’alternatives. Pour savoir dans quel cas on est, `isinstance(x, str)` renvoie `True` si `x` est une chaîne ; de même avec `list`, `int`…

    ```python
    regles = {"3": "a", "2": [["4", "3"], ["3", "1"]]}
    print(isinstance(regles["3"], str))    # True : regle "lettre"
    print(isinstance(regles["2"], str))    # False
    print(isinstance(regles["2"], list))   # True : liste d'alternatives
    ```

    **Intérêt.** Cela évite de stocker une information supplémentaire (« type de règle ») : la valeur elle-même dit de quoi il s’agit. Question : que renvoie `isinstance(["a"], str)` ?

### <span class="exo-num">Exercice 4</span> — Reconnaître un message <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-recherche-textuelle-aoc-1-4 }

Écrire une fonction récursive `fins(regles, num, message, i)` qui renvoie la **liste des positions** où peut se terminer un morceau du message commençant à l’indice `i` et reconnu par la règle `num` (lire l’encadré). Un message est accepté si `len(message)` figure dans `fins(regles, ’0’, message, 0)`. Tester sur l’exemple, puis compter les messages acceptés.

??? pouce "Coup de pouce"

    Cas de base : une règle « lettre » renvoie `[i + 1]` si `message[i]` est cette lettre (et `i` dans les bornes), et `[]` sinon.

??? pouce "Coup de pouce 2 (début de solution)"

    Pour une alternative `[’4’, ’3’]` : partir de `positions = [i]` ; pour chaque sous-règle, remplacer `positions` par la liste de toutes les fins obtenues depuis chacune des positions. Les résultats des différentes alternatives sont mis bout à bout.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Les elfes s’aperçoivent que deux de leurs règles étaient fausses et vous envoient les bonnes : `8: 42 | 42 8` et `11: 42 31 | 42 11 31`. Ces règles font appel à elles-mêmes : la règle `8` reconnaît une ou plusieurs répétitions de la règle `42`, et la règle `11` reconnaît $k$ fois la règle `42` suivie de $k$ fois la règle `31` ($k \geq 1$). Réponse : le nouveau nombre de messages valides.

### <span class="exo-num">Exercice 5</span> — Des règles récursives <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-recherche-textuelle-aoc-1-5 }

Deux règles sont remplacées par des règles qui **s’appellent elles-mêmes**. Modifier le dictionnaire comme indiqué et relancer le comptage. Votre fonction `fins` fonctionne-t-elle encore ? Pourquoi ne boucle-t-elle pas indéfiniment ?

??? pouce "Coup de pouce"

    Observer où apparaît le numéro de la règle dans sa propre définition : jamais en première position. Avant chaque appel récursif, au moins une lettre a donc été consommée.

Exemple de test (inventé ; en partie 2, on remplace les règles `8` et `11` comme dans le résumé) :

```console
0: 8 11
8: 42
11: 42 31
42: 1 1 | 2 1
31: 1 2 | 2 2
1: "a"
2: "b"

aabaab
aaaaab
aaaabaabbb
aaabab
baaaaaab
abaaab
babaabab
```

Avec les règles d’origine, on doit compter `2` messages ; avec les règles modifiées, `4`.

## Pour y arriver : grammaires et récursivité <span class="horsprog">au-delà du programme</span>

!!! encadre "Grammaire, expression régulière et positions de fin"

    **Grammaire.** Les règles de l’énoncé forment une *grammaire* : chaque règle décrit un ensemble de mots à partir d’autres règles, comme « une phrase est un groupe nominal suivi d’un verbe ». On dit qu’un mot est *reconnu* s’il peut être obtenu en partant de la règle `0`.

    **Pourquoi pas une expression régulière ?** En partie 1, on peut remplacer chaque numéro par sa définition jusqu’à n’avoir que des lettres et obtenir une expression régulière (module `re`) : sur l’exemple de la fiche, la règle `0` devient `(aa|b)(ba|a(aa|b))`. Mais si une règle contient son propre numéro, ce remplacement ne s’arrête jamais. Pire : une règle du type « `X` suivi de `Y` autant de fois que de `X` » (même nombre des deux côtés) ne peut *pas du tout* s’écrire comme une expression régulière, car celles-ci ne savent pas compter.

    **L’idée de la fonction `fins`.** Plutôt que de deviner *où* s’arrête la partie reconnue par une règle, on renvoie *toutes* les possibilités. Sur l’exemple de la fiche, avec le mot `bbaa` : la règle `1` depuis l’indice `0` renvoie `[1]` (la lettre `b`) ; la règle `2` depuis l’indice `1` renvoie `[3]` (le morceau `ba`). Donc `fins(regles, ’0’, "bbaa", 0)` vaut `[3]` : le mot n’est pas reconnu en entier car $3 \neq 4$. Quand une règle a plusieurs alternatives, la liste peut contenir plusieurs positions ; une liste vide signifie « échec ».

## Approfondissement

!!! encadre "Outils Python : les ensembles (set) et all"

    Un **ensemble** est une collection sans doublon et sans ordre. On l’écrit entre accolades, on peut le construire par compréhension comme une liste, et réunir deux ensembles avec `|`. La fonction `all` renvoie `True` si *tous* les éléments d’une suite de booléens sont vrais.

    ```python
    debuts = {"a", "b"}
    fins = {"a", "ab"}
    mots = {d + f for d in debuts for f in fins}   # tous les "collages"
    print(mots)                     # {'aa', 'aab', 'ba', 'bab'} (ordre quelconque)
    print("ba" in mots)             # True : test d'appartenance tres rapide
    reunion = mots | {"bb"}         # reunion de deux ensembles
    mots |= {"aa"}                  # deja present : rien ne change
    print(len(mots))                # 4
    print(all(m in mots for m in ["aa", "ba"]))   # True
    print(all(m in mots for m in ["aa", "bb"]))   # False
    ```

    **Intérêt.** Le test `x in ensemble` prend un temps qui ne dépend pas de la taille de l’ensemble (contrairement à une liste, qu’il faut parcourir), et les doublons disparaissent d’eux-mêmes. Question : combien d’éléments a `{d + f for d in "ab" for f in "ab"}` ?

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Approfondissement 1 : une méthode par blocs, propre aux données <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-recherche-textuelle-aoc-1-6 }

Dans les vraies données, la règle `0` est `8 11`, et les règles `42` et `31` ne contiennent pas de cycle : chacune reconnaît un ensemble **fini** de mots, et ces mots ont tous la même longueur.

1.  À la main, sur l’exemple de test de la partie 2 : écrire l’ensemble des mots reconnus par `42` et par `31`. Découper `aaaabaabbb` et `baaaaaab` en blocs de deux lettres et dire, pour chaque bloc, à quelle règle il appartient.

2.  Avec la règle `0: 8 11` modifiée, montrer qu’un message est valide si et seulement s’il s’écrit « $p$ blocs de `42` suivis de $q$ blocs de `31` » avec $p > q \geq 1$. Et en partie 1 ?

3.  Écrire une fonction récursive `mots(regles, num)` qui renvoie l’ensemble des mots reconnus par une règle sans cycle.

    ??? pouce "Coup de pouce"

        Pour une alternative, partir de l’ensemble `{""}` (le mot vide) et, pour chaque sous-règle, coller à chaque début chacun des mots de la sous-règle.

    ??? pouce "Coup de pouce 2 (début de solution)"

        `possibles = {debut + fin for debut in possibles for fin in mots(regles, sous_regle)}` ; les ensembles obtenus pour les différentes alternatives sont réunis avec `|=`.

4.  Écrire `valide_par_blocs(message, m42, m31)` et retrouver le résultat de la partie 2. Pourquoi faut-il que les deux ensembles n’aient aucun mot commun ? Le vérifier sur vos données.

    ??? pouce "Coup de pouce"

        Compter le nombre `p` de blocs de tête qui sont dans `m42` ; tous les blocs restants doivent être dans `m31` (utiliser `all`).

5.  Comparer avec la fonction `fins` : vitesse, et généralité (que se passe-t-il si l’on change la règle `0` ?).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 2 : mémoïser la fonction `fins` <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-09-recherche-textuelle-aoc-1-7 }

Pour un message donné, la fonction `fins` peut être appelée plusieurs fois avec la même règle et la même position `i`.

1.  Sur l’exemple de test de la partie 2, avec les règles modifiées, expliquer pourquoi le calcul de `fins(regles, ’8’, message, 0)` appelle deux fois `fins(regles, ’42’, message, 0)`. Que se passe-t-il ensuite à la position 2, à la position 4…?

2.  Écrire `fins_memo(regles, num, message, i, memo)` qui range chaque résultat dans le dictionnaire `memo`, de clé `(num, i)`, et le réutilise s’il est déjà calculé. Vérifier qu’on obtient les mêmes réponses.

    ??? pouce "Coup de pouce"

        Le dictionnaire doit être **vide au début de chaque message** : un même couple `(num, i)` ne donne pas le même résultat pour deux messages différents.

3.  Combien de couples `(num, i)` différents au plus pour un message de longueur $n$ et $R$ règles ? Que peut-on en dire sur la complexité ?
